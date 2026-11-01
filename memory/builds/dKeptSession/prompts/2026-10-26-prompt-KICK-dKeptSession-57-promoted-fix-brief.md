**Serves:** research KICK-dKeptSession-57 KICK-dKeptSession-62

# Promoted-fix brief — dKeptSession, the three findings over the round-3 promotions

The round-3 spec audit (`unattended-build.js` run `wf_6d475fdb-d1e`, record
`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`) promoted
`KICK-dKeptSession-57` to `-62`. The main loop then ran `tools/check-spec-tokens.py` and
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`.

Fix exactly these, in place, keeping each spec's `**Derived:**` line, §3 edges and §8 marks as they stand. The specs
are uncommitted, so they stay at the rev their header carries. Write nothing else, commit nothing, and return each
finding with what you changed. The spec brief,
`memory/builds/dKeptSession/prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md`, still binds every rule.

## The findings

1. `2026-10-26-spec-KICK-dKeptSession-57.md` · `check-spec-tokens` `[path]` · `tools/policy/policy.py` in §6 is an
   untracked path. Cite it by basename (`policy.py`) in §6, keeping the full path in §2, §4 and Files touched.
2. `2026-10-26-spec-KICK-dKeptSession-62.md` · `check-spec-tokens` `[bar]` · an acceptance criterion names
   `resolve-python.test.sh`, a suite. Observe the checker on a staged break or a fixture instead, and keep the suite
   on a `New arm:` line in §7 if it gains an arm.
3. `2026-10-26-spec-KICK-dKeptSession-62.md` · hygiene check 25 · §2 item S27 retires a named thing and carries no
   `**Readers:**` clause. Write `**Readers:**` with its `by name:` half and its `by value:` half (or
   `NO VALUE READERS` and a reason), each found by `git grep`; a reader only on an unlanded parent branch takes
   `READER NOT IN TREE` and the reason, in the shape
   `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md` S6 uses. Reword S27 instead only if it
   truly retires nothing, and say why in your return.

When done, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm it prints no finding on
a dKeptSession spec. The main loop re-runs `check-spec-tokens.py`.
