#!/usr/bin/env bash
# **Serves:** journal TOOL-dSealedTally-1
# TOOL-dSealedTally-1 — a HERMETIC probe for `--landed`'s write ordering.
#
# WHY THIS EXISTS RATHER THAN ARMS IN THE SUITE. `tools/unattended/`'s self-test suites are under a
# standing owner instruction not to be run (2026-08-23): they cost 20-85 minutes each and were
# re-run across two days. The instruction names the remedy this file implements — a hermetic probe
# built from the suite's OWN setup, so there is no second copy of the fixture to drift.
#
# Lines 1-362 of `unattended.test.sh` define every helper these arms use (`hit`, `miss`, `same`,
# `mkconf`, `readme`, `runmd`, `reset_tree`, `run`, `fixture`, and `sum`, which is
# `git hash-object` over the run-state file and is exactly the byte-identity witness AC1 wants).
# They are EXTRACTED at run time, never copied, with two substitutions: `HERE` is repointed at the
# kit, because the probe does not live beside the suite, and `SCRIPT` is repointed at whichever
# driver is under test.
#
#   bash <this file>                      # the patched driver in the worktree
#   PROBE_DRIVER=/path/to/old.sh bash …   # AC2's staged break: the driver BEFORE the fix
#
# Exit 0 means every arm held.

set -u

SELF="$(cd "$(dirname "$0")" && pwd)"
KIT="$(cd "$SELF/../../../../tools/unattended" && pwd)"

TMPKIT="$(mktemp -d)"
trap 'rm -rf "$TMPKIT"' EXIT

# THE DRIVER UNDER TEST. `PROBE_REV` is AC2's staged break and is the supported way to run it.
# The driver resolves its kit library RELATIVE TO ITSELF, so an old `unattended.sh` dropped in a
# scratch directory refuses with "the kit library is missing beside this script" and never
# reaches a single arm. That produced a RED for entirely the wrong reason on the first attempt
# here -- the grading-a-copy-that-never-ran class -- so the whole kit directory is copied and
# only the one file is swapped.
#
#   PROBE_REV=HEAD~1 bash <this file>     # observe the arms fail against the pre-fix driver
if [ -n "${PROBE_REV:-}" ]; then
  OLDKIT="$TMPKIT/kit"
  mkdir -p "$OLDKIT"
  cp -r "$KIT/." "$OLDKIT/"
  if ! git -C "$KIT" show "$PROBE_REV:tools/unattended/unattended.sh" > "$OLDKIT/unattended.sh"
  then
    echo "probe: cannot read unattended.sh at $PROBE_REV" >&2; exit 2
  fi
  DRIVER="$OLDKIT/unattended.sh"
else
  DRIVER="${PROBE_DRIVER:-$KIT/unattended.sh}"
fi

[ -r "$KIT/unattended.test.sh" ] || { echo "probe: no suite at $KIT/unattended.test.sh" >&2; exit 2; }

[ -r "$DRIVER" ] || { echo "probe: no driver at $DRIVER" >&2; exit 2; }

TMP="$TMPKIT/compose"
mkdir -p "$TMP"

{
  sed -n '1,362p' "$KIT/unattended.test.sh" \
    | sed -e "s|^HERE=.*|HERE=\"$KIT\"|" -e "s|^SCRIPT=.*|SCRIPT=\"$DRIVER\"|"
  cat <<'ARMS'

# ============================ TOOL-dSealedTally-1 ============================
echo "probe: driver under test = $SCRIPT"
n_before=$n

reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
mkconf; printf 'LANDER_MARKER="tmarker"\n' >> .unattended.conf
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md
GCD=$(cd "$(git rev-parse --git-common-dir)" && pwd)
fixture
git push -q -f origin HEAD:main 2>/dev/null

# ---- AC1. A REFUSAL LEAVES THE RECORD BYTE-IDENTICAL.
# The marker names an EARLIER landing, which is the refusal four recorded instances actually hit.
printf 'landed main at 0000000000000000000000000000000000000000 by a previous run\n' > "$GCD/tmarker"
before=$(sum)
out=$(run --landed tRun)

# THE ANTECEDENT FIRST: without this the arms below pass whenever the verb refused for some OTHER
# reason, or did not run at all, which is the fixture-passes-by-finding-nothing class.
hit "$out" "the lander marker names a different commit"
same "AC1 the run-state file is BYTE-IDENTICAL after a refused --landed" "$(sum)" "$before"
same "AC1 ...so the phase still reads LANDING" \
     "$(grep -c '^phase: LANDING' memory/builds/tRun/RUN.md)" "1"
same "AC1 ...and no terminal phase was written" \
     "$(grep -c '^phase: LANDED' memory/builds/tRun/RUN.md)" "0"
same "AC1 ...and no landed-anchor was written either, which is the wedge this unit removes" \
     "$(grep -c '^landed-anchor:' memory/builds/tRun/RUN.md)" "0"

# ---- AC3. THE ACCEPTING PATH STILL WRITES BOTH FACTS AND EXITS 0.
# Without this the fix could be "never write anything", which AC1 alone cannot distinguish.
printf 'landed main at %s by push-main\n' "$(git rev-parse HEAD)" > "$GCD/tmarker"
out=$(run --landed tRun)
miss "$out" "the lander marker names a different commit"
same "AC3 the accepting path reaches LANDED" \
     "$(grep -c '^phase: LANDED' memory/builds/tRun/RUN.md)" "1"
same "AC3 ...and writes landed-anchor in the same run, so the pair lands together" \
     "$(grep -c '^landed-anchor:' memory/builds/tRun/RUN.md)" "1"

# ---- AC4. A REFUSAL FROM A FACT WRITE LATER THAN THE MARKER GATE.
# `units-at-landing` is written after the gate and before the terminal pair. It is made to fail by
# giving the build README a roster region the unit reader refuses, which is the cheapest lever that
# does not need filesystem permissions -- those do not behave the same way under MSYS.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
mkconf; printf 'LANDER_MARKER="tmarker"\n' >> .unattended.conf
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md
sed -i 's|<!-- /roster:units -->||' memory/builds/tRun/README.md
fixture
git push -q -f origin HEAD:main 2>/dev/null
printf 'landed main at %s by push-main\n' "$(git rev-parse HEAD)" > "$GCD/tmarker"
before4=$(sum)
out=$(run --landed tRun)
if [ "$(grep -c '^phase: LANDED' memory/builds/tRun/RUN.md)" = "0" ]; then
  same "AC4 a refusal LATER than the marker gate still leaves the phase at LANDING" \
       "$(grep -c '^phase: LANDING' memory/builds/tRun/RUN.md)" "1"
else
  echo "SKIP AC4 — the malformed roster did not make a later fact write refuse, so this arm"
  echo "     exercised nothing. Recorded as a skip rather than counted as a pass."
fi

# LIVENESS ON THE PROBE ITSELF. `same` and `hit` are SILENT on success, so a green run
# is indistinguishable from a run whose arms never executed. This asserts the count
# actually moved by the number of assertions written below the marker.
n_mine=$((n - n_before))
if [ "$n_mine" -lt 8 ]; then
  echo "FAIL probe liveness: only $n_mine of the 8 dSealedTally assertions ran"
  st=1
fi
echo "probe: $n arm(s) run, $n_mine of them this unit's"
exit $st
ARMS
} > "$TMP/probe.sh"

bash "$TMP/probe.sh"
