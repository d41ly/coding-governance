**Serves:** journal TOOL-dWitnessedBar-15

# TOOL-dWitnessedBar-15 — builder return 1 (run `wf_c651adcf-b6c`), a divergence, nothing committed

## Why

DIVERGENCE: §4 "Files touched" (and S5, which puts `gen_map.py --out` in this unit) cannot be committed as written.

1. The commit needs `memory/map/generated/symbols.json`, and --dispatch refuses it. The pre-commit codebase-map gate failed `test_generated_artifacts_are_fresh` with "STALE symbols.json". The new functions in `tools/lib/legacy_ledger.py` and its two copies make that file stale. `symbols.json` is not on the spec's Files touched list. When I declared it, `unattended.sh --dispatch` refused with check 49: "--dispatch declares a generated index together with its generator", because `tools/codebase-map/gen_map.py`, its generator, is already in this unit's write set (S5 `--out`). The refusal binds this pass. So the spec has to take one of two forms:
   - Move `gen_map.py --out` out of this unit's write set, for example into its own unit, or give S5 a codebase-map seed argv that needs no `gen_map.py` change. This unit can then declare and restage `symbols.json`.
   - Or state another route by which the map is regenerated in this unit's commit.

2. Smaller points for the spec writer to settle in the same revision:
   - (a) S5 runs the adopters' `seed --home` "from memory-tree's copy", but that copy carries no CLI today; its docstring says "The CLI lives on the canonical copy only". Units 17 and 53 read S5 as giving that copy a `seed` CLI. The spec should say so.
   - (b) S2, read literally, says a failed seed leaves "the header and one `# unarmed` line". Under `--widen` over an armed home, that would wipe the rows that §4's widen row says are never removed. The spec should state the widen-failure case. I built it as: write nothing, print `unarmed <p> <reason>; the armed home is unchanged`, exit 1.
   - (c) The exit code of a failed seed is not stated anywhere. I used 1, the CLI's existing convention for a finding.

3. Not a spec defect, but it also blocks any commit here: the hygiene check-catalog row for README regions (`doc.hygiene#the-check-catalog-all-in-tools-memory-tree-check-memory-hygiene-sh-this-file-is-the-prose-home`) failed on `memory/builds/dWitnessedBar/README.md`. Other agents have uncommitted edits to specs 14, 16, 20 and 24, plus untracked prompt files, in this shared worktree. The hook renders from that working tree, and `--write-staged` declined for that reason. Those files were left untouched.

Every path this pass changed is restored to HEAD and nothing was committed. RUN.md stays staged with the driver's dispatch rows, as it was at base plus this pass's declarations.

## Summary

TOOL-dWitnessedBar-15 was built and checked with scratch-fixture probes, then rolled back uncommitted: the commit hook needs a regenerated `symbols.json`, and --dispatch refuses it in this unit (the `why` has the details).

**Saved work.** The full staged diff is in C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/TOOL-dWitnessedBar-15-pass.patch. It holds every path except RUN.md and was confirmed reversible with `git apply --check -R --cached`. The drafted commit message, with its `Decided:` lines and `Pass:` trailer, is in C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/TOOL-dWitnessedBar-15-commit-msg.txt.

**What the patch contains:**
- `tools/lib/legacy_ledger.py`: new functions inside the `legacy_ledger_py` block, copied byte-identically into the memory-tree and gate-lint copies: `seed_population`, `seed_home`, `read_home_state`, `check_home_admitted`, `run_seed_argv`, `read_seed_policy` and `run_seed_cli`. `write_rows` now writes through a new `_write_atomic`. The seed bound is pinned as `SEED_TIMEOUT` (PINNED: its value lives in `tools/lib/legacy_ledger.py#SEED_TIMEOUT`).
- `retrofit.unseeded` is read by calling `policy.py get "retrofit.unseeded"` as a subprocess, with the key as a literal, from the kit `resolve_kit_dir` finds.
- The memory-tree copy gains a seed-only `__main__` and imports `resolve_kit_dir` from `backlog`. The gate-lint copy carries an inline `resolve_kit_dir` block, which I checked against its canonical with `blk`.
- `gen_map.py` gains `--out`.
- Both adopters' absent-only guards now call `seed --home` from memory-tree's copy. codebase-map finds that copy through `map_lib.MEMORY_TREE_DIR`, drift-audit through `drift_report.resolve_kit_dir`.
- Docs: `help/policy.md` gets a `retrofit.unseeded` bullet; the codebase-map and drift-audit READMEs name the seed.
- Ask rows TOOL-dDeclaredLoop-118 (F4 as F7 words it) and TOOL-dDeclaredLoop-119 (F5), with their SEV rows.
- Deviation record 154 and the acceptance ledger, which records AC8 as NOT OBSERVED because those asks have not landed.
- The two `New arm:` arms: section 2o's seed cases in `tools/lib/resolve-python.test.sh`, and arm 7 of `tools/codebase-map/adopt-codebase-map.test.sh`. Both were checked with `bash -n` only.

**Checks that ran (no gate, suite or bar):**
- A probe of the canonical CLI over a scratch git repo under `%TEMP%`, standing in for the resolver suite's 2o seed arm. It observed:
  - AC1: `armed p 2`, rows stamped with HEAD's sha and `seeded`, no stray temp files.
  - AC2: `present p`, the home byte-identical after a third key was planted and committed.
  - AC3: `widened p c`, the new row stamped `widened:R1`, the first rows unchanged.
  - AC4: `unarmed p exit 1` and `unarmed p dead probe`, then `armed p 3` once the seed was repaired.
  - AC5: the home in an untracked directory was not created.
  - AC6: the default printed `unarmed q no seed` and exited 0; a committed `refuse` exited 2 naming q; with no policy kit it fell back to the default with one stderr line; a reader refusal passed its own line through with exit 2.
- An adopter probe over a scratch target, standing in for the `codebase-map adopter e2e`, `drift-audit selftest` and `drift-audit wiring` legs. AC7 held: `present`, the affordance list byte-identical with a planted violation live, and `drift_signals.py` armed then present with a tuned file unchanged.
- Import and parity probes of all three copies, standing in for the parity leg.
- The naming lexicon's `--suggest`.

**Owed at the close once this is re-dispatched:**
- RED-first observation of both `New arm:` lines.
- Every leg in §7.
- `gotchas.py --for-diff` was never run, because there was no commit to run it over.

**Known red until TOOL-dWitnessedBar-47 lands:** the tracked-file home test makes a fresh adopt of codebase-map and drift-audit print `unarmed` and stop. That will red arm 6 of `adopt-codebase-map.test.sh`, and any fresh drift-audit adopt, until unit 47 replaces the test.

Nothing was skipped for a timeout. The scratch fixtures `%TEMP%/ll15`, `%TEMP%/ad15` and `%TEMP%/gb15` were removed.
