# TOOL-dCalibratedLens-27 — a failing reading or proposer becomes an `unread` line, and the record is checked before anything is filed, so no period re-runs forever

**Status:** DEFERRED · rev-2 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 3 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-27-deviation-271.md](../build/2026-11-02-build-TOOL-dCalibratedLens-27-deviation-271.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 |
| [2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 49, HIGH, item H9 of the round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`). Unit 3 S2 exits the
walk 1 when an item raises or refuses, so `run_cadence_period` hands the lease over and the next wake
runs the period again, with no retry bound. Several failures are deterministic: unit 15 refuses a
breach subject carrying a space or a comma at the write boundary, unit 16's `check_trend_classes` and
`check_trend_complete` exit 1, and any `METRICS` reader can raise. The order is lease, gather, price,
file, record, so a refusal at `record` re-files every proposal on every wake, each a `seen` receipt on
its intake. This unit isolates every reading and proposer, moves the record's refusals ahead of the
first filing, and proves both with plants. It repairs `TOOL-dCalibratedLens-3`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text (each at rev-2,
  its §4 "Amendments (round-1 spec audit)", id 49): unit 3 S2 and S5 — each `METRICS` reader and each
  proposer runs under its own `try`, and a raise or a refusal becomes that entry's Metrics line
  `<name>: unread · <why>`, or for a proposer the line `loop — <key> · <proposer> · unread · <why>` and
  no proposal, never the walk's exit; `<why>` is `<exception class>: <message>` with every line break
  made a space and every ` · ` made `, `, and a reading whose answered value or source carries a line
  break is written `<name>: unread · refused value` (round-2 id 31, `TOOL-dCalibratedLens-40`); the
  gather item's outcome line counts the unread readings, `loop — <key> · item.loop.gather · measured
  · <n> unread: <names>` (round-2 id 22); an empty-`accept` proposal is refused by its own line and
  is not the file item's refusal, so the walk goes on and exits 0 (round-2 id 7); and before
  `item.loop.file` files anything the walk renders the record once through `render_loop_record`,
  every proposal marked `pending`, so a writer refusal left after isolation (a proposal `id` carrying
  a line break, a malformed key) exits 1 before any intake is written. Unit 15 §4 "The metrics" — a subject
  carrying a space or a comma is skipped from `cap-breaches` with one `ledger — cap · <subject> ·
  skipped · unsplittable subject` line, never refused. Unit 16 S2 and S5 — their refusals answer the
  `stall-trend` reading `unread · <why>`, never exit 1 of the walk. Observed by AC1.
- **S2** — The proof, two `--fixture` plants in `tools/loop/loop_review.py`: `reader-raises`, a planted
  `METRICS` entry that raises: `run --dry-run --key 2026-W45` exits 0, the printed record carries
  `<entry>: unread · <the folded class and message>`, every other line intact, and the gather item's
  outcome line reads `1 unread: <entry>` (round-2 id 22); and `record-refuses`, a planted proposal
  whose `id` carries a line break beside one valid proposal: `run` runs WITHOUT `--dry-run`, the key
  supplied as `GOV_CADENCE_KEY=2026-W45` as the executor supplies it (unit 3 S3 admits `--key` only
  with `--dry-run`), with a counting stub standing in for the intake filer, recording each call
  (round-2 id 32). The walk exits 1 at the pre-render and the stub's count reads 0. Observed by AC2 and
  AC3.
- **S3** — The retry: the same `record-refuses` plant run twice leaves the planted filer's call count at
  0 both times, so a deterministic refusal files no receipt however often the period re-runs. A
  proposal with an empty `accept` takes the other path: it is refused by its own line, the walk exits
  0 and the period records, so nothing re-runs it (round-2 id 7). Observed by AC3.

## 3. Non-goals (OUT)

- A hand-over bound per period (the third failure filing an owner item). Once readings and proposers
  are isolated and the record is checked first, the failures left after a filing are I/O failures of
  the final write, transient by nature; a counter would need a store the lease does not carry.
- Making `intake.py file` idempotent within a period. It is TOOL-dWellOiledMachine-27's verb, and with
  the refusal moved ahead of the filing nothing deterministic re-files.
- Unit 15's and unit 16's own fixtures for their skip and `unread` lines: each lands with its amended
  criteria.
- The multi-line `<why>` case of `reader-raises`: `TOOL-dCalibratedLens-40` (round-2 id 31).
- AC1 observes only the disposal's text in sibling specs and is green at writing; it is a
  precondition, not an observation of this unit's build (the round-2 audit's ids 4, 18 and 29).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-3` — `run_loop_walk`, `measure_loop_metrics`, `render_loop_record`, `run_loop_file` and the `--fixture` frame; without the walk there is no failure to isolate
- **hands-off** `TOOL-dCalibratedLens-40` — the `reader-raises` plant, which that unit's `reader-raises-multiline` case extends (round-2 id 31)

## 4. Design

### Evidence

- spec-3 S2: the walk "exits 1 when an item raises or refuses, so `run_cadence_period` releases the
  lease as a hand-over and the next wake runs the period again"; §4 "The items" orders file before
  record; S7: a recurrence "appends its receipt to the open intake, route `seen`".
- spec-15 §4 "The metrics": "A subject carrying a space or a comma is refused at the write boundary".
- spec-16 S2 and S5: `check_trend_classes` and `check_trend_complete` exit 1.
- spec-15 §4 "The metrics" calls repeated `seen` receipts "the noise the clause forbids".

### The walk, as amended

```
lease -> gather (each reader in its own try) -> price -> [propose] (each proposer in its own try)
  -> render_loop_record(..., filed=pending)   # a refusal exits 1 here, nothing filed
  -> file -> record (write)
```

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `reader-raises`, `record-refuses` | `--fixture` plant names | none |
| `unread` | Metrics value word | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2 and S3, the plants

### Alternatives rejected

- **Keep the exit, add a retry counter.** The review's first option; it bounds the noise at three
  receipts instead of removing it, and needs a per-period store.
- **Record before file.** The record's Filed lines need the filing's routes, so the write cannot move;
  a pre-render with routes `pending` checks everything the write checks.

## 5. Production-readiness checklist

- security — the writer's refusals are unchanged and now fire before any external write.
- perf / scale — one extra pure render per period.
- error / empty / loading states — a dead reading is a named `unread` line, never a missing record.
- observability — every isolated failure prints its entry and reason.
- risks — a reader that always raises reads `unread` every period, visible in every record rather
  than blocking the review.
- testing — the two plants and the retry of S3.
- migration — N/A: no period has run at base.
- user docs — `help/loop-review.md` (unit 3 S11) gains the `unread` word through unit 3's amendment.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'unread · <why>'` runs over the specs of units 3 and 16 and `grep -n
  'unsplittable subject' memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-15.md`
  runs, each prints its amendment.
  Red when: a sibling still exits the walk on a reading's failure.
  A precondition read at writing: it greps the disposal's text.
- **AC2** — When `python loop_review.py --fixture --plant reader-raises` runs `run --dry-run --key
  2026-W45`, it exits 0, the record carries the `unread` line for the raising entry, and the gather
  outcome line names it as `1 unread`.
  Red when: one raising reader stops the period, or a period of dead readings prints a bare
  `measured`.
- **AC3** — When the plant `record-refuses` runs `run` twice under `GOV_CADENCE_KEY=2026-W45` with the
  counting stub, each run exits 1 at the pre-render and the stub's call count reads 0 after both; under
  the staged break (the record rendered only after filing) the count reads above 0.
  Red when: a refusal after filing re-files on the retry, or the plant runs in a mode that files
  nothing either way.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plants once that unit lands.

New arm: tools/loop/loop_review.py · covers AC2 AC3 · the plants `reader-raises` and `record-refuses`, staged red by a walk that lets a reader's raise escape and renders the record only after filing · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 49 (HIGH, item H9) of the round-1 spec audit;
  units 3, 15 and 16 amended at the disposal (their rev-2).
- rev-2 · 2026-11-02 · §3 S1 S2 S3 AC1 AC2 AC3 · amended at the disposal of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`: the folded `<why>` and the refused-value
  line (id 31, `TOOL-dCalibratedLens-40`); the empty-`accept` path (id 7), the unread count on the
  gather line (id 22), `record-refuses` run without `--dry-run` under the executor's key with a
  counting filer (id 32) and AC1 stated a precondition (ids 4, 18, 29), all `TOOL-dCalibratedLens-41`;
  §3 gains the hands-off to unit 40.

## 10. Reuse audit

The seam extended is unit 3's walk and its pure `render_loop_record`, called once more before the
filing; no new reader or writer. `python tools/codebase-map/reuse_lookup.py "isolate each reader so
one failure becomes an unread line, never the walk's exit"` ranked name stems only (`read_text`,
`read`, `walk`), none an isolating runner, so no existing seam fits and the isolation is new inside
the walk. The recall probe returned TOOL-cMendedVintage-19, the placement ruling this unit's order
follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
