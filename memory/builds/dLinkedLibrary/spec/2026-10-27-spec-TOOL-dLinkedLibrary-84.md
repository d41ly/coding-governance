# TOOL-dLinkedLibrary-84 — the CI census runs the indirection test over every GitLab top-level block that reaches every job, and reads the global script keys

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 25 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |
| [2026-10-27-build-TOOL-dLinkedLibrary-84-deviation-841.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-84-deviation-841.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-86 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 75 to 80
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md`) confirmed
finding **id 33 at HIGH**, report item **H3**. No other id shares the item; id 5, item M5, binds the same
defect at MEDIUM and is an item of the minors batch `TOOL-dLinkedLibrary-86`.

`TOOL-dLinkedLibrary-76` S1 limits the indirection test to a job's keys plus `default:`. GitLab applies
other top-level blocks to every job: the top-level `variables:`, the `variables:` a `workflow:` rule sets,
and the deprecated but still honoured global `image:`, `services:`, `cache:`, `before_script:` and
`after_script:`. `TOOL-dLinkedLibrary-79` reads the top-level `variables:` for credential names only, and
no spec runs the `!reference`, alias or merge test over any of them, or says how the global script keys
are read. So `variables: *creds`, with `TWINE_PASSWORD: $PYPI_TOKEN` behind an anchor in a hidden job,
puts no credential name in any block 79 reads and a `./release.sh` job grades `importable`; and a
top-level `before_script: [npm publish]` injects a publish into every job unread.

This unit names the class, every top-level block that reaches every job, runs the test over each, and
reads the global script keys as `default:`'s are read. It repairs `TOOL-dLinkedLibrary-76` and builds
one step after it (order 25).

## 2. Scope (IN)

- **S1** — The class. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, the job-wide top-level
  blocks of a `.gitlab-ci.yml` are `default:`, `variables:`, `workflow:`, `image:`, `services:`, `cache:`,
  `before_script:` and `after_script:`. None is a job, and none has a census row of its own, as 76 S2
  states for `default:`. Observed by AC4.
- **S2** — The test over each. 76 S1's indirection test, reading each line's whole value as
  `TOOL-dLinkedLibrary-83` S1 states, runs over each block of S1 other than `default:`, from its own line
  to its last line. A hit refuses every job in the file through 76 S2's file-wide path, each reading
  `refused: opaque step <key> <block>:<child>`, `<block>` the top-level key and `<child>` as 83 S2 defines
  it, so `variables: *creds` reads `refused: opaque step alias variables:`. Observed by AC1 and AC3.
- **S3** — The global script keys. The lines of a top-level `before_script:` and `after_script:` are
  applied to every job as `TOOL-dLinkedLibrary-63` S1 applies `default:`'s same keys, so unit 51's
  normalisation and refusal list run over them for each job. Observed by AC2.
- **S4** — What stays readable. A block of S1 holding none of the tokens leaves its plain jobs graded as
  63 S1 to S3 and 79 state. Observed by AC4.
- **S5** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch tree of
  its own with two plain jobs, `release` running `./release.sh` before the block and `test` running `npm
  test` after it: `variables: *creds` following a hidden `.creds: &creds` that maps `TWINE_PASSWORD:
  $PYPI_TOKEN`, the anchor first as YAML requires; a top-level `before_script: [npm publish]`; a `workflow:` whose `rules:` item holds
  `variables: !reference [.vars, variables]`; and a top-level `image: node:20` with `variables:` mapping
  only `NODE_ENV: test`. Observed by AC1 to AC4.

## 3. Non-goals (OUT)

- The reading of a block's own line and its flow value: `TOOL-dLinkedLibrary-83` (id 32), which this
  unit applies.
- The top-level `include:`: `TOOL-dLinkedLibrary-71` S2, unchanged.
- Credential names in the top-level `variables:` and `default:`: `TOOL-dLinkedLibrary-79`, unchanged.
- An `after_script:` plant and the page sentence naming the global script keys: the minors batch
  `TOOL-dLinkedLibrary-86`, its item for id 5.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-76` — S1's indirection test, S2's file-wide refusal and S3's application of `default:`'s script lines, which S2 and S3 run over every other job-wide top-level block (id 33)
- **consumes-from** `TOOL-dLinkedLibrary-83` — S1's whole-value reading of a block's own line and S2's `<child>`, which S2 applies to each block of S1 (id 33)
- **hands-off** `TOOL-dLinkedLibrary-86` — S3's global `after_script:` reading, which unit 86 plants, and the census page's sentence naming the global script keys, which unit 86 writes (id 5)
- **hands-off** `TOOL-dLinkedLibrary-89` — S1's class of job-wide blocks and S2's file-wide refusal path, which unit 89 extends to GitLab's `spec:` header and an `inputs` interpolation (id 30)
- **hands-off** `TOOL-dLinkedLibrary-90` — S3's global `before_script:` reading, which unit 90's BOM-led GitLab plant grades through (id 33)
- **hands-off** `TOOL-dLinkedLibrary-91` — S2's reason and seam, S5's plants, AC3, AC4, its order after 83 and §4's 79 cite, which unit 91's S6, S11 to S15 and S30 settle and plant at this unit's pass (ids 14, 24, 3, 32, 19, 12, 17)

## 4. Design

### Evidence

- 76 S1 (`2026-10-27-spec-TOOL-dLinkedLibrary-76.md:34-36`) tests "the job's own keys and the top-level
  `default:` map".
- 79 S1's GitLab row (`2026-10-27-spec-TOOL-dLinkedLibrary-79.md:42`) reads the top-level `variables:` and
  `default:` for credential names; 79 §3 hands indirection under `default:` alone to 76.
- 63 S1's GitLab row lists `script`, `before_script`, `after_script` and `default:`'s same three; no spec
  names the global `before_script:` or `after_script:`.
- GitLab's CI keyword reference lists `default`, `include`, `stages`, `variables` and `workflow` as global
  keywords, `workflow:rules:variables` as variables for the whole pipeline, and the globally defined
  `image`, `services`, `cache`, `before_script` and `after_script` as deprecated but still applied to
  every job.

### A GitLab file after S2 and S3

```yaml
.creds: &creds
  TWINE_PASSWORD: $PYPI_TOKEN
release:
  script: ./release.sh        # S2: refused, opaque step alias variables:
variables: *creds
test:
  script: [npm test]          # S2: refused, the same reading
```

### Rollout

Order 25 beside `TOOL-dLinkedLibrary-83` and `TOOL-dLinkedLibrary-85`. All three write
`adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences them, and this unit consumes 83's reading,
so its pass follows 83's.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S5

### Alternatives rejected

- **Adding `variables:` alone beside `default:`.** It closes the instance the finding names and leaves
  `workflow:` and the global keys, which reach every job the same way.
- **Reading `stages:` as a job-wide block.** It lists stage names and supplies no text or value a job
  runs, so an alias there injects nothing.

## 5. Production-readiness checklist

- security — closes the import of a job whose text or credentials arrive by an indirection in a
  job-wide top-level block, or by a global script key; deny by default.
- perf / scale — each top-level block walked once per file.
- error / empty / loading states — unchanged from 63 and 76.
- observability — each refusal names the key and the block holding it.
- risks — a file using an alias in its top-level `variables:` for harmless values refuses every job; the
  owner may rule a job in.
- testing — S5's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — the census page's sentence naming the global keys is unit 86's item for id 5; 76 S5's
  sentence covers `default:`.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both plain jobs
  of the tree holding `variables: *creds` read `refused: opaque step alias variables:`.
  Red when: 76's `default:`-only test leaves an alias in the top-level `variables:` unread.
- **AC2** — When the same plant runs, both plain jobs of the tree holding a top-level `before_script: [npm
  publish]` read `refused: npm publish`.
  Red when: a global script key's line reaches no job.
- **AC3** — When the same plant runs, both plain jobs of the tree whose `workflow:` rule holds `variables:
  !reference [.vars, variables]` read `refused: opaque step !reference workflow:variables`.
  Red when: an indirection in a `workflow:` rule passes.
- **AC4** — When the same plant runs, both plain jobs of the tree holding `image: node:20` and `NODE_ENV:
  test` read `importable`, and no tree has a census row named `variables`, `workflow`, `image` or
  `before_script`.
  Red when: a job-wide block without a token refuses its jobs, or is graded as a job.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC4 · the `ci-census` plant's four job-wide top-level trees, the failing case staged by 76's `default:`-only test and 63's job-only script keys · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 75 to 80, id 33 (HIGH, item
  H3).
- rev-2 · 2026-10-27 · §3 · the hands-off edges to units 89, 90 and 91, the mirrors of the consumes-from
  edges their specs declare, promoted from the spec audit of units 81 to 86; no scope or criterion moved.

## 10. Reuse audit

The seam extended is 76 S1's indirection test and S2's file-wide refusal, as 83 widens the line read,
with 63 S1's application of `default:`'s script keys reused for the global ones, all inside
`TOOL-dLinkedLibrary-8`'s `ci-job` class in `tools/memory-tree/adopt_program.py`. `python
tools/codebase-map/reuse_lookup.py "run the indirection test over every gitlab top level block applied to
every job"` ranked `run`, `run_git`, `run_arms` and `extract_run_facts`, none a CI reader, so no existing
seam fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how does a census refuse an indirection on the default line or a global gitlab block" --terms "census ci-job gitlab default flow alias reference merge-key global before_script variables refused"`
