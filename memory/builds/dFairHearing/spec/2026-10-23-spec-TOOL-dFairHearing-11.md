# TOOL-dFairHearing-11 — every agent the review harness spawns is typed from a declared stage, and an opted-in review step runs twin finder runs the synthesis merges

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 9 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0078@ed5e83ae whole
**Carries:** node:policy-key.review.twin

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

The review harness spawns one agent no stage declares and that carries no type: the resume probe
(gap-review-13). This unit gives every spawn a declared stage and an explicit agent type, refused
before any agent when one resolves to none, and observed red on a planted untyped spawn. It also
lands the twin merge the owner's `review.twin` key opts a review step into (RS-1): two finder runs of
one shape, verified together and merged into one report, with its check (gap-review-12).

## 2. Scope (IN)

- **S1** — The resume probe joins the stage table. `ROLE_KEYS` in
  `tools/workflows/tier2-review.template.js` gains `probe`, so `roles.probe` and `efforts.probe` are
  read under the refusals both objects already carry. The probe's `agent()` call takes
  `renderStageOpts(probeType, 'probe')`, where `probeType` is `roles.probe`, else `Plan`, and one log
  line names it and its source, as the other three stages' lines do. Observed by AC1 and AC2.
- **S2** — Every stage resolves an explicit `agentType`. A new constant `PLATFORM_TYPE`,
  `general-purpose`, is the type a stage takes where it took no type before: the synthesis with no
  `roles.synthesis`, and every judge stage under `workerType: 'none'` that no role names. `durable`
  becomes true exactly when both judge stages resolve to `PLATFORM_TYPE`, which is the case it covered
  before. `workerType` joins the review key's print by the argument as given, so no key moves.
  Observed by AC2 and AC3.
- **S3** — Two refusals of an untyped spawn. Before the probe, the harness refuses by name a stage
  whose resolved type is empty. A new arm of `tools/workflows/tier2-review.test.sh` reads the
  template's code and refuses an `agent(` call whose options are not one of the four stage option
  constants `probeOpts`, `findOpts`, `verifyOpts` and `synthOpts`. Observed by AC4.
- **S4** — The `review.twin` stand-in. The harness takes a `twin` argument, a closed set `never`,
  `design-records`, `design-and-landing` and `always`, default `never`, refused outside it in the
  shape `intensity` takes. It is the policy key `review.twin` with v2's values and default, passed
  directly as a pin argument through `review.pin` until dDeclaredLoop's `review.trigger` lands:
  `tools/workflows/review_pin.py`, TOOL-dFairHearing-3's stand-in, takes `--twin <value>` and prints
  it as the `twin` argument in its JSON line, checking its shape only. Observed by AC5.
- **S5** — Which runs twin. A design-record audit is a spec audit whose subjects are all design
  subjects, paths holding no `builds/<slug>/spec/` segment by the harness's own `SPEC_SUBJECT_PATH`
  class (:317), or whose `preset` is not `unit-spec`. `twinned` is true under `always`; under
  `design-records` on a design-record audit; and under `design-and-landing` on that case or on any
  diff review. Observed by AC6.
- **S6** — A twinned run dispatches a second finder run, run b, over the same `LENSES` literal after
  run a, as a second `boundedParallel` call. Run b's labels end `:b` and its lens files are
  `find-<lens>-b.json`. Ids number run a's findings first, then run b's, so each run is one contiguous
  range. The verify stage runs over the union at its fixed batch count, and every count, `agents` and
  the review-shape line cover both runs. Observed by AC7.
- **S7** — The twin merge and its check. Each confirmed finding reaches the synthesis carrying
  `run=a` or `run=b`, under a TWIN RUN block that lists the cross-run candidate pairs grouped by
  `deriveAddressKey` (TOOL-dFairHearing-4) and asks for one item per defect, its ids from either run
  or both. The harness renders a `review-twin` record line, `review-twin runs=2 a=<first>-<last>
  b=<first>-<last>`, which the synthesis copies verbatim beside the review-shape line. The return
  carries `twin`: run a's and run b's confirmed ids, `agreed` (items holding a confirmed id of each
  run), `onlyA` and `onlyB`, derived from the items, and `null` when the tally refuses the item list.
  An untwinned run's return carries `twin: null`. Observed by AC8 and AC9.
- **S8** — The review key. A twinned run's input print gains `twin: true`, so it never reuses an
  untwinned run's lens or verify files, and an untwinned run's key is unchanged. Observed by AC10.
- **S9** — The kit's own records. `tools/workflows/README.md` states the probe's stage and type, the
  synthesis's default type, and the `twin` argument with its four values. The rendered
  `tools/workflows/tier2-review.js` is re-rendered from the template. The template's `version:`
  moves once against its value at base `3708a705` if no earlier unit of this build moved it.
  Observed by AC11 and AC12.

## 3. Non-goals (OUT)

- A `probe` stage in `tools/roles/workflows.toml`. No catalogue role fits a reader that judges
  nothing, and the shapes' declared stages are dBoundRoles' (systems `[design-role-shapes]`).
- A new item or record kind for the twin merge. The merge runs inside the report step, the item
  `review.report` TOOL-dFairHearing-8 owns, and its record is the review record, the kind
  TOOL-dFairHearing-17 owns (section 8 F4).
- Twins in the build harness, the unit harness or the drift-audit harnesses.
- A policy file read of `review.twin`. The key reaches the harness as a pin argument until
  dDeclaredLoop's `review.trigger` lands.
- Gating a shape change on the noise between twins, which is the Loop Review's (dCalibratedLens).
- The same-address pairs of one run handed to the synthesis to flag a refuted twin, which are
  TOOL-dFairHearing-7's. A twin run here is a second finder run, never a same-address pair.
- A `REVIEW_SHAPE` bump. No lens or skeptic prompt of an untwinned run changes, and a twinned run's
  key moves by S8.
- The address key itself. S7 groups its pairs by TOOL-dFairHearing-4's `deriveAddressKey`, ordered
  before this unit; that unit declares no edge to this one at this writing, so none is declared here.

### Edges

- **consumes-from** `TOOL-dFairHearing-2` — the `preset` argument S5 reads beside the subjects' class; without it only an all-design-subject audit counts as a design-record audit
- **consumes-from** `TOOL-dFairHearing-3` — `review_pin.py`, the `review.pin` stand-in this unit extends with the `review.twin` pin argument; without it the key reaches the harness only from a hand-written call
- **hands-off** `TOOL-dFairHearing-8` — the typed resume probe in its declared stage, which that unit extends with the leg-manifest read
- **hands-off** `TOOL-dFairHearing-15` — the stage table every spawn takes its type from, which that unit's checklist agent joins as the resume probe did
- **hands-off** `TOOL-dFairHearing-10` — the synthesizer role's input line names a twinned run's two finder runs
- **hands-off** external — dDeclaredLoop's review trigger replaces the direct pin argument, and dBoundRoles' declared shapes name the twin kind and the probe's stage

## 4. Design

### Evidence

- The probe's `agent()` call passes `label`, `phase` and `schema` and no stage options
  (`tools/workflows/tier2-review.template.js:1026-1028`). The comments at :218-221 and :233-235 say
  the probe never takes a type, and `tools/workflows/README.md:355` and :418 say so to a caller.
- `ROLE_KEYS` holds four keys (:236), and `renderStageOpts` (:270-272) omits `agentType` for an empty
  type. `synthType` is `roles.synthesis` or empty (:252), and `workerType` reads `none` as empty
  (:227), so the synthesis and a `none` run's judges spawn untyped today.
- Measured 2026-10-23 over the workflow agent metadata under this node's Claude projects directory:
  every untyped workflow agent records `agentType` `workflow-subagent` (1873 agents), the probe among
  them (`resume:probe`, phase `Resume`), and 191 workflow agents ran as `Plan`. The installed binary
  defines `workflow-subagent` as a built-in type with every tool. No workflow agent has run as
  `general-purpose`; it is the Agent tool's own default, recorded 281 times on direct spawns
  (section 8 F2).
- `durable` is `!findType && !verifyType` (:281), so a judge stage's emptiness is what marks a run
  durable today.
- Every finder fan is `boundedParallel(LENSES.map(...))` over the marked literal (:842, :1173), and
  each lens call is inline in the map body, which is what the verifier fan-out check reads.
- Every diff review this repository runs is the closing review over the cumulative diff (BUILD-METHOD
  M8; `tools/roles/workflows.toml` entry `closing-review`), so a diff review is a landing review
  (section 8 F5).

### The stage table

| Stage key | Spawns | Type when no role names it |
|---|---|---|
| `probe` | the resume probe | `Plan` |
| `diffFinder` or `specFinder` | every finder, run a and run b | `workerType`'s type, `Plan` when absent, `PLATFORM_TYPE` under `none` |
| `skeptic` | every skeptic batch | as the finders |
| `synthesis` | the synthesis | `PLATFORM_TYPE` |

A role key wins for its own stage, as today. `probeOpts` joins `findOpts`, `verifyOpts` and
`synthOpts` (:273-275), each built by `renderStageOpts`. The type refusal runs after the four types
resolve and before `phase('Resume')`, naming the stage key. The probe takes no part in `durable` or
the key: it writes no keyed file.

### The twin run

Run b is a second awaited `boundedParallel(LENSES.map(...))` statement after run a's, never a loop,
so each fan stays a call over the bounded literal. The per-lens prompt and options are built by one
function both maps call, and each map keeps its `agent(` call inline. Run b reuses a lens file only
under the run's own key and its own `-b` file name. A skipped lens is skipped in both runs. A
dead-lens deferral names run b's dead lenses by their `:b` labels in `pending`.

The synthesis block is headed TWIN RUN, a phrase distinct from TOOL-dFairHearing-7's same-address
twins. It is handed only on a twinned run, so an untwinned synthesis prompt is byte-identical. The
existing tally (:1947-1992) already refuses a confirmed id placed in no item or in two, over both
runs, because ids are global. The twin figures are derived after it and only over an item list it
accepted, so an unplaced id nulls `twin` rather than skewing `agreed`. `twin.agreed`, `onlyA` and
`onlyB` count items, and the record carries no figure the harness did not render: a reader derives
agreement from the `review-twin` line's ranges and the report's items.

### Data model

- Argument `twin`: one of the four `review.twin` values, absent reading `never`.
- Return `twin`: `null`, or `{ a: [<confirmed id>...], b: [...], agreed: <n>, onlyA: <n>, onlyB: <n> }`.
- Record line: `review-twin runs=2 a=<first id>-<last id> b=<first id>-<last id>`; a run with no
  finding renders its range as `-`.

### Inventory

Names this unit mints: the stage key `probe`, the constant `PLATFORM_TYPE`, the argument `twin`, the
derived flag `twinned`, the record line head `review-twin`, the return field `twin`, the option
constant `probeOpts`, and the `:b` label and `-b` file suffixes. No naming cell grades them. The
one function both finder maps call to build a lens's prompt and options is named by the builder in
the `js.function` cell `tools/lexicon/lexicon.py` grades, from its declared verbs.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js` (the render of the template, by
  `check-protocol-parity.test.sh --render`)
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/review_pin.py` (TOOL-dFairHearing-3's stand-in, the `--twin` argument only)
- `tools/workflows/README.md`

### Rollout

`twin` defaults to `never`, so no review twins until a caller passes the key. The type change is
live: a `none` run's judges and every synthesis spawn as `general-purpose` instead of
`workflow-subagent`. Reverting S2 is one constant read in two places.

### Alternatives rejected

- **Leaving the platform-default stages without an `agentType`.** It keeps the clause's "every agent
  typed" false for the synthesis and for a `none` run's judges (section 8 F2).
- **The probe under `workerType`.** Under `none` it would be untyped again, and the probe needs no
  Write tool (section 8 F3).
- **Twin finders as one ten-lens fan.** The verifier fan-out check sizes a lens literal at five slots,
  so a ten-element receiver is refused at the merge bar.
- **Each twin run as a separate harness run merged by the caller.** The merge would then have no
  harness check, which is gap-review-12's defect.

## 5. Production-readiness checklist

- security — no new write path: the synthesis and a `none` run's judges already held every tool as
  `workflow-subagent`, and `general-purpose` holds the same Write tool; the probe narrows to `Plan`,
  which holds no Write tool.
- perf / scale — a twinned run doubles the finder agents, from five to ten at the same concurrency
  bound, and adds no skeptic batch; an untwinned run is unchanged.
- error / empty / loading states — a stage typed empty refuses before any agent; a twin run with no
  finding renders `-` for its range; a dead run-b lens defers by its `:b` label.
- observability — one log line per stage names its type and source, the probe's included; a twinned
  run logs its two ranges and `twin`'s figures.
- risks — `general-purpose` has no workflow measurement here: a run where it misbehaves shows as dead
  agents in the deferral path, and S2's rollout line says how to revert. The second risk is a prompt
  echo: the synthesis must copy the `review-twin` line, and the return's `twin` is the source a caller
  compares against.
- testing — AC1 to AC12 as stub-agent probes and greps; the new suite arms under section 7.
- migration — none: an absent `twin` and an absent `roles.probe` keep today's behaviour but the types
  S2 names.
- user docs — `tools/workflows/README.md`; no page under `help/` names the probe or a twin, and
  `help/roles.md` describes harness labels, which keep their shape.

## 6. Acceptance criteria

The probe for AC1 to AC10 is `$SCRATCH/t2-stub.js`, written by the pass under its scratch
directory: it evaluates its first argument as an AsyncFunction with stub `agent`, `parallel`, `phase`
and `log` globals and its second argument as `args`, the shape `tools/workflows/tier2-review.test.sh`
uses, records each agent call's label and options, and answers each from a canned table.

- **AC1** — When `node "$SCRATCH/t2-stub.js" tools/workflows/tier2-review.js '{"repo":"/r","base":"aaaaaaa","roles":{"probe":"gov-orienter"}}'`
  runs, the call labelled `resume:probe` carries `agentType` `gov-orienter`, and with `roles` absent
  it carries `Plan`; with `{"roles":{"probe":"none"}}` the harness throws naming `roles`.
  Red when: the probe's options omit `agentType`, or `probe` is not a legal `roles` key.
- **AC2** — When the same probe runs with `{"workerType":"none"}`, every finder, skeptic batch and the
  synthesis carries `agentType` `general-purpose` and the probe carries `Plan`; with no `workerType`
  and no `roles`, the judges carry `Plan` and the synthesis carries `general-purpose`.
  Red when: any recorded call lacks `agentType`.
- **AC3** — When the probe runs with `{"workerType":"none"}`, the return's `durable` is `true` and each
  finder prompt carries the DURABILITY instruction; with `{"workerType":"Plan"}` it is `false`; and the
  return's `key` under `none` equals the key the render at the pass's starting commit computes for
  the same args.
  Red when: `durable` follows the new explicit type instead of the judge stages' resolution, or the
  key moves.
  fixture: the starting render, read with `git show 'HEAD:tools/workflows/tier2-review.js'` before the
  pass commits.
- **AC4** — When the pass copies the template to `$SCRATCH/planted.js` with the probe's `probeOpts`
  removed from its options and runs the new code-reading arm's predicate over it with
  `node "$SCRATCH/stage-arm.js" "$SCRATCH/planted.js"`, it names the probe's `agent(` call and exits 1;
  over `tools/workflows/tier2-review.template.js` it exits 0. A stub run whose stage table is edited to
  resolve `synthesis` to an empty string throws naming `synthesis` before the probe is called.
  Red when: the planted untyped spawn passes either check.
- **AC5** — When the probe runs with `{"twin":"sometimes"}` it throws naming `twin` and its four
  values; with each of `never`, `design-records`, `design-and-landing` and `always` it starts; and
  `python 'tools/workflows/review_pin.py' --twin always` prints a JSON line whose `twin` is `always`.
  Red when: an unknown value is defaulted instead of refused, or the stand-in drops the argument.
- **AC6** — When the probe runs a diff review, a spec audit of spec subjects under `builds/x/spec/`
  with `preset` absent and with `design-audit`, and a spec audit of design subjects outside any spec
  folder, under each `twin` value, the run dispatches ten finders exactly in the cases S5 names:
  `always` everywhere; `design-records` on the design-subject audit and the `design-audit` audit;
  `design-and-landing` on those two and the diff review.
  Red when: a spec-subject audit at `unit-spec` twins under `design-records`, or a diff review twins
  under it.
  figure: ten is derived, twice the `LENSES` literal's five slots at the template read.
- **AC7** — When a twinned stub run returns two findings from each lens of run a and one from each of
  run b, the ids run 1 to 10 on run a and 11 to 15 on run b, run b's labels end `:b`, the verify stage
  dispatches the same batch count an untwinned fifteen-finding run does, and the return's `agents` and
  `raw` count both runs.
  Red when: run b's ids interleave run a's, or the batch count grows with the second run.
- **AC8** — When that run's synthesis stub places ids 3 and 12 in one item and every other confirmed
  id alone, the return's `twin` reads `agreed` 1, and its `a` and `b` arrays list the confirmed ids of
  each run; the synthesis prompt carries the TWIN RUN block and the line
  `review-twin runs=2 a=1-10 b=11-15` between marker lines, and an untwinned run's synthesis prompt
  carries neither.
  Red when: the figures are read from the prompt instead of the items, or the line is absent.
- **AC9** — When the synthesis stub leaves a run-b confirmed id in no item, the return's `blockers`
  and `twin` are both `null` and the note names the id.
  Red when: `twin` is computed over an item list the tally refused.
- **AC10** — When the probe runs the same args twice, once with `twin` absent and once with
  `{"twin":"always"}` on a diff review, the two `key` values differ, and the first equals the key with
  `{"twin":"never"}`.
  Red when: a twinned run can reuse an untwinned run's lens files.
- **AC11** — When `grep -n "never takes one\|never take the type" tools/workflows/README.md` runs, it
  prints nothing, and `grep -n "review.twin" tools/workflows/README.md` prints the argument's section.
  Red when: the README still tells a caller the probe takes no type.
- **AC12** — When `grep -c "PLATFORM_TYPE" tools/workflows/tier2-review.js` and the same grep over
  `tools/workflows/tier2-review.template.js` run after the pass's re-render, they print one count, and
  `grep -m1 "version: " tools/workflows/tier2-review.template.js` prints a version other than
  `git show '3708a705:tools/workflows/tier2-review.template.js' | grep -m1 "version: "` does.
  Red when: the render was not refreshed, or the kit's version never moved over the build.
  figure: the base version, `1.53`, is pinned, read from the template at base `3708a705` on 2026-10-23.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 · a copy of the template with the probe's stage options removed, and stub runs over each twin case · FLOOR_ASSERTIONS raised by the arms added, from its value at dispatch

## 8. Open questions

- **F1 — One unit for the typed stages and the twin merge, or two?** BUILD-METHOD M2 asks one
  mechanism per spec, and the clause carries both. (a) One unit, as the roster has it: both are the
  stage table of the panel's spawns, since run b is a second spawn of a declared stage, and one diff
  lets a reviewer place a finding by its S item. (b) Split the twin into a new unit carrying the clause
  `part 2/2`, a departure adding a roster unit. (b) adds a unit, a departure record and a second pass
  over the same file for no behaviour (a) lacks. Recommendation (a). Rung 3. RESOLVED (agent,
  2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — What type does a stage take where it took none?** (a) `general-purpose`, the Agent tool's
  default, explicit on the synthesis and on a `none` run's judges. (b) No `agentType` there, the stage
  only declared, the platform recording `workflow-subagent`. (c) Every stage's role made mandatory.
  (b) leaves the clause's "every agent typed" false for two stages, and (c) refuses every caller that
  passes no `roles`, an acceptance loss for every existing call. (a) has no workflow measurement here
  (section 4 Evidence), which is a risk, not a veto: it adds no tool the platform default lacked.
  Recommendation (a), with the rollout line in section 4. Rung 3. RESOLVED (agent, 2026-10-23,
  delegated): (a). widens: none · relaxes: none
- **F3 — The probe's default type: `Plan`, or the judges' resolved type?** The judges' type is
  `general-purpose` under `none`, so the probe would gain a Write tool it never uses; `Plan` is
  measured in 191 workflow agents and the finders already run git under it. Recommendation `Plan`.
  Rung 3. RESOLVED (agent, 2026-10-23, delegated): `Plan`, a `roles.probe` key overriding it.
  widens: none · relaxes: none
- **F4 — Does the twin merge mint an item and a record kind?** Gap-review-12 says twin merges have
  none. (a) New nodes for a twin-merge item and record kind. (b) The merge runs in the report step,
  `review.report`, whose node TOOL-dFairHearing-8 owns, and its record is the review record, whose kind
  TOOL-dFairHearing-17 owns, marked by the `review-twin` line; the check is the tally over both runs
  plus this unit's arms. (a) mints nodes outside the packet's ten owned nodes, a departure the systems
  record's owner table does not ask for (it gives dFairHearing "the panel's internals and the twin
  merge"). Recommendation (b). Rung 1. RESOLVED (agent, 2026-10-23, delegated): (b). widens: none ·
  relaxes: none
- **FACT-QUESTION · F5 — Is every diff review a landing review, for `design-and-landing`?** Probe:
  read BUILD-METHOD M8 and every tracked caller of the harness for a diff review that is not the
  closing review (`git grep -n "tier2-review" -- '*.js' '*.sh' '*.py' '*.toml'`). Observation: M8
  names one adversarial review over the cumulative diff and says per-pass reviews do not substitute;
  `tools/roles/workflows.toml` names the diff review only in `closing-review`, and the build harness
  calls the harness as a spec audit only. Liveness: a tracked caller passing the diff kind outside the
  closing review would have refuted it, and the grep could print one. RESOLVED (agent, 2026-10-23,
  delegated): every diff review twins under `design-and-landing`. widens: none · relaxes: none

- **F6 — Does the grant cover the harness and stand-in edits?** Every path under `tools/` is a
  governance carrier by `PLAY-dClosedLoop-10`'s list (its routed product paths), and the clause names
  the panel's internals and the twin merge `review.twin` opts a review step into. RESOLVED (agent,
  2026-10-23, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the
  review harness's stage table, its twin run and the twin pin argument of the review.pin stand-in ·
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.

## 10. Reuse audit

The seam is TOOL-aOrientedCast-5's stage table in `tools/workflows/tier2-review.template.js`:
`ROLE_KEYS` (:236), the two refusals over `roles` and `efforts` (:238-269), and `renderStageOpts`
(:270-272). The probe joins it as a fifth key and the type defaults extend its resolution, so no
second spawn-option builder exists. The twin merge extends the existing tally (:1947-1992) and the
marker-line copy the review-shape line uses (:1902-1903). `python tools/codebase-map/reuse_lookup.py
"type every agent a review harness spawns and declare its stage"` ranked `renderAgentLabel` and
`resolve_stage_efforts` among name-stem hits and did not rank `renderStageOpts` or `ROLE_KEYS`, which
the template read found; no hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how does the review harness type the agents
it spawns and merge two twin review runs" --terms "resume probe agentType roles stage workerType
synthesis twin merge review.twin RS-1 panel untyped"`
