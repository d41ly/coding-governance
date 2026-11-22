# TOOL-dTotalRecall-13 — the shared extraction primitive in `tools/lib`, which the map and the lexicon each call

**Status:** CLOSED · rev-3 · 2026-11-22 · node d · Tier-2 · base 8b8b1374 · streams tooling · order 2 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0224@bfb0a85c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-12 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-11-22-build-TOOL-dTotalRecall-13-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dTotalRecall-13-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dTotalRecall-13-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-13-reground-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-11-22-prompt-TOOL-dTotalRecall-13-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-13-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-13-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-13-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-13-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-13-reground-spec-writer.md) | journal | — |
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

- **S1** — The canonical block in `tools/lib/extract_code.py`, opened by `# >>> extract_code —
  canonical copy: extract_code.py in gov's lib dir (byte-identical; gated)` and closed by `# <<<
  extract_code`, the marker shape every `PARITY_ROWS` row's block carries. It holds, moved from
  `tools/lexicon/lexicon.py` with their code unchanged, every top-level statement from
  `tools/lexicon/lexicon.py#ext_of` through `tools/lexicon/lexicon.py#extract_text` except
  `tools/lexicon/lexicon.py#resolve_pattern_sets`, plus `tools/lexicon/lexicon.py#PATTERN_SETS`. That
  is the parsers `_python_defs`, `parse_shell_defs`, `parse_ts_defs`, `parse_ts_source` and
  `parse_tsx_defs`; the tokenizers `scan_shell_tokens` and `scan_ts_tokens` with every `check_ts_`
  and `read_ts_` helper and every `_SH_` and `_TS_` constant; and `PARSERS`, `_probe_defs`,
  `resolve_extractor` and `extract_text`, whose signature `extract_text(src, mode, pset, *,
  sets=None)` stays. An `ast` walk of that range at `8b8b1374` finds no lexicon name it loads outside
  itself but `PATTERN_SETS` and `re`. `resolve_pattern_sets` stays: it reads `PATTERN_PARTS` from
  `lexicon_conf`, a conf the primitive never reads. `KNOWN_EXTS` stays: `scaffold_lexicon.py` reads
  it as `lex.KNOWN_EXTS`. A comment the move makes false is corrected, and no code byte changes.
  Observed by AC1 and AC2.
- **S2** — The state reader `read_defs_at(root, state, paths=None, cache=None, *, armed=None,
  sets=None)` in the block, generalising `tools/lexicon/lexicon.py#read_defs_at_sha`: `state` is
  `worktree`, `index` or a revision, per §4 "The states". A helper it defines leads with a verb
  `.lexicon.conf` declares. Observed by AC3 and AC7.
- **S3** — The copies: `tools/lexicon/extract_code.py` and `tools/codebase-map/extract_code.py`, each
  carrying the block byte for byte, held by a new `PARITY_ROWS` row `extract_code` in
  `tools/lib/resolve-python.test.sh` whose canonical is `tools/lib/extract_code.py`. Observed by AC1.
- **S4** — The lexicon calls its copy: `tools/lexicon/lexicon.py` imports every moved name from its own
  `extract_code.py` by an explicit list, underscore names included, after its own `sys.path` insert,
  so `lexicon.extract_text`, `lexicon.ext_of`, `lexicon.read_ts_jsx_defs` and every other moved name
  still resolve on the module. `read_defs_at_sha` keeps its signature as a thin adapter over
  `read_defs_at`. Observed by AC2.
- **S5** — The map calls its copy: `tools/codebase-map/map_extractors.py#scan_shell_layer` imports
  `parse_shell_defs` from the codebase-map kit's own `extract_code.py`, and its
  `resolve_kit_dir("lexicon", "lexicon.py", TOOLS)` lookup, the `MapError` raised when that lookup
  fails, and the `from lexicon import parse_shell_defs` line retire. Its docstring's fail-closed list
  and the two comments above `SHELL_ROOTS` and on the `kit-sh` row of `SYMBOL_EXTRACTORS` name the
  kit's own copy. Observed by AC4.
  **Readers:** by name: `from lexicon import parse_shell_defs` is spelled in `scan_shell_layer` of
  `tools/codebase-map/map_extractors.py` only (`git grep` at 8b8b1374) · by value: NO VALUE READERS —
  the import yields a function, and the shell layer's rows are what its readers compare, unchanged.
- **S6** — The map's lexer moved into the primitive: every top-level statement of
  `tools/codebase-map/map_lib.py` from `tools/codebase-map/map_lib.py#_IDENT_TOKEN_RE` through
  `tools/codebase-map/map_lib.py#_identifier_tokens`, that is `_LEX_PROFILES` with the loop filling
  it, the three `_PROFILE_` rows, `_DATA_EXTS`, `DEFINITION_CARRYING_EXTS`, `_TRIPLE_QUOTES`,
  `_PY_PREFIX_CHARS`, `_IDENT_TOKEN_RE` and `_identifier_tokens`, moves into the block. The range
  loads no `map_lib` name outside itself but `re` (an `ast` walk at `8b8b1374`). `map_lib.py` imports
  them from its kit's `extract_code.py`, so `map_lib._identifier_tokens` still resolves. Observed by
  AC6.
  **Readers:** by name: `_identifier_tokens` in `build_reference_index` of
  `tools/codebase-map/map_lib.py`, and in `test_identifier_tokens_per_language` and
  `test_identifier_tokens_corpus_recall` of `tools/codebase-map/selftest.py`;
  `DEFINITION_CARRYING_EXTS` in `derive_present_layers` of `tools/codebase-map/map_lib.py` ·
  by value: the reference index `build_reference_index` and `fan_in`, whose token sets are unchanged.
- **S7** — The drift-audit copy retires: `tools/drift-audit/drift_report.py#_read_defs_at_sha` is
  deleted, and its two callers in
  `tools/drift-audit/drift_report.py#build_lexicon_marginal_offense_rate` call
  `lex.read_defs_at_sha(ctx.root, sha, armed, sets)` through the lexicon module that function already
  imports. Observed by AC5.
  **Readers:** by name: `_read_defs_at_sha` in `build_lexicon_marginal_offense_rate` of
  `tools/drift-audit/drift_report.py`, twice, and in the docstring of `read_defs_at_sha` in
  `tools/lexicon/lexicon.py` · by value: the `lexicon marginal offense rate` signal's two operands,
  `at_base` and `at_head`.
- **S8** — The lexicon's offender pin follows the move. The moved offenders `ext_of`, `_python_defs`,
  `_probe_defs` with its nested `hits`, and `_identifier_tokens` (DERIVED 2026-11-22 by `python
  tools/lexicon/lexicon.py --offenders`) land in three tracked copies, so `VERB_OFFENDER_PIN` in
  `.lexicon.conf` is re-measured by `python tools/lexicon/lexicon.py --measure` and pasted as it
  prints, under a dated comment in the shape the pin's history carries. NOT OBSERVED by a criterion:
  the `lexicon naming predicates` leg's two-sided pin grades it at the close.
- **S9** — The guard follows the import: the `[[exempt_leg]]` row `drift-audit selftest` in
  `tools/govkit/registry.toml` gains `{prefix}/lexicon/extract_code.py` beside its lexicon
  modules, and `python tools/run-gates/leg_factory.py --write` renders it into
  `tools/gate-legs.json`. That suite's import closure reaches every lexicon module through
  `drift_report.py`'s `import lexicon` (`python tools/run-gates/py_reads.py --guards "drift-audit
  selftest"` at `8b8b1374`), and `tools/run-gates/py_reads.py#run_guards` reds a walked module its
  guard does not cover. Observed by AC8.

## 3. Non-goals (OUT)

- Definition context, the enclosing class, bases resolved through imports and decorators with aliases
  resolved
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:423-427`):
  dMindYourWords' (cl-dClosedLoop-0273), which extends this primitive.
- Line ranges, body hashes and call sites: TOOL-dTotalRecall-8 adds them to the block for the `code`
  record.
- Re-implementing `_identifier_tokens` over the lexicon's tokenizers for the languages both read: a
  behaviour change to the map's ranking that no clause asks for (§8 F2).
- Changing what any extractor returns. Every moved function keeps its code and its output.
- The map's other dependency on the lexicon, its `lexicon-verbs` inventory: it stays
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:439-441`).
- Giving `tools/codebase-map/map_extractors.template.py` a shell layer, which the kit's own copy now
  makes possible: no clause asks for it.
- Bumping `KIT_LEXICON_VERSION`, `KIT_CODEBASE_MAP_VERSION` or `KIT_DRIFT_AUDIT_VERSION`: the lander
  mints them through `tools/govkit/govkit.py#cmd_mint`, so a branch owes none
  (`tools/govkit/govkit.py#cmd_epoch`'s docstring, TOOL-aMendedFleet-65 S6).
- `tools/memory-tree/tree_lib.py#read_blobs_at`, the memory-tree kit's own revision reader: a
  different kit's reader of record text, not of definitions, and no kit this unit touches requires
  the memory-tree kit but the map.

### Edges

- **hands-off** `TOOL-dTotalRecall-8` — `extract_code.py`, the block and `read_defs_at`, which unit 8 extends with ranges, body hashes and calls and copies into the memory-tree kit
- **hands-off** external — dMindYourWords (cl-dClosedLoop-0273) calls this primitive and extends it with definition context
- **hands-off** `TOOL-dTotalRecall-43` — `BUILTIN_ARMED` and `read_defs_at`'s worktree ids, which that unit changes for the round-1 audit's ids 18 and 48

## 4. Design

### The block

The canonical file opens with a short comment header outside the markers, naming itself the
canonical and the parity row; the markers wrap everything a caller reaches. Each kit copy carries its
own comment header and the identical block, and neither spells an install prefix, as the
`resolve_kit_dir` copies do (`tools/codebase-map/map_extractors.py#resolve_kit_dir`). The parity arm
cuts the block with `tools/lib/resolve-python.test.sh#blk`, which prints from the opening marker line
through the closing one, and finds copies with the `git grep -l -E "^(# |// )>>> $stem"` over `*.py`
beside it, so no extractor change is needed: a new row is the whole join. No stem in `PARITY_ROWS`
at `8b8b1374` has `extract_code` as a prefix, nor is a prefix of it.

```
extract_code|$ROOT/$KIT_REL/extract_code.py|$KIT_REL/extract_code
```

The block imports only the standard library (`ast`, `hashlib`, `re`, `subprocess`), since a
copy-installed kit carries no `tools/lib` at an adopter.

One module name serves every kit. A process that loads both kits, as the codebase-map selftest's
lexicon arm does after `map_lib` is loaded, imports whichever `extract_code.py` `sys.path` finds
first and reuses it from `sys.modules`. The parity row is what makes that choice immaterial: the two
copies differ only in their comment headers.

### The states

| `state` | Paths and blob ids | Text |
|---|---|---|
| `worktree` | `git ls-files -s -z`, gitlinks skipped | each file's bytes from disk; the blob id is git's own, `sha1(b"blob %d\0" % len + bytes)`, computed in Python with no spawn |
| `index` | `git ls-files -s -z`, stage-0 entries only (§8 F4) | one `git cat-file --batch` over the ids not in `cache` |
| a revision | `git ls-tree -r -z <rev>` | one `git cat-file --batch`, as `read_defs_at_sha` reads today |

The return is `{path: (blob, triple)}`, `triple` the `(functions, types, imports)` of `extract_text`,
for every path whose extension `armed` maps; `armed` maps an extension to `(pset, mode)`, the shape
`read_defs_at_sha` reads as `armed[ext]`. It defaults to `BUILTIN_ARMED`, the four parsers by
extension (`py` `python-ast`; `sh` and `bash` `shell-tokens`; `js`, `mjs`, `cjs` and `ts`
`ts-tokens`; `tsx` and `jsx` `tsx-tokens`), each under `parser`. A blob whose extractor raises
`SyntaxError`, `ValueError` or `KeyError`, or that `extract_text` answers `None` for, yields the
empty triple, the fail-closed rule `read_defs_at_sha` states. A tracked path absent from disk yields
no entry in the `worktree` state, which TOOL-dTotalRecall-43 S36 later counts as `missing`. A failed
git call returns `None`, which is not an empty tree. `cache` maps `(blob, ext)` to the triple, so a
blob shared by two states is parsed once.

`read_defs_at_sha(root, sha, armed, sets, paths=None, cache=None)` in `lexicon.py` becomes:

```python
got = read_defs_at(root, sha, paths, cache, armed=armed, sets=sets)
return None if got is None else {(rel, nm) for rel, (_b, t) in got.items() for nm, _ln in t[0]}
```

Its cache changes from names to triples. `tools/lexicon/lexicon.py#check_merge_losses` holds one
cache across every call of its run, as today, and never reads an entry itself.

### The callers

| Caller | Before | After |
|---|---|---|
| `tools/lexicon/lexicon.py` | defines the parsers | imports them from `extract_code` |
| `tools/codebase-map/map_extractors.py#scan_shell_layer` | `from lexicon import parse_shell_defs`, after resolving the lexicon kit | `from extract_code import parse_shell_defs`, its own kit |
| `tools/codebase-map/map_lib.py` | defines the profile lexer | imports it from `extract_code` |
| `tools/drift-audit/drift_report.py#build_lexicon_marginal_offense_rate` | calls its own batched reader | calls `lex.read_defs_at_sha` |

`map_lib.py` and `map_extractors.py` import the codebase-map kit's module by the directory `map_lib`
is loaded from. Every importer of `map_lib` already holds that directory on `sys.path`, by inserting
the kit directory or by running from it (`git grep -n "import map_lib" -- tools` at `8b8b1374`).

### Inventory

Minted: `tools/lib/extract_code.py`, `tools/lexicon/extract_code.py`,
`tools/codebase-map/extract_code.py`, the block `extract_code`, `read_defs_at`, `BUILTIN_ARMED`, the
`PARITY_ROWS` row `extract_code`. Naming cells: `python tools/lexicon/lexicon.py --suggest
read_defs_at --as py.function` answered OK at `8b8b1374`, `read` being a declared verb.

### Migration

None for an adopter's records or confs. A copy-installed adopter receives the two kit copies on its
next `govkit update`; both kits ship under an `include = "**"` engine rule
(`tools/lexicon/kit.toml`, `tools/codebase-map/kit.toml`), and the copy-install runbook copies each
kit directory whole, so the file travels with it.

### Files touched (estimate)

- `tools/lib/extract_code.py` (new)
- `tools/lexicon/extract_code.py` (new)
- `tools/codebase-map/extract_code.py` (new)
- `tools/lexicon/lexicon.py`
- `tools/lexicon/selftest.py`
- `tools/codebase-map/map_extractors.py`
- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/selftest.py`
- `tools/drift-audit/drift_report.py`
- `tools/lib/resolve-python.test.sh`
- `tools/govkit/registry.toml`
- `tools/gate-legs.json` (the render of `leg_factory.py --write`)
- `.lexicon.conf`
- `memory/map/generated/` (the render of `gen_map.py --write`)

### Alternatives rejected

- **Keep the map importing the lexicon kit.** The clause has the map call the primitive, and
  KN-1 with `TOOL-dClosedLexicon-12` hold that neither kit requires the other
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:429-431`).
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
  empty triple, never a silent drop of the path; a path absent from disk yields no worktree entry.
- observability — none new; each caller reports as today.
- risks — a moved name a caller reaches by attribute and the explicit import list misses; AC2 and
  AC5 compare outputs at base and at the tip, and the lexicon's own selftest arms run at the close.
- testing — AC1 to AC8 by the pass; the new arms of §7 at the close.
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
  fixture: the base's kit is `git archive <base> tools/lexicon`, unpacked into a scratch directory.
- **AC3** — When a probe calls `read_defs_at` over a fixture repository under `%TEMP%` whose `a.py`
  defines `f` at HEAD, `g` in the staged index and `h` in the working tree, the three states return
  `f`, `g` and `h` respectively for `a.py`, each with its own blob id.
  Red when: a state reads another state's text, or the worktree blob id differs from `git hash-object`.
- **AC4** — When `scan_shell_layer("kit-sh", SHELL_ROOTS)` runs from the pass tip over gov's tree, its
  rows for every `.sh` file the pass leaves untouched equal the base's; and when the same call runs
  from a scratch tree under `%TEMP%`, `git init`ed and holding copies of `tools/`, `.githooks/`,
  `skills/` and `.codebase-map.conf` with `tools/lexicon/` absent, it returns the tip's rows less
  those whose `file` sits under `tools/lexicon/`.
  Red when: the shell layer still resolves the lexicon kit, so the scratch call raises `MapError`.
- **AC5** — When a probe computes drift-audit's `build_lexicon_marginal_offense_rate` from the base's
  `drift_report.py` and from the tip's, both against one repository at one HEAD, the two results are
  equal, and `git grep -n _read_defs_at_sha -- tools/drift-audit` prints nothing and exits 1.
  Red when: the signal's operands change, or the copy survives.
- **AC6** — When a probe calls `map_lib._identifier_tokens` at base and at the tip over every
  extension `_LEX_PROFILES` maps and one it does not, each returns the same token set; and an `ast`
  probe of the tip's `map_lib.py` finds no module-level assignment to `_LEX_PROFILES`.
  Red when: the lexer changed behaviour in the move, or a second copy stays in `map_lib.py`.
- **AC7** — When `read_defs_at` reads a revision that does not exist, it returns `None`; when it reads
  a fixture blob holding a Python syntax error, that path maps to the empty triple.
  Red when: a git failure reads as an empty tree, or a parse error drops the path.
- **AC8** — When `python tools/run-gates/py_reads.py --guards "drift-audit selftest"` runs at the tip,
  its closure lists the lexicon kit's `extract_code.py` and it exits 0.
  Red when: the guard lacks the copy, and the run prints `RED guard` naming that copy and exits 1.

## 7. Gates

`lexicon selftest` · `lexicon naming predicates` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `drift-audit selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `python reads (a name never bound, an import outside its guard)` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `playbook render selftest` · `policy fixtures` · `measure-legs selftest` · `gate-leg conformance` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `straggler-guard arms` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary`

New arm: tools/lib/resolve-python.test.sh · covers AC1 · the `extract_code` `PARITY_ROWS` row, staged by one byte changed in `tools/codebase-map/extract_code.py` · that suite's assertion count, raised by the row
New arm: tools/lexicon/selftest.py · covers AC3 AC7 · a `read_defs_at` arm over the three states and the two failure cases on a scratch repository, staged by reading the index through the worktree branch · none
New arm: tools/codebase-map/selftest.py · covers AC4 · the shell layer built with no lexicon kit reachable, staged by restoring the `from lexicon import` line · none

What these do not check: that a copy's comment header is accurate, since the cut starts at the
marker; a moved name reached only by a computed attribute, which no import list can see; and the
worktree state under a checkout filter, which TOOL-dTotalRecall-43 S36 takes.

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
  floors measure (`tools/codebase-map/selftest.py#test_identifier_tokens_corpus_recall`); (c) keeps
  the copy whose only stated reason, that the kits cannot import each other (the comment above
  `tools/codebase-map/map_lib.py#_DATA_EXTS`), this primitive removes. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the most criteria met with no behaviour change. widens: none · relaxes:
  none
- **F3 — Does the primitive carry definition context (class, bases, decorators) as
  `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:423-427`
  lists?** Options: (a) here; (b) dMindYourWords'. RESOLVED (agent, 2026-10-26, delegated): (b),
  rung 1, cl-dClosedLoop-0224 names the states and the tokenizers only, and cl-0273's row builds the
  definition classes over it. widens: none · relaxes: none
- **F4 — Which entries does the `index` state read for an unmerged path, whose entries sit at stages 1
  to 3?** `git ls-files -s -z` prints one row per stage, so the state needs a rule the clause does not
  give. Options: (a) stage-0 entries only, so an unmerged path yields no entry; (b) stage 2, the
  current branch's side; (c) `None` for the whole read. (b) answers a question no caller asks, since a
  commit cannot be made over an unmerged index; (c) turns one conflicted path into a failed read of
  the tree. RESOLVED (agent, 2026-11-22, delegated): (a), rung 3, the one index text git itself
  would commit, and the same no-entry answer the `worktree` state gives an absent file. widens: none
  · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 13, the brief's I13, scout B's row for
  cl-0224 and the sources read at base `462d20f3`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dTotalRecall-43, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-22 · S1, S2, S4, S5, S6, S7, S8, S9 · §3 · §4 · §5 · AC2, AC4, AC5, AC8 · §7 · §8
  F2, F3, F4 · §10 · re-grounded at base `8b8b1374` per
  `2026-11-22-prompt-TOOL-dTotalRecall-13-reground-brief`: cites by symbol; S1 names the whole moved
  range; the version bump leaves for the lander's mint, S8 re-measures the offender pin and S9 widens
  drift-audit's guard; AC4 drops the lexicon kit's own rows; F4 decides the index stage.

## 10. Reuse audit

The seam is the lexicon's own extraction, verified at base `8b8b1374`: the parsers from
`tools/lexicon/lexicon.py#ext_of` through `tools/lexicon/lexicon.py#extract_text`, and the batched
revision reader `tools/lexicon/lexicon.py#read_defs_at_sha`, whose docstring calls itself the copy of
`tools/drift-audit/drift_report.py#_read_defs_at_sha`. That is the second instance, so it is extracted
here and never copied a third time. The inline-block mechanism is `PARITY_ROWS` in
`tools/lib/resolve-python.test.sh`, whose `blk` reader and copy grep already read `*.py` copies, as
the `legacy_ledger_py` and `commit_trailers_py` rows' Python copies show. `python
tools/codebase-map/reuse_lookup.py "move shell and javascript tokenizers into one shared extraction
primitive read at a revision"`, re-run at `8b8b1374`, ranked name-stem neighbours (`read_text`,
`read`, `read_blobs_at`) and `parse_shell_defs` at fan-in 2, the moved function itself; it does not
see the map's profile lexer as a tokenizer, which `git grep _LEX_PROFILES` found. Scout B's line
numbers were read at `462d20f3` and every one has moved; the symbol cites above replace them.
`tools/memory-tree/tree_lib.py#read_blobs_at` is the nearest batched reader and stays out, for the
reason §3 gives.

Recall terms used: `python tools/memory-recall/query.py "how does one extraction primitive in tools/lib serve the lexicon and the map" --terms "extract_text read_defs_at_sha parse_shell_defs scan_ts_tokens tokenizer primitive PARITY_ROWS inline canonical copy lexicon codebase-map"`
