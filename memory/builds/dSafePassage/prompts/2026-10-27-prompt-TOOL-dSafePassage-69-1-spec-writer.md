**Serves:** research TOOL-dSafePassage-69

# Brief: the floor step's down refuses every rollback to the pin, and says why on a stream nobody reads

## The prompt

No owner prompt. After TOOL-dSafePassage-68, the build run's main loop ran `python -I tools/govkit/upgrade_walk.py --case kill --step lib/python-floor-3.15`. It was red. The run adopts the fix under M10.

## The brief

### Goal

A rollback to the pin passes the floor step's down whenever the code it restores runs under the floor the pin really had. When the down refuses, the refusal is in the step's `tail`, which is what the walk, the leg and the operator read.

**What was measured** at HEAD `dbd1d6b01`:

- The rollback from the killed floor state stops: `the rollback's reverse walk stopped at lib/python-floor-3.15: down exit 1: .`, with an empty tail. Its log is `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/kill68-floor.log`.
- The step's down is `["bash", "{gov}/lib/python-floor.sh", "down", "3.11", "{target}", "{to}"]` (`tools/govkit/steps.toml:34`). TOOL-dSafePassage-26 S10/S11 (dfcef45a7) made it grade the files the rollback restores, read at `<to>`, under the prior floor 3.11.
- A read-only probe, `python_floor.check_down_floor(Path('.'), '3.11', '60d90cb7…')`, returns one finding: `tools/memory-recall/check-recall.py:394: a # in a replacement field`. At the pin that line is `print(f"{'#':>3}  …")`. Python 3.11 rejects `#` inside an f-string replacement field, so the pin's own code needed 3.12 while the step restores 3.11. The pin has no `tools/lib/python-floor.txt`; HEAD's says 3.15.
- `python_floor.py down` prints its mode line, its findings and its count on stdout (`tools/lib/python_floor.py:403-418`). `run_step_isolated` keeps stderr's last 20 lines as `tail` (`tools/govkit/upgrade_steps.py:~1130`). So the refusal reaches nobody.
- Unit 5's sixth pass had this case green at 7c51ef25f, which was before TOOL-dSafePassage-26. A `--case down` run is in flight and will say whether `down` is red the same way.

### Items

1. **Author `memory/builds/dSafePassage/spec/2026-10-27-spec-TOOL-dSafePassage-69.md`** with this header:
   - Tier-2, `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 7`
   - `**Derived:** TOOL-dSafePassage-26`
   - `consumes-from` TOOL-dSafePassage-5, -11 and -26

   Decide from the code and the records (TOOL-dSafePassage-11's and -26's specs, DECISIONS, and `help/` on the floor):
   - (a) **The prior floor.** Is 3.11 the pin's real floor? Measure what the pin's code requires: run the scanner over the pin's whole tree, not only this file. Then the step declares that floor, or the down stops grading findings that already stand at `<to>`, because a rollback cannot make them worse. Pick one and say why. A fork you cannot derive goes in §8, with a recommendation.
   - (b) **The refusal's stream.** The down's findings and count reach `tail`, by printing them on stderr. Check every other step command for the same class: a step whose failure text goes to stdout. Gate that class if a cheap predicate exists.
   - Acceptance criteria must be observable without the whole leg: the `check_down_floor` probe, a `python_floor.py down` run, and the leg's `--case kill --step lib/python-floor-3.15` (about 6 minutes). Each needs a Red-when and a `New arm:` line.
2. **Add its row** to the README's authored `roster:units` table.
3. **Commit nothing.** Return the files you wrote.

### Acceptance

- The spec is conforming: status header, `**Derived:**` line, §6 with a Red-when, §7 with a `New arm:` line, §10 reuse.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, and no edit to a CLOSED spec.
- No commit and no stage into the real index.
