# Brief — aShelvedLeg: the unattended kit gate runs only on demand

**Serves:** research TOOL-aShelvedLeg-1

## The prompt

> exclude check-unattended from merge/push bars and make it run only on demand

The owner's turn on 2026-11-10. It came after the aSwiftRefusal lander had spent over two hours on its
push bar and had failed it on host contention, with the `unattended kit gate` leg running 45 minutes.

## The brief

### Goal
`check-unattended.sh` runs on no automatic bar, merge or push, in this repository or an adopter's, and still runs whenever someone asks for it.

### Items
1. The `unattended kit gate` leg declares `subject = "kit"` in `tools/unattended/kit.toml` and in `tools/gate-legs.json`. The bar already holds every `kit` leg unless `GATE_SELFTESTS` is set, so no new switch is built. `tools/govkit/subject-pins.tsv` is regenerated so the move shows in the diff. The descriptor records the owner's ruling and its price beside the leg. [planned TOOL-aShelvedLeg-1]

### Acceptance
1. A bar with `GATE_SELFTESTS` unset prints `GATE held  unattended kit gate` and does not run `check-unattended.sh`. At BASE the same bar runs it.
2. With `GATE_SELFTESTS=1` the bar runs the leg.
3. `bash tools/unattended/run-unattended-gates.sh --checks` still runs `check-unattended.sh`.
4. `python tools/govkit/govkit.py selfcheck` is green: the descriptor, the manifest and the subject pins agree.

### Gates
govkit selfcheck · kit version markers · kit epoch · memory hygiene · spec tokens · docs · routed commits · brief-recorded; then the full bar at the lander.

### Non-goals
Making `check-unattended.sh` faster or scoping its checks (TOOL-dThriftyLanding-7 stays open). A per-repository hold override. Any other leg's subject. Changing what `GATE_SELFTESTS` runs.

### Limitations
Kit versions move through the lander's `mint`, not by hand. The change reaches adopters only at their next `govkit update`. The bar's subject criterion in `run-gates.sh` says a leg whose failure means "this repository is misconfigured" is `repo`; this leg is `kit` by the owner's ruling, not by that criterion, and the descriptor says so.

### Reuse
The bar's existing hold: `run-gates.sh` holds a leg whose subject is `kit` or whose chunk is `selftests`, and `GATE_SELFTESTS=1` runs it (owner ruling 2026-08-23). `aBenchedProbe` declared `subject = "kit"` in a descriptor for the same reason, cost. Recall returned TOOL-aBoundedCeiling-10: a held leg cannot notice its own drift, and the kit gate was RED on main for weeks in August 2026 (TOOL-aBoundedCeiling-9).

## Drawn from the session

> GATE FAIL  routed commits name a specced unit  (timed out after 760s, again on its serial retry; HOST: a spawn cost 9.1x this clone's floor)
— agent, the aSwiftRefusal lander's output, 2026-11-10, after 7652 s

> unattended kit gate	2038.741	ok	…	478bf8254…
— agent, this worktree's gate ledger: the leg's wall on aSwiftRefusal's branch bar

## Owner confirmation

Asked: The unattended kit gate's subject is declared in tools/unattended/kit.toml, and govkit requires that descriptor and gate-legs.json to agree. There is no override per repository, so flipping it to `kit` (held) also holds it in every adopter's bar (incms, nicocares) at their next `govkit update`. Which scope?
Answer: "Every bar (Recommended)"

Asked: Kickoff for aShelvedLeg is READY: one Tier-2 unit, TOOL-aShelvedLeg-1. It flips the `unattended kit gate` leg's subject to `kit` in kit.toml and gate-legs.json, regenerates the subject pins and records the ruling in the descriptor. A bar then holds the leg, and it runs via `run-unattended-gates.sh --checks` or `GATE_SELFTESTS=1`. Start the build (spec writer, then builder, then review, then land, then re-run the aSwiftRefusal lander)?
Answer: "Go"; spec audit: "No (Recommended)"
