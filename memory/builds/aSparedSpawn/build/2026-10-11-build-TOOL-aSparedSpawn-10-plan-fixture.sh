#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-10
# TOOL-aSparedSpawn-10 (spec rev-3) — the pass-time check of the foreign-prefix leg's classifier.
# It takes the leg's own classifier block (from `SELF_ROW=` up to the `--plan` branch, verbatim), and
# runs the plan branch's five calls against a hand-built git repository holding the REAL unattended
# kit.toml and driver, so the kit's version marker is the shipped one. No arm of any suite runs, no
# clone of gov is made, and the population is a `run-selftests.sh --list` captured once.
#   bash <this> <leg path> <a captured run-selftests.sh --list> <scratch dir> <gov root>
set -u
SUITE="$1"; LIST="$2"; W="$3"; GOV="$4"
step_fail=0
check_step() { if [ "$1" = 0 ]; then echo "ok    $2"; else echo "FAIL  $2"; step_fail=1; fi; }
blk="$W/classifier.sh"
awk '/^SELF_ROW=/ { f = 1 } /^if \[ "\$PLAN" = 1 \]; then/ { f = 0 } f' "$SUITE" > "$blk"
grep -q '^derive_row_kinds()' "$blk"; check_step $? "the extracted block holds derive_row_kinds"
grep -q '^print_plan()' "$blk"; check_step $? "the extracted block holds print_plan"

R="$W/repo"; rm -rf "$R"; mkdir -p "$R/tools/unattended"
git -C "$R" init -q . && git -C "$R" config user.email fx@fx.test && git -C "$R" config user.name fx && git -C "$R" config core.autocrlf false
cp "$GOV/tools/unattended/kit.toml" "$GOV/tools/unattended/unattended.sh" "$R/tools/unattended/"
git -C "$R" add -A && git -C "$R" commit -q -m c1

# The plan branch's calls, in its order, in a fresh shell per run so KIT_BUMP starts empty.
# $1 = what to stage after the classifier is loaded: none | stale | twoprobes
run_plan() {
  ( mode="$1"; ROOT="$R"; TROOT=tools; KIT=run-gates; set --
    source "$blk"
    list=$(<"$LIST")
    [ "$mode" = stale ] && WHOLE_RUN+=("no such row anywhere|a staged stale declaration")
    load_population "$list"
    check_declarations
    derive_row_kinds plan "$TROOT"
    if [ "$mode" = twoprobes ]; then
      for j in "${!R_NAME[@]}"; do [ "${R_KIND[j]}" = represented ] && { R_KIND[j]=probe; break; }; done
    fi
    derive_dispatch_order
    print_plan
    echo "fixture: fails=$fails" )
}

# 1. The root commit has no first parent: every shard of both families is probed.
run_plan none > "$W/p1.txt"
grep -q "has no first parent" "$W/p1.txt"; check_step $? "a HEAD with no first parent says so"
[ "$(grep -c 'every shard is probed' "$W/p1.txt")" = 2 ]; check_step $? "both sharded families probe every shard at a root commit"
grep -q '· represented ·' "$W/p1.txt"; [ $? != 0 ]; check_step $? "no row is represented at a root commit"
grep -q '^fixture: fails=0$' "$W/p1.txt"; check_step $? "the root-commit plan is green"

# 2. A commit that leaves the marker alone rotates: one probe per family, the rest represented.
git -C "$R" commit -q --allow-empty -m c2
run_plan none > "$W/p2.txt"
[ "$(grep -c 'rule input HEAD [0-9a-f]\{40\} as an integer mod 8 = ' "$W/p2.txt")" = 2 ]; check_step $? "each family prints the rule's input, the whole sha and the modulus"
[ "$(grep -c '· represented · by shard [1-8]/8$' "$W/p2.txt")" = 14 ]; check_step $? "fourteen shard rows are represented, seven per family"
[ "$(grep -c '^\[plan\] [0-9]*\. unattended .* shard [1-8]/8 · probe ·' "$W/p2.txt")" = 2 ]; check_step $? "exactly one shard row per family is a probe"
grep -q '^fixture: fails=0$' "$W/p2.txt"; check_step $? "the rotating plan is green"
# The answer is the arithmetic: HEAD's sha mod 8, plus one.
sha=$(git -C "$R" rev-parse HEAD); want=$(python -c "import sys; print(int(sys.argv[1], 16) % 8 + 1)" "$sha")
grep -q "unattended.test.sh' · rule input HEAD $sha as an integer mod 8 = $((want - 1)) · .* probes shard $want/8," "$W/p2.txt"; check_step $? "the representative is HEAD's sha mod 8 plus one, computed independently ($want/8)"
# Whole rows lead the order, by descending budget, before any probe row.
awk -F' · ' '/^\[plan\] [0-9]+\. / { k = $2; b = $3 + 0; if (k == "whole") { if (seenp || (nw && b > last)) bad = 1; last = b; nw++ } else if (k == "probe") seenp = 1 } END { exit (bad || nw == 0) }' "$W/p2.txt"
check_step $? "every whole row is ordered before every probe row, in descending budget"

# 3. A later commit with a different rotation input moves the representative (AC3).
rep2=$(grep -o "unattended.test.sh' · rule input .* probes shard [0-9]*/8" "$W/p2.txt" | grep -o 'shard [0-9]*/8$')
moved=1
for k in 1 2 3 4 5 6 7 8 9 10; do
  git -C "$R" commit -q --allow-empty -m "c3-$k"
  run_plan none > "$W/p3.txt"
  rep3=$(grep -o "unattended.test.sh' · rule input .* probes shard [0-9]*/8" "$W/p3.txt" | grep -o 'shard [0-9]*/8$')
  [ "$rep3" != "$rep2" ] && { moved=0; break; }
done
check_step "$moved" "a commit whose rotation input differs probes another shard ($rep2 -> $rep3)"

# 4. A commit that moves the kit's version marker probes every shard again.
sed -i 's/^KIT_UNATTENDED_VERSION=.*/KIT_UNATTENDED_VERSION="99.0.0-fixture"/' "$R/tools/unattended/unattended.sh"
git -C "$R" commit -q -am bump
run_plan none > "$W/p4.txt"
[ "$(grep -c "version marker moved since HEAD's first parent .*-> KIT_UNATTENDED_VERSION=\"99.0.0-fixture\") · every shard is probed" "$W/p4.txt")" = 2 ]; check_step $? "a version bump probes every shard and prints both markers"
grep -q '^fixture: fails=0$' "$W/p4.txt"; check_step $? "the bump plan is green"

# 5. Staged breaks: a stale WHOLE_RUN entry, and a second probe row forced into one family (AC6).
git -C "$R" commit -q --allow-empty -m c5
run_plan stale > "$W/p5.txt"
grep -q '^FAIL  a whole-run declaration names no row in the population: no such row anywhere$' "$W/p5.txt"; check_step $? "a stale WHOLE_RUN entry reds naming it"
grep -q '^fixture: fails=1$' "$W/p5.txt"; check_step $? "the stale entry is the plan's one failure"
run_plan twoprobes > "$W/p6.txt"
grep -q "^FAIL  the family '.*' has 2 probe row(s) where the rule answers 1$" "$W/p6.txt"; check_step $? "a second probe row forced into one family reds"
grep -q '^fixture: fails=1$' "$W/p6.txt"; check_step $? "the forced probe is the plan's one failure"
echo "fixture: $([ "$step_fail" = 0 ] && echo GREEN || echo RED)"
exit "$step_fail"
