**Serves:** journal TOOL-dWitnessedBar-20

# TOOL-dWitnessedBar-20 — builder return 1 (run `wf_73e0e22f-ba9`), a divergence, nothing committed

## Why

DIVERGENCE: the spec misses a third caller of `check_legacy_graded`, and the new rule it sets turns that caller's fixture case red. The spec does not say what that case should assert.

The affected parts are §2 S5 (the `check_legacy_graded` sentence and its Readers line), §2 S2 (its Readers by-name sweep), §2 S10 (the README sections it names) and §4 "Reaching the factory".

What the spec says: S5 states that "`check_legacy_graded` keeps its name and both callers, `cmd_lists` and `arm_legacy_homes`". Its rule then becomes: graded where `derive_census_tree` answers `source`, a `legacy-homes` registration is read through `read_registrations` (tracked files only), and that registration's home exists as a file at `repo`.

What the tree holds: there is a third caller, `tools/policy/check_policy.py#run_census_source_receipt` at line 4537, which is the `census-source-receipt` fixture case of TOOL-dSafePassage-103. It calls `policy.check_legacy_graded(t, KIT)` in a scratch repository that holds an untracked copy of gov's registry and a source-mode receipt. It expects `(("source", <tool root>), True)`, which it calls "with the legacy list graded". Today it answers True only because `(KIT / LEGACY_LIST).is_file()` reads gov's own kit directory. Under the S5/§4 rule that scratch tree has no tracked registry, so no registration is found, and it has no `memory/project/legacy-homes.txt`. The call therefore answers False and the case's "source-mode receipt" check prints WRONG on the `policy fixtures` leg.

`tools/policy/README.md` states the same expectation in prose (the `census-source-receipt` paragraph: "`derive_census_tree` must answer `source` at that tool root and `check_legacy_graded` true"). None of the README sections S10 names covers that paragraph.

The S2 sweep (`git grep -n "legacy-homes\|LEGACY_LIST\|LEGACY_HEADER\|legacy_homes"`) cannot match `check_legacy_graded`, which is how the caller was missed.

What the spec has to say: name `run_census_source_receipt` as a caller and reader of `check_legacy_graded` (S5 Readers, and the S2 sweep re-run with `check_legacy_graded` in its pattern). It then has to choose that case's new expectation, which is a design choice I did not make. Either (a) the source-mode answer pairs with `graded` False in a tree that tracks no registration and holds no home, or (b) the case commits the registry and plants the home so `graded` stays True. It also has to add the README's `census-source-receipt` paragraph to S10, plus a criterion or case note that observes the chosen expectation.

Every other claim I probed held. Nothing was written to the repository and no commit was made.

## Summary

Nothing was built or committed for TOOL-dWitnessedBar-20. The spec misses a third caller of `check_legacy_graded`, a fixture case its new rule would turn red, so I stopped before the first product edit (details in `why`). The worktree is clean at base 53cb8c5a249468313804af0664fe3d58828b3337.

**What ran:**
- Read `memory/guides/BUILD-METHOD.md` whole, the spec (memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-20.md, rev-4) and the brief.
- `unattended.sh --brief` answered "brief already recorded, unchanged".
- Read probes of the tree only. None of them stands in for a gate.

**Spec claims checked and holding:**
- The list at the run's base 9e21ac76 matches HEAD's list, key for key.
- `policy.py lists --check` at HEAD is green, with 114 rows derived, which matches the pinned count. (DERIVED from the builder's probe)
- These names exist where the spec says:
  - in the factory: `read_registrations`, `read_ledger`, `write_rows`, `render_header`, `compare_counts`, `compare_to_base`, `run_seed_argv`, `derive_seed_prefix`, and the canonical CLI's `read` verb.
  - in `tools/memory-tree/legacy_ledger.py`: the docstring naming converting kits as callers.
  - in the kits: the policy kit's `requires = ["memory-tree"]`, `load_tree_lib`, `positional.py#read_list_registration` and `merge-rows.py#check_ledger`.
  - in the files the unit touches: the three `ignore_patterns` sites, the landed `LEGACY_CASES` list, `PROJECT_REGISTRY_EXTRA`, the kickoff manifest's `watch:` line (it holds `.memory-tree.conf` and `tools/gate-legs.json`), and `tools/run-gates/leg_factory.py`.
- The memory-tree copy of `legacy_ledger.py` imports on its own beside `coverage_join.py` and `backlog.py` (`python -I` in the scratchpad), so the planned fixture copy can work.
- A guard under `memory/` falls into govkit selfcheck 7c's `memory-root-relative` class, so the new guard needs no `[[exempt]]` row.
- The step gate's `file` class reads only `write` plan rows. The deleted project-owned rule therefore owes no `[[upgrade]]` step, as the spec's Migration says.

**The failing claim:** S5 says `check_legacy_graded` has two callers. There is a third, the `census-source-receipt` fixture case (`tools/policy/check_policy.py#run_census_source_receipt`), and under the new rule it would print WRONG on the `policy fixtures` leg. The policy kit's README states the same expectation in a paragraph no S10 item covers.

**Skipped:** the build itself, `gen_build_index.py --write`, the acceptance ledger, the CLOSED status flip, and `gotchas.py --for-diff HEAD~1..HEAD`, which needs a committed range. No command hit its time bound.

**Owed at the close once the unit is built:** the `New arm:` line's RED-first observation on `tools/policy/check_policy.py` (`--fixture legacy-homes` cases growth, planted-row, shrink, unmarked and drain-merge, covering AC4 to AC7 and AC9), and the §7 leg set.
