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

# ==================================================================================================
# ---- the ORIENTATION check (TOOL-aReplayedCard-1): a `git commit` on an un-oriented card ----------
# The fixture is a scratch REPOSITORY under this suite's mktemp, with one commit and a LINKED
# WORKTREE, so the arms exercise the `.git` FILE branch every real session in this repo takes. Every
# payload `cwd` is the fixture as node spells it (`C:\…`), never the MSYS path, because that is what
# the harness hands the hook. The arm rule: an ALLOW with a present `--write` card asserts stderr
# byte-EMPTY; an ALLOW on absence, replay origin, an unwalkable target or the exemption asserts its
# one witness line by text; a DENY asserts the card path and the remedy by text. Session ids carry
# the `sgtest-` prefix, and the last arm lists this repository's real common dir for strays.

# run_card <name> <want_exit> <stderr-expect> <command-text> [<field>=<value> ...]
#   <stderr-expect> is `empty` (byte-EMPTY), `one;;<needle>[;;<needle>…]` (exactly one line, carrying
#   every needle) or `any;;<needle>[;;<needle>…]` (every needle present). Fields are payload keys
#   beside tool_name/tool_input: session_id, cwd, agent_id, tool_use_id.
run_card() {
  local name=$1 want=$2 expect=$3 cmd=$4; shift 4
  local payload got err bad="" mode rest needle
  payload=$("$TESTPY" -c 'import json,sys; d={"tool_name":"Bash","tool_input":{"command":sys.argv[1]}}; d.update(kv.split("=",1) for kv in sys.argv[2:]); print(json.dumps(d))' "$cmd" "$@")
  # THE LIVENESS GUARD, `run`'s and for its reason: a builder that produced nothing makes every ALLOW
  # arm pass for the wrong reason — and every `empty` stderr assertion with it. The meta-arm stubs
  # this line too, so the guard is observed to fire here as well.
  case "$payload" in *'"command"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  printf '%s' "$payload" \
    | HOME="$FIX_HOME" USERPROFILE="$FIX_PROFILE" TEMP="$FIX_TEMP" TMP="$FIX_TEMP" TMPDIR= \
      node "$HOOK" >/dev/null 2>"$TMP/err"
  got=$?
  err=$(cat "$TMP/err")
  if [ "$got" != "$want" ]; then
    echo "FAIL $name (exit $got, want $want)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); return
  fi
  mode=${expect%%;;*}; rest=${expect#*;;}
  case "$mode" in
    empty) [ -z "$err" ] || bad="stderr is not byte-empty" ;;
    one)   [ "$(printf '%s' "$err" | grep -c .)" = 1 ] || bad="stderr is not exactly one line" ;;
    any)   ;;
    *)     bad="unknown stderr expectation '$mode'" ;;
  esac
  if [ "$mode" != empty ] && [ -z "$bad" ]; then
    while :; do
      needle=${rest%%;;*}
      case "$err" in *"$needle"*) ;; *) bad="stderr lacks '$needle'"; break ;; esac
      [ "$needle" = "$rest" ] && break
      rest=${rest#*;;}
    done
  fi
  if [ -z "$bad" ]; then echo "ok   $name (exit $got)"; pass=$((pass+1))
  else echo "FAIL $name (exit $got, $bad)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}

# The fixture: SGFIX is the primary (`.git` a directory), SGWT its linked worktree (`.git` a file).
SGFIX="$TMP/sgfix"; SGWT="$TMP/sgwt"; SGGIT="git -c user.email=sg@test -c user.name=sgtest"
if git init -q "$SGFIX" && $SGGIT -C "$SGFIX" commit -q --allow-empty -m init \
   && git -C "$SGFIX" worktree add -q "$SGWT" -b sg-wt 2>/dev/null; then
  echo "ok   the orientation fixture built: a scratch repository with one commit and a linked worktree"; pass=$((pass+1))
else
  echo "FAIL the orientation fixture could not be built (git init / commit / worktree add)"; fail=$((fail+1))
fi
SG_CWD_FIX=$(cd "$SGFIX" && node -p 'process.cwd()')
SG_CWD_WT=$(cd "$SGWT" && node -p 'process.cwd()')
SG_TOP_FIX=$(git -C "$SGFIX" rev-parse --show-toplevel)     # git's spelling — what the writer's `tree —` cell carries
SG_TOP_WT=$(git -C "$SGWT" rev-parse --show-toplevel)
SG_CARDS="$SGFIX/.git/orientation"
SG_READY='READY — sgtest · node a · sg-wt · base 0000000 · Tier-1 · gates none'
# The hook's one comparable form, read from the hook rather than re-spelled here — a second fold in
# the test would be the second normaliser the spec forbids in the hook, one file over.
build_comparable() { node -e 'console.log(require(process.argv[1]).buildComparablePath(process.argv[2]))' "$HOOK" "$1"; }
# write_card <sid> <tree-cell-toplevel> <writer-verb> <ready-line> — the writer's shape, by hand.
write_card() {
  mkdir -p "$SG_CARDS"
  printf 'orientation — %s · written 2026-09-14T00:00:00+0000 · by manifest-check.sh --card --%s\nnode — a · sgtest\ntree — %s · worktree · branch sg-wt · BASE 0000000 · clean\nworktrees — 2\nlive — skipped: no .memory-tree.conf in this tree\nrecent —\n%s\n' \
    "$1" "$3" "$2" "$4" > "$SG_CARDS/$1.md"
}
SG_CARD_FIX=$(build_comparable "$SG_CWD_FIX")/.git/orientation   # the card path as the hook prints it

# ---- AC1: an absent card, with and without the directory, and a replay-written sentinel card -----
rm -rf "$SG_CARDS"
run_card "AC1 absent card, no orientation/ dir -> allow, one witness line" 0 "one;;absent;;$SG_CARD_FIX/sgtest-a1.md" 'git commit -m x' session_id=sgtest-a1 "cwd=$SG_CWD_WT"
mkdir -p "$SG_CARDS"
run_card "AC1 absent card, orientation/ dir present -> allow, one witness line" 0 "one;;absent;;sgtest-a1.md" 'git commit -m x' session_id=sgtest-a1 "cwd=$SG_CWD_WT"
write_card sgtest-a2 "$SG_TOP_WT" replay 'READY — none yet'
run_card "AC1 replay-written sentinel card -> allow, one witness line" 0 "one;;replay-written;;$SG_CARD_FIX/sgtest-a2.md" 'git commit -m x' session_id=sgtest-a2 "cwd=$SG_CWD_WT"

# ---- AC2: a --write card with the sentinel only denies; a real READY line and matching cell allows -
write_card sgtest-b1 "$SG_TOP_WT" write 'READY — none yet'
run_card "AC2 --write card holding the sentinel only -> deny naming the card path, sentinel, /session-kickoff" 2 "any;;$SG_CARD_FIX/sgtest-b1.md;;sentinel;;/session-kickoff" 'git commit -m x' session_id=sgtest-b1 "cwd=$SG_CWD_WT"
write_card sgtest-b1 "$SG_TOP_WT" write "$SG_READY"
run_card "AC2 real READY line, matching tree cell -> allow, stderr EMPTY" 0 empty 'git commit -m x' session_id=sgtest-b1 "cwd=$SG_CWD_WT"

# ---- AC3: the card names tree A, the payload comes from linked worktree B through its .git FILE ---
write_card sgtest-c1 "$SG_TOP_FIX" write "$SG_READY"
run_card "AC3 card names A, payload from B -> deny naming both trees and cd B && /session-kickoff" 2 "any;;$SG_TOP_FIX;;cd $(build_comparable "$SG_CWD_WT") && /session-kickoff" 'git commit -m x' session_id=sgtest-c1 "cwd=$SG_CWD_WT"
write_card sgtest-c1 "$SG_TOP_WT" write "$SG_READY"   # the cell rewritten to B, as --card --append does
run_card "AC3 the cell rewritten to B -> allow, stderr EMPTY" 0 empty 'git commit -m x' session_id=sgtest-c1 "cwd=$SG_CWD_WT"

# ---- AC4: the exemption — a NEW build README carrying an accepted authorized-by: value -----------
write_card sgtest-d1 "$SG_TOP_WT" write 'READY — none yet'
mkdir -p "$SGWT/builds/x" && printf -- '---\nslug: x\nauthorized-by: prompt\n---\n' > "$SGWT/builds/x/README.md" && git -C "$SGWT" add builds/x/README.md
run_card "AC4 staged NEW builds/x/README.md authorized-by: prompt -> allow, exemption line" 0 "one;;exempt;;builds/x/README.md;;prompt" 'git commit -m x' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
# `-f` on every cleanup: `git rm --cached` REFUSES a file whose index blob differs from both HEAD and
# the worktree — exactly the state the staged-versus-worktree pair below builds — and the refusal
# left the README staged, so AC8 measured a fixture with an index that was not empty. Found RED.
git -C "$SGWT" rm -q -f --cached builds/x/README.md && rm -rf "$SGWT/builds"
mkdir -p "$SGWT/memory/builds/y" && printf -- '---\nslug: y\nauthorized-by: prompt\n---\n' > "$SGWT/memory/builds/y/README.md" && git -C "$SGWT" add memory/builds/y/README.md
run_card "AC4 staged NEW memory/builds/y/README.md authorized-by: prompt -> allow, exemption line" 0 "one;;exempt;;memory/builds/y/README.md;;prompt" 'git commit -m x' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
printf -- '---\nslug: y\nauthorized-by: recipe\n---\n' > "$SGWT/memory/builds/y/README.md" && git -C "$SGWT" add memory/builds/y/README.md
run_card "AC4 the same with authorized-by: recipe -> allow, exemption line" 0 "one;;exempt;;recipe" 'git commit -m x' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
printf -- '---\nslug: y\n---\n' > "$SGWT/memory/builds/y/README.md"   # the index still holds the recipe blob
run_card "AC4 staged blob carries the key, worktree copy does not -> allow (the BLOB is read)" 0 "one;;exempt" 'git commit -m x' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
git -C "$SGWT" add memory/builds/y/README.md && printf -- '---\nslug: y\nauthorized-by: prompt\n---\n' > "$SGWT/memory/builds/y/README.md"
run_card "AC4 staged blob lacks the key, worktree copy carries it -> deny" 2 "any;;sentinel" 'git commit -m x' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
# F10 (the aReplayedCard closing review): the key OUTSIDE the front matter — a column-0 line in the
# body, the shape a fenced example or copied prose leaves — exempts nothing, because the unattended
# driver reads the key between line 1's `---` and the next `---` and nowhere else.
printf -- '---\nslug: y\n---\n\n```\nauthorized-by: prompt\n```\n' > "$SGWT/memory/builds/y/README.md" && git -C "$SGWT" add memory/builds/y/README.md
run_card "AC4 staged NEW README with authorized-by: prompt in the BODY only, front matter without it -> deny (F10)" 2 "any;;sentinel" 'git commit -m x' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
git -C "$SGWT" rm -q -f --cached memory/builds/y/README.md && rm -rf "$SGWT/memory"
mkdir -p "$SGWT/docs" && printf -- '---\nauthorized-by: prompt\n---\n' > "$SGWT/docs/README.md" && git -C "$SGWT" add docs/README.md
run_card "AC4 NEW docs/README.md carrying the key -> deny (outside the rule)" 2 "any;;sentinel" 'git commit -m x' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
git -C "$SGWT" rm -q -f --cached docs/README.md && rm -rf "$SGWT/docs"
mkdir -p "$SGWT/rebuilds/z" && printf -- '---\nauthorized-by: prompt\n---\n' > "$SGWT/rebuilds/z/README.md" && git -C "$SGWT" add rebuilds/z/README.md
run_card "AC4 NEW rebuilds/z/README.md carrying the key -> deny (the pathspec lists it, the rule rejects it)" 2 "any;;sentinel" 'git commit -m x' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
git -C "$SGWT" rm -q -f --cached rebuilds/z/README.md && rm -rf "$SGWT/rebuilds"

# ---- AC8: an UNTRACKED authorized README and the single-call add-and-commit from a subdirectory --
mkdir -p "$SGWT/memory/builds/y" && printf -- '---\nslug: y\nauthorized-by: prompt\n---\n' > "$SGWT/memory/builds/y/README.md"
SG_CWD_SUB=$(cd "$SGWT/memory" && node -p 'process.cwd()')
run_card "AC8 untracked memory/builds/y/README.md, nothing staged, add-and-commit from a subdirectory -> allow, exemption line" 0 "one;;exempt;;memory/builds/y/README.md" 'git add memory && git commit -m z' session_id=sgtest-d1 "cwd=$SG_CWD_SUB"

# ---- AC5: the folder COMMITTED in HEAD exempts nothing — the exemption is the commit that CREATES it
git -C "$SGWT" add memory && $SGGIT -C "$SGWT" commit -q -m "an authorized build folder, landed"
printf 'x\n' > "$SGWT/unrelated.txt" && git -C "$SGWT" add unrelated.txt
run_card "AC5 authorized folder already in HEAD, an unrelated file staged -> deny" 2 "any;;sentinel;;/session-kickoff" 'git commit -m y' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
git -C "$SGWT" rm -q -f --cached unrelated.txt && rm -f "$SGWT/unrelated.txt"

# ---- AC6 / AC7: the subagent allow, and the fail-open set is exactly session_id and cwd ----------
run_card "AC6 agent_id present, sentinel card -> allow, stderr EMPTY" 0 empty 'git commit -m x' session_id=sgtest-d1 "cwd=$SG_CWD_WT" agent_id=sub-1
run_card "AC7 no session_id -> allow, prints nothing" 0 empty 'git commit -m x' "cwd=$SG_CWD_WT"
run_card "AC7 no cwd -> allow, prints nothing" 0 empty 'git commit -m x' session_id=sgtest-d1
run_card "AC7 tool_use_id absent, session_id and cwd present, sentinel card -> deny (tool_use_id is not read)" 2 "any;;sentinel" 'git commit -m x' session_id=sgtest-d1 "cwd=$SG_CWD_WT"

# ---- AC9: the CLASS arm — every inline `git ` span of the engine's Steps 0–4 is allowed ----------
# The population is EXTRACTED from the engine file at run time, so a command the engine adds to its
# orientation batch is fed here without anyone remembering to add an arm. The floor is PINNED at the
# base measurement; an empty extraction is REFUSED rather than passed, the green-by-absence class.
SG_SPAN_FLOOR=8   # measured 2026-09-14 at base c95fe32a: eight spans between `## Step 0` and `## Step 5`
extract_git_spans() { # <engine-file> → the spans, one per line; exit 1 naming the empty population
  local spans
  spans=$(awk '/^## Step 0/{f=1} /^## Step 5/{f=0} f' "$1" | grep -o '`git [^`]*`' | tr -d '`')
  if [ -z "$spans" ]; then echo "extract_git_spans: empty population — no inline git span between Step 0 and Step 5 in $1" >&2; return 1; fi
  printf '%s\n' "$spans"
}
SG_ENGINE="$ROOT/skills/session-kickoff/SKILL.md"
if [ -f "$SG_ENGINE" ] && extract_git_spans "$SG_ENGINE" > "$TMP/spans" 2>"$TMP/spans.err"; then
  sg_nspans=$(grep -c . "$TMP/spans")
  echo "     AC9 extracted $sg_nspans inline git spans from the engine's Steps 0-4 (floor $SG_SPAN_FLOOR)"
  if [ "$sg_nspans" -ge "$SG_SPAN_FLOOR" ]; then echo "ok   AC9 the extracted count is at or above the pinned floor"; pass=$((pass+1))
  else echo "FAIL AC9 extracted $sg_nspans spans, under the floor of $SG_SPAN_FLOOR — the engine lost commands or the extractor lost its grip"; fail=$((fail+1)); fi
  while IFS= read -r sg_span; do
    run_card "AC9 engine span '$sg_span' on a sentinel card -> allow, stderr EMPTY" 0 empty "$sg_span" session_id=sgtest-d1 "cwd=$SG_CWD_WT"
  done < "$TMP/spans"
else
  echo "FAIL AC9 the engine file yielded no git spans — an empty population is refused, not passed"; cat "$TMP/spans.err" 2>/dev/null; fail=$((fail+1))
fi
printf '# a fixture engine\n## Step 0 — x\nno spans here\n## Step 5 — y\n' > "$TMP/empty-engine.md"
if extract_git_spans "$TMP/empty-engine.md" >/dev/null 2>"$TMP/e"; then
  echo "FAIL AC9 the extractor passed a fixture engine with no git span"; fail=$((fail+1))
elif grep -q 'empty population' "$TMP/e"; then echo "ok   AC9 the extractor exits 1 naming the empty population on a spanless engine"; pass=$((pass+1))
else echo "FAIL AC9 the extractor failed on the spanless engine without naming the empty population"; fail=$((fail+1)); fi
for sg_lit in 'git fetch' 'git merge --ff-only origin/main' 'git rev-parse HEAD' 'git status --short' 'git worktree list' \
              'git merge-base origin/main HEAD' 'git log --grep commit' 'git commit-tree' 'git push origin main'; do
  run_card "AC9 literal '$sg_lit' on a sentinel card -> allow, stderr EMPTY" 0 empty "$sg_lit" session_id=sgtest-d1 "cwd=$SG_CWD_WT"
done
# The value flags: `-C` walks the FOLDED target from a cwd OUTSIDE the fixture, quoted or not.
SG_TOP_WT_MSYS=$(printf '%s' "$SG_TOP_WT" | sed 's#^\([A-Za-z]\):/#/\l\1/#')   # C:/… -> /c/…
SG_CWD_OUT=$(cd "$TMP" && node -p 'process.cwd()')
run_card "AC9 git -C </c/ spelling of the fixture> commit from OUTSIDE the fixture, sentinel -> deny" 2 "any;;sentinel" "git -C $SG_TOP_WT_MSYS commit -m y" session_id=sgtest-d1 "cwd=$SG_CWD_OUT"
run_card "AC9 git -C \"<fixture toplevel>\" commit (quoted value is one token), sentinel -> deny" 2 "any;;sentinel" "git -C \"$SG_TOP_WT\" commit -m y" session_id=sgtest-d1 "cwd=$SG_CWD_OUT"
run_card "AC9 git -c a=b commit, sentinel -> deny" 2 "any;;sentinel" 'git -c a=b commit' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
run_card "AC9 git -c \"a=b\" commit, sentinel -> deny" 2 "any;;sentinel" 'git -c "a=b" commit' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
write_card sgtest-e1 "$SG_TOP_WT" write "$SG_READY"
run_card "AC9 git -C </c/ spelling> commit from OUTSIDE with a real card naming the fixture -> allow, stderr EMPTY (the fold walked)" 0 empty "git -C $SG_TOP_WT_MSYS commit -m y" session_id=sgtest-e1 "cwd=$SG_CWD_OUT"
run_card "AC9 git -C /nowhere/x commit -> allow, the does-not-exist line (F4: a missing start is never walked)" 0 "one;;does not exist" 'git -C /nowhere/x commit' session_id=sgtest-e1 "cwd=$SG_CWD_WT"
mkdir -p "$TMP/nogit"; SG_NOGIT=$(cd "$TMP/nogit" && node -p 'process.cwd()')
run_card "AC9 git -C <an existing dir under no repository> commit -> allow, the unwalkable line" 0 "one;;no .git above" "git -C $SG_NOGIT commit" session_id=sgtest-e1 "cwd=$SG_CWD_WT"

# ---- F3 and F4 (the aReplayedCard closing review): `cd <dir> && git commit`, and targets that ----
# ---- do not exist or are not literal paths ----------------------------------------------------
# F3 — the compound form is judged against the tree the `cd` names, in BOTH directions: the card
# names the worktree and the payload cwd is the primary; the card names the primary and the same
# command runs. Absolute and relative `cd` targets, the relative one from the fixtures' parent.
run_card "F3 cd <wt> && git commit from the primary, cell = wt -> allow, stderr EMPTY" 0 empty "cd $SG_TOP_WT && git commit -m y" session_id=sgtest-e1 "cwd=$SG_CWD_FIX"
run_card "F3 cd sgwt && git commit from the fixtures' parent (relative), cell = wt -> allow, stderr EMPTY" 0 empty 'cd sgwt && git commit -m y' session_id=sgtest-e1 "cwd=$SG_CWD_OUT"
write_card sgtest-f3 "$SG_TOP_FIX" write "$SG_READY"
run_card "F3 cd <wt> && git commit, cell = primary -> deny naming <wt> as the target and cd <wt> && /session-kickoff" 2 "any;;$SG_TOP_FIX;;this commit targets $(build_comparable "$SG_CWD_WT");;cd $(build_comparable "$SG_CWD_WT") && /session-kickoff" "cd $SG_TOP_WT && git commit -m y" session_id=sgtest-f3 "cwd=$SG_CWD_FIX"
run_card "F3 the last cd wins: cd <primary>; cd <wt> && git commit, cell = wt -> allow, stderr EMPTY" 0 empty "cd $SG_TOP_FIX; cd $SG_TOP_WT && git commit -m y" session_id=sgtest-e1 "cwd=$SG_CWD_OUT"
# F4 — a `-C` target that does not exist used to walk UP into the primary's `.git` and deny with a
# remedy that re-homed the card to the wrong tree; an unexpandable one (`$X`, `~/x`) resolved
# literally to a directory that does not exist and did the same. Both are witnesses now.
run_card "F4 git -C ../sgfix/nope commit from the worktree (the walk from a missing start would land on the PRIMARY's .git), real card naming the worktree -> allow, the does-not-exist line" 0 "one;;does not exist;;sgfix/nope" 'git -C ../sgfix/nope commit -m y' session_id=sgtest-e1 "cwd=$SG_CWD_WT"
run_card "F4 git -C \"\$X\" commit on a sentinel card -> allow, the not-a-literal-path line" 0 "one;;not a literal path;;\$X" 'git -C "$X" commit -m y' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
run_card "F4 cd \$S && git commit on a sentinel card (a scratch fixture) -> allow, the not-a-literal-path line" 0 "one;;not a literal path;;\$S" 'cd $S && git commit -m y' session_id=sgtest-d1 "cwd=$SG_CWD_WT"
run_card "F4 cd ~/x && git commit on a sentinel card -> allow, the not-a-literal-path line" 0 "one;;not a literal path;;~/x" 'cd ~/x && git commit -m y' session_id=sgtest-d1 "cwd=$SG_CWD_WT"

# ---- AC10: the CROSS-KIT arm — the writer's own card, from the LIVE writer, in the worktree ------
# The WORKING TREE's `skills/session-kickoff/manifest-check.sh` by default, so a spelling fold
# between the two kits reds HERE, on the writer's real bytes: it ran from a blob pinned at the
# step's base (`c95fe32a`, 208 lines behind the writer that shipped) and could not see the
# `tree —` re-render or the appended READY line the live writer produces (the aReplayedCard closing
# review, F6). `SG_WRITER_BASE=<sha>` takes a blob EXPLICITLY; neither present is an announced skip.
SG_WRITER="$ROOT/skills/session-kickoff/manifest-check.sh"
if [ -n "${SG_WRITER_BASE:-}" ]; then
  SG_WRITER="$TMP/manifest-check.sh"
  git -C "$HERE" show "$SG_WRITER_BASE:skills/session-kickoff/manifest-check.sh" > "$SG_WRITER" 2>/dev/null || rm -f "$SG_WRITER"
fi
if [ ! -f "$SG_WRITER" ]; then
  echo "SKIP AC10 the kickoff kit's writer is not at $SG_WRITER — the cross-kit arm has no writer to run; install skills/session-kickoff/ or pass SG_WRITER_BASE=<sha>"
elif (cd "$SGWT" && bash "$SG_WRITER" --card --write --session sgtest-w1 </dev/null >"$TMP/writer.out" 2>&1) \
   && [ -f "$SG_CARDS/sgtest-w1.md" ]; then
  echo "ok   AC10 the writer at $SG_WRITER wrote $SG_CARDS/sgtest-w1.md from the linked worktree"; pass=$((pass+1))
  run_card "AC10 the writer's card unchanged (sentinel in place) -> deny naming the sentinel and the card path" 2 "any;;sentinel;;$SG_CARD_FIX/sgtest-w1.md" 'git commit -m x' session_id=sgtest-w1 "cwd=$SG_CWD_WT"
  sed -i "s/^READY — none yet\$/$SG_READY/" "$SG_CARDS/sgtest-w1.md"
  run_card "AC10 the sentinel replaced by a real READY line through sed -> allow, stderr EMPTY" 0 empty 'git commit -m x' session_id=sgtest-w1 "cwd=$SG_CWD_WT"
  rm -f "$SG_CARDS/sgtest-w1.md"
  run_card "AC10 the writer's card removed -> allow, the absence line" 0 "one;;absent;;sgtest-w1.md" 'git commit -m x' session_id=sgtest-w1 "cwd=$SG_CWD_WT"
  # THE FOLD ITSELF: a fresh card, then the writer's own `--card --append` with a real READY body
  # pinned at the worktree's HEAD — the append re-renders the `tree —` cell and replaces the sentinel
  # — and the hook reads that card. Every spelling both kits share is exercised end to end here.
  sg_w1_head=$(git -C "$SGWT" rev-parse HEAD)
  if (cd "$SGWT" && bash "$SG_WRITER" --card --write --session sgtest-w1 </dev/null >"$TMP/writer.out" 2>&1) \
     && printf '## task\n- `README.md:1`\nREADY — sgtest · node a · sg-wt · base %s · Tier-1 · gates none\n' "$sg_w1_head" \
        | (cd "$SGWT" && bash "$SG_WRITER" --card --append --session sgtest-w1 >"$TMP/append.out" 2>&1); then
    echo "ok   AC10 the writer's --card --append landed a real READY body on sgtest-w1"; pass=$((pass+1))
  else
    echo "FAIL AC10 the writer's --card --append refused the real READY body:"; sed 's/^/     /' "$TMP/append.out" 2>/dev/null; fail=$((fail+1))
  fi
  run_card "AC10 the card the live writer wrote AND appended -> allow, stderr EMPTY (the cross-kit fold)" 0 empty 'git commit -m x' session_id=sgtest-w1 "cwd=$SG_CWD_WT"
  rm -f "$SG_CARDS/sgtest-w1.md"
else
  echo "FAIL AC10 the writer at $SG_WRITER did not run from the linked worktree, or wrote no card:"; sed 's/^/     /' "$TMP/writer.out" 2>/dev/null; fail=$((fail+1))
fi
write_card sgtest-w2 "$SG_TOP_WT_MSYS" write "$SG_READY"
run_card "AC10 the card holding /c/… and the payload C:\\… for one tree -> allow, stderr EMPTY" 0 empty 'git commit -m x' session_id=sgtest-w2 "cwd=$SG_CWD_WT"

# ---- AC12: a non-commit payload with a sentinel card never reaches the check --------------------
run_card "AC12 non-commit ls payload on a sentinel card -> allow, stderr EMPTY" 0 empty 'ls' session_id=sgtest-d1 "cwd=$SG_CWD_WT"

# ---- AC11: the shared common dir is clean, and the accepted modes are the driver's own -----------
sg_common=$(git -C "$HERE" rev-parse --git-common-dir 2>/dev/null)
if [ -n "$sg_common" ] && [ -z "$(ls "$sg_common/orientation" 2>/dev/null | grep '^sgtest-')" ]; then
  echo "ok   AC11 this repository's common dir holds no orientation/sgtest-* card after the run"; pass=$((pass+1))
else
  echo "FAIL AC11 a fixture card leaked into this repository's common dir: $(ls "$sg_common/orientation" 2>/dev/null | grep '^sgtest-' | tr '\n' ' ')"; fail=$((fail+1))
fi
# DERIVED, never spelled: the driver's path is a sibling kit's, which this file may not name by
# literal; `git ls-files` answers where it lives in THIS tree, and an empty answer is a refusal.
sg_driver=$(git -C "$ROOT" ls-files -- '*/unattended.sh' 2>/dev/null | head -1)
sg_modes_driver=$(sed -n 's/^SECOND_ANCHOR_MODES="\([^"]*\)".*/\1/p' "$ROOT/$sg_driver" 2>/dev/null | head -1)
sg_modes_hook=$(node -p "require(process.argv[1]).ANCHOR_MODES.join(' ')" "$HOOK")
if [ -z "$sg_driver" ] || [ -z "$sg_modes_driver" ]; then
  echo "FAIL AC11 the parity arm found no SECOND_ANCHOR_MODES in a tracked unattended.sh — an arm with no subject cannot pass"; fail=$((fail+1))
elif [ "$sg_modes_driver" = "$sg_modes_hook" ]; then
  echo "ok   AC11 the hook's accepted authorized-by: values equal the driver's SECOND_ANCHOR_MODES ($sg_modes_hook)"; pass=$((pass+1))
else
  echo "FAIL AC11 the hook accepts '$sg_modes_hook' but the driver's SECOND_ANCHOR_MODES is '$sg_modes_driver'"; fail=$((fail+1))
fi

n=$((pass+fail))
# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not on the written one. An arm stranded
# past an early exit is invisible to grep and to a reader; only the total moves. Lower it in a
# reviewed diff or not at all.
# 164 = 134 (the suite as landed by aReplayedCard) + the 27 assertions TOOL-aProbedUnit-5 added (26 in
# its block, 1 from re-targeting the /tmp near-miss) + the 3 its round-1 fold added (clusters J and K).
# The pin sits alone on its line because the testsuite-counts leg reads it anchored.
FLOOR_ASSERTIONS=164
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; fail=$((fail+1)); }
echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ]
