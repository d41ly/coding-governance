# Research: testing anywhere in the flow

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 101's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-5-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`.

---

1. **Verdict**

The design tests in four places only: the landing verdict in Test, the read-only research items, the skeptic's refute probes, and the executor's acceptance re-runs. 61 of its 81 items have no role that could ask for a test, and none of its 20 role items can run an experiment that writes. The unattended code has a pre-spec `TESTING` position that the design dropped. I recommend candidate E: one `probe.*` program with two ways in. The driver can place a probe at any item boundary, the way a breakpoint is placed, and a role can raise one as an outcome, the way research is routed. Test stays as the landing verdict. Experiments reuse aScoutedSeam's corpus, variant, scorer and judge pattern as a fifth registered shape.

2. **Today: testing outside the Test step, measured**

| Testing | Who | Recorded as | Handed on |
|---|---|---|---|
| A visual check of the generated atlas: 11 views, 1440×900 and 375×812, no console errors, no sideways scroll | the main session, by hand | prose bullets (`atlas-instruments.md:186-192`), which say "The checks under `[preview]` were run by hand" (`:47`). There is no screenshot and no witness | the record only |
| Reproducing a bug | whoever files the ask | the ask's `seen` clause, `LOCATOR [ " run `" COMMAND "`" ]` (`tools/memory-tree/backlog.py:28-29`). 97 of 859 asks carry `seen`, and 41 of those carry a `run` command | the ask's acceptance, at triage |
| An experiment before a baseline: the aScoutedSeam benchmark | the main session, as "owner opt-in to real Workflow runs; the owner waived the five-agent concurrency cap" (`benchmark.md:5`, on that branch) | scripts, corpus and results committed, and every figure re-derived by the committed grader (`benchmark.md:6-7`) | cited by v2 `[owed]` (`v2:1250-1256`), and dTotalRecall is "accepted by re-running aScoutedSeam's benchmark" (`v2:1190`) |
| The compaction experiment | the main session, at the owner's request | blinded by commit order: the key committed before the compaction, and the recall committed before the key was read (`compaction-results.md:6-7`). The tallies come from an instrument | v2 was revised from it (`v2:101`) |
| Research probes | researcher agents with `writes: none` (`.claude/roles.json:31-36`), working in scratch | returns with commands and output (61 `research-*` records in this build) | through the driver and the prompt writer (P26, `flow-roles:16-33`) |
| Seen-red checks | the builder or the main session, on a planted copy | prose such as "Seen red: each arm on a planted copy" (`layer-roles.md:428-430`). There is no recorder (`gap-test-06`, register:242) | the record only |
| Testing candidates before speccing | an unattended run | `PHASES_CORE="PREFLIGHT RESEARCHING TESTING SPECCING …"` (`tools/unattended/unattended.sh:852`), deliberately "POSITIONS, not pass kinds" (`:855-859`), plus the directive `solution-tested:M12` (`:1042`) | an attested directive |

**Where the records and the code disagree:**
- The code's `TESTING` position has no counterpart in any design item. The only record that names it is `research-runtime-executor.md:16`.
- The tester is a core role in the design (`layer-roles.md:451`), but no tester agent exists. `.claude/agents/` holds 9 files, none of them a tester.
- The researcher's `none` write class is declared in the role index, but scratch-guard reads nothing for it: "`none`, `review` and `records` are declared in the index and read by nothing here" (`tools/hooks/scratch-guard.js:102-103`).

3. **The design today, step by step**

```
$ python -I - (actor census over flow-steps' item tables)
entry {'hook':1,'ROLE':2,'command':2,'owner':1}  plan {'command':7,'ROLE':4}
design {'command':6,'ROLE':6}  build {'command':6,'ROLE':1,'executor':2,'owner':1}
test {'command':8,'ROLE':2}  deploy {'command':13}  breakpoint {'command':4,'ROLE':4}
lifecycle {'owner':1,'executor':1,'command':4}  adopt {'command':3,'owner':1,'ROLE':1}
$ grep -n '| testing\|testing |' flow-steps.md
522 building→testing · 525 testing→deploying · 526 testing→building · 527 testing→designing · 528-529 deploying→testing
```

| Step | Testing it can hold today | Items and roles | What it cannot do |
|---|---|---|---|
| Entry | the scout re-verifies recall, read-only (P29, `v2:657`); `placement.check` checks facts | `entry.orient` and `entry.place` (orientation scout) | verify an owner's observation or reproduce a report before placing it. Free actions are `read-only-probes` (`v2:752`, OR-3) |
| Plan | research, read-only; acceptance is written "as observations" but not run | `plan.research` (researcher, `flow-steps:120`) and `plan.record` | an experiment that writes or spawns. There is no item that measures a baseline |
| Design | the seams' probe digests, re-derived by the executor (`:167`); `design.research` (`:169`) | reuse scout, researcher | an experiment between candidates. dIndexedDesign's "research harness" (`v2:1195`) has no item |
| Build | the acceptance re-run (`:218`), core checks and scope | the executor and the builder | a red-first reproduction; a seen-red before Test |
| Test | the landing verdict, attribution, flakes, seen-red (`:271-282`) | the tester at `test.attribute` and `test.reason` only | anything before a built range exists ("Takes in a built range", `v2:1171`) |
| Deploy | the post-merge bar, `deploy.core` (`:342`) | none: 13 commands | any probe a role raises, because there is no role |
| Breakpoint | the skeptic's refutation: "each verdict names its probe and the probe's output" (`:449`) | skeptic | its records are disposed into folds, units or asks (`:451`) and never handed to the item it resumes |
| Maintain | the cadence levels, with the tester attributing their reds (`flow-roles:116`) | the tester, in the expansion | nothing more |
| Adopt | `test.seed` seeds the debt ledgers (`:499`) | command | this "baseline" means tolerated legacy debt (`retrofit.md:310-343`), not a measured reference |

The chain already needs experiments that set a baseline, and it places them as build units:
- dFairHearing's "owed replays first", scored by `tools/workflows/review_replay.py`, which exists in the tree (`v2:1187`);
- dTotalRecall's "replay with the map and without at its first unit" (`v2:1190`);
- dTotalRecall's acceptance by re-running aScoutedSeam's benchmark (`v2:1190`).

4. **aScoutedSeam's shapes**

All of these are on `origin/branch/deterministic-reuse-workflows-f70c33`, under `memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-`. I re-derived the scores offline with the committed grader; I ran no workflow.

```
$ python -I …-4-bench.py grade …-3-cases.json …-5-results.json <arm> | tail -1
m1@medium:  positives 24 solved 13 · items 20/59 · decoy MUSTs 1
m1b@medium: positives 24 solved 13 · items 23/59 · decoy MUSTs 1
m3@medium:  positives 23 solved 12 · items 20/56
m1cA@medium: positives 24 solved 16 · items 26/59 · decoy MUSTs 2
m1cB@medium: positives 24 solved 16 · items 24/59 · decoy MUSTs 1
$ … judged m1cA@medium m1b@medium
m1cA primary 17/24 · items 39/59 · wrong MUST 20 · mean 3.50
m1b  primary 14/24 · items 37/59 · wrong MUST 11 · mean 3.50
```

These match the records: `benchmark.md:166` (13 of 24) and `m1c-trial` (16 of 24).

| Shape (file:line) | What it varies | What it measures | How it judges | Result | Generalises? |
|---|---|---|---|---|---|
| `6-batch-all.js:19-28` | the arm, as child workflows over at most 5 cases, capped at 4 | nothing itself | — | ran M1, M1b, M3 and D1 | **yes**: the variant runner |
| `6-m1-single-scout.js:19-29,57` | a free-roaming prompt | seams against the SEAMS schema | the grader | 13 of 24 at medium | it is one variant |
| `6-m1b-checklist-scout.js:45-58` | a fixed 7-step checklist | the same | the same | 13 of 24, 23 of 59 items | variant |
| `6-m1c-sketch-scout.js:18,49-63` | house index, sketch, census | the same | the same | 16 of 24 in both runs | variant, and the winner |
| `6-m2-lens-scout.js:5-8,60-101` | frame, 5 lenses, 2 skeptics | the same | the same | pilot only, 1.6–1.9M tokens per case (`benchmark.md:96`) | rejected arm |
| `6-m3-lean-scout.js:111-115` | code and design halves, then a judge | the same | the same | 12 of 23, the same as M1b on a third of the agents (`benchmark.md:169-171`) | rejected arm |
| `6-m3-complete.js:91,113-117` / `6-m3-halves.js:112-115` | finishing killed halves from a packet; halves skippable | — | — | completed M3 | **yes**: resume and complete |
| `6-d1-diff-check.js:19-24` | a review at diff time | duplicates-found or clean | the grader | 7 of 23 at extra, 4 of 23 at medium (`benchmark.md:147`) | a review lens, not an experiment |
| `6-rerun.js:17-27`, `6-rerun-effort.js:17-28` | effort (low, medium, high), and re-running killed agents | — | — | rows filed `<arm>@<effort>`, "nothing pooled" (`benchmark.md:133-134`) | **yes**: re-run and effort axis |
| `6-judge.js:18-26,45` | — | covered, primary, wrong, valid_extra, score 1–5 | one blind judge per case, labels anonymous and rotated, no git history | M1c and M1b both mean 3.50 | **yes**: blind judge |
| `4-bench.py:8-11,332-400` | — | `trees` (blinded clone at the case's point), `grade`, a paired `compare`, `misses`, `cost` | deterministic path and symbol matcher | re-derives every figure | **yes**: blinding and scorer. The matcher itself is specific to this domain |
| `3-cases.json` | — | corpus: id, point SHA, prompt, ground_truth, decoys, reinvention | — | 30 cases (24 positive, 6 controls) | **yes**: corpus schema |
| `8-precision.py:2-14` | demotion rules, simulated offline | wrong MUSTs by class | it "takes judge verdicts as given" | an existence check removes 0 of 19 wrong MUSTs | yes: offline post-hoc reading |

**What generalises:** a corpus pinned to a point with controls and decoys; blinding at that point; variants sharing one return schema; a bounded fan of five slots; a deterministic scorer that re-derives every figure from committed files, paired over the cases every variant answered; a blind judge for what a matcher cannot see; re-runs keyed by `<variant>@<effort>`; cost as a pinned reading.

The tree already holds the second instance of that scorer: `tools/workflows/review_replay.py` scores a known set against a candidate, and refuses a parse that returns only part of a population (`:1-40`). The charter's `[reuse]` rule therefore owes a factory.

**How it registers:**
- a fifth shape kind, `experiment` (fan = cases × variants, judge = command or role, merge = scorer), beside `single`, `per-unit`, `panel` and `twin` in `workflows.toml` (`systems:408-410`);
- its harness at Runtime's role-harness point (`layer-runtime:819`);
- its scorer as a command adapter with a witness contract (`:817`);
- each arm's run as a shape-run row (`systems:416-423`).

5. **Candidates**

The probe record has one schema across all candidates:
- the question;
- its kind (`verification`, `reproduction`, `seen-red` or `experiment`);
- the subject, pinned by SHA;
- the method: commands, or a harness and shape;
- the losing outcome, committed before the run (M12; the compaction blinding);
- the captured output, by hash;
- the verdict, from {confirmed, refuted, inconclusive, unrunnable}, or for an experiment {measured, within-noise, aborted};
- who judged it.

Its witness is one of two things:
- the executor re-runs the declared commands, as `build.acceptance` does (`flow-steps:218`);
- for an agent experiment, the scorer re-derives the result from committed raw outputs bound by shape-run rows. An agent-judged figure is classed `claimed` (P23 and P29) and may route only to an owner item.

| | **A. A test point at a boundary (the breakpoint mechanism)** | **B. Test as a re-entrant step** | **C. Static test items per step** | **D. A probe a role raises (the research route generalised)** | **E. A and D: one `probe.*` program, two ways in** |
|---|---|---|---|---|---|
| Mechanism | a point declares position, disposer (the tester) and trigger, like `[breakpoint]` (`flow-steps:417-423`), then resumes at the item it stands before | a build enters `testing` from any state and returns | e.g. `entry.verify`, `plan.experiment`, `build.reproduce`, each with routes | every role item's outcome set gains `probe`; it goes to `probe.*` and back, as `plan.record`→`plan.research`→back (`:119-120`, `:168-169`) | one program; entered from a boundary point (A) or from a role's outcome (D) |
| Trigger and key | `probe.points` (a set of boundaries, default none), a recommendation, or the owner's request | a route to `testing` | static | `probe.raise`: roles-and-owner, owner-only, off | both, plus `probe.observations`: verify-before-place, verify-at-plan, on-request |
| Role | tester (verification), researcher plus executor (experiment) | tester | per item | tester or researcher, by kind | tester verifies cold (P29 verifiers); researcher designs the experiment; executor runs it; scorer or blind judge decides |
| Hand-down (P26) | needs a new input on the work order: the probe records at the boundary | the transition record | declared inputs | the asker's re-entry carries the record, as research already does | both edges: the probe record is an input of the next or asking item |
| Cost | about 6 items | a call stack in the engine | about 5 items per step, and every build pays where they run unconditionally | an outcome on 20 templates, plus the program | about 6 items, one record kind, one outcome on 20 role templates |
| **Losing test, written first** | can a role mid-item obtain a result and continue? | can Test's program run before a built range exists? | can static items cover a test "depending on the user request" at an undeclared boundary? | can a test be placed where no role acts? | (i) can a probe before placement write a record with no build? (ii) does it blur the landing verdict? |
| **Result** | **LOSES that path.** Triggers are only "policy, recommendation, or owner's request" (`:420`), and dispose sends records to folds, units or asks, never to the resumed item (`:451`). It wins for points the driver or owner places, at all 81 boundaries | **LOSES.** `test.merge` prepares the landing merge (`:273`), and the contract takes "a built range" (`v2:1171`). Rows into `testing` come only from building and deploying (`:522-529`), and the engine "refuses any transition it lacks" (`:508`). With a different program it becomes A or D under another name | **LOSES.** Coverage is only the declared positions. A conditional skip is a trigger, which is A's mechanism, so C reduces to A's default placements | **LOSES that path.** 61 of 81 items have no role. Deploy (13 commands) and lifecycle (6) are unreachable | **Survives.** (i) The triage pass already runs outside any build and keys its records by content, minting no id (`:100-103`), so an entry-time probe follows the same rule. (ii) Only `test.verdict`'s runner-written record gates the landing, and probe verdicts never feed `deploy.current` |

**What separates the three kinds of testing (under E):**
- A **verification** checks a claim at a pinned SHA. It is evidence for the asking item and blocks nothing beyond that item.
- An **experiment** compares variants over a pre-registered corpus and yields a measured reference that later acceptance cites. It is owner-gated above the agent cap, as the precedent was (`benchmark.md:5`).
- The **landing verdict** is the bar on the prepared merge, Test only, and the one that blocks.
- Every route back counts against `flow.route-backs` (`:32-34`).
- The driver learns that a probe is owed because `next` returns the probe item as the frontier (P22), with the asker held `awaiting`.

6. **Visual verification**

**What the runtime must provide:**
- A `browser` row in each harness adapter's capability table, "measured, never claimed" (`layer-runtime:790`): serve, navigate, set the viewport, screenshot, read the console, evaluate DOM probes.
- A `visual.capture` command adapter that does five things:
  - serves the pinned tree over HTTP, because the pane refused a `file://` open of the 4 MB page (`atlas-instruments.md:18`);
  - busts the browser cache (`:20`);
  - takes declared viewports;
  - writes screenshots to the git common dir, by hash, uncommitted, after the secret scan;
  - returns the console and DOM results.
- Where the capability is absent, the probe is recorded `unrunnable` and becomes an owner item.

**What counts as a witness:**
1. Deterministic DOM, console and layout assertions that the adapter captured at the pinned SHA and the executor can re-run. The atlas's "scroll width equals the window's" (`:190`) is the model.
2. An agent's judgment of a screenshot is `claimed` evidence: an ask, or an owner item, never a route.
3. The owner's own observation is an owner disposition record.
4. A visual defect worth keeping becomes a deterministic probe that has been seen red.

7. **Chain, gaps and forks**

**Units by build:**

| Build | Units to add |
|---|---|
| dDeclaredLoop | the `probe.*` program (`probe.trigger`, `probe.pin`, `probe.design`, `probe.run`, `probe.judge`, `probe.return`); the boundary edge, extending the `review.breakpoints` grammar; the `probe` outcome route; the entry-time keying by content; the keys `probe.points`, `probe.raise`, `probe.observations` and `probe.experiment.authority` |
| dBoundRoles | the `probe` outcome on all 20 role return templates; the tester agent, which does not exist today; the tester's allowance (scratch and the browser capability); the `experiment` shape kind in `workflows.toml`; enforcement of the `none` write class |
| dWitnessedBar | the probe witness (executor re-run); the seen-red recorder as the probe kind `seen-red` (`gap-test-06`) |
| dTotalRecall | the `probe` record kind; the measured-reference kind, under a name that does not collide with retrofit's `baseline` |
| dWellOiledMachine | the browser capability row; `visual.capture`; act binding and shape-run rows for experiment acts |
| dIndexedDesign | its "research harness" becomes the experiment shape |
| dRankedPlan | `plan.record` declares the probes owed before Design |
| dScopedBuild | a red-first reproduction for a patch build that comes from a bug report |
| dCalibratedLens | prices probe cost in the value ledger |

**Gaps to register.** The numbers are provisional, because parallel night-pass researchers may claim the same ones:

| Gap | Severity | Owner | What it records |
|---|---|---|---|
| `gap-flow-16` | HIGH | dDeclaredLoop | no testing outside Test. The code's `TESTING` position (`unattended.sh:852`) was dropped from the design |
| `gap-roles-21` | HIGH | dBoundRoles | no role may run an experiment that writes, and no tester agent exists |
| `gap-mem-28` | MED | dTotalRecall | no probe or measured-reference record kind; "baseline" is ambiguous |
| `gap-rt-22` | MED | dWellOiledMachine | no browser capability and no visual witness |
| `gap-test-18` | MED | (fork F6) | the experiment scorer has two instances and no factory: `bench.py` and `review_replay.py` |

**The owner's forks:**

| Fork | Options | Recommendation |
|---|---|---|
| F1 the mechanism | E; A only (roles return through the existing research route); C | E: A and D each failed a losing test |
| F2 who verifies | the tester, cold; the asking role, warm; the researcher | the tester. P29 lists the tester among the verifiers, and the `[class]` rule keeps a guard's state apart from what it guards |
| F3 `probe.experiment.authority` | owner-opts-in; within-cap; free | owner-opts-in: 195 agents in one re-run (`benchmark.md:133`) |
| F4 `probe.observations` | verify-before-place; verify-at-plan; on-request | verify-before-place |
| F5 the name of the measured reference | `measure`; `benchmark`; `baseline` with a subkind | `measure`, to avoid colliding with retrofit's kind |
| F6 the scorer factory's owner | dFairHearing, which runs the replays first; dWitnessedBar, beside its ledger factory; dBoundRoles | dFairHearing, because it comes earliest and already owns `review_replay.py` |

The aScoutedSeam source files are on the branch only. The offline grader copies I ran are in `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\ass\`.

Files I relied on:
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-16-build-PLAY-dClosedLoop-1-systems.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-16-build-PLAY-dClosedLoop-1-atlas-instruments.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\unattended\unattended.sh`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\hooks\scratch-guard.js`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\workflows\review_replay.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\memory-tree\backlog.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\.claude\roles.json`
