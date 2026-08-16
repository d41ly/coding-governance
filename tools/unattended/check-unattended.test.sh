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
cp "$HERE/check-unattended.sh" "$HERE/unattended.sh" "$HERE/PROTOCOL.template.md" "$HERE/SKILL.template.md" tools/unattended/
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
DIRECTIVES_EXTRA=""
DIRECTIVES_FLOOR="${DFLOOR_OVERRIDE:-$DIRECTIVES_FLOOR_DERIVED}"
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
**Build status:** OPEN · 1 unit(s)
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

DIRECTIVES_FLOOR_DERIVED="$(grep '^DIRECTIVES_CORE=' "$HERE/unattended.sh" | sed 's/^DIRECTIVES_CORE="//; s/"$//' | wc -w)"
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

# A fixture edit that changes nothing is a fixture that tests nothing. Three shapes cost this build
# real time: a grep anchored at column 0 against indented rows, an `s///` whose replacement carried a
# raw newline (a sed syntax error that edits nothing while reading as written), and a `git fetch` by
# PATH that moved no remote-tracking ref. Each looked correct and each mutated zero bytes.
mutate() { # file · sed-script
  local f="$1" before; before=$(git hash-object "$f")
  sed -i "$2" "$f"
  n=$((n+1))
  [ "$(git hash-object "$f")" != "$before" ] || { echo "FAIL fixture no-op on $f: $2"; st=1; }
}

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

# ---- check 8, all three branches: malformed markers on each side, and a region that DRIFTED from
# ---- the slice it is a copy of.
reset_tree; sed -i '/<!-- \/run:generated -->/d' memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file's generated markers are malformed, so the copy cannot be compared with its source"
reset_tree; sed -i '/<!-- \/gen:build-index -->/d' memory/builds/tRun/README.md
hit "$(run)" "a build README's generated markers are malformed, so the copy has no source to be compared with"
reset_tree; sed -i 's/^\*\*Build status:\*\* OPEN · 1 unit(s)$/**Build status:** CLOSED · 9 unit(s)/' memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file's generated region differs from the build README slice it is a COPY of; re-run the driver rather than hand-editing it"

# ...and the SAME staleness on a TERMINAL record is silent. Check 26 refuses --preflight on a
# finished run, and --preflight is the only verb that re-splices this region, so without the
# exemption a build that continues after its run ended reds the bar forever with nothing able to
# clear it. Reproduced on this repo's own tree. The pair matters more than either arm: the red one
# above proves the exemption did not simply turn check 8 off.
reset_tree
mutate memory/builds/tRun/RUN.md 's/^\*\*Build status:\*\* OPEN · 1 unit(s)$/**Build status:** CLOSED · 9 unit(s)/'
mutate memory/builds/tRun/RUN.md 's/^phase: RUNNING$/phase: ABORTED/'
out=$(run)
miss "$out" "a run-state file's generated region differs from the build README slice it is a COPY of"
same "a stale TERMINAL record leaves the leg green" "$(run; echo $?)" "0"

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
hit "$(run)" "a run-state file's generated markers are malformed, so the copy cannot be compared with its source"
reset_tree
sed -i 's|^<!-- /run:generated -->$|<!-- /run:generated --> and the same on the close marker|' memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file's generated markers are malformed, so the copy cannot be compared with its source"
reset_tree
sed -i 's|^<!-- gen:build-index -->$|<!-- gen:build-index --> trailing text on the SOURCE side|' memory/builds/tRun/README.md
hit "$(run)" "a build README's generated markers are malformed, so the copy has no source to be compared with"
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


# ---- check 16, the DIRECTIVE REGISTRY joined to the table an agent reads. Nine branches, nine arms,
# ---- each beside the green control the suite opened with. The join is a SECOND OPINION: a shell
# ---- constant against a hand-authored markdown table in a different file. A generator would make
# ---- the two agree by construction and check nothing.

# arm 1: the kit ships no template at all — a broken install, not a project choice.
reset_tree; mv tools/unattended/SKILL.template.md tools/unattended/SKILL.template.md.bak
hit "$(run)" "the kit ships no SKILL.template.md, so the directive table an agent reads cannot be joined to the registry it is supposed to mirror; a shipped kit always has one, so this is a broken install rather than a project choice"
mv tools/unattended/SKILL.template.md.bak tools/unattended/SKILL.template.md

# arm 2: a template with no readable row. This is the arm that matters most — without it the join
# passes by finding nothing, which is the class this whole build keeps meeting.
reset_tree; grep -v '^[[:space:]]*| `[a-z]' tools/unattended/SKILL.template.md > t.md && mv t.md tools/unattended/SKILL.template.md
hit "$(run)" "the Skill template carries no directive table row this leg can read, so arm A would join the registry against nothing and pass by finding nothing; the row shape it looks for is a leading pipe then a backticked lowercase handle"

# arm 3: a row citing two sections has no single answer to read. The reset is load-bearing: without
# it this ran on the tree arm 2 left behind, whose rows were all stripped, so the sed matched nothing
# and the arm asserted a state its own fixture had just made unreachable.
reset_tree; sed -i 's/| the transcript rule under a mandate |/| M2 |/' tools/unattended/SKILL.template.md   # a second M<n> must be its OWN CELL
hit "$(run)" "a directive row cites more than one build-method section, so the join has no single answer to read for that handle"

# arm 4: declared in the registry, absent from the table.
reset_tree; sed -i '/| `wrap-up-derived` |/d' tools/unattended/SKILL.template.md
hit "$(run)" "a directive is declared in the registry and absent from the Skill's table, so the agent that reads the table is bound by a set it was never shown"

# arm 5: in the table, absent from the registry — the other direction, and it needs its own arm
# because a one-way containment check would pass here.
reset_tree; sed -i 's/^DIRECTIVES_CORE="minimal-prose:M10 /DIRECTIVES_CORE="/' tools/unattended/unattended.sh
hit "$(run)" "the Skill's table names a directive the registry does not declare, so the agent is told about a handle no verb will accept"

# arm 6: a cited section that does not resolve. Arm B is SILENT without the carrier, so the fixture
# has to HAVE one for this to be reachable at all.
reset_tree; printf '# method

## M2

## M3

## M4

## M5

## M6

## M8

## M10
' > memory/guides/BUILD-METHOD.md   # M9 omitted on purpose
hit "$(run)" "a directive points at a build-method section that does not exist, so the handle names a rule no reader can reach:"
rm -f memory/guides/BUILD-METHOD.md

# arm 7: the floor undeclared.
reset_tree; sed -i '/^DIRECTIVES_FLOOR=/d' .unattended.conf
hit "$(run)" "DIRECTIVES_FLOOR is undeclared in .unattended.conf, and with no floor a deleted directive is indistinguishable from a set that never had one"

# arm 8: the floor malformed. Undeclared and malformed are separate branches, mirroring CORE_FLOOR,
# because either one leaves the pin unenforced while the conf still looks configured.
reset_tree; sed -i 's/^DIRECTIVES_FLOOR=.*/DIRECTIVES_FLOOR="eleven"/' .unattended.conf
hit "$(run)" "DIRECTIVES_FLOOR is not a plain integer, so the shrink-only pin on the directive set is unenforced while the conf still looks configured"

# arm 9: the core set shrunk below its floor.
reset_tree; sed -i 's/^DIRECTIVES_CORE="[a-z-]*:M[0-9]* /DIRECTIVES_CORE="/' tools/unattended/unattended.sh
hit "$(run)" "the kit's CORE directive set has shrunk below its floor, and deleting a directive is a silent, reason-free relaxation of everything keyed on it"

# ---- and the green control AGAIN, after nine mutations. reset_tree restores refs as well as the
# ---- work tree, but a suite that only ever reds is a suite that arms every branch and checks
# ---- nothing; this is what says the mutations above were the cause.
reset_tree
same "the tree is still clean after nine mutations" "$(run >/dev/null 2>&1; echo $?)" "0"

# ---- check 17, the parked WAIVER: a declared handle, a non-empty reason, and presence in the
# ---- run-state file's FIRST committed blob. TOOL-aStandingWrit-8 names this arm set by id — the
# ---- kit had driver arms and leg arms and ZERO arms that run the driver and THEN the leg over one
# ---- tree — so the green control's waiver line is PRODUCED BY `--preflight --waive`, never
# ---- hand-authored. A hand-authored line only tests the checker against its own idea of the grammar.
# ----
# ---- A FRESH build slug, because `--diff-filter=A | tail -1` takes the OLDEST add: reusing tRun,
# ---- whose RUN.md is already committed, would compare against a blob written before any waiver
# ---- existed and the control would fail for a reason that has nothing to do with the check.
reset_tree
# The driver's preflight OBSERVES the remote's own HEAD advertisement, and this suite's bare
# origin has no HEAD symref because no leg check ever needed one. Set it here, where the only
# arms that run the driver live; nothing else in this file reads the remote's advertisement.
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main
git checkout -q main
printf '# method\n\n## M2\n\n## M3\n\n## M4\n\n## M5\n\n## M6\n\n## M8\n\n## M9\n\n## M10\n' > memory/guides/BUILD-METHOD.md
mkdir -p memory/builds/tWaive
cat > memory/builds/tWaive/README.md <<'RM'
---
slug: tWaive
node: a
opened: 2026-08-01
streams: architecture
roster: ARCH
ids: ARCH-tWaive-1
---

# tWaive

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s)
<!-- /gen:build-index -->
RM
# tRun's record is RUNNING, and a second live run trips check 7 — 'the run' stops being well
# defined for anything keyed on it. Retire it in the same commit so this block's green control
# measures check 17 rather than a collision this fixture created.
sed -i 's/^phase: RUNNING$/phase: ABORTED/' memory/builds/tRun/RUN.md
git add -A && git commit -q -m tWaive --no-verify && git push -q -f origin main
git checkout -q unit && git merge -q --no-edit main >/dev/null 2>&1
WP=$(git rev-parse HEAD)
wreset() { git reset -q --hard "$WP"; git clean -qfd; }
drive() { bash tools/unattended/unattended.sh "$@" 2>&1; }
wline() { grep -F ' waiver · item ' memory/builds/tWaive/RUN.md; }

# GREEN CONTROL: the driver writes the waiver, the record's first commit carries it, the leg is silent.
wreset
dout=$(drive --preflight tWaive --keepalive-id k1 --waive minimal-prose --reason taken-by-the-owner)
hit "$dout" "preflight OK"
same "the driver wrote a waiver line the leg can select" "$([ -n "$(wline)" ] && echo yes)" "yes"
git add -A && git commit -q -m waived --no-verify
out=$(run)
same "a tree whose waiver was taken at preflight exits 0" "$?" "0"
miss "$out" "check 17"

# arm 1 — an UNDECLARED handle. Edited before the first commit, so the join is satisfied and this
# arm can only fire on the membership test rather than on two branches at once.
wreset
drive --preflight tWaive --keepalive-id k1 --waive minimal-prose --reason taken-by-the-owner >/dev/null 2>&1
sed -i 's/· item minimal-prose ·/· item no-such-handle ·/' memory/builds/tWaive/RUN.md
git add -A && git commit -q -m bad-handle --no-verify
out=$(run)
hit "$out" "a parked waiver names a handle outside the effective directive set, so the record claims a relaxation of a rule no verb would have accepted"
miss "$out" "absent from the run-state file's FIRST committed blob"

# arm 2 — an EMPTY reason. Unit 3 refuses one at the moment of writing; this is the second opinion
# over a record where that refusal was bypassed by editing the file directly.
wreset
drive --preflight tWaive --keepalive-id k1 --waive minimal-prose --reason taken-by-the-owner >/dev/null 2>&1
sed -i 's/· reason taken-by-the-owner$/· reason /' memory/builds/tWaive/RUN.md
git add -A && git commit -q -m empty-reason --no-verify
hit "$(run)" "a parked waiver carries an empty reason, and a waiver recording no reason is indistinguishable from one nobody meant"

# arm 3 — THE JOIN, and the whole point of the check: a well-formed waiver naming a declared handle
# with a real reason, APPENDED after the record was created. Every shape test passes; only the git
# join can see that the owner did not take it at preflight.
wreset
drive --preflight tWaive --keepalive-id k1 >/dev/null 2>&1
git add -A && git commit -q -m no-waiver --no-verify
printf '2026-08-16T00:00:00Z waiver · item minimal-prose · reason appended later\n' >> memory/builds/tWaive/RUN.md
git add -A && git commit -q -m appended --no-verify
out=$(run)
hit "$out" "a parked waiver line is absent from the run-state file's FIRST committed blob, so it was appended after the record was created and the claim that the owner took it at preflight is not what landed"
miss "$out" "outside the effective directive set"
miss "$out" "empty reason"

# arm 4 — S5: a record STAGED but never committed is in the population (`git ls-files` reads the
# index) and has no first blob, so the join is SILENT. Reddening it would red the honest
# preflight-to-first-commit window with nobody present to interpret it.
wreset
drive --preflight tWaive --keepalive-id k1 --waive minimal-prose --reason taken-by-the-owner >/dev/null 2>&1
git add -A
out=$(run)
miss "$out" "absent from the run-state file's FIRST committed blob"

# restore: main back to the shared anchor, or every later arm inherits tWaive and the method file.
git checkout -q main; git reset -q --hard "$ANCHOR0"; git push -q -f origin main; git checkout -qf unit; reset_tree

# ---- check 18: the kickoff step is ORDERED after preflight in the Skill an agent reads. Keyed on a
# ---- non-blank KICKOFF_ENGINE like check 12, because an adopter may ship no kickoff skill at all.
kick_engine() { # stage a conforming engine + declare it, so check 12 stays silent and only 18 speaks
  mkdir -p skills/session-kickoff
  cat > skills/session-kickoff/SKILL.md <<'ENG'
## Step 5 — READY card, then stop
control back: *"Ready — say go and I'll start, or adjust any field."* Do not start building.
## Step 5b — the unattended hand-back
ENG
  printf 'KICKOFF_ENGINE="skills/session-kickoff/SKILL.md"\n' >> .unattended.conf
  git add -A && git commit -q -m engine --no-verify
}

# GREEN CONTROL: the template this kit actually ships orders the two correctly.
reset_tree; kick_engine
same "the shipped Skill template orders kickoff after preflight" "$(run)" ""

# ...TRANSPOSED. The deadlock: kickoff invoked first halts at its READY card with nobody under a
# mandate to answer it. Judged on the FIRST occurrence of each, which is the one the agent reads.
mutate tools/unattended/SKILL.template.md '2i Invoke /session-kickoff before anything else.'
hit "$(run)" "the Skill template puts the kickoff step BEFORE --preflight, and kickoff invoked first halts at its READY card with nobody under a mandate to answer it: /session-kickoff at line"

# ...kickoff never named at all. ABSENCE IS A REFUSAL rather than the safe side, because a template
# that never names kickoff and one that names it too early read identically on any count.
reset_tree; kick_engine
mutate tools/unattended/SKILL.template.md '\|/session-kickoff|d'
hit "$(run)" "the Skill template never names /session-kickoff while this project declares a kickoff engine, and a missing step reads exactly like a deadlocked one on any count-based check"

# ...no --preflight invocation to order anything against.
reset_tree; kick_engine
mutate tools/unattended/SKILL.template.md '/unattended.sh --preflight/d'
hit "$(run)" "the Skill template names no --preflight invocation, so there is no anchor to order the kickoff step against and the sequence this check exists to hold is unstated"

# ...a blank engine turns the check off, and the arm proves it by leaving the lines TRANSPOSED —
# silent because the project ships no kickoff skill, not because the template is conforming.
reset_tree
mutate tools/unattended/SKILL.template.md '2i Invoke /session-kickoff before anything else.'
same "a blank KICKOFF_ENGINE turns check 18 off even on a transposed template" "$(run)" ""
reset_tree

# ---- check 16 arms D and E: the CONTRACT's two tables joined to the constants the driver enforces.
# ---- Both edits go to BOTH protocol copies, or check 15's parity fires and the arm would be
# ---- satisfied by a refusal that has nothing to do with the join it is testing.
# Through `mutate`, so a locator that stops matching after a document reword FAILS here instead of
# silently turning six arms into six no-ops that still read as tests.
pedit() { mutate tools/unattended/PROTOCOL.template.md "$1"
          mutate memory/guides/UNATTENDED-PROTOCOL.md "$1"; }

# GREEN CONTROL: the shipped contract already agrees with the driver in both tables.
reset_tree
same "the shipped protocol's two tables join clean" "$(run)" ""

# D, driver -> protocol: a core phase the contract never publishes.
reset_tree; pedit 's/`SPECCING` · //'   # mid-line: VERIFYING ends a line, so it has no trailing space to match
out=$(run)
hit "$out" "a CORE phase is enforced by the driver and absent from the protocol's run-order list, so the contract publishes a vocabulary the kit does not use"
miss "$out" "names a phase the driver does not carry"

# D, protocol -> driver: a published position no run can occupy.
reset_tree; pedit 's/`PREFLIGHT` · /`PREFLIGHT` · `INVENTED` · /'
out=$(run)
hit "$out" "the protocol's run-order list names a phase the driver does not carry, so the contract promises a position no run can ever occupy"
miss "$out" "absent from the protocol's run-order list"

# D, the locator itself: rewording the prose anchor empties the extraction. Without this refusal the
# join would compare against nothing and pass — silently, and on a document edit nobody reviews as code.
reset_tree; pedit 's/in run order:$/in this order:/'
out=$(run)
hit "$out" "the protocol's run-order paragraph yields no phase token, so the phase join would compare the driver's vocabulary against nothing and pass by finding nothing; the anchor is the line ending 'in run order:'"
miss "$out" "absent from the protocol's run-order list"

# E, driver -> protocol: --close blocks on an item the contract never mentions.
reset_tree; pedit '/^| `build-complete` |/d'
out=$(run)
hit "$out" "a CORE Definition-of-Done item is enforced by --close and absent from the protocol's table, so a run is blocked by an item the contract never told anyone about"
miss "$out" "names an item the driver does not carry"

# E, protocol -> driver: a published gate nothing evaluates.
# `a` rather than an `s` with a newline in its replacement: a raw newline there is a sed syntax
# error, and the edit silently did nothing while the arm read as written.
reset_tree; pedit '/^| `parked-decisions-surfaced` /a | `invented-item` | machine | nothing evaluates this |'
out=$(run)
hit "$out" "the protocol's Definition-of-Done table names an item the driver does not carry, so the contract publishes a gate nothing evaluates"

# E, the locator itself: every row gone empties the extraction, and the EMPTY refusal is what fires
# rather than eight absent-item refusals — the guard is ordered ahead of the comparison on purpose.
reset_tree; pedit '/^| `[a-z][a-z-]*` |/d'
out=$(run)
hit "$out" "the protocol's Definition-of-Done table yields no item row, so the DoD join would compare the driver's set against nothing and pass by finding nothing"
miss "$out" "absent from the protocol's table"
reset_tree

# ---- `mutate` itself, both ways. The failing direction runs in a SUBSHELL, or the FAIL it is
# ---- supposed to emit would fail this suite instead of being observed by it.
reset_tree
mout=$(n=0; st=0; mutate .unattended.conf 's/__matches_nothing_at_all__/x/'; echo "st=$st n=$n")
hit "$mout" "FAIL fixture no-op on .unattended.conf"
hit "$mout" "st=1 n=1"
gout=$(n=0; st=0; mutate .unattended.conf 's/^MEMORY_ROOT=.*/MEMORY_ROOT=mem2/'; echo "st=$st n=$n")
miss "$gout" "FAIL fixture no-op"
hit "$gout" "st=0 n=1"
reset_tree

# FLOOR_ASSERTIONS — TOOL-cBriefedPilot-23. A shrink-only pin on the EXECUTED count. This build
# shipped nine arms stranded past an unconditional `exit`: the file still contained them, so a static
# grep saw nine and `check-arms.py` text-matched nine, and the only signal that moved was this total,
# which nothing compared to anything. Lower it in a reviewed diff or not at all.
FLOOR_ASSERTIONS=148
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
