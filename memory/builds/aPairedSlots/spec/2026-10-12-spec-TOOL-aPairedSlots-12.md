# TOOL-aPairedSlots-12 — the A/B instrument reads the run record's verdict by key, and the rule check proves an arm from its bar rows

**Status:** CLOSED · rev-1 · 2026-10-12 · node a · Tier-1 · base d3354597 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-TOOL-aPairedSlots-12-1-acceptance-ledger.md](../build/2026-10-12-build-TOOL-aPairedSlots-12-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 TOOL-aPairedSlots-11 TOOL-aPairedSlots-13 TOOL-aPairedSlots-14 TOOL-aPairedSlots-15 |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's H2 (id 12, with L8, id 38): the A/B instrument takes the first line of a run
record's `verdict` file as the verdict. That line is `ended<TAB><time>`, so every finished bar's row
gains a field and its proof lands one column right. The MAKESPAN row then collects the expected-leg
count as its proof, and the rule check accepts any proof but `NO`, so a re-measure could prove an arm
from a refusal. This decided nothing wrong in this build: A1's true proof reads `yes`, and B1 and C1
were unproven. But the results record tells an owner to re-run this instrument before turning two
slots on.

## 2. Scope (IN)

- **S1 — the instrument reads the verdict by key.** `measure_bar` takes the `verdict` key's value
  from the run record's `verdict` file, so a bar row keeps the sixteen fields its header declares.
  Observed by AC1.
- **S2 — the rule check proves an arm from its bar rows.** Each arm-run is proven when both of its bar
  rows carry proof `yes` and their `ok` plus `fail` equal `expected`, read at the row's own offsets: a
  seventeen-field row is the shifted layout the results record explains. The MAKESPAN row's proof
  column is no longer read. Observed by AC2.

## 3. Non-goals (OUT)

- Re-running the A/B, or changing the committed rows: the decision stands on them.
- The two-bar check, which reads the same file the same way (TOOL-aPairedSlots-13).

## 4. Design

The run record's files are key-TAB-value, and every verdict write in the runner opens with `ended`.
Reading by key is the form the runner's own readers use. The rule check keeps reading the committed
rows, so it must read both layouts: a row's field count says which one it is.

### Files touched (estimate)

- `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh`
- `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-9-rule-check.py`

## 5. Acceptance criteria

- **AC1** — When the instrument's `measure_bar` runs over a fixture root whose newest run record holds
  an `ended` line before its `verdict` line, the row it appends has sixteen fields and its verdict
  column reads the `verdict` key's value.
  Red when: the row has seventeen fields, or the verdict column reads `ended`.
- **AC2** — When the rule check runs over the committed rows and the tree, it prints AGREE, and over a
  copy of those rows whose A1 bar rows carry proof `NO`, it refuses to decide.
  Red when: the copy decides, because the MAKESPAN row's shifted column still reads as proof.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-12 · initial draft, promoted from the closing review's round 1.
