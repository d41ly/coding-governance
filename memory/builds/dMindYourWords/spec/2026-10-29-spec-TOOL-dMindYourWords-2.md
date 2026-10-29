# TOOL-dMindYourWords-2 — forced names recognised by what forces them, under `lexicon.forced`

**Status:** DEFERRED · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 8 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0263@bab0ffd1 whole
**Carries:** node:policy-key.lexicon.forced

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-1 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-12 TOOL-dMindYourWords-11 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-9 TOOL-dMindYourWords-16 TOOL-dMindYourWords-13 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

Today every extracted definition is graded by its leading subtoken alone. So `emit` on a
`logging.Handler`, four pytest hooks, `__str__` and a `mktemp` shim count as debt, and the only exits
are a pin raise or a corpus-wide text waiver (gap-lex-01). This unit grades a name as forced only by
what forces it. Pack `member` and `prefix` rows apply where the enclosing class resolves statically,
through its imports, to that base. A namespaced closed set applies by name through its namespace
pattern (`pytest_*`, `__*__`). An override of a class defined in the repository is forced by that
parent. Everything runs against committed pack data, never a live import. The policy key
`lexicon.forced` chooses among `verified`, `by-name` and `by-annotation`.

## 2. Scope (IN)

- **S1** — The forced check in `measure_pass`'s P1 loop (`tools/lexicon/lexicon.py:2941-2965`), run on
  each definition the verb test would grade an offender, before the debt and unruled split. A forced
  definition becomes an `Offender` with `grade` `forced` (I1, TOOL-dMindYourWords-1) and a new field
  `source` (I2), and never counts against the pin. Every other definition keeps today's path. A
  conforming name stays conforming: the check never runs on it. Observed by AC1, AC2.
- **S2** — Base resolution for a Python site, `resolve_forced_source(site, context, packs, classes)`,
  over TOOL-dMindYourWords-12's definition context (I5), read once per run by
  `read_definition_context(root, "worktree", conf)` over `extract_ranges` with `context=True`: the
  enclosing class, its bases as dotted names resolved through the module's imports (`unresolved` where
  they do not resolve), and its decorators with aliases resolved. It walks the bases left to right, depth first, at most 8 deep, with a cycle guard (§4 "The
  walk"). The first base that forces the name decides it. Observed by AC1, AC3, AC4.
- **S3** — The repository class index, `build_class_index(contexts)`. It maps each class the scanned
  corpus defines to its path, the member names it defines and its resolved bases. Its dotted name is
  derived from the repo path by module-path suffix (§4 "The class index"), and an ambiguous suffix
  resolves to nothing. An override of a class in that index is forced by it, source
  `parent:<path>::<Class>`. When that parent's member is renamed, the override is graded again.
  Observed by AC4.
- **S4** — The shell sites. A `host` row of a pack whose `langs` holds `sh` forces a shell function by
  name. A `shim` row forces a shell function whose name is a word `scan_shell_tokens`
  (`lexicon.py:469`) yields elsewhere in the same file, which is what "a command it also invokes" reads
  as here (§4 "Shell"). Observed by AC5.
- **S5** — The three cases with their own outcome, each with its fixture:
  - an unresolved base grades as debt and prints `lexicon: forced unresolved — <site> (base <expr>)`;
  - an override of a repository parent is forced by that parent (S3);
  - a marker on a base defined in the repository, or on an unpacked base, prints `lexicon: forced
    marker reported — <site> (base <dotted>, repository|unpacked)` and moves no exit code.
  Observed by AC3, AC4, AC6.
- **S6** — `lexicon.forced`, read once per run by the literal call `read_policy_value("lexicon.forced",
  root)` (I7, TOOL-dMindYourWords-1). Each value routes as the table in §4 "The values" says. Under
  `by-name` the run prints the measured false-exemption rate on the tally. A value outside the three is
  a problem line naming it, and the run reds. Observed by AC7, AC8, AC9.
- **S7** — The tally, one line after the P1 line in `check_pass` (`lexicon.py:3390`), on green and on
  red: `lexicon: forced=<n> (pack=<a>, parent=<b>, contract=<c>, suppressed=<d>)` (I2). `contract`
  reads 0 until TOOL-dMindYourWords-3 lands. Observed by AC1, AC10.
- **S8** — The packs a run applies: every `tools/lexicon/packs/*.toml` (the kit's `packs/` directory)
  through `load_pack` (I6, TOOL-dMindYourWords-7), each applied only to sites whose extension its
  `langs` names. Both Python minors load, so their rows apply as a union. A pack `load_pack` refuses is
  a problem line naming it, never a skip. Observed by AC1, AC11.
- **S9** — The catalogue row `lexicon.forced` (`tools/policy/catalogue.toml:394`) gains `summary` and
  `usage`, and `python tools/policy/policy.py lists --write` drains the name from
  `tools/policy/unsummarised-keys.txt:105`. Its allowed values and default stay as written. The
  literal call of S6 is the reader the policy kit's reader-coverage arm counts
  (`tools/policy/check_policy.py:518`, `READER_SHAPES` at :423). Observed by AC12.
- **S10** — The docs. A `### Forced names` section of `tools/lexicon/README.md` gives the walk, the
  three cases, the values and the tally. `help/policy.md`'s key table gains the `lexicon.forced` row.
  `KIT_LEXICON_VERSION` (`lexicon.py:90`) moves. Observed by AC13.

## 3. Non-goals (OUT)

- The pack files, their grammar, `load_pack` and `Pack.read_row`: TOOL-dMindYourWords-7's. This unit
  calls them and adds no second row matcher.
- Which packs are selected: TOOL-dMindYourWords-8 narrows S8's "every pack" by census, manifests and
  `PACKS:` under `lexicon.packs`, and reports a kit no pack covers as uncovered. Until it lands, every
  shipped pack applies, which for the Python minors is the review's union fallback.
- Marker verification and the red for a marker with no defining base: TOOL-dMindYourWords-4's. This
  unit only reports the two marker cases its clause names.
- The contract table: TOOL-dMindYourWords-3's, which adds the `contract:` source to S1's check.
- The reasoned site suppression, its key and its reason: TOOL-dMindYourWords-5's `load_waivers`, whose
  hits this unit counts as `suppressed:` and routes under each value.
- The pin, the classes and the offender key set: TOOL-dMindYourWords-1's. Its counting reads
  `grade == debt`, so a forced name leaves the pin and `--offenders` by construction.
- JavaScript and TypeScript `member` and `prefix` rows: the extraction primitive yields no class
  membership there until its second wave (lexicon review `[forced]` item 1, :255-258). A JS or TS site
  takes only the `contract` and `suppressed` sources.
- Forced type names. A pack row names a member, and `class XHandler(logging.Handler)` chose its name,
  so P2's suffix grading is unchanged.
- A live import of any module at grading time (lexicon review :275-277).

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `Offender.grade`, the class field a forced definition is recorded with, and the pin that counts `debt` only; without it a forced name has no class to take
- **consumes-from** `TOOL-dMindYourWords-1` — `read_policy_value`, the I7 helper S6 calls with the literal key `lexicon.forced`
- **consumes-from** `TOOL-dMindYourWords-12` — `extract_ranges` with `context=True`, read through `read_definition_context` (I5): enclosing class, bases resolved through imports, decorators with aliases resolved; without it no base resolves and S2 to S5 cannot run
- **consumes-from** `TOOL-dMindYourWords-5` — `load_waivers` and its `(rows, problems)` shape, the reasoned site suppressions S1 counts as `suppressed:` and `by-annotation` applies alone
- **consumes-from** `TOOL-dMindYourWords-7` — `load_pack` and `Pack.read_row`, the packs S8 loads and the one row matcher S2 and S4 ask
- **consumes-from** external — TOOL-dTotalRecall-13 and TOOL-dTotalRecall-8, the extraction primitive unit 12 extends, each DEFERRED at base and built before this build run
- **hands-off** `TOOL-dMindYourWords-3` — `Offender.source`, whose `contract:<row tag>` value that unit's table supplies to S1's check
- **hands-off** `TOOL-dMindYourWords-4` — `Offender.source`, S5's marker report, and the walk and class index of S2 and S3 (`resolve_forced_source`, `build_class_index`), which that unit's marker verification walks instead of building a second
- **hands-off** `TOOL-dMindYourWords-6` — `Offender.source`, the forced answer `--suggest` prints with its base
- **hands-off** `TOOL-dMindYourWords-8` — `Offender.source` and S8's pack set, which that unit's selection narrows so a `pack:<kit>:<row>` source names only a selected pack
- **hands-off** `TOOL-dMindYourWords-10` — `Offender.source`, the forced check that unit asks of every candidate so a forced name never establishes a verb
- **hands-off** `TOOL-dMindYourWords-29` — its pin falls, which the minors batch keeps in the ledger home (review id 6)

## 4. Design

### Evidence

Read at `ba8b3c8c4`. No product file differs from base `ccd1292e`.

- The P1 loop grades `leading_verb(name)` against VERBS and splits an offender `debt` or `unruled`
  (`lexicon.py:2941-2965`). `Offender.__slots__` is `kind, path, line, text, detail, verb, cls`
  (`:250`).
- `_python_defs` walks with `ast.walk` (`:433`) and records no enclosing class or base. Each
  extractor collects imports as its third element (`:438-455`).
- `extract_decorators` (`:2527-2573`) keys decorators by `(path, lineno, name)`. It records a dotted
  decorator by its last segment, so `@typing.override` reads as `override`, and an alias such as
  `from typing import override as ov` reads as `ov`. I5 resolves that alias.
- `leading_verb` strips leading underscores (`subtokens.py:39-48`), so `__str__` grades on `str`
  today.
- Measured off `python tools/lexicon/lexicon.py --offenders` at `ba8b3c8c4`, PINNED: 1218 keys. They
  include `pytest_configure`, `pytest_runtest_logstart`, `pytest_runtest_logfinish` and
  `pytest_sessionfinish` in `tools/pytest-parallel-guardrails/crashprobe.py`, `__str__` in
  `tools/lexicon/lexicon.py` and `tools/policy/policy.py`, and `mktemp` in
  `tools/unattended/unattended.test.sh`. `emit` in `tools/govkit/govkit.py:1641` sits on `class
  Report` with no outside base, and `emit` in `tools/memory-recall/query.py:968` is a module function.
  Both stay debt.
- `scan_shell_tokens` returns `[(kind, text, line)]` with `kind` `word` or `op`, and treats `$(…)` as
  code (`lexicon.py:469-475`). So the `mktemp` inside `TMP=$(mktemp -d)`
  (`tools/unattended/unattended.test.sh:130`) is a word.
- `policy.py get` reads the landed revision, refusing with exit 2 (`tools/policy/policy.py:1332-1360`),
  so a planted policy file is committed in its fixture repository.

### The walk

For a Python function `name` defined in class `C` of file `p`:

1. Every applicable pack's `host` rows are asked first with `Pack.read_row(None, name)`, because a
   namespaced closed set applies by name wherever the definition sits. A hit gives
   `pack:<kit>:host#<k>`.
2. Then each base `b` of `C`, left to right:
   - `b` is `unresolved`, I5's answer for an expression it cannot resolve to a dotted name
     (TOOL-dMindYourWords-12 §4): it is remembered, and the walk goes on to the next base;
   - `b` is in the class index: if that class defines `name`, the source is `parent:<path>::<Class>`;
     otherwise its own bases are walked, one level deeper;
   - `b` is any other dotted name: each applicable pack is asked `read_row(b, name)`, and a `member`
     or `prefix` hit gives `pack:<kit>:<array>#<k>`.
3. No source found: the definition is graded as today. When step 2 met an unresolved base, the run
   prints S5's unresolved line for it.

A module function (`C` absent) gets step 1 only. A depth past 8, or a class met twice, stops that
branch as unresolved.

### The class index

Each scanned `py` file's module path is its repo path with `.py` removed, `/__init__` dropped, and `/`
read as `.`. A dotted base `a.b.C` names repo class `C` when exactly one scanned module path ends with
the segments `a.b` and defines `C`. A bare name defined in the same module resolves to that module's
class. Two or more matches make the base resolve to nothing, which is case 1 when no other base forces
the name. This tree imports sibling modules by bare name after a `sys.path` insert, so suffix matching
is what resolves `from lexicon_conf import ConfError` to `tools/lexicon/lexicon_conf.py`.

### Shell

For a shell function `name` in file `p`: each applicable pack's `host` rows are asked by name, then
`read_row(None, name, invokes=W)`, where `W` is every `word` token `scan_shell_tokens` yields for `p`
on a line other than the definition's. One limit is stated rather than closed: an `unset -f mktemp`
line names `mktemp` as a word, and counts as an invocation.

### The values

| `lexicon.forced` | `host` and `shim` rows | `member` and `prefix` rows | repository parent | `contract` and `suppressed` |
|---|---|---|---|---|
| `verified` (default) | by name and the shim rule | where a base resolves to the row's base | yes | yes |
| `by-name` | by name and the shim rule | by name alone, wherever the name is defined | no | yes |
| `by-annotation` | no | no | no | yes |

Under `by-name`, a `member` row forces its `name` everywhere, and a `prefix` row forces every name
that starts with its prefix. The run also resolves as `verified` does, for the count alone, and the
tally line gains ` · by-name exempted=<E>, verified forces <V> of them, false-exemption rate
<E-V>/<E>`. The review measured 53 sites for 1 forced on this tree (lexicon review :280-281); the
figure printed is derived each run. `by-annotation` is item 4's route: only a reasoned site
suppression or a contract row exempts.

### The three cases

- **Unresolved.** `class H(make_base()):` with `def emit(self)`: `emit` is debt, and the run prints
  `lexicon: forced unresolved — h.py::H.emit (base make_base())`.
- **Repository parent.** `base.py` defines `class Base` with `def emit(self)`, and `child.py` defines
  `class Child(Base)` with `def emit(self)`. `Child.emit` is forced, source `parent:base.py::Base`.
  `Base.emit` is graded as today, because the parent carries the one debt. Rename `Base.emit` to
  `Base.print_record` and `Child.emit` is graded debt.
- **Marker reported.** A method decorated with `override`, resolved through I5 from `typing` or
  `typing_extensions`, whose class's bases are all repository classes or all outside bases no
  applicable pack names. It prints the marker line and changes no exit code. Its name takes whatever S2
  gives it. Confirming a marker against a pack, and the red when no base defines the member, are
  TOOL-dMindYourWords-4's.

### Data model

`Offender` gains one slot, `source`, default `None` (`lexicon.py:250-254`). It is set only when
`grade` is `forced`, to one of `pack:<kit>:<array>#<k>`, `parent:<path>::<Class>`, `contract:<row tag>`
or `suppressed:<path>::<name>` (I2, I3). The `(name, lineno)` pairs `extract` returns are untouched,
because `drift_report.py` unpacks them by position (`lexicon.py:2532-2540`).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `resolve_forced_source` | function, `lexicon.py` | `py.function`, asked: OK |
| `build_class_index` | function, `lexicon.py` | `py.function`, asked: OK |
| `measure_false_exemptions` | function, `lexicon.py` | `py.function`, asked: OK |
| `Offender.source` | slot | none |
| `forced unresolved`, `forced marker reported` | report lines | none |

### Rollout

Live at landing under the default `verified`. On this tree the first wave forces the four pytest
hooks, both `__str__` and the `mktemp` shim, and TOOL-dMindYourWords-1's pin falls by that count in
the landing commit. That figure is derived by the landing run, never typed here.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1 to S8, `KIT_LEXICON_VERSION`
- `tools/lexicon/selftest.py`: the arms of §7
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`: S9
- `tools/lexicon/README.md`, `help/policy.md`: S10
- `.lexicon.conf`: the pin's fall at landing, in TOOL-dMindYourWords-1's form

### Alternatives rejected

- **A new sibling module `tools/lexicon/forced.py`** (scout A row 2). The walk reads `measure_pass`'s
  scanned list, `Offender` and the decorators. The test is what a sibling import would add: one
  `import lexicon` from `forced.py`, which is a cycle with lexicon importing it. Kept in `lexicon.py`.
- **A live import to resolve a base**, as the research prototype did (research-lexicon-instruments
  :264-327). Rejected by the review's item 5, and by measurement: pytest imports under 3.12 here and
  not under 3.14, so two interpreters on one node grade differently.
- **The forced check on every definition, conforming ones included.** It would count a declared-verb
  override such as `threading.Thread.run` as forced and move it off the conforming count, which no
  reader asked for. The tally then measures exemptions granted, the figure gap-lex-01 is about.

## 5. Production-readiness checklist

- security — no grading path imports or executes repository or host code. Resolution reads syntax
  trees and committed packs. A refused pack reds the run rather than applying fewer rows.
- perf / scale — one class index per run, and one dictionary lookup per base per pack. The I5 context
  is TOOL-dMindYourWords-12's cost. A walk is bounded at depth 8.
- error / empty / loading states — no pack directory, or an empty one, applies no rows and prints
  `forced=0`. A refused pack, or an unknown policy value, reds with its name.
- observability — S7's tally on every run, the unresolved and marker lines, and under `by-name` the
  false-exemption rate.
- risks — a suffix match can tie two modules, so the base resolves to nothing and the name stays debt:
  a false debt, never a false exemption. `by-name` exempts free choices by design, and prints the cost.
- testing — the arms of §7, each in a fixture repository with the policy kit, a committed
  `.governance/policy.toml` where a value is planted, and the first-wave packs.
- migration — the pin falls once, at landing (Rollout). No data file changes shape.
- user docs — `tools/lexicon/README.md` `### Forced names`, and `help/policy.md`'s key row.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py` runs in a fixture repository holding `class
  H(logging.Handler)` with `def emit`, `class V(ast.NodeVisitor)` with `def visit_Call`, a `def
  __str__`, a module function `def emit` and a module function `def pytest_configure`, the tally prints
  `forced=4 (pack=4, parent=0, contract=0, suppressed=0)`, and the module function `emit` is the only
  one of the five in `--offenders`.
  Red when: the free `emit` is forced, or any of the four forced sites is graded debt.
- **AC2** — When the same fixture's `def __frobnicate__` is graded, it is in `--offenders` on verb
  `frobnicate`. `__str__`'s offender entry is absent and its source reads `pack:python:host#<k>`.
  Red when: a dunder outside the data-model set is forced.
- **AC3** — When `lexicon.py` runs over a fixture holding `class H(make_base())` with `def emit`, it
  prints `forced unresolved` naming `H.emit` and `make_base()`, and `emit` is in `--offenders`.
  Red when: the unresolved site is exempted, or no line is printed.
- **AC4** — When `lexicon.py` runs over the fixture pair `base.py` (`class Base`, `def emit`) and
  `child.py` (`from base import Base`, `class Child(Base)`, `def emit`), `Child.emit` is forced with
  source `parent:base.py::Base` and `Base.emit` is in `--offenders`. After `Base.emit` is renamed
  `print_record` in the fixture, `Child.emit` is in `--offenders`.
  Red when: the override is debt while its parent defines it, or stays forced after the rename.
- **AC5** — When `lexicon.py` runs over a shell fixture defining `mktemp()` in a file that also runs
  `$(mktemp -d)`, and `precmd()`, both are forced. A second file defining `mktemp()` and never
  otherwise naming it grades `mktemp` debt.
  Red when: the shim forces a function its file never invokes.
- **AC6** — When `lexicon.py` runs over a fixture whose `class C(Base)`, `Base` a repository class
  defining `emit`, carries `@ov def emit` after `from typing import override as ov`, and whose `class
  D(View)`, `View` imported from an unpacked module, carries `@override def get`, it prints two
  `forced marker reported` lines, ending `repository` and `unpacked`, and its exit code equals the same
  run with both decorators removed.
  Red when: a marker on either base turns the run red, or a line is missing.
- **AC7** — When the fixture of AC1 commits `.governance/policy.toml` setting `lexicon.forced =
  "by-name"`, the module function `emit` is also forced and the tally prints `false-exemption rate
  1/5`.
  Red when: `by-name` resolves bases, or prints no rate.
  figure: DERIVED by the run over the fixture; 53 for 1 is the review's PINNED reading of this tree.
- **AC8** — When the committed policy file sets `by-annotation`, the four pack sites of AC1 are in
  `--offenders`, and a site carrying a reasoned suppression (TOOL-dMindYourWords-5's row) is forced
  with source `suppressed:<path>::<name>`.
  Red when: a pack row applies under `by-annotation`.
- **AC9** — When the committed policy file sets `verified`, the output equals the run with no policy
  file. With `forced-ish`, the run exits non-zero naming the value.
  Red when: the default differs from `verified`, or an unknown value is graded as one.
  fixture: the policy file is committed, because `policy.py get` reads the landed revision.
- **AC10** — When `python tools/lexicon/lexicon.py` runs on this tree after the unit lands, the tally
  line follows the P1 line and its `pack=` is at least 7, the four pytest hooks, two `__str__` and
  `mktemp`.
  Red when: the line is absent on a green run, or a first-wave site of §4 Evidence stays debt.
  figure: 7 is PINNED at `ba8b3c8c4`; later trees may add forced sites.
- **AC11** — When a fixture's pack directory holds a pack with a bare generic `host` row, `lexicon.py`
  exits non-zero naming the pack and the row.
  Red when: the refused pack is skipped and the run is green.
- **AC12** — When `python tools/policy/policy.py lists --write` has run, `grep -c lexicon.forced
  tools/policy/unsummarised-keys.txt` prints 0, and `git grep -c 'read_policy_value("lexicon.forced"'
  -- tools/lexicon/lexicon.py` prints at least 1.
  Red when: the row lacks `summary` or `usage`, or no literal reader exists.
- **AC13** — When `grep -n "lexicon.forced" help/policy.md tools/lexicon/README.md` runs, it prints
  the key's row in the help page and the README's `### Forced names` section naming the three values.
  Red when: a value is unnamed in either page.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `lexicon naming predicates` · `straggler-guard arms` · `govkit acceptance matrix` · `lexicon wiring` · `policy fixtures` · `policy check` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC11 · one fixture repository per case with the first-wave packs and the policy kit, a committed policy file for each value, its failing case a free module function `emit` forced under `verified` · none

## 8. Open questions

- **F1 — Does a conforming name enter the forced check?** Options: (a) only a name the verb test would
  grade an offender; (b) every definition. RESOLVED (agent, 2026-10-29, delegated): (a), rung 1: the
  clause has the forced class keep names out of debt, and the lexicon review's class table gives each
  definition exactly one class with conforming first (lexicon review :212-218). widens: none ·
  relaxes: none
- **F2 — Which packs apply before TOOL-dMindYourWords-8 selects?** Options: (a) every shipped pack,
  filtered by `langs`; (b) none until selection lands. (b) ships a forced check that forces nothing,
  and every seen-red case of the clause would wait on another unit. RESOLVED (agent, 2026-10-29,
  delegated): (a), rung 3. The Python minors' union is the review's own fallback when no version is
  declared (lexicon review :291-293). widens: none · relaxes: none
- **F3 — Where do `contract` and `suppressed` sources apply across the three values?** Options: (a)
  under every value; (b) `contract` under `verified` and `by-name` only. A contract row and a reasoned
  suppression each carry their own reason, so neither is the reasonless exemption L-1 ruled out.
  `by-annotation` is "item 4's site suppression" (lexicon review :281-282), and dropping gov's
  contract rows under it would make that value red on names gov's own readers force. RESOLVED (agent,
  2026-10-29, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — How does a shim learn "a command it also invokes"?** Options: (a) any `word` token of the
  same file on another line; (b) a command-position parse. (b) needs a shell grammar this kit does not
  have, and `scan_shell_tokens` emits no position. RESOLVED (agent, 2026-10-29, delegated): (a), rung
  3, with §4 "Shell"'s limit stated. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Items 2, v2:1203, the lexicon review's
  `[forced]` :236-286 and `[classes]` :210-234, debt-fold rows :627, :638, :653 and :663, scout A row 2
  and interfaces 1, 2, 5 and 7, and the spec brief's I1, I2, I5, I6 and I7.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (TOOL-dMindYourWords-29); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are `measure_pass`'s P1 loop (`tools/lexicon/lexicon.py:2941-2965`), `Offender`
(`:238-257`) and `check_pass`'s count lines (`:3378-3390`). The unit reads through
TOOL-dMindYourWords-12's `read_definition_context` over `extract_ranges`, TOOL-dMindYourWords-7's `load_pack` and
`Pack.read_row`, TOOL-dMindYourWords-5's `load_waivers` and TOOL-dMindYourWords-1's
`read_policy_value`. `scan_shell_tokens` (`:469`) supplies a shim's invocations. `python
tools/codebase-map/reuse_lookup.py "resolve a class's base through its module imports to decide
whether a method name is forced by that base"` ranked name-stem hits: `resolve`, `resolve_kit_dir`,
`resolve_prefix_token` and `resolve_compare_base`. None resolves a class base, so the walk and the
class index are new. Scout A's row 2 holds against source at `ba8b3c8c4`. Its proposed
`tools/lexicon/forced.py` is rejected in §4 "Alternatives rejected".

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon tell a host-forced name from debt" --terms "forced names base resolution imports override parent unresolved marker lexicon.forced verified by-name debt"`
