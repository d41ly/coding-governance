# TOOL-dWitnessedBar-71 deviation 712 — the gov suite's shell-role row regains the TAB unit 70 dropped, so the resolver suite's widen can run

**Serves:** deviation TOOL-dWitnessedBar-71

- **Departs from:** `TOOL-dWitnessedBar-71@rev-3 [Files touched]`
- **Hand-off:** spec-to-code
- **Before:** §4 Files touched has the pass widen the resolver suite's row of `memory/project/shell-role.txt` and touch no other row of it.
- **After:** the pass also restores the TAB between the count `715` and the sha `fb46531ffc39c0584fbf3cd8d3ac37e2d2108306` in the `tools/run-gates/run-gates.gov.test.sh` row, which `0890c99d1` wrote as one field; the count, sha and `widened:` stamp are unit 70's, unchanged.
- **Cause:** builder discovery
- **Reason:** `ratchet.py widen shell-role` reads every row of the home before it writes one, and refused with exit 2 naming line 107 as not the key's fields, so the resolver suite's row could not be widened as §4 states while the malformed row stood. The repair is the one byte the row lacks; the shell-role seed still measures the gov suite at 715.
- **Evidence:** `python tools/memory-tree/ratchet.py widen shell-role --key tools/lib/resolve-python.test.sh ...` exited 2 with `memory/project/shell-role.txt: line 107: not the key's fields, a count and every trailing field, TAB-separated`, and exited 0 writing `2026-11-21-build-TOOL-dWitnessedBar-71-widen-13` after the TAB was restored; `sh_hygiene.py --shell-role --measure . ':!memory/'` printed `tools/run-gates/run-gates.gov.test.sh` at 715. (DERIVED from the builder's probe)
- **Risk:** editorial
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dWitnessedBar-71
