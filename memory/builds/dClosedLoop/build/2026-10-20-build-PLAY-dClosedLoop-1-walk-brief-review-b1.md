# Walk return: run B, walker 1, a review of its brief

**Serves:** research PLAY-dClosedLoop-1

Dispatch 165's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-6-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

I found two high-severity defects and one medium in `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-walk-brief-b1.md`. All three are leaks in what the walk keeps hidden, under the brief's "Where you read" section. Each gives walker B1 another way to find the answers to the planted defects. The brief only lists what is forbidden, and the readable material around the copy includes the answers. So each run's recall score (how many of the planted defects its walkers find) partly measures whether the walker happened to read the answers. That is the rubric's c3 class: a check that certifies what it does not check.

The rest of the brief checks out against the round record and the code. I rendered run B's briefs from the working tree's `walk.py` into my scratch folder, and the result is byte-identical to the committed b1. Its slice matches the round record's row for run B walker 1. The copy's flow-steps has exactly 6 entry items and 11 plan items, so the walk table is 119 cells. All four builds have a row in v2's `[chain]`, and all eight principles appear in v2's `[enforcement]` section. Every record the brief names exists in the copy, and the copy's tools/ and skills/ match the working tree's. The scorer's address pattern accepts the address form the brief asks for.

### R6-1 — The sealed copy's past reviews hold the fixes the plants undo, and the brief doesn't put them off-limits
- **Spec and section:** walk-brief-b1, "Where you read".
- **Severity:** high (c3).
- **Evidence:**
  - `diff -rq <copy>/memory/builds/dClosedLoop/reviews <worktree>/memory/builds/dClosedLoop/reviews` printed nothing. The copy's 50 reviews are byte-identical to the working tree's, so no sentence was cut from them. The copy's `prompts/` folder (91 files) is not cut either.
  - A diff of the copy's flow-steps line 81 against the working tree shows a plant in B1's own slice: the copy's `entry.intake` actor reads "orientation scout", where the fixed text reads "hook: prompt-submit".
  - The copy's `reviews/2026-10-15-review-PLAY-dClosedLoop-1-flow-a.md:105` gives the fix in plain words: "`entry.intake` becomes a hook item, awaited on the prompt-subm…".
  - `reviews/…-chain-order.md:45,49` and `…-design-audit.md:44` discuss the `plan.exit` ratification, where the copy's flow-steps line 140 also differs from the tree.
  - The copy's v2 cites `reviews/2026-10-18-review-PLAY-dClosedLoop-1-chain-order.md` by path, which invites the walker to follow it. The reviewer role also says to read "the siblings it names".
  - The brief forbids only the working tree's `memory/`, design records outside the copy's `build/`, a diff against the tree, and git history. The copy's `reviews/` and `prompts/` are none of these, and the line "a finding cited from anywhere else is not scored" doesn't stop a walker from reading them.
- **Consequence:** A walker following v2's citations reads the earlier finding and fix for a plant in its slice. It then "finds" the plant without walking anything. The recall bar (at least 8 of 12 per run, 10 together) is then met by reading old reviews, and Mills's estimate of the defects left in the design comes out too low.
- **Fix:**
  - Remove `reviews/` and `prompts/` from the copy, or cut every sentence in them that names a plant, as `[recall]` already does for the build records.
  - Change `walk.py`'s template from a list of bans to a list of the only places a walker may read: the copy's `build/`, `design-map.txt`, `stage0-leads.md`, and code from the working tree. Everything else is forbidden.
  - Re-render run B's briefs before they are dispatched.
  - Probe the build must run: grep the stripped copy for each plant's words from the key, outside the planted lines, and expect zero hits.

### R6-2 — The walker's scratch folder sits beside unplanted copies of the records and run A's working folders
- **Spec and section:** walk-brief-b1, "What you return" (the line naming the scratch path under `scratchpad/walk-b1/`), together with "Where you read".
- **Severity:** high (c3).
- **Evidence:**
  - `ls <scratchpad>` lists `night2/dry/…`, `night2/pairs/dry*/…` and `night2/tag/dry*/…`. Each is a full `memory/builds/dClosedLoop/build/` tree. It also lists `v2*.md`, `fs*.md` and `*-planted*.md` snapshots, and run A's folders `walk-a2` to `walk-a5`.
  - `grep -rl "hook: prompt-submit, in an owner-bound session only" <scratchpad>` matched `night2/dry/…/flow-steps.md` and 9 more files. That is the unplanted text of the `entry.intake` plant.
  - `walk-a2/` holds row extracts for `dPlacedRequest` and `dKeptSession`, two of B1's own builds.
  - The brief bans diffing the copy against "it" (the working tree) and against git history, but says nothing about these snapshots. A subagent's environment block also names the same scratchpad, so the walker finds it even without the brief's path.
- **Consequence:** A diff of the copy against `night2/dry` points straight at the plants. The record's `[walk]` section also promises that run A's returns are kept away from run B's scratch folders, but run A's working folders sit in the same place.
- **Fix:**
  - Give each walker a fresh scratch folder outside the session scratchpad, for example under the temp root next to `seed-dcl`, and pass it as `--scratch`.
  - Add one line to the template: "Read nothing in the scratchpad or the temp root outside your own scratch folder and the paths above."
  - Or move the old snapshots out before dispatch.

### R6-3 — Running Stage 0 on the copy and comparing it with the leads points at a plant
- **Spec and section:** walk-brief-b1, "Where you read", the bullet on Stage 0's leads.
- **Severity:** medium.
- **Evidence:**
  - The round record's `[briefs]` section says the leads come from "the run on the working tree, never on the copy". The brief gives walkers the leads but doesn't forbid them from running the copy's own `build/…-stage0.py` against the copy.
  - I ran `python -I …-stage0.py --root <copy>` and `--root <worktree>` and diffed the two outputs. The only difference: `K2: … terminal 33 …` became `terminal 32`.
- **Consequence:** That one count tells the walker that a route's end state was changed somewhere. That is a pointer to a planted, non-mechanical defect obtained without reading the design. It is weaker than R6-1 and R6-2, but it is the same kind of leak.
- **Fix:** Add "Run no instrument from the copy's `build/` against the copy; Stage 0's leads are the only output of the mechanical checks you read" to `walk.py`'s template, and re-render.

Any probe output I kept is under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/rev6/`. I wrote nothing to the repository.
