# TOOL-dLinkedLibrary-76 — the CI census refuses a GitLab indirection key under `default:`, which reaches every job

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 24 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-27-build-TOOL-dLinkedLibrary-76-deviation-761.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-76-deviation-761.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 65 to 74
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md`) confirmed
finding **id 32 at HIGH**, report item **H2**. No other id shares the item.

`TOOL-dLinkedLibrary-71` S1 refuses `extends:`, a `!reference` tag, an alias `*<name>` or a merge key
`<<:` only when a `.gitlab-ci.yml` job carries one. `TOOL-dLinkedLibrary-63` S1 applies `default:`'s
`script`, `before_script` and `after_script` to every job, and `default:` is not a job. So `default: {
before_script: !reference [.publish, script] }`, with `npm publish` in a hidden `.publish`, injects a
publish into every job, and each plain job grades `importable`: under 63 the tag reads as literal text
that matches no refusal pattern. That bypasses the deny-by-default rule 63's F2 settled.

This unit applies 71's indirection test to every block 63 S1 applies to a job, `default:` included, and
plants the inherited case. It repairs `TOOL-dLinkedLibrary-71` and builds one step after it (order 24).

## 2. Scope (IN)

- **S1** — The blocks tested. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, 71 S1's test for a
  `!reference` tag, an alias `*<name>` or a merge key `<<:` runs over every block 63 S1 applies to a job:
  the job's own keys and the top-level `default:` map, at any depth below it. Observed by AC1 and AC2.
- **S2** — A `default:` hit. An indirection key found under `default:` refuses every job in the file, each
  reading `refused: opaque step <key> default:<child>`, `<key>` spelled `!reference`, `alias` or `<<` as 71
  S1 spells it and `<child>` the key of `default:` that holds it. A `default:` is not a job and has no
  census row of its own. Observed by AC1 and AC2.
- **S3** — What stays readable. A `default:` carrying none of S1's keys, its script lines applied as 63 S1
  states, leaves a plain job graded as 63 S1 to S3 and 71 S3 state; an anchor definition `&<name>` is not
  an indirection key. Observed by AC3.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each in its own scratch
  tree because a `default:` hit refuses the whole file: one whose `default:` holds `before_script:
  !reference [.publish, script]`, a hidden `.publish` running `npm publish`, and a plain `test` job running
  `npm test`; one whose `default:` holds `<<: *publish` over a hidden job anchored `&publish`, beside the
  same plain job; and one whose `default:` holds `before_script: [npm ci]` beside the same plain job.
  Observed by AC1 to AC3.
- **S5** — The page. `help/adopt.md`'s census section carries the sentence "A `!reference`, alias or merge
  key under `default:` refuses every job in the file." Observed by AC4.

## 3. Non-goals (OUT)

- Resolving `default:`, an anchor or a hidden job: the census stays a text reader, as 63 §3 and 71 §3
  keep it.
- Credentials `default:` carries, such as `id_tokens:`: `TOOL-dLinkedLibrary-79`.
- The job-level keys and the top-level `include:`: `TOOL-dLinkedLibrary-71` S1 and S2, unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-71` — S1's indirection test, S3's readable set and the `ci-census` plant, which S1 and S2 extend to `default:` (id 32)
- **hands-off** `TOOL-dLinkedLibrary-83` — S1's indirection test over `default:`, S2's file-wide refusal and S4's plant trees, which unit 83 extends to the `default:` line's own value and to flow style (id 32 of the spec audit of units 75 to 80)
- **hands-off** `TOOL-dLinkedLibrary-84` — S1's indirection test, S2's file-wide refusal and S3's application of `default:`'s script lines, which unit 84 runs over every other job-wide top-level block (id 33 of the spec audit of units 75 to 80)
- **hands-off** `TOOL-dLinkedLibrary-86` — S2's reason and file-wide refusal and S4's plant trees, which unit 86 completes (ids 8, 42, 19, 24, 37 of the spec audit of units 75 to 80)

## 4. Design

### Evidence

- 63 S1's key table: `.gitlab-ci.yml` reads "`script`, `before_script`, `after_script`, and `default:`'s
  same three, applied to every job".
- 71 S1 refuses the keys when "a `.gitlab-ci.yml` job" carries one; 71 S4's four plants are job-level or
  file-level `include:`, none a `default:` case.
- `git ls-files` lists no `.gitlab-ci.yml` at base, so S4's plants are the whole population.

### A GitLab file after S1 and S2

```yaml
default:
  before_script: !reference [.publish, script]   # S1: found under default:
.publish:
  script: [npm publish]
test:
  script: [npm test]          # S2: refused, opaque step !reference default:before_script
```

### Rollout

Order 24 beside `TOOL-dLinkedLibrary-77` and `TOOL-dLinkedLibrary-78`. All three write
`adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences the passes; this unit owns the indirection
test and neither sibling changes it.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4
- `help/adopt.md`: S5

### Alternatives rejected

- **Refusing only the jobs whose inherited text holds a publish verb.** The census cannot read the
  referenced text, so that is a guess, as 71 §4 rejects it.
- **Reading `default:` as a job of its own.** A refused `default:` row leaves every real job `importable`,
  which is the bypass.

## 5. Production-readiness checklist

- security — closes the import of a publish injected through `default:`; deny by default.
- perf / scale — one more block walked per file.
- error / empty / loading states — unchanged from 63 and 71.
- observability — each refusal names the key and the `default:` child holding it.
- risks — a file whose `default:` uses `!reference` for a harmless step refuses every job; the owner may
  rule a job in, as for any refused job.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — `help/adopt.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the plain
  `test` job of the tree whose `default:` holds `before_script: !reference [.publish, script]` reads
  `refused: opaque step !reference default:before_script`.
  Red when: a plain job reads `importable` while `default:` injects referenced text into it.
- **AC2** — When the same plant runs, the plain `test` job of the tree whose `default:` holds `<<:
  *publish` reads `refused: opaque step <<`.
  Red when: a merge key under `default:` passes.
- **AC3** — When the same plant runs, the plain `test` job of the tree whose `default:` holds
  `before_script: [npm ci]` reads `importable`, and no tree has a census row named `default`.
  Red when: the refusal reaches a `default:` with no indirection, or `default:` is graded as a job.
- **AC4** — When `grep -n 'under .default:. refuses every job'` runs over the help page `adopt.md` (its
  path in Files touched) at this pass's tip it prints S5's sentence, and over the page as unit 71's pass
  leaves it, read with `git show`, it prints nothing.
  Red when: the page names the job-level keys alone.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 · the `ci-census` plant's three `default:` trees, the failing case staged by 71's job-only indirection test · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 65 to 74, id 32 (HIGH, item
  H2).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-83, TOOL-dLinkedLibrary-84, TOOL-dLinkedLibrary-86, promoted from the spec
  audit of units 75 to 80; nothing else moved.

## 10. Reuse audit

The seam extended is 71 S1's indirection test inside `TOOL-dLinkedLibrary-8`'s `ci-job` class in
`tools/memory-tree/adopt_program.py`, run over one more block. `python tools/codebase-map/reuse_lookup.py
"refuse a gitlab job whose default block carries a reference tag or alias"` ranked
`build_reference_index`, `CensusRefused`, `ScopeRefused` and `default_kits`, none a CI reader, so no
existing seam fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how does a census refuse a ci job whose text or credentials come from a block it does not read" --terms "census ci-job refused opaque step credentials default variables block scalar fold header promoted"`
