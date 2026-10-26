**Serves:** research KICK-dKeptSession-65

# Promoted-fix brief — dKeptSession, the one finding over the round-6 promotion

The round-6 spec audit (`unattended-build.js` run `wf_9c01a891-b4b`, record
`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-64-spec-audit.md`) promoted
`KICK-dKeptSession-65`. The main loop then ran `tools/check-spec-tokens.py`: one `[path]` hit in
`memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-65.md`. Hygiene checks 2, 12 and 25 are clean.

Fix exactly this, in place, keeping the spec's `**Derived:**` line, §3 edges and §8 marks as they stand. It is
uncommitted, so it stays at the rev its header carries. Write nothing else, commit nothing, and return what you
changed. The spec brief, `memory/builds/dKeptSession/prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md`,
still binds every rule.

## The finding

1. `{prefix}/memory-tree/gen_build_index.py` reads as an untracked path: the checker does not expand the install
   prefix. In §6 cite the file by basename (`gen_build_index.py`) or by its path in this repository
   (`tools/memory-tree/gen_build_index.py`, which is tracked), whichever the criterion means.

When done, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm it prints no finding on
a dKeptSession spec. The main loop re-runs `check-spec-tokens.py`.
