# TOOL-dTotalRecall-13 — the shared extraction primitive in `tools/lib`, which the map and the lexicon each call

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 2 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0224@bfb0a85c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-12 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-1 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-16 TOOL-dTotalRecall-25 TOOL-dTotalRecall-5 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-22 TOOL-dTotalRecall-3 TOOL-dTotalRecall-2 TOOL-dTotalRecall-7 TOOL-dTotalRecall-11 TOOL-dTotalRecall-10 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-9 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-20 TOOL-dTotalRecall-17 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-26 TOOL-dTotalRecall-12 |

<!-- /gen:spec-records -->

## 1. Goal

Move the definition extraction the lexicon owns today, its Python reader and its shell and JavaScript
tokenizers, into one canonical primitive in `tools/lib`, `tools/lib/extract_code.py`, that reads the
working tree, the staging index or a revision, and that each copy-installed kit carries inline as a
byte-identical copy. The codebase map then stops importing the lexicon kit for its shell layer, the
drift-audit copy of the batched blob reader retires, and the map's own comment-and-string lexer lives
in the same primitive, so one module holds every tokenizer (LX-2, gap-mem-04).

## 2. Scope (IN)

- **S1** — The canonical block `# >>> extract_code — canonical copy` … `# <<< extract_code` in
  `tools/lib/extract_code.py`, holding, moved verbatim from `tools/lexicon/lexicon.py` at base: `ext_of`
  (`:417`), `_python_defs` (`:425`), `scan_shell_tokens` (`:469`), `parse_shell_defs` (`:747`), the
  TypeScript helpers and `scan_ts_tokens` (`:950`), `parse_ts_defs` (`:1693`), `parse_ts_source`
  (`:1739`), `parse_tsx_defs` (`:2134`), `PARSERS` (`:2149`), `PATTERN_SETS` (`:142`), `_probe_defs`
  (`:2179`), `resolve_extractor` (`:2192`) and `extract_text` (`:2222`), with `extract_text(src, mode,
  pset, *, sets=None)` keeping its signature. Observed by AC1 and AC2.
- **S2** — The state reader `read_defs_at(root, state, paths=None, cache=None, *, armed=None,
  sets=None)` in the block, generalising `read_defs_at_sha` (`tools/lexicon/lexicon.py:4113`):
  `state` is `worktree`, `index` or a revision, per §4 "The states". Observed by AC3 and AC7.
- **S3** — The copies: `tools/lexicon/extract_code.py` and `tools/codebase-map/extract_code.py`, each
  carrying the block byte for byte, held by a new `PARITY_ROWS` row `extract_code` in
  `tools/lib/resolve-python.test.sh` whose canonical is `tools/lib/extract_code.py`. Observed by AC1.
- **S4** — The lexicon calls its copy: `tools/lexicon/lexicon.py` imports every moved name from its own
  `extract_code.py` by an explicit list, underscore names included, so `lexicon.extract_text`,
  `lexicon.ext_of` and every other moved name still resolve on the module; `read_defs_at_sha` keeps its
  signature as a thin adapter over `read_defs_at`. Observed by AC2.
- **S5** — The map calls its copy: `scan_shell_layer` in `tools/codebase-map/map_extractors.py:295`
  imports `parse_shell_defs` from the codebase-map kit's own `extract_code.py`, and the
  `resolve_kit_dir("lexicon", …)` lookup at `:309` and the import at `:314` retire. Observed by AC4.
  **Readers:** by name: `from lexicon import parse_shell_defs` is spelled at
  `tools/codebase-map/map_extractors.py:314` only (`git grep` at base) · by value: NO VALUE READERS —
  the import yields a function, and the shell layer's rows are what its readers compare, unchanged.
- **S6** — The map's lexer moved into the primitive: `_LEX_PROFILES`, the three `_PROFILE_*` rows,
  `_DATA_EXTS`, `DEFINITION_CARRYING_EXTS`, `_TRIPLE_QUOTES`, `_PY_PREFIX_CHARS`, `_IDENT_TOKEN_RE` and
  `_identifier_tokens` (`tools/codebase-map/map_lib.py:642-818`) move into the block; `map_lib.py`
  imports them from its kit's `extract_code.py`, so `map_lib._identifier_tokens` still resolves.
  Observed by AC6.
  **Readers:** by name: `_identifier_tokens` at `tools/codebase-map/map_lib.py:948`,
  `tools/codebase-map/selftest.py:1692` and `:1748`; `_LEX_PROFILES` at `map_lib.py:714`;
  `DEFINITION_CARRYING_EXTS` at `map_lib.py:853` · by value: the reference index
  `build_reference_index` (`map_lib.py:902`) and `fan_in` (`:960`), whose token sets are unchanged.
- **S7** — The drift-audit copy retires: `_read_defs_at_sha` (`tools/drift-audit/drift_report.py:1387`)
  is deleted and its two callers (`:1527`, `:1528`) call `lex.read_defs_at_sha(ctx.root, sha, armed,
  sets)` through the lexicon module they already import (`:1278`). Observed by AC5.
  **Readers:** by name: `_read_defs_at_sha` at `tools/drift-audit/drift_report.py:1527` and `:1528`,
  and the docstring of `read_defs_at_sha` at `tools/lexicon/lexicon.py:4118` · by value: the
  `lexicon marginal offense rate` signal's two operands, `at_base` and `at_head`.
- **S8** — The kit versions move with their shipped bytes: `KIT_LEXICON_VERSION` in `lexicon.py`, the
  codebase-map kit's `KIT_CODEBASE_MAP_VERSION` (`map_lib.py:49`) and drift-audit's
  `KIT_DRIFT_AUDIT_VERSION` (`drift_report.py:95`). NOT OBSERVED by a criterion: the
  `kit epoch (shipped bytes move, the version moves)` leg grades it at the close.

## 3. Non-goals (OUT)

- Definition context, the enclosing class, bases resolved through imports and decorators with aliases
  resolved (lexicon.md:421-427): dMindYourWords' (cl-dClosedLoop-0273), which extends this primitive.
- Line ranges, body hashes and call sites: TOOL-dTotalRecall-8 adds them to the block for the `code`
  record.
- Re-implementing `_identifier_tokens` over the lexicon's tokenizers for the languages both read: a
  behaviour change to the map's ranking that no clause asks for (§8 F2).
- Changing what any extractor returns. Every moved function keeps its bytes and its output.
- The map's other dependency on the lexicon, its `lexicon-verbs` inventory: it stays (lexicon.md:440).
- `tools/memory-tree/tree_lib.py`'s `read_blobs_at`, the memory-tree kit's own revision reader: a
  different kit's reader of record text, not of definitions.

### Edges

- **hands-off** `TOOL-dTotalRecall-8` — `extract_code.py`, the block and `read_defs_at`, which unit 8 extends with ranges, body hashes and calls and copies into the memory-tree kit
- **hands-off** external — dMindYourWords (cl-dClosedLoop-0273) calls this primitive and extends it with definition context
- **hands-off** `TOOL-dTotalRecall-43` — `BUILTIN_ARMED` and `read_defs_at`'s worktree ids, which that unit changes for the round-1 audit's ids 18 and 48

## 4. Design

### The block

The canonical file opens with a short header outside the markers, naming itself the canonical and
the parity row; the markers wrap everything a caller reaches. Each kit copy carries its own header and
the identical block. The parity arm cuts the block with `blk` (`tools/lib/resolve-python.test.sh:213`)
and finds copies with `git grep -l "^# >>> extract_code" -- '*.py'` (`:218`), so no extractor change
is needed: a new row is the whole join.

```
extract_code|$ROOT/$KIT_REL/extract_code.py|$KIT_REL/extract_code
```

The block imports only the standard library (`ast`, `hashlib`, `re`, `subprocess`), since a
copy-installed kit carries no `tools/lib` at an adopter.

### The states

| `state` | Paths and blob ids | Text |
|---|---|---|
| `worktree` | `git ls-files -s -z` (gitlinks skipped) | each file's bytes from disk; the blob id is git's own, `sha1(b"blob %d\0" % len + bytes)`, computed in Python with no spawn |
| `index` | `git ls-files -s -z` | one `git cat-file --batch` over the ids not in `cache` |
| a revision | `git ls-tree -r -z <rev>` | one `git cat-file --batch`, as `read_defs_at_sha` reads today |

The return is `{path: (blob, triple)}`, `triple` the `(functions, types, imports)` of `extract_text`,
for every path whose extension `armed` maps; `armed` defaults to `BUILTIN_ARMED`, the four parsers
by extension (`py` `python-ast`; `sh` and `bash` `shell-tokens`; `js`, `mjs`, `cjs` and `ts`
`ts-tokens`; `tsx` and `jsx` `tsx-tokens`), each under `parser`. A blob its extractor cannot parse
yields the empty triple, the fail-closed rule `read_defs_at_sha` states. A failed git call returns
`None`, which is not an empty tree. `cache` maps `(blob, ext)` to the triple, so a blob shared by two
states is parsed once.

`read_defs_at_sha(root, sha, armed, sets, paths=None, cache=None)` in `lexicon.py` becomes:

```python
got = read_defs_at(root, sha, paths, cache, armed=armed, sets=sets)
return None if got is None else {(rel, nm) for rel, (_b, t) in got.items() for nm, _ln in t[0]}
```

Its cache changes from names to triples, held per call as today.

### The callers

| Caller | Before | After |
|---|---|---|
| `tools/lexicon/lexicon.py` | defines the parsers | imports them from `extract_code` |
| `tools/codebase-map/map_extractors.py:314` | `from lexicon import parse_shell_defs`, after resolving the lexicon kit | `from extract_code import parse_shell_defs`, its own kit |
| `tools/codebase-map/map_lib.py:642-818` | defines the profile lexer | imports it from `extract_code` |
| `tools/drift-audit/drift_report.py:1387` | its own batched reader | `lex.read_defs_at_sha` |

`map_extractors.py` imports the codebase-map kit's module by the directory `map_lib` is loaded from,
which the shell layer already holds on `sys.path`.

### Inventory

Minted: `tools/lib/extract_code.py`, `tools/lexicon/extract_code.py`,
`tools/codebase-map/extract_code.py`, the block `extract_code`, `read_defs_at`, `BUILTIN_ARMED`, the
`PARITY_ROWS` row `extract_code`. Naming cells: `read_defs_at` is asked of the lexicon's `--suggest`
under `--as py.function` at the pass.

### Migration

None for an adopter's records or confs. A copy-installed adopter receives the two kit copies on its
next `govkit update`; the copy-install runbook copies the kit directory whole, so the file travels
with it.

### Files touched (estimate)

- `tools/lib/extract_code.py` (new)
- `tools/lexicon/extract_code.py` (new)
- `tools/codebase-map/extract_code.py` (new)
- `tools/lexicon/lexicon.py`
- `tools/codebase-map/map_extractors.py`
- `tools/codebase-map/map_lib.py`
- `tools/drift-audit/drift_report.py`
- `tools/lib/resolve-python.test.sh`

### Alternatives rejected

- **Keep the map importing the lexicon kit.** The clause has the map call the primitive, and
  KN-1 with `TOOL-dClosedLexicon-12` hold that neither kit requires the other (lexicon.md:428-431).
- **One `extract_code` block inside `lexicon.py` and `map_lib.py`.** A whole-file copy keeps both host
  modules readable and makes the copy one file a kit ships under its `include = "**"` rule
  (`tools/lexicon/kit.toml`), with the same parity row.
- **Import the canonical from `tools/lib`.** `tools/lib` ships nothing, so an adopter's copy-installed
  kit cannot reach it.

## 5. Production-readiness checklist

- security — no new write path or spawn class: the reader runs the same `git ls-tree`, `ls-files` and
  `cat-file --batch` the lexicon runs today.
- perf / scale — at most two spawns per state read, as today; the worktree state hashes in Python
  with no spawn per file.
- error / empty / loading states — a failed git call returns `None`; an unparseable blob yields the
  empty triple, never a silent drop of the path.
- observability — none new; each caller reports as today.
- risks — a moved name a caller reaches by attribute and the explicit import list misses; AC2 and
  AC5 compare outputs at base and at the tip, and the lexicon's own selftest arms run at the close.
- testing — AC1 to AC7 by the pass; the new arms of §7 at the close.
- migration — none, as §4 says.
- user docs — none under `help/`: no page names the extractors.

## 6. Acceptance criteria

- **AC1** — When the `extract_code` block is cut with the parity arm's `blk` awk range from
  `extract_code.py` in `tools/lib`, `tools/lexicon` and `tools/codebase-map`, the three cuts are equal;
  with one byte changed in the codebase-map copy, its cut differs.
  Red when: a copy carries the block outside the markers, or no row names the stem.
- **AC2** — When a probe calls `read_defs_at_sha(root, sha, armed, sets)` from the base's
  `lexicon.py` and from the pass tip's over gov's repository at the base sha, with the armed set
  `.lexicon.conf` declares, the two returned sets are equal and non-empty.
  Red when: a moved parser changed its output, or the adapter drops a path.
- **AC3** — When a probe calls `read_defs_at` over a fixture repository under `%TEMP%` whose `a.py`
  defines `f` at HEAD, `g` in the staged index and `h` in the working tree, the three states return
  `f`, `g` and `h` respectively for `a.py`, each with its own blob id.
  Red when: a state reads another state's text, or the worktree blob id differs from `git hash-object`.
- **AC4** — When `scan_shell_layer` runs from the pass tip over gov's tree, its rows equal the base's;
  and in a scratch copy of `tools/` with `tools/lexicon/` removed, it still returns those rows.
  Red when: the shell layer still resolves the lexicon kit.
- **AC5** — When a probe computes drift-audit's `build_lexicon_marginal_offense_rate` at base and at
  the tip over the same base and head shas, the two results are equal, and `git grep -n
  _read_defs_at_sha -- tools/drift-audit` prints nothing.
  Red when: the signal's operands change, or the copy survives.
- **AC6** — When a probe calls `map_lib._identifier_tokens` at base and at the tip over every
  extension `_LEX_PROFILES` maps and one it does not, each returns the same token set; and an `ast`
  probe of the tip's `map_lib.py` finds no module-level assignment to `_LEX_PROFILES`.
  Red when: the lexer changed behaviour in the move, or a second copy stays in `map_lib.py`.
- **AC7** — When `read_defs_at` reads a revision that does not exist, it returns `None`; when it reads
  a fixture blob holding a Python syntax error, that path maps to the empty triple.
  Red when: a git failure reads as an empty tree, or a parse error drops the path.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `drift-audit selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/lib/resolve-python.test.sh · covers AC1 · the `extract_code` `PARITY_ROWS` row, staged by one byte changed in `tools/codebase-map/extract_code.py` · that suite's assertion count, raised by the row
New arm: tools/lexicon/selftest.py · covers AC3 AC7 · a `read_defs_at` arm over the three states and the two failure cases on a scratch repository, staged by reading the index through the worktree branch · none
New arm: tools/codebase-map/selftest.py · covers AC4 · the shell layer built with no lexicon kit reachable, staged by restoring the `from lexicon import` line · none

## 8. Open questions

- **F1 — I13 spells `read_defs_at(root, state, paths=None, cache=None)`; the lexicon needs its armed
  map and pattern sets, which that signature cannot carry.** Options: (a) keep the four positional
  parameters and add keyword-only `armed` and `sets`, defaulting to the four built-in parsers; (b)
  a second function for the lexicon; (c) bind the lexicon's conf into the primitive. (b) is a second
  reader of one batch; (c) puts one kit's conf in every kit's copy. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the interface's positional spelling unchanged, so unit 8 calls it as I13
  spells it. widens: none · relaxes: none
- **F2 — What does "retire the map's second tokenizer" do with `_identifier_tokens`?** Options: (a)
  move it and its profile table into the primitive, one module holding both lexers; (b) re-implement
  it over the lexicon's tokenizers for Python, shell and JavaScript and keep the profile lexer for the
  rest; (c) leave it in `map_lib.py`. (b) changes the ranking the map's corpus recall and precision
  floors measure (`tools/codebase-map/selftest.py:1699`); (c) keeps the copy whose only stated reason,
  that the kits cannot import each other (`map_lib.py:672-679`), this primitive removes. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the most criteria met with no behaviour change.
  widens: none · relaxes: none
- **F3 — Does the primitive carry definition context (class, bases, decorators) as lexicon.md:421-427
  lists?** Options: (a) here; (b) dMindYourWords'. RESOLVED (agent, 2026-10-26, delegated): (b),
  rung 1, cl-dClosedLoop-0224 names the states and the tokenizers only, and cl-0273's row builds the
  definition classes over it. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 13, the brief's I13, scout B's row for
  cl-0224 and the sources read at base `462d20f3`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dTotalRecall-43, written by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is the lexicon's own extraction, verified at base `462d20f3`: the parsers at
`tools/lexicon/lexicon.py:417-2253`, the batched revision reader `read_defs_at_sha` at `:4113`, whose
docstring calls itself the copy of `_read_defs_at_sha` at `tools/drift-audit/drift_report.py:1387`
(the second instance, so it is extracted here and never copied a third time), and the inline-block
mechanism `PARITY_ROWS` at `tools/lib/resolve-python.test.sh:168-184`, whose `blk` reader and copy
grep at `:213` and `:218` already read `*.py` copies. `python tools/codebase-map/reuse_lookup.py
"move shell and javascript tokenizers into one shared extraction primitive read at a revision"`
ranked name-stem neighbours (`read`, `read_blobs_at`, `read_records`) and `parse_shell_defs` at fan-in
2, the moved function itself; it does not see the map's profile lexer as a tokenizer, which `git grep
_LEX_PROFILES` found. Scout B's line numbers agreed with source at base, but its `:659-697` for the
profile lexer stops before `_identifier_tokens`, which runs from `:697` to `:818`, its table opening
with `_IDENT_TOKEN_RE` at `:642`.

Recall terms used: `python tools/memory-recall/query.py "how does one extraction primitive in tools/lib serve the lexicon and the map" --terms "extract_text read_defs_at_sha parse_shell_defs scan_ts_tokens tokenizer primitive PARITY_ROWS inline canonical copy lexicon codebase-map"`
