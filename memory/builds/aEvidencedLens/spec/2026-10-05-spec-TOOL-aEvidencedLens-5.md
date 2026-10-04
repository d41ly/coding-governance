# TOOL-aEvidencedLens-5 — the build harness hands the audit its context, sibling specs, checklist and prior findings

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-5-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-5-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The only automated caller of a spec audit, the Audit stage of
`tools/workflows/unattended-build.template.js`, hands `tier2-review.js` five fields: `kind`, `repo`,
`round`, `reviewDir` and `subjects`. So every lens of an opted-in audit runs with no statement of what
the build is for, no sibling spec to cross-read, no bug-class checklist, no scratch directory to probe
in, and, on a fold round, neither the previous round's findings nor the text it changed. The review
harness already accepts every one of these. This unit makes the caller pass them, and announces each
one it could not produce.

## 2. Scope (IN)

- **S1** — `context`: a string naming `memory/builds/<slug>/README.md` and the run mandate under
  `memory/builds/<slug>/prompts/` (the file whose name carries `run-mandate`; under a run with no
  prompt the README is the mandate), told to the lenses as the two documents to read FIRST. Observed by
  AC1.
- **S2** — `specs`: `memory/TEMPLATE-SPEC.md` first, the format the method says lenses are primed with,
  then every `units[].specPath` of this build that is NOT a subject this round, in roster order, each
  once. A round auditing the whole set therefore passes the format alone. Observed by AC1.
- **S3** — `checklist`: the resolver agent, which already runs `git` per subject, also reads each
  resolved subject's `### Files touched (estimate)` backticked paths, unions them, and runs
  `python {{MEMORY_TREE_DIR}}/gotchas.py --for-paths <paths>` in `repo` under a stated timeout. It
  returns the stdout as `checklist` and the paths as `checklistPaths`, or `checklistError` naming why
  none was produced: no path declared, a non-zero exit, or the timeout. The command is a new constant
  carrying the kit path as a render token, as `CHECKLIST` already does. Observed by AC2.
- **S4** — `scratch`: the harness's own folded `scratch` arg, passed through. Observed by AC1.
- **S5** — Fold inputs, two new args. `prevSubjects` is an array of `{path, blob}` with a 7 to 40 hex
  blob; `priorFindings` is an array of objects. On a FOLD re-invoke, a callee round above 1, each
  subject whose path matches a `prevSubjects` entry carries `prevBlob` set to that entry's blob, and
  `priorFindings` is passed through. A subject that already carries a `prevBlob` keeps it. Observed by
  AC4.
- **S6** — Malformed `prevSubjects` or `priorFindings` throws `unattended-build: …` naming the field,
  the legal shape and what was given, before any agent spawns. Either one present when the callee round
  is 1, a fresh generation with no previous round, throws naming that. Observed by AC6.
- **S7** — The CONVERGING return carries `prevSubjects`, the `{path, blob}` set this round pinned, and
  `priorFindings`, the callee's `confirmedFindings`, and its `nextAction` names both as the args to
  copy back beside `round` and `subjectRound`. Observed by AC7.
- **S8** — Every input the harness could not produce is ANNOUNCED with a `log('WARNING: …')` line and
  never passed as an empty value: no checklist (with the resolver's reason, or because a caller-pinned
  `subjects` skipped the resolver); a fold re-invoke without `prevSubjects` or `priorFindings`, which
  the callee then runs as a degraded fold review; a callee return with no `confirmedFindings` array on
  the CONVERGING path. Observed by AC3, AC5 and AC7.
- **S9** — The `args` header block documents `prevSubjects` and `priorFindings`, and the meta `Audit`
  phase detail names the inputs the stage passes. Observed by AC8.
- **S10** — `tools/workflows/unattended-build.test.sh` gains arms for S1 to S8 and keeps the arm
  pinning the stripped `{path, blob}` subject shape, which a round-1 audit still meets. NOT OBSERVED
  inside the pass, because shared invariant 9 keeps suites out of passes; §7 declares the arms.

## 3. Non-goals (OUT)

- Anything inside `tools/workflows/tier2-review.template.js`. The review harness's `scratch` and
  `prevBlob` contracts are `TOOL-aEvidencedLens-2`'s and `TOOL-aEvidencedLens-4`'s.
- The DISPOSAL stage and `writeRound`'s counts. `TOOL-aEvidencedLens-8` owns them, in this file, after
  this unit by order; it rewrites the CONVERGING return's fold sentence, and this unit adds only the
  two copy-back args to it.
- A `byDesign` or `lensNotes` input. No source in the build folder states either, and the review
  harness already announces their absence.
- Pinning a checklist when a caller supplies `subjects`. That caller has pinned the blobs itself and
  skips the resolver; the absence is announced (S8), and a caller wanting a checklist lets the
  resolver run.
- A kit version bump. The main loop bumps once at the close (shared invariant 7).

### Edges

- **consumes-from** `TOOL-aEvidencedLens-2` — the review harness's `scratch` arg, REQUIRED on a spec
  audit after that unit; without this unit the build harness's audit is refused there.
- **consumes-from** `TOOL-aEvidencedLens-4` — a spec subject's `prevBlob`, which the review harness
  validates and reads at a fold round; without it S5's field is an unread key.

## 4. Design

### Evidence

Read at base `028b5cac`, which is `origin/main` at preflight; the run branch's later commits touch only
`memory/builds/aEvidencedLens/`.

- The Audit stage's call at `tools/workflows/unattended-build.template.js:840` to `:854` passes
  `kind`, `repo`, `round`, `reviewDir` and `subjects`, nothing else.
- `tools/workflows/tier2-review.template.js` reads `context` (`:158`, defaulting to "the spec set under
  audit"), `specs` (`:231`, refusing a path that is absolute, home-relative, drive-lettered,
  backslashed, carrying `..` or a control character, and, on a spec audit, one that is also a subject,
  `:242`), `checklist` (`:250`, a string of `- ` items, which `gotchas.py`'s output is) and
  `priorFindings` (`:166`). Each absence is logged as a WARNING by the review harness itself.
- The resolver agent at `:778` runs `git rev-parse HEAD:<specPath>` and `git hash-object <specPath>`;
  `SUBJECTS_SCHEMA` at `:435` requires only `subjects`.
- The harness already folds `scratch` at `:225` and spells `{{MEMORY_TREE_DIR}}` in `CHECKLIST` at
  `:361`.
- `python tools/memory-tree/gotchas.py --for-paths tools/workflows/unattended-build.template.js` printed
  a `#`-prefixed preamble and nine `- [ ] <class>` items with continuation lines and exited 0,
  measured 2026-10-05; `parseChecklist` reads the `#` lines as preamble and each `- ` line as an item.
- The CONVERGING return at `:1124` carries `subjectRound` and `auditIds` back for the caller to copy,
  and its `nextAction` at `:1150` names them. That is the precedent S7 follows.
- The review harness returns `confirmedFindings` in the shape `priorFindings` reads, on every exit
  (`tools/workflows/tier2-review.template.js:1051`).
- `units[].specPath` arrives from `--plan`, repo-relative.

### Data model

```js
// the Audit stage's call after this unit
{ kind: 'spec-audit', repo, round: roundNo - subjectRound + 1, reviewDir, scratch,
  subjects: [{ path, blob, prevBlob? }],                 // prevBlob only on a fold re-invoke
  context: 'Build <slug>: read memory/builds/<slug>/README.md and the run mandate under ' +
           'memory/builds/<slug>/prompts/ FIRST …',
  specs: ['memory/TEMPLATE-SPEC.md', /* sibling specPaths not in subjects */],
  checklist?: '<gotchas.py --for-paths stdout>',        // absent, and announced, when none
  priorFindings?: [ /* the previous round's confirmedFindings */ ] }
```

```js
// SUBJECTS_SCHEMA, the resolver's return, gains three OPTIONAL properties
{ subjects: [...], checklist: '<stdout>', checklistPaths: ['<path>', ...], checklistError: '<why>' }
```

### Inventory

| Name | Cell | Kind |
|---|---|---|
| `AUDIT_CHECKLIST` | none: `.lexicon.conf` declares no JavaScript constant cell | new constant, the `--for-paths` command with its render token |
| `prevSubjects` | args field and CONVERGING return field | new |
| `priorFindings` | args field and CONVERGING return field | new on this harness |

No new function.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`

The render is regenerated by the parity tool's `--render` form in the same commit, never hand-edited
(shared invariant 1).

### Alternatives rejected

- **The script composing the checklist command for the caller to run.** A workflow script has no
  shell; the resolver agent already runs commands per subject and is the one actor that can.
- **`--for-diff` over the subjects.** A spec audit precedes the code; there is no diff, and the
  subjects' declared files are the paths the build will touch.
- **Deriving `prevBlob` from `git log` inside the resolver.** The previous round's pin is a fact the
  previous invocation HELD; recomputing it from history guesses which commit the last audit read,
  which the hand-back makes unnecessary, as `subjectRound` does.

## 5. Production-readiness checklist

- security — every path reaching the callee is validated there (`specs`), and the resolver's
  `gotchas.py` run is read-only and bounded; `context` carries two fixed repo paths and the slug,
  which `check_slug`'s grammar already constrains at the driver.
- perf / scale — one extra bounded command inside an agent that already runs; no new agent.
- error / empty / loading states — every input that could not be produced is a WARNING (S8); a
  malformed fold arg is a throw before any spawn (S6).
- observability — the WARNING lines, and the callee's RUN INTEGRITY block, which names what it received.
- risks — the new inputs change the callee's review key, so a re-run after this lands reuses no lens
  file written before it; that is the key doing its job.
- testing — stub runs of the render (§6); the suite arms run once at `VERIFYING`.
- migration — none: a caller passing neither new arg gets today's behaviour plus the announcements.
- user docs — the `args` header block and the CONVERGING return's `nextAction` (S7, S9).

## 6. Acceptance criteria

Every stub-run criterion below evaluates the RENDER `tools/workflows/unattended-build.js` with `node`,
in the `run_wf` AsyncFunction shape of the build harness's self-test, copied into a scratch script
under the run's scratch directory and run there, never by running the suite. Inputs use that file's
`UNITS` args (subjects `s1` and `s2`, units with specs `s1`, `s2` and `s3`) and its `returns`,
`review_out` and `rec` doubles; the `wargs:` trace line is the callee's args.

- **AC1** — When the stub runs `UNITS` at round 1 with `returns CONVERGED 0`, the `wargs:` line carries
  `"scratch":"/tmp/s"`, a `context` containing the fixture build's README path, "memory/builds/tB/README.md",
  and its prompts directory, and `"specs":["memory/TEMPLATE-SPEC.md","s3"]`.
  Red when: any of the four is absent, or a subject appears in `specs`.
- **AC2** — When the args omit `subjects` and the `audit:subjects` double returns one subject and a
  `checklist` of two `- ` items, the `wargs:` line carries that `checklist` verbatim, and the traced
  `prompt:audit:subjects:` line names `gotchas.py --for-paths` and `Files touched (estimate)`.
  Red when: the resolver is not asked for the checklist, or its answer does not reach the callee.
- **AC3** — When that double returns `checklistError` instead, the trace logs a `WARNING` naming it
  and the `wargs:` line carries no `checklist` key; when `subjects` is supplied, the trace logs a
  `WARNING` saying no resolver ran.
  Red when: an absent checklist is passed as `""` or goes unannounced.
- **AC4** — When the stub runs round 3, `subjectRound` 2, with
  `"prevSubjects":[{"path":"s1","blob":"1234abc"}]` and a one-entry `priorFindings`, the `wargs:` line
  carries `{"path":"s1","blob":"abc1234","prevBlob":"1234abc"}`, `s2` with no `prevBlob`, and the
  `priorFindings` entry.
  Red when: the previous pin does not reach its subject, or reaches the wrong one.
- **AC5** — When the stub runs round 3, `subjectRound` 2, with neither fold arg, it does not throw,
  logs a `WARNING` naming a degraded fold review, and the `wargs:` line carries no `prevBlob` and no
  `priorFindings`.
  Red when: the fold re-invoke throws, or runs silently undegraded.
- **AC6** — When `prevSubjects` carries `{"path":"s1","blob":"xyz"}`, the stub THROWS naming
  `prevSubjects` and the 7 to 40 hex rule; when `priorFindings` is a string, it throws naming
  `priorFindings`; when either is given at round 1, it throws naming the fresh generation; and in each
  case the trace holds no `workflow:` line.
  Red when: a malformed or misplaced fold arg reaches the callee.
- **AC7** — When the stub runs `returns CONVERGING 3` with a `workflow`
  double carrying a one-entry `confirmedFindings`, the RESULT carries `prevSubjects` equal to the
  pinned `{path, blob}` set and `priorFindings` equal to that entry, and `nextAction` names
  `prevSubjects` and `priorFindings`; with the double's `confirmedFindings` absent, the trace logs a
  `WARNING` and the RESULT carries `"priorFindings":[]`.
  Red when: the hand-back is missing, or a missing callee field is silent.
- **AC8** — When `node tools/workflows/check-workflow-syntax.js` runs after the render it exits 0;
  `grep -c "gotchas.py --for-paths" tools/workflows/unattended-build.js` prints a non-zero count with
  no `{{` left on that line; and `grep -n "prevSubjects" tools/workflows/unattended-build.template.js`
  shows the field in the `args` header block.
  Red when: the render was not regenerated, the token survived, or the header omits a field the file
  reads.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `review-join self-test` · `verifier fan-out self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · the base harness, whose audit call carries no `context`, `specs`, `checklist` or `scratch` · none
New arm: tools/workflows/unattended-build.test.sh · a fold re-invoke with `prevSubjects`, which the base harness ignores · none
New arm: tools/workflows/unattended-build.test.sh · a malformed `prevSubjects`, which the base harness passes through unread · none

## 8. Open questions

- **F1 — Where does the previous round's pin and confirmed set travel between invocations?** Options:
  (a) on the CONVERGING return, copied back by the caller, as `subjectRound` already travels; (b)
  re-derived by the resolver from history; (c) read from the review record on disk. (b) guesses which
  commit the last audit read; (c) depends on the synthesis agent having written the appendix and the
  pin line, which nothing verifies.
  RESOLVED (agent, 2026-10-05, delegated): (a), S5 to S7, the brief's recommendation.
- **F2 — Where is the checklist produced?** The script has no shell; the resolver agent runs commands
  already. A separate agent would cost a spawn for one command.
  RESOLVED (agent, 2026-10-05, delegated): the resolver, S3.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the spec brief's unit 5 and both templates read at
  `028b5cac`.

## 10. Reuse audit

No new seam. Every input is one `tools/workflows/tier2-review.template.js` already reads and validates
(`context`, `specs`, `checklist`, `priorFindings`, and after units 2 and 4 `scratch` and `prevBlob`);
the checklist is `gotchas.py --for-paths`, the existing no-diff mode of the memory-tree kit's
bug-class tool; the resolver agent and the CONVERGING hand-back, which already carries `subjectRound`,
are extended in place. `python tools/codebase-map/reuse_lookup.py "hand the spec audit its context,
sibling specs, bug-class checklist and the previous round's findings"` returned only name-stem
neighbours (`parse_spec_h1`, `target_context`), none a caller of the review harness, and the lookup
does not scan JavaScript workflow templates as callers. The recall query returned
`TOOL-dRetiredFork-22` and `TOOL-dRetiredFork-41`, which moved this stage's spawn to the script and
explain why only the resolver agent can run a command here, and `TOOL-aSightedSkeptic-3`, which built
the `specs` validation this unit's sibling list must pass.

Recall terms used: `python tools/memory-recall/query.py "what does the build harness pass to the spec audit sub-workflow, and why is the context empty" --terms "unattended-build Audit stage tier2-review subjects specs checklist context priorFindings subjectRound resolver gotchas"`
