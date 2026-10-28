# TOOL-dIndexedDesign-42 — fork records are numbered within their build and joined by their `Fork` field, so two units' F1 forks never collide under the factory's per-build key

**Status:** OPEN · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 10 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-46 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 31 to 38
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md`)
confirmed finding **id 12 at HIGH**, report item **H4**, the item's only id. `TOOL-dIndexedDesign-8` S6
names a fork record `<date>-build-<unit id>-fork-<n>.md`, with `<n>` the F-item's number. F-items are
numbered per spec, so `F1` recurs in every unit that has a fork. `TOOL-dIndexedDesign-32` S1 makes
`fork` a typed kind, policed by `build_records.py`. That factory takes its `<n>` collision from
`tools/memory-tree/deviation_join.py`, whose `read_records` (`:283-292`) groups records by (build, n)
and marks every member malformed. Two units of one build that each record an F1 fork therefore read
malformed, naming each other.

This unit takes the first of the skeptic's two options, the one the factory already supports. A fork
record's file `<n>` is the next number free within its build. The F-item stays in the record's
`**Fork:**` field, and `check_fork_records` joins a record to its F-item by the Serves unit and that
field, never by the file name. The same per-build scope is the one `TOOL-dIndexedDesign-46` states for
`diff` (report ids 14 and 35). It repairs `TOOL-dIndexedDesign-32` and takes order 10, one above
unit 32's 9.

## 2. Scope (IN)

- **S1** — The number. A fork record's `<n>` is one more than the highest `-<kind>-<n>.md` number the
  build's `build/` folder holds for `fork`, so it is unique within the build, the factory's collision
  scope. Unit 8 S6's "`<n>` the F-item's number" is superseded, and the F-item is carried only by
  `- **Fork:** F<n>`. Observed by AC1.
- **S2** — The join. `check_fork_records` (unit 8 S8, `tools/memory-tree/design_lib.py`) keys each fork
  record by the unit id of its `**Serves:**` line and its `Fork` value, and never reads the F-item from
  the file name. Two records keyed alike are a finding naming both. Observed by AC1 and AC2.
- **S3** — The writer's guide. When `design_lib.py --decompose` reports a resolved F-item with no fork
  record, the finding names the file to write: the build's next free `-fork-<n>.md` and the `Fork`
  value. A hand writer copies one line, and the number is derived, never chosen. Observed by AC3.
- **S4** — The plants. Unit 8's `--plant fork-unrecorded` and `--plant fork-classes` write fork records
  numbered within the build. A new `--plant fork-two-units` writes an F1 fork for each of two units of
  one scratch build. Observed by AC1.

## 3. Non-goals (OUT)

- Re-keying the factory's collision on the unit id, the skeptic's second option. It changes a parent's
  extracted rule, which every typed kind would inherit (§4 Alternatives rejected).
- The `diff` number's scope and its allocator: report ids 14, 35 and 34, MEDIUM, batched into
  `TOOL-dIndexedDesign-46`.
- The fork kind's fields and closed sets: unit 32 S1 and unit 8 S6. The closed sets' one home is report
  id 8's item in `TOOL-dIndexedDesign-46`.
- The report's left-shift checklist entry. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-32` — S1's typed `fork` kind and the factory's per-build collision it binds, under which S1 numbers fork files (id 12)
- **consumes-from** `TOOL-dIndexedDesign-8` — S6's fork home and `Fork` field, S8's `check_fork_records` and the fork plants, which S1 to S4 re-number and re-key (id 12)
- **hands-off** `TOOL-dIndexedDesign-53` — S1's count, S3's findings and AC1 to AC3's command form, which that unit's S4, S13 and S15 change at this unit's pass: tracked and on-disk files, consecutive numbers, and `--decompose-fixture` (ids 9, 15 and 28)

## 4. Design

### Evidence

- `tools/memory-tree/deviation_join.py:160`, `RECORD_NAME`, captures the build slug and `<n>`.
  `:283-292` group the records by `(r["build"], r["n"])` and mark each member of a group of two or more
  "shares deviation-{n} with …". The docstring at `:11-12` says `<n>` is unique within its build. Read
  2026-10-28.
- PLAY-dOrderedCharter-7 S7 extracts "the `<n>` collision" from that module into `build_records.py`.
  PLAY-dOrderedCharter-42 S3 applies the file-name join to every typed kind.
- The tree's own deviation records follow the per-build scope: units 10 and 4 of one build hold
  deviation-101, -102 and -41.
- Unit 8 S6 already writes `- **Fork:** F<n>` into each record, and its id `<unit id>#F<n>` reads the
  unit from the Serves line and the F-item from that field.

### Data model

```
memory/builds/tFix/build/2026-10-28-build-TOOL-tFix-1-fork-1.md   **Serves:** fork TOOL-tFix-1   - **Fork:** F1
memory/builds/tFix/build/2026-10-28-build-TOOL-tFix-2-fork-2.md   **Serves:** fork TOOL-tFix-2   - **Fork:** F1
```

Both bind. The join keys them `TOOL-tFix-1#F1` and `TOOL-tFix-2#F1`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `fork-two-units` | `--plant` value of `design_lib.py` | none |

### Migration

None: no fork record exists at base, and unit 8's checks grade only from `SPEC_FORK_RECORD_CUTOFF`,
which ships blank (`TOOL-dIndexedDesign-40` S2).

### Rollout

Live at its pass, order 10, beside `TOOL-dIndexedDesign-33`, `TOOL-dIndexedDesign-34` and
`TOOL-dIndexedDesign-5`. Unit 34 also writes `design_lib.py`, so `--dispatch` sequences the two.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S2 to S4

### Alternatives rejected

- **Key the factory's collision on (build, unit, n).** Lost to its reach: the rule is a parent's,
  extracted for every typed kind, and the tree's deviation records already number within the build.
  A per-unit key would also let two deviation records of one build share a number.
- **Keep `<n>` the F-item's number, and name fork files `-fork-<unit seq>-<n>.md`.** Lost to the typed
  grammar `-<kind>-<n>.md`, which a second number breaks.

## 5. Production-readiness checklist

- security — N/A: no new write path; the hand writer gains a derived file name.
- perf / scale — none.
- error / empty / loading states — two records keyed alike are a finding naming both; a build with no
  fork record is graded by nothing, as unit 8 says.
- observability — S3's finding names the exact file to write.
- risks — a hand writer could still pick a used number. The factory's collision marks both malformed,
  so the slip is loud.
- testing — AC1 to AC3 by the CLI and `python -c` over scratch plants.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python design_lib.py --decompose tFix --plant fork-two-units` runs in the memory-tree
  kit, the two records `-fork-1.md` and `-fork-2.md` each read `bound` through `tree_lib.read_bindings`,
  and the command exits 0 with both F1 forks joined.
  Red when: either record reads malformed, or one F1 is joined to the other unit's record.
  fixture: a scratch repository under `%TEMP%/<short-name>`.
- **AC2** — When the same plant is rewritten with both records numbered `-fork-1.md`, `read_bindings`
  marks both malformed naming each other. With two records of one unit both `Fork: F1`,
  `--decompose` exits 1 naming the unit and `F1`.
  Red when: the per-build collision is silent, or a doubled F-item passes.
- **AC3** — When `--decompose` runs over `--plant fork-unrecorded` with one fork record already in the
  build, its finding names `-fork-2.md` and `Fork: F1`.
  Red when: the named number is the F-item's, or no file is named.

## 7. Gates

`policy fixtures` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest`

New arm: tools/memory-tree/design_lib.py · covers AC1 AC2 · the `fork-two-units` plant, staged by numbering a fork file by its F-item so two units collide · none

## 8. Open questions

- **F1 — Number fork files within the build, or key the factory's collision by unit (id 12)?** Options:
  (a) number within the build and join by the `Fork` field; (b) re-key the factory. (b) changes a
  parent's rule for every typed kind and breaks the deviation convention, so it fails an existing
  acceptance criterion of PLAY-dOrderedCharter-7 S7, "its verdicts unchanged" (veto 1). RESOLVED
  (agent, 2026-10-28, delegated): (a), rung 3, the one survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 31 to 38, id 12
  (HIGH, item H4), on its sound fix, repairing TOOL-dIndexedDesign-32 S1 and TOOL-dIndexedDesign-8 S6
  and S8.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-53, promoted by the round-1 spec audit of units 39 to 46; nothing else
  moved.

## 10. Reuse audit

The seam is the factory's per-build collision, extracted from `deviation_join.read_records`
(`tools/memory-tree/deviation_join.py:268-293`), and unit 8's existing `Fork` field. S1 adopts the
first, and S2 joins on the second, so no new key or rule is written. The probe
`python tools/codebase-map/reuse_lookup.py "number a hand-written build record within its build and join it by a field"`
ranked `build`, `records`, `field`, `build_commit` and `build_fixture`. None numbers or joins a typed
record, so no seam fits beyond the factory's rule.

Recall terms used: `python tools/memory-recall/query.py "how is a fork record numbered and joined to its F-item" --terms "fork record F-item Fork field build_records collision per-build number check_fork_records typed kind"`
