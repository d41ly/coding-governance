**Serves:** research KICK-dKeptSession-64

# Promoted-fix brief — dKeptSession, the three findings over the round-5 promotion

The round-5 spec audit (`unattended-build.js` run `wf_ed6db077-277`, record
`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-63-spec-audit.md`) promoted
`KICK-dKeptSession-64`. The main loop then ran `tools/check-spec-tokens.py`: three `[path]` hits, all in
`memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md`. Hygiene checks 2, 12 and 25 are clean.

Fix exactly these, in place, keeping the spec's `**Derived:**` line, §3 edges and §8 marks as they stand. It is
uncommitted, so it stays at the rev its header carries. Write nothing else, commit nothing, and return each finding
with what you changed. The spec brief,
`memory/builds/dKeptSession/prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md`, still binds every rule.

## The findings

1. `tools/loop/selftest.py` in §6 is an untracked path. Cite it by basename, or name the leg that runs it, keeping
   the suite on its `New arm:` line in §7.
2. `tools/unattended/VERBS.template.md)` reads as an untracked path because the closing parenthesis sits inside the
   backticks. Move the `)` outside the backtick span.
3. `memory/guides/UNATTENDED-VERBS.md)`: the same, the `)` moved outside the backticks.

When done, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm it prints no finding on
a dKeptSession spec. The main loop re-runs `check-spec-tokens.py`.
