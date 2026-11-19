#!/bin/bash
# Everything, end to end, for spheroids AND general ellipsoids, two-body AND full body: one script.
#
#   bash run.sh                      every case (below)
#   bash run.sh 1A_pro 3D            some cases
#   DRY=1 bash run.sh                print what would be submitted, submit nothing
#   LOCAL=1 bash run.sh 3A           no Slurm: run every step here, one after the other
#   SEEDS="0 1 2" bash run.sh 1C     + two more training seeds of the pair model (the spread of every pair number)
#   REDO="clusters rows nbody eval" bash run.sh 3D      do these stages again even though their outputs exist
#                                    (clusters: finish the missing ones; rows / nbody / eval: rebuild from scratch)
#   SMOKE=1 LOCAL=1 bash run.sh 3A   a tiny end-to-end run on coarse clouds (minutes, CPU): checks the whole chain
#   CUT=contact bash run.sh          the models with the learned range set by CONTACT FACTOR (< 4) instead of centre
#                                    distance: new pair data (any distance, contact factor up to 4.2), new models, in
#                                    data/final_c and results_c (nothing of the distance-cut runs is touched); jobs
#                                    are named <cell>_C_...; case 3C then also trains the prolate-oblate pairing
#
# Cases (cell = paper grid; every case also runs its full-body cell):
#   spheroid form   1A_pro 1A_obl (+2A)   1B (+2B)   1C (+2C)   1D (+2D)
#   triaxial form   3A (+4A)              3B (+4B)   3C (+4C)   3D (+4D)
#   A one shape     B many shapes, one per cluster     C shapes mixed in every cluster     D every shape and size mixed
#
# Stages per case, each skipped when its output already exists (so the script is resumable, and on a workspace that
# already holds data and models it only runs the evaluation):
#   pairs      MFS pair data: training sets, separate test sets (unseen seeds), unseen test pairings
#   pair       the two-body model (a chain of <= 3:59 jobs, resumable)
#   clusters   MFS mobility matrices of whole clusters (4 workers)
#   rows       many-body training rows from the clusters and the pair model
#   nbody      the many-body model (cross blocks)
#   selfrows   many-body training rows of the SELF blocks, from the same clusters
#   nself      the many-body self model (what keeps the operator positive definite)
#   ref        the first $NREF configurations of every test set solved again with the finer ($REF) clouds
#   eval       clouds, pair test, Fig. 3, Fig. 4, ring and pair dynamics, structural check, ceiling -- each with the
#              error of MFS itself under the same conditions -- then report.py -> results/REPORT.md
#
#   EVAL_ONLY=1 bash run.sh          use the trained models already in the workspaces (models/ of the repo, unpacked
#                                    by setup.sh): no training data, no clusters, no training -- only the test sets,
#                                    the MFS references and the evaluation
#
# Workspaces.  A workspace is a directory with data/points (clouds + shapes.json); data/final is written there.  The
# two forms use two workspaces because their pair data share names but not ranges:
#   NEMO_SPHEROID  (default <repo>/workspaces/spheroid)      NEMO_TRIAXIAL  (default <repo>/workspaces/triaxial)
# Results go to <repo>/results/<case>/, whatever the workspace; job logs to <repo>/logs.
set -eo pipefail
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd); ROOT=$(cd "$HERE/.." && pwd)
SPH=${NEMO_SPHEROID:-$ROOT/workspaces/spheroid}
TRI=${NEMO_TRIAXIAL:-$ROOT/workspaces/triaxial}
ACC=${ACC:-fine}; REF=${REF:-Xfine}; NREF=${NREF:-256}
D=data/final; M=$D/models; RES=$ROOT/results; ALLJ=""
CUT=${CUT:-distance}; JT=U
if [ "$CUT" = contact ]; then D=data/final_c; M=$D/models; RES=$ROOT/results_contact; JT=C; fi
PY="python $HERE"
if [ -n "${SMOKE:-}" ]; then
  ACC=coarse; REF=medium; NREF=8; D=data/smoke; M=$D/models; RES=$ROOT/results_smoke
  if [ "$CUT" = contact ]; then D=data/smoke_c; M=$D/models; RES=$ROOT/results_smoke_contact; fi
  N_TRAIN=48; N_TEST=16; STEPS=150; WIDTH=16; CL="--plan smoke --per 2"; NB="--epochs 3 --width 16 --bands 4 --batch 256 --eval-every 1"; NS="--epochs 3 --width 16 --bands 4 --batch 64 --eval-every 1"
  F3="--N 10 --phi 0.05 0.1 --seeds 2 --ref-seeds 1"; F4="--N 6 10 --phi 0.05 --seeds 1 --ref-seeds 1"
  DYN="--steps 4"; PDYN="--steps 4"; CHK="--N 6"; CEIL="--N 8 --phi 0.05 --seeds 1"; PD="--N 6 10 --phi 0.05 0.1 --seeds 3 --max-pairs 8"
else
  CL=""; NB=""; NS=""; F3="--ref-seeds 1"; F4="--N 50 100 200 300 --phi 0.05 0.1 0.15 0.2 --seeds 5 --ref-seeds 1 --ref-max-n 100"
  DYN=""; PDYN="--contact 1.5 --steps 1500"; CHK=""; CEIL=""; PD=""
fi
mkdir -p "$ROOT/logs" "$RES"
EXCL=${EXCL-$(sinfo -h -N -o %N 2>/dev/null | grep '^nal' | sort -u | paste -sd, - || true)}
GPU="--gres=gpu:1${EXCL:+ --exclude=$EXCL}"
queued=$(squeue -h -u "$USER" -o "%j" 2>/dev/null | tr -d ' ' || true)
declare -A JOB
W=""; FORM=""; RCUT=""; TAG=""; OUT=""

have() { case $1 in /*) [ -e "$1" ] ;; *) [ -e "$W/$1" ] ;; esac; }
redo() { [[ " ${REDO:-} " == *" $1 "* ]]; }
deps() { local d="" x; for x in "$@"; do if [ -n "$x" ]; then d+=":$x"; fi; done; echo "${d#:}"; }

sub() {  # name, time, mem, dependency ids ("" = none), command -> OUT = job id ("" when nothing was queued)
  local name="${1%%_*}_${JT}_${1#*_}" time=$2 mem=$3 dep=$4 cmd=$5
  OUT=""
  if [ -n "${LOCAL:-}" ]; then echo "run   $name" >&2; (cd "$W" && eval "$cmd") >&2; return 0; fi
  if grep -qx "$name" <<<"$queued"; then OUT=$(squeue -h -u "$USER" -n "$name" -o %i | head -1); return 0; fi
  if [ -n "${DRY:-}" ]; then echo "DRY   $name  [$time, $mem${dep:+, after $dep}]  cd $W && $cmd" >&2; OUT="DRY"; return 0; fi
  OUT=$(sbatch --parsable -J "$name" --output="$ROOT/logs/%x_%j.out" --chdir="$W" $GPU ${dep:+--dependency=afterany:$dep} \
      --mem=$mem --time=$time --wrap="source $HERE/env.sh; $cmd")
  echo "sub   $name  job $OUT" >&2
  ALLJ+=":$OUT"
}
chain() {  # stage, name, links, mem, dependency ids, done file, command -> OUT = id of the last link ("" if already done)
  local stage=$1 name=$2 n=$3 mem=$4 dep=$5 done_file=$6 cmd=$7 k guard
  OUT=""
  if have "$done_file" && ! redo "$stage"; then return 0; fi
  [ -n "${LOCAL:-}" ] && n=1
  for ((k = 1; k <= n; k++)); do
    guard="if [ -e '$done_file' ]; then echo 'already done: $done_file'; else $cmd; fi"
    if redo "$stage" && [ "$k" = 1 ]; then guard="rm -f '$done_file'; $cmd"; fi
    sub "${name}_$k" 3:59:00 $mem "$dep" "$guard"
    dep=$OUT
  done
}
cloud() { [ -f "$W/data/points/b_$1_$2.txt" ]; }
prange() { if [ "$CUT" = contact ]; then echo "--cmax 4.2"; else echo "--r-max $RCUT"; fi; }   # which pairs are solved
pairs() {  # cell, shape a, shape b, n, suffix ("" or _test) -> TAG; JOB[W|TAG] = job id
  local cell=$1 a=$2 b=$3 n=$4 tag="$2__$3$5" s
  TAG=$tag
  for s in $a $b; do cloud $s $ACC || { echo "missing cloud $W/data/points/b_${s}_$ACC.txt (shape $s)" >&2; exit 1; }; done
  if [ -z "${JOB[$W|$tag]+x}" ]; then
    chain pairs "${cell}_pairs_$tag" $((n > 4096 ? 2 : 1)) 32G "" "$D/pairs/${tag}_$ACC/shard_$(printf %04d $(((n - 1) / 1024))).npz" \
        "$PY/makedata.py pairs --out $D --acc $ACC --shapes $a $b --tag $tag --n $n $(prange) --time-budget 12600"
    JOB[$W|$tag]=$OUT
  fi
}
refpairs() {  # cell, a, b: the test set of this pairing again with the finer clouds, if both shapes have them
  local cell=$1 a=$2 b=$3 tag="$2__$3_test"
  OUT=""
  cloud $a $REF && cloud $b $REF || return 0
  if [ -z "${JOB[$W|$tag|ref]+x}" ]; then
    chain ref "${cell}_ref_$tag" 1 64G "${JOB[$W|$tag]}" "$D/pairs/${tag}_$REF/shard_0000.npz" \
        "$PY/makedata.py pairs --out $D --acc $REF --shapes $a $b --tag $tag --n $NREF $(prange)"
    JOB[$W|$tag|ref]=$OUT
  fi
  OUT=${JOB[$W|$tag|ref]}
}
evalj() {  # cell, name, links, mem, deps, result file (under the case's results), command
  local R=$RES/$CASE
  chain eval "$1_$2" $3 $4 "$5" "$R/$6" "$PY/evaluate.py $7 --data $D --acc $ACC --ref-acc $REF --results $R"
}

case_run() {  # cell, name, width, steps, "a:b:n ..." train, "a:b ..." unseen test pairings, kinds of the clusters,
              # cluster flags (--one-kind = B), kinds of the test suspensions (default: the cluster kinds)
  local cell=$1 name=$2 width=${WIDTH:-$3} steps=${STEPS:-$4} train=$5 test=$6 kinds=$7 cflags=${8:-} ekinds=${9:-$7}
  local sets="" tests="" d_train="" d_test="" a b n spec all=""
  for spec in $train; do
    IFS=: read -r a b n <<<"$spec"; n=${N_TRAIN:-$n}
    if [ -z "${EVAL_ONLY:-}" ]; then pairs $cell $a $b $n ""; sets+=" $TAG"; d_train=$(deps "$d_train" "${JOB[$W|$TAG]}"); fi
    pairs $cell $a $b ${N_TEST:-2048} _test; tests+=" $TAG"; d_test=$(deps "$d_test" "${JOB[$W|$TAG]}")
    refpairs $cell $a $b; d_test=$(deps "$d_test" "$OUT"); all+=" $a $b"
  done
  for spec in $test; do                                             # pairings never trained on
    IFS=: read -r a b <<<"$spec"
    pairs $cell $a $b ${N_TEST:-2048} _test; tests+=" $TAG"; d_test=$(deps "$d_test" "${JOB[$W|$TAG]}")
    refpairs $cell $a $b; d_test=$(deps "$d_test" "$OUT"); all+=" $a $b"
  done
  all=$(echo $all $kinds $ekinds | tr ' ' '\n' | awk '!s[$0]++' | paste -sd' ' -)
  local pm=$M/pair_$name.pt pj sd
  if [ -n "${EVAL_ONLY:-}" ]; then
    for f in $pm $M/nbody_$name.pt $M/nself_$name.pt; do have $f || { echo "EVAL_ONLY: missing model $W/$f (run setup.sh with the models)" >&2; exit 1; }; done
  fi
  chain pair "${cell}_pair_$name" 3 64G "$d_train" $pm \
      "$PY/train.py pair --form $FORM --cut $CUT --data $D --acc $ACC --sets$sets --width $width --steps $steps --out $pm"; pj=$OUT
  evalj $cell "clouds_$name" 1 32G "" CLOUDS.md "clouds --kinds $all"
  evalj $cell "test_$name" 1 64G "$(deps "$pj" "$d_test")" PAIR_pair_$name.md "pair --pair $pm --sets$tests"
  for sd in ${SEEDS:-0}; do                                         # more training seeds: the spread of every pair number
    [ "$sd" = 0 ] && continue
    chain pair "${cell}_pair_${name}_s$sd" 3 64G "$d_train" $M/pair_${name}_s$sd.pt \
        "$PY/train.py pair --form $FORM --cut $CUT --data $D --acc $ACC --sets$sets --width $width --steps $steps --seed $sd --out $M/pair_${name}_s$sd.pt"
    evalj $cell "test_${name}_s$sd" 1 64G "$(deps "$OUT" "$d_test")" PAIR_pair_${name}_s$sd.md "pair --pair $M/pair_${name}_s$sd.pt --sets$tests"
  done
  local fb=${cell/1/2}; fb=${fb/3/4}                                # the full-body cell of this case
  local cj="" w rj nj nm=$M/nbody_$name.pt
  for w in 0 1 2 3; do
    [ -n "${EVAL_ONLY:-}" ] && break
    # rows already built from these clusters: more clusters would not be used, unless the rows are rebuilt too
    if have "$D/nbody_rows/${name}_$ACC.npz" && ! redo clusters && ! redo rows; then break; fi
    chain clusters "${fb}_clusters_${name}_w$w" 2 128G "" "$D/clusters/${name}_$ACC/.done_w$w" \
        "$PY/makedata.py clusters --out $D --acc $ACC --kinds $kinds $cflags $CL --tag $name --num-workers 4 --worker $w --time-budget 12600 && touch $D/clusters/${name}_$ACC/.done_w$w"
    cj=$(deps "$cj" "$OUT")
  done
  [ -n "${EVAL_ONLY:-}" ] || chain rows "${fb}_rows_$name" 1 128G "$(deps "$pj" "$cj")" "$D/nbody_rows/${name}_$ACC.npz" \
      "$PY/makedata.py nbody-rows --out $D --acc $ACC --clusters $name --pair-model $pm"; rj=$OUT
  chain nbody "${fb}_nbody_$name" 3 128G "$rj" $nm "$PY/train.py nbody --rows $D/nbody_rows/${name}_$ACC.npz $NB --out $nm"; nj=$OUT
  local sm=$M/nself_$name.pt sj
  [ -n "${EVAL_ONLY:-}" ] || chain selfrows "${fb}_selfrows_$name" 1 128G "$(deps "$pj" "$cj")" "$D/self_rows/${name}_$ACC.npz" \
      "$PY/makedata.py self-rows --out $D --acc $ACC --clusters $name --pair-model $pm"; sj=$OUT
  chain nself "${fb}_nself_$name" 2 128G "$sj" $sm "$PY/train.py self --rows $D/self_rows/${name}_$ACC.npz $NS --out $sm"; sj=$OUT
  nj=$(deps "$pj" "$nj" "$sj")
  local mo="--kinds $ekinds --pair $pm --nbody $nm --nself $sm"
  evalj $fb "fig3_$name" 3 128G "$nj" SUSPENSION_${name}_fig3.md "suspension $mo --name ${name}_fig3 $F3"
  evalj $fb "fig4_$name" 3 128G "$nj" SUSPENSION_${name}_fig4.md "suspension $mo --name ${name}_fig4 $F4"
  evalj $fb "ring_$name" 1 64G "$nj" DYNAMICS_ring_$name.md "dynamics $mo --name $name --case ring $DYN"
  evalj $fb "pairdyn_$name" 1 64G "$nj" DYNAMICS_pair_$name.md "dynamics $mo --name $name --case pair $PDYN"
  evalj $fb "check_$name" 1 64G "$nj" CHECK_$name.md "check $mo --name $name $CHK"
  evalj $fb "pd_$name" 1 64G "$nj" PD_$name.md "pd $mo --name $name --sets$tests $PD"
  evalj $fb "ceiling_$name" 2 128G "$nj" CEILING_$name.md "ceiling $mo --name $name $CEIL"
}
same() { local n=$1 s out=""; shift; for s in "$@"; do out+=" $s:$s:$n"; done; echo "$out"; }

P=prolateSpheroid; O=oblateSpheroid; T=triaxial_123
S7="prolate_ar1p5 prolate_ar2 $P prolate_ar4 oblate_ar1p5 $O oblate_ar3"
SMIX="$P:$O:4096 prolate_ar2:$O:2048 prolate_ar4:oblate_ar3:2048 prolate_ar2:oblate_ar1p5:2048 prolate_ar1p5:oblate_ar3:2048 $P:prolate_ar2:2048 $O:oblate_ar3:2048 prolate_ar4:$O:2048 $P:oblate_ar1p5:2048"
SSIZED="${P}_x0p75:$P:2048 ${O}_x1p5:$O:2048 prolate_ar2_x1p5:prolate_ar2:2048 oblate_ar3_x0p75:oblate_ar3:2048 ${O}_x1p5:${P}_x0p75:2048 prolate_ar2_x1p5:$O:2048"
T6="$T triaxial_1p5_2 triaxial_1p5_3 triaxial_2_4 triaxial_2_5 triaxial_3_4"
TMIX="$T:$P:4096 $T:$O:4096 $T:triaxial_2_5:2048 $P:triaxial_2_5:2048 $P:$O:2048 $T:triaxial_1p5_2:2048 $T:triaxial_2_4:2048 $T:triaxial_3_4:2048 $O:triaxial_1p5_2:2048 $P:triaxial_2_4:2048 triaxial_2_5:triaxial_3_4:2048"
TSIZED="${T}_x0p75:$T:2048 ${O}_x1p5:$O:2048 ${P}_x1p25:$P:2048 triaxial_1p5_2_x1p5:triaxial_1p5_2:2048 ${T}_x0p75:$P:2048 ${O}_x1p5:$T:2048"

cases() {
  CASE=$1
  case $1 in 1*) W=$SPH; FORM=spheroid; RCUT=12 ;; 3*) W=$TRI; FORM=triaxial; RCUT=14 ;; *) echo "unknown case $1" >&2; exit 1 ;; esac
  [ -d "$W/data/points" ] || { echo "workspace $W has no data/points (set NEMO_SPHEROID / NEMO_TRIAXIAL)" >&2; exit 1; }
  mkdir -p "$W/$M"
  case $1 in
    1A_pro) case_run 1A pro 128 200000 "$P:$P:16384" "" "$P" ;;
    1A_obl) case_run 1A obl 128 200000 "$O:$O:16384" "" "$O" ;;
    1B) case_run 1B multi 128 400000 "$(same 4096 $S7)" "prolate_ar2p5:prolate_ar2p5 oblate_ar2p5:oblate_ar2p5 prolate_ar5:prolate_ar5" "$S7" --one-kind "prolate_ar2" ;;
    1C) case_run 1C mixed 128 400000 "$P:$P:8192 $O:$O:8192 $P:$O:8192" "" "$P $O" ;;
    1D) case_run 1D poly 256 600000 "$(same 4096 $S7) $SMIX $SSIZED" \
            "prolate_ar2:oblate_ar3 prolate_ar4:oblate_ar1p5 prolate_ar2p5:oblate_ar2p5 prolate_ar2p5_x1p25:prolate_ar2p5_x1p25 oblate_ar3_x0p75:prolate_ar2_x1p5 prolate_ar2p5_x1p25:$O" \
            "$S7 ${P}_x0p75 ${O}_x1p5 prolate_ar2_x1p5 oblate_ar3_x0p75" "" "$P $O prolate_ar2 oblate_ar3 ${O}_x1p5 ${P}_x0p75" ;;
    3A) case_run 3A t123 128 200000 "$T:$T:16384" "" "$T" ;;
    3B) case_run 3B multi 128 400000 "$(same 4096 $T6)" "triaxial_2p5_3p5:triaxial_2p5_3p5 triaxial_3_6:triaxial_3_6" "$T6" --one-kind "triaxial_2_4" ;;
    3C) if [ "$CUT" = contact ]; then case_run 3C mixed 128 400000 "$T:$T:8192 $P:$P:4096 $O:$O:4096 $T:$P:8192 $T:$O:8192 $P:$O:8192" "" "$T $P $O"
        else case_run 3C mixed 128 400000 "$T:$T:8192 $P:$P:4096 $O:$O:4096 $T:$P:8192 $T:$O:8192" "$P:$O" "$T $P $O"; fi ;;
    3D) case_run 3D poly 256 600000 "$(same 4096 $T6) $P:$P:4096 $O:$O:4096 $TMIX $TSIZED" \
            "$O:triaxial_2_5 triaxial_1p5_2:triaxial_3_4 $T:triaxial_2p5_3p5 $P:triaxial_3_6 ${O}_x1p5:triaxial_1p5_2_x1p5 ${T}_x0p75:triaxial_3_4 ${P}_x1p25:${P}_x1p25" \
            "$T6 $P $O ${T}_x0p75 ${O}_x1p5 ${P}_x1p25 triaxial_1p5_2_x1p5" "" "$T $P $O triaxial_1p5_2 ${T}_x0p75 ${O}_x1p5" ;;
    *) echo "unknown case $1" >&2; exit 1 ;;
  esac
}
for c in ${*:-1A_pro 1A_obl 1B 1C 1D 3A 3B 3C 3D}; do cases "$c"; done
# the combined report: after every job of this call (or right away when nothing had to be queued)
REPORT="python $HERE/report.py $RES"
if [ -n "${LOCAL:-}" ]; then (cd "$W" && $REPORT)
elif [ -n "${DRY:-}" ]; then echo "DRY   ALL_U_report  cd $W && $REPORT" >&2
else
  id=$(sbatch --parsable -J ALL_${JT}_report --output="$ROOT/logs/%x_%j.out" --chdir="$W" ${ALLJ:+--dependency=afterany:${ALLJ#:}} \
      --mem=8G --time=0:10:00 --wrap="source $HERE/env.sh; $REPORT")
  echo "sub   ALL_${JT}_report  job $id   ->  $RES/REPORT.md" >&2
fi
echo "queue: squeue -u \$USER --format='%.10i %.40j %.8T %.10M %R'" >&2
