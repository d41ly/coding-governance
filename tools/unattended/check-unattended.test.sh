#!/usr/bin/env bash
# Fixture self-test for check-unattended.sh — every branch armed by a POSITIVE assertion naming its
# own failure text, and every RED arm paired with a GREEN control. Silence proves nothing on its
# own: a check that was never reached is silent for the same reason a passing one is.
#
#   bash tools/unattended/check-unattended.test.sh    # "PASS (…assertions)" + exit 0 = good
#
# ONE scratch repo, rebuilt to a pristine state between arms. The kit is COPIED in rather than run
# from the source tree, because the leg resolves its own install prefix and the parity arm depends
# on that prefix being the scratch repo's, not this one's.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP" "${ORIGIN_DIR:-}"' EXIT
st=0; n=0
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }
miss() { n=$((n+1)); if grep -qF -- "$2" <<<"$1"; then echo "FAIL unexpected: $2"; st=1; fi; }
same() { n=$((n+1)); [ "$2" = "$3" ] || { echo "FAIL $1: expected [$3], got [$2]"; st=1; }; }

cd "$TMP" || exit 2
git init -q -b main . && git config user.email t@t.test && git config user.name t \
  && git config core.autocrlf false
mkdir -p tools/unattended memory/guides
cp "$HERE/check-unattended.sh" "$HERE/unattended.sh" "$HERE/PROTOCOL.template.md" tools/unattended/
cp "$HERE/PROTOCOL.template.md" memory/guides/UNATTENDED-PROTOCOL.md
SCRIPT="$TMP/tools/unattended/check-unattended.sh"

mkconf() { cat > .unattended.conf <<EOF
MEMORY_ROOT=memory
LANDER="echo land"
BYPASS_BAN="--no-verify"
GATE_CMD="true"
WIRING_CHECK="true"
CORE_FLOOR="${FLOOR_OVERRIDE:-$CORE_FLOOR_DERIVED}"
KEEPALIVE_CREATE="CronCreate"
KEEPALIVE_DELETE="CronDelete"
PHASES_EXTRA="${1-}"
DOD_EXTRA="${2-}"
EOF
}

build() { # slug
  mkdir -p "memory/builds/$1"
  cat > "memory/builds/$1/README.md" <<EOF
---
slug: $1
node: a
opened: 2026-08-01
streams: architecture
roster: ARCH
ids: ARCH-$1-1
---

# $1

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s)
<!-- /gen:build-index -->
EOF
  cat > "memory/builds/$1/RUN.md" <<EOF
# $1 — run state

<!-- run:generated -->
<!-- /run:generated -->

## Mandate
<!-- run:mandate -->
The owner authorizes $1 to merge and to push.
<!-- /run:mandate -->

## Run facts
phase: RUNNING
witness: WITNESS
base: BASE
EOF
}

CORE_FLOOR_DERIVED="$(grep '^PHASES_CORE=' "$HERE/unattended.sh" | tr -d '
' | sed 's/^PHASES_CORE="//; s/"$//' | wc -w):$(grep '^DOD_CORE=' "$HERE/unattended.sh" | tr -d '
' | sed 's/^DOD_CORE="//; s/"$//' | wc -w)"
mkconf; build tRun
git add -A && git commit -q -m base --no-verify
# A REMOTE-TRACKING anchor: check 9 measures against `refs/remotes/...` only, because a bare local
# branch is a ref the run can move with `git branch -f` — a reproduced way to make BASE equal HEAD.
# It lives OUTSIDE the work tree, or `git clean -qfd` in reset_tree deletes it.
ORIGIN_DIR=$(mktemp -d); ORIGIN="$ORIGIN_DIR/origin.git"
git init -q --bare "$ORIGIN" && git remote add origin "$ORIGIN" && git push -q origin main
ANCHOR0=$(git rev-parse main)
git checkout -q -b unit
git commit -q --allow-empty -m "unit work" --no-verify
BASE0=$(git rev-parse HEAD)
export GOV_DEFAULT_BRANCH=main
sed -i "s/^witness: WITNESS$/witness: $(git rev-parse HEAD)/" memory/builds/tRun/RUN.md
sed -i "s/^base: BASE$/base: $(git merge-base origin/main HEAD)/" memory/builds/tRun/RUN.md
git add -A && git commit -q -m facts --no-verify
PRISTINE=$(git rev-parse HEAD)
# RESETS THE REF NAMESPACE TOO, not just the work tree. Arms below repoint the anchor and add
# replace refs, and a `reset --hard` undoes none of that — the damage leaks into every later arm and
# green controls quietly start measuring something else. Batched through one `update-ref --stdin`
# because a git process per ref per arm dominates this suite's wall time. `--no-deref`, or deleting
# the symbolic `origin/HEAD` deletes the ref it POINTS AT instead of itself.
reset_tree() {
  git reset -q --hard "$PRISTINE"; git clean -qfd
  { git for-each-ref --format='delete %(refname)' refs/remotes/ refs/replace/ \
      | grep -v ' refs/remotes/origin/main$'
    printf 'update refs/remotes/origin/main %s\n' "$ANCHOR0"
  } | git update-ref --stdin --no-deref
}
run() { bash "$SCRIPT" 2>&1; }

# ---- THE GREEN CONTROL, first. Every red arm below is worthless if the clean tree is not clean:
# ---- a leg that reds on everything arms every branch and checks nothing.
out=$(run); rc=$?
same "a conforming tree exits 0" "$rc" "0"
same "a conforming tree prints nothing" "$out" ""

# ---- check 1, all three branches: no conf, a key undeclared, and the driver's core sets unreadable.
reset_tree; rm -f .unattended.conf
hit "$(run)" "no .unattended.conf at the repo root, and every value this leg checks is declared there"

reset_tree; sed -i 's/^LANDER=.*/LANDER=""/' .unattended.conf
out=$(run)
hit "$out" "a required key is undeclared in .unattended.conf, and an undeclared value is not a defaulted one"
hit "$out" "LANDER"

reset_tree; sed -i 's/^PHASES_CORE=.*/PHASES_CORE=unparseable/' tools/unattended/unattended.sh
hit "$(run)" "cannot read the kit's core sets from the driver, so every membership check below would pass over an empty set"

# ---- checks 2 and 3: the CORE sets are one-directional. Deleting a member reds; ADDING a project
# ---- member is green — and that green half is the arm that keeps the check from being "the sets
# ---- must be exactly the core sets", which would make PHASES_EXTRA and DOD_EXTRA unusable.
reset_tree; sed -i 's/^PHASES_CORE="[^"]*"/PHASES_CORE=""/' tools/unattended/unattended.sh
hit "$(run)" "cannot read the kit's core sets from the driver, so every membership check below would pass over an empty set"

# ---- The floor is a COUNT because the membership form was measured VACUOUS: the leg composes the
# ---- effective set as core plus extras, so core is a subset by construction and "every core member
# ---- is present" can never fail. It armed cleanly and tested nothing. These arms delete a core
# ---- member from the DRIVER — the only place the names live — and watch the count fall.
reset_tree
# reset_tree's `git clean -qfd` removes the copied kit, so the arm re-stages it before editing.
# Without this the sed edits nothing, the grep counts nothing, and the arm passes by finding nothing.
mkdir -p tools/unattended && cp "$HERE/unattended.sh" tools/unattended/unattended.sh
ncore=$(grep '^PHASES_CORE=' tools/unattended/unattended.sh | tr -d '
' | sed 's/^PHASES_CORE="//; s/"$//' | wc -w)
short=$(grep '^PHASES_CORE=' tools/unattended/unattended.sh | tr -d '
' | sed 's/^PHASES_CORE="//; s/"$//')
sed -i "s|^PHASES_CORE=.*|PHASES_CORE=\"${short% *}\"|" tools/unattended/unattended.sh
out=$(run)
hit "$out" "the kit's CORE phase vocabulary has shrunk below its floor, and deleting a core member is a silent, reason-free override of everything keyed on it"
hit "$out" "$((ncore-1)) against $ncore"
# ...the member deleted was a TERMINAL one, so the independent terminal-membership check fires too.
# Two sets declared separately, so THAT one is falsifiable where the subset form was not.
hit "$out" "a TERMINAL phase is not in the effective vocabulary, so no run could ever reach it"

reset_tree; mkconf "PARKED" ""
out=$(run)
miss "$out" "the kit's CORE phase vocabulary has shrunk below its floor"
same "a project phase EXTENSION is green" "$(run)" ""

reset_tree
mkdir -p tools/unattended && cp "$HERE/unattended.sh" tools/unattended/unattended.sh
ndod=$(grep '^DOD_CORE=' tools/unattended/unattended.sh | tr -d '
' | sed 's/^DOD_CORE="//; s/"$//' | wc -w)
sed -i 's/ parked-decisions-surfaced:agent"$/"/' tools/unattended/unattended.sh
out=$(run)
hit "$out" "the kit's CORE Definition-of-Done set has shrunk below its floor, and deleting an item is a silent, reason-free override of everything keyed on it"
hit "$out" "$((ndod-1)) against $ndod"

reset_tree; mkconf "" "project-item:machine"
same "a project DoD EXTENSION is green" "$(run)" ""

# ---- ...and the floor itself must be DECLARED. Omitting the key is the quietest way to disarm a
# ---- shrink-only pin, so the omission is its own refusal rather than a skipped check.
reset_tree; sed -i '/^CORE_FLOOR=/d' .unattended.conf
hit "$(run)" "CORE_FLOOR is undeclared in .unattended.conf, and with no floor a deleted core member is indistinguishable from a set that never had one"

# ---- check 2/3's empty-set branches. Reached by declaring the CORE set as whitespace, which parses
# ---- to a readable-but-empty value — distinct from the unreadable case armed above.
reset_tree; sed -i 's/^PHASES_CORE="[^"]*"/PHASES_CORE=" "/' tools/unattended/unattended.sh
hit "$(run)" "the effective phase vocabulary is empty, which makes every phase check below vacuously true"
reset_tree; sed -i 's/^DOD_CORE="[^"]*"/DOD_CORE=" "/' tools/unattended/unattended.sh
hit "$(run)" "the effective Definition-of-Done set is empty, so --close would block on nothing"

# ---- check 4 branch 1: THE POPULATION GUARD, both states. A run-state file under the memory root
# ---- but NOT at the selected path is the mis-segmentation. A tree with none anywhere is a YOUNG
# ---- tree and must be SILENT — the arm whose absence made the equivalent guard red every freshly
# ---- scaffolded repo, which is recorded in this fleet's own gotcha catalogue.
reset_tree; mkdir -p memory/elsewhere && git mv memory/builds/tRun/RUN.md memory/elsewhere/RUN.md
git commit -q -am moved --no-verify
out=$(run)
hit "$out" "a run-state file exists under the memory root but none at the path this leg selects, so the selector is mis-segmented and every check below is silent for the wrong reason"

reset_tree; git rm -q memory/builds/tRun/RUN.md && git commit -q -m young --no-verify
out=$(run); rc=$?
miss "$out" "the selector is mis-segmented"
same "a young tree with no run-state file anywhere exits 0" "$rc" "0"
same "a young tree prints nothing" "$out" ""

# ---- check 4 branches 2 and 3: no phase, and a phase outside the vocabulary.
reset_tree; sed -i '/^phase: /d' memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file declares no phase, and a file with no phase is outside every check keyed on one"
reset_tree; sed -i 's/^phase: RUNNING$/phase: MARINATING/' memory/builds/tRun/RUN.md
out=$(run)
hit "$out" "a run-state file declares a phase outside the effective vocabulary"
hit "$out" "MARINATING"

# ---- checks 5 and 6, and the ORDERING that makes presence worth separating. Absence fires 5 and
# ---- must NOT fire 6; a present-but-dead witness fires 6 and must not fire 5. Folded together,
# ---- the absence case would be skipped as unjudgeable and could never fire at all.
reset_tree; sed -i '/^witness: /d' memory/builds/tRun/RUN.md
out=$(run)
hit "$out" "a phase claim carries no witness, and presence is its own refusal because an oracle that skips an unwitnessed claim can never fire on one"
miss "$out" "a witness looks like a sha and resolves to no commit in this history"

reset_tree; sed -i 's/^witness: .*/witness: deadbeefdeadbeefdeadbeefdeadbeefdeadbeef/' memory/builds/tRun/RUN.md
out=$(run)
hit "$out" "a witness looks like a sha and resolves to no commit in this history"
miss "$out" "a phase claim carries no witness"

# ...and the unjudgeable shape is SKIPPED, not failed. Without this the discipline collapses into
# "every witness must be a sha", which the protocol deliberately does not say.
reset_tree; sed -i 's/^witness: .*/witness: wf_077104e6/' memory/builds/tRun/RUN.md
out=$(run)
miss "$out" "a witness looks like a sha and resolves to no commit in this history"
miss "$out" "a phase claim carries no witness"

# ---- check 7: two non-terminal run-state files. The green half is the whole rest of this file —
# ---- every other arm runs with exactly one live run and must not trip this.
reset_tree; build tTwo
sed -i "s/^witness: WITNESS$/witness: $(git rev-parse HEAD)/" memory/builds/tTwo/RUN.md
sed -i "s/^base: BASE$/base: $(git merge-base main HEAD)/" memory/builds/tTwo/RUN.md
git add -A && git commit -q -m two --no-verify
out=$(run)
hit "$out" "more than one run-state file is non-terminal, so 'the run' is not well-defined for anything keyed on it"
# ...and a TERMINAL second run does not trip it: the invariant is about live runs, not about files.
sed -i 's/^phase: RUNNING$/phase: LANDED/' memory/builds/tTwo/RUN.md
out=$(run)
miss "$out" "more than one run-state file is non-terminal"

# ---- check 4, the ARCHIVED-record branch (kit 1.6). An archived record must be TERMINAL, and this
# ---- has its own branch rather than riding check 7 because check 7 fires at TWO: a live RUN.md that
# ---- has reached LANDED plus one archived record edited back to RUNNING gives nlive=1 and the leg
# ---- would say nothing — which is the steady state after every completed second run.
# ---- THE POPULATION ARM COMES FIRST: the branch is only meaningful if the widened selector reaches
# ---- an archived file at all, and a selector that reached none would leave this silent for the
# ---- wrong reason.
reset_tree
cp memory/builds/tRun/RUN.md memory/builds/tRun/RUN.LANDED.abcd1234.md
sed -i 's/^phase: .*/phase: RUNNING/' memory/builds/tRun/RUN.LANDED.abcd1234.md
git add -A && git commit -q -m "an archived record left live" --no-verify
out=$(run)
hit "$out" "an ARCHIVED run-state file carries a non-terminal phase, so a finished record was retired while still claiming to be live, or was edited after retirement"
hit "$out" "RUN.LANDED.abcd1234.md"
# ...and a TERMINAL archived record is silent. Without this control the arm above proves only that
# the leg can red, not that it reds on the right thing.
sed -i 's/^phase: .*/phase: LANDED/' memory/builds/tRun/RUN.LANDED.abcd1234.md
git add -A && git commit -q -m "archived and finished" --no-verify
out=$(run)
miss "$out" "an ARCHIVED run-state file carries a non-terminal phase"

# ---- check 16: the INSTALLED protocol describes the rotation it is the rules for. Check 10 cannot
# ---- see this — it is a byte-diff of the shipped/installed pair and is green whatever BOTH say.
reset_tree
sed -i 's/RUN\.<phase>\.<blob8>\.md/RUN.the-old-spelling.md/g' memory/guides/UNATTENDED-PROTOCOL.md
hit "$(run)" "the installed protocol does not spell the archive filename grammar 'RUN.<phase>.<blob8>.md', so the rules a run is measured against do not describe what --preflight does to a finished record"
reset_tree
miss "$(run)" "the installed protocol does not spell the archive filename grammar"

# ---- check 8: the region holds NO COPY. It used to assert the region EQUALLED the README slice,
# ---- which was unmaintainable in the ordinary case — a spec rev bump moves the build index and the
# ---- only writer refuses once a run is live. Asserting EMPTINESS is the same invariant with the
# ---- second copy removed.
reset_tree; sed -i '/<!-- \/run:generated -->/d' memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file's generated markers are malformed"
reset_tree
printf '%s
' '**Build status:** OPEN · 1 unit(s)' > /tmp/_copy.$$
sed -i "/<!-- run:generated -->/r /tmp/_copy.$$" memory/builds/tRun/RUN.md; rm -f /tmp/_copy.$$
hit "$(run)" "a run-state file's generated region carries a COPY of the unit list; that list is DERIVED from the build README on every read, so a copy here is a second answer waiting to go stale. Empty the region between its markers"

# ---- TOOL-aDeclaredCeiling-3's four arms lived here and are SUPERSEDED. They asserted that a
# ---- terminal run's region is skipped from the EQUALITY comparison; dClosedLexicon r2 removed the
# ---- copy entirely, so the region is empty by contract and there is nothing to compare at any
# ---- phase. That is the same invariant with the failure mode designed out rather than scoped
# ---- around, and the arms above already cover it.

# ---- check 9: a recorded BASE the run could quietly move is not a pin.
reset_tree; sed -i 's/^base: .*/base: 0000000000000000000000000000000000000000/' memory/builds/tRun/RUN.md
hit "$(run)" "a recorded BASE does not resolve to a commit in this history, and the record is written by the run"

# ---- check 11: the bypass flag, checked where the record is.
reset_tree; printf '\nparked: considered --no-verify to get past the hook\n' >> memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file names the declared bypass flag, and bypassing the lander discards the whole bar the mandate leaned on"

# ---- check 10, both branches: the pair DRIFTED, and one half missing. The second is the arm that
# ---- keeps a parity check with one file from reading as a passing parity check.
reset_tree; printf '\ndrifted line\n' >> memory/guides/UNATTENDED-PROTOCOL.md
out=$(run)
hit "$out" "the shipped protocol and this repo's installed copy have drifted, so the kit ships something other than what it runs on"
hit "$out" "drifted line"
reset_tree; rm -f tools/unattended/PROTOCOL.template.md
hit "$(run)" "one half of the protocol pair is missing, and a parity check with one file is a check that cannot fail"

# ---- check 12: the kickoff hand-back, all four states. This is the only check that reads a file
# ---- outside the kit, and it exists because nothing else read the engine's TEXT — the manifest
# ---- ratchet watches the project layer and the coverage gate enumerates the skill's PATH.
reset_tree
mkdir -p skills/session-kickoff
cat > skills/session-kickoff/SKILL.md <<'ENG'
## Step 5 — READY card, then stop
control back: *"Ready — say go and I'll start, or adjust any field."* Do not start building.
## Step 5b — the unattended hand-back
1. **Step 0 · one** → abort.
2. **Step 0 · two** → abort.
3. **Step 1 · three** → abort.
4. **Step 2 · four** → park.
5. **Step 3 · five** → park.
6. **Step 5 · six** → replaced by the hand-back.
ENG
printf 'KICKOFF_ENGINE="skills/session-kickoff/SKILL.md"\nKICKOFF_EXITS="6"\n' >> .unattended.conf
git add -A && git commit -q -m engine --no-verify
same "a conforming kickoff engine is green" "$(run)" ""

# ...the hand-back deleted: a mandated run halts at the card with nobody to answer it.
sed -i '/^## Step 5b/d' skills/session-kickoff/SKILL.md
hit "$(run)" "the kickoff engine declares no unattended hand-back, so a mandated run still halts at the READY card with nobody to answer it"

# ...the STOP deleted, which is the other direction and the more dangerous one: every ATTENDED
# kickoff would then run on without asking. Asserted on the literal prompt string, because a section
# heading survives a gutted body.
git checkout -q -- skills/session-kickoff/SKILL.md
sed -i "/Ready — say go/d" skills/session-kickoff/SKILL.md
hit "$(run)" "the kickoff engine no longer carries the READY prompt string, so the DEFAULT stop is gone and every attended kickoff would run on unasked"

# ...an exit dropped from the enumeration: the count is the only thing that notices a run silently
# regaining a place to stop.
git checkout -q -- skills/session-kickoff/SKILL.md
sed -i '/^4\. \*\*Step 2/d' skills/session-kickoff/SKILL.md
out=$(run)
hit "$out" "the kickoff engine enumerates fewer interactive exits than the floor, and a dropped exit is a place an unattended run silently regains to stop"
hit "$out" "5 against 6"

# ...and a declared engine that is not there. Without this the whole check is skipped by a typo.
git checkout -q -- skills/session-kickoff/SKILL.md
sed -i 's|^KICKOFF_ENGINE=.*|KICKOFF_ENGINE="skills/session-kickoff/NOPE.md"|' .unattended.conf
hit "$(run)" "KICKOFF_ENGINE names a file that does not exist, so the hand-back check reads nothing and passes"

# ...blank turns it off, which is what lets an adopter without the kickoff skill stay green.
sed -i 's|^KICKOFF_ENGINE=.*|KICKOFF_ENGINE=""|' .unattended.conf
same "a blank KICKOFF_ENGINE turns the check off" "$(run)" ""

# ---- check 1 branch 5: a MALFORMED floor is a refusal, not a skip. Only the wholly UNDECLARED case
# ---- was caught, so `CORE_FLOOR="6"` left BOTH shrink-only pins unenforced while the conf still
# ---- read as configured — the easier half of the same mistake, armed and the harder half not.
reset_tree; sed -i 's/^CORE_FLOOR=.*/CORE_FLOOR="6"/' .unattended.conf
hit "$(run)" "CORE_FLOOR is malformed and both shrink-only floors are therefore unenforced; want two integers separated by a colon"
reset_tree; sed -i 's/^CORE_FLOOR=.*/CORE_FLOOR="six:six"/' .unattended.conf
hit "$(run)" "CORE_FLOOR is malformed and both shrink-only floors are therefore unenforced; want two integers separated by a colon"

# ---- check 9 branch 1: an ABSENT `base:` line is the violation, not the exemption. The check was
# ---- wrapped in `if [ -n "$rb" ]`, so deleting one line from a run-WRITABLE file disarmed the only
# ---- BASE assertion on the bar.
reset_tree; sed -i '/^base: /d' memory/builds/tRun/RUN.md; git add -A
hit "$(run)" "a run-state file records no BASE, and the record is written by the run — an absent pin is not a satisfied one"

# ---- check 9 branch 3: the anchor sitting AT HEAD, at a phase that CLAIMS work was done. The two
# ---- halves of this kit used to disagree here - the driver blesses this state at preflight, where a
# ---- run has correctly built nothing yet, while the leg refused it unconditionally, each with its
# ---- own green test. The refusal is scoped to the phases where a run asserts it built something.
reset_tree; git push -q -f origin unit:main
sed -i "s/^base: .*/base: $(git rev-parse HEAD)/" memory/builds/tRun/RUN.md
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md; git add -A
hit "$(run)" "the recorded BASE equals HEAD at a phase that claims work was done, so the run authored every byte an authorization comparison would read"

# ...and the SAME tree at a pass phase is silent, or the scoping is indistinguishable from deleting
# the check. This is the arm that would have caught the two halves disagreeing.
sed -i 's/^phase: .*/phase: BUILDING/' memory/builds/tRun/RUN.md; git add -A
miss "$(run)" "the recorded BASE equals HEAD at a phase that claims work was done"

# ...and ABORTED is NOT a work-claiming phase. It was listed with the other three, so a run that
# aborted before its first commit — base pinned at HEAD through preflight's degenerate path — red the
# bar with its own abort record, on the one exit that exists for a run which cannot meet its
# obligations. The three that remain are the control: dropping ABORTED must not drop them too.
sed -i 's/^phase: .*/phase: ABORTED/' memory/builds/tRun/RUN.md; git add -A
miss "$(run)" "the recorded BASE equals HEAD at a phase that claims work was done"
for ph in LANDING LANDED VERIFYING; do
  sed -i "s/^phase: .*/phase: $ph/" memory/builds/tRun/RUN.md; git add -A
  hit "$(run)" "the recorded BASE equals HEAD at a phase that claims work was done, so the run authored every byte an authorization comparison would read"
done
git push -q -f origin "$ANCHOR0":main

# ---- check 15, SECOND HALF: the LANDED witness lies on the history the anchor blesses. A record can
# ---- claim LANDED with a witness that is a perfectly real commit on the run's own branch and never
# ---- reached the remote at all - which is the claim this half exists to refuse, and the reason
# ---- --landed observes rather than asserts.
reset_tree
sed -i 's/^phase: .*/phase: LANDED/' memory/builds/tRun/RUN.md
sed -i "s/^witness: .*/witness: $(git rev-parse HEAD)/" memory/builds/tRun/RUN.md; git add -A
hit "$(run)" "a record claims LANDED with a witness that is not an ancestor of the anchor, so the work it says reached the remote is not on the branch the remote calls its default"

# ...and the GREEN CONTROL: the same record, the same phase, once the witness IS on the anchor.
# Without this the arm above proves only that check 15 can fire, not that it distinguishes anything.
sed -i "s/^witness: .*/witness: $ANCHOR0/" memory/builds/tRun/RUN.md; git add -A
miss "$(run)" "a record claims LANDED with a witness that is not an ancestor of the anchor"

# ...and a witness that resolves to nothing at all is CHECK 6's question, not check 15's. Asking it
# twice is a second answer to one question, and check 15 stays silent so the record reds ONCE with
# the sentence that fits.
sed -i "s/^witness: .*/witness: 0000000000000000000000000000000000000000/" memory/builds/tRun/RUN.md; git add -A
out=$(run)
hit "$out" "a witness looks like a sha and resolves to no commit in this history"
miss "$out" "a record claims LANDED with a witness that is not an ancestor of the anchor"

# ...and the DOUBLE-RED control: a non-sha witness at LANDED reds the SHAPE half and must not also
# reach the ancestry half, which `fail` not being `continue` used to let happen.
sed -i 's/^witness: .*/witness: wf_deadbeef-000/' memory/builds/tRun/RUN.md; git add -A
out=$(run)
hit "$out" "a record claims LANDED with a witness that is not sha-shaped"
miss "$out" "a record claims LANDED with a witness that is not an ancestor of the anchor"

# ---- check 15, FIRST HALF: sha SHAPE, and it must fire with NO anchor available. This is the half
# ---- that is deliberately outside check 9's loop: the loop needs a recorded BASE and a resolvable
# ---- default branch, and on a clone with neither it runs zero times while looking like coverage.
# ---- The fixture removes BOTH inputs, so a check placed inside the loop cannot pass this arm.
reset_tree
sed -i 's/^phase: .*/phase: LANDED/' memory/builds/tRun/RUN.md
sed -i 's/^witness: .*/witness: wf_3c665f96-4ff/' memory/builds/tRun/RUN.md
sed -i '/^base: /d' memory/builds/tRun/RUN.md; git add -A
hit "$(GOV_DEFAULT_BRANCH= run)" "a record claims LANDED with a witness that is not sha-shaped, so the claim that the work reached the remote cannot be judged at all, and a terminal claim is exactly where an unjudgeable witness costs the most"

# ...and the control that the SHAPE rule is scoped to LANDED. A non-terminal claim may carry a tag or
# a workflow id — the binding protocol permits all three shapes, and section 3 narrows it for the
# terminal phases only, because there the ancestry assertion IS the claim.
sed -i 's/^phase: .*/phase: BUILDING/' memory/builds/tRun/RUN.md; git add -A
miss "$(GOV_DEFAULT_BRANCH= run)" "a record claims LANDED with a witness that is not sha-shaped"

# ---- check 13: THE AUTHORIZATION, asserted by the BAR. Before this the leg did not contain the
# ---- marker string at all - it checked the driver's bookkeeping and never the thing the bookkeeping
# ---- was about, so every authorization defect was invisible here. The subject moved to the build
# ---- folder; the obligation did not.
# ----
# ---- Each arm has to break the README AT THE ANCHOR COMMIT, not in the working copy: the leg reads
# ---- `<recorded base>:<path>`, so a working-copy edit changes nothing it looks at. Editing main,
# ---- pushing, merging back and RE-RECORDING the base is the only shape that actually arms these -
# ---- an arm that edits the working tree passes against a leg that does no check at all.
anchor_break() { # everything after the first argument runs on main, then the base is re-recorded
  reset_tree
  git checkout -q main
  "$@"
  git add -A >/dev/null && git commit -q -m anchor-break --no-verify && git push -q -f origin main
  git checkout -q unit && git merge -q --no-edit main >/dev/null 2>&1
  sed -i "s|^base: .*|base: $(git merge-base origin/main HEAD)|" memory/builds/tRun/RUN.md
  sed -i "s|^witness: .*|witness: $(git rev-parse HEAD)|" memory/builds/tRun/RUN.md
  git add -A >/dev/null
}
anchor_restore() {
  # DROP the unit branch's staged fixture edits FIRST. Without this, `git checkout main` refuses
  # because the checkout would overwrite them, the `&&` swallows the refusal, main keeps the previous
  # arm's break, and every later arm starts from a tree it did not build - which is how one arm here
  # passed for the wrong reason and the next could not pass at all.
  git reset -q --hard "$PRISTINE"
  git checkout -qf main && git reset -q --hard "$ANCHOR0"
  git push -q -f origin "$ANCHOR0":main
  git checkout -qf unit
  reset_tree
}

drop_readme()  { rm -f memory/builds/tRun/README.md; }
break_fm()     { printf 'not front matter at all\n\n# tRun\n' > memory/builds/tRun/README.md; }
break_slug()   { sed -i 's|^slug: .*|slug: someoneElse|' memory/builds/tRun/README.md; }

anchor_break drop_readme
hit "$(run)" "no build README at a run's recorded BASE, so nothing committed before that run branched authorizes it"
anchor_restore

anchor_break break_fm
hit "$(run)" "the build README at a run's recorded BASE is not a build README - front matter opens at line 1 and this does not, so the authorization names something that is not a build"
anchor_restore

anchor_break break_slug
hit "$(run)" "a build README at its run's recorded BASE declares a different slug, so the folder was renamed or its README copied from another build: declared"
anchor_restore

# ---- and the GREEN control for all three: the same machinery with NOTHING broken must stay silent,
# ---- or these arms are indistinguishable from a leg that reds on any anchor edit at all.
noop_break() { :; }
anchor_break noop_break
miss "$(run)" "recorded BASE"
anchor_restore


# ---- check 9: a base that RESOLVES but sits off the anchor's history. The run's own branch is
# ---- exactly where such a commit lives, so this is the branch that replaced the equality test.
reset_tree
off=$(git commit-tree "$(git rev-parse HEAD^{tree})" -m "a commit the run authored off the anchor")
sed -i "s/^base: .*/base: $off/" memory/builds/tRun/RUN.md
hit "$(run)" "a recorded BASE is not an ancestor of the anchor, so it names a commit off the history the anchor blesses — which is where a run's own commits live: recorded"

# ---- check 9: an ancestor of the ANCHOR that this working history does not build on. Two separate
# ---- branches because they fail separately — the anchor can advance past a stale unit branch.
reset_tree
ahead=$(git commit-tree "$(git rev-parse "$ANCHOR0^{tree}")" -p "$ANCHOR0" -m ahead)
git update-ref refs/remotes/origin/main "$ahead"
sed -i "s/^base: .*/base: $ahead/" memory/builds/tRun/RUN.md
hit "$(run)" "a recorded BASE is not an ancestor of HEAD, so the run-state file pins a commit this working history does not build on"

# ---- THE LIFECYCLE, and the reason ancestry replaced equality. A run that does exactly what its
# ---- authorization grants — merge to the default branch and push — moved the merge-base past the
# ---- pinned base, and the old equality test then red the bar on EVERY later push, forever. Honest
# ---- fixture, no attacker anywhere in it.
reset_tree
git checkout -q main && git merge -q --no-ff unit -m "land the run"
git update-ref refs/remotes/origin/main "$(git rev-parse main)"
out=$(run); rc=$?
same "a LANDED run-state record leaves the bar green" "$out" ""
same "a LANDED run-state record exits 0" "$rc" "0"
git checkout -q unit; reset_tree

# ---- check 14: a replace ref or a graft file is itself the violation. The GIT() pin makes THIS
# ---- leg's reads honest; it binds no other tool reading the same objects.
reset_tree
git update-ref "refs/replace/$(git rev-parse HEAD)" "$(git rev-parse HEAD^)"
hit "$(run)" "a repo carrying an unattended run-state file also carries replace refs, and a replace ref rewrites what a sha MEANS for every read that is not pinned"
reset_tree
miss "$(run)" "also carries replace refs"
gf="$(git rev-parse --git-common-dir)/info/grafts"
mkdir -p "$(dirname "$gf")"; printf '%s %s\n' "$(git rev-parse HEAD)" "$(git rev-parse HEAD^)" > "$gf"
hit "$(run)" "a repo carrying an unattended run-state file also carries a grafts file, which rewrites the commit GRAPH underneath every ancestry read"
rm -f "$gf"
miss "$(run)" "also carries a grafts file"

# ---- the MARKER GRAMMAR: a marker line is the marker or it is malformed. Trailing text on the open
# ---- marker was invisible to both sides of the byte-compare while sitting inside the block a human
# ---- reads — a run widening its own authorization with both slices still equal.
# ---- The authorization moved out of a mandate BLOCK and into the build folder, so the surviving
# ---- region() caller is check 8's generated-region copy. The grammar defect is the same one: a
# ---- marker line carrying trailing content used to be dropped whole on BOTH sides, so a byte-compare
# ---- could not see it, and anything a run appended there rode along invisibly.
reset_tree
sed -i 's|^<!-- run:generated -->$|<!-- run:generated --> trailing text the byte-compare cannot see|' memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file's generated markers are malformed"
reset_tree
sed -i 's|^<!-- /run:generated -->$|<!-- /run:generated --> and the same on the close marker|' memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file's generated markers are malformed"
# The SOURCE-side marker is no longer check 8's business: nothing compares against it here any
# more. `--preflight` still validates it, and its arm lives in the driver's own test.
# GREEN CONTROL: clean markers stay silent, or the three arms above prove only that region() reds.
reset_tree
miss "$(run)" "generated markers are malformed"

# ---- the POPULATION LOOP: a tracked path with a space used to word-split into two non-existent
# ---- paths, both swallowed, so every per-file check silently skipped it.
reset_tree
mkdir -p "memory/builds/t Spaced"
cp memory/builds/tRun/README.md "memory/builds/t Spaced/README.md"
cp memory/builds/tRun/RUN.md "memory/builds/t Spaced/RUN.md"
sed -i 's/^base: .*/base: 0000000000000000000000000000000000000000/' "memory/builds/t Spaced/RUN.md"
git add -A && git commit -q -m spaced --no-verify
out=$(run)
hit "$out" "t Spaced/RUN.md"
miss "$out" "a run-state file is tracked at a path this leg cannot read"
git reset -q --hard "$PRISTINE"; git clean -qfd

# ---- check 4: tracked, selected, and genuinely unreadable. `continue` used to swallow it, which is
# ---- the same silence the word-split produced and just as invisible.
reset_tree; rm -f memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file is tracked at a path this leg cannot read, and skipping it silently removes it from every check below"
reset_tree

# ---- SOURCE-level: the leg must stay READ-ONLY. It runs on the merge bar, where a gate that writes
# ---- is a gate that can make the tree it is judging pass.
reset_tree
w=$(grep -nE '(^|[^-[:alnum:]])(mv|rm|cp|sed -i|tee|> *"?\$)' "$HERE/check-unattended.sh" \
    | grep -v '^[0-9]*: *#' || true)
n=$((n+1)); [ -z "$w" ] || { echo "FAIL the leg contains a write: $w"; st=1; }

# ---- SOURCE-level: the hot accessors must not fork. `fact_of`, `phase_of` and `core_of` run per
# ---- run-state file per check, and as `sed | head | tr` they cost three processes each — measured
# ---- 1094 sed/head/tr spawns across this suite, 278 after. Process spawn dominates on Windows.
# ---- Comment lines are excluded, or this grep matches the comment that explains the ban — a trap
# ---- this repo has hit twice and recorded.
nf=$(grep -nE 'head -1 \| tr -d' "$HERE/check-unattended.sh" | grep -v '^[0-9]*: *#' || true)
n=$((n+1)); [ -z "$nf" ] || { echo "FAIL a hot accessor reverted to the fork-per-call idiom: $nf"; st=1; }

[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
