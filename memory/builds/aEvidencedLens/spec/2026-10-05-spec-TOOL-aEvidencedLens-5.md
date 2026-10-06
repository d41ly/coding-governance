# TOOL-aEvidencedLens-5 — the build harness hands the audit its context, sibling specs, checklist and prior findings

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 6 · ratified 2026-10-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-aEvidencedLens-1-runlog-696fbe29.md](../build/2026-10-05-build-TOOL-aEvidencedLens-1-runlog-696fbe29.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14 TOOL-aEvidencedLens-15 TOOL-aEvidencedLens-18 TOOL-aEvidencedLens-19 TOOL-aEvidencedLens-20 TOOL-aEvidencedLens-21 |
| [2026-10-05-build-TOOL-aEvidencedLens-5-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-aEvidencedLens-5-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-5-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-5-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md) | diff-review | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14 TOOL-aEvidencedLens-15 TOOL-aEvidencedLens-18 TOOL-aEvidencedLens-19 TOOL-aEvidencedLens-20 |
| [2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |

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
  the harness's `briefDir` const (the file whose name carries `run-mandate`; under a run with no
  prompt the README is the mandate), told to the lenses as the two documents to read FIRST. The
  mandate directory is composed from `briefDir`, never re-spelled, so a caller passing another
  `briefDir` sends the lenses where the mandate is. Observed by AC1.
- **S2** — `specs`: `memory/TEMPLATE-SPEC.md` first, the format the method says lenses are primed with,
  then every `units[].specPath` of this build that is a non-empty string and is NOT a subject this
  round, in roster order, each once. The non-empty filter runs BEFORE the subject exclusion, because
  the harness carries an empty `specPath` for every unit its spec stage just authored, and the callee
  refuses an empty `specs` member before any lens. A round auditing the whole set therefore passes the
  format alone. Observed by AC1 and AC9.
- **S3** — `checklist`: the resolver agent, which already runs `git` per subject, also reads each
  resolved subject's `### Files touched (estimate)` backticked paths, unions them, and runs
  `python {{MEMORY_TREE_DIR}}/gotchas.py --for-paths <paths>` in `repo` under a stated timeout. It
  returns the stdout as `checklist` and the paths as `checklistPaths`, or `checklistError` naming why
  none was produced: no path declared, a non-zero exit, the timeout, or a stdout carrying no line that
  starts `- `, which `gotchas.py` prints with exit 0 when no class is selected and which the callee's
  `parseChecklist` refuses. The last reads `no bug class selected`. The command is a new constant
  carrying the kit path as a render token, as `CHECKLIST` already does. Observed by AC2 and AC3.
- **S4** — `scratch`: the harness's own folded `scratch` arg, passed through. The harness's own
  `scratch` validation also applies the callee's two extra refusals, a control character and a value
  equal to or under `repo` after the same fold, lowercasing and trailing-slash drop
  `TOOL-aEvidencedLens-2` §4 "The argument" states, throwing `unattended-build: …` naming `scratch`
  before any stage. A scratch the callee would refuse therefore dies at this harness's prelude and not
  after the spec stage and the resolver have spent their work. Observed by AC1 and AC10.
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
  copy back beside `round` and `subjectRound`. When the callee returned no `confirmedFindings` array,
  `priorFindings` is OMITTED from the return rather than carried as `[]`, so a copied-back value never
  reaches the next invoke as an empty one. Observed by AC7.
- **S8** — Every input the harness could not produce is ANNOUNCED with a `log('WARNING: …')` line and
  never passed as an empty value: no checklist (with the resolver's reason, or because a caller-pinned
  `subjects` skipped the resolver); a fold re-invoke without `prevSubjects`, which the callee runs as a
  whole-file review of each subject; a fold re-invoke without `priorFindings`, which the callee runs
  with no prior findings and says so; a fold re-invoke without both, which the callee runs as a
  degraded fold review, the wording `TOOL-aEvidencedLens-4` S3 uses; a callee return with no
  `confirmedFindings` array on the CONVERGING path. Each WARNING names the field it lacks. Observed by
  AC3, AC5 and AC7.
- **S9** — The `args` header block documents `prevSubjects` and `priorFindings`, and the meta `Audit`
  phase detail names the inputs the stage passes: `context`, `specs`, `checklist` and `scratch`.
  Observed by AC8.
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
  audit after that unit, and its two extra refusals, which S4 applies at this harness's prelude too;
  without this unit the build harness's audit is refused there.
- **consumes-from** `TOOL-aEvidencedLens-4` — a spec subject's `prevBlob`, which the review harness
  validates and reads at a fold round; without it S5's field is an unread key.
- **hands-off** `TOOL-aEvidencedLens-21` — the closing diff review's batched minors, which amend what this unit built.

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
- `gotchas.py`'s `cmd_for_paths` also exits 0 after printing only its `#` header lines when no class
  is selected, and `parseChecklist` (`tools/workflows/tier2-review.template.js:266-268`) THROWS on a
  non-blank string with no line starting `- `. This repo's universal classes hide the case; an
  adopter meets it. S3 routes it to `checklistError`.
- The harness's own `scratch` refusal (`:218-225`) is by shape only, while the callee after
  `TOOL-aEvidencedLens-2` also refuses a control character and a value equal to or under `repo`.
- The CONVERGING return at `:1124` carries `subjectRound` and `auditIds` back for the caller to copy,
  and its `nextAction` at `:1150` names them. That is the precedent S7 follows.
- The review harness returns `confirmedFindings` in the shape `priorFindings` reads, on every exit
  (`tools/workflows/tier2-review.template.js:1051`).
- `units[].specPath` arrives from `--plan`, repo-relative, and IS EMPTY for every unit the spec
  stage just authored (`tools/workflows/unattended-build.template.js:1534`; `:1572` carries
  `u.specPath || ''`). The callee refuses an empty or non-string `specs` member before any lens
  (`tools/workflows/tier2-review.template.js:235-240`), so S2 filters it.
- `briefDir` is a const, `a.briefDir || 'memory/builds/' + slug + '/prompts'` (`:230`), already
  handed to `renderRoster`; S1 composes `context` from it.

### Data model

```js
// the Audit stage's call after this unit
{ kind: 'spec-audit', repo, round: roundNo - subjectRound + 1, reviewDir, scratch,
  subjects: [{ path, blob, prevBlob? }],                 // prevBlob only on a fold re-invoke
  context: 'Build <slug>: read memory/builds/<slug>/README.md and the run mandate under ' +
           briefDir + '/ FIRST …',
  specs: ['memory/TEMPLATE-SPEC.md', /* non-empty sibling specPaths not in subjects */],
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
  and the `wargs:` line carries no `checklist` key; when the double returns a `checklist` holding
  only two `#` header lines, the trace logs a `WARNING` naming `no bug class selected` and the
  `wargs:` line carries no `checklist` key; when `subjects` is supplied, the trace logs a `WARNING`
  saying no resolver ran.
  Red when: an absent checklist is passed as `""`, a header-only checklist reaches the callee, or
  either goes unannounced.
- **AC4** — When the stub runs round 3, `subjectRound` 2, with
  `"prevSubjects":[{"path":"s1","blob":"1234abc"}]` and a one-entry `priorFindings`, the `wargs:` line
  carries `{"path":"s1","blob":"abc1234","prevBlob":"1234abc"}`, `s2` with no `prevBlob`, and the
  `priorFindings` entry.
  Red when: the previous pin does not reach its subject, or reaches the wrong one.
- **AC5** — When the stub runs round 3, `subjectRound` 2, with neither fold arg, it does not throw,
  logs a `WARNING` naming a degraded fold review, and the `wargs:` line carries no `prevBlob` and no
  `priorFindings`. With `prevSubjects` given and `priorFindings` absent, it logs a `WARNING` naming
  `priorFindings` and not a degraded fold review; with `priorFindings` given and `prevSubjects`
  absent, it logs a `WARNING` naming `prevSubjects` and a whole-file review of each subject.
  Red when: the fold re-invoke throws, runs silently undegraded, or a one-missing case is announced
  as degraded or not at all.
- **AC6** — When `prevSubjects` carries `{"path":"s1","blob":"xyz"}`, the stub THROWS naming
  `prevSubjects` and the 7 to 40 hex rule; when `priorFindings` is a string, it throws naming
  `priorFindings`; when either is given at round 1, it throws naming the fresh generation; and in each
  case the trace holds no `workflow:` line.
  Red when: a malformed or misplaced fold arg reaches the callee.
- **AC7** — When the stub runs `returns CONVERGING 3` with a `workflow`
  double carrying a one-entry `confirmedFindings`, the RESULT carries `prevSubjects` equal to the
  pinned `{path, blob}` set and `priorFindings` equal to that entry, and `nextAction` names
  `prevSubjects` and `priorFindings`; with the double's `confirmedFindings` absent, the trace logs a
  `WARNING` naming `confirmedFindings` and the RESULT carries no `priorFindings` key.
  Red when: the hand-back is missing, a missing callee field is silent, or it is handed back as `[]`.
- **AC8** — When `node tools/workflows/check-workflow-syntax.js` runs after the render it exits 0;
  `grep -c "gotchas.py --for-paths" tools/workflows/unattended-build.js` prints a non-zero count with
  no `{{` left on that line; `grep -n "prevSubjects"` and `grep -n "priorFindings"` over
  `tools/workflows/unattended-build.template.js` each show the field in the `args` header block; and
  the meta `Audit` phase detail names `context`, `specs`, `checklist` and `scratch`.
  Red when: the render was not regenerated, the token survived, the header omits a field the file
  reads, or the phase detail omits an input the stage passes.
- **AC9** — When the stub runs `UNITS` at round 1 with unit `s3`'s `specPath` set to `""` and a
  fourth unit whose `specPath` is absent, the `wargs:` line carries
  `"specs":["memory/TEMPLATE-SPEC.md"]` and a `workflow:` line, and no `THROW` line.
  Red when: an empty `specPath` reaches `specs` and the callee would refuse the audit.
- **AC10** — When the stub runs with `scratch` set to `'/tmp/s\nX'`, to `'/tmp/r/sub'` beside
  `repo: '/tmp/r'`, or to `'C:\\R\\x'` beside `repo: 'c:/r'`, each THROWS a message starting
  `unattended-build:` and naming `scratch`, and the trace holds no `workflow:` line and no spec-stage
  agent; `'/tmp/rs'` beside `repo: '/tmp/r'` proceeds.
  Red when: a scratch the callee refuses passes this harness's prelude.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `review-join self-test` · `verifier fan-out self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · the base harness, whose audit call carries no `context`, `specs`, `checklist` or `scratch`, and passes an empty `specPath` and a header-only checklist through · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/unattended-build.test.sh · a fold re-invoke with `prevSubjects`, which the base harness ignores · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/unattended-build.test.sh · a malformed `prevSubjects`, which the base harness passes through unread, and a scratch under `repo`, which it accepts · `FLOOR_ASSERTIONS` raised by the assertions added

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
- rev-2 · 2026-10-05 · §3 §4 §7 S1 S2 S3 S4 S7 S8 S9 AC3 AC5 AC7 AC8 AC9 AC10 · round-1 spec audit
  fold. Id 38 (MEDIUM): S2 filters an empty `specPath` before the subject exclusion, and AC9
  observes it. Id 39 (MEDIUM): S3 routes a header-only checklist to `checklistError`, and AC3
  observes it. Id 40 (MEDIUM): S4 applies the callee's two extra `scratch` refusals at this
  harness's prelude, AC10 observes them, and the §3 edge to `TOOL-aEvidencedLens-2` names that
  contract. Id 24 (LOW): AC5 adds the one-missing cases and AC8 the `priorFindings` header line and
  the phase detail's four inputs. Id 32 (LOW): S8 names each one-missing case as unit 4 S3 grades it.
  Id 33 (LOW): S7 and AC7 omit `priorFindings` instead of returning `[]`. Id 43 (LOW): S1 composes
  `context` from `briefDir`. Id 30 (LOW, its unit-5 half): §7's arms raise `FLOOR_ASSERTIONS`.
- rev-3 · 2026-10-05 · §3 · the mirror of `TOOL-aEvidencedLens-21`'s consumes-from edge, written by
  the main loop when the closing review's minors were promoted.

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
