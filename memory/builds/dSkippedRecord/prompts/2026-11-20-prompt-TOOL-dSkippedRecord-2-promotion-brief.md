# Brief — dSkippedRecord: the closing review's two LOW items, promoted

**Serves:** research TOOL-dSkippedRecord-2

## The prompt

> The AC1 arm checks only the skip line's prefix, so the 'last committed at <hash>' ending is never checked. The closed rev-1 spec still describes the addfail and difffail arms as GIT function overrides, but red fix 26f99cdb0 replaced them with a PATH git shim.

## The brief

### Goal
Dispose both confirmed findings of the round-1 closing review
(`reviews/2026-11-20-review-TOOL-dSkippedRecord-1-closing-diff-round1.md`) by the build method's severity rule:
the two LOW items are batched into `TOOL-dSkippedRecord-2`.

### Items
1. The review's item 1 (finding 2). The `same` call of `run_render_helper` in `tools/unattended/unattended.test.sh`
   asserts the whole skip line, its trailing commit hash included: the short hash of the fixture commit that
   committed `memory/builds/tRun/build/lu-record.md`, read inside the helper's fixture, never typed.
2. The review's item 2 (finding 3). Unit 1's spec is CLOSED and stays frozen. Unit 2's spec records the
   as-built failed-stage mechanism: the `addfail` and `difffail` modes write one `git` shim under the fixture's
   git dir and put it first on PATH, spelled by the shell's own `pwd`, and it hands every other call to the real
   git. Its revision log names the correction to unit 1's suite-arm design and the red fix that caused it.

### Acceptance
Item 1: the `same` arm fails when the skip line's hash is blanked or wrong (a staged break that drops the
`GIT log` substitution's output, or points it at another path), and passes on the tree as built. Observed by the
hermetic probe the unit 1 acceptance ledger records, since the unattended suites are held.
Item 2: unit 2's spec states the shim mechanism, and `grep` over it finds no claim that the modes override `GIT`.

### Gates
`lexicon naming predicates` · `lexicon wiring` · `memory hygiene` · `spec tokens (a spec's own names resolve)` ·
`writing practice (records and units)` · `positional (the citation check alone)` · `codebase-map coverage + freshness` ·
the full bar at landing.

### Non-goals
No change to `tools/unattended/unattended.sh`. No edit to unit 1's CLOSED spec. No new shell function in the
suite: the lexicon pins the count of non-snake function names and of unruled verbs, and red fix 26f99cdb0
exists because two overrides broke both.

### Limitations
Units run no gates. No unattended `--selftests` without the owner's ask. Refusals earlier passes of this build
hit, to avoid: a new shell function definition in the suite (the lexicon pins); a PATH entry spelled from
`git rev-parse` (its `C:/...` splits PATH at its colon); a count in prose with no pin on its line; a bare
`path:line` citation outside a code span; a `Pass: none` trailer anywhere but the final trailer block. Run
`python tools/check-spec-tokens.py --spec <path>` before returning.

### Reuse
Item 1 extends the `same` call and the `run_render_helper` fixture in region 8 of
`tools/unattended/unattended.test.sh`. Item 2 follows the precedent of `TOOL-dSettledStage-4`, whose own spec
recorded a correction to a frozen sibling.

## Drawn from the session

> Fix every blocker, and ONLY blockers: highs, mediums and lows carry to the exit, where M4 promotes them.
— agent, the build method's close section

## Owner confirmation

Asked: Say go and I'll start, or adjust any field.
Answer: land it
