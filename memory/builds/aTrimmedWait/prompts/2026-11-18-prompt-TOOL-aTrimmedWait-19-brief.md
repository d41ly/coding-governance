# Brief — aTrimmedWait: the hygiene suite's partition helper takes back main's name, so the landing's merge-loss check clears

**Serves:** research TOOL-aTrimmedWait-19

## The prompt

> Rename back (Recommended)

The owner's answer on 2026-11-18. `bash tools/push-main.sh` from the primary tree was refused before
any leg ran: the pre-push merge-loss check (TOOL-aMendedFleet-3) printed
`merge-losses: LOSS 01aad174 parent 2: tools/memory-tree/check-memory-hygiene.test.sh: extract_hs_lines`.
`TOOL-aTrimmedWait-12`'s reconcile merge dropped main's `extract_hs_lines` on the owner's ruling of
2026-11-16, which kept this branch's `derive_partition_lines` and its fixture arm. The check accepts
a `superseded:` line only in that merge's own message, and rewriting it would rewrite every later
commit, the owner's terminal commit of `.governance/policy.toml` among them. The check also clears a
loss whose definition the range tip carries, so the owner chose to rename this branch's helper back
to main's name.

## The brief

### Goal
`tools/memory-tree/check-memory-hygiene.test.sh` defines the partition helper as `extract_hs_lines`,
with this branch's body, so the tip carries the name the reconcile merge lost and the merge-loss
check over `origin/main..main` reads no loss.

### Items
1. Rename `derive_partition_lines` to `extract_hs_lines` at its definition and every call and FAIL
   text in the suite. The body, its argument form and every assertion stay as they are.
2. Re-render the codebase map for the renamed shell function and commit `memory/map/generated` with
   it.
3. The CLOSED specs and records that cite `derive_partition_lines` are history and stay as written;
   say how the spec-token checks treat a CLOSED spec citing a name the tree no longer holds, and
   meet whatever they require without editing those specs' substance.

### Acceptance
- `git grep -n derive_partition_lines -- tools/` prints nothing, and the suite defines
  `extract_hs_lines` once.
- `bash -n tools/memory-tree/check-memory-hygiene.test.sh` exits 0.
- The lexicon kit's `--merge-losses` over `origin/main..HEAD`, run as the pre-push hook runs it,
  reports no loss.

### Gates
The pre-push bar at the push, run by the main loop through `push-main.sh`. The hygiene suite's
partition arms are renamed, not changed, so no slow suite is owed; running one is the owner's call.

### Non-goals
- Any change to the helper's body, to what the arms compare, or to the floor.
- Editing a CLOSED spec's substance or rewriting any commit.
- A pass commit without its acceptance ledger at
  `memory/builds/aTrimmedWait/build/2026-11-18-build-TOOL-aTrimmedWait-19-1-acceptance-ledger.md`.
- An edit after the commit that sets the spec CLOSED: the status flip is the last change of the pass.

## Owner confirmation

> Rename back (Recommended)
