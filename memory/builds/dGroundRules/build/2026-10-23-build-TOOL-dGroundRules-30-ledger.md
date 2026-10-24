# TOOL-dGroundRules-30 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-30

No merge bar, no gate leg and no self-test suite ran in this pass; a role hook refuses them, and it
refused the parity script's `--check` mode as a suite. Every criterion was observed by hand in a
scratch clone of this branch at `a5bc3f94b` under `%TEMP%`, with this pass's
`tools/workflows/check-protocol-parity.test.sh` copied over it, running the kit's `--render` mode and
`check-verifier-fanout.sh` in its explicit-file mode. The clone was removed after. The `New arm:`
line's red-first observation and the §7 legs are the close's.

**Evidences:** TOOL-dGroundRules-30
- AC1 — `govkit update --kits agent-cap` — with the clone's `WRITER_MARK` staged to `gov:staged-other`, `--render` exited 0 and stderr printed `protocol-parity: the agent-cap hook does not admit the writer split: BLOCKED by agent-cap: a verify/fan-out stage spawns one agent per item. ... Update it: govkit update --kits agent-cap`; the rendered `unattended-build.js` carried `boundedParallel(thunks, cap = 5)` at line 150, `const SPEC_WRITERS = 5` at 942 and `// gov:fixed-verifiers` on the split at 957, and `grep -c "Math.min(" tools/workflows/unattended-build.js` printed `0`. With the HEAD hook restored by `git checkout -- tools/hooks/agent-cap.js`, `bash tools/workflows/check-verifier-fanout.sh tools/workflows/unattended-build.js` exited 0, and with `git show 3c2b69be:tools/hooks/agent-cap.js` written over it, exited 0 again.
- AC2 — `gov:fixed-writers` — in the unchanged clone `--render` exited 0 with an empty stderr, the rendered `unattended-build.js` kept `// gov:fixed-writers` on the split at line 957 and equalled the tracked copy (`git status` showed no change to it).
- AC3 — `grep -c "KIT_AGENT_CAP_VERSION" tools/workflows/check-protocol-parity.test.sh` — printed `0`; `WRITER_FLOOR` counts 0 too.
- AC4 — `--render` — with the clone's `agent-cap.js` staged to a script that reads stdin, prints `BLOCKED by staged hook: every script denied` and exits 2, `--render` exited 2, stderr named that line, stdout printed `the agent-cap hook denies unattended-build.js's verifier-bounded fallback too, so nothing was rendered or graded. Its answer:` over the hook's line, and `git hash-object` of `unattended-build.js` was the same before and after.
- AC5 — `DEFAULT PARAMETER` — in the clone holding the base `3c2b69be` hook, AC1's render staged with `const SPEC_WRITERS = 6` made `check-verifier-fanout.sh tools/workflows/unattended-build.js` exit 1 naming `does not show to be bounded`, and staged with `boundedParallel(thunks, cap = 6)` exit 1 naming `DEFAULT PARAMETER of boundedParallel() is 6, above the 5-agent cap`.
