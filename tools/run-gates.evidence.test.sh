#!/usr/bin/env bash
# run-gates.evidence.test.sh — fixture harness for DURABLE LEG EVIDENCE (TOOL-dNomadicAtlas-1).
# Exit 0 = all cases pass.
#
# What this gates that nothing else can: when a leg goes red, its own output must survive on disk, so
# a caller who pipes/backgrounds/scrolls away the runner can still name the failing test without
# re-running the whole bar. leg() already held every leg's merged output in $out and printed it, then
# kept only the ROW for the durable summary — the reason was in scope at the exact line the durable
# record was built, and dropped there.
#
# This is a FIXTURE harness, not a canary: run-gates.test.sh is static (it parses the manifest and
# greps the runner) and never executes run-gates.sh. Executing the real runner in place would re-run
# the whole bar recursively and clobber the live gate-last-summary.txt mid-run, so every case here
# drives it through GATE_LEGS with its own scratch GIT_DIR.
set -u

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "evidence-test: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
RUNNER="$ROOT/tools/run-gates.sh"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
bad=0
ok()   { echo "  ok   — $1"; }
nope() { echo "  FAIL — $1"; bad=1; }

# mk_legs <file> <json-array-body>
mk_legs() { printf '[%s]\n' "$2" > "$1"; }

# fresh_gitdir <n> — a scratch GIT_DIR per case, so cases cannot read each other's logs and the real
# gate-last-summary.txt is never touched
fresh_gitdir() {
  local d="$tmp/gd$1"; rm -rf "$d"; git init -q --bare "$d" 2>/dev/null || mkdir -p "$d"
  printf '%s' "$d"
}
# GIT_WORK_TREE is required, not decoration: the runner resolves ROOT with `--show-toplevel`,
# which refuses a bare GIT_DIR outright. Without it every case dies at line 7 with exit 2.
run() { GIT_DIR="$1" GIT_WORK_TREE="$ROOT" GATE_LEGS="$2" bash "$RUNNER" 2>&1; }

# ---------------------------------------------------------------------------------------------
# 1. a failing leg's own output survives on disk, and the caller's stdout is irrelevant to that
# ---------------------------------------------------------------------------------------------
gd="$(fresh_gitdir 1)"
mk_legs "$tmp/l1.json" '{"name":"red-leg","argv":["bash","-c","echo NEEDLE_UP_4c1; exit 1"]}'
run "$gd" "$tmp/l1.json" > /dev/null 2>&1
log="$gd/gate-logs/red-leg.log"
if [ -f "$log" ] && grep -q NEEDLE_UP_4c1 "$log"; then
  ok "a red leg's output survives on disk"
else
  nope "a red leg's output is NOT on disk (looked in $log)"
fi

# the durable summary must POINT at it — a pointer, never the bytes: this file is what an operator
# is told to read after a refused push
sum="$gd/gate-last-summary.txt"
if [ -f "$sum" ] && grep -q 'red-leg.log' "$sum"; then
  ok "the durable summary points at the failing leg's log"
else
  nope "the durable summary does not name the failing leg's log"
fi
if [ -f "$sum" ] && grep -q NEEDLE_UP_4c1 "$sum"; then
  nope "raw leg bytes leaked into gate-last-summary.txt (must be a POINTER only)"
else
  ok "gate-last-summary.txt carries a pointer, not raw leg output"
fi

# ---------------------------------------------------------------------------------------------
# 2. a PASSING leg is captured too — a later bisect reads the green run's output, and the bytes are
#    already in memory
# ---------------------------------------------------------------------------------------------
gd="$(fresh_gitdir 2)"
mk_legs "$tmp/l2.json" '{"name":"green-leg","argv":["bash","-c","echo NEEDLE_GREEN_88; exit 0"]}'
run "$gd" "$tmp/l2.json" > /dev/null 2>&1
if grep -q NEEDLE_GREEN_88 "$gd/gate-logs/green-leg.log" 2>/dev/null; then
  ok "a passing leg's output is captured as well"
else
  nope "a passing leg's output was not captured"
fi

# ---------------------------------------------------------------------------------------------
# 3. gate-last-failure.txt is written on RED and SURVIVES a later green run. gate-last-summary.txt is
#    overwritten by every run, so the reflexive re-run would otherwise erase the failing evidence.
# ---------------------------------------------------------------------------------------------
gd="$(fresh_gitdir 3)"
mk_legs "$tmp/l3red.json"   '{"name":"r","argv":["bash","-c","echo NEEDLE_KEEP_d2; exit 1"]}'
mk_legs "$tmp/l3green.json" '{"name":"r","argv":["bash","-c","echo fine; exit 0"]}'
run "$gd" "$tmp/l3red.json"   > /dev/null 2>&1
run "$gd" "$tmp/l3green.json" > /dev/null 2>&1
if [ -f "$gd/gate-last-failure.txt" ] && grep -q 'gates RED' "$gd/gate-last-failure.txt"; then
  ok "gate-last-failure.txt survives a subsequent GREEN run"
else
  nope "gate-last-failure.txt was erased by the green re-run"
fi
if grep -q 'gates GREEN' "$gd/gate-last-summary.txt" 2>/dev/null; then
  ok "gate-last-summary.txt still reflects the LATEST run"
else
  nope "gate-last-summary.txt did not follow the latest run"
fi

# ---------------------------------------------------------------------------------------------
# 4. THE CAPTURE PATH MUST NEVER DECIDE WHETHER A LEG RUNS.
#
# Two distinct states, and only one of them is reachable through GIT_DIR. An absent GIT_DIR is
# refused at line 7 by `git rev-parse --show-toplevel` — before any capture code — so the evidence
# layer can never compose a path from an empty root that way. The capture-off branch is reached by a
# gate-logs that cannot be CREATED, which a plain file in its place produces exactly.
# ---------------------------------------------------------------------------------------------
mk_legs "$tmp/l4.json" '{"name":"fine","argv":["bash","-c","echo hi; exit 0"]}'
out="$(GIT_DIR="$tmp/nope.git" GIT_WORK_TREE="$ROOT" GATE_LEGS="$tmp/l4.json" bash "$RUNNER" 2>&1)"; rc=$?
if [ "$rc" -eq 2 ] && printf '%s' "$out" | grep -q 'not a git repo'; then
  ok "an absent git dir is refused at the repo guard, before any capture"
else
  nope "an absent git dir was not refused cleanly (rc=$rc)"
fi

gd="$(fresh_gitdir 4)"; : > "$gd/gate-logs"   # a FILE where the directory must go
out="$(run "$gd" "$tmp/l4.json")"; rc=$?
if [ "$rc" -eq 0 ] && printf '%s' "$out" | grep -q 'gates GREEN'; then
  ok "an uncreatable log dir does not change the verdict"
else
  nope "an uncreatable log dir changed the verdict (rc=$rc)"
fi
if printf '%s' "$out" | grep -qi 'evidence capture OFF'; then
  ok "capture-off is STATED, not silent"
else
  nope "capture was disabled silently — green-by-absence"
fi

# ---------------------------------------------------------------------------------------------
# 5. REDACTION — a leg can echo an operator-exported credential, and a file outlives a terminal
# ---------------------------------------------------------------------------------------------
gd="$(fresh_gitdir 5)"
mk_legs "$tmp/l5.json" '{"name":"secret","argv":["bash","-c","echo using postgresql://carol:topsecret@db.example/x; exit 1"]}'
run "$gd" "$tmp/l5.json" > /dev/null 2>&1
sl="$gd/gate-logs/secret.log"
if [ -f "$sl" ] && ! grep -q 'topsecret' "$sl" && grep -q 'db.example' "$sl"; then
  ok "URL userinfo is redacted, the rest of the line is kept"
else
  nope "a credential survived into a durable log"
fi

# ---------------------------------------------------------------------------------------------
# 6. the GATE_LEGS seam itself: without it this harness cannot exist, so it is part of the contract
# ---------------------------------------------------------------------------------------------
out="$(GIT_DIR="$(fresh_gitdir 6)" GIT_WORK_TREE="$ROOT" GATE_LEGS="$tmp/definitely-absent.json" bash "$RUNNER" 2>&1)"; rc=$?
if [ "$rc" -eq 2 ] && printf '%s' "$out" | grep -q 'definitely-absent.json'; then
  ok "an unreadable GATE_LEGS exits 2 and names the file it could not parse"
else
  nope "an unreadable GATE_LEGS did not fail cleanly (rc=$rc)"
fi

echo
if [ "$bad" = 0 ]; then echo "PASS (run-gates evidence durability)"; else echo "FAIL (run-gates evidence durability)"; fi
exit "$bad"
