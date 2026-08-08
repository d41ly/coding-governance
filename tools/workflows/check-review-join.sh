#!/usr/bin/env bash
# check-review-join.sh — the retirement gate for the ref-keyed verdict join.
#
#   bash tools/workflows/check-review-join.sh          # every tracked *.js under tools/
#   bash tools/workflows/check-review-join.sh <file>…  # explicit files (the self-test's fixtures)
#
# Exit 0 = clean · 1 = a ref-keyed join reappeared · 2 = not a git repo.
#
# WHAT THIS BANS AND WHY. A Tier-2 review harness joins each finding to its skeptic verdict. Keying
# that join on a `file:line` STRING the skeptic has to reproduce byte-for-byte has two failure modes,
# both of which shipped upstream and one of which was live in this kit:
#   * echo drift — a re-wrapped path or a re-derived line number misses the join, and the finding
#     silently leaves the count;
#   * COLLISION — two findings at one file:line (normal when two lenses read one function) collapse
#     into a single map entry, and BOTH inherit whichever verdict landed last.
# The class has no runtime signal — a mis-keyed harness reports a clean bill. Removing the selectable
# defective construct is the whole remedy, so this gate asserts the construct is gone.
#
# COMMENT STRIPPING IS LOAD-BEARING, not politeness. `tier2-review.js` explains the retired join in a
# comment that necessarily SPELLS the banned expression. A whole-file-text absence assertion would
# red on the documentation of its own fix — the exact trap recorded in the kickoff manifest's
# environment traps. Only code lines are judged.
#
# THE GATE IS OUTSIDE ITS OWN POPULATION for the same reason: this file holds every banned pattern
# verbatim in order to search for it. The population is `*.js`; this is `.sh`; and SELF_EXCLUDE below
# keeps that true if the gate is ever rewritten in JavaScript.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "review-join: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

SELF_EXCLUDE='^tools/workflows/check-review-join\.(sh|js|test\.sh)$'

if [ "$#" -gt 0 ]; then
  FILES=$(printf '%s\n' "$@")
  EXPLICIT=1
else
  FILES=$(git ls-files -- '*.js' | grep -E '^tools/.*\.js$' | grep -vE "$SELF_EXCLUDE" || true)
  EXPLICIT=0
fi

if [ "$EXPLICIT" = 0 ] && [ -z "$FILES" ]; then
  echo "review-join: no JavaScript under tools/ — the population is empty, which is not a pass"
  exit 1
fi

# One awk over the whole population. Per line: drop a /* … */ span (including one that opens here and
# closes later), then drop a // tail — but only when the // is at the start or follows whitespace and
# is NOT preceded by a colon, so `https://…` inside a string survives as code. Then match the bans.
#
#   BAN 1  obj[<something>.ref]          — an object or Map literal keyed by a ref string
#   BAN 2  .get/.set/.has/.delete(x.ref) — the same defect wearing a Map's clothes
#   BAN 3  verdictByRef                  — the retired identifier itself, in any position
SCAN=()
while IFS= read -r f; do [ -n "$f" ] && [ -f "$f" ] && SCAN+=("$f"); done <<<"$FILES"
if [ "${#SCAN[@]}" = 0 ]; then
  echo "review-join: none of the named files exist — nothing was scanned, which is not a pass"
  exit 1
fi

# The stripper is a CHARACTER scan, not a regex. A `match(/\/\//)` on the raw line cannot tell the
# `//` that opens a comment from the one inside `"https://…"`, and cutting on the wrong one turns a
# code line into prose and the ban into a no-op. Quote state carries across lines (template
# literals), block-comment state carries across lines, and a backslash escape consumes its next
# character so a regex literal's `\/` is not read as a delimiter. Both states reset per file.
hits=$(awk '
  function strip(s,   n, i, c, d, out) {
    n = length(s); out = ""; i = 1
    while (i <= n) {
      c = substr(s, i, 1); d = substr(s, i, 2)
      if (inblk)  { if (d == "*/") { inblk = 0; i += 2 } else i++; continue }
      if (c == "\\") { out = out substr(s, i, 2); i += 2; continue }
      if (q != "") { if (c == q) q = ""; out = out c; i++; continue }
      if (d == "/*") { inblk = 1; i += 2; continue }
      if (d == "//") break
      if (c == "\"" || c == "'"'"'" || c == "`") { q = c }
      out = out c; i++
    }
    return out
  }
  FNR == 1 { inblk = 0; q = "" }
  { code = strip($0)
    if (code ~ /\[[A-Za-z_$][A-Za-z0-9_$.]*\.ref\]/)                       print FILENAME ":" FNR ": object/Map literal keyed by a .ref string"
    else if (code ~ /\.(get|set|has|delete)\([A-Za-z_$][A-Za-z0-9_$.]*\.ref[),]/) print FILENAME ":" FNR ": Map keyed by a .ref string"
    else if (code ~ /verdictByRef/)                                         print FILENAME ":" FNR ": the retired verdictByRef identifier"
  }' "${SCAN[@]}")

if [ -n "$hits" ]; then
  echo "review-join: FAILED — a ref-keyed verdict join reappeared. Key the join on the integer id the"
  echo "review-join: orchestrator assigns before the skeptic sees the finding (tier2-review.js)."
  printf '%s\n' "$hits" | sed 's/^/    /'
  exit 1
fi
echo "review-join: clean — no ref-keyed verdict join under tools/"
