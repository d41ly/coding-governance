# TOOL-dTendedCadence-57 — the retrofit sweep's offender key observed through `--readings`, one key per run and byte-equal across a count change

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 17 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 17 of `reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`,
HIGH, item H3. Unit 44 AC1 reads the retrofit-heat key from `python drift_report.py --offenders`
(spec-44:87-91), which keys only signals that are gateable and live (`drift_report.py:4364-4366`), and
`maintain.retrofit-heat` is `gateable` False (spec-9 S2, :64). Its byte-equal check compares two empty
outputs and cannot fail, so a detail row still carrying `reads` or `touches` passes it. This unit is
the arm that observes the key where the reading publishes it, the `keys` member `--readings` emits
(unit 8 S5), with a lower bound so an empty population reds.

## 2. Scope (IN)

- **S1** — The case, in `tools/drift-audit/selftest.py`: two runs of `python drift_report.py
  --readings` over one fixture whose reads file differs between the runs only in the sweep target's
  read count. From each run's JSON it takes the record whose `reading` is `maintain.retrofit-heat` and
  its `keys`. Observed by AC1.
- **S2** — The bound. The case asserts each run's record exists and carries exactly one key before it
  compares, so a reading that is absent, dead or keyless reds rather than comparing nothing. Observed
  by AC1 and AC2.

## 3. Non-goals (OUT)

- The detail row and `sweep` member: unit 44 S1 to S3, unchanged.
- A registry-wide arm over every reading's detail rows: unit 44 §3's left-shift, not built here.

### Edges

- **consumes-from** `TOOL-dTendedCadence-44` — `measure_retrofit_heat`'s identity-only detail row, whose key stability this arm observes in place of AC1's empty compare
- **consumes-from** `TOOL-dTendedCadence-8` — `drift_report.py --readings` and its `keys` member, byte-equal to the keys `--offenders` would print (S5)

## 4. Design

`keys` is derived by `derive_offender_keys` for a live reading over its pin, gateable or not, and a
reading not asked or not live carries none (spec-8 :188-192). The fixture therefore sweeps a target
with reads on untouched legacy, so the reading is over its pin of 0. The case finds the record by its
`reading` name, never by position.

### Files touched (estimate)

- `tools/drift-audit/selftest.py`: S1, S2

## 5. Acceptance criteria

- **AC1** — When the case runs `python drift_report.py --readings` twice over the fixture, each run's
  `maintain.retrofit-heat` record carries exactly one key, the two keys are byte-equal, and neither
  contains `reads` or `touches`.
  Red when: a count reaches the key, or either run carries zero keys.
- **AC2** — When the case runs with the fixture's reads file emptied, so no target is swept, it fails
  naming `maintain.retrofit-heat` and the count 0.
  Red when: an empty population passes the compare.

## 6. Gates

`drift-audit selftest` · `memory hygiene`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · two reads files differing in one count and one emptied, staged against a four-field detail row · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 17 (HIGH, item H3) of the round-1 spec
  audit of units 35 to 48.

## 9. Reuse audit

The seam is unit 8's `--readings` output and `derive_offender_keys`, read as published; the case adds
no keyer. `python tools/codebase-map/reuse_lookup.py "read the offender key a reading publishes"` ranked
name stems only, `read`, `read_text`, `key` and `keys`; `--readings` is absent at base, so no existing
seam fits beyond unit 8's member.

Recall terms used: `python tools/memory-recall/query.py "why does an offenders compare pass on a
reading that is not gateable" --terms "offenders gateable readings keys retrofit-heat detail row
byte-equal empty population lower bound"`
