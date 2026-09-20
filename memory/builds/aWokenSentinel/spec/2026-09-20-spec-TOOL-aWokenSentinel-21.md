# TOOL-aWokenSentinel-21 — the build harness's suite joins the declared self-test population: a held leg, a budget row, a registry exemption and a shrink-only `FLOOR_ASSERTIONS`, so its supplied-subject fixtures are an executed arm

**Status:** SPECCED · rev-2 · 2026-09-20 · node a · Tier-2 · base 830c46e8 · streams tooling · order 21

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-prompt-TOOL-aWokenSentinel-21-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-21-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-21-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-21-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H1 (round 3, raw id 26): `TOOL-aWokenSentinel-15` placed its dirty-tree compare
after and outside the resolver branch of `tools/workflows/unattended-build.js`, where it ran over
caller-supplied `{path, blob}` subjects too, so `undefined !== blob` read every supplied subject as
dirty and the harness suite's fifteen supplied-subject fixtures threw `Commit the fold` for a fold
that does not exist — and nothing would have run that suite to see it. The placement is folded at
spec 15's rev-2. The CLASS is that `tools/workflows/unattended-build.test.sh` is the one suite this
build edits that no runner executes: it sits on no `tools/gate-legs.json` leg, no
`tools/run-gates/selftest-budgets.txt` row and no floor, so a throw over fifteen of its fixtures reds
nothing anywhere. This unit puts the suite where its three siblings in the same kit already are: a
held `chunk: selftests` leg, a budget row the on-demand runner reads, a `[[exempt_leg]]` row in the
govkit registry beside the siblings', and a shrink-only `FLOOR_ASSERTIONS` on its executed count, so
the fixtures are an executed regression arm for unit 15's compare and for every later edit of the
harness, and a lost arm reds rather than shrinks.

## 2. Scope (IN)

- **S1** — `tools/gate-legs.json` gains one leg in the shape of `tier2-review self-test`: name
  `unattended-build self-test`, argv `bash tools/workflows/unattended-build.test.sh`, `guard`
  `tools/workflows/`, `chunk` `selftests`, `subject` `kit`, and a `ceiling` DERIVED at the pass as
  the budget of S2 times the `sweep-ceiling-factor` the budgets file declares, so the bar's hang
  bound and the on-demand runner's agree. The plain bar HOLDS it, as it holds every kit self-test
  by the 2026-08-23 owner ruling; `GATE_SELFTESTS=1` and `run-selftests.sh --kit tools/workflows`
  run it. Observed by AC1.
- **S2** — `tools/run-gates/selftest-budgets.txt` gains the row `unattended-build self-test` with
  an empty argv column, so the argv is taken from the leg, and a budget DERIVED at the pass: the
  static count of `run_wf` sites in the suite (100 at this unit's base, by `grep -c 'run_wf '`)
  times the seconds one `run_wf` invocation costs, measured by the pass the way spec 15's AC1 runs
  one, times 1.5, floored at 60 — the `unattended gate-guard selftest` row's shape, whose reading
  column says the pass that wrote it may not run the suite and the main loop's first VERIFYING
  reading is the one it is re-derived from. Observed by AC2.
- **S3** — `tools/govkit/registry.toml` gains an `[[exempt_leg]]` row named
  `unattended-build self-test` with the `why` its three sibling rows carry, the suite's filename
  substituted, because the suite is already withheld from adopters by
  `tools/workflows/kit.toml`'s `project-owned` rule and a held leg claimed by no descriptor must be
  exempted by name or `govkit.py selfcheck` reds. Observed by AC3.
- **S4** — The suite gains the sibling suites' floor block directly above its `--- $n arms, exit
  $st` line, so the compare runs BEFORE the summary the way `tools/unattended/gate-guard.test.sh:455`
  to `:456` orders them: a `FLOOR_ASSERTIONS=<n>` pin authored at ten percent under the static
  count of its `same`, `has` and `hasnt_` sites (317 at this unit's base, by
  `grep -cE '^\s*(same|has|hasnt_) '`), rounded down and never lower, the authoring rule in its
  comment, the compare that prints `FAIL executed $n assertions against a floor of
  $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent` and sets `st=1`, and beside it the
  after-exit self-read spec 19 S5 writes for the adopter suite, anchored on this suite's spelling:
  `[ "$(sed -n '/^exit \$st$/,$p' "$0" | grep -cvE '^\s*(#|$)')" = 1 ] || { echo "FAIL a line
  follows the terminal exit and can never run"; st=1; }`. The suite's own `n` counter and its
  summary line are unchanged; the `PASS ($n assertions)` line that follows the summary is
  `TOOL-aWokenSentinel-27`'s. Observed by AC4 and AC5.
- **S5** — The floor's failing case and the self-read's are observed at the pass without running
  the suite: the block is extracted with `sed -n` and evaluated by `bash -c` with `n` one below
  the pin, printing the `FAIL executed` sentence, and with `n` at the pin, printing nothing; the
  self-read line is evaluated with `$0` pointed at a copy of the suite with one non-comment line
  appended after `exit $st`, printing `FAIL a line follows the terminal exit`, and at the
  unmodified suite, printing nothing. Observed by AC5.

## 3. Non-goals (OUT)

- **No run of the suite inside the pass.** The build-level rule forbids it and the `gate-guard`
  hook refuses it; the pin is authored from the static count and confirmed by the first green
  under `GATE_SELFTESTS=1` or `run-selftests.sh --kit tools/workflows`, as the gate-guard suite's
  own floor was.
- **No change to the close's frozen-clone command.** `run-unattended-gates.sh` is the unattended
  kit's runner and reads the unattended kit's rows; this suite is the workflows kit's, and the
  build-level rule for this round names the second runner invocation the close adds beside it.
- **No change to any arm.** The floor counts what the arms execute; the compare inside the resolver
  branch and the two arms that observe it are unit 15's.
- **No enrolment in the meta-gates that grade a manifest leg.** `testsuite counts (every bar
  self-test prints one)` wants the `PASS ($n assertions)` line, `codebase-map coverage +
  freshness` wants the `gate-legs` key claimed in a dossier with the map re-rendered, and
  `govkit selfcheck` wants a row in the GENERATED `tools/govkit/subject-pins.tsv`; all three are
  unguarded and red from this unit's commit until `TOOL-aWokenSentinel-27`, ordered after it,
  enrols the leg in each. The bar runs once at the close, so the interval is a records fact and not
  a red bar. The rev-1 non-goal refusing the `PASS` line is withdrawn: the line is the shape the
  counts leg reads, not a rename of the summary.
- **No kit-wide after-exit loop.** `TOOL-dUnstalledConvoy-19` asks for the structural arm in every
  suite that ends with a terminal `exit`; S4 writes this suite's one-liner beside the floor, as
  unit 19 wrote the adopter suite's, and the loop over the suites this build does not touch stays
  the backlog row unit 19 hands off.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-15` — the two arms that unit adds to the suite and the
  compare they observe; the floor's static count at the pass includes them, which is why this unit
  is ordered after unit 15.
- **consumes-from** `TOOL-aWokenSentinel-19` — the floor block and its authoring rule as that
  unit wrote them for the adopter suite: a static count at ten percent headroom, confirmed by the
  first green, which this suite's block copies; and the hand-off of this suite's floor, which
  that unit's §3 makes to this one.
- **consumes-from** external — the three sibling legs of the workflows kit in
  `tools/gate-legs.json` (`verifier fan-out self-test`, `tier2-review self-test`,
  `review-join self-test`), their budget rows, their `[[exempt_leg]]` rows in
  `tools/govkit/registry.toml`, and the `project-owned` rule at `tools/workflows/kit.toml:32` that
  already withholds this suite from adopters.
- **hands-off** `TOOL-aWokenSentinel-27` — the `PASS ($n assertions)` line under the summary, the
  `gate-legs` claim in `memory/map/features/review-harnesses.md` with the re-rendered map, and the
  `subject-pins.tsv` row: the three meta-gate enrolments the new leg owes, each observed by its own
  checker there.
- **hands-off** external — the kit-wide after-exit loop `TOOL-dUnstalledConvoy-19` asks for, which
  unit 19's backlog row carries for the `*.test.sh` this build does not touch; this suite's own
  self-read is S4.

## 4. Design

### The leg, the row, the exemption

```
{ "name": "unattended-build self-test",
  "argv": ["bash", "tools/workflows/unattended-build.test.sh"],
  "guard": ["tools/workflows/"], "chunk": "selftests", "subject": "kit", "ceiling": <2 x budget> }
```

The guard is `tools/workflows/` alone, as `tier2-review self-test` has it: the suite evaluates
`unattended-build.js` and `unattended-unit.js` with stub hooks and reads the driver only for its
refusal set, so a change under the workflows kit is what selects it and nothing else does. The
budgets row is `unattended-build self-test<TAB><budget><TAB><TAB><reading>`, the empty third column
meaning "take the argv from the leg", which is how every sibling row is written; the reading column
states the derivation — `run_wf` sites times one measured invocation, x1.5 — and that the first
VERIFYING reading re-derives it. The registry row is the sibling `[[exempt_leg]]` text with
`unattended-build.test.sh` in place of `tier2-review.test.sh`, and nothing else changes in it,
because the reason is the same reason.

### The floor block

Inserted directly above the `--- $n arms, exit $st` line at
`tools/workflows/unattended-build.test.sh:1255`, so a breach sets `st` BEFORE the summary prints it
and the summary never reads `exit 0` on the one run the floor exists for — the order of
`gate-guard.test.sh:455` to `:456`, which the rev-1 text had inverted:

```
# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not on the written one. Authored from a
# static count of the `same`/`has`/`hasnt_` sites in this file at ~10 % headroom, because the pass
# that wrote this line may not run the suite; the first green under GATE_SELFTESTS=1 or
# run-selftests.sh --kit tools/workflows confirms the executed count against it. Lower it in a
# reviewed diff or not at all.
FLOOR_ASSERTIONS=<n>
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }
# NOTHING RUNS AFTER THE TERMINAL EXIT (TOOL-dUnstalledConvoy-19): the floor cannot see an arm
# appended past `exit $st`, and neither can check-arms.py or the summary line. One grep can.
[ "$(sed -n '/^exit \$st$/,$p' "$0" | grep -cvE '^\s*(#|$)')" = 1 ] || { echo "FAIL a line follows the terminal exit and can never run"; st=1; }
```

The tail of the file then reads: this block, `echo "--- $n arms, exit $st"`, the `PASS` line
`TOOL-aWokenSentinel-27` adds, `exit $st`. The self-read counts the non-comment, non-blank lines
from the terminal `exit $st` to end of file and wants exactly one — the exit itself — so an arm a
later unit appends past it reds with its own sentence instead of hiding inside the floor's slack.

`<n>` is the static count times 0.9 rounded down — 285 from the 317 sites at base, re-derived by
the pass from the file it edits, because unit 15 adds arms before this unit's order and the count
at the pass is what binds; AC4 bounds it from below as well as above, so a pin far under the
count is red rather than merely slack. The static count is a lower bound on the executed count everywhere but
one place: the `PV-AC12` branch near the suite's end skips its sites with an announced `SKIP` when
no unattended adopter sits at `$UK`, and this repo carries one, so on this tree the sites execute
and the ten percent is headroom rather than a mask. The inline `n=$((n+1))` sites the grep does
not count only raise the executed figure above the static one.

### Why a held leg and not a bar leg

The 2026-08-23 owner ruling took every kit self-test off the plain bar; the three sibling suites are
held legs run by `GATE_SELFTESTS=1` and by `run-selftests.sh --kit tools/workflows`, and the
charter's DoD for KIT work owes the flagged bar. A leg on the plain bar would reverse that ruling
(BUILD-METHOD M3, veto 2), and a suite in neither place is what this unit exists to end. What the
held leg buys over nothing is the declared population's two-direction assertion: the
`every held leg is budgeted, every budget row resolves` leg reds the day the row and the leg
disagree, and `govkit.py selfcheck` reds a held leg no descriptor claims and no exemption names.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `unattended-build self-test` | a leg name in the manifest, a budgets row, an exemption row | no cell; not a function |
| `FLOOR_ASSERTIONS` | a shell variable in the harness suite, the sibling suites' name | no cell; not a function |

No function, key, verb or file is minted.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/gate-legs.json` | one leg beside the three workflows self-test legs |
| `tools/run-gates/selftest-budgets.txt` | one row beside `tier2-review self-test` |
| `tools/govkit/registry.toml` | one `[[exempt_leg]]` row beside the three sibling rows |
| `tools/workflows/unattended-build.test.sh` | the floor block with the after-exit self-read, above the `--- $n arms` summary |
| `memory/guides/SESSION-KICKOFF.md` | the `last-audit` re-stamp: `tools/gate-legs.json` is on the manifest's `watch` line, and `skills/session-kickoff/manifest-check.sh --staged` (C5s, the pre-commit fast leg) refuses a commit that stages a watched file without moving the stamp in the same commit |

### Alternatives rejected

- **Have spec 15's AC4 run the suite at the tip.** The audit's own interim fix. It puts a suite run
  inside a pass, which the build-level rule and the `gate-guard` hook both refuse, and it observes
  the fifteen fixtures once rather than on every later edit of the harness.
- **A budget row with no leg.** The runner accepts a row naming a tracked file; but the row would sit
  in no guard, so a change under the workflows kit would select nothing, and the `--kit` filter is
  the only route the row would have. The leg is what makes the guard exist.
- **A leg on the plain bar.** Veto 2; the ruling above.
- **Pin the floor at the executed value.** Reds on the first arm anybody legitimately removes; the
  sibling suites' discount exists for that reason and is copied.

## 5. Production-readiness checklist

- security — N/A; a manifest row, a budget row, a registry row and an integer compare.
- perf / scale — the plain bar holds the leg and pays nothing; a flagged bar pays the suite's cost,
  which the budget row declares and the ceiling bounds.
- error / empty / loading states — a suite executing zero assertions reds against any positive
  floor; a row with no leg or a leg with no row reds the declaration leg; a held leg with no
  exemption reds `govkit.py selfcheck`.
- observability — the breach sentence names both numbers; the runner names the suite on a non-zero
  exit; the declaration leg names the missing side.
- risks — a static count that overshoots the executed one reds the first flagged green; the remedy
  is a reviewed lowering with the executed count in the comment. A budget derived from one measured
  invocation may under-declare on a loaded box, which the budgets file's own header says to read by
  re-running quiet before believing.
- testing — §6; the block evaluated by `bash -c` on both sides of the pin, and greps over the three
  declarations.
- migration — additive; a new leg name, a new row, a new exemption.
- user docs — none; the block's comment and the budgets row's reading column.

## 6. Acceptance criteria

- **AC1** — When `python3 -c` reads `tools/gate-legs.json` at the tip and prints the leg named
  `unattended-build self-test`, its `argv` is `["bash", "tools/workflows/unattended-build.test.sh"]`,
  its `chunk` is `selftests`, its `subject` is `kit`, its `guard` is `tools/workflows/` and its
  `ceiling` equals the second field of the `unattended-build self-test` row in
  `tools/run-gates/selftest-budgets.txt` times the integer on that file's `# sweep-ceiling-factor:`
  line, both read by the same `python3 -c` at observation; at this unit's base the same read finds
  no such leg.
  Red when: the suite is still on no leg, which is the class; or the leg is not a held one, which
  reverses the owner ruling and lands a suite on every records-only bar; or the ceiling is any
  positive integer other than the product, which is S1's rule stated and observed by nobody — a
  ceiling of 1 would pass a presence read and kill the suite on its first flagged bar.
  figure: the ceiling is DERIVED at the pass as the budget times the `sweep-ceiling-factor` row of
  `tools/run-gates/selftest-budgets.txt`, and the criterion re-derives it at observation.
- **AC2** — When `grep -c '^unattended-build self-test	'` runs over
  `tools/run-gates/selftest-budgets.txt` at the tip it prints 1 and 0 at this unit's base, and the
  row's second field is an integer at or above 60 whose reading column names the `run_wf` site
  count and the measured seconds it was derived from.
  Red when: the leg exists with no budget, which the declaration leg reds as a held leg with
  unbounded cost; or the budget is typed rather than derived, which is a number beside nothing.
  figure: the budget is DERIVED at the pass — `grep -c 'run_wf '` over the suite, times the
  seconds of one `run_wf` invocation timed by the pass, times 1.5, floored at 60.
- **AC3** — When `grep -c 'name = "unattended-build self-test"' tools/govkit/registry.toml` runs at
  the tip it prints 1 and 0 at this unit's base, and
  `grep -c 'unattended-build.test.sh.*tools/workflows/kit.toml' tools/govkit/registry.toml` prints
  1, the row's `why` naming the suite file and the descriptor that withholds it.
  Red when: a held leg is claimed by no descriptor and exempted by nobody, which `govkit.py
  selfcheck` reds at the close.
- **AC4** — When `grep -cE '^\s*(same|has|hasnt_) ' tools/workflows/unattended-build.test.sh` runs
  at the tip it prints a count `c`, and `sed -n 's/^FLOOR_ASSERTIONS=//p'` over the same file
  prints an integer equal to `c * 9 / 10` rounded down, or at least `c * 8 / 10` where the pass
  recorded a reason in the block's comment, sitting on a line above the file's `--- $n arms`
  summary, which sits above `exit $st`; at this unit's base the `sed` prints nothing.
  Red when: the pin is above the static count, which reds the first flagged green on honest arms;
  or the pin is under `c * 8 / 10`, which is a floor a lost arm never reaches — a pin of 1 is
  the zero pin with one more character; or no pin exists; or the block sits after the summary,
  which prints `exit 0` on the breach, or after the exit, which is `TOOL-dUnstalledConvoy-19`'s
  stranded shape.
  figure: `c` is DERIVED by the grep at observation — 317 at base, PINNED as read on 2026-09-20 and
  expected to have moved with unit 15.
- **AC5** — When the floor block — the `FLOOR_ASSERTIONS=` line and the compare below it — is
  extracted with `sed -n` and run by `bash -c` with `n` set one below the pin and `st=0`, it prints
  `FAIL executed` and leaves `st` at 1; with `n` equal to the pin it prints nothing and `st` stays 0;
  and when the self-read line is run by `bash -c` with `$0` set to a copy of the suite that has
  `true` appended after its `exit $st`, it prints `FAIL a line follows the terminal exit` and
  leaves `st` at 1, and with `$0` set to the unmodified suite it prints nothing.
  Red when: the compare passes under the pin, which is a floor that cannot fail; or it reds at the
  pin, which is an off-by-one that reds every honest run; or the self-read passes on the appended
  line, which is the stranded shape unseen; or it reds on the unmodified suite, which is an
  anchor that does not match this suite's `exit $st` spelling.
  fixture: the suite copy with one appended line, made by `cp` and `printf` under a short
  `%TEMP%` path.

## 7. Gates

`every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `govkit selfcheck` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the reads and greps of
AC1 to AC4 and the extracted block of AC5. Under `every held leg is budgeted, every budget row
resolves`, the new leg and its row are the pair this unit adds; under `leg ceilings clear their
evidenced maximum`, the new leg is reported as unbacked until its first reading, which that gate
reports and does not fail on; under `govkit selfcheck`, the exemption row satisfies the
descriptor-claim check and nothing else — the subject-pin row that same gate wants, the
`gate-legs` claim the codebase map wants and the `PASS` line the counts leg wants are
`TOOL-aWokenSentinel-27`'s, and those three legs read RED between this unit's commit and that
one, which the close never sees because it runs after both. The suite itself runs under the flagged bar the charter's
kit-work DoD owes, and under the on-demand runner's `--kit tools/workflows` selection, which the
build-level rule for this round adds to the close's frozen-clone run beside the unattended kit's
own runner.

New arm: `tools/workflows/unattended-build.test.sh` · the floor compare, whose failing case is `n` under the pin, staged by evaluating the extracted block, and the after-exit self-read, whose failing case is one line appended past `exit $st` in a copy · `FLOOR_ASSERTIONS` is this unit's own pin, authored at ten percent under the static count

## 8. Open questions

none

## 9. Revision log

- rev-2 · 2026-09-20 · S4 · S5 · §3 · §4 · AC1 · AC4 · AC5 · §7 · folded spec-audit round 4:
  sibling agreement for the promoted `TOOL-aWokenSentinel-27` (H3 raw 18, 29; H4 raw 20, 30; H5
  raw 19) — the `PASS`-line non-goal withdrawn, the three meta-gate enrolments handed off by edge
  and named in §3 and §7 as red between the two passes; M3 (raw 5) — AC1 observes the ceiling as
  the budget times `sweep-ceiling-factor`, read from the budgets file; M4 (raw 6) — AC4 bounds
  the pin from below at `c * 8 / 10`; M5 (raw 31) — S4 carries spec 19 S5's after-exit self-read
  anchored on `exit $st`, S5 and AC5 stage its failing case on a copy, and the kit-wide loop
  stays the hand-off; L1 (raw 17) — the block sits above the `--- $n arms` summary so a breach
  never prints `exit 0`. Found while folding, not a report id: `tools/gate-legs.json` is on the
  kickoff manifest's `watch` line, so the pass's commit owes the `last-audit` re-stamp
  `manifest-check.sh --staged` demands, added to Files touched.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 3 as the
  promotion of H1 (raw id 26): the compare's placement is spec 15's rev-2 fold, and the class — a
  suite no runner executes — is this unit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declare a test suite in the self-test population with
a budget row, a leg and an assertion floor"` ranked `build_self_chain` in
`tools/process-monitor/scope.py` and `population` in `tools/govkit/refusal_join.py`, neither a
declaration of a suite, and reported `unscanned layers: .sh`; no Python seam fits. The seam, read
at source, is the declared population itself: the three workflows self-test legs in
`tools/gate-legs.json` (`tier2-review self-test`, `verifier fan-out self-test`,
`review-join self-test`), their rows in `tools/run-gates/selftest-budgets.txt` and their
`[[exempt_leg]]` rows in `tools/govkit/registry.toml`, the `project-owned` rule at
`tools/workflows/kit.toml:32` that already withholds this suite, and the floor block at
`tools/unattended/gate-guard.test.sh:432` to `:455` that unit 19 copies too. The recall probe's
top hits were `TOOL-aDeferredBar-4` (a budgeted `*.test.sh` with no `project-owned` claim ships to
adopters — this suite has the claim, which is why the row is safe), the aQuenchedHarness-3 spec
that wrote the twenty-one exemption rows this one joins, and aQuenchedHarness-4's AC3, which is
the declaration leg this unit's pair is graded by; no prior record declares the harness suite.

Recall terms used: `self-test suite held leg selftest-budgets exempt_leg registry FLOOR_ASSERTIONS declared population run-selftests kit withheld project-owned`
