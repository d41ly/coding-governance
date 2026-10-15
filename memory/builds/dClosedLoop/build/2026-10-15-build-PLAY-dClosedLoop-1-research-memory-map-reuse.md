# Research: the memory layer, the codebase map and the reuse tools

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 24's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-5-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`.

---

# The codebase map and the reuse tools: what they see, and what a caller map would take (PLAY-dClosedLoop-1, part 3)

The map does not track callers. It stores definitions only, it misses about a quarter of Python's definitions, and it captures no Markdown, TOML or JSON symbols. A caller map can be built with the standard library on top of parsers the repository already has, and it finishes in under 8 seconds on this tree. `reuse_lookup.py` should be retired as a ranker. `memory-recall` is worth keeping, but only as a record finder.

## Inventory

**What `tools/codebase-map/` captures, by language** (HEAD `69d01844f`)

| Language | Tracked files outside `memory/` | Captured | Kinds | Source |
|---|---|---|---|---|
| Python | 88 (87 `tools/`, 1 `.githooks/`) | Public module-level `def` and `class`, plus static `__all__` names, under `tools/` only. `*.template.py` files are dropped. | function, class, const-export | `map_lib.py:318-360`, `map_extractors.py:336-353` |
| Shell | 128 (120 `tools/`, 6 `.githooks/`, 2 `skills/`) | Public functions, read by the lexicon kit's tokenizer `parse_shell_defs` | function | `map_extractors.py:289-333` |
| JavaScript | 20 (`tools/`) | Export scan combined with a regex for statement-leading definitions | function, class, const-export | `map_extractors.py:356-377`, `map_lib.py:414-489` |
| PowerShell | **0 tracked** | No lexical profile exists for it either | — | `map_lib.py:663-670` |
| Markdown, TOML, JSON | 95 / 36 / 23 | No symbols. Only inventory keys: gotcha, guide and backlog file names, `SKILL.md` directories, gate-leg names from `gate-legs.json`, hook keys from `settings.json` | — | `map_extractors.py:190-244` |

The only allowed symbol kinds are `function`, `class`, `component` and `const-export` (`map_lib.py:313`).

**Relations and callers: none are stored.**
- Each `symbols.json` row holds exactly `id`, `kind` and `file`. Fan-in is left out on purpose, because it would restale the file on every commit (`map_lib.py:1586-1592`).
- "Fan-in" is computed on demand. It counts the distinct files that mention the name as an identifier, minus the files that define it. The code says itself that this is "not a resolved call graph" (`map_lib.py:960-981`).

**What `memory/map/` holds**

| Item | Content |
|---|---|
| `features/` | 31 dossiers. Each has a TOML claims fence plus prose sections (`gen_map.py:103-104`). |
| `FOUNDATION.md` | Claims on the shared substrate |
| `baseline.toml` | 2,133 B. A shrink-only list of keys nobody has claimed: 19 gate legs, 5 kits, and so on. It carries one recorded exception, a renamed key. |
| `generated/inventories.json` | 11 inventories, 353 keys in total |
| `generated/MAP.md`, `CARDS.md` | Rendered views |
| `generated/symbols.json` | 4,670 rows, 555,035 B |

**Two records that disagree with the code**
- `memory/map/README.md:35-36` tells readers to run `python codebase-map/reuse_lookup.py`. That path does not exist: `ls codebase-map` fails. The kit lives under `tools/`.
- `map_lib.py:441`, `:453` and `:832` quote "six tracked `tools/**/*.js`". Today there are 20. These are dated measurements written in the present tense.

## Sequence

1. I read the extractors, the renderer and the lookup.
2. I counted definitions against `symbols.json`.
3. I ran the freshness check, which only compares bytes.
4. I probed a stdlib call graph: first resolving by name only, then with Python imports.
5. I timed `reuse_lookup` by calling its pure functions. That skips `main`, so `write_lookup` (`reuse_lookup.py:819-866`) never ran and no log row was written.
6. I read the usage logs.
7. I ran the recall extract and bench into the session scratchpad.
8. I checked which external tools are installed.

None of this changed a tracked file. The extra `git status` entries during the run are the parent session's dClosedLoop records.

## Measurements

**How many definitions the map knows** (`python3 count.py .` and `python3 graph.py .`, scratch scripts using `ast` over `git ls-files` outside `memory/`)
```
py: top-func 2678, class 65, method 30, nested-func 468   (total 3,241)
symbols.json rows 4670 {('py','class'):55, ('py','function'):2392, ('sh','function'):1919,
                        ('js','function'):294, ('js','const-export'):10}
sh regex (incl. heredoc bodies) pub 1983 priv 29;  js defs any-indent 297
```

| Language | In the tree | In the map | Coverage | What is missing |
|---|---|---|---|---|
| Python | 3,241 | 2,447 | **75.5%** | 262 private module-level defs, 468 nested functions, 30 methods, 24 template defs, and the `.githooks` Python file |
| Shell | about 1,983 public (regex upper bound) | 1,919 | about 97% | Private `_` functions, by design |
| JS | about 297 | 304 | about 100% | — |
| MD, TOML, JSON | — | 0 symbols | — | Only the inventory keys above |

**Caller edges in the map: 0.**

**Freshness**
```
$ time python3 tools/codebase-map/gen_map.py --check
real 0m4.399s   exit=0
```
The generated files are current.

**Probe 1: stdlib graph, resolving by name only** (7.8 s)
```
py call-sites 59468 {'to-no-repo-def':34630,'same-file':19216,'unique-cross-file':3971,'ambiguous(>1 definer)':1651}
js call-sites 6300  {'unique-cross-file':301,'ambiguous(>1 definer)':252,'to-no-repo-def':4921,'same-file':826}
sh(word==defined fn) 32343 {'ambiguous(>1 definer)':1154,'same-file':29804,'unique-cross-file':1385}
distinct def names 4563, names with >1 definer 322, shfail 0, jsfail 0
script-invocation sites (interp + path) by caller ext {'sh':875,'py':109,'json':12,'js':10,'hook':3,'yml':3}
```
- The lexicon tokenizers parsed all 128 tracked shell files and all 20 JS files with **no failures**.
- Matched by name alone, the cross-file calls are ambiguous at these rates: Python 29%, shell 45%, JS 46%.

**Probe 2: Python with import awareness** (4.7 s). An alias resolves to a module stem, preferring a module in the caller's own kit directory, which is how the kits extend `sys.path`. `from x import y` is resolved the same way.
```
{'local':14450,'mod.attr resolved':1861,'from-import resolved':125,'mod.attr ambiguous':11,
 'method/dynamic (unresolved)':21588,'external':3984,'builtin/other':17500}
resolved edges 2857, cross-file edges 698
```
- Ambiguous sites fell from **1,651 to 11**.
- 21,588 attribute calls stay unresolved: `self.x`, `str` methods and dynamic dispatch. That is the floor for anything without type inference.

**Probe 3: `reuse_lookup` ranking, timed**
- Loading the corpus took 0.1 s. Building the reference index took 3.2 s.
- "find the python launcher that actually runs" returned **316** ranked candidates. The top one is `run`, a test helper defined in 29 files (fan-in 91). `resolve_python` came second (fan-in 6, despite 69 installs).
- "append one JSONL row to a log under the git common dir" returned 280. The top two are the test helpers `rows` and `row`.
- The cause is the ranking itself: seeds are chosen by shared name stem and then sorted by fan-in (`reuse_lookup.py:277-281`, `:348-370`).

**Usage logs** (under `.git/` in the common directory)
```
.git/codebase-map/lookups.jsonl 285 {'lookup':285} 2026-09-01..2026-10-15; n_shown==0: 0 of 285; median n_shown 110
.git/recall/queries.jsonl 697 {'query':570,'refused':6,'opened':121} 2026-08-08..2026-10-15
opened in_shown {False:92, True:29}; queries since opened hook (2026-08-16): 530
```
- The handed fact puts the inCMS lookup log at one row. Gov's own log holds 285 rows, so the two do not conflict.
- No lookup was ever logged with an empty answer, and the median answer lists 110 candidates.
- The lookup has no hook that records what was opened, so there is no signal of whether it helped.
- For recall, only 29 of 530 queries (5.5%) were followed by a Read of a hit that recall had shown. 92 were followed by a Read of a memory file it had not shown. The hook records only the first Read per query (`recall-opened.js:170`), and every opened row is inferred.

**What recall indexes**
- Markdown under `MEMORY_ROOT` (`extract.py:302-309`), plus three declared extra sources (`.memory-tree.conf:671`), minus the versioned archive files (`:680`). **No code at all.**

**Recall bench.** I ran it because both steps write only to a directory I choose: `extract.py:864-877` writes to the out-dir, and `bench.py:496` writes only with `--json`.
```
$ python3 tools/memory-recall/extract.py . <scratch> --rev HEAD      real 57.3s
records 2806 docs; chunks 52335 docs; orphan ids 22 (1.0%)
$ python3 tools/memory-recall/bench.py <scratch> recall-fixture.json --sets records,chunks --subs grep,fts5,fts5w --ks 1,5,20   real 6.3s
records  fts5  r@1 0.42  r@5 0.83  r@20 0.83  MRR 0.576
chunks   fts5  r@1 0.00  r@5 0.00  r@20 0.00
```
The fixture has 12 queries.

**Installed here:** node v24.16.0, npm 11.13.0 and ripgrep 14.1.1.
- Node's bundled acorn 8.16.0 parses `agent-cap.js` (68 top-level nodes), but only with `--expose-internals`, which Node does not support as an API.

**Not installed:** ctags, universal-ctags, the tree-sitter CLI, scip, scip-python, scip-typescript, pyright, pylsp, bash-language-server, gtags and cscope. Neither Python 3.14 nor 3.12 has the modules `tree_sitter`, `jedi`, `bashlex`, `esprima`, `pyan` or `pycg`.

## Gaps

1. **No relations at all.** No caller, callee or import edge is stored. The cross-language edges also matter: 1,012 sites invoke a repository script through an interpreter, 875 of them from shell. No symbol indexer in the candidate list sees those.
2. **Python is a quarter dark.** The map misses methods, nested functions and private helpers, and it ignores Python outside `tools/`.
3. **The lookup's fan-in counts files that mention a name, not calls.** Common test-helper names win the ranking. The handed benchmark result (0 of 24 cases solved) is consistent with what I saw.
4. **Recall does not index code.** It can answer a reuse question only through a record that names the code.
5. **The recall bench's chunk set scores 0.00 on fts5.** The kit's floor is `served:r@5>=0.86` (`.memory-tree.conf:814`), graded by `check-recall.py`, which I did not run. I have not established why the bench's chunk arm scores zero.
6. **The map README names a path that does not exist** (`memory/map/README.md:35-36`).

## Candidates

| | Mechanism | Languages covered here | Callers? | Deterministic | Runtime here | Dependencies | Test that could make it lose | Result |
|---|---|---|---|---|---|---|---|---|
| **A. Extend the existing seam** | `map_lib`'s `ast` extractor widened to all defs, plus an import-aware call pass. Shell and JS use the lexicon kit's `scan_shell_tokens` and `scan_ts_tokens(calls=…)` (`lexicon.py:469`, `:950`), which `map_extractors.py:306` already imports. An interpreter-plus-path scan adds the cross-language edges. Output is a generated `calls.json` with the same freshness check. | Python, shell, JS. MD, TOML and JSON need no call edges. | Yes. Resolved for Python, by name for shell and JS. | Yes: sorted rows, as `render_symbols_json` already does | 4.7 s for Python, 7.8 s for all three | None. Stdlib only, and holds for every kit. | (a) Python cross-file ambiguity must be at most 1% with import awareness. (b) Shell and JS ambiguity must fall below 10% once edges are scoped to `source`d files and the caller's kit directory. | (a) **Passed**: 11 of 1,997. (b) **Open.** Name-only ambiguity is 45% for shell and 46% for JS. The build must run (b), and A loses for shell and JS if it fails. |
| **B. universal-ctags** | A tag file of definitions | Python, shell, JS and Markdown parsers exist. PowerShell does too, but there is none here. | No. Its reference tags record imports, not calls. | Yes, with `--sort` | Not measured (not installed) | An external binary. Breaks stdlib-only. | Ask it for a call-site role in Python and shell. | Not run (not installed). Rejected on documented capability: it has no call-site role for Python or shell, so it cannot give the owner a caller map. |
| **C. tree-sitter tags** | A grammar plus `tags.scm` queries for `@definition.*` and `@reference.call` | Python, bash and JS grammars | Yes, but by name only | Yes | Not measured (not installed) | Binary wheels or a CLI, plus grammars. Breaks stdlib-only. | Must produce an edge or definition that A misses, or parse a file A refuses. | Not run. Its `@reference.call` captures name only, the same resolution that left 29-46% ambiguous in probe 1. A's tokenizers already parse all 148 shell and JS files with no failures, so C has no measured edge left to win. Rejected unless the build's test shows such an edge. |
| **D. SCIP or LSIF** (scip-python, scip-typescript) | A compiler-grade index with resolved symbols | Python and JS only. No bash indexer. | Yes, resolved | Mostly. The metadata includes tool versions. | Not measured (not installed) | node or npm packages and pyright | Shell must be covered. | **Loses.** 128 of 236 code files are shell, and so are 875 of 1,012 script-invocation sites. |
| **E. Runtime tracing** (`sys.setprofile` during the self-tests) | Records the calls that actually execute | Python only | Yes, the observed ones | **No.** Edges depend on which test paths ran. | Requires running the self-tests, which this pass forbids | None | Two runs must produce byte-identical output. | Not run. Its mechanism fails the determinism test, and shell is untraced, so it loses either way. |

**Reuse tools**

| Tool | What it answers | Evidence | Verdict |
|---|---|---|---|
| `reuse_lookup.py` | A stem-matched, fan-in-ordered shortlist over `symbols.json` and the dossiers | 0 of 24 cases solved (handed). My probe ranked test helpers first, with a median of 110 candidates shown and none ever empty. 285 logged runs, but no signal of whether any helped. | **Retire the ranker.** The M1c scout (16 of 24, handed) succeeds by reading a generated house index, so the generated index is the part worth keeping. Retiring it means editing these places that cite it: `AGENTS.md:122`, `coding-governance-agents.template.md:121`, `BUILD-METHOD.md:156`, `SESSION-KICKOFF.md:106`, `TEMPLATE-SPEC.md:297`, `.claude/agents/gov-reuse-scout.md:15` and `memory/map/README.md:35`. |
| `memory-recall` (`query.py`) | FTS5 search over memory Markdown and three declared conf files | records fts5 r@5 0.83 on 12 queries. 570 queries logged. Only 5.5% were followed by a read of a hit it showed. | **Redesign it under the declared memory conventions, as a record finder in the knowledge expansion. Remove it from the code-reuse obligation**, because it holds no code. Reading chunks is where it is weakest: 0.00 in the bench, and 92 of 121 recorded reads went to files it never showed. |

## Pick

**Candidate A**, extending the existing seam. It is the only candidate that:
- covers shell, which is most of this repository's code;
- sees the 1,012 cross-language invocations;
- keeps every kit stdlib-only;
- produced a measured result on the real tree: 2,857 resolved Python edges, 11 ambiguous sites, 7.8 s for all three languages.

Its open risk is the build's first test. Edges for shell and JS, scoped to `source`d files and the caller's kit directory, must fall below 10% ambiguity. If they do not, those two languages ship as "mentions" rather than "callers", and the gap is stated out loud.

Retire `reuse_lookup.py` as a ranker, and let the caller map plus a scout's census replace it. Keep `memory-recall` as a record finder with the narrower role.

Probe scripts (scratch, outside the repository): `C:\Users\d41ly\AppData\Local\Temp\rprobe\count.py`, `C:\Users\d41ly\AppData\Local\Temp\rprobe\graph.py` and `C:\Users\d41ly\AppData\Local\Temp\rprobe\pyimp.py`.
