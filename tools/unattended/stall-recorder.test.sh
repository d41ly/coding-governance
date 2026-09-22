#!/usr/bin/env bash
# Runnable check for stall-recorder.js — the `StopFailure` hook that appends one line per API-error
# stall of a bound session to `<git-dir>/unattended/stall.<slug>.log`, and cannot block.
# Run: bash tools/unattended/stall-recorder.test.sh   (exit 0 = all pass)
#
# WITHHELD FROM THE BAR AND FROM ADOPTERS, like every suite in this kit (kit.toml `project-owned`):
# its subject is the hook's key and its line shape, which move only when this file's siblings move.
# `run-unattended-gates.sh` enumerates it through its budget row; the main loop runs it at
# VERIFYING. A build pass never runs it — the pass observes each arm by feeding the copied hook
# the arm's payload directly instead (spec TOOL-aWokenSentinel-4 §6).
#
# WHAT THIS FILE DOES NOT CHECK, stated up front because a structural check reads as a semantic
# one to everybody who did not write it: it does not prove the hook is WIRED (the adopter's
# --check arm and check-hook-destinations.sh own that), it does not prove the harness hands the
# hook an `error` field — that field is UNVERIFIED on this fleet (spec §3), and every arm here
# FEEDS the payload it asserts on — and it does not prove `--liveness` is right beyond the one
# `last-stall:` line the real-driver arm reads back.
#
# EVERY ARM DRIVES ITS OWN TREE. The hook keys on a `.git`, a conf and a run-state record, so every
# fixture is a scratch tree carrying exactly those and never the real tree: an arm that inherited
# the real repository would bind or not depending on which session ran it. The hook is COPIED to a
# scratch kit dir beside its module; no driver stub, because this hook never spawns one.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# STALL_RECORDER_TEST_TMP is the pass's seam: a unit pass runs one arm at a time from a sourced
# copy of this prologue and must put its scratch under the session scratchpad, not /tmp.
# STALL_RECORDER_TEST_GITTMP is the real-driver arm's: its `git init` fixture wants a SHORT path on
# Windows, where the scratchpad's is long enough to break git.
TMP="${STALL_RECORDER_TEST_TMP:-$(mktemp -d)}"; trap 'rm -rf "$TMP"' EXIT
GITTMP="${STALL_RECORDER_TEST_GITTMP:-$TMP}"
pass=0; fail=0
print_ok()   { echo "ok   $1"; pass=$((pass+1)); }
print_bad()  { echo "FAIL $1"; fail=$((fail+1)); }
check_same() { if [ "$2" = "$3" ]; then print_ok "$1"; else print_bad "$1: expected [$3], got [$2]"; fi; }
check_hit()  { if grep -qF -- "$2" <<<"$1"; then print_ok "$3"; else print_bad "$3: missing [$2]"; fi; }

if [ -f "$HERE/../lib/resolve-python.sh" ]; then
  . "$HERE/../lib/resolve-python.sh"
  TESTPY=$(resolve_python) || { echo "stall-recorder.test: no usable python"; exit 2; }
else
  TESTPY=python3   # gov:literal-python — last-resort fallback when ../lib/ is absent (adopter layout)
fi
# The payload's `cwd` must be a path node resolves on this host: MSYS spells a scratch dir /tmp/x
# where node wants C:/..., and a cwd node cannot walk keys nothing, which passes every silent arm
# for the wrong reason.
resolve_native() { cygpath -m "$1" 2>/dev/null || printf '%s' "$1"; }

# THE KIT COPY: the hook and its module, nothing else.
KIT="$TMP/kit"; mkdir -p "$KIT"
cp "$HERE/stall-recorder.js" "$HERE/run-lease.js" "$KIT/" 2>/dev/null
HOOK="$KIT/stall-recorder.js"
SID="11111111-2222-3333-4444-555555555555"

# build_fixture <phase> <session-fact> -> a scratch tree: .git/HEAD, a conf, one record whose
# `## Run facts` region carries the phase and the session fact.
build_fixture() {
  local d; d=$(mktemp -d "$TMP/fx.XXXXXX")
  mkdir -p "$d/.git" "$d/memory/builds/fx"
  printf 'ref: refs/heads/fx\n' > "$d/.git/HEAD"
  printf 'MEMORY_ROOT=memory\n' > "$d/.unattended.conf"
  printf '# fx\n\n## Run facts\nwitness: abc\nphase: %s\nsession: %s\n\n## Parked\n' "$1" "$2" > "$d/memory/builds/fx/RUN.md"
  printf '%s' "$d"
}
# build_payload <fixture> [extra-json-object] — BUILT by python, never hand-spliced; the extra
# object is merged over the base so an arm adds `error` in whatever shape it wants, or none.
build_payload() {
  "$TESTPY" -c 'import json,sys
p={"session_id":sys.argv[2],"hook_event_name":"StopFailure","cwd":sys.argv[1]}
p.update(json.loads(sys.argv[3]) if len(sys.argv)>3 and sys.argv[3] else {})
print(json.dumps(p))' "$(resolve_native "$1")" "$SID" "${2:-}"
}
# run_hook <payload> — runs the copied hook; OUT, ERR and RC are what it did. THE LIVENESS GUARD:
# the hook exits 0 silently on unparseable stdin by design, so a builder that produced nothing
# makes every silent arm pass for the wrong reason; an empty payload is a failed assertion.
run_hook() {
  case "$1" in *'"session_id"'*) ;; *) print_bad "the payload builder produced nothing"; OUT=""; ERR=""; RC=99; return;; esac
  OUT=$(printf '%s' "$1" | node "$HOOK" 2>"$TMP/err"); RC=$?; ERR=$(cat "$TMP/err")
}
derive_sidecar() { printf '%s/.git/unattended/stall.fx.log' "$1"; }
measure_lines() { grep -c '' "$1" 2>/dev/null || echo 0; }
# read_field <file> <n> — field n (1-based) of the LAST line, split on the first three spaces.
read_field() { "$TESTPY" -c 'import sys
ls=[l for l in open(sys.argv[1],encoding="utf-8").read().splitlines() if l.strip()]
print(ls[-1].split(" ",3)[int(sys.argv[2])-1])' "$1" "$2"; }
# check_payload <file> <payload> — `same` when the last line's tail parses deep-equal to the payload.
check_payload() { "$TESTPY" -c 'import json,sys
ls=[l for l in open(sys.argv[1],encoding="utf-8").read().splitlines() if l.strip()]
print("same" if json.loads(ls[-1].split(" ",3)[3])==json.loads(sys.argv[2]) else "differs")' "$1" "$2"; }
# ---- arms ----------------------------------------------------------------------------------------

# ---- AC1: an unbound session — no record names it — exits 0 silently and writes nothing. The
# ---- record is at BUILDING with `session: absent`, the literal that must never bind.
F=$(build_fixture BUILDING absent)
run_hook "$(build_payload "$F" '{"error":"rate_limit"}')"
check_same "AC1 unbound rc" "$RC" "0"
check_same "AC1 unbound stdout empty" "$OUT" ""
[ ! -e "$(derive_sidecar "$F")" ] && print_ok "AC1 unbound writes no sidecar" || print_bad "AC1 unbound wrote $(derive_sidecar "$F")"
run_hook "$(build_payload "$F" '{"session_id":"absent","error":"rate_limit"}')"
check_same "AC1 the literal absent never binds" "$OUT" ""
[ ! -e "$(derive_sidecar "$F")" ] && print_ok "AC1 the literal absent writes no sidecar" || print_bad "AC1 the literal absent wrote a line"

# ---- AC2: a bound session with `error` rate_limit — rc 0, empty stdout, ONE line whose third
# ---- field is the class and whose tail parses deep-equal to the payload fed.
F=$(build_fixture BUILDING "$SID")
P=$(build_payload "$F" '{"error":"rate_limit"}')
run_hook "$P"
check_same "AC2 bound rc" "$RC" "0"
check_same "AC2 bound stdout empty" "$OUT" ""
check_same "AC2 one sidecar line" "$(measure_lines "$(derive_sidecar "$F")")" "1"
check_same "AC2 second field is the session" "$(read_field "$(derive_sidecar "$F")" 2)" "$SID"
check_same "AC2 third field is the class" "$(read_field "$(derive_sidecar "$F")" 3)" "rate_limit"
check_same "AC2 the tail parses deep-equal to the payload" "$(check_payload "$(derive_sidecar "$F")" "$P")" "same"
# the utc is the driver's --park spelling: second precision, Z
check_same "AC2 first field is a second-precision utc" \
  "$(read_field "$(derive_sidecar "$F")" 1 | grep -cE '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$')" "1"

# ---- AC3: no `error` key, `error` as an object, `error` as an empty string — `unknown` each time,
# ---- and the payload still shows what was there.
F=$(build_fixture BUILDING "$SID")
run_hook "$(build_payload "$F")"
check_same "AC3 no error key rc" "$RC" "0"
check_same "AC3 no error key reads unknown" "$(read_field "$(derive_sidecar "$F")" 3)" "unknown"
P=$(build_payload "$F" '{"error":{"type":"rate_limit","retry":3}}')
run_hook "$P"
check_same "AC3 an object reads unknown" "$(read_field "$(derive_sidecar "$F")" 3)" "unknown"
check_same "AC3 the object rides the payload" "$(check_payload "$(derive_sidecar "$F")" "$P")" "same"
run_hook "$(build_payload "$F" '{"error":""}')"
check_same "AC3 an empty string reads unknown" "$(read_field "$(derive_sidecar "$F")" 3)" "unknown"
check_same "AC3 three lines" "$(measure_lines "$(derive_sidecar "$F")")" "3"

# ---- AC4: whitespace in the class is folded to `-`, so the payload keeps its field position.
F=$(build_fixture BUILDING "$SID")
P=$(build_payload "$F" '{"error":"server error 500"}')
run_hook "$P"
check_same "AC4 whitespace folded" "$(read_field "$(derive_sidecar "$F")" 3)" "server-error-500"
check_same "AC4 the payload still parses" "$(check_payload "$(derive_sidecar "$F")" "$P")" "same"

# ---- AC5: stdin that is not JSON — rc 0, empty stdout, nothing written; and no session_id.
F=$(build_fixture BUILDING "$SID")
OUT=$(printf 'not json' | node "$HOOK" 2>/dev/null); RC=$?
check_same "AC5 unparseable stdin rc" "$RC" "0"
check_same "AC5 unparseable stdin stdout empty" "$OUT" ""
[ ! -e "$(derive_sidecar "$F")" ] && print_ok "AC5 unparseable stdin writes nothing" || print_bad "AC5 unparseable stdin wrote a line"
OUT=$(printf '{"hook_event_name":"StopFailure","error":"rate_limit","cwd":"%s"}' "$(resolve_native "$F")" | node "$HOOK" 2>/dev/null); RC=$?
check_same "AC5 no session_id rc" "$RC" "0"
[ ! -e "$(derive_sidecar "$F")" ] && print_ok "AC5 no session_id writes nothing" || print_bad "AC5 no session_id wrote a line"

# ---- AC6: two payloads append in order with the first unchanged; a worktree's `.git` FILE routes
# ---- the line to the per-worktree git dir it names.
F=$(build_fixture BUILDING "$SID")
P1=$(build_payload "$F" '{"error":"rate_limit"}'); run_hook "$P1"
FIRST=$(head -n 1 "$(derive_sidecar "$F")")
P2=$(build_payload "$F" '{"error":"overloaded"}'); run_hook "$P2"
check_same "AC6 two lines" "$(measure_lines "$(derive_sidecar "$F")")" "2"
check_same "AC6 the first line is unchanged" "$(head -n 1 "$(derive_sidecar "$F")")" "$FIRST"
check_same "AC6 the second line is the second class" "$(read_field "$(derive_sidecar "$F")" 3)" "overloaded"
F=$(build_fixture BUILDING "$SID")
mkdir -p "$F/wt-git"; mv "$F/.git/HEAD" "$F/wt-git/HEAD"; rmdir "$F/.git"
printf 'gitdir: %s\n' "$(resolve_native "$F/wt-git")" > "$F/.git"
run_hook "$(build_payload "$F" '{"error":"rate_limit"}')"
check_same "AC6 worktree rc" "$RC" "0"
[ -f "$F/wt-git/unattended/stall.fx.log" ] && print_ok "AC6 the line landed under the named git dir" || print_bad "AC6 no line under $F/wt-git"
check_same "AC6 exactly one stall.fx.log under the fixture" "$(find "$F" -name 'stall.fx.log' | grep -c '')" "1"

# ---- §5: an UNWRITABLE sidecar — one stderr sentence, rc 0, nothing on stdout.
F=$(build_fixture BUILDING "$SID")
printf 'a file where the directory goes\n' > "$F/.git/unattended"
run_hook "$(build_payload "$F" '{"error":"rate_limit"}')"
check_same "unwritable rc" "$RC" "0"
check_same "unwritable stdout empty" "$OUT" ""
check_hit "$ERR" "sidecar-unwritable" "unwritable says so on stderr"
check_same "unwritable wrote nothing" "$(cat "$F/.git/unattended")" "a file where the directory goes"

# ---- S4 / AC13: the fragment registers StopFailure under `*`, and the suite is withheld.
check_same "S4 fragment event StopFailure" "$(grep -c '"event": "StopFailure"' "$HERE/stall-recorder.fragment.json")" "1"
check_same "S4 fragment matcher *" "$(grep -c '"matcher": "\*"' "$HERE/stall-recorder.fragment.json")" "1"
check_same "AC13 the suite is withheld by the descriptor" "$(grep -c 'stall-recorder.test.sh' "$HERE/kit.toml")" "1"

# ---- AC10: ONE arm against the REAL driver, on a `git init` fixture seeded by the adopter suite's
# ---- own seed() — extracted as one function, never the suite — which commits once so HEAD is
# ---- born and the driver's clock probe is live. Before the payload `last-stall: none`; after it,
# ---- the `last-stall:` line equals the sidecar's last line, both read from the fixture.
KIT_REL="${KIT_REL:-tools/unattended}"
TR_T=${KIT_REL%/*}; [ "$TR_T" = "$KIT_REL" ] && TR_T=""; [ -z "$TR_T" ] || TR_T="$TR_T/"
eval "$(sed -n '/^seed() {/,/^}/p' "$HERE/adopt-unattended.test.sh")"
FR="$GITTMP/real"; rm -rf "$FR"; mkdir -p "$GITTMP"; seed "$FR" >/dev/null 2>&1
mkdir -p "$FR/memory/builds/fx"
printf '# fx\n\n## Run facts\nwitness: abc\nphase: BUILDING\nbranch-ref: refs/heads/main\nsession: %s\npid: absent\n\n## Parked\n' "$SID" > "$FR/memory/builds/fx/RUN.md"
if [ -f "$FR/$KIT_REL/stall-recorder.js" ] && [ -f "$FR/$KIT_REL/unattended.sh" ]; then
  BEFORE=$( cd "$FR" && bash "$KIT_REL/unattended.sh" --liveness fx 2>/dev/null | sed -n 's/^last-stall: //p' )
  check_same "AC10 before the payload last-stall is none" "$BEFORE" "none"
  OUT=$(printf '%s' "$(build_payload "$FR" '{"error":"rate_limit"}')" | node "$FR/$KIT_REL/stall-recorder.js" 2>"$TMP/err"); RC=$?
  check_same "AC10 real-driver rc" "$RC" "0"
  check_same "AC10 real-driver stdout empty" "$OUT" ""
  LAST=$(tail -n 1 "$(derive_sidecar "$FR")"); LAST=${LAST%$'\r'}
  AFTER=$( cd "$FR" && bash "$KIT_REL/unattended.sh" --liveness fx 2>/dev/null | sed -n 's/^last-stall: //p' )
  [ -n "$LAST" ] && print_ok "AC10 the sidecar holds a line" || print_bad "AC10 the sidecar is empty"
  check_same "AC10 last-stall equals the sidecar's last line" "$AFTER" "$LAST"
  check_same "AC10 the reader kept the payload whole" "$(printf '%s' "$AFTER" | grep -c 'rate_limit {"session_id"')" "1"
else
  print_bad "AC10 the seed did not place the hook and the driver under $FR/$KIT_REL"
fi
[ "$GITTMP" = "$TMP" ] || rm -rf "$FR"

# ---- the payload-builder liveness guard, its own failing case: run_hook() refuses an empty payload,
# ---- observed once by handing it one.
before=$fail; run_hook ""; [ "$fail" = $((before+1)) ] && { fail=$before; print_ok "run_hook refuses an empty payload"; } || print_bad "run_hook accepted an empty payload"

n=$((pass+fail))
# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not on the written one. Derived from
# the nine arm blocks each run ALONE from the sourced prologue on node a, 2026-09-20 (the pass that
# wrote this file may not run the suite): 5 7 6 2 5 6 4 3 6 plus the run_hook guard's one, 45
# executed, pinned at ~10% headroom. The main loop's first green at VERIFYING confirms the executed
# count against this floor. Lower it in a reviewed diff or not at all.
FLOOR_ASSERTIONS=40
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; fail=$((fail+1)); }
echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ]
