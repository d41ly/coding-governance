# TOOL-dLinkedLibrary-71 — the CI census refuses a GitLab job whose text arrives by inheritance or include

**Status:** OPEN · rev-4 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 23 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-71-deviation-711.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-71-deviation-711.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-74 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 54 to 64
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md`) confirmed
finding **id 15 at HIGH**, report item **H5**. Id 40 shares the item and is its own unit,
`TOOL-dLinkedLibrary-72`.

`TOOL-dLinkedLibrary-63` S2's opaque list holds only GitLab `trigger:` or `include:` "inside a job". A
GitLab job also takes its text from elsewhere: job-level `extends:` pulls a hidden job's `script`, a
`!reference` tag splices another job's list, a YAML alias or merge key (`<<: *x`) copies an anchored
map, and a top-level `include:` imports jobs from other files and projects. None is read or refused, so
`release: extends: .publish`, with `npm publish` in the hidden `.publish`, has no line of its own and
reads `importable`. No `.gitlab-ci.yml` is tracked here, so the plants are the whole population.

This unit refuses each GitLab indirection as an opaque step, denying by default as 63's F2 settled. It
repairs `TOOL-dLinkedLibrary-63` and builds one step after it (order 23).

## 2. Scope (IN)

- **S1** — The job-level keys. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, a
  `.gitlab-ci.yml` job carrying `extends:`, any value tagged `!reference`, a YAML alias `*<name>` or a
  merge key `<<:` reads `refused: opaque step <key> <value>`, the key spelled `extends`, `!reference`,
  `alias` or `<<`. Observed by AC1.
- **S2** — The file-level key. A `.gitlab-ci.yml` holding a top-level `include:` refuses every job in the
  file, each reading `refused: opaque step include <value>`, because an included file may define or
  override any job by name. Observed by AC2.
- **S3** — What stays readable. A hidden job, a key opening `.`, is not itself a job the census grades;
  a job using none of S1's keys in a file with no top-level `include:` is graded as 63 S1 to S3 state.
  Observed by AC3.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`: `release` with `extends:
  .publish` whose hidden job runs `npm publish`; a job whose `script:` is `!reference [.publish, script]`;
  a job merging `<<: *publish`; and a second scratch tree whose `.gitlab-ci.yml` holds a top-level
  `include: remote:` and one plain test job. Observed by AC1 and AC2.
- **S5** — The page. `help/adopt.md`'s census section names the GitLab indirection refusals. Observed by
  AC4.

## 3. Non-goals (OUT)

- Azure's indirection keys: `TOOL-dLinkedLibrary-72` (id 40).
- The block-scalar reader: `TOOL-dLinkedLibrary-73` (id 39).
- Resolving a hidden job, an anchor or an included file in-file: the census stays a text reader, as
  63 §3 keeps it.
- GitLab's credential keys: `TOOL-dLinkedLibrary-74`'s item for id 41.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-63` — S2's opaque-step refusal and the `ci-census` plant, which S1 and S2 extend to GitLab's inheritance and include keys (id 15)
- **hands-off** `TOOL-dLinkedLibrary-76` — S1's indirection test, S3's readable set and the `ci-census` plant, which unit 76 extends to `default:` (id 32 of the spec audit of units 65 to 74)
- **hands-off** `TOOL-dLinkedLibrary-80` — S5's page paragraph, which unit 80 completes (id 16 of the spec audit of units 65 to 74)
- **hands-off** `TOOL-dLinkedLibrary-93` — S2's one file-wide refusal function, which unit 93 calls with the `unreadable line break` reason for a file holding a break other than LF (id 21)
- **hands-off** `TOOL-dLinkedLibrary-96` — S1's per-job test and S2's one file-wide function, which unit 96 names as the seams 89 S2 and S3 extend and lists among 91 S17's call sites (ids 3, 15, 20)
- **hands-off** `TOOL-dLinkedLibrary-102` — S2's one file-wide function, which unit 102's S15 routes 79 S3's pipeline-level hit through and its S6 calls first for a line break (ids 2, 19)

## 4. Design

### Evidence

- 63 S2: "A GitLab `trigger:` or `include:` inside a job, and an Azure `task:` or `template:` step … the
  job reads `refused: opaque step <key> <value>`"; 63 F2 resolved deny by default.
- `git ls-files` lists no `.gitlab-ci.yml` at base, so S4's plants are the only population.

### A GitLab file after S1 and S2

```yaml
.publish:
  script: [npm publish]       # hidden: not graded itself
release:
  extends: .publish           # S1: refused, opaque step extends .publish
deploy:
  script: !reference [.publish, script]   # S1: refused, opaque step !reference
```

### Rollout

Order 23 beside `TOOL-dLinkedLibrary-72` and `TOOL-dLinkedLibrary-73`. All three write
`adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences the passes; each owns its own keys and none
reads another's output.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4
- `help/adopt.md`: S5

### Alternatives rejected

- **Resolving `extends:` against hidden jobs in the same file.** It needs merge semantics, anchors and
  `!reference` resolution, a YAML engine's work, and still cannot read an included file.
- **Refusing only jobs whose inherited text holds a publish verb.** The census cannot read the inherited
  text, so that is a guess.

## 5. Production-readiness checklist

- security — closes the import of a publishing GitLab job assembled by inheritance; deny by default.
- perf / scale — one more key test per job line.
- error / empty / loading states — unchanged from 63.
- observability — each refusal names the key and its value.
- risks — a plain test job built with `extends:` is refused; the owner may rule it in, as for any refused
  job.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — `help/adopt.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the `release`
  job reads `refused: opaque step extends .publish`, the `!reference` job and the merge-key job each read
  `refused: opaque step`.
  Red when: a GitLab job whose text is inherited reads `importable`.
- **AC2** — When the same plant runs, the plain test job of the second tree, whose file holds a top-level
  `include:`, reads `refused: opaque step include`.
  Red when: a job in a file that includes others reads `importable`.
- **AC3** — When the same plant runs, 63's GitLab test job, in a file with no indirection, still reads
  `importable`, and the hidden `.publish` job has no census row.
  Red when: the refusal reaches a job using no indirection, or a hidden job is graded.
- **AC4** — When `grep -n "extends\|!reference\|include"` runs over the help page `adopt.md` (its path in
  Files touched), it prints the census section's GitLab lines.
  Red when: the page states the in-job keys alone.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 · the `ci-census` plant's four GitLab indirection jobs, the failing case staged by 63's in-job opaque list · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 54 to 64, id 15 (HIGH, item
  H5).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-76, TOOL-dLinkedLibrary-80, promoted from the spec
  audit of units 65 to 74; nothing else moved.
- rev-3 · 2026-10-27 · §3 · the hands-off edges to units 93 and 96, the mirrors of the
  consumes-from edges their specs declare, promoted from the spec audit of units 87 to 91;
  no scope or criterion moved.
- rev-4 · 2026-10-27 · §3 · the hands-off edge to unit 102, the mirror of the
  consumes-from edge its spec declares, promoted from the spec audit of units 92 to 96;
  no scope or criterion moved.

## 10. Reuse audit

The seam extended is 63 S2's opaque-step refusal inside `TOOL-dLinkedLibrary-8`'s `ci-job` class in
`tools/memory-tree/adopt_program.py`, one more set of keys on the same rule. `python
tools/codebase-map/reuse_lookup.py "refuse a ci job that inherits its script through extends or an
anchor"` ranked `anchors`, `anchor_at`, `CensusRefused`, `ScopeRefused` and `ReapRefused`, none a CI
reader, so no existing seam fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding of a spec audit repair a unit at the next order step" --terms "spec-audit promoted high finding repairs order staged break conf reader row grammar census indirection"`
