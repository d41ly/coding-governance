**Serves:** journal TOOL-dDeclaredLoop-18

# Builder return — TOOL-dDeclaredLoop-18, dispatch 2: refused at the dispatch gate, nothing built

Run wf_d21a2038-553. The builder read spec rev-4 against the code and found no divergence in what it read, then ran its
one dispatch declaration, which the driver refused on check 118: the spec-audit chain reads CONTINUE at round 0, reason
unreviewed, and names 98 ids to audit, every live spec of the build. Nothing was written and nothing committed.

## Why the gate reads round 0

- The build README declares a spec audit, and this run began after the fold cutoff the project conf declares, so the dispatch
  gate reads the chain record. The build holds no chain-rounds record: its twelve audit rounds ran in the spec run, before
  that record existed, and are recorded only as review records under `reviews/`.
- The owner ended that audit chain at round 12, quoted in
  `memory/builds/dDeclaredLoop/prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-owner-review-stop.md`.

## What the builder noted for the next dispatch

- AC8's command is the argv of the tags leg, so a pass can only probe the changed checks; the leg itself is owed at the close.
- The write set adds the generated companions to the spec's eight files: the ledger, the spec, the run-state file, the build
  README, the live index, the month ledger and the four generated map files.
- Owed at the close once built: the section 7 new arm on the playbook adopter, red on its four plants and then green.
