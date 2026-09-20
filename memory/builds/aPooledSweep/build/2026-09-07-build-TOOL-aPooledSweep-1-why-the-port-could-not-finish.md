# Why the port could not finish, and what that leaves as the lever

**Serves:** research TOOL-aPooledSweep-1

Node `a`, 2026-09-07, read at `05fb897c`. `TOOL-aQuenchedHarness-6` ported one suite of the declared
population and recorded AC5 — its majority-share criterion — NOT MET, with the arithmetic written
down rather than the threshold lowered to fit. This is the diagnosis the owner asked for. It is not a
criticism of that record: the survey it rests on is careful, honest about what it did not run, and
its central claim is correct. What it could not see is that the criterion was unreachable before the
first suite was examined.

Three reasons, independent, each sufficient on its own.

## 1. A third of the population was never surveyed, and could not have been

`bash tools/run-gates/run-selftests.sh --rank` at `05fb897c` ranks 59 rows holding 36146 s. The
declared share is 50% and it is carried by the TOP FIVE. The survey covered the twelve costliest rows
**as they stood when it ran** — which, against today's ranking, is positions 3 through 14. Positions 1
and 2 are absent from its table:

| rank | suite | recorded | in the survey |
|---|---|---|---|
| 1 | unattended gate selftest | 9067 s | no |
| 2 | unattended driver selftest | 2569 s | no |
| 3 | manifest-check self-test | 2547 s | yes |
| 4 | run-gates canary | 2436 s | yes |
| 5 | run-gates turnstile | 2419 s | yes |

The survey says so itself, in one clause: "two were not surveyed because they had no reading when it
ran." Those two are 11636 s — **32.2% of the population**, and two of the five rows the share needs.

This is not an oversight, it is a CIRCULARITY. The selection rule (§S3) sorts by recorded seconds;
§S2 refuses the selection until every row carries a reading; and the six unattended rows had no
reading, because they are in no gate manifest and nothing had ever timed them. Producing those
readings is what the survey's own run did — "running the whole kit on a frozen clone produced them,
and the verb then ran on the real tree for the first time." So the act that made the ranking valid
and the act that surveyed the twelve were the same act, and the two rows the ranking then promoted to
the top arrived after the survey had closed. Nothing re-opened it.

**The consequence is arithmetic and not judgement.** Even if every one of the twelve surveyed rows
had been ported perfectly, the top two would still be unported, the share would still fail, and no
amount of work inside the survey's scope could have reached 50%.

## 2. The harness cannot express what these suites assert, and the safety property forbids changing them

`tools/lib/lib-selftest.sh` declares an arm as `arm <label> <want-rc> <want-substring> <setup>
<subject>`. Exactly one POSITIVE substring, or the empty string meaning "do not grade the output",
plus an exact rc equality. That is the whole assertion vocabulary.

This repo's suites assert NEGATIVES, heavily. Counted at `05fb897c` over the two unsurveyed suites,
by their own `hit`/`miss`/`same` helpers:

| suite | positive (`hit`) | negative (`miss`) | equality (`same`) |
|---|---|---|---|
| `tools/unattended/check-unattended.test.sh` | 247 | 101 | 27 |
| `tools/unattended/unattended.test.sh` | 471 | 109 | 164 |

210 negative assertions across the two costliest suites, and not one of them has a spelling under
`arm`. The survey found the same thing in the twelve it did read: all 62 of manifest-check's arms
carry a no-raw-`fatal:` negative, 56 in memory-hygiene, 8 in install-prefix. It also names three
further gaps — a structural silent-clean predicate, an rc-INEQUALITY, and slicing a capture per check
rather than searching the whole of it.

**And this is where the unit closes against itself.** §S5 makes the port's safety property an arm
inventory extracted before and diffed after, and a non-empty diff "a defect in the port, not a
judgement call". A suite whose assertion the harness cannot express must have that assertion
REWRITTEN to be ported. A rewritten assertion is a changed arm. A changed arm is a non-empty diff. So
the safety property refuses exactly the ports the vocabulary gap forces — which is why the survey's
verdict is the absolute "not portable under this unit's own rules" rather than "expensive". Under
those rules it is not a matter of effort. It is closed.

The remaining classes the survey names are real and are not vocabulary: three suites are Python
driving module internals with no CLI entry point, two print no recoverable per-arm line so no
inventory can be diffed at all, and four need arms to share state that a per-arm `cp -a` destroys —
`run-gates turnstile` grades a peak-occupancy count across live runners, and `install-prefix` embeds
a running counter in two arm LABELS. Those four classes plus the vocabulary gap cover all twelve.

## 3. The cost being attacked is inside each suite; the population's cost is the runner adding them up

`tools/run-gates/run-selftests.sh` executes its 59 suites SERIALLY, and its own header says why:

> THE OUTER POOL IS 1 BECAUSE THE RUN LOOP BELOW IS SERIAL, and it is serial on purpose: this runner
> grades each suite against its OWN declared budget, so two suites racing would charge each of them
> the other's contention and a breach would name the wrong one.

That is a sound reason for a real constraint, and it was never revisited. The parent build attacked
cost one suite at a time, inside the suite, by parallelising ARMS — which is what forces every one of
the obstacles above. The runner that sums those suites was not in scope for any of its nine units.

The measurements it took point the same way. `TOOL-aGradedDoorway-8` records that the unit of cost
here is process creation: an on-access scanner sits in front of every `exec` on this node, a spawn
costs 0.019–0.039 s against roughly a millisecond elsewhere, and one invocation of the longest leg
measured `real 14.4s user 0.33s sys 0.62s` — 93% of it spent waiting rather than working. **Work that
is 93% waiting is work that parallelises,** and the cheapest place to parallelise it is where 59
independent processes are already being run one after another.

## What this leaves

The port programme is not blocked, it is SUPERSEDED — for the goal it was serving, which is the
parent build's own: the on-demand sweep costing minutes rather than hours. A bounded outer pool in
the runner touches no suite, so it cannot lose an arm; it needs no assertion vocabulary, so the
Python suites and the unextractable ones are not special cases; and it applies to 100% of the
population where one port reached 0.58% — `check-line-length.test.sh`, 208 s of 36146 before,
8 s after, both readings in the budgets file's own rows.

**What it does not buy, stated rather than left to be discovered.** A pool's wall clock cannot fall
below its longest member, and that member is 9067 s. So this is not "minutes" either; it is roughly
ten hours to roughly two and a half, over the whole population instead of one suite of it. Falling
further means dividing that one suite, which already carries a `--shard 1/2` contract it is
deliberately run without — a follow-up, named here and not built, because the shard-versus-whole-suite
claim distinction is a real one that `run-unattended-gates.sh` records and this build does not
resolve.

**And what the survey's verdict is still worth.** It stays the record of what a port would need: five
suites rated partial with their arm counts, four blocking classes, and one named follow-up
(`manifest-check.test.sh`, 62 of 62 arms mappable) with its four concrete obstacles enumerated. A
later build that wants those suites on the harness for a reason other than cost — attribution, or
arms that a whole-suite verdict cannot give — should start from that table and from the vocabulary
gap counted above, not from a fresh survey.
