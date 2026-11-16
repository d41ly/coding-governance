**Serves:** journal TOOL-dDeclaredLoop-33

# Builder return — TOOL-dDeclaredLoop-33, dispatch 3: the pass commit was refused by hygiene check 12: six forks carried no resolution mark

## Why

DIVERGENCE: spec §8 (Open questions) cannot reach CLOSED as written. Six of its forks, F5, F6, F7, F9, F10 and F11, end with "Recommendation (a); the spec body is written on it." None of them carries a conforming resolution mark (`RESOLVED (<who>, <date>, <how>): <option>`), which F1 to F4, F8 and F12 to F14 all have. The pre-commit hook's memory-hygiene check 12 refused the pass commit with this message: "HYGIENE check 12 FAILED — spec files dated >= 2026-07-15 not conforming to memory/TEMPLATE-SPEC.md: memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-33.md (terminal Status, §8 F-items carrying no conforming resolution mark in their own span, at/after FORK_ITEM_CUTOFF 2026-09-30): F5, F6, F7, F9, F10, F11". A builder may only change the status line, so the fix is the spec writer's: mark each of those six forks resolved to (a), as the body is already written, in a rev-9. That is the only change needed. With it, rev-8's design builds as written: the code was finished, every criterion was observed on the working tree, and the sweep re-run at the base held (23 cycles over 45 edges PINNED, nothing unreached, 0 live builds PINNED, lexicon offender pin 1215 PINNED, no `*.sh` edited). The hook stopped at this hygiene failure, so any pre-commit gates that run after hygiene were not reached. The work is saved as a patch and every path is restored; see summary.

## Summary

Nothing is committed and the tree is clean at 2fa00d7c3. I built the whole unit, but the commit that closes the spec was refused by memory-hygiene check 12: six forks in §8 (F5, F6, F7, F9, F10, F11) carry no resolution mark. Only the spec writer can add those marks; details are in `why`.

**Saved work.** All 29 changed paths are in C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/TOOL-dDeclaredLoop-33-builder-3.patch. `git apply --check` passes against HEAD. It contains:
- the new `tools/loop/termination.py` and `tools/loop/termination-pending.txt`;
- edits to `tools/loop/loop.toml`, `item-schema.toml`, `adapt.py`, `loop_transition.py`, `position.py`, `kit.toml` and the kit README;
- the gate-leg, registry, usage, subject-pins and selftest-budgets rows, `help/loop.md`, the feature dossier and the kickoff manifest re-stamp;
- the regenerated map and build-index outputs, the acceptance ledger and deviation 335;
- the `RUN.md` dispatch row, and the spec header set to CLOSED.

**Re-landing after rev-9.** Apply the patch, take the spec header from rev-9 (setting only its status to CLOSED), and run `gen_build_index.py --write` and `gen_map.py --write` again. The kickoff manifest re-stamp must point at the new HEAD. Then commit. My draft commit message is at C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/msg33.txt.

**Commands I ran.** `--dispatch` with the full write set: it was accepted and staged a dispatch row in `RUN.md`, which I restored, so dispatch needs to run again. `--brief`: already recorded, unchanged. The naming lexicon's suggest verb: every new function name passed.

**Checks that ran, and the gate each stands in for:**
- `termination.py check` over this repository, with the item rows read from the working definition by a `python -c` probe because the compose verb reads HEAD: exit 0, both pending counts printed (AC10). Stands in for `loop termination`.
- All 15 termination plants, run one at a time by direct CLI, each printed `held`: AC1 to AC5, AC7 to AC9 and AC11. Stands in for `loop termination`.
- The adapt plants `additive`, `owner-approves`, `mid-step`, `loosening`, `act-mismatch` and `unit-row`, run one at a time, each `held`. The `loosening` held row ends `· recommend decline`. Stands in for `loop adapt fixtures`.
- A `python -c` probe of `check_loop`, `check_program`, `check_witness_classes` and `check_transition_tables` over the edited definition: no refusals. Stands in for `loop definition` and `loop transition tables`.
- A `json.load` probe of the new leg row: one row named `loop termination` with argv `termination.py check --selftest`, no `guard` key, `enforces` holding `principle.p39` and `stage` holding `step.test` (the rest of AC10).
- `grep -c CLAIM_WAIT_CEILING tools/loop/README.md` printed 1 (AC12).
- `docs_leg.py --fingerprints` for the two new help anchors.

**Owed at the close:**
- Every leg §7 names, plus `loop termination`.
- RED-first on the `tools/loop/termination.py` arm: every plant against the base, where the module does not exist.

The gotchas checklist (`gotchas.py --for-diff`) did not run, because there is no pass commit to read.
