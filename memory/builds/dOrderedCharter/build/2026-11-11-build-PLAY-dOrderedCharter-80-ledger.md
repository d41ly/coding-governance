# PLAY-dOrderedCharter-80 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-80

Each line is a probe this pass ran at rev-1 of the spec, over `67f588760` with the pass applied in the worktree.
No leg, suite or bar ran in the pass: each checker the criteria name is the close's, and where a line says
"owed" the main loop observes it after every unit is terminal. The probes ran a criterion's own `python -c`, a
copy of a changed module's lines over a scratch fixture, or a `git grep`.

**Evidences:** PLAY-dOrderedCharter-80
- AC1 — `bash tools/check-install-prefix.sh` — owed. `git grep -n "PFX / \"playbook\"" -- tools/govkit/matrix.py` printed nothing, and the shape-5 arm's read of the `playbook-render` descriptor resolved the template's `to` to `tools/playbook/coding-governance-agents.template.md` in a scratch target's context (PINNED, at 67f588760 with the pass applied).
- AC2 — `bash tools/check-dead-paths.sh` — owed. `git grep -c "adopt-agent-instructions.sh" -- tools/dead-path-waivers.txt` counted 2, each row's text the trimmed registry line its matcher compares (PINNED, at 67f588760 with the pass applied).
- AC3 — `python tools/govkit/govkit.py selfcheck` — owed. The criterion's `python -c` printed `['A.md']`, and `derive_root_shipped` over the live descriptors returned the root template alone, disjoint from the five root confs (PINNED, at 67f588760 with the pass applied).
- AC4 — `python tools/govkit/govkit.py selfcheck` — owed. The leg's argv in `tools/govkit/entries/check-microformats.kit.toml` holds two elements, `bash` and the gate (PINNED, at 67f588760 with the pass applied).
- AC5 — the gate over the tree — owed. The criterion's fixture, a copy of the gate under a scratch repository beside a `playbook` directory, exited 0 printing `microformats OK —`, then exited 2 printing `not delimited by exactly one fence pair` once the kit's template was removed; the base gate over the same fixture exited 2 on the first run. At gov the resolver found `tools/playbook`, which holds no template, so a no-argument run reads the root template (PINNED, at 67f588760 with the pass applied).
- AC6 — `python tools/govkit/govkit.py epoch` — owed. The criterion's `python -c` printed `skip broken`; `derive_epoch_state` for the live `playbook` entry returned `skip · no declared version · moved: none`; a scratch registry holding a fileless `none` entry printed `epoch: fk · skip · no declared version · moved: none` under the pass's engine and `epoch: fk · FAILED · no engine/seed/rendered/merged source to measure` under the base engine (PINNED, at 67f588760 with the pass applied).
- AC7 — `python tools/govkit/check_runbook_parity.py` — owed: the scratch guard refused it as the parity leg. `PROBLEM_PIN` reads 17 (PINNED, at 67f588760 with the pass applied).
- AC8 — `python tools/govkit/matrix.py` — owed: a role agent's scratch guard refuses a scratch install. `git grep -c "render_deploy_tail(" -- tools/govkit/matrix.py` counted 4, and the tail for the registry default printed its `kits` line, the answers header and one stub per placeholder with the five fixed answers over them (PINNED, at 67f588760 with the pass applied).
- AC9 — `python tools/playbook/render_playbook.py --selftest` — owed. A probe running the cross-os arm's lines over gov's template refused with `the document registry … does not read` for both renders without the planted registry, and rendered both with it (PINNED, at 67f588760 with the pass applied).
- AC10 — the render self-test — owed. The legacy arm's lines over gov's engine: a `v4.0` marker exited 0 printing the reseed note, and the engine's own major, `v5.0`, exited 1 printing `legacy v3 placeholder`; `git grep -n "'v4.0', 'legacy" -- tools/playbook/render_playbook.py` printed nothing (PINNED, at 67f588760 with the pass applied).
- AC11 — `run_fixture("drive-default-route")` printed `ok · the unattended start line renders once, with the attended /build line directly under it` and exited 0; with the `/build` row filtered out of the drive rows it printed `FAILED` and exited 1; `git grep -c "the unattended start line renders once" -- tools/playbook/render_playbook.py` counted 0. The matrix half is owed with AC8 (PINNED, at 67f588760 with the pass applied).

**Owed to the close.** Every leg of the spec's Gates section, and the RED-first observation of each of its four
`New arm:` lines: the no-argument arm pair in `tools/check-microformats.test.sh`, the fileless `fk` entry of
`check_epoch_verb` in `tools/govkit/selftest.py`, the cross-os and legacy arms of the render self-test, and the
`drive-default-route` plant of `tools/playbook/instruction_units.py`.
