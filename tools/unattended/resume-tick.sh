#!/usr/bin/env bash
# resume-tick.sh — the OS-scheduled, OUT-OF-PROCESS resumer for a stalled unattended run.
# TOOL-aWokenSentinel-5. Registered by the owner as a scheduled task (the README has the line per
# OS), never by this kit: unregistered it does nothing, and the adopter's --check reports that as
# INFO, because an adopter who has not registered it has a working kit, not a broken one.
#
#   resume-tick.sh [--repo <root>] [--dry-run]
#
# WHY IT EXISTS. Every recorded resume of a stalled run was a human starting a session. The two
# hooks beside this file (stop-guard, stall-recorder) act INSIDE the session, so a session that is
# idle-on-error, hung, locked out or dead gets nothing from them. This script does not share the
# session's process: every ten minutes it walks every worktree of the repo, asks the driver beside
# it `--liveness` about every run whose lease names a session, and on `STALE` kills the recorded
# pid's tree, appends an attempt line and launches `claude -p --resume <session>` DETACHED with a
# payload that forbids re-parking. Everything it decides from is `--liveness`'s output: it never
# re-derives `stale`, `pid-alive` or the terminal predicate, because a second spelling of any of
# them is the two-answers class the driver's `--liveness` exists to remove.
#
# THE DECISION, per bound run — one line each, `resume-tick: <slug> · <worktree> · <act>`:
#   RUN.md not in the index               -> skip · RUN.md is not tracked (nothing probed, nothing launched)
#   host: names another node              -> skip · leased on <host>, not this node <me>
#   verdict not STALE, and not            -> skip · verdict <V>
#     FINISHED-UNSTAMPED with stale: yes
#   STALE, RESUME_ATTEMPTS or more since  -> skip · ATTEMPTS EXHAUSTED · last <utc> · out <path>
#     the run's last move
#   STALE, newest attempt's launched pid  -> skip · IN-FLIGHT · launched <pid> alive since <utc>
#     alive AND the line newer than the run's last move
#   STALE, under the cap, not logged in   -> SKIP — the CLI is not logged in ... (kills nothing, writes nothing)
#   STALE, under the cap, pid-alive yes   -> kill the tree — the recorded pid's, and a launched pid still
#     alive after the run moved (a resumed session that hung) — then the row below
#   STALE, under the cap, logged in       -> append the attempt line, launch detached, resumed · attempt <n> · out <path>
# The login row PRECEDES the kill row and the order is the point: a kill is useful only where a
# launch will follow, so the probe that decides whether one can happen runs first, and
# a logged-out node kills nothing (TOOL-aWokenSentinel-12 owns that ordering's proof). `--dry-run`
# prints the line it would act on with ` (dry-run)` appended and does nothing else — no kill, no
# attempt line, no launch, no login probe.
#
# THE MANDATE IS THE INDEX, NOT THE FILESYSTEM (the closing review's id 1). This script hands a
# session id to `claude -p --dangerously-skip-permissions`, and the record it reads that id from
# must be one the owner's act put in the index — `stage_or_fail` writes it there at --preflight and
# at --resume --keepalive-id — never a file an `acceptEdits` session, a sub-agent or an injected edit
# dropped under a worktree. So the lease is read from the INDEX BLOB (`git grep --cached`), an
# untracked RUN.md is announced and skipped, and the working copy's bytes decide nothing. What this
# does NOT close: an actor who can stage is the shell-access case protocol section 9 concedes.
#
# THE ATTEMPT CAP IS CONSECUTIVE, NOT LIFETIME. Only the sidecar lines newer than the run's last move
# count against RESUME_ATTEMPTS, so a resume that produced a commit, a write or a transcript entry
# resets the count; the `attempt <n>` ordinal in the line is the lifetime one, so an owner reading
# the sidecar sees both. ponytail: a transcript-only move resets the count too, which RESUME_TURNS
# and the stop-guard's block cap bound; count commits alone if that proves too generous.
#
# THE IN-FLIGHT GUARD IS THE LAUNCHED PID (the closing review's id 3). The pid the tick launched is
# written onto the attempt line as `launched <pid>` and read back by the next tick: alive with the
# tree unmoved since the launch, the resumer has not produced its first turn yet — throttled, or
# still starting — and a second launch would put two skip-permissions agents on one tree, so the
# tick skips; alive with the tree moved since, the resumed session ran and then hung, which is the
# case the tree kill exists for, so its tree is killed beside the recorded pid's and the run is
# relaunched. A resumed session that ran `--resume --keepalive-id` is the recorded pid and takes the
# ordinary row. ponytail: the launched pid is `bash.exe` running the launcher, and the resumed CLI is
# its child, so the tree kill reaches it; if a launcher ever exits while its child lives, record
# the child instead.
#
# THE TWO KNOBS are ROOT-SCOPED: this file sources the root's `.unattended.conf` into its own shell
# and reads RESUME_ATTEMPTS and RESUME_TURNS through the library's `read_bound_key`, exactly as the
# driver reads its four — one repo, one pair of bounds, and a NOTE that names the file
# (TOOL-aWokenSentinel-13). RESUME_STALE_BOUND is `--liveness`'s number and is not read here.
#
# WHAT THIS FILE DOES NOT DO, said where it is read: it defines no `fail()` helper and has no
# numbered checks, so it joins no population the harness meta-gate discovers — its refusal lines are
# its own suite's to assert. It notifies nobody: `ATTEMPTS EXHAUSTED` is the line a notification
# would key on. It never re-derives liveness: `pid-alive` for the RECORDED pid is `--liveness`'s,
# and the one probe it runs itself, on the pid it launched, is the library's `check_pid_alive`, the
# same function `--liveness` calls. And it spells no path outside its own directory: the kit dir is
# derived from `$0`, the repo root from `--repo` or git, and the sidecar root from the library's one
# derivation.
set -u

# THE KIT'S OWN DIRECTORY, DERIVED, and the two siblings it needs from there — the same three lines
# the driver and its suites use to find each other. An empty derivation refuses naming what it
# looked for; a path composed from an empty root would name a file at the filesystem root.
KIT_DIR="$(cd "$(dirname "$0")" && pwd)"
[ -n "$KIT_DIR" ] || { echo "resume-tick: REFUSED — could not derive the kit directory from \$0 ($0), so neither the driver nor the library beside it can be found" >&2; exit 2; }
DRIVER="$KIT_DIR/unattended.sh"
[ -f "$KIT_DIR/lib-unattended.sh" ] || { echo "resume-tick: REFUSED — the kit library is missing beside this script: $KIT_DIR/lib-unattended.sh" >&2; exit 2; }
[ -f "$DRIVER" ] || { echo "resume-tick: REFUSED — the driver is missing beside this script, and --liveness is the only predicate this tick acts on: $DRIVER" >&2; exit 2; }
# shellcheck source=lib-unattended.sh
. "$KIT_DIR/lib-unattended.sh"

# KIT DEFAULTS, named so no call below types a digit. Six consecutive fruitless launches, and forty
# turns per resumed session — a run that needs more is resumed again by the next tick.
RESUME_ATTEMPTS_DEFAULT=6
RESUME_TURNS_DEFAULT=40

ROOT=""; DRY_RUN=0
while [ $# -gt 0 ]; do
  case "$1" in
    --repo) [ $# -ge 2 ] || { echo "resume-tick: REFUSED — --repo takes a path" >&2; exit 2; }; ROOT="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    *) echo "resume-tick: REFUSED — unknown argument '$1'; this script takes [--repo <root>] [--dry-run]" >&2; exit 2 ;;
  esac
done
# THE ROOT: `--repo` when given, else the checkout this runs inside. A root that is not a git
# repository is a refusal, never an empty walk that exits 0 — a scheduler starts a task in a cwd
# nobody chose, and an empty worktree list from the wrong place reads exactly like a repo with no
# bound run. Re-spelled through `pwd` so it shares one spelling with KIT_DIR (MSYS prints the two
# differently), which is what lets the CONTINUE payload derive the kit's repo-relative path.
[ -n "$ROOT" ] || ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || ROOT="$PWD"
_top=$(git -C "$ROOT" rev-parse --show-toplevel 2>/dev/null) || _top=""
[ -n "$_top" ] || { echo "resume-tick: REFUSED — $ROOT is not a git repository, so there is no worktree list to walk" >&2; exit 2; }
ROOT=$(cd "$_top" && pwd)

# THE ROOT CONF, sourced into THIS shell before the two bound reads, so `read_bound_key` reads a
# declaration rather than the scheduler's environment and its NOTE names the file. The two clearing
# assignments are the driver's idiom: `${!name}` reads the calling shell INCLUDING its environment,
# so without them an exported RESUME_ATTEMPTS would stand in for a declaration the conf never made.
CONF="$ROOT/.unattended.conf"
[ -f "$CONF" ] || { echo "resume-tick: REFUSED — $ROOT carries no .unattended.conf, so the tick has no bounds to read" >&2; exit 2; }
RESUME_ATTEMPTS=""; RESUME_TURNS=""
# shellcheck disable=SC1090
. "$CONF"
read_bound_key RESUME_ATTEMPTS "$RESUME_ATTEMPTS_DEFAULT" attempts "a stalled run is resumed at most the kit default of ${RESUME_ATTEMPTS_DEFAULT} consecutive fruitless time(s) before the tick says ATTEMPTS EXHAUSTED"
read_bound_key RESUME_TURNS "$RESUME_TURNS_DEFAULT" turns "a resumed session gets the kit default of ${RESUME_TURNS_DEFAULT} turns, and a run that needs more is resumed again by the next tick"

print_decision() { # slug · worktree · act
  if [ "$DRY_RUN" = 1 ]; then echo "resume-tick: $1 · $2 · $3 (dry-run)"; else echo "resume-tick: $1 · $2 · $3"; fi
}

# THE LOGIN PROBE, consulted before any kill. `claude auth status` printed, on node `a` 2026-09-16
# with the CLI logged in, a JSON object whose second line is `"loggedIn": true`, exit 0. The grep
# is over the measured shape and anything else — `false`, an error, an empty answer, a timeout —
# is not logged in, because the logged-out exit code was not measured and a grep is right in both.
# Bounded by `timeout 60` where `timeout` works (the driver's measured liveness probe, which
# `timeout 1 true` fails under load); a bound may never turn the check into a skip. THE ANSWER GOES
# TO A FILE, never through `$( )`: a substitution reads until the LAST write end closes, so a
# child the CLI leaves behind would hold the tick past the bound with the verdict already in —
# `memory/gotchas/bounded-through-a-pipe-is-unbounded`, and the suite measures the wall.
check_login() { # scratch-file -> 0 when the CLI answers logged in
  if timeout -k 1s 10 true >/dev/null 2>&1; then timeout -k 5s 60 claude auth status </dev/null >"$1" 2>&1
  else claude auth status </dev/null >"$1" 2>&1; fi
  grep -qE '"loggedIn":[[:space:]]*true' "$1" 2>/dev/null; local rc=$?
  rm -f -- "$1"
  return "$rc"
}

# THE TREE KILL. Under MSYS the recorded pid is `claude.exe`'s Windows pid, a native parent, so
# `taskkill /T` walks the tree from a Windows edge; the `//` doubling is the MSYS path-mangling
# guard. Measured on node `a` 2026-09-16: a bash-started child killed this way is gone from both
# `tasklist` and `ps`. Elsewhere the process group then the pid, UNVERIFIED — no registered node is
# POSIX. ponytail: one taskkill; route through a per-row reaper if a resumed turn ever re-stalls on
# an MSYS-forked survivor whose parent edge is not a Windows one.
run_kill_tree() { # pid
  local pg
  case "$(uname -s 2>/dev/null)" in
    MINGW*|MSYS*|CYGWIN*) taskkill //PID "$1" //T //F >/dev/null 2>&1 </dev/null ;;
    *) pg=$(ps -o pgid= -p "$1" 2>/dev/null | tr -d ' '); [ -n "$pg" ] && kill -- -"$pg" 2>/dev/null; kill "$1" 2>/dev/null ;;
  esac
  return 0
}

# THE DETACH: the tick returns while the resumed session runs. Under MSYS a PowerShell
# `Start-Process -WindowStyle Hidden` gives the child a console of its own — measured on node `a`
# 2026-09-16 to return in 0 s with the child alive two seconds later and its output file written —
# where a `nohup … &` inside the scheduler's console rests on a property nobody measured. The
# launcher path rides in double quotes inside the single-quoted argument list, so a repo path with
# a space still arrives as one argument. THE LAUNCHED PID GOES TO A FILE (`-PassThru`'s `.Id`; `$!`
# elsewhere), never through `$( )` — the same rule as the login probe — and `RD_PID` carries it,
# empty when the launch reported none.
RD_PID=""
run_detached() { # launcher · pid-file
  local b l
  RD_PID=""
  case "$(uname -s 2>/dev/null)" in
    MINGW*|MSYS*|CYGWIN*)
      b=$(cygpath -m "$(command -v bash)"); l=$(cygpath -m "$1")
      powershell.exe -NoProfile -NonInteractive -Command "(Start-Process -WindowStyle Hidden -FilePath '$b' -ArgumentList '\"$l\"' -PassThru).Id" </dev/null >"$2" 2>&1 ;;
    *) setsid nohup bash "$1" </dev/null >/dev/null 2>&1 & printf '%s\n' "$!" > "$2" ;;
  esac
  RD_PID=$(tr -dc '0-9' < "$2" 2>/dev/null)
  rm -f -- "$2"
  return 0
}

# ATTEMPTS SINCE THE LAST MOVE: the sidecar lines whose UTC stamp is newer than `now - last-move`.
# ISO-8601 stamps compare as strings, so awk's `>` is the whole comparison. Sets RT_TOTAL (every
# line, the lifetime count), RT_SINCE (the lines that count against the cap), RT_LAST (the last
# line, or empty), RT_LAUNCHED (the last line's `launched <pid>`, or empty for a line that carries
# none) — globals, because a `$( )` capture would lose all but one.
RT_TOTAL=0; RT_SINCE=0; RT_LAST=""; RT_LAUNCHED=""
derive_attempts() { # log · last-move-seconds
  local cutoff
  RT_TOTAL=0; RT_SINCE=0; RT_LAST=""; RT_LAUNCHED=""
  [ -s "$1" ] || return 0
  cutoff=$(date -u -d "@$(( $(date -u +%s) - $2 ))" +%Y-%m-%dT%H:%M:%SZ)
  RT_TOTAL=$(grep -c '' "$1")
  RT_SINCE=$(awk -v t="$cutoff" '$1 > t { c++ } END { print c + 0 }' "$1")
  RT_LAST=$(tail -n 1 -- "$1"); RT_LAST=${RT_LAST%$'\r'}
  case "$RT_LAST" in *" launched "*) RT_LAUNCHED=${RT_LAST##* launched }; RT_LAUNCHED=${RT_LAUNCHED%% *} ;; esac
  case "$RT_LAUNCHED" in *[!0-9]*) RT_LAUNCHED="" ;; esac
}

# THE FIVE VALUES, off the driver's `key: value` lines. RL_RC is the driver's exit; a non-zero one —
# the `fail 52` dead-probe refusal included — means no verdict is answerable and the run is skipped,
# because the alternative reads a dead probe as a verdict. RL_FIRST is the line for that skip: the
# driver's `UNATTENDED check` sentence when one printed, else the first line that is not a NOTE,
# else the first line — because the driver NOTEs every undeclared bound on stderr at source time,
# so for an adopter on a kit default the first merged line was `NOTE - this project declares no …`
# and the scheduler log kept that instead of the check (the closing review's id 16).
RL_RC=0; RL_FIRST=""; RL_VERDICT=""; RL_PID=""; RL_ALIVE=""; RL_MOVE=""; RL_STALE=""
read_liveness() { # worktree · slug
  local out
  out=$(cd "$1" && bash "$DRIVER" --liveness "$2" 2>&1 </dev/null); RL_RC=$?
  RL_FIRST=$(printf '%s\n' "$out" | grep -m 1 '^UNATTENDED check')
  [ -n "$RL_FIRST" ] || RL_FIRST=$(printf '%s\n' "$out" | grep -m 1 -v '^unattended: NOTE')
  [ -n "$RL_FIRST" ] || RL_FIRST=$(printf '%s\n' "$out" | head -n 1)
  RL_VERDICT=$(printf '%s\n' "$out" | sed -n 's/^verdict: //p' | head -n 1)
  RL_PID=$(printf '%s\n' "$out" | sed -n 's/^pid: //p' | head -n 1)
  RL_ALIVE=$(printf '%s\n' "$out" | sed -n 's/^pid-alive: //p' | head -n 1)
  RL_MOVE=$(printf '%s\n' "$out" | sed -n 's/^last-move: //p' | head -n 1)
  RL_STALE=$(printf '%s\n' "$out" | sed -n 's/^stale: //p' | head -n 1)
  [ "$RL_RC" = 0 ] && [ -n "$RL_VERDICT" ] || { [ "$RL_RC" = 0 ] && RL_RC=1; return 1; }
  return 0
}

# ONE BOUND RUN, the decision table above. The sidecar root is the library's one derivation, called
# with cwd in the worktree so it answers THAT tree's git dir, made absolute because the main
# worktree's answer is the relative `.git`.
run_tick() { # worktree · slug · session · host
  local wt="$1" slug="$2" sid="$3" host="$4" me sidecar log utc stamp launcher out n payload kitrel lastutc lastout
  # THE NODE FIRST: a record leased on another node is not this tick's to probe, kill or launch —
  # its pid is a number in another process table (closing review id 2). A lease with no host
  # recorded (`absent`, or written before the fact existed) is judged as it always was.
  me=$(read_host_name) || me=""
  case "$host" in ""|absent|"$me") ;; *) print_decision "$slug" "$wt" "skip · leased on $host, not this node ${me:-unknown}"; return 0 ;; esac
  if ! read_liveness "$wt" "$slug"; then
    echo "resume-tick: $slug · $wt · liveness probe failed: $RL_FIRST"; return 0
  fi
  # STALE acts; so does FINISHED-UNSTAMPED with `stale: yes` — a session that died between the
  # lander's push and `--landed` outranks STALE in the verdict order and nothing else stamps it,
  # the B1 wedge for a dead session (closing review id 5); the payload's "continue from the phase
  # the run-state file names" is `--landed` there.
  case "$RL_VERDICT:$RL_STALE" in STALE:*|FINISHED-UNSTAMPED:yes) ;; *) print_decision "$slug" "$wt" "skip · verdict $RL_VERDICT"; return 0 ;; esac
  sidecar=$(cd "$wt" && resolve_sidecar_dir) || { echo "resume-tick: $slug · $wt · liveness probe failed: the sidecar root cannot be derived in this worktree"; return 0; }
  case "$sidecar" in /*|[A-Za-z]:*) ;; *) sidecar="$wt/$sidecar" ;; esac
  log="$sidecar/resume.$slug.log"
  derive_attempts "$log" "$RL_MOVE"
  lastutc=${RT_LAST%% *}; lastout=${RT_LAST##* out }; lastout=${lastout%% launched *}
  if [ "$RT_SINCE" -ge "$RESUME_ATTEMPTS" ]; then
    print_decision "$slug" "$wt" "skip · ATTEMPTS EXHAUSTED · last $lastutc · out $lastout"; return 0
  fi
  # THE LAUNCHED PID, read back: alive and the tree unmoved since its line, the resumer is still
  # starting and a second launch would be a second agent on this tree; alive and the tree moved
  # since, it ran and hung, and joins the kill below.
  if [ -n "$RT_LAUNCHED" ] && [ "$RT_SINCE" -gt 0 ] && [ "$(check_pid_alive "$RT_LAUNCHED")" = yes ]; then
    print_decision "$slug" "$wt" "skip · IN-FLIGHT · launched $RT_LAUNCHED alive since $lastutc"; return 0
  fi
  n=$((RT_TOTAL + 1))
  utc=$(date -u +%Y-%m-%dT%H:%M:%SZ); stamp=$(date -u +%Y%m%dT%H%M%SZ)
  out="$sidecar/resume.$slug.$stamp.out"; launcher="$sidecar/resume.$slug.$stamp.sh"
  if [ "$DRY_RUN" = 1 ]; then print_decision "$slug" "$wt" "resumed · attempt $n · out $out"; return 0; fi
  # The sidecar dir first: the login answer lands in a file there (see check_login) and the attempt
  # line follows it. A dir that cannot be made is announced like a dead probe, and nothing is killed.
  mkdir -p "$sidecar" || { echo "resume-tick: $slug · $wt · liveness probe failed: the sidecar directory cannot be created: $sidecar"; return 0; }
  if ! check_login "$sidecar/resume.$slug.$stamp.auth"; then
    echo "resume-tick: $slug · $wt · SKIP — the CLI is not logged in on this node; nothing can resume $slug"; return 0
  fi
  [ "$RL_ALIVE" = yes ] && run_kill_tree "$RL_PID"
  [ -n "$RT_LAUNCHED" ] && [ "$(check_pid_alive "$RT_LAUNCHED")" = yes ] && run_kill_tree "$RT_LAUNCHED"
  # THE CONTINUE PAYLOAD, one string. The kit's repo-relative path is derived, never spelled; a kit
  # outside the root keeps its absolute path, which still runs.
  kitrel=${KIT_DIR#"$ROOT"/}
  payload="You are the resumed session of unattended run \`$slug\`. First run \`bash $kitrel/unattended.sh --resume $slug --keepalive-id <the idle-wake id you schedule now, per the unattended Skill>\` so this session's lease replaces the dead one. Then continue from the phase the run-state file names. The owner is absent: never park a question the protocol lets you decide — take the option that makes no measured observable worse and record why. If the run is terminal, reap the idle-wake and stop."
  # THE ATTEMPT LINE, appended BEFORE the launch, so a tick that dies mid-launch still counts; the
  # launched pid is written onto it AFTER, because it exists only then.
  printf '%s attempt %s session %s pid %s pid-alive %s out %s\n' "$utc" "$n" "$sid" "$RL_PID" "$RL_ALIVE" "$out" >> "$log"
  # THE LAUNCHER: three statements, and the record of what was launched, argv included. The PATH
  # export is what lets a suite's stub `claude` win — a login shell would re-read its profile and
  # put the real CLI back. `-p` warns after 3 s with no stdin, so stdin is /dev/null. `--max-turns`
  # is absent from `claude --help` on CLI 2.1.178 and ACCEPTED by it, measured 2026-09-16 on node
  # `a`; a withdrawn flag leaves `unknown option` in the .out, and the attempt still counts.
  {
    printf 'export PATH=%q\n' "$PATH"
    printf 'cd %q || exit 2\n' "$wt"
    printf 'claude -p --resume %q --dangerously-skip-permissions --max-turns %q %q </dev/null >%q 2>&1\n' "$sid" "$RESUME_TURNS" "$payload" "$out"
  } > "$launcher"
  run_detached "$launcher" "$sidecar/resume.$slug.$stamp.pid"
  [ -z "$RD_PID" ] || sed -i "\$ s/\$/ launched $RD_PID/" "$log"
  print_decision "$slug" "$wt" "resumed · attempt $n · out $out"
  return 0
}

# THE WALK: every worktree of the root, every run-state file IN THE INDEX whose `session:` fact is
# present and not `absent`. That read — one `git grep --cached` per tree, the lease's `session:`
# and `host:` off the index blob — is the only read this file makes of a record; everything else is
# `--liveness`'s. A RUN.md on disk and not in the index is announced and skipped: the index is what
# the owner's act wrote, the working copy is what anything with a file handle wrote. A tree without
# `.unattended.conf` is a checkout predating the kit: announced and skipped while the other trees
# are still walked. Zero candidates is an announced nothing.
scan_worktrees() {
  local wts wt mr hits stray line f slug sid host seen ntrees=0 ncand=0
  wts=$(git -C "$ROOT" worktree list --porcelain 2>/dev/null | sed -n 's/^worktree //p')
  # fd 9, not stdin: the driver, the login probe and the launcher all take stdin, and a loop fed
  # on fd 0 would hand them the remaining worktree lines.
  while IFS= read -r -u 9 wt; do
    [ -n "$wt" ] || continue
    ntrees=$((ntrees + 1))
    [ -f "$wt/.unattended.conf" ] || { echo "resume-tick: $wt · skipped: no .unattended.conf in this worktree, a checkout predating the kit"; continue; }
    mr=$( MEMORY_ROOT=memory; . "$wt/.unattended.conf" >/dev/null 2>&1; printf '%s' "$MEMORY_ROOT" )
    # TWO spawns per tree, not one per record: a spawn costs most of a second on this fleet, and a
    # tree with sixty build folders walked five times over was 21 s of nothing. The untracked
    # records first, each one line; then `<file>:session: <value>` and `<file>:host: <value>` off
    # the INDEX, and the split is on the first `:session:` / `:host:`, which a drive letter's colon
    # precedes but never contains. The first `session:` per file is the one `set_fact` rewrites.
    stray=$(git -C "$wt" ls-files --others -- "$mr/builds/*/RUN.md" 2>/dev/null)
    while IFS= read -r -u 8 f; do
      [ -n "$f" ] || continue
      slug=${f%/RUN.md}; slug=${slug##*/}
      ncand=$((ncand + 1))
      print_decision "$slug" "$wt" "skip · RUN.md is not tracked, and the tick launches only on a lease the index holds"
    done 8<<<"$stray"
    hits=$(git -C "$wt" grep --cached -H -E '^(session|host): ' -- "$mr/builds/*/RUN.md" 2>/dev/null)
    seen=""
    while IFS= read -r -u 8 line; do
      case "$line" in *:session:*) ;; *) continue ;; esac
      f=${line%%:session:*}; sid=${line#*:session:}; sid=${sid#"${sid%%[![:space:]]*}"}; sid=${sid%$'\r'}
      [ "$f" != "$seen" ] || continue; seen=$f
      case "$sid" in ""|absent) continue ;; esac
      host=""
      case $'\n'"$hits" in *$'\n'"$f:host:"*) host=${hits#*"$f:host:"}; host=${host%%$'\n'*}; host=${host#"${host%%[![:space:]]*}"}; host=${host%$'\r'} ;; esac
      slug=${f%/RUN.md}; slug=${slug##*/}
      ncand=$((ncand + 1))
      run_tick "$wt" "$slug" "$sid" "$host"
    done 8<<<"$hits"
  done 9<<<"$wts"
  [ "$ncand" -gt 0 ] || echo "resume-tick: no bound run in $ntrees worktree(s)"
  return 0
}

scan_worktrees
exit 0
