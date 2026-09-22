#!/usr/bin/env bash
# Runnable check for stop-guard.js — the `Stop` hook that refuses the turn end of a session bound
# to a non-terminal unattended run, bounded per session, with a sidecar line per bound stop.
# Run: bash tools/unattended/stop-guard.test.sh   (exit 0 = all pass)
#
# WITHHELD FROM THE BAR AND FROM ADOPTERS, like every suite in this kit (kit.toml `project-owned`):
# its subject is the hook's decision table and key, which move only when this file's siblings move.
# `run-unattended-gates.sh` enumerates it through its budget row; the main loop runs it at
# VERIFYING. A build pass never runs it — the pass observes each arm by feeding the copied hook
# the arm's payload directly instead (spec TOOL-aWokenSentinel-3 §6).
#
# WHAT THIS FILE DOES NOT CHECK, stated up front because a structural check reads as a semantic
# one to everybody who did not write it: it does not prove the hook is WIRED (the adopter's
# --check arm and check-hook-destinations.sh own that), it does not prove `--liveness` is right
# (unit 2's suite owns that — every arm but one runs a STUB driver that prints a chosen verdict),
# and it does not prove the harness delivers the block reason to the model (measured once in the
# research record, section 6, and not re-measured here).
#
# EVERY ARM DRIVES ITS OWN TREE. The hook keys on a `.git`, a conf and a run-state record, so every
# fixture is a scratch tree carrying exactly those and never the real tree: an arm that inherited
# the real repository would bind or not depending on which session ran it. The hook is COPIED to
# a scratch kit dir beside the stub driver, because the hook spawns `unattended.sh` from its own
# `__dirname` and the stub is what makes the decision observable in milliseconds.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# STOP_GUARD_TEST_TMP is the pass's seam: a unit pass runs one arm at a time from a sourced copy of
# this prologue and must put its scratch under the session scratchpad, not /tmp.
TMP="${STOP_GUARD_TEST_TMP:-$(mktemp -d)}"; trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0
print_ok()   { echo "ok   $1"; pass=$((pass+1)); }
print_bad()  { echo "FAIL $1"; fail=$((fail+1)); }
check_same() { if [ "$2" = "$3" ]; then print_ok "$1"; else print_bad "$1: expected [$3], got [$2]"; fi; }
check_hit()  { if grep -qF -- "$2" <<<"$1"; then print_ok "$3"; else print_bad "$3: missing [$2]"; fi; }
check_miss() { if grep -qF -- "$2" <<<"$1"; then print_bad "$3: found [$2]"; else print_ok "$3"; fi; }

if [ -f "$HERE/../lib/resolve-python.sh" ]; then
  . "$HERE/../lib/resolve-python.sh"
  TESTPY=$(resolve_python) || { echo "stop-guard.test: no usable python"; exit 2; }
else
  TESTPY=python3   # gov:literal-python — last-resort fallback when ../lib/ is absent (adopter layout)
fi
# The payload's `cwd` must be a path node resolves on this host: MSYS spells a scratch dir /tmp/x
# where node wants C:/..., and a cwd node cannot walk keys nothing, which passes every ALLOW arm
# for the wrong reason.
resolve_native() { cygpath -m "$1" 2>/dev/null || printf '%s' "$1"; }

# THE KIT COPY: the hook, its module and a STUB driver that prints the file
# STOP_GUARD_TEST_LIVENESS names on --liveness, exits STOP_GUARD_TEST_LIVENESS_RC, and sleeps
# STOP_GUARD_TEST_LIVENESS_SLEEP seconds first. The sleep's stdio is detached so the hook's bound
# kills the stub rather than waiting on a grandchild holding the pipe.
KIT="$TMP/kit"; mkdir -p "$KIT"
cp "$HERE/stop-guard.js" "$HERE/run-lease.js" "$KIT/" 2>/dev/null
HOOK="$KIT/stop-guard.js"
cat > "$KIT/unattended.sh" <<'EOF'
#!/usr/bin/env bash
[ -n "${STOP_GUARD_TEST_LIVENESS_SLEEP:-}" ] && sleep "$STOP_GUARD_TEST_LIVENESS_SLEEP" >/dev/null 2>&1 </dev/null
[ "${1:-}" = --liveness ] && [ -n "${STOP_GUARD_TEST_LIVENESS:-}" ] && cat "$STOP_GUARD_TEST_LIVENESS"
exit "${STOP_GUARD_TEST_LIVENESS_RC:-0}"
EOF
export STOP_GUARD_TEST_LIVENESS="$TMP/liveness.txt"
unset STOP_GUARD_TEST_LIVENESS_RC STOP_GUARD_TEST_LIVENESS_SLEEP STOP_GUARD_LIVENESS_BOUND_MS
SID="11111111-2222-3333-4444-555555555555"

# set_liveness <phase> <verdict> — what the stub prints, in the driver's own key: value shape.
set_liveness() { printf 'phase: %s\nstate: live\nsession: %s\nverdict: %s\n' "$1" "$SID" "$2" > "$STOP_GUARD_TEST_LIVENESS"; }
# build_fixture <phase> <session-fact> [conf-extra-line] -> a scratch tree: .git/HEAD, a conf, one
# record whose `## Run facts` region carries the phase and the session fact.
build_fixture() {
  local d; d=$(mktemp -d "$TMP/fx.XXXXXX")
  mkdir -p "$d/.git" "$d/memory/builds/fx"
  printf 'ref: refs/heads/fx\n' > "$d/.git/HEAD"
  { printf 'MEMORY_ROOT=memory\n'; [ -n "${3:-}" ] && printf '%s\n' "$3"; } > "$d/.unattended.conf"
  printf '# fx\n\n## Run facts\nwitness: abc\nphase: %s\nsession: %s\n\n## Parked\n' "$1" "$2" > "$d/memory/builds/fx/RUN.md"
  printf '%s' "$d"
}
# build_payload <fixture> [extra-json-object] — BUILT by python, never hand-spliced; the extra object is
# merged over the base so an arm adds `background_tasks`, `agent_id` or `session_crons`.
build_payload() {
  "$TESTPY" -c 'import json,sys
p={"session_id":sys.argv[2],"hook_event_name":"Stop","cwd":sys.argv[1],"stop_hook_active":False}
p.update(json.loads(sys.argv[3]) if len(sys.argv)>3 and sys.argv[3] else {})
print(json.dumps(p))' "$(resolve_native "$1")" "$SID" "${2:-}"
}
# run_hook <payload> — runs the copied hook; OUT, ERR and RC are what it did. THE LIVENESS GUARD: the
# hook exits 0 silently on unparseable stdin by design, so a builder that produced nothing makes
# every ALLOW arm pass for the wrong reason; an empty payload is a failed assertion, never a feed.
run_hook() {
  case "$1" in *'"session_id"'*) ;; *) print_bad "the payload builder produced nothing"; OUT=""; ERR=""; RC=99; return;; esac
  OUT=$(printf '%s' "$1" | node "$HOOK" 2>"$TMP/err"); RC=$?; ERR=$(cat "$TMP/err")
}
derive_sidecar() { printf '%s/.git/unattended/stop.fx.log' "$1"; }
# read_field <file> <key> — the LAST line's value, parsed as JSON, never grepped over raw bytes.
read_field() { "$TESTPY" -c 'import json,sys
ls=[l for l in open(sys.argv[1],encoding="utf-8").read().splitlines() if l.strip()]
v=json.loads(ls[-1])[sys.argv[2]]
print(json.dumps(v) if isinstance(v,(dict,list,bool)) or v is None else v)' "$1" "$2"; }
measure_lines() { grep -c '' "$1" 2>/dev/null || echo 0; }
# extract_reason <stdout> — the `reason` string of the block JSON.
extract_reason() { printf '%s' "$1" | "$TESTPY" -c 'import json,sys;d=json.loads(sys.stdin.read() or "{}");print(d["reason"] if d.get("decision")=="block" else "")'; }
read_now_ms() { "$TESTPY" -c 'import time;print(int(time.time()*1000))'; }
# ---- arms ----------------------------------------------------------------------------------------

# ---- AC1: an unbound session — no record names it — exits 0 silently and writes nothing. The
# ---- record is at BUILDING with `session: absent`, the literal that must never bind.
F=$(build_fixture BUILDING absent); set_liveness BUILDING LIVE
run_hook "$(build_payload "$F")"
check_same "AC1 unbound rc" "$RC" "0"
check_same "AC1 unbound stdout empty" "$OUT" ""
[ ! -e "$(derive_sidecar "$F")" ] && print_ok "AC1 unbound writes no sidecar" || print_bad "AC1 unbound wrote $(derive_sidecar "$F")"
# the literal `absent` is the driver's spelling of "no lease", so a payload whose session_id IS that
# word must not bind the record that carries it
run_hook "$(build_payload "$F" '{"session_id":"absent"}')"
check_same "AC1 the literal absent never binds" "$OUT" ""
[ ! -e "$(derive_sidecar "$F")" ] && print_ok "AC1 the literal absent writes no sidecar" || print_bad "AC1 the literal absent wrote a line"

# ---- AC2: a bound session on an open run is BLOCKED, the reason names the slug, the count and
# ---- --plan, and the sidecar holds one block line with blocks 1.
F=$(build_fixture BUILDING "$SID"); set_liveness BUILDING LIVE
run_hook "$(build_payload "$F")"
check_same "AC2 bound rc" "$RC" "0"
R=$(extract_reason "$OUT")
check_hit "$R" "unattended run fx" "AC2 reason names the slug"
check_hit "$R" "block 1/6" "AC2 reason counts 1 of the default 6"
check_hit "$R" "unattended.sh --plan fx" "AC2 reason names --plan"
check_hit "$R" "phase BUILDING, liveness LIVE" "AC2 reason names phase and verdict"
check_same "AC2 one sidecar line" "$(measure_lines "$(derive_sidecar "$F")")" "1"
check_same "AC2 line decision" "$(read_field "$(derive_sidecar "$F")" decision)" "block"
check_same "AC2 line blocks" "$(read_field "$(derive_sidecar "$F")" blocks)" "1"
check_same "AC2 line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "run-open"
check_same "AC2 line phase" "$(read_field "$(derive_sidecar "$F")" phase)" "BUILDING"
check_same "AC2 line session" "$(read_field "$(derive_sidecar "$F")" session)" "$SID"
# the key order is the spec's table, asserted once on the raw line
check_same "AC2 key order" "$("$TESTPY" -c 'import json,sys;print(" ".join(json.loads(open(sys.argv[1]).read().splitlines()[0]).keys()))' "$(derive_sidecar "$F")")" \
  "utc session decision reason phase verdict blocks background_tasks stop_hook_active session_crons"
# a second stop counts 2, from the file
run_hook "$(build_payload "$F")"
check_hit "$(extract_reason "$OUT")" "block 2/6" "AC2 the second stop counts from the sidecar"
check_same "AC2 two sidecar lines" "$(measure_lines "$(derive_sidecar "$F")")" "2"

# ---- AC3: a TERMINAL verdict allows, and the allow still writes its line.
F=$(build_fixture LANDED "$SID"); set_liveness LANDED TERMINAL
run_hook "$(build_payload "$F")"
check_same "AC3 terminal rc" "$RC" "0"
check_same "AC3 terminal stdout empty" "$OUT" ""
check_same "AC3 line decision" "$(read_field "$(derive_sidecar "$F")" decision)" "allow"
check_same "AC3 line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "terminal"
check_same "AC3 line blocks" "$(read_field "$(derive_sidecar "$F")" blocks)" "0"

# ---- AC4: a pending background task allows — the harness re-invokes the session when it ends.
F=$(build_fixture BUILDING "$SID"); set_liveness BUILDING LIVE
run_hook "$(build_payload "$F" '{"background_tasks":[{"id":"t1"},{"id":"t2"}]}')"
check_same "AC4 background rc" "$RC" "0"
check_same "AC4 background stdout empty" "$OUT" ""
check_same "AC4 line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "background-tasks"
check_same "AC4 line background_tasks" "$(read_field "$(derive_sidecar "$F")" background_tasks)" "2"
run_hook "$(build_payload "$F" '{"background_tasks":[]}')"
check_hit "$(extract_reason "$OUT")" "block 1/6" "AC4 an empty array blocks"

# ---- AC5: the count is read from the sidecar and from nothing else: two seeded block lines for
# ---- this session against a knob of 2 exhaust it; one seeded line blocks 2/2; another session's
# ---- lines never move this session's count.
render_seedline() { printf '{"utc":"2026-09-16T00:00:00Z","session":"%s","decision":"block","reason":"run-open","phase":"BUILDING","verdict":"LIVE","blocks":%s,"background_tasks":0,"stop_hook_active":false,"session_crons":null}\n' "$1" "$2"; }
F=$(build_fixture BUILDING "$SID" 'STOP_GUARD_BLOCKS="2"'); set_liveness BUILDING LIVE
mkdir -p "$F/.git/unattended"; { render_seedline "$SID" 1; render_seedline "$SID" 2; } > "$(derive_sidecar "$F")"
run_hook "$(build_payload "$F")"
check_same "AC5 exhausted rc" "$RC" "0"
check_same "AC5 exhausted stdout empty" "$OUT" ""
check_same "AC5 line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "blocks-exhausted"
check_same "AC5 line blocks" "$(read_field "$(derive_sidecar "$F")" blocks)" "2"
check_miss "$ERR" "declares no STOP_GUARD_BLOCKS" "AC5 a declared knob prints no NOTE"
render_seedline "$SID" 1 > "$(derive_sidecar "$F")"
run_hook "$(build_payload "$F")"
check_hit "$(extract_reason "$OUT")" "block 2/2" "AC5 one seeded line blocks 2/2"
{ render_seedline other-session 1; render_seedline other-session 2; } > "$(derive_sidecar "$F")"
# the seed is asserted before the feed: an empty seed reads 0 and passes the next line vacuously
check_same "AC5 two lines seeded for another session" "$(measure_lines "$(derive_sidecar "$F")")" "2"
run_hook "$(build_payload "$F")"
check_hit "$(extract_reason "$OUT")" "block 1/2" "AC5 another session's lines are not counted"
check_same "AC5 three lines after the third stop" "$(measure_lines "$(derive_sidecar "$F")")" "3"

# ---- AC6: no knob declared — the NOTE once on stderr and the default 6 in the reason; a malformed
# ---- knob ALLOWS with knob-malformed at rc 0, never the driver's exit 2, which is a block.
F=$(build_fixture BUILDING "$SID"); set_liveness BUILDING LIVE
run_hook "$(build_payload "$F")"
check_same "AC6 NOTE once" "$(printf '%s\n' "$ERR" | grep -c 'declares no STOP_GUARD_BLOCKS')" "1"
check_hit "$(extract_reason "$OUT")" "block 1/6" "AC6 the default is 6"
F=$(build_fixture BUILDING "$SID" 'STOP_GUARD_BLOCKS="zero"'); set_liveness BUILDING LIVE
run_hook "$(build_payload "$F")"
check_same "AC6 malformed rc" "$RC" "0"
check_same "AC6 malformed stdout empty" "$OUT" ""
check_same "AC6 line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "knob-malformed"
check_hit "$ERR" "not a positive integer" "AC6 malformed says so on stderr"
F=$(build_fixture BUILDING "$SID" 'export STOP_GUARD_BLOCKS=3 # a comment'); set_liveness BUILDING LIVE
run_hook "$(build_payload "$F")"
check_hit "$(extract_reason "$OUT")" "block 1/3" "AC6 an exported, commented knob line reads 3"

# ---- AC7: an unreadable liveness — a non-zero exit, then no verdict line — allows and says so.
F=$(build_fixture BUILDING "$SID"); set_liveness BUILDING LIVE
STOP_GUARD_TEST_LIVENESS_RC=1 run_hook "$(build_payload "$F")"
check_same "AC7 rc-1 rc" "$RC" "0"
check_same "AC7 rc-1 stdout empty" "$OUT" ""
check_same "AC7 rc-1 line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "liveness-unreadable"
check_same "AC7 rc-1 line verdict" "$(read_field "$(derive_sidecar "$F")" verdict)" "unreadable"
check_same "AC7 rc-1 line phase" "$(read_field "$(derive_sidecar "$F")" phase)" "unknown"
printf 'phase: BUILDING\nstate: live\n' > "$STOP_GUARD_TEST_LIVENESS"
run_hook "$(build_payload "$F")"
check_same "AC7 no-verdict rc" "$RC" "0"
check_same "AC7 no-verdict stdout empty" "$OUT" ""
check_same "AC7 no-verdict line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "liveness-unreadable"
# a missing stub is the same class: the spawn fails, the stop allows
mv "$KIT/unattended.sh" "$KIT/unattended.sh.aside"
run_hook "$(build_payload "$F")"
check_same "AC7 no-driver rc" "$RC" "0"
check_same "AC7 no-driver line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "liveness-unreadable"
mv "$KIT/unattended.sh.aside" "$KIT/unattended.sh"

# ---- AC8: session_crons is copied VERBATIM, and stop_hook_active appends the continuation.
F=$(build_fixture BUILDING "$SID"); set_liveness BUILDING LIVE
CRONS='[{"id":"c1","schedule":"*/10 * * * *","prompt":"tick"},{"id":"c2","schedule":"0 * * * *","prompt":"wake","extra":[1,2]}]'
run_hook "$(build_payload "$F" "{\"session_crons\":$CRONS,\"stop_hook_active\":true}")"
check_same "AC8 crons deep-equal" "$("$TESTPY" -c 'import json,sys
line=json.loads(open(sys.argv[1]).read().splitlines()[-1])
print("same" if line["session_crons"]==json.loads(sys.argv[2]) else "differs")' "$(derive_sidecar "$F")" "$CRONS")" "same"
check_same "AC8 line stop_hook_active" "$(read_field "$(derive_sidecar "$F")" stop_hook_active)" "true"
R=$(extract_reason "$OUT")
check_same "AC8 reason ends with the continuation" "${R##* This is a continuation the hook already blocked once.}" ""
check_hit "$R" "This is a continuation the hook already blocked once." "AC8 continuation sentence present"
run_hook "$(build_payload "$F")"
check_same "AC8 absent crons is null" "$(read_field "$(derive_sidecar "$F")" session_crons)" "null"
check_miss "$(extract_reason "$OUT")" "already blocked once" "AC8 the first stop carries no continuation"

# ---- AC9: a sub-agent-shaped payload never binds: agent_id, then SubagentStop; and the fragment
# ---- registers Stop alone.
F=$(build_fixture BUILDING "$SID"); set_liveness BUILDING LIVE
run_hook "$(build_payload "$F" '{"agent_id":"a-1","agent_type":"worker"}')"
check_same "AC9 agent_id rc" "$RC" "0"
check_same "AC9 agent_id stdout empty" "$OUT" ""
run_hook "$(build_payload "$F" '{"hook_event_name":"SubagentStop"}')"
check_same "AC9 SubagentStop rc" "$RC" "0"
check_same "AC9 SubagentStop stdout empty" "$OUT" ""
[ ! -e "$(derive_sidecar "$F")" ] && print_ok "AC9 neither wrote a line" || print_bad "AC9 a sub-agent payload wrote a line"
check_same "AC9 fragment event Stop" "$(grep -c '"event": "Stop"' "$HERE/stop-guard.fragment.json")" "1"
check_same "AC9 fragment never SubagentStop" "$(grep -c SubagentStop "$HERE/stop-guard.fragment.json")" "0"
# unparseable stdin and an empty session_id are the same silent exit
OUT=$(printf 'not json' | node "$HOOK" 2>/dev/null); RC=$?
check_same "AC9 unparseable stdin rc" "$RC" "0"
check_same "AC9 unparseable stdin stdout empty" "$OUT" ""

# ---- AC10: a worktree's `.git` FILE routes the sidecar to the per-worktree git dir it names.
F=$(build_fixture BUILDING "$SID"); set_liveness BUILDING LIVE
mkdir -p "$F/wt-git"; mv "$F/.git/HEAD" "$F/wt-git/HEAD"; rmdir "$F/.git"
printf 'gitdir: %s\n' "$(resolve_native "$F/wt-git")" > "$F/.git"
run_hook "$(build_payload "$F")"
check_hit "$(extract_reason "$OUT")" "block 1/6" "AC10 the worktree fixture binds and blocks"
[ -f "$F/wt-git/unattended/stop.fx.log" ] && print_ok "AC10 the line landed under the named git dir" || print_bad "AC10 no line under $F/wt-git"
check_same "AC10 exactly one stop.fx.log under the fixture" "$(find "$F" -name 'stop.fx.log' | grep -c '')" "1"

# ---- THE `landing-unstamped` ROW (TOOL-aWokenSentinel-8). `--landed` runs after the lander, so its
# ---- refusals fire when the witness is already on the default branch and `--liveness` reads
# ---- FINISHED-UNSTAMPED; each ends the turn on the promise that this hook continues the session.
# ---- Spec 3's table ALLOWED that verdict, which wedged every wired landing at LANDING (audit B1).
# ---- A bound session at that verdict BLOCKS, bounded by the same knob as `run-open`, and is told
# ---- `--landed` is the one act left — never `--plan`, which sends a finished run to build nothing.
# ---- Observed RED first against the hook at this unit's base, where the stop is allowed.
# ---- U8-AC1: the block, its reason text, and the sidecar line carrying the listing verbatim.
F=$(build_fixture LANDING "$SID"); set_liveness LANDING FINISHED-UNSTAMPED
CRONS='[{"id":"f1209d79","schedule":"*/10 * * * *","prompt":"tick"}]'
run_hook "$(build_payload "$F" "{\"session_crons\":$CRONS}")"
check_same "U8-AC1 finished-unstamped rc" "$RC" "0"
check_same "U8-AC1 the stop is blocked" "$(printf '%s' "$OUT" | "$TESTPY" -c 'import json,sys;print(json.loads(sys.stdin.read() or "{}").get("decision",""))')" "block"
R=$(extract_reason "$OUT")
check_hit "$R" "finished and unstamped" "U8-AC1 reason says finished and unstamped"
check_hit "$R" "unattended.sh --landed fx" "U8-AC1 reason names --landed"
check_hit "$R" "block 1/6" "U8-AC1 reason counts 1 of the default 6"
check_hit "$R" "phase LANDING" "U8-AC1 reason names the phase"
check_miss "$R" "--plan" "U8-AC1 reason never names --plan"
check_miss "$R" "--abort" "U8-AC1 reason never names --abort"
check_same "U8-AC1 line decision" "$(read_field "$(derive_sidecar "$F")" decision)" "block"
check_same "U8-AC1 line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "landing-unstamped"
check_same "U8-AC1 line phase" "$(read_field "$(derive_sidecar "$F")" phase)" "LANDING"
check_same "U8-AC1 line verdict" "$(read_field "$(derive_sidecar "$F")" verdict)" "FINISHED-UNSTAMPED"
check_same "U8-AC1 line crons deep-equal" "$("$TESTPY" -c 'import json,sys
line=json.loads(open(sys.argv[1]).read().splitlines()[-1])
print("same" if line["session_crons"]==json.loads(sys.argv[2]) else "differs")' "$(derive_sidecar "$F")" "$CRONS")" "same"
# ---- U8-AC2: the cap is the shared knob — two seeded landing-unstamped lines against 2 exhaust it,
# ---- one seeded line blocks 2/2; the seed is asserted before the feed.
render_landingline() { printf '{"utc":"2026-09-20T00:00:00Z","session":"%s","decision":"block","reason":"landing-unstamped","phase":"LANDING","verdict":"FINISHED-UNSTAMPED","blocks":%s,"background_tasks":0,"stop_hook_active":false,"session_crons":[]}\n' "$1" "$2"; }
F=$(build_fixture LANDING "$SID" 'STOP_GUARD_BLOCKS="2"'); set_liveness LANDING FINISHED-UNSTAMPED
mkdir -p "$F/.git/unattended"; { render_landingline "$SID" 1; render_landingline "$SID" 2; } > "$(derive_sidecar "$F")"
check_same "U8-AC2 two lines seeded" "$(measure_lines "$(derive_sidecar "$F")")" "2"
run_hook "$(build_payload "$F")"
check_same "U8-AC2 exhausted rc" "$RC" "0"
check_same "U8-AC2 exhausted stdout empty" "$OUT" ""
check_same "U8-AC2 line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "blocks-exhausted"
render_landingline "$SID" 1 > "$(derive_sidecar "$F")"
run_hook "$(build_payload "$F")"
check_hit "$(extract_reason "$OUT")" "block 2/2" "U8-AC2 one seeded line blocks 2/2"
# ---- U8-AC3: a pending background task still allows at this verdict — the harness re-invokes.
F=$(build_fixture LANDING "$SID"); set_liveness LANDING FINISHED-UNSTAMPED
run_hook "$(build_payload "$F" '{"background_tasks":[{"id":"t1"}]}')"
check_same "U8-AC3 background rc" "$RC" "0"
check_same "U8-AC3 background stdout empty" "$OUT" ""
check_same "U8-AC3 line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "background-tasks"
# ---- U8-AC5: an UNBOUND record at LANDING never reaches the row — every pre-unit-1 record in the
# ---- tree keeps ending its turns silently.
F=$(build_fixture LANDING absent); set_liveness LANDING FINISHED-UNSTAMPED
run_hook "$(build_payload "$F")"
check_same "U8-AC5 unbound rc" "$RC" "0"
check_same "U8-AC5 unbound stdout empty" "$OUT" ""
[ ! -e "$(derive_sidecar "$F")" ] && print_ok "U8-AC5 unbound writes no sidecar" || print_bad "U8-AC5 unbound wrote $(derive_sidecar "$F")"

# ---- AC18: the two bounds side by side — the default under the harness cap, the cap pinned at 8.
check_same "AC18 BLOCKS_DEFAULT <= HARNESS_CONSECUTIVE_CAP" \
  "$(node -e 'const m=require(process.argv[1]);console.log(m.BLOCKS_DEFAULT<=m.HARNESS_CONSECUTIVE_CAP?"under":"over")' "$(resolve_native "$HOOK")")" "under"
check_same "AC18 HARNESS_CONSECUTIVE_CAP is 8" "$(node -e 'console.log(require(process.argv[1]).HARNESS_CONSECUTIVE_CAP)' "$(resolve_native "$HOOK")")" "8"
check_same "AC18 the suite is withheld by the descriptor" "$(grep -c 'stop-guard.test.sh' "$HERE/kit.toml")" "1"

# ---- AC19: an unwritable sidecar ALLOWS — a bound the hook cannot derive is one it cannot
# ---- enforce; and a hung liveness is bounded, not waited on.
F=$(build_fixture BUILDING "$SID"); set_liveness BUILDING LIVE
printf 'a file where the directory goes\n' > "$F/.git/unattended"
run_hook "$(build_payload "$F")"
check_same "AC19 unwritable rc" "$RC" "0"
check_same "AC19 unwritable stdout empty" "$OUT" ""
check_hit "$ERR" "sidecar-unwritable" "AC19 unwritable says so on stderr"
check_same "AC19 unwritable wrote nothing" "$(cat "$F/.git/unattended")" "a file where the directory goes"
F=$(build_fixture BUILDING "$SID"); set_liveness BUILDING LIVE
T0=$(read_now_ms)
STOP_GUARD_TEST_LIVENESS_SLEEP=3 STOP_GUARD_LIVENESS_BOUND_MS=500 run_hook "$(build_payload "$F")"
T1=$(read_now_ms)
check_same "AC19 hung liveness rc" "$RC" "0"
check_same "AC19 hung liveness stdout empty" "$OUT" ""
check_same "AC19 hung liveness line reason" "$(read_field "$(derive_sidecar "$F")" reason)" "liveness-unreadable"
[ $((T1 - T0)) -lt 2000 ] && print_ok "AC19 the bound fired within 2 s ($((T1 - T0)) ms)" || print_bad "AC19 the bound did not fire: $((T1 - T0)) ms"

# ---- AC11: ONE arm against the REAL driver, on a `git init` fixture seeded by the adopter suite's
# ---- own seed() — extracted as one function, never the suite — which commits once so HEAD is
# ---- born and the driver's clock probe is live. The line's verdict is whatever the copied driver's
# ---- own --liveness prints, read by the arm, never a literal.
KIT_REL="${KIT_REL:-tools/unattended}"
TR_T=${KIT_REL%/*}; [ "$TR_T" = "$KIT_REL" ] && TR_T=""; [ -z "$TR_T" ] || TR_T="$TR_T/"
eval "$(sed -n '/^seed() {/,/^}/p' "$HERE/adopt-unattended.test.sh")"
FR="$TMP/real"; seed "$FR" >/dev/null 2>&1
mkdir -p "$FR/memory/builds/fx"
printf '# fx\n\n## Run facts\nwitness: abc\nphase: BUILDING\nbranch-ref: refs/heads/main\nsession: %s\npid: absent\n\n## Parked\n' "$SID" > "$FR/memory/builds/fx/RUN.md"
if [ -f "$FR/$KIT_REL/stop-guard.js" ] && [ -f "$FR/$KIT_REL/unattended.sh" ]; then
  REAL_VERDICT=$( cd "$FR" && bash "$KIT_REL/unattended.sh" --liveness fx 2>/dev/null | sed -n 's/^verdict: //p' )
  [ -n "$REAL_VERDICT" ] && print_ok "AC11 the real driver printed a verdict ($REAL_VERDICT)" || print_bad "AC11 the real driver printed no verdict line"
  OUT=$(printf '%s' "$(build_payload "$FR")" | node "$FR/$KIT_REL/stop-guard.js" 2>"$TMP/err"); RC=$?
  check_same "AC11 real-driver rc" "$RC" "0"
  check_hit "$(extract_reason "$OUT")" "block 1/6" "AC11 the real driver's open run blocks"
  check_same "AC11 line verdict is the driver's own" "$(read_field "$(derive_sidecar "$FR")" verdict)" "$REAL_VERDICT"
  check_same "AC11 line phase" "$(read_field "$(derive_sidecar "$FR")" phase)" "BUILDING"
else
  print_bad "AC11 the seed did not place the hook and the driver under $FR/$KIT_REL"
fi

# ---- the payload-builder liveness guard, its own failing case: run_hook() refuses an empty payload,
# ---- observed once by handing it one.
before=$fail; run_hook ""; [ "$fail" = $((before+1)) ] && { fail=$before; print_ok "run_hook refuses an empty payload"; } || print_bad "run_hook accepted an empty payload"

n=$((pass+fail))
# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not on the written one. Derived from
# the thirteen arm blocks each run ALONE from the sourced prologue on node a, 2026-09-20 (the pass
# that wrote this file may not run the suite): 5 14 5 5 9 7 10 6 9 3 3 8 5 plus the run_hook
# guard's one, 90 executed, pinned at ~10% headroom. The main loop's first green at VERIFYING confirms the
# executed count against this floor. Lower it in a reviewed diff or not at all.
# RAISED 80 -> 104 by TOOL-aWokenSentinel-8: the `landing-unstamped` block run ALONE from the sourced
# prologue on node a, 2026-09-20, executed 24 (13 5 3 3), green against the tip and 10 RED against
# the hook at its base 6bb7ac75, where the stop was allowed with `finished-unstamped`.
FLOOR_ASSERTIONS=104
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; fail=$((fail+1)); }
echo "---- $pass passed, $fail failed ----"
# THE TRAILER IS UNCONDITIONAL. `run-selftests.sh --pooled` reads a completed run by its trailer
# (SWEEP_TRAILER_RX); a red-but-complete run that prints only a green-gated `PASS (` is UNTRAILED
# there, writes no calibrate reading, and refuses every later pooled run (aBatchedArm closing D4,
# applied at the merge that brought this suite in).
echo "  ($n assertions executed)"
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ]
