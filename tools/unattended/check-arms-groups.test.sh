#!/usr/bin/env bash
# check-arms-groups.test.sh — arms for the structural group linter. TOOL-aBatchedArm-2.
#
#   bash <kit>/check-arms-groups.test.sh    # "PASS (…assertions)" + exit 0 = good
#
# EVERY RED IS OBSERVED ON A PLANTED COPY. The linter is a static scan, so each rule's failing case is
# a violation planted into a scratch copy of the tracked suite and the copy is discarded — the
# AGENTS.md §7 rule that a gate is not landed until its failing case has been seen, and it costs
# seconds. The tracked suite is run too, for its header and its liveness line, and its own verdict is
# PRINTED here and never taken as this suite's: the spec's §3 forbids waiving a pre-existing
# violation and the starting figures are the unit's acceptance ledger's to record, so a leg that
# adopted that verdict would be red by design on its first day. What this suite grades is the LINTER.
# NO `tools/<kit>/` LITERAL: both paths are derived from this file's own directory, because the
# install-prefix leg bans a kit file naming its own directory and a sibling is not this kit's to spell.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
LINT="$HERE/check-arms-groups.sh"
SUITE="$HERE/check-unattended.test.sh"
[ -f "$LINT" ] || { echo "FAIL cannot find check-arms-groups.sh beside this test"; exit 2; }
[ -f "$SUITE" ] || { echo "FAIL cannot find check-unattended.test.sh beside this test"; exit 2; }
T=$(mktemp -d) || exit 2
trap 'rm -rf "$T"' EXIT
st=0; n=0
check_has()   { n=$((n+1)); case "$2" in *"$3"*) echo "ok   $1" ;; *) echo "FAIL $1 -- output did not carry '$3'"; st=1 ;; esac; }
check_lacks() { n=$((n+1)); case "$2" in *"$3"*) echo "FAIL $1 -- output carried '$3' and must not"; st=1 ;; *) echo "ok   $1" ;; esac; }
check_same()  { n=$((n+1)); if [ "$2" = "$3" ]; then echo "ok   $1"; else echo "FAIL $1 -- got '$2' want '$3'"; st=1; fi; }
measure_rule() { printf '%s\n' "$2" | grep -c "^RED rule $1 " || true; }   # rule letter · output

# ---- the tracked suite: header, liveness, a verdict that is 0 or 1 and never a refusal ------------
base=$(bash "$LINT" "$SUITE"); brc=$?
echo "     tracked verdict (reported, not graded): $(printf '%s\n' "$base" | tail -1) · exit $brc"
check_has  "T0 the header names what the linter does NOT grade (AC5)" "$base" "does NOT grade"
check_has  "T0 the delimiter set is resolved from the file and names reset_tree" "$base" "delimiter set resolved from the file: reset_tree"
check_has  "T0 the liveness line reports the boundary and group counts (S4)" "$base" "boundaries "
groups=$(printf '%s\n' "$base" | sed -n 's/^check-arms-groups: boundaries [0-9]* ([0-9]* seams) · groups \([0-9]*\) .*/\1/p')
seams=$(printf '%s\n' "$base" | sed -n 's/^check-arms-groups: boundaries [0-9]* (\([0-9]*\) seams).*/\1/p')
n=$((n+1)); [ "${groups:-0}" -gt 0 ] 2>/dev/null && echo "ok   T0 the tracked suite parses into groups ($groups)" || { echo "FAIL T0 the tracked suite parsed into no groups: '$groups'"; st=1; }
n=$((n+1)); [ "${seams:-0}" -gt 0 ] 2>/dev/null && echo "ok   T0 the region seams are boundaries ($seams)" || { echo "FAIL T0 no in_shard seam was counted: '$seams'"; st=1; }
n=$((n+1)); case "$brc" in 0|1) echo "ok   T0 the tracked run is a verdict (exit $brc), not a refusal" ;; *) echo "FAIL T0 the tracked run exited $brc — a refusal over the real suite"; st=1 ;; esac
check_lacks "T0 a run with findings or a green one never prints REFUSED" "$base" "REFUSED"
bA=$(measure_rule A "$base"); bB=$(measure_rule B "$base"); bC=$(measure_rule C "$base")
echo "     starting figures over the tracked suite: rule A $bA · rule B $bB · rule C $bC"

# ---- plants. The locator is the first `check_emitted` call — the first BATCHED group — and a plant is one
# ---- line inserted after it, so every expected line number is that locator plus one.
E=$(grep -n '^check_emitted ' "$SUITE" | head -1 | cut -d: -f1)
[ -n "$E" ] || { echo "FAIL the tracked suite carries no check_emitted call to plant beside, so rules A and B cannot be staged"; exit 2; }
E1=$((E+1))
write_planted() { # <copy> · <after line> · <line text>   — inserts one line after the given line number
  awk -v at="$2" -v txt="$3" '{ print } NR == at { print txt }' "$SUITE" > "$1"
}

# ---- AC1 · rule A: a control moved into a batched group reds, naming the arm, the group and the rule
write_planted "$T/a.sh" "$E" 'miss "$out" "planted control inside a batched group"'
o=$(bash "$LINT" "$T/a.sh"); rc=$?
check_same "AC1 a miss inside a batched group is RED" "$rc" "1"
check_same "AC1 exactly one rule-A finding is added" "$(measure_rule A "$o")" "$((bA + 1))"
check_has  "AC1 the finding names the arm's line, the helper and rule A" "$o" "RED rule A · group at line "
check_has  "AC1 the finding names the planted line" "$o" "· line $E1: miss "
write_planted "$T/a2.sh" "$E" 'same "planted equality inside a batched group" "$out" ""'
o=$(bash "$LINT" "$T/a2.sh")
check_same "AC1 a same inside a batched group is rule A too" "$(measure_rule A "$o")" "$((bA + 1))"
# the negative: the same control inside a SOLO group is not rule A's business
R=$(grep -n '^reset_tree$' "$SUITE" | head -1 | cut -d: -f1)
write_planted "$T/a3.sh" "$R" 'miss "$out" "planted control inside a solo group"'
o=$(bash "$LINT" "$T/a3.sh")
check_same "AC1 a miss inside a solo group adds no rule-A finding" "$(measure_rule A "$o")" "$bA"

# ---- AC2 · rule B: two arms with one text in one group red, naming both lines
H=$(sed -n "${E1}p" "$SUITE")
case "$H" in hit\ *) ;; *) echo "FAIL the line after the first check_emitted call is not a hit line, so the duplicate cannot be planted: $H"; exit 2 ;; esac
write_planted "$T/b.sh" "$E1" "$H"
o=$(bash "$LINT" "$T/b.sh"); rc=$?
check_same "AC2 a duplicated assertion text in one group is RED" "$rc" "1"
check_same "AC2 exactly one rule-B finding is added" "$(measure_rule B "$o")" "$((bB + 1))"
check_has  "AC2 the finding names both line numbers" "$o" "· lines $E1 $((E1 + 1)): 2 arms carry one text"

# ---- AC3 · rule C: a run capture assigned to a foreign name reds; the group's own out does not
write_planted "$T/c.sh" "$E" '_foreign=$(GOV_UNATTENDED_REPORT=1 run)'
o=$(bash "$LINT" "$T/c.sh"); rc=$?
check_same "AC3 a capture under a foreign name is RED" "$rc" "1"
check_same "AC3 exactly one rule-C finding is added" "$(measure_rule C "$o")" "$((bC + 1))"
check_has  "AC3 the finding names the capture, its line and rule C" "$o" "RED rule C · group at line "
check_has  "AC3 the finding names the planted line and name" "$o" "· line $E1: capture \`_foreign\`"
write_planted "$T/c2.sh" "$E" 'out=$(GOV_UNATTENDED_REPORT=1 run)'
o=$(bash "$LINT" "$T/c2.sh")
check_same "AC3 a capture into the group's own out adds no rule-C finding" "$(measure_rule C "$o")" "$bC"

# ---- AC4 · liveness: a file that parses into no groups REFUSES and never prints a clean verdict
printf 'reset_tree() { git reset -q --hard "$P"; git clean -qfd; }\n# a definition and nothing else\n' > "$T/empty.sh"
o=$(bash "$LINT" "$T/empty.sh"); rc=$?
check_same "AC4 zero groups exits 2" "$rc" "2"
check_has  "AC4 zero groups says it graded nothing" "$o" "graded nothing"
check_lacks "AC4 zero groups never prints GREEN" "$o" "GREEN"
printf 'reset_tree() { git checkout -q main; }\nreset_tree\nhit "$out" "x"\n' > "$T/noset.sh"
o=$(bash "$LINT" "$T/noset.sh"); rc=$?
check_same "AC4 an empty delimiter set exits 2" "$rc" "2"
check_has  "AC4 an empty delimiter set is named as the refusal" "$o" "delimiter set is EMPTY"
check_lacks "AC4 an empty delimiter set never prints GREEN" "$o" "GREEN"
o=$(bash "$LINT" "$T/does-not-exist.sh"); rc=$?
check_same "AC4 a missing file exits 2" "$rc" "2"
check_has  "AC4 a missing file is refused by name" "$o" "REFUSED"

# ---- the green path, so a verdict of 0 is observed as well as the reds
printf 'reset_tree() { git reset -q --hard "$P"; }\nif in_shard 1; then\nreset_tree\nout=$(run)\nhit "$out" "a"\nreset_tree\nout=$(GOV_UNATTENDED_REPORT=1 run)\ncheck_emitted "a|b" "$out"\nhit "$out" "a"\nhit "$out" "b"\nfi\n' > "$T/clean.sh"
o=$(bash "$LINT" "$T/clean.sh"); rc=$?
check_same "GREEN a clean file exits 0" "$rc" "0"
check_has  "GREEN a clean file prints GREEN with its counts" "$o" "GREEN — 0 findings over 3 groups and 3 arms"
check_has  "GREEN the batched group and its non-sentinel set are counted" "$o" "· batched 1 · sentinels 0"

# ---- the delimiter is DERIVED: a new reset helper, and a wrapper that calls it, are boundaries
W=$(grep -n '^wreset() ' "$SUITE" | head -1 | cut -d: -f1)
[ -n "$W" ] || { echo "FAIL the tracked suite defines no wreset to plant beside"; exit 2; }
awk -v at="$W" -v e="$E" '{ print }
  NR == at { print "myreset() { git reset -q --hard \"$WP\"; }"; print "mywrap() { myreset; }" }
  NR == e  { print "mywrap"; print "miss \"$out\" \"planted after a transitive reset helper\"" }' "$SUITE" > "$T/d.sh"
o=$(bash "$LINT" "$T/d.sh")
check_has  "DELIM a planted hard-reset helper joins the resolved set" "$o" " myreset"
check_has  "DELIM a helper that calls it joins the set transitively" "$o" " mywrap"
check_same "DELIM the wrapper's call opens a new group, so the control after it is not rule A" "$(measure_rule A "$o")" "$bA"

# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, measured when this suite was written:
# every arm above ran, and a block stranded past an exit would lower it.
FLOOR_ASSERTIONS=35
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }
# THE TRAILER IS UNCONDITIONAL: a red-but-complete run must still carry one, or the pooled runner
# reads it as untrailed and writes no reading (aBatchedArm closing D4).
echo "  ($n assertions executed)"
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
