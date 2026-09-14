#!/usr/bin/env bash
# Runnable check for scratch-guard.js — the PreToolUse guard that keeps agent scratch out of the
# home directory. Run: bash tools/hooks/scratch-guard.test.sh   (exit 0 = all pass)
#
# WHAT THIS FILE DOES NOT CHECK, stated up front because a structural check reads as a semantic one
# to everybody who did not write it: it does not prove the hook is WIRED. That is check-wiring.sh's
# `scratch-guard` arm. It also does not prove the predicate is complete over real usage — that is the
# corpus probe recorded in this build's record, which ran it over 93,208 historical Bash tool calls.
#
# EVERY ARM DRIVES ITS OWN HOME AND TEMP. The hook resolves both from the environment, so an arm that
# inherited the operator's would measure a different thing on every node and pass green on the ones
# where it stopped matching. `memory/gotchas/fixture-inherits-ambient-machine-state.md` names exactly
# this. The fixture home is deliberately a name no machine has, in two spellings, so the 8.3
# cross-substitution is exercised rather than assumed.
KIT_REL="${KIT_REL:-tools/hooks}"
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
HOOK="$HERE/scratch-guard.js"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0

if [ -f "$HERE/../lib/resolve-python.sh" ]; then
  . "$HERE/../lib/resolve-python.sh"
  TESTPY=$(resolve_python) || { echo "scratch-guard.test: no usable python"; exit 2; }
else
  TESTPY=python3   # gov:literal-python — last-resort fallback when ../lib/ is absent (adopter layout)
fi

FIX_HOME='/c/Users/fixtureuser'
FIX_PROFILE='C:\Users\fixtureuser'
FIX_TEMP='C:\Users\FIXTUR~1\AppData\Local\Temp'

# run <name> <expected_exit> <command-text> [tool] [pre] — the payload is BUILT, never hand-spliced;
# an unescaped backslash in a Windows path is the top JSON breaker and every arm here carries one.
#
# THE FIFTH ARGUMENT IS JAVASCRIPT ON process.env, NEVER `env` WORDS. An arm that needs TEMP=/tmp,
# or TEMP unset, cannot hand that through the shell on a Git-Bash host: the MSYS runtime rewrites a
# POSIX-shaped value for native node.exe (`TEMP=/tmp node -e ...` prints the TEMP path, measured
# 2026-09-14 on node `a`, and MSYS2_ENV_CONV_EXCL does not stop it), and GNU `env` refuses `-u` after
# an assignment. So the prelude runs INSIDE node, where MSYS cannot reach, and the hook runs as that
# node's child with stdin, stdout and stderr inherited — main(), the stdin parse and renderDeny all
# run, and every sentence assertion below still reads the hook's own stderr. `?? 1` because
# process.exit(null) exits 0 on node 22, and a signal-killed hook must not read as an allow.
run() {
  local name=$1 want=$2 cmd=$3 tool=${4:-Bash} pre=${5:-}
  local payload got
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":sys.argv[1],"tool_input":{"command":sys.argv[2]}}))' "$tool" "$cmd")
  # THE LIVENESS GUARD. The hook exits 0 on unparseable stdin by design, so a builder that produced
  # nothing makes every ALLOW arm pass for the wrong reason. A fixture that produced nothing is a
  # failure, not a silent green. Its own failing case is exercised by the meta-arm at the bottom.
  case "$payload" in *'"command"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  printf '%s' "$payload" \
    | HOME="$FIX_HOME" USERPROFILE="$FIX_PROFILE" TEMP="$FIX_TEMP" TMP="$FIX_TEMP" TMPDIR= \
      node -e "$pre;const r=require('child_process').spawnSync(process.execPath,[process.argv[1]],{stdio:'inherit'});process.exit(r.status??1)" "$HOOK" >/dev/null 2>"$TMP/err"
  got=$?
  if [ "$got" = "$want" ]; then echo "ok   $name (exit $got)"; pass=$((pass+1))
  else echo "FAIL $name (exit $got, want $want)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}

# ---- fail-open: the hook must never be the reason a good command dies -----------------------------
raw() { # name expected_exit payload
  printf '%s' "$3" | HOME="$FIX_HOME" USERPROFILE="$FIX_PROFILE" TEMP="$FIX_TEMP" TMP="$FIX_TEMP" \
    node "$HOOK" >/dev/null 2>&1
  local got=$?
  if [ "$got" = "$2" ]; then echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $got, want $2)"; fail=$((fail+1)); fi
}
raw "empty stdin -> allow"            0 ''
raw "non-JSON stdin -> allow"         0 'not json at all'
raw "JSON null -> allow"              0 'null'
raw "no tool_name -> allow"           0 '{"tool_input":{"command":"echo x > ~/.litter"}}'
raw "unrelated tool -> allow"         0 '{"tool_name":"Read","tool_input":{"command":"echo x > ~/.litter"}}'
raw "no command key -> allow"         0 '{"tool_name":"Bash","tool_input":{}}'

# ---- every home-root spelling DENIES, each with an ALLOW near-miss --------------------------------
# One arm per spelling is the point: the predicate claims seven and a hook recognising only `~/`
# would pass a suite that tested only `~/`. The near-miss beside each one stops the arm being
# satisfied by a hook that denies everything.
run "tilde home write -> deny"                    2 'echo x > ~/.litter'
run "  near-miss: repo-relative write -> allow"   0 'echo x > memory/notes.md'
run "\$HOME home write -> deny"                   2 'echo x > $HOME/.litter'
run "  near-miss: \$PWD write -> allow"           0 'echo x > $PWD/notes.md'
run "\${HOME} home write -> deny"                 2 'echo x > ${HOME}/.litter'
run "  near-miss: \${PWD} write -> allow"         0 'echo x > ${PWD}/notes.md'
run "msys absolute home write -> deny"            2 'echo x > /c/Users/fixtureuser/.litter'
run "  near-miss: msys other user -> allow"       0 'echo x > /c/Users/someoneelse/.litter'
run "windows fwd-slash home write -> deny"        2 'echo x > C:/Users/fixtureuser/.litter'
run "  near-miss: another drive -> allow"         0 'echo x > D:/Users/fixtureuser/.litter'
run "windows backslash home write -> deny"        2 'echo x > C:\Users\fixtureuser\.litter'
run "  near-miss: backslash other root -> allow"  0 'echo x > C:\ProgramData\thing.log'
run "8.3 contracted home write -> deny"           2 'echo x > C:/Users/FIXTUR~1/.litter'
run "  near-miss: 8.3 under TEMP -> allow"        0 'echo x > C:/Users/FIXTUR~1/AppData/Local/Temp/a.log'

# ---- every write-context family DENIES, each with an ALLOW near-miss ------------------------------
run "redirect > -> deny"                          2 'echo x > ~/.a'
run "append >> -> deny"                           2 'echo x >> ~/.a'
run "stderr 2> -> deny"                           2 'cmd 2> ~/.a'
run "both &> -> deny"                             2 'cmd &> ~/.a'
run "the observed litter shape -> deny"           2 'bash tools/run-gates/run-gates.sh > ~/.merge-bar.log 2>&1'
run "  near-miss: redirect to /dev/null -> allow" 0 'cmd > /dev/null 2>&1'
run "tee -> deny"                                 2 'echo x | tee ~/.a'
run "touch -> deny"                               2 'touch ~/.a'
run "mkdir -> deny"                               2 'mkdir -p ~/.gov-push'
run "  near-miss: mkdir in repo -> allow"         0 'mkdir -p memory/builds/x'
run "cp destination -> deny"                      2 'cp memory/x.md ~/.backup.md'
run "cp home-rooted SOURCE -> allow"              0 'cp ~/.merge-bar.log memory/inv/'
run "mv destination -> deny"                      2 'mv memory/x.md ~/.backup.md'
run "mv home-rooted SOURCE -> allow"              0 'mv ~/.merge-bar.log memory/inv/'
run "rsync destination -> deny"                   2 'rsync -a memory/ ~/.mirror/'

# ---- the DRIVE-ROOT rule. The home rule above was scoped to home, so everything outside it was
# ---- unguarded: an agent fixture wrote 7.2 MB to C:/gvi, outside repo, scratchpad and guard.
# ---- Measured over 128,568 real tool calls: this predicate hits 16, all of them agent litter,
# ---- while the obvious wider one hits 2,449 and is almost all legitimate /tmp use.
run "drive-root mkdir -> deny"                    2 'mkdir -p /c/gvi'
run "drive-root redirect -> deny"                 2 'echo x > /c/temp-hyg.txt'
run "drive-root windows spelling -> deny"         2 'mkdir C:/gvi'
run "drive-root cp DESTINATION -> deny"           2 'cp memory/x.md /c/scratch/inv/'
run "/tmp write -> deny (the 2026-09-14 ruling)"  2 'echo x > /tmp/hyg.txt'
run "  near-miss: under the fixture TEMP -> allow" 0 'echo x > C:/Users/FIXTUR~1/AppData/Local/Temp/hyg.txt'
run "  near-miss: under a project -> allow"       0 'echo x > /c/projects/incms/f.txt'
run "  near-miss: windows dir -> allow"           0 'echo x > /c/Windows/Temp/f.txt'
run "  near-miss: /dev/null -> allow"             0 'echo hi > /dev/null'
run "TMPDIR= to home -> deny"                     2 'export TMPDIR=~/.gov-push'
run "TMP= to home -> deny"                        2 'TMP=~/.scratch bash x.sh'
run "  near-miss: TMPDIR= to TEMP -> allow"       0 'export TMPDIR=C:/Users/FIXTUR~1/AppData/Local/Temp/gatetmp'

# ---- the allowlist, including the boundary that a naive prefix test gets wrong --------------------
run "~/.claude write -> allow"                    0 'echo x > ~/.claude/settings.json'
run "~/.claudex write -> deny"                    2 'echo x > ~/.claudex/y'
run "~/.claude-scratch write -> deny"             2 'echo x > ~/.claude-scratch/y'
run "TEMP write, 8.3 spelling -> allow"           0 'echo x > C:/Users/FIXTUR~1/AppData/Local/Temp/a.log'
# THE CROSS-SPELLING ARM. The machine hands %TEMP% 8.3-contracted while commands write it long. The
# corpus probe produced 259 false positives before the hook re-spelled its roots under every known
# home form; this arm is that finding, pinned.
run "TEMP write, LONG spelling -> allow"          0 'echo x > C:/Users/fixtureuser/AppData/Local/Temp/a.log'
run "TEMP write, msys spelling -> allow"          0 'echo x > /c/Users/fixtureuser/AppData/Local/Temp/a.log'
run "scratchpad under TEMP -> allow"              0 'cat > /c/Users/fixtureuser/AppData/Local/Temp/claude/x/s.md'
run "sibling of TEMP -> deny"                     2 'echo x > /c/Users/fixtureuser/AppData/Local/Tempest/a.log'

# ---- the three rules TOOL-aProbedUnit-5 added: an EMPTY temp variable, /tmp, and POSIX-root litter.
# ---- Every denial below exited 0 against the hook at base 1b000d1a, measured 2026-09-14 on node
# ---- `a`; the controls exit 0 at base and at the tip. Adjacent rules are told apart by the KIND
# ---- SENTENCE in stderr, never by exit status — every denial exits 2 — so a boundary arm asserts
# ---- the sentence it expects AND the absence of its neighbour's.
PRE_TMP='process.env.TEMP="/tmp";process.env.TMP="/tmp";delete process.env.TMPDIR'
PRE_NONE='delete process.env.TMPDIR;delete process.env.TMP;delete process.env.TEMP'
SENT_TMP='/tmp is not a sanctioned destination'
SENT_POSIX='POSIX_ROOT_CONVENTIONAL'

# rule 1, `empty-var`: `cp x $TMPDIR/y` with TMPDIR empty lands at `/y`. The fixture prefix already
# pins TMPDIR empty and TEMP set; the allow half needs TMPDIR NON-empty, which only the prelude can do.
run "\$TMPDIR EMPTY -> deny (the write lands at /)" 2 'cp x $TMPDIR/y'
case "$(cat "$TMP/err")" in
  *'$TMPDIR is EMPTY'*'lands at the filesystem root'*) echo "ok   the empty-var deny names \$TMPDIR and says where the bytes land"; pass=$((pass+1)) ;;
  *) echo "FAIL the empty-var deny does not name the variable, or does not say the write lands at the root"; fail=$((fail+1)) ;;
esac
case "$(cat "$TMP/err")" in
  *"BLOCKED by scratch-guard"*'$TMPDIR/y'*"appdata/local/temp"*) echo "ok   the empty-var deny keeps the BLOCKED prefix, the target and a resolved root"; pass=$((pass+1)) ;;
  *) echo "FAIL the empty-var deny dropped the shared prefix, the target or the roots list"; fail=$((fail+1)) ;;
esac
run "  \$TMPDIR set through the prelude -> allow"  0 'cp x $TMPDIR/y' Bash 'process.env.TMPDIR="C:/Users/FIXTUR~1/AppData/Local/Temp"'
run "\${TEMP} UNSET -> deny"                      2 'echo x > ${TEMP}/y' Bash 'delete process.env.TEMP'
case "$(cat "$TMP/err")" in
  *'$TEMP is EMPTY'*) echo "ok   the braced spelling is matched and the deny names \$TEMP"; pass=$((pass+1)) ;;
  *) echo "FAIL the \${TEMP} deny does not name TEMP"; fail=$((fail+1)) ;;
esac
run "  \$TEMP set -> allow (expands under the TEMP root)" 0 'echo x > $TEMP/a.log'
run "  same-command TMP= assignment -> allow"    0 'TMP=$(mktemp -d); echo x > $TMP/f' Bash 'delete process.env.TMP'
run "\${TMPDIR:-/tmp} default expands -> deny (tmp)" 2 'echo x > ${TMPDIR:-/tmp}/y'
case "$(cat "$TMP/err")" in
  *"$SENT_TMP"*) echo "ok   the expanded default reached the tmp rule"; pass=$((pass+1)) ;;
  *) echo "FAIL the default form was denied by some rule other than tmp, or not expanded"; fail=$((fail+1)) ;;
esac

# rule 2, `tmp`: denied by the 2026-09-14 ruling even on a Git-Bash host where /tmp maps onto TEMP.
run "/tmp/hyg -> deny (tmp)"                      2 'echo x > /tmp/hyg'
case "$(cat "$TMP/err")" in
  *"BLOCKED by scratch-guard"*'/tmp/hyg'*"appdata/local/temp"*"$SENT_TMP"*) echo "ok   the tmp deny names the scratchpad and keeps the prefix, the target and a root"; pass=$((pass+1)) ;;
  *) echo "FAIL the tmp deny is missing its sentence, the prefix, the target or the roots list"; fail=$((fail+1)) ;;
esac
# THE /tmp BOUNDARY. `/tmpx` is four characters, absent from POSIX_ROOT_CONVENTIONAL and not `/tmp`:
# rule 3 claims it whatever rule 2 does, so an exit-0 control here would be red at a correct tip.
run "/tmpx/hyg -> deny (posix-root, NOT tmp)"     2 'echo x > /tmpx/hyg'
case "$(cat "$TMP/err")" in
  *"$SENT_TMP"*) echo "FAIL a bare startsWith('/tmp') gave /tmpx the tmp sentence"; fail=$((fail+1)) ;;
  *"$SENT_POSIX"*) echo "ok   /tmpx carries the posix-root sentence and not the tmp one"; pass=$((pass+1)) ;;
  *) echo "FAIL /tmpx was denied with neither the tmp nor the posix-root sentence"; fail=$((fail+1)) ;;
esac
# The exception is keyed on os.tmpdir(), not on the literal: under the fixture TEMP the derived
# tmpdir is NOT /tmp, so /tmp/claude is just another /tmp write.
run "/tmp/claude/x under the fixture env -> deny" 2 'echo x > /tmp/claude/x'
case "$(cat "$TMP/err")" in
  *"$SENT_TMP"*) echo "ok   /tmp/claude is denied when os.tmpdir() is not /tmp"; pass=$((pass+1)) ;;
  *) echo "FAIL /tmp/claude was denied for a reason other than tmp"; fail=$((fail+1)) ;;
esac

# rule 2's exception, `<os.tmpdir()>/claude`, DERIVED under the emptied environment rather than pinned.
# On a POSIX host that derives /tmp and proves the new root; on a Windows node it derives
# C:\Windows\temp, under a conventional drive root, and this arm is a CONTROL that says so.
sg_derived=$(node -e "$PRE_NONE;console.log(require('os').tmpdir())")
run "<os.tmpdir()>/claude under the emptied env -> allow (a proof only where that derives /tmp; a control under a conventional drive root, as on every Windows node)" 0 "echo x > $sg_derived/claude/x" Bash "$PRE_NONE"
# THE DISCRIMINATING PAIR, and the one half of this rule that can fail on every registered node.
# With TEMP=/tmp and TMP=/tmp handed INSIDE node, os.tmpdir() derives /tmp on Windows and POSIX
# alike, the new root is /tmp/claude, and no other root covers /tmp because a /tmp-valued variable
# contributes none. The LIVENESS assertion first: a runtime that rewrites the value reports itself
# by name instead of a deny for the wrong reason. Its red is the shell-prefix form, which prints TEMP.
sg_probe=$(node -e "$PRE_TMP;console.log(require('os').tmpdir())")
case "$sg_probe" in
  /tmp)
    echo "ok   the prelude reaches the hook: os.tmpdir() derives /tmp inside node"; pass=$((pass+1))
    run "os.tmpdir()=/tmp: /tmp/claude/x -> allow (the scratch base inside the denied prefix)" 0 'echo x > /tmp/claude/x' Bash "$PRE_TMP"
    run "os.tmpdir()=/tmp: /tmp/other -> deny (a /tmp-valued TEMP joins no root)" 2 'echo x > /tmp/other' Bash "$PRE_TMP"
    case "$(cat "$TMP/err")" in
      *"$SENT_TMP"*) echo "ok   /tmp/other under TEMP=/tmp carries the tmp sentence"; pass=$((pass+1)) ;;
      *) echo "FAIL /tmp/other under TEMP=/tmp was denied for a reason other than tmp"; fail=$((fail+1)) ;;
    esac
    # THE EXPANSION ARM. Every other set temp variable in this suite is itself an allowed root, so
    # `$TEMP/a.log` is allowed whether or not the variable expands, and the expansion branch of
    # `buildResolvedTarget` had no arm that could red it: dropping `env[t[1]] ||` from it left the
    # suite green (closing diff review round 1, cluster K). Here TEMP is the one value that is NOT
    # a root, so `$TEMP/other` is denied by the tmp rule only if the variable expanded to /tmp —
    # unexpanded it is an unresolved token that no rule claims, and the arm reads exit 0.
    run "TEMP=/tmp: \$TEMP/other expands and is denied (tmp)" 2 'echo x > $TEMP/other' Bash "$PRE_TMP"
    case "$(cat "$TMP/err")" in
      *"$SENT_TMP"*) echo "ok   \$TEMP/other under TEMP=/tmp expanded and carries the tmp sentence"; pass=$((pass+1)) ;;
      *) echo "FAIL \$TEMP/other under TEMP=/tmp was denied for a reason other than tmp, or not expanded"; fail=$((fail+1)) ;;
    esac ;;
  *) echo "FAIL the prelude did not reach the hook: os.tmpdir() derived '$sg_probe', not /tmp, so the discriminating pair grades nothing"; fail=$((fail+1)) ;;
esac

# rule 3, `posix-root`: a new top-level entry at the POSIX root, the drive rule's shape without a
# drive letter. Four targets in 55,231 real Bash calls, every one agent throwaway.
run "posix-root mkdir -> deny"                    2 'mkdir -p /mir/x'
case "$(cat "$TMP/err")" in
  *"BLOCKED by scratch-guard"*'/mir/x'*"appdata/local/temp"*"$SENT_POSIX"*) echo "ok   the posix-root deny names its set and keeps the prefix, the target and a root"; pass=$((pass+1)) ;;
  *) echo "FAIL the posix-root deny is missing its sentence, the prefix, the target or the roots list"; fail=$((fail+1)) ;;
esac
run "  near-miss: /dev/null -> allow"             0 'echo x > /dev/null'
run "  near-miss: /c/projects/x is the drive rule's -> allow" 0 'echo x > /c/projects/x'
run "  near-miss: /usr/local/x is conventional -> allow" 0 'mkdir -p /usr/local/x'
# The macOS near-miss: `/Users` is where every macOS home lives, and the set held `private` and
# `volumes` without it, so this write was denied as new top-level litter on every macOS host
# (closing diff review round 1, cluster J). Red against the hook before `users` joined the set.
run "  near-miss: /Users/Shared/f is a macOS root -> allow" 0 'echo x > /Users/Shared/f'

# ---- the two views: a quoted operator is invisible, a quoted target still resolves ----------------
# Without the blanking, the guard denies the commit message describing it — including this build's.
run "shape quoted in a commit message -> allow"   0 'git commit -m "fixes the > ~/.merge-bar.log litter"'
run "shape in a single-quoted arg -> allow"       0 "grep -n '> ~/.merge-bar.log' memory/notes.md"
run "quoted redirect TARGET -> deny"              2 'echo x > "$HOME/.merge-bar.log"'
run "quoted arg AND a real redirect -> deny"      2 'git commit -m "about > ~/.x" > ~/.out.log'
run "heredoc body quoting the shape -> allow"     0 'cat > memory/x.md <<EOF
see > ~/.merge-bar.log
EOF'
run "empty heredoc body -> allow"                 0 'cat > memory/x.md <<EOF
EOF'

# ---- PowerShell is the same act through the other shell ------------------------------------------
run "PowerShell redirect to home -> deny"         2 'Set-Content ~/.litter "x"' PowerShell
run "PowerShell TEMP write -> allow"              0 'Set-Content C:/Users/FIXTUR~1/AppData/Local/Temp/a.log "x"' PowerShell
run "PowerShell out-of-scope tool name -> allow"  0 'echo x > ~/.litter' Zsh

# ---- the degraded branch the header promises -----------------------------------------------------
# With no home resolvable the hook keeps the symbolic roots and says so in its header. Nothing else
# tests the branch, so it would rot into a comment.
degraded() { # name expected_exit command
  local payload got
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Bash","tool_input":{"command":sys.argv[1]}}))' "$3")
  printf '%s' "$payload" | env -u HOME -u USERPROFILE -u TEMP -u TMP -u TMPDIR node "$HOOK" >/dev/null 2>&1
  got=$?
  if [ "$got" = "$2" ]; then echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $got, want $2)"; fail=$((fail+1)); fi
}
degraded "no home resolvable: ~/ still denies"    2 'echo x > ~/.litter'
degraded "no home resolvable: repo path allows"   0 'echo x > memory/notes.md'

# ---- the deny message must be satisfiable ---------------------------------------------------------
msg=$("$TESTPY" -c 'import json; print(json.dumps({"tool_name":"Bash","tool_input":{"command":"echo x > ~/.litter"}}))' \
  | HOME="$FIX_HOME" USERPROFILE="$FIX_PROFILE" TEMP="$FIX_TEMP" TMP="$FIX_TEMP" node "$HOOK" 2>&1 >/dev/null)
case "$msg" in
  *"BLOCKED by scratch-guard"*) echo "ok   the deny carries the BLOCKED prefix"; pass=$((pass+1)) ;;
  *) echo "FAIL the deny is missing its BLOCKED prefix"; fail=$((fail+1)) ;;
esac
case "$msg" in
  *"appdata/local/temp"*) echo "ok   the deny NAMES a resolved writable root"; pass=$((pass+1)) ;;
  *) echo "FAIL the deny does not name a writable root, so it is not satisfiable"; fail=$((fail+1)) ;;
esac
case "$msg" in
  *'~/.litter'*) echo "ok   the deny quotes the offending target"; pass=$((pass+1)) ;;
  *) echo "FAIL the deny does not quote the offending target"; fail=$((fail+1)) ;;
esac

# ---- kit-versus-wired parity ---------------------------------------------------------------------
# `.claude/**` is outside the govkit surface, outside the codebase-map inventories and outside both
# tools/-scoped JS gates, so nothing else in the bar notices the EXECUTED copy drifting from the
# graded one. Absence must not satisfy it.
ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null || echo "")
# SELF-ARMING ON THE RESOLVED COPY COUNT — TOOL-dRetiredFork-14.
# This arm asserted TWO copies and hard-FAILED when the second was absent. That became the CORRECT
# state the moment the kit stopped shipping a second destination, so the arm failed on the shipped
# layout: not a parity check any more, just a stale assumption with a test around it.
#
# It now grades the population it actually finds:
#   0 copies  -> REFUSE. A parity arm with no subject proves nothing, and saying "skip" there is the
#                green-by-absence shape this repo has a catalogue entry for.
#   1 copy    -> the single-copy layout. There is nothing to drift FROM, and that is a pass.
#   2 or more -> the historical dual-ship. Every extra copy must match the kit copy byte for byte.
if [ -n "$ROOT" ] && [ -f "$ROOT/$KIT_REL/scratch-guard.js" ]; then
  sg_extra=""
  for sg_c in "$ROOT/.claude/hooks/scratch-guard.js"; do
    [ -f "$sg_c" ] && sg_extra="$sg_extra $sg_c"
  done
  sg_n=$(printf '%s' "$sg_extra" | wc -w | tr -d ' ')
  if [ "$sg_n" = 0 ]; then
    echo "ok   single-copy layout: $KIT_REL/scratch-guard.js is the only tracked copy, so there is nothing to drift from"
    pass=$((pass+1))
  else
    sg_drift=0
    for sg_c in $sg_extra; do
      if ! diff -q <(sed 's/\r$//' "$sg_c") <(sed 's/\r$//' "$ROOT/$KIT_REL/scratch-guard.js") >/dev/null; then
        echo "FAIL ${sg_c#"$ROOT/"} has drifted from $KIT_REL/scratch-guard.js"
        echo "     fix: cp $KIT_REL/scratch-guard.js ${sg_c#"$ROOT/"}"
        sg_drift=1
      fi
    done
    if [ "$sg_drift" = 0 ]; then
      echo "ok   all $((sg_n+1)) tracked copies of scratch-guard.js agree"; pass=$((pass+1))
    else
      fail=$((fail+1))
    fi
  fi
else
  echo "FAIL the parity arm found NO kit copy of scratch-guard.js in this tree — an arm with no subject cannot pass"
  fail=$((fail+1))
fi

# ---- the meta-arm: prove the liveness guard itself fires ------------------------------------------
# A guard nobody has seen fail is an assertion about nothing. This runs a COPY of this file with the
# payload builder stubbed to emit nothing, and requires that copy to fail naming the builder.
if [ "${SG_META:-}" != "1" ]; then
  sed 's#^  payload=$("$TESTPY".*#  payload=""#' "$0" > "$TMP/meta.sh"
  if SG_META=1 bash "$TMP/meta.sh" 2>&1 | grep -q 'the payload builder produced nothing'; then
    echo "ok   the payload-builder liveness guard fires when the builder is stubbed"; pass=$((pass+1))
  else
    echo "FAIL the liveness guard did NOT fire — every ALLOW arm here may be passing vacuously"
    fail=$((fail+1))
  fi
fi

n=$((pass+fail))
# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not on the written one. An arm stranded
# past an early exit is invisible to grep and to a reader; only the total moves. Lower it in a
# reviewed diff or not at all.
# 90 = 60 + the 27 assertions TOOL-aProbedUnit-5 added (26 in its block, 1 from re-targeting the /tmp
# near-miss) + the 3 its round-1 fold added (clusters J and K). The pin sits alone on its line because
# the testsuite-counts leg reads it anchored, `^FLOOR_ASSERTIONS=[0-9]+$`.
FLOOR_ASSERTIONS=90
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; fail=$((fail+1)); }
echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ]
