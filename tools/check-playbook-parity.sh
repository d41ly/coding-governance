#!/usr/bin/env bash
# check-playbook-parity.sh — the playbook's claims about THIS repo, machine-checked.
#
#   bash tools/check-playbook-parity.sh
#
# Exit 0 = every claim holds · 1 = a claim disagrees with its source · 2 = the gate could not run.
#
# WHY. Every other unit of this build corrected a hand-kept claim that drifted from its source, and
# four of those defects were RECURRENCES of ones a previous build had already fixed. This gate holds
# the three classes that recurred:
#
#   S1 kit coverage      — every tracked kit dir under tools/ is named in a playbook file or waived.
#   S2 value parity      — a value the playbook STATES equals the source that OWNS it.
#   S3 catalogue         — the placeholder counts customize.md states equal the measured sets.
#
# WHAT IT DOES NOT DO, said here rather than implied away: it holds STRUCTURAL claims only. A fluent
# paraphrase that is subtly wrong still passes. Checking prose for accuracy in general is undecidable
# and this gate does not pretend otherwise.
#
# ANTI-VACUITY IS THE LOAD-BEARING CONSTRAINT. `parallel-coding-governance.domain-rules.md` names the
# failure this gate is most likely to have: "a coverage check that greps for a literal the real code
# never spells … matches the empty set and passes checking nothing." Three arms guard it:
#   1. every S2 pair must extract a NON-EMPTY value on BOTH sides, or it reds as unresolvable;
#   2. the S1 kit set must be non-empty AND contain the frozen sentinel `memory-tree`;
#   3. the sibling self-test proves each arm reds, by feeding it a synthetic violation.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "playbook-parity: not a git tree"; exit 2; }
cd "$ROOT" || exit 2

TEMPLATE=coding-governance-agents.template.md
# The charter converged to ONE file at v3.0, so the kit-coverage haystack is the charter PLUS the
# runbook, which is where the kit-adoption prose moved. TWO variables and a two-file precondition:
# with no precondition on the runbook, an absent one reds every kit with a wrong reason instead of
# exiting 2 with the right one.
RUNBOOK=WIRE-INTO-PROJECT.md
WAIVERS=${PLAYBOOK_KIT_WAIVERS:-tools/playbook-kit-waivers.txt}
SENTINEL=memory-tree

status=0
fail() { printf 'PLAYBOOK-PARITY check %s FAILED — %s\n' "$1" "$2"; status=1; }

for f in "$TEMPLATE" "$RUNBOOK"; do
  [ -f "$f" ] || { echo "playbook-parity: missing playbook file: $f"; exit 2; }
done

# ================================================================= S1 — kit coverage ============
# The kit set is DERIVED from the tree, never hand-listed. Same derivation check-install-prefix.sh
# and the codebase-map extractor already use — a third enumeration would be a third thing to drift.
kits=$(git ls-files -- 'tools/*/*' | awk -F/ 'NF>2 {print $2}' | sort -u)

# ARM 2 of the anti-vacuity set. An empty or broken derivation must red by NAME rather than report
# universal coverage: with no kits, "every kit is documented" is vacuously true.
if [ -z "$kits" ]; then
  fail 1 "the kit derivation returned an empty set, so coverage would pass by checking nothing"
elif ! printf '%s\n' "$kits" | grep -qx "$SENTINEL"; then
  fail 2 "the kit derivation lost its frozen sentinel member, so the derivation is broken rather than the tree being empty: expected to find $SENTINEL"
fi

# AC9: the registry is CONSUMED here and owned elsewhere. Absent, this gate stops rather than
# creating one — a gate that seeds its own waiver list can waive whatever it cannot check.
if [ ! -f "$WAIVERS" ]; then
  fail 3 "the kit waiver registry is absent and this gate never creates it: expected $WAIVERS"
  printf 'PLAYBOOK-PARITY: stopping — S1 cannot be evaluated without the registry.\n'
  exit 1
fi

waived=$(grep -vE '^[[:space:]]*(#|$)' "$WAIVERS" | awk '{print $1}' | sort -u)

# The match is an anchored PATH SEGMENT, case-sensitive — `tools/<kit>/` or a backticked `<kit>/` —
# never a bare substring. A substring search scores the kit `lib` many times over the trio — every
# hit inside "deliberate"/"deliberately" or "stdlib", none of them about `tools/lib/` — and would
# certify it documented on that evidence. That is the vacuous-selector shape this gate exists to
# prevent, committed by the gate itself. No count is written here: the figure was measured at 7
# when this comment was drafted and was 9 by the time the build landed, which is the same
# stale-count defect one file over.
named_in_playbook() { # <kit>
  grep -qE "tools/$1/|\`$1/\`" "$TEMPLATE" "$RUNBOOK" 2>/dev/null
}

for k in $kits; do
  if named_in_playbook "$k"; then continue; fi
  if printf '%s\n' "$waived" | grep -qx "$k"; then continue; fi
  fail 4 "a kit ships and the playbook never names it, with no waiver row to excuse it: $k"
done

# AC6, both arms. The registry must be able to GROW — a missing kit reds, so an experimental kit
# needs an escape hatch — which is why it drains through these two arms instead of a shrink-only pin.
for w in $waived; do
  if ! printf '%s\n' "$kits" | grep -qx "$w"; then
    fail 5 "a waiver row names a kit that no longer exists, so the row excuses nothing and is stale: $w"
  elif named_in_playbook "$w"; then
    fail 6 "a waiver row names a kit the playbook DOES document, so the row excuses nothing: $w"
  fi
done

# ============================================================== S2 — value parity ===============
# A declared pair list: each row names a value the playbook STATES and the source that OWNS it, plus
# the extraction for each side. In-script rather than a data file (§8 F1) — it reuses the seam
# kit-dogfood-parity.PAIRS already establishes, and a data file would split one mechanism in two.
#
#   <label>~<stated-file>~<stated-extraction>~<owning-file>~<owning-extraction>
#
# The field separator is `~` and NOT `|`, because one of the values being compared is the hook
# matcher `Workflow|Agent` and its extraction regex therefore contains a pipe. With `|` as the
# delimiter that row silently reparsed into the wrong fields and the gate reported "the owning
# source does not exist: ]*)`.*/\1/p" — a real failure for a fake reason, which is worse than
# either a pass or an honest red. `~` appears in none of these patterns.
PAIRS="
lens-array bound~$TEMPLATE~sed -n 's/.*array LITERAL of ≤\([0-9]\+\) elements.*/\1/p'~tools/hooks/agent-cap.js~sed -n 's/^const MAX_LENSES = \([0-9]\+\).*/\1/p'
agent-cap hook matcher~$TEMPLATE~sed -n 's/.*matcher \`\([A-Za-z|]*\)\`.*/\1/p'~.claude/settings.json~sed -n 's/.*\"matcher\": \"\(Workflow[^\"]*\)\".*/\1/p'
"

# The pair loop runs in a subshell (it is the right-hand side of a pipe), so its findings have to
# cross a process boundary. That crossing is now CHECKED at both ends: unchecked, an unwritable
# TMPDIR made both redirections fail silently and the gate reported "pairs in agreement" with
# rc=0 over injected drift — this stage passing by finding nothing, which is the exact class the
# gate exists to catch, in the gate.
PPTMP="${TMPDIR:-/tmp}/pp.$$"
if ! : > "$PPTMP" 2>/dev/null || [ ! -w "$PPTMP" ]; then
  fail 14 "the value-parity stage could not create its results file, so no pair was compared and this gate must not report agreement: $PPTMP"
  printf 'PLAYBOOK-PARITY: stopping — S2 cannot be evaluated without a writable results file.\n'
  exit 1
fi
{
printf '%s\n' "$PAIRS" | while IFS='~' read -r label sfile sx ofile ox; do
  [ -n "${label:-}" ] || continue
  [ -f "$ofile" ] || { printf 'PAIRFAIL~%s~the owning source does not exist: %s\n' "$label" "$ofile"; continue; }
  sval=$(eval "$sx" < "$sfile" 2>/dev/null | head -1 | tr -d '[:space:]')
  oval=$(eval "$ox" < "$ofile" 2>/dev/null | head -1 | tr -d '[:space:]')
  # ARM 1 of the anti-vacuity set, and the reason this loop cannot report ok by finding nothing.
  if [ -z "$sval" ] || [ -z "$oval" ]; then
    printf 'PAIRFAIL~%s~an extraction matched NOTHING, so the pair was never compared (stated=%s owned=%s)\n' \
      "$label" "${sval:-<empty>}" "${oval:-<empty>}"
  elif [ "$sval" != "$oval" ]; then
    printf 'PAIRFAIL~%s~the playbook states %s where %s owns %s\n' "$label" "$sval" "$ofile" "$oval"
  fi
done
printf 'PAIRSTAGE-RAN\n'
} > "$PPTMP"
# A SENTINEL proves the stage actually ran. The loop always emits it, so an empty results file
# means the subshell died or its output was lost — indistinguishable, from here, from "no pair
# disagreed", which is why it cannot be allowed to read as success.
if ! grep -q '^PAIRSTAGE-RAN$' "$PPTMP" 2>/dev/null; then
  fail 15 "the value-parity stage produced no completion sentinel, so its results were lost rather than empty and no pair was actually compared"
fi
while IFS='~' read -r tag label msg; do
  [ "$tag" = "PAIRFAIL" ] || continue
  fail 7 "a declared value pair disagrees with the source that owns it. Pair $label, detail: $msg"
done < "$PPTMP"
rm -f "$PPTMP"

# The success line reads ONLY what the surviving stages assign. The catalogue stage above
# assigned three counters this line used to print, and the script runs under `set -u` — so
# deleting that stage without rewriting this line killed the gate with an unbound-variable
# error instead of a verdict, which is the named-failure contract this tree enforces everywhere.
[ "$status" -eq 0 ] && printf 'playbook-parity OK — %s kit(s) documented or waived · pairs in agreement\n' \
  "$(printf '%s\n' "$kits" | grep -c .)"
exit "$status"
