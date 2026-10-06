# Acceptance ledger — TOOL-aGraftedHelix-17

**Serves:** journal TOOL-aGraftedHelix-17

Node `a`, 2026-10-05. The build commit is `ec687ade`, over the dispatch records commit `6e61446f`.
The code matched the spec's rev-3, so no revision preceded it. No merge bar and no self-test suite
ran in this pass. The direct check was AC1's slice: the suite's prologue, lines 1 to 135, plus unit
14's check-27 engine block with the new arm, written under the session scratchpad with `HERE`
pointed at `tools/memory-tree` and the fixture under a short `%TEMP%` directory. The slice dumped the
branch run's output to a file so that the green run's lines could be read too. Three copies ran, each
built from the tracked file and none editing it: as written; with the branch row's body made the
base row's; and that second copy with the new arm deleted. The break is the real base row text, not
a synthetic value, and it keeps the branch row's own id.

**Evidences:** TOOL-aGraftedHelix-17
- AC1 — `check 28:` — at `ec687ade` the slice as written exited 0 with `PASS (5 assertions)`, its branch run printing `check 27: ARCH-tTwo-1 (memory/DECISIONS.md:4) near-matches ARCH-tOne-1 at 0.462` and no line opening `check 28:`. With the branch row's body made the base row's verbatim, `ARCH-tTwo-1` kept, it exited 1 printing the new arm's `FAIL check 27 through the engine: the branch run printed a check 28 line - the fixture's branch row ARCH-tTwo-1 is a content duplicate of its base row ARCH-tOne-1, so the exit belongs to check 28 and not to 27`, quoting `check 28: 2 records hold one content key — memory/DECISIONS.md:3 (ARCH-tOne-1), memory/DECISIONS.md:4 (ARCH-tTwo-1)`, beside the --offenders arm's red keying `[check 27,check 28]`; the branch run printed check 27 and check 28 lines and zero lines opening `check 20:`. With the new arm deleted from that copy it still exited 1, through the --offenders arm alone, and its text appeared zero times.
- AC2 — `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` — run at `ec687ade` with base `6e61446f` it exited 0 and printed `epoch: memory-tree · clean · 2.127`, and with the unit's starting HEAD `b388b24a` as the base it printed the same line; `bash tools/check-kit-versions.sh` printed `kit-versions: clean — 16 declared carrier(s) under tools/`.
