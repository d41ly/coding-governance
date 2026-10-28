# TOOL-dIndexedDesign-8 — the feature level: `design.decompose`'s feature designs, roster and fork records, forks resolved as `design.forks` says

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 8 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0390@a096f77c part 1/2
**Carries:** node:item.design.decompose
**Carries:** node:policy-key.design.forks
**Carries:** node:record-kind.feature-design
**Carries:** node:record-kind.fork
**Carries:** node:record-kind.roster

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-c.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-c.md) | research | TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |

<!-- /gen:spec-records -->

## 1. Goal

gap-flow-01 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:107`):
there is no feature level between build and unit, so the interfaces between a feature's units have no
record and re-design has no granularity but the unit. The owner settled build, features, units, each
feature carrying the design of its units' interfaces (flow FL-D4,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md:286-287`, settled at
:267-270 and :306-308), and agents resolving forks by the most feature-rich and expandable option with
a full record, configurable as `design.forks` (FL-D3, :256-259, settled at :275-280; v2 P18 and `[policies]`,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:906-912`, :1146).
This unit is `design.decompose` (flow-steps:238): the feature design records with each interface
declared structurally, the roster as a record kind, every raised fork joined to its fork record, and
the join refusing a resolution `design.forks` does not admit.

It carries cl-dClosedLoop-0390 in part 1 of 2 (§8 F1). Part 2, the two-level re-entry by
`design.reentry` with its additive-versus-breaking classification by the `diff` record, `design.input`
and the re-design inventory of gap-flow-25, is TOOL-dIndexedDesign-20; it reads this unit's
structured interface fields through `read_feature_designs`.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: the record-kind factory `record_kinds.py
new` and `tools/memory-tree/record-kinds.toml` (TOOL-dTotalRecall-1 S1, S9); the `[[item]]` and
`[[stand-in]]` rows of `tools/loop/loop.toml` (TOOL-dDeclaredLoop-12 S2, -13 S8) and the item factory
(TOOL-dDeclaredLoop-24); `read_spec_section` and the tag `section.open-questions` (TOOL-dIndexedDesign-9,
I1); `read_spec_edge_lines` (TOOL-dIndexedDesign-12, I2); `read_design_policy` (TOOL-dIndexedDesign-16,
I3); the `spec` row's `sections` column and the `### Interfaces` sub-head (TOOL-dIndexedDesign-7, I8, its
S4).

Shared files the build run sequences, this unit first at order 8: `tools/loop/loop.toml`, where S11
arms `item.design.decompose`'s row, TOOL-dIndexedDesign-13 S6 adds an `upstream` entry to that same row
and TOOL-dIndexedDesign-20 S10 arms the `input`, `reentry` and `inventory` rows;
`tools/memory-tree/design_lib.py`, whose `read_feature_designs` TOOL-dIndexedDesign-20 S1 widens with a
revision argument; and `tools/memory-tree/BUILD-METHOD.template.md` M2, where S12 and
TOOL-dIndexedDesign-20 S12 each add a sentence.

- **S1** — The feature design record, kind `feature-design`, tag `record.feature-design`, registered by
  `python record_kinds.py new feature-design --tag record.feature-design --writer hand --check "memory
  hygiene" --field Feature --field Units --field Interface --field Boundary` (I15). Home
  `memory/builds/<slug>/build/<date>-build-<first unit id>-feature-<seg>.md`, bound `**Serves:**
  feature-design <unit ids>`, its fields one per line: `- **Feature:** feature.<seg>`; `- **Units:**`
  the feature's unit ids; one `- **Interface:** <name> · producer <unit id> · consumers <unit id>[,
  <unit id>] · contract <token>` per interface; one `- **Boundary:** <path>` per path the feature may
  write, or none. Observed by AC1.
- **S2** — The one reader, `read_feature_designs(root, slug)` in `tools/memory-tree/design_lib.py`:
  `{feature: {"path", "units", "interfaces": [(name, producer, consumers, contract)], "boundaries"}}`
  over the build's records bound `feature-design`, read through `tree_lib.read_bindings`. A record
  naming one feature twice, or two records naming one feature, is a refusal naming both.
  TOOL-dIndexedDesign-20's structural diff reads these fields and no other. Observed by AC1 and AC2.
- **S3** — Membership. A unit joins its feature by `**Edges:** implements=feature.<seg>` in its spec,
  read only through `read_spec_edge_lines(text)` (I2, I9). Observed by AC2.
- **S4** — The roster kind: `python record_kinds.py new roster --tag record.roster --writer hand
  --check "memory hygiene"`, its home the build README's `<!-- roster:units -->` region, which M2
  already names as the roster (`memory/guides/BUILD-METHOD.md:39-42`). No column of that table changes,
  so `read_roster_at` and the packet renderer read it as they do. Observed by AC8.
- **S5** — The interface schema check, `check_feature_designs(root, slug)` in `design_lib.py`, the
  decompose item's witness. Findings, each naming the record or spec and the token: (a) a record's unit
  not on the roster; (b) an `implements=feature.<seg>` no record designs; (c) a record's unit whose spec
  does not declare `implements=` for that feature; (d) an interface whose producer or a consumer is not
  one of the feature's units; (e) a §3 `**hands-off**` bullet, or a `### Interfaces` row of the Design
  section (TOOL-dIndexedDesign-7 S4, read through `read_spec_section(text, "section.design")`), between
  two units of one feature that backticks neither the name nor the contract of an interface the feature
  declares; (f) a unit's
  declared write path, by `read_spec_writes` and `check_writes_intersect`, outside every `Boundary` of a
  feature that declares one. A build with no `feature-design` record is graded by nothing and says so.
  Observed by AC2 and AC3.
- **S6** — The fork record, kind `fork`, tag `record.fork`, registered by `python record_kinds.py new
  fork --tag record.fork --writer hand --check "memory hygiene" --field Fork --field Level --field Class
  --field Resolver --field Options --field Pick`. Home
  `memory/builds/<slug>/build/<date>-build-<unit id>-fork-<n>.md`, `<n>` the F-item's number, bound
  `**Serves:** fork <unit id>`; fields `- **Fork:** F<n>`; `- **Level:** unit|feature`; `- **Class:**
  fact|preference|goal`; `- **Resolver:** agent|owner`; `- **Options:**` the admitted options in
  rank order, joined by ` > `; `- **Pick:**` one of them. Its id is `<unit id>#F<n>`. Observed by AC4.
- **S7** — The F-item reader, `read_fork_items(text)` in `design_lib.py`: the body of
  `section.open-questions` through `read_spec_section`, split by the F-item opener the template states
  (`memory/TEMPLATE-SPEC.md:354-357`), each item's `F<n>`, its `FACT-QUESTION` flag, and its mark's
  resolver and date by the documented shape, or none. It is the Python twin of check 12's F-item arm
  (`tools/memory-tree/check-memory-hygiene.sh:2426-2441`) and `plan_state` (`tools/unattended/unattended.sh:4458`),
  held in agreement by a case table, never an import (`unattended.sh:4435-4437`). Observed by AC5.
- **S8** — The fork join, `check_fork_records(root, slug, forks)`, over every spec of the build dated on
  or after `SPEC_FORK_RECORD_CUTOFF`: each resolved F-item has a fork record for that unit and `F<n>`
  whose `Resolver` equals the mark's; each fork record has its F-item; and the mark's resolver is one
  the `forks` value admits for the record's `Class`, as §4 "The forks rule" states. Observed by AC4 and
  AC6.
- **S9** — The key. The CLI reads `design.forks` once, by the literal call
  `read_design_policy("design.forks", root)` (I3), and hands its value to `check_fork_records`. The
  catalogue row (`tools/policy/catalogue.toml:41-44`, owner dIndexedDesign) gains its `summary` and a
  `usage` line, `design.forks = "preference-forks-park"`, and the name leaves
  `tools/policy/unsummarised-keys.txt` (:54) through `python policy.py lists --write`; no second row is
  added. Observed by AC6 and AC7.
- **S10** — The CLI and its wiring. `python design_lib.py --decompose [<slug>]` runs S5 and S8 over one
  build or every build, printing `design-lib: decompose <check> <path> — <detail>` per finding and one
  population line naming what it graded and what it does not check; exit 1 on a finding, 0 on none, 2
  on a record it could not read or a key it could not resolve. Check 12 runs it after its §3 edge
  joins when `SPEC_FORK_RECORD_CUTOFF` is set, a non-zero exit failing 12, held under
  `--staged` as the edge joins are. `--decompose-fixture <dir> --plant <case>` writes a scratch
  repository for each case of §6. Observed by AC2 to AC6.
- **S11** — The item goes live. `item.design.decompose`'s `[[stand-in]]` row leaves
  `tools/loop/loop.toml`, and its row's `witness` names `design_lib.py --decompose` and its `returns`
  `record-kind.feature-design`; its needs, outcomes and routes stay as TOOL-dDeclaredLoop-12 transcribed
  them. Observed by AC8.
- **S12** — The keys and the prose. `SPEC_FORK_RECORD_CUTOFF` joins the defaults block of
  `check-memory-hygiene.sh`, `tools/memory-tree/.memory-tree.conf.example`, blank, and
  `.memory-tree.conf`, set strictly ahead of the corpus. `tools/memory-tree/SPEC-TEMPLATE.template.md`'s
  §8 skeleton paragraph and FORK_ITEM_CUTOFF section gain one paragraph each: a resolved F-item owes a
  fork record from the cutoff, and `design.forks` decides which resolver is admitted;
  `tools/memory-tree/BUILD-METHOD.template.md` M2 names the feature design record as the overview's
  interface home. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` re-render. Observed by AC9.

## 3. Non-goals (OUT)

- Part 2 of the clause: `design.reentry`, `item.design.reentry`, `item.design.input`,
  `item.design.inventory`, the `diff` and `inventory` kinds and the additive-versus-breaking classifier
  (PLAY-dOrderedCharter-36 S5 is its nearest seam): TOOL-dIndexedDesign-20 (§8 F1).
- Writing a door for these records: their writer is `hand`, the class TOOL-dTotalRecall-2 replaces
  with doors; this unit adds none.
- Changing `plan_state`'s FORKED reading or its one-token contract: a mark the key refuses fails the
  join, and the spec writer then parks the fork, which `plan_state` already reads as FORKED.
- The feature transition table and its states: TOOL-dDeclaredLoop-13 S4 owns F1 to F6.
- Grading any landed spec: the fork join starts at its cutoff; the feature checks grade only a build
  that writes a feature design record.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-9` — `read_spec_section` and the tag `section.open-questions`, the body `read_fork_items` splits; without it S7 holds a second section walk
- **consumes-from** `TOOL-dIndexedDesign-12` — `read_spec_edge_lines`, the one reader of `**Edges:** implements=feature.<seg>`, the membership S3 and S5 join on
- **consumes-from** `TOOL-dIndexedDesign-16` — `read_design_policy`, the one reader S9 calls for `design.forks`; without it the join has no value to grade a mark against
- **consumes-from** `TOOL-dIndexedDesign-7` — `record-kind.spec`, the `spec` row whose `sections` column S5 reads a unit's declared sections through, beside which S1, S4 and S6 register their rows, and its `### Interfaces` sub-head, each unit's half of a feature's interfaces that S5's arm (e) joins
- **hands-off** `TOOL-dIndexedDesign-20` — `read_feature_designs` and the `Interface` fields its structural diff classifies `additive` or `breaking`, part 2/2 of cl-dClosedLoop-0390

## 4. Design

### Evidence

- No feature level exists: `parse_spec_text` reads `order`, `writes` and `consumes`
  (`tools/memory-tree/gen_build_index.py:544-551`), and the only unit-to-unit interface record is the
  §3 edge bullet (`design_lib.read_spec_edges`, `tools/memory-tree/design_lib.py:543`).
- The fork rule is prose (M3, `memory/guides/BUILD-METHOD.md:86-97`); two awk readers grade the mark
  (check 12's arm and `plan_state`), and no Python reader of an F-item exists:
  `tools/runlog/model.py:1439-1453` reads marks section-wide under `## 8.`, in another kit.
- `design.forks` has its catalogue row and no reader (`tools/policy/catalogue.toml:41-44`,
  `tools/policy/unsummarised-keys.txt:54`).
- TOOL-dDeclaredLoop-12 S2 transcribes every `design.*` item from flow-steps, owner dIndexedDesign, and
  -13 S8 holds a `[[stand-in]]` row for each while its owning build has not landed.
- TOOL-dTotalRecall-19 already writes `**Edges:** implements=feature.record-door` under a heading
  (`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-19.md:183-188`).

### A feature design record

```markdown
# Feature design — feature.record-door

**Serves:** feature-design TOOL-tFix-1 TOOL-tFix-2

- **Feature:** feature.record-door
- **Units:** TOOL-tFix-1 TOOL-tFix-2
- **Interface:** record door · producer TOOL-tFix-1 · consumers TOOL-tFix-2 · contract `open_record`
- **Boundary:** tools/fix/
```

### The forks rule

| `design.forks` | `agent` mark admitted for | `owner` mark admitted for |
|---|---|---|
| `agents-feature-rich-expandable` | every class | every class |
| `preference-forks-park` | `fact` and `goal` | every class |
| `owner-decides-all` | none | every class |

A `goal` fork under the default is the agent's, through a plan revision under the mandate (P18; FR-12),
so the default admits it. A refused mark is a finding naming the unit, `F<n>`, the class and the
value; the remedy is the owner's mark or a park, which leaves the fork open.

### What it does not check

Whether an interface's contract means what both units think; whether the options are the real ones or
ranked well; a fork nobody declared; and a build that writes no feature design record.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_feature_designs`, `check_feature_designs`, `read_fork_items`, `check_fork_records` | functions in `design_lib.py` | `py.function`, asked at the pass |
| `--decompose`, `--decompose-fixture` | flags of `design_lib.py` | `cli.flag`, asked at the pass |
| `feature-design`, `fork`, `roster` | record kinds, rows of `record-kinds.toml` | none |
| `Feature`, `Units`, `Interface`, `Boundary`, `Fork`, `Level`, `Class`, `Resolver`, `Options`, `Pick` | record fields | none |
| `SPEC_FORK_RECORD_CUTOFF` | conf key | none |
| `feature.<seg>` | id namespace, dTotalRecall's | none |

### Migration

None: no feature design record exists, and the fork join starts at a cutoff ahead of the corpus.

### Rollout

Live at landing. The decompose item's stand-in leaves in the same commit as its witness lands.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S2, S5, S7, S8, S9, S10
- `tools/memory-tree/record-kinds.toml`: S1, S4, S6, written by the factory
- `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`: S7, S10, S12
- `tools/memory-tree/.memory-tree.conf.example`, `.memory-tree.conf`: S12
- `tools/memory-tree/SPEC-TEMPLATE.template.md`, render `memory/TEMPLATE-SPEC.md`: S12
- `tools/memory-tree/BUILD-METHOD.template.md`, render `memory/guides/BUILD-METHOD.md`: S12
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`, `.governance/policy.json`: S9
- `tools/loop/loop.toml`: S11

### Alternatives rejected

- **The clause whole in one unit** — lost to M2's one-mechanism test: the re-entry classifier is a
  generated `diff` record and a different item, read at a different moment, so one pass could not be
  reviewed per mechanism · `memory/guides/BUILD-METHOD.md:34-37`
- **Feature membership as a roster column** — lost to the readers of the authored roster:
  `read_roster_at` and the packet renderer parse its four columns, and a fifth would be a change in
  every chain README; the spec-site edge is one line per unit · `memory/builds/dIndexedDesign/README.md:58`
- **The fork record inside §8** — lost to the record-kind rule: §8 already carries the mark two readers
  grade; a second grammar there would be a third reader's shape, while a typed record is graded by its
  kind's row · `memory/TEMPLATE-SPEC.md:348-372`
- **Reading `design.forks` in `plan_state`'s awk** — lost to I4: the one-token contract two harnesses
  slice stays unchanged, and the join already turns a refused mark into a fork left open ·
  `tools/unattended/unattended.sh:4458`

## 5. Production-readiness checklist

- security — reads tracked records and specs; the policy value comes from the policy kit's own reader
  by subprocess, never parsed here.
- perf / scale — one pass over a build's records and specs; empty at landing.
- error / empty / loading states — exit 2 naming an unreadable record or an unresolved key; a build with
  no feature record says so.
- observability — every finding names its check, path and token; the population line names what is
  not checked.
- risks — a spec writer may meet a refused mark at commit under a non-default value; the finding names
  the remedy.
- testing — each check's plant red and its clean twin green, each `design.forks` value planted, the
  F-item case table.
- migration — none.
- user docs — the spec template's §8 paragraphs and M2's sentence; `help/policy.md` lists keys from
  the catalogue, whose row gains its summary.

## 6. Acceptance criteria

- **AC1** — When `python design_lib.py --decompose-fixture <dir> --plant feature` runs and `python -c`
  calls `read_feature_designs` on its build `tFix`, it returns `feature.record-door` with its two units,
  its one interface `record door` with producer, consumers and contract `open_record`, and its boundary.
  Red when: a field is dropped, or a second record naming the feature is not a refusal.
- **AC2** — When `python design_lib.py --decompose tFix` runs in that fixture, it exits 0; under
  `--plant unknown-unit` it exits 1 naming the record and the unit not on the roster, and under `--plant
  undesigned` it exits 1 naming the spec whose `implements=feature.ghost` no record designs.
  Red when: either plant exits 0, or the clean fixture prints a finding.
- **AC3** — When `design_lib.py --decompose tFix` runs over `--plant undeclared-interface`, whose
  producer hands off `close_record` to its feature sibling, it exits 1 naming the bullet and
  `close_record`; over `--plant undeclared-interface-row`, whose consumer's `### Interfaces` row takes
  `close_record` from its feature sibling, it exits 1 naming the row; over `--plant boundary`, whose unit
  writes outside the feature's boundary, it exits 1 naming the path.
  Red when: an edge between two units of one feature names no declared interface and passes.
- **AC4** — When `design_lib.py --decompose tFix` runs over `--plant fork-unrecorded`, a spec dated at
  the cutoff whose `F1` carries an agent mark and no fork record, it exits 1 naming the unit and `F1`;
  with the fork record written, it exits 0; with the record's `Resolver` reading `owner`, it exits 1
  naming the disagreement.
  Red when: a resolved F-item with no record passes, or a resolver mismatch passes.
- **AC5** — When `python -c` runs `read_fork_items` over each case of the F-item table check 12's suite
  holds, every case returns the verdict check 12's arm gives: the two opener spellings, an option bullet
  inside a span, a quoted mark, a wrapped mark and the `FACT-QUESTION · ` prefix.
  Red when: a case's Python verdict and awk verdict differ.
- **AC6** — When `design_lib.py --decompose tFix` runs over `--plant fork-classes`, a `preference` and a
  `fact` fork each resolved by an agent mark with its record, it exits 0 with no policy file; with a
  planted `.governance/policy.toml` setting `design.forks = "preference-forks-park"` it exits 1 naming
  only the `preference` fork; with `design.forks = "owner-decides-all"` it exits 1 naming both, and the
  same plant with both marks `owner` exits 0.
  Red when: a value admits a mark the forks rule refuses, or refuses one it admits.
- **AC7** — When `python policy.py get design.forks` runs with no policy file it prints
  `agents-feature-rich-expandable`, after `python policy.py lists --write` the unsummarised list no
  longer names `design.forks`, and `grep -n 'read_design_policy("design.forks"' design_lib.py` finds
  the literal reader.
  Red when: the row stays unsummarised or no literal call reads the key.
- **AC8** — When `python -c` loads `record-kinds.toml` and `loop.toml` with `tomllib`, the first holds
  rows `feature-design`, `fork` and `roster` with tags `record.feature-design`, `record.fork` and
  `record.roster`, and the second holds no `[[stand-in]]` row for `item.design.decompose` while its
  item row's `witness` names `--decompose`.
  Red when: a row is missing, or the stand-in survives the witness.
- **AC9** — When `grep -n "SPEC_FORK_RECORD_CUTOFF" TEMPLATE-SPEC.md .memory-tree.conf.example` runs
  over the render and the kit's example conf, both name the key, and `grep -n "feature design"
  BUILD-METHOD.md` finds M2's sentence.
  Red when: a render or the example conf omits it.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `policy check` · `policy fixtures` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC3 AC4 AC5 AC6 · each decompose plant red under check 12 and its clean twin green, the three `design.forks` values planted, and the F-item case table run through both readers, staged by dropping the fork record · none

## 8. Open questions

- **F1 — Is cl-dClosedLoop-0390 one mechanism?** Options: (a) one unit carrying it whole; (b) two
  parts, decompose (feature designs, roster, fork records, `design.forks`) and re-entry (`design.input`,
  `design.reentry`, the `diff` and `inventory` records); (c) four parts, one per record family. (a)
  fails M2: the diff record is a generated artifact read at a different item. (c) splits
  `design.decompose`'s one witness, which flow-steps:238 states as the roster and interface schema check
  with every feature fork joined to its fork record, across units. RESOLVED (agent, 2026-10-28,
  delegated): (b), rung 3, the most feature-rich survivor of M2: this unit carries part 1/2 and owns
  `item.design.decompose`, `policy-key.design.forks` and the kinds `feature-design`, `fork` and
  `roster`; part 2/2 owns `item.design.input`, `item.design.reentry`, `item.design.inventory`,
  `policy-key.design.reentry` and the kinds `diff` and `inventory`, and carries the token
  `design.reentry`. widens: none · relaxes: none
- **F2 — How does a unit name its feature?** Options: (a) `**Edges:** implements=feature.<seg>` in the
  spec, I2's grammar; (b) a roster column; (c) the feature record alone listing units. (b) breaks the
  authored roster's readers; (c) is one fact the unit cannot see from its own spec. RESOLVED (agent,
  2026-10-28, delegated): (a) with (c)'s `Units` field joined to it both ways (S5 checks b and c), rung
  3.
  grants: PLAY-dClosedLoop-3 the `**Edges:**` line carries feature membership. widens: none · relaxes: none
- **F3 — Where does the fork join run?** Options: (a) check 12, through `design_lib.py --decompose`,
  behind its own cutoff; (b) the Design exit only, through `check_design_exit` (I5); (c) `plan_state`.
  (b) meets a refused mark only at the hand-off, after the spec run committed it; (c) breaks I4.
  RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, the format check flow-steps:243 names for
  `design.unit-spec`; `--dispatch` meets the open fork through `plan_state` as it does today.
  grants: PLAY-dClosedLoop-3 check 12 gains the decompose call. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 8, gap-flow-01, flow FL-D2 to FL-D6,
  flow-steps:235-243, v2 P17, P18 and its `[policies]` row, scout C's row for this unit, and the parent
  rows of TOOL-dDeclaredLoop-12, -13, -24 and TOOL-dTotalRecall-1; part 1 of 2 by §8 F1.

## 10. Reuse audit

The seams extended are `read_spec_edges`, `read_spec_writes` and `check_writes_intersect`
(`tools/memory-tree/design_lib.py:543`, :528, :601), `tree_lib.read_bindings` for the records, the
record-kind factory (TOOL-dTotalRecall-1 S9), the item rows and stand-ins (TOOL-dDeclaredLoop-12 S2,
-13 S8), and check 12's F-item grammar, twinned by a case table rather than imported; each line
verified at `4bf0f400d`. Scout C cited `design_lib.py:543`, :528 and :601 and `catalogue.toml:41`, :47
correctly at that commit. `python tools/codebase-map/reuse_lookup.py "declare a feature's interfaces
between its units and join each resolved fork to a record"` ranked name stems (`resolve`, `records`,
`units`, `resolve_kit_dir`, `declares`); none declares an interface or joins a fork, and scout C's
second probe found only `govkit` `classify_row` and `census.classify`, which classify unrelated rows,
so no existing seam fits the feature record or the fork join and S2, S5, S7 and S8 add them beside the
readers they call. PLAY-dOrderedCharter-36 S5's widening classifier is part 2's seam, not this unit's.

Recall terms used: `python tools/memory-recall/query.py "how does design decompose a build into features with declared interfaces and resolve forks by policy" --terms "feature level feature design interfaces producer consumers contract decompose fork record design.forks roster"`
