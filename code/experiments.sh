#!/bin/bash
# The physics experiments (experiments.py) as jobs, for prolate and oblate spheroids, with the trained models of the
# spheroid workspace.  Each job also draws its movie.
#
#   bash experiments.sh              submit all          DRY=1 bash experiments.sh       print only
#   bash experiments.sh orbits three     some experiments: orbits three cloud cloudmfs diffusion spinners fibre
#
# Output: <repo>/results/experiments/EXP_*.md (numbers + conditions), .json, .npz, .mp4.
set -eo pipefail
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd); ROOT=$(cd "$HERE/.." && pwd)
W=${NEMO_SPHEROID:-$ROOT/workspaces/spheroid}
M=data/final/models; OUT=$ROOT/results/experiments
mkdir -p "$ROOT/logs" "$OUT"
EXCL=${EXCL-$(sinfo -h -N -o %N 2>/dev/null | grep '^nal' | sort -u | paste -sd, - || true)}
WANT=" ${*:-orbits three cloud cloudmfs diffusion spinners fibre} "
job() {  # cell, experiment key, name, experiments.py arguments, result stem (for the movie; "" = no movie)
  [[ "$WANT" == *" $2 "* ]] || return 0
  local name="$1_U_exp_$3" cmd="python $HERE/experiments.py $4 --results $OUT"
  [ -n "$5" ] && cmd+=" && python $HERE/movie.py --render $OUT/$5.npz --out $OUT/$5.mp4"
  if [ -n "${DRY:-}" ]; then echo "DRY   $name  cd $W && $cmd"; return 0; fi
  echo "sub   $name  job $(sbatch --parsable -J "$name" --output="$ROOT/logs/%x_%j.out" --chdir="$W" --gres=gpu:1 ${EXCL:+--exclude=$EXCL} \
      --mem=64G --time=3:59:00 --wrap="source $HERE/env.sh; module load FFmpeg 2>/dev/null || true; $cmd")"
}
for s in pro:prolateSpheroid obl:oblateSpheroid; do
  n=${s%%:*}; k=${s##*:}
  two="--kinds $k --pair $M/pair_$n.pt --name $n"
  full="$two --nbody $M/nbody_$n.pt"; [ -f "$W/$M/nself_$n.pt" ] && full+=" --nself $M/nself_$n.pt"
  job 1A orbits   "orbits_$n"    "orbits $two"                                   "EXP_orbits_$n"
  job 2A three    "three_$n"     "three $full"                                   "EXP_three_$n"
  job 2A cloud    "cloud_$n"     "cloud $full --N 200"                           "EXP_cloud_${n}_N200"
  job 2A cloudmfs "cloudmfs_$n"  "cloud $full --N 30 --truth-max 30 --steps 300" "EXP_cloud_${n}_N30"
  job 2A diffusion "diffusion_$n" "diffusion $full --truth"                      ""
  job 2A spinners "spinners_$n"  "spinners $full"                                "EXP_spinners_$n"
done
job 2A fibre "fibre_pro" "fibre --kinds prolateSpheroid --pair $M/pair_pro.pt --nbody $M/nbody_pro.pt --name pro" "EXP_fibre_pro"
echo "when done: ls $OUT ; cat $OUT/EXP_*.md"
