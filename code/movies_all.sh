#!/bin/bash
# Movies of every cell of the paper grid: rows A-D of both forms, a two-body movie (cells 1x / 3x) and a full-body
# movie (cells 2x / 4x) each, from the trained models of that row.  Every movie shows three views side by side in each
# frame: looking along x, along y, and along z (from above).  Solid bodies = MFS at every step (the truth); black
# outlines = the operator (positive definite, psd.py); lines = paths of the centres seen from the falling camera.
#
#   bash movies_all.sh                  submit all 22 movies as Slurm jobs (GPU, <= 3:59 each)
#   bash movies_all.sh 1B 4D            only these cells (a cell name selects its movies; 1B = both 1B movies)
#   bash movies_all.sh 2A_obl           only this movie
#   DRY=1 bash movies_all.sh            print the jobs, submit nothing
#   LOCAL=1 bash movies_all.sh 1C       run here, one after the other (needs a GPU to finish in reasonable time)
#   RENDER=1 bash movies_all.sh         draw every movie again from its saved trajectories (.npz): no solve;
#                                       one job on a GPU node (or here with LOCAL=1).  Also redraws the four older movies
#                                       of movies.sh in results/movies/ with the three views.
#   COMPARE=1 bash movies_all.sh        two more movies per movie, for comparison: <movie>_MFS.mp4 (MFS alone, the truth)
#                                       and <movie>_model.mp4 (the operator alone), same run, same camera and colours.
#                                       Drawn from the saved trajectories (no new solve): one small job per movie,
#                                       started after that movie's simulation job if it is still queued or running.
#
# Output: <repo>/results/movies_all/<movie>.mp4 (.gif without ffmpeg), <movie>.npz (trajectories), <movie>.png (a still from the
# middle of the run), and movies_all/INDEX.md (what each movie shows).  Logs: <repo>/logs/<cell>_U_movie_<movie>_<job>.out.
# Workspaces as run.sh (default <repo>/workspaces/spheroid and /triaxial): NEMO_SPHEROID (cells 1x, 2x), NEMO_TRIAXIAL (3x, 4x); models
# data/final/models/{pair,nbody,nself}_<case>.pt.  A movie whose models are missing is skipped with a message.
#
# Settings.  Two-body: two particles side by side at the same height (contact factor 1.3), dt 0.1, up to 1500 steps.
# Full body: 8 particles grown into a compact cluster (neighbours at contact factor 1.3), dt 0.1, up to 1000 steps;
# MFS runs for at most 2.5 h (TIME_BUDGET seconds) so that the drawing always fits in the job; the movie is then as
# long as MFS got.  Every run stops when two particles reach contact factor 1.05 (nothing is learned closer).
set -eo pipefail
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd); ROOT=$(cd "$HERE/.." && pwd)
SPH=${NEMO_SPHEROID:-$ROOT/workspaces/spheroid}
TRI=${NEMO_TRIAXIAL:-$ROOT/workspaces/triaxial}
OUT=$ROOT/results/movies_all; M=data/final/models
BUDGET=${TIME_BUDGET:-9000}
mkdir -p "$ROOT/logs" "$OUT"
EXCL=${EXCL-$(sinfo -h -N -o %N 2>/dev/null | grep '^nal' | sort -u | paste -sd, - || true)}
WANT=" $* "
P=prolateSpheroid; O=oblateSpheroid; T=triaxial_123

# ------------------------------------------------------------------------------------------------- the movies
# movie name | cell | workspace (sph / tri) | models of case | kind (two / full) | particles | pair tilts (deg) | what it shows
MOVIES=(
  "1A_pro|1A|sph|pro|two|$P $P|0 45|Two prolate spheroids 1:1:3, one upright and one tilted 45 deg: they turn through 90 deg and circle each other"
  "1A_obl|1A|sph|obl|two|$O $O|0 45|Two oblate spheroids 2:2:1, one lying flat and one tilted 45 deg: a tilted disk glides sideways as it falls"
  "1B_rods|1B|sph|multi|two|prolate_ar4 prolate_ar4|0 90|Slender rods 1:1:4, one upright and one lying: alone, the upright one would fall 1.29 times faster; together they interact as it pulls ahead"
  "1B_disks|1B|sph|multi|two|oblate_ar3 oblate_ar3|90 0|Thin disks 3:3:1, one edge-on and one flat: alone, the edge-on one would fall 1.22 times faster; together they interact as it pulls ahead"
  "1C_rod_disk|1C|sph|mixed|two|$P $O|0 45|A rod 1:1:3 upright beside a disk 2:2:1 tilted 45 deg: two different shapes in one pair"
  "1D_sizes|1D|sph|poly|two|${O}_x1p5 ${P}_x0p75|0 45|A large flat disk (3:3:1.5) beside a small tilted rod (0.75:0.75:2.25): shapes AND sizes differ"
  "2A_pro|2A|sph|pro|full|$P|-|8 prolate spheroids 1:1:3 in a compact cluster: it falls faster than one particle alone, and the particles turn"
  "2A_obl|2A|sph|obl|full|$O|-|8 oblate spheroids 2:2:1 in a compact cluster"
  "2B_rods|2B|sph|multi|full|prolate_ar4|-|8 slender rods 1:1:4 in a compact cluster"
  "2B_disks|2B|sph|multi|full|oblate_ar3|-|8 thin disks 3:3:1 in a compact cluster"
  "2C_mixed|2C|sph|mixed|full|$P $O|-|4 rods 1:1:3 and 4 disks 2:2:1 mixed in one cluster"
  "2D_poly|2D|sph|poly|full|${O}_x1p5 ${P}_x0p75 prolate_ar2_x1p5 oblate_ar3_x0p75 prolate_ar4 oblate_ar1p5 $P $O|-|8 different spheroids, aspect ratios 1:3 to 4:1, three sizes, in one cluster"
  "3A_t123|3A|tri|t123|two|$T $T|0 45|Two triaxial ellipsoids 1:2:3, one with its long axis upright and one tilted 45 deg"
  "3B_long|3B|tri|multi|two|triaxial_2_5 triaxial_2_5|0 90|Long flat bodies 1:2:5, one with its long axis upright and one lying"
  "3B_plates|3B|tri|multi|two|triaxial_3_4 triaxial_3_4|0 60|Plate-like bodies 1:3:4, one upright and one tilted 60 deg"
  "3C_mixed|3C|tri|mixed|two|$T $O|45 0|A 1:2:3 ellipsoid tilted 45 deg beside a flat disk 2:2:1: a triaxial and a spheroid in one pair"
  "3D_sizes|3D|tri|poly|two|${O}_x1p5 $T|0 45|A large flat disk (3:3:1.5) beside a 1:2:3 ellipsoid tilted 45 deg: shapes and sizes differ"
  "4A_t123|4A|tri|t123|full|$T|-|8 triaxial ellipsoids 1:2:3 in a compact cluster"
  "4B_long|4B|tri|multi|full|triaxial_2_5|-|8 long flat bodies 1:2:5 in a compact cluster"
  "4B_plates|4B|tri|multi|full|triaxial_3_4|-|8 plate-like bodies 1:3:4 in a compact cluster"
  "4C_mixed|4C|tri|mixed|full|$T $P $O|-|1:2:3 ellipsoids, rods 1:1:3 and disks 2:2:1 mixed in one cluster"
  "4D_poly|4D|tri|poly|full|${T}_x0p75 ${O}_x1p5 ${P}_x1p25 triaxial_1p5_2_x1p5 triaxial_2_5 triaxial_3_4 $P $O|-|8 different ellipsoids and spheroids, three sizes, in one cluster"
)

selected() {  # movie name, cell
  [ "$WANT" = "  " ] && return 0
  [[ "$WANT" == *" $1 "* || "$WANT" == *" $2 "* ]]
}
submit() {  # job name, workspace, gpu (1/0), time, command
  if [ -n "${DRY:-}" ]; then echo "DRY   $1  cd $2 && $5"; return 0; fi
  if [ -n "${LOCAL:-}" ]; then echo "run   $1"; (cd "$2" && eval "$5"); return 0; fi
  local gres=""; [ "$3" = 1 ] && gres="--gres=gpu:1 ${EXCL:+--exclude=$EXCL}"
  echo "sub   $1  job $(sbatch --parsable -J "$1" --output="$ROOT/logs/%x_%j.out" --chdir="$2" $gres --mem=64G --time=$4 \
      --wrap="source $HERE/env.sh; module load FFmpeg 2>/dev/null || true; $5")"
}

write_index() {  # the list of movies, with the MFS-only and model-only versions when they are made
  {
    echo "# Movies of every cell"
    echo
    echo "Three views in every frame: looking along x, along y, and along z (from above).  Solid = MFS (the truth, fine clouds);"
    echo "black outline = the trained operator of that row (positive definite); lines = paths seen from the falling camera."
    echo "Two-body: far field + two-body model.  Full body: + many-body model (+ self model).  Made by \`movies_all.sh\`."
    echo "MFS alone / model alone: the same run drawn with only the truth, or only the operator (\`COMPARE=1\`), same camera."
    echo
    echo "| movie | MFS alone | model alone | cell | particles | what it shows |"
    echo "|---|---|---|---|---|---|"
    for m in "${MOVIES[@]}"; do
      IFS='|' read -r name cell ws cs kind shapes tilt what <<<"$m"
      echo "| [$name]($name.mp4) | [MFS](${name}_MFS.mp4) | [model](${name}_model.mp4) | $cell | $shapes | $what |"
    done
  } > "$OUT/INDEX.md"
}

# ------------------------------------------------------------------------------------------------- MFS alone, model alone
if [ -n "${COMPARE:-}" ]; then
  write_index
  n=0
  for m in "${MOVIES[@]}"; do
    IFS='|' read -r name cell ws cs kind shapes tilt what <<<"$m"
    selected "$name" "$cell" || continue
    sim="${cell}_U_movie_${name#*_}"
    W=$SPH; [ "$ws" = tri ] && W=$TRI                 # run in the movie's workspace: its shapes.json registers the shapes
    if [ -f "$OUT/${name}_MFS.mp4" ] && [ -f "$OUT/${name}_model.mp4" ] && [ -z "${REDO:-}" ]; then
      echo "done  $name: ${name}_MFS.mp4 and ${name}_model.mp4 exist (REDO=1 to draw them again)" >&2
      continue
    fi
    dep=$(squeue -h -u "$USER" -n "$sim" -o %i 2>/dev/null | head -1 || true)
    if [ -z "$dep" ] && [ ! -f "$OUT/$name.npz" ] && [ -z "${DRY:-}" ]; then
      echo "skip  $name: its simulation job $sim is not queued and $OUT/$name.npz does not exist (did it fail? see logs/${sim}_*.out)" >&2
      continue
    fi
    cmd="test -f $OUT/$name.npz || { echo 'no $OUT/$name.npz: the simulation job did not finish'; exit 1; }; "
    cmd+="python $HERE/movie.py --render $OUT/$name.npz --only mfs --out $OUT/${name}_MFS.mp4 --still 0.5 --title '$cell: $what'; "
    cmd+="python $HERE/movie.py --render $OUT/$name.npz --only model --out $OUT/${name}_model.mp4 --still 0.5 --title '$cell: $what'"
    if [ -n "${DRY:-}" ]; then echo "DRY   ${sim}_cmp  ${dep:+[after job $dep]}  cd $W && $cmd"
    elif [ -n "${LOCAL:-}" ]; then echo "run   ${sim}_cmp"; (cd "$W" && eval "$cmd")
    else
      # a GPU node like every other job: on the CPU-only (amr) nodes this PyTorch build dies with "Illegal instruction"
      echo "sub   ${sim}_cmp  job $(sbatch --parsable -J "${sim}_cmp" --output="$ROOT/logs/%x_%j.out" --chdir="$W" --gres=gpu:1 ${EXCL:+--exclude=$EXCL} \
          --mem=16G --time=2:00:00 ${dep:+--dependency=afterany:$dep} --wrap="source $HERE/env.sh; module load FFmpeg 2>/dev/null || true; $cmd")${dep:+  (after the simulation, job $dep)}"
    fi
    n=$((n + 1))
  done
  echo "$n comparison jobs.  When done: ls $OUT/*_MFS.mp4 $OUT/*_model.mp4 ; the list is in $OUT/INDEX.md"
  exit 0
fi

# ------------------------------------------------------------------------------------------------- redraw only
if [ -n "${RENDER:-}" ]; then
  cmd=""
  for m in "${MOVIES[@]}"; do
    IFS='|' read -r name cell ws cs kind shapes tilt what <<<"$m"
    selected "$name" "$cell" || continue
    [ -f "$OUT/$name.npz" ] || { echo "skip  $name: no $OUT/$name.npz yet" >&2; continue; }
    W=$SPH; [ "$ws" = tri ] && W=$TRI
    cmd+="(cd $W && python $HERE/movie.py --render $OUT/$name.npz --out $OUT/$name.mp4 --still 0.5 --title '$cell: $what'); "
  done
  if [ "$WANT" = "  " ]; then
    for f in "$ROOT"/results/movies/*.npz; do
      [ -f "$f" ] && cmd+="(cd $SPH && python $HERE/movie.py --render $f --out ${f%.npz}_3views.mp4 --still 0.5); "
    done
  fi
  [ -n "$cmd" ] || { echo "nothing to redraw"; exit 0; }
  submit ALL_U_movie_redraw "$HERE" 1 3:59:00 "$cmd"
  exit 0
fi

# ------------------------------------------------------------------------------------------------- simulate + draw
write_index

n=0
for m in "${MOVIES[@]}"; do
  IFS='|' read -r name cell ws cs kind shapes tilt what <<<"$m"
  selected "$name" "$cell" || continue
  W=$SPH; [ "$ws" = tri ] && W=$TRI
  [ -d "$W/data/points" ] || { echo "skip  $name: workspace $W has no data/points (set NEMO_SPHEROID / NEMO_TRIAXIAL)" >&2; continue; }
  for s in $shapes; do
    [ -f "$W/data/points/b_${s}_fine.txt" ] || { echo "skip  $name: no fine cloud for $s in $W" >&2; continue 2; }
  done
  [ -f "$W/$M/pair_$cs.pt" ] || { echo "skip  $name: no $W/$M/pair_$cs.pt" >&2; continue; }
  models="--pair $M/pair_$cs.pt"
  if [ "$kind" = two ]; then
    run="--case pair --contact 1.3 --tilt $tilt --dt 0.1 --steps 1500"
  else
    [ -f "$W/$M/nbody_$cs.pt" ] || { echo "skip  $name: no $W/$M/nbody_$cs.pt" >&2; continue; }
    models+=" --nbody $M/nbody_$cs.pt"
    [ -f "$W/$M/nself_$cs.pt" ] && models+=" --nself $M/nself_$cs.pt"
    run="--case cluster --N 8 --delta 0.3 --seed 3 --dt 0.1 --steps 1000 --time-budget $BUDGET"
  fi
  submit "${cell}_U_movie_${name#*_}" "$W" 1 3:59:00 \
      "python $HERE/movie.py --shapes $shapes $run --acc fine $models --still 0.5 --title '$cell: $what' --out $OUT/$name.mp4"
  n=$((n + 1))
done
echo "$n movies.  When done: ls $OUT ; the list is in $OUT/INDEX.md"
