# Build brief — TOOL-dFairHearing-1

**Serves:** research TOOL-dFairHearing-1

Build this unit from `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md`, its latest rev, and nothing else. The packet `memory/builds/dFairHearing/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md` is the chain context the spec was written from; where the two differ the spec wins.

- This is the build run of dFairHearing: every unit was specced and audited by the spec run, and the owner stopped the spec-audit chain after round 5 (`memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-owner-stop-reviews.md`), so no spec is re-audited before it is built.
- Units ahead of this one in the build order are built; verify each line the spec cites against the file before relying on it, since earlier units moved them.
- Route the session card to this unit with `manifest-check.sh --card --append` BEFORE the first write; never copy a drafted file into the tree with `cp` or any other shell write to get past the write gate.
- Before you commit, run `python tools/lexicon/lexicon.py --check` (your role's one gate) and read its `verb offenders <n> over pin <m>` line: your commit must not raise `<n>` above what it read at your pass's start. Name every new definition from the declared VERBS table, `lexicon.py --suggest <name> --as <cell>`, nested helpers included.
- Run no gate leg, no suite and no bar. Every `New arm:` line is owed to the main loop at the close.
- Declare with `--dispatch` every path the commit will carry, the generated renders a hook forces into it included (`memory/LIVE.md`, `memory/backlog/TOOL.md`, this build's `README.md`, the codebase map's `symbols.json` when a shell or Python definition moves, and a map dossier with `memory/map/generated/` when a new file needs claiming). Never declare the run-state file `RUN.md`: check 49 refuses it, and the driver's own verbs write it.
- The main loop flips the spec to INPROGRESS before it dispatches you; the write gate admits a Tier-2 unit's writes under `tools/` at INPROGRESS only. Your one spec edit is the CLOSED flip in your commit.
- A spec criterion a correct build cannot pass is a `DIVERGENCE:` naming the criterion, never a build around it.
- Writes stay inside the spec's files touched and this build's folder; a write outside both is a departure, recorded or returned.
- Temp files go in the run's scratch root, never under the repo.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise.

## This unit runs in two builder passes, with the main loop between them

Replay 1's runs are TOOL-dFairHearing-25's (its hands-off edge supersedes AC4, AC5 and AC9's replay-1 half), so this unit does not bundle, clone or run the design-audit preset. Replays 3 and 4 spawn agents, and an agent inside this sidechain cannot spawn one; the spec names the main loop as the adjudicator.

- **This pass (a):** build S1 to S4 (the known-set file, `parse_known_set`, `read_matched_list`, `--known-set`/`--matched`, the calibration with its two committed matched lists and the weak-candidate observation), and run replay 2 (S6) by its deterministic probe, recording its figures and raw output under `build/`. Then STAGE replays 3 and 4: for each, write under `memory/builds/dFairHearing/build/` the exact input the main loop hands its agent — for replay 3, one synthesis prompt per run (A and B) as the harness renders it under `addressTwins: 'shown'`, naming the negative pair; for replay 4, one skeptic prompt per fix (#23's and the §8 F4 control), as the harness renders the fix question under the switch unit 8 shipped — and the bar each must meet. Commit with `Pass: TOOL-dFairHearing-1` and LEAVE THE SPEC AT INPROGRESS: this pass does not close the unit, and that is this brief's instruction, not a divergence. Return `committed: true` and list the staged input files in `summary`.
- **The main loop** then runs the four agents on those inputs, writes their raw outputs beside them, and adjudicates.
- **Pass (b)**, a second dispatch of this unit, writes the S9 verdict record, flips each switch whose replay met its bar, and closes the unit.
