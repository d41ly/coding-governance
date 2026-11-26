**Serves:** journal TOOL-dTotalRecall-5

# TOOL-dTotalRecall-5 fourth build pass — the builder's return

The gov-builder return for the fourth pass, dispatched at `e571543c8` from [2026-11-22-prompt-TOOL-dTotalRecall-5-build-brief-4](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-5-build-brief-4.md), recorded whole.

## Why

I built TOOL-dTotalRecall-5 from spec rev-11 in two commits, both carrying `Pass: TOOL-dTotalRecall-5`. The pass commit is 202a354a4. It holds the code, the spec header set to CLOSED, the deviation record 52, the acceptance ledger, the re-stamped kickoff manifest and the regenerated indexes. The follow-up commit e556566b4 fixes two problems the bug-class checklist found in the pass commit. Before writing anything I re-ran the spec's searches at the base and they matched what it pins: the reader census gave 73 lines in 37 files, and the two fixture searches gave 793 lines in 53 files. No spec claim I checked was wrong, so there is no divergence to report.

## Summary

**What was built (202a354a4)**
- `tools/memory-tree/id_grammar.py` now derives the slug grammar once from the three `builds.slug-*` policy keys and exports it.
  - New names: `derive_slug_grammar`, `SlugGrammar` (with `render_label`), `SLUG_DEFAULTS`, `parse_slug_grammar`, `render_slug_shape`, `scan_readers`, `run_flip_probe`.
  - New CLI modes: `--print`, `--readers` and `--flip-probe`.
  - Readers bind the grammar at first use, through `SlugPattern`.
- The session era, `Conf.digest`, the tree_lib id token and its range form, and drift-audit's local copy now use the grammar's slug class.
- Both new-build doors check the new slug against the grammar in force and write a `slug-grammar:` line. The LIVE page and the ledger shards label a build through `render_label`.
- The hygiene script gains `--print-slug-re` and `--print-slug-class`. Check 4 reads the derived pattern. A set `BUILD_SLUG_RE` now refuses with exit 2, naming the three keys.
- Every reader `--readers` found was re-pointed: the Python ones through each kit's resolver, the shell ones through the print modes, the JavaScript ones through a new `{{SLUG_CLASS}}` template token.
- The kits that do not require memory-tree carry an inline copy of the legacy slug shape, held identical to the canonical by two new `PARITY_ROWS` rows:
  - runlog and branch-reconcile carry `slug_legacy_py`, next to a new copy of the `resolve_kit_dir` block.
  - run-gates, push-main and the workflows renderer carry `slug_legacy_sh`.
- runlog, branch-reconcile, run-gates and workflows each gained a `requires_if` row for memory-tree.
- The three policy keys gained their summary, usage and help-page sections.
- One script rewrote 1463 fixture-slug occurrences across the 26 files the spec marks for re-spelling; I also rewrote the runlog names table (DERIVED, the builder's script output at `202a354a4`).
- Things I added that the spec did not state are in deviation 52: the helper functions, push-main's legacy fallback, and moving `zAB` to `zAFixB` so the doctor arm still tests prefix matching.

**The follow-up (e556566b4)** fixes the two checklist findings:
- `_eras` lost a dead branch that spelled the legacy shape a second time.
- `load_slug_class` in `lib-unattended.sh` now falls back to the module's own print mode when the hygiene script is absent.
- Two suite fixtures that install a grammar reader without memory-tree now carry it: push-main's fence fixture and the roles adopter's fixture.

**What I checked.** No gate, suite or bar ran. I probed each criterion directly in the worktree, in scratch clones under %TEMP%, and in one fixture shaped like the hygiene suite's base tree:
- AC1–AC15 each held on the probe the acceptance ledger records for it.
- AC10: `--flip-probe` printed `ok` for all six flips and exited 0.
- AC12: `read_bindings` read the same ids at the base and the tip: 10583 records, 3062 distinct ids (DERIVED, `read_bindings` at `e571543c8` and `202a354a4`).
- AC13: in a master-pinned repository the defaults applied with exactly one policy read and nothing on stderr. In the hygiene-shaped fixture, a planted `d_bad` folder failed check 4 with the fallback line printed once after it.
- AC15: runlog's slug pattern answered `True True False False` for `myBuild`, `aFix`, `my-build`, `a`, and after the rewrite the two searches find only the hits the spec's table keeps.
- I also probed the naming lexicon (`lexicon.py --measure`) and the block parity rows. The probes stand in for these gates and suites: build-index selftest, memory-hygiene self-test, the unattended kit gate, push-main self-test, roles adopter self-test, drift-audit selftest, the python resolver parity rows, kit placeholders, docs and policy check.

**Owed at the close**
- Every gate in §7.
- The four `New arm:` RED-first observations: `tools/lib/resolve-python.test.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`, `tools/drift-audit/selftest.py`, and the `gen_build_index.py --selftest` arms.
- AC10's red case: put the old session era back and both `in-slug` flips should fail.
- The policy mirror, `.governance/policy.json`: `policy.py mirror --write` refuses until the catalogue is committed, so it has to run after this commit.
- No kit version was bumped, following unit 16's precedent. The `kit epoch` leg will judge that.

**Risks for the close to measure**
- Every driver verb that checks a slug now starts the hygiene script, which reads three policy keys. That is roughly a second per invocation, so suite time budgets may be exceeded.
- A suite fixture that installs a grammar reader without memory-tree will fail. I fixed the two I found; others may remain.

Nothing timed out or was skipped. Every scratch clone and fixture was removed. Detail is in:
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-5-4-acceptance-ledger.md
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-5-deviation-52.md

## Next action


