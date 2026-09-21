#!/usr/bin/env bash
# run-gates.runlog.test.sh — the gate runner's run-log line, observed from OUTSIDE the runner.
#
#   bash <this kit>/run-gates.runlog.test.sh                         # every arm, against the floor
#   RGRL_ARMS="AC3 CAP" bash <this kit>/run-gates.runlog.test.sh     # the named arms only, no floor
#   RGRL_BEFORE=<a runner> bash <this kit>/run-gates.runlog.test.sh  # AC4 against a named baseline
#
# TOOL-dLoggedFlight-3. Every bar appends one line to `runlog/gates.log` under the git common dir, from
# the runner's EXIT trap. Every arm below drives a COPY of the runner in a scratch clone and reads what
# it wrote; nothing here reads or writes the journal of the clone this file lives in, and no arm runs
# the real bar.
#
# WITHHELD FROM ADOPTERS, AND HELD ON GOV'S BAR. Its subject is the runner in this directory, which an
# adopter copy-installs and never edits, so `kit.toml` withholds this file with a `project-owned` rule
# and the registry carries its leg with an `[[exempt_leg]]` row, per TOOL-aQuenchedHarness-3.
#
# ONE ARM PER ACCEPTANCE CRITERION of the unit's spec, named by it:
#   AC1  a red bar under a pinned run id: one line, its counts, its failing leg, its head
#   AC2  a green bar, a wall-breached bar and an all-held bar each write their own verdict and rc
#   AC3  TERM, INT and HUP each end a running bar with exactly ONE line, verdict=NONE and 128+n, and a
#        TERM held behind a command substitution still carries 143, not the command's 0
#   AC4  the writer adds no external exec after the last leg; a clone's first bar pays one mkdir
#   AC5  a failed append leaves rc and stdout alone and says so once; GOV_RUNLOG=0 writes nothing
#   AC6  this suite's own declarations: withheld, budgeted, a held leg with a ceiling
#   AC7  21 failing legs: fail.1 to fail.20, fail_more=1, and the line under the cap
#   AC8  both refusals after the trap write a pre-header line, and every exit after the trap has an
#        arm or a named exemption (EXITS, which runs last because it reads which arms ran)
#   AC9  a linked worktree and the primary tree write one COMMON journal
#   CAP  a line over the cap is fitted exactly as the runlog kit's `render_line` fits it, both steps
# AC10 is `gotchas.py --for-paths` over the runner, a command of its own, and is not repeated here.
#
# WHAT THIS DOES NOT CHECK. Whether a line MEANS anything past the fields named here: the run model is
# a later unit. The turnstile and the wall watcher are OFF in every bar but the wall arm, so their
# background ticks cannot outlive a bar holding this scratch open; the writer sits in `cleanup`, which
# runs the same with either on. An `exit` inside a function DEFINED above the trap and called below it
# is not enumerated, since the lexer keys on the line the `exit` sits on; the two such functions today,
# `prof_die` and the turnstile ticker, run only above it. A SIGKILL, which runs no trap and leaves no
# line. Wall time, except where the verdict is the wall firing. The lexer is a COPY of the one in the
# unattended kit's run-log suite, because kits do not source each other's tests; each copy is graded
# by its own staged arms.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
FLOOR_ASSERTIONS=192
# Where the scratch clone installs the runner: a FIXTURE-INTERNAL path, bound once, never gov's prefix.
KR=kit/run-gates
n=0; st=0
ARMS_SEEN=" "

# THE AMBIENT SCOPING ENVIRONMENT IS CLEARED ONCE, for every nested bar below. A leg of the real bar
# inherits GATE_SELFTESTS, and a push boundary exports GATE_BASE; a nested runner reading either answers
# a question about the OUTER run, which is `memory/gotchas/inputs-inside-the-subjects-reach.md`.
unset GATE_BASE GATE_FULL GATE_REUSE GATE_JOBS GATE_PROFILES GATE_PROFILE GATE_RUN_ID GATE_SELFTESTS \
  GATE_WALL GATE_LEGS GATE_TURNSTILE GATE_TURNSTILE_HELD GATE_RUN_KEEP GOV_RUNLOG \
  GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR

check() { # name · got · want
  n=$((n + 1))
  [ "$2" = "$3" ] && return 0
  echo "FAIL $1: expected [$3], got [$2]"; st=1; return 1
}

# An arm runs when no selection is made, or when the selection names it. A SELECTED run grades its
# arms and never the floor, and it says so at its end rather than printing a PASS it did not earn.
check_selected() { # arm name -> 0 when it runs
  [ -z "${RGRL_ARMS:-}" ] && return 0
  case " $RGRL_ARMS " in *" $1 "*) return 0 ;; esac
  return 1
}

add_arm_seen() { ARMS_SEEN="$ARMS_SEEN$1|"; }

# ------------------------------------------------------------------------------ the scratch clone
# A MISSING CAPABILITY IS A FAILURE HERE, not a skip: these arms are the only observation the writer
# has, and a suite that skipped them would print a count that proves nothing.
PY=""
if [ -f "$HERE/../lib/resolve-python.sh" ]; then
  # shellcheck source=/dev/null
  . "$HERE/../lib/resolve-python.sh"
  PY=$(resolve_python 2>/dev/null) || PY=""
fi
RUNLOG_KIT="$HERE/../runlog"
[ -n "$PY" ] && [ -f "$RUNLOG_KIT/runlog_lib.py" ] || {
  echo "FAIL no python, or no runlog kit beside this one: the journal cannot be graded, so nothing below can be"; exit 1; }
# AC3 LAUNCHES THROUGH `timeout --foreground`, and INT is the reason. An `&` job of a shell with no job
# control starts with SIGINT ignored, and bash cannot trap a signal that was ignored when it started,
# so a runner launched with a bare `&` sleeps through INT and finishes green. `set -m` first fixes that
# only while this suite did not itself start with INT ignored, and a leg of the real bar always does.
# `timeout` installs its own INT handler whatever it inherited, which `exec` resets to the default in
# its child, so the runner can trap INT however this suite was launched: the class is
# `memory/gotchas/async-job-starts-with-sigint-ignored.md`. The launch below is itself an `&` job, so
# the INT arm grades that reset in a direct run as well as under the bar.
timeout --foreground 10 true >/dev/null 2>&1 || {
  echo "FAIL no runnable 'timeout --foreground' on this host: AC3 cannot deliver INT to a runner launched from a leg"; exit 1; }
WORK=$(mktemp -d 2>/dev/null) || { echo "FAIL no mktemp -d on this host"; exit 1; }
LEG_PIDS=""
remove_scratch() {
  local p
  for p in $LEG_PIDS; do kill "$p" 2>/dev/null; done
  cd / && rm -rf "$WORK"
}
trap remove_scratch EXIT
REPO="$WORK/repo"
JOURNAL="$REPO/.git/runlog/gates.log"
KITV=$(sed -n 's/^KIT_RUN_GATES_VERSION=\([0-9.]*\).*/\1/p' "$HERE/run-gates.sh")

# The journal reader is the runlog kit's own library. Written to a FILE, never fed on stdin.
cat > "$WORK/jl.py" <<'PYEOF'
import sys
sys.path.insert(0, sys.argv[1])
import runlog_lib as r

mode = sys.argv[2]
if mode == "grade":
    j = r.read_journal(sys.argv[3])
    print(f"state={j.state} lines={len(j.lines)} bad={j.bad}")
    for lineno, why in j.refusals[:3]:
        print(f"  refusal line {lineno}: {why}")
elif mode == "render":
    # ONE written line, rebuilt as the runner held it BEFORE the fit: its own fields in their order,
    # every failing leg's name from the manifest back in place of what the fit dropped, and an
    # uncut run id when one is given. The REFERENCE writer must fit that to the same bytes.
    raw = open(sys.argv[3], "rb").read().decode("utf-8").rstrip("\n")
    names = [x for x in open(sys.argv[4], "rb").read().decode("utf-8").split("\n") if x]
    fields = {}
    for part in raw.split("\t"):
        k, _, v = part.partition("=")
        fields[k] = r._parse_value(v)
    base = {k: v for k, v in fields.items()
            if not (k.startswith("fail.") or k in ("fail_more", "kit"))}
    if sys.argv[5] != "-":
        base["run"] = open(sys.argv[5], "rb").read().decode("utf-8")
    for i, nm in enumerate(names[:20], 1):
        base[f"fail.{i}"] = nm
    if len(names) > 20:
        base["fail_more"] = str(len(names) - 20)
    base["kit"] = fields.get("kit", "")
    same = r.render_line(base) == raw and r.check_line(raw) is None
    print(len(raw.encode("utf-8")), fields.get("fail_more", "-"), "SAME" if same else "DIFF")
PYEOF

build_scratch() {
  mkdir -p "$WORK/nohooks" || return 1
  git init -q -b main "$REPO" || return 1
  cd "$REPO" || return 1
  # Hooks pointed at an EMPTY directory rather than bypassed per commit, and autocrlf OFF: the global
  # conf on a Windows node would check the runner out with CRLF in the linked worktree AC9 makes.
  git config user.email t@t; git config user.name t; git config commit.gpgsign false
  git config core.autocrlf false; git config core.hooksPath "$WORK/nohooks"
  mkdir -p "$KR" fx
  cp "$HERE/run-gates.sh" "$HERE/gate-fingerprint.sh" "$HERE/gate-profiles.txt" "$KR/" || return 1
  printf '#!/usr/bin/env bash\necho ok\nexit 0\n' > fx/ok.sh
  printf '#!/usr/bin/env bash\necho boom\nexit 3\n' > fx/red.sh
  # The slow leg reports ready as its FIRST act, with its own pid, and then becomes the sleep. Ready
  # means the runner wrote its header and dispatched, so a signal sent after it lands mid-run.
  printf '#!/usr/bin/env bash\nif [ -n "${RGRL_READY:-}" ]; then echo $$ > "$RGRL_READY.tmp" && mv "$RGRL_READY.tmp" "$RGRL_READY"; fi\nexec sleep 30\n' > fx/slow.sh
  git add -A >/dev/null && git commit -qm base || return 1
  write_legs one '[{"name": "one", "argv": ["bash", "fx/ok.sh"]}]'
  return 0
}

write_legs() { printf '%s\n' "$2" > "$WORK/$1.json"; }   # name · JSON array -> $WORK/<name>.json

# One bar from the scratch clone, stdout and stderr OUTSIDE it: a file written inside would make the
# tree untracked-dirty and move the runner onto a different teardown path.
run_bar() { # NAME=VALUE... -> RC, OUT, ERR
  env GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_WALL=0 "$@" bash "$KR/run-gates.sh" \
    >"$WORK/out" 2>"$WORK/err"; RC=$?
  OUT=$(cat "$WORK/out"); ERR=$(cat "$WORK/err")
}

measure_lines() { # -> the journal's line count, 0 when it is absent
  if [ -f "$JOURNAL" ]; then wc -l < "$JOURNAL" | tr -d ' '; else echo 0; fi
}

read_line() { sed -n "${1}p" "$JOURNAL"; }   # line number -> that line, raw

read_field() { # line number · key -> the value as written, or the literal <absent>
  awk -F'\t' -v l="$1" -v k="$2" 'NR == l { for (i = 1; i <= NF; i++) if (index($i, k "=") == 1) { print substr($i, length(k) + 2); f = 1 } }
    END { if (!f) print "<absent>" }' "$JOURNAL"
}

read_header_key() { # run id · key -> that key of the scratch run record's header
  awk -F'\t' -v k="$2" '$1 == k { print $2 }' "$REPO/.git/gate-run/$1/header" 2>/dev/null
}

check_journal() { # label -> every line in the journal parses under the runlog kit's reader
  local got
  got=$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" grade "$JOURNAL" | head -1)
  check "$1: the journal reads" "${got%% *}" state=read
  check "$1: no bad line in the journal" "${got##* }" bad=0
}

# ------------------------------------------------------------------------------------------ AC1
check_ac1_red() {
  local l0 l
  # A PREVIOUS run first, so a writer that read a stale record — the last run's verdict rather than
  # this one's — has a green one to find.
  write_legs ac1-prev '[{"name": "passing leg", "argv": ["bash", "fx/ok.sh"]}]'
  run_bar GATE_LEGS="$WORK/ac1-prev.json"
  check "AC1 the previous bar is green" "$RC" 0
  write_legs ac1 '[{"name": "passing leg", "argv": ["bash", "fx/ok.sh"]}, {"name": "failing leg", "argv": ["bash", "fx/red.sh"]}]'
  l0=$(measure_lines)
  run_bar GATE_LEGS="$WORK/ac1.json" GATE_RUN_ID=push-1-1
  l=$(measure_lines)
  check "AC1 the bar is red" "$RC" 1
  check "AC1 one bar, one line" "$l" "$((l0 + 1))"
  check "AC1 p" "$(read_field "$l" p)" gates
  check "AC1 ev" "$(read_field "$l" ev)" once
  check "AC1 run is the pinned id" "$(read_field "$l" run)" push-1-1
  check "AC1 verdict" "$(read_field "$l" verdict)" RED
  check "AC1 ran" "$(read_field "$l" ran)" 2
  check "AC1 failed" "$(read_field "$l" failed)" 1
  check "AC1 skipped" "$(read_field "$l" skipped)" 0
  check "AC1 held" "$(read_field "$l" held)" 0
  check "AC1 reused" "$(read_field "$l" reused)" 0
  check "AC1 fail.1 names the failing leg" "$(read_field "$l" fail.1)" "failing leg"
  check "AC1 no second fail field" "$(read_field "$l" fail.2)" "<absent>"
  check "AC1 no fail_more under the cap" "$(read_field "$l" fail_more)" "<absent>"
  check "AC1 the passing leg is named nowhere on the line" "$(read_line "$l" | grep -c 'passing leg')" 0
  check "AC1 head is the scratch HEAD" "$(read_field "$l" head)" "$(git rev-parse HEAD)"
  check "AC1 started is this run's own header value" "$(read_field "$l" started)" "$(read_header_key push-1-1 started)"
  check "AC1 wt is the scratch worktree" "$(read_field "$l" wt)" "$(git rev-parse --show-toplevel)"
  check "AC1 rc is the runner's own" "$(read_field "$l" rc)" "$RC"
  check "AC1 stage is empty once a header exists" "$(read_field "$l" stage)" ""
  check "AC1 full is the header's, empty without GATE_FULL" "$(read_field "$l" full)" ""
  check "AC1 kit is the runner's version" "$(read_field "$l" kit)" "$KITV"
  check "AC1 the previous bar wrote its own green line" "$(read_field $((l - 1)) verdict)" GREEN
  [ "$l" = "$((l0 + 1))" ] && [ "$(read_field "$l" verdict)" = RED ] && add_arm_seen "AC1 red"
  check_journal AC1
}

# ------------------------------------------------------------------------------------------ AC2
check_ac2_paths() {
  local l0 l
  write_legs ac2-green '[{"name": "one", "argv": ["bash", "fx/ok.sh"]}]'
  l0=$(measure_lines)
  run_bar GATE_LEGS="$WORK/ac2-green.json" GATE_SELFTESTS=1
  l=$(measure_lines)
  check "AC2 green bar exits 0" "$RC" 0
  check "AC2 green bar, one line" "$l" "$((l0 + 1))"
  check "AC2 green verdict" "$(read_field "$l" verdict)" GREEN
  check "AC2 green rc" "$(read_field "$l" rc)" 0
  check "AC2 green ran" "$(read_field "$l" ran)" 1
  check "AC2 green failed" "$(read_field "$l" failed)" 0
  check "AC2 green names no failing leg" "$(read_field "$l" fail.1)" "<absent>"
  check "AC2 green wall_breach is empty" "$(read_field "$l" wall_breach)" ""
  check "AC2 selftests carries GATE_SELFTESTS" "$(read_field "$l" selftests)" 1
  [ "$l" = "$((l0 + 1))" ] && [ "$(read_field "$l" verdict)" = GREEN ] && add_arm_seen "AC2 green"
  # THE WALL. The slow leg sleeps 30 s and the wall is 3 s, so the watcher fires, kills the leg's
  # tree and the runner takes its breach exit.
  write_legs ac2-wall '[{"name": "sleeper", "argv": ["bash", "fx/slow.sh"]}]'
  l0=$(measure_lines)
  run_bar GATE_LEGS="$WORK/ac2-wall.json" GATE_WALL=3
  l=$(measure_lines)
  check "AC2 the wall reds the bar" "$RC" 1
  check "AC2 the runner said the wall fired" "$(printf '%s\n' "$OUT" | grep -c 'wall fired')" 1
  check "AC2 wall bar, one line" "$l" "$((l0 + 1))"
  check "AC2 wall verdict" "$(read_field "$l" verdict)" RED
  check "AC2 wall_breach names the wall" "$(read_field "$l" wall_breach)" 3
  check "AC2 wall rc" "$(read_field "$l" rc)" 1
  [ "$l" = "$((l0 + 1))" ] && [ "$(read_field "$l" wall_breach)" = 3 ] && add_arm_seen "AC2 wall"
  # EVERY LEG HELD, which the runner refuses with exit 2 rather than calling green.
  write_legs ac2-held '[{"name": "held one", "argv": ["bash", "fx/ok.sh"], "subject": "kit"}]'
  l0=$(measure_lines)
  run_bar GATE_LEGS="$WORK/ac2-held.json"
  l=$(measure_lines)
  check "AC2 an all-held bar is refused" "$RC" 2
  check "AC2 held bar, one line" "$l" "$((l0 + 1))"
  check "AC2 held verdict" "$(read_field "$l" verdict)" REFUSED
  check "AC2 held rc" "$(read_field "$l" rc)" 2
  check "AC2 held count" "$(read_field "$l" held)" 1
  check "AC2 held ran" "$(read_field "$l" ran)" 0
  check "AC2 held selftests is empty without GATE_SELFTESTS" "$(read_field "$l" selftests)" ""
  [ "$l" = "$((l0 + 1))" ] && [ "$(read_field "$l" verdict)" = REFUSED ] && add_arm_seen "AC2 refused"
  check_journal AC2
}

# ------------------------------------------------------------------------------------------ AC3
# THE SIGNAL IS SENT ONLY ONCE THE LEG IS PROVABLY RUNNING, and it is sent to the RUNNER. The leg
# writes the ready file as its first act, so the runner is past its header and waiting on it. The
# runner's pid is the tail of its default run id, which `gate-run/current` names: `timeout` is the
# process this suite started, and signalling it would test timeout's forwarding instead of the trap.
check_ac3_signals() {
  local sig want rp l0 l i lp id rpid tp rc
  write_legs ac3 '[{"name": "sleeper", "argv": ["bash", "fx/slow.sh"]}]'
  for sig in TERM INT HUP; do
    case $sig in TERM) want=143 ;; INT) want=130 ;; HUP) want=129 ;; esac
    rp="$WORK/ready.$sig"; rm -f "$rp"; l0=$(measure_lines)
    RGRL_READY="$rp" GATE_LEGS="$WORK/ac3.json" GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_WALL=0 \
      timeout --foreground 300 bash "$KR/run-gates.sh" >"$WORK/out.$sig" 2>&1 &
    tp=$!
    i=0; while [ ! -s "$rp" ] && [ "$i" -lt 600 ]; do sleep 0.1; i=$((i + 1)); done
    lp=$(cat "$rp" 2>/dev/null); LEG_PIDS="$LEG_PIDS $lp"
    id=$(cat "$REPO/.git/gate-run/current" 2>/dev/null); rpid=${id##*-}
    check "AC3 $sig: the leg reported ready, so the bar is past its header" "$([ -n "$lp" ] && echo yes)" yes
    check "AC3 $sig: the run id names the runner's pid" "$(case "$rpid" in ''|*[!0-9]*) echo no ;; *) echo yes ;; esac)" yes
    check "AC3 $sig: no line before the signal" "$(measure_lines)" "$l0"
    kill -"$sig" "$rpid" 2>/dev/null
    wait "$tp"; rc=$?
    l=$(measure_lines)
    check "AC3 $sig: the bar exits with 128 plus the signal" "$rc" "$want"
    check "AC3 $sig: exactly ONE line" "$((l - l0))" 1
    check "AC3 $sig: verdict NONE, since no verdict file was written" "$(read_field "$l" verdict)" NONE
    check "AC3 $sig: rc is the signal's status" "$(read_field "$l" rc)" "$want"
    check "AC3 $sig: the line names the run that was killed" "$(read_field "$l" run)" "$id"
    check "AC3 $sig: stage is empty, since the header was written" "$(read_field "$l" stage)" ""
    check "AC3 $sig: head is still read back from the header" "$(read_field "$l" head)" "$(git rev-parse HEAD)"
    check "AC3 $sig: the counts are empty with no verdict to read" "$(read_field "$l" ran)" ""
    kill "$lp" 2>/dev/null
  done
  # A SIGNAL THAT LANDS IN A FOREGROUND COMMAND, and this is the case the explicit status exists for.
  # A signal that interrupts `wait -n` leaves `$?` at 128+n when the trap starts, so the three arms
  # above read the right status with or without it. One that lands while the runner waits on a command
  # substitution runs its trap only when that command ends, with `$?` at the command's own 0. The
  # runner here is a copy beside a fingerprint stub that reports ready and holds the first
  # `$(fingerprint)` open until the signal has been sent, which is after the trap and before the
  # header, so the same line also shows a run killed before its header.
  local fp="$WORK/fp-stub/run-gates"
  mkdir -p "$fp"
  cp "$HERE/run-gates.sh" "$HERE/gate-profiles.txt" "$fp/"
  printf '#!/usr/bin/env bash\nif [ -n "${RGRL_FP_READY:-}" ]; then\n  echo $$ > "$RGRL_FP_READY.tmp" && mv "$RGRL_FP_READY.tmp" "$RGRL_FP_READY"\n  i=0; while [ ! -e "$RGRL_FP_READY.sent" ] && [ "$i" -lt 300 ]; do sleep 0.1; i=$((i + 1)); done\nfi\necho fixture-fingerprint\n' \
    > "$fp/gate-fingerprint.sh"
  rp="$WORK/ready.fp"; rm -f "$rp" "$rp.sent"; l0=$(measure_lines)
  RGRL_FP_READY="$rp" GATE_LEGS="$WORK/one.json" GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_WALL=0 \
    timeout --foreground 300 bash "$fp/run-gates.sh" >"$WORK/out.fp" 2>&1 &
  tp=$!
  i=0; while [ ! -s "$rp" ] && [ "$i" -lt 600 ]; do sleep 0.1; i=$((i + 1)); done
  id=$(cat "$REPO/.git/gate-run/current" 2>/dev/null); rpid=${id##*-}
  check "AC3 foreground: the stub holds the runner in a command substitution" "$([ -s "$rp" ] && echo yes)" yes
  kill -TERM "$rpid" 2>/dev/null
  : > "$rp.sent"
  wait "$tp"; rc=$?
  l=$(measure_lines)
  check "AC3 foreground: the bar exits 143" "$rc" 143
  check "AC3 foreground: exactly ONE line" "$((l - l0))" 1
  check "AC3 foreground: rc is the signal's status, not the command's" "$(read_field "$l" rc)" 143
  check "AC3 foreground: verdict NONE" "$(read_field "$l" verdict)" NONE
  check "AC3 foreground: killed before the header, so stage pre-header" "$(read_field "$l" stage)" pre-header
  check "AC3 foreground: the line names the run that was killed" "$(read_field "$l" run)" "$id"
  check_journal AC3
}

# ------------------------------------------------------------------------------------------ AC4
# THE EXEC COUNT, from an xtrace on ITS OWN DESCRIPTOR, so a command inside a `2>/dev/null` callee is
# still seen. A command word that is not an assignment, a builtin, a keyword or a function the traced
# runner defines is an external exec. The window opens at the first depth-one `remove_wall_watcher`,
# which follows the last leg's `wait`, and runs to the end of the trace, the EXIT trap included.
measure_execs() { # trace file · the runner it traced -> "<count> <sorted names>"
  local known l w c=0 names="" on="" pre
  known=" $(compgen -b | tr '\n' ' ') $(compgen -k | tr '\n' ' ') "
  known="$known$(sed -n 's/^[[:space:]]*\([A-Za-z_][A-Za-z0-9_]*\)[[:space:]]*()[[:space:]]*{.*/\1/p' "$2" | tr '\n' ' ') "
  while IFS= read -r l; do
    case "$l" in +*) ;; *) continue ;; esac
    pre=${l%%[!+]*}; l=${l#"$pre"}; l=${l# }
    w=${l%% *}; w=${w#\'}; w=${w%\'}
    if [ -z "$on" ]; then
      [ "$pre" = + ] && [ "$w" = remove_wall_watcher ] && on=1
      continue
    fi
    case "$w" in ""|*=*|\(*) continue ;; esac
    case "$known" in *" $w "*) continue ;; esac
    c=$((c + 1)); names="$names$w"$'\n'
  done < "$1"
  [ -n "$on" ] || { echo "nowindow"; return 0; }
  printf '%s %s\n' "$c" "$(printf '%s' "$names" | sort | tr '\n' ' ')"
}

build_traced_runner() { # side · runner source -> a copy with its siblings, OUTSIDE the scratch tree
  mkdir -p "$WORK/traced-$1/run-gates"
  cp "$2" "$WORK/traced-$1/run-gates/run-gates.sh"
  cp "$HERE/gate-fingerprint.sh" "$HERE/gate-profiles.txt" "$WORK/traced-$1/run-gates/"
  printf '%s' "$WORK/traced-$1/run-gates/run-gates.sh"
}

run_traced() { # trace file · runner · NAME=VALUE... -> one bar under xtrace into the file
  local tf=$1 rn=$2; shift 2
  env PS4='+ ' BASH_XTRACEFD=9 GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_WALL=0 GATE_RUN_KEEP=1000 \
    "$@" bash -x "$rn" 9>"$tf" >/dev/null 2>&1
}

check_ac4_spawns() {
  local before after l0 off on first extra rc
  write_legs ac4 '[{"name": "one", "argv": ["bash", "fx/ok.sh"]}, {"name": "two", "argv": ["bash", "fx/ok.sh"]}]'
  # WARM, so both traced bars find a ledger and a journal directory already there: the first bar in a
  # clone takes the ledger's no-merge branch and the one-time mkdir, which are not the writer's cost.
  run_bar GATE_LEGS="$WORK/ac4.json" GATE_RUN_KEEP=1000
  check "AC4 the journal directory exists before the traced bars" "$([ -d "$REPO/.git/runlog" ] && echo yes)" yes
  after=$(build_traced_runner after "$HERE/run-gates.sh")
  l0=$(measure_lines)
  # THE BASELINE NEVER CALLS THE WRITER. A copy whose `cleanup` has lost the call is the base teardown
  # byte for byte; `GOV_RUNLOG=0` is not, because it still runs whatever the writer does before it reads
  # the switch, and an exec placed there would be counted on both sides and never seen.
  if [ -n "${RGRL_BEFORE:-}" ]; then
    before=$(build_traced_runner before "$RGRL_BEFORE")
    echo "AC4 baseline: the runner named by RGRL_BEFORE"
  else
    sed 's/^cleanup() { write_runlog_verdict "\$?"; /cleanup() { /' "$HERE/run-gates.sh" > "$WORK/no-writer.sh"
    check "AC4 the baseline copy's cleanup no longer calls the writer" \
      "$(grep -c '^cleanup() {.*write_runlog_verdict' "$WORK/no-writer.sh")|$(grep -c '^cleanup() { run_outstanding_reap;' "$WORK/no-writer.sh")" "0|1"
    before=$(build_traced_runner before "$WORK/no-writer.sh")
  fi
  run_traced "$WORK/t.off" "$before" GATE_LEGS="$WORK/ac4.json"; rc=$?
  # BOTH SIDES DID THE WORK: equal counts from two bars that refused early would compare nothing.
  check "AC4 the baseline bar ran green" "$rc" 0
  check "AC4 the baseline bar wrote no line" "$(measure_lines)" "$l0"
  run_traced "$WORK/t.on" "$after" GATE_LEGS="$WORK/ac4.json"; rc=$?
  check "AC4 the writer's bar ran green" "$rc" 0
  check "AC4 the traced bar with the writer on wrote one line" "$(measure_lines)" "$((l0 + 1))"
  off=$(measure_execs "$WORK/t.off" "$before"); on=$(measure_execs "$WORK/t.on" "$after")
  check "AC4 the window opens in the baseline trace" "$([ "$off" != nowindow ] && echo yes)" yes
  check "AC4 the window opens in the writer's trace" "$([ "$on" != nowindow ] && echo yes)" yes
  check "AC4 the probe sees execs after the last leg" "$([ "${off%% *}" -gt 0 ] 2>/dev/null && echo yes)" yes
  echo "AC4 execs after the last leg: baseline ${off%% *}, writer on ${on%% *}"
  check "AC4 the writer adds no external exec after the last leg" "$on" "$off"
  # The one sanctioned spawn: a clone's FIRST bar makes the journal directory, once.
  mv "$REPO/.git/runlog" "$WORK/runlog.keep"
  run_traced "$WORK/t.first" "$after" GATE_LEGS="$WORK/ac4.json"; rc=$?
  check "AC4 the first bar ran green" "$rc" 0
  first=$(measure_execs "$WORK/t.first" "$after")
  extra=$(comm -13 <(printf '%s\n' ${on#* } | sort) <(printf '%s\n' ${first#* } | sort) | tr '\n' ' ')
  check "AC4 a clone's first bar pays exactly one mkdir" "$extra" "mkdir "
  check "AC4 and nothing else" "${first%% *}" "$(( ${on%% *} + 1 ))"
  check "AC4 and that bar still wrote its line" "$(wc -l < "$REPO/.git/runlog/gates.log" | tr -d ' ')" 1
  cat "$REPO/.git/runlog/gates.log" >> "$WORK/runlog.keep/gates.log"
  rm -rf "$REPO/.git/runlog"; mv "$WORK/runlog.keep" "$REPO/.git/runlog"
  check_journal AC4
}

# ------------------------------------------------------------------------------------------ AC5
check_ac5_write_failure() {
  local out_off rc_off err_off l0
  write_legs ac5 '[{"name": "one", "argv": ["bash", "fx/ok.sh"]}]'
  mv "$REPO/.git/runlog" "$WORK/runlog.keep"
  : > "$REPO/.git/runlog"
  run_bar GATE_LEGS="$WORK/ac5.json" GOV_RUNLOG=0; out_off=$OUT; rc_off=$RC; err_off=$ERR
  check "AC5 the switch-off bar is green, so rc and stdout are compared between two bars that ran" "$rc_off" 0
  run_bar GATE_LEGS="$WORK/ac5.json"
  check "AC5 a failed append leaves rc alone" "$RC" "$rc_off"
  check "AC5 a failed append leaves stdout alone" "$OUT" "$out_off"
  check "AC5 stderr carries ONE run-log line" "$(printf '%s\n' "$ERR" | grep -c '^run-gates: run log')" 1
  check "AC5 that line names the file it could not write" "$(printf '%s\n' "$ERR" | grep '^run-gates: run log' | grep -c 'runlog/gates.log')" 1
  check "AC5 and nothing else new on stderr" "$(printf '%s\n' "$ERR" | grep -v '^run-gates: run log')" "$err_off"
  # A RED bar too: its rc is the one a failed write must never turn into a green.
  write_legs ac5-red '[{"name": "one", "argv": ["bash", "fx/red.sh"]}]'
  run_bar GATE_LEGS="$WORK/ac5-red.json"
  check "AC5 a red bar keeps its rc when the append fails" "$RC" 1
  check "AC5 and says so once" "$(printf '%s\n' "$ERR" | grep -c '^run-gates: run log')" 1
  rm -f "$REPO/.git/runlog"; mv "$WORK/runlog.keep" "$REPO/.git/runlog"
  l0=$(measure_lines)
  run_bar GATE_LEGS="$WORK/ac5.json" GOV_RUNLOG=0
  check "AC5 GOV_RUNLOG=0 writes nothing" "$(measure_lines)" "$l0"
  check "AC5 and says nothing on stderr about the log" "$(printf '%s\n' "$ERR" | grep -c '^run-gates: run log')" 0
  run_bar GATE_LEGS="$WORK/ac5.json" GOV_RUNLOG=1
  check "AC5 any other value of the switch writes" "$(measure_lines)" "$((l0 + 1))"
  check_journal AC5
}

# ------------------------------------------------------------------------------------------ AC6
# THIS SUITE'S OWN DECLARATIONS, read from the files that make them. The version carriers, the
# deployer's resolution and the budget verdict are graded by their own legs after the build; what is
# asserted here is that each declaration EXISTS, so a suite that ships, runs unbudgeted or drops off
# the manifest reds here too.
check_ac6_declarations() {
  local legs="$HERE/../gate-legs.json"
  check "AC6 the suite is withheld by the kit's project-owned list" \
    "$(awk '/^\[\[files\]\]/ { inc = "" } /^include = \[/ { inc = $0 } /^role = "project-owned"/ && inc ~ /"run-gates\.runlog\.test\.sh"/ { print "withheld" }' "$HERE/kit.toml")" withheld
  check "AC6 the suite's leg has a budget row" \
    "$(awk -F'\t' '$1 == "run-gates run-log line" && $2 ~ /^[0-9]+$/ { print "budgeted" }' "$HERE/selftest-budgets.txt")" budgeted
  check "AC6 the suite's leg is held, guarded and bounded" "$("$PY" -c '
import json, sys
rows = [l for l in json.load(open(sys.argv[1], encoding="utf-8")) if l.get("name") == "run-gates run-log line"]
ok = (len(rows) == 1 and rows[0]["argv"][-1].endswith("/run-gates.runlog.test.sh")
      and rows[0].get("chunk") == "selftests" and rows[0].get("subject") == "kit"
      and isinstance(rows[0].get("ceiling"), int) and rows[0]["ceiling"] > 0
      and any(g.endswith("run-gates/") for g in rows[0].get("guard", [])))
print("declared" if ok else "not declared")
' "$legs")" declared
  check "AC6 the runner and its README carry one version" \
    "$(grep -c "gov:kit run-gates@$KITV\b" "$HERE/README.md")" 1
}

# ------------------------------------------------------------------------------------------ AC7
check_ac7_many_fails() {
  local legs="" i l0 l
  for i in $(seq -w 1 21); do legs="$legs${legs:+, }{\"name\": \"red $i\", \"argv\": [\"bash\", \"fx/red.sh\"]}"; done
  write_legs ac7 "[$legs]"
  l0=$(measure_lines)
  run_bar GATE_LEGS="$WORK/ac7.json" GATE_JOBS=4
  l=$(measure_lines)
  check "AC7 the bar is red" "$RC" 1
  check "AC7 one line" "$l" "$((l0 + 1))"
  check "AC7 failed counts all 21" "$(read_field "$l" failed)" 21
  check "AC7 fail.1 is the first failing leg in the manifest" "$(read_field "$l" fail.1)" "red 01"
  check "AC7 fail.20 is the twentieth" "$(read_field "$l" fail.20)" "red 20"
  check "AC7 no fail.21" "$(read_field "$l" fail.21)" "<absent>"
  check "AC7 fail_more counts the rest" "$(read_field "$l" fail_more)" 1
  check "AC7 the line is at or under 2048 bytes" "$(read_line "$l" | LC_ALL=C awk '{ print (length($0) <= 2048) ? "under" : "over" }')" under
  check_journal AC7
}

# ------------------------------------------------------------------------------------------ AC8
check_ac8_pre_header() {
  local l0 l
  # THE MANIFEST PARSE, the second refusal after the trap. The run directory exists and holds no
  # header, so `stage=pre-header` is read off the record rather than assumed.
  printf '[{"name": "one", "argv": \n' > "$WORK/ac8-bad.json"
  l0=$(measure_lines)
  run_bar GATE_LEGS="$WORK/ac8-bad.json" GATE_RUN_ID=bad-manifest
  l=$(measure_lines)
  check "AC8 a malformed manifest refuses" "$RC" 2
  check "AC8 manifest: one line" "$l" "$((l0 + 1))"
  check "AC8 manifest: verdict NONE" "$(read_field "$l" verdict)" NONE
  check "AC8 manifest: stage pre-header" "$(read_field "$l" stage)" pre-header
  check "AC8 manifest: rc 2" "$(read_field "$l" rc)" 2
  check "AC8 manifest: run is the pinned id" "$(read_field "$l" run)" bad-manifest
  check "AC8 manifest: the header's keys are empty" "$(read_field "$l" wt)|$(read_field "$l" head)|$(read_field "$l" started)" "||"
  check "AC8 manifest: the run directory exists with no header" \
    "$([ -d "$REPO/.git/gate-run/bad-manifest" ] && [ ! -e "$REPO/.git/gate-run/bad-manifest/header" ] && echo yes)" yes
  [ "$l" = "$((l0 + 1))" ] && [ "$(read_field "$l" stage)" = pre-header ] && add_arm_seen "AC8 manifest"
  # THE RUN-DIRECTORY MKDIR, the first refusal after the trap: a FILE where the run root must go.
  mv "$REPO/.git/gate-run" "$WORK/gate-run.keep"; : > "$REPO/.git/gate-run"
  l0=$(measure_lines)
  run_bar GATE_LEGS="$WORK/one.json" GATE_RUN_ID=no-dir
  l=$(measure_lines)
  check "AC8 an uncreatable run record refuses" "$RC" 2
  check "AC8 run-dir: the runner said why" "$(printf '%s\n' "$ERR" | grep -c 'cannot create the run record')" 1
  check "AC8 run-dir: one line" "$l" "$((l0 + 1))"
  check "AC8 run-dir: verdict NONE" "$(read_field "$l" verdict)" NONE
  check "AC8 run-dir: stage pre-header" "$(read_field "$l" stage)" pre-header
  check "AC8 run-dir: rc 2" "$(read_field "$l" rc)" 2
  check "AC8 run-dir: run is the pinned id" "$(read_field "$l" run)" no-dir
  [ "$l" = "$((l0 + 1))" ] && [ "$(read_field "$l" stage)" = pre-header ] && add_arm_seen "AC8 run-dir"
  rm -f "$REPO/.git/gate-run"; mv "$WORK/gate-run.keep" "$REPO/.git/gate-run"
  check_journal AC8
}

# THE EXIT-SITE ENUMERATION. A small lexer, because every cheaper predicate read something else: `exit`
# appears in the runner's awk and python programs, its messages and its comments. It tracks single,
# double and ANSI-C quotes and skips comments and here-document bodies, then reports each `exit` word in
# command position as `<file> <line> <marked> <text>`; the marked field is the copy's origin and unused.
scan_exit_sites() { # file... -> one TAB-separated row per shell exit
  awk '
    FNR == 1 { st = "N"; hd = ""; prevcode = "" }
    {
      line = $0; sub(/\r$/, "", line)
      if (hd != "") { t = line; sub(/^\t+/, "", t); if (t == hd) hd = ""; next }
      nl = length(line); i = 1; pend = ""
      while (i <= nl) {
        c = substr(line, i, 1)
        if (st == "S") { if (c == "\047") st = "N"; i++; continue }
        if (st == "A") { if (c == "\\") { i += 2; continue }; if (c == "\047") st = "N"; i++; continue }
        if (st == "D") { if (c == "\\") { i += 2; continue }; if (c == "\"") st = "N"; i++; continue }
        if (c == "\\") { i += 2; continue }
        if (c == "$" && substr(line, i + 1, 1) == "\047") { st = "A"; i += 2; continue }
        if (c == "\047") { st = "S"; i++; continue }
        if (c == "\"") { st = "D"; i++; continue }
        b = (i == 1) ? " " : substr(line, i - 1, 1)
        if (c == "#" && b ~ /[ \t;&|()]/) break
        if (c == "<" && substr(line, i, 3) ~ /^<<[^<]/) {
          rest = substr(line, i + 2); sub(/^-/, "", rest); sub(/^[ \t]*/, "", rest)
          if (match(rest, /^["\047]?[A-Za-z_][A-Za-z0-9_]*/)) { w = substr(rest, RSTART, RLENGTH); gsub(/["\047]/, "", w); pend = w }
          i += 2; continue
        }
        if (substr(line, i, 4) == "exit" && b ~ /[ \t;&|({!]/ && (i + 4 > nl || substr(line, i + 4, 1) ~ /[ \t;)}]/)) {
          pre = substr(line, 1, i - 1); sub(/[ \t]+$/, "", pre)
          # COMMAND POSITION, not merely a word: `f+=(rc "$rc" exit "$ex")` names a key.
          if (pre != "" && pre !~ /(;|&&|\|\||\||[{()!]|(^|[ \t])(then|else|do))$/) { i += 4; continue }
          text = line; sub(/^[ \t]+/, "", text); sub(/[ \t]+$/, "", text)
          printf "%s\t%d\t0\t%s\n", FILENAME, FNR, text
          i += 4; continue
        }
        i++
      }
      if (pend != "") hd = pend
    }' "$@"
}

# Every exit AFTER the trap line, by its trimmed TEXT and the number of sites carrying that text, joined
# to the table below. Text rather than a line number, because every edit above an exit moves its line;
# text AND count, because the red bar and the wall breach both end `exit 1`, and a third one must read
# as a count that moved rather than as a match.
cat > "$WORK/exits.tsv" <<'EXITS'
echo "run-gates: cannot create the run record at $RUNDIR" >&2; exit 2	1	AC8 run-dir
' "$LEGS_FILE" "$TIMINGS") || { echo "run-gates: cannot parse $LEGS_FILE"; exit 2; }	1	AC8 manifest
kill -0 "$_me" 2>/dev/null || exit 0	1	exempt: the wall watcher's ( … ) & subshell, which runs no trap of the runner's
[ -f "$_work/wall.disarm" ] && exit 0	1	exempt: the wall watcher's ( … ) & subshell, which runs no trap of the runner's
cd "$dir" || exit 97	1	exempt: run_leg_at's ( … ) subshell, from TOOL-dDerivedDocket-23's red attribution, which runs no trap of the runner's
exit 1	2	AC2 wall|AC1 red
exit 2	1	AC2 refused
echo "gates GREEN — $ran/$ran legs passed$skipnote"; exit 0	1	AC2 green
EXITS

check_exit_table() { # runner -> EXIT_TRAP, EXIT_SITES, EXIT_UNKNOWN, EXIT_MISCOUNT, EXIT_STALE
  local cnt text want
  EXIT_TRAP=$(grep -n '^trap cleanup EXIT$' "$1" | head -1 | cut -d: -f1)
  scan_exit_sites "$1" | awk -F'\t' -v t="${EXIT_TRAP:-999999}" '$2 > t { print $4 }' \
    | LC_ALL=C sort | uniq -c > "$WORK/sites.txt"
  EXIT_SITES=0; EXIT_UNKNOWN=""; EXIT_MISCOUNT=""; EXIT_STALE=""
  while read -r cnt text; do
    [ -n "$text" ] || continue
    EXIT_SITES=$((EXIT_SITES + cnt))
    want=$(X="$text" awk -F'\t' '$1 == ENVIRON["X"] { print $2 }' "$WORK/exits.tsv")
    if [ -z "$want" ]; then EXIT_UNKNOWN="$EXIT_UNKNOWN[$text]"
    elif [ "$want" != "$cnt" ]; then EXIT_MISCOUNT="$EXIT_MISCOUNT[$text: $cnt sites, table $want]"; fi
  done < "$WORK/sites.txt"
  while IFS=$'\t' read -r text want _; do
    [ -n "$text" ] || continue
    X="$text" awk '{ sub(/^ *[0-9]+ /, "") } $0 == ENVIRON["X"] { f = 1 } END { exit !f }' "$WORK/sites.txt" \
      || EXIT_STALE="$EXIT_STALE[$text]"
  done < "$WORK/exits.tsv"
}

check_ac8_exits() {
  local text want arm a unarmed=""
  check_exit_table "$HERE/run-gates.sh"
  check "AC8 EXITS the trap line is found" "$([ -n "$EXIT_TRAP" ] && echo found)" found
  check "AC8 EXITS the scan sees the exits after the trap" "$([ "$EXIT_SITES" -ge 8 ] && echo yes)" yes
  check "AC8 EXITS every exit after the trap has a row" "${EXIT_UNKNOWN:-none}" none
  check "AC8 EXITS every row's site count holds" "${EXIT_MISCOUNT:-none}" none
  check "AC8 EXITS every row still names a site" "${EXIT_STALE:-none}" none
  # EVERY ARM A ROW NAMES RAN, AND SAW ITS LINE. A selected run did not run them all, so it says so.
  if [ -z "${RGRL_ARMS:-}" ]; then
    while IFS=$'\t' read -r text want arm; do
      case "$arm" in exempt:*) continue ;; esac
      while IFS= read -r a; do
        [ -n "$a" ] || continue
        case "$ARMS_SEEN" in *" $a|"*|*"|$a|"*) ;; *) unarmed="$unarmed[$a]" ;; esac
      done <<<"${arm//|/$'\n'}"
    done < "$WORK/exits.tsv"
    check "AC8 EXITS every arm the table names ran and saw its line" "${unarmed:-none}" none
  else
    echo "SKIP AC8 EXITS arm join: RGRL_ARMS selected [$RGRL_ARMS], so not every arm the table names ran"
  fi
  # THE ENUMERATION'S FAILING CASES, staged into COPIES every run: an exit nobody armed, directly
  # below the trap; a second copy of an armed text, which only the count can see; and the control.
  awk '{ print } /^trap cleanup EXIT$/ { print "exit 3" }' "$HERE/run-gates.sh" > "$WORK/mut.sh"
  check_exit_table "$WORK/mut.sh"
  check "AC8 EXITS staged: an unarmed exit below the trap is caught" "$EXIT_UNKNOWN" "[exit 3]"
  { cat "$HERE/run-gates.sh"; printf 'exit 2\n'; } > "$WORK/mut.sh"
  check_exit_table "$WORK/mut.sh"
  check "AC8 EXITS staged: a second copy of an armed text is caught" "$EXIT_MISCOUNT" "[exit 2: 2 sites, table 1]"
  awk '/^trap cleanup EXIT$/ { print "# exit 3 in a comment"; print "echo \"exit 3\"" } { print }' "$HERE/run-gates.sh" > "$WORK/mut.sh"
  check_exit_table "$WORK/mut.sh"
  check "AC8 EXITS control: a comment and a string are not exits" "${EXIT_UNKNOWN:-none}|${EXIT_MISCOUNT:-none}" "none|none"
}

# ------------------------------------------------------------------------------------------ AC9
check_ac9_worktree() {
  local wt="$WORK/wt2" l top gd
  git worktree add -q "$wt" -b side >/dev/null 2>&1
  write_legs ac9 '[{"name": "one", "argv": ["bash", "fx/ok.sh"]}]'
  (cd "$wt" && env GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_WALL=0 GATE_LEGS="$WORK/ac9.json" \
    GATE_RUN_ID=from-worktree bash "$KR/run-gates.sh" >/dev/null 2>&1)
  l=$(measure_lines)
  top=$(git -C "$wt" rev-parse --show-toplevel)
  gd=$(git -C "$wt" rev-parse --path-format=absolute --git-dir)
  check "AC9 the linked worktree's line lands in the COMMON journal" "$(read_field "$l" run)" from-worktree
  check "AC9 and names the worktree it ran in" "$(read_field "$l" wt)" "$top"
  check "AC9 its own git dir is under worktrees" "$(case "$gd" in */.git/worktrees/*) echo yes ;; esac)" yes
  check "AC9 nothing is journaled under the worktree's git dir" "$([ -e "$gd/runlog" ] && echo present || echo none)" none
  check "AC9 its run record is its own" "$([ -f "$gd/gate-run/from-worktree/verdict" ] && echo yes)" yes
  run_bar GATE_LEGS="$WORK/ac9.json" GATE_RUN_ID=from-primary
  l=$(measure_lines)
  check "AC9 the primary tree writes the same file" "$(read_field "$l" run)" from-primary
  check "AC9 and names itself" "$(read_field "$l" wt)" "$(git rev-parse --show-toplevel)"
  check "AC9 the journal is the one under the common dir" \
    "$([ "$(cd "$(git rev-parse --path-format=absolute --git-common-dir)/runlog" && pwd)" = "$(cd "$REPO/.git/runlog" && pwd)" ] && echo yes)" yes
  git worktree remove --force "$wt" >/dev/null 2>&1
  check_journal AC9
}

# ------------------------------------------------------------------------------------------ CAP
# BOTH STEPS OF THE FIT, each re-rendered by the runlog kit's reference writer from what the runner held
# before it fitted the line, and each required to come back byte-identical.
#   Step one: 21 failing legs whose names are long enough that twenty of them overflow the cap, so
#   whole fail.<i> fields drop, highest first, into the fail_more the runner already wrote.
#   Step two: a run id over the filesystem's name limit, so the run-directory mkdir refuses, the line
#   is pre-header, and the id is the longest value: plain ASCII, a three-byte character behind a zero-,
#   one- and two-byte prefix so a cut lands INSIDE a character, and TABs, whose two-byte escape a cut
#   can halve, behind the same three prefixes.
check_cap_fit() {
  local legs="" i nm res id pre short=0 halved=0 l
  : > "$WORK/names.txt"
  for i in $(seq -w 1 21); do
    nm="leg $i $(printf 'n%.0s' $(seq 1 110))"
    printf '%s\n' "$nm" >> "$WORK/names.txt"
    legs="$legs${legs:+, }{\"name\": \"$nm\", \"argv\": [\"bash\", \"fx/red.sh\"]}"
  done
  write_legs cap "[$legs]"
  run_bar GATE_LEGS="$WORK/cap.json" GATE_JOBS=4 GATE_RUN_ID=cap-drop
  l=$(measure_lines); read_line "$l" > "$WORK/one.log"
  res=$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" render "$WORK/one.log" "$WORK/names.txt" -)
  check "CAP step one: the line is cut as render_line cuts it" "${res##* }" SAME
  check "CAP step one: fields dropped into the fail_more already there" "$(read_field "$l" fail_more | awk '{ print ($1 > 1) ? "added" : "not added" }')" added
  check "CAP step one: fail.1 survives the drop" "$(read_field "$l" fail.1)" "$(head -1 "$WORK/names.txt")"
  : > "$WORK/nonames.txt"
  for pre in ascii "" a ab tab tab.a tab.aa; do
    case "$pre" in
      ascii) id=$(printf 'X%.0s' $(seq 1 2500)) ;;
      tab*)  id="${pre#tab}"; id="${id#.}$(printf 'a\t%.0s' $(seq 1 1100))" ;;
      *)     id="$pre$(printf '€%.0s' $(seq 1 900))" ;;
    esac
    printf '%s' "$id" > "$WORK/full"
    run_bar GATE_LEGS="$WORK/one.json" GATE_RUN_ID="$id"
    l=$(measure_lines); read_line "$l" > "$WORK/one.log"
    check "CAP step two [$pre]: an over-long run id refuses the run directory" "$RC|$(read_field "$l" stage)" "2|pre-header"
    res=$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" render "$WORK/one.log" "$WORK/nonames.txt" "$WORK/full")
    check "CAP step two [$pre]: the run id is cut as render_line cuts it" "${res##* }" SAME
    case "$pre" in
      tab*) case "$res" in "2047 "*) halved=$((halved + 1)) ;; esac ;;
      ascii) ;;
      *) case "$res" in "2048 "*) ;; *) short=$((short + 1)) ;; esac ;;
    esac
  done
  check "CAP a cut landed inside a character at least once" "$([ "$short" -gt 0 ] && echo yes)" yes
  check "CAP a cut halved an escape at least once" "$([ "$halved" -gt 0 ] && echo yes)" yes
  check_journal CAP
}

build_scratch || { echo "FAIL the scratch clone could not be built"; exit 1; }

check_selected AC1 && check_ac1_red
check_selected AC2 && check_ac2_paths
check_selected AC3 && check_ac3_signals
check_selected AC4 && check_ac4_spawns
check_selected AC5 && check_ac5_write_failure
check_selected AC6 && check_ac6_declarations
check_selected AC7 && check_ac7_many_fails
check_selected AC8 && check_ac8_pre_header
check_selected AC9 && check_ac9_worktree
check_selected CAP && check_cap_fit
check_selected AC8 && check_ac8_exits

if [ -n "${RGRL_ARMS:-}" ]; then
  echo "SELECTED ($n assertions, arms [$RGRL_ARMS]; the floor of $FLOOR_ASSERTIONS grades only a full run)"
  exit "$st"
fi
if [ "$n" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "FAIL $n assertions ran, under the floor of $FLOOR_ASSERTIONS: an arm stopped asserting"; st=1
fi
[ "$st" = 0 ] && echo "PASS ($n assertions)"
[ "$st" = 0 ] || echo "FAILED ($n assertions)"
exit "$st"
