**Serves:** journal TOOL-dWitnessedBar-18

# TOOL-dWitnessedBar-18 — builder return 1 (run `wf_3c2664c5-1ae`), a divergence, nothing committed

## Why

DIVERGENCE: the spec's `landed-steps` population (S3, S4, §4 "The populations" and Migration, AC1, AC5, §7, §8 F6) is graded by `ratchet (both ways)` against a seed whose output depends on `origin/main`, which moves outside the commit being graded. Under the spec as written, the act AC5 calls green reds a leg on §7's own line, and the population goes red the moment the build lands.

Evidence from the tree at 03b75c054:
(1) `tools/memory-tree/ratchet.py#run_both_ways` runs the seed of each registration naming that leg and compares counts through `LL.compare_counts`. Under `append-only`, a declared row the seed does not print is an `unmeasured row` (red), and a measured key with no row is an `undeclared site` (red).
(2) The seed has to print landed ids only. S3 says "one row per landed step id", §4 pins "landed steps 5 of 16 step rows against the landed ref origin/main", and AC1 requires the row count to equal the seed's line count. `upgrade_steps.py#cmd_list` derives landed through `resolve_landed_ref` (the remote ladder, `origin/main`). `python tools/govkit/upgrade_steps.py list` at HEAD prints 24 step rows, 5 landed and 19 unlanded (rows 6-24, unit 16/17's `*-to-ledger` steps).
(3) So AC5's "adding a new step row and its ledger row exits 0" holds for `never-gains` but reds `both-ways`: the new step is unlanded, so its row is an `unmeasured row`. Leaving the row out is the only way to keep the bar green at the close.
(4) After the build is pushed, `origin/main` holds the 19 unlanded steps plus this unit's own new `playbook-render/positional-refs-to-ledger` step. The seed then prints 25 ids against a ledger of 5, written at the run's base per Migration. AC1 "on the landed tree" fails, and `ratchet (both ways)` is red on main until someone appends the rows. No unit owns that append. The next build that adds a step meets the same trap again: its ledger row reds the bar before landing, and leaving it out reds the bar after landing.

What the spec has to say instead, for the spec-writer to choose:
(a) The seed prints every declared step id (`read_steps(root, None, None)`), not only landed ones. The population becomes "every step row ever declared" (append-only), with AC1/AC5/§4 re-pinned to that. Or
(b) The seed compares against a ref inside the graded commit rather than `origin/main`. Or
(c) `landed-steps` names no both-ways seed, and §8 F6 is re-resolved.
Each one changes §8 F6 and AC5, so it is a fork for the spec-writer, not a builder's choice.

Secondary findings for the same rev:
- §4 pins "16 step rows". HEAD has 24, so the pin is stale.
- Files touched omits `tools/memory-tree/ratchet.py`. §7's `New arm:` line puts an `append-removed` plant in `ratchet selftest`, and no such plant exists today (`run_plant_append_edited` is the nearest).

Every other cited symbol, path and figure I probed holds at HEAD:
- positional.py, writing_practice.py, instruction_units.py, render_playbook.py `write_empty_lists`, gov_tag.py `run_plant` and `--list-positional`, `upgrade_steps.py#main`, `read_steps` and `check_frozen`, and `convert_registry.py` `LEGACY`, `parse_keyed_reason` and `derive_registration`.
- The registry entry `playbook-render` maps to `{prefix}/playbook/kit.toml`.
- List row counts are 38334, 15, 15216 and 33. No duplicate rows, and no line-number-shaped field outside `ref`.

No path was written and nothing was committed. `--brief` reported the brief already recorded and unchanged.

## Summary

I stopped before writing any code: one design defect in the spec blocks TOOL-dWitnessedBar-18, so nothing is committed. The full divergence is in `why`.

The problem is the `landed-steps` population. Its seed counts only steps already on `origin/main`, and `ratchet (both ways)` compares the ledger against that seed. So adding a step row together with its ledger row (green under AC5) turns `ratchet (both ways)` red, and leaving the row out turns it red once the build lands. At HEAD that means 19 steps plus this unit's own new step. `upgrade_steps.py list` shows 24 step rows, 5 of them landed.

Checks that ran (all read-only):
- `git rev-parse HEAD`, which gave the base 03b75c054.
- `unattended.sh --brief`, which reported the brief already recorded and unchanged.
- Each symbol, path and line the spec cites, looked up in the source.
- Row counts, field shapes and duplicate checks on the four list files, using the spec's own `grep`/`cut` forms.
- `python tools/govkit/upgrade_steps.py list` at HEAD.
- A read of `ratchet.py#run_both_ways` and `#run_never_gains`, and of `legacy_ledger.py#compare_counts` and `#compare_to_base`.

These probes stand in for `ratchet (both ways)` and `ratchet (never gains)`. No gate, suite or bar ran.

Not run here, owed at the close once the spec is revised and the unit rebuilt:
- AC1 to AC7.
- The `New arm:` `append-removed` plant in `ratchet selftest`: its red-first, then green observation is owed.

The gotchas checklist (`gotchas.py --for-diff`) did not run because there is no commit to check. The working tree is clean at 03b75c054.
