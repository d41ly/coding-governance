# Acceptance ledger — TOOL-aGuardedEffort-2

**Serves:** journal TOOL-aGuardedEffort-2

Built against spec rev-1 and committed at `927edde5d`. The builder ran the spec's observation and renderer probe in its pass. The main loop then ran the three suites at that commit: the hook suite printed `139 passed, 0 failed`, the render selftest `PASS (93 assertions)` and the roles adopter suite `PASS (76 assertions)`. It staged seven breaks of rule 8 through the hook suite: B2 read `unset` for a stage whose role the call names, B3 admitted a stage key the call names nowhere, and B4 let an unkeyed workflow admit.

**Evidences:** TOOL-aGuardedEffort-2
- AC1 — `tools/hooks/agent-cap.test.sh` — the observation's `r-swap` read `deny:` naming `builder`, `gov-skeptic` and its level; the suite's three `rule8 GE2 item 1` swap arms were green, and red under B2 (3 failed).
- AC2 — `tools/hooks/agent-cap.test.sh` — the observation's `r-omit` read `deny:` with a line per workflow and `r-union` read `admit`; the two omission arms were green, and red under B3 (2 failed).
- AC3 — `tools/hooks/agent-cap.test.sh` — the observation's `s-entry` and `s-key` read `throw:` naming `build`; the two `rule8 GE2 item 3` arms were green, and red under B4 (2 failed).
- AC4 — `tools/roles/render_agents.py` — the renderer probe printed `['build', 'nostage'] [{}, {}, {}]` and `True`, and the `--check` verb exited 0 with no re-render. Selftest arm 20 was green and has not been seen red.
- AC5 — `tools/hooks/agent-cap.js` — the criterion's payload exited 2 opening `BLOCKED by agent-cap: rule 6` with no `rule 8` in its text. The reorder that reds the order arms has not been staged.
- AC6 — `tools/hooks/README.md` — the criterion's `git grep` printed nothing and exited 1.
- AC7 — `tools/hooks/agent-cap.js` — the three counts printed `2`, `1` and `1`.
