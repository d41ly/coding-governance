**Serves:** research TOOL-aQueuedIndex-1

# Brief: spec TOOL-aQueuedIndex-1 — writers of the shared tag index queue instead of failing

## The prompt

> fix the tag index contention so bars don't flake

— owner, 2026-11-12. The build's brief, which the owner accepted, is
`memory/builds/aQueuedIndex/prompts/2026-11-12-prompt-TOOL-aQueuedIndex-1-brief.md`; read it whole first.

## The brief

### Goal

Write spec TOOL-aQueuedIndex-1, the Tier-2 spec for the build's one unit: every write to the node's shared tag index takes
its lock first and waits past a full tree build, and a writer that waited re-reads whether its tree was built before building
it.

### Items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/foldaq1/2026-11-12-spec-TOOL-aQueuedIndex-1.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md`; status line `DEFERRED · rev-1 · 2026-11-12 · node a ·
   Tier-2 · base <HEAD short sha> · streams tooling · order 1`.
2. **The evidence.** In a scratch clone at `97e0841d7` with a fresh index, `gov_tag.py check` raced against
   `instructions_edit.py check` red the first race: the tags check refused at 31 s with `database is locked`, inside the 60 s
   `BUSY_TIMEOUT`. With `isolation_level="IMMEDIATE"` on the index connection alone, one race of two still red after 94 s; with
   IMMEDIATE plus a 600 s timeout, three of three passed, the second writer taking about 150 s against the first's 95 s.
   Reproduce the race yourself before designing, and read why the first red came before the timeout.
3. **The design.** Read every connection to the index (`tools/playbook/tag_index.py#load_index`, the two in
   `tools/playbook/gov_tag.py`, and any other reader the code names) and every write block under them, then say how each write
   takes its lock first, what the busy timeout becomes and why that value, and where a waiter re-reads `tree_built` so it reuses
   the tree the other writer built. Keep the index file, its schema version and its journal mode; the brief rules out a
   write-ahead log. A choice no seam decides is a fork with options and a recommendation; the run takes recommendations.
4. **The arm.** Declare a `New arm:` that races two writers over one unbuilt tree in a scratch repository of its own, never the
   node's index, observed red at BASE and green after; say which suite or self-test carries it and its wall-clock cost.
5. Criteria observe the race going green, and the waiter not rebuilding. The spec-token check grades a live spec's acceptance
   bullets word by word: no acceptance command whose words include an untracked path, no `path#symbol`, no suite as the
   observation, each backticked span on one line, every tripped leg on the gates line. Every new fact pinned, every new
   `path:line` blob-pinned, every minted function through the lexicon's `--suggest`.

### Acceptance

- Spec TOOL-aQueuedIndex-1 builds as written over HEAD, and its criteria observe both writers of one race exiting green.

### Gates

None run on the repository: this is a scratch write.

### Non-goals

- No code. No edit outside the scratch copy. No change to what the index stores.
