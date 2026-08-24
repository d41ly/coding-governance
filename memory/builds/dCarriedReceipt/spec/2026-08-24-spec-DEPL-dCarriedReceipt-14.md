# DEPL-dCarriedReceipt-14 — post-write verification, with index rollback

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

## 1. Goal

`three_way`'s stdout goes to disk at `govkit.py:3097` and to the target's index at `:3103`, and
nothing observes it. The exposure is specifically the CLEAN-merge path, not the conflict path: a
conflict already leaves the file byte-identical and writes an order (`:3085-3095`), while a `git
merge-file` that succeeds on non-overlapping hunks produces a plausible, wrong, executable file whose
first observer is a merge bar days later. `three_way`'s own docstring says so — a wrong argument order
does not error, it emits a plausible file with one side silently dropped (`:2899-2902`) — and the
write loop then hands that file to `git add` and re-stamps the receipt at `:3124`. Every kit in this
repo already declares how to measure whether it works: `[check].argv`, run per kit by `cmd_check` at
`:1632-1644`. This unit runs that same declaration after a write, and rolls the kit back when it reds.

## 2. Scope (IN)

- **S1** — extract `cmd_check`'s per-kit `[check].argv` runner (`:1632-1644`) into one helper taking a
  descriptor, a ctx and a target, returning the state it already computes: `adopted`,
  `landed-but-inert`, or `landed-unmeasured`. `cmd_check` calls the helper; nothing about its output
  changes.
- **S2** — a pre-write snapshot, taken before the first byte moves, of every path the run will touch:
  its index entry from `git -C <target> ls-files -s -- <path>` as `(mode, oid)`, or the marker
  `absent`. The snapshot rides `-7`'s index-side read rather than adding a second index reader.
- **S3** — the snapshot also captures each touched ROW's `sha256`, `commit` and `gov_oid` **before**
  the loop mutates them in place at `:3072-3073` and `:3098-3099`. Restoring bytes while leaving a row
  stamped forward re-creates `-8` exactly: the next run reads the row as `equal` against bytes that
  were reverted.
- **S4** — after the write loop, for every TOUCHED kit — a kit owning at least one path in `changed`
  or `deleted` — run S1's helper. A kit the run did not touch is not executed.
- **S5** — a kit returning `landed-but-inert` is rolled back, that kit only: for each of its touched
  paths, `git -C <target> update-index --cacheinfo <mode>,<oid>,<path>` then `git -C <target>
  checkout-index -f -- <path>`; a path whose snapshot is `absent` is `git rm --cached`-ed and
  unlinked. Its rows are restored from S3.
- **S6** — a rolled-back kit writes an outbox order in the shape `cmd_update` already uses at `:3087`,
  naming the kit, its check argv, the exit code and every path restored, and calls `r.fail`. The
  existing `if r.problems` arm (`:3111`) then declines to re-stamp the receipt, which is already the
  correct behaviour and needs no change.
- **S7** — the skip announces itself. A kit whose `[check]` is `{ none = "…" }`, or whose argv carries
  an unresolved token (`:1634-1637`), returns `landed-unmeasured` and is printed as **unverified**,
  counted separately from verified. A check that could not run is not a pass.
- **S8** — `selftest.py` arms per branch, and a `refusal_join.py` arm for the refusals S5 and S6 add.

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
- **Land-alone:** this unit needs `-7` beneath it for S2's index-side read. With `-7` landed it stands
  alone and leaves both trees green.

## 4. Design

### Data model

No receipt shape change. The snapshot is per-run state: one map from touched path to `(mode, oid)` or
`absent`, and one map from touched path to the row's pre-write `sha256`, `commit` and `gov_oid`.

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
- *Run the check before the write as a baseline.* It doubles the run cost to answer a question the
  operator can answer with `govkit check` on a tree they have not yet modified, and a kit that was
  already red before the write is a state this unit reports rather than repairs.

### Files touched (estimate)

`tools/govkit/govkit.py` (~110 lines: the extracted helper, the snapshot, the verify-and-roll-back
pass in `cmd_update`), `tools/govkit/selftest.py` (7 arms), one fixture whose kit check rejects the
exact file a clean three-way produces.

## 5. Production-readiness checklist

- security — this unit executes the target's copy of a kit check, which `cmd_check` already does for
  every claimed kit, so no new execution surface is opened. It stays bounded to kits the receipt
  claims: running a check for an unclaimed kit would execute code the receipt never authorized.
- perf / scale — one check per TOUCHED kit, not per row and not per claimed kit. On a run that moves
  rows in two kits, two checks run.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a check that crashes rather than exiting non-zero is treated as
  red and rolled back; a run that touched nothing runs no checks and says so; a `checkout-index` that
  itself fails is a refusal naming the path, never a silent partial restore.
- observability — one line per touched kit carrying its state, one rolled-back-paths list per red kit,
  and separate tallies for verified, unverified and rolled back. The unverified count is printed even
  when it is zero, so its absence is never mistaken for coverage.
- risks — the residual risk is a check whose own dependencies are unavailable in the adopter's
  environment: it reds, the kit rolls back, and a correct write is reverted. That is the direction
  chosen: a spurious rollback costs a re-run, a missed bad merge costs the file. `landed-unmeasured`
  exists so the third case — cannot run — is not silently folded into either.
- testing + left-shift gates — seven `selftest.py` arms, RED-first at AC1. The class left-shifted is
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
- **AC4** — The receipt row for that path still carries its pre-run `sha256`, `commit` and `gov_oid`,
  and `install.json`'s `gov_commit` is unchanged — the `if r.problems` arm at `:3111` declining to
  re-stamp.
- **AC5** — A green kit's writes survive a sibling kit's rollback: in a two-kit fixture where only one
  reds, the other kit's paths are staged at the new bytes and its rows carry the `--to` commit.
- **AC6** — Only touched kits run. In a fixture claiming three kits where one moves rows, exactly one
  `[check].argv` subprocess is observed and the tally names the other two as `not-run`.
- **AC7** — A kit declaring `[check] = { none = "…" }` and a kit whose argv carries an unresolved
  token are both printed as `landed-unmeasured` and counted as **unverified**, and neither is counted
  as verified.
- **AC8** — `python tools/govkit/refusal_join.py` exits 0, with an arm for each refusal branch this
  unit adds, and `govkit.py check` output is byte-identical before and after the S1 extraction on a
  fixture target.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs, plus `tools/govkit/refusal_join.py`. Adds seven arms and the AC8 extraction-parity
assertion; adds no new leg file. The `refusal_join.py` anchor set moves because S1 relocates
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
- **F3 — landing order.** This unit cannot land before `-7`, whose index-side read S2 reuses. It has
  no other dependency and does not conflict with `-11` or `-13`.
  RESOLVED (agent, 2026-08-24, delegated): lands after `-7`.

## 9. Revision log

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
(`:3111`) rather than adding a second condition. The refusals reuse the `Refusal` class (`:78`) and
the `Report` channel (`:565`) and are counted by the existing `refusal_join.py` contract. One new
mechanism exists — the index snapshot and restore — and it has no prior seam: nothing in this engine
has ever undone a write.
