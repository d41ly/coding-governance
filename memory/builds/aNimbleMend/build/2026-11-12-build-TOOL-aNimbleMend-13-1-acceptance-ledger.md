# Acceptance ledger — TOOL-aNimbleMend-13

**Serves:** journal TOOL-aNimbleMend-13

Built against spec rev-2 in one pass commit. Each line is a probe of the changed code the builder made in the pass. No suite, gate leg, pass-leg run or bar ran in the pass. Owed to the main loop at the close: AC1, AC2, AC7 and AC9, the legs of the spec's Gates section, and the RED-first observation of the spec's two new arms, in `tools/run-gates/run-gates.test.sh` (arm 14a2) and `tools/run-gates/run-gates.evidence.test.sh` (the kit-subject arms).

**Evidences:** TOOL-aNimbleMend-13
- AC1 — `gate-pass-legs.txt` — NOT OBSERVED in the pass: a role agent's hook refuses the pass-leg runner, so the main loop owes the run. Stood in for by two probes: the shim run as `--leg` with the variable exported printed `unset` under a `bash` head and under a `python3` head, and `--report` printed no `selected` line for the held leg.
- AC2 — `gate-pass-legs.json` — NOT OBSERVED in the pass: only a pass-leg run writes the file, so the main loop owes it. Stood in for by the adapter's own filter expression run over the tracked manifest, which printed two equal counts above zero and kept every key but `argv` of every row.
- AC3 — `kit-subject kit-subject` — the criterion's command printed exactly that line.
- AC4 — `would hold it` — the criterion's command printed a list of one string holding the phrase.
- AC5 — `python tools/run-gates/pass_legs.py --check` — after `--apply`, which took the field off one row of the manifest, `--report` opened the resolver leg's line with `kit-subject`, `--check` exited 0, and `--budget` exited 0 on a last line opening `pass-budget:` that names the budget.
- AC6 — `GOVKIT_RERENDER` — the criterion's grep over the descriptor printed 1.
- AC7 — `python tools/govkit/govkit.py selfcheck` — NOT OBSERVED in the pass: the command is a leg's own, so the main loop owes it. Stood in for by the selfcheck's sentence patterns copied into a probe over the kit's tracked files, which named no sentence.
- AC8 — `remove_pass_field` — the grep for `def strip` printed 0, the grep for the new name printed 2, and the diff of `.lexicon.conf` against HEAD printed nothing before the commit.
- AC9 — `over pin` — NOT OBSERVED in the pass: the command is a leg's own, so the main loop owes it.
- AC10 — `pass-leg-evidence.txt` — the grep for the old two-file sentence printed 0 and the grep for the evidence file's name printed 1.
- AC11 — `filtered list and not the manifest` — the three greps printed 0, 1 and 1, in the criterion's order.
