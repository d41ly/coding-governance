# Wave 1 — Lens 1: dead code, made trustworthy

**Serves:** research TOOL-aScouredKit-1

## Verdict: CLEAN WITH FIXES


**Subject:** the whole repo at `093730e40355d6a04300966f791f2634379e8b45`.
**Question the lens was given:** the repo reports an unused-export / fan-in number. Learn what it
structurally cannot see, then turn it into a list somebody can act on.

**Headline.** The number is `dead_exports: 412`. All 412 are live. Every one was verified by an
exhaustive search across the seven ways a symbol is reached in this repo. The metric's *positive*
verdict is no better: 63% of every fan-in edge in the corpus is a file that DEFINES a symbol of the
same name rather than one that references it, and the three highest-scoring "seams" in the repo are
`pathlib.Path.read_text`, `pathlib.Path.resolve` and `re.search`. Two shipped consumers act on that
ranking, one of them by writing to a tracked file.

Actual dead code found by exhaustive search, outside the metric: **one** shell function pair.

---

## What computes the number

`tools/codebase-map/map_lib.py`

- `build_reference_index()` (`:797`) walks the top-level dirs named by `generated/symbols.json`,
  filtered to the extension set present in that same file, and builds `token -> {files}` from
  `_identifier_tokens()`.
- `_identifier_tokens()` (`:667`) is a genuinely good language-aware comment/string stripper. What
  survives it is `_IDENT_TOKEN_RE = [A-Za-z_$][\w$]*` over the remaining CODE. That is every
  identifier: function names, class names, **local variables, parameters, keyword-argument names,
  object properties, and attribute names after a dot**.
- `fan_in(index, symbol_id, def_file)` (`:823`) = `len(index.get(symbol_id, set()) - {def_file})`.

Two structural properties fall straight out of those three lines, and both matter more than the
docstring's stated ceiling ("over-counts a common id (`get`), under-counts registry/dynamic
dispatch"):

1. **The def file is the only exclusion.** A module-private helper called twenty times inside its own
   file has fan-in 0.
2. **There is no symbol resolution at all.** `foo.read_text()` and a function called `read_text`
   produce the same token. So do a local variable named `tree`, a kwarg `check=True`, and a JS object
   property `report:`.

Corpus at this SHA: `generated/symbols.json` carries 701 rows across 48 files, all under `tools/`,
extensions `.py` (647) and `.js` (54). `build_reference_index` therefore scans 53 files — `tools/**/*.{py,js}`.
`.codebase-map.conf` declares `RECALL_DARK_LAYERS="bash"`, which is honest and correctly surfaced,
but it means the 84 tracked `.sh` files that are most of this product contribute neither symbols nor
reference edges.

---

## (a) FALSE POSITIVES

### a1. The fan-in-0 half — `dead_exports: 412`, of which 0 are dead

Reproduced with the kit's own code (`build_reference_index` + `fan_in` over the committed
`symbols.json`), then classified:

| class | count | why it is live |
|---|---:|---|
| module-private helper, referenced inside its own file | **385** | `fan_in` subtracts the def file. AST-verified: each id appears as an `ast.Name` / `ast.Attribute` / `ast.keyword` inside its own module. |
| decorator-registered test arms in `tools/memory-recall/test_recall_floor.py` | 20 | `@check("…")` at `:57` registers each at import time. The file is gate leg **"recall floor arms"** (`python3 tools/memory-recall/test_recall_floor.py`) in `tools/gate-legs.json`. |
| pytest plugin hooks in `tools/pytest-parallel-guardrails/crashprobe.py` | 4 | `pytest_configure`, `pytest_sessionfinish`, `pytest_runtest_logstart`, `pytest_runtest_logfinish` — dispatched by pytest's hookspec machinery. |
| arms in `aiosqlite_worker_resilience.test-template.py` | 2 | a `.test-template.py` instantiated into an adopter's repo. |
| `bench.expected_hits` (`tools/memory-recall/bench.py:369`) | 1 | genuinely unreferenced — **but** `bench.py` is declared **verbatim**, byte-pinned in `verbatim.json` and asserted by `selftest.py` (`tools/memory-recall/README.md:196`, `memory/map/features/memory-recall.md:47`). Vendored. Out of scope, and deleting the function would red the pin. **Not filed.** |

**385/412 = 93.4% is the single class the printed caveat does not name.** The line reads
`dead_exports: 412 symbol(s) with fan-in 0 (a hint - a used dup is not dead)` — "a used dup" is the
smallest class present, not the dominant one.

Verification commands:

```
python - <<'PY'   # fan-in distribution over the committed corpus
import sys, json, collections; sys.path.insert(0,'tools/codebase-map'); import map_lib as m
s=json.load(open('memory/map/generated/symbols.json'))['symbols']
idx=m.build_reference_index([x['file'] for x in s])
print(collections.Counter(m.fan_in(idx,x['id'],x['file']) for x in s))
PY
# -> fan-in 0: 412 of 701

python tools/codebase-map/map_diff.py HEAD..HEAD --converge | tail -2
# -> dead_exports: 412 symbol(s) with fan-in 0 (a hint - a used dup is not dead)
```

The 27 non-private candidates were then AST-verified (no `ast.Name`/`Attribute`/`keyword` reference
inside the def file) and each was hand-checked against the seven reachability channels: `gate-legs.json`
argv, `kit.toml` `[check]`/`[adopt]`/`[[gate_leg]]`/`[[hole]]` argv, `*.test.sh` / `selftest.py`,
`.claude/settings.json` hooks, Skill markdown, waiver/limits `.txt` files, and `check-wiring.sh`.

### a2. The positive half — the SEAM verdict is 43% wrong on the same math

165 symbols score at/above `SEAM_FANIN_THRESHOLD=3`. Over the whole corpus there are 2,561 fan-in
edges; **1,626 of them (63%) are a file that defines a symbol with the same id.** Restricted to the
seam set: 1,598 of 2,396 edges (67%). **71 of the 165 seams fall below the threshold once
sibling definitions are discounted.**

Four distinct contamination classes, each verified against real lines:

| class | example | measured |
|---|---|---|
| sibling definition of the same name | `main` | defined in 35 files; fan-in 34; **34/34** are the other 35 files' own `main`. Same shape: `cmd_report` (5 defs, 4/4), `Problem` (5 defs, 4/4), `cmd_check` (4/4), `read` (5/7). |
| **stdlib/library attribute after a dot** | `read_text` | defined once (`gen_build_index.py`); fan-in **29**; **29/29** are `Path(...).read_text(encoding="utf-8")` calls. `map_diff.py:120`, `map_lib.py:187`, `gen_map.py:262`, … |
| same | `resolve` | fan-in **25**, 25/25 are `pathlib.Path(__file__).resolve()`. |
| same | `search` | fan-in **21**, 21/21 are `re.search(...)` / `_TOML_FENCE_RE.search(...)`. |
| same | `parse_args` | fan-in **9**, 9/9 are `parser.parse_args()` / `ap.parse_args(argv)`. |
| local variable / parameter name | `tree` | fan-in 11; e.g. `map_diff.py` `tree = m.load_map_tree(...)` — a local, unrelated to `selftest.py`'s `tree()`. |
| keyword-argument name | `check`, `key` | `subprocess.run(..., check=True)`, `sorted(..., key=lambda …)`. |

None of these are speculative — each was produced by diffing `build_reference_index`'s own index
against the `symbols.json` definition map and then reading the cited lines.

### a3. Both shipped consumers act on the contaminated ranking

**`gen_map.py --seed-affordances`** (`tools/codebase-map/gen_map.py:182`, via
`reuse_lookup.seed_affordances` at `reuse_lookup.py:249`) is the "bounded big-bang worklist" — the
tool that tells an operator which symbols to declare as `## Reuse affordance` seams in dossiers. Run
at this SHA:

```
# seed-affordances: top 15 undeclared seams (fan-in >= 3)
- main       [fan-in 34 | tools/settings-merge.py]
- read_text  [fan-in 29 | tools/memory-tree/gen_build_index.py]
- key        [fan-in 26 | tools/memory-tree/merge-rows.py]
- run        [fan-in 26 | tools/settings-merge.py]
- resolve    [fan-in 25 | tools/memory-recall/recall_conf.py]
- search     [fan-in 21 | tools/memory-recall/query.py]
- check      [fan-in 18 | tools/memory-recall/test_recall_floor.py]
- load_conf  [fan-in 18 | tools/memory-tree/row_grammar.py]
- write_text [fan-in 18 | tools/memory-tree/gen_build_index.py]
- write · repo_root · why · tree · parse · parse_args
```

Fifteen of fifteen are junk. Following that worklist writes fiction into fifteen dossiers — the exact
"map rots into fiction" outcome the kit exists to prevent, and it arrives with the kit's own
authority.

**`map_diff.py --converge`** routes the same math into a **write**. `collision_flags` flags a new
symbol that shares a token stem with an existing high-fan-in seam it did not wire through, and
appends each to `<MAP_ROOT>/reinvention-backlog.md`. Run over `HEAD~60..HEAD`:

```
collision_flags: 31
- WARN main [tools/govkit/fixtures/make_incms_receipt.py] resembles seam main (fan-in 34) …
- WARN check_read_path [tools/memory-tree/corpus_ids.py] resembles seam read_text (fan-in 29) …
- WARN read_gov_blob / read_gov_text / read_gov_tree … resembles seam read_text (fan-in 29) …
- WARN parseBranches [tools/hooks/agent-cap.js] resembles seam parse_args (fan-in 9) …
  -> 31 row(s) appended to memory/map/reinvention-backlog.md
```

The generated table's first data row is literally `| main | main | … | 34 | function | medium |` —
fold `main` into `main`. At minimum **12 of the 31 rows name a "seam" that is not a symbol anybody
can wire through**: 1× `main` (34/34 sibling defs), 4× `read_text` (29/29 `Path.read_text`), 3× `read`
(5/7 sibling defs), 1× `cmd_report` (4/4 sibling defs), 1× `parse_args` (9/9 `ArgumentParser.parse_args`),
1× `tree` (locals), 1× `load_conf` (8/18 sibling defs). The remainder are stem collisions against
seams that are real (`lf`, `map_root`, `build_reference_index`) — those are the stemmer's documented
ceiling, not this defect.

The file is append-only and deduped by `(new, resembles)`, so the noise is permanent once committed.
`memory/map/reinvention-backlog.md` was untracked at this SHA; the run above created it and **it was
deleted again** — `git status` is back to baseline (`A memory/builds/aScouredKit/RUN.md` only).

**The suggested fix, and it is small.** In `fan_in`, subtract the files that define a symbol of the
same id (the caller already has `symbols.json`), and have `build_reference_index` record whether a
token occurrence was dot-prefixed so an attribute-only file can be dropped. Both are cheap and both
are on-demand code — no committed artifact changes, no gate moves. Alternatively: keep the number and
stop letting `--converge` and `--seed-affordances` *write* from it.

---

## (b) TRUE DEAD CODE

The metric cannot see shell at all (`RECALL_DARK_LAYERS="bash"`, correctly declared), so shell was
swept independently: 541 function definitions across 84 tracked `.sh` files, each checked for any
word-boundary reference in its own file, in every other tracked `.sh`, and in every other tracked
file outside `memory/builds` and `memory/archive`.

**`tools/unattended/unattended.sh:498` — `is_scope()`, one occurrence in the entire repository.**

```sh
scopes()      { printf 'all %s\n' "$AUTH_MODES"; }          # :496
is_scope()    { case " $(scopes) " in *" $1 "*) return 0;; esac; return 1; }   # :498
```

`git grep is_scope` returns exactly that one line. A filesystem grep including untracked files returns
the same one line. There is no indirect invocation: the only `eval`-of-a-function-name in the kit is
`unattended.test.sh:3668`'s `slice_fn`, which slices literal names. Its three siblings are all live —
`is_auth_mode` (`:1325`), `is_second_anchor_mode` (`:1346`), `is_terminal` (`:1230`, `:1543`, `:2033`,
`:2365`, `:2640`). `scopes()` at `:496` has no caller other than the dead `is_scope`, so **both are
dead**.

Two things make this more than a tidy-up:

1. **It is a new instance of `memory/gotchas/two-readers-of-one-config-one-re-derived`.** The comment
   directly above `scopes()` says the scope set is *"DERIVED, never a second constant … Deriving it is
   what stops the two disagreeing — a second literal would need editing in step with this one, and the
   pair that already existed did not."* The set's only real consumer is
   `tools/unattended/check-unattended.sh:197`, which builds it a second time:
   `AUTH_SCOPES="all $AUTH_MODES"` — reading `AUTH_MODES` back out of the driver with `core_of` and
   re-concatenating `all` by hand. The derivation the comment defends is the unreachable one.
2. **Nothing validates a directive's scope field.** `scope_of()` (`:482`) returns the third field of a
   `DIRECTIVES_EXTRA` entry, defaulting to `all`. Its one consumer, `check_waiver_scope` (`:1139`),
   compares it against `all` and `$AUTH_MODE` and nothing else. A project that writes a typo'd scope
   into `.unattended.conf` gets a directive that is permanently unwaivable, refused by `fail 45` with a
   message blaming the *run's mode* rather than the malformed declaration. `is_scope` is exactly the
   membership test that would have named it.

Fix: delete both, or call `is_scope` in `check_waiver_scope` and make `check-unattended.sh` read
`scopes` through the driver instead of re-deriving `AUTH_SCOPES`. Not tracked in
`memory/backlog/TOOL.md` or `DEPL.md` (`grep -n "is_scope\|scopes()\|scope_of\|AUTH_SCOPES"` → no rows).

### Nothing else survived

The rest of the hunt came back clean, which is worth recording so it is not re-run:

- **Whole dead files.** All 221 tracked files under `tools/`, `skills/`, `.githooks/` were checked for
  any mention of their basename in any other tracked file. Two hits, both false: the flattened
  `tools/unattended/fixture-records/tools~unattended~fixture-pieces~one~piece.md.md` pair, constructed
  by path-mangling at runtime.
- **Executables reachable only by tests.** One hit: `tools/govkit/check_runbook_parity.py`. **Already
  tracked** as `TOOL-dScaffoldedMirror-15` (backlog line 217) and its recorded measurement is still
  exact — re-ran it, still 18 problems, 7 anchored sections, 25 registry entries, exit 1. Not
  re-filed, and not worse.
- **Modules imported only by their own tests.** None.
- **Module-level constants with no reader** (AST, every `tools/**/*.py`, cross-checked against every
  tracked non-`memory/` file). Zero.
- **Shell variables assigned at column 0 and never expanded anywhere.** Zero.
- **Dead JS functions** across all 10 tracked `.js` files. Zero.
- **Config keys declared with no reader** — all 66 keys across `.codebase-map.conf`, `.lexicon.conf`,
  `.memory-tree.conf`, `.unattended.conf` have a `.py`/`.sh`/`.js` reader.
- **Declaration files naming paths that do not resolve** — all 8 `tools/*.txt` and 8
  `memory/project/*.txt` registries: every path-shaped token resolves.
- **Env flags read but nameable by nobody.** Six reads with no other mention; all are either
  OS/tool-provided (`NUMBER_OF_PROCESSORS`, `PYTEST_XDIST_WORKER`), test-local
  (`FLOOR_OVERRIDE`, `DFLOOR_OVERRIDE`), or undocumented-but-live escape hatches
  (`GOV_REMOTE` at `tools/push-main.sh:27`, `PLAYBOOK_PY` at `tools/playbook/adopt-playbook.sh:48`).
  Not filed — an undocumented override is a docs gap, not dead code.

The negative result is the interesting half: at the level a fan-in metric operates on, this repo is
clean. The 412 it flags are the metric's error bar, not the repo's debt.

---

## Working-tree note

`map_diff.py --converge HEAD~60..HEAD` created `memory/map/reinvention-backlog.md` as a side effect.
It was removed. `git status --porcelain` at the end of this pass shows only
`A  memory/builds/aScouredKit/RUN.md`, which was staged before this review started.
