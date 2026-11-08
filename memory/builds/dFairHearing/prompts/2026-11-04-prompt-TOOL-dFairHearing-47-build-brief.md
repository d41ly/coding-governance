# Build brief — TOOL-dFairHearing-47

**Serves:** research TOOL-dFairHearing-47

Build this unit from `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-47.md`, its latest rev, and nothing else. The packet `memory/builds/dFairHearing/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md` is the chain context the spec was written from; where the two differ the spec wins.

- This unit repairs reds the close's lint legs attribute to this build, specced in this build run and built from its spec as written.
- Units ahead of this one in the build order are built; verify each line the spec cites against the file before relying on it, since earlier units moved them.
- Route the session card to this unit with `manifest-check.sh --card --append` BEFORE the first write; never copy a drafted file into the tree with `cp` or any other shell write to get past the write gate.
- Before you commit, run `python tools/lexicon/lexicon.py --check` (your role's one gate) and read its `verb offenders <n> over pin <m>` line: your commit must not raise `<n>` above what it read at your pass's start. Name every new definition from the declared VERBS table, `lexicon.py --suggest <name> --as <cell>`, nested helpers included.
- Run no gate leg, no suite and no bar. Every `New arm:` line is owed to the main loop at the close.
- Declare with `--dispatch` every path the commit will carry, the generated renders a hook forces into it included (`memory/LIVE.md`, `memory/backlog/TOOL.md`, this build's `README.md`, the codebase map's `symbols.json` when a shell or Python definition moves, and a map dossier with `memory/map/generated/` when a new file needs claiming). Never declare the run-state file `RUN.md`: the dispatch check refuses it, and the driver's own verbs write it.
- The main loop flips the spec to INPROGRESS before it dispatches you; the write gate admits a Tier-2 unit's writes under `tools/` at INPROGRESS only. Your one spec edit is the CLOSED flip in your commit.
- A spec criterion a correct build cannot pass is a `DIVERGENCE:` naming the criterion, never a build around it.
- Writes stay inside the spec's files touched and this build's folder; a write outside both is a departure, recorded or returned.
- Temp files go in the run's scratch root, never under the repo.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise.
