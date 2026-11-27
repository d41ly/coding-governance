**Serves:** journal TOOL-dTotalRecall-87
**Caused-by:** TOOL-dTotalRecall-87

# TOOL-dTotalRecall-87 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `02e6a8172` from [2026-11-24-prompt-TOOL-dTotalRecall-87-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-87-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `073d03dd7`.

## Why

Built as spec rev-3 reads, with no divergence. AC1 to AC4 were observed by probes of this unit's own code, except that AC4's literal "every line as at the pass base" holds only with each literal's own line number masked. The spec is CLOSED in the pass commit.

## Summary

`tree_lib.py` gains `resolve_memory_root`, and `resolve_kept_home` joins only what it returns. In `record_causes.py`, `check_kept_home` prints `read nowhere` for a refused root and adds no second red. `run_cause_writers` is shared by `main` and `run_fixture`, and the plants `kept-home-trailing-root` and `kept-root-blank` are new, with their arm in `check-memory-hygiene.test.sh`. The map's `symbols.json` was regenerated.

Checks run (DERIVED 2026-11-24, node a):
- AC1: the resolver probe gave the four stated roots. The four refused values each raised `ValueError` naming `MEMORY_ROOT`, as did `/`, a lone dot, `a/../b` and a leading double backslash.
- AC2: `kept-home-trailing-root` exited 0 with no red, and both home lines named one home under `docs/memory`. With the conf's raw value joined in a probe process, its `read at` line named a doubled slash. (DERIVED 2026-11-24, the pass)
- AC3: `kept-root-blank` exited 1 with one red and the `read nowhere` line. With the blank refusal skipped, or with the raw value joined, it exited 0. (DERIVED 2026-11-24, the pass)
- AC4: the probe printed the home three times, then `MEMORY_ROOT` twice. Over the base's engines it printed the second and third as spelled and a home for the last two. `--cause-writers` on gov exited 0, and its 128 lines equal the base's once each literal's own line number is masked. This unit's added lines move the literals below them, as in unit 73's ledger. (DERIVED 2026-11-24, the pass)
- The plants `kept-home-rooted`, `kept-row-docs-root` and `legacy` were also run: exit 1 with its one red, 0 and 0. (DERIVED 2026-11-24, the pass)
- Naming lexicon: OK for both new functions. These fixture and probe runs stand in for `memory-hygiene self-test` and `record causes`.

Not exercised by a run: the `alias-compare MEMORY_ROOT=` red, read from the existing catch in `record_kinds.py#check_alias_compares`; and a `..` or drive root through a whole census run.

Owed to the close: every leg in section 7, and the RED-first observation of the new `check-memory-hygiene.test.sh` arm (AC2 AC3), staged by joining the conf's raw value in `resolve_kept_home`. (DERIVED 2026-11-24, the pass)

Bug-class checklist: run over HEAD~1..HEAD, 41 classes selected, nothing to fix. I checked `sourced-conf-blank-overrides-the-default` (the blank is refused, not defaulted), and `staged-break-substitutes-a-synthetic-value` and `fixture-passes-by-finding-nothing` (the raw-join runs show the conf rewrite took effect). (DERIVED 2026-11-24, the pass)

No command was skipped for its bound. The gate guard blocked one read-only `file` command and the worktree guard blocked two compound commands; I re-ran the needed parts as simpler commands, and nothing had executed. The commit trailer is the charter's `Claude Opus 5`. Nothing outside the declared set was written; the spec-88, 91, 93, 94 and 95 prompt files stay untracked and unstaged. (DERIVED 2026-11-24, the pass)
