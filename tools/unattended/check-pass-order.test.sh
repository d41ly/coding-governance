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
mkfixture() { # order -> prints the fixture root
  local ord="$1" T
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
    cat > memory/builds/tOrder/RUN.md <<RUNMD
# tOrder — run state
<!-- run:generated -->
<!-- /run:generated -->
## Run facts
base: $BASE
## Parked
RUNMD
    git add -A >/dev/null; git commit -q -m "run state" --no-verify

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
    if [ "$1" = "spec-first" ]; then
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
T=$(mkfixture spec-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "spec BEFORE build: the leg is green" "$rc" "0"
has  "spec BEFORE build: the unit was graded" "$o" "graded 1 closed unit"
hasnt "spec BEFORE build: nothing is reported as a violation" "$o" "FAILED"
rm -rf "$T"

# ---- AC5: THE FAILING CASE, OBSERVED. This is the arm the whole leg exists for, and until it has
# ---- been seen RED the leg is an assertion about nothing.
T=$(mkfixture build-first)
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "build BEFORE spec: the leg REDS" "$rc" "1"
has  "build BEFORE spec: the message names the unit" "$o" "ARCH-tOrder-1"
has  "build BEFORE spec: the message says what happened" "$o" "BUILT before a conforming spec"
has  "build BEFORE spec: the unit was graded, not skipped" "$o" "graded 1 closed unit"
rm -rf "$T"

# ---- AC7: THE CUTOFF, both directions. Blank ANNOUNCES rather than passing silently; set, the
# ---- liveness line names all three populations this leg walks.
T=$(mkfixture build-first)
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
T=$(mkfixture build-first)
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
T=$(mkfixture build-first)
( cd "$T" && printf 'echo OWNED; plan_state() { echo READY; }
' > tools/unattended/evil.sh    && printf '
DRIVER="tools/unattended/evil.sh"
' >> .unattended.conf )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
n=$((n+1)); case "$o" in *OWNED*) echo "FAIL a conf line redirected DRIVER, so the leg eval'd a file the graded run chose"; st=1 ;; *) echo "ok   hostile conf: DRIVER is not assignable from the conf" ;; esac
same "hostile conf: the honest verdict survives the DRIVER line" "$rc" "1"
rm -rf "$T"

T=$(mkfixture build-first)
( cd "$T" && printf "
trap 'exit 0' EXIT
" >> .unattended.conf )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
n=$((n+1)); [ "$rc" != 0 ] && echo "ok   hostile conf: an appended EXIT trap cannot force rc 0"   || { echo "FAIL an appended EXIT trap forced rc 0 -- the worse shape, where the leg prints FAILED and exits green"; st=1; }
rm -rf "$T"

# ---- THE LIVENESS PROBE. A leg whose classifier cannot be sliced must SAY so and exit 2, never
# ---- report a clean bill. Staged by breaking the driver's function header in a copy.
T=$(mkfixture spec-first)
( cd "$T" && sed -i 's/^plan_state()/plan_state_renamed()/' tools/unattended/unattended.sh )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "unsliceable classifier: exits 2 rather than reporting clean" "$rc" "2"
has  "unsliceable classifier: it says which predicate it lost" "$o" "plan_state"
rm -rf "$T"

# ---- THE WHOLE-TOKEN ID JOIN. `ARCH-tOrder-1` must not match a commit naming `ARCH-tOrder-11`.
# ---- Every id ending in a 1-up sequence is a prefix of nine others, and an unanchored match would
# ---- attribute the wrong commit -- which on this leg means grading the wrong parent.
T=$(mkfixture spec-first)
( cd "$T" && printf 'x\n' > tools/other.sh && git add -A >/dev/null \
    && git commit -q -m "ARCH-tOrder-11: a different unit entirely" --no-verify )
o=$(cd "$T" && bash tools/unattended/check-pass-order.sh 2>&1); rc=$?
same "id join is whole-token: a -11 commit does not disturb -1's verdict" "$rc" "0"
rm -rf "$T"

echo "--- $n arms, exit $st"
exit $st
