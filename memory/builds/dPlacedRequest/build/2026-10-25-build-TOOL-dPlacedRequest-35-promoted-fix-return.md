**Serves:** research TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43

# The promoted-fix pass — dPlacedRequest round 2, its return

The return of the gov-spec-writer dispatched from `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-7-spec-writer.md`, run direct/a7174936dfa88f616, extracted from its transcript by script.

All five hits are fixed. `check-memory-hygiene.sh --only 2,12,25` exits 0 with both specs staged, and spec 34 ends at **47699 bytes**, 1453 under the 49152 ceiling.

**Spec 43, the four [guards] hits: fixed.** `tools/hooks/scratch-guard.js` is in its files-touched list, and each of the four legs guards the whole `{prefix}/hooks/` directory in `tools/gate-legs.json`, so all four hits were real. I added `agent-cap self-test`, `verifier fan-out self-test`, `review-join self-test` and `hook destinations self-test` to its §7 leg line, bumped it to rev-2 and added the §9 line.

**Spec 34, the [size] hit: fixed, 50807 down to 47699 bytes.** All 59 scope items, all 59 criteria, all 30 edges, the 4 forks and the 5 Readers clauses are still there, and each item still ends with its `Observed by ACn`. The two round-2 hands-off edges (to 35 and 43) and the consumes-from edge to 40 are word for word as before. The records block is unchanged. What I cut:
- **Fetch diagram:** removed from §4, because S5, S6, S7 and S12 already state it. Its one extra fact, `--no-write-fetch-head`, moved into S5.
- **Census sub-section:** removed from §4. Its rules (the column-0 `}` scope and the three calls a writer must make) moved into S16 and S17.
- **One evidence bullet:** removed from §4, because S24 and S25 repeat it. Its `:866` citation moved into S25.
- **Edges:** each edge line no longer repeats the list of items that use that unit, since each item already names its unit. The three folded edges are untouched.
- **Sibling ids:** in §2, §4 and §6, `TOOL-dPlacedRequest-N` is now written "unit N", matching how §1 and §3 already refer to units. AC19 keeps its backticked id because it is that criterion's only witness.
- **Prose:** tightened in §1, §5, §8 and §10, and §2 and §6 reflowed.
- **Rev log:** bumped to rev-4 with its §9 line. I also shortened the rev-3 line's wording without changing what it records.

The first hygiene run after the reflow went red, and I fixed it. The checks read `Red when:`, `by value:` and `READER NOT IN TREE` as single-line markers, and the reflow had split them. AC19 had also lost its witness to the id change.

Three things the main loop should know:
- **The records render will grow spec 34.** The new brief lists spec 34 under Serves, so the next render adds at least one row of about 450 bytes, possibly two. That puts spec 34 at roughly 48150 to 48600 bytes, still under the ceiling.
- **That is above spec 43's own target.** Spec 43's S22 and AC22 require spec 34 to be at most 47104 bytes after the render. That stays a build-time item of spec 43: it moves "Measured sizes" and "The one deletion outside leases" out to a research record, and I left both sections in place so that move still works.
- **I did not run `check-spec-tokens.py`; that's still for the main loop.** The reflow joined some backtick spans in §6 that used to break across lines, so the extractor now sees them. I checked the new words by hand. The only file-like one is `gov-feed.log` in AC33, and it shouldn't be flagged: the bare-name check isn't on here, since AC14's `gov-queue.log` was already visible to the checker and was never flagged.

Files:
- C:\projects\coding-governance\.claude\worktrees\unattended-dplacedrequest-f41432\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-43.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dplacedrequest-f41432\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-34.md
- Pre-edit copy of spec 34: C:\Users\DAILY-~1\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-dplacedrequest-f41432\a4a72c24-4423-4b1e-9176-5acec5cc094f\scratchpad\spec34.orig.md
