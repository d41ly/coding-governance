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

# run <name> <expected_exit> <command-text> [tool] — the payload is BUILT, never hand-spliced;
# an unescaped backslash in a Windows path is the top JSON breaker and every arm here carries one.
run() {
  local name=$1 want=$2 cmd=$3 tool=${4:-Bash}
  local payload got
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":sys.argv[1],"tool_input":{"command":sys.argv[2]}}))' "$tool" "$cmd")
  # THE LIVENESS GUARD. The hook exits 0 on unparseable stdin by design, so a builder that produced
  # nothing makes every ALLOW arm pass for the wrong reason. A fixture that produced nothing is a
  # failure, not a silent green. Its own failing case is exercised by the meta-arm at the bottom.
  case "$payload" in *'"command"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  printf '%s' "$payload" \
    | HOME="$FIX_HOME" USERPROFILE="$FIX_PROFILE" TEMP="$FIX_TEMP" TMP="$FIX_TEMP" TMPDIR= \
      node "$HOOK" >/dev/null 2>"$TMP/err"
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
run "cp home-rooted SOURCE -> allow"              0 'cp ~/.merge-bar.log /tmp/inv/'
run "mv destination -> deny"                      2 'mv memory/x.md ~/.backup.md'
run "mv home-rooted SOURCE -> allow"              0 'mv ~/.merge-bar.log /tmp/inv/'
run "rsync destination -> deny"                   2 'rsync -a memory/ ~/.mirror/'

# ---- the DRIVE-ROOT rule. The home rule above was scoped to home, so everything outside it was
# ---- unguarded: an agent fixture wrote 7.2 MB to C:/gvi, outside repo, scratchpad and guard.
# ---- Measured over 128,568 real tool calls: this predicate hits 16, all of them agent litter,
# ---- while the obvious wider one hits 2,449 and is almost all legitimate /tmp use.
run "drive-root mkdir -> deny"                    2 'mkdir -p /c/gvi'
run "drive-root redirect -> deny"                 2 'echo x > /c/temp-hyg.txt'
run "drive-root windows spelling -> deny"         2 'mkdir C:/gvi'
run "drive-root cp DESTINATION -> deny"           2 'cp memory/x.md /c/scratch/inv/'
run "  near-miss: /tmp is a real root -> allow"   0 'echo x > /tmp/hyg.txt'
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
if [ -n "$ROOT" ] && [ -f "$ROOT/tools/hooks/scratch-guard.js" ]; then
  if [ ! -f "$ROOT/.claude/hooks/scratch-guard.js" ]; then
    echo "FAIL the wired copy .claude/hooks/scratch-guard.js is MISSING (parity must not be satisfiable by absence)"
    fail=$((fail+1))
  elif diff -q <(sed 's/\r$//' "$ROOT/.claude/hooks/scratch-guard.js") <(sed 's/\r$//' "$ROOT/tools/hooks/scratch-guard.js") >/dev/null; then
    echo "ok   the wired copy matches the kit copy"; pass=$((pass+1))
  else
    echo "FAIL .claude/hooks/scratch-guard.js has drifted from $KIT_REL/scratch-guard.js"
    echo "     fix: cp $KIT_REL/scratch-guard.js .claude/hooks/scratch-guard.js"
    fail=$((fail+1))
  fi
else
  echo "skip the two-copy parity arm — no kit copy tracked in this tree (adopter layout)"
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
FLOOR_ASSERTIONS=60
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; fail=$((fail+1)); }
echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ]
