#!/usr/bin/env bash
# check-template-size.sh — size gate for the governance playbook template.
# The template is the operational ruleset an agent reads every session; it must stay lean.
# Prose that doesn't affect instruction clarity is what gets dropped first: since v3.0 the charter
# is ONE file with no companion to externalize into, so the budget is spent or it is trimmed. The ceiling
# moved 32 KiB -> 48 KiB on owner order (recorded in memory/DECISIONS.md); the PREFERENCE for externalizing
# did not move with it, and the high-water ratchet below is what prices growth now that the ceiling
# is no longer doing it.
#
#   <prefix>/check-template-size.sh            # gate the tracked template
#   <prefix>/check-template-size.sh <file>     # gate one subject
#   <prefix>/check-template-size.sh --bump [<file> ["" [<record>]]]  # re-record the high-water
#
# The ceiling for each subject is DECLARED in <prefix>/template-size-limits.txt with its history
# beside it, and read through the policy kit's budgets.py, that file's ONE reader, at the landed
# revision (TOOL-dGroundRules-9): this script maps its subject's repo-relative key to that census row
# and asks once. A value `budgets."<key>"` in .governance/policy.toml takes the row's place. A
# subject with no row keeps this script's hard default, handed in as `default:`. Whether a breach
# REFUSES is the switch's: `budgets.enforce` (warn by default) and `budgets.pinned`. Under `warn` a
# breach prints a `BUDGET WARN` line and exits 0; under `refuse`, or for a pinned subject, it is
# check 2, naming the rule. The positional limit, the MAX_BYTES environment variable and the
# limits-path override retired with this script's own parse of the file, and a positional limit or
# limits path is refused rather than ignored.
#
# Exit 0 = within budget, or a warned breach (prints one line). Exit 1 = over budget, refused.
# Exit 2 = file missing, or a retired positional given.
# Exit 3 = the high-water record exists but this subject's row is not a number.
# Exit 4 = --bump could not write the high-water record.
# Exit 5 = the DECLARED limit could not be read: a row that is not a number, a cap held in both
#          homes, no policy kit beside this gate, or any other refusal of the policy reader.
# Exit 6 = the subject states its own budget in prose and it disagrees with its declared row.
# Checks 3, 5 and 6 are correctness, never size: they refuse under `warn` too.
#
# THAT LIST IS THE FULL SET OF DISTINCT FAIL_CODE VALUES this file assigns, and it is stated here
# because a gate's own header is where a reader learns what its exit codes mean. It omitted 4 for as
# long as 4 existed, which is the checker-whose-record-does-not-describe-it class one level in.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || ROOT=.
# The two sidecars sit BESIDE this gate, so their defaults are derived from its own directory
# (TOOL-aRepatriatedFork-29 S3): gov runs at whatever kit root it was checked out under.
_self_dir=$(cd "$(dirname "$0")" 2>/dev/null && pwd) || _self_dir="$ROOT"

# Every exit path goes through fail(), which is what puts this gate into check-arms.py's
# population: its FAIL_RE matches `fail <n> "…` and its branches() refuses a message with no
# literal run of 12+ characters to assert on. The exit CODE is carried in FAIL_CODE rather than
# an argument, because the discovery regex reads the check number and the message and would not
# survive a third positional between them. A message may span lines; only the first is asserted.
FAIL_CODE=1
fail() { printf 'TEMPLATE-SIZE check %s FAILED — %s\n' "$1" "$2"; exit "$FAIL_CODE"; }

# `--bump` is a FLAG, not a positional, because the three positionals below are already spoken for
# (subject, limit, record path) and a mode sharing a slot with a path is how one of them silently
# becomes the other. Strip it wherever it appears, then read the positionals from what is left.
BUMP=0
# Rebuild the positional list THROUGH "$@" rather than through a string: an `ARGS="$ARGS $a"`
# accumulator followed by an unquoted `set -- $ARGS` word-splits any path containing whitespace,
# glob-expands a `*`/`?`/`[`, and drops an empty positional — sliding every later argument one
# slot left. That loop also ran on invocations with no --bump at all, so it was a regression on
# the ordinary path, not just the bump one.
if [ "$#" -gt 0 ]; then
  _n=$#
  for _i in $(seq 1 "$_n"); do
    _a=$1; shift
    if [ "$_a" = "--bump" ]; then BUMP=1; else set -- "$@" "$_a"; fi
  done
  unset _n _i _a
fi

FILE=${1:-"$ROOT/coding-governance-agents.template.md"}

# THE RETIRED POSITIONALS (TOOL-dGroundRules-9). `$2` was a limit and `$4` a limits-file path; both
# outranked the declaration, so a caller still passing one would believe it chose a ceiling. Refused,
# never ignored. The record path keeps its slot, `$3`, so an empty `$2` stands before it.
if [ -n "${2:-}" ] || [ -n "${4:-}" ]; then
  FAIL_CODE=2
  _given="${2:-} ${4:-}"   # named, so the harness-arms signature ends at `(given`
  fail 7 "a retired positional was given, and the limit and the limits path are read through the policy kit's budgets.py now; pass the subject, an empty second argument and the record (given $_given)"
fi

# `key` is needed by BOTH the declared-limit lookup and the high-water lookup, so it is derived once
# here rather than twice. Repo-RELATIVE, with both sides normalized through the same `cd && pwd`:
# `git rev-parse --show-toplevel` answers a drive-letter form on this fleet while `pwd` answers the
# POSIX one, so comparing them raw never matches and every key lands machine-absolute — which a
# TRACKED record cannot survive. A subject outside the repo keeps its absolute path, correctly.
# GIT answers both sides since TOOL-dGroundRules-9: `pwd` under a temp dir answers `/tmp/...`,
# `/c/Users/<user>/...` or a short 8.3 name for one directory, so a `pwd` comparison missed whenever
# the caller's spelling differed from git's, and a census subject read as no row at all. A subject
# whose directory git places in THIS repository takes git's own prefix; any other keeps its path.
_name=$(basename "$FILE")
if [ -e "$FILE" ]; then
  _up=.; [[ $FILE == */* ]] && { _up=${FILE%/*}; _up=${_up:-/}; }
  _dir=$(cd "$_up" 2>/dev/null && pwd) || _dir=$_up
  key=$_dir/$_name
  if [ "$(unset GIT_DIR GIT_WORK_TREE; git -C "$_dir" rev-parse --show-toplevel 2>/dev/null)" = "$ROOT" ]; then
    key=$(unset GIT_DIR GIT_WORK_TREE; git -C "$_dir" rev-parse --show-prefix 2>/dev/null)$_name
  fi
else
  key=$FILE
fi

# The interpreter the policy reader runs under, and the sibling-kit resolver that finds it.
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
        # The direct executable where the probe named a file, so a consumer never spawns the
        # Windows App Execution Alias again; the candidate's own name otherwise.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
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
    echo "resolve_python: tried:$_rp_tried"
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
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. `resolve_kit_dir <python> <home> <anchor> <here>` prints the kit directory ABSOLUTE, since
# the subject's repository need not be the one this gate sits in, or the resolver's named refusal
# on stderr and exits 1.
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
print(d.as_posix())' "$2" "$3" "$4"
}

# The DECLARED ceiling and the switch's mode for this subject, in ONE read of the policy reader:
# `budgets.py resolve <key>=default:49152` prints `<key> <value> <mode> <source>`, the value the
# census row's home holds (or the policy file's), and the 48 KiB hard default, source `constant`,
# for a subject no census row names. The reader runs in the subject's repository, whose landed
# revision it reads; every refusal it makes is check 5, and so is a missing policy kit, because
# without it this gate has no declaration to read at all. A reader that refuses ANSWERS, its mode
# `refuse` and the refusal on its stderr (TOOL-dGroundRules-21 S31), so a subject over its cap refuses
# below and is never read as `warn`. No python launcher takes the no-kit branch, and says so once.
budget="" _py="" _pk=""
if ! _py=$(resolve_python "${TEMPLATE_SIZE_PY:-}" 2>&1); then
  budget="no python launcher resolved, so no policy kit can read the declaration: ${_py%%$'\n'*}"; _pk=""
elif _pk=$(resolve_kit_dir "$_py" policy budgets.py "$_self_dir" 2>&1); then
  budget=$(cd "$ROOT" && "$_py" "$_pk/budgets.py" resolve "$key=default:49152" 2>&1) || _pk=""
else
  budget="no policy kit to read the declaration through: $_pk"; _pk=""
fi
if [ -z "$_pk" ]; then
  FAIL_CODE=5
  fail 5 "the declared size limit for this subject could not be read, so nothing is compared: $budget"
fi
IFS=$'\t' read -r _cap MAX_BYTES MODE SOURCE <<<"$budget"
# A row of the census, or the policy file's value, is a DECLARATION; the handed-in default is not.
declared=""
[ "$SOURCE" = constant ] || declared=$MAX_BYTES

# The high-water record, resolved three ways — positional $3, then the environment, then the
# tracked default — because a gate leg cannot set an environment variable and the self-test must
# point the gate at a scratch copy without writing the tracked one.
HIGHWATER=${3:-${HIGHWATER:-"$_self_dir/template-size-highwater.txt"}}

[ -f "$FILE" ] || { FAIL_CODE=2; fail 1 "the file to measure does not exist: $FILE"; }
# Measure LF-NORMALIZED bytes (strip CR) so the gate is checkout-independent — a Windows autocrlf
# smudge to CRLF must not inflate the count and spuriously fail the limit.
bytes=$(tr -d '\r' < "$FILE" | wc -c | tr -d '[:space:]')
name=$(basename "$FILE")

# --- the PAIR TERM ------------------------------------------------------------------------------
# A subject may state its own budget in its own prose. With the ceiling ALSO in a declaration that is
# two spellings of one fact, and a value stated in prose beside the source that owns it rots between
# changes. This branch is the pair: change both or neither.
#
# BEFORE the over-budget branch, deliberately. A disagreement makes the over-budget verdict ambiguous
# — you cannot tell which ceiling you failed — so the disagreement is reported first.
#
# TWO GUARDS, NOT ONE. `[ -n "$declared" ]` keeps a subject with no declared row from being compared
# against this script's hard default. `[ -n "$bline" ]` keeps the three subjects that carry no budget
# line out of the comparison entirely; measured, only the two halves of one byte-compared pair carry
# one at all, and a single guard would have compared the other three against an empty prose value.
#
# AN UNPARSEABLE BUDGET LINE REDS THROUGH THIS SAME BRANCH, and that is the point rather than a side
# effect: `${prose:-…}` is empty when the line says `≤27 KB` instead of bytes, an empty string never
# equals a declared row, so rewriting the prose back to a KB spelling cannot silently disarm the term.
# One branch covers both cases, which also means one arm satisfies check-arms.py.
# A value of 0 is unchecked, as the switch's `check_cap` reads it: there is no ceiling for the prose to agree with.
bline=$(tr -d '\r' < "$FILE" | grep -m1 '^\*\*Budget:')
if [ "$MAX_BYTES" -gt 0 ] && [ -n "$declared" ] && [ -n "$bline" ]; then
  prose=$(printf '%s' "$bline" | sed -n 's/^\*\*Budget:[^0-9]*\([0-9][0-9]*\) bytes.*/\1/p')
  if [ "$prose" != "$declared" ]; then
    FAIL_CODE=6
    fail 6 "the subject states its own budget and disagrees with its declaration: $name says
  '${prose:-no bytes figure}', its declaration (source $SOURCE) says $declared. Two spellings of one fact; change both or
  neither. A budget line this gate cannot parse as bytes reads the same as a wrong one, deliberately."
  fi
fi

# Check 2 obeys the switch. The verdict line is the policy reader's own, so it names the rule that
# set the mode: `budgets.pinned` or `budgets.enforce`. A second read, and only on a breach.
WARNED=0
if [ "$MAX_BYTES" -gt 0 ] && [ "$bytes" -gt "$MAX_BYTES" ]; then
  over=$((bytes - MAX_BYTES))
  verdict=$(cd "$ROOT" && "$_py" "$_pk/budgets.py" check "$key=default:49152" "$bytes" 2>&1); _vrc=$?
  if [ "$MODE" = warn ] && [ "$_vrc" = 0 ]; then
    printf '%s\n' "$verdict"
    WARNED=1
  else
    FAIL_CODE=1
    fail 2 "the file is over its size budget: $name is $bytes bytes, $over over $MAX_BYTES.
  $verdict
  Drop a conditional block, or trim non-instructional prose — the v3.0 charter is ONE file, so
  there is no companion to move a section into.
  Raising the limit is the owner's decision, or a run's on the terms the header of the declared
  limits file beside this gate states; either way it is argued beside the row and recorded in
  memory/DECISIONS.md, never a fix for the edit that hit it. This message is shared with the
  kickoff engine at its own limit."
  fi
fi

# --- the high-water ratchet -------------------------------------------------------------------
# Advisory: it never changes the exit code. Rows are `<path>\t<bytes>`, KEYED BY MEASURED FILE,
# because two consumers ride this script ~14 KB apart and one shared number can only ever serve one
# of them. Absent record = no ratchet plus an explicit line; a non-numeric row is a NAMED failure,
# never a `set -u` explosion at the numeric comparison below.
# The key is REPO-RELATIVE, and both sides are normalized through the same `cd && pwd` before the
# prefix is stripped. `git rev-parse --show-toplevel` answers `C:/projects/...` on this fleet while
# `pwd` answers `/c/projects/...`, so comparing the two raw never matches and every key lands as a
# machine-absolute path — which would make a TRACKED record differ per machine and per worktree.
# A subject outside the repo (the self-test's scratch files) keeps its absolute path, which is
# correct: it has no repo-relative name to have.
# `key` was derived once, above, where the declared-limit lookup also needs it.
recorded=""
if [ -f "$HIGHWATER" ]; then
  recorded=$(awk -F'\t' -v k="$key" '$1 == k { print $2 }' "$HIGHWATER" | tr -d '[:space:]')
fi

# The non-numeric contract is enforced BEFORE the bump branch, not only on the read path. It used
# to sit in the read chain below, so `--bump` over a corrupt record reached $((bytes - recorded))
# and died with a set -u unbound-variable error — the exact "shell error rather than a named
# failure" this gate promises not to do, on the one path that also WRITES.
if [ -n "$recorded" ] && ! printf '%s' "$recorded" | grep -qE '^[0-9]+$'; then
  FAIL_CODE=3
  fail 3 "the high-water record holds a non-numeric value for $key in $HIGHWATER: '$recorded'"
fi

if [ "$BUMP" = 1 ]; then
  # The DIRECTORY is checked before anything is opened. A failed  redirection is reported by
  # the shell itself, so a 2>/dev/null on the command does not suppress it and the caller sees a
  # raw "No such file or directory" instead of this gate naming its own failure.
  # ONE fail site for "could not write". The directory is tested BEFORE anything is opened, because
  # a failed `>` redirection is reported by the shell itself and a 2>/dev/null on the command does
  # not suppress it — the caller would see a raw "No such file or directory" instead of this gate
  # naming its failure. That test and every write below converge here: a second fail site would be a
  # second branch, and the mid-sequence one is unreachable from any fixture on this fleet (the
  # directory test shadows every permission case, and chmod does not deny the owner here). An
  # unarmable branch is either a standing pin or a design smell, and this one was the smell.
  _hwdir=$(dirname "$HIGHWATER")
  _w=0
  { [ -d "$_hwdir" ] && [ -w "$_hwdir" ]; } || _w=1
  tmp="${HIGHWATER}.tmp.$$"
  if [ "$_w" = 0 ]; then
    if [ -f "$HIGHWATER" ]; then
      awk -F'\t' -v k="$key" '$1 != k' "$HIGHWATER" > "$tmp" 2>/dev/null || _w=1
    else
      : > "$tmp" 2>/dev/null || _w=1
    fi
    [ "$_w" = 0 ] && { printf '%s\t%d\n' "$key" "$bytes" >> "$tmp" 2>/dev/null || _w=1; }
    [ "$_w" = 0 ] && { LC_ALL=C sort -o "$tmp" "$tmp" 2>/dev/null || _w=1; }
    [ "$_w" = 0 ] && { mv "$tmp" "$HIGHWATER" 2>/dev/null || _w=1; }
  fi
  if [ "$_w" != 0 ]; then
    rm -f "$tmp" 2>/dev/null
    FAIL_CODE=4
    fail 4 "the high-water record could not be written, so no bump was recorded: $HIGHWATER"
  fi
  if [ -n "$recorded" ]; then
    echo "TEMPLATE-SIZE BUMP — $key high-water $recorded -> $bytes ($((bytes - recorded)) bytes)."
  else
    echo "TEMPLATE-SIZE BUMP — $key high-water recorded at $bytes (no prior row)."
  fi
elif [ ! -f "$HIGHWATER" ]; then
  echo "TEMPLATE-SIZE no-ratchet — no high-water record at $HIGHWATER; growth is unpriced."
elif [ -z "$recorded" ]; then
  echo "TEMPLATE-SIZE no-ratchet — $key has no row in $HIGHWATER; growth is unpriced."
elif ! printf '%s' "$recorded" | grep -qE '^[0-9]+$'; then
  FAIL_CODE=3
  fail 3 "the high-water record holds a non-numeric value for $key in $HIGHWATER: '$recorded'"
elif [ "$bytes" -gt "$recorded" ]; then
  echo "TEMPLATE-SIZE WARN — $name grew past its recorded high-water: $recorded -> $bytes (+$((bytes - recorded))). Advisory only; re-record with --bump when the growth is intended."
fi

# A warned breach has printed its BUDGET WARN line and exits 0 with no OK line: it is not within budget.
[ "$WARNED" = 1 ] && exit 0
[ "$MAX_BYTES" -gt 0 ] || { printf 'template-size OK — %s: %d bytes, unchecked\n' "$name" "$bytes"; exit 0; }
printf 'template-size OK — %s: %d / %d bytes (%d under, %.1f%%)\n' "$name" "$bytes" "$MAX_BYTES" "$((MAX_BYTES - bytes))" "$(awk "BEGIN{print $bytes/$MAX_BYTES*100}")"
