#!/usr/bin/env bash
# check-verifier-fanout.sh — the COMMITTED workflow harnesses obey every rule agent-cap.js enforces.
# TOOL-dTieredTribunal-14 S3: this gate pipes each harness to the hook with NO --only flag, so once
# the hook's raw-primitive early exit was inverted it began enforcing the ref-keyed-join rule too.
# No verdict moved — its population is a SUBSET of the join gate's and the wider set was measured
# clean — but a header describing a one-rule gate would be a structural check reading as a
# semantic one, which is the class the charter names. Disclosed rather than widened silently.
#
#   bash <prefix>/workflows/check-verifier-fanout.sh          # every workflow script git can see
#   bash <prefix>/workflows/check-verifier-fanout.sh <file>…  # explicit files (the self-test's fixtures)
#   ... --print-cap                                         # the hook's effective fan-out cap
#
# Exit 0 = clean · 1 = a rule the hook enforces is broken · 2 = misconfigured.
#
# THIS GATE DOES NOT IMPLEMENT THE RULE. It feeds each script to `<prefix>/hooks/agent-cap.js` — the
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

# ---- THE POPULATION HAS NO PREFIX -- TOOL-aRepatriatedFork-4 ----------------------------------
# Every `*.js` git lists, then the `export const meta` marker below. The marker IS the selector,
# as it is in check-workflow-syntax.js, so a harness is judged wherever it lives -- both adopters
# keep theirs under `.claude/workflows/`, which a kit-prefix filter never reached, and each carried
# a hand-kept fork to compensate. The prefix TOOL-dRetiredFork-10 derived here was doing nothing
# the marker does not, except hiding those harnesses.
HERE="$(cd "$(dirname "$0")" && pwd)"

# ---- THE PREDICATE, PROBED -------------------------------------------------------------------
# Three rungs, and the third is not optional. Adopter nc keeps its hooks a directory up from its
# harnesses, which rung 2 reaches. adopter ic has no such directory AT ALL -- its only copy sits at
# `.claude/hooks/agent-cap.js` -- so a two-rung chain strands it, and that was found by testing the
# derivation against both trees rather than by reasoning about one.
#
# F1, ratified: rung 3 stays a literal. `.claude/hooks/` is the HARNESS's own convention, not an
# install prefix an adopter chooses, and this is the one place the unit does not practise what it
# enforces. Said here rather than left for a reader to notice.
#
# TOOL-aRepatriatedFork-46: rungs 1 and 2 are the sibling-kit resolver's. It reads the install
# receipt BEFORE it probes this kit's own directory and its parent, so a hooks kit an adopter homed
# under another name is found, and it names the kit by its home rather than as a literal segment.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  "$1" -c "$(cat <<'RKD'
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).resolve()
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).resolve()
        if hit.is_file() and root in hit.parents:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
)"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
HOOK=""
if _hk_py=$(resolve_python 2>/dev/null) && _hk_dir=$(resolve_kit_dir "$_hk_py" hooks agent-cap.js "$HERE" 2>/dev/null); then
  HOOK="$ROOT/$_hk_dir/agent-cap.js"
elif [ -f "$ROOT/.claude/hooks/agent-cap.js" ]; then
  HOOK="$ROOT/.claude/hooks/agent-cap.js"
fi
[ -n "$HOOK" ] || { echo "verifier-fanout: no agent-cap.js through the install receipt, at $HERE/hooks/, $HERE/../hooks/ or $ROOT/.claude/hooks/ — this gate has no predicate to delegate to"; exit 2; }
command -v node >/dev/null 2>&1 || { echo "verifier-fanout: node not found — the predicate is a node hook"; exit 2; }

# `--print-cap` relays the hook's answer for this checkout's effective fan-out cap and judges nothing.
# It exists so a sibling in this kit (check-protocol-parity.test.sh) asks the hook through the one
# probe above, instead of locating the hook again or re-parsing `.agent-cap.conf` itself.
[ "${1:-}" = --print-cap ] && exec node "$HOOK" --print-cap </dev/null

# The gate and its fixtures are outside their own population: the test's RED fixtures spell the banned
# shape on purpose, and a fixture that lands in the repo would otherwise make the merge bar
# permanently red. (They live under `mktemp -d`, so this is belt-and-braces — the same shape
# check-review-join.sh carries for the same reason.)
SELF_EXCLUDE='(^|/)check-verifier-fanout\.(sh|js|test\.sh)$'
# BASENAME-anchored, because the gate is installed under whatever prefix an adopter picks: an
# exclusion spelled with a rooted literal would name a path that exists only here.

if [ "$#" -gt 0 ]; then
  FILES=$(printf '%s\n' "$@")
  EXPLICIT=1
else
  # tracked AND untracked-but-unignored, matching the other two JavaScript gates: a new harness is
  # judged the moment it exists, not the moment someone remembers to stage it.
  # A `*.template.js` is a RENDER SOURCE, not a harness (TOOL-aRepatriatedFork-7 S7): its fan-out cap
  # is the `{{FANOUT_CAP}}` token, which no hook can resolve and no runtime ever sees. What runs is
  # its render, which IS in this population, and check-protocol-parity.test.sh pins the render to it.
  FILES=$(git ls-files --cached --others --exclude-standard -- '*.js' \
    | grep -vE "$SELF_EXCLUDE" | grep -vE '\.template\.js$' | LC_ALL=C sort -u || true)
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
    echo "verifier-fanout: no workflow script (a *.js exporting meta) anywhere git lists, .claude/workflows/ included — the population is empty, which is not a pass"
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

# THE CAP PRINTED IS THE EFFECTIVE ONE (TOOL-aRepatriatedFork-7 S6), and the HOOK answers it for the
# root this script stands in (closing review round 1 residual b): the sed this replaced matched
# nothing on a BOM-led conf and printed the ceiling over a hook enforcing 4. A refusal reds the run.
CAPN=$(node "$HOOK" --print-cap </dev/null 2>&1) || { printf 'verifier-fanout: %s\n' "$CAPN"; st=1; }
[ "$st" = 0 ] && echo "verifier-fanout: clean — $n workflow script(s) obey the ≤$CAPN-verifier rule"
exit "$st"
