# Research: gov's measured history of stalls and loops

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 146's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-21-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-stall-and-loop.md`.

---

**The history of stalls and loops in gov, from its own records**

Every path below is relative to the repo root, `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/`. Node-local logs are under `C:/projects/coding-governance/.git/`. I wrote nothing in the repository, and the scratch parsers are deleted.

**How I measured it.** Two Python parsers ran over the tree:
- **The 565 review records** under `memory/builds/*/reviews/`. From each I took the `**Serves:**` kind and ids, the round number (from the filename or heading), the `## Verdict` line, and the confirmed count and precision. 397 records carry a confirmed count I could parse, and 416 carry a precision.
- **The 98 run-state files**, `memory/builds/*/RUN*.md`. From each I took the phase, halt code, hold code and park lines.

I also read the node-local logs: `.git/runlog/{driver,gates,pushes}.log`, `.git/health.log` and `.git/worktrees/*/unattended/stall.*.log`. Those logs exist only on this node.

**One heuristic to keep in mind.** A review "subject" is a build, its review kind and its Serves id set. dClosedLoop is the exception: it is grouped by filename stem, because its 48 records review different layers under one id.

## 1. Measured table

| # | Case | Source | What looped or stalled | How long / how many | What stopped it | Cost |
|---|---|---|---|---|---|---|
| 1 | dClosedLexicon review loop | `memory/builds/aBoundedVerdict/README.md` [What the measurements said]; `memory/builds/dClosedLexicon/RUN.md` abort line | One predicate's (P3) review never converged | 10 records in two days. Rounds 2–7 were BLOCKED with blocker counts 1, 1, 2, 1, 2 | The agent's own stopping rule, set before round 3 ("my own assessment was wrong three consecutive times"). Abort `fork-unresolvable`, then an attended merge `c48ccdaa` | The run died ABORTED, and the record still reads ABORTED (`...dUnstuckLanding-1-census.md` [gov: ABORTED today]) |
| 2 | aSiftedPlaybook spec audit | aBoundedVerdict README, same table | Five consecutive spec-audit rounds plus a closing round | Verdicts CWF, B, B, B, CWF, B, all in one day; specs reached rev-12 | Nothing structural. It landed | Not recorded |
| 3 | dScriptedRepeat closing diff review | `memory/builds/dScriptedRepeat/reviews/*-diff-round{1..9}.md` | Each round reviewed the previous fold | 9 rounds, 08-21 to 08-24. Confirmed findings: 32, 16, 18, 22, 23, 29, then 16, 16, 19 | **The owner**: round 9 says "the owner has authorised this fold and then a merge and push with no further review" | 4 days of rounds. Token cost not recorded |
| 4 | aGradedDialect-4 diff review | `memory/builds/aGradedDialect/reviews/2026-09-11-*-diff-round{1..6}.md` | Every finding from round 3 to round 6 is "a regression the round-N fold introduced" | 6 rounds in one day. Confirmed 23, 14, 10, 11, 9, 10 | The run aborted (`scope-approval-needed`, private source in a public repo) | One day |
| 5 | aBatchedArm spec audits | `memory/builds/aBatchedArm/RUN.ABORTED.7742ee67.md`; its RUN.md review lines | Three units looped | Blocker sequences: `-3` 8, 9, 8, 4, 12; `-1` 3, 13, 4, 0; `-5` 3, 2, 1, 2. Precision 0.31–0.67 | Abort `scope-approval-needed` ("three units, four spec audits, all BLOCKED"). The owner then added a unit and it was re-run to LANDED | RUN.md spans 49.3 h |
| 6 | aWokenSentinel promotion cascade | `memory/DECISIONS.md:209` (TOOL-aWokenSentinel-29); `memory/builds/aWokenSentinel/RUN.md:249` | Each spec-audit generation promoted new units, and each new unit was audited | 4 generations promoted 7, 6, 4, 4 units. Precision 0.80, 0.58, 0.77, 0.61 (never under 0.5) | The run's own `specs-audited` override ("about 75 minutes and 3M tokens each with no convergence in sight") | About 4 × 75 min and about 12M tokens, by the run's estimate |
| 7 | aEvidencedLens promotion chain | `memory/builds/aEvidencedLens/RUN.md:169` | Same shape | Rounds 1–4 promoted 3, 1, 1, 2 units at precision 0.94, 0.94, 1.00, "high" | The run's override after round 4. Then the owner ruled that only the owner opts a build into the audit (`DECISIONS.md:221`, TOOL-aWardedAudit-4) | Units 19–20 were built unaudited |
| 8 | dDerivedDocket spec generations | `memory/builds/dDerivedDocket/RUN.md` review lines (g1 to g10) | Generations of spec sets were audited and promoted | 10 generations from 09-14 to 09-27. g3-folds and g8 exited BOUNDED and promoted | Converged at g10 | RUN.md spans 351.8 h (holds included) |
| 9 | Fold-caused findings | `memory/gotchas/fold-text-is-unreviewed-surface.md` [Where it bit]; dTieredTribunal and dFramedEntrypoint review records | The next round mostly found defects in the previous fold's prose | See §2 | Never stopped structurally. It is documented as a gotcha, "No machine gate" | It recurs in dClosedLoop: 7 of 17 defects in the answers fold |
| 10 | aStagedLane review cost | `memory/builds/aStagedLane/reviews/2026-09-05-...-diff-review-round1.md:172` | Spec audit then diff review | Spec-audit blocker sequence 4, 2, 1, 3 (NON-CONVERGENT). 5 review rounds in total | The predicate's NON-CONVERGENT exit | About 7.7M subagent tokens |
| 11 | Weekly-limit wake loop | `.git/worktrees/build-readme-governance-18d6ea/unattended/stall.dDerivedDocket.log` | One session, `2588f719`, kept being woken into a refused API turn | 115 entries (112 `rate_limit`, 3 `server_error`). One roughly every 10 min, 09-24 08:10–20:44 and 09-25 09:59–15:14. Payload: "You've hit your weekly limit · resets Sep 27" | The quota reset, then a **manual** `--resume` on 09-27T14:17 (RUN.md:316) | 4.8 days of wall clock (09-22 18:35 → 09-27 14:17). Turns were refused, so tokens were near zero |
| 12 | Reviews dying on limits went unseen | `tools/unattended/stall-recorder.js:11-13` | Four Tier-2 reviews died on limits | 4 | **A person reading a journal**. The stall recorder was built afterwards (TOOL-aWokenSentinel-4) | Not recorded |
| 13 | A non-terminal LANDING record blocked every run | `memory/builds/aBoundedVerdict/RUN.ABORTED.fc79c21d.md` parks at 08:25 and 15:00 | aPacedTurnstile's record sat at LANDING, which is not terminal. Check 7 counted it against every later run | aBoundedVerdict lost 7.9 h of run and aborted `gate-red-out-of-scope` | Abort, then a re-run to LANDED `77246746` | One aborted run and one re-run |
| 14 | Abandoned run at LANDING | `memory/builds/dTieredTribunal/RUN.md` abort line | The record was untouched from 16:19 and no process named it, so check 7 "redded every bar" | Until 17:40 on 08-27 | **The owner** ("STOPPED BY THE OWNER ... so that a second unattended run could land") | One run's landing was blocked |
| 15 | Two guards wedged each other | `memory/gotchas/two-guards-one-question-two-answers.md` [Where it bit] (TOOL-dUnstalledConvoy-33) | Check 24 and check 48 disagreed, so a rescope row was "refused forever" | 4 units on one build | A fix that derives the question once | Not recorded |
| 16 | Pre-push hook refused every run claim | `memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md:25-32` (aGraftedHelix) | On node a, with `GOV_DEFAULT_BRANCH` unset, the hook "refused every claim, so no unattended run could start" | Every run on the node; duration not recorded | A fix to the fixture and the hook | A fleet-wide start stall |
| 17 | A rule merged mid-run refused the run's own record | `memory/builds/aGraftedHelix/RUN.ABORTED.6410435d.md` abort line | Merged-in check 89 refused the record's spec-audit opt-in at `--close` with no override, and the pinned BASE cannot change | 25.0 h of run | Abort (`repo-state-out-of-mandate`, "rotation, not abandonment"), then a re-preflight | One rotation |
| 18 | A gate that rejected its own bookkeeping | `memory/builds/dMispairedQuote/RUN.md` abort line | 85 of 86 legs green. Kit check 2 counted a promoted id per non-convergent exit, but M4 allowed a fold there, which leaves no id | Run aborted | Abort `gate-red-out-of-scope`, then landed the same day (census) | One abort |
| 19 | Unbounded commands inside unit passes | `memory/builds/aProbedUnit/README.md:16-20` | A full bar with self-tests inside a pass; a 6 h `rm`; an empty `$TMPDIR` that sent a cleanup to an approval prompt nobody answered | Bar up to 12 h; `rm` 6 h | **The owner's report**, then TOOL-aProbedUnit-8/-10/-11 (bar once per session, scratchpad, `UNIT_STALL_BOUND`=1800 s) | Up to half a day per unit |
| 20 | Bars killed at the bound | census [gov: ABORTED today] (aHoistedPass) | Lander on a diverged primary main | Two bars killed at 3604 s and 3602 s | `GATE_BOUND` 3600 s (`tools/unattended/unattended.sh:437`), then abort `repo-state-out-of-mandate` | About 2 h of bar |
| 21 | Slow-host canary | census (aMeteredTurnstile); `DECISIONS.md:72` (TOOL-cSteadyMetronome-1) | The canary's timing ratio measured the machine, not the code | Blocked 3 pushes; aMeteredTurnstile aborted | The owner chose "replace, not retry" (`memory/builds/cSteadyMetronome/README.md:63-64`) | 3 pushes, 1 abort |
| 22 | A hung canary retried | `.git/health.log` | `retry-passed run-gates canary after a 13200s timeout` | Twice (10-11 and 10-13), plus 3 dead bar holders reaped | The ceiling kill plus a retry in the drain tail (TOOL-aSparedSpawn-3) | About 3.7 h each |
| 23 | Red bars on this node | `.git/runlog/gates.log` (09-14 to 10-19) | Repeated reds | 46 of 81 bars RED. 36.3 h of the 44.0 h of bar wall time was in red runs. At most 4 consecutive REDs in one worktree. Top failing legs: `govkit selftest` 22, `memory hygiene` 19, foreign-prefix parity 15. One `wall_breach=21600` (21619 s) | Fixes per leg. The 6 h wall | 36 h |
| 24 | Driver refusals | `.git/runlog/driver.log` (09-13 to 10-14) | Verb calls refused | 85 of 981 calls ended rc=1. The most repeated was `--dispatch dLoggedFlight`, check class 49, 10 times | Agent corrections. Ambiguous: `fail 49` has 35 sites in `unattended.sh`, so the class does not name the site | Small |
| 25 | Inherited reds and owner hand-offs at close | `memory/builds/dUnstuckLanding/build/2026-10-04-...-census.md` [The headline] | Runs aborted as a way of handing work back | 37 aborts across 3 repos (15 in gov). 36 of 37 landed anyway; 29 by attended merges 14 min to 41 h later. Gov closes recorded 12 `gates-green` overrides (5 were owner "skip the bar") | Owner rulings TOOL-dDerivedDocket-24 and TOOL-dUnstuckLanding-22 (inherited red lands at any age), plus `--handoff` / HELD | One owner turn per abort |
| 26 | HELD hand-offs | The 98 RUN files' `hold` and `handoff` lines | Runs waited "until owner" | 16 `owner-decision` hand-offs. 8 records still read `phase: HELD`; their slugs appear in merge subjects on main from 10-09 to 10-13 (I matched by subject grep; I did not verify each merge is the landing). Host holds lasted 1.5–40.7 h before a resume | Every resume line (23 of 23) reads `manual` | Records go stale; work still landed |
| 27 | Review cap that relocated the stall | `memory/builds/aBoundedVerdict/build/2026-08-18-...-review-loop-design.md` [§1] | The two-round cap (TOOL-aBoundedVerdict-1) | The method's only exit, a CLEAN verdict, occurred in **0 of 90** records | The owner reversed the cap (`DECISIONS.md:95`). The cause was the missing BLOCKED disposition, not a missing count | — |
| 28 | The spec audit's cost | `memory/builds/aBlindedTrial/build/2026-09-20-...-trial-report.md` [§5] | The audit as default ceremony | 12× output tokens, 17× cache reads. The audit alone was 60% of the arm, at precision 0.39. No measurable correctness gain (p ≥ 0.8) | The owner made the audit opt-in (`DECISIONS.md:214`, TOOL-aBlindedTrial-6, 09-20), then owner-only (`:221`, 10-05) | — |

## 2. The review-convergence curve

**Confirmed findings per round, from the review records.** Subjects are those with explicit round order; dClosedLoop is excluded.

| Round | Spec audits: n / median confirmed / median precision | Diff reviews: n / median confirmed / median precision |
|---|---|---|
| 1 | 96 / 22 / 0.52 | 131 / 16 / 0.81 |
| 2 | 37 / 20 / 0.53 | 45 / 14 / 0.85 |
| 3 | 14 / 23 / 0.61 | 12 / 14 / 0.84 |
| 4 | 2 / 11 / 0.43 | 6 / 16 / 0.87 |
| 5 | 1 / 18 / 0.40 | 2 / 16 / 0.94 |
| 6 | — | 2 / 19.5 / 0.85 |

- **Round 2 against round 1.** Across 79 subjects, the median ratio is **0.90**, and **33 of 79 (42%)** had round 2 at or above round 1.
- **Consecutive pairs.** Spec audits fell 34, rose 16, held flat 1. Diff reviews fell 33, rose 24, held flat 8.
- **Where the count first did not fall.** For spec audits: round 2 in 12 subjects, round 3 in 3, and 45 fell to the end. For diff reviews: round 2 in 21, round 3 in 3, round 4 in 3, and 25 fell to the end.

**Blockers per round, from the driver's own `review ·` lines in RUN files.** 222 subjects:
- Median blockers by round: round 1 is 1.0 (108 of 226 at zero), round 2 is 1.0 (mean 1.89), round 3 is 1.5, round 4 is 3.0 (n = 4).
- In multi-round subjects, blockers first failed to fall at round 2 in 34, round 3 in 14, round 4 in 4, and fell to the end in 50.
- Recorded exits: 156 `CONVERGED`, 51 `NON-CONVERGENT`, 10 `BOUNDED`, **0 `CEILING`**.

**So the count stops falling at round 2–3.** Confirmed findings stay roughly flat at 14–23 per round. Only the blocker count trends down, and it plateaus at 1–3.

**How much of the next round the fold caused.**

| Record | Fold created the defect | Fold misread its own finding | Previous round missed it | Fold-caused share |
|---|---|---|---|---|
| dFramedEntrypoint-1, round 2 | 25 | 17 | 20 | 42 of 62 (68%) |
| dTieredTribunal-1, round 2 | 20 | 6 | 3 | 26 of 29 (90%) |
| dTieredTribunal-1, round 3 (hand fold) | 20 | 11 | — | 31 of 32 (97%) |
| dTieredTribunal-11, round 2 ("minimise new prose") | 11 | 5 | 2 | 16 of 18 (89%) |

Sources: the round-2 dFramedEntrypoint record (line 17) and the dTieredTribunal round records (round 2 lines 30–32, round 3 lines 32–36, `-11` round 2 lines 30–37). The dTieredTribunal records' own conclusions: "author count is not what drives this", and minimising new prose "is a way to make a fold smaller, not ... safer". Separately, the round files of dScriptedRepeat, aGradedDialect, aScouredKit and aWeldedTribunal describe their findings as fold-introduced in prose, but give no counts.

**Why it stopped looping, by period** (subjects with 2+ records / all subjects):

| Period | Rule in force | Spec audits | Diff reviews |
|---|---|---|---|
| Before 08-16 | No exit rule | 2/27 | 2/13 |
| 08-16 to 09-13 | The convergence rule | 48/100 (18 had 3+) | 36/80 |
| 09-14 to 09-19 | `REVIEW_ROUNDS=1` | 9/16 | 5/9 |
| 09-20 to 10-04 | Audit opt-in | 1/16 | 7/25 |
| From 10-05 | Owner-only opt-in, promote everything | 0/6 outside dClosedLoop | 4/32 |

The October diff-review chains are mostly promotion chains, not repeat rounds; for example dLadderedRemote-2 to -8 is five "rounds" in one day, each on a new id. dClosedLoop itself has 48 review records over 10-15 to 10-19, with 1531 confirmed findings.

## 3. Mechanisms that worked, and mechanisms that did not

**Worked:**
- **Giving BLOCKED a disposition** (the predicate at `tools/unattended/unattended.sh:12473-12481`: zero blockers means CONVERGED, a count at or above the previous one means NON-CONVERGENT). The evidence is the 51 NON-CONVERGENT and 10 BOUNDED exits in RUN files, with no subject past 5 driver rounds. It replaced a cap that the 0-of-90 measurement showed was aimed at the wrong variable (table row 27).
- **One spec-audit round by default** (`unattended.sh:447`, `.unattended.conf:111`) **plus owner-only opt-in** (`BUILD-METHOD.md:117-121`). Spec subjects with 2+ records fell from 48% to 0 outside dClosedLoop. The cost evidence is aBlindedTrial §5.
- **Promote instead of fold** (`DECISIONS.md:219-220`; `BUILD-METHOD.md:144`). It moves findings out of the loop. aBatchedMinors' README (lines 15–17) records why: folded minors "stood unfolded for weeks".
- **Command bounds and ceiling kills**: `GATE_BOUND` 3600 s (`unattended.sh:437`) and `UNIT_STALL_BOUND` 1800 s (`unattended.sh:440`). They worked in table rows 20 and 22. I found no recorded firing of the `--audit` STALLED verdict in any RUN file.
- **Halt codes, HELD and `--handoff`.** They turned silent stalls into named stops: 13 aborts carry codes. dUnstuckLanding's census shows the codes were mostly being used as hand-offs, which led to TOOL-dUnstuckLanding-22.

**Did not work, or never fired:**
- **`RUNAWAY_CEILING=8`** (`unattended.sh:774`). It fired 0 times; the halt code `runaway-ceiling-unclean` appears nowhere under `memory/`. Its own comment (`:766-771`) says it is a backstop set above any observed sequence.
  - **Record and code disagree.** That comment says that on a ceiling hit "the run promotes and lands anyway", and `:12720` repeats this. The halt-code vocabulary at `:980` lists the same event as a halt. Neither path has ever run.
- **Resume attempts** (`RESUME_ATTEMPTS`=6, `tools/unattended/resume-tick.sh:121,326`; `.unattended.conf:98`). "ATTEMPTS EXHAUSTED" appears only in specs and reviews, never in a run. All 23 recorded resumes are `manual`. The 4.8-day weekly-limit stall was ended by the quota reset and a person.
- **The precision floor as the end of a promotion chain** (`BUILD-METHOD.md:144`). **Record and code disagree:** `unattended.sh` never reads precision, and `tools/workflows/tier2-review.js:1494` only prints advice below 0.5. Neither real chain fell below the floor (aWokenSentinel ≥ 0.58, aEvidencedLens ≥ 0.94). Both were stopped by the run's own `specs-audited` override.
  - **Ambiguous.** aWokenSentinel cites "M4's CEILING clause" for its stop. Today's M4 has no such clause for chains.
- **Fold review.** No gate exists for it (the gotcha's own words: "No machine gate"). The fold-caused share stayed at 61–69% narrow and 89–97% wide however the fold was written.
- **Guard-on-guard wedges and records left non-terminal** (table rows 13–18). Each was found when a run aborted or a person noticed, and fixed one instance at a time.

**Loops that ended only because a person noticed or ruled:** table rows 3 (owner authorised the last round), 12 (a human reading a journal), 11 (manual resume after the reset), 14 (owner stop), 19 (owner report), 21 (owner chose replace over retry), 25–26 (attended merges and manual resumes), and the aBoundedVerdict build itself, opened on the owner's report of an indefinite review cycle.

**Gaps in the sources:**
- The runlogs are this node's only, so other nodes' bars and stalls are not counted.
- Run token cost is not recorded anywhere except the few review records quoted above.
- Pre-09-14 review lines in RUN files carry no state token: 139 of 356 lines.
- The aTetheredScratch "73 of 123 legitimate commands denied" figure (`DECISIONS.md:98`; `memory/builds/aTetheredScratch/README.md:47-48`) is a counterfactual measured over past commands, not a stall that happened.

One line for another researcher (the census of the design's cycles): the handed v2 keys `runtime.hold-ceiling` and `roles.retries` have no counterpart in today's history beyond the manual resumes in row 26.
