#!/bin/bash
# Stress and bulk properties as jobs: the stresslet / strain truth of pairs, the two-body stress model, and the
# periodic-box numbers (hindered settling, self-diffusion, viscosity against volume fraction, settling instability).
#
#   bash stress.sh                 submit everything        DRY=1 bash stress.sh        print only
#   bash stress.sh pro obl         some cases:  pro obl (spheroid workspace)  tri (triaxial workspace, 1:2:3)
#   STAGES="bulk streamers" bash stress.sh        some stages: data train bulk streamers
#
# data (8 jobs per case) -> train (waits for data) -> bulk (waits for train).  bulk uses the mobility models that
# run.sh trained (pair_X.pt, nbody_X.pt, nself_X.pt) if they exist, else the far field alone; streamers needs nothing.
# Output: <workspace>/data/stress/models/stress_X.md and <repo>/results/bulk/BULK_X.md, STREAM_X_N*.md
set -eo pipefail
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd); ROOT=$(cd "$HERE/.." && pwd)
WS=${NEMO_SPHEROID:-$ROOT/workspaces/spheroid}; WT=${NEMO_TRIAXIAL:-$ROOT/workspaces/triaxial}
OUT=$ROOT/results/bulk; mkdir -p "$ROOT/logs" "$OUT"
EXCL=${EXCL-$(sinfo -h -N -o %N 2>/dev/null | grep '^nal' | sort -u | paste -sd, - || true)}
STAGES=" ${STAGES:-data train bulk streamers} "
N=${N:-8192}; WORKERS=${WORKERS:-8}
sub() {  # name, workspace, dependency ("" = none), command
  if [ -n "${DRY:-}" ]; then echo "DRY   $1  cd $2 && $4" >&2; echo 0; return 0; fi
  sbatch --parsable -J "$1" --output="$ROOT/logs/%x_%j.out" --chdir="$2" --gres=gpu:1 ${EXCL:+--exclude=$EXCL} ${3:+--dependency=afterok:$3} \
      --mem=64G --time=3:59:00 --wrap="source $HERE/env.sh; $4"
}
for c in ${*:-pro obl tri}; do
  case $c in
    pro) W=$WS; K=prolateSpheroid; CELL=1A; FULL=2A; M=data/final/models/pair_pro.pt; NB=data/final/models/nbody_pro.pt; NS=data/final/models/nself_pro.pt ;;
    obl) W=$WS; K=oblateSpheroid;  CELL=1A; FULL=2A; M=data/final/models/pair_obl.pt; NB=data/final/models/nbody_obl.pt; NS=data/final/models/nself_obl.pt ;;
    tri) W=$WT; K=triaxial_123;    CELL=3A; FULL=4A; M=data/final/models/pair_t123.pt; NB=data/final/models/nbody_t123.pt; NS=data/final/models/nself_t123.pt ;;
    *) echo "unknown case $c"; exit 1 ;;
  esac
  S=data/stress/models/stress_$c.pt; dep=""
  if [[ "$STAGES" == *" data "* ]]; then
    ids=""
    for w in $(seq 0 $((WORKERS - 1))); do
      id=$(sub "${CELL}_U_stressdata_${c}_$w" "$W" "" "python $HERE/stress.py data --shapes $K $K --tag $c --n $N --worker $w --num-workers $WORKERS")
      ids+="${ids:+:}$id"
    done
    dep=$ids; echo "sub   ${CELL}_U_stressdata_$c  jobs $ids"
  fi
  if [[ "$STAGES" == *" train "* ]]; then
    dep=$(sub "${CELL}_U_stress_$c" "$W" "$dep" "python $HERE/stress.py train --sets $c --out $S"); echo "sub   ${CELL}_U_stress_$c  job $dep"
  fi
  if [[ "$STAGES" == *" bulk "* ]]; then
    models=""
    [ -f "$W/$M" ] && models+=" --pair $M"
    [ -f "$W/$M" ] && [ -f "$W/$NB" ] && models+=" --nbody $NB"
    [ -f "$W/$M" ] && [ -f "$W/$NB" ] && [ -f "$W/$NS" ] && models+=" --nself $NS"
    { [ -f "$W/$S" ] || [[ "$STAGES" == *" train "* ]]; } && models+=" --stress $S"
    echo "sub   ${FULL}_U_bulk_$c  job $(sub "${FULL}_U_bulk_$c" "$W" "$dep" "python $HERE/periodic.py bulk --kinds $K --name $c --results $OUT$models")"
  fi
  if [[ "$STAGES" == *" streamers "* ]]; then
    echo "sub   ${FULL}_U_streamers_$c  job $(sub "${FULL}_U_streamers_$c" "$W" "" "python $HERE/periodic.py streamers --kinds $K --name $c --N 200 --phi 0.01 --steps 1000 --results $OUT")"
  fi
done
echo "when done: cat $OUT/*.md $WS/data/stress/models/*.md $WT/data/stress/models/*.md"
