#!/usr/bin/env bash
# fork-count.sh — forks per invocation of each declared hot entrypoint, against a shrink-only ceiling.
#
#   bash <this> <ceilings-file> [root] [--only <id>] [--sites]   # 0 every row within its ceiling, 1 a red, 2 a refusal
#   bash <this> --selftest                             # the calibration twice, the declaration staged wrong, and the three graded-nothing outcomes
#
# WHY A COUNT AND NOT A CLOCK. A fork costs 89 to 315 ms under MSYS and nothing in the source reads that
# way, so a saving or a regrowth is invisible until a suite runs an hour slower. A timing arm flakes on a
# loaded host; a trace count cannot. No clock is read anywhere in this file. (TOOL-aSparedSpawn-8)
#
# HOW IT COUNTS. Each entrypoint runs under `env SHELLOPTS=xtrace BASH_XTRACEFD=<fd>` with a PS4 that
# carries `${BASHPID}` and `${BASH_SOURCE##*/}:${LINENO}`. SHELLOPTS is readonly inside bash, so it is
# set through `env`, and exported it makes every child `bash` trace too. The forks are the distinct
# BASHPID values in the trace, less the root's. A red names the delta and the ten `file:line` sites the
# most forked subshells first traced at — never a bare total. A site that grew by one can tie below
# those ten, so `--sites` prints every site with its count, for a diff against the parent's run.
#
# CALIBRATED FIRST, EVERY RUN. A specimen with a declared fork count is written from a quoted heredoc
# below and counted before any entrypoint; a counter that reads it wrong refuses with 2, because a probe
# that cannot move reports a reassuring zero exactly as a clean tree does.
#
# THE DECLARATION is a ledger population the caller owns, one row per (entrypoint, bash major.minor):
#   <id> TAB <bash> TAB <base> TAB <setup> TAB <command> TAB <ceiling> TAB <sha> TAB <disposition>
# `setup` runs untraced in a fresh scratch directory and builds the fixture; `command` is the one traced
# invocation. Both run with that directory as the working directory, `ROOT` naming the graded tree and
# `SCRATCH` the directory. A row whose setup fails prints the `skipped` shape and is never a pass. An
# entrypoint with no row for the running bash prints the `skipped` shape too: fork counts differ by bash
# version — `$(<f)` forks on 5.2 and not on 5.3 — so a ceiling is declared per version. `base` is the
# count the row was first measured at, kept beside the ceiling so the saving reads off one line.
# Two directions red: a count above its ceiling, and a ceiling more than max(3, 5 %) above its count,
# which is a saving nobody banked.
#
# A RUN THAT GRADES NOTHING has three outcomes, and none of them reads as a measured pass:
#   - an `--only <id>` naming no declared row refuses with 2 and lists the declared ids — a typo;
#   - a selection with a row declared for the running bash, every such row skipped because its setup
#     failed or it wrote no trace, refuses with 2 naming that bash — it could have graded and did not;
#   - a selection with NO row for the running bash keeps the `skipped` shape and exits 0, by owner
#     ruling F1(a), and prints `fork-count: NOT MEASURED — no row declares bash <major.minor>, ...`,
#     so the leg's log shows the gap. Declaring that bash's rows turns the line into a graded run.
# (TOOL-aSparedSpawn-19)
#
# WHAT THIS DOES NOT CHECK. The count is a deterministic LOWER bound: a subshell that traces no command
# of its own is unseen, and so is every process a non-bash child starts — a python or node child is
# invisible beyond the subshell, if any, that started it. Nor does it see a child that unsets the
# trace variables, a script that writes to the trace's own descriptor, or the cost of fork-free work.
set -u
# A FIXTURE MUST NOT REACH THE GRADED REPOSITORY. Git exports GIT_DIR into a hook, and a fixture's own
# `git init` and `git commit` under an inherited one would act on the repository being graded; a bar's
# GATE_* knobs and a session's CLAUDE_* ids change what an entrypoint does, so a count would depend on
# who ran it. All three families leave this process before anything runs.
for FC_V in $(compgen -e); do
  case "$FC_V" in GIT_*|GATE_*|CLAUDE_*) unset "$FC_V" ;; esac
done
FC_FD=87
FC_PS4='+${BASHPID}|${BASH_SOURCE##*/}:${LINENO}|'
# The specimen's declared count: two command substitutions of a function, one explicit subshell, and a
# two-stage pipeline, each of which traces a command of its own.
SPECIMEN_FORKS=5

write_specimen() { # path -> the calibration specimen, from a quoted heredoc so a lint reads it as data
  cat > "$1" <<'SPECIMEN'
f() { printf '%s' x; }
a=$(f)
b=$(f)
( : )
printf 'x\n' | while IFS= read -r l; do :; done
:
SPECIMEN
}

measure_forks() { # trace file -> FC_COUNT, FC_ROOTPID and FC_SITES (`<count> <file:line>` lines), no fork
  local line pid site root=""
  local -A first=()
  FC_COUNT=0; FC_SITES=""
  [ -s "$1" ] || return 1
  while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in +*'|'*'|'*) ;; *) continue ;; esac
    line=${line#"${line%%[!+]*}"}; pid=${line%%|*}; site=${line#*|}; site=${site%%|*}
    case "$pid" in ''|*[!0-9]*) continue ;; esac
    [ -n "$root" ] || root=$pid
    [ -n "${first[$pid]+x}" ] || first[$pid]=$site
  done < "$1"
  FC_ROOTPID=$root
  local -A per=()
  for pid in "${!first[@]}"; do
    [ "$pid" = "$root" ] && continue
    FC_COUNT=$((FC_COUNT + 1)); per[${first[$pid]}]=$(( ${per[${first[$pid]}]:-0} + 1 ))
  done
  for site in "${!per[@]}"; do FC_SITES+="${per[$site]} $site"$'\n'; done
  return 0
}

run_traced() { # dir · command -> the trace file's path in FC_TRACE; the command's own output is dropped
  FC_TRACE="$1/.fork-trace"
  ( cd "$1" && env SHELLOPTS=xtrace BASH_XTRACEFD="$FC_FD" PS4="$FC_PS4" ROOT="$FC_ROOT_DIR" SCRATCH="$1" \
      bash -c "$2" >/dev/null 2>&1 87>"$FC_TRACE" )
  return 0
}

print_contributors() { # [all] -> the ten sites the most forked subshells first traced at, or every one
  if [ -n "${1:-}" ]; then printf '%s' "$FC_SITES" | sort -k1,1nr -k2,2V | sed 's/^/    /'
  else printf '%s' "$FC_SITES" | sort -k1,1nr -k2,2V | head -10 | sed 's/^/    /'; fi
}

check_calibration() { # scratch dir -> 0 when the specimen counts as declared, else 2 with the refusal
  write_specimen "$1/specimen.sh"
  run_traced "$1" "bash ./specimen.sh"
  measure_forks "$FC_TRACE" || FC_COUNT=""
  if [ "$FC_COUNT" != "$SPECIMEN_FORKS" ]; then
    echo "fork-count: REFUSING — the calibration specimen declares $SPECIMEN_FORKS fork(s) and the trace counted ${FC_COUNT:-nothing}, so the counter cannot move and every count below would be a number about nothing" >&2
    return 2
  fi
  echo "fork-count: calibrated — the specimen's $SPECIMEN_FORKS fork(s) counted exactly"
  return 0
}

# The python launcher, INLINED byte-identically from the canonical copy named on its marker line
# (this kit is copy-installed and has no shared lib to source): the registry is read through the
# ledger factory, which is Python (TOOL-dWitnessedBar-16 S4).
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
  # THE BAR'S OWN RESOLUTION, taken with no spawn (TOOL-aMeasuredDrag-11). The run-gates runner
  # exports GATE_RESOLVED_PY as four lines: the version, the launcher it resolved, and GOV_PYTHON and
  # PATH as it saw them. With no caller override the loop below is decided by GOV_PYTHON, PATH and the
  # floor, so a memo matching both byte for byte, at or above THIS floor, is what the loop would print.
  # Anything else, malformed or partial included, is ignored and the loop runs. Only an absolute
  # launcher is admitted (TOOL-aMeasuredDrag-12): a relative one names another file once a leg
  # changes directory, and a bare name does too under a PATH holding `.`.
  _rp_re=$'^([0-9]+)\\.([0-9]+)\n(/[^\n]*|[A-Za-z]:/[^\n]*|[A-Za-z]:\\\\[^\n]*)\n([^\n]*)\n(.*)$'
  if [ -z "${1:-}" ] && [[ ${GATE_RESOLVED_PY:-} =~ $_rp_re ]] \
    && [ "${BASH_REMATCH[4]}" = "${GOV_PYTHON:-}" ] && [ "${BASH_REMATCH[5]}" = "$PATH" ] \
    && [ $(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} )) -ge "$_rp_fv" ]; then
    printf '%s\n' "${BASH_REMATCH[3]}"
    return 0
  fi
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
# The wrong-shell refusal, INLINED byte-identically beside the launcher it guards.
# >>> refuse_wrong_shell — canonical copy: refuse-wrong-shell.sh in gov's lib dir (byte-identical; gated)
wrong_shell_at() {   # <abs path> <wsl 0|1>; returns 0 when the path is a Windows checkout under WSL
  [ "$2" = 1 ] || return 1
  case "$1" in /mnt/[a-z]/*) return 0 ;; esac
  return 1
}
refuse_wrong_shell() {
  _rws_wsl=0
  { [ -n "${WSL_DISTRO_NAME:-}" ] || [ -e /proc/sys/fs/binfmt_misc/WSLInterop ]; } && _rws_wsl=1
  _rws_p=${BASH_SOURCE[0]:-$0}
  case "$_rws_p" in /*) ;; *) _rws_p=$PWD/$_rws_p ;; esac
  wrong_shell_at "$_rws_p" "$_rws_wsl" || return 0
  echo "refuse_wrong_shell: WSL's bash is running $_rws_p from a Windows checkout under /mnt/;" >&2
  echo "refuse_wrong_shell: run it with Git's bash (C:/Program Files/Git/bin/bash.exe)." >&2
  return 1
}
# <<< refuse_wrong_shell
refuse_wrong_shell || exit 2
FC_HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd) || FC_HERE=.

# THE DECLARATION IS A LEDGER POPULATION (TOOL-dWitnessedBar-16 S4), `fork-ceilings`, a `ceiling` keyed by
# <id>, <bash>, <base>, <setup> and <command>, its count the ceiling, read through the ledger factory this
# kit carries: `<id> TAB <bash> TAB <base> TAB <setup> TAB <command> TAB <ceiling> TAB <sha> TAB
# <disposition>`. A row's reason is the conversion record's or its widen record's, never the row's.
# FC_ROWS holds each row in the order `check_budgets` reads, `<id> <bash> <ceiling> <base> <setup> <command>`.
read_budgets() { # ceilings file -> FC_ROWS, one row per declared entrypoint; refuses a malformed row by name
  local out rc row
  FC_ROWS=()
  [ -f "$1" ] || { echo "fork-count: no ceilings file at $1, so there is nothing to grade — a refusal and not a pass" >&2; return 2; }
  FC_PY=$(resolve_python) || { echo "fork-count: no usable python, and the ceilings file is read through the ledger factory" >&2; return 2; }
  out=$("$FC_PY" -I -c '
import re, sys
sys.path.insert(0, sys.argv[1])
import legacy_ledger as LL
shape = "<id> TAB <bash major.minor> TAB <base> TAB <setup> TAB <command> TAB <ceiling> TAB <sha> TAB <disposition>"
rows, bad = LL.read_rows(sys.argv[2], 5, verbatim=(2,))
for number, kind, row in bad:
    print("fork-count: REFUSING — line %d is not %s (%s): %s" % (number, shape, LL.MALFORMED_TEXT.get(kind, kind), row))
    sys.exit(2)
for (ident, ver, base, setup, cmd), (ceil, _tail, number, row) in sorted(rows.items(), key=lambda kv: kv[1][2]):
    if not re.fullmatch(r"[0-9]+\.[0-9]+", ver) or not re.fullmatch(r"[0-9]+", base):
        print("fork-count: REFUSING — line %d is not %s: %s" % (number, shape, row))
        sys.exit(2)
    print("\t".join([ident, ver, str(ceil), base, setup, cmd]))' "$FC_HERE" "$1" | tr -d '\r'; exit "${PIPESTATUS[0]}")
  rc=$?
  if [ "$rc" != 0 ]; then
    printf '%s\n' "${out:-fork-count: REFUSING — the ledger factory beside this leg did not read $1}" >&2
    return 2
  fi
  # A scratch FILE feeds the loop, never a here-string over the substitution's value: that is the
  # stall `sh_hygiene.py` gates (TOOL-dWitnessedBar-16 S15). The caller's scratch root holds it.
  printf '%s\n' "$out" > "$FC_WORK/budget-rows" || { echo "fork-count: the scratch root $FC_WORK took no write" >&2; return 2; }
  while IFS= read -r row; do
    [ -n "$row" ] && FC_ROWS+=("$row")
  done < "$FC_WORK/budget-rows"
  [ "${#FC_ROWS[@]}" -gt 0 ] || { echo "fork-count: the ceilings file declares no row, so this run graded NOTHING — a refusal and not a pass" >&2; return 2; }
  return 0
}

check_budgets() { # scratch root · [only id] -> one verdict line per entrypoint, then the summary; rc 1 on a red, 2 on a run that graded nothing it could have
  local work="$1" only="${2:-}" row id want ceil base setup cmd margin dir rc ok=0 red=0 skip=0 declared=0
  local -A ids=() have=()
  want="${BASH_VERSINFO[0]}.${BASH_VERSINFO[1]}"
  for row in "${FC_ROWS[@]}"; do
    IFS=$'\t' read -r id _ _ _ _ _ _ <<<"$row"; ids[$id]=1
  done
  if [ -n "$only" ] && [ -z "${ids[$only]+x}" ]; then
    echo "fork-count: REFUSING — --only $only names no declared row, so this run would grade NOTHING; the declared ids are: ${!ids[*]}" >&2
    return 2
  fi
  for row in "${FC_ROWS[@]}"; do
    IFS=$'\t' read -r id ver ceil base setup cmd _ <<<"$row"
    [ -z "$only" ] || [ "$id" = "$only" ] || continue
    [ "$ver" = "$want" ] || continue
    have[$id]=1; declared=$((declared + 1))
    dir="$work/$id"; mkdir -p "$dir"
    ( cd "$dir" && ROOT="$FC_ROOT_DIR" SCRATCH="$dir" bash -c "$setup" ) >"$dir/.setup.log" 2>&1; rc=$?
    if [ "$rc" != 0 ]; then
      echo "skipped — $id · its fixture setup exited $rc, so no count was taken: $(tail -1 "$dir/.setup.log")"
      skip=$((skip + 1)); continue
    fi
    run_traced "$dir" "$cmd"
    if ! measure_forks "$FC_TRACE"; then
      echo "skipped — $id · the traced command wrote no trace line, so it never ran under the counter"
      skip=$((skip + 1)); continue
    fi
    margin=$(( FC_COUNT * 5 / 100 )); [ "$margin" -ge 3 ] || margin=3
    if [ "$FC_COUNT" -gt "$ceil" ]; then
      echo "fork-count: RED $id · measured $FC_COUNT · ceiling $ceil · delta +$((FC_COUNT - ceil)) · base $base — the sites the most forked subshells first traced at:"
      print_contributors; red=$((red + 1))
      echo "fork-count:   a site that grew by one can tie below these ten: run --only $id --sites here and at the parent, and diff the two"
    elif [ "$ceil" -gt $((FC_COUNT + margin)) ]; then
      echo "fork-count: RED $id · STALE ceiling $ceil is more than $margin above the measured $FC_COUNT — lower the row to $FC_COUNT, a saving nobody banked is a regrowth nobody sees"
      red=$((red + 1))
    else
      echo "fork-count: ok $id · measured $FC_COUNT · ceiling $ceil · base $base"
      ok=$((ok + 1))
    fi
    [ -z "$FC_ALL" ] || { echo "fork-count: sites $id — every site a forked subshell first traced at, with its count:"; print_contributors all; }
  done
  for id in "${!ids[@]}"; do
    [ -z "$only" ] || [ "$id" = "$only" ] || continue
    [ -n "${have[$id]+x}" ] || { echo "skipped — $id · no ceiling is declared for bash $want"; skip=$((skip + 1)); }
  done
  echo "fork-count: $ok passed · $red red · $skip skipped — a skipped row is not a pass"
  if [ $((ok + red)) = 0 ]; then
    if [ "$declared" -gt 0 ]; then
      echo "fork-count: REFUSING — $declared row(s) in this selection are declared for bash $want and every one was skipped, so this run graded NOTHING it could have — a refusal and not a pass; fix the setup the skipped line names" >&2
      return 2
    fi
    echo "fork-count: NOT MEASURED — no row declares bash $want, so the spawn budget was not measured on this bash"
  fi
  [ "$red" = 0 ]
}

run_selftest() { # -> the calibration twice, a copy with the declaration moved by one refusing, and the three graded-nothing outcomes
  local work rc rc1 rc2 rc3 rc4 rc5 got1 got2 out out3 out4 out5 want other
  work=$(mktemp -d) || return 2
  FC_ROOT_DIR=$work
  check_calibration "$work" >/dev/null 2>&1; rc1=$?; got1=$FC_COUNT
  check_calibration "$work" >/dev/null 2>&1; rc2=$?; got2=$FC_COUNT
  sed 's/^SPECIMEN_FORKS=.*/SPECIMEN_FORKS='"$((SPECIMEN_FORKS + 1))"'/' "${BASH_SOURCE[0]}" > "$work/moved.sh"
  out=$(bash "$work/moved.sh" "$work/none.txt" "$work" 2>&1); rc=$?
  # The graded-nothing outcomes run THIS script over scratch ceilings files: one row for a bash that
  # cannot be the running one, and one row for the running bash whose setup fails. (TOOL-aSparedSpawn-19)
  want="${BASH_VERSINFO[0]}.${BASH_VERSINFO[1]}"; other="$((BASH_VERSINFO[0] + 1)).0"
  printf 'alpha\t%s\t1\ttrue\ttrue\t1\tabcdef12\tseeded\n' "$other" > "$work/other.txt"
  printf 'beta\t%s\t1\texit 1\ttrue\t1\tabcdef12\tseeded\n' "$want" > "$work/failed.txt"
  out3=$("$BASH" "${BASH_SOURCE[0]}" "$work/other.txt" "$work" --only no-such-id 2>&1); rc3=$?
  out4=$("$BASH" "${BASH_SOURCE[0]}" "$work/failed.txt" "$work" 2>&1); rc4=$?
  out5=$("$BASH" "${BASH_SOURCE[0]}" "$work/other.txt" "$work" 2>&1); rc5=$?
  rm -rf "$work"
  local st=0
  [ "$rc1" = 0 ] && [ "$rc2" = 0 ] && [ "$got1" = "$got2" ] \
    || { echo "SELFTEST FAIL: the calibration did not hold on two runs: rc $rc1/$rc2, counts $got1/$got2 against $SPECIMEN_FORKS"; st=1; }
  [ "$rc" = 2 ] && [[ $out == *"the counter cannot move"* ]] \
    || { echo "SELFTEST FAIL: a declaration moved by one did not refuse with 2 naming the counter (rc $rc): $out"; st=1; }
  [ "$rc3" = 2 ] && [[ $out3 == *"fork-count: REFUSING — --only no-such-id names no declared row, so this run would grade NOTHING; the declared ids are: alpha"* ]] \
    || { echo "SELFTEST FAIL: an --only id naming no row did not refuse with 2 listing the declared ids (rc $rc3): $out3"; st=1; }
  [ "$rc4" = 2 ] && [[ $out4 == *"fork-count: REFUSING — 1 row(s) in this selection are declared for bash $want and every one was skipped"* ]] \
    || { echo "SELFTEST FAIL: a declared row whose setup fails did not refuse with 2 naming bash $want (rc $rc4): $out4"; st=1; }
  [ "$rc5" = 0 ] && [[ $out5 == *"fork-count: NOT MEASURED — no row declares bash $want, so the spawn budget was not measured on this bash"* ]] \
    && [[ $out5 == *"skipped — alpha · no ceiling is declared for bash $want"* ]] \
    || { echo "SELFTEST FAIL: a file declaring only bash $other did not exit 0 with the skipped shape and the NOT MEASURED line (rc $rc5): $out5"; st=1; }
  [ "$st" = 0 ] && echo "PASS (5 assertions) — the specimen counted $got1 twice, a declaration of $((SPECIMEN_FORKS + 1)) refused, an --only typo and a declared row graded nothing refused, and an undeclared bash $want passed as NOT MEASURED"
  return "$st"
}

case "${1:-}" in
  --selftest) run_selftest; exit $? ;;
  ''|-*) echo "fork-count: usage: bash fork-count.sh <ceilings-file> [root] [--only <id>] [--sites] | --selftest" >&2; exit 2 ;;
esac
FC_FILE=$1; FC_ROOT_DIR=${2:-.}; FC_ONLY=""; FC_ALL=""
shift; [ "$#" -gt 0 ] && shift
while [ "$#" -gt 0 ]; do
  case "$1" in
    --only) FC_ONLY=${2:-}; shift 2 || shift ;;
    --sites) FC_ALL=1; shift ;;
    *) echo "fork-count: unknown argument: $1" >&2; exit 2 ;;
  esac
done
FC_ROOT_DIR=$(cd "$FC_ROOT_DIR" 2>/dev/null && pwd) || { echo "fork-count: not a directory: ${2:-.}" >&2; exit 2; }
FC_WORK=$(mktemp -d) || { echo "fork-count: no scratch directory could be made, so nothing was counted" >&2; exit 2; }
trap 'rm -rf "$FC_WORK"' EXIT
check_calibration "$FC_WORK" || exit 2
read_budgets "$FC_FILE" || exit 2
check_budgets "$FC_WORK" "$FC_ONLY"
