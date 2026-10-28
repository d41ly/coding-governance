# TOOL-dIndexedDesign-43 — the typed record factory admits a field its kind declares repeatable, so an inventory with one `Of` and one `Verdict` line per row binds

**Status:** DEFERRED · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 11 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-43-deviation-431.md](../build/2026-10-28-build-TOOL-dIndexedDesign-43-deviation-431.md) | deviation | — |
| [2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-46 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 31 to 38
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md`)
confirmed finding **id 13 at HIGH**, report item **H5**, the item's only id. `TOOL-dIndexedDesign-34` S1
makes `inventory` a typed kind requiring `Input`, `Of` and `Verdict`, and names no repeatable field.
The factory extracts `deviation_join.read_record`'s refusals, and that reader refuses a repeated key as
"is given twice" (`tools/memory-tree/deviation_join.py:223`). `TOOL-dIndexedDesign-20` S7 writes one
`- **Of:**` line per build ruled on and one `- **Verdict:**` line per built unit. An inventory that rules
on two units, the normal case, therefore reads malformed, and `check_inventory` fails every valid one.

This unit takes the more feature-rich of the skeptic's two options. The factory's per-kind table gains
a declared set of repeatable fields, and `inventory` declares `Of` and `Verdict` there. The kind stays
typed, so its `-inventory-<n>.md` home is still policed both ways and its required fields still graded.
It repairs `TOOL-dIndexedDesign-34` and takes order 11, one above unit 34's 10.

## 2. Scope (IN)

- **S1** — The repeatable set. Each row of `build_records.py`'s per-kind table may name `repeatable`
  fields, a tuple defaulting to empty. The factory's record reader admits a repeated key the kind names
  there and returns its values as a list in file order. Any other repeated key keeps the
  "is given twice" refusal. A repeatable field that is also required is satisfied by one line or more.
  Observed by AC1 and AC2.
- **S2** — The inventory row. Unit 34 S1's `inventory` row declares `repeatable = ("Of", "Verdict")`.
  `Input` stays single. Observed by AC1.
- **S3** — Every other kind unchanged. Each existing row declares no repeatable field, so `deviation`,
  `exception`, `override`, `change`, `fork` and `diff` refuse a repeated key as they do today.
  Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- Keeping `inventory` untyped, the skeptic's other option: it gives up the both-ways file-name join and
  every field grade (§8 F1).
- `check_inventory`'s own findings (unit 20 S8): unchanged. It already finds a unit with two verdicts.
- Repeatable fields for any other kind. None is declared until a writer emits one.
- The report's left-shift checklist entry. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-34` — S1's typed `inventory` kind and its per-kind table row, which S1 and S2 give a repeatable set (id 13)
- **consumes-from** `TOOL-dIndexedDesign-20` — S7's inventory record grammar, one `Of` line per build and one `Verdict` line per built unit, the cardinality S2 admits (id 13)
- **hands-off** `TOOL-dIndexedDesign-53` — S1 to S3, which that unit's S2 lands in unit 34's pass commit, and S1's list shape at count one, which its S14 states there (ids 4 and 29)

## 4. Design

### Evidence

- `tools/memory-tree/deviation_join.py:212-224`: `read_record` walks `FIELD` matches, and a key already
  in `seen` appends "is given twice, at lines …" to `bad`. `FIELD` is `:145`. Read 2026-10-28.
- PLAY-dOrderedCharter-7 S7 extracts "read_record's duplicate, missing and closed-set refusals" into
  `build_records.py`, with each kind's required fields and closed sets in a per-kind table.
- Unit 20 S7 spells "one `- **Of:** <slug> @ <rev>` per build" and "one `- **Verdict:** <unit id> ·
  <verdict> · <reason>` per built unit".

### Data model

```python
KINDS = {
    "deviation": {"required": (...), "closed": {...}},                       # repeatable: ()
    "inventory": {"required": ("Input", "Of", "Verdict"), "repeatable": ("Of", "Verdict")},
}
read_record(...)["fields"]["Verdict"]  ->  ["TOOL-tFix-1 · kept · …", "TOOL-tFix-2 · amended by … · …"]
```

The table's key names follow the factory as built. `repeatable` is the one key this unit adds.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `repeatable` | per-kind table key, `build_records.py` | none |

### Migration

None: no record of any kind repeats a field at base, and no inventory record exists.

### Rollout

Live at its pass, order 11, beside `TOOL-dIndexedDesign-31` and `TOOL-dIndexedDesign-4`, whose write
sets hold no factory file.

### Files touched (estimate)

- `tools/memory-tree/build_records.py`: S1 to S3, and its `typed-kinds` plant

### Alternatives rejected

- **`inventory` untyped, as `seams` is (`TOOL-dIndexedDesign-33` S1).** Lost to M3's richer survivor: a
  `-inventory-<n>.md` file bound to another kind would pass, and nothing would grade `Input`.
- **One `Verdicts:` field holding every verdict joined by `;`.** Lost to unit 20 S7's line grammar,
  which `check_inventory` reads line by line, and to the one-line field rule.

## 5. Production-readiness checklist

- security — N/A: a reader change; no write path.
- perf / scale — none.
- error / empty / loading states — a repeated non-repeatable key is still refused by name; an empty
  repeatable field reads as missing.
- observability — the refusal text is unchanged for every kind that declares nothing.
- risks — callers that read a repeatable field must take a list. Only `inventory` declares one, and
  no caller of the factory reads it today.
- testing — AC1 to AC3 by `python -c` and the plant; the arm §7 declares.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` reads, through `build_records.py`'s record reader, a scratch
  `-inventory-1.md` record with one `Input` line, two `Of` lines and two `Verdict` lines, it reads
  `bound` with no refusal, and `Verdict` is a list of two in file order.
  Red when: a repeated `Of` or `Verdict` is refused, or the list loses an entry.
  fixture: a scratch repository under `%TEMP%/<short-name>`.
- **AC2** — When the same reader reads that record with a second `Input` line, it refuses naming
  `Input` and "is given twice". When it reads a deviation record with a repeated `Cause` line, it
  refuses the same way.
  Red when: the repeatable set leaks to a field or kind that did not declare it.
- **AC3** — When `python build_records.py --fixture --plant typed-kinds` runs in the memory-tree kit
  with its inventory record carrying two verdicts, every typed kind round-trips `bound`.
  Red when: the plant's inventory record reads malformed.

## 7. Gates

`policy fixtures` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest`

New arm: tools/memory-tree/build_records.py · covers AC1 AC2 AC3 · the `typed-kinds` plant's inventory record at two `Of` and two `Verdict` lines, staged by dropping `repeatable` from the inventory row · none

## 8. Open questions

- **F1 — Repeatable fields in the factory, or `inventory` untyped (id 13)?** Options: (a) a declared
  `repeatable` set per kind, with `inventory` naming `Of` and `Verdict`; (b) `inventory` in the untyped
  head. Both pass every written criterion. (a) keeps the both-ways file-name join and the field grades,
  and needs no new dependency, surface or carrier. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3,
  the most feature-rich survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 31 to 38, id 13
  (HIGH, item H5), on its sound fix, repairing TOOL-dIndexedDesign-34 S1.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-53, promoted by the round-1 spec audit of units 39 to 46; nothing else
  moved.

## 10. Reuse audit

The seam is the factory's own per-kind table and record reader, PLAY-dOrderedCharter-7 S7's
`build_records.py`, extracted from `deviation_join.read_record` (`tools/memory-tree/deviation_join.py:212`).
S1 adds one key to the table it already reads. The probe
`python tools/codebase-map/reuse_lookup.py "admit a repeated field in a typed record reader"` ranked
`read`, `read_text`, `records`, `field` and `read_conf`. None reads typed fields, so no seam fits beyond
the factory. The factory is unbuilt at base, a parent's, built before this build run.

Recall terms used: `python tools/memory-recall/query.py "how does the typed record factory treat a field given twice" --terms "typed record factory read_record given twice repeatable field inventory Of Verdict build_records per-kind table"`
