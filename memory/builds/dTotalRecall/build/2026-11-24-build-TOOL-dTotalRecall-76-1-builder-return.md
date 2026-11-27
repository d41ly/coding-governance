**Serves:** journal TOOL-dTotalRecall-76
**Caused-by:** TOOL-dTotalRecall-76

# TOOL-dTotalRecall-76 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `b59778f81` from [2026-11-24-prompt-TOOL-dTotalRecall-76-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-76-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `67ffd1289`.

## Why

Built as spec rev-4 states. Every read-only item held at the tip, so no deviation record was owed, and no divergence was found.

## Summary

Built:
- S10: both `run_fixture`s (record_causes.py, record_kinds.py) hold `(*GIT_ENV_LEAKS, "GOV_REMOTE", "GOV_DEFAULT_BRANCH")` aside through `set_env_aside`. record_kinds' teardown is now an ExitStack callback. The arm is added to tools/memory-tree/check-memory-hygiene.test.sh.
- S16: `reads` base and history on the three ratchet rows in tools/govkit/registry.toml, rendered into tools/gate-legs.json by `leg_factory.py --write`. A second run moved no byte.
- S17: `census-kept-paths.txt` is out of `PROJECT_REGISTRY_EXTRA`, and its comment is reworded.
- S18: section B re-read with none corrected, `last-audit` re-stamped and `last-body-change` set to b59778f81, all in the same commit.
- The spec is CLOSED. The ledger is memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-76-1-acceptance-ledger.md, with the S19 sweep block copied in by script from the brief.

Observed by probe (no gate, suite or --selftest ran):
- AC1 to AC3: the blob probe, the greps and the ancestor reads, standing in for the history reads. Every count is as pinned (DERIVED 2026-11-24).
- AC4 to AC7, AC9 and AC15: `--fixture --plant` runs and python probes, standing in for the `memory-hygiene self-test`, `record-kinds` and `record causes` legs. AC5 was red at the base (both plants refused, exit 2) and gives exit 1 with one red each at the tip. The AC7 probe ran at the base and over this edit, and the outputs are equal. (DERIVED 2026-11-24, the pass)
- AC8, AC10, AC11 and AC14: the commands the spec states.
- AC12, read after the commit: W and S are both 67ffd1289, the watched count since `last-body-change` is 1 (DERIVED 2026-11-24), and 408d05723 is its ancestor.
- AC13: read from the main loop's sweep, with 64 unit lines for population 64 (DERIVED 2026-11-24). Its one red span is unit 22's check 9, closed by unit 3's pass f8b950c13. No span is OPEN. pass(69) reads clean for C5.

Pre-commit hooks passed on the second attempt. The first was refused by check 9, because a sibling spec writer had moved spec 96 after my render. I re-rendered the worktree README and staged only my own rows. (DERIVED 2026-11-24, the pass)

Owed to the close: section 7's legs; the RED-first observation of the one new arm (AC5, staged by taking the two names out of each held tuple); the checker's C5 and C9 verdict and check 3's verdict over gov (main-loop pass legs).

Bug-class checklist run over HEAD~1..HEAD: no item required a change. The conf edit is gov-only, so nothing reaches an adopter. The hygiene suite gained two plant runs; its budget row is not re-measured and is left to the close.

Reported, not fixed:
- The manifest's 2026-11-10 dated correction has met its prune condition. It stands, as unit 75 left it. (DERIVED 2026-11-24, the pass)
- The worktree README still shows sibling writers' rows for units 89, 96 and 97, left unstaged. (DERIVED 2026-11-24, the pass)
- memory/map/generated needed no change.
