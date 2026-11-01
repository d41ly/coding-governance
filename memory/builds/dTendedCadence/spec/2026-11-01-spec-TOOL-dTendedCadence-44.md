# TOOL-dTendedCadence-44 — the retrofit sweep's offender key carries only its target's identity, so an unchanged target recurs instead of filing a new sweep each period

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 16 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-45 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 41 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, item H9. Unit 9's one detail row is `{"path", "population", "reads", "touches"}` (spec-9 S2,
:63-66), and the offender key is that row's JSON with sorted keys and only its line locators dropped
(`json.dumps(extract_unlocated(d), sort_keys=True, ...)`, `tools/drift-audit/drift_report.py:4007`;
`extract_unlocated`, `:3734-3743`, drops `line`, `lines` and a trailing `:<digits>`). Read counts move
every period and differ between nodes, so each period files a new intake, which under `hot-first`
places a new patch build for the same path; S5's "a target unchanged next period adds a `seen` row"
and the risks line's "two nodes ranking one target file one intake" (:226-228) do not hold. This unit
keeps only stable identity in the detail row.

## 2. Scope (IN)

- **S1** — The detail row. `measure_retrofit_heat` returns `detail` as one row `{"path": "<path>",
  "population": "<name>"}`, the target's identity alone. Observed by AC1.
- **S2** — The measurements. The target's `reads` and `touches` travel as one record member beside
  `detail`, `sweep: {"reads": <r>, "touches": <t>}`, which `--readings` passes through as the I4
  record plus row keys (unit 8 S5) and which no key reads. The intake text names the population and the
  path, as unit 9 S5 already says, and carries no count, so its content key is the target's too.
  Observed by AC1 and AC2.
- **S3** — The CLI's `--json` prints `sweep` beside `detail`, and the human line is unchanged.
  Observed by AC1.

## 3. Non-goals (OUT)

- How the target is picked: `derive_sweep_target`, unit 9 §8 F2, unchanged; the counts still rank.
- A selftest arm perturbing the counts of every `[[reading]]`'s detail rows: the report's left-shift
  gate over the whole registry, a separate mechanism, not built here.

### Edges

- **consumes-from** `TOOL-dTendedCadence-9` — `measure_retrofit_heat` and its sweep row, whose detail this unit narrows to identity
- **hands-off** `TOOL-dTendedCadence-57` — `measure_retrofit_heat`'s key stability, which that unit's arm observes through `--readings` with a lower bound (review id 17)
- **hands-off** `TOOL-dTendedCadence-59` — the sweep's cross-node dedupe, which the minors batch repairs (review id 41)

## 4. Design

### Evidence

`render_drift_offenders` (`drift_report.py:3985-4022`) keys each detail row by its full JSON minus
line locators; a count inside the row is therefore part of the key. `extract_unlocated`'s docstring
calls itself the "ONE spelling, shared by `--offenders` and the history's key hash", so the fix is in
the row the reading emits, not in the shared keyer.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `sweep` | reading record member | none |

### Files touched (estimate)

- `tools/drift-audit/retrofit_heat.py`: S1, S2, S3
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **Drop `reads` and `touches` in `extract_unlocated`.** It is the one keyer for every signal, and a
  field name meaning "volatile" here is a real identity field elsewhere.

## 5. Production-readiness checklist

- security — N/A — no write path; the text quotes no transcript, as before.
- perf / scale — N/A.
- error / empty / loading states — no target leaves `detail` empty and `sweep` absent.
- observability — `--json` still shows the counts.
- risks — a target whose population is renamed files a new sweep, which is a new target by identity.
- testing — the criteria of §6.
- migration — N/A — the reading is new in this build.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python retrofit_heat.py --reads <file> --json` runs twice over one fixture whose
  reads file differs only in the target's read count, `python drift_report.py --offenders` prints a
  byte-equal `maintain.retrofit-heat` key both times, and each `--json` carries `sweep` with the two
  counts.
  Red when: a count moves the key, or the counts are lost.
- **AC2** — When the two runs file through `item.maintain.patch` with a recording filer, the two
  recorded texts are byte-equal.
  Red when: the intake text carries a count or a period.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · two reads files differing in one count, staged against the four-field detail row · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 41 (HIGH, item H9) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (units 57 and 59); no scope, design or criterion moved.

## 10. Reuse audit

The seam is unit 9's `measure_retrofit_heat`; the shared keyer `extract_unlocated`
(`tools/drift-audit/drift_report.py:3734`) and `render_drift_offenders` (`:3985`) are called
unchanged. `python tools/codebase-map/reuse_lookup.py "find an ask carrying a marker and whether it is
closed"` and the other set probes named no detail-row normalizer beyond those two, so no new seam is
added.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
