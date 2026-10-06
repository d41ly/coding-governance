# TOOL-aMendedFleet-73 — the vague-brief trial arm: a full spec against a short plan, on a three-sentence brief

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 73

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-73-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-73-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-build-TOOL-aMendedFleet-73-brief.md](../build/2026-10-06-build-TOOL-aMendedFleet-73-brief.md) | journal | — |
| [2026-10-06-build-TOOL-aMendedFleet-73-freeze.tsv](../build/2026-10-06-build-TOOL-aMendedFleet-73-freeze.tsv) | journal | — |
| [2026-10-06-build-TOOL-aMendedFleet-73-harness.py](../build/2026-10-06-build-TOOL-aMendedFleet-73-harness.py) | journal | — |
| [2026-10-06-build-TOOL-aMendedFleet-73-hidden-suite.py](../build/2026-10-06-build-TOOL-aMendedFleet-73-hidden-suite.py) | journal | — |
| [2026-10-06-build-TOOL-aMendedFleet-73-results.tsv](../build/2026-10-06-build-TOOL-aMendedFleet-73-results.tsv) | journal | — |
| [2026-10-06-build-TOOL-aMendedFleet-73-trial-report.md](../build/2026-10-06-build-TOOL-aMendedFleet-73-trial-report.md) | journal | — |
| [2026-10-06-build-TOOL-aMendedFleet-73-trial.js](../build/2026-10-06-build-TOOL-aMendedFleet-73-trial.js) | journal | — |
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

The aBlindedTrial build ran three arms on three explicit briefs: build from the brief (B), write a
40-line plan and build (P), and this repo's full spec route (S). Every tool passed its hidden suite,
the defect counts did not separate, and S cost 12.3 times B in output tokens while P cost 1.1 times.
Its own report named the untested case: a three-sentence owner brief, where a spec has the most room
to help. The report this build answers asks for that arm, P against S, because it decides whether the
charter's §1 design pass keeps a full Tier-2 spec or shrinks to a plan `[B#19] [B#43]`. The first
trial's instruments lived under `%TEMP%` and are gone. This unit runs the vague-brief arm with every
instrument and every result row committed to this build's folder, and records a reading whose
decision rule is written down before any arm runs. It reports; it changes no rule.

## 2. Scope (IN)

- **S1** — THE BRIEF AND THE HELD-OUT INTENT. A journal record under this build's `build/` folder
  carries three things verbatim: the vague brief in §4, the full Task A brief it was cut from, copied
  from the aBlindedTrial briefs journal, and the DECISION LIST. That list names every behaviour the
  full brief pins and the vague brief leaves open, one numbered `D<n>` row each with a one-line probe
  hint, and holds at least the fourteen rows §4 lists. Observed by AC1.
- **S2** — THE HARNESS. One Python file under `build/`, standard library plus the installed pytest,
  with six verbs. `cells` makes ten cell repositories under a short `%TEMP%` root, each holding only
  the vague brief, and the S cells also the spec skeleton from `memory/TEMPLATE-SPEC.md`, plus an
  eleventh for the pilot; `cells --blind` copies the ten built tools and the exit-0 stub under salted
  code names and keeps the key outside the blind directory. `freeze`
  writes the sha256 of the hidden suite and of the decision list to a committed rows file. `stub` runs
  the suite against an exit-0 stub. `hidden` runs the suite against each cell's tool and writes
  per-tool pass counts by tag. `tokens` sums each agent's output tokens and joins them to a cell by
  the prompt tag. `aggregate` reads committed rows only and prints the per-arm means, the exact
  two-sided permutation p over all 252 five-against-five splits, and the verdict word of §4;
  `aggregate --collect` first unblinds the scorers' marks and records them with the judges' marks.
  `--selftest` asserts the permutation p and the verdict rule.
  Observed by AC2, AC3, AC6 and AC7.
- **S3** — THE HIDDEN SUITE, written from the full brief by an agent that has seen no implementation,
  because none exists when the unit pass writes it. Its tests reach a tool only through what the
  vague brief pins: the file name, the registry's name and row shape, and the `tools/` directory.
  Each test is tagged `intent`, a behaviour the vague brief's stated purpose implies, or `contract`,
  a spelling only the full brief pins. The hidden measure is the `intent` pass rate. Observed by AC2
  and AC3.
- **S4** — THE TRIAL WORKFLOW. One Workflow script under `build/`, run once by the main loop, in six
  stages. Fan-out goes only through `boundedParallel(thunks, 5)`, inlined from
  `tools/workflows/tier2-review.js`, and every agent's prompt opens with a tag naming its cell or
  stage. A script runs no command, so two runner agents run the harness verbs between stages: one
  grades the pilot, one grades the arms and blinds the tools. Observed by AC4, AC5 and AC8.
  1. A suite verifier re-tags any test asserting more than its tag allows, then runs `freeze` and
     `stub`.
  2. A pilot agent builds from the vague brief with no document, and `hidden` grades it. Above 0.8
     on `intent`, the measure has no headroom: the workflow stops, and the record says so.
  3. The arms, five cells each. P is one agent that writes a `PLAN.md` of at most 40 lines and then
     builds. S is one agent that writes a Tier-2 spec to the skeleton and resolves every §8 fork itself,
     then a different agent that builds from that spec and bumps its rev before diverging from it.
  4. Decision probes. The ten tools under salted code names, plus the exit-0 stub as a planted
     negative control, are split across at most four agents. Each probe agent writes, per tool and
     per `D<n>`, the command it ran, its fixture and the observed output.
  5. At most two blind scorers mark each tool and decision met, unmet or contradicted, from those
     observations and the full brief alone.
  6. At most two document judges mark each P plan and S spec, per decision, decided-compatible,
     decided-incompatible or silent; one judge reads the five plans, the other the five specs.
- **S5** — THE RECORD. The result rows and a trial-report journal under `build/`. Every figure names
  the committed rows file and the harness verb that derives it, the report carries an acceptance
  ledger, and a section says what the arm cannot show. Observed by AC6 and AC7.
- **S6** — THE ROUTE. The unit pass authors S1 to S4 and commits them with this spec at INPROGRESS.
  It returns to the main loop the need to run the workflow, because a pass runs in a sidechain that
  cannot spawn agents. The main loop runs S4, then commits S5 and sets this spec CLOSED. Observed by
  AC8.

## 3. Non-goals (OUT)

- Changing the charter's §1, the template or any rule. The record recommends; an owner-approved unit
  acts on it.
- A B arm. The fork §1 faces is a full spec against a plan, and no rule proposes building a Tier-2
  unit with no design document. The pilot is one B-shaped reading, reported and never compared.
- The spec audit in the S arm. It became opt-in at aBlindedTrial units 2 to 5, and this repository's
  conf declares no default, so today's S route has none.
- A blind finder and skeptic review. In the first trial every arm carried the same defect classes,
  and the confirmed counts did not separate (p of 0.82 or more). The question here is intent
  recovered, and the decision probes measure that directly.
- A standing eval built from history, briefed from owner prompts. The report sequences it after this
  arm, and its do-not-build list forbids a general experiment framework before a second experiment
  exists.
- Recovering the first trial's lost instruments. Its record keeps their figures; this unit writes its
  own.
- The rule that an experiment's instruments are committed. That is `PLAY-aMendedFleet-2`; this unit
  obeys it.

### Edges

- **hands-off** `PLAY-aMendedFleet-2` — that unit files the HIGH ask gating §1 on this arm, which the
  record here answers.
- **hands-off** external — any change to the charter's §1 design-pass rule that the reading supports.

## 4. Design

### Evidence

Read at base `7af5f564` on 2026-10-04.

- The first trial's record, the aBlindedTrial unit 1 trial report, measured per-cell means of 21.2 k
  output tokens for P and 235.7 k for S. S split as spec 37.0 k, audit 141.4 k, fold 30.2 k and
  build 27.1 k. Its hidden suites passed at 100% in all 27 cells. On the open points its tools were
  79 of 100 unanimous. Its section 6 names the vague-brief case as untested.
- Its scratch root, `C:/Users/daily-agent/AppData/Local/Temp/xp/`, holds 0 files: the briefs, the
  cells, the results and every script are gone. Its record cites `retro.py`, `harness.py` and the
  workflow scripts by name only, and the briefs survive only because a journal copied them. PINNED,
  `find` over that root on 2026-10-04.
- `.unattended.conf` declares `SPEC_AUDIT_DEFAULT=""`, so no audit is owed by default.
- `python -c "import pytest"` on node a reports 9.1.1.
- `tools/runlog/extract.py` resolves a session's tree including its `subagents` directory and reads
  `usage` events per request (`resolve_session_tree`, `read_records`, `build_usage`). That is the
  token seam S2's `tokens` verb reuses instead of a new transcript reader.
- A Workflow script is found by its `export const meta` marker. `tools/workflows/check-workflow-syntax.js`
  parses every such script git can see, and `tools/hooks/agent-cap.js` reads the `scriptPath` it is
  handed. Both reach a script outside `tools/workflows/`.
- Build folders already hold non-markdown instruments under `build/`: a `.py` census in aHonedRuleset,
  a `.sh` probe in dSealedTally, `.tsv` rows in dDerivedDocket. No `.js` is there yet; AC9 observes
  that hygiene admits one.

### The vague brief, verbatim

> Our kits live as subdirectories of `tools/`, and a `kits.toml` at the repository root lists them
> as `[[kit]]` rows, each with a `name` and a `path`. Write `declared.py`, a Python 3
> standard-library-only checker we can run as a merge-bar leg, that tells us when the directories and
> the registry have drifted apart. A few kits are deliberately unlisted, so give us a way to exempt
> them.

It pins only what any test needs in order to reach the tool. It drops the three finding tokens, the
exit codes 0, 1 and 2, the waiver file's name and grammar, the stale-waiver rule, `--preview`,
`--root`, and determinism.

### The decision list — the floor the journal starts from

| D | the full brief pins |
|---|---|
| D1 | exit 0 on a clean tree |
| D2 | a non-zero exit on any finding |
| D3 | a misconfiguration exit distinct from a finding exit |
| D4 | an undeclared kit directory is a finding naming its path |
| D5 | a declared path that is not a directory is a finding naming the kit |
| D6 | exemptions live in a file beside the registry, one path per line |
| D7 | a blank line and a `#` line in that file are ignored |
| D8 | an exemption that no longer exempts anything is itself a finding |
| D9 | a non-failing preview mode prints the same findings |
| D10 | the tree to check can be named, defaulting to the current directory |
| D11 | one line per finding, on stdout |
| D12 | the same tree gives the same bytes |
| D13 | only immediate subdirectories of `tools/` are kits |
| D14 | an unparseable registry or a row missing a field is a misconfiguration, explained on stderr |

The unit pass may add rows from the full brief and may not remove one.

### The reading, registered before any arm runs

The primary measure is a tool's decision-met rate, from stage 5. `aggregate` prints `S-BETTER` when
the S mean exceeds the P mean by at least 0.10 with exact p at most 0.05, and `P-BETTER` for the
mirror case. It prints `NO-DIFFERENCE` when the means differ by less than 0.10 and p exceeds 0.05,
and `INCONCLUSIVE` otherwise. The record states that word, the `intent` pass rates, the document
decision coverage, and the S-to-P output-token ratio beside it. Five replicates per arm are chosen
because three cannot reach p below 0.1 on an exact two-sided test, so with three no result could
change the reading.

### Liveness, per instrument

- The hidden suite: the exit-0 stub fails every test (AC2).
- Headroom: the pilot scores at most 0.8 on `intent`, or the workflow stops (AC3).
- The probes: the planted stub scores a decision-met rate of at most 0.25. It legitimately meets D1
  and D12 and little else, so a higher rate means the probes or the scorers are not discriminating
  (AC5).
- Tokens: every agent's usage joins to a tag, and none is left unattributed (AC7).

### Inventory

New files, all under this build's `build/` folder, named by hygiene check 5's grammar with the
suffixes `-73-brief.md`, `-73-harness.py`, `-73-hidden-suite.py`, `-73-trial.js`, `-73-freeze.tsv`,
`-73-results.tsv` and `-73-trial-report.md`. The harness's Python definitions take a verb from the
declared table in `.lexicon.conf`; `python3 tools/lexicon/lexicon.py --suggest` answers each.

### Files touched (estimate)

- `memory/builds/aMendedFleet/build/`
- `memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-73.md`

### Cost

About 27 agents: one verifier, one pilot, two runners, five P, ten S, four probes, two scorers and
two judges.
Output tokens are estimated at 0.6 to 0.7 million from the first trial's per-step means, which is
UNVERIFIED for a vaguer brief. Concurrency never exceeds five.

### Alternatives rejected

- **A hidden suite alone as the primary measure.** On a vague brief it either floors, because no
  tool can guess the full brief's spellings, or it saturates on the few behaviours the brief pins.
  The decision probes adapt to each tool's own interface, which is the only way to grade intent
  recovered.
- **A real owner prompt from history as the brief.** Its truth would be a multi-file change to this
  repository, which no cell can hold, and its acceptance was written by the same route under test.
- **Running the arms inside the unit pass.** A sidechain agent cannot spawn one, and a single agent
  playing every arm destroys the arms' independence.

## 5. Production-readiness checklist

- security — cells are scratch git repositories under `%TEMP%`, each forbidden to read outside itself;
  no secret enters a prompt, and every agent writes only inside its cell or this build's `build/`.
- perf / scale — about 27 agents, never more than five at once; one Workflow call.
- error / empty / loading states — a session limit kills workflow agents silently, so the main loop
  resumes the run by its id; a cell with no tool scores 0 and is named, never dropped.
- observability — every agent's prompt carries its tag, and the record names every stage's count.
- risks — the judges and the builders are one model family. Five replicates still bound the
  detectable effect, which the record states. The `.js` under a build folder is new, and AC9 covers
  it.
- testing — AC1 to AC9; the instruments carry their own liveness controls.
- migration — none.
- user docs — the trial report is the deliverable.

## 6. Acceptance criteria

- **AC1** — When `grep -c "^| D[0-9]"` runs over the brief journal this unit commits, it prints at least
  14, and the journal quotes the vague brief byte-identical to §4.
  Red when: a §4 decision row is missing, or the brief drifted.
- **AC2** — When the harness's `stub` verb runs, every hidden test fails against the exit-0 stub, and
  `freeze` has written two sha256 rows that `hidden` asserts before it grades.
  Red when: any test passes the stub, or `hidden` grades a suite whose hash moved.
- **AC3** — When stage 2 has run, the `hidden` verb prints the pilot's `intent` pass rate, and stage 3
  starts only when that rate is at most 0.8.
  Red when: the arms run on a measure the pilot already saturates.
- **AC4** — When `node tools/workflows/check-workflow-syntax.js` and
  `bash tools/workflows/check-verifier-fanout.sh` run with the trial script committed, both exit 0,
  and `tools/hooks/agent-cap.js`, fed a Workflow tool-call payload naming that script on stdin, exits
  0.
  Red when: the script fails to parse, or the hook denies its fan-out.
- **AC5** — When stages 4 and 5 have run, the planted stub's decision-met rate printed by `aggregate`
  is at most 0.25; when the workflow stopped at AC3's headroom guard, stages 4 and 5 did not run and
  the trial report says so.
  Red when: the stub scores higher, which means the probes cannot tell a tool from nothing.
- **AC6** — When `aggregate` runs from a fresh `git clone --local` of the unit's tip, with no
  `%TEMP%` state, it prints the record's results table byte-identical, the exact p over 252 splits and
  one of the four verdict words; after a headroom stop it holds no score row and exits as a DEAD
  PROBE, and the committed rows file carries the pilot's grading rows the report quotes.
  Red when: a figure needs a file outside the repository, or the record and the rows disagree.
  cost: seconds; the arms themselves are the main loop's, at the estimate in §4.
- **AC7** — When the `tokens` verb runs over the workflow's session tree, it reports a per-tag
  output-token sum for every agent the trial spawned, and 0 untagged agents when the trial ran in a
  session of its own; in a shared session the other workflows' agents count as untagged.
  Red when: an agent's usage joins no tag.
- **AC8** — When `git log --format=%s` lists this build's commits naming the unit, the commit adding
  the harness, the suite and the workflow precedes the commit adding the result rows, and the spec
  reads CLOSED only in the second.
  Red when: results land without committed instruments, or the unit closes before the arm ran.
- **AC9** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs at the unit's tip, it names
  none of the files this unit added.
  Red when: a check refuses the `.js` or `.py` instruments under `build/`, or the report's binding.
  cost: about a minute.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `workflow script syntax` · `verifier fan-out` · `lexicon naming predicates` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: none · the instruments carry their own liveness controls (AC2, AC3, AC5), and a suite arm over a one-off experiment would be the framework the report forbids · none

## 8. Open questions

- **F1 — Which arms run?**
  Options: P against S, as the report names; B, P and S, as the first trial's record proposed. The
  §1 question is a full spec against a plan, and B adds five builds and five probe rows that answer
  nothing §1 asks.
  RESOLVED (agent, 2026-10-04, delegated): P against S, with the pilot as one reported B reading.
- **F2 — Does the S arm include the spec audit?**
  Options: the first trial's S, with the audit; today's default S, without it. The audit was made
  opt-in after the first trial, and the reading must describe the route a session takes today.
  RESOLVED (agent, 2026-10-04, delegated): no audit, per S4 stage 3.
- **F3 — What is the primary measure?**
  Options: the hidden suite's pass rate; the decision-met rate from probes; the document decision
  coverage. A brief-shaped suite cannot grade intent the brief omits, and coverage grades the
  document rather than the tool.
  RESOLVED (agent, 2026-10-04, delegated): the decision-met rate, with the other two reported.
- **F4 — How many replicates?**
  Options: three, matching the first trial; five. At three per arm, the smallest exact two-sided p is
  0.1, so no outcome could reach the registered threshold.
  RESOLVED (agent, 2026-10-04, delegated): five.
- **F5 — Who runs the arms?**
  Options: the unit pass; the main loop after the unit pass; a second unit. A pass runs in a sidechain
  that holds no spawn tool, and a second unit would still need the main loop.
  RESOLVED (agent, 2026-10-04, delegated): the main loop, per S6.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft; the first trial's record re-read, its scratch root found empty,
  and the arm designed with a decision rule registered before it runs.
- rev-2 · 2026-10-06 · S2 · S4 · §4 · §5 · the unit pass found three things the design needed and did not
  name: the pilot needs a cell of its own, so `cells` makes eleven; the scorers must not see which
  cell built a tool, so `cells --blind` and `aggregate --collect` carry the salted names and the
  unblinding inside the six verbs; and a Workflow script runs no command, so two runner agents run
  the grading verbs, which moves the agent estimate from 26 to 27.
- rev-3 · 2026-10-06 · AC5 · AC6 · AC7 · the main loop ran the trial once and it stopped at the
  pilot: intent 10 of 10, above the 0.8 guard, after three agents. AC5 and AC6 gain the stop's
  branch, since stages 4 and 5 never ran. AC7 read every agent as untagged because the Workflow
  harness prefixes a preamble to each prompt, so the `tokens` verb now searches for the tag instead
  of matching it at the start; and the verb reads the whole session tree, so 0 untagged holds only
  for a trial run in a session of its own. The unit closes on the stop.

## 10. Reuse audit

The seams reused are the first trial's design, from the aBlindedTrial unit 1 trial report and its
briefs journal; `boundedParallel` from `tools/workflows/tier2-review.js`; and the transcript readers
in `tools/runlog/extract.py` for the token join. No existing seam fits the harness itself:
`python tools/codebase-map/reuse_lookup.py "run a blinded comparison of build arms against a frozen
hidden suite and compute a permutation test"` returned only name-stem neighbours such as `run`,
`build_index` and `compute_coverage`, none of which runs a trial, and the first trial's own harness
no longer exists anywhere on node a. Recall returned the aBlindedTrial unit 1 spec, its parked
"fourth task with a deliberately vague brief", its trial report's saturated-suite section, and the
briefs journal. Where the report and the tree disagree: the report reads as though an instrument
could be reused from the first trial; none survives.

Recall terms used: `python tools/memory-recall/query.py "does writing a full spec before code beat a
short plan when the owner's brief is vague" --terms "blinded trial vague brief plan-lite spec-first
arm hidden suite saturated edge probes replicates permutation instrument TEMP"`
