# TOOL-dGroundRules-24 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-24

No merge bar, gate leg or self-test suite ran in this pass, and no function was minted, so the naming
lexicon had nothing to answer. The case was observed by scratch probes that import `check_policy`
and call `run_fixture("adopter-fresh-target")` in process. Each probe builds its target under the
system temp directory and runs `govkit.py apply` there as a subprocess. The two red probes made
their break in an in-memory copy of the case's source, never on disk. The red-first observation of
the `New arm:` line, and the `policy fixtures` leg itself, are left for the close.

**Evidences:** TOOL-dGroundRules-24
- AC1 — `apply` — on the built tree the probe printed "apply --kits policy exited 0 into its target
  · the 7 file(s) under tools/ are each a receipt row's path, and its 7 engine or seed row(s) are
  each present · no stray or missing receipt path". It then printed that every arm graded clean or
  announced, with the install staged and once it is committed, and that the README table names
  exactly the 5 arms of `ARMS`: 33 assertions executed, 0 wrong, exit 0. The policy kit's `kit.toml`
  declares no `requires`, so the closure was `policy` alone. A copy whose `--kits` named
  `no-such-kit` printed "WRONG: govkit.py apply --kits policy exited 2, so nothing was installed to
  grade", followed by govkit's refusal, and ran no adopter: 7 assertions, 1 wrong, exit 1. Each arm
  green with every unit built is the close's observation, as the criterion's permission line says.
- AC2 — `WRONG` — a copy that planted `tools/policy/zz-planted.txt` after `apply` and before the
  receipt compare printed "WRONG: tools/policy/zz-planted.txt is under the tool root and is no
  receipt row's path (stray)": 34 assertions, 1 wrong, exit 1.
- AC3 — `govkit.py` — a scratch copy of the source tree holding `tools/policy/` and no `tools/govkit/`
  printed "WRONG: no deployer to install with: looked for govkit.py at
  <copy>/tools/govkit/govkit.py, under this kit's tool root": 7 assertions, 1 wrong, exit 1. No
  target was installed.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: --fixture adopter-fresh-target. stray plant -> `WRONG: tools/stray-planted.txt is under the tool root and is no receipt row's path (stray)`; govkit.py deleted -> `WRONG: no govkit kit holding govkit.py in this install`. GREEN `223 assertion(s) executed · 0 wrong`.
