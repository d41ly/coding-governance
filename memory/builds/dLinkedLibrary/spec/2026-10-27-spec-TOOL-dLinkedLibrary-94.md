# TOOL-dLinkedLibrary-94 — the CI census reads an Azure `variables:` value written on the line after its key

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 34 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-94-deviation-941.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-94-deviation-941.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 87 to 91
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md`) confirmed
finding **id 22 at HIGH**, report item **H3**. No other id shares the item.

`TOOL-dLinkedLibrary-88` S1 catches a flow value only on the `variables:` key's own line. YAML also lets
the value sit on the next, deeper-indented line: `variables:` over `  [ { group: release-vars } ]`, or
`variables: # vars` over `  { CONFIG: Release }`. `TOOL-dLinkedLibrary-81` S1 reads only block list items
and mapping keys, so no 81 or 88 rule names that line, and a variable group reaches jobs that grade
`importable`. 81 S2's scalar branch has the same same-line limit: `variables:` over `  ${{
parameters.vars }}` is a scalar no rule reads.

This unit locates a `variables:` value once, on the key's line or the next deeper content line, and has
88's flow and empty tests and 81's scalar branch read the located value. It repairs
`TOOL-dLinkedLibrary-88` and builds one step after it (order 34).

## 2. Scope (IN)

- **S1** — The locator. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, the value of an
  `azure-pipelines.yml` `variables:` key, at any level 81 S1 reads, is the text after its colon when that
  text holds anything but whitespace and a comment. Otherwise it is the first following line that is
  neither blank nor comment-only, when that line is indented deeper than the key; otherwise the value is
  empty, an empty block as 81 §5 reads one. Observed by AC1 to AC5.
- **S2** — Flow on the next line. 88 S1's flow test and 88 S4's empty-collection test read S1's located
  value, so `variables:` over a deeper line opening `[` or `{` refuses the jobs its block applies to,
  scoped as 79 S3 scopes a hit, each reading `refused: unreadable variables item flow`; a deeper line
  that is the whole of `[]` or `{}` refuses nothing. Observed by AC1, AC2 and AC4.
- **S3** — A scalar on the next line. A located next-line value that opens neither `- `, nor a mapping key
  as 81 S1 reads one, nor `[` or `{` is a scalar, and refuses as 81 S2's scalar branch does, `<form>`
  `expression`. The four openings are disjoint by their first characters, so no order between the tests
  is needed for a next-line value. Observed by AC3.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch tree of its
  own with two plain jobs, `publish` running `./publish.sh` and `test` running `npm test`: a pipeline-level
  `variables:` alone over `  [ { group: release-vars } ]`; a pipeline-level `variables: # vars` over a
  blank line, the comment line `  # release settings` and `  { CONFIG: Release }`; a pipeline-level
  `variables:` alone over `  ${{ parameters.vars }}`, beside a `parameters:` list holding `- name: vars`
  with `type: object`; and a pipeline-level `variables:` alone over `  {}`. Observed by AC1 to AC4.

## 3. Non-goals (OUT)

- Reading a flow collection's items: 88 §3 keeps the census a text reader, and a flow value refuses.
- The same-line order between 88's flow test and 81's scalar branch: the minors batch
  `TOOL-dLinkedLibrary-96`, its items for ids 1 and 25, which land at 88's pass.
- GitLab's and GitHub's variable blocks: unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-88` — S1's flow test and S4's empty-collection test, which S1 and S2 apply to a value on the line after the key (id 22)
- **consumes-from** `TOOL-dLinkedLibrary-81` — S1's list and mapping reading and S2's scalar branch, which S1 and S3 apply to a value on the line after the key (id 22)
- **hands-off** `TOOL-dLinkedLibrary-99` — S1's locator, S3's next-line scalar test and §5's empty-block sentence, which unit 99 extends to a block list at the key's own indentation (id 24)
- **hands-off** `TOOL-dLinkedLibrary-102` — S1, S3 and AC5, which unit 102's S8 and S9 settle and plant at this unit's pass, §4's cites, by its S20, and the naming leg at this pass, by its S21 (ids 3, 25, 8, 20)

## 4. Design

### Evidence

- 88 S1 (`2026-10-27-spec-TOOL-dLinkedLibrary-88.md:35-38`) reads a value "on its own line", the key's
  line, and 88 S5 (`:46-51`) plants only same-line values and a `- {` item.
- 81 S1 and S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-81.md`, S1 and S2) read `- name:`, `- group:` and
  `- template:` items, plain mapping keys, keys opening `${{`, and a scalar on the key's line.
- Azure YAML is YAML 1.2, in which a block mapping's value may begin on the next, deeper-indented line,
  after blank and comment lines.

### An Azure file under S1 and S2

```yaml
variables:                        # S1: the value is the next content line
  [ { group: release-vars } ]     # S2: refused, item form flow
jobs:
- job: publish
  steps:
  - script: ./publish.sh          # refused: unreadable variables item flow
```

### Rollout

Order 34, one step after `TOOL-dLinkedLibrary-88`, beside `TOOL-dLinkedLibrary-90`. Both write
`adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences the passes; neither reads the other's
plant. If the pass adds a function, it re-renders the generated map with `python
tools/codebase-map/gen_map.py --write` where its `--check` exits 1, in the pass commit.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: the Rollout re-render

### Alternatives rejected

- **A next-line flow test beside 88 S1's same-line test.** Two value readers for one key, and the
  scalar branch keeps the same hole; S1 locates the value once for every test.
- **Refusing every `variables:` whose value is not on the key's line.** It refuses every block list
  and mapping, the forms 81 S1 reads.

## 5. Production-readiness checklist

- security — closes the import of a job whose variables arrive as a flow collection or an expression
  on the line after the key; deny by default.
- perf / scale — one look-ahead per `variables:` key.
- error / empty / loading states — a key with nothing deeper after it is an empty block and refuses
  nothing; `[]` or `{}` on the next line refuses nothing.
- observability — each refusal names the form `flow` or `expression`.
- risks — a pipeline writing harmless variables in flow style on the next line refuses its jobs; the
  owner may rule a job in.
- testing — S4's plants under `adopt_program.py --fixture`, AC5's scratch copy.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — none under `help/`: the forms and reasons 88 and 81 name are unchanged.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both jobs of
  the tree whose `variables:` stands alone over `  [ { group: release-vars } ]` read `refused: unreadable
  variables item flow`.
  Red when: the next-line flow value is neither an item nor a key to 81's read, and the jobs read
  `importable`.
- **AC2** — When the same plant runs, both jobs of the tree whose `variables: # vars` sits over a blank
  line, a comment line and `  { CONFIG: Release }` read `refused: unreadable variables item flow`.
  Red when: the locator stops at a blank or comment line and the flow mapping passes.
- **AC3** — When the same plant runs, both jobs of the tree whose `variables:` stands alone over `  ${{
  parameters.vars }}` read `refused: unreadable variables item expression`.
  Red when: a next-line scalar is read as an empty block and passes.
- **AC4** — When the same plant runs, both jobs of the tree whose `variables:` stands alone over `  {}`
  read `importable`.
  Red when: an empty flow collection on the next line refuses its jobs.
- **AC5** — When a scratch copy of `adopt_program.py` whose locator reads only the key's line runs the
  same plant by `python -I`, both jobs of AC1's, AC2's and AC3's trees print `importable`.
  Red when: the staged break leaves a tree refused, so the plant does not discriminate S1.

## 7. Gates

`codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC4 · the `ci-census` plant's four next-line `variables:` trees, the failing case staged by a locator that reads the key's line alone · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 87 to 91, id 22 (HIGH, item
  H3).
- rev-2 · 2026-10-27 · §3 · the hands-off edges to units 99 and 102, the mirrors of the
  consumes-from edges their specs declare, promoted from the spec audit of units 92 to 96;
  no scope or criterion moved.

## 10. Reuse audit

The seam extended is 88 S1's flow test and 81 S1 and S2's closed-set read inside
`TOOL-dLinkedLibrary-8`'s `ci-job` class in `tools/memory-tree/adopt_program.py`, with 79 S3's scoping
reused for the refusal. `python tools/codebase-map/reuse_lookup.py "find the value of a yaml key on the
next indented line"` ranked `key`, `keys`, `read_conf_key` and `check_line`; `read_conf_key`
(`tools/check-spec-tokens.py`, `tools/roles/roles_lib.py`) reads a conf key and no YAML value, so no
existing seam fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how does the census find a variables value written on the line after its key" --terms "census ci-job azure variables flow value next line indented locator refused item"`
