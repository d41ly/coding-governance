#!/usr/bin/env bash
# fork-count.sh — forks per invocation of each declared hot entrypoint, against a shrink-only ceiling.
#
#   bash <this> <ceilings-file> [root] [--only <id>] [--sites]   # 0 every row within its ceiling, 1 a red, 2 a refusal
#   bash <this> --selftest                             # the calibration twice, and the declaration staged wrong
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
# THE DECLARATION is a TAB-separated file the caller owns, one row per (entrypoint, bash major.minor):
#   <id> TAB <bash> TAB <ceiling> TAB <base> TAB <setup> TAB <command> TAB <reason>
# `setup` runs untraced in a fresh scratch directory and builds the fixture; `command` is the one traced
# invocation. Both run with that directory as the working directory, `ROOT` naming the graded tree and
# `SCRATCH` the directory. A row whose setup fails prints the `skipped` shape and is never a pass. An
# entrypoint with no row for the running bash prints the `skipped` shape too: fork counts differ by bash
# version — `$(<f)` forks on 5.2 and not on 5.3 — so a ceiling is declared per version. `base` is the
# count the row was first measured at, kept beside the ceiling so the saving reads off one line.
# Two directions red: a count above its ceiling, and a ceiling more than max(3, 5 %) above its count,
# which is a saving nobody banked.
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

read_budgets() { # ceilings file -> FC_ROWS, one row per line; refuses a malformed row by name
  local n=0 row f
  FC_ROWS=()
  [ -f "$1" ] || { echo "fork-count: no ceilings file at $1, so there is nothing to grade — a refusal and not a pass" >&2; return 2; }
  while IFS= read -r row || [ -n "$row" ]; do
    n=$((n + 1)); row=${row%$'\r'}
    case "$row" in ''|'#'*) continue ;; esac
    IFS=$'\t' read -r -a f <<<"$row"
    if [ "${#f[@]}" -lt 7 ] || [[ ! ${f[1]} =~ ^[0-9]+\.[0-9]+$ ]] || [[ ! ${f[2]} =~ ^[0-9]+$ ]] || [[ ! ${f[3]} =~ ^[0-9]+$ ]]; then
      echo "fork-count: REFUSING — line $n is not <id> TAB <bash major.minor> TAB <ceiling> TAB <base> TAB <setup> TAB <command> TAB <reason>: $row" >&2
      return 2
    fi
    FC_ROWS+=("$row")
  done < "$1"
  [ "${#FC_ROWS[@]}" -gt 0 ] || { echo "fork-count: the ceilings file declares no row, so this run graded NOTHING — a refusal and not a pass" >&2; return 2; }
  return 0
}

check_budgets() { # scratch root · [only id] -> one verdict line per entrypoint, then the summary; rc 1 on a red
  local work="$1" only="${2:-}" row id want ceil base setup cmd margin dir rc ok=0 red=0 skip=0
  local -A ids=() have=()
  want="${BASH_VERSINFO[0]}.${BASH_VERSINFO[1]}"
  for row in "${FC_ROWS[@]}"; do
    IFS=$'\t' read -r id _ _ _ _ _ _ <<<"$row"; ids[$id]=1
  done
  for row in "${FC_ROWS[@]}"; do
    IFS=$'\t' read -r id ver ceil base setup cmd _ <<<"$row"
    [ -z "$only" ] || [ "$id" = "$only" ] || continue
    [ "$ver" = "$want" ] || continue
    have[$id]=1
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
  [ "$red" = 0 ]
}

run_selftest() { # -> the calibration twice, and a copy with the declaration moved by one refusing
  local work rc rc1 rc2 got1 got2 out
  work=$(mktemp -d) || return 2
  FC_ROOT_DIR=$work
  check_calibration "$work" >/dev/null 2>&1; rc1=$?; got1=$FC_COUNT
  check_calibration "$work" >/dev/null 2>&1; rc2=$?; got2=$FC_COUNT
  sed 's/^SPECIMEN_FORKS=.*/SPECIMEN_FORKS='"$((SPECIMEN_FORKS + 1))"'/' "${BASH_SOURCE[0]}" > "$work/moved.sh"
  out=$(bash "$work/moved.sh" "$work/none.txt" "$work" 2>&1); rc=$?
  rm -rf "$work"
  local st=0
  [ "$rc1" = 0 ] && [ "$rc2" = 0 ] && [ "$got1" = "$got2" ] \
    || { echo "SELFTEST FAIL: the calibration did not hold on two runs: rc $rc1/$rc2, counts $got1/$got2 against $SPECIMEN_FORKS"; st=1; }
  [ "$rc" = 2 ] && [[ $out == *"the counter cannot move"* ]] \
    || { echo "SELFTEST FAIL: a declaration moved by one did not refuse with 2 naming the counter (rc $rc): $out"; st=1; }
  [ "$st" = 0 ] && echo "PASS (2 assertions) — the specimen counted $got1 twice, and a declaration of $((SPECIMEN_FORKS + 1)) refused"
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
