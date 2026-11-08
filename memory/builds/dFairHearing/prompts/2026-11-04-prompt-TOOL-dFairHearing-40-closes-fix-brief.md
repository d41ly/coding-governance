# Fix brief — TOOL-dFairHearing-40: the last unit's header closes the build's ask

**Serves:** research TOOL-dFairHearing-40

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-40.md` so that its CLOSED flip lands in a commit the hooks accept. Its first build pass returned a DIVERGENCE with the work done and the commit refused: read `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-40-1-builder-return.md` first. Unit 40 is the last unit in build order. The build's BACKLOG.md DEFERRED row for `TOOL-dFairHearing-19`, the README's rule 1 and that ask's accept clause all say the last unit's header carries `closes` for the ask. The header still says `advances TOOL-dFairHearing-19`, so a CLOSED flip would drop the ask to OPEN. Commit nothing; the main loop commits.

### Items
1. Change the status header's `advances TOOL-dFairHearing-19` to `closes TOOL-dFairHearing-19`. Leave its state as INPROGRESS.
2. Check that no criterion, risk or change-log line still says this unit only advances the ask. Restate any that does.
3. Bump the rev and add one change-log line naming this brief.

### Acceptance
The header reads `closes TOOL-dFairHearing-19`, and nothing else in the spec contradicts it.

### Gates
None you run.

### Non-goals
No other spec, no code, and not the build's BACKLOG.md: the main loop writes the status row for `TOOL-dFairHearing-42`.
