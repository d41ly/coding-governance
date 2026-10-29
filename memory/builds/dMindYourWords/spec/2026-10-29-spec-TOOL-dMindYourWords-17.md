# TOOL-dMindYourWords-17 — the overloaded terms settled: attended, playbook and baseline each keep one sense, defined once and reworded where a carrier spends it on another

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 17 · closes TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0278@8c3bb6f9 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-build-TOOL-dMindYourWords-14-reuse-scout-d.md](../build/2026-10-29-build-TOOL-dMindYourWords-14-reuse-scout-d.md) | research | TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 |
| [2026-10-29-build-TOOL-dMindYourWords-17-deviation-171.md](../build/2026-10-29-build-TOOL-dMindYourWords-17-deviation-171.md) | deviation | — |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |

<!-- /gen:spec-records -->

## 1. Goal

Three words each name two things (`gap-lex-09`): attended a kind of session and a mode, playbook the charter's
renderer and playbook mode, baseline retrofit's tolerated debt and a measured reference. This unit gives each word
one sense, writes each settled term once as a `definition` unit the one-fact check guards, and rewords the carriers
that spend a word on its retired sense, so a reader meets one meaning per word.

## 2. Scope (IN)

Build-run precondition: PLAY-dOrderedCharter-9 S1 (the `[[unit]]` row), -15 S2 and S3 (`instructions_edit.py`,
`propose`, `instructions.edit`) and -20 S2 (`instruction_units.py one-fact`) have landed; dOrderedCharter is an
ancestor of this build through dWitnessedBar and dDeclaredLoop, so they land first. This unit calls them and never
re-specs them.

- **S1** — The settled senses, the table in §4 "### The senses", following the records that decided two of them:
  attendance is a mode and the session the owner types in is the "owner" session (night pass :79-81, :88,
  :113-114); "baseline" keeps retrofit's meaning and an experiment's probe record is the "measured reference" (night
  pass :181-182); "playbook" keeps playbook mode's record and the charter's kit is the "charter renderer" (§8 F1).
  Observed by AC1 and AC5.
- **S2** — Seven `definition` units, the rows of §4 "### The definitions", each `<term> — <meaning>` in
  `tools/lexicon/instructions.toml` through `python tools/playbook/instructions_edit.py propose --manifest lexicon`
  with `add`'s arguments. Under `instructions.edit`'s default `owner-command-agents-propose` an agent's call writes
  nothing, so the builder writes the proposal record
  `memory/builds/dMindYourWords/build/<date>-build-TOOL-dMindYourWords-17-definitions.md`: the seven rows in a `toml`
  fence and the apply command `propose` printed, which the owner runs at a terminal (§8 F2). Observed by AC1.
- **S3** — Session-kind `attended` reworded to the owner session in every prose and comment line of §4 "### The
  carriers" row A. Observed by AC2.
- **S4** — The value `attended` of the persisted fact `landed-by`, and the display `LANDED (attended)` it drives, move
  to `owner`: the writer at `tools/unattended/unattended.sh:7311` and `:7390` writes `landed-by owner`, `DP_BY`
  takes `owner` (`:1527`), the display reads `LANDED (owner)` (`:8190`), check 15's population is `owner`
  (`tools/unattended/check-unattended.sh:2170-2187`, `:3039`) and `read_missing_landed_facts` takes `owner`
  (`tools/unattended/lib-unattended.sh:1782-1788`). Every reader of the fact accepts `attended` as well, read as
  `owner`, because eight committed run-state records carry it and a landed record is never rewritten.
  **Readers:**
  by name: `tools/unattended/unattended.sh` (`:1409`, `:1527`, `:7170`, `:7221`, `:7270`, `:7311`, `:7327`, `:7390`,
  `:7417-7419`, `:8187-8190`, `:9222`); `tools/unattended/check-unattended.sh` (`:2168-2187`, `:3039`);
  `tools/unattended/lib-unattended.sh` (`:1775-1788`); `tools/unattended/STOPS.template.md` (`:34`, `:254`, `:496`,
  `:499`, `:504`, `:507`, `:554`, `:555`) and `tools/unattended/VERBS.template.md` (`:102`, `:326`, `:327`, `:985`) with
  their renders `memory/guides/UNATTENDED-STOPS.md` and `memory/guides/UNATTENDED-VERBS.md`;
  `tools/unattended/unattended.test.sh` (`:10708`, `:10711`, `:10750`); `tools/unattended/check-unattended.test.sh`
  (`:6169-6172`).
  by value: the eight records `memory/builds/aEvidencedLens/RUN.md`, `memory/builds/aFrugalTurnstile/RUN.md`,
  `memory/builds/aHomedAnchor/RUN.md`, `memory/builds/aMendedFleet/RUN.md`, `memory/builds/aQuotedBrief/RUN.md`,
  `memory/builds/aRoutedQuill/RUN.md`, `memory/builds/dHomedResolver/RUN.md` and
  `memory/builds/dRemeasuredRender/RUN.md`, each `landed-by: attended`, compared by the fact reads at
  `unattended.sh:7221`, `:8189` and `check-unattended.sh:2170`, which keep reading them as `owner`.
  Observed by AC3 and AC4.
- **S5** — The charter sense of `playbook` reworded to "the charter", "the charter template" or "the charter
  renderer" in every line of §4 "### The carriers" row C; a path, a kit id, a placeholder or a leg name spelling
  `playbook` stays (§4 "### Kept names"). Observed by AC5.
- **S6** — The live-entry sense of `baseline` in the unattended kit, scout D's fourth sense, reworded to "live-entry
  commit" or "live-entry roster" in every comment and refusal text of §4 "### The carriers" row D, with the suite
  lines asserting those texts; the function `baseline_units` keeps its name (§4 "### Kept names"). Observed by AC6.
- **S7** — The terms other builds carry as nodes. `policy-key.runtime.attended-judge` and
  `policy-key.runtime.attended-allowance` name the judge and allowance for an owner session (layer-runtime :1450-1453),
  the session sense this unit settles away, and are dWellOiledMachine's carried nodes, so their rename is that build's deviation: this unit
  files the ask §8 F4 states. `record-kind.baseline` (TOOL-dLinkedLibrary-8) is retrofit's, `record-kind.playbook`
  (TOOL-dIndexedDesign-10) is playbook mode's record, and `record-kind.attendance-override` is the mode's, each the
  kept sense and owed nothing. NOT OBSERVED by a criterion of this unit: the ask is filed by the main loop and
  answered by dWellOiledMachine.

## 3. Non-goals (OUT)

- Any frozen record: the night pass two record's "baseline loop scenario" (night pass two :14), scout D's fifth sense,
  and the chain's own records and instruments, which the packet's Non-goals freeze. A record is evidence, not a
  carrier.
- Renaming an identifier, a conf key, a placeholder, a kit id, a stream, a family or an install path that spells one
  of the words in another sense: the kept names of §4, a relaxed bound recorded in
  `2026-10-29-build-TOOL-dMindYourWords-17-deviation-171.md` (§8 F3).
- The other kits' `baseline` senses, each bound to an identifier or a sibling's vocabulary: run-gates' diff base and
  its calibrated `--calibrate` evidence, drift-audit's `BASELINES`, `DESIGN_BASELINE`, govkit's `on_baseline_red`, the
  manifest check's stall baseline, runlog's `start^` baseline. Named so the residual is visible; a follow-up if the
  owner wants them reworded.
- Applying the seven definitions: the owner's act at a terminal, under `instructions.edit`'s default.
- The mode sense of `attended` (an attended run, build, path or landing, `mode: 'attended'`), which is the kept
  sense and stays as written.

### Edges

- **consumes-from** external — PLAY-dOrderedCharter-9 S1, -15 S2 and S3, -20 S2 (the unit row, `propose`, `instructions.edit`, `one-fact`); without them there is no definition unit and no one-fact check
- **hands-off** external — dWellOiledMachine renames `runtime.attended-judge` and `runtime.attended-allowance` by its own deviation (§8 F4); the owner applies the seven definitions from the proposal record

## 4. Design

### The senses

| Word | Keeps | Retired sense | Settled spelling of the retired sense |
|---|---|---|---|
| `attended` | the mode: a run, build, path or landing under an `attendance` other than `unattended` | a kind of session, and who landed a hand-off | "owner session"; `landed-by: owner`, `LANDED (owner)` |
| `playbook` | the record a `recipe` run follows, `record-kind.playbook` | the charter, its template and its renderer | "the charter", "the charter template", "the charter renderer" |
| `baseline` | retrofit's tolerated debt: the map's `baseline.toml`, `record-kind.baseline` | a measured reference, and the commit a run entered its live phase at | "measured reference"; "live-entry commit" |

### The definitions

Each row: `level = 3` (`methods`), `type = "definition"`, `scope = ["reader.every"]`, `trigger = "always"`,
`budget = "line"`, `owner = "dMindYourWords"`, `class = "fixed"`, and an `enforced-by` list of one description:
`instruction_units.py one-fact: a second active definition of the term is red`.

| Tag | Text |
|---|---|
| `unit.lexicon.term-attended` | `attended — under an attendance other than unattended: a mode of a run, build, path or landing, never a kind of session` |
| `unit.lexicon.term-owner-session` | `owner session — the session the owner types in, whatever the attendance; its binding record reads owner` |
| `unit.lexicon.term-playbook` | `playbook — the record a recipe run follows, written from PLAYBOOK-TEMPLATE.md; a record-kind.playbook record` |
| `unit.lexicon.term-charter-renderer` | `charter renderer — the kit at tools/playbook/, which renders the charter from its template; its id keeps playbook as a name` |
| `unit.lexicon.term-baseline` | `baseline — the debt a retrofit tolerates at adoption, such as the codebase map's baseline.toml` |
| `unit.lexicon.term-measured-reference` | `measured reference — an experiment's probe record, the measurement a later one is compared with` |
| `unit.lexicon.term-live-entry-commit` | `live-entry commit — the commit an unattended run entered its live phase at, whose roster the add arm compares` |

### The carriers

Pinned at `ccd1292e`, 2026-10-29, by `git grep -n -i -w` per word over the product paths and classified by sense;
the builder re-runs the grep at build time and applies the same rule to any line that moved.

| Row | Sense reworded | Lines |
|---|---|---|
| A | `attended` as a session | `WIRE-INTO-PROJECT.md:699`; `skills/session-kickoff/SKILL.md:220`; `tools/hooks/README.md:144`, `:173`; `tools/hooks/agent-cap.js:1393`, `:1438`, `:1550`; `tools/roles/README.md:301`; `tools/unattended/README.md:125`, `:395`; `tools/unattended/gate-guard.js:77`; `tools/unattended/check-unattended.sh:565` |
| B | `landed-by: attended` and `LANDED (attended)` | S4's readers |
| C | `playbook` as the charter | `README.md:7`, `:11`, `:19`; `WIRE-INTO-PROJECT.md:17`, `:236`, `:484`, `:485`, `:779`, `:799`, `:870`, `:1285`, `:1342`; `help/roles.md:150`; `skills/deploy-governance/SKILL.md:3`; `skills/session-kickoff/MANIFEST-TEMPLATE.md:76`, `:136`, `:139`; `skills/session-kickoff/SKILL.md:266`; `tools/roles/README.md:79`, `:81`, `:82` |
| D | `baseline` as the live-entry commit | `tools/unattended/lib-unattended.sh:1958-2000`, `:2077`, `:2093`, `:2096`, `:2102`, `:2106`, `:2110`, `:2114`, `:2117`, `:2130`, `:2142-2144`; `tools/unattended/check-unattended.sh:3893-3968`; `tools/unattended/unattended.sh:5237`, `:13394-13396`; `tools/unattended/check-unattended.test.sh:3795`, `:3820`, `:3836`, `:3840`; `tools/unattended/unattended.test.sh:8635`, `:8652` |

The `attended` hits the grep finds and row A does not list are the mode sense: the charter template's "An attended
code build" (`coding-governance-agents.template.md:140`), the protocol's "An attended run" (`tools/unattended/PROTOCOL.template.md:642`),
the build Skill (`tools/roles/SKILL.template.md`), the harness's `mode: 'attended'`, the attended landing of
`tools/push-main.sh`. The `playbook` hits outside row C are playbook mode's record in `tools/unattended/`, kept.

### Kept names

Spelled in another sense and kept as names, each a public surface, an install path, a frozen grammar or an identifier
a suite asserts: `tools/playbook/`, the kit id `playbook`, `render_playbook.py`, `adopt-playbook.sh`,
`{{PLAYBOOK_PATH}}`, `playbook_path`, the `gov:playbook` marker, `check-playbook-parity.sh`, the stream `playbook` and
the family `PLAY`; `baseline_units` (asserted by name at `tools/unattended/unattended.test.sh:8670-8679`); the
as-built view's `baseline` row word (`tools/memory-tree/design_lib.py:125`), `DESIGN_BASELINE`, `BASELINES`,
`on_baseline_red`, `STEP_BASELINE`. The `charter renderer` definition names the first group, so the word's one
definition says where it survives as a name.

### Migration

The persisted value is read both ways from this pass on and written only as `owner`: no record is rewritten, and a
run-state file a `--settle` or a rotation writes after the pass carries `landed-by: owner`.

### Rollout

The rewording and the value migration are live at landing; the definitions are live once the owner applies the
proposal record's command, and the one-fact check guards them from then.

### Files touched (estimate)

- `README.md`
- `WIRE-INTO-PROJECT.md`
- `help/roles.md`
- `skills/deploy-governance/SKILL.md`
- `skills/session-kickoff/MANIFEST-TEMPLATE.md`
- `skills/session-kickoff/SKILL.md` (its installed copy follows from the adopter)
- `tools/roles/README.md`
- `tools/hooks/README.md`
- `tools/hooks/agent-cap.js`
- `tools/unattended/README.md`
- `tools/unattended/gate-guard.js`
- `tools/unattended/STOPS.template.md` and its render `memory/guides/UNATTENDED-STOPS.md`
- `tools/unattended/VERBS.template.md` and its render `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `memory/builds/dMindYourWords/build/2026-10-29-build-TOOL-dMindYourWords-17-definitions.md` (the proposal record; the date is the build pass's)

### Alternatives rejected

- **Renaming the charter's kit and stream so playbook mode keeps the word alone**: `tools/playbook/` is an install
  location, outside the grant, and the `PLAY` family's ids are immutable in every record (§8 F1).
- **Renaming playbook mode to `recipe` so the charter keeps the word**: `record-kind.playbook` is
  TOOL-dIndexedDesign-10's carried node and cl-dClosedLoop-0392 names "the playbook record kind" (§8 F1).
- **Writing the definitions into the manifest by hand**: the write path's default refuses an agent's write, and
  bypassing it widens the instruction write surface (§8 F2).
- **Every identifier renamed too**: the as-built view's grammar at `design_lib.py:125` parses a frozen record's word
  `baseline` (§8 F3).

## 5. Production-readiness checklist

- security: no write surface widens; the definitions go through the guarded write path's `propose`, and the owner applies them.
- perf / scale: text edits and one fact read; nothing runs per call.
- error / empty / loading states: a fact `landed-by` missing reads as today; `attended` reads as `owner`.
- observability: `--status` prints `LANDED (owner)`; check 15's report names the `owner` population.
- risks: a missed carrier line keeps a retired sense; the grep of AC2 and AC5 and the kept-names list bound it, and the one-fact check guards the definitions.
- testing: AC1 to AC6 and §7's arms.
- migration: §4 "### Migration".
- user docs: `help/roles.md`, `README.md`, `WIRE-INTO-PROJECT.md` and the Skills are the carriers reworded.

## 6. Acceptance criteria

- **AC1** — When a scratch clone sets `instructions.edit = "command-for-all"` in its `.governance/policy.toml`,
  applies the seven rows of the proposal record with `instructions_edit.py add`, and runs
  `python instruction_units.py one-fact`, it exits 0; with an eighth active row `unit.demo.attended-again` whose text is
  `attended — a kind of session`, it exits 1 naming the term `attended`.
  Red when: a second definition of a settled term passes, or one of the seven fails the schema.
  fixture: a scratch clone under `%TEMP%`; the tree holds the rows only once the owner applies them.
- **AC2** — When `git grep -n -i -E "attended session|ATTENDED session"` runs over `tools/`, `skills/`, `help/`,
  `README.md` and `WIRE-INTO-PROJECT.md` after the pass, it prints nothing.
  Red when: a row A line keeps the session sense.
- **AC3** — When `grep -n -E "landed-by (attended|owner)" tools/unattended/unattended.sh` runs, every writer line
  writes `owner` and the only `attended` left sits in a read that accepts the legacy value.
  Red when: a writer still writes `attended`, or a reader refuses it.
- **AC4** — When `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh` runs after the pass, its check 15
  report line names an `owner LANDED` population that counts the eight legacy records, and no `attended` population.
  Red when: a legacy `landed-by: attended` record falls out of the population or reds.
  figure: 8 is PINNED at 2026-10-29; the report DERIVES the count.
- **AC5** — When `git grep -n -i -w playbook` runs over the row C files after the pass, every hit is a path, a kit id,
  a placeholder, a leg name or playbook mode's record, and none of the row C lines names the charter by the word.
  Red when: a row C line keeps the charter sense.
- **AC6** — When `git grep -n -i baseline -- tools/unattended/lib-unattended.sh tools/unattended/check-unattended.sh`
  runs after the pass, every hit is the kept identifier `baseline_units` or retrofit's `baseline.toml`
  (`check-unattended.sh:1094`), and the refusal texts read "live-entry".
  Red when: a row D line still calls the live-entry commit the baseline.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `policy fixtures` · `recall floor` · `recall floor arms` · `routed-commits selftest`

New arm: tools/unattended/unattended.test.sh · covers AC3 · the settle case at `:10708-10750` asserts `landed-by owner` and `LANDED (owner)`, red while the writer writes `attended` · none
New arm: tools/unattended/check-unattended.test.sh · covers AC4 · a planted record carrying `landed-by: attended` beside one carrying `landed-by: owner`, both graded in the `owner` population · none

## 8. Open questions

- **F1 — Which sense keeps "playbook".** Options: (a) playbook mode's record keeps it, the charter's kit is the "charter renderer" and the charter the charter; (b) the charter keeps it and playbook mode becomes `recipe` throughout, which renames `record-kind.playbook`, TOOL-dIndexedDesign-10's carried node that cl-dClosedLoop-0392 calls "the playbook record kind", so it cannot complete in this build; (c) the kit, stream and family are renamed, which moves the install location `tools/playbook/`, a veto 2 change the `may: PLAY-dClosedLoop-3` grant does not name, and cannot touch the `PLAY` ids every record carries. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the most capable survivor, matching v2's own use of the word for the record kind and the unattended kit's `recipe` for the mode. widens: none · relaxes: none
- **F2 — How the seven definitions reach the manifest.** Options: (a) `instructions_edit.py propose` and a proposal record the owner applies at a terminal, the default `owner-command-agents-propose` working as written; (b) the rows and their `change` records written by hand through the factory's `new change` door, which bypasses the write path's refusal of an agent's write and widens the instruction write surface (veto 3); (c) `instructions.edit = "command-for-all"` set in `.governance/policy.toml`, an owner policy change (veto 2 outside the grant). RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the one survivor. widens: none · relaxes: none
- **F3 — How far the rewording reaches.** Options: (a) every carrier and identifier spelling a word in another sense, which renames the as-built view's frozen row word read at `design_lib.py:125` (veto 1, the packet's Non-goals), the `PLAY` family (the charter's immutable ids) and `tools/playbook/` (veto 2, an install location); (b) user-facing prose, comments and printed or persisted values in the carriers scout D lists and every session-kind `attended` hit, identifiers and the other kits' bound `baseline` senses kept, which falls short of the clause's "settled" for those; (c) the definitions alone, short of it everywhere. Every option fails veto 1, so rung 6 relaxes the weakest failing bound: (a) breaks two strongest-tier bounds, an owner ruling and the charter's id rule, and (b) one weakest-tier bound, the reach into names and other kits' vocabularies this spec read into "settled", which the clause's text never names. RESOLVED (agent, 2026-10-29, delegated): (b), rung 6, ER:328 "Relax the weakest bound", recorded in deviation 171 with its Bound, Tier and Reason; the governance-carrier wording is a veto 2 change the clause names. widens: none · relaxes: the clause's settlement over the identifier-bound senses and the other kits' baseline senses · grants: PLAY-dClosedLoop-3 the governance-carrier wording of attended, playbook and baseline
- **F4 — The two runtime keys spelling the session sense.** `runtime.attended-judge` and `runtime.attended-allowance` decide an owner session's gated call. Options: rename them here, an edit of dWellOiledMachine's carried nodes this build may not make; leave them, which keeps the retired sense in two keys; ask dWellOiledMachine. RESOLVED (agent, 2026-10-29, delegated): ask, rung 3. The ask, for dWellOiledMachine's `BACKLOG.md`: THE RUNTIME KEYS SPELL ATTENDED AS A SESSION KIND · accept `runtime.attended-judge` and `runtime.attended-allowance` renamed by dWellOiledMachine's deviation to name the owner session, or a recorded decision that they name the mode, seen as `policy.py get` answering the settled name. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft.

## 10. Reuse audit

No existing seam fits in code: the lexicon kit grades code identifiers, never prose terms, and the probe
`python tools/codebase-map/reuse_lookup.py "check that one term has exactly one definition across instruction units"`
ranked `check`, `has`, `units` and
`check_convention`, none a term-uniqueness check; the seam extended is PLAY-dOrderedCharter-20 S2's one-fact check over
`definition` units, written through PLAY-dOrderedCharter-15's `propose`. The fact reader `fact` and its writer
`set_fact` in `tools/unattended/` carry the value migration, read both ways rather than a second reader. Where a
record and source disagree: scout D cites the persisted value at `unattended.sh:1527`, `:7221`, `:7311`, `:7327` and
`:7390`, which hold, and misses `:7170`, `:7270`, `:7417-7419`, `:8187-8190` and `:9222`, the other readers, now in
S4; it cites lib-unattended's fourth sense at `:1958-2000`, which holds, and misses the refusal texts at `:2096-2130`
and the checker's comments at `check-unattended.sh:3893-3968`, now in row D; the recall probe surfaced
`derive_attended` (TOOL-dFurnishedOrders-16) and `resolve_owner_question`'s `attended` flag (TOOL-dBoundRoles-11), both
the kept mode sense.

Recall terms used: `python tools/memory-recall/query.py "which sense does attended playbook and baseline keep once the overloaded terms are settled" --terms "attended attendance owner session playbook recipe charter renderer baseline retrofit measured reference gap-lex-09"`
