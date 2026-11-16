# Revision — aPiecewiseGrade: the owner's answer to TOOL-aPiecewiseGrade-4's F1

**Serves:** research TOOL-aPiecewiseGrade-2 TOOL-aPiecewiseGrade-4

## The prompt

> (b) Name file, no rename

The owner's answer, 2026-11-15, to TOOL-aPiecewiseGrade-4's F1, put through the session's question tool: "Which promotion does unit 2 build?", with options (a) rename the `mktemp -d` directory, (b) a name file and no rename, and (c) a lint unit first.

## The brief

### Goal
The owner resolved TOOL-aPiecewiseGrade-4's F1, "The lint cannot admit a rename across the driver's two halves. Which promotion does TOOL-aPiecewiseGrade-2 build on this contract?", as (b): the read half writes the live generation's name into a file beside the whole key and removes the old generation, renaming nothing. TOOL-aPiecewiseGrade-2 is rewritten to that promotion; TOOL-aPiecewiseGrade-4's contract serves it unchanged.

### Items
1. In `memory/builds/aPiecewiseGrade/spec/2026-11-15-spec-TOOL-aPiecewiseGrade-4.md`, F1 carries `RESOLVED (owner, 2026-11-15): (b) Name file, no rename` in its own span, its header gains the ratified pointer, and its rev bumps with a revision-log line naming this record by its file stem. Nothing else in it moves unless the resolution makes a sentence false; name any such sentence in the log line.
2. Rewrite `memory/builds/aPiecewiseGrade/spec/2026-11-15-spec-TOOL-aPiecewiseGrade-2.md` to option (b): where the name file lives and what it is called, how the read half writes it only where the whole key is recorded, how every reader of the cache resolves the live generation through it, the shape check on every name read back before any `rm -rf` sees it, and the sweep that removes every generation but the live one. State what a run killed between writing the name and removing the old generation leaves, and why the next run is still correct. No `mv` of a generation directory remains, and no row in `memory/project/temp-name-sites.txt` moves.
3. Its criteria observe each of those: the name file's content after a recorded dispatch, no promotion on a refused or tree-moved dispatch, a planted malformed name refused before removal, the sweep sparing the live generation, `scan_temp_file` over the built driver reporting no new site, and every driver line byte-identical to the pre-change driver's. Each new arm is one that can be seen red.
4. Bump its rev and add a revision-log line naming this record by its file stem. Its order stays 4 and its edges keep the build order 3, 1, 4, 2.
5. Stage both specs and clear `python tools/check-spec-tokens.py --spec` over each. Do not commit. Return each spec's path and status line, each new or changed criterion's id with one line, any fork with its recommendation, and the checker's final line for each.

### Acceptance
- TOOL-aPiecewiseGrade-4's F1 reads RESOLVED with the owner's pick, its rev bumped and its log naming this record.
- TOOL-aPiecewiseGrade-2 at a bumped rev, its promotion by a name file with no rename, each piece of item 2 observed by a criterion.

### Gates
`check-spec-tokens.py --spec` over each spec.

### Non-goals
- Any edit to TOOL-aPiecewiseGrade-1's or TOOL-aPiecewiseGrade-3's CLOSED spec.
- A row raised in `memory/project/temp-name-sites.txt`, and a lint change.
- Any change to a verdict, a refusal line, the summary line or an exit status.
- Building anything.
