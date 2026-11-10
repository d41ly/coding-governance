# Revision brief — aSmoothedDispatch: units 6 and 7 are inside the owner's go

**Serves:** research TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7

## The brief

### Goal
Author the specs of units 6 and 7. The spec stage's writer for unit 6 refused it, reading the owner's "Yes, build 1–5" as unit numbers 1 to 5. The numbers are the rows of the analysis table the owner was answering, and that table had five rows, each a fix:
- row 1, the spec-token check at dispatch, became units 4, 5 and 7;
- row 2, `--writes` taking one path, is unit 1;
- row 3, the stale card route blocking builder edits, is unit 6;
- row 4, the refused run-state path, is unit 2;
- row 5, `--help`, is unit 3.

So unit 6 is the owner's row 3, and unit 7 completes row 1. Unit 5's spec, now on disk, found the scratch-guard hook already admits a spec writer running `tools/check-spec-tokens.py` with any argument. It therefore adds a one-spec `--spec <path>` mode to the checker. Its §9 hand-off says the `gov-spec-writer` role prompt, `tools/roles/house/gov-spec-writer.md`, still tells writers they may run only the hygiene gate and the lexicon. A writer told nothing never runs the new mode. Unit 7 is that prompt change, a separate document and so a separate unit (M2). It may also advance TOOL-aDeferredBar-6, which unit 5 names.

### Items
1. Unit 6, as the build brief's item 6 states it: a builder's product write is not refused when the session card's `## route` names a CLOSED unit while the build's run-state file holds an open `--dispatch` row for another unit. Either `--dispatch` appends that unit's route to the card, or scratch-guard admits a unit with an open dispatch row; pick the one that keeps one source. Read `tools/hooks/scratch-guard.js`'s route reader and its buildable-unit rule, and the 63 refusals' text in the build brief, before choosing. [planned TOOL-aSmoothedDispatch-6]
2. Unit 7: the `gov-spec-writer` house prompt (`tools/roles/house/gov-spec-writer.md`) states that the writer runs `python tools/check-spec-tokens.py --spec <its spec>` over each spec it wrote, fixes every hit, and only then returns. The rendered agent file and any parity or render gate follow by the roles kit's own render step (`tools/roles/render_agents.py`). Its spec names unit 5 as the provider of `--spec`, ordered after unit 5. [planned TOOL-aSmoothedDispatch-7]

### Acceptance
1. Unit 6: a fixture card routing a CLOSED unit, with an open dispatch row for an INPROGRESS unit, admits the builder's Edit on a product path; with no open dispatch row the Edit is refused as today.
2. Unit 7: the rendered `gov-spec-writer` agent file carries the instruction, the roles kit's render check is green over it, and a spec writer's one-spec checker call is admitted by the hook.

### Gates
The touched kits' gate legs and self-test arms, spec tokens, memory hygiene, lexicon naming predicates, kit epoch, kit version markers; then the full bar once, at the landing.

### Non-goals
The `--close` bar order; any other role prompt; any instruction about heredoc quoting, sleep polling or `/tmp`; asks TOOL-dFairHearing-52, -53, -55 and -56; any refusal guarding a real defect.

### Limitations
Kit versions move through the lander's `mint`, not by hand. Unit agents run no gate legs. Units 1, 2, 3, 4 and 6 share `tools/unattended/unattended.sh` when unit 6 picks the driver side, so they build one at a time.
