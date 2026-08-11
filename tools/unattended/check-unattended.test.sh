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
CORE_FLOOR="6:6"
KEEPALIVE_CREATE="CronCreate"
KEEPALIVE_DELETE="CronDelete"
PHASES_EXTRA="${1-}"
DOD_EXTRA="${2-}"
EOF
}

build() { # slug
  mkdir -p "memory/builds/$1"
  cat > "memory/builds/$1/README.md" <<EOF
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
base-ref: refs/remotes/origin/main
EOF
}

mkconf; build tRun
git add -A && git commit -q -m base --no-verify
# A REMOTE-TRACKING anchor: check 9 measures against `refs/remotes/...` only, because a bare local
# branch is a ref the run can move with `git branch -f` — a reproduced way to make BASE equal HEAD.
# It lives OUTSIDE the work tree, or `git clean -qfd` in reset_tree deletes it.
ORIGIN_DIR=$(mktemp -d); ORIGIN="$ORIGIN_DIR/origin.git"
git init -q --bare "$ORIGIN" && git remote add origin "$ORIGIN" && git push -q origin main
# The gate derives the default branch from refs/remotes/origin/HEAD ONLY, and a bare push creates
# refs/remotes/origin/main WITHOUT it — so without this line the leg has nothing to derive and every
# arm below would pass because the check was OFF.
git remote set-head origin main >/dev/null 2>&1
ANCHOR0=$(git rev-parse main)
git checkout -q -b unit
git commit -q --allow-empty -m "unit work" --no-verify
BASE0=$(git rev-parse HEAD)
# GOV_DEFAULT_BRANCH is deliberately NOT exported: the leg must not read it, and exporting it here
# would hide that by making the steered and canonical answers identical.
sed -i "s/^witness: WITNESS$/witness: $(git rev-parse HEAD)/" memory/builds/tRun/RUN.md
sed -i "s/^base: BASE$/base: $(git merge-base origin/main HEAD)/" memory/builds/tRun/RUN.md
git add -A && git commit -q -m facts --no-verify
PRISTINE=$(git rev-parse HEAD)
reset_tree() { git reset -q --hard "$PRISTINE"; git clean -qfd; }
run() { bash "$SCRIPT" 2>&1; }

# ---- THE GREEN CONTROL, first. Every red arm below is worthless if the clean tree is not clean:
# ---- a leg that reds on everything arms every branch and checks nothing.
out=$(run); rc=$?
same "a conforming tree exits 0" "$rc" "0"
same "a conforming tree prints nothing" "$out" ""

# ---- check 9's BASE provenance. The leg must be a second OPINION, not a
# ---- second computation of the same steered value — a leg that reads the same input the driver read
# ---- confirms the steer instead of contradicting it, which is how three reproduced authorization
# ---- defects stayed green on the bar.

# The variable the DRIVER honours must not move this leg at all. If the leg read it, this arm would
# be green for the wrong reason and a steered run would land.
reset_tree
out=$(GOV_DEFAULT_BRANCH=nosuchbranch run); rc=$?
same "the leg ignores GOV_DEFAULT_BRANCH entirely" "$rc" "0"
same "the leg ignores GOV_DEFAULT_BRANCH, silently" "$out" ""

# origin/HEAD deleted: the leg has nothing outside the run's reach to derive from, and that is a RED.
# This body used to sit under `if [ -n "$d" ]` with no else, so one local command with no push
# disarmed every BASE check at once and the bar stayed green.
reset_tree
git symbolic-ref -d refs/remotes/origin/HEAD >/dev/null 2>&1
hit "$(run)" "this leg cannot derive a default branch: refs/remotes/origin/HEAD does not resolve, so the recorded BASE cannot be checked against anything outside the run's reach — repair it with 'git remote set-head origin -a'"
git remote set-head origin main >/dev/null 2>&1

# base-ref absent is the violation, not the exemption — the same rule the base: arm already carries.
reset_tree; sed -i '/^base-ref: /d' memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file records no base-ref, so the ref its BASE was derived from cannot be re-resolved — an absent pin is not a satisfied one"

# base-ref present but naming a ref this leg did not derive: the driver was pointed somewhere the
# gate is not, which is exactly the shape GOV_DEFAULT_BRANCH steering produces.
reset_tree; sed -i 's|^base-ref: .*|base-ref: refs/remotes/origin/steered|' memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file's base-ref is not the ref this leg derives from refs/remotes/origin/HEAD, which means the driver was pointed somewhere this gate is not: recorded"

# base-ref AGREES with what the leg derives, but the ref itself is gone. origin/HEAD is a symref and
# resolves even when its target does not, so this state is reachable with one command and is NOT the
# disagreement arm above.
reset_tree
git update-ref -d refs/remotes/origin/main
hit "$(run)" "a run-state file's base-ref does not resolve, so nothing can be re-derived from it"
git update-ref refs/remotes/origin/main main

# The ref resolves but shares no history with HEAD, so there is no merge-base to reproduce. Without
# this arm the empty-merge-base branch would read as covered by the mismatch arm, which it is not.
reset_tree
ORPHAN=$(git commit-tree "$(git hash-object -t tree -w /dev/null)" -m orphan)
git update-ref refs/remotes/origin/main "$ORPHAN"
hit "$(run)" "and HEAD, so the recorded BASE reproduces nothing"
git update-ref refs/remotes/origin/main main

# A TERMINAL record is exempt from the merge-base reproduction — after a run lands, its branch point
# is gone by construction and reproducing it would red main forever. What still holds is REACHABILITY,
# so a terminal record whose BASE is not an ancestor of HEAD describes a run that landed somewhere
# else, and that is a red.
reset_tree
sed -i 's/^phase: RUNNING$/phase: LANDED/' memory/builds/tRun/RUN.md
ORPH=$(git commit-tree "$(git hash-object -t tree -w /dev/null)" -m orphan)
sed -i "s/^base: .*/base: $ORPH/" memory/builds/tRun/RUN.md
hit "$(run)" "a terminal run-state file records a BASE that is not an ancestor of HEAD, so the run it describes did not land on this history"

# POSITIVE CONTROL for the exemption itself: the same terminal record with a REACHABLE base is green,
# which is the half that proves the skip is a skip and not a blanket pass.
reset_tree
sed -i 's/^phase: RUNNING$/phase: LANDED/' memory/builds/tRun/RUN.md
sed -i "s/^base: .*/base: $(git rev-parse HEAD)/" memory/builds/tRun/RUN.md
out=$(run); rc=$?
same "a terminal record with a reachable BASE is green" "$rc" "0"

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
sed -i 's/^PHASES_CORE="PREFLIGHT RUNNING VERIFYING LANDING LANDED ABORTED"/PHASES_CORE="PREFLIGHT RUNNING VERIFYING LANDING LANDED"/' tools/unattended/unattended.sh
out=$(run)
hit "$out" "the kit's CORE phase vocabulary has shrunk below its floor, and deleting a core member is a silent, reason-free override of everything keyed on it"
hit "$out" "5 against 6"
# ...the member deleted was a TERMINAL one, so the independent terminal-membership check fires too.
# Two sets declared separately, so THAT one is falsifiable where the subset form was not.
hit "$out" "a TERMINAL phase is not in the effective vocabulary, so no run could ever reach it"

reset_tree; mkconf "PARKED" ""
out=$(run)
miss "$out" "the kit's CORE phase vocabulary has shrunk below its floor"
same "a project phase EXTENSION is green" "$(run)" ""

reset_tree
sed -i 's/ parked-decisions-surfaced:agent"$/"/' tools/unattended/unattended.sh
out=$(run)
hit "$out" "the kit's CORE Definition-of-Done set has shrunk below its floor, and deleting an item is a silent, reason-free override of everything keyed on it"
hit "$out" "5 against 6"

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

# ---- check 9: a recorded BASE the run could quietly move is not a pin.
reset_tree; sed -i 's/^base: .*/base: 0000000000000000000000000000000000000000/' memory/builds/tRun/RUN.md
hit "$(run)" "a recorded BASE is not the merge-base this history reproduces, and every mandate assertion hangs on that value: recorded"

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

# ---- check 9 branch 3: the anchor sitting AT HEAD. `git branch -f main HEAD` was the reproduced
# ---- exploit; the leg now refuses the resulting state as well as the driver.
reset_tree; git push -q -f origin unit:main
sed -i "s/^base: .*/base: $(git rev-parse HEAD)/" memory/builds/tRun/RUN.md; git add -A
hit "$(run)" "the merge-base equals HEAD, so the run authored every byte a mandate comparison would read"
git push -q -f origin "$ANCHOR0":main

# ---- check 13, all four branches: THE MANDATE, asserted by the BAR. Before this the leg did not
# ---- contain the string `run:mandate` at all — it checked the driver's bookkeeping and never the
# ---- thing the bookkeeping is about, so every authorization defect was invisible here.
reset_tree
sed -i 's/^The owner authorizes tRun to merge and to push\.$/FORGED — the run rewrote its own authorization./' memory/builds/tRun/RUN.md
git add -A
hit "$(run)" "a run-state file's mandate differs from the one at its recorded BASE — the run edited its own authorization"

reset_tree
printf '
<!-- run:mandate -->
FORGED SECOND BLOCK: also authorize force-push.
<!-- /run:mandate -->
' >> memory/builds/tRun/RUN.md
git add -A
hit "$(run)" "a run-state file does not carry exactly one well-formed mandate block on both sides of the BASE comparison; a second block is a second authorization nobody granted"

reset_tree; build tEmptyMandate
sed -i '/^The owner authorizes tEmptyMandate to merge and to push\.$/d' memory/builds/tEmptyMandate/RUN.md
sed -i "s/^witness: WITNESS$/witness: $(git rev-parse HEAD)/" memory/builds/tEmptyMandate/RUN.md
sed -i 's/^phase: RUNNING$/phase: LANDED/' memory/builds/tEmptyMandate/RUN.md
# The EMPTY-mandate file must exist AT THE ANCHOR, or check 13 branch 4 fires instead of branch 2.
git add -A && git commit -q -m emptymandate --no-verify && git push -q -f origin unit:main
git commit -q --allow-empty -m ahead --no-verify
sed -i "s/^base: BASE$/base: $(git merge-base origin/main HEAD)/" memory/builds/tEmptyMandate/RUN.md
git add -A && git commit -q -m rebase --no-verify
hit "$(run)" "the mandate block is absent or empty at the recorded BASE, so nothing committed before the run authorizes it"

reset_tree; build tNoBase
sed -i "s/^witness: WITNESS$/witness: $(git rev-parse HEAD)/" memory/builds/tNoBase/RUN.md
sed -i "s/^base: BASE$/base: $(git merge-base origin/main HEAD)/" memory/builds/tNoBase/RUN.md
sed -i 's/^phase: RUNNING$/phase: LANDED/' memory/builds/tNoBase/RUN.md
git add -A && git commit -q -m nobase --no-verify
hit "$(run)" "a run-state file does not exist at its own recorded BASE, so its mandate cannot have been committed before the run"

# ---- SOURCE-level: the leg must stay READ-ONLY. It runs on the merge bar, where a gate that writes
# ---- is a gate that can make the tree it is judging pass.
reset_tree
w=$(grep -nE '(^|[^-[:alnum:]])(mv|rm|cp|sed -i|tee|> *"?\$)' "$HERE/check-unattended.sh" \
    | grep -v '^[0-9]*: *#' || true)
n=$((n+1)); [ -z "$w" ] || { echo "FAIL the leg contains a write: $w"; st=1; }

[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
