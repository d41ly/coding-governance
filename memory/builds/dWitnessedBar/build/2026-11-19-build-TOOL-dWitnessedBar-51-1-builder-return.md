**Serves:** journal TOOL-dWitnessedBar-51

# TOOL-dWitnessedBar-51 — builder return 1 (run `wf_b331e924-d60`), a divergence, nothing committed

## Why

DIVERGENCE: rev-6 of memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-51.md cannot be built as written. Every failed check is listed here in one report.

(1) §2 S21 and §6 AC17 contradict each other. S21 says `drift_report.py#read_gate_health` takes the bar's legs through `tools/run-gates/held_halves.py#test_held`. That function is `subject == "kit" or chunk == "selftests"` and reads only the manifest row. AC17 needs a fixture manifest with "one leg held by `quarantine` and one by `kit`" where "neither is a bar leg". No manifest row can carry a quarantine hold. None of the 18 keys across the 219 rows of tools/gate-legs.json does. A quarantine hold comes only from the selection that `verdict_flow.py select` derives from the asks at R (`derive_quarantine_rows`, `SELECT_SOURCES`), which `run-gates.sh#derive_hold_source` reads through `GATE_SELECTION`. So with S21 as written, the quarantine-held leg stays a bar leg and AC17 is red. Making AC17 hold means reading the quarantine source as well, which S21 does not say. S21 also says drift-audit cannot import run-gates, and verdict_flow lives there. One of the two has to change. Either S21 names the quarantine source and how drift-audit reads it, or AC17's fixture drops the quarantine leg, or AC17 says a quarantine-held leg stays in the bar. (DERIVED from the builder's probe)

(2) §4 "Files touched" does not cover S1's widen records. `ratchet.py#run_widen` writes through `build_records.write_record`, which names each file `<day>-build-<unit>-widen-<n>.md` after the `--unit` it is given. S1 says "one record per growing unit, its Caused-by that unit". The pass commits after fe49c7d2a that touched the 20 grown files and the new one (`git log --format=%(trailers:key=Pass)`) belong to units 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 25, 29, 30, 40, 41, 42 and 43, plus 51. So the records would be `...-build-TOOL-dWitnessedBar-<u>-widen-1.md` for each of those units, while Files touched only allows `...-TOOL-dWitnessedBar-51-widen-<n>.md`. Each record serves a CLOSED unit, so `gen_build_index.py --write`, which the brief requires, would rewrite the `gen:spec-records` region of each of those CLOSED specs. None of them is in Files touched, and the method keeps a CLOSED spec frozen. The spec has to either list those paths and state that the regeneration is allowed, or say which unit the records are filed under.

(3) Files touched leaves out the kickoff manifest re-stamp. The change edits paths on `memory/guides/SESSION-KICKOFF.md`'s `watch:` list: check-memory-hygiene.sh, run-gates.sh, run-selftests.sh and .memory-tree.conf. `memory/guides/SESSION-KICKOFF.md` is in neither Files touched nor this dispatch, while earlier units' dispatches carried it.

Separately, for the main loop: the `--dispatch` write set dropped four paths that §4 Files touched does list: `.gitattributes`, `AGENTS.md`, `WIRE-INTO-PROJECT.md` and `.memory-tree.conf`.

Nothing was written. `--brief` reported "already recorded, unchanged". The tree is exactly as it was at the base: the pre-existing help/ edits and the staged RUN.md were already there.

## Summary

I committed nothing. The spec for TOOL-dWitnessedBar-51 (rev-6) can't be built as written. There are three problems, and the spec writer needs to fix them before this unit is dispatched again.

1. **S21 and AC17 can't both hold.** S21 says the gate-health measurement picks the bar's legs using `held_halves.py#test_held`, which only checks two manifest fields (`subject` is `kit` or `chunk` is `selftests`). AC17 wants a leg held by quarantine to drop out of the bar too. A quarantine hold is never written in the manifest; it comes from the selection that `verdict_flow.py select` builds from the open asks. So with S21 as written, AC17 stays red. Either S21 has to say where the quarantine holds are read from, or AC17 has to change.
2. **S1's widen records are named after other units.** The widen command files each record under the unit it is caused by. That gives one record each for units 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 25, 29, 30, 40, 41, 42 and 43, plus 51. The spec's file list only allows records named for unit 51. Regenerating the build index, which the brief requires, would also rewrite the generated records table in each of those units' CLOSED specs, which are meant to stay frozen and aren't listed.
3. **The kickoff manifest re-stamp is missing.** The change edits four files that `memory/guides/SESSION-KICKOFF.md` watches (`check-memory-hygiene.sh`, `run-gates.sh`, `run-selftests.sh`, `.memory-tree.conf`). That file is in neither the spec's file list nor the declared write set.

Separately, the declared write set left out four paths the spec does list: `.gitattributes`, `AGENTS.md`, `WIRE-INTO-PROJECT.md` and `.memory-tree.conf`.

**What I checked:** read-only probes against the tree at the base commit, checking the spec's claims about current code before writing anything. Everything else I probed matches the tree:
- the 20 grown, 3 shrunk and 1 new shell-role rows;
- the AC3 grep population and the 20 waiver rows;
- the 5 flagged `New arm:` lines, 2 of which resolve to legs;
- the 13 `resolve_shell_argv` call sites;
- the `b80649e60` commit for AC8;
- the `AGENTS.md` size (23575 against a high-water row of 16732) and the protocol size (68283 against 68288);
- the remaining symbols and pinned lines the spec cites.

These probes don't stand in for any gate. I ran no gate, suite or bar, wrote no product code, and observed no criterion or new arm. No commit was made, so I didn't run the post-commit checklist (`gotchas.py --for-diff`). The working tree is unchanged: the edits to `help/reference/drive.md` and `help/reference/units.md` and the staged `memory/builds/dWitnessedBar/RUN.md` were already there before this pass.
