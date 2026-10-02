# TOOL-aRepatriatedFork-26 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-26

Written by the unit pass on node a, 2026-09-29. No merge bar, no self-test runner and no whole suite
ran. Fixture repositories were built under the temp root and removed after. Two changed suite arms
ran as slices, each its suite's prologue plus the one block, in a temporary script inside the kit
directory that was deleted after. The `govkit apply` fixtures read gov from a local clone whose tip
carried this unit's working tree, because `apply` lands committed bytes.

**Evidences:** TOOL-aRepatriatedFork-26
- AC1 — `git grep -nE '<project>/tools/' -- WIRE-INTO-PROJECT.md` prints nothing and exits 1. Every `cp` step names `<project>/<prefix>/<kit>` and gov's side `<gov>/<prefix>/<kit>`, and the Definitions line declares `<prefix>` once for both
- AC2 — a per-line scan of the 22 owned files with the gate's own counter program — 203 counted literals before, 7 after, all seven in WIRE's `harness-migration` blocks, which rev-3 returns. `--write-ratchet` wrote 189 rows, down from 210, and removed every owned row but WIRE's, which now counts 7 under a hand-written reason. `bash tools/check-install-prefix.sh` exits 0, clean on all three arms, and the `tools/memory-tree/README.md:117` waiver row is struck
- AC3 — `govkit apply` at prefix `scripts`, kits lexicon, review-harness, drift-audit, kickoff-manifest, playbook, memory-tree, agent-cap and settings-merge — the rendered lexicon Skill names `python3 scripts/lexicon/lexicon.py` four times and carries no `tools/`. The seeded `AGENTS.md`, `SESSION-KICKOFF.md` and `drift_signals.py` carry no `tools/` and three `<prefix>` tokens each. The review-harness renders are not produced by `apply` ("nothing in this install produces it"), so the drift-audit-state template landed carrying `{{TOOL_ROOT}}`; its renderer's substitution rule, read and not run, writes `scripts/gate-legs.json` there, and gov's own render is byte-unchanged
- AC4 — the same `apply` into a second fixture from `e870bb9a`, the pre-change tip, whose five touched templates carry the same `tools/` lines as `2143b6d6`'s — the seeded `AGENTS.md` carried 3 `tools/` paths, `SESSION-KICKOFF.md` 2, `drift_signals.py` 3, and the rendered lexicon Skill 1, so the control is red as required. Both runs printed the same five pre-existing problem lines
- AC5 — `bash tools/check-kit-versions.sh` exits 0 after twelve kits moved in every carrier: agent-cap 1.24, check-wiring 1.14, codebase-map 1.14, drift-audit 1.17, kickoff-manifest 1.10, lexicon 1.12, memory-recall 1.21, memory-tree 2.105, playbook-render 1.13, process-monitor 0.9, review-harness and tier2-review 1.16, run-gates 1.13, and the charter at v3.2 with v3.1 cut to the archive. `bash tools/check-template-size.sh` exits 0 at 48238 of 49152 bytes. `govkit.py selfcheck` exits 0. The `govkit.py epoch` verb grades commits, so it ran against this unit's commit, as the commit message records
- AC6 — `bash tools/check-playbook-parity.sh` exited 1 naming hooks, playbook, process-monitor and workflows before `named_in_playbook` took the `<prefix>/<kit>/` form, and exits 0 after, 17 kits documented or waived. The sliced AC12 block of `check-wiring.test.sh` passed 4 of 4, and with the README's line put back to `tools/` it failed its two published-command arms
- S7 — the sliced arm 3 of `adopt-codebase-map.test.sh` passed 5 of 5 with `DEFAULT_MDC` at the example's new shape, and failed the three declined prefixes with the old root value staged back; the sliced arm 4, the documented copy-the-example path, passed
