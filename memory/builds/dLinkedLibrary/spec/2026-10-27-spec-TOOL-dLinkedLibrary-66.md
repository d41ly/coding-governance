# TOOL-dLinkedLibrary-66 — the micro-format suite's lib-less arm stages its failing case as the stripped block

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 5 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-66-deviation-661.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-66-deviation-661.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-74 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 54 to 64
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md`) confirmed
finding **id 33 at HIGH**, report item **H1**. Id 24 shares the item and is its own unit,
`TOOL-dLinkedLibrary-65`. Item M1 (ids 1 and 34) is the same defect at medium, batched in
`TOOL-dLinkedLibrary-74`.

`TOOL-dLinkedLibrary-55` S2 makes its lib-less arm discriminate by running a second copy of the gate
with `. "$(dirname "$0")/lib/region.sh"` inserted after `set -u`, and asserting a non-zero exit. The gate
runs `set -u` with no `set -e` (`tools/check-microformats.sh:23`), and 54's inline block still defines
`region`, so that copy exits 0 on every correct gate: the audit reproduced `No such file or directory`,
then `microformats OK`, rc 0. The arm ships with the gate, so as written it is red at the close in gov
and in every default adopter, and a builder chasing the red improvises a break nobody priced.

This unit re-stages the arm's failing case as the defect it exists to catch, the inline `region_sh`
block replaced by a source line, and asserts exit 2. It repairs `TOOL-dLinkedLibrary-55` and builds one
step after it (order 5).

## 2. Scope (IN)

- **S1** — The staged copy. In `tools/check-microformats.test.sh`, the arm 55 S1 adds writes its second
  copy of the gate by deleting every line from `# >>> region_sh` to `# <<< region_sh` and writing `.
  "$(dirname "$0")/lib/region.sh"` in their place, one awk pass over the first copy; the inserted-line
  copy of 55 S2 is not written. Observed by AC1 and AC2.
- **S2** — The assertion. The arm runs the stripped copy from `$WORK` over the passing fixture and
  asserts exit 2 and that its output names `region`, one assertion through `say_ok` or `say_fail`, in
  place of 55 S2's non-zero assertion, so `FLOOR_ASSERTIONS` keeps the value 55 S3 sets. Observed by AC1
  and AC2.
- **S3** — The arm reads no message wording of the gate's: `region` appears both in bash's
  command-not-found line and in `TOOL-dLinkedLibrary-65`'s refusal, so the arm holds with or without that
  unit. Observed by AC1.

## 3. Non-goals (OUT)

- The gate's own guard and its message: `TOOL-dLinkedLibrary-65` (id 24).
- 55 S1's first run, the shipped gate copied alone and exiting 0: unchanged.
- Unit 55's acceptance ledger answer for its AC1: `TOOL-dLinkedLibrary-74`'s item for id 1.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-55` — S1's lib-less arm and S2's staged copy, which S1 re-stages as the stripped block and S2 asserts at exit 2 (id 33)
- **hands-off** `TOOL-dLinkedLibrary-74` — the stripped-block arm, which unit 74 records in unit 55's ledger (id 1 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-80` — the stripped-block arm, its assertion and its comment, which unit 80 corrects (ids 13, 23, 6 of the spec audit of units 65 to 74)

## 4. Design

### Evidence

- `tools/check-microformats.sh:23`: `set -u`, and no `set -e` anywhere in the file.
- 54 §4 "The read after S1": `block=$(region "$FILE" "$OPEN" "$CLOSE") || { …; exit 2; }`, so a gate whose
  `region` is undefined exits 2 whether or not 65's guard lands first.
- `tools/check-microformats.test.sh:12-13` find the gate beside the suite and make the arm's scratch,
  and `:23-41` build the one repository and fixture every arm reuses.

### Why the stripped block discriminates

A copy that still finds a library directory sources `region.sh`, defines `region` and exits 0, so the arm
reds when its copy step stops isolating the gate. A copy at a prefix with no library directory has no
`region`, and exits 2. The inserted-line copy cannot tell the two apart, because the inline block defines
`region` either way.

### Files touched (estimate)

- `tools/check-microformats.test.sh`: S1 to S3

### Alternatives rejected

- **Turning on `set -e` in the gate so 55's line fails.** It changes the shipped gate's exit table to
  rescue a fixture.
- **Asserting 65's exact message.** It couples a same-order parallel unit's wording to this arm, which
  then reds if either lands alone.

## 5. Production-readiness checklist

- security — the arm writes under the suite's own `mktemp -d` scratch, removed by its trap.
- perf / scale — one awk pass and one gate run, as 55 priced.
- error / empty / loading states — an awk pass that leaves the block in place makes the copy exit 0,
  and the arm reds naming the exit it saw.
- observability — the arm prints its exit and the first output line on a failure.
- risks — none beyond 55's.
- testing — AC1 and AC2 by probe; the arm itself is the close's.
- migration — none.
- user docs — none under `help/`: the suite's header names its arms.

## 6. Acceptance criteria

- **AC1** — When the arm's staged run is reproduced by hand in a scratch git repository under
  `%TEMP%/mf66` holding the suite's passing fixture as `charter.md`, with the gate at this pass's tip
  copied alone to the prefix `pfx` and its `region_sh` block replaced by the source line, `bash` running
  that copy from the root with `charter.md` exits 2 and prints a line holding `region`; with the canonical
  `region.sh` placed in the prefix's library directory the same copy exits 0.
  Red when: the staged copy exits 0 at a lib-less prefix, or the arm cannot tell an isolated copy from one
  beside a library.
- **AC2** — When `grep -n 'region_sh' tools/check-microformats.test.sh` and `grep -n '^FLOOR_ASSERTIONS='
  tools/check-microformats.test.sh` run at this pass's tip, the first prints the arm's strip step and the
  second the value 55 S3 set.
  Red when: the arm still inserts the source line beside the block, or the floor moved.

## 7. Gates

`micro-format gate selftest` · `micro-format definitions` · `foreign-prefix parity (every self-test at three prefixes)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/check-microformats.test.sh · covers AC1 AC2 · the stripped-block copy at a lib-less prefix, the failing case staged by the same copy beside a `region.sh` in the prefix's library directory · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 18 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 54 to 64, id 33 (HIGH, item
  H1).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-80, promoted from the spec
  audit of units 65 to 74; nothing else moved.

## 10. Reuse audit

The seam extended is the arm unit 55 adds and the suite's one reused scratch repository
(`tools/check-microformats.test.sh:12-41`); this unit changes how the arm builds its second copy and what
it asserts, not the harness. `python tools/codebase-map/reuse_lookup.py "refuse a micro-format gate whose
inline region reader is missing"` ranked `read`, `read_text`, `read_conf`, `read_journal` and `region`,
none a staged-break builder, so no existing seam fits beyond the suite being extended.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding of a spec audit repair a unit at the next order step" --terms "spec-audit promoted high finding repairs order staged break conf reader row grammar census indirection"`
