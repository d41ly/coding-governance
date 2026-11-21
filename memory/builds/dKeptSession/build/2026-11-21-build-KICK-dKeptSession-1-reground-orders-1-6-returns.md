**Serves:** research KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60

# Returns — dKeptSession build run: build orders 1 to 6 re-grounded on the run's tree

Four gov-spec-writer agents, one per brief under `prompts/` named `2026-11-21-prompt-KICK-dKeptSession-<lead>-orders-<orders>-reground-brief`,
re-grounded the sixteen specs of build orders 1 to 6 on the tree at the run's BASE `c2a407b0`, concurrently, each over a
disjoint spec set. The main loop relayed each writer's `interface-changes` to the writer whose spec they touched while it
ran, and resumed a returned writer where a later return moved its spec.

## The revs reached

- Orders 1 to 2: spec 1 rev-5, spec 19 rev-2, spec 33 rev-3.
- Orders 3 to 4: specs 2, 3, 34, 40 rev-3.
- Order 5: specs 4, 49, 50, 54 rev-3.
- Order 6: spec 20 rev-5, 32 rev-3, 58 rev-5, folded twice after the others (spec 34 now carries its compare; spec 54's old text is void), 59 rev-4, 60 rev-3.

## Rulings the main loop took on the returns

- Spec 1's fork F5 (who builds the `guard.py --expansion` verb the owner ruled on 2026-11-05) is accepted at its pick (a):
  the owner's ruling fixed the verb, its grammar, its exit and the subprocess, and expected it from dDeclaredLoop through
  an ask; dDeclaredLoop landed at `9e21ac76` without it, and option (b) leaves four of unit 1's criteria waiting on a run
  no plan schedules. The pick moves only who builds it, into `tools/loop/guard.py` under this run's declared writes.
- Units 34, 54 and 58 overlapped on the derived cap's compare; spec 34 rev-3 builds it, 54 and 58 observe it.
- Unit 4 lands `render_scaffold(rows, preset=None)` with a default at order 5, and unit 32 removes the default at order 6
  once unit 4 has given the two bare callers `--preset standard`; the five `check_policy.py` calls pass `"standard"` in 32.

## Carried to later waves' re-ground briefs

- 44: S41 only extracts check_preset_pairs behind presets.py pairs (unit 20 adds the verb at order 6); AC36 holds. S12's docstring/README lines now in spec 2's S2.
- 56: S28 reduces to observing unit 32's S5/AC4 (five check_policy.py calls pass "standard"). S29, S42 for unit 40 now spec 40's S3. S25's legs for units 34, 40 now named in those specs. S38 cites spec 34 AC2 (exists).
- 63: S10 already in place (unit 60 AC1 reads the joined paragraph).
- 4: render_scaffold(rows, preset) no default (spec 32); bare callers govkit/selftest.py#check_fanout_step, govkit/steps/kickoff_facts_to_overlay.py#build_fact_fixture — sent to W3 writer.
- 54: spec 34 rev-3 carries 54's S1-S4 — sent to W3 writer.
- 58: spec 34 rev-3 carries 58's S1-S2 — sent back to W4 writer (resumed).
- 32: spec 3's verb opens "- preset — <name>", new --section form; "- no key differs" unchanged, 32 AC2 holds.
- 58 rev-4: S1,S2 now observations of unit 34's preset-derived-cap; S3 supersedes 54's 'same row' text (answered in unit 54's ledger); Files touched none.
- 44 S1/AC1: unit 1 now prints the not-graded line itself (`presets-core-only · not graded · TOOL-dDeclaredLoop-2 S8 admits after-release-verifies`); S1 shrinks to observation.
- 56 S41: met by 33 S1 (its policy.py:132 cite stale). 56 S25: met by 33's Gates line.
- unit 1 factory: `python {prefix}/loop/factories.py preset`, plants preset-new, preset-from-unknown (replace presets.py new / presets-factory case).
- 12: ask KICK-dKeptSession-66 — S3 observes the always-resume switch TOOL-dPlacedRequest-2 S7 built, by its line; builds no second. Fold at 12's re-ground (rev bump + §9 line); closes 66.
- F5 of spec 1 accepted (unit 1 builds guard.py --expansion in tools/loop/guard.py): Decided trailer on the spec commit.
- 62 S1: the restated cases' arm for unit 54 is unit 34's now; 54 carries no arm.
- 44 S13: still owns the written branch; unit 4 adds an exit-2 refusal (no policy file and no --preset) and passes its kept branch's exit through.
- 56 S38: stands; 54 AC1 still observes preset-every-key.
- 63 S19/AC19 and its consumes-from 58 edge: void (58 rev-5 S3 is its own ledger answer; 54 answers by the case output of KICK-dKeptSession-34) — re-point or drop.
