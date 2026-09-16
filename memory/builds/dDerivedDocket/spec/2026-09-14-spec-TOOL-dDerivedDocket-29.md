# TOOL-dDerivedDocket-29 — review durability across a dead fan

**Status:** SPECCED · rev-3 · 2026-09-16 · node d · Tier-2 · base abac6d59 · streams tooling · order 29

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 |

<!-- /gen:spec-records -->

## 1. Goal

A review workflow is all-or-nothing today. When lens or skeptic agents die on a session limit or an
API overload, every result they produced dies with the run, the harness returns a degraded note
that the unattended audit stage throws on, and the re-run pays for every lens again. Make every
lens and skeptic batch write its result to a durable file before it returns, let a re-run of the
same review reuse those files and dispatch only what is missing, and return a distinct
`deferred-platform` exit whenever an agent died, which an unattended run holds on with the workflow
runId recorded as a run fact.

## 2. Scope (IN)

- **S1** Write before return. Every lens prompt in `tools/workflows/tier2-review.js` names one file,
  `<git-common-dir>/review-lenses/<key>/find-<lens>.json`, and tells the agent to write its result
  there BEFORE it returns. Every skeptic prompt names `verify-<first id>-<last id>.json` in the same
  directory. Both finding schemas and the verdict schema gain a REQUIRED `path` field, so an agent
  that skips the write cannot return cleanly. Observed by AC1 and AC12.
- **S2** The review key, computed in the script from its inputs and nothing else: the kind, the
  round, the pinned subject, and a fingerprint over `context`, `byDesign` and `priorFindings`. The
  pinned subject is every `path@blob` in the order given for a spec audit, and the RESOLVED base sha
  plus the RESOLVED head sha for a diff review (§8 F5). Observed by AC2 and AC3.
- **S3** One resume probe agent runs before the Find phase. It resolves `base` and `head` to shas on
  a diff review, and from then on every lens prompt and the record's range line name those shas
  instead of the refs. It reads the key directory and returns each file it finds, parsed. A lens
  whose file carries the computed key is reused; every other lens is dispatched. A dead probe
  dispatches every lens with the refs as given and logs that it did. Observed by AC2, AC3 and AC4.
- **S4** A skeptic batch is reused when its file carries the computed key AND a fingerprint of the
  batch's own findings, ids and claims together. Any other batch is dispatched. Observed by AC5.
- **S5** The `deferred-platform` exit. Every return gains an `exit` field. It reads
  `deferred-platform` whenever any lens, any skeptic batch, or the synthesis returned null, and
  `complete` otherwise. A deferred return carries `blockers: null`, the key, and a `pending` list
  naming every agent label that did not return. It is never `complete`, and no deferred path asks
  the synthesis to write a report that calls the run finished. Observed by AC6 and AC7.
- **S6** The AUDIT adapter in `tools/workflows/unattended-build.js` recognises
  `exit: 'deferred-platform'` BEFORE its non-integer blocker refusal. It returns a structured result
  naming the stage, the round, the pending labels and the hold instruction, records no review round,
  and does not throw. Observed by AC8.
- **S7** The driver. `--hold` gains an optional `--pending-run <runId>`, written as the fact
  `hold-run`; a `--hold` without the flag writes it empty, so no later hold inherits an earlier
  stop's run. The HELD checkpoint gains a `pending run <runId>` line, and a `--resume` take-over of
  a record carrying the fact names the relaunch with that runId. The value is refused, numbered and
  before any write, unless it is 1 to 64 characters of `[A-Za-z0-9_-]`. Observed by AC9 and AC10.
- **S8** Carriers. `tools/workflows/REVIEW-PROTOCOL.template.md` gains the durability rule and its
  render `memory/guides/REVIEW-PROTOCOL.md` is regenerated. The unattended Skill, the verb carrier
  and the stops companion unit 4 creates gain the re-run-once-then-hold step and the
  `--pending-run` flag. `memory/map/features/review-harnesses.md` prose is refreshed. No version
  constant moves here. The review harness moves once for this build's landing range in
  `TOOL-dDerivedDocket-21`, the first unit in build order to change that kit's bytes, and this unit's
  review-harness bytes ride that move; the unattended kit's move is `TOOL-dDerivedDocket-1`'s, and
  this unit's driver bytes ride it. Observed by AC11 and AC13.

## 3. Non-goals (OUT)

- `tools/workflows/drift-audit-code.js` and `drift-audit-state.js` keep today's all-or-nothing fan.
  They run on demand and outside any landing path, and none of the stop census's entries was one.
  Porting this shape to them is a follow-up.
- No change to the lens catalogue, the concurrency cap, the verifier arithmetic, or any finding
  field other than the added `path`.
- No answer to whether a runId survives a compaction or whether the platform caches a dead agent's
  null. `DEPL-aHoistedPass-8` records that as UNVERIFIED, and this unit keeps its conclusion: the
  platform's prefix cache is a bonus, and the files are the mechanism.
- No automatic retry inside the harness. A workflow script has no clock and cannot wait out a limit;
  the caller re-runs.
- No pruning of old key directories. Each holds a few kilobytes of JSON under the git common dir,
  which no gate reads and nothing commits.
- The `--hold` verb, its codes, the lease, the checkpoint block and the take-over are unit 4's. This
  unit adds one flag, one fact and two printed lines.
- `tools/workflows/unattended-build.test.sh` is run by no bar at BASE, which the open ask
  `TOOL-dBriefedPass-7` records. Registering it is that ask's work; this unit adds an arm to it and
  observes the arm by hand.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-4` — the `--hold` verb, its fact set, the checkpoint block
  and the `--resume` take-over. This unit extends all four with the pending run; without them there
  is no hold to carry the runId and no checkpoint to print it.

## 4. Design

### Where the results live, and why there

`<git-common-dir>/review-lenses/<key>/` is resolved by the agent with `git rev-parse
--git-common-dir`, because the script has no filesystem and cannot. The git common dir is chosen for
three properties. Nothing there is tracked, so a careless `git add memory/` cannot commit a lens file
into a reviews folder, where hygiene check 5's filename grammar would red it. It is shared by every
worktree on the node, which is what a take-over from another worktree needs, and unit 4's lease
already lives there. And it is the house precedent: the gate runner persists per-leg logs under
`<git-dir>/gate-logs/`.

A resume on ANOTHER node sees no files and dispatches every lens. That is the cost of a node-local
store, and it is paid only on a cross-node take-over.

### The key

```
key = <kind> "-r" <round> "-" <subject> "-" <fnv1a32(canonical JSON of context, byDesign, priorFindings)>
subject (spec-audit)  = fnv1a32 of every "<path>@<blob>" joined by newlines, in the order given
subject (diff-review) = <resolved base, first 12 hex> "-" <resolved head, first 12 hex>
```

FNV-1a is written with `Math.imul` and string built-ins, which a workflow script admits; the runtime
refuses only the clock and randomness. The human-readable parts make a collision need the same kind,
round and subject as well as a 32-bit hash match. Each file carries the key in a `key` field, and
reuse compares that field with the computed string, never the directory name alone.

### The probe, and why one agent rather than a reader per lens

The probe returns every present file's parsed content under a schema whose items are the lens and
verdict schemas, so a malformed file fails validation instead of being trusted. Re-emitting a file's
JSON costs its output tokens once. A reader agent per reused lens would cost a spawn per lens on a
platform that has just been refusing spawns, and a caller-supplied `reuse` argument would put the
burden on every caller, including `unattended-build.js`, which has no filesystem either.

The probe is trusted exactly as far as a lens is. It could fabricate an empty lens, and so could the
lens it replaces. Everything a reused lens returns still passes through the skeptics.

### The fan-out shape does not change

A reused lens's thunk returns its cached value and never calls `agent()`. The receiver stays
`LENSES.map(...)` over the marked ternary of two array literals, which is the one dialect
`tools/hooks/agent-cap.js` admits here, and the verify receiver stays `batches.map(...)`. So neither
`verifier fan-out` nor the hook at the tool call sees a new shape. Ids are still assigned after every
lens has returned, in lens order. When every lens is reused, the ids and batches come out identical,
which is what lets a dead synthesis re-run alone. When a dead lens is re-dispatched, the ids after it
shift, the batch fingerprints stop matching, and those batches run again, which is the correct
outcome: a verdict is reused only for the exact findings it judged.

### Every exit, at BASE and after

| Path at BASE (`tier2-review.js`) | Returns at BASE | Returns after |
|---|---|---|
| every lens dead (`:371-378`) | note `UNVERIFIED`, `blockers: null` | `exit: 'deferred-platform'`, pending names every `find:` label |
| zero findings, some lens dead (`:379-386`) | note `partial: … survivors found nothing` | `deferred-platform`, pending names the dead lenses |
| zero findings, none dead | note `clean: 0 findings` | unchanged, plus `exit: 'complete'` |
| all refuted, some agent dead (`:474-484`) | note `… treat as partial` | `deferred-platform` |
| all refuted, none dead | note `all findings adjudicated and refuted` | unchanged, plus `exit: 'complete'` |
| synthesis dead (`:598-603`) | note `UNVERIFIED: the synthesis agent died` | `deferred-platform`, pending `synth`; a re-run reuses every lens and batch and dispatches only the synthesis |
| a skeptic batch dead, synthesis ran | note `PARTIAL`, integer `blockers` | `deferred-platform`, `blockers: null`; the synthesis is NOT run on a partial verify |
| every agent returned | note `complete` | unchanged, plus `exit: 'complete'` |

The harness cannot tell a user's mid-run skip from a death, because both return null, so both
defer. That is the right reading for a review: an unjudged finding was never a result.

### The unattended route

`unattended-build.js` returns
`{stage: 'Audit', exit: 'deferred-platform', round, pending, key, next}` where `next` names the
remedy: re-run this workflow once with identical args, and on a second deferral hold. The Skill's
step, in the order the session runs it:

1. On the first `deferred-platform`, re-run with identical args. Reuse makes it cost only what died.
2. On a second one, `--hold <slug> --code platform-limit --until after <reset UTC>` when the tool
   result's failures name a usage or session limit, and `--code platform-unavailable --until probe
   api` otherwise, in both cases with `--pending-run <runId>` from the Workflow tool result.

### The driver fact

`hold-run` joins unit 4's hold facts and is rewritten by every `--hold`. The checkpoint prints it
only while the record is HELD, so a value left behind after a resume misleads nobody. The observed
runId shape, measured from this repo's review records, is `wf_` then 8 hex, a dash and 3 hex, as in
`wf_c6bc1036-ec2`. The validator admits that shape without pinning it, because the platform owns the
format.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `deferred-platform`, `complete` | `exit` values | none; a closed pair the adapter tests by equality |
| `review-lenses/<key>/`, `find-<lens>.json`, `verify-<a>-<b>.json` | file names under the git common dir | none |
| the key and fingerprint helpers in `tier2-review.js` | JS functions | lexicon `js.function`, camel; each name passes `python tools/lexicon/lexicon.py --suggest <name> --as js.function` before it is written |
| `--pending-run` | driver flag | none |
| `hold-run` | run fact | none |

### Files touched (estimate)

`tools/workflows/tier2-review.js` · `tools/workflows/tier2-review.test.sh` ·
`tools/workflows/unattended-build.js` · `tools/workflows/unattended-build.test.sh` ·
`tools/workflows/REVIEW-PROTOCOL.template.md` · `memory/guides/REVIEW-PROTOCOL.md` ·
`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/VERBS.template.md` · `tools/unattended/SKILL.template.md` · unit 4's stops
companion template · the rendered guides · `memory/map/features/review-harnesses.md`.

### Alternatives rejected

Each candidate below lost on a fact recorded in the tree or on an observation of the source.

- **The platform's `resumeFromRunId` as the mechanism.** Rejected by `DEPL-aHoistedPass-8`, which
  records that runId survival across a compaction is UNVERIFIED, and by the `aFusedCharter` park,
  whose recorded runId could restore nothing because no lens had completed. A measurement that a fan
  dying whole kept the files its prompts asked for, while every structured return was lost, exists
  only in one node's local memory and is UNVERIFIED here. The runId is recorded anyway, as the bonus
  path.
- **Each lens checks its own file and returns early.** Every lens is still spawned, so the re-run
  dispatches four where the acceptance says two, and spawning is exactly what a recovering platform
  refuses first.
- **A caller-supplied reuse list.** `unattended-build.js` is a workflow script with no filesystem, so
  the unattended route could not supply one.
- **Lens files under the build's `reviews/` folder.** Check 5's filename grammar reds any free-named
  file there the moment it is tracked.

## 5. Production-readiness checklist

- security — agents write only under the git common dir, a location outside the tree that nothing
  tracks. The probe returns data through schema validation and never a command. The runId is
  validated and never executed or parsed further.
- perf / scale — one extra serial agent per review, whose output is the size of the reused results.
  A re-run after a partial death costs only the dead agents.
- error / empty / loading states — a dead probe dispatches everything and says so; a malformed file
  fails the probe's schema and its lens is dispatched; an absent directory means nothing to reuse.
- observability — the `exit` field on every return, the `pending` labels, a log line per reused lens
  and batch, and the `pending run` checkpoint line.
- risks — a stale file reused for a changed question. The key covers every input the lens prompt
  interpolates, and AC3 stages each component of the key.
- testing — whole-script arms in `tools/workflows/tier2-review.test.sh` using the AsyncFunction
  runner `tools/workflows/unattended-build.test.sh` already uses; driver cases by hand in a scratch
  fixture repo, D12-h's method (b).
- migration — none. Existing callers read `exit` only if they want it; the unattended adapter is the
  one caller changed.
- user docs — the review protocol's rule, the Skill step, the verb carrier entry and the companion
  row.

## 6. Acceptance criteria

- **AC1** — When `bash tools/workflows/tier2-review.test.sh` evaluates the whole script with stub
  hooks, every traced `find:` prompt names a file under `review-lenses/` ending `find-<lens>.json`,
  and both finding schemas list `path` in `required`.
  Red when: `path` is optional, so an agent that never wrote its file still returns cleanly.
  permission: the suite is a held leg; its arms run at the build's one post-build bar with
  `GATE_SELFTESTS=1`, and each staged break is observed by hand in a scratch copy.
- **AC2** — When a first stub run has two of the four lens agents return null, and a second run
  with identical `args` is fed a probe return carrying the two surviving files under the computed
  key, the second trace records exactly two `find:` spawns.
  Red when: the re-run dispatches all four lenses.
- **AC3** — When the probe returns a lens file whose `key` field differs from the computed key in one
  component only — another round, another head sha, another resolved base sha after `origin/main`
  moved, one spec-audit subject's blob, or the fingerprint over `context`, `byDesign` and
  `priorFindings` — `tools/workflows/tier2-review.test.sh` sees that lens dispatched in each case.
  Red when: the key omits a component, or reuse matches on the lens name or the directory alone, so
  a stale lens answers a changed question.
- **AC4** — When the probe stub returns null in `tools/workflows/tier2-review.test.sh`, every lens
  is dispatched and the log carries a line saying nothing could be reused.
  Red when: a dead probe is read as every file present, so no lens runs and the review is empty.
- **AC5** — When a `verify-<a>-<b>.json` file carries the right ids but a fingerprint over
  different claims, the batch is dispatched; with a matching fingerprint it is reused.
  Red when: batch reuse keys on the id range alone, which after a changed lens pairs old verdicts
  with new findings.
- **AC6** — When all four lens stubs return null, the harness returns `exit: 'deferred-platform'`,
  `blockers: null`, and a `pending` list naming the four `find:` labels; when two lens stubs return
  null and the survivors find nothing, it returns `deferred-platform` with those two labels pending;
  and when one lens stub returns null and every finding is refuted by its skeptics, it returns
  `deferred-platform` too.
  Red when: any of the three paths returns `exit: 'complete'` or a note beginning `clean` or
  `partial`, so the unattended adapter records a review round over a partial fan as clean.
- **AC7** — When one skeptic batch stub returns null, and separately when the synthesis stub returns
  null, each run returns `deferred-platform` with the dead label in `pending`, and no synthesis runs
  after a dead batch.
  Red when: the BASE `PARTIAL` path survives, returning an integer `blockers` over a half-judged set.
- **AC8** — When `bash tools/workflows/unattended-build.test.sh` feeds its `workflow` double a
  deferred return, the harness returns `exit: 'deferred-platform'` naming the Audit stage and the
  pending labels, the trace holds no `audit:record` agent, and nothing throws.
  Red when: the non-integer blocker refusal fires first and the run dies reading DEGRADED.
  cost: seconds, run by hand, since no bar runs this suite at BASE.
- **AC9** — When `unattended.sh --hold <slug> ... --pending-run wf_0a1b2c3d-4e5` runs in a scratch
  fixture repo, `--status` prints `pending run wf_0a1b2c3d-4e5` in the checkpoint block, and a
  `--resume` take-over of that record prints the relaunch line naming `wf_0a1b2c3d-4e5`; after a
  resume and a second `--hold` with no flag, the checkpoint prints no pending run.
  Red when: the fact survives the second hold, so a checkpoint names a run from an earlier stop; or
  the take-over never prints the relaunch, so the recorded runId is written and never used.
  permission: this unit may not run the unattended suites; the arm is written, and the case is
  observed by running the verb itself in the fixture, D12-h's method (b).
- **AC10** — When `--pending-run` carries ` · ` or a newline, `--hold` refuses with a numbered
  message and the run-state file is byte-unchanged.
  Red when: the value is accepted, and the separator forges a second fact or row.
- **AC11** — When `bash tools/workflows/check-protocol-parity.test.sh` and
  `bash tools/unattended/adopt-unattended.sh --check` run, the rendered review protocol matches its
  template with the durability rule in it, and the Skill names `--pending-run`.
  Red when: the template changes and the dogfood render is left behind.
- **AC12** — When this build's closing diff review runs through the rebuilt harness, the key
  directory under `git rev-parse --git-common-dir` holds one `find-<lens>.json` per lens that
  returned, each carrying the key the run computed.
  Red when: the directory is empty after lenses returned, which means the write instruction is
  ignored and S1's schema field is satisfied by a path to nothing.
  cost: nothing beyond the closing review, which runs anyway. fixture: none exists until then.
- **AC13** — When `tools/workflows/tier2-review.js` is read with `git show` at this unit's build
  commit, the line carrying `version: '` reads 1.8 as `meta.version`, in the `gov:kit tier2-review@`
  marker and in the `gov:kit review-harness@` marker, the one move unit 21 makes over BASE's 1.7;
  when `git diff HEAD^ HEAD -- tools/workflows/tier2-review.js` runs on that commit, no removed or
  added line carries `version: '`; and `bash tools/check-kit-versions.sh` exits 0.
  Red when: a kit's shipped bytes move and its marker is left behind; or this unit moves the review
  harness a second time in the landing range, so the line reads past 1.8, which
  `tools/check-kit-versions.sh` cannot see, because it grades only that the three tokens agree and
  a second move keeps them agreeing.
  permission: the reads are `git show` and `git diff` observations in the pass;
  `check-kit-versions.sh` is the `kit version markers` leg and runs at the build's one post-build
  bar.

## 7. Gates

`tier2-review self-test` · `workflow script syntax` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `review-protocol parity (kit vs dogfood)` · `unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/workflows/tier2-review.test.sh` · a whole-script stub run with dead lens, skeptic and synthesis stubs, a probe return carrying files under a mismatched key · the suite's assertion floor, raised by the new arms
New arm: `tools/workflows/unattended-build.test.sh` · a `workflow` double returning a deferred result · none, the suite is on no bar
New arm: `tools/unattended/unattended.test.sh` · `--hold --pending-run` with a separator in the value · none, the suite is not run in this unit

## 8. Open questions

- **F1** — Which deaths defer? Options: (a) only every lens dead, as DR's second criterion reads;
  (b) any agent returning null. (a) keeps the BASE `PARTIAL` path, which records a round over a
  half-judged set, and leaves DR's first criterion, a re-run after two deaths, with no reason to
  happen. RESOLVED (agent, 2026-09-14, delegated): (b), which satisfies both of DR's criteria and
  is cheap because a re-run pays only for what died.
- **F2** — Where the files live. Options: the build's `reviews/` folder; a scratch path in the
  worktree; the git common dir. The first reds check 5 when tracked, the second is per worktree and
  one `git add` from being committed. RESOLVED (agent, 2026-09-14, delegated): the git common dir.
- **F3** — Do skeptic batches get reused, or only lenses? DR's text reuses lenses and has skeptics
  write. RESOLVED (agent, 2026-09-14, delegated): reuse both, keyed by the batch fingerprint. It is
  the more feature-rich option, and without it a dead synthesis re-runs every skeptic.
- **F4** — How the runId reaches the record. Options: a new verb; a flag on `--review`; a flag on
  unit 4's `--hold`. A deferred run has no verdict or blocker count, which `--review` requires, and
  the stop that needs a runId later is exactly the one that holds. RESOLVED (agent, 2026-09-14,
  delegated): `--hold --pending-run`.
- **F5 — how is a ref-valued diff base keyed?** Options: (a) the probe resolves `base` to a sha like
  `head`, and the key and every prompt name it; (b) reuse is refused whenever `base` is not a pinned
  hex id. (b) disables reuse for the harness's own default, `origin/main`. RESOLVED (agent,
  2026-09-14, delegated): (a), which also pins every diff review to an immutable base.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.
- rev-2 · 2026-09-14 · folds the round-1 spec audit (G4 M10, M26, M27, L5, M7; G1 M11). M10: S2
  and S3 have the probe resolve the diff base too, and the key and prompts name the sha (F5). M26:
  AC3 stages every key component. M27: AC6 stages both partial-death exits. L5: AC9 observes the
  take-over's relaunch line. M7 with G1 M11: S8 moves the review harness only; the unattended move
  is unit 1's, and AC13 keeps its review-harness half.
- rev-3 · 2026-09-16 · spec-audit round 2 fold, third pass. The fold-2 verifier problem that §2 S8
  still claimed the review harness's move as the first unit to scope it, decided by the orchestrator
  as the first-to-change rule: unit 21 S6 changes that kit's descriptor at order 21, so unit 21 S8
  owns the move. §2 S8 drops the move and says this unit's review-harness bytes ride unit 21's. §6
  AC13 keeps its 1.8 read, one move over BASE's 1.7; its `Red when:` also reds a second move by this
  unit, and a permission line places its leg at the build's one post-build bar. Fold verification:
  `tools/check-kit-versions.sh` grades only that the three version tokens agree, so it could see
  neither the 1.8 value nor a second move; §6 AC13 now reads the version line with `git show` at the
  build commit and with `git diff HEAD^ HEAD`, as unit 21's AC8 reads its own moves.

## 10. Reuse audit

The seams are the harness's own. The dead-agent counting in `tools/workflows/tier2-review.js`
(`lensesDead`, `skepticsDead`, the null-never-zero `blockers`) is what S5 generalises into an exit
field. The whole-script AsyncFunction runner in `tools/workflows/unattended-build.test.sh` is the
test seam the new arms reuse, and today's `tier2-review.test.sh` extracts only the prelude.
`unattended-build.js`'s non-integer refusal at `:587-593` is where S6 inserts its branch. Unit 4's
`--hold` fact writer is where S7's fact goes. `python tools/codebase-map/reuse_lookup.py "persist
review lens output to disk before returning and skip completed lenses on re-run"` returned name-stem
neighbours only, `run`, `skip`, `REVIEW-PROTOCOL.md` and the `agent-cap` seam among them, and it
reports `.sh` as an unscanned layer; no existing seam persists or reuses a lens result. Recall
returned `aFusedCharter/RUN.md:26`, a park naming `resumeFromRunId` for a tier2 review none of whose
lenses had completed, and `aProvenReuse`'s spec-audit record derived from a run journal after its
synthesis died: two measured cases of exactly this stop. It also returned `TOOL-dTieredTribunal-16`,
whose defect the RUN INTEGRITY block at `tools/workflows/tier2-review.js:507-526` already answers in
the source; this unit leaves that row to its owner.

Where DR and the source disagree at BASE: DR's criteria speak of five lenses, and the harness runs
four per kind, so every criterion here counts four. M12's candidates and the test that rejected each
are in §4, Alternatives rejected.

Recall terms used: `tier2-review lens skeptic died workflow fan session limit 529 write before
returning resume runId`
