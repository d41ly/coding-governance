# TOOL-dTrueNorth-1 — the clause ids and binding lines, parsed once, behind a cutoff

**Status:** CLOSED · rev-2 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 1

**Carries:** cl-dClosedLoop-0001@83b6b117 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-1-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-1-ledger.md) | journal | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-1-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-build-brief.md) | journal | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-1-owner-audit-cap.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-owner-audit-cap.md) | research | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md) | research | TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 |
| [2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) | spec-audit | TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 |
| [2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md) | diff-review | TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing in the product reads a design clause or a spec's claim to carry one: the only reader is the
bootstrap instrument `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py`,
which no gate runs (gap-design-13). This unit ships the one parser every later reader imports, as
`tools/memory-tree/design_lib.py`: each clause of the design with its minted `cl-` id and the hash of
its text as the design's `[clause-ids]` section defines it, the ids that section withdraws, and each
spec's `**Carries:**`, `**Derived:**`, `**Moved:**`, `**Retired:**` and `**Deferred:**` lines, a
malformed line refused by name. It also declares the five `.memory-tree.conf` keys that say where the
design is and from which spec date the chain builds' specs alone are read.

## 2. Scope (IN)

- **S1** — Five keys in gov's `.memory-tree.conf`, each under a comment block in the file's house
  style: `SPEC_CARRIES_CUTOFF="2026-10-21"`, the date of the opening landing `271aa59de`;
  `DESIGN_RECORD` naming v2; `DESIGN_BASELINE` holding the pin
  `59ff8f2ac04a967751eae00de6856afbea66c033`; `DESIGN_VIEW` naming the as-built view
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`; and
  `DESIGN_NODES` naming the owned-node deriver, today
  `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py` (§8 F2). The kit's
  example conf declares none of them. Observed by AC10.
- **S2** — `derive_clause_hash`, the first eight hex digits of the SHA-256 of a clause's UTF-8 text
  with its trailing `cl-` id cut off and each whitespace run folded to one space, exactly as
  `carries.py:85-87` takes it. Observed by AC5.
- **S3** — `read_design_view`, the view reader: every row of `DESIGN_VIEW`'s table, parsed by the
  as-built row grammar `asbuilt.py:33`, as `(build, clause id, text, hash8, since)`, plus
  `extract_clause_tokens`, a clause's backticked names as `carries.py:104` takes them. A view with
  no row, a row whose id repeats, or a key naming no readable file is a named refusal. The chain
  builds are the view's Build column; no build list is typed anywhere. Observed by AC5, AC6.
- **S4** — `read_retired_ids`, the withdrawn ids the `[clause-ids]` section of `DESIGN_RECORD`
  lists, read from the blob at `DESIGN_BASELINE` and never from the working tree, as
  `carries.py:106-107` reads that list. A baseline
  that names no object, or a record absent at it, is a named refusal. Observed by AC7.
- **S5** — `read_owned_nodes`, each chain build's owned nodes as `<ns>.<key>`, read from the
  deriver `DESIGN_NODES` names: its `derive()` and its own `OWNED` tuple, joined by owner exactly as
  `carries.py:111-119` joins them. A deriver that is not a tracked `.py` file, or whose `derive()`
  raises, is a named refusal. Observed by AC8.
- **S6** — `parse_binding_lines`, the binding-line parser. A line at column 0 that opens with one of
  the five bold keys and sits outside a fenced block is a binding. Each parses to a clause carried
  `whole` or as `part k/n`, an owned node as `node:<ns>.<key>`, a `**Derived:**` decision, or a
  release line with its decision, the three release keys §4's data model names. Every line that opens with a key and
  fails its grammar is collected, and the parser raises once naming each `path:line`, the line and
  the grammar it fails. Called with `strict=False` it returns the well-formed bindings and passes
  over the rest, which is how a caller reads a past revision that a later one corrected.
  Observed by AC1, AC2, AC3, AC4.
- **S7** — `scan_chain_specs`, the population: the tracked spec files under a chain build's
  `spec/` folder, at any depth, whose filename date is on or after the cutoff its caller passes,
  with the paths it passed over counted by reason. The cutoff is a parameter, read by the caller
  through `read_cutoff_key` (`tools/check-spec-tokens.py:650-670`), so this module reads no date
  key. Observed by AC9.
- **S8** — `read_design`, the one composition the readers above share: the four `DESIGN_*` values
  from the caller's conf, validated, then the view, the withdrawn ids and the owned nodes, returned
  as one value. A blank key is a refusal naming the key. Observed by AC11.
- **S9** — A command line for probes and authors, three verbs: `--parse <path>...`,
  `--design [--build <slug>]` and `--chain-specs <cutoff>`. Exit 0 clean, 1 on a malformed line
  or a refusal, 2 when the `DESIGN_*` keys are blank, so nothing was read. Observed by AC1, AC5,
  AC9, AC11.

## 3. Non-goals (OUT)

- The join. Ghost ids, stale pins, ambiguity, the stopped-carrying arm, the token arm and the
  never-green rule are `TOOL-dTrueNorth-2`'s; this unit parses and refuses malformed lines only.
- The coverage region and the hygiene refusal, which are `TOOL-dTrueNorth-3`'s.
- Minting clause ids or editing v2, the as-built view or any instrument (the packet's Non-goals).
  `2026-10-19-build-PLAY-dClosedLoop-1-clause-ids.py` stays the minter.
- A `memory/TEMPLATE-SPEC.md` section stating the binding grammar for chain spec writers. It is a
  separate document, so a separate unit (BUILD-METHOD M2); this unit's docstring and the conf
  comment are the grammar's home until one is specced. Named as a follow-up.
- Generalising the grammars beyond what `carries.py:50-56` admits. A decision id stays
  `[A-Z]+-d[A-Z]\w+-\d+` and a build slug `d[A-Z]\w+`, the instrument's own shapes, so the product
  and the instrument read one grammar while both run.
- Any reader for an adopter. The keys are gov's: blank or absent, nothing here is read.

### Edges

- **hands-off** `TOOL-dTrueNorth-2` — the parser and readers in `design_lib.py`, and the cutoff key `SPEC_CARRIES_CUTOFF` its join reads through `read_cutoff_key`
- **hands-off** `TOOL-dTrueNorth-3` — `read_design_view`'s Build column, which names the chain builds whose README carries a coverage region
- **hands-off** `TOOL-dTrueNorth-4` — the binding-line parser in `design_lib.py`, imported by its deviation population
- **hands-off** `TOOL-dTrueNorth-6` — the view reader in `design_lib.py`, imported by its generator
- **hands-off** `TOOL-dTrueNorth-16` — `design_lib.py`'s readers, which that unit extends with `read_design_keys`, `read_spec_revisions` and `SPEC_FILE_DATE` for the round-1 spec audit's ids 5, 20, 23, 25 and 43

## 4. Design

### Evidence

- The instrument's grammars are `carries.py:50-56`: `CID`, `CARRY`, `DERIVED` and `RELEASED`. Its
  hash is `clause_hash` at `carries.py:85-87`. Its clause tokens are the backticked names of the
  clause body at `carries.py:104`. It reads v2's `[chain]` directly (`carries.py:90-105`) and its
  withdrawn ids from `[clause-ids]` (`carries.py:106-107`). It reads lines with `re.M` over the
  whole text, fenced blocks included, and silently ignores a line that fails `CARRY`.
- Owned nodes come from the map instrument's `derive()`, joined by the `owner` relation over the
  `OWNED` namespaces (`carries.py:108-119`). The map instrument declares the same tuple at
  `2026-10-17-build-PLAY-dClosedLoop-1-map.py:43` and resolves its sources from its own file
  location, so it reads correctly whatever the caller's working directory.
- The view's row grammar is `asbuilt.py:33`, `ROW`. A probe this pass ran over the view at base
  parsed 509 rows across 22 builds, and `clause_hash` of each row's text equalled `carries.py`'s
  hash of the same clause in v2 for all 509 (PINNED, measured 2026-10-21 at `271aa59d`). Reading
  clauses from the view therefore leaves every pin unchanged until a deviation's `amends` row moves
  one, which is S2 of the spec brief's interfaces.
- `[clause-ids]` today reads `Retired: none.` (v2:1807), so the withdrawn set is empty.
- `read_cutoff_key` refuses a set value that is not a real ISO date
  (`tools/check-spec-tokens.py:650-670`). `check_cutoff_relation` (`:593-626`) is called for
  `SPEC_DIRECT_CUTOFF` and `SPEC_GUARD_LEGS_CUTOFF` only (`:1072-1073`), and not for
  `SPEC_HANDOFF_CUTOFF`.
- `tree_lib.parse_conf` (`tools/memory-tree/tree_lib.py:132-143`) is the kit's conf reader and
  `tree_lib.unfenced_lines` (`:146`) its fence reader.

### Data model

A binding is one dict per line:

| field | value |
|---|---|
| `kind` | `carries`, `derived`, `moved`, `retired` or `deferred` |
| `line` | the 1-based line number in the text |
| `clause` | the `cl-` id, or None for a node or a `**Derived:**` line |
| `hash` | the pinned hash8 of a clause carry, else None |
| `part` | `(k, n)` for `part k/n`, None for `whole` |
| `node` | `<ns>.<key>` for a node carry, else None |
| `decision` | the decision id of a `**Derived:**` or release line, else None |
| `to` | the receiving build of a `**Moved:**` line, else None |

The grammars, each at column 0 with optional trailing whitespace and nothing else on the line:

| key | grammar |
|---|---|
| `**Carries:**` | `<cl-id>@<hash8> whole`, `<cl-id>@<hash8> part k/n` with 1 ≤ k ≤ n and n ≥ 2, or `node:<ns>.<key>` with `<ns>` as `[a-z-]+` |
| `**Derived:**` | `<decision id>` |
| `**Moved:**` | `<cl-id> to <build> by <decision id>` |
| `**Retired:**`, `**Deferred:**` | `<cl-id> by <decision id>` |

The shapes are the instrument's: `<cl-id>` is `cl-d[A-Z]\w+-\d{4}`, `<hash8>` eight lowercase hex
digits, `<build>` `d[A-Z]\w+`, and `<decision id>` `[A-Z]+-d[A-Z]\w+-\d+`. Two tightenings over
`RELEASED`, each refusing a line the instrument would misread rather than reading one it refuses:
a `**Moved:**` line must name its receiving build, and a `**Retired:**` or `**Deferred:**` line must
not. A `part k/n` outside the bounds above is malformed here; the instrument catches it later, as a
parts sequence that is not 1 to n.

`read_design(root, conf)` returns:

```python
{"baseline": "<40-hex>", "view": "<path>",
 "rows": [(build, cid, text, hash8, since), ...],          # view order
 "builds": {build: {cid: (text, hash8, since)}},
 "retired": {cid, ...},
 "nodes": {build: {"<ns>.<key>", ...}}}
```

`since` is `baseline` or `deviation <record id>`, the view's own cell. `DesignRefusal(ValueError)`
carries every refusal; its message names the key, the path or the `path:line`, so a caller prints
it whole.

### Behaviour

- **Fenced blocks are not read.** `parse_binding_lines` walks `tree_lib.unfenced_lines`, so a spec
  may show a binding line as an example inside a fence. That is the house rule the claims join keeps
  (`tools/check-spec-tokens.py:22-23`). A text that ends inside an open fence is a refusal naming the
  fence's line, because every line after it would otherwise be skipped unseen. A spec author must
  still keep a column-0 example out of prose: the instrument reads fences, and it checks this build's
  specs at the Design exit.
- **A malformed line is collected, not first-hit.** The parser reads the whole text, then raises one
  `DesignRefusal` listing every malformed `path:line` with the line and the grammar it fails.
  `strict=False` is the one exception, for history: a revision a later commit corrected is read for
  what it carried, and its malformed lines are not this commit's finding.
- **The view reader validates once.** The table is the rows `asbuilt.py:33`'s grammar matches; a
  table line it does not match, inside the table, is a refusal, so a hand edit that breaks a row
  cannot shrink the clause population silently.
- **The deriver is loaded by path.** `importlib.util.spec_from_file_location` on the tracked file
  `DESIGN_NODES` names, then its `derive()`, then its `OWNED`. Nothing else in it is called.
- **The cutoff gates the population, not the parser.** `scan_chain_specs(paths, builds, cutoff,
  memory_root="memory")` keeps a path when its build is a chain build and its filename date, read as
  `/(\d{4}-\d{2}-\d{2})-spec-`, is on or after `cutoff`. It counts what it passed over as
  `other-build`, `pre-cutoff` and `undated`. Statuses are not read here: which statuses carry is the
  join's choice.
- **No conf date key is read here.** `SPEC_CARRIES_CUTOFF` reaches this module only as a parameter.
  The CLI's `--chain-specs` takes it as an argument for the same reason, so the date has one reader.
  The relation check is not applied to it, as it is not applied to `SPEC_HANDOFF_CUTOFF`: the key
  exists to grade this build's own specs, dated on its own day.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `design_lib.py` | new module | `tools/memory-tree/` |
| `DesignRefusal` | exception class | design_lib |
| `CLAUSE_ID`, `CARRY`, `DERIVED`, `RELEASED`, `BINDING_HEAD`, `VIEW_ROW` | compiled patterns | design_lib |
| `DESIGN_KEYS` | tuple of the four `DESIGN_*` key names | design_lib |
| `derive_clause_hash` | function | design_lib |
| `extract_clause_tokens` | function | design_lib |
| `read_design_view` | function | design_lib |
| `read_retired_ids` | function | design_lib |
| `read_owned_nodes` | function | design_lib |
| `parse_binding_lines` | function | design_lib |
| `scan_chain_specs` | function | design_lib |
| `read_design` | function | design_lib |
| `main` | CLI entry, `--parse`, `--design`, `--chain-specs`, `--build` | design_lib |
| `SPEC_CARRIES_CUTOFF`, `DESIGN_RECORD`, `DESIGN_BASELINE`, `DESIGN_VIEW`, `DESIGN_NODES` | conf keys | `.memory-tree.conf` |

Every function name leads with a verb the naming lexicon declares, checked with
`tools/lexicon/lexicon.py --suggest` at writing time. `DesignRefusal` is a Pascal type with no
banned suffix.

### Rollout

The keys land set, so `design_lib.py` is readable from this unit's commit. Nothing reads it until
`TOOL-dTrueNorth-2` lands, so this unit changes no gate's verdict on its own. Behind a blank key an
adopter's tree reads nothing.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`
- `.memory-tree.conf`

### Alternatives rejected

- **The parser inside `tools/check-spec-tokens.py`.** That checker ships to no adopter and sits
  outside the memory-tree kit, while `gen_build_index.py` and the hygiene engine, which read the
  view through `TOOL-dTrueNorth-3`, are kit engines. A kit engine importing a repo-root tool for its
  grammar would put the kit's parse outside the kit.
- **The parser inside `tree_lib.py`.** Every engine of the kit imports that module on start, and
  only four readers need the design.
- **Reading clauses from v2's `[chain]`, as the instrument does.** It would freeze each clause at the
  baseline, so a deviation's `amends` row could never move a pin, which is S2 of the brief.

## 5. Production-readiness checklist

- security — no write path. The one new execution surface is the deriver: a tracked `.py` file a
  tracked conf names, loaded only when the key is set, the same trust as the checker that loads it.
  An untracked or non-`.py` value is refused before any import.
- perf / scale — the view parse is one 517-line read; the deriver's `derive()` took 0.5 s in a
  `carries.py --report` run this pass timed (PINNED, 2026-10-21). One `git show` reads the record at
  the baseline.
- error / empty / loading states — a blank key, an unreadable file, an empty view, a repeated id, a
  baseline naming no object and an unclosed fence each refuse with their name; none reads as an
  empty design.
- observability — `--design` prints the counts it read; every refusal names its key, path or line.
- risks — the deriver is an instrument the product depends on until dIndexedDesign's index lands;
  an edit to it moves the node population with no pin. The instrument `carries.py` reads the same
  deriver, so the two cannot disagree while both run.
- testing — AC1 to AC11 as probes of the module over scratch fixtures and the real tree; the arms
  under §7 land with `TOOL-dTrueNorth-2`, whose join is this parser's first gated caller.
- migration — none. No spec today carries a binding line.
- user docs — the module docstring and the conf comment block; no page under `help/` covers the
  memory tree's spec grammar, and the `TEMPLATE-SPEC.md` section is a named follow-up (§3).

## 6. Acceptance criteria

Every command below runs from the repository root, the module as python tools/memory-tree/design_lib.py.
The criteria spell it by its bare name, `design_lib.py`, because the file is this unit's to create
and the spec-token checker grades a path-shaped token in a criterion against the tracked set.

- **AC1** — When `design_lib.py --parse` reads a scratch spec whose only
  binding is `**Carries:** cl-dClosedLoop-0001@83b6b11 whole` (seven hex digits) at column 0, it
  exits 1 and its output names the file, line 1 and the `**Carries:**` grammar. With the digit
  restored it exits 0 and prints the carry as whole at `83b6b117`.
  Red when: a line failing `CARRY` is skipped silently, as `carries.py:232` skips it.
  fixture: a scratch file the pass writes under the run's scratchpad; none is tracked.
- **AC2** — When `--parse` reads a scratch spec holding, each at column 0, a malformed `part 3/2`
  carry, a `**Moved:**` line with no `to <build>`, a `**Retired:**` line with one, and a
  `**Derived:**` line naming `none`, it exits 1 and names all four `path:line` pairs in one run.
  Red when: the parser stops at the first malformed line, or accepts the instrument's optional `to`.
- **AC3** — When `--parse` reads a scratch spec carrying one line of each well-formed kind, a whole
  carry, a `part 1/2` carry, `node:record-kind.deviation`, a `**Derived:** PLAY-dClosedLoop-2`
  line and one each of moved, retired and deferred, it exits 0 and prints seven bindings with the
  fields §4's data model names.
  Red when: any well-formed kind is refused or printed with a missing field.
  A probe calling `parse_binding_lines` with `strict=False` on this file with AC1's malformed line
  appended returns the same seven bindings and raises nothing.
- **AC4** — When `--parse` reads a scratch spec whose malformed `**Carries:**` line sits inside a
  fenced block, it exits 0 and prints no binding; the same file with the fence left open exits 1
  naming the fence's line.
  Red when: a fenced line is parsed as a binding, or an unclosed fence hides the lines after it.
- **AC5** — When `design_lib.py --design` runs over the tree, it prints
  509 clauses across 22 builds, and a probe comparing each row's `derive_clause_hash` with the hash
  `carries.py`'s `design()` computes from v2 finds no difference.
  Red when: the hash is taken with the id still on, or without folding whitespace.
  figure: the counts are DERIVED at observation from the view; 509 and 22 are today's.
- **AC6** — When `--design --build dTrueNorth` runs, it prints `cl-dClosedLoop-0001` to
  `cl-dClosedLoop-0006` with the hashes the packet's Items list gives (`83b6b117` to `06ceb3cc`),
  each `since` as `baseline`. A scratch copy of the view with one row's id repeated, given to
  `read_design_view`, raises `DesignRefusal` naming the id.
  Red when: a repeated id is read twice, or the build filter returns another build's rows.
- **AC7** — When a probe calls `read_retired_ids` on a scratch git repository whose record lists
  `cl-dProbe-0002` after `Retired:` in its `[clause-ids]` section at the baseline commit, and lists
  none in its working tree, it returns that one id; over the real tree it returns the empty set; with
  a baseline that names no object it raises `DesignRefusal`.
  Red when: the working-tree record is read in place of the baseline blob.
  fixture: a scratch repository under `%TEMP%`, short-named, as the run's rule for clones requires.
- **AC8** — When `--design --build dTrueNorth` runs, its owned nodes read `record-kind.deviation`,
  and a probe finds `read_owned_nodes`'s set for every chain build equal to `carries.py`'s `design()`
  nodes. With `DESIGN_NODES` naming an untracked scratch file, `read_design` raises naming the key.
  Red when: the module restates `OWNED` and drifts from the deriver's, or loads an untracked file.
  figure: today's total is 524 nodes, DERIVED at observation.
- **AC9** — When `design_lib.py --chain-specs 2026-10-21` runs over a
  scratch clone holding one planted spec under a non-chain build and one chain-build spec dated
  2026-10-20, it lists dTrueNorth's specs only and counts the two planted files under `other-build`
  and `pre-cutoff`.
  Red when: a non-chain or pre-cutoff spec is listed, or a skipped file goes uncounted.
  fixture: a scratch clone under `%TEMP%`.
- **AC10** — When `grep -nE '^(SPEC_CARRIES_CUTOFF|DESIGN_RECORD|DESIGN_BASELINE|DESIGN_VIEW|DESIGN_NODES)=' .memory-tree.conf`
  runs, it prints the five keys with the values S1 names, and a probe calling `read_cutoff_key` from
  `tools/check-spec-tokens.py` on the key returns `2026-10-21`. The kit's example conf,
  `tools/memory-tree/.memory-tree.conf.example`, holds no line naming a `DESIGN_` key.
  Red when: a key is missing, misspelt or carries a value `read_cutoff_key` refuses.
- **AC11** — When `--design` runs in a scratch clone whose conf leaves `DESIGN_VIEW` blank, it exits 2
  and names the key; with all four keys blank it exits 2 and says nothing was read.
  Red when: a blank key reads as an empty design and exits 0.

## 7. Gates

`lexicon naming predicates` · `kit/dogfood doc parity` · `recall floor` · `straggler-guard arms` · `transition-audit arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No suite arm lands with this unit: nothing gated calls the parser until `TOOL-dTrueNorth-2`'s join,
whose own `New arm:` line carries the malformed-line case into `tools/check-spec-tokens.test.sh`.
AC1 to AC11 are the probes the close reads for this unit.

## 8. Open questions

- **FACT-QUESTION · F1 — Is `DRAFT`, the status the spec brief names, a legal spec status?** Probe:
  `grep -n 'OPEN · SPECCED' memory/HYGIENE.md` prints the seven tokens a spec header reuses
  (HYGIENE.md line 105). Liveness: the line would print `DRAFT` if the vocabulary declared it.
  Observed: it does not, so a `DRAFT` header fails check 12. RESOLVED (agent, 2026-10-21,
  delegated): `OPEN`, which TEMPLATE-SPEC gives as "drafting".
- **F2 — Where does the product read each chain build's owned nodes?** The brief's interfaces name
  the view, the record and the baseline (S2) and no node source, while `TOOL-dTrueNorth-2`'s node
  plant and `TOOL-dTrueNorth-3`'s "owned nodes no carrier names" both need one. (a) A fifth key,
  `DESIGN_NODES`, naming the deriver `carries.py` already reads, loaded by path. (b) Each chain
  build's packet, whose Owned nodes section `packet.py` renders from that same deriver. (c) No node
  source, the node fields reading "not read". (c) fails the node plant and clause 0003's field, so
  veto 1 discards it. (b) adds a hop and a second grammar, a generated markdown section, over the
  same source. Recommendation (a): it reads the instrument's own source, so the two agree by
  construction, and it is additive to the brief's three keys, which keep their spelling. Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a).
- **F3 — Is the hash function spelled `clause_hash`, as the brief's S3 writes it?** The naming
  lexicon refuses a Python function whose name leads with no declared verb, and
  `tools/lexicon/lexicon.py --suggest clause_hash --as py.function` refuses it as unscoped.
  (a) `derive_clause_hash`, the semantics of `carries.py:85-87` unchanged. (b) `clause_hash` with a
  verb waiver row. Recommendation (a): the brief names the semantics a reader shares, the lexicon
  names the function, and a waiver for a new name is the shrink-only registry growing. Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft.
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to each unit the round-1 spec audit
  promoted against this one, TOOL-dTrueNorth-16, the mirror of its consumes-from; no other section
  moves.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "parse a spec's binding lines naming the design
clause it carries"` ranked `tree_lib.parse_conf` and `parse_spec_h1`
(`tools/memory-tree/tree_lib.py`) as the nearest seams, and nothing that parses a design clause or a
binding line. The seam this unit extends is `tree_lib.py`: its conf parser and fence reader are
reused, and the new module sits beside it as `tools/memory-tree/design_lib.py` rather than inside it,
because only four readers need the design. The grammars are the instrument's, `carries.py:50-56`,
`:85-87` and `asbuilt.py:33`, lifted rather than re-invented. The recall query's hits were the
instruments, the packet and the brief; no hit named a product parser, and none disagreed with source
on the lines cited in §4.

Recall terms used: `python tools/memory-recall/query.py "where is a design clause id and its text
hash parsed for a spec" --terms "clause ids carries binding line spec cutoff conf key parser hash
design record view"`
