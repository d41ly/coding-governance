# Fix brief — TOOL-dFairHearing-36: AC3's suite path read as a bar token

**Serves:** research TOOL-dFairHearing-36

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Make `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-36.md` dispatchable. Its builder's `--dispatch` was refused by check 49: `python tools/check-spec-tokens.py` exits 1 on one hit in this spec, `[bar] tools/hooks/agent-cap.test.sh — a bar or suite is not an acceptance observation`. The bar join (`tools/check-spec-tokens.py:419-424`, its `BAR` pattern) reads every backticked bare `*.test.sh` path in a §6 bullet as a suite run, even one used as a file input. AC3 spells its input as "`tools/hooks/agent-cap.test.sh` as `git show` prints it at `3708a705`". The builder's return is `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-36-1-builder-return.md`; every criterion was observed holding, so this is the one change the unit owes. Commit nothing; the main loop commits.

### Items
1. Re-spell AC3's input so no backticked word of §6 is a bare suite path, the way the other criteria already name their files through the scope item that names them (for example "base's hook suite, the file S1 names, as `git show` prints it at `3708a705`"). The criterion reads the same file as before.
2. Check every other backticked word of §6 against the `BAR` pattern at `tools/check-spec-tokens.py:419-424`, so no second hit is left.
3. Rev bump and one §9 line naming AC3 and this brief. Leave the status header's state as it is.

### Acceptance
No §6 token of the spec matches the bar pattern; AC3 reads the same input as before.

### Gates
None you run.

### Non-goals
No other change to the spec, no other file.
