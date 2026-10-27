# TOOL-dLinkedLibrary-73 — the CI census reads a block scalar across blank lines and as a list item

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 23 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-27-build-TOOL-dLinkedLibrary-73-deviation-731.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-73-deviation-731.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-74 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 54 to 64
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md`) confirmed
finding **id 39 at HIGH**, report item **H6**. No other id shares the item.

`TOOL-dLinkedLibrary-63` S1 reads a block scalar "up to the first line indented no deeper than the key".
A blank line has indent 0, so the read stops at the first blank line inside a `|` or `>` block, which YAML
allows. S1 is also silent on a list item that is itself a block scalar, `- |` under `script:`, the common
GitLab multi-line form. `script: |` holding `npm ci`, a blank line and `npm publish` reads only `npm ci`,
and the job grades `importable`.

This unit states the block-scalar extent for the census's one reader, every dialect included, and plants
both layouts. It repairs `TOOL-dLinkedLibrary-63` and builds one step after it (order 23).

## 2. Scope (IN)

- **S1** — The extent. In `tools/memory-tree/adopt_program.py`'s block-scalar reader
  (`TOOL-dLinkedLibrary-51` S2, which 63 S1 reads for every dialect), a block scalar opened by `<key>: |`
  or `<key>: >`, with any chomping or indentation indicator, holds every following line that is empty,
  whitespace-only, or indented deeper than the key, and ends at the first line that is neither. Blank
  lines inside it are kept as lines of the block. Observed by AC1.
- **S2** — The list item. A list item `- |` or `- >`, with any indicator, under a line key of 63 S1 opens a
  block scalar measured from the item's dash: it holds every following line that is blank or indented
  deeper than the dash, and each of its lines is a line the job runs. Observed by AC2.
- **S3** — The plants, cases of `adopt_program.py --fixture --plant ci-census`: a GitLab `script: |` block
  holding `npm ci`, a blank line, then `npm publish`; a GitLab `script:` list whose second item is `- |`
  holding `cargo publish`; and a GitHub `run: |` with a blank line before `npm publish`. Each reads
  `refused`. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Which keys a dialect's job runs: 63 S1, unchanged.
- The opaque-step keys: `TOOL-dLinkedLibrary-71` and `TOOL-dLinkedLibrary-72`.
- Flow scalars split over lines and other YAML forms the census does not read: the census stays a text
  reader, as 63 §3 keeps it.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-63` — S1's block-scalar rule over every dialect's line keys, whose extent S1 and S2 restate (id 39)
- **hands-off** `TOOL-dLinkedLibrary-77` — S1's key header and S2's list-item header, which unit 77 restates to YAML's grammar (id 34 of the spec audit of units 65 to 74)
- **hands-off** `TOOL-dLinkedLibrary-78` — S1's `>` block and S2's per-line reading, which unit 78 folds and joins before matching (id 35 of the spec audit of units 65 to 74)

## 4. Design

### Evidence

- 63 S1: "Each key is read as a scalar, a list of scalars, or a block scalar (`|`, `>`, with or without a
  chomping indicator) up to the first line indented no deeper than the key".
- YAML 1.2 §8.1: empty lines inside a literal or folded block scalar belong to its content, and the
  block's indentation is set by its first non-empty line.

### The two layouts after S1 and S2

```yaml
release:
  script: |
    npm ci

    npm publish          # S1: inside the block; refused: npm publish
deploy:
  script:
    - npm ci
    - |
      cargo publish      # S2: the item's block; refused: cargo publish
```

### Rollout

Order 23 beside `TOOL-dLinkedLibrary-71` and `TOOL-dLinkedLibrary-72`. All three write
`adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences the passes; this unit owns the reader and
neither sibling changes it.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S3

### Alternatives rejected

- **A YAML library.** 63 §3 and unit 8 §5 keep the census a text reader with no new dependency (M3
  veto 2).
- **A per-dialect block reader.** The rule is YAML's and identical for every dialect; one reader keeps
  one extent.

## 5. Production-readiness checklist

- security — closes the bypass of the publish refusal by an ordinary YAML layout.
- perf / scale — the same lines read, with blank lines kept.
- error / empty / loading states — a block that runs to the end of the file ends there.
- observability — a refusal names the verb, as 51 states.
- risks — a trailing blank run is read as part of the block, which only adds empty lines.
- testing — S3's plants under `adopt_program.py --fixture`.
- migration — none.
- user docs — none under `help/`: the page names the keys read, and the extent is YAML's own.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the GitLab
  job whose `script: |` holds a blank line before `npm publish` reads `refused: npm publish`, and the
  GitHub job whose `run: |` does the same reads the same.
  Red when: the read stops at a blank line inside a block.
- **AC2** — When the same plant runs, the GitLab job whose `script:` list holds a `- |` item running
  `cargo publish` reads `refused: cargo publish`.
  Red when: a list-item block scalar is not read.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 · the `ci-census` plant's blank-line and `- |` jobs, the failing case staged by 63's no-deeper-than-the-key extent · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 54 to 64, id 39 (HIGH, item
  H6).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-77, TOOL-dLinkedLibrary-78, promoted from the spec
  audit of units 65 to 74; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-51` S2's block-scalar reader in
`tools/memory-tree/adopt_program.py`, the one reader 63 S1 applies to every dialect. `python
tools/codebase-map/reuse_lookup.py "read a yaml block scalar by indentation including blank lines"`
ranked `read`, `read_text`, `read_conf` and `read_journal`, none a YAML reader, so no existing seam fits
beyond the census's reader.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding of a spec audit repair a unit at the next order step" --terms "spec-audit promoted high finding repairs order staged break conf reader row grammar census indirection"`
