# TOOL-dMindYourWords-7 — the packs: their file, their loader and the four generators

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 7 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0268@2d14651f whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-7-reuse-scout-b.md](../build/2026-10-29-build-TOOL-dMindYourWords-7-reuse-scout-b.md) | research | TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-5 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

A host kit forces some names: `logging.Handler.emit`, `ast.NodeVisitor`'s `visit_*`, pytest's
`pytest_*` hooks, Python's dunders. This unit ships those names as committed data, one pack per host
kit, each with its kit, version range and generator command. It also ships the one loader every reader
of a pack calls, and the four generators that rebuild the packs: `inspect` per Python minor, the
wheel's syntax tree, pluggy hookspecs and `.d.ts`. Nothing is resolved at grading time by importing a
host package, so every node grades the same. The first wave ships here. The second wave waits on an
adopter census (v2:2000 `[owed]`).

## 2. Scope (IN)

- **S1** — The pack file and its grammar, `tools/lexicon/packs/<name>.toml` (I6, §4 "Data model"):
  header keys `kit`, `versions` (a PEP 440 specifier set), `langs`, `generator` (the command, or
  `curated`) and `families`. Rows sit in four arrays of tables, `member` (`base`, `name`), `prefix`
  (`base`, `prefix`), `host` (`namespace`, `name`) and `shim` (`command`). Observed by AC1, AC2.
- **S2** — The one loader and validator, `load_pack(path)` in `tools/lexicon/pack.py`. It returns a
  `Pack` or raises `PackError` naming the file and the offending row. It refuses the pack whole on any
  of the nine rules in §4 "Validation". Shipped packs and custom packs take the same path. Observed by
  AC1, AC2.
- **S3** — The lookup, `Pack.read_row(base, name, invokes=())`. It returns the row that forces `name`
  given the site's resolved base (a dotted name, or `None` for a module function) and the commands
  its file invokes, or `None` when no row does. It is the only code that matches pack rows. Base
  resolution is TOOL-dMindYourWords-2's. Observed by AC3.
- **S4** — The generator CLI, `tools/lexicon/gen_pack.py`, with the four generator modes `inspect`,
  `wheel`, `hookspec` and `dts`, and the mode `check <pack>...`, which runs S2 over each file. Each
  generator writes the header's `generator` key as the exact command that rebuilds the file. Each
  validates its own output through `load_pack` before writing. Output is deterministic: rows are
  sorted, and the file carries no timestamp, interpreter path or host name. Observed by AC4 to AC8.
- **S5** — `inspect` keyed on a declared Python version and never on the running interpreter.
  `--python <major>.<minor>` resolves that minor's interpreter by running each candidate, and
  introspects inside it under `-I`. A declared module whose source guards a class or a method on a
  platform test is refused unless `--platform <tag>` is given, and the tag then joins the file name.
  Observed by AC4, AC5.
- **S6** — The first wave shipped, four files (§4 "The first wave"):
  - `python-3.12.toml` and `python-3.14.toml`, holding the data model, the commonly subclassed stdlib
    bases, and `unittest`, `argparse`, `ast`, `http.server`, `logging`, `json` and `cmd`;
  - `pytest.toml`, from pytest's hookspecs;
  - `shell.toml`, the curated shell hosts and shims.
  Observed by AC1, AC3, AC4, AC6, AC10.
- **S7** — The second wave specced and not built: Django, Flask, Starlette, FastAPI and React each get
  a pack after an adopter census shows their names offend (v2:2000). This unit ships the `wheel` and
  `dts` generators those packs need, proven on planted inputs, and no pack for those kits. Observed by
  AC7, AC8, AC10.
- **S8** — The docs. A `## Packs` section in `tools/lexicon/README.md` gives the grammar, the nine
  validation rules, the four generator modes, `check`, and the first wave with its generator commands.
  `tools/lexicon/LEXICON.md` gets one paragraph pointing at that section. `KIT_LEXICON_VERSION`
  (`tools/lexicon/lexicon.py:90`) moves. Observed by AC11.

## 3. Non-goals (OUT)

- Applying a pack to a definition: base resolution, the forced check in `measure_pass`, the
  `lexicon.forced` values and the tally are TOOL-dMindYourWords-2's. Markers are TOOL-dMindYourWords-4's,
  `--suggest --base` is TOOL-dMindYourWords-6's, pack selection and custom packs declared in
  `PACKS:` are TOOL-dMindYourWords-8's, and what a family means is TOOL-dMindYourWords-10's.
- Any second-wave pack (S7), and any JavaScript or TypeScript forced-name grading. JS and TS forced
  names are out of the first wave until the extraction primitive yields class membership there
  (lexicon review `[forced]` item 1, :255-258).
- Registering packs as `[[generated]]` rows. `tools/run-gates/regen.py` re-runs those from the tree
  at every landing, and a pack is built from an outside interpreter or wheel (scout B row 7).
- A tag `pack.<kit>` on a forced-name pack. That spelling names a leg pack (TOOL-dWitnessedBar-12),
  and `[[pack]]` rows name instruction packs (PLAY-dOrderedCharter-15 S8).
- A live import of a host package at grading time, or anywhere in `wheel`, `hookspec` or `dts`
  (lexicon review :275-277). `inspect` imports only stdlib modules, inside the declared minor's
  interpreter under `-I`.
- A change to `tools/lexicon/kit.toml`. Its `include = "**"` engine rule already ships every tracked
  file under the kit home, subdirectories included (`tools/govkit/govkit.py:6664-6668`).

### Edges

- **hands-off** `TOOL-dMindYourWords-2` — `load_pack` and `Pack.read_row`, which the forced check calls for every graded definition
- **hands-off** `TOOL-dMindYourWords-4` — `load_pack`, whose `member` rows confirm a marker on an outside base
- **hands-off** `TOOL-dMindYourWords-6` — `load_pack`, which `--suggest --base` answers from without a corpus pass
- **hands-off** `TOOL-dMindYourWords-8` — `load_pack`, the one validator a custom pack declared in `PACKS:` passes through, and `Pack.versions`, the parsed specifier set selection compares
- **hands-off** `TOOL-dMindYourWords-10` — `load_pack`, whose `families` header table is where a pack declares its kit's verb families

## 4. Design

### Evidence

Read at `ba8b3c8c4`. No product file differs from base `ccd1292e`.

- Nothing in `tools/lexicon/` holds a pack, a forced-name row or a generator. `grep -n "pytest_\|setUp"
  tools/lexicon/lexicon.py` finds nothing. The prototypes exist only in records (scout B row 7).
- The kit refuses to import a sibling kit: every non-relative import of a `.py` file beside
  `lexicon.py` names a stdlib module or a file in that directory (`check_self_containment`,
  `tools/lexicon/lexicon.py:2359`). `pack.py` and `gen_pack.py` import only the stdlib, `canon`,
  `subtokens` and `lexicon`.
- `tomllib` is Python 3.11+. The kit's floor today is 3.10 (`lexicon.py:2384-2387`). The policy reader
  every unit of this build calls (I7, `policy.py get`) already imports `tomllib` at module top
  (`tools/policy/policy.py:56`). So a lexicon run that reads a policy key needs 3.11 already, and the
  packs add no new floor.
- Measured on this node, PINNED 2026-10-29: `py -3.12` is 3.12.10 and `py -3.14` is 3.14.5. pytest
  9.1.0 imports under 3.12 from the user site and not under 3.14. Its `_pytest/hookspec.py` holds 52
  module-level `pytest_*` functions, the four hooks `tools/pytest-parallel-guardrails/crashprobe.py`
  defines among them.
- The member sets differ by minor, PINNED 2026-10-29. 3.14 adds `assertEndsWith` and seven more to
  `unittest.TestCase`, and drops `visit_Constant` from `ast.NodeVisitor`. The builtin types' dunders
  are 124 under 3.12 and 127 under 3.14 (`__annotate__`, `__firstlineno__`, `__static_attributes__`).
  So a pack generated from the running interpreter differs between the two, and AC4 discriminates.
- The platform probe, PINNED 2026-10-29 under 3.14. Over the first wave's modules plus
  `socketserver`, only `socketserver` guards classes on a platform test: `hasattr(os, 'fork')` at
  :556, :718 and :737, and `hasattr(socket, 'AF_UNIX')` at :725. `logging`'s two guards wrap module
  functions, not class members.
- On this tree the first wave forces 4 pytest hooks, 2 `__str__` and the `mktemp` shim
  (`tools/unattended/unattended.test.sh:9188`), read off `python tools/lexicon/lexicon.py
  --offenders` at `ba8b3c8c4` (1218 keys). `emit` in `tools/govkit/govkit.py:1641` sits on class
  `Report`, which has no outside base, so it stays debt.

### Data model

```toml
# python-3.12.toml — GENERATED by gen_pack.py; rebuild with `generator`, never edit
kit = "python"
versions = "==3.12.*"
langs = ["py"]
generator = "python {kit}/gen_pack.py inspect --python 3.12 --host-namespace __*__ --host-module builtins … --module logging … --prefix ast.NodeVisitor=visit_ …"
families = {}
member = [
  { base = "logging.Handler", name = "emit" },
]
prefix = [
  { base = "ast.NodeVisitor", prefix = "visit_" },
]
host = [
  { namespace = "__*__", name = "__str__" },
]
shim = []
```

- `kit`: a lowercase token, `[a-z0-9][a-z0-9._-]*`. The pack's source.
- `versions`: a PEP 440 specifier set over release segments only, clauses joined by `,`. Each clause
  is `==`, `!=`, `>=`, `<=`, `>`, `<` or `~=` followed by `N(.N)*`, with a trailing `.*` legal on `==`
  and `!=`. `load_pack` parses it into `Pack.versions`, a tuple of `(operator, release tuple,
  wildcard)`. No `packaging` import, which would be a new external dependency.
- `langs`: the `KNOWN_EXTS` extensions (`lexicon.py:117-119`) the rows apply to. A refinement of I6,
  which had no such key, so the shell pack's exact names never clear a Python definition.
- `generator`: the rebuild command, with `{kit}` the kit-dir token `kit.toml` already spells, or the
  literal `curated`.
- `families`: a table of `<family> = [<verb>, …]`. It may be empty. Its meaning is
  TOOL-dMindYourWords-10's.
- `member`: `base` (a dotted public access path, `json.JSONEncoder` and never `json.encoder.JSONEncoder`,
  because resolution yields the path the source imports) and `name`.
- `prefix`: `base` and `prefix`. The prefix is curated, because `inspect` cannot see a dispatch
  convention.
- `host`: `namespace` (an `fnmatchcase` pattern) and `name` (one member of the closed set). I6 spelled
  the second key `pattern`. It is `name` here because it holds one literal name, never a pattern. That
  refinement is reported to the writers of units 2, 4, 6, 8 and 10.
- `shim`: `command`, an external command a shell function may shadow.

A custom pack (TOOL-dMindYourWords-8) may write the four arrays as `[[member]]` table headers instead.
TOML gives both spellings the same value, so `load_pack` sees one shape. Generators render the
one-line form, which is about half the bytes.

### Validation

`load_pack(path)` reads with `tomllib` and refuses the whole pack, raising `PackError("<path>: <where>:
<rule>")`, where `<where>` is `header` or `<array> #<k>` (1-based). It refuses:

1. a TOML parse error, named with `tomllib`'s line and column;
2. a missing or mistyped header key, or a top-level key outside the nine;
3. a row with a missing key, an extra key or a non-string value;
4. a duplicate row within one array;
5. a malformed `versions` clause;
6. a `langs` entry outside `KNOWN_EXTS`;
7. a `host` row whose `namespace` holds no literal character, or whose `name` does not match its
   `namespace` under `fnmatchcase`;
8. a bare generic token in the by-name set: a `host` row whose `namespace` is an exact name (no `*`
   or `?`), and whose `name` is one subtoken (`subtokens.subtokens`) that is a form in
   `canon.build_form_index(canon.CLUSTERS)`. Those are `setup`, `run`, `emit` and every other spelling
   the canon knows. A namespaced row such as `__init__` under `__*__` is scoped by its affix and
   passes;
9. a `member` or `prefix` row whose `base` is not a dotted name, or a `prefix` that is empty.

### The lookup

`Pack.read_row(base, name, invokes=())` returns `(array, k)` for the first row that forces `name`, or
`None`:

- `member`, when `base` equals the row's `base` and `name` equals its `name`;
- `prefix`, when `base` equals the row's `base` and `name` starts with its `prefix` and is longer;
- `host`, whatever `base` is, when `name` is in the closed set of rows whose `namespace` it matches;
- `shim`, when `name` equals the row's `command` and `name` is in `invokes`.

A free module function passes `base=None`, so only `host` and `shim` rows can force it.

### The generators

- **`inspect`** — `gen_pack.py inspect --python 3.12 [--platform <tag>] --kit python --host-namespace
  '__*__' --host-module <m>… --module <m>… --prefix <base>=<prefix>…`. `resolve_interpreter("3.12")`
  runs `py -3.12`, then `python3.12`, then `python3.12.exe`, each with `-c` printing
  `sys.version_info[:2]`. It keeps the first that prints `(3, 12)` and refuses naming the three it
  tried. Running each candidate is the rule `tools/lib/resolve-python.sh` states for the MS-Store
  stub. The child runs `-I -c <script>`, with the script embedded in `gen_pack.py`, and prints JSON:
  - for each `--module`, each public class it exports (`__all__`, else every name not opening `_`),
    keyed `<module>.<Name>`, with the names bound across its MRO (`object` excluded) to a function,
    `classmethod`, `staticmethod` or method descriptor, dunders excluded;
  - for `--host-module`, every `__*__` name in the `__dict__` of every class those modules export.

  The parent turns the JSON into rows, adds the `--prefix` rows, and refuses a `--prefix` base the
  child did not report. A `--module` whose source the platform probe flags is refused unless
  `--platform` is given. The probe is an `ast` walk for an `if` whose test reads `sys.platform`,
  `os.name`, or `hasattr(os|socket|sys, …)`, wrapping a class, or a method inside a class. With
  `--platform <tag>`, the output is `python-<minor>-<tag>.toml`.
- **`wheel`** — `gen_pack.py wheel --dist <path.whl|dir> --kit <k> --base <pkg.mod.Class>…`. It reads
  the archive with `zipfile`, or the directory, and never imports. It finds `pkg/mod.py` or
  `pkg/mod/__init__.py`, parses it with `ast`, and takes each declared class's methods, dunders
  excluded. It follows a base the same distribution defines, resolved through that module's imports.
  `versions` is `==<major>.<minor>.*` of `Version:` in `*.dist-info/METADATA`.
- **`hookspec`** — `gen_pack.py hookspec --dist <path.whl|dir> --kit pytest --module _pytest/hookspec.py
  --namespace 'pytest_*'`. It uses `wheel`'s reader. Every module-level function of that module whose
  name matches the namespace is a `host` row, which is how pluggy's `add_hookspecs` collects them.
  Undecorated hookspecs are therefore included.
- **`dts`** — `gen_pack.py dts --dir <package dir> --kit <k>`. It reads every `*.d.ts` under the
  directory through `scan_ts_tokens` (`lexicon.py:950`). For each `class` or `interface` opened at
  depth 0, optionally after `export` and `declare`, it takes each member identifier followed by `(`,
  `?(` or `<` at brace depth 1. Each becomes a `member` row with base `<kit>.<Name>`.

### The first wave

| File | Generator | Rows (PINNED estimate, 2026-10-29) |
|---|---|---|
| `python-3.12.toml`, `python-3.14.toml` | `inspect`, host modules `builtins`, `collections.abc`, `contextlib`, `functools`, `types`, `os`; modules `logging`, `logging.handlers`, `unittest`, `argparse`, `ast`, `http.server`, `json`, `cmd`, `threading`, `html.parser`, `string`, `contextlib`, `queue` | about 1100 member, 8 prefix, about 125 host each |
| `pytest.toml` | `hookspec` over pytest 9.1.0, `versions = "==9.1.*"` | 52 host |
| `shell.toml` | `curated`, `langs = ["sh"]`, `versions = ">=0"` | 7 host, 5 shim |

- The `prefix` rows are `ast.NodeVisitor` and `ast.NodeTransformer` with `visit_`, `cmd.Cmd` with
  `do_`, `help_` and `complete_`, `http.server.BaseHTTPRequestHandler` and
  `http.server.SimpleHTTPRequestHandler` with `do_`, and `unittest.TestCase` with `test`.
- The shell hosts are exact names: bash's `command_not_found_handle`, and zsh's `precmd`, `preexec`,
  `chpwd`, `periodic`, `zshaddhistory` and `zshexit`. The shims are `mktemp`, `date`, `sleep`, `uname`
  and `git`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `load_pack`, `render_pack`, `resolve_interpreter` | functions, `pack.py` and `gen_pack.py` | `py.function`, asked: OK |
| `extract_stdlib_rows`, `extract_wheel_rows`, `extract_hookspec_rows`, `extract_dts_rows` | functions, `gen_pack.py` | `py.function`, asked: OK |
| `read_row` | method of `Pack` | `py.function`, asked: OK |
| `Pack`, `PackError` | classes, `pack.py` | `py.type`, asked: OK |
| `inspect`, `wheel`, `hookspec`, `dts`, `check` | modes of `gen_pack.py` | none |
| `pack.py`, `gen_pack.py` | file stems | `py.file`, undeclared at base; TOOL-dMindYourWords-15 re-arms it |

### Rollout

The packs are inert data until TOOL-dMindYourWords-2 reads them, so landing this unit changes no
verdict and no pin. The forced check that reads them is TOOL-dMindYourWords-2's, built after this unit.

### Files touched (estimate)

- `tools/lexicon/pack.py` (new): S2, S3
- `tools/lexicon/gen_pack.py` (new): S4, S5
- `tools/lexicon/packs/python-3.12.toml`, `tools/lexicon/packs/python-3.14.toml`,
  `tools/lexicon/packs/pytest.toml`, `tools/lexicon/packs/shell.toml` (new): S6
- `tools/lexicon/selftest.py`: the arms of §7
- `tools/lexicon/README.md`, `tools/lexicon/LEXICON.md`: S8
- `tools/lexicon/lexicon.py`: `KIT_LEXICON_VERSION` only

### Alternatives rejected

- **The packs in the conf's own line grammar, parsed by `_parse_rows`** (`lexicon_conf.py:187`). That
  avoids `tomllib`, but a pack is a typed header plus four row kinds, and the line grammar has one row
  kind per block. It also differs from I6's spelling, which six writers share. The `tomllib` floor
  costs nothing the policy read has not already spent (Evidence).
- **One pack per stdlib module** (`logging.toml`, `json.toml` …). The test: a member or prefix row
  applies only where a site's base resolves through its imports. So a stdlib row that is selected but
  never imported forces nothing, and per-module files only multiply generator commands and fixtures.
  Rejected. The census still selects `pytest.toml` and `shell.toml` on its own (TOOL-dMindYourWords-8).
- **One file across the minors, `versions = ">=3.12,<3.15,!=3.13.*"`.** It loses
  the per-minor rows that differ (Evidence), and its byte identity cannot be stated per interpreter.
- **bats hooks (`setup`, `teardown`) as `host` rows.** Refused by validation rule 8, because `setup` is
  a canon form. `.bats` is also not in `KNOWN_EXTS`, so no bats definition is ever extracted.
- **`socketserver` in the first wave.** The platform probe flags it (Evidence). Its two request
  handlers' members reach `http.server.BaseHTTPRequestHandler` through the MRO anyway.

## 5. Production-readiness checklist

- security — no grading path imports a host package. `inspect` runs the declared stdlib interpreter
  under `-I`, so no user-site package loads. `wheel`, `hookspec` and `dts` only parse. `load_pack`
  refuses a malformed custom pack whole, so a bad row cannot widen an exemption.
- perf / scale — four files, about 140 KB in total (PINNED estimate). `load_pack` is one `tomllib`
  parse per file per run.
- error / empty / loading states — every refusal names the file, the row and the rule. An empty array
  is legal. A pack with every array empty loads and forces nothing.
- observability — `gen_pack.py check` prints one line per pack with its kit, versions and row counts.
- risks — a wrong curated row exempts a free choice. Validation rule 8 refuses the bare generic class,
  and a row applies only on a resolved base. The minors shipped are those this node can run (§8 F2).
- testing — the arms of §7, each on a planted pack, wheel, `.d.ts` or interpreter pair.
- migration — N/A: new files, nothing read yet.
- user docs — `tools/lexicon/README.md` `## Packs` and its `LEXICON.md` pointer. `help/` holds no
  lexicon page.

## 6. Acceptance criteria

- **AC1** — When `python gen_pack.py check` runs over the four first-wave files, it exits 0 and prints
  one line per file naming its `kit`, `versions` and the count of each array.
  Red when: a shipped pack breaks a rule of §4 "Validation", or a file is missing.
- **AC2** — When `load_pack` runs over nine planted packs, each breaking one rule of §4 "Validation"
  (an unknown array `mebmer`, no `kit`, a `member` row without `name`, a repeated row, `versions =
  ">=three"`, `langs = ["rb"]`, a `host` namespace of `*`, a `host` row `namespace = "setup"`, `name =
  "setup"`, a `prefix` with empty `prefix`), each raises `PackError` naming the file and the row's
  `<array> #<k>`, and returns no rows. `python gen_pack.py check` on each exits 1 printing that line.
  With the break removed, each loads.
  Red when: any planted pack loads, or a refusal omits the row.
- **AC3** — When `Pack.read_row` runs over the planted site table of each first-wave pack, it returns
  a row for each forced site and `None` for its free twin. For `python-3.12.toml`: `("logging.Handler",
  "emit")` gives `member`, `("ast.NodeVisitor", "visit_Call")` gives `prefix`, `(None, "__str__")`
  gives `host`, and `(None, "emit")`, a module function of the same name, gives `None`. For
  `pytest.toml`: `pytest_configure` gives `host`, and `pytest_configur` matches the namespace but not
  the set and gives `None`. For `shell.toml`: `precmd` gives `host`, `mktemp` with `invokes={"mktemp"}`
  gives `shim`, and `mktemp` with no invocation gives `None`.
  Red when: a free twin is forced, or a forced site is not.
  fixture: the site table is planted in the arm. The source-level twin is TOOL-dMindYourWords-2's.
- **AC4** — When the committed `generator` command of `python-3.12.toml` runs once under `py -3.12` and
  once under `py -3.14`, writing to two scratch files, the two outputs and the committed file are
  byte-identical. The same holds for `python-3.14.toml`.
  Red when: the generator introspects the running interpreter, so that the 3.14 driver writes
  `assertEndsWith` into the 3.12 pack.
  permission: needs both interpreters, which this node holds (PINNED 2026-10-29).
- **AC5** — When `python gen_pack.py inspect --python 3.14 --kit python --module socketserver` runs, it
  exits 1 naming `socketserver` and `ForkingMixIn`. With `--platform win_amd64` it writes
  `python-3.14-win_amd64.toml` to the scratch output directory.
  Red when: a platform-guarded module is accepted untagged, which is the probe's planted positive.
- **AC6** — When `python gen_pack.py hookspec` runs over pytest 9.1.0's distribution directory under
  `py -3.14`, an interpreter where pytest does not import, it writes bytes identical to `pytest.toml`
  with 52 `host` rows. Over a planted wheel whose hookspec module holds `pytest_alpha`, a decorated
  `pytest_beta` and a helper `build_spec`, it writes exactly two rows.
  Red when: the helper becomes a row, or the run imports pytest.
  figure: 52 is PINNED for pytest 9.1.0; the planted wheel's 2 is DERIVED.
- **AC7** — When `python gen_pack.py wheel` runs over a planted wheel whose module `views.py`, in package `pkg`, defines `View`
  with `get` and `_render`, and `Sub(View)` with `post`, given `--base pkg.views.Sub`, it writes
  `member` rows `get`, `_render` and `post` on base `pkg.views.Sub`, and `versions` from the planted
  `METADATA`.
  Red when: a method of an undeclared class appears, or the run imports `pkg`.
- **AC8** — When `python gen_pack.py dts` runs over a planted package holding `export declare class
  Component<P> { render(): Node; setState(s: P): void; readonly props: P }` and `interface Props {
  onClick?(): void }`, it writes `member` rows `render`, `setState` and `onClick`, and no row for
  `props`.
  Red when: a property or a type token becomes a row.
- **AC9** — When `python gen_pack.py inspect --python 3.12 … --prefix nosuch.Base=do_` runs, it exits
  1 naming `nosuch.Base`.
  Red when: a curated prefix row is written on a base the interpreter does not define.
- **AC10** — When `git ls-files` lists the kit's pack directory, it prints exactly the four first-wave files,
  and `shell.toml`'s header reads `generator = "curated"`.
  Red when: a second-wave pack ships, or the curated pack claims a generator.
- **AC11** — When `grep -n "## Packs" tools/lexicon/README.md` runs, it prints the section heading,
  and the section names `load_pack`, the four modes and `check`.
  Red when: the section is missing, or a mode is unnamed.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `lexicon naming predicates` · `lexicon wiring` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lexicon/selftest.py · covers AC2 AC3 AC5 AC6 AC7 AC8 AC9 · the planted packs, site tables, wheels, `.d.ts` package and the `socketserver` probe, its failing case a planted pack with a bare generic `host` row that loads · none

New arm: tools/lexicon/selftest.py · covers AC4 · the two-interpreter byte-identity run, its failing case a generator patched to introspect its own interpreter; with one interpreter absent it prints `not graded` and checks nothing · none

## 8. Open questions

- **F1 — Do first-wave packs declare verb families?** Options: (a) `families = {}` in every
  first-wave pack; (b) curate a family per host kit. No generator can derive a family. LX-1 has
  families declared and never inferred, and the owner declares them through `instructions.edit` (v2's
  clause `cl-dClosedLoop-0271`). A curated family in a shipped pack is gov choosing an adopter's
  vocabulary. RESOLVED (agent, 2026-10-29, delegated): (a), rung 1: the clause for
  TOOL-dMindYourWords-10 has families "declared by the packs the stack census selects … and by the
  owner", and a pack declares only what its host kit dictates, which for the first wave is none.
  widens: none · relaxes: none
- **F2 — Which Python minors ship?** Options: (a) the minors whose interpreter this node can run, 3.12
  and 3.14; (b) every minor from 3.11 to 3.14. (b) needs interpreters installed on the node, a new
  install location (veto 2). RESOLVED (agent, 2026-10-29, delegated): (a), rung 3. A version between
  or outside the shipped minors takes the nearest range below and reports the gap
  (TOOL-dMindYourWords-8). Adding a minor is one generator run on a node that holds it. widens: none ·
  relaxes: none
- **FACT-QUESTION · F3 — Does any first-wave module's member set differ by platform?** Probe: the
  `ast` walk of §4 "The generators" over each declared module's source. It decides by whether any
  module guards a class or a method on a platform test. Liveness: `socketserver` is a known positive
  (`hasattr(os, 'fork')` at :556), so the probe can return a hit. RESOLVED (agent, 2026-10-29,
  delegated): no first-wave module is flagged; `socketserver`, flagged, is left out; no per-platform
  pack ships; the generator keeps the probe as a refusal (AC5). widens: none · relaxes: none
- **F4 — Do `wheel` and `dts` ship before any pack uses them?** Options: (a) ship all four generators,
  each proven on a planted input; (b) ship `inspect` and `hookspec` only, and the other two with the
  second wave. The clause names the four generators as how packs are generated, and v2:2000 defers only
  the second-wave packs. RESOLVED (agent, 2026-10-29, delegated): (a), rung 1, the clause's text.
  `hookspec` already reads through `wheel`'s archive reader. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Items 7, v2:2000, the lexicon review's
  `[packs]` :288-326 and `[forced]` items 1 and 5, debt-fold rows :623 and :634-638, scout B row 7 and
  interfaces 1 and 2, and the spec brief's I6.

## 10. Reuse audit

No existing seam fits the pack store, its loader or its generators. `python
tools/codebase-map/reuse_lookup.py "load and validate a generated data file of forced names per host
library, refusing a malformed file whole"` ranked only name-stem hits: `load_conf` in six kits,
`load_toml` (`tools/govkit/govkit.py`) and `load_workflows`. None reads a forced-name row. Scout B's
row 7 holds against source at `ba8b3c8c4`. The seams the unit wires through are these:
- `canon.build_form_index` and `canon.CLUSTERS` (`tools/lexicon/canon.py:52-132`), which validation
  rule 8 calls rather than keeping a second generic-word list;
- `subtokens.subtokens` (`tools/lexicon/subtokens.py:33`);
- `scan_ts_tokens` (`tools/lexicon/lexicon.py:950`), which `dts` reads through;
- the `generator=` spelling of `[[generated]]` rows (`tools/codebase-map/kit.toml:148-154`), borrowed
  as a header key only;
- the run-each-candidate rule of `tools/lib/resolve-python.sh`, followed by `resolve_interpreter` for
  one named minor. That script resolves any python3 and cannot be asked for a minor.

One disagreement: scout B proposed rows as `[[host]] namespace, pattern`. §4 keeps `namespace` and
names the second key `name`, and adds `langs` (Data model).

Recall terms used: `python tools/memory-recall/query.py "how are host-forced names packed per library version and generated without a live import" --terms "packs forced names inspect wheel hookspecs pluggy generator header versions stdlib minor byte-identical"`
