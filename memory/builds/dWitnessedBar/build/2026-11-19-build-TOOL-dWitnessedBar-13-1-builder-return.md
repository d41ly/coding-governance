**Serves:** journal TOOL-dWitnessedBar-13

# TOOL-dWitnessedBar-13 — builder return 1 (run `wf_62b9efd5-0fc`), a divergence, nothing committed

## Why

DIVERGENCE: I checked rev-3 of memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-13.md against the tree at 5e569d9c9 before writing anything. It can't be built as written. The spec writer needs to settle the points below; I've listed them all here so one revision covers them.

(1) S10, AC2, AC4 and section 4's function table: `compare <population>` has no measurement source. AC2 needs "a site measured that no row declares" and AC4 needs "no drain". But `compare_counts(measured, declared, direction)` takes `measured` as input, and nothing in the spec says where the CLI gets it. The only candidate is running the registration's `seed` argv. How that argv runs is designed by other units:
- TOOL-dWitnessedBar-15 section 4: the stdout row grammar, the 600 s bound (PINNED, unit 15 section 4), `dead probe:` liveness.
- TOOL-dWitnessedBar-51 S32: head `python`/`python3` runs as sys.executable, head `bash` runs through resolve_bash_py, `{prefix}`/`{kit}` resolve via tools/run-gates/regen.py#resolve_argv, and the cwd is the repo root.
Building it here would design what those units own, or build a weaker version that they then re-specify. Section 4 needs to name the source: either `compare` runs `seed` through a named function whose contract is stated or shared with unit 15, or it reads measured rows from a named input.

(2) AC1 contradicts S10 and AC9. AC1 runs `python legacy_ledger.py read <fixture>` "from tools/lib/ over a fixture repo". S10 says `read|compare|carry <population>`, run in the repository the CLI is invoked from, and AC9 uses `read <population>`. AC1 has to use one of the two forms, for example `read <population>` with the cwd set to the fixture.

(3) Section 4, "The registration": `read_registrations(root)` reads "every tracked kit.toml under the tool root" and `<tool root>/govkit/registry.toml`, but nothing says how the tool root is found at a root other than gov's own checkout. That covers the AC1/AC9 fixtures and every adopter. tools/govkit/govkit.py#derive_tool_root keys on a govkit registry, which section 4 says no copy-installed adopter tracks. The derivation needs naming, for example the parent of each tracked `<dir>/<kit>/kit.toml`, refusing on two.

(4) Section 4's `compare_to_base` row cannot meet AC4 as written. After `carry`, the working rows use the new path and the base rows the old one. Under `shrink-only` that is "a key the base lacks", so it prints `gained`. AC4 forbids that. The row must say base rows are re-keyed through the `<base>..HEAD` renames before the direction is judged. S5 implies this but the function table doesn't state it.

(5) Section 5 conflicts with section 4. Section 5 says `write_rows` writes "only a registration's declared home after the hygiene admission test". Section 4 says whether a home is admitted is TOOL-dWitnessedBar-15's seed-time test. The `carry` verb writes rows (AC4: "its rows move to the new path"), so the spec must say whether `carry`/`write_rows` runs that test in this unit, and how.

(6) Section 4, "The merge class", says the other three postconditions "run unchanged". tools/memory-tree/merge-rows.py#no_row_loss and #structure_identity split rows from other lines with `_ROW_RE`. Run unchanged, every TSV row counts as structure, so `no_row_loss` raises RowLoss on every ledger merge. AC5 and AC6 can't pass that way. It should say these postconditions run with the ledger row predicate and key, as the bullet above it does for the row plane.

Every other claim I probed matches the tree:
- tools/lib/coverage_join.py#compute_coverage and tools/lib/compare_base.py#resolve_compare_base exist.
- memory-tree's coverage_join.py carries the coverage_join, remote_ladder_py and compare_base_py blocks.
- In merge-rows.py, merge() handles check_manifest first, then the view/shard refusal, then check_build_backlog with `ids=`.
- The PARITY_ROWS copy grep would find a gate-lint copy by its marker.
- 2n is the last part-2 section, so 2o is free.
- The sh_hygiene and encoding_posture read_registry/check_registry functions are as cited.
- merge-rows.test.sh has the "disjoint appends" case.
- tools/check-wiring.sh#check_merge_rows exists.

No path was changed and nothing was committed. memory/builds/dWitnessedBar/RUN.md was already staged by the main loop's --dispatch. The four untracked prompt files belong to other units, and I left them alone.

## Summary

I built nothing and committed nothing for TOOL-dWitnessedBar-13: the spec can't be built as written, and the `why` field lists six problems for the spec writer to fix in one revision.

The main one is that the `compare` command has no defined way to get the counts it compares against. The only candidate is running the registration's `seed` command, and how that runs is designed by TOOL-dWitnessedBar-15 and TOOL-dWitnessedBar-51 S32. I'd have to design their part to build it here. The other five:
- AC1 says the command runs from tools/lib/ with a fixture argument, but S10 and AC9 say it takes a population name and runs in the repo it is called from.
- The spec doesn't say how `read_registrations` finds the tool root in a fixture or an adopter repo that has no govkit registry.
- As specified, `compare_to_base` would report a renamed file's rows as `gained`, which AC4 forbids.
- Section 5 has `write_rows` checking whether the home is admitted, but section 4 gives that check to unit 15.
- Run "unchanged", the merge driver's `no_row_loss` check would refuse every ledger merge, because it only recognises bullet lines as rows.

**What ran:**
- `git rev-parse HEAD` returned 5e569d9c90a0d207c3200daf4df1f893750ab4bb; this is `base`.
- `unattended.sh --brief` said the brief was already recorded and unchanged at 183b97abe5c6.
- I read the build method, the brief and the spec whole.
- I checked each claim the spec makes about current code against these files:
  - tools/lib/coverage_join.py
  - tools/lib/compare_base.py
  - tools/lib/resolve_remote.py
  - tools/memory-tree/coverage_join.py
  - tools/memory-tree/merge-rows.py (the row plane, the postconditions and merge())
  - tools/lib/resolve-python.test.sh (the parity table, the `blk` extractor and sections 2j to 2n)
  - tools/gate-lint/sh_hygiene.py and tools/gate-lint/encoding_posture.py (the registry code)
  - tools/gate-lint/kit.toml and tools/govkit/govkit.py (derive_tool_root, load_registry)
  - the TOOL-dWitnessedBar-15 and TOOL-dWitnessedBar-51 specs, for the seed-run contract

**What didn't run:** no fixture or probe of new code ran, because I wrote none, so none stands in for any gate. No gate, suite or bar ran. Nothing was committed, so `gotchas.py --for-diff` had no commit to read and didn't run. Nothing timed out or was skipped.

**Still owed at the close, once a revised spec is built:** RED-first observation of the spec's two new arms: tools/lib/resolve-python.test.sh (the `legacy_ledger_py` parity row and section 2o; AC1-4, AC7, AC9, AC10) and tools/memory-tree/merge-rows.test.sh (the ledger cases; AC5, AC6). Plus the legs section 7 lists: shell-hygiene selftest, the two scanner legs, the python resolver, the row-keyed merge driver replay, the row-driver view refusal, the check-wiring self-test and memory hygiene.

**Tree state:** unchanged. RUN.md was already staged by the main loop's `--dispatch`, and the four untracked prompt files belong to TOOL-dWitnessedBar-11 and -14. The spec stays INPROGRESS.
