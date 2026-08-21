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
DIRECTIVES_EXTRA_TABLE=""
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
<!-- gen:build-units -->
<!-- /gen:build-units -->
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
# It must ADVERTISE a HEAD symref. Since TOOL-aBranchedMandate-3 the leg reads the remote rather
# than any refs/remotes ref, and `git init --bare` leaves HEAD dangling — so without this line
# ADV_HEAD is empty, check 15's second half is guarded off and check 9's ancestor-of-HEAD branch
# is unreachable. The driver test carries the same line for the same reason.
git init -q --bare "$ORIGIN"
# SEPARATE LINES, not an && chain: chained, a non-zero from symbolic-ref silently skips the push,
# `refs/remotes/origin/main` never exists, and the merge-base below resolves EMPTY — which showed
# up as 33 arms failing with "records no BASE" rather than as anything about this line.
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main
git remote add origin "$ORIGIN"
git push -q origin main
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

# ---- a FOURTH branch, separate from the one above because an empty mode
# ---- vocabulary is a different failure. The other core sets stay readable, so the leg runs on and
# ---- every mode-membership test passes over nothing - a green that means the opposite of what it
# ---- looks like, which is exactly why it refuses instead of carrying on.
reset_tree; sed -i 's/^AUTH_MODES=.*/AUTH_MODES=unparseable/' tools/unattended/unattended.sh
hit "$(run)" "cannot read AUTH_MODES from the driver, so the mode-membership branch and the directive scope join would both pass over an empty set - an empty vocabulary makes every check keyed on it vacuously true"

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

# ...and the same COPY on a TERMINAL record is silent. No verb can empty that region once a run has
# ended, so reddening it would be a wedge with no exit — and the RED arm above is what proves the
# exemption did not simply switch check 8 off. Unit 6's fixture carries this pair as a standing
# property rather than as two arms about one past bug.
reset_tree
mutate memory/builds/tRun/RUN.md '/<!-- run:generated -->/a | [ARCH-tRun-1 — the unit](spec/one.md) | OPEN | rev-1 | 2026-08-01 |'
mutate memory/builds/tRun/RUN.md 's/^phase: RUNNING$/phase: ABORTED/'
out=$(run)
miss "$out" "a run-state file's generated region carries a COPY of the unit list"
same "a terminal record carrying a copy leaves the leg green" "$(run; echo $?)" "0"

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


# ---- check 9, S6c: the leg FAILS CLOSED when the remote advertises nothing. Without this branch
# ---- the whole block was skipped, so every BASE predicate, check 15's second half and the check-13
# ---- mandate assertion went silently absent on an unreachable remote — fail-OPEN under a comment
# ---- promising the opposite. The control is the arms above, which pass with the remote reachable.
reset_tree
git remote set-url origin "$ORIGIN_DIR/gone.git"
hit "$(run)" "the remote advertised no tips, so the recorded BASE cannot be shown to be published and this leg will not pass a run it could not check; the bar's authoritative run is the pre-push hook, which has the network by construction"
git remote set-url origin "$ORIGIN"
miss "$(run)" "the remote advertised no tips, so the recorded BASE cannot be shown to be published"

# ---- check 9, S6: a base that RESOLVES but is PUBLISHED NOWHERE. The predicate moved from
# ---- "ancestor of the anchor" to "ancestor of any tip the remote advertises", so the failing
# ---- case is a commit on no advertised history at all — which is exactly where a commit the
# ---- run authored on its own unpushed branch lives.
reset_tree
off=$(git commit-tree "$(git rev-parse HEAD^{tree})" -m "a commit the run authored off the anchor")
sed -i "s/^base: .*/base: $off/" memory/builds/tRun/RUN.md
hit "$(run)" "a recorded BASE is not published on the remote — it is an ancestor of no tip the remote advertises, so it names a commit that exists only where this run could have authored it: recorded"

# ---- check 9: an ancestor of the ANCHOR that this working history does not build on. Two separate
# ---- branches because they fail separately — the anchor can advance past a stale unit branch.
reset_tree
ahead=$(git commit-tree "$(git rev-parse "$ANCHOR0^{tree}")" -p "$ANCHOR0" -m ahead)
# PUSHED, not update-ref'd. The old fixture moved `refs/remotes/origin/main`, which S6 no longer
# reads, so the base was simply unpublished and check 9 refused one branch earlier. Reaching the
# ancestor-of-HEAD branch needs a base that IS published and still off this working history.
git push -q -f origin "$ahead:refs/heads/ahead" 2>/dev/null
sed -i "s/^base: .*/base: $ahead/" memory/builds/tRun/RUN.md
hit "$(run)" "a recorded BASE is not an ancestor of HEAD, so the run-state file pins a commit this working history does not build on"

# ---- THE LIFECYCLE, and the reason ancestry replaced equality. A run that does exactly what its
# ---- authorization grants — merge to the default branch and push — moved the merge-base past the
# ---- pinned base, and the old equality test then red the bar on EVERY later push, forever. Honest
# ---- fixture, no attacker anywhere in it.
reset_tree
git checkout -q main && git merge -q --no-ff unit -m "land the run"
# PUSHED. The control used to move `refs/remotes/origin/main`, a ref S6 removed from this leg's
# reads — so it stopped reproducing the merge-AND-PUSH state it exists for, and an is_published
# mutated back to equality would have survived it silently. The push moves the ADVERTISED tip,
# which is what the predicate now reads.
git push -q -f origin main
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
printf '# method\n\n## M2\n\n## M3\n\n## M4\n\n## M5\n\n## M6\n\n## M8\n\n## M9\n\n## M10\n\n## M12\n' > memory/guides/BUILD-METHOD.md
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
<!-- gen:build-units -->
<!-- /gen:build-units -->
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

# ---- 21 (TOOL-aBoundedVerdict-11 S5): the generated-units pair is REQUIRED on every tracked build
# ---- README. The corpus is clean, so a check with no red fixture here proves nothing - it would be
# ---- silent whether the predicate worked or not, which is the class this kit keeps meeting.
reset_tree
mutate memory/builds/tRun/README.md '/gen:build-units/d'
# The arm carries the ENTIRE literal signature up to the first interpolation, not a readable prefix:
# check-arms grades a branch on the whole thing, and a prefix reds. That is also why the remedy is
# part of THIS assertion rather than a second one - the remedy is inside the same literal.
hit "$(run)" "a tracked build README does not carry exactly one well-formed generated-units marker pair, so the driver cannot read its unit list and no run against it can close; repair with the --write mode of tools/memory-tree/gen_build_index.py"

# ...a DUPLICATED pair is refused too, not just an absent one. `region` conflates the two statuses, so
# an arm for only the absent case would leave the malformed half unproven.
reset_tree
printf '
%s
%s
' '<!-- gen:build-units -->' '<!-- /gen:build-units -->' >> memory/builds/tRun/README.md
hit "$(run)" "a tracked build README does not carry exactly one well-formed generated-units marker pair"

# ...and the GREEN control: an untouched corpus is silent on check 21. Without it the two arms above
# could both be firing on something unrelated.
reset_tree
miss "$(run)" "well-formed generated-units marker pair"

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

# E, the COUNT SENTENCE: the rows can all be right while the prose above them miscounts, which is
# exactly what shipped — an eight-row table under a sentence saying six, in both copies, parity green.
reset_tree; pedit 's/^Eight kit-owned core items\./Six kit-owned core items./'
hit "$(run)" "the protocol's stated count of core Definition-of-Done items disagrees with the set the driver enforces, and that sentence sits directly above the table it miscounts: says '"

# ...and the sentence gone entirely. Absence is its own refusal for the reason every locator here
# has one: a summary nobody can find is a summary nobody can join.
reset_tree; pedit 's/^Eight kit-owned core items\. //'
hit "$(run)" "the protocol states no count of kit-owned core Definition-of-Done items, so the sentence that summarises the table cannot be joined to the table or to the driver"
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

# ---- TOOL-cSettledDocket-2: DIRECTIVES_EXTRA was waivable and unshowable at once. `--waive` accepts
# ---- any handle `directives()` composes — core PLUS extra — while check 16 arm A joined CORE alone,
# ---- so a project could relax a rule the agent was never shown and could not fix that by adding a
# ---- table row, because the Skill is rendered from a kit-owned template.
# ----
# ---- RESTORED: these arms were deleted by a marker-to-marker slice while rewriting unit 6's block,
# ---- and the suite stayed green because the arms that remained were fine. Only `check-arms` saw it,
# ---- by noticing two `fail 16` branches had lost their positive assertion. That is the whole reason
# ---- the arms meta-gate is keyed on branches rather than on a suite's exit code.

# GREEN CONTROL: undeclared is the empty set, which is every adopter today, and is what keeps this
# change from reddening anyone who uses no extras.
reset_tree
same "an undeclared row source changes nothing" "$(run)" ""

# ...an extra handle with NO row source is REFUSED now, where it was silently waivable.
reset_tree; mutate .unattended.conf 's/^DIRECTIVES_EXTRA=""$/DIRECTIVES_EXTRA="house-style:M9"/'
hit "$(run)" "a directive is declared in the registry and absent from the Skill's table, so the agent that reads the table is bound by a set it was never shown: house-style:M9"

# ...and with a row source that CARRIES it, the project is whole again: declared, shown, waivable.
mutate .unattended.conf 's|^DIRECTIVES_EXTRA_TABLE=""$|DIRECTIVES_EXTRA_TABLE="memory/project/extra-directives.md"|'
mkdir -p memory/project
printf '| Handle | What it points at | Method | Directive |\n|---|---|---|---|\n| `house-style` | the prose rules this project adds | M9 | P1 |\n' > memory/project/extra-directives.md
same "declared + shown is silent" "$(run)" ""

# ...a row source naming a handle the registry does NOT declare reds the other way, so the join stays
# two-directional across the union rather than one-directional over it.
printf '| `never-declared` | nothing declares this | M9 | P2 |\n' >> memory/project/extra-directives.md
hit "$(run)" "the Skill's table names a directive the registry does not declare, so the agent is told about a handle no verb will accept: never-declared"

# ...a DECLARED path that does not exist is a NAMED refusal, not an empty union. Silently, every
# extra handle would land back on the absent-from-table branch with nothing saying why.
reset_tree
mutate .unattended.conf 's|^DIRECTIVES_EXTRA_TABLE=""$|DIRECTIVES_EXTRA_TABLE="memory/project/nope.md"|'
hit "$(run)" "DIRECTIVES_EXTRA_TABLE names a file that does not exist, so every project-declared directive would read as absent from the table it is supposed to be in"

# ...and a declared file carrying no readable row is its own refusal, for the reason every locator in
# this leg has one: a source contributing nothing is indistinguishable from no source at all.
mkdir -p memory/project && printf 'no rows here, just prose\n' > memory/project/nope.md
hit "$(run)" "DIRECTIVES_EXTRA_TABLE names a file carrying no readable directive row, so the project declared a row source and the union it contributes is empty"
reset_tree

# ---- TOOL-cSettledDocket-6: the STANDING frozen-versus-live fixture. cBriefedPilot's closing review
# ---- found one root three times — a predicate joining a FROZEN historical value to a LIVE present
# ---- one. The rule it encodes is general: once a run is TERMINAL its record is immutable through
# ---- the kit, so ANY leg check that can red on a terminal record is a wedge by construction.
# ----
# ---- REWRITTEN for main's check-8 redesign, adopted over this branch's. Main removed the COPY
# ---- rather than exempting its staleness: the region must be EMPTY and the unit list is derived
# ---- from the README on every read. The frozen-vs-live PAIR survives the change intact — only the
# ---- invariant it moves around is different — which is the argument for a standing fixture rather
# ---- than three arms pinned to three past bugs.
# ----
# ---- AC1 is scoped PER MOVE to the check named in that move's collision column, never to total leg
# ---- silence: widening DIRECTIVES_CORE reds check 16 by construction, and a builder chasing total
# ---- silence would exempt check 16 on terminal records — the over-wide exemption this build has
# ---- already committed once.
frozen() { sed -i 's/^phase: .*/phase: ABORTED/' memory/builds/tRun/RUN.md; }

# MOVE 1 — a COPY appears in the run-state region, which is what every pre-redesign record holds.
# Collides with check 8. On a TERMINAL record it must be silent: no verb can empty that region once
# the run has ended, so reddening it would be a wedge with no exit.
reset_tree; frozen
mutate memory/builds/tRun/RUN.md '/<!-- run:generated -->/a | [ARCH-tRun-1 — the unit](spec/one.md) | OPEN | rev-1 | 2026-08-01 |'
out=$(run)
miss "$out" "a run-state file's generated region carries a COPY of the unit list"
same "move 1 leaves a terminal record green" "$(run; echo $?)" "0"

# ...LIVE control. Without it, move 1's silence is satisfiable by deleting check 8 altogether.
reset_tree
mutate memory/builds/tRun/RUN.md '/<!-- run:generated -->/a | [ARCH-tRun-1 — the unit](spec/one.md) | OPEN | rev-1 | 2026-08-01 |'
hit "$(run)" "a run-state file's generated region carries a COPY of the unit list"

# MOVE 2 — the kit gains a directive, which a later version does. Collides with check 17: a frozen
# waiver's handle graded against today's set. THE WAIVER ROW IS THE POPULATION — without it the loop
# never iterates and the miss below passes by finding nothing, which is what shipped in this arm and
# is what the closing review caught by deleting the exemption and watching the suite still pass.
reset_tree
printf '
2026-08-16T00:00:00Z waiver · item minimal-prose · reason owner took it
' >> memory/builds/tRun/RUN.md
same "the frozen arm HAS a waiver row to grade" "$(grep -c 'waiver · item ' memory/builds/tRun/RUN.md)" "1"
mutate tools/unattended/unattended.sh 's/^DIRECTIVES_CORE="minimal-prose:M10 /DIRECTIVES_CORE="retired-handle:M10 /'
frozen
miss "$(run)" "a parked waiver names a handle outside the effective directive set"

# ...LIVE control for move 2: the same tree with a RUNNING record must still red, or the exemption
# has switched the check off rather than scoped it.
reset_tree
printf '
2026-08-16T00:00:00Z waiver · item minimal-prose · reason owner took it
' >> memory/builds/tRun/RUN.md
mutate tools/unattended/unattended.sh 's/^DIRECTIVES_CORE="minimal-prose:M10 /DIRECTIVES_CORE="retired-handle:M10 /'
hit "$(run)" "a parked waiver names a handle outside the effective directive set"
reset_tree

# ---- check 19: the authorization MODE, re-derived by the BAR rather than believed.
# ---- TOOL-aPromptedMandate-1. The driver reads `authorized-by:` at BASE to decide which discipline
# ---- binds a run; a value only the driver ever reads is a value only the driver can be wrong about.
# ----
# ---- THE FORGED DIRECTION, which is the whole reason the check exists: the record claims `prompt`
# ---- while the README at its own recorded BASE declares nothing. Note this arm does NOT need
# ---- `anchor_break` - it breaks the RECORD, not the anchor, and the anchor staying honest is
# ---- exactly what makes the disagreement visible.
reset_tree
sed -i '/^base: /a mode: prompt' memory/builds/tRun/RUN.md
git add -A >/dev/null
hit "$(run)" "a run-state file records an authorization mode the build README at its own recorded BASE does not declare, so the discipline the run says bound it is not the one its authorization asked for:"
reset_tree

# ---- THE AGREEING DIRECTION. Without it the arm above passes over a check that fires on every
# ---- record carrying a mode at all, which would red the bar for every honest prompt-mode run. The
# ---- README has to gain the key AT THE ANCHOR, so this one does need `anchor_break`.
add_mode() { sed -i '/^slug: /a authorized-by: prompt' memory/builds/tRun/README.md; }
anchor_break add_mode
sed -i '/^base: /a mode: prompt' memory/builds/tRun/RUN.md
git add -A >/dev/null
miss "$(run)" "a run-state file records an authorization mode the build README at its own recorded BASE does not declare"
anchor_restore

# ---- ABSENT is outside the arm BY CONSTRUCTION, not by a waiver: every run-state file written
# ---- before this unit carries no `mode:` line, and the leg's documented idiom is silence on
# ---- absence. tRun's pristine record is exactly such a file.
reset_tree
miss "$(run)" "a run-state file records an authorization mode the build README at its own recorded BASE does not declare"

# ---- MEMBERSHIP, which is a different question from agreement and needs
# ---- its own arm because the fixture that proves it is the one the agreement arm CANNOT see.
# ----
# ---- THE AGREEING-MISSPELLING case. Both sides carry the SAME illegal value, so the agreement
# ---- branch is satisfied and says nothing; before this unit the check passed here, which is the
# ---- whole defect - it asked whether two values MATCH and never whether either was LEGAL. This
# ---- arm therefore asserts the membership message HITS and the agreement message MISSES: an arm
# ---- that only asserted a red would have passed on the old code for the wrong reason.
add_bad_mode() { sed -i '/^slug: /a authorized-by: slugg' memory/builds/tRun/README.md; }
anchor_break add_bad_mode
sed -i '/^base: /a mode: slugg' memory/builds/tRun/RUN.md
git add -A >/dev/null
hit  "$(run)" "a run-state file records an authorization mode outside the kit's published set, so the discipline it names is one no kit member defines - legal values are"
miss "$(run)" "a run-state file records an authorization mode the build README at its own recorded BASE does not declare"
anchor_restore

# ---- THE README SIDE. MEASURED while writing this arm: the whole mode block is guarded by
# ---- `[ -n "$recmode" ]`, so a SILENT record never computes `dmode` and this branch is unreachable
# ---- from any fixture whose record carries no mode. That guard is correct — a legacy record is
# ---- outside the arm by construction — and it means the fixture must pair a LEGAL recorded mode
# ---- with an ILLEGAL declared one. The agreement branch fires too on that pair, which is expected;
# ---- this arm asserts only its own message, because asserting the absence of the other would be
# ---- asserting a coincidence rather than a behaviour.
anchor_break add_bad_mode
sed -i '/^base: /a mode: slug' memory/builds/tRun/RUN.md
git add -A >/dev/null
hit "$(run)" "the build README at a run's recorded BASE declares an authorization mode outside the kit's published set, so the authorization names a discipline no kit member defines - legal values are"
anchor_restore

# ---- the DECLARATION SEAM second-opinioned. The record claims a
# ---- playbook and a count the README at its own BASE does not declare. Two branches, two
# ---- fixtures, because one arm asserting either message would pass on whichever fired.
add_recipe_seam() { sed -i '/^slug: /a authorized-by: recipe\nplaybook: content/pb.md\npieces: 3' memory/builds/tRun/README.md; }
anchor_break add_recipe_seam
sed -i '/^base: /a mode: recipe' memory/builds/tRun/RUN.md
sed -i '/^base: /a playbook: content/other.md' memory/builds/tRun/RUN.md
sed -i '/^base: /a pieces: 99' memory/builds/tRun/RUN.md
git add -A >/dev/null
out=$(run)
hit "$out" "a run-state file records a playbook the build README at its own recorded BASE does not name, so the instructions the run says bound it are not the ones its authorization pointed at - recorded against declared follow:"
hit "$out" "a run-state file records a piece count the build README at its own recorded BASE does not declare, so the number the run will be measured against is not the number it was asked for - recorded against declared follow:"
anchor_restore

# ---- THE NEW MEMBER IS LEGAL. Without this the two arms above pass over a set that could have
# ---- been narrowed to nothing, and a membership test against an empty vocabulary reds everything -
# ---- which looks like rigour and is the vacuity this repo reds by name.
add_recipe_mode() { sed -i '/^slug: /a authorized-by: recipe' memory/builds/tRun/README.md; }
anchor_break add_recipe_mode
sed -i '/^base: /a mode: recipe' memory/builds/tRun/RUN.md
git add -A >/dev/null
miss "$(run)" "outside the kit's published set"
miss "$(run)" "a run-state file records an authorization mode the build README at its own recorded BASE does not declare"
anchor_restore
reset_tree

# TOOL-aPromptedMandate-2 - the PASS-KIND subset, joined both ways and guarded against its own
# vacuity, exactly as D is. Each arm was run against the live tree with the template broken in that
# one way BEFORE being written here, and each fired with the text below and no other. The line is
# anchored ^...$ so it selects the pass-kind line and not the run-order line above it, which also
# contains SPECCING.
#
# F, driver -> protocol: the driver publishes a pass kind the contract omits.
reset_tree; pedit 's/^`SPECCING` · `REVIEWING` · `FOLDING` · `BUILDING`$/`SPECCING` · `REVIEWING` · `FOLDING`/'
out=$(run)
hit "$out" "the driver publishes a phase as a build-method pass kind and the protocol does not list it, so the contract understates which positions the method names:"
miss "$out" "the contract claims the method names a position it does not"

# F, protocol -> driver: the contract calls a POSITION a pass kind. This is the direction the spec
# audit found - RESEARCHING and TESTING are positions, and a document that quietly promotes one
# contradicts the build method's closed pass set with nothing to notice.
reset_tree; pedit 's/^`SPECCING` · `REVIEWING` · `FOLDING` · `BUILDING`$/`SPECCING` · `REVIEWING` · `FOLDING` · `BUILDING` · `RESEARCHING`/'
out=$(run)
hit "$out" "the protocol lists a phase as a build-method pass kind that the driver does not publish as one, so the contract claims the method names a position it does not:"
miss "$out" "the contract understates which positions the method names"

# F, the locator: the same vacuity hole D has, opened the same way - by rewording prose.
reset_tree; pedit "s/Named for the build method's PASS kinds:/Named for the pass kinds of the method:/"
out=$(run)
hit "$out" "the protocol names no phase as a build-method pass kind, so the pass-kind join would compare the driver's subset against nothing and pass by finding nothing; the anchor is the line ending 'PASS kinds:'"
miss "$out" "the contract understates which positions the method names"
reset_tree

# TOOL-aPromptedMandate-4 - the SCOPE column, joined to the registry's third field. Both branches
# were run against the live tree before being written here, and each fired with the text below.
#
# G, the scopes disagree. ONE branch and not a comm pair: measured, a single changed scope cell puts
# the same handle in BOTH differences, so an only-in-table branch could never fire alone and its arm
# would have proved nothing. Arm A already covers the handle set in both directions.
reset_tree; mutate tools/unattended/SKILL.template.md 's/| M12 | prompt | D9 |/| M12 | all | D9 |/'
hit "$(run)" "the directive scopes the registry declares are not the scopes the Skill's table shows, so the agent is told which runs a rule binds by a table that disagrees with the verb enforcing it:"

# G, the locator: the column REMOVED entirely. Without this the join compares two empty sets and is
# green - the vacuity shape every other join in this leg carries a guard for.
reset_tree; mutate tools/unattended/SKILL.template.md 's/ | all | D/ | D/; s/ | prompt | D/ | D/'
out=$(run)
hit "$out" "the Skill's directive table carries no scope cell this leg can read, so the scope join would compare the registry against nothing and pass by finding nothing; the cell it looks for holds one of:"
miss "$out" "the agent is told which runs a rule binds by a table that disagrees"

# G, the PROJECT's own extra rows carry no scope column and must NOT red: the kit never asked an
# adopter to write one, and the join is scoped to the CORE set for exactly that reason.
reset_tree
mutate .unattended.conf 's/^DIRECTIVES_EXTRA=""$/DIRECTIVES_EXTRA="house-style:M9"/'
mutate .unattended.conf 's|^DIRECTIVES_EXTRA_TABLE=""$|DIRECTIVES_EXTRA_TABLE="memory/project/extra-directives.md"|'
mkdir -p memory/project
printf '| Handle | What it points at | Method | Directive |\n|---|---|---|---|\n| `house-style` | the prose rules this project adds | M9 | P1 |\n' > memory/project/extra-directives.md
# The DISCRIMINATING string, not the vacuity one. Reproduced both ways in a scratch repo: with the
# exclusion broken (`corescope` built from CORE **plus** EXTRA) the leg reds with the DISAGREEMENT
# message naming `house-style:all`, while the vacuity string appears zero times in either build -
# `tblscope` reads the kit template only, so that branch is unreachable here. The arm was green over
# the broken implementation, which is the fixture-passes-by-finding-nothing class this leg's own
# comments cite, committed in an arm written to guard against it.
miss "$(run)" "the directive scopes the registry declares are not the scopes the Skill's table shows"
reset_tree

# TOOL-aPromptedMandate-5 - check 20, the PROMPT path ordered inside its OWN section. Check 18
# orders the file's FIRST --preflight against its FIRST /session-kickoff; once a second start path
# exists that check keeps grading the first one and goes SILENTLY blind to the other. A false red is
# noticed in a minute; silent blindness is not, so the second path gets its own ordering.
#
# H, the OWNER TURN after the push. This is the direction that destroys the provenance argument: the
# one question the path may ask would be asked by a run already authorized, with nobody present.
reset_tree
mutate tools/unattended/SKILL.template.md 's/One `AskUserQuestion`, every gap/One ask, every gap/'
mutate tools/unattended/SKILL.template.md 's/^6\. \*\*The kickoff hand-back\*\*/6. **The kickoff hand-back** AskUserQuestion/'
hit "$(run)" "the Skill's prompt path puts its owner turn AFTER the branch push, so the one question it is allowed to ask would be asked by a run that is already authorized and has nobody to answer it:"

# H, the PUSH after preflight. Preflight run first meets the refusal that nothing published
# authorizes the run - the exact refusal step 1 quotes so the agent does not have to diagnose it.
reset_tree
mutate tools/unattended/SKILL.template.md 's/^4\. \*\*Commit, then PUSH THE BRANCH\.\*\*/4. **Commit.**/'
mutate tools/unattended/SKILL.template.md 's/^6\. \*\*The kickoff hand-back\*\*/6. PUSH THE BRANCH now\n6. **The kickoff hand-back**/'
hit "$(run)" "the Skill's prompt path puts the branch push AFTER preflight, and preflight run first meets the refusal that nothing published authorizes the run:"

# H, the locator: a step no longer named at all. Without this the two order comparisons compare
# against empty strings and are green - the vacuity shape every join in this leg carries a guard for.
reset_tree
mutate tools/unattended/SKILL.template.md 's/PUSH THE BRANCH/push the branch/'
out=$(run)
hit "$out" "the Skill's prompt path does not name all three of its ordered steps, so the order that makes the owner turn provably older than the authorization cannot be checked at all; it looks for AskUserQuestion, PUSH THE BRANCH and a bolded Preflight"
miss "$out" "puts its owner turn AFTER the branch push"

# H, a template with NO prompt path is legal and silent - this kit shipped without one, and an
# adopter on an older copy is not in error. Deleting the heading empties the slice.
reset_tree
mutate tools/unattended/SKILL.template.md 's/^## Start a run from a PROMPT$/## Notes/'
miss "$(run)" "the Skill's prompt path does not name all three of its ordered steps"
reset_tree

# TOOL-aPromptedMandate-6 fold — the three predicates the CLOSING REVIEW asked for. Each was measured
# firing against the live tree before its arm was written, which is the claim that failed for exactly
# one arm in this build and is why these say so explicitly.
#
# I, review H1: a floor BELOW the kit's own core count. This build SHIPPED that state - the bump to
# 13 was reverted by a `git checkout --` during an unrelated probe and arm C passed, because it only
# asked whether the count met the floor and never whether the floor met the kit.
reset_tree; mutate .unattended.conf 's/^DIRECTIVES_FLOOR="13"$/DIRECTIVES_FLOOR="11"/'
hit "$(run)" "DIRECTIVES_FLOOR is declared below the kit's own core directive count, so the shrink-only pin is slack by construction and a deleted core handle would pass it:"

# I, review L2: a PROJECT-declared scope. Two carriers say the scope is kit-owned; nothing enforced
# it, because scope_of composes core PLUS extra and would have honoured this silently.
reset_tree; mutate .unattended.conf 's/^DIRECTIVES_EXTRA=""$/DIRECTIVES_EXTRA="house-style:M9:prompt"/'
hit "$(run)" "a project-declared directive carries a SCOPE, and the scope is kit-owned because a project-selectable one is a narrowing of the core wearing another name:"

# I, review L3: a pass kind outside the vocabulary. The both-ways join to the protocol cannot see it
# - both sides would agree on the same wrong token, which is the two-derived-values class.
reset_tree; mutate tools/unattended/unattended.sh 's/^PHASES_PASSKIND="SPECCING /PHASES_PASSKIND="INVENTED /'
hit "$(run)" "a phase is published as a build-method pass kind and is not in the core vocabulary, so the contract names a position no run can ever occupy:"
reset_tree

# 175 -> 162 is a DELIBERATE lowering and owes its reason here. The 99-commit reconcile adopted
# main's check-8 redesign — the region holds no COPY, so there is nothing to keep fresh — which
# retired the staleness arms this branch had written against the old invariant. The
# frozen-versus-live PAIR survived and was rewritten against the new one; the anti-over-exemption
# arm did not, because main's exemption has the same over-wide scoping and narrowing it is a
# change the owner did not ask for. Filed as TOOL-cSettledDocket-11 rather than made silently.
# FLOOR_ASSERTIONS — TOOL-cBriefedPilot-23. A shrink-only pin on the EXECUTED count. This build
# shipped nine arms stranded past an unconditional `exit`: the file still contained them, so a static
# grep saw nine and `check-arms.py` text-matched nine, and the only signal that moved was this total,
# which nothing compared to anything. Lower it in a reviewed diff or not at all.
FLOOR_ASSERTIONS=200
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
