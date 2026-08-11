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
TOOLROOT=${KITREL%/*}; [ "$TOOLROOT" = "$KITREL" ] && TOOLROOT=""
[ -z "$TOOLROOT" ] || TOOLROOT="$TOOLROOT/"   # "tools/" at a prefix, "" at a root install

LIVE="$M/guides/REVIEW-PROTOCOL.md"
SHIP="$KITREL/REVIEW-PROTOCOL.template.md"
MODE="${1:---check}"

# A RENDER, not a strip. The shipped template carries a brace-delimited TOOL_ROOT placeholder and
# this substitutes it, so what the gate grades is exactly what an adopter installs. The old form was
# an unanchored global `sed "s|tools/||g"` over the LIVE copy, which stripped every occurrence of
# `tools/` rather than a leading kit path, and left the SHIPPED template spelling a root install — so
# an adopter at a prefix installed a protocol document naming files they do not have.
render() { sed -e "s|{{TOOL_ROOT}}|$TOOLROOT|g" -e 's/\r$//' "$1"; }

[ -f "$LIVE" ] || { echo "protocol-parity: missing live copy $LIVE"; exit 1; }
case "$MODE" in
  --render) render "$SHIP" > "$LIVE"; echo "protocol-parity: rendered $LIVE from $SHIP"; exit 0 ;;
  --check) ;;
  *) echo "usage: $0 [--check|--render]"; exit 2 ;;
esac
[ -f "$SHIP" ] || { echo "protocol-parity: missing shipped copy $SHIP"; exit 1; }
if ! diff -q <(sed 's/\r$//' "$LIVE") <(render "$SHIP") >/dev/null; then
  echo "protocol-parity: DRIFT — $LIVE does not match $SHIP rendered for this install ('$KITREL')"
  diff <(sed 's/\r$//' "$LIVE") <(render "$SHIP") | head -30 | sed 's/^/    /'
  echo "    fix: bash $KITREL/check-protocol-parity.test.sh --render"
  exit 1
fi
# A surviving placeholder would ship a literal token into an adopter's protocol document, and the
# diff above cannot see it: a live copy rendered by the same broken substitution matches perfectly.
if render "$SHIP" | grep -q '{{[A-Z_]*}}'; then
  echo "protocol-parity: $SHIP still holds an unsubstituted placeholder after rendering:"
  render "$SHIP" | grep -n '{{[A-Z_]*}}' | head -5 | sed 's/^/    /'
  exit 1
fi
# A parity check that compares two empty files passes. Assert the population is real: the live copy
# must carry the rule this document exists to state, or "in parity" means "both are wrong".
#
# THE NUMBER, not the digit-free phrase. `verify-stage agents TOTAL` survives every edit that changes
# the cap — the live copy could read "≤50 verify-stage agents TOTAL", the shipped copy could be
# re-rendered to match, and both halves of this gate would go green over a document that no longer
# states the rule the hook enforces. The assertion has to be able to fail on the thing that matters.
grep -qF '≤5 verify-stage agents TOTAL' "$LIVE" \
  || { echo "protocol-parity: $LIVE no longer states the hard cap AT ITS NUMBER (expected the literal '≤5 verify-stage agents TOTAL') — parity over the wrong content"; exit 1; }
echo "protocol-parity: in parity — $LIVE == $SHIP rendered for '$KITREL'"
