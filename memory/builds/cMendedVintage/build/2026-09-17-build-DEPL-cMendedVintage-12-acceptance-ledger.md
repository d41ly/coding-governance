# cMendedVintage — the acceptance ledger for unit 12

**Serves:** journal DEPL-cMendedVintage-12

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar, no self-test suite and
no `*.test.sh` ran in this pass. Every observation below was taken by running the real engine against
scratch fixture targets at the shell — once against the pre-change engine and once after — so every
criterion is answered by a fixture and none by a suite.*

## The one thing worth reading twice

**The defect is live and it was reproduced before a line was written.** Two scratch fixtures were
built from the same descriptor, one declaring `inert = ["memory-tree"]` and one declaring nothing at
all. Against the pre-change engine their `apply --write` output was byte-identical line for line,
both printed
`CONFIGURE memory-tree: adopter exit 1 — seed-and-stop [accepted stop]`
and both ended with `.memory-tree.conf` present in the tree. The posture the operator wrote down was
flipped by the verb every runbook recommends as the fallback, and nothing in the output said so.

**The spec proposed a function name the naming declaration refuses, and the declaration was asked
rather than reasoned with.** `--suggest inert_kits` answered that `inert` is in no row of the table,
that no canon cluster holds it, and that this is therefore a scoping question rather than a spelling
one. `--suggest read_inert_kits` answered OK against the same cell. The name is amended at rev-2. The
two neighbours rev-1 cited as precedent, `lf_pins` and `tracked`, are offenders that predate the
prescriptive table, not precedents for adding to it.

**S3's branch is load-bearing and its failing case was observed, not assumed.** With
`or row.get("kit") in inert_declined` removed from the OBSERVE condition and nothing else changed,
the inert fixture's run exits 1 and prints four findings reading
`is absent after its adopter ran — the adopter owns those bytes and did not write them`
about an adopter that never ran. The break was staged, the RED read, and the line restored.

**The decline sits ahead of the hole-blocked skip, not only ahead of the argv resolution.** Both
reach the same `continue`, so ordering them the other way would silently swallow S4's line for any
kit that is inert AND hole-blocked. S2 is amended at rev-2 to say so.

**No shipped document in this repo spells the `inert` key.** The spec's §5 promised to correct a
sentence naming the reader; there is no such sentence to correct, in the deployer runbook or
anywhere else. The bullet is withdrawn at rev-2 rather than answered with a doc this unit did not
scope.

**AC4's fixture needed a precondition the spec did not state.** `update`'s decline loop iterates
`touched_kits`, which is empty for a target whose rows are all current — so backdating the receipt's
`gov_commit`, tampering a row digest and drifting a landed file all produced `0 argv run, 0 declined`
and proved nothing. Deleting one landed engine file and committing puts the kit in that set, and the
decline then prints. The precondition is added to the criterion at rev-2.

**Evidences:** DEPL-cMendedVintage-12

*Every token below sits on its own bullet's FIRST physical line, deliberately: hygiene check 23
joins an answer's backticked tokens to the criterion's per PHYSICAL line, so a token pushed onto a
continuation belongs to no line and its criterion grades as answered by nothing.*

- AC1 — OBSERVED — `inert` — a fixture declaring `inert = ["memory-tree"]` and taken through
  `apply --target <fixture> --write` prints
  `CONFIGURE memory-tree: DECLINED — the target holds this kit INERT`
  and `.memory-tree.conf` is ABSENT from the fixture afterwards. The tree is the observable, not the
  line: the RED-WHEN is a decline printed after the argv resolution, which would satisfy a
  stdout-only assertion while the posture had already been flipped. The same run's exit code is 0.
- AC2 — OBSERVED — `inert` — the same descriptor with the `inert` key removed and nothing else
  changed runs the adopter, prints the `seed-and-stop [accepted stop]` line unchanged,
  and leaves `.memory-tree.conf` present. This is the direction the spec names as the one nobody
  tests, and both fixtures were built by one function differing in one line.
- AC3 — OBSERVED — `rendered` — the declined kit ships four `rendered` rows, and each absent
  destination is reported
  `not rendered — 'memory-tree' is held INERT by this target, so its adopter never ran`
  with the run still exiting 0. The RED-WHEN was staged and read: with the inert set out of that
  branch the same run exits 1 and names an adopter run that never happened. Folding into
  `stopped_ok` is refused by its own arm — the string `stopped at an accepted outcome` appears
  nowhere in the inert fixture's output.
- AC4 — OBSERVED — `update --target <fixture> --write` — the same fixture, applied, committed, then
  stripped of one landed engine file so the kit enters the run's touched set, prints
  `DECLINED memory-tree: the target holds this kit INERT`
  from `update`'s own decline, which now calls the shared reader. The structural half agrees:
  `deploy.get("inert")` occurs exactly once in the engine, inside `read_inert_kits`, and
  `read_inert_kits` has exactly two call sites. AMENDED rev-2 for the fixture precondition, logged
  at §9.

## OWED

- **The gate-side encoding of AC1 through AC3.** Five arms tagged `[-12]` land in this unit's write
  set and only the govkit self-test suite can execute them. That suite is a merge-bar leg and no
  gate, suite or bar ran in this pass. They are NOT asserted by construction: the block's source was
  extracted from the shipped file verbatim between its banner and the next comment, dedented, and
  executed with the suite's own `make_target`, `run`, `check` and `DEPLOY_FULL` bound, and all five
  reported `ok`. What is owed is the suite RUN — that the block still holds in the suite's own
  scope, with the suite's own `tmp`, and that the arms it sits beside are still green.
- **AC4 has no gate-side arm and that is deliberate.** Its fixture needs an applied, committed target
  with one landed file deleted, which is three more fixture steps than the criterion's value: the
  question AC4 actually asks is whether one reader serves both consumers, and that is answered
  structurally by a single occurrence of `deploy.get("inert")` in the engine. Filing a suite arm for
  it would buy a slower copy of a grep.
- **The merge bar is owed whole.** `govkit selftest`, `govkit selfcheck` and the acceptance matrix are
  this unit's declared gates and none ran here. Two checkers that are not suites DID run and are not
  owed: the carried-prefix scan reports `carried-prefix clean` over its recorded files, and the
  naming checker exits 0 with its verb-offender pin unmoved, which is the pin the spec's original
  function name would have raised.
- **No other unit's owed criterion is discharged here.** This unit's §3 declares no edges in either
  direction, and nothing measured during the build contradicted that.
