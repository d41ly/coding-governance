# TOOL-aRepatriatedFork-46 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-46

Written by the unit pass on node a, 2026-09-30. No merge bar, no self-test runner and no whole suite
ran. Each criterion ran its direct check: the gate's own `--list` in a scratch clone, a probe of a
suite's derivation header run beside the suite, a slice of a suite inside its kit dir, or a
`--selftest` flag. The drain itself was checked mechanically before anything ran. With every
derived name read back as gov's, each edited shell suite renders identical to its previous bytes
apart from the derivation header and the lines rev-2 §4 names. Each edited Python file is
AST-identical to its previous bytes apart from its real reads of a sibling kit and the named edits.

**Evidences:** TOOL-aRepatriatedFork-46
- AC1 — `bash tools/check-install-prefix.sh --list` in a scratch clone whose `tools/zzfix/ac1.py` carries `run("plan", "--kits", "memory-tree")`, `x = ["bin", "lib"]`, `{"matcher": "a", "hooks": []}` and `os.path.join(w, "scripts", "run-gates")` records that file at 1, kit `run-gates`. With the comma branch's path-join test reverted in the clone's copy of the gate, the row reads 4, kits `hooks,lib,memory-tree,run-gates`
- AC2 — in the same clone `tools/zzfix/ac2.sh`, carrying `"$ROOT/${PFX}hooks/agent-cap.js"`, and `tools/zzfix/ac2.py`, spelling `{PFX}` before the lexicon kit, each record 1, and `tools/zzfix/ac2.md`, holding the hooks path led by `{prefix}/`, `{{TOOL_ROOT}}` and `<prefix>/`, records no row. With the brace rule reverted in the clone's copy, neither of the first two records a row. The suite's four new epoch-6 arms, sliced with their prologue, pass against the built gate and fail against the epoch-5 gate
- AC3 — `grep -n '^PREDICATE_EPOCH=' tools/check-install-prefix.sh` prints 6, `tools/install-prefix-carried.txt` records `predicate-epoch: 6`, and a second `--rebaseline` refuses naming the recorded epoch. Measured before any line was derived: rows 56 to 82 and occurrences 625 to 1004, which is 625 - 47 + 426
- AC4 — `--list` on the built tree holds 18 rows and 224 occurrences, every one TOOL-aRepatriatedFork-30's class: `tools/check-install-prefix.test.sh` 40, the frozen receipt 91, the rendered `tools/unattended/playbook.fixture.md` 5 and its two piece records 2 each, the two workflow scripts 6 and 1 at gov's literal prefix, `tools/dead-path-waivers.txt` 2, and ten suites' literal-prefix fixtures: `tools/workflows/unattended-build.test.sh` 32, `tools/workflows/check-verifier-fanout.test.sh` 10, `tools/memory-tree/check-memory-hygiene.test.sh` 8, `tools/govkit/selftest.py` 7, `tools/run-gates/adopt-run-gates.test.sh` 7, `tools/workflows/check-review-join.test.sh` 4, `tools/unattended/check-unattended.test.sh` 3, `.githooks/pre_push_bar_selftest.py` 2, `tools/check-wiring.test.sh` 1, `tools/unattended/adopt-unattended.test.sh` 1
- AC5 — in a scratch clone with `tools/hooks/agent-cap.js` moved to `scripts/agent-cap/` and a matching receipt row, `bash tools/workflows/check-review-join.sh` and `bash tools/workflows/check-verifier-fanout.sh` resolve the hook at `scripts/agent-cap/agent-cap.js` and exit 0. The same two gates at `3b68b495` in that clone refuse naming no agent-cap.js
- AC6 — in the same clone `python tools/settings-merge.py --selftest` passes, and wiring a copy of the settings file writes `scripts/agent-cap/agent-cap.js`. At `3b68b495` the merge refuses, naming `tools/hooks/agent-cap.js` as missing. The first cut, `d2df966d`, let gov's declared top-level prefix outrank the receipt and named the moved kit under `tools/`; `44ae083e` fixed it
- AC7 — this ledger, under `memory/builds/aRepatriatedFork/build/`, records no whole-suite count: the executed counts of the moved suites are the main loop's to record, per the criterion's permission clause. What this pass observed: every edited suite's derivation header, probed beside the suite, resolves each sibling to the directory it always named; `resolve-python.test.sh`'s parity section, sliced, runs 116 arms green before and after its own commit, and its count rises by one arm per new inline copy by construction. `corpus_ids.py --selftest` holds 61 arms and `gotchas.py --selftest` 25, before and after
- AC8 — `git grep -nE 'tools/(govkit|unattended|run-gates)/' -- .githooks/gate-env.sh WIRE-INTO-PROJECT.md` finds nothing, and `python tools/govkit/check_runbook_parity.py` exits 0 at its pin of 18
- AC9 — `bash tools/check-kit-versions.sh` exits 0 with 16 declared carriers, and `python tools/govkit/govkit.py epoch --base 6830f257` is clean for every entry, as it is at `--base f8fdd873`. Eight kits moved: review-harness and tier2-review 1.21, unattended 1.46, memory-tree 2.109, codebase-map 1.18, check-wiring 1.17, settings-merge 1.13, kickoff-manifest 1.13 and playbook-render 1.16

Other direct checks: `check-wiring.sh --check` prints the same verdict lines before and after over
gov. govkit's subject-floor probe, on a scratch target that homes run-gates by a per-entry `kit`
answer with a 1.0 runner, withholds `subject`, where the probe at `3b68b495` emitted it. The
install-prefix self-test's slice of arms 1 to 8, the consumer, D3 and the vendor-prefix arm fails 9
arms at `3b68b495` and 3 on the built tree, and those 3 fail at `3b68b495` too: arm 7, the consumer
fixture's liveness, and the vendor-prefix arm, whose arm-3 population reads gov's literal prefix.
Those are owed to the main loop's whole-suite run, not to this unit.
