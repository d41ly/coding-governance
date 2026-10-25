# TOOL-dWitnessedBar-40 — the per-tree verdict keeps the retired writers' two declines and carries the reuse pair the hook judges

**Status:** OPEN · rev-4 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 18 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 |
| [2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md) | research | TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-40-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md) | research | TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 18 at HIGH**, its item **H1**, alone in that item. `TOOL-dWitnessedBar-4` S2 has
the runner write `gate-verdict/<tree>[.scoped]` on every run that started clean, and S4 deletes the
hook's writer. That writer declines in two cases the runner never learns of: a doc-only scoped push
(`.githooks/pre-push:2398-2399`) and a scoped push resting on an inherited green (`:2400-2403`). The
per-tree key list also omits `reused` and `reused_cache`, the pair predicate 9 `check_green_reuse`
reads (`:1549`), so unit 4's AC5 cannot be met. A docs-mode run would write a `kind scoped` GREEN that a
later push of the same tree adopts while skipping code legs it never ran. This unit takes the report's
fix. It repairs `TOOL-dWitnessedBar-4`.

## 2. Scope (IN)

- **S1** — The docs decline. The runner writes no per-tree record when its docs mode is on, that is
  when `DOCS_BASE` resolved (`tools/run-gates/run-gates.sh:428-436`), and prints one line naming why.
  Observed by AC1.
- **S2** — The inherited-base decline. The runner reads `GATE_BASE_FROM` once and unsets it before any
  leg starts, as it does `GATE_RUN_ID`. Its value is `full` or `inherited`, and anything else reads
  `full`. Under `inherited` a scoped run writes no `.scoped` record and prints why. The hook exports
  `GATE_BASE_FROM=inherited` beside `GATE_BASE` in its inherited-green branch (`.githooks/pre-push:2122-2126`),
  and the unattended driver exports it where `--decide` printed `-` as the full base
  (`.githooks/pre-push:2193`). Observed by AC2.
- **S3** — The reuse pair. The per-tree record gains `reused` and `reused_cache`, written from the same
  counts the full-green stamp writes (`run-gates.sh:5619-5620`). Observed by AC3.
- **S4** — The hook judges the pair. `check_bar_record` calls `check_green_reuse` on the per-tree
  record's `reused` and `reused_cache` after `check_green_record`, so a record that took a leg from the
  cache, or one with `reused` and no `reused_cache`, is not adopted. A per-tree record carrying neither
  key is not adopted either, since it cannot say whether it reused. Observed by AC4.

## 3. Non-goals (OUT)

- The per-tree record itself, its two slots and its other keys: `TOOL-dWitnessedBar-4`'s.
- The selection witness on the per-tree record: `TOOL-dWitnessedBar-41`'s.
- The STUB decline (`.githooks/pre-push:2396-2397`). The runner is never the declared stub, so nothing
  carries over.
- A pre-push.test.sh arm per decline branch of every retired writer, the report's left-shift: AC1, AC2
  and AC4 are those arms for the two declines and the reuse pair.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-4` — the runner's per-tree verdict writer and the hook's `check_bar_record` over it, whose declines and reuse keys this unit adds; without them there is no record to decline or judge
- **hands-off** `TOOL-dWitnessedBar-51` — the per-tree record's `reused_cache` key, which the minors batch's id 13 item uses as unit 4's AC5 plant
- **hands-off** `TOOL-dWitnessedBar-56` — the reuse pair, the keyless refusal, `GATE_BASE_FROM` and its export, which the verdict-boundary minors batch observes, classifies and records on `base_from` (ids 3, 4, 14, 15, 27, 32)
- **hands-off** `TOOL-dWitnessedBar-58` — `GATE_BASE_FROM`'s read-once-and-unset and the hook's export, which id 12's unit observes at the stub bar and the runner boundary and from a leg that must not see it
- **hands-off** `TOOL-dWitnessedBar-60` — the driver's own `GATE_BASE_FROM` export, which id 28's unit keeps on the bar call's `env` argv after the driver's scrub
- **hands-off** `TOOL-dWitnessedBar-63` — the scoped decline, which the minors batch removes as unit 58's second staged break (id 34)

## 4. Design

### Evidence

- The retired writer's declines: `bar_record = stub`, then `GATE_DOCS_BASE` set, then `RUNLOG_DECISION =
  scoped` with `inh_sha` set (`.githooks/pre-push:2396-2403`); its comment says a doc-only bar "ran fewer
  legs than a scoped bar from the same base, which the record cannot say".
- The runner unsets `GATE_DOCS_BASE` after resolving `DOCS_BASE` (`run-gates.sh:429-436`), so the runner
  alone knows whether docs mode was on.
- The hook exports `GATE_BASE=$scoped_base` in both scoped branches, and `scoped_base=$inh_sha` when the
  base is inherited (`.githooks/pre-push:1898`); the runner cannot tell the two apart from `GATE_BASE`.
- `check_green_reuse <label> <reused> <reused_cache>` (`.githooks/pre-push:1549-1559`) forces on a
  non-zero `reused_cache`, and on a non-zero `reused` with no `reused_cache`.

### The write rule

```
write the per-tree record when the tree started clean and did not move (unit 4 S2), unless
  DOCS_BASE is non-empty                       -> "run-gates: no gate-verdict written — docs mode"
  scoped and GATE_BASE_FROM = inherited        -> "run-gates: no gate-verdict written — scoped on an inherited green"
keys: unit 4's, plus  reused <n>  reused_cache <n>
```

A full run under docs mode cannot occur: `DOCS_BASE` is set only when `GATE_FULL` is empty
(`run-gates.sh:429`).

### Inventory

Minted: the env knob `GATE_BASE_FROM` and its two values; the per-tree keys `reused` and
`reused_cache` (spelled as on the full-green stamp); the two decline lines. Naming cells: the knob is
asked of `python tools/lexicon/lexicon.py --suggest GATE_BASE_FROM` at the pass.

### Migration

A per-tree record written between `TOOL-dWitnessedBar-4`'s pass and this one lacks the pair and is not
adopted (S4), so the first push after this pass may run a bar it could have adopted. That costs a
saving, never a verdict.

### Rollout

Live at landing, in one commit with the hook.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `tools/unattended/unattended.sh`

### Alternatives rejected

- **The hook deletes a record it judges docs-mode after the bar.** A second writer of one fact, and a
  record written by one party and removed by another.
- **The record carries `docs_base` and the hook refuses it.** The record would still exist for every
  other reader, `local-hook`'s reader among them (`TOOL-dWitnessedBar-6` S4), which would read a
  doc-only GREEN as a verdict.

## 5. Production-readiness checklist

- security — closes a fail-open path: a doc-only GREEN can no longer certify code legs it never ran.
- perf / scale — one env read and two string tests per run.
- error / empty / loading states — an unrecognised `GATE_BASE_FROM` reads `full`, which writes; the hook
  still refuses a scoped record whose base no full green covers (`check_bar_base`).
- observability — each decline prints one line naming its reason.
- risks — a docs-only push of a tree is never adopted later; the next push of that tree runs its bar.
- testing — AC1 to AC4 by fixture; the arms of §7 at the close.
- migration — §4.
- user docs — `tools/run-gates/README.md`'s verdict section names the two declines and the pair at the
  pass; no page under `help/` covers the boundary.

## 6. Acceptance criteria

- **AC1** — When the runner makes a scoped run with `GATE_DOCS_BASE` set to a resolvable commit over a
  fixture manifest (`--legs <fixture>`) in a clean scratch clone, `ls <common-dir>/gate-verdict/` holds
  no file for `git rev-parse HEAD^{tree}` and the output carries `no gate-verdict written — docs mode`;
  with `GATE_DOCS_BASE` unset the same run writes the `.scoped` record.
  Red when: the DOCS_BASE guard is removed, so a doc-only scoped run writes a GREEN.
  fixture: a scratch clone under `%TEMP%/<short-name>`; the tree holds none.
- **AC2** — When the same scoped run is made with `GATE_BASE_FROM=inherited`, no `.scoped` record is
  written and the output names the inherited green; a fixture leg printing its environment shows no
  `GATE_BASE_FROM`.
  Red when: a scoped run on an inherited base writes a record, or a leg inherits the knob.
- **AC3** — When a full run passes over a fixture manifest, `grep -P '^reused(_cache)?\t'` over its
  per-tree record prints both keys with the run's counts.
  Red when: the record omits either key.
- **AC4** — When `.githooks/pre-push` runs over a scratch clone whose pushed tree carries a full GREEN
  per-tree record from the same manifest with `reused_cache 2`, it runs the bar; with `reused 1` and no
  `reused_cache` it runs the bar; with both at 0 it adopts the record.
  Red when: `check_bar_record` skips `check_green_reuse`, so a cached GREEN is adopted.

## 7. Gates

`measure-legs selftest` · `pre-push self-test` · `pre-push bar self-test` · `run-gates canary` · `run-gates evidence` · `memory hygiene`

The unattended kit's own suites are waived for this build's landing (README rule), so the driver's
export of S2 is observed by AC2's runner half, not by its suite.

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 · a docs-mode scoped run, an inherited-base scoped run and a full run, each on a scratch clone, staged red by removing the DOCS_BASE guard · none
New arm: .githooks/pre-push.test.sh · covers AC4 · a per-tree record planted with `reused_cache 2`, then `reused 1` alone, staged red by removing the `check_green_reuse` call · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dWitnessedBar-4`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How does the runner learn that its base is an inherited green?** Options: (a) an env knob the
  caller sets beside `GATE_BASE`, read once and unset; (b) the runner re-derives inherited greens
  itself; (c) the hook removes the record after the bar. (b) duplicates the hook's whole
  inherited-green predicate in the runner; (c) is a second writer. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the `GATE_RUN_ID` precedent. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 18 (HIGH, item H1).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-56, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-58's
  consumes-from edge and the hands-off bullet mirroring TOOL-dWitnessedBar-60's consumes-from edge,
  promoted by the round-1 spec audit of units 52 to 57; nothing else moved.
- rev-4 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-63's
  consumes-from edge, promoted by the round-1 spec audit of units 58 to 62; nothing else moved.

## 10. Reuse audit

The seams extended are the hook's retired declines (`.githooks/pre-push:2392-2403`), carried over
rather than re-derived, and predicate 9 `check_green_reuse` (`:1549`), called on one more record kind.
`python tools/codebase-map/reuse_lookup.py "decline to record a per-tree green for a doc-only or
inherited-base bar"` ranked generic stems (`tree`, `records`, `read_records`, `render_record`) and no
writer of the per-tree record; no existing seam fits beyond the two named, since the runner holds no
decline today.

Recall terms used: `python tools/memory-recall/query.py "why does the pre-push hook decline to write a bar green on a doc-only push" --terms "gate-bar-green GATE_DOCS_BASE docs-only inherited green decline write_bar_green reused_cache check_green_reuse per-tree verdict"`
