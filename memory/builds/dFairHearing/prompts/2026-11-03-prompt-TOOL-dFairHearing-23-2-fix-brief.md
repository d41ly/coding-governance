# Fix brief — TOOL-dFairHearing-23: AC41's suite token

**Serves:** research TOOL-dFairHearing-23

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Make `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md` pass `tools/check-spec-tokens.py`. Its one hit, from the main loop's run over the rev-5 spec: `[bar] unattended-build.test.sh — a bar or suite is not an acceptance observation`. The token is AC41's backticked bare filename `unattended-build.test.sh`, which the checker's BAR pattern (`tools/check-spec-tokens.py`, the `BAR` regex and its comment above it) reads as a suite run, though AC41 only slices one function out of that file with `sed`. Commit nothing; the main loop commits.

### Items
1. Re-spell AC41's file reference so the BAR pattern does not read it as an invocation while it still names the same file, for example the `path:line` citation `tools/workflows/unattended-build.test.sh:968-987` the pattern's comment says it leaves to the cites join. Change nothing else in AC41's meaning.
2. Check no other criterion in §6 spells a suite or the bar at command position; fix any the same way.
3. Rev bump and one §9 line per change, naming this brief. Leave the status header's state as it is.

### Acceptance
The BAR pattern finds no hit in §6 of the spec at its next rev.

### Gates
None you run.

### Non-goals
No other change to the spec, no other spec, no code.
