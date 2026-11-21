**Serves:** research KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60

# Brief — dKeptSession: specs 20, 32, 58, 59, 60 checked for behaviour before their builds

## The prompt

> /unattended dKeptSession

## The brief

### Goal

Specs 20, 32, 58, 59, 60 were re-grounded on the run's tree, and every textual check passes on them. The units built so far
still diverged at build on behaviour no textual check reads: a criterion naming an exit its verb never gives, a
fixture copy lacking a kit or a file the new code imports, a fixture guard not covering what a fixture copies, a new
rule turning a reader's refusal into a silent fallback, a factory whose halves did not fit a caller. Since the
re-ground, KICK-dKeptSession-1, -19, -33 and -2 have landed (the preset store and its checks in `tools/policy/presets.py`
and `presets.toml`, the shrink-list factory and reader join, the derived-row rules, and the preset step in
`tools/policy/policy.py`'s reader), KICK-dKeptSession-3 is being built, and specs 34, 40, 4, 49, 50 and 54 build
before yours. Read those specs for what they build. Check each spec
against the tree as it now stands, and fix what would make its builder diverge.

### Items

1. F-behaviour: for each criterion, run or read its command against the verb it calls and the fixture that seeds it, and confirm the exit, output and seed it names are the ones the code gives.
2. F-callers: grep every caller of each function the unit changes or adds a rule to, and every suite or fixture that copies a file the unit touches or imports; where one would break, the spec says how (a copy added, a guard widened, a refusal kept) and names its paths in Files touched.
3. F-landed: re-cite against KICK-dKeptSession-1's landed code (and units 19, 33 and 2, and the specs ordered before yours for what they build); an item unit 1 already built is reduced to its observation.
4. F-positional: no `path:number` token stands in the spec unless it is a blob pin; a quoted refusal line is described, not quoted with its line suffix.
5. F-hook-paths: Files touched names the paths the commit hook will need: a watched file's kickoff-manifest re-stamp (`memory/guides/SESSION-KICKOFF.md`), `memory/map/generated/symbols.json` for new code symbols, and any reference page or docs list a re-render moves.
6. Keep each spec within the live-spec size cap, pin every figure with DERIVED or PINNED, leave no fork open (a fork you rule is marked `RESOLVED (agent, 2026-11-21, delegated): <option>, rung <n>; <reason>. widens: <value|none> · relaxes: <value|none>`), and where you change nothing in a spec, say so and leave it at its rev.

### Acceptance

Each spec you changed is at a new rev with one revision-log line naming this brief by its file stem, and
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession <its id>` report nothing for it.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip, and no spec other than 20, 32, 58, 59, 60. Another writer may be
checking other specs, and unit 3 is being built: read them, never write them.
