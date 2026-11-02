**Serves:** research TOOL-dScopedBuild-39

# Fix brief — dScopedBuild, the round-2 promotions' one hygiene red

The round-2 spec audit's disposal promoted TOOL-dScopedBuild-36 to -39, uncommitted. Hygiene check 12 refuses the
commit on one item: `memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-39.md` §2 S28 names neither an
acceptance criterion nor `NOT OBSERVED`, which every scope item owes at or after `SCOPE_JOIN_CUTOFF` 2026-09-08
(`memory/TEMPLATE-SPEC.md`). Name the §6 criterion that observes S28, adding one if none does, with a planted case a
pass can run; or, only where no observation is possible, write `NOT OBSERVED` and the reason. Change nothing else. The
spec has never been committed, so it stays at `rev-1` and owes no §9 line.

Return the change, then rerun `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and report its verdict on
that file. Write nothing outside `memory/builds/dScopedBuild/spec/`, commit nothing, run no generator.
