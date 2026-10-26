# TOOL-dLinkedLibrary-14 — the code reader: `gov map code`, and `gov code show`, `callers`, `tests` and `where`, `git grep` its floor

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 17 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0251@23b8b8e1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-c.md) | research | TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-1 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 |

<!-- /gen:spec-records -->

## 1. Goal

The core `code` record holds every definition, range, call and test edge, and nothing reads it for
an agent: the research's spec writer made 80 code lookups and its builder 45, each a text search or
a file read (research-code-orientation.md:79-92, night pass point 3). This unit gives the record its
readers: `gov map code`, the level-1 view of the code namespace by kit, and `gov code show`,
`callers`, `tests` and `where`, the level-2 views of one definition, with `git grep` the engine of
`where` and the floor every other verb falls back to for a language with no extractor. The map's
level 0 holds one counted `code` line, TOOL-dTotalRecall-14 S8's.

## 2. Scope (IN)

The record is TOOL-dTotalRecall-8's: `derive_code_record(root, tree)`, which returns the cached rows
of a tree it has derived, and the tables `code_row`, `code_file`, `code_edge` (types `calls`,
`tests`, `mention`, `invokes`, `registers`) and `code_meta` (S2 to S7, S9). The level-1 form
`python gov_map.py <ns>[.<seg>]`, the namespace row's `map` field and the counted level-0 line are
TOOL-dTotalRecall-14's S2, S4 and S8. The namespace registry is PLAY-dOrderedCharter-19 S2's
`tools/playbook/namespaces.toml`, read by `read_namespaces`. All are DEFERRED at base `5fede642`
and are a build-run precondition; this unit re-specs none of them.

- **S1** — The reader, `tools/memory-tree/gov_code.py`, standing in for `gov code` as `gov_map.py`
  stands in for `gov map` (shared interface I17). Every verb reads the record through
  `derive_code_record` at HEAD's tree, never through SQL of its own, and resolves a target as §4
  "Targets" says. Exit 0 when it prints a finding, 1 printing `none — <target>` when the record
  holds nothing for it, 2 on a refusal (no record, a malformed target, an ambiguous target for a verb
  that needs one). Observed by AC1 to AC5.
- **S2** — `gov_code.py show <target>`: one line per definition the target resolves to,
  `<key> · <kind> · <path>:<line>-<end_line> · hash <first 8 hex>`, a file target listing every
  definition of that file in line order. Observed by AC1.
- **S3** — `gov_code.py callers <target>`: one `calls — <src key> · <path>:<line>` line per `calls`
  edge whose `dst` is the target's key, then one `mentions — <path>:<line> · <call text>` line per
  `mention` edge whose call text ends in the target's last name segment, the two kept apart because a
  mention is unresolved. Observed by AC2.
- **S4** — `gov_code.py tests <target>`: one `tests — <test path>:<line> · <src key>` line per
  `tests` edge into the target's key. Observed by AC3.
- **S5** — `gov_code.py where <word> [-- <pathspec>…]`: one `<path> · <n>` line per tracked file
  holding the word as a whole word, `<n>` its matches, from one call of `grep_words` (S7). It reads no
  record, so it answers for every language and for the population hunts no record answers.
  Observed by AC4.
- **S6** — The floor. When `code_meta.degraded` is set, `show`, `callers` and `tests` print
  `degraded — <reason> · gov code where <name>` and then `where`'s lines for the target's last name
  segment; when the target's file is one whose language `code_meta.languages` lists with the
  extractor `none` (TOOL-dLinkedLibrary-21 S5), they print `not extracted for <language> · gov code
  where <name>` and the same lines. The floor exits 0 when `where` finds the word and 1 when it does
  not. Observed by AC5.
- **S7** — The `git grep` primitive, `grep_words(root, words, pathspecs)`, lifted at its second
  instance from `build_open_asks_cited_by_product_source` (`tools/drift-audit/drift_report.py:2119`):
  one `git -C <root> grep -o -z -w -F -f - -- <pathspecs>` call with the words on stdin, returning
  `(hits, None)` with `hits` mapping each matched word to `{path: count}`, `({}, None)` on git's
  exit 1, and `(None, <git's last stderr line>)` on any exit above 1. Its canonical block
  `# >>> grep_words_py` … `# <<< grep_words_py` sits in `tools/lib/grep_words.py`; `gov_code.py`
  and `drift_report.py` each carry it inline under a new `PARITY_ROWS` row `grep_words_py` of
  `tools/lib/resolve-python.test.sh`, and drift's signal calls its copy with its verdict unchanged.
  Observed by AC4 and AC7.
- **S8** — `gov map code`. `render_code_map(record, kit=None)` in `gov_code.py` renders the code
  namespace at level 1: with no kit, one line per kit, `- code.<kit> — <files> files ·
  <definitions> definitions · gov map code.<kit>`; with a kit, one line per definition of that kit in
  TOOL-dTotalRecall-14's `line` grammar, `- <key> · <inbound calls> calls, <tests> tests`. It prints
  through `gov_code.py map [<kit>]`, and `gov_map.py code[.<kit>]` prints the same bytes: the `code`
  row of `namespaces.toml` carries `map = "fold"` and a new field `render =
  "gov_code:render_code_map"`, the `<module>:<function>` shape its `extractor` already takes, which
  `read_namespaces` admits and `gov_map.py`'s level-1 form calls for a row declaring it. Observed by
  AC6.
- **S9** — The fixture, `python gov_code.py --fixture --plant <case>`, its plants run together by
  `gov_code.py --selftest`: a scratch repository holding
  `a.py` (a function `f`, a class `Base` with a method `g`), `b.py` calling `f` and, through `eval`,
  `h`, `test_a.py` calling `f`, `x.go` defining `Run` under `memory.code-languages: builtin`, and a
  kit directory holding a `kit.toml`, its record derived by `code_record.py`. The plants are §6's.
  Observed by AC1 to AC6.
- **S10** — The page `help/code.md`: the five verbs, their line grammar, the floor and when it fires,
  and `gov_map.py code`; linked from `help/README.md` and from `help/code-languages.md`
  (TOOL-dLinkedLibrary-21 S8). Observed by AC8.

## 3. Non-goals (OUT)

- The `code` record, its derivation, freshness and bounds: TOOL-dTotalRecall-8's.
- The level-0 map, its counted `code` line, its budget and its cache: TOOL-dTotalRecall-14's S8,
  cited; this unit renders level 1 and level 2 only.
- A purpose on `show`'s line: TOOL-dLinkedLibrary-15 adds it.
- The per-item `code` slot and `memory.code-budget`: dBoundRoles'; TOOL-dLinkedLibrary-16 renders a
  slot for its replay only.
- Ranking `where`'s hits or reading a regular expression: `-F -w` over literal words is the floor
  the research measured (research-code-orientation.md:62), and a pattern search stays the shell's.
- A `gov` command: no `gov` CLI exists at base, and each `gov_*.py` stand-in is the form a later
  front door dispatches to.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-21` — `degraded`, with the per-language extractor `none`: the two record states in which S6 prints the floor and runs `where`
- **hands-off** `TOOL-dLinkedLibrary-15` — `gov_code.py`, whose `show` line gains the definition's purpose and its pending state
- **hands-off** `TOOL-dLinkedLibrary-16` — `gov_code.py`, its `derive_callers`, `derive_callees` and `derive_tests`, from which the replay's slot is rendered
- **hands-off** `TOOL-dLinkedLibrary-2` — `gov_code.py`, whose `callers` verb gives the house index each listed symbol's caller files
- **consumes-from** external — TOOL-dTotalRecall-8 S2 to S7 and S9 (the record), TOOL-dTotalRecall-14 S2, S4 and S8 (`gov_map.py`, the `map` field, the counted line) and PLAY-dOrderedCharter-19 S2 (`namespaces.toml`, `read_namespaces`), DEFERRED at base and built before this unit's pass
- **hands-off** `TOOL-dLinkedLibrary-46` — `code record selftest`, the leg that runs `gov_code.py --selftest`; this unit's ledger names it for the arm line (id 49)
- **hands-off** `TOOL-dLinkedLibrary-52` — `grep_words` and `show`, which unit 52 guards (ids 71, 72)

## 4. Design

### Evidence

- No code reader exists at base: `symbols.json` holds id, kind and file only
  (`tools/codebase-map/map_lib.py:1599-1625`), and `python_symbols` (`map_lib.py:318`) reads public
  module-level names; no caller index is committed (scout C, verified at base).
- The batched donor `tools/drift-audit/drift_report.py:2119` runs `git grep -o -z -w -F -f -` with
  the ids on stdin, reads exit 1 as no match and anything above it as git failing (`:2117-2126`),
  verified at base. Two other `git grep` calls, `tools/codebase-map/map_lib.py:878` (an `-E`
  marker scan) and `tools/branch-reconcile/branch_reconcile.py:488` (`-F -h` over one row at a ref),
  answer other questions and stay as they are.
- The research's verdict on candidate C: it "loses as the caller source" (`main`: 180 files against
  5 resolved callers) and "survives as the floor": 14 of the builder's 56 lookups were searches no
  map answers (research-code-orientation.md:91-92).

### Targets

| Target | Resolves to |
|---|---|
| `<path>::<qualified name>` | that definition key |
| `<path>` | every definition of that file, for `show`; a refusal for `callers` and `tests` |
| a bare name | every key whose last segment equals it; `callers` and `tests` refuse two or more, listing them |

### The lines

```
show       a.py::Base.g · method · a.py:4-6 · hash 3f9c2a71
callers    calls — b.py::main · b.py:7
           mentions — b.py:9 · h
tests      tests — test_a.py:3 · test_a.py::test_f
where      a.py · 2
floor      not extracted for go · gov code where Run
map        - code.memory-tree — 41 files · 612 definitions · gov map code.memory-tree
map <kit>  - tools/memory-tree/gov_code.py::show · 1 calls, 1 tests
```

### Inventory

Minted: `tools/memory-tree/gov_code.py` with `resolve_target`, `derive_callers`, `derive_callees`,
`derive_tests`, `render_code_map` and the verbs `show`, `callers`, `tests`, `where`, `map`;
`tools/lib/grep_words.py`, the block `grep_words_py` and its `PARITY_ROWS` row; the namespace field
`render`; `help/code.md`. Naming cells: each function asked of the lexicon's `--suggest` under
`--as py.function` at the pass.

### Migration

None. The reader is new, and drift's signal keeps its output.

### Rollout

Live at landing wherever the `code` record is built; with no record, every verb but `where` refuses
naming `code_record.py`.

### Files touched (estimate)

- `tools/memory-tree/gov_code.py` (new)
- `tools/lib/grep_words.py` (new)
- `tools/lib/resolve-python.test.sh`: the `grep_words_py` row
- `tools/drift-audit/drift_report.py`: the inline copy, the call, `KIT_DRIFT_AUDIT_VERSION` moved
- `tools/memory-tree/gov_map.py`: the level-1 form calls a declared `render`
- `tools/playbook/namespaces.toml`: the `code` row's `map` and `render`
- `tools/playbook/tag_index.py`: `read_namespaces` admits `render`
- `tools/memory-tree/check-memory-hygiene.sh`: `KIT_MEMORY_TREE_VERSION` moved
- `tools/memory-tree/README.md`
- `help/code.md` (new)
- `help/README.md`

### Alternatives rejected

- **A SQL reader of the index in `gov_code.py`.** A second reader of TOOL-dTotalRecall-8's tables
  beside `derive_code_record` is the copy the charter's `[reuse]` rule refuses.
- **`where` over `grep -r` or Python's own walk.** `git grep` reads only tracked files, honours the
  index, and is the engine the clause names.
- **`gov map code` rendered only by `gov_map.py`.** `gov_map.py` is built only on
  TOOL-dTotalRecall-17's `win` (TOOL-dTotalRecall-14 S1), so the level-1 view would vanish on a loss
  (§8 F1).

## 5. Production-readiness checklist

- security — read-only: the verbs read the record and run `git grep` with fixed flags, the words on
  stdin and the pathspecs after `--`, so no target reaches git as an option.
- perf / scale — one record read per verb from the cache; `where` is one `git grep`, 97 to 113 ms per
  query on gov's tree (research-code-orientation.md:62, PINNED 2026-10-18).
- error / empty / loading states — `none — <target>` on an empty answer, a refusal naming the
  missing record or the ambiguous candidates, and the floor when the record cannot answer.
- observability — the floor names why it fired; `where` prints counts per file.
- risks — a bare name shared by many definitions makes `callers` refuse; the refusal lists the keys
  to pass instead.
- testing — the plants of S9 and the parity row.
- migration — none.
- user docs — `help/code.md`, S10.

## 6. Acceptance criteria

- **AC1** — When `python gov_code.py --fixture --plant show` runs `show a.py::Base.g`, `show g` and
  `show a.py`, the first two print the one line `a.py::Base.g · method · a.py:<line>-<end> · hash
  <8 hex>` and the third prints `a.py::f` then `a.py::Base` then `a.py::Base.g`.
  Red when: a method is not found by its bare name, or a file target lists out of line order.
- **AC2** — When the plant `callers` runs `callers f`, it prints a `calls — b.py::<caller>` line and
  a `calls — test_a.py::test_f` line, and `callers h` prints only a `mentions —` line.
  Red when: an `eval` call is printed as a `calls —` line, or a resolved call is missing.
- **AC3** — When the plant `tests` runs `tests f` and `tests Base.g`, the first prints one
  `tests — test_a.py:<line>` line and the second prints `none — Base.g` and exits 1.
  Red when: a definition no test calls is reported tested.
- **AC4** — When the plant `where` runs `where f`, it prints `a.py`, `b.py` and `test_a.py` each with
  its count; and when `python drift_report.py --json` runs at the pass tip and at the pass base, the
  `open_asks_cited_by_product_source` signal's `value`, `of` and `detail` are equal in the two.
  Red when: a non-word match is counted, a git failure reads as no match, or drift's signal moves.
- **AC5** — When the plant `floor` runs `show x.go::Run`, it prints `not extracted for go · gov code
  where Run` and `x.go · 1`; with the record's `degraded` set by `code_record.py --ceiling 0.01`,
  `callers f` prints `degraded — time ceiling · gov code where f` and `where`'s lines.
  Red when: an unextracted file or a degraded record answers `none` without running `where`.
- **AC6** — When the plant `map` runs `gov_code.py map` and `gov_code.py map <kit>`, the first prints
  one `- code.<kit> —` line per kit with its file and definition counts and the second one line per
  definition of that kit; and `python gov_map.py code` and `python gov_map.py code.<kit>` print the
  same bytes, while `python gov_map.py` holds exactly one line starting `- code.* — `.
  Red when: the two renders differ, or level 0 carries more than one `code` line.
  fixture: `gov_map.py` exists only after TOOL-dTotalRecall-17's `win`; on a `lose` its two halves
  are §8 F1's route.
- **AC7** — When the `grep_words_py` block, from its opening marker line to its closing one, is cut
  from `grep_words.py`, `gov_code.py` and `drift_report.py` and the three cuts are compared with
  `cmp`, they are byte-identical, and a `grep -n "^grep_words_py|"` over the resolver suite finds the
  block's row in its `PARITY_ROWS` table.
  Red when: a copy differs from the canonical, or no parity row holds the block.
- **AC8** — When `grep -n "gov code where" code.md` runs over the help page, it finds the floor's
  section beside the five verbs, and `grep -n "code.md" README.md` over `help/` finds the link.
  Red when: the page omits a verb or the floor.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `drift-audit selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures`

New arm: tools/memory-tree/gov_code.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · `gov_code.py --selftest` run by the `code record` leg beside `code_record.py --selftest`, its failing case staged by a `callers` that reads `mention` edges as `calls` · none
New arm: tools/lib/resolve-python.test.sh · covers AC7 · the `grep_words_py` `PARITY_ROWS` row, staged by one byte changed in drift's copy · that suite's assertion count, raised by the row

## 8. Open questions

- **F1 — Where does `gov map code`'s render live, when `gov_map.py` is built only on a won replay?**
  TOOL-dTotalRecall-14 S1 holds the map renderer unbuilt on TOOL-dTotalRecall-17's `lose`. Options:
  (a) the level-1 code render in `gov_map.py`, absent on a loss; (b) the render in `gov_code.py` as
  `render_code_map`, printed by `gov_code.py map`, with `gov_map.py code` calling it through the
  namespace row's declared `render` when the map is built; (c) a second renderer in each file. (c)
  is two renders of one view. RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the most
  feature-rich survivor: the clause's level-1 view exists under either verdict, and `gov map code`
  prints it wherever `gov map` exists; I17 is refined to name `gov_code.py map` as the render and
  `gov_map.py code` as its map-side form. On a `lose`, the pass records the `gov map code` spelling
  carried by `gov_code.py map` alone as a deviation from cl-dClosedLoop-0251. widens: none ·
  relaxes: none
- **F2 — `grep_words`: extract a primitive, or call `git grep` inline again?** Options: (a) inline in
  `gov_code.py`, a second copy of drift's batched call; (b) extract the canonical block at this, its
  second instance, carried inline by both kits under a parity row; (c) import drift's function across
  kits. (a) is the copy the charter's `[reuse]` rule refuses at a second instance; (c) crosses a kit
  boundary a copy-installed adopter cannot follow. RESOLVED (agent, 2026-10-26, delegated): (b),
  rung 3, the `PARITY_ROWS` pattern of TOOL-dTotalRecall-8 S5. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 14, night pass point 3 items 4 and 6,
  research-code-orientation.md:85-112, TOOL-dTotalRecall-8 and TOOL-dTotalRecall-14, and scout C's
  row for cl-0251.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-46, TOOL-dLinkedLibrary-52, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.

## 10. Reuse audit

The seams extended: TOOL-dTotalRecall-8's `derive_code_record` and its tables, the one record this
reader reads; TOOL-dTotalRecall-14's `gov_map.py` level-1 form and the namespace row's `map` field,
which gains `render`; and drift-audit's batched `git grep` at `tools/drift-audit/drift_report.py:2119`,
extracted as `grep_words` at its second instance. `python tools/codebase-map/reuse_lookup.py "find
callers tests and definition of a symbol with git grep word search fallback"` ranked name stems
(`git`, `search`, `run_git`, `read_git_output`, `python_symbols`, `render_symbols_json`); none reads
callers or tests, so no existing seam fits the verbs themselves, and `python_symbols`
(`tools/codebase-map/map_lib.py:318`) reads public module-level names only. Scout C's lines agreed
with source at base (`drift_report.py:2119`, `map_lib.py:878`, `branch_reconcile.py:488`); its
"`gov map code` is `gov_map.py code`, not a new script" is refined by §8 F1, since `gov_map.py` may
never be built. The recall query returned scout C's rows and the walk record, nothing that reads the
record's edges.

Recall terms used: `python tools/memory-recall/query.py "how does an agent find the callers tests and definition of a code symbol" --terms "gov code show callers tests where git grep floor code record definition key degraded night pass"`
