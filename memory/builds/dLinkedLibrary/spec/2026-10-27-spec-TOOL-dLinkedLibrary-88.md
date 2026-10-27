# TOOL-dLinkedLibrary-88 — the CI census refuses a flow-style Azure `variables:` value or item as an unreadable item form

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 33 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-88-deviation-881.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-88-deviation-881.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 81 to 86
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md`) confirmed
finding **id 27 at HIGH**, report item **H2**. No other id shares the item.

`TOOL-dLinkedLibrary-81` S1 reads an Azure `variables:` block as a block list or a block mapping, and S2
refuses an unknown first key, an item or key opening `${{`, and a scalar. A flow value is none of those:
`variables: [ { group: release-vars } ]`, `variables: { CONFIG: Release }`, or a list item `- { group: x
}`, which has no first key for `<form>`. Flow reading exists only in `TOOL-dLinkedLibrary-83` S1, for
GitLab's `default:`. So a job whose variable group arrives in flow style grades `importable`, a wrong
security result; `TOOL-dLinkedLibrary-82`'s `- template:` item has the same hole.

This unit makes flow style its own refused form: any non-empty flow value of `variables:`, and any list
item opening a flow collection, refuses the jobs the block applies to. It repairs
`TOOL-dLinkedLibrary-81` and builds one step after it (order 33).

## 2. Scope (IN)

- **S1** — The flow value. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, an
  `azure-pipelines.yml` `variables:` key, at any level 81 S1 reads, whose value on its own line opens `[`
  or `{`, after optional whitespace, refuses every job its block applies to, scoped as 79 S3 scopes a hit.
  Each job reads `refused: unreadable variables item flow`. Observed by AC1, AC2 and AC4.
- **S2** — The flow item. A list item of a `variables:` block whose text after the dash opens `{` or `[`
  refuses the same jobs with the same reason, `<form>` `flow`. Observed by AC3.
- **S3** — Precedence. The flow test runs before any item reading, so 79 S2's `- group:` reading and 82
  S1's `- template:` reading, which read block items only, never see a flow item, and a flow-style group
  or template reads `refused: unreadable variables item flow`. Observed by AC1 and AC3.
- **S4** — The empty collection. A `variables:` whose whole value is `[]` or `{}` declares no variable
  and refuses nothing, as 81 §5 states for an empty block. Observed by AC5.
- **S5** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch tree of its
  own with two plain jobs, `publish` running `./publish.sh` and `test` running `npm test`: an Azure file
  whose pipeline-level line is `variables: [ { group: release-vars } ]`; one whose pipeline-level line is
  `variables: { CONFIG: Release }`; one with two stages, the first holding a stage-level `variables:` list
  whose only item is `- { group: stage-vars }` and the second none, each stage holding the two jobs; and
  one whose pipeline-level line is `variables: {}`. Observed by AC1 to AC5.

## 3. Non-goals (OUT)

- Reading a flow collection's items: the census stays a text reader, as 63 §3 keeps it, and the closed
  set refuses what it does not read.
- GitLab's and GitHub's variable blocks: 79 S1's rows for them, and 83 S1's flow reading of `default:`,
  are unchanged.
- The page sentence naming the item forms the census reads: the minors batch `TOOL-dLinkedLibrary-91`,
  its item for ids 7 and 25, which names flow style beside them.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-81` — S1's closed set, S2's `unreadable variables item <form>` reason and its scoping, which S1 to S3 extend to a flow value and a flow item (id 27)
- **hands-off** `TOOL-dLinkedLibrary-91` — the `flow` form S1 and S2 add, which unit 91's page sentence names among the refused item forms (ids 7, 25)
- **hands-off** `TOOL-dLinkedLibrary-94` — S1's flow test and S4's empty-collection test, which unit 94 applies to a value on the line after the key (id 22)
- **hands-off** `TOOL-dLinkedLibrary-96` — S1, S3 and S4 with AC4, whose order before 81 S2's scalar branch unit 96's S1 and S2 state and restage at this unit's pass, and this unit's pass, which lands 91 S3's page sentence and the map re-render, by S3 and S12 (ids 1, 25, 2, 11)

## 4. Design

### Evidence

- 81 S1 and S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-81.md`, S1 and S2) name a block list, a block
  mapping, a scalar, and items or keys opening `${{`; no flow rule.
- 83 S1 (`2026-10-27-spec-TOOL-dLinkedLibrary-83.md`, S1) reads a flow collection for GitLab's `default:`
  only.
- 79 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-79.md:47-54`) reads `- group: <name>`, a block item.
- Azure YAML is YAML 1.2, so a flow sequence or flow mapping is a legal `variables:` value.

### An Azure file after S1 and S3

```yaml
variables: [ { group: release-vars } ]   # S1: refused, item form flow
jobs:
- job: publish
  steps:
  - script: ./publish.sh       # refused: unreadable variables item flow
```

### Rollout

Order 33 beside `TOOL-dLinkedLibrary-87`. Both write `adopt_program.py`, so BUILD-METHOD M6's clause 1
sequences the passes; neither reads the other's plant.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S5

### Alternatives rejected

- **Reading flow items as 83 S1 does, then applying 81 S1's item test.** It needs key extraction inside
  a flow collection, which 83's token search does not give: a parser in all but name, for a style Azure
  pipelines rarely use. Refusing is deny by default and costs a false refusal at most.
- **Refusing `[]` and `{}` too.** They declare nothing, and 81 §5 already reads an empty block as
  refusing nothing.

## 5. Production-readiness checklist

- security — closes the import of a job whose variables, a group or template included, arrive in flow
  style; deny by default.
- perf / scale — one prefix test per `variables:` value and item.
- error / empty / loading states — S4: an empty flow collection refuses nothing; an unclosed one still
  opens `[` or `{` and refuses.
- observability — each refusal names the form `flow`.
- risks — a pipeline writing harmless variables in flow style refuses its jobs; the owner may rule a job
  in.
- testing — S5's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — the page sentence is unit 91's item for ids 7 and 25.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both jobs of
  the tree whose line is `variables: [ { group: release-vars } ]` read `refused: unreadable variables item
  flow`.
  Red when: the flow value is neither a block item nor a scalar to 81's read, and the jobs read
  `importable`.
- **AC2** — When the same plant runs, both jobs of the tree whose line is `variables: { CONFIG: Release }`
  read `refused: unreadable variables item flow`.
  Red when: a flow mapping value passes.
- **AC3** — When the same plant runs, both jobs of the stage whose list holds `- { group: stage-vars }`
  read `refused: unreadable variables item flow`, and both jobs of the second stage read `importable`.
  Red when: a flow item has no first key and passes, or a stage-level hit reaches another stage.
- **AC4** — When a scratch copy of `adopt_program.py` without S1's test runs the same plant by `python
  -I`, both jobs of AC1's tree print `importable`.
  Red when: the staged break leaves the jobs refused, so the plant does not discriminate S1.
- **AC5** — When the same plant runs, both jobs of the tree whose line is `variables: {}` read
  `importable`.
  Red when: an empty flow collection refuses its jobs.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC5 · the `ci-census` plant's four flow-style `variables:` trees, the failing case staged by 81's block-only read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 81 to 86, id 27 (HIGH, item
  H2).
- rev-2 · 2026-10-27 · §3 · the hands-off edges to units 94 and 96, the mirrors of the
  consumes-from edges their specs declare, promoted from the spec audit of units 87 to 91;
  no scope or criterion moved.

## 10. Reuse audit

The seam extended is 81 S1 and S2's closed-set item read inside `TOOL-dLinkedLibrary-8`'s `ci-job` class
in `tools/memory-tree/adopt_program.py`, with 79 S3's scoping reused for the refusal. `python
tools/codebase-map/reuse_lookup.py "read a yaml flow collection value in a ci file"` ranked `read`,
`read_text`, `read_conf` and `read_journal`, none a CI or YAML reader, so no existing seam fits beyond the
census being extended; 83 S1's flow reading was weighed and rejected in §4.

Recall terms used: `python tools/memory-recall/query.py "how does the census read a yaml flow sequence or flow mapping value" --terms "census ci-job flow mapping sequence bracket azure variables group refused closed-set reader"`
