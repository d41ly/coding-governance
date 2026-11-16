# TOOL-aClearedLedger-4 — the scratch guard suite's context arms start from a session tree with no card file

**Status:** CLOSED · rev-1 · 2026-11-13 · node a · Tier-1 · base 8db6f4be · streams tooling · order 4 · closes TOOL-aNimbleMend-17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aClearedLedger-1-2-observations.md](../build/2026-11-14-build-TOOL-aClearedLedger-1-2-observations.md) | journal | TOOL-aClearedLedger-1 TOOL-aClearedLedger-3 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 TOOL-aClearedLedger-11 TOOL-aClearedLedger-12 TOOL-aClearedLedger-13 TOOL-aClearedLedger-14 TOOL-aClearedLedger-15 TOOL-aClearedLedger-16 |
| [2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md) | research | TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 |
| [2026-11-13-review-TOOL-aClearedLedger-1-2-3-4-5-6-7-9-10-diff-review-round1.md](../reviews/2026-11-13-review-TOOL-aClearedLedger-1-2-3-4-5-6-7-9-10-diff-review-round1.md) | diff-review | TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 |

<!-- /gen:spec-records -->

## 1. Goal

Seven context arms of the scratch guard's suite red because an earlier arm of the same suite
leaves a rendered card file in the fixture worktree, and the hook then wraps every context in
that file's envelope, as designed. The refusal is right and the arms' expectations are right; the
fixture is wrong. This unit makes the context block remove the card file before its first arm.

## 2. Scope (IN)

- **S1** — In `tools/hooks/scratch-guard.test.sh`, the SUBAGENT CONTEXT block sets `SG_CF` ahead
  of its first `run_sub` call and empties the session tree of the card file at that path there,
  with a comment naming the arm that leaves it. The S-AC8 block reads that one assignment, so the
  path is spelled once in the suite. Observed by AC1 and AC2.
- **S2** — The seven arms hold with no edit to their expectations: `S-AC2` twice, `S-AC3` twice,
  `S-AC5` once and `S-AC8` twice. Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- Any edit to `tools/hooks/scratch-guard.js`. The envelope is intended where the session tree
  holds the card file, by PLAY-dOrderedCharter-8 S6, and `renderRouteContext` does what its
  comment says.
- Any edit to an arm's expectation, to `check_ctx`, or to `FLOOR_ASSERTIONS`. No assertion is
  added or taken away, so the executed count does not move.
- Any edit to the AC10 cross-kit arm or to `skills/session-kickoff/manifest-check.sh`. The writer
  renders the card file by design, and AC10 is right to run the live writer.
- A new arm that feeds the live writer's card file to the context. The S-AC8 arms plant their own
  envelope lines so that a hook typing its own reds; a cross-kit envelope arm is a separate ask.
- Any kit version, which the lander's `mint` moves.

## 4. Design

### The cause

Read at `82ceaab5`, and reproduced on 2026-11-13 in a scratch repository.

- The AC10 arm runs the live writer in the linked fixture worktree:
  `tools/hooks/scratch-guard.test.sh@eccc92bcc809:812` and line 839 of that blob call
  `manifest-check.sh --card --write --session sgtest-w1` from `$SGWT`.
- Since commit `06d9f5678` (PLAY-dOrderedCharter-8) the writer also renders the stored card into
  `<tree>/.claude/orientation-card.md`, through `write_card_file` at
  `skills/session-kickoff/manifest-check.sh@4d3d63c0fad1:876`. AC10 removes the stored card,
  `$SG_CARDS/sgtest-w1.md`, and leaves the rendered file.
- `tools/hooks/scratch-guard.js#readCardEnvelope` reads that file's first and last lines, and
  `renderRouteContext` wraps every non-empty context in them.
- The suite's output at `8db6f4be`, the file `a17.out` the brief names, shows the wrap: each
  failing context opens with the line carrying the writer's own direction text, "the build's
  card: where this session stands; level 0 outranks it", which is `CARD_FILE_DIRECTION` at line
  874 of the writer's blob above. The fixture's own envelope line, `SG_CF_OPEN`, reads "a fixture
  direction".
- The reproduction: in a fresh repository the writer's `--card --write` left the card file, the
  hook's `SubagentStart` context was three lines, and with the file removed it was one line.

The S-AC1, D-AC5 and SD8 arms run with the same file present and pass, because they test for
lines the context carries and not for its line count. The seven failing arms test a line count,
a last line, or byte equality with a bare context.

### The fix

The context block states its own precondition instead of relying on what earlier arms left. After
the line that empties `$TMP/ctx-all` and before the first `run_sub`, the block gains:

```bash
# The session tree holds NO card file from here to the S-AC8 block: the AC10 arm runs the live
# writer in this worktree, and since PLAY-dOrderedCharter-8 the writer renders one, which
# renderRouteContext would wrap around every context below.
SG_CF="$SG_TOP_WT/.claude/orientation-card.md"
rm -f "$SG_CF"
```

The S-AC8 block keeps its `SG_CF_OPEN`, its `mkdir -p`, its planted file and its own `rm -f`, and
loses its `SG_CF=` line.

The removal sits at the head of the block that needs the precondition, not at the tail of AC10.
An arm added later that runs the writer in `$SGWT` would leak the same file past a cleanup tied
to AC10; a block that clears its own precondition does not care which arm leaked.

### Files touched (estimate)

`tools/hooks/scratch-guard.test.sh`

## 5. Acceptance criteria

- **AC1** — When
  `grep -n -m1 -e 'rm -f "$SG_CF"' -e '^run_sub "S-AC1' tools/hooks/scratch-guard.test.sh` runs,
  the one line it prints is the `rm -f` line.
  Red when: the removal sits after the first context arm, which prints the `run_sub` line. At
  `82ceaab5` the command prints the `run_sub` line.
- **AC2** — When `grep -c '^SG_CF=' tools/hooks/scratch-guard.test.sh` runs, it prints `1`, and
  `bash -n tools/hooks/scratch-guard.test.sh` exits 0.
  Red when: the S-AC8 block keeps a second definition, or the edit broke the script's syntax.
- **AC3** — When a pass repeats the reproduction of §4 in a scratch repository under `%TEMP%`,
  the hook's context for a session with no stored card is one line once the rendered card file
  is removed from the tree, read through `node tools/hooks/scratch-guard.js` on a `SubagentStart`
  payload.
  Red when: the hook wraps a context with no card file in the tree, which would make the hook
  the wrong side and this unit's fix the wrong one.
  fixture: a fresh `git init` repository with one empty commit and a `.memory-tree.conf` setting
  `MEMORY_ROOT` and `ROUTED_PATHS`; the tree holds none today, and the pass removes it after.
- **AC4** — When the main loop runs the scratch guard's suite, the one the `scratch-guard
  self-test` leg of `tools/gate-legs.json` runs, no line of its output opens `FAIL S-AC2`,
  `FAIL S-AC3`, `FAIL S-AC5` or `FAIL S-AC8`.
  Red when: the card file is still in the fixture worktree at the first context arm. At
  `8db6f4be` the suite prints seven such lines.
  permission: a role agent's pass runs no suite. The main loop runs it on a frozen clone.

## 6. Gates

The main loop runs the suite at the close. No arm is added or moved: the seven arms were seen RED
at `8db6f4be`, recorded in `a17.out`, and AC4 is their GREEN.

`scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 9. Reuse audit

No existing seam fits beyond the suite's own: `SG_CF` and the `rm -f "$SG_CF"` the S-AC8 block
already carries are moved up, and nothing is built. The recall probe refused with a
`PermissionError` on the shared cache's `chunks.db`, held by a sibling writer's rebuild, so the
cause was found by reading the suite, the writer and `a17.out`, and by the reproduction of §4.

Recall terms used: scratch-guard SubagentStart additionalContext orientation-card envelope
readCardEnvelope S-AC8 AC10 writer fixture worktree manifest-check card-file
