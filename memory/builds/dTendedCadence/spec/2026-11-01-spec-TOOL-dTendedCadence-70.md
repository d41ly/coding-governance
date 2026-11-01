# TOOL-dTendedCadence-70 — the landing's staleness cases run with the payload object already local: in the clone that landed it, and in the walk's own clone

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 22 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-70-deviation-701.md](../build/2026-11-01-build-TOOL-dTendedCadence-70-deviation-701.md) | deviation | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-60-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-60-promoted-fix-brief.md) | research | TOOL-dTendedCadence-60 TOOL-dTendedCadence-67 TOOL-dTendedCadence-69 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 36 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, which shares item H3 with id 4 (TOOL-dTendedCadence-69). Unit 50's AC1 and AC2 both run in the
second clone (spec-50 :136-141): after AC1 the first payload's object is local, so AC2's older text
skips the fetch, prints `unchanged` and exits 0 where AC2 expects `superseded`. Its outcome depends on
the order the cases run, and no case lands an older payload where the object was built, the walk's own
clone. This unit states the cases with the object local, so the staleness check is observed on the
path the defect took.

## 2. Scope (IN)

- **S1** — Unit 50 AC2, in place. Spec-50 AC2 reads: when the second clone has landed the first
  record (AC1), the walk's clone pushes a second record under the same key, and the second clone,
  which already landed the first record, lands the first text's values again, `land` exits 1
  printing `superseded` and the file still holds the first record's bytes. Corrected in spec-50's
  text, a rev bump with a §9 line naming review id 36. Observed by AC1.
- **S2** — The walk-clone case. One drift-audit selftest case lands the first text's values in the
  walk's own clone, where `write_record_landing` built the object, after the second record was pushed,
  and requires exit 1 `superseded` with no file written. Observed by AC2.
- **S3** — The order. Both cases assert `git cat-file -e <first payload>^{commit}` succeeds before
  `land` runs, so each states its precondition instead of inheriting it from the case before. Observed
  by AC2.

## 3. Non-goals (OUT)

- The check itself: TOOL-dTendedCadence-69.

### Edges

- **consumes-from** `TOOL-dTendedCadence-50` — §6 AC2, rewritten in place, and its fixture, whose clones these cases use
- **consumes-from** `TOOL-dTendedCadence-69` — `read_remote_record_ref` and the always-run verdict it answers, which these cases observe with the object local

## 4. Design

Each case asserts its own precondition, the object local, so reordering the cases cannot turn a
`superseded` expectation into a skipped check. At base, before TOOL-dTendedCadence-69, the walk-clone
case prints `unchanged` or `written` and exits 0: that is its staged red.

### Files touched (estimate)

- `tools/drift-audit/selftest.py`: S2, S3
- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-50.md`: S1

## 5. Acceptance criteria

- **AC1** — When `awk '/^- \*\*AC2\*\*/,/Red when/' 2026-11-01-spec-TOOL-dTendedCadence-50.md` runs in
  the spec folder, piped to `grep -c "already landed"`, it prints 1, where at base it prints 0; S1's
  text spells "the second clone, which already landed the first record".
  Red when: unit 50's criterion still lands in an order-dependent clone.
- **AC2** — When the selftest cases of S2 and S3 run, each first prints the object present, then
  `land` exits 1 printing `superseded`, the verdict on the sha `read_remote_record_ref` answers, and
  the record path's bytes are unchanged; with the check of TOOL-dTendedCadence-69 reverted to the
  cache-miss branch, both cases fail.
  Red when: a local payload object lets an older record land.

## 6. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/drift-audit/selftest.py · covers AC2 · an older payload landed with its object local in the walk clone and in a clone that already landed it, staged against the cache-miss-only check · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 36 (HIGH, item H3) of the round-1 spec
  audit of units 49 to 59.

## 9. Reuse audit

The seam is unit 50's own fixture of two clones and a bare remote, extended by one case and one
precondition. `python tools/codebase-map/reuse_lookup.py "check a remote ref names a commit before
landing"` ranked name stems only, so no existing seam fits beyond that fixture.

Recall terms used: `python tools/memory-recall/query.py "how does a landing know its payload is the
newest record of its key" --terms "superseded payload object local walk clone order-dependent fixture
landing refs gov maintain-record"`
