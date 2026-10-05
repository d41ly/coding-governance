# TOOL-aMendedFleet-15 — the shrink-only pin on `backlog_asks_unlabelled` is re-armed

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 15

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Before the backlog switch-over, check 20's `SEVERITY_UNLABELLED_PIN` held the count of rows with no
severity and refused a rise. The switch-over blanked it, because the shard census reads a generated
view as zero rows, and its successor, drift-audit's `backlog_asks_unlabelled`, shipped with no pin
at all. So today that signal prints `over pin 0` at 452 on every run, which says nothing, and a rise
in unlabelled asks moves no number anybody is held to. This unit pins the signal at its measured
value and makes raising that pin cost a written reason, as every other shrink-only drift pin does.

## 2. Scope (IN)

- **S1** — `PINS` in `tools/drift-audit/drift_signals.py` gains `"backlog_asks_unlabelled": <n>`,
  where `<n>` is the signal's `value` read from `python tools/drift-audit/drift_report.py --json` at
  the pass's HEAD, after `TOOL-aMendedFleet-14`'s dispositions. A comment above it says the value is
  MEASURED at this unit, why the population can only fall, and that the old check-20 pin is the
  predecessor it stands in for. Observed by AC1.
- **S2** — `RATCHETS` in the same file gains `{"file": _THIS_FILE, "key": "backlog_asks_unlabelled",
  "weakens": "up"}`, so a raise of the S1 pin without an `<old> -> <new>` line above it is a
  `RATCHET WEAKENED` finding under `--check`. Observed by AC2 and AC3.
- **S3** — The signal stays report-only, `gateable: False`: a value above the pin prints
  `over pin <n> (report only)` and never reds `--check` by itself. Observed by AC1.

## 3. Non-goals (OUT)

- Making the signal gateable. That changes the shipped kit's verdict for every adopter in `builds`
  mode, whose first `--check` would red on one unlabelled ask (§8 F1).
- Re-declaring `SEVERITY_UNLABELLED_PIN` in `.memory-tree.conf`. Check 20 counts view rows under
  `builds`, which are zero by construction, so that key has nothing to hold.
- Lowering the pin as asks gain severity. A pin left above its value grades nothing until the value
  climbs back, and no gate here asks for the drain; the status column prints `drain it`.
- Labelling or deferring any ask, which is `TOOL-aMendedFleet-14`.
- Pins on the other two ask signals. `backlog_asks_contested` and `backlog_evidence_sha` read zero,
  where the default tolerance already holds them.

### Edges

- **consumes-from** `TOOL-aMendedFleet-14` — the unlabelled count after its five dispositions; a pin
  measured before them would sit five above the value on the day it lands.

## 4. Design

### Evidence

Read at base `7af5f564` on 2026-10-04, PINNED to that date.

- `drift_report.py` prints `backlog_asks_unlabelled 452 457 over pin 0 (report only)`.
  `build_backlog_asks_unlabelled` reads the live `--asks --json` projection and counts rows whose
  `sev` is `unlabelled`; its tolerance is `ctx.pins.get(name, 0)`, and `PINS` carries no key for it.
- `.memory-tree.conf` keeps `SEVERITY_UNLABELLED_PIN=""` with a comment recording that it was lowered
  to empty at the switch-over by `TOOL-dDerivedDocket-34` S4, because `row_grammar.py --emit-pin`
  reads each view as zero rows.
- `ratchet_findings` in `drift_report.py` reads a `"key": <int>,` line through `_scalar_at`, compares
  the working copy with the base ref's blob, and skips a key the base does not carry. So the row S2
  adds grades the NEXT move of the pin, never the one that introduces it.
- The population can only fall on its own. V12 refuses an ask filed on or after `ASK_CUTOFF`
  without a `SEV` row, so a new unlabelled ask arrives only as a pre-cutoff row relocated from a
  stale branch, or as a terminal ask a `REOPEN` revives.
- `live_backlog_rows_per_shard` and `source_cited_ids_resolving_to_no_record` are report-only pins
  with a `RATCHETS` row each; S1 and S2 copy that pair exactly.

### Files touched (estimate)

- `tools/drift-audit/drift_signals.py`

It is the project layer, not kit code, so no kit version moves.

### Alternatives rejected

- **A gateable pin.** §8 F1.
- **Re-arming check 20 on the ask projection.** It would put a second count of one population in a
  second kit, read by a second parser, which is the copy that drifts.

## 5. Production-readiness checklist

- security — N/A — one integer and one list entry in a project-layer module.
- perf / scale — N/A — no new read; the signal already runs.
- error / empty / loading states — under `shards` the signal reads "not asked" and the pin is
  inert; a blind projection still prints DEAD PROBE through the signal's existing `live` field.
- observability — the status column reads `ok (pin <n>, drain it)` at or below the pin.
- risks — a relocation that carries old unlabelled rows raises the value above the pin; the remedy
  is a severity row or a pin raise with its reason, and either is a visible act.
- testing — AC1 to AC3 are direct runs of the report; no suite runs.
- migration — N/A.
- user docs — N/A — the pin's comment is the record.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py` runs after the pass, the
  `backlog_asks_unlabelled` row prints a status of `ok (pin <n>, drain it)` with `<n>` equal to its
  own value column, and `python tools/drift-audit/drift_report.py --json` reports that signal's
  `pin` as the same integer and `gateable` false.
  Red when: the row still reads `over pin 0`, or the pin and the value disagree on landing.
  figure: `<n>` DERIVED at observation time from the report itself.
- **AC2** — When the pin is raised by one in the working copy of
  `tools/drift-audit/drift_signals.py` with no justification line, and
  `python tools/drift-audit/drift_report.py --check --base-ref HEAD` runs, stderr carries a
  `RATCHET WEAKENED` line naming `backlog_asks_unlabelled` and both values; the edit is then reverted.
  This is the staged break for S2's new ratchet row.
  Red when: no such line names the key, so the raise passes silently.
- **AC3** — When the same raise carries a comment line `<n> -> <n+1>` within `RATCHET_LOOKBACK`
  lines above the pin, and when the pin is instead LOWERED by one, the same command prints no
  `RATCHET WEAKENED` line naming the key in either case; both edits are reverted.
  Red when: a justified raise or a drain is refused, which would make the pin unmovable.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `spec tokens (a spec's own names resolve)`

The one path trips the `drift-audit selftest` guard; that suite builds its own signals module and
never reads this one, so it is owed by the guard rather than by the change.

## 8. Open questions

- **F1 — Report-only with a ratchet row, or gateable?**
  Options: keep `gateable: False` and add the `RATCHETS` row, as the two sibling backlog pins do; or
  flip the signal gateable so a value over the pin reds `--check`. Gateable holds the line harder,
  and it changes the shipped kit's verdict for every `builds`-mode adopter, whose project layer
  carries no pin and so falls back to a tolerance of 0. That is a public-surface change, which M3's
  veto 2 refuses.
  RESOLVED (agent, 2026-10-04, delegated): report-only plus the ratchet row, in this repo's project
  layer only.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the signal, the project layer's pins and the ratchet
  reader at base.

## 10. Reuse audit

The seam extended is the project layer's `PINS` and `RATCHETS` in
`tools/drift-audit/drift_signals.py`, read by `ratchet_findings` and `_scalar_at` in
`tools/drift-audit/drift_report.py`; nothing in the kit changes. `python
tools/codebase-map/reuse_lookup.py "shrink-only pin on a report-only drift signal"` returned name-stem
neighbours only, so the seam was found by reading the two sibling pins. Recall named the
switch-over's design record, where the signal was introduced as a report-only count, and
`DEPL-aHoistedPass-9`, a shrink-only floor trailing its population, which is the drain risk §3
leaves open.

Recall terms used: `python tools/memory-recall/query.py "why was the unlabelled severity pin
blanked at the backlog switch-over" --terms "SEVERITY_UNLABELLED_PIN backlog_asks_unlabelled
shrink-only pin RATCHETS PINS drift_signals switch-over check 20 re-arm"`
