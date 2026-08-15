#!/usr/bin/env bash
# Fixture self-test for unattended.sh — every refusal branch armed by a POSITIVE assertion naming
# its own failure text (which is what check-arms.py reads), plus the behavioural arms no message
# test can cover: that a refusal writes NOTHING, that the generated region is a COPY rather than a
# re-derivation, and that --status and --resume agree.
#
#   bash tools/unattended/unattended.test.sh    # "PASS (…assertions)" + exit 0 = good
#
# ONE scratch repo, reset between arms. Twenty-six git inits would triple the runtime and buy
# nothing: every arm's state is reachable from the pristine tree by a checkout and a clean.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="$HERE/unattended.sh"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP" "${ORIGIN_DIR:-}"' EXIT
st=0
n=0

# A POSITIVE assertion: the run's output must CONTAIN the branch's own failure text. `hit` is the
# only arming helper here; `miss` is deliberately spelled so check-arms scores it as negative.
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }
miss() { n=$((n+1)); if grep -qF -- "$2" <<<"$1"; then echo "FAIL unexpected: $2"; st=1; fi; }
same() { n=$((n+1)); [ "$2" = "$3" ] || { echo "FAIL $1: expected [$3], got [$2]"; st=1; }; }

cd "$TMP" || exit 2
git init -q -b main . && git config user.email t@t.test && git config user.name t \
  && git config core.autocrlf false

mkconf() { # wiring · gate
  cat > .unattended.conf <<EOF
MEMORY_ROOT=memory
LANDER="echo land"
BYPASS_BAN="--no-verify"
GATE_CMD="${2-true}"
WIRING_CHECK="${1-true}"
KEEPALIVE_CREATE="CronCreate"
KEEPALIVE_DELETE="CronDelete"
PHASES_EXTRA=""
DOD_EXTRA=""
EOF
}

readme() { # slug
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

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [ARCH-$1-1 — the unit](spec/one.md) | OPEN | rev-1 | 2026-08-01 |
<!-- /gen:build-index -->
EOF
}

runmd() { # slug · mandate-body
  mkdir -p "memory/builds/$1"
  cat > "memory/builds/$1/RUN.md" <<EOF
# $1 — run state

<!-- run:generated -->
<!-- /run:generated -->

## Mandate
<!-- run:mandate -->
$2
<!-- /run:mandate -->

## Run facts

## Parked
EOF
}

MANDATE="The owner authorizes build tRun to merge to main and to push."
mkconf
readme tRun
runmd tRun "$MANDATE"
# Both live ON MAIN, because the authorization is asked about the BASE. Producing either by editing on
# the unit branch is impossible by construction: the branch is exactly what the BASE is not.
mkdir -p memory/builds/tNoFm
printf 'not front matter at all

# tNoFm
' > memory/builds/tNoFm/README.md
readme tWrongSlug
sed -i 's/^slug: tWrongSlug$/slug: someoneElse/' memory/builds/tWrongSlug/README.md
# A build whose README is on MAIN and which never had a run-state file - S2's subject. Deleting
# tRun's would have worked only by making the tree dirty, which check 2 refuses first, so the arm
# would have tested the dirty-tree refusal while claiming to test creation.
readme tFresh
# TOOL-cBriefedPilot-4: the build-method carrier, which --preflight now REFUSES without. A stub,
# because the driver tests existence and nothing else; the file whose sections have to resolve lives
# in the LEG's fixture. It is created before the initial commit deliberately - every arm begins with
# `reset_tree`, which runs `git clean -qfd`, and an untracked stub would be deleted by the first one.
mkdir -p memory/guides
printf '# build method (stub)\n\n## M1\n\nExistence is what the driver tests.\n' > memory/guides/BUILD-METHOD.md
git add -A && git commit -q -m base --no-verify
# A REMOTE-TRACKING anchor, because that is now the only thing resolve_base will measure against: a
# bare local branch is a ref the run can move with `git branch -f`, and moving it to HEAD was a
# reproduced exploit. A bare repo one directory up is the cheapest honest origin.
# OUTSIDE the work tree. `reset_tree` runs `git clean -qfd`, which cheerfully deletes an untracked
# `origin.git` sitting inside the repo — the anchor vanishes and every later arm fails for a reason
# that has nothing to do with what it tests.
ORIGIN_DIR=$(mktemp -d); ORIGIN="$ORIGIN_DIR/origin.git"
# The bare repo must ADVERTISE a HEAD symref: the anchor is now read from the remote's own
# advertisement, and `git init --bare` leaves HEAD pointing at whatever init.defaultBranch says,
# which then dangles. MEASURED: `ls-remote --symref --exit-code HEAD` exits 2 against that, which
# is check 28 - so without this line every arm below dies on a refusal about the FIXTURE.
git init -q --bare "$ORIGIN"
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main
git remote add origin "$ORIGIN"
git push -q origin main
git checkout -q -b unit
# ...and the unit branch must be AHEAD of the anchor. merge-base == HEAD is now its own refusal:
# nothing was built on top of the anchor, so the mandate comparison would be trivially true.
git commit -q --allow-empty -m "unit work" --no-verify
BASE=$(git rev-parse main)
UNIT0=$(git rev-parse HEAD)
export GOV_DEFAULT_BRANCH=main

# Back to the pristine unit-branch tree. A HARD reset, not a checkout: several arms COMMIT their
# fixture (they have to — preflight refuses a dirty tree, so an uncommitted fixture would be
# reported as dirtiness instead of as the thing under test), and a checkout leaves those commits.
reset_tree() { git checkout -q unit 2>/dev/null; git reset -q --hard "$UNIT0"; git clean -qfd; mkconf; }

run() { bash "$SCRIPT" "$@" 2>&1; }
# Stage and commit the fixture edit. Preflight evaluates EVERY precondition before it writes, so a
# dirty fixture still arms the message arms — but it never reaches the write phase, which is where
# checks 9 and 17 live. Those arms have to commit.
fixture() { git add -A >/dev/null && git commit -q -m fixture --no-verify; }
sum() { git hash-object memory/builds/tRun/RUN.md; }

# ---- check 1: the slug is validated against hygiene check 4's OWN folder grammar, so a traversal
# ---- argument is refused by the rule that would have refused the folder. Paired with the no-write
# ---- arm, because "it printed a refusal" and "it changed nothing" are two claims.
reset_tree; before=$(sum)
out=$(run --status ../etc)
hit "$out" "the slug is not a build-folder name; expected the slug alone, a letter then letters, digits or dashes: ../etc"
same "check 1 wrote nothing" "$(sum)" "$before"

# ---- check 2: dirty tree. The check refreshes the stat cache first and then asks about CONTENT —
# ---- a linked worktree can report a path modified whose bytes are identical after the eol filter.
reset_tree; before=$(sum); printf 'scratch\n' > untracked.txt
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "the working tree is dirty, so the pinned BASE would name a state that is not what runs"
same "check 2 wrote nothing" "$(sum)" "$before"
rm -f untracked.txt

# ---- check 3's second branch USED to be reached by unsetting GOV_DEFAULT_BRANCH in a repo with no
# ---- origin/HEAD. The anchor is now OBSERVED from the remote, so that state resolves perfectly well
# ---- and the branch is reachable only when the observation ALSO fails - which is check 27's job and
# ---- has its own arm below. Unsetting the variable is now the NORMAL path, and asserting THAT is
# ---- worth more than asserting a message the state no longer produces: the environment has stopped
# ---- being an input to the anchor, which is exactly what route 2 of the reproduced bypass used.
reset_tree
out=$(env -u GOV_DEFAULT_BRANCH bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "preflight OK"
miss "$out" "cannot resolve the default branch"

reset_tree; git checkout -q main
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "the run is on the default branch, where its own commits would land unreviewed on the branch it means to merge INTO"
git checkout -q unit

# ---- check 4, all three branches: undeclared, declared-but-REPAIRING, and declared-and-failing.
# ---- The repairing arm is the one that matters most — a project can wire `--fix` here by accident
# ---- and every later green would be produced by a mode that rewrites tracked bytes.
reset_tree; mkconf ""
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "WIRING_CHECK is not declared in .unattended.conf — an undeclared wiring probe is not a passing one"

# The ban is an ALLOW-LIST, not a `*--fix*` blacklist. The fixture uses `--session`, which repairs
# and which the blacklist form let through — the arm that made the blacklist look like a check.
reset_tree; mkconf "true --session"
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "WIRING_CHECK carries a flag this kit does not recognise as READ-ONLY, and preflight delegates to a check rather than a fix; permitted: --check, --dry-run, --verify, -n"
reset_tree; mkconf "true --check"
miss "$(run --preflight tRun --keepalive-id k1)" "WIRING_CHECK carries a flag this kit does not recognise as READ-ONLY, and preflight delegates to a check rather than a fix; permitted: --check, --dry-run, --verify, -n"

reset_tree; mkconf "false"
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "the declared wiring check failed, and a dormant hook makes every later green meaningless"

# ---- check 5: a second non-terminal run-state file. Both are TRACKED, because the selector reads
# ---- git, not the filesystem — an untracked second run would leave this arm passing over one file.
reset_tree
readme tTwo; runmd tTwo "other"
printf 'phase: RUNNING\n' >> memory/builds/tTwo/RUN.md
sed -i 's/^## Run facts$/## Run facts\nphase: RUNNING/' memory/builds/tRun/RUN.md
git add -A && git commit -q -m two --no-verify
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "more than one run-state file is in a non-terminal phase, so 'the run' is not well-defined"

# ---- check 6: the build folder exists on the unit branch but NOT at the pinned BASE. The
# ---- self-authored case in its purest form - the run invented the build that authorizes it.
reset_tree
readme tNew
git add -A && git commit -q -m new --no-verify
out=$(run --preflight tNew --keepalive-id k1)
hit "$out" "no build README at the pinned BASE, so nothing committed before this run branched authorizes it, and a build folder the run created on its own branch authorizes nothing"

# ---- check 7: the path RESOLVES at the BASE and is not a build README. Distinct from check 6 on
# ---- purpose: "the folder is not there" and "it is there and is not a build" are different facts,
# ---- and collapsing them tells an operator to create something that already exists.
reset_tree
out=$(run --preflight tNoFm --keepalive-id k1)
hit "$out" "the blob at the pinned BASE is not a build README - front matter opens at line 1 and this does not, so the path resolved to something that is not a build"

# ---- check 20: the README at BASE declares a DIFFERENT slug - a folder renamed, or a README copied
# ---- from another build. The authorization resolves, and it does not name this build.
reset_tree
out=$(run --preflight tWrongSlug --keepalive-id k1)
hit "$out" "the build README at the pinned BASE declares a different slug, so the folder was renamed or its README copied from another build and the authorization does not name this one: declared"

# ---- S8, the roster region. OPT-IN by presence: a build without the markers authorizes on existence
# ---- alone, which is what keeps every build that predates this working.
roster() { # slug · body   (pure shell: a python launcher here is unresolved, and mkconf leaves the
           #                   tree dirty, which is what silently blocked the checkout below)
  printf '
%s
%s
%s
' '<!-- roster:units -->' "$2" '<!-- /roster:units -->' >> "memory/builds/$1/README.md"
}

# green control FIRST: a roster present at BASE and untouched must authorize.
reset_tree; git checkout -qf main; roster tRun "1. the first unit"
git add -A >/dev/null && git commit -q -m roster --no-verify && git push -q -f origin main
git checkout -qf unit && git merge -q --no-edit main >/dev/null 2>&1
# reset_tree rewinds to UNIT0, which PREDATES this merge - so the arms below would run against a tree
# with no roster at all and pass by finding nothing. Pin a post-merge pristine and reset to THAT.
RPRISTINE=$(git rev-parse HEAD)
rreset() { git reset -q --hard "$RPRISTINE"; git clean -qfd; mkconf; }
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "preflight OK"
miss "$out" "rewrote the scope"

# ...the run EDITS its own scope. Same tree, one line changed.
rreset
sed -i 's|^1\. the first unit$|1. a unit the owner never wrote|' memory/builds/tRun/README.md
hit "$(run --preflight tRun --keepalive-id k1)" "the roster differs from the one at the pinned BASE - the run rewrote the scope it is executing against, and a run that can edit its own scope mid-flight is not running the build that was authorized"

# ...a SECOND pair in the working copy. `region` conflates absent with duplicated, so this is the arm
# that proves the presence test is a grep and not that exit status.
rreset
roster tRun "1. a second roster nobody granted"
hit "$(run --preflight tRun --keepalive-id k1)" "the working copy's build README does not carry exactly one well-formed roster pair while the pinned BASE does, so the scope this run is executing against cannot be compared"
git checkout -q main; git reset -q --hard "$BASE"; git push -q -f origin main; git checkout -qf unit; reset_tree

# ...and the BASE side MALFORMED: two pairs committed to the anchor. Without this arm the
# grep-for-presence test and the well-formedness check cannot be told apart.
git checkout -qf main; roster tRun "1. one"; roster tRun "2. two"
git add -A >/dev/null && git commit -q -m tworoster --no-verify && git push -q -f origin main
git checkout -qf unit && git merge -q --no-edit main >/dev/null 2>&1
hit "$(run --preflight tRun --keepalive-id k1)" "the build README at the pinned BASE carries a roster marker but not exactly one well-formed pair, so there is no single scope to compare against"
git checkout -qf main; git reset -q --hard "$BASE"; git push -q -f origin main; git checkout -qf unit; reset_tree

# ...and ABSENT at BASE is still authorized - the opt-in half, without which every existing build breaks.
reset_tree
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "preflight OK"
miss "$out" "roster"

# ---- check 8: the keepalive id is the AGENT's half of the split. No script can produce it, so its
# ---- absence is a refusal rather than a default.
reset_tree
out=$(run --preflight tRun)
hit "$out" "no --keepalive-id was supplied — scheduling is the AGENT's half of the split and only the agent can do it; the driver records the id it is handed"

# ---- S2: a build with no run-state file is the NORMAL case now - preflight creates it and the owner
# ---- authors nothing, which is the whole point of this build. Three claims, three assertions: it
# ---- succeeds, the file exists, and it is STAGED. The third is not decoration - every check in the
# ---- gate leg iterates `git ls-files`, so an unstaged run-state file is a silent opt-out from the
# ---- entire leg.
reset_tree
out=$(run --preflight tFresh --keepalive-id k1)
hit "$out" "preflight OK"
n=$((n+1)); [ -f memory/builds/tFresh/RUN.md ] || { echo "FAIL preflight did not create the run-state file for a build that never had one"; st=1; }
same "the created run-state file is STAGED, or the gate leg cannot see the run" "$(git ls-files memory/builds/tFresh/RUN.md)" "memory/builds/tFresh/RUN.md"
git rm -q --cached memory/builds/tFresh/RUN.md >/dev/null 2>&1; rm -f memory/builds/tFresh/RUN.md

# ---- check 9 branch 1: the scaffold cannot write. A DIRECTORY where the run-state file belongs is
# ---- the cheapest unwritable path that does not need permissions this node may not honour, and an
# ---- empty directory is invisible to git, so check 2 stays green and this arm tests its own branch.
reset_tree
mkdir -p memory/builds/tFresh/RUN.md
out=$(run --preflight tFresh --keepalive-id k1)
hit "$out" "cannot create the run-state file, so there is nothing for the run to record its phase, witness and parked decisions in"
rmdir memory/builds/tFresh/RUN.md

# ---- check 29: THE SECOND REPORTED BYPASS ROUTE, closed. A bogus GOV_DEFAULT_BRANCH used to SELECT
# ---- which ref the anchor was measured against, and the gate leg read the same variable, so it
# ---- computed the same wrong value and agreed with it. It is now a cross-check that can only refuse.
reset_tree
out=$(GOV_DEFAULT_BRANCH=nosuchbranch bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "GOV_DEFAULT_BRANCH names a branch the remote does not advertise as its default, and a branch the run can create with one push is not an anchor: env"

# ---- check 29, the direction that matters. A branch that genuinely EXISTS on the remote, pushed by
# ---- the run itself, is refused just the same. Without this arm check 29 reads as "the name must
# ---- resolve" - which is the weaker property a run defeats with one `git push`.
reset_tree
git push -q origin unit:refs/heads/decoy 2>/dev/null
out=$(GOV_DEFAULT_BRANCH=decoy bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "GOV_DEFAULT_BRANCH names a branch the remote does not advertise as its default"
git push -q origin :refs/heads/decoy 2>/dev/null

# ---- check 16: no shared history with the advertised tip. Reachable now only from an orphan branch,
# ---- because the anchor is no longer a NAME that can simply fail to resolve.
reset_tree
git checkout -q --orphan orphanb
git rm -rqf . >/dev/null 2>&1 || true
mkconf; readme tRun; runmd tRun "$MANDATE"
git add -A >/dev/null && git commit -q -m orphan --no-verify
out=$(bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "no merge-base against the tip the remote advertises, so this run shares no history with the branch it means to land on; the anchor is never a local ref and never a name from the environment"
git checkout -qf unit; git branch -qD orphanb 2>/dev/null

# ---- check 27: the remote does not answer. The anchor is an OBSERVATION, so an unreachable remote
# ---- is a refusal and not a fallback - and the fallback is exactly what used to be forgeable.
reset_tree
git remote set-url origin "$ORIGIN_DIR/nope.git"
out=$(bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "the remote did not answer, and the anchor is an observation of it rather than of any local ref; a run that cannot reach the remote cannot land on it either"
git remote set-url origin "$ORIGIN"

# ---- check 3 branch 2: the default branch cannot be named AT ALL. Reachable only when the
# ---- observation fails too, which is why it sits here rather than where it used to: with an anchor
# ---- observed, `default_branch` answers from the advertisement and this branch is unreachable.
reset_tree
git remote set-url origin "$ORIGIN_DIR/nope.git"
out=$(env -u GOV_DEFAULT_BRANCH bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "cannot resolve the default branch (set GOV_DEFAULT_BRANCH) — refusing rather than assuming one"
git remote set-url origin "$ORIGIN"

# ---- check 28: the remote answers but advertises no HEAD of its own. `--exit-code` is what makes
# ---- this distinguishable from a successful answer: without it `ls-remote` exits 0 printing nothing,
# ---- and the kit would read an empty advertisement as agreement.
reset_tree
git init -q --bare "$ORIGIN_DIR/headless.git"
git remote set-url origin "$ORIGIN_DIR/headless.git"
out=$(bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "the remote answered but advertised no HEAD symref, so it named no default branch of its own and this kit will not choose one for it"
git remote set-url origin "$ORIGIN"

# ---- check 30: the remote advertises a tip this clone does not have. Built INSIDE the bare repo, so
# ---- the object genuinely does not exist here - pushing one from this clone would leave it present.
reset_tree
ahead=$(git --git-dir="$ORIGIN" commit-tree "$(git --git-dir="$ORIGIN" rev-parse main^{tree})" -p "$(git --git-dir="$ORIGIN" rev-parse main)" -m ahead)
git --git-dir="$ORIGIN" update-ref refs/heads/main "$ahead"
out=$(bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "the remote advertises a tip this clone does not have, so no merge-base can be computed against it; fetch and re-run"
git --git-dir="$ORIGIN" update-ref refs/heads/main "$BASE"

# ---- check 24: more than one remote, so the kit would be CHOOSING which endpoint to believe.
reset_tree
git remote add second "$ORIGIN"
out=$(bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "this clone declares a number of remotes other than one, and the anchor has to be the endpoint the landing push goes to, so the kit refuses to pick one"
git remote remove second

# ---- check 25: observe and push name different endpoints. Labelled a cost-raiser at the call site
# ---- rather than part of the property, because a relay satisfies it with a single URL.
reset_tree
git config remote.origin.pushurl "$ORIGIN_DIR/elsewhere.git"
out=$(bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "the URL this clone would OBSERVE is not the URL it would PUSH to, so the anchor and the landing name two different endpoints: fetch"
git config --unset remote.origin.pushurl

# ---- check 22: git config supplied through the ENVIRONMENT.
reset_tree
out=$(GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.bare GIT_CONFIG_VALUE_0=false bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "git configuration is being supplied through the environment, and a check that reads a config its own caller injected is reading the run's answer rather than the repo's"

# ---- check 23: an object-substitution lever left on disk. Refused BEFORE the mandate comparison,
# ---- which is why the pin's end-to-end arm below asserts this message rather than check 7's.
reset_tree
git replace -f "$BASE" "$(git commit-tree "$(git rev-parse 'HEAD^{tree}')" -m lever)" >/dev/null 2>&1
out=$(bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "this clone carries an object-substitution lever, which rewrites what a sha MEANS for every read below it, so the anchor can be honest and the bytes at it forged"
git replace -d "$BASE" >/dev/null 2>&1

# ...and the OTHER half of the same rule: a resolvable anchor that sits AT HEAD. This is the state
# `git branch -f main HEAD` used to produce, and it defeated the whole kit — the mandate at BASE was
# the mandate the run had just written. Refusing to fall back to HEAD is not the same as refusing to
# BE at HEAD, and only the first was implemented.
# ---- S3 SPLIT THIS ONE by verb. The state is legal at --preflight, where a run has correctly built
# ---- nothing yet, and a refusal at --close, where a run that built nothing has nothing to land. Both
# ---- arms run against the SAME fixture one command apart, which is the only way to show it is the
# ---- VERB that differs and not the tree.
# ---- ...and after unit 2 the split SURVIVES but --close's refusal is CONDITIONAL. All four branches
# ---- run against one fixture, which is still the only way to show the verb differs and not the tree.
reset_tree; git push -q -f origin unit:main
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "preflight OK"
miss "$out" "the recorded BASE equals HEAD"
# BRANCH 1 — the run that built NOTHING. preflight pinned the base AT HEAD through the degenerate
# path, so the recorded value still equals HEAD and there is nothing to land. This is the property
# the old unconditional refusal bought, and it is the one that had to survive the narrowing.
out=$(run --close tRun)
hit "$out" "the recorded BASE equals HEAD, so this run built nothing on top of the anchor and has nothing to land; that is the state the merge-base could not distinguish from a landed one"

# BRANCH 2 — an ABSENT discriminator FAILS CLOSED. Deleting one line from a run-written file must not
# be the way past this refusal; the kit's recorded scar is a deleted base line degenerating a
# comparison to the git index, and this is the same shape one verb over.
sed -i '/^base: /d' memory/builds/tRun/RUN.md
hit "$(run --close tRun)" "the merge-base equals HEAD and the record pins no BASE to tell a landed run from one that built nothing, and an absent discriminator is a refusal rather than a pass"

# BRANCH 3 — a base off the history the anchor blesses. The early return this replaces SKIPPED the
# cross-check entirely, so --close now runs a comparison on this path that no caller used to run.
reset_tree; git push -q -f origin unit:main
run --preflight tRun --keepalive-id k1 >/dev/null
# An ORPHAN commit — a real object in this repo that is on no history HEAD reaches. `commit-tree`
# with no parent is the cheapest way to get one, and it is a genuine commit rather than a
# rev-parse failure, so this arm tests ANCESTRY and not resolvability.
ALIEN=$(git commit-tree "$(git rev-parse HEAD^{tree})" -m alien </dev/null)
sed -i "s/^base: .*/base: $ALIEN/" memory/builds/tRun/RUN.md
hit "$(run --close tRun)" "the BASE recorded in the run-state file is not an ancestor of the base this history derives"

# BRANCH 4 — THE POINT OF THE UNIT: a run whose work is fully LANDED can close. Same degenerate
# merge-base as branch 1, and the only difference is that the recorded base is no longer HEAD —
# which is exactly the discriminator the merge-base cannot express.
reset_tree; git push -q -f origin unit:main
run --preflight tRun --keepalive-id k1 >/dev/null
printf 'keepalive-reaped: yes\nparked-surfaced: yes\n' >> memory/builds/tRun/RUN.md
fixture
git push -q -f origin HEAD:main
out=$(run --close tRun)
miss "$out" "the recorded BASE equals HEAD"
miss "$out" "an absent discriminator is a refusal"
hit "$out" "close OK"
same "the landed run reached LANDING" "$(sed -n 's/^phase: //p' memory/builds/tRun/RUN.md)" "LANDING"
git push -q -f origin "$BASE":main

# ---- check 9, both branches: the marker pair is malformed in the SOURCE and in the TARGET. The
# ---- source arm is the one a re-deriving driver would not have — this one copies, so a broken
# ---- pair upstream is a refusal rather than something to guess around.
reset_tree; sed -i '/<!-- \/gen:build-index -->/d' memory/builds/tRun/README.md; fixture; before=$(sum)
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "the build README's generated markers are malformed, and the region is COPIED from there, so an unpaired marker is not something to guess around"
same "check 9.1 wrote nothing" "$(sum)" "$before"

reset_tree; sed -i '/<!-- \/run:generated -->/d' memory/builds/tRun/RUN.md; fixture
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "the run-state file's generated markers are malformed — exactly one open and one close, close after open"

# ---- check 17: the splice succeeded but there is nowhere to record a fact. Without this branch the
# ---- verb would report a successful preflight over a file carrying none of the facts it claimed.
reset_tree; sed -i '/^## Run facts$/d' memory/builds/tRun/RUN.md; fixture
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "cannot record a run fact — the file carries neither that key's line nor a Run facts heading to put one under"

# ---- THE HAPPY PATH, and the four behavioural claims no message arm can make.
reset_tree
out=$(run --preflight tRun --keepalive-id KA-1234)
hit "$out" "preflight OK"
# the region is a COPY: byte-identical to the README's slice, not a re-render of the same data
slice() { awk -v o="$2" -v c="$3" 'index($0,o)==1{i=1;next} index($0,c)==1{i=0;next} i' "$1"; }
same "the generated region is a byte copy of the README slice" \
  "$(slice memory/builds/tRun/RUN.md '<!-- run:generated -->' '<!-- /run:generated -->' | git hash-object --stdin)" \
  "$(slice memory/builds/tRun/README.md '<!-- gen:build-index -->' '<!-- /gen:build-index -->' | git hash-object --stdin)"
same "the recorded BASE is the merge-base" \
  "$(sed -n 's/^base: //p' memory/builds/tRun/RUN.md)" "$BASE"
same "the keepalive id is recorded verbatim" \
  "$(sed -n 's/^keepalive: //p' memory/builds/tRun/RUN.md)" "KA-1234"

# ---- check 11: a phase with no witness. Asserted by REMOVING the witness preflight just wrote, so
# ---- the arm cannot be satisfied by a file that never had one.
fixture
sed -i '/^witness: /d' memory/builds/tRun/RUN.md
out=$(run --status tRun)
hit "$out" "the phase carries no witness, and presence is its own refusal: an oracle that skips an unwitnessed claim makes naming no witness the cheapest way to say nothing. Phase"
git checkout -q -- memory/builds/tRun/RUN.md

# ---- --status and --resume must AGREE. Two answers to one question is the class this whole build
# ---- exists to remove, so the arm compares the shared line rather than each verb's own wording.
sout=$(run --status tRun); rout=$(run --resume tRun)
same "resume reproduces the status line" \
  "$(grep -c "$(printf '%s' "$sout" | head -1)" <<<"$rout")" "1"
hit "$sout" "phase RUNNING"
hit "$rout" "resume at phase RUNNING"
hit "$sout" "next ARCH-tRun-1"

# ---- check 10, all three branches: no file for --status, no phase, no file for --close.
reset_tree; readme tNoRun; fixture
out=$(run --status tNoRun);  hit "$out" "no run-state file, so there is no run to report on"
out=$(run --close tNoRun);   hit "$out" "no run-state file, so there is no run to close"
reset_tree
out=$(run --status tRun)
hit "$out" "the run-state file declares no phase, and a run with no phase is not resumable"

# ---- check 12, both branches: an override naming an undeclared item, and one with no reason.
reset_tree
out=$(run --close tRun --override no-such-item --reason "because")
hit "$out" "--override names an item that is not in the declared DoD set, and an override on an item nobody declared is not an override"
out=$(run --close tRun --override gates-green)
hit "$out" "--override requires --reason: an unrecorded override is indistinguishable from a passing check"

# ---- check 13, both branches, each ISOLATED so the arm names the right one. Agent-attested first:
# ---- every machine item is satisfied, so only the attested pair can be unmet.
reset_tree; run --preflight tRun --keepalive-id KA-1234 >/dev/null
out=$(run --close tRun)
hit "$out" "an agent-attested DoD item is unmet; the driver can only read back what the agent recorded, so this is an attestation, not a machine verdict"
miss "$out" "a machine-checked DoD item is unmet, so --close blocks"

# ...then the machine branch, with both attestations recorded so ONLY the gate command can fail.
printf 'keepalive-reaped: yes\nparked-surfaced: yes\n' >> memory/builds/tRun/RUN.md
mkconf "true" "false"
out=$(run --close tRun)
hit "$out" "a machine-checked DoD item is unmet, so --close blocks"
hit "$out" "gates-green"

# ---- the override PATH, end to end: the blocked item is overridden, the run closes, and the reason
# ---- is written as a parked entry. A blocking gate with an override nobody can read is not a gate.
out=$(run --close tRun --override gates-green --reason "the bar was run by hand at the pinned base")
hit "$out" "close OK"
hit "$(cat memory/builds/tRun/RUN.md)" "the bar was run by hand at the pinned base"
same "the phase advanced to LANDING" \
  "$(sed -n 's/^phase: //p' memory/builds/tRun/RUN.md)" "LANDING"

# ---- TOOL-cBriefedPilot-1: the override REPEATS. The scalar form overwrote the first pair, so
# ---- verb_close blocked on the second unmet item forever with nobody to read the block.
reset_tree; run --preflight tRun --keepalive-id KA-1234 >/dev/null
printf 'keepalive-reaped: yes\nparked-surfaced: yes\n' >> memory/builds/tRun/RUN.md
mkconf "false" "false"
out=$(run --close tRun --override gates-green --reason "bar run by hand" --override records-current --reason "index re-rendered by hand")
hit "$out" "close OK"
hit "$out" "override recorded for 'gates-green'"
hit "$out" "override recorded for 'records-current'"
hit "$(cat memory/builds/tRun/RUN.md)" "bar run by hand"
hit "$(cat memory/builds/tRun/RUN.md)" "index re-rendered by hand"
same "two overrides parked, not one" "$(grep -c 'override · item ' memory/builds/tRun/RUN.md)" "2"

# ---- the non-overridable item refuses wherever it sits, not only last. The scalar form could only
# ---- ever see the FINAL pair, so a first-position authorization-reachable was invisible to it.
reset_tree; run --preflight tRun --keepalive-id KA-1234 >/dev/null
out=$(run --close tRun --override authorization-reachable --reason "first" --override gates-green --reason "second")
hit "$out" "the authorization item is NOT overridable"
miss "$out" "close OK"

# ---- a flag left pending when argv ends keeps its EMPTY reason, so it meets the missing-reason
# ---- refusal that already exists rather than vanishing. No second branch was added for it.
out=$(run --close tRun --override gates-green --reason "has one" --override records-current)
hit "$out" "--override requires --reason: an unrecorded override is indistinguishable from a passing check"
miss "$out" "close OK"

# ---- TOOL-cBriefedPilot-4: --preflight REFUSES a tree with no build-method carrier. Every
# ---- directive is a pointer into a section of that file, so a run without it is bound by a set
# ---- that resolves to nothing. The refusal joins the precondition block, so it writes nothing.
reset_tree
rm -f memory/guides/BUILD-METHOD.md
# COMMIT the removal. Left dirty, check_clean refuses first and the two assertions below are
# satisfied by the dirty-tree path instead of by the subject - over-determined, and they would
# stay green with this unit's branch deleted. Observed: only the message arm went red.
fixture
out=$(run --preflight tFresh --keepalive-id KA-1234)
hit "$out" "no build method under the memory root, so every directive this run is bound by points into a file that does not exist:"
hit "$out" "unattended: --preflight refused; the run-state file is unchanged"
present=$([ -e memory/builds/tFresh/RUN.md ] && echo present || echo absent)
same "a refused preflight left NO run-state file" "$present" "absent"

# ---- the green control. Without it the arm above passes on ANY preflight failure, which is the
# ---- fixture-passes-by-finding-nothing class this repo has already paid for once.
reset_tree
out=$(run --preflight tFresh --keepalive-id KA-1234)
hit "$out" "preflight OK"
miss "$out" "no build method under the memory root, so every directive this run is bound by points into a file that does not exist:"

# ---- TOOL-cBriefedPilot-5: the BASE is pinned ONCE. Re-preflight is the verb a run is TOLD to
# ---- re-run after a compaction, and it used to re-pin against a merge-base that had moved - which
# ---- the mandated lander makes happen on most runs, because it reconciles origin before the gate.
reset_tree
run --preflight tRun --keepalive-id k1 >/dev/null
base1=$(sed -n "s/^base: //p" memory/builds/tRun/RUN.md)
same "the first preflight wrote a base" "$([ -n "$base1" ] && echo yes || echo no)" "yes"
# advance the anchor and reconcile it, which is exactly what the lander does before the gate
git -C "$ORIGIN" --work-tree=. --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main 2>/dev/null || true
git checkout -q main && echo advance >> advance.txt && git add -A && git commit -q -m advance --no-verify
git push -q "$ORIGIN" main 2>/dev/null || true
git checkout -q unit && git merge -q --no-edit main >/dev/null 2>&1 || true
git fetch -q "$ORIGIN" 2>/dev/null || true
out=$(run --preflight tRun --keepalive-id k1)
base2=$(sed -n "s/^base: //p" memory/builds/tRun/RUN.md)
same "the base did not move on the second preflight" "$base2" "$base1"
hit "$out" "base $base1"

# ---- S6, the phase PRODUCER. Three branches and one behavioural claim.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
out=$(run --phase tRun BUILDING --witness "$(git rev-parse HEAD)")
hit "$out" "phase BUILDING"
same "the phase was actually written" "$(sed -n 's/^phase: //p' memory/builds/tRun/RUN.md)" "BUILDING"

# ...and preflight must NOT move it back. It used to rewrite the phase unconditionally, so the very
# verb a compaction-resumed run is told to re-run silently reset its position to RUNNING.
# COMMIT the phase move first. Without this the re-run preflight refuses on a DIRTY TREE, so the
# phase survives because nothing ran - the arm passed with the guard reverted, which is this
# repo's own fixture-passes-by-finding-nothing class inside the kit meant to make runs checkable.
git add -A >/dev/null; git commit -q -m "phase moved" --no-verify
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "preflight OK"
same "a re-run preflight leaves a reached phase alone" "$(sed -n 's/^phase: //p' memory/builds/tRun/RUN.md)" "BUILDING"

reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
hit "$(run --phase tRun NOSUCHPHASE --witness abc)" "the phase is not in the declared vocabulary, and a phase nothing recognises is not a position"
hit "$(run --phase tRun BUILDING)" "a phase claim carries a WITNESS - a sha, a tag or a run id - and presence is its own refusal because an unwitnessed claim is the one an oracle skips"
reset_tree
hit "$(run --phase tBare BUILDING --witness abc)" "no run-state file, so there is no run to move"

# ...and a TERMINAL phase is refused here whatever the vocabulary says. Membership is not permission:
# a run that could set LANDED through this verb would skip the entire Definition-of-Done gate, and
# the two agent-attested items are enforced in no other place.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
hit "$(run --phase tRun LANDED --witness abc)" "a terminal phase is written by --landed or --abort, which evaluate what it claims, and not by this verb, because reaching it through here would skip the whole Definition-of-Done gate"
miss "$(run --phase tRun BUILDING --witness abc)" "a terminal phase is written by --landed or --abort"

# ---- S9: LANDING is CLOSE-ONLY, and this branch is what makes --landed's precondition mean
# ---- anything. LANDING is an ordinary non-terminal vocabulary member, so before this refusal
# ---- `--phase tRun LANDING` wrote it and `--landed` then reached LANDED with dod_met never invoked
# ---- — the exact hole the terminal refusal above exists to close, reachable in one command. The
# ---- GREEN CONTROL is the line below it: an ordinary phase move is untouched, or this arm proves
# ---- only that --phase can refuse.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
before=$(sum)
hit "$(run --phase tRun LANDING --witness abc)" "LANDING is written by --close alone, because it is the record that the Definition-of-Done set was evaluated; a phase move into it would be that claim without the evaluation"
same "the refused LANDING move wrote nothing" "$(sum)" "$before"
miss "$(run --phase tRun BUILDING --witness abc)" "LANDING is written by --close alone"

# ---- F6: a FINISHED run cannot be re-opened. This is the third of the three fixes the aStandingWrit
# ---- review's F2 asked for and the only one never built — because before the producers below, no
# ---- record could BE terminal. Without it, one --phase call returns a LANDED run to the single-live
# ---- counter that leg check 7 reds on.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: LANDED/' memory/builds/tRun/RUN.md
hit "$(run --phase tRun BUILDING --witness abc)" "the run is already finished and a finished record is not something to move, re-open or re-pin; every later run is measured against the counter this record left, and the verb that would rewrite it names itself here"

# ...and the run-state file cannot be staged. A DIRECTORY at the index path is the cheapest failure
# that needs no permissions this node may not honour.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
git rm -q --cached memory/builds/tRun/RUN.md >/dev/null 2>&1 || true
git commit -q -m untrack --no-verify >/dev/null 2>&1 || true
mkdir -p .git/index-blocked 2>/dev/null || true

# ---- S4, the gap list. The states are the build method's M2 vocabulary, spelled exactly; what is
# ---- asserted here is that this verb COMPUTES them, never that it defines them.
mkspec() { # slug · id · status · scope · acceptance · gates · forks
  mkdir -p "memory/builds/$1/spec"
  cat > "memory/builds/$1/spec/2026-08-01-spec-$1-1.md" <<SPEC
# $2 — a unit

**Status:** $3 · rev-1 · 2026-08-01 · node a · Tier-2 · base abcdef12 · streams architecture

## 1. Goal
g
## 2. Scope (IN)
$4
## 3. Non-goals (OUT)
n
## 4. Design
d
## 5. Production-readiness checklist
c
## 6. Acceptance criteria
$5
## 7. Gates
$6
## 8. Open questions
$7
## 9. Revision log
- rev-1
## 10. Reuse audit
r
SPEC
}

reset_tree; readme tPlan; mkspec tPlan ARCH-tPlan-1 SPECCED "S1 a thing" "AC1 it works" "the bar" "none"; fixture
out=$(run --plan tPlan)
hit "$out" "READY"
hit "$out" "next: ARCH-tPlan-1 (READY - build it)"
git reset -q --hard HEAD~1; git clean -qfd

reset_tree; readme tPlan; mkspec tPlan ARCH-tPlan-1 SPECCED "S1 a thing" "" "the bar" "none"; fixture
hit "$(run --plan tPlan)" "THIN"
git reset -q --hard HEAD~1; git clean -qfd

reset_tree; readme tPlan; mkspec tPlan ARCH-tPlan-1 SPECCED "S1 a thing" "AC1 it works" "the bar" "F1 which way?"; fixture
hit "$(run --plan tPlan)" "FORKED"
git reset -q --hard HEAD~1; git clean -qfd

# ...and THIN wins over FORKED, because M2 orders the checks and the first match wins. Without this
# arm the two are indistinguishable whenever a spec is both.
reset_tree; readme tPlan; mkspec tPlan ARCH-tPlan-1 SPECCED "" "AC1 it works" "the bar" "F1 which way?"; fixture
out=$(run --plan tPlan)
hit "$out" "THIN"
miss "$out" "FORKED"
git reset -q --hard HEAD~1; git clean -qfd

# ...a terminal spec is DONE whatever its sections say, and is never the next target.
reset_tree; readme tPlan; mkspec tPlan ARCH-tPlan-1 CLOSED "" "" "" "F1 unresolved"; fixture
out=$(run --plan tPlan)
hit "$out" "DONE"
hit "$out" "next: none - every tracked spec is terminal"
git reset -q --hard HEAD~1; git clean -qfd

# ...and a build with no tracked spec REFUSES rather than printing an empty, complete-looking list.
reset_tree; readme tPlanEmpty; fixture
hit "$(run --plan tPlanEmpty)" "no tracked spec under this build, so every planned unit is MISSING and this verb cannot say which - the roster it would need is the README's authored Units table, which it does not parse"
git reset -q --hard HEAD~1; git clean -qfd

# ---- check 14: an unknown argument. The verbs are a closed set.
out=$(run --frobnicate tRun)
hit "$out" "unknown argument; the verbs are --preflight, --plan, --phase, --status, --resume, --close, --landed and --abort: --frobnicate"
# ---- S10: the THREE enumerations name ONE set. The usage line was two verbs behind before this unit
# ---- and the refusal above is what an operator who mistypes a verb actually reads. Assert every verb
# ---- appears in all three, or the next verb repeats the drift a prior review already asked to fix.
for v in --preflight --plan --phase --status --resume --close --landed --abort; do
  n=$((n+1))
  [ "$(grep -cE "^#   unattended\.sh $v( |$)" "$SCRIPT")" -ge 1 ] \
    || { echo "FAIL the header docstring omits $v"; st=1; }
  n=$((n+1))
  [ "$(sed -n '/^\[ -n "\$VERB" \]/p' "$SCRIPT" | grep -cF -- "$v")" -ge 1 ] \
    || { echo "FAIL the usage line omits $v"; st=1; }
done

# ---- check 18: the recorded BASE is EVIDENCE, never the input. --close used to read it straight
# ---- out of the run-state file — a file the run writes — and an absent line degenerated the
# ---- comparison to `git show ":path"`, the git INDEX, so both sides were bytes the run had staged.
# ---- A forged mandate passed. Now the base is re-derived and the recorded one must agree with it.
reset_tree; run --preflight tRun --keepalive-id KA-1234 >/dev/null
sed -i 's/^base: .*/base: 0000000000000000000000000000000000000000/' memory/builds/tRun/RUN.md
hit "$(run --close tRun)" "the BASE recorded in the run-state file does not resolve to a commit in this history, and the recorded value is written by the run: recorded"

# ---- check 18, branch 2: a base that RESOLVES but sits off the shared history. This is the case
# ---- that must still refuse after the test moved from equality to ancestry — a run forging its pin
# ---- to a commit it authored on its own branch. HEAD is exactly that shape: an ancestor of HEAD,
# ---- never an ancestor of the merge-base the anchor and this history share.
reset_tree; run --preflight tRun --keepalive-id KA-1234 >/dev/null
sed -i "s/^base: .*/base: $(git rev-parse HEAD)/" memory/builds/tRun/RUN.md
hit "$(run --close tRun)" "the BASE recorded in the run-state file is not an ancestor of the base this history derives, so it names a commit off the history the anchor blesses - which is where a run's own commits live: recorded"

# ---- check 18, THE POSITIVE ARM, and the reason this check moved off equality at all. A base that
# ---- is an ANCESTOR of the derived one is the ordinary state after a reconcile — which the MANDATED
# ---- lander performs before the gate — so equality refused every run whose remote had moved, on the
# ---- one path it is required to take. Reproduced live with no attacker anywhere near it. Ancestry
# ---- must ACCEPT it, or the fix is only a differently-worded wedge.
reset_tree; run --preflight tRun --keepalive-id KA-1234 >/dev/null
sed -i "s/^base: .*/base: $(git rev-parse HEAD~1)/" memory/builds/tRun/RUN.md
miss "$(run --close tRun 2>&1)" "the BASE recorded in the run-state file"

# ...and the DELETED-line case, which was THE exploitable one: an absent `base:` used to degenerate
# the comparison to the git index, so both sides became bytes the run had just staged. It is no
# longer a hazard at all - `trusted_base` DERIVES the value when the record carries none, so the item
# is evaluated honestly instead of silently satisfied. Assert the HARMLESSNESS, because a reader
# cannot otherwise tell a closed hole from an untested one.
reset_tree; run --preflight tRun --keepalive-id KA-1234 >/dev/null
sed -i '/^base: /d' memory/builds/tRun/RUN.md
printf 'keepalive-reaped: yes
parked-surfaced: yes
' >> memory/builds/tRun/RUN.md
git add -A
out=$(run --close tRun)
miss "$out" "authorization-reachable"

# ...and the item GENUINELY unmet, which is now a different fixture entirely: a build whose README is
# not at the pinned BASE because the run created it. The close-side twin of check 6.
reset_tree
readme tNew; runmd tNew "irrelevant now"
printf 'phase: RUNNING
keepalive-reaped: yes
parked-surfaced: yes
' >> memory/builds/tNew/RUN.md
fixture
out=$(run --close tNew)
hit "$out" "a machine-checked DoD item is unmet, so --close blocks"
hit "$out" "authorization-reachable"
miss "$out" "close OK"
git reset -q --hard HEAD~1; git clean -qfd

# ---- check 21: the authorization item is NOT overridable. The generic override loop accepted it,
# ---- which makes the override on the authorization check BE the authorization check — and the
# ---- protocol says in one sentence that there is no override for this one.
reset_tree
hit "$(run --close tRun --override authorization-reachable --reason "trust me")" "the authorization item is NOT overridable; an override on the authorization check IS the authorization check, and the protocol states there is no override for this one"

# ---- THE DEREFERENCE PIN. A sha is a NAME, and both levers below rewrite what it resolves to at a
# ---- PERFECTLY HONEST anchor - so no amount of anchor hardening closes either, and an anchor fix
# ---- shipped without this would have read forged bytes at a sha it had just proved trustworthy.
# ---- Each arm carries a LIVE CONTROL proving the forgery is real in THIS fixture on THIS node,
# ---- because without one "the driver refused" is indistinguishable from "the attack never worked
# ---- here" - and the second reading passes against a driver with no pin at all.
reset_tree
runmd tEmpty "$MANDATE"        # the run writes, in its own working copy, the mandate it wants to have
fixture
FORGED=$(git commit-tree "$(git rev-parse 'HEAD^{tree}')" -m forged)
git replace -f "$BASE" "$FORGED" >/dev/null 2>&1
# control — the substitution IS in force for an unpinned read at the unchanged BASE sha.
same "replace-control: an unpinned read at BASE returns the run's bytes"      "$(git show "$BASE:memory/builds/tEmpty/RUN.md" 2>/dev/null | grep -c "authorizes build")" "1"
# control — and the pinned read at the SAME sha does not.
same "replace-control: the pinned read at BASE returns the honest bytes"      "$(git -c core.useReplaceRefs=false show "$BASE:memory/builds/tEmpty/RUN.md" 2>/dev/null | grep -c "authorizes build")" "0"
# the arm — the run is refused. Note WHICH refusal: check 23 sees the lever on disk and stops before
# the mandate comparison is reached, so this end-to-end assertion proves the TRIPWIRE, not the pin.
# The pin is proved by the two controls above, which compare a pinned and an unpinned read at the
# SAME sha, and by the source-level arms below. Saying so matters: an end-to-end arm that would pass
# with the pin deleted is not evidence for the pin, and this one would.
hit "$(run --preflight tEmpty --keepalive-id k1)" "this clone carries an object-substitution lever"
git replace -d "$BASE" >/dev/null 2>&1

# ---- The GRAFT flavour cannot be made exploitable in this fixture without rewriting the branch
# ---- topology every other arm depends on, so it is armed where it is honest: that the suppression
# ---- this node's git actually needs is IN FORCE. `-c core.useReplaceRefs=false` and
# ---- GIT_NO_REPLACE_OBJECTS=1 were both MEASURED to leave a graft fully effective; only pointing
# ---- GIT_GRAFT_FILE away from the repo restored the honest answer. That is version-dependent
# ---- behaviour, so it is measured here rather than trusted.
gtmp=$(mktemp -d)
( cd "$gtmp" && git init -q -b main . && git config user.email t@t.test && git config user.name t   && echo a > f && git add f && git commit -q -m A --no-verify   && git checkout -q --orphan side && echo z > f && git add f && git commit -q -m Z --no-verify ) >/dev/null 2>&1
groot=$(git -C "$gtmp" rev-parse main); gz=$(git -C "$gtmp" rev-parse side)
# ABSOLUTE, deliberately. `rev-parse --git-path` prints a path relative to the REPO, and this shell's
# cwd is the outer scratch repo - redirecting to it wrote the graft into the wrong .git entirely, and
# the control then failed for a reason that had nothing to do with grafts.
mkdir -p "$gtmp/.git/info"
printf '%s %s
' "$groot" "$gz" > "$gtmp/.git/info/grafts"
same "graft-control: the graft gives two unrelated histories a merge-base"      "$(git -C "$gtmp" merge-base "$gz" main 2>/dev/null)" "$gz"
same "graft-arm: GIT_GRAFT_FILE suppresses it, which is what the driver exports"      "$(GIT_GRAFT_FILE=/dev/null git -C "$gtmp" merge-base "$gz" main 2>/dev/null)" ""
rm -rf "$gtmp"

# ---- SOURCE-level: the pin is EXPORTED and every dereference on the authorization path goes through
# ---- it. A pin that one call site skips is not a pin - that call site is the whole attack surface.
n=$((n+1)); grep -q '^export GIT_GRAFT_FILE=/dev/null' "$SCRIPT"   || { echo "FAIL the driver does not export GIT_GRAFT_FILE, so a graft file rewrites its merge-base"; st=1; }
n=$((n+1)); grep -q '^GIT() { git -c core.useReplaceRefs=false' "$SCRIPT"   || { echo "FAIL the driver defines no GIT() wrapper pinning core.useReplaceRefs"; st=1; }
unpinned=$(grep -nE '\$\(git (show|merge-base) |[^A-Z]git show "\$(base|rb):' "$SCRIPT" | grep -v '^[0-9]*: *#' || true)
n=$((n+1)); [ -z "$unpinned" ] || { echo "FAIL a dereference on the authorization path bypasses the GIT() pin: $unpinned"; st=1; }

# ---- SOURCE-level: every `check_authorization` call site is GUARDED by `trusted_base`. There is no
# ---- runtime guard inside check_mandate for an empty base, deliberately — it would be a branch no
# ---- fixture could reach — so the invariant is asserted against the text instead. An unguarded
# ---- call would restore the `git show ":path"` index read that made a forged mandate pass.
ug=$(grep -n 'check_authorization "' "$SCRIPT" | grep -v 'trusted_base' | grep -v '^\s*#' || true)
n=$((n+1))
while IFS= read -r ln; do
  [ -n "$ln" ] || continue
  no=${ln%%:*}
  sed -n "$((no-4)),${no}p" "$SCRIPT" | grep -q 'trusted_base'     || { echo "FAIL check_authorization is called without a trusted_base guard within 4 lines: $ln"; st=1; }
done <<<"$ug"

# ---- SOURCE-level: the driver must not grow a python dependency. Every other kit here carries the
# ---- launcher resolver inline because it needs python; this one does not, and a `python` appearing
# ---- in it later would be an un-resolved launcher rather than a resolved one.
np=$(grep -nE '(^|[^-[:alnum:]])(python3?|py) ' "$SCRIPT" | grep -v '^[0-9]*:#' || true)
n=$((n+1)); [ -z "$np" ] || { echo "FAIL the driver invokes a python launcher without the resolver: $np"; st=1; }

# ============================================================ S1/S2 — the terminal producers
# The two verbs that let a run FINISH. Before them the vocabulary's last two members were
# unreachable, so every completed run stayed non-terminal and the single-live counter grew forever.

# ---- 31: LANDED is reached from LANDING and nowhere else. Preflight leaves the record at RUNNING,
# ---- so this is the ordinary state of a run that never closed. The refusal fires BEFORE the clean
# ---- and anchor checks, so no fixture commit is needed to reach it.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
before=$(sum)
hit "$(run --landed tRun)" "a run reaches LANDED only from LANDING, because LANDING is the record that --close evaluated the Definition-of-Done set and this verb does not evaluate it a second time"
same "the refused --landed wrote nothing" "$(sum)" "$before"
hit "$(run --landed tBare)" "no run-state file, so there is no run to mark landed"

# ---- 32: the OBSERVATION. The fixture's unit branch is one commit AHEAD of the anchor, which is
# ---- exactly the state of a run that has built but not landed — so HEAD is not an ancestor of the
# ---- advertised tip and the claim is refused. This is the branch that makes LANDED an observation
# ---- rather than a phase the run picks.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md
fixture
before=$(sum)
hit "$(run --landed tRun)" "HEAD is not an ancestor of the tip the remote advertises, so the work this run means to mark landed is not on the branch the remote calls its default; land it first, then mark it"
same "the unlanded --landed wrote nothing" "$(sum)" "$before"

# ---- AC18: an unobservable anchor is FATAL here and reports in the OBSERVATION's own words. --close
# ---- suppresses that message and prints only the downstream unmet item, which is the message-channel
# ---- scar this kit already carries; the arm pins that this verb does not repeat it.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md
fixture
git remote set-url origin "$TMP/no-such-origin.git"
hit "$(run --landed tRun)" "the remote did not answer, and the anchor is an observation of it rather than of any local ref"
git remote set-url origin "$ORIGIN"

# ---- AC3 + AC13: the SUCCESS path, standing ON the default branch. That is not incidental — the
# ---- mandated lander refuses to run anywhere but the default branch, so --landed is invoked exactly
# ---- where check_branch would fire, and S3 omits that guard on purpose. A feature-branch fixture
# ---- cannot tell a guard that was omitted from one that was never reached, which is why this arm
# ---- checks the default branch out rather than taking the easier fixture.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md
fixture
git push -q -f origin HEAD:main
git checkout -q -B main HEAD
out=$(run --landed tRun)
hit "$out" "phase LANDED"
same "--landed wrote the terminal phase" "$(sed -n 's/^phase: //p' memory/builds/tRun/RUN.md)" "LANDED"
same "--landed witnessed HEAD" "$(sed -n 's/^witness: //p' memory/builds/tRun/RUN.md)" "$(git rev-parse HEAD)"
n=$((n+1)); git diff --cached --name-only | grep -qF 'memory/builds/tRun/RUN.md' \
  || { echo "FAIL --landed left the terminal record unstaged, so the leg's index-read population cannot see it"; st=1; }
git checkout -q unit; git branch -f main "$BASE"; git push -q -f origin "$BASE":main

# ---- 33/34/35: --abort. It is deliberately NOT symmetric with --landed: an aborted run landed
# ---- nothing, so the four machine items assert obligations it does not have — but it owes BOTH
# ---- agent-attested items, and a first cut of this unit dropped the second.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
before=$(sum)
hit "$(run --abort tRun)" "--abort requires --reason, because an abort with no recorded reason is indistinguishable from a run that simply stopped, and the reason is the only thing the owner gets in place of the turn nobody took"
same "the reasonless --abort wrote nothing" "$(sum)" "$before"
hit "$(run --abort tBare --reason r)" "no run-state file, so there is no run to abort"

reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: LANDED/' memory/builds/tRun/RUN.md
hit "$(run --abort tRun --reason "second thoughts")" "the run is already finished and a finished record is not something to move, re-open or re-pin"

# ...both attestations, one at a time, so the arm distinguishes them. Attesting only the keepalive
# still refuses, which is the half a first cut of this unit let through.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
hit "$(run --abort tRun --reason "no anchor")" "an agent-attested item is unmet and an abort still owes both; the driver can only read back what the agent recorded, so this is an attestation and not a machine verdict. Write the RECORD KEY, which is not always the item name: keepalive-reaped via keepalive-reaped"
printf 'keepalive-reaped: yes\n' >> memory/builds/tRun/RUN.md
hit "$(run --abort tRun --reason "no anchor")" "an agent-attested item is unmet and an abort still owes both; the driver can only read back what the agent recorded, so this is an attestation and not a machine verdict. Write the RECORD KEY, which is not always the item name: parked-decisions-surfaced via parked-surfaced"

# ...and the success path. AC19: the parked entry names itself an ABORT. Routed through the old
# hardcoded `park` it would have read "override · item …", and the build method derives the owner's
# open/parked row from parked entries "plus any recorded DoD override" — so an abort would have
# arrived in the one turn the owner gets wearing the label of an override that never happened.
printf 'parked-surfaced: yes\n' >> memory/builds/tRun/RUN.md
out=$(run --abort tRun --reason "the remote never answered")
hit "$out" "phase ABORTED"
same "--abort wrote the terminal phase" "$(sed -n 's/^phase: //p' memory/builds/tRun/RUN.md)" "ABORTED"
same "--abort witnessed HEAD" "$(sed -n 's/^witness: //p' memory/builds/tRun/RUN.md)" "$(git rev-parse HEAD)"
hit "$(cat memory/builds/tRun/RUN.md)" "abort · item tRun · reason the remote never answered"
miss "$(sed -n '/^## Parked/,$p' memory/builds/tRun/RUN.md)" "override"

# ...and the OTHER caller of the same helper still writes an override entry, or the kind argument
# has simply relabelled every parked line rather than distinguishing two kinds.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
printf 'keepalive-reaped: yes\nparked-surfaced: yes\n' >> memory/builds/tRun/RUN.md
run --close tRun --override records-current --reason "records lag" >/dev/null 2>&1
hit "$(cat memory/builds/tRun/RUN.md)" "override · item records-current · reason records lag"


# ============================================================ the phase-writer population
# THE LEFT-SHIFT for this build's own worst finding. Two verbs wrote a phase with no terminal guard
# because the rule had been spelled at each call site instead of once, and the closing review found
# both: --close re-opened a LANDED record to LANDING printing "close OK", and --landed then re-pointed
# the witness check 15 judges, with the bar green throughout.
#
# So the population is DERIVED from source rather than listed here, and every member is driven against
# a finished record. A sixth phase writer reds this arm until it is added to the drive list, which is
# the property a hand-written list cannot have.
writers=$(grep -c 'set_fact "$rel" phase' "$SCRIPT")
n=$((n+1)); [ "$writers" = 5 ]   || { echo "FAIL the driver has $writers phase writer(s), and this arm drives 5 — add the new verb to the drive list below, or the terminal guard is unproven for it"; st=1; }

reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: LANDED/' memory/builds/tRun/RUN.md
fixture
before=$(sum)
for v in "--phase tRun BUILDING --witness abc" "--close tRun" "--abort tRun --reason r" "--preflight tRun --keepalive-id k2" "--landed tRun"; do
  # shellcheck disable=SC2086
  out=$(run $v)
  hit "$out" "the run is already finished and a finished record is not something to move, re-open or re-pin"
  same "the finished record survived $v" "$(sum)" "$before"
done

# ---- F5: a TRUTHFUL abort reason may not spell the bypass flag, because park() writes it verbatim
# ---- into the file leg check 11 greps WHOLE — so the honest sentence would red the bar permanently,
# ---- on a terminal record no verb can rewrite. The control is that an ordinary reason is accepted.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
printf 'keepalive-reaped: yes
parked-surfaced: yes
' >> memory/builds/tRun/RUN.md
before=$(sum)
hit "$(run --abort tRun --reason "the lander refused and I would not reach for --no-verify")" "the reason spells the declared bypass flag, and the gate greps this file whole for it, so recording this sentence would red the bar on a terminal record nothing can rewrite; say it without the literal flag"
same "the refused abort wrote nothing" "$(sum)" "$before"
out=$(run --abort tRun --reason "the lander refused and I would not bypass it")
hit "$out" "phase ABORTED"
miss "$(cat memory/builds/tRun/RUN.md)" "--no-verify"

# ---- SOURCE-level: no verb may reach the repairing wiring mode, whatever the conf says. The runtime
# ---- arm above covers a project that DECLARES `--fix`; this covers the driver calling it directly.
nf=$(grep -nE 'check-wiring[^"]*--fix' "$SCRIPT" | grep -v '^[0-9]*:#' || true)
n=$((n+1)); [ -z "$nf" ] || { echo "FAIL the driver reaches the repairing wiring mode directly: $nf"; st=1; }

# ---- SOURCE-level: the hot accessors must not fork. `fact` run per
# ---- run-state file per check, and as `sed | head | tr` they cost three processes each — measured
# ---- 1094 sed/head/tr spawns across this suite, 278 after. Process spawn dominates on Windows.
# ---- Comment lines are excluded, or this grep matches the comment that explains the ban — a trap
# ---- this repo has hit twice and recorded.
nf=$(grep -nE 'head -1 \| tr -d' "$HERE/unattended.sh" | grep -v '^[0-9]*: *#' || true)
n=$((n+1)); [ -z "$nf" ] || { echo "FAIL a hot accessor reverted to the fork-per-call idiom: $nf"; st=1; }

[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
