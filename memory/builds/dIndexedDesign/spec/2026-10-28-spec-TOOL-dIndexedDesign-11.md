# TOOL-dIndexedDesign-11 — the playbook set record as a kind, its identity derived once, and a set check that reds at the bar, registered at Test's leg-pack point

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 14 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0393@c8409a33 whole
**Carries:** node:record-kind.playbook-set

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-d.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-d.md) | research | TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-19 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

A playbook run's set record (`<records>/set-<run>.md`, written by `record_set`,
`tools/unattended/unattended.sh:13181`) carries the ordered hashes of the run's pieces and one verdict
per set-scoped check. Only the driver's `--close` grades it (`set-checks-recorded`, :11423, its
superseded compare at :11592-11606), so on the attended path, which never calls `--close`, a set
verdict describing pieces that have since changed lands green, and the leg that reads set records
reports and never fails (`tools/unattended/check-playbook.sh:662-710`). The set's identity is derived
twice, by the writer (:13248-13251) and by the close (:11598-11601). This unit registers the set
record as `record-kind.playbook-set`, derives its identity in one function, and adds the set check
that can go red at the merge bar, registered at Test's leg-pack point (night pass, point 6; layer-memory
"playbook set" row, :429).

## 2. Scope (IN)

- **S1** — One identity. `derive_set_identity <records-root> <run>` in
  `tools/unattended/lib-unattended.sh` prints the `LC_ALL=C`-sorted, comma-joined `hash:` values of
  every tracked `*.md` directly under `<records-root>` whose first `run:` line equals `<run>`, read
  split-safe (`GIT -c core.quotePath=false ls-files -z`, each name read with `read -r -d ''`), and
  prints nothing for a run with no piece record. `verb_record_set` (`unattended.sh:13231`) and the
  `set-checks-recorded` arm of `--close` (:11598) each call it in place of their inline loops, their
  verdicts unchanged. Observed by AC1 and AC2.
- **S2** — The set reader sources the library. `tools/unattended/check-playbook.sh` sources
  `lib-unattended.sh` beside it, behind the missing-file refusal `check-pass-order.sh:53-59` uses, and its
  set block (:662-710) becomes one function, `check_set_records <records-root> <playbook> <set-checks>
  <strict>`, which derives each run's identity through `derive_set_identity`. With `<strict>` empty it
  prints today's notes, and one more, `set superseded — <record> …`, where a record's `set:` line
  differs from the derived identity. Observed by AC3.
- **S3** — The set check. A mode `bash check-playbook.sh --sets` runs the population and, per
  playbook declaring `set_checks`, `check_set_records` with `<strict>` set, which `fail`s (exit 1) on
  three states of a set record: its `set:` line differs from `derive_set_identity` (`superseded`); it
  records a `FAIL` verdict (`failed`); its run has no piece record under the root (`orphan`). A run with
  no set record, and a record lacking a declared check's verdict, stay notes (§8 F1). It prints `sets
  <n> record(s) read · superseded <a> · failed <b> · orphan <c>` on every run, and `sets 0 record(s)
  read — no playbook run has recorded a set, so this check graded nothing` when the population holds no
  set record. Observed by AC3, AC4 and AC5.
- **S4** — The leg, registered at `point.flow.leg-pack`. A `[[gate_leg]]` row `playbook set check` in
  `tools/unattended/kit.toml`, argv `["bash", "{kit}/check-playbook.sh", "--sets"]`, `guard = []`,
  `red_after_land = true` and `pack = "design"`, the pack key PLAY-dOrderedCharter-19 S12 adds and the
  pack TOOL-dIndexedDesign-10 S5 opens, so the leg is one of the pack legs Test's leg-pack point composes
  (PLAY-dOrderedCharter-17 §4; the slot grammar of TOOL-dWitnessedBar-28 S10); `tools/gate-legs.json`
  rendered from it by `leg_factory.py --write` (TOOL-dWitnessedBar-11 S1, S8). The rows a new leg owes:
  `run_one "playbook set check"` and its budget line in `tools/unattended/run-unattended-gates.sh`
  (beside :202, :430), its row in `tools/govkit/subject-pins.tsv` and in
  `tools/run-gates/ceiling-evidence.txt`, and its name in the `gate-legs` claim of
  `memory/map/features/playbook-mode.md`. Build-run precondition: the leg factory and the `pack` key
  landed. Observed by AC6.
- **S5** — The kind's row. `playbook-set` appended to `tools/memory-tree/record-kinds.toml` through
  TOOL-dTotalRecall-1 S9's factory, `python record_kinds.py new playbook-set --tag record.playbook-set
  --writer "unattended.sh --record-set" --check "playbook set check" --purpose "a playbook run's set
  record: the run's pieces joined by hash, the set's identity derived from them, one verdict per
  set-scoped check"`, with TOOL-dTotalRecall-18's columns set through its landed verb: layer
  `layer.memory`, home `**/set-*.md` (§8 F2), id-rule `set-<run>.md`, schema `{ form = "header" }`,
  lifecycle `current-state`, and `readers = []` with `readers-none = "read by the set check and by
  --close's set-checks-recorded, under the root its playbook declares"`. Its node is
  `record-kind.playbook-set`. Build-run precondition: TOOL-dTotalRecall-1 and -18 landed. Observed by
  AC7.
- **S6** — The docs. `tools/unattended/PLAYBOOK-TEMPLATE.template.md`'s section 8 row and the
  `set_checks` comment name the set check leg and the three states it reds, rendered into
  `memory/guides/PLAYBOOK-TEMPLATE.md`; `KIT_UNATTENDED_VERSION` moves. NOT OBSERVED by a criterion:
  prose and a version, graded by the `kit/dogfood doc parity` and `unattended skill wiring` legs at the
  close.

## 3. Non-goals (OUT)

- The playbook kind, its resolver and Design's pack tag on `playbook validity gate`:
  TOOL-dIndexedDesign-10.
- Grading whether a run is complete. `pieces-complete` and the unrecorded set-check arm of
  `set-checks-recorded` stay `--close`'s; the bar cannot tell an attended run in progress from a
  finished one (§8 F1).
- A slot line printed by gov's own composition: TOOL-dWitnessedBar-28 S10 prints
  `slot point.flow.leg-pack` for the `adopter` pack; this unit adds a pack leg, not a printer.
- Moving `declared_list` or `declared_scalar` into the library: their twins stay byte-compared by
  check 28 of `tools/unattended/check-unattended.sh`.
- Comparing a piece record's `hash:` with its piece's live blob: the per-piece `stale` state the leg
  already reports.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-10` — `record.playbook`, whose declared `records` root is where every set record this check reads lives, and whose `design` pack this leg joins
- **consumes-from** external — TOOL-dTotalRecall-1 S9's factory and TOOL-dTotalRecall-18's columns; TOOL-dWitnessedBar-11's leg factory and PLAY-dOrderedCharter-19 S12's `pack` key; each DEFERRED at base and an ancestor's
- **hands-off** external — dWitnessedBar's `test.verdict` reads the set record through this leg (night-pass instruments, FK-11-1)

## 4. Design

### Evidence

- The two identity derivations at `4bf0f400d` differ in one respect a merge-bar reader must not
  inherit: both walk `for r in $(GIT ls-files -- "$root/*.md")`, which splits a path holding a space
  into two names, the class the leg fixed for its own reads in round 7 (`check-playbook.sh:242-243`, :685-686).
  S1's one function reads NUL-separated.
- `check-playbook.sh` sources nothing at base, and its comment on the declared-list twins says each
  kit script installs standalone (:262-264); `check-pass-order.sh`, `check-brief-recorded.sh` and
  `check-unattended.sh` each source `lib-unattended.sh` from beside them, so a leg of this kit sourcing
  the library is the kit's own pattern, and the twins stay as they are.
- The kit's fixture set record, `tools/unattended/fixture-records/set-dScriptedRepeat.md`, records
  `set: 44433e00…,57787f3e…`, the sorted `hash:` lines of the fixture's two piece records, and one
  `PASS`; `--sets` reads it green at base (PINNED, read at writing).

### The states

| State | Read from | Default mode | `--sets` |
|---|---|---|---|
| no set record for a run that has pieces | the root's piece records | note | note |
| a declared check with no verdict | the record's `## Verdicts` | note | note |
| `superseded`: `set:` differs from `derive_set_identity` | the record and the piece records | note | fail |
| `failed`: a `FAIL` verdict row | the record | note | fail |
| `orphan`: no piece record carries the record's run | the root | note | fail |

### Data flow

`--sets` → population loop (TOOL-dIndexedDesign-10's `check_is_playbook`) → per playbook,
`declared_scalar records` and `declared_list set_checks` → `check_set_records <root> <playbook>
<checks> strict` → per run id read from the piece records and per `set-*.md` under the root,
`derive_set_identity` → findings → exit.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_set_identity` | shell function, `lib-unattended.sh` | `sh.function`, asked at the pass |
| `check_set_records` | shell function, `check-playbook.sh` | `sh.function`, asked at the pass |
| `--sets` | flag of `check-playbook.sh` | none |
| `playbook set check` | gate leg | none |
| `playbook-set` | registry row, node `record-kind.playbook-set` | none |

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`: S1
- `tools/unattended/unattended.sh`: S1's two call sites, `KIT_UNATTENDED_VERSION`
- `tools/unattended/check-playbook.sh`: S2, S3
- `tools/unattended/kit.toml`: S4's row
- `tools/gate-legs.json`: the render of S4, never the edit
- `tools/unattended/run-unattended-gates.sh`: S4's `run_one` and budget
- `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt`: S4's rows
- `memory/map/features/playbook-mode.md`: S4's `gate-legs` claim
- `tools/memory-tree/record-kinds.toml`: S5's row, written by its factory
- `tools/unattended/PLAYBOOK-TEMPLATE.template.md` and its render `memory/guides/PLAYBOOK-TEMPLATE.md`: S6
- `tools/unattended/check-playbook.test.sh` and `tools/unattended/unattended.test.sh`: the arms of §7

### Alternatives rejected

- **A new script for the set check.** It would parse the population and the declaration block a
  second time; a mode of the leg reads them once.
- **Red the set states in the default mode.** Two legs would then red on one fact; the default mode
  keeps classifying and `--sets` is the one that fails.
- **Inline twins of the identity in the driver and the leg, byte-compared by check 28.** The library
  already exists for "the predicates the driver and the gate leg must answer IDENTICALLY"
  (`lib-unattended.sh:1`); a third twin pair would be a copy where a source is available.

## 5. Production-readiness checklist

- security — no new write path; the leg reads tracked records, and `record_set`'s three field guards
  (:13196-13201) still govern what reaches a record.
- perf / scale — one `ls-files` per records root and one read per set and piece record; the fixture
  root holds three.
- error / empty / loading states — an empty set population prints its `graded nothing` line, never a
  silent green; a missing library is exit 2 naming it.
- observability — each finding names the record, its state and, for `superseded`, both lists.
- risks — a landed set record already superseded reds the bar on the first run; gov's one record is
  green at base (§4 "Evidence"), and an adopter's red names the record and the verb that re-stamps it.
- testing — AC1 to AC7 by the pass; the arms of §7 at the close.
- migration — none: no record changes, and the leg reads what `record_set` already writes.
- user docs — the playbook template (S6); no `help/` page covers recipe mode (`help/README.md`).

## 6. Acceptance criteria

- **AC1** — When `bash -c '. tools/unattended/lib-unattended.sh ; derive_set_identity tools/unattended/fixture-records dScriptedRepeat'`
  runs at the repo root, it prints
  `44433e009c98e5b7f4730743c8ce7286165e21ef,57787f3e201f8edb2153f43318ea65b641ae0ccb`, the `set:` line
  of `set-dScriptedRepeat.md`; with the run `nobody` it prints nothing.
  Red when: the order, the separator or the run filter differs from the writer's.
- **AC2** — When `grep -c 'derive_set_identity' tools/unattended/unattended.sh` runs, it prints at
  least 2, and `grep -c "sed -n 's/^hash: //p'" tools/unattended/unattended.sh` prints 0.
  Red when: either call site keeps its own loop, so the identity is derived in two places.
- **AC3** — In a scratch clone whose fixture set record's `set:` line has its two hashes swapped and
  committed, `bash tools/unattended/check-playbook.sh --sets` exits 1 printing `superseded` and the
  record's path, and `bash tools/unattended/check-playbook.sh` exits 0 printing `set superseded`; with
  the record restored, `--sets` exits 0.
  Red when: a set whose identity disagrees with its pieces passes the set check.
  fixture: a clone under `%TEMP%`, written by the pass.
- **AC4** — In the same clone, a `leg fixture-distinct · verdict FAIL` row in place of the `PASS` row
  makes `--sets` exit 1 printing `failed`; a set record for a run named ghost, which no piece record
  carries, makes it exit 1 printing `orphan`.
  Red when: a failing set verdict or a set no piece belongs to passes.
- **AC5** — When `--sets` runs in the clone with the fixture set record deleted, it exits 0, prints
  `no set record` as a note and prints `sets 0 record(s) read`.
  Red when: the bar reds a run that has not yet recorded its set, or an empty population reads as
  graded.
- **AC6** — When `python -c "import json, sys; print(sorted(l['name'] for l in json.load(open(sys.argv[1], encoding='utf-8')) if l.get('pack') == 'design'))" tools/gate-legs.json`
  runs at the pass tip, it prints `['playbook set check', 'playbook validity gate']`, and
  `grep -c 'playbook set check' tools/unattended/run-unattended-gates.sh` prints at least 1.
  Red when: the leg carries no `pack`, or the kit's own runner never runs it.
- **AC7** — When `python record_kinds.py --check` runs at the pass tip, it lists `playbook-set` with
  tag `record.playbook-set`, home `**/set-*.md`, form `header` and check `playbook set check`, and
  exits 0.
  Red when: the row lacks a column TOOL-dTotalRecall-16 or -18 requires, or names no leg.
  fixture: the registry is TOOL-dTotalRecall-1's, absent at base until it lands.

## 7. Gates

The leg S4 adds, `playbook set check`, joins the manifest at this unit's pass and is kept green from
then on; the line below names the legs that exist at base.

`playbook validity gate` · `unattended kit gate` · `unattended skill wiring` · `routed-commits selftest` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `measure-legs selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-playbook.test.sh · covers AC3 AC4 AC5 · the `--sets` cases over the suite's scratch tree, its failing case staged by `check_set_records` comparing nothing in strict mode · none
New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · the record-set and `--close` set cases reading `derive_set_identity`, staged by the function sorting without `LC_ALL=C` · none

## 8. Open questions

- **F1 — Which states of a set record red the merge bar?** Options: (a) `superseded` only; (b)
  `superseded`, `failed` and `orphan`, each a fact about a recorded set whenever it is read; (c) those
  three plus a run with no set record and a declared check with no verdict. RESOLVED (agent,
  2026-10-28, delegated): (b), rung 1: the clause names the set record and "its set check", and
  layer-memory's row (:429) makes the set check the record's writer-side grader, "a playbook run's
  pieces joined by hash, and the set's identity derived from them", so its subject is a set record
  that exists; (a) leaves a landed failing set verdict green, which is the set check reading as passed;
  (c) reds an attended run between its pieces and its set, a state only `--close`, which knows the run
  is finishing, can grade. widens: none · relaxes: none
- **F2 — What is the kind's `home`, when each playbook declares its own `records` root?** Options:
  (a) `**/set-*.md`, the kind decided by the set check's population, the home admitting; (b) a fixed
  folder for set records; (c) one row per declared root. RESOLVED (agent, 2026-10-28, delegated):
  (a), rung 3, the most feature-rich survivor and the shape TOOL-dIndexedDesign-10 §8 F1 takes for the
  playbook itself: TOOL-dTotalRecall-42 S5 has the kind decide and the home admit; (b) moves every
  adopter's set records and the fixture's, which `record_set` writes under the declared root
  (:13203); (c) makes the registry change with each adopter playbook. widens: none · relaxes: none
- **F3 — Is the set check a new leg or a verdict of the existing one?** Options: (a) a new leg, a mode
  of `check-playbook.sh`; (b) red the set states in `playbook validity gate`; (c) a new script.
  RESOLVED (agent, 2026-10-28, delegated): (a), rung 3: the clause registers "its set check" at Test's
  leg-pack point as its own registration, (b) makes one leg answer two questions and red twice for one
  fact in the default mode's notes, and (c) re-parses the population. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 11, scout D's row 11, shared interfaces
  4 to 6 and disagreement 8, and the sources read at `4bf0f400d`.

## 10. Reuse audit

The seams extended are the set writer `record_set` and its verb `verb_record_set`
(`tools/unattended/unattended.sh:13181`, :13231), whose identity derivation (:13248-13251) and the close's
copy (:11598-11601) become one library function in `lib-unattended.sh`, the kit's home for predicates
the driver and a leg must answer identically; the leg's set block (`check-playbook.sh:662-710`),
made one function both modes call; and the leg factory for the registration.
`python tools/codebase-map/reuse_lookup.py "derive a playbook set identity from its piece record
hashes and red a superseded set"` ranked name stems (`records` in `gotchas.py`, `derive_clause_hash`,
`read_records` in `deviation_join.py`), none of which reads a set record: no seam fits beyond the two
copies the scout found, which S1 folds. Scout D's lines held at `4bf0f400d` except the set reader's
`declared_list` call, at :670 rather than :668, and its range, :662-710; its proposed home for the
identity, `lib-unattended.sh`, is kept, and its note that `check-playbook.sh` carries no library is
true at base and changed by S2. A dScriptedRepeat round-1 diff review asked for exactly this compare
of the `set:` line against the derived list (`memory/builds/dScriptedRepeat/reviews/2026-08-21-review-TOOL-dScriptedRepeat-5-diff-round1.md`, line 158); the close took it and the leg did not.

Recall terms used: `python tools/memory-recall/query.py "where is a playbook set record graded and its identity compared" --terms "playbook set record set_checks record_set verb_record_set superseded identity leg-pack set-checks-recorded check-playbook hash"`
