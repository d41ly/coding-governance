**Serves:** journal TOOL-dTotalRecall-56
**Caused-by:** TOOL-dTotalRecall-56

# TOOL-dTotalRecall-56 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `1e9a5ebab` from [2026-11-23-prompt-TOOL-dTotalRecall-56-build-brief](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-56-build-brief.md), recorded whole; the pass tip is `798f98fc1`.

## Why

TOOL-dTotalRecall-56 is built from spec rev-6 as written. Every claim the spec makes about the code held when probed: the build-folder walk read `ALIAS_COMPARE_KEPT`, `CENSUS_KEPT_PATHS`, `read_kept_path` and `read_kept_rows` existed, `BIND_HEAD_LINES` is 12, line 380 of the deviations instrument holds the compare, and the instrument's blob is 30a1f15b. `record_causes.py` only reads the table's rows for its own census, so adding the alias row cannot turn its census red. No divergence.

## Summary

Commit 798f98fc1 builds TOOL-dTotalRecall-56. Its subject names the unit, its final trailer block has `Pass: TOOL-dTotalRecall-56` and the Co-Authored-By line, and the spec status is set to CLOSED (rev-6, 2026-11-23) in the same commit.

**What changed**
- `tools/memory-tree/tree_lib.py`: `CENSUS_KEPT_PATHS` gains the row `("check_alias_compares", "memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py", "pinned instrument")`.
- `tools/memory-tree/record_kinds.py`:
  - The build-folder walk in `check_alias_compares` now keeps a hit only where `read_kept_path("check_alias_compares", path)` returns a reason, and prints `kept <reason>`.
  - The red message now names `tree_lib.CENSUS_KEPT_PATHS`.
  - `ALIAS_COMPARE_KEPT` is gone, along with its comment and every place it was spelled (module docstring, function docstring, the keep test, the red message).
  - The fixture gains the plant `unkept-build-alias`: a new constant `FIXTURE_BUILD_ALIAS`, an entry in `PLANTS`, a `build_fixture` branch, and a `run_selftest` `want` entry. No new function.
- The commit also carries `RUN.md` and the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-56-1-acceptance-ledger.md`, plus what `gen_build_index.py --write` regenerated (`memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README). Every path was in the declared write set.
- `gen_map` was not needed because the map does not list constants. Neither file is on the kickoff manifest's watch list.

**Checks run (probes standing in for the gates; no gate, suite or bar ran)**
- **AC1** (stands in for the `record-kinds` leg on the real tree): `python record_kinds.py --check` lists `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py@30a1f15b:380 · kept pinned instrument`, and the build-folder count line reads `54 script(s) · 1 hits · 1 kept · 0 red`. The command still exits 1, because of two `RED pocket` lines (`dHomedResolver`, `history-verdicts`). Those are entries in the shared git common dir that this unit's census does not read, and the close's `record-kinds` leg grades them on its own node. `git grep -c "census: kept"` on the instrument printed nothing and exited 1, as AC1 requires.
- **AC2** (stands in for the `record-kinds` `--selftest` arm): `--fixture --plant unkept-build-alias` exits 1 with exactly one `RED alias-compare the fixture build bFix's planted probe script, line 14,` line. As a probe of the staged break, a `python -c` run with `read_kept_path` replaced by a keep-everything reader made the plant exit 0 with the line listed as kept.
- **AC3**: `git hash-object` on the instrument prints `30a1f15bf67566aeaf5b7e1628483c630b23b416`.
- **AC4**: `git grep -n ALIAS_COMPARE_KEPT -- tools` prints nothing and exits 1.

**Owed at the close:** the legs on the spec's gates section (`memory hygiene`, `lexicon naming predicates`, `recall floor`, `recall floor arms`, `record-kinds`). The new arm is `record_kinds.py` `--selftest`'s `want` entry for `unkept-build-alias` (covers AC2); its RED-first observation is still owed, staged by making the build-folder walk keep every hit.

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` exited 0 and selected 32 classes. I acted on these:
- fixture-passes-by-finding-nothing: the plant does trigger the rule, and the staged break turns it green.
- staged-break-substitutes-a-synthetic-value: the break used is the one the spec's `New arm:` line names.
- retirement-inventory-misses-readers-by-value: a grep found nothing that counts `CENSUS_KEPT_PATHS` rows or the alias census figures.
- ledger-token-wrapped: every backticked token in the ledger stays on one line.

No command timed out and nothing was skipped.
