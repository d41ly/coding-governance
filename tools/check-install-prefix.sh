#!/usr/bin/env bash
# check-install-prefix.sh — nothing this repo SHIPS may spell a root-install kit path.
#
#   bash tools/check-install-prefix.sh            # assert; exit 1 on an unwaived hit
#   bash tools/check-install-prefix.sh --list     # print every hit, waived or not (authoring aid)
#
# WHY. Kits install at `tools/<kit>/` in a target repo (one segment; the codebase-map gate template
# resolves no deeper). Every ENGINE already derives its own prefix, so what actually strands an
# adopter is a path SPELLED in something they receive: a runbook step, a usage header, a remedy
# string, a rendered artifact. Those fail quietly. Measured before this gate existed: a `tools/`
# install scaffolded the adopter's own committed `HYGIENE.md` with seven kit paths that resolve to
# nothing in their tree, and the hygiene gate exited 0 over it.
#
# THE POPULATION is what a target repo RECEIVES, and the two exclusions are principled rather than
# convenient. Test and selftest files are excluded because they BUILD root-prefix installs on
# purpose, to prove the dual-spelling support this repo keeps for its existing adopters — gating
# them would forbid testing the thing that support exists for. `*.conf.example` is excluded because
# its values are stamped by an adopter at install time.
#
# THE PREDICATE matches a kit name followed by a real FILE. A bare `memory-tree/` in prose names the
# kit, not a path anyone runs, and gating it would make every sentence about a kit a violation. The
# kit-name alternation is DERIVED from the tracked `tools/*` directories, never listed, so a new kit
# is covered the day it lands.
#
# WAIVERS are a tracked file, one `<path>:<line>` per row with a reason after whitespace. Every entry
# today is a deliberate root spelling that supports the not-retrofitted adopters. Shrink-only: the
# count may fall, never rise, so a new spelling cannot be waived away quietly.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "install-prefix: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

WAIVERS="tools/install-prefix-waivers.txt"
MODE="${1:---check}"
case "$MODE" in --check|--list) ;; *) echo "usage: $(basename "$0") [--check|--list]"; exit 2 ;; esac

# The kit names, derived. `git ls-files` so the answer is the same on every node and in every
# checkout — a directory listing would also see untracked scratch dirs.
kits=$(git ls-files -- 'tools/*/*' | awk -F/ 'NF>2 {print $2}' | sort -u)
[ -n "$kits" ] || { echo "install-prefix: no kit directories under tools/ — that is not a pass"; exit 1; }
alt=$(printf '%s' "$kits" | tr '\n' '|'); alt=${alt%|}

# The shipped surface: what a target repo receives, plus the file that tells them where to put it.
# WIRE-INTO-PROJECT.md is in the population even though nothing copies it — it PRESCRIBES the install
# paths, so a root spelling there becomes a root install in every repo that follows it. Highest
# leverage member of the set, not an edge case.
files=$(git ls-files -- 'tools/*' 'skills/*' '.githooks/*' '*.template.*' '*.fragment.json' \
                       'coding-governance-agents.template.md' 'WIRE-INTO-PROJECT.md' \
        | grep -vE '(\.test\.sh|\.test\.py|selftest\.py|\.conf\.example)$' \
        | grep -vE '^tools/(check-install-prefix\.sh|install-prefix-waivers\.txt)$')
[ -n "$files" ] || { echo "install-prefix: the shipped surface is empty — that is not a pass"; exit 1; }

# `}` and `{` join the excluded lead characters so a placeholder-prefixed path — the very fix this
# gate exists to encourage — is not itself a hit. Without it `{{TOOL_ROOT}}codebase-map/x.py` reds,
# which would make the gate refuse the corrected form and accept only the broken one.
RE="(^|[^/{}[:alnum:]._-])($alt)/[A-Za-z0-9_.-]+\.(sh|py|js|md|json|toml)"

hits=$(printf '%s\n' "$files" | tr -d '\r' | while IFS= read -r f; do
  [ -n "$f" ] || continue
  grep -nE "$RE" -- "$f" 2>/dev/null | while IFS= read -r m; do printf '%s:%s\n' "$f" "${m%%:*}"; done
done)

waived_rows=""
[ -f "$WAIVERS" ] && waived_rows=$(grep -vE '^\s*(#|$)' "$WAIVERS" | awk '{print $1}')
waived_n=$(printf '%s' "$waived_rows" | grep -c . || true)

if [ "$MODE" = --list ]; then
  printf '%s\n' "$hits" | grep -c . | xargs -I{} echo "install-prefix: {} hit(s) over $(printf '%s\n' "$files" | grep -c .) shipped files"
  printf '%s\n' "$hits" | while IFS= read -r h; do
    [ -n "$h" ] || continue
    if printf '%s\n' "$waived_rows" | grep -qxF "$h"; then printf '  waived  %s\n' "$h"
    else printf '  HIT     %s  %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-90)"; fi
  done
  exit 0
fi

bad=0
for h in $hits; do
  printf '%s\n' "$waived_rows" | grep -qxF "$h" && continue
  if [ "$bad" = 0 ]; then
    echo "install-prefix: a SHIPPED file spells a root-install kit path. An adopter installs kits at"
    echo "install-prefix: tools/<kit>/, so these resolve to nothing in their tree — and nothing else"
    echo "install-prefix: reds. Fix the path, or add a row to $WAIVERS with the reason it must stay."
  fi
  bad=$((bad+1))
  printf '  %s  %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-90)"
done
[ "$bad" = 0 ] || exit 1

# A waiver that no longer names a hit is a stale row: the spelling it excused is gone, and leaving it
# lets the NEXT one in silently under a pin that never fell.
stale=0
for w in $waived_rows; do
  printf '%s\n' "$hits" | grep -qxF "$w" && continue
  [ "$stale" = 0 ] && echo "install-prefix: stale waiver(s) — the spelling they excuse is gone; delete the row:"
  stale=$((stale+1)); printf '  %s\n' "$w"
done
[ "$stale" = 0 ] || exit 1

echo "install-prefix: clean — $(printf '%s\n' "$files" | grep -c .) shipped files, $waived_n declared waiver(s), no undeclared root-install spelling"
