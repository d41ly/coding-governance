# TOOL-dLinkedLibrary-99 — the `variables:` locator reads a block list at the key's own indentation as the value

**Status:** DEFERRED · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 35 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-99-deviation-991.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-99-deviation-991.md) | deviation | — |
| [2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 92 to 96
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md`) confirmed
finding **id 24 at HIGH**, report item **H3**. Id 17 binds the same defect at MEDIUM, item M8, and is
batched in `TOOL-dLinkedLibrary-102`.

`TOOL-dLinkedLibrary-94` S1 takes a `variables:` value from the next content line only when that line
is indented deeper than the key, and calls every other case "an empty block as 81 §5 reads one"; 94 §5
repeats that a key with nothing deeper after it refuses nothing. YAML lets a block sequence sit at its
key's own indentation, and that is the house Azure form: 81 §4 and 82 §4 write `variables:` at column 0
over `- ...` at column 0. A builder who gates 81's item reading on the locator reads that list as empty,
and a `- group:`, `- template:` or `- ${{ if }}:` item grades `importable`, reopening the credential and
indirection holes units 79, 81 and 82 close. No 94 criterion plants such a list.

This unit names every legal start of the value in the locator, the same-indent `- ` sequence among them,
plants that form under a pipeline-level `variables:` linking a variable group, and stages the locator
that reads it as empty. It repairs `TOOL-dLinkedLibrary-94` and builds one step after it (order 35).

## 2. Scope (IN)

- **S1** — The value's three starts. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, 94 S1's
  locator, for a `variables:` key whose line holds nothing after its colon but whitespace and a comment,
  takes the first following line that is neither blank nor comment-only, and reads it as the start of the
  value when it is indented deeper than the key, or when it sits at the key's own indentation and opens
  `- `. A same-indent `- ` line opens a block sequence, read item by item by 81 S1 at the list's own
  indentation, the items ending at the first content line at that indentation that does not open `- `.
  Observed by AC1 and AC3.
- **S2** — Only then empty. The value is empty, an empty block as 81 §5 reads one, only when that first
  following content line is neither deeper than the key nor a same-indent `- ` line, or when no content
  line follows. 94 §5's "a key with nothing deeper after it is an empty block" reads as this sentence.
  Observed by AC2.
- **S3** — Not a scalar. 94 S3's next-line scalar test never reads a same-indent `- ` line: a line at the
  key's indentation opening `- ` is S1's sequence, and only a deeper line is tested as a scalar, a mapping
  key or a flow opening. Observed by AC1.
- **S4** — The plant, a case of `adopt_program.py --fixture --plant ci-census`: an `azure-pipelines.yml`
  whose first line is `variables:` at column 0, followed by `- group: release-vars` at column 0, then
  `jobs:` at column 0 holding two plain jobs, `publish` running `./publish.sh` and `test` running `npm
  test`. A second case repeats it with a `- name: CONFIG` item over `  value: Release` in place of the
  group, a plain item 81 S1 reads and 79 S2 finds no credential in. Observed by AC1 and AC2.
- **S5** — The staged red. A scratch copy of `adopt_program.py` whose locator takes the next line only
  when it is deeper than the key, as 94 S1 is written, turns both jobs of S4's group tree `importable`.
  Observed by AC3.

## 3. Non-goals (OUT)

- 81's `- ${{ if ... }}:` tree and 82's `- template: release-vars.yml` tree read through S1: id 17, the
  batch `TOOL-dLinkedLibrary-102`.
- A bug-class checklist entry that a YAML value locator names every legal placement of the value: the
  report's left-shift, a separate record this unit does not write.
- GitLab's and GitHub's variable blocks: unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-94` — S1's locator, S3's next-line scalar test and §5's empty-block sentence, which S1 to S3 extend to a block list at the key's own indentation (id 24)
- **consumes-from** `TOOL-dLinkedLibrary-81` — S1's item reading at the list's own indentation and S3's precedence keeping 79 S2's `- group:` reason, which S1 feeds from the locator and AC1 reads (id 24)
- **hands-off** `TOOL-dLinkedLibrary-102` — S1's same-indent sequence start, which unit 102 observes over 81's and 82's column-0 trees with their own staged red (id 17)

## 4. Design

### Evidence

- 94 S1 (`2026-10-27-spec-TOOL-dLinkedLibrary-94.md`, S1) reads the next content line only "when that line
  is indented deeper than the key; otherwise the value is empty"; 94 §5's error row repeats it.
- 81's example (`2026-10-27-spec-TOOL-dLinkedLibrary-81.md:92-93`) is `variables:` at column 0 over `- ${{
  if eq(...) }}:` at column 0; 82's (`2026-10-27-spec-TOOL-dLinkedLibrary-82.md:80-81`) is `variables:`
  over `- template: release-vars.yml`, both at column 0.
- 79 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-79.md`, S2) names a `- group: <name>` item `group <name>`,
  and 79 AC2 reads `refused: unreadable credentials group release-vars`; 81 S3 keeps that reason.
- YAML 1.2 admits a block sequence as a mapping value at the key's own indentation; a line at that
  indentation opening anything else starts the next key.

### An Azure file under S1

```yaml
variables:                # S1: the next line sits at this indentation and opens `- `
- group: release-vars     # 81 S1 reads the item; 79 S2's reason
jobs:                     # ends the sequence
- job: publish
  steps:
  - script: ./publish.sh  # refused: unreadable credentials group release-vars
```

### Rollout

Order 35, one step after `TOOL-dLinkedLibrary-94`, beside `TOOL-dLinkedLibrary-91`, `-92` and `-93`. All
write `adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences the passes. If the pass adds a
function, it re-renders the generated map with `python tools/codebase-map/gen_map.py --write` where its
`--check` exits 1, then runs `python tools/lexicon/lexicon.py`, in the pass commit; a function it adds is
named after `python3 tools/lexicon/lexicon.py --suggest <name>`.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S5
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: the Rollout re-render

### Alternatives rejected

- **Reading a same-indent `- ` line as the value only when 81 S1 reads the block.** It keeps two readers
  answering "where is the value" for one key, the shape 94 S1 removed.
- **Refusing every `variables:` whose value does not start on a deeper line.** It refuses the house form
  81 and 82 plant, and every plain `- name:` list with it.

## 5. Production-readiness checklist

- security — closes a variable group, template or expression item escaping 79's, 81's and 82's refusals
  because the locator reads its list as empty; deny by default.
- perf / scale — unchanged: one look-ahead per `variables:` key.
- error / empty / loading states — a key followed by neither a deeper line nor a same-indent `- ` item is
  an empty block and refuses nothing.
- observability — each refusal keeps the reason 79, 81 or 82 names.
- risks — none new: the same-indent form is the one 81 and 82 already read.
- testing — S4's plants under `adopt_program.py --fixture`, S5's scratch copy.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — none under `help/`: no reason changes.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both jobs of
  S4's group tree read `refused: unreadable credentials group release-vars`.
  Red when: the locator reads the column-0 list as empty and the jobs read `importable`.
- **AC2** — When the same plant runs, both jobs of S4's `- name: CONFIG` tree read `importable`, and both
  jobs of 94 S4's tree whose `variables:` stands alone over `  {}` still read `importable`.
  Red when: a plain same-indent list or an empty flow value refuses its jobs.
- **AC3** — When the scratch copy of S5 runs the same plant by `python -I`, both jobs of S4's group tree
  print `importable`.
  Red when: the staged locator leaves the tree refused, so the plant does not discriminate S1.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 · the `ci-census` plant's column-0 group and name trees, the failing case staged by a locator that reads only a deeper line · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 92 to 96, id 24 (HIGH, item
  H3).

## 10. Reuse audit

The seam extended is 94 S1's locator and 81 S1's item reading inside `TOOL-dLinkedLibrary-8`'s `ci-job`
class in `tools/memory-tree/adopt_program.py`, with 79 S2's group reason reused unchanged. `python
tools/codebase-map/reuse_lookup.py "locate a yaml value on the line after its key including a same
indent list"` ranked `key`, `keys`, `same` and `read_conf_key`; `read_conf_key`
(`tools/check-spec-tokens.py`, `tools/roles/roles_lib.py`) reads a conf key and no YAML value, so no
existing seam fits beyond the locator being extended.

Recall terms used: `python tools/memory-recall/query.py "how does the census find a variables value written as a list at the key's own indentation" --terms "census ci-job azure variables locator same-indent block sequence group template refused importable"`
