# Acceptance ledger — TOOL-aGuardedEffort-1

**Serves:** journal TOOL-aGuardedEffort-1

Built against spec rev-2 and committed at `27e6aead2`. The builder ran the spec's observation and parity probe in its pass; the main loop then ran the two suites the unit adds arms to at that commit, and at `927edde5d` staged seven breaks of rule 8, one at a time, through the hook suite. B1 made rule 8 return at once, B5 switched off the `CLAUDE_CODE_EFFORT_LEVEL` branch, B6 read the Agent call's expected level from the default table, and B7 switched off the two-profile note.

**Evidences:** TOOL-aGuardedEffort-1
- AC1 — `tools/hooks/agent-cap.test.sh` — the builder's observation printed `deny:` for `a-none` and `a-high`, naming `gov-builder`, `medium`, `claude-fable-5-2` and `role-efforts --model`, and `admit` for `a-medium`. The suite's `rule8 AC1` arms were green in `118 passed, 0 failed`, and red under B1 (30 failed) and under B6 (7 failed).
- AC2 — `tools/hooks/agent-cap.test.sh` — the observation's `o-none` read `admit` and `o-medium` read `deny:`; the suite's rule 8 arms for a model no profile matches were green, and among B1's 30 failures.
- AC3 — `tools/hooks/agent-cap.test.sh` — the observation's `w-none` and `w-high` read `deny:` naming `builder`, `medium` and `stage-efforts build --model`, and `w-medium` read `admit`; the suite's arms were green and red under B1.
- AC4 — `tools/hooks/agent-cap.test.sh` — the observation's `m-fable` read `deny:` naming `medium` and `the call`.
- AC5 — `tools/hooks/agent-cap.test.sh` — `n-path`, `n-unreadable` and `n-empty` each read `note:` with the not-checked line, and the hook exited 0 on a payload with no `transcript_path`.
- AC6 — `tools/roles/adopt-roles.test.sh` — the parity probe's `diff` printed nothing and its last line read `affable-1 -`; arm 20 was green in `PASS (74 assertions)`. Arm 20 has not been seen red.
- AC7 — `tools/roles/render_agents.py` — the `--check` verb exited 0 after the re-render, a hand-set level exited 1 naming `drift .claude/roles.json`, and arm 21 was green. Arm 21 has not been seen red in the suite.
- AC8 — `tools/hooks/scratch-guard.js` — an index whose `effort` is a list read `broken`, and the suite's `rule8 AC8` arms were green on both tools. They have not been seen red.
- AC9 — `tools/hooks/agent-cap.js` — the `w-none` payload piped to the hook exited 2 opening `BLOCKED by agent-cap: rule 8`, and with no `transcript_path` printed `rule 8 did not check` and exited 0.
- AC10 — `tools/roles/README.md` — the five grep counts printed `0`, `5`, `1`, `1` and `2`, in the criterion's order.
- AC11 — `tools/hooks/agent-cap.test.sh` — `f1-two`, `f2-agent` and `f2-workflow` read as the criterion says; the suite's `rule8 AC11` arms were green, the variable's arm red under B5 and the two-profile arm red under B7.
