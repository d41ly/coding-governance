# Fix brief — TOOL-dFairHearing-16: the edges its move breaks outside this build, and two commit-time obligations

**Serves:** research TOOL-dFairHearing-16

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-16.md` so the build already drafted against it can commit. The builder's second return is `memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-16-2-builder-return.md`, and its whole build is a patch at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f/scratchpad/u16probe/TOOL-dFairHearing-16-build.patch`; read the return first. Commit nothing; the main loop commits.

### Items
1. The move takes `tools/hooks/agent-cap.js` to about 947 lines, so `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md`, a live spec of another build, cites lines that no longer exist (`:1972-1994` at its line 138, `:2220` at its line 91), and the spec-token checker refuses every dispatch on it. This build may not edit that spec. Settle it as a §8 fork by M3, the way `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-18.md` §8 F2 and TOOL-dGroundRules-10 §8 F7 settled the same cite: under the standing ruling ER:388, with its mark citing the ruling and carrying `widens:` and `relaxes:` as this build's README rule 5 requires. The option that worked there is a waiver row per broken cite in `memory/project/spec-token-waivers.txt`, in that file's row grammar and count convention, plus an ask in `memory/builds/aOrientedCast/BACKLOG.md` asking that build to re-cite by symbol. Name both files in §4 Files touched, and the deviation record README rule 5's `relaxes:` value needs.
2. The same move leaves stale hook cites in DEFERRED specs, which each go red when their unit goes live: this build's units 22, 23, 32 and 37, and others in dBoundRoles, dFurnishedOrders, dWellOiledMachine, dIndexedDesign, dMindYourWords, dOrderedCharter, dKeptSession and dTotalRecall. For this build's four, state in §3 Edges that each re-grounds its own cites before its build, as unit 13's and 16's did. For the others, state that the cure is the same ask-and-waiver route when each goes live, and that this unit files nothing for them now.
3. §4 Files touched adds `memory/guides/SESSION-KICKOFF.md`: pre-commit check 5 refuses a commit staging the watched `tools/gate-legs.json` unless the kickoff manifest's `last-audit` is re-stamped in the same commit. Move that re-stamp here from TOOL-dFairHearing-23 S28, and edit unit 23's spec so its S28 no longer schedules it (rev bump and §9 line on both).
4. S5's new `spec-audit opt-in pack self-test` leg: say what it guards. A guard on `{prefix}/hooks/`, `{prefix}/lib/` or `{prefix}/workflows/` reds the guards join on aOrientedCast-28. Prefer the unguarded form `review-replay selftest` already takes (see the TOOL-aSightedSkeptic-9 note in `tools/workflows/kit.toml`), unless M3 picks the waiver route of item 1; record the choice in §8.
5. Rev bump and one §9 line per change, naming this brief. Leave each status header's state as it is.

### Acceptance
Unit 16's spec at its next rev names every write its build makes, including the waiver rows, the ask and the manifest re-stamp, with each §8 mark in the shape README rule 5 states. Unit 23's S28 and unit 16's §4 agree. The main loop runs `python tools/check-spec-tokens.py` before committing.

### Gates
None you run: the spec-token checker is the main loop's, as the last pass found.

### Non-goals
No edit to another build's spec. No code, and no write outside units 16's and 23's specs.
