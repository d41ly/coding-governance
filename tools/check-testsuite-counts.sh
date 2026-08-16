#!/usr/bin/env bash
# check-testsuite-counts.sh — TOOL-cSettledDocket-5. Every self-test the BAR runs must print an
# executed assertion count, in one agreed shape, against a shrink-only floor.
#
#   bash tools/check-testsuite-counts.sh    # silent + exit 0 = good
#
# WHY. `TOOL-cBriefedPilot-23` gave three suites a runtime count and a floor, after one of them had
# printed a hardcoded `PASS (130 assertions)` for its whole life with no counter behind it. The floor
# is what catches a block of arms stranded past an `exit` — the defect that shipped nine dead arms
# while `check-arms.py` certified all nine as armed, because it grades TEXT and not EXECUTION.
#
# Measured when this leg was written: 27 tracked `*.test.sh`, 12 printing no count at all, four
# different spellings among the 15 that did, and 3 floors. So the floor guarded three suites out of
# twenty-seven and there was no agreed shape for a leg to check. Per-suite editing has no end and no
# ratchet: the twenty-eighth suite lands silent and nobody notices.
#
# THE POPULATION IS DERIVED from `tools/gate-legs.json`, never hand-kept. A hand-maintained second
# list is how `check-kit-versions.sh` grew a duplicate assertion that printed two messages for one
# defect, and the manifest is already the single source for what the bar runs — `run-gates.test.sh`
# treats it that way. A suite nobody runs has no count worth checking.
#
# IT RUNS NOTHING. Executing 27 suites to read their output would re-run the whole bar inside one
# leg; the shape is asserted by reading the file, which costs milliseconds.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "testsuite-counts: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
MANIFEST=tools/gate-legs.json
WAIVERS=memory/project/testsuite-count-waivers.txt
status=0
fail() { echo "TESTSUITE-COUNTS FAILED — $1"; status=1; }

[ -f "$MANIFEST" ] || { echo "testsuite-counts: no $MANIFEST, so the population would be empty and this leg would pass by finding nothing"; exit 2; }

# Every `*.test.sh` the manifest names, deduplicated. Selected from the argv strings rather than by
# globbing the tree, so the leg's population and the bar's are the same set by construction.
suites=$(grep -oE '"[^"]*\.test\.sh"' "$MANIFEST" | tr -d '"' | sort -u)
if [ -z "$suites" ]; then
  fail "the gate manifest names no *.test.sh, so this leg would grade an empty population — the vacuous-selector shape it exists to prevent"
  exit "$status"
fi

# The registry is SHRINK-ONLY: a row leaves when its suite complies. Seeded from a measured
# population so the leg lands green; a leg with twelve silent exceptions checks nothing, a leg with
# twelve NAMED ones ratchets.
waived=""
[ -f "$WAIVERS" ] && waived=$(grep -vE '^[[:space:]]*(#|$)' "$WAIVERS" || true)

compliant() { # file -> 0 when it prints the agreed shape AND pins a floor
  grep -qE 'echo "PASS \(\$[A-Za-z_][A-Za-z0-9_]* assertions\)"' "$1" \
    && grep -qE '^FLOOR_ASSERTIONS=[0-9]+$' "$1"
}

while IFS= read -r f; do
  [ -n "$f" ] || continue
  is_waived=0
  case "
$waived
" in *"
$f
"*) is_waived=1 ;; esac
  if [ ! -f "$f" ]; then
    fail "the gate manifest names a self-test this leg cannot read, and skipping it silently removes it from the population: $f"
    continue
  fi
  if compliant "$f"; then
    # A STALE waiver reds. A row whose suite now complies silently widens the surface it was written
    # to narrow — the same rule `install-prefix-waivers.txt` already carries.
    [ "$is_waived" = 0 ] || fail "a testsuite-count waiver names a suite that now complies, so the list has stopped shrinking and the row hides nothing: $f in $WAIVERS"
  else
    if [ "$is_waived" = 0 ]; then
      if grep -qE '^FLOOR_ASSERTIONS=[0-9]+$' "$f"; then
        fail "a self-test pins a floor but does not print the agreed count line, so nothing compares the floor to anything: $f wants echo \"PASS (\$n assertions)\""
      else
        fail "a self-test on the bar prints no executed assertion count against a floor, so a block of its arms could be stranded past an exit and the suite would still report success: $f"
      fi
    fi
  fi
done <<EOF
$suites
EOF

# A waiver naming a path the manifest does not run is dead weight pointing at nothing.
if [ -n "$waived" ]; then
  while IFS= read -r w; do
    [ -n "$w" ] || continue
    case "
$suites
" in *"
$w
"*) ;;
      *) fail "a testsuite-count waiver names a suite the gate manifest does not run, so it waives nothing and outlives what it was written for: $w" ;;
    esac
  done <<EOF
$waived
EOF
fi

exit "$status"
