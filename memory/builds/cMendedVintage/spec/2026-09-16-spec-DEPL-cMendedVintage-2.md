# DEPL-cMendedVintage-2 — a failed restore keeps its receipt row forward, and the order names the path

**Status:** CLOSED · rev-4 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-DEPL-cMendedVintage-2-acceptance-ledger.md](../build/2026-09-16-build-DEPL-cMendedVintage-2-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-prompt-DEPL-cMendedVintage-2-2-build-brief.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-2-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |

<!-- /gen:spec-records -->

## 1. Goal

When a rollback cannot restore a path, `update --write` reverts that path's receipt row to its
pre-run values anyway and writes the result to disk, so the receipt claims a `sha256` the file does
not have and the next run classifies it against bytes that never came back. Revert the row only when
the file actually went back, and name the path that did not in the order.

## 2. Scope (IN)

- **S1** The four restore-failure branches inside `tools/govkit/govkit.py`'s rollback path loop —
  the `demand_contained_dest` refusal, the `git rm --cached` failure, the `git update-index` failure
  and the `git checkout-index` failure — record the path they could not restore in an `unrestored`
  list before they `continue`. Named by their calls and not by line numbers: rev-1 spelled those and
  they drifted 41 lines in one commit, then again inside this unit's own. Observed by AC1.
- **S2** The `ROLLBACK_FIELDS` revert and the `withdrawn_rows` removal at the foot of the snapshot-entry
  loop run only when every path of that snapshot entry that this run WROTE is in `restored`. Observed by
  AC2 for the failing half and AC5 for the clean one; the `WROTE` filter itself is observed by
  nothing and AC3 says why.
- **S3** The rollback order gains a fourth block naming every unrestored path, and its lead sentence
  stops claiming that every path below was put back. The block's LINE is derived from the same
  `_left` predicate that gates the revert, never from `unrestored` alone, so a path the gate did not
  hold is never printed under a sentence claiming its row was left forward. The `demand_contained_dest`
  refusal is that case and it takes its own sentence, named in §4. Observed by AC4 and AC6.
- **S4** That fourth block states the half-restored case explicitly: when `git checkout-index` is what
  failed, the index was ALREADY reverted to the pre-run blob while the worktree file did not come
  back, so index and worktree disagree at that path and the row was left at this run's values.
  Observed by AC4.

## 3. Non-goals (OUT)

- No new refusal. Each of the four branches already calls `r.fail` with its own message; this unit
  adds a list append beside each and changes no message, so the deployer's refusal-branch population
  is unchanged.
- No retry, no second restore attempt, no fallback write. A restore that git refused is an operator
  problem, and a tool that keeps trying is how a part-restored tree becomes an unreadable one.
- No change to the `origin == "landed"` branch, which already gates
  its own row removal on the same predicate. This unit lifts that idea one level out; it does not
  rewrite that branch.
- Nothing about WHICH kits reach the restore loop. That is the unit before this one.

### Edges

- **consumes-from** `DEPL-cMendedVintage-1` — after that unit the green-to-red arm has two exits and
  a kit diverted by a declined render never walks the restore loop at all. This unit's gating grades
  only the kits that do walk it, and would otherwise be written as though every rolled-back kit
  passed through here.
- **hands-off** external — nothing in this build consumes this unit's output.

- **hands-off** `DEPL-cMendedVintage-18` — that unit keeps a withdrawn row whose path did not restore in the receipt, which this unit's gating leaves open.
## 4. Design

### The defect, read from source

`tools/govkit/govkit.py`'s rollback arm opens `for s in [x for x in snap_rows if x["kit"] == eid]:`
and then
`for p in s["paths"]:`. Inside the inner loop, four outcomes end in `continue`: a containment refusal,
a `git rm --cached` that would not unstage, a `git update-index` that would not take the entry, and a
`git checkout-index` that could not write the worktree file. Each appends nothing to `restored`.

Control then leaves the inner loop and reaches, unconditionally, the block that copies
`s["fields"]` back onto `s["row"]` for every key in `ROLLBACK_FIELDS` and drops the row from
`withdrawn_rows`, and the receipt is then serialised to `install.json`. So the file on disk is not
what the row describes — it holds what this run wrote, or, where `checkout-index -f` refused, nothing
at all — while the row claims the pre-run `sha256`, `oid`, `commit` and `version` —
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
the row is correct for it, so an unfiltered predicate would keep that entry's row forward for a path
it had no business holding. AC3 records that no entry reachable today mixes the two, so the filter
is a class guard rather than a fix for a live case — its reason lives at the code site, where the
next reader of the predicate will meet it. And the predicate is the one the `origin == "landed"` branch thirty
lines above already computes for itself as `_left_landed`; this is the same test one level out, which
is why it is a gate and not a new mechanism.

### What the row keeping its forward values means

The row then describes what this run did rather than a pre-run state nothing returned to, which is
the weaker claim the receipt can actually stand behind: where the restore left the file this run's,
the row matches it, and where `checkout-index` took the file away entirely the row at least stops
attesting a `sha256` for content that was never put back. The consequence is stated rather than left
to be discovered: the next `update` sees that row
at this run's vintage and will not re-offer the work, so the operator's repair is the order file and
not a second update. That is the correct trade — a receipt that agrees with the tree and re-offers
nothing beats a receipt that disagrees and re-offers everything, because only the second one can
silently overwrite an operator's manual repair.

### The order's fourth block

The lead sentence today reads "Every path marked `restored` below was put back to the index entry it
had before the first byte moved, and its receipt row with it." It becomes conditional: the sentence
is narrowed to the `restored` block with an `and ONLY those`, and a new sentence says that any path
under `NOT restored` is one the rollback could not return at all, whose own line names what refused
and what its receipt row now holds. The line does not say whose bytes are on disk, because after a
refused `checkout-index` nothing in this tool knows.

The fourth block is emitted beside the three that exist:

```
NOT restored <path> — <the git operation that refused>; the rollback did not return it, so its
                      receipt row was LEFT at this run's values rather than claiming a pre-run
                      state the tree does not have
```

S4's half-restored sentence is emitted for the `checkout-index` branch specifically, because that is
the only one of the four where a partial revert already happened: `update-index` succeeded, so the
index names the pre-run blob. What the WORKTREE holds there was measured rather than assumed, and it
is not what rev-2 of this spec claimed. `git checkout-index -f` unlinks the existing file BEFORE it
writes the replacement, so on the failing path the worktree file is simply GONE — staged, in the
probe under §"The fixture", as an absent `tools/demo/victim.txt` beside an index entry naming the
pre-run blob. The sentence therefore says that index and worktree disagree and that the row was left
at this run's values; it does not promise which bytes are on disk, because after a refused
`checkout-index` that is git's business and not this tool's. An operator reading `git status` there
sees a deletion they did not make, and the order is the only place that explains it.

### The containment case prints a different sentence

The `demand_contained_dest` refusal runs BEFORE the `p not in written_paths`
test at `:7584`, and its own header says it exists for a receipt row spelling `../../x` that the
write loop refused — which is a path absent from `written_paths` by construction. So `_left` excludes
it and the revert DOES run for its entry. Printing it under the sentence above would make two false
claims at once: the bytes are not this run's, and the row did not stay forward.

```
NOT restored <path> — refused as outside the target; nothing was written for it and its receipt
                      row was reverted with the rest of its entry
```

The block is therefore assembled per path from the predicate that decided that path's fate, not from
`unrestored` as one list. That is the same rule §4's gate follows one paragraph up, applied to the
document instead of to the receipt: the report and the revert read one predicate or they disagree.

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

The `NO ARM REACHES THE THREE PLUMBING FAILURES` header in `tools/govkit/govkit.py` says no arm reaches the three plumbing failures, because
each needs the TARGET's git to refuse a call the suite does not manufacture. The cheapest
manufacturable one is `checkout-index`, and rev-2 named the wrong way to manufacture it: a DIRECTORY
at the worktree path does NOT reproduce the branch, because `checkout-index -f` removes a directory
in its way and restores the file cleanly — measured on the real engine before any of this was
written, and the probe reported the path `restored`.

What does reproduce it is a git filter the target's own git must honour: the kit's `[check]` script,
which runs AFTER the write and BEFORE the rollback, writes a `.gitattributes` binding the victim path
to a `required` filter whose smudge command fails. `checkout-index` then exits non-zero with
`smudge filter … failed` and the `git checkout-index` branch is reached. That window is
the fixture's whole trick and it is why no fixture could stage this from outside the run: before the
write the path must be ordinary or the write loop trips on it, and after the rollback it is too late.
It is a fixture edit rather than a git mock, and it is the arm AC1, AC2 and AC4 are observed on.

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
  untouched paths and quietly invert the fix. Nothing observes that today (AC3, retired), so the
  reason is written at the code site where the next reader of the predicate will meet it.
- **testing** — direct selftest arms over one new fixture, plus the existing rollback arms held green
  as the negative case. AC6 gets none and §6 says why.
- **migration** — N/A; nothing stored changes shape and no back-fill is possible.
- **user docs** — `WIRE-INTO-PROJECT.md`'s maintenance section gains two sentences on what a
  `NOT restored` line means and why the row was left forward.

## 6. Acceptance criteria

- **AC1** — When the fixture makes `git checkout-index` fail for one path of a rolled-back kit,
  `python tools/govkit/govkit.py update --target <fixture> --write` names that path in an
  `r.fail` message and in the order's `NOT restored` block.
  Red when: the branch still only `continue`s, so the path is in none of `restored`, `removed` or
  `left alone`, and the order is silent about a file the rollback did not return.
  fixture: built by this unit — the kit's own `[check]` binds that path to a `required` git filter
  whose smudge command fails, in the window between the write and the rollback.
- **AC2** — When that run finishes, the receipt row for the failed path still carries this run's
  `sha256` and `commit`, and the worktree does NOT hold the pre-run bytes — so no row claims a
  restore that did not happen. The disk side is stated as a negative on purpose: rev-2 asked for the
  file to hash to the row, and a refused `checkout-index -f` leaves no file at all, so that positive
  is unobservable on the only fixture that reaches the branch.
  Red when: the unconditional revert survives, so the row carries the pre-run `sha256` while the
  worktree does not.
- **AC3** — RETIRED as an observable criterion, by reading the code it was written against. The only
  snapshot entry carrying two paths is a `renamed` one, and both its spellings enter `written_paths`
  together or neither does: a rename that lands puts both in `renamed`, and a rename the occupied
  destination refuses writes neither. A `withdrawn` entry carries exactly one path, and that path is
  in `deleted`. So NO fixture can stage an entry mixing a written path with an untouched one, and
  dropping `p in written_paths` today changes no receipt anywhere — rev-2 claimed it would break
  "every successful rollback", which is false.
  The filter STAYS, as a class guard with its reason at the code site: the first verdict that writes
  one path of a multi-path entry inverts the fix without it. What is observable is the other half,
  that the gate does not fire on a clean rollback, and AC5 owns that.
  Red when: the filter is dropped AND some later verdict writes one path of a multi-path entry while
  leaving another untouched — then that untouched path pins its row forward and the rollback stops
  reverting rows it did restore. No fixture reaches that population today, which is why this
  criterion is retired to a code-site comment rather than staged; a criterion no run can fail is the
  green-by-absence class and is not left standing as if it were coverage.
- **AC4** — When the order file from AC1 is read, its lead sentence no longer claims that every path
  below was put back, and the `NOT restored` line for the `checkout-index` failure says that the
  index was already reverted to the pre-run blob while the worktree file did not come back, so the
  two disagree.
  Red when: the lead sentence is left as written, so the document's first claim is false of the block
  printed under it.
- **AC5** — When the existing rollback arms run unchanged — the `-14` fixture at
  `tools/govkit/selftest.py:6130` and the landing fixture at `:5617` — every path still reports
  `restored` and every row still reverts.
  Red when: the gate is written so that it also fires on a clean rollback, which would leave every
  rolled-back row stamped forward and re-create the defect this gate's own neighbours were built for.
- **AC6** — When a fixture receipt row spells a path outside the target and
  `python tools/govkit/govkit.py update --target <fixture> --write` rolls that kit back, the order's
  `NOT restored` line for that path says the write was refused and the row was reverted, and does not
  claim the bytes are this run's.
  Red when: the block is assembled from `unrestored` as one list, so the containment case takes the
  restore branch's sentence and the one document written to explain a failed restore makes two false
  claims about the only population that branch exists for.
  fixture: NONE, and that is recorded rather than smoothed over. Reaching this line needs a receipt
  row whose `path` escapes the target AND a verdict touching enough to enter `snap_rows`, which the
  receipt-integrity preamble is built to refuse before the rollback is ever reached; rev-2 called it
  cheap without staging it. The sentence selection ships class-guarded, on exactly the footing the
  containment refusal above it already declares for itself — guarded because the class is the same
  and the cost is one condition, not because a fixture demonstrated it. The branch count is held by
  `govkit refusal join` on the owed bar; the sentence itself is held by nothing and says so here.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/govkit/selftest.py · a rolled-back kit whose own check installs a `required` git
filter over one of its paths, so `git checkout-index -f` refuses and the branch at
the `git checkout-index` branch is reached · none

`govkit refusal join` is named because this unit reuses the four existing `r.fail` branches and adds
none, so its branch pin and enumerated anchor set must be unchanged by this commit.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-16 · S3 · §4 · AC6 · folded spec-audit round 1 finding M4: a path the containment
  refusal rejects is excluded by the `_left` filter, so its row IS reverted, and printing it under
  the restore branch's sentence made two false claims. The block is now derived per path from the
  predicate that decided it, the containment case has its own sentence, and AC6 stages it.
- rev-3 · 2026-09-16 · S1 · S2 · S3 · S4 · §4 · §5 · AC2 · AC3 · AC4 · AC6 · §7 · the build pass staged the
  failure against the real engine before writing the fix, and it falsified three of this spec's
  claims. (a) A DIRECTORY at the worktree path does not make `checkout-index -f` refuse — git removes
  it and restores the file — so the fixture rev-2 named would have graded a clean rollback; the
  fixture is now a `required` git filter the kit's own check installs in the window between the write
  and the rollback. (b) `checkout-index -f` unlinks before it writes, so on the failing path the
  worktree file is ABSENT, not this run's bytes: S4's half-restored sentence, AC2's disk clause and
  the order's line are restated as index-and-worktree-disagree rather than as a promise about which
  bytes are on disk. (c) AC6's containment case was called cheap to stage and is not — no fixture
  reaches it and it now says so, on the same class-guard footing the refusal it reports on already
  declares. (d) AC3 is retired: no reachable snapshot entry mixes a written path with an untouched
  one, so the filter it graded is unobservable today and the criterion said otherwise. Also: every
  `tools/govkit/govkit.py` line number in rev-1 was taken before
  `DEPL-cMendedVintage-1` landed in the same function and had drifted +41; they are re-taken here
  against 03ba97f1 and will drift again, which is why each one is named beside the identifier it
  points at.
- rev-4 · 2026-09-17 · §3 · RECIPROCAL EDGE, no scope or criterion changed. The spec-audit disposal authored DEPL-cMendedVintage-18 naming this unit, and the edge was never written back — hygiene check 12 reds on a handoff one author declared and the other never saw. The edge is a fact about this build that became true when the promotion was created, so recording it completes the record rather than changing the design.

## 10. Reuse audit

The seam this unit extends is in the same function and was found by reading it rather than by name:
`tools/govkit/govkit.py`'s `_left_landed = [p for p in s["paths"] if p not in restored]`, the
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
