# TOOL-aRoutedQuill-6 — routed against raw: a paired trial on frozen clones of real repositories

**Status:** DEFERRED · rev-5 · 2026-10-09 · node a · Tier-1 · base 6473ae38 · streams tooling · order 6 · advances TOOL-aRoutedQuill-8 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md) | journal | TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-7 |

<!-- /gen:spec-records -->

## 1. Goal

This build routes every product-code write through orientation, a committed brief and a specced
unit, and enforces that from landing. No record shows that routing improves the code. The blinded
trial measured spec-first against build-first on three standalone one-file tools and could not
separate the arms, and the vague-brief rerun stopped at its pilot. This unit runs a raw arm and a
routed arm on real tasks inside frozen clones of real repositories. It grades them blind against the
decisions the owner actually made, under a decision rule committed before any arm runs. The reading
becomes asks to keep, re-tier or relax the Tier-1 route; the trial changes no rule itself.

The hypothesis: on in-repo tasks, the routed arm meets more of the owner's held-out decisions than
the raw arm, by a paired mean of at least 0.10 at exact p of at most 0.05. It holds only while the
routed arm carries no more confirmed blocker-or-high defects and no more duplicated seams. A reading
of NO-DIFFERENCE or RAW-BETTER, with both controls live and the pilot showing headroom, refutes it.

## 2. Scope (IN)

- **S1** — THE TASK REGISTRY. A committed `tasks.tsv` under this build's `build/` folder, one row per
  task: repository, base sha, landed range, fix commits, the owner's first message and where it was
  read, the follow-on prompt or `none`, and the stratum. Strata cross vague with clear and small with
  cross-cutting, at the quota §8 F2 settles, chosen by the deterministic rule in §4 "The tasks". The
  harness's `tasks` verb validates every row. Observed by AC1.
- **S2** — THE HIDDEN DECISION LISTS. One list per task and per follow-on, authored from the landed
  range, its fix commits and the owner's own turns, each row citing the owner turn that decided it
  and tagged `stated` or `held-out` against the prompt bytes. A verifier re-checks each list, and
  `freeze` hashes it. Two controls per task bound the instrument: the untouched base and the landing
  plus its fixes. Observed by AC2 and AC10.
- **S3** — THE FROZEN CLONE. Per task, a `git clone --local` under a short `%TEMP%` root, cut to the
  base with no later object reachable, then given gov at the build's landing tip with the
  repository's `ROUTED_PATHS` value and its dependency install. The template is never written again,
  and every cell is a copy of it. Observed by AC3.
- **S4** — THE ARMS. A raw cell and a routed cell per task, and an orientation-only cell if §8 F1
  admits it, identical except for the wiring and, for the orientation arm, one opening line. Each
  cell runs one headless session under the same model, turn cap and wall ceiling, followed by the
  task's follow-on prompt in the same mode. Each session ends in an outcome from a closed set and
  proves its work by a product commit. Observed by AC4 and AC5.
- **S5** — THE OWNER PROXY. A fresh headless call per question, holding only the task's decision list
  and the frozen proxy instructions, answering one decision per question. Observed by AC6.
- **S6** — BLIND GRADING. Code-named trees per task, built from the template plus each tree's product
  patch with every arm-minted id neutralised. Decision probes and blind scorers grade them, as do
  finders over two lenses, defects by severity and duplicated seams, with batched skeptics. The
  clone's own merge bar runs once at each build cell's end sha. Observed by AC7 and AC10.
- **S7** — VALIDITY GUARDS. A contamination audit over every session's transcript tree, the two
  controls, the finder's positive control, and a `--selftest` holding the audit and the reading.
  Observed by AC8 and AC10.
- **S8** — COST. Per session, output, cache-write and cache-read tokens from its own transcript tree,
  spend before READY for the routed and orientation sessions, driver-clock wall and owner turns. Per
  grading agent, tokens joined by prompt tag in the orchestrator's session. Observed by AC5 and AC11.
- **S9** — THE PILOT. Two tasks, one raw and one routed cell each, graded with the controls before the
  main arms. It stops the trial on no headroom, a dead control or a route that never engaged.
  Observed by AC9.
- **S10** — THE READING AND THE RECORD. The rule in §4 "The reading", committed with the instruments
  before the pilot runs. The result rows and a trial report under `build/` carry an acceptance ledger
  and a section on what the trial cannot show. The closing commit files the asks §4's outcome table
  names, and nothing else. Observed by AC8, AC10, AC12 and AC13.
- **S11** — THE ROUTE. The unit pass authors S1 to S8's instruments and commits them. The main loop
  runs every stage in an attended session of its own, behind four owner asks. Observed by AC12.

## 3. Non-goals (OUT)

- Changing enforcement. The gate enforces from landing (D4); a reading becomes asks, and an owner
  ruling acts on them.
- The plan-against-spec question. `TOOL-aMendedFleet-109` asks it on the vague brief and stays open;
  this trial compares the shipped route with no route.
- A spec audit in the routed arm. None is declared for this build (D5), so the shipped route has
  none.
- Testing the gate, the push leg or the subagent hook. Their own units observe them; the trial uses
  them as shipped.
- The unattended route. Arms run headless with a proxy; a run under the unattended driver is a
  different mandate and is not measured.
- A shared trial framework. The harness adapts the aMendedFleet-73 kit by copy; promoting either
  into a kit is a follow-up once a third trial exists.
- Tasks larger than one session's context, and multi-node work.

### Edges

- **consumes-from** `TOOL-aRoutedQuill-5` — the default install that wires the gate, scaffolds
  `ROUTED_PATHS` and makes `check-wiring.sh` red an unwired or unarmed tree. Without it the routed
  cell is hand-wired, a configuration no adopter receives, and the raw cell cannot prove it is raw.
- **consumes-from** external — the aMendedFleet-73 trial kit under
  `memory/builds/aMendedFleet/build/`: its harness verbs, decision-list grammar, blind code names,
  probe-then-scorer split, token tag join and verdict-rule shape, adapted by copy. A later change to
  that kit does not reach this trial.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- The blinded trial built nine tools per arm and confirmed 21, 21 and 19 defects, with
  blocker-or-high at 8, 6 and 4, and no contrast below p = 0.23
  (`memory/builds/aBlindedTrial/build/2026-09-20-build-TOOL-aBlindedTrial-1-trial-report.md:117`
  to `:128`). Its F3 kept in-repo tasks out because they measure reuse of existing seams
  (`memory/builds/aBlindedTrial/spec/2026-09-20-spec-TOOL-aBlindedTrial-1.md:194`). That reuse is
  part of what this unit measures.
- Brief-derived hidden suites saturated twice: 27 of 27 tools at 100%, and the aMendedFleet-73
  pilot at intent 10 of 10 (its trial report, line 18). That report names the decision list as the
  instrument with room (line 31), and `TOOL-aMendedFleet-109`
  (`memory/builds/aMendedFleet/BACKLOG.md:10`) asks for its rate as the primary measure behind a
  pilot headroom check. `PLAY-aMendedFleet-6` (`memory/DECISIONS.md:222`) kept the full Tier-2
  design pass without a reading.
- The aMendedFleet-73 harness carries the verdict-rule shape (`derive_verdict`, harness lines 362 to
  369) and a planted-stub liveness line that reds above 0.25 (lines 419 to 430). Its token join
  searches the whole first prompt for the tag because the Workflow harness prefixes a preamble (line
  285). In a shared session the other workflows' agents read untagged (trial report, line 41).
- Its script fans out only through `boundedParallel` over marked literals (trial.js lines 39 to 44
  and 58 to 62), which `tools/hooks/agent-cap.js` allowed on 2026-10-06 (its ledger, AC4).
- `tools/runlog/extract.py` resolves a session's tree (`resolve_session_tree`,
  `tools/runlog/extract.py:266`), streams its records (`:308`) and finds its READY point
  (`derive_ready_point`, `:1152`). Orientation costs a median of about 66.7K tokens and 6.7 minutes
  before READY over 23 sessions
  (`memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-70.md:15`). Its effect on
  code was never measured
  (`memory/builds/aWeighedCompass/build/2026-09-04-build-TOOL-aWeighedCompass-1-findings.md:502`).
- `tools/workflows/orient-counterfactual.js` measures orientation cost and never code. Its runs end
  in a closed `outcome`, so a dead arm is a named value (lines 23 to 29), and a matched pair runs
  sequentially so neither measures the other's load (lines 9 to 14).
- A headless session is the in-repo precedent for a run with no owner turn:
  `tools/unattended/resume-tick.sh:358` launches `claude -p --resume` with
  `--dangerously-skip-permissions` and `--max-turns`. A PreToolUse deny reaches the model, and
  `claude -p --bare` skips hooks (the contract's survey of the hook documentation, 2026-10-09).
  Whether a deny still fires under `--dangerously-skip-permissions` is UNVERIFIED; the pilot
  observes it.
- Source repositories on node a, PINNED 2026-10-09 by `grep -l "^## The prompt"` over each tree's
  prompt records: coding-governance 24, `C:/projects/incms/main` 7, `C:/projects/nicocares/main` 2.
  Both adopters carry `.memory-tree.conf`, with 8208 and 3249 commits. Most first messages
  therefore come from session transcripts, read through `runlog.py narration`
  (`tools/runlog/README.md:145`).

### The arms

| Arm | Wiring | Prompt | What it isolates |
|---|---|---|---|
| raw | gov at the landing tip, the write gate unwired | the owner's first message, byte for byte | today's adopter, without enforcement |
| routed | the same install, wired as `TOOL-aRoutedQuill-5` wires it | the same bytes | the shipped route: gate, kickoff brief, a spec per unit, the unit harness where the route takes it |
| orient (§8 F1) | the same install, the gate unwired | the same bytes, opened with one line asking for `/session-kickoff` | orientation and the brief, without the gate or the spec |

Fixed across arms: the model, the turn cap summed over a session's invocations, the wall ceiling,
the disallowed web tools, the proxy instructions, and the frozen template the cell is copied from.
Every arm session runs on Opus 5.5 (`claude-opus-5-5`) at Medium reasoning effort, by the owner's
ruling of 2026-10-09, which amends an earlier High. Every other agent the trial spawns, Workflow
agents included, runs at High and never Extra. The pilot records the settings that pin both, which
are UNVERIFIED for a `claude -p` session today. The owner registers the turn cap and the wall
ceiling at Ask A. Both arms of one task run in the same wave, so a load spike hits the pair. Cells
are scored as assigned, never by what they did: a routed cell whose route did not engage, such as
one that wrote through Bash, is scored as routed and named.

### The tasks

The pool is every owner first message that started a build, read from a prompt record's
`## The prompt` or from the first owner turn of the session's transcript. A message is eligible when
all of these hold:

1. The landed range is attributable: its subjects name the unit or the build slug.
2. The base is the parent of the build's first commit, so neither its spec nor its brief exists there.
3. Its fix commits, when any, are later commits naming the unit or build that touch its product files.
4. The repository's merge bar completes at the base in a frozen clone.

Size is derived: small when the landed range touches at most two files under the repository's
product paths, cross-cutting otherwise. Clarity is classified at selection: clear when the message
states at least one observable acceptance, such as an output, an exit status or a named test, and
vague otherwise. The quoted clause is recorded in the row. Within each stratum, rows are taken in
ascending sha1 of `<repo>:<slug>` until the quota fills, so nobody picks tasks. A follow-on is the
next owner first message that built on the task's landed product files, or `none`.

One replicate per arm per task. The comparison is paired by task, which takes out between-task
variance, the largest source in real work. Twelve paired tasks give an exact two-sided sign-flip
test over 4096 assignments. The blinded trial's nine unpaired builds per arm could not separate 19
defects from 21.

### The decision lists and the controls

The `lists` stage of the trial script writes one list per task and per follow-on. An author agent
reads the source repository at the landed range, its fix commits and the owner's turns. Each row
`D<n>` is one behaviour the owner decided, with a probe hint and an owner citation: a prompt-record
line, an owner-resolved §8 mark, or a transcript turn by session id and time. A verifier tags each
row `stated` or `held-out` against the prompt bytes. It rejects three kinds of row: one backed only
by an agent-resolved fork, one only a file under the memory root can show, and one no probe can
observe. A probe hint names a command against the tree, or a read of the code when no command can
observe the row; a read row is tagged `static` and its rate is reported apart.

Two controls per task bound the instrument. The `base` tree, the template with nothing built, must
meet at most 0.25 of the held-out rows. The `truth` tree, the landing plus its fixes, must meet at
least 0.8 of all rows. A task failing either is named and left out of the reading. When more than a
quarter of the tasks fail, `aggregate` prints `DEAD PROBE` and there is no reading.

### The frozen clone

`build_frozen_clone` clones with `git clone --local` under `%TEMP%/rq6`, because a clone under the
scratchpad path fails on MAX_PATH. It points the one branch at the base, deletes every other ref and
remote, expires the reflogs and prunes. `check_no_future` then asserts the landed sha is no object
of the clone. Paths are compared resolved, never as strings, because `%TEMP%` is an 8.3 short name
on node a. A `rev:path` read uses `git ls-tree`, because MSYS mangles the colon form.

Gov is then brought to the build's landing tip through `tools/govkit/govkit.py`, the adopter path
`TOOL-aRoutedQuill-5` ships. The registry's `ROUTED_PATHS` value is written into the clone's
`.memory-tree.conf`, and the repository's dependency install runs once. That is the template's one
commit above the base. Whether govkit completes over a historical adopter tree is UNVERIFIED; a
repository where it does not is named and leaves the pool. A cell is a file copy of the template,
dependencies included, with a local bare repository as its `origin`.

### Running an arm

The `run` verb starts one headless session per cell with `claude -p` in the cell, never `--bare`,
with identical flags for every arm. Those flags include `--dangerously-skip-permissions`, inside the
frozen clone only, as `tools/unattended/resume-tick.sh:358` launches a run (F5). At most the hook's bound runs at once: `CAP` in
`tools/hooks/agent-cap.js:85`, 5 at `6473ae38`. The hook cannot see a `claude -p` process, so the
driver holds the bound itself.

When a session ends its turn, its last message goes to the proxy. An answer resumes it with
`--resume`, and `DONE` closes it; each resume is one owner turn. The session ends in one outcome:

| Outcome | Meaning | Scored as |
|---|---|---|
| `built` | at least one commit touches the product paths | its trees |
| `no-product` | the session closed with no product commit | 0, named |
| `ceiling` | the turn cap or the wall ceiling stopped it | the trees that exist, named |
| `dead` | the process exited with no closing message | 0, named |
| `contaminated` | the audit found an outside read twice | 0, named |

`check_contamination` scans the session's whole transcript tree for a tool input naming a path
outside the cell and an allowlist, which holds the session's scratchpad and the Claude config
directory. A web call is a hit too. A first hit re-runs the cell in a fresh session. A second scores
0. The audit matters because a clone's own `AGENTS.md` names the source repository's path.

For a routed or orientation cell, the row also records the routing observations: a committed brief,
a spec committed before the first product commit naming its unit, and a `## route` line on the card.
These are observations, not filters.

After the build, the cell runs the task's follow-on prompt in the same mode on top of its end state.
The route is a standing property of an adopter's tree, so the follow-on asks whether living under it
makes the next change better or cheaper.

`measure_bar` runs the clone's own merge bar once at each build cell's end sha. Bars run serially, one
per host, with no retry, and the arm never sees the result. Legs red at the base and the ownership
leg `TOOL-aRoutedQuill-3` ships are excluded and listed, so raw is not charged for routing it was
never asked to do. The repository's own legs and gov's record legs are reported apart.

### The owner proxy

The proxy is one fresh headless call per question. It holds the task's decision list, the frozen
`proxy.md` and the question, and no tool. It answers one decision per question, or "your call" when
no row covers it, and refuses to enumerate decisions. It confirms a brief, approves a scope, and
answers yes to a Workflow request, under the standing line the owner approves at Ask C. Each answer
names the row it drew on, so every cell's met rows split into asked and unasked. That split shows
whether routing pays by asking or by building.

### Grading

One Workflow call per stage, each prompt opening with `[rq6:<tag>]`. Fan-out copies the
aMendedFleet-73 shape: `boundedParallel` over marked literals no wider than the hook's bound, with
the picking done inside the thunk.

1. `blind` writes code-named trees per task: raw, routed, orient when run, base, truth, and
   first-landing, the landing before its fixes. Each is the template plus that tree's product patch.
   Files under the memory root are excluded, and `render_blind_patch` rewrites every id the arm
   minted to a neutral token. The key file sits outside the blind root.
2. Probe agents read only the task's decision list and the blind trees. They write the command, the
   fixture and the observation per tree and per row, and judge nothing.
3. Two blind scorers mark each row met, unmet or contradicted from the observations and the list.
4. One finder per task group reads the base and each code-named patch under two lenses. One lens is
   defects by severity. The other is new definitions duplicating a base seam, each citing both
   `file:line`. First-landing is the finder's positive control: the defects its fix commits repaired
   should appear among its confirmed findings.
5. Skeptics, batched, at most `MAX_VERIFIERS` (`tools/hooks/agent-cap.js:470`) for the whole stage,
   default to refuted, as the hard cap in `memory/guides/REVIEW-PROTOCOL.md:9` requires.

### Measures

| Measure | Role | Instrument | Liveness |
|---|---|---|---|
| decision-met rate, held-out rows | primary | probes, then blind scorers | base at most 0.25, truth at least 0.8 |
| decision-met rate, all rows, split asked and unasked | reported | the same | the same |
| confirmed defects, all and blocker-or-high | secondary | finder, then skeptic batches | first-landing's fixed defects found; finder precision printed |
| confirmed duplicated seams | secondary | the finder's second lens, then skeptics | first-landing's count printed beside the arms |
| merge bar green at the end sha | secondary | `measure_bar` | the base bar recorded per repository |
| follow-on decision-met rate | secondary | probes over the follow-on trees | the follow-on's own controls |
| tokens, wall, owner turns, spend before READY | cost | transcript trees, driver clock, proxy rows | every session joins, 0 untagged grading agents |

### The reading, registered before any arm runs

Per task, `d` is the routed cell's held-out decision-met rate minus the raw cell's. `D` is the mean
of `d`. `derive_paired_p` returns the exact two-sided sign-flip p over every sign assignment of the
`d` values. `derive_verdict` keeps the aMendedFleet-73 thresholds:

- `ROUTED-BETTER` when `D` is at least 0.10 and p is at most 0.05.
- `RAW-BETTER` for the mirror case.
- `NO-DIFFERENCE` when the absolute `D` is below 0.10 and p exceeds 0.05.
- `INCONCLUSIVE` otherwise.

Each secondary measure is printed with its own paired p and never votes. When the orientation arm
runs, routed against orient and orient against raw take the same rule. Strata are printed as
exploratory and never yield a verdict word. The owner registers at Ask A the highest routed-to-raw
output-token ratio a ROUTED-BETTER reading may carry before it files a re-tier ask instead.

### What each outcome changes

The closing commit files these as asks in `memory/builds/aRoutedQuill/BACKLOG.md`. It changes no
gate, conf or charter line; an owner ruling does that.

| Reading | Ask filed |
|---|---|
| ROUTED-BETTER within the cost ceiling, orient short of routed by at least 0.10 | none; the record is what a later relaxation ask must answer |
| ROUTED-BETTER, orient within 0.10 of routed | relax the Tier-1 route to orientation and a brief, without a micro-spec |
| ROUTED-BETTER above the cost ceiling | re-tier: keep the route where the strata show it paying |
| NO-DIFFERENCE | relax the Tier-1 route, citing the cost ratio; Tier-2 untouched |
| RAW-BETTER | relax enforcement for Tier-1, at HIGH, owing an owner ruling |
| INCONCLUSIVE | a rerun at the task count the observed variance needs, which `aggregate` prints |
| a stratum signal | re-tier, marked exploratory, owing a confirmatory rerun |
| headroom stop or `DEAD PROBE` | an ask naming the dead instrument; no reading |

### Where the owner is asked

The trial runs in an attended session of its own. The asks need the owner, and the token join needs
a session no other work shares, so it never runs under the unattended driver. Every Workflow call
needs the owner's explicit opt-in at run time, so each one waits on its own ask:

- **Ask A**, before any agent runs: the task registry with every quoted prompt, the open §8 forks,
  the non-arm agents' model, the turn cap, the wall ceiling, the cost-ratio ceiling, the budget,
  and the opt-in for the `lists` Workflow call.
- **Ask B**, after the pilot sessions: the opt-in for the `pilot` Workflow call.
- **Ask C**, after the pilot guard passes: the main arms' budget, re-estimated from the pilot's
  measured spend per session, and the proxy's standing line on Workflow requests.
- **Ask D**, after every session and bar: the opt-in for the `grade` Workflow call, with spend so far.

No stage starts on an assumed yes. The report quotes each answer.

### Cost (estimate)

Every per-unit figure is UNVERIFIED for in-repo work and is re-derived from the pilot before Ask C.
The routed multiplier is DERIVED from the blinded trial's S arm without its audit: spec 37.0k plus
build 27.1k over B's 19.1k is 3.36 times
(`memory/builds/aBlindedTrial/build/2026-09-20-build-TOOL-aBlindedTrial-1-trial-report.md:190`).

| Item | Count, 12 tasks, two arms | Output tokens | Basis |
|---|---|---|---|
| raw builds | 12 | 0.6 to 1.8M | 50k to 150k a session, the B cell's 19.1k scaled for a real repository |
| routed builds | 12 | 2.0 to 6.0M | 3.36 times raw |
| follow-ons | up to 24 | 1.3 to 3.9M | half a build each |
| proxy answers | about 100 | 0.1 to 0.3M | one short call each |
| `lists` stage | about 8 agents | 0.4 to 0.8M | 50k to 100k an agent |
| pilot, sessions and `pilot` stage | 4 sessions, about 4 agents | 0.5 to 1.2M | as above |
| `grade` stage | about 45 agents | 1.4 to 3.6M | 30k to 80k an agent |
| total | | 6.3 to 17.6M | cache reads near 120 times output, the blinded trial's ratio |

The orientation arm adds 12 builds, 12 follow-ons and 12 bars. At an UNVERIFIED 1.5 times a raw
session, that is about a quarter more in total. Wall, at the hook's bound with each task's arms in
one wave: 1 to 2 hours for `lists`, 1 to 3 for the pilot, 5 to 20 for builds and follow-ons, 2 to
24 for 24 serial bars, and 2 to 6 for `grade`. That is 11 to 55 hours over one to three days for
two arms. The recommended budget is 20M output tokens and 72 hours for two arms, and 24M and 90
hours for three. The `tokens` verb reports spend at every stage boundary, and the trial stops at a
boundary once spend passes the budget.

### Inventory

New records under this build's `build/` folder, each named `<date>-build-TOOL-aRoutedQuill-6-<suffix>`
per hygiene check 5: `-6-tasks.tsv`, `-6-decisions.md`, `-6-proxy.md`, `-6-harness.py`,
`-6-trial.js`, `-6-freeze.tsv`, `-6-results.tsv` and `-6-trial-report.md`.

| Identifier | Kind | Cell |
|---|---|---|
| `cmd_tasks` `cmd_freeze` `cmd_cells` `cmd_run` `cmd_blind` `cmd_bar` `cmd_tokens` `cmd_aggregate` | harness verbs | `py.function`; each answered OK by `python3 tools/lexicon/lexicon.py --suggest <name> --as py.function` |
| `check_task_row` `build_frozen_clone` `check_no_future` `build_cells` `run_session` `render_proxy_answer` `render_blind_patch` `check_contamination` `measure_bar` `measure_session_tokens` | harness functions | `py.function`, each answered OK |
| `derive_paired_p` `derive_verdict` `check_controls` `read_decision_list` `check_selftest` | harness functions | `py.function`, each answered OK |
| `--pilot` | flag of the `aggregate` verb | none declared |
| `OUTCOMES` | the closed outcome set | none: `py.constant` is undeclared in `.lexicon.conf` |
| `[rq6:<tag>]` | prompt tag | none |

`boundedParallel` is inlined from `tools/workflows/tier2-review.js` and mints nothing.

### Files touched (estimate)

`memory/builds/aRoutedQuill/build/` · `memory/builds/aRoutedQuill/BACKLOG.md` · `memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-6.md`

### Rollout

- No kit file is touched, so no kit version is owed; the build's single bump per kit belongs to the
  units that touch kits.
- Order 6: the trial runs after `TOOL-aRoutedQuill-5` lands. The unit pass writes records only, under
  no `ROUTED_PATHS` entry, so the write gate does not engage on it. Its commits still carry the unit
  id in the subject shape `TOOL-aRoutedQuill-3` grades.
- The pass returns the stages to the main loop, because a sidechain holds no spawn tool and cannot
  start a session. The main loop runs them behind Asks A to D, commits the rows, and sets this spec
  CLOSED in the commit adding the report.
- Cells and blind trees under `%TEMP%/rq6` are deleted once the record lands. The rows stay.

### Alternatives rejected

- **Standalone briefs, as the blinded trial ran.** They exclude reuse of existing code, which is half
  of what the route's orientation exists to buy.
- **Workflow agents as arms.** A Workflow subagent runs under the orchestrator's settings and hooks,
  so the clone's gate never fires; and it cannot spawn the subagents the route itself uses.
- **More replicates instead of more tasks.** Pairing by task needs tasks; nine replicates per arm
  separated nothing.
- **A hidden suite as the primary measure.** It saturated on explicit briefs and on a vague one.
- **The unpaired permutation the aMendedFleet-73 harness ran.** Pairing by task removes the
  variance that dominates real work, at no extra build.
- **`tools/workflows/tier2-review.js` per arm diff.** It costs a full lens fan per diff; the lean
  finder and skeptic pair is the blinded trial's measured shape.
- **Gov's own history as the task source.** §8 F3: gov's product is the routing machinery itself.

## 5. Production-readiness checklist

- security — cells hold private adopter code under `%TEMP%`, and nothing leaves node a except through
  the model API, as in any session. Web tools are disallowed and the contamination audit reads every
  transcript. Prompts and decision rows are scrubbed of credentials before commit, and the owner
  approves the adopter text at Ask A.
- perf / scale — sessions and workflow agents stay within the hook's bound, bars run one per host,
  and the cost table above is re-derived from the pilot.
- error / empty / loading states — every session ends in a closed outcome and a dead one scores 0,
  named. A session limit kills workflow agents silently, so a stage resumes by its run id. An empty
  stratum refuses at `tasks`.
- observability — every figure is a row in `-6-results.tsv`. Each stage emits a heartbeat line, and
  `aggregate` prints its liveness lines beside the verdict.
- risks — judges and builders are one model family, so a shared blind spot passes both; the report
  states it. The landed truth may itself have been routed, which is why rows must be owner-backed.
  The proxy's leak is bounded per answer and recorded. One replicate per task means a noisy task is
  not detectable as noise.
- testing — `--selftest` holds the contamination audit, the paired test and the verdict rule; the
  controls and the pilot guard are the liveness checks; AC1 to AC13.
- migration — none: records only.
- user docs — the trial report is the deliverable; no help page.

## 6. Acceptance criteria

- **AC1** — When the harness's `tasks` verb runs over `tasks.tsv`, it prints each row's stratum and
  refuses a row whose landed commit does not descend from its base, whose size class disagrees with
  `git diff --name-only` over the repository's product paths, or whose prompt source does not
  resolve. It also refuses a stratum below its quota.
  Red when: a row with a mis-derived size class is admitted.
- **AC2** — When `freeze` runs, `freeze.tsv` carries the sha256 of every decision list, the registry
  and `proxy.md`, and `aggregate` refuses to grade against a list whose bytes moved. `freeze` refuses
  a row whose owner citation does not resolve in the source repository at its sha.
  Red when: an agent-resolved fork enters a list, or a list edited after the pilot is graded.
- **AC3** — When `freeze` builds a task's template, `git cat-file -e` on the landed sha fails inside
  it, and the clone holds one branch and no remote but its local bare.
  Red when: the landed commit, a later tag or a reflog entry is reachable from the clone.
- **AC4** — When `cells` makes a task's cells, `tools/check-wiring.sh` reports the gate wired and
  armed in the routed cell and unwired in the raw cell, and `git diff --stat` between the two cells
  names only the wiring files.
  Red when: the arms differ in anything but the wiring, or the raw cell is silently armed.
- **AC5** — When `run` closes a session, `results.tsv` carries its outcome from `OUTCOMES`, session
  id, driver-clock wall and owner turns. A `built` row adds the count of commits touching
  `ROUTED_PATHS`. A routed row adds whether a brief, a spec committed before code and a `## route`
  line exist.
  Red when: a cell with no product commit reads `built`, or an outcome is blank.
- **AC6** — When the proxy answers, its row names the decision it drew on or `none`, and
  `render_proxy_answer` refuses an answer drawing on two rows.
  Red when: one answer discloses two decisions, or two arms of one task get different instructions.
- **AC7** — When `blind` writes the code-named trees, `git grep` for every id an arm minted finds
  nothing under the blind root, no blind tree carries a file under the memory root, and the key file
  sits outside the blind root.
  Red when: a judge can read an arm-minted id, a spec or a brief.
- **AC8** — When the harness runs with `--selftest`, `check_contamination` marks a planted transcript
  reading the source repository's path as `contaminated` and passes one reading only its cell.
  `derive_paired_p` returns 2/4096 for twelve equal positive differences, and `derive_verdict`
  returns each of its four words on its registered case.
  Red when: the planted read passes, or a verdict case moves.
  figure: 2/4096 is DERIVED by the function under test, two extreme assignments out of 2^12.
- **AC9** — When the pilot has run, `aggregate --pilot` prints the raw cells' held-out decision-met
  rate, both controls, and whether each routed cell routed. The main arms start only when the rate
  is at most 0.8, the controls hold, and a routed cell routed.
  Red when: the arms fan out past a failed guard.
  permission: the pilot's sessions and its Workflow call wait on Asks A and B.
- **AC10** — When `aggregate` runs over the main arms' committed rows, it prints per task `d`, both
  controls and the first-landing finder control, then `D`, the exact sign-flip p, the verdict word,
  each secondary measure with its own p, and the cost ratios. A task failing a control is named and
  left out, and more than a quarter failing prints `DEAD PROBE`.
  Red when: a failed control is averaged into the reading.
  cost: §4's estimate, paid by the main loop after Asks C and D; the observation itself is seconds.
- **AC11** — When `tokens` runs, every session has output, cache-write and cache-read rows read
  through `resolve_session_tree`, and routed and orientation sessions carry spend before READY from
  `derive_ready_point`. Every grading agent joins a `[rq6:<tag>]` tag, with 0 untagged.
  Red when: a session has no token row, or a grading agent joins no tag.
- **AC12** — When `git log --format=%s` lists the unit's commits, the commit adding `harness.py`,
  `trial.js`, the lists and `freeze.tsv` precedes the first commit carrying a pilot row. The spec
  reads CLOSED only in the commit adding the report, which quotes the answers to Asks A to D.
  `aggregate` from a fresh `git clone --local` of that tip prints the report's tables byte-identical.
  Red when: results precede instruments, or a figure needs a file under `%TEMP%`.
- **AC13** — When the verdict is printed, the closing commit appends to this build's `BACKLOG.md`
  exactly the asks §4's outcome table names for it, and no commit of the unit touches a path under
  `ROUTED_PATHS` or `.memory-tree.conf`.
  Red when: the trial's own commits change enforcement.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `workflow script syntax` · `verifier fan-out` · `lexicon naming predicates` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: none · covers none · the instruments carry their own liveness: the controls, the pilot guard and `--selftest` (AC8 to AC10) · none

## 8. Open questions

- **F1 — Does an orientation-only arm run beside raw and routed?**
  Options: two arms, 24 builds and 24 follow-ons; or three arms, half as many again at about a
  quarter more total cost. Only the third arm can say whether the micro-spec and the gate add
  anything over orientation and a brief, which is the relax option §4's outcome table files.
  Recommendation: three arms.
  RESOLVED (owner, 2026-10-09): three arms.
- **F2 — How many tasks, at one replicate per arm?**
  Options: 8, two per stratum; 12, three per stratum; 16, four per stratum. Each task costs about a
  twelfth of the arms. Eight leaves each stratum's signal to two tasks. Sixteen adds a third to the
  bill, while twelve already resolve p far below the registered 0.05.
  Recommendation: 12, with a rerun at 16 only on an INCONCLUSIVE reading.
  RESOLVED (owner, 2026-10-09): 12 tasks at one replicate per arm, rerun at 16 only on an INCONCLUSIVE reading.
- **F3 — Which repositories supply the tasks?**
  Options: the two adopters only; the adopters plus gov tasks whose landed diff misses the routing
  machinery, with only that machinery overlaid at the landing tip; gov only. A gov clone at a
  historical base cannot carry the build's gate without carrying gov's own future, because gov's
  product is the kits. The overlay is a pairing that ships nowhere, the shape
  `memory/gotchas/ab-arm-never-did-the-work.md` warns against. Adopter prompts and decision rows land
  in gov's memory, and the owner approves that text at Ask A.
  Recommendation: the adopters only, falling back to the overlay only when they cannot fill a
  stratum.
  RESOLVED (owner, 2026-10-09): the adopters only, falling back to the overlay only when they cannot fill a stratum.
- **F4 — Who answers an arm's questions?**
  Options: the owner live; a proxy holding the decision list; nobody. The owner live is the real
  signal but leaves dozens of sessions waiting on a person. Nobody under-credits the brief
  confirmation the route is built around. The proxy's leak is one decision per answer, recorded per
  row.
  Recommendation: the proxy.
  RESOLVED (owner, 2026-10-09): the proxy.
- **F5 — How do the arms' headless sessions handle permissions?**
  Option (a): an explicit allowed-tools list and no bypass, closer to how owners run, with the pilot
  showing builds finish under it. Option (b): `--dangerously-skip-permissions`, inside the frozen
  clone only, as `tools/unattended/resume-tick.sh:358` launches a run; an arm can then run any
  command on the machine without asking. Whether a PreToolUse deny still fires under the bypass is
  UNVERIFIED, so the pilot must observe one before the main arms run; with none observed, the routed
  arm cannot be measured and the trial stops at Ask C.
  RESOLVED (owner, 2026-10-09): (b), bypass inside the frozen clones only.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §3 · §4 · cross-read fold: order 5 to 6, because `KICK-aRoutedQuill-1` moved
  from order 1 to 2, which shifts every later step by one.
- rev-3 · 2026-10-09 · §4 · §8 · owner resolves F1 to F4 as recommended, adds F5 resolved as
  bypass inside the frozen clones only, and runs every session and agent at High effort, never Extra.
- rev-4 · 2026-10-09 · §4 · the owner amends the arms to Opus 5.5 at Medium effort; the trial's
  other agents stay at High, never Extra, and Ask A registers only the non-arm agents' model.
- rev-5 · 2026-10-09 · §4 · the M2 cross-read of 2026-10-09 found §4 Rollout still said order 5
  where the status header, the rev-2 line and the build README say order 6; Rollout now reads order 6.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "run a blinded trial comparing build arms on frozen clones,
probe each tool against a hidden decision list, and join token usage to arms by tag"` returned only
name-stem neighbours, such as `run`, `probe`, `arm` and `frozen`, all test-suite helpers. Its scan
reported no unscanned layer, so no existing seam fits the harness itself. The seams extended are
these. The aMendedFleet-73 kit sits under `memory/` and outside the map, and it is adapted by copy.
`resolve_session_tree`, `read_records` and `derive_ready_point` in `tools/runlog/extract.py` give
the per-session token and READY figures. `boundedParallel` is inlined from
`tools/workflows/tier2-review.js`. The closed outcome set follows
`tools/workflows/orient-counterfactual.js`. Recall returned `TOOL-aBlindedTrial-1`,
`TOOL-aMendedFleet-73` and its report, `TOOL-aMendedFleet-109`, `PLAY-aMendedFleet-6`, and
`TOOL-aReplayedCard-9`'s parked orientation matrix, which measured cost and never code.

Recall terms used: `python tools/memory-recall/query.py "has a trial measured whether routing a build
through orientation, a brief and a spec improves code against building from the raw prompt" --terms
"blinded trial vague brief decision headroom pilot orientation counterfactual routed spec-first
permutation frozen clone"`
