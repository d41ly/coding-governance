# TOOL-dLinkedLibrary-85 — the CI census reads a block-scalar header on a list item that opens with a key, the GitHub `- run: |` step

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 25 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |
| [2026-10-27-build-TOOL-dLinkedLibrary-85-deviation-851.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-85-deviation-851.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-86 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 75 to 80
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md`) confirmed
finding **id 35 at HIGH**, report item **H4**. No other id shares the item; id 1, item M1, binds the same
defect at MEDIUM and is an item of the minors batch `TOOL-dLinkedLibrary-86`.

`TOOL-dLinkedLibrary-77` S1 states the header `<key>: |` and S2 the header `- |`, a dash followed by S1's
sequence after the colon. Neither states a list item whose first key opens the block, which is how a
GitHub step is written: `- run: |`. 77 §4 offers a probe pattern as the grammar, and under python it
rejects `      - run: | # release`, `- run: &a |` and `- run: !!str |2-` while accepting `  script: |`
and `      - |`. A builder who copies it stops recognising the most common GitHub `run:` header: the block
goes unread and `npm publish` grades `importable`, or `TOOL-dLinkedLibrary-78` S3 refuses every such job
as an unreadable multi-line scalar.

This unit adds the third header form, widens the pattern to it, and plants it. It repairs
`TOOL-dLinkedLibrary-77` and builds one step after it (order 25).

## 2. Scope (IN)

- **S1** — The third form. In `tools/memory-tree/adopt_program.py`'s block-scalar reader, a line also
  opens a block scalar when it holds a dash, whitespace, and then 77 S1's whole sequence: the key and its
  colon, the optional node properties, the indicator, the optional chomping and indentation indicators,
  and the optional comment. Observed by AC1 and AC2.
- **S2** — Its extent. The block belongs to the key, not the dash: its lines are those indented deeper
  than the key's own column, the dash's column plus the whitespace after it, read to the extent 73 S1
  states from that column. Observed by AC3.
- **S3** — The pattern. 77 §4's probe pattern gains an optional dash before the key, `(?:-[ \t]+)?`, and
  keeps its bare-dash alternative; this spec's §4 records the widened pattern and the shapes it was run
  against. Observed by AC1.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, in one GitHub workflow
  under `.github/workflows/`: a job whose step is `      - run: | # release` holding `npm publish`; a job
  whose step is `      - run: &a |` holding `npm publish`; and a job whose step is `      - run: |`
  holding `npm test` followed by a second step `      - run: echo done`, whose block ends at that step.
  Observed by AC1 to AC3.

## 3. Non-goals (OUT)

- The plant spelling 77 AC1's GitHub header as a `- run: !!str |2-` step: the minors batch
  `TOOL-dLinkedLibrary-86`, its item for id 1.
- Folding and continuation: `TOOL-dLinkedLibrary-78`, unchanged.
- A nested sequence `- - |`: no CI dialect the census reads writes one, and the pattern still refuses it.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-77` — S1's key header, S2's list-item header and §4's probe pattern, which S1 to S3 extend to a list item opening with a key (id 35)
- **hands-off** `TOOL-dLinkedLibrary-86` — the `- run: !!str |2-` step of 77 AC1's GitHub plant, which unit 86 spells and grades against this unit's third form (id 1)
- **hands-off** `TOOL-dLinkedLibrary-91` — S4's third plant, which unit 91's S16 completes with a key-column sibling at this unit's pass (id 5)

## 4. Design

### Evidence

- 77 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-77.md:43-45`): "A list item opens a block scalar when its
  dash is followed by the same sequence S1 states after the colon".
- `2026-10-26-spec-TOOL-dLinkedLibrary-51.md:92` plants the GitHub step as `    - run: |`.

### The widened pattern, as a probe

The builder may write it another way. On 2026-10-27, under `python -I`, the old pattern and this one
gave the results below.

```python
re.compile(r'^(?P<ind>[ \t]*)(?:(?P<dash>-[ \t]+)?(?P<key>[A-Za-z_][\w.-]*)[ \t]*:|-)[ \t]+'
           r'(?:(?:&\S+|!\S*)[ \t]+){0,2}(?P<style>[|>])(?:[1-9][+-]?|[+-][1-9]?)?'
           r'(?:[ \t]+#.*)?[ \t]*$')
```

| Line | 77 §4's pattern | This pattern |
|---|---|---|
| `      - run: \| # release`, `- run: &a \|`, `- run: \|`, `      - run: !!str \|2-`, `- script: &a \|` | refused | accepted |
| `script: \| # release`, `run: !!str &a \|2-`, `- &x \|- # c`, `  script: \|`, `      - \|` | accepted | accepted |
| `- run: npm publish`, `- run: \|x`, `- run: "\|"`, `- - \|`, `script: \|x` | refused | refused |

### Rollout

Order 25 beside `TOOL-dLinkedLibrary-83` and `TOOL-dLinkedLibrary-84`. All three write
`adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences the passes; this unit owns the header and
neither sibling changes it.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4

### Alternatives rejected

- **Stripping a leading dash before the header test.** It loses the key's column, which S2 needs to end
  the block at the next step.
- **Refusing any `- <key>: |` line.** It refuses every GitHub job with a multi-line `run:`, the common
  case, which deny by default does not require when the block can be read.

## 5. Production-readiness checklist

- security — closes the bypass of the publish refusal by the GitHub step header form.
- perf / scale — one pattern per line, as before.
- error / empty / loading states — a header with nothing after it reads an empty block, as 73 states.
- observability — a refusal names the verb, as 51 states.
- risks — none beyond 77's: the form is YAML's own.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none.
- user docs — none under `help/`: the page names the keys read, and the header is YAML's own.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the GitHub jobs
  whose steps are `- run: | # release` and `- run: &a |` each read `refused: npm publish`.
  Red when: 77's two-form header leaves a `- <key>: |` block unread.
- **AC2** — When the same plant runs, no job of the workflow reads `refused: unreadable multi-line scalar
  run`.
  Red when: an unrecognised `- run:` header reaches 78 S3's split-scalar refusal.
- **AC3** — When the same plant runs, the job whose `- run: |` block holds `npm test` followed by the step
  `- run: echo done` reads `importable`, its block ending at the second step.
  Red when: the block's extent is measured from the dash and swallows the next step.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 · the `ci-census` plant's three `- run:` steps, the failing case staged by 77's two-form header · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 75 to 80, id 35 (HIGH, item
  H4).
- rev-2 · 2026-10-27 · §3 · the hands-off edges to units 91, the mirrors of the consumes-from
  edges their specs declare, promoted from the spec audit of units 81 to 86; no scope or criterion moved.

## 10. Reuse audit

The seam extended is 77's header, on `TOOL-dLinkedLibrary-51` S2's block-scalar reader in
`tools/memory-tree/adopt_program.py`: one more opener form, the same sequence after it. `python
tools/codebase-map/reuse_lookup.py "read a yaml block scalar header on a list item that opens with a
key"` ranked `read`, `read_text`, `key` and `keys`, none a YAML reader, so no existing seam fits beyond
the census's reader.

Recall terms used: `python tools/memory-recall/query.py "how is a block scalar header read on a github step list item" --terms "census ci-job block scalar header list-item dash run key anchor tag pattern"`
