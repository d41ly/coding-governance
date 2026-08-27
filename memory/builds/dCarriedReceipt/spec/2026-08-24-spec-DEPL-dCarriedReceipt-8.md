# DEPL-dCarriedReceipt-8 — a merge result never overwrites `gov_oid`

**Status:** CLOSED · rev-5 · 2026-08-25 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-build-DEPL-dCarriedReceipt-8-acceptance-ledger.md](../build/2026-08-25-build-DEPL-dCarriedReceipt-8-acceptance-ledger.md) | journal | — |
| [2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round6.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round6.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 |
| [2026-08-26-review-DEPL-dCarriedReceipt-15-diff-review-round4.md](../reviews/2026-08-26-review-DEPL-dCarriedReceipt-15-diff-review-round4.md) | diff-review | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |

<!-- /gen:spec-records -->

## 1. Goal

`update` preserves an adopter's local edit through a three-way merge, then destroys it on the next
run and reports that as a clean write. This is the unit the owner's whole requirement reduces to,
and it was reproduced end to end on 2026-08-24 at `9ddcc5c9` rather than reasoned about.

The reproduction. A scratch target takes `govkit.py apply --kits check-wiring`, its receipt is
rewound to `24f39915`, and one line is appended to `tools/check-wiring.sh`. Then
`update --to 372e6b2a --write` reports `diverged 1 · stale 1`, the three-way merges, and the local
line survives — the guarantee working exactly as designed. The next `update --write` to `9ddcc5c9`
reports `stale 2` and `wrote 2, deleted 0, 0 conflict(s)`, and `grep -c` for that line on the file
returns 0. The adopter's edit is gone, and the run that destroyed it printed no finding at all.

The mechanism, in the file's own terms. On the merged row `:3098` sets `row["sha256"]` to the hash
of the MERGED bytes and `:3099` advances `commit`. On the next run `classify_row` compares the
target's bytes to that field (`:2889`), gets `o_state` `equal`; `theirs` has moved, so `t_state` is
`differs`; `VERDICT_GRID[("equal", "differs")]` is `stale` (`:2845`); and the write arm at
`:3069-3073` raw-overwrites with gov's bytes. The code contradicts its own docstring while it does
it: `classify_row` at `:2877-2878` says the receipt's hash "is what gov actually wrote", and `:3098`
writes what the merge produced.

A second symptom of the same overload, also measured. Immediately after the successful merge,
`govkit.py check` reds — `provenance: 1/2 resolved` and `'tools/check-wiring.sh': the receipt's hash
does not match gov's own bytes at 372e6b2a9a7d` — because `cmd_check`'s provenance loop
(`:1522-1531`) reads that same field as GOV's hash. One field, two readers, opposite meanings.

`-7` supplies the two identities and deliberately leaves this corruption intact under a new name.
This unit is where `gov_oid` starts meaning gov's blob at `commit` and keeps meaning it.

## 2. Scope (IN)

- **S1** — the merge branch stops deriving `gov_oid` from anything the target produced. It writes
  `oid` as the blob of the merged bytes and `gov_oid` as the blob gov ships at `to_commit` for the
  row's `source`, and `commit` still advances to `to_commit`.
- **S2** — the raw-write branch at `:3069-3073` writes `oid` and `gov_oid` as the same gov blob.
  The two agreeing there is not a coincidence to maintain, it is the definition of that arm.
- **S3** — `oid != gov_oid` is the local-delta predicate, recomputed per run from `-7`'s index read
  against the row's STORED `gov_oid`. No stored boolean expresses it, here or anywhere. A row a
  proven `carry` rung explains reads `oid != gov_oid` TOO, because a filtered or relocated copy is
  never byte-identical to gov's blob. Such a row is NOT a local delta in the adopter-edit sense; it
  is CARRIED, and the two states are distinguished by `-9`'s proof rather than by this predicate.
  `-9` owns the rung and this unit does not restate its mechanism. The one consequence that binds
  here is that a proven rung leaves `o_state` alone, so the verdict still comes from the unchanged
  `VERDICT_GRID` (`:2843`) and the row RECONCILES through this unit's `three_way` (`:2897`) with
  `-9`'s rung already applied. A proven rung therefore never re-opens the raw-write arm **through the
  `stale` cell**: `stale` sits on the `equal` OURS row of the grid, and a carried row is not on it.
  The arm at `:3069-3073` is guarded by `v == "stale" or v == "missing"`, and the second half is NOT
  closed by this reasoning — `missing` comes from the `absent` OURS row (`:2887-2888`), which a
  carried row the target DELETED does reach, with no `ours` bytes left to prove a rung against. That
  cell is `-9` S11's, and it writes the CARRIED form from the row's own directory pair rather than
  gov's raw bytes. Stating only the `stale` half here is what made rev-3's version of this bullet
  false in exactly the case S11 exists for. Read the bullet as licensing a rung row onto the raw arm
  by either route and the destruction this unit exists to close comes straight back in through `-9`.
- **S4** — a delta row routes to `three_way` (`:2897`) ALWAYS and is never eligible for the
  raw-write arm again. `-7` already routes the predicate into the grid's OURS axis, so this is
  structural rather than a second branch; what this unit adds is the ASSERTION that it is
  structural, as a `selfcheck` arm over `VERDICT_GRID`.
- **S5** — a conflict on a delta row keeps today's behaviour exactly: the file is left
  byte-identical, an order is written under `.governance/outbox/`, and the row is an `r.fail`
  (`:3084-3095`).
- **S6** — `cmd_check`'s provenance loop reads `gov_oid` and its integrity loop reads `oid`, so a
  correctly merged target stops reporting as receipt corruption.
- **S7** — the selftest's unit-2 sequence gains a THIRD update over a three-vintage fixture, and a
  fourth, asserting the local line survives each one.

## 3. Non-goals (OUT)

- **Not** the `carry` rungs. A carried row still reads `oid != gov_oid` here and still routes to the
  three-way; what `-9` adds is the PROOF of which rung explains the difference and the reconciliation
  that proof enables. This unit must not pre-empt the ladder by guessing at one rung of it.
- **Not** strict mode. inCMS's policy that vendored kits carry zero local edits makes a delta row a
  violation rather than a merge, and that flag is keyed on the target descriptor. This unit makes
  the state expressible; it does not decide anyone's policy.
- **Not** a new verdict word. `VERDICT_GRID`'s vocabulary is untouched. The fix is which identity
  the OURS axis reads and what the merge branch stamps, not a fourth name for a row.
- **Not** a `--force`, `--theirs` or `--ours` escape, and not line-level partial application of a
  residual file. Both sit on the build's ratified cut list.
- **Not** re-stamping a `patched` row. A row nothing wrote keeps its `commit` and its `gov_oid`,
  because advancing them would make the receipt claim a vintage it never compared against and would
  move the base the next three-way merges from.
- **Land-alone:** no, and this is the one place it must be said plainly. `-8` lands on top of `-7`;
  on `9ddcc5c9` alone the two identity fields do not exist, so there is nothing to keep separate.
  Section 8's F3 records what that means for the red-first observation.

## 4. Design

### Data model

No new field. `-7` introduces `gov_oid` and `oid`; this unit fixes what each write branch puts in
them, and both branches are named in the table below.

| write branch | `oid` becomes | `gov_oid` becomes | `commit` |
|---|---|---|---|
| raw write, `stale` or `missing` (`:3069-3073`) | gov's blob at `to_commit` | gov's blob at `to_commit` | advances |
| three-way merged (`:3097-3099`) | the blob of the merged bytes | gov's blob at `to_commit` | advances |
| three-way conflicted (`:3084-3095`) | unchanged | unchanged | unchanged |
| `patched`, nothing written | unchanged | unchanged | unchanged |

The row's permanence falls out of the table rather than being enforced by a flag. A merged row's two
identities differ, so its OURS axis is `differs` forever, so it can only ever reach `patched` or
`diverged`, and both raw-write verdicts sit on the `equal` row of the grid. An adopter who later
reverts their edit by hand puts the index blob back to `gov_oid`, and the row rejoins the raw-write
arm on its own — which is exactly the behaviour a stored boolean would get wrong.

### Alternatives rejected

- *Stamp `sha256` with gov's bytes instead of the merge result — a one-line fix.* It does stop the
  destruction, and it breaks the other reader instead: the row would then claim the target holds
  gov's bytes at `commit` while it holds merged bytes, so `cmd_check`'s INTEGRITY loop reds every
  merged target forever. Measured in the mirror direction already, and it is the two-identity
  argument in miniature — one field cannot answer both questions whichever way you point it.
- *Store `has_local_delta: true` on the row.* A stored boolean about a comparison goes stale the
  moment either side moves, and the specific stale case here is an adopter who reverts their edit
  and is then merged against a base they no longer differ from, forever.
- *Refuse a delta row rather than merging it.* That is strict mode, which is a target-descriptor
  policy and not an engine default. Refusing by default would take the merge guarantee away from
  every adopter who wants it in order to serve the one who does not.
- *Keep the raw-write arm reachable and guard it with a check just before the write.* A guard that
  reads the same field the bug corrupts is disabled by the bug it exists to catch. Routing the
  predicate through the grid's axis means the arm is not reachable at all.

### Files touched (estimate)

`tools/govkit/govkit.py` (~20 lines), `tools/govkit/selftest.py` (~7 arms including two new fixture
vintages), and one `selfcheck` predicate.

## 5. Production-readiness checklist

- security — this is the security item. Silent destruction of an operator's edit in a repository gov
  does not own, reported as a successful write with zero conflicts, is the worst outcome this verb
  can produce, and it is reachable today by running the documented command twice.
- perf / scale — N/A: the same two blob reads per row, with one comparison changing operand.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a row whose `gov_oid` does not resolve at its `commit` refuses
  through the path `cmd_check` already uses for an unresolvable provenance blob, rather than falling
  back to a comparison against nothing.
- observability — a delta row now prints `diverged` where it printed `stale`, which is the operator
  visible change and is the point. The landing note names it, because a changed verdict word reads
  as drift otherwise.
- risks — the residual risk is a three-way that merges cleanly but wrongly, which `git merge-file`
  can do and this unit does not claim to detect. It is bounded by the conflict path being unchanged
  and by `-14`'s post-write verification, and it is strictly better than the current behaviour,
  which does not merge at all on the run that matters.
- testing + left-shift gates — the class is "a receipt field written by one side and read as the
  other", and AC5 gates it structurally over `VERDICT_GRID` rather than over the one row that
  exposed it.
- migration / rollback — `gov_oid` is STORED and trusted from the file, per the owner decision of
  2026-08-24 recorded in `-7` S3 and in F4 below; nothing recomputes it per run. It is DERIVED once,
  from `blob_at(root, row["commit"], row["source"])`, on the schema-2 to schema-3 upgrade `-7`
  performs, and that one derivation is what repairs a receipt already carrying a corrupted merge
  stamp: the corrupted `sha256` is carried into neither identity. From schema 3 onward the stored
  field is kept honest by `-7` S9's preamble assertion over every row that carries it, which refuses
  by name rather than repairing silently. An adopter whose edit was already destroyed is not
  recoverable by this unit, and the landing note says so.
- user docs — `WIRE-INTO-PROJECT.md`'s update section gains the sentence that a row with a local
  delta is merged on every subsequent update and is never overwritten.

## 6. Acceptance criteria

- **AC1** — The three-update sequence, over the three vintages of `tools/check-wiring.sh` at
  `24f39915`, `372e6b2a` and `9ddcc5c9`, with one line appended to the installed file. After
  `update --to 372e6b2a --write` the line is present; after the following `update --write` it is
  still present and the row is reported `diverged`, not `stale`. Observe RED first: measured
  2026-08-24 at `9ddcc5c9`, the second run reports `stale 2 · wrote 2, 0 conflict(s)` and `grep -c`
  for the line returns 0.
- **AC2** — On the merged row, `gov_oid` equals `git -C <gov> rev-parse 372e6b2a:tools/check-wiring.sh`
  while `oid` equals `git -C <target> hash-object` of the merged bytes, and the two differ. Observe
  RED first: at `9ddcc5c9` there is one field and it holds the merge result.
- **AC3** — `govkit.py check --target <t>` exits 0 immediately after the merged update. Observe RED
  first: measured, it prints `provenance: 1/2 resolved` and names the receipt hash that does not
  match gov's own bytes.
- **AC4** — Permanence across four updates. Inserting the `0f4d3084` vintage between `24f39915` and
  `372e6b2a` gives a fourth run, and `grep -c` for the local line returns 1 after every one of them.
  A guarantee asserted once is a guarantee asserted for one run.
- **AC5** — The structural gate. A `selfcheck` arm asserts that no `VERDICT_GRID` cell whose OURS
  key is `differs` maps to a verdict the write loop raw-writes. It reds when the grid is hand-edited
  to map `("differs", "differs")` to `stale`, and that failing case is observed before it lands.
- **AC6** — The no-regression arm, so the fix cannot quietly turn every update into a merge. A row
  with NO local delta whose gov copy moved still takes the raw write, and afterwards
  `git -C <target> cat-file blob :<path>` equals gov's blob at `--to`. The existing `u2a` fixture
  arm covers it and is asserted rather than assumed.
- **AC7** — `python tools/govkit/govkit.py selfcheck` exits 0 and `python
  tools/govkit/refusal_join.py` stays green, this unit adding one refusal branch for an unresolvable
  `gov_oid`.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest`, `govkit selfcheck`
and `refusal_join` legs. Adds arms, one standing `selfcheck` predicate and one refusal anchor; adds
no new leg file.

## 8. Open questions

- **F1 — on a successful merge, should `commit` advance to `to_commit`?** Yes, unchanged from
  today. `commit` names the gov vintage this row has been merged UP TO, `gov_oid` names the blob at
  that vintage, and leaving `commit` behind would re-merge an already-merged hunk on every later run.
  RESOLVED (agent, 2026-08-24, delegated): advance, under the full-scope approval.
- **F2 — should a `patched` row, a delta gov did not move, be re-stamped at the new `commit`?** No.
  Nothing was written, so nothing was compared at the new vintage, and the row's `commit` is the
  base the next three-way merges from. Advancing it silently moves that base.
  RESOLVED (agent, 2026-08-24, delegated): leave `patched` rows untouched.
- **F3 — the red-first observation lands after `-7`, so which tree is it observed against?** Both,
  and the spec is written to make that possible. rev-1 predicted that `-7` deliberately preserves
  the corruption under the new field names, so the sequence would reproduce identically on both
  trees. **rev-5: BUILDING MEASURED THE OPPOSITE, and the difference matters.** `-7` does leave the
  diverged arm stamping the merge result, but its S9 preamble integrity assertion then INTERCEPTS
  that stamp on the next run: at `9ddcc5c9` the second update reported `wrote 2, 0 conflict(s)`,
  rc 0, and the operator's line silently vanished, while on `-7`'s tip the same fixture refuses at
  rc 2 naming both oids, writes nothing, and can never be updated again. Silent destruction became
  a permanent brick. Both symptoms were reproduced end to end before the fix and both are recorded
  at the code site.
  RESOLVED (agent, 2026-08-24, delegated): observe on both, fix on `-7`'s tip.
- **F4 — is `gov_oid` stored in the receipt, or recomputed from `blob_at(root, commit, source)` on
  every read?** Stored. Recomputed was the rejected alternative, and the reason is `-13`: with
  `gov_oid` derived from `commit` at read time, `commit` alone would determine the base every row is
  compared and merged against, so `-13`'s `evidence: "pinned"` would assert nothing
  `evidence: "vintage-match"` does not already assert — there would be nothing pinned. The cost of
  storing it is a field that can go stale through a text merge of `install.json`, and that cost is
  paid by `-7` S9's per-row integrity refusal rather than absorbed.
  RESOLVED (owner, 2026-08-24): stored, with `-7` S9's per-row integrity refusal.
- **F5 — what relation must `--to` bear to the receipt's `gov_commit`?** A BACKWARDS `commit` is the
  rejected alternative. Today `:2940-2944` validates `--to` with `rev-parse --verify` and nothing
  compares it to `receipt["gov_commit"]`, so `update --to <older sha>` raw-writes every clean row
  backwards and rewinds `receipt["gov_commit"]` at `:3126`. This unit does not close that, and says
  so rather than leaving it implied: the two refusals — `--to` a descendant of the receipt's commit,
  and `--to` reachable from some ref — land in `-12`, each with its `refusal_join.py` arm.
  RESOLVED (agent, 2026-08-24, delegated): backwards rejected; both refusals are `-12`'s.

## 9. Revision log

- rev-5 · 2026-08-25 · built. §8 F3 predicted that `-7` preserves the corruption so the red-first
  sequence reproduces identically on both trees; measured, it does not. `-7` S9 intercepts the
  corrupt stamp and the second update REFUSES at rc 2 permanently rather than destroying the edit
  silently. F3's grounds are corrected and its resolution stands. §3's non-goal carries the same
  prediction and is corrected with it. Also recorded: S6's integrity half is deliberately NOT
  implemented, because repointing `check`'s integrity loop index-side would delete unit 5 AC2's
  unstaged-edit guarantee, and adding a second reader is what §10 forbids in the same sentence.
- rev-4 · 2026-08-24 · round-3 fold: S3's rev-3 sentence was FALSE in exactly the case `-9` S11
  exists for. It claimed a proven rung never re-opens the raw arm at `:3069-3073` because that arm
  sits on the grid's `equal` row — but the arm is guarded by `v == "stale" or v == "missing"`, and
  `missing` comes from the `absent` OURS row at `:2887-2888`, which a carried row the target DELETED
  does reach. S3 now closes both routes and hands the second to `-9` S11 by name.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold). Every cited
  line was opened at `9ddcc5c9`, and the destruction was reproduced rather than inferred: install,
  rewind, local edit, merge at `372e6b2a`, overwrite at `9ddcc5c9`, local line count 1 then 0. Two
  brief citations were slightly off and are corrected here — the merge stamp is `:3098` and not
  `:3096`, and the OURS comparison is `:2889` and not `:2886`. One fact the brief did not carry was
  found while reproducing and is folded into section 1 and into S6: the same overloaded field makes
  `govkit check` red immediately after a successful merge, with `provenance: 1/2 resolved`, so the
  corruption already has a second observable symptom today. One brief phrase was narrowed. The fix
  is described as routing a delta row to the three-way always, and the honest mechanism is that
  `-7` feeds the delta predicate into the grid's OURS axis, which makes the raw-write arm
  unreachable for such a row structurally rather than by a second guard.
- rev-2 · 2026-08-24 · folded the pre-code review: the migration line now matches the owner's
  decision that `gov_oid` is STORED rather than recomputed, naming the one derivation on the
  schema-2 upgrade as the repair path and `-7` S9's assertion as what keeps the stored field honest.
  §8 gains F4, which records recomputation as the rejected alternative and what it would cost
  `-13`'s `evidence: "pinned"`, and F5, which records a BACKWARDS `commit` as the rejected `--to`
  relation and points the two new refusals at `-12` rather than at this unit. S3 gains the
  one-sentence `-9` qualification, without which a builder reading this spec alone builds a grid in
  which no proven `carry` rung can ever take an automatic write.
- rev-3 · 2026-08-24 · round-2 fold: S3 is rewritten so the rung case is explicit rather than
  implied. A rung row reads `oid != gov_oid` like any other, is NOT a local delta in the
  adopter-edit sense, and reconciles through the three-way with `-9`'s rung already applied, so the
  raw-write arm stays closed on it. The bullet now cross-references `-9` instead of restating its
  base-and-theirs cancellation, and rev-2's closing clause is gone because a builder taking
  "no proven rung ever reaches an automatic write" literally builds exactly the raw-arm defect this
  unit closes. §3's matching non-goal is restated the same way so the two cannot drift, and §5's
  migration line is aligned with `-7` S9's field-presence scoping.

## 10. Reuse audit

Adds no seam and deletes none. `three_way` (`:2897`) stays the single merge primitive and keeps
delegating to `git merge-file`; `VERDICT_GRID` (`:2843`) and `UPDATE_ROLE` (`:2857`) are untouched
in both shape and vocabulary, which is what lets the fix be a change of operand rather than a new
branch. `gov_oid`'s bytes come from `blob_at` (`:2148`), the one function in this file that answers
"what did gov ship at a commit", rather than from a second reader. The conflict path reuses the
existing outbox order writer at `:3087-3094` unchanged, and the new refusal reuses `Refusal`
(`:78`) and `Report` (`:565`) under the standing `refusal_join.py` contract. `cmd_check`'s two loops
are re-pointed at the identity each already meant, so S6 removes an overload rather than adding a
reader. `classify_row` (`:2874`) keeps its signature, `planned_writes` (`:1359`), `resolve_entry`
(`:270`) and `target_context` (`:535`) are not reached by this unit at all, and the per-kit
`[check].argv` runner (`:1632-1652`) is untouched because it measures adoption rather than identity.
