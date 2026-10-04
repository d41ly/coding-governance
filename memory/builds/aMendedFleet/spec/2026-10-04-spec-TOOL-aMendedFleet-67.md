# TOOL-aMendedFleet-67 — review and drift harnesses can spawn their judges as a read-only agent type that omits the charter

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 67

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Every agent a review or drift workflow spawns loads this repo's charter, `AGENTS.md` through its
`CLAUDE.md` import, before it reads one line of its task: 64,344 bytes at the report's tip, about
16,000 tokens at four bytes a token, in each of the 2,239 workflow agents counted since 09-04. A finder
or a skeptic judges code against a brief the harness writes; it does not land, commit or mint ids, so
the charter buys it little. The report proposed a worker type that omits the charter for those agents
only. This unit gives `tools/workflows/tier2-review.js` and the two drift-audit workflows an optional
`workerType` argument that spawns their judges as a named agent type, defaulting to today's behaviour,
so the one A/B run the report asks for can measure precision and first-turn tokens before anything
defaults to it.

## 2. Scope (IN)

- **S1** — `tools/workflows/tier2-review.template.js` and its render read `args.workerType`. Absent,
  every spawn is byte-identical to today's. Present, it must match `^[A-Za-z][A-Za-z0-9_-]{0,63}$` or
  the harness throws an error opening `tier2-review:` and naming `workerType` before any agent is
  spawned; when it
  matches, every FINDER and every SKEPTIC `agent(...)` call carries `agentType: workerType` in its
  options, and the resume probe and the synthesis agent carry none. Observed by AC1, AC2, AC3.
- **S2** — Under `workerType`, the finder and skeptic prompts carry no DURABILITY instruction to write
  a `find-*.json` or `verify-*.json` file, because a read-only type holds no Write tool and its own
  prompt forbids file creation. The harness logs one line naming the worker type and saying this
  run's lens and batch results are not durable, so a resume re-dispatches them. Observed by AC1.
- **S3** — `tools/workflows/drift-audit-code.template.js`, `tools/workflows/drift-audit-state.template.js`
  and their renders read the same argument under the same validation, and pass it to their SKEPTIC
  batches only. Their finders keep the default type. Observed by AC4.
- **S4** — `tools/workflows/README.md` documents the argument in each harness's `args` description and
  states three facts with a verified stamp: which built-in types omit the charter on the CLI it was
  read from, that a project agent definition cannot ask for that on that CLI, and why the drift
  finders are excluded. It names the restart caveat for a custom definition as UNVERIFIED. Observed by
  AC5.
- **S5** — New arms in `tools/workflows/tier2-review.test.sh` record the spawn options under a
  `workerType` and without one. NOT OBSERVED by a criterion here: the suite runs once at the close,
  and the arm is declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- The A/B run itself, one tier2 review with and without `workerType`, scored on precision and
  first-turn tokens. §8 F4 moves it to `TOOL-aMendedFleet-93`: it must run from the main loop, and
  its token half reads each judge's sidechain transcript directly, not unit 70's tokens-to-READY
  mode, which stops at a main thread's READY point.
- Making any worker type the default. That is `TOOL-aMendedFleet-93`'s decision to take on its
  measurement.
- A custom agent definition. §8 F1 found that the installed CLI does not let one omit the charter.
- The drift-audit FINDERS. Each writes its prose writeup to a file as it works, which is both its
  deliverable and the durability control the harness records after a two-hour finder died with
  nothing on disk; a type with no Write tool can hold neither.
- The orchestrating agents: the synthesis agent writes the report file, and the resume probe reads
  lens files from the git common dir.

### Edges

- **hands-off** `TOOL-aMendedFleet-93` — the A/B run and the default it may set, which §8 F4 moves
  to that unit, ordered after this one.

## 4. Design

### Evidence

Read at base `7af5f564`, and from the PATH CLI on node a, `claude --version` 2.1.178, on 2026-10-04.

- A workflow `agent()` call accepts `agentType` in its options: `tools/workflows/orient-counterfactual.js`
  passes it, and the aReplayedCard unit 5 acceptance ledger records a built-in `Explore` spawn through a
  Workflow, and a named refusal, `agent type 'orient' not found`, for a custom type with no definition.
- The CLI's spawn path omits the user context's charter only when the agent definition sets
  `omitClaudeMd`, the caller supplies no user context of its own, and a server flag defaults on. Read
  from the binary with a read-only `grep -a -o` around each occurrence of the field.
- Only two definitions set it: the built-in `Explore`, whose model is `haiku`, and the built-in `Plan`,
  whose model is `inherit`. Both disallow the file-editing tools and carry a read-only prompt that
  forbids creating files, with Bash allowed for read-only commands such as `git diff`.
- The CLI's list of known definition front-matter keys carries `tools`, `disallowedTools`,
  `permissionMode`, `maxTurns`, `isolation` and `keep-coding-instructions`, and not `omitClaudeMd`.
- `tools/workflows/tier2-review.js` tells every finder and skeptic to Write its return to
  `<keyDir>/find-<lens>.json` or `verify-<a>-<b>.json` before returning; the resume probe reads those
  files to reuse a lens or batch.
- The drift finders write `wave1-<lens>.md` under `outDir` early and append as they go; the synthesis
  agent reads those writeups by path. The drift skeptics write nothing and only return verdicts.

### Inventory

No new function. The argument is read inline beside `intensity` and `kind`, and refused with the
harness's existing `throw new Error('tier2-review: ...')` shape; the two drift harnesses refuse with
their own prefixes.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/drift-audit-code.template.js`
- `tools/workflows/drift-audit-code.js`
- `tools/workflows/drift-audit-state.template.js`
- `tools/workflows/drift-audit-state.js`
- `tools/workflows/README.md`
- `tools/workflows/tier2-review.test.sh`

### Rollout

Dark: no caller passes `workerType`, so every review and drift run behaves as today until the A/B unit
measures one and decides. The review-harness and drift-audit kit versions move once, minted at the
lander by unit 65 or owed at the close.

### Alternatives rejected

- **A custom `gov-worker` agent definition under the agents directory.** On this CLI it cannot omit the
  charter, so it would buy a tool restriction and a session restart, and none of the saving.
- **Defaulting to `Explore`.** Its model is `haiku`, which changes the judge as well as the context;
  an A/B could not tell the two effects apart.
- **Routing the drift finders too.** Their writeup file is their deliverable and their durability
  control; returning it inline instead moves the whole writeup through the orchestrator.

## 5. Production-readiness checklist

- security — narrows what a judge can do: the built-in read-only types hold no Write or Edit, and the
  argument is shape-validated before it reaches a spawn option.
- perf / scale — the point of the unit; the saving is measured by the A/B unit, not claimed here.
- error / empty / loading states — an unknown type reaches the spawn and comes back as the platform's
  named `not found` refusal, which the harnesses already handle as a dead agent; a malformed value is
  refused before any spawn.
- observability — the one log line under S2 says which type ran and that durability was off.
- risks — a read-only type's own system prompt may shift what a finder reports; that is precision,
  which is exactly what the A/B measures before any default moves.
- testing — AC1 to AC6 directly; the arm in S5.
- migration — none.
- user docs — S4.

## 6. Acceptance criteria

- **AC1** — When `tools/workflows/tier2-review.js` is evaluated as an async function body with recording
  stub `agent` functions and args carrying `workerType: 'Plan'` and two canned findings, every finder
  and skeptic spawn's options carry `agentType` equal to `Plan`, the probe and synthesis spawns carry
  none, no finder or skeptic prompt contains `DURABILITY`, and the log carries the S2 line.
  Red when: a judge spawn lacks the type, an orchestrating spawn carries it, or a judge is still told
  to write a file.
  fixture: the stub runner is the evaluation shape the harness's own suite already uses, written to
  the scratchpad for this check.
- **AC2** — When the same stub run is made with no `workerType`, against the unit's tip and against
  `tools/workflows/tier2-review.js` as it stood at the pass's starting commit, the recorded prompts
  and options of every spawn are identical between the two. The starting commit, not base
  `7af5f564`, because units 11, 17 and 18 move the same harness's prompts first.
  Red when: a default run's prompts or options change.
- **AC3** — When the stub run is made with `workerType` set to `'two words'`, to `7` and to a
  65-character name, each throws an error naming `workerType` before the first spawn is recorded. These
  are the staged breaks for S1's refusal.
  Red when: any of the three reaches a spawn.
- **AC4** — When `tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js` are
  each evaluated the same way with `workerType: 'Plan'` and one canned finding, every skeptic batch
  spawn carries `agentType` equal to `Plan` and no finder spawn carries it.
  Red when: a finder is routed, or a skeptic is not.
- **AC5** — When `grep -n "workerType" tools/workflows/README.md` runs, it hits all three harnesses'
  argument descriptions, and the section beside them names `Plan`, `Explore`, the CLI version the
  fact was read from with its date and node, and the drift finders' exclusion.
  Red when: an argument is undocumented, or the CLI fact carries no stamp.
- **AC6** — When `node tools/workflows/check-workflow-syntax.js` and
  `bash tools/workflows/check-verifier-fanout.sh` run at the unit's tip, both exit 0, and a `diff` of
  each touched template against its render differs only on the `FANOUT_CAP` lines it differed on at
  the pass's starting commit.
  Red when: a script no longer parses, the verifier cap moves, or a render and its template diverge.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `review-protocol parity (kit vs dogfood)` · `review-join ban (no ref-keyed join)` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `install-prefix (shipped surface)` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/workflows/tier2-review.test.sh` · stub spawns recorded with and without `workerType`, against the base harness, which reads no such argument · none

## 8. Open questions

- **FACT-QUESTION · F1 — Can a project agent definition ask the installed CLI to omit the charter?**
  Probe: a read-only `grep -a -o` over the PATH CLI binary for the definition front-matter key list and
  for every occurrence of `omitClaudeMd`. Observation: the key list does not carry the field, and the
  field is set only on the built-in `Explore` and `Plan` definitions and read on the spawn path.
  Liveness: the same probe finds `permissionMode` in that key list and `omitClaudeMd` on `Explore`, so
  it can return a positive. Recorded on 2026-10-04 against 2.1.178; a later CLI may differ, which is
  why the argument names a type rather than this unit shipping one.
  RESOLVED (agent, 2026-10-04, delegated): no custom definition; the argument names a type, and the
  built-in read-only types are the ones that omit the charter on this CLI.
- **F2 — Which agents does the argument route?**
  Options: every agent; finders and skeptics in all three harnesses; tier2 finders and skeptics plus
  drift skeptics. The orchestrating agents write the report and read the lens files; the drift finders
  write their deliverable as they go.
  RESOLVED (agent, 2026-10-04, delegated): tier2 finders and skeptics, and the drift skeptics, per S1
  and S3.
- **F3 — What happens to tier2 durability under a type with no Write tool?**
  Options: refuse the combination; send the instruction anyway and let the type refuse it; send none
  and announce that resume reuse is off. Refusing makes the argument unusable with the only types that
  omit the charter; sending it asks an agent to break its own read-only prompt.
  RESOLVED (agent, 2026-10-04, delegated): send none and announce it, per S2.
- **F4 — Does the A/B run belong to this unit?**
  Options: an acceptance criterion here; a unit of its own. A unit pass runs inside a Workflow
  sidechain, which holds no Workflow tool, so no pass of this unit can start a tier2 run; and its
  token half needs unit 70's tokens-to-READY mode, ordered after this unit.
  RESOLVED (agent, 2026-10-04, delegated): split — the A/B run and the default it may set move to a
  new unit the run adds, ordered after units 67 and 70. That unit is `TOOL-aMendedFleet-93`, whose
  §10 found unit 70's mode cannot see a judge's first turn, so it keeps the order and not the read.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from a read of the three harnesses' spawn sites and durability
  instructions at base and of the PATH CLI's agent definitions on node a.
- rev-2 · 2026-10-04 · §3 · AC2 · AC6 · §8 · M2 cross-read: the A/B unit is `TOOL-aMendedFleet-93`,
  which reads judge transcripts and not unit 70's mode, so the non-goal and the edge now name it;
  AC2 and AC6 compared against base, which units 11, 17 and 18 move first, and now compare against
  the pass's starting commit.

## 10. Reuse audit

The seam extended is the `agentType` spawn option `tools/workflows/orient-counterfactual.js` already
passes, whose behaviour through a Workflow the aReplayedCard unit 5 ledger recorded: a built-in type
spawns, an absent custom one is a named refusal. The argument validation reuses each harness's own
`throw new Error` refusal shape. `python tools/codebase-map/reuse_lookup.py "spawn review finder and
skeptic agents as a chosen agent type"` returned only name-stem neighbours such as `find_block` and
`derive_review_verdict`, none of which spawns an agent; the map does not index the workflow scripts'
spawn options, so `git grep -n agentType tools/workflows/` was the probe and found the one precedent.
Recall returned `TOOL-aReplayedCard-9`, the stage-2 matrix of an `orient` custom type against
`Explore`, and the orientation design record that first noted `Explore` skips the charter, and
`TOOL-aProbedUnit-16`, on the review and drift harnesses handing their agents no scratch root, which
this unit does not change. Where the report and the tree disagree: the report wrote `omitClaudeMd` as
a field a worker type could set; on the installed CLI a project definition cannot.

Recall terms used: `python tools/memory-recall/query.py "can review and drift agents run without
loading the charter, as a read-only agent type" --terms "omitClaudeMd agentType worker read-only
finder skeptic tier2-review agent definition CLAUDE.md context tokens orient Explore"`
