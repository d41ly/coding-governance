# TOOL-dIndexedDesign-5 — the research harness: one experiment factory on dBoundRoles' `experiment` shape, the reuse bench its first entry

**Status:** DEFERRED · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 10 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0387@f264e3f3 whole
**Carries:** node:item.design.research

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-b.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-b.md) | research | TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

Research has no harness: the `research` workflow runs its researcher with `harness = "none"`
(`tools/roles/workflows.toml:81-87`), and a test that compares candidates has nowhere to run but by
hand (gap-design-07, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:355`).
The clause asks for "the research harness, built on dBoundRoles' `experiment` shape (night pass, point 2,
and WK-2)". This unit ships `experiment.js`, the one experiment factory, as the `research` workflow's
harness. It extracts the factory at its second instance, the charter's `[reuse]` rule, since
TOOL-dLinkedLibrary-2 S11's `reuse-bench.js` is the first, and it re-points that bench as the
factory's first entry. The night pass's shape is the acceptance: a corpus with controls, blinding,
variants on one schema, a bounded fan, a deterministic scorer or a blind judge, and reruns keyed by
variant and effort (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:151-155`).

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and DEFERRED at base: the
`experiment` kind, its `[workflow.experiment]` table and rule R9 (TOOL-dBoundRoles-16 S4, §4 "The
experiment"); the composed workflow rows `compose_workflows`, the overlay `.governance/instructions.toml`
and the open workflow registry that replaces `WORKFLOW_NAMES` (TOOL-dBoundRoles-20 S3, S4); the scorer
factory `replay_scorer.py`, its `INSTANCES`, `case_evidence` and `--experiment <manifest>`
(TOOL-dFairHearing-12 S1, TOOL-dFairHearing-14 S1, S2); `reuse-bench.js` and its committed manifest
(TOOL-dLinkedLibrary-2 S11); the `kind: research-return` line (TOOL-dLinkedLibrary-13 S1); and the
item factory `loop_items.py new` with `tools/loop/loop.toml` (TOOL-dDeclaredLoop-24 S6). Every one
of those builds is an ancestor of this one, dFairHearing through dDeclaredLoop.

- **S1** — The factory. `tools/workflows/experiment.template.js`, rendered to
  `tools/workflows/experiment.js` with the one token `{{FANOUT_CAP}}`: a `rendered` `[[files]]` row in
  `tools/workflows/kit.toml` beside `tier2-review.template.js`'s, and a pair in `PAIRS` of
  `tools/workflows/check-protocol-parity.test.sh:94-98`. Its fan-out is the inlined `boundedParallel`
  with its `// gov:bounded-fanout` marker, copied from `tools/workflows/tier2-review.template.js:16-23`
  as `tools/workflows/unattended-build.template.js:137` copies it, because a workflow script cannot
  import. It takes `mode`, either `research` or `experiment`, and writes nothing: it RETURNS the
  record text, the results and the manifest, and the main loop writes them. Observed by AC1 and AC3.
- **S2** — Research mode. One `gov-researcher` agent, label `<slug> · <unit> · researcher`, is handed
  `question` and, when given, `brief`. Its return is the role's `returns:` line verbatim
  (`tools/roles/agents/gov-researcher.agent.md:10`). The harness returns `record`: a first line
  `**Serves:** research <ids>`, a second line `kind: research-return`, then a blank line and the
  return. The main loop writes it as
  `memory/builds/<slug>/build/<date>-build-<unit id>-research[-<x>].md`. A return whose losing test is
  an experiment names that experiment's entry, which the caller runs next in experiment mode.
  Observed by AC1.
- **S3** — Experiment mode, the shape. It takes `table`, the line S5 prints, and `cases`, the line
  S6 prints. It refuses before any spawn:
  - a case carrying a key other than `id` and `input`, the defence behind S6's blinding;
  - a `fan` above `{{FANOUT_CAP}}`;
  - a `reruns` key whose variant is not listed.

  Each `<variant>.<level>` key of `reruns`, run its count `n` times, spawns one agent per case of
  the entry's `subject` stage role, at `effort: <level>`. Each prompt holds the variant's block, then
  the one `## Returns` block, then the case's `input`, so every variant answers on one schema. Each
  answer is parsed as a JSON object; one that does not parse is recorded as `null` and is never
  retried, so S5 of TOOL-dFairHearing-14 counts it unparsed. Concurrency is the smaller of `fan`
  and `{{FANOUT_CAP}}`. Observed by AC2 and AC3.
- **S4** — Scoring, exactly one of two. With `scorer`, the harness returns `results`,
  `{"<arm>": {"<case id>": <answer>}}`, and `manifest`, in TOOL-dFairHearing-14 §4's shape: its
  `instance` is the scorer, and its `arms` each carry `name`, `base`, `settings` and `dispatched`. The
  main loop commits both and runs `replay_scorer.py --experiment <manifest>`, the deterministic scorer
  that re-derives every figure. With `judge`, one judge agent per case, of the entry's `judge` stage
  role, reads every arm's answer for that case under a label rotated by the case's index, so no arm
  holds one label on every case (TOOL-dFairHearing-14 S6). The harness returns the label key
  `{<case>: {<label>: <arm>}}`, and the judge prompt never names an arm. The arm grammar and its
  bases are §4 "The arms". Observed by AC4 and AC5.
- **S5** — The table as args. `python tools/roles/handoff.py experiment-args <workflow>`, a verb
  beside `print_harness_args` (`tools/roles/handoff.py:452-470`) and read through
  `compose_workflows`, prints one JSON line: the entry's `[workflow.experiment]` table as R9 graded it,
  its `stages`, and the blocks of its variants file. The variants file sits beside the `cases` file,
  named `<cases stem>.variants.md`, and holds one `## <variant>` section per listed variant, a
  `## Returns` section and a `## Losing` section, which is the losing outcome stated before the run.
  The verb refuses, naming the cause: an entry whose `kind` is not `experiment`; a variants file
  that is absent, untracked or modified in the working tree; a missing or extra variant block; and a
  missing `## Returns` or `## Losing`. Observed by AC6.
- **S6** — The blind inputs. `python tools/workflows/replay_scorer.py --blind <instance> <cases src>`
  prints `[{"id": <id>, "input": <case_input(case)>}]`. `case_input(case)` is a new per-instance
  hook beside `case_evidence` (TOOL-dFairHearing-14 S2). It is an ALLOW-list: it names what an agent
  may see, and everything else is withheld. The `scouted-seam` instance hands every key of a case but
  `ground_truth` and `control`. The `review-replay` instance declares no hook, so `--blind` refuses
  it as not dispatchable. A case set with no case whose `control` key is `true` is refused, because
  the corpus must carry controls. That key is the one aScoutedSeam's cases already spell (blob
  `921345a50b49d8fb87687b3e411611d1d0b8e740`). `<cases src>` must be tracked and unmodified. Observed
  by AC7.
- **S7** — The entries.
  - The `research` entry (`tools/roles/workflows.toml:81-87`) becomes `driver = "workflow"`,
    `harness = "{prefix}/workflows/experiment.js"` and `stages = { researcher = "gov-researcher" }`.
    `render_agents.py --write` re-renders `.claude/roles.json`, whose `harnesses` list then holds
    `experiment.js`, the admission the agent-cap hook reads.
  - The reuse bench becomes the factory's first entry: a repository `[[workflow]]` row `reuse-bench`
    in `.governance/instructions.toml`, of kind `experiment`, with harness
    `{prefix}/workflows/experiment.js` and `stages = { subject = "gov-reuse-scout" }`. Its table is the
    one TOOL-dLinkedLibrary-2's committed bench manifest runs: one variant, `house-index`, with
    `scorer = "scouted-seam"`. Its held-out run is the same entry with the frozen held-out file handed
    to S6 as `<cases src>`. The manifest names that file under `heldOut`.
  - `tools/workflows/reuse-bench.js` is deleted with its `project-owned` row in
    `tools/workflows/kit.toml`, so no second dispatcher exists.

  **Readers:** by name: `tools/workflows/kit.toml`, whose `project-owned` row TOOL-dLinkedLibrary-2
  S11 adds; READER NOT IN TREE for `help/reuse.md`, TOOL-dLinkedLibrary-2 S12's page, which names the
  bench and is unbuilt at base · by value: NO VALUE READERS — a workflow script is run by its
  `scriptPath` and nothing compares, counts or derives from the file; `.claude/roles.json` never
  listed it. Observed by AC8.
- **S8** — The item `design.research`, node `item.design.research`. The item factory,
  `loop_items.py new design.research`, appends its `[[item]]` row to `tools/loop/loop.toml` with
  `--step step.design`, `--actor role:gov-researcher`, `--owner dIndexedDesign` and the witness "the
  research record's kind line and Serves binding". That witness is TOOL-dLinkedLibrary-13's
  `read_declared_kind` returning `research-return` on the record S2 shapes. This is the item that TOOL-dLinkedLibrary-13 S2 says
  writes the kind line, and that TOOL-dDeclaredLoop-11 maps the directives `researched` and
  `solution-tested` onto. Observed by AC9.
- **S9** — The docs: a new page `help/experiments.md` and its line in `help/README.md`. The page
  covers the two modes, the variants file, the three commands that turn an entry into a run, and
  what the factory refuses. `tools/workflows/README.md` names `experiment.js`. Observed by AC11.
- **S10** — The first live run. The main loop runs the `reuse-bench` entry through the factory at
  the close, and it reproduces TOOL-dLinkedLibrary-2's bar. Observed by AC10.

## 3. Non-goals (OUT)

- The `experiment` kind, its table and R9: TOOL-dBoundRoles-16's. This unit reads them and adds no
  table key, so `experiment-args` prints what R9 graded and never grades it again.
- The scorer's figures, the held-out freeze, the one-variable rule and the parsed counts: the
  `--experiment` rules of TOOL-dFairHearing-14. This unit adds one hook, `case_input`, and one verb,
  `--blind`, to that factory.
- The `bug-class-intent` instance, its corpus and its entry: TOOL-dIndexedDesign-14's, which runs on
  this factory.
- A recorder agent. The agents this factory spawns write nothing (`writes: none` on every role it
  spawns), and the main loop writes the returned text, so no role gains a write class.
- Recall's bench and union as an experiment entry (TOOL-dLinkedLibrary-30, an open ask of that
  build): a later entry of this factory, not built here.
- The `plan.research` item: dRankedPlan's.

### Edges

- **hands-off** `TOOL-dIndexedDesign-14` — `experiment.js`, the factory the `bug-class-intent` entry runs on, with `experiment-args` and `--blind` turning that entry into a run
- **consumes-from** external — dBoundRoles: the `[workflow.experiment]` table, R9, `compose_workflows` and the overlay rows (TOOL-dBoundRoles-16 S4, TOOL-dBoundRoles-20 S3, S4)
- **consumes-from** external — dFairHearing: `replay_scorer.py`, `INSTANCES`, `case_evidence` and `--experiment` (TOOL-dFairHearing-12 S1, TOOL-dFairHearing-14 S1, S2)
- **consumes-from** external — dLinkedLibrary: `reuse-bench.js` and its manifest (TOOL-dLinkedLibrary-2 S11), the `kind: research-return` line (TOOL-dLinkedLibrary-13 S1)
- **consumes-from** external — dDeclaredLoop: `loop_items.py new` and `tools/loop/loop.toml` (TOOL-dDeclaredLoop-24 S6)
- **hands-off** `TOOL-dIndexedDesign-31` — S6's `scouted-seam` input, which that unit makes a true allow-list, and AC7, which it supersedes (report id 37, BLOCKER)

## 4. Design

### Evidence

- `research` is `driver = "agent"` and `harness = "none"` at base (`tools/roles/workflows.toml:81-87`).
  `.claude/roles.json`'s `harnesses` lists three scripts, and the agent-cap hook admits a `Workflow`
  call only by a `scriptPath` that list names (`tools/hooks/agent-cap.js:27`).
- A workflow script has no filesystem, so every fact reaches it as an argument
  (`tools/workflows/unattended-build.template.js:31-35`). This is why S5 and S6 are commands the main
  loop runs, and why the factory returns text instead of writing files.
- `agent()` inside a loop body is refused unless it is the one marked bounded loop
  (`tools/hooks/agent-cap.js:1185-1190`). Both shipped harnesses fan out through the inlined
  `boundedParallel`.
- The stub runner `run_wf` in `tools/workflows/unattended-build.test.sh:157-215` evaluates a workflow
  script as its runtime does and records each spawn's label, type, effort and prompt. It already
  drives a second script, `unattended-unit.js`, through its third argument.
- `gov-researcher` and `gov-reuse-scout` both declare `writes: none`.
- aScoutedSeam's case blob `921345a5` opens with a `// **Serves:**` line and marks its controls
  `"control": true`.

### The arms

Each arm is named `<variant>@<level>#<k>`. `k` runs from 1 to the `reruns` count of
`<variant>.<level>`. Its `settings` are `{"variant", "effort", "rerun"}`, and `dispatched` is the
number of cases. Every arm differs from its base in exactly one key, which is TOOL-dFairHearing-14 S4's
rule:

| Arm | `base` | The key it varies |
|---|---|---|
| the first variant at its first level, rerun 1 | `null` | none, it is the root |
| the first variant at a later level, rerun 1 | the root | `effort` |
| another variant at a level, rerun 1 | the first variant at that level, rerun 1 | `variant` |
| any arm at rerun `k` above 1 | the same variant and level at rerun 1 | `rerun` |

A level a later variant lists and the first does not takes that variant's own first level as its
base and varies `effort`.

### The run, end to end

```
python tools/roles/handoff.py experiment-args <workflow>                          # S5 -> table, stages, blocks
python tools/workflows/replay_scorer.py --blind <instance> <cases src>            # S6 -> blind cases
Workflow { scriptPath: 'tools/workflows/experiment.js',
           args: { mode: 'experiment', repo, slug, unit, table, cases, roles } }   # S3, S4
# the main loop writes results.json and manifest.json under memory/builds/<slug>/build/, commits them, then:
python tools/workflows/replay_scorer.py --experiment <manifest>                   # TOOL-dFairHearing-14
```

`roles` is what `handoff.py harness-args experiment` prints. That is the union of the `stages`
tables of every entry whose harness is `experiment.js`: `researcher`, `subject` and, when an entry
has a judge, `judge`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `experiment.template.js`, `experiment.js` | workflow template and its render | none |
| `experiment-args`, `print_experiment_args` | `handoff.py` verb and function | `py.function` for the function, answered OK by `lexicon.py --suggest`; no verb cell is declared |
| `--blind`, `print_blind_cases` | `replay_scorer.py` flag and function | `py.function` for the function, answered OK by `lexicon.py --suggest` |
| `case_input` | an `INSTANCES` hook key, as `case_evidence` is; each instance's function behind it takes a lexicon verb, `derive_<instance>_input` | none for the key; `py.function` for each function |
| `researcher`, `subject`, `judge` | harness stage keys | none |
| `<cases stem>.variants.md`, `## Returns`, `## Losing` | the variants file and its sections | none |
| `reuse-bench` | repository workflow row | none |
| `design.research` | loop item, node `item.design.research` | none |
| `help/experiments.md` | help page | none |

### Migration

The `research` entry changes its driver and harness. A caller that spawned `gov-researcher` directly
still works, because the role and its `workflow` key do not move; only the agent-cap admission list
gains `experiment.js`. No record is rewritten. The scout and research records already in the tree
keep their names.

### Rollout

The factory, the verbs and the entries land live, in one pass. S10 runs at the close as the main
loop's Workflow call. The unit's ledger answers AC10 from the scored figures.

### Files touched (estimate)

- `tools/workflows/experiment.template.js` (new), `tools/workflows/experiment.js` (new, its render): S1 to S4
- `tools/workflows/kit.toml`, `tools/workflows/check-protocol-parity.test.sh`: S1, S7
- `tools/workflows/replay_scorer.py`: S6
- `tools/workflows/reuse-bench.js` (deleted): S7
- `tools/workflows/unattended-build.test.sh`: the arm §7 declares
- `tools/workflows/README.md`: S9
- `tools/roles/handoff.py`, `tools/roles/adopt-roles.test.sh`: S5
- `tools/roles/workflows.toml`, `.claude/roles.json` (render): S7
- `.governance/instructions.toml`: S7
- `tools/loop/loop.toml`: S8
- `help/experiments.md` (new), `help/README.md`: S9

### Alternatives rejected

- a recorder agent writing results — lost to the write-class probe `grep -h "^writes:" tools/roles/agents/*.agent.md`, where every role the factory spawns prints `none`; giving one a write class widens a write surface (M3 veto 3), and the main loop already writes records · `tools/roles/agents/gov-researcher.agent.md`
- a second harness, `research.js`, beside `experiment.js` — lost to the charter's `[reuse]` rule, read against S2: research mode is one spawn on the same runner, label and args, so a second file copies the factory at its third instance · `tools/workflows/tier2-review.template.js`
- each experiment's table in a record rather than a workflow row — lost to TOOL-dBoundRoles-16 §4, which homes the table on the entry and grades it with R9; a record copy would be a second home that R9 never reads · `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-16.md`
- a new `experiment.test.sh` suite and leg — lost to the stub runner probe: `run_wf` in `tools/workflows/unattended-build.test.sh:157-215` takes the script as its third argument, and a new leg trips the meta-gates the catalogue class `a-new-leg-trips-a-growing-set-of-meta-gates` names · `memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`

## 5. Production-readiness checklist

- security — no agent this factory spawns may write. The cases reach an agent only through S6's
  allow-list and S3's key refusal, so the truth and the control flag never enter a prompt. The judge
  sees labels and never arm names. Every input file must be tracked and unmodified, which is the
  pre-registration.
- perf / scale — the agent count is the cases times the sum of `reruns`, run `min(fan, cap)` at a time.
  The reuse bench is 42 cases at one rerun.
- error / empty / loading states — refusals before any spawn name their cause. A dead agent is a
  `null` answer counted unparsed and never retried. An entry of the wrong kind, a missing block or a
  set with no control exits nonzero.
- observability — every spawn carries the label `<slug> · <unit> · <stage>`. The manifest's
  `dispatched` and the scorer's `parsed` lines show what returned before any figure.
- risks — an agent with Bash can read beyond its prompt, so blinding binds what it is handed, not
  what it could find; the page and §4 say so. The judge path has no gov entry yet, so only the stub
  arm observes it.
- testing — stub runs of both modes, the args verb's refusals, the blind verb over the aScoutedSeam
  blob, and the live bench at the close.
- migration — the `research` entry's driver and harness; nothing else moves.
- user docs — `help/experiments.md`, S9.

## 6. Acceptance criteria

- **AC1** — When a `node -e` stub run evaluates `experiment.js` as the runtime does, with `mode`
  set to `research`, a `question` and the ids `TOOL-tFix-1`, it spawns exactly one agent typed `gov-researcher`,
  and the returned `record` opens with `**Serves:** research TOOL-tFix-1` then `kind: research-return`.
  Red when: the kind line is missing or a second researcher spawns.
- **AC2** — When the same `node -e` stub run uses `mode: 'experiment'` with three cases, one of
  them carrying a sentinel `truth` key, it refuses before any spawn and names that key. With the key
  removed, two variants and reruns `{"a.medium": 2, "b.medium": 1}`, it records nine prompts, and
  each prompt holds its variant's block and exactly one `## Returns` block.
  Red when: a prompt carries the sentinel, or the agent count is not cases times reruns.
- **AC3** — When the `node -e` stub run's table sets `fan: 2`, no stub `parallel` call receives more
  than two thunks, and with a `fan` above the rendered cap the run throws before any `agent` call,
  naming `fan`.
  Red when: a batch exceeds `fan` or an over-cap table spawns.
- **AC4** — When the AC2 run returns, `manifest` lists the arms `a@medium#1`, `a@medium#2` and
  `b@medium#1`, each `dispatched: 3`. The base of `a@medium#2` is `a@medium#1`, varying `rerun`. The
  base of `b@medium#1` is `a@medium#1`, varying `variant`. A stub answer that is not JSON reads
  `null` in `results`.
  Red when: an arm differs from its base in two keys, or a non-JSON answer is retried.
- **AC5** — When the `node -e` stub run's table names `judge` over two arms and three cases, it spawns
  three judge agents. No judge prompt contains an arm name. The returned label key gives neither arm
  the same label on every case.
  Red when: an arm name reaches a judge, or a label is fixed to one arm.
- **AC6** — When `python handoff.py experiment-args reuse-bench` runs in a fixture copy whose
  variants file lacks `## Losing`, it exits nonzero naming `## Losing`. It refuses the same way for an
  untracked variants file and for an entry of kind `single`. With the file complete and committed, it
  prints one JSON line holding the table, `stages` and the three blocks.
  Red when: an incomplete or uncommitted pre-registration prints args.
- **AC7** — When `python replay_scorer.py --blind scouted-seam <cases src>` runs over the blob
  `921345a50b49d8fb87687b3e411611d1d0b8e740`, no printed case holds `ground_truth` or `control`.
  `--blind review-replay` exits 2 as not dispatchable, and a planted case set with no `control` case
  exits 2 naming the rule.
  Red when: a withheld key prints, or a set without controls is accepted.
- **AC8** — When `grep -n "experiment.js" workflows.toml` runs in `tools/roles/`, it prints the
  `research` entry's harness. `python handoff.py experiment-args reuse-bench` prints `scouted-seam`.
  `python render_agents.py --check` passes with `.claude/roles.json` listing `experiment.js`, and
  `git ls-files "*reuse-bench.js"` prints nothing.
  Red when: research keeps `harness = "none"`, or the old dispatcher remains.
- **AC9** — When a `python -c` `tomllib` read of the loop kit's `loop.toml` lists its `[[item]]` rows, the
  row `design.research` carries `step.design`, the actor `role:gov-researcher` and the owner
  `dIndexedDesign`.
  Red when: the row is absent or names another actor.
- **AC10** — When the main loop runs the `reuse-bench` entry through `experiment.js` over the
  benchmark cases and then the held-out cases, and `python replay_scorer.py --experiment <manifest>`
  scores each committed run, the parsed lines print before the figures, and the figures read at least
  16 of 24 positives on the benchmark and at least 8 of 12 on the held-out cases.
  Red when: a figure falls below TOOL-dLinkedLibrary-2's bar, or a figure prints before its parsed line.
  cost: 42 agents, and the case trees' clones.
  permission: a Workflow run, the main loop's, at the close.
  fixture: the `incms` and `nicocares` clones under `%TEMP%`; machine-local, not in the tree.
  figure: 16 and 8 are PINNED by TOOL-dLinkedLibrary-2 §4; the solved counts are DERIVED by the scorer.
- **AC11** — When `grep -n "## Losing" experiments.md` runs in `help/`, it finds the variants-file
  section. `grep -n "experiments.md" README.md` in `help/` finds its line.
  Red when: the page is absent or omits the pre-registration.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `review-replay selftest` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC2 AC3 AC4 AC5 · `run_wf` pointed at `experiment.js` through its script argument, the failing case a planted `truth` key reaching a prompt, staged by dropping S3's key refusal · none
New arm: tools/roles/adopt-roles.test.sh · covers AC6 · a fixture copy whose variants file lacks `## Losing`, staged by dropping the section check · none
New arm: tools/workflows/replay_scorer.py · covers AC7 · `run_selftest`'s arms over a planted case set with no control and a `ground_truth` key, staged by widening `case_input` to every key · none

## 8. Open questions

- **F1 — How does the `research` workflow reach the factory, given the table lives on an entry?**
  Options: (a) `research` keeps `harness = "none"` and each experiment is its own entry; (b)
  `research`'s harness becomes `experiment.js`, which runs a researcher in research mode and any
  `experiment` entry in experiment mode; (c) the table moves into a research record that a second
  caller grades. (a) fails the clause and gap-design-07, because research stays harnessless. (c)
  gives the table a second home that R9 never reads. RESOLVED (agent, 2026-10-28, delegated): (b),
  rung 3, the most feature-rich survivor: it meets the clause and keeps TOOL-dBoundRoles-16's one
  table home. grants: PLAY-dClosedLoop-3 the `research` entry's `driver`, `harness` and `stages`.
  widens: none · relaxes: none
- **F2 — Who writes the results, the manifest and the research record?** Options: (a) a recorder
  agent of a role given a write class; (b) the factory returns the text and the main loop writes it.
  (a) widens a write surface beyond the unit's tier (M3 veto 3). RESOLVED (agent, 2026-10-28,
  delegated): (b), rung 3, the only survivor of veto 3. widens: none · relaxes: none
- **F3 — Where is a control marked, and who strips what an agent must not see?** Options: (a) each
  instance declares a deny-list of hidden keys; (b) each instance declares an allow-list,
  `case_input`, and a control is the `control` key aScoutedSeam's cases already spell; (c) the
  harness strips a fixed key set. (a) and (c) leak any key nobody listed. RESOLVED (agent,
  2026-10-28, delegated): (b), rung 3: deny by default (the charter's `[security]`), and the control
  key is the measured spelling. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 5, the night pass's point 2
  (:118-176) and its instruments' shape list (:719-724), TOOL-dBoundRoles-16 S4, TOOL-dFairHearing-12
  and -14, TOOL-dLinkedLibrary-2 S11 and -13 S1, I12 and scout B's row for this unit.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from edge of TOOL-dIndexedDesign-31,
  promoted by the round-1 spec audit of this build; nothing else moved.

## 10. Reuse audit

The seams extended are TOOL-dBoundRoles-16 S4's `[workflow.experiment]` table and R9;
TOOL-dFairHearing-14's `--experiment` manifest and `case_evidence`, which `case_input` sits beside;
`print_harness_args` (`tools/roles/handoff.py:452`), which `experiment-args` sits beside;
`boundedParallel` (`tools/workflows/tier2-review.template.js:18`); and the stub runner `run_wf`
(`tools/workflows/unattended-build.test.sh:157`). Each line was verified at base. `python
tools/codebase-map/reuse_lookup.py "dispatch agents over frozen cases and variants then score results
with a deterministic scorer"` ranked name stems (`frozen`, `score` in `tools/memory-recall/bench.py`,
`renderAgentLabel`). None of them dispatches over cases, so no existing seam fits the dispatcher
outside the specced parents, and S1 builds it as their factory. Scout B cited
`tools/roles/workflows.toml:80-87`; the entry spans :81-87 at base, :80 being the table header.
Scout B also proposed that a recorder write `results.json`; F2 refuses that on the write-class probe.

Recall terms used: `python tools/memory-recall/query.py "how does research get a harness that runs an experiment over frozen cases with variants and a scorer" --terms "research harness experiment shape variants frozen cases controls blinding scorer judge reruns fan-out factory"`
