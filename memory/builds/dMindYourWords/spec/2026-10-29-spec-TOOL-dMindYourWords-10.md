# TOOL-dMindYourWords-10 — drift beyond verbs: one verb per declared family per object, and a noun canon

**Status:** DEFERRED · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 13 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0271@09fb0fff whole
**Carries:** node:policy-key.lexicon.drift

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-10-deviation-101.md](../build/2026-10-29-build-TOOL-dMindYourWords-10-deviation-101.md) | deviation | — |
| [2026-10-29-build-TOOL-dMindYourWords-7-reuse-scout-b.md](../build/2026-10-29-build-TOOL-dMindYourWords-7-reuse-scout-b.md) | research | TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-1 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-12 TOOL-dMindYourWords-11 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-16 TOOL-dMindYourWords-13 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

The lexicon grades a name by its leading token alone, so `load_conf`, `read_conf` and `parse_conf`
all pass while naming one thing three ways, and `sha`, `oid`, `hash` and `digest` name one concept
four ways unchecked (gap-lex-05). This unit adds two predicates the clause states: one verb per
declared family per object, over families the selected packs and the owner declare (LX-1), and a
noun canon of clusters written exogenously, the corpus deciding only which clusters are live, both
governed by `lexicon.drift` (lexicon review `[drift]` :355-388, L-3 :535-541, settled :570).

## 2. Scope (IN)

- **S1** — The shipped noun canon `canon.NOUNS` in `tools/lexicon/canon.py`, a tuple in `CLUSTERS`'
  shape `(representative, gloss, (alternative, ...))` (`canon.py:55`), holding exactly two clusters:
  `sha` with alternatives `oid`, `hash` and `digest`, and `dir` with `directory` and `folder`, the two
  the gap register names. It is read only through the existing `build_clusters`, `build_form_index`
  and `read_gloss` (`canon.py:84`, `:150`, `:167`) called with `clusters=canon.NOUNS`; no new canon
  function. `build_clusters` gains one keyword, `label="CANON"`, which its four refusal messages
  print in place of the literal `CANON`, so a noun overlay's refusal names `NOUNS`. Observed by AC1.
- **S2** — The owner's noun overlay, a `NOUNS:` block in `.lexicon.conf`: one `BLOCK_KEYS` row
  (`tools/lexicon/lexicon_conf.py:37`) and one `_BLOCK_PARSERS` row (`:401`) that reuses
  `_parse_canon` (`:365`), which gains a `block` argument naming the block in its two refusals. `run()`
  merges it beside the `CANON:` merge (`tools/lexicon/lexicon.py:3536`) as
  `canon.build_clusters(conf.get("NOUNS") or {}, clusters=canon.NOUNS, label="NOUNS")`, so its
  refusals land with the other declaration refusals, above the corpus walk. Observed by AC2.
- **S3** — Families, declared and never inferred. A `FAMILIES:` block, rows
  `<family> <representative> <representative>...`, parsed by a new `_parse_families` beside
  `_parse_canon`: a family name and each member alphabetic, at least two members, no member twice in
  a row. `read_declared_families(conf, packs, clusters)` in `lexicon.py` returns
  `{family: (representative, ...)}`: each pack `resolve_packs` returns for `lexicon.packs`
  (TOOL-dMindYourWords-8) contributes its header's `families` table, `<family> = [<verb>, ...]`, read
  through `load_pack` (TOOL-dMindYourWords-7), and an owner row replaces a pack's family of the same
  name. No first-wave pack declares one (TOOL-dMindYourWords-7 §8 F1). It refuses,
  naming the row and its source, a member that is no representative of the merged verb clusters and
  a representative that two families claim. The block changes only through `instructions.edit`, the
  write path TOOL-dMindYourWords-11 guards. Observed by AC3.
- **S4** — The family predicate, in `measure_pass` after the forced check and the P1 split
  (`lexicon.py:2930-2965`). Its population is every graded function definition whose leading verb is
  a declared `VERBS` row whose representative belongs to a declared family, that the forced check
  (TOOL-dMindYourWords-2, `Offender.source`) does not grade forced, and whose object is not empty. The
  object is the subtokens after the verb (`subtokens.py:33`), each mapped through the noun form index
  to its representative, joined by `_`. `scan_family_splits` groups the population by family and
  object; a group carrying two or more distinct verbs is a split. Observed by AC4.
- **S5** — The established verb. `derive_established_verbs(root, sites, rev=None)` reads each split
  group's earliest-landed site: one `git blame --porcelain -w` per file holding a site, with one
  `-L <line>,<line>` per site, at `rev` when it names a commit, over the working tree when it is
  `None`, and with `--contents` over HEAD's history for any other source text; an uncommitted line
  reads as the latest. The verb of the earliest `author-time` is established. Every definition of the
  group using another verb is an offender of rule `drift`, `Offender.grade` `debt`, its detail naming
  the family, the object, the established verb and the earliest site. A group whose earliest time is
  shared by two verbs is a tie: one `drift tie` line naming the group, and no offender. A forced name
  never establishes a verb and is never a `drift` offender, because S4 leaves it out. Observed by AC5
  and AC6.
- **S6** — The noun predicate. `scan_noun_variants` grades every subtoken of a graded function
  definition after its leading verb, and every subtoken of a graded type, against the merged noun form
  index: a subtoken that is an alternative of a cluster is an offender of rule `noun`, grade `debt`,
  its detail "`<form>` is a spelling of `<representative>`". A forced name is never a `noun`
  offender. A cluster with no form among the graded subtokens is dormant and grades nothing; the
  corpus decides liveness and nothing else. Observed by AC7.
- **S7** — `lexicon.drift`, read once per run in `run()` through
  `read_policy_value("lexicon.drift", root)` (TOOL-dMindYourWords-1, I7), its values and default the
  catalogue row's verbatim (`tools/policy/catalogue.toml:406`). `refuse-new`, the default: the
  `drift` and `noun` offenders join the measured offenders, so they are keys `render_offender_keys`
  prints, debt `measure_debt_keys` counts for the pin (TOOL-dMindYourWords-1 S2) and keys the by-name
  comparison grades. `report`: S4 to S6 run, their
  findings print under `--list` and on the tally line, and none is a key or debt. `off`: S4 to S6 do
  not run. Observed by AC8 and AC9.
- **S8** — The tally line, one line after the P1 line on `--check`, `--list` and `--measure`:
  `lexicon: drift=<n> noun=<n> ties=<t> families=<k> nouns-live=<l> (lexicon.drift=<value>)`, or
  `lexicon: drift not measured (lexicon.drift=off)`. With `families=0` it says no family is declared,
  so a family predicate that graded nothing is announced rather than read as clean. Observed by AC4
  and AC8.
- **S9** — The map's noun inventory. `_read_lexicon_verbs` (`tools/codebase-map/map_extractors.py:250`)
  becomes `_read_lexicon_block(block)`, returning the named block's row keys through the lexicon's own
  reader, and `EXTRACTORS` gains `"lexicon-nouns": lambda: _read_lexicon_block("NOUNS")` beside the
  `lexicon-verbs` row (`:246`). Every dossier's `[claims]` gains `lexicon-nouns`, because a dossier
  carries exactly the inventory ids (`tools/codebase-map/map_lib.py:1063`); the lexicon dossier claims
  the overlay's keys. `adopt-lexicon.sh`'s orphaned-extractor arm (`:400-415`) names either inventory,
  and the README's uninstall order names both. Observed by AC10.
  **Readers:** by name: `tools/codebase-map/map_extractors.py` (the `EXTRACTORS` row at `:246` and the
  definition at `:250`), the only source spelling `_read_lexicon_verbs`; the generated
  `memory/map/generated/symbols.json` re-renders · by value: NO VALUE READERS of the function's name;
  its value, the `lexicon-verbs` inventory, keeps its id and its output byte for byte.
- **S10** — The catalogue row `lexicon.drift` gains its `summary` and `usage`, and
  `python tools/policy/policy.py lists --write` drains its name from
  `tools/policy/unsummarised-keys.txt` (`:104`). No second row. Observed by AC11.
- **S11** — Arming on this tree. The shipped noun canon grades this corpus in the unit's build
  commit, so that commit carries a vocabulary record tagged `unit.lexicon.nouns`, written through
  TOOL-dMindYourWords-11's door with this unit's id as its cause, and runs
  `python lexicon.py --rebaseline <record>` (TOOL-dMindYourWords-11 S8), which sets the debt pin and
  prints the delta. No `FAMILIES:` row is written for this repository (§8 F2). Observed by AC12.
- **S12** — The help page `help/lexicon.md` gains a section on families, the noun canon and
  `lexicon.drift`'s three values, and `tools/lexicon/README.md` and `tools/lexicon/LEXICON.md` state
  both predicates. Where no earlier unit of this build wrote the page, this unit writes it and its
  row in `help/README.md`. Observed by AC13.

## 3. Non-goals (OUT)

- Refusing at commit and comparing by name at the bar: TOOL-dMindYourWords-9 builds both arms and
  observes the split table's nine cells (lexicon review :377-381) on them (§8 F3). This unit decides
  only what the predicates emit under each `lexicon.drift` value.
- Declaring this repository's own families, the acquire family over `load`, `read` and `parse`
  included: the owner's, through `instructions.edit` (§8 F2).
- Grading tag names against the families and the noun canon: TOOL-dMindYourWords-13.
- The re-baseline mechanism and the write path's record: TOOL-dMindYourWords-11. The debt pin and its
  keyed population: TOOL-dMindYourWords-1.
- Pack selection and the pack header's grammar: TOOL-dMindYourWords-8 and TOOL-dMindYourWords-7.
- Noun clusters beyond the two the gap register names: the owner's `NOUNS:` overlay adds them.
- A new drift-audit signal for the split counts: the tally line is the count `report` names.

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `read_policy_value` for `lexicon.drift`, `Offender.grade` for the `debt` grade S5 and S6 set, and `render_offender_keys`' rule values `drift` and `noun` (I1, I4, I7)
- **consumes-from** `TOOL-dMindYourWords-14` — `load_conf`'s repeated-header refusal, which must stand before the `FAMILIES:` and `NOUNS:` blocks land (I8)
- **consumes-from** `TOOL-dMindYourWords-11` — `--rebaseline` and the `unit.lexicon.nouns` record S11 writes in the arming commit, and the write path `instructions.edit` that guards `FAMILIES:` and `NOUNS:`: `RECORD_TAGS`, whose `NOUNS:` and `FAMILIES:` rows put both blocks under `--check-record`, so neither block changes without a record
- **consumes-from** `TOOL-dMindYourWords-7` — `load_pack`, through which S3 reads each selected pack header's `families`
- **consumes-from** `TOOL-dMindYourWords-2` — `Offender.source`, the forced check S4 and S6 ask of every candidate so a forced name never establishes a verb
- **consumes-from** `TOOL-dMindYourWords-8` — `resolve_packs`, the packs `lexicon.packs` selects, whose families S3 reads
- **hands-off** `TOOL-dMindYourWords-9` — `canon.NOUNS` and the `drift` and `noun` keys, which the commit arm and the by-name comparison grade, and the split table's nine cells, which that unit observes
- **hands-off** `TOOL-dMindYourWords-13` — `canon.NOUNS` and `read_declared_families`, against which a tag's nouns and verbs are graded
- **hands-off** external — the owner's declaration of this repository's acquire family through `instructions.edit`, which this unit does not write (§8 F2)
- **hands-off** `TOOL-dMindYourWords-29` — the drift tally, the drift blame, `scan_noun_variants`, its pin falls and its noun inventory id, which the minors batch repairs (review ids 2, 6, 22, 27, 28, 37, 48)

## 4. Design

### Evidence

At this base the P1 loop reads the leading verb and nothing after it (`lexicon.py:2941-2965`); no
code in `tools/lexicon/` groups definitions by object or models a noun (the population research,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-population.md`
:140-154: 57 objects carry two or more acquire-family verbs over 165 definitions; `sha` 13, `oid` 4,
`hash` 4, `digest` 10; `dir` 101, `directory` 1, `folder` 2; PINNED, measured 2026-10-15 over 5,428
definitions). The canon holds verb synonyms only (`canon.py:55-82`), so `load`, `read` and `parse`
are three clusters with three meanings, which is why the canon carries no families (LX-1).

### Data model

| Name | Where | Shape |
|---|---|---|
| `canon.NOUNS` | `tools/lexicon/canon.py` | `(("sha", gloss, ("oid", "hash", "digest")), ("dir", gloss, ("directory", "folder")))` |
| `NOUNS:` | `.lexicon.conf` | `_parse_canon`'s rows: `<representative> <alternative>...`, a leading `-` deleting a shipped cluster |
| `FAMILIES:` | `.lexicon.conf` | `<family> <representative> <representative>...` |
| family map | `read_declared_families` | `{family: (representative, ...)}`, owner rows over pack rows |
| split group | `scan_family_splits` | `{(family, object): [(path, line, name, verb)]}` with two or more verbs |
| offender | `measure_pass` | `Offender(kind, path, line, name, detail)`, rule `drift` or `noun`, grade `debt` |

The established verb is never stored. It is derived from history on every run, so nothing typed
beside the corpus can disagree with it.

### The flow in one pass

1. `run()` merges `CANON:` over `canon.CLUSTERS` and `NOUNS:` over `canon.NOUNS`, reads
   `lexicon.drift`, and, unless it is `off`, builds the family map from the selected packs and
   `FAMILIES:`.
2. `measure_pass` grades as today, the forced check runs, then `scan_family_splits` and
   `scan_noun_variants` run over the same materialised walk; nothing walks the corpus twice.
3. For each split group, `derive_established_verbs` blames only that group's sites. A group with one
   verb costs nothing.
4. Under `refuse-new` the offenders join `offenders["drift"]` and `offenders["noun"]`, which
   `render_offender_keys` prints as `<path>\tdrift\t<name>` and `<path>\tnoun\t<name>` (I4).

### Inventory

Names this unit mints, each asked of `lexicon.py --suggest <name> --as py.function` at this base and
answered OK: `_parse_families`, `read_declared_families`, `scan_family_splits`,
`derive_established_verbs`, `scan_noun_variants`, `_read_lexicon_block`. `NOUNS` is a module constant;
the `py.constant` cell is undeclared at this base, so no cell grades it. Conf blocks: `FAMILIES:`,
`NOUNS:`. Inventory id: `lexicon-nouns`. Offender rules: `drift`, `noun` (I4's spelling).

### Migration

An adopter's declaration without `FAMILIES:` or `NOUNS:` parses exactly as before, since an absent
block resolves to its empty container (`lexicon_conf.py:115-117`). The shipped noun canon applies
on its first run after the update, which raises debt; the adopter's next commit through the write
path runs the re-baseline. Under `lexicon.drift = "off"` nothing changes.

### Rollout

Lands after TOOL-dMindYourWords-14, so a repeated `FAMILIES:` or `NOUNS:` header is refused, and in
one commit with this repository's re-baseline (S11).

### Files touched (estimate)

- `tools/lexicon/canon.py`
- `tools/lexicon/lexicon_conf.py`
- `tools/lexicon/lexicon.py`
- `tools/lexicon/selftest.py`
- `tools/lexicon/adopt-lexicon.sh`
- `tools/lexicon/README.md`
- `tools/lexicon/LEXICON.md`
- `tools/codebase-map/map_extractors.py`
- `memory/map/features/` (each dossier's `lexicon-nouns` claim)
- `memory/map/generated/` (re-rendered by `gen_map.py --write`)
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt` (rendered by `policy.py lists --write`)
- `.lexicon.conf` (the re-baselined pin, through TOOL-dMindYourWords-11's door)
- `memory/builds/dMindYourWords/build/` (the re-baseline's record)
- `help/lexicon.md`
- `help/README.md`

### Alternatives rejected

- **Families inferred from the corpus.** Rejected by LX-1 (lexicon review :357-365): `load`, `read`
  and `parse` are three meanings, and an inferred family would make one of them debt by majority.
- **Families as a fourth field of `CLUSTERS`.** Rejected: the canon is synonyms, and a family groups
  representatives, so a field on a cluster cannot express a family over three clusters.
- **The majority verb as established.** Rejected by the test §8 F1 states: on a group of two `load`
  and one `read`, adding a second `read` flips the majority and re-keys the two `load` definitions, so
  a branch would be refused for sites it never touched.
- **Every definition of a split group as debt.** Rejected by the same test: adding a definition that
  uses the established verb adds a key, so the conforming choice is refused.
- **A noun canon derived from corpus frequency.** Rejected by the clause: the clusters are written
  exogenously and the corpus decides only which are live.

## 5. Production-readiness checklist

- security — N/A: the predicates read the tracked corpus and git history and write nothing.
- perf / scale — one blame per file holding a split-group site; 0.08 to 0.10 s per file on this node
  (PINNED, measured 2026-10-29 over `tools/lexicon/lexicon.py` and `tools/codebase-map/map_lib.py`).
  No family is declared on this tree, so the family predicate costs nothing here until one is.
- error / empty / loading states — no family declared prints `families=0` with its sentence; a blame
  that fails (no git, a shallow history) reads every site of that file as latest, so its group ties
  and reports; an overlay refusal is a declaration refusal at exit 1.
- observability — the tally line on every mode, the `drift tie` lines, each offender's detail.
- risks — the noun canon raises this repository's debt once; S11 records it through the re-baseline.
- testing — planted fixtures in `tools/lexicon/selftest.py` per §6; New arm lines in §7.
- migration — §4 Migration.
- user docs — `help/lexicon.md` (S12).

## 6. Acceptance criteria

The drift fixture is a scratch git repository under `%TEMP%` with a short name. Its `.lexicon.conf`
declares `LANGS="py:python-ast:parser"`, `VERBS` rows `load`, `read`, `parse` and `check`, and
`FAMILIES: acquire load read parse`. Its first commit adds `a.py` defining `load_conf`; its second
adds `b.py` defining `read_conf` and `check_oid_cache`. Policy is a committed
`.governance/policy.toml` on its default branch. Each command runs with the fixture as its working
directory and this repository's `tools/lexicon/lexicon.py` as the engine.

- **AC1** — When `python -c "import canon; print(canon.build_form_index(canon.NOUNS)['oid'])"` runs
  in `tools/lexicon/`, it prints `sha`; `canon.build_clusters({"sha": ()}, clusters=canon.NOUNS,
  label="NOUNS")` raises a `ValueError` whose text names `NOUNS`.
  Red when: `NOUNS` is absent, or a noun overlay's refusal names `CANON`.
- **AC2** — When the fixture's `.lexicon.conf` gains `NOUNS:` with the row `-tmp`, `lexicon.py
  --check` exits 1 naming the row and `NOUNS`; with the row `sha oid`, `oid` still grades and `hash`
  no longer does.
  Red when: a bad noun row is ignored, or the overlay does not replace the shipped alternatives.
- **AC3** — When the fixture's `FAMILIES:` row is `acquire load fetch`, `lexicon.py --check` exits 1
  naming `fetch` as a spelling of `load`; when a second row `io read write` is added beside the first,
  it exits 1 naming `read` and both families.
  Red when: either row parses.
- **AC4** — When `lexicon.py --offenders` runs in the drift fixture, it prints the key
  `b.py\tdrift\tread_conf` and no `drift` key for `load_conf`, and the tally line from `lexicon.py
  --measure` reads `drift=1`; with the `FAMILIES:` block deleted, the tally reads `families=0` and
  says no family is declared.
  Red when: `read_conf` passes, or `families=0` prints a bare zero.
- **AC5** — When the fixture's commit order is reversed, so `read_conf` lands first, `lexicon.py
  --offenders` prints `a.py\tdrift\tload_conf` and no key for `read_conf`; when one commit adds both,
  it prints a `drift tie` line naming `acquire` and `conf`, and no `drift` key.
  Red when: the established verb ignores landing order, or a tie keys either site.
- **AC6** — When `b.py`'s class `Loader(Base)` defines `read_conf` and the forced check grades it
  forced, `lexicon.py --offenders` prints no `drift` key for it, and a later `parse_conf` is keyed
  against `load_conf`, not against `read_conf`.
  Red when: a forced name is keyed, or establishes the verb.
  fixture: needs TOOL-dMindYourWords-2's forced check and TOOL-dMindYourWords-7's pack; planted per
  their fixtures.
- **AC7** — When `lexicon.py --offenders` runs in the drift fixture, it prints
  `b.py\tnoun\tcheck_oid_cache`, and `lexicon.py --list` names `oid` as a spelling of `sha`; a type named
  `DirCache` yields no `noun` key.
  Red when: `oid` passes, or a representative is keyed.
- **AC8** — When the fixture's committed `.governance/policy.toml` sets `[lexicon]` `drift =
  "report"`, `lexicon.py --offenders` prints no `drift` and no `noun` key while the tally line reads
  `drift=1 noun=1`; with `drift = "off"`, the tally reads `drift not measured`; with
  `drift = "refuse-new"` or no key, both keys print.
  Red when: `report` keys a finding, `off` measures one, or the default omits a key.
- **AC9** — When `git grep -n 'read_policy_value("lexicon.drift"' -- tools/lexicon/lexicon.py` runs,
  it finds one call, the literal reader the policy kit's reader-coverage arm reads.
  Red when: the key is read through a variable and the arm finds no reader.
- **AC10** — When `python tools/codebase-map/gen_map.py --check` runs after the unit, it reports the
  `lexicon-nouns` inventory claimed in every dossier and nothing stale; `grep -c "lexicon-nouns"`
  over each file in `memory/map/features/` prints 1.
  Red when: a dossier lacks the claim, or the extractor reads a second parser of the conf.
- **AC11** — When `grep -c "^lexicon.drift$" tools/policy/unsummarised-keys.txt` runs after
  `policy.py lists --write`, it prints 0, and the catalogue's `lexicon.drift` row carries `summary`
  and `usage`.
  Red when: the name stays listed, or a second row is added.
- **AC12** — When `lexicon.py --measure` runs at the unit's build commit, the debt it prints equals
  the pin `--rebaseline` set, and the commit holds the `unit.lexicon.nouns` record naming
  `TOOL-dMindYourWords-10` as its cause, with the `re-baseline unit.lexicon.nouns: debt <old> -> <new>`
  line it printed.
  Red when: the pin backstop reds at the build commit, or the delta has no record.
  figure: the delta is DERIVED at the build commit by `lexicon.py --measure`.
- **AC13** — When `grep -n "lexicon.drift\|FAMILIES:\|NOUNS:" lexicon.md` runs in `help/`, each matches.
  Red when: the page omits one.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `govkit acceptance matrix` · `policy fixtures` · `straggler-guard arms` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC7 AC8 · the drift fixture with a reversed commit order, a tie, a non-canon noun, each `lexicon.drift` value and each refused overlay row, staged against today's engine, which keys none of them · none
New arm: tools/lexicon/selftest.py · covers AC6 · a forced `read_conf` under a packed base, staged with the forced check removed from the drift population · none

## 8. Open questions

- **F1 — How is a split group's established verb derived?** (a) The earliest `author-time` that
  `git blame` gives over the group's sites, blamed only for split groups; (b) the verb most of the
  group's definitions use; (c) no established verb, every definition of a split group being debt. The
  test: on a group of two `load_conf`-style definitions and one `read_conf`, add a definition using
  `load`. Under (a) no key is added; under (b) adding a second `read` instead flips the majority and
  re-keys untouched sites; under (c) the conforming addition is itself a key. Only (a) leaves a
  by-name comparison stable, and it is the lexicon review's own rule (:367-368). Rung 3.
  RESOLVED (agent, 2026-10-29, delegated): (a). widens: none · relaxes: none
- **F2 — Does this unit declare this repository's acquire family?** (a) No: it ships the mechanism and
  the owner declares families through `instructions.edit`; (b) the build writes
  `FAMILIES: acquire load read parse`. The clause gives families to the packs and to "the owner
  through `instructions.edit`", and the review refuses a session adding vocabulary on its own
  (:409-413). Rung 1, v2's clause. RESOLVED (agent, 2026-10-29, delegated): (a); the return names
  the owner's declaration as an external hand-off. widens: none · relaxes: none
- **F3 — Which unit observes the split table's cells across `lexicon.at-commit`?** (a)
  TOOL-dMindYourWords-9, which builds the commit arm and the by-name comparison those cells exercise;
  (b) this unit, at an order before either arm exists. (b) cannot run its observation at order 13.
  Rung 3. RESOLVED (agent, 2026-10-29, delegated): (a); this unit observes the `lexicon.drift`
  column of what the predicates emit (AC8). widens: none · relaxes: none
- **F4 — What does "an object already split is reported for the owner instead of refused" mean for a
  pass that reads one tree?** (a) The splits present when the predicate first arms join the pin
  through the re-baseline and refuse nothing; afterwards a definition departing from its object's
  established verb is a key like any other, and only a tie reports; (b) a group split at the base
  never refuses a definition a branch adds to it, which puts the base inside every measurement and
  makes this tree's debt count depend on which branch measures it. (b) fails S4's one-walk design and
  the pin's count. Rung 3, with the review's own "existing splits become debt with their rename,
  through the re-baseline" (:388). RESOLVED (agent, 2026-10-29, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (TOOL-dMindYourWords-29); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended: the canon's tuple and its three readers, `build_clusters`, `build_form_index`
and `read_gloss` (`tools/lexicon/canon.py:84`, `:150`, `:167`), which already take the tuple as a
parameter; the conf reader's block door, `BLOCK_KEYS` and `_BLOCK_PARSERS`
(`tools/lexicon/lexicon_conf.py:37`, `:401`), with `_parse_canon` (`:365`) reused for `NOUNS:`; the
splitter `subtokens` and `leading_verb` (`tools/lexicon/subtokens.py:33`, `:39`); the P1 loop in
`measure_pass` (`tools/lexicon/lexicon.py:2930-2965`); and the map's verb inventory
`_read_lexicon_verbs` (`tools/codebase-map/map_extractors.py:246-275`), extracted at its second
instance rather than copied. The probe `python tools/codebase-map/reuse_lookup.py "group definitions
by the object after the verb and refuse two verbs of one family over one object"` ranked
`leading_verb` (SEAM, fan-in 4) and nothing that groups by object; `python
tools/codebase-map/reuse_lookup.py "a closed set of noun spellings merged with an owner overlay and
normalised to one representative"` ranked `merge` and `resolve_pattern_sets` by name stem, neither a
canon. So no existing seam fits the family grouping or the blame read, and both are new over the
seams above. Where scout B's record disagrees with source at this base: it cites `build_clusters` at
`canon.py:72` and the two readers at `:135-158`; they sit at `:84`, `:150` and `:167`.

Recall terms used: `python tools/memory-recall/query.py "how are verb families and a noun canon
declared and checked for drift beyond verbs" --terms "lexicon drift family noun canon CLUSTERS
build_clusters overlay leading_verb object split debt"`
