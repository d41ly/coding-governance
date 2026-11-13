# Acceptance ledger — TOOL-aNimbleMend-4

**Serves:** journal TOOL-aNimbleMend-4

Built against spec rev-2 in the pass commits `0ea161c39`, the builder's, and `729762c56`, the main loop's. AC1 to AC7 are probes the builder made and returned; AC8 and AC9 are the main loop's own, as the spec assigns them. No suite or bar ran in either pass; the four legs of AC8 each ran once, alone, to be timed. Owed to the close: the legs of the spec's Gates section, the seven new arms of `tools/check-spec-tokens.test.sh` observed RED with the unit lookup removed and GREEN restored, and arm 1a's `scope_of` control in `tools/run-gates/run-gates.test.sh` observed the same way.

**Evidences:** TOOL-aNimbleMend-4
- AC1 — `tools/gate-legs.json` — the criterion's print over the manifest gave the three scoped rows as the spec's table spells them.
- AC2 — `python tools/check-spec-tokens.py --pass-spec 6fbf4a9b7~1..6fbf4a9b7` — named one unit and its spec, graded 1 named spec, exit 0. (PINNED, 2026-11-12)
- AC3 — `python tools/check-spec-tokens.py --pass-spec 1265772cc~1..1265772cc` — printed the zero line, exit 0.
- AC4 — `--pass-spec no-such-rev..HEAD` — printed REFUSING and exited 2, as did `--pass-spec` beside `--spec`.
- AC5 — `GATE_BASE=6fbf4a9b7` — the flag with no range named the range from that base to HEAD.
- AC6 — `read_scope_reds` — in fixture F the scoped form took its parent's 5 reds and read `selected`; a bad `scope_of` exited 2 with a clean tree; with the credit line removed the form read `no-red`. (PINNED, 2026-11-12)
- AC7 — `python tools/run-gates/owed_rows.py --base` — at the pass's starting tip it printed 0 rows owed and 3 deferred, and the grep over `core-pending.txt` printed 3. (PINNED, 2026-11-12)
- AC8 — `tools/run-gates/ceiling-evidence.txt` — the criterion's grep printed 4 after the four `--observed` writes, and no such row's source reads `runner`: 73.7 s, 9.3 s, 26.2 s and 13.3 s, each timed alone at the main loop on node a. (PINNED, 2026-11-12)
- AC9 — `GOV_NODE=a python tools/run-gates/pass_legs.py --report` — each of the four legs read `selected`, and `--check` exited 0 with 30 legs declared at 535.3s of the 600s budget. (PINNED, 2026-11-12)

## Arms observed at the close

The main loop observed each new arm on node a on 2026-11-13, in scratch clones of the branch under the host's temp directory: GREEN in a whole run of the suite, RED in a whole run with the staged break named below applied to the clone's copy of the shipped file and nothing else changed. The suites' inherited failures, present at base `1265772cc`, are named where they stand beside a red. (PINNED, 2026-11-13)

- `tools/check-spec-tokens.test.sh` — GREEN at `7e785ac21`: 249 of 250 assertions pass against a floor of 245; the one failure, the manifest parity arm, also fails at base. RED with the unit lookup answering no unit: four arms failed, `NM4 AC2` twice and `NM4 AC5` twice. (PINNED, 2026-11-13)
- `tools/run-gates/run-gates.test.sh` — arm 1a's `scope_of` control: GREEN and RED as the first line of TOOL-aNimbleMend-2's ledger states, in the same pair of runs, both keys having left the literal together. (PINNED, 2026-11-13)
