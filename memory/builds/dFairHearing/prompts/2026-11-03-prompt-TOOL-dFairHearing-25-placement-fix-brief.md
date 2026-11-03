# Fix brief — TOOL-dFairHearing-25: replay 1's call refused by the opt-in pack's subject rule

**Serves:** research TOOL-dFairHearing-25

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md` so replay 1's two runs can be admitted. Pass (a) is `d3c98d523` (its return is `memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-25-1-builder-return.md`): it built S8 and S9 and made clones `fhr1a` and `fhr2a` by S2's placement. The main loop then made the S1 call, `tier2-review.js` with `repo` the clone, `reviewDir` `memory/builds/dFairHearing/reviews` and the one subject `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`. The live agent-cap hook denied both calls before any agent ran, through `tools/workflows/spec-audit-optin.js:158-164`: a spec-audit call whose `subjects` name a path outside `builds/<reviewDir's build>/` is refused. So S2 and AC2 cannot pass as written: AC2's own red case is the state the tree is in. Commit nothing; the main loop commits.

### Items
1. Read `tools/workflows/spec-audit-optin.js` from its argument read through the README and `RUN.md` reads (about `:118-215`), and state in §4 what the pack needs from a replay call: the subject's build folder, the README it reads in the clone, the `RUN.md` branch, and the front-matter key. Cite the lines.
2. Settle the placement as a §8 fork marked by M3 and resolved `RESOLVED (agent, 2026-11-03, delegated)` with M3's reason. The owner's opt-in is the `spec-audit:` key in this build's README at base `3708a705`; a key the run writes into another build's README is the self-opt-in the pack's own comments refuse (TOOL-aWardedAudit-4), so name that veto if you discard such an option. The candidate the main loop sees is: the placement commit also adds the subject's blob `767187aa` at a path under `memory/builds/dFairHearing/`, the call names that path as its subject, and the sibling `specs` stay at their dClosedLoop paths. Check the known-set scoring (spec 1 S3, the `[tag]` address) and spec 1 AC4's blindness against it, and reject it if either breaks.
3. Carry the choice through S1, S2, S8 (the placement step in `tools/workflows/README.md`, which pass (b) may now edit), AC1 (the clone's `diff --name-only` line), AC2 and AC8, so every criterion agrees with the chosen placement.
4. S10's attempts: say whether `fhr1a` and `fhr2a`, made but never run because the call was refused, count as attempts. A clone that no agent read is not a void run; if the new placement needs new clones, name them so no clone serves two attempts.
5. Pass (b) builds the rest. Say in §4 that the main loop runs the two calls between pass (b)'s placement change and its verdict commit, or split the remaining work so the S7 rule still holds: the commit that adds the verdict record has the orchestrating commit as its first parent.
6. Rev bump and one §9 line per change, each naming a section, scope or acceptance id, and this brief. Leave the status header's state as it is.

### Acceptance
Every criterion a correct build can pass on today's tree and hook; the §8 fork in the shape README rule 5 states; the return names the lines item 1 read.

### Gates
None you run.

### Non-goals
No change to the known set, the bars, the scorer, the pack, or any spec but this one. No code.
