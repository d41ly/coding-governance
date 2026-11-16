# TOOL-aHastenedSweep-7 — the hygiene suite's assertion floor pinned to the count the close measured, so a stranded block of arms reds it

**Status:** SPECCED · rev-1 · 2026-11-16 · node a · Tier-1 · base f25308f0 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-16-prompt-TOOL-aHastenedSweep-7-brief.md](../prompts/2026-11-16-prompt-TOOL-aHastenedSweep-7-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The hygiene suite's assertion floor sits at 719 while a full run of the suite prints 742, so
stranding any block of 23 or fewer arms still passes, and the floor arm `TOOL-aHastenedSweep-6`
declared for unit 3's five assertions cannot go red. This unit moves `FLOOR_ASSERTIONS` to the
measured count, so the floor arm reds on a stranded block again.

## 2. Scope (IN)

- **S1** — `FLOOR_ASSERTIONS` in `tools/memory-tree/check-memory-hygiene.test.sh` moves from 719 to
  742, the count the suite printed at `0c1935569`. Observed by AC1 and AC3.
- **S2** — One `# RAISED 719 -> 742` comment, in the shape of the entries above it, directly above
  the floor line. It names `TOOL-aHastenedSweep-7`, says the floor sat below the printed count before
  this build began, says this unit pins it to the count the close measured, and marks that count
  PINNED with its sha, date and node. Observed by AC2.
- **S3** — The correction to the CLOSED spec 6, recorded in §4 of this spec and not in spec 6.
  NOT OBSERVED — a record of what spec 6 claimed wrongly, with no code to observe; AC3 is the
  observation spec 6's AC5 lacked.

## 3. Non-goals (OUT)

- Any other arm, assertion, RAISED line or suite change: the floor line and one new comment are
  the whole diff to the suite.
- Any edit to spec 6. It is CLOSED and stays frozen; §4 carries its correction.
- A gate comparing a floor with the printed count. The class is already filed as the ask
  `assertion-floor-left-below-the-added-arms`, which spec 6's non-goals hand to the main loop.
- Accounting for the 23 assertions arm by arm. The floor pins the printed count, as the
  `TOOL-aRepatriatedFork-42` entry above it did, and the RAISED line says the gap predates the build.
- No self-test suite and no bar inside the pass, a sliced suite included. The pass runs `bash -n`
  and the greps; the main loop observes the floor red and green at the close.
- A pass commit without its acceptance ledger at
  `memory/builds/aHastenedSweep/build/2026-11-16-build-TOOL-aHastenedSweep-7-1-acceptance-ledger.md`,
  and any edit after the commit that sets this spec CLOSED.
- `memory/builds/dDeclaredLoop/`, its run's worktree, its branch and its run-state file.

## 4. Design

### Evidence

Read at the build's tip `dc8d077e1` on 2026-11-16.

- The floor is `FLOOR_ASSERTIONS=719` at
  `tools/memory-tree/check-memory-hygiene.test.sh@78d46e3185e1:4876`, and its comparison at `:4877`
  is `n + n_skip` against it, printing `FAIL executed $n assertions against a floor of ...` and
  setting `st=1` when short. The last RAISED entry, `:4872-4875`, is spec 6's `710 -> 719`.
- The suite prints `PASS ($n assertions)` at `:4879`, which counts `n` alone. `n_skip` grows only in
  four branches, `:3791`, `:3880`, `:3937` and `:4686`, each taken when a sibling kit is absent and
  each echoing a line that opens `skip `. This repository carries all four siblings:
  `tools/workflows/tier2-review.js`, `tools/playbook/render_playbook.py`, `tools/check-spec-tokens.py`
  and `tools/memory-recall/`. So on node a `n_skip` is 0 and the printed 742 is the compared sum.
- The base floor was `FLOOR_ASSERTIONS=708` at `f25308f0`. Since the base, three commits touched the
  suite: `c0008f704` (unit 3, five assertions), `cf64f39df` (unit 4, two) and `a46ef3919` (unit 6,
  four). 708 + 11 = 719, which is today's floor. The close printed 742, so the suite at the base
  already executed 742 - 11 = 731 against a floor of 708 (DERIVED from these figures): the 23-arm gap
  predates the build, and this build's own arms are all counted.
- The `TOOL-aRepatriatedFork-42` entry at `:4796-4799` is the precedent for raising "to the PRINTED
  count", and the `-ge` comparison makes a floor at the printed count the tightest legal value.
- `tools/check-testsuite-counts.sh` reads only the shape `^FLOOR_ASSERTIONS=[0-9]+$` and refuses
  zero (`:93-94`), so 742 passes it unchanged.

### The change

Replace the floor line, and add above it, after spec 6's entry:

```bash
# RAISED 719 -> 742 by TOOL-aHastenedSweep-7, to the PRINTED count: the suite printed PASS (742
# assertions) at 0c1935569 (PINNED, 2026-11-16, node a, n_skip 0). The floor sat 23 below the count
# before this build began; this build's eleven are the two raises above, so this pins the floor to
# the measured count and a stranded block of any size reds it.
FLOOR_ASSERTIONS=742
```

The comment wording may change; S2's four facts may not.

### Correction to spec 6

Spec 6 (`spec/2026-11-16-spec-TOOL-aHastenedSweep-6.md`, CLOSED at rev-2) stays frozen. Where it and
this section disagree, this section holds.

- AC5's figure says "the floor equals" the close's printed count, and its New-arm line for AC5 says
  unit 3's block wrapped in `if false; then … fi` drops five assertions under the floor. Neither
  held: the close printed 742 against 719, so dropping five leaves 737, still above the floor. AC3
  below is the observation that arm needed.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/builds/aHastenedSweep/build/2026-11-16-build-TOOL-aHastenedSweep-7-1-acceptance-ledger.md`

### Rollout

One pass at order 6, after `TOOL-aHastenedSweep-6` is CLOSED. The spec lands in a records commit
before the code, and the status flip to CLOSED is the pass's last change.

### Alternatives rejected

- **A floor below the count, for headroom.** Any slack is the size of the block that can strand
  silently, which is the defect this unit closes.
- **Counting the 23 arms by reading and raising by that sum.** The printed count is the measurement
  the `-ge` compares against, and a reading can miscount where the run cannot.

## 5. Acceptance criteria

- **AC1** — When `grep -cx 'FLOOR_ASSERTIONS=742' tools/memory-tree/check-memory-hygiene.test.sh`
  runs it prints 1, `grep -c '^FLOOR_ASSERTIONS=' tools/memory-tree/check-memory-hygiene.test.sh`
  prints 1, and `bash -n tools/memory-tree/check-memory-hygiene.test.sh` exits 0.
  Red when: the floor line is left at 719, written twice, or the edit breaks the suite's syntax.
  figure: 742 is PINNED, the suite's printed count at `0c1935569` on node a, 2026-11-16.
- **AC2** — When `grep -n 'RAISED 719 -> 742' tools/memory-tree/check-memory-hygiene.test.sh` runs
  it prints one line, directly above the floor line, and that comment names `TOOL-aHastenedSweep-7`,
  `0c1935569`, `PINNED` and that the floor sat below the count before this build began.
  Red when: the raise carries no RAISED line, or the line omits the unit, the pin or the pre-build gap.
- **AC3** — When the main loop runs the hygiene suite at the close, it prints `PASS (742 assertions)`
  and no line opening `skip `. With unit 3's block wrapped in `if false; then … fi` as the staged
  break, the run prints `FAIL executed 737 assertions against a floor of 742` and exits non-zero.
  Restored, it prints the PASS line again.
  Red when: the floor sits below the printed count, so the stranded block passes, or above it, so
  the green run fails.
  permission: the suite run is the main loop's at the close, under a `Pass: none` commit; a unit pass
  does not run it.
  cost: one full suite run and one staged run on node a.
  figure: 737 is DERIVED, 742 less unit 3's five assertions; a different printed count at the close
  moves the floor to it and this figure with it, recorded in the ledger.

## 6. Gates

`memory-hygiene self-test` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC3 · unit 3's block wrapped in `if false; then … fi` drops five assertions under the floor · `FLOOR_ASSERTIONS` 719 -> 742

A pass checks its own change with `bash -n`, the AC1 and AC2 greps, the lexicon and the spec-token
checker. The close runs the bar once and observes the floor arm red then green.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-16 · initial draft from `prompts/2026-11-16-prompt-TOOL-aHastenedSweep-7-brief.md`,
  grounded at the build's tip `dc8d077e1`.

## 9. Reuse audit

The seam this unit extends is the floor line and its RAISED history in
`tools/memory-tree/check-memory-hygiene.test.sh`, in the `TOOL-aRepatriatedFork-42` "to the PRINTED
count" shape; no new code. `python tools/codebase-map/reuse_lookup.py "a suite's assertion floor
pinned to the count a full run prints"` returned only generic `run` and `counts` name-stem hits, so no
other seam fits. Recall named the closing review's round-1 M1 fix, which asked for exactly this
printed-count confirmation and a stranded-block red, and `TOOL-dUnstalledConvoy-19`, an earlier
floor that sat sixty under its executed count.

Recall terms used: `python tools/memory-recall/query.py "how is a self-test suite's assertion floor
raised to the printed count" --terms "FLOOR_ASSERTIONS RAISED floor assertions printed count stranded
block n_skip unreachable arms"`
