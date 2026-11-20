# TOOL-dWitnessedBar-63 deviation 632 — two gov-canary arms red at the base repaired, and the scrub arm's comment spells the fold

**Serves:** deviation TOOL-dWitnessedBar-63

- **Departs from:** `TOOL-dWitnessedBar-63@rev-4`
- **Hand-off:** spec-to-code
- **Before:** §6 AC2 has the scrub parity arm fail naming `GATE_SELECTION` and `PM_SCRUB` over a copy with `GATE_SELECTION` cut, and S2 reads `Present at HEAD` for the arm's comment naming post-merge's fold `${PM_SCRUB//$'\n'/ }`; §7 lists `run-gates gov canary` and names no change to the verdict backends' plant loop beyond the `key-no-tab` plant. At the base the copy's `sed` script and its file name were one word, `'…/\1/'"$bsp_pm"`, so `sed` refused the script and wrote an empty copy, the arm named `PM_SCRUB reads empty` and never `lacks GATE_SELECTION`, and the gov canary failed there; the comment said "the fold post-merge itself applies" without spelling it; and the plant loop owed `peer-no-ssh-keygen` exit 1 while unit 62's AC26 scenario, owed exit 0, had become the plant's last, so the plant exited 0 and the loop failed it. (DERIVED from the base's `tools/run-gates/run-gates.gov.test.sh#check_bar_scrub_parity` and `tools/run-gates/verdict_backends.py#run_fixture`)
- **After:** the copy's `sed` takes its file as a separate word; the arm's comment spells `${PM_SCRUB//$'\n'/ }`; the loop owes `peer-no-ssh-keygen` exit 0, the last owed exit `run_fixture` returns, now that AC12's sweep scenario is that last one.
- **Cause:** builder discovery
- **Reason:** AC2 is observed only through a copy that holds `PM_SCRUB` less one name, and the brief makes any red other than the hygiene leg's this unit's to fix; the plant's exit is the last owed exit by `run_fixture`'s own rule, and AC12 extends that very scenario.
- **Evidence:** the base's line, run as written over a scratch path, printed `sed: -e expression #1, char 48: unknown option to 's'` and wrote 0 bytes; the repaired copy, through the arm cut by its awk range over the shipped hook and driver, printed `PM_SCRUB 29` and `PM_SCRUB in … lacks GATE_SELECTION`, exit 1; `python verdict_backends.py --fixture --plant peer-no-ssh-keygen` in `tools/run-gates/` held both scenarios and exited 0. (DERIVED from the builder's probe)
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dWitnessedBar-63
