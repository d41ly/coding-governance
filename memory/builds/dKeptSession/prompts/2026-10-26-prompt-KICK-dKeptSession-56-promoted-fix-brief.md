**Serves:** research KICK-dKeptSession-56

# Promoted-fix brief — dKeptSession, the four findings over the round-2 promotions

The round-2 spec audit (`unattended-build.js` run `wf_300de914-24f`, record
`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`) promoted
`KICK-dKeptSession-45` to `-56`. The main loop then ran `tools/check-spec-tokens.py` and
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`; every finding is in one spec,
`memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-56.md`, the round's minors batch.

Fix exactly these, in place, keeping its `**Derived:**` line, §3 edges and §8 marks as they stand. The spec is
uncommitted, so it stays at the rev its header carries. Write nothing else, commit nothing, and return each finding
with what you changed. The spec brief,
`memory/builds/dKeptSession/prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md`, still binds every rule.

## The findings

1. `check-spec-tokens` `[path]` and `[bar]` · an acceptance criterion names `tools/loop/selftest.py`, a suite and an
   untracked path. Observe the checker on a staged break or a fixture instead, citing any file by basename, and keep
   the suite on a `New arm:` line in §7 if it gains an arm.
2. Hygiene check 12 · AC17 and AC28 name no backticked witness, required since `SPEC_WITNESS_CUTOFF`. Give each the
   backticked command, file or output token a pass observes.
3. Hygiene check 25 · §2 item S16 retires a named thing and carries no `**Readers:**` clause. Write `**Readers:**`
   with its `by name:` half (the readers that spell the name) and its `by value:` half (the readers of its value, or
   `NO VALUE READERS` and a reason), each found by `git grep`; a reader that lives only on an unlanded parent branch
   takes `READER NOT IN TREE` and the reason, in the shape
   `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md` S6 uses. If S16 retires nothing, reword
   it so no retirement word sits beside a backticked token.

When done, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm it prints no finding on
a dKeptSession spec. The main loop re-runs `check-spec-tokens.py`.
