# Acceptance ledger — TOOL-aProfiledEffort-1

**Serves:** journal TOOL-aProfiledEffort-1

Built against spec rev-1 at the pass's parent `bb2e53cc6`. Each line below is a probe of the changed code, made in the pass. The fixtures `pe1` and `pe2` and the two scratch scripts sat in the run's scratch directory and are not tracked. No suite, gate leg or bar ran in the pass, and the render self-test did not run: arm 19's own code has not executed, and the driver of AC9 is a second spelling of its calls. Owed to the main loop at the close: the legs of the spec's Gates section, and arm 19 observed RED on each of its two staged breaks and GREEN restored, recorded here under a `Pass: none` commit.

**Evidences:** TOOL-aProfiledEffort-1
- AC1 — `python tools/roles/handoff.py stage-efforts spec-write` — it and the same verb for `spec-review`, `build` and `closing-review` printed the four lines of the spec's Evidence table byte for byte, and the role probe printed the nine `slot=level` pairs the criterion pins.
- AC2 — `['medium'] 9 13` — the criterion's command printed exactly this over the tree's policy.
- AC3 — `True None fable fable` — the criterion's command printed exactly this.
- AC4 — `$SCRATCH/pe1` — with the `probe` profile appended the criterion's command printed `max low {'diffFinder': 'low', 'skeptic': 'low', 'synthesis': 'xhigh'} {'builder': 'max'} True`, the library unedited since AC2.
- AC5 — `$SCRATCH/pe1` — the unedited copy printed `clean`; rows 0 to 13 each exited 1 with a last stderr line holding `R12 — `, the row's dotted key and the dash after it. Over `$SCRATCH/pe2/roles` the checker printed nothing on the unedited kit and one line with the same key for rows 1, 2, 4, 6, 10 and 12, and `grep -c "effort.profiles" tools/roles/check_roles.py` printed 1.
- AC6 — `effort.profiles.x.match` — the command printed `low`, then exited 1 with a last stderr line naming `claude-fable-5-2`, `effort.profiles.fable.match` and `effort.profiles.x.match`.
- AC7 — `python tools/roles/render_agents.py --check` — exited 0 with nine agent types and one index graded. Before the commit, with the pass's changes staged, the criterion's two `git diff` commands read against the index in place of `HEAD`: no path under `.claude` moved, and the policy's numstat line read 6 added and `0` deleted. The top-level tables printed `['effort', 'gates']`.
- AC8 — `python tools/codebase-map/gen_map.py --check` — exited 0 after `gen_map.py --write` moved `symbols.json` alone, and `grep -c '"id": "resolve_profile"' memory/map/generated/symbols.json` printed `1`.
- AC9 — `build_fixture` — a scratch driver importing `render_agents` from the kit directory built the arm's catalogue and made the calls of rows 19a to 19f through `run_mode` and the library; every row's assertion held, all thirteen refusal rows of 19e among them. `grep -c "check_arm(state, 19," tools/roles/render_agents.py` printed 5.
