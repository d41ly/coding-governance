# DEPL-dRatifiedSeam-1 — the tracked-count invariant admits additions, and `update` lands a new source

**Status:** OPEN · rev-3 · 2026-09-03 · node d · Tier-2 · base 7c6f3eb7 · streams deployer · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`govkit update` cannot land a gov source the target has no receipt row for, because a standing
predicate asserts the target's tracked-file count never changes on a run without
`--write-withdrawals`. The capability is already built and measured; the owner ruled
(`DEPL-dRetiredFork-13`) that the invariant is superseded rather than routed around. This unit
changes the predicate and lands the half that was held back.

## 2. Scope (IN)

- **S1** — Change the standing predicate from *unchanged* to *never FALLS*. A run without
  `--write-withdrawals` may add tracked files and may never remove one. The assertion stays an
  assertion: this is a direction change, not a deletion. The ruling names this explicitly.
- **S2** — Audit the other three tracked-count sites in `tools/govkit/selftest.py` and give each
  the same treatment or a stated reason it differs. Grounding measured exactly four; a change that
  fixes one and leaves three is the could-not-fail shape one level up.
- **S3** — WRITE the new-source landing path: `update` writes a gov source the target has no
  receipt row for, and records it. **The code does not exist yet.** `DEPL-dRetiredFork-2`
  diagnosed, built and MEASURED it in a working tree and then committed none of it — its own
  commit `cf97f3bc` says so: "diagnosed, built, measured working, and NOT landed". Only the
  `--kits` scope fix landed. So the diagnosis is reusable and the implementation is not.
- **S4** — A NEW arm asserting the direction that still binds: a run without
  `--write-withdrawals` that REMOVES a tracked file must still red. Without this, S1 relaxes the
  predicate into a check that cannot fail, which is the class `dRetiredFork` spent fifteen units
  removing.
- **S5** — The nineteen cascade failures are re-run and each is dispositioned: fixed by S1, a real
  defect S3 must address, or a fixture that needs updating. A cascade is not a verdict; each arm
  gets an answer.

## 3. Non-goals (OUT)

- Any write into an adopter tree. `DEPL-dRetiredFork-14` ruled that the adopter performs their own
  write on their own timing, and this unit does not revisit it.
- `--write-withdrawals` semantics. The removal path is untouched; only the addition direction moves.
- The separate-verb design the run recommended and the owner declined. It is recorded in
  `DEPL-dRetiredFork-13` so the trade-off stays legible, and it is not built here.
- Re-auditing `DEPL-dCarriedReceipt-11`'s other `[-11]` arms — renames, refusals, seed rows, AC10
  and AC11 — which share the tag and not the subject.

## 4. Design

### Data model

No new shapes. The predicate is one `check(...)` in `tools/govkit/selftest.py` comparing
`len(_files_before)` against `len(_files_after)`, both `git ls-files` snapshots taken either side
of the write run.

### The change

`len(before) == len(after)` becomes `len(after) >= len(before)`, plus S4's new arm asserting that a
removal still reds. The pair is what keeps the predicate a predicate: one direction relaxed, the
other newly and explicitly bound.

### Rollout

S1, S2 and S4 land together — relaxing without S4 leaves a window where nothing grades removals.
S3 lands after, because it is the change that exercises the relaxed direction.

### Alternatives rejected

A separate verb or an opt-in flag, which is what the run recommended on the grounds that this
verb's failure mode is silent data loss in a repository gov does not own. The owner chose to
supersede the invariant instead. Recorded, not relitigated.

### Files touched (estimate)

`tools/govkit/selftest.py` (one predicate, three audited sites, one new arm),
`tools/govkit/govkit.py` (the new-source landing path, WRITTEN HERE — see S3; rev-1 of this
spec claimed it was already written and that was wrong), and `DEPL-dRetiredFork-2`'s spec status.

## 5. Production-readiness checklist

- security — the relaxed direction lets `update` ADD files to a tree gov does not own. S4 is the
  compensating bound; the removal direction, which is the destructive one, stays asserted.
- perf / scale — N/A: two `git ls-files` snapshots already taken.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a landing whose destination already exists must refuse rather
  than overwrite; `DEPL-dRetiredFork-2`'s measurement already reported 8 rows correctly
  not-landed and that behaviour must survive.
- observability — every landed source prints a row naming it and its gov vintage, so an addition
  is visible in the run output rather than only in `git status` afterwards.
- risks — the real one is S1 without S4: a predicate relaxed in both directions grades nothing,
  and it would read as green forever.
- testing + left-shift gates — `python tools/govkit/selftest.py`, plus S4's new arm, plus the
  nineteen cascade arms dispositioned under S5.
- migration / rollback — none: no stored shape changes.
- user docs — `WIRE-INTO-PROJECT.md` gains a line only if the landing becomes operator-visible.

## 6. Acceptance criteria

- **AC1** — When the `[-11]` fixture's write run ADDS a tracked file — an arm S1 must create,
  because no arm adds one today and the relaxed direction is otherwise never taken —
  `python tools/govkit/selftest.py` exits 0 rather than failing the standing predicate.
- **AC2** — When a write run without `--write-withdrawals` REMOVES a tracked file, that same
  command exits non-zero, naming the removal. Observed by staging the break and reverting.
- **AC3** — When `grep -nE "tracked-file count|tracked_before|tracked_after"` runs over
  `tools/govkit/selftest.py`, it reports the same FOUR sites grounding measured, and each one's
  comparison operator is `>=` or is named in this unit's ledger with the arm that proves its
  different direction still fails. A comment alone does not satisfy this: the ledger row must
  cite an arm, because a criterion a comment can answer is the class this build closes.
- **AC4** — When `govkit update --write` runs against a fixture holding a gov source with no
  receipt row, the source is written and reported, and a row appears in `install.json`.
- **AC5** — When the same run meets a destination the target already holds, it REFUSES rather than
  overwriting, and the fixture target's receipt is unchanged for that row. The receipt path is
  named in `tools/govkit/govkit.py` rather than spelled here: it is generated INSIDE an adopter
  at install time and gov tracks no such file, so citing it as a repo path is a citation that
  resolves to nothing.
- **AC6** — When `python tools/govkit/selftest.py` is re-run, ZERO arms fail. The nineteen
  cascade arms are each named in this unit's ledger with what resolved them, but the criterion
  is the exit status, not the prose: a disposition written beside a still-failing arm satisfies
  nothing.
- **AC7** — `python tools/govkit/selftest.py` and `python tools/govkit/govkit.py selfcheck` both
  exit 0.
- **AC8** — `bash tools/run-gates/run-gates.sh` is green, AND its `govkit selftest` and
  `govkit acceptance matrix` legs are among the legs that RAN rather than being skipped by a
  guard. A bare green bar is the unrelated-green-gate shape `memory/TEMPLATE-SPEC.md` forbids;
  what makes it an observation of THIS change is that the legs grading this diff executed.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · `memory hygiene`

## 8. Open questions

- **F1 — does S3's landing need `--write-withdrawals`' symmetry, an explicit opt-in of its own?**
  The ruling supersedes the unchanged-count invariant but says nothing about whether ADDING should
  itself be opt-in. Recommendation: no. The ruling's plain reading is that `update` reconciles, and
  a second flag would rebuild the separate-verb design the owner declined.
- **F2 — what happens to a cascade arm that fails for a REAL reason S3 must fix?** Recommendation:
  it becomes a defect this unit fixes, not a disposition. S5 exists to tell the two apart, and the
  answer is only cheap if the arms are read rather than counted.

## 9. Revision log

- rev-1 · 2026-09-03 · initial draft. Scope corrected from the ruling's "nineteen arms" by the
  grounding measurement: four tracked-count sites, one standing predicate, nineteen cascade
  failures downstream of a single write run.
- rev-2 · 2026-09-03 · S3 and §4 corrected. rev-1 said the new-source landing path was "already
  written for `DEPL-dRetiredFork-2`" and it is NOT: `grep` for its reporting text over
  `tools/govkit/govkit.py` returns 0 at HEAD, `git log -S` finds it in no commit, and that
  unit's own commit message states it was built and not landed. A builder reading rev-1 would
  have gone looking for code that does not exist. Found by the M4 audit — by hand, because the
  agent fan died whole on a 529 and returned an empty finding list that read like a clean pass.
- rev-3 · 2026-09-03 · folded four M4 findings against this spec's own acceptance, every one
  verified against the tree. AC1's antecedent was never exercised: no fixture arm adds a tracked
  file, so it could pass with the relaxed direction untaken. AC3 and AC6 were SELF-GRADED — each
  admitted a comment or a ledger sentence as its answer, which is the gate-satisfied-by-its-own
  -prose class this build spent fifteen units removing, appearing in the acceptance of the spec
  that removes it. AC8 was a bare green bar, which `memory/TEMPLATE-SPEC.md` names as the
  unrelated-green-gate shape. The audit was self-review: the cold reviewers all died on server
  529s, and self-review of one's own spec is the weaker instrument, so a cold M4 pass is still
  owed and is not claimed here.

## 10. Reuse audit

**Probe result.** `python tools/codebase-map/reuse_lookup.py "selftest arm asserting a tracked file
count invariant"` returns `tracked` (`tools/govkit/govkit.py`, fan-in 7, SEAM) and `cmd_selftest`
(`tools/memory-tree/row_grammar.py`, fan-in 4, SEAM). Neither is a seam this unit extends: the
change is one assertion's direction inside an existing arm, and the landing path was already
written for `DEPL-dRetiredFork-2`. No new seam is created and none is needed.

**Recall terms used:** `standing predicate tracked-file count unchanged withdrawals update receipt
landing govkit selftest arms invariant`, and `withdrawals removal tracked count invariant establish
unit deployer update receipt rows silent data loss adopter`. The second located
`memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-11.md`, which is where the
invariant was established and which records that the unit removed the engine's only unguarded
delete of a tracked file in a repository gov does not own — the reason the removal direction must
stay bound when the addition direction is relaxed.
