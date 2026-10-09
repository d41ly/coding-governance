#!/usr/bin/env bash
# Fixture self-test for check-unattended.sh — every branch armed by a POSITIVE assertion naming its
# own failure text, and every RED arm paired with a GREEN control. Silence proves nothing on its
# own: a check that was never reached is silent for the same reason a passing one is.
#
#   bash <prefix>/unattended/check-unattended.test.sh    # "PASS (…assertions)" + exit 0 = good
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
HERE="$(cd "$(dirname "$0")" && pwd)"
# THIS SUITE'S OWN DIRECTORY, DERIVED (TOOL-aRepatriatedFork-18 S2). It ships beside its gate, so a
# spelled default resolved only at gov's prefix and nothing ever set it (TOOL-dRetiredFork-39). The
# block is byte-identical to the canonical copy named on its marker line, gated by the parity table
# in the resolve-python self-test.
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "FAIL this suite is not inside a git repository"; exit 2; }

# ---- THE SHARD CONTRACT — ADOPTED, not reinvented (TOOL-aShardedFloor-3) -------------------------
# The contract is TOOL-aShardedFloor-2's and its reasoning lives in the head of
# <prefix>/unattended/unattended.test.sh: one file and guarded contiguous regions rather than a
# physical split (which `check-arms.py`'s one-gate-one-sibling map and the armed-branch pin refuse),
# the flag PARSED rather than position-read, and the refusal before any scratch dir exists.
#
# EIGHT regions since TOOL-aBatchedArm-3 (two before it), cut ONLY at `reset_tree`-led block edges
# and balanced against per-shard SERIAL readings, which the budget rows carry. What differs from the
# driver suite is the seams and the floors. Three carriers can break at a cut and each is handled
# once: shell VARIABLES (none cross a boundary — scanned per boundary, recorded in the build),
# FUNCTIONS (every region-defined helper is HOISTED; the block below `anchor_restore` names the
# population and its derivation) and REFS, which the nine re-cut seams restore by `anchor_restore`
# and then read with `read_topo s1` to `s9` as their instrument, the eight region starts with
# `read_topo 2` to `8`, and `run_landed_replay` where the unsharded run's topology differs from a
# fresh start. `check_helpers_hoisted` is the standing check on the hoist rule (TOOL-aGraftedHelix-36).
SHARD_ARITY=8
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
# ---- THE FOURTH HELPER, for a BATCHED block (TOOL-aBatchedArm-1 S1). A group is one `reset_tree`,
# ---- its mutations in sequence, ONE `out=$(GOV_UNATTENDED_REPORT=1 run)`, one `check_emitted`, then the
# ---- group's `hit "$out" …` lines exactly as they were when each had a tree of its own. It grades
# ---- the SET of failure SIGNATURES the run emitted against the set the group expects: `$1` is
# ---- `|`-separated, each entry the interpolation-stripped signature of one `fail N "…"` branch as
# ---- `check-arms.py` derives it (the longest literal run between interpolations, trailing `:" `
# ---- trimmed) — the only per-branch identifier the checker emits; a check NUMBER is not one, since
# ---- 6 of 29 carry a single branch. No signature contains `|` (measured over all 178 at 46b12b93).
# ---- It REDS when an expected signature is on no `UNATTENDED check N FAILED` line, when such a
# ---- line carries no expected signature (a break fired a branch nobody asserted), or when a skip
# ---- line on the report channel names a check number one of the explained lines carries — a check
# ---- pushed onto a skip path by a group-mate prints nothing on the default channel and is
# ---- byte-identical to one that stayed silent, which is why a group runs with the channel ON. The
# ---- skip lines are then STRIPPED from the global `out`, so the verbatim `hit` lines below read
# ---- what an unbatched arm read. The failure prints the expected set, the observed misses and
# ---- extras, and every skip line seen. ONE assertion, whatever the set's size.
# ---- WHAT IT DOES NOT CHECK: that a branch fired for the reason its arm intended — a signature on
# ---- the line is all it sees, and the per-branch `hit` lines stay for that. Nor can it tell a
# ---- `miss` control's branch dark from silent, which is why no `miss` and no `same` is ever in a
# ---- group (TOOL-dScriptedRepeat-15 S3, taken flat). And it cannot know a break's COMPLETE
# ---- emission: an expected set derived from the arms alone is incomplete wherever a break fires
# ---- a branch no arm names — three such blocks are proven in the build record — so a group's set
# ---- is written from an OBSERVED run or not at all.
# ---- THE SENTINEL (owner ruling 2026-09-14, spec rev-6). Every group the rev-6 pass converted
# ---- carries `"?"` until the build's final gate pass pastes its set from the OBSERVED run, with
# ---- the run named beside the group. `"?"` is refused BY NAME — one FAIL line per group, so the
# ---- converted file cannot pass in the window — and `out` is still stripped, so the `hit` lines
# ---- below it read exactly what they will read once the set exists. AC3's recipe counts these.
# ---- TWO REPORT SHAPES ARE NOT SKIPS, and dDerivedDocket put both on every run over this fixture,
# ---- so read as skips each turned a group's own coverage into a dark branch. A COVERAGE COUNT,
# ---- `check <n> byte-compared|compared|graded <count> …` - check 10's pair count is one
# ---- (TOOL-dDerivedDocket-20 S4, AC4) - says what a check graded; a half it could not grade is a
# ---- failure line or a skip line of its own, which the dark scan still reads. And check 26's
# ---- SUITE-ABSENT skip (TOOL-dDerivedDocket-30 S6, AC8), printed on every run because this fixture
# ---- carries neither suite, as no adopter tree does, so no group-mate can have pushed check 26
# ---- onto it. WHAT THIS DOES NOT CHECK: a count reading zero, which is its check's own liveness.
CE_STANDING='^unattended-report: check [0-9]+ (byte-compared|compared|graded) [0-9]+ |^unattended-report: check 26 skipped for .*/(check-)?unattended[.]test[.]sh .* this tree does not carry the suite, which is withheld from every adopter install'
check_emitted() { # signatures · output
  local _s _l _num _ok _exp _miss="" _extra="" _dark="" _nums=" " _skips
  n=$((n+1))
  out=$(grep -v '^unattended-report: ' <<<"$2" || true)   # every path below leaves `out` stripped
  if [ "$1" = "?" ]; then
    # ---- the OBSERVED set follows the refusal, indented so `grep '^FAIL'` does not count it: the
    # ---- final pass pastes a group's set from these lines, and the caller's line is the join.
    echo "FAIL check_emitted: expected set not yet observed — owed at the final pass · call at line ${BASH_LINENO[0]}"; st=1
    grep '^UNATTENDED check [0-9]* FAILED ' <<<"$2" | sed 's/^/    observed: /'; return
  fi
  # FED FROM FILES. The four loops below read `$_exp`, `$2` and `$_skips`, each assigned from a
  # command substitution, which is the shape the shell-hygiene leg gates -- such a loop can read
  # until an EOF that never arrives. The registry carrying the pre-existing sites is shrink-only,
  # so a new one cannot be declared: the texts go to a scratch dir and the loops read those.
  local _ced; _ced=$(mktemp -d) || { echo "FAIL check_emitted: no scratch dir"; st=1; return; }
  _exp=$(printf '%s\n' "$1" | tr '|' '\n' | sed 's/^[[:space:]]*//; s/[[:space:]]*$//' | grep -v '^$' || true)
  printf '%s\n' "$_exp" > "$_ced/exp"; printf '%s\n' "$2" > "$_ced/out"
  [ -n "$_exp" ] || { echo "FAIL check_emitted: no signature given, so the set it would grade is empty and every run would satisfy it"; st=1; rm -rf "$_ced"; return; }
  while IFS= read -r _s; do
    grep -qF -- "$_s" <<<"$2" || _miss="$_miss [$_s]"
  done < "$_ced/exp"
  while IFS= read -r _l; do
    case "$_l" in "UNATTENDED check "*" FAILED "*) ;; *) continue ;; esac
    _num=${_l#UNATTENDED check }; _num=${_num%% *}; _ok=0
    while IFS= read -r _s; do
      case "$_l" in *"$_s"*) _ok=1; _nums="$_nums$_num "; break ;; esac
    done < "$_ced/exp"
    [ "$_ok" = 1 ] || _extra="$_extra [$_l]"
  done < "$_ced/out"
  _skips=$(grep '^unattended-report: ' <<<"$2" || true)
  printf '%s\n' "$_skips" > "$_ced/skips"
  while IFS= read -r _l; do
    [ -n "$_l" ] || continue
    [[ $_l =~ $CE_STANDING ]] && continue
    _num=${_l#*check }; _num=${_num%%[!0-9]*}
    [ -n "$_num" ] || continue
    case "$_nums" in *" $_num "*) _dark="$_dark [$_l]" ;; esac
  done < "$_ced/skips"
  rm -rf "$_ced"
  [ -z "$_miss$_extra$_dark" ] \
    || { echo "FAIL check_emitted: expected [$(printf '%s' "$_exp" | tr '\n' '|')] · missing:$_miss · unexplained:$_extra · dark:$_dark · skips: $_skips"; st=1; }
}

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
cp "$HERE/VERBS.template.md" $KIT_REL/
cp "$HERE/PROTOCOL.template.md" memory/guides/UNATTENDED-PROTOCOL.md
# THE VERB CARRIER, BOTH HALVES. Seeded for the same reason the protocol pair is: check 10 now
# iterates two pairs and check 26 reads this carrier ALONE, so a fixture missing either half
# models a broken install and every arm below grades that refusal instead of its own subject.
cp "$HERE/VERBS.template.md" memory/guides/UNATTENDED-VERBS.md
# THE ASK GUIDE, BOTH HALVES (TOOL-dDerivedDocket-20 S4), for the verb carrier's reason: check 10
# iterates a third pair, and a fixture missing either half grades that refusal in every arm below.
cp "$HERE/ASKS.template.md" $KIT_REL/
cp "$HERE/ASKS.template.md" memory/guides/UNATTENDED-ASKS.md
# THE REPAIR POINTER'S TARGET (closing review round 1 M5). `derive_index_repair` probes for the
# memory-tree kit's generator beside this kit, and a fixture holding only the unattended kit made it
# print its not-found text, so check 21's arm asserted a literal the leg never produced here. The
# probe tests only that the FILE exists, so a stub at the sibling home is the whole dependency.
MT_REL=$(dirname "$KIT_REL")/memory-tree; MT_REL=${MT_REL#./}
mkdir -p "$MT_REL" && printf '# fixture stub: the probe target of derive_index_repair\n' > "$MT_REL/gen_build_index.py"
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
HOLD_CODES_EXTRA=""
HOLD_FLOOR="${HDFLOOR_OVERRIDE:-$HOLD_FLOOR_DERIVED}"
# THE DURABLE RESTART CARRIER, DECLARED (TOOL-dDerivedDocket-5 S1). RESUME_SCHEDULE is absent, so it
# defaults to on, and check 46 requires the pair while it is on: without these two lines every run
# over this fixture printed two check 46 FAILED lines, which every batched group read as a branch
# nobody asserted. Spelled apart from KEEPALIVE_CREATE, or check 46's carrier refusal fires instead.
# The driver suite's fixture declares the same pair for the same reason.
RESUME_SCHEDULE_CREATE="TheScheduleCreate"
RESUME_SCHEDULE_DELETE="TheScheduleDelete"
# DECLARED HERE, AND THAT IS A FIXTURE FIX RATHER THAN A PRODUCT ONE (TOOL-dFoldedVerdict-2 fallout).
# The key was absent from this block, so the DEFAULT fixture took check 2's blank branch and the leg
# announced it on stdout once per run. That announcement is CORRECT for a blank cutoff and wrong for
# the tree every other arm treats as conforming: this suite's opening control asserts that a
# conforming tree prints NOTHING, so it and every absence assertion below it were graded against a
# tree that already talks.
#
# 2099-01-01, not a real date and not today's. A cutoff AHEAD of every fixture record forces the
# pre-cutoff id-delta proxy, which is byte-for-byte what the blank branch did, so declaring the key
# moves no other arm's verdict. A date behind the records would silently switch ~290 arms onto the
# recorded-disposition predicate instead, which is a different fixture wearing the same name.
#
# THE BLANK BRANCH IS STILL ARMED. The arm that wants it now STRIPS this key rather than relying on
# its absence here - see the blank-cutoff arm in region one. Leaving one arm to depend on a hole in
# the shared fixture is what made this a suite-wide red rather than one arm's problem.
#
# WHAT THIS DOES NOT FIX: an adopter who copies .unattended.conf.example verbatim gets the key BLANK
# and therefore the same announcement on every bar. Whether it should fire there is dFoldedVerdict's
# question, not this fixture's, and it is untouched.
DISPOSITION_CUTOFF="2099-01-01"
UNDECLARED_WRITE_BUDGET="${UWB_OVERRIDE:-0}"
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
HOLD_FLOOR_DERIVED="$(grep '^HOLD_CODES_CORE=' "$HERE/unattended.sh" | sed 's/^HOLD_CODES_CORE="//; s/"$//' | wc -w)"
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
# An identity on the BARE repo too: check 9's ghost-tip arm runs `commit-tree` INSIDE it, and a bare
# repo inherits nothing from the worktree, so on a host with no global identity $ghost comes back
# empty. The driver test carries the same two lines for the same arm shape.
git --git-dir="$ORIGIN" config user.email t@t.test
git --git-dir="$ORIGIN" config user.name t
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
#
# BOTH STORES, not just the clone (TOOL-aBatchedArm-3 S5). Two arms leave HEADS behind that a fresh
# start does not carry: check 9's `ahead` is pushed to the ORIGIN, and the LANDED control's `trunk`
# is created locally and then pushed, so it leaks into both. The clone-side batch below now sweeps
# `refs/heads/` too, keeping only the two heads the fixture is born with; the origin is a separate
# store this batch cannot reach, so its half is ONE more `update-ref --stdin` against the bare repo.
# The set is DERIVED, not guessed - every `git push`/`git branch` in this file whose target is not
# `main` or `unit` - and re-deriving it is one grep when an arm grows a new head: a `delete` of a
# ref that does not exist is a silent no-op, so a stale entry costs nothing and a MISSING one leaks.
# MUT counts `reset_tree`-led cycles IN THIS PROCESS (TOOL-aBatchedArm-3 S6). A control that says
# "still clean after N mutations" is evidence only if those N cycles ran here; cut into another
# shard it degrades into a copy of the opening control, still green. Its block declares the count
# it expects and the control asserts the counter against it BEFORE running the leg, so separating
# the two is a red rather than a silent loss of meaning. Both start at 0 so a control that lands
# in a shard whose block did not run compares 0 against what that shard did run, and reds.
MUT=0; MUT_EXPECTED=0
reset_tree() {
  MUT=$((MUT+1))
  git reset -q --hard "$PRISTINE"; git clean -qfd
  { git for-each-ref --format='delete %(refname)' refs/remotes/ refs/replace/ refs/heads/ \
      | grep -v -e ' refs/remotes/origin/main$' -e ' refs/heads/main$' -e ' refs/heads/unit$'
    printf 'update refs/remotes/origin/main %s\n' "$ANCHOR0"
  } | git update-ref --stdin --no-deref
  printf 'delete refs/heads/ahead\ndelete refs/heads/trunk\n' | git --git-dir="$ORIGIN" update-ref --stdin
}
run() { bash "$SCRIPT" 2>&1; }
# THE WHOLE-OUTPUT GREEN CONTROLS GRADE "NOTHING ELSE PRINTED", NOT "NOTHING PRINTED". Checks 45 and
# 46 announce the effective LANDER_MODE, RESUME_SCHEDULE and SELFTESTS_OWED_PATHS on the DEFAULT
# channel by design (the checker's header, THREE), so a control comparing the whole output to empty
# reds on every tree once those checks exist. This removes exactly those announcement shapes and
# nothing else; the lm_dir arms assert the announcements themselves, so the pair grades both halves.
# Check 23's FLEET line is the same kind (header exception TWO: it reports and never fails the leg),
# printed on every run that grades a pass, so it is removed too (TOOL-aGraftedHelix-34 S4); the arms
# that are about it read it off the whole output. The cross-component suite carries a byte-identical
# copy, and a new announcement shape is owed to both.
remove_announcements() { # leg output -> the same output without the check-23/45/46 announcement lines
  printf '%s\n' "$1" | grep -v -E '^unattended: (LANDER_MODE [^ ]+ \((declared|defaulted)\) — |RESUME_SCHEDULE [^ ]+ \((declared|defaulted)\) — |RESUME_SCHEDULE is off — |SELFTESTS_OWED_PATHS is blank — |SELFTESTS_OWED_PATHS entry [^ ]+ — resolves to tracked paths$|check 23 fleet — )'
}
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
# TOOL-aHomedAnchor-2 - the opt-in the leg reads off the remote's default branch, appended to a conf.
add_local_scope() { printf 'ANCHOR_SCOPE="local"\n' >> .unattended.conf; }

# ---- THE HOIST SET (TOOL-aBatchedArm-3 S1). Every helper a region used to define beside its first
# ---- caller lives here instead, because a function defined in one shard and called from another
# ---- is a command-not-found that no gate sees until the shard runs. The population is DERIVED,
# ---- not typed from memory: every `name() {` definition between the first `in_shard` line and the
# ---- floor line — 27 of them at BASE 0422ea2e, 2026-09-13 — and ALL of them moved, whether or not a
# ---- cut separates one from a caller today, so a re-balance can never strand one. Bodies are
# ---- byte-identical to their old positions and keep their order; the comment that explained each
# ---- stayed with the arm that uses it. A helper that READS a variable (`WP`, `_c31_skill`, `URO`,
# ---- `UEND`) still reads one the calling block sets first — a definition crossing a cut is safe,
# ---- its caller's block crossing one is what the variable scan is for.
dispconf() { mkconf; sed -i '/^DISPOSITION_CUTOFF=/d' .unattended.conf; printf 'DISPOSITION_CUTOFF="%s"\n' "$1" >> .unattended.conf; }
mkdisp() { # base-region-rows · head-region-rows · run rows
  mkdir -p memory/builds/tDisp
  printf '# tDisp\n\n<!-- gen:build-units -->\n| Unit | Status |\n|---|---|\n%b<!-- /gen:build-units -->\n' "$1" > memory/builds/tDisp/README.md
  git add -A >/dev/null 2>&1 && git -c commit.gpgsign=false commit -q -m dispbase --no-verify
  DISPBASE=$(git rev-parse HEAD)
  printf '# tDisp\n\n<!-- gen:build-units -->\n| Unit | Status |\n|---|---|\n%b<!-- /gen:build-units -->\n' "$2" > memory/builds/tDisp/README.md
  printf '# tDisp\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nphase: RUNNING\nwitness: abc\nbase: %s\n\n%b' "$DISPBASE" "$3" > memory/builds/tDisp/RUN.md
  # COMMITTED, not merely staged. The cutoff grades the record's own FIRST-COMMIT date; a staged
  # record has none, and an undated record is graded regardless of the cutoff — so a staged fixture
  # made the 2099 and 2000 arms produce byte-identical output and the grandfathering arm proved
  # nothing at all. GIT_COMMITTER_DATE pins the date so neither arm depends on the day it runs.
  # DISPDATE overrides it for the arms that grade a record against the driver's FOLD_CUTOFF, which
  # the default of 2026-09-01 predates: a fold-beside-blockers row at that date is the grandfathered
  # population, and the red arm has to commit AT the cutoff to be graded by the rule.
  git add -A >/dev/null 2>&1
  GIT_COMMITTER_DATE="${DISPDATE:-2026-09-01T12:00:00 +0000}" git -c commit.gpgsign=false commit -q -m disprun --no-verify >/dev/null 2>&1
}
drop_readme()  { rm -f memory/builds/tRun/README.md; }
break_fm()     { printf 'not front matter at all\n\n# tRun\n' > memory/builds/tRun/README.md; }
break_slug()   { sed -i 's|^slug: .*|slug: someoneElse|' memory/builds/tRun/README.md; }
noop_break() { :; }
_bm_sections() { printf '# method

## M2

## M3

## M4

## M5

## M6
%s
## M7

## M8

## M9

## M10

## M12
' "$1"; }
wreset() { git reset -q --hard "$WP"; git clean -qfd; }
drive() { bash "$KIT_REL"/unattended.sh "$@" 2>&1; }
wline() { grep -F ' waiver · item ' memory/builds/tWaive/RUN.md; }
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
_bm31() { # [route path]; with no argument the section names no route at all
  local body
  body=$(printf '\n`parallel-when-disjoint` `passes-committed` `passes-harnessed`')
  [ $# -gt 0 ] && body=$(printf '%s — the route is `%s`' "$body" "$1")
  _bm_sections "$body" > memory/guides/BUILD-METHOD.md
}
_mkskill() { # <route path>...; the Skill's harness bullet and nothing else
  mkdir -p "$(dirname "$_c31_skill")"
  { printf 'the harness is:\n'; for _s in "$@"; do printf -- '- `%s`\n' "$_s"; done; } > "$_c31_skill"
}
pedit() { mutate $KIT_REL/PROTOCOL.template.md "$1"
          mutate memory/guides/UNATTENDED-PROTOCOL.md "$1"; }
frozen() { sed -i 's/^phase: .*/phase: ABORTED/' memory/builds/tRun/RUN.md
           sed -i 's/^phase: ABORTED/halt-code: fork-unresolvable\nphase: ABORTED/' memory/builds/tRun/RUN.md; }
add_mode() { sed -i '/^slug: /a authorized-by: prompt' memory/builds/tRun/README.md; }
add_bad_mode() { sed -i '/^slug: /a authorized-by: slugg' memory/builds/tRun/README.md; }
add_recipe_seam() { sed -i '/^slug: /a authorized-by: recipe\nplaybook: content/pb.md\npieces: 3' memory/builds/tRun/README.md; }
add_recipe_mode() { sed -i '/^slug: /a authorized-by: recipe' memory/builds/tRun/README.md; }
gut_parser() { # fn-name · whole replacement body (one line)
  local f
  for f in $KIT_REL/check-playbook.sh $KIT_REL/unattended.sh; do
    mutate "$f" "/^$1() {/,/^}/ { /^$1() {/b; /^}/b; d; }"
    mutate "$f" "/^$1() {/a\\$2"
  done
}
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
drow() {               # unit · declared paths — a dispatch row at the CURRENT HEAD
  printf '\n2026-08-21T00:00:00Z dispatch · item %s %s · reason %s\n' \
    "$(git rev-parse --short=8 HEAD)" "$1" "$2" >> memory/builds/tRun/RUN.md
  git add -A && git commit -q -m "declare $1" --no-verify
}
write_run_branch() {            # names the checked-out branch as tRun's run branch, so check 23 FAILS this run
  grep -q '^run-branch: ' memory/builds/tRun/RUN.md \
    || sed -i "/^## Run facts$/a run-branch: $(git symbolic-ref -q HEAD)" memory/builds/tRun/RUN.md
}
write_overlapping_dispatch() {              # unit · declared paths — drow, then a SIBLING that never commits, so the
  write_run_branch              # unit's window overlaps one and check 23 COUNTS its undeclared writes
  drow "$1" "$2"
  drow ARCH-tRun-9 "work/nine.txt"
}
drows() {              # unit · paths-for-row-1 · paths-for-row-2 — BOTH at the current anchor
  G=$(git rev-parse --short=8 HEAD)
  printf '\n2026-08-21T00:00:00Z dispatch · item %s %s · reason %s\n' "$G" "$1" "$2" >> memory/builds/tRun/RUN.md
  printf '2026-08-21T00:00:00Z dispatch · item %s %s · reason %s\n' "$G" "$1" "$3" >> memory/builds/tRun/RUN.md
  git add -A && git commit -q -m "declare $1" --no-verify
}
gdrows() {             # unit1 · paths1 · unit2 · paths2 — both rows at the CURRENT anchor
  G=$(git rev-parse --short=8 HEAD)
  printf '\n2026-08-21T00:00:00Z dispatch · item %s %s · reason %s\n' "$G" "$1" "$2" >> memory/builds/tRun/RUN.md
  printf '2026-08-21T00:00:00Z dispatch · item %s %s · reason %s\n' "$G" "$3" "$4" >> memory/builds/tRun/RUN.md
  git add -A && git commit -q -m "declare $1 and $3" --no-verify
}
land_as() {            # anchor-kind · witness
  sed -i 's/^phase: .*/phase: LANDED/' memory/builds/tRun/RUN.md
  sed -i "s/^witness: .*/witness: $2/" memory/builds/tRun/RUN.md
  [ -n "$1" ] && printf 'landed-anchor: %s\n' "$1" >> memory/builds/tRun/RUN.md
  git add -A
}

# ---- THE REF CARRIER, and the rule the two-shard file wrote by hand once (TOOL-aBatchedArm-3 S5).
# ---- A shard starts from a FRESH fixture; the unsharded run reaches the same line carrying what
# ---- every earlier region left behind. Region one's lifecycle control merges `unit` into `main`
# ---- and pushes, so from there `unit` is an ANCESTOR of `main` on both stores, and the tWaive
# ---- fixture fast-forwards onto that without saying so — a bare shard hits a real merge that
# ---- CONFLICTS on tRun/RUN.md and is swallowed whole; measured when the two-shard seam was cut,
# ---- three arms failing naming a waiver and none naming the cause. The replay re-establishes that
# ---- topology at every boundary whose unsharded capture carries it; `read_topo` is what says
# ---- whether a boundary owes it, and whether the replay was enough.
run_landed_replay() {
  git checkout -qf main && git merge -q --no-edit unit >/dev/null 2>&1
  git push -q -f origin main >/dev/null 2>&1
  git checkout -qf unit
}
# TOPOLOGY, never shas: the ref NAME sets on the fixture origin and in the clone, plus the ancestry
# verdicts a later arm depends on. Two processes never share a sha, which is why the sha-bearing
# oracle was refused. ENV-GATED and inert by default — it adds no assertion and moves no verdict;
# CHECK_UNATTENDED_TOPO=1 prints one `topo` line per boundary, which the unsharded run emits at the
# boundary's line and shard k at its start. The two must be byte-identical after the replay (AC8).
# A second line carries the clock and the count, which differ by construction and are not compared.
read_topo() { # <boundary index>
  [ -n "${CHECK_UNATTENDED_TOPO:-}" ] || return 0
  local o l a b
  o=$(git ls-remote --heads "$ORIGIN" 2>/dev/null | cut -f2 | tr '\n' ' ')
  l=$(git for-each-ref --format='%(refname)' refs/heads/ | tr '\n' ' ')
  a=$(git merge-base --is-ancestor unit main 2>/dev/null && echo yes || echo no)
  b=$(git merge-base --is-ancestor unit "$(git --git-dir="$ORIGIN" rev-parse refs/heads/main)" 2>/dev/null && echo yes || echo no)
  echo "topo boundary=$1 origin=[$o] local=[$l] unit<main=$a unit<origin-main=$b"
  echo "topo-at boundary=$1 t=$SECONDS n=$n"
}
# THE NAMED NEGATIVE's plant (AC8). A capture that always prints the fresh set is dead, and nothing
# above can tell. CHECK_UNATTENDED_PLANT names heads, space-separated, that a fresh start does NOT
# carry — the derived leaked set, `ahead` and `trunk` at this base — and they are created in BOTH
# stores here, before any region, so shard k's opening capture must show them and differ from the
# same shard's unplanted capture. Inert unless set; the region's first `reset_tree` deletes them.
for _plant in ${CHECK_UNATTENDED_PLANT:-}; do
  git branch -f "$_plant" HEAD >/dev/null 2>&1 && git push -q origin "refs/heads/$_plant" >/dev/null 2>&1
done

# ---- THE HOIST SET, continued (TOOL-aGraftedHelix-34 S7). Thirty-one helpers had come to be defined
# ---- inside region 8 since the set above was gathered, against its own rule; they moved here when
# ---- that region was re-cut across the eight, byte-identical and in their old order, so a section
# ---- moved to another region can never strand one. The comments that explain them stayed with
# ---- the arms that use them.
read_scan_overlaps() { ( cd "$_b1" && . "./$KIT_REL/lib-unattended.sh" \
  && scan_shared_index_overlaps "$(resolve_shared_records "$1" memory)" "$(resolve_generated_indexes "$_b1" "" memory)" ); }
run_skip_leg() { bash "$SCRIPT" --skip 28 2>&1; }
lmrun() { ( cd "$lm_dir" && bash "$KIT_REL/check-unattended.sh" 2>&1 ); }
lmrestore() { git -C "$lm_dir" checkout -q -- "$1"; }
lmland() { # python-expression-free: awk over the section boundaries
  LMREPL="$1" awk -v mode="$2" '
    $0 == "## Land" { inl = 1; print; next }
    inl && /^## / { inl = 0 }
    inl && mode == "empty" { next }
    inl && mode == "sub" { gsub(ENVIRON["LMFROM"], ENVIRON["LMREPL"]) }
    { print }
    END { }' "$lm_dir/$KIT_REL/SKILL.template.md" > "$lm_dir/.land.tmp" \
    && mv "$lm_dir/.land.tmp" "$lm_dir/$KIT_REL/SKILL.template.md"
}
ric() { # fixture dir · record path · literal line · [cap]
  ( cd "$1" || exit 2
    INTRODUCING_WALK_CAP=${4:-400}; export INTRODUCING_WALK_CAP
    # shellcheck disable=SC1091
    . "$TMP/$KIT_REL/lib-unattended.sh"
    # shellcheck disable=SC1090
    . "$ric_fn"
    resolve_introducing_commit "$2" "$3" )
}
ric_want() { # label · derived sha
  n=$((n+1)); [ -n "$2" ] || { echo "FAIL $1 derived no commit — the fixture did not build, and every assertion over it would compare two empties"; st=1; }
}
ric_init() { # dir -> a fresh repository with one seed commit
  mkdir -p "$1/$ric_d"; ( cd "$1" || exit 2
    git init -q -b main . && git config user.email t@t.test && git config user.name t \
      && git config core.autocrlf false
    echo seed > seed.txt; git add seed.txt; git commit -qm seed ) >/dev/null 2>&1
}
set_ak_pristine() {
  ( cd "$ak" && git reset -q --hard "$AK_PRISTINE" && git clean -qfd && git branch -f main "$AK_ANCHOR" \
      && git push -q -f origin "$AK_ANCHOR":main && git --git-dir="$ak_origin" symbolic-ref HEAD refs/heads/main )
}
run_ak_leg() { ( cd "$ak" && GOV_UNATTENDED_REPORT=1 bash "$KIT_REL/check-unattended.sh" --skip 28 2>&1 ); }
add_ak_commit() { ( cd "$ak" && git add -A >/dev/null && git commit -q -m "$1" --no-verify ); }
run_touching_probe() { # fixture dir · commit · base · path -> rc=<status>; reason in $tc_root/err, git trace in $tc_root/trace
  rm -f "$tc_root/err" "$tc_root/trace"
  ( cd "$1" || exit 9
    # shellcheck disable=SC1091
    . "$TMP/$KIT_REL/lib-unattended.sh"
    GIT_TRACE="$tc_root/trace"; export GIT_TRACE
    check_touching_commit_reachable "$2" "$3" "$4"; echo "rc=$?" ) 2>"$tc_root/err"
}
ma_leg() { ( cd "$1" && GOV_UNATTENDED_REPORT=1 bash "$KIT_REL/check-unattended.sh" --skip 28 2>&1 ); }
ma_commit() { ( cd "$1" && git add -A >/dev/null && git commit -q -m "$2" --no-verify ) }
ma_sha() { git -C "$1" rev-parse "$2" 2>/dev/null; }
ma_base() { git -C "$1" log --format=%H --grep='^second$' -1; }
ma_readme() { # dir · slug · [extra front-matter line]
  mkdir -p "$1/memory/builds/$2"
  printf -- '---\nslug: %s\nnode: a\nopened: 2026-08-01\nstreams: architecture\nroster: TOOL\nids: TOOL-%s-1\n%s---\n\n# %s\n\n<!-- gen:build-index -->\n<!-- gen:build-units -->\n<!-- /gen:build-units -->\n<!-- /gen:build-index -->\n' \
    "$2" "$2" "${3:+$3
}" "$2" > "$1/memory/builds/$2/README.md"
}
ma_run() { # dir · slug -> an empty record; ma_facts fills it
  printf '# %s - run state\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nphase: RUNNING\nwitness: WITNESS\nbase: BASE\nmode: slug\nmay: none\n' \
    "$2" > "$1/memory/builds/$2/RUN.md"
}
ma_facts() { # dir · slug · phase · witness-rev · base-rev
  sed -i "s|^phase: .*|phase: $3|; s|^witness: .*|witness: $(ma_sha "$1" "$4")|; s|^base: .*|base: $(ma_sha "$1" "$5")|" \
    "$1/memory/builds/$2/RUN.md"
}
ma_grant() { # dir · slug · value -> a `may:` line added to that build's README front matter
  sed -i "/^slug: $2\$/a may: $3" "$1/memory/builds/$2/README.md"
}
ma_init() { # name · [bare] -> $ma_root/<name>, built to the shape above; `bare` commits neither grant
  local d="$ma_root/$1"
  mkdir -p "$d/$KIT_REL" "$d/memory/guides"
  cp "$TMP/$KIT_REL/check-unattended.sh" "$TMP/$KIT_REL/unattended.sh" "$TMP/$KIT_REL/lib-unattended.sh" \
     "$TMP/$KIT_REL/check-playbook.sh" "$TMP/$KIT_REL/PROTOCOL.template.md" "$TMP/$KIT_REL/SKILL.template.md" \
     "$TMP/$KIT_REL/VERBS.template.md" "$TMP/$KIT_REL/PLAYBOOK-TEMPLATE.template.md" \
     "$TMP/$KIT_REL/.unattended.conf.example" "$d/$KIT_REL/"
  cp "$TMP/$KIT_REL/PROTOCOL.template.md" "$d/memory/guides/UNATTENDED-PROTOCOL.md"
  cp "$TMP/$KIT_REL/VERBS.template.md" "$d/memory/guides/UNATTENDED-VERBS.md"
  cp "$TMP/$KIT_REL/ASKS.template.md" "$d/$KIT_REL/"
  cp "$TMP/$KIT_REL/ASKS.template.md" "$d/memory/guides/UNATTENDED-ASKS.md"
  cp "$TMP/.unattended.conf" "$d/.unattended.conf"
  ma_readme "$d" tRun; ma_readme "$d" tOther; ma_readme "$d" tOther2; ma_readme "$d" tOther3
  ma_run "$d" tRun
  ( cd "$d" || exit 2
    git init -q -b main . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
    git add -A >/dev/null && git commit -q -m base --no-verify
    printf 'second\n' > second.txt; git add -A >/dev/null && git commit -q -m second --no-verify
    git init -q --bare "$d.git" && git --git-dir="$d.git" symbolic-ref HEAD refs/heads/main
    git remote add origin "$d.git" && git push -q origin main
    git checkout -q -b unit ) >/dev/null 2>&1
  ma_facts "$d" tRun RUNNING main "$(ma_base "$d")"; ma_commit "$d" facts
  [ "${2:-}" = bare ] || { ma_grant "$d" tOther2 bin/run-granted.sh; ma_commit "$d" "run grants"; }
  ( cd "$d" && git commit -q --allow-empty -m "unit work" --no-verify )
  ( cd "$d" && git checkout -q main ) >/dev/null 2>&1
  [ "${2:-}" = bare ] || { ma_grant "$d" tOther bin/owner-granted.sh; ma_commit "$d" "owner grants"; }
  ( cd "$d" && git push -q origin main && git checkout -q unit ) >/dev/null 2>&1
}
ma0_reset() { ( cd "$ma0" && git reset -q --hard "$MA0_PRISTINE" && git clean -qfd ); }
write_rounds_line() { sed -i '/^REVIEW_ROUNDS=/d' "$1/.unattended.conf"; printf 'REVIEW_ROUNDS="%s"\n' "$2" >> "$1/.unattended.conf"; }
build_round_walk() { # name · run raise or "" · evil merge value or "" -> $mar, a landed terminal record
  ma_init "$1" bare; mar="$ma_root/$1"
  ( cd "$mar" && git checkout -q main ) >/dev/null 2>&1; write_rounds_line "$mar" 2; ma_commit "$mar" "owner raises rounds"
  ( cd "$mar" && git push -q origin main && git checkout -q unit ) >/dev/null 2>&1
  if [ -n "$3" ]; then
    ( cd "$mar" && git merge -q --no-ff --no-commit main ) >/dev/null 2>&1
    write_rounds_line "$mar" "$3"; ma_commit "$mar" "evil reconcile"
  else
    ( cd "$mar" && git merge -q --no-edit main ) >/dev/null 2>&1
  fi
  [ -z "$2" ] || { write_rounds_line "$mar" "$2"; ma_commit "$mar" "run raises rounds"; }
  ( cd "$mar" && git checkout -q main && git merge -q --no-ff --no-edit -m "land tRun" unit ) >/dev/null 2>&1
  ma_facts "$mar" tRun LANDED HEAD "$(ma_base "$mar")"
  printf 'landed-anchor: remote\n' >> "$mar/memory/builds/tRun/RUN.md"; ma_commit "$mar" "landed record"
  MA_OWNR=$(git -C "$mar" log --format=%H --grep='^owner raises rounds$' -1)
}
measure_round_count() { printf '%s\n' "$1" | grep -cF -- "$MA_ROUNDS"; }
run_lg_leg() { GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" --skip 28 2>&1; }
write_lg_commit() { # message · [committer date]
  if [ -n "${2:-}" ]; then
    GIT_COMMITTER_DATE="$2T12:00:00Z" GIT_AUTHOR_DATE="$2T12:00:00Z" git commit -q -m "$1" --no-verify
  else
    git commit -q -m "$1" --no-verify
  fi
}
write_lg_record() { # slug · phase · witness · extra fact lines (printf %b) -> a README and a record, unstaged
  build "$1"
  sed -i "s/^phase: .*/phase: $2/; s/^witness: .*/witness: $3/; s/^base: .*/base: $ANCHOR0/" "memory/builds/$1/RUN.md"
  [ -z "${4:-}" ] || printf '%b' "$4" >> "memory/builds/$1/RUN.md"
}
write_lg_filler() { # slug -> twenty lines no other record carries
  local i; for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
    printf '<!-- %s filler %s, unique to this record -->\n' "$1" "$i" >> "memory/builds/$1/RUN.md"
  done
}
seed_c42() {
  cat > c42-profile.sh <<'C42P'
#!/usr/bin/env bash
printf 'name\tstub\n'
if [ -n "${C42_WALL:-}" ]; then printf 'wall\t%s\n' "$C42_WALL"; fi
if [ -n "${C42_QUEUE:-}" ]; then printf 'queue\t%s\n' "$C42_QUEUE"; fi
if [ -n "${C42_CMAX:-}" ]; then printf 'ceiling_max\t%s\n' "$C42_CMAX"; fi
exit "${C42_RC:-0}"
C42P
}
write_c42_conf() { # GATE_WALL · GATE_PROFILE_CMD
  printf 'GATE_WALL="%s"\nGATE_PROFILE_CMD="%s"\n' "$1" "$2" >> .unattended.conf
}

# ---- THE HOIST RULE, STANDING (TOOL-aGraftedHelix-36 S11). A helper defined inside a shard region is
# ---- stranded for every later caller in a shard that does not run that region, which is how 31 came
# ---- to live in region 8 before unit 34 hoisted them. One prologue arm, so every shard pays it: no
# ---- column-0 function definition between the first `if in_shard` line and the floor line. A file
# ---- with no region or no floor line is a DEAD PROBE, never a clean read. WHAT THIS DOES NOT CHECK:
# ---- an indented definition, which is a string a fixture writes, or a helper defined inside `eval`.
check_helpers_hoisted() { # <suite file> -> 0 and nothing printed, or 1 naming each definition
  awk '/^if in_shard/ { r++ } /^FLOOR_ASSERTIONS=/ { f = 1; exit }
       r && /^[A-Za-z_][A-Za-z0-9_]*\(\) *\{/ { print FILENAME ":" NR ": " $0; bad = 1 }
       END { if (!r || !f) { print "DEAD PROBE: no shard region or no floor line read in " FILENAME; exit 1 }
             exit bad }' "$1"
}
_hh=$(check_helpers_hoisted "$HERE/check-unattended.test.sh"); _hrc=$?
n=$((n+1)); [ "$_hrc" = 0 ] && [ -z "$_hh" ] \
  || { echo "FAIL a helper is defined inside a shard region, stranded for any shard that does not run it: $_hh"; st=1; }

# ---- REGION 1 ------------------------------------------------------------------------------------
# Bodies are NOT reindented: `check-arms.py` reads lines and skips comments, so an unindented wrapper
# leaves every arm signature byte-identical and the armed-branch pin untouched.
if in_shard 1; then
# ---- a leg that reds on everything arms every branch and checks nothing.
out=$(run); rc=$?
same "a conforming tree exits 0" "$rc" "0"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi
same "a conforming tree prints nothing" "$(remove_announcements "$out")" ""

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

# ---- THE CONF MAY NOT REDIRECT THE LEG'S OWN SUBJECT (closing-review F1). The import's arm used to
# ---- be the open glob `[A-Z][A-Z0-9_]*`, which assigned EVERY uppercase key the conf declared -
# ---- including the three this leg sets ABOVE the import. `.unattended.conf` is a tracked file an
# ---- unattended run commits itself, and this leg is on an unguarded merge bar, so one line in it
# ---- pointed the gate at a file other than the one it certifies.
# ----
# ---- PORTED FROM `check-brief-recorded.test.sh`'s evil-driver arm, which armed the same class on
# ---- the sibling importer in the same build. Three keys, three shapes, because they break three
# ---- different things and an arm on one is an arm on one.
# ----
# ---- EQUALITY, not a `miss` on one string. The claim is that the hostile line changed NOTHING, and
# ---- a `miss` on one refusal would pass over any other damage the redirect did. `$_f1_clean` is
# ---- captured on the same pristine fixture, so the two runs differ by exactly one appended line.
# ----
# ---- THE HOSTILE LINES ARE `export`-PREFIXED, and that is the whole point rather than a flourish.
# ---- Check 22's project-conf key join greps `^[A-Z_]+=` - column 0, no `export` - while the
# ---- importer's sed accepts a leading `export`, so the exported spelling is the one check 22 is
# ---- BLIND to and the importer still honours. An arm on the column-0 form alone would have been
# ---- satisfied by check 22 redding for an entirely different reason, and would have proved nothing
# ---- about the import. The column-0 form gets its own arm below, saying exactly that.
reset_tree
_f1_clean=$(run)
# The control's validity, asserted rather than assumed - and NOT as "the baseline is empty". This
# fixture carries whatever standing reds the suite already has, and an emptiness assertion here would
# simply restate the conforming-tree arm above and inherit its failures. What matters is that the
# baseline does not ALREADY carry the redirect's own symptom, or the equality arms below would be
# comparing one broken run against another.
miss "$_f1_clean" "cannot read AUTH_MODES from the driver, so the mode-membership branch and the directive scope join would both pass over an empty set"

reset_tree
printf 'export DRIVER="/dev/null"
' >> .unattended.conf
same "a conf DRIVER does not redirect the leg away from the driver it certifies" "$(run)" "$_f1_clean"

# ...`HERE` redirects the kit files this leg reads out of its own install directory - the Skill
# template check 16 joins the registry against, and the playbook leg check 28 byte-compares.
reset_tree
printf 'export HERE="/nonexistent"
' >> .unattended.conf
same "a conf HERE does not redirect the kit files this leg reads out of its own install dir" "$(run)" "$_f1_clean"

# ...and `SCOPE`, which is the worst of the three: it is read AFTER the import, so `skip28` in the
# conf silently deleted the whole check-28 region including 28c, the pinned-git-read enforcement -
# a check quietly deleted by the file it grades. The break is check 28's own scalar-parser arm, so a
# region that RAN says so in its own words rather than by the absence of something.
reset_tree
rm -f $KIT_REL/check-playbook.sh
printf 'export SCOPE="skip28"
' >> .unattended.conf
hit "$(run)" "the declared-scalar parser is missing from one of the two scripts that inline it, so the comparison that keeps the copies one answer would pass over an empty pair - driver and leg follow:"

# ...and the COLUMN-0 spelling, recorded so nobody re-litigates check 22 as the mitigation. It reds
# here, but on check 22 and for its own reason - an undeclared key in the project conf - while the
# thing that actually matters is that check 1 no longer refuses over a driver it was pointed at.
reset_tree
printf 'DRIVER="/dev/null"
' >> .unattended.conf
out=$(run)
hit "$out" "the protocol's binding key table and the declared conf disagree, so a key is either configurable and undocumented or documented and dead. undocumented in the protocol:"
miss "$out" "cannot read AUTH_MODES from the driver, so the mode-membership branch and the directive scope join would both pass over an empty set"
reset_tree

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
# `--framed` and `--paths` are flags of `--plan`: each selects an output MODE and dispatches
# nothing, so demanding either a Skill section would demand a section nobody should write.
# TOOL-aQuenchedHarness-10.
#
# BOTH ARE HERE BECAUSE THAT UNIT PUT THEM IN THE POPULATION. Rewriting `--plan`'s argument
# loop turned `[ "${1:-}" = "--paths" ]` into a `--paths)` case arm, and this population is
# derived from case arms - so a refactor that changed no behaviour added a verb to a set it
# never meant to touch. I first recorded `--paths` as a pre-existing red on the strength of it
# appearing equally in both trees; a baseline run of this suite against main named only
# `--disposition` and `--unit`, which is what settled it. Counting occurrences of a flag is not
# the same question as whether it is DISPATCHED.
#
# FIXED 2026-09-22, at the aBatchedArm landing, on the owner's instruction to clear the
# pre-existing reds: `--unit` is a flag of `--brief` and `--disposition` one of `--review`, both
# dispatched as case arms and both documented by the verb they belong to, so both are denied and
# the floor below is re-derived over the population they were inflating.
#
# FIVE MORE FLAGS, from dDerivedDocket, each a case arm that assigns and documented on its verb's
# header line: `--asks` is an output mode of `--plan` as `--paths` is (TOOL-dDerivedDocket-16 S8);
# `--until` and `--reaped` are arguments of `--hold` (TOOL-dDerivedDocket-4 S2); `--replaces` and
# `--scheduled` are arguments of `--resume` (TOOL-dDerivedDocket-4 S6, TOOL-dDerivedDocket-5 S6).
# Undenied, each demanded a Skill section, a synopsis line and a VERBS_ entry of its own.
# TWO MORE, found red at aWindowedPass's VERIFYING and already red at its base: `--task` and
# `--heartbeat` are arguments of `--register-task`/`--release-task`, documented on their header lines.
# TWO MORE, `--highs` and `--minors`, arguments of `--review` as `--disposition` is, case arms since
# the review verb took its severity counts; red from then until TOOL-aGraftedHelix-34 S3 denied them.
_denied='--keepalive-id --item --value --override --waive --reason --code --subject --verdict --blockers --act --pass --successor --writes --leg --path --step --records-root --playbook-sha --run --set --framed --paths --unit --disposition --asks --until --reaped --replaces --scheduled --task --heartbeat --highs --minors'
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
# EIGHTEEN, the verbs this kit actually dispatches, DERIVED at the aBatchedArm landing by running
# this file's own derivation over the driver and counting: 20 case arms less `--unit` and
# `--disposition`, the two flags the line above now denies. It was 14 against a polluted population
# of 20, so six verbs could have stopped being dispatched with the floor still green. A floor set
# against a polluted population pins nothing.
# NINETEEN since dDerivedDocket, re-derived the same way: `--hold` is a verb it added
# (TOOL-dDerivedDocket-4 S2), and the five flags it added are denied above. The assertion count is
# unchanged; only the number it compares against moved.
n=$((n+1)); [ "$_nverbs" -ge 19 ] || { echo "FAIL the dispatched-verb population read $_nverbs verbs against a floor of 19, so the documentation join below would grade a set smaller than the kit actually ships"; st=1; }
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
hit "$out" "review loops that ran past the ceiling, stalled without recording it, or exited without accounting for their blockers"
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
same "a project phase EXTENSION is green" "$(remove_announcements "$(run)")" ""

reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
ndod=$(grep '^DOD_CORE=' $KIT_REL/unattended.sh | tr -d '
' | sed 's/^DOD_CORE="//; s/"$//' | wc -w)
mutate $KIT_REL/unattended.sh 's/ [a-z][a-z-]*:\(machine\|agent\)"$/"/'
out=$(run)
hit "$out" "the kit's CORE Definition-of-Done set has shrunk below its floor, and deleting an item is a silent, reason-free override of everything keyed on it"
hit "$out" "$((ndod-1)) against $ndod"

reset_tree; mkconf "" "project-item:machine"
same "a project DoD EXTENSION is green" "$(remove_announcements "$(run)")" ""

# ---- ...and the floor itself must be DECLARED. Omitting the key is the quietest way to disarm a
# ---- shrink-only pin, so the omission is its own refusal rather than a skipped check.
reset_tree; sed -i '/^CORE_FLOOR=/d' .unattended.conf
# ---- check 2/3's empty-set branches. Reached by declaring the CORE set as whitespace, which parses
# ---- to a readable-but-empty value — distinct from the unreadable case armed above.
sed -i 's/^PHASES_CORE="[^"]*"/PHASES_CORE=" "/' $KIT_REL/unattended.sh
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "CORE_FLOOR is undeclared in .unattended.conf, and with no floor a deleted core member is indistinguishable from a set that never had one|the effective phase vocabulary is empty, which makes every phase check below vacuously true|a TERMINAL phase is not in the effective vocabulary, so no run could ever reach it|a run-state file declares a phase outside the effective vocabulary|the protocol's run-order list names a phase the driver does not carry, so the contract promises a position no run can ever occupy|a phase is published as a build-method pass kind and is not in the core vocabulary, so the contract names a position no run can ever occupy" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 1/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "CORE_FLOOR is undeclared in .unattended.conf, and with no floor a deleted core member is indistinguishable from a set that never had one"
hit "$out" "the effective phase vocabulary is empty, which makes every phase check below vacuously true"
reset_tree; sed -i 's/^DOD_CORE="[^"]*"/DOD_CORE=" "/' $KIT_REL/unattended.sh
# ---- check 4 branch 1: THE POPULATION GUARD, both states. A run-state file under the memory root
# ---- but NOT at the selected path is the mis-segmentation. A tree with none anywhere is a YOUNG
# ---- tree and must be SILENT — the arm whose absence made the equivalent guard red every freshly
# ---- scaffolded repo, which is recorded in this fleet's own gotcha catalogue.
mkdir -p memory/elsewhere && git mv memory/builds/tRun/RUN.md memory/elsewhere/RUN.md
git commit -q -am moved --no-verify
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "the effective Definition-of-Done set is empty, so --close would block on nothing|the kit's CORE Definition-of-Done set has shrunk below its floor, and deleting an item is a silent, reason-free override of everything keyed on it|a run-state file exists under the memory root but none at the path this leg selects, so the selector is mis-segmented and every check below is silent for the wrong reason|the protocol's Definition-of-Done table names an item the driver does not carry, so the contract publishes a gate nothing evaluates|the protocol's stated count of core Definition-of-Done items disagrees with the set the driver enforces, and that sentence sits directly above the table it miscounts: says" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 1/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "the effective Definition-of-Done set is empty, so --close would block on nothing"
hit "$out" "a run-state file exists under the memory root but none at the path this leg selects, so the selector is mis-segmented and every check below is silent for the wrong reason"

reset_tree; git rm -q memory/builds/tRun/RUN.md && git commit -q -m young --no-verify
out=$(run); rc=$?
miss "$out" "the selector is mis-segmented"
same "a young tree with no run-state file anywhere exits 0" "$rc" "0"
same "a young tree prints nothing" "$(remove_announcements "$out")" ""

# ---- check 4 branches 2 and 3: no phase, and a phase outside the vocabulary.

fi   # ---- end REGION 1 -----------------------------------------------------------------------------------

# ---- REGION 2 -----------------------------------------------------------------------------------
if in_shard 2; then
read_topo 2
reset_tree; sed -i '/^phase: /d' memory/builds/tRun/RUN.md
hit "$(run)" "a run-state file declares no phase, and a file with no phase is outside every check keyed on one"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi
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

# ---- TOOL-aUnblockedFleet-2/-4: check 7 REPORTS two non-terminal run-state files and the leg still
# ---- passes. It asserted a refusal until kit 1.13. The green half is the whole rest of this file —
# ---- every other arm runs with exactly one live run and must not trip this.
reset_tree; build tTwo
sed -i "s/^witness: WITNESS$/witness: $(git rev-parse HEAD)/" memory/builds/tTwo/RUN.md
sed -i "s/^base: BASE$/base: $(git merge-base main HEAD)/" memory/builds/tTwo/RUN.md
git add -A && git commit -q -m two --no-verify
out=$(run)
hit "$out" "2 concurrent unattended run(s) — none of them blocks another"
hit "$out" "memory/builds/tTwo/RUN.md · phase RUNNING"
miss "$out" "more than one run-state file is non-terminal"
# ...and a TERMINAL second run produces NO report at all: the report is about live runs, not files.
# This is the silent-at-one control, and without it a leg that reported unconditionally passes above.
sed -i 's/^phase: RUNNING$/phase: LANDED/' memory/builds/tTwo/RUN.md
out=$(run)
miss "$out" "concurrent unattended run(s)"

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
#
# ---- THE CUTOFF IS STRIPPED, and that is load-bearing rather than tidiness. This record is STAGED
# ---- and never committed, so it carries no first-commit date - and check 2 grades exactly that case
# ---- "whatever the cutoff says, being the one case that can still record a disposition"
# ---- (check-unattended.sh:483). With a cutoff DECLARED, these two rows take the recorded-disposition
# ---- path, record none, and the leg emits the no-disposition message instead of the promotion count
# ---- this arm asserts. Measured: declaring the key in mkconf broke this one arm and only this one.
# ---- The arm wants the blank branch, so it now says so instead of inheriting it from the fixture.
reset_tree; mkconf; sed -i '/^DISPOSITION_CUTOFF=/d' .unattended.conf
mkdir -p memory/builds/tProm
printf '# tProm\n\n<!-- gen:build-units -->\n| Unit | Status |\n|---|---|\n| TOOL-tProm-1 | CLOSED |\n<!-- /gen:build-units -->\n' > memory/builds/tProm/README.md
git add -A >/dev/null 2>&1 && git -c commit.gpgsign=false commit -q -m promobase --no-verify
PROMBASE=$(git rev-parse HEAD)
printf '# tProm\n\n<!-- gen:build-units -->\n| Unit | Status |\n|---|---|\n| TOOL-tProm-1 | CLOSED |\n| TOOL-tProm-2 | CLOSED |\n<!-- /gen:build-units -->\n' > memory/builds/tProm/README.md
printf '# tProm\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nphase: RUNNING\nwitness: abc\nbase: %s\n\n2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT\n\n2026-08-20T02:00:00Z review · item S2 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT\n' "$PROMBASE" > memory/builds/tProm/RUN.md
git add -A >/dev/null 2>&1
hit "$(run)" "2 subject(s) EXITED without converging and the generated units region gained only 1 non-WONTDO unit id(s) this run BASE lacked, so at least one blocker was neither fixed nor promoted"
reset_tree

# ---- THE SET IS READ FROM THE DRIVER, so an unreadable declaration is a refusal and not a silent
# ---- comparison against nothing. Closing-review fold: the leg used to restate `fold|promote`, which
# ---- drifts the moment the driver's set moves and lets this leg tell a record it was hand-edited
# ---- when the driver itself wrote the value.
reset_tree; mkconf
mutate $KIT_REL/unattended.sh 's|^REVIEW_DISPOSITIONS=.*|REVIEW_DISPOSITIONS=fold\|promote|'
hit "$(run)" "the driver declares no readable REVIEW_DISPOSITIONS, so the clause that grades a recorded disposition would compare every value against an empty set and report whatever that produces as a verdict"
reset_tree

# ---- TOOL-dFoldedVerdict-2: THE GRADED PATH — clause 3 READING a recorded disposition instead of
# ---- inferring one from ids. Every arm pins the cutoff to a date the fixture cannot drift past:
# ---- 2000-01-01 forces grading, 2099-01-01 forces the pre-cutoff proxy. Neither depends on the day
# ---- the suite runs, which a cutoff of "today" would.
# STRIPS BEFORE IT APPENDS, since mkconf now declares the key itself. Appending alone would leave the
# conf carrying two declarations of one key: the leg's import reads the last and would behave, but a
# fixture that declares a key twice is a fixture check 22 grades on a key set nobody meant to write.
D_ONE='| TOOL-tDisp-1 | CLOSED |\n'
D_TWO='| TOOL-tDisp-1 | CLOSED |\n| TOOL-tDisp-2 | CLOSED |\n'

# A FOLD BESIDE A NON-ZERO BLOCKER COUNT IS A REFUSAL (closing review of aProbedUnit, cluster C).
# This fixture used to be the green "a fold-only exit demands nothing" control, and that was the
# hole: `review_state` returns CONVERGED for count 0, so a NON-CONVERGENT row stands on a blocker,
# the severity rule promotes every blocker, and `blockers 2 · disposition fold` was two blockers left
# standing under a field the clause read as demanding nothing. The driver refuses the row at write
# time now; the leg reds one first-committed AT OR AFTER the driver's FOLD_CUTOFF, so the record is
# committed at that date. At base this fixture printed no check 2 line.
reset_tree; dispconf 2000-01-01
DISPDATE="2026-09-15T00:00:00 +0000" mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition fold\n'
hit "$(run)" "record disposition fold beside a NON-ZERO blocker count in a record first-committed on or after FOLD_CUTOFF, after which the driver refuses this at write time, and the severity rule promotes every blocker, so a fold there is a blocker left standing under a field that says nothing was"

# ...AND THE RULE HAS ITS OWN CUTOFF (closing review of aProbedUnit, round 2, cluster A — the
# BLOCKER). Graded under DISPOSITION_CUTOFF alone, the clause above redded sixteen tracked
# append-only records this repo's own driver wrote while `fold` was legal at every terminal exit,
# and no verb can rewrite them. A record first-committed BEFORE FOLD_CUTOFF carrying the same row is
# read as the contract that accepted it read it — demanding nothing — and one AT the cutoff is
# graded by the rule. The pair is BOUNDED, the exit the kit default produces.
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · BOUNDED · disposition fold\n'
miss "$(run)" "check 2 FAILED"
reset_tree; dispconf 2000-01-01
DISPDATE="2026-09-15T00:00:00 +0000" mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · BOUNDED · disposition fold\n'
hit "$(run)" "record disposition fold beside a NON-ZERO blocker count in a record first-committed on or after FOLD_CUTOFF"

# ...and a FOLD_CUTOFF the leg cannot read is named, not defaulted: empty sorts before every date
# and reds the whole grandfathered population, malformed sorts after and disarms the clause. Named
# inside check 2's own failure rather than at a `fail` site of its own, because the pinned check-2
# ordinals in memory/project/unarmed-branches.txt sit below the read.
reset_tree; mkconf
mutate $KIT_REL/unattended.sh 's|^FOLD_CUTOFF=.*|FOLD_CUTOFF=2026-09-15|'
hit "$(run)" "the driver declares no readable ISO-date FOLD_CUTOFF, so the fold-beside-blockers clause cannot tell a record written under the old contract from one graded by the severity rule and would red every record or none"

# ...and a fold beside ZERO blockers still demands nothing: nothing above MEDIUM stood, so nothing
# was owed a unit. Written by hand — the driver reaches CONVERGED at 0 and never NON-CONVERGENT —
# which is exactly the population this clause grades.
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · disposition fold\n'
miss "$(run)" "check 2 FAILED"

# A CONVERGED ROW RECORDING `promote` OWES AN ID (cluster C, id 12). The severity rule disposes the
# HIGHS that stood at zero blockers, the driver records the promotion on the converged row, and
# `needs` never read a CONVERGED row — so a promotion the harness performed was invisible to the bar
# and a missing unit passed. At base the first fixture printed no check 2 line.
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · disposition promote\n'
hit "$(run)" "1 subject(s) EXITED recording disposition promote and the generated units region gained only 0 non-WONTDO unit id(s) this run BASE lacked"
# ...its green control: the id present, the row passes.
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_TWO" '2026-08-20T01:00:00Z review · item S1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · disposition promote\n'
miss "$(run)" "check 2 FAILED"
# ...and a CONVERGED row with NO field is still the ordinary converged round and demands nothing.
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED\n'
miss "$(run)" "check 2 FAILED"

# ...and the GREEN CONTROL for it: the same fixture with the disposition stripped is a REFUSAL, not a
# pass. Without this arm `nneed` falls to zero on every unlabelled record and the clause becomes
# green-by-absence — the shape this rewrite exists to remove.
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT\n'
hit "$(run)" "record NO disposition while this record is graded against DISPOSITION_CUTOFF, so which of fold or promote the run took cannot be read"

# A PROMOTE EXIT SHORT OF IDS still reds, so reading the field did not disarm the clause.
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition promote\n'
hit "$(run)" "EXITED recording disposition promote and the generated units region gained only 0 non-WONTDO unit id(s) this run BASE lacked"

# ...and its green control: the same promote exit WITH the id present passes.
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_TWO" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition promote\n'
miss "$(run)" "check 2 FAILED"

# ---- TOOL-aBatchedMinors-3: A CLOSING-REVIEW ROW CARRYING COUNTS OWES ONE UNIT PER BLOCKER AND HIGH,
# ---- PLUS ONE FOR ITS MINORS. The owner ruled on 2026-10-04 that the closing diff review promotes
# ---- every finding, the mediums and lows batched into one unit or two, and `--review` now writes
# ---- `highs <n> · minors <n>` on that exit. Against the base reader every red arm below passes on
# ---- one new id, because the floor was one per subject whatever stood.
D_THREE='| TOOL-tDisp-1 | CLOSED |\n| TOOL-tDisp-2 | CLOSED |\n| TOOL-tDisp-3 | CLOSED |\n'
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_TWO" '2026-08-20T01:00:00Z review · item tDisp · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 3 · disposition promote\n'
out=$(run)
hit "$out" "gained only 1 non-WONTDO unit id(s) this run BASE lacked, against a floor of 2"
# ...the leading count is SUBJECTS, the floor is UNITS: one subject owing two (round 1, L6 id 11)
hit "$out" "1 subject(s) EXITED recording disposition promote and the generated units region gained only 1"
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_THREE" '2026-08-20T01:00:00Z review · item tDisp · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 3 · disposition promote\n'
miss "$(run)" "check 2 FAILED"
# ...the minors add nothing when none stood: two highs owe two units, not three
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_TWO" '2026-08-20T01:00:00Z review · item tDisp · reason verdict BLOCKED · blockers 0 · CONVERGED · highs 2 · minors 0 · disposition promote\n'
hit "$(run)" "against a floor of 2"
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_THREE" '2026-08-20T01:00:00Z review · item tDisp · reason verdict BLOCKED · blockers 0 · CONVERGED · highs 2 · minors 0 · disposition promote\n'
miss "$(run)" "check 2 FAILED"
# ...a closing exit that did not converge owes its standing blockers too: 2 + 1 + 1 = 4
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_THREE" '2026-08-20T01:00:00Z review · item tDisp · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · highs 1 · minors 5 · disposition promote\n'
hit "$(run)" "gained only 2 non-WONTDO unit id(s) this run BASE lacked, against a floor of 4"
# ...a converged closing row standing on minors with NO disposition is not the ordinary converged
# round: it owes a promotion and reaches the no-disposition refusal
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item tDisp · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 0 · minors 2\n'
hit "$(run)" "record NO disposition while this record is graded against DISPOSITION_CUTOFF"
# ...its green control: a closing exit standing on nothing records zeros and owes nothing
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item tDisp · reason verdict CLEAN · blockers 0 · CONVERGED · highs 0 · minors 0\n'
miss "$(run)" "check 2 FAILED"
# ...and the closing review folds nothing, at the fold cutoff and after it (round 1, L7: both dates armed)
reset_tree; dispconf 2000-01-01
DISPDATE="2026-09-15T00:00:00 +0000" mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item tDisp · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 0 · minors 2 · disposition fold\n'
hit "$(run)" "record disposition fold on a row carrying highs and minors, and a counted exit folds nothing on any subject"
reset_tree; dispconf 2000-01-01
DISPDATE="2026-10-04T00:00:00 +0000" mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item tDisp · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 0 · minors 2 · disposition fold\n'
hit "$(run)" "record disposition fold on a row carrying highs and minors, and a counted exit folds nothing on any subject"
# ...and the floors SUM across subjects in one record (round 1, L6 id 9): 1 (a spec subject without
# counts) + 2 (a closing row, one high plus the minors) = 3, so a per-subject maximum would pass two
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_THREE" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition promote\n\n2026-08-20T02:00:00Z review · item tDisp · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 1 · disposition promote\n'
hit "$(run)" "2 subject(s) EXITED recording disposition promote and the generated units region gained only 2 non-WONTDO unit id(s) this run BASE lacked, against a floor of 3"
D_FOUR='| TOOL-tDisp-1 | CLOSED |\n| TOOL-tDisp-2 | CLOSED |\n| TOOL-tDisp-3 | CLOSED |\n| TOOL-tDisp-4 | CLOSED |\n'
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_FOUR" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition promote\n\n2026-08-20T02:00:00Z review · item tDisp · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 1 · disposition promote\n'
miss "$(run)" "check 2 FAILED"

# ---- TOOL-aEvidencedLens-9 S7: A SPEC SUBJECT'S TERMINAL ROW COUNTS AND NEVER FOLDS from the
# ---- driver's SPEC_COUNTS_CUTOFF on (2026-10-06). The base check 2 passes both red rows below: a
# ---- countless converged row is the ordinary converged round, and a fold beside zero blockers
# ---- demands nothing. A record first-committed before the cutoff keeps that reading.
SC_MSG="record a terminal row with no highs and minors counts or with disposition fold in a record first-committed on or after SPEC_COUNTS_CUTOFF"
reset_tree; dispconf 2000-01-01
DISPDATE="2026-10-06T00:00:00 +0000" mkdisp "$D_ONE" "$D_ONE" '2026-10-06T01:00:00Z review · item S1 · reason verdict CLEAN · blockers 0 · CONVERGED\n'
hit "$(run)" "spec subject(s) S1 $SC_MSG"
reset_tree; dispconf 2000-01-01
DISPDATE="2026-10-06T00:00:00 +0000" mkdisp "$D_ONE" "$D_ONE" '2026-10-06T01:00:00Z review · item S1 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition fold\n'
hit "$(run)" "spec subject(s) S1 $SC_MSG"
# ...its green control: the counted row passes after the cutoff
reset_tree; dispconf 2000-01-01
DISPDATE="2026-10-06T00:00:00 +0000" mkdisp "$D_ONE" "$D_ONE" '2026-10-06T01:00:00Z review · item S1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 0 · minors 0\n'
miss "$(run)" "check 2 FAILED"
# ...a record first-committed before the cutoff is not re-graded, and the build-slug subject is not a spec one
reset_tree; dispconf 2000-01-01
DISPDATE="2026-10-04T00:00:00 +0000" mkdisp "$D_ONE" "$D_ONE" '2026-10-04T01:00:00Z review · item S1 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition fold\n'
miss "$(run)" "check 2 FAILED"
reset_tree; dispconf 2000-01-01
DISPDATE="2026-10-06T00:00:00 +0000" mkdisp "$D_ONE" "$D_ONE" '2026-10-06T01:00:00Z review · item tDisp · reason verdict CLEAN · blockers 0 · CONVERGED\n'
miss "$(run)" "check 2 FAILED"
# ...and a SPEC_COUNTS_CUTOFF the leg cannot read is named inside check 2, as FOLD_CUTOFF's is
reset_tree; mkconf
mutate $KIT_REL/unattended.sh 's|^SPEC_COUNTS_CUTOFF=.*|SPEC_COUNTS_CUTOFF=2026-10-06|'
hit "$(run)" "the driver declares no readable ISO-date SPEC_COUNTS_CUTOFF, so the counted-spec-row clause cannot tell"

# ---- TOOL-aProbedUnit-6: BOUNDED is a terminal exit that OWES a disposition and, on promote, an
# ---- id, exactly as NON-CONVERGENT does. At base the first fixture printed NOTHING: the `needs`
# ---- regex did not know the token, so a bounded promote owed nothing and the exit was green by
# ---- absence. The `term` half cannot be discriminated by a driver-written record — the driver writes
# ---- BOUNDED only on a strictly smaller count and the stalled-loop clause needs a flat one.
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · BOUNDED\n'
hit "$(run)" "record NO disposition while this record is graded against DISPOSITION_CUTOFF, so which of fold or promote the run took cannot be read"
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_TWO" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · BOUNDED · disposition promote\n'
miss "$(run)" "check 2 FAILED"

# AN ILLEGAL VALUE IS ITS OWN REFUSAL, and `promoted` is the near-miss a hand-editor actually types —
# not a nonsense token. Reading it as ABSENT would name the wrong cause, and the hand-edited record
# is not hypothetical: TOOL-dFoldedVerdict-3 creates exactly that class.
reset_tree; dispconf 2000-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition promoted\n'
out=$(run)
hit "$out" "carry a disposition outside the closed set fold|promote"
miss "$out" "record NO disposition while this record is graded against DISPOSITION_CUTOFF"

# A CUTOFF AHEAD OF THE RECORD restores today's verdict verbatim, which is what grandfathering means.
reset_tree; dispconf 2099-01-01
mkdisp "$D_ONE" "$D_ONE" '2026-08-20T01:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition fold\n'
hit "$(run)" "1 subject(s) EXITED without converging and the generated units region gained only 0 non-WONTDO unit id(s) this run BASE lacked"

# A BLANK CUTOFF grandfathers everything AND SAYS SO, unconditionally and on stdout. A silently
# disabled clause reads exactly like a clause finding nothing wrong.
#
# THE KEY IS STRIPPED EXPLICITLY, and it used to be a bare `mkconf` relying on the shared fixture not
# declaring it. That made one arm's break the DEFAULT state of every other arm's tree, so the whole
# suite ran against a tree that announced. This is the UNDECLARED shape, which is the one an adopter
# actually hits; the leg defaults the variable to empty before the branch, so blank and undeclared
# are the same state by the time it is read.
reset_tree; mkconf; sed -i '/^DISPOSITION_CUTOFF=/d' .unattended.conf
hit "$(run)" "DISPOSITION_CUTOFF is blank or undeclared, so check 2 clause 3 grades EVERY record on the id-delta proxy"

# A MALFORMED CUTOFF is a REFUSAL, never a defaulted value — S6's one new branch, and the reason the
# three pinned check-2 ordinals moved by one in memory/project/unarmed-branches.txt.
reset_tree; dispconf "last tuesday"
hit "$(run)" "DISPOSITION_CUTOFF is declared and is not an ISO date, and a cutoff nothing can compare grades every record or none"
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
mkdir -p "$TMPBIN"; printf '#!/bin/sh\ncase "$*" in *" true") exit 0 ;; esac\nexit 124\n' > "$TMPBIN/timeout"; chmod +x "$TMPBIN/timeout"
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
# NOTHING ELSE PRINTED AND EXIT 0, through the announcement filter: checks 45 and 46 announce
# LANDER_MODE, RESUME_SCHEDULE and SELFTESTS_OWED_PATHS on every run (the checker's header, THREE;
# TOOL-dDerivedDocket-3 S1, TOOL-dDerivedDocket-5 S1), so the output is never the status line alone.
same "a terminal record carrying a copy leaves the leg green" "$(remove_announcements "$(run; echo $?)")" "0"

# ---- check 9: a recorded BASE the run could quietly move is not a pin.
reset_tree; sed -i 's/^base: .*/base: 0000000000000000000000000000000000000000/' memory/builds/tRun/RUN.md
hit "$(run)" "a recorded BASE does not resolve to a commit in this history, and the record is written by the run"

# ---- check 11: the bypass flag, checked where the record is.
reset_tree; printf '\nparked: considered --no-verify to get past the hook\n' >> memory/builds/tRun/RUN.md
# ---- check 10, both branches: the pair DRIFTED, and one half missing. The second is the arm that
# ---- keeps a parity check with one file from reading as a passing parity check.
printf '\ndrifted line\n' >> memory/guides/UNATTENDED-PROTOCOL.md
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "a run-state file names the declared bypass flag, and bypassing the lander discards the whole bar the mandate leaned on|the shipped protocol and this repo's installed copy have drifted, so the kit ships something other than what it runs on" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 2/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "a run-state file names the declared bypass flag, and bypassing the lander discards the whole bar the mandate leaned on"
hit "$out" "the shipped protocol and this repo's installed copy have drifted, so the kit ships something other than what it runs on"
hit "$out" "drifted line"

fi   # ---- end REGION 2 -----------------------------------------------------------------------------------

# ---- REGION 3 -----------------------------------------------------------------------------------
if in_shard 3; then
read_topo 3
reset_tree; rm -f $KIT_REL/PROTOCOL.template.md
# ---- check 10, THE SECOND PAIR. TOOL-dFoldedVerdict-5 moved the verb entries into their own
# ---- byte-compared carrier because the protocol had reached its cap exactly. A pair added without
# ---- its own two arms is a pair nothing watches, and the check would still report green.
printf '\ndrifted line\n' >> memory/guides/UNATTENDED-VERBS.md
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "one half of the protocol pair is missing, and a parity check with one file is a check that cannot fail|the shipped verb carrier and this repo's installed copy have drifted, so the kit ships something other than what it runs on" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 3/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "one half of the protocol pair is missing, and a parity check with one file is a check that cannot fail"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi
hit "$out" "the shipped verb carrier and this repo's installed copy have drifted, so the kit ships something other than what it runs on"
hit "$out" "drifted line"
reset_tree; rm -f $KIT_REL/VERBS.template.md
hit "$(run)" "one half of the verb-carrier pair is missing, and a parity check with one file is a check that cannot fail"

# ---- check 10, THE THIRD PAIR. TOOL-dDerivedDocket-20 S4 moved the ask contract into its own
# ---- byte-compared guide, and a pair added without its own two arms is a pair nothing watches.
reset_tree; printf '\ndrifted line\n' >> memory/guides/UNATTENDED-ASKS.md
out=$(run)
hit "$out" "the shipped ask guide and this repo's installed copy have drifted, so the kit ships something other than what it runs on"
hit "$out" "drifted line"
reset_tree; rm -f memory/guides/UNATTENDED-ASKS.md
hit "$(run)" "one half of the ask-guide pair is missing, and a parity check with one file is a check that cannot fail"
# ...and the report channel names every pair it compared, so a pair whose row was never added to the
# count is visible in one run rather than only by reading the source.
reset_tree
hit "$(GOV_UNATTENDED_REPORT=1 run)" "check 10 byte-compared 3 of its 3 pairs: protocol verbs asks"

# ---- check 38: NO PATH IS BOTH A SHARED RECORD AND A GENERATED INDEX (TOOL-dDerivedDocket-20 S1).
# ---- Three shapes, because each is a different way to get the predicate wrong: a nested pair in
# ---- EACH direction reds an equality test, and an UNDECLARED SHARED_RECORDS reds a leg that reads the
# ---- key as blank instead of taking the kit default the driver takes. The control is the pristine
# ---- conf, which declares neither key, so the default is compared against an empty index set.
C38_MSG="a path is declared under both SHARED_RECORDS and GENERATED_INDEXES, so --dispatch answers it by whichever of condition 3's two rules it reaches first and the other declaration means nothing"
reset_tree
miss "$(run)" "$C38_MSG"
# ...and the control is LIVE: the report channel names the two populations it compared, the kit
# default's two records against an index set the fixture conf leaves empty.
hit "$(GOV_UNATTENDED_REPORT=1 run)" "check 38 compared 2 shared record(s) against 0 index half(s)"
printf '\nSHARED_RECORDS="memory"\nGENERATED_INDEXES="memory/LIVE.md:gen.py"\n' >> .unattended.conf
out=$(run)
hit "$out" "a path is declared under both SHARED_RECORDS and GENERATED_INDEXES, so --dispatch answers it by whichever of condition 3's two rules it reaches first and the other declaration means nothing"
hit "$out" "SHARED_RECORDS memory overlaps the index memory/LIVE.md"
reset_tree
printf '\nSHARED_RECORDS="memory/LIVE.md"\nGENERATED_INDEXES="memory:gen.py"\n' >> .unattended.conf
hit "$(run)" "SHARED_RECORDS memory/LIVE.md overlaps the index memory"
reset_tree
printf '\nGENERATED_INDEXES="memory/backlog:gen.py"\n' >> .unattended.conf
hit "$(run)" "SHARED_RECORDS memory/backlog overlaps the index memory/backlog"
# ...and a DECLARED blank is the empty set, not the default, so the same index is then accepted.
reset_tree
printf '\nSHARED_RECORDS=""\nGENERATED_INDEXES="memory/backlog:gen.py"\n' >> .unattended.conf
miss "$(run)" "$C38_MSG"
reset_tree

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
same "a conforming kickoff engine is green" "$(remove_announcements "$(run)")" ""

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
# regaining a place to stop. TOOL-aHonedRuleset-3 MOVED that enumeration out of the engine and into
# the contract, so the break is staged in the PROTOCOL PAIR -- template and installed copy, the way
# pedit does it below -- and no longer in the synthetic engine fixture, which does not carry the
# exits any more. `mutate` fails loudly on a no-op, so an arm that stopped reaching its subject
# reports as a broken fixture rather than as a passing check.
git checkout -q -- skills/session-kickoff/SKILL.md
mutate $KIT_REL/PROTOCOL.template.md '/^4\. \*\*Step 2/d'
mutate memory/guides/UNATTENDED-PROTOCOL.md '/^4\. \*\*Step 2/d'
out=$(run)
hit "$out" "the installed protocol enumerates fewer of the kickoff engine's interactive exits than the floor, and a dropped exit is a place an unattended run silently regains to stop"
hit "$out" "5 against 6"

# ...and the floor declared with no installed protocol to count in. Without this arm the move above
# turns a missing contract into a zero count, which reads exactly like a dropped exit.
#
# NOT `reset_tree` HERE. PRISTINE is pinned long before this section's own fixture commit (the
# synthetic engine plus KICKOFF_ENGINE/KICKOFF_EXITS, committed above), so resetting to it does
# not clean the tree -- it DESTROYS the fixture, check 12 is then skipped for want of a declared
# engine, and every arm below reads green while testing nothing. `checkout -- .` keeps the commit.
git checkout -q -- .
rm -f memory/guides/UNATTENDED-PROTOCOL.md
hit "$(run)" "KICKOFF_EXITS declares a floor on the kickoff engine's interactive exits, which now live in the installed protocol, and there is no protocol at"
# Put the deleted half BACK. Check 10 compares the protocol pair unconditionally and returns 2 on
# a missing half, so leaving it deleted makes every later run() emit and the blank-engine arm
# below -- which asserts byte-empty output -- could never pass for the right reason.
git checkout -q -- memory/guides/UNATTENDED-PROTOCOL.md

# ...and the protocol present but carrying NO section 13. The count is declared section-scoped, so a
# protocol without that heading must refuse by name rather than count zero and read as six dropped.
mutate memory/guides/UNATTENDED-PROTOCOL.md 's/^## 13[.] /## 13x /'
hit "$(run)" "KICKOFF_EXITS declares a floor counted in section 13 of the installed protocol, and there is no section 13 heading in"
git checkout -q -- memory/guides/UNATTENDED-PROTOCOL.md

# ...an exit dropped from a `**Step ` item OUTSIDE section 13 must NOT satisfy the floor. The
# count is declared section-scoped in three places; before this arm it ran over the whole file,
# so one such item anywhere could mask a real drop from section 13.
mutate memory/guides/UNATTENDED-PROTOCOL.md '/^## 12[.] /a 9. **Step X** -- a decoy outside section 13.'
mutate memory/guides/UNATTENDED-PROTOCOL.md '/^4\. \*\*Step 2/d'
out=$(run)
hit "$out" "the installed protocol enumerates fewer of the kickoff engine's interactive exits than the floor"
hit "$out" "5 against 6"
git checkout -q -- memory/guides/UNATTENDED-PROTOCOL.md

# ...and a declared engine that is not there. Without this the whole check is skipped by a typo.
git checkout -q -- skills/session-kickoff/SKILL.md
sed -i 's|^KICKOFF_ENGINE=.*|KICKOFF_ENGINE="skills/session-kickoff/NOPE.md"|' .unattended.conf
hit "$(run)" "KICKOFF_ENGINE names a file that does not exist, so the hand-back check reads nothing and passes"

# ...blank turns it off, which is what lets an adopter without the kickoff skill stay green.
sed -i 's|^KICKOFF_ENGINE=.*|KICKOFF_ENGINE=""|' .unattended.conf
same "a blank KICKOFF_ENGINE turns the check off" "$(remove_announcements "$(run)")" ""

# ---- check 1 branch 5: a MALFORMED floor is a refusal, not a skip. Only the wholly UNDECLARED case
# ---- was caught, so `CORE_FLOOR="6"` left BOTH shrink-only pins unenforced while the conf still
# ---- read as configured — the easier half of the same mistake, armed and the harder half not.
reset_tree; sed -i 's/^CORE_FLOOR=.*/CORE_FLOOR="6"/' .unattended.conf
hit "$(run)" "CORE_FLOOR is malformed and both shrink-only floors are therefore unenforced; want two integers separated by a colon"
reset_tree; sed -i 's/^CORE_FLOOR=.*/CORE_FLOOR="six:six"/' .unattended.conf
# ---- check 9 branch 1: an ABSENT `base:` line is the violation, not the exemption. The check was
# ---- wrapped in `if [ -n "$rb" ]`, so deleting one line from a run-WRITABLE file disarmed the only
# ---- BASE assertion on the bar.
sed -i '/^base: /d' memory/builds/tRun/RUN.md; git add -A
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "CORE_FLOOR is malformed and both shrink-only floors are therefore unenforced; want two integers separated by a colon|a run-state file records no BASE, and the record is written by the run — an absent pin is not a satisfied one" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 3/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "CORE_FLOOR is malformed and both shrink-only floors are therefore unenforced; want two integers separated by a colon"
hit "$out" "a run-state file records no BASE, and the record is written by the run — an absent pin is not a satisfied one"

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
same "a LANDED run-state record leaves the bar green" "$(remove_announcements "$out")" ""
same "a LANDED run-state record exits 0" "$rc" "0"
git checkout -q unit; reset_tree


fi   # ---- end REGION 3 -----------------------------------------------------------------------------------

# ---- REGION 4 -----------------------------------------------------------------------------------
if in_shard 4; then
[ "$SH_I" = 4 ] && run_landed_replay   # owed here: the unsharded capture at this line carries unit<main=yes
read_topo 4
reset_tree

# ---- check 14: a replace ref or a graft file is itself the violation. The GIT() pin makes THIS
# ---- leg's reads honest; it binds no other tool reading the same objects.
reset_tree
git update-ref "refs/replace/$(git rev-parse HEAD)" "$(git rev-parse HEAD^)"
hit "$(run)" "a repo carrying an unattended run-state file also carries replace refs, and a replace ref rewrites what a sha MEANS for every read that is not pinned"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi
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
# AN ASSIGNMENT IN A CONDITION COUNTS TOO. Check 42 (TOOL-dDerivedDocket-27) creates its capture dir
# as `elif ! _c42_d=$(mktemp -d …); then`, and a derivation anchored at the line start missed it, so
# the redirect into that scratch read as a write into the tree. Comment lines are dropped first, or a
# header quoting the shape would bless a name nothing assigns.
mkt=$(grep -vE '^[[:space:]]*#' "$HERE/check-unattended.sh" \
      | grep -oE '(^[[:space:]]*|(^|[;&|[:space:]])(if|elif|while|until)[[:space:]]+(![[:space:]]+)?)(local +)?[A-Za-z_][A-Za-z0-9_]*=\$\(mktemp' \
      | sed -E 's/=\$\(mktemp$//; s/^.*[[:space:]!;&|]//' | sort -u)
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

# THE COUNT THE CONTROL ASSERTS IS DECLARED HERE, BY ITS OWN BLOCK (TOOL-aBatchedArm-3 S6): every
# `reset_tree`-led cycle from this line to the control increments MUT, and "nine" is the ARM count,
# not the cycle count — arm 6b alone runs three. Counted from the file, not typed from the note.
MUT=0; MUT_EXPECTED=13
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

# arm 6b: THE BODY TERM (TOOL-aHoistedPass-2). Arm 6 above proves the section EXISTS check; this one
# proves the term that opens it. FOUR FIXTURES, because the block-wise comment strip is the whole
# point of the term and only the fourth separates it from the naive line-prefix filter that was
# measured ADMITTING that evasion.
# every section present, every handle absent from every body -> RED, naming the pair
reset_tree; _bm_sections "" > memory/guides/BUILD-METHOD.md
hit "$(run)" "a directive's cited build-method section states nothing about it, so a run resolving the handle reads that section and finds no rule — absent in backticks outside every HTML comment"
# the anchor present ONLY inside a SINGLE-line HTML comment -> still RED
reset_tree; _bm_sections '
<!-- anchors: `passes-harnessed` `passes-committed` `parallel-when-disjoint` -->' > memory/guides/BUILD-METHOD.md
hit "$(run)" "a directive's cited build-method section states nothing about it, so a run resolving the handle reads that section and finds no rule — absent in backticks outside every HTML comment"
# the anchor present ONLY inside a MULTI-line HTML comment, on its SECOND line -> still RED.
# THIS is the fixture the naive filter passes: it drops the comment's first line and keeps line two.
reset_tree; _bm_sections '
<!-- anchors:
     `passes-harnessed` `passes-committed` `parallel-when-disjoint` -->' > memory/guides/BUILD-METHOD.md
hit "$(run)" "a directive's cited build-method section states nothing about it, so a run resolving the handle reads that section and finds no rule — absent in backticks outside every HTML comment"
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
same "the tree is still clean after nine mutations: every cycle of its block ran in this process" "$MUT" "$MUT_EXPECTED"
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
#
# IT FELL BEHIND ANYWAY, in exactly the way the paragraph above predicts, and this is the repair.
# `TOOL-aHoistedPass-2` landed check 16's BODY term: a section must now name its own handles in
# backticks, not merely exist. A carrier of bare headings satisfies arm B and reds the body term
# SEVENTEEN times, so the green control below - "a tree whose waiver was taken at preflight exits 0"
# - failed on a check-16 message that has nothing to do with waivers. Measured while building
# `TOOL-aHoistedPass-9`, on shard 2/2, with that unit's own edits reverted; the derivation now emits
# each section's handles as well as its heading, and both halves still come out of the registry.
{ printf '# method\n'
  _reg=$(grep -m1 '^DIRECTIVES_CORE=' $KIT_REL/unattended.sh | sed 's/^DIRECTIVES_CORE="//; s/"$//')
  for _sec in $(printf '%s\n' $_reg | cut -d: -f2 | sort -u); do
    printf '\n## %s\n\n' "$_sec"
    for _h in $(printf '%s\n' $_reg | awk -F: -v s="$_sec" '$2 == s { print $1 }'); do printf '`%s` ' "$_h"; done
    printf 'state their rules in this section.\n'
  done
} > memory/guides/BUILD-METHOD.md
n=$((n+1)); [ "$(grep -c '^## M' memory/guides/BUILD-METHOD.md)" -ge 8 ] \
  || { echo "FAIL the derived build-method carrier holds too few sections to satisfy the registry"; st=1; }
# ...and the ANCHORS, counted, because the section list alone is what stopped being enough. Without
# this the fixture can fall behind a THIRD time and the report will again be a message about whatever
# ran next. Both sides derive from the registry, so neither can be typed out of date.
_want_h=$(printf '%s\n' $_reg | grep -c .)
n=$((n+1)); [ "$(grep -oE '`[a-z][a-z-]*`' memory/guides/BUILD-METHOD.md | sort -u | grep -c .)" -ge "$_want_h" ] \
  || { echo "FAIL the derived build-method carrier names fewer directive handles than the registry declares, so check 16's body term reds every arm below it"; st=1; }
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

# GREEN CONTROL: the template this kit actually ships orders the two correctly.
reset_tree; kick_engine
same "the shipped Skill template orders kickoff after preflight" "$(remove_announcements "$(run)")" ""

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
mutate memory/builds/tRun/README.md '/gen:build-units/d'
mutate memory/builds/tPlanOk/README.md '/gen:build-units/d'
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "the Skill template names no --preflight invocation, so there is no anchor to order the kickoff step against and the sequence this check exists to hold is unstated|a tracked build README does not carry exactly one well-formed generated-units marker pair, so the driver cannot read its unit list and no run against it can close|a declared verb is never invoked in the Skill an agent actually reads, so nothing an agent follows would ever call it|the driver returned no verdict for any build this check asked it about, so a clean result here is about a driver path that answered nothing rather than about the corpus" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 4/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "the Skill template names no --preflight invocation, so there is no anchor to order the kickoff step against and the sequence this check exists to hold is unstated"
hit "$out" "the driver returned no verdict for any build this check asked it about, so a clean result here is about a driver path that answered nothing rather than about the corpus"
# ---- AND THIS IS THE ARM THAT EXERCISES THE CANARY. TOOL-aQuenchedHarness-10 gave check 30 a
# ---- selection stage, so on a corpus where nothing is selected the driver would be asked about
# ---- NOTHING and this liveness branch would pass over an empty ask - the exact vacuity it exists
# ---- to catch. One build is therefore graded anyway. Every `--plan` in this fixture refuses, so
# ---- the branch above fires whether the slug came from the selection or from the canary - this
# ---- arm grades that the ask is never EMPTY, not which limb supplied it.

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

# ---- 30 branch 3 (TOOL-aQuenchedHarness-10): the SELECTOR's own liveness. The check no longer
# ---- asks the driver about every build - it scans the spec corpus and asks about the ones that
# ---- can produce a NOT A UNIT row. A scan reading no spec selects nothing, asks nothing, and
# ---- reports clean; that is a second empty population one level above the one branch 1 guards,
# ---- and it needs its own assertion because branch 1 cannot see it.
# ---- The break is the INDEX, not the worktree: the scan enumerates with `git ls-files`, so a
# ---- spec still on disk but no longer tracked is invisible to it - which is also the real shape
# ---- this could take in a live tree.
reset_tree
# UNTRACK THE WHOLE POPULATION, not two builds by name. Naming tRun and tPlanOk left every
# other fixture build's specs tracked, so the scan still read specs, the check never fired,
# and this arm asserted a message the tool had no reason to emit. The fixture-no-op guard
# below is what caught it - which is the entire reason `mutate` and this arm carry one.
git ls-files -z "memory/builds/*/spec/*.md" | xargs -0 -r git rm -q --cached >/dev/null 2>&1
n=$((n+1)); [ -z "$(git ls-files "memory/builds/*/spec/*.md")" ] || { echo "FAIL fixture no-op: specs still tracked"; st=1; }
hit "$(run)" "the spec scan that selects this check's population read no tracked spec at all, so both the selection and the clean result below are about an empty corpus rather than about the builds"

# ---- 30 branch 4 (TOOL-aQuenchedHarness-10): the selector is keyed on TWO patterns copied from
# ---- the driver's own `spec_facts`, and a predicate spelled in two places is one that stops
# ---- selecting when a copy moves. A selector that silently selects nothing reports clean
# ---- forever, so the check greps both literals out of the driver first and REFUSES without them.
# ---- The mutation is anchored on `spec_facts`'s own status action so it moves that one awk
# ---- pattern and nothing else the leg parses out of this file.
reset_tree
mutate $KIT_REL/unattended.sh '/if (st == "")/s/Status:/Stat_us:/'
hit "$(run)" "the driver no longer spells one of the two patterns this check selects its population with, so the selection below is keyed on a predicate the driver has moved away from and would quietly grade nothing"

# ---- 31 (TOOL-aHoistedPass-9): the route the `passes-harnessed` directive names RESOLVES in this
# ---- tree, and every case the check cannot COMPARE announces itself on the REPORT channel instead
# ---- of passing silently. ONE BREAK PER BRANCH plus a green control; the arms are the count and
# ---- no numeral is typed beside them, for the reason the leg's own header now gives.
# ----
# ---- The fixture ships no build-method carrier, so each arm writes one through `_bm_sections` -
# ---- the same helper arm 6b uses. That keeps every OTHER cited section present, so these arms grade
# ---- check 31 rather than grading arm B's missing-section refusal.
# ----
# ---- THE ROUTE PATH IS DERIVED, NEVER SPELLED. `install-prefix` is a BAN on this file, not a
# ---- ratchet: a literal kit path in a shipped body arrives verbatim in a target installed at
# ---- another prefix and resolves to nothing there. Six literal spellings here moved this file's
# ---- ratchet row 3 -> 9 and the gate refused them, correctly. The route's home is the SIBLING of
# ---- this suite's own `KIT_REL`, which is where `mutate` and `cp` already reach the kit under test.
# ---- At a root install `KIT_REL` has no directory part and this resolves to `./workflows`, which
# ---- the check's own `(^|/)workflows/` key still matches and `dirname` still walks.
_c31_dir="$(dirname "$KIT_REL")/workflows"
_c31_route="$_c31_dir/unattended-unit.js"
# The M6 body, built through printf so the BACKTICKS come from a single-quoted format while the path
# comes from the derived variable. A backtick inside a double-quoted string in this suite is command
# substitution, and the fixture would then be written by whatever it ran - the trap `mkconf` carries
# a loud comment about, which cost a 50-minute run to find.

# branch F1, and this is the POSITIVE assertion `fail 31` owes under check-arms: the section names a
# script this tree does not carry while the directory that would hold it IS present, which is a kit
# that was taken and a route that is broken. The kit's own parent exists in the fixture because the
# kit installs under it; the route directory is created by this arm and by nothing else.
reset_tree
_bm31 "$_c31_route"
mkdir -p "$_c31_dir"
hit "$(run)" "a carrier of the harnessed-pass route names a script this tree does not carry while the directory that holds it IS present, so the route's kit was taken and its route is broken: $_c31_route named by memory/guides/BUILD-METHOD.md"

# branch S5, and the split against F1 above IS the ruling: an absent DIRECTORY means the route's kit
# was never installed here, which is an install decision a standing bar cannot undo. It announces on
# REPORT and stays silent on the default channel, which is what makes a skip byte-distinguishable
# from a pass. `govkit apply` is where that same gap is refused, at the act that creates it.
reset_tree
_bm31 "$_c31_route"
miss "$(run)" "check 31"
hit "$(GOV_UNATTENDED_REPORT=1 run)" "check 31 skipped for $_c31_route — the directory that would hold it is absent"

# branch S2, the carrier absent. Check 16 arm B is SILENT on this exact state by design - it guards
# its whole loop on `[ -f … ]` - and this line is the announcement arm B does not make. The fixture
# ships no carrier, so this arm breaks nothing and that is the point: the silent state is the shipped
# one. No `mutate` here for the same reason; there is no file to no-op against.
reset_tree
hit "$(GOV_UNATTENDED_REPORT=1 run)" "check 31 skipped for memory/guides/BUILD-METHOD.md — this tree carries no build-method carrier"

# branch S4, the section resolving but naming no route at all. This is the state of every adopter
# tree whose render predates the M6 route sentence, which is the whole population this check exists
# to reach - so an arm for it is not a corner case, it is the common one.
reset_tree
_bm31
hit "$(GOV_UNATTENDED_REPORT=1 run)" "check 31 skipped for memory/guides/BUILD-METHOD.md — M6 names no backticked route script"

# branches S5 then F1 at a FOREIGN PREFIX, which is what says the verdict follows the named path's
# own `dirname` rather than an install-prefix literal. TOOL_ROOT renders to the empty string at a
# root install, so a literal would be wrong in an adopter tree in BOTH directions - failing a correct
# route installed elsewhere, or skipping forever over a broken one. The route's kit segment is the
# derived one above, so the foreign path types no kit name (TOOL-aRepatriatedFork-30 S8).
_c31_far="vendor/harness/${_c31_dir##*/}/unattended-unit.js"
reset_tree
_bm31 "$_c31_far"
hit "$(GOV_UNATTENDED_REPORT=1 run)" "check 31 skipped for $_c31_far — the directory that would hold it is absent"
mkdir -p "$(dirname "$_c31_far")"
hit "$(run)" "so the route's kit was taken and its route is broken: $_c31_far"

# branch S1, the registry itself unreadable, so the section holding the route is unnamed. Reached by
# EMPTYING the driver's core set rather than by `--only 28`: that flag leaves `$core` unset for the
# same reason, but the leg dies at check 30's `MEMORY_ROOT: unbound variable` twenty lines earlier
# and check 31 never runs. Measured at e828f778, filed as TOOL-aHoistedPass-37, not this unit's.
reset_tree
mutate $KIT_REL/unattended.sh 's/^DIRECTIVES_CORE=.*/DIRECTIVES_CORE=""/'
hit "$(GOV_UNATTENDED_REPORT=1 run)" "— the directive registry names no passes-harnessed handle this leg can read"
miss "$(run)" "check 31"

# ---- THE SECOND CARRIER (closing-review F6). Check 31 read the build-method render alone, so the
# ---- Skill - the carrier an agent actually reads, and the one that mandates `scriptPath` calls -
# ---- was graded by nothing, while it spelled the same two scripts as install-prefix LITERALS that
# ---- resolve to nothing at a root install. A check added to catch an unresolvable route, passing
# ---- over exactly the half that had one. These arms are the same three branches as above, driven
# ---- through the Skill instead, so a future edit cannot re-narrow the subject without redding.
# ----
# ---- THE SKILL IS WRITTEN, NOT RENDERED. The fixture's kit ships `SKILL.template.md` and no
# ---- adopter has run here, so `.claude/skills/unattended/SKILL.md` is genuinely absent - which is
# ---- branch S6's own fixture and is why that arm needs no break. `printf` with a single-quoted
# ---- format for the same reason `_bm31` uses one: a backtick inside a double-quoted string in this
# ---- suite is command substitution.
_c31_skill=".claude/skills/unattended/SKILL.md"

# branch S6, the Skill absent. The fixture ships no render, so this state is the shipped one and the
# arm breaks nothing - the point being that the announcement exists at all, where before this the
# whole carrier was silent by omission rather than by a stated skip.
reset_tree
hit "$(GOV_UNATTENDED_REPORT=1 run)" "check 31 skipped for .claude/skills/unattended/SKILL.md — this tree carries no rendered Skill"

# branch S7, the Skill present and naming no route: every adopter whose render predates the bullet.
reset_tree
_mkskill
hit "$(GOV_UNATTENDED_REPORT=1 run)" "check 31 skipped for .claude/skills/unattended/SKILL.md — the rendered Skill names no backticked route script"

# branch F1 THROUGH THE SKILL, which is the arm that says the widening actually grades: the same
# broken route, named only by the Skill, with the build-method carrier absent entirely. The message
# names its own carrier, so the two halves are distinguishable in a failing run rather than merged.
reset_tree
_mkskill "$_c31_route"
mkdir -p "$_c31_dir"
hit "$(run)" "a carrier of the harnessed-pass route names a script this tree does not carry while the directory that holds it IS present, so the route's kit was taken and its route is broken: $_c31_route named by $_c31_skill"

# ...and the GREEN CONTROL, which is the arm that makes the announcing ones mean anything: with the
# route actually resolving in BOTH carriers, check 31 says nothing on EITHER channel. Without it,
# every arm above is equally consistent with a check that announces unconditionally. The Skill is
# seeded here too - leave it out and the S6 announcement fires and this control reds, which is the
# correct behaviour and would make the control a test of the fixture.
reset_tree
_bm31 "$_c31_route"
_mkskill "$_c31_route"
mkdir -p "$_c31_dir" && : > "$_c31_route"
miss "$(GOV_UNATTENDED_REPORT=1 run)" "check 31"
reset_tree

# ---- 32 (TOOL-aWokenSentinel-11): the kit holds ONE derivation of the sidecar root, on a CODE
# ---- line of the library, and the driver reads every sidecar through it. The fixture's driver and
# ---- library are copies of the shipped pair, so the pristine tree counts one spelling in the lib,
# ---- none in the driver and one caller, and the arms below move exactly one of those three.
# ---- The break is the shape the spec-audit finding named: a second `$(GIT rev-parse --git-dir)`
# ---- spelled inline inside `verb_status`, which is where one spec of that build had put it.
# ---- The arm carries the ENTIRE literal signature up to the first interpolation plus the count
# ---- the refusal prints, so it reads the refusal's number and not only its sentence.
reset_tree
mutate $KIT_REL/unattended.sh '/^verb_status() {/a\  _x=$(GIT rev-parse --git-dir)/unattended'
hit "$(run)" "the kit must hold ONE derivation of the sidecar root — resolve_sidecar_dir, in lib-unattended.sh — and the driver must read every sidecar through it; a second 'rev-parse --git-dir' on a code line of the driver, the lib or the tick is a second spelling that drifts from the first, and zero is a reader with no derivation. code-line count: 2"
# ...the NEAR-MISS, and it is a control on the predicate rather than a second break: the same line
# as a COMMENT is not a spelling, because the driver's idiom is a prose header beside every function
# and a header that names the rule is right. The check's own header says a commented-out second
# derivation passes until the edit that uncomments it, and this arm is that sentence, observed.
reset_tree
mutate $KIT_REL/unattended.sh '/^verb_status() {/a\  # _x=$(GIT rev-parse --git-dir)/unattended'
miss "$(run)" "check 32"
# ...and ZERO CALLERS is the other direction of the same refusal: a derivation nothing calls is a
# function that exists for the grep. The one call site is deleted and the count the refusal prints
# is read, so an `at most one` predicate — which would pass this copy — cannot pass this arm.
reset_tree
mutate $KIT_REL/unattended.sh 's|[$](resolve_sidecar_dir)|$(true)|g'
hit "$(run)" "driver callers: 0"
reset_tree

# ---- 33 (TOOL-aWokenSentinel-23): no shell file in the kit counts a captured variable's lines by
# ---- adding a newline before the count. The fixture's kit holds no suite, so the arm copies the
# ---- DRIVER SUITE in — the file the instance lived in, and the one the check's own population must
# ---- read where KIT_SH does not — and stages the banned count inside a function body. THE STAGED
# ---- LINE IS ASSEMBLED FROM FRAGMENTS: the command word split and the variable joined at run time,
# ---- written to a file and spliced in by sed's `r`, so this suite never carries the banned bytes
# ---- contiguously on a code line and the checker's by-name exclusion of this file is a second guard
# ---- rather than the only one. (A quoted heredoc would put those exact bytes on a code line the
# ---- `^[^#]*` predicate matches, and sed's `a` processes escapes, so `\n` in the text would become a
# ---- newline — `r` copies the file verbatim.) The arm carries the ENTIRE literal signature up to
# ---- the first interpolation, and reads the file the refusal names.
reset_tree
cp "$HERE/unattended.test.sh" $KIT_REL/
_lc_cmd="pri""ntf"; _lc_var='"$_o"'
_lc_line="  _x=\$($_lc_cmd '%s\\n' $_lc_var | wc -l)"
printf '%s\n' "$_lc_line" > "$TMPBIN_PARENT/lc.line"
mutate $KIT_REL/unattended.test.sh "/^check_status_one_line() {/r $TMPBIN_PARENT/lc.line"
out=$(run)
hit "$out" "a shell file in this kit counts a captured variable's lines by adding a newline first — printf '%s\n', echo or a here-string into wc -l — which reads an EMPTY capture as one line, so an assertion on the count passes on a command that wrote nothing; count with printf '%s' \"\$x\" | grep -c '' instead, which reads empty as 0. hits: unattended.test.sh:"
hit "$out" "UNATTENDED check 33 FAILED"
# ...the NEAR-MISS, a control on the predicate rather than a second break: the same count WITHOUT the
# added newline is the driver's own idiom — it counts embedded newlines and reads an empty capture
# as 0 — and the check's header says it is not a hit. This arm is that sentence,
# observed; without it the arm above is equally consistent with a ban on every `| wc -l`.
reset_tree
cp "$HERE/unattended.test.sh" $KIT_REL/
_lc_line="  _x=\$($_lc_cmd '%s' $_lc_var | wc -l)"
printf '%s\n' "$_lc_line" > "$TMPBIN_PARENT/lc.line"
mutate $KIT_REL/unattended.test.sh "/^check_status_one_line() {/r $TMPBIN_PARENT/lc.line"
miss "$(run)" "check 33"
# ...and the RESTORED copy: the shipped driver suite, unmodified, in the population. This is the
# reading that says spec 17's `grep -c ''` fold actually landed — a suite still carrying the
# instance would red here, on every bar, naming its own line.
reset_tree
cp "$HERE/unattended.test.sh" $KIT_REL/
miss "$(run)" "check 33"
reset_tree
# ---- 33, THE OTHER TWO SPELLINGS (TOOL-aWokenSentinel-28): the predicate has three branches and the
# ---- arm above stages only `printf '%s\n'`. The `echo` spelling shares the first group and the
# ---- here-string is a separate top-level alternation with the variable AFTER `wc -l`, so a
# ---- mis-escaped `<<<` branch passed every reading above. Each is staged here by the same
# ---- fragment-assembled splice, read RED naming the copy's basename AND line, then DELETED from
# ---- that copy by a second `mutate` and read GREEN — a fresh copy would be the restored reading
# ---- above, and would not say the red was this line. `_lc_at` is the line the splice lands on.
reset_tree
cp "$HERE/unattended.test.sh" $KIT_REL/
_lc_at=$(( $(grep -n '^check_status_one_line() {' $KIT_REL/unattended.test.sh | cut -d: -f1) + 1 ))
_lc_cmd="ec""ho"
_lc_line="  _x=\$($_lc_cmd \"\$_o\" | wc -l)"
printf '%s\n' "$_lc_line" > "$TMPBIN_PARENT/lc.line"
mutate $KIT_REL/unattended.test.sh "/^check_status_one_line() {/r $TMPBIN_PARENT/lc.line"
out=$(run)
hit "$out" "counts a captured variable's lines by adding a newline first"
hit "$out" "hits: unattended.test.sh:$_lc_at:"
mutate $KIT_REL/unattended.test.sh '/^check_status_one_line() {/{n;d;}'
miss "$(run)" "counts a captured variable's lines by adding a newline first"
# ...the HERE-STRING, the second top-level alternation. `<<""<` joins to `<<<` at run time.
reset_tree
cp "$HERE/unattended.test.sh" $KIT_REL/
_lc_line="  _x=\$(wc -l <<""< \"\$_o\")"
printf '%s\n' "$_lc_line" > "$TMPBIN_PARENT/lc.line"
mutate $KIT_REL/unattended.test.sh "/^check_status_one_line() {/r $TMPBIN_PARENT/lc.line"
out=$(run)
hit "$out" "counts a captured variable's lines by adding a newline first"
hit "$out" "hits: unattended.test.sh:$_lc_at:"
mutate $KIT_REL/unattended.test.sh '/^check_status_one_line() {/{n;d;}'
miss "$(run)" "counts a captured variable's lines by adding a newline first"
# ...and the here-string CONTROL: a here-string that is not a count. Without it the arm above is
# equally consistent with a `<<<` branch escaped so loosely it bans every here-string in the kit.
reset_tree
cp "$HERE/unattended.test.sh" $KIT_REL/
printf '%s\n' '  read -r _y <<< "$_o"' > "$TMPBIN_PARENT/lc.line"
mutate $KIT_REL/unattended.test.sh "/^check_status_one_line() {/r $TMPBIN_PARENT/lc.line"
miss "$(run)" "counts a captured variable's lines by adding a newline first"
reset_tree

# ---- 36 (TOOL-aRepatriatedFork-6, closing review round 2 M1): every run-state key read routes
# ---- through the `## Run facts` section. The staged break is the instance the round found:
# ---- `baseline_units`' phase probe with its section filter removed, the whole-file first match
# ---- round 1 L2 left behind. Read RED naming the library's line, then the shipped copy GREEN.
reset_tree
mutate $KIT_REL/lib-unattended.sh 's#| extract_run_facts | grep -m1 #| grep -m1 #'
out=$(run)
hit "$out" "a run-state key is read over the whole file rather than the Run facts section, so it can answer a line above the heading or under Parked that the driver's fact never reads - route it through fact, fact_of or extract_run_facts: lib-unattended.sh:"
hit "$out" "UNATTENDED check 36 FAILED"
reset_tree
miss "$(run)" "UNATTENDED check 36 FAILED"
# ...and a STALE exemption: the driver's spec-audit front-matter read removed, so the registry row
# naming it matches nothing in a file the population holds.
reset_tree
mutate $KIT_REL/unattended.sh '/print "spec-audit=" v/d'
hit "$(run)" "a run-state read exemption matches no read in the kit, and a stale exemption silently widens the surface it was written to narrow; unattended.sh ^spec-audit:"
reset_tree
# ...and the two LIVENESS refusals, each reached by removing what it asserts is there. No scoped read
# at all: EVERY section-filtered read in the fixture kit respelled unscoped, `extract_run_facts`
# before a pipe or a redirect as `cat` and an awk `sec && /…/` guard without its `sec &&`. This arm
# named the kit's two such reads one by one; dDerivedDocket took the fixture kit to six, across the
# library, this leg and the driver, so the four it did not name kept the scan live and the refusal
# never fired. The report's count is read first, so a scoped read the respelling misses reds here
# as a count, not as a missing refusal. RAISED the floors by 2: one `mutate` more and that `hit`.
for _sf in lib-unattended.sh check-unattended.sh unattended.sh; do
  mutate $KIT_REL/$_sf '/^[[:space:]]*#/!{s/extract_run_facts\([[:space:]]*[|<]\)/cat\1/g; s/\([^A-Za-z_]\)sec *&& *\//\1\//g;}'
done
out=$(GOV_UNATTENDED_REPORT=1 run)
hit "$out" " anchored reads, 0 scoped to the Run facts section, "
hit "$out" "no key read in the kit carries the Run facts scope, so the scan matched nothing it was written to find and a clean result would be coverage of nothing"
reset_tree
# No `phase` key derived: every `fact`/`set_fact`/`fact_of` call naming it respelled.
mutate $KIT_REL/unattended.sh 's/\(fact[a-z_]* "[^"]*"\) phase/\1 phaze/g'
mutate $KIT_REL/check-unattended.sh 's/\(fact[a-z_]* "[^"]*"\) phase/\1 phaze/g'
hit "$(run)" "the run-state key derivation found no phase key, so the read scan grades against nothing: "
reset_tree

# ---- 21 (TOOL-aBoundedVerdict-11 S5): the generated-units pair is REQUIRED on every tracked build
# ---- README. The corpus is clean, so a check with no red fixture here proves nothing - it would be
# ---- silent whether the predicate worked or not, which is the class this kit keeps meeting.
reset_tree
mutate memory/builds/tRun/README.md '/gen:build-units/d'
# The arm carries the ENTIRE literal signature up to the first interpolation, not a readable prefix:
# check-arms grades a branch on the whole thing, and a prefix reds. That is also why the remedy is
# part of THIS assertion rather than a second one - the remedy is inside the same literal.
hit "$(run)" "a tracked build README does not carry exactly one well-formed generated-units marker pair, so the driver cannot read its unit list and no run against it can close; repair with the --write mode of $MT_REL/gen_build_index.py"

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
same "a blank KICKOFF_ENGINE turns check 18 off even on a transposed template" "$(remove_announcements "$(run)")" ""
reset_tree

# ---- 34 (TOOL-aRepatriatedFork-6 AC5): a Run facts key carried twice with two DIFFERENT values is a
# ---- fact nothing wrote, because every reader takes the first match. The forgery's own shape: a
# ---- `phase: LANDED` inserted directly under the heading, above the real `phase: RUNNING`.
reset_tree
mutate memory/builds/tRun/RUN.md '/^## Run facts/a phase: LANDED'
out=$(run)
hit "$out" "UNATTENDED check 34 FAILED — a run-state file carries one Run facts key twice with two different values, and every reader takes the first match, so one of them is a fact nothing wrote: memory/builds/tRun/RUN.md: phase is [LANDED] and [RUNNING]"
# ...the NEAR-MISS control: a SAME-value repeat forges nothing (the first match gives the same
# answer) and is the shape of the one hand repair in gov's tree, so the rule is not "any repeat".
reset_tree
mutate memory/builds/tRun/RUN.md '/^## Run facts/a phase: RUNNING'
out=$(GOV_UNATTENDED_REPORT=1 run)
miss "$out" "UNATTENDED check 34 FAILED"
hit "$out" "check 34 graded "
# ---- L2 (closing review round 1): the readers check 34 protects are scoped to the SAME section it
# ---- grades. A terminal phase ABOVE the heading was read ahead of the real `phase: RUNNING` while
# ---- check 34 reported clean. This fixture carries no halt-code, so an ABORTED read surfaces as the
# ---- halt-vocabulary refusal; the control below is that refusal firing on the in-section phase.
reset_tree
mutate memory/builds/tRun/RUN.md '1a phase: ABORTED'
out=$(run)
miss "$out" "memory/builds/tRun/RUN.md (phase ABORTED and no halt-code fact"
reset_tree
mutate memory/builds/tRun/RUN.md 's/^phase: RUNNING$/phase: ABORTED/'
hit "$(run)" "memory/builds/tRun/RUN.md (phase ABORTED and no halt-code fact, so the record says a run stopped and never says why)"
reset_tree

# ---- check 16 arms D and E: the CONTRACT's two tables joined to the constants the driver enforces.
# ---- Both edits go to BOTH protocol copies, or check 15's parity fires and the arm would be
# ---- satisfied by a refusal that has nothing to do with the join it is testing.
# Through `mutate`, so a locator that stops matching after a document reword FAILS here instead of
# silently turning six arms into six no-ops that still read as tests.

# GREEN CONTROL: the shipped contract already agrees with the driver in both tables.

fi   # ---- end REGION 4 -----------------------------------------------------------------------------------

# ---- REGION 5 -----------------------------------------------------------------------------------
if in_shard 5; then
read_topo 5
reset_tree
same "the shipped protocol's two tables join clean" "$(remove_announcements "$(run)")" ""
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi

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
reset_tree; pedit 's/^[A-Z][a-z]* kit-owned core items\./Six kit-owned core items./'
hit "$(run)" "the protocol's stated count of core Definition-of-Done items disagrees with the set the driver enforces, and that sentence sits directly above the table it miscounts: says '"

# ...and the sentence gone entirely. Absence is its own refusal for the reason every locator here
# has one: a summary nobody can find is a summary nobody can join.
reset_tree; pedit 's/^[A-Z][a-z]* kit-owned core items\. //'
hit "$(run)" "the protocol states no count of kit-owned core Definition-of-Done items, so the sentence that summarises the table cannot be joined to the table or to the driver"
reset_tree

# ---- E, THE COUNT WORD TABLE PAST TWELVE (TOOL-dDerivedDocket-17). The table stopped at `twelve`,
# ---- which was exactly the size of the core set — so the FIRST correct sentence written after the
# ---- thirteenth item landed mapped to -1 and red the leg for stating the right number.
# ----
# ---- THE WORD IS READ FROM THE SHIPPED CONTRACT, never typed into the arm. A locator spelling last
# ---- month's count is a `mutate` no-op, and the two arms directly above this one are exactly that:
# ---- they say `Ten` over a contract that has said `Twelve` and now says `Thirteen`. Deriving it is
# ---- what keeps this arm from joining them the next time an item lands.
reset_tree
_c16cw=$(sed -n 's/^\([A-Za-z]*\) kit-owned core items\..*/\1/p' $KIT_REL/PROTOCOL.template.md | head -1)
same "the shipped contract states a count word at all" \
  "$(printf '%s\n' "$_c16cw" | grep -c '^[A-Za-z][A-Za-z]*$' || true)" "1"
same "...and the word table READS that word rather than mapping it to -1" \
  "$(run | grep -c 'stated count of core Definition-of-Done items disagrees' || true)" "0"
# ...and the boundary still refuses a word the table cannot read, or the arm above is satisfied by a
# table that maps everything to something.
reset_tree; pedit "s/^$_c16cw kit-owned core items\./Thirtyone kit-owned core items./"
hit "$(run)" "the protocol's stated count of core Definition-of-Done items disagrees with the set the driver enforces, and that sentence sits directly above the table it miscounts: says '"

# ---- E, the new item's OWN row: the thirteenth item is enforced by --close, so a contract that
# ---- does not publish it blocks a run on something nobody was told about.
reset_tree; pedit '/^| `asks-disposed` |/d'
out=$(run)
hit "$out" "a CORE Definition-of-Done item is enforced by --close and absent from the protocol's table, so a run is blocked by an item the contract never told anyone about"
hit "$out" "asks-disposed"
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

# GREEN CONTROL: undeclared is the empty set, an adopter's ordinary case, and is what keeps this
# change from reddening anyone who uses no extras.
reset_tree
same "an undeclared row source changes nothing" "$(remove_announcements "$(run)")" ""

# ...an extra handle with NO row source is REFUSED now, where it was silently waivable.
reset_tree; mutate .unattended.conf 's/^DIRECTIVES_EXTRA=""$/DIRECTIVES_EXTRA="house-style:M9"/'
hit "$(run)" "a directive is declared in the registry and absent from the Skill's table, so the agent that reads the table is bound by a set it was never shown: house-style:M9"

# ...and with a row source that CARRIES it, the project is whole again: declared, shown, waivable.
mutate .unattended.conf 's|^DIRECTIVES_EXTRA_TABLE=""$|DIRECTIVES_EXTRA_TABLE="memory/project/extra-directives.md"|'
mkdir -p memory/project
printf '| Handle | What it points at | Method | Directive |\n|---|---|---|---|\n| `house-style` | the prose rules this project adds | M9 | P1 |\n' > memory/project/extra-directives.md
same "declared + shown is silent" "$(remove_announcements "$(run)")" ""

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

# ---- AN EXTRA HANDLE IS GRADED FOR EXISTENCE AND NOT FOR BODY (closing-review F3). The body term
# ---- looped `core` - core PLUS extra - while its own rationale promised CORE-ONLY, so an adopter
# ---- who used the documented `DIRECTIVES_EXTRA` knob got a permanent `fail 16` on a carrier the
# ---- memory-tree kit ships as `role = "rendered"` and the doc-parity leg byte-compares. No route
# ---- to green, on an unguarded merge-bar leg.
# ----
# ---- THE FIXTURE MUST HAVE THE CARRIER, and that is the reusable half. `declared + shown is
# ---- silent` above runs after a `reset_tree` that leaves no `BUILD-METHOD.md`, so the term's own
# ---- `[ -f … ]` guard makes it silent whatever it iterates: that arm passed on the broken code and
# ---- on the fixed code alike. Any arm exercising a `[ -f ]`-guarded term must assert the file is
# ---- there first, or it is testing the guard.
# ----
# ---- THE CONTROL IS A CORE HANDLE CITING THE SAME SECTION. `wrap-up-derived:M9` and
# ---- `house-style:M9` read the same empty M9 body; the only difference between them is core versus
# ---- extra. So the `hit` proves the term is LIVE on this exact fixture and the `miss` proves it
# ---- stops at the core set - which no pair of separate fixtures could establish.
reset_tree
mutate .unattended.conf 's/^DIRECTIVES_EXTRA=""$/DIRECTIVES_EXTRA="house-style:M9"/'
mutate .unattended.conf 's|^DIRECTIVES_EXTRA_TABLE=""$|DIRECTIVES_EXTRA_TABLE="memory/project/extra-directives.md"|'
mkdir -p memory/project
printf '| Handle | What it points at | Method | Directive |\n|---|---|---|---|\n| `house-style` | the prose rules this project adds | M9 | P1 |\n' > memory/project/extra-directives.md
_bm_sections "" > memory/guides/BUILD-METHOD.md
n=$((n+1)); [ -f memory/guides/BUILD-METHOD.md ] \
  || { echo "FAIL fixture: no build-method carrier, so the term under test is guarded off and this arm proves nothing"; st=1; }
out=$(run)
hit  "$out" "a directive's cited build-method section states nothing about it, so a run resolving the handle reads that section and finds no rule — absent in backticks outside every HTML comment: wrap-up-derived:M9"
miss "$out" "absent in backticks outside every HTML comment: house-style:M9"
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

# MOVE 1 — a COPY appears in the run-state region, which is what every pre-redesign record holds.
# Collides with check 8. On a TERMINAL record it must be silent: no verb can empty that region once
# the run has ended, so reddening it would be a wedge with no exit.
reset_tree; frozen
mutate memory/builds/tRun/RUN.md '/<!-- run:generated -->/a | [ARCH-tRun-1 — the unit](spec/one.md) | OPEN | rev-1 | 2026-08-01 |'
out=$(run)
miss "$out" "a run-state file's generated region carries a COPY of the unit list"
# Through the announcement filter, for the reason the terminal-copy control in check 8's block gives.
same "move 1 leaves a terminal record green" "$(remove_announcements "$(run; echo $?)")" "0"

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

fi   # ---- end REGION 5 -----------------------------------------------------------------------------------

# ---- REGION 6 -----------------------------------------------------------------------------------
if in_shard 6; then
read_topo 6
reset_tree
git commit -q --allow-empty -m unit-only --no-verify
sed -i "s|^base: .*|base: $(git rev-parse HEAD)|" memory/builds/tRun/RUN.md
git add -A >/dev/null
hit "$(run)" "a run's recorded BASE is not on the branch the remote calls its default, so it came from the second anchor, while the build README there declares a mode whose discipline is that the folder already existed: mode"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi

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

# ---- TOOL-aHomedAnchor-2: THE LOCAL ANCHOR, opted into on the REMOTE's default branch. The base is a
# ---- commit on `unit` that no remote tip carries, which is what the driver's local anchor pins.
# ---- AC1 and AC4: origin's conf declares `local`, so check 9 admits the base and check 29, whose
# ---- `slug` README sits on that off-default base, stays silent.
anchor_break add_local_scope
# ---- TOOL-aHomedAnchor-7 AC4: a record whose BASE is on the default branch prints no check 29 skip.
miss "$(GOV_UNATTENDED_REPORT=1 run)" "check 29 skipped for"
git commit -q --allow-empty -m unit-only --no-verify
_hb=$(git rev-parse HEAD)
sed -i "s|^base: .*|base: $_hb|" memory/builds/tRun/RUN.md
git add -A >/dev/null
out=$(GOV_UNATTENDED_REPORT=1 run)
hit  "$out" "check 9 admitted by the local anchor — a recorded BASE no remote tip carries, on HEAD's history, in a repo whose default-branch conf declares ANCHOR_SCOPE=local: "
miss "$out" "a recorded BASE is not published on the remote — it is an ancestor of no tip the remote advertises, so it names a commit that exists only where this run could have authored it: recorded"
miss "$out" "a run's recorded BASE is not on the branch the remote calls its default, so it came from the second anchor, while the build README there declares a mode whose discipline is that the folder already existed: mode"
# ---- AC3: the same opt-in does not admit a base off HEAD's history.
off=$(git commit-tree "$(git rev-parse 'HEAD^{tree}')" -m "a commit off this working history")
sed -i "s|^base: .*|base: $off|" memory/builds/tRun/RUN.md
git add -A >/dev/null
hit  "$(run)" "a recorded BASE is not published on the remote — it is an ancestor of no tip the remote advertises, so it names a commit that exists only where this run could have authored it: recorded $off"
# ---- TOOL-aHomedAnchor-7 AC1: back on the local-admitted base, a pinned may: grant and a pinned
# ---- asks: mandate each red, because a slug mode no longer proves the first anchor there.
sed -i "s|^base: .*|base: $_hb|" memory/builds/tRun/RUN.md
sed -i '/^base: /a may: memory/notes.md' memory/builds/tRun/RUN.md
sed -i '/^base: /a asks: EXMP-aFoo-3' memory/builds/tRun/RUN.md
git add -A >/dev/null
out=$(run)
hit  "$out" "a run-state file pins a may: grant on a BASE the local anchor admitted, a commit on this node the run could have written, so the grant could be one the run wrote for itself - ruling D12-j honours a grant only from a slug README the owner committed at the default-branch anchor: may: [memory/notes.md] in "
hit  "$out" "a run-state file pins an asks: mandate on a BASE the local anchor admitted, a commit on this node the run could have written, so the mandate and the tree it is asserted against could both be this run's own: "
anchor_restore
# ---- AC2: `local` in the WORKING TREE only, the remote's default branch unchanged, admits nothing.
reset_tree
add_local_scope
git add -A >/dev/null && git commit -q -m unit-only --no-verify
sed -i "s|^base: .*|base: $(git rev-parse HEAD)|" memory/builds/tRun/RUN.md
git add -A >/dev/null
out=$(GOV_UNATTENDED_REPORT=1 run)
hit  "$out" "a recorded BASE is not published on the remote — it is an ancestor of no tip the remote advertises, so it names a commit that exists only where this run could have authored it: recorded"
miss "$out" "check 9 admitted by the local anchor"
reset_tree
# ---- TOOL-aHomedAnchor-7 AC2: LOCAL REFS carrying `local` - refs/heads/main and the remote-tracking
# ---- ref moved to a commit that declares it, never pushed - admit nothing: the leg reads the
# ---- advertisement, which still names the strict conf.
git checkout -q main
add_local_scope; git add -A >/dev/null && git commit -q -m side --no-verify; _side=$(git rev-parse HEAD)
git checkout -q unit
git update-ref refs/remotes/origin/main "$_side"
git commit -q --allow-empty -m unit-only --no-verify
sed -i "s|^base: .*|base: $(git rev-parse HEAD)|" memory/builds/tRun/RUN.md
git add -A >/dev/null
out=$(GOV_UNATTENDED_REPORT=1 run)
hit  "$out" "a recorded BASE is not published on the remote — it is an ancestor of no tip the remote advertises, so it names a commit that exists only where this run could have authored it: recorded"
miss "$out" "check 9 admitted by the local anchor"
git update-ref refs/heads/main "$ANCHOR0"
reset_tree
# ---- AC3: the reader's shapes. `export` is an assignment, an expansion reads strict, the last wins.
eval "$(sed -n '/^read_origin_scope() {/,/^}/p' "$SCRIPT")"
same "aHomedAnchor-7 AC3 an export prefix reads local" "$(read_origin_scope 'export ANCHOR_SCOPE="local"')" "local"
same "aHomedAnchor-7 AC3 an expansion reads strict" "$(read_origin_scope 'ANCHOR_SCOPE="${X:-local}"')" ""
same "aHomedAnchor-7 AC3 a backtick on any assignment reads strict" "$(read_origin_scope "$(printf 'ANCHOR_SCOPE=local\nANCHOR_SCOPE=`true`')")" ""
same "aHomedAnchor-7 AC3 the last plain assignment wins" "$(read_origin_scope "$(printf 'ANCHOR_SCOPE=local\nANCHOR_SCOPE="published"')")" "published"

# ---- the DECLARATION SEAM second-opinioned. The record claims a
# ---- playbook and a count the README at its own BASE does not declare. Two branches, two
# ---- fixtures, because one arm asserting either message would pass on whichever fired.
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
reset_tree; mutate $KIT_REL/SKILL.template.md 's/| M7 | recipe | D11 |/| M7 | all | D11 |/'
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
mutate $KIT_REL/SKILL.template.md 's/^4\. \*\*Commit, then PUSH THE BRANCH\*\*.*/4. **Commit.**/'
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
# I, review L3: a pass kind outside the vocabulary. The both-ways join to the protocol cannot see it
# - both sides would agree on the same wrong token, which is the two-derived-values class.
mutate $KIT_REL/unattended.sh 's/^PHASES_PASSKIND="SPECCING /PHASES_PASSKIND="INVENTED /'
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "a directive is declared in the registry and absent from the Skill's table, so the agent that reads the table is bound by a set it was never shown|a project-declared directive carries a SCOPE, and the scope is kit-owned because a project-selectable one is a narrowing of the core wearing another name|a phase is published as a build-method pass kind and is not in the core vocabulary, so the contract names a position no run can ever occupy|the driver publishes a phase as a build-method pass kind and the protocol does not list it, so the contract understates which positions the method names|the protocol lists a phase as a build-method pass kind that the driver does not publish as one, so the contract claims the method names a position it does not" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 6/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "a project-declared directive carries a SCOPE, and the scope is kit-owned because a project-selectable one is a narrowing of the core wearing another name:"
hit "$out" "a phase is published as a build-method pass kind and is not in the core vocabulary, so the contract names a position no run can ever occupy:"
reset_tree

# ---- the proposal-kind unit: check 26, the VERB SET across the documents that spell it. Each arm
# ---- removes ONE carrier and asserts THIS check speaks, because a leg that reds on everything arms
# ---- every branch and checks nothing.
reset_tree; mutate $KIT_REL/unattended.sh '/^#   unattended[.]sh --propose /d'
# The VERB CARRIER, which is where the entries live after TOOL-dFoldedVerdict-5. BOTH copies, so
# check 10's byte-parity arm does not fire alongside and leave two messages where the arm under test
# is one of them.
mutate $KIT_REL/VERBS.template.md '/^- .--propose. — writes a PROPOSAL/d'
mutate memory/guides/UNATTENDED-VERBS.md '/^- .--propose. — writes a PROPOSAL/d'
out=$(GOV_UNATTENDED_REPORT=1 run)
# THE THIRD SIGNATURE is check 26's flag join (TOOL-dDerivedDocket-30 S5): the deleted header line
# was the only one naming `--propose` and `--step`, so both are now parsed and documented nowhere.
check_emitted "a declared verb is absent from the driver's own header, and the usage text is RENDERED from that header, so the verb has no documented arguments anywhere a reader looks|a declared verb has no entry in the verb carrier, so the contract a run is measured against does not describe a verb that run can call|the driver's parser accepts a flag no header line documents, and the usage text is rendered from that header, so the argument reaches no reader" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 6/8 at 72f54937 (aBatchedArm landing step 0); third signature OBSERVED 2026-09-29 node d, attributed run of shard 6/8 at 8331469c
hit "$out" "a declared verb is absent from the driver's own header, and the usage text is RENDERED from that header, so the verb has no documented arguments anywhere a reader looks:"
hit "$out" "a declared verb has no entry in the verb carrier, so the contract a run is measured against does not describe a verb that run can call:"

# The carrier ABSENT. Its own named refusal, because the guard it replaced was `[ -f X ] && read X`
# with no else — which skips the whole join in silence and reports a green that means nothing. This
# arm accepts that check 10's missing-half branch speaks too: `hit` asserts the message under test is
# PRESENT, and the alternative is a fixture that cannot reach the state at all.
reset_tree; rm -f $KIT_REL/VERBS.template.md
mutate $KIT_REL/SKILL.template.md 's|unattended[.]sh --propose <slug>|unattended.sh --nothing <slug>|'
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "one half of the verb-carrier pair is missing, and a parity check with one file is a check that cannot fail|the verb carrier is absent, so the arm that joins every declared verb to the contract cannot run and would otherwise skip in silence|a declared verb is never invoked in the Skill an agent actually reads, so nothing an agent follows would ever call it" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 6/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "the verb carrier is absent, so the arm that joins every declared verb to the contract cannot run and would otherwise skip in silence"
hit "$out" "a declared verb is never invoked in the Skill an agent actually reads, so nothing an agent follows would ever call it:"

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

fi   # ---- end REGION 6 -----------------------------------------------------------------------------------

# ---- REGION 7 -----------------------------------------------------------------------------------
if in_shard 7; then
read_topo 7
reset_tree; mutate $KIT_REL/SKILL.template.md '/^## Which path$/,/^## Start a run$/s/| `recipe` |/| `slug` |/'
hit "$(run)" "the driver declares an authorization mode that no routing row names, so a build may legally declare a mode the Skill never tells anyone how to start: recipe against"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi

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
mutate $KIT_REL/check-playbook.sh '/^declared_list() {/,/^}/ s|raw=\${_l%%\[\[:space:\]\]#\*}|raw=${_l}|'
mutate $KIT_REL/unattended.sh     '/^declared_list() {/,/^}/ s|raw=\${_l%%\[\[:space:\]\]#\*}|raw=${_l}|'
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
mutate $KIT_REL/check-playbook.sh '/^declared_scalar() {/,/^}/ s|_v=\${_l%%\[\[:space:\]\]#\*}|_v=${_l}|'
mutate $KIT_REL/unattended.sh     '/^declared_scalar() {/,/^}/ s|_v=\${_l%%\[\[:space:\]\]#\*}|_v=${_l}|'
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
mutate $KIT_REL/check-playbook.sh '/^declared_scalar() {/,/^}/ s|_v=\${_l%%\[\[:space:\]\]#\*}|case $_l in *#*) continue ;; esac; _v=${_l}|'
mutate $KIT_REL/unattended.sh     '/^declared_scalar() {/,/^}/ s|_v=\${_l%%\[\[:space:\]\]#\*}|case $_l in *#*) continue ;; esac; _v=${_l}|'
hit "$(run)" "the extracted declared-scalar parser does not return the VALUE of a non-empty declaration, which is the only direction that tells a working parser from one answering nothing - a parser that empties every commented line passes every other assertion here. Specimen, wanted and got follow: ["

# ---- THE SOURCE POPULATION the three rules scan, derived from the kit directory rather than typed:
# ---- round 5 found 28c naming three files while the kit had seven. Its liveness is MEMBERSHIP rather
# ---- than a count - this checker and the adopter are themselves in that directory, so the population
# ---- is never empty and a count floor could be reached by no fixture.
reset_tree; rm -f $KIT_REL/check-playbook.sh
# ---- 28a, RE-ARMED AFTER ROUND 6 FOUND THE DISCARD ENUMERATION UNWINNABLE. The rule now enumerates
# ---- the COMPLIANT set, so the default is FAIL and a new spelling cannot widen the hole by existing.
# ---- Four spellings are staged, and the last two are the ones round 6 found walking past the
# ---- enumerate-the-discards version.
DISC='does not act on its exit status'
mutate $KIT_REL/unattended.sh 's@if ! _declared=$(declared_list "$_blob" set_checks); then@_declared=$(declared_list "$_blob" set_checks) || true; if false; then@'
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "the playbook leg is not in the source population these three rules scan, so the census reader - the one that dereferences the BASE blob every DoD verdict rests on - would go unexamined|a parser that can REFUSE is called at a site that does not act on its exit status, so the refusal arrives as the empty string every caller reads as the declared null and the item it guards grades met with nothing recorded - parser, site and call follow|the shipped template declares a key no inlined parser ever reads, so this check certifies a parse nothing consumes while whatever does consume it is unexamined - declare a parser read for it, or an exemption naming the reader that owns it|a key exemption names a reader whose signature is no longer in that file, so the key is unread by any parser AND unaccounted for by the exemption that excused it - key, file and missing literal follow|every bare git invocation in the kit was excused by the flags-only or for-each-ref property, so the raw arm graded nothing at all this run - it is reporting a clean nothing rather than a pass, and the two are not the same claim|the declared-scalar parser is missing from one of the two scripts that inline it, so the comparison that keeps the copies one answer would pass over an empty pair - driver and leg follow|the declared-list parser is missing from one of the two scripts that inline it, so the comparison that keeps the copies one answer would pass over an empty pair - driver and leg follow" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 7/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "the playbook leg is not in the source population these three rules scan, so the census reader - the one that dereferences the BASE blob every DoD verdict rests on - would go unexamined"
hit "$out" "a parser that can REFUSE is called at a site that does not act on its exit status, so the refusal arrives as the empty string every caller reads as the declared null and the item it guards grades met with nothing recorded - parser, site and call follow: declared_list at"
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
# ---- 28b. THE EXEMPTION ROW IS RETARGETED, never replaced with a synthetic: round 6's BLOCKER 1 was
# ---- a `key|file|literal` record destroyed by word-splitting, and the staged break that was supposed
# ---- to cover it substituted a value with no spaces in it, so it could not exhibit the split. The
# ---- table is newline-separated and read without splitting now, and this arm keeps the shipped
# ---- record's real spacing while pointing its key at one the template does not declare.
mutate $KIT_REL/check-unattended.sh 's@^legs|check-playbook.sh|@legsX|check-playbook.sh|@'
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "neither inlined parser carries a nonzero return any more, so the rule that a refusal must be read now binds nothing - either the refusal round 3 added was removed, in which case a legal multi-line declaration parses to the declared null again, or this check's derivation of which parsers can refuse has stopped matching them|the shipped template declares a key no inlined parser ever reads, so this check certifies a parse nothing consumes while whatever does consume it is unexamined - declare a parser read for it, or an exemption naming the reader that owns it|the extracted declared-list parser does not REFUSE an array left open at the end of its line, so a legal multi-line declaration parses to the declared null and every piece carrying no verdict grades verified - specimen, exit status and answer follow: [" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 7/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "neither inlined parser carries a nonzero return any more, so the rule that a refusal must be read now binds nothing - either the refusal round 3 added was removed, in which case a legal multi-line declaration parses to the declared null again, or this check's derivation of which parsers can refuse has stopped matching them"
hit "$out" "the shipped template declares a key no inlined parser ever reads, so this check certifies a parse nothing consumes while whatever does consume it is unexamined - declare a parser read for it, or an exemption naming the reader that owns it"

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

fi   # ---- end REGION 7 -----------------------------------------------------------------------------------

# ---- REGION 8 -----------------------------------------------------------------------------------
if in_shard 8; then
read_topo 8

# ---- 28c. The WRAPPER's own pin first, which round 5's cut could not see at all.
# THE CONSTANT, not the wrapper line. The merged library spells the pin as `-c "$GIT_PIN_REPLACE"`,
# so a break aimed at the old literal no-ops - and it is the constant that check 28c now follows, so
# breaking it is both the reachable mutation and the one that exercises the indirection.
reset_tree; mutate $KIT_REL/lib-unattended.sh 's|^GIT_PIN_REPLACE=.*|GIT_PIN_REPLACE=core.useReplaceRefs=true|'
# ...a bare unpinned read on a verb the first widening did not carry.
mutate $KIT_REL/unattended.sh 's@^export GIT_GRAFT_FILE=/dev/null@export GIT_GRAFT_FILE=/dev/null\n_probe() { git log -1 --format=%s "$1"; }@'
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "the kit's own git wrapper is defined without the replace-ref pin, so every read routed through it is unpinned at once - and this kit routes its BASE-blob authorization read through it. Site follows|a sha is dereferenced without the replace-ref pin, so a replace ref this run may install at any moment substitutes the committed bytes the census grades - and the run then supplies the playbook it is measured against, on an item no waiver can move. Site and read follow" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 8/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "the kit's own git wrapper is defined without the replace-ref pin, so every read routed through it is unpinned at once - and this kit routes its BASE-blob authorization read through it. Site follows"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi
hit "$out" "a sha is dereferenced without the replace-ref pin, so a replace ref this run may install at any moment substitutes the committed bytes the census grades - and the run then supplies the playbook it is measured against, on an item no waiver can move. Site and read follow"

# ...and the same read with a trailing comment mentioning the WRAPPER, which is round 6's MEDIUM 2:
# classifying the whole LINE as wrapper-routed let prose excuse the code beside it.
reset_tree; mutate $KIT_REL/unattended.sh 's@^export GIT_GRAFT_FILE=/dev/null@export GIT_GRAFT_FILE=/dev/null\n_probe() { git cat-file -p "$1"; }  # routed through GIT show elsewhere@'
hit "$(run)" "a sha is dereferenced without the replace-ref pin, so a replace ref this run may install at any moment substitutes the committed bytes the census grades - and the run then supplies the playbook it is measured against, on an item no waiver can move. Site and read follow"

# ...and the raw arm reaching NO graded candidate, which must not look like a pass. Routing the kit's
# last bare dereference through the wrapper leaves only exempt candidates behind.
reset_tree; mutate $KIT_REL/check-playbook.sh 's@^GITSHOW() { git -c core.useReplaceRefs=false -c advice.graftFileDeprecated=false show@GITSHOW() { GIT show@'
# ---- 28c's three liveness statements. The wrapper DEFINITION going missing, the bare spelling going
# ---- missing, and the wrapped spelling going missing are three different blindnesses, and round 5's
# ---- cut reported a clean nothing for two of them.
mutate $KIT_REL/lib-unattended.sh 's@^GIT() {@GITWRAP() {@'
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "no git wrapper definition was found anywhere in this kit, so the GIT-spelled reads below are accepted on the strength of a definition this check cannot see - which is the same as not checking them|every bare git invocation in the kit was excused by the flags-only or for-each-ref property, so the raw arm graded nothing at all this run - it is reporting a clean nothing rather than a pass, and the two are not the same claim" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 8/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "every bare git invocation in the kit was excused by the flags-only or for-each-ref property, so the raw arm graded nothing at all this run - it is reporting a clean nothing rather than a pass, and the two are not the same claim"
hit "$out" "no git wrapper definition was found anywhere in this kit, so the GIT-spelled reads below are accepted on the strength of a definition this check cannot see - which is the same as not checking them"

# ---- the scalar SPECIMEN loop's exec branch, a different branch from the template loop's.
reset_tree; gut_parser declared_scalar '  ((this is not shell'
# ---- and the shipped template's own LIST declaration being refused by the parser that reads it.
mutate $KIT_REL/PLAYBOOK-TEMPLATE.template.md 's|^\([a-z_][a-z_]*[[:space:]]*\)= \[\]|\1= [|'
out=$(GOV_UNATTENDED_REPORT=1 run)
check_emitted "the extracted declared-scalar parser could not be executed, so every parse assertion in this check would read its silence as the declared null and pass - specimen and exit status follow: [|the shipped template's own list declaration is REFUSED by the parser that reads it, so an adopter who copies the template inherits a declaration the driver cannot parse - and this check is the template's only grader, so nothing else would say so. Key and exit status follow|the extracted declared-scalar parser could not be executed over the shipped template's own line, and an unexecutable parser returns the empty string every assertion here reads as clean - key and exit status follow|the driver returned no verdict for any build this check asked it about, so a clean result here is about a driver path that answered nothing rather than about the corpus" "$out"  # set OBSERVED 2026-09-15 node a, direct run shard 8/8 at 72f54937 (aBatchedArm landing step 0)
hit "$out" "the extracted declared-scalar parser could not be executed, so every parse assertion in this check would read its silence as the declared null and pass - specimen and exit status follow: ["
hit "$out" "the shipped template's own list declaration is REFUSED by the parser that reads it, so an adopter who copies the template inherits a declaration the driver cannot parse - and this check is the template's only grader, so nothing else would say so. Key and exit status follow"

reset_tree

# ---- check 28 (round-2 fold): the inlined parser is ONE answer in two files, and the answer is the
# ---- one an adopter gets. Both branches, because agreement and correctness are different claims and
# ---- this check makes both.
reset_tree; mutate $KIT_REL/check-playbook.sh '/^declared_list() {/,/^}/ s|_m=\${_m//,/ }|_m=${_m}|'
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

# ---- A RE-RUN BUILD's ADD baseline is THIS run's, not the finished run's (TOOL-aRepatriatedFork-50).
# ---- The run-state path keeps the first run's history, so a walk over all of it stopped at that run's
# ---- first live commit and read every unit specced between the two runs as added mid-run. Measured on
# ---- aRepatriatedFork at 6e7cb0df: 19 units closed before the second run's preflight redded check 24.
# ---- The first run goes live with unit 1 and lands; unit 7 is specced; the second run pins a new BASE
# ---- and goes live; unit 9 arrives with no row. Unit 9 is the liveness half: the arm still grades.
seed_ros
sed -i 's/^phase: .*$/phase: LANDED/' memory/builds/tRos/RUN.md
git add -A && git commit -q -m "the first run landed" --no-verify
add_u7
git add -A && git commit -q -m "unit 7 specced between the runs" --no-verify
sed -i "s/^base: .*$/base: $(git rev-parse HEAD)/; s/^phase: .*$/phase: RUNNING/" memory/builds/tRos/RUN.md
git add -A && git commit -q -m "the second run's preflight" --no-verify
awk -v r='| [ARCH-tRos-9 — added mid-run](spec/nine.md) | OPEN | rev-1 | 2026-08-01 |' -v e="$UEND" \
  '$0==e{print r} {print}' memory/builds/tRos/README.md > /tmp/ros9.$$ && mv /tmp/ros9.$$ memory/builds/tRos/README.md
git add -A && git commit -q -m "unit 9 added while the second run is live" --no-verify
out=$(run)
miss "$out" "so the scope moved with nothing on the record saying so: ARCH-tRos-7 in"
hit "$out" "so the scope moved with nothing on the record saying so: ARCH-tRos-9 in"

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

# a pass that commits INSIDE its declared set is clean
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
miss "$(run)" "check 23 FAILED"

# ...and a pass that commits OUTSIDE it is the disjointness proof failing where it can be checked
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'b\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run)" "a pass of the run this branch drives committed outside the set it declared before dispatch while its window overlapped a sibling pass, and that declaration is the disjointness proof two concurrent passes rest on"

# ---- GENERATED RENDERS (TOOL-aRepatriatedFork-55): a GENERATED_INDEXES index and a change confined to
# ---- a gen region are the generator's writes, not the pass's; an authored line beside them is not.
# a write a GENERATED_INDEXES index covers is not counted
reset_tree
printf '\nGENERATED_INDEXES="memory/LIVE.md:gen.py"\n' >> .unattended.conf
git add -A && git commit -q -m "fixture: a generated index" --no-verify
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'live\n' >> memory/LIVE.md
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
miss "$out" "check 23 FAILED"
hit  "$out" "a generated render, the memory/LIVE.md index"
# ...and a write a KIT's `[[generated]]` row declares is not counted, with no conf line at all: the
# declaration lives with the generator (TOOL-aWindowedPass-4 AC3)
reset_tree
mkdir -p tools/genkit && printf 'x\n' > tools/genkit/gen.py
printf '[[generated]]\npath = "{memory_root}/derived"\ngenerator = "gen.py"\nwhy = "a fixture generator"\n' > tools/genkit/kit.toml
git add -A && git commit -q -m "fixture: a kit declaring a generated output" --no-verify
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work memory/derived && printf 'a\n' > work/one.txt && printf 'd\n' > memory/derived/out.json
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
miss "$out" "check 23 FAILED"
hit  "$out" "a generated render, the memory/derived index"
hit  "$out" "GENERATED_INDEXES resolved to: "
hit  "$out" "memory/derived:"
# ...and the SHIPPED defaults agree with every kit's REAL `[[generated]]` rows (closing review r1, B1).
# Gov's own conf hid an unconditional backlog row: it had dropped the backlog from SHARED_RECORDS,
# while the kit default and the example still name it, so every adopter's conf was refused at load.
# A scratch tree holding every real descriptor and the shipped confs is what an adopter loads.
# The scratch tree mirrors THIS install's layout, derived from where the suite sits, never spelled.
_b1=$(mktemp -d); git -C "$_b1" init -q
_b1tr=$(dirname -- "$KIT_REL"); [ "$_b1tr" = . ] && _b1tr="" || _b1tr="$_b1tr/"
for _b1k in "$HERE"/../*/kit.toml; do
  _b1d=${_b1k%/kit.toml}; _b1d=${_b1d##*/}; mkdir -p "$_b1/$_b1tr$_b1d"; cp "$_b1k" "$_b1/$_b1tr$_b1d/"
done
cp "$HERE/lib-unattended.sh" "$_b1/$KIT_REL/"; git -C "$_b1" add -A >/dev/null 2>&1
_b1sr=$(sed -n 's/^SHARED_RECORDS="\(.*\)"$/\1/p' "$HERE/.unattended.conf.example")
same "the example's SHARED_RECORDS was read, so the scan below grades something" "$(printf '%s' "$_b1sr" | grep -c backlog)" "1"
same "the kit-default SHARED_RECORDS overlaps no kit's real [[generated]] row" "$(read_scan_overlaps __kit-default__)" ""
same "the example's SHARED_RECORDS overlaps no kit's real [[generated]] row" "$(read_scan_overlaps "$_b1sr")" ""
# the control: under BACKLOG_MODE=builds the backlog rows apply, so the same scan does see them
printf 'BACKLOG_MODE="builds"\n' > "$_b1/.memory-tree.conf"
hit "$(read_scan_overlaps __kit-default__)" "memory/backlog"
rm -rf "$_b1"
# ...nor a change inside a README's gen regions, NESTED as the build README's are: the line between
# the inner close and the outer close is still generated
reset_tree
printf '# r\n\nprose\n\n<!-- gen:index -->\n<!-- gen:units -->\nold\n<!-- /gen:units -->\nRecords: 1\n<!-- /gen:index -->\n' > memory/README.md
git add -A && git commit -q -m "fixture: a README with a gen region" --no-verify
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && sed -i 's/^old$/new/; s/^Records: 1$/Records: 2/' memory/README.md
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
miss "$out" "check 23 FAILED"
hit  "$out" "a generated render, a change inside its gen regions only"
# ...but an authored line of the same README is the pass's own write, and counts
reset_tree
printf '# r\n\nprose\n\n<!-- gen:index -->\n<!-- gen:units -->\nold\n<!-- /gen:units -->\nRecords: 1\n<!-- /gen:index -->\n' > memory/README.md
git add -A && git commit -q -m "fixture: a README with a gen region" --no-verify
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && sed -i 's/^prose$/edited prose/' memory/README.md
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(run)
hit  "$out" "check 23 FAILED"
hit  "$out" "wrote memory/README.md"

# ---- OVERLAP (TOOL-aWindowedPass-1). Only a pass whose window overlapped a sibling's is counted,
# ---- which is why every counting arm in this file dispatches through `write_overlapping_dispatch`.
# AC1: one pass, alone, wrote outside its declaration: reported SOLO and not counted. BOUND, so the
# miss below is live: a counted write in the bound run would fail the leg.
reset_tree; write_run_branch
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'b\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(run)
hit  "$out" "check 23 SOLO ARCH-tRun-1 at "
hit  "$out" "wrote work/stray.txt in memory/builds/tRun/RUN.md — outside its declaration, but its window overlapped no sibling pass"
miss "$out" "check 23 FAILED"
# AC2: a sibling dispatched at a LATER anchor, before the first pass committed: the windows overlap
reset_tree; write_run_branch
drow ARCH-tRun-1 "work/one.txt"
drow ARCH-tRun-2 "work/two.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'b\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
printf 'c\n' > work/two.txt
git add -A && git commit -q -m "ARCH-tRun-2 builds its lane" --no-verify
out=$(run)
hit  "$out" "check 23 FAILED"
miss "$out" "check 23 SOLO"
# AC3: the sibling dispatched AFTER the first committed: sequential, so the stray write is SOLO
reset_tree; write_run_branch
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'b\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
drow ARCH-tRun-2 "work/two.txt"
printf 'c\n' > work/two.txt
git add -A && git commit -q -m "ARCH-tRun-2 builds its lane" --no-verify
out=$(run)
hit  "$out" "check 23 SOLO ARCH-tRun-1"
hit  "$out" "check 23 memory/builds/tRun/RUN.md — graded 2 pass(es), 0 overlapped a sibling"
miss "$out" "check 23 FAILED"

# ---- ABSORB (TOOL-dDerivedDocket-24 S9, AC8). The pass declared one path; a commit of its own, whose
# ---- subject is the absorb grammar and names no unit id, fixed an inherited red at another path. It
# ---- is reported on an ABSORB line and reaches neither anomaly branch. The CONTROL is the same paths
# ---- under a subject that also names the unit: that commit IS the pass commit, and the path is an
# ---- undeclared write whatever the subject starts with.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
mkdir -p fix && printf 'f\n' > fix/leg.txt
git add -A && git commit -q -m "absorb(tRun): memory hygiene inherited at 0123abcd" --no-verify
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
hit  "$out" "check 23 ABSORB"
hit  "$out" "'absorb(tRun): memory hygiene inherited at 0123abcd' wrote fix/leg.txt; an inherited red fixed in its own commit, graded as neither a dodged join nor an undeclared write"
miss "$out" "check 23 FAILED"
miss "$out" "the only join this check has was dodged"
# ...and an absorb commit moving a DECLARED path while no commit names the pass is not a dodged join.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "absorb(tRun): memory hygiene inherited at 0123abcd" --no-verify
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
hit  "$out" "check 23 ABSORB"
miss "$out" "the only join this check has was dodged"
miss "$out" "check 23 FAILED"
# CONTROL: the same paths with a unit id in the subject are the pass commit, graded and anomalous.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work fix && printf 'a\n' > work/one.txt && printf 'f\n' > fix/leg.txt
git add -A && git commit -q -m "absorb(tRun): memory hygiene inherited at 0123abcd ARCH-tRun-1" --no-verify
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
miss "$out" "check 23 ABSORB"
hit  "$out" "a pass of the run this branch drives committed outside the set it declared before dispatch while its window overlapped a sibling pass, and that declaration is the disjointness proof two concurrent passes rest on"

# ---- THE WIDENING REPAIR, AND THE POST-HOC REWRITE THAT WEARS ITS CLOTHES (closing review F3/F4).
# ---- A widening `--dispatch` made while the pass is OPEN parks a second row AT THE SAME ANCHOR, so a
# ---- widened declaration is two rows under one key and the pass may write their union (arm F,
# ---- TOOL-aGraftedHelix-39). A widening asked for AFTER the pass committed cannot reuse that anchor,
# ---- because HEAD has moved, so it lands under a new key and the original narrow row is still graded.
# ---- That is the ordering constraint, obtained by construction instead of by comparing timestamps.

# A: the sanctioned repair. Widened at its own anchor, commits inside the widened set.
reset_tree
write_run_branch
drows ARCH-tRun-1 "work/one.txt" "work/one.txt work/two.txt"
drow ARCH-tRun-9 "work/nine.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'b\n' > work/two.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
miss "$(run)" "check 23 FAILED"

# B: ...and the superseding row is still GRADED. Without this arm the fix above is indistinguishable
# from switching the check off for any pass that ever re-declared, which is a larger hole.
reset_tree
write_run_branch
drows ARCH-tRun-1 "work/one.txt" "work/one.txt work/two.txt"
drow ARCH-tRun-9 "work/nine.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run)" "a pass of the run this branch drives committed outside the set it declared before dispatch while its window overlapped a sibling pass, and that declaration is the disjointness proof two concurrent passes rest on"

# C: THE POST-HOC REWRITE. Narrow row, the offending commit, THEN a widened row at a later anchor.
# The finding must survive: a declaration cannot be rewritten to cover a write already made. The
# first repair folded on the unit alone with no ordering constraint, and this case went GREEN.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
drow ARCH-tRun-1 "work/one.txt work/stray.txt"
hit "$(run)" "a pass of the run this branch drives committed outside the set it declared before dispatch while its window overlapped a sibling pass, and that declaration is the disjointness proof two concurrent passes rest on"

# D: SEVERAL PASSES OF ONE UNIT are legal — M6 defines five pass kinds and a unit may be dispatched
# once per kind. Each row governs its own pass. Folding them together graded pass one's commit
# against pass two's declaration and redded a correct run.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/spec.txt"
mkdir -p work && printf 's\n' > work/spec.txt
git add -A && git commit -q -m "ARCH-tRun-1 authors its spec" --no-verify
drow ARCH-tRun-1 "work/build.txt"
printf 'b\n' > work/build.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its unit" --no-verify
miss "$(run)" "check 23 FAILED"

# E: ...and the SECOND pass is graded too. The fold left it unlooked-at entirely, so a stray write in
# pass two exited 0 — the same fixture as D with one extra file, and the difference is the point.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/spec.txt"
mkdir -p work && printf 's\n' > work/spec.txt
git add -A && git commit -q -m "ARCH-tRun-1 authors its spec" --no-verify
drow ARCH-tRun-1 "work/build.txt"
printf 'b\n' > work/build.txt && printf 'x\n' > work/STRAY.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its unit" --no-verify
hit "$(run)" "a pass of the run this branch drives committed outside the set it declared before dispatch while its window overlapped a sibling pass, and that declaration is the disjointness proof two concurrent passes rest on"

# F: TWO SAME-ANCHOR ROWS WITH DISJOINT PATHS are one pass that may write their UNION
# (TOOL-aGraftedHelix-39): the second row ADDS a path and replaces nothing. Built as arm A is, with its
# sibling row. Graded against the last row alone, the commit's write to work/one.txt is undeclared.
reset_tree
write_run_branch
drows ARCH-tRun-1 "work/one.txt" "work/two.txt"
drow ARCH-tRun-9 "work/nine.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'b\n' > work/two.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(run)
hit  "$out" "unattended: check 23 fleet — 0 undeclared write(s) over 1 graded pass(es)"
miss "$out" "check 23 FAILED"

# G: BOTH IDS IN ONE DISPATCH GROUP, which is the whole of this arm and is what the first two
# versions of it missed. The ambiguity loop only pairs siblings sharing an anchor, so a fixture that
# parks its two ids at different anchors never reaches the comparison it claims to pin — and reverting
# the anchoring left the whole suite green. `ARCH-tRun-1` is a prefix of `ARCH-tRun-10`, so under an
# unanchored `case ... in *"$dssunit"*` the `-10` commit reads as naming `-1` too and a correct run is
# refused for ambiguous attribution.
reset_tree; write_run_branch
gdrows ARCH-tRun-1 "work/one.txt" ARCH-tRun-10 "work/ten.txt"
mkdir -p work && printf 'b\n' > work/ten.txt
git add -A && git commit -q -m "ARCH-tRun-10 builds its lane" --no-verify
out=$(run)
miss "$out" "unattended: check 23 — one commit names two passes of the same dispatch group"
miss "$out" "check 23 FAILED"
# ...and the positive control, so this arm cannot pass by finding nothing: ONE commit that genuinely
# names both passes IS ambiguous, and the refusal must fire.
reset_tree
gdrows ARCH-tRun-1 "work/one.txt" ARCH-tRun-2 "work/two.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'b\n' > work/two.txt
git add -A && git commit -q -m "ARCH-tRun-1 and ARCH-tRun-2 build together" --no-verify
hit "$(run)" "unattended: check 23 — one commit names two passes of the same dispatch group, so a subset test over it cannot say which pass wrote what and the attribution this comparison rests on is not available:"

# ...declaring MORE than you use is conservative and fine
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt work/two.txt"
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
miss "$(run)" "check 23 FAILED"

# ---- THE NO-COMMIT CASE IS SPLIT. A pass that produced no change commits nothing and that is legal;
# ---- the same silence with the declared paths MOVED is the join being dodged.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
hit "$out" "no commit names this pass and none of its declared paths moved, which is a pass that produced no change"
miss "$(run)" "check 23 FAILED"

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
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
printf 'folded\n' > work/later.txt
git add -A && git commit -q -m "ARCH-tRun-1 folds a review fix" --no-verify
miss "$(run)" "check 23 FAILED"

# ---- THE `Pass:` TRAILER ATTRIBUTES A COMMIT (TOOL-aWindowedPass-2). A records commit whose subject
# ---- names the unit, ahead of the real pass, is no pass when it says `Pass: none`: the walk takes the
# ---- commit whose trailer names the unit, and the records commit's out-of-set write is never graded.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p notes && printf 'r\n' > notes/records.md
git add -A && git commit -q -m "records for ARCH-tRun-1..3" -m "Pass: none" --no-verify
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "lane" -m "Pass: ARCH-tRun-1" --no-verify
miss "$(run)" "check 23 FAILED"
# ...and with NO trailer anywhere the subject still attributes, so a landed record keeps its verdict:
# the records commit is taken as the pass and its out-of-set write is graded
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p notes && printf 'r\n' > notes/records.md
git add -A && git commit -q -m "records for ARCH-tRun-1..3" --no-verify
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)" "ARCH-tRun-1 at"
# ...and the build-commit pick reads the same attribution: a `Pass: none` commit naming the unit in
# its subject is passed over for the commit whose trailer names it
reset_tree
_bc_base=$(git rev-parse HEAD)
mkdir -p work && printf 'r\n' > work/rec.txt
git add -A && git commit -q -m "ARCH-tRun-1 records" -m "Pass: none" --no-verify
printf 'a\n' > work/one.txt
git add -A && git commit -q -m "lane" -m "Pass: ARCH-tRun-1" --no-verify
_bc_want=$(git rev-parse HEAD)
_bc_got=$(cd "$TMP" && . "$TMP/$KIT_REL/lib-unattended.sh" && build_commit "$_bc_base..HEAD" ARCH-tRun-1 memory/builds/tRun "" "")
same "build_commit takes the commit whose Pass: trailer names the unit" "$_bc_got" "$_bc_want"
# ...and a `none` BESIDE the unit's id attributes that commit to nothing here too (closing review r2, M8)
reset_tree
_bc_base=$(git rev-parse HEAD)
mkdir -p work && printf 'r\n' > work/rec.txt
git add -A && git commit -q -m "lane prep" -m "$(printf 'Pass: none\nPass: ARCH-tRun-1')" --no-verify
printf 'a\n' > work/one.txt
git add -A && git commit -q -m "lane" -m "Pass: ARCH-tRun-1" --no-verify
_bc_want=$(git rev-parse HEAD)
_bc_got=$(cd "$TMP" && . "$TMP/$KIT_REL/lib-unattended.sh" && build_commit "$_bc_base..HEAD" ARCH-tRun-1 memory/builds/tRun "" "")
same "build_commit passes over a commit whose trailer pairs none with the unit" "$_bc_got" "$_bc_want"

# ---- THE SKIPS ANNOUNCE. A run with no declaration would otherwise be green over nothing, and the
# ---- default run must still print nothing.
reset_tree
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
hit "$out" "this run declared no concurrent dispatch, so there is no declaration to compare and a green verdict here would be coverage of nothing"
out=$(run)
miss "$out" "check 23 skipped"
miss "$out" "check 23 FAILED"

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
write_overlapping_dispatch ARCH-tRun-1 "work/sub/"
mkdir -p work/sub && printf 'a\n' > work/sub/x.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
miss "$(run)" "check 23 FAILED"
# ...and the positive control on the same shape, so the arm cannot pass by the check being silent:
# a commit genuinely outside the declared lane still reports.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/sub/"
mkdir -p work/sub && printf 'a\n' > work/sub/x.txt && printf 'b\n' > work/elsewhere.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run)" "a pass of the run this branch drives committed outside the set it declared before dispatch while its window overlapped a sibling pass, and that declaration is the disjointness proof two concurrent passes rest on"

# ---- THE BRIEF ROW'S PATH LEAVES THE POPULATION (TOOL-aLeakedHandle-7, TOOL-aRatifiedRulings-2).
# ---- `--brief` stages only the run-state file and the brief is already tracked, so the pass's one
# ---- commit carries a file the pass never wrote and never declared. Five fixtures, one shape: the
# ---- dispatch row through `drow`, the brief file and a conforming `brief · item` row written
# ---- inline — a real twelve-hex `hash-object` prefix, though check 23 never reads the hash — and
# ---- the pass commit carrying all of it. A is the exclusion; B is the control that keeps A from
# ---- passing by finding nothing, one stray file apart; C pins the tree at the PASS COMMIT, a row
# ---- appended after it excludes nothing; D pins the PATH and not its directory; E pins `normpath`,
# ---- for the reason the `covers` arm above was written. A, B and E were RED against the checker at
# ---- base; C and D are controls the base checker already passes, each redded once by a staged
# ---- break named in the unit's acceptance ledger.
BRIEF=memory/builds/tRun/prompts/2026-08-21-prompt-ARCH-tRun-1-1-build-brief.md
# A: the brief is in the pass commit and its row names it — silent by default, announced on the
# report channel, which is the positive artifact that the exclusion branch ran on that path.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work memory/builds/tRun/prompts && printf 'a\n' > work/one.txt && printf '# brief\n' > "$BRIEF"
printf '2026-08-21T00:00:01Z brief · item ARCH-tRun-1 · reason %s %s\n' \
  "$(git hash-object "$BRIEF" | cut -c1-12)" "$BRIEF" >> memory/builds/tRun/RUN.md
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
miss "$(run)" "check 23 FAILED"
hit "$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)" "check 23 excluded $BRIEF for ARCH-tRun-1 in memory/builds/tRun/RUN.md"
# B: ...and a stray file beside it still reports, minus the brief. The exclusion is the one path.
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work memory/builds/tRun/prompts && printf 'a\n' > work/one.txt && printf 'b\n' > work/stray.txt \
  && printf '# brief\n' > "$BRIEF"
printf '2026-08-21T00:00:01Z brief · item ARCH-tRun-1 · reason %s %s\n' \
  "$(git hash-object "$BRIEF" | cut -c1-12)" "$BRIEF" >> memory/builds/tRun/RUN.md
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(run)
hit  "$out" "wrote work/stray.txt in memory/builds/tRun/RUN.md"
miss "$out" "build-brief.md"
# C: POST HOC. The row lands in a second commit touching only the run-state file, so the pass
# commit's tree holds no row and the brief stays reported — a row written afterwards hides nothing.
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work memory/builds/tRun/prompts && printf 'a\n' > work/one.txt && printf '# brief\n' > "$BRIEF"
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
printf '2026-08-21T00:00:02Z brief · item ARCH-tRun-1 · reason %s %s\n' \
  "$(git hash-object "$BRIEF" | cut -c1-12)" "$BRIEF" >> memory/builds/tRun/RUN.md
git add -A && git commit -q -m "run-state bookkeeping" --no-verify
hit "$(run)" "wrote $BRIEF"
# D: DIRECTORY. A row naming `prompts` excludes nothing under it, so both files still report.
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work memory/builds/tRun/prompts && printf 'a\n' > work/one.txt && printf '# brief\n' > "$BRIEF" \
  && printf 'other\n' > memory/builds/tRun/prompts/other.md
printf '2026-08-21T00:00:01Z brief · item ARCH-tRun-1 · reason %s memory/builds/tRun/prompts\n' \
  "$(git hash-object "$BRIEF" | cut -c1-12)" >> memory/builds/tRun/RUN.md
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run)" "memory/builds/tRun/prompts/other.md"
# E: SPELLING. A row naming the brief as `./memory/...` is the same path once normalised.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work memory/builds/tRun/prompts && printf 'a\n' > work/one.txt && printf '# brief\n' > "$BRIEF"
printf '2026-08-21T00:00:01Z brief · item ARCH-tRun-1 · reason %s ./%s\n' \
  "$(git hash-object "$BRIEF" | cut -c1-12)" "$BRIEF" >> memory/builds/tRun/RUN.md
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
miss "$(run)" "check 23 FAILED"
# F: THE BOOKKEEPING COMMIT IS NOT THE PASS COMMIT (closing diff review, finding 7). The ordinary
# shape: `--brief` requires the brief tracked and stages the run-state file, so the run commits
# `{brief, brief row}` first, naming the unit, and the pass's real commit follows. With the brief
# forgiven only in this check, `pass_commit` SELECTED that bookkeeping commit, the exclusion emptied
# it, and the stray in the commit that followed was never graded — silent where B reports. Now the
# library subtracts the same set before selecting, so the walk reaches the commit with the stray.
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work memory/builds/tRun/prompts && printf '# brief\n' > "$BRIEF"
printf '2026-08-21T00:00:01Z brief · item ARCH-tRun-1 · reason %s %s\n' \
  "$(git hash-object "$BRIEF" | cut -c1-12)" "$BRIEF" >> memory/builds/tRun/RUN.md
git add -A && git commit -q -m "ARCH-tRun-1 brief handed" --no-verify
printf 'a\n' > work/one.txt && printf 'b\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run)" "wrote work/stray.txt in memory/builds/tRun/RUN.md"

# ---- TOOL-dDerivedDocket-30 S1: THE DIRECTORY AND THE BLOB, the two conditions A to F left out. Four
# ---- fixtures on arm A's shape, each graded through `--skip 28` because check 23 sits outside that
# ---- region. G: the brief EDITED after its row hashed it is no longer the brief the row names, so it
# ---- reports. H: a row naming a SIBLING unit excuses nothing for this one. I: a row naming a path
# ---- outside the build's own `prompts/` - a product file, hashed correctly - excuses nothing. J: the
# ---- `{brief, row}` commit carrying an EDITED brief is not skipped as bookkeeping, so it is the commit
# ---- graded and the edit reports rather than the clean commit after it. G, I and J were silent at
# ---- the base, where the row's unit alone decided; H is the unit condition's control.
# G: edited after hashing
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work memory/builds/tRun/prompts && printf 'a\n' > work/one.txt && printf '# brief\n' > "$BRIEF"
printf '2026-08-21T00:00:01Z brief · item ARCH-tRun-1 · reason %s %s\n' \
  "$(git hash-object "$BRIEF" | cut -c1-12)" "$BRIEF" >> memory/builds/tRun/RUN.md
printf '# brief, edited after the row hashed it\n' > "$BRIEF"
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run_skip_leg)" "wrote $BRIEF in memory/builds/tRun/RUN.md"
# H: a sibling's row
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work memory/builds/tRun/prompts && printf 'a\n' > work/one.txt && printf '# brief\n' > "$BRIEF"
printf '2026-08-21T00:00:01Z brief · item ARCH-tRun-2 · reason %s %s\n' \
  "$(git hash-object "$BRIEF" | cut -c1-12)" "$BRIEF" >> memory/builds/tRun/RUN.md
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run_skip_leg)" "wrote $BRIEF in memory/builds/tRun/RUN.md"
# I: a product file named by a correctly hashed row
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'p\n' > work/product.txt
printf '2026-08-21T00:00:01Z brief · item ARCH-tRun-1 · reason %s work/product.txt\n' \
  "$(git hash-object work/product.txt | cut -c1-12)" >> memory/builds/tRun/RUN.md
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run_skip_leg)" "wrote work/product.txt in memory/builds/tRun/RUN.md"
# J: the bookkeeping commit carrying an edited brief is graded, not skipped
reset_tree
drow ARCH-tRun-1 "work/one.txt"
mkdir -p memory/builds/tRun/prompts && printf '# brief\n' > "$BRIEF"
printf '2026-08-21T00:00:01Z brief · item ARCH-tRun-1 · reason %s %s\n' \
  "$(git hash-object "$BRIEF" | cut -c1-12)" "$BRIEF" >> memory/builds/tRun/RUN.md
printf '# brief, edited after the row hashed it\n' > "$BRIEF"
git add -A && git commit -q -m "ARCH-tRun-1 brief handed" --no-verify
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
hit "$(run_skip_leg)" "wrote $BRIEF in memory/builds/tRun/RUN.md"

fi   # ---- a re-cut seam of the region-8 span (TOOL-aGraftedHelix-34 S7): the section below is region 3's
if in_shard 3; then
cd "$TMP" || exit 2; anchor_restore; read_topo s1   # every section after a re-cut seam starts from the prologue's fixture, refs and remote
# ---- EACH RUN AGAINST ITS OWN BUDGET (TOOL-aWindowedPass-5, TOOL-dUnstuckLanding-17). The run this
# ---- branch drives fails when its counted writes exceed its per-build budget, 0 here, so ONE counted
# ---- write fails it; the same record read from a detached HEAD binds no run and is only printed. This
# ---- arm used to assert the opposite - spec 23 S1 / AC9 pinned "reports without failing" - and that
# ---- pin is SUPERSEDED rather than deleted quietly.
# AC1: the bound run's one counted write fails the leg, naming the run and its budget
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(run); rc=$?
same "check 23 fails the bound run on one counted write, exit code" "$rc" "1"
hit  "$out" "a pass of the run this branch drives committed outside the set it declared before dispatch while its window overlapped a sibling pass, and that declaration is the disjointness proof two concurrent passes rest on: 1 in memory/builds/tRun/RUN.md against a per-build budget of 0"
hit  "$out" "wrote work/stray.txt in memory/builds/tRun/RUN.md"
# ...and the fleet line is printed beside the failure, naming the build over budget (S6)
hit  "$out" "unattended: check 23 fleet — 1 undeclared write(s) over 1 graded pass(es) in 1 record(s) · budget 0 per build · over tRun=1 · range "
# AC2: the same tree from a detached HEAD: reported OTHER RUN, and check 23 does not fail
_c23br=$(git symbolic-ref -q --short HEAD)
git checkout -q --detach
out=$(run)
hit  "$out" "check 23 OTHER RUN memory/builds/tRun/RUN.md: 1 counted, graded at its own close - this tree drives a detached HEAD"
miss "$out" "UNATTENDED check 23 FAILED"
git checkout -q "$_c23br"

# ---- ...AND THE BUDGET IS A BUDGET. Same fixture, one instance, a budget of 1: check 23 is clean.
# ---- Without this control the arm above is satisfied by a check that reds on everything. It asserts
# ---- check 23's own strings and not the leg's exit code, because the overlapping fixture's sibling
# ---- pass never commits and no arm asserts the other checks clean on it.
mutate .unattended.conf 's/^UNDECLARED_WRITE_BUDGET=.*/UNDECLARED_WRITE_BUDGET="1"/'
out=$(run)
miss "$out" "check 23 FAILED"
# ...the fleet line names no build over a budget the record does not exceed
hit  "$out" "· budget 1 per build · over none · "
# ...and the per-instance detail survives on the report channel, so a green run has not gone dark.
hit "$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)" "wrote work/stray.txt in memory/builds/tRun/RUN.md"
reset_tree

# ---- THE BUDGET IS MANDATORY, in the shape its siblings already take: undeclared or malformed is
# ---- a refusal and never a defaulted value.
reset_tree
mutate .unattended.conf 's/^UNDECLARED_WRITE_BUDGET=.*/UNDECLARED_WRITE_BUDGET=""/'
hit "$(run)" "UNDECLARED_WRITE_BUDGET is undeclared in .unattended.conf, and with no budget a pass that wrote outside its declared set is reported and never graded - which is the state this check exists to end"
mutate .unattended.conf 's/^UNDECLARED_WRITE_BUDGET=.*/UNDECLARED_WRITE_BUDGET="several"/'
hit "$(run)" "UNDECLARED_WRITE_BUDGET is not a single integer, so the per-build comparison below would be a string test wearing a numeric name"
reset_tree

# ---- THE RETIRED KEY IS REFUSED BY NAME (S8), off the leg's text scan of declared names, so an
# ---- adopter who upgrades without moving it is told which key replaced it. Staged out, the old key
# ---- is silently ignored and the leg passes.
reset_tree
printf '\nUNDECLARED_WRITE_CEILING="0"\n' >> .unattended.conf
out=$(run)
hit "$out" " is retired: check 23 grades each run record against a per-build budget now, so declare UNDECLARED_WRITE_BUDGET in .unattended.conf and delete the old key, which nothing reads any more"
# AC3 (TOOL-aWindowedPass-5): a conf still setting the retired key passes check 22 and is reported as
# retired there; check 23's refusal above is the one that names the replacement.
reset_tree
printf '\nUNDECLARED_WRITE_CEILING="5"\n' >> .unattended.conf
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
miss "$out" "check 22 FAILED"
hit  "$out" "check 22 - UNDECLARED_WRITE_CEILING is RETIRED (TOOL-aWindowedPass-5)"
reset_tree

# ---- THE LIVENESS HALF. A budget above zero says instances may exist; grading NO dispatched pass at
# ---- all and then reporting zero of them is a probe that died, not a tree that is clean. The
# ---- fixture declares no dispatch, so the loop above takes its skip branch and grades nothing.
reset_tree
mutate .unattended.conf 's/^UNDECLARED_WRITE_BUDGET=.*/UNDECLARED_WRITE_BUDGET="1"/'
hit "$(run)" "the declared budget on undeclared writes is above zero while NO dispatched pass was graded at all, so every per-build comparison above would report a reassuring zero for a probe that died rather than for a tree that is clean"
# ...and the control: at a budget of 0 the same tree is clean, so the arm above is not just
# asserting that an undeclared-dispatch fixture reds.
reset_tree
miss "$(run)" "check 23 FAILED"
# AC4: the measuring flag is retired with the key
reset_tree
out=$(bash "$SCRIPT" --emit-ceiling 2>&1); rc=$?
same "--emit-ceiling is retired, exit code" "$rc" "2"
hit  "$out" "retired with UNDECLARED_WRITE_CEILING (TOOL-aWindowedPass-5)"
reset_tree
# closing review r1, M6: a record naming NO run branch is bound by no checkout, and says so distinctly
# rather than claiming a close that will grade it
drow ARCH-tRun-1 "work/one.txt"
drow ARCH-tRun-9 "work/nine.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(run)
hit  "$out" "check 23 UNBOUND memory/builds/tRun/RUN.md: 1 counted - the record names no run branch"
miss "$out" "check 23 OTHER RUN"
reset_tree
# closing review r1, M7: a base that does not resolve places no window, so even a lone bound pass is
# COUNTED - the verdict before overlap counting - and the leg says why
write_run_branch; sed -i 's/^base: .*/base: 0000000000000000000000000000000000000000/' memory/builds/tRun/RUN.md
git add -A && git commit -q -m "fixture: an unresolvable base" --no-verify
drow ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)
hit  "$out" "UNATTENDED check 23 FAILED"
hit  "$out" "check 23 overlap unavailable for memory/builds/tRun/RUN.md"
miss "$out" "check 23 SOLO"
reset_tree

# ---- RANGE MODE (TOOL-dUnstuckLanding-17 S5, AC4). A pass whose pass commit is already on the tip the
# ---- remote advertises was graded when it landed; it stays COUNTED on the fleet line and is not
# ---- graded against its record's budget again. Pass 1 writes outside its declaration and is pushed;
# ---- pass 2 is clean and unpushed: no FAILED. Then pass 2 writes outside too: FAILED naming pass 2
# ---- and never pass 1. Red when the `check_adv_reaches` test is staged out of the budget count.
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
RG_TIP=$(git rev-parse HEAD)
git push -q -f origin HEAD:main
drow ARCH-tRun-2 "work/two.txt"
printf 'b\n' > work/two.txt
git add -A && git commit -q -m "ARCH-tRun-2 builds its lane" --no-verify
RG_HEAD=$(git rev-parse HEAD)
out=$(run)
hit  "$out" "unattended: check 23 fleet — 1 undeclared write(s) over 2 graded pass(es) in 1 record(s) · budget 0 per build · over tRun=1 · range ${RG_TIP:0:8}..${RG_HEAD:0:8} · at ${RG_HEAD:0:8}"
miss "$out" "check 23 FAILED"
# ...the unpushed pass writing outside its declaration is graded, and the pushed one is not named
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
git push -q -f origin HEAD:main
drow ARCH-tRun-2 "work/two.txt"
printf 'b\n' > work/two.txt && printf 'd\n' > work/stray2.txt
git add -A && git commit -q -m "ARCH-tRun-2 builds its lane" --no-verify
out=$(run)
hit  "$out" "a pass of the run this branch drives committed outside the set it declared before dispatch while its window overlapped a sibling pass, and that declaration is the disjointness proof two concurrent passes rest on: 1 in memory/builds/tRun/RUN.md against a per-build budget of 0"
hit  "$out" "ARCH-tRun-2 at $(git rev-parse HEAD) wrote work/stray2.txt"
rg_fail=$(grep -F 'check 23 FAILED' <<<"$out" || true)
miss "$rg_fail" "ARCH-tRun-1 at"
hit  "$out" "check 23 fleet — 2 undeclared write(s) over 2 graded pass(es) in 1 record(s) · budget 0 per build · over tRun=2 · range "
# ...and WHOLE mode, when no advertised tip resolves, grades the pushed pass as the leg always did
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/nothing-here
out=$(run)
hit  "$out" "· range whole (the tip did not resolve: "
hit  "$out" "2 in memory/builds/tRun/RUN.md against a per-build budget of 0"
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main
git push -q -f origin "$ANCHOR0":main
reset_tree

# ---- DERIVED LANDED IS NOT GRADED (TOOL-aSightedSkeptic-13): check 23 asks check 7's predicate, so an
# ---- in-place landing whose record stays LANDING stops counting once its landing commit is on the
# ---- advertised tip. Each arm is the stray-write fixture above, graded at the adopter's ceiling of 0,
# ---- and asserts only check 23's own strings, because a LANDING record moves checks 7, 15 and 19 too.
# A: pushed, so derived LANDED - excluded, naming the record and its landing commit
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md
git add -A && git commit -q -m "tRun lands" --no-verify
git push -q -f origin HEAD:main
out=$(run)
hit  "$out" "check 23 EXCLUDED memory/builds/tRun/RUN.md — derived LANDED: its landing commit $(git rev-parse HEAD)"
miss "$out" "check 23 FAILED"
git push -q -f origin "$ANCHOR0":main
# B (control): the same LANDING record, NOT pushed, is a live run and is graded
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md
git add -A && git commit -q -m "tRun lands" --no-verify
out=$(run)
hit  "$out" "check 23 FAILED"
miss "$out" "check 23 EXCLUDED"
# C: no advertised tip resolves - UNAVAILABLE once, and the record is graded rather than excluded
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md
git add -A && git commit -q -m "tRun lands" --no-verify
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/nothing-here
out=$(run)
same "check 23 exclusion UNAVAILABLE prints once" "$(grep -c 'check 23 exclusion UNAVAILABLE' <<<"$out")" "1"
hit  "$out" "UNATTENDED check 23 FAILED"
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main
# D (control): a recorded LANDED record is still skipped by its phase before the predicate is asked
reset_tree
write_overlapping_dispatch ARCH-tRun-1 "work/one.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane" --no-verify
sed -i 's/^phase: .*/phase: LANDED/' memory/builds/tRun/RUN.md
git add -A && git commit -q -m "tRun landed" --no-verify
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/nothing-here
out=$(run)
miss "$out" "check 23 EXCLUDED"
miss "$out" "check 23 exclusion UNAVAILABLE"
miss "$out" "UNATTENDED check 23 FAILED"
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main
reset_tree

# ---- THE TRAILER, READ ONE WAY EVERYWHERE (closing review r1, M3 and L2).
# M3: a trailered pass commit whose SUBJECT mentions a sibling is still that pass's alone, and graded
reset_tree; write_run_branch
gdrows ARCH-tRun-1 "work/one.txt" ARCH-tRun-2 "work/two.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "ARCH-tRun-1 builds its lane beside ARCH-tRun-2" -m "Pass: ARCH-tRun-1" --no-verify
out=$(run)
hit  "$out" "UNATTENDED check 23 FAILED"
miss "$out" "one commit names two passes"
# L2: a comma-joined trailer names each of its ids, so the pass is attributed and graded
reset_tree; write_run_branch
gdrows ARCH-tRun-1 "work/one.txt" ARCH-tRun-2 "work/two.txt"
mkdir -p work && printf 'a\n' > work/one.txt && printf 'c\n' > work/stray.txt
git add -A && git commit -q -m "lane" -m "Pass: ARCH-tRun-1, ARCH-tRun-9" --no-verify
hit  "$(run)" "UNATTENDED check 23 FAILED"
# ...and `none` beside an id names nothing, so the commit is no pass and its declared path moved unnamed
reset_tree; write_run_branch
gdrows ARCH-tRun-1 "work/one.txt" ARCH-tRun-2 "work/two.txt"
mkdir -p work && printf 'a\n' > work/one.txt
git add -A && git commit -q -m "lane" -m "$(printf 'Pass: none\nPass: ARCH-tRun-1')" --no-verify
out=$(run)
hit  "$out" "the only join this check has was dodged"
miss "$out" "UNATTENDED check 23 FAILED"

# ---- A NEGATIVE CHECK-23 ARM MUST BE ABLE TO FAIL (closing review r1, H1). Check 23 counts a write only
# ---- beside an overlapping sibling and fails only the bound run, so an arm dispatching one unit with no
# ---- `write_run_branch` stays green whatever the code does: eight arms were vacuous that way, one of them the
# ---- only holder of `pass_commit`'s trailer branch. Graded over this file's own check-23 region.
_h1=$(awk '/^# ---- check 23 \(TOOL-dUnstalledConvoy-10\)/ { on = 1 } /^# ---- A NEGATIVE CHECK-23 ARM/ { on = 0 }
  on && /^reset_tree/ { live = ($0 ~ /write_run_branch/); disp = 0 }
  on && /^(write_overlapping_dispatch|write_run_branch)/ { live = 1 }
  on && /^(drow|drows|gdrows|write_overlapping_dispatch) / { disp = 1 }
  on && /^miss .*"(UNATTENDED )?check 23 FAILED"/ { n++; if (disp && !live) print NR }
  END { print "graded=" n + 0 }' "$HERE/${0##*/}"); _h1rc=$?
# LIVENESS (closing review r2, M3): a scan that read nothing - its anchor reworded, its file unread -
# printed an empty list and passed. It must have read the file and graded at least one negative arm.
same "the H1 self-scan read this suite, exit code" "$_h1rc" "0"
same "the H1 self-scan graded at least one negative check-23 arm" "$(printf '%s\n' "$_h1" | sed -n 's/^graded=//p' | awk '{ print ($1 > 0) ? "yes" : "no" }')" "yes"
same "every negative check-23 arm that dispatches runs bound, so its miss can fail" "$(printf '%s\n' "$_h1" | grep -v '^graded=')" ""

# ---- check 15 (TOOL-dUnstalledConvoy-2): the ancestry half now branches on the RECORDED anchor kind.
# ---- A `local` record is a claim about ONE clone — the protocol calls it a record of a merge rather
# ---- than an observation of one — so a clone that never had that merge says so instead of redding.
# ---- Without that, a run lands locally on one node and the same leg reds on every other node that
# ---- has not fast-forwarded its own default branch.

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

# ---- TOOL-aRepatriatedFork-11 S1 (AC1): check 21 grades the BUILD ROOT's README and no README
# ---- nested inside a build. Both carry no marker pair; before the `:(glob)` magic the plain
# ---- pathspec's `*` crossed the slash and the nested file was named too (41 of them at adopter ic).
reset_tree
mkdir -p memory/builds/tOne/notes
printf '# tOne\n' > memory/builds/tOne/README.md
printf '# a nested readme\n' > memory/builds/tOne/notes/README.md
git add -A
out=$(run)
hit  "$out" "a tracked build README does not carry exactly one well-formed generated-units marker pair, so the driver cannot read its unit list and no run against it can close; repair with"
hit  "$out" " memory/builds/tOne/README.md"
miss "$out" "memory/builds/tOne/notes/README.md"

# ---- check 35 (S2, AC2): a kit script spelling a build-root pathspec without the magic is refused
# ---- by file and line; a DESCENDING tail is sub-spec depth on purpose and is not graded.
reset_tree
mutate $KIT_REL/unattended.sh 's|":(glob)$M/builds/\*/RUN.md"|"$M/builds/*/RUN.md"|'
out=$(run)
hit "$out" "a script in the kit directory names a file at a build root through a pathspec without the :(glob) magic, so its wildcard crosses a slash and every same-named file nested inside a build joins the population"
hit "$out" " unattended.sh:"
reset_tree
printf '_x=$(GIT ls-files "$M/builds/*/spec/*.md")\n' >> $KIT_REL/unattended.sh
miss "$(run)" "names a file at a build root through a pathspec without the :(glob) magic"

# ---- --emit-ceiling is RETIRED (TOOL-dUnstuckLanding-17 S9, AC8): a budget is declared, not measured,
# ---- so the flag refuses with exit 2 before any check runs and names the fleet line, where the count
# ---- now appears. Red when the branch still runs checks rather than exiting at once.
reset_tree
out=$(bash "$SCRIPT" --emit-ceiling 2>&1); rc=$?
same "--emit-ceiling is refused, exit code" "$rc" "2"
hit  "$out" "refused (TOOL-dUnstuckLanding-17): check 23 grades the run this branch drives against a declared per-build budget, which is a policy and not a measurement, so there is no pin left to measure, and the fleet's count now appears on the 'check 23 fleet' line every run prints"
miss "$out" "UNATTENDED check"
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

fi   # ---- a re-cut seam of the region-8 span (TOOL-aGraftedHelix-34 S7): the section below is region 8's
if in_shard 8; then
cd "$TMP" || exit 2; anchor_restore; read_topo s2   # every section after a re-cut seam starts from the prologue's fixture, refs and remote
# ============== TOOL-dDerivedDocket-4: the phase-read routing, the core floor, --phase ============
# CHECKS 39 AND 40 here are the pair this unit's spec calls 32 and 33: main numbered its own 32 and
# 33 first, and the reconcile merge kept main's numbers and moved this pair.
# Every arm below grades a DRIVER COPY in the fixture, which is the only place the sets and the call
# sites live. The re-stage before each edit is load-bearing for the reason the parked-kind arms
# above already record: `reset_tree`'s `git clean -qfd` removes the copied kit, and without it the
# sed edits nothing, the grep finds nothing, and the arm passes by finding nothing.

# ---- CHECK 39, arm one: a direct read of the phase fact in a function that is neither reader.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh 's|^  read_derived_phase "$rel"; p="$DP_PHASE"; w=$(fact "$rel" witness)$|  p=$(fact "$rel" phase); w=$(fact "$rel" witness)|'
out=$(run)
hit "$out" "the phase fact is read outside the two readers, or the recorded-phase allow-list disagrees with the source, so the effective phase and the recorded one can differ at a call site nobody classified"
hit "$out" "reads the phase fact directly inside verb_status()"

# ---- CHECK 39, arm two: the same read inside a function that also WRITES the phase. The exemption
# ---- is a LINE and never a function, so `verb_preflight`'s rotation test is graded although the
# ---- same function carries the `set_fact … phase RUNNING` guard the exemption covers. This is the
# ---- one live instance at BASE, and a function-wide exemption would cover five of the ten rows.
# ---- ANCHORED ON A TOKEN INSIDE THE FUNCTION, never on a whole line (TOOL-aGraftedHelix-34 S3): the
# ---- whole-line anchor this arm had stopped matching when the rotation test gained its settled-
# ---- abandoned clause, and `mutate` printed a no-op while the arm graded nothing. The call token
# ---- survives any rewrite of the condition around it.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh '/^verb_preflight() {/,/^}/ s|is_terminal "\$DP_PHASE"|is_terminal "$(fact "$rel" phase)"|'
out=$(run)
hit "$out" "reads the phase fact directly inside verb_preflight()"

# ---- CHECK 39, arm three: a `read_recorded_phase` call in a function the allow-list does not name.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh 's|^  read_derived_phase "$rel"; p="$DP_PHASE"$|  p=$(read_recorded_phase "$rel")|'
out=$(run)
hit "$out" "calls read_recorded_phase() inside verb_resume(), which the allow-list does not name"

# ---- CHECK 39, arm four: a STALE allow-list row. A row naming a function that no longer reads the
# ---- phase silently widens the very set it was written to narrow, so the join runs both ways.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/check-unattended.sh 's|^PHASE_RECORDED_FNS=.*|PHASE_RECORDED_FNS="refuse_if_terminal archive_name_of verb_landed print_liveness run_settle ghostfn"|'
out=$(run)
hit "$out" "the allow-list names ghostfn(), which no longer calls read_recorded_phase()"

# ---- CHECK 39, the CONTROL: the shipped driver and the shipped allow-list are silent. Without it
# ---- every arm above could be passing because the check reds on anything at all.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
out=$(run)
miss "$out" "the phase fact is read outside the two readers"
# ...and the liveness refusal below is silent over the shipped readers, or it could be passing
# because it reds on every driver.
miss "$out" "a phase reader holds no read the classifier recognises"

# ---- CHECK 1's CORE_FLOOR, over the PHASE half: deleting HELD reds against a floor of 13:12.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh 's/ HELD VERIFYING / VERIFYING /'
out=$(run)
hit "$out" "the kit's CORE phase vocabulary has shrunk below its floor"

# ---- CHECK 2's HOLD_FLOOR: deleting a hold code a sibling unit routes to reds the shrink-only pin.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh 's/ inherited-red / /'
out=$(run)
hit "$out" "the kit's CORE hold vocabulary has shrunk below its floor, and deleting a member is a silent, reason-free override of every record and every sibling unit that routes to it"

# ---- TOOL-dUnstuckLanding-13 AC11: the floor guards the two HAND-OFF codes too. The fixture's floor is
# ---- derived from the shipped driver, so it reads 7 with them in; dropping `owner-decision` alone
# ---- reds the pin naming both counts.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh 's/ owner-decision"$/"/'
out=$(run)
hit "$out" "the kit's CORE hold vocabulary has shrunk below its floor, and deleting a member is a silent, reason-free override of every record and every sibling unit that routes to it: 6 against 7"

# ---- ...and its two conf branches, which behave exactly as HALT_FLOOR's do: undeclared and
# ---- malformed are both REFUSALS, because a pin that quietly defaults is a pin nobody set.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate .unattended.conf 's/^HOLD_FLOOR=.*/HOLD_FLOOR=""/'
out=$(run)
hit "$out" "HOLD_FLOOR is undeclared in .unattended.conf, and with no floor a deleted hold code is indistinguishable from a vocabulary that never had one"

reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate .unattended.conf 's/^HOLD_FLOOR=.*/HOLD_FLOOR="five"/'
out=$(run)
hit "$out" "HOLD_FLOOR is not a single integer, so the shrink-only comparison below would be a string test wearing a numeric name"

# ---- The PHASE TAIL the gate-guard hook restates. HELD sits BEFORE VERIFYING, so the hook's own
# ---- parity arm keeps reading the list it already spells and a run held from BUILDING is refused
# ---- the flagged bar and the suites. Read off the shipped driver, never off a copy of the list.
n=$((n+1))
c39_tail=$(sed -n 's/^PHASES_CORE="\(.*\)"/\1/p' "$HERE/unattended.sh" | grep -o 'VERIFYING.*')
[ "$c39_tail" = "VERIFYING LANDING LANDED ABORTED" ] \
  || { echo "FAIL the driver's phase tail from VERIFYING is [$c39_tail], which is not the list gate-guard.js spells in PHASES_ALLOW"; st=1; }

# ---- CHECK 40: a phase another verb PRODUCES is not reachable through --phase. Dropping HELD's
# ---- guard makes one phase move write a HELD record with no held-at, hold-until, hold-code or
# ---- held-from — a pause nothing can evaluate and --resume cannot release.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh 's|^  if \[ "$want" = HELD \]; then$|  if [ "$want" = NEVERAPHASE ]; then|'
out=$(run)
hit "$out" "a phase another verb PRODUCES is reachable through --phase, so one phase move would write that phase with none of the facts its producer writes beside it, and the verb that releases it would have nothing to read"
hit "$out" "HELD"

# ---- ...and CHECK 40's CONTROL, for arm four's reason.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
out=$(run)
miss "$out" "a phase another verb PRODUCES is reachable through --phase"
reset_tree


# ---- the hold vocabulary's VACUITY arm: an empty core set makes the hold verb validate against
# ---- nothing and record a pause under any word at all.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh 's/^HOLD_CODES_CORE=.*/HOLD_CODES_CORE=""/'
out=$(run)
hit "$out" "the driver declares no HOLD_CODES_CORE vocabulary, so the hold verb would validate against an empty set and record a pause under any word at all"

# ---- TOOL-dUnstuckLanding-14 S1, closing review round 1 L5 (id 25): the HAND-OFF codes the leg reads
# ---- for its derived-LANDED predicate are guarded as the hold codes are. A renamed constant reads
# ---- empty, and a member outside the hold vocabulary is a hold no verb could record.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh 's/^HOLD_CODES_HANDOFF=/HOLD_CODES_HANDED=/'
hit "$(run)" "the driver declares no readable HOLD_CODES_HANDOFF, so this leg would derive LANDED for no handed record while the driver derives it for each"
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh 's/^HOLD_CODES_HANDOFF="owner-landing /HOLD_CODES_HANDOFF="owner-landed /'
hit "$(run)" "a hand-off code is not a member of the driver's HOLD_CODES_CORE, so a record could carry a hand-off the hold vocabulary refuses: owner-landed"
reset_tree

# ---- ...and check 39's own liveness refusal. A read predicate that matches nothing classifies
# ---- nothing, and grading no read is how a structural arm passes by finding nothing. Staged by
# ---- quoting the key in ONE reader's own read, `fact "$1" "phase"`: the same read to bash, a
# ---- spelling the predicate does not match, so every direct read spelled that way would be
# ---- invisible to it too. This arm used to REMOVE the driver, a state check 1 refuses and exits on
# ---- before check 39 runs, so it never passed; the leg's guard now asserts what can fail. One
# ---- `mutate` more than that arm, and the check-39 control above gained a `miss`: floors +2.
reset_tree
mkdir -p $KIT_REL && cp "$HERE/unattended.sh" "$HERE/lib-unattended.sh" $KIT_REL/
mutate $KIT_REL/unattended.sh 's/^  fact "\$1" phase$/  fact "$1" "phase"/'
out=$(run)
hit "$out" "a phase reader holds no read the classifier recognises, so its predicate no longer matches how the driver reads the fact and the routing below would be graded over no lines at all and would pass by finding nothing"
reset_tree

fi   # ---- a re-cut seam of the region-8 span (TOOL-aGraftedHelix-34 S7): the section below is region 1's
if in_shard 1; then
cd "$TMP" || exit 2; anchor_restore; read_topo s3   # every section after a re-cut seam starts from the prologue's fixture, refs and remote
# ---- TOOL-dDerivedDocket-3 — checks 44 and 45 (this build's 34 and 35, renumbered above main's 34 to 36) ----
# ---- ITS OWN scratch repository, for the reason the driver suite's sibling block gives: these arms
# ---- edit the SKILL TEMPLATE and the DRIVER the leg reads its closed set out of, and doing that in
# ---- the shared fixture would leave every later arm grading a mutated carrier.
# ----
# ---- EVERY RED ARM HAS A GREEN CONTROL, and the controls come first: a check that was never reached
# ---- is silent for the same reason a passing one is, and this leg's whole contract is that silence
# ---- means clean.
lm_dir=$(mktemp -d)
(
  cd "$lm_dir" || exit 2
  git init -q -b main . && git config user.email t@t.test && git config user.name t \
    && git config core.autocrlf false
  # THE KIT HOME IS THE SUITE'S OWN `$KIT_REL`, never a spelled prefix: the kit is installed and
  # run here at the same derived path the shared fixture uses, so the block grades at any prefix.
  mkdir -p "$KIT_REL" memory/guides
  cp "$HERE/check-unattended.sh" "$HERE/unattended.sh" "$HERE/lib-unattended.sh" \
     "$HERE/PROTOCOL.template.md" "$HERE/SKILL.template.md" "$HERE/VERBS.template.md" \
     "$HERE/STOPS.template.md" "$HERE/check-playbook.sh" "$HERE/PLAYBOOK-TEMPLATE.template.md" \
     "$HERE/.unattended.conf.example" "$KIT_REL/"
  cp "$HERE/PROTOCOL.template.md" memory/guides/UNATTENDED-PROTOCOL.md
  cp "$HERE/VERBS.template.md" memory/guides/UNATTENDED-VERBS.md
  cp "$HERE/ASKS.template.md" "$KIT_REL/"
  cp "$HERE/ASKS.template.md" memory/guides/UNATTENDED-ASKS.md
  cp "$HERE/STOPS.template.md" memory/guides/UNATTENDED-STOPS.md
  # LANDER is graded for presence only (check 1), so it carries the shared fixture's inert value.
  cat > .unattended.conf <<'LMC'
MEMORY_ROOT=memory
LANDER="echo land"
LANDER_MODE="in-place"
BYPASS_BAN="--no-verify"
GATE_CMD="true"
WIRING_CHECK="true"
KEEPALIVE_CREATE="CronCreate"
KEEPALIVE_DELETE="CronDelete"
LMC
  # The owed surface is the kit home this block installs, so it resolves to tracked paths here.
  printf 'SELFTESTS_OWED_PATHS="%s/"\n' "$KIT_REL" >> .unattended.conf
  git add -A >/dev/null && git commit -q -m seed --no-verify
) >/dev/null 2>&1
# The Land SECTION alone, rewritten in place. A file-wide edit would also move the Close section,
# which names `--prepare` too, so an arm made that way could not tell the two apart.

# ---- GREEN CONTROLS: the shipped Land section passes, and both announcements are on the DEFAULT
# ---- channel, because a reader of a green bar is owed the landing shape and the declared surface.
out=$(lmrun)
miss "$out" "check 44 FAILED"
hit  "$out" "LANDER_MODE in-place (declared)"
hit  "$out" "SELFTESTS_OWED_PATHS entry $KIT_REL/ — resolves to tracked paths"

# ---- 44: the Land section without `--prepare`, and without `--land`. Two arms, because a section
# ---- missing either one sends an agent to a landing it cannot complete and the messages differ.
LMFROM="--prepare" lmland "--ready" sub
out=$(lmrun)
hit "$out" "the Skill's Land section names neither landing shape in full - an in-place landing prepares the merge and then pushes exactly it, and a section missing either verb sends an agent to a landing it cannot complete"
lmrestore "$KIT_REL/SKILL.template.md"
LMFROM="--land" lmland "--ship" sub
out=$(lmrun)
hit "$out" "and a section missing either verb sends an agent to a landing it cannot complete"
lmrestore "$KIT_REL/SKILL.template.md"

# ---- 44: the primary path's fallback text surviving into the Land section. It is wrong twice over
# ---- under `in-place`: that ref is one the session can move, and it carries whatever else on the
# ---- node is unpushed. PLACED UNDER THE LAND HEADING, never appended: Land is not the template's
# ---- last section, so an EOF append lands in whichever section closes the file and the
# ---- section-scoped check never reads it.
awk '{ print } /^## Land[ \t]*$/ { print ""; print "If the push fails, merge the branch into local main and land from the primary tree." }' \
  "$lm_dir/$KIT_REL/SKILL.template.md" > "$lm_dir/.land.tmp" \
  && mv "$lm_dir/.land.tmp" "$lm_dir/$KIT_REL/SKILL.template.md"
out=$(lmrun)
hit "$out" "the Skill's Land section directs a merge into the node's own default branch, which is a ref this session can move and which carries whatever else here is unpushed, so the landing it describes is not the one the bar graded"
lmrestore "$KIT_REL/SKILL.template.md"

# ---- 44: an EMPTY section. Without this arm the two above would pass over nothing the day the
# ---- section is renamed, which is this leg's own could-not-fail shape one level up.
lmland "" empty
out=$(lmrun)
hit "$out" "the Skill template carries no Land section body, so every assertion about the landing an agent is told to perform would be graded over nothing and would pass by finding nothing"
lmrestore "$KIT_REL/SKILL.template.md"

# ---- 45: a declared mode outside the DRIVER's own closed set. Every run in such a project refuses
# ---- at conf load, so the bar must say so rather than leave it to the next invocation.
sed -i 's/^LANDER_MODE=.*/LANDER_MODE="inplace"/' "$lm_dir/.unattended.conf"
out=$(lmrun)
hit "$out" "LANDER_MODE is declared outside the driver's closed set, so every run in this project refuses at conf load and no landing is reachable at all, declared"
lmrestore .unattended.conf

# ---- 45: a declared self-test prefix that matches no tracked path reads as coverage of a surface
# ---- that is not there. A BLANK key is not a fault and is announced instead.
sed -i "s|^SELFTESTS_OWED_PATHS=.*|SELFTESTS_OWED_PATHS=\"$KIT_REL/ nosuchdir/\"|" "$lm_dir/.unattended.conf"
out=$(lmrun)
hit "$out" "SELFTESTS_OWED_PATHS declares a prefix that matches no tracked path, so it reads as coverage of a surface that is not in this tree and a run of kit work under it would never be told the flagged bar is owed"
lmrestore .unattended.conf
sed -i 's|^SELFTESTS_OWED_PATHS=.*|SELFTESTS_OWED_PATHS=""|' "$lm_dir/.unattended.conf"
out=$(lmrun)
hit  "$out" "SELFTESTS_OWED_PATHS is blank — no run's range in this project can ever be told the kit Definition of Done owes the flagged bar"
miss "$out" "check 45 FAILED"
lmrestore .unattended.conf

# ---- 45: the DRIVER's marker removed. The closed set is read off the driver's own line rather than
# ---- retyped here, so a marker that stops resolving must REFUSE: a set read as empty would make
# ---- every declared value, including a misspelling, read as legal.
sed -i '/gov:lander-mode-set/d' "$lm_dir/$KIT_REL/unattended.sh"
out=$(lmrun)
hit "$out" "this leg cannot read the closed LANDER_MODE set and its default off the driver's own marked lines, so the declared mode would be graded against an empty set and every value, including a misspelling, would read as legal"
lmrestore "$KIT_REL/unattended.sh"


# ---- 46: the DURABLE restart carrier, TOOL-dDerivedDocket-5. GREEN CONTROL first: this conf
# ---- declares no switch at all, which is the population every upgrading adopter is in, and the
# ---- effective value has to be ANNOUNCED rather than silently applied. AC1 says the default does
# ---- not red ON THAT ACCOUNT, and S1 requires the carrier pair while the value is on, so the control
# ---- declares the pair (apart from the keepalive's tools) and leaves the switch alone: without the
# ---- pair the switch-on-no-carrier refusal below fires here, and the control grades that instead.
printf 'RESUME_SCHEDULE_CREATE="TheScheduleCreate"\nRESUME_SCHEDULE_DELETE="TheScheduleDelete"\n' >> "$lm_dir/.unattended.conf"
out=$(lmrun)
hit  "$out" "RESUME_SCHEDULE on (defaulted)"
miss "$out" "check 46 FAILED"
lmrestore .unattended.conf

# ---- 46: an unrecognised spelling. The driver refuses it at conf load, so every verb in such a
# ---- project is unreachable and a leg that resolved it silently to either value would be reporting
# ---- about a project that cannot run at all.
printf 'RESUME_SCHEDULE="maybe"\n' >> "$lm_dir/.unattended.conf"
out=$(lmrun)
hit "$out" "RESUME_SCHEDULE is declared outside the driver's closed set, so every run in this project refuses at conf load and no verb is reachable at all, declared"
lmrestore .unattended.conf

# ---- 46: the switch on and no carrier declared. Undeclared is not defaulted: every hold such a
# ---- project takes records `none · no carrier` and pauses with nothing filed to restart it.
printf 'RESUME_SCHEDULE="on"\n' >> "$lm_dir/.unattended.conf"
out=$(lmrun)
hit "$out" "(declared) and this key is undeclared, so every hold this project takes records 'none · no carrier' and pauses with nothing filed to restart it; declare the pair, or write RESUME_SCHEDULE=\"off\""
hit "$out" "RESUME_SCHEDULE_DELETE"
lmrestore .unattended.conf

# ---- 46: the carrier declared as the KEEPALIVE's own create tool. That store is session-scoped by
# ---- this project's own conf, so every restart filed there dies with the session it exists to
# ---- outlive — and the hold that filed it reads as owing a restart that can never fire.
printf 'RESUME_SCHEDULE="on"\nRESUME_SCHEDULE_CREATE="CronCreate"\nRESUME_SCHEDULE_DELETE="CronDelete"\n' >> "$lm_dir/.unattended.conf"
out=$(lmrun)
hit "$out" "the declared durable restart carrier is the keepalive's own create tool, and that store is session-scoped, so every restart filed there dies with the session it exists to outlive: RESUME_SCHEDULE_CREATE and KEEPALIVE_CREATE are both"
lmrestore .unattended.conf

# ---- 46: OFF is a legal declaration and is announced, not a refusal. A project may decide that
# ---- every held run waits for a person, and a leg that red on that would be policy, not a check.
printf 'RESUME_SCHEDULE="off"\n' >> "$lm_dir/.unattended.conf"
out=$(lmrun)
hit  "$out" "RESUME_SCHEDULE is off — no hold in this project owes a durable restart, and every held run waits for a person to type --resume"
miss "$out" "check 46 FAILED"
lmrestore .unattended.conf

# ---- 46: the DRIVER's marker removed, on check 45's own terms. A set read as empty would make
# ---- every declared value, a misspelling included, read as legal.
sed -i '/gov:resume-schedule-set/d' "$lm_dir/$KIT_REL/unattended.sh"
out=$(lmrun)
hit "$out" "this leg cannot read the closed RESUME_SCHEDULE set and its default off the driver's own marked lines, so the declared switch would be graded against an empty set and every value, a misspelling included, would read as legal"
lmrestore "$KIT_REL/unattended.sh"

rm -rf "$lm_dir"

fi   # ---- a re-cut seam of the region-8 span (TOOL-aGraftedHelix-34 S7): the section below is region 8's
if in_shard 8; then
cd "$TMP" || exit 2; anchor_restore; read_topo s4   # every section after a re-cut seam starts from the prologue's fixture, refs and remote
# ==== TOOL-dDerivedDocket-52: resolve_introducing_commit, over scratch fixtures ==================
# THE FUNCTION IS EXTRACTED AND SOURCED, the way the driver suite's bound arms grade `run_bounded`:
# nothing calls this resolver at its own commit — unit 18's S2 is its first caller, at a later order
# — so a suite that ran the leg would grade a code path no check reaches yet. An EMPTY extraction is
# a refusal rather than a silent skip, because a sourced empty file defines no function and every
# assertion below would then grade the shell's "command not found".
#
# EVERY FIXTURE IS ITS OWN REPOSITORY, outside the scratch tree: the arms need rotations, merges,
# shallow clones and windows deeper than a cap, and none of those may be staged in the tree whose
# cleanliness the controls above depend on. `reset_tree` would delete them anyway.
#
# NO ARM READS THE REAL TREE. No tracked record carries the facts these arms grade until unit 35
# arms gov, so a real-tree assertion here would be an assertion about nothing.
#
# COST: eight repositories, about sixty commits and forty resolver calls, measured at 13 s on node d
# 2026-09-21 running this block standalone. Process creation is this suite's cost centre and its
# budget row is in the run-gates kit's selftest-budgets.txt; 13 s against that row needs no raise.
# PRISTINE FIRST. Every arm above that mutates the fixture's copy of the kit restores it, but the
# extraction below reads that copy, and an arm that graded a leg some earlier block left mutated
# would be grading someone else's break. This costs a reset and removes the question.
reset_tree
ric_fn=$(mktemp)
sed -n '/^resolve_introducing_commit() {/,/^}$/p' "$SCRIPT" > "$ric_fn"
[ -s "$ric_fn" ] || { echo "FAIL could not extract resolve_introducing_commit from $SCRIPT — every arm below would grade nothing"; st=1; }
ric_root=$(mktemp -d)
ric_d=memory/builds/b
# ONE CALL, IN A SUBSHELL, so the `cd` and the sourced kit library cannot reach the arms that follow
# — and the assertions stay in THIS shell, where `n` and `st` live. A subshell that ran the
# assertions too would lose every failure it found.
# A FIXTURE THAT DID NOT BUILD COMPARES TWO EMPTIES AND PASSES. Every sha below is derived from the
# fixture by `git log --grep`, and an arm asserting an empty answer against an empty expectation is
# the fixture-passes-by-finding-nothing class in its purest form — so each derivation is refused
# before it is used.

# ---- FIXTURE A: a record rotated by a later run's preflight, the shape `--preflight` actually
# ---- writes — a staged `git mv` inside the folder plus a fresh live record in the same commit.
ric_a=$ric_root/a; ric_init "$ric_a"
( cd "$ric_a" || exit 2
  printf 'phase: LANDED\nm-base: AAAA\nanchor-kind: default-branch\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm "run one preflight"
  echo x >> seed.txt; git add seed.txt; git commit -qm "body one"
  git mv $ric_d/RUN.md $ric_d/RUN.LANDED.deadbeef.md
  printf 'phase: BUILDING\nm-base: BBBB\nanchor-kind: default-branch\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md $ric_d/RUN.LANDED.deadbeef.md
  git commit -qm "run two preflight, prior LANDED retired"
  echo y >> seed.txt; git add seed.txt; git commit -qm "body two" ) >/dev/null 2>&1
ric_a_pre=$(git -C "$ric_a" log --format=%H --grep='run one preflight')
ric_a_rot=$(git -C "$ric_a" log --format=%H --grep='run two preflight')
ric_want "fixture A's preflight commit" "$ric_a_pre"
ric_want "fixture A's rotation commit" "$ric_a_rot"

# ---- AC1: the archived record grades against the value ITS OWN run recorded. A path-scoped search
# ---- answers the rotation here, which is a wrong sha and not a missing one.
ric_out=$(ric "$ric_a" "$ric_d/RUN.LANDED.deadbeef.md" "m-base: AAAA" 2>"$ric_root/err"); ric_err=$(cat "$ric_root/err")
same "AC1 a rotated record answers its own preflight commit" "$ric_out" "$ric_a_pre"
same "AC1 an answer prints no reason line" "$ric_err" ""
n=$((n+1)); [ "$ric_out" != "$ric_a_rot" ] || { echo "FAIL AC1 the resolver answered the ROTATION commit, so a caller would re-derive a base nobody wrote"; st=1; }

# ---- AC8: two tenancies at ONE path, sharing a line byte for byte. The floor is what separates
# ---- them; the verification step cannot and is not asked to.
ric_out=$(ric "$ric_a" "$ric_d/RUN.md" "anchor-kind: default-branch" 2>"$ric_root/err")
same "AC8 the live record answers the SECOND tenancy's own preflight" "$ric_out" "$ric_a_rot"
ric_unfloored=$(git -C "$ric_a" rev-list --full-history --reverse HEAD -- $ric_d/RUN.md | head -1)
same "AC8 control: the UNFLOORED walk answers the first run's commit instead" "$ric_unfloored" "$ric_a_pre"
ric_out=$(ric "$ric_a" "$ric_d/RUN.md" "m-base: BBBB" 2>"$ric_root/err")
same "AC2 the second tenancy's own line is introduced at its own preflight" "$ric_out" "$ric_a_rot"

# ---- FIXTURE B: the rotation lands inside a MERGE commit. The obvious spelling for either end of
# ---- the window — the newest `--diff-filter=A` at the path — answers NOTHING here under both
# ---- spellings, because git computes no diff for a merge. Both ends are resolved by first TOUCH.
ric_b=$ric_root/b; ric_init "$ric_b"
( cd "$ric_b" || exit 2
  printf 'phase: LANDED\nm-base: AAAA\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm "run one preflight"
  git checkout -qb side; echo s > side.txt; git add side.txt; git commit -qm "side work"
  git checkout -q main; echo m > main.txt; git add main.txt; git commit -qm "main work"
  git merge -q --no-commit --no-ff side
  git mv $ric_d/RUN.md $ric_d/RUN.LANDED.deadbeef.md
  printf 'phase: BUILDING\nm-base: BBBB\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md $ric_d/RUN.LANDED.deadbeef.md
  git commit -qm "merge side; run two preflight"
  echo z >> main.txt; git add main.txt; git commit -qm after ) >/dev/null 2>&1
ric_b_pre=$(git -C "$ric_b" log --format=%H --grep='run one preflight')
ric_want "fixture B's preflight commit" "$ric_b_pre"
ric_out=$(ric "$ric_b" "$ric_d/RUN.LANDED.deadbeef.md" "m-base: AAAA" 2>"$ric_root/err")
same "AC4 a rotation inside a merge still answers the preflight commit" "$ric_out" "$ric_b_pre"
same "AC4 control: the add search answers nothing there, plain" \
  "$(git -C "$ric_b" log --diff-filter=A --format=%H -- $ric_d/RUN.LANDED.deadbeef.md)" ""
same "AC4 control: and nothing with --full-history either" \
  "$(git -C "$ric_b" log --full-history --diff-filter=A --format=%H -- $ric_d/RUN.LANDED.deadbeef.md)" ""

# ---- FIXTURE C: an `-s ours` merge, the shape the drift-audit kit's drift_report.py reproduced for
# ---- this same flag. The commit that introduced the line is TREESAME-pruned out of a simplified
# ---- walk, so the simplified spelling answers nothing at all — an absent answer wearing the face
# ---- of a clean one.
ric_c=$ric_root/c; ric_init "$ric_c"
( cd "$ric_c" || exit 2
  printf 'phase: BUILDING\nm-base: AAAA\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm "run one preflight"
  git checkout -qb side
  printf 'phase: BUILDING\nm-base: AAAA\nasks-at-landing: 3\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm "side touches the record"
  git checkout -q main; echo m > main.txt; git add main.txt; git commit -qm "main work"
  git merge -q -s ours --no-ff side -m "merge side, ours"
  echo z >> main.txt; git add main.txt; git commit -qm after ) >/dev/null 2>&1
ric_c_side=$(git -C "$ric_c" log --all --format=%H --grep='side touches the record')
ric_want "fixture C's pruned side commit" "$ric_c_side"
ric_out=$(ric "$ric_c" "$ric_d/RUN.md" "asks-at-landing: 3" 2>"$ric_root/err")
same "AC4 the unsimplified walk reaches the pruned commit that introduced the line" "$ric_out" "$ric_c_side"
same "AC4 control: a simplified walk cannot see that commit at all" \
  "$(git -C "$ric_c" rev-list HEAD -- $ric_d/RUN.md | grep -cF "$ric_c_side")" "0"

# ---- FIXTURE D: a shallow clone. Every file in a graft commit reads as INTRODUCED there, so the
# ---- floor — the one place this resolver stops applying the parent test — would hand back a
# ---- confident wrong sha. It refuses instead, and says which refusal it is.
ric_dd=$ric_root/d; ric_init "$ric_dd"
( cd "$ric_dd" || exit 2
  printf 'phase: BUILDING\nm-base: AAAA\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm "run one preflight"
  printf 'phase: BUILDING\nm-base: AAAA\nwitness: c0ffee\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm "witness recorded"
  printf 'phase: LANDING\nm-base: AAAA\nwitness: c0ffee\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm landing ) >/dev/null 2>&1
git clone -q --depth 1 --no-local "file://$ric_dd" "$ric_root/d-shallow" >/dev/null 2>&1
ric_out=$(ric "$ric_root/d-shallow" "$ric_d/RUN.md" "m-base: AAAA" 2>"$ric_root/err"); ric_err=$(cat "$ric_root/err")
same "AC3 a shallow clone answers nothing" "$ric_out" ""
hit "$ric_err" "the range could not be resolved - the oldest end of the window names a parent this repository does not have"

# ---- FIXTURE E: a record with no committed history at all — the tenancy floor cannot be resolved,
# ---- which is a DIFFERENT unknown from "the window held no introduction" and says so.
ric_e=$ric_root/e; ric_init "$ric_e"
printf 'phase: BUILDING\nm-base: AAAA\n' > "$ric_e/$ric_d/RUN.md"
ric_out=$(ric "$ric_e" "$ric_d/RUN.md" "m-base: AAAA" 2>"$ric_root/err"); ric_err=$(cat "$ric_root/err")
same "AC8 an unresolvable tenancy floor answers nothing" "$ric_out" ""
hit  "$ric_err" "the tenancy floor could not be resolved"
miss "$ric_err" "the whole tenancy window was walked"

# ---- FIXTURE F: a tenancy window DEEPER than the cap, with the line introduced at its oldest end.
# ---- `--max-count` applies during a newest-first traversal, so a capped walk keeps the wrong end;
# ---- the cap therefore detects the window rather than selecting one.
ric_f=$ric_root/f; ric_init "$ric_f"
( cd "$ric_f" || exit 2
  printf 'phase: BUILDING\nm-base: AAAA\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm "run one preflight"
  i=0; while [ $i -lt 8 ]; do i=$((i+1))
    printf 'phase: BUILDING\nm-base: AAAA\npass: %s\n' "$i" > $ric_d/RUN.md
    git add $ric_d/RUN.md; git commit -qm "pass $i"
  done ) >/dev/null 2>&1
ric_f_pre=$(git -C "$ric_f" log --format=%H --grep='run one preflight')
ric_want "fixture F's preflight commit" "$ric_f_pre"
ric_out=$(ric "$ric_f" "$ric_d/RUN.md" "m-base: AAAA" 4 2>"$ric_root/err"); ric_err=$(cat "$ric_root/err")
same "AC6 a window deeper than the cap answers nothing" "$ric_out" ""
hit  "$ric_err" "the tenancy window is deeper than the 4-commit walk cap"
miss "$ric_err" "the whole tenancy window was walked"
ric_out=$(ric "$ric_f" "$ric_d/RUN.md" "m-base: AAAA" 400 2>"$ric_root/err"); ric_err=$(cat "$ric_root/err")
same "AC6 the same fixture answers once the cap is raised past the window" "$ric_out" "$ric_f_pre"
same "AC6 and that answer prints no reason line" "$ric_err" ""

# ---- FIXTURE G: deeper than the cap AND carrying an introduce-remove-re-introduce shape inside the
# ---- window. A window that merely lacks its answer cannot tell a walk that ANNOUNCES from one that
# ---- answers wrongly: here a sentinel met mid-walk returns the RE-introduction, with no reason
# ---- line at all, which is a wrong sha wearing the face of an answer.
ric_g=$ric_root/g; ric_init "$ric_g"
( cd "$ric_g" || exit 2
  printf 'phase: BUILDING\nm-base: AAAA\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm "run one preflight"
  i=0; while [ $i -lt 4 ]; do i=$((i+1))
    printf 'phase: BUILDING\npass: %s\n' "$i" > $ric_d/RUN.md
    git add $ric_d/RUN.md; git commit -qm "pass $i, the line removed"
  done
  i=0; while [ $i -lt 3 ]; do i=$((i+1))
    printf 'phase: BUILDING\nm-base: AAAA\nlate: %s\n' "$i" > $ric_d/RUN.md
    git add $ric_d/RUN.md; git commit -qm "late $i, the line back"
  done ) >/dev/null 2>&1
ric_g_pre=$(git -C "$ric_g" log --format=%H --grep='run one preflight')
ric_g_re=$(git -C "$ric_g" log --format=%H --grep='late 1, the line back')
ric_want "fixture G's preflight commit" "$ric_g_pre"
ric_want "fixture G's re-introduction commit" "$ric_g_re"
ric_out=$(ric "$ric_g" "$ric_d/RUN.md" "m-base: AAAA" 4 2>"$ric_root/err"); ric_err=$(cat "$ric_root/err")
same "AC6 the re-introduction fixture answers nothing at a cap below its window" "$ric_out" ""
hit  "$ric_err" "the tenancy window is deeper than the 4-commit walk cap"
n=$((n+1)); [ "$ric_out" != "$ric_g_re" ] || { echo "FAIL AC6 the truncated walk returned the RE-introduction among its retained newest commits"; st=1; }
ric_out=$(ric "$ric_g" "$ric_d/RUN.md" "m-base: AAAA" 400 2>"$ric_root/err")
same "AC6 control: uncapped, the same fixture answers the FIRST introduction" "$ric_out" "$ric_g_pre"

# ---- FIXTURE H: a candidate whose FIRST PARENT already carries the line. The boundary here is an
# ---- archived sibling filed on its own, so the floor is not itself a candidate and the oldest
# ---- candidate is not an introduction. Returned unverified it would be a wrong sha; passed over it
# ---- leaves the window with no introduction in it, which is the truth and is announced as such.
ric_h=$ric_root/h; ric_init "$ric_h"
( cd "$ric_h" || exit 2
  printf 'phase: LANDED\nm-base: AAAA\nanchor-kind: default-branch\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm "run one preflight"
  printf 'phase: LANDED\nm-base: AAAA\nanchor-kind: default-branch\n' > $ric_d/RUN.ABORTED.cafebabe.md
  git add $ric_d/RUN.ABORTED.cafebabe.md; git commit -qm "an archived sibling filed on its own"
  printf 'phase: LANDED\nm-base: AAAA\nanchor-kind: default-branch\nwitness: c0ffee\n' > $ric_d/RUN.md
  git add $ric_d/RUN.md; git commit -qm "the record is touched, the line unchanged" ) >/dev/null 2>&1
ric_out=$(ric "$ric_h" "$ric_d/RUN.md" "m-base: AAAA" 2>"$ric_root/err"); ric_err=$(cat "$ric_root/err")
same "AC2 a candidate whose first parent carries the line is passed over" "$ric_out" ""
hit  "$ric_err" "the whole tenancy window was walked and no commit in it introduced that line"
ric_h_tip=$(git -C "$ric_h" rev-parse HEAD 2>/dev/null)
ric_want "fixture H's tip" "$ric_h_tip"
ric_out=$(ric "$ric_h" "$ric_d/RUN.md" "witness: c0ffee" 2>"$ric_root/err")
same "AC2 control: a genuine introduction inside the same window IS answered" "$ric_out" "$ric_h_tip"

# ---- AC7: the header states what the resolver does NOT answer, in ONE sentence naming BOTH limits.
# ---- A header that states only what a function does is how a resolution gets read as a guarantee.
same "AC7 the resolver's header names both limits, once" \
  "$(grep -cF "answers only inside the queried record's own tenancy of that path, says nothing about an earlier" "$SCRIPT")" "1"
hit "$(sed -n '/answers only inside the queried/,+2p' "$SCRIPT")" "does not follow a record moved out of its build folder"

rm -f "$ric_fn"; rm -rf "$ric_root"


fi   # ---- a re-cut seam of the region-8 span (TOOL-aGraftedHelix-34 S7): the section below is region 5's
if in_shard 5; then
cd "$TMP" || exit 2; anchor_restore; read_topo s5   # every section after a re-cut seam starts from the prologue's fixture, refs and remote
# ---- TOOL-dDerivedDocket-18: THE ASK-MANDATE SECOND OPINIONS ------------------------------------
# Six arms over the four facts the ask path pins (`asks:`, `m-base:`, `asks-ready:` and the
# `asks-at-landing:` freeze), each observed RED here and each beside the control that shows the
# break is the only thing that changed. The leg re-derives every fact from inputs the run cannot
# move; a fixture that let the run move them would grade the leg against itself.
#
# ITS OWN REPOSITORY, outside the scratch tree, for the reason the resolver block above gives: the
# arms need a second branch, a pushed tip, a remote whose HEAD can be repointed and a build folder
# whose README carries an `asks:` line AT THE ANCHOR, and `reset_tree` would delete all of it.
#
# THE RECALL KIT'S REAL EXTRACTOR, copied in. S3's whole claim is that it judges an anchor by that
# kit's `anchor_at` and holds no copy of its shapes, so a fixture carrying a stub extractor would be
# grading a double this block wrote - a green arm over a shape the real callee never returns.
#
# THE STUB PRODUCER READS ITS TABLE AT THE REV IT IS ASKED ABOUT, so an arm can tell "re-derived at
# the pinned tree" from "re-derived at HEAD": a table that moves after the pin changes the answer
# only for a leg that asked about the wrong tree.
#
# `--skip 28` ON EVERY RUN. These arms live in the per-record loop, and check 28 is half the leg's
# wall clock and none of this block's subject.
reset_tree
ak_root=$(mktemp -d)
ak="$ak_root/repo"; ak_origin="$ak_root/origin.git"
ak_R=memory/builds/tRun/RUN.md
ak_B=memory/builds/tRun/README.md
mkdir -p "$ak/$KIT_REL" "$ak/rk" "$ak/memory/guides" "$ak/memory/builds/tRun" "$ak/memory/builds/aFoo"
cp "$TMP/$KIT_REL/check-unattended.sh" "$TMP/$KIT_REL/unattended.sh" "$TMP/$KIT_REL/lib-unattended.sh" \
   "$TMP/$KIT_REL/check-playbook.sh" "$TMP/$KIT_REL/PROTOCOL.template.md" "$TMP/$KIT_REL/SKILL.template.md" \
   "$TMP/$KIT_REL/VERBS.template.md" "$TMP/$KIT_REL/PLAYBOOK-TEMPLATE.template.md" \
   "$TMP/$KIT_REL/.unattended.conf.example" "$ak/$KIT_REL/"
cp "$TMP/$KIT_REL/PROTOCOL.template.md" "$ak/memory/guides/UNATTENDED-PROTOCOL.md"
cp "$TMP/$KIT_REL/VERBS.template.md" "$ak/memory/guides/UNATTENDED-VERBS.md"
cp "$TMP/$KIT_REL/ASKS.template.md" "$ak/$KIT_REL/"
cp "$TMP/$KIT_REL/ASKS.template.md" "$ak/memory/guides/UNATTENDED-ASKS.md"
# the recall kit's extractor and its conf reader, into a directory the declared RECALL_CLI names
# FOUND by the file only that kit holds, never by a typed kit directory (the carried-prefix ban).
_rk_rel=$(git -C "$HERE" ls-files --full-name -- ':(top)*recall_conf.py' | head -n 1)
_rk_src="$(git -C "$HERE" rev-parse --show-toplevel)/${_rk_rel%/*}"
cp "$_rk_src/extract.py" "$_rk_src/recall_conf.py" "$ak/rk/"
n=$((n+1)); [ -f "$ak/rk/extract.py" ] || { echo "FAIL the ask block could not copy the recall kit's extractor, so every S3 arm below would grade a missing grammar"; st=1; }
printf 'MEMORY_ROOT=memory\nFAMILIES="example:EXMP tooling:TOOL"\n' > "$ak/.memory-tree.conf"
cat > "$ak/.unattended.conf" <<AKCONF
MEMORY_ROOT=memory
LANDER="echo land"
BYPASS_BAN="--no-verify"
GATE_CMD="true"
WIRING_CHECK="true"
CORE_FLOOR="$CORE_FLOOR_DERIVED"
KEEPALIVE_CREATE="CronCreate"
KEEPALIVE_DELETE="CronDelete"
PHASES_EXTRA=""
DOD_EXTRA=""
DIRECTIVES_EXTRA=""
DIRECTIVES_FLOOR="$DIRECTIVES_FLOOR_DERIVED"
DIRECTIVES_EXTRA_TABLE=""
HALT_CODES_EXTRA=""
HALT_FLOOR="$HALT_FLOOR_DERIVED"
HOLD_CODES_EXTRA=""
HOLD_FLOOR="$HOLD_FLOOR_DERIVED"
RECALL_CLI="rk/query.py"
ASKS_CMD="bash stub-asks.sh"
AKCONF
cat > "$ak/stub-asks.sh" <<'AKSTUB'
#!/usr/bin/env bash
set -u
ids=""; mode=""; rev=""
for a in "$@"; do
  case "$a" in
    --ready) mode=ids; continue ;;
    --at) mode=at; continue ;;
    --*) mode=""; continue ;;
  esac
  [ "$mode" = ids ] && ids="$ids $a"
  [ "$mode" = at ] && rev="$a"
done
tbl=$(git show "$rev:stub-table.txt" 2>/dev/null)
k=0
for i in $ids; do
  s=$(printf '%s\n' "$tbl" | sed -n "s/^$i status //p"); [ -n "$s" ] || s=OPEN
  r=$(printf '%s\n' "$tbl" | sed -n "s/^$i ready //p"); [ -n "$r" ] || r=yes
  printf 'ask\t%s\t%s\tnobody\t-\tHIGH\t%s\t-\t-\t-\t-\n' "$i" "$s" "$r"
  k=$((k+1))
done
printf 'examined\t%s\n' "$k"
AKSTUB
printf 'EXMP-aFoo-3 ready yes\nEXMP-aFoo-3 status OPEN\n' > "$ak/stub-table.txt"
printf '# aFoo asks\n\n- EXMP-aFoo-3 · filed 2026-09-01 · unit · do the thing\n' > "$ak/memory/builds/aFoo/BACKLOG.md"
printf -- '---\nslug: tRun\nnode: a\nopened: 2026-08-01\nstreams: architecture\nroster: TOOL\nids: TOOL-tRun-1\nasks: EXMP-aFoo-3\n---\n\n# tRun\n\n<!-- gen:build-index -->\n<!-- gen:build-units -->\n<!-- /gen:build-units -->\n<!-- /gen:build-index -->\n' > "$ak/$ak_B"
printf '# tRun - run state\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nphase: RUNNING\nwitness: WITNESS\nbase: BASE\nmode: slug\nasks: EXMP-aFoo-3\n' > "$ak/$ak_R"
(
  cd "$ak" || exit 2
  git init -q -b main . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
  git add -A >/dev/null && git commit -q -m base --no-verify
  printf 'a second commit, so the anchor has an OLDER ancestor to forge a pin to\n' > second.txt
  git add -A >/dev/null && git commit -q -m second --no-verify
  git init -q --bare "$ak_origin"
  git --git-dir="$ak_origin" symbolic-ref HEAD refs/heads/main
  git remote add origin "$ak_origin" && git push -q origin main
  git checkout -q -b unit && git commit -q --allow-empty -m "unit work" --no-verify
  # THE THREE PINNED ASK FACTS IN ONE COMMIT, which is what preflight's staging produces, so the
  # commit introducing `m-base:` is findable and its first parent is HEAD at preflight.
  # FROM THE LOCAL `main`, not `origin/main`: the tracking ref exists only if the push above
  # succeeded, and a push that failed would leave both pins EMPTY while every arm below went on
  # grading a record that pins nothing.
  mb=$(git merge-base main HEAD)
  sed -i "s|^witness: WITNESS$|witness: $(git rev-parse HEAD)|; s|^base: BASE$|base: $mb|" "$ak_R"
  printf 'anchor-sha: %s\nm-base: %s\nasks-ready: EXMP-aFoo-3=yes\n' "$(git rev-parse main)" "$mb" >> "$ak_R"
  git add -A >/dev/null && git commit -q -m facts --no-verify
)
AK_PRISTINE=$(git -C "$ak" rev-parse HEAD); AK_ANCHOR=$(git -C "$ak" rev-parse main); AK_C1=$(git -C "$ak" rev-parse main~1)
# THE FIXTURE MUST ACTUALLY PIN SOMETHING, and the remote must actually hold the anchor: a build that
# half-failed would red thirty arms below for a reason none of them names.
n=$((n+1)); { grep -qE '^m-base: [0-9a-f]{40}$' "$ak/$ak_R" && [ "$(git --git-dir="$ak_origin" rev-parse main 2>/dev/null)" = "$AK_ANCHOR" ]; } \
  || { echo "FAIL the ask block's fixture pinned no m-base or its remote holds no anchor, so every arm below would grade a record that pins nothing"; st=1; }

# control: the conforming mandated record fires none of the six arms, and says what it examined
set_ak_pristine; out=$(run_ak_leg)
miss "$out" "UNATTENDED check 19 FAILED"
miss "$out" "UNATTENDED check 15 FAILED"
miss "$out" "UNATTENDED check 37 FAILED"
hit  "$out" "check 37 found no foreign anchor under memory/builds/tRun"
hit  "$out" "the ask-mandate second opinions examined 1 run-state record(s) pinning an asks: fact"

# AC1: the pinned fact differs by one id from the README line at the recorded BASE
set_ak_pristine; sed -i 's/^asks: EXMP-aFoo-3$/asks: EXMP-aFoo-3 EXMP-aFoo-4/' "$ak/$ak_R"; out=$(run_ak_leg)
hit "$out" "a run-state file pins an asks: mandate the build README at its own recorded BASE does not declare, so the set the run says authorized it is not the set its authorization asked for - pinned against declared follow: ["
hit "$out" "pinned against declared follow: [EXMP-aFoo-3 EXMP-aFoo-4] against [EXMP-aFoo-3]"

# CLOSING REVIEW F2: the pinned value reads through the driver's own IDLIST reader, ALL OR NOTHING.
# A comma-suffixed token reds BY NAME rather than dropping out of every arm keyed on the ids; a `-N`
# continuation is an id, so P5 looks for the row it names. RED under the binding-line expander this
# replaced, which read the first record as no id at all and the second as `-3` alone.
set_ak_pristine; sed -i 's/^asks: EXMP-aFoo-3$/asks: EXMP-aFoo-3,/' "$ak/$ak_R"; out=$(run_ak_leg)
hit "$out" "a run-state file pins an asks: mandate that does not read whole as an id list, so every arm below would grade the ids that did parse and the owner's own list would narrow with the leg green: "
hit "$out" "\`EXMP-aFoo-3,\` (neither an id, an id range, nor a -N continuation)"
set_ak_pristine; sed -i 's/^asks: EXMP-aFoo-3$/asks: EXMP-aFoo-3 -4/' "$ak/$ak_R"; out=$(run_ak_leg)
hit  "$out" "EXMP-aFoo-4, wanted in memory/builds/aFoo/BACKLOG.md"
miss "$out" "does not read whole as an id list"

# AC2: a LIVE record's README edited at HEAD reds; the same edit under a record past its close does not
set_ak_pristine; sed -i 's/^asks: EXMP-aFoo-3$/asks: EXMP-aFoo-3 EXMP-aFoo-4/' "$ak/$ak_B"; add_ak_commit "head edit"; out=$(run_ak_leg)
hit "$out" "a LIVE run's build README carries an asks: line at HEAD that is not the one the run pinned, so the mandate this run will be measured against was edited underneath it - pinned against HEAD follow: ["
set_ak_pristine; sed -i 's/^asks: EXMP-aFoo-3$/asks: EXMP-aFoo-3 EXMP-aFoo-4/' "$ak/$ak_B"
sed -i 's/^phase: RUNNING$/phase: LANDING/' "$ak/$ak_R"; add_ak_commit "head edit under LANDING"; out=$(run_ak_leg)
miss "$out" "carries an asks: line at HEAD that is not the one the run pinned"
hit  "$out" "which is past its close, and the pinned-mandate property binds a LIVE run"
set_ak_pristine; sed -i 's/^asks: EXMP-aFoo-3$/asks: EXMP-aFoo-3 EXMP-aFoo-4/' "$ak/$ak_B"
mutate "$ak/$ak_R" 's/^phase: RUNNING$/phase: LANDED/'
printf 'asks-at-landing: EXMP-aFoo-3=OPEN\nlanded-anchor: local\n' >> "$ak/$ak_R"; add_ak_commit "head edit under LANDED"; out=$(run_ak_leg)
miss "$out" "carries an asks: line at HEAD that is not the one the run pinned"

# AC3: no filed row for the mandated ask in its home BACKLOG at the recorded m-base. The anchor moves
# too, so the equality arm stays green and this is the only refusal the fixture can reach.
set_ak_pristine
( cd "$ak" && git checkout -q main && sed -i '/EXMP-aFoo-3/d' memory/builds/aFoo/BACKLOG.md \
    && git commit -q -am "drop the ask row" --no-verify && git push -q -f origin main \
    && git checkout -q unit && git merge -q --no-edit main >/dev/null 2>&1 \
    && nm=$(git rev-parse main) \
    && sed -i "s|^m-base: .*|m-base: $nm|; s|^anchor-sha: .*|anchor-sha: $nm|; s|^base: .*|base: $nm|" "$ak_R" \
    && git commit -q -am "re-record against the row-less anchor" --no-verify )
out=$(run_ak_leg)
hit  "$out" "a mandated ask has no filed row in the tree this run pinned its mandate against, so the run was authorized by a record that tree does not carry and could have written the row itself"
hit  "$out" "EXMP-aFoo-3, wanted in memory/builds/aFoo/BACKLOG.md"
miss "$out" "is not the merge-base of the anchor it pinned"

# AC4: base: and m-base: forged TOGETHER to an older ancestor of anchor-sha still red, naming m-base:
set_ak_pristine; sed -i "s|^m-base: .*|m-base: $AK_C1|; s|^base: .*|base: $AK_C1|" "$ak/$ak_R"; add_ak_commit "forge the pair"; out=$(run_ak_leg)
hit "$out" "a run-state file's m-base: is not the merge-base of the anchor it pinned and the tree its own preflight stood on, so the tree its mandate was asserted against was chosen rather than derived - recorded against re-derived follow: ["
hit "$out" "[$AK_C1] against [$AK_ANCHOR]"
# ...an m-base: line no commit introduced falls back to ANCESTRY and says so, and S8 skips by name
set_ak_pristine; sed -i "s|^m-base: .*|m-base: $AK_C1|" "$ak/$ak_R"; out=$(run_ak_leg)
hit  "$out" "FELL BACK TO ANCESTRY for the m-base:"
hit  "$out" "SKIPPED the pin re-derivation"
miss "$out" "is not an ancestor of both the anchor it pinned"
# ...and the fallback is a test that can fail: a pin OFF the anchor's history reds under it
set_ak_pristine; sed -i "s|^m-base: .*|m-base: $(git -C "$ak" rev-parse HEAD~1)|" "$ak/$ak_R"; out=$(run_ak_leg)
hit "$out" "a run-state file's m-base: is not an ancestor of both the anchor it pinned and this working history, so the tree its mandate was asserted against does not lie on the history that authorized the run: m-base ["
# ...and an m-base: nothing can read is its own refusal rather than a skip
set_ak_pristine; sed -i '/^m-base: /d' "$ak/$ak_R"; out=$(run_ak_leg)
hit "$out" "a run-state file pins an asks: mandate and no m-base: this clone can read, so every property about the tree that mandate was asserted against would be graded over an empty blob or, worse, over the index the run itself staged: m-base ["

# AC5: a backticked foreign id in a table row's first cell ANCHORS; a link-wrapped one does not
set_ak_pristine
printf '# notes\n\n| `TOOL-zOther-7` | a foreign id, backticked |\n| [TOOL-zOther-8](x.md) | a foreign id, link-wrapped |\n' > "$ak/memory/builds/tRun/notes.md"
add_ak_commit "foreign anchors"; out=$(run_ak_leg)
hit  "$out" "a mandated run's own build folder ANCHORS a record id belonging to another build, so this folder is a second claimant for an id it does not own and the two builds' records can no longer be told apart"
hit  "$out" "memory/builds/tRun/notes.md:3:TOOL-zOther-7"
miss "$out" "TOOL-zOther-8"

# AC6: a blank RECALL_CLI is a named skip, never zero anchors found
set_ak_pristine
printf '# notes\n\n| `TOOL-zOther-7` | a foreign id, backticked |\n' > "$ak/memory/builds/tRun/notes.md"
sed -i 's|^RECALL_CLI=.*|RECALL_CLI=""|' "$ak/.unattended.conf"; add_ak_commit "blank recall cli"; out=$(run_ak_leg)
hit  "$out" "check 37 SKIPPED for memory/builds/tRun"
hit  "$out" "RECALL_CLI is blank in this project"
miss "$out" "ANCHORS a record id belonging to another build"

# AC7: a LANDED record under a mandate with no freeze (its control is AC12b's record below)
set_ak_pristine; sed -i 's/^phase: RUNNING$/phase: LANDED/' "$ak/$ak_R"; printf 'landed-anchor: local\n' >> "$ak/$ak_R"
add_ak_commit "landed, no freeze"; out=$(run_ak_leg)
hit "$out" "a record claims LANDED under an asks: mandate and freezes no answer to it, so what that run actually answered is whatever the tree says today rather than what it said at landing"

# AC8: EVERY member of the driver's second-anchor set is refused, read from the constant; and a slug
# record under a blank ASKS_CMD is refused by the conf half alone
ak_modes=$(sed -n 's/^SECOND_ANCHOR_MODES="\(.*\)"$/\1/p' "$TMP/$KIT_REL/unattended.sh")
n=$((n+1)); [ -n "$ak_modes" ] || { echo "FAIL the driver's SECOND_ANCHOR_MODES read empty, so the mode arms below would loop over nothing"; st=1; }
for ak_m in $ak_modes; do
  set_ak_pristine; sed -i "s/^mode: slug$/mode: $ak_m/" "$ak/$ak_R"; out=$(run_ak_leg)
  hit "$out" "a run-state file pins an asks: mandate while recording an authorization mode whose discipline lets the run reach the anchor it writes, so the mandate and the tree it is asserted against could both be this run's own: mode ["
done
set_ak_pristine; sed -i 's|^ASKS_CMD=.*|ASKS_CMD=""|' "$ak/.unattended.conf"; out=$(run_ak_leg)
hit  "$out" "a run-state file pins an asks: mandate while this project declares no ASKS_CMD, so nothing here or in the driver ever said whether any of that mandate is executable and every check keyed on it passes over an ungraded list"
miss "$out" "recording an authorization mode whose discipline"

# AC9's direct form: a tree where no record pins an asks: fact announces the vacuity with its count
set_ak_pristine; sed -i '/^asks: EXMP-aFoo-3$/d' "$ak/$ak_R" "$ak/$ak_B"; add_ak_commit "no mandate anywhere"; out=$(run_ak_leg)
hit "$out" "0 run-state records pin an asks: fact"

# AC11: a forged grade on an UNPUBLISHED record reds naming both pairs...
set_ak_pristine; sed -i 's/^asks-ready: .*/asks-ready: EXMP-aFoo-3=no/' "$ak/$ak_R"; add_ak_commit "forge the grade"; out=$(run_ak_leg)
hit "$out" "a run-state file's asks-ready: is not what the declared producer says at the very tree the run pinned, so the grades that mandate was admitted on are not the producer's - recorded against re-derived follow: ["
hit "$out" "[EXMP-aFoo-3=no] against [EXMP-aFoo-3=yes]"
# ...the same forgery once PUBLISHED is counted and not re-derived...
set_ak_pristine; sed -i 's/^asks-ready: .*/asks-ready: EXMP-aFoo-3=no/' "$ak/$ak_R"; add_ak_commit "forge the grade"
git -C "$ak" push -q -f origin HEAD:main; out=$(run_ak_leg)
miss "$out" "is not what the declared producer says at the very tree the run pinned"
hit  "$out" "is published, not re-derived"
# ...a producer past the bound is UNANSWERED and never a red...
set_ak_pristine; mutate "$ak/$KIT_REL/unattended.sh" 's/^REMOTE_BOUND="[0-9]*"/REMOTE_BOUND="2"/'
printf '#!/usr/bin/env bash\nsleep 30\n' > "$ak/stub-asks.sh"
sed -i 's/^asks-ready: .*/asks-ready: EXMP-aFoo-3=no/' "$ak/$ak_R"; add_ak_commit "a stalled producer over a forged grade"; out=$(run_ak_leg)
hit  "$out" "UNANSWERED rather than red"
hit  "$out" "was KILLED by this leg's wall-clock bound"
miss "$out" "is not what the declared producer says at the very tree the run pinned"
# ...an unobserved default tip re-derives EVERY mandated record and prints why...
set_ak_pristine; git --git-dir="$ak_origin" symbolic-ref HEAD refs/heads/nothing-here; out=$(run_ak_leg)
hit "$out" "re-deriving the pins of EVERY mandated record because this run observed no readable default-branch tip"
git --git-dir="$ak_origin" symbolic-ref HEAD refs/heads/main
# ...and a producer whose answer MOVED after the pin is graded at the pinned tree, not at HEAD
set_ak_pristine; mutate "$ak/stub-table.txt" 's/^EXMP-aFoo-3 ready yes$/EXMP-aFoo-3 ready no/'
add_ak_commit "the table moves after the pin"; out=$(run_ak_leg)
miss "$out" "is not what the declared producer says at the very tree the run pinned"

# AC12: a forged freeze on an unpublished record reds naming both...
set_ak_pristine; sed -i 's/^phase: RUNNING$/phase: LANDED/' "$ak/$ak_R"
printf 'asks-at-landing: EXMP-aFoo-3=CLOSED\nlanded-anchor: local\n' >> "$ak/$ak_R"; add_ak_commit "forge the freeze"; out=$(run_ak_leg)
hit "$out" "a landed record's asks-at-landing: is not what the declared producer says at the tree its landing verb examined, so the answer frozen into a terminal record is not the one that tree gives - recorded against re-derived follow: ["
hit "$out" "[EXMP-aFoo-3=CLOSED] against [EXMP-aFoo-3=OPEN]"
# ...a REOPEN at HEAD does not red a PUBLISHED record...
set_ak_pristine; sed -i 's/^phase: RUNNING$/phase: LANDED/' "$ak/$ak_R"
printf 'asks-at-landing: EXMP-aFoo-3=CLOSED\nlanded-anchor: local\n' >> "$ak/$ak_R"; add_ak_commit "the freeze"
git -C "$ak" push -q -f origin HEAD:main
mutate "$ak/stub-table.txt" 's/^EXMP-aFoo-3 status OPEN$/EXMP-aFoo-3 status REOPEN/'
add_ak_commit "a later REOPEN"; out=$(run_ak_leg)
miss "$out" "is not what the declared producer says at the tree its landing verb examined"
# ...nor an UNPUBLISHED one, whose freeze is graded at the tree the landing examined. This record
# is also AC7's control: LANDED, mandated, and carrying its freeze.
set_ak_pristine; sed -i 's/^phase: RUNNING$/phase: LANDED/' "$ak/$ak_R"
mutate "$ak/stub-table.txt" 's/^EXMP-aFoo-3 status OPEN$/EXMP-aFoo-3 status CLOSED/'
add_ak_commit "the tree the landing examined"
printf 'asks-at-landing: EXMP-aFoo-3=CLOSED\nlanded-anchor: local\n' >> "$ak/$ak_R"; add_ak_commit "the freeze"
sed -i 's/^EXMP-aFoo-3 status CLOSED$/EXMP-aFoo-3 status REOPEN/' "$ak/stub-table.txt"; add_ak_commit "a later REOPEN"; out=$(run_ak_leg)
miss "$out" "is not what the declared producer says at the tree its landing verb examined"
miss "$out" "freezes no answer to it"

# AC13: a freeze that omits one mandated id reds naming that id
set_ak_pristine; sed -i 's/^asks: EXMP-aFoo-3$/asks: EXMP-aFoo-3 EXMP-aFoo-4/' "$ak/$ak_R"
sed -i 's/^phase: RUNNING$/phase: LANDED/' "$ak/$ak_R"
printf 'asks-at-landing: EXMP-aFoo-3=OPEN\nlanded-anchor: local\n' >> "$ak/$ak_R"; add_ak_commit "freeze missing an id"; out=$(run_ak_leg)
hit "$out" "a landed record's asks-at-landing: omits an ask its own mandate names, so that ask's answer at landing is lost and the freeze covers less than the question the run was authorized by"
hit "$out" "EXMP-aFoo-4 in memory/builds/tRun/RUN.md"

# THE ROTATED RECORD, which is where S2 meets TOOL-dDerivedDocket-52's resolver for the first time
# (that unit's AC1 and AC3 left their check-19 half to this commit). The anchor MOVES after
# preflight, the run merges it, lands and is rotated by the next preflight, so HEAD-at-preflight and
# the rotation's first parent have DIFFERENT merge-bases with the pinned anchor. A resolver that
# answered the rotation commit would grade this honest archived record against a base nobody wrote.
set_ak_pristine
( cd "$ak" && git checkout -q main && printf 'the anchor moves after preflight\n' > third.txt \
    && git add -A >/dev/null && git commit -q -m "main moves" --no-verify && git push -q -f origin main \
    && nm=$(git rev-parse main) && git checkout -q unit \
    && sed -i "s|^anchor-sha: .*|anchor-sha: $nm|" "$ak_R" && git commit -q -am "the anchor preflight observed" --no-verify \
    && git merge -q --no-edit main >/dev/null 2>&1 \
    && sed -i 's/^phase: RUNNING$/phase: LANDED/' "$ak_R" \
    && printf 'asks-at-landing: EXMP-aFoo-3=OPEN\nlanded-anchor: local\n' >> "$ak_R" \
    && git commit -q -am "land" --no-verify \
    && git mv "$ak_R" memory/builds/tRun/RUN.LANDED.deadbeef.md \
    && printf '# tRun - run state\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nphase: RUNNING\nwitness: %s\nbase: %s\n' "$(git rev-parse HEAD)" "$nm" > "$ak_R" \
    && git add -A >/dev/null && git commit -q -m "the next preflight rotates the record" --no-verify )
out=$(run_ak_leg)
miss "$out" "is not the merge-base of the anchor it pinned"
miss "$out" "FELL BACK TO ANCESTRY for the m-base: of memory/builds/tRun/RUN.LANDED.deadbeef.md"
hit  "$out" "the ask-mandate second opinions examined 1 run-state record(s) pinning an asks: fact"


# ---- TOOL-dDerivedDocket-22 S15 / AC14: under `in-place` landing the freeze is due at the CLOSE, so a
# ---- COMMITTED LANDING record carrying `asks:` and no `asks-at-landing:` reds; under `primary` the same
# ---- record does not, because there the freeze is `--landed`'s; and with the fact present it passes.
set_ak_pristine; printf 'LANDER_MODE="in-place"\nLANDER="echo land"\n' >> "$ak/.unattended.conf"
sed -i 's/^phase: RUNNING$/phase: LANDING/' "$ak/$ak_R"; add_ak_commit "committed LANDING, no freeze"; out=$(run_ak_leg)
hit "$out" "a committed LANDING record under an asks: mandate carries no asks-at-landing:, and under in-place landing --close writes that freeze beside the phase, so the record the push carries answers nothing about the question the run was authorized by: memory/builds/tRun/RUN.md"
set_ak_pristine
sed -i 's/^phase: RUNNING$/phase: LANDING/' "$ak/$ak_R"; add_ak_commit "committed LANDING under primary"; out=$(run_ak_leg)
miss "$out" "a committed LANDING record under an asks: mandate carries no asks-at-landing:"
set_ak_pristine; printf 'LANDER_MODE="in-place"\nLANDER="echo land"\n' >> "$ak/.unattended.conf"
sed -i 's/^phase: RUNNING$/phase: LANDING/' "$ak/$ak_R"; printf 'asks-at-landing: EXMP-aFoo-3=OPEN\n' >> "$ak/$ak_R"
add_ak_commit "committed LANDING, frozen at close"; out=$(run_ak_leg)
miss "$out" "a committed LANDING record under an asks: mandate carries no asks-at-landing:"
miss "$out" "freezes no answer to it"
rm -rf "$ak_root"

fi   # ---- a re-cut seam of the region-8 span (TOOL-aGraftedHelix-34 S7): the section below is region 8's
if in_shard 8; then
cd "$TMP" || exit 2; anchor_restore; read_topo s6   # every section after a re-cut seam starts from the prologue's fixture, refs and remote
# ==== TOOL-dDerivedDocket-54: check_touching_commit_reachable, over one scratch fixture ==========
# SOURCED FROM THE KIT LIBRARY rather than extracted: the predicate lives in `lib-unattended.sh`,
# which defines functions and nothing else, so sourcing it is exactly how its callers reach it.
# Nothing calls it at its own commit - the terminal-record exclusion is its first caller, at a later
# order - so a suite that ran the leg would grade a code path no check reaches yet.
#
# THE SUBJECT IS A PARENT, NEVER THE WITNESS. The caller asks once per parent of each merge on a
# witness's tail, and the one parent at which the simplified and unsimplified spellings disagree is
# a parent that is ITSELF a merge, TREESAME to one of its own parents for the record's path. At a
# plain parent the simplified spelling is already right, so an arm graded there certifies nothing.
# The fixture's witness therefore takes such a NESTED merge as its first parent and an unrelated
# side branch off BASE as its second, and every yes/no arm below grades one of those two parents.
#
# ITS OWN REPOSITORY, outside the scratch tree, for the reason the two blocks above give. The walks
# are COUNTED through git's own trace rather than through a shim over the wrapper, so the empty-BASE
# arm can assert the refusal came BEFORE any walk, and a control below proves the counter moves.
reset_tree
tc_root=$(mktemp -d)
tc_fx=$tc_root/fx
tc_P=memory/builds/b/RUN.md
# ONE CALL, IN A SUBSHELL, so the `cd` and the sourced library reach no arm that follows, and the
# assertions stay in THIS shell, where `n` and `st` live. The STATUS is the answer, so it is printed
# as `rc=<n>` and is the only stdout a call may carry; the reason line lands in `err`.
mkdir -p "$tc_fx/memory/builds/b"
( cd "$tc_fx" || exit 2
  git init -q -b main . && git config user.email t@t.test && git config user.name t \
    && git config core.autocrlf false
  printf 'phase: BUILDING\n' > $tc_P; echo seed > seed.txt
  git add $tc_P seed.txt; git commit -qm "base"
  git checkout -qb side; echo s > side.txt; git add side.txt; git commit -qm "side work"
  git checkout -q main; git checkout -qb run
  printf 'phase: LANDED\n' > $tc_P; git add $tc_P; git commit -qm "run touches the record"
  git checkout -q main; echo m > main.txt; git add main.txt; git commit -qm "default branch work"
  git merge -q --no-ff --no-commit run
  printf 'phase: BUILDING\n' > $tc_P; git add $tc_P
  git commit -qm "nested merge resolves the record to the default side"
  git merge -q --no-ff -m "witness" side ) >/dev/null 2>&1
tc_base=$(git -C "$tc_fx" log --format=%H --grep='^base$')
tc_nest=$(git -C "$tc_fx" rev-parse --verify --quiet 'HEAD^1' 2>/dev/null)
tc_other=$(git -C "$tc_fx" rev-parse --verify --quiet 'HEAD^2' 2>/dev/null)
# A FIXTURE THAT DID NOT BUILD COMPARES EMPTIES, and every arm below would then grade a refusal of
# its own inputs. The shape is asserted, not inferred: the first parent is a merge, and it is TREESAME
# to its default-branch parent for the record's path and not to its run-branch parent.
n=$((n+1)); [ -n "$tc_base" ] && [ -n "$tc_nest" ] && [ -n "$tc_other" ] \
  || { echo "FAIL the TOOL-dDerivedDocket-54 fixture derived no base, nested parent or other parent - every arm below would grade nothing"; st=1; }
same "fixture: the witness's first parent is itself a merge" \
  "$(git -C "$tc_fx" rev-parse --verify --quiet "$tc_nest^2" >/dev/null 2>&1 && echo merge)" "merge"
same "fixture: the nested merge is TREESAME to its default-branch parent for the record" \
  "$(git -C "$tc_fx" diff --name-only "$tc_nest^1" "$tc_nest" -- $tc_P)" ""
same "fixture: the nested merge is NOT treesame to its run-branch parent for the record" \
  "$(git -C "$tc_fx" diff --name-only "$tc_nest^2" "$tc_nest" -- $tc_P)" "$tc_P"

# ---- AC1: the nested-merge PARENT answers yes, and the simplified spelling answers nothing for that
# ---- same parent - rows 5 and 6 of the spec's table, reproduced here rather than quoted.
same "AC1 the witness's nested-merge parent answers yes" \
  "$(run_touching_probe "$tc_fx" "$tc_nest" "$tc_base" "$tc_P")" "rc=0"
same "AC1 a yes prints no reason line" "$(cat "$tc_root/err")" ""
same "AC1 control: the walk counter counts the one walk that ran" \
  "$(cat "$tc_root/trace" 2>/dev/null | grep -c 'built-in: git rev-list')" "1"
same "AC1 control: the SIMPLIFIED spelling answers nothing for that same parent" \
  "$(git -C "$tc_fx" rev-list -1 "$tc_nest" "^$tc_base" -- $tc_P)" ""
same "AC1 control: the unsimplified spelling answers the nested merge for it" \
  "$(git -C "$tc_fx" rev-list --full-history -1 "$tc_nest" "^$tc_base" -- $tc_P)" "$tc_nest"

# ---- AC2: the witness's OTHER parent reaches no touching commit and answers no, so exactly one
# ---- side is excluded. Without this, a predicate that now matches everything passes AC1.
same "AC2 the witness's other parent answers no" \
  "$(run_touching_probe "$tc_fx" "$tc_other" "$tc_base" "$tc_P")" "rc=1"
same "AC2 a no prints no reason line, so it cannot be mistaken for a refusal" "$(cat "$tc_root/err")" ""

# ---- AC3: three BASEs that fail three different ways. Not an object: any spelling catches it.
same "AC3 a BASE that is not an object cannot answer" \
  "$(run_touching_probe "$tc_fx" "$tc_nest" 0123456789abcdef0123456789abcdef01234567 "$tc_P")" "rc=2"
hit "$(cat "$tc_root/err")" "check_touching_commit_reachable cannot answer for commit [$tc_nest] and path [$tc_P]"
# ---- ...EMPTY: the range spelling would exit 0 printing nothing, byte-identical to an honest no,
# ---- and the caret spelling would fail closed for free - so the arm asserts NO WALK RAN.
same "AC3 an empty BASE cannot answer" "$(run_touching_probe "$tc_fx" "$tc_nest" "" "$tc_P")" "rc=2"
hit "$(cat "$tc_root/err")" "the BASE is empty or blank, so no walk was started"
same "AC3 an empty BASE is refused WITHOUT walking" \
  "$(cat "$tc_root/trace" 2>/dev/null | grep -c 'built-in: git rev-list')" "0"
# ---- ...a legal object of another TYPE: `^<object>` excludes nothing, so a non-empty test lets the
# ---- walk answer a confident YES over the whole history. The control proves this fixture shows it.
tc_blob=$(git -C "$tc_fx" rev-parse --verify --quiet "$tc_base:$tc_P" 2>/dev/null)
tc_tree=$(git -C "$tc_fx" rev-parse --verify --quiet "$tc_base^{tree}" 2>/dev/null)
n=$((n+1)); [ -n "$(git -C "$tc_fx" rev-list --full-history -1 "$tc_other" "^$tc_blob" -- $tc_P 2>/dev/null)" ] \
  || { echo "FAIL AC3 control: a blob BASE excluded something here, so the wrong-type arm below grades nothing"; st=1; }
same "AC3 a BLOB BASE gives no answer rather than a yes" \
  "$(run_touching_probe "$tc_fx" "$tc_other" "$tc_blob" "$tc_P")" "rc=2"
hit "$(cat "$tc_root/err")" "does not resolve to a commit"
same "AC3 a TREE BASE gives no answer rather than a yes" \
  "$(run_touching_probe "$tc_fx" "$tc_other" "$tc_tree" "$tc_P")" "rc=2"

# ---- The other cannot-answer branches, each a distinct status from the honest no.
same "an unknown commit cannot answer" "$(run_touching_probe "$tc_fx" deadbeef "$tc_base" "$tc_P")" "rc=2"
hit "$(cat "$tc_root/err")" "the commit does not resolve to a commit in this history"
same "a blank path cannot answer" "$(run_touching_probe "$tc_fx" "$tc_nest" "$tc_base" " ")" "rc=2"
hit "$(cat "$tc_root/err")" "the path is empty or blank"
same "a walk git refuses cannot answer" "$(run_touching_probe "$tc_fx" "$tc_nest" "$tc_base" ../outside)" "rc=2"
hit "$(cat "$tc_root/err")" "the walk itself failed"
# the path is LITERAL: as a pattern this one matches the record and would answer yes
same "a glob-shaped path is one literal path, which nothing touched" \
  "$(run_touching_probe "$tc_fx" "$tc_nest" "$tc_base" 'memory/builds/*/RUN.md')" "rc=1"
# a shallow clone keeping every commit, BASE included, so only the shallowness can refuse it
git clone -q --depth 3 --no-local "file://$tc_fx" "$tc_root/shallow" >/dev/null 2>&1
same "a shallow clone cannot answer" "$(run_touching_probe "$tc_root/shallow" "$tc_nest" "$tc_base" "$tc_P")" "rc=2"
hit "$(cat "$tc_root/err")" "this clone is shallow"

# ---- AC4: the header sentence naming the simplification, ONCE, naming both the TREESAME shape and
# ---- the existence-only limit. A flag with no clause beside it survives until the next tidy reader.
same "AC4 the header sentence naming the simplification appears once" \
  "$(grep -cF 'THE WALK IS UNSIMPLIFIED ON PURPOSE' "$TMP/$KIT_REL/lib-unattended.sh")" "1"
hit "$(sed -n '/THE WALK IS UNSIMPLIFIED ON PURPOSE/,+4p' "$TMP/$KIT_REL/lib-unattended.sh")" "TREESAME to one side for that path"
hit "$(sed -n '/THE WALK IS UNSIMPLIFIED ON PURPOSE/,+4p' "$TMP/$KIT_REL/lib-unattended.sh")" "EXISTENCE only, never which commit"

rm -rf "$tc_root"
fi   # ---- a re-cut seam of the region-8 span (TOOL-aGraftedHelix-34 S7): the section below is region 6's
if in_shard 6; then
cd "$TMP" || exit 2; anchor_restore; read_topo s7   # every section after a re-cut seam starts from the prologue's fixture, refs and remote
# ==== TOOL-dDerivedDocket-19: THE GRANT, SECOND-OPINIONED ========================================
# Three arms of check 19 over the `may:` fact. The first two compare the fact against the README at
# the recorded BASE and against the recorded mode; the third walks each run's OWN commits for a
# commit that writes a `may:` line into any build README.
#
# THE THIRD ARM IS WHY THESE ARE SEVERAL REPOSITORIES. It reads a record's range off the SHAPE of
# the history behind its witness - a prepared merge, a plain reconcile, a primary landing merge, a
# fix commit on top of one, push-main's own reconcile - and the scratch tree above is one linear
# history `reset_tree` rewinds. Each group builds its own repository with a bare origin, from ONE
# builder, so every graph starts from the same BASE and differs only in what it is testing.
#
# EVERY GRAPH CARRIES BOTH SIDES OF THE QUESTION. An OWNER commit on the default branch, made after
# BASE, adds a grant to `tOther` - the channel ruling D12-j keeps open, which must never red - and
# the RUN's own commit adds one to `tOther2`, which must always red. An arm asserting only the red
# half would pass a walk over `base..HEAD`, and one asserting only the quiet half would pass a walk
# over nothing. `--skip 28` on every run, for the reason the ask block above gives.
reset_tree
ma_root=$(mktemp -d)
# BASE is the commit named `second`, found by subject so a moved `main` can never re-point it.
# THE BUILDER. BASE is `second` on main; the run branch `unit` opens with the record's first commit
# (its facts), then the RUN'S grant to tOther2, then ordinary work; main then takes the OWNER'S grant
# to tOther and is pushed. What each group does after that is the thing it tests.
MA_RUN_RD="in memory/builds/tOther2/README.md, run memory/builds/tRun/RUN.md"
MA_OWN_RD="in memory/builds/tOther/README.md, run"
MA_WRITES="a commit among a run's own commits writes a may: line into a build README, so a run could land the grant the next run would be authorized by - commit and README follow:"

# ---- G0: THE FACT AGAINST THE README AT BASE (AC4), THE MODE (AC5), AND THE TWO SPELLINGS (AC3). Four
# ---- records in one tree, each named in every message, so one run grades all four at once.
ma0="$ma_root/g0"
mkdir -p "$ma0/$KIT_REL" "$ma0/memory/guides"
cp "$TMP/$KIT_REL/check-unattended.sh" "$TMP/$KIT_REL/unattended.sh" "$TMP/$KIT_REL/lib-unattended.sh" \
   "$TMP/$KIT_REL/check-playbook.sh" "$TMP/$KIT_REL/PROTOCOL.template.md" "$TMP/$KIT_REL/SKILL.template.md" \
   "$TMP/$KIT_REL/VERBS.template.md" "$TMP/$KIT_REL/PLAYBOOK-TEMPLATE.template.md" \
   "$TMP/$KIT_REL/.unattended.conf.example" "$ma0/$KIT_REL/"
cp "$TMP/$KIT_REL/PROTOCOL.template.md" "$ma0/memory/guides/UNATTENDED-PROTOCOL.md"
cp "$TMP/$KIT_REL/VERBS.template.md" "$ma0/memory/guides/UNATTENDED-VERBS.md"
cp "$TMP/$KIT_REL/ASKS.template.md" "$ma0/$KIT_REL/"
cp "$TMP/$KIT_REL/ASKS.template.md" "$ma0/memory/guides/UNATTENDED-ASKS.md"
cp "$TMP/.unattended.conf" "$ma0/.unattended.conf"
# THE GRANT IS SPELLED ONCE (TOOL-aGraftedHelix-34 S3). A landing merge respelled this path in the
# READMEs, the liveness grep and the expected sentences and left the three seds writing the old one,
# so the fixture built records whose grant matched nothing and four arms redded. Every seed, sed, grep
# and sentence below reads this variable, so one edit moves them all or none.
MA0_GRANT=bin/lander-granted.sh
ma_readme "$ma0" tRun
ma_readme "$ma0" tTick "may: \`$MA0_GRANT\`"
ma_readme "$ma0" tBare "may: $MA0_GRANT"
ma_readme "$ma0" tPrompt 'authorized-by: prompt'
for ma_s in tRun tTick tBare tPrompt; do ma_run "$ma0" "$ma_s"; done
sed -i 's/^mode: slug$/mode: prompt/' "$ma0/memory/builds/tPrompt/RUN.md"
sed -i "s|^may: none\$|may: $MA0_GRANT|" "$ma0/memory/builds/tTick/RUN.md" "$ma0/memory/builds/tBare/RUN.md"
( cd "$ma0" || exit 2
  git init -q -b main . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
  git add -A >/dev/null && git commit -q -m base --no-verify
  git init -q --bare "$ma0.git" && git --git-dir="$ma0.git" symbolic-ref HEAD refs/heads/main
  git remote add origin "$ma0.git" && git push -q origin main
  git checkout -q -b unit && git commit -q --allow-empty -m "unit work" --no-verify ) >/dev/null 2>&1
for ma_s in tRun tTick tBare tPrompt; do ma_facts "$ma0" "$ma_s" RUNNING unit main; done
ma_commit "$ma0" facts
MA0_PRISTINE=$(ma_sha "$ma0" HEAD)
n=$((n+1)); { [ -n "$MA0_PRISTINE" ] && grep -qxF "may: $MA0_GRANT" "$ma0/memory/builds/tTick/RUN.md" \
  && grep -qxF "may: \`$MA0_GRANT\`" "$ma0/memory/builds/tTick/README.md"; } \
  || { echo "FAIL the TOOL-dDerivedDocket-19 G0 fixture did not build its four records, so every arm below would grade a missing one"; st=1; }

# control: the backticked and the bare README both agree with a bare fact (AC3's leg half), and the
# honest `none` records fire nothing
out=$(ma_leg "$ma0")
miss "$out" "pins a may: grant the build README at its own recorded BASE does not declare"
miss "$out" "pins a may: grant while recording an authorization mode that resolves at the second anchor"
miss "$out" "$MA_WRITES"
hit  "$out" "the ask-mandate second opinions (checks 19, 15 and 37) are VACUOUS on this tree"
# AC4: a fact that differs from the README's line at BASE reds, naming both values
ma0_reset; sed -i "s|^may: none\$|may: $MA0_GRANT|" "$ma0/memory/builds/tRun/RUN.md"; ma_commit "$ma0" forged
out=$(ma_leg "$ma0")
hit "$out" "a run-state file pins a may: grant the build README at its own recorded BASE does not declare, so the authority the run says its owner committed is not the authority that README carries - pinned against declared follow: ["
hit "$out" "pinned against declared follow: [$MA0_GRANT] against [none] in memory/builds/tRun/RUN.md"
# ...and against BASE, never HEAD: the README edited on the run branch to match the fact still reds
ma_grant "$ma0" tRun "$MA0_GRANT"; ma_commit "$ma0" "matched at head"
out=$(ma_leg "$ma0")
hit "$out" "pinned against declared follow: [$MA0_GRANT] against [none] in memory/builds/tRun/RUN.md"
# AC5: a `prompt` record carrying a grant reds by its mode, whatever its README says
ma0_reset; sed -i "s|^may: none\$|may: $MA0_GRANT|" "$ma0/memory/builds/tPrompt/RUN.md"; ma_commit "$ma0" "prompt grant"
out=$(ma_leg "$ma0")
hit "$out" "a run-state file pins a may: grant while recording an authorization mode that resolves at the second anchor, so the grant could be one the run wrote for itself - ruling D12-j honours a grant only under slug: mode [prompt], may: [$MA0_GRANT] in memory/builds/tPrompt/RUN.md"


# ---- TOOL-aWardedAudit-5: THE SPEC-AUDIT OPT-IN IS A GRANT TOO. A live record on the builder's graph,
# ---- whose run then writes a blank default (no opt-in), a dated default and a `spec-audit:` line,
# ---- while the OWNER's commit on main writes `spec-audit:` into another README. Observed RED-first
# ---- against the base checker, which read `may:` alone.
ma_init gsa; masa="$ma_root/gsa"
printf 'SPEC_AUDIT_DEFAULT=""\n' >> "$masa/.unattended.conf"; ma_commit "$masa" "run blanks the default"
printf 'SPEC_AUDIT_DEFAULT="2026-10-05"\n' >> "$masa/.unattended.conf"; ma_commit "$masa" "run dates the default"
sed -i '/^slug: tOther3$/a spec-audit: 2026-10-05' "$masa/memory/builds/tOther3/README.md"; ma_commit "$masa" "run opts in"
( cd "$masa" && git checkout -q main ) >/dev/null 2>&1
sed -i '/^slug: tOther$/a spec-audit: 2026-10-05' "$masa/memory/builds/tOther/README.md"; ma_commit "$masa" "owner opts in"
( cd "$masa" && git push -q origin main && git checkout -q unit ) >/dev/null 2>&1
MASA_BLANK=$(git -C "$masa" log --format=%H --grep='^run blanks the default$' -1)
MASA_DATE=$(git -C "$masa" log --format=%H --grep='^run dates the default$' -1)
MASA_KEY=$(git -C "$masa" log --format=%H --grep='^run opts in$' -1)
MASA_OWN=$(git -C "$masa" log main --format=%H --grep='^owner opts in$' -1)
n=$((n+1)); { [ -n "$MASA_BLANK" ] && [ -n "$MASA_DATE" ] && [ -n "$MASA_KEY" ] && [ -n "$MASA_OWN" ]; } \
  || { echo "FAIL the TOOL-aWardedAudit-5 fixture did not build its four commits"; st=1; }
out=$(ma_leg "$masa")
hit  "$out" "a commit among a run's own commits writes a spec-audit: line into a build README, so a run could land the opt-in the next run's pre-code audit would rest on, and only the owner opts a build in - commit and README follow: $MASA_KEY in memory/builds/tOther3/README.md, run memory/builds/tRun/RUN.md"
hit  "$out" "a commit among a run's own commits writes a non-blank SPEC_AUDIT_DEFAULT into the project conf, so a run could land the project-wide opt-in every later run's pre-code audit would rest on, and only the owner opts a build in - commit and conf follow: $MASA_DATE in .unattended.conf, run memory/builds/tRun/RUN.md"
miss "$out" "$MASA_BLANK in .unattended.conf"
miss "$out" "$MASA_OWN in memory/builds/tOther/README.md"
# ...and the may: arm keeps its own message on the same graph.
hit  "$out" "$MA_WRITES $(git -C "$masa" log --format=%H --grep='^run grants$' -1) $MA_RUN_RD"
# ---- A LIVE RECORD IS GRADED ONLY IN A TREE ON ITS OWN RUN BRANCH. Its range is HEAD past the
# ---- advertised tip, so a tree on another branch charged the record with that branch's commits (the
# ---- aEvidencedLens close bar named aClosedDocket and aUnblockedFleet). Same graph, same three writes:
# ---- a record naming ANOTHER branch skips all three own-commit arms, announced; one naming the
# ---- checked-out branch, or any record on a detached HEAD, is graded as before.
sed -i '/^may: none$/a branch-ref: refs/heads/elsewhere' "$masa/memory/builds/tRun/RUN.md"; ma_commit "$masa" "record on another branch"
out=$(ma_leg "$masa")
miss "$out" "$MASA_KEY in memory/builds/tOther3/README.md"
miss "$out" "$MASA_DATE in .unattended.conf"
miss "$out" "$MA_WRITES"
hit  "$out" "check 19 SKIPPED the grant-write and round-bound arms for memory/builds/tRun/RUN.md - it is live on its run branch refs/heads/elsewhere and this tree has refs/heads/unit checked out"
sed -i 's|^branch-ref: .*|branch-ref: refs/heads/unit|' "$masa/memory/builds/tRun/RUN.md"; ma_commit "$masa" "record on its own branch"
out=$(ma_leg "$masa")
hit  "$out" "commit and README follow: $MASA_KEY in memory/builds/tOther3/README.md, run memory/builds/tRun/RUN.md"
miss "$out" "it is live on its run branch"
sed -i 's|^branch-ref: .*|branch-ref: refs/heads/elsewhere|' "$masa/memory/builds/tRun/RUN.md"; ma_commit "$masa" "record on another branch again"
( cd "$masa" && git checkout -q --detach ) >/dev/null 2>&1
out=$(ma_leg "$masa")
hit  "$out" "commit and README follow: $MASA_KEY in memory/builds/tOther3/README.md, run memory/builds/tRun/RUN.md"
miss "$out" "it is live on its run branch"
( cd "$masa" && git checkout -q unit ) >/dev/null 2>&1
# ---- G1: A LIVE RECORD, AND AN IN-PLACE TERMINAL ONE, over unit 2's prepared merge T - first parent
# ---- the advertised tip, which carries the owner's grant, second parent the run branch.
ma_init g1; ma1="$ma_root/g1"
( cd "$ma1" && git checkout -q --detach main && git merge -q --no-ff --no-edit -m "merge: tRun — land onto main" unit \
    && git checkout -q -B unit ) >/dev/null 2>&1
ma_facts "$ma1" tRun RUNNING HEAD "$(ma_base "$ma1")"; ma_commit "$ma1" "record on the prepared merge"
MA_RUN=$(git -C "$ma1" log --format=%H --grep='^run grants$' -1)
MA_OWN=$(git -C "$ma1" log --format=%H --grep='^owner grants$' -1)
n=$((n+1)); { [ -n "$MA_RUN" ] && [ -n "$MA_OWN" ] && [ -n "$(ma_sha "$ma1" 'HEAD~1^2')" ]; } \
  || { echo "FAIL the TOOL-dDerivedDocket-19 G1 fixture built no prepared merge over both grants"; st=1; }
out=$(ma_leg "$ma1")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"
# the in-place close: a single-parent commit on T is the witness of a terminal record
ma_facts "$ma1" tRun LANDED HEAD "$(ma_base "$ma1")"
printf 'landed-anchor: local\n' >> "$ma1/memory/builds/tRun/RUN.md"; ma_commit "$ma1" "the close"
out=$(ma_leg "$ma1")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"

# ---- G2: THE PRIMARY LANDER'S --no-ff LANDING MERGE L as the witness, unpushed and then pushed, and
# ---- then a single-parent fix commit on the pushed L. L's run side is its SECOND parent.
ma_init g2; ma2="$ma_root/g2"
( cd "$ma2" && git checkout -q main && git merge -q --no-ff --no-edit -m "land tRun" unit ) >/dev/null 2>&1
MA_L=$(ma_sha "$ma2" HEAD)
ma_facts "$ma2" tRun LANDED "$MA_L" "$(ma_base "$ma2")"
printf 'landed-anchor: remote\n' >> "$ma2/memory/builds/tRun/RUN.md"; ma_commit "$ma2" "landed record"
MA_RUN=$(git -C "$ma2" log --format=%H --grep='^run grants$' -1)
same "fixture: the landing merge's first parent is the owner's grant" \
  "$(git -C "$ma2" log -1 --format=%s "$MA_L^1")" "owner grants"
out=$(ma_leg "$ma2")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"
( cd "$ma2" && git push -q origin main ) >/dev/null 2>&1
out=$(ma_leg "$ma2")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"
# a fix commit on the pushed landing merge, pushed, is the witness
printf 'fix\n' > "$ma2/fix.txt"; ma_commit "$ma2" "fix after landing"
ma_facts "$ma2" tRun LANDED HEAD "$(ma_base "$ma2")"; ma_commit "$ma2" "record the fix"
( cd "$ma2" && git push -q origin main ) >/dev/null 2>&1
out=$(ma_leg "$ma2")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"

# ---- G4: PUSH-MAIN'S OWN RECONCILE as the witness. L is made locally and NOT pushed; another node
# ---- pushes a SECOND owner grant onto the remote meanwhile, and the lander merges the remote in.
# ---- The reconcile's run side is its FIRST parent, the one holding L, and the walk goes on to L.
ma_init g4; ma4="$ma_root/g4"
( cd "$ma4" && git checkout -q main && git merge -q --no-ff --no-edit -m "land tRun" unit ) >/dev/null 2>&1
( git clone -q "$ma4.git" "$ma_root/g4-other" && cd "$ma_root/g4-other" \
    && git config user.email o@t.test && git config user.name o \
    && sed -i '/^slug: tOther3$/a may: bin/other-node.sh' memory/builds/tOther3/README.md \
    && git commit -qam "other node grants" --no-verify && git push -q origin main ) >/dev/null 2>&1
( cd "$ma4" && git fetch -q origin && git merge -q --no-ff --no-edit -m "reconcile origin/main" origin/main ) >/dev/null 2>&1
MA_M=$(ma_sha "$ma4" HEAD)
MA_RUN=$(git -C "$ma4" log --format=%H --grep='^run grants$' -1)
same "fixture: push-main's reconcile takes the other node's grant as its second parent" \
  "$(git -C "$ma4" log -1 --format=%s "$MA_M^2")" "other node grants"
same "fixture: ...and the landing merge as its first" "$(git -C "$ma4" log -1 --format=%s "$MA_M^1")" "land tRun"
ma_facts "$ma4" tRun LANDED "$MA_M" "$(ma_base "$ma4")"
printf 'landed-anchor: remote\n' >> "$ma4/memory/builds/tRun/RUN.md"; ma_commit "$ma4" "record the reconcile"
( cd "$ma4" && git push -q origin main ) >/dev/null 2>&1
out=$(ma_leg "$ma4")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"
miss "$out" "in memory/builds/tOther3/README.md, run"

# ---- G3: A RUN ABORTED BEFORE --prepare, after a PLAIN reconcile R brought the owner's grant in.
# ---- Graded live, then terminal with R as the witness, then with a single-parent commit after R.
ma_init g3; ma3="$ma_root/g3"
( cd "$ma3" && git merge -q --no-edit main ) >/dev/null 2>&1
MA_R=$(ma_sha "$ma3" HEAD)
MA_RUN=$(git -C "$ma3" log --format=%H --grep='^run grants$' -1)
same "fixture: the plain reconcile takes the owner's grant as its SECOND parent" \
  "$(git -C "$ma3" log -1 --format=%s "$MA_R^2")" "owner grants"
ma_facts "$ma3" tRun RUNNING "$MA_R" "$(ma_base "$ma3")"; ma_commit "$ma3" "live after the reconcile"
out=$(ma_leg "$ma3")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"
ma_facts "$ma3" tRun ABORTED "$MA_R" "$(ma_base "$ma3")"; ma_commit "$ma3" "aborted at the reconcile"
out=$(ma_leg "$ma3")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"
printf 'after\n' > "$ma3/after.txt"; ma_commit "$ma3" "work after the reconcile"
ma_facts "$ma3" tRun ABORTED HEAD "$(ma_base "$ma3")"; ma_commit "$ma3" "aborted after the reconcile"
out=$(ma_leg "$ma3")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"


# ---- TOOL-dDerivedDocket-22 S17 / AC17: A DERIVED-LANDED record's own commits run from its landing
# ---- commit C, with the exclusions its merges' run sides give. Read as LIVE, its range would be what
# ---- this tree has not pushed - nothing, once it landed - and the run's own grant would go ungraded.
# ---- In-place: the prepared merge T takes the owner's grant as its first parent, and C sits on T.
ma_init g22a; ma22="$ma_root/g22a"
( cd "$ma22" && git fetch -q origin && git checkout -q --detach origin/main \
    && git merge -q --no-ff --no-edit -m "merge: tRun - land onto origin/main" unit \
    && git branch -qf unit HEAD && git checkout -q unit ) >/dev/null 2>&1
ma_facts "$ma22" tRun LANDING unit "$(ma_base "$ma22")"; ma_commit "$ma22" "records(tRun): close — LANDING"
( cd "$ma22" && git push -q origin HEAD:main ) >/dev/null 2>&1
MA_RUN=$(git -C "$ma22" log --format=%H --grep='^run grants$' -1)
same "fixture: the in-place landing commit is on the advertised tip" \
  "$(git --git-dir="$ma22.git" rev-parse main)" "$(ma_sha "$ma22" HEAD)"
out=$(ma_leg "$ma22")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"
# ---- Primary: the run branch reconciled the default branch PLAINLY mid-run, after the owner's grant
# ---- landed there, then committed its LANDING and was landed by a --no-ff merge. The reconcile's
# ---- excluded parent is its SECOND, the owner's side, never the first.
ma_init g22b; ma22="$ma_root/g22b"
( cd "$ma22" && git merge -q --no-edit main ) >/dev/null 2>&1
MA_R=$(ma_sha "$ma22" HEAD)
same "fixture: the plain reconcile takes the owner's grant as its SECOND parent" \
  "$(git -C "$ma22" log -1 --format=%s "$MA_R^2")" "owner grants"
ma_facts "$ma22" tRun LANDING HEAD "$(ma_base "$ma22")"; ma_commit "$ma22" "close by hand"
( cd "$ma22" && git checkout -q main && git merge -q --no-ff --no-edit -m "land tRun" unit \
    && git push -q origin main && git checkout -q unit ) >/dev/null 2>&1
MA_RUN=$(git -C "$ma22" log --format=%H --grep='^run grants$' -1)
out=$(ma_leg "$ma22")
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
miss "$out" "$MA_OWN_RD"

# ==== TOOL-aEvidencedLens-9: NO RUN COMMIT CHANGES THE ROUND BOUND ===============================
# The same own-commit list as the grant arm, so the same builder: the run's raise must red on a live
# and on a terminal record, and an OWNER raise merged into the run branch must not. The fixture conf
# declares no REVIEW_ROUNDS, so the bound before every raise is the driver's default of 1. At base
# no arm below printed a round line. Every graph still carries the run's grant, so the grant arm
# hitting in the quiet group proves the leg graded that range rather than finding nothing.
MA_ROUNDS="a commit among a run's own commits changes the effective REVIEW_ROUNDS bound in .unattended.conf, and the round bound is the owner's, set by an owner commit outside any run (run mandate memory/builds/aEvidencedLens/prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-0-run-mandate.md, decision 4) - commit and bound follow:"
# ---- R1: a live record whose own commit raises the bound
ma_init gr1; mar="$ma_root/gr1"
write_rounds_line "$mar" 2; ma_commit "$mar" "run raises rounds"; MA_RR=$(ma_sha "$mar" HEAD)
hit "$(ma_leg "$mar")" "$MA_ROUNDS $MA_RR 1 -> 2, run memory/builds/tRun/RUN.md"
# ---- R2: the owner raises it on main and the run branch merges main. The merge's FIRST-parent diff
# ---- carries the raise, so a scan reading it would red; the merge took one side's value, and the
# ---- owner's commit is on the advertised tip, so nothing is named.
ma_init gr2; mar="$ma_root/gr2"
( cd "$mar" && git checkout -q main ) >/dev/null 2>&1; write_rounds_line "$mar" 2; ma_commit "$mar" "owner raises rounds"
( cd "$mar" && git push -q origin main && git checkout -q unit && git merge -q --no-edit main ) >/dev/null 2>&1
MA_RUN=$(git -C "$mar" log --format=%H --grep='^run grants$' -1)
same "fixture: the reconcile's first-parent diff carries the owner's raise" \
  "$(git -C "$mar" diff --name-only HEAD^1 HEAD -- .unattended.conf)" ".unattended.conf"
out=$(ma_leg "$mar")
miss "$out" "changes the effective REVIEW_ROUNDS bound"
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
# ---- R3: a TERMINAL record, landed by a --no-ff merge named as its witness, whose range holds the
# ---- run's raise. A live-only fixture never reaches the terminal arm of the range.
ma_init gr3; mar="$ma_root/gr3"
write_rounds_line "$mar" 2; ma_commit "$mar" "run raises rounds"; MA_RR=$(ma_sha "$mar" HEAD)
( cd "$mar" && git checkout -q main && git merge -q --no-ff --no-edit -m "land tRun" unit ) >/dev/null 2>&1
ma_facts "$mar" tRun LANDED HEAD "$(ma_base "$mar")"
printf 'landed-anchor: remote\n' >> "$mar/memory/builds/tRun/RUN.md"; ma_commit "$mar" "landed record"
hit "$(ma_leg "$mar")" "$MA_ROUNDS $MA_RR 1 -> 2, run memory/builds/tRun/RUN.md"
# ---- TOOL-aEvidencedLens-21 S6 (closing review L1). R4: a run commit writes a DECOY conf, `4` sourced
# ---- and a dead `1` after it; the last-assignment read saw `1`, the default, and named nothing.
ma_init gr4; mar="$ma_root/gr4"
sed -i '/^REVIEW_ROUNDS=/d' "$mar/.unattended.conf"; printf 'REVIEW_ROUNDS=4\nif false; then\nREVIEW_ROUNDS=1\nfi\n' >> "$mar/.unattended.conf"
ma_commit "$mar" "run writes a decoy"; MA_RR=$(ma_sha "$mar" HEAD)
hit "$(ma_leg "$mar")" "$MA_ROUNDS $MA_RR 1 -> multi:4,1, run memory/builds/tRun/RUN.md"
# ---- R5: `1` then `01` is one bound, so neither run commit is a round write; the grant hit is the
# ---- liveness, proving the leg graded that range rather than finding nothing.
ma_init gr5; mar="$ma_root/gr5"
write_rounds_line "$mar" 1; ma_commit "$mar" "run spells rounds"; write_rounds_line "$mar" 01; ma_commit "$mar" "run zero-pads rounds"
MA_RUN=$(git -C "$mar" log --format=%H --grep='^run grants$' -1)
out=$(ma_leg "$mar")
miss "$out" "changes the effective REVIEW_ROUNDS bound"
hit  "$out" "$MA_WRITES $MA_RUN $MA_RUN_RD"
# ---- The four reports that skip or narrow the walk name BOTH arms it gates.
same "round reports: no skip report names the grant-write arm alone" \
  "$(grep -cF 'SKIPPED the grant-write arm for' "$TMP/$KIT_REL/check-unattended.sh")" "0"
same "round reports: both skip reports name both arms" \
  "$(grep -cF 'SKIPPED the grant-write and round-bound arms for' "$TMP/$KIT_REL/check-unattended.sh")" "2"
hit "$(grep -F 'excludes the LOCAL ref' "$TMP/$KIT_REL/check-unattended.sh")" "grant-write and round-bound arms"
hit "$(grep -F 'examined NO own commit' "$TMP/$KIT_REL/check-unattended.sh")" "grant-write and round-bound arms"

# ==== TOOL-aEvidencedLens-14: THE WALK FIRES ON EITHER SCAN'S HIT =================================
# A BARE graph carries no grant, so the grant scan never hits and only the round scan can trigger the
# terminal walk. The owner raises the bound on main; the run branch reconciles main (plainly, or by an
# evil merge), optionally raises it itself, and lands by a --no-ff merge named as the witness. Against
# the grant-only trigger the unwalked superset names the owner's commit.
# ---- round walk: AC1 - an owner raise merged into a terminal record's run names no round write
build_round_walk grw1 "" ""
same "round walk: fixture, the owner raise and the run's reconcile of it are in base..witness" \
  "$(git -C "$mar" log --format=%s -1 "$MA_OWNR")|$(git -C "$mar" log --format=%s -1 'HEAD~1^2')" "owner raises rounds|Merge branch 'main' into unit"
out=$(ma_leg "$mar")
miss "$out" "$MA_ROUNDS $MA_OWNR"
miss "$out" "changes the effective REVIEW_ROUNDS bound"
# ---- round walk: AC2 - the same record with a run raise beside it: named once, the owner's dropped.
# ---- Also the liveness of AC1's `miss`: the same leg on the same graph does name a round write.
build_round_walk grw2 3 ""
MA_RR=$(git -C "$mar" log --format=%H --grep='^run raises rounds$' -1)
out=$(ma_leg "$mar")
hit  "$out" "$MA_ROUNDS $MA_RR 2 -> 3, run memory/builds/tRun/RUN.md"
miss "$out" "$MA_ROUNDS $MA_OWNR"
same "round walk: a run raise beside an owner raise fails check 19 once" "$(measure_round_count "$out")" 1
# ---- round walk: AC3 - an EVIL run merge whose resolution sets 3 over parents 1 (run) and 2 (owner)
# ---- is a run write the walk keeps. Its red is a staged break: a walk that drops merge commits
# ---- themselves, the superset read untouched, names nothing on the same graph.
build_round_walk grw3 "" 3
MA_EM=$(git -C "$mar" log --format=%H --grep='^evil reconcile$' -1)
out=$(ma_leg "$mar")
hit  "$out" "$MA_ROUNDS $MA_EM 1 -> 3, run memory/builds/tRun/RUN.md"
miss "$out" "$MA_ROUNDS $MA_OWNR"
same "round walk: an evil run merge fails check 19 once" "$(measure_round_count "$out")" 1
mutate "$mar/$KIT_REL/lib-unattended.sh" 's/GIT rev-list "\$_rrc_end" "^\$_rrc_base" \$_rrc_ex 2>/GIT rev-list "$_rrc_end" "^$_rrc_base" $_rrc_ex ${_rrc_ex:+--no-merges} 2>/'
same "round walk: a walk that drops the merge itself names nothing" "$(measure_round_count "$(ma_leg "$mar")")" 0
# ...and the broken leg is alive, not mute: on AC2's graph it still walks and names the run's plain raise
cp "$mar/$KIT_REL/lib-unattended.sh" "$ma_root/grw2/$KIT_REL/lib-unattended.sh"
hit "$(ma_leg "$ma_root/grw2")" "$MA_ROUNDS $MA_RR 2 -> 3, run memory/builds/tRun/RUN.md"
rm -rf "$ma_root"


fi   # ---- a re-cut seam of the region-8 span (TOOL-aGraftedHelix-34 S7): the section below is region 1's
if in_shard 1; then
cd "$TMP" || exit 2; anchor_restore; read_topo s8   # every section after a re-cut seam starts from the prologue's fixture, refs and remote
# ================== TOOL-dDerivedDocket-22 — the derived terminal, graded by the leg ==============
# ---- In the shared fixture, each arm from `reset_tree` and each one that pushes restoring the
# ---- remote's anchor, so no later arm inherits a moved tip. The leg is run with the report channel
# ---- on, because the fact-set arm's counts and its disabled state are announced there.
# `--follow` FOLLOWS COPIES as well as renames, so a record sharing more than half its lines with
# another at its first commit is followed INTO that one and dated by its add. On a real history the
# source is older and that errs toward grandfathering, but a BACKDATED fixture commit is older than
# its own copy source, so the dated arms make their records dissimilar rather than assert an artifact.

# ---- AC8, the leg's half: a LANDING record whose WITNESS is on the remote and whose record commit is
# ---- not is counted live by check 7; with the record commit pushed it is EXCLUDED as derived LANDED.
# ---- The witness reading this replaced excluded the first record too.
reset_tree
write_lg_record tLand LANDING "$ANCHOR0"
git add -A >/dev/null && write_lg_commit "tLand closes"
out=$(run)
hit  "$out" "2 concurrent unattended run(s) — none of them blocks another"
miss "$out" "check 7 EXCLUDED memory/builds/tLand/RUN.md"
git push -q -f origin HEAD:main
out=$(run)
hit  "$out" "check 7 EXCLUDED memory/builds/tLand/RUN.md — derived LANDED: its landing commit $(git rev-parse HEAD)"
miss "$out" "concurrent unattended run(s)"
git push -q -f origin "$ANCHOR0":main

# ---- AC18: a rotated record's `landed-derived` is TESTED, not trusted. The witness is pinned on the
# ---- advertised tip, so the witness ancestry test cannot red the record in this arm's place.
reset_tree
lg_off=$(git rev-parse HEAD)
write_lg_record tArch LANDED "$ANCHOR0" "landed-derived: $lg_off $ANCHOR0\nunits-at-landing: ARCH-tArch-1\n"
git add memory/builds/tArch >/dev/null
git mv -f memory/builds/tArch/RUN.md memory/builds/tArch/RUN.LANDED.deadbeef.md
git add -A >/dev/null
out=$(run_lg_leg)
hit "$out" "a record claims LANDED on derived evidence and the landing commit its landed-derived: names is not on the tip the remote advertises, so the derivation it records is one this remote does not support: $lg_off against $ANCHOR0 in memory/builds/tArch/RUN.LANDED.deadbeef.md"
miss "$out" "names no anchor kind while its own first commit"
sed -i "s/^landed-derived: .*/landed-derived: $ANCHOR0 $ANCHOR0/" memory/builds/tArch/RUN.LANDED.deadbeef.md
git add -A >/dev/null
out=$(run_lg_leg)
miss "$out" "a record claims LANDED on derived evidence"

# ---- AC9 and AC16: the fact-set arm, by population and by date. A malformed cutoff refuses; a blank
# ---- one announces that the arm is off; a recorded LANDED missing the roster reds naming the fact;
# ---- the count line names every population and says so at zero.
reset_tree
printf 'LANDED_FACTS_CUTOFF="soon"\n' >> .unattended.conf
out=$(run_lg_leg)
hit "$out" "LANDED_FACTS_CUTOFF is declared and is not an ISO date, and a cutoff nothing can compare would grade every landed record or none while reading as configured"
reset_tree
out=$(run_lg_leg)
hit "$out" "the landed fact-set arm of check 15 is OFF - LANDED_FACTS_CUTOFF is blank or undeclared"
printf 'LANDED_FACTS_CUTOFF="2026-06-01"\n' >> .unattended.conf
out=$(run_lg_leg)
hit "$out" "recorded LANDED 0 · rotated derived LANDED 0 · committed LANDING 0 · attended LANDED 0 - a count of 0, so this arm graded nothing on this tree"
write_lg_record tFacts LANDED "$ANCHOR0" "landed-anchor: remote\nunpushed-at-landing: 0\n"
git add -A >/dev/null && write_lg_commit "a landed record with no roster"
out=$(run_lg_leg)
hit "$out" "a landed record first committed on or after LANDED_FACTS_CUTOFF is missing a fact its landing verb writes, so what that landing covered cannot be read from the record it left, and no verb adds a fact to a record once it is terminal or pushed - population landed, missing [units-at-landing] in memory/builds/tFacts/RUN.md"
hit "$out" "recorded LANDED 1 · rotated derived LANDED 0 · committed LANDING 0"
# ...a rotated derived record is graded as its own population
write_lg_record tDer LANDED "$ANCHOR0" "landed-derived: $ANCHOR0 $ANCHOR0\n"
git add memory/builds/tDer >/dev/null
git mv -f memory/builds/tDer/RUN.md memory/builds/tDer/RUN.LANDED.cafef00d.md
git add -A >/dev/null && write_lg_commit "a rotated derived record with no roster"
out=$(run_lg_leg)
hit "$out" "population derived, missing [units-at-landing] in memory/builds/tDer/RUN.LANDED.cafef00d.md"

# ---- AC9: a record first committed BEFORE the cutoff and rotated AFTER it is not graded, by either
# ---- cutoff: `--follow` dates the archive by the run's own first commit, not by the rotation that
# ---- added its name. Anchorless and factless, so an undated reading reds it twice.
reset_tree
printf 'LANDED_FACTS_CUTOFF="2026-06-01"\n' >> .unattended.conf
sed -i 's/^LANDED_ANCHOR_CUTOFF=.*//' .unattended.conf; printf 'LANDED_ANCHOR_CUTOFF="2026-06-01"\n' >> .unattended.conf
write_lg_record tOld LANDED "$ANCHOR0"; write_lg_filler tOld
git add memory/builds/tOld >/dev/null && write_lg_commit "an old landed run" 2026-01-01
git mv memory/builds/tOld/RUN.md memory/builds/tOld/RUN.LANDED.0bd0bd00.md
write_lg_commit "rotated after the cutoff"
out=$(run_lg_leg)
miss "$out" "in memory/builds/tOld/RUN.LANDED.0bd0bd00.md"
miss "$out" "names no anchor kind while its own first commit is at or after the declared cutoff"
hit  "$out" "recorded LANDED 0 · rotated derived LANDED 0 · committed LANDING 0"
same "the archive is dated by its run's first commit" \
  "$( . "$TMP/$KIT_REL/lib-unattended.sh"; read_first_commit_date memory/builds/tOld/RUN.LANDED.0bd0bd00.md )" "2026-01-01"

# ---- AC9: the LIVE record in a folder that has rotated is dated by its OWN tenancy, the rotation,
# ---- and not by the previous run's first commit, which `--follow --diff-filter=A` alone returns.
# ---- The ANCHOR cutoff keeps the unfloored reading, and the same record shows it: anchorless, it
# ---- is not red for naming no anchor kind, because flooring that older key would red terminal
# ---- records no verb may now repair.
reset_tree
printf 'LANDED_FACTS_CUTOFF="2026-02-01"\nLANDED_ANCHOR_CUTOFF="2026-02-01"\n' >> .unattended.conf
write_lg_record tFloor ABORTED "$ANCHOR0" "halt-code: fork-unresolvable\n"; write_lg_filler tFloor
git add memory/builds/tFloor >/dev/null && write_lg_commit "the first run" 2026-01-01
git mv memory/builds/tFloor/RUN.md memory/builds/tFloor/RUN.ABORTED.f1007000.md
write_lg_record tFloor LANDED "$ANCHOR0" "unpushed-at-landing: 0\n"
git add memory/builds/tFloor >/dev/null && write_lg_commit "the rotation, and the second run" 2026-03-01
same "the live record is dated by its own tenancy" \
  "$( . "$TMP/$KIT_REL/lib-unattended.sh"; read_first_commit_date memory/builds/tFloor/RUN.md )" "2026-03-01"
same "the anchor cutoff's unfloored reading dates the path's first add" \
  "$( . "$TMP/$KIT_REL/lib-unattended.sh"; read_first_commit_date memory/builds/tFloor/RUN.md nofloor )" "2026-01-01"
out=$(run_lg_leg)
hit  "$out" "population landed, missing [landed-anchor units-at-landing] in memory/builds/tFloor/RUN.md"
miss "$out" "names no anchor kind while its own first commit is at or after the declared cutoff, so which history was meant to bless its witness cannot be read at all: memory/builds/tFloor/RUN.md"

# ---- AC16: under `in-place` a hand-committed LANDING record with no roster reds, counted as its
# ---- own population; under `primary` the same record, pushed so it derives LANDED, is REPORTED
# ---- naming --landed and never graded.
reset_tree
printf 'LANDED_FACTS_CUTOFF="2026-06-01"\nLANDER_MODE="in-place"\n' >> .unattended.conf
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md
git add -A >/dev/null && write_lg_commit "a hand-committed LANDING"
out=$(run_lg_leg)
hit  "$out" "population landing, missing [units-at-landing] in memory/builds/tRun/RUN.md"
hit  "$out" "recorded LANDED 0 · rotated derived LANDED 0 · committed LANDING 1"
sed -i 's/^LANDER_MODE=.*//' .unattended.conf
git push -q -f origin HEAD:main
out=$(run_lg_leg)
miss "$out" "population landing, missing [units-at-landing] in memory/builds/tRun/RUN.md"
hit  "$out" "check 15 did not grade the landed facts of memory/builds/tRun/RUN.md - it is a committed LANDING the remote already carries, so it derives LANDED, and under primary landing the verb that writes those facts has not run yet: --landed tRun"
git push -q -f origin "$ANCHOR0":main

# ---- TOOL-dUnstuckLanding-14 AC1, the leg's half: a settled hand-off is counted in the `attended`
# ---- population, which owes `landed-by` beside the derived facts, and reds naming a missing one.
reset_tree
printf 'LANDED_FACTS_CUTOFF="2026-06-01"\n' >> .unattended.conf
write_lg_record tAtt LANDED "$ANCHOR0" "landed-derived: $ANCHOR0 $ANCHOR0\nunits-at-landing: ARCH-tAtt-1\nlanded-by: attended\n"
git add -A >/dev/null && write_lg_commit "records(tAtt): settle the run record"
out=$(run_lg_leg)
hit  "$out" "committed LANDING 0 · attended LANDED 1"
miss "$out" "population attended, missing"
sed -i '/^units-at-landing: /d' memory/builds/tAtt/RUN.md
git add -A >/dev/null
out=$(run_lg_leg)
hit  "$out" "population attended, missing [units-at-landing] in memory/builds/tAtt/RUN.md"

# ---- TOOL-dUnstuckLanding-14 S3: a HELD record under a hand-off code whose own commit is on the
# ---- advertised tip is EXCLUDED by check 7 as derived LANDED; under any other hold code it counts.
reset_tree
write_lg_record tHand HELD "$ANCHOR0" "hold-code: owner-landing\n"
git add -A >/dev/null && write_lg_commit "records(tHand): hand-off"
git push -q -f origin HEAD:main
out=$(run)
hit  "$out" "check 7 EXCLUDED memory/builds/tHand/RUN.md — derived LANDED: its landing commit $(git rev-parse HEAD)"
sed -i 's/^hold-code: .*/hold-code: inherited-red/' memory/builds/tHand/RUN.md
git add -A >/dev/null && write_lg_commit "records(tHand): a plain hold"
git push -q -f origin HEAD:main
out=$(run)
miss "$out" "check 7 EXCLUDED memory/builds/tHand/RUN.md"
git push -q -f origin "$ANCHOR0":main

# ---- TOOL-dUnstuckLanding-14 AC7: work-landed-at is UPHELD by the content predicate, not graded on
# ---- presence. tKept's work landed and stayed; tRev's landed and was reverted on the first-parent
# ---- line, and its hand-written fact reds naming the fact and the file. A cutoff the record does not
# ---- predate reds the fact as discard, and a blank one reds it as undatable. An `abandoned` marker
# ---- standing alone reds, and check 7 excludes the record carrying it, as --preflight does.
# ---- Implementation review round 1, fold pass A: each fact names the tip it was written at, and is
# ---- graded THERE (M9). tMerge's work landed as a --no-ff merge that `git revert -m 1` backed out
# ---- (M4); tGone's never merged, which only clause (ii) decides (M11); tWrong's fact names a commit
# ---- that is not its witness (L6); tOffTip's names a tip the default branch does not carry. Each
# ---- reds through the library's `check_work_landed_fact`, the one the drift parity arm runs too.
reset_tree
printf 'HANDOFF_CUTOFF="2099-01-01"\n' >> .unattended.conf
# Its own commit, so the revert of tKept's work below cannot take the cutoff with it.
git add -A >/dev/null && write_lg_commit "chore: date the hand-off cutoff"
for lg_s in tKept tRev tWrong tOffTip; do
  mkdir -p "memory/builds/$lg_s"; printf '%s\n' "$lg_s" > "memory/builds/$lg_s/work.txt"
  git add -A >/dev/null && write_lg_commit "work($lg_s): the change"
  eval "lg_w_$lg_s=\$(git rev-parse HEAD)"
done
git -c core.hooksPath=/dev/null revert --no-edit "$lg_w_tRev" >/dev/null 2>&1
lg_b=$(git symbolic-ref --short HEAD)
git checkout -q -b lg-merge
mkdir -p memory/builds/tMerge; printf 'tMerge\n' > memory/builds/tMerge/work.txt
git add -A >/dev/null && write_lg_commit "work(tMerge): the change"
lg_w_tMerge=$(git rev-parse HEAD)
git checkout -q "$lg_b"
git -c core.hooksPath=/dev/null merge -q --no-ff --no-edit -m "land the tMerge run" lg-merge >/dev/null 2>&1
lg_m_tMerge=$(git rev-parse HEAD)
git -c core.hooksPath=/dev/null revert -m 1 --no-edit "$lg_m_tMerge" >/dev/null 2>&1
git checkout -q -b lg-gone
mkdir -p memory/builds/tGone; printf 'tGone\n' > memory/builds/tGone/work.txt
git add -A >/dev/null && write_lg_commit "work(tGone): the change"
lg_w_tGone=$(git rev-parse HEAD)
git checkout -q "$lg_b"
lg_tip=$(git rev-parse HEAD)
write_lg_record tKept ABORTED "$lg_w_tKept" "halt-code: fork-unresolvable\nwork-landed-at: $lg_w_tKept $lg_tip\n"
write_lg_record tRev ABORTED "$lg_w_tRev" "halt-code: fork-unresolvable\nwork-landed-at: $lg_w_tRev $lg_tip\n"
write_lg_record tMerge ABORTED "$lg_w_tMerge" "halt-code: fork-unresolvable\nwork-landed-at: $lg_w_tMerge $lg_tip\n"
write_lg_record tGone ABORTED "$lg_w_tGone" "halt-code: fork-unresolvable\nwork-landed-at: $lg_w_tGone $lg_tip\n"
write_lg_record tWrong ABORTED "$lg_w_tWrong" "halt-code: fork-unresolvable\nwork-landed-at: $lg_w_tKept $lg_tip\n"
write_lg_record tOffTip ABORTED "$lg_w_tOffTip" "halt-code: fork-unresolvable\nwork-landed-at: $lg_w_tOffTip $lg_w_tGone\n"
git add -A >/dev/null && write_lg_commit "records: six aborted runs"
git push -q -f origin HEAD:main
out=$(run_lg_leg)
hit  "$out" "a record claims work-landed-at and the content predicate does not uphold it at the tip the fact records, so the fact is not one --settle could have written: a commit on the tip's first-parent line reverts its commit ${lg_w_tRev:0:8} in memory/builds/tRev/RUN.md"
same "AC7 the kept record's fact is upheld" \
  "$(printf '%s\n' "$out" | grep -F 'a record claims work-landed-at' | grep -c 'memory/builds/tKept/' || true)" "0"
hit  "$out" "a commit on the tip's first-parent line reverts the merge ${lg_m_tMerge:0:8}, which brought its commit ${lg_w_tMerge:0:8} onto the tip in memory/builds/tMerge/RUN.md"
hit  "$out" "its commit ${lg_w_tGone:0:8} is not on the tip ${lg_tip:0:8} in memory/builds/tGone/RUN.md"
hit  "$out" "its work-landed-at names ${lg_w_tKept:0:8} and its witness is ${lg_w_tWrong:0:8}, so the fact is not about this run's own work in memory/builds/tWrong/RUN.md"
hit  "$out" "the tip its work-landed-at records, ${lg_w_tGone:0:8}, is not on the advertised tip "
hit  "$out" ", so it names no landing the default branch carries in memory/builds/tOffTip/RUN.md"
# ---- M9: a revert landing AFTER a correct settle is a report line, never a red on every later bar.
git -c core.hooksPath=/dev/null revert --no-edit "$lg_w_tKept" >/dev/null 2>&1
git push -q -f origin HEAD:main
out=$(run_lg_leg)
same "AC7 a later revert leaves the kept record's fact upheld" \
  "$(printf '%s\n' "$out" | grep -F 'a record claims work-landed-at' | grep -c 'memory/builds/tKept/' || true)" "0"
hit  "$out" "unattended-report: check 15 upheld work-landed-at in memory/builds/tKept/RUN.md at the tip it records, ${lg_tip:0:8}, and the content predicate no longer reads that work landed on the advertised tip "
hit  "$out" "reported and never a red, because no verb rewrites the record: a commit on the tip's first-parent line reverts its commit ${lg_w_tKept:0:8}"
# ---- Implementation review round 2, L8 (id 29): a tip whose first-parent line cannot be READ is not a
# ---- revert anybody observed. A git double fails `log --first-parent` over the advertised tip alone,
# ---- so the fact still reads upheld at the tip it records and is reported as not re-judged, never as
# ---- undone. RED against the reader that folded the undecidable status into WLF_NOW.
c15_adv=$(git ls-remote origin HEAD | cut -f1)
c15_git=$(command -v git)
mkdir -p "$TMPBIN"
printf '#!/bin/sh\ncase " $* " in *" --first-parent "*" %s "*) exit 128 ;; esac\nexec "%s" "$@"\n' "$c15_adv" "$c15_git" > "$TMPBIN/git"
chmod +x "$TMPBIN/git"
out=$(PATH="$TMPBIN:$PATH" run_lg_leg)
rm -f "$TMPBIN/git"
hit  "$out" "unattended-report: check 15 upheld work-landed-at in memory/builds/tKept/RUN.md at the tip it records, ${lg_tip:0:8}, and it was not re-judged at the advertised tip ${c15_adv:0:8}: the tip's first-parent line since ${lg_w_tKept:0:8} cannot be read"
miss "$out" "check 15 upheld work-landed-at in memory/builds/tKept/RUN.md at the tip it records, ${lg_tip:0:8}, and the content predicate no longer reads that work landed"
sed -i 's/^HANDOFF_CUTOFF=.*/HANDOFF_CUTOFF="2000-01-01"/' .unattended.conf
out=$(run_lg_leg)
hit  "$out" "an ABORTED record first committed on or after HANDOFF_CUTOFF claims work-landed-at, and from that date ABORTED means discard, so no verb writes that its work landed: "
hit  "$out" "against 2000-01-01 in memory/builds/tKept/RUN.md"
sed -i 's/^HANDOFF_CUTOFF=.*/HANDOFF_CUTOFF=""/' .unattended.conf
out=$(run_lg_leg)
hit  "$out" "an ABORTED record claims work-landed-at and HANDOFF_CUTOFF is not a date, so whether it predates the day ABORTED came to mean discard cannot be read, and --settle refuses every such record: blank in memory/builds/tKept/RUN.md"
write_lg_record tAban RUNNING "$ANCHOR0" "abandoned: 2026-10-04T00:00:00Z\n"
git add -A >/dev/null
out=$(run_lg_leg)
hit  "$out" "a record carries abandoned with no work-landed-at, and --settle writes the two together, so the marker that takes it out of the live-run count stands on no proof that its work landed: memory/builds/tAban/RUN.md"
hit  "$out" "check 7 EXCLUDED memory/builds/tAban/RUN.md — abandoned at 2026-10-04T00:00:00Z"
git push -q -f origin "$ANCHOR0":main

# ---- THE DATING SELF-SCAN: a first-commit DATE read with --diff-filter=A and no --follow anywhere in
# ---- the kit's shell reds, naming the file and line; the same read with --follow does not.
# The flag rides a variable so no single line of THIS suite spells the offending read: check 15 scans
# every `*.sh` beside the checker, this suite included, and a literal here reds the real-tree leg.
reset_tree
_c15_dfa='--diff-filter=A'
printf '#!/usr/bin/env bash\nd=$(git log %s --format=%%cs -- x | tail -1)\n' "$_c15_dfa" > "$TMP/$KIT_REL/probe-date.sh"
out=$(run_lg_leg)
hit  "$out" "a first-commit DATE is read with --diff-filter=A and no --follow in this kit's own shell, so a rotation re-dates an archived record to the commit that added its name and a cutoff grades a record it was written to grandfather"
hit  "$out" "probe-date.sh:2"
printf '#!/usr/bin/env bash\nd=$(git log --follow --diff-filter=A --format=%%cs -- x | tail -1)\n' > "$TMP/$KIT_REL/probe-date.sh"
out=$(run_lg_leg)
miss "$out" "a first-commit DATE is read with --diff-filter=A and no --follow"
rm -f "$TMP/$KIT_REL/probe-date.sh"
reset_tree

fi   # ---- a re-cut seam of the region-8 span (TOOL-aGraftedHelix-34 S7): the section below is region 7's
if in_shard 7; then
cd "$TMP" || exit 2; anchor_restore; read_topo s9   # every section after a re-cut seam starts from the prologue's fixture, refs and remote
# ==== TOOL-dDerivedDocket-30: the conf hoist, the allow-list join and the flag arm =================
# ---- AC3. `--only 28` used to die on `set -u` at check 30, because the conf import sat inside the
# ---- guard it skips. Now it exits 0, announces one skip per numbered check after the 28 region on
# ---- the report channel, and prints nothing by default. The list below is this suite's pin of the
# ---- population; the leg DERIVES it, which the staged header after it is what proves.
reset_tree
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" --only 28 2>&1); rc=$?
same "--only 28 exits 0 once the conf is read above the scope guard" "$rc" "0"
miss "$out" "unbound variable"
for o28 in 30 31 32 33 39 40 15 41 42 43; do
  hit "$out" "check $o28 skipped under --only 28 — this run asked for the 28 region alone"
done
out=$(bash "$SCRIPT" --only 28 2>&1); rc=$?
same "--only 28 without the report channel exits 0" "$rc" "0"
same "--only 28 without the report channel prints nothing" "$out" ""
# ...and the population is DERIVED: a header staged after the region is announced with no list edited.
# 97 is a number no check of the leg uses.
mutate $KIT_REL/check-unattended.sh '/^if \[ "\$SCOPE" = only28 \]; then$/a # ---- check 97 - a fixture header, staged after the 28 region'
hit "$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" --only 28 2>&1)" "check 97 skipped under --only 28 — this run asked for the 28 region alone"
# ---- S6: the `--skip 28` smoke arm, the leg's other scope over the pristine fixture. It is also the
# ---- GREEN CONTROL for every fixture below: the flag arm and the allow-list join read the pristine
# ---- driver and leg without a finding, which is AC12's restored-verb half. Graded by what checks 22
# ---- and 26 say rather than by the whole verdict, because this fixture's conf predates keys other
# ---- checks now require, and a control that asserted the whole leg green would measure those.
reset_tree
out=$(run_skip_leg)
miss "$out" "unknown argument"
miss "$out" "UNATTENDED check 22 FAILED"
miss "$out" "UNATTENDED check 26 FAILED"

# ---- AC4, the allow-list join. A key removed from the region reds NAMING it; then the three region
# ---- shapes that yield no usable key - one sentinel gone, an empty pair, a doubled pair - each red
# ---- naming the REGION, because each would otherwise subtract nothing or everything and pass.
reset_tree
mutate $KIT_REL/check-unattended.sh 's/RECALL_CLI|ASKS_CMD|/RECALL_CLI|/'
hit "$(run_skip_leg)" "a key the shipped example declares and this leg initialises is missing from the import allow-list, so a project that declares it keeps the initialised default and every gate stays green: ASKS_CMD"
# ---- TOOL-dUnstuckLanding-13 AC9: HANDOFF_CUTOFF is joined by check 22 in both of its halves. Its
# ---- protocol row removed reds the key table; its allow-list entry removed reds the import join; with
# ---- all three in place neither line names it.
reset_tree
mutate memory/guides/UNATTENDED-PROTOCOL.md '/^| `HANDOFF_CUTOFF` |/d'
hit "$(run_skip_leg)" "undocumented in the protocol: HANDOFF_CUTOFF"
reset_tree
mutate $KIT_REL/check-unattended.sh 's/|HANDOFF_CUTOFF|/|/'
hit "$(run_skip_leg)" "a key the shipped example declares and this leg initialises is missing from the import allow-list, so a project that declares it keeps the initialised default and every gate stays green: HANDOFF_CUTOFF"
reset_tree
out=$(run_skip_leg)
miss "$out" "undocumented in the protocol: HANDOFF_CUTOFF"
miss "$out" "every gate stays green: HANDOFF_CUTOFF"
reset_tree
mutate $KIT_REL/check-unattended.sh '/^    # gov:conf-allow-end$/d'
hit "$(run_skip_leg)" "the import allow-list is not exactly one bare gov:conf-allow-begin and gov:conf-allow-end pair enclosing at least one key, so the join that reads it would subtract nothing or everything and report green over a real mismatch"
reset_tree
mutate $KIT_REL/check-unattended.sh '/^    # gov:conf-allow-begin$/,/^    # gov:conf-allow-end$/{/# gov:conf-allow-/!d}'
hit "$(run_skip_leg)" "the import allow-list is not exactly one bare gov:conf-allow-begin and gov:conf-allow-end pair enclosing at least one key, so the join that reads it would subtract nothing or everything and report green over a real mismatch"
reset_tree
mutate $KIT_REL/check-unattended.sh 's/^    # gov:conf-allow-end$/&\n    # gov:conf-allow-begin\n    # gov:conf-allow-end/'
hit "$(run_skip_leg)" "the import allow-list is not exactly one bare gov:conf-allow-begin and gov:conf-allow-end pair enclosing at least one key, so the join that reads it would subtract nothing or everything and report green over a real mismatch"

# ---- AC5 and AC6, the flag arm in both directions: a header flag no parser takes, and a parser arm
# ---- no header names.
reset_tree
mutate $KIT_REL/unattended.sh 's/^#   unattended\.sh --status <slug> /#   unattended.sh --status <slug> [--frobnicate] /'
hit "$(run_skip_leg)" "the driver's header documents a flag no parser token accepts, so the usage text a reader follows names an argument the driver refuses: --frobnicate"
reset_tree
mutate $KIT_REL/unattended.sh 's/^    --pass)         PK_ITEM=/    --frobnicate)   shift ;;\n    --pass)         PK_ITEM=/'
hit "$(run_skip_leg)" "the driver's parser accepts a flag no header line documents, and the usage text is rendered from that header, so the argument reaches no reader: --frobnicate"
# ---- AC12: a slug verb is parsed by SET MEMBERSHIP. Dropped from VERBS_SLUG with its header line
# ---- kept, it is a documented flag nothing parses; restored, the pristine control above is silent.
reset_tree
mutate $KIT_REL/unattended.sh '/^VERBS_SLUG=/s/ --audit / /'
hit "$(run_skip_leg)" "the driver's header documents a flag no parser token accepts, so the usage text a reader follows names an argument the driver refuses: --audit"

# ---- AC8, the suite half. The fixture carries NEITHER suite, which is every adopter tree: one
# ---- announced skip per suite, and the verdict is the other checks'. Then a driver suite with every
# ---- `--version` line dropped, and one with every `--framed` line dropped, each red naming the flag.
reset_tree
out=$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" --skip 28 2>&1)
miss "$out" "UNATTENDED check 26 FAILED"
hit "$out" "/unattended.test.sh — this tree does not carry the suite, which is withheld from every adopter install, so no arm can be joined to the flags its parser accepts"
hit "$out" "/check-unattended.test.sh — this tree does not carry the suite, which is withheld from every adopter install, so no arm can be joined to the flags its parser accepts"
grep -v -- '--version' "$HERE/unattended.test.sh" > "$TMP/$KIT_REL/unattended.test.sh"
out=$(run_skip_leg)
hit "$out" "a flag a parser accepts appears on no non-comment line of its suite, so no arm has ever passed it and it is the one invocation nobody runs"
hit "$out" "/unattended.test.sh lacks --version"
grep -v -- '--framed' "$HERE/unattended.test.sh" > "$TMP/$KIT_REL/unattended.test.sh"
hit "$(run_skip_leg)" "unattended.test.sh lacks --framed"
# ---- AC13, the leg's own half: its suite with every `--skip` line dropped reds naming `--skip`, and
# ---- the leg with its argv-begin sentinel deleted reds naming the region.
reset_tree
grep -v -- '--skip' "$HERE/check-unattended.test.sh" > "$TMP/$KIT_REL/check-unattended.test.sh"
hit "$(run_skip_leg)" "check-unattended.test.sh lacks --skip"
reset_tree
mutate $KIT_REL/check-unattended.sh '/^# gov:argv-begin$/d'
hit "$(run_skip_leg)" "a parser's argument region is not exactly one bare gov:argv-begin and gov:argv-end pair holding at least one flag, so the flag join would grade that parser against nothing and pass by finding nothing"
reset_tree

# ==== TOOL-dDerivedDocket-28 S8: CHECK 41, a process not in the ledger is never killed ===============
# ---- Both carriers an agent acts from must say so. The stops template is SEEDED into the kit copy
# ---- here, because the shared fixture carries only the Skill's; the pristine pair is the GREEN control,
# ---- each carrier with the sentence reworded is a RED naming that file, and an absent carrier is
# ---- announced on the report channel rather than graded green in silence.
reset_tree
cp "$HERE/STOPS.template.md" $KIT_REL/
out=$(GOV_UNATTENDED_REPORT=1 run)
miss "$out" "does not state that a process not in the ledger is never killed"
hit  "$out" "check 41 graded 2 of 2 carriers of the process-ledger rule"
mutate $KIT_REL/STOPS.template.md 's/never killed/sometimes killed/I'
out=$(run)
hit  "$out" "a carrier an agent acts from does not state that a process not in the ledger is never killed, so a stray process carrying this kit's command line is left to the agent's judgement, which is how a run had to be parked over five processes that were another repository's"
hit  "$(printf '%s\n' "$out" | grep 'UNATTENDED check 41 FAILED')" "/STOPS.template.md"
reset_tree
mutate $KIT_REL/SKILL.template.md 's/never killed/sometimes killed/I'
out=$(GOV_UNATTENDED_REPORT=1 run)
hit  "$(printf '%s\n' "$out" | grep 'UNATTENDED check 41 FAILED')" "/SKILL.template.md"
hit  "$out" "check 41 did not grade"
hit  "$out" "check 41 graded 1 of 2 carriers of the process-ledger rule"
reset_tree

# ==== TOOL-dDerivedDocket-27 S6 and S7: CHECK 42, the unattended bar's wall, and CHECK 43, the hold routing
# ---- Check 42 runs the project's declared GATE_PROFILE_CMD, so a STUB profile is written after every
# ---- reset: it prints `wall`, `queue` and `ceiling_max` from C42_WALL, C42_QUEUE and C42_CMAX, each only
# ---- when set, and exits C42_RC. The shared fixture's conf declares no GATE_* key, which is the state
# ---- every adopter starts in and the first arm's subject.
# ...and the two keys appended to the working conf, the later spelling winning when it is sourced.
# AC15, the leg's half: a BLANK profile command is announced on the report channel and never reds.
reset_tree; seed_c42
out=$(GOV_UNATTENDED_REPORT=1 run)
hit  "$out" "check 42 cannot compare the unattended bar's wall with the largest leg ceiling: this project declares no GATE_PROFILE_CMD, so there is no profile to read ceiling_max from"
miss "$out" "UNATTENDED check 42 FAILED"
# ...and a declared profile printing neither queue nor wall is announced naming the key it lacked,
# as is one printing no ceiling_max under a declared wall.
write_c42_conf "" "bash c42-profile.sh"
out=$(GOV_UNATTENDED_REPORT=1 run)
hit  "$out" "check 42 cannot compare the unattended bar's wall with the largest leg ceiling: GATE_WALL is blank and the profile printed no usable wall, so there is no wall to compare with the largest leg ceiling"
miss "$out" "UNATTENDED check 42 FAILED"
write_c42_conf "40" "bash c42-profile.sh"
hit  "$(GOV_UNATTENDED_REPORT=1 run)" "check 42 cannot compare the unattended bar's wall with the largest leg ceiling: the profile printed no usable ceiling_max, so the 40s wall cannot be compared with the largest leg ceiling"
# AC4, the leg's half: a declared wall below the profile's largest ceiling reds, naming both numbers,
# although the profile's OWN wall clears it. RED against a comparison with that wall.
write_c42_conf "10" "bash c42-profile.sh"
out=$(C42_WALL=40 C42_QUEUE=20 C42_CMAX=30 run)
hit  "$out" "the unattended bar's wall is below the largest declared leg ceiling, so a healthy bar that dispatches that leg is killed by its own wall and every unattended close reads red over a bound nobody chose"
hit  "$out" "the effective wall, the declared GATE_WALL, is 10s, below the largest declared leg ceiling of 30s"
# ...the GREEN control: a wall equal to the ceiling clears it, and the report channel says so.
write_c42_conf "30" "bash c42-profile.sh"
out=$(GOV_UNATTENDED_REPORT=1 C42_WALL=40 C42_QUEUE=20 C42_CMAX=30 run)
hit  "$out" "check 42 graded the unattended bar's wall: the effective wall, the declared GATE_WALL, is 30s and clears the largest declared leg ceiling of 30s"
miss "$out" "UNATTENDED check 42 FAILED"
# ...a BLANK wall is the profile's own, graded the same way.
write_c42_conf "" "bash c42-profile.sh"
hit  "$(C42_WALL=5 C42_QUEUE=20 C42_CMAX=30 run)" "the effective wall, the profile's own wall, GATE_WALL being blank, is 5s, below the largest declared leg ceiling of 30s"
# ...a wall the driver would refuse at conf load is a red: no verb of any run is reachable under it.
write_c42_conf "ten" "bash c42-profile.sh"
hit  "$(run)" "', which is not a positive integer of seconds, so the driver refuses at conf load and no verb of any unattended run in this project is reachable"
# ...a profile command that fails, and one reporting no ceiling at all, are announced and never red.
write_c42_conf "30" "bash c42-profile.sh"
out=$(GOV_UNATTENDED_REPORT=1 C42_RC=3 run)
hit  "$out" "check 42 cannot compare the unattended bar's wall with the largest leg ceiling: the declared GATE_PROFILE_CMD exited 3: bash c42-profile.sh"
miss "$out" "UNATTENDED check 42 FAILED"
hit  "$(GOV_UNATTENDED_REPORT=1 C42_WALL=40 C42_QUEUE=20 C42_CMAX=- run)" "the profile reports that no leg declares a ceiling, so the 30s wall has no ceiling to clear"
# CHECK 43, the GREEN control first: the kit's own Skill template routes a hold line correctly.
reset_tree
miss "$(run)" "UNATTENDED check 43 FAILED"
# ...the hold lead gone is a red, because a paragraph this cannot find would pass by finding nothing.
mutate $KIT_REL/SKILL.template.md 's/^\*\*A `hold ·` line from `gates-green` is your next step/**A hold line is next/'
hit  "$(run)" "the Skill template's Close section carries no paragraph opening with the hold lead, so nothing tells a run what to do with the hold line gates-green prints, and this check would pass by finding nothing"
# ...--hold named before the commit is a red, which the HELD unit's clean-tree precondition refuses.
reset_tree
mutate $KIT_REL/SKILL.template.md 's/Take it in this order: commit the staged records/Take it in this order: run --hold, then commit the staged records/'
out=$(run)
hit  "$out" "the Skill's hold paragraph does not name the commit of the staged records, the branch push, the keepalive reap and --hold in that order, and --hold refuses a dirty tree and, under ANCHOR_SCOPE=published, an unpublished tip; the first step missing or out of order"
hit  "$(printf '%s\n' "$out" | grep 'UNATTENDED check 43 FAILED')" "the first step missing or out of order: --hold"
# ...no platform-unavailable hold for a push the remote does not answer is a red.
reset_tree
mutate $KIT_REL/SKILL.template.md 's/take the hold as `platform-unavailable` instead/take another hold instead/'
hit  "$(run)" "the Skill's hold paragraph names no platform-unavailable hold for a branch push the remote does not answer, so under ANCHOR_SCOPE=published the run's only documented ending is refused"
# ...and a hold line routed to an override is a red, which spends the one check on a host fault.
reset_tree
mutate $KIT_REL/SKILL.template.md 's/then run `--hold` with the code/then run `--close --override gates-green` or `--hold` with the code/'
hit  "$(run)" "the Skill's hold paragraph routes a hold line to an override, which spends the one check between a run and its landing on a fault that is not the run's"
reset_tree

# ==== TOOL-dAlignedCarrier-1: CHECK 47, the retired commit premise in any shipped file of the kit
# ---- The staged line is ASSEMBLED FROM FRAGMENTS split inside their words, so the staged sentence
# ---- never exists contiguously in this suite's own bytes, and the real-tree leg, which reads this
# ---- file too, stays clean. It is written to a file and appended by sed's `r`, as check 33's arm
# ---- does, and the copy it lands in is the fixture's tracked lib, one of the population's plain
# ---- shell files.
reset_tree
_c47_no="n""o"; _c47_dv="dri""ver ve""rb"; _c47_cm="comm""its"
printf '# the rows: %s %s %s them\n' "$_c47_no" "$_c47_dv" "$_c47_cm" > "$TMPBIN_PARENT/c47.line"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c47.line"
out=$(run)
hit  "$out" "a shipped file of this kit states the retired premise that the driver makes no commit of its own, but under LANDER_MODE=in-place --close commits its own records commit, so a reader who trusts the sentence expects staged rows to stay uncommitted after the close has committed them; reword it to name the step that commits them. matches: "
hit  "$(printf '%s\n' "$out" | grep 'UNATTENDED check 47 FAILED')" "matches: $KIT_REL/lib-unattended.sh: "
# ...the NEAR-MISS, a control on the predicate rather than a second break: the same words ending in
# a verb that makes no commit, the shape a sibling suite carries, stay silent. Without it the arm
# above is equally consistent with a ban on every sentence that names the driver's verbs at all.
reset_tree
printf '# the rows: %s %s does\n' "$_c47_no" "$_c47_dv" > "$TMPBIN_PARENT/c47.line"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c47.line"
miss "$(run)" "UNATTENDED check 47 FAILED"
reset_tree

# ==== TOOL-dAlignedCarrier-6: CHECK 47's SECOND ROW, the retired premise that the landing's close
# ---- is where the owed flagged bar is told (closing review L2). Assembled from fragments split
# ---- inside their words, as the first row's arm is, so this suite's own bytes form no instance.
# ---- Both alternatives are staged, the mode token first and the announcing word first.
_c47_ip="in-""place"; _c47_an="anno""unces"
printf '# the %s close %s the owed bar\n' "$_c47_ip" "$_c47_an" > "$TMPBIN_PARENT/c47.line"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c47.line"
out=$(run)
hit  "$out" "a shipped file of this kit states the retired premise that the landing's close is where the owed flagged bar is told, but since TOOL-dAlignedCarrier-6 the move into VERIFYING announces it under every LANDER_MODE and the close says nothing, so a reader who trusts the sentence waits at the close for a notice that never comes; reword it to name the move into VERIFYING. matches: "
hit  "$(printf '%s\n' "$out" | grep 'UNATTENDED check 47 FAILED')" "matches: $KIT_REL/lib-unattended.sh: \"$_c47_ip close $_c47_an\""
reset_tree
printf '# it %s, on an %s close, that the bar is owed\n' "$_c47_an" "$_c47_ip" > "$TMPBIN_PARENT/c47.line"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c47.line"
out=$(run)
hit  "$out" "the retired premise that the landing's close is where the owed flagged bar is told"
hit  "$(printf '%s\n' "$out" | grep 'UNATTENDED check 47 FAILED')" "matches: $KIT_REL/lib-unattended.sh: \"$_c47_an, on an $_c47_ip close,\""
# ...the NEAR-MISS: the same mode's close with no announcing word stays silent, so the arm above is
# not equally consistent with a ban on naming that close at all.
reset_tree
printf '# the %s close runs the bar\n' "$_c47_ip" > "$TMPBIN_PARENT/c47.line"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c47.line"
miss "$(run)" "UNATTENDED check 47 FAILED"
reset_tree

# ==== TOOL-dAlignedCarrier-6 rev-5: CHECK 47's WINDOW HOLDS EACH ROW'S WIDEST INSTANCE WRAPPED AT
# ---- EVERY WORD, AND EACH EXCERPT IS WHOLE (closing review round 2, L1 and L4). Row 2's widest
# ---- instance is eight words and row 1's seven. Each is staged once per position it can wrap at,
# ---- every copy after a line of eight neutral words that flushes the window, and the ONE run must
# ---- report the whole quoted excerpt once per copy: 7 for row 2, 6 for row 1. A window a word short
# ---- drops a copy and a pattern ending on a bare stem truncates every excerpt, so either reds the
# ---- count. Fragments as above, so this suite's own bytes form no instance.
_c47_ip="in-""place"; _c47_an="anno""unces"; _c47_no="n""o"; _c47_vb="ve""rb"; _c47_cm="comm""its"
for _c47_row in "$_c47_ip p q close r s t $_c47_an" "$_c47_no p q $_c47_vb r s $_c47_cm"; do
  read -r -a _c47_w <<<"$_c47_row"
  for ((_c47_i = 1; _c47_i < ${#_c47_w[@]}; _c47_i++)); do
    printf '# f f f f f f f f\n# %s\n# %s\n' "${_c47_w[*]:0:_c47_i}" "${_c47_w[*]:_c47_i}"
  done
done > "$TMPBIN_PARENT/c47.line"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c47.line"
out=$(run)
same "check 47 row 2 wrapped at each of its 7 positions" \
  "$(printf '%s\n' "$out" | grep -F "the landing's close is where the owed flagged bar is told" | grep -oF "\"$_c47_ip p q close r s t $_c47_an\"" | wc -l | tr -d ' ')" 7
same "check 47 row 1 wrapped at each of its 6 positions" \
  "$(printf '%s\n' "$out" | grep -F "the driver makes no commit of its own" | grep -oF "\"$_c47_no p q $_c47_vb r s $_c47_cm\"" | wc -l | tr -d ' ')" 6
reset_tree

# ==== TOOL-dAlignedCarrier-6: CHECK 48, a run-state fact written after the function's last stage
# ---- of it (closing review M1). The staged function is written to a file and appended by sed's
# ---- `r` into the fixture's tracked lib, one of the population's shell files; its two calls are
# ---- spelled from fragments, so this suite's own bytes carry no function the real-tree leg grades.
_c48_st="stage""_or_fail"; _c48_sw="set""_fact"
printf 'c48probe() {\n  %s "$rel" || return 1\n  %s "$rel" witness x || return 1\n}\n' "$_c48_st" "$_c48_sw" > "$TMPBIN_PARENT/c48.fn"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c48.fn"
out=$(run)
hit  "$out" "a function in a shipped shell file of this kit writes a run-state fact after its last staging of that same file, so the index holds the file as it was before that write and the write stays unstaged: a commit of what the verb staged records half of it and leaves the tree dirty; stage after the last write. matches: "
hit  "$(printf '%s\n' "$out" | grep 'UNATTENDED check 48 FAILED')" "matches: $KIT_REL/lib-unattended.sh:"
# ...the NEAR-MISS: the same two calls with the write first and the stage last stay silent, so the
# arm above is not equally consistent with a ban on writing a fact inside a staging function at all.
reset_tree
printf 'c48probe() {\n  %s "$rel" witness x || return 1\n  %s "$rel" || return 1\n}\n' "$_c48_sw" "$_c48_st" > "$TMPBIN_PARENT/c48.fn"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c48.fn"
miss "$(run)" "UNATTENDED check 48 FAILED"
reset_tree

# ==== TOOL-dUnstuckLanding-20: CHECK 49, a LANDING_NODES token that is not a <tag>=<machine>/<user>
# ---- pair, or a tag declared twice, reds naming each; a malformed token claims its tag, so `d` is the
# ---- doubled one here. The well-formed value beside it stays silent, so the red is not a ban on the key.
printf 'LANDING_NODES="d=compeeto a=m/u d=m2/u2"\n' >> .unattended.conf
out=$(run)
hit  "$out" "LANDING_NODES declares a token that is not a <tag>=<machine>/<user> pair, or a tag or machine/user declared twice, and a malformed token never matches, so that node hands off on every run with nothing else red: d=compeeto d"
reset_tree
printf 'LANDING_NODES="a=m/u d=compeeto/d41ly"\n' >> .unattended.conf
miss "$(run)" "UNATTENDED check 49 FAILED"
reset_tree
# ---- closing review round 1 M14 (id 21): one machine/user under two tags, and a pair with a third
# ---- field, each red by name; RED against a staged scan that skipped each. L2 (id 22): a `%20`-escaped
# ---- user is a well-formed pair, so the escape the driver decodes is not a malformed token here.
printf 'LANDING_NODES="a=m/u b=m/u"\n' >> .unattended.conf
hit  "$(run)" "so that node hands off on every run with nothing else red: m/u"
reset_tree
printf 'LANDING_NODES="a=m/u/x"\n' >> .unattended.conf
hit  "$(run)" "so that node hands off on every run with nothing else red: a=m/u/x"
reset_tree
printf 'LANDING_NODES="a=desk/john%%20smith"\n' >> .unattended.conf
miss "$(run)" "UNATTENDED check 49 FAILED"
reset_tree

# ==== Implementation review round 2, hunt item 3: CHECK 50, the driver's inherited-red policy path
# ---- against the pre-push hook's `_gate_env` derivation. A hook spelling another file reds, and so
# ---- does a driver that moved its own; the two spelling one path stay silent, and a tree tracking no
# ---- hook says it compared nothing. RED against the leg before the check, which read neither.
out=$(GOV_UNATTENDED_REPORT=1 run)
hit  "$out" "unattended-report: check 50 did not compare the inherited-red policy path - this tree tracks no .githooks/pre-push, so no hook reads one beside the driver"
mkdir -p .githooks
printf '#!/usr/bin/env bash\n_gate_env="$top/.githooks/gate-env.sh"\n' > .githooks/pre-push
git add .githooks/pre-push
out=$(GOV_UNATTENDED_REPORT=1 run)
miss "$out" "UNATTENDED check 50 FAILED"
hit  "$out" "unattended-report: check 50 compared the inherited-red policy path the driver and the pre-push hook read: .githooks/gate-env.sh"
printf '#!/usr/bin/env bash\n_gate_env="$top/.githooks/policy-env.sh"\n' > .githooks/pre-push
git add .githooks/pre-push
hit  "$(run)" "the driver's inherited-red policy path is not the pre-push hook's, so on a conf naming no policy file the two readers of one policy read two files, and a red the driver lands is one the hook refuses to push: hook .githooks/policy-env.sh, driver .githooks/gate-env.sh"
printf '#!/usr/bin/env bash\n_gate_env="$top/.githooks/gate-env.sh"\n' > .githooks/pre-push
git add .githooks/pre-push
mutate $KIT_REL/unattended.sh 's|hook="\.githooks/gate-env\.sh"|hook=".githooks/moved-env.sh"|'
hit  "$(run)" "a red the driver lands is one the hook refuses to push: hook .githooks/gate-env.sh, driver .githooks/moved-env.sh"
reset_tree

# ==== TOOL-aGraftedHelix-31: CHECK 51, a function that writes a terminal phase and never the run claim
# ---- (closing review H3). The staged function is appended to the fixture's tracked lib by sed's `r`,
# ---- as check 48's arms stage theirs, and its write is spelled from fragments so this suite's own
# ---- bytes carry nothing the real-tree leg could read as a writer. RED, the three red arms, against
# ---- the leg with the check's block deleted.
_c51_sw="set""_fact"
printf 'c51probe() {\n  %s "$rel" phase ABORTED || return 1\n}\n' "$_c51_sw" > "$TMPBIN_PARENT/c51.fn"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c51.fn"
out=$(run)
hit  "$out" "a function in a shipped shell file of this kit writes a terminal phase and no run claim, so the run it ends leaves its claim on the remote reading live or held, a held claim never ages, and the slug's next --preflight is refused at check 107 by a claim nobody releases; write the claim with write_claim after the record is staged, or name the function on TERMINAL_CLAIM_EXEMPT_FNS with its reason"
hit  "$(printf '%s\n' "$out" | grep -F 'c51probe()')" "$KIT_REL/lib-unattended.sh:"
# ...the same function named on the list is silent, so the arm above is not a ban on the write.
reset_tree
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c51.fn"
mutate $KIT_REL/check-unattended.sh 's|^TERMINAL_CLAIM_EXEMPT_FNS=.*|TERMINAL_CLAIM_EXEMPT_FNS="c51probe"|'
miss "$(run)" "writes a terminal phase and no run claim"
# ...a STALE entry reds by name: one naming no function the predicate would hit widens the set.
reset_tree
mutate $KIT_REL/check-unattended.sh 's|^TERMINAL_CLAIM_EXEMPT_FNS=.*|TERMINAL_CLAIM_EXEMPT_FNS="ghostfn"|'
hit  "$(run)" "TERMINAL_CLAIM_EXEMPT_FNS names ghostfn(), which is no function writing a terminal phase without a claim write"
# ...LIVENESS: every terminal write respelled with a quoted key, the same write to bash and one the
# predicate does not match, so the scan finds no writer and must refuse rather than pass.
reset_tree
mutate $KIT_REL/unattended.sh 's/\(set_fact "\$[A-Za-z_]*" \)phase \(LANDED\|ABORTED\)/\1"phase" \2/g'
hit  "$(run)" "the scan found no function writing a terminal phase in this kit's shell files, so its predicate no longer matches how the driver spells that write and the claim pairing would be graded over no writer at all, passing by finding nothing"
# ...the CONTROL: the shipped driver and the shipped, empty list print neither failure, and the
# report counts the writers it graded.
reset_tree
out=$(GOV_UNATTENDED_REPORT=1 run)
miss "$out" "writes a terminal phase and no run claim"
miss "$out" "the scan found no function writing a terminal phase"
hit  "$out" "writing a terminal phase, 0 exempt"
reset_tree
# ---- TOOL-aGraftedHelix-38 S3: a claim write through a DECLARED helper, TERMINAL_CLAIM_HELPER_FNS, one
# ---- level deep. Staged as the arms above are. (a) a writer calling an UNLISTED helper that writes no
# ---- claim is a hit, so following any call is not the rule; (b) that helper on the list is a hit on
# ---- the list entry, whose own body holds no write_claim; (c) a writer whose only claim write is
# ---- run_hold's `held`, unlisted, is a hit, the H3 shape, so following any CLAIM-WRITING call is not
# ---- the rule either; (d) a writer through the shipped helper is silent; (e) a stale entry reds.
printf 'c51nohelper() {\n  %s "$rel" phase ABORTED || return 1\n  c51quiet "$rel"\n}\nc51quiet() {\n  echo "$1"\n}\n' "$_c51_sw" > "$TMPBIN_PARENT/c51a.fn"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c51a.fn"
hit  "$(run)" "c51nohelper() writes a terminal phase and never calls write_claim"
reset_tree
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c51a.fn"
mutate $KIT_REL/check-unattended.sh 's|^TERMINAL_CLAIM_HELPER_FNS=.*|TERMINAL_CLAIM_HELPER_FNS="write_settle_claim c51quiet"|'
hit  "$(run)" "TERMINAL_CLAIM_HELPER_FNS names c51quiet(), whose own body holds no write_claim call"
reset_tree
printf 'c51hold() {\n  %s "$rel" phase ABORTED || return 1\n  run_hold "$slug" x x x x x x\n}\n' "$_c51_sw" > "$TMPBIN_PARENT/c51c.fn"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c51c.fn"
hit  "$(run)" "c51hold() writes a terminal phase and never calls write_claim"
reset_tree
printf 'c51settle() {\n  %s "$rel" phase ABORTED || return 1\n  write_settle_claim "$slug" "$rel" x first\n}\n' "$_c51_sw" > "$TMPBIN_PARENT/c51d.fn"
mutate $KIT_REL/lib-unattended.sh "\$r $TMPBIN_PARENT/c51d.fn"
miss "$(run)" "c51settle() writes a terminal phase"
reset_tree
mutate $KIT_REL/check-unattended.sh 's|^TERMINAL_CLAIM_HELPER_FNS=.*|TERMINAL_CLAIM_HELPER_FNS="write_settle_claim ghosthelper"|'
hit  "$(run)" "TERMINAL_CLAIM_HELPER_FNS names ghosthelper(), which is no function of the shell files this check reads"
reset_tree
fi   # ---- end of the region-8 span, re-cut across the eight regions by TOOL-aGraftedHelix-34 S7 ---------

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
# ---- RAISED 410 -> 419 by TOOL-dDerivedDocket-5: check 36's nine arms, all in the LANDER_MODE
# ---- fixture block inside region two, so FLOOR_SHARD_2 carries the same +9 and FLOOR_SHARD_1
# ---- is untouched.
# ---- RAISED 419 -> 457 by exactly the arm, TOOL-dDerivedDocket-52: the resolver's thirty-eight
# ---- assertions over its eight scratch fixtures, all in the block at the END of region two, so
# ---- FLOOR_SHARD_2 carries the same +38 and FLOOR_SHARD_1 is untouched. COUNTED, not measured
# ---- through a suite run: this unit's pass may run no suite, so the figure is the block's own
# ---- `hit`/`same`/`miss` calls plus its two bare `n=$((n+1))` sites, and the block was executed
# ---- once standalone in a replica of this prologue to confirm it -- thirty-eight assertions,
# ---- green, and red under each of six staged breaks.
# ---- RAISED 457 -> 517 by exactly the arm, TOOL-dDerivedDocket-18: the ask-mandate block's
# ---- sixty executed assertions, all in its own repository at the END of region two, so
# ---- FLOOR_SHARD_2 carries the same +60 and FLOOR_SHARD_1 is untouched. COUNTED by executing the
# ---- block standalone in a replica of this prologue, the same way and for the same reason as the
# ---- line above: this unit's pass may run no suite.
# ---- RAISED 517 -> 549 by exactly the arm, TOOL-dDerivedDocket-54: the reachability probe's
# ---- thirty-two executed assertions over its one fixture repository, all at the END of region
# ---- two, so FLOOR_SHARD_2 carries the same +32 and FLOOR_SHARD_1 is untouched. COUNTED by
# ---- executing the block standalone in a replica of this prologue, for the reason above.
# ---- RAISED 549 -> 582 by exactly the arm, TOOL-dDerivedDocket-19: the grant block's 33
# ---- assertions, all in region two, so FLOOR_SHARD_2 moves by the same 33. Measured by running the
# ---- block alone behind this suite's prologue by hand, n 0 -> 33; this pass runs no suite.
# ---- RAISED 582 -> 592 by exactly the arm, TOOL-dDerivedDocket-20: the ask-guide pair's three
# ---- check-10 arms, its pair-count report arm and check 38's six, ten unconditional `hit`/`miss`
# ---- calls, all beside check 10 inside region one, so FLOOR_SHARD_1 carries the same +10 and
# ---- FLOOR_SHARD_2 is untouched. COUNTED off the diff; this pass runs no suite. Its checklist fold
# ---- added check 38's report-channel liveness arm, one more in the same place: 592 -> 593.
# ---- RAISED 593 -> 633 by exactly the arm, TOOL-dDerivedDocket-22: forty assertions, all in
# ---- region two - four in the ask block, six in the grant block and thirty in the derived-
# ---- terminal block at its END - so FLOOR_SHARD_2 carries the same +40 and FLOOR_SHARD_1 is
# ---- untouched. MEASURED by running the three blocks behind a replica of this prologue by hand,
# ---- n 0 -> 40 and green, and red under eight staged breaks; this pass runs no suite.
# ---- MERGED 2026-09-21 at the reconcile of origin/main into dDerivedDocket: both sides raised all
# ---- three floors from one base - the dDerivedDocket and aWokenSentinel raise lines above - so
# ---- each constant is base + ours + theirs. FLOOR_ASSERTIONS 410 + 223 + 24 = 657; FLOOR_SHARD_1
# ---- 91 + 11 + 0 = 102; FLOOR_SHARD_2 319 + 212 + 24 = 555. COUNTED off the two sides' own raise
# ---- lines, not measured through a suite run: the merge runs no suite. main's check-32 and
# ---- check-33 arms keep main's numbers; this build's phase-routing pair, which its own spec
# ---- calls 32 and 33, is checks 39 and 40 in the merged leg.
# ---- RAISED 657 -> 700 by exactly the arm, TOOL-dDerivedDocket-30: forty-three executed assertions,
# ---- all in region two - four check-23 brief fixtures G to J beside arm F, and thirty-nine in the
# ---- unit's block at the END of region two - so FLOOR_SHARD_2 carries the same +43 and
# ---- FLOOR_SHARD_1 is untouched. COUNTED by executing both blocks behind a replica of this
# ---- prologue by hand; this pass runs no suite.
# ---- RAISED 700 -> 710 by exactly the arm, TOOL-dDerivedDocket-28: the check-41 block at the END
# ---- of region two executes nine assertions (two `mutate`, six `hit`, one `miss`) and the
# ---- `--only 28` announcement loop one more for check 41, so FLOOR_SHARD_2 carries the same +10 and
# ---- FLOOR_SHARD_1 is untouched. COUNTED off the diff; this pass runs no suite, and the check's
# ---- block was run sliced out of the leg over the kit and its staged breaks.
# ---- RAISED 710 -> 736 by exactly the arm, TOOL-dDerivedDocket-27: the check-42 and check-43 block at
# ---- the END of region two executes twenty-four assertions (four `mutate`, fifteen `hit`, five
# ---- `miss`) and the `--only 28` announcement loop two more, so FLOOR_SHARD_2 carries the same +26
# ---- and FLOOR_SHARD_1 is untouched. COUNTED by running the block behind a replica of this prologue
# ---- by hand, n 0 -> 24 and green, and red under four staged breaks; this pass runs no suite.
# ---- RE-MEASURED at TOOL-aBatchedArm-3, 2026-09-13, node a, from the xtrace of one unsharded run at
# ---- BASE (every `n=` increment attributed to the region it fired in) and confirmed by the eight
# ---- shard runs and the unsharded run at the commit: figures beside each constant below, ~3 % under
# ---- the reading. The sum of the eight shard readings equals the unsharded reading EXACTLY, so
# ---- PROLOGUE_ARMS is still 0 for the floor-graded count: the C21 pair below runs AFTER the grade
# ---- and is an epilogue constant only the PASS line carries. The floors are not asserted to sum to
# ---- FLOOR_ASSERTIONS: with one discount over a clean partition they nearly do, and that is a
# ---- coincidence of the numbers, not an invariant.
# ---- READINGS, 2026-09-14, node a, TOOL-aBatchedArm-3's Phase B (its acceptance ledger has the runs):
# ---- unsharded at HEAD 555 (BASE 554 + the one `same` S6 adds); shards on the landed cut 81 · 58 ·
# ---- 38 · 77 · 64 · 75 · 93 · 69, of which 1..4 are the repeat's direct runs, 5 and 6 the first
# ---- candidate's (their regions did not move), 7 the profiled run of the re-cut region, and 8 is
# ---- DERIVED as 162 - 93 from the first candidate's regions 7 + 8 — the one figure below with no
# ---- direct run behind it. The build was landed by owner ruling before its closing runs, so
# ---- FLOOR_SHARD_8 is re-read at the build's final gate pass and corrected there if it moved.
# ---- MERGED 2026-09-14 with main's +8 assertions (TOOL-aRatifiedRulings-2's five check-23 brief
# ---- fixtures, seven, and its closing review's fixture F, one), which landed in the old region two
# ---- and now sit in whichever of the eight regions the merge placed them; every floor below is a
# ---- MINIMUM the counts rose past, and all nine are re-read at the build's final gate pass.
# ---- RE-READ at the build's final pass, 2026-09-15, node a, from the eight direct shard runs on a
# ---- frozen clone at 72f54937 and their pasted-set re-runs at 7549981a: shards 83 · 59 · 40 · 78 ·
# ---- 64 · 78 · 95 · 80 (sum 577 = unit 3's 555 + the fourteen check_emitted calls + main's eight
# ---- merged arms), every floor below ~3 % under its reading, FLOOR_SHARD_8 now a READING and not
# ---- a derivation. The unsharded floor is the sum's discount; no unsharded run was taken at this
# ---- pass, and the eight-shard partition is the pooled route's own reading.
# ---- MERGED 2026-09-15 with main's +10 assertions (aProbedUnit: four check-2 disposition fixtures,
# ---- two BOUNDED check-2 fixtures, and the round-2 trio with its `mutate`), which all landed in
# ---- REGION 2 of this partition. RE-READ the same day, node a, from the eight direct shard runs on
# ---- a frozen clone at a117faeb, 8-wide on an idle box (517-922 s each): 83 · 69 · 40 · 78 · 64 ·
# ---- 78 · 95 · 80 (sum 587 = 577 + the ten), FAIL union still the 21-line oracle, no check_emitted
# ---- red; FLOOR_SHARD_2 and FLOOR_ASSERTIONS re-read ~3 % under, the other seven unchanged.
# ---- MERGED 2026-09-22 with main's growth since 4cf0944d (aWokenSentinel's check-31, -32 and -33
# ---- arms and the aProbedUnit fold, main's own floor 410 -> 434, +24 assertions), which land in
# ---- whichever of the eight regions this partition puts them in. Every floor below is therefore a
# ---- MINIMUM the counts rose past until the landing's own shard runs re-read all nine.
# ---- RE-READ 2026-09-22 at the aBatchedArm landing, node a, from eight direct `--shard k/8` runs on
# ---- a frozen clone at a5d54fb6 — the first run of this file with EVERY arm reaching its assertion,
# ---- since the twenty-two reds it carried were all fixtures pinned to texts that had moved. Readings
# ---- 86 · 69 · 49 · 102 · 64 · 78 · 95 · 94 (sum 637); every floor ~3 %% under its own, the unsharded floor the sum's discount.
# ---- MERGED 2026-09-27 at the second reconcile of origin/main into dDerivedDocket. This build's raise
# ---- lines above counted its arms in the TWO-region cut it was written against: +302 over base 434,
# ---- eleven in its region one and 291 in its region two. main re-cut the suite into eight regions
# ---- and re-read every floor, 434 -> 617, +183. FLOOR_ASSERTIONS is base + ours + theirs, 434 + 302 +
# ---- 183 = 919. The per-shard floors are main's, each raised by this build's arms that LAND in that
# ---- region of the eight-way cut: the eleven beside checks 10 and 38 sit in region 3 (47 -> 58), the
# ---- five check-16 count-word and asks-disposed arms in region 5 (62 -> 67), and the other 286 at the
# ---- END of region 8 (91 -> 377). COUNTED off both sides' own raise lines and a static census of where
# ---- each arm landed, not measured: the merge runs no suite, and all nine are owed a re-read at the
# ---- build's next gate pass. The `check 36` of the TOOL-dDerivedDocket-5 raise line above is check 46
# ---- in the merged leg: main took 34 to 36 first, so this build's three moved to 44 to 46.
# ---- RAISED 919 -> 923 by exactly the arm, the fold of dDerivedDocket's closing diff review, round
# ---- 1, F2: the IDLIST arms after the ask block's AC1, three `hit` and one `miss`, all at the END of
# ---- region 8, so FLOOR_SHARD_8 carries the same +4 and the other seven are untouched. MEASURED by
# ---- running that block alone behind a replica of this prologue by hand, n 64 -> 68, green on the
# ---- fold and red on HEAD's kit for all but the `miss`, which is the control; this pass runs no suite.
# ---- RAISED 923 -> 932 by exactly the arms dDerivedDocket's VERIFYING suite fix added, 2026-09-29:
# ---- region 1 +5, the five flags the dispatched-verb denylist gained, each one pass of its stale-
# ---- exemption loop; region 4 +2, check 36's scope liveness arm respelling all three fixture files
# ---- and reading the report's count; region 8 +2, check 39's liveness arm staging its break with a
# ---- `mutate` and the check-39 control's new `miss`. FLOOR_SHARD_1, _4 and _8 carry the same.
# ---- RAISED 938 -> 951 by exactly the arm, TOOL-aGraftedHelix-31: check 51's thirteen assertions
# ---- (five `mutate`, five `hit`, three `miss`), all at the END of region 8, so FLOOR_SHARD_8 carries
# ---- the same +13 and the other seven are untouched. MEASURED by running the block alone behind a
# ---- replica of this prologue on node a, 2026-10-05, n 0 -> 13 and green, and the three red arms red
# ---- with the check's block deleted from the fixture's leg; this pass runs no suite.
# ---- RAISED 951 -> 953 by TOOL-aGraftedHelix-34 S3: the dispatched-verb denylist's two new flags, each
# ---- one pass of its stale-exemption loop in region 1 (the `s1` slice, 34 -> 36). THE RE-CUT, S7 of
# ---- the same unit, moves no unsharded count. It moves six region-8 sections to regions 1, 3, 5, 6
# ---- and 7, so each per-shard floor below moves by what its slice EXECUTED, read off a slice of the
# ---- prologue, the normalization line and the section on node a, 2026-10-06 (the prologue alone
# ---- then executed 0, and executes 1 since the hoist arm below): checks 44 to 46, 21, and the derived terminal, 50, to region 1; check 23's
# ---- budget-to-ceiling arms, 72, to region 3; the ask-mandate opinions, 68, to region 5; the grant
# ---- and rounds arms, 77, to region 6; the conf hoist through check 51, 126, to region 7. A receiving
# ---- floor rises by 97 % of its sections, the discount every floor here carries; region 8's floor is
# ---- re-read whole, 97 % of its four remaining sections' executed counts (108, 34, 38 and 32, so 205),
# ---- because the old 402 had fallen far below the 626 that region ran; this pass runs no suite.
# ---- RAISED 953 -> 954 by TOOL-aGraftedHelix-36 S11: `check_helpers_hoisted`'s one prologue arm,
# ---- which every shard executes too, so each FLOOR_SHARD_k below rises by the same 1. MEASURED on a
# ---- slice of the prologue on node a, 2026-10-06, n 0 -> 1, green, and red with a column-0 helper
# ---- planted inside region 8 of a scratch copy; this pass runs no suite.
# ---- RAISED 954 -> 965 by exactly the arms, TOOL-aGraftedHelix-38 S3: check 51's helper-list arms
# ---- (six `mutate`, four `hit`, one `miss`), at the END of check 51's block in region 7, so
# ---- FLOOR_SHARD_7 carries the same +11 and the other seven are untouched. MEASURED on a slice of
# ---- the prologue and check 51's block on node a, 2026-10-06; this pass runs no suite.
# ---- RAISED 965 -> 967 by exactly the arm, TOOL-aGraftedHelix-39 S8: check 23's arm F, two same-
# ---- anchor rows with disjoint paths graded as their union (one `hit`, one `miss`), in the
# ---- widening-repair block of region 8, so FLOOR_SHARD_8 carries the same +2 and the other seven
# ---- are untouched. The block's old arm F, both ids in one group, is relabelled G. MEASURED on a
# ---- slice of the prologue and arms A to G on node a, 2026-10-06; this pass runs no suite.
FLOOR_ASSERTIONS=967
# THE FLOOR IS MODE-SELECTED, or every shard leg reds forever against the unsharded floor. The
# per-shard floors carry the SAME proportional discount the unsharded pin does rather than pinning
# at 100 % of observation, which would red on the first arm anyone legitimately removes. The
# figure every floor reads is the FLOOR-GRADED count — `$n` at the grade below — never the PASS line.
FLOOR_SHARD_1=159
FLOOR_SHARD_2=67
FLOOR_SHARD_3=128
FLOOR_SHARD_4=101
FLOOR_SHARD_5=133
FLOOR_SHARD_6=150
FLOOR_SHARD_7=226
FLOOR_SHARD_8=208
case "$SH_I" in
  0) FLOOR=$FLOOR_ASSERTIONS; MODE="unsharded" ;;
  *) _fv="FLOOR_SHARD_$SH_I"; FLOOR=${!_fv}; MODE="shard $SH_I/$SHARD_ARITY" ;;
esac
# PRINTED ON EVERY RUN, green or red: a RED run prints no PASS line, so without this the floor-graded
# count of a shard that is red at BASE is readable nowhere, and AC1's identity cannot be observed.
echo "  ($n assertions executed in $MODE against a floor of $FLOOR)"
[ "$n" -ge "$FLOOR" ] || { echo "FAIL executed $n assertions in $MODE against a floor of $FLOOR — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
# WHAT A GREEN SHARD LEG IS EVIDENCE ABOUT: its own region, and nothing else. No shard alone is
# this suite, and the whole-suite claim lives only in a run with no `--shard` argument. That every
# index 1..8 is declared, each once, is the shard join `run-selftests.sh --check` carries.
#
# ONE CONTROL LOSES ITS MEANING WITHOUT FAILING when this file is split, and it is named here
# because no gate sees it: a "the tree is still clean after N mutations" control is a control only
# if those N mutations ran in the same process. Split away from them it degrades into a duplicate
# of the opening control — still green, and no longer evidence. Since TOOL-aBatchedArm-3 S6 its
# block declares the cycle count and the control asserts MUT against it, so the split is a red.


# ---- TOOL-dRetiredFork-9 S3: the BATCHED C21 join agrees with the per-file loop -------------------
# The absorption replaced 2 greps PER FILE with 2 greps and one awk for the whole population — 176
# processes to 3 over this corpus's 88 build READMEs. A speed-up that changes a verdict is not an
# optimisation, so the two are run over one fixture and their answers compared.
#
# The fixture carries all four shapes on purpose: well-formed, missing-open, missing-close, and
# DUPLICATED — because the check's own contract is EXACTLY ONE pair, and a join that merely tested
# presence would pass the duplicate.
c21_fixture=$(mktemp -d)
mkdir -p "$c21_fixture/ok" "$c21_fixture/noopen" "$c21_fixture/noclose" "$c21_fixture/dup"
printf '<!-- gen:build-units -->\n<!-- /gen:build-units -->\n' > "$c21_fixture/ok/README.md"
printf '<!-- /gen:build-units -->\n'                            > "$c21_fixture/noopen/README.md"
printf '<!-- gen:build-units -->\n'                             > "$c21_fixture/noclose/README.md"
printf '<!-- gen:build-units -->\n<!-- gen:build-units -->\n<!-- /gen:build-units -->\n' > "$c21_fixture/dup/README.md"
c21_files="$c21_fixture/ok/README.md $c21_fixture/noopen/README.md $c21_fixture/noclose/README.md $c21_fixture/dup/README.md"

# the RETIRED per-file loop, kept here as the oracle
c21_loop=""
for f in $c21_files; do
  o=$(grep -cxF -- '<!-- gen:build-units -->' "$f" 2>/dev/null || true)
  c=$(grep -cxF -- '<!-- /gen:build-units -->' "$f" 2>/dev/null || true)
  [ "${o:-0}" = 1 ] && [ "${c:-0}" = 1 ] && continue
  c21_loop="$c21_loop $f"
done

# the SHIPPED batched join, character for character
c21_batched=$(grep -cxF -- '<!-- gen:build-units -->' /dev/null $c21_files 2>/dev/null \
  | awk -F: -v closes="$(grep -cxF -- '<!-- /gen:build-units -->' /dev/null $c21_files 2>/dev/null)" '
      BEGIN { n = split(closes, L, "\n")
              for (i = 1; i <= n; i++) { p = L[i]; sub(/:[0-9]*$/, "", p)
                                         c = L[i]; sub(/^.*:/, "", c); CL[p] = c } }
      $0 !~ /^\/dev\/null:/ {
        path = $0; sub(/:[0-9]*$/, "", path)
        open = $0; sub(/^.*:/, "", open)
        if (open != 1 || CL[path] != 1) printf " %s", path
      }')

n=$((n+1))
if [ "$c21_loop" = "$c21_batched" ]; then
  echo "ok   C21: the batched join and the per-file loop return the same verdict"
else
  echo "FAIL C21: batched [$c21_batched] != per-file [$c21_loop]"; st=1
fi
# ANTI-VACUITY: the fixture must actually catch something, or the equality above is two empties.
n=$((n+1))
case "$c21_batched" in *noopen*|*noclose*|*dup*) echo "ok   C21: the fixture is non-vacuous" ;;
  *) echo "FAIL C21: the fixture caught nothing, so the equality proves nothing"; st=1 ;; esac
rm -rf "$c21_fixture"

[ "$SH_I" = 0 ] || echo "  (this leg ran $MODE only; the other $((SHARD_ARITY - 1)) regions were NOT exercised here)"
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
