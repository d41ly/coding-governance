# DEPL-dCarriedReceipt-14 — post-write verification, with index rollback

**Status:** CLOSED · rev-7 · 2026-08-25 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-build-DEPL-dCarriedReceipt-14-acceptance-ledger.md](../build/2026-08-25-build-DEPL-dCarriedReceipt-14-acceptance-ledger.md) | journal | — |
| [2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-15 |

<!-- /gen:spec-records -->

## 1. Goal

`three_way`'s stdout goes to disk at `govkit.py:3097` and to the target's index at `:3103`, and
nothing observes it. The exposure is specifically the CLEAN-merge path, not the conflict path: a
conflict already leaves the file byte-identical and writes an order (`:3085-3095`), while a `git
merge-file` that succeeds on non-overlapping hunks produces a plausible, wrong, executable file whose
first observer is a merge bar days later. `three_way`'s own docstring says so — a wrong argument order
does not error, it emits a plausible file with one side silently dropped (`:2899-2902`) — and the
write loop then hands that file to `git add` and re-stamps the receipt at `:3125`. Every kit in this
repo already declares how to measure whether it works: `[check].argv`, run per kit by `cmd_check` at
`:1632-1644`. This unit runs that same declaration after a write, and rolls the kit back when it reds.

## 2. Scope (IN)

- **S1** — extract `cmd_check`'s per-kit `[check].argv` runner (`:1632-1644`) into one helper taking a
  descriptor, a ctx and a target, returning the state it already computes: `adopted`,
  `landed-but-inert`, or `landed-unmeasured`. `cmd_check` calls the helper; nothing about its output
  changes.
- **S2** — a pre-write snapshot, taken before the first byte moves, keyed on the ROW rather than on a
  path string. It carries every path that row occupies — for a `renamed` row (`-11` S4) BOTH
  spellings, old and new — each with its index entry from `git -C <target> ls-files -s -- <path>` as
  `(mode, oid)`, or the marker `absent`. The snapshot rides `-7`'s index-side read rather than adding
  a second index reader. Keyed on the old path alone it cannot restore a rename: the bytes land at a
  path whose pre-write entry is `absent` under a key nothing ever looks up.
- **S3** — the snapshot also captures each touched ROW's `path`, `source`, `sha256`, `commit`,
  `gov_oid` and `oid` — every field `-11` S4 rewrites as a set, plus the two identities — **before**
  the loop mutates them in place at `:3072-3073`, at `:3098-3099`, and in `-11` S4, the third
  mutation site. Restoring bytes while leaving a row stamped forward re-creates `-8` exactly: the
  next run reads the row as `equal` against bytes that were reverted.
- **S4** — S1's helper runs TWICE for every TOUCHED kit: once as a BASELINE before the first byte
  moves, and once after the write loop. A touched kit is one owning at least one path in `changed`,
  `renamed` or `deleted` — `renamed` because `-11` S6's rows appear in neither of the other two, and
  a predicate reading only those two never verifies, never snapshots and never rolls back a rename.
  The population is known before the write, which is the same fact S2 already depends on, so the
  baseline needs no second classification pass. A kit the run did not touch is executed NEITHER time:
  the baseline is bounded to exactly the kits S4 was already going to check, so it never becomes the
  whole-bar run §3 rejects. A CLAIMED kit the run did not touch is printed once as `not-run` and
  counted under its own tally; an unclaimed registry entry is not one of these — `cmd_update`
  already prints it as `available (not installed)` at `:3027-3032`, and a second line about the
  same kit is two answers to one question. That state is owned here rather than by S1's helper,
  which returns only the three states a check that RAN can produce: a kit nothing executed has no
  check result to return.
- **S5** — the rollback keys on the TRANSITION, never on the after-state alone. A kit that was
  `adopted` at baseline and `landed-but-inert` after is rolled back, that kit only: for each of its
  touched paths, `git -C <target> update-index --cacheinfo <mode>,<oid>,<path>` then `git -C <target>
  checkout-index -f -- <path>`; a path whose snapshot is `absent` is `git rm --cached`-ed and
  unlinked, and a renamed row is restored under BOTH spellings from its S2 entry. Its rows are
  restored from S3. Restoring a renamed row restores `path` and `source` together with `commit` and
  `gov_oid`, because `-7` S9 asserts them against each other and a partial restore is the split that
  assertion exists to refuse.
- **S6** — a kit that was `landed-but-inert` at BOTH runs is **pre-existing red**: it is printed and
  counted under that name, its writes stand, and it is NOT rolled back and does NOT `r.fail`. That is
  the same disposition §8 F2 already gives `landed-unmeasured`, and it is the only escape from the
  wedge — rolling back on the after-state alone means an adopter carrying one unrelated local red
  reverts every correct write on every run, forever, while `r.fail` reaching `:3115` keeps
  `gov_commit` from ever advancing and §3 refuses the `--force` that would otherwise be the way out.
- **S7** — a rolled-back kit writes an outbox order in the shape `cmd_update` already uses at `:3087`,
  naming the kit, its check argv, both exit codes and every path restored, and calls `r.fail`. The
  existing `if r.problems` arm (`:3115`) then declines to re-stamp the receipt, which is already the
  correct behaviour and needs no change. A pre-existing red writes an order too, naming the kit and
  both exit codes, but without the `r.fail`, so the run completes and the receipt re-stamps.
- **S8** — the skip announces itself. A kit whose `[check]` is `{ none = "…" }`, or whose argv carries
  an unresolved token (`:1634-1637`), returns `landed-unmeasured` and is printed as **unverified**,
  counted separately from verified. A check that could not run is not a pass.
- **S9** — `selftest.py` arms per branch, and a `refusal_join.py` arm for the refusals S5 and S7 add.

## 3. Non-goals (OUT)

- **Not** a second check runner. The whole point is that `cmd_check` already knows how; a parallel
  implementation is the duplicate-answer class this build spends units removing.
- **Not** running the target's full gate bar. A deployer that runs an adopter's whole bar owns their
  runtime, their timeouts and their flakes. The kit's own declared check is the bounded question.
- **Not** rolling back the whole run when one kit reds. Kits are independent; a green kit's write is
  correct and reverting it discards a good result to punish a sibling.
- **Not** committing, reverting a commit, or touching the operator's stash or branches. The rollback
  restores the index and the worktree to the exact pre-write state for those paths and stops there.
- **Not** a `--force`, `--skip-verify` or `--no-verify` in any spelling. Cut-list item, and a verifier
  reachable past a flag is a verifier nobody runs.
- **Land-alone:** this unit needs `-7` beneath it for S2's index-side read and `-11` beneath it for
  the `renamed` disposition S2 and S4 both read. The full order is `-7`, then `-11`, then this unit,
  and it is an ORDER rather than a conflict — §8 F3 ratifies it and this bullet must not be read as
  a weaker "should". With both landed it stands alone and leaves both trees green. Nothing here
  orders against `-13`.

## 4. Design

### Data model

No receipt shape change. The snapshot is per-run state and it is keyed on the ROW, not on a path
string: one entry per touched row, carrying every path that row occupies — for a `renamed` row both
the old and the new spelling — each with its `(mode, oid)` or the marker `absent`, plus the row's
pre-write `path`, `source`, `sha256`, `commit`, `gov_oid` and `oid` — every field `-11` S4 rewrites
as a set, plus the two identities. A path-keyed map cannot restore a rename, because the new path's
pre-write state is `absent` and sits under a key the old spelling does not reach.

### Rollout

The verifier runs on every `--write` run from the moment it lands; there is no flag to enable it. That
is deliberate — an opt-in verifier verifies the runs that were already careful.

### Alternatives rejected

- *Verify by re-classifying the rows after the write.* It reads the same state the write produced, so
  a merge that dropped a hunk classifies as a clean `current`. A guard sharing a variable with the
  thing it guards is disabled by the bug it exists to catch.
- *Compare the merged file's line count or size against the two inputs.* A heuristic that passes for
  most wrong merges, which is the worst available property in a guard.
- *Restore from bytes held in memory instead of index OIDs.* The index OID is what the rest of this
  engine treats as the target's identity after `-7`, and a second restore channel would disagree with
  it the first time a filter or an `eol` pin is in play.
- *Roll back on the conflict path too.* Nothing is written there; the file is already byte-identical
  and the order already exists. Adding a rollback would be a check that cannot fail.
- *Baseline EVERY claimed kit before the write.* Rejected on the "every claimed kit" half only: it
  runs checks for kits the run never touches, which is the whole-bar behaviour §3 refuses. S4
  baselines the TOUCHED kits and nothing else, costing one extra check per kit the run was already
  going to check, and it is the only way to tell "this write broke it" from "it was already broken" —
  the distinction the rollback keys on, and the difference between a verifier and a wedge.

### Files touched (estimate)

`tools/govkit/govkit.py` (~125 lines: the extracted helper, the row-keyed snapshot, the baseline
pass and the verify-and-roll-back pass in `cmd_update`), `tools/govkit/selftest.py` (8 arms), one
fixture whose kit check rejects the exact file a clean three-way produces, and one whose kit check
reds at the baseline as well.

## 5. Production-readiness checklist

- security — this unit executes the target's copy of a kit check, which `cmd_check` already does for
  every claimed kit, so no new execution surface is opened. It stays bounded to kits the receipt
  claims: running a check for an unclaimed kit would execute code the receipt never authorized.
- perf / scale — two checks per TOUCHED kit, one baseline and one after, and none at all per row or
  per untouched claimed kit. On a run that moves rows in two kits, four checks run.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a check that crashes rather than exiting non-zero is treated as
  red and rolled back; a run that touched nothing runs no checks and says so; a `checkout-index` that
  itself fails is a refusal naming the path, never a silent partial restore.
- observability — one line per touched kit carrying BOTH its states, one `not-run` line per
  claimed kit the run did not touch, one rolled-back-paths list per rolled-back kit, and separate
  tallies for verified, unverified, not-run, rolled back and pre-existing red.
  Every one of those counts is printed even when it is zero, so an absence is never mistaken for
  coverage — a silent pre-existing-red tally would hide exactly the kits nothing verified.
- risks — the wedge is the risk to name first. Rolling back on the after-state alone means a target
  carrying ONE unrelated local red in a touched kit reverts every correct write on every run,
  forever: S5 would revert it, S7's `r.fail` reaches `:3115` so `gov_commit` never advances, and §3
  refuses a `--force` in any spelling, so nothing gets the adopter out and the run reports their
  standing red as a bad merge. The escape is S4's baseline, not a flag. Red-before-and-red-after is
  reported as pre-existing and left alone, and only green-before-red-after rolls back. What remains
  is narrower and is stated rather than implied: a kit already red keeps its writes, so a genuinely
  broken merge inside THAT kit lands unobserved, because a binary check cannot tell "still broken"
  from "newly broken". The trade is accepted in that direction, since reverting correct writes
  forever is the worse failure. `landed-unmeasured` still covers the third case, cannot run.
- testing + left-shift gates — eight `selftest.py` arms, RED-first at AC1. The class left-shifted is
  "a write reaches the index with nothing observing it", gated as AC5: after a red kit, that kit's
  paths are byte-identical to their pre-write index OIDs.
- migration / rollback — none on disk. Reverting the unit removes a verifier and restores today's
  behaviour; no receipt written under it reads differently without it.
- user docs — `WIRE-INTO-PROJECT.md`'s update section gains the post-write verification step and the
  fact that a red kit reverts itself and leaves an order.

## 6. Acceptance criteria

- **AC1** — In a fixture where a clean `git merge-file` produces a file the kit's own `[check].argv`
  rejects, `govkit.py update --write` at `9ddcc5c9` exits **0**, prints `0 conflict(s)`, leaves the
  broken file on disk and staged (`git -C <target> diff --cached --name-only` names it), and re-stamps
  the receipt. Observe this RED first; it is the exposure.
- **AC2** — After the change, the same fixture runs that kit's `[check].argv`, reports it
  `landed-but-inert`, and exits **1**.
- **AC3** — The rolled-back path's index entry equals its pre-write OID: `git -C <target> rev-parse
  :<path>` matches the snapshot, and `git -C <target> status --porcelain -- <path>` prints nothing.
  In a `-11` rename fixture the same assertion holds under BOTH spellings: the old path is restored
  from its snapshotted `(mode, oid)` and the new path is gone from the index, and the rolled-back
  row's `path` and `source` both carry the OLD spelling, so `-7` S9's preamble assertion holds on
  the next run. That is S2's row-keyed snapshot observed directly, and it is unreachable from a
  snapshot keyed on the old path alone.
- **AC4** — The receipt row for that path still carries its pre-run `path`, `source`, `sha256`,
  `commit`, `gov_oid` and `oid`, and `install.json`'s `gov_commit` is unchanged — the
  `if r.problems` arm at `:3115` declining to re-stamp.
- **AC5** — A green kit's writes survive a sibling kit's rollback: in a two-kit fixture where only one
  reds, the other kit's paths are staged at the new bytes and its rows carry the `--to` commit.
- **AC6** — Only touched kits run, twice each. In a fixture claiming three kits where one moves
  rows, exactly TWO `[check].argv` subprocesses are observed — S4's baseline and S4's after-pass
  over the one touched kit — and the other two claimed kits each print one `not-run` line and the
  `not-run` tally reads 2, with zero subprocesses for them. The arm fails both against a draft
  that baselines every claimed kit (six subprocesses, the whole-bar behaviour §3 refuses) and
  against one that skips the baseline (one subprocess, the wedge AC9 exists to close).
- **AC7** — A kit declaring `[check] = { none = "…" }` and a kit whose argv carries an unresolved
  token are both printed as `landed-unmeasured` and counted as **unverified**, and neither is counted
  as verified.
- **AC8** — `python tools/govkit/refusal_join.py` exits 0, with an arm for each refusal branch this
  unit adds, and `govkit.py check` output is byte-identical before and after the S1 extraction on a
  fixture target.
- **AC9** — the pre-existing-red arm. In a fixture whose kit `[check].argv` reds at the BASELINE as
  well as after the write, `update --write` prints that kit as **pre-existing red**, performs no
  rollback — `git -C <target> rev-parse :<path>` does NOT match the pre-write snapshot and the new
  bytes stand — raises no `r.fail` for it, and `install.json`'s `gov_commit` advances to `--to`. This
  is the wedge arm, and it fails against a draft that keys the rollback on the after-state: there, an
  adopter with one unrelated local red reverts every correct write on every run, forever.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs, plus `tools/govkit/refusal_join.py`. Adds eight arms, the AC8 extraction-parity
assertion and AC9's pre-existing-red arm; adds no new leg file. The `refusal_join.py` anchor set
moves because S1 relocates
`cmd_check`'s existing `r.fail` calls into a helper, and that shift is re-pinned in the same commit
rather than waived.

## 8. Open questions

- **F1 — verify per touched KIT, or per touched PATH?** Per kit. A kit's `[check].argv` is a statement
  about the kit, not about one file, and a per-path rollback would revert half a kit into a state its
  own check never graded.
  RESOLVED (agent, 2026-08-24, delegated): per kit, under the full-scope approval.
- **F2 — should a `landed-unmeasured` kit block the receipt re-stamp?** No, but it must be loud. It is
  the pre-existing state of any kit that declares no check, so blocking on it would make every such
  target permanently red from a successful update — the failure `-2` exists to remove. It is counted
  as unverified and named in the run's output.
  RESOLVED (agent, 2026-08-24, delegated): report loudly, do not block.
- **F3 — landing order.** This unit cannot land before `-7`, whose index-side read S2 reuses, and it
  cannot land before `-11` either. `-11` introduces the `renamed` disposition that S2's row-keyed
  snapshot and S4's touched-kit predicate both read, and a merged renamed row lands at a NEW path
  whose pre-write snapshot is `absent` under the old key, so rev-1's "does not conflict with `-11`"
  was false. It is an ORDER rather than a conflict, and the order is `-7`, then `-11`, then this
  unit. Nothing here touches `-13`.
  RESOLVED (agent, 2026-08-24, delegated): lands after `-7` and after `-11`.

## 9. Revision log

- rev-7 · 2026-08-25 · round-6 fold: L6 — rev-6 declared the `not-run` state in the scope item
  that owns it, but left it UNSCOPED: "a kit the run did not touch", where §5 and AC6 both bound
  it to CLAIMED kits. A builder implementing S4 as written prints a `not-run` line for every
  registry entry the target does not claim, which `cmd_update` already prints as `available (not
  installed)` at `:3027-3032` — two answers to one question, in the output of the verb built to
  end silent partial installs. S4 now carries the bound and names that collision. AC6's "the
  tally names the other two kits" is split into the LINE per kit and the COUNT, matching §5's two
  outputs rather than giving one output two spellings.
- rev-6 · 2026-08-25 · round-5 fold: M5 — AC6 asserted a tally state `not-run` that S1's
  return set, S8 and §5's enumeration all omitted, so a builder implementing §5 as written
  printed four tallies and reds the one criterion fencing S4's baseline. The state is added where
  it is owned: S4 declares it and says why S1's helper cannot supply it, and §5's observability
  line prints a `not-run` line per untouched claimed kit and carries the fifth tally. AC6 is
  unchanged; its subprocess half was already right.
- rev-5 · 2026-08-25 · round-4 fold: B3 — the rollback snapshot enumerated four of the six fields
  `-11` S4 rewrites as a set, so a rolled-back rename kept `path`/`source` at their post-rename
  spelling beside `commit`/`gov_oid` at their pre-rename values, which is the
  exactly-one-of-the-two split `-7` S9 refuses the whole run on. S3, §4's Data model and AC4 now
  enumerate `path`, `source`, `sha256`, `commit`, `gov_oid` and `oid`; S3 names `-11` S4 as the
  third mutation site; S5 restores a renamed row's paths together with its identities; and AC3's
  rename arm asserts the OLD spelling on both. H3 — AC6 asserted ONE `[check].argv` subprocess
  where S4 mandates two per touched kit, so it reds a correct build; it now asserts TWO and names
  the two drafts it fails against.
- rev-4 · 2026-08-24 · round-3 fold: the rollback snapshot restored three of the receipt's four
  per-row identity fields. S3, §4 and AC4 each enumerated `sha256`, `commit` and `gov_oid` — the set
  as it stood before `-7` added `oid` as a stored field — so a rolled-back row kept the failed run's
  `oid` and read as a local delta forever after. All three enumerations now carry `oid`.
- rev-3 · 2026-08-24 · round-2 fold: §3's land-alone bullet now carries the ORDER F3 ratified —
  `-7`, then `-11`, then this unit — instead of naming the two prerequisites without their sequence,
  so the two sections cannot be read as a hard order and a soft preference. The `cmd_check`
  citations were re-measured at `9ddcc5c9` and both stand: the `[check].argv` arm is `:1632-1644`
  and the state machine around it is `:1630-1655`, with the `[[hole]].discharge` runner beginning at
  `:1657` — which this unit does not touch and does not cite.
- rev-2 · 2026-08-24 · folded the pre-code review: the verifier no longer wedges a target that was
  already red. S4 baselines the TOUCHED kits — the population it already bounds — and runs the check
  before as well as after; S5 keys the rollback on the TRANSITION, so only green-before-red-after
  reverts; a new S6 reports red-before-and-red-after as pre-existing red, without a rollback and
  without an `r.fail`, so `gov_commit` still advances and the adopter is not reverted forever with no
  `--force` to escape by; and §5's risks line now states the wedge, the escape and the narrower
  residual it leaves. The `-11` interaction is folded too: S2's snapshot is keyed on the ROW and
  carries both spellings of a renamed row, S4's touched-kit predicate reads `renamed`, AC3 asserts
  the rename rollback, and F3's "does not conflict with `-11`" is replaced by the ordering `-7`,
  `-11`, this unit. AC9 is the pre-existing-red fixture arm, the old S6–S8 renumber to S7–S9, and
  the three `if r.problems` citations move from `:3111` to `:3115` with the re-stamp at `:3125`,
  both re-read at `9ddcc5c9`.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold). The unobserved
  write path (`:3097`, `:3103`), the conflict path's byte-identical guarantee (`:3085-3095`),
  `three_way`'s dropped-side docstring (`:2899-2902`), `cmd_check`'s argv runner and its three states
  (`:1630-1655`), and the row mutations at `:3072-3073` and `:3098-3099` were each read in source at
  `9ddcc5c9`. The brief cites `:1632-1652` for the runner; the argv arm is `:1632-1644` and the
  surrounding state machine `:1630-1655`. No rollback machinery of any kind exists in this file today.

## 10. Reuse audit

The check runner is the reuse: `cmd_check`'s existing `[check].argv` arm is extracted and called
twice rather than re-implemented, and it keeps using `resolve_tokens` (`:516`) and
`resolve_shell_argv` (`:498`) exactly as it does today. The target-side index read is `-7`'s, not a
second one. The outbox order reuses the path and format already written for a three-way conflict
(`:3087-3093`), and the receipt-not-re-stamped behaviour reuses the existing `if r.problems` arm
(`:3115`) rather than adding a second condition. The refusals reuse the `Refusal` class (`:78`) and
the `Report` channel (`:565`) and are counted by the existing `refusal_join.py` contract. One new
mechanism exists — the index snapshot and restore — and it has no prior seam: nothing in this engine
has ever undone a write.
