# TOOL-dBoundRoles-90 — a harness stage whose effect may already have landed is spawned once

**Status:** INPROGRESS · rev-1 · 2026-11-24 · node a · Tier-2 · base f3ec096a8 · streams tooling · order 44

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 |
| [2026-11-24-prompt-TOOL-dBoundRoles-90-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-90-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-90-spec-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-90-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The harnesses spawn a stage again when its agent returns nothing, and they do it to stages that write:
the round record, the spec commit, the disposal and the builder. An agent that wrote and then died has
its write repeated. This unit spawns those stages once, so a null stops where the harness already stops,
and keeps the re-run for the stages that read.

## 2. Scope (IN)

- **S1** — The build harness. In `tools/workflows/unattended-build.template.js` the spec commit, the
  round record (`writeRound`) and the disposal call `agent(prompt, opts)` directly, prompt and options
  unchanged. The subject resolver alone stays in `runWithRetries`. The comments over `retries` and over
  the helper say so, and the `retries` log line names the subject resolver as the stage re-run. Observed
  by AC1, AC2, AC3 and AC4.
- **S2** — The render. `tools/workflows/unattended-build.js` is the template rendered by its renderer,
  never edited by hand. Observed by AC1 and AC7.
- **S3** — The unit harness. `tools/workflows/unattended-unit.js` spawns its builder by one `agent()`
  call outside any loop. `ATTEMPTS`, the read, refusal and log of its `retries`, its `retries` args
  paragraph and the second exception of its shape paragraph go. The build harness leaves `retries` out
  of `dispatch.args` and still forwards it to the audit's review call. Observed by AC5 and AC6.
  **Readers:** by name: `retries`, handed to the unit harness by `dispatch.args` of
  `tools/workflows/unattended-build.template.js`, the verbs guide, the build Skill and
  `help/roles.md`, each moved by S3 or S7; by value: NO VALUE READERS, since the loop that goes with it
  was the one reader of the count.
- **S4** — The review harness is unchanged. Its wrapped stages stay wrapped: the checklist agent and the
  resume probe run `git ls-files`, `git rev-parse`, `git hash-object` and file reads, and the synthesis
  writes one report file, which its return names. A repeated synthesis writes a report, appends no row,
  draws no round and commits nothing. Observed by AC4.
- **S5** — The static check, in `tools/workflows/unattended-build.test.sh`. For each
  `await runWithRetries(` call of the two templates it takes the text up to the call's
  `renderAgentLabel(` and the stage that label closes on. It reds where that text names the driver
  (`DRIVER`), the commit block (`commitBlock`), a git write (`git add`, `git commit`, `git push`,
  `git merge`) or a `--write` flag, and where the stages found differ from the declared set: `subjects`
  in the build template; `resume:checklist`, `resume:probe` and `synth` in the review template. It reds
  where the unit harness holds a `runWithRetries` or a `gov:sequential-agents` loop. Observed by AC4.
- **S6** — The arms. The stub runtime of that suite takes one more value in a `__seq` list, an object
  whose one key `__wroteThenNull` names a row: the spawn traces `wrote:<row>` and returns null. This
  unit's rows stand where the builder's DBR5 AC6 rows and the child's DBR5 AC7 rows stood; the parent's
  and the review call's stay. Observed by AC1, AC2, AC3 and AC5.
- **S7** — The texts. `tools/workflows/README.md`'s entry "The harnesses' retries" says which stages are
  re-run and which are spawned once, and why. The verbs guide (`tools/unattended/VERBS.template.md` and
  its rendered copy), the build Skill (`tools/roles/SKILL.template.md` and its rendered copy) and
  `help/roles.md` pass `retries` to the build and the review harness only. Observed by AC8.
- **S8** — The departure. A deviation record of this unit under `memory/builds/dBoundRoles/build/` names
  `TOOL-dBoundRoles-5@rev-6` S6, S7, AC6 and AC7 and deviation 53's list of wrapped stages as what it
  departs from. The CLOSED spec and that record are not edited. Observed by AC9.

## 3. Non-goals (OUT)

- A read-back before a re-run. The report names it as the alternative; §8 F1 takes the single spawn.
- The text of the existing stops. `the round was not recorded` is thrown on a null that may follow a
  written row; whoever re-invokes reads the run state first, as today.
- A stage inside a fan, which was never re-run (`TOOL-dBoundRoles-5` §3).
- An upper bound in the catalogue on `roles.retries`, and the handed-text fences of the unit harness:
  other items of the report.
- The `SubagentStop` send-back of `handoff.py check-return`, which reads `roles.retries` on the direct
  route and re-runs nothing.

This unit amends what `TOOL-dBoundRoles-5` S6 landed. It edits `tools/workflows/unattended-unit.js`, as the
batched minors unit `TOOL-dBoundRoles-92` may; the order verbs decide which goes first.

### Edges

- **consumes-from** external — the driver's `--review` verb, which appends a row on a repeat of a subject with no terminal row; this unit changes no driver verb

## 4. Design

### Evidence

Read and probed at HEAD `c31769972`, whose `tools/` and `help/` trees equal base `f3ec096a8`'s:

- `runWithRetries` (`tools/workflows/unattended-build.template.js@6ccb1997:650`) awaits `agent(prompt, opts)`
  again while it answers null or undefined, up to `retries` times. Its call sites are the spec commit
  (`@6ccb1997:1382`), the subject resolver (`@6ccb1997:1617`), the round record (`@6ccb1997:2110`) and the
  disposal (`@6ccb1997:2650`). The builder's loop is `tools/workflows/unattended-unit.js@ee9e2dbb:525`.
- The defect holds. The suite's `run_wf` body was run by `node` from scratch over the shipped files with
  `retries` 2 and each stage answering null and then a good object. The record, the commit, the disposal
  and the builder each spawned twice and the run went on from the second return. The resolver did too,
  harmlessly: its prompt runs `git rev-parse`, `git hash-object`, `git show` and the checklist's
  `--for-paths` read.
- The stops a null already meets: the commit throws `the spec commit stage returned nothing`
  (`@6ccb1997:1445`), the record throws `the round was not recorded` inside `writeRound`, the disposal
  returns an empty roster whose note reads `the disposal stage returned nothing at all` (`@6ccb1997:2877`),
  and the builder returns `committed: false` with an empty `sha`.
- `verb_review` (`tools/unattended/unattended.sh#verb_review`) refuses a repeat only where a terminal row
  stands; any other repeat appends a row. This is the report's reading, confirmed by its two skeptics.
- The review template's wrapped stages are `resume:checklist`
  (`tools/workflows/tier2-review.template.js@94dbd5b2:1482`), `resume:probe` (`@94dbd5b2:1650`) and `synth`
  (`@94dbd5b2:2624`). Its finders and skeptics call `agent(` inside their fans.
- S5's word list, run from scratch over both templates at HEAD, names `commit` (the driver, `git add` and
  the block), `record` (the driver) and `dispose` (the driver), and clears `subjects` and the review
  template's stages. So it reds on today's tree for exactly the stages this unit unwraps.

### The change

Each of S1's calls loses the helper's name and keeps its argument list: `await runWithRetries(` becomes
`await agent(`. Each is straight-line code at top level or in `writeRound`, outside any loop, which the
fan-out rule reads as a plain spawn.

In the unit harness:

```js
const r = await agent(
  PROMPT,
  Object.assign({ label: identity, schema: UNIT_SCHEMA }, /* the options, unchanged */),
)
```

Its shape paragraph goes back to one deliberate exception, the one top-level definition. A `retries`
key in its args is an undeclared key, which that file ignores as it ignores any other.

The check of S5 is one `node` program in the suite, in the shape the evidence ran: split the source on
`await runWithRetries(`, take each piece up to `renderAgentLabel(`, match. It grades text and not
behaviour. What a wrapped prompt tells an agent in other words it cannot see, which is why the stage
set is declared beside it: a newly wrapped stage reds until a person adds it.

### Inventory

Minted: the fixture key `__wroteThenNull`, and the arm group `DBR90`. No function is minted.

### Migration

None. A caller that passes `retries` to the unit harness gets one spawn.

### Rollout

Live at landing.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js` (S1, S3's forwarding)
- `tools/workflows/unattended-build.js` (rendered by the protocol parity script's `--render`)
- `tools/workflows/unattended-unit.js` (S3)
- `tools/workflows/unattended-build.test.sh` (S5, S6, the floor)
- `tools/workflows/README.md` (S7)
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md` (rendered by `adopt-unattended.sh`)
- `tools/roles/SKILL.template.md`
- `.claude/skills/build/SKILL.md` (rendered by `adopt-roles.sh --scaffold`)
- `help/roles.md`
- `tools/run-gates/selftest-budgets.txt` (the `unattended-build self-test` row)

### Alternatives rejected

- **Read back, then repeat.** Each prompt would look for what the earlier attempt landed: the run-state
  row of the round, the spec commit, the promoted specs, a `Pass:` commit. Each look-up is prose told to
  an agent, which no script can check.
- **Keep `retries` in the unit harness, graded and unused.** A policy value with no route reads as one
  that has a route.

## 5. Production-readiness checklist

- security — narrows: a stage that writes is spawned at most once, so `roles.retries` multiplies reads only.
- perf / scale — fewer spawns on a dead agent; none otherwise.
- error / empty / loading states — a null from a writing stage takes the stop it took before
  `TOOL-dBoundRoles-5`; the caller reads the run state before it re-invokes.
- observability — the `retries` log line names the stage it applies to, and the unit harness logs none.
- risks — a writing agent that died before its write costs a re-invocation where a re-run used to mend
  it. That is the price of never repeating a write.
- testing — the stub runtime arms and the static check, each with its staged break below.
- migration — none.
- user docs — `help/roles.md` and the guides of S7.

## 6. Acceptance criteria

The probe of these criteria is a scratch `node` file holding the body of the suite's `run_wf` function
with S6's value, run over the named script with `retries` 2; S6's value stands for the write.

- **AC1** — When the probe runs `tools/workflows/unattended-build.js` with the round record answering
  `{"__seq":[{"__wroteThenNull":"review"},{"token":"CONVERGED","exitCode":0}]}` over a zero-blocker
  audit, the trace holds one `agent:record` line and one `wrote:review` line, and the run ends on
  `THROW` naming `the round was not recorded`.
  Red when: the record is spawned again after a null, so the trace holds a second `agent:record` line.
- **AC2** — When the probe runs `tools/workflows/unattended-build.js` over the audit-off roster with the
  spec commit answering `__wroteThenNull` and then a good commit, the trace holds one `agent:commit` line
  and the run ends on `THROW` naming `the spec commit stage returned nothing`.
  Red when: the commit stage is spawned again and the second return is taken.
- **AC3** — When the probe runs `tools/workflows/unattended-build.js` over a one-blocker audit recorded
  `NON-CONVERGENT` with the disposal answering `__wroteThenNull` and then a good disposal, the trace
  holds one `agent:dispose` line and the result's note names `the disposal stage returned nothing at all`.
  Red when: the disposal is spawned again and the roster is handed out.
- **AC4** — When S5's check is run by `node` from scratch over `tools/workflows/unattended-build.template.js`
  and `tools/workflows/tier2-review.template.js`, it prints no finding; over a copy whose record call is
  wrapped in `runWithRetries` again it names `record`, and over a copy with the resolver unwrapped it
  names the missing `subjects`. And the probe, with the subject resolver answering null and then a good
  object, traces two `agent:subjects` lines.
  Red when: a wrapped stage that names the driver passes, the check finds no call and calls that clean,
  or the resolver stops being re-run.
- **AC5** — When the probe runs `tools/workflows/unattended-unit.js` with the builder answering
  `__wroteThenNull` and then a committed object, the trace holds one `agent:build` line and the result
  reads `"committed":false`.
  Red when: the builder is spawned a second time after its commit.
- **AC6** — When `grep -n "retries\|ATTEMPTS\|sequential-agents" tools/workflows/unattended-unit.js` runs
  it prints nothing, and when the probe runs the build harness with `retries` 2 the result's
  `dispatch.args` carries no `retries` while the `wargs:` line carries `"retries":2`.
  Red when: the child keeps a count it does not use, or the parent drops the review call's.
- **AC7** — When `grep -c "gov:sequential-agents(5)$" tools/workflows/unattended-build.js` runs it prints 1,
  the helper's own loop, and `git diff --no-index -U0 tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js`
  shows only lines whose template side holds a `{{` token.
  Red when: a writing stage keeps a loop of its own, or the render was edited by hand.
- **AC8** — When `grep -n "retries" tools/workflows/README.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/roles/SKILL.template.md .claude/skills/build/SKILL.md help/roles.md`
  runs, no line gives `retries` to the unit harness, and the README's entry names the stages spawned once.
  Red when: a guide still tells the caller to pass `retries` to `unattended-unit`.
- **AC9** — When `grep -l "TOOL-dBoundRoles-5@rev-6" memory/builds/dBoundRoles/build/*TOOL-dBoundRoles-90-deviation*`
  runs, it prints one path, and `git diff f3ec096a8 -- memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-5.md`
  shows no line outside its generated records region.
  Red when: the amendment has no record, or the CLOSED spec was edited.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out` · `verifier fan-out self-test` · `review-join self-test` · `policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC2 AC3 AC5 · each stage answering `__wroteThenNull`, staged by putting `runWithRetries` back around that stage's call and the marked loop back around the builder's · FLOOR_ASSERTIONS by the rows added less the DBR5 rows replaced, counted by reading
New arm: tools/workflows/unattended-build.test.sh · covers AC4 · the static check over the two templates, staged by a copy wrapping the record again, a copy with the resolver unwrapped, and a source holding no call · the same floor
New arm: tools/workflows/unattended-build.test.sh · covers AC6 · `dispatch.args` with no `retries` beside a review call carrying it, staged by restoring the forwarding spread · the same floor

## 8. Open questions

- **F1 — What does a null from a writing stage do?** Options: (a) the stage is spawned once and the null
  takes the stop the file already has; (b) the stage is re-run with a prompt that first reads back what the
  earlier attempt landed. Both meet the report's fix; (b) rests on prose told to an agent, and no script of
  these harnesses can read the tree to check it. RESOLVED (agent, 2026-11-24, delegated): (a), the one whose
  criteria a stub runtime observes whole. options: (a) > (b) · pick: (a) · admitted-by: principle.p18 ·
  widens: none · relaxes: a writing stage that died before its write is no longer re-run
- **F2 — What becomes of `retries` in the unit harness, whose one spawn is the builder's?** Options: (a) it
  is deleted, with its loop, its refusal, its forwarding and its texts; (b) it is still read and refused
  when malformed, and never used. (b) keeps `TOOL-dBoundRoles-5` AC7's third file and leaves a policy value
  with no route. RESOLVED (agent, 2026-11-24, delegated): (a), the charter's delete-rather-than-disable
  rule; the amended criterion is S8's record. options: (a) > (b) · pick: (a) · admitted-by: principle.p18 ·
  widens: none · relaxes: a malformed `retries` handed to the unit harness is no longer refused
- **F3 — Does the static check grade a list of forbidden words, or a declared set of stages?** Options:
  (a) both; (b) the words alone; (c) the set alone. (b) passes a writing stage told in other words, and
  (c) passes a driver call added to a declared stage. RESOLVED (agent, 2026-11-24, delegated): (a).
  options: (a) > (b) > (c) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-24 · initial draft, from the brief `2026-11-24-prompt-TOOL-dBoundRoles-90-spec-brief`
  and item H4 of `2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1`.

## 10. Reuse audit

The seams extended are `runWithRetries` in `tools/workflows/unattended-build.template.js`, which keeps its
one caller, the suite's `run_wf` stub runtime and its `__seq` list, and the stops each stage already has.
`python tools/codebase-map/reuse_lookup.py "spawn a workflow stage again when its agent returns nothing"`
ranked `returns`, `load_workflows`, `derive_stage_map` and `check_return`, none a spawn helper, so no
existing seam fits beyond the helper this unit narrows. `scanAgentCalls` of the review harness's suite
reads a call's options and drops its prompt, the half S5 grades, so the check reads the source beside it.
The recall probe returned `TOOL-dBoundRoles-5`, its acceptance ledger, the verbs guide,
`TOOL-dBoundRoles-39` and `TOOL-dRetiredFork-22`'s account of a record agent that died.

Recall terms used: `python tools/memory-recall/query.py "may a harness stage whose agent died after its write be spawned again" --terms "runWithRetries roles.retries harness re-run null return single-call stage double-record review round idempotent builder spawn"`
