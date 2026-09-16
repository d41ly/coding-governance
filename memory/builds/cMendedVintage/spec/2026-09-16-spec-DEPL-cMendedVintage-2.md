# DEPL-cMendedVintage-2 — a failed restore keeps its receipt row forward, and the order names the path

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |

<!-- /gen:spec-records -->

## 1. Goal

When a rollback cannot restore a path, `update --write` reverts that path's receipt row to its
pre-run values anyway and writes the result to disk, so the receipt claims a `sha256` the file does
not have and the next run classifies it against bytes that never came back. Revert the row only when
the file actually went back, and name the path that did not in the order.

## 2. Scope (IN)

- **S1** The four restore-failure branches inside the rollback path loop
  (`tools/govkit/govkit.py:7594`, `:7609`, `:7618` and the containment refusal at `:7588`) record the
  path they could not restore in an `unrestored` list before they `continue`. Observed by AC1.
- **S2** The `ROLLBACK_FIELDS` revert and the `withdrawn_rows` removal at `tools/govkit/govkit.py:7659`
  run only when every path of that snapshot entry that this run WROTE is in `restored`. Observed by
  AC2 and AC3.
- **S3** The rollback order gains a fourth block naming every unrestored path, and its lead sentence
  stops claiming that every path below was put back. Observed by AC4.
- **S4** That fourth block states the half-restored case explicitly: when `git checkout-index` is what
  failed, the index was already reverted, so the row's `sha256` matches the worktree and its `oid`
  does not. Observed by AC4.

## 3. Non-goals (OUT)

- No new refusal. Each of the four branches already calls `r.fail` with its own message; this unit
  adds a list append beside each and changes no message, so the deployer's refusal-branch population
  is unchanged.
- No retry, no second restore attempt, no fallback write. A restore that git refused is an operator
  problem, and a tool that keeps trying is how a part-restored tree becomes an unreadable one.
- No change to the `origin == "landed"` branch at `tools/govkit/govkit.py:7627`, which already gates
  its own row removal on the same predicate. This unit lifts that idea one level out; it does not
  rewrite that branch.
- Nothing about WHICH kits reach the restore loop. That is the unit before this one.

### Edges

- **consumes-from** `DEPL-cMendedVintage-1` — after that unit the green-to-red arm has two exits and
  a kit diverted by a declined render never walks the restore loop at all. This unit's gating grades
  only the kits that do walk it, and would otherwise be written as though every rolled-back kit
  passed through here.
- **hands-off** external — nothing in this build consumes this unit's output.

## 4. Design

### The defect, read from source

`tools/govkit/govkit.py:7566` opens `for s in [x for x in snap_rows if x["kit"] == eid]:` and then
`for p in s["paths"]:`. Inside the inner loop, four outcomes end in `continue`: a containment refusal,
a `git rm --cached` that would not unstage, a `git update-index` that would not take the entry, and a
`git checkout-index` that could not write the worktree file. Each appends nothing to `restored`.

Control then leaves the inner loop and reaches, unconditionally, the block that copies
`s["fields"]` back onto `s["row"]` for every key in `ROLLBACK_FIELDS` and drops the row from
`withdrawn_rows`. The receipt is serialised at `tools/govkit/govkit.py:7827`. So the file on disk
holds what this run wrote while its row claims the pre-run `sha256`, `oid`, `commit` and `version` —
which is the exact disagreement `DEPL-dCarriedReceipt-7` and `-8` were built to prevent, arriving
through the failure path instead of the success path.

### The gate

```
_left = [p for p in s["paths"] if p in written_paths and p not in restored]
if _left:
    <skip the revert and the withdrawn_rows removal; the row stays forward>
else:
    <the existing revert, unchanged>
```

Two details the shape depends on. The filter is `p in written_paths and p not in restored`, not
`p not in restored` alone: a path this run never wrote is collected into `untouched` and reverting
the row is correct for it, so an unfiltered predicate would keep every row forward whenever an entry
carried one untouched path. And the predicate is the one the `origin == "landed"` branch thirty
lines above already computes for itself as `_left_landed`; this is the same test one level out, which
is why it is a gate and not a new mechanism.

### What the row keeping its forward values means

The row then describes the bytes that are actually on disk, which is the invariant the receipt exists
to hold. The consequence is stated rather than left to be discovered: the next `update` sees that row
at this run's vintage and will not re-offer the work, so the operator's repair is the order file and
not a second update. That is the correct trade — a receipt that agrees with the tree and re-offers
nothing beats a receipt that disagrees and re-offers everything, because only the second one can
silently overwrite an operator's manual repair.

### The order's fourth block

The lead sentence today reads "Every path marked `restored` below was put back to the index entry it
had before the first byte moved, and its receipt row with it." It becomes conditional: the sentence
stands for the `restored` block, and a new sentence says that any path under `NOT restored` is one
the rollback could not return, that its bytes are this run's, and that its receipt row was therefore
LEFT at this run's values on purpose.

The fourth block is emitted beside the three that exist:

```
NOT restored <path> — <the git operation that refused>; its bytes are this run's and its
                      receipt row was left forward so the receipt still describes the tree
```

S4's half-restored sentence is emitted for the `checkout-index` branch specifically, because that is
the only one of the four where a partial revert already happened: `update-index` succeeded, so the
index names the pre-run blob while the worktree holds this run's bytes and the row's `sha256`. An
operator reading `git status` there sees a modification they did not make, and the order is the only
place that explains it.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `unrestored` | local list in the rollback arm | `tools/govkit/govkit.py`, beside `restored`, `removed_landed` and `untouched` |
| `_left` | local list in the snapshot-entry loop | beside the existing `_left_landed` |

No new flag, file, config key or public surface; both names follow the three siblings already in that
scope.

### Files touched (estimate)

`tools/govkit/govkit.py` — about 25 lines: one list, four appends, one conditional around an existing
block, one order block and two sentences. `tools/govkit/selftest.py` — one fixture and three arms.

### The fixture, and why it does not exist today

`tools/govkit/govkit.py:7556`'s own header says no arm reaches the three plumbing failures, because
each needs the TARGET's git to refuse a call the suite does not manufacture. The cheapest
manufacturable one is `checkout-index`: make the worktree path a DIRECTORY where the receipt names a
file, so `checkout-index -f` cannot write it. That is a fixture edit rather than a git mock, it
reproduces the exact branch S4 describes, and it is the arm AC1 through AC4 are observed on.

### Alternatives rejected

- **Revert the row and re-stamp it afterwards from the file on disk.** That recomputes a hash for
  bytes nobody chose, so the receipt would attest content this run neither wrote nor restored.
- **Roll the whole kit's rows forward whenever any path fails.** Coarser than the entry, and it
  would keep a row forward for a path that restored cleanly, which is the mirror of the defect.
- **Raise a `Refusal` and abort the verb.** The run has already written bytes into a repository gov
  does not own; aborting mid-rollback leaves less on disk and less written down, not more.

### Migration

None. No receipt field or descriptor key changes shape. A target already carrying a row reverted over
a failed restore is not repaired by this unit — nothing knows which rows those are — and that is
stated rather than implied: the repair is the operator's, guided by the order this unit starts writing.

### Rollout

Lands directly. The gated path is only reachable inside a rollback that already failed, so no
adopter's ordinary run changes behaviour.

## 5. Production-readiness checklist

- **security** — no new write path. The unit strictly REDUCES what is written to the receipt.
- **perf / scale** — one list comprehension per snapshot entry inside a branch that already runs one.
- **error / empty / loading states** — an entry with no written paths leaves `_left` empty and takes
  the existing revert; an entry whose every path failed keeps every field forward.
- **observability** — the order gains a fourth block and the `r.fail` messages are unchanged, so the
  path appears both in the run's findings and in the durable record.
- **risks** — the main one is the filter: dropping `p in written_paths` would keep rows forward for
  untouched paths and quietly invert the fix. AC3 is written against exactly that mistake.
- **testing** — three direct selftest arms over one new fixture, plus the existing rollback arms held
  green as the negative case.
- **migration** — N/A; nothing stored changes shape and no back-fill is possible.
- **user docs** — `WIRE-INTO-PROJECT.md`'s maintenance section gains two sentences on what a
  `NOT restored` line means and why the row was left forward.

## 6. Acceptance criteria

- **AC1** — When the fixture makes `git checkout-index` fail for one path of a rolled-back kit,
  `python tools/govkit/govkit.py update --target <fixture> --write` names that path in an
  `r.fail` message and in the order's `NOT restored` block.
  Red when: the branch still only `continue`s, so the path is in none of `restored`, `removed` or
  `left alone`, and the order is silent about a file the rollback did not return.
  fixture: built by this unit — a directory at the worktree path the receipt names as a file.
- **AC2** — When that run finishes, the receipt row for the failed path still carries this run's
  `sha256`, and the file on disk hashes to it.
  Red when: the unconditional revert survives, so the row carries the pre-run `sha256` while the
  worktree holds this run's bytes.
- **AC3** — When a snapshot entry carries one path this run wrote and restored and one path this run
  never wrote, that entry's row IS reverted.
  Red when: the predicate omits `p in written_paths`, so an untouched path blocks the revert and every
  successful rollback stops reverting its rows.
- **AC4** — When the order file from AC1 is read, its lead sentence no longer claims that every path
  below was put back, and the `NOT restored` line for the `checkout-index` failure says that the
  index holds the pre-run blob while the worktree and the row hold this run's bytes.
  Red when: the lead sentence is left as written, so the document's first claim is false of the block
  printed under it.
- **AC5** — When the existing rollback arms run unchanged — the `-14` fixture at
  `tools/govkit/selftest.py:6130` and the landing fixture at `:5617` — every path still reports
  `restored` and every row still reverts.
  Red when: the gate is written so that it also fires on a clean rollback, which would leave every
  rolled-back row stamped forward and re-create the defect this gate's own neighbours were built for.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/govkit/selftest.py · a rolled-back kit whose worktree path is a directory, so
`git checkout-index -f` refuses and the branch at `tools/govkit/govkit.py:7618` is reached · none

`govkit refusal join` is named because this unit reuses the four existing `r.fail` branches and adds
none, so its branch pin and enumerated anchor set must be unchanged by this commit.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

The seam this unit extends is in the same function and was found by reading it rather than by name:
`tools/govkit/govkit.py:7638`'s `_left_landed = [p for p in s["paths"] if p not in restored]`, the
predicate the landed branch already computes to decide whether its own row may be dropped. This unit
is that predicate hoisted one level, and `python tools/codebase-map/reuse_lookup.py "update verb rolls
a kit back after declining its render step"` surfaces no other candidate — its ranked hits are
rendering and kit-path helpers, which is a miss to record rather than a phrasing to soften. Recall
returned the two records that own the invariant being protected: `DEPL-dSealedTally-1`, whose S3 and
S5 state that the row's fields are restored TOGETHER, and `DEPL-dCarriedReceipt-14`, which built the
rollback pass. Verified against source rather than against those records: the `-8` failure they name
is reachable through the failure branches they do not mention.

Recall terms used: `govkit update rollback receipt row restore verify baseline transition rendered
regenerate decline outbox order unattributed`
