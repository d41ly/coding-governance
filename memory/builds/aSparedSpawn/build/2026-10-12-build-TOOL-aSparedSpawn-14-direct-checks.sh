#!/usr/bin/env bash
# The direct checks TOOL-aSparedSpawn-14's pass ran: the changed driver and leg invoked directly, each
# once, over the tree or over a staged break. No suite, no bar, no slice of a suite.
#   bash memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-14-direct-checks.sh <scratch dir>
# Run from the repository root. The scratch dir receives a copy of the unattended kit, whose driver
# each check-52 break is staged into; the real driver is never edited. Prints every observed line
# under a `==` label; the acceptance ledger reads them. check-arms' own breaks are the sibling
# `-arm-breaks.py`, run against check-arms.py beside a staged copy of it.
set -u
S=${1:?a scratch directory}
K="$S/kit"; rm -rf "$K"; mkdir -p "$K"; cp -r tools/unattended/. "$K/"
D="$K/unattended.sh"; cp "$D" "$D.orig"
export GOV_RUNLOG=0

echo "== row 1 replay: a verb on a slug with no run-state file"
bash tools/unattended/unattended.sh --status aNoSuchRun 2>&1; echo "rc=$?"
echo "== row 2 replay: --park with no --item, refused by the shared reader before any write"
bash tools/unattended/unattended.sh --park aSparedSpawn --reason "a direct check" 2>&1; echo "rc=$?"
echo "== row 2: usage renders VERB_REQUIRES row for row (diff of the render against the source text)"
diff <(bash tools/unattended/unattended.sh 2>&1 | sed -n '/^required flags, per verb:$/,$p' | sed '1d; s/^  //') \
     <(sed -n '/^VERB_REQUIRES="/,/"$/p' tools/unattended/unattended.sh | sed 's/^VERB_REQUIRES="//; s/"$//') \
  && echo "identical"
echo "== row 5 replay: a scratch call of print_env_failure from the sourced driver"
bash -c '. tools/unattended/unattended.sh; print_env_failure 99 "a scratch environment failure the helper prints"; echo "not reached"' 2>&1
echo "rc=$?"

leg52() { GOV_UNATTENDED_REPORT=1 bash "$K/check-unattended.sh" --only 52 2>&1 | grep -E 'check 52' \
            | sed 's/.*covers its condition: /FAILED, hits: /'; }
stage() { # label · awk program over the pristine driver copy
  awk "$2" "$D.orig" > "$D"; echo "== $1"; leg52; cp "$D.orig" "$D"
}
stage "row 1 / AC8: a scratch verb tests its run-state file and refuses by itself" '
  { print } END { print "c52probe() {"; print "  runmd_of \"$1\" >/dev/null; rel=$_runmd"
                  print "  [ -f \"$rel\" ] || { fail 99 \"a scratch verb refusing a missing record by itself\"; return 1; }"; print "}" }'
stage "AC8 near-miss: the same test on a variable not named from _runmd stays silent" '
  { print } END { print "c52probe() {"; print "  rel=$1"
                  print "  [ -f \"$rel\" ] || { fail 99 \"a scratch verb refusing a missing file of its own\"; return 1; }"; print "}" }'
stage "AC8: a per-site message back under another number" '
  { print } END { print "c52probe() {"; print "  fail 98 \"no run-state file, so there is no scratch run: $1\""; print "}" }'
stage "AC9: a listed flag whose call is gone" '/check_verb_flag --park --reason/ { next } { print }'
stage "AC9: a call the table does not list" '
  { print } /check_verb_flag --park --item/ { print "  check_verb_flag --park --step \"$item\" || return 1" }'
stage "row 4 / AC10: a claim mode in a case arm CLAIM_MODES lacks" '
  { print } /^  case "\$mode:\$cls" in/ { print "    scratch:mine) CW_ACT=renew ;;" }'
stage "AC10: a read class in a case arm CLAIM_READS lacks" '
  { print } /^  case "\$mode:\$cls" in/ { print "    holder:foreign-scratch) CW_ACT=take ;;" }'
stage "AC10: a caller passing an undeclared mode" '
  { print } END { print "c52probe() { check_claim_writable \"$1\" scratchmode a b c; }" }'
stage "check 52 liveness: no VERB_REQUIRES row" '/^VERB_REQUIRES="/ { skip = 1 } skip { if ($0 ~ /"$/) skip = 0; next } { print }'
stage "control: the pristine driver" '{ print }'

# ROW 15's REPLAY IS NOT HERE. It needs the leg's core run - checks 1 to 27 are one unit - over a conf
# naming the retired key and not its replacement, and that run passed the pass's 600 s bound on node a
# and was stopped unread, the conf restored from its copy. It is OWED at VERIFYING, where the leg suite's
# check-22 report arm (TOOL-aWindowedPass-5 AC3) and check-23 budget arm observe both survivors.
rm -rf "$K"
