# DEPL-dCarriedReceipt-11 — rename detection, and `withdrawn` stops deleting silently

**Status:** SPECCED · rev-5 · 2026-08-25 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

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

- **S0** — the two vintages this spec names, disambiguated once. `base_commit` is the PER-RUN field,
  `receipt.get("gov_commit")` read at `:2938`, and it bounds the one rename diff S1 takes. A ROW's
  base is `row["commit"]`, which a partial earlier update can leave behind the run's. Everywhere below
  that says `blob_at(root, base_commit, <old source>)` means the ROW's base, `row["commit"]` — a
  per-run vintage would compare a row against a tree it never came from, which is the class `-13` S3
  refuses on the read side. S1 is the only per-run use in this spec.
- **S0b** — `renamed` is computed for every role that REACHES classification, and only `how ==
  "table"` performs it. The verdict word and the write are two different questions, and an earlier
  rev conflated them into a bullet that scoped the verdict out and then edited a print tuple the
  scoping made unreachable — a branch that cannot fire, which this build's own gate discipline
  forbids. The three call sites, each verified at `9ddcc5c9`:
  - `skip`-dispatched roles (`project-owned`, `generated`) `continue` at `:3006-3008`, **before**
    `classify_row`. They never take any verdict, never enter `acted`, and no edit in the write loop
    can reach them. That is correct and this unit does not change it.
  - Every row that does reach `acted` is printed at `:3024`, one line before `acted.append` at
    `:3025`. So a renamed row NEVER vanishes from the run's output — the claim an earlier rev made
    here was simply false — and the write loop's line is a SECOND line, not the only one.
  - `renamed` is added to the reported-only tuple at `:3064`, so a non-`table` role that reaches the
    write loop gets that second line naming what was not written, rather than falling through
    `("missing", "stale", "withdrawn", "diverged")` to the bare `continue`.
- **S0c** — `renamed` is EXEMPT from the seed override at `:3016-3020`, added beside `"missing"` in
  the same change. This is the sharpest thing in the unit and it was found by walking the composed
  design rather than the diff. That override rewrites any non-`missing` verdict on a `seed` or
  `report-reseed` row to `current`/`patched`. Without the exemption a seed row whose gov source gov
  RENAMED classifies `t_state = "absent"` → `withdrawn` (`:2846`) → **rewritten to `current`** — the
  run reports the row healthy while the source behind it no longer exists, which is a silent-green of
  exactly the kind the comment at `:3054-3058` records a measured incident for. This unit does not
  become its sequel.
- **S1** — one `git -C <gov> diff --find-renames --name-status <base_commit> <to_commit>` per run,
  producing a map from old source path to new source path over the `R` rows. It runs **unscoped**:
  pathspec-limiting the diff to the receipt's sources hides the destination half of every rename pair.
- **S2** — a receipt row whose `source` is an `R` old path takes a new verdict `renamed`, decided
  before `VERDICT_GRID` is consulted, so the `("equal","absent")` cell never sees it.
- **S3** — the new destination is recomputed through `resolve_entry` (`:270`) against the row's kit
  and the target's ctx, never by string-editing the old destination. A rename that crosses a rule
  boundary changes the descriptor's answer, and a string edit would land the file where the
  descriptor does not declare it.
- **S4** — under `--write`, a `renamed` row is performed as `git -C <target> mv <old> <new>`, and the
  row's `path`, `source`, `commit` and `gov_oid` are rewritten TOGETHER, never one without the others.
  The BYTE outcome is decided by this unit, and it is decided BEFORE the move, against the OLD source,
  because `git mv` moves bytes unchanged. A row whose pre-move `oid` equals `blob_at(root,
  base_commit, <old source>)` (`:2148`) carries NO local delta: it takes the ordinary write of gov's
  blob at `to_commit` for the NEW source, and `commit` and `gov_oid` advance together with it.
  Deferring the question to a post-move comparison is a FREEZE, not a deferral — `gov_oid` would be
  gov's blob at the new path while `oid` is still the old content, so `oid != gov_oid` for a row
  nobody edited, `-8` closes the raw-write arm, the three-way runs with `base == theirs`, `git
  merge-file` returns ours, and the file sits at pre-rename content forever while the run prints
  `patched`, which is `VERDICT_GRID`'s word at `:2847` for an adopter edit that never happened.
  Leaving `commit` at `base_commit` instead is the other bad end: `gov_oid` then cannot resolve at the
  new source and `-8`'s integrity refusal fires on a row this unit just wrote.
- **S5** — only a row whose pre-move `oid` ALREADY differed from `blob_at(root, base_commit, <old
  source>)` carries a delta into the rename. That row keeps the raw-write arm closed per `-8` and
  takes the three-way, with `base` = gov's blob at `base_commit` for the OLD source and `theirs` =
  gov's blob at `to_commit` for the NEW source, so gov's semantic change lands and the adopter's edit
  survives. `patched` is therefore never printed for a renamed row that carried no delta.
- **S6** — a performed rename records BOTH spellings in a per-run `renamed` list, in the shape
  `changed` and `deleted` already take at `:3074` and `:3078`. `git mv` stages both, so this list is
  not a second `git add`: it exists because `-14`'s pre-write snapshot and touched-kit predicate read
  those lists, and a renamed row is invisible to both through `changed`/`deleted` alone.
- **S7** — the degrade path. When `--find-renames` finds no `R` pair for a source, the verdict stays
  `withdrawn` and nothing is invented. The similarity threshold is declared as a named constant at
  its one call site rather than left to git's default, so the value is reviewable.
- **S8** — `withdrawn` becomes report plus an outbox order under `--write`, in the shape `cmd_update`
  already writes at `:3087`. It stops unlinking, stops `git rm`-ing, and stops dropping the row.
- **S9** — a new `--write-withdrawals` flag, default OFF, is the only way a deletion is performed. It
  widens `parse_args` (`:3316`), which today returns a fixed 8-tuple.
- **S10** — `selftest.py` arms per branch, and a `refusal_join.py` arm for every refusal S4 and S9 add.
  The byte outcome S4 and S5 decide is asserted by AC8 and AC9, not left to the rename arms.
- **S11** — the rung intersection. A row carrying a `-9` `carry` rung ALWAYS differs from gov's
  blob at the old source, so S5's "already differed" branch takes every carried row in a renamed kit
  — with an UN-carried `base`, which is the one input a rung exists to correct. On such a row the
  rung is applied to `base` and to `theirs` exactly as `-9` S6 does, BEFORE this unit's comparison,
  at the two vintages and the two sources S5 already names: the OLD source at `base_commit` and the
  NEW source at `to_commit`. S5's delta question is then asked against the rung-applied blob — a row
  whose bytes equal the rung applied to `blob_at(root, base_commit, <old source>)` carries no delta
  BEYOND the rung — and it still takes the three-way rather than S4's ordinary write, because a
  proven rung never opens the raw-write arm (`-9` S9) and a raw write here would land gov's spelling
  at the new path. The row is stamped per `-9` S12. The ladder, the derivation and the stamping rule
  are `-9`'s and are not restated here. This item is INERT until `-9` is beneath this unit: with no
  rungs there are no carried rows and the branch is unreachable, so it forces no landing order in
  either direction and its arm lands with whichever of the two is second (§8 F3).

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
`tools/govkit/selftest.py` (9 arms, the ninth being S11's and landing with `-9`), one fixture that
renames a claimed engine file in a scratch gov and one that renames it AND changes its content in
the same range.

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
- testing + left-shift gates — nine `selftest.py` arms, the RED-first observation being AC1. The
  class gated is "a verdict deletes a tracked file", asserted as AC6: no `update` run without
  `--write-withdrawals` may reduce the target's tracked-file count. The ninth arm is S11's carried
  rename, gated as "a rename compared against an un-carried base", and it lands with `-9`.
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
- **AC8** — the clean rename that also changes CONTENT. In a fixture where gov both renames a claimed
  `engine` file and edits it between `base_commit` and `--to`, with the target's copy byte-identical
  to `blob_at(root, base_commit, <old source>)`, `update --write` leaves `git -C <target> show
  :<new-path>` byte-identical to `blob_at(root, to_commit, <new source>)`, and the row's `commit` and
  `gov_oid` both carry the `--to` vintage afterwards. This is the arm that fails against a draft
  which moves the file and stamps the row forward without writing gov's new bytes.
- **AC9** — no renamed row reports `patched` without an adopter edit. In the AC8 fixture the printed
  verdict is `renamed` and the string `patched` appears nowhere in the run's output; the row's stored
  `sha256` equals `_sha` of gov's blob at `to_commit`, not of the pre-rename content. The class gated
  is `VERDICT_GRID`'s `("differs","equal")` cell at `:2847` naming a divergence the target never
  created.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs, plus `tools/govkit/refusal_join.py`, whose declared contract is that each added
refusal branch has an arm. Adds nine arms and one standing predicate; adds no new leg file.

## 8. Open questions

- **F1 — should `--write-withdrawals` be a per-run flag or a `deploy.toml` field?** Per-run. A
  descriptor field is a standing authorization, and the whole reason this unit exists is that a
  deletion happened without anyone deciding it once, let alone standing.
  RESOLVED (agent, 2026-08-24, delegated): per-run flag, under the full-scope approval.
- **F2 — what similarity threshold?** git's default 50%, declared as a named constant rather than
  left implicit. Nothing measured here justifies a different number, and an undeclared default is a
  value nobody can review.
  RESOLVED (agent, 2026-08-24, delegated): 50%, named at its call site.
- **F3 — a renamed row that also carries a `-9` rung: whose question is the rung, and where does it
  get applied?** `-9` owns the ladder; this unit applies it, before the rename comparison. The
  intersection was owned by nobody through rev-2 and it is not hypothetical: a `relocate` row's bytes
  never equal gov's blob at the old source, so S5's branch is where every carried row in a renamed
  kit lands, and S5 as written hands it a `base` still spelling gov's prefix. Deferring to `-9`
  instead is worse, because by the time it sees the row the `path` and `source` have been rewritten
  and the old-source base S5 named no longer exists on the row. Not an ORDER: with `-9` unlanded
  there are no rungs and S11 is unreachable, and with `-11` unlanded there is no rename to compare,
  so neither unit blocks the other and the arm lands with whichever is second.
  RESOLVED (agent, 2026-08-24, delegated): the rung is applied to `base` and `theirs` per `-9` S6
  before the rename comparison and the row is stamped per `-9` S12, stated as S11 here and not
  restated as a second ladder.

## 9. Revision log

- rev-5 · 2026-08-25 · round-5 fold: S0b was self-contradicting and its mechanism was false
  against source — it scoped `renamed` out of the write loop and then edited a tuple the scoping
  made unreachable, and claimed a renamed row would vanish from the output when every row in
  `acted` prints at `:3024`. Rewritten against the three real call sites. New S0c exempts
  `renamed` from the seed override at `:3016-3020`: without it a seed row whose gov source was
  RENAMED prints `current`.
- rev-4 · 2026-08-24 · round-4 fold: the two vintages this spec names are disambiguated in a new
  S0 — `base_commit` is the PER-RUN receipt field bounding S1's one diff, while every per-ROW
  comparison means `row["commit"]`. And S0b scopes `renamed` to `how == "table"` and ADDS it to
  the write loop's reported-only tuple at `:3060`: a new verdict word falls through that tuple to
  a bare `continue`, so a `rendered` or `project-owned` row whose gov source moved would have
  vanished from the run's output.
- rev-3 · 2026-08-24 · round-2 fold: the rename-by-rung intersection, which no unit owned. S11
  states it — a carried row ALWAYS differs from gov's blob at the old source, so S5's branch takes
  every one of them, and the rung is applied to `base` and `theirs` per `-9` S6 before the rename
  comparison, with the row stamped per `-9` S12 — and §8 F3 records why it lives here rather than in
  `-9` and why it forces no landing order. The arm count goes 8 to 9.
- rev-2 · 2026-08-24 · folded the pre-code review: the renamed row's BYTE outcome is now stated
  rather than deferred. S4 decides it BEFORE the move against the OLD source — a pre-move `oid`
  equal to `blob_at(root, base_commit, <old source>)` is no delta and takes the ordinary write of
  gov's blob at `to_commit` for the NEW source, with `commit` and `gov_oid` advancing together —
  because deferring it freezes the file at pre-rename content while printing `patched`, and leaving
  `commit` behind instead trips `-8`'s refusal. S5 keeps the three-way for a row that ALREADY
  differed, S6 records both spellings in a `renamed` list so `-14`'s snapshot and touched-kit
  predicate have a population to read, the old S5–S8 renumber to S7–S10, and AC8 and AC9 assert the
  clean-rename-with-content-change outcome and that no renamed row reports `patched` without an
  adopter edit.
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
is created: the rename map is per-run local state inside `cmd_update`, and the byte decision is still
expressed in `-7`'s two identities and `blob_at` (`:2148`) rather than in a comparison of its own —
S4 fixes only WHICH vintage and WHICH source path each identity is read at, which is the one question
a rename asks and which nothing else in this engine answers. The `renamed` list S6 records reuses the
shape of `changed` and `deleted` rather than introducing a third collection kind.
