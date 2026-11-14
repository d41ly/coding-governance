# Acceptance ledger — TOOL-aClearedLedger-3

**Serves:** journal TOOL-aClearedLedger-3

Built against spec rev-1 in this record's own commit, from base 127e5cc83.
Each line is a probe the builder made in the pass, over the fixture `<F>` of the spec's probe set built in the session scratchpad, with the hook in place so the manifest read is the real one. No suite, gate leg or bar ran in the pass; the suite file was parsed with `bash -n` and not run.
Owed to the close, and since observed by the main loop in this build's observations record: the gate guard's suite, AC10, and the RED-first observation of each of the three `New arm:` lines of the spec's Gates section. The header comment of the hook, the unobserved half of S8, is the closing review's to read against the code.

**Evidences:** TOOL-aClearedLedger-3
- AC1 — `node tools/unattended/gate-guard.js` — rows P1 to P5 each exited 2, and each stderr held `BLOCKED by gate-guard` and its leg's manifest name: `routed-commits selftest`, `measure-legs selftest`, `policy fixtures`, `corpus-ids selftest` and `build-index selftest`.
- AC2 — `node tools/unattended/gate-guard.js` — rows P6 and P7 each exited 0 with an empty stderr.
- AC3 — `node tools/unattended/gate-guard.js` — rows P8, P10, P11 and P12 each exited 2, P12 fed with the tool name `PowerShell`; a glued redirection and a double-quoted `$( … )` span around row P1 exited 2 as well.
- AC4 — `phase: VERIFYING` — row P9 exited 0 with the record at `BUILDING`, and row P1 exited 0 with an empty stderr once that line replaced the phase line of the fixture's run record.
- AC5 — `0 0 1` — the candidate probe of the spec's section 4, run through `node`, printed that line.
- AC6 — `[]` — `readSuiteLegs` answered it for the absent file, for a file holding the text `{`, and for a file holding a JSON object that is no list.
- AC7 — `tools/gate-legs.json` — a one-off probe over the hook's exports put each `chunk = selftests` leg in exactly one class: 53 denied by `scanDenyHits`, 5 matched by `checkSuiteLeg`, 15 in a direct-check form at or under the bound, 1 the script `test_recall_floor.py`; the sum is 74 of 74 legs, none in no class and none in two. (DERIVED from the manifest at 127e5cc83)
- AC8 — `--selftest,--fixture,fixture` — the second `node -p` printed it, the first printed `300`, and the grep over the suite counted 6 lines holding `DIRECT_CHECK_WORDS`. <!-- PINNED 2026-11-13 -->
- AC9 — `grep -n 'gate-legs.json' tools/unattended/README.md` — printed two lines: line 109, inside the paragraph under the heading "The act is refused at the tool call, not only forbidden", and line 428, which stood before this unit in another section.
- AC10 — `FAIL parity:` — the main loop ran the suite whole on a frozen clone at 48ee864e3, this unit's closing commit: no line opened that, it exited 0, and it printed `216 passed, 0 failed`.
