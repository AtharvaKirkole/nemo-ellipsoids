# Environment for the jobs of this folder (sourced by run.sh from the workspace).
# Picks, in order: an already-live venv, $NEMO_VENV, <repo>/.venv, ./.venv.  Without a venv, the python on PATH.
# Needs torch with CUDA, numpy, scipy; nothing else.
_live=0
if [ -n "${VIRTUAL_ENV:-}" ]; then
  case "$(command -v python 2>/dev/null)" in "$VIRTUAL_ENV"/*) _live=1 ;; esac
fi
if [ "$_live" = 0 ]; then
  _repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
  for _c in "${NEMO_VENV:-}" "$_repo/.venv" "$PWD/.venv"; do
    if [ -n "$_c" ] && [ -f "$_c/bin/activate" ]; then set +u; source "$_c/bin/activate"; set -u; _live=1; break; fi
  done
fi
# CUDA toolkit for the MFS kernel (truth_mfs/mfs_cuda.py is compiled on first use by torch load_inline: needs nvcc,
# CUDA_HOME and ninja).  Without it every truth solve silently falls back to dense BatchedMFS (same answer, 60-100x
# slower).  On a cluster with Lmod the CUDA module is loaded below; elsewhere put nvcc on PATH yourself.
_ml() { if command -v module >/dev/null 2>&1; then module load "$@";
        elif [ -n "${LMOD_CMD:-}" ]; then eval "$("$LMOD_CMD" bash load "$@")"; else echo "no module command (LMOD_CMD unset)"; fi; }
if ! command -v nvcc >/dev/null 2>&1; then
  case $- in *u*) _u=1 ;; *) _u=0 ;; esac; set +u
  _log="${TMPDIR:-/tmp}/env_ml_$$.log"; : > "$_log"
  for _m in "CUDA/12.9.1" "CUDA/12.6.0" "CUDA/12.4.0" "CUDA/12.1.1" "CUDA"; do   # CUDA alone: GCC/12.3.0 is preloaded on ICER, GCC/14.3.0 conflicts with it
    echo "== module load $_m" >> "$_log"; _ml $_m >> "$_log" 2>&1
    command -v nvcc >/dev/null 2>&1 && break
  done
  command -v nvcc >/dev/null 2>&1 || { echo "[env] no nvcc after module load; last messages:"; tail -n 8 "$_log"; }
  rm -f "$_log"; [ "$_u" = 1 ] && set -u
fi
if [ -z "${CUDA_HOME:-}" ] && command -v nvcc >/dev/null 2>&1; then export CUDA_HOME="$(dirname "$(dirname "$(command -v nvcc)")")"; fi
echo "[env] nvcc $(command -v nvcc || echo none)  CUDA_HOME ${CUDA_HOME:-unset}  ninja $(command -v ninja || echo none)"
export TORCH_EXTENSIONS_DIR="${TORCH_EXTENSIONS_DIR:-$HOME/.cache/torch_extensions_pinn}"
export PYTHONUNBUFFERED=1 TORCH_COMPILE_DISABLE=1
echo "host $(hostname)  job ${SLURM_JOB_ID:-local}  python $(command -v python)"
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU ONLY')"
_here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python -c "import sys, torch; sys.path.insert(0, '$_here'); from truth_mfs import mfs_cuda; print('mfs cuda kernel', 'OK' if mfs_cuda.available() else 'UNAVAILABLE (' + str(mfs_cuda.error()) + ')') if torch.cuda.is_available() else None" 2>&1 | tail -1
