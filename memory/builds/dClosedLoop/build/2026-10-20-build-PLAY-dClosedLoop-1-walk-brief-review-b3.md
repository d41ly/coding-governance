# Walk return: run B, walker 3, a review of its brief

**Serves:** research PLAY-dClosedLoop-1

Dispatch 167's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-8-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

I found three defects and one weakness in brief b3 that would let a walker break the return check or read past the seal. Two of them make run B's recall score unreliable before any walker starts.

### B3-R1: the walker's scratch folder sits next to the mechanical plants and older copies of the design
- **Address:** walk-brief-b3, "What you return" (line 77) and "Where you read" (lines 10–20).
- **Class:** K10 (trust boundary), c3. **Severity:** high.
- **Evidence:**
  - Line 77 tells the walker to write under `.../1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/walk-b3/`. The harness also hands each subagent that same scratchpad as its temp directory.
  - `ls` of that scratchpad shows 892 entries, including:
    - `audit-run/stage0-copy.out`, Stage 0's run on the sealed copy. Grepping K3/K5 lines in it against `stage0-tree-k3k5.out` printed `3`: three reds appear only in the copy run. Those are the two mechanical plants, which the copy record and `[recall]` keep from walkers.
    - `audit-run/seal_run_b.py` (it mentions "plant" 3 times) and `stage0/run_plants.py`.
    - Full older trees of the design (`tree/`, `plant/`), `flow-steps.md`, `architecture-v2.md`, `v2.diff`, `fs.diff` and `v2-planted*.md`. `diff scratchpad/flow-steps.md` against the copy's flow-steps gives 374 changed lines.
    - Run A's scratch folders `walk-a2` to `walk-a5`, and `walk-b2`, which a concurrent walker is writing now.
  - "Where you read" forbids only `memory/` in the working tree and git history. It never says "read nothing else".
  - The working tree's `whole-audit [walk]` assumes the scratchpad is safe: "outside the repository and its scratchpad".
- **Consequence:** A walker that lists or greps the folder it was told to write in can see the two mechanical plants, or diff the copy against older text. Its hits would then be counted as recall the walk never earned. This is the same kind of breach as run A's walker 5, through a path the "sealed tighter" fix left open.
- **Fix:**
  - Give each walker a fresh empty scratch root outside the session scratchpad (for example `seed-dcl/scratch/walk-b3/`).
  - Move `audit-run/stage0-copy.out` and the sealing scripts out of anything a walker can reach.
  - Add to "Where you read": "read nothing outside the sealed copy's `build/`, its `design-map.txt` and `stage0-leads.md`, and the working tree's `tools/`, `skills/` and `.githooks/`".

### B3-R2: the copy's `reviews/` folder was not cut, and the brief does not forbid it
- **Address:** walk-brief-b3, "Where you read"; whole-audit `[recall]` ("Every sentence of the copy's records that names a candidate plant is cut").
- **Class:** K10, c3. **Severity:** high.
- **Evidence:**
  - `diff -rq <copy>/memory/builds/dClosedLoop/reviews <tree>/.../reviews` printed nothing: the 50 review reports are byte-identical.
  - In `build/`, by contrast, 15 files differ, including `research-final-audit`, `final-questions` and `session-log`, so cuts were made there and nowhere in `reviews/`.
  - `[recall]` defines the plants as "defects a later review found ... each fixed by a fold since". The review that found each plant therefore sits in `reviews/`.
  - The brief bans only the working tree's reviews. The copy's reviews are not mentioned.
- **Consequence:** A walker checking earlier reviews for leads can read the finding, address and fix of a plant from the copy's own reviews.
- **Fix:**
  - Cut or remove the copy's `reviews/` (and `prompts/`) before run B, or name them as forbidden in the brief.
  - Probe the build must run: grep each key plant's `anchors` and `words` across `<copy>/memory/builds/dClosedLoop/reviews/`. Any hit means that plant was exposed.

### B3-R3: `test.seed` looks like part of the slice but is outside it, and S4 names it
- **Address:** walk-brief-b3, "Your slice" ("test (10 items)") and the S4 text.
- **Class:** K1. **Severity:** medium.
- **Evidence:**
  - Grepping `| \`test.` in the copy's flow-steps finds 11 tags. Ten are in `[test]` (lines 293–302). `test.seed` is in `[adopt]` at line 612.
  - Running `map.derive()` (from the working tree) prints `adopt 5 [... 'test.seed' ...]`. So `walk.py` gives `test.seed` to walker B5, not B3.
  - The brief lists no item tags. Its S4 text says "a new check seeded by `test.seed`", and `design-map.txt:95` lists `dWitnessedBar`, a B3 build, as an owner of `step.adopt`.
  - `walk.py check` (line 153) flags any row outside the slice as "a cell outside the slice".
- **Consequence:** A careful walker adds `test.seed` rows for S1–S7, and its return fails the check, which the brief says fails the return.
- **Fix:** Have the template list each step's item tags. At minimum add: "`test.seed` is the adopt step's item: give a finding if one is warranted, but no row."

### B3-R4: the leads file is not limited to the slice, and the reading rules conflict with the walker's role
- **Address:** walk-brief-b3, "Where you read" (lines 12 and 20).
- **Class:** K10. **Severity:** low.
- **Evidence:**
  - "Stage 0's leads for your slice" points at one file that every brief shares, 326 lines covering all steps.
  - The walker's role tells it to read `memory/guides/REVIEW-PROTOCOL.md` for any review. That file is under the working tree's `memory/`, which line 12 forbids except for the brief itself.
- **Consequence:** The walker either breaks the seal rule, which would be logged like run A's breach, or skips its protocol. Separately, "for your slice" misdescribes what the file holds.
- **Fix:** Change the wording to "Stage 0's leads (whole; take the ones your slice reaches)". Either allow `memory/guides/` explicitly or point the walker at the copy's identical guides.

### Checked and held
- **Paths:** every record and path the brief names exists in the copy.
- **Item counts:** test 10 and deploy 13 match `derive()`.
- **Builds and principles:** the build and principle lists match `[slicing]` B3. The five run-B briefs together cover all 42 principles once, and all 22 builds against `derive()`'s chain.
- **Copy against the tree:** `[scenarios]` and `[rubric]` are identical. `diff -rq` of `tools/` against the copy shows only `__pycache__`, and `git diff --stat 747a2af22 HEAD` is empty for `tools`, `skills` and `.githooks`, so "today's code" is the same code the copy was cut from.
- **Grammar:** the brief's address and ID formats match the patterns in `score.py` and `walk.py`.

I ran no gate, no `walk.py check` and no scorer. I read the key-adjacent files only to count and fingerprint them, not to recover plant content.

Files involved:
- Brief: `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-walk-brief-b3.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-19-build-PLAY-dClosedLoop-1-walk.py`
- `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\audit-run\stage0-copy.out`
- `C:\Users\d41ly\AppData\Local\Temp\claude\seed-dcl\tree\memory\builds\dClosedLoop\reviews\`
