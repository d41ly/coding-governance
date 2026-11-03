# TOOL-dCalibratedLens-5 — instruction effectiveness from returns and findings that cite unit tags, and the Loop Review's proposals under `review.loop.retire`, with the keep record

**Status:** DEFERRED · rev-4 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 11 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0462@cad135ef whole
**Carries:** node:item.loop.propose
**Carries:** node:policy-key.review.loop.retire

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-5-deviation-51.md](../build/2026-11-02-build-TOOL-dCalibratedLens-5-deviation-51.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-5-deviation-52.md](../build/2026-11-03-build-TOOL-dCalibratedLens-5-deviation-52.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-5-deviation-53.md](../build/2026-11-03-build-TOOL-dCalibratedLens-5-deviation-53.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-5-deviation-54.md](../build/2026-11-03-build-TOOL-dCalibratedLens-5-deviation-54.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-29 |
| [2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-14 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing records which instruction units an agent loaded, followed or broke, so text that bears no load
is never found (gap-found-16), and the Loop Review has no step that turns a reading into a proposal
(gap-review-02, gap-maint-03 in part). This unit makes a role agent's return and a review finding cite
unit tags, measures each unit's load and breakage from those citations, and lands the Loop Review's
`propose` step: retiring a priced row that caught nothing, pruning a unit that bears no load, tightening
a unit broken often, each as `review.loop.retire` says (`propose-ratify`, `demote-then-propose`,
`report`), and proposing a charter amendment for a rule whose override records recur, so a standing
override becomes an amendment rather than a habit (foundations, step 1, the owner's FK-11-1). An owner's
keep is a record of its own, which the next proposal honours until it lapses (layer-expansions:212,
:262-263).

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`, re-grounded by the build run, which
stops this unit when one is absent: TOOL-dCalibratedLens-2 (`derive_ledger_rows`, `derive_row_state`,
`read_record_fields`, the snapshot, the `item.loop.price` row) and TOOL-dCalibratedLens-3 (`METRICS`, the
walk, `run_loop_file` and its proposal shape, the record); PLAY-dOrderedCharter-9 (the `[[unit]]` rows
and `read_units`), -11 (`tools/playbook/load_sets.py` and its `derive` verb, and the load-set call in
`render_agent_file` and `render_handoff`), -2 S4 (the override record), -15 (`instructions_edit.py`, the
change record and its `new change` stand-in door); TOOL-dFairHearing-8 S8 (the appendix's tenth column,
`disposition`); TOOL-dTotalRecall-1 (the registry `tools/memory-tree/record-kinds.toml`).

- **S1** — (amended, id 35) A return cites unit tags. `UNIT_SCHEMA` (`tools/workflows/unattended-unit.js:206`) and
  `SPEC_SCHEMA` (`tools/workflows/unattended-build.template.js:739`, rendered into
  `tools/workflows/unattended-build.js`) gain an optional `units`, an array of strings. The `returned`
  micro-format (`coding-governance-agents.template.md:70`, rendered into `AGENTS.md:66`) gains the
  trailing field `· units <units>`. `print_agent_lines` (`tools/roles/handoff.py:808`) fills `units` from
  a harness agent's result when its `units` is a list of strings each matching `UNIT_TAG_RE`, joined by
  `,`, and `-` otherwise, never empty, so the hold rule that keeps an `unknown` line out of the agent
  ledger (`:914`, `:918`) never holds a line for want of it. Observed by AC1.
- **S2** — A finding cites unit tags. The items of `FINDING_SCHEMA` and `SPEC_FINDING_SCHEMA`
  (`tools/workflows/tier2-review.template.js:637`, `:742`) gain an optional `units`, an array of strings;
  `renderAppendix` (`:1638`) gains the column `units` after `disposition`, each cell the finding's tags
  matching `UNIT_TAG_RE` joined by one space, or `-`; a tag that does not match is left out of the cell and
  counted in the run's note. `tools/workflows/tier2-review.js` is re-rendered. Observed by AC2.
- **S3** — What an agent can cite. `render_agent_file` (`tools/roles/render_agents.py:144`) and
  `render_handoff` (`tools/roles/handoff.py:312`) render, after the load-set check PLAY-dOrderedCharter-11
  S4 adds, one line `Units: <tag>, <tag>, …`, the role's load set in registry order as `load_sets.py
  derive` returns it; and the roles kit's manifest `tools/roles/instructions.toml` gains the unit
  `unit.cite-units` (§4 "The citation unit"), written with its change record through
  `build_records.py new change` while `instructions_edit.py` refuses writes (PLAY-dOrderedCharter-15 S4,
  S7). The agent files `.claude/agents/*.md` are re-rendered. Observed by AC3.
- **S4** — (amended, id 28) The effectiveness reading. `read_returned_units(root, window)` reads the `returned` lines
  ADDED inside the window to the tracked agent ledgers `<MEMORY_ROOT>/builds/*/build/*-agent-ledger.md`,
  from one `git log --since --until -p --unified=0` pass, each line's role (its first field) and its
  `units`; `read_finding_units(root, window)` reads the appendix rows whose `verdict` is `confirmed` from
  the tracked review records `<MEMORY_ROOT>/builds/*/reviews/*.md` whose file-name date falls in the
  window, the columns found by header name, never position, each row's `units` cell and its record's
  build; and `derive_unit_effectiveness(returns, findings, load_sets)` returns per unit tag `loads` (the
  returns carrying a `units` field whose role's load set holds the tag), `cites` (the returns naming it),
  `broken` (the confirmed findings naming it) and `builds` (the distinct builds of those findings). The
  load sets come from `load_sets.py derive`, one bounded subprocess per role met (60 s), the playbook kit
  found through the inline `resolve_kit_dir` block. A `METRICS` entry `instruction-units` answers §4
  "The lines". Observed by AC4.
- **S5** — The override reading. `read_override_records(root, window)` reads the tracked override
  records `<MEMORY_ROOT>/builds/*/build/*-override-*.md` (PLAY-dOrderedCharter-2 S4) whose file-name date
  falls in the window, each record's `Rule` and `Session` through `read_record_fields`; a record lacking
  either is counted `unread`, never left out silently. A `METRICS` entry `overrides` answers §4 "The
  lines". Observed by AC6.
- **S6** — (amended, id 3) `loop.propose`. `derive_proposals(root, window, rows, readings, retire, earlier)` runs each
  entry of `PROPOSERS`, a list of `(name, proposer)` pairs, in list order, and returns the proposals in
  TOOL-dCalibratedLens-3 S7's shape `{"kind", "id", "action", "accept", "row"}`. This unit's three:
  `derive_retire_proposals` (every ledger row whose state is `idle` and whose `catches` is a number:
  `retire`), `derive_unit_proposals` (a unit with `loads` at least `UNIT_LOAD_MIN` and no cite and no
  break: `prune`; a unit with `broken` at least `UNIT_BROKEN_MIN` across two or more builds:
  `tighten`) and `derive_amend_proposals` (a rule named by at least `OVERRIDE_RECUR_MIN` override records
  from two or more sessions: `amend`), each `accept` and `row` per §4 "The proposals". Each of the three
  leaves out a proposal whose `(kind, id)` a live keep governs (S8); another unit's entry reads
  `read_keep_records` and applies its own clause's rule. Run as `python loop_review.py propose [--dry-run]`,
  the walk's item between `item.loop.price` and `item.loop.file`. **Readers:** by name: none, since
  this item withdraws no name and its action words are values it mints · by value: NO VALUE READERS,
  nothing this item names is taken out of the tree. Observed by AC5, AC6 and AC8.
- **S7** — (amended, id 30) `review.loop.retire`, read through `read_loop_policy(root, "review.loop.retire")`, the key a
  string literal at the call. `resolve_retire_route(value, proposals, earlier)` governs the `retire`,
  `prune` and `tighten` proposals and never an `amend` or another unit's: under `propose-ratify` each is
  handed to `item.loop.file`; under `demote-then-propose` a `retire` or `prune` becomes `demote` unless a
  committed `loop-review` record whose file-name date is at least the window's days before the walk
  carries a `proposals` segment naming that `(kind, id)` with `demote`, and is then handed on as it
  stands; under `report` none is handed on. Every proposal, handed on or not, is one segment of the
  `proposals` line the record carries (§4 "The lines"). Each value is seen on its planted case.
  **Readers:** by name: none, since the item reads a key and withdraws no name · by value:
  NO VALUE READERS, the key's values are unchanged. Observed by AC7.
- **S8** — (amended, ids 1, 36, 37) The keep record, kind `keep`. `write_keep_record(root, kind, id, words, caused_by, at)`, run as
  `python loop_review.py keep --kind <kind> --id <id> --words <text> --caused-by <id>`, writes
  `<MEMORY_ROOT>/loop-review/<date>-keep-<key hash>.md`, and `-<n>` before `.md` when that day already
  holds one for the key, so a second keep is a record of its own; the key hash is `derive_key_hash(kind,
  id)`, factored out of `run_loop_file` so the filing key and the keep's name are one function. Its four
  fields are §4 "The keep record"; an empty field exits 2 before a write. `read_keep_records(root)` reads
  the TRACKED keeps, and the newest by file-name date and then `<n>` governs its `(kind, id)`. A keep is
  live while its date is fewer than the window's days before the walk and no catch or false red of the
  row is dated after it. `derive_ledger_rows` hands each row its governing keep and the newest event
  after it, and `derive_row_state` gains `kept`, after `catching` and before `new` and `idle`
  (TOOL-dCalibratedLens-2 §3). The registry row is §4 "The registry row". Observed by AC8 and AC9.
- **S9** — The item row `item.loop.propose` in `tools/loop/loop.toml`, in TOOL-dDeclaredLoop-12's row
  form: `step = "cadence.loop"`, `actor = "command:loop.propose"`, `needs = ["item.loop.price"]`,
  `outcomes = ["proposed"]`, `routes = { proposed = "item.loop.file" }`, `returns = "proposals"`, `owner =
  "dCalibratedLens"`; `item.loop.price`'s route is re-pointed to it and `item.loop.file`'s `needs` to
  `item.loop.propose`. Observed by AC5.
- **S10** — The catalogue row S7 reads (`tools/policy/catalogue.toml:1289-1293`) gains
  `summary` and `usage`, and `python tools/policy/policy.py lists --write` drains it from
  `tools/policy/unsummarised-keys.txt` (`:192`); values and default stay the row's. Observed by AC10.
- **S11** — The docs: `help/loop-review.md` gains "Proposals and keeps" (the four actions, their
  thresholds, the three values of the key S7 reads, the keep and its lapse, `keep` and `propose
  --dry-run`); `help/roles.md` "What each agent line tells you" (`:70`) gains the `units` field and the
  `Units:` line; `tools/loop/README.md` names the readers. Observed by AC11.

## 3. Non-goals (OUT)

- Applying a proposal. The loop writes no unit, rule, policy value or leg: a prune, a tighten, a demote,
  a retire and an amendment are each filed for the owner, who applies one through
  `instructions_edit.py`, the guarded policy command or a build, as P10 and the brief's S8 require.
- Merging two priced rows. `loop.propose`'s row in layer-expansions:262 also names merging; the ledger's
  row carries catch counts and no catch identities (TOOL-dCalibratedLens-2 §4 "The row"), so nothing can
  tell two rows that catch the same thing. §8 F6.
- The proposals other clauses name: re-derived caps (TOOL-dCalibratedLens-4), a breach that persists
  (TOOL-dCalibratedLens-15), the map's retirement (TOOL-dCalibratedLens-8), an eval case
  (TOOL-dCalibratedLens-10) and a promoted scenario (TOOL-dCalibratedLens-14), each a `PROPOSERS` entry of
  its unit and none routed by `review.loop.retire` (§8 F5).
- Filing and the intake: TOOL-dCalibratedLens-3's `run_loop_file`. Writing the keep at the owner's
  breakpoint: dDeclaredLoop's breakpoints call `keep` once they land; until then the owner runs it.
- Rules and bug classes as ledger rows: TOOL-dCalibratedLens-2 §3 gives them none.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-2` — `derive_ledger_rows` and `derive_row_state`, which gain the keep and `kept`; `read_record_fields`; the snapshot's rows; the `item.loop.price` row whose route moves to `item.loop.propose`
- **consumes-from** `TOOL-dCalibratedLens-3` — `METRICS`, which gains `instruction-units`, `overrides` and `proposals`; the walk; `run_loop_file`, whose key hash moves into `derive_key_hash`, and its proposal shape; the record and its home
- **hands-off** `TOOL-dCalibratedLens-10` — the appendix's `units` column and the return's `units` field, whose confirmed findings its eval cases are added from, and `PROPOSERS`, which gains its entry
- **hands-off** `TOOL-dCalibratedLens-8` — `PROPOSERS`, which gains the map-retirement entry
- **hands-off** `TOOL-dCalibratedLens-14` — `PROPOSERS`, which gains the scenario entry, and the keep record and `read_keep_records`, which its decline writes and reads under its own rule, never this unit's lapse
- **consumes-from** external — PLAY-dOrderedCharter-9, -11, -2 S4 and -15, TOOL-dFairHearing-8 S8 and TOOL-dTotalRecall-1, each DEFERRED at base and of an ancestor or parent build
- **hands-off** `TOOL-dCalibratedLens-25` — the `returned` fence and `print_agent_lines`' `units` field, whose position that unit's format-guard fixtures hold (id 35)
- **hands-off** `TOOL-dCalibratedLens-30` — the `[[usage]]` rows of `propose` and `keep`, which the minors batch's `docs_leg.py --list` observation reads (id 39)
- **consumes-from** `TOOL-dCalibratedLens-35` — the `three-homes` plant's `graded-by-a-row` case, which grades the keep this unit adds to the plant with its `keep` row (round-2 id 1)

## 4. Design

**Waits on:** TOOL-dCalibratedLens-2, TOOL-dCalibratedLens-3, PLAY-dOrderedCharter-9, -11, -2 and -15,
TOOL-dFairHearing-8 and TOOL-dTotalRecall-1; none exists at `8bec4cef` (`tools/loop/`,
`tools/playbook/load_sets.py`, `tools/playbook/instructions_edit.py` and every `instructions.toml` are
absent).

### Evidence

- No grammar carries a unit tag today: the `returned` shape is `<role> · <outcome> · <wall> · <tokens>
  out · run <run-id|direct>/<agent-id>` (`coding-governance-agents.template.md:70`); the appendix's nine
  columns are `id lens ref severity skepticSeverity verdict reason fixVerdict classes`
  (`tools/workflows/tier2-review.template.js:1640`); and neither return schema names a unit
  (`tools/workflows/unattended-unit.js:206-216`).
- The agent ledger is the committed home of every return: `print_agent_lines --write` adds each complete
  `agent` and `returned` line to the build's `*-agent-ledger.md` (`tools/roles/handoff.py:755`, `:928`),
  and a harness agent's line is filled from its journal result (`:898`).
- A rendered unit is its text alone (PLAY-dOrderedCharter-9 S4's `render_unit`), so an agent sees no tag
  unless the render names one; S3's `Units:` line is that name.
- `python tools/policy/policy.py get review.loop.retire` prints `propose-ratify` at base, and the key's
  row sits at `tools/policy/catalogue.toml:1289-1293` with no `summary` (`unsummarised-keys.txt:192`).

### The citation unit

```toml
# tools/roles/instructions.toml
[[unit]]
tag = "unit.cite-units"
level = 5
type = "directive"
scope = ["reader.every"]
trigger = "always"
budget = "line"
text = "MUST list in your return's units, and in each finding's units, the tags from your Units: line that the work followed or the finding shows broken."
owner = "dCalibratedLens"
enforced-by = "none — a citation is evidence the Loop Review reads, and an uncited unit reads as bearing no load"
```

`UNIT_TAG_RE` is `^[a-z][a-z0-9-]*(\.[a-z0-9-]+)+$`, declared once in each kit that holds a tag
(`handoff.py`, `tier2-review.template.js`, `loop_review.py`), since a kit imports no sibling kit; the
three spellings are compared by a parity arm (§7).

### The lines

Metrics lines of the `loop-review` record, in TOOL-dCalibratedLens-3 §4's grammar, the last segment the
source:

```
instruction-units: 214 units · 61 returns · 18 findings · 40 cited · 6 broken · agent ledgers, review records
overrides: 5 records · 3 rules · 1 recurring · 0 unread · builds/*/build/*-override-*.md
proposals: leg docs retire · unit unit.cite-units prune · unit unit.reuse-first tighten · rule practice.verify amend · propose-ratify
```

The `proposals` line is appended by the propose item to the metrics the walk hands `record`; its last
segment is the value of `review.loop.retire` in force; with nothing proposed its value is `none`.

### The proposals

| Proposer | `kind` | `id` | `action` | `row` | `accept` |
|---|---|---|---|---|---|
| `derive_retire_proposals` | the ledger kind | the ledger id | `retire`, or `demote` (S7) | the snapshot row | the row retired or demoted at the owner's breakpoint, or kept by a keep record |
| `derive_unit_proposals` | `unit` | the unit tag | `prune`, or `demote` (S7) | `loads <n> · cited 0 · broken 0` | the unit removed through `instructions_edit.py remove`, or kept |
| `derive_unit_proposals` | `unit` | the unit tag | `tighten` | `broken <n> · builds <k> · <finding refs>` | the unit edited through `instructions_edit.py edit` with a change record naming the findings, or kept |
| `derive_amend_proposals` | `rule` | the override records' `Rule` | `amend` | `<n> overrides · sessions <k> · <record paths>` | the rule amended through `instructions_edit.py edit` with a change record naming the override records, or kept |

`UNIT_LOAD_MIN` is 30, `UNIT_BROKEN_MIN` 3 and `OVERRIDE_RECUR_MIN` 2, declared once in
`loop_review.py` (§8 F3, F4). A ledger row in state `new` is never proposed, so nothing retires before a
full window of evidence (walkthrough:729-730).

### The keep record

```markdown
# Keep — leg docs

- **Kind:** leg
- **Id:** docs
- **Words:** "keep docs, it guards the help pages"
- **Caused-by:** <the intake or ask the proposal was filed as>
```

The date is the file name's. `--kind` is held to `^[a-z][a-z0-9-]*$` and `--id` to one line at the write
boundary; the path is built from the date and the key hash alone, so no argument becomes a path
component.

### The registry row

```toml
[[record-kind]]
name = "keep"
tag = "record.keep"
layer = "layer.observability"
home = "<MEMORY_ROOT>/loop-review/"
id-rule = "<date>-keep-<key hash>[-<n>].md"
schema = { form = "fields", fields = ["Kind", "Id", "Words", "Caused-by"] }
writer = "loop_review.py keep"
readers = ["loop_review.py propose", "loop_review.py price"]
lifecycle = "written once per keep, never edited; the newest of a (kind, id) governs"
check = "record-kinds"
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_returned_units`, `read_finding_units`, `read_override_records`, `read_keep_records`, `write_keep_record`, `derive_unit_effectiveness`, `derive_proposals`, `derive_retire_proposals`, `derive_unit_proposals`, `derive_amend_proposals`, `resolve_retire_route`, `derive_key_hash` | functions, `tools/loop/loop_review.py` | `read`, `write`, `derive`, `resolve`, each answered OK by `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at base |
| `PROPOSERS`, `UNIT_LOAD_MIN`, `UNIT_BROKEN_MIN`, `OVERRIDE_RECUR_MIN`, `UNIT_TAG_RE` | constants | none |
| `propose`, `keep` | `loop_review.py` verbs | none |
| `item.loop.propose` | item tag | none |
| `keep` | record kind | none |
| `kept` | ledger state | none |
| `retire`, `demote`, `prune`, `tighten`, `amend` | proposal actions | none |
| `instruction-units`, `overrides`, `proposals` | `METRICS` names | none |
| `units` | return field, finding field, appendix column, `returned` shape field | none |
| `unit.cite-units` | instruction unit | none |

§6 runs a sibling's file by its basename: `record_kinds.py` is `tools/memory-tree/record_kinds.py` (TOOL-dTotalRecall-1).

### Amendments (round-1 spec audit)

The round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Each bullet supersedes the text it
names; the unit it names owns the finding and its proof.

- **id 1 · §4 "The registry row" (H1, `TOOL-dCalibratedLens-19`)** —
  `home = "memory/loop-review/*-keep-*.md"`, the glob of the row's id-rule.
- **id 36 · §4 "The keep record", S8, AC9 (H2, `TOOL-dCalibratedLens-20`)** — The keep's third line
  is `**Serves:** keep TOOL-dCalibratedLens-5`, and `keep` joins `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` and HYGIENE's closed `<kind>` list in this pass, so AC9's field
  check reaches it.
- **id 35 · S1 (H7, `TOOL-dCalibratedLens-25`)** — The field sits before the run field as an
  optional bracket:
  `returned — <role> · <outcome> · <wall> · <tokens> out[ · units <units>] · run <run-id|direct>/<agent-id>`,
  so the agent id stays last for the format guard's `checkCarries`
  (`tools/hooks/format-guard.js:431-435`) and a line without the field still matches;
  `print_agent_lines` always writes it, `-` when the result carries none. The guard's fixtures and
  the leg's guard are `TOOL-dCalibratedLens-25`'s.
- **id 3 · §3, §8 F5, S6 (H4, `TOOL-dCalibratedLens-22`)** — `PROPOSERS` holds propose-time
  proposers only: this unit's three and those of units 8, 10 and 14. The gather-time proposals of
  units 4, 6, 15 and 16 reach `item.loop.file` through the walk's one route (TOOL-dCalibratedLens-3
  S7 as amended), and none is re-homed here; F5's "joining it in this unit's pass" is withdrawn.
- **id 48 · AC5 (H8, `TOOL-dCalibratedLens-26`)** — AC5 also runs `propose --dry-run` over
  TOOL-dCalibratedLens-26's plant `catch-none`, where every leg reads `catches` `-`, and it prints
  no `retire` proposal.
- **id 28 · S4 (M12, `TOOL-dCalibratedLens-30`)** — `read_finding_units` reads confirmed rows
  through a new verb `python tools/workflows/review_replay.py --confirmed-rows <record> --json`,
  printing `parse_appendix_rows`' rows or its refusal, run as a bounded subprocess through
  `resolve_kit_dir`; a refused record counts as `unread`, never as zero breaks.
- **id 29 · §4 "The citation unit", §7 (M13, `TOOL-dCalibratedLens-30`)** — The cited-tag check is
  PLAY-dOrderedCharter-19's `TAG_RE` and `TAG_MAX_BYTES`; the Python copies in `handoff.py` and
  `loop_review.py` are held by a new `PARITY_ROWS` row of `tools/lib/resolve-python.test.sh`, and
  the arm in `tier2-review.test.sh` compares only the JS template's copy with the canonical.
  `UNIT_TAG_RE` is not minted.
- **id 30 · S7 (M14, `TOOL-dCalibratedLens-30`)** — The earlier record S7 compares against is read
  through `read_loop_records` (TOOL-dCalibratedLens-3 S8 as amended).
- **id 37 · §4 "The registry row", AC9 (M17, `TOOL-dCalibratedLens-30`)** — The row carries
  `unarmed = "no keep is tracked until the owner's first keep"`, and AC9 also runs
  `record_kinds.py --check` over the tree after the pass: exit 0.
- **id 38 · Files touched, §7 (M18, `TOOL-dCalibratedLens-30`)** — After the row edit,
  `python tools/memory-tree/record_kinds.py --write` then `adopt-memory-tree.sh --render`; both
  HYGIENE copies land in this commit.
- **id 39 · S11 (M19, `TOOL-dCalibratedLens-30`)** — `tools/govkit/usage.toml` gains `[[usage]]`
  rows for `propose` and `keep`, with their flags.

### Amendments (round-2 spec audit)

The round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Its ids restart at 1, so each bullet
spells `r2 id`; each supersedes the text it names, and the unit it names owns the finding and its
proof.

- **r2 id 1 · S8, AC9 (H2, `TOOL-dCalibratedLens-35`)** — In the pass that lands the `keep` row,
  this unit adds one keep record of §4 "The keep record" to `TOOL-dCalibratedLens-19`'s `three-homes`
  plant in `tools/loop/loop_review.py`, so that plant's `graded-by-a-row` case grades three records
  from this order on; AC9 also runs that plant and reads `graded-by-a-row — ok` for the keep.

### Amendments (round-3 spec audit)

The round-3 spec audit
(`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`) confirmed the
findings below, and its disposal amended this text. Its ids restart at 1, so each bullet spells
`r3 id`; each supersedes the text it names, and the unit it names owns the finding and its proof.

- **r3 id 3 · §7 (M2, `TOOL-dCalibratedLens-48`)** — This unit edits three of the loads of
  `TOOL-dCalibratedLens-10`'s seed case, `coding-governance-agents.template.md`,
  `tools/workflows/tier2-review.template.js` and the `.claude/agents/` files it re-renders, so the
  seed is owed from this pass and §7 names the leg `instruction-eval` in prose. The one replay is
  the main loop's, recorded after the last commit touching a loaded path and before the close bar
  (`TOOL-dCalibratedLens-23` S1).
- **r3 id 5 · AC9, r2 id 1's bullet (M4, `TOOL-dCalibratedLens-48`)** — The `graded-by-a-row` case
  counts and names what it grades, so AC9 reads `graded-by-a-row — ok · 3 records` naming the keep's
  path (`TOOL-dCalibratedLens-35` S2).

### Files touched (estimate)

- `tools/loop/loop_review.py` (S4 to S8, the fixture plants)
- `tools/loop/loop.toml` (S9)
- `tools/loop/README.md` (S11)
- `tools/memory-tree/record-kinds.toml` (S8)
- `tools/policy/catalogue.toml` and `tools/policy/unsummarised-keys.txt` (S10)
- `tools/roles/handoff.py` (S1, S3)
- `tools/roles/render_agents.py` (S3)
- `tools/roles/instructions.toml` (S3)
- `.claude/agents/` (S3, re-rendered, never edited)
- `coding-governance-agents.template.md` and its render `AGENTS.md` (S1)
- `tools/workflows/tier2-review.template.js` and its render `tools/workflows/tier2-review.js` (S2)
- `tools/workflows/unattended-build.template.js` and its render `tools/workflows/unattended-build.js` (S1)
- `tools/workflows/unattended-unit.js` (S1)
- `tools/roles/adopt-roles.test.sh` and `tools/workflows/tier2-review.test.sh` (the arms in §7)
- `help/loop-review.md` and `help/roles.md` (S11)
- `tools/memory-tree/tree_lib.py` — `TYPED_RECORD_KINDS` gains `keep` (id 36)
- `tools/memory-tree/HYGIENE.template.md` and its render `memory/HYGIENE.md` (ids 36, 38)
- `tools/workflows/review_replay.py` — the `--confirmed-rows` verb (id 28)
- `tools/lib/resolve-python.test.sh` — the `PARITY_ROWS` row of the tag grammar (id 29)
- `tools/govkit/usage.toml` — the `propose` and `keep` rows (id 39)

### Alternatives rejected

- **Tags rendered on every unit line.** The test: a render of a role's load set with one `[unit.<tag>]`
  prefix per line against one `Units:` line; the prefix form grows every agent file by a tag per line
  and changes PLAY-dOrderedCharter-9's `render_unit`, a second build's renderer, while the line costs one
  line per file.
- **"Loaded" read from the citation itself.** A unit nobody cites would then read as never loaded, so a
  load-bearing unit and a dead one look alike; the load set is the denominator, read from the one deriver
  of it.
- **The loop applying a demotion.** Every write to a unit refuses an agent under the default
  `instructions.edit` (PLAY-dOrderedCharter-15 S3, S4), and the brief's S8 forbids a loop item writing a
  policy value; §8 F2.
- **Per-unit lines in the record.** At 200 or more units a line per unit outweighs the record; the
  counts stay in `instruction-units`, and each unit that moves is a proposal carrying its row.

## 5. Production-readiness checklist

- security — every tag is held to `UNIT_TAG_RE` before it reaches a line, a cell or a filing; the keep
  writer validates its four arguments at the write boundary and builds its path from a date and a hash;
  the loop writes no instruction, policy or leg; every subprocess takes an argument list and a bound.
- perf / scale — once per period: one `git log -p` over the agent ledgers, one read per review record and
  override record in the window, one `load_sets.py derive` per role met.
- error / empty / loading states — no ledger, review or override record in the window gives
  `searched-none` with its glob; an unreadable override record is counted `unread`; nothing proposed
  gives `proposals: none`; an absent playbook kit gives `instruction-units: searched-none` and no unit
  proposal, never a prune of every unit.
- observability — the three lines; each proposal carries its row; each keep is a committed record.
- risks — an agent that ignores `unit.cite-units` makes its units read as bearing no load, so prune needs
  30 loading returns and is only ever proposed; the `returned` shape gains a field, which the hooks kit's
  format guard reads from the same fence (`tools/roles/README.md:88`), so a session's pasted lines follow
  the fence's change.
- testing — §6's plants and fixtures, and §7's arms.
- migration — the ledger lines written before this unit carry no `units` field and count as no return
  for `loads`; review records before it carry no `units` column and count no break; nothing is rewritten.
- user docs — `help/loop-review.md` and `help/roles.md` (S11).

## 6. Acceptance criteria

- **AC1** — When `python tools/roles/handoff.py agents --run <id>` runs over a fixture journal holding one
  harness agent whose result carries `"units": ["unit.reuse-first", "BAD TAG"]` and one whose result has
  none, the first `returned` line ends `· units unit.reuse-first` and the second `· units -`, and both
  lines reach the ledger with `--write`; `grep -n "units <units>" coding-governance-agents.template.md
  AGENTS.md` prints the shape in both.
  Red when: a result with no `units` renders `unknown` and its line is held out of the ledger, or an
  unmatched tag is printed.
- **AC2** — When the review harness's fixture renders an appendix for two confirmed findings, one carrying
  `units` `["unit.verify-first"]`, `grep -n "| classes | disposition | units |" tools/workflows/tier2-review.js`
  prints the header and the rows carry `unit.verify-first` and `-` in that column.
  Red when: the column is missing, or sits before `disposition`.
- **AC3** — When `python tools/roles/render_agents.py --write` runs over a fixture whose load set for
  `gov-builder` holds two units, the rendered `gov-builder.md` carries one line `Units:
  unit.cite-units, unit.reuse-first`, and `grep -n 'tag = "unit.cite-units"' tools/roles/instructions.toml`
  prints the row.
  Red when: the line is absent or lists a unit outside the load set.
- **AC4** — When `python loop_review.py --fixture --plant effectiveness` commits two agent
  ledgers whose added `returned` lines carry `units` and one review record with two confirmed rows naming
  `unit.b`, over planted load sets, `gather --dry-run` prints the `instruction-units` line with the
  planted counts, and a ledger line added before the window is not counted.
  Red when: a line outside the window counts, or a return with no `units` field counts as a load.
- **AC5** — (amended, id 48) When the plant `retire` commits a snapshot holding one `idle` row with `catches` 0, one `new`
  row and one row whose `catches` is `-`, `propose --dry-run` prints one proposal, `leg <id> retire`, with
  an `accept`; and `run --check` prints `loop — 6 item(s) · ok`, the dry-run walk running `propose`
  between `price` and `file`.
  Red when: a `new` row or a `-` row is proposed, or the walk skips `propose`.
- **AC6** — When the plant `units-and-overrides` plants a unit loaded by 30 returns and cited by none, a
  unit broken by three confirmed findings across two builds, and two override records naming
  `practice.verify` from two sessions, `propose --dry-run` prints `unit … prune`, `unit … tighten` and
  `rule practice.verify amend`; with 29 loads, three breaks in one build, or both override records from
  one session, the matching proposal is absent; a third override record lacking `Session` makes the
  `overrides` line read `1 unread`.
  Red when: a threshold is crossed one short, or an unreadable override record is dropped silently.
- **AC7** — When the plant `retire-values` commits `review.loop.retire` as each value in turn over the
  `retire` plant: `propose-ratify` hands `leg <id> retire` to `file`; `demote-then-propose` hands `leg <id>
  demote`, and with an earlier committed record 60 or more days old whose `proposals` line names `leg <id>
  demote` hands `retire`; `report` hands nothing and the `proposals` line still names the proposal and
  `report`; under every value the `amend` proposal is handed to `file`.
  Red when: a value is not read, `report` files a proposal, or `demote-then-propose` retires with no
  earlier demote.
- **AC8** — When the plant `keep` runs `keep --kind leg --id <id> --words "keep it" --caused-by
  INTAKE-1`, then `price` and `propose --dry-run`, the row reads `kept` and is not proposed; with the keep
  dated 60 days back it is proposed; with a planted catch dated after the keep it reads `catching`; a
  second `keep` the same day writes a second file ending `-2.md`; `keep` with an empty `--words` exits 2
  and writes nothing.
  Red when: a pricer ignores the keep, a keep never lapses, or a second keep overwrites the first.
- **AC9** — (amended, ids 36, 37; r2 id 1) When `python record_kinds.py --check` runs in a scratch worktree holding one
  keep record that lacks `Words`, it exits 1 naming the record; with the field restored it exits 0;
  and `python loop_review.py --fixture --plant three-homes` prints `graded-by-a-row — ok · 3 records`
  naming the keep's path (r3 id 5).
  Red when: the `keep` row's fields do not reach the field check.
  fixture: `record_kinds.py` is TOOL-dTotalRecall-1's, absent at `8bec4cef`.
- **AC10** — When `grep -n -A8 'name = "review.loop.retire"' tools/policy/catalogue.toml` runs it shows
  `summary` and `usage`, `grep -cx 'review.loop.retire' tools/policy/unsummarised-keys.txt` prints `0`, and
  `git grep -n '"review.loop.retire"' -- tools/loop` prints the one literal reader.
  Red when: the row lacks a field, the name stays listed, or the key has no literal reader.
- **AC11** — When `grep -n "demote-then-propose" loop-review.md` and `grep -n "units" help/roles.md`
  run, each prints the new section's line.
  Red when: either page lacks it.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `docs` · `micro-format definitions` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `policy check` · `policy fixtures` · `check-wiring self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test` · `review-protocol parity (kit vs dogfood)` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base and
is named here in prose; it grades the loop arm once that unit lands.

The leg `instruction-eval` (TOOL-dCalibratedLens-10) is not in the manifest at base and is named here
in prose: this unit edits three of its seed case's loads, so the seed is owed from this pass (r3 id 3).

New arm: tools/loop/loop_review.py · covers AC4 AC5 AC6 AC7 AC8 · the `--fixture` plants `effectiveness`, `retire`, `units-and-overrides`, `retire-values` and `keep`, staged red by a proposer that ignores keeps, a `report` that files, and a threshold one short · none
New arm: tools/roles/adopt-roles.test.sh · covers AC1 · arm 9's `agents --run` fixture gains a result carrying `units` and one carrying none, staged red by a `units` field rendered `unknown`, which holds the line out of the ledger · none
New arm: tools/roles/render_agents.py · covers AC3 · its `--selftest` gains a `Units:` line case over a planted load set, staged red by a line listing a unit outside it · none
New arm: tools/workflows/tier2-review.test.sh · covers AC2 · an appendix fixture with a `units` finding, staged red by the column dropped, and the `UNIT_TAG_RE` parity across the three kits · none

## 8. Open questions

- **F1 — Where is the citation written, so the Loop Review reads it from committed records?** Options:
  (a) a `units` field in each return schema, carried onto the `returned` line the agent ledger commits,
  and a `units` appendix column on every review record; (b) a field on the act record
  (TOOL-dWellOiledMachine-32 S7), written once per harness session, which a role agent inside a Workflow
  is not; (c) a new record per return. (b) misses every subagent; (c) is a new record kind for a value an
  existing line can carry. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3, a reuse of the agent
  ledger and the appendix. widens: none · relaxes: none · grants: PLAY-dClosedLoop-3 the `returned` shape
  of `coding-governance-agents.template.md`, the clause naming "returns and findings that cite unit tags"
- **F2 — What does `demote-then-propose` do when the loop may write no unit or leg?** Options: (a) the
  loop proposes the demotion, and a row or unit still idle a window after its `demote` proposal is
  proposed for retirement; (b) the loop demotes through `instructions_edit.py` where `instructions.edit`
  admits an agent's write, and falls back to (a) otherwise; (c) treat it as `propose-ratify`. (b) widens
  the loop's write surface to instruction text (veto 3); (c) fails the value's own planted case. RESOLVED
  (agent, 2026-11-02, delegated): (a), rung 3, recorded as deviation 51 from the owner's option wording
  "Demote, then propose" (walkthrough:737-739), since the demotion is filed rather than performed.
  widens: none · relaxes: none
- **F3 — How many loading returns make a unit "bear no load"?** Options: (a) 30, the evidence floor this
  build's clauses 6 and 16 already state; (b) 10, `P90_MIN_ROWS`'s floor (TOOL-dWellOiledMachine-53 §8
  F2); (c) any one. (c) prunes a unit after its first uncited use. RESOLVED (agent, 2026-11-02,
  delegated): (a), rung 3, `UNIT_LOAD_MIN` declared once. widens: none · relaxes: none
- **F4 — What is "broken often", and how many override records "recur"?** Options for broken: (a) three
  confirmed findings across two or more builds in the window; (b) a p90 over every unit's breaks through
  TOOL-dCalibratedLens-4's factory, which the brief's S9 scopes to clauses 4, 6 and 16, and which reads
  every unit with one break as often while most units have none; (c) any one. For recur: (a) two records
  from two sessions; (b) two records from any sessions. (b) counts one session's repeated override as a
  standing one, which the clause's "habit" rules out. RESOLVED (agent, 2026-11-02, delegated): (a) for
  both, rung 3, `UNIT_BROKEN_MIN` and `OVERRIDE_RECUR_MIN` declared once. widens: none · relaxes: none
- **F5 — Which proposals does `review.loop.retire` route, and in what order do earlier proposers land?**
  The key's question (walkthrough:737-739) is a gate, rule or bug class that caught nothing, and the
  clause adds pruning and tightening; TOOL-dCalibratedLens-15 (order 6) and -4 (order 7) land before this
  unit (order 11) and propose. Options: (a) the key routes `retire`, `prune` and `tighten` only, and
  `PROPOSERS` is built here, a proposal step an earlier unit landed joining it in this unit's pass with
  its own routing; (b) the key routes every proposal, so `report` would silence a breach's owner item,
  the brake clause 15 exists for; (c) each proposer files on its own, a second filing path beside
  `run_loop_file`. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3. widens: none · relaxes: none
- **F6 — Does `propose` propose merges?** layer-expansions:262 names "retiring or merging", and the
  ledger row carries counts, not which findings or reds a row caught. Options: (a) leave merging out
  and name it a non-goal here, the item row's `does` naming retirement only; (b) merge rows whose counts
  and last-catch dates are equal, which pairs rows that caught different defects; (c) ask
  TOOL-dCalibratedLens-2 for a catch-identity column. (c) widens a sibling's row grammar for a proposal no
  clause states. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3; the clauses this unit carries name
  no merge. widens: none · relaxes: none
- **F7 — What can an agent cite, when a rendered unit shows no tag?** Options: (a) one `Units:` line per
  agent file and handoff, from the load set; (b) a tag on every rendered unit line; (c) practice tags
  only, which the charter already shows. (b) changes another build's renderer and costs a tag per line;
  (c) leaves every non-practice unit unmeasured. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3.
  widens: none · relaxes: none · grants: PLAY-dClosedLoop-3 the rendered agent files and handoffs gaining
  the `Units:` line, and the roles manifest gaining `unit.cite-units`

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the packet's Items 5 (`cl-dClosedLoop-0462@cad135ef`) and
  Obligations v2:1343, the brief's row for unit 5 and its S2, S3, S5 and S11 interfaces as
  TOOL-dCalibratedLens-2 and -3 rev-1 spell them, layer-expansions:212 and :259-266, the walkthrough's
  R2, foundations step 1, and PLAY-dOrderedCharter-2, -9, -11 and -15 at their current revisions.
- rev-2 · 2026-11-02 · §3 §4 §7 §8 S1 S4 S6 S7 S8 AC5 AC9 · amended at the disposal of the round-1
  spec audit `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4 "Amendments
  (round-1 spec audit)": ids 1 (`TOOL-dCalibratedLens-19`), 36 (`TOOL-dCalibratedLens-20`), 35
  (`TOOL-dCalibratedLens-25`), 3 (`TOOL-dCalibratedLens-22`), 48 (`TOOL-dCalibratedLens-26`), and
  28, 29, 30, 37, 38 and 39 (`TOOL-dCalibratedLens-30`); §3 gains the hands-offs to units 25 and 30.
- rev-3 · 2026-11-02 · §3 §4 S8 AC9 · amended at the disposal of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`, §4 "Amendments (round-2 spec audit)": r2 id
  1 (`TOOL-dCalibratedLens-35`), the keep added to the `three-homes` plant; §3 gains the
  consumes-from of unit 35.
- rev-4 · 2026-11-03 · §4 §7 AC9 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, §4 "Amendments (round-3 spec audit)": r3 ids
  3 and 5 (`TOOL-dCalibratedLens-48`), the `instruction-eval` seed this unit owes and AC9's counted
  line.

## 10. Reuse audit

The seams extended: the agent ledger and `print_agent_lines` (`tools/roles/handoff.py:755`, `:808`), the
committed home of every return; the review appendix (`renderAppendix`,
`tools/workflows/tier2-review.template.js:1638`) after TOOL-dFairHearing-8's column; the two harness
return schemas (`tools/workflows/unattended-unit.js:206`, `tools/workflows/unattended-build.template.js:739`);
PLAY-dOrderedCharter-11's `load_sets.py derive` for the denominator; PLAY-dOrderedCharter-2's override
record and PLAY-dOrderedCharter-15's `instructions_edit.py` as the amendment's route; and
TOOL-dCalibratedLens-2's pricer and field reader and TOOL-dCalibratedLens-3's filer, whose key hash is
factored rather than copied. `python tools/codebase-map/reuse_lookup.py "record which instruction units
an agent loaded followed or broke"` ranked name stems only (`load`, `records`, the test helper `units` in
`tools/unattended/unattended.test.sh`, `load_workflows`), none a record of a unit's use, and the recall
query below returned the brief, the packet, v2's row and PLAY-dOrderedCharter-15's brief, none a writer of
a unit tag; at base no writer of a unit tag exists, so no existing seam fits the citation itself and it is
added to the two existing carriers above. Where the brief and source disagree:
the brief has the `units` field "on a role agent's return"; a return reaches a committed record only
through the `returned` line, so S1 carries it there, and no return schema today holds any field of the
kind.

Recall terms used: `python tools/memory-recall/query.py "how does the loop review measure which
instruction units bear load and propose pruning tightening or a charter amendment" --terms "instruction
unit tag returned line agent ledger finding appendix override record keep record review.loop.retire
propose"`
