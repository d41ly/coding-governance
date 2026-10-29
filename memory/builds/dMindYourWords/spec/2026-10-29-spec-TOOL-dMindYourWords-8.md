# TOOL-dMindYourWords-8 — packs detected from the import census and manifests and declared by the owner

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 12 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0269@f2bbdcc2 whole
**Carries:** node:policy-key.lexicon.packs

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-7-reuse-scout-b.md](../build/2026-10-29-build-TOOL-dMindYourWords-7-reuse-scout-b.md) | research | TOOL-dMindYourWords-7 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

A forced-name pack must apply to a repository whose code uses that host kit, and to no other: applied
everywhere, `emit` is forced in a tree that never imports `logging`; applied nowhere, `__init__` is
debt. This unit selects the packs as `lexicon.packs` says: detected from an import census over the one
corpus walk and from the four manifest kinds, declared by the owner in a `PACKS:` block, custom packs
included, with every input no pack covers reported in a state of its own (L-5; lexicon review
`[packs]` "Selection").

## 2. Scope (IN)

- **S1** — The import census. `measure_import_census(scanned, context_imports, root)` in the new
  `tools/lexicon/stack_census.py` returns `{key: files}`, the number of armed files naming each key.
  A key is every dotted prefix of each non-relative import `scan_corpus` yields in `defs[2]`
  (`tools/lexicon/lexicon.py:2262-2321`), unioned with the targets of the per-module `imports`
  TOOL-dMindYourWords-12's `read_definition_context` gives the forced check in the same run, plus one
  implicit host per armed file: the language its `LANGS` row arms it under, the pattern-set id's
  first segment (`python` for `py:python-ast`, `shell` for `sh:shell-tokens`), which is how the
  language packs TOOL-dMindYourWords-7 ships, `kit = "python"` and `kit = "shell"`, are detected
  (§8 F1). A relative import (leading `.` or `/`) and a `node:` specifier are not keys. Observed by
  AC1.
- **S2** — The manifests. `read_manifest_versions(root, rels)` reads every tracked `pyproject.toml`
  (`[project]` `dependencies`, `optional-dependencies` and `requires-python`, through `tomllib`),
  `requirements.txt` (PEP 508 lines; `-r`, `-e`, URL and comment lines skipped), `package.json`
  (`dependencies`, `devDependencies`, `peerDependencies`, `optionalDependencies`) and `composer.json`
  (`require`, `require-dev`), and returns `{kit: [version facts]}`, each reduced by the table in §4
  "Version facts", names normalised by PEP 503. A manifest `check_out_of_scope` (TOOL-dMindYourWords-15)
  answers with a reason is not read. A manifest that does not parse is a refusal naming its path.
  Observed by AC2, AC10.
- **S3** — The declaration. A `PACKS:` block in `.lexicon.conf`, one `BLOCK_KEYS` row
  (`tools/lexicon/lexicon_conf.py:37`) and its parser `_parse_packs` in `_BLOCK_PARSERS` (`:401-402`),
  rows `<kit>  <source>  [<version>]`: `<source>` is `shipped` or a repository-relative path to a
  custom pack ending `.toml`, refused at its line when absolute or carrying a `..` segment;
  `<version>` is an exact version or a PEP 440 specifier set, refused at its line when malformed; the
  row `python  shipped  <version>` declares the Python version the `python` packs are keyed on.
  `--print-rows PACKS <conf>` prints each row as typed. Observed by AC7, AC11.
- **S4** — The range test. `check_version_in_range(version, versions)` compares a version's release
  segments, as an integer tuple with pre, post, dev and local segments dropped, against a parsed
  specifier set: a pack's `Pack.versions`, which `load_pack` parses (TOOL-dMindYourWords-7 §4 "Data
  model"), or a `PACKS:` or pip specifier parsed by that same parse, called and never copied. It also
  reads a set's floor and ceiling for S5. Observed by AC3, AC4, AC5.
  **Readers:** by name: READER NOT IN TREE — the segments are dropped inside this new comparison's
  own parse of one version string, and no tracked file compares a pack version before this build ·
  by value: NO VALUE READERS — nothing is stored without the dropped segments; the version string a
  manifest or a census carries is read whole by its own reader and left unchanged.
- **S5** — The selection. `resolve_packs(shipped, census, manifests, declared, value, root)` returns
  the applied packs, each with its kit and state, by the tables in §4 "What each value applies" and
  "The states". A shipped pack is detected when its header `kit` is a census key or a manifest name,
  or a member or prefix row's base names a census key as its module, and is applied only where one of
  its `langs` is armed. A custom pack is loaded through `load_pack`, so a malformed one is refused
  whole naming its row, and its header `kit` must equal its row's key. A `shipped` row naming a kit no
  shipped pack carries is a refusal. Every refusal joins `measure_pass`'s `problems`. Observed by AC1,
  AC3, AC4, AC5, AC6, AC7, AC8.
- **S6** — The wiring. `measure_pass` (`:2796`) calls S1, S2 and S5 once per run, after the corpus
  walk and before the forced check, which reads S5's applied set in place of every shipped pack, as do
  `check_override_marker` (TOOL-dMindYourWords-4) and the family map (TOOL-dMindYourWords-10).
  `check_pass` prints `render_pack_lines`' output on green and on red:
  `lexicon: packs lexicon.packs=<value> applied=<n> (<kit>, …) uncovered=<m> (<kit>, …)` and one line
  per state other than `applied` that holds a kit. Observed by AC1, AC3, AC4, AC5, AC8.
- **S7** — The policy read. `read_policy_value("lexicon.packs", root)` (I7), the literal the policy
  kit's reader-coverage arm counts, read once in `measure_pass` and once in `run_suggest`. The
  catalogue row (`tools/policy/catalogue.toml:411-415`) gains its `summary` and `usage`, and
  `python tools/policy/policy.py lists --write` drains `lexicon.packs` from
  `tools/policy/unsummarised-keys.txt` (`:106`); the allowed values and default stay as written.
  Observed by AC8, AC12.
- **S8** — `--suggest` reads the declared packs. `run_suggest`'s pack set (TOOL-dMindYourWords-6 S2)
  becomes S5's set computed with no census and no manifest, since both are corpus reads: every
  shipped pack under `detected-and-declared`, `detected` and `all`, the declared shipped kits under
  `declared`, and the `PACKS:` custom packs under every value but `detected`, each kit's packs taken
  as the union of their versions. Observed by AC9.
- **S9** — Docs and version. A "Pack selection" section in `tools/lexicon/README.md` and the `PACKS:`
  grammar in `tools/lexicon/LEXICON.md`; `help/policy.md`'s consumer paragraph names the lexicon as
  `lexicon.packs`' reader; `KIT_LEXICON_VERSION` (`lexicon.py:90`) moves. Observed by AC12.

## 3. Non-goals (OUT)

- The pack files, their grammar, `load_pack` and `gen_pack.py`: TOOL-dMindYourWords-7. The second-wave
  packs and the adopter census they wait on (v2:2000 `[owed]`).
- Applying a pack to a site: the forced check is TOOL-dMindYourWords-2's, the marker check
  TOOL-dMindYourWords-4's; this unit decides which packs they read.
- The verb families a selected pack declares: TOOL-dMindYourWords-10 reads them from S5's set.
- The write-path guard over `PACKS:` rows and custom pack files: TOOL-dMindYourWords-11's, under
  `record-kind.lexicon-declaration`, which that unit carries.
- The path selector itself: TOOL-dMindYourWords-15. Any live import, `pip`, `npm` or `composer` run:
  selection reads committed bytes only (lexicon review `[forced]` item 5).
- A list of Node's core modules. A bare `fs` reads as an uncovered kit, which the report states (§8 F3).

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `read_policy_value`, I7, through which S7 reads `lexicon.packs`
- **consumes-from** `TOOL-dMindYourWords-14` — `load_conf` with the repeated-header refusal, which must stand before S3 adds a block
- **consumes-from** `TOOL-dMindYourWords-15` — `check_out_of_scope`, through which S2 skips a manifest in a record or a planted fixture tree
- **consumes-from** `TOOL-dMindYourWords-12` — `extract_ranges` with `context=True`, whose per-module `imports`, read through `read_definition_context`, S1 unions into the census
- **consumes-from** `TOOL-dMindYourWords-7` — `load_pack`, through which S5 loads the shipped and custom packs and reads each header's `kit` and `langs`, and `Pack.versions`, the parsed specifier set S4 compares against
- **consumes-from** `TOOL-dMindYourWords-2` — `Offender.source`: the forced check whose pack set S6 narrows to the selection, so a `pack:<kit>:<row>` source names only a selected pack
- **consumes-from** `TOOL-dMindYourWords-4` — `check_override_marker`, whose `packs` argument S6 fills with the selection
- **consumes-from** `TOOL-dMindYourWords-6` — `run_suggest`, whose pack set S8 replaces
- **hands-off** `TOOL-dMindYourWords-10` — `resolve_packs`: the packs `lexicon.packs` selects, whose headers' families the family map reads
- **hands-off** `TOOL-dMindYourWords-9` — `resolve_packs`: the packs `lexicon.packs` selects, which the work order's vocabulary slot lists for a write set

## 4. Design

### Evidence

Read at `ba8b3c8c4`; no product file differs from base `ccd1292e`.

- `_python_defs` (`tools/lexicon/lexicon.py:425-456`) records each `Import` and `ImportFrom`, both
  `a.b` and `a.b.c` for `from a.b import c`, with relative dots kept; the `js-regex` set reads
  `import … from` and `require(…)` (`:149-150`); `parse_ts_defs` returns an empty import list by
  contract (`:1693-1736`, refusal 6), so a TypeScript file adds no census key until the extraction
  primitive's second wave, and TypeScript stacks are detected by `package.json`.
- `scan_corpus` (`:2262-2321`) yields `(rel, ext, defs, problem)` for every tracked file;
  `measure_pass` (`:2796-2821`) materialises it once.
- `BLOCK_KEYS` (`tools/lexicon/lexicon_conf.py:37`) and `_BLOCK_PARSERS` (`:401-402`) are the one door
  for a block; `_parse_rows` (`:187-201`) refuses a duplicate row key; `--print-rows` (`:501-546`)
  prints any block in `BLOCK_KEYS`, with a branch per value shape.
- No manifest reader exists in `tools/lexicon/` (scout B row 8), and no manifest is tracked in this
  repository: `git ls-files` matches none of the four names at `ba8b3c8c4`.
- `policy.py get` (`tools/policy/policy.py:1332-1360`) reads the landed revision; the
  `lexicon.packs` row (`catalogue.toml:411-415`) has no reader today.
- Measured by a read-only probe over `scan_corpus` at `ba8b3c8c4` (PINNED): 157 armed Python files,
  154 with imports; 34 armed JavaScript files, 11 with imports; third-party top-level names `pytest` (2
  files), `aiosqlite` (2), `numpy`, `sklearn`, `model2vec`, `harness` and `tests` (1 each), and five
  Node core names, `path`, `fs`, `child_process`, `crypto` and `os`.

### Version facts

| Source | Spelling | Fact |
|---|---|---|
| pip, `requires-python`, a `PACKS:` version | `==X` or `===X` without a wildcard | pinned X |
| npm, composer | `X` or `=X` | pinned X |
| pip, `requires-python`, a `PACKS:` version | `>=X`, `>X`, `~=X`, `==X.*` | floor X |
| npm, composer | `^X`, `~X`, `>=X`, `A - B`, alternatives joined by `\|\|` | floor at the lowest bound |
| any | empty, `*`, `latest`, a URL, a path, a tag, `workspace:` | unknown |

A kit's version source is, first to answer: its `PACKS:` row's version, then its manifest facts; for
the kit `python`, whose packs carry the data model and the stdlib bases one file per minor
(TOOL-dMindYourWords-7, "The first wave"), the manifest fact is `requires-python`. Two or more facts
for one kit read as one floor at the lowest. With no fact, the shipped `python-3.12.toml` and
`python-3.14.toml` are both taken, the `unknown` state.

### What each value applies

| `lexicon.packs` | detected shipped packs | `PACKS:` `shipped` rows | `PACKS:` custom rows | every other shipped pack |
|---|---|---|---|---|
| `detected-and-declared` (default) | applied | applied | applied | no |
| `detected` | applied | ignored, reported | ignored, reported | no |
| `declared` | not detected | applied | applied | no |
| `all` | applied | applied | applied | applied |

Under `declared` the census and manifests are not read for selection and the line says so; under
every other value they are, and the uncovered kits are reported.

### The states

| State | When | Packs taken | Line |
|---|---|---|---|
| `applied` | a pinned version inside one or more of the kit's ranges | those | on the tally line |
| `nearest-below` | a pinned version outside every range, some range below it | the pack with the highest floor below it | `took <range>, the nearest below <X>` |
| `below-every-range` | a pinned version below every range | none | `<X> is below every range; no pack applied` |
| `span` | a floor | every pack whose range is not wholly below the floor | `spans <spec>; took the union of <n>` |
| `unknown` | no version source | every pack of the kit | `version unknown; took the union of <n>` |
| `uncovered` | a detected kit, a top-level third-party name, with no pack | none | on the tally line; its forced names route to a reasoned site suppression (TOOL-dMindYourWords-5) |

A third-party name is a census key's first segment that is not in `sys.stdlib_module_names`, not a
tracked `.py` stem or tracked package directory of this repository, not an implicit language host,
and not a relative or `node:` specifier, or a manifest name. The stdlib test reads the running
interpreter's list and decides only who is named on the report line, never which pack applies. The four uncovered inputs the lexicon review lists (`[packs]` "Selection") are `uncovered`,
`nearest-below` with `below-every-range`, `unknown` and `span`.

### Inventory

Minted, each asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at base and
answered `OK`: `measure_import_census`, `read_manifest_versions`, `check_version_in_range`,
`resolve_packs`, `render_pack_lines` and `_parse_packs`; the file `stack_census.py`, graded by
`py.file` once TOOL-dMindYourWords-15 re-arms that cell; the block key `PACKS`.

### Files touched (estimate)

- `tools/lexicon/stack_census.py` — new: S1, S2, S4, S5
- `tools/lexicon/lexicon.py` — S6's calls in `measure_pass` and `check_pass`, S8 in `run_suggest`,
  `KIT_LEXICON_VERSION`
- `tools/lexicon/lexicon_conf.py` — `BLOCK_KEYS`, `_parse_packs`, `_BLOCK_PARSERS`, `--print-rows`
- `tools/lexicon/selftest.py` — the fixtures of §6
- `tools/lexicon/README.md`
- `tools/lexicon/LEXICON.md`
- `tools/policy/catalogue.toml` — S7's two fields
- `tools/policy/unsummarised-keys.txt` — drained by `lists --write`
- `help/policy.md` — S9

### Alternatives rejected

- **Packs as `[[generated]]` rows, re-run per landing.** Lost to scout B row 7: `regen.py` re-derives
  from the tree, and a pack is built from an outside interpreter or wheel.
- **A live `importlib` or `pip show` read for versions.** Lost to `[forced]` item 5: every node must
  grade the same, and on this node pytest imports under one interpreter and not the other.
- **Selection inside `scan_corpus`.** Its four-tuple shape is read by `measure_pass` (`:2821`) and
  `scaffold_lexicon.py:230`; the census reads its output instead of changing it.

## 5. Production-readiness checklist

- security — a custom pack path is validated at the conf line, repository-relative with no `..`; packs
  and manifests are parsed with `tomllib` and `json`, never imported or run; a malformed pack or
  manifest is refused, never skipped.
- perf / scale — the census rides the one corpus walk; manifests are the tracked files of four
  basenames, read once per run.
- error / empty / loading states — no import, no manifest and no `PACKS:` block applies only the
  implicit hosts' packs; each uncovered input prints its state; `declared` with no block applies none
  and says so.
- observability — the S6 lines on green and red.
- risks — a pack applied too widely exempts free names; detection is per repository, and the forced
  check still resolves each member row's base per site.
- testing — the fixtures of §6, each manifest kind, each state and each value a planted case.
- migration — none; an absent `PACKS:` block reads as empty.
- user docs — `tools/lexicon/README.md`, `tools/lexicon/LEXICON.md`, `help/policy.md`.

## 6. Acceptance criteria

- **AC1** — When `python lexicon.py --check` runs in a fixture repository with no manifest, whose `a.py`
  imports `alpha`, `jsalpha`, `numpy`, a sibling `b.py` and a relative module, which arms `py` and `sh`
  but not `js`, and which tracks `run.sh`, the packs line reads `lexicon.packs=detected-and-declared`,
  applies `alpha`, `python` and `shell`, applies none of `beta`, `gamma` and `jsalpha`, and reads
  `uncovered=1 (numpy)`, with no key for `b` or the relative import; the `unknown` line names `alpha`
  and the union of its 2 packs.
  Red when: a relative or repository-local import is counted, an imported kit or an armed language's
  pack is not applied, or a pack none of whose `langs` is armed is applied.
  fixture: the selftest builds the repository under the temp root, the kit copied beside it with the
  planted packs `alpha.toml` (`>=1.0,<2.0`), `alpha2.toml` (kit `alpha`, `>=2.0,<3.0`), `beta.toml`,
  `gamma.toml`, `python.toml` (kit `python`), `shell.toml` (kit `shell`, `langs = ["sh"]`) and
  `jsalpha.toml` (kit `jsalpha`, `langs = ["js"]`) in place of the shipped ones.
- **AC2** — When the fixture adds, one at a time, `requirements.txt` holding `alpha==1.4`,
  `pyproject.toml` whose `[project]` `dependencies` hold `alpha==1.4`, `package.json` whose
  `dependencies` hold `"beta": "1.2.0"`, and `composer.json` whose `require` holds `"beta": "1.2.0"`,
  each run applies `alpha` from `alpha.toml` alone, or `beta` though no file imports it.
  Red when: a manifest kind is not read, or its pin does not narrow the union.
- **AC3** — When `requirements.txt` holds `alpha==3.1`, the line `took >=2.0,<3.0, the nearest below
  3.1` prints and `alpha2.toml` alone applies; with `alpha==0.9`, the line `0.9 is below every range;
  no pack applied` prints.
  Red when: a version outside every range applies nothing silently, or applies a range above it.
- **AC4** — When `requirements.txt` holds `alpha>=1.5`, the `span` line names `alpha` and both packs
  apply.
  Red when: a span of minors takes one pack.
- **AC5** — When `check_version_in_range` is called with `("1.4", ">=1.0,<2.0")`, `("2.0",
  ">=1.0,<2.0")`, `("3.12.1", "~=3.12")` and `("3.13", "==3.12.*")`, it returns `True`, `False`, `True`
  and `False`.
  Red when: a boundary or a compatible-release range is misread.
- **AC6** — When the fixture's tracked tree holds `numpy` imports only, under `detected` the tally
  reads `uncovered=1 (numpy)` and the run exits as it did without the import.
  Red when: a kit with no pack is silent, or turns the run red.
- **AC7** — When `.lexicon.conf` carries `PACKS:` with a row naming kit `delta` and a valid custom pack
  `delta.toml` under the fixture's `packs/` directory, `delta` applies; when that pack carries a row
  with no `name`, `--check` exits 1 naming the pack's path and the row; when the row's path instead
  climbs out of the repository through a `..` segment, the run exits 1 naming the conf line; when a row reads `zeta  shipped`, it exits 1 naming `zeta`; when the custom pack's
  header names kit `omega`, it exits 1 naming both kits.
  Red when: a malformed, escaping, unknown or mismatched declaration is accepted.
- **AC8** — When the fixture commits `.governance/policy.toml` setting `lexicon.packs` to `detected`,
  AC7's valid `delta` row is reported ignored and does not apply; to `declared`, only `delta` and the
  rows `PACKS:` names apply and the line says detection is off; to `all`, `gamma` applies too; with no
  policy file, AC1's and AC7's applied sets join.
  Red when: any value applies a set its row of "What each value applies" excludes.
  fixture: the policy kit beside the kit copy, as I7 resolves it; the file is committed because
  `policy.py get` reads the landed revision.
- **AC9** — When `python lexicon.py --suggest run_delta --as py.function --base delta.Base` runs in
  AC7's fixture with `delta`'s pack holding that member row, it prints `FORCED` with a `pack:delta:`
  source; with `lexicon.packs` committed as `detected`, it prints today's answer.
  Red when: `--suggest` ignores a declared custom pack, or applies one `detected` excludes.
- **AC10** — When the fixture's `OUT_OF_SCOPE:` block carries a row covering `fixtures/**` and a
  `package.json` under that tree lists `beta`, `beta` is not applied; with the row removed it is.
  Red when: a manifest the path selector excludes selects a pack.
- **AC11** — When `python lexicon_conf.py --print-rows PACKS .lexicon.conf` runs over AC7's conf, it
  prints the row's key `delta`, a TAB and its source exactly as typed, and exits 0.
  Red when: the block cannot be read back as typed.
- **AC12** — When `python tools/policy/policy.py get lexicon.packs` runs with no policy file it prints
  `detected-and-declared`; `grep -c lexicon.packs tools/policy/unsummarised-keys.txt` prints 0;
  `git grep -n 'read_policy_value("lexicon.packs"' -- tools/lexicon` prints at least one line; and
  `grep -n lexicon.packs help/policy.md` prints the consumer sentence.
  Red when: the row lacks `summary` or `usage`, no literal reader exists, or the help page omits it.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `lexicon naming predicates` · `policy fixtures` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 AC11 · the planted packs, manifests and committed policy values, its failing case `requirements.txt` pinning `alpha==1.4` while both `alpha` packs apply · none

## 8. Open questions

- **F1 — How is a pack no import can name detected, the Python data model and the shell hosts?**
  Options: (a) the census counts one implicit host per armed file, the language its `LANGS` row arms
  it under, read as the pattern-set id's first segment, so `py:python-ast` yields `python` and
  `sh:shell-tokens` yields `shell`, the `kit` values TOOL-dMindYourWords-7 gives `python-3.12.toml`,
  `python-3.14.toml` and `shell.toml`; (b) every language pack applies whenever its extension is armed,
  by a list of such packs in the kit; (c) only a `PACKS:` row detects them. (b) types a list beside the
  packs it describes, the copy `[one-fact]` refuses; (c) leaves `__init__` debt under the default value
  in every repository. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the most feature-rich
  survivor: the language is read from the declaration the extraction already obeys, and a Python
  module's implicit binding of `builtins` makes the language part of its import census. widens: none ·
  relaxes: none
- **F2 — What is "a kit" in a manifest and in the census, when an import name differs from its
  distribution name (`sklearn`, `scikit-learn`)?** Options: (a) match the header `kit` against both,
  PEP 503-normalised, and read a mismatch as two kits, the distribution's version unknown to the
  import; (b) a name-mapping table. (b) is a typed table of third-party facts. RESOLVED (agent,
  2026-10-29, delegated): (a), rung 3; the mismatch reads `unknown` and takes the union, the state the
  review assigns an unknown version. widens: none · relaxes: none
- **F3 — Does the uncovered report name Node's core modules?** Options: (a) yes, as any bare
  specifier with no pack; (b) a curated list of Node core modules excluded; (c) ask a live `node`.
  (b) types Node's own inventory into the kit; (c) is a live read every node answers differently.
  RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, measured at five names on this tree (§4); the
  report is informational and never red. widens: none · relaxes: none
- **F4 — What does `--suggest` select with no corpus pass?** Options: (a) S8's set, every version of a
  kit unioned and custom packs per value; (b) run the census, a corpus walk. (b) breaks the contract
  at `lexicon.py:3727-3730`. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3; the given base names
  its own module, so a member row's pack is detected wherever that base resolves. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Item 8 and v2:1206, the lexicon review's
  `[packs]` "Selection", L-5 and its settled table, review finding M21 (B) on the selection states,
  scout B's row 8, and the spec brief's I6, I7, I8 and I10.

## 10. Reuse audit

The seams extended are `scan_corpus` (`tools/lexicon/lexicon.py:2262`), whose `defs[2]` imports the
census reads without changing its shape; the `BLOCK_KEYS` and `_BLOCK_PARSERS` door
(`tools/lexicon/lexicon_conf.py:37`, `:401`), which the comment at `:393` prices at one row plus its
parser; `_parse_rows` (`:187`) for the row split and its duplicate refusal; `--print-rows` (`:501`);
`measure_pass`'s `problems` (`:2796`); and I7's literal policy read. `python
tools/codebase-map/reuse_lookup.py "count imported top-level modules and read dependency versions from
project manifests"` ranked `read`, `read_text`, `counts`, `manifest` and `read_conf` first, each a
name-stem match; its `manifest` hit is a test-suite helper in `tools/check-testsuite-counts.test.sh`
and reads no dependency manifest, so S2 and S4 are new. Scout B's row 8 holds against source at
`ba8b3c8c4`: `BLOCK_KEYS` is at `:37`, `_BLOCK_PARSERS` at `:401-402`, and the `lexicon.packs` row at
`catalogue.toml:411-415` has no reader. The recall probe surfaced debt-fold row `import-census` (lexicon
review :666), which refutes a missing census input, and the review's four selection states, which §4
"The states" carries.

Recall terms used: `python tools/memory-recall/query.py "how are lexicon packs selected from the import
census and manifests with custom packs" --terms "lexicon packs selection import census manifest
pyproject package.json custom pack detected declared"`
