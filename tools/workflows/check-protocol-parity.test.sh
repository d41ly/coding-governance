#!/usr/bin/env bash
# check-protocol-parity.test.sh — every artifact this kit RENDERS must equal its template rendered
# for this install. Exit 0 = in parity · 1 = drift · 2 = misconfigured.
#
#   bash tools/workflows/check-protocol-parity.test.sh            # assert parity
#   bash tools/workflows/check-protocol-parity.test.sh --render    # (re)write every rendered copy
#   ... --tracked-only    with either mode: SKIP, by name, a pair whose live copy is absent AND
#                         untracked, so the run refreshes what this install holds and creates nothing
#
# WHY THIS KIT OWNS IT. `tools/memory-tree/kit-dogfood-parity.test.sh` does exactly this job for the
# memory-tree kit's two documents, and the obvious move was to add a third pair to its list. That
# would hardcode a WORKFLOWS-kit path into the MEMORY-TREE kit's shipped gate: an adopter who installs
# memory-tree alone would get a gate demanding a file their tree has no reason to contain, and the
# memory-tree kit would carry knowledge of a kit it does not depend on. Each kit gates its own pairs.
#
# THE PAIRS, declared once in `PAIRS` below. The review protocol this repo RUNS ON, the unattended
# BUILD HARNESS, and — since TOOL-aRepatriatedFork-7 — the review and drift-audit harnesses, which
# render only so a repo that LOWERS the fan-out cap in `.agent-cap.conf` receives harnesses its own
# hook admits, instead of a hand-kept fork of each. The build harness joined this list when it stopped shipping verbatim:
# apply writes an engine file's bytes unchanged, so every install path it spelled arrived in a tree
# installed at another prefix naming files that tree does not have — the driver, the bug-class
# checklist, the sub-workflow it awaits and the child it hands the caller. A workflow script has no
# filesystem at run time, so it cannot derive those paths itself. Rendering at install is the one
# derivation it can have, and the owner chose it on 2026-09-12 over having each caller pass the paths
# in. `kit.toml` declares both pairs `rendered` and names `--render --tracked-only` as the entry's
# `[[regenerate]]` argv, so an update re-renders every pair this install already holds unless
# GOVKIT_RERENDER=0 is exported. With GOVKIT_RERENDER=0 `update` declines that block and NAMES the
# decline, yet it still prints each moved render's row as `re-rendered` although no render ran, and
# this leg, wherever a bar wires it, is what reds the stale copy.
#
# WHY THE REGENERATE CREATES NOTHING (round 2, R2-3). govkit runs that argv with its output captured,
# prints one `ran` line, and rows nothing the argv writes. A render mode that created a missing live
# copy therefore installed a second review protocol into a consumer that keeps its own extract on
# purpose, and no line anywhere named the file. Creating a live copy is an install decision, so it
# stays with the hand `--render` a fresh install runs; `--tracked-only` refreshes and skips out loud.
#
# FOUR TOKENS, and each one is DERIVED here rather than typed:
#   KIT_DIR          this kit's directory, repo-relative — the harness's own siblings live in it
#   TOOL_ROOT        the directory the kits sit in, with a trailing slash; empty at a root install
#   MEMORY_TREE_DIR  the directory holding the memory-tree kit's `gotchas.py`
#   FANOUT_CAP       the fan-out cap for this checkout, as the agent-cap hook ANSWERS it (`--print-cap`)
# The third is NOT derivable from the second. Both adopters measured when this was written install
# the memory-tree kit FLAT, directly in their tool root, so `TOOL_ROOT` plus `memory-tree/` names a
# file neither of them has. It is PROBED instead: the first TRACKED of the nested and the flat
# spelling wins. It never guesses, because a guessed path renders a checklist command that runs
# nothing and reads as a clean one. Neither being tracked SKIPS, out loud and by name, only the pair
# whose template carries the token, so an install without the memory-tree kit still renders and
# grades the protocol; an override naming nothing tracked is still a refusal.
#
# WHAT THIS DOES NOT CHECK. It compares each render against its template and asserts no placeholder
# survives. It does NOT prove a rendered path RESOLVES: `TOOL_ROOT` plus `unattended/` is taken on
# the kit-layout convention, and only `MEMORY_TREE_DIR` is asserted to exist. The harness's own
# suite, `unattended-build.test.sh`, holds the class arm that every path the harness emits is
# tracked, and it is a kit self-test that no boundary runs.
set -u
MODE=--check; TRACKED_ONLY=0
for _a in "$@"; do
  case "$_a" in
    --check|--render) MODE=$_a ;;
    --tracked-only) TRACKED_ONLY=1 ;;
    *) echo "usage: $0 [--check|--render] [--tracked-only]"; exit 2 ;;
  esac
done

# THE KIT'S OWN LOCATION, BY A LOGICAL WALK TO THE NEAREST `.git`. This used to strip the repo root
# off the kit dir as two path STRINGS, and under MSYS one directory has two spellings — git reports
# `C:/Users/…/Temp/x` while a caller standing in `/tmp/x` reports that — so the strip no-opped and
# the script refused a kit that was plainly inside the repo. The walk compares nothing: it builds
# the relative path from basenames and stops at the first `.git`, which is a FILE in a linked
# worktree, hence `-e`. The unattended adopter's walk, copied rather than invented.
HERE="$(cd "$(dirname "$0")" && pwd)"
KIT_ROOT=""; KITREL=""; _p="$HERE"
while : ; do
  _parent="$(dirname "$_p")"
  [ "$_parent" = "$_p" ] && break
  KITREL="$(basename "$_p")${KITREL:+/$KITREL}"
  if [ -e "$_parent/.git" ]; then KIT_ROOT="$_parent"; break; fi
  _p="$_parent"
done
[ -n "$KIT_ROOT" ] || { echo "protocol-parity: the kit at $HERE is not inside a git repository"; exit 2; }
cd "$KIT_ROOT" || exit 2
git rev-parse --show-toplevel >/dev/null 2>&1 || { echo "protocol-parity: not a git repo"; exit 2; }
MEMORY_ROOT=memory
[ -f .memory-tree.conf ] && . ./.memory-tree.conf
M="$MEMORY_ROOT"
TOOLROOT=${KITREL%/*}; [ "$TOOLROOT" = "$KITREL" ] && TOOLROOT=""
[ -z "$TOOLROOT" ] || TOOLROOT="$TOOLROOT/"   # "tools/" at a prefix, "" at a root install

# The pairs: `<live copy>|<template>`, both repo-relative. The render of each template is the live
# copy's ENTIRE expected content.
PAIRS="$M/guides/REVIEW-PROTOCOL.md|$KITREL/REVIEW-PROTOCOL.template.md
$KITREL/unattended-build.js|$KITREL/unattended-build.template.js
$KITREL/tier2-review.js|$KITREL/tier2-review.template.js
$KITREL/drift-audit-code.js|$KITREL/drift-audit-code.template.js
$KITREL/drift-audit-state.js|$KITREL/drift-audit-state.template.js"

# FANOUT_CAP, THE FOURTH TOKEN — TOOL-aRepatriatedFork-7 S7. ANSWERED BY THE HOOK, never parsed here
# (closing review round 1 residual b): this used to re-read `.agent-cap.conf` with a sed of its own,
# which matched nothing on a BOM-led line and rendered cap-5 harnesses under a hook enforcing 4. The
# sibling gate's `--print-cap` locates the hook and relays its answer for this checkout, so the value
# rendered is the value enforced. A refusal stops here as the hook denies there, because a harness
# rendered at a cap its own hook will not admit is exactly the fork this token retires.
if ! FANOUT_CAP=$(bash "$HERE/check-verifier-fanout.sh" --print-cap 2>&1); then
  echo "protocol-parity: the agent-cap hook would not answer the effective fan-out cap:"
  printf '%s\n' "$FANOUT_CAP" | sed 's/^/  /'
  echo "  Nothing was rendered or graded."
  exit 2
fi
case "$FANOUT_CAP" in
  [1-9]) ;;
  *) echo "protocol-parity: the agent-cap hook answered '$FANOUT_CAP' for the fan-out cap, not a digit 1-9. Nothing was rendered or graded."; exit 2 ;;
esac

check_tracked() { git ls-files --error-unmatch -- ":(literal)$1" >/dev/null 2>&1; }

# MEMORY_TREE_DIR — the probe, then what an unanswered probe costs. The OVERRIDE is an environment
# variable and it is a HAND-INSTALL channel only: the gate leg runs this file with no environment of
# its own, so a tree that needs the override on its bar has to export it there too. That is the
# drift-audit adopter's recorded limit for its own sibling override, met again rather than solved.
# An override is asserted exactly as a probe answer is, because a wrong answer typed by a person
# runs nothing either.
#
# WARN WHEN ABSENT, REFUSE WHEN MISPLACED, and only for the pair whose template carries the token.
# This kit requires agent-cap and nothing else, so an install with no memory-tree kit is legal, and
# in one nothing tracks a `gotchas.py`. The probe used to exit 2 before any pair was graded, so that
# install lost `REVIEW-PROTOCOL.md` as well: the document stating the concurrency cap could be
# neither rendered nor graded, over a harness only the unattended kit runs (round 1, F3). An unset
# probe with nothing to find now SKIPS the pairs that need it, by name and out loud. An override that
# names nothing tracked is still a refusal, because that is a person's wrong answer, not an absence.
MTD=""; MTD_SKIP=""
if [ -n "${MEMORY_TREE_DIR:-}" ]; then
  _mtd=${MEMORY_TREE_DIR%/}
  if check_tracked "$_mtd/gotchas.py"; then MTD="$_mtd"
  else
    echo "protocol-parity: MEMORY_TREE_DIR is set to '$MEMORY_TREE_DIR', and '$_mtd/gotchas.py' is not"
    echo "  tracked in this repo. The harness would render a checklist command naming a file that does"
    echo "  not exist. Point it at the directory that holds the memory-tree kit's gotchas.py."
    exit 2
  fi
else
  for _c in "${TOOLROOT}memory-tree/gotchas.py" "${TOOLROOT}gotchas.py"; do
    if check_tracked "$_c"; then MTD=$(dirname "$_c"); break; fi
  done
  [ -n "$MTD" ] || MTD_SKIP="neither ${TOOLROOT}memory-tree/gotchas.py nor ${TOOLROOT}gotchas.py is tracked in this repo"
fi
# AN UNSUPPORTED CHARACTER IS A REFUSAL. Both values land inside a single-quoted JS string in the
# harness and inside a shell command an agent runs, so a quote ends the string early and a space
# splits the command. The set is a path's, and no install measured so far needs more.
case "$KITREL/$MTD" in
  *[!A-Za-z0-9._/+@-]*)
    echo "protocol-parity: the kit path '$KITREL' or MEMORY_TREE_DIR '$MTD' holds a character outside"
    echo "  [A-Za-z0-9._/+@-]. Both are interpolated into a JS string literal and a shell command, where"
    echo "  a quote ends the string and a space splits the command. Nothing was written."
    exit 2 ;;
esac

# A RENDER, not a strip, and no `sed`. Parameter substitution with a QUOTED replacement treats `&`,
# `|` and `\` in a value as themselves; `sed` would read the first two as syntax, and the override
# above is a value a person types. `$( )` strips every trailing newline, hence the `X` sentinel, and
# `cat` exits the substitution itself because a substitution reports its LAST command's status.
# Only a CR that ENDS a line is dropped, which is what the `sed 's/\r$//'` this replaced did.
render() { # template -> stdout
  local out
  out=$( cat "$1" || exit 1; printf X ) || return 1
  out=${out%X}
  out=${out//$'\r\n'/$'\n'}; out=${out%$'\r'}
  out=${out//\{\{KIT_DIR\}\}/"$KITREL"}
  out=${out//\{\{TOOL_ROOT\}\}/"$TOOLROOT"}
  out=${out//\{\{MEMORY_TREE_DIR\}\}/"$MTD"}
  out=${out//\{\{FANOUT_CAP\}\}/"$FANOUT_CAP"}
  printf '%s' "$out"
}
read_lf() { sed 's/\r$//' "$1"; }

# EVERY TEMPLATE THIS KIT SHIPS IS A PAIR. A template with no pair renders nowhere, and its live
# copy — if anything writes one — is graded by nobody. Asserted over the tracked set, so a new
# template reds here the day it lands rather than the day somebody notices its render drifted.
_unpaired=""
# Captured FIRST and fed from a variable: a loop reading a heredoc that holds a command substitution
# is the shape the shell-hygiene leg bans, because its reader can wait on EOF forever under MSYS.
_tpls=$(git ls-files -- "$KITREL/*.template.*")
while IFS= read -r _t; do
  [ -n "$_t" ] || continue
  case "
$PAIRS
" in *"|$_t
"*) ;; *) _unpaired="$_unpaired $_t" ;; esac
done <<EOF
$_tpls
EOF
if [ -n "$_unpaired" ]; then
  echo "protocol-parity: a template this kit ships renders to nothing this script grades:$_unpaired"
  echo "  add its pair to PAIRS and a \`rendered\` rule to kit.toml, or it ships an artifact nobody checks"
  exit 1
fi

TMPD=$(mktemp -d) || exit 2
trap 'rm -rf "$TMPD"' EXIT
bad=0; i=0; skipped=" "; nskip=0; skipped_live=" "
while IFS='|' read -r LIVE SHIP; do
  [ -n "$LIVE" ] || continue
  i=$((i+1))
  [ -f "$SHIP" ] || { echo "protocol-parity: missing shipped copy $SHIP"; bad=1; continue; }
  # --tracked-only: A LIVE COPY THIS INSTALL NEVER TOOK IS NOT CREATED, and not graded either. Absent
  # from the worktree AND from the index is the only case: a tracked copy somebody deleted is still
  # this install's, and a present untracked one is somebody's render to refresh.
  if [ "$TRACKED_ONLY" = 1 ] && [ ! -e "$LIVE" ] && ! check_tracked "$LIVE"; then
    echo "protocol-parity: SKIP $LIVE — it is absent and untracked, and --tracked-only refreshes only"
    echo "  what this install already holds, so this pair was neither rendered nor graded. To install"
    echo "  it, run bash $KITREL/check-protocol-parity.test.sh --render and commit what it writes."
    skipped="$skipped$i "; skipped_live="$skipped_live$LIVE "; nskip=$((nskip+1)); continue
  fi
  # THE SKIP, per pair and out loud. It names what went ungraded and what would grade it, because a
  # skip that reads as a pass is indistinguishable from coverage.
  if [ -n "$MTD_SKIP" ] && grep -qF '{{MEMORY_TREE_DIR}}' "$SHIP"; then
    echo "protocol-parity: SKIP $LIVE — its template names the memory-tree kit's gotchas.py, and"
    echo "  $MTD_SKIP, so this pair was neither rendered nor graded$([ -f "$LIVE" ] && echo " (the live copy that exists was NOT checked)")."
    echo "  If that kit is installed somewhere else, set MEMORY_TREE_DIR=<the directory holding"
    echo "  gotchas.py> and re-run. A guessed path is a checklist command that runs nothing."
    skipped="$skipped$i "; skipped_live="$skipped_live$LIVE "; nskip=$((nskip+1)); continue
  fi
  if ! render "$SHIP" > "$TMPD/$i"; then
    echo "protocol-parity: the render of $SHIP FAILED — the template could not be read"; bad=1; continue
  fi
  [ -s "$TMPD/$i" ] || { echo "protocol-parity: the render of $SHIP is EMPTY, and an empty file matches an empty file"; bad=1; continue; }
  # A surviving placeholder would ship a literal token into an adopter's tree, and the diff below
  # cannot see it: a live copy rendered by the same broken substitution matches perfectly.
  if grep -q '{{[A-Z_]*}}' "$TMPD/$i"; then
    echo "protocol-parity: $SHIP still holds an unsubstituted placeholder after rendering:"
    grep -n '{{[A-Z_]*}}' "$TMPD/$i" | head -5 | sed 's/^/    /'
    bad=1; continue
  fi
  if [ "$MODE" = --render ]; then
    continue
  fi
  if [ ! -f "$LIVE" ]; then
    echo "protocol-parity: missing live copy $LIVE"
    echo "    fix: bash $KITREL/check-protocol-parity.test.sh --render"
    bad=1; continue
  fi
  if ! diff -q <(read_lf "$LIVE") "$TMPD/$i" >/dev/null; then
    echo "protocol-parity: DRIFT — $LIVE does not match $SHIP rendered for this install ('$KITREL')"
    diff <(read_lf "$LIVE") "$TMPD/$i" | head -30 | sed 's/^/    /'
    echo "    fix: bash $KITREL/check-protocol-parity.test.sh --render"
    bad=1
  fi
done <<EOF
$PAIRS
EOF
[ "$i" -gt 0 ] || { echo "protocol-parity: PAIRS resolved to nothing, so this run graded nothing"; exit 1; }

# --render WRITES ONLY WHEN EVERY PAIR RENDERED CLEAN. A half-written set is two vintages of one
# kit, and the check that follows would report the half nobody wrote as drift somewhere else.
# A MISSING live copy is created: an update that lands this kit fresh has none to overwrite.
if [ "$MODE" = --render ]; then
  [ "$bad" = 0 ] || { echo "protocol-parity: nothing was written"; exit 1; }
  i=0
  while IFS='|' read -r LIVE SHIP; do
    [ -n "$LIVE" ] || continue
    i=$((i+1))
    case "$skipped" in *" $i "*) continue ;; esac
    mkdir -p "$(dirname "$LIVE")" && cp "$TMPD/$i" "$LIVE" || { echo "protocol-parity: could not write $LIVE"; exit 1; }
    echo "protocol-parity: rendered $LIVE from $SHIP"
  done <<EOF
$PAIRS
EOF
  exit 0
fi
[ "$bad" = 0 ] || exit 1

LIVE="$M/guides/REVIEW-PROTOCOL.md"
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
#
# A PROTOCOL PAIR --tracked-only SKIPPED has no live copy to read, and this arm says so rather than
# redding an install that never took the document or passing by reading nothing.
_p_bad=0; _secs='The hard cap
Concurrency'
case "$skipped_live" in
  *" $LIVE "*) echo "protocol-parity: the pointer arm over $LIVE did NOT run — that pair was skipped above"; _secs="" ;;
esac
while IFS= read -r _sec; do
  [ -n "$_sec" ] || continue
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
done <<EOF
$_secs
EOF
[ "$_p_bad" = 0 ] || exit 1
if [ "$nskip" -gt 0 ]; then
  echo "protocol-parity: in parity — $((i-nskip)) rendered pair(s) match their templates for '$KITREL'; $nskip pair(s) SKIPPED, each named above"
else
  echo "protocol-parity: in parity — $i rendered pair(s) match their templates for '$KITREL' (MEMORY_TREE_DIR '$MTD')"
fi
