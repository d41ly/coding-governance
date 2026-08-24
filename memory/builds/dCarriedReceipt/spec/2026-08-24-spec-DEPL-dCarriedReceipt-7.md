# DEPL-dCarriedReceipt-7 — two identities, read index-side

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

## 1. Goal

One receipt field is asked to be two different things at once. `classify_row` (`govkit.py:2874`)
compares `sha256` against the target's WORKTREE bytes — `dp.read_bytes()` at `:2884`, the comparison
at `:2889` — while `cmd_check`'s provenance loop compares that same field against GOV's blob at the
row's `commit` (`:1522-1531`). Both claims can hold only where the target's worktree bytes are
byte-identical to the blob gov shipped, and that is false for any adopter whose clone applies a
line-ending filter.

Measured here on 2026-08-24 at `9ddcc5c9`. A scratch target takes `govkit.py apply --kits
memory-tree`, which lands 24 files and writes 28 rows, and `update` against it reports `current 24 ·
missing 3`. The same target cloned with `git clone -c core.autocrlf=true` reports `current 1 ·
missing 3 · patched 23`. Twenty-three of twenty-four engine rows read as locally modified because
the worktree holds CRLF and gov shipped LF. The one survivor is the single path that kit's `lf_pin`
block governs, and the shipped kits declare four `lf_pin` patterns across twelve registry entries,
so nothing govkit installs makes an adopter immune. An adopter on a default Windows clone therefore
reads about 96% false divergence, achieves zero automatic adoption, and is shown a plausible table
while it happens.

The fix is the two identities. `gov_oid` is the git blob gov shipped at the row's `commit`, and it
means that forever. `oid` is the git blob the TARGET holds, read from its INDEX and never from its
worktree. `sha256` is retained so a schema-2 reader keeps working, and stops being the comparator.

## 2. Scope (IN)

- **S1** — every receipt row gov writes carries `gov_oid` and `oid`, both git blob oids. `sha256` is
  still written, is still what `install.sums` lists, and decides no verdict.
- **S2** — `classify_row` reads ours as the target's INDEX blob, from one batched
  `git -C <target> ls-files -s -z --` over the receipt's paths, rather than `read_bytes` at `:2884`.
  `theirs` and `base` keep `blob_at` (`:2148`), which is already index-side by construction.
- **S3** — the OURS axis compares that index blob against the row's `gov_oid`, not against `sha256`.
  `oid != gov_oid` is the local-delta predicate, evaluated per run, stored as no boolean anywhere.
- **S4** — a receipt-claimed path that is tracked in the target but carries no index entry is a
  REFUSAL naming the path. Without it the index read's own `absent` routes to `missing` and then to
  the raw write at `:3069`, which would overwrite whatever untracked file the operator has there.
- **S5** — writes go `git hash-object -w --stdin`, then `git update-index --cacheinfo`, then
  `git checkout-index -f --`, so the TARGET's own filters decide its worktree bytes. The mode comes
  from the row's existing index entry, and from gov's tree entry at `commit` for a row with none.
- **S6** — `RECEIPT_SCHEMA` goes 2 to 3 (`:39`) and readers accept 1, 2 and 3. The schema-1
  role-distrust arm keeps its `schema < 2` bound and keeps firing.
- **S7** — `cmd_apply` records both identities: `gov_oid` from the blob it wrote, and `oid` read
  from the index after the `git add` it already performs at `:2477`.
- **S8** — one selftest arm per acceptance criterion, plus the class gate AC6 describes.

## 3. Non-goals (OUT)

- **Not** the `carry` rungs. The `verbatim` / `eol` / `relocate` ladder and its needle map are
  `-9`'s. This unit makes the two identities readable and leaves any difference a plain local delta.
- **Not** changing what the merge branch stamps. `:3097-3098` keeps writing the merge result into
  BOTH identities under this unit, so the corruption is renamed rather than fixed. That is
  deliberate: `-8` owns the fix, and `-8`'s red-first observation must survive this unit landing.
- **Not** dropping `sha256`. It is read by `cmd_check`'s sidecar join (`:1544-1556`) and it is what
  `install.sums` carries, so removing it is a migration nobody asked for.
- **Not** normalizing, renormalizing or re-pinning the target's `.gitattributes`. A target whose
  pins are wrong is `-2`'s `pins` disposition and the operator's decision, and `lf_pins` (`:1805`)
  is untouched here.
- **Not** repairing the exec bit on rows `apply` already landed. This unit needs a mode to call
  `update-index` at all; it does not claim to fix what earlier installs wrote.
- **Land-alone:** yes. Its fixture selects `check-wiring`, which declares no `lf_pin` and therefore
  produces no `attributes` row, so this unit does not need `-2` green to observe its acceptance.

## 4. Design

### Data model

| field | means | written by | read by |
|---|---|---|---|
| `gov_oid` | the blob gov shipped at this row's `commit` | `apply`, `update` | the OURS axis, and `check`'s provenance loop |
| `oid` | the blob the target's index held when the row was last written | `apply`, `update` | `check`'s integrity loop |
| `sha256` | sha256 of gov's bytes at install | `apply`, `update` | `install.sums` and its join, and no verdict |

The live delta predicate reads the target's CURRENT index blob and compares it to `gov_oid`. The
stored `oid` is that same quantity as of the last write, which is how `check` sees a change nobody
recorded. Two questions, two fields, and neither field answering both is the whole unit.

Feeding the predicate into the grid's OURS axis is what keeps `VERDICT_GRID` (`:2843`) untouched.
Identities that agree give `equal`, which is the only axis value the raw-write verdicts sit on.
Identities that differ give `differs`, which reaches only `patched` and `diverged`.

### Alternatives rejected

- *Normalize line endings before hashing.* A rewrite rule with no proof behind it, forbidden by the
  build's cut list, and it would silently mask a real edit that differs only in whitespace.
- *Pin every installed path to `eol=lf` in the target.* That is gov's deployer dictating a repo-wide
  attributes policy in a repository gov does not own, and it fails outright for an adopter who
  declines the pin.
- *Store a `locally_modified` boolean.* A stored boolean about a comparison goes stale the moment
  either side moves; an operator who reverts an edit leaves it set forever.
- *Keep the worktree read and widen the tolerance.* A comparator that accepts two spellings of one
  file accepts them for a genuinely edited file too.

### Files touched (estimate)

`tools/govkit/govkit.py` (~70 lines), `tools/govkit/selftest.py` (~8 arms), and one anchor in
`tools/govkit/refusal_join.py`'s enumerated set.

## 5. Production-readiness checklist

- security — S4 closes a real overwrite. Reading the index without it classifies a path with no
  index entry as `absent`, which the write loop turns into a raw write over an untracked local file.
- perf / scale — one batched `ls-files -s` per run replaces one worktree read per row, which is
  strictly fewer syscalls on any receipt holding more than one file.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a target with no index entry for a claimed path refuses by name.
  A `checkout-index` that fails reports and leaves the index entry rather than half-writing, with
  the rollback itself left to `-14`.
- observability — the printed table keeps its shape and its vocabulary. The header line at `:2967`
  moves from `receipt schema 2` to `receipt schema 3`, which is how an operator sees the migration.
- risks — the residual risk is a target whose index is stale against its worktree, where this unit
  reports a file as gov's while the operator's editor shows otherwise. Stated rather than solved:
  `-12`'s dirty-path precondition refuses that exact state before any write, and `-12` lands ahead.
- testing + left-shift gates — the class is "a receipt field asked to be two things at once", and
  AC6 gates it behaviourally by corrupting every `sha256` and asserting no verdict moves.
- migration / rollback — a schema-2 receipt upgrades in place on the first `update`, with both
  identities computed from evidence rather than carried over from `sha256`. A schema-3 receipt read
  by an older govkit is benign: it ignores unknown keys and still finds `sha256`.
- user docs — `WIRE-INTO-PROJECT.md`'s receipt section gains the two-identity paragraph and the
  schema-3 note.

## 6. Acceptance criteria

- **AC1** — A fixture installed by `govkit.py apply --kits memory-tree` and then cloned with
  `git clone -c core.autocrlf=true` reports the same tally as the uncloned original, `current 24 ·
  missing 3`, with zero `patched`. Observe RED first: measured 2026-08-24 at `9ddcc5c9`, that clone
  reports `current 1 · missing 3 · patched 23`.
- **AC2** — Both arms of the index read, because a fix that reads neither side is indistinguishable
  from one that reads the wrong side. With a claimed path edited in the clone's worktree and NOT
  staged, its row still reads `current`; after `git add` of that same edit, it reads `patched`.
- **AC3** — With a claimed path dropped from the index by `git rm --cached` and left on disk
  untracked, `update --write` refuses, names the path, and leaves the file's bytes unchanged. This
  arm is not red at `9ddcc5c9`: it guards a hazard S2 itself introduces, so its failing case is
  observed by staging S2 without S4, watching the overwrite, and then unstaging it.
- **AC4** — On the autocrlf clone, `update --write` of a genuinely stale row leaves the index blob
  byte-identical to `git -C <gov> rev-parse <to>:<source>`, and leaves the worktree file carrying
  the line endings that target's own filters produce. Observe RED first: `dp.write_bytes` at
  `:3071` lands LF, which is not what those filters produce for that path.
- **AC5** — After `--write`, `install.json` reads `"schema": 3` and every engine row carries
  `gov_oid`, `oid` and `sha256`. A hand-built schema-1 fixture and a schema-2 fixture both still
  classify without refusal, and the schema-1 role-distrust arm still fires on the schema-1 fixture.
- **AC6** — The class gate. An arm rewrites every row's `sha256` to one constant and asserts the
  printed verdict lines are byte-identical to the run before it. Observe RED first: at `9ddcc5c9`
  that corruption turns every row `patched`.
- **AC7** — `python tools/govkit/govkit.py selfcheck` exits 0, and `python
  tools/govkit/refusal_join.py` accounts for S4's new refusal branch with an arm that reaches it.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest`, `govkit selfcheck`
and `refusal_join` legs. Adds arms and one refusal anchor; adds no new leg.

## 8. Open questions

- **F1 — the mode for `update-index --cacheinfo` on a row with no existing index entry.** Gov's
  tree entry mode at `commit`, or a literal `100644`? Gov's tree entry: a hook that lands
  non-executable is a hook that does not run, and `-1` is about to make `.githooks/pre-push` a
  reachable destination.
  RESOLVED (agent, 2026-08-24, delegated): gov's tree entry mode, under the full-scope approval.
- **F2 — one batched `ls-files -s`, or one per row?** Batched over the receipt's path list, read
  into a dict before the classification loop. A per-row spawn is one process per file on a receipt
  that already knows every path it will ask about.
  RESOLVED (agent, 2026-08-24, delegated): batched.
- **F3 — retain `sha256` at schema 3, or drop it?** Retain. Dropping it breaks `install.sums` and
  the join that asserts the sidecar against the receipt, which is the artifact a target verifies
  with bash alone.
  RESOLVED (agent, 2026-08-24, delegated): retain.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold). Every cited
  line was opened at `9ddcc5c9`. Three brief citations were off by a little and are corrected here:
  the OURS comparison is `:2889` and not `:2886`, the merge stamp is `:3098` and not `:3096`, and
  `Report` is `:565` while `Refusal` is `:78`, rather than the two together at `:566`. The
  23-patched measurement was reproduced end to end rather than taken on trust, and its complement
  was measured beside it: the same target uncloned reports `current 24 · missing 3`. One brief claim
  is narrowed. inCMS is immune through `core.autocrlf=false`, but NicoCares is immune for a
  different reason — a repo-wide `* text=auto eol=lf` baseline in its own `.gitattributes` — despite
  carrying `core.autocrlf=true` locally. Neither live target reproduces the defect, so the red-first
  observation runs on a constructed fixture and this spec says so rather than implying a live red.

## 10. Reuse audit

Wires through seams that already exist rather than adding any. `blob_at` (`:2148`) keeps answering
"what did gov ship", and its docstring already states the index-side rule this unit extends to the
target side. The batched index read joins the `ls-files` form already spelled at `:112` (`tracked`),
`:1790`, `:2642` and `:2673` rather than adding a fourth spelling, and `tracked` itself is the seam
for the tracked-versus-indexed distinction S4 needs. `VERDICT_GRID` (`:2843`), `UPDATE_ROLE`
(`:2857`) and the `classify_row` (`:2874`) and `three_way` (`:2897`) pair are untouched in shape;
only which identity the OURS axis reads changes. Refusals reuse `Refusal` (`:78`) and `Report`
(`:565`) and are counted by the existing `refusal_join.py` contract rather than a new counter.
`resolve_entry` (`:270`), `target_context` (`:535`), `resolve_tokens` (`:516`), `load_deploy`
(`:553`) and `planned_writes` (`:1359`) are deliberately untouched: this unit changes what a row's
fields MEAN, never how a destination is resolved. `cmd_check`'s per-kit `[check].argv` runner
(`:1632-1652`) is untouched for the same reason — it measures adoption, not identity.
