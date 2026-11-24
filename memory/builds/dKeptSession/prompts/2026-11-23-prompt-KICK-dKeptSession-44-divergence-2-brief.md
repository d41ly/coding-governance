**Serves:** research KICK-dKeptSession-44

# Brief — dKeptSession: KICK-dKeptSession-44's second divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-44's second builder (run `wf_6e2e17aa-70c`) stopped before its first edit at base `4423f5ffe`, on
two divergences in rev-7. Every other code claim held there, including rev-7's S20 re-point.

- S13: `adopt-policy.sh --scaffold --preset lax` is to pass the scaffold's exit 2 and stderr through. The adopter
  suite's existing arm in `tools/policy/adopt-policy.test.sh` (block "4b", the `--preset lax writes nothing` line)
  asserts the opposite, exit 1 with the generic "could not be written" line. That suite runs under the policy kit's
  `adopter-suite` fixture (`tools/policy/check_policy.py#run_adopter_suite`), and the file is outside Files touched.
- AC37: the probe reads red at the base. Commit `8a76ad2f4` (PLAY-dOrderedCharter-50) changes
  `tools/govkit/subject-pins.tsv` and adds a real pin row with a `[[gate_leg]]` in `tools/playbook/kit.toml` and
  `tools/run-gates/kit.toml`, without touching `tools/gate-legs.json`.

Revise the spec to the main loop's rulings below.

### Items

1. F-adopter-arm: resolved by the main loop.
   - Add `tools/policy/adopt-policy.test.sh` to Files touched, tied to S13.
   - S13 re-arms block 4b's lax line in place, in the same commit: exit 2, with the scaffold's
     `policy: scaffold refused · preset · ` stderr naming `lax` and the four shipped presets.
   - The block's second check (no policy file after a refused scaffold) stays. The no-mv arm keeps the adopter's
     `exit 1` site armed.
   - Declare the re-armed arm on a §7 `New arm:` line covering AC11, staged against the base adopter, which prints
     the generic line.
   - Add the policy kit's `adopter-suite` fixture to §7's legs if it is not there.
2. F-ac37: resolved by the main loop. Restate AC37 so it holds at the base and still catches the class it was
   written for, a no-op regen: each commit the range prints also touches `tools/gate-legs.json` or a kit's
   `kit.toml` (the `[[gate_leg]]` descriptors). Re-read the paragraph it observes, so the clause and the criterion
   say one thing.
3. F-map: S25's regen runs `python tools/codebase-map/gen_map.py --write` after an edit to
   `memory/map/features/unattended.md`. When KICK-dKeptSession-21 made that same edit, the regen also rewrote
   `memory/map/generated/MAP.md`, `CARDS.md` and `inventories.json` (its re-dispatch `e356c0e35` widened the write
   set by exactly those three). Add the three to Files touched beside `symbols.json`, tied to S25.
4. F-records: S22's "today it prints `red-fix` and `widen` rows" also misses `deviation` rows over dKeptSession.
   Correct the text. The design is unchanged.
5. Size: the spec is over the live-spec cap, which only warns. Make this revision without growing the spec. Condense
   where the text repeats what a cited symbol or an earlier clause already says, and never cut a clause's token, a
   criterion or a revision-log line.
6. Bump the spec one rev, with one revision-log line naming this brief by its file stem.
   - Cite code by `path#symbol`, and pin every figure with DERIVED or PINNED on its own line.
   - Write no `[..](..)` link shape outside the generated records table.
   - Leave no fork open.

### Acceptance

These all report nothing for the spec:
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`
- a plain `bash tools/memory-tree/check-memory-hygiene.sh --only 2`
- `python tools/check-spec-tokens.py --spec <path>`
- a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
- `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-44`

### Gates

Only these: the memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts
check and the driver's `--check-specs`.

### Non-goals

- No product code, no commit and no index render.
- No spec other than KICK-dKeptSession-44's. Read files freely; edit only the spec, in the run worktree.
