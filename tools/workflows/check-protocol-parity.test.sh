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
# THE POINTER, per RULE. This arm used to freeze the literal cap as a digit, on the reasoning that a
# digit-free paraphrase is the drift it exists to catch. That reasoning was right and its instrument
# was the weaker half of it: a document that RESTATES the number is itself a second answer, and a
# reader holding a stale copy cannot tell which of the two binds. The property that needs protecting
# is unchanged — a protocol stating a bound it does not say how to READ is a protocol an agent
# cannot check itself against.
#
# PER RULE and not per document. This protocol states TWO bounds in two sections, and
# memory/gotchas/concurrency-is-not-a-budget.md exists because conflating them was a real defect; one
# predicate over "the document" would let either section lose its pointer while the other carried the
# gate. Each section that states a bound names the resolver within its OWN body.
#
# This is the POINTER-SHAPE half and deliberately only that half: it asserts each section NAMES its
# resolver, never that the named file resolves anything. The second half — that the pointed-at
# carrier is one the hook actually reads — belongs to the commit that makes the hook read it, and no
# such commit exists yet.
_p_bad=0
for _sec in 'The hard cap' 'Concurrency'; do
  # `next` DROPS the heading from the body. Without it this arm graded the heading line, and both
  # headings already contain the literal `agent-cap.js` -- so `grep -qF` passed on the heading no
  # matter what the body said, and the arm could not detect the body losing its pointer. A predicate
  # that reads its own subject line is this repo's vacuity class wearing the shape of a section scan.
  _body=$(awk -v want="$_sec" '
      /^## / { inb = (index($0, want) > 0) ? 1 : 0; next }
      inb { print }' "$LIVE")
  if [ -z "$_body" ]; then
    echo "protocol-parity: $LIVE has no '## $_sec ...' section, so this pointer arm would pass by finding nothing"
    _p_bad=1; continue
  fi
  printf '%s\n' "$_body" | grep -qF 'agent-cap.js' \
    || { echo "protocol-parity: $LIVE's '$_sec' section states a bound without naming the file that RESOLVES it (expected 'agent-cap.js' inside that section) — a bound an agent cannot look up"; _p_bad=1; }
done
[ "$_p_bad" = 0 ] || exit 1
echo "protocol-parity: in parity — $LIVE == $SHIP rendered for '$KITREL'"
