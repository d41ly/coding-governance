#!/usr/bin/env bash
# chain-packet.test.sh — red/green arms for <prefix>/chain-packet.py (TOOL-aBatchedPacket-1).
#
#   bash <prefix>/chain-packet.test.sh    # "PASS (N assertions)" + exit 0 = good
#
# The door runs the dClosedLoop packet instrument's own `main` with two reads answered in-process,
# and falls back to the instrument as a child when an instrument's blob is not the one its
# shortcuts were read against. So the arms are of two kinds:
#
#   CP1, CP2   fixture S, a scratch repository holding only a STUB at the packet instrument's path.
#              The blob binding must send the stub down the fallback, and no instrument at all must
#              be the door's own refusal.
#   CP3-CP9    fixture T, a scratch clone of this repository at HEAD with the REAL instruments, its
#              chain specs trimmed to two of $SLUG and every spec of $PARENT that holds a carry
#              line, so the instrument's own walk costs seconds and the parent's state in T, yes
#              and yes, depends on those specs' text. The door and the instrument must print the
#              same stdout and exit alike on a stale packet and on a green one, the packet the
#              door wrote must hold the parent's line, `--parity` must say identical, a moved
#              instrument must fall back, and a spec revision the instrument refuses on must make
#              `--parity` say DIFFERENT.
#   CP8        the parent read's cache, graded against git's own. A probe loads the door, installs
#              the reads, makes the instrument's git raise, and compares the answer for each kept
#              parent path, one holding a lone CR, with a `git show` the probe ran itself.
#   CP9        the door and the instrument under `GIT_DIR` naming a second git directory whose
#              HEAD holds one parent spec OPEN: both must print the same red stdout and exit 1,
#              and the door must say on stderr that the instrument's own git read the parents.
#
# CP3, CP4 and CP5 also assert that the door's stderr holds no `chain-packet:` line at all, so a
# run that fell back cannot pass as a fast one: that covers the shortcuts-off line, the in-process
# report's own fallback notice, and the notice of a git location variable. WHEN AN INSTRUMENT'S
# BLOB HAS MOVED AT HEAD those three arms fail and print the door's line naming the role (the
# spec's F2): read that instrument's reliance points, listed beside its constant in the door,
# against the new bytes, then set the constant.
#
# HERMETIC: both fixtures are scratch copies under mktemp -d and the real tree is only cloned,
# never written. Their content is this tree's records at HEAD.
#
# What it does not check: the full tree, speed, the `--fixture` route, and a moved `carries` or
# `packet` role on real bytes, which CP6 shows for the schedule role only. Nor
# (TOOL-aBatchedPacket-2): a git variable outside `tree_lib.GIT_ENV_LEAKS`, a graft file among
# them, under which the batch reader and the instrument's git still run under different
# environments; a leak variable that is set and harmless, on which the door declines by presence,
# so under one CP3 to CP5 red naming the door's notice, which is the true reading of that run; the
# report read under a foreign git directory, which reads working-tree files on both paths, CP9
# comparing only the two outputs; a parent spec that is not UTF-8, in CP8, which the batch answers
# None and the instrument's git reads, CP8 holding no such path; the README refusal of fixture T's
# trim, which no arm stages; whether the checker copy that the checker suite's marker-door arm runs
# is the tracked checker, since that arm makes the copy; and the class, since no gate finds another
# leg whose suite reads past its guard.
#
# RECORDS, UNDER CHANGED MODE. The leg's guard is the tool root and the instrument folder, so this
# leg is not selected under changed mode by a change that moves only records. The records fixture T
# reads are the tracked specs of $SLUG and $PARENT, the first line and front matter of every
# packet-holding build's README, the tracked packets under `memory/builds/*/prompts/`, the v2
# design file the instruments name, and `memory/DECISIONS.md`. After a change to any of them the
# route is the bar with `GATE_FULL=1`.
set -u
case "${BASH_SOURCE[0]:-}" in */*) HERE=${BASH_SOURCE[0]%/*} ;; *) HERE=. ;; esac
HERE=$(cd "$HERE" && pwd) || exit 2
DOOR="$HERE/chain-packet.py"

# The shrink-only assertion floor. A suite that stops running arms must RED rather than report a
# smaller success: `check-testsuite-counts.sh` reads this pin, the printed count, and the comparison
# between them. One assertion per arm, CP1 to CP9.
# RAISED 7 -> 9 by TOOL-aBatchedPacket-2: its two arms, CP8 over the parent read's cache and CP9
# under a foreign GIT_DIR, each top-level. Counted by reading; OWED: observed at the close.
FLOOR_ASSERTIONS=9
# The launcher is RESOLVED by running it; `PY=` overrides. The resolver is carried INLINE, as in the
# checker's suite beside this one.
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
[ -n "${PY:-}" ] || PY=$(resolve_python) || exit 2
ROOT=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel) || { echo "chain-packet.test: not inside a git repository"; exit 2; }
# The instruments are DERIVED by shape, as the door derives them: no unit id is spelled here.
INST=$(git -C "$ROOT" ls-files -- ':(glob)memory/builds/dClosedLoop/build/*-build-*-packet.py')
SCHED=$(git -C "$ROOT" ls-files -- ':(glob)memory/builds/dClosedLoop/build/*-build-*-schedule.py')
[ -f "$ROOT/$INST" ] && [ -f "$ROOT/$SCHED" ] || { echo "chain-packet.test: this tree tracks no single packet and schedule instrument, so there is nothing to run the door over"; exit 2; }
# Fixture T's pair: a chain build and one of its parents. Any pair serves whose trimmed tree leaves
# the build's packet stale; these two are the chain's oldest.
SLUG=dGroundRules
PARENT=dTrueNorth
pass=0; fail=0
out=; err=; rc=0

print_pass() { echo "arm ok    $1"; pass=$((pass+1)); }
print_fail() { echo "arm FAIL  $1 — $2"; fail=$((fail+1)); }
run_in() {           # $1 dir · $2 script · the rest its arguments. Sets out, err and rc; CR dropped.
  local d=$1 script=$2
  shift 2
  out=$(cd "$d" && "$PY" "$script" "$@" 2>"$base/stderr"); rc=$?
  err=$(<"$base/stderr")
  out=${out//$'\r'/}; err=${err//$'\r'/}
}

base=$(mktemp -d) || { echo "chain-packet.test: mktemp failed"; exit 2; }
trap 'rm -rf "$base"' EXIT

# ---- fixture S: a stub at the packet instrument's path, as the checker suite's packet arms build it.
S=$base/s
git init -q "$S"; git -C "$S" config user.email t@t.test; git -C "$S" config user.name t
mkdir -p "$S/${INST%/*}"
printf 'import sys\nprint("packet: tChain - stub - byte compare red")\nsys.exit(1)\n' > "$S/$INST"
git -C "$S" add -A >/dev/null 2>&1; git -C "$S" commit -qm stub --no-verify

run_in "$S" "$DOOR" --check tChain
if [ "$rc" = 1 ] && [ "$out" = "packet: tChain - stub - byte compare red" ] \
   && [[ $err == "chain-packet: shortcuts off"*"carries: no file"* ]] && [[ $err != *$'\n'* ]]; then
  print_pass "CP1 a stub at the instrument's path runs as a child: its line, its exit 1, and one shortcuts-off line naming carries: no file"
else
  print_fail "CP1 a stub at the instrument's path runs as a child" "rc $rc, stdout '$out', stderr '$err'"
fi
# FOREIGN_PREFIX_PROBE: the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${pass:-1} assertions)" || echo "FAIL (${pass:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi

rm -f "$S/$INST"
run_in "$S" "$DOOR" --check tChain
if [ "$rc" = 2 ] && [[ $out == "chain-packet: 0 files match the packet instrument's shape"* ]]; then
  print_pass "CP2 no packet instrument is the door's own refusal on stdout, exit 2"
else
  print_fail "CP2 no packet instrument is the door's own refusal on stdout, exit 2" "rc $rc, stdout '$out', stderr '$err'"
fi

# ---- fixture T: a clone at HEAD, made as the foreign-prefix leg makes its clone. One commit leaves
# two specs in $SLUG's spec folder, every spec of $PARENT's that holds a carry line, and no other
# chain spec; the chain builds are the builds holding a packet. The carry pattern below is a copy of
# the head of `schedule.py#CARRY`, graded by CP4: a pattern that keeps too few specs leaves a
# clause uncarried and the parent's line reads `specs done no`. A build left with no spec gets a
# `status:` front-matter key in the same commit, because the index generator the instrument runs
# for the open asks refuses a build whose status it can derive from nothing.
T=$base/t
HEADSHA=$(git -C "$ROOT" rev-parse HEAD)
git clone -q --no-hardlinks "$ROOT" "$T" || { echo "chain-packet.test: could not clone $ROOT"; exit 2; }
git -C "$T" checkout -q -B chain-packet "$HEADSHA" || { echo "chain-packet.test: the clone cannot check out HEAD $HEADSHA"; exit 2; }
git -C "$T" config user.email t@t.test; git -C "$T" config user.name t
declare -A kept=()
keep=()
while IFS= read -r f; do
  kept[$f]=1; keep+=("$f")
  [ "${#keep[@]}" -lt 2 ] || break
done < <(git -C "$T" ls-files -- ":(glob)memory/builds/$SLUG/spec/*.md")
slug_kept=${#keep[@]}
while IFS= read -r f; do
  kept[$f]=1; keep+=("$f")
done < <(git -C "$T" grep -lE '^\*\*(Carries|Moved|Retired|Deferred):\*\* cl-' -- ":(glob)memory/builds/$PARENT/spec/*.md")
parent_kept=$(( ${#keep[@]} - slug_kept ))
chain=()
while IFS= read -r p; do
  b=${p#memory/builds/}; chain+=("${b%%/*}")
done < <(git -C "$T" ls-files -- ':(glob)memory/builds/*/prompts/*-prompt-*-packet.md')
[ "$slug_kept" = 2 ] && [ "$parent_kept" -ge 1 ] && [ "${#chain[@]}" -ge 2 ] || { echo "chain-packet.test: fixture T found $slug_kept spec(s) of $SLUG and $parent_kept carry-holding spec(s) of $PARENT to keep and ${#chain[@]} chain build(s), so its arms would read nothing"; exit 2; }
PARENT_SPEC=${keep[2]}      # the first kept parent spec: it takes the lone CR, and CP9's OPEN status
for b in "${chain[@]}"; do
  while IFS= read -r f; do
    [ -n "${kept[$f]:-}" ] || printf '%s\n' "$f"
  done < <(git -C "$T" ls-files -- "memory/builds/$b/spec/")
done | git -C "$T" rm -q --pathspec-from-file=- >/dev/null
# The key goes in after line 1 only where that lands inside front matter holding no status yet.
for b in "${chain[@]}"; do
  [ "$b" != "$SLUG" ] && [ "$b" != "$PARENT" ] || continue
  awk 'NR == 1 { sub(/\r$/, ""); if ($0 != "---") { bad = 1; exit }; fenced = 1; next }
       /^---/ { exit }
       /^status:/ { bad = 1; exit }
       END { exit (bad || !fenced) }' "$T/memory/builds/$b/README.md" \
    || { echo "chain-packet.test: fixture T cannot place a status key in memory/builds/$b/README.md: its first line is not the front-matter fence, or its front matter already holds a status key"; exit 2; }
  sed -i '1a status: CLOSED' "$T/memory/builds/$b/README.md"
done
# One line holding a lone CR, a CR with no LF after it. It matches neither of the schedule
# instrument's two patterns, so the parent's state is unmoved, and CP8 counts it in the blob.
printf 'A line holding a lone CR,\rfor the parent read (chain-packet.test fixture T).\n' >> "$T/$PARENT_SPEC"
git -C "$T" commit -qam trim --no-verify || { echo "chain-packet.test: fixture T's trim commit failed"; exit 2; }

# CP9's second git directory, U: one commit past the trim holds the first kept parent spec OPEN, T's
# branch and working tree return to the trim, and a linked worktree of T with no checkout has that
# commit as its HEAD and as its index. Under GIT_DIR=$U a git run in T therefore reads T's files
# and U's history, where the parent is not done.
sed -i 's/^\*\*Status:\*\* CLOSED/**Status:** OPEN/' "$T/$PARENT_SPEC"
git -C "$T" commit -qam 'the first kept parent spec OPEN' --no-verify || { echo "chain-packet.test: fixture T's OPEN commit failed, so CP9 has no foreign HEAD"; exit 2; }
FOREIGN=$(git -C "$T" rev-parse HEAD)
git -C "$T" reset -q --hard HEAD~1
git -C "$T" worktree add -q --no-checkout --detach "$base/u" "$FOREIGN" >/dev/null 2>&1 \
  && U=$(git -C "$base/u" rev-parse --absolute-git-dir) && git -C "$base/u" read-tree HEAD \
  || { echo "chain-packet.test: fixture T could not make the second git directory at $FOREIGN"; exit 2; }

# CP3 — the stale packet: both print the same lines and exit 1, and the door did not fall back.
run_in "$T" "$DOOR" --check "$SLUG"; d_out=$out d_rc=$rc d_err=$err
run_in "$T" "$INST" --check "$SLUG"
if [ "$d_rc" = 1 ] && [ "$rc" = 1 ] && [ "$d_out" = "$out" ] && [[ $out == *"byte compare red"* ]] \
   && [[ $d_err != *"chain-packet:"* ]]; then
  print_pass "CP3 on a stale packet the door's --check and the instrument's print the same stdout and both exit 1"
else
  print_fail "CP3 on a stale packet the door's --check and the instrument's print the same stdout and both exit 1" "door rc $d_rc, instrument rc $rc, door stderr '$d_err', door stdout '${d_out:0:300}', instrument stdout '${out:0:300}'"
fi

# CP4 — the door's --write, then the green packet: the same lines and exit 0, with no fallback, and
# the packet the door wrote holds the parent's line as the kept parent specs' text gives it. The
# instrument's --check compares that file with its own render, so a door that read a parent text
# otherwise fails both.
run_in "$T" "$DOOR" --write "$SLUG"; w_out=$out w_rc=$rc w_err=$err
written=${w_out#packet: wrote }; written=${written%%$'\n'*}
run_in "$T" "$DOOR" --check "$SLUG"; d_out=$out d_rc=$rc d_err=$err
run_in "$T" "$INST" --check "$SLUG"
green_out=$d_out
if [ "$w_rc" = 0 ] && [[ $w_out == "packet: wrote "* ]] && [ "$d_rc" = 0 ] && [ "$rc" = 0 ] && [ "$d_out" = "$out" ] \
   && [[ $out == *"byte compare green"* ]] && [[ $w_err$d_err != *"chain-packet:"* ]] \
   && (cd "$T" && grep -q "^- $PARENT: specs done yes, build done yes" "$written") 2>/dev/null; then
  print_pass "CP4 the door's --write prints packet: wrote, its packet holds the parent's line specs done yes, build done yes, then both --check runs print the same stdout and exit 0"
else
  print_fail "CP4 the door's --write prints packet: wrote, its packet holds the parent's line specs done yes, build done yes, then both --check runs print the same stdout and exit 0" "write rc $w_rc '$w_out', door rc $d_rc, instrument rc $rc, door stderr '$w_err$d_err', parent line '$(cd "$T" && grep "^- $PARENT: " "$written" 2>/dev/null)', door stdout '${d_out:0:300}', instrument stdout '${out:0:300}'"
fi

# CP5 — parity on the real instruments: identical, with a byte count.
run_in "$T" "$DOOR" --parity "$SLUG"
if [ "$rc" = 0 ] && [[ $out =~ ^"chain-packet: parity $SLUG · identical · "[0-9]+" bytes · " ]] && [[ $err != *"chain-packet:"* ]]; then
  print_pass "CP5 --parity prints identical with a byte count and exits 0"
else
  print_fail "CP5 --parity prints identical with a byte count and exits 0" "rc $rc, stdout '${out:0:300}', stderr '$err'"
fi

# CP6 — one byte appended to the REAL schedule instrument, uncommitted: the door falls back naming
# that role, and the instrument's own run prints what CP4's green check printed.
printf '#' >> "$T/$SCHED"
run_in "$T" "$DOOR" --check "$SLUG"
git -C "$T" checkout -q -- "$SCHED"
if [ "$rc" = 0 ] && [ "$out" = "$green_out" ] && [ -n "$green_out" ] \
   && [[ $err == "chain-packet: shortcuts off"*"schedule: blob "* ]]; then
  print_pass "CP6 a moved schedule instrument turns the shortcuts off naming schedule, and stdout and exit equal CP4's"
else
  print_fail "CP6 a moved schedule instrument turns the shortcuts off naming schedule, and stdout and exit equal CP4's" "rc $rc, stderr '$err', stdout '${out:0:300}'"
fi

# CP8 — the parent read's cache against git's own. The probe takes the expected text of each parent
# spec path from a `git show` it runs itself, so it shares no state with the cache it grades. It
# then installs the door's reads, lets the instrument's `ls-tree` call fill the cache, and makes the
# schedule instrument's own git raise: from there only the cache can answer a `show`.
IFS= read -r -d '' CP8_PROBE <<'PROBE' || :
import importlib.util, re, subprocess, sys, types
sys.stdout.reconfigure(encoding="utf-8")
door_path, parent = sys.argv[1:3]
spec = importlib.util.spec_from_file_location("door", door_path)
door = importlib.util.module_from_spec(spec)
spec.loader.exec_module(door)
found = door.resolve_instruments()
moved = door.scan_moved(found)
if moved:
    sys.exit("chain-packet.test: CP8 has no shortcut to grade, a role moved: " + "; ".join(moved))
folder = f"memory/builds/{parent}/spec/"
listed = subprocess.run(["git", "ls-tree", "-r", "--name-only", "HEAD", folder],
                        capture_output=True, text=True, encoding="utf-8", check=True).stdout
paths = [p for p in listed.split("\n") if p]
want, lone = {}, 0
for p in paths:
    want[p] = subprocess.run(["git", "show", f"HEAD:{p}"], capture_output=True, text=True,
                             encoding="utf-8", check=True).stdout
    raw = subprocess.run(["git", "cat-file", "blob", f"HEAD:{p}"], capture_output=True, check=True).stdout
    lone += bool(re.search(rb"\r(?!\n)", raw))
tree_lib = door.load_module("tree_lib", door.HERE / "memory-tree" / "tree_lib.py")
packet = door.load_module("packet", found["packet"][0])
door.set_reads(packet, tree_lib)
packet.schedule.git("ls-tree", "-r", "--name-only", "HEAD", folder)


def run(*a, **k):
    raise RuntimeError("the instrument's own git ran")


packet.schedule.subprocess = types.SimpleNamespace(run=run)
for p in paths:
    try:
        got = packet.schedule.git("show", f"HEAD:{p}")
    except RuntimeError:
        sys.exit(f"chain-packet.test: the cache did not answer {p}, the instrument's own git was asked")
    if got != want[p]:
        sys.exit(f"chain-packet.test: the cache's answer for {p} differs from git's own")
if not paths or not lone:
    sys.exit(f"chain-packet.test: {len(paths)} parent path(s) and {lone} holding a lone CR, so nothing was graded")
print(f"chain-packet.test: cache answered {len(paths)} of {len(paths)} parent path(s) · {lone} holding a lone CR")
PROBE
out=$(cd "$T" && printf '%s' "$CP8_PROBE" | "$PY" - "$DOOR" "$PARENT" 2>"$base/stderr"); rc=$?
err=$(<"$base/stderr"); out=${out//$'\r'/}; err=${err//$'\r'/}
if [ "$rc" = 0 ] && [[ $out =~ ^"chain-packet.test: cache answered "[1-9][0-9]*" of "[1-9][0-9]*" parent path(s) · "[1-9][0-9]*" holding a lone CR"$ ]]; then
  print_pass "CP8 the parent read's cache answers every kept parent path as git's own show does, one holding a lone CR, with the instrument's git made to raise"
else
  print_fail "CP8 the parent read's cache answers every kept parent path as git's own show does, one holding a lone CR, with the instrument's git made to raise" "rc $rc, stdout '${out:0:300}', stderr '${err:0:400}'"
fi

# CP9 — the packet is green under T's own HEAD, by CP4. Under GIT_DIR=$U, for these two runs only,
# HEAD holds a parent spec OPEN, so the instrument reads the parent as not done and its byte compare
# reds. The door must print the same, having left the parent read to the instrument's own git and
# said so. A door that answered from its batch would read T's CLOSED text, print green and exit 0.
GIT_DIR=$U run_in "$T" "$DOOR" --check "$SLUG"; d_out=$out d_rc=$rc d_err=$err
GIT_DIR=$U run_in "$T" "$INST" --check "$SLUG"
if [ "$d_rc" = 1 ] && [ "$rc" = 1 ] && [ "$d_out" = "$out" ] && [[ $out == *"byte compare red"* ]] \
   && [[ $d_err == "chain-packet: GIT_DIR set"* ]] && [[ $d_err != *$'\n'* ]]; then
  print_pass "CP9 under a foreign GIT_DIR the door's --check and the instrument's print the same red stdout and exit 1, and the door says the instrument's own git read the parents"
else
  print_fail "CP9 under a foreign GIT_DIR the door's --check and the instrument's print the same red stdout and exit 1, and the door says the instrument's own git read the parents" "door rc $d_rc, instrument rc $rc, door stderr '$d_err', door stdout '${d_out:0:300}', instrument stdout '${out:0:300}'"
fi

# CP7 — a kept spec committed with a non-UTF-8 byte and committed again restored: the instrument's
# child raises on that revision and the packet refuses, the door reads no history and renders, so
# parity must say DIFFERENT. This is the one known difference, and the arm that shows parity
# compares two renders rather than one with itself.
printf '\377\n' >> "$T/${keep[0]}"
git -C "$T" add -- "${keep[0]}" >/dev/null 2>&1; git -C "$T" commit -qm 'a revision that is not UTF-8' --no-verify
git -C "$T" checkout -q HEAD~1 -- "${keep[0]}"; git -C "$T" commit -qm restored --no-verify
run_in "$T" "$DOOR" --parity "$SLUG"
if [ "$rc" = 1 ] && [[ $out == "chain-packet: parity $SLUG · DIFFERENT · the instrument refused: "*" · the door packet "*" bytes" ]]; then
  print_pass "CP7 a spec revision that is not UTF-8 makes --parity print DIFFERENT and exit 1"
else
  print_fail "CP7 a spec revision that is not UTF-8 makes --parity print DIFFERENT and exit 1" "rc $rc, stdout '${out:0:400}', stderr '${err:0:300}'"
fi

total=$((pass+fail))
if [ "$total" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "chain-packet.test: $total assertion(s) executed, below the declared floor of $FLOOR_ASSERTIONS —"
  echo "  arms went missing rather than failing, which reports as success without this check."
  exit 1
fi
[ "$fail" = 0 ] && echo "PASS ($total assertions)"
[ "$fail" = 0 ] || { echo "chain-packet.test: $fail of $total assertion(s) failed"; exit 1; }
