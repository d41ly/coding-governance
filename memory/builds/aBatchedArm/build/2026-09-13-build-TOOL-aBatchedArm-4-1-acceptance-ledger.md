# TOOL-aBatchedArm-4 — acceptance ledger

**Serves:** journal TOOL-aBatchedArm-4

Two commits: `3bb5c8a2` (S1 alone) and the S2-through-S8 commit this record rides in. Every arm
named below was observed RED against a staged break before it was kept, and the observation that
saw it is written beside it. The suite ran at `SELFTEST_INNER_WIDTH=8`; 43 arms before, 53 after.

**Evidences:** TOOL-aBatchedArm-4
- AC1 — `bash tools/run-gates/run-selftests.test.sh` — arm `a numeric-ratio token such as --shard 1/8
  is admitted by --check` is green on a row whose argv carries `--shard 1/8`, and arm `a DIGIT-LED
  untracked path is still refused by name` reds `--check` naming `1abc/2suite.sh`. RED observed both
  ways: under the glob `[0-9]*/[0-9]*` the digit-led arm got rc 0 and `declaration clean` over an
  untracked path; with no predicate at all the ratio arm got `names '1/8', which git does not track`.
  The discriminating path leads with a digit on BOTH sides of the slash — `1abc/suite.sh` passed
  under both predicates, because the glob's second half wants a digit too. On the real tree
  `bash tools/run-gates/run-selftests.sh --check` printed `declaration clean — 61 row(s)`.
- AC2 — `bash tools/run-gates/run-selftests.sh` with no mode — arm `a run with NO mode REFUSES naming
  both spellings, and executes no suite`: rc 2, the line `declares --serial or --pooled`, and the
  fixture's `suite-mark.sh` left no `ran.marker`. RED observed with the refusal staged out: rc 99,
  the marker present, the serial header `2 suite(s), declared total 2 minutes` printed — the silent
  serial default, seen running.
- AC3 — `bash tools/run-gates/run-selftests.sh --check` on the real tree: rc 0, 61 rows; arm `--list
  takes no mode and is not refused`: rc 0; arm `a --kit filter matching nothing REFUSES` under
  `--serial --kit tools/nowhere`: rc 2 naming `so this run graded NOTHING at all`, so the liveness
  refusal at the old `:383` still fires by name after the mode refusal and is not shadowed by it.
- AC4 — amended rev-5 — the pooled clause read O as the lesser of the resolved width and the row
  count; the runner sets outer to the resolved width and never clamps it to the population, so the
  clause now reads what `peak concurrency P of outer O` can print. OBSERVED over a fixture, the real
  `run-unattended-gates.sh` and the real shared runner over three stub suites and five stub checks
  (`ac4-fixture.sh`, scratch): bare, `--selftests` and `--all` each rc 2 naming `--serial or --pooled`
  with zero suite rows printed; `--serial` differs from the OLD pair's bare run — `git show
  HEAD:` of both files — by exactly one line, the summary gaining ` · serial`, with the seconds column
  masked; `--selftests --serial` and `--serial --selftests` are identical to it; `--pooled` printed
  ` · pooled, 3 cost verdicts withheld` where 3 is what `run-selftests.sh --kit tools/unattended
  --list` counts in that fixture, and `peak concurrency 2 of outer 2` on a width-2 fallback host;
  `--checks` ran 5 with no mode, no refusal and no token; `--all --serial` ran 8 with the token.
  Failing case on the REAL tree: with the kit runner's refusal staged out, the bare form dispatched
  `run-selftests: 7 suite(s), declared total 324 minutes` and started a suite before a 25 s timeout
  cut it. NOT observed: the 12657 s serial pass and the pooled pass over the seven real rows — priced
  by this criterion itself, and the brief names the pooled one as unit 3's measurement.
- AC5 — `bash tools/run-gates/run-selftests.test.sh` — the pair over one suite, `suite-mid.sh` at
  5 s against a budget of 4: arm `under --serial a breaching suite gets OVER BUDGET` rc 1; arm
  `under --pooled the SAME breaching suite is 'cost withheld'` rc 0 with no `OVER BUDGET` line. RED
  observed twice: the pool made to grade a budget (`OVER BUDGET ... (STAGED BREAK)`, rc 1 on the
  pooled arm) and the serial loop's comparison disabled (rc 0 on the serial arm and on the older
  over-budget arm beside it).
- AC6 — `bash tools/run-gates/run-selftests.sh --help` and `run-unattended-gates.sh --help` exercised
  and grepped for `usage:`, `no flag`, `no-flag`, `(default)`, `--serial`, `--pooled`: every hit
  names a mode and none spells the bare form or `(default)`. The three remedies that interpolate
  the runner's own path, exercised by arm: `:412` via `SELFTEST_TIMEOUT_BIN=definitely-not-a-binary
  --pooled` prints `Use --serial, which reports each suite`; `:746` via a completed `--pooled` run
  prints `run the serial mode: bash tools/run-gates/run-selftests.sh --serial`; `:758` via a RED
  `--pooled` run prints `the serial re-run: bash tools/run-gates/run-selftests.sh --serial`. The
  remedy-text arm was RED when `:412` was staged back to `Use the no-flag mode`. Read as text:
  `SESSION-KICKOFF.md:132` spells `run-selftests.sh --serial`, `:168-169` spells
  `--selftests --serial`, `tools/unattended/README.md:66` spells `run-unattended-gates.sh --serial`.
- AC7 — read as text after the commit, each names `--serial` beside `run-unattended-gates.sh`:
  `.githooks/gate-env.sh:27` (`--selftests --serial`), `tools/unattended/kit.toml:125` (`--serial`)
  and `:126` (`--all --serial`), `run-unattended-gates.sh:27` (`--selftests --serial`, the script's
  bare name so the carried-literal count does not rise) and `:231` (the line that was `:203`,
  `--selftests --serial`), `AGENTS.md:519` (`--serial`). None spells the bare form.
- AC8 — `bash tools/check-template-size.sh AGENTS.md` on the staged tree: `64503 / 64512 bytes
  (9 under)`. The edit at `AGENTS.md:519` is the nine bytes of ` --serial` and nothing else.
- AC9 — `bash tools/check-install-prefix.sh` on the staged tree: `carried-prefix clean — 135 recorded
  file(s), 35 hand-justified, none rising`; `tools/install-prefix-carried.txt` untouched, the
  `run-selftests.sh` row still 6 and the `run-unattended-gates.sh` row still 4. Every rewritten usage
  line edited its literal in place; the one new mention at `run-unattended-gates.sh:27` is the bare
  script name, which the predicate does not count.

## What this ledger does not evidence

The seven real unattended rows were not run under either mode. AC4 prices the serial pass at
12657 s and the pooled pass at 27200 s, the brief forbids both here, and unit 3 owns the pooled
measurement. What is evidenced is the plumbing — the refusals, the pass-through, the token, the
parsed count — over a fixture where the same two scripts run in seconds.

Seen incidentally and not this unit's: `unattended adopter e2e` is RED, 22 `FAIL` lines, on a clean
detached checkout of the branch tip before this unit's code. It is the red `TOOL-aQuenchedHarness-9`
already records for that suite at BASE.

The kit runner still has no self-test of its own. Spec §3's last item says why and what it owes.
