#!/usr/bin/env bash
# runlog-writer.test.sh — the unattended driver's run log, observed from OUTSIDE the driver.
#
#   bash <this kit>/runlog-writer.test.sh
#
# TOOL-dLoggedFlight-2. The driver writes a START line before it parses its arguments and an END line
# from an EXIT trap, into `runlog/driver.log` under the git common dir. Every arm below drives a COPY
# of the driver in a scratch clone and reads what it wrote; nothing here reads or writes the journal
# of the clone this file lives in.
#
# APPROVED BY THE OWNER 2026-09-13, AND NOT A GATE LEG. This kit's self-tests stay off the merge bar
# (the 2026-08-23 ruling recorded in kit.toml) and out of adopters' trees (TOOL-aQuenchedHarness-3),
# so this suite is withheld by kit.toml's project-owned list and budgeted as a NON-held row of the
# self-test budget file. The kit's own on-demand runner picks it up from that row with every sibling
# suite; run it ALONE, directly, wherever the siblings are held back, since the runner cannot run one.
#
# ONE ARM PER ACCEPTANCE CRITERION of the unit's spec, named by it:
#   AC1  a START and an END per call; `rc`, `checks` and `phase_to` from the driver and the file
#   AC2  every exit SHAPE ends `exit=clean` with its real status, a conf EXIT trap changes nothing,
#        and every `exit` in the driver and its library carries the clean-exit marker
#   AC3  TERM mid-`--close` ends `exit=unclean` without waiting for the bar; KILL leaves START alone
#   AC4  `oob=1` after an outside edit, and never on a first call
#   AC5  session values are shape-checked before they reach a line
#   AC6  `--version`, `--plan` and GOV_RUNLOG=0 write nothing
#   AC7  the writer adds no process to a call whose journal directory exists
#   AC8  a failed append changes neither rc nor stdout, and says so once on stderr
#   AC9  this suite's own declarations: withheld, budgeted, never a manifest leg
#   AC10 the protocol paragraph, the key row, the example line and the verbs sentence
#   AC11 a linked worktree writes the COMMON journal, not its own git dir
#   AC13 the unit field comes from the verb's own unit argument, free text never reaches a line, and
#        the writer's unit shape agrees with `_ids_of`'s grammar on a fixed probe set
#   CAP  a line over 2048 bytes is cut exactly as the runlog kit's `render_line` cuts it
# AC12 is `gotchas.py --for-paths` over the driver, a command of its own, and is not repeated here.
#
# WHAT THIS DOES NOT CHECK. Whether a line MEANS anything past the fields named here: the run model
# is a later unit. Wall time, except in AC3, where the verdict is "the stub is still alive after the
# driver died" and not a threshold. The pairing duty is asserted over the journal THIS suite writes,
# which is the population the runlog kit's README assigns to a producer's suite, and nothing wider.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
FLOOR_ASSERTIONS=163
SLUG=sLug
# Where the scratch clone installs the kit: a FIXTURE-INTERNAL path, bound once, never gov's prefix.
KR=tools/unattended
n=0; st=0

check() { # name · got · want
  n=$((n + 1))
  [ "$2" = "$3" ] && return 0
  echo "FAIL $1: expected [$3], got [$2]"; st=1; return 1
}

# ------------------------------------------------------------------------------ the scratch clone
# A MISSING CAPABILITY IS A FAILURE HERE, not a skip: the arms below are the only observation this
# unit's writer has, and a suite that skipped them would print a count that proves nothing.
PY=""
if [ -f "$HERE/../lib/resolve-python.sh" ]; then
  # shellcheck source=/dev/null
  . "$HERE/../lib/resolve-python.sh"
  PY=$(resolve_python 2>/dev/null) || PY=""
fi
RUNLOG_KIT="$HERE/../runlog"
[ -n "$PY" ] && [ -f "$RUNLOG_KIT/runlog_lib.py" ] || {
  echo "FAIL no python, or no runlog kit beside this one: the journal cannot be read, so nothing below can be graded"; exit 1; }
WORK=$(mktemp -d 2>/dev/null) || { echo "FAIL no mktemp -d on this host"; exit 1; }
STUB_PIDS=""
remove_scratch() {
  local p
  for p in $STUB_PIDS; do kill "$p" 2>/dev/null; done
  cd / && rm -rf "$WORK"
}
trap remove_scratch EXIT
REPO="$WORK/repo"
JOURNAL="$REPO/.git/runlog/driver.log"

# The journal reader, as the runlog kit's own library: the pairing duty is stated through
# `build_invocations`, and the cap rule through `render_line`. Written to a FILE, never fed on stdin.
cat > "$WORK/jl.py" <<'PY'
import sys
sys.path.insert(0, sys.argv[1])
import runlog_lib as r

mode, path = sys.argv[2], sys.argv[3]
if mode == "pairs":
    j = r.read_journal(path)
    states, mism = {}, 0
    for inv in r.build_invocations(j.lines):
        states[inv.state] = states.get(inv.state, 0) + 1
        if inv.state == "ended" and inv.start.fields.get("verb", "") != inv.end.fields.get("verb", ""):
            mism += 1
    print(f"bad={j.bad} ended={states.get('ended', 0)} open={states.get('killed-or-running', 0)} "
          f"orphan={states.get('orphan-end', 0)} mismatch={mism}")
    for why in j.refusals[:3]:
        print(f"  refusal {why}")
elif mode == "open-verbs":
    j = r.read_journal(path)
    print(" ".join(inv.start.fields.get("verb", "") for inv in r.build_invocations(j.lines)
                   if inv.state == "killed-or-running"))
elif mode == "render":
    # Every line carrying `key` is re-rendered by the REFERENCE writer with the value restored to the
    # uncut original, and must come back byte-identical. Prints `<ev> <bytes> SAME|DIFF`.
    key = sys.argv[4]
    full = open(sys.argv[5], "rb").read().decode("utf-8")
    for raw in open(path, "rb").read().decode("utf-8").split("\n"):
        if not raw or f"\t{key}=" not in raw:
            continue
        fields = {}
        for part in raw.split("\t"):
            k, _, v = part.partition("=")
            fields[k] = r._parse_value(v)
        fields[key] = full
        same = r.render_line(fields) == raw and r.check_line(raw) is None
        print(fields["ev"], len(raw.encode("utf-8")), "SAME" if same else "DIFF")
PY

build_sandbox() {
  mkdir -p "$WORK/nohooks"
  git init -q --bare "$WORK/origin.git" || return 1
  git --git-dir="$WORK/origin.git" symbolic-ref HEAD refs/heads/main
  git init -q "$REPO" || return 1
  cd "$REPO" || return 1
  # Hooks pointed at an EMPTY directory rather than bypassed per commit, and autocrlf OFF: the global
  # conf on a Windows node would check the driver out with CRLF in the linked worktree AC11 makes.
  git config user.email t@t; git config user.name t; git config commit.gpgsign false
  git config core.autocrlf false; git config core.hooksPath "$WORK/nohooks"
  git checkout -q -b main
  mkdir -p "$KR" "memory/builds/$SLUG/spec"
  cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" "$KR/"
  # THE CONF IS A FIXTURE WITH SWITCHES. Each arm that needs a hostile or a particular conf sets an
  # RLW_ variable for one call; the conf itself never changes, so no arm inherits another's.
  cat > .unattended.conf <<'CONF'
GATE_BOUND="3600"
GATE_CMD="${RLW_GATE_CMD:-true}"
RUNLOG_SESSION_VARS="${RLW_SESS_VARS:-}"
if [ -n "${RLW_CONF_TRAP:-}" ]; then trap 'exit 0' EXIT; fi
if [ -n "${RLW_CONF_TRAPFN:-}" ]; then trap() { :; }; fi
if [ -n "${RLW_CONF_OFF:-}" ]; then GOV_RUNLOG=0; fi
CONF
  { echo '---'; echo "slug: $SLUG"; echo 'streams: tooling'; echo '---'; echo; echo "# $SLUG"; echo
    echo '<!-- roster:units -->'; echo '| # | Unit |'; echo '|---|---|'; echo '| 1 | the unit |'
    echo '<!-- /roster:units -->'; echo; echo '<!-- gen:build-index -->'; echo '<!-- gen:build-units -->'
    echo '| Unit | Status | Rev | Last change |'; echo '|---|---|---|---|'
    echo "| [X-$SLUG-1 — the unit](spec/one.md) | SPECCED | rev-1 | 2026-09-13 |"
    echo '<!-- /gen:build-units -->'; echo '<!-- /gen:build-index -->'; } > "memory/builds/$SLUG/README.md"
  printf '# X-%s-1 the unit\n\n**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-1 · base 00000000 · streams tooling\n\n## 2. Scope\n\n- writes `work/one`.\n\n## 6. Acceptance criteria\n\n- AC1: `work/one` exists.\n\n## 7. Gates\n\n- the arm is silent.\n\n## 8. Open questions\n\nnone\n' \
    "$SLUG" > "memory/builds/$SLUG/spec/one.md"
  echo brief > brief.md
  git add -A >/dev/null && git commit -qm base || return 1
  BASE=$(git rev-parse HEAD)
  # The run-state file in the scaffold's shape. The writer reads one fact from it, `phase:`, and its
  # mtime; it is committed so the linked worktree of AC11 carries it too.
  printf '# %s - run state\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nwitness: %s\nphase: BUILDING\n\n## Parked\n' \
    "$SLUG" "$BASE" > "memory/builds/$SLUG/RUN.md"
  git add -A >/dev/null && git commit -qm run-state || return 1
  git remote add origin "$WORK/origin.git" && git push -q origin main 2>/dev/null
  return 0
}

run_driver() { # argv... -> OUT (stdout), ERR (stderr), RC; the driver runs from the scratch clone
  bash "$KR/unattended.sh" "$@" >"$WORK/out" 2>"$WORK/err"; RC=$?
  OUT=$(cat "$WORK/out"); ERR=$(cat "$WORK/err")
}

measure_lines() { # -> the journal's line count, 0 when it is absent
  if [ -f "$JOURNAL" ]; then wc -l < "$JOURNAL" | tr -d ' '; else echo 0; fi
}

read_field() { # line number · key -> the value, or the literal <absent>
  awk -F'\t' -v l="$1" -v k="$2" 'NR == l { for (i = 1; i <= NF; i++) if (index($i, k "=") == 1) { print substr($i, length(k) + 2); f = 1 } }
    END { if (!f) print "<absent>" }' "$JOURNAL"
}

check_pairs() { # label -> asserts the pairing duty over the whole journal
  local got; got=$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" pairs "$JOURNAL" | head -1)
  check "$1: no bad line" "$(printf '%s' "$got" | sed 's/.*bad=\([0-9]*\).*/\1/')" 0
  check "$1: no END without its START" "$(printf '%s' "$got" | sed 's/.*orphan=\([0-9]*\).*/\1/')" 0
  check "$1: every END's verb is its START's" "$(printf '%s' "$got" | sed 's/.*mismatch=\([0-9]*\).*/\1/')" 0
}

build_sandbox || { echo "FAIL the scratch clone could not be built"; exit 1; }

# ------------------------------------------------------------------------------------------ AC1
check_ac1_calls() {
  local l0 l
  l0=$(measure_lines)
  run_driver --park "$SLUG" --item q1 --reason r1
  check "AC1 --park succeeds" "$RC" 0
  run_driver --park "$SLUG" --bogus
  check "AC1 an unknown argument refuses" "$RC" 1
  run_driver --phase "$SLUG" VERIFYING --witness "$BASE"
  check "AC1 --phase succeeds" "$RC" 0
  run_driver --phase "$SLUG" NOTAPHASE --witness "$BASE"
  check "AC1 --phase outside the vocabulary refuses" "$RC" 1
  check "AC1 four calls, eight lines" "$(measure_lines)" "$((l0 + 8))"
  l=$((l0 + 2))
  check "AC1 --park END rc" "$(read_field $l rc)" 0
  check "AC1 --park END exit" "$(read_field $l exit)" clean
  check "AC1 --park END checks, empty when nothing refused" "$(read_field $l checks)" ""
  check "AC1 --park END phase_to" "$(read_field $l phase_to)" BUILDING
  l=$((l0 + 4))
  check "AC1 refused --park END rc" "$(read_field $l rc)" 1
  check "AC1 refused --park END checks" "$(read_field $l checks)" 14
  check "AC1 refused --park END exit" "$(read_field $l exit)" clean
  check "AC1 refused --park START verb" "$(read_field $((l - 1)) verb)" --park
  l=$((l0 + 6))
  check "AC1 --phase END verb, which the parse loop never assigns" "$(read_field $l verb)" --phase
  check "AC1 --phase START phase_from" "$(read_field $((l - 1)) phase_from)" BUILDING
  check "AC1 --phase END phase_to, read back from the file" "$(read_field $l phase_to)" VERIFYING
  check "AC1 --phase END rc" "$(read_field $l rc)" 0
  l=$((l0 + 8))
  # A refused phase move leaves the file where it was, and END reads the FILE: an rc-derived value
  # would name the phase that was asked for, or nothing.
  check "AC1 refused --phase END phase_to is the file's" "$(read_field $l phase_to)" VERIFYING
  check "AC1 refused --phase END checks" "$(read_field $l checks)" 19
  check "AC1 START and END share a nonce" "$(read_field $((l - 1)) n)" "$(read_field $l n)"
  # CALL ORDER, derived from the driver's own stdout rather than typed: a --close that refuses on
  # several items must list every check it printed, in the order it printed them.
  RLW_GATE_CMD=false run_driver --close "$SLUG"
  local want
  want=$(printf '%s\n' "$OUT" | sed -n 's/^UNATTENDED check \([0-9]*\) FAILED.*/\1/p' | paste -sd, -)
  l=$(measure_lines)
  check "AC1 a refusing --close printed more than one check" "$(printf '%s' "$want" | grep -c ,)" 1
  check "AC1 --close END checks, every refusal in call order" "$(read_field $l checks)" "$want"
  check "AC1 --close END rc" "$(read_field $l rc)" "$RC"
  check_pairs AC1
}

# ------------------------------------------------------------------------------------------ AC2
# THE EXIT-SITE ENUMERATION. A small lexer, because every cheaper predicate read something else:
# `exit` appears in awk programs, refusal messages and comments throughout the driver. It tracks
# single, double and ANSI-C quotes and skips comments and here-document bodies, then reports each
# `exit` word in command position as `<file> <line> <marked> <text>`. MARKED means the code before it
# on its line ends `RUNLOG_CLEAN=1;`, or it opens its line and the previous code line ends so.
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
          marked = (pre ~ /RUNLOG_CLEAN=1;$/) ? 1 : 0
          if (!marked && pre ~ /^[ \t]*(\{|then|else|do)?$/ && prevcode ~ /RUNLOG_CLEAN=1;?$/) marked = 1
          text = line; sub(/^[ \t]+/, "", text); sub(/[ \t]+$/, "", text)
          printf "%s\t%d\t%d\t%s\n", FILENAME, FNR, marked, text
          i += 4; continue
        }
        i++
      }
      if (pend != "") hd = pend
      t = line; sub(/[ \t]+$/, "", t)
      if (st == "N" && t != "" && t !~ /^[ \t]*#/) prevcode = t
    }' "$@"
}

# The exits that run BEFORE the trap exists, named by their TEXT: this unit's own insertions moved
# their line numbers, and a text that matches twice is a second exit nobody exempted. The sixth is
# the REVIEW_ROUNDS ceiling refusal main added before the install, found by this enumeration at the
# second origin/main reconcile (2026-09-16).
EXEMPT_EXITS='exit 2
ROOT="$(GIT rev-parse --show-toplevel 2>/dev/null)" || { echo "unattended: not a GIT repo"; exit 2; }
cd "$ROOT" || exit 2
echo "unattended: project-specific value from there and restates none of them."; exit 2; }
exit 2 ;;
[ "$REVIEW_ROUNDS" -lt "$RUNAWAY_CEILING" ] || { echo "unattended: REFUSING - REVIEW_ROUNDS is $REVIEW_ROUNDS, at or above the runaway ceiling of $RUNAWAY_CEILING, so the ceiling would fire first and the declared bound could never be reached." >&2; exit 2; }'

check_exit_rows() { # label · driver · library -> UNMARKED (unexempted unmarked rows), EXEMPTED count
  local label="$1" drv="$2" lib="$3" install rows row f ln mk tx ex cnt
  install=$(grep -n "builtin trap 'write_runlog_end" "$drv" | head -1 | cut -d: -f1)
  rows=$(scan_exit_sites "$drv" "$lib")
  UNMARKED=""; EXEMPTED=0
  while IFS= read -r row; do
    [ -n "$row" ] || continue
    IFS=$'\t' read -r f ln mk tx <<<"$row"
    [ "$mk" = 1 ] && continue
    ex=0
    if [ "$f" = "$drv" ] && [ -n "$install" ] && [ "$ln" -lt "$install" ]; then
      while IFS= read -r e; do [ "$tx" = "$e" ] && ex=1; done <<<"$EXEMPT_EXITS"
    fi
    if [ "$ex" = 1 ]; then EXEMPTED=$((EXEMPTED + 1)); else UNMARKED="$UNMARKED ${f##*/}:$ln"; fi
  done <<<"$rows"
  # Each exempt text matches EXACTLY one site, in the driver, above the install.
  EXEMPT_OK=1
  while IFS= read -r e; do
    cnt=$(printf '%s\n' "$rows" | awk -F'\t' -v e="$e" '$4 == e' | grep -c . || true)
    [ "$cnt" = 1 ] || EXEMPT_OK=0
  done <<<"$EXEMPT_EXITS"
  ALL_ROWS=$(printf '%s\n' "$rows" | grep -c . || true)
  INSTALL_LINE=$install
}

check_ac2_exits() {
  local l
  # Shape 1: the dispatch's closing `exit "$status"`, refused and succeeding.
  run_driver --park "$SLUG" --item q2 --reason r2 --waive h
  l=$(measure_lines)
  check "AC2 a waive refusal exits 1" "$RC" 1
  check "AC2 exit \"\$status\" END rc is the process status" "$(read_field $l rc)" "$RC"
  check "AC2 exit \"\$status\" END exit" "$(read_field $l exit)" clean
  check "AC2 the waive refusal is check 37" "$(read_field $l checks)" 37
  # Shape 2: the inline --phase exit, refused inside the loop before the verb runs.
  run_driver --phase "$SLUG" BUILDING --witness "$BASE" --waive h
  l=$(measure_lines)
  check "AC2 inline --phase refusal exits 1" "$RC" 1
  check "AC2 inline --phase END rc" "$(read_field $l rc)" 1
  check "AC2 inline --phase END exit" "$(read_field $l exit)" clean
  # Shape 3: the usage error, a call with no verb at all.
  run_driver --item orphaned
  l=$(measure_lines)
  check "AC2 no verb is a usage error" "$RC" 2
  check "AC2 usage END rc" "$(read_field $l rc)" 2
  check "AC2 usage END exit" "$(read_field $l exit)" clean
  check "AC2 usage START verb is empty, since argv 1 is a flag" "$(read_field $((l - 1)) verb)" ""
  check "AC2 usage START slug is empty, since argv 2 is a value" "$(read_field $((l - 1)) slug)" ""
  # A HOSTILE CONF: its EXIT trap is replaced, and a function named `trap` intercepts nothing.
  RLW_CONF_TRAP=1 run_driver --park "$SLUG" --bogus
  l=$(measure_lines)
  check "AC2 a conf EXIT trap does not change the status" "$RC" 1
  check "AC2 a conf EXIT trap does not remove END" "$(read_field $l ev)" end
  check "AC2 under a conf EXIT trap END rc" "$(read_field $l rc)" 1
  check "AC2 under a conf EXIT trap END exit" "$(read_field $l exit)" clean
  RLW_CONF_TRAPFN=1 run_driver --park "$SLUG" --bogus
  l=$(measure_lines)
  check "AC2 a conf function named trap does not remove END" "$(read_field $l ev)" end
  check "AC2 under a conf trap function END rc" "$(read_field $l rc)" 1
  # THE ENUMERATION over the real driver and library.
  check_exit_rows real "$HERE/unattended.sh" "$HERE/lib-unattended.sh"
  check "AC2 the install line is found" "$([ -n "$INSTALL_LINE" ] && echo found)" found
  check "AC2 every exit site carries the clean-exit marker or a named exemption" "${UNMARKED:-none}" none
  check "AC2 each exemption text matches exactly one site" "$EXEMPT_OK" 1
  check "AC2 all five exemptions were seen" "$EXEMPTED" 5
  check "AC2 the scan sees the post-install exits too" "$([ "$ALL_ROWS" -gt 5 ] && echo yes)" yes
  # THE ENUMERATION'S FAILING CASES, staged into COPIES every run: an unmarked exit inside a verb body
  # ABOVE the install, one in the library, and a marked one as the control. A checker only ever seen
  # passing is an assertion about nothing.
  awk '{ print } /^verb_park\(\) \{/ { print "  exit 3" }' "$HERE/unattended.sh" > "$WORK/mut.sh"
  cp "$HERE/lib-unattended.sh" "$WORK/mutlib.sh"
  check_exit_rows staged "$WORK/mut.sh" "$WORK/mutlib.sh"
  check "AC2 staged: an unmarked exit in a verb body is caught" "$(printf '%s' "$UNMARKED" | grep -c 'mut.sh:')" 1
  printf 'stray_exit() { exit 4; }\n' >> "$WORK/mutlib.sh"
  check_exit_rows staged "$HERE/unattended.sh" "$WORK/mutlib.sh"
  check "AC2 staged: an unmarked exit in the library is caught" "$(printf '%s' "$UNMARKED" | grep -c 'mutlib.sh:')" 1
  awk '{ print } /^verb_park\(\) \{/ { print "  RUNLOG_CLEAN=1; exit 3" }' "$HERE/unattended.sh" > "$WORK/mut.sh"
  check_exit_rows control "$WORK/mut.sh" "$HERE/lib-unattended.sh"
  check "AC2 control: a marked exit in a verb body passes" "${UNMARKED:-none}" none
  { cat "$HERE/unattended.sh"; printf 'exit 2\n'; } > "$WORK/mut.sh"
  check_exit_rows staged "$WORK/mut.sh" "$HERE/lib-unattended.sh"
  check "AC2 staged: a second copy of an exempt text is caught" "$EXEMPT_OK" 0
  check_pairs AC2
}

# ------------------------------------------------------------------------------------------ AC3
# THE SIGNAL IS SENT ONLY ONCE THE CHILD IS PROVABLY RUNNING. The stub writes its pid as its FIRST act
# and then becomes the sleep, so the poll below proves the driver is inside the bar before any signal
# is sent, and the pid it reads is the process to check is still alive. A fixed sleep instead would
# place the signal wherever the scheduler happened to be.
check_ac3_signals() {
  local ready="$WORK/ready" dp spid i l0 l verbs
  printf '#!/usr/bin/env bash\necho $$ > "%s.tmp" && mv "%s.tmp" "%s"\nexec sleep 20\n' "$ready" "$ready" "$ready" > "$WORK/stub.sh"
  for sig in TERM KILL; do
    rm -f "$ready"; l0=$(measure_lines)
    RLW_GATE_CMD="bash $WORK/stub.sh" bash "$KR/unattended.sh" --close "$SLUG" >"$WORK/out" 2>&1 &
    dp=$!
    i=0; while [ ! -s "$ready" ] && [ "$i" -lt 600 ]; do sleep 0.1; i=$((i + 1)); done
    spid=$(cat "$ready" 2>/dev/null); STUB_PIDS="$STUB_PIDS $spid"
    check "AC3 $sig: the stub reported ready" "$([ -n "$spid" ] && echo yes)" yes
    check "AC3 $sig: the stub is running when the signal is sent" "$(kill -0 "$spid" 2>/dev/null && echo alive)" alive
    kill "-$sig" "$dp" 2>/dev/null; wait "$dp" 2>/dev/null
    # The driver is gone and the bar it was waiting on is NOT: it did not wait for the child.
    check "AC3 $sig: the driver exited while the stub still ran" "$(kill -0 "$spid" 2>/dev/null && echo alive)" alive
    kill "$spid" 2>/dev/null
    l=$(measure_lines)
    if [ "$sig" = TERM ]; then
      check "AC3 TERM: START and END" "$((l - l0))" 2
      check "AC3 TERM: END reads unclean" "$(read_field $l exit)" unclean
      check "AC3 TERM: END verb" "$(read_field $l verb)" --close
    else
      check "AC3 KILL: START alone" "$((l - l0))" 1
      check "AC3 KILL: that line is the START" "$(read_field $l ev)" start
    fi
  done
  verbs=$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" open-verbs "$JOURNAL")
  check "AC3 exactly one call has no END, the killed --close" "$verbs" --close
  check_pairs AC3
}

# ------------------------------------------------------------------------------------------ AC4
check_ac4_outside_edit() {
  local s2=oobSlug runmd stamp l
  mkdir -p "memory/builds/$s2"
  printf '# %s\n\n## Run facts\nwitness: %s\nphase: BUILDING\n\n## Parked\n' "$s2" "$BASE" > "memory/builds/$s2/RUN.md"
  runmd="memory/builds/$s2/RUN.md"; stamp="$REPO/.git/runlog-stamp-$s2"
  check "AC4 no stamp before the first call" "$([ -e "$stamp" ] && echo present || echo none)" none
  run_driver --status "$s2"; l=$(measure_lines)
  check "AC4 a first call with no stamp carries no oob" "$(read_field $((l - 1)) oob)" "<absent>"
  check "AC4 END leaves a stamp" "$([ -e "$stamp" ] && echo present)" present
  run_driver --status "$s2"; l=$(measure_lines)
  check "AC4 an untouched file carries no oob" "$(read_field $((l - 1)) oob)" "<absent>"
  # A plain write. If this filesystem's clock is coarse enough that it lands on the stamp's own tick,
  # write again after a second rather than grade an equality as an edit nobody made.
  printf '\nan edit made by hand\n' >> "$runmd"
  [ "$runmd" -nt "$stamp" ] || { sleep 1; printf 'again\n' >> "$runmd"; }
  run_driver --status "$s2"; l=$(measure_lines)
  check "AC4 an outside edit sets oob" "$(read_field $((l - 1)) oob)" 1
  run_driver --status "$s2"; l=$(measure_lines)
  check "AC4 the stamp was refreshed, so the next call is clean" "$(read_field $((l - 1)) oob)" "<absent>"
  rm -rf "memory/builds/$s2"
}

# ------------------------------------------------------------------------------------------ AC5
check_ac5_session() {
  local l uuid=0f4c1a2e-9b7d-4c3e-8a1f-2d3e4f5a6b7c long
  long=$(printf 'a%.0s' $(seq 1 129))
  RLW_SESS_VARS="RLW_SA RLW_SB RLW_SC RLW_SA" RLW_SA=$uuid RLW_SB='a/b' run_driver --status "$SLUG"
  l=$(($(measure_lines) - 1))
  check "AC5 a UUID reaches the line" "$(read_field $l sess.RLW_SA)" "$uuid"
  check "AC5 a value holding / is written empty" "$(read_field $l sess.RLW_SB)" ""
  check "AC5 and flagged" "$(read_field $l sess_bad)" 1
  check "AC5 an unset variable writes no field" "$(read_field $l sess.RLW_SC)" "<absent>"
  check "AC5 no raw value reached the line" "$(sed -n "${l}p" "$JOURNAL" | grep -c 'a/b')" 0
  RLW_SESS_VARS="RLW_SA" RLW_SA=$long run_driver --status "$SLUG"
  l=$(($(measure_lines) - 1))
  check "AC5 a 129-character value is written empty" "$(read_field $l sess.RLW_SA)" ""
  check "AC5 and flagged" "$(read_field $l sess_bad)" 1
  RLW_SESS_VARS="RLW_SA 9bad" RLW_SA=ok run_driver --status "$SLUG"
  l=$(($(measure_lines) - 1))
  check "AC5 a name that is not an identifier is flagged" "$(read_field $l sess_bad)" 1
  check "AC5 a good name beside it still reads" "$(read_field $l sess.RLW_SA)" ok
  RLW_SESS_VARS="N1 N2 N3 N4 N5 N6 N7 N8 N9 N10" N1=1 N9=9 run_driver --status "$SLUG"
  l=$(($(measure_lines) - 1))
  check "AC5 eight names at most, the rest counted" "$(read_field $l sess_more)" 2
  check "AC5 the ninth name is not read" "$(read_field $l sess.N9)" "<absent>"
  check "AC5 the first name is read" "$(read_field $l sess.N1)" 1
  RLW_SESS_VARS="RLW_SA" RLW_SA=clean run_driver --status "$SLUG"
  l=$(($(measure_lines) - 1))
  check "AC5 a clean session carries no flag" "$(read_field $l sess_bad)" "<absent>"
  check_pairs AC5
}

# ------------------------------------------------------------------------------------------ AC6
check_ac6_unjournaled() {
  local l0
  l0=$(measure_lines)
  run_driver --version
  check "AC6 --version succeeds" "$RC" 0
  run_driver --plan "$SLUG"
  check "AC6 --version and --plan write nothing" "$(measure_lines)" "$l0"
  GOV_RUNLOG=0 run_driver --park "$SLUG" --item q6 --reason r6
  GOV_RUNLOG=0 run_driver --status "$SLUG"
  check "AC6 GOV_RUNLOG=0 writes nothing" "$(measure_lines)" "$l0"
  # The switch is the ENVIRONMENT's: a conf assigning it does not turn the log off.
  RLW_CONF_OFF=1 run_driver --status "$SLUG"
  check "AC6 a conf assigning GOV_RUNLOG=0 does not" "$(measure_lines)" "$((l0 + 2))"
}

# ------------------------------------------------------------------------------------------ AC7
# THE EXEC COUNT, from an xtrace on ITS OWN DESCRIPTOR: traced on stderr, every command inside a
# function called with `2>/dev/null` is invisible, and `GIT` is called that way throughout. A
# command word that is not an assignment, a builtin, a keyword or a function either file defines is
# an external exec.
measure_execs() { # trace file -> "<count> <sorted names>"
  local known w l c=0 names=""
  known=" $(compgen -b | tr '\n' ' ') $(compgen -k | tr '\n' ' ') "
  known="$known$(sed -n 's/^[[:space:]]*\([A-Za-z_][A-Za-z0-9_]*\)[[:space:]]*()[[:space:]]*{.*/\1/p' \
    "$KR/unattended.sh" "$KR/lib-unattended.sh" | tr '\n' ' ') "
  while IFS= read -r l; do
    case "$l" in +*) ;; *) continue ;; esac
    l=${l#"${l%%[!+]*}"}; l=${l# }; l=${l#* }
    w=${l%% *}; w=${w#\'}; w=${w%\'}
    case "$w" in ""|*=*|\(*) continue ;; esac
    case "$known" in *" $w "*) continue ;; esac
    c=$((c + 1)); names="$names$w"$'\n'
  done < "$1"
  printf '%s %s\n' "$c" "$(printf '%s' "$names" | sort | tr '\n' ' ')"
}

run_traced() { # trace file · argv... -> runs the driver under xtrace into the file
  local tf="$1"; shift
  PS4='+ ${EPOCHREALTIME} ' BASH_XTRACEFD=9 bash -x "$KR/unattended.sh" "$@" 9>"$tf" >/dev/null 2>&1
}

check_ac7_spawns() {
  local off on first extra
  [ -d "$REPO/.git/runlog" ] || mkdir "$REPO/.git/runlog"
  GOV_RUNLOG=0 run_traced "$WORK/t.off" --status "$SLUG"
  run_traced "$WORK/t.on" --status "$SLUG"
  off=$(measure_execs "$WORK/t.off"); on=$(measure_execs "$WORK/t.on")
  check "AC7 the probe sees execs at all" "$([ "${off%% *}" -gt 0 ] && echo yes)" yes
  check "AC7 the traced call with the writer on really wrote" "$(grep -c 'write_runlog_end' "$WORK/t.on" | awk '{print ($1 > 0)}')" 1
  check "AC7 the traced call with the writer off wrote nothing" "$(grep -c 'write_runlog_start' "$WORK/t.off")" 0
  check "AC7 the writer adds no external exec" "$on" "$off"
  # The one sanctioned spawn: a clone's FIRST call makes the journal directory, once.
  mv "$REPO/.git/runlog" "$WORK/runlog.keep"
  run_traced "$WORK/t.first" --status "$SLUG"
  first=$(measure_execs "$WORK/t.first")
  extra=$(comm -13 <(printf '%s\n' ${off#* } | sort) <(printf '%s\n' ${first#* } | sort) | tr '\n' ' ')
  check "AC7 a clone's first call pays exactly one mkdir" "$extra" "mkdir "
  check "AC7 and nothing else" "${first%% *}" "$(( ${off%% *} + 1 ))"
  cat "$REPO/.git/runlog/driver.log" >> "$WORK/runlog.keep/driver.log"
  rm -rf "$REPO/.git/runlog"; mv "$WORK/runlog.keep" "$REPO/.git/runlog"
  check_pairs AC7
}

# ------------------------------------------------------------------------------------------ AC8
check_ac8_write_failure() {
  local out_off rc_off err_off
  mv "$REPO/.git/runlog" "$WORK/runlog.keep"
  : > "$REPO/.git/runlog"
  GOV_RUNLOG=0 run_driver --status "$SLUG"; out_off=$OUT; rc_off=$RC; err_off=$ERR
  run_driver --status "$SLUG"
  check "AC8 a failed append leaves rc alone" "$RC" "$rc_off"
  check "AC8 a failed append leaves stdout alone" "$OUT" "$out_off"
  check "AC8 stderr carries ONE run-log line" "$(printf '%s\n' "$ERR" | grep -c '^unattended: run log')" 1
  check "AC8 and nothing else new" "$(printf '%s\n' "$ERR" | grep -v '^unattended: run log')" "$err_off"
  run_driver --park "$SLUG" --bogus
  check "AC8 a refused verb keeps its status too" "$RC" 1
  rm -f "$REPO/.git/runlog"; mv "$WORK/runlog.keep" "$REPO/.git/runlog"
}

# ------------------------------------------------------------------------------------------ AC9
check_ac9_declarations() {
  local budgets="$HERE/../run-gates/selftest-budgets.txt"
  check "AC9 no manifest leg runs a kit suite of this directory" \
    "$(grep -cE 'unattended/[A-Za-z-]+\.test\.sh' "$HERE/../gate-legs.json")" 0
  check "AC9 this suite is withheld by the kit's project-owned list" \
    "$(awk '/^\[\[files\]\]/ { inc = "" } /^include = \[/ { inc = $0 } /^role = "project-owned"/ && inc ~ /"runlog-writer\.test\.sh"/ { print "withheld" }' "$HERE/kit.toml")" withheld
  check "AC9 this suite has a budget row" \
    "$(awk -F'\t' '$3 ~ /runlog-writer\.test\.sh$/ && $2 ~ /^[0-9]+$/ { print "budgeted" }' "$budgets")" budgeted
}

# ----------------------------------------------------------------------------------------- AC10
check_ac10_carriers() {
  local proto="$HERE/PROTOCOL.template.md" verbs="$HERE/VERBS.template.md"
  check "AC10 the run-log paragraph opens a line in section 2" \
    "$(awk '/^## 2[.] /{f=1;next} f&&/^## /{f=0} f' "$proto" | grep -c '^\*\*The run log is not this file')" 1
  check "AC10 section 8 carries the key row" \
    "$(awk '/^## 8[.] /{f=1;next} f&&/^## /{f=0} f' "$proto" | grep -c '^| `RUNLOG_SESSION_VARS` |')" 1
  check "AC10 the example conf declares the key" "$(grep -c '^RUNLOG_SESSION_VARS=' "$HERE/.unattended.conf.example")" 1
  check "AC10 the verbs preamble carries the sentence" \
    "$(awk '/^- `--/{exit} {print}' "$verbs" | grep -c '^Every verb but `--version` and `--plan` also writes')" 1
}

# ----------------------------------------------------------------------------------------- AC11
check_ac11_worktree() {
  local wt="$WORK/wt2" l top gd
  git worktree add -q "$wt" -b side >/dev/null 2>&1
  (cd "$wt" && bash "$KR/unattended.sh" --status "$SLUG" >/dev/null 2>&1)
  l=$(measure_lines)
  top=$(git -C "$wt" rev-parse --show-toplevel)
  gd=$(git -C "$wt" rev-parse --path-format=absolute --git-dir)
  check "AC11 the linked worktree's line lands in the COMMON journal" "$(read_field $((l - 1)) wt)" "$top"
  check "AC11 its own git dir is under worktrees" "$(case "$gd" in */.git/worktrees/*) echo yes ;; esac)" yes
  check "AC11 nothing is journaled under the worktree's git dir" "$([ -e "$gd/runlog" ] && echo present || echo none)" none
  check "AC11 its out-of-band stamp is its own" "$([ -e "$gd/runlog-stamp-$SLUG" ] && echo present)" present
  run_driver --status "$SLUG"
  check "AC11 the primary tree writes the same file" "$(read_field $(measure_lines) ev)" end
  check "AC11 and names itself" "$(read_field $(($(measure_lines) - 1)) wt)" "$(git rev-parse --show-toplevel)"
  git worktree remove --force "$wt" >/dev/null 2>&1
  check_pairs AC11
}

# ----------------------------------------------------------------------------------------- AC13
check_ac13_units() {
  local l
  run_driver --brief "$SLUG" --unit "X-$SLUG-1" --path nofile
  check "AC13 --brief END unit" "$(read_field $(measure_lines) unit)" "X-$SLUG-1"
  run_driver --dispatch "$SLUG" --pass "X-$SLUG-1" --writes work/one
  check "AC13 --dispatch END unit" "$(read_field $(measure_lines) unit)" "X-$SLUG-1"
  run_driver --rescope "$SLUG" --act add --item "X-$SLUG-2" --reason r13
  check "AC13 --rescope END unit" "$(read_field $(measure_lines) unit)" "X-$SLUG-2"
  run_driver --review "$SLUG" --subject "X-$SLUG-1" --verdict CLEAN --blockers 0
  check "AC13 --review END unit" "$(read_field $(measure_lines) unit)" "X-$SLUG-1"
  run_driver --phase "$SLUG" BUILDING --witness "$BASE"
  check "AC13 --phase END slug" "$(read_field $(measure_lines) slug)" "$SLUG"
  check "AC13 --phase END carries no unit" "$(read_field $(measure_lines) unit)" "<absent>"
  run_driver --park "$SLUG" --item "free text X-$SLUG-9 sails here" --reason r13
  check "AC13 a free-text item reaches no line" "$(grep -c 'free text' "$JOURNAL")" 0
  check "AC13 --park END carries no unit" "$(read_field $(measure_lines) unit)" "<absent>"
  # ...and no FLAG either. The shape check alone would keep free text off the line even if PK_ITEM
  # were read for --park, so the only sign of that read is a flag on a verb that has no unit to judge.
  check "AC13 --park END judged no unit at all" "$(read_field $(measure_lines) unit_bad)" "<absent>"
  run_driver --brief "$SLUG" --unit "not a unit" --path nofile
  l=$(measure_lines)
  check "AC13 a value that is not unit-shaped is flagged" "$(read_field $l unit_bad)" 1
  check "AC13 and not written" "$(read_field $l unit)" "<absent>"
  run_driver --dispatch "$SLUG" --pass "X-$SLUG-1-2" --writes work/one
  check "AC13 a unit with a dash too many is flagged" "$(read_field $(measure_lines) unit_bad)" 1
  # ONE GRAMMAR, TWO SPELLINGS, JOINED HERE. The writer tests the unit shape in pure bash because
  # `_ids_of` forks a grep, and a second spelling of one grammar drifts unless something compares
  # them. The ERE is read from `_ids_of`'s own line, and each probe must get the same verdict from it
  # as from the writer. A missing ERE is a failure, never a skip.
  local ere probe want got
  ere=$(sed -n "s/^_ids_of() { grep -oE '\\([^']*\\)'.*/\\1/p" "$KR/unattended.sh")
  check "AC13 the unit-id grammar is read from _ids_of" "$([ -n "$ere" ] && echo read)" read
  for probe in TOOL-dLoggedFlight-2 X-a1-7 x-Lower-1 TOOL-a-b-2 TOOL--2 TOOL-a-2x "TOOL-é-1" -a-1; do
    want=$(printf '%s\n' "$probe" | grep -cxE "$ere")
    run_driver --brief "$SLUG" --unit "$probe" --path nofile
    got=0; [ "$(read_field $(measure_lines) unit)" = "$probe" ] && got=1
    check "AC13 the writer and _ids_of agree on [$probe]" "$got" "$want"
  done
  check_pairs AC13
}

# ------------------------------------------------------------------------------------------ CAP
# A value longer than the line cap, three ways: plain ASCII, and a three-byte character with a one- and
# a two-byte prefix, so at least one cut lands INSIDE a character. Each line is re-rendered by the
# runlog kit's reference writer from the uncut value and must come back byte-identical.
check_cap_fit() {
  local runmd="memory/builds/$SLUG/RUN.md" keep="$WORK/run.keep" val res pre short=0
  cp "$runmd" "$keep"
  for pre in ascii "" a ab; do
    if [ "$pre" = ascii ]; then val=$(printf 'X%.0s' $(seq 1 2500))
    else val="$pre$(printf '€%.0s' $(seq 1 900))"; fi
    printf '# s\n\n## Run facts\nwitness: %s\nphase: %s\n\n## Parked\n' "$BASE" "$val" > "$runmd"
    printf '%s' "$val" > "$WORK/full"
    : > "$WORK/one.log"
    run_driver --status "$SLUG"
    tail -2 "$JOURNAL" > "$WORK/one.log"
    res=$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" render "$WORK/one.log" phase_from "$WORK/full")
    check "CAP [$pre] START is cut as render_line cuts it" "${res##* }" SAME
    case "$res" in *" 2048 "*) ;; *) short=$((short + 1)) ;; esac
    res=$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" render "$WORK/one.log" phase_to "$WORK/full")
    check "CAP [$pre] END is cut as render_line cuts it" "${res##* }" SAME
  done
  check "CAP a cut landed inside a character at least once" "$([ "$short" -gt 0 ] && echo yes)" yes
  cp "$keep" "$runmd"
  check_pairs CAP
}

check_ac1_calls
check_ac2_exits
check_ac3_signals
check_ac4_outside_edit
check_ac5_session
check_ac6_unjournaled
check_ac7_spawns
check_ac8_write_failure
check_ac9_declarations
check_ac10_carriers
check_ac11_worktree
check_ac13_units
check_cap_fit

if [ "$n" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "FAIL $n assertions ran, under the floor of $FLOOR_ASSERTIONS: an arm stopped asserting"; st=1
fi
if [ "$st" = 0 ]; then echo "PASS ($n assertions)"; else echo "FAILED ($n assertions)"; fi
exit "$st"
