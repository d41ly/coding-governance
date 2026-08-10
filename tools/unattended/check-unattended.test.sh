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
trap 'rm -rf "$TMP"' EXIT
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
EOF
}

mkconf; build tRun
git add -A && git commit -q -m base --no-verify
git checkout -q -b unit
BASE0=$(git rev-parse HEAD)
export GOV_DEFAULT_BRANCH=main
sed -i "s/^witness: WITNESS$/witness: $(git rev-parse HEAD)/" memory/builds/tRun/RUN.md
sed -i "s/^base: BASE$/base: $(git merge-base main HEAD)/" memory/builds/tRun/RUN.md
git add -A && git commit -q -m facts --no-verify
PRISTINE=$(git rev-parse HEAD)
reset_tree() { git reset -q --hard "$PRISTINE"; git clean -qfd; }
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

# ---- SOURCE-level: the leg must stay READ-ONLY. It runs on the merge bar, where a gate that writes
# ---- is a gate that can make the tree it is judging pass.
reset_tree
w=$(grep -nE '(^|[^-[:alnum:]])(mv|rm|cp|sed -i|tee|> *"?\$)' "$HERE/check-unattended.sh" \
    | grep -v '^[0-9]*: *#' || true)
n=$((n+1)); [ -z "$w" ] || { echo "FAIL the leg contains a write: $w"; st=1; }

[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
