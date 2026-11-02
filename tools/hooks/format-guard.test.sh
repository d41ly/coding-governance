#!/usr/bin/env bash
# Runnable check for format-guard.js — the Stop hook that refuses a routed session's final message
# without the charter's BUILD/SPEC pair or a committed line. Run: bash <prefix>/hooks/format-guard.test.sh
# (exit 0 = all pass)
#
# WHAT THIS FILE DOES NOT CHECK, stated up front: it does not prove the hook is WIRED (check-wiring.sh
# and check-hook-destinations.sh own that), and it does not prove the harness delivers
# `last_assistant_message` on the running CLI — a payload here is built by hand. The build record
# TOOL-aHeardState-1 S9 names holds an in-tree observation on the real card, LIVE.md, charter and HEAD
# with a hand-built payload; harness delivery and the surfaced block are still the owner's to observe.
#
# EVERY ARM RUNS AGAINST A FIXTURE REPOSITORY under the suite's own temp dir: a charter carrying the
# real fence, a LIVE.md naming the routed build, an orientation card under the fixture's common dir,
# and commits made there. The real repository's card, LIVE.md and HEAD are never read, so the suite
# measures the same thing on every node.
set -u
HERE=.; [[ $0 == */* ]] && HERE=${0%/*}
HERE="$(cd "$HERE" && pwd)"
HOOK="$HERE/format-guard.js"
ROOT=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "format-guard.test: not inside a git repository"; exit 2; }
command -v node >/dev/null 2>&1 || { echo "format-guard.test: node is not on PATH"; exit 2; }
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0

# The runlog kit's prose reader, for the AC6 parity arm: resolved, never spelled.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  # THE FLOOR is declared once, in python-floor.txt in gov's lib dir. The literal below is its
  # generated copy, held equal to it by the floor module's `check` and by these blocks' parity rows,
  # because a copy-installed kit has no lib dir to read. A candidate that runs below it is passed
  # over and named, exactly as a candidate that does not run.
  _rp_floor="3.15"
  _rp_fv=$(( ${_rp_floor%%.*} * 1000 + ${_rp_floor#*.} ))
  _rp_tried=""; _rp_seen=""; _rp_best=""; _rp_bv=0; _rp_bver=""; _rp_o1=""; _rp_og=""; _rp_i=0
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    _rp_i=$((_rp_i + 1))
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    # ONE spawn per candidate, isolated: its major.minor and its own executable, forward-slashed,
    # because a backslashed C:\ path handed to MSYS bash loses its separators.
    _rp_out=$("$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))' 2>/dev/null) || _rp_out=""
    _rp_out=${_rp_out%$'\r'}
    if [[ ${_rp_out%% *} =~ ^([0-9]+)\.([0-9]+)$ ]]; then
      _rp_cv=$(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} ))
      if [ "$_rp_cv" -ge "$_rp_fv" ]; then
        # An override, the caller's or GOV_PYTHON, names the command a consumer spawns, a wrapper
        # or a venv launcher included, and is echoed as given. Only the three launcher names give
        # way to the direct executable where the probe named a file; the launcher's own name
        # otherwise. The `[ -f ]` HOLDS on a Windows App Execution Alias, so a Store Python whose
        # own sys.executable is an alias is echoed as printed: a gap the run-gates kit's
        # check_app_alias closes for the legs it measures, and this block does not.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_i" -gt 2 ] && [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
        return 0
      fi
      _rp_why="ran ${_rp_out%% *}, below the floor $_rp_floor"
      if [ "$_rp_cv" -gt "$_rp_bv" ]; then _rp_best=$_rp_c; _rp_bv=$_rp_cv; _rp_bver=${_rp_out%% *}; fi
    else
      _rp_why="did not run"
    fi
    _rp_seen="${_rp_seen}resolve_python:   $_rp_c: $_rp_why"$'\n'
    [ "$_rp_i" != 1 ] || _rp_o1=$_rp_why
    [ "$_rp_i" != 2 ] || _rp_og=$_rp_why
  done
  {
    echo "resolve_python: no usable python launcher at the floor $_rp_floor (python-floor.txt in gov's lib dir)."
    echo "resolve_python: Each candidate was RUN with -I -c — being on PATH is not evidence (the Microsoft Store"
    echo "resolve_python: python3 stub answers \`command -v\` and exits 9009 without running anything)."
    printf '%s' "$_rp_seen"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and $_rp_o1."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and $_rp_og. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
    # THE INSTALL COMMAND, as platforms.provision says. The policy kit's own reader answers it at the
    # landed revision, run by the newest candidate that ran, since its tomllib needs 3.11, and never
    # through the policy shim, which resolves a launcher itself and would re-enter this refusal.
    _rp_prov=name; _rp_pwhy=""
    if [ -z "$_rp_best" ]; then
      _rp_pwhy="no reader ran, because no candidate ran"
    elif [ "$_rp_bv" -lt 3011 ]; then
      _rp_pwhy="no reader ran, because the newest candidate that ran, $_rp_best, is $_rp_bver, below the 3.11 the reader needs"
    else
      IFS= read -r -d '' _rp_rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
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
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
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
      case "${BASH_SOURCE[0]:-}" in */*) _rp_here=${BASH_SOURCE[0]%/*} ;; *) _rp_here=. ;; esac
      _rp_kit=$("$_rp_best" -I -c "${_rp_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$_rp_here" 2>&1) || _rp_pwhy="no reader ran, because ${_rp_kit%$'\r'}"
      if [ -z "$_rp_pwhy" ]; then
        _rp_kit=${_rp_kit%$'\r'}
        _rp_val=$("$_rp_best" "$_rp_kit/policy.py" get platforms.provision 2>/dev/null) || _rp_pwhy="the reader, policy.py get, exited $?"
        _rp_val=${_rp_val%$'\r'}
        case "$_rp_pwhy:$_rp_val" in
          :name|:uv|:off) _rp_prov=$_rp_val ;;
          :*) _rp_pwhy="the reader, policy.py get, printed '$_rp_val', which is no value of the key" ;;
        esac
      fi
    fi
    [ -z "$_rp_pwhy" ] || echo "resolve_python: platforms.provision reads its catalogue default, name: $_rp_pwhy."
    if [ "$_rp_prov" = uv ]; then
      if [ ! -t 2 ]; then _rp_no="not offered, because stderr is not a terminal"
      elif ! uv --version >/dev/null 2>&1; then _rp_no="not offered, because uv does not run"
      else
        printf 'resolve_python: platforms.provision is uv. Run `uv python install %s` now? [y/N] ' "$_rp_floor"
        _rp_a=""; read -r _rp_a </dev/tty || :
        if [ "$_rp_a" = y ]; then
          uv python install "$_rp_floor" || :
          echo "resolve_python: re-run once the floor is on PATH, or name it in GOV_PYTHON."
          _rp_prov=offered
        else
          _rp_no="declined at the prompt"
        fi
      fi
      [ "$_rp_prov" = offered ] || echo "resolve_python: platforms.provision is uv, and the install was $_rp_no."
    fi
    case "$_rp_prov" in
      off) echo "resolve_python: platforms.provision is off, so this refusal names no install command." ;;
      name|uv)
        echo "resolve_python: install the floor with: uv python install $_rp_floor"
        case "${OSTYPE:-}" in msys*|cygwin*|win*) echo "resolve_python: or, on Windows: py install $_rp_floor" ;; esac ;;
    esac
    # LAST, verbatim: the first line names the refusal and this one the candidates, and the lines
    # between them carry the outcomes, the overrides and the install (TOOL-dSafePassage-26 S20).
    echo "resolve_python: tried:$_rp_tried"
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
  local _rkd
  IFS= read -r -d '' _rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
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
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
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
  "$1" -c "${_rkd%$'\n'}"'
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
# no message byte passes through a shell quote. The payload names an empty transcript by default
# (TOOL-aOrientedCast-21), so the agent arm reads a turn with no agent and writes nothing.
: > "$TMP/empty.jsonl"
run_stop() {
  local name=$1 want=$2 msg=$3 extra=${4:-}
  [ -n "$extra" ] || extra='{}'
  node -e '
    const fs = require("fs")
    const p = { hook_event_name: "Stop", session_id: process.argv[2], cwd: process.argv[3], stop_hook_active: false,
                transcript_path: process.argv[5], last_assistant_message: fs.readFileSync(process.argv[1], "utf8") }
    Object.assign(p, JSON.parse(process.argv[4] || "{}"))
    process.stdout.write(JSON.stringify(p))' "$msg" "$SID" "$(resolve_native "$REPO")" "$extra" "$(resolve_native "$TMP")/empty.jsonl" > "$TMP/payload"
  node "$HOOK" < "$TMP/payload" > "$TMP/out" 2> "$TMP/err"
  local rc=$? got=allow
  [ -s "$TMP/out" ] && got=block
  if [ "$rc" = 0 ] && [ "$got" = "$want" ]; then echo "ok   $name ($got)"; pass=$((pass+1))
  else echo "FAIL $name (exit $rc, $got, want $want)"; sed 's/^/     /' "$TMP/out" "$TMP/err"; fail=$((fail+1)); fi
}
check_contains() { # <name> <file> <fixed string>
  if grep -qF -- "$3" "$2"; then echo "ok   $1"; pass=$((pass+1))
  else echo "FAIL $1 (no '$3' in ${2##*/})"; sed 's/^/     /' "$2"; fail=$((fail+1)); fi
}
check_empty() { # <name> <file>
  if [ ! -s "$2" ]; then echo "ok   $1"; pass=$((pass+1))
  else echo "FAIL $1 (${2##*/} not empty)"; sed 's/^/     /' "$2"; fail=$((fail+1)); fi
}
check_absent() { # <name> <file> <fixed string>
  if ! grep -qF -- "$3" "$2"; then echo "ok   $1"; pass=$((pass+1))
  else echo "FAIL $1 ('$3' in ${2##*/})"; sed 's/^/     /' "$2"; fail=$((fail+1)); fi
}

# write_message <name> <line>... — one message file, one argument per line. Every string here is one line and
# the backtick is built from an octal escape, because the codebase map tokenizes this file as a kit
# shell layer and a multi-line or backticked quoted word is where that tokenizer loses its place.
write_message() { local f=$1; shift; printf '%s\n' "$@" > "$TMP/$f.md"; }
B='BUILD — tBuild · Tier-2 · 1/2 build · left TOOL-tBuild-2'
S='SPEC — [TOOL-tBuild-1](memory/builds/tBuild/spec/x.md) · review none'
BT=$'\140'; FENCE="$BT$BT$BT"
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
write_message inline "${FENCE}npm test${FENCE} passed." "" "- $B" "- $S"

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
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${pass:-1} assertions)" || echo "FAIL (${pass:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi

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
check_contains "TOOL-aHeardState-8 the commit defect names both line shapes" "$TMP/out" "committed or merged line"
check_contains "TOOL-aHeardState-8 the reason says not yet terminal" "$TMP/out" "not yet terminal"
sha=$(seed_fixture_commit "two")
printf '%s\n\n- committed — %s · main · two\n' "$(<"$TMP/good.md")" "${sha:0:7}" > "$TMP/reported.md"
run_stop "AC6 a commit named by a committed line allows" allow "$TMP/reported.md"
sha=$(seed_fixture_commit "three")
printf '%s\n\n- committed — 0000000 · main · three\n' "$(<"$TMP/good.md")" > "$TMP/wrong.md"
run_stop "AC6 a committed line naming another sha blocks" block "$TMP/wrong.md"
sha=$(seed_fixture_commit "four")
printf '%s\n\n- merged — --no-ff tBranch → main · %s\n' "$(<"$TMP/good.md")" "${sha:0:8}" > "$TMP/merged.md"
run_stop "AC6 a merged line naming the commit allows" allow "$TMP/merged.md"
# TOOL-aHeardState-7 — a chained stop leaves the baseline alone, so its commit is owed at the next
# unchained stop: the behaviour the header now states.
sha=$(seed_fixture_commit "five")
run_stop "TOOL-aHeardState-7 a chained stop after a commit allows" allow "$TMP/good.md" '{"stop_hook_active":true}'
run_stop "TOOL-aHeardState-7 the next unchained stop demands the chained commit" block "$TMP/good.md"
check_contains "TOOL-aHeardState-7 the reason names the chained commit" "$TMP/out" "commit ${sha:0:9}"

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

# TOOL-aHeardState-8 — the closing review's fixtures, each a branch no arm ran before.
# M3: an inline triple-backtick span is not a fence, so the pair after it stays bare.
seed_repo "$TMP/charter.md"
run_stop "TOOL-aHeardState-8 an inline backtick span leaves the pair bare" allow "$TMP/inline.md"
# M6: a payload without last_assistant_message allows, with a witness.
run_stop "TOOL-aHeardState-8 a payload with no message allows" allow "$TMP/none.md" '{"last_assistant_message":null}'
check_contains "TOOL-aHeardState-8 the witness names the missing message" "$TMP/err" "no last_assistant_message"
# M7: a routed unit with no spec owes the BUILD line alone; the spec'd route owes SPEC too.
write_message buildonly "Done." "" "- $B"
printf '## route\n- build: tBuild\n- unit: TOOL-tBuild-1\n' > "$REPO/.git/orientation/$SID.md"
run_stop "TOOL-aHeardState-8 a spec-less route allows a lone BUILD line" allow "$TMP/buildonly.md"
seed_repo "$TMP/charter.md"
run_stop "TOOL-aHeardState-8 the spec'd route blocks the same lone BUILD line" block "$TMP/buildonly.md"
check_contains "TOOL-aHeardState-8 the reason names the missing SPEC line" "$TMP/out" "no SPEC line"
# L5: a sidecar sha that is not an ancestor of HEAD writes a witness and blocks nothing.
seed_repo "$TMP/charter.md"
seed_fixture_commit "six" >/dev/null
run_stop "TOOL-aHeardState-8 a baseline stop before the reset allows" allow "$TMP/good.md"
git -C "$REPO" reset -q --hard HEAD~1
run_stop "TOOL-aHeardState-8 a HEAD reset behind the baseline allows" allow "$TMP/good.md"
check_contains "TOOL-aHeardState-8 the reset writes the no-first-parent witness" "$TMP/err" "along no first-parent path"
# M5: a linked worktree as the payload cwd keeps its sidecar under the worktree's own git dir.
seed_repo "$TMP/charter.md"
git -C "$REPO" worktree add -q "$TMP/wt" -b tWorktree 2>/dev/null
REPO="$TMP/wt" run_stop "TOOL-aHeardState-8 a linked worktree's first stop allows" allow "$TMP/good.md"
if [ -s "$TMP/repo/.git/worktrees/wt/format-guard/$SID.head" ]; then echo "ok   TOOL-aHeardState-8 the worktree's sidecar lands under .git/worktrees/wt"; pass=$((pass+1))
else echo "FAIL TOOL-aHeardState-8 no sidecar under .git/worktrees/wt/format-guard"; fail=$((fail+1)); fi
# M4: an unreadable HEAD skips the commit check with a witness, never silently.
seed_repo "$TMP/charter.md"
printf 'ref: refs/heads/tNowhere\n' > "$REPO/.git/HEAD"
run_stop "TOOL-aHeardState-8 an unreadable HEAD allows" allow "$TMP/good.md"
check_contains "TOOL-aHeardState-8 the witness names the unreadable HEAD" "$TMP/err" "HEAD is unreadable"

# TOOL-aOrientedCast-21 — every agent the turn dispatched or received owes its bare line.
# write_transcript <scenario> — a fixture transcript at $TMP/sess/$SID.jsonl and its session dir, built
# by node from JSON objects so no byte crosses a shell quote; prints the payload field naming it.
write_transcript() {
  rm -rf "$TMP/sess"; mkdir -p "$TMP/sess"
  node -e '
    const fs = require("fs"), path = require("path")
    const [scenario, file] = process.argv.slice(1)
    const dir = file.replace(/\.jsonl$/, "")
    const typed = (text) => ({ type: "user", message: { role: "user", content: text } })
    const call = (id, name) => ({ type: "assistant", message: { role: "assistant", content: [{ type: "tool_use", id, name, input: {} }] } })
    const result = (id, r) => ({ type: "user", message: { role: "user", content: [{ type: "tool_result", tool_use_id: id, content: "ok" }] }, toolUseResult: r })
    const said = (text) => ({ type: "assistant", message: { role: "assistant", content: [{ type: "text", text }] } })
    // A notification with no id leaves its header without one; a body becomes its <result> (TOOL-aOrientedCast-24).
    const block = (id, body) => "<task-notification>\n" + (id ? "<tool-use-id>" + id + "</tool-use-id>\n" : "") + "<status>completed</status>\n" + (body ? "<result>" + body + "</result>\n" : "") + "</task-notification>"
    const notice = (id, body) => ({ type: "user", origin: { kind: "task-notification" }, message: { role: "user", content: block(id, body) } })
    const queued = (id) => ({ type: "attachment", attachment: { type: "queued_command", prompt: block(id) } })
    const meta = (text, extra) => Object.assign({ type: "user", isMeta: true, message: { role: "user", content: [{ type: "text", text }] } }, extra || {})
    const summary = { type: "user", isCompactSummary: true, message: { role: "user", content: "This session is being continued from a previous conversation." } }
    const journal = (sub, entries) => {
      fs.mkdirSync(path.join(dir, "subagents", sub), { recursive: true })
      fs.writeFileSync(path.join(dir, "subagents", sub, "journal.jsonl"), entries.map((e) => JSON.stringify(e)).join("\n") + "\n")
    }
    const dispatch = [call("t1", "Agent"), result("t1", { status: "async_launched", agentId: "a1" })]
    const agentTurn = [typed("go"), ...dispatch, said("Launched.")]
    const runTurn = [typed("go"), call("t2", "Workflow"), result("t2", { status: "async_launched", runId: "wf_t-1" }), said("Launched.")]
    const quotedTurn = [typed("go"), ...dispatch, call("t9", "Agent"), result("t9", { status: "async_launched", agentId: "a9" }), said("Launched.")]
    const quote = "I also saw <tool-use-id>t9</tool-use-id> go by."
    const records = {
      agent: agentTurn,
      "agent-notified": [...agentTurn, notice("t1"), said("Done.")],
      run: runTurn,
      "run-notified": [...runTurn, notice("t2"), said("Done.")],
      "bad-run": [typed("go"), call("t3", "Workflow"), result("t3", { status: "async_launched", runId: "../x" }), said("Launched.")],
      quoted: [...quotedTurn, notice("t1", quote), said("Done.")],
      "quoted-headless": [...quotedTurn, notice(null, quote), said("Done.")],
      skill: [typed("go"), ...dispatch, call("t5", "Skill"), result("t5", { success: true }), meta("Base directory for this skill: x", { sourceToolUseID: "t5" }), said("Done.")],
      image: [typed("go"), ...dispatch, call("t6", "Read"), result("t6", { type: "image" }), meta("[Image: original 10x10, displayed at 10x10]"), said("Done.")],
      compact: [typed("go"), ...dispatch, { type: "system", subtype: "compact_boundary", content: "Conversation compacted" }, summary, said("Done.")],
      tick: [...agentTurn, meta("<tick>"), said("Idle.")],
      queued: [...agentTurn, queued("t1"), said("Done.")],
      foreground: [typed("go"), call("t1", "Agent"), result("t1", { status: "completed", agentId: "a1" }), said("Done.")],
      "run-foreground": [typed("go"), call("t2", "Workflow"), result("t2", { status: "completed", runId: "wf_t-1" }), said("Done.")],
      torn: [typed("go"), call("t1", "Agent"), "{torn", result("t1", { status: "async_launched", agentId: "a1" }), said("Launched.")],
    }[scenario]
    // A string element is one raw line, which is how the torn line is written.
    fs.writeFileSync(file, records.map((r) => (typeof r === "string" ? r : JSON.stringify(r))).join("\n") + "\n")
    const started = [{ type: "started", agentId: "a2" }, { type: "started", agentId: "a3" }]
    const ended = scenario === "run-notified" || scenario === "run-foreground"
    journal("workflows/wf_t-1", ended ? [...started, { type: "result", agentId: "a2" }, { type: "failed", agentId: "a3" }] : started)
    journal("x", [{ type: "started", agentId: "aOutside" }])
    process.stdout.write(JSON.stringify({ transcript_path: file }))' "$1" "$(resolve_native "$TMP/sess")/$SID.jsonl"
}
A1='agent — gov-builder · effort high · model m · TOOL-tBuild-1 · prompt [x.txt](x.txt) · writes product · gates none · run direct/a1'
R1='returned — gov-builder · committed · 3m · 12k out · run direct/a1'
A2='agent — gov-builder · effort high · model m · TOOL-tBuild-1 · prompt [x.txt](x.txt) · writes product · gates none · run wf_t-1/a2'
A3='agent — gov-builder · effort high · model m · TOOL-tBuild-2 · prompt [y.txt](y.txt) · writes product · gates none · run wf_t-1/a3'
R2='returned — gov-builder · committed · 3m · 12k out · run wf_t-1/a2'
R3='returned — gov-builder · failed · 1m · 2k out · run wf_t-1/a3'
write_message agent1   "Done." "" "- $A1" "- $B" "- $S"
write_message agenttick "Done." "" "- $BT$A1$BT" "- $B" "- $S"
write_message agentcut "Done." "" "- ${A1/run direct/direct}" "- $B" "- $S"
write_message returned1 "Done." "" "- $R1" "- $B" "- $S"
write_message runboth  "Done." "" "- $A2" "- $A3" "- $B" "- $S"
write_message runa2    "Done." "" "- $A2" "- $B" "- $S"
write_message runall   "Done." "" "- $A2" "- $A3" "- $R2" "- $R3" "- $B" "- $S"
seed_repo "$TMP/charter.md"
TP=$(write_transcript agent)
run_stop "TOOL-aOrientedCast-21 a dispatched agent with no agent line blocks" block "$TMP/good.md" "$TP"
check_contains "TOOL-aOrientedCast-21 the reason names the agent" "$TMP/out" "agent a1"
check_contains "TOOL-aOrientedCast-21 the reason says the turn dispatched it" "$TMP/out" "which this turn dispatched"
check_contains "TOOL-aOrientedCast-21 the reason names the verb" "$TMP/out" "handoff.py agents"
run_stop "TOOL-aOrientedCast-21 a bare agent line ending run direct/a1 allows" allow "$TMP/agent1.md" "$TP"
run_stop "TOOL-aOrientedCast-21 the agent line in backticks blocks" block "$TMP/agenttick.md" "$TP"
check_contains "TOOL-aOrientedCast-21 the backticked line names rule r1" "$TMP/out" "rule r1"
run_stop "TOOL-aOrientedCast-21 the agent line with its last field cut blocks" block "$TMP/agentcut.md" "$TP"
check_contains "TOOL-aOrientedCast-21 the cut line names its charter shape" "$TMP/out" "does not match its charter shape"
TP=$(write_transcript agent-notified)
run_stop "TOOL-aOrientedCast-21 a received agent with no returned line blocks" block "$TMP/good.md" "$TP"
check_contains "TOOL-aOrientedCast-21 the reason names the returned line for a1" "$TMP/out" "no returned line for agent a1"
run_stop "TOOL-aOrientedCast-21 a returned line alone allows: the earlier dispatch is not owed again" allow "$TMP/returned1.md" "$TP"
TP=$(write_transcript run)
run_stop "TOOL-aOrientedCast-21 both of a run's started agents shown allows" allow "$TMP/runboth.md" "$TP"
run_stop "TOOL-aOrientedCast-21 a run's agent left out blocks" block "$TMP/runa2.md" "$TP"
check_contains "TOOL-aOrientedCast-21 the reason names the agent left out" "$TMP/out" "agent a3"
check_absent "TOOL-aOrientedCast-21 the reason does not name the agent shown" "$TMP/out" "agent a2"
TP=$(write_transcript run-notified)
run_stop "TOOL-aOrientedCast-21 a received run owes its returned lines too" block "$TMP/runboth.md" "$TP"
check_contains "TOOL-aOrientedCast-21 the reason names a failed agent's returned line" "$TMP/out" "no returned line for agent a3"
run_stop "TOOL-aOrientedCast-21 a received run with all four lines allows" allow "$TMP/runall.md" "$TP"
awk -v bt="$BT" 'index($0, "- " bt "agent — ") != 1' "$TMP/charter.md" > "$TMP/noagent.md"
grep -qF -- "- ${BT}agent — " "$TMP/noagent.md" && { echo "FAIL TOOL-aOrientedCast-21 the fixture edit did not delete the agent definition"; fail=$((fail+1)); }
seed_repo "$TMP/noagent.md"
TP=$(write_transcript agent)
run_stop "TOOL-aOrientedCast-21 a charter with no agent shape allows" allow "$TMP/good.md" "$TP"
check_contains "TOOL-aOrientedCast-21 the witness names the missing agent shape" "$TMP/err" "no agent shape"
check_contains "TOOL-aOrientedCast-21 the witness counts the agent" "$TMP/err" "1 agent(s)"
run_stop "TOOL-aOrientedCast-21 a charter with no agent shape and no agent in the turn allows" allow "$TMP/good.md"
check_empty "TOOL-aOrientedCast-21 no agent in the turn writes nothing" "$TMP/err"
seed_repo "$TMP/charter.md"
run_stop "TOOL-aOrientedCast-21 a payload with no transcript_path allows" allow "$TMP/good.md" '{"transcript_path":null}'
check_contains "TOOL-aOrientedCast-21 the witness names transcript_path" "$TMP/err" "transcript_path"
TP=$(write_transcript bad-run)
# The fixture plants a journal at subagents/x, where ../x would land: read, its agent would block.
run_stop "TOOL-aOrientedCast-21 a run id off its shape allows, its outside journal unread" allow "$TMP/good.md" "$TP"
check_contains "TOOL-aOrientedCast-21 the witness names the run id" "$TMP/err" '"../x"'

# TOOL-aOrientedCast-24 — the notification's header id (M1), the two opener exceptions and the tick they
# must not reach (M2), both delivery routes and the foreground endings (M7), and a torn line (L1).
write_message agentret "Done." "" "- $A1" "- $R1" "- $B" "- $S"
seed_repo "$TMP/charter.md"
TP=$(write_transcript quoted)
run_stop "TOOL-aOrientedCast-24 a notification quoting another id in its result allows the R1 message" allow "$TMP/returned1.md" "$TP"
run_stop "TOOL-aOrientedCast-24 the same notification blocks pair-only" block "$TMP/good.md" "$TP"
check_contains "TOOL-aOrientedCast-24 the reason names the header's agent" "$TMP/out" "no returned line for agent a1"
check_absent "TOOL-aOrientedCast-24 the reason does not name the quoted agent" "$TMP/out" "agent a9"
TP=$(write_transcript quoted-headless)
run_stop "TOOL-aOrientedCast-24 a notification with no header id requires nothing its result quotes" allow "$TMP/good.md" "$TP"
for sc in skill image compact; do
  TP=$(write_transcript "$sc")
  run_stop "TOOL-aOrientedCast-24 the $sc record opens no turn: pair-only blocks" block "$TMP/good.md" "$TP"
  check_contains "TOOL-aOrientedCast-24 the $sc reason names the agent" "$TMP/out" "agent a1"
  check_contains "TOOL-aOrientedCast-24 the $sc reason says the turn dispatched it" "$TMP/out" "which this turn dispatched"
done
TP=$(write_transcript tick)
run_stop "TOOL-aOrientedCast-24 an idle tick after assistant text opens the turn: pair-only allows" allow "$TMP/good.md" "$TP"
check_empty "TOOL-aOrientedCast-24 the tick writes nothing to stderr" "$TMP/err"
for sc in queued foreground; do
  TP=$(write_transcript "$sc")
  run_stop "TOOL-aOrientedCast-24 the $sc agent's agent line alone blocks" block "$TMP/agent1.md" "$TP"
  check_contains "TOOL-aOrientedCast-24 the $sc reason names the returned line" "$TMP/out" "no returned line for agent a1"
  run_stop "TOOL-aOrientedCast-24 the $sc agent's two lines allow" allow "$TMP/agentret.md" "$TP"
done
TP=$(write_transcript run-foreground)
run_stop "TOOL-aOrientedCast-24 a foreground run's agent lines alone block" block "$TMP/runboth.md" "$TP"
check_contains "TOOL-aOrientedCast-24 the reason names the failed agent's returned line" "$TMP/out" "no returned line for agent a3"
run_stop "TOOL-aOrientedCast-24 a foreground run with all four lines allows" allow "$TMP/runall.md" "$TP"
TP=$(write_transcript torn)
run_stop "TOOL-aOrientedCast-24 a torn line in the turn still grades its agent: pair-only blocks" block "$TMP/good.md" "$TP"
check_contains "TOOL-aOrientedCast-24 the torn reason names the agent" "$TMP/out" "agent a1"
check_contains "TOOL-aOrientedCast-24 the witness counts the torn line" "$TMP/err" "1 line(s)"

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
names="good none tick indent bold head fenced first gap noleft inline"
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
# messages and its liveness); 57 = 54 + TOOL-aHeardState-7's three chained-stop assertions; 73 =
# 57 + TOOL-aHeardState-8's 16: 2 wording, 13 in its fixture block, 1 inline parity message; 101 =
# 73 + TOOL-aOrientedCast-21's 28 agent-line assertions; 129 = 101 + TOOL-aOrientedCast-24's 28: 4 quoted,
# 1 headless, 9 in the three-record loop, 2 tick, 6 in the two-route loop, 3 foreground-run, 3 torn.
# The pin sits alone on its line because the testsuite-counts leg reads it anchored.
FLOOR_ASSERTIONS=129
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; fail=$((fail+1)); }
echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ]
