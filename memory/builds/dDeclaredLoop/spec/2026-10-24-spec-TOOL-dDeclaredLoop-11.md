# TOOL-dDeclaredLoop-11 — every checklist item named by a semantic tag, its number only display order

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 9 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0096@18103ca9 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |

<!-- /gen:spec-records -->

## 1. Goal

Every checklist item is named by a semantic tag in the `item` namespace, and no reader addresses one
by its number (P11, v2:1833). The flow's step items already carry tags, `item.<step>.<name>`, declared
by `TOOL-dDeclaredLoop-12` and checked by `TOOL-dDeclaredLoop-9`. What remains is the unattended
driver's two handle registries, the seams the instruction layer names for this
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:432-435`):
`DOD_CORE`'s Definition-of-Done items (`tools/unattended/unattended.sh:868`) and `DIRECTIVES_CORE`'s
method directives (:1042). This unit maps each handle onto the declared item whose witness it reads,
in the loop definition, and checks the map both ways against the registries.

## 2. Scope (IN)

- **S1** — `[[checklist]]` rows in `tools/loop/loop.toml`, each `registry` (`DOD_CORE` or
  `DIRECTIVES_CORE`), `handle` and `item`, and no other key, read by `read_checklist_rows` in
  `tools/loop/loop_checklist.py`. A row carrying a number, or any key beyond the three, is refused, so
  an item's position is never stored. Observed by AC1 and AC4.
- **S2** — The thirty rows of §4, one per handle of the two core registries, each mapped onto the
  `[[item]]` row whose witness the handle's check reads. Several handles may map onto one item.
  Observed by AC1.
- **S3** — `check_checklist_rows` and `python tools/loop/loop_checklist.py check`: every core handle,
  parsed from the registry lines of the unattended driver found through `resolve_kit_dir`, has exactly
  one row, and every row's handle is in its registry; every row's `item` resolves through
  `TOOL-dDeclaredLoop-12`'s `read_items` to a declared item. Observed by AC1, AC2 and AC3.
- **S4** — `python tools/loop/loop_checklist.py show <handle>` printing the handle's registry and item
  tag, so a reader who holds a handle reaches its item without a position. Observed by AC5.
- **S5** — The leg `loop checklist tags`, running `check --selftest`, with the rows a new leg owes,
  and a section of `help/loop.md`. Observed by AC6.

## 3. Non-goals (OUT)

- No step item's tag: `TOOL-dDeclaredLoop-12` declares every `[[item]]` row and its tag, and
  `TOOL-dDeclaredLoop-9` checks the fields.
- No retirement of a number, because the measurement found none to retire: every DoD item and every
  directive is addressed by its handle (`verb_attest` matches `"$item:"` at
  `tools/unattended/unattended.sh:12579`, `checker_of` at :1275), and the driver's display order is the
  registry's word order. A retirement with readers would owe a `**Readers:**` clause; this unit names
  none.
- No positional reference: a directive's `M<n>` section field, M3's numbered vetoes read as `veto
  (2|3)` (:12218), the driver's and the hygiene gate's check numbers, and `§n`, `Sn` and `ACn` tokens
  are positional references to a document, which the instruction layer leaves to Convergence's
  inventory (layer-instruction.md:438-441), the clause `cl-dClosedLoop-0476` of dConvergedCharter.
- No adopter handle: a `DOD_EXTRA` or `DIRECTIVES_EXTRA` member names an adopter's item, which the
  overlay's item rows map (`TOOL-dDeclaredLoop-24`).
- No change to the driver's registries, their grammar or their suites. The unattended kit's own
  self-test suites are waived for this build's landing (README rule 8), and this unit's checks read
  the registries without editing them.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-9` — `item.<step>.<name>`, each item declared under its semantic tag, onto which the checklist items are mapped
- **hands-off** external — every positional reference, to dConvergedCharter's `cl-dClosedLoop-0476`, which migrates the remaining ones to tags

## 4. Design

### Data model

```toml
[[checklist]]
registry = "DOD_CORE"          # DOD_CORE | DIRECTIVES_CORE, the driver constant that holds the handle
handle = "gates-green"         # the handle, exactly as the registry spells it before its first ":"
item = "item.test.verdict"     # the declared item whose witness the handle's check reads
```

The registry lines are read as `check-unattended.sh`'s `core_of` reads them
(`tools/unattended/check-unattended.sh:412-416`): the one line `<NAME>="<members>"` of the driver,
each member split at its first `:`. The driver is found with the canonical-copy block of
`tools/lib/resolve_kit_dir.py`, graded by its existing `resolve_kit_dir` row of `PARITY_ROWS`.

### The map

| Registry | Handle | Item | The item's witness the check reads |
|---|---|---|---|
| `DOD_CORE` | `gates-green` | `item.test.verdict` | the runner's verdict for the tree |
| `DOD_CORE` | `records-current` | `item.deploy.record` | the landing record and the records it carries |
| `DOD_CORE` | `authorization-reachable` | `item.deploy.mandate` | the landing's authority |
| `DOD_CORE` | `landed-via-lander` | `item.deploy.land` | the lander's landing |
| `DOD_CORE` | `build-complete` | `item.build.exit` | the step's exit over every unit |
| `DOD_CORE` | `closing-review-recorded` | `item.build.ratify` | the ratification the closing review precedes |
| `DOD_CORE` | `specs-audited` | `item.design.ready` | READY and the audit's disposition |
| `DOD_CORE` | `pieces-complete` | `item.build.exit` | the step's exit over a recipe run's pieces |
| `DOD_CORE` | `set-checks-recorded` | `item.test.verdict` | a playbook run's set check at the verdict |
| `DOD_CORE` | `keepalive-reaped` | `item.deploy.unlease` | the run's leases and wake closed |
| `DOD_CORE` | `parked-decisions-surfaced` | `item.deploy.record` | the landing record the owner reads |
| `DOD_CORE` | `reuse-probed` | `item.design.seams` | the map and recall probes over the scope |
| `DOD_CORE` | `asks-disposed` | `item.deploy.record` | the asks the landing record carries |
| `DIRECTIVES_CORE` | `minimal-prose` | `item.deploy.record` | the one record a run speaks through |
| `DIRECTIVES_CORE` | `sub-specced` | `item.design.unit-spec` | each unit's spec |
| `DIRECTIVES_CORE` | `forks-resolved` | `item.design.unit-spec` | each spec's resolved forks |
| `DIRECTIVES_CORE` | `specs-reviewed` | `item.design.ready` | the audit's disposition |
| `DIRECTIVES_CORE` | `reuse-first` | `item.design.seams` | the seams found before design |
| `DIRECTIVES_CORE` | `parallel-when-disjoint` | `item.build.unit-pass` | disjoint write sets run in parallel |
| `DIRECTIVES_CORE` | `passes-committed` | `item.build.unit-pass` | each pass's commit |
| `DIRECTIVES_CORE` | `diff-reviewed` | `item.build.ratify` | the closing review before ratification |
| `DIRECTIVES_CORE` | `land-once-done` | `item.deploy.land` | the one landing |
| `DIRECTIVES_CORE` | `conflicts-reconciled` | `item.build.resolve` | the resolution commit |
| `DIRECTIVES_CORE` | `wrap-up-derived` | `item.deploy.record` | the landing record |
| `DIRECTIVES_CORE` | `researched` | `item.design.research` | the answered fact fork |
| `DIRECTIVES_CORE` | `solution-tested` | `item.design.research` | the discriminating test |
| `DIRECTIVES_CORE` | `pieces-recorded` | `item.build.exit` | the recipe run's pieces |
| `DIRECTIVES_CORE` | `playbook-followed` | `item.build.unit-pass` | each pass of a recipe run |
| `DIRECTIVES_CORE` | `discoveries-adopted` | `item.design.decompose` | an adopted discovery decomposed into a unit |
| `DIRECTIVES_CORE` | `passes-harnessed` | `item.build.unit-pass` | the harnessed pass |

The handles are the registries' at base `ed497191`, PINNED by a measurement of
`tools/unattended/unattended.sh:868` and :1042 on 2026-10-24; `check` re-derives the set from the
driver on every run, so a handle added there reds until its row lands. The items are rows of
`TOOL-dDeclaredLoop-12`'s five step programs (flow-steps.md's `[design]`, `[build]`, `[test]` and
`[deploy]` tables).

### The check

`check_checklist_rows(rows, registries, items)` reds: a core handle with no row, a handle with two
rows, a row whose handle its registry lacks, a row whose `registry` is neither constant, a row whose
`item` is not an `item.<step>.<name>` tag or resolves to no declared item, and a row carrying any key
but the three. It prints each registry's count and each row. `--selftest` runs the plants of §6.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/loop_checklist.py` | module | none declared for files |
| `read_checklist_rows` | function | `py.function`, OK |
| `check_checklist_rows` | function | `py.function`, OK |
| `[[checklist]]` | table of `tools/loop/loop.toml` | none |
| `loop checklist tags` | leg | none |

### Migration

None: the registries are read, never rewritten.

### Rollout

Live on landing. A handle added to a registry without a row reds the new leg, which is the point.

### Files touched (estimate)

- `tools/loop/loop.toml`: the thirty `[[checklist]]` rows
- `tools/loop/loop_checklist.py`
- `tools/loop/kit.toml`: the module and the leg declared
- `tools/gate-legs.json`: the leg `loop checklist tags`, argv `python {prefix}/loop/loop_checklist.py check --selftest`
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `tools/run-gates/ceiling-evidence.txt`, the new leg's row
- `memory/map/features/loop.md`: the module's claim and the leg in its `gate-legs` list
- `help/loop.md`: the checklist section

### Alternatives rejected

- **A new tag per handle, `item.<step>.<handle>`.** Thirty tags no `[[item]]` row declares, which
  `TOOL-dDeclaredLoop-18`'s `extract_item` would never read, so the namespace check would not see them.
- **The tag written into the driver's registry, `<handle>:<class>:<item>`.** It widens a grammar
  four readers split by position (`tools/unattended/check-unattended.sh:427-438`) and whose suites
  are waived for this landing, so nothing would observe the change.
- **Renaming M3's vetoes and re-pointing `veto (2|3)`.** A positional reference into a governance
  document, which the instruction layer assigns to Convergence.

## 5. Production-readiness checklist

- security — read-only over tracked files.
- perf / scale — two line reads of the driver and one definition read.
- error / empty / loading states — a driver the resolver cannot find exits 2 naming the kit; an empty
  registry line exits 2, never green over nothing.
- observability — every red names the registry, the handle and the row.
- risks — the map is a judgement per handle of which item's witness its check reads; a wrong pairing
  is caught by review, not by the check, which grades resolution only.
- testing — the plants of §6 under the new leg.
- migration — none.
- user docs — `help/loop.md` (S5).

## 6. Acceptance criteria

- **AC1** — When `python loop_checklist.py check` runs on the built tree, it exits 0 printing 13
  `DOD_CORE` rows and 17 `DIRECTIVES_CORE` rows, `gates-green` beside `item.test.verdict`.
  Red when: a row is read from a table other than the loop definition's, so a row added there is not
  printed.
  figure: 13 and 17 are DERIVED from the driver's two registry lines at the run.
- **AC2** — When `python loop_checklist.py --fixture --plant missing-handle` runs, its driver copy
  carrying a DoD handle `retired-check` no row maps, `check` exits 1 naming it; under
  `--plant stale-row`, a row whose handle no registry holds, it exits 1 naming the row.
  Red when: the map is checked one way only.
- **AC3** — When the fixture runs with `--plant undeclared-item`, a row mapping onto
  `item.deploy.nosuch`, and `--plant bare-item`, one mapping onto `deploy.land`, `check` exits 1
  naming each.
  Red when: a row names an item tag no `[[item]]` row declares and passes.
- **AC4** — When the fixture runs with `--plant numbered-row`, a row carrying `number = 3`, `check`
  exits 1 naming the key `number`.
  Red when: a checklist row stores a position.
- **AC5** — When `python loop_checklist.py show reuse-probed` runs, it prints `DOD_CORE
  item.design.seams`, and `show nosuch` exits 2.
  Red when: `show` resolves a handle by its position in the registry.
- **AC6** — When `grep -n '"loop checklist tags"' tools/gate-legs.json` runs, it finds the leg row and
  its argv naming `loop_checklist.py check`, and `grep -n 'loop_checklist.py show' loop.md` in `help/`
  finds the section.
  Red when: the leg row is absent or names another command, so no bar runs the check.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest`

New arm: tools/loop/loop_checklist.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the `loop checklist tags` leg, its failing case staged by the `missing-handle` plant · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-24: the tuple
  does not hold `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it. RESOLVED (agent,
  2026-10-24, delegated): `OPEN`.
- **FACT-QUESTION · F2 — Does any reader address a DoD item or a directive by its number?** Probe:
  every reader of `DOD_CORE`, `DIRECTIVES_CORE`, `dod()` and `directives()` in
  `tools/unattended/unattended.sh` and `tools/unattended/check-unattended.sh`, read for a positional
  index. Observation, 2026-10-24: each matches a member by its handle (`"$item:"`, `"$h:"`), and the
  only numbers in the members are the directives' `M<n>` section fields. Liveness: a reader indexing
  a member by position, such as a word count used as a key, would show here. RESOLVED (agent,
  2026-10-24, delegated): none, so no number retires in this unit.
- **F3 — Does "BUILD-METHOD's numbered checks", in the brief, include M3's numbered vetoes?** Options:
  (a) tag them and re-point `veto (2|3)` and every carrier citing a veto by number; (b) leave them to
  Convergence. The instruction layer names `DOD_CORE` and `DIRECTIVES_CORE` as this clause's seams and
  puts "the other positional references" in Convergence's inventory (layer-instruction.md:432-441).
  RESOLVED (agent, 2026-10-24, delegated): (b), rung 1, handed to `cl-dClosedLoop-0476`.
- **F4 — Does each handle get its own tag, or map onto a declared item?** Options: (a) map onto the
  declared item whose witness the check reads; (b) mint `item.<step>.<handle>`. (b) mints tags no
  item row declares, outside the namespace's extractor. RESOLVED (agent, 2026-10-24, delegated): (a),
  rung 3, the population `TOOL-dDeclaredLoop-9` hands this unit.

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 11, the instruction layer's checklist
  paragraph and the two registries at base `ed497191`.

## 10. Reuse audit

The seams extended are the two driver registries, read as their gate already reads them
(`core_of`, `tools/unattended/check-unattended.sh:412-416`, verified at base), and
`TOOL-dDeclaredLoop-12`'s `read_items`. The scout's citation of `core_of` at :412-418 is the function
and its first calls; the function body is :412-416. `python tools/codebase-map/reuse_lookup.py "map
checklist handles onto semantic item tags with numbers only display order"` ranked `map_root`,
`check_rule_tags` in `tools/roles/roles_lib.py` and `derive_install_order`, name stems; `check_rule_tags`
joins a role's `rules:` to charter tags, a different join, so no seam fits the map, which is new.
`python tools/memory-recall/query.py "how are definition of done items and directives named and
numbered"` returned the scout row, layer-instruction.md:432-439, the review of the instruction layer
finding `DIRECTIVES_CORE` absent from its subject, and `TOOL-dAlignedCarrier-3`'s scope change to two
directives; none disagrees with source.

Recall terms used: DOD_CORE DIRECTIVES_CORE handle item tag checklist number display order directive section core_of
