# Acceptance ledger — TOOL-aBatchedPacket-2

**Serves:** journal TOOL-aBatchedPacket-2

Built against spec rev-1 by the unit's builder and left staged; the main loop committed it as `d46719074` with the generated map, the index and the manifest stamp the pre-commit hook requires. Lines marked builder are the builder's probes on a hand-built fixture; the rest were observed by the main loop on node a beside the live dDeclaredLoop run. No bar ran.

**Evidences:** TOOL-aBatchedPacket-2
- AC1 — `- <parent>: specs done yes, build done yes` — builder: the door's write gave `- dTrueNorth: specs done yes, build done yes` and the instrument's check then exited 0. Main loop: the suite's CP4 green, and red with the cache made to return an empty string.
- AC2 — `cache answered <n> of <n> parent path(s) · <k> holding a lone CR` — builder: `cache answered 6 of 6 parent path(s) · 1 holding a lone CR`, exit 0. Main loop: the suite's CP8 green, and red on the same staged break.
- AC3 — `python tools/playbook/core.py meta-check` — exit 0, no line naming `chain-packet self-test`.
- AC4 — `VERB_OFFENDER_PIN` — `--measure` printed `VERB_OFFENDER_PIN="1208"`, the value `.lexicon.conf` holds.
- AC5 — `tools/check-spec-tokens.py` — the checker suite's marker-door arm green; red with the door never routed. The suite's two remaining reds are the parity arms red at `8db6f4bef`.
- AC6 — `python tools/chain-packet.py --check <slug>` — the suite's CP3, CP4 and CP5 green with stderr empty; red with the in-process report made to raise.
- AC7 — `python tools/check-spec-tokens.py --legs-for tools/roles/handoff.py` — builder: the leg `chain-packet self-test` is listed against the tool root.
- AC8 — `GIT_DIR` — the suite's CP9 green; red with the location-variable branch switched off.
- AC9 — `git diff --quiet 8db6f4bef HEAD -- memory/builds/dClosedLoop/build/` — exit 0 at `d46719074`.
- AC10 — `python tools/chain-packet.py --check dDeclaredLoop` — on the frozen clone of `8db6f4bef`: the instrument's eight lines by `diff`, exit 1, 23 processes, 50.2 s; the write there took 18.2 s and its packet equals the instrument's by `cmp`. (PINNED, 2026-11-14)
- AC11 — `grep -c 'chain-packet self-test.354' tools/run-gates/selftest-budgets.txt` — prints 0, a departure: the nine-arm suite took 419 s, so the row reads 629 by the file's own rule, recorded on the pass commit. (PINNED, 2026-11-14)

The checker with one live chain run, on the frozen clone of `f75d11d47`, with the final door: 95.7 s, 49 processes, every line equal to the base checker's. (PINNED, 2026-11-14)
