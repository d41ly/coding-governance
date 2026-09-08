#!/usr/bin/env bash
# adopt-process-monitor.test.sh — the adopter's refusals, each staged and observed RED.
#
# gov:kit process-monitor@0.1
#
# Every arm here stages a break into a SCRATCH copy of the conf and asserts the adopter refuses.
# Nothing is asserted about the shipped tree except by the two arms that say so, because a suite
# that only ever runs against a green tree is an assertion about nothing.
#
#   bash tools/process-monitor/adopt-process-monitor.test.sh
#
# Exit 0 = all arms passed · 1 = an arm failed.
set -u

KIT_DIR="$(cd "$(dirname "$0")" && pwd)"
ADOPT="$KIT_DIR/adopt-process-monitor.sh"
ROOT="$(cd "$KIT_DIR" && git rev-parse --show-toplevel)"
# The kit's own prefix, DERIVED — a scratch adopter tree is built at it, and spelling it out
# is exactly the literal the install-prefix ban refuses.
KIT_REL="$(cd "$KIT_DIR" && git rev-parse --show-prefix)"; KIT_REL="${KIT_REL%/}"
# The floor the merge bar's `check-testsuite-counts.sh` reads: a suite that prints no
# executed count against a declared floor could strand a block of its arms past an exit and
# still report success.
FLOOR_ASSERTIONS=31
PASS=0; FAIL=0
WORK="$(mktemp -d)"
REALROOT="$WORK/declared-root-under-test"
mkdir -p "$REALROOT"
trap 'rm -rf "$WORK" 2>/dev/null || true' EXIT

add_pass()  { PASS=$((PASS + 1)); printf '  ok   %s\n' "$1"; }
add_fail()  { FAIL=$((FAIL + 1)); printf '  FAIL %s\n' "$1" >&2; }
check_equal() { if [ "$2" = "$3" ]; then add_pass "$1"; else add_fail "$1 (got '$2', wanted '$3')"; fi; }

# A conf with every key valid. Arms mutate ONE key off this.
build_base_conf() {
  # The roots must be REAL DIRECTORIES: the adopter tests for one, which is the half of the
  # split-root defect no predicate over the string can catch. `$REALROOT` is created per scratch
  # repo below.
  cat <<CONF
PROCMON_ROOTS="$REALROOT"
PROCMON_AGE_CEILING="14400"
PROCMON_SPIN_RATE="0.5"
PROCMON_REAP_MODE="reap-orphans"
PROCMON_THROTTLE_S="300"
PROCMON_BACKEND=""
CONF
}

# Run the adopter against a scratch repo holding $1 as its conf. Echoes the exit code.
# The scratch repo is a real git repo because the adopter derives its own path through git.
run_against() {
  local conf_body="$1" repo="$WORK/r$RANDOM$RANDOM"
  mkdir -p "$repo/tools/process-monitor" "$REALROOT"
  git -C "$repo" init -q 2>/dev/null
  cp "$ADOPT" "$repo/tools/process-monitor/"
  [ "$conf_body" = "__ABSENT__" ] || printf '%s\n' "$conf_body" > "$repo/.process-monitor.conf"
  # A COMPLETE adoption, because --check now refuses an unwired hook: a fixture that omitted the
  # settings entry would pin the permissive exit the closing review flagged.
  mkdir -p "$repo/.claude"
  printf '%s\n' '{"hooks":{"PostToolUse":[{"matcher":"Bash|PowerShell","hooks":[{"type":"command","command":"node procmon-hook.js"}]}]}}' > "$repo/.claude/settings.json"
  ( cd "$repo" && bash "$KIT_REL/adopt-process-monitor.sh" --check ) >"$WORK/out" 2>&1
  echo $?
}

echo "adopt-process-monitor: refusals"

# --- the happy path, so every refusal below is a CONTRAST and not the only thing observed
check_equal "test_valid_conf_is_accepted" "$(run_against "$(build_base_conf)")" 0

# --- AC2: a blank roots list is a refusal, not an empty set
check_equal "test_blank_roots_refuses" \
    "$(run_against "$(build_base_conf | sed 's|^PROCMON_ROOTS=.*|PROCMON_ROOTS=""|')")" 1
grep -q "blank roots list is a REFUSAL" "$WORK/out" \
  && add_pass "test_blank_roots_names_the_key" || add_fail "test_blank_roots_names_the_key"

# --- AC8: add_fail declared root may be the system temp directory or an ancestor of it
# Forward-slashed BEFORE it reaches any replacement: TMP/TEMP hold backslashes on Windows and GNU
# sed reads \U, \L and friends in the REPLACEMENT as case-conversion escapes, so this arm silently
# declared a mangled path that was not the temp root and the refusal correctly did not fire. awk
# with a -v binding, because it does add_fail escape processing on the value at all. The adopter
# normalises separators itself, so a forward-slashed value exercises the same rule.
_tmp="$(printf '%s' "${TMPDIR:-${TMP:-${TEMP:-/tmp}}}" | tr '\' '/')"
check_equal "test_temp_root_refuses" \
    "$(run_against "$(build_base_conf | awk -v r="$_tmp" '/^PROCMON_ROOTS=/{print "PROCMON_ROOTS=\"" r "\""; next} {print}')")" 1
grep -q "system temp directory or an ancestor" "$WORK/out" \
  && add_pass "test_temp_root_names_the_reason" || add_fail "test_temp_root_names_the_reason"

# --- containment tested BOTH ways: a root that claims everything
check_equal "test_filesystem_root_refuses" \
    "$(run_against "$(build_base_conf | sed 's|^PROCMON_ROOTS=.*|PROCMON_ROOTS="/"|')")" 1
check_equal "test_short_root_refuses" \
    "$(run_against "$(build_base_conf | sed 's|^PROCMON_ROOTS=.*|PROCMON_ROOTS="/c/x"|')")" 1

# ...and the NARROW declaration is admitted, which is the direction a one-way guard breaks.
# A real, DEEPER directory. `$REALROOT` inside SINGLE quotes reached the conf unexpanded, so
# the adopter refused a literal dollar-sign string and the arm read as a guard defect rather
# than as its own quoting bug.
mkdir -p "$REALROOT/deeper/still"
check_equal "test_narrow_root_is_admitted" \
    "$(run_against "$(build_base_conf | awk -v r="$REALROOT/deeper/still" '/^PROCMON_ROOTS=/{print "PROCMON_ROOTS=\"" r "\""; next} {print}')")" 0

# --- the closed value sets
check_equal "test_mode_outside_the_set_refuses" \
    "$(run_against "$(build_base_conf | sed 's|^PROCMON_REAP_MODE=.*|PROCMON_REAP_MODE="destroy-all"|')")" 1
check_equal "test_unset_mode_refuses" \
    "$(run_against "$(build_base_conf | grep -v PROCMON_REAP_MODE)")" 1
check_equal "test_non_numeric_ceiling_refuses" \
    "$(run_against "$(build_base_conf | sed 's|^PROCMON_AGE_CEILING=.*|PROCMON_AGE_CEILING="4h"|')")" 1
check_equal "test_non_numeric_throttle_refuses" \
    "$(run_against "$(build_base_conf | sed 's|^PROCMON_THROTTLE_S=.*|PROCMON_THROTTLE_S="5m"|')")" 1

# --- AC3: an absent conf refuses, and --check REPAIRS NOTHING
check_equal "test_absent_conf_refuses" "$(run_against "__ABSENT__")" 1
_repo="$WORK/norepair"; mkdir -p "$_repo/tools/process-monitor"; git -C "$_repo" init -q 2>/dev/null
cp "$ADOPT" "$_repo/tools/process-monitor/"
( cd "$_repo" && bash "$KIT_REL/adopt-process-monitor.sh" --check ) >/dev/null 2>&1 || true
[ -f "$_repo/.process-monitor.conf" ] \
  && add_fail "test_check_refuses_without_repairing (a conf was created)" \
  || add_pass "test_check_refuses_without_repairing"

# --- AC7: version_from must name a file THIS unit ships, and must resolve
grep -q '^KIT_PROCESS_MONITOR_VERSION=' "$ADOPT" \
  && add_pass "test_version_from_names_a_file_this_unit_ships" \
  || add_fail "test_version_from_names_a_file_this_unit_ships"
[ "$(grep -c '^KIT_PROCESS_MONITOR_VERSION=' "$ADOPT")" = "1" ] \
  && add_pass "test_version_marker_is_unique" || add_fail "test_version_marker_is_unique"

# --- AC6: the README states what the kit does NOT check
if grep -qi '^## What this kit does NOT check' "$KIT_DIR/README.md" 2>/dev/null; then
  add_pass "test_readme_states_what_it_does_not_check"
else
  add_fail "test_readme_states_what_it_does_not_check"
fi

# --- AC8 over the SHIPPED conf, not a fixture: this repo's own declaration must obey the rule
if [ -f "$ROOT/.process-monitor.conf" ]; then
  ( cd "$ROOT" && bash "$KIT_REL/adopt-process-monitor.sh" --check ) >/dev/null 2>&1 \
    && add_pass "test_shipped_conf_is_accepted" || add_fail "test_shipped_conf_is_accepted"
else
  add_fail "test_shipped_conf_is_accepted (add_fail shipped conf — the arm cannot run, and a skip here would be indistinguishable from coverage)"
fi

# ---- TOOL-aReapedSpinner-5: the session seam -------------------------------------------------
# Three DISTINGUISHABLE states, and keeping them apart is the unit's whole job: clean is SILENT,
# flagged is a short list, and a broken monitor is ONE named line. Collapsing the first and third is
# how "nothing to report" becomes indistinguishable from "the probe could not run".
HOOK="$KIT_DIR/procmon-hook.js"
GD=$(git -C "$ROOT" rev-parse --git-common-dir 2>/dev/null)
run_hook() { printf '%s' "$1" | CLAUDE_PROJECT_DIR="$ROOT" PROCMON_PYTHON="${2:-python}" node "$HOOK" 2>&1; }

if [ -f "$HOOK" ] && command -v node >/dev/null 2>&1; then
  rm -f "$GD/procmon-stamp" 2>/dev/null
  _out=$(run_hook '{"hook_event_name":"PostToolUse"}')
  if [ -z "$_out" ]; then add_pass "test_clean_is_silent"; else add_fail "test_clean_is_silent (got: $_out)"; fi

  # The stamp is written AFTER the work: a hook that stamps first throttles itself out of ever
  # running again the moment it crashes, and that silence reads exactly like a clean tree.
  if [ -f "$GD/procmon-stamp" ]; then add_pass "test_stamp_is_written_after_the_run"; else add_fail "test_stamp_is_written_after_the_run"; fi

  # The throttled path must spawn NOTHING. Shimming python to a name that cannot exist proves it:
  # had the early exit run a census, this would report the failure instead of staying silent.
  _out=$(run_hook '{"hook_event_name":"PostToolUse"}' nonesuch-python-shim)
  if [ -z "$_out" ]; then add_pass "test_throttled_path_spawns_nothing"; else add_fail "test_throttled_path_spawns_nothing (got: $_out)"; fi

  # SessionStart ignores the window: a fresh session inherits another session's stamp, and that is
  # precisely how a two-day-old orphan goes unseen.
  _out=$(run_hook '{"hook_event_name":"SessionStart"}' nonesuch-python-shim)
  case "$_out" in
    *"could NOT run"*) add_pass "test_session_start_ignores_the_throttle" ;;
    *) add_fail "test_session_start_ignores_the_throttle (got: $_out)" ;;
  esac

  # A broken monitor names the failure and STILL exits 0 — a monitoring fault may not block a tool
  # call, and a silent failure is the one outcome this unit exists to prevent.
  rm -f "$GD/procmon-stamp" 2>/dev/null
  _out=$(run_hook '{"hook_event_name":"PostToolUse"}' nonesuch-python-shim); _rc=$?
  case "$_out" in
    *"could NOT run"*) add_pass "test_broken_monitor_names_the_failure" ;;
    *) add_fail "test_broken_monitor_names_the_failure (got: $_out)" ;;
  esac
  if [ "$_rc" = 0 ]; then add_pass "test_broken_monitor_fails_open"; else add_fail "test_broken_monitor_fails_open (rc=$_rc)"; fi
  rm -f "$GD/procmon-stamp" 2>/dev/null

  if grep -q 'procmon-hook.js' "$KIT_DIR/kit.toml"; then
    add_pass "test_hook_destination_is_declared_by_the_unit_that_ships_it"
  else
    add_fail "test_hook_destination_is_declared_by_the_unit_that_ships_it"
  fi

  _n=$(grep -c 'procmon-hook' "$ROOT/.claude/settings.json" 2>/dev/null || true)
  if [ "$_n" = 2 ]; then add_pass "test_wiring_is_idempotent (2 entries)"; else add_fail "test_wiring_is_idempotent (found ${_n:-0}, wanted 2)"; fi
else
  add_fail "the session-seam arms could not run (no hook file or no node) — a skip here would be indistinguishable from coverage"
fi

printf '\nadopt-process-monitor: %d passed, %d failed (%d assertions)\n' "$PASS" "$FAIL" "$((PASS + FAIL))"
# ---- the five arms units 5 and 6 name and nothing implemented -------------------------------
# A flagged census, staged by lowering the ceiling in a scratch conf rather than by waiting for a
# real process to age past four hours.
_pmdir="$WORK/flagged"; mkdir -p "$_pmdir/$(dirname "$KIT_REL")"
# The hook resolves reap.py under its OWN root, so this fixture needs the kit, not just a conf.
cp -r "$KIT_DIR" "$_pmdir/$KIT_REL"
git -C "$_pmdir" init -q 2>/dev/null
sed 's|^PROCMON_AGE_CEILING=.*|PROCMON_AGE_CEILING="1"|' "$ROOT/.process-monitor.conf" > "$_pmdir/.process-monitor.conf"
rm -f "$GD/procmon-stamp" 2>/dev/null
_out=$(printf '%s' '{"hook_event_name":"SessionStart"}' | CLAUDE_PROJECT_DIR="$_pmdir" node "$HOOK" 2>&1)
case "$_out" in
  *"past the declared ceiling"*) add_pass "test_hook_reports_a_flagged_row" ;;
  *) add_fail "test_hook_reports_a_flagged_row (got: ${_out:-<silence>})" ;;
esac

# The second run inside the window must be silent AND must not spawn a census. Shimming python to a
# name that cannot exist proves the second half: had it run one, the failure would print.
rm -f "$GD/procmon-stamp" 2>/dev/null
run_hook '{"hook_event_name":"PostToolUse"}' >/dev/null 2>&1
_out=$(run_hook '{"hook_event_name":"PostToolUse"}' nonesuch-python-shim)
if [ -z "$_out" ]; then add_pass "test_throttle_suppresses_the_second_run"; else add_fail "test_throttle_suppresses_the_second_run (got: $_out)"; fi

# A census that never answers must not block the tool call: the hook bounds it and exits 0.
rm -f "$GD/procmon-stamp" 2>/dev/null
# THE HOOK'S CENSUS BOUND, exercised through the real path. A shim on PROCMON_PYTHON cannot do
# it: node's execFileSync refuses a .cmd without shell:true (CVE-2024-27980), so the shim never
# ran and the arm passed in 0s over a bound it had not touched. What the hook actually bounds is
# the reap.py under its own root, so the fixture supplies one that sleeps.
_slowdir="$WORK/slowroot"; mkdir -p "$_slowdir/$KIT_REL"
git -C "$_slowdir" init -q 2>/dev/null
cp "$ROOT/.process-monitor.conf" "$_slowdir/.process-monitor.conf"
printf 'import time\ntime.sleep(600)\n' > "$_slowdir/$KIT_REL/reap.py"
rm -f "$GD/procmon-stamp" 2>/dev/null
_t0=$(date +%s)
_out=$(printf '%s' '{"hook_event_name":"PostToolUse"}' | CLAUDE_PROJECT_DIR="$_slowdir" timeout 200 node "$HOOK" 2>&1); _rc=$?
_t1=$(date +%s)
_el=$((_t1 - _t0))
# It must have actually WAITED — a sub-10s return means the census never started, and a
# bounding assertion over that certifies nothing.
if [ "$_el" -lt 10 ]; then
  add_fail "test_hung_census_does_not_block_the_hook (returned in ${_el}s; the census never ran, so no bound was exercised)"
elif [ "$_rc" = 0 ] && [ "$_el" -lt 180 ]; then
  add_pass "test_hung_census_does_not_block_the_hook (bounded at ${_el}s, exit 0)"
else
  add_fail "test_hung_census_does_not_block_the_hook (rc=$_rc after ${_el}s)"
fi
rm -f "$GD/procmon-stamp" 2>/dev/null

# The declared hole's DISCHARGE PROBE is the adopter's own --check, and a probe nobody staged a
# failure for is a probe that cannot fail.
check_equal "test_roots_hole_probe_fails_when_blank" \
    "$(run_against "$(build_base_conf | sed 's|^PROCMON_ROOTS=.*|PROCMON_ROOTS=""|')")" 1

# The SHIPPED conf, not a fixture: this repo's own declaration must obey the temp-root rule.
if grep -q '^PROCMON_ROOTS=' "$ROOT/.process-monitor.conf"; then
  ( cd "$ROOT" && bash "$KIT_REL/adopt-process-monitor.sh" --check ) >/dev/null 2>&1 \
    && add_pass "test_shipped_roots_exclude_the_temp_root" \
    || add_fail "test_shipped_roots_exclude_the_temp_root"
else
  add_fail "test_shipped_roots_exclude_the_temp_root (no shipped conf to grade)"
fi

n=$((PASS + FAIL))
[ "$n" -ge "$FLOOR_ASSERTIONS" ] \
  || { echo "adopt-process-monitor: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; FAIL=$((FAIL + 1)); }
[ "$FAIL" = 0 ] && echo "PASS ($n assertions)"
[ "$FAIL" -eq 0 ] || exit 1
