#!/usr/bin/env bash
# check-pass-order.test.sh - arms for the pass-order history leg. TOOL-dBriefedPass-3.
#
# EVERY ARM DRIVES A REAL FIXTURE REPOSITORY with real commits, because the whole subject of the leg
# is COMMIT ORDER and a fixture that fakes the history proves nothing about a check that reads it.
# The two arms that matter are a matched pair: the same build, once with the spec commit BEFORE the
# build commit and once after. An arm for the refusal alone would not distinguish a leg that reds
# correctly from one that reds on everything.
# NO KIT_REL SWEEP IN THIS FILE, DELIBERATELY. Every path below is INSIDE the fixture tree this
# suite builds with `mkdir -p tools/unattended`, so `tools/` here is the FIXTURE's own layout
# and not gov's install prefix -- a fixture value, not a path to derive. Sweeping it broke 14
# of 19 arms: the `.unattended.conf` heredoc is `<<'CONF'`, which is QUOTED, so the config got
# the four literal bytes `$KIT_REL` and the generated-index claim pointed at nothing. This
# suite is not on the bar, so nothing would have reported it.
set -u
st=0; n=0
SCRIPT="$(cd "$(dirname "$0")" && pwd)/check-pass-order.sh"
KIT="$(cd "$(dirname "$0")" && pwd)"
[ -f "$SCRIPT" ] || { echo "FAIL cannot find check-pass-order.sh beside this test"; exit 2; }

same() { n=$((n+1)); if [ "$2" = "$3" ]; then echo "ok   $1"; else echo "FAIL $1 -- got '$2' want '$3'"; st=1; fi }
has()  { n=$((n+1)); case "$2" in *"$3"*) echo "ok   $1" ;; *) echo "FAIL $1 -- output did not carry '$3'"; st=1 ;; esac }
hasnt(){ n=$((n+1)); case "$2" in *"$3"*) echo "FAIL $1 -- output carried '$3' and must not"; st=1 ;; *) echo "ok   $1" ;; esac }

# ---------------------------------------------------------------------------------------------
# THE FIXTURE. One build, one unit, and the ORDER of two commits is the only thing that varies.
# `order` is the argument: `spec-first` or `build-first`.
mkfixture() { # run-state-mode · staging-order -> prints the fixture root
  local RUNMODE="$1" ord="$2" T
  T=$(mktemp -d) || exit 2
  ( cd "$T" || exit 2
    git init -q .
    git config user.email t@t; git config user.name t; git config commit.gpgsign false
    mkdir -p tools/unattended memory/builds/tOrder/spec
    cp "$KIT/lib-unattended.sh" tools/unattended/ 2>/dev/null || true
    cp "$KIT/unattended.sh"     tools/unattended/
    cp "$KIT/check-pass-order.sh" tools/unattended/
    cat > .unattended.conf <<'CONF'
MEMORY_ROOT=memory
PASS_ORDER_CUTOFF="2026-01-01"
GENERATED_INDEXES="memory/LIVE.md:tools/memory-tree/gen_build_index.py"
SHARED_RECORDS="memory/DECISIONS.md memory/backlog"
CONF
    cat > memory/builds/tOrder/README.md <<'RM'
---
slug: tOrder
node: t
opened: 2026-06-01
streams: tooling
roster: ARCH
ids: ARCH-tOrder-1
---
# tOrder
<!-- gen:build-index -->
<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [ARCH-tOrder-1 — the unit](spec/one.md) | 1 | 2 | CLOSED | rev-1 | 2026-06-01 |
<!-- /gen:build-units -->
<!-- /gen:build-index -->
RM
    git add -A >/dev/null; git commit -q -m "fixture base" --no-verify
    BASE=$(git rev-parse HEAD)
    # TOOL-aStagedLane-1 - `norun` and `badbase` skip or corrupt the run-state file. The leg used to
    # exclude those builds outright; it now derives their range from the build folder's own history,
    # so they are the population every arm below this line exercises.
    case "$RUNMODE" in
      norun|preanchor|preanchor-record|first-commit|parent-commit|no-closed) ;;
      badbase)
        printf '# tOrder\n<!-- run:generated -->\n<!-- /run:generated -->\n## Run facts\nbase: not-a-sha\n## Parked\n' > memory/builds/tOrder/RUN.md
        git add -A >/dev/null; git commit -q -m "run state" --no-verify ;;
      *)
        cat > memory/builds/tOrder/RUN.md <<RUNMD
# tOrder — run state
<!-- run:generated -->
<!-- /run:generated -->
## Run facts
base: $BASE
## Parked
RUNMD
        git add -A >/dev/null; git commit -q -m "run state" --no-verify ;;
    esac

    write_spec() {
      cat > memory/builds/tOrder/spec/one.md <<'SPEC'
# ARCH-tOrder-1 — the unit

**Status:** CLOSED · rev-1 · 2026-06-02 · node t · Tier-2 · base 0123abcd

## 2. Scope (IN)

- S1 a real scope item.

## 6. Acceptance criteria

- AC1 something observable.

## 7. Gates

- a gate.

## 8. Open questions

none
SPEC
    }
    # ---- TOOL-aStagedLane-1 stagings. Each builds the SAME violation at a different position
    # ---- relative to the build folder's first commit, which is what the derived range hangs on.
    if [ "$ord" = "no-closed" ]; then
      # AC17 - a build whose units region carries no CLOSED row contributes nothing.
      sed -i 's/ CLOSED / OPEN /' memory/builds/tOrder/README.md
      write_spec
      git add -A >/dev/null; git commit -q -m "spec ARCH-tOrder-1 authored" --no-verify
    elif [ "$ord" = "preanchor" ] || [ "$ord" = "preanchor-record" ] || [ "$ord" = "parent-commit" ]; then
      # The build folder does NOT exist yet at this point: it is created by the spec commit below.
      # So the product commit here is strictly earlier than the folder's first commit, which is the
      # flagrant case an anchored range cannot see. `preanchor-record` makes the early commit touch
      # ONLY a shared record, which must NOT be reported.
      # THE FOLDER MUST NEVER HAVE EXISTED. `rev-list HEAD -- <dir>` reaches the ORIGINAL creation
      # commit, so deleting and recreating the folder leaves its first commit back at the fixture
      # base and the violation lands inside the derived range after all — the arm would then pass
      # while testing nothing. Rewriting the base commit without the folder is the only staging that
      # actually puts the product commit before the folder's history begins.
      git rm -r -q --cached memory/builds/tOrder >/dev/null 2>&1 || true
      rm -rf memory/builds/tOrder
      git add -A >/dev/null; git commit -q -m "drop the build folder" --no-verify
      git checkout -q --orphan clean-base
      git rm -r -q --cached . >/dev/null 2>&1 || true
      git add tools .unattended.conf >/dev/null 2>&1
      git commit -q -m "fixture base without the build folder" --no-verify
      git branch -q -D master main 2>/dev/null || true
      if [ "$ord" = "preanchor-record" ]; then
        mkdir -p memory/backlog; printf 'a row\n' > memory/backlog/ARCH.md; git add -A >/dev/null
        git commit -q -m "backlog(ARCH-tOrder-1): open the row" --no-verify
      else
        printf 'the product\n' > tools/product.sh; git add -A >/dev/null
        git commit -q -m "ARCH-tOrder-1: build the thing" --no-verify
      fi
      # `preanchor` puts FILLER between the product commit and the folder, so the violation sits
      # strictly earlier than `<first>^`; `parent-commit` leaves it exactly AT `<first>^`. Two
      # positions, two arms — otherwise both would test the same commit and one would prove nothing.
      if [ "$ord" = "preanchor" ]; then
        printf 'filler
' > tools/filler.sh; git add -A >/dev/null
        git commit -q -m "unrelated filler" --no-verify
      fi
      mkdir -p memory/builds/tOrder/spec
      cat > memory/builds/tOrder/README.md <<'RM2'
---
slug: tOrder
node: t
opened: 2026-06-01
streams: tooling
roster: ARCH
ids: ARCH-tOrder-1
---
# tOrder
<!-- gen:build-index -->
<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [ARCH-tOrder-1 — the unit](spec/one.md) | 1 | 2 | CLOSED | rev-1 | 2026-06-01 |
<!-- /gen:build-units -->
<!-- /gen:build-index -->
RM2
      write_spec
      git add -A >/dev/null; git commit -q -m "spec ARCH-tOrder-1 authored" --no-verify
    elif [ "$ord" = "first-commit" ]; then
      # AC8 - the violating commit IS the build folder's own first commit: it creates the folder and
      # writes product code in one act. An exclusive range anchor drops exactly this commit.
      git rm -r -q --cached memory/builds/tOrder >/dev/null 2>&1 || true
      rm -rf memory/builds/tOrder
      git add -A >/dev/null; git commit -q -m "drop the build folder" --no-verify
      mkdir -p memory/builds/tOrder/spec
      cat > memory/builds/tOrder/README.md <<'RM3'
---
slug: tOrder
node: t
opened: 2026-06-01
streams: tooling
roster: ARCH
ids: ARCH-tOrder-1
---
# tOrder
<!-- gen:build-index -->
<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [ARCH-tOrder-1 — the unit](spec/one.md) | 1 | 2 | CLOSED | rev-1 | 2026-06-01 |
<!-- /gen:build-units -->
<!-- /gen:build-index -->
RM3
      printf 'the product\n' > tools/product.sh; git add -A >/dev/null
      git commit -q -m "ARCH-tOrder-1: build the thing" --no-verify
      write_spec
      git add -A >/dev/null; git commit -q -m "spec ARCH-tOrder-1 written afterwards" --no-verify
    elif [ "$ord" = "spec-first" ]; then
      # THE SPEC COMMIT WRITES WHAT A REAL SPEC PASS WRITES, and this is load-bearing rather than
      # realism for its own sake. A spec pass regenerates the index, touches the build README and the
      # run-state file, and its SUBJECT names the unit id. With the exclusion set to `spec/` and
      # `reviews/` alone, all of those sit outside it, so this commit won the build-commit selection
      # and the leg graded ITS parent — reporting "the spec was written after the code" about a run
      # that did the opposite. A fixture whose spec commit touched only `spec/` could not see it.
      write_spec
      printf 'regenerated index
' > memory/LIVE.md
      git add -A >/dev/null; git commit -q -m "spec ARCH-tOrder-1 authored" --no-verify
      printf 'the product\n' > tools/product.sh; git add -A >/dev/null
      git commit -q -m "ARCH-tOrder-1: build the thing" --no-verify
    else
      printf 'the product\n' > tools/product.sh; git add -A >/dev/null
      git commit -q -m "ARCH-tOrder-1: build the thing" --no-verify
      write_spec
      printf 'regenerated index
' > memory/LIVE.md
      git add -A >/dev/null; git commit -q -m "spec ARCH-tOrder-1 written afterwards" --no-verify
    fi
  ) >/dev/null 2>&1
  printf '%s' "$T"
}

# ---- AC6: THE PASSING CASE, first. A refusal with no observed passing case is a gate that cannot be
# ---- satisfied, and it is the arm most often missing.
T=$(mkfixture run spec-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "spec BEFORE build: the leg is green" "$rc" "0"
has  "spec BEFORE build: the unit was graded" "$o" "graded 1 closed unit"
hasnt "spec BEFORE build: nothing is reported as a violation" "$o" "FAILED"
rm -rf "$T"

# ---- AC5: THE FAILING CASE, OBSERVED. This is the arm the whole leg exists for, and until it has
# ---- been seen RED the leg is an assertion about nothing.
T=$(mkfixture run build-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "build BEFORE spec: the leg REDS" "$rc" "1"
has  "build BEFORE spec: the message names the unit" "$o" "ARCH-tOrder-1"
has  "build BEFORE spec: the message says what happened" "$o" "BUILT before a conforming spec"
has  "build BEFORE spec: the unit was graded, not skipped" "$o" "graded 1 closed unit"
rm -rf "$T"

# ---- AC7: THE CUTOFF, both directions. Blank ANNOUNCES rather than passing silently; set, the
# ---- liveness line names all three populations this leg walks.
T=$(mkfixture run build-first)
( cd "$T" && sed -i 's/^PASS_ORDER_CUTOFF=.*/PASS_ORDER_CUTOFF=""/' .unattended.conf )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "cutoff BLANK: exits 0 over a tree that would otherwise RED" "$rc" "0"
has  "cutoff BLANK: the skip ANNOUNCES itself" "$o" "the ORDER term is OFF"
# The grandfathering direction: a build OPENED before the cutoff is skipped and counted.
( cd "$T" && sed -i 's/^PASS_ORDER_CUTOFF=.*/PASS_ORDER_CUTOFF="2026-12-01"/' .unattended.conf )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "cutoff AFTER the build opened: grandfathered, exits 0" "$rc" "0"
has  "cutoff AFTER: the skipped build is COUNTED, not silent" "$o" "1 build(s) skipped by the"
rm -rf "$T"

# ---- THE HOSTILE CONF, both shapes, and this is the arm the fix exists for. `$CONF` is a TRACKED
# ---- file the graded run commits, so a leg that SOURCES it lets its own subject end or hijack it.
# ---- Both shapes were reproduced against this leg before the import was hardened: `exit 0` gave rc 0
# ---- with zero output, byte-indistinguishable from a clean tree, and `trap` was worse — the leg
# ---- PRINTED its own FAILED line and still exited 0. Both siblings met these one incident at a time.
T=$(mkfixture run build-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "hostile-conf control: the fixture reds BEFORE the conf is touched" "$rc" "1"
( cd "$T" && printf '
exit 0
' >> .unattended.conf )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
n=$((n+1)); [ "$rc" != 0 ] && echo "ok   hostile conf: an appended \`exit 0\` cannot end the leg at 0"   || { echo "FAIL an appended exit 0 ended the leg at 0 -- the subject silenced its own gate"; st=1; }
rm -rf "$T"

# ---- THE VECTOR THE SPLICE MISSED, and the reason the import assigns an ALLOW-LIST rather than the
# ---- sibling's uppercase glob. This leg sets DRIVER above the import — the path it eval's its
# ---- classifier out of — so one tracked conf line redirected it at an attacker-chosen file. The
# ---- sibling is safe with a glob because it sets nothing it cares about above its own import; a
# ---- block copied verbatim between two scripts is not the same block.
T=$(mkfixture run build-first)
( cd "$T" && printf 'echo OWNED; plan_state() { echo READY; }
' > tools/unattended/evil.sh    && printf '
DRIVER="tools/unattended/evil.sh"
' >> .unattended.conf )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
n=$((n+1)); case "$o" in *OWNED*) echo "FAIL a conf line redirected DRIVER, so the leg eval'd a file the graded run chose"; st=1 ;; *) echo "ok   hostile conf: DRIVER is not assignable from the conf" ;; esac
same "hostile conf: the honest verdict survives the DRIVER line" "$rc" "1"
rm -rf "$T"

T=$(mkfixture run build-first)
( cd "$T" && printf "
trap 'exit 0' EXIT
" >> .unattended.conf )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
n=$((n+1)); [ "$rc" != 0 ] && echo "ok   hostile conf: an appended EXIT trap cannot force rc 0"   || { echo "FAIL an appended EXIT trap forced rc 0 -- the worse shape, where the leg prints FAILED and exits green"; st=1; }
rm -rf "$T"

# ---- THE LIVENESS PROBE. A leg whose classifier cannot be sliced must SAY so and exit 2, never
# ---- report a clean bill. Staged by breaking the driver's function header in a copy.
T=$(mkfixture run spec-first)
( cd "$T" && sed -i 's/^plan_state()/plan_state_renamed()/' tools/unattended/unattended.sh )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "unsliceable classifier: exits 2 rather than reporting clean" "$rc" "2"
has  "unsliceable classifier: it says which predicate it lost" "$o" "plan_state"
rm -rf "$T"

# ---- THE WHOLE-TOKEN ID JOIN. `ARCH-tOrder-1` must not match a commit naming `ARCH-tOrder-11`.
# ---- Every id ending in a 1-up sequence is a prefix of nine others, and an unanchored match would
# ---- attribute the wrong commit -- which on this leg means grading the wrong parent.
T=$(mkfixture run spec-first)
( cd "$T" && printf 'x\n' > tools/other.sh && git add -A >/dev/null \
    && git commit -q -m "ARCH-tOrder-11: a different unit entirely" --no-verify )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "id join is whole-token: a -11 commit does not disturb -1's verdict" "$rc" "0"
rm -rf "$T"

# =============================================================== TOOL-aStagedLane-1 — THE WIDENING
# Every arm below drives a build with NO usable run-state file, which is the population this unit
# added. The matched pair is kept: the same violation observed RED, and the conforming order green.

# ---- AC1: a run-state-free build whose unit was built before its spec REDS. Observed before the
# ---- code that greens it, per the rule that a gate never seen failing is an assertion about nothing.
T=$(mkfixture norun build-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "no RUN.md, build BEFORE spec: the leg REDS" "$rc" "1"
has  "no RUN.md, build BEFORE spec: the unit is named" "$o" "ARCH-tOrder-1"
has  "no RUN.md: the build was GRADED, not skipped" "$o" "graded 1 closed unit"
rm -rf "$T"

# ---- AC2: the same build, spec first, is green AND graded. A refusal with no observed passing case
# ---- is a gate that cannot be satisfied.
T=$(mkfixture norun spec-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "no RUN.md, spec BEFORE build: the leg is green" "$rc" "0"
has  "no RUN.md, spec BEFORE build: the unit was graded" "$o" "graded 1 closed unit"
rm -rf "$T"

# ---- AC3/AC11: the liveness line names the new count and no longer carries the retired one. A field
# ---- with no reachable increment site is a dead probe whatever value it prints.
T=$(mkfixture norun spec-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1)
has   "liveness: the run-state-free population is counted by name" "$o" "graded with no run-state file"
hasnt "liveness: the retired skip count is GONE, not pinned at zero" "$o" "with no pinned run BASE"
has   "liveness: the pre-anchor population is counted" "$o" "pre-anchor violation"
has   "liveness: the waiver population is counted" "$o" "waived by"
rm -rf "$T"

# ---- AC9: a RUN.md whose `base:` is garbage falls back to the folder anchor rather than exempting
# ---- the build. Otherwise a build with a broken run-state file is MORE exempt than one with none.
T=$(mkfixture badbase build-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "garbage RUN.md base: still graded, and the violation still REDS" "$rc" "1"
has  "garbage RUN.md base: graded through the folder anchor" "$o" "graded 1 closed unit"
rm -rf "$T"

# ---- AC7: the flagrant case. Product code lands BEFORE the build folder exists, so it sits outside
# ---- any folder-derived range. It must RED, not fall into the unbuilt-in-range tally this file's own
# ---- liveness block warns is not benign.
T=$(mkfixture preanchor preanchor)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "pre-anchor build commit: the leg REDS" "$rc" "1"
has  "pre-anchor: the message says the folder did not exist yet" "$o" "BEFORE this build's folder existed"
has  "pre-anchor: it is counted as its own population" "$o" "1 pre-anchor violation"
rm -rf "$T"

# ---- AC12: the false-positive arm, and the reason the pre-anchor probe reuses the WHOLE build-commit
# ---- predicate. A backlog row naming the unit ordinarily lands before the build folder exists.
T=$(mkfixture preanchor-record preanchor-record)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "pre-anchor RECORD-only commit: green, because the exclusion still applies" "$rc" "0"
has  "pre-anchor record-only: reported as unbuilt-in-range, not as a violation" "$o" "unbuilt-in-range"
rm -rf "$T"

# ---- AC8: the violating commit IS the build folder's first commit. `rev-list A..HEAD` excludes A, so
# ---- an exclusive anchor drops exactly this one — the boundary the unit exists to police.
T=$(mkfixture first-commit first-commit)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "violation AT the folder's first commit: the leg REDS" "$rc" "1"
rm -rf "$T"

# ---- AC16: one commit earlier — the immediate PARENT of the folder's first commit. S2's anchor is
# ---- `<first>^`, so a pre-anchor window described as "strictly before the anchor" would exclude it
# ---- twice and leave a one-commit hole. Both ends of the range now have an arm.
T=$(mkfixture parent-commit parent-commit)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "violation at the PARENT of the folder's first commit: the leg REDS" "$rc" "1"
rm -rf "$T"

# ---- AC17: a build with no CLOSED unit contributes nothing and must not pass silently.
T=$(mkfixture no-closed no-closed)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "no CLOSED unit: exits 0" "$rc" "0"
has  "no CLOSED unit: graded nothing, and says so" "$o" "graded 0 closed unit"
rm -rf "$T"

# ---- AC14/AC15: the waiver registry. A waived violation is green and COUNTED; a row matching nothing
# ---- REDS, because an exemption that has outlived its reason widens the surface it was written to
# ---- narrow. The control comes first: the same fixture reds before the registry exists.
T=$(mkfixture norun build-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "waiver control: the fixture REDS with no registry" "$rc" "1"
# COMMITTED, because the registry is read from the graded commit. An arm leaving it untracked
# would exercise the uncommitted path H3 closed, and would pass either way.
( cd "$T" && mkdir -p memory/project && printf 'ARCH-tOrder-1\tthe control arm waives it\n' > memory/project/pass-order-waiver.txt \
    && git add -A >/dev/null && git commit -q -m 'waive it' --no-verify )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "waived violation: green" "$rc" "0"
has  "waived violation: COUNTED, not silent" "$o" "1 waived by"
# TWO ROWS, and this arm exists because a ONE-row registry cannot tell a working membership test from
# one that only ever matches the last line. The shipped registry has two rows and waived NOTHING
# until the id list was flattened, while the single-row arm above passed throughout — the instance
# was covered and the class was not.
( cd "$T" && printf 'ARCH-tOrder-2\ta row BEFORE the real one\nARCH-tOrder-1\tthe unit that actually violates\n' > memory/project/pass-order-waiver.txt \
    && git add -A >/dev/null && git commit -q -m 'two rows' --no-verify )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
hasnt "MULTI-row waiver: a row that is not the last still waives its unit" "$o" "BUILT at"
has   "MULTI-row waiver: the stale sibling is still named" "$o" "ARCH-tOrder-2"
( cd "$T" && printf 'ARCH-tOrder-99\tnothing matches this\n' > memory/project/pass-order-waiver.txt \
    && git add -A >/dev/null && git commit -q -m 'stale row' --no-verify )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "STALE waiver row: REDS" "$rc" "1"
has  "stale waiver: names the row that matched nothing" "$o" "ARCH-tOrder-99"
rm -rf "$T"

# ---- AC13/S2f: `--preview` prints what it finds and sets NO exit status, which is what lets a
# ---- candidate predicate be run over a real tree before it is wired.
T=$(mkfixture norun build-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh --preview 2>&1); rc=$?
same "--preview: exit 0 over a tree that REDS without it" "$rc" "0"
has  "--preview: the violation is still printed" "$o" "ARCH-tOrder-1"
has  "--preview: it says the status is not set" "$o" "exit status is NOT set"
rm -rf "$T"

# ---- AC13: the pre-anchor probe's cap, exercised by DECLARING a cap of 1 rather than by building a
# ---- 400-commit fixture. The conf key is the seam that makes this arm affordable; a probe that gave
# ---- up and a probe that found nothing print the same thing without the count.
# The RECORD-only fixture, not the violating one: with a cap of 1 the probe's first look at a
# violating fixture MATCHES, so it returns a hit and never truncates — the arm would then assert on a
# path it does not take. Here the first look legitimately misses, which is the only way a probe can
# reach its cap. Written the other way first, and it failed honestly.
T=$(mkfixture preanchor-record preanchor-record)
( cd "$T" && printf '
PASS_ORDER_PREANCHOR_CAP="1"
' >> .unattended.conf )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
has  "pre-anchor cap: the truncation is COUNTED" "$o" "1 probe(s) truncated"
has  "pre-anchor cap: the cap it stopped at is named" "$o" "1-commit cap"
same "pre-anchor cap: a truncated probe does not invent a violation" "$rc" "0"
rm -rf "$T"

# ---- S6: the cutoff is read from the COMMIT, so editing the working copy cannot exempt a build.
# ---- Control first — the same fixture reds before the working tree is touched.
T=$(mkfixture norun build-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "cutoff control: reds before the working copy is edited" "$rc" "1"
( cd "$T" && sed -i 's/^opened: .*/opened: 2020-01-01/' memory/builds/tOrder/README.md )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "working-tree opened: back-date does NOT exempt the build" "$rc" "1"
# AC10 - the COMMITTED value still grandfathers, which is the narrowing this unit makes and not a
# removal. The header says so; this arm proves the residual is real rather than theoretical.
( cd "$T" && git add -A >/dev/null && git commit -q -m "back-date the build" --no-verify )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "COMMITTED opened: back-date still exempts — the declared residual" "$rc" "0"
rm -rf "$T"

# ============================================ THE CLOSING REVIEW'S FINDINGS — B1, H1, H2, H3
# Every arm below covers a defect the closing diff review found in code this build had already
# committed and self-tested. They share one shape: a read that should come from the graded COMMIT was
# coming from the working tree, or a bound was tested one step too early.

# ---- B1: an UNTRACKED RUN.md must not change the verdict. S6 moved the `opened:` read to HEAD and
# ---- left `base:` on the filesystem, so dropping an untracked run-state file naming HEAD emptied the
# ---- range and greened the leg. Control first, then the bypass attempt.
T=$(mkfixture norun build-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "B1 control: the fixture REDS before the bypass is attempted" "$rc" "1"
( cd "$T" && mkdir -p memory/builds/tOrder && printf '# tOrder\nbase: %s\n' "$(cd "$T" && git rev-parse HEAD)" > memory/builds/tOrder/RUN.md )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "B1: an UNTRACKED RUN.md does not exempt the build" "$rc" "1"
rm -rf "$T"

# ---- B1, second read: an UNCOMMITTED deletion of a CLOSED row must not drop the unit from grading.
# ---- That read selects the POPULATION, so it is earlier and worse than the range read.
T=$(mkfixture norun build-first)
( cd "$T" && sed -i 's/ CLOSED / OPEN /' memory/builds/tOrder/README.md )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "B1: an UNCOMMITTED CLOSED-row edit does not drop the unit" "$rc" "1"
has  "B1: the unit is still graded from the committed region" "$o" "graded 1 closed unit"
rm -rf "$T"

# ---- H3: an UNCOMMITTED waiver must not waive. Otherwise the waiver works for whoever wrote it and
# ---- its stale-row red can never fire for anybody else, because the file is not in the pushed tree.
T=$(mkfixture norun build-first)
( cd "$T" && mkdir -p memory/project && printf 'ARCH-tOrder-1\tnever committed\n' > memory/project/pass-order-waiver.txt )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "H3: an UNCOMMITTED waiver does not waive" "$rc" "1"
rm -rf "$T"

# ---- H1: the violation sits AT the anchor with a cap SMALLER than the window behind it. `--reverse`
# ---- puts the anchor LAST, so testing the cap at the top of the loop consumed the anchor as the
# ---- truncation sentinel and the probe could never grade the one commit it exists to reach.
T=$(mkfixture parent-commit parent-commit)
( cd "$T" && printf '\nPASS_ORDER_PREANCHOR_CAP="1"\n' >> .unattended.conf && git add -A >/dev/null && git commit -q -m 'cap 1' --no-verify )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "H1: the violation AT the anchor is graded, not eaten by the cap" "$rc" "1"
has  "H1: it is reported as a pre-anchor violation" "$o" "1 pre-anchor violation"
rm -rf "$T"

# ---- H2: the cap is validated before it reaches arithmetic. A tracked conf the graded run commits
# ---- reached `$(( ))` unchecked, which is code execution in this leg's own shell, and a non-numeric
# ---- value disabled the whole pre-anchor class while reporting zero truncations.
T=$(mkfixture preanchor preanchor)
( cd "$T" && printf '\nPASS_ORDER_PREANCHOR_CAP="not-a-number"\n' >> .unattended.conf )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "H2: a non-numeric cap is a REFUSAL, not a silent green" "$rc" "2"
has  "H2: it says what the value must be" "$o" "must be a non-negative integer"
( cd "$T" && sed -i 's/^PASS_ORDER_PREANCHOR_CAP=.*/PASS_ORDER_PREANCHOR_CAP="1+1"/' .unattended.conf )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "H2: an arithmetic EXPRESSION is refused rather than evaluated" "$rc" "2"
rm -rf "$T"

echo "--- $n arms, exit $st"
exit $st
