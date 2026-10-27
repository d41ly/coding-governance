# TOOL-dLinkedLibrary-77 — the CI census reads a block-scalar header that carries node properties or a comment

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 24 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-77-deviation-771.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-77-deviation-771.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 65 to 74
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md`) confirmed
finding **id 34 at HIGH**, report item **H3**. No other id shares the item; id 35, item H4, is the
folding half of the same reader and its own unit, `TOOL-dLinkedLibrary-78`.

`TOOL-dLinkedLibrary-73` S1 opens a block scalar on `<key>: |` or `<key>: >` with chomping or indentation
indicators, and S2 on `- |` or `- >`. Neither admits node properties, an anchor such as `script: &rel |`
or a tag such as `run: !!str |`, nor a trailing comment, `script: | # release`. All are legal YAML
block-scalar headers. A reader built to 73's text reads such a header as a plain scalar and leaves the
block's lines unread, so `npm publish` inside grades `importable`; 63 S3's credential rule does not catch
a bare `npm publish` relying on an implicit token.

This unit states the header as YAML's grammar states it, for the key form and the list-item form, and
plants one case per optional component. It repairs `TOOL-dLinkedLibrary-73` and builds one step after it
(order 24).

## 2. Scope (IN)

- **S1** — The key header. In `tools/memory-tree/adopt_program.py`'s block-scalar reader (73 S1), a line
  opens a block scalar when it holds, in order: the key and its colon; optionally node properties, an
  anchor `&<name>` and a tag (`!<suffix>`, `!!<suffix>` or `!<<uri>>`), at most one of each, in either
  order, each followed by whitespace; the indicator `|` or `>`; optionally a chomping indicator `+` or `-`
  and an indentation digit `1` to `9`, at most one of each, in either order; then optional whitespace and,
  after at least one space, an optional `#` comment to the end of the line. This is YAML 1.2.2's
  `c-b-block-header` preceded by `c-ns-properties`. Observed by AC1.
- **S2** — The list-item header. A list item opens a block scalar when its dash is followed by the same
  sequence S1 states after the colon; the block's extent is 73 S2's, measured from the dash. Observed by
  AC2.
- **S3** — The order of rules. 71 S1's refusal of a `!reference` tag is read before this header, so a
  tagged header is a block only when its tag is not `!reference`. A line that holds anything else after
  the indicator, `script: |x` say, is not a header, as before. Observed by AC3.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`: a GitLab `script: | #
  release` block holding `npm publish`; a GitLab `script: &rel |` block holding `npm publish`; a GitHub
  `run: !!str |2-` block holding `npm publish`; and a GitLab `script:` list whose second item is `- &up |-
  # upload` holding `cargo publish`. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Folding a `>` block and joining a continued command: `TOOL-dLinkedLibrary-78`.
- The extent of a block, blank lines included: 73 S1 and S2, unchanged.
- Resolving an anchor or an alias: the census stays a text reader, and an alias is 71's refusal.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-73` — S1's key header and S2's list-item header, which S1 and S2 restate to YAML's grammar (id 34)
- **hands-off** `TOOL-dLinkedLibrary-85` — S1's key header, S2's list-item header and §4's probe pattern, which unit 85 extends to a list item opening with a key (id 35 of the spec audit of units 75 to 80)
- **hands-off** `TOOL-dLinkedLibrary-86` — AC1's GitHub plant and the header reader, which unit 86 spells as a `- run:` step and reads with CRs stripped (ids 1, 17 of the spec audit of units 75 to 80)

## 4. Design

### Evidence

- 73 S1: "a block scalar opened by `<key>: |` or `<key>: >`, with any chomping or indentation
  indicator"; S2: "A list item `- |` or `- >`, with any indicator"; S3's plants use bare headers only.
- YAML 1.2.2 §8.1.1, `c-b-block-header`: the indentation and chomping indicators in either order, then
  `s-b-comment`, which admits whitespace and a comment; §6.9, `c-ns-properties`: a tag and an anchor, either
  first, before the node's content.

### The header, as a probe pattern

The builder may write it another way; the probe on 2026-10-27 accepted the left column and refused the
right with this pattern.

```python
re.compile(r'^(?P<ind>[ \t]*)(?:(?P<key>[A-Za-z_][\w.-]*)[ \t]*:|-)[ \t]+'
           r'(?:(?:&\S+|!\S*)[ \t]+){0,2}(?P<style>[|>])(?:[1-9][+-]?|[+-][1-9]?)?'
           r'(?:[ \t]+#.*)?[ \t]*$')
```

| Accepted | Refused |
|---|---|
| `script: \| # release`, `script: &rel \|`, `run: !!str &a \|2-` | `script: \|x`, `script: \|#x` |
| `- &x \|- # c`, `- !<tag:yaml.org,2002:str> >+1` | `script: "\|"`, `script: npm publish` |

### Rollout

Order 24 beside `TOOL-dLinkedLibrary-76` and `TOOL-dLinkedLibrary-78`. All three write
`adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences the passes; this unit owns the header and
78 owns what is done with a block's lines.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4

### Alternatives rejected

- **A YAML library.** 63 §3 and unit 8 §5 keep the census a text reader with no new dependency (M3
  veto 2).
- **Refusing any header the reader does not recognise.** A header is recognised by the grammar above, so
  an unrecognised one is a plain scalar, which the line keys already read.

## 5. Production-readiness checklist

- security — closes the bypass of the publish refusal by an anchored, tagged or commented header.
- perf / scale — one pattern per line, as before.
- error / empty / loading states — a header with nothing after it reads an empty block, as 73 states.
- observability — a refusal names the verb, as 51 states.
- risks — an anchor on a script block is read, and its alias elsewhere stays 71's refusal.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none.
- user docs — none under `help/`: the page names the keys read, and the header is YAML's own.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the GitLab
  jobs whose headers are `script: | # release` and `script: &rel |` and the GitHub job whose header is
  `run: !!str |2-` each read `refused: npm publish`.
  Red when: a header carrying a comment, an anchor, a tag or both indicators leaves its block unread.
- **AC2** — When the same plant runs, the GitLab job whose list item is `- &up |- # upload` reads
  `refused: cargo publish`.
  Red when: a list-item header with properties or a comment is not read.
- **AC3** — When the same plant runs, 71's `!reference` job still reads `refused: opaque step !reference`
  and 73's bare-header jobs read as 73 AC1 and AC2 state.
  Red when: the wider header reads a referenced value as a block, or a bare header stops reading.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 · the `ci-census` plant's four headed blocks, the failing case staged by 73's bare-header opener · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 65 to 74, id 34 (HIGH, item
  H3).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-85, TOOL-dLinkedLibrary-86, promoted from the spec
  audit of units 75 to 80; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-51` S2's block-scalar reader in
`tools/memory-tree/adopt_program.py`, as 73 restates its extent: this unit widens only the line that opens
it. `python tools/codebase-map/reuse_lookup.py "read a yaml block scalar header with an anchor tag or
comment and fold its lines"` ranked `read`, `read_text`, `anchors` and `read_conf`, none a YAML reader,
so no existing seam fits beyond the census's reader.

Recall terms used: `python tools/memory-recall/query.py "how does a census refuse a ci job whose text or credentials come from a block it does not read" --terms "census ci-job refused opaque step credentials default variables block scalar fold header promoted"`
