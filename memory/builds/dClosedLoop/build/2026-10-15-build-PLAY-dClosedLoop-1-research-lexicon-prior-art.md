# Research: the lexicon kit, prior art and the forced-name mechanism

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 29's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-10-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`.

---

# Research C: keeping forced names out of lexicon debt (prior art and mechanism)

## Inventory

**Where P1 grades today, read from the code:**

| Seam | Location | What it does |
|---|---|---|
| Python extractor | `tools/lexicon/lexicon.py:425-456` | `ast.walk` collects every `FunctionDef`, including methods and dunders. It records no class context and no bases. |
| P1 loop | `tools/lexicon/lexicon.py:2941-2965` | Every extracted function whose `leading_verb` is not in VERBS becomes an offender. Nothing about a definition's origin is consulted. |
| `leading_verb` | `tools/lexicon/subtokens.py:39-48` | Strips leading `_` first, so `__str__` grades on `str` and `__init__` on `init`. |
| Name allow-list | `tools/lexicon/lexicon-verb-waivers.txt:1-8` | Keyed on the matched text, with a reason per row. Its header says the pin is a two-sided equality, which the settled `shrink-only` default will contradict. |
| Decorator accessor | `lexicon.py:2527-2573`, `lexicon_conf.py:72` (`SELECTOR_KINDS`) | Records each decorator's last segment per site. It feeds CELLS conventions only: P1 "walks every extracted function … whatever any `CELLS` row says" (`lexicon.py:3743-3750`). |
| Import extraction | `lexicon.py:438-455` | Already yields every import per file. This is the stack-detection seam. |
| VERBS absorbs forced names | `.lexicon.conf:569` (`init`), `:576` (`main`), `:578` (`test`) | The 10 `__init__` definitions grade clean only because `init` is a declared verb. |

There is no manifest-based stack detector anywhere. `git grep` for `package.json|pyproject.toml|requirements.txt` in `tools/lexicon` and `tools/codebase-map` returns only a fixture string (`ts-conformance-fixtures.json:22`), and this repository has no manifest at its root.

**Prior art: how established checkers treat names the user can't change**

| Checker | Mechanism | Evidence |
|---|---|---|
| pylint `invalid-name` | **Inference from inheritance**, plus a **config allow-list**. `visit_functiondef` returns early when `utils.overrides_a_method(...)`, and drops confidence to `INFERENCE_FAILURE` when the bases are unknown. `good-names` defaults to `i,j,k,ex,Run,_`; `good-names-rgxs` adds patterns. | pylint `checkers/base/name_checker/checker.py` (main): option at line 249, override skip at line 425; https://pylint.readthedocs.io/en/stable/user_guide/configuration/all-options.html |
| ruff N802 (pep8-naming) | **Override marker**: "exempts methods decorated with @typing.override". Also a **shipped config allow-list**: `ignore-names` defaults to `setUp, tearDown, setUpClass, tearDownClass, setUpModule, tearDownModule, asyncSetUp, asyncTearDown, setUpTestData, failureException, longMessage, maxDiff`, which is in effect a per-kit table for unittest. `extend-ignore-names` takes globs. | https://docs.astral.sh/ruff/rules/invalid-function-name/ ; https://docs.astral.sh/ruff/settings/#lint_pep8-naming_ignore-names |
| ESLint `camelcase` | **Config allow-list** (`allow`: strings or regex) and **scope switches**: `properties: never`, `ignoreImports`, `ignoreDestructuring`, `ignoreGlobals`. It has no override awareness. | https://eslint.org/docs/latest/rules/camelcase |
| TypeScript `override` | **Override marker, verified by the compiler**. `noImplicitOverride` (TS 4.3) makes an unmarked override an error (4114). typescript-eslint `naming-convention` can select the `override` modifier, and offers `requiresQuotes` plus `filter` for names it can't control. | https://www.typescriptlang.org/tsconfig/#noImplicitOverride ; https://typescript-eslint.io/rules/naming-convention/ |
| PEP 698 `@typing.override` | **Marker**. Checkers treat it as an error "unless that method is overriding a compatible method … in some ancestor". It ships in Python 3.12 and has no runtime enforcement beyond `__override__`. | https://peps.python.org/pep-0698/ |
| RuboCop `Naming/MethodName` | **Config allow-list** (`AllowedPatterns`, whose doc example is a callback name) plus `ForbiddenIdentifiers`/`ForbiddenPatterns`, and `# rubocop:disable` at the site. It does not infer inheritance. | https://docs.rubocop.org/rubocop/latest/cops_naming.html |
| Checkstyle | **Java's `@Override` marker**. `MethodName` "Does not check-style the name of an overridden method[s]". `ParameterName.ignoreOverridden` "skip[s] methods with Override annotation" (default false). | https://checkstyle.org/checks/naming/methodname.html ; https://checkstyle.org/checks/naming/parametername.html |
| revive `var-naming` / golangci-lint | **Built-in convention table**: skips `Example*`, `Test*`, `Benchmark*` and `Fuzz*` in test files. **Config allow-list and block-list** of initialisms. **Site suppression** with `//nolint:revive // reason`. **Path and text exclusion rules** in `linters.exclusions.rules`. | https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#var-naming ; https://golangci-lint.run/docs/linters/false-positives/ |

Across these tools: the ones that never exempt a free choice (pylint, TypeScript, Checkstyle) all resolve or verify the base. The ones that ship tables (ruff, revive) key them on names that are namespaced by convention, or on a well-known framework list.

## Sequence

1. I ran the kit's reporting verbs, `--offenders` and `--list`, to get the population.
2. I read the P1 path, the extractor, `leading_verb`, the decorator seam and the waiver file.
3. I wrote a read-only override-resolution prototype in the scratchpad and ran it twice over the 108 tracked `.py` files.
4. I introspected stdlib tables and tested them for name collisions against the real offenders.
5. I sized the pytest, Django, Flask, Starlette and FastAPI tables by parsing downloaded wheels with `ast` (no import), and React and Node from `@types` `.d.ts` files. All downloads went to the scratchpad only.
6. I probed shell and JavaScript for host-fixed names.

The worktree outside `memory/builds/dClosedLoop/` stayed clean (`git status --porcelain` filtered: empty).

## Measurements

**Population:**
```
$ python tools/lexicon/lexicon.py --offenders | cut -f2 | sort | uniq -c   (exit 1, 6.1 s)
      1 problem      6 sh.function.conv     1088 verb
$ python tools/lexicon/lexicon.py --list | tail -2
lexicon: P1 verb   graded=5710 offenders=1088 (debt=87 + unruled=1001) waived=0
by extension: sh 611 · py 439 · js 38
```
This disagrees with the record: the live count is 1088 against `VERB_OFFENDER_PIN="1087"` at `.lexicon.conf:268`. Classifying that is Researcher B's work.

**Python override resolution (prototype `proto.py`).** It resolves bases through each module's imports. Bases inside the corpus are resolved by AST only, never imported. Bases outside it go through `importlib`, then `hasattr` and the MRO owner.
```
method defs by (resolution, is_offender):
  ('ext', False) 10     ('ext', True) 1     ('free', False) 8     ('free', True) 10
@override decorators in corpus: 0
EXT-forced offenders:   tools/lexicon/lexicon.py  Offender.__str__  <- builtins.object
EXT-forced NON-offenders: {'__init__': 10}
LOCAL-inherited offenders: (none)     UNRESOLVED bases: Counter()
run 1: 5064 ms   run 2: 4993 ms   identical
```
The tree has 3,345 Python function definitions but only 66 classes, almost all of them `Exception` leaves, so inheritance accounts for very little here. The prototype marks **1** offender.

**Other forced Python names:**
```
$ git grep -n "def pytest_" -- '*.py'
tools/pytest-parallel-guardrails/crashprobe.py:147,160,166,172  (pytest_configure, _runtest_logstart, _runtest_logfinish, _sessionfinish)
$ python -I -c "import pytest"   ->  ModuleNotFoundError: No module named 'pytest'
pytest-9.1.1 wheel, _pytest/hookspec.py parsed: 52 hookspecs; all 4 above are members -> [True, True, True, True]
```
Two problems show up here:
- These hooks are module functions, so inheritance inference can't see them.
- Their marker is aliased (`_hook_trylast = pytest.hookimpl(trylast=True)`, `crashprobe.py:45-47`), so `extract_decorators` records `_hook_trylast` and not `hookimpl`.

**Forced offenders on this tree: 5 of 1,088 (0.46%)**, namely `__str__` and the 4 pytest hooks.

- **JavaScript:** there are 0 `class … extends` in the 21 tracked JS files, and all 38 JS offenders are free helpers.
- **Shell:** the protocol-shaped offenders are `cleanup` ×4, `usage` and `setup_repo`. All are free choices (trap handlers and local helpers). The `declare -F` probes (`tools/unattended/check-pass-order.sh:145`, `tools/run-gates/post-merge.sh:355`) check in-repo protocols that gov chose itself. Git hook names are filenames, which P1 does not grade.

**Name-keyed tables against this tree (`stdtab.py`):**
```
stdlib public classes: 1047   distinct method names: 2306   distinct leading tokens: 1045
curated bases: 35   distinct overridable names: 369   rows (base,name): 1270
name-keyed whole-stdlib names: exempts 53 -> ['__str__','_bind','_dump','_quote','acct','clean','cleanup','commit',
   'digest','discover','dump','emit','empty','expect','fail','keys','lineno','merge',...,'reset','search','skip','walk']
VERB-keyed whole-stdlib names: exempts 202 of 1088
name-keyed curated-bases names: exempts 21 -> ['__str__','dump','emit','fail','keys','reset','sections']
VERB-keyed curated-bases names: exempts 99 of 1088
```
Every one of these sets is forced only for `__str__`. The rest are free choices.

**Table sizes and production:**

| Kit | Produced by | Size | Versioned by |
|---|---|---|---|
| Python object and dunders | `inspect`/`vars(object)`, plus the data model | about 80 names, namespaced `__x__` | Python minor |
| stdlib commonly-subclassed bases (unittest, argparse, ast, http.server, logging, threading, html.parser, cmd, json, collections.abc …) | `inspect`/`dir()` on 35 curated bases | 1,270 (base, name) rows, 369 names | Python minor |
| pytest via pluggy | AST of `_pytest/hookspec.py`, or `pluggy` `HookspecMarker` | 52 (9.1.1) | pytest version |
| Django | AST of the wheel's class bodies; full MRO needs import or AST MRO | 342 own-method rows over 14 of 23 bases (mixins under-count) | Django 6.1.2 |
| Flask / Starlette / FastAPI | AST of the wheel | 92 / 24 / 59 rows | 3.1.3 / 1.8.0 / 0.143.2 |
| React | `@types/react` `index.d.ts` 19.3.0 (`ComponentLifecycle` and `function use*`) | 9 lifecycle names (plus `render` and the statics), 18 hooks | `@types/react` version |
| Node core events, Express | `@types/node/events.d.ts`, `@types/express-serve-static-core` | 0 forced definition names: event names are string arguments and handlers are anonymous signatures | none needed |
| Shell hosts (bats `setup`/`teardown`/`*_file`, bash `command_not_found_handle`, zsh `precmd`/`preexec`/`chpwd`) | curation | about 8 | host version |

**Stack detection on this tree.** It has no manifest. An import census over the extractor's output finds `{'pytest': 2, 'numpy': 2, 'sklearn': 2, 'model2vec': 1, 'aiosqlite': 4, …}`, so imports detect the stack where manifests can't. Manifest files (`pyproject.toml`, `requirements.txt`, `package.json`, `composer.json`) would give version pins, and the import census gives which modules are actually in use.

## Gaps

| # | Gap | Evidence |
|---|---|---|
| G1 | P1 records no class context or bases, so it can't tell an override from a free definition. | `lexicon.py:433-437`, `2941-2965` |
| G2 | The decorator seam stops short of P1, and it keys on the last segment, so an aliased marker is invisible. | `lexicon.py:3743-3750`; `crashprobe.py:45-47` |
| G3 | Live `importlib` resolution depends on each node's environment, while the pin must match on every node. | `ModuleNotFoundError: pytest` on this node |
| G4 | Dynamic-dispatch protocols are not attributes of their base: `ast.NodeVisitor.visit_*`, `BaseHTTPRequestHandler.do_*`, `cmd.Cmd.do_*/help_*/complete_*`. `hasattr` misses them, so a table needs (base, prefix) rows. | stdlib behaviour; absent from this tree |
| G5 | VERBS mixes forced names with vocabulary: `init` exists partly to clear `__init__`. | `.lexicon.conf:569`; 10 `__init__` absorbed |
| G6 | Forced names are 5 of the 1,088 offenders here, so whatever agents are labelling "third-party verbs" is mostly not forced by any mechanism I could detect. That is Researcher B's classification to confirm. | Measurements |

## Candidates

| Id | Mechanism | Test that could make it lose | Result |
|---|---|---|---|
| **K1** Name allow-list in config, shipped per-kit (pylint `good-names`, ruff `ignore-names`, ESLint `allow`, RuboCop `AllowedPatterns`; today's waiver file) | Exempt any definition whose name or token is listed | A shipped table must exempt **0** free choices on this tree. | **Loses.** Whole stdlib: 53 sites, 1 forced. Curated bases: 21 sites, 1 forced. Verb-keyed: 99 to 202, about 0 forced. Only namespaced rows (`__*__`, `pytest_*`) survive, and those are folded into K4. |
| **K2** Site override marker (PEP 698, TS `override`, `@Override`; ruff N802, Checkstyle, ts-eslint modifier) | Exempt a definition carrying `@override`/`override`/`hookimpl` | (a) It must cover ≥80% of forced offenders with no source edits. (b) A marked non-override must red. | **Loses as default.** (a) It covers 0/5: there are 0 `@override` here, the pytest hooks are not overrides, and `hookimpl` is aliased. (b) The lexicon can't verify a marker without K3's resolution, and an unverified marker is K5. |
| **K3** Live inheritance inference (pylint `overrides_a_method`) | Resolve bases through imports, then `importlib` + `hasattr`, and exempt where the defining class is outside the corpus | (a) It must exempt 0 free choices. (b) It must give the same count on two nodes. (c) It must cover ≥80% of forced offenders. | (a) **Passes:** 1 marked, 0 in-corpus or unresolved. (b) **Loses** by construction (G3), and it runs adopter package import side effects inside a read gate. (c) **Loses:** 1/5. |
| **K4** Generated, versioned per-kit tables keyed by **(base qualname, member)**, **(base, prefix)** and **(host, name or namespace)**. They are applied only at sites statically resolved through imports (K3's walk run against committed data, never a live import). Unresolved sites stay graded and are reported. | Tables are generated by introspection (`inspect` per Python minor, wheel AST for pip kits, the pluggy hookspec module, `.d.ts`), and curated for shell. Each carries a header with the kit, version range and generator command. The stack is detected from the import census, with manifests for versions. | (a) It must cover ≥80% of forced offenders. (b) It must exempt 0 free choices. (c) Output must be byte-identical across two runs and two environments, with no adopter imports. | **Passes on this tree.** (a) 5/5 (`object.__str__` plus 4 of the 52 hookspecs). (b) 0. (c) Identical across two runs. A cross-node run is the test the build must run. The 5-name sample is thin evidence, so the build owes a fixture: a Django CBV, a React class component, a `NodeVisitor`, a pytest plugin, a bats file. It must clear every forced name there and clear no same-named free module function. |
| **K5** Site suppression comment (`# noqa`, `//nolint`, `eslint-disable`, `rubocop:disable`, a future `gov:note`) | Exempt a definition carrying a reasoned comment | It must exempt 0 free choices. | **Loses** by construction: any agent can stamp any name, which is the pin-raising habit the owner reports in a different form. It survives only as an owner-visible fallback for undetectable host protocols, counted and printed, with a reason required. |

**Cost and determinism, per language:**

- **Python:** K4's resolution is an AST walk of the files already parsed (the prototype took about 5 s; the leg ceiling is 300 s). It is deterministic given committed tables.
- **JavaScript:** `class X extends Y` with `Y` imported is a regex probe under `js:js-regex:probe` (`.lexicon.conf:24`). It is cheap and deterministic but only probe-accurate. This tree has nothing to apply it to.
- **Shell:** keyed on the host (a `.bats` extension or shebang) plus a curated name list. The cost is near zero and it is deterministic. This tree has 0 shell forced names.

## Pick

**K4, generated per-kit tables resolved at the site against committed data.** It is the only candidate that passes all three losing tests on the real tree: 5/5 forced names covered, 0 free choices exempted, byte-identical output. It combines pylint's and Checkstyle's rule (exempt only what a base outside the corpus defines) with ruff's and revive's shipped tables, and it drops the live import that would make K3 vary by node.

**How the rest fit around it:**

- **K2** is honoured only as a fast path that K4's resolution verifies: an `@override` with no external base reds, following PEP 698's rule.
- **K5** stays as an owner-visible fallback.
- **The waiver file** keeps owner rulings only.
- **The extension points** are `_python_defs` (add class context and bases), `extract_decorators` (resolve aliases) and the import extraction at `lexicon.py:438-455` for stack detection.
- **One VERBS change:** under K4, `init` (`.lexicon.conf:569`) stops being needed to clear `__init__`, and its row should be re-justified as vocabulary or removed.

The prototypes and downloaded material are in `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\` (`proto.py`, `stdtab.py`, `whtab.py`, `off.tsv`, `list.txt`, `wh\`, `dl\`).
