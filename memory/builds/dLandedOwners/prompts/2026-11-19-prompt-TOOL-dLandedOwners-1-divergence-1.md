# Revision — dLandedOwners: TOOL-dLandedOwners-1 diverged at its first build pass

**Serves:** research TOOL-dLandedOwners-1

## The prompt

> Fix the Ask 5, remove the ask TOOL-dTrackedAtlas-19

The owner's go for this build, of 2026-11-19; this record carries the builder's divergence back to the spec writer, its Goal the builder's `why` verbatim.

## The brief

### Goal
DIVERGENCE: two places where the spec cannot be built as written. Both have to be revised before this unit is dispatched again.

(1) §4 "The fixture case" contradicts AC4 and §7. Its third bullet says to copy "every *.py of the resolved memory-tree kit" beside the kit copy. That copy runs inside run_fixture's process, where the audit hook (check_policy.py#add_source_read) records every source file it opens. check_policy.py#check_guard_trace then prints a `policy-fixture: guard-trace · WRONG <path> · not under the policy fixtures guard` line for each recorded read that trips no `policy fixtures` guard. I checked the seven files below with `python tools/check-spec-tokens.py --legs-for -`, and none of them trips that guard:
- tools/memory-tree/check-arms.py
- tools/memory-tree/commit_trailers.py
- tools/memory-tree/coverage_join.py
- tools/memory-tree/import_walk.py
- tools/memory-tree/merge-rows.py
- tools/memory-tree/migrate_backlog.py
- tools/memory-tree/transition_audit.py

tools/memory-tree/tree_lib.py, by contrast, trips it. So every `--fixture` run, AC4's single-case run included, would print seven WRONG lines. AC4 ("No line holds WRONG") would fail, and so would the `policy fixtures` leg. Fixing it means one of two spec changes:
- (a) Copy only the import closure that half 2 needs. That is tree_lib.py, gen_build_index.py, backlog.py, design_lib.py, row_grammar.py and id_grammar.py, which gen_build_index and row_grammar import lazily. All six are already in the guard.
- (b) Add the seven paths to the `policy fixtures` guard in tools/gate-legs.json. The spec would then have to add that file to Files touched.

(2) §4 "Files touched (estimate)" lists only tools/policy/check_policy.py, tools/policy/README.md and help/policy.md. It leaves out the acceptance ledger, memory/builds/dLandedOwners/build/2026-11-19-build-TOOL-dLandedOwners-1-ledger.md. Closing this spec needs that ledger: memory/HYGIENE.md "Acceptance ledger" grades every criterion a closed spec numbers. The brief says the spec's Files touched names a ledger, and it does not. The prior dTrackedAtlas unit specs (9, 12) list theirs.

Three smaller points the spec writer should settle in the same revision:
- AC4 says the run "prints five policy-fixture: lines". run_fixture always adds the guard-trace lines and the count line, so it should say five sub-case lines.
- In §4, `base-unresolved` says "both run records", but each planted repository holds one RUN.md. It should say which two it means.
- The brief tells the builder to "leave the spec's status flip to the main loop", while this dispatch says to set CLOSED. That contradiction is the brief's, not the spec's.

### Items
1. `derive_landed_owners` in `tools/policy/check_policy.py` reads a build run that landed with a unit carried forward, DEFERRED against an ask, as landed, by the predicate the schedule's derivation took (its spec's fork F1, option g: a build-kind run record with a first-parent landing merge on the default branch), in a form a shipped kit can hold [planned TOOL-dLandedOwners-1]
2. The reader scan (`READER_SHAPES`, `scan_reader_keys`) reads a key passed to a reader call through a module-level constant, the shape the loop kit uses for seven dDeclaredLoop keys [planned TOOL-dLandedOwners-2]
3. A key whose only reader sits outside the scanned code, `deviation.approval`, read by a dClosedLoop instrument under the memory root, takes a declared disposition with its reason, never a silent pass [planned TOOL-dLandedOwners-3]
4. Ask TOOL-dTrackedAtlas-19 withdrawn on the owner's word [stale landed at `51971579a` before this build opened]

### Acceptance
At the build's tip, `derive_landed_owners` names dDeclaredLoop, dSafePassage, dFairHearing and dTrueNorth among the landed owners; reader coverage grades the keys of every landed owner and reports no finding; each new arm is observed red before green; the merge bar is green.

### Gates
The merge bar, `bash tools/run-gates/run-gates.sh`, once after the last unit; per unit, the direct check its spec names. The policy kit's own self-test arms are the owner's flagged bar, waived for this build as for dTrackedAtlas.

### Non-goals
Any other policy key; the loop kit's code, beyond what a reader shape needs to see; the chain builds' specs; the flagged bar.
