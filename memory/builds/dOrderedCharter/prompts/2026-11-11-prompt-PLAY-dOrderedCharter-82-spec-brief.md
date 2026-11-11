**Serves:** research PLAY-dOrderedCharter-82

# Brief: spec PLAY-dOrderedCharter-82 — the third close bar's python-reads guard red

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. The close's third bar over `8ecef2cf1` failed five legs. Three are not this build's to fix (the inherited
policy check, the dead-path hit on gov's install receipt the lander rewrites, and a `database is locked` collision on the shared
index); memory hygiene is the main loop's records; one is a product red.

## The brief

### Goal

Write spec PLAY-dOrderedCharter-82, a micro-spec for one mechanical fix unit at order 44 that clears the python-reads guard red.

### Items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold82/2026-11-11-spec-PLAY-dOrderedCharter-82.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md` for a Tier-1 micro-spec, as PLAY-dOrderedCharter-81 is
   written; carry its `**Derived:**` binding line; status line `DEFERRED · rev-1 · 2026-11-11 · node a · Tier-1 · base <HEAD short
   sha> · streams playbook · order 44 · advances PLAY-dOrderedCharter-38`.
2. **The red.** The `python reads (a name never bound, an import outside its guard)` leg prints fourteen lines of the form
   `py-reads: RED guard · govkit acceptance matrix · tools/memory-tree/<module>.py is imported and outside its guard`. The
   `govkit acceptance matrix` leg's guard in `tools/gate-legs.json` is `{prefix}/govkit/`, `{prefix}/playbook/`,
   `{prefix}/check-microformats.sh`, `{prefix}/check-line-length.sh` and `.lexicon.conf`; since PLAY-dOrderedCharter-78 the
   matrix's scratch install carries the renderer's requirement closure, so the leg imports memory-tree modules. Confirm the
   fourteen at HEAD by running the reads checker's own reader, and whether any other kit directory (the policy kit's) is imported
   too; name the narrowest guard addition that covers them, read the guard grammar the other legs use, and say whether the
   matrix leg's ceiling or a guard-parity row moves with it.
3. Criteria observe the reads leg's verdict line going green over the tree. The spec-token check grades a live spec's acceptance
   bullets word by word: no acceptance command whose words include an untracked path, no `path#symbol`, no suite as the
   observation, each backticked span on one line, every tripped leg on the gates line. Every new fact pinned.

### Acceptance

- Spec 82 builds as written over HEAD, and its criterion observes the python-reads leg going green.

### Gates

None run on the repository: this is a scratch write.

### Non-goals

- No code. No edit outside the scratch copy. Nothing outside this red.
