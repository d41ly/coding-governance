**Serves:** journal TOOL-dTotalRecall-59
**Caused-by:** TOOL-dTotalRecall-59

# TOOL-dTotalRecall-59 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `206422580` from [2026-11-23-prompt-TOOL-dTotalRecall-59-build-brief](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-59-build-brief.md), recorded whole; the pass tip is `47afc8937`.

## Why

Spec rev-4 could be built as written. Every claim I checked held against the tree: the registry block, the absent `absorbs`, §4's probe output, the section `2o` helpers and the compare output format. I built it as written and committed it as one pass commit.

## Summary

TOOL-dTotalRecall-59 is built and committed as 47afc8937 on base 206422580. No gate, suite or bar ran in this pass. What the close still owes is listed at the end.

**What changed**
- `C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/lib/resolve-python.test.sh`, section `2o`:
  - Before the fixture's base commit, it appends `fx-merged` to the fixture's govkit registry: key `record`, fields `"path", "section", "check"`, `shrink-only`, `"section"` verbatim, home `memory/project/fx-merged.txt`.
  - It writes that home with two rows: `a.md spec-audit kind-schema` and `a.md - causes`.
  - After the AC3 group it adds the case `merged-home-gained`. With `b.md - causes` planted, `run_ll compare fx-merged` must print the line `fx-merged (shrink-only): gained b.md<TAB>-<TAB>causes` (exact-line `grep -xF`) and exit `rc=1`. After `run_ll_reset` it must print no `gained` and exit `rc=0`.
  - The section header comment now says five registrations.
- `memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-59-1-acceptance-ledger.md` is new, one line per criterion.
- The spec's status header is now CLOSED (rev-4, 2026-11-23). That is the only edit I made to the spec; its records table was re-rendered by the generator.
- `gen_build_index.py --write` rewrote these, all committed: `memory/LIVE.md`, `memory/backlog/TOOL.md`, `memory/builds/dTotalRecall/README.md` and the spec's records region. The build status now reads DEFERRED because no unit is INPROGRESS any more. `memory/builds/dTotalRecall/RUN.md` went in the same commit.
- `gen_map.py --write` changed nothing, since no symbol was added.
- The commit carries `Pass: TOOL-dTotalRecall-59` and `Co-Authored-By: Claude Opus 5`, the charter's trailer, which the brief also names. The pre-commit hooks passed, including the staged hygiene check 23 and codebase-map freshness.

**Checks that ran, standing in for the gates**
- **AC1:** §4's probe, run from `tools/memory-tree/`, printed `True (None, 'no memory/project/record-kinds-legacy.txt at 8b8b1374c4fc (merge-base of HEAD and origin/main)')`. This stands in for `ratchet (never gains)` and `memory hygiene`.
- **AC2:** both `git grep -n absorbs` commands printed nothing and exited 1.
- **AC3:** I built the case's fixture by hand under `%TEMP%/ll59` and removed it afterwards. It used a bare remote, `main` pushed and fetched, and the branch `feature`. `python tools/lib/legacy_ledger.py compare fx-merged`, with `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` unset, printed the exact gained line and exited 1 with the planted row. Reset, it printed no `gained` and exited 0. This stands in for the `python resolver (behaviour + inline parity + idiom ban)` leg's new case.
- **Later `seed --all` cases (lines 1602-1610):** I re-probed in the same fixture to check that `fx-merged` does not disturb them. It reads `unarmed fx-merged no seed` with rc=0, the same as `fx-keys`, so the existing asserts still hold.
- `bash -n` over the edited suite file passed (syntax only, not a run).
- The probe scripts are in the scratchpad: `C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/ac3-probe.sh` and `C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/seedall-probe.sh`.

**Bug-class checklist** (`gotchas.py --for-diff HEAD~1..HEAD`, rc=0; it selected 26 classes plus 6 universal):
- *Fixture passes by finding nothing:* not hit. The case plants a row the base lacks, and the gained/not-gained pair asserts exact lines and exit codes.
- *Ledger token wrapped across a line:* not hit. Each ledger token sits on one line and is spelled in its criterion.
- *Staged break substitutes a synthetic value:* the fixture registration matches the real one's key, fields, verbatim and direction. It keeps `build_ll_table`'s `drain = "none"` and `seed = []` where the real one has `drain = "key"` and a seed argv. That follows §4 as written and is the only gap.
- *Empty field collapses*, *pipe in a code span* and *heredoc escape:* none apply. I made the suite edits with the Edit tool.

**Owed to the main loop at the close**
1. Run the legs on the spec's gates section: `memory hygiene`, `python resolver (behaviour + inline parity + idiom ban)`, `recall floor`, `recall floor arms`, and the four codebase-map legs (`coverage + freshness`, `kit selftest`, `gate coverage`, `adopter e2e`).
2. The `New arm:` RED-first observation for `tools/lib/resolve-python.test.sh` section `2o` case `merged-home-gained`, covering AC3. The staged break, as §7 states it, is committing the planted `b.md - causes` row into the fixture's base so nothing is gained; the case should then read RED and go GREEN once restored.

Nothing was skipped for running past its time bound.
