# Build brief — TOOL-dFairHearing-1, pass (b): the verdicts

**Serves:** research TOOL-dFairHearing-1

Build pass (b) of this unit from `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md`, its latest rev. Pass (a) is `9028a7ee6`: it built S1 to S4, ran replay 2 and staged replays 3 and 4. The main loop has since run replays 3 and 4; their raw returns are committed under `memory/builds/dFairHearing/build/`:

- `2026-11-03-build-TOOL-dFairHearing-1-replay-3-synthesis-a-return.md` and `…-synthesis-b-return.md`: each synthesizer's verbatim return and the report it wrote.
- `2026-11-03-build-TOOL-dFairHearing-1-replay-4-skeptic-23-return.md` and `…-skeptic-control-return.md`: each skeptic's verbatim return.
- `2026-11-03-build-TOOL-dFairHearing-1-replay-void-runs.md`: the first runs, voided because each agent read its staged file's bar section, and why.
- Replay 2's figures are pass (a)'s `2026-11-03-build-TOOL-dFairHearing-1-replay-2.md`.

## This pass

- Write S9's one verdict record: each replay's figures, its bar, its verdict and its raw outputs by path. Judge each verdict yourself from the raw returns and the staged files' bars; the main loop states none for you.
- For each replay that met its bar, flip its switch's default as S9 says, in `tools/workflows/tier2-review.template.js`, re-rendered into `tools/workflows/tier2-review.js`, with the README, suite arms and floor that move with it. A replay that missed its bar changes nothing.
- Record these departures, beside F7's, in the verdict record or a deviation record as README rule 5 asks: replays 3 and 4 ran as direct role spawns (the agent-cap hook admits no inline Workflow script); the two synthesizers ran at their agent type's high effort, not the staged medium, since a direct spawn takes no effort; their reports went to the run's scratch, not the committed path their prompt names; the first runs are void and the second runs read bar-free copies whose sha256 prefixes each return record names.
- Set the spec to CLOSED in this pass's commit. This is the unit's last pass.

## Standing rules

- Before you commit, run `python tools/lexicon/lexicon.py --check` (your role's one gate) and read its `verb offenders <n> over pin <m>` line: your commit must not raise `<n>` above what it read at your pass's start. Name every new definition from the declared VERBS table, `lexicon.py --suggest <name> --as <cell>`, nested helpers included.
- Route the session card to this unit with `manifest-check.sh --card --append` BEFORE the first write; never copy a drafted file into the tree with `cp` or any other shell write to get past the write gate.
- Run no gate leg, no suite and no bar. Every `New arm:` line is owed to the main loop at the close.
- Declare with `--dispatch` every path the commit will carry, the generated renders a hook forces into it included (`memory/LIVE.md`, `memory/backlog/TOOL.md`, this build's `README.md`, the codebase map's `symbols.json` when a shell or Python definition moves, a map dossier with `memory/map/generated/` when a new file needs claiming, and dClosedLoop's as-built view when a deviation record lands). Never declare the run-state file `RUN.md`: check 49 refuses it, and the driver's own verbs write it.
- Writes stay inside the spec's files touched and this build's folder; a write outside both is a departure, recorded or returned.
- Temp files go in the run's scratch root, never under the repo.
- A spec criterion a correct build cannot pass is a `DIVERGENCE:` naming the criterion, never a build around it.
