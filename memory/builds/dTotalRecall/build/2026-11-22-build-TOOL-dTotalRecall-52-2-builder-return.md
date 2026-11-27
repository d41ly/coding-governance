**Serves:** journal TOOL-dTotalRecall-52
**Caused-by:** TOOL-dTotalRecall-52

# TOOL-dTotalRecall-52 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `7d07249b5` from [2026-11-23-prompt-TOOL-dTotalRecall-52-build-2-brief](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-52-build-2-brief.md), recorded whole; the pass tip is `926526b1c`.

## Why

Spec rev-7 can be built as written. Rev-7 changes only AC3's pathspec, which now also spares memory/project/record-kinds-legacy.txt (§8 F3). That resolves pass 1's conflict between AC3 and AC5. I re-applied pass 1's draft unchanged with `git apply --index` and re-checked every criterion at this tip. All five acceptance criteria and S1's owed `--seed-legacy` observation came out green.

## Summary

Unit TOOL-dTotalRecall-52 is built and committed at 926526b1c on top of base 7d07249b5. The commit subject names the unit. The final trailer block carries Pass: TOOL-dTotalRecall-52 beside `Co-Authored-By: Claude Opus 5`. I used the charter's spelling because AGENTS.md outranks the harness reminder's "Opus 5.5". The spec status header moved from INPROGRESS to CLOSED in the same commit.

What the commit changes:
- **Registry** (C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/govkit/registry.toml): the `record-kinds-legacy` table is keyed `path`, `section`, `check` with `verbatim = ["section"]`. The `legacy-records` table is gone, and the `record causes` leg's `why` now names the merged population's `causes` slice.
- **Homes:** memory/project/legacy-records.txt is deleted. memory/project/record-kinds-legacy.txt holds 67624 `causes` rows and 11135 `kind-schema` rows.
- **Conf:** the old home's `PROJECT_REGISTRY_EXTRA` entry and its comment are gone from .memory-tree.conf.
- **record_causes.py:** `POPULATION` is `record-kinds-legacy`. `read_legacy_paths` reads only the `causes` slice. `--measure` prints `check` as the third field. The fixture's table uses the three key fields.
- **record_kinds.py:** `read_legacy_keys` returns the `kind-schema` slice as (path, section) pairs. `--seed-legacy` prints both slices. The fixture writes its table and home with the three key fields.
- **Docs and test:** the memory-tree README and the `--plant none` assertion in check-memory-hygiene.test.sh name the merged population.
- **Records:** I wrote memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-52-2-acceptance-ledger.md. I re-stamped memory/guides/SESSION-KICKOFF.md's last-audit because .memory-tree.conf is on its watch list. I ran gen_build_index.py --write and committed what it rewrote: LIVE.md, backlog/TOOL.md, the build README and the spec's generated records region. RUN.md is in the commit too.
- **Not touched:** no function or constant was minted, so VERB_OFFENDER_PIN and symbols.json needed no change.

Checks run (unit probes only; no gate, suite or bar ran):
- **AC1 probe:** printed `('path','section','check') ('section',) 78759 [] ['causes','kind-schema']`. It stands in for the duplicate-key read of `memory hygiene` and `govkit selftest`.
- **AC2 probe (unit 62's §4):** printed True for `check_new_at_base`, and `compare_to_base` returned no findings, naming the home absent at 8b8b1374c4fc. The `git grep absorbs` over the registry printed nothing. It stands in for `ratchet (never gains)`.
- **AC3 grep:** printed nothing in both the worktree and the index, and `git ls-files memory/project` lists no legacy-records.txt. It stands in for `memory hygiene`.
- **AC4 probe:** 10796 record rows plus 56828 section rows equal the 67624 `causes` rows, and the 11135 keys equal the `kind-schema` rows. `record_causes.py --fixture --plant none` printed the exact line AC4 requires. It stands in for the check-memory-hygiene.test.sh assertion.
- **AC5:** a `tomllib` probe found one registration and no `legacy-records` table. The home's rows per slice equal both base homes' row counts at 7d07249b5, and the row sets are identical with `check` inserted third.
- **S1 `--seed-legacy`:** every row printed with four TAB fields, `check` third. The seed does not match the folded home row for row, which is expected: the home keeps the 139 widened comment-headed rows, and the seed adds records written after the base seed.
- **Fixtures:** `record_kinds.py --fixture` (default, `field-missing-legacy` and `value-ledger` plants) and `record_causes.py --fixture --plant legacy` all came back green.
- **Bug-class checklist:** I ran `gotchas.py --for-diff HEAD~1..HEAD` after the commit. Acting on it, I swept readers of the new spelling and of the retired name: no stale two-field row-shape docs and no assertions on the fixture's row lines. Adopters are unaffected because the population is gov-only.

Owed to the close: the §7 gates (`kit/dogfood doc parity`, `recall floor`, `recall floor arms`, `transition-audit arms`, `straggler-guard arms`, `memory hygiene`, `lexicon naming predicates`, `shell-hygiene selftest`, `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`, `policy fixtures`). Also owed are the live `record-kinds` and `record causes` legs over the tree, and `leg_factory --check`. §7 declares no new arm, so no RED-first observation is owed.

No command was skipped and no deviation record was needed. The pre-commit hook passed.
