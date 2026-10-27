# TOOL-dLinkedLibrary-18 — the region-parser factory in `tools/lib`, and every region parser re-pointed to it

**Status:** OPEN · rev-3 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 2 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0255@c0b78911 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-b.md) | research | TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-1 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 |

<!-- /gen:spec-records -->

## 1. Goal

Eighteen sites in eleven kits and three languages find a slice of text between two marker lines, and
they agree on no contract: `render_playbook.py` counts substrings, `check_roles.py` takes the first
`str.find`, govkit's selftest matches a substring anywhere in a line, and only the generator and the
unattended kit's awk readers hold column 0, one trailing CR and close-after-open (gap-mem-33, the
night pass's point 4). This unit lands one factory in `tools/lib` holding that contract, in Python,
shell and JavaScript, each copy-installed kit carrying it inline under a parity row, and re-points
every region parser the query of §4 returns to it, `check_roles.py`'s roles-catalogue region and
govkit selftest's hold-region scan among them beside the register's five.

## 2. Scope (IN)

- **S1** — The contract, shared interface I14 as §8 F1 settles it. A line IS a marker when, after one
  trailing CR is stripped, it equals the marker string exactly, the marker's own leading spaces
  included; a call that admits a label also takes the marker followed by one space and any text. A line
  that begins with the marker and is not one of those is MALFORMED and refused. A pair is exactly one
  open and one close, the close after the open; anything else is refused naming the marker and the rule.
  The case table of `tools/memory-tree/marker-contract.test.sh:198-207` is this contract, unchanged.
  Observed by AC1.
- **S2** — The Python factory, `tools/lib/region.py`, one block between `# >>> region_py -- canonical
  copy: region.py in the gov lib dir (byte-identical; gated)` and `# <<< region_py`: `RegionError`
  (a `ValueError`); `is_marker_line(line, mark, labelled=False)`; `find_pair(lines, open_mark,
  close_mark, labelled=False)` returning the two indexes; `read_region(text, open_mark, close_mark,
  labelled=False)` returning the lines between; `splice_region(text, open_mark, close_mark, body,
  labelled=False)` returning the text with `body` written between the markers and both markers kept byte for byte; `iter_regions(text,
  open_mark, close_mark, labelled=False)` returning every pair of a repeated, non-nested region in file
  order; and `iter_family(text, families)` returning every span of a marker FAMILY, a lead followed by
  a name `[A-Za-z0-9_.-]+` and an optional space-led tail, nesting by depth across every family given,
  refusing an orphan close, an unclosed open, a crossed pair and a close naming another name. Observed
  by AC1, AC2 and AC3.
- **S3** — The shell twin, `tools/lib/region.sh`: the block `region_sh` holding `region <file> <open>
  <close>` and `splice <file> <open> <close> <payload-file>`, each exit 3 on a malformed pair, the
  bodies of today's canonical (`tools/unattended/check-unattended.sh:211-216`) and of `splice`
  (`tools/unattended/unattended.sh:1328-1339`); the block `gen_region_awk` holding the one-line
  assignment `GEN_REGION_AWK='…'`, the gen family's strip, its two marker patterns anchored at the end
  of the line (§8 F3); and, outside both blocks, `region_nth <open> <close> <k> <file>`, the k-th
  labelled block printed whole, which only gov-internal suites source. Observed by AC1, AC4 and AC5.
- **S4** — The JavaScript twin, `tools/lib/region.js`: the block `region_js` between `// >>> region_js`
  and `// <<< region_js` holding `readMarkerRegion(text, openMark, closeMark)`, the lines between or
  `{ error }` naming the rule broken, on S1's contract. Observed by AC1.
- **S5** — The parity rows. `PARITY_ROWS` in `tools/lib/resolve-python.test.sh:168-187` gains
  `region_py`, `region_sh`, `gen_region_awk` and `region_js` rows, each canonical in `tools/lib`; the
  `kickoff_region` row is retired in their favour, its two copies renamed `region_sh`; and `blk` (:221)
  and the copy discovery (:226) read the `//` leader beside `#`, so a JavaScript copy is graded as a
  shell or Python one is. Observed by AC4.
  **Readers:** by name: `tools/lib/resolve-python.test.sh` (the `kickoff_region` row :170 and its
  comment :205), `tools/unattended/check-unattended.sh:210` and :217, `skills/session-kickoff/manifest-check.sh:1289`
  and :1296 · by value: `tools/lib/resolve-python.test.sh`'s copy discovery (:226), which greps the stem
  to find the copies it grades; `tools/codebase-map/map_lib.py`'s install-site scan (:860), which counts
  each stem's copies as fan-in.
- **S6** — The re-points, every site the query of §4 returns at the pass, the table of §4 "The
  population" being its reading at base. Each Python site inlines the `region_py` block once per kit
  module that reads a region and calls the factory; each keeps its own names and messages, so
  `apply_region`, `check_marker_line` and `_marker_index` in `tools/memory-tree/gen_build_index.py`
  become thin callers of `splice_region`, `is_marker_line` and `find_pair`. Each shell site carries the
  `region_sh` block in place of its own body, `unattended.sh`'s near-copy at :1310 among them; the
  unattended library carries `gen_region_awk`; `format-guard.js` carries `region_js`. Observed by AC6
  and AC7.
- **S7** — The census, `python tools/lib/region.py --census`, the query of §4 run over the tracked tree:
  it prints each region-parsing site outside the factory and its inline blocks as `<path>:<line> —
  <why>`, then `region census — <n> site(s) outside the factory`, exit 1 when `n` is not `0`. Observed
  by AC8.
- **S8** — The conformance suite. `tools/memory-tree/marker-contract.test.sh` grades the factory's three
  twins on its contract-1 case table, adds the family cases of S2 (orphan close, unclosed open, crossed
  pair, a close naming another name, a nested pair) for `iter_family` and for `GEN_REGION_AWK`'s strip,
  and its header's "why a conformance test and not a shared function" paragraph is rewritten: the
  function is now shared, and the suite proves its three languages agree. Observed by AC1 and AC5.
- **S9** — The kit versions of every kit whose engine file changes move one step with their `gov:kit`
  markers: memory-tree, playbook-render, roles, runlog, govkit, codebase-map, drift-audit, unattended,
  kickoff-manifest and agent-cap. NOT OBSERVED by a criterion here: the `kit version markers` leg
  observes it at the close.

## 3. Non-goals (OUT)

- A marker FIND that reads no region: `render_playbook.py`'s `REGION_MARKER_RE.search(v)` (:885) asks
  whether a value carries a marker, and `tools/govkit/matrix.py:834` asks whether a file carries one.
  Neither slices text, and the census of S7 does not count them.
- The `gov:note`/`gov:end <tag>` span rule: TOOL-dLinkedLibrary-17 reads it from `iter_family` and
  `read_region`; this unit builds the verdicts, not that grammar.
- The legacy block's marker pair, `<!-- gov:legacy src=<path> -->`: TOOL-dLinkedLibrary-23 writes it
  through `splice_region`.
- Changing what any region holds, or any marker's spelling. The govkit hold markers stay indented, read
  as indented markers (S1).
- `deviation_join.py`'s reader of `GEN_REGION_AWK` (`read_gen_region_awk`, `tools/memory-tree/deviation_join.py:357`): it
  reads the assignment from the unattended library as today, and that line is now the factory's copy.

### Edges

- **hands-off** `TOOL-dLinkedLibrary-17` — `read_region`, with `iter_family`'s orphan, unclosed, crossed and mismatched verdicts, the contract its `gov:end <tag>` span refusals apply
- **hands-off** `TOOL-dLinkedLibrary-23` — `read_region` and `splice_region`, the contract its legacy block is read and written through
- **hands-off** `TOOL-dLinkedLibrary-41` — `iter_family`, whose depth origin unit 41 pins with a family case (id 4)
- **hands-off** `TOOL-dLinkedLibrary-43` — `region.py --census`, whose predicate unit 43 states and whose population it completes; this unit's ledger answers AC8 citing it (id 20)
- **hands-off** `TOOL-dLinkedLibrary-45` — `find_pair` and `splice_region`, through which unit 45 re-points govkit's `find_block` (id 30)
- **hands-off** `TOOL-dLinkedLibrary-52` — `splice_region`, which unit 52 makes refuse a body holding its own marker (id 78)
- **hands-off** `TOOL-dLinkedLibrary-54` — `region_sh`, the block unit 54 carries inline in `tools/check-microformats.sh` (id 3 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-56` — `region_nth`, which unit 56 wraps in its own parity-gated block for `tools/run-gates/run-gates.test.sh` (id 17 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-64` — `region_py` and the MALFORMED prefix test, which unit 64 applies to `find_block` and `splice_region` (ids 32, 33 of the spec audit of units 37 to 53)

## 4. Design

### The population

The query is the two commands below, run over the tracked tree; a hit inside `tools/lib/region.*` or
inside a `region_py`, `region_sh`, `gen_region_awk` or `region_js` block is the factory, not a site.

```bash
# Python and JavaScript: a module-level marker constant, a string opening `<!--` or `#`, used as the
# argument of a string method (find, rfind, index, count, split, startswith, endswith, partition,
# indexOf) or as an operand of `in`, `not in` or `==` — read with `ast` for Python, a regex for JS.
git grep -nE "^[A-Z_]*(OPEN|CLOSE|BEGIN|END|MARK)[A-Z_]*(, [A-Z_]+)? *= *['\"](<!--|#)" -- 'tools/*' 'skills/*'
# Shell and awk: a marker test written `index(ln, o) == 1`, a `GEN_REGION_AWK=` assignment, and a
# `>>> ` opener read by a regex.
git grep -nE "index\(ln, ?[oc]\) ?== ?1|^GEN_REGION_AWK=|\^# >>> |\(\?:#\|//\) >>> " -- 'tools/*' 'skills/*'
```

Its reading at base `5fede642`, every site verified at the line cited:

| Site | Contract today | Re-pointed to |
|---|---|---|
| `tools/memory-tree/gen_build_index.py` `apply_region` :1874, `check_marker_line` :2166, `_marker_index` :2178 | column 0, one CR, one pair, order | `splice_region`, `is_marker_line`, `find_pair` |
| `tools/playbook/render_playbook.py` `build_region` :757-776 | substring count, no order check | `find_pair` and `splice_region`; an absent pair still appends |
| `tools/playbook/render_playbook.py` :1836 | a regex split around the pair | `find_pair`, the text outside it |
| `tools/playbook/render_playbook.py` `check_one_line_regions` :698 | `.strip()`, so indented; nesting refused | `iter_regions` |
| `tools/playbook/render_playbook.py` `check_fences` :582, `remove_fenced` :613 | a regex over `kit:` and `when:`, whitespace tolerated, one stack | `iter_family` over both families |
| `tools/roles/check_roles.py` :114, `check_catalogue_region` :148-152, the write :392-395 | first `str.find`, no doubled check | `read_region`, `splice_region` |
| `tools/roles/roles_lib.py` :212-215 | `find` and a count of one, else the whole text | `find_pair`; no pair keeps the whole text, a malformed pair is a `RolesError` |
| `tools/roles/roles_lib.py` :260-262 | `in lines`, `lines.index` | `read_region` |
| `tools/runlog/prose.py` :63-65 | `in lines`, `lines.index`, no CR | `read_region` |
| `tools/govkit/selftest.py` `scan_hold_region` :1539-1560 | substring in a line, indented and labelled markers | `find_pair` with the indented marks, `labelled=True` |
| `tools/codebase-map/map_lib.py` `_INSTALL_MARKER_RE` :860 | `^\s*(#\|//) >>> name`, openers only | `iter_family` over the `# >>> `/`# <<< ` and `// >>> `/`// <<< ` families |
| `tools/drift-audit/drift_report.py` `_GEN_MARK` :1821, :1917 | the first line opening `<!-- gen:` | `iter_family`, the first span's open line |
| `tools/unattended/check-unattended.sh` `region` :210-217 | the canonical, column 0, exit 3 | the `region_sh` copy |
| `skills/session-kickoff/manifest-check.sh` :1289-1296 | a parity copy of it | the `region_sh` copy |
| `tools/unattended/unattended.sh` `region` :1310, `splice` :1328 | a near-copy outside any marker, so parity never saw it | the `region_sh` copy |
| `tools/unattended/lib-unattended.sh` `GEN_REGION_AWK` :1136 | a regex family strip, unanchored at the end | the `gen_region_awk` copy |
| `tools/lib/resolve-python.test.sh` `blk` :221 | a prefix regex, the k-th block | `region_nth`, sourced from `tools/lib/region.sh` |
| `tools/hooks/format-guard.js` :187-189 | `indexOf` of an exact line, close after open | `readMarkerRegion` |

### The factory, in one place

```python
# >>> region_py -- canonical copy: region.py in the gov lib dir (byte-identical; gated)
class RegionError(ValueError): ...
def is_marker_line(line, mark, labelled=False): ...      # one trailing CR stripped, then == mark,
                                                          # or startswith(mark + " ") when labelled
def find_pair(lines, open_mark, close_mark, labelled=False): ...   # -> (o, c) or RegionError
def read_region(text, open_mark, close_mark, labelled=False): ...
def splice_region(text, open_mark, close_mark, body, labelled=False): ...
def iter_regions(text, open_mark, close_mark, labelled=False): ... # -> [(o, c), …]
def iter_family(text, families): ...   # families: [(open_lead, close_lead, tail | None), …]
                                        # -> [Span(family, name, open, close, depth), …]
# <<< region_py
```

The factory exports no marker constants. Shared interface I14 proposed `REGION_OPEN` and
`REGION_CLOSE` in `region.py`; a default pair would be a guess at every caller's markers, so the two
names stay what the clause uses them for, each consumer's own constant pair (`render_playbook.py:121`,
`check_roles.py:114`), and the census query reads them. I14's `apply_region(text, open, close, body)`
is spelled `splice_region` here: `tools/memory-tree/gen_build_index.py:1874` already defines an
`apply_region` with another signature, which the marker-contract suite calls, and an inline block
defining the same name in that module would shadow it; `splice_region` also matches the shell twin's
`splice`.

`tail` pins what follows the name: `" -->"` for the HTML-comment families, `None` for the copy
families, whose openers carry a free label. A Python consumer that already defines one of these names
is refused by the census, so the block never shadows a local; at base no tracked file defines any of
them (`git grep -nE "def (read_region|splice_region|find_pair|iter_regions|iter_family|is_marker_line)\b"`
prints nothing).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/lib/region.py`, `tools/lib/region.sh`, `tools/lib/region.js` | canonical files | none |
| `RegionError`, `is_marker_line`, `find_pair`, `read_region`, `splice_region`, `iter_regions`, `iter_family` | Python | `py.function`, asked at the pass |
| `region_nth` | shell function | `sh.function`, asked at the pass |
| `readMarkerRegion` | JS function | `js.function`, asked at the pass |
| `region_py`, `region_sh`, `gen_region_awk`, `region_js` | parity stems | none |
| `--census` | flag of `region.py` | none |

### Migration

None for data. A malformed marker a lenient reader accepted today is refused after the re-point, naming
the marker and the rule. The census and AC6 run each re-pointed reader over every tracked file it reads
at the pass, so a refusal the tree would meet is found by the build, not at an adopter.

### Rollout

The factory and its parity rows first, then the re-points kit by kit, each commit leaving the parity
suite green. Live at landing.

### Files touched (estimate)

- `tools/lib/region.py`, `tools/lib/region.sh`, `tools/lib/region.js`: S2 to S4, S7
- `tools/lib/resolve-python.test.sh`: S5 and the census arm
- `tools/memory-tree/marker-contract.test.sh`: S8
- `tools/memory-tree/gen_build_index.py`, `tools/memory-tree/check-memory-hygiene.sh`
- `tools/playbook/render_playbook.py`
- `tools/roles/check_roles.py`, `tools/roles/roles_lib.py`
- `tools/runlog/prose.py`, `tools/runlog/runlog_lib.py`
- `tools/govkit/selftest.py`, `tools/govkit/govkit.py` (`KIT_GOVKIT_VERSION`)
- `tools/codebase-map/map_lib.py`
- `tools/drift-audit/drift_report.py`
- `tools/unattended/check-unattended.sh`, `tools/unattended/unattended.sh`, `tools/unattended/lib-unattended.sh`
- `skills/session-kickoff/manifest-check.sh`
- `tools/hooks/format-guard.js`, `tools/hooks/agent-cap.js` (`KIT_AGENT_CAP_VERSION`)

### Alternatives rejected

- **A conformance suite and no shared code**, today's choice in `marker-contract.test.sh`'s header: it
  proves four readers agree and leaves eleven others outside it; the parity rows make a shared function
  legal across kits, which is the reason the header gave for not having one.
- **Python only, the shell and JS readers left as they are.** The three awk copies are the contract's
  origin and the copy whose absence once truncated a run-state file; leaving them outside the factory
  keeps two spellings of one predicate.

## 5. Production-readiness checklist

- security — `splice_region` is the write half: it refuses a malformed pair before writing, so a
  doubled or transposed marker can no longer truncate a file in any of the readers that used to accept
  one (`build_region`, `check_roles`' write).
- perf / scale — one pass over the lines per call, as each reader does now; the census reads the tracked
  tree once.
- error / empty / loading states — every refusal names the marker and the rule broken; an absent pair is
  `RegionError` where a reader had a fallback, and the reader keeps its fallback by catching it.
- observability — the census prints each site outside the factory and a count line.
- risks — a reader that tolerated an indented or doubled marker now refuses it; AC6 runs each over the
  tree first. The unattended kit's suites are waived for this landing (README rule 8), so the
  `unattended.sh` and `check-unattended.sh` re-points are observed by AC7's probe, not by those suites.
- testing — AC1 to AC8 by a pass; the arms of §7 at the close.
- migration — §4.
- user docs — no page under `help/` covers marker regions.

## 6. Acceptance criteria

- **AC1** — When a probe feeds the ten contract-1 cases of the marker-contract suite to `region.py`'s
  `read_region`, to `region.sh`'s `region` and to `region.js`'s `readMarkerRegion` by a probe of the
  three files, each accepts the `column-0` case and refuses the other nine, and the three agree on
  every case.
  Red when: any twin accepts an indented, trailing-text, unpaired, reversed or doubled pair.
- **AC2** — When `python -c "import sys; sys.path.insert(0, 'tools/lib'); import region; …"` calls
  `iter_family` over a text with `<!-- gen:a -->`, `<!-- gen:b -->`, `<!-- /gen:b -->`,
  `<!-- /gen:a -->`, it returns two spans, `b` at depth 2; over the same text with the two closes
  swapped it raises `RegionError` naming the crossed pair; over an orphan `<!-- /gen:c -->` it raises
  naming the orphan.
  Red when: a crossed, orphan or unclosed family marker is returned as a span.
- **AC3** — When `splice_region` is called over a text whose open marker appears twice, it raises and the
  input is not written; with one pair it replaces only the slice, both markers kept byte for byte.
  Red when: a doubled pair is spliced, or a byte outside the slice moves.
- **AC4** — When `region_nth '# >>> region_py' '# <<< region_py' 1 <file>` from `region.sh`
  prints the block of the canonical and of every copy the parity discovery finds, all are byte-identical,
  and after a one-byte edit inside the `region_js` block of a scratch copy of `format-guard.js` the
  JavaScript comparison differs; `git grep -n "kickoff_region" -- tools skills` prints nothing.
  Red when: a copy differs from its canonical, a JS copy is not found by the discovery, or the old stem
  survives.
- **AC5** — When `GEN_REGION_AWK` from `tools/unattended/lib-unattended.sh` and `iter_family` strip the
  same README carrying the nested `build-index` and `build-units` pairs, both leave the same authored
  lines; a gen marker carrying trailing text is kept as content by the strip and refused by
  `iter_family`, the one difference the case table pins.
  Red when: the two strips disagree on a well-formed README.
- **AC6** — When each re-pointed Python reader runs over the tracked files it reads at the pass —
  `python tools/memory-tree/gen_build_index.py --check`, `python tools/roles/check_roles.py`,
  `python tools/playbook/render_playbook.py --check`, `python tools/codebase-map/gen_map.py --check` —
  each exits as it did at base, and `scan_hold_region` returns the same `(sites, unmarked, explicit)` over
  `tools/govkit/govkit.py` as at base.
  Red when: a re-pointed reader refuses a file the tree holds, or a verdict moves.
- **AC7** — When a probe slices the `region_sh` block out of `tools/unattended/unattended.sh`,
  `tools/unattended/check-unattended.sh` and `skills/session-kickoff/manifest-check.sh`, sources each
  alone in a fresh `bash`, and calls its `region` over a fixture README holding the units pair, all three
  print the same slice, and each exits 3 over the same README with the pair reversed.
  Red when: a copy differs from the canonical, or one exits 0 on a reversed pair.
- **AC8** — When `python region.py --census`, run from `tools/lib`, runs at the pass tip, it prints `region census —
  0 site(s) outside the factory` and exits 0; over a scratch copy of the tree with one planted
  `FOO_OPEN = "<!-- foo -->"` and a `text.find(FOO_OPEN)` in a tool module, it exits 1 naming that line.
  Red when: the planted parser is not found, or a site of §4's table is still outside the factory.
  figure: DERIVED at the pass; eighteen sites at `5fede642`.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `marker contracts` · `manifest-check self-test` · `agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `routed-commits selftest` · `pre-push run-log line` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor arms` · `drift-audit selftest` · `runlog selftest` · `run-gates run-log line` · `hook destinations self-test` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `roles catalogue` · `unattended kit gate` · `build-index selftest` · `kit version markers` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lib/resolve-python.test.sh · covers AC4 AC8 · the four new parity rows and the census, the failing cases a one-byte edit in the `region_js` copy and a planted marker find outside the factory · none

New arm: tools/memory-tree/marker-contract.test.sh · covers AC1 AC5 · the factory's three twins and the family cases, the failing case a twin accepting a reversed pair · none

## 8. Open questions

- **F1 — Which contract do the disagreeing readers settle to?** Options: (a) the generator's and the
  awk readers' column-0 exact line, one CR, one pair, close after open, a marker-prefixed line refused,
  with a `labelled` admission for the two marker shapes that carry a label (govkit's hold markers and the
  canonical-copy openers); (b) the substring readers' leniency, so no reader's verdict moves; (c) (a)
  with indentation tolerated. (b) keeps the doubled-marker truncation `marker-contract.test.sh`'s header
  records, a veto-3 widening of a write surface. (c) re-admits the indented marker the case table refuses
  because a reader rewrote a line the author wrote. (a) is the table every awk reader already passes.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes:
  none
- **F2 — Does the factory serve family readers and repeated regions, or single pairs only?** Options:
  (a) single pairs only, the family and repeated readers left outside; (b) `iter_regions` and
  `iter_family` beside the pair functions. The register's five include `map_lib.py`'s opener scan and
  `resolve-python.test.sh`'s `blk`, which read families and repeated blocks, so (a) leaves two of the five
  the clause names unre-pointed (veto 1). Recommendation (b). Rung 1, the clause's "the register's five".
  RESOLVED (agent, 2026-10-26, delegated): (b). widens: none · relaxes: none
- **F3 — How is `GEN_REGION_AWK` re-pointed when another kit reads its text?** `deviation_join.py`
  reads exactly one single-line `GEN_REGION_AWK='…'` assignment from the unattended library
  (`deviation_join.py:357`). Options: (a) the assignment becomes the factory's `gen_region_awk`
  block, copied into the library under a parity row, so its reader is untouched; (b) the strip moves into
  a shell function and `deviation_join.py` calls the Python `iter_family`, a change to a parent build's
  instrument design (P0.1 row 8a); (c) it stays outside the factory. (c) fails the clause's "every region
  parser" (veto 1); (b) changes dTrueNorth's join for no gain (a) lacks. Recommendation (a), its two
  patterns end-anchored so a trailing-text marker reads as content, as AC5 pins. Rung 3. RESOLVED
  (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F4 — Is the JavaScript reader in the population?** `format-guard.js` holds the microformats pair as
  `FENCE_OPEN`/`FENCE_CLOSE` and slices by `indexOf`. Options: (a) a JS twin with a `region_js` parity
  row, `blk` reading the `//` leader `map_lib.py`'s scan already reads; (b) leave it, the parity table
  being `#`-only today. (b) leaves a marker-pair find the query returns (veto 1). Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F5 — Is the census a standing arm or a one-time probe?** Options: (a) a probe AC8 runs once; (b) an
  arm of the parity suite that already grades the factory's copies. (a) lets the next hand-rolled
  `str.find` of a marker pass every gate, the class the charter's `[class]` rule names; (b) is the same
  mechanism as S5, the factory's parity over its population. Recommendation (b). Rung 3. RESOLVED
  (agent, 2026-10-26, delegated): (b). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 18, gap-mem-33, the brief's I14, and scout
  B's row 18, every site re-read at base `5fede642` and four more found by the query of §4.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-41, TOOL-dLinkedLibrary-43, TOOL-dLinkedLibrary-45, TOOL-dLinkedLibrary-52, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-54, TOOL-dLinkedLibrary-56, TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seams extended are the awk `region` and `splice` contract (`tools/unattended/check-unattended.sh:210-217`,
`tools/unattended/unattended.sh:1310-1339`), the generator's `check_marker_line` and `apply_region`
(`tools/memory-tree/gen_build_index.py:2166`, :1874), the case table that pins them
(`tools/memory-tree/marker-contract.test.sh:198-207`), and the canonical-copy route with its parity
table (`tools/lib/resolve-python.test.sh:160-226`, rows at :168-187), which `compare_base_py` and `health_log_py` already
travel. `python tools/codebase-map/reuse_lookup.py "read the lines between an opening and a closing
marker line and refuse a doubled or reversed pair"` ranked name stems (`read`, `read_text`, a test
helper `pair`, `read_conf`), none a region reader; scout B's runs found `region` in
`check-unattended.sh`, `apply_region` in `gen_build_index.py`, `marker_pair` in `govkit.py` and
`check_gen_region_only` in `lib-unattended.sh`, and missed the rest, so the population of §4 comes from
the query, not the lookup. Scout B's table placed `kickoff_region`'s canonical at
`check-unattended.sh:211` (verified) and did not list `render_playbook.py:1836`'s split,
`check_fences`, `remove_fenced` or `iter_regions`' need in `check_one_line_regions`, which §4 adds.
The recall query returned scout B's row 18, TOOL-aMouldedFolio-4 (the unit that proved one contract
across four readers and wrote the case table S1 adopts) and TOOL-aPromptedMandate-14 (the open-coded
copy that survived beside them), which is the recurrence S7's census closes.

Recall terms used: `python tools/memory-recall/query.py "one shared reader for marker-delimited regions across shell python and javascript" --terms "region marker pair REGION_OPEN REGION_CLOSE apply_region kickoff_region parity canonical copy marker-contract column-0"`
