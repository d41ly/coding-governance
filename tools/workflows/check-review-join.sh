#!/usr/bin/env bash
# check-review-join.sh — the retirement gate for the ref-keyed verdict join.
#
#   bash tools/workflows/check-review-join.sh          # every *.js under tools/ that git can see
#   bash tools/workflows/check-review-join.sh <file>…  # explicit files (the self-test's fixtures)
#
# Exit 0 = clean · 1 = a ref-keyed join reappeared · 2 = THIS GATE REFUSED.
#
# A 2 is never a finding about the code under it. It means this gate declined to return a verdict:
# not a git repo, the predicate absent, node missing, the predicate returning a status this gate
# cannot classify, or the predicate exiting 2 without naming a line, which is its own refusal being
# handed up rather than a join. The last two arrived with the delegation and this line did not move
# with them - a stale exit-code contract is the same defect class as a stale pointer.
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
set -o pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "review-join: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

SELF_EXCLUDE='^tools/(workflows/check-review-join\.(sh|js|test\.sh)|hooks/agent-cap\.js)$'
# TOOL-dTieredTribunal-14 S6 - the hook joins the exclusion because it now HOLDS the ban table.
# Measured, not defensive: the retired-identifier ban is a bare regex literal, a regex literal
# survives the hook's own literal blanking, and the predicate run over the hook returns one hit on
# exactly the table's line. This file's header already declared the doctrine and said SELF_EXCLUDE
# keeps it true if the predicate is ever written in JavaScript. After S1 it is.

if [ "$#" -gt 0 ]; then
  FILES=$(printf '%s\n' "$@")
  EXPLICIT=1
else
  # --cached AND --others: a NEW workflow script is judged the moment it exists, not the moment
  # someone remembers to stage it. --exclude-standard keeps ignored files ignored, and that is the
  # escape hatch: a scratch .js you do not want judged is a .gitignore line, not an unstaged file.
  # This DOES change the landing boundary — tools/push-main.sh gates on `git status --porcelain -uno`
  # and so deliberately permits untracked files at a push — which is the point: a banned join sitting
  # unstaged in the tree was previously invisible to the gate that exists to ban it.
  FILES=$(git ls-files --cached --others --exclude-standard -- '*.js' \
    | grep -E '^tools/.*\.js$' | grep -vE "$SELF_EXCLUDE" | LC_ALL=C sort -u || true)
  EXPLICIT=0
fi

if [ "$EXPLICIT" = 0 ] && [ -z "$FILES" ]; then
  echo "review-join: no JavaScript under tools/ — the population is empty, which is not a pass"
  exit 1
fi

# TOOL-dTieredTribunal-14 S5 - THE PREDICATE MOVED. It lives in tools/hooks/agent-cap.js as rule 5,
# and this gate delegates to it so both entry points share one predicate. The reason is the modality:
# an ad-hoc review harness is an inline `script` string on a Workflow tool call and is NEVER a file,
# so this gate covered the already-compliant committed harnesses and none of the observed failures.
# The hook sees that string. Its three bans, and the `why` text this gate's own self-test asserts,
# are pinned in that rule; the stripper is the hook's `blankLiterals`, which BLANKS string contents
# where the retired in-file scanner kept them, and that narrowing is recorded in section 4 Migration.
# The retired tool's NAME is deliberately not written under this path: this gate has one predicate
# and it is the hook's, so a reader grepping for the old one should find nothing here.
SCAN=()
while IFS= read -r f; do [ -n "$f" ] && [ -f "$f" ] && SCAN+=("$f"); done <<<"$FILES"
if [ "${#SCAN[@]}" = 0 ]; then
  echo "review-join: none of the named files exist — nothing was scanned, which is not a pass"
  exit 1
fi

HOOK="$ROOT/tools/hooks/agent-cap.js"
[ -f "$HOOK" ] || { echo "review-join: the predicate is at $HOOK and it is not there — a gate whose predicate is absent must say so, not pass"; exit 2; }
command -v node >/dev/null 2>&1 || { echo "review-join: node is not on PATH, so the predicate cannot run — refusing rather than passing"; exit 2; }

hits=""
for f in "${SCAN[@]}"; do
  # The payload is built by node itself: a JSON encoder written in shell is one more place for a
  # backslash or a backtick in a script under judgement to change the meaning of the thing judged.
  out=$(node -e '
      const fs = require("fs")
      process.stdout.write(JSON.stringify({
        tool_name: "Workflow",
        tool_input: { script: fs.readFileSync(process.argv[1], "utf8") },
      }))' "$f" | node "$HOOK" --only=join 2>&1) && rc=0 || rc=$?
  # This loop used to read "the pipeline exited non-zero" as "rule 5 fired". Two symptoms, one root.
  # The hook exits 2 on its OWN environment refusal before any rule runs, and that message carries
  # no line starting with two spaces and L, so the sed emptied it and the gate printed a ref-keyed
  # join with a blank body - sending an operator off to rewrite a join that is not there. And with
  # no pipefail only the hook's status was read, so a builder that threw fed empty stdin to a
  # JSON.parse whose catch exits 0 and the file was recorded CLEAN. A status this gate cannot
  # interpret is a refusal, never a verdict: its own header preaches that a probe which cannot move
  # must say so, and it was the counterexample.
  if [ "$rc" != 0 ] && [ "$rc" != 2 ]; then
    echo "review-join: the predicate returned $rc on $f, which is neither clean nor a rule hit - refusing rather than reporting"
    printf '%s\n' "$out" | sed 's/^/    /'
    exit 2
  fi
  if [ "$rc" = 2 ]; then
    body=$(printf '%s' "$out" | sed -n '/^  L/,$p')
    if [ -z "$body" ]; then
      echo "review-join: the predicate exited 2 on $f without naming a line, so that is its own refusal and not a join"
      printf '%s\n' "$out" | sed 's/^/    /'
      exit 2
    fi
    hits="$hits$f:
$body
"
  fi
done

if [ -n "$hits" ]; then
  echo "review-join: FAILED — a ref-keyed verdict join reappeared. Key the join on the integer id the"
  echo "review-join: orchestrator assigns before the skeptic sees the finding (tier2-review.js)."
  printf '%s\n' "$hits" | sed 's/^/    /'
  exit 1
fi
echo "review-join: clean — no ref-keyed verdict join under tools/"
