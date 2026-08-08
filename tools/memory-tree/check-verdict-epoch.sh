#!/usr/bin/env bash
# check-verdict-epoch.sh — the kit version DATES the engine's verdicts, so it must move when they do.
#
#   bash tools/memory-tree/check-verdict-epoch.sh [<base>]     # default base: the mainline merge-base
#
# Exit 0 = the constant is honest for this range · 1 = the engine moved and the constant did not ·
# 2 = misconfigured.
#
# WHY. `hygiene-parity.test.sh` derives its baseline floor from the first commit introducing the
# CURRENT `KIT_MEMORY_TREE_VERSION`, on the stated ground that the constant marks when the verdicts
# last changed. Measured, that ground gave way: this repo changed check 5's selector, the §9 rev
# range and the index set across three commits while the constant sat at 1.5, so the floor pointed at
# a commit from before those changes and the parity harness accepted a baseline it could not legally
# compare against. The floor was not wrong about WHERE to look; the constant was wrong about WHEN.
#
# THE RULE. Over `<base>..HEAD`, if any added or removed line in the engine is not a comment and not
# blank, `KIT_MEMORY_TREE_VERSION` must differ between the two ends.
#
# IT OVER-COUNTS, DELIBERATELY. A rename or a whitespace-only refactor changes no verdict and still
# demands a bump. That is the safe direction: the cost is three lines and a `--render`, and the
# alternative — deciding from a diff whether a verdict moved — is the judgement call that produced
# the stale constant in the first place. A line whose first non-space character is `#` cannot change
# what `sh` or `awk` does, so the exemption cannot hide a behaviour change.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "verdict-epoch: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

ENGINE=tools/memory-tree/check-memory-hygiene.sh
[ -f "$ENGINE" ] || { echo "verdict-epoch: $ENGINE is missing — this gate reads the engine's own source"; exit 2; }

BASE="${1:-}"
if [ -z "$BASE" ]; then
  DEF="${GOV_DEFAULT_BRANCH:-main}"
  BASE=$(git merge-base "origin/$DEF" HEAD 2>/dev/null || git merge-base "$DEF" HEAD 2>/dev/null || true)
fi
# No resolvable base — a shallow clone, a fresh init, a detached probe. SKIP LOUDLY: silence here
# would be indistinguishable from "the constant is fine", which is the failure this gate exists for.
if [ -z "$BASE" ]; then
  echo "verdict-epoch: skip — no mainline base to compare against (shallow clone or no default branch)"
  exit 0
fi
git cat-file -e "$BASE^{commit}" 2>/dev/null || { echo "verdict-epoch: base '$BASE' is not a commit in this repo"; exit 2; }

# Non-comment, non-blank added/removed lines in the engine. `git diff -U0` so context lines cannot be
# mistaken for changes; the `+++`/`---` file headers are excluded by requiring a second character.
moved=$(git diff -U0 "$BASE"..HEAD -- "$ENGINE" \
  | grep -E '^[+-]' | grep -vE '^(\+\+\+|---)' | sed 's/^.//' \
  | grep -vE '^[[:space:]]*(#|$)' | grep -c . || true)

now=$(sed -n 's/^KIT_MEMORY_TREE_VERSION=\([0-9.]*\).*/\1/p' "$ENGINE" | head -1)
was=$(git show "$BASE:$ENGINE" 2>/dev/null | sed -n 's/^KIT_MEMORY_TREE_VERSION=\([0-9.]*\).*/\1/p' | head -1)
[ -n "$now" ] || { echo "verdict-epoch: cannot read KIT_MEMORY_TREE_VERSION from $ENGINE"; exit 2; }

if [ "$moved" = 0 ]; then
  echo "verdict-epoch: clean — the engine's behaviour-bearing lines are unchanged since ${BASE} (version $now)"
  exit 0
fi
# A base that predates the constant reads as empty; treat that as "it changed", since it did.
if [ -n "$was" ] && [ "$was" = "$now" ]; then
  echo "verdict-epoch: FAILED — $moved non-comment line(s) of $ENGINE changed since $BASE, but"
  echo "verdict-epoch: KIT_MEMORY_TREE_VERSION is $now at BOTH ends. The constant is what dates the"
  echo "verdict-epoch: engine's verdicts — hygiene-parity.test.sh derives its baseline floor from it —"
  echo "verdict-epoch: so leaving it still makes the floor point at a commit from before this change."
  echo "verdict-epoch: Bump it in ALL THREE places, which must move together:"
  echo "verdict-epoch:   $ENGINE (the constant AND the gov:kit marker on that same line)"
  echo "verdict-epoch:   tools/memory-tree/HYGIENE.template.md (line 1)"
  echo "verdict-epoch:   memory/HYGIENE.md (line 1) — then: bash tools/memory-tree/kit-dogfood-parity.test.sh --render"
  exit 1
fi
echo "verdict-epoch: clean — $moved non-comment line(s) changed and the version moved ${was:-<absent>} -> $now"
