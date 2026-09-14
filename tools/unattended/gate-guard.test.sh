#!/usr/bin/env bash
# Runnable check for gate-guard.js — the PreToolUse guard that refuses the flagged merge bar and
# every self-test suite while the unattended run on the current branch is before VERIFYING.
# Run: bash tools/unattended/gate-guard.test.sh   (exit 0 = all pass)
#
# WITHHELD FROM THE BAR AND FROM ADOPTERS, like every suite in this kit: its subject is the hook's
# predicate and key, which move only when this file's sibling moves. `run-unattended-gates.sh`
# enumerates it through the budget row; the main loop runs it at VERIFYING, where the hook itself
# admits the invocation. A build pass never runs it — the hook this suite tests would deny the
# invocation at BUILDING, which is the whole point, and the pass observes each arm by feeding the
# hook the arm's payload directly instead (spec TOOL-aDeferredBar-3 §6).
#
# WHAT THIS FILE DOES NOT CHECK, stated up front because a structural check reads as a semantic one
# to everybody who did not write it: it does not prove the hook is WIRED (the adopter's --check arm
# and check-hook-destinations.sh own that), and it does not prove the predicate is complete over
# real usage — that is the corpus probe in the build record, which ran it over every shell call in
# the operator's transcript store and walked the near-misses by hand.
#
# EVERY ARM DRIVES ITS OWN TREE. The hook keys on a `.git` HEAD, a conf and a run-state record, so
# every fixture is a scratch tree under mktemp -d carrying exactly those three and never the real
# tree: an arm that inherited the real repository would measure a different thing on every branch
# and pass green on the ones where no run was live.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
HOOK="$HERE/gate-guard.js"
DRIVER="$HERE/unattended.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0

if [ -f "$HERE/../lib/resolve-python.sh" ]; then
  . "$HERE/../lib/resolve-python.sh"
  TESTPY=$(resolve_python) || { echo "gate-guard.test: no usable python"; exit 2; }
else
  TESTPY=python3   # gov:literal-python — last-resort fallback when ../lib/ is absent (adopter layout)
fi

# The payload's `cwd` must be a path node resolves on this host: MSYS spells a scratch dir /tmp/x
# where node wants C:/..., and a cwd node cannot walk keys nothing, which passes every deny arm for
# the wrong reason.
resolve_native() { cygpath -m "$1" 2>/dev/null || printf '%s' "$1"; }

# build_fixture <phase> [fact-line ...] -> a scratch tree: .git/HEAD on refs/heads/fx, a conf, one record.
# The default record is run-branch-anchored and carries branch-ref: refs/heads/fx, which is the
# fallback key; arms that need another shape pass their own fact lines.
build_fixture() {
  local d; d=$(mktemp -d "$TMP/fx.XXXXXX")
  mkdir -p "$d/.git" "$d/memory/builds/fx"
  printf 'ref: refs/heads/fx\n' > "$d/.git/HEAD"
  printf 'MEMORY_ROOT=memory\n' > "$d/.unattended.conf"
  { printf '# fx\n\n## Run facts\nwitness: abc\nphase: %s\n' "$1"; shift
    if [ "$#" = 0 ]; then printf 'anchor-kind: run-branch\nbranch-ref: refs/heads/fx\n'
    else for l in "$@"; do printf '%s\n' "$l"; done; fi
  } > "$d/memory/builds/fx/RUN.md"
  printf '%s' "$d"
}

# run <name> <expected_exit> <fixture> <command-text> [tool] — the payload is BUILT, never
# hand-spliced; a Windows path carries backslashes and those are the top JSON breaker.
run() {
  local name=$1 want=$2 fix=$3 cmd=$4 tool=${5:-Bash}
  local payload got
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":sys.argv[1],"cwd":sys.argv[2],"tool_input":{"command":sys.argv[3]}}))' "$tool" "$(resolve_native "$fix")" "$cmd")
  # THE LIVENESS GUARD. The hook exits 0 on unparseable stdin by design, so a builder that produced
  # nothing makes every ALLOW arm pass for the wrong reason. Its own failing case is the meta-arm.
  case "$payload" in *'"command"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  printf '%s' "$payload" | node "$HOOK" >/dev/null 2>"$TMP/err"
  got=$?
  if [ "$got" = "$want" ]; then echo "ok   $name (exit $got)"; pass=$((pass+1))
  else echo "FAIL $name (exit $got, want $want)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}
# check_names <name> <token> — the LAST run's stderr carries an indented line naming the token.
check_names() {
  if grep -qE "^  (flag|suite|runner): $2\$" "$TMP/err"; then echo "ok   $1 names $2"; pass=$((pass+1))
  else echo "FAIL $1 does not name $2"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}
run_raw() { # name expected_exit payload
  printf '%s' "$3" | node "$HOOK" >/dev/null 2>&1
  local got=$?
  if [ "$got" = "$2" ]; then echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $got, want $2)"; fail=$((fail+1)); fi
}

B=$(build_fixture BUILDING)
BAR='GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh'
D4='bash tools/unattended/check-unattended.test.sh'

# ---- fail-open: the hook must never be the reason a good command dies -----------------------------
run_raw "empty stdin -> allow"        0 ''
run_raw "non-JSON stdin -> allow"     0 'not json at all'
run_raw "JSON null -> allow"          0 'null'
run_raw "unrelated tool -> allow"     0 "{\"tool_name\":\"Read\",\"cwd\":\"$(resolve_native "$B")\",\"tool_input\":{\"command\":\"$D4\"}}"
run_raw "no command key -> allow"     0 "{\"tool_name\":\"Bash\",\"cwd\":\"$(resolve_native "$B")\",\"tool_input\":{}}"

# ---- AC1: the flagged bar at BUILDING on the fixture's own branch ---------------------------------
run "AC1 GATE_SELFTESTS=1 on the plain bar at BUILDING -> deny"   2 "$B" "$BAR"
check_names "AC1" 'GATE_SELFTESTS=1'
case "$(cat "$TMP/err")" in *"BLOCKED by gate-guard"*) echo "ok   the deny carries the BLOCKED prefix"; pass=$((pass+1)) ;; *) echo "FAIL the deny is missing its BLOCKED prefix"; fail=$((fail+1)) ;; esac
case "$(cat "$TMP/err")" in *"memory/builds/fx/RUN.md"*) echo "ok   the deny names the record path, derived from the walk"; pass=$((pass+1)) ;; *) echo "FAIL the deny does not name the record"; fail=$((fail+1)) ;; esac
case "$(cat "$TMP/err")" in *"before VERIFYING"*) echo "ok   the deny names the phase the bar waits for"; pass=$((pass+1)) ;; *) echo "FAIL the deny does not name VERIFYING"; fail=$((fail+1)) ;; esac

# ---- AC2: eleven deny payloads, each naming its matched token ------------------------------------
run "AC2 GATE_FULL=1 prefix -> deny"               2 "$B" 'GATE_FULL=1 bash tools/run-gates/run-gates.sh'; check_names "AC2 prefix" 'GATE_FULL=1'
run "AC2 after export -> deny"                     2 "$B" 'export GATE_FULL=1; bash tools/run-gates/run-gates.sh'; check_names "AC2 export" 'GATE_FULL=1'
run "AC2 behind env -> deny"                       2 "$B" 'env GATE_FULL=1 bash tools/run-gates/run-gates.sh'; check_names "AC2 env" 'GATE_FULL=1'
run "AC2 behind a NAME=value word -> deny"         2 "$B" 'GATE_JOBS=1 GATE_FULL=1 bash tools/run-gates/run-gates.sh'; check_names "AC2 NAME=value" 'GATE_FULL=1'
run "AC2 behind timeout 30 -> deny"                2 "$B" 'timeout 30 env GATE_FULL=1 bash tools/run-gates/run-gates.sh'; check_names "AC2 timeout" 'GATE_FULL=1'
run "AC2 after && -> deny"                         2 "$B" 'cd /x && GATE_FULL=1 bash tools/run-gates/run-gates.sh'; check_names "AC2 &&" 'GATE_FULL=1'
run "AC2 after then -> deny"                       2 "$B" 'if true; then GATE_FULL=1 bash tools/run-gates/run-gates.sh; fi'; check_names "AC2 then" 'GATE_FULL=1'
run "AC2 D2 the self-test runner -> deny"          2 "$B" 'bash tools/run-gates/run-selftests.sh'; check_names "AC2 D2" 'tools/run-gates/run-selftests.sh'
run "AC2 D3 this kit's runner -> deny"             2 "$B" 'bash tools/unattended/run-unattended-gates.sh'; check_names "AC2 D3" 'tools/unattended/run-unattended-gates.sh'
run "AC2 D4 a suite -> deny"                       2 "$B" "$D4"; check_names "AC2 D4" 'tools/unattended/check-unattended.test.sh'
run "AC2 D5 a suite inside bash -c quotes -> deny" 2 "$B" "bash -c 'timeout 5400 bash tools/unattended/unattended.test.sh'"; check_names "AC2 D5" 'tools/unattended/unattended.test.sh'

# ---- rev-4 shapes: the three prefixes the corpus measurement found hiding 38 runs -----------------
run "time bash <suite> -> deny"                    2 "$B" 'time bash tools/x.test.sh 2>&1 | tail -3'; check_names "time" 'tools/x.test.sh'
run "(time bash <suite>) -> deny"                  2 "$B" '(time bash tools/x.test.sh) > out 2>&1'
run "nohup bash <suite> & -> deny"                 2 "$B" 'nohup bash tools/x.test.sh > out 2>&1 &'
run "{ bash <suite>; } -> deny"                    2 "$B" 'cd x && { bash tools/x.test.sh > out; echo rc=$?; }'
run "  near-miss: time bash <suite> --check -> allow" 0 "$B" 'time bash tools/x.test.sh --check'

# ---- closing review F2: a whole-suite `selftest.py` FILE is a suite; a `--selftest` FLAG is not -----
# Both readers of this build spelled "suite" as the `.test.sh` filename convention, and the manifest's
# python whole-suite legs — govkit's at 3445 s — walked past both. RED-first on the shipped hook:
# the first payload printed rc=0.
run "F2 python <kit>/selftest.py -> deny"           2 "$B" 'python tools/govkit/selftest.py'; check_names "F2 selftest.py" 'tools/govkit/selftest.py'
run "F2 a --selftest FLAG on another file -> allow"  0 "$B" 'python3 tools/memory-tree/gotchas.py --selftest'
# THE PARITY ARM, and the reason the rows above are not the last word: the suite population is the
# manifest's `chunk = selftests` legs, DERIVED here rather than restated, minus the `--selftest`
# flag form the child prompt admits. Every member must be a hit at BUILDING. ONE assertion over the
# population, so the floor does not move with the manifest, plus one that the population is
# non-empty — a manifest naming no suite would otherwise certify parity by grading nothing.
# The exemption list is a DECLARED, ANNOUNCED skip with its reason, asserted live (a stale name reds):
#   test_recall_floor.py — the pytest `test_*.py` convention, gov-only, 12 s to 34 s in the ledger.
#   A `test_*.py` word shape would deny an adopter's single-file pytest run, which is exactly the
#   direct check a spec may name, so the class is not gated and this one member is named instead.
LEGS="$HERE/../gate-legs.json"
PARITY_EXEMPT='test_recall_floor.py'
if [ -f "$LEGS" ]; then
  pop=$("$TESTPY" -c 'import json,sys
for l in json.load(open(sys.argv[1], encoding="utf-8")):
    a = l.get("argv") or []
    if l.get("chunk") == "selftests" and "--selftest" not in a: print(" ".join(a))' "$LEGS" | tr -d '\r')
  # `tr -d '\r'`: a Windows python writes CRLF to a pipe, and a CR on the basename made the exemption
  # never match — observed while writing this arm, and the stale-exemption clause is what said so.
  popn=$(printf '%s\n' "$pop" | grep -c .)
  if [ "$popn" -gt 0 ]; then echo "ok   parity: the manifest holds $popn whole-suite selftests leg(s)"; pass=$((pass+1))
  else echo "FAIL parity: the manifest holds no whole-suite selftests leg, so parity would be certified over nothing"; fail=$((fail+1)); fi
  unmatched=""; skipped=""; exempt_seen=""
  while IFS= read -r cmd; do
    [ -n "$cmd" ] || continue
    base=${cmd##*/}
    case " $PARITY_EXEMPT " in *" $base "*) skipped="$skipped $base"; exempt_seen="$exempt_seen $base"; continue ;; esac
    payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Bash","cwd":sys.argv[1],"tool_input":{"command":sys.argv[2]}}))' "$(resolve_native "$B")" "$cmd")
    printf '%s' "$payload" | node "$HOOK" >/dev/null 2>&1; [ $? = 2 ] || unmatched="$unmatched
     $cmd"
  done <<PARITY
$pop
PARITY
  for x in $PARITY_EXEMPT; do
    case " $exempt_seen " in *" $x "*) ;; *) unmatched="$unmatched
     (stale exemption: $x names no whole-suite selftests leg in the manifest)" ;; esac
  done
  for x in $skipped; do echo "     skip: $x — declared exempt, see the comment above"; done
  if [ -z "$unmatched" ]; then echo "ok   parity: every whole-suite selftests leg of the manifest is a hit at BUILDING ($popn legs, $(printf '%s' "$skipped" | wc -w) exempt)"; pass=$((pass+1))
  else echo "FAIL parity: a manifest suite invocation the hook does NOT deny at BUILDING:$unmatched"; fail=$((fail+1)); fi
else
  echo "FAIL parity: no gate manifest beside the kit at $LEGS, so the suite population cannot be derived"; fail=$((fail+1))
fi

# ---- AC3: the allow set is the tail of PHASES_CORE from VERIFYING -------------------------------
for ph in VERIFYING LANDING LANDED ABORTED; do
  F=$(build_fixture "$ph")
  run "AC3 $ph: D1 -> allow" 0 "$F" "$BAR"
  run "AC3 $ph: D2 -> allow" 0 "$F" 'bash tools/run-gates/run-selftests.sh'
  run "AC3 $ph: D3 -> allow" 0 "$F" 'bash tools/unattended/run-unattended-gates.sh'
  run "AC3 $ph: D4 -> allow" 0 "$F" "$D4"
done
# ...and at BUILDING the forms the owner allows: the plain bar and the read-only verbs.
run "AC3 BUILDING: the plain bar with GATE_JOBS=1 -> allow"  0 "$B" 'GATE_JOBS=1 bash tools/run-gates/run-gates.sh'
run "AC3 BUILDING: D1's OFF spelling, the empty assignment -> allow" 0 "$B" 'GATE_FULL= bash tools/run-gates/run-gates.sh'
run "AC3 BUILDING: GATE_FULL=\"\" quoted empty -> allow"     0 "$B" 'GATE_FULL="" bash tools/run-gates/run-gates.sh'
run "AC3 BUILDING: run-selftests.sh --list -> allow"          0 "$B" 'bash tools/run-gates/run-selftests.sh --list'
run "AC3 BUILDING: run-selftests.sh --check -> allow"         0 "$B" 'bash tools/run-gates/run-selftests.sh --check'
run "AC3 BUILDING: run-selftests.sh --rank -> allow"          0 "$B" 'bash tools/run-gates/run-selftests.sh --rank'
run "AC3 BUILDING: run-unattended-gates.sh --help -> allow"   0 "$B" 'bash tools/unattended/run-unattended-gates.sh --help'
run "AC3 BUILDING: a suite --render -> allow"                 0 "$B" 'bash tools/memory-tree/kit-dogfood-parity.test.sh --render'
run "AC3 BUILDING: a suite --check -> allow"                  0 "$B" 'bash tools/memory-tree/kit-dogfood-parity.test.sh --check'
# rev-5: the no-exec syntax check. The wired hook denied this suite's own `bash -n` in the pass
# that built it; 412 raw mentions of the shape in the corpus, every one a parse.
run "AC3 BUILDING: bash -n <suite>, the syntax check -> allow" 0 "$B" 'bash -n tools/unattended/gate-guard.test.sh'
run "  control: bash -x <suite> is still a run -> deny"       2 "$B" 'bash -x tools/unattended/gate-guard.test.sh'
run "  control: BUILDING still denies the bare suite"         2 "$B" "$D4"

# ---- AC4: the key --------------------------------------------------------------------------------
F=$(build_fixture BUILDING 'anchor-kind: run-branch' 'branch-ref: refs/heads/other')
run "AC4 branch fact names another branch -> allow"           0 "$F" "$D4"
F=$(build_fixture BUILDING 'anchor-kind: run-branch')
run "AC4 neither run-branch nor branch-ref -> allow"          0 "$F" "$D4"
F=$(build_fixture BUILDING); printf '0123456789abcdef0123456789abcdef01234567\n' > "$F/.git/HEAD"
run "AC4 HEAD holds a bare sha -> allow"                      0 "$F" "$D4"
F=$(build_fixture BUILDING); rm "$F/memory/builds/fx/RUN.md"
run "AC4 no record -> allow"                                  0 "$F" "$D4"
F=$(build_fixture BUILDING); rm "$F/.unattended.conf"
run "AC4 .unattended.conf absent -> allow"                    0 "$F" "$D4"
# The conf is SOURCED by the driver and re-parsed here, the two-readers class: a legal shell
# spelling the second reader misreads turns into a memory root that resolves nowhere, and the hook
# switches itself off silently. One arm per spelling the corpus of conf files actually uses.
F=$(build_fixture BUILDING); printf 'MEMORY_ROOT=memory   # the tree, matching .memory-tree.conf\n' > "$F/.unattended.conf"
run "conf: MEMORY_ROOT with a trailing comment still keys -> deny" 2 "$F" "$D4"
F=$(build_fixture BUILDING); printf 'MEMORY_ROOT="memory"\n' > "$F/.unattended.conf"
run "conf: a double-quoted MEMORY_ROOT still keys -> deny"    2 "$F" "$D4"
F=$(build_fixture BUILDING); printf 'LANDER="x"\n' > "$F/.unattended.conf"
run "conf: no MEMORY_ROOT key defaults to memory -> deny"     2 "$F" "$D4"
F=$(build_fixture BUILDING); printf 'MEMORY_ROOT=../elsewhere\n' > "$F/.unattended.conf"
run "conf: a MEMORY_ROOT escaping the root keys nothing -> allow" 0 "$F" "$D4"
F=$(build_fixture BUILDING); printf 'phase: BUILDING\nrun-branch: refs/heads/fx\n' > "$F/memory/builds/fx/RUN.md"
run "AC4 a record with no Run facts heading still keys -> deny" 2 "$F" "$D4"
# THE WORKTREE ARM AND ITS NEGATIVE CONTROL. `.git` is a FILE whose gitdir names a directory under
# the common dir; the worktree's HEAD is there and the common dir's HEAD is the primary's branch.
# Swapping the two HEADs must flip the verdict, or the hook is reading the wrong one.
build_worktree() { # <worktree-HEAD-ref> <common-HEAD-ref>
  local d; d=$(build_fixture BUILDING)
  mkdir -p "$d/common/.git/worktrees/wt"
  printf 'ref: %s\n' "$2" > "$d/common/.git/HEAD"
  printf 'ref: %s\n' "$1" > "$d/common/.git/worktrees/wt/HEAD"
  printf '../../..\n' > "$d/common/.git/worktrees/wt/commondir"
  rm -rf "$d/.git"
  printf 'gitdir: %s/common/.git/worktrees/wt\n' "$(resolve_native "$d")" > "$d/.git"
  printf '%s' "$d"
}
F=$(build_worktree refs/heads/fx refs/heads/main)
run "AC4 worktree FILE whose gitdir HEAD keys the deny -> deny" 2 "$F" "$D4"
F=$(build_worktree refs/heads/main refs/heads/fx)
run "  control: the COMMON dir's HEAD keys the deny, the worktree's does not -> allow" 0 "$F" "$D4"
# THE DEFAULT-BRANCH RECORD, the 17-of-44 hole rev-1 keyed: no branch-ref, run-branch equal to HEAD.
# RED-first against a copy of the hook with the run-branch read removed, which is rev-1's keying.
F=$(build_fixture BUILDING 'anchor-kind: default-branch' 'run-branch: refs/heads/fx')
sed "s/readFact('run-branch') || readFact('branch-ref')/readFact('branch-ref')/" "$HOOK" > "$TMP/rev1.js"
if grep -q "readFact('run-branch')" "$TMP/rev1.js"; then echo "FAIL the rev-1 copy still reads run-branch, so the RED-first arm has no subject"; fail=$((fail+1)); else echo "ok   the rev-1 copy reads branch-ref only"; pass=$((pass+1)); fi
payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Bash","cwd":sys.argv[1],"tool_input":{"command":sys.argv[2]}}))' "$(resolve_native "$F")" "$D4")
printf '%s' "$payload" | node "$TMP/rev1.js" >/dev/null 2>&1; got=$?
if [ "$got" = 0 ]; then echo "ok   RED-first: rev-1 keying allows the default-branch record (exit 0)"; pass=$((pass+1)); else echo "FAIL rev-1 keying should allow the default-branch record, got $got"; fail=$((fail+1)); fi
run "AC4 default-branch record keyed by run-branch: on the shipped hook -> deny" 2 "$F" "$D4"
F=$(build_fixture BUILDING 'anchor-kind: run-branch' 'branch-ref: refs/heads/fx')
run "AC4 branch-ref: equal and no run-branch: -> deny"        2 "$F" "$D4"
F=$(build_fixture BUILDING 'anchor-kind: run-branch' 'run-branch: refs/heads/fx' 'branch-ref: refs/heads/other')
run "AC4 run-branch: wins over a differing branch-ref: -> deny" 2 "$F" "$D4"
# Two records on the branch: one already at VERIFYING, one still at BUILDING. The deny names the one
# that is before VERIFYING.
F=$(build_fixture VERIFYING); mkdir -p "$F/memory/builds/gx"; printf '# gx\n\n## Run facts\nphase: BUILDING\nbranch-ref: refs/heads/fx\n' > "$F/memory/builds/gx/RUN.md"
run "two records on the branch, one before VERIFYING -> deny" 2 "$F" "$D4"
case "$(cat "$TMP/err")" in *"BUILDING (memory/builds/gx/RUN.md)"*) echo "ok   the deny names the BUILDING record and not the VERIFYING one"; pass=$((pass+1)) ;; *) echo "FAIL the deny does not name the BUILDING record"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)) ;; esac

# ---- AC5: mentions are not hits ------------------------------------------------------------------
run "AC5 git commit -m quoting a suite name -> allow"          0 "$B" 'git commit -m "the unattended.test.sh arm for run-branch"'
run "AC5 heredoc body spelling GATE_FULL=1 -> allow"           0 "$B" 'python - <<EOF
import subprocess
subprocess.run("GATE_FULL=1 bash tools/run-gates/run-gates.sh", shell=True)
EOF'
run "AC5 grep with a bare suite name argument -> allow"        0 "$B" 'grep -c gate-guard.test.sh tools/run-gates/selftest-budgets.txt'
run "AC5 grep with a quoted suite name -> allow"               0 "$B" "grep -n 'check-unattended.test.sh' tools/unattended/kit.toml"
run "AC5 echo quoting a brace-group run -> allow"              0 "$B" 'echo "{ bash tools/x.test.sh; }"'
run "AC5 node reading the hook itself -> allow"                0 "$B" 'node tools/unattended/gate-guard.js'
run "AC5 cat over this suite -> allow"                         0 "$B" 'cat tools/unattended/gate-guard.test.sh'
run "AC5 --writes naming a suite behind the driver -> allow"   0 "$B" 'bash tools/unattended/unattended.sh --dispatch s --pass TOOL-s-1 --writes tools/unattended/check-unattended.test.sh'

# ---- two shapes in one command are two indented lines --------------------------------------------
run "flag and suite in one command -> deny"                    2 "$B" "$BAR && bash tools/unattended/unattended.test.sh"
check_names "two shapes, first" 'GATE_SELFTESTS=1'
check_names "two shapes, second" 'tools/unattended/unattended.test.sh'
case "$(head -1 "$TMP/err")" in *"the flagged merge bar and a self-test suite"*) echo "ok   the first line names both shapes in words"; pass=$((pass+1)) ;; *) echo "FAIL the first line does not name both shapes"; fail=$((fail+1)) ;; esac

# ---- a quoted path still resolves; a pipe or a subshell is still a run --------------------------
run "quoted suite path -> deny"                                2 "$B" 'bash "tools/unattended/unattended.test.sh"'
run "suite piped into tail -> deny"                            2 "$B" 'bash tools/x.test.sh 2>&1 | tail -3'
run "suite inside a subshell -> deny"                          2 "$B" '(cd /x; bash tools/x.test.sh)'
run "suite inside a command substitution -> deny"              2 "$B" 'x=$(bash tools/x.test.sh)'
run "bash -x <suite> -> deny"                                  2 "$B" 'bash -x tools/x.test.sh'

# ---- closing review F7: three corpus RUN shapes the rev-5 view let through, each observed rc=0 first
# A double-quoted `$( … )` was blanked as string content; `timeout -k 5 120` made `-k` the head;
# `stdbuf` was not a prefix word. Each is a sidechain-corpus shape, and each is a run.
run "F7 a suite inside a double-quoted \$( ) -> deny"          2 "$B" 'printf "rc=%s\n" "$(bash tools/memory-tree/kit-dogfood-parity.test.sh; echo $?)"'; check_names "F7 subst" 'tools/memory-tree/kit-dogfood-parity.test.sh'
run "F7 timeout -k 5 120 bash <suite> -> deny"                 2 "$B" 'timeout -k 5 120 bash tools/unattended/unattended.test.sh > out 2>&1'
run "F7 (stdbuf -oL -eL bash <suite>) & -> deny"               2 "$B" '(stdbuf -oL -eL bash tools/run-gates/run-gates.test.sh > out 2>&1) &'
# ...and the fourth the re-run corpus walk surfaced: `time` by path, with its format option.
run "F7 /usr/bin/time -f FMT bash <suite> -> deny"             2 "$B" "/usr/bin/time -f 'real %e' bash tools/x.test.sh > out 2>&1"
run "  control: a single-quoted \$( ) stays content -> allow"  0 "$B" "echo '\$(bash tools/x.test.sh)'"

# ---- PowerShell is the same act through the other shell ------------------------------------------
run "PowerShell running a suite -> deny"                       2 "$B" "$D4" PowerShell
# closing review F8: the PowerShell-NATIVE flag spelling. `NAME=value cmd` is not PowerShell syntax,
# so the one spelling that runs the flagged bar under the second wired tool is `$env:NAME=value;`.
# The shipped FLAG_RE anchored on the bare name and both `$env:` forms printed rc=0.
run "F8 PowerShell \$env:GATE_SELFTESTS=1; bash <bar> -> deny" 2 "$B" '$env:GATE_SELFTESTS=1; bash tools/run-gates/run-gates.sh' PowerShell; check_names "F8 env" '[$]env:GATE_SELFTESTS=1'
run "F8 PowerShell \$env:GATE_FULL=\"\"; bash <bar> -> allow"  0 "$B" '$env:GATE_FULL=""; bash tools/run-gates/run-gates.sh' PowerShell
run "out-of-scope tool name -> allow"                          0 "$B" "$BAR" Zsh

# ---- the PHASES_CORE parity arm: the restatement in the hook equals the driver's tail ------------
# The kit's own checker reads PHASES_CORE only through the driver and opens no sibling .js, so its
# silence over this file would be a zero that proves nothing (spec §8 F5). This arm is the liveness.
want=$(sed -n 's/^PHASES_CORE="\(.*\)"/\1/p' "$DRIVER" | grep -o 'VERIFYING.*')
got=$(node -p "require(require('path').resolve(process.argv[1])).PHASES_ALLOW.join(' ')" "$HOOK" 2>/dev/null)
if [ -n "$want" ] && [ "$want" = "$got" ]; then echo "ok   PHASES_ALLOW equals the driver's PHASES_CORE tail from VERIFYING: $got"; pass=$((pass+1))
else echo "FAIL PHASES_ALLOW [$got] != the driver's tail [$want] — a restatement that drifted"; fail=$((fail+1)); fi

# ---- the meta-arm: prove the liveness guard itself fires ------------------------------------------
if [ "${GG_META:-}" != "1" ]; then
  sed 's#^  payload=$("$TESTPY" -c .import json,sys; print(json.dumps({"tool_name":sys.argv\[1\].*#  payload=""#' "$0" > "$TMP/meta.sh"
  if GG_META=1 bash "$TMP/meta.sh" 2>&1 | grep -q 'the payload builder produced nothing'; then
    echo "ok   the payload-builder liveness guard fires when the builder is stubbed"; pass=$((pass+1))
  else
    echo "FAIL the liveness guard did NOT fire — every ALLOW arm here may be passing vacuously"; fail=$((fail+1))
  fi
fi

n=$((pass+fail))
# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not on the written one. Authored from a
# static count of the arms above at ~10% headroom, because the pass that wrote this file may not
# run it (the hook it tests denies the invocation at BUILDING); the main loop's first green at
# VERIFYING confirms the executed count against this floor. Lower it in a reviewed diff or not at all.
FLOOR_ASSERTIONS=103
# RAISED 90 -> 94 at the closing review's F2, by the static count of the arms it added: the
# selftest.py deny, the --selftest flag allow, and the two parity assertions. RAISED 94 -> 103 at
# its F7 and F8 by the same rule: four run-shape denies with one token check and one control, and
# the two PowerShell `$env:` arms with one token check.
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; fail=$((fail+1)); }
echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ]
