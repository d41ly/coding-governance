# TOOL-dGroundRules-53 — the trap row's shell verdict observed with the library sourced by its tracked path and the trap pair whole

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-53-deviation-41.md](../build/2026-10-23-build-TOOL-dGroundRules-53-deviation-41.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-53-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-task.md) | research | TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run, round 1
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`),
confirmed finding **id 5 at HIGH** under item **H1**, which it shares with ids 9, 12, 14 and 19.
Id 5 is H1 seen from correctness. `TOOL-dGroundRules-44` AC2 runs `TRAP_SH`, which sources the
unattended library by its bare file name and passes the trap row's second path stripped to its
basename. Run from the repository root, the source fails and the call prints `127`, so the built
tree can never show the `1` AC2 expects. With the operand stripped, a raw prefix compare answers the
pair as disjoint too, so the `0` AC2 expects under `RAW_BOTH` can never be shown either. Id 12
names this same literal, and this unit carries it for both, spelled once; id 9's route, AC2 read
through the repaired overlap probe, is `TOOL-dGroundRules-54`'s. This unit is id 5's
promotion: the shell half of the trap row's verdict gets a literal that sources the library by its
tracked path and passes the trap pair whole, and `TOOL-dGroundRules-44` AC2 is observed with it. It
repairs `TOOL-dGroundRules-44`, which sits at order 14, so it builds at order 17.

## 2. Scope (IN)

- **S1** — The literal. `TRAP_SH_WHOLE` (§4) sources `tools/unattended/lib-unattended.sh` by its
  tracked path and calls `overlaps` on the trap row exactly as `TOOL-dGroundRules-44` S1 spells it,
  both operands whole. It stands in `TRAP_SH`'s place wherever `TOOL-dGroundRules-44` §6 names it.
  Observed by AC1.
- **S2** — `TOOL-dGroundRules-44` AC2 restated. On the built tree, `TRAP_PY` of
  `TOOL-dGroundRules-44` §6 prints `False` and `TRAP_SH_WHOLE` prints `1`. Observed by AC2.
- **S3** — Its red half restated. In a scratch copy where `RAW_BOTH` of `TOOL-dGroundRules-44` §6
  is staged, the same two print `True` and `0`. Observed by AC3.

## 3. Non-goals (OUT)

- Any edit to the text of `TOOL-dGroundRules-44` §6. That spec gains only the hands-off line to this
  unit; its `TRAP_SH` is read through S1, never respelled in place.
- `TRAP_PY`, `TRAP_PROBE` and `RAW_BOTH`. All three are whole in `TOOL-dGroundRules-44` §6 and
  this unit names them there.
- Observing the trap row through the repaired overlap probe, which the review offers as the better
  route: `TOOL-dGroundRules-54`, a second witness of AC2 that shares no spelling with this unit's.
- The not-a-trap staging and the row check's refusal: `TOOL-dGroundRules-57` and
  `TOOL-dGroundRules-56`. The class record: `TOOL-dGroundRules-55`.
- Any change to `overlaps`, `covers` or `check_writes_intersect`.

### Edges

- **consumes-from** `TOOL-dGroundRules-44` — the trap row S1 spells, `TRAP_PY` and the `RAW_BOTH` staging, which S2 and S3 restate AC2 over; without them there is no row and no red case to observe

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `7810198ad`, from the repository root.

- `TOOL-dGroundRules-44` §6 spells `TRAP_SH` with `. lib-unattended.sh` and the operands
  `tools/policy/a` and `ab.py`; its S1 row and `TRAP_PY` spell the second operand
  `tools/policy/ab.py`. The spec has one committed revision (`d794a81bc`), so no earlier text holds
  the original literal; the review's sound fix and the inventory of the closing brief both give it.
- `TRAP_SH` as spelled printed `lib-unattended.sh: No such file or directory`,
  `overlaps: command not found` and `127`.
- `tools/unattended/lib-unattended.sh:745-750` defines `covers` as "b is a, or sits under it" over
  normalised paths, and `overlaps` as `covers` in either direction.
- `TRAP_SH_WHOLE` (below) printed `1`.
- In a scratch copy of that library whose `covers` line 747 was staged to
  `case "$_cb" in "$_ca"*) return 0 ;; esac`, a raw prefix compare, `TRAP_SH_WHOLE` printed `0`.
  With the stripped operand `ab.py` in its place it printed `1` under the same staging, which is
  why the stripped literal cannot show AC2's red half.
- `check_writes_intersect` is not yet in `tools/memory-tree/design_lib.py`; `TOOL-dGroundRules-32`
  (order 10) adds it, so `TRAP_PY` is first runnable once that unit is built.

### The literal

It is spelled here, in §4, so the paths join over §6 never grades its operands and no sweep can
respell it to a basename. Run it verbatim from the repository root or the root of a scratch copy.

```text
TRAP_SH_WHOLE = bash -c '. tools/unattended/lib-unattended.sh; overlaps tools/policy/a tools/policy/ab.py; echo $?'
```

### Inventory

No identifier is minted. `TRAP_SH_WHOLE` is a literal label inside this spec.

### Files touched (estimate)

None. The unit restates a criterion and writes no product file.

### Alternatives rejected

- **`TRAP_SH` and `TRAP_PY` dropped, and AC2 observed only through the repaired overlap probe.**
  The review calls this the better option, because the pair would then be spelled only in the suite,
  and `TOOL-dGroundRules-54` takes it for id 9. Keeping `TRAP_SH_WHOLE` as well leaves AC2 a witness
  that runs on today's tree and rests on no other repair.
- **`TOOL-dGroundRules-44` §6 respelled in place.** The disposal's write set gives that spec its
  hands-off lines only, so the corrected literal lives here and is named there.
- **One unit each for ids 5 and 12.** Both name one literal, and two units restating it would be
  the second spelling these findings condemn.

## 5. Production-readiness checklist

- security — N/A: a read-only shell probe of a tracked library.
- perf / scale — one shell start per run.
- error / empty / loading states — a source that fails prints `127`, which AC1 reds.
- observability — the probe prints the call's exit code.
- risks — none: no product file changes.
- testing — AC1 to AC3.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

Every command runs from the repository root unless it says otherwise. A scratch copy is a git clone
of this repository under `%TEMP%/gr53`, checked out at the commit under test. `TRAP_SH_WHOLE` is
spelled in §4. `TRAP_PY` and `RAW_BOTH` are spelled in §6 of `TOOL-dGroundRules-44`.

- **AC1** — When `TRAP_SH_WHOLE` runs, it prints `1` and no `No such file or directory` line.
  Red when: the library is sourced by a name that does not resolve from the root, so `overlaps` is
  undefined and the call prints `127`.
- **AC2** — When `TRAP_PY` and `TRAP_SH_WHOLE` run on the built tree, they print `False` and `1`.
  Red when: either rule answers the trap row as intersecting.
  fixture: `check_writes_intersect`, which the tree holds once `TOOL-dGroundRules-32` is built.
- **AC3** — When `RAW_BOTH` is staged in the scratch copy and `TRAP_PY` and `TRAP_SH_WHOLE` run
  there, they print `True` and `0`.
  Red when: the shell literal's operands are a pair a raw prefix compare and containment answer
  alike, so the staged regression passes unseen.

## 7. Gates

`memory hygiene` · `spec-tokens self-test`

The suite arm that stages `RAW_BOTH` is `TOOL-dGroundRules-44`'s `New arm:` line; this unit adds no
arm.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 5 (HIGH, item H1) of the closing diff
  review round 1, with id 12 carried on the same literal, from the review's sound fix, with
  `TRAP_SH`, `TRAP_SH_WHOLE` and a raw-prefix staging of `covers` run on 2026-10-23.

## 10. Reuse audit

The seam reused is `overlaps` (`tools/unattended/lib-unattended.sh:750`), called exactly as
`TOOL-dGroundRules-44` S1 names the row; nothing is built beside it. `python
tools/codebase-map/reuse_lookup.py "run one suite function alone on a staged row to observe its
refusal line"` ranked `rows`, `row` and `run`, name-stem hits that hold no overlap probe, so no
existing seam fits the literal beyond the library it sources. The recall probe returned
`TOOL-dGroundRules-45`, `TOOL-dGroundRules-42`, `TOOL-dGroundRules-47` and `TOOL-dGroundRules-44`;
all agree with source, and `TOOL-dGroundRules-47` S1's verbatim re-run is the step this unit's
evidence records.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion that reads a fixture
instead of running the check repaired" --terms "acceptance criterion fixture side read never runs
check stripped literal respelled trap row overlap arm suite function"`
