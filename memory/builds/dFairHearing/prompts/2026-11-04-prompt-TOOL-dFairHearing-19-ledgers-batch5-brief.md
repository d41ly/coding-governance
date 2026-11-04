# Research brief — the acceptance ledgers the build's CLOSED units owe

**Serves:** research TOOL-dFairHearing-1

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Draft the acceptance ledger for each CLOSED unit of build dFairHearing in your batch, from the records already on disk, so the main loop can review and commit them at the close. The memory-hygiene gate's ledger-coverage check reds on every criterion of units 1 to 18, 20 to 23 and 25 to 36, because none of those units has a ledger. Your batch: TOOL-dFairHearing-30, TOOL-dFairHearing-31, TOOL-dFairHearing-32, TOOL-dFairHearing-33, TOOL-dFairHearing-34, TOOL-dFairHearing-35, TOOL-dFairHearing-36. Write nothing under the repository. Write each draft to `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f/scratchpad/ledgers/`. Run no gate, suite or bar, and commit nothing.

### Items
1. Read the ledger rules in `memory/HYGIENE.md`, section "Acceptance ledger — how a built unit evidences its criteria". Model each draft on the four existing ledgers in `memory/builds/dFairHearing/build/`, the files ending `-acceptance-ledger.md`, for units 37 to 40.
2. For each unit, read:
   - its spec's acceptance section and change log;
   - its builder return(s) under `memory/builds/dFairHearing/build/`;
   - its pass commit, found with `git log --grep "Pass: <unit id>$"`.
3. Write `2026-11-04-build-<unit id>-1-acceptance-ledger.md` containing:
   - the title;
   - `**Serves:** journal <unit id>`;
   - a short paragraph naming the spec rev built and the pass commit, and saying the main loop drafted the ledger at the close from the builder return;
   - `**Evidences:** <unit id>`;
   - one line per criterion the spec numbers.
4. Use the two forms only. OBSERVED carries a backticked token that also appears backticked in the criterion's own text. AMENDED names the rev that changed the criterion.
5. Never invent an observation. If nothing on disk evidences a criterion, it gets no line. List it under UNEVIDENCED in your return, with its command.
6. New text must not cite a check, section or method rule by a bare number; name each by what it checks. Use LF line endings.

### Acceptance
One draft per unit in your batch. Every line in a draft is backed by a record on disk, and every criterion without one is listed under UNEVIDENCED.

### Gates
None you run.

### Non-goals
No edit under the repository, no spec change, and no observation run on the main loop's behalf.
