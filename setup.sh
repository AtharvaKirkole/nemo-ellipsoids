#!/bin/bash
# Unpacks the MFS point clouds into the two workspaces (workspaces/spheroid, workspaces/triaxial).
#     bash setup.sh            clouds only: a full reproduction (everything is generated and trained again)
#     bash setup.sh --models   clouds + our trained models: then run.sh skips training (see README, EVAL_ONLY=1)
set -eo pipefail
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
unpack() {  # tarball (maybe split into .partNN), destination
  local t=$1 dest=$2
  mkdir -p "$dest"
  if [ -f "$t" ]; then tar xzf "$t" -C "$dest"
  elif ls "$t".part* >/dev/null 2>&1; then cat "$t".part* | tar xz -C "$dest"
  else echo "missing $t (has tools/pack_hpcc.sh been run?)" >&2; exit 1; fi
}
for name in spheroid triaxial; do
  unpack "$ROOT/points/${name}_points.tar.gz" "$ROOT/workspaces/$name/data/points"
  echo "workspaces/$name: $(ls "$ROOT/workspaces/$name/data/points" | grep -c '^b_') clouds"
  if [ "${1:-}" = --models ]; then
    unpack "$ROOT/models/${name}_models.tar.gz" "$ROOT/workspaces/$name"
    echo "workspaces/$name: $(find "$ROOT/workspaces/$name/data" -name '*.pt' | wc -l) trained models"
  fi
done
