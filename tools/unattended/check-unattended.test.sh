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
# THE FIXTURE'S KIT HOME, ONCE (TOOL-aGradedDoorway-2). `seed()` INSTALLS the kit here and every
# arm below RUNS it here, and those had been two independent spellings of one fact. An adopter at
# another prefix had to repath all of them by hand, and a missed one is SILENT rather than red:
# `mutate` and `cp` no-op on a path that does not exist, so the arm asserts against a tree it never
# changed and passes. The default keeps gov byte-identical; an adopter sets it once, and the arms
# are run at a foreign prefix to prove the suite still grades.
KIT_REL="${KIT_REL:-tools/unattended}"
HERE="$(cd "$(dirname "$0")" && pwd)"

# ---- THE SHARD CONTRACT — ADOPTED, not reinvented (TOOL-aShardedFloor-3) -------------------------
# The contract is TOOL-aShardedFloor-2's and its reasoning lives in the head of
# tools/unattended/unattended.test.sh: one file and two guarded contiguous regions rather than a
# physical split (which `check-arms.py`'s one-gate-one-sibling map and the armed-branch pin refuse),
# the flag PARSED rather than position-read, and the refusal before any scratch dir exists.
#
# What differs here is the SEAM and the floors, which is why this is a second unit rather than a
# second paragraph. Its HOIST SET is two — `anchor_break` and `anchor_restore`.
SHARD_ARITY=2
SHARD=""; SHARD_GIVEN=0
if [ "${1:-}" = --shard ]; then
  SHARD_GIVEN=1; SHARD="${2:-}"
elif [ $# -gt 0 ]; then
  echo "check-unattended.test: unrecognised argument '$1' — this suite takes '--shard <i>/<n>' or nothing"; exit 2
fi
# A BARE `--shard` takes the same refusal branch as a bad value. Keying on a non-empty value instead
# lets a bare flag run the FULL suite under a leg that claims to be a shard.
if [ "$SHARD_GIVEN" = 1 ]; then
  [ -n "$SHARD" ] || { echo "check-unattended.test: --shard takes '<i>/<n>', got no value"; exit 2; }
  case "$SHARD" in
    */*) : ;;
    *) echo "check-unattended.test: --shard takes '<i>/<n>', got '$SHARD'"; exit 2 ;;
  esac
  SH_I=${SHARD%%/*}; SH_N=${SHARD##*/}
  case "$SH_I$SH_N" in *[!0-9]*|"") echo "check-unattended.test: --shard indices must be numeric, got '$SHARD'"; exit 2 ;; esac
  [ "$SH_N" = "$SHARD_ARITY" ] || { echo "check-unattended.test: --shard arity must be $SHARD_ARITY, got '$SHARD'"; exit 2; }
  [ "$SH_I" -ge 1 ] 2>/dev/null && [ "$SH_I" -le "$SHARD_ARITY" ] \
    || { echo "check-unattended.test: --shard index out of range 1..$SHARD_ARITY, got '$SHARD'"; exit 2; }
else
  SH_I=0
fi
in_shard() { [ "$SH_I" = 0 ] || [ "$SH_I" = "$1" ]; }

TMP=$(mktemp -d)
trap 'rm -rf "$TMP" "${ORIGIN_DIR:-}"' EXIT
st=0; n=0
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }
miss() { n=$((n+1)); if grep -qF -- "$2" <<<"$1"; then echo "FAIL unexpected: $2"; st=1; fi; }
same() { n=$((n+1)); [ "$2" = "$3" ] || { echo "FAIL $1: expected [$3], got [$2]"; st=1; }; }

cd "$TMP" || exit 2
git init -q -b main . && git config user.email t@t.test && git config user.name t \
  && git config core.autocrlf false
mkdir -p $KIT_REL memory/guides
cp "$HERE/check-unattended.sh" "$HERE/unattended.sh" "$HERE/lib-unattended.sh" "$HERE/PROTOCOL.template.md" "$HERE/SKILL.template.md" $KIT_REL/
# BOTH SIDES OF THE MERGE ADDED A SEED HERE, for different checks, and both are needed.
# Check 28 compares the parser inlined in the driver AND the playbook leg and then runs it
# over the shipped template, so a tree missing either takes the missing-from-the-pair branch
# and every arm below grades that refusal. Check 22 joins the protocol key table against the
# EXAMPLE CONF and refuses when it is absent. A fixture that drops either models a broken
# install rather than a repo.
cp "$HERE/check-playbook.sh" "$HERE/PLAYBOOK-TEMPLATE.template.md" "$HERE/.unattended.conf.example" $KIT_REL/
cp "$HERE/PROTOCOL.template.md" memory/guides/UNATTENDED-PROTOCOL.md
SCRIPT="$TMP/$KIT_REL/check-unattended.sh"

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
# NO DISPATCH_GRADING. TOOL-dUnstalledConvoy-23 retired that key when the comparison became a
# REPORT that always runs: a report has no failure to gate, and a key that only silences output makes
# a check dark without saying so. Check 22 joins the protocol key table against the declared conf, so
# a fixture still setting it declares a key the protocol no longer documents - which is how this
# surfaced, on a merge where one side removed the key and the other still seeded it.
#
# NO BACKTICKS IN THIS BLOCK. It sits inside an UNQUOTED heredoc, so a backticked identifier is
# COMMAND SUBSTITUTION and the fixture writes a conf with a shell error in it. This comment cost a
# 50-minute suite run to find, which is the only reason it is this loud.
HALT_CODES_EXTRA=""
HALT_FLOOR="${HFLOOR_OVERRIDE:-$HALT_FLOOR_DERIVED}"
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
HALT_FLOOR_DERIVED="$(grep '^HALT_CODES_CORE=' "$HERE/unattended.sh" | sed 's/^HALT_CODES_CORE="//; s/"$//' | wc -w)"
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
# TOOL-dHonouredPark-4 fallout. Check 30 asserts its own LIVENESS — it refuses to report clean when
# it walked no build whose `--plan` returned a verdict — and every fixture build here has an EMPTY
# generated units region and no spec, so `--plan` refused for all of them and the check redded on a
# population of zero. Five arms failed for a fixture that predates the check.
#
# A SEPARATE BUILD, not a reshape of tRun. Dozens of arms below assert against tRun's README and
# run-state file; changing its shape to satisfy one check would put every one of them at risk. This
# one exists only to be counted, and nothing else references it.
#
# SPECCED, NOT CLOSED, deliberately: check 30 separately flags a build whose every tracked spec is
# TERMINAL, so the obvious status would trade this red for that one.
mkdir -p memory/builds/tPlanOk/spec
cat > memory/builds/tPlanOk/README.md <<'PLANOK'
---
slug: tPlanOk
node: a
opened: 2026-08-01
streams: architecture
roster: ARCH
ids: ARCH-tPlanOk-1
---

# tPlanOk

<!-- gen:build-index -->
**Build status:** SPECCED · 1 unit(s)
<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [ARCH-tPlanOk-1 — the unit](spec/one.md) | SPECCED | rev-1 | 2026-08-01 |
<!-- /gen:build-units -->
<!-- /gen:build-index -->
PLANOK
printf '# ARCH-tPlanOk-1 the unit

**Status:** SPECCED · rev-1 · 2026-08-01 · node a · Tier-1 · base 00000000 · streams architecture
' > memory/builds/tPlanOk/spec/one.md
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
# A scratch dir for STUBBED BINARIES, prepended to PATH by the arms that need one. Used to fire a
# code path whose real trigger is a network partition, which no fixture can arrange.
# ITS PARENT IS TRAPPED, not just the stub inside it. `$(mktemp -d)/bin` leaked one scratch directory
# per invocation, and the EXIT trap above never learned the parent. Orphaned scratch dirs are not
# cosmetic here: 99 of them accumulated in one session and the next suite aborted at startup with
# `Device or resource busy` - see memory/gotchas/bounded-through-a-pipe-is-unbounded.md.
TMPBIN_PARENT=$(mktemp -d); TMPBIN="$TMPBIN_PARENT/bin"
trap 'rm -rf "$TMP" "${ORIGIN_DIR:-}" "${TMPBIN_PARENT:-}"' EXIT

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

# ---- HOISTED FOR THE SHARD CONTRACT. Region two drives these too; they are MOVED rather than
# ---- duplicated, because two definitions of one helper is two answers to one question.
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

# ---- REGION ONE ----------------------------------------------------------------------------------
# Bodies are NOT reindented: `check-arms.py` reads lines and skips comments, so an unindented wrapper
# leaves every arm signature byte-identical and the armed-branch pin untouched.
if in_shard 1; then
# ---- a leg that reds on everything arms every branch and checks nothing.
out=$(run); rc=$?
same "a conforming tree exits 0" "$rc" "0"
same "a conforming tree prints nothing" "$out" ""

# ---- check 1, all three branches: no conf, a key undeclared, and the driver's core sets unreadable.
# ---- ROUND 9's BLOCKER: the conf could no longer END this leg and could still HIJACK it, because the
# ---- real source ran in the MAIN shell below `status=0` and below `fail()`. Two shapes, and both are
# ---- graded on the EXIT CODE rather than on output text - shape B produces no output at all, so an
# ---- output-only assertion cannot see it. The conf is imported through a subshell now, so nothing it
# ---- defines, traps or exits crosses into this process.
for _hijack in "trap 'exit 0' EXIT" 'fail() { :; }'; do
  reset_tree
  sed -i 's/^LANDER=.*/LANDER=""/' .unattended.conf
  printf '%s
' "$_hijack" >> .unattended.conf
  out=$(run); rc=$?
  same "a conf that takes over the shell does not take over the verdict: $_hijack" "$rc" "1"
done
reset_tree

# ---- ROUND 8's BLOCKER 1, OTHER HALF: this leg SOURCES the conf in its main shell, so one appended
# ---- `exit 0` in a tracked file the graded run can commit itself ends the leg at status 0 - which
# ---- `run-gates` reads as GATE ok, with every check below unrun and nothing saying so. The probe that
# ---- guards it is a subshell, so an abort inside it is a status rather than an exit of this process.
reset_tree; ( printf 'exit 0
'; cat .unattended.conf ) > .unattended.conf.new && mv .unattended.conf.new .unattended.conf
out=$(run); rc=$?
same "a conf that ends the shell does not end the leg at 0" "$rc" "1"
hit "$out" "the project conf does not source cleanly, so this leg cannot read a single declared value - and sourcing it in this shell would let that file end or take over the leg rather than be graded by it"

reset_tree; rm -f .unattended.conf
hit "$(run)" "no .unattended.conf at the repo root, and every value this leg checks is declared there"

reset_tree; sed -i 's/^LANDER=.*/LANDER=""/' .unattended.conf
out=$(run)
hit "$out" "a required key is undeclared in .unattended.conf, and an undeclared value is not a defaulted one"
hit "$out" "LANDER"

reset_tree; sed -i 's/^PHASES_CORE=.*/PHASES_CORE=unparseable/' $KIT_REL/unattended.sh
hit "$(run)" "cannot read the kit's core sets from the driver, so every membership check below would pass over an empty set"

# ---- a FOURTH branch, separate from the one above because an empty mode
# ---- vocabulary is a different failure. The other core sets stay readable, so the leg runs on and
# ---- every mode-membership test passes over nothing - a green that means the opposite of what it
# ---- looks like, which is exactly why it refuses instead of carrying on.
# ---- the SLACK arms, the mirror of the shrink arms above. A floor BELOW the kit's own core count
# ---- is not a pin: the set grew, the declaration did not, and the pin now sits under the value it
# ---- guards. Both halves, because a pin armed on one half is a pin on one half.
reset_tree; sed -i 's/^CORE_FLOOR=.*/CORE_FLOOR="12:2"/' .unattended.conf
hit "$(run)" "the declared Definition-of-Done floor sits below the kit's own core count, so the pin guards nothing and a later deletion would pass it - declared against core:"
reset_tree; sed -i 's/^CORE_FLOOR=.*/CORE_FLOOR="2:10"/' .unattended.conf
hit "$(run)" "the declared PHASE floor sits below the kit's own core count, so the pin guards nothing and a later deletion would pass it - declared against core:"
reset_tree

reset_tree; sed -i 's/^AUTH_MODES=.*/AUTH_MODES=unparseable/' $KIT_REL/unattended.sh
hit "$(run)" "cannot read AUTH_MODES from the driver, so the mode-membership branch and the directive scope join would both pass over an empty set - an empty vocabulary makes every check keyed on it vacuously true"

# ---- the same read, one set over (TOOL-dNarrowedAnchor-1), and the DIRECTION of the failure is why
# ---- it gets its own refusal rather than a default. An unreadable AUTH_MODES makes checks keyed on
# ---- it vacuously TRUE; an unreadable SECOND_ANCHOR_MODES makes check 29 treat every mode as
# ---- inadmissible, so it would red every branch-anchored run in the tree instead of passing them.
reset_tree; sed -i 's/^SECOND_ANCHOR_MODES=.*/SECOND_ANCHOR_MODES=unparseable/' $KIT_REL/unattended.sh
hit "$(run)" "cannot read SECOND_ANCHOR_MODES from the driver, so check 29 would treat every declared mode as inadmissible on the second anchor and red every branch-anchored run in the tree"

# ---- checks 2 and 3: the CORE sets are one-directional. Deleting a member reds; ADDING a project
# ---- member is green — and that green half is the arm that keeps the check from being "the sets
# ---- must be exactly the core sets", which would make PHASES_EXTRA and DOD_EXTRA unusable.
reset_tree; sed -i 's/^PHASES_CORE="[^"]*"/PHASES_CORE=""/' $KIT_REL/unattended.sh
hit "$(run)" "cannot read the kit's core sets from the driver, so every membership check below would pass over an empty set"

# ---- The floor is a COUNT because the membership form was measured VACUOUS: the leg composes the
# ---- effective set as core plus extras, so core is a subset by construction and "every core member
# ---- is present" can never fail. It armed cleanly and tested nothing. These arms delete a core
# ---- member from the DRIVER — the only place the names live — and watch the count fall.
reset_tree
# reset_tree's `git clean -qfd` removes the copied kit, so the arm re-stages it before editing.
# Without this the sed edits nothing, the grep counts nothing, and the arm passes by finding nothing.
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
ncore=$(grep '^PHASES_CORE=' $KIT_REL/unattended.sh | tr -d '
' | sed 's/^PHASES_CORE="//; s/"$//' | wc -w)
short=$(grep '^PHASES_CORE=' $KIT_REL/unattended.sh | tr -d '
' | sed 's/^PHASES_CORE="//; s/"$//')
sed -i "s|^PHASES_CORE=.*|PHASES_CORE=\"${short% *}\"|" $KIT_REL/unattended.sh
out=$(run)
hit "$out" "the kit's CORE phase vocabulary has shrunk below its floor, and deleting a core member is a silent, reason-free override of everything keyed on it"
hit "$out" "$((ncore-1)) against $ncore"
# ...the member deleted was a TERMINAL one, so the independent terminal-membership check fires too.
# Two sets declared separately, so THAT one is falsifiable where the subset form was not.
hit "$out" "a TERMINAL phase is not in the effective vocabulary, so no run could ever reach it"




# ---- CHECK 8's MARKER-SHAPE BRANCH, on a TERMINAL record. The exemption used to clear `rd` for any
# ---- terminal phase, which skipped this refusal as well as the emptiness one — so a finished record
# ---- with malformed generated markers was exempt from a shape check that has nothing to do with why
# ---- the exemption exists. Measured when it was scoped: unexempting this branch reds nothing in the
# ---- corpus, which is exactly why it needs a fixture. A check whose only evidence is a corpus that
# ---- cannot trigger it is the fixture-passes-by-finding-nothing class.
reset_tree; mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh; mkconf
mkdir -p memory/builds/tMarker
printf '# tMarker - run state\n\n<!-- run:generated -->\n\n## Run facts\nphase: LANDED\nwitness: 0123456789abcdef0123456789abcdef01234567\nbase: 0123456789abcdef0123456789abcdef01234567\nunits-at-landing: ARCH-tMarker-1\n' > memory/builds/tMarker/RUN.md
printf 'readme\n' > memory/builds/tMarker/README.md
git add -A >/dev/null 2>&1; git -c commit.gpgsign=false commit -q -m marker --no-verify >/dev/null 2>&1
hit "$(run)" "a run-state file's generated markers are malformed"
# ...and the EMPTINESS refusal keeps its terminal exemption, which is the half the exemption is for:
# a finished record legitimately carries a frozen roster in that region.
printf '# tMarker - run state\n\n<!-- run:generated -->\nunits-at-landing frozen here\n<!-- /run:generated -->\n\n## Run facts\nphase: LANDED\nwitness: 0123456789abcdef0123456789abcdef01234567\nbase: 0123456789abcdef0123456789abcdef01234567\n' > memory/builds/tMarker/RUN.md
git add -A >/dev/null 2>&1; git -c commit.gpgsign=false commit -q -m marker2 --no-verify >/dev/null 2>&1
out=$(run)
miss "$out" "a run-state file's generated markers are malformed"
reset_tree




# ---- EVERY DISPATCHED VERB IS DOCUMENTED, joined from the driver's own `case "$VERB"` arms to the
# ---- three synopsis strings and the Skill template. `--review` shipped reachable and named NOWHERE:
# ---- not in the Skill, not in the protocol's verb list, and missing from all three driver strings —
# ---- directly under a comment claiming "THE SAME SET, in all three places". A verb no procedure
# ---- mentions is a verb no run uses, and its gate check then grades a population nothing creates.
D="$HERE/unattended.sh"
# THE POPULATION IS BOTH DISPATCH SITES, not one. The first cut scanned only `case "$VERB" in` for
# 2-space-indented arms and found nine verbs; `--plan` and `--phase` are dispatched from the ARGV
# loop at a different indent and were invisible to it. An arm that grades nine of eleven verbs
# reports full coverage of a set it never saw - the same could-not-fail shape one level up, and the
# reason this derives the set from every `--verb)` case arm in the file rather than from one block.
verbs=$(grep -oE '^ +--[a-z]+\)' "$D" | tr -d ' )' | sort -u)
# ...minus the FLAGS, which are arguments rather than verbs and are documented by the verb they
# belong to. Named explicitly, because a flag silently treated as a verb would demand a Skill
# section nobody should write.
# `--witness` is NOT here: it is read inside the --phase handler rather than dispatched as its own
# case arm, so it never enters the derived population and exempting it removed nothing. The
# assertion below caught that on its first run, which is the entire reason it exists.
_denied='--keepalive-id --item --value --override --waive --reason --code --subject --verdict --blockers --act --pass --successor --writes --leg --path --step --records-root --playbook-sha --run --set'
for _f in $_denied; do
  verbs=$(printf '%s
' "$verbs" | grep -vxF -- "$_f" || true)
done
# A FLOOR, NOT A NON-EMPTINESS TEST. The old guard refused only an EMPTY population, which is exactly
# how a nine-of-eleven population passed while reporting full coverage. The floor is shrink-only and
# is the number of verbs this kit dispatches; adding one and forgetting to document it now reds here
# rather than widening the set the join grades.
_nverbs=$(printf '%s
' "$verbs" | grep -c .)
# FOURTEEN, the verbs this kit actually dispatches. It was 12 against a population of 18 - four of
# main's flags had not been denied, so the count was inflated and two verbs could have stopped being
# dispatched with the floor still green. A floor set against a polluted population pins nothing.
n=$((n+1)); [ "$_nverbs" -ge 14 ] || { echo "FAIL the dispatched-verb population read $_nverbs verbs against a floor of 14, so the documentation join below would grade a set smaller than the kit actually ships"; st=1; }
# ...and every DENYLIST entry must really be a flag, or a stale exemption silently narrows the
# population the join covers. A name is a flag when it is dispatched but assigns rather than acting;
# the cheap proxy is that it must still appear as a case arm in the driver.
for _f in $_denied; do
  n=$((n+1)); grep -qE "^ +\Q$_f\E\)" "$D" 2>/dev/null || grep -qE "^ +$_f\)" "$D" || { echo "FAIL the flag denylist exempts $_f, which the driver no longer dispatches - a stale exemption narrows the verb set this join grades and nothing else would notice"; st=1; }
done
undoc=""
for v in $verbs; do
  grep -q -- "$v" "$HERE/SKILL.template.md" 2>/dev/null || undoc="$undoc $v(skill)"
  # THE USAGE SURFACE is the driver's own header block, which `usage()` self-reads and prints; the
  # REFUSAL SURFACE is the verb DECLARATION, which `verb_list()` renders into the refusal text. Both
  # used to be greps for a literal single-line `echo` and a typed `the verbs are --a, --b` string -
  # exactly the two hand-maintained lists this kit replaced with derivations, so an arm pinned to
  # their spelling calls a driver that fixed the drift broken.
  grep -qE "^#   unattended[.]sh $v( |\$)" "$D" || undoc="$undoc $v(usage)"
  grep -qE "^VERBS_(SLUG|INLINE)=.*$v( |\")" "$D" || undoc="$undoc $v(refusal)"
done
n=$((n+1)); [ -z "$undoc" ] || { echo "FAIL a dispatched verb is absent from a surface an agent reads, so no run can learn it exists:$undoc"; st=1; }


# ---- THE REVIEW-LOOP CHECK. Its three clauses cannot be exercised by the corpus, which is exactly why
# ---- they need fixtures — and the FIRST arm is about the check being able to run at all. It reads the
# ---- ceiling from the driver through `core_of`, which parses only a DOUBLE-QUOTED value; when that
# ---- read came back empty the whole three-clause check was skipped and said nothing, which is
# ---- indistinguishable from a clean corpus. An unreadable ceiling is a refusal now.
reset_tree; mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh; mkconf
sed -i 's/^RUNAWAY_CEILING=.*/RUNAWAY_CEILING=8/' $KIT_REL/unattended.sh


hit "$(run)" "the driver declares no readable RUNAWAY_CEILING, so the review-loop check below would be skipped entirely and its absence would look exactly like a clean corpus"

# ---- AND THE SAME SHAPE FOR THE THREE REMOTE BOUNDS, which is where this class was actually LIVE:
# ---- all three were declared unquoted in the driver, so every core_of read returned empty and a
# ---- `${x:-60}` fallback restated the numbers from memory. The leg then observed the remote under
# ---- bounds it invented while a comment above claimed a single source, and tuning the driver moved
# ---- nothing. Unquoting one here reproduces exactly that read.
reset_tree; mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh; mkconf
sed -i 's/^REMOTE_CONNECT_BOUND=.*/REMOTE_CONNECT_BOUND=20/' $KIT_REL/unattended.sh
hit "$(run)" "the driver declares no readable REMOTE_BOUND, REMOTE_CONNECT_BOUND or REMOTE_LOWSPEED_BYTES, so this leg would observe the remote under bounds it invented rather than the ones the driver uses; core_of reads a double-quoted value only, so an unquoted constant reads as absent"

# a group whose counts do not shrink and which records no exit
reset_tree; mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh; mkconf
mkdir -p memory/builds/tRev
printf '# tRev\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nphase: RUNNING\nwitness: abc\n\n2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2\n\n2026-08-20T02:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2\n\n2026-08-20T03:00:00Z review · item S1 · reason verdict BLOCKED · blockers 3\n' > memory/builds/tRev/RUN.md
git add -A >/dev/null 2>&1; git -c commit.gpgsign=false commit -q -m rev --no-verify >/dev/null 2>&1
out=$(run)
hit "$out" "review loops that ran past the ceiling, stalled without recording it, or exited without promoting"
hit "$out" "blocker counts did not shrink across consecutive rounds and no round carries an exit token"

# ...and the SAME sequence carrying an exit token is green. Without this the arm above could be
# passing because the check reds on any review group at all.
printf '# tRev\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nphase: RUNNING\nwitness: abc\n\n2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2\n\n2026-08-20T02:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT\n' > memory/builds/tRev/RUN.md
git add -A >/dev/null 2>&1; git -c commit.gpgsign=false commit -q -m rev2 --no-verify >/dev/null 2>&1
miss "$(run)" "blocker counts did not shrink across consecutive rounds"
reset_tree


# ---- THE HALT VOCABULARY: six refusals, each armed by a POSITIVE assertion naming its own text. All
# ---- six were OBSERVED against the real tree before they were armed here, which is the order this
# ---- repo asks for — a gate whose failing case has only ever been imagined is an assertion about
# ---- nothing. The driver-editing arms re-stage the kit copy first: reset_tree's `git clean -qfd`
# ---- removes it, and without the re-stage the sed edits nothing and the arm passes by finding nothing.

reset_tree; mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh
mkconf; sed -i 's/^HALT_FLOOR=.*/HALT_FLOOR=""/' .unattended.conf
# SED, not the override channel: `${HFLOOR_OVERRIDE:-$DERIVED}` substitutes the default when the
# override is empty, so an empty override declares the key rather than clearing it — the arm passed
# by testing the opposite of what it says.
hit "$(run)" "HALT_FLOOR is undeclared in .unattended.conf, and with no floor a deleted halt code is indistinguishable from a vocabulary that never had one"

reset_tree; mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh
HFLOOR_OVERRIDE="seven" mkconf
# A WORD, not a numeral. The shrink-only comparison below it is `-ge`, which on a non-numeric operand
# is a shell error rather than a verdict — so a floor that reads as English disarms the pin while
# looking set, which is worse than one left blank.
hit "$(run)" "HALT_FLOOR is not a single integer, so the shrink-only comparison below would be a string test wearing a numeric name"

reset_tree; mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh
mkconf; sed -i 's/^HALT_CODES_CORE="[a-z-]* /HALT_CODES_CORE="/' $KIT_REL/unattended.sh
hit "$(run)" "the kit's CORE halt vocabulary has shrunk below its floor, and deleting a member is a silent, reason-free override of every record that cited it"

reset_tree; mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh
mkconf; sed -i 's/^HALT_CODES_CORE=.*/HALT_CODES_CORE=""/' $KIT_REL/unattended.sh
hit "$(run)" "the driver declares no HALT_CODES_CORE vocabulary, so the abort verb would validate against an empty set and accept anything"

# ---- and the two record-level refusals. The population is every TRACKED run-state file, archived ones
# ---- included, so the fixture has to be committed for the check to see it at all.
reset_tree; mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh; mkconf
mkdir -p "memory/builds/tHalt"
printf '# tHalt - run state\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nphase: ABORTED\nwitness: 0123456789abcdef0123456789abcdef01234567\nbase: 0123456789abcdef0123456789abcdef01234567\n' > memory/builds/tHalt/RUN.md
git add -A >/dev/null 2>&1; git -c commit.gpgsign=false commit -q -m halt --no-verify >/dev/null 2>&1
out=$(run)
# the check's own header, which is what the arms gate signs the branch with; the per-record line
# below says WHICH record.
hit "$out" "aborted run-state records whose halt code is missing or outside the effective vocabulary"
hit "$out" "phase ABORTED and no halt-code fact, so the record says a run stopped and never says why"

sed -i 's/^phase: ABORTED/halt-code: not-a-real-code\nphase: ABORTED/' memory/builds/tHalt/RUN.md
git add -A >/dev/null 2>&1; git -c commit.gpgsign=false commit -q -m halt2 --no-verify >/dev/null 2>&1
hit "$(run)" "halt-code outside the effective vocabulary: not-a-real-code"

# ...and the CONTROL: a legal code is silent. Without it every arm above could be passing because the
# check reds on any aborted record at all, which is the shape that would also red the whole corpus.
sed -i 's/^halt-code: not-a-real-code/halt-code: fork-unresolvable/' memory/builds/tHalt/RUN.md
git add -A >/dev/null 2>&1; git -c commit.gpgsign=false commit -q -m halt3 --no-verify >/dev/null 2>&1
out=$(run)
miss "$out" "phase ABORTED and no halt-code fact"
miss "$out" "halt-code outside the effective vocabulary"
reset_tree


# ---- THE PARKED-KIND TAXONOMY, both refusals, driven the way every other core-set arm here is: by
# ---- editing the DRIVER COPY, which is the only place the set lives. The re-stage before each edit
# ---- is load-bearing — reset_tree's `git clean -qfd` removes the copied kit, and without it the sed
# ---- edits nothing, the grep finds nothing, and the arm passes by finding nothing.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh
# a STALE MEMBER: a kind in the taxonomy that no park call site writes. This is the direction the
# join asserts, and the failure it exists for — a count that exists to be narrow, silently wider.
sed -i 's|^PARK_KINDS_OWED=.*|PARK_KINDS_OWED="decision abort override waiver ghostkind"|' $KIT_REL/unattended.sh
out=$(run)
hit "$out" "the parked-kind taxonomy names a kind no park call site in the driver writes, so a count that exists to be narrow is silently wider than the code it measures"

reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh
# ...and the VACUITY arm. An empty set would make the surfaced count and the parked-decisions
# Definition-of-Done item both range over nothing, which is the empty-population shape this kit
# refuses by name everywhere else.
sed -i 's|^PARK_KINDS_OWED=.*|PARK_KINDS_OWED=""|' $KIT_REL/unattended.sh
out=$(run)
hit "$out" "the driver declares no PARK_KINDS_OWED taxonomy, so the surfaced count and the parked-decisions Definition-of-Done item both range over a set this leg cannot read"

reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" $KIT_REL/unattended.sh
# ...and the CONTROL: the shipped set is green. Without it both arms above could be passing because
# the check reds on everything.
out=$(run)
miss "$out" "the parked-kind taxonomy names a kind no park call site in the driver writes"
miss "$out" "the driver declares no PARK_KINDS_OWED taxonomy"


reset_tree; mkconf "PARKED" ""
out=$(run)
miss "$out" "the kit's CORE phase vocabulary has shrunk below its floor"
same "a project phase EXTENSION is green" "$(run)" ""

reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
ndod=$(grep '^DOD_CORE=' $KIT_REL/unattended.sh | tr -d '
' | sed 's/^DOD_CORE="//; s/"$//' | wc -w)
sed -i 's/ parked-decisions-surfaced:agent"$/"/' $KIT_REL/unattended.sh
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
reset_tree; sed -i 's/^PHASES_CORE="[^"]*"/PHASES_CORE=" "/' $KIT_REL/unattended.sh
hit "$(run)" "the effective phase vocabulary is empty, which makes every phase check below vacuously true"
reset_tree; sed -i 's/^DOD_CORE="[^"]*"/DOD_CORE=" "/' $KIT_REL/unattended.sh
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

# ---- check 9: THE REMOTE COUNT IS ITS OWN FAULT, not an answer about the remote. Zero remotes and
# ---- two-plus remotes both used to arrive downstream as an empty advertisement and print 'the
# ---- remote advertised no tips' - a sentence about the REMOTE for a misconfiguration in this
# ---- clone. The split existed above; only the reporting did not.
reset_tree; mkconf
git remote remove origin
out=$(run)
hit  "$out" "this clone declares NO remote, so there is no endpoint to observe and whether a recorded BASE is published was never asked; that is a fault in this clone rather than an answer about any remote: recorded"
miss "$out" "the remote advertised no tips"
git remote add origin "$ORIGIN"

reset_tree; mkconf
git remote add second "$ORIGIN"
out=$(run)
hit  "$out" "this clone declares more than one remote, so which endpoint published would even mean is a guess; the leg refuses to pick one rather than measuring the BASE against whichever name sorts first: recorded"
miss "$out" "the remote advertised no tips"
git remote remove second
reset_tree

# ---- THE PROMOTION CLAUSE, which had NO arm at all - neither of its two messages was assertedanywhere, so the rewrite that made it count across subjects was landed unobserved. Two subjects both
# ---- exit NON-CONVERGENT and the region gains exactly ONE id since the run BASE, so the count is
# ---- short by one and the clause must say so. A per-subject reading would have passed this.
reset_tree; mkconf
mkdir -p memory/builds/tProm
printf '# tProm\n\n<!-- gen:build-units -->\n| Unit | Status |\n|---|---|\n| TOOL-tProm-1 | CLOSED |\n<!-- /gen:build-units -->\n' > memory/builds/tProm/README.md
git add -A >/dev/null 2>&1 && git -c commit.gpgsign=false commit -q -m promobase --no-verify
PROMBASE=$(git rev-parse HEAD)
printf '# tProm\n\n<!-- gen:build-units -->\n| Unit | Status |\n|---|---|\n| TOOL-tProm-1 | CLOSED |\n| TOOL-tProm-2 | CLOSED |\n<!-- /gen:build-units -->\n' > memory/builds/tProm/README.md
printf '# tProm\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nphase: RUNNING\nwitness: abc\nbase: %s\n\n2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT\n\n2026-08-20T02:00:00Z review · item S2 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT\n' "$PROMBASE" > memory/builds/tProm/RUN.md
git add -A >/dev/null 2>&1
hit "$(run)" "2 subject(s) EXITED without converging and the generated units region gained only 1 unit id(s) this run BASE lacked, so at least one blocker was neither fixed nor promoted"
reset_tree

# ---- check 9: A TRANSPORT FAILURE IS NOT AN ANSWER EITHER. Splitting the wall-clock bound out left
# ---- every OTHER non-zero - auth refused, DNS gone, a 404 endpoint - reporting as a statement about
# ---- what the remote advertised, which is a claim the leg never got close enough to make.
reset_tree; mkconf
git remote set-url origin "https://nonexistent.invalid/no/such.git"
out=$(run)
hit  "$out" "the remote could not be reached to observe its tips, so whether a recorded BASE is published is UNKNOWN rather than answered no; that is a transport or credential fault and not a statement about what the remote holds: recorded"
miss "$out" "the remote advertised no tips"
git remote set-url origin "$ORIGIN"
reset_tree

# ---- check 9: A TIP THIS CLONE DOES NOT HAVE IS NOT AN ANSWER. `merge-base --is-ancestor` fails
# ---- both when the commit is not an ancestor AND when the tip object is missing, and is_published
# ---- used to collapse those into 'not published'. Cost a red bar for real on 2026-08-21: the
# ---- remote advanced, this clone had not fetched, and all SIXTEEN honest run records reported as
# ---- naming commits that exist only locally - then the same leg went green minutes later once the
# ---- tip arrived. A bar that reds on network timing rather than on the tree teaches people to
# ---- re-run instead of to read.
# ---- The fixture advertises a tip built INSIDE the bare origin, so the clone cannot have it.
reset_tree; mkconf
ghost=$(git --git-dir="$ORIGIN" commit-tree "$(git --git-dir="$ORIGIN" rev-parse HEAD^{tree})" -m ghost -p "$(git --git-dir="$ORIGIN" rev-parse HEAD)")
git --git-dir="$ORIGIN" update-ref refs/heads/main "$ghost"
n=$((n+1)); git cat-file -e "$ghost^{commit}" 2>/dev/null && { echo "FAIL the ghost tip IS present in this clone, so the arm below would grade the ordinary published path instead of the unobservable one"; st=1; }
out=$(run)
hit  "$out" "the remote advertised tips this clone does not have, so whether a recorded BASE is published CANNOT BE OBSERVED and this leg will not answer a question it could not ask; fetch and re-run: recorded"
miss "$out" "is an ancestor of no tip the remote advertises"
git --git-dir="$ORIGIN" update-ref refs/heads/main "$ANCHOR0"
reset_tree

# ---- check 22: the section-8 key table and the KIT'S EXAMPLE conf, joined both ways, plus a
# ---- one-way check that this project sets nothing undocumented. Three keys reached
# ---- the tree undocumented and one of them REDS this leg when undeclared, so an adopter configuring
# ---- from the contract got a refusal naming a key the contract never mentioned. Check 10 is a
# ---- byte-diff of the pair and both copies were identically incomplete, which is the limitation its
# ---- own header states. Misspelling ONE row fires both directions at once, which is the arm.
# ...and the check REFUSES when it cannot read its own reverse population, rather than skipping. A
# `[ -f ]` guard around the whole thing made it vanish silently exactly where a documentation join is
# worth most, and a check that says nothing reads identically to one that passed.
reset_tree
rm -f $KIT_REL/.unattended.conf.example
hit "$(run)" "the kit ships no .unattended.conf.example, so the key table below can be joined against nothing and this check would pass by grading an empty set"
reset_tree

reset_tree
sed -i 's/| `HALT_FLOOR` |/| `HALT_FLOOOR` |/' memory/guides/UNATTENDED-PROTOCOL.md
out=$(run)
hit "$out" "the protocol's binding key table and the declared conf disagree, so a key is either configurable and undocumented or documented and dead. undocumented in the protocol:"
hit "$out" "undocumented in the protocol: HALT_FLOOR"
hit "$out" "documented but in no example: HALT_FLOOOR"
reset_tree
miss "$(run)" "the protocol's binding key table and the declared conf disagree"

# ---- check 9: THE THREE OBSERVATION OUTCOMES, KEPT APART. One message covered all three, so a dead
# ---- scratch dir and a fired wall-clock bound both reported as "the remote advertised no tips" and
# ---- sent the reader at the network. The driver had already split these one file over.
# the wall-clock bound FIRING, stubbed at `timeout` so the run does not actually wait it out
reset_tree
mkdir -p "$TMPBIN"; printf '#!/bin/sh\ncase "$*" in *"1 true") exit 0 ;; esac\nexit 124\n' > "$TMPBIN/timeout"; chmod +x "$TMPBIN/timeout"
out=$(PATH="$TMPBIN:$PATH" run)
hit  "$out" "the remote observation was KILLED by this kit's own wall-clock bound rather than answered, so the recorded BASE could not be checked; that is a partition or a stalled server, not a remote that advertises nothing"
miss "$out" "the remote advertised no tips"
rm -f "$TMPBIN/timeout"

# a scratch file that cannot be created: a fault on THIS side, and it used to skip both observations
# in silence, which read downstream as a remote answering nothing
reset_tree
out=$(TMPDIR=/nonexistent-scratch-dir run)
hit  "$out" "cannot create a scratch file to capture the remote advertisement, so this leg observed NOTHING and the BASE predicates below would be graded against an empty answer; this is a fault on THIS side, not the remote's"
miss "$out" "the remote advertised no tips"
reset_tree

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
# a LEGAL halt code rides along: the aborted population is graded for one now, and without it
# this fixture would red on a check that has nothing to do with what it tests.
mutate memory/builds/tRun/RUN.md 's/^phase: RUNNING$/phase: ABORTED/'
sed -i 's/^phase: ABORTED/halt-code: fork-unresolvable\nphase: ABORTED/' memory/builds/tRun/RUN.md
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
reset_tree; rm -f $KIT_REL/PROTOCOL.template.md
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
# a LEGAL halt code rides along: the aborted population is graded for one now, and without it
# this fixture would red on a check that has nothing to do with what it tests.
sed -i 's/^phase: .*/phase: ABORTED/' memory/builds/tRun/RUN.md
sed -i 's/^phase: ABORTED/halt-code: fork-unresolvable\nphase: ABORTED/' memory/builds/tRun/RUN.md; git add -A
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
# ---- The anchor helpers are HOISTED to the prologue for the shard contract.

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
# AN EMPTY BARE REPO, not a missing one. A path that does not exist is a TRANSPORT fault and reports
# as one since the five-cause split; "advertised no tips" is reserved for a remote that answered and
# had nothing to say, which is what an initialised-but-empty bare repo produces.
reset_tree
git init -q --bare "$ORIGIN_DIR/empty.git"
git remote set-url origin "$ORIGIN_DIR/empty.git"
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

fi   # ---- end REGION ONE ----------------------------------------------------------------------

# ---- REGION TWO ----------------------------------------------------------------------------------
# THE SEAM, chosen between two block-edge candidates and MEASURED. It sits at the end of the
# lifecycle block, which is the safer of the two: it keeps that block's un-restored `main`/origin
# state on one side rather than straddling the boundary. The alternative, the end of check 14, is
# the more balanced candidate and its timing is recorded in this build's record beside this one.
#
# NOT chosen by arm count. One tokenisation of this file splits nearly evenly while the
# git-operation weight splits about 2:1 — and the bar's floor is the LARGER shard, so an imbalance
# measured the wrong way eats the win directly.
#
# Neither candidate separates an arm from its control. The obvious-looking cut one line earlier
# does exactly that, which is why the boundary is stated here rather than left to a line number.
if in_shard 2; then
# REPLAY WHAT REGION ONE LEAVES, and it is one property rather than a pile of state: region one's
# anchor arms repeatedly check out main, commit, force-push and then merge main back into unit, so by
# this seam `unit` is an ANCESTOR of `main`. The tWaive fixture below relies on that without saying
# so — its `git merge -q --no-edit main >/dev/null 2>&1` is a FAST-FORWARD in the whole-suite run.
#
# MEASURED, both ways. Whole suite at this point: `Updating d0faf46..ab26c43`, merge rc 0. Shard two
# without this line: the branches have diverged, that merge is a real one, it CONFLICTS on
# memory/builds/tRun/RUN.md, and `>/dev/null 2>&1` swallows the conflict whole. `BUILD-METHOD.md`
# then never reaches unit, `--preflight` refuses on check 34 with "no build method under the memory
# root", no run-state file is written — and THREE arms fail naming a waiver, none of them naming the
# cause. That is what this one line buys, and it is why it is a line rather than a comment.
if [ "$SH_I" = 2 ]; then
  git checkout -qf main && git merge -q --no-edit unit >/dev/null 2>&1
  git push -q -f origin main >/dev/null 2>&1
  git checkout -qf unit
fi
reset_tree

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
# ----
# ---- THE PROPERTY IS "NO WRITE INTO THE TREE IT JUDGES", not "no redirect anywhere", and the two
# ---- stopped being the same thing when the leg's remote observations became BOUNDED. A wall-clock
# ---- bound has to capture through a FILE — `out=$(timeout N cmd)` reads until EOF and a surviving
# ---- descendant holds the pipe, so the verdict is bounded while the clock is not — and that file is a
# ---- `mktemp` scratch path outside the repository.
# ----
# ---- So the exemption checks a PROPERTY rather than blessing a line: a redirect is allowed only when
# ---- its target variable is assigned from `mktemp` somewhere in this same file. Blessing the spelling
# ---- `>"$out"` would let any future variable called `out` write anywhere; deriving the allowed names
# ---- from the mktemp assignments means the exemption shrinks and grows with the code it describes.
reset_tree
# the variables this file assigns from mktemp — the only legal redirect targets
mkt=$(grep -oE '^[[:space:]]*(local +)?[A-Za-z_][A-Za-z0-9_]*=\$\(mktemp' "$HERE/check-unattended.sh" \
      | sed -E 's/^[[:space:]]*(local +)?//; s/=\$\(mktemp$//' | sort -u)
# ONE PATTERN VARIABLE, shared by this arm and by the BOUND on its exemption below. They used to
# carry two different regexes: this one ends with a LITERAL dollar, matching a redirect into a
# variable; the bound ended with a bare dollar, an end-of-line anchor, and dropped the leading
# word-boundary group as well. So every redirect the exemption removes sat OUTSIDE the bound's
# population and the stated bound did not hold over redirects at all - it still fired on mv, rm and
# cp, which is why it read as armed.
# UNDERSCORE IN THE BOUNDARY CLASS. `[^-[:alnum:]]` does not exclude `_`, so a VARIABLE whose name
# ends in one of these verbs matched as a write: this kit's OWN check-unattended.sh carries
# `for _pv_rm in $(GIT ls-files ...)` in check 30, and the word `rm` inside that identifier reds
# this arm against a file that writes nothing. A name is not a command.
WRITE_RE='(^|[^-_[:alnum:]])(mv|rm|cp|sed -i|tee|> *"?\$)'
w=$(grep -nE "$WRITE_RE" "$HERE/check-unattended.sh" \
    | grep -v '^[0-9]*: *#' || true)
# A line is exempt when its write touches a SCRATCH variable and the line names no path in the
# tree under judgement. That is the property spelled directly rather than a verb-by-verb chase:
# a redirect into the scratch file and the cleanup that removes it are both fine, and either
# would stop being fine the moment the same line also named the memory root.
if [ -n "$w" ] && [ -n "$mkt" ]; then
  for v in $mkt; do
    w=$(printf '%s\n' "$w" | grep -vF -- "$v" || true)
  done
  w=$(printf '%s\n' "$w" | grep -v '^[[:space:]]*$' || true)
fi
n=$((n+1)); [ -z "$(printf '%s' "$w" | tr -d '[:space:]')" ] || { echo "FAIL the leg contains a write into the tree it judges: $w"; st=1; }
# ...and the exemption is not vacuous: this file MUST actually declare a mktemp scratch variable, or
# the loop above filtered nothing and the arm is the old one wearing a new comment.
n=$((n+1)); [ -n "$mkt" ] || { echo "FAIL the read-only arm derived no mktemp scratch variable, so its exemption filtered nothing and the property it claims to check is not the one it checks"; st=1; }
# THE EXEMPTION IS BOUNDED: no line it removed may also name the memory root, or the property
# check would be exempting a real write to the tree under judgement.
n=$((n+1)); [ -z "$(grep -nE "$WRITE_RE" "$HERE/check-unattended.sh" | grep -v '^[0-9]*: *#' | grep -F -- "$mkt" | grep -E '($M|memory)/' || true)" ] || { echo "FAIL a line exempted as scratch also names the tree under judgement, so the read-only exemption is covering a real write"; st=1; }

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
reset_tree; mv $KIT_REL/SKILL.template.md $KIT_REL/SKILL.template.md.bak
hit "$(run)" "the kit ships no SKILL.template.md, so the directive table an agent reads cannot be joined to the registry it is supposed to mirror; a shipped kit always has one, so this is a broken install rather than a project choice"
mv $KIT_REL/SKILL.template.md.bak $KIT_REL/SKILL.template.md

# arm 2: a template with no readable row. This is the arm that matters most — without it the join
# passes by finding nothing, which is the class this whole build keeps meeting.
reset_tree; grep -v '^[[:space:]]*| `[a-z]' $KIT_REL/SKILL.template.md > t.md && mv t.md $KIT_REL/SKILL.template.md
hit "$(run)" "the Skill template carries no directive table row this leg can read, so arm A would join the registry against nothing and pass by finding nothing; the row shape it looks for is a leading pipe then a backticked lowercase handle"

# arm 3: a row citing two sections has no single answer to read. The reset is load-bearing: without
# it this ran on the tree arm 2 left behind, whose rows were all stripped, so the sed matched nothing
# and the arm asserted a state its own fixture had just made unreachable.
reset_tree; sed -i 's/| the transcript rule under a mandate |/| M2 |/' $KIT_REL/SKILL.template.md   # a second M<n> must be its OWN CELL
hit "$(run)" "a directive row cites more than one build-method section, so the join has no single answer to read for that handle"

# arm 4: declared in the registry, absent from the table.
reset_tree; sed -i '/| `wrap-up-derived` |/d' $KIT_REL/SKILL.template.md
hit "$(run)" "a directive is declared in the registry and absent from the Skill's table, so the agent that reads the table is bound by a set it was never shown"

# arm 5: in the table, absent from the registry — the other direction, and it needs its own arm
# because a one-way containment check would pass here.
reset_tree; sed -i 's/^DIRECTIVES_CORE="minimal-prose:M10 /DIRECTIVES_CORE="/' $KIT_REL/unattended.sh
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
reset_tree; sed -i 's/^DIRECTIVES_CORE="[a-z-]*:M[0-9]* /DIRECTIVES_CORE="/' $KIT_REL/unattended.sh
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
# The build-method carrier for the driver arms below, DERIVED from the registry it must satisfy.
# Typed out, it listed the sections the registry cited on the day it was written and every later
# directive redded the GREEN CONTROL of an unrelated arm — a fixture falling behind the thing it
# exists to support, reported as a failure of whatever ran next. The MISSING-section case keeps its
# own hand-written carrier at arm 6 above, which is where that negative belongs.
{ printf '# method\n'
  grep -m1 '^DIRECTIVES_CORE=' $KIT_REL/unattended.sh \
    | grep -oE ':M[0-9]+' | tr -d ':' | sort -u | while read -r _sec; do printf '\n## %s\n' "$_sec"; done
} > memory/guides/BUILD-METHOD.md
n=$((n+1)); [ "$(grep -c '^## M' memory/guides/BUILD-METHOD.md)" -ge 8 ] \
  || { echo "FAIL the derived build-method carrier holds too few sections to satisfy the registry"; st=1; }
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
# a LEGAL halt code rides along: the aborted population is graded for one now, and without it
# this fixture would red on a check that has nothing to do with what it tests.
sed -i 's/^phase: RUNNING$/phase: ABORTED/' memory/builds/tRun/RUN.md
sed -i 's/^phase: ABORTED/halt-code: fork-unresolvable\nphase: ABORTED/' memory/builds/tRun/RUN.md
git add -A && git commit -q -m tWaive --no-verify && git push -q -f origin main
# A FAST-FORWARD, and the region-two opener above is what keeps it one. A real merge here conflicts
# on tRun/RUN.md and this redirection swallows it whole — measured, and the reason that opener exists.
git checkout -q unit && git merge -q --no-edit main >/dev/null 2>&1
WP=$(git rev-parse HEAD)
wreset() { git reset -q --hard "$WP"; git clean -qfd; }
drive() { bash "$KIT_REL"/unattended.sh "$@" 2>&1; }
wline() { grep -F ' waiver · item ' memory/builds/tWaive/RUN.md; }

# GREEN CONTROL: the driver writes the waiver, the record's first commit carries it, the leg is silent.
wreset
dout=$(drive --preflight tWaive --keepalive-id k1 --waive minimal-prose --reason taken-by-the-owner)
hit "$dout" "preflight OK"
same "the driver wrote a waiver line the leg can select" "$([ -n "$(wline)" ] && echo yes)" "yes"
git add -A && git commit -q -m waived --no-verify
out=$(run); wrc=$?
same "a tree whose waiver was taken at preflight exits 0" \
  "$wrc$([ "$wrc" != 0 ] && printf ' — %s' "$(printf '%s\n' "$out" | grep -m1 'FAILED')")" "0"
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
mutate $KIT_REL/SKILL.template.md '2i Invoke /session-kickoff before anything else.'
hit "$(run)" "the Skill template puts the kickoff step BEFORE --preflight, and kickoff invoked first halts at its READY card with nobody under a mandate to answer it: /session-kickoff at line"

# ...kickoff never named at all. ABSENCE IS A REFUSAL rather than the safe side, because a template
# that never names kickoff and one that names it too early read identically on any count.
reset_tree; kick_engine
mutate $KIT_REL/SKILL.template.md '\|/session-kickoff|d'
hit "$(run)" "the Skill template never names /session-kickoff while this project declares a kickoff engine, and a missing step reads exactly like a deadlocked one on any count-based check"

# ...no --preflight invocation to order anything against.
reset_tree; kick_engine
mutate $KIT_REL/SKILL.template.md '/unattended.sh --preflight/d'
hit "$(run)" "the Skill template names no --preflight invocation, so there is no anchor to order the kickoff step against and the sequence this check exists to hold is unstated"

# ---- 30 (TOOL-dHonouredPark, closing review round 3): a --plan run may never claim terminality over
# ---- a build it graded nothing on. The check WALKS the corpus, so its liveness assertion is the one
# ---- that decides whether a clean verdict means anything: with every build's units pair broken,
# ---- every --plan refuses, the walk grades nothing, and a check without this branch would report
# ---- clean over an empty population.
# ---- BOTH BUILDS. The comment above describes a fixture that predates tPlanOk: breaking tRun alone
# ---- WAS enough when tRun was the only build, and tPlanOk was added in this same round precisely so
# ---- that one build grades. From that commit on, this arm asserted a message the check cannot emit —
# ---- `--plan tPlanOk` exits 0, the walk counts one verdict, and the liveness branch never fires.
# ---- Measured on the fixture: tRun alone gives 0 hits, both give 1.
reset_tree
mutate memory/builds/tRun/README.md '/gen:build-units/d'
mutate memory/builds/tPlanOk/README.md '/gen:build-units/d'
hit "$(run)" "check 30 walked no build whose --plan returned a verdict, so a clean result here is about an empty population rather than about the corpus"

# ---- 30 branch 2: the VERDICT the walk exists to reach. Branch 1 above grades the walk's LIVENESS
# ---- and nothing else, so `check-arms.py` reports this branch as carrying no positive assertion and
# ---- the leg ships pinned-or-unarmed. BOTH halves of the mutation are load-bearing and neither reds
# ---- alone: a headerless spec beside a SPECCED unit still names a next, and a CLOSED unit with no
# ---- headerless spec prints no NOT A UNIT row. Only the conjunction is the blocker — a build told it
# ---- is finished by a verb that graded nothing on the file it is reporting.
# ---- The new spec is `git add`ed because `--plan` finds specs with `git ls-files`, so an untracked
# ---- file is invisible to it and this arm would assert against an unchanged listing.
reset_tree
mutate memory/builds/tPlanOk/spec/one.md 's/^\*\*Status:\*\* SPECCED /**Status:** CLOSED /'
printf '# cross-unit contracts

Ratified centrally. Not a unit spec, and carries no status header.
' > memory/builds/tPlanOk/spec/contracts.md
git add memory/builds/tPlanOk/spec/contracts.md
hit "$(run)" "a build's --plan reports NOT A UNIT rows AND claims every tracked spec is terminal, so a reader picking up work is told a build is finished by a verb that graded nothing on it: tPlanOk"

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
mutate $KIT_REL/SKILL.template.md '2i Invoke /session-kickoff before anything else.'
same "a blank KICKOFF_ENGINE turns check 18 off even on a transposed template" "$(run)" ""
reset_tree

# ---- check 16 arms D and E: the CONTRACT's two tables joined to the constants the driver enforces.
# ---- Both edits go to BOTH protocol copies, or check 15's parity fires and the arm would be
# ---- satisfied by a refusal that has nothing to do with the join it is testing.
# Through `mutate`, so a locator that stops matching after a document reword FAILS here instead of
# silently turning six arms into six no-ops that still read as tests.
pedit() { mutate $KIT_REL/PROTOCOL.template.md "$1"
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
reset_tree; pedit 's/^Ten kit-owned core items\./Six kit-owned core items./'
hit "$(run)" "the protocol's stated count of core Definition-of-Done items disagrees with the set the driver enforces, and that sentence sits directly above the table it miscounts: says '"

# ...and the sentence gone entirely. Absence is its own refusal for the reason every locator here
# has one: a summary nobody can find is a summary nobody can join.
reset_tree; pedit 's/^Ten kit-owned core items\. //'
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
frozen() { sed -i 's/^phase: .*/phase: ABORTED/' memory/builds/tRun/RUN.md
           sed -i 's/^phase: ABORTED/halt-code: fork-unresolvable\nphase: ABORTED/' memory/builds/tRun/RUN.md; }

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
mutate $KIT_REL/unattended.sh 's/^DIRECTIVES_CORE="minimal-prose:M10 /DIRECTIVES_CORE="retired-handle:M10 /'
frozen
miss "$(run)" "a parked waiver names a handle outside the effective directive set"

# ...LIVE control for move 2: the same tree with a RUNNING record must still red, or the exemption
# has switched the check off rather than scoped it.
reset_tree
printf '
2026-08-16T00:00:00Z waiver · item minimal-prose · reason owner took it
' >> memory/builds/tRun/RUN.md
mutate $KIT_REL/unattended.sh 's/^DIRECTIVES_CORE="minimal-prose:M10 /DIRECTIVES_CORE="retired-handle:M10 /'
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

# ---- THE README SIDE. The fixture must pair a LEGAL recorded mode with an ILLEGAL declared one,
# ---- because check 19 lives inside the `[ -n "$recmode" ]` guard: a record carrying no mode of its
# ---- own is outside this arm by construction, and that is correct for a legacy record.
# ---- The ORIGINAL note here said the reason was that a silent record never computes `dmode`. That
# ---- stopped being true at TOOL-dNarrowedAnchor-1, which hoisted the `dmode` derivation ABOVE the
# ---- guard so check 29 could reach every record. The requirement is unchanged; the reason for it
# ---- is now the guard alone, and a measured claim that has quietly gone false is worse than none. The agreement branch fires too on that pair, which is expected;
# ---- this arm asserts only its own message, because asserting the absence of the other would be
# ---- asserting a coincidence rather than a behaviour.
anchor_break add_bad_mode
sed -i '/^base: /a mode: slug' memory/builds/tRun/RUN.md
git add -A >/dev/null
hit "$(run)" "the build README at a run's recorded BASE declares an authorization mode outside the kit's published set, so the authorization names a discipline no kit member defines - legal values are"
anchor_restore

# ---- check 29: THE SECOND ANCHOR IS ADMISSIBLE PER MODE, and the bar has its own opinion of it.
# ---- The fixture is a base on the `unit` branch and NOT on the advertised default branch, which is
# ---- exactly what the second anchor produces — no stub, because the discriminator is an ancestry
# ---- test against a real advertisement and a fixture that faked it would assert this file's own
# ---- imagination. The README at that base carries no `authorized-by:` key, which reads as `slug`.
reset_tree
git commit -q --allow-empty -m unit-only --no-verify
sed -i "s|^base: .*|base: $(git rev-parse HEAD)|" memory/builds/tRun/RUN.md
git add -A >/dev/null
hit "$(run)" "a run's recorded BASE is not on the branch the remote calls its default, so it came from the second anchor, while the build README there declares a mode whose discipline is that the folder already existed: mode"

# ---- ...and the ADMITTED direction, which is the only thing separating this check from one that
# ---- reds every branch-anchored run. Same base, same anchor, one declared mode different.
reset_tree
sed -i '/^slug: /a authorized-by: prompt' memory/builds/tRun/README.md
git add -A >/dev/null && git commit -q -m prompt-mode --no-verify
sed -i "s|^base: .*|base: $(git rev-parse HEAD)|" memory/builds/tRun/RUN.md
git add -A >/dev/null
miss "$(run)" "a run's recorded BASE is not on the branch the remote calls its default, so it came from the second anchor, while the build README there declares a mode whose discipline is that the folder already existed: mode"

# ---- ...and CANNOT TELL stays silent. With no remote there is no advertised default-branch tip, so
# ---- the ancestry test has nothing to run against. A leg that reds a fleet on a network fault is
# ---- worse than one that waits for the next run, and without this arm the guard could red on
# ---- absence and every other arm here would still pass.
reset_tree; mkconf
git commit -q --allow-empty -m unit-only --no-verify
sed -i "s|^base: .*|base: $(git rev-parse HEAD)|" memory/builds/tRun/RUN.md
git add -A >/dev/null
git remote remove origin
miss "$(run)" "a run's recorded BASE is not on the branch the remote calls its default, so it came from the second anchor, while the build README there declares a mode whose discipline is that the folder already existed: mode"
git remote add origin "$ORIGIN"
reset_tree

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
reset_tree; mutate $KIT_REL/SKILL.template.md 's/| M12 | prompt | D9 |/| M12 | all | D9 |/'
hit "$(run)" "the directive scopes the registry declares are not the scopes the Skill's table shows, so the agent is told which runs a rule binds by a table that disagrees with the verb enforcing it:"

# G, the locator: the column REMOVED entirely. Without this the join compares two empty sets and is
# green - the vacuity shape every other join in this leg carries a guard for.
reset_tree; mutate $KIT_REL/SKILL.template.md 's/ | [a-z][a-z-]* | D\([0-9]\)/ | D\1/'
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
mutate $KIT_REL/SKILL.template.md 's/One `AskUserQuestion`, every gap/One ask, every gap/'
mutate $KIT_REL/SKILL.template.md 's/^6\. \*\*The kickoff hand-back\*\*/6. **The kickoff hand-back** AskUserQuestion/'
hit "$(run)" "the Skill's prompt path puts its owner turn AFTER the branch push, so the one question it is allowed to ask would be asked by a run that is already authorized and has nobody to answer it:"

# H, the PUSH after preflight. Preflight run first meets the refusal that nothing published
# authorizes the run - the exact refusal step 1 quotes so the agent does not have to diagnose it.
reset_tree
mutate $KIT_REL/SKILL.template.md 's/^4\. \*\*Commit, then PUSH THE BRANCH\.\*\*/4. **Commit.**/'
mutate $KIT_REL/SKILL.template.md 's/^6\. \*\*The kickoff hand-back\*\*/6. PUSH THE BRANCH now\n6. **The kickoff hand-back**/'
hit "$(run)" "the Skill's prompt path puts the branch push AFTER preflight, and preflight run first meets the refusal that nothing published authorizes the run:"

# H, the locator: a step no longer named at all. Without this the two order comparisons compare
# against empty strings and are green - the vacuity shape every join in this leg carries a guard for.
reset_tree
mutate $KIT_REL/SKILL.template.md 's/PUSH THE BRANCH/push the branch/'
out=$(run)
hit "$out" "the Skill's prompt path does not name all three of its ordered steps, so the order that makes the owner turn provably older than the authorization cannot be checked at all; it looks for AskUserQuestion, PUSH THE BRANCH and a bolded Preflight"
miss "$out" "puts its owner turn AFTER the branch push"

# H, a template with NO prompt path is legal and silent - this kit shipped without one, and an
# adopter on an older copy is not in error. Deleting the heading empties the slice.
reset_tree
mutate $KIT_REL/SKILL.template.md 's/^## Start a run from a PROMPT$/## Notes/'
miss "$(run)" "the Skill's prompt path does not name all three of its ordered steps"
reset_tree

# TOOL-aGroundedOrientation-2 - the ORIENTATION PROBES precede the build-folder write. Three arms,
# and the third is the one that earns the section slice: without it every criterion is satisfied by
# a whole-file grep, which the spec's own 4 rejects. The round-1 spec audit caught exactly that.
#
# J, the ORDERING violation: probes moved below the write, so the roster is authored before the
# probes that inform it.
reset_tree
mutate $KIT_REL/SKILL.template.md '/RUN the orientation probes/d'
mutate $KIT_REL/SKILL.template.md 's|^5\. \*\*Preflight\*\*|5. RUN the orientation probes\n5. **Preflight**|'
hit "$(run)" "the Skill's prompt path runs its orientation probes AFTER it writes the build folder, so the roster is authored and pushed before the probes that inform it, and correcting it costs a commit and a push:"

# J, the VACUITY case: the locator gone entirely. Without this arm the ordering comparison runs
# against an empty string and is GREEN - the same shape check 20's own third arm exists for.
reset_tree
mutate $KIT_REL/SKILL.template.md '/RUN the orientation probes/d'
out=$(run)
hit "$out" "the Skill's prompt path does not name both its orientation-probe step and its build-folder write, so the ordering that puts the probes before the roster cannot be checked at all and would compare against an empty string; it looks for 'RUN the orientation probes' and 'Write the build folder'"
miss "$out" "runs its orientation probes AFTER it writes the build folder"

# J, THE SECTION SLICE IS OBSERVABLE. The literal is deleted from the prompt path and re-added under
# a DIFFERENT heading. A file-wide locator finds it there and goes green; a section-scoped one still
# refuses. This arm is the only thing separating the shipped implementation from the one 4 rejects.
reset_tree
mutate $KIT_REL/SKILL.template.md '/RUN the orientation probes/d'
mutate $KIT_REL/SKILL.template.md 's|^## While it runs$|## While it runs\n\nRUN the orientation probes\n|'
hit "$(run)" "the Skill's prompt path does not name both its orientation-probe step and its build-folder write, so the ordering that puts the probes before the roster cannot be checked at all and would compare against an empty string; it looks for 'RUN the orientation probes' and 'Write the build folder'"
reset_tree

# TOOL-aPromptedMandate-6 fold — the three predicates the CLOSING REVIEW asked for. Each was measured
# firing against the live tree before its arm was written, which is the claim that failed for exactly
# one arm in this build and is why these say so explicitly.
#
# I, review H1: a floor BELOW the kit's own core count. This build SHIPPED that state - the bump to
# 13 was reverted by a `git checkout --` during an unrelated probe and arm C passed, because it only
# asked whether the count met the floor and never whether the floor met the kit.
reset_tree; mutate .unattended.conf 's/^DIRECTIVES_FLOOR=".*"$/DIRECTIVES_FLOOR="1"/'
hit "$(run)" "DIRECTIVES_FLOOR is declared below the kit's own core directive count, so the shrink-only pin is slack by construction and a deleted core handle would pass it:"

# I, review L2: a PROJECT-declared scope. Two carriers say the scope is kit-owned; nothing enforced
# it, because scope_of composes core PLUS extra and would have honoured this silently.
reset_tree; mutate .unattended.conf 's/^DIRECTIVES_EXTRA=""$/DIRECTIVES_EXTRA="house-style:M9:prompt"/'
hit "$(run)" "a project-declared directive carries a SCOPE, and the scope is kit-owned because a project-selectable one is a narrowing of the core wearing another name:"

# I, review L3: a pass kind outside the vocabulary. The both-ways join to the protocol cannot see it
# - both sides would agree on the same wrong token, which is the two-derived-values class.
reset_tree; mutate $KIT_REL/unattended.sh 's/^PHASES_PASSKIND="SPECCING /PHASES_PASSKIND="INVENTED /'
hit "$(run)" "a phase is published as a build-method pass kind and is not in the core vocabulary, so the contract names a position no run can ever occupy:"
reset_tree

# ---- the proposal-kind unit: check 26, the VERB SET across the documents that spell it. Each arm
# ---- removes ONE carrier and asserts THIS check speaks, because a leg that reds on everything arms
# ---- every branch and checks nothing.
reset_tree; mutate $KIT_REL/unattended.sh '/^#   unattended[.]sh --propose /d'
hit "$(run)" "a declared verb is absent from the driver's own header, and the usage text is RENDERED from that header, so the verb has no documented arguments anywhere a reader looks:"

# The protocol carrier. BOTH copies, so check 10's byte-parity arm does not fire alongside and leave
# two messages where the arm under test is one of them.
reset_tree
mutate $KIT_REL/PROTOCOL.template.md '/^- .--propose. — writes a PROPOSAL/d'
mutate memory/guides/UNATTENDED-PROTOCOL.md '/^- .--propose. — writes a PROPOSAL/d'
hit "$(run)" "a declared verb has no entry in the protocol's verb section, so the contract a run is measured against does not describe a verb that run can call:"

reset_tree; mutate $KIT_REL/SKILL.template.md 's|unattended[.]sh --propose <slug>|unattended.sh --nothing <slug>|'
hit "$(run)" "a declared verb is never invoked in the Skill an agent actually reads, so nothing an agent follows would ever call it:"

# LIVENESS. Every arm above iterates the declared set, so a set that fails to parse would run zero
# comparisons and report exactly the green a fully-wired driver reports.
reset_tree; mutate $KIT_REL/unattended.sh 's/^VERBS_SLUG=".*"$/VERBS_SLUG=""/'
hit "$(run)" "cannot read the driver's verb declarations, so every carrier below would be joined against an empty set and this check would pass over nothing:"

# ---- check 27: the parked-kind vocabulary against the call sites that write it, BOTH directions.
reset_tree; mutate $KIT_REL/unattended.sh 's/^  park "[$]rel" decision /  park "$rel" notakind /'
hit "$(run)" "a park() call site writes a kind the driver does not declare, and every reader of that region parses BY kind, so the row would be written and then counted by nothing:"

# The other direction, which is the half this kit has a recorded case of: DECISION was declared for
# as long as the contract had instructed a run to park one, and no verb wrote it.
reset_tree; mutate $KIT_REL/unattended.sh 's/^PARK_KINDS="decision /PARK_KINDS="invented decision /'
hit "$(run)" "the driver declares a parked kind that no park() call site ever writes, so the vocabulary names a row nothing can produce and the instruction to record one cannot be obeyed:"

reset_tree; mutate $KIT_REL/unattended.sh 's/^PARK_KINDS_OWED="decision /PARK_KINDS_OWED="ghost decision /'
hit "$(run)" "a kind the owner is owed an answer to is not in the declared parked-kind set, so the status split and the vocabulary disagree about which rows exist:"

reset_tree; mutate $KIT_REL/unattended.sh 's/^PARK_KINDS=".*"$/PARK_KINDS=""/'
hit "$(run)" "cannot read the parked-kind vocabulary or cannot find a single park() call site, so the membership join below would pass over an empty set - declared and found follow: ["
reset_tree

# ---- check 24: the MODE SET against the routing table, both directions, plus the two vacuity arms.
# ---- A join whose extraction returns nothing passes over nothing, which is the shape every other
# ---- arm in this file exists because of.
reset_tree; mutate $KIT_REL/SKILL.template.md 's/^## Which path$/## Something Else/'
hit "$(run)" "the Skill template carries no routing section, so a reader holding a build to start is never told which mode their path declares and every join below would have nothing to read; the heading this looks for is '## Which path'"

# The section present and carrying no readable mode cell. Backticks stripped from every mode, so the
# rows survive and the extraction does not — which is exactly the state a green would be a lie about.
reset_tree; mutate $KIT_REL/SKILL.template.md '/^## Which path$/,/^## Start a run$/s/| `\([a-z][a-z-]*\)` |/| \1 |/'
hit "$(run)" "the Skill's routing section carries no row naming an authorization mode, so both joins below would compare the driver's mode set against an empty one and pass by finding nothing"

# A declared mode with no row. The playbook row's cell is retyped as an existing mode, so the table
# stays well-formed and one mode simply stops being reachable — the failure that does not look like
# a failure.
reset_tree; mutate $KIT_REL/SKILL.template.md '/^## Which path$/,/^## Start a run$/s/| `recipe` |/| `slug` |/'
hit "$(run)" "the driver declares an authorization mode that no routing row names, so a build may legally declare a mode the Skill never tells anyone how to start: recipe against"

# ...and the reverse: a row for a mode the driver will refuse.
reset_tree; mutate $KIT_REL/SKILL.template.md '/^## Which path$/,/^## Start a run$/s/| `recipe` |/| `sonnet` |/'
hit "$(run)" "the Skill's routing table names an authorization mode the driver does not declare, so a reader following that row writes a build README preflight will refuse: sonnet against"

# ---- check 25: the content-scope rule stays a CHECK that denies its own machine half.
reset_tree; mutate $KIT_REL/SKILL.template.md 's/^## Start a PLAYBOOK run$/## Start a playbook run/'
hit "$(run)" "the Skill template carries no playbook-run section, so the mode the driver accepts has no start path an agent can follow:"

reset_tree; mutate $KIT_REL/SKILL.template.md 's/there is no machine half/it is enforced end to end/'
hit "$(run)" "the Skill's playbook-run path does not deny its own machine half, and a prose rule that reads like enforcement stops the reader looking for the gate that is not there:"

reset_tree; mutate $KIT_REL/SKILL.template.md 's/ordinary code build/perfectly ordinary build/'
hit "$(run)" "the Skill's playbook-run path does not say what this mode is NOT for, so the one refusal it is supposed to carry in prose is absent from the prose:"
reset_tree

# ---- check 28, ROUND-3 HALF: the answer arm now has a POSITIVE direction and asserts the parser's
# ---- EXIT STATUS. Before this it fed only the template's `[]` lines and asserted the output was
# ---- EMPTY — so a syntax error, a truncated extraction and a correct parse were ONE observation, and
# ---- gutting both parser bodies to a dead `printf` left the check silent and green while the census
# ---- went verified-over-unchecked. A dead harness must not be byte-indistinguishable from a live one.
# ----
# ---- Every arm replaces the WHOLE function body in BOTH copies, so the byte-compare stays satisfied
# ---- and the ANSWER assertions are what speak. Replacing only the first line left the pipeline's
# ---- continuation lines orphaned, which fired the rc branch instead of the one under test — caught
# ---- because `mutate` proves the edit landed and the arm still named the wrong branch.
gut_parser() { # fn-name · whole replacement body (one line)
  local f
  for f in $KIT_REL/check-playbook.sh $KIT_REL/unattended.sh; do
    mutate "$f" "/^$1() {/,/^}/ { /^$1() {/b; /^}/b; d; }"
    mutate "$f" "/^$1() {/a\\$2"
  done
}
# ---- ROUND 7's BLOCKER 1: A PARSER BROKEN ONLY FOR ONE INPUT SHAPE. `gut_parser` above breaks a
# ---- parser for EVERY input, which the fixed specimen loops catch on their own. This taints it for
# ---- the SHIPPED TEMPLATE's block alone - `step_selector` is in that block and in none of the
# ---- specimens - so the two single-line specimen batches stay aligned and pass while the two
# ---- template batches misalign. The batched harness used to answer every misaligned slot with the
# ---- batch's own rc, which is 0 when the batch RAN, and `(rc 0, "")` is the PASSING pair in both
# ---- template arms: the leg came out at rc 0 with zero output, in the loop that is the shipped
# ---- template's ONLY grader. A degraded-mode substitute must never be spelled with the value some
# ---- assertion reads as clean.
reset_tree
for _pf in $KIT_REL/check-playbook.sh $KIT_REL/unattended.sh; do
  mutate "$_pf" '/^declared_scalar() {/a\  case "$1" in *step_selector*) printf "EXTRA\\n" ;; esac'
done
hit "$(run)" "the batched parser harness got a reply it cannot split per specimen, so no assertion below is answering about the input it names - parser, specimens sent and answer lines received follow"
reset_tree

reset_tree; gut_parser declared_list "  printf ''"
hit "$(run)" "the extracted declared-list parser does not return the members of a NON-EMPTY declaration, which is the only direction that tells a working parser from one answering nothing - specimen, wanted and got follow: ["

# ...and the MULTI-LINE refusal itself: a parser that ANSWERS an unterminated array rather than
# refusing it is round 3's blocker, and this check used to certify that answer because empty was all
# it ever asserted.
reset_tree; mutate $KIT_REL/check-playbook.sh '/^declared_list() {/,/^}/ s|return 2|:|'
mutate $KIT_REL/unattended.sh     '/^declared_list() {/,/^}/ s|return 2|:|'
hit "$(run)" "the extracted declared-list parser does not REFUSE an array left open at the end of its line, so a legal multi-line declaration parses to the declared null and every piece carrying no verdict grades verified - specimen, exit status and answer follow: [k = ["

# ...and the COMMENTED spellings of the same array, which is round 4's blocker: the terminator test
# ran on the RAW line, so a `]` anywhere in a trailing comment satisfied it and the strip below then
# reduced the value to a bare `[`. The plain form still refused, which is exactly why the arm above
# and the fold that wrote it both passed. Moving the strip back after the `case` is the mutation.
reset_tree
mutate $KIT_REL/check-playbook.sh '/^declared_list() {/,/^}/ s|[#][.][*][$]|ZZZZ|'
mutate $KIT_REL/unattended.sh     '/^declared_list() {/,/^}/ s|[#][.][*][$]|ZZZZ|'
hit "$(run)" "the extracted declared-list parser does not REFUSE an array left open at the end of its line, so a legal multi-line declaration parses to the declared null and every piece carrying no verdict grades verified - specimen, exit status and answer follow: [k = [   # one per piece [see section 7]]"

# ---- ROUND 8's LOW 2: a SYNTAX error makes `bash -c` exit 2, the empty-reply branch faithfully
# ---- fills every slot with that 2, and 2 is exactly the value the multi-line REFUSAL arm
# ---- asserts - so a harness that ran nothing reported a correct refusal. It grades the harness
# ---- first now, and this is the arm for that.
reset_tree; gut_parser declared_list '  ((this is not shell'
hit "$(run)" "the multi-line refusal is graded against a harness that answered nothing, so a parser that will not parse would report the refusal this arm is looking for: specimen ["
reset_tree; gut_parser declared_list '  ((this is not shell'
hit "$(run)" "the extracted declared-list parser could not be executed, so every parse assertion in this check would read its silence as the declared null and pass - specimen and exit status follow: ["

reset_tree; gut_parser declared_scalar '  ((this is not shell'
hit "$(run)" "the extracted declared-scalar parser could not be executed over the shipped template's own line, and an unexecutable parser returns the empty string every assertion here reads as clean - key and exit status follow:"

# ---- the SCALAR sibling, byte-compared on the same terms as the list one. Round 3, HIGH 6: the list
# ---- parse was consolidated and compared while five scalar reads stayed ad-hoc, so this check
# ---- generalised the PARSE across list keys and the GATE across `*_checks` — two of the ten keys.
reset_tree; rm -f $KIT_REL/check-playbook.sh
hit "$(run)" "the declared-scalar parser is missing from one of the two scripts that inline it, so the comparison that keeps the copies one answer would pass over an empty pair - driver and leg follow:"

reset_tree; mutate $KIT_REL/check-playbook.sh '/^declared_scalar() {/a\  # a line only this copy carries'
hit "$(run)" "the two inlined copies of the declared-scalar parser have drifted, and a declaration parsed two ways is two answers to one question - they are copy-inlined because each kit script installs standalone, so this comparison is the only thing holding them together"

# ...and the ANSWER for the scalar keys: the COMMENT must not survive. Every key in the shipped block
# is a declared null of its own type, so a `#` in the parse is the leak signature — and it is the same
# signature for all ten keys rather than for the two the old pattern matched.
reset_tree
mutate $KIT_REL/check-playbook.sh '/^declared_scalar() {/,/^}/ s|[#][.][*][$]|ZZZZ|'
mutate $KIT_REL/unattended.sh     '/^declared_scalar() {/,/^}/ s|[#][.][*][$]|ZZZZ|'
hit "$(run)" "the shipped template's own declaration line parses with its COMMENT still attached, so an adopter who fills the template in place and keeps the comments gets that prose as the value - key and parse follow:"

# ...and the template half must have RUN. Without this both loops are green over a fence that yielded
# nothing, which the built-in specimens cannot distinguish from a fence that yielded everything. The
# keys are INDENTED rather than renamed: the population awk anchors at column 0, and a rename to
# `x_<key>` still matched it — the first attempt at this arm, caught by the arm staying green.
# ---- ONE LOOP AT A TIME, because that is the finding. Round 4, MEDIUM 6: both template loops shared
# ---- one counter, so the list half could go dark while the seven scalar keys satisfied the liveness
# ---- assertion, or the reverse. The all-keys indent below kills BOTH and cannot tell them apart, so
# ---- it is kept as the both-dark arm and each half now has its own.
reset_tree; mutate $KIT_REL/PLAYBOOK-TEMPLATE.template.md '/^```toml/,/^```$/ s|^\([a-z_][a-z_]*[[:space:]]*=\)|  \1|'
out=$(run)
hit "$out" "the shipped template's declaration block yielded no LIST key this check could parse, so the list half of the template assertion covered nothing and a parser that answers nothing for every array would pass it"
hit "$out" "the shipped template's declaration block yielded no SCALAR key this check could parse, so the scalar half of the template assertion covered nothing and a comment leak on every scalar key would pass it"

# ...the LIST half alone. Indenting only the `= [` lines leaves the seven scalar keys reachable, so a
# shared counter would still be satisfied and the check would stay green over a dead list loop.
reset_tree; mutate $KIT_REL/PLAYBOOK-TEMPLATE.template.md '/^```toml/,/^```$/ s|^\([a-z_][a-z_]*[[:space:]]*=[[:space:]]*\[\)|  \1|'
out=$(run)
hit "$out" "the shipped template's declaration block yielded no LIST key this check could parse, so the list half of the template assertion covered nothing and a parser that answers nothing for every array would pass it"
miss "$out" "the shipped template's declaration block yielded no SCALAR key this check could parse"

# ...and the SCALAR half alone, the mirror image. Indent every declaration that is NOT a list.
reset_tree; mutate $KIT_REL/PLAYBOOK-TEMPLATE.template.md '/^```toml/,/^```$/ { /^[a-z_][a-z_]*[[:space:]]*=[[:space:]]*\[/b; s|^\([a-z_][a-z_]*[[:space:]]*=\)|  \1|; }'
out=$(run)
hit "$out" "the shipped template's declaration block yielded no SCALAR key this check could parse, so the scalar half of the template assertion covered nothing and a comment leak on every scalar key would pass it"
miss "$out" "the shipped template's declaration block yielded no LIST key this check could parse"

# ---- THE SCALAR PARSER'S POSITIVE DIRECTION. Round 4, HIGH 5: the scalar half asserted only that no
# ---- `#` survived, so a parser answering NOTHING for every input scored correct — measured, gutting
# ---- it to an empty printf visited seven template keys with zero failures, and swapping its comment
# ---- strip for a delete-the-whole-line sed left the whole kit green. The list half got specimens in
# ---- the same commit; this one got none.
reset_tree; gut_parser declared_scalar "  printf ''"
hit "$(run)" "the extracted declared-scalar parser does not return the VALUE of a non-empty declaration, which is the only direction that tells a working parser from one answering nothing - a parser that empties every commented line passes every other assertion here. Specimen, wanted and got follow: ["

# ...and the subtler mutation the byte-compare cannot see, because two identically dead copies are
# still identical: a strip that DELETES every commented line rather than trimming the comment off it.
reset_tree
mutate $KIT_REL/check-playbook.sh '/^declared_scalar() {/,/^}/ s|s/\[\[:space:\]\]\[\[:space:\]\]\*#\.\*\$//|/#/d|'
mutate $KIT_REL/unattended.sh     '/^declared_scalar() {/,/^}/ s|s/\[\[:space:\]\]\[\[:space:\]\]\*#\.\*\$//|/#/d|'
hit "$(run)" "the extracted declared-scalar parser does not return the VALUE of a non-empty declaration, which is the only direction that tells a working parser from one answering nothing - a parser that empties every commented line passes every other assertion here. Specimen, wanted and got follow: ["

# ---- THE SOURCE POPULATION the three rules scan, derived from the kit directory rather than typed:
# ---- round 5 found 28c naming three files while the kit had seven. Its liveness is MEMBERSHIP rather
# ---- than a count - this checker and the adopter are themselves in that directory, so the population
# ---- is never empty and a count floor could be reached by no fixture.
reset_tree; rm -f $KIT_REL/check-playbook.sh
hit "$(run)" "the playbook leg is not in the source population these three rules scan, so the census reader - the one that dereferences the BASE blob every DoD verdict rests on - would go unexamined"

# ---- 28a, RE-ARMED AFTER ROUND 6 FOUND THE DISCARD ENUMERATION UNWINNABLE. The rule now enumerates
# ---- the COMPLIANT set, so the default is FAIL and a new spelling cannot widen the hole by existing.
# ---- Four spellings are staged, and the last two are the ones round 6 found walking past the
# ---- enumerate-the-discards version.
DISC='does not act on its exit status'
reset_tree; mutate $KIT_REL/unattended.sh 's@if ! _declared=$(declared_list "$_blob" set_checks); then@_declared=$(declared_list "$_blob" set_checks) || true; if false; then@'
hit "$(run)" "a parser that can REFUSE is called at a site that does not act on its exit status, so the refusal arrives as the empty string every caller reads as the declared null and the item it guards grades met with nothing recorded - parser, site and call follow: declared_list at"
reset_tree; mutate $KIT_REL/unattended.sh 's@if ! _declared=$(declared_list "$_blob" set_checks); then@_declared=$(declared_list "$_blob" set_checks) || return 0; if false; then@'
hit "$(run)" "$DISC"
reset_tree; mutate $KIT_REL/unattended.sh 's@if ! _declared=$(declared_list "$_blob" set_checks); then@_declared=$(declared_list "$_blob" set_checks) || _declared=""; if false; then@'
hit "$(run)" "$DISC"
reset_tree; mutate $KIT_REL/unattended.sh 's@if ! _declared=$(declared_list "$_blob" set_checks); then@_declared=$(declared_list "$_blob" set_checks); if false; then@'
hit "$(run)" "$DISC"

# ...and TWO CONTROLS, which are as load-bearing as the four breaks. A rule tightened until it reds on
# an honest caller has traded one false answer for another, and round 6 found exactly that: an honest
# refusal whose PROSE contained the word `true` matched the old discard arm.
reset_tree; mutate $KIT_REL/unattended.sh 's@if ! _declared=$(declared_list "$_blob" set_checks); then@_declared=$(declared_list "$_blob" set_checks) || { DOD_OUT=x; return 1; }; if false; then@'
miss "$(run)" "$DISC"
reset_tree; mutate $KIT_REL/unattended.sh 's@so this item would read the declared null@so this item would read what is not true, the declared null@'
miss "$(run)" "$DISC"

# ---- 28a's per-FILE branch, which is the masking direction the per-parser counter cannot see: one
# ---- file's call spelling drifts, the other file still has calls, and the parser-level count stays
# ---- healthy while a whole file goes unpoliced.
reset_tree; mutate $KIT_REL/check-playbook.sh 's@$(declared_list "@$( declared_list "@g'
hit "$(run)" "a file spells a call to a refusing parser in a shape this rule cannot enumerate, so its call sites go unpoliced while the rule reports nothing about them - parser and file follow"

# ---- 28a's per-PARSER liveness. Renaming the calls in BOTH files leaves the refusal in place and the
# ---- enumeration empty, which a hit count of zero cannot tell from compliance.
reset_tree
mutate $KIT_REL/check-playbook.sh 's@$(declared_list @$(declared_list_X @g'
mutate $KIT_REL/unattended.sh     's@$(declared_list @$(declared_list_X @g'
hit "$(run)" "a refusing parser has NO call site this rule can see, so it was asserted over an empty population and would stay green with every caller discarding the status - the enumeration pattern has stopped matching the way this kit calls this parser"

# ---- ...and the rule binding nothing at all, if the refusal itself is removed.
reset_tree
mutate $KIT_REL/check-playbook.sh '/^declared_list() {/,/^}/ s|return 2|:|'
mutate $KIT_REL/unattended.sh     '/^declared_list() {/,/^}/ s|return 2|:|'
hit "$(run)" "neither inlined parser carries a nonzero return any more, so the rule that a refusal must be read now binds nothing - either the refusal round 3 added was removed, in which case a legal multi-line declaration parses to the declared null again, or this check's derivation of which parsers can refuse has stopped matching them"

# ---- 28b. THE EXEMPTION ROW IS RETARGETED, never replaced with a synthetic: round 6's BLOCKER 1 was
# ---- a `key|file|literal` record destroyed by word-splitting, and the staged break that was supposed
# ---- to cover it substituted a value with no spaces in it, so it could not exhibit the split. The
# ---- table is newline-separated and read without splitting now, and this arm keeps the shipped
# ---- record's real spacing while pointing its key at one the template does not declare.
reset_tree; mutate $KIT_REL/check-unattended.sh 's@^legs|check-playbook.sh|@legsX|check-playbook.sh|@'
hit "$(run)" "the shipped template declares a key no inlined parser ever reads, so this check certifies a parse nothing consumes while whatever does consume it is unexamined - declare a parser read for it, or an exemption naming the reader that owns it"

# ...and the exemption going STALE, which is the failure mode an exemption list adds. Rewriting the
# reader it names takes its excuse with it.
reset_tree; mutate $KIT_REL/check-playbook.sh 's@    ent=$(printf .%s.n. "$body" | grep -oE@    ent=$(printf "%s" "$body" | grep -oE@'
hit "$(run)" "a key exemption names a reader whose signature is no longer in that file, so the key is unread by any parser AND unaccounted for by the exemption that excused it - key, file and missing literal follow"

# ...and a parser read that is COMMENTED OUT, which the positive half had no filter for until round 6.
reset_tree; mutate $KIT_REL/check-playbook.sh 's@^  cur=$(declared_scalar "$body" curated)@#  cur=$(declared_scalar "$body" curated)@'
hit "$(run)" "the shipped template declares a key no inlined parser ever reads, so this check certifies a parse nothing consumes while whatever does consume it is unexamined - declare a parser read for it, or an exemption naming the reader that owns it"

# ...and the NEGATIVE half: an ad-hoc read added BESIDE a parser read, never instead of it.
reset_tree; mutate $KIT_REL/check-playbook.sh 's@^  cur=$(declared_scalar "$body" curated)@  cur=$(declared_scalar "$body" curated); _x=$(printf "%s" "$body" | sed -n "s/^curated[[:space:]]*=//p")@'
hit "$(run)" "a declaration key the shipped template ships is read by an ad-hoc pipeline rather than by the parser this check certifies it through, so the answer this gate blesses and the answer its consumer actually gets are two answers to one question - key, site and read follow: curated at"

# ---- 28b's own liveness: a template whose fence yields no key to bind.
reset_tree; mutate $KIT_REL/PLAYBOOK-TEMPLATE.template.md '/^```toml/,/^```$/ s|^\([a-z_][a-z_]*[[:space:]]*=\)|  \1|'
hit "$(run)" "the shipped template yielded no declaration key to bind to a reader, so every key in it could be read by an ad-hoc pipeline and this rule would stay green over the empty set"

# ---- 28c. The WRAPPER's own pin first, which round 5's cut could not see at all.
# THE CONSTANT, not the wrapper line. The merged library spells the pin as `-c "$GIT_PIN_REPLACE"`,
# so a break aimed at the old literal no-ops - and it is the constant that check 28c now follows, so
# breaking it is both the reachable mutation and the one that exercises the indirection.
reset_tree; mutate $KIT_REL/lib-unattended.sh 's|^GIT_PIN_REPLACE=.*|GIT_PIN_REPLACE=core.useReplaceRefs=true|'
hit "$(run)" "the kit's own git wrapper is defined without the replace-ref pin, so every read routed through it is unpinned at once - and this kit routes its BASE-blob authorization read through it. Site follows"

# ...a bare unpinned read on a verb the first widening did not carry.
reset_tree; mutate $KIT_REL/unattended.sh 's@^export GIT_GRAFT_FILE=/dev/null@export GIT_GRAFT_FILE=/dev/null\n_probe() { git log -1 --format=%s "$1"; }@'
hit "$(run)" "a sha is dereferenced without the replace-ref pin, so a replace ref this run may install at any moment substitutes the committed bytes the census grades - and the run then supplies the playbook it is measured against, on an item no waiver can move. Site and read follow"

# ...and the same read with a trailing comment mentioning the WRAPPER, which is round 6's MEDIUM 2:
# classifying the whole LINE as wrapper-routed let prose excuse the code beside it.
reset_tree; mutate $KIT_REL/unattended.sh 's@^export GIT_GRAFT_FILE=/dev/null@export GIT_GRAFT_FILE=/dev/null\n_probe() { git cat-file -p "$1"; }  # routed through GIT show elsewhere@'
hit "$(run)" "a sha is dereferenced without the replace-ref pin, so a replace ref this run may install at any moment substitutes the committed bytes the census grades - and the run then supplies the playbook it is measured against, on an item no waiver can move. Site and read follow"

# ...and the raw arm reaching NO graded candidate, which must not look like a pass. Routing the kit's
# last bare dereference through the wrapper leaves only exempt candidates behind.
reset_tree; mutate $KIT_REL/check-playbook.sh 's@^GITSHOW() { git -c core.useReplaceRefs=false -c advice.graftFileDeprecated=false show@GITSHOW() { GIT show@'
hit "$(run)" "every bare git invocation in the kit was excused by the flags-only or for-each-ref property, so the raw arm graded nothing at all this run - it is reporting a clean nothing rather than a pass, and the two are not the same claim"

# ---- 28c's three liveness statements. The wrapper DEFINITION going missing, the bare spelling going
# ---- missing, and the wrapped spelling going missing are three different blindnesses, and round 5's
# ---- cut reported a clean nothing for two of them.
reset_tree; mutate $KIT_REL/lib-unattended.sh 's@^GIT() {@GITWRAP() {@'
hit "$(run)" "no git wrapper definition was found anywhere in this kit, so the GIT-spelled reads below are accepted on the strength of a definition this check cannot see - which is the same as not checking them"

# ---- the scalar SPECIMEN loop's exec branch, a different branch from the template loop's.
reset_tree; gut_parser declared_scalar '  ((this is not shell'
hit "$(run)" "the extracted declared-scalar parser could not be executed, so every parse assertion in this check would read its silence as the declared null and pass - specimen and exit status follow: ["

# ---- and the shipped template's own LIST declaration being refused by the parser that reads it.
reset_tree; mutate $KIT_REL/PLAYBOOK-TEMPLATE.template.md 's|^\([a-z_][a-z_]*[[:space:]]*\)= \[\]|\1= [|'
hit "$(run)" "the shipped template's own list declaration is REFUSED by the parser that reads it, so an adopter who copies the template inherits a declaration the driver cannot parse - and this check is the template's only grader, so nothing else would say so. Key and exit status follow"

reset_tree

# ---- check 28 (round-2 fold): the inlined parser is ONE answer in two files, and the answer is the
# ---- one an adopter gets. Both branches, because agreement and correctness are different claims and
# ---- this check makes both.
reset_tree; mutate $KIT_REL/check-playbook.sh '/^declared_list() {/,/^}/ s|; s/,/ /g||'
hit "$(run)" "the two inlined copies of the declared-list parser have drifted, and a declaration parsed two ways is two answers to one question - they are copy-inlined because each kit script installs standalone, so this comparison is the only thing holding them together"

# ...and the MISSING half, which is the branch every arm here would silently take if the scratch tree
# stopped carrying the leg. A pair check with one file present grades nothing.
reset_tree; rm -f $KIT_REL/check-playbook.sh
hit "$(run)" "the declared-list parser is missing from one of the two scripts that inline it, so the comparison that keeps the copies one answer would pass over an empty pair - driver and leg follow:"

# ...and the ANSWER, over the line the shipped template actually carries. Agreement alone is
# satisfied by two identical wrong copies, which is how the defect that produced this check shipped.
reset_tree; mutate $KIT_REL/PLAYBOOK-TEMPLATE.template.md 's/^piece_checks = \[\]/piece_checks = [oops]/'
hit "$(run)" "the shipped template's own declaration line does not parse to the declared null, so an adopter who copies the template verbatim inherits phantom check names and every piece grades unchecked - key and parse follow:"

reset_tree; rm -f $KIT_REL/PLAYBOOK-TEMPLATE.template.md
hit "$(run)" "the shipped playbook template is missing, so the parser cannot be run over the line every adopter actually copies and this check would grade agreement alone:"

reset_tree

# 175 -> 162 is a DELIBERATE lowering and owes its reason here. The 99-commit reconcile adopted
# main's check-8 redesign — the region holds no COPY, so there is nothing to keep fresh — which
# retired the staleness arms this branch had written against the old invariant. The
# frozen-versus-live PAIR survived and was rewritten against the new one; the anti-over-exemption
# arm did not, because main's exemption has the same over-wide scoping and narrowing it is a
# change the owner did not ask for. Filed as TOOL-cSettledDocket-11 rather than made silently.
# ---- check 22 (TOOL-dUnstalledConvoy-6): an AMENDMENT with no record. M3 now delegates this build's
# ---- own scope, so the failure mode moved from stalling to DRIFTING — a unit quietly retired with
# ---- nothing on the record saying so.
# ----
# ---- THE BASELINE MUST CARRY A ROSTER or there is nothing to compare against, and that is not a
# ---- fixture convenience: an EMPTY baseline is vacuously ACCUSATORY, because every unit the build
# ---- has would read as added. The shared `tRun` fixture is exactly that shape — a live phase from
# ---- its first commit — which is also the prompt-authorized shape, so these arms build their own
# ---- run whose baseline already names a unit, and the empty case is asserted separately as a SKIP.
URO='| [ARCH-tRos-1 — the first unit](spec/one.md) | OPEN | rev-1 | 2026-08-01 |'
UR7='| [ARCH-tRos-7 — a later unit](spec/seven.md) | OPEN | rev-1 | 2026-08-01 |'
# A unit that is WONTDO in the BASELINE region itself — the case the retire loop exempts.
UROW='| [ARCH-tRos-8 — retired before the run](spec/eight.md) | WONTDO | rev-1 | 2026-08-01 |'
UEND='<!-- /gen:build-units -->'
seed_ros() {
  reset_tree
  build tRos
  awk -v r="$URO" -v e="$UEND" '$0==e{print r} {print}' memory/builds/tRos/README.md > /tmp/ros.$$ \
    && mv /tmp/ros.$$ memory/builds/tRos/README.md
  sed -i "s/^witness: WITNESS$/witness: $(git rev-parse HEAD)/" memory/builds/tRos/RUN.md
  git add -A && git commit -q -m "tRos baseline" --no-verify
  # THE PINNED BASE IS THIS COMMIT, not the merge-base. `pinned_units` reads the units REGION at the
  # pinned commit, and the merge-base predates this fixture build folder entirely — so the RETIRE arm
  # would refuse rather than grade, and every arm below would be green because the arm found nothing.
  sed -i "s/^base: .*$/base: $(git rev-parse HEAD)/" memory/builds/tRos/RUN.md
  git add -A && git commit -q -m "tRos baseline pin" --no-verify
}
add_u7() {
  awk -v r="$UR7" -v e="$UEND" '$0==e{print r} {print}' memory/builds/tRos/README.md > /tmp/ros7.$$ \
    && mv /tmp/ros7.$$ memory/builds/tRos/README.md
}
rrow() { printf '\n2026-08-20T00:00:00Z rescope · item %s · reason %s\n' "$1" "$2" >> memory/builds/tRos/RUN.md; }

# an id present now and absent at the baseline, with NO rescope row, is the whole point of the check
seed_ros; add_u7
git add -A && git commit -q -m "a unit nobody recorded" --no-verify
hit "$(run)" "a unit is in the roster this run is executing and was not in the roster it entered BUILDING with, and no rescope row adds or supersedes into it, so the scope moved with nothing on the record saying so:"

# ...an `add` row naming it ACCOUNTS for it.
seed_ros; add_u7
rrow "add ARCH-tRos-7" "the build needed it"
git add -A && git commit -q -m recorded --no-verify
miss "$(run)" "check 24 FAILED"

# ...so does a SUPERSEDE row naming it as the SUCCESSOR, which is the case an add-only rule redded:
# a correct supersession leaves the successor present now and absent then, and the sibling verb
# refuses an `add` for an id the region already carries, so the run would have had no legal repair.
seed_ros; add_u7
rrow "supersede ARCH-tRos-1 -> ARCH-tRos-7" "the mechanism split"
git add -A && git commit -q -m superseded --no-verify
miss "$(run)" "check 24 FAILED"

# ...a SUPERSESSION whose successor never landed is a retirement wearing a better name.
seed_ros
rrow "supersede ARCH-tRos-1 -> ARCH-tRos-9" "never landed"
git add -A && git commit -q -m orphan --no-verify
hit "$(run)" "a rescope row supersedes into a successor the executing roster does not carry, so the replacement never landed and the row records a retirement wearing a better name:"

# ...a unit that goes WONTDO after the baseline owes a retire or a supersede.
seed_ros
sed -i 's#(spec/one.md) | OPEN |#(spec/one.md) | WONTDO |#' memory/builds/tRos/README.md
git add -A && git commit -q -m dropped --no-verify
hit "$(run)" "a unit is WONTDO now and was not at the BASE this run pinned, and no rescope row retires or supersedes it, so declared scope was dropped with nothing on the record saying so:"

# ...and the same transition WITH a retire row is accounted for.
seed_ros
sed -i 's#(spec/one.md) | OPEN |#(spec/one.md) | WONTDO |#' memory/builds/tRos/README.md
rrow "retire ARCH-tRos-1" "the probe cannot see this tree"
git add -A && git commit -q -m "retired on the record" --no-verify
miss "$(run)" "check 24 FAILED"

# ...and a unit that was ALREADY WONTDO AT THE BASELINE owes NOTHING, because nothing transitioned.
# This arm exists because TOOL-dUnstalledConvoy-33 broke exactly it: moving the baseline derivation
# into the library, the first draft returned BARE IDS, and this loop asks `id_rows … | grep -q
# "| WONTDO |"` — which no bare id can satisfy. The exemption went dead and every build carrying a
# unit retired BEFORE its run would have redded for a retirement nobody performed. It had no arm,
# because the four negatives in this block all asserted the absence of `check 22 FAILED`, a message
# this check cannot print.
reset_tree
build tRos
awk -v r="$UROW" -v e="$UEND" '$0==e{print r} {print}' memory/builds/tRos/README.md > /tmp/rosw.$$ \
  && mv /tmp/rosw.$$ memory/builds/tRos/README.md
sed -i "s/^witness: WITNESS$/witness: $(git rev-parse HEAD)/" memory/builds/tRos/RUN.md
git add -A && git commit -q -m "already retired before the run" --no-verify
# THE PIN IS THIS COMMIT, not the merge-base, and this arm is the one that most needs it: its whole
# subject is the exemption the RETIRE arm reads out of the PINNED roster. Against a merge-base that
# predates this fixture build folder, `pinned_units` REFUSES, the arm SKIPS, and `miss "check 24
# FAILED"` passes by absence - a rewritten predicate with no arm that can fail.
sed -i "s/^base: .*$/base: $(git rev-parse HEAD)/" memory/builds/tRos/RUN.md
git add -A && git commit -q -m "already retired, pinned" --no-verify
miss "$(run)" "check 24 FAILED"
# ITS LIVENESS HALF: the fixture must actually carry a WONTDO row, or the arm above is green because
# the loop selected nothing rather than because the exemption fired.
same "the already-WONTDO fixture carries the row the exemption reads" \
  "$(grep -c '| WONTDO |' memory/builds/tRos/README.md)" "1"

# ---- THE EMPTY BASELINE SKIPS rather than accusing, and the REPORT CHANNEL is what makes that
# ---- visible. A skip nobody can see is indistinguishable from coverage; the default run stays silent.
reset_tree
hit "$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)" "the baseline roster names no unit, so every unit this build has would read as added and the comparison would accuse rather than check"
out=$(run)
miss "$out" "check 24 skipped"
miss "$out" "check 24 FAILED"
reset_tree

# ---- check 23 (TOOL-dUnstalledConvoy-10): a DECLARED write set against what the pass COMMITTED.
# ---- The sibling verb records what a dispatched pass said it would write; this is the half that can
# ---- catch the declaration out, because the two artifacts are made by different acts at different
# ---- times. What it cannot buy is in its own header: both are authored by the run.
drow() {               # unit · declared paths — a dispatch row at the CURRENT HEAD
  printf '\n2026-08-21T00:00:00Z dispatch · item %s %s · reason %s\n' \
    "$(git rev-parse --short=8 HEAD)" "$1" "$2" >> memory/builds/tRun/RUN.md
  git add -A && git commit -q -m "declare $1" --no-verify
}

# a pass that commits INSIDE its declared set is clean
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
miss "$(run)" "unattended: check 23 —"

# ...and a pass that commits OUTSIDE it is the disjointness proof failing where it can be checked
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'b\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run)" "unattended: check 23 — a dispatched pass committed a path outside the set it declared before dispatch:"

# ---- THE WIDENING REPAIR, AND THE POST-HOC REWRITE THAT WEARS ITS CLOTHES (closing review F3/F4).
# ---- `--dispatch`'s widening supersedes an OPEN pass's row and parks the replacement AT THE SAME
# ---- ANCHOR, so a widened declaration is two rows under one key and the later binds. A widening
# ---- asked for AFTER the pass committed cannot reuse that anchor — the driver no longer finds the
# ---- row to supersede — so it lands under a new key and the original narrow row is still graded.
# ---- That is the ordering constraint, obtained by construction instead of by comparing timestamps.
drows() {              # unit · paths-for-row-1 · paths-for-row-2 — BOTH at the current anchor
  G=$(git rev-parse --short=8 HEAD)
  printf '\n2026-08-21T00:00:00Z dispatch · item %s %s · reason %s\n' "$G" "$1" "$2" >> memory/builds/tRun/RUN.md
  printf '2026-08-21T00:00:00Z dispatch · item %s %s · reason %s\n' "$G" "$1" "$3" >> memory/builds/tRun/RUN.md
  git add -A && git commit -q -m "declare $1" --no-verify
}

# A: the sanctioned repair. Widened at its own anchor, commits inside the widened set.
reset_tree
drows ARCH-tRun-1 "work/one.txt" "work/one.txt work/two.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'b\n' > work/two.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
miss "$(run)" "unattended: check 23 —"

# B: ...and the superseding row is still GRADED. Without this arm the fix above is indistinguishable
# from switching the check off for any pass that ever re-declared, which is a larger hole.
reset_tree
drows ARCH-tRun-1 "work/one.txt" "work/one.txt work/two.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run)" "unattended: check 23 — a dispatched pass committed a path outside the set it declared before dispatch:"

# C: THE POST-HOC REWRITE. Narrow row, the offending commit, THEN a widened row at a later anchor.
# The finding must survive: a declaration cannot be rewritten to cover a write already made. The
# first repair folded on the unit alone with no ordering constraint, and this case went GREEN.
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
drow ARCH-tRun-1 "work/one.txt work/stray.txt"
hit "$(run)" "unattended: check 23 — a dispatched pass committed a path outside the set it declared before dispatch:"

# D: SEVERAL PASSES OF ONE UNIT are legal — M6 defines five pass kinds and a unit may be dispatched
# once per kind. Each row governs its own pass. Folding them together graded pass one's commit
# against pass two's declaration and redded a correct run.
reset_tree
drow ARCH-tRun-1 "work/spec.txt"
mkdir -p work && printf 's\n' > work/spec.txt
git add -A && git commit -q -m "ARCH-tRun-1 authors its spec" --no-verify
drow ARCH-tRun-1 "work/build.txt"
printf 'b\n' > work/build.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its unit" --no-verify
miss "$(run)" "unattended: check 23 —"

# E: ...and the SECOND pass is graded too. The fold left it unlooked-at entirely, so a stray write in
# pass two exited 0 — the same fixture as D with one extra file, and the difference is the point.
reset_tree
drow ARCH-tRun-1 "work/spec.txt"
mkdir -p work && printf 's\n' > work/spec.txt
git add -A && git commit -q -m "ARCH-tRun-1 authors its spec" --no-verify
drow ARCH-tRun-1 "work/build.txt"
printf 'b\n' > work/build.txt && printf 'x\n' > work/STRAY.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its unit" --no-verify
hit "$(run)" "unattended: check 23 — a dispatched pass committed a path outside the set it declared before dispatch:"

# F: BOTH IDS IN ONE DISPATCH GROUP, which is the whole of this arm and is what the first two
# versions of it missed. The ambiguity loop only pairs siblings sharing an anchor, so a fixture that
# parks its two ids at different anchors never reaches the comparison it claims to pin — and reverting
# the anchoring left the whole suite green. `ARCH-tRun-1` is a prefix of `ARCH-tRun-10`, so under an
# unanchored `case ... in *"$dssunit"*` the `-10` commit reads as naming `-1` too and a correct run is
# refused for ambiguous attribution.
gdrows() {             # unit1 · paths1 · unit2 · paths2 — both rows at the CURRENT anchor
  G=$(git rev-parse --short=8 HEAD)
  printf '\n2026-08-21T00:00:00Z dispatch · item %s %s · reason %s\n' "$G" "$1" "$2" >> memory/builds/tRun/RUN.md
  printf '2026-08-21T00:00:00Z dispatch · item %s %s · reason %s\n' "$G" "$3" "$4" >> memory/builds/tRun/RUN.md
  git add -A && git commit -q -m "declare $1 and $3" --no-verify
}
reset_tree
gdrows ARCH-tRun-1 "work/one.txt" ARCH-tRun-10 "work/ten.txt"
mkdir -p work && printf 'b\n' > work/ten.txt
git add -A && git commit -q -m "ARCH-tRun-10 builds its lane" --no-verify
out=$(run)
miss "$out" "unattended: check 23 — one commit names two passes of the same dispatch group"
miss "$out" "unattended: check 23 —"
# ...and the positive control, so this arm cannot pass by finding nothing: ONE commit that genuinely
# names both passes IS ambiguous, and the refusal must fire.
reset_tree
gdrows ARCH-tRun-1 "work/one.txt" ARCH-tRun-2 "work/two.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'b\n' > work/two.txt
git add -A && git commit -q -m "ARCH-tRun-1 and ARCH-tRun-2 build together" --no-verify
hit "$(run)" "unattended: check 23 — one commit names two passes of the same dispatch group, so a subset test over it cannot say which pass wrote what and the attribution this comparison rests on is not available:"

# ...declaring MORE than you use is conservative and fine
reset_tree
drow ARCH-tRun-1 "work/one.txt work/two.txt"
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
miss "$(run)" "unattended: check 23 —"

# ---- THE NO-COMMIT CASE IS SPLIT. A pass that produced no change commits nothing and that is legal;
# ---- the same silence with the declared paths MOVED is the join being dodged.
reset_tree
drow ARCH-tRun-1 "work/one.txt"
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
hit "$out" "no commit names this pass and none of its declared paths moved, which is a pass that produced no change"
miss "$(run)" "unattended: check 23 —"

reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "a commit that names no pass at all" --no-verify
hit "$(run)" "unattended: check 23 — a declared path of a dispatched pass moved inside its window while no commit names that pass, so the declared work happened and the only join this check has was dodged:"

# ---- AMBIGUOUS ATTRIBUTION is refused rather than guessed: a subset test over a commit that could
# ---- belong to either of two passes proves nothing about either.
reset_tree
# BOTH ROWS AT ONE ANCHOR — that is what makes them one GROUP. Declaring them in two commits gives
# them two anchors and no sibling relation, which is a fixture that tests nothing.
G=$(git rev-parse --short=8 HEAD)
printf '
2026-08-21T00:00:00Z dispatch · item %s ARCH-tRun-1 · reason work/one.txt
' "$G" >> memory/builds/tRun/RUN.md
printf '
2026-08-21T00:00:00Z dispatch · item %s ARCH-tRun-2 · reason work/two.txt
' "$G" >> memory/builds/tRun/RUN.md
git add -A && git commit -q -m "declare both passes of one group" --no-verify
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "ARCH-tRun-1 and ARCH-tRun-2 in one commit" --no-verify
hit "$(run)" "unattended: check 23 — one commit names two passes of the same dispatch group, so a subset test over it cannot say which pass wrote what and the attribution this comparison rests on is not available:"

# ---- THE WINDOW IS THE FIRST COMMIT AND NOTHING AFTER IT. A pass's later review fold lands outside
# ---- its group by construction, and grading it would red an ordinary sequential fold with no
# ---- in-band repair — which is the defect this rule was rewritten to avoid.
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
printf 'folded\n' > work/later.txt
git add -A && git commit -q -m "ARCH-tRun-1 folds a review fix" --no-verify
miss "$(run)" "unattended: check 23 —"

# ---- THE SKIPS ANNOUNCE. A run with no declaration would otherwise be green over nothing, and the
# ---- default run must still print nothing.
reset_tree
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
hit "$out" "this run declared no concurrent dispatch, so there is no declaration to compare and a green verdict here would be coverage of nothing"
out=$(run)
miss "$out" "check 23 skipped"
miss "$out" "unattended: check 23 —"

reset_tree
printf '\n2026-08-21T00:00:00Z dispatch · item deadbeef ARCH-tRun-1 · reason work/one.txt\n' >> memory/builds/tRun/RUN.md
git add -A && git commit -q -m "a group anchor this clone does not carry" --no-verify
hit "$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)" "the recorded group anchor does not resolve in this clone, so the commit window cannot be opened"
reset_tree



# ---- THE SUBSET TEST GOES THROUGH `covers`, WHICH NORMALISES (spec 23 S8). Round 4 found this fix
# ---- shipped with nothing holding it: reverting `covers "$dsp" "$dsq"` to a bare
# ---- `case "$dsq" in "$dsp"|"$dsp"/*)` left both suites green at byte-identical counts. The
# ---- discriminator is a RECORD holding an un-normalised spelling, which `drow` can write and the
# ---- driver no longer can — the driver normalises before parking, so only a hand-written row
# ---- reaches this. That is exactly why the arm has to be here rather than driver-side.
reset_tree
drow ARCH-tRun-1 "work/sub/"
mkdir -p work/sub && printf 'a\n' > work/sub/x.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
miss "$(run)" "unattended: check 23 —"
# ...and the positive control on the same shape, so the arm cannot pass by the check being silent:
# a commit genuinely outside the declared lane still reports.
reset_tree
drow ARCH-tRun-1 "work/sub/"
mkdir -p work/sub && printf 'a\n' > work/sub/x.txt && printf 'b\n' > work/elsewhere.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run)" "unattended: check 23 — a dispatched pass committed a path outside"

# ---- THE COMPARISON NEVER FAILS THE LEG (spec 23 S1 / AC9). Both halves, because a check that is
# ---- silent AND exits 0 is indistinguishable from one that is working, and that is the shape this
# ---- whole mechanism spent four rounds in. The fixture is the one that produced a finding above.
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(run); rc=$?
same "check 23 reports without failing the leg, exit code" "$rc" "0"
hit  "$out" "unattended: check 23 — a dispatched pass committed a path outside"
miss "$out" "FAILED"

# ---- check 15 (TOOL-dUnstalledConvoy-2): the ancestry half now branches on the RECORDED anchor kind.
# ---- A `local` record is a claim about ONE clone — the protocol calls it a record of a merge rather
# ---- than an observation of one — so a clone that never had that merge says so instead of redding.
# ---- Without that, a run lands locally on one node and the same leg reds on every other node that
# ---- has not fast-forwarded its own default branch.
land_as() {            # anchor-kind · witness
  sed -i 's/^phase: .*/phase: LANDED/' memory/builds/tRun/RUN.md
  sed -i "s/^witness: .*/witness: $2/" memory/builds/tRun/RUN.md
  [ -n "$1" ] && printf 'landed-anchor: %s\n' "$1" >> memory/builds/tRun/RUN.md
  git add -A
}

# ---- ADV_NAME IS GRADED, and before this nothing distinguished the working parse from an empty one.
# ---- The local arm reaches `refs/heads/$ADV_NAME`; with ADV_NAME empty the test short-circuits, the
# ---- run takes the skip line, and every surrounding assertion still passes. The parse is the single
# ---- most consequential rewrite of the cross-build merge - main added it on an unbounded
# ---- substitution and it was grafted onto the bounded capture - so it gets an arm that fails when it
# ---- resolves to nothing.
reset_tree
land_as local "$(git rev-parse main)"
out=$(GOV_UNATTENDED_REPORT=1 run)
miss "$out" "a local-anchored LANDED names a witness this clone does not carry on its own default branch"

# ...and the CONTROL that proves the name came from the ADVERTISEMENT rather than coinciding with
# `main`. The origin's HEAD is repointed at a branch called `trunk`; a parse that hardcodes or guesses
# the default name passes the arm above and fails here.
reset_tree
git branch -f trunk main >/dev/null 2>&1
git push -q origin trunk 2>/dev/null
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/trunk
land_as local "$(git rev-parse trunk)"
out=$(GOV_UNATTENDED_REPORT=1 run)
miss "$out" "a local-anchored LANDED names a witness this clone does not carry on its own default branch"
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main
reset_tree

# a REMOTE record whose witness never reached the remote is the claim this half exists to refuse
reset_tree
land_as remote "$(git rev-parse HEAD)"
hit "$(run)" "a record claims LANDED with a witness that is not an ancestor of the anchor, so the work it says reached the remote is not on the branch the remote calls its default"

# ...the SAME witness under a LOCAL record, once the local default branch carries it, is the whole
# point of the two-anchor landing: green here, and red under the line above.
reset_tree
W=$(git rev-parse HEAD)
git branch -f main "$W"
land_as local "$W"
miss "$(run)" "a record claims LANDED with a witness that is not an ancestor of the anchor"
git branch -f main "$ANCHOR0"

# ...a LOCAL witness this clone carries on NEITHER branch is an announced SKIP, never a refusal. That
# is the cross-node case: the run-state file travels and a local ref does not.
reset_tree
land_as local "$(git rev-parse HEAD)"
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
hit "$out" "a local-anchored LANDED names a witness this clone does not carry on its own default branch, and a local anchor is a record of a merge rather than an observation of one, so this clone cannot judge it"
miss "$(run)" "a record claims LANDED with a witness that is not an ancestor of the anchor"

# ...an anchor kind outside the closed set is a refusal. Defaulting an unrecognised one would promote
# the record to whichever claim the reader assumed, which is the failure shape a value guard exists
# to prevent.
reset_tree
land_as sideways "$(git rev-parse HEAD)"
hit "$(run)" "a record claims LANDED with an anchor kind outside the closed set of remote and local, and defaulting an unrecognised one would promote the record to whichever claim the reader assumed:"

# ---- THE CUTOFF. Every LANDED record written before this unit carries no anchor kind and every one
# ---- of them is in fact remote-anchored, so a check that redded them would be unlandable by any run.
# ---- A record whose FIRST commit is at or after the declared date has no such excuse.
reset_tree
land_as "" "$(git rev-parse HEAD)"
printf '\nLANDED_ANCHOR_CUTOFF="1999-01-01"\n' >> .unattended.conf
git add -A
hit "$(run)" "a record claims LANDED and names no anchor kind while its own first commit is at or after the declared cutoff, so which history was meant to bless its witness cannot be read at all:"

# ...and the same record under a FUTURE cutoff is grandfathered, read as remote, and meets the
# ordinary ancestry refusal rather than the missing-kind one.
reset_tree
land_as "" "$(git rev-parse HEAD)"
printf '\nLANDED_ANCHOR_CUTOFF="2999-01-01"\n' >> .unattended.conf
git add -A
out=$(run)
miss "$out" "names no anchor kind while its own first commit is at or after the declared cutoff"
hit "$out" "a record claims LANDED with a witness that is not an ancestor of the anchor"
reset_tree

# RAISED 200 -> 243, then to 251 by TOOL-dUnstalledConvoy-2 by TOOL-dUnstalledConvoy-10. A floor well below the executed count is not a floor,
# it is a number: the sibling suite carried a sixty-arm slack and hid FIFTY stranded arms behind it in
# this same session. Pinned AT the count.
# FLOOR_ASSERTIONS — TOOL-cBriefedPilot-23. A shrink-only pin on the EXECUTED count. This build
# shipped nine arms stranded past an unconditional `exit`: the file still contained them, so a static
# grep saw nine and `check-arms.py` text-matched nine, and the only signal that moved was this total,
# which nothing compared to anything. Lower it in a reviewed diff or not at all.
# ---- Main sharded this suite while this branch added arms to it. The SHARDING is kept — it is
# ---- the structure — and the floors below are RE-MEASURED against the merged suite rather than
# ---- carried over, because a floor inherited across a merge is a number, not a floor.
fi   # ---- end REGION TWO ----------------------------------------------------------------------

# ---- RE-MEASURED AT THE dUnstalledConvoy MERGE, 2026-08-21, node d. Both sides of that merge
# ---- touched these constants and they disagreed about what a floor is for, so the reconciliation is
# ---- recorded here rather than left for the next reader to re-derive from whichever half they open.
# ----
# ---- MAIN's argument: discount the floor ~15% so it does not red on the first arm somebody
# ---- legitimately removes. THIS BRANCH's argument: a 338 floor under a 398 executed count is a
# ---- SIXTY-ARM SLACK, and that slack is exactly what let two whole blocks be appended past an
# ---- unconditional `exit` and never run, twice in one session, while the suite reported PASS and
# ---- `check-arms` text-matched every stranded arm.
# ----
# ---- Both are right and they pull opposite ways, so the headroom is ~3%: large enough that pruning
# ---- one arm is not a red, small enough that a stranded BLOCK is. The failure this pin exists to
# ---- catch is measured in tens of arms, never in ones.
# ----
# ---- MEASURED unsharded 271, shard one 84, shard two 187. 84 + 187 = 271 EXACTLY: this file has no prologue arms, so the shards partition the count with nothing paid twice.
# ---- RE-MEASURED at the playbook-mode merge, 2026-08-21, node d: unsharded 305, shard one 86, shard two 219, so the two regions share no prologue arm here. Main sharded these suites while this branch added arms to them; a floor inherited across a merge is a number and not a floor, so all three were taken again on the merged tree at the ~3% headroom this block argues for.
# ---- RE-MEASURED after the ROUND-3 fold, 2026-08-22, node d: unsharded 337, shard one 86, shard two 251,
# ---- and 86 + 251 = 337 EXACTLY, so this file still has no prologue arm. The three new arms are all in
# ---- region two, which is why shard one did not move. NOTE for whoever reads the line above: the pin it
# ---- sat under was 324, which no measurement line here accounts for — it was raised against a 334 that
# ---- nobody recorded. A floor whose measurement is missing is a number, so this line records all three.
# ---- RE-MEASURED after the ROUND-4 fold, 2026-08-22, node d: unsharded 379, shard one 86, shard two 293,
# ---- and 86 + 293 = 379, so this file still has no prologue arm. The twelve new arms cover the three
# ---- structural rules check 28 grew this round and the two liveness directions of each.
# ---- RE-MEASURED after the ROUND-5 fold, 2026-08-22, node d: unsharded 405, shard one 86, shard two 319,
# ---- and 86 + 319 = 405, so still no prologue arm. The twenty-six new arms are the three source rules
# ---- re-armed after round 5 found all three of them instance gates - eight staged breaks and, as much
# ---- to the point, two CONTROLS: a rule tightened until it reds on an honest caller has traded one
# ---- false answer for another, and only a control says which happened.
FLOOR_ASSERTIONS=392
# THE FLOOR IS MODE-SELECTED, or every shard leg reds forever against the unsharded floor. The
# per-shard floors carry the SAME proportional discount the unsharded pin does — 200 against a
# measured 230 is ~13 % of headroom — rather than pinning at 100 % of observation, which would red on
# the first arm anyone legitimately removes.
#
# MEASURED on node a: unsharded 230 assertions / 478 s, shard one 84 / 190 s, shard two 146 / 246 s.
# `84 + 146 = 230` EXACTLY: unlike the driver suite this file has no prologue arms, so its
# PROLOGUE_ARMS is 0 and the two shards partition the count with nothing paid twice. Balance is
# max(shard) 246 s over 478 s = 51.5 %, which is what the floor actually drops to.
#
# The two per-shard floors sum to exactly FLOOR_ASSERTIONS, which falls out of one discount applied
# to a clean partition. That is a coincidence of these numbers and NOT an invariant — do not write a
# check asserting it, because the driver suite's own three constants cannot satisfy the same
# relation, and asserting it over floors rather than executed counts is how the first draft of the
# sibling spec shipped an identity that was false by 60.
FLOOR_SHARD_1=83
FLOOR_SHARD_2=309
case "$SH_I" in
  1) FLOOR=$FLOOR_SHARD_1; MODE="shard 1/$SHARD_ARITY" ;;
  2) FLOOR=$FLOOR_SHARD_2; MODE="shard 2/$SHARD_ARITY" ;;
  *) FLOOR=$FLOOR_ASSERTIONS; MODE="unsharded" ;;
esac
[ "$n" -ge "$FLOOR" ] || { echo "FAIL executed $n assertions in $MODE against a floor of $FLOOR — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
# WHAT A GREEN SHARD LEG IS EVIDENCE ABOUT: its own region, and nothing else. Neither shard alone is
# this suite, and the whole-suite claim lives only in a run with no `--shard` argument.
#
# TWO CONTROLS LOSE THEIR MEANING WITHOUT FAILING when this file is split, and they are named here
# because no gate sees it: a "the tree is still clean after N mutations" control is a control only if
# those N mutations ran in the same process. Split away from them it degrades into a duplicate of the
# opening control — still green, and no longer evidence.
[ "$SH_I" = 0 ] || echo "  (this leg ran $MODE only; the other region was NOT exercised here)"
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
