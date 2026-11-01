# TOOL-dScopedBuild-6 — the per-pass checklist's retirement witnessed at Build: a pass whose prompt calls the lookup by its write set's paths refused before it spawns

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 8 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0404@f111410c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-7 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-3 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-1 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

NT-24 retired writing-time serving by path, "with the per-pass checklist and the prebuild"
(`night-pass-two.md:473-474`), and dFurnishedOrders retires the two keys that carried them. This unit
witnesses that retirement at Build, where a pass is built: the unit harness refuses, before any spawn,
a pass whose prompt would have its builder call the bug-class lookup over its write set's paths, by
whatever argument the lookup arrived, so the retirement cannot return through a key nobody retired.

## 2. Scope (IN)

- **S1** — The refusal. `tools/workflows/unattended-unit.js`, after its prompt is composed and before
  its one `agent()` spawn (`:333`), tests the composed prompt for the lookup NT-24 withdrew: the
  path-selected call `gotchas.py --for-paths` and the per-pass call `gotchas.py --for-diff HEAD~1..HEAD`,
  matched as a command, its words separated by whitespace. A match throws `unattended-unit: this pass's
  prompt spells <the match>, the per-pass bug-class lookup NT-24 withdrew; the work order's named
  classes stand in its place (TOOL-dFurnishedOrders-4 S5)`, and nothing is spawned. This item adds a
  refusal and takes nothing out of the tree; the withdrawal it witnesses is TOOL-dFurnishedOrders-4 S5's. The test reads the prompt, the
  whole of what the builder is told, so a `ground`, a `driver` or any other argument the prompt
  spells is held alike. Observed by AC1 and AC2.
- **S2** — Both modes. The refusal runs before the mode split matters, so an `attended` dispatch, the
  `/build` Skill's, and an `unattended` one are refused alike. Observed by AC2.
- **S3** — Its edge. A ground naming the closing review's range, `gotchas.py --for-diff <BASE>..HEAD`,
  which BUILD-METHOD M8 keeps (`tools/memory-tree/BUILD-METHOD.template.md:253`), is not refused, and a
  clean dispatch's prompt is byte for byte the prompt the harness composes without this unit.
  Observed by AC3 and AC4.
- **S4** — The file's shape. The test is one `if` beside the harness's existing pre-spawn refusals
  (`unattended-unit.js:136-145`), with its pattern inline: the header's style rule, one top-level
  definition and no loop, array method or arrow (`:20-25`), holds, and no name is minted. The header
  paragraph on `prebuild` (`:43-51`), which FO-4 S5 takes out, gives way to two sentences stating this
  refusal and what it does not check (§4). Observed by AC5.

## 3. Non-goals (OUT)

- The retirement itself: the `checklist` and `prebuild` keys, their sentences and the build harness's
  `CHECKLIST` (TOOL-dFurnishedOrders-4 S5), the refusal of a caller passing either key and its
  observation (TOOL-dFurnishedOrders-30 S1), and the upgrade steps' witness over an adopter's call
  sites (TOOL-dFurnishedOrders-25). Cited, never re-specced.
- BUILD-METHOD M6's sentence owing the per-pass checklist (`BUILD-METHOD.template.md:187-190`): it is
  TOOL-dFurnishedOrders-4 S6's, which gives M6's paragraph and its command way to one sentence (§8 F2).
- The spec audit's checklist, `AUDIT_CHECKLIST` (`unattended-build.template.js:588`): a review's,
  NT-25's question, not a pass's.
- gap-build-04's second half, "agents a harness spawns are uncounted" (`research-build.md:112`): it is
  not in cl-dClosedLoop-0404's text, and no clause of this build carries it.
- A builder that calls the lookup unprompted: NT-26 rejected serving classes at runtime, and nothing
  reads a pass's tool calls at HEAD.

### Edges

- **consumes-from** external — TOOL-dFurnishedOrders-4 S5's retired `checklist` key and its post-commit sentence, without which every pass's prompt spells `--for-diff HEAD~1..HEAD` and S1 refuses it; TOOL-dFurnishedOrders-30 S1's key refusal beside this one
- **hands-off** `TOOL-dScopedBuild-35` — S1's refusal pattern, which that unit's S24 widens to the program and mode and to every HEAD-relative one-commit range (id 42)

## 4. Design

### Where the check sits

```
cfg validated (check(...), the retired-key refusals of FO-30 S1)
PROMPT composed (ground, the brief and spec paths, DRIVER_STEPS, the closing sentences)
if PROMPT spells the retired lookup  -> throw, before any log of the builder or any spawn   (S1)
log lines; agent(PROMPT, ...)                                                              (unchanged)
```

The pattern is a literal regular expression in the `if`: `gotchas\.py\s+--for-paths\b` or
`gotchas\.py\s+--for-diff\s+HEAD~1\.\.HEAD\b`. It names the program and the flag, never a prefix, so
a ground naming the kit directory or the word "checklist" is not refused.

### Why the prompt and not the key

The keys are the instance. FO-30 S1 refuses `checklist` and `prebuild`; a `ground` or a `driver` the
parent composes carries free text into the same prompt (`unattended-unit.js:257-258`), and the
night pass two's review asked for "a check red on a planted pass that still calls
`gotchas.py --for-paths`" (`2026-10-19-review-PLAY-dClosedLoop-1-night-pass-two-a.md:107`). The
composed prompt is the whole of what a pass is told, so testing it gates the class: the charter's `[class]` rule.

### What it does not check

The brief file's text: a Workflow script reads no file, and the builder reads the brief itself. A
typed builder's own agent file, which TOOL-dFurnishedOrders-4 S6 rewords
(`tools/roles/agents/gov-builder.agent.md:42-43`). A pass dispatched by hand, outside the harness.
And a builder that runs the lookup unprompted (§3).

### Rollout

Live at landing. A build-run precondition: TOOL-dFurnishedOrders-4 S5 has landed, since until then
the harness's own closing sentence spells `cfg.checklist`, the per-pass command, in every prompt.

### Files touched (estimate)

- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.test.sh`

### Alternatives rejected

- A suite arm re-observing FO-30 S1's key refusal alone. Rejected by the clause's planted pass: a
  `ground` carrying `gotchas.py --for-paths` passes every key check at HEAD (`unattended-unit.js:98-145`
  validates shape, never content), so such an arm stays green on the case the clause names.
- FO-25's `retired_dispatch_args.py witness` run at the Build exit. Rejected by its S1: it scans an
  adopter's tracked call sites, less records and markdown, which is where a pass's prompt is not.
- A transcript reader over the builder's tool calls. Rejected because no reader of a pass's transcript
  exists at HEAD (dWellOiledMachine's transition verifier, `orientation.md:217-218`, is unbuilt), so it
  adds a parent this build does not have for a case NT-26 already ruled out of scope.

## 5. Production-readiness checklist

- security — N/A: no write path, no input beyond the harness's own arguments.
- perf / scale — one regular-expression test over one prompt string per pass.
- error / empty / loading states — a match throws before any spawn; no match changes nothing.
- observability — the throw names the matched text and the retirement it enforces.
- risks — a false refusal on a ground that quotes the command in prose; S3's edge and AC3 bound it.
- testing — the build harness suite's new arms (§7).
- migration — none: a caller still passing the retired lookup by text meets the refusal, whose
  remedy is FO-4 S5's work-order classes.
- user docs — N/A: the harness is driven by the build harness and the `/build` Skill, which already
  stop spelling the command under TOOL-dFurnishedOrders-4.

## 6. Acceptance criteria

- **AC1** — When a node probe evaluates `tools/workflows/unattended-unit.js` as the build harness
  suite's `run_wf` does (`unattended-build.test.sh:162`), with a stub `agent` tracing each spawn and
  args in `unattended` mode whose `ground` ends asking for `gotchas.py --for-paths` over two file
  paths of the pass's write set,
  it throws naming `gotchas.py --for-paths` and traces no `agent:build`.
  Red when: the planted pass spawns with the path lookup in its prompt.
  fixture: the probe is a scratch file the pass writes; FO-4 S5 has landed.
- **AC2** — When the AC1 probe runs the same args in `attended` mode, and again with `driver` set to
  `bash drv.sh && python gotchas.py --for-diff HEAD~1..HEAD`, each throws before any spawn, the second
  naming `--for-diff HEAD~1..HEAD`.
  Red when: a mode or an argument other than the retired keys carries the lookup through.
- **AC3** — When the AC1 probe runs args whose `ground` names `gotchas.py --for-diff 5f0b11f12..HEAD`,
  it spawns once.
  Red when: the closing review's range command, which M8 keeps, is refused as a per-pass call.
- **AC4** — When the AC1 probe runs the suite's clean child args (`CHILD_ARGS`, less the retired
  `checklist`), the traced prompt is byte-identical to the one the harness traced before this unit.
  Red when: the check changes a clean pass's prompt or refuses it.
- **AC5** — When `node tools/workflows/check-workflow-syntax.js` runs, it passes `unattended-unit.js`,
  and `grep -c "^function \|=>" tools/workflows/unattended-unit.js` prints the count it printed before.
  Red when: the refusal adds a definition or an arrow the header's style rule forbids.

## 7. Gates

`unattended-build self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `workflow script syntax` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC2 AC3 AC4 · the planted pass whose `ground` asks for `gotchas.py --for-paths` over its write set, in each mode, and one whose `driver` asks for `--for-diff HEAD~1..HEAD`, its failing case the pass spawned · none

## 8. Open questions

- **F1 — Where does Build witness the retirement?** Options: (a) the unit harness refuses a composed
  prompt spelling the retired lookup, before any spawn; (b) a suite arm over FO-30 S1's key refusal
  alone; (c) a reader of the builder's transcript; (d) FO-25's call-site witness run at the Build exit.
  (b) stays green on a `ground` carrying the lookup, the clause's planted pass, so it fails the
  clause's seen-red case (veto 1); (c) needs a transcript reader no parent at HEAD supplies; (d) reads
  scripts, not passes. Rung 3, the most feature-rich survivor. RESOLVED (agent, 2026-11-01,
  delegated): (a). widens: none · relaxes: none
- **FACT-QUESTION · F2 — Is the M6 sentence that owes the checklist (`BUILD-METHOD.template.md:187-190`)
  this unit's to change?** Probe: `grep -n "BUILD-METHOD.template.md:185-193"` over
  TOOL-dFurnishedOrders-4's spec. Observation that decides: a parent scope item retiring that
  paragraph. Liveness: no hit leaves the sentence to this unit. Run at writing: S6 of
  TOOL-dFurnishedOrders-4 gives M6's per-pass checklist paragraph and its command way to one sentence.
  RESOLVED (agent, 2026-11-01, delegated): cited in §3 and left to that unit; this unit edits no
  method text. widens: none · relaxes: none
- **FACT-QUESTION · F3 — Does TOOL-dFurnishedOrders-4 land before this unit is built?** Probe: the
  `parents:` line of `memory/builds/dScopedBuild/README.md`. Observation that decides: dFurnishedOrders
  named there. Liveness: a build absent from the line prints no match. Run at writing: the line names
  dFurnishedOrders. RESOLVED (agent, 2026-11-01, delegated): a build-run precondition (§4 Rollout), no
  stand-in. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam extended is `tools/workflows/unattended-unit.js`'s own pre-spawn refusals (`check(...)` at
`:98-105` and the `prebuild` throw at `:136-145`, which FO-30 S1 turns into the retired-key refusal),
joined by one more `if` over the prompt the file already composes; the suite seam is
`unattended-build.test.sh`'s `run_wf` (`:162`) and its child fixtures (`:1053`, `:1120`).
`reuse_lookup.py "refuse a retired argument passed to the unit harness before any spawn"` ranked
name-token neighbours only (`before`, `units`, `CensusRefused`), an answer recorded rather than
retried: no shared refusal helper fits a script whose header forbids a second definition. The recall
query found scout A's row and TOOL-dFurnishedOrders-4, whose lines agree with source at
`5f0b11f12` (`:105` the `checklist` check, `:322` the post-commit sentence, `:43-49` the `prebuild`
paragraph, `unattended-build.template.js:565` `CHECKLIST`); scout A's `unattended-build.js:2485` is the
render, its source line the template's.

Recall terms used: `python tools/memory-recall/query.py "is the per-pass bug-class checklist retired and what refuses a pass that still calls it" --terms "per-pass checklist prebuild gotchas for-paths for-diff retired NT-24 unattended-unit refused before spawn"`
