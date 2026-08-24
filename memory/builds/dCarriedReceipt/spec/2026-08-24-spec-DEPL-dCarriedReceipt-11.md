# DEPL-dCarriedReceipt-11 — rename detection, and `withdrawn` stops deleting silently

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

## 1. Goal

`cmd_update` walks receipt rows and nothing else (`govkit.py:2970`). When gov renames a file inside a
claimed kit, that row's `source` stops resolving at `--to`, `classify_row` reports `t_state` `absent`,
`VERDICT_GRID` returns `withdrawn` (`:2846`), and the write loop unlinks the adopter's file (`:3076`),
`git rm`s it (`:3106`) and drops the row from the receipt (`:3082`, `:3109`). The replacement is never
landed, because no verb in this engine reconciles gov's planned destinations against a receipt during
an update. The run exits 0 and reports a clean deletion. The adopter is left holding a kit missing a
file, a runner leg whose argv was resolved at install time (`:2716`) and still names the deleted path,
and no receipt row through which anything could ever notice. That branch is also this engine's only
unguarded delete: it removes a tracked file from a repository gov does not own, with no flag and no
order.

## 2. Scope (IN)

- **S1** — one `git -C <gov> diff --find-renames --name-status <base_commit> <to_commit>` per run,
  producing a map from old source path to new source path over the `R` rows. It runs **unscoped**:
  pathspec-limiting the diff to the receipt's sources hides the destination half of every rename pair.
- **S2** — a receipt row whose `source` is an `R` old path takes a new verdict `renamed`, decided
  before `VERDICT_GRID` is consulted, so the `("equal","absent")` cell never sees it.
- **S3** — the new destination is recomputed through `resolve_entry` (`:270`) against the row's kit
  and the target's ctx, never by string-editing the old destination. A rename that crosses a rule
  boundary changes the descriptor's answer, and a string edit would land the file where the
  descriptor does not declare it.
- **S4** — under `--write`, a `renamed` row is performed as `git -C <target> mv <old> <new>` followed
  by a rewrite of the row's `path`, `source`, `commit` and `gov_oid`. Whether the row also takes BYTES
  is `-7`'s predicate and not this unit's: `oid != gov_oid` after the move means a local delta, the
  raw-write arm stays closed, and only the three-way applies.
- **S5** — the degrade path. When `--find-renames` finds no `R` pair for a source, the verdict stays
  `withdrawn` and nothing is invented. The similarity threshold is declared as a named constant at
  its one call site rather than left to git's default, so the value is reviewable.
- **S6** — `withdrawn` becomes report plus an outbox order under `--write`, in the shape `cmd_update`
  already writes at `:3087`. It stops unlinking, stops `git rm`-ing, and stops dropping the row.
- **S7** — a new `--write-withdrawals` flag, default OFF, is the only way a deletion is performed. It
  widens `parse_args` (`:3316`), which today returns a fixed 8-tuple.
- **S8** — `selftest.py` arms per branch, and a `refusal_join.py` arm for every refusal S4 and S7 add.

## 3. Non-goals (OUT)

- **Not** rename detection for COVERAGE. That sits on the build's ratified cut list, and the two are
  genuinely different questions: this unit reconciles a row the receipt already holds, while coverage
  asks about destinations the receipt never claimed. `-4` owns the second and must not inherit this.
- **Not** landing a file gov ADDED to a claimed kit. An addition has no `R` pair and no receipt row,
  so it is invisible here by construction. It is a coverage gap and `-4` reports it.
- **Not** re-emitting the target's gate legs at the new path. `update` does not own leg emission —
  role `gate-leg` dispatches to `refuse` today (`:2865`) and to `report` after `-2` — so a stale leg
  argv is REPORTED by this unit and repaired by the operator or by a later `apply`. Silently
  rewriting a target's runner during an update creates a second writer for a file `apply` owns.
- **Not** a `--force`. `--write-withdrawals` is a scope flag rather than an escape hatch: it enables
  a narrower class of action, defaults OFF, and overrides no refusal. A flag that overrode a refusal
  would be the banned shape.
- **Land-alone:** this unit needs `-7` beneath it, because S4's byte decision is stated in `-7`'s two
  identities. With `-7` landed it stands alone and leaves both trees green.

## 4. Design

### Data model

No new receipt field. `renamed` is a verdict, and the rename map is per-run state. The row's `path`
and `source` are rewritten in place, which is what makes the next run's classification correct.

### Migration

None. A receipt written before this unit reads identically after it. The first update following a gov
rename is where behaviour differs, and it differs by not destroying anything.

### Alternatives rejected

- *Derive the new destination by substituting the renamed segment into the old destination.* It is a
  second answer to "where does this file land", and `-1` exists because this file already paid for
  one of those. `resolve_entry` is the answer `apply` uses.
- *Keep the delete and just add an order.* An order describing a file already unlinked and `git
  rm`-ed is a report about damage rather than a guard against it.
- *Treat a low-similarity rename as a delete-plus-add and land the new file anyway.* That is
  attribution by guess: the new file has no receipt row, so its `gov_oid` would be invented, which is
  exactly the inversion `-13` refuses. Falling back to `withdrawn` and writing nothing is honest.
- *Detect renames across the whole `--all` graph.* The diff is between two named commits by design,
  and reaching outside them is how a base nobody asked for gets selected.

### Files touched (estimate)

`tools/govkit/govkit.py` (~70 lines, across `cmd_update`, `parse_args`, `USAGE` and `main`),
`tools/govkit/selftest.py` (6 arms), one fixture that renames a claimed engine file in a scratch gov.

## 5. Production-readiness checklist

- security — this unit removes the engine's only unguarded delete of a tracked file in a repository
  gov does not own. That is the change's main safety content, not a side effect of the rename work.
- perf / scale — one extra `git diff` per run, between two commits already resolved. Negligible
  against the per-row `git show` the classifier already performs through `blob_at` (`:2148`).
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a rename whose new destination the target already holds is a
  refusal by name rather than an overwrite, and a `git mv` that fails leaves the row unmodified and
  is reported rather than half-applied.
- observability — `renamed` and `withdrawn` each print a row and are counted by the existing tally;
  the withdrawn order names the file, its last gov commit, and why nothing was deleted.
- risks — the residual risk is a rename git scores below threshold, which degrades to `withdrawn` and
  therefore to a report. That is a coverage gap rather than a data-loss path, and it is the direction
  the degrade is deliberately chosen to fail in.
- testing + left-shift gates — six `selftest.py` arms, the RED-first observation being AC1. The class
  gated is "a verdict deletes a tracked file", asserted as AC6: no `update` run without
  `--write-withdrawals` may reduce the target's tracked-file count.
- migration / rollback — none on disk. Reverting the unit restores the old behaviour without touching
  any receipt.
- user docs — `WIRE-INTO-PROJECT.md`'s update section gains the two dispositions and the flag, stated
  as "deletion is opt-in".

## 6. Acceptance criteria

- **AC1** — In a fixture where gov renames a claimed `engine` file between `base_commit` and `--to`,
  `govkit.py update --write` at `9ddcc5c9` unlinks the target's copy, drops its row from
  `install.json`, lands nothing at the new path, and exits **0**. Observe this RED first; it is the
  defect.
- **AC2** — After the change, the same fixture prints `renamed`, `git -C <target> status --porcelain`
  shows an `R` entry, and the receipt row's `path` and `source` both carry the new spelling.
- **AC3** — A rename whose similarity falls below the declared threshold produces no `R` pair, the
  verdict is `withdrawn`, the file is still on disk (`test -f <path>`), and its row is still in
  `install.json`.
- **AC4** — With `--write-withdrawals` supplied, that same withdrawn row is deleted, `git -C <target>
  ls-files -- <path>` prints nothing, and the run writes an order under `.governance/outbox/`.
- **AC5** — A `renamed` row whose target copy carries a local delta (`oid != gov_oid` per `-7`) is
  moved and then three-way merged: `git -C <target> show :<new-path>` is not byte-identical to
  `blob_at(root, to_commit, <new-src>)`, which is what proves no raw write occurred.
- **AC6** — Across `update --write` in the AC3 fixture, `git -C <target> ls-files | wc -l` is
  unchanged — the standing predicate that no run without `--write-withdrawals` deletes anything.
- **AC7** — `python tools/govkit/refusal_join.py` exits 0, with every refusal branch this unit adds
  reached by a named arm.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs, plus `tools/govkit/refusal_join.py`, whose declared contract is that each added
refusal branch has an arm. Adds six arms and one standing predicate; adds no new leg file.

## 8. Open questions

- **F1 — should `--write-withdrawals` be a per-run flag or a `deploy.toml` field?** Per-run. A
  descriptor field is a standing authorization, and the whole reason this unit exists is that a
  deletion happened without anyone deciding it once, let alone standing.
  RESOLVED (agent, 2026-08-24, delegated): per-run flag, under the full-scope approval.
- **F2 — what similarity threshold?** git's default 50%, declared as a named constant rather than
  left implicit. Nothing measured here justifies a different number, and an undeclared default is a
  value nobody can review.
  RESOLVED (agent, 2026-08-24, delegated): 50%, named at its call site.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold). The withdrawn
  branch, the receipt-rows-only loop and the install-time leg-argv resolution were each read in source
  at `9ddcc5c9`. **Brief correction:** the brief cites `:3078` for the silent delete; that line is
  `deleted.append`, the branch spans `:3075-3082`, and the row is actually dropped at `:3109`. The
  cited defect is real at those lines.

## 10. Reuse audit

`resolve_entry` (`:270`) is the existing destination seam and this unit calls it rather than deriving
a second spelling — the duplicate-answer class `-1` closes, which this unit must not re-open one level
down. The outbox order reuses the path and format `cmd_update` already writes for a three-way conflict
(`:3087-3093`). The verdict tally reuses the existing counter rather than adding a second. No new seam
is created: the rename map is per-run local state inside `cmd_update`, and the byte decision is
delegated to `-7`'s two identities rather than re-derived here.
