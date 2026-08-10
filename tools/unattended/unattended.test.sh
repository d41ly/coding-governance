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
trap 'rm -rf "$TMP"' EXIT
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
# tEmpty exists ON MAIN with an EMPTY mandate block, because check 7 branch 1 asks about the BASE.
# Producing that state by editing on the unit branch is impossible by construction: the branch is
# exactly what the BASE is not.
readme tEmpty
runmd tEmpty ""
git add -A && git commit -q -m base --no-verify
git checkout -q -b unit
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

# ---- check 3, both branches. Unresolvable default branch (no override, no origin) and the run
# ---- sitting ON the default branch. The first run also arms check 16, because a default branch
# ---- that cannot be named is also a merge-base that cannot be resolved — one state, two honest
# ---- refusals, and each is asserted by its own text.
reset_tree
out=$(env -u GOV_DEFAULT_BRANCH bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "cannot resolve the default branch (set GOV_DEFAULT_BRANCH) — refusing rather than assuming one"

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

reset_tree; mkconf "true --fix"
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "WIRING_CHECK declares a REPAIRING mode, and preflight delegates to a check, never a fix"

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

# ---- check 6: the run-state file exists on the unit branch but NOT at the pinned BASE. This is the
# ---- self-authored case in its purest form — the run created the file that holds its own mandate.
reset_tree
readme tNew; runmd tNew "$MANDATE"
git add -A && git commit -q -m new --no-verify
out=$(run --preflight tNew --keepalive-id k1)
hit "$out" "no run-state file at the pinned BASE, so the mandate cannot be reachable — the owner authors and commits it BEFORE the run starts"

# ---- check 7 branch 1: the file is reachable but its mandate block is EMPTY at the BASE. Reaching
# ---- the file is not reaching the mandate, and a run that filled an empty block authored it.
reset_tree
out=$(run --preflight tEmpty --keepalive-id k1)
hit "$out" "the mandate block is absent or empty at the pinned BASE — a mandate introduced after the branch point is one the run could have written, and grants nothing"

# ---- check 7 branch 2: present at BASE, EDITED in the working copy. Same comparison, other side.
reset_tree
runmd tRun "$MANDATE and also to force-push, which the owner never wrote."
out=$(run --preflight tRun --keepalive-id k1)
hit "$out" "the mandate block differs from the one at the pinned BASE — the run edited its own authorization"

# ---- check 8: the keepalive id is the AGENT's half of the split. No script can produce it, so its
# ---- absence is a refusal rather than a default.
reset_tree
out=$(run --preflight tRun)
hit "$out" "no --keepalive-id was supplied — scheduling is the AGENT's half of the split and only the agent can do it; the driver records the id it is handed"

# ---- check 15: a build folder with no run-state file at all.
reset_tree; readme tBare; fixture
out=$(run --preflight tBare --keepalive-id k1)
hit "$out" "no run-state file to assert against — preflight asserts a mandate, it does not create one"
git reset -q --hard HEAD~1; git clean -qfd

# ---- check 16: the default branch NAMES something that does not exist, so the merge-base cannot be
# ---- resolved. The refusal is the point: falling back to HEAD would make the mandate comparison
# ---- pass by construction, because HEAD holds whatever the run just wrote.
reset_tree
out=$(GOV_DEFAULT_BRANCH=nosuchbranch bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1)
hit "$out" "cannot resolve a merge-base against the default branch — refusing rather than pinning HEAD, which would make the mandate check pass by construction"

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

# ---- check 14: an unknown argument. The verbs are a closed set.
out=$(run --frobnicate tRun)
hit "$out" "unknown argument; the verbs are --preflight, --status, --resume and --close: --frobnicate"

# ---- SOURCE-level: the driver must not grow a python dependency. Every other kit here carries the
# ---- launcher resolver inline because it needs python; this one does not, and a `python` appearing
# ---- in it later would be an un-resolved launcher rather than a resolved one.
np=$(grep -nE '(^|[^-[:alnum:]])(python3?|py) ' "$SCRIPT" | grep -v '^[0-9]*:#' || true)
n=$((n+1)); [ -z "$np" ] || { echo "FAIL the driver invokes a python launcher without the resolver: $np"; st=1; }

# ---- SOURCE-level: no verb may reach the repairing wiring mode, whatever the conf says. The runtime
# ---- arm above covers a project that DECLARES `--fix`; this covers the driver calling it directly.
nf=$(grep -nE 'check-wiring[^"]*--fix' "$SCRIPT" | grep -v '^[0-9]*:#' || true)
n=$((n+1)); [ -z "$nf" ] || { echo "FAIL the driver reaches the repairing wiring mode directly: $nf"; st=1; }

[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
