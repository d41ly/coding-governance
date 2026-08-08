#!/usr/bin/env bash
# check-protocol-parity.test.sh — the review protocol this repo RUNS ON must equal the one this kit
# SHIPS, modulo the declared install prefix. Exit 0 = in parity · 1 = drift · 2 = misconfigured.
#
#   bash tools/workflows/check-protocol-parity.test.sh            # assert parity
#   bash tools/workflows/check-protocol-parity.test.sh --render    # rewrite the shipped copy
#
# WHY THIS KIT OWNS IT. `tools/memory-tree/kit-dogfood-parity.test.sh` does exactly this job for the
# memory-tree kit's two documents, and the obvious move was to add a third pair to its list. That
# would hardcode a WORKFLOWS-kit path into the MEMORY-TREE kit's shipped gate: an adopter who installs
# memory-tree alone would get a gate demanding a file their tree has no reason to contain, and the
# memory-tree kit would carry knowledge of a kit it does not depend on. Each kit gates its own pairs.
#
# THE SUBSTITUTION is the same one, for the same reason: the kit ships TOOL-ROOT-RELATIVE paths
# (`workflows/…`, `hooks/…`) because an adopter chooses where the kits live, and this repo installs
# them under `tools/`. Only that leading prefix may differ; anything else is drift.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "protocol-parity: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
MEMORY_ROOT=memory
[ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"
M="$MEMORY_ROOT"
HERE="$(cd "$(dirname "$0")" && pwd)"
# Both sides through the same `cd … && pwd`: under MSYS one directory has two spellings, and a raw
# prefix strip across those flavors silently yields an absolute path.
ROOT_N="$(cd "$ROOT" && pwd)"
KITREL=${HERE#"$ROOT_N"/}
[ "$KITREL" = "$HERE" ] && { echo "protocol-parity: cannot locate this kit inside the repo ($HERE vs $ROOT_N)"; exit 2; }
TOOLROOT=${KITREL%/*}; TOOLROOT=${TOOLROOT%/}
PREFIX=""; [ -n "$TOOLROOT" ] && [ "$TOOLROOT" != "$KITREL" ] && PREFIX="$TOOLROOT/"

LIVE="$M/guides/REVIEW-PROTOCOL.md"
SHIP="$KITREL/REVIEW-PROTOCOL.template.md"
MODE="${1:---check}"

norm() { if [ -n "$PREFIX" ]; then sed -e 's/\r$//' -e "s|$PREFIX||g" "$1"; else sed -e 's/\r$//' "$1"; fi; }

[ -f "$LIVE" ] || { echo "protocol-parity: missing live copy $LIVE"; exit 1; }
case "$MODE" in
  --render) norm "$LIVE" > "$SHIP"; echo "protocol-parity: rendered $SHIP from $LIVE"; exit 0 ;;
  --check) ;;
  *) echo "usage: $0 [--check|--render]"; exit 2 ;;
esac
[ -f "$SHIP" ] || { echo "protocol-parity: missing shipped copy $SHIP"; exit 1; }
if ! diff -q <(norm "$LIVE") <(sed 's/\r$//' "$SHIP") >/dev/null; then
  echo "protocol-parity: DRIFT — $SHIP does not match $LIVE (after stripping the '$PREFIX' install prefix)"
  diff <(norm "$LIVE") <(sed 's/\r$//' "$SHIP") | head -30 | sed 's/^/    /'
  echo "    fix: bash $KITREL/check-protocol-parity.test.sh --render"
  exit 1
fi
# A parity check that compares two empty files passes. Assert the population is real: the live copy
# must carry the rule this document exists to state, or "in parity" means "both are wrong".
grep -qF 'verify-stage agents TOTAL' "$LIVE" \
  || { echo "protocol-parity: $LIVE no longer states the hard cap — parity over the wrong content"; exit 1; }
echo "protocol-parity: in parity — $SHIP == $LIVE (modulo the '$PREFIX' prefix)"
