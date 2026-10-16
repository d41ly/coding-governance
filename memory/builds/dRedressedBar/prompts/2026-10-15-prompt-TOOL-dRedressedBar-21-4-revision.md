# Revision — dRedressedBar: TOOL-dRedressedBar-21 takes the capture links and the held stamp's temp, and spec 23's title under the index cap

**Serves:** research TOOL-dRedressedBar-21 TOOL-dRedressedBar-23

## The brief

### Goal
Two writers found the same defect class beyond H1's record. Unit 21's writer: `run_leg` opens each leg's capture with a plain `open(capture, "wb")` (`tools/run-gates/measure_legs.py:777`) and `write_leg_capture` reads and deletes it (`:1431`, `:1441`), all following a link planted in the run's own scratch dir. The owner ruled on 2026-10-15 to fold that into unit 21. The Readers writer: `write_held_stamp` in `tools/run-gates/held_halves.py:322` uses the same fixed `.tmp`-then-`os.replace` pattern S4 removes from `write_atomic`, and S5's static check parses `measure_legs.py` alone. Separately, check 7 caps the build README's generated unit rows at 350 bytes, and spec 23's row is 459 because of its H1.

### Items
1. **TOOL-dRedressedBar-21** (uncommitted rev-1, so no rev bump): move the capture-path hand-off from §3 into scope. The capture's open, read and delete go through S2's checked reader and S3's same-file delete rule (or the create-side equivalent for the open: a new file only, never through an existing entry), each with a `**Readers:**` clause, an AC and a red half planting a link at the capture's path. Widen S4 and S5 to the class: every fixed-name temp-then-replace writer under `tools/run-gates/` (find them with grep, `held_halves.py:322` included) takes the unpredictable temp, and S5's static arm parses every such file, with its red half observed on the current tree. Record the owner's ruling and this record in §9 as the rev-1 drafting note it is.
2. **TOOL-dRedressedBar-23** (uncommitted rev-1, so no rev bump): shorten its H1 so the generated row is at most 350 bytes (the row adds 93 bytes around the H1, so the H1 is at most 257 bytes), keeping the id and naming what the unit does. A candidate measured at 250 bytes: `TOOL-dRedressedBar-23 — the closing review's govkit findings M3, M4, M6 and L4, batched: a narrower apply keeps a carried kit's orders and order-file legs, quoted spawn stderr decodes through one helper, and two selftest guards grade what they read`. Confirm its last clause against spec 23's S5 and S6, and fix it if it misstates them.

### Acceptance
`bash tools/memory-tree/check-memory-hygiene.sh --staged` over the staged specs 21 to 23 prints no check 7 or check 25 line after the main loop re-renders the README. Spec 21's §3 no longer hands off the capture path.

### Gates
`memory hygiene` · `lexicon naming predicates`

### Non-goals
- No code. No edit to any spec but 21 and 23. No status change. No index regeneration; the main loop runs it.
