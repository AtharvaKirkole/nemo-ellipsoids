#!/bin/bash
# Run ONCE on the machine that holds the original workspaces, from inside this repository:
#     bash tools/pack_hpcc.sh [spheroid workspace] [triaxial workspace]
# Packs the MFS point clouds (data/points) and the trained models of both workspaces into points/ and models/,
# then commits and pushes them.  Files over 95 MB are split into parts (setup.sh joins them again).
set -eo pipefail
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
SPH=${1:-$HOME/pinn-stokes-ellipsoids}; TRI=${2:-$HOME/ellipsoids_2}
pack() {  # output tarball, base dir, list of paths relative to base (one per line, on stdin)
  local out=$1 base=$2 list; list=$(mktemp)
  cat > "$list"
  [ -s "$list" ] || { echo "nothing to pack for $out" >&2; rm -f "$list"; return 0; }
  tar czf "$out" -C "$base" -T "$list"; rm -f "$list"
  if [ "$(stat -c %s "$out")" -gt 99614720 ]; then split -b 90m -d "$out" "$out.part"; rm "$out"; fi
  echo "packed $(ls "$out"* | xargs -n1 basename | paste -sd' ') ($(du -ch "$out"* | tail -1 | cut -f1))"
}
for f in spheroid:$SPH triaxial:$TRI; do
  name=${f%%:*}; W=${f#*:}
  [ -d "$W/data/points" ] || { echo "no $W/data/points" >&2; exit 1; }
  rm -f "$ROOT/points/${name}_points.tar.gz"* "$ROOT/models/${name}_models.tar.gz"*
  (cd "$W/data/points" && find . -maxdepth 1 -type f \( -name 'b_*.txt' -o -name 's_*.txt' -o -name 'shapes.json' \) | sed 's#^\./##' | sort) \
      | pack "$ROOT/points/${name}_points.tar.gz" "$W/data/points"
  (cd "$W" && find data/final/models data/final_c/models data/stress/models -maxdepth 1 -type f \( -name '*.pt' -o -name '*.json' -o -name '*.md' \) 2>/dev/null | sort) \
      | pack "$ROOT/models/${name}_models.tar.gz" "$W"
done
cd "$ROOT"
git add -f points models
git commit -qm "MFS point clouds and trained models of both workspaces" && git push && git log --oneline -1
