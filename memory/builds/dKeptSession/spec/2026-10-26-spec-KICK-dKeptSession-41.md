# KICK-dKeptSession-41 — the three catalogue rows that already stand given their summary and usage, one row per name, never a second minted beside them

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 29 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-41-deviation-411.md](../build/2026-10-26-build-KICK-dKeptSession-41-deviation-411.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 45 at HIGH**, report item **H8**. Ids 7 and 34 are the same defect at MEDIUM,
item M4, batched into `KICK-dKeptSession-44`. Fixing one item fixes the other: this unit makes the
fix, and unit 44's M4 items observe it.

`KICK-dKeptSession-8`, `-11` and `-17` each run `core.py new policy-key` unconditionally for
`actions.free`, `notify.owner` and `attendance`, and dGroundRules' catalogue already holds all three
rows with owner dKeptSession and the same defaults. The factory then appends a duplicate `[[key]]`
row or its wrapped check reds and restores the file, and each unit's criterion reads `r[0]` of the
row that already stands, so it is green before the unit is built. This unit re-grounds the three rows
the way `KICK-dKeptSession-13` S5 and `KICK-dKeptSession-14` S2 ground theirs: it writes each standing
row's `summary` and `usage`, drains it from `unsummarised-keys.txt`, and leaves exactly one row per
name. It repairs three units, so it takes the order past every unit of the build (order 29).

## 2. Scope (IN)

- **S1** — id 45. The text. In `tools/policy/catalogue.toml`, the standing rows gain:
  - `actions.free` (`:223` at `3c8c4718a`): `summary = "What a tool call outside the item in flight
    may do: read-only probes, item reads only, or anything recorded."`, `usage = 'actions.free =
    "item-reads-only"'`;
  - `notify.owner` (`:543`): `summary = "Which events report the build's progress to the owner as
    one progress line."`, `usage = 'notify.owner = "park-and-landing"'`;
  - `attendance` (`:60`): `summary = "Whether the owner attends a run: the breakpoints placed for
    them and the questions asked live."`, `usage = 'attendance = "confirm-steps"'`.
  Observed by AC1.
- **S2** — id 45. One row per name. Where a build pass of unit 8, 11 or 17 appended a second
  `[[key]]` row for its name, the appended row is deleted and the standing dGroundRules row kept, so
  each name has exactly one row. Observed by AC1.
- **S3** — id 45. The drain. `python tools/policy/policy.py lists --write` regenerates
  `tools/policy/unsummarised-keys.txt`, which then lists none of the three. Observed by AC2.
- **S4** — id 45. `KICK-dKeptSession-8` S1 and AC8, `KICK-dKeptSession-11` S1 and AC6, and
  `KICK-dKeptSession-17` S1 and AC7 are superseded by name here: each unit's row is the standing one,
  and its acceptance ledger answers its criterion with AC1's output. Observed by AC1.

## 3. Non-goals (OUT)

- The keys' readers: units 8, 11 and 17, unchanged.
- The factory's refusal of a name that already stands, the report's left-shift gate: it is
  TOOL-dDeclaredLoop-6 S4's `new policy-key`, another build's surface, handed off below.
- The JSON mirror: a row's `summary` and `usage` are not mirrored values, so
  `.governance/policy.json` does not move.

### Edges

- **consumes-from** `KICK-dKeptSession-8` — S1's `actions.free` row, which this unit grounds on the standing row (id 45)
- **consumes-from** `KICK-dKeptSession-11` — S1's `notify.owner` row, which this unit grounds on the standing row (id 45)
- **consumes-from** `KICK-dKeptSession-17` — S1's `attendance` row, which this unit grounds on the standing row (id 45)
- **hands-off** `KICK-dKeptSession-44` — the one row per name and the drained list, which that unit's M4 items, ids 7 and 34, observe
- **hands-off** external — TOOL-dDeclaredLoop-6 S4's `new policy-key` refusing a name the catalogue already holds, the report's left-shift gate for this class
- **hands-off** `KICK-dKeptSession-56` — the catalogue edit's `.governance/policy.json` and §7's legs, the batch's S29 and S26 (ids 40, 35)

## 4. Design

### Evidence

- `git show 3c8c4718a:tools/policy/catalogue.toml` holds `actions.free` (default `read-only-probes`),
  `notify.owner` (`turn-micro-formats`) and `attendance` (`unattended`), each owner dKeptSession and
  none with a `summary` (read with `tomllib`, 2026-10-26); the audit cites `:223`, `:543` and `:60`.
- `unsummarised-keys.txt` at `3c8c4718a` lists the three at lines 5, 142 and 11; its header says a
  row leaves it once it has both fields and `lists --write` runs.
- `KICK-dKeptSession-13` S5 and `KICK-dKeptSession-14` S2 run the factory "only where the landed
  catalogue lacks the row", and units 7 and 21 say "No catalogue rows".

### Inventory

No identifier is minted.

### Migration

None: summaries are prose fields no reader compares.

### Files touched (estimate)

- `tools/policy/catalogue.toml`: S1 and S2
- `tools/policy/unsummarised-keys.txt`: S3, regenerated

### Alternatives rejected

- **Amending units 8, 11 and 17 in place.** The audit's disposal promotes and never folds, so the
  repair is its own unit and the three specs are superseded by name.
- **Leaving the duplicate rows.** `read_catalogue_row` would answer the first, and the second would
  be a row nobody reads.

## 5. Production-readiness checklist

- security — none: prose fields of three rows.
- perf / scale — none.
- error / empty / loading states — a factory restore that left no duplicate makes S2 a no-op.
- observability — `lists --check` names any row still unsummarised.
- risks — a sibling build editing the same rows' text merges line by line.
- testing — the probes of §6.
- migration — none.
- user docs — the three units' help sections, unchanged.

## 6. Acceptance criteria

- **AC1** — When `python -c "import tomllib, sys; d=tomllib.load(open(sys.argv[1], 'rb'))['key'];
  print([(n, len([k for k in d if k['name'] == n]), [k.get('summary', '')[:12] for k in d if k['name']
  == n]) for n in ('actions.free', 'notify.owner', 'attendance')])" catalogue.toml` runs in the policy
  kit, each name shows one row and its summary opens with S1's text.
  Red when: a name has two rows, or its row carries no summary, which is the base state.
- **AC2** — When `grep -cx 'actions.free\|notify.owner\|attendance' unsummarised-keys.txt` runs in the
  policy kit after `policy.py lists --write`, it prints `0`.
  Red when: a row stays unsummarised, as it is at `3c8c4718a`.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The policy kit's `policy check` leg grades `unsummarised-keys.txt` once dGroundRules has landed it.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H8 (id 45).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared

## 10. Reuse audit

The seam is the standing catalogue row and dGroundRules' `lists --write`, the one writer of
`unsummarised-keys.txt`, grounded as `KICK-dKeptSession-13` S5 and `KICK-dKeptSession-14` S2 ground
their rows. No code is minted; `python tools/codebase-map/reuse_lookup.py "give a catalogue row its
summary and drain it from the unsummarised list"` ranked `rows`, `row`, `extract_row`,
`read_id_list` and `declared_list` by name stem only, none a catalogue writer: the policy kit is not
at this base, so no existing seam in the tree fits and the branch's catalogue is the one edited.

Recall terms used: `python tools/memory-recall/query.py "how does a unit ground a catalogue key that
already stands" --terms "catalogue row summary usage unsummarised-keys lists --write new policy-key
actions.free notify.owner attendance standing"`
