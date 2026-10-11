# TOOL-aFrugalTurnstile-9 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-9

No merge bar, no runner and no self-test suite ran for this ledger. One scratch script under a short
temp root built the §6 fixture fresh per case, in the suite's in-place shape: a bare origin, the
env-driven stub lander, a stub bar writing `GATE_FULL` and `GATE_BASE` to a file outside the repo,
the case's `.githooks/gate-env.sh` committed and pushed as R, and `core.hooksPath` at a stub
`pre-push` that records its argv and prints the case's decision. Each case ran `--close tRun` once
per driver, the drivers extracted whole with `git archive` at `bef97330` and at `4f2b42c5a`, eight
fixtures at a time. At base the hook was never asked and the bar always saw `GATE_FULL=1`, so AC1 to
AC4 and AC7 were RED there; AC5, AC6 and AC8 are no-change controls and held at base as they do at
HEAD. At HEAD all eight were GREEN. AC5 as written compared against base and could not hold, since
the base predates TOOL-aFrugalTurnstile-3's record line; it was re-run against the parent driver at
`ab2851125` and amended. The close still owes the new arm block in
`tools/unattended/unattended.test.sh`, which covers AC1 to AC5 and AC7 and was not run, and every §7
leg; no suite arm covers AC6 or AC8, which this fixture alone observed.

**Evidences:** TOOL-aFrugalTurnstile-9
- AC1 — `pre-push --decide answered 'full stale'` — at HEAD the argv file held `--decide`, the close's HEAD and R; the bar saw `GATE_FULL=1` and no `GATE_BASE`; `gate-bar-green` read `kind full`; the line was printed. At base the argv file was absent and no record was written.
- AC2 — `gate-bar-green.scoped` — at HEAD the bar saw `GATE_FULL` unset and `GATE_BASE` equal to R's full sha, and `gate-bar-green.scoped` read `kind scoped` with that base while `gate-bar-green` stayed absent. At base the bar saw `GATE_FULL=1`.
- AC3 — `met without a bar` — at HEAD the bar's environment file stayed absent, the output named `gate-bar-green@1234abcd`, the close printed `close OK`, and the `gates-run:` line was empty before and after. At base the bar ran with `GATE_FULL=1` and a `gates-run` fact was written.
- AC4 — `did not answer with one decision line` — at HEAD each of `maybe`, two lines, an empty answer, `scoped deadbeef` and a hook exiting 1 printed that line and ran the bar with `GATE_FULL=1`; with the hook removed the output carried `no pre-push hook at` and the bar ran full. At base neither line appeared.
- AC5 — amended rev-4 — the `unattended: gates-green` lines are compared with the driver at `ab2851125`, masking run ids and 8-hex short shas; observed identical, with the hook's argv file absent and the bar at `GATE_FULL=1`.
- AC6 — `GATE_POLICY_FILE` — with `GATE_POST_MERGE=local` committed only on the run branch, and again with the conf's `GATE_POLICY_FILE` declaring `local` over an undeclared hook file at R, the argv file was absent and the bar saw `GATE_FULL=1`, at HEAD as at base.
- AC7 — `outside 'local ci'` — at HEAD the argv file was absent, the bar saw `GATE_FULL=1`, and the line named `yes`. At base the line was absent.
- AC8 — `LANDER_MODE=primary` — with R declaring `local`, the argv file was absent and the bar's environment read `GATE_FULL` and `GATE_BASE` both unset, equal to the base driver's and the parent driver's.
