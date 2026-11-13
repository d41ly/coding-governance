# Brief — aNimbleMend: unit 13, the findings of the pass legs' first run repaired

**Serves:** research TOOL-aNimbleMend-13

## The prompt

> Build an opt-in mechanism (opted in by default in any repo) that allows two things: 2. passes run ONLY fast legs: an opt-in pass leg list that should NOT EXCEED 10 minutes (with 10-15% fluctuation) per pass.

The owner's prompt is recorded whole in `memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md`; this unit serves the passage above.

## The brief

### Goal
The main loop ran `bash tools/run-gates/pass-legs.sh --base HEAD~1` once, over the pass commit `bde79f210`. Eight legs went red. This unit repairs every finding that is a defect of this build, so that a pass-leg run in this repository reds only on a real red of the pass it grades. Each defect sits in a unit whose spec is CLOSED, so the repair is a new unit on top.

### Items
1. Three declared pass legs read the leg list the environment names as their SUBJECT, and the pass-leg runner hands the bar runner a filtered list, so each false-reds: `testsuite counts (every bar self-test prints one)` reports every waiver as naming a suite the manifest does not run, `leg ceilings clear their evidenced maximum` reports evidence rows naming legs the manifest no longer carries, and `every held leg is budgeted, every budget row resolves` reports budget rows with no leg. Under a pass-leg run each must grade the whole manifest, or leave the declared list by a rule the derivation states.
2. The selection rule of `tools/run-gates/pass_legs.py` declares `python resolver (behaviour + inline parity + idiom ban)`, a leg the bar runner holds as a self-test or kit-subject leg, so the budget gate reds and every pass-leg run prints the held finding. The rule must never select a leg the runner would hold.
3. `govkit selfcheck` refuses `tools/run-gates/kit.toml`: the kit now declares `[[regenerate]]`, and a sentence says `update` re-renders without naming `GOVKIT_RERENDER` in the same sentence.
4. `lexicon naming predicates` and `lexicon wiring` red at 1209 verb offenders over the pin of 1208: `tools/run-gates/pass_legs.py` defines a function named `strip`, whose leading token is no declared verb. Rename it through the lexicon's `--suggest`; never move the pin.
5. The `cmd_check` docstring of `tools/run-gates/derive-ceilings.py` still says it reads two tracked files and nothing else, and the budget arm now also reads the pass-leg evidence.
6. For item 1, read how `tools/run-gates/pass-legs.sh` builds the filtered list and how `tools/check-testsuite-counts.sh`, `tools/run-gates/derive-ceilings.py` and `tools/run-gates/run-selftests.sh` read the leg list, then choose one mechanism and say why. The preferred direction: a pass-leg run keeps the whole manifest as every leg's subject and narrows only which legs the runner starts. Leaving the three legs out of the declared list is the fallback. A choice that is not derivable is a fork in the spec's open questions, with a recommendation.
7. Write the spec at `memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-13.md`, Tier-2, status SPECCED, order 13, with `memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-3.md` as the worked example of the shape. Units 1 to 7 are CLOSED and frozen, so declare edges only as `external` or to the unbuilt units 8 to 12, and state each correction in this spec itself.
8. The exact red lines are in the failure record `gate-last-failure.txt` of this worktree's git directory, `C:/projects/coding-governance/.git/worktrees/inline-bar-fixes-pass-legs-1a64f7`. A criterion that needs a pass-leg run or a gate leg run is the main loop's, and the spec says so in that criterion, as `TOOL-aNimbleMend-4` does for its last two.
9. Every spec line stating a figure with a unit carries the word PINNED or a commit sha on the same line. The acceptance section cites no path the unit has not built yet. Before returning, stage the spec and clear `python tools/check-spec-tokens.py --spec` over it and `python tools/playbook/positional.py check`; do not run the whole-tree memory hygiene, and do not commit.

### Acceptance
- A pass-leg run in this repository over a commit that touches none of these legs' inputs reports none of the three list-reading legs red and prints no held finding.
- `python tools/run-gates/pass_legs.py --budget` exits 0 over this repository's manifest, and the declared list still sums inside the budget.
- `govkit selfcheck` no longer names `tools/run-gates/kit.toml`.
- The lexicon's verb offender count is back at its pin with the pin unmoved.
- Each fix of a gate's behaviour has an arm seen red.

### Gates
The full bar once, at the close, with `GATE_FULL=1`, without the self-tests and without the unattended kit gate leg.

### Non-goals
- The `docs` leg's two undocumented policy keys, which `TOOL-aNimbleMend-11` documents.
- Any change to the three list-reading legs' behaviour under the full bar.
- Any kit version, which the lander's mint moves.

### Limitations
- A CLOSED spec stays frozen; this unit's spec states each correction itself.
- A pass leg never runs inside a role agent's pass, so the criterion that needs a pass-leg run is the main loop's, and the unit's header stays INPROGRESS until the main loop has observed it.
- The derivation's output, the `pass_leg` fields and the evidence file, is re-derived by the tool on node `a`, never typed.

### Reuse
- The run's log is at the main loop's scratch path and is not tracked; the findings above quote it. The failure record is `gate-last-failure.txt` in the worktree's git directory.
- Seams: `tools/run-gates/pass-legs.sh` (the adapter that builds the filtered list), `tools/run-gates/pass_legs.py#check_pass_eligible` and `#check_pass_budget`, `tools/check-testsuite-counts.sh`, `tools/run-gates/derive-ceilings.py`, `tools/run-gates/run-selftests.sh`, `tools/run-gates/kit.toml`.
- `TOOL-aNimbleMend-5`'s builder named the three list-reading scripts in its return, and `TOOL-aNimbleMend-3`'s builder named the kit-subject row.

## Drawn from the session

> GATE FAIL  govkit selfcheck  (exit 1) · GATE FAIL  docs  (exit 1) · GATE FAIL  lexicon naming predicates  (exit 1) · GATE FAIL  testsuite counts (every bar self-test prints one)  (exit 1) · GATE FAIL  writing practice (records and units)  (exit 1) · GATE FAIL  leg ceilings clear their evidenced maximum  (exit 1) · GATE FAIL  every held leg is budgeted, every budget row resolves  (exit 1) · GATE FAIL  lexicon wiring  (exit 1)
— agent, the pass-leg run of 2026-11-12 over `bde79f210`, 211 s wall on node a (PINNED, 2026-11-12)

## Owner confirmation

not asked — the run is unattended, and the unit is added under the mandate by `--rescope --act add`
