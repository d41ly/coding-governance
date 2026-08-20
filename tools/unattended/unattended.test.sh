#!/usr/bin/env bash
# Fixture self-test for unattended.sh — every refusal branch armed by a POSITIVE assertion naming
# its own failure text (which is what check-arms.py reads), plus the behavioural arms no message
# test can cover: that a refusal writes NOTHING, that the generated region holds NO copy (the unit
# list is derived from the build README), and that --status and --resume agree.
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

cd "$TMP" || exit 2
git init -q -b main . && git config user.email t@t.test && git config user.name t \
  && git config core.autocrlf false

mkconf() { # wiring · gate
  cat > .unattended.conf <<EOF
MEMORY_ROOT=memory
UNITS_REGION_CUTOFF="${3-2026-08-19}"
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

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [ARCH-$1-1 — the unit](spec/one.md) | OPEN | rev-1 | 2026-08-01 |
<!-- /gen:build-units -->
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
mutate memory/builds/tWrongSlug/README.md 's/^slug: tWrongSlug$/slug: someoneElse/'
# A build whose README is on MAIN and which never had a run-state file - S2's subject. Deleting
# tRun's would have worked only by making the tree dirty, which check 2 refuses first, so the arm
# would have tested the dirty-tree refusal while claiming to test creation.
readme tFresh
# TOOL-aPromptedMandate-1 - the authorization MODE fixtures, both on MAIN for tFresh's reason. The
# key is inserted AFTER `slug:` in both, deliberately: the parse this unit replaces printed the slug
# and EXITED on its first match, so a fixture with the key FIRST would pass over the very defect the
# re-shape exists to fix - and the arm would have proved nothing.
readme tModeBad
mutate memory/builds/tModeBad/README.md '/^slug: tModeBad$/a authorized-by: banana'
readme tModeOk
mutate memory/builds/tModeOk/README.md '/^slug: tModeOk$/a authorized-by: prompt'
# review M1's subject: a README whose generated marker pair is UNPAIRED. On MAIN for tFresh's
# reason - authored on the unit branch it never resolves at BASE, so check_authorization refuses
# first and the region validation this arm is about is never reached. Measured.
readme tUnpaired
mutate memory/builds/tUnpaired/README.md 's|^<!-- /gen:build-index -->$||'
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
# An identity on the BARE repo too, because check 30 builds its ahead-commit with `commit-tree`
# INSIDE it. A bare repo inherits nothing from the worktree clone above, so on a machine with no
# global identity that call dies, $ahead comes back empty, and `update-ref` reports ": not a valid
# SHA1" - which reads as a broken kit rather than an unconfigured fixture. MEASURED on node `a`.
git --git-dir="$ORIGIN" config user.email t@t.test
git --git-dir="$ORIGIN" config user.name t
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

# ---- check 4, the SURFACING half. `false` prints nothing, so the arm above passes identically
# ---- whether the driver forwards the declared check's output or discards it with `>/dev/null 2>&1`
# ---- — it cannot tell the two apart. This one declares a check whose failure carries a distinctive
# ---- literal and asserts that literal reaches the operator, which is the whole of what S4 changed.
# ---- The remedy the driver may not spell itself is the one the declared check already prints.
reset_tree
printf '#!/usr/bin/env bash\necho "WIRINGPROBE-the-declared-checks-own-remedy"\nexit 1\n' > probe-wiring.sh
mkconf "bash probe-wiring.sh"
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "the declared wiring check failed, and a dormant hook makes every later green meaningless"
hit "$out" "WIRINGPROBE-the-declared-checks-own-remedy"

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

# TOOL-aBoundedVerdict-11 - the GENERATED pair's fixture writer. The authorization scope moved off the
# authored roster onto this region, so the arms below drive THIS. Appends a second pair when the
# README already has one, which is exactly what the duplicate-pair arms need.
units() { # slug · body
  printf '
%s
%s
%s
' '<!-- gen:build-units -->' "$2" '<!-- /gen:build-units -->' >> "memory/builds/$1/README.md"
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

# ...the run REMOVES a unit from its own scope. TOOL-aBoundedVerdict-11 S6: the comparison is the
# unit-ID SET and BASE must be a SUBSET of HEAD, so a DELETED id is the refusal and an added one is
# admitted. The old arm mutated PROSE inside the roster and asserted a byte difference; under the id
# comparison that prose edit is correctly no longer a scope change, so the arm's SUBJECT moves rather
# than its wording.
rreset
mutate memory/builds/tRun/README.md '/ARCH-tRun-1/d'
hit "$(run --preflight tRun --keepalive-id k1)" "a unit in the scope at the pinned BASE is absent from it now, so this run narrowed or renamed the scope it was authorized for; additions are admitted and removals are not"

# ...and the twin the id comparison exists to ADMIT: a row whose STATUS and REV moved, which is what
# every build does to its own units, and which a byte comparison would have refused. Without this arm
# the subset test is indistinguishable from the byte test it replaced.
rreset
mutate memory/builds/tRun/README.md 's/| OPEN | rev-1 |/| CLOSED | rev-3 |/'
git add -A >/dev/null && git commit -q -m statusmoved --no-verify
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "preflight OK"
miss "$out" "absent from it now"

# ...and an ADDED unit is admitted, which is what makes the promotion disposition legal.
rreset
mutate memory/builds/tRun/README.md 's#^| \[ARCH-tRun-1#| [ARCH-tRun-9 — promoted](spec/nine.md) | OPEN | rev-1 | 2026-08-01 |\n| [ARCH-tRun-1#'
git add -A >/dev/null && git commit -q -m unitadded --no-verify
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "preflight OK"
miss "$out" "absent from it now"

# TOOL-aBoundedVerdict-11 S4 - the WORKING COPY's unit list must be READABLE at preflight, so an agent
# meets the requirement here rather than at --close after a whole run. Two arms, because `region`
# conflates ABSENT with MALFORMED and the refusal has to fire for both.
rreset
sed -i '/gen:build-units/d' memory/builds/tRun/README.md
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "the build README's unit list cannot be read, so every verb keyed on it would run blind"
hit "$out" "the build README carries no single well-formed <!-- gen:build-units --> pair"
miss "$out" "preflight OK"

# ...and the remedy it prints names the SCRIPT and its mode, never a bare launcher: the driver's own
# resolver ban refuses one, and this repo cannot assume a launcher exists on the operator's PATH.
hit "$out" "the --write mode of tools/memory-tree/gen_build_index.py"

# ...a SECOND pair in the working copy. `region` conflates absent with duplicated, so this is the arm
# that proves the presence test is a grep and not that exit status.
rreset
units tRun "| [ARCH-tRun-1 — a second region nobody granted](spec/one.md) | OPEN | rev-1 | 2026-08-01 |"
hit "$(run --preflight tRun --keepalive-id k1)" "the working copy's build README does not carry exactly one well-formed units pair while the pinned BASE does, so the scope this run is executing against cannot be compared"
git checkout -q main; git reset -q --hard "$BASE"; git push -q -f origin main; git checkout -qf unit; reset_tree

# TOOL-aBoundedVerdict-11 S6a - a BASE with NO units pair, dated at or after UNITS_REGION_CUTOFF, is a
# REFUSAL rather than an empty set. A subset test over an empty BASE is vacuously true, which is the
# hole the id comparison exists to close. The fixture's anchor commit is made DURING this run, so its
# date is today and therefore at or after the cutoff: the case the branch is written for.
git checkout -qf main
sed -i '/gen:build-units/d' memory/builds/tRun/README.md
git add -A >/dev/null && git commit -q -m nounitsatbase --no-verify && git push -q -f origin main
git checkout -qf unit && git merge -q --no-edit main >/dev/null 2>&1
# the WORKING COPY gets the pair back: BASE lacks it, HEAD has it. Deleting it from both would make
# S4's readability refusal fire first and mask the branch this arm is about.
readme tRun; git add -A >/dev/null && git commit -q -m unitsathead --no-verify
hit "$(run --preflight tRun --keepalive-id k1)" "the build README at the pinned BASE carries no units marker pair and this BASE is dated at or after UNITS_REGION_CUTOFF, so an empty set would satisfy the subset test vacuously"
git checkout -qf main; git reset -q --hard "$BASE"; git push -q -f origin main; git checkout -qf unit; reset_tree

# ...and the BOOTSTRAP case, which is the whole reason the cutoff exists: a BASE that PREDATES it and
# carries no pair is still authorized. Without this the unit is unlandable by any run, because every
# candidate run's BASE is pinned before the migration render that creates the region.
git checkout -qf main
sed -i '/gen:build-units/d' memory/builds/tRun/README.md
git add -A >/dev/null && git commit -q -m nounitsatbase2 --no-verify && git push -q -f origin main
git checkout -qf unit && git merge -q --no-edit main >/dev/null 2>&1
readme tRun
# The conf is SOURCED by the driver, so the cutoff moves THERE rather than being exported - an
# exported value never reaches a sourced conf, and an arm built that way passes for the wrong reason.
# It is written BEFORE the commit: mkconf dirties the tree, and preflight refuses a dirty tree on
# check_clean before authorization is ever reached, which is what made the first cut of this arm fail
# for a reason that had nothing to do with the cutoff.
mkconf true true 2099-01-01
git add -A >/dev/null && git commit -q -m unitsathead2 --no-verify
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "preflight OK"
miss "$out" "dated at or after UNITS_REGION_CUTOFF"
mkconf
git checkout -qf main; git reset -q --hard "$BASE"; git push -q -f origin main; git checkout -qf unit; reset_tree

# ...and the BASE side MALFORMED: two pairs committed to the anchor. Without this arm the
# grep-for-presence test and the well-formedness check cannot be told apart.
git checkout -qf main; units tRun "| [ARCH-tRun-1 — one](spec/one.md) | OPEN | rev-1 | 2026-08-01 |"
git add -A >/dev/null && git commit -q -m tworegion --no-verify && git push -q -f origin main
git checkout -qf unit && git merge -q --no-edit main >/dev/null 2>&1
hit "$(run --preflight tRun --keepalive-id k1)" "the build README at the pinned BASE carries a units marker but not exactly one well-formed pair, so there is no single scope to compare against"
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
mutate memory/builds/tRun/RUN.md '/^base: /d'
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
out=$(run --close tRun --override closing-review-recorded --reason "fixture build records no review" --override build-complete --reason "fixture build is one OPEN unit with no roster, by construction")
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
hit "$out" "the build README's generated markers are malformed, and the unit list is DERIVED from there, so an unpaired marker is not something to guess around"
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
# The region holds NO COPY. It used to be byte-identical to the README's slice, and that equality
# was unmaintainable in the ordinary case: a spec rev bump moves the build index and preflight — the
# only writer — refuses once a run is live. The unit list is DERIVED at read time instead, so the
# region is empty and there is nothing here to keep fresh.
slice() { awk -v o="$2" -v c="$3" 'index($0,o)==1{i=1;next} index($0,c)==1{i=0;next} i' "$1"; }
same "the generated region holds no copy of the unit list" \
  "$(slice memory/builds/tRun/RUN.md '<!-- run:generated -->' '<!-- /run:generated -->' | tr -d '[:space:]')" ""
# ...and --status DERIVES the unit from the README rather than from the file it just wrote.
hit "$(run --status tRun)" "tRun"
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
out=$(run --close tRun --override build-complete --reason "fixture build is one OPEN unit with no roster, by construction" --override closing-review-recorded --reason "fixture build records no review")
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
out=$(run --close tRun --override closing-review-recorded --reason "fixture build records no review" --override build-complete --reason "fixture build is one OPEN unit with no roster, by construction" --override gates-green --reason "the bar was run by hand at the pinned base")
hit "$out" "close OK"
hit "$(cat memory/builds/tRun/RUN.md)" "the bar was run by hand at the pinned base"
same "the phase advanced to LANDING" \
  "$(sed -n 's/^phase: //p' memory/builds/tRun/RUN.md)" "LANDING"

# ---- TOOL-cBriefedPilot-1: the override REPEATS. The scalar form overwrote the first pair, so
# ---- verb_close blocked on the second unmet item forever with nobody to read the block.
reset_tree; run --preflight tRun --keepalive-id KA-1234 >/dev/null
printf 'keepalive-reaped: yes\nparked-surfaced: yes\n' >> memory/builds/tRun/RUN.md
mkconf "false" "false"
out=$(run --close tRun --override closing-review-recorded --reason "fixture build records no review" --override build-complete --reason "fixture build is one OPEN unit with no roster, by construction" --override gates-green --reason "bar run by hand" --override records-current --reason "index re-rendered by hand")
hit "$out" "close OK"
hit "$out" "override recorded for 'gates-green'"
hit "$out" "override recorded for 'records-current'"
hit "$(cat memory/builds/tRun/RUN.md)" "bar run by hand"
hit "$(cat memory/builds/tRun/RUN.md)" "index re-rendered by hand"
same "four overrides parked, one per pair — the scalar form kept only the last" "$(grep -c 'override · item ' memory/builds/tRun/RUN.md)" "4"

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

# ---- TOOL-cBriefedPilot-7: `build-complete` — the owner's "merge and push only when the entire
# ---- build is fully done", given a checker. FIVE terms, and the GREEN CONTROL comes FIRST: without
# ---- a tree where the item is genuinely MET, every arm below would pass by finding nothing, which
# ---- is the exact class this build kept meeting. Each arm then breaks exactly ONE term off it.
# ---- Terms 4 and 5 are broken in BOTH the README and the run-state copy, so `records-current` stays
# ---- met and the refusal is attributable to this item alone rather than to two at once.
git checkout -qf main
sed -i 's/| OPEN | rev-1 |/| CLOSED | rev-1 |/' memory/builds/tRun/README.md
roster tRun "1. ARCH-tRun-1 — the unit"
mkdir -p memory/builds/tRun/spec
printf '# ARCH-tRun-1 the unit\n\n**Status:** CLOSED · rev-1 · 2026-08-01 · node a · Tier-1 · base 00000000 · streams architecture\n' > memory/builds/tRun/spec/one.md
git add -A >/dev/null && git commit -q -m bc-fixture --no-verify && git push -q -f origin main
git checkout -qf unit && git merge -q --no-edit main >/dev/null 2>&1
BCP=$(git rev-parse HEAD)
bcreset() { git reset -q --hard "$BCP"; git clean -qfd; mkconf; }
bcopen() { bcreset; run --preflight tRun --keepalive-id KA-1234 >/dev/null
           printf 'keepalive-reaped: yes\nparked-surfaced: yes\n' >> memory/builds/tRun/RUN.md; }

# GREEN CONTROL: a complete build closes with NO override at all. If this ever needs one, the item
# has stopped being satisfiable and every arm below is measuring the wrong thing.
bcopen
out=$(run --close tRun --override closing-review-recorded --reason "fixture build records no review")
hit "$out" "close OK"
miss "$out" "build-complete"

# ---- TOOL-aBoundedVerdict-11 S7: BOTH items MET, with NO --override at all. This is the control the
# ---- close-path audit found DISARMED: `build-complete`'s green control above overrides
# ---- `closing-review-recorded`, and every `closing-review-recorded` arm overrides `build-complete`,
# ---- so nothing in this suite ever had both satisfied at once. That is how `build-complete` becoming
# ---- unsatisfiable on 49 of 49 corpus builds rode the merge bar green: the arm written to catch
# ---- exactly that was cleared by the override of the item it was measuring.
bcopen
mkdir -p memory/builds/tRun/reviews
printf '**Serves:** diff-review ARCH-tRun-1

# closing review

range %s...HEAD
' "$(git rev-parse --short "$(sed -n 's/^base: //p' memory/builds/tRun/RUN.md)")" > memory/builds/tRun/reviews/r1.md
git add -A >/dev/null
out=$(run --close tRun)
hit "$out" "close OK"
miss "$out" "build-complete"
miss "$out" "closing-review-recorded"

# ---- ...and the REGRESSION arm for the defect itself: a records-shaped row inside `gen:build-index`
# ---- but OUTSIDE `gen:build-units`. That is exactly what `gen_build_index.py` renders for any build
# ---- holding a tracked record, and by row SHAPE it counted as an unfinished unit - which is what made
# ---- the two items mutually unsatisfiable. The driver must not see it.
bcopen
mkdir -p memory/builds/tRun/reviews
printf '**Serves:** diff-review ARCH-tRun-1

# closing review

range %s...HEAD
' "$(git rev-parse --short "$(sed -n 's/^base: //p' memory/builds/tRun/RUN.md)")" > memory/builds/tRun/reviews/r1.md
# `%` as the delimiter: the replacement is a markdown TABLE, so every `|` in it would have closed a
# `|`-delimited sed expression early and produced a plausible-looking wrong file.
# THROUGH `mutate`, and that is the point of this fix. The first cut of this line carried RAW
# newlines in the replacement: GNU sed answers `unterminated 's' command`, exits 1, and edits
# NOTHING - so the one negative control for the record-row defect BOTH nodes fixed passed while
# testing zero bytes. `mutate` hashes before and after and reds on a no-op; the helper existed,
# its own comment names this exact shape, and this call site did not use it.
mutate memory/builds/tRun/README.md 's%^<!-- /gen:build-units -->%<!-- /gen:build-units -->\n\n| Record | Kind | Serves |\n|---|---|---|\n| [r1.md](reviews/r1.md) | diff-review | ARCH-tRun-1 |%'
git add -A >/dev/null
out=$(run --close tRun)
hit "$out" "close OK"
miss "$out" "build-complete"

# term 1 — no well-formed roster pair. A COMPLETENESS check cannot borrow check_authorization's
# opt-in-by-presence disposition: on this tree 1 of 35 build READMEs carries the pair, so an opt-in
# build-complete would be vacuously true for 34 of them and blind in the case it exists for.
bcopen; sed -i "/gen:build-units/d" memory/builds/tRun/README.md
out=$(run --close tRun)
hit "$out" "a machine-checked DoD item is unmet, so --close blocks"
hit "$out" "build-complete"
# TOOL-aBranchedMandate-13: and it says WHICH region. The five terms were ANDed into one verdict,
# so this case reported a bare "unmet" -- the state of every build README older than the item.
hit "$out" "the build README carries no well-formed units marker pair"

# term 2 — the pair is well-formed and names no id at all. TOOL-aBoundedVerdict-11 S8: this term now
# reads the GENERATED region's ids (`unit_ids_of`) rather than the authored plan, so the id has to be
# taken out of the rendered unit ROW. The authored plan keeps its own term, which is term 3.
bcopen; sed -i 's#^| \[ARCH-tRun-1 — the unit#| [a rendered row carrying no id#' memory/builds/tRun/README.md
out=$(run --close tRun)
hit "$out" "build-complete"
# TOOL-aBoundedVerdict-12 S3 - and it says WHICH term. The four surviving terms were ANDed into one
# verdict, so all four printed the same sentence and an operator could not tell a missing spec from an
# unfinished unit; `--override build-complete` was the natural next move for a reader with no cause.
hit "$out" "the build's generated units region names no unit id, so there is no roster to judge completeness against"

# term 3 — the roster names a unit nobody specced. This is the ONLY term that can see it: the
# generated region is rendered from the specs that EXIST, so terms 4 and 5 are blind to a planned
# unit with no spec file.
bcopen; sed -i 's/^1\. ARCH-tRun-1 — the unit$/1. ARCH-tRun-1 — the unit\n2. ARCH-tRun-9 — never specced/' memory/builds/tRun/README.md
out=$(run --close tRun)
hit "$out" "build-complete"
hit "$out" "the authored plan names a unit that no tracked spec carries, so the build is incomplete by its own roster"

# term 4 — the generated region is spliced EMPTY. Term 5 is vacuously true over an empty selection,
# so without this term a run-state file carrying no unit rows would satisfy "none is non-terminal"
# by having none. Emptied in both files, so records-current stays met.
bcopen
sed -i '/^| \[ARCH-tRun-1/d' memory/builds/tRun/RUN.md
sed -i '/^| \[ARCH-tRun-1/d' memory/builds/tRun/README.md
out=$(run --close tRun)
hit "$out" "build-complete"
miss "$out" "records-current"
# rows deleted means ids are gone too, and the driver tests ROWS FIRST precisely so this message is
# the one that fires. Asserting the ids sentence here instead would have been asserting the mask.
hit "$out" "the generated units region carries no unit ROWS"

# term 5 — one unit row is non-terminal. The case the owner actually asked for.
bcopen
sed -i 's/| CLOSED | rev-1 |/| OPEN | rev-1 |/' memory/builds/tRun/RUN.md
sed -i 's/| CLOSED | rev-1 |/| OPEN | rev-1 |/' memory/builds/tRun/README.md
out=$(run --close tRun)
hit "$out" "build-complete"
miss "$out" "records-current"
hit "$out" "a unit of this build is not terminal, so the build is not done"
# ...and it NAMES the offending row rather than only counting it, so the operator does not re-derive
# which unit is unfinished from a file the refusal already read.
hit "$out" "ARCH-tRun-1"

# ---- TOOL-aPromptedMandate-12: the selector reads the UNITS table, not the whole region. The
# ---- generated region renders TWO tables and the old `^| [` took both, so every review record M4
# ---- mandates and the closing review M8 mandates counted as a non-terminal unit - the item was
# ---- unsatisfiable for any build that followed the method. Measured on builds that had already
# ---- LANDED: aBranchedMandate 13 rows against 6 units, aStandingWrit 3 against 1.
# ----
# ---- These run on the build-complete fixture, whose unit is CLOSED and whose roster pair exists.
# ---- Written against `reset_tree` instead, both positive arms failed on the fixture's own OPEN
# ---- unit and term 1's missing roster - measuring the fixture rather than the subject.
bcopen
# INSIDE the region, not appended. `>>` puts the row past `<!-- /gen:build-index -->`, where
# `region()` never sees it - so these arms restated the green control and passed identically against
# the PRE-FIX selector. The shipped fix had no regression gate, which is the class this same
# changeset adds a gotcha sub-shape for. Caught by the second closing review, not by me.
sed -i '/<!-- gen:build-index -->/a | [2026-08-01-review-ARCH-tRun-1-x.md](reviews/2026-08-01-review-ARCH-tRun-1-x.md) | spec-audit | ARCH-tRun-1 |' memory/builds/tRun/README.md
sed -i '/<!-- gen:build-index -->/a | [2026-08-01-review-ARCH-tRun-1-x.md](reviews/2026-08-01-review-ARCH-tRun-1-x.md) | spec-audit | ARCH-tRun-1 |' memory/builds/tRun/RUN.md
out=$(run --close tRun --override closing-review-recorded --reason "fixture build records no review")
hit  "$out" "close OK"
miss "$out" "build-complete"

# ...and the SECOND reader agrees. `verb_status` open-coded the same pipeline and never called the
# helper, so narrowing one left --close and --status disagreeing about one region. Before this,
# --status on a landed build offered a `build/` record filename as the next unit.
out=$(run --status tRun)
miss "$out" "2026-08-01-review-ARCH-tRun-1-x.md"
hit  "$out" "(no non-terminal unit)"

# ---- a unit title containing `]` is STILL selected. `[^]]*` stops at the first one, and a dropped
# ---- unit row is a false GREEN: nonterminal_units cannot see it, so build-complete passes over an
# ---- unfinished unit. The spec audit caught this before the code was written.
bcopen
sed -i 's/ARCH-tRun-1 — the unit\]/ARCH-tRun-1 — the [bracketed] unit]/' memory/builds/tRun/README.md
sed -i 's/ARCH-tRun-1 — the unit\]/ARCH-tRun-1 — the [bracketed] unit]/' memory/builds/tRun/RUN.md
out=$(run --close tRun --override closing-review-recorded --reason "fixture build records no review")
hit  "$out" "close OK"
miss "$out" "build-complete"

# the OVERRIDE path: the item blocks, and the owner's named reason unblocks it and is readable
# afterwards. A blocking gate whose override nobody can read is not a gate.
out=$(run --close tRun --override closing-review-recorded --reason "fixture build records no review" --override build-complete --reason "shipping 1 of 2 units deliberately")
hit "$out" "close OK"
hit "$(cat memory/builds/tRun/RUN.md)" "shipping 1 of 2 units deliberately"

# ---- TOOL-aBoundedVerdict-12 S7: a line BEFORE the network round-trip. A close that is about to
# ---- spend one has printed something, so "hung" and "working" are distinguishable from outside.
# ---- Unconditional rather than tty-gated, because a progress line an unattended run cannot observe
# ---- is not a progress line - and this arm reads stdout, which is the only thing a run has.
bcopen
hit "$(run --close tRun)" "observing the anchor, then evaluating the Definition of Done"

# ---- S5: the agent-item refusal names the RECORD KEY, which is not the item name.
# ---- `parked-decisions-surfaced` is read from a line spelled `parked-surfaced:`, so an operator
# ---- obeying the old refusal wrote a key nothing reads and re-ran forever.
bcreset; run --preflight tRun --keepalive-id KA-1234 >/dev/null
printf 'keepalive-reaped: yes
' >> memory/builds/tRun/RUN.md
out=$(run --close tRun)
hit "$out" "an agent-attested DoD item is unmet"
hit "$out" "write the RECORD KEY, which is not always the item name: parked-surfaced: yes"

# ---- S4: closing-review-recorded distinguishes its failure modes. The UNTRACKED case is the
# ---- likeliest and was unguessable: the join reads --cached, so a record on disk and never staged
# ---- is invisible here and reads exactly like having written no review at all.


# restore main to the shared BASE so the later arms see the tree they were written against.
git checkout -q main; git reset -q --hard "$BASE"; git push -q -f origin main; git checkout -qf unit; reset_tree

# ---- TOOL-cBriefedPilot-8: `closing-review-recorded` — a tracked review record under this build
# ---- names the base the run pinned once. GREEN CONTROL first for the same reason as unit 7: every
# ---- arm below asserts the item is UNMET, and without a tree where it is genuinely MET they would
# ---- all pass against an item that can never be satisfied.
# NOTE: expanded UNQUOTED on purpose, so it must word-split into exactly four arguments. A
# reason with spaces does not survive that: quotes inside a variable are literal characters,
# not shell quoting, and the tail becomes stray argv the driver rejects.
crbc='--override build-complete --reason fixture-build-is-one-open-unit'
cropen() { reset_tree; run --preflight tRun --keepalive-id KA-1234 >/dev/null
           printf 'keepalive-reaped: yes\nparked-surfaced: yes\n' >> memory/builds/tRun/RUN.md
           mkdir -p memory/builds/tRun/reviews; }
crbase() { sed -n 's/^base: //p' memory/builds/tRun/RUN.md; }

# GREEN CONTROL: a TRACKED record naming the pinned base, abbreviated to eight, satisfies the item.
cropen; rb=$(crbase)
printf '**Serves:** diff-review ARCH-tRun-1

# closing review\n\nrange %s...HEAD\n' "$(git rev-parse --short "$rb")" > memory/builds/tRun/reviews/r1.md
git add -A >/dev/null
out=$(run --close tRun $crbc)
hit "$out" "close OK"
miss "$out" "closing-review-recorded"

# ---- TOOL-aBoundedVerdict-16 S1: a SPEC-AUDIT quoting the pinned base does NOT satisfy an item named
# ---- for a closing review. Measured before the change: two of the four runs that matched did so on a
# ---- spec-audit record, so the item was kind-blind and said so nowhere.
cropen; rb=$(crbase)
git rm -q --cached --ignore-unmatch memory/builds/tRun/reviews/*.md >/dev/null 2>&1 || true
rm -f memory/builds/tRun/reviews/*.md
printf '**Serves:** spec-audit ARCH-tRun-1

# a design review

range %s...HEAD
' "$rb" > memory/builds/tRun/reviews/audit.md
git add -A >/dev/null
out=$(run --close tRun $crbc)
hit "$out" "none is a diff-review naming a commit in BASE..HEAD"
miss "$out" "close OK"

# ---- S2: a diff-review naming a sha strictly INSIDE the range is accepted -- the fold-scoped case,
# ---- which the old pinned-base test rejected outright, and which -14 now makes the honest one.
cropen; rb=$(crbase)
git rm -q --cached --ignore-unmatch memory/builds/tRun/reviews/*.md >/dev/null 2>&1 || true
rm -f memory/builds/tRun/reviews/*.md
mid=$(git rev-parse HEAD)
printf '**Serves:** diff-review ARCH-tRun-1

# closing review

range %s...HEAD
' "$mid" > memory/builds/tRun/reviews/fold.md
git add -A >/dev/null
out=$(run --close tRun $crbc)
miss "$out" "closing-review-recorded"

# ---- S3: a sha that is NOT an ancestor of HEAD is refused even though the STRING is present. A
# ---- substring test cannot express range membership and would accept a sha off any branch.
cropen; rb=$(crbase)
git rm -q --cached --ignore-unmatch memory/builds/tRun/reviews/*.md >/dev/null 2>&1 || true
rm -f memory/builds/tRun/reviews/*.md
printf '**Serves:** diff-review ARCH-tRun-1

# closing review

range deadbeefdeadbeefdeadbeefdeadbeefdeadbeef...HEAD
' > memory/builds/tRun/reviews/off.md
git add -A >/dev/null
out=$(run --close tRun $crbc)
hit "$out" "closing-review-recorded"
miss "$out" "close OK"

# SELF-SUFFICIENT, not inherited: earlier arms in this section COMMIT review records, so `cropen`'s
# reset leaves tracked ones behind and the item is simply MET - printing nothing and proving nothing.
# Untrack whatever is there before claiming the tree has no tracked review.
cropen; rb=$(crbase)
git rm -q --cached --ignore-unmatch memory/builds/tRun/reviews/*.md >/dev/null 2>&1 || true
printf '**Serves:** diff-review ARCH-tRun-1

# closing review

range %s...HEAD
' "$(git rev-parse --short "$rb")" > memory/builds/tRun/reviews/r1.md
out=$(run --close tRun $crbc)
hit "$out" "a review record exists on disk but is NOT TRACKED"
hit "$out" "stage it with git add"

# ...and with NO review record at all, a DIFFERENT sentence - the two cases must not read alike, which
# is the whole point: the untracked case was previously indistinguishable from having written none.
cropen
git rm -q --cached --ignore-unmatch memory/builds/tRun/reviews/*.md >/dev/null 2>&1 || true
rm -f memory/builds/tRun/reviews/*.md
out=$(run --close tRun $crbc)
hit "$out" "no review record exists under this build at all"

# ...and a record spelling the base at EXACTLY SEVEN, the shortest abbreviation git produces here.
# The join shipped at eight and matched none of this corpus's seven-char records, so the item could
# only ever be cleared by an override the run wrote for itself. Pinned by name, not by whatever
# `git rev-parse --short` returns on the machine running this suite.
cropen; rb=$(crbase)
printf '**Serves:** diff-review ARCH-tRun-1

# closing review

range %s...HEAD
' "${rb:0:7}" > memory/builds/tRun/reviews/r1.md
git add -A >/dev/null
out=$(run --close tRun $crbc)
hit "$out" "close OK"
miss "$out" "closing-review-recorded"

# arm 1 — the build records no review at all. The empty directory is the ordinary case at the start
# of a run, and it must block rather than pass by selecting over nothing.
cropen
out=$(run --close tRun $crbc)
hit "$out" "a machine-checked DoD item is unmet, so --close blocks"
hit "$out" "closing-review-recorded"

# arm 2 — the record exists in the WORKING TREE and is not tracked. `--cached` reads the index, so
# this is excluded by construction rather than by a filter; without --cached it would pass.
cropen; rb=$(crbase)
printf '**Serves:** diff-review ARCH-tRun-1

# closing review\n\nrange %s...HEAD\n' "$(git rev-parse --short "$rb")" > memory/builds/tRun/reviews/r1.md
hit "$(run --close tRun $crbc)" "closing-review-recorded"

# arm 3 — a tracked record that names a DIFFERENT sha. The record exists and the join still refuses,
# which is the difference between "a review was written" and "the review covers what shipped".
cropen
printf '**Serves:** diff-review ARCH-tRun-1

# closing review\n\nrange deadbee1...HEAD\n' > memory/builds/tRun/reviews/r1.md
git add -A >/dev/null
hit "$(run --close tRun $crbc)" "closing-review-recorded"

# arm 4 — THE LENGTH GUARD, and the reason it is not defensive decoration. The record here is a
# perfectly good tracked review; only the recorded base is gone. `grep -F ""` matches every line of
# every file, so without the >=8 test this arm would SELECT that record and the item would pass by
# finding anything — the same degeneration an empty base once caused in check_authorization.
cropen; rb=$(crbase)
printf '**Serves:** diff-review ARCH-tRun-1

# closing review\n\nrange %s...HEAD\n' "$(git rev-parse --short "$rb")" > memory/builds/tRun/reviews/r1.md
git add -A >/dev/null
sed -i '/^base: /d' memory/builds/tRun/RUN.md
hit "$(run --close tRun $crbc)" "closing-review-recorded"

# arm 5 — a base TRUNCATED below eight characters is refused for the same reason, and separately,
# because "absent" and "too short to be a needle" reach the guard by different routes.
cropen; rb=$(crbase)
printf '**Serves:** diff-review ARCH-tRun-1

# closing review\n\nrange %s...HEAD\n' "$(git rev-parse --short "$rb")" > memory/builds/tRun/reviews/r1.md
git add -A >/dev/null
sed -i 's/^base: .*/base: abc/' memory/builds/tRun/RUN.md
hit "$(run --close tRun $crbc)" "closing-review-recorded"
reset_tree

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

# ---- The BASE is pinned ONCE (unit deliberately unnamed — non-terminal spec, and the drift signal
# ---- for those cited by product source is at its pin). Re-preflight is the verb a run is TOLD to
# ---- re-run after a compaction, and it used to re-pin against a merge-base that had moved - which
# ---- the mandated lander makes happen on most runs, because it reconciles origin before the gate.
reset_tree
run --preflight tRun --keepalive-id k1 >/dev/null
base1=$(sed -n "s/^base: //p" memory/builds/tRun/RUN.md)
same "the first preflight wrote a base" "$([ -n "$base1" ] && echo yes || echo no)" "yes"
asha1=$(sed -n "s/^anchor-sha: //p" memory/builds/tRun/RUN.md)
# advance the anchor and reconcile it, which is exactly what the lander does before the gate
git -C "$ORIGIN" --work-tree=. --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main 2>/dev/null || true
git checkout -q main && echo advance >> advance.txt && git add -A && git commit -q -m advance --no-verify
git push -q "$ORIGIN" main 2>/dev/null || true
git checkout -q unit && git merge -q --no-edit main >/dev/null 2>&1 || true
git fetch -q "$ORIGIN" 2>/dev/null || true
# ...and again by REMOTE NAME. Fetching by PATH updates no `refs/remotes/origin/*`, so the anchor
# this fixture spends four lines advancing never actually moved, and both pinned-once arms below
# were comparing a value against itself. The freeze arm's control is what exposed it.
git fetch -q origin 2>/dev/null || true
out=$(run --preflight tRun --keepalive-id k1)
base2=$(sed -n "s/^base: //p" memory/builds/tRun/RUN.md)
same "the base did not move on the second preflight" "$base2" "$base1"
# TOOL-cBriefedPilot-5, the fork the owner resolved: the anchor TRIPLE freezes with the base.
# Protocol section 2 describes all four as observed at pin time so an outside party can re-derive
# the pin; a triple that keeps moving dates a different moment from the value it is evidence for.
# The CONTROL first — without it this arm passes whenever the anchor happens not to have moved, and
# the whole point of the fixture above is that it did.
asha2=$(sed -n "s/^anchor-sha: //p" memory/builds/tRun/RUN.md)
now=$(git rev-parse refs/remotes/origin/main)
same "the anchor really did move, so the freeze has something to resist"   "$([ "$now" != "$asha1" ] && echo moved || echo stayed)" "moved"
same "the anchor sha did not move on the second preflight" "$asha2" "$asha1"
hit "$out" "base $base1"

# ---- TOOL-cBriefedPilot-2: the directive registry. AC1 is exercised by every arm in this file -
# ---- mkconf does NOT emit DIRECTIVES_EXTRA, so a driver that read it without a default would have
# ---- aborted under set -u on the first invocation. Asserted explicitly anyway, because a property
# ---- that holds by accident of another fixture is one nobody notices losing.
reset_tree
out=$(run --status tRun)
miss "$out" "unbound variable"
hit "$out" "phase "

# ---- THIRTEEN pairs, read from the driver's OWN constant line — the same line the gate leg's
# ---- core_of() parses, so a count here and a count there cannot disagree. It was eleven until
# ---- TOOL-aPromptedMandate-4 added the two prompt-scoped handles.
dirline=$(grep '^DIRECTIVES_CORE=' "$SCRIPT")
ndir=$(printf '%s\n' "$dirline" | grep -o ':M[0-9][0-9]*' | wc -l | tr -d ' ')
same "the registry declares thirteen handles" "$ndir" "13"

# ---- every handle POINTS at a build-method section and none of them restates one. The pointer is
# ---- the whole design: a gloss grown into a condition would be the M1 defect this build exists to
# ---- avoid, and a shape check is the cheapest thing that notices it happening.
# ----
# ---- The grammar admits an OPTIONAL third field since TOOL-aPromptedMandate-4, over the closed set
# ---- `all|prompt` and nothing wider - a free-text third field would be exactly the gloss this arm
# ---- exists to refuse, one colon further along.
nbad=$(printf '%s\n' "$dirline" | sed -e 's/^DIRECTIVES_CORE="//' -e 's/"$//' | tr ' ' '\n' \
       | grep -v '^$' | grep -cvE '^[a-z][a-z-]*:M[0-9]+(:(all|prompt))?$' || true)
same "every registry entry is handle:M-section with at most a closed scope" "$nbad" "0"

# ---- ...and the scope vocabulary is CLOSED at the source, so a typo cannot invent a third value
# ---- that the arm above would then bless as legal grammar.
nscope=$(printf '%s\n' "$dirline" | grep -o ':M[0-9][0-9]*:[a-z]*' | sed 's/.*://' | sort -u | grep -cvE '^(all|prompt)$' || true)
same "no registry entry declares a scope outside all/prompt" "$nscope" "0"

# ---- S5, the resume pointer. Armed because S2 taught this unit what an unarmed scope item costs:
# ---- it can silently not ship while the suite stays green.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
same "resume names the directive table" "$(run --resume tRun | grep -c 'the directives and their waivers')" "1"

# ---- S2, the ACCESSOR exists and composes core plus extra. This arm is here because its absence
# ---- was invisible: the accessor edit silently no-opped, the suite stayed green at 192, and the
# ---- source-level arm below could not see it either — it checks that a key is DEFAULTED, not that
# ---- anything READS it. A scope item with no arm is a scope item that can quietly not ship.
same "directives() is defined" "$(grep -c '^directives()' "$SCRIPT")" "1"
same "directives() composes core and extra" \
  "$(grep '^directives()' "$SCRIPT" | grep -c 'DIRECTIVES_CORE.*DIRECTIVES_EXTRA')" "1"

# ---- S6, the SOURCE-level arm: every conf key the DRIVER reads is defaulted in its own init block.
# ---- The population is the KIT'S SHIPPED EXAMPLE, not the fixture's conf. The first cut read
# ---- `.unattended.conf`, which under `mkconf` omits the very key the arm was written for, so it was
# ---- VACUOUS — observed by stripping DIRECTIVES_EXTRA from the init line and watching the suite
# ---- stay green. The example is the kit's own declaration of the surface a project fills in, it is
# ---- tracked, and no fixture can narrow it.
example="$HERE/.unattended.conf.example"

# ---- TOOL-aPromptedMandate-2, S5: the example's FLOORS, joined to the driver's own set sizes.
# ---- The example shipped CORE_FLOOR="10:6" against an EIGHT-member DOD_CORE, and stayed wrong for
# ---- its whole life because the only arm that read this file iterates key NAMES and never a value.
# ---- The header tells an adopter to MEASURE rather than copy; nothing made that self-enforcing, so
# ---- a project copying the example inherited a floor too slack to detect the deletion it exists to
# ---- detect. `wc -w` is normalised because it pads on this platform and the comparison is textual.
wcw() { grep -m1 "^$1=" "$SCRIPT" | cut -d\" -f2 | wc -w | tr -d " \t"; }
same "the example CORE_FLOOR equals the driver phase and DoD set sizes" \
  "$(sed -n 's/^CORE_FLOOR="\(.*\)"/\1/p' "$example" | head -1)" "$(wcw PHASES_CORE):$(wcw DOD_CORE)"
same "the example DIRECTIVES_FLOOR equals the driver directive count" \
  "$(sed -n 's/^DIRECTIVES_FLOOR="\(.*\)"/\1/p' "$example" | head -1)" "$(wcw DIRECTIVES_CORE)"
initblock=$(grep -A1 '^MEMORY_ROOT=memory; ' "$SCRIPT")
undefaulted=""
checked=0
for k in $(sed -n 's/^\([A-Z_][A-Z_]*\)=.*/\1/p' "$example"); do
  grep -q "[^A-Z_]$k" "$SCRIPT" || continue
  checked=$((checked + 1))
  case "$initblock" in *"$k="*) ;; *) undefaulted="$undefaulted $k" ;; esac
done
same "every conf key the driver reads is defaulted in its init block" "$undefaulted" ""

# ---- and the population is NON-EMPTY and plausible. Without this the arm above passes when the
# ---- example cannot be read, when the reference test matches nothing, or when a path resolves
# ---- differently for two tools — all three of which happened while this arm was being written.
same "the arm actually checked a plausible number of keys" \
  "$([ "$checked" -ge 8 ] && echo yes || echo no)" "yes"

# ---- TOOL-cBriefedPilot-3: --waive. Five refusals, and the first is a DISPATCH guard rather than a
# ---- precondition: verb_preflight never runs for another verb, so a guard there could never fire.
# ---- The M4 audit found that; the spec had put it in the wrong place.
reset_tree
hit "$(run --status tRun --waive minimal-prose --reason x)" \
  "--waive is accepted by --preflight alone; the owner turn that grants a waiver is the last one there is, and a verb reachable mid-run is a place the run could answer its own question:"
# --plan and --phase EXIT INSIDE the parse loop, so a post-loop guard alone never sees them. Both
# arms are here because that is exactly the miss the guard is shaped to avoid.
hit "$(run --plan tRun --waive minimal-prose --reason x)" \
  "--waive is accepted by --preflight alone; the owner turn that grants a waiver is the last one there is, and a verb reachable mid-run is a place the run could answer its own question:"
hit "$(run --phase tRun BUILDING --witness deadbeef --waive minimal-prose --reason x)" \
  "--waive is accepted by --preflight alone; the owner turn that grants a waiver is the last one there is, and a verb reachable mid-run is a place the run could answer its own question:"

# ---- an undeclared handle waives nothing.
reset_tree; before_waive=$(sum)
hit "$(run --preflight tRun --keepalive-id k1 --waive no-such-directive --reason because)" \
  "--waive names a handle that is not in the effective directive set, and a waiver on a directive nobody declared relaxes nothing:"

# ---- a waiver with no reason is indistinguishable from one nobody meant.
reset_tree
hit "$(run --preflight tRun --keepalive-id k1 --waive minimal-prose)" \
  "--waive requires --reason, because a waiver with no recorded reason is indistinguishable from one nobody meant and the wrap-up has nothing to surface"

# ---- the reason may not spell the declared bypass flag: park writes it verbatim and the leg greps
# ---- this file whole, so a truthful reason would red the bar forever on a record no verb rewrites.
reset_tree
hit "$(run --preflight tRun --keepalive-id k1 --waive minimal-prose --reason 'ran with --no-verify')" \
  "a waiver reason may not spell the declared bypass flag or contain a newline; park writes it verbatim into a line-oriented region that the leg greps whole, so either one corrupts a record no verb rewrites"

# ---- nor a newline: park's grammar is one line per entry, so a reason carrying one forges a second
# ---- well-formed entry the owner never granted.
reset_tree
hit "$(run --preflight tRun --keepalive-id k1 --waive minimal-prose --reason "$(printf 'first\nsecond')")" \
  "a waiver reason may not spell the declared bypass flag or contain a newline; park writes it verbatim into a line-oriented region that the leg greps whole, so either one corrupts a record no verb rewrites"

# ---- every refusal above leaves the run-state file ABSENT, not merely prints. A refused preflight
# ---- that had already written would have changed the state its refusal is about.
# tRun SHIPS a run-state file, so `absent` was never the right claim - the property is that a
# refused preflight changed NOTHING. `sum` is the idiom every other no-write arm here uses.
same "a refused --waive preflight left the run-state file byte-identical" "$(sum)" "$before_waive"

# ---- the happy path: two pairs, both parked with their reasons, in the STAGED blob.
reset_tree
# PREFLIGHT CREATES the record — protocol section 2 — so a first waiver arrives on a build
# that has none. The fixture pre-makes tRun's, which let the old permissive guard accept a
# SECOND owner turn: a waiver added to an existing waiver-free record. Unit 13's
# cross-component arm found that, the guard was narrowed, and this arm now exercises the
# flow a real run takes.
rm -f memory/builds/tRun/RUN.md; git add -A >/dev/null; git commit -q -m 'no record yet' --no-verify
out=$(run --preflight tRun --keepalive-id k1 --waive minimal-prose --reason "nobody reads it" --waive parallel-when-disjoint --reason "sequenced by hand")
hit "$out" "preflight OK"
hit "$out" "directive waived — minimal-prose"
hit "$out" "directive waived — parallel-when-disjoint"
same "two waivers parked, one per pair" \
  "$(grep -c 'waiver · item ' memory/builds/tRun/RUN.md)" "2"
hit "$(cat memory/builds/tRun/RUN.md)" "nobody reads it"
hit "$(cat memory/builds/tRun/RUN.md)" "sequenced by hand"
same "the waivers are in the STAGED blob, which is the leg's whole population" \
  "$(git show :memory/builds/tRun/RUN.md | grep -c 'waiver · item ')" "2"

# ---- a re-preflight naming the SAME set is idempotent: it is a resume, not a second owner turn.
before=$(grep -c 'waiver · item ' memory/builds/tRun/RUN.md)
run --preflight tRun --keepalive-id k1 --waive minimal-prose --reason "nobody reads it" --waive parallel-when-disjoint --reason "sequenced by hand" >/dev/null
same "a re-preflight with the same set duplicates nothing" \
  "$(grep -c 'waiver · item ' memory/builds/tRun/RUN.md)" "$before"

# ---- and one naming a DIFFERENT set refuses, rather than silently re-writing what the owner granted.
hit "$(run --preflight tRun --keepalive-id k1 --waive diff-reviewed --reason "changed my mind")" \
  "the requested waiver set differs from the one already recorded, and a re-preflight is a RESUME rather than a second owner turn; re-issue the recorded set or none at all"

# The happy path STAGED the run-state file, so the tree is dirty and check_clean refuses for a
# reason that has nothing to do with waivers. Commit it, as every arm reaching the write phase does.
fixture
# ---- an invocation naming NO handle is not a refusal. Unit 5's design requires a --preflight before
# ---- every --close, and over a waived run that invocation carries no pairs.
hit "$(run --preflight tRun --keepalive-id k1)" "preflight OK"
same "a no-handle re-preflight left the recorded set intact" \
  "$(grep -c 'waiver · item ' memory/builds/tRun/RUN.md)" "2"

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

# ---- TOOL-cBriefedPilot-6: --plan sees the planned unit that has no spec. M2 makes the README's
# ---- authored Units table the roster; this verb did not parse it, so it enumerated the half of the
# ---- roster that already had specs and said so in its own closing line.
reset_tree; readme tPlan
mkspec tPlan ARCH-tPlan-1 SPECCED "S1 a thing" "AC1 it works" "the bar" "none"
roster tPlan "1. ARCH-tPlan-1 the specced one
2. ARCH-tPlan-7 the one nobody has specced"
fixture
out=$(run --plan tPlan)
hit "$out" "ARCH-tPlan-7"
hit "$out" "MISSING"
same "exactly one MISSING row, for the id with no spec" "$(printf '%s\n' "$out" | grep -c 'MISSING')" "1"
miss "$out" "ARCH-tPlan-1        -           MISSING"
hit "$out" "roster: the README roster region"

# ---- a MALFORMED pair is a NAMED refusal, not a silent fall-through to the no-roster path. `region`
# ---- exits 3 for ABSENT and for MALFORMED alike, and treating that one status as "absent" is the
# ---- discarded-signal defect this kit has already shipped once.
reset_tree; readme tPlan
mkspec tPlan ARCH-tPlan-1 SPECCED "S1 a thing" "AC1 it works" "the bar" "none"
# `readme` already renders ONE units pair, so one more makes the malformed case the refusal is about.
units tPlan "| [ARCH-tPlan-1 — a second pair nobody granted](spec/one.md) | OPEN | rev-1 | 2026-08-01 |"
fixture
out=$(run --plan tPlan)
hit "$out" "the build README carries a units marker but not exactly one well-formed pair, so the roster this verb would join against is not a single slice:"
miss "$out" "ARCH-tPlan-1"

# ---- no roster marker at all: today's output, today's sentence, and the caveat is then TRUE.
reset_tree; readme tPlan
mkspec tPlan ARCH-tPlan-1 SPECCED "S1 a thing" "AC1 it works" "the bar" "none"
fixture
out=$(run --plan tPlan)
hit "$out" "roster: tracked specs under"
hit "$out" "a planned unit with no spec is invisible here"
miss "$out" "MISSING"

# ---- S6's extraction is BYTE-IDENTICAL at --status. A refactor and a behaviour change in one
# ---- reviewable diff is what this criterion exists to prevent.
reset_tree
run --preflight tRun --keepalive-id k1 >/dev/null
same "--status names a non-terminal unit through the extracted helper" "$(run --status tRun | grep -c 'next ')" "1"
# ---- the extraction selects the SAME first row as the inline pipeline it replaced. `region` is a
# ---- function INSIDE the driver, not a command here, so the control re-derives the slice with awk.
# ---- The first cut called `region` and the control returned empty, which would have compared the
# ---- helper against nothing and passed forever.
# The control reads the BUILD README, not the run-state file: main's redesign removed the copy,
# so the unit list lives in one place and is derived on every read. This control still
# re-derives the slice with awk rather than calling `region`, which is a driver function and
# not a command here — the first cut called it, got empty, and would have compared the helper
# against nothing and passed forever.
# The control re-derives with the SAME selector the driver now uses. Left at the broad `^| [` it
# asserted the fix had NOT happened - a control encoding the pre-fix behaviour turns green into
# proof of the defect.
want_unit=$(awk '/<!-- gen:build-index -->/{f=1;next} /<!-- .gen:build-index -->/{f=0} f' memory/builds/tRun/README.md | grep -E '^\| \[.*\]\(spec/' | grep -vE '\| (CLOSED|WONTDO) \|' | head -1 | sed -e 's/^| \[//' -e 's/\](spec\/.*//')
same "the control extracted a non-empty first row" "$([ -n "$want_unit" ] && echo yes || echo no)" "yes"
same "--status selects the same first row through the extracted helper" "$(run --status tRun | sed 's/.*· next //')" "$want_unit"


hit "$(run --plan tPlanEmpty)" "no tracked spec under this build, so every planned unit is MISSING; the README roster is what this verb reads to say WHICH, and with no spec beside it there is nothing to join that roster against"
git reset -q --hard HEAD~1; git clean -qfd

# ---- check 14: an unknown argument. The verbs are a closed set.
out=$(run --frobnicate tRun)
hit "$out" "unknown argument; the verbs are --preflight, --plan, --phase, --status, --resume, --close, --landed, --park and --abort: --frobnicate"
# ---- S10: the THREE enumerations name ONE set. The usage line was two verbs behind before this unit
# ---- and the refusal above is what an operator who mistypes a verb actually reads. Assert every verb
# ---- appears in all three, or the next verb repeats the drift a prior review already asked to fix.
for v in --preflight --plan --phase --status --resume --close --landed --park --abort; do
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
# `env -u GIT_GRAFT_FILE`, and the -u is load-bearing. This arm's meaning is "a graft is
# effective BY DEFAULT", so it must control the one variable that decides that rather than
# inherit it. The driver `export`s GIT_GRAFT_FILE=/dev/null as deliberate hardening, and that
# export reaches every child — so when `--close` ran the merge bar, which runs this selftest,
# the control got an empty merge-base and the leg redded. The gate could not pass in a state
# that was entirely legitimate: a branch touching tools/unattended/ un-skips this leg, and
# --close is exactly where it then runs.
same "graft-control: the graft gives two unrelated histories a merge-base"      "$(env -u GIT_GRAFT_FILE git -C "$gtmp" merge-base "$gz" main 2>/dev/null)" "$gz"
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

# ============================================================ TOOL-aBoundedVerdict-15
# ---- S1: the two phase writers that did NOT stage now do. The leg's whole per-run population is the
# ---- INDEX, so an unstaged phase is invisible to every leg check -- and --landed's check_clean then
# ---- refuses because the tree is dirty with --close's OWN write, blaming the operator's tree.
# ---- The arm is the SEQUENCE: --close then --landed with no intervening git add. Asserting either
# ---- verb alone passes today and proves nothing.
bcopen
run --close tRun >/dev/null 2>&1
n=$((n+1)); [ -n "$(git diff --cached --name-only -- memory/builds/tRun/RUN.md)" ] \
  || { echo "FAIL --close left its phase write unstaged, so the leg cannot see the run at all"; st=1; }

# ---- ...and --phase, the SECOND omission. Three of five staged, which is why rev-1's "the only phase
# ---- writer that does not stage" was wrong and why the source rule had to wait for both.
bcopen
run --phase tRun BUILDING --witness "$(git rev-parse HEAD)" >/dev/null 2>&1
n=$((n+1)); [ -n "$(git diff --cached --name-only -- memory/builds/tRun/RUN.md)" ] \
  || { echo "FAIL --phase left its write unstaged, and it was the second of the two omissions"; st=1; }

# ---- S2: --attest, because the two AGENT-attested keys had no writer and --abort REQUIRES both. Its
# ---- refusals first: no item, an undeclared item, and a MACHINE-checked item.
# ...and with NO run-state file at all: --attest must not mint one, because a record created by an
# attestation is a run that authorized its own existence.
reset_tree; rm -f memory/builds/tRun/RUN.md
hit "$(run --attest tRun --item keepalive-reaped)" "no run-state file, so there is no run to attest anything about"

bcopen
hit "$(run --attest tRun)" "--attest requires --item: an attestation with no item named is not an attestation"
hit "$(run --attest tRun --item not-a-real-item)" "--attest names an item that is not in the declared DoD set, so nothing would ever read it"
# The refusal reads the item's declared CHECKER rather than matching a pair of names, so a project
# that renames a machine item still gets refused and one that declares its own agent item gets the verb.
hit "$(run --attest tRun --item gates-green)" "--attest refuses a MACHINE-checked item, because writing its key by hand is the self-certification the Definition of Done exists to prevent; this item is checked by the driver"

# ---- ...and the accept path, which must derive the RECORD KEY rather than write the item name:
# ---- `parked-decisions-surfaced` is read from a line spelled `parked-surfaced:`.
bcopen
out=$(run --attest tRun --item parked-decisions-surfaced)
hit "$out" "attested"
hit "$(cat memory/builds/tRun/RUN.md)" "parked-surfaced: yes"
miss "$(cat memory/builds/tRun/RUN.md)" "parked-decisions-surfaced: yes"
n=$((n+1)); [ -n "$(git diff --cached --name-only -- memory/builds/tRun/RUN.md)" ] \
  || { echo "FAIL --attest wrote the key but did not stage it, so the leg cannot read it back"; st=1; }

# ---- ...and --abort becomes reachable WITHOUT a hand edit, which is the whole point of the verb.
bcopen
run --attest tRun --item keepalive-reaped >/dev/null
run --attest tRun --item parked-decisions-surfaced >/dev/null
hit "$(run --abort tRun --reason "the arm that proves the documented exit needs no hand edit")" "phase ABORTED"

# ---- S3: the override park is the FOURTH caller of a guard that existed in triplicate. A truthful
# ---- reason -- one that says why the flag matters -- used to red leg check 11 permanently on a record
# ---- no verb can rewrite. Refused in the validation loop, BEFORE anything is written.
bcopen
before=$(sum)
out=$(run --close tRun --override build-complete --reason "the lander must never be given --no-verify")
hit "$out" "an override item or reason spells the declared bypass flag, and the gate greps this file whole for it, so recording this would red the bar on a record no verb can rewrite; say it without the literal flag"
n=$((n+1)); [ "$(sum)" = "$before" ] || { echo "FAIL the bypass-flag override refusal fired AFTER writing, so it prevented nothing"; st=1; }

# ---- SOURCE-level, TOOL-aBoundedVerdict-15 S4: the two rules that were each followed everywhere but
# ---- once. Landing LAST, deliberately: a meta-gate written before its subject is clean reds on the
# ---- very diff that fixes it, and this repo has already paid a session for that ordering.
# ----
# ---- SCOPED BY FUNCTION, not by line distance. The first cut asked for `stage_or_fail` within three
# ---- lines of a phase write and for a bypass guard within forty lines of a `park` call, and it
# ---- produced three FALSE POSITIVES on correct code: verb_landed legitimately batches phase, witness
# ---- and units-at-landing before one stage, and both guarded park sites sit further from their guard
# ---- than an arbitrary window allows. A proximity rule measures text where the question is control
# ---- flow, and a meta-gate that fires on correct code is worse than none - it teaches its readers to
# ---- ignore it, or to contort code to satisfy it.
#
# Rule 1 - a function that writes the phase must also stage. Nothing about WHERE.
badstage=$(awk '
  /^[a-z_]+\(\)/ { fn = $1; ph[fn] = 0; sg[fn] = 0 }
  fn && /set_fact "\$rel" phase/ { ph[fn] = 1 }
  fn && /stage_or_fail/          { sg[fn] = 1 }
  END { for (f in ph) if (ph[f] && !sg[f]) print f }
' "$SCRIPT")
n=$((n+1)); [ -z "$badstage" ] || { echo "FAIL a function writes the phase and never stages it: $badstage"; st=1; }

# Rule 1's RED FIXTURE, without which the rule is silent whether it works or not: strip verb_close's
# stage and prove the rule names verb_close.
u4="$TMP/s4-unstaged.sh"
awk '/set_fact "\$rel" phase LANDING/ { print; skip = 1; next }
     skip && /stage_or_fail/ { skip = 0; next }
     { print }' "$SCRIPT" > "$u4"
ru=$(awk '
  /^[a-z_]+\(\)/ { fn = $1; ph[fn] = 0; sg[fn] = 0 }
  fn && /set_fact "\$rel" phase/ { ph[fn] = 1 }
  fn && /stage_or_fail/          { sg[fn] = 1 }
  END { for (f in ph) if (ph[f] && !sg[f]) print f }
' "$u4")
n=$((n+1)); [ -n "$ru" ] || { echo "FAIL S4 rule 1 does NOT fire on a copy with verb_close's stage removed, so it would not notice a regression"; st=1; }

# Rule 2 - a function that parks must also carry the bypass-flag guard. Same scoping, same reason.
#
# ONE DECLARED EXEMPTION, and the rule's limit stated with it: `verb_preflight` parks a waiver, and its
# guard lives in `check_waivers`, which it CALLS. This rule reads text and cannot follow a call, so a
# cross-function guard is declared here rather than pretended away. That is the whole cost of the
# scoping choice, and it is the second false positive this rule produced before being narrowed -- the
# first was a proximity window, this one a call boundary. A NEW name appearing in this exemption list
# deserves the scrutiny the rule exists to apply, not an edit to the list.
badguard=$(awk '
  /^[a-z_]+\(\)/ { fn = $1; pk[fn] = 0; gd[fn] = 0 }
  fn && /^ *park "\$rel"/ { pk[fn] = 1 }
  fn && /BYPASS_BAN/       { gd[fn] = 1 }
  END { for (f in pk) if (pk[f] && !gd[f] && f != "verb_preflight()") print f }
' "$SCRIPT")
n=$((n+1)); [ -z "$badguard" ] || { echo "FAIL a function parks an entry with no bypass-flag guard anywhere in it: $badguard"; st=1; }

# Rule 2's RED FIXTURE. Rule 1 had one and rule 2 did not, which I said out loud rather than shipping
# the asymmetry: a source rule with no negative control is the class this build keeps filing.
rg=$(awk '
  /^[a-z_]+\(\)/ { fn = $1; pk[fn] = 0; gd[fn] = 0 }
  fn && /^ *park "\$rel"/ { pk[fn] = 1 }
  fn && /BYPASS_BAN/       { gd[fn] = 1 }
  END { for (f in pk) if (pk[f] && !gd[f] && f != "verb_preflight()") print f }
' <(sed '/BYPASS_BAN/d' "$SCRIPT"))
n=$((n+1)); [ -n "$rg" ] || { echo "FAIL S4 rule 2 does NOT fire on a copy with every bypass guard deleted, so it would not notice a regression"; st=1; }

# ---- SOURCE-level, TOOL-aBoundedVerdict-12 S6: every `dod_met` arm this unit gives a message to must
# ---- actually carry a NON-EMPTY DOD_OUT assignment. The rule keys on the arm BODY rather than on a
# ---- literal `return 1`, because rev-1's predicate did exactly that and was VACUOUS: a literal
# ---- `return 1` appears in only two arms and both already set the variable, while six arms fail by
# ---- falling off the end of their case arm with a false test. So the shipped driver satisfied the
# ---- rule as first written, and the criterion claiming otherwise was false.
# ----
# ---- SCOPE IS DECLARED (S6a) rather than universal: this unit gives messages to gates-green,
# ---- build-complete and closing-review-recorded. `records-current`, `landed-via-lander` and
# ---- authorization-reachable are OUT -- the last prints through its own refusals now that S2 stopped
# ---- discarding them, and the other two belong to the LANDER-MARKER unit -- specced, not built, and
# ---- named here by what it is because a bare unbuilt id reads to the drift oracle as stale. The two agent-attested
# ---- arms and the `*)` project arm are exemptions: their cause is an absent attestation or an item
# ---- this kit knows nothing about, and the refusal already says so.
# ----
# ---- NON-EMPTY is the load-bearing word. `gates-green` clears DOD_OUT to "" on success, so a rule
# ---- satisfied by any assignment would be satisfied by the clearing one.
dodarm() { # arm label -> that arm's body out of dod_met's case block
  awk -v want="$1" '
    /^dod_met\(\) \{/ { inf = 1 }
    inf && $0 ~ "^    " want "\\)" { grab = 1; next }
    grab && /^    [a-z*][a-z-]*\)/ { grab = 0 }
    grab { print }
  ' "$SCRIPT"
}
for arm in gates-green build-complete closing-review-recorded; do
  body=$(dodarm "$arm")
  n=$((n+1))
  [ -n "$body" ] || { echo "FAIL S6 could not locate the $arm arm in dod_met, so this rule is grading nothing"; st=1; continue; }
  # NOT a quoted literal only: `gates-green` assigns from a command substitution,
  # DOD_OUT=$($GATE_CMD 2>&1), a good non-empty message the first cut called a violation.
  # The predicate is 'assigns something other than the empty string', as the prose always said.
  printf '%s\n' "$body" | grep -qE 'DOD_OUT=("[^"]|[^"])' \
    || { echo "FAIL the $arm arm reaches its failing exit with no non-empty DOD_OUT, so a blocked close names the item and not the cause"; st=1; }
done

# ---- ...and the RED FIXTURE, without which the loop above is the vacuity it exists to replace: strip
# ---- the assignments out of one arm in a COPY and prove the rule fires. A source rule with no red
# ---- fixture is indistinguishable from one whose locator silently matches nothing.
sfx="$TMP/s6-stripped.sh"   # $TMP is this suite's own scratch dir, made at line 14
# GENERIC, not a list of literal messages. The first cut named the four sentences it wanted gone, and
# -16 then rewrote one of them -- so the strip went stale, the arm kept a non-empty DOD_OUT, and this
# red fixture reported that the rule would not fire. It was right, which is what a negative control
# is for. Emptying every quoted assignment cannot go stale when a message is reworded.
sed 's/DOD_OUT="[^"]*"/DOD_OUT=""/g' "$SCRIPT" > "$sfx"
sbody=$(awk -v want="closing-review-recorded" '
    /^dod_met\(\) \{/ { inf = 1 }
    inf && $0 ~ "^    " want "\\)" { grab = 1; next }
    grab && /^    [a-z*][a-z-]*\)/ { grab = 0 }
    grab { print }
  ' "$sfx")
n=$((n+1))
[ -n "$sbody" ] || { echo "FAIL S6's red fixture lost the arm entirely, so the negative control proves nothing"; st=1; }
n=$((n+1))
printf '%s\n' "$sbody" | grep -qE 'DOD_OUT=("[^"]|[^"])' \
  && { echo "FAIL S6's rule does NOT fire on an arm stripped of its messages, so it would not notice a regression"; st=1; }

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
# THE ROSTER IS FROZEN AT LANDING. The unit list is derived from a MUTABLE README while a run is
# live, which is right — but a finished record must still answer which units it covered, and a later
# build touching that README would otherwise change a landed run's answer retroactively.
same "--landed froze the roster into the record" \
  "$(sed -n 's/^units-at-landing: //p' memory/builds/tRun/RUN.md)" "ARCH-tRun-1"
# ...and it survives the README moving underneath it, which is the whole point.
printf '%s\n' '| [ARCH-tRun-2 — a unit added later](spec/two.md) | OPEN | rev-1 | 2026-08-02 |' >> memory/builds/tRun/README.md
same "the frozen roster does not follow a later README edit" \
  "$(sed -n 's/^units-at-landing: //p' memory/builds/tRun/RUN.md)" "ARCH-tRun-1"
git checkout -q -- memory/builds/tRun/README.md 2>/dev/null || true
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
run --close tRun --override closing-review-recorded --reason "fixture build records no review" --override build-complete --reason "fixture build is one OPEN unit with no roster, by construction" --override records-current --reason "records lag" >/dev/null 2>&1
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
# THE DRIVE LIST IS FOUR, NOT FIVE, since kit 1.6 — `--preflight` ROTATES a finished record rather
# than refusing it (TOOL-dClosedLexicon-11), and is proven separately below. The derived count still
# covers all FIVE writers: four refuse here and the fifth is the rotation arm, so a SIXTH writer
# still reds this arm until someone places it.
writers=$(grep -c 'set_fact "$rel" phase' "$SCRIPT")
n=$((n+1)); [ "$writers" = 5 ]   || { echo "FAIL the driver has $writers phase writer(s); this arm drives 4 of them and the rotation arm below drives the fifth — place the new verb in one of the two, or the terminal guard is unproven for it"; st=1; }

reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: LANDED/' memory/builds/tRun/RUN.md
fixture
before=$(sum)
for v in "--phase tRun BUILDING --witness abc" "--close tRun" "--abort tRun --reason r" "--landed tRun"; do
  # shellcheck disable=SC2086
  out=$(run $v)
  hit "$out" "the run is already finished and a finished record is not something to move, re-open or re-pin"
  same "the finished record survived $v" "$(sum)" "$before"
done

# ============================================================ rotation: the fifth phase writer
# `--preflight` over a terminal record RETIRES it and starts a fresh run. The refusal above is right
# about the RECORD and was wrong as a policy about the BUILD: this repo's own first unattended run
# aborted with three units left and no second run could start.
#
# `sum()` at the top of this file is DELIBERATELY not re-pointed. It is a shared helper — `$(sum)`
# appears in nine arms, every one proving a refused verb wrote nothing — and `git hash-object` on a
# missing path exits 128 with EMPTY stdout, so re-pointing it would make eight unrelated arms compare
# "" to "" and pass whatever happened. Byte-identity here is `cmp -s` against a copy taken before the
# call, which is what the spec's AC2 asks for.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: ABORTED/' memory/builds/tRun/RUN.md
fixture
retired_copy=$(mktemp -t retired.XXXXXX); cp memory/builds/tRun/RUN.md "$retired_copy"
blob=$(git hash-object memory/builds/tRun/RUN.md)
arch="memory/builds/tRun/RUN.ABORTED.${blob:0:8}.md"
out=$(run --preflight tRun --keepalive-id k2)
hit "$out" "preflight OK"
hit "$out" "retired the finished record"
n=$((n+1)); [ -f "$arch" ]                     || { echo "FAIL rotation did not produce the derived archive path: $arch"; st=1; }
n=$((n+1)); [ -f memory/builds/tRun/RUN.md ]   || { echo "FAIL rotation left no fresh run-state file"; st=1; }
same "the fresh record starts at RUNNING" "$(sed -n 's/^phase: //p' memory/builds/tRun/RUN.md)" "RUNNING"
n=$((n+1)); cmp -s "$retired_copy" "$arch" || { echo "FAIL the archived bytes are not the retired record's"; st=1; }
# BOTH SIDES IN THE INDEX. The leg's whole per-run population is `git ls-files`, so an unstaged
# archive is invisible to every check the widened population gave it.
n=$((n+1)); git ls-files --error-unmatch "$arch" >/dev/null 2>&1 || { echo "FAIL the archive is not staged, so the gate leg cannot see it"; st=1; }
n=$((n+1)); [ "$(git hash-object memory/builds/tRun/RUN.md)" != "$blob" ] || { echo "FAIL RUN.md still hashes to the retired record — the fresh one was not written"; st=1; }

# ...and a NON-terminal record is not rotated. The green control for the arm above: without it,
# "rotation happened" and "rotation happens on everything" look the same.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
git add -A >/dev/null; git commit -q -m "live run" --no-verify
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "preflight OK"
miss "$out" "retired the finished record"
n=$((n+1)); [ -z "$(ls memory/builds/tRun/RUN.*.md 2>/dev/null)" ] || { echo "FAIL a NON-terminal record was rotated"; st=1; }

# ...and an archive already present with DIFFERENT bytes REFUSES, over an untouched tree. This is the
# branch that makes `GIT mv -f` safe: force is only ever applied to a destination the test cleared.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: ABORTED/' memory/builds/tRun/RUN.md
blob=$(git hash-object memory/builds/tRun/RUN.md)
printf 'a hand-placed file at the derived name\n' > "memory/builds/tRun/RUN.ABORTED.${blob:0:8}.md"
fixture
before=$(git hash-object memory/builds/tRun/RUN.md)
out=$(run --preflight tRun --keepalive-id k2)
hit "$out" "an archive already exists at the name this record derives, carrying DIFFERENT bytes — that cannot happen by rotation, so something placed it by hand and overwriting it would destroy a finished record"
same "the refused rotation left the record alone" "$(git hash-object memory/builds/tRun/RUN.md)" "$before"
n=$((n+1)); [ -z "$(git status --porcelain)" ] || { echo "FAIL the refused rotation left the tree dirty: $(git status --porcelain | head -3)"; st=1; }

# ...and a DIRECTORY at the derived name REFUSES before the write gate. MEASURED: `git mv -f` onto a
# directory exits 0 and files the record INSIDE it, so the retired record lands at `<dir>/RUN.md`,
# off the path every reader globs, with the verb reporting success. Letting git decide would have
# made a silent misfiling the happy path — which is why this is refused here rather than there.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: ABORTED/' memory/builds/tRun/RUN.md
blob=$(git hash-object memory/builds/tRun/RUN.md)
mkdir -p "memory/builds/tRun/RUN.ABORTED.${blob:0:8}.md"
printf 'x
' > "memory/builds/tRun/RUN.ABORTED.${blob:0:8}.md/inner.txt"
fixture
before=$(git hash-object memory/builds/tRun/RUN.md)
out=$(run --preflight tRun --keepalive-id k2)
hit "$out" "the name this record derives is occupied by something that is not a regular file, and a rename onto it would file the finished record somewhere no reader looks rather than fail"
same "the refused rotation left the record alone" "$(git hash-object memory/builds/tRun/RUN.md)" "$before"

# ...and an archive present with IDENTICAL bytes PROCEEDS. Plain `git mv` returns 128 here
# (`destination exists`), so without `-f` this case takes the refusal path the spec says it does not.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null
sed -i 's/^phase: .*/phase: ABORTED/' memory/builds/tRun/RUN.md
blob=$(git hash-object memory/builds/tRun/RUN.md)
cp memory/builds/tRun/RUN.md "memory/builds/tRun/RUN.ABORTED.${blob:0:8}.md"
fixture
out=$(run --preflight tRun --keepalive-id k2)
hit "$out" "preflight OK"
hit "$out" "retired the finished record"
same "the fresh record starts at RUNNING" "$(sed -n 's/^phase: //p' memory/builds/tRun/RUN.md)" "RUNNING"

# ---- TOOL-aBranchedMandate-12: a blocked --close NAMES the leg. The existing check-13 arm declares
# ---- GATE_CMD="false", which prints nothing, so it passes whether the output is forwarded or
# ---- discarded -- the same blind spot unit 2's AC4 found in the wiring arm one function away.
reset_tree; readme tRun
printf '#!/usr/bin/env bash
echo "GATEPROBE-the-leg-that-blocked-it"
exit 1
' > probe-gate.sh
mkconf "true" "bash probe-gate.sh"
fixture
run --preflight tRun --keepalive-id k1 >/dev/null
out=$(run --close tRun)
hit "$out" "a machine-checked DoD item is unmet, so --close blocks: gates-green"
hit "$out" "GATEPROBE-the-leg-that-blocked-it"

# ---- ...and a PASSING bar prints nothing. Without this the arm above is satisfied by a driver that
# ---- dumps the gate's output unconditionally, which is noise on every successful close.
reset_tree; readme tRun
printf '#!/usr/bin/env bash
echo "GATEPROBE-should-not-appear"
exit 0
' > probe-gate.sh
mkconf "true" "bash probe-gate.sh"
fixture
run --preflight tRun --keepalive-id k1 >/dev/null
miss "$(run --close tRun)" "GATEPROBE-should-not-appear"

# ---- TOOL-aBranchedMandate-3, S9: the SECOND ANCHOR. Every arm here drives the real bare origin the
# ---- fixture already builds, because the whole mechanism is an observation of a remote and a
# ---- fixture that stubbed it would be asserting against this test's own imagination.
# ----
# ---- The build README is committed on `unit` and NOT on `main`, which is the exact state the unit
# ---- exists for: the merge-base carries no build folder, so the first anchor refuses and the second
# ---- one is the only thing that can authorize the run.
scope() { printf 'ANCHOR_SCOPE="%s"\n' "$1" >> .unattended.conf; }

# S5's refusal set FIRST, because it decides whether any of the rest may fire. UNDECLARED, BLANK and
# MISSPELLED must all keep the strict anchor — a value-set guard whose failing case is untested is
# the guard that silently admits.
reset_tree; readme tBr; git add -A >/dev/null && git commit -q -m br --no-verify
git push -q -f origin unit 2>/dev/null
for s in "" "publshed" "PUBLISHED" "default-branch"; do
  reset_tree; readme tBr; [ -n "$s" ] && scope "$s"; git add -A >/dev/null && git commit -q -m br --no-verify; git push -q -f origin unit 2>/dev/null
  out=$(run --preflight tBr --keepalive-id k1)
  hit "$out" "no build README at the pinned BASE, so nothing committed before this run branched authorizes it"
done

# ...and DECLARED, the same tree, now authorizes. Paired with the arms above so "it refused" and "it
# refused for the reason we think" are two claims, not one.
reset_tree; readme tBr; scope published; git add -A >/dev/null && git commit -q -m br --no-verify
git push -q -f origin unit 2>/dev/null
out=$(run --preflight tBr --keepalive-id k1)
miss "$out" "no build README at the pinned BASE, so nothing committed before this run branched authorizes it"
hit "$out" "preflight OK"
hit "$(cat memory/builds/tBr/RUN.md)" "anchor-kind: run-branch"
hit "$(cat memory/builds/tBr/RUN.md)" "branch-ref: refs/heads/unit"

# ---- 32: the branch is committed but NOT published. Nothing the remote advertises authorizes it.
reset_tree; readme tBr; scope published; git add -A >/dev/null && git commit -q -m br --no-verify
git push -q origin :refs/heads/unit 2>/dev/null
out=$(run --preflight tBr --keepalive-id k1)
hit "$out" "the remote advertises no tip for the branch this run is on, so nothing published authorizes it; push the branch first: refs/heads/"
git push -q -f origin unit 2>/dev/null

# ---- 33: the remote advertises a tip that is NOT an ancestor of HEAD. A real advertised commit, not
# ---- a missing one — the spec names that distinction because a fixture using an absent ref proves
# ---- only that absence refuses.
reset_tree; readme tBr; scope published; git add -A >/dev/null && git commit -q -m br --no-verify
# A SIBLING commit: parented on main, present in THIS clone (commit-tree writes it here), and not
# an ancestor of HEAD. Pushing `main` itself does not work — main IS an ancestor of the unit
# branch, so the guard correctly stays silent and the arm proves nothing. Pushing from the second
# clone does not work either: the object would be missing locally and refusal 30 fires first.
side=$(git commit-tree "$(git rev-parse HEAD^{tree})" -p "$(git rev-parse main)" -m side)
git push -q -f origin "$side:refs/heads/unit" 2>/dev/null
out=$(run --preflight tBr --keepalive-id k1)
hit "$out" "the advertised tip of this run's branch is not an ancestor of HEAD, so it names history this run does not build on and cannot be its base: refs/heads/"
git push -q -f origin unit 2>/dev/null

# ---- 30 branch 2: the remote advertises a tip this clone does not have. Pushed from a SECOND clone
# ---- so the object genuinely never reaches this one.
reset_tree; readme tBr; scope published; git add -A >/dev/null && git commit -q -m br --no-verify
C2=$(mktemp -d)
git clone -q "$ORIGIN" "$C2/c2" 2>/dev/null
( cd "$C2/c2" && git config user.email t@t.test && git config user.name t \
  && git checkout -q -B unit && git commit -q --allow-empty -m offshore \
  && git push -q -f origin unit ) 2>/dev/null
out=$(run --preflight tBr --keepalive-id k1)
hit "$out" "the remote advertises a branch tip this clone does not have, so no comparison against it means anything; fetch and re-run: refs/heads/"
rm -rf "$C2"
git push -q -f origin unit 2>/dev/null

# ---- 31: a detached HEAD has no branch for the remote to advertise a tip for.
reset_tree; readme tBr; scope published; git add -A >/dev/null && git commit -q -m br --no-verify
git checkout -q --detach 2>/dev/null
out=$(run --preflight tBr --keepalive-id k1)
hit "$out" "the run is not on a named branch, so there is no branch for the remote to advertise a tip for, and a detached HEAD cannot be the second anchor"
git checkout -qf unit

# ---- S12's WIDENED fail 18. The guard now fires only for a base on NEITHER derivation, which is
# ---- strictly smaller than before — so without a failing case here "monotone" and "deleted" look
# ---- identical from outside. The base recorded is a commit on no advertised history at all.
reset_tree; readme tBr; scope published; git add -A >/dev/null && git commit -q -m br --no-verify
git push -q -f origin unit 2>/dev/null
run --preflight tBr --keepalive-id k1 >/dev/null
ORPHAN=$(git commit-tree -m orphan "$(git rev-parse HEAD^{tree})" 2>/dev/null)
sed -i "s|^base: .*|base: $ORPHAN|" memory/builds/tBr/RUN.md
out=$(run --close tBr)
hit "$out" "the BASE recorded in the run-state file is not an ancestor of the base this history derives"

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

# ---- TOOL-cSettledDocket-1: `--park`, the fourth writer of a parked entry and the first available
# ---- MID-RUN. §2 declares four kinds; park() had callers for three, and DECISION — the kind §2
# ---- names first — had none. GREEN CONTROL first, then one arm per refusal.
reset_tree; run --preflight tRun --keepalive-id k1 >/dev/null

# GREEN CONTROL: the happy path writes exactly one row, of the declared kind.
out=$(run --park tRun --item "do facts 5-7 pin with fact 4" --reason "widens the unit; owner call")
hit "$out" "decision parked"
same "exactly one decision row" "$(grep -c 'decision · item ' memory/builds/tRun/RUN.md)" "1"
hit "$(cat memory/builds/tRun/RUN.md)" "decision · item do facts 5-7 pin with fact 4 · reason widens the unit; owner call"

# ...and it is IDEMPOTENT on the same pair. The protocol's post-compaction recovery re-runs the run's
# own steps, so a re-derived refusal must not duplicate. NOT --waive's rule: that compares handle
# SETS, this compares one pair, because there is no set here to compare.
out=$(run --park tRun --item "do facts 5-7 pin with fact 4" --reason "widens the unit; owner call")
hit "$out" "already parked, unchanged"
same "the repeat added no row" "$(grep -c 'decision · item ' memory/builds/tRun/RUN.md)" "1"

# ...a DIFFERENT question is a second row, not a no-op.
run --park tRun --item "second question" --reason "also owner" >/dev/null
same "a different item parks its own row" "$(grep -c 'decision · item ' memory/builds/tRun/RUN.md)" "2"

# ...and --status SURFACES it, which is the whole point of writing it somewhere a reader reaches.
# The arm here used to assert the slug appeared in --status's output — true on every reachable path,
# so it could not fail, and it documented a capability the verb did not have. It has it now.
hit "$(run --status tRun)" "· parked 2"
miss "$(run --status tNoPark)" "· parked"

# refusal: no --item.
before=$(git hash-object memory/builds/tRun/RUN.md)
out=$(run --park tRun --reason "r")
hit "$out" "--park requires --item, because a parked entry with no question recorded is the bare 'parked' the protocol calls indistinguishable from 'forgotten'"
same "a refused park wrote nothing" "$(git hash-object memory/builds/tRun/RUN.md)" "$before"

# refusal: no --reason.
out=$(run --park tRun --item "q")
hit "$out" "--park requires --reason, because an entry recording no reason is indistinguishable from one nobody meant - the same argument --waive already makes"

# refusal: a reason spelling the declared bypass flag. park() writes it verbatim and leg check 11
# greps the file WHOLE, so recording it would red the bar on a record no verb can rewrite.
out=$(run --park tRun --item "q" --reason "the lander wanted --no-verify")
hit "$out" "the item or the reason spells the declared bypass flag, and the gate greps this file whole for it, so recording this would red the bar on a record no verb can rewrite; say it without the literal flag"
# ...and the ITEM half, which is the half that shipped unscreened: check 11 greps the file WHOLE,
# so it does not care which field spelled the flag.
before=$(git hash-object memory/builds/tRun/RUN.md)
hit "$(run --park tRun --item "drop --no-verify from the lander" --reason r)" "the item or the reason spells the declared bypass flag"
same "the unscreened field wrote nothing either" "$(git hash-object memory/builds/tRun/RUN.md)" "$before"

# refusal: a NEWLINE in the reason. This is the one --waive refusal rev-1 of the spec left out, and
# it is the load-bearing one here: park() appends ONE line and check 17 parses the region line-wise,
# so a reason carrying a newline forges a second parked row that no verb wrote.
out=$(run --park tRun --item "q" --reason "$(printf 'first\nsecond')")
hit "$out" "a parked item or reason contains a newline, and park() appends ONE line that the gate parses line-wise, so this would forge a second parked row nothing wrote"
same "the forged row was not written" "$(grep -c 'decision · item ' memory/builds/tRun/RUN.md)" "2"

# refusal: an item spelling the record's own field separator, which would make its row unparseable
# by the very check that grades it.
hit "$(run --park tRun --item 'a · reason b' --reason r)" "a parked item spells the record's own field separator ' · ', which makes the row unparseable by the check that reads it"

# refusal: a TERMINAL record. Two guards, not one — see the next arm for why.
run --phase tRun LANDING --witness "$(git rev-parse HEAD)" >/dev/null 2>&1 || true
sed -i 's/^phase: .*/phase: ABORTED/' memory/builds/tRun/RUN.md
hit "$(run --park tRun --item q --reason r)" "ABORTED via --park"

# refusal: NO RECORD AT ALL. `refuse_if_terminal` returns 0 for a file that does not exist, so a
# design leaning on it alone would let --park mint a parked entry for a run that never started.
reset_tree; rm -f memory/builds/tRun/RUN.md
out=$(run --park tRun --item q --reason r)
hit "$out" "no run-state file, so there is no run to park a decision against"
same "--park created no record" "$([ -f memory/builds/tRun/RUN.md ] && echo yes || echo no)" "no"
reset_tree

# ---- check 44: the authorization mode is a CLOSED set, and a value outside it refuses rather than
# ---- defaulting. Paired with a no-write arm, because "it printed a refusal" and "it changed
# ---- nothing" are two claims - and this branch sits BEFORE the write gate precisely so both hold.
reset_tree
out=$(run --preflight tModeBad --keepalive-id k1)
hit "$out" "the build README at the pinned BASE declares an authorization mode outside the closed set of prompt and slug, and defaulting an unrecognised mode would select a discipline nobody declared"
same "check 44 created no run-state file" "$([ -f memory/builds/tModeBad/RUN.md ] && echo yes || echo no)" "no"

# ---- the PASSING direction, which is the only thing that tells a WORKING reader from a dead one:
# ---- with the key absent the record says `slug`, and with a dead parse it says `slug` too. This
# ---- arm is the discriminator, and it is why the fixture orders the key after `slug:`.
reset_tree
out=$(run --preflight tModeOk --keepalive-id k1)
hit "$out" "preflight OK"
hit "$(cat memory/builds/tModeOk/RUN.md)" "mode: prompt"
git rm -q --cached memory/builds/tModeOk/RUN.md >/dev/null 2>&1; rm -f memory/builds/tModeOk/RUN.md

# ---- ABSENT is `slug`, which is every build README written before this key existed. Run over
# ---- tFresh, an untouched fixture, so the arm cannot pass because of something this unit wrote.
reset_tree
out=$(run --preflight tFresh --keepalive-id k1)
hit "$out" "preflight OK"
hit "$(cat memory/builds/tFresh/RUN.md)" "mode: slug"
git rm -q --cached memory/builds/tFresh/RUN.md >/dev/null 2>&1; rm -f memory/builds/tFresh/RUN.md
reset_tree

# ---- check 45: a waiver of a PROMPT-scoped directive on a run that is not prompt-authorized. The
# ---- refusal cannot live in check_waivers, which runs BEFORE the authorization read that produces
# ---- the mode - there AUTH_MODE is unset for both modes, so one spelling never fires and the other
# ---- always does. These arms are what prove it is evaluated where the mode exists.
reset_tree
out=$(run --preflight tFresh --keepalive-id k1 --waive researched --reason "does not apply here")
hit "$out" "--waive names a directive scoped to prompt-authorized runs while this run is not one, so the waiver would record the relaxation of a rule that never bound it:"
same "check 45 created no run-state file" "$([ -f memory/builds/tFresh/RUN.md ] && echo yes || echo no)" "no"

# ---- ...and an ALL-scoped handle on the SAME run is accepted, or the refusal is just a broken
# ---- waiver path wearing a scope's name.
reset_tree
out=$(run --preflight tFresh --keepalive-id k1 --waive reuse-first --reason "owner accepted the silence")
hit "$out" "preflight OK"
hit "$out" "directive waived — reuse-first"
git rm -q --cached memory/builds/tFresh/RUN.md >/dev/null 2>&1; rm -f memory/builds/tFresh/RUN.md

# ---- ...and the PROMPT-scoped handle IS accepted on a prompt-authorized run, which is the whole
# ---- point of the scope rather than a way to refuse things.
reset_tree
out=$(run --preflight tModeOk --keepalive-id k1 --waive researched --reason "the prompt named one solution")
hit "$out" "preflight OK"
hit "$(cat memory/builds/tModeOk/RUN.md)" "waiver · item researched"
git rm -q --cached memory/builds/tModeOk/RUN.md >/dev/null 2>&1; rm -f memory/builds/tModeOk/RUN.md
reset_tree

# ---- review M1: a malformed build README must leave NO run-state file behind. `scaffold_runmd` ran
# ---- BEFORE this validation, so the refusal fired over a tree the verb had already changed - and
# ---- the retry then met the DIRTY-TREE refusal, naming a cause that was this verb's own leftover.
# ---- The adjacent comment claimed the scaffold happens after every precondition; it now does.
reset_tree
out=$(run --preflight tUnpaired --keepalive-id k1)
hit "$out" "the build README's generated markers are malformed, and the unit list is DERIVED from there, so an unpaired marker is not something to guess around"
same "a malformed README leaves no orphan run-state file" "$([ -f memory/builds/tUnpaired/RUN.md ] && echo yes || echo no)" "no"
reset_tree

# FLOOR_ASSERTIONS — TOOL-cBriefedPilot-23. A shrink-only pin on the EXECUTED count. This build
# shipped nine arms stranded past an unconditional `exit`: the file still contained them, so a static
# grep saw nine and `check-arms.py` text-matched nine, and the only signal that moved was this total,
# which nothing compared to anything. Lower it in a reviewed diff or not at all.
FLOOR_ASSERTIONS=338
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
