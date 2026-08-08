#!/usr/bin/env bash
# check-verifier-fanout.sh — the COMMITTED workflow harnesses obey the review protocol's verifier cap.
#
#   bash tools/workflows/check-verifier-fanout.sh          # every workflow script git can see
#   bash tools/workflows/check-verifier-fanout.sh <file>…  # explicit files (the self-test's fixtures)
#
# Exit 0 = clean · 1 = a per-item verify fan-out survives · 2 = misconfigured.
#
# THIS GATE DOES NOT IMPLEMENT THE RULE. It feeds each script to `tools/hooks/agent-cap.js` — the
# same predicate the `PreToolUse` hook applies at the `Workflow` tool call — and reports what the hook
# says. A bash re-implementation of a node predicate is two answers to one question: they would not
# disagree loudly, they would drift the day either side is tightened, and the gate would then bless
# scripts the hook denies (or the reverse) with no signal at all.
#
# WHY BOTH ENTRY POINTS EXIST. The hook is the PRIMARY one: it sees the inline `script` string of an
# ad-hoc review, which is the modality that actually produced the violation this rule exists for, and
# which no file-scoped gate can ever see. This gate is the second line — it covers the harnesses that
# live in the tree and are invoked by NAME, where the hook receives no source at all.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "verifier-fanout: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

HOOK="$ROOT/tools/hooks/agent-cap.js"
[ -f "$HOOK" ] || { echo "verifier-fanout: $HOOK is missing — this gate has no predicate to delegate to"; exit 2; }
command -v node >/dev/null 2>&1 || { echo "verifier-fanout: node not found — the predicate is a node hook"; exit 2; }

# The gate and its fixtures are outside their own population: the test's RED fixtures spell the banned
# shape on purpose, and a fixture that lands in the repo would otherwise make the merge bar
# permanently red. (They live under `mktemp -d`, so this is belt-and-braces — the same shape
# check-review-join.sh carries for the same reason.)
SELF_EXCLUDE='^tools/workflows/check-verifier-fanout\.(sh|js|test\.sh)$'

if [ "$#" -gt 0 ]; then
  FILES=$(printf '%s\n' "$@")
  EXPLICIT=1
else
  # tracked AND untracked-but-unignored, matching the other two JavaScript gates: a new harness is
  # judged the moment it exists, not the moment someone remembers to stage it.
  FILES=$(git ls-files --cached --others --exclude-standard -- '*.js' \
    | grep -E '^tools/.*\.js$' | grep -vE "$SELF_EXCLUDE" | LC_ALL=C sort -u || true)
  EXPLICIT=0
fi

# A workflow script IDENTIFIES ITSELF by exporting `meta` — the same marker check-workflow-syntax.js
# uses, so a gate/helper `.js` sitting in the same directory is not judged as a harness.
SCAN=""
while IFS= read -r f; do
  [ -n "$f" ] && [ -f "$f" ] || continue
  if [ "$EXPLICIT" = 1 ] || grep -qE '^[[:space:]]*export[[:space:]]+const[[:space:]]+meta[[:space:]]*=' "$f"; then
    SCAN="$SCAN$f
"
  fi
done <<<"$FILES"

if [ -z "$SCAN" ]; then
  if [ "$EXPLICIT" = 1 ]; then
    echo "verifier-fanout: none of the named files exist — nothing was scanned, which is not a pass"
  else
    echo "verifier-fanout: no workflow script under tools/ — the population is empty, which is not a pass"
  fi
  exit 1
fi

st=0
n=0
while IFS= read -r f; do
  [ -n "$f" ] || continue
  n=$((n+1))
  # The payload is built by node itself: a JSON encoder written in shell is one more place for a
  # backslash or a backtick in a workflow's prompt text to change the meaning of the thing being
  # judged.
  if ! out=$(node -e '
      const fs = require("fs")
      process.stdout.write(JSON.stringify({
        tool_name: "Workflow",
        tool_input: { script: fs.readFileSync(process.argv[1], "utf8") },
      }))' "$f" | node "$HOOK" 2>&1); then
    echo "verifier-fanout: FAILED — $f"
    printf '%s\n' "$out" | sed 's/^/    /'
    st=1
  fi
done <<<"$SCAN"

[ "$st" = 0 ] && echo "verifier-fanout: clean — $n workflow script(s) obey the ≤5-verifier rule"
exit "$st"
