#!/usr/bin/env bash
# Runnable check for format-guard.js — the Stop hook that refuses a routed session's final message
# without the charter's BUILD/SPEC pair or a committed line. Run: bash <prefix>/hooks/format-guard.test.sh
# (exit 0 = all pass)
#
# WHAT THIS FILE DOES NOT CHECK, stated up front: it does not prove the hook is WIRED (check-wiring.sh
# and check-hook-destinations.sh own that), and it does not prove the harness delivers
# `last_assistant_message` on the running CLI — a payload here is built by hand. The live witness of
# both is the build record TOOL-aHeardState-1 S9 names.
#
# EVERY ARM RUNS AGAINST A FIXTURE REPOSITORY under the suite's own temp dir: a charter carrying the
# real fence, a LIVE.md naming the routed build, an orientation card under the fixture's common dir,
# and commits made there. The real repository's card, LIVE.md and HEAD are never read, so the suite
# measures the same thing on every node.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
HOOK="$HERE/format-guard.js"
ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "format-guard.test: not inside a git repository"; exit 2; }
command -v node >/dev/null 2>&1 || { echo "format-guard.test: node is not on PATH"; exit 2; }
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0

# The runlog kit's prose reader, for the AC6 parity arm: resolved, never spelled.
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
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
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
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
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
TESTPY=$(resolve_python) || { echo "format-guard.test: no usable python"; exit 2; }
RUNLOG_DIR=$(resolve_kit_dir "$TESTPY" runlog prose.py "$HERE") || exit 2

# The native spelling of a directory: node reads the payload's cwd as a Windows path on Windows, and
# an MSYS `/tmp/x` names nothing there (memory/gotchas, the node-a /tmp mount).
resolve_native() { (cd "$1" && { pwd -W 2>/dev/null || pwd; }); }

REPO="$TMP/repo"
SID=tSession-1
seed_repo() { # charter-file -> a fresh fixture repository at $REPO with one commit
  rm -rf "$REPO"; mkdir -p "$REPO/memory"
  git -C "$REPO" init -q
  cp "$1" "$REPO/AGENTS.md"
  printf 'MEMORY_ROOT="memory"\n' > "$REPO/.memory-tree.conf"
  printf '| Build | Status |\n|---|---|\n| [tBuild](builds/tBuild/README.md) | INPROGRESS |\n' > "$REPO/memory/LIVE.md"
  git -C "$REPO" add -A
  git -C "$REPO" -c user.name=t -c user.email=t@t commit -q -m seed
  mkdir -p "$REPO/.git/orientation"
  printf '## task\n- t\n## route\n- build: tBuild\n- unit: TOOL-tBuild-1 · spec memory/builds/tBuild/spec/x.md\nREADY — tBuild · node a · main · base x · Tier-2 · gates none\n' > "$REPO/.git/orientation/$SID.md"
}
seed_fixture_commit() { # subject -> the new HEAD's sha
  printf '%s\n' "$1" >> "$REPO/memory/LIVE.md.note"
  git -C "$REPO" add -A
  git -C "$REPO" -c user.name=t -c user.email=t@t commit -q -m "$1"
  git -C "$REPO" rev-parse HEAD
}

# run_stop <name> <block|allow> <message-file> [extra JSON fields] — builds the payload with node, so
# no message byte passes through a shell quote.
run_stop() {
  local name=$1 want=$2 msg=$3 extra=${4:-}
  [ -n "$extra" ] || extra='{}'
  node -e '
    const fs = require("fs")
    const p = { hook_event_name: "Stop", session_id: process.argv[2], cwd: process.argv[3], stop_hook_active: false,
                last_assistant_message: fs.readFileSync(process.argv[1], "utf8") }
    Object.assign(p, JSON.parse(process.argv[4] || "{}"))
    process.stdout.write(JSON.stringify(p))' "$msg" "$SID" "$(resolve_native "$REPO")" "$extra" > "$TMP/payload"
  node "$HOOK" < "$TMP/payload" > "$TMP/out" 2> "$TMP/err"
  local rc=$? got=allow
  [ -s "$TMP/out" ] && got=block
  if [ "$rc" = 0 ] && [ "$got" = "$want" ]; then echo "ok   $name ($got)"; pass=$((pass+1))
  else echo "FAIL $name (exit $rc, $got, want $want)"; sed 's/^/     /' "$TMP/out" "$TMP/err"; fail=$((fail+1)); fi
}
check_contains() { # <name> <file> <fixed string>
  if grep -qF -- "$3" "$2"; then echo "ok   $1"; pass=$((pass+1))
  else echo "FAIL $1 (no '$3' in $(basename "$2"))"; sed 's/^/     /' "$2"; fail=$((fail+1)); fi
}
check_empty() { # <name> <file>
  if [ ! -s "$2" ]; then echo "ok   $1"; pass=$((pass+1))
  else echo "FAIL $1 ($(basename "$2") not empty)"; sed 's/^/     /' "$2"; fail=$((fail+1)); fi
}

# write_message <name> <line>... — one message file, one argument per line. Every string here is one line and
# the backtick is built from an octal escape, because the codebase map tokenizes this file as a kit
# shell layer and a multi-line or backticked quoted word is where that tokenizer loses its place.
write_message() { local f=$1; shift; printf '%s\n' "$@" > "$TMP/$f.md"; }
B='BUILD — tBuild · Tier-2 · 1/2 build · left TOOL-tBuild-2'
S='SPEC — [TOOL-tBuild-1](memory/builds/tBuild/spec/x.md) · review none'
BT=$(printf '\140'); FENCE="$BT$BT$BT"
write_message good   "Done." "" "- $B" "- $S"
write_message none   "Done, all good."
write_message tick   "- $BT$B$BT" "- $BT$S$BT"
write_message indent "  - $B" "  - $S"
write_message bold   "- **$B**" "- **$S**"
write_message head   "## $B" "- $S"
write_message fenced "$FENCE" "- $B" "- $S" "$FENCE"
write_message first  "- $S" "- $B"
write_message gap    "- $B" "" "- $S"
write_message noleft "- BUILD — tBuild · Tier-2 · 1/2 build" "- $S"

# The real charter, CR-stripped: a worktree checkout can land CRLF, and the fence edits below compare
# whole lines (memory/gotchas, worktree CRLF outside the gated population).
tr -d '\r' < "$ROOT/AGENTS.md" > "$TMP/charter.md"
grep -qxF '<!-- microformats -->' "$TMP/charter.md" || { echo "format-guard.test: $ROOT/AGENTS.md carries no microformats fence, so every arm would pass over nothing"; exit 2; }
seed_repo "$TMP/charter.md"

# AC1 — a pair-less final message blocks once, and never on a continuation.
run_stop "AC1 a message with no pair blocks" block "$TMP/none.md"
check_contains "AC1 the reason names the missing BUILD line" "$TMP/out" "no BUILD line"
check_contains "AC1 the reason quotes the charter's BUILD definition" "$TMP/out" 'BUILD — <slug> · Tier-<n>'
run_stop "AC1 stop_hook_active true allows" allow "$TMP/none.md" '{"stop_hook_active":true}'

# AC2 — rule r1: five non-bare spellings.
for f in tick indent bold head fenced; do
  run_stop "AC2 a $f pair blocks" block "$TMP/$f.md"
  check_contains "AC2 the $f reason names rule r1" "$TMP/out" "rule r1"
done

# AC3 — adjacency.
run_stop "AC3 SPEC before BUILD blocks" block "$TMP/first.md"
check_contains "AC3 the reason names the [pair] rule" "$TMP/out" "[pair] rule"
run_stop "AC3 a blank line between the pair blocks" block "$TMP/gap.md"
check_contains "AC3 the gap reason names the [pair] rule" "$TMP/out" "[pair] rule"

# AC4 — a correct pair passes silently.
run_stop "AC4 a well-formed adjacent bare pair allows" allow "$TMP/good.md"
check_empty "AC4 a correct pair writes nothing to stderr" "$TMP/err"

# AC8 — a dropped field fails the derived shape.
run_stop "AC8 a BUILD line without its left field blocks" block "$TMP/noleft.md"
check_contains "AC8 the reason names the charter shape" "$TMP/out" "does not match its charter shape"

# AC6 — commits since the previous stop.
seed_repo "$TMP/charter.md"
run_stop "AC6 the first armed stop records a baseline and allows" allow "$TMP/good.md"
if [ -s "$REPO/.git/format-guard/$SID.head" ]; then echo "ok   AC6 the sidecar holds the baseline HEAD"; pass=$((pass+1))
else echo "FAIL AC6 no sidecar at .git/format-guard/$SID.head"; fail=$((fail+1)); fi
sha=$(seed_fixture_commit "one")
run_stop "AC6 an unreported commit blocks" block "$TMP/good.md"
check_contains "AC6 the reason names the new commit" "$TMP/out" "commit ${sha:0:9}"
sha=$(seed_fixture_commit "two")
printf '%s\n\n- committed — %s · main · two\n' "$(cat "$TMP/good.md")" "${sha:0:7}" > "$TMP/reported.md"
run_stop "AC6 a commit named by a committed line allows" allow "$TMP/reported.md"
sha=$(seed_fixture_commit "three")
printf '%s\n\n- committed — 0000000 · main · three\n' "$(cat "$TMP/good.md")" > "$TMP/wrong.md"
run_stop "AC6 a committed line naming another sha blocks" block "$TMP/wrong.md"
sha=$(seed_fixture_commit "four")
printf '%s\n\n- merged — --no-ff tBranch → main · %s\n' "$(cat "$TMP/good.md")" "${sha:0:8}" > "$TMP/merged.md"
run_stop "AC6 a merged line naming the commit allows" allow "$TMP/merged.md"

# AC5 — unarmed: every case silent on both streams.
seed_repo "$TMP/charter.md"
SID=tSession-2 run_stop "AC5 no card allows" allow "$TMP/none.md"
check_empty "AC5 no card writes no witness" "$TMP/err"
printf '## task\n- t\n' > "$REPO/.git/orientation/$SID.md"
run_stop "AC5 a card with no route allows" allow "$TMP/none.md"
check_empty "AC5 a card with no route writes no witness" "$TMP/err"
printf '## route\n- build: tOther\n' > "$REPO/.git/orientation/$SID.md"
run_stop "AC5 a route whose build LIVE.md does not list allows" allow "$TMP/none.md"
check_empty "AC5 an unlisted build writes no witness" "$TMP/err"
seed_repo "$TMP/charter.md"
run_stop "AC5 a sub-agent payload allows" allow "$TMP/none.md" '{"agent_id":"a1"}'
check_empty "AC5 a sub-agent payload writes no witness" "$TMP/err"
run_stop "AC5 a SubagentStop event allows" allow "$TMP/none.md" '{"hook_event_name":"SubagentStop"}'

# AC7 — the grammar is read from the charter, never restated.
awk '$0 != "<!-- microformats -->" && $0 != "<!-- /microformats -->"' "$TMP/charter.md" > "$TMP/nofence.md"
seed_repo "$TMP/nofence.md"
run_stop "AC7 a charter with no fence allows" allow "$TMP/none.md"
check_contains "AC7 the witness names the missing fence" "$TMP/err" "microformats -->"
awk -v bt="$BT" 'index($0, "- " bt "BUILD — ") == 1 && substr($0, length($0)) == bt { $0 = substr($0, 1, length($0) - 1) " · x <y>" bt } { print }' \
  "$TMP/charter.md" > "$TMP/fourth.md"
grep -qF -- "· x <y>$BT" "$TMP/fourth.md" || { echo "FAIL AC7 the fixture edit did not land in the BUILD definition"; fail=$((fail+1)); }
seed_repo "$TMP/fourth.md"
run_stop "AC7 a BUILD definition with a fourth field blocks a message the real charter passes" block "$TMP/good.md"
check_contains "AC7 the edited shape is the one quoted" "$TMP/out" '· x <y>'

# AC9 — a payload that is not JSON allows.
printf 'not json' | node "$HOOK" > "$TMP/out" 2> "$TMP/err"; rc=$?
if [ "$rc" = 0 ] && [ ! -s "$TMP/out" ]; then echo "ok   AC9 non-JSON stdin exits 0 with empty stdout"; pass=$((pass+1))
else echo "FAIL AC9 non-JSON stdin (exit $rc)"; fail=$((fail+1)); fi

# AC6 (TOOL-aHeardState-2) — runlog prose re-implements this hook's pair predicate in Python; both
# readers grade the same messages against the same charter and must agree on every one.
seed_repo "$TMP/charter.md"
read_hook_verdict() { # message-file -> block|allow, counting nothing
  node -e '
    const fs = require("fs")
    process.stdout.write(JSON.stringify({ hook_event_name: "Stop", session_id: process.argv[2], cwd: process.argv[3],
      stop_hook_active: false, last_assistant_message: fs.readFileSync(process.argv[1], "utf8") }))' "$1" "$SID" "$(resolve_native "$REPO")" \
    | node "$HOOK" 2>/dev/null | grep -q . && echo block || echo allow
}
names="good none tick indent bold head fenced first gap noleft"
files=""; for f in $names; do files="$files $TMP/$f.md"; done
# shellcheck disable=SC2086
"$TESTPY" -c '
import pathlib, sys
sys.path.insert(0, sys.argv[1])
import prose as pr
shapes, err = pr.read_charter_shapes(pathlib.Path(sys.argv[2]))
if shapes is None:
    sys.exit("prose could not derive the pair grammar: " + err)
for f in sys.argv[3:]:
    text = pathlib.Path(f).read_text(encoding="utf-8")
    print(pathlib.Path(f).stem, "block" if pr.check_pair(pr.scan_message_lines(text), shapes) else "allow")
' "$ROOT/$RUNLOG_DIR" "$TMP/charter.md" $files > "$TMP/prose-verdicts" 2> "$TMP/err"
for f in $names; do
  hook=$(read_hook_verdict "$TMP/$f.md")
  py=$(awk -v n="$f" '$1 == n { print $2 }' "$TMP/prose-verdicts")
  if [ -n "$py" ] && [ "$hook" = "$py" ]; then echo "ok   AC6 the $f message reads $hook in both readers"; pass=$((pass+1))
  else echo "FAIL AC6 the $f message reads ${hook} in format-guard and ${py:-nothing} in runlog prose"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
done
if grep -q ' allow$' "$TMP/prose-verdicts" && grep -q ' block$' "$TMP/prose-verdicts"; then
  echo "ok   AC6 liveness: the verdict set holds both an allow and a block"; pass=$((pass+1))
else echo "FAIL AC6 liveness: the verdicts never moved, so agreement proves nothing"; fail=$((fail+1)); fi

n=$((pass+fail))
# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count. 43 = the suite as TOOL-aHeardState-1 landed it; 54 = 43 + TOOL-aHeardState-2's AC6 arm (10
# messages and its liveness).
# The pin sits alone on its line because the testsuite-counts leg reads it anchored.
FLOOR_ASSERTIONS=54
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; fail=$((fail+1)); }
echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ]
