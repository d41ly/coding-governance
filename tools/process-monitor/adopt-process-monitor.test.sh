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
PASS=0; FAIL=0
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK" 2>/dev/null || true' EXIT

add_pass()  { PASS=$((PASS + 1)); printf '  add_pass   %s\n' "$1"; }
add_fail()  { FAIL=$((FAIL + 1)); printf '  FAIL %s\n' "$1" >&2; }
check_equal() { if [ "$2" = "$3" ]; then add_pass "$1"; else add_fail "$1 (got '$2', wanted '$3')"; fi; }

# A conf with every key valid. Arms mutate ONE key off this.
build_base_conf() {
  cat <<'CONF'
PROCMON_ROOTS="C:/projects/somewhere-real /c/projects/somewhere-real"
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
  mkdir -p "$repo/tools/process-monitor"
  git -C "$repo" init -q 2>/dev/null
  cp "$ADOPT" "$repo/tools/process-monitor/"
  [ "$conf_body" = "__ABSENT__" ] || printf '%s\n' "$conf_body" > "$repo/.process-monitor.conf"
  ( cd "$repo" && bash tools/process-monitor/adopt-process-monitor.sh --check ) >"$WORK/out" 2>&1
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

# --- ...and the NARROW declaration is admitted, which is the direction a one-way guard breaks
check_equal "test_narrow_root_is_admitted" \
    "$(run_against "$(build_base_conf | sed 's|^PROCMON_ROOTS=.*|PROCMON_ROOTS="/c/projects/a-real-long-path"|')")" 0

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
( cd "$_repo" && bash tools/process-monitor/adopt-process-monitor.sh --check ) >/dev/null 2>&1 || true
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
  ( cd "$ROOT" && bash tools/process-monitor/adopt-process-monitor.sh --check ) >/dev/null 2>&1 \
    && add_pass "test_shipped_conf_is_accepted" || add_fail "test_shipped_conf_is_accepted"
else
  add_fail "test_shipped_conf_is_accepted (add_fail shipped conf — the arm cannot run, and a skip here would be indistinguishable from coverage)"
fi

printf '\nadopt-process-monitor: %d passed, %d failed (%d assertions)\n' "$PASS" "$FAIL" "$((PASS + FAIL))"
[ "$FAIL" -eq 0 ] || exit 1
