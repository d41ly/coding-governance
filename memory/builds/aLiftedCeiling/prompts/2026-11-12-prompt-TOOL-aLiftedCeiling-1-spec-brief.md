**Serves:** research TOOL-aLiftedCeiling-1

# Brief: spec TOOL-aLiftedCeiling-1 — the instruction-edits leg's ceiling covers its wait on the tag index

## The prompt

> Yes, raise it

— owner, 2026-11-12, answering "Raise instruction edits' 180 s ceiling so the wait stops costing a retry?". The build's brief
is `memory/builds/aLiftedCeiling/prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-1-brief.md`; read it whole first.

## The brief

### Goal

Write spec TOOL-aLiftedCeiling-1, a Tier-1 micro-spec for one unit at order 1 that raises the `instruction edits (manifest
checks)` leg's declared ceiling in `tools/gate-legs.json` to cover its wait on the other tag-index writer.

### Items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/foldal1/2026-11-12-spec-TOOL-aLiftedCeiling-1.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md` for a Tier-1 micro-spec; status line `DEFERRED · rev-1 ·
   2026-11-12 · node a · Tier-1 · base <HEAD short sha> · streams tooling · order 1`. Write no open fork: where a choice remains,
   take your recommendation and mark it resolved in its own span.
2. **The value.** The leg is the second writer of the shared tag index since aQueuedIndex (landed `aa8f08000`): it now waits for
   the tags leg's tree build instead of failing, and timed out at its 180 s ceiling and passed on retry at both of that build's
   bars. Its partner `tags (the resolver's checks)` declares 420 s. Read the run-gates kit's ceiling rules (its README's ceiling
   sections and `tools/run-gates/derive-ceilings.py --help`), the leg's readings in the runner's records and the evidence file,
   and size the new ceiling from them; say why that value and not another.
3. **The evidence.** Say whether the raise owes an evidence row in `tools/run-gates/ceiling-evidence.txt` (a generated file, never
   hand-edited) and how it is written, and which kit checks grade a ceiling against its evidence.
4. **Watched file.** `tools/gate-legs.json` is on the kickoff manifest's `watch:` list; the unit re-stamps the manifest.
5. Criteria observe the manifest's new value, the evidence the kit reads for it, and the leg finishing inside its new ceiling in a
   race of the two tag-index checks on a fresh index in a scratch clone. The spec-token check grades a live spec's acceptance
   bullets word by word: no acceptance command whose words include an untracked path, no `path#symbol`, no suite as the
   observation, each backticked span on one line, every tripped leg on the gates line. Every new fact pinned, every new `path:line`
   blob-pinned.

### Acceptance

- Spec TOOL-aLiftedCeiling-1 builds as written over HEAD, and its criteria observe the leg run once inside its new ceiling.

### Gates

None run on the repository: this is a scratch write.

### Non-goals

- No code. No edit outside the scratch copy. No other leg's ceiling, and no change to the tag index or its busy timeout.
