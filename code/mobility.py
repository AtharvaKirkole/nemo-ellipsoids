"""The assembled mobility operator for N ellipsoids (any registered shapes, one per particle), dense, float64.

    op = Operator(load_pair("pair.pt"), load_nbody("nbody.pt"))
    U = op.apply(pos, quats, shapes, F)                 # (N, 6[, k]) velocities for loads F
    M = op.grand_M(pos, quats, shapes, mode="full")     # (6N, 6N)

    M_tt = M_iso(shape_t, R_t) + sum_s f_s(t, s)  [+ f_self(t)]        isolated particle + two-body self corrections
                                                                       [+ many-body self correction, mode "full"]
    M_ts = far(t, s)                                    r >= r_cut     12-Stokeslet far field (farfield.py)
         = (1 - w) far + w f_t  [+ f_nb]                r <  r_cut     pair model [+ many-body correction]
    (r and r_cut in units of the pair's length l = sqrt(l_t l_s): pair.py)

mode "far"   every pair by the far field, isolated self blocks: the ellipsoid analogue of RPY (the baseline)
     "pair"  + the two-body model
     "full"  + the many-body correction f_nb of the cross blocks (needs the nbody model) and, when a self model is
             given, of the self blocks (nbody.py SelfModel: what keeps the operator positive definite)

M is symmetric by construction in every mode (reciprocal far field, swap-averaged networks, symmetrised self blocks).
`two_body` is the one code path for the operator AND for the labels of f_nb (makedata.py), and `neighbours`
(nbody.py) the one neighbour selection, so the many-body model is always applied to what it was trained on.
Dense = O(N^2) pairs and a (6N)^2 matrix: accuracy studies up to a few thousand particles.
"""
from __future__ import annotations

import numpy as np
import torch

import pair as P
from farfield import far_blocks
from geometry import clearance_torch, quat_to_matrix
from nbody import neighbours
from truth import iso_mobility

MODES = ("far", "pair", "full")


class Operator:
    def __init__(self, pair_model=None, nbody_model=None, acc: str = "fine", device: str | None = None,
                 pair_chunk: int = 20000, nb_chunk: int = 2048, self_model=None):
        self.dev = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))
        self.pair = pair_model.double().to(self.dev).eval() if pair_model is not None else None
        self.nbody = nbody_model.double().to(self.dev).eval() if nbody_model is not None else None
        if self.nbody is not None:
            assert self.pair is not None and (self.pair.cut != "distance" or self.nbody.pair_cutoff <= self.pair.r_cut), \
                "f_nb corrects pairs inside the pair model's range"
            assert self.nbody.form is self.pair.form, "the pair and many-body models must be of the same form"
        self.nself = self_model.double().to(self.dev).eval() if self_model is not None else None
        self.acc, self.pair_chunk, self.nb_chunk = acc, int(pair_chunk), int(nb_chunk)
        self._iso: dict = {}

    # ------------------------------------------------------------------------------------------- pieces
    def geometry(self, pos, quats, shapes):
        """-> X (N, 3), R (N, 3, 3), descriptors, kinds (unique shape names), kid (N,) index into kinds."""
        f64 = dict(dtype=torch.float64, device=self.dev)
        X = torch.as_tensor(np.asarray(pos, dtype=np.float64), **f64)
        R = torch.as_tensor(quat_to_matrix(quats), **f64)
        shapes = list(shapes)
        kinds = list(dict.fromkeys(shapes))
        kid = torch.as_tensor([kinds.index(s) for s in shapes], device=self.dev)
        return X, R, P.describe(shapes, R), kinds, kid

    def iso_blocks(self, shapes, R: torch.Tensor) -> torch.Tensor:
        """Isolated self blocks in the lab frame, (N, 6, 6)."""
        for s in set(shapes):
            if s not in self._iso:
                self._iso[s] = torch.as_tensor(iso_mobility(s, self.acc), dtype=torch.float64, device=self.dev)
        G = torch.zeros(len(R), 6, 6, dtype=torch.float64, device=self.dev)
        G[:, :3, :3], G[:, 3:, 3:] = R, R
        return G @ torch.stack([self._iso[s] for s in shapes]) @ G.transpose(-1, -2)

    def far(self, X, R, kinds, kid, t, s) -> torch.Tensor:
        d = X[s] - X[t]
        out = torch.zeros(len(t), 6, 6, dtype=torch.float64, device=self.dev)
        for a in range(len(kinds)):
            for b in range(len(kinds)):
                m = (kid[t] == a) & (kid[s] == b)
                if bool(m.any()):
                    out[m] = far_blocks(kinds[a], kinds[b], d[m], R[t[m]], R[s[m]])
        return out

    @torch.no_grad()
    def two_body(self, X, R, desc, kinds, kid, t, s, learned: bool = True):
        """Ordered pairs (t, s) -> physical cross blocks (n, 6, 6), self corrections (n, 6, 6), clearances (n,)
        (the clearance is only computed where a model reads it; 0 elsewhere)."""
        d = X[s] - X[t]
        far = self.far(X, R, kinds, kid, t, s)
        zero = torch.zeros_like(far)
        g = torch.zeros(len(t), dtype=torch.float64, device=self.dev)
        if not learned or self.pair is None:
            return far, zero, g
        rn = d.norm(dim=-1)
        r = rn / P.pair_length(P.take(desc, t), P.take(desc, s))                  # in units of the pair length
        # pairs that can be inside the learned range: by distance, or (contact cut) by the bound c >= r / (a_max,t + a_max,s)
        cand = r < self.pair.r_cut if self.pair.cut == "distance" else rn < self.pair.r_cut * (desc["amax"][t] + desc["amax"][s])
        need = cand | (r < self.nbody.pair_cutoff) if self.nbody is not None else cand     # f_nb reads the clearance too
        idx = torch.nonzero(need)[:, 0]
        if len(idx):
            g[idx] = clearance_torch(desc["A"][t[idx]], desc["A"][s[idx]], d[idx])
        w = torch.zeros_like(g)
        ci = torch.nonzero(cand)[:, 0]
        if len(ci):
            w[ci] = self.pair.weight(d[ci], g[ci], P.take(desc, t[ci]), P.take(desc, s[ci]))
        cross = (1.0 - w)[:, None, None] * far
        near = torch.nonzero(w > 0)[:, 0]
        if len(near):
            tn, sn = t[near], s[near]
            c, sf = self.pair(d[near], g[near], P.take(desc, tn), P.take(desc, sn))
            cross[near] += c / P.SIX_PI
            zero[near] = sf / P.SIX_PI
        return cross, zero, g

    @torch.no_grad()
    def many_body(self, X, desc, t, s, g) -> torch.Tensor:
        """f_nb blocks (n, 6, 6), physical units, for ordered pairs inside the many-body pair cutoff."""
        out = []
        for i in range(0, len(t), self.nb_chunk):
            tt, ss = t[i:i + self.nb_chunk], s[i:i + self.nb_chunk]
            pt, ps = P.take(desc, tt), P.take(desc, ss)
            nbr, nD, mask, nz = neighbours(X, desc["D"], 0.5 * (X[tt] + X[ss]), torch.stack([tt, ss], 1),
                                           self.nbody.neighbor_cutoff * P.pair_length(pt, ps), desc["z"])
            out.append(self.nbody(X[ss] - X[tt], g[i:i + self.nb_chunk], pt, ps, nbr, nD, mask, nz) / P.SIX_PI)
        return torch.cat(out) if out else torch.zeros(0, 6, 6, dtype=torch.float64, device=self.dev)

    @torch.no_grad()
    def many_self(self, X, desc) -> torch.Tensor:
        """Many-body corrections of the self blocks (N, 6, 6), physical units."""
        out = []
        for i in range(0, len(X), self.nb_chunk):
            idx = torch.arange(i, min(len(X), i + self.nb_chunk), device=self.dev)
            pt = P.take(desc, idx)
            nbr, nD, mask, nz = neighbours(X, desc["D"], X[idx], idx[:, None], self.nself.neighbor_cutoff * P.length(pt), desc["z"])
            out.append(self.nself(pt, nbr, nD, mask, nz) / P.SIX_PI)
        return torch.cat(out)

    # ------------------------------------------------------------------------------------------- the operator
    @torch.no_grad()
    def grand_M(self, pos, quats, shapes, mode: str = "full") -> torch.Tensor:
        assert mode in MODES, mode
        assert mode == "far" or self.pair is not None, f"mode {mode} needs a pair model"
        assert mode != "full" or self.nbody is not None, "mode full needs a many-body model"
        X, R, desc, kinds, kid = self.geometry(pos, quats, shapes)
        N = len(X)
        selfsum = self.iso_blocks(list(shapes), R)
        M = torch.zeros(N, 6, N, 6, dtype=torch.float64, device=self.dev)
        ii, jj = torch.meshgrid(torch.arange(N, device=self.dev), torch.arange(N, device=self.dev), indexing="ij")
        T, S = ii[ii != jj], jj[ii != jj]
        nb_t, nb_s, nb_g = [], [], []
        for i in range(0, len(T), self.pair_chunk):
            t, s = T[i:i + self.pair_chunk], S[i:i + self.pair_chunk]
            cross, self_, g = self.two_body(X, R, desc, kinds, kid, t, s, learned=mode != "far")
            M[t, :, s, :] = cross
            selfsum.index_add_(0, t, self_)
            if mode == "full":
                keep = (X[s] - X[t]).norm(dim=-1) / P.pair_length(P.take(desc, t), P.take(desc, s)) < self.nbody.pair_cutoff
                nb_t.append(t[keep]), nb_s.append(s[keep]), nb_g.append(g[keep])
        if mode == "full" and nb_t:
            t, s, g = torch.cat(nb_t), torch.cat(nb_s), torch.cat(nb_g)
            if len(t):
                M[t, :, s, :] += self.many_body(X, desc, t, s, g)
        if mode == "full" and self.nself is not None:
            selfsum = selfsum + self.many_self(X, desc)
        ar = torch.arange(N, device=self.dev)
        M[ar, :, ar, :] = selfsum
        return M.reshape(6 * N, 6 * N)

    @torch.no_grad()
    def apply(self, pos, quats, shapes, F, mode: str = "full") -> np.ndarray:
        F = np.asarray(F, dtype=np.float64)
        Fm = torch.as_tensor(F, device=self.dev).reshape(6 * len(pos), -1)
        return (self.grand_M(pos, quats, shapes, mode) @ Fm).cpu().numpy().reshape(F.shape)
