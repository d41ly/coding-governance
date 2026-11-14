# Acceptance ledger — TOOL-aClearedLedger-13

**Serves:** journal TOOL-aClearedLedger-13

Built against spec rev-1 in this record's own commit, from base 144653086.
Each line is a probe the builder made in the pass: the two probes of TOOL-aClearedLedger-11's spec over this spec's rows file and over that spec's, saved in the session scratchpad and run from the worktree's toplevel, and the criteria's own greps. No suite, gate leg or bar ran in the pass.
Before the edit probe C named rows T1 to T9 and ended `rows wrong: 9`, the red figure the spec states for AC1 (PINNED, 2026-11-14), and probe H ended `rows wrong: 0` over both files: this unit changes no code of the hook.
The floor the builder found in the hook's suite was the one TOOL-aClearedLedger-12 left, so the raise is the spec's own derivation and nothing was added to another value.
The cap fixture was built under the machine's temp directory by a short name and not in the session scratchpad, as the harness rules for a fixture repository, and was removed after the probe.
Owed to the close: the three suites on a frozen clone, the legs of the spec's Gates section, the lint's own argv over the tree read for a `[bar]` row, and the RED-first observation of each `New arm:` line, staged as that line says. Check 8's printed clause is among them: the pass did not run the template size gate, so arms A25c and A25d are unobserved until the close.
Not a criterion, and probed all the same: `bash -n` read each of the three suites without a syntax error; the widened spellings array, cut out of the lint's suite and fed to `check_bar` over the suite's staged rows, read every entry as a hit, and over the lint at the base it named the four entries of item M1 and the two of item M2 (PINNED, 2026-11-14); and the three commands of the hook's new arms, fed to the hook's own functions over a staged leg, read hit, miss, miss.

**Evidences:** TOOL-aClearedLedger-13
- AC1 — `rows wrong: 0 · no set: False` — probe C, run through `python` against `tools/check-spec-tokens.py`, printed that as its only line over the rows file and again over the older rows file (PINNED, 2026-11-14).
- AC2 — `rows wrong: 0` — probe H, run through `node` against `tools/unattended/gate-guard.js` and the rows file, printed that as its only line, on a tree holding TOOL-aClearedLedger-12's guard at 320ca81be.
- AC3 — `grep -c 'run_planted "D6 the leg behind python3 -m pdb' tools/unattended/gate-guard.test.sh` — printed 1, and `grep -c 'run_planted "D6 a kept gap: ' tools/unattended/gate-guard.test.sh` printed 2 (PINNED, 2026-11-14).
- AC4 — `git diff --cached -U0 -- tools/unattended/gate-guard.test.sh | grep '^[-+]FLOOR_ASSERTIONS='` — printed one removed line holding 214 and one added line holding 217, the removed value plus 3 (PINNED, 2026-11-14).
- AC5 — `git diff --cached -- tools/check-spec-tokens.test.sh | grep -c '^[-+]FLOOR_ASSERTIONS='` — printed 0, and the criterion's first grep over the suite printed 9, one line for each entry of the spec's table (PINNED, 2026-11-14).
- AC6 — `grep -c 'glued variable prefix' tools/unattended/gate-guard.js tools/unattended/README.md tools/check-spec-tokens.py` — printed 1 for every file; the grep for the second phrase printed 2, 2 and 1; the grep for the count word printed 0 for both files and the last grep printed 0 (PINNED, 2026-11-14).
- AC7 — `python tools/policy/budgets.py resolve AGENTS.md=default:49152` — in the fixture it exited 0, its first line read `AGENTS.md`, 49152, `refuse`, `constant`, its second opened `policy: refused`, and the `home` verb printed 32768 as its third field, under the 49152 answered; `grep -c -e 'A25c ' -e 'A25d ' tools/check-template-size.test.sh` printed 2 (PINNED, 2026-11-14).
- AC8 — `git diff --cached --name-only | grep -cxFf <(sed -n 's/^watch: //p' memory/guides/SESSION-KICKOFF.md | tr ';' '\n' | sed 's/^ *//')` — printed 0 with the six code files staged, so no watched file moved and no stamp is owed (PINNED, 2026-11-14).
