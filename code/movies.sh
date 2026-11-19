#!/bin/bash
# Four movies of spheroids settling under gravity, as jobs: prolate and oblate, two-body and full body.
#
#   bash movies.sh            submit       DRY=1 bash movies.sh      print only
#
# Each movie: solid bodies = MFS (fine clouds) at every step; black outlines = the trained operator.
#   two-body   two particles side by side, one upright and one tilted 45 degrees; outline = far field + two-body model
#   full body  8 particles in a compact random cluster;       outline = far field + two-body + many-body model
# The camera falls with the particles, so the movie shows how they turn and move around each other.
# Output: movies/<name>.mp4 (or .gif when ffmpeg is not found) and movies/<name>.npz (the trajectories) next to this
# script.  Needs matplotlib in the Python environment; if it is missing the job still saves the .npz and says how to
# draw the movie from it afterwards.
set -eo pipefail
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd); ROOT=$(cd "$HERE/.." && pwd)
W=${NEMO_SPHEROID:-$ROOT/workspaces/spheroid}
M=data/final/models
mkdir -p "$ROOT/logs" "$ROOT/results/movies"
EXCL=${EXCL-$(sinfo -h -N -o %N 2>/dev/null | grep '^nal' | sort -u | paste -sd, - || true)}
job() {  # name, command
  if [ -n "${DRY:-}" ]; then echo "DRY   $1  cd $W && $2"; return 0; fi
  echo "sub   $1  job $(sbatch --parsable -J "$1" --output="$ROOT/logs/%x_%j.out" --chdir="$W" --gres=gpu:1 ${EXCL:+--exclude=$EXCL} \
      --mem=64G --time=3:59:00 --wrap="source $HERE/env.sh; module load FFmpeg 2>/dev/null || true; $2")"
}
for s in pro:prolateSpheroid obl:oblateSpheroid; do
  n=${s%%:*}; k=${s##*:}
  job 1A_U_movie_${n}_two_body "python $HERE/movie.py --kinds $k --case pair --contact 1.3 --tilt 0 45 --dt 0.1 --steps 1500 --acc fine \
      --pair $M/pair_$n.pt --out $ROOT/results/movies/${n}_two_body.mp4"
  job 2A_U_movie_${n}_full_body "python $HERE/movie.py --kinds $k --case cluster --N 8 --delta 0.3 --dt 0.1 --steps 1000 --acc fine \
      --pair $M/pair_$n.pt --nbody $M/nbody_$n.pt --out $ROOT/results/movies/${n}_full_body.mp4"
done
echo "when done: ls $ROOT/results/movies   (download the .mp4 / .gif files to watch them)"
