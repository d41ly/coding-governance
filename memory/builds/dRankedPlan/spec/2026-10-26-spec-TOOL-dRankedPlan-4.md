# TOOL-dRankedPlan-4 — dormancy disposal: a dormant build moved by the owner's disposition, shown in the plan view

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 11 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0372@5c733981 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-15 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) | spec-audit | TOOL-dRankedPlan-16 TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-2 TOOL-dRankedPlan-14 TOOL-dRankedPlan-13 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-3 TOOL-dRankedPlan-5 TOOL-dRankedPlan-15 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-7 |

<!-- /gen:spec-records -->

## 1. Goal

Dormant work is labelled, never disposed (gap-plan-05): at base `memory/LIVE.md` labels 22 of its 46
live builds `dormant`, and nothing moves one. The walkthrough's planned unit says a build dormant past
the threshold is deferred as one of Maintain's safe fixes and the plan view shows it
(walkthrough:346-347). This unit carries the clause `dormancy disposal`: a proposal naming each
dormant build, a disposal that moves a build only on the owner's disposition record, and the views
showing the disposed state where they showed `dormant`. The one threshold stays `LIVE_DORMANT_DAYS`
(I13).

## 2. Scope (IN)

- **S1** — The disposed states. `derive_activity(builds, conf, reading)` in
  `tools/memory-tree/gen_build_index.py` (TOOL-dRankedPlan-1 S3 extracts it from `render_live`)
  answers, for a live build whose newest `transition` record (TOOL-dDeclaredLoop-3 S2) has `To`
  `paused`, `withdrawn` or `superseded`, that word, before the date test that answers `active` or
  `dormant` by `LIVE_DORMANT_DAYS`. `LIVE.md`'s `Activity` column and `PLAN.md`'s `Dormant` column
  both print it, since both read this one function. A build with no such record renders as it does at
  base. Observed by AC1.
- **S2** — The proposal. `python tools/memory-tree/gen_build_index.py --dormant` prints one line per
  live build `derive_activity` answers `dormant`, in slug order, `dormant — <slug> · last <date> ·
  <status> · propose pause`, or `dormant — none`, and exits 0; it writes nothing. With
  `LIVE_DORMANT_DAYS` blank it prints `dormant — unmeasured: LIVE_DORMANT_DAYS is blank` and exits 0.
  Observed by AC2.
- **S3** — The disposal. `apply_build_disposal(repo, slug)` in `tools/loop/loop_transition.py`, run
  as `python tools/loop/loop_transition.py dispose --build <slug>`, reads the build's disposition
  records (`record-kind.disposition`, TOOL-dDeclaredLoop-16 S4) added after its newest transition,
  takes the newest whose `Item` and `Disposition` name one of §4's three moves, and records that move
  through `write_transition` (TOOL-dDeclaredLoop-3 S5) with `--from` the state `derive_position`
  answers (TOOL-dDeclaredLoop-7 S1) and `--witness` the commit that added the disposition record. It
  prints the writer's `transition —` line and exits 0. Observed by AC3, AC4.
- **S4** — Held without the owner. With no such record, `dispose` writes nothing and exits 1,
  `dispose — <slug> held: no owner disposition names a move`. A record whose move the build's table
  refuses, as `derive_move` does T11 or T12 past the `pushed` fact, exits 2 naming the row and the
  refusal and writes nothing. A record already applied, its move the build's newest transition,
  prints `dispose — <slug> exists` and exits 0. Observed by AC4, AC5.
- **S5** — The hand-off to the Maintain cadence. The safe fix `maintain.fixes` names `defer dormant`
  (v2:1321), owned by dTendedCadence, this build's child. Its two halves are S2's proposal and S3's
  disposal, and the name is handed to dTendedCadence as the ask in §8 F3. Observed by AC6.
- **S6** — The docs: `help/plan.md` (TOOL-dRankedPlan-16 S9) gains a section "Dormant builds" naming
  `LIVE_DORMANT_DAYS`, `--dormant`, the three moves with the record each takes, and `dispose`.
  Observed by AC7.

## 3. Non-goals (OUT)

- A second threshold, or a clock: `LIVE_DORMANT_DAYS` and the newest record date in the tree stay the
  one anchor (`render_live`, `tools/memory-tree/gen_build_index.py:2083-2110`).
- The `life.request` command the owner pauses a build with, and its guard: dWellOiledMachine's
  (flow-steps.md:684). S3 applies the owner's record; it never writes one.
- Running the cadence that proposes disposals: dTendedCadence's `maintain.fixes`.
- Deciding for the owner: nothing here writes a disposition record or moves a build the owner has
  not disposed, and the proposal is a proposal.
- The live-build mapping: TOOL-dRankedPlan-5's, which reads this unit's proposal.
- The move rows themselves: B19 and B20 (TOOL-dDeclaredLoop-13), T11 and T12 (TOOL-dDeclaredLoop-15).

### Edges

- **consumes-from** `TOOL-dRankedPlan-1` — `PLAN.md`, whose `Dormant` column S1 fills with the disposed state, and `derive_activity`, the one dormancy derivation that unit extracts from `render_live`
- **hands-off** `TOOL-dRankedPlan-5` — `LIVE_DORMANT_DAYS`, the one threshold, read through `gen_build_index.py --dormant`, by which the mapping names the dormant builds whose track it confirms
- **consumes-from** external — dDeclaredLoop, built before this build run: `write_transition` and `loop_transition.py record` (TOOL-dDeclaredLoop-3 S5), the `transition` record kind (-3 S2), `derive_move` and rows B19, T11 and T12 (-13 S5, -15), `derive_position` (-7 S1), and the disposition record (-16 S4)
- **hands-off** external — dTendedCadence: `maintain.fixes`' `defer dormant`, S2 and S3 its two halves, by the ask of §8 F3
- **consumes-from** `TOOL-dRankedPlan-24` — `read_item_disposition`, the one bounded reader S3's `read_build_disposition` is built on, so its "added after its newest transition" rule is spelled once (round-1 spec audit, id 21)
- **hands-off** `TOOL-dRankedPlan-29` — the `paused`, `withdrawn` and `superseded` Activity words, which that unit's S4, S20 and S21 read (round-1 spec audit, ids 8, 24, 33)

## 4. Design

### Evidence

- `render_live` labels a build `dormant` when no record of it is dated within `LIVE_DORMANT_DAYS` of
  the newest record date in the tree (`tools/memory-tree/gen_build_index.py:2083-2110`), from
  `derive_last_record` (:1908), which reads the build's tracked record filenames among its sources.
  `.memory-tree.conf:1034` sets the threshold to 21.
- At base `memory/LIVE.md` lists 46 live builds, 22 of them `dormant`: 7 `INPROGRESS`, 7 `SPECCED`,
  4 `DEFERRED`, 3 `OPEN`, 1 `BLOCKED`. A build leaves `LIVE.md` only when every unit is terminal, and
  `DEFERRED` is not terminal (`tools/memory-tree/tree_lib.py:28-31`), so flipping headers to
  `DEFERRED` disposes nothing: 4 dormant builds are already `DEFERRED`.
- The drift signal `live_builds_without_activity` (`tools/drift-audit/drift_report.py:3479`) reports
  the same rows and moves nothing.
- The only standing move of an open build that is not a step's exit is B19, `@open` by
  `item.life.request` `pause` to `paused`, undone by B20 (TOOL-dDeclaredLoop-13:154-155). T11 and T12
  end an open build `withdrawn` or `superseded`, each `when before-push` (TOOL-dDeclaredLoop-15:104-105).

### The three moves

| Disposition record | Move | Row | View cell |
|---|---|---|---|
| `**Item:** item.life.request`, `**Disposition:** pause` | `@open` to `paused` | B19 | `paused` |
| `**Item:** item.life.close`, `**Disposition:** withdrawn` | `@open` to `withdrawn`, before push | T11 | `withdrawn` |
| `**Item:** item.life.close`, `**Disposition:** superseded`, `**Reason:** by <slug> · …` | `@open` to `superseded`, before push | T12 | `superseded` |

The disposition record sits in the disposed build's `build/` folder, named under the build's first unit
id as TOOL-dDeclaredLoop-16 §4 states for a build-level owner item. `pause` is the safe fix the
proposal names, since B20 resumes the build in the state it paused in and nothing is lost. A resumed
build's newest transition is the resume, so S1 measures it by date again.

### The proposal

```
dormant — dFixA · last 2026-09-03 · INPROGRESS · propose pause
dormant — dFixB · last 2026-09-11 · OPEN · propose pause
```

The proposal and the disposal never share state: the proposal reads the views' derivation, and the
disposal reads only the build's records and the loop's position.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `--dormant` | verb of `gen_build_index.py` | none |
| `render_dormant_proposal` | function, `gen_build_index.py` | `py.function`, asked at the pass |
| `dispose` | verb of `loop_transition.py` | none |
| `apply_build_disposal`, `read_build_disposition` | functions, `loop_transition.py` | `py.function`, asked at the pass |
| `DISPOSAL_MOVES` | constant, `loop_transition.py`: the three rows of the table above | none |
| the plants `dormant-proposal`, `dormant-paused`, `dispose-pause`, `dispose-held`, `dispose-pushed`, `dispose-exists` | fixture cases | none |

### Migration

None. A build with no disposal renders as at base, so `LIVE.md` and `PLAN.md` keep their bytes until
the first disposal is recorded.

### Rollout

Live at landing. Nothing proposes or disposes on its own: the owner runs `--dormant`, writes a
disposition record for each build they dispose, and runs `dispose`; dTendedCadence's cadence takes
the proposal over when it lands.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`: S1's disposed states in `derive_activity`, S2's `--dormant`, the plants
- `tools/loop/loop_transition.py`: S3 and S4, `dispose` and its plants
- `help/plan.md`: S6's section

### Alternatives rejected

- **Flipping the build's unit headers to `DEFERRED`.** `DEFERRED` is a live status, so the build stays
  labelled `dormant` and the label returns; it also rewrites another build's specs.
- **A new `@open` to `deferred` row.** It needs a row TOOL-dDeclaredLoop-13 does not hold, a parent
  surface, where B19 already parks a build reversibly.
- **Disposing in the generator.** The generator writes views and never moves state; a disposal is a
  transition, so it goes through `write_transition`, the one writer of a move.

## 5. Production-readiness checklist

- security — `dispose` writes a move only on a disposition record the owner leaves, the trust model of
  every owner gate (TOOL-dDeclaredLoop-19 S6); an agent-written record is the forgery class that
  model accepts until dWellOiledMachine's guarded `life.request` command lands. The slug is read
  against the build folders, never joined into a path unchecked.
- perf / scale — `derive_activity` reads one newest `transition` record per live build from the
  record list the generator already holds; `dispose` touches one build.
- error / empty / loading states — S4's three exits; `dormant — none` and `dormant — unmeasured`.
- observability — every move prints the writer's `transition —` line; the views show the state.
- risks — under a `transitions.record` value without `log`, no transition record file exists and S1
  cannot see a disposal, since the generator reads no git history; `dispose` then prints one `NOTE:`
  naming `transitions.record`.
- testing — the six plants, red and green.
- migration — none.
- user docs — `help/plan.md`, S6.

## 6. Acceptance criteria

- **AC1** — When `python gen_build_index.py --dormant --plant dormant-paused` renders a fixture with
  `LIVE_DORMANT_DAYS="21"`, a build whose last record is 30 days old and whose newest `transition`
  record reads `To: paused` shows `paused` in `PLAN.md`'s `Dormant` column and `LIVE.md`'s `Activity`
  column, and a second build 30 days old with no transition shows `dormant` in both.
  Red when: a paused build reads `dormant` or `active`, or the two views disagree.
- **AC2** — When `python gen_build_index.py --dormant --plant dormant-proposal` runs, it prints
  `dormant — <slug> · last <date> · <status> · propose pause` for the 30-day build only and exits 0,
  and with `LIVE_DORMANT_DAYS` blank it prints `dormant — unmeasured`.
  Red when: an active or paused build is proposed, or a blank key proposes anything.
- **AC3** — When `python loop_transition.py --fixture --plant dispose-pause` adds the owner's
  disposition record `Item: item.life.request`, `Disposition: pause` to a dormant fixture build and
  runs `dispose --build tFix`, one transition record `From: <state> · To: paused` is written, its
  witness the record's commit, and the generator's `--dormant` no longer names `tFix`.
  Red when: the move is not recorded, or the build is still proposed.
- **AC4** — When the plant `dispose-held` runs `dispose --build tFix` with no disposition record, and
  again with a record older than the build's newest transition, each exits 1 printing `held: no owner
  disposition` and writes no transition.
  Red when: a build moves without a fresh owner disposition.
- **AC5** — When the plant `dispose-pushed` gives a build whose `pushed` fact holds a record
  `Disposition: withdrawn`, `dispose` exits 2 naming T11 and the refusal; and the plant
  `dispose-exists` re-runs `dispose` after AC3's move and prints `exists`, exit 0, writing nothing.
  Red when: a refused move is written, or a second run writes a second transition.
- **AC6** — When `grep -n "defer dormant"` runs over this spec's §8, it finds F3's ask naming
  `--dormant` and `dispose`, and the main loop's filed ask row in dTendedCadence's `BACKLOG.md`
  carries the same accept line.
  Red when: the safe fix's name is handed to nobody.
  permission: the ask row is filed by the main loop after the writers return, not by this pass.
- **AC7** — When `grep -n "Dormant builds" plan.md` runs over the help page, it finds S6's section
  naming `LIVE_DORMANT_DAYS`, `pause`, `withdrawn`, `superseded` and `dispose`.
  Red when: the section is absent or omits a move.

## 7. Gates

`build-index selftest` · `tier2-review self-test` · `policy fixtures` · `memory hygiene` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 · the `dormant-paused` and `dormant-proposal` plants in its selftest, the failing case a paused build labelled `dormant` · none

New arm: tools/loop/loop_transition.py · covers AC3 AC4 AC5 · the four `dispose-*` plants beside TOOL-dDeclaredLoop-3's, run by that unit's `loop transition record` leg, the failing case a move written with no owner disposition · none

## 8. Open questions

- **F1 — What move disposes a dormant build?** Options: (a) B19 `pause` as the proposal, with T11
  `withdrawn` and T12 `superseded` open to the owner's record; (b) flip the build's unit headers to
  `DEFERRED`, the walkthrough's word; (c) a new `@open` to `deferred` row asked of dDeclaredLoop. (b)
  leaves the build live and labelled `dormant`, so it fails the clause; (c) changes a parent's table
  where (a) already holds the move. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most
  feature-rich survivor: reversible by B20, and the owner may end a build outright where the table
  admits it; walkthrough:346's "deferred" is read as the loop's reversible park. widens: none ·
  relaxes: none
- **F2 — Is the disposer built here, or left to dTendedCadence's `maintain.fixes`?** Options: (a)
  here, with the safe fix's name handed on; (b) there, leaving this clause's owned gap open until the
  child lands. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3: (b) closes no gap in this build
  and the child reads its parent's verbs. widens: none · relaxes: none
- **F3 — Ask for dTendedCadence: the safe fix `defer dormant`.** Target build: dTendedCadence. Accept:
  `maintain.fixes`' `defer dormant` runs `gen_build_index.py --dormant` and proposes each named build
  to the owner, and applies `loop_transition.py dispose` only to a build holding the owner's
  disposition record, seen on a fixture with one dormant build proposed and one disposed. The main
  loop files it once after the writers return. RESOLVED (agent, 2026-10-26, delegated): stated here as
  the hand-off of S5, rung 1, v2:1321 naming `defer dormant` among dTendedCadence's safe fixes.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 4, walkthrough:346-347, v2:1321,
  TOOL-dDeclaredLoop-13 B19 and B20, TOOL-dDeclaredLoop-15 T11 and T12, TOOL-dRankedPlan-1 S3, and
  scout B's row -4.
- rev-2 · 2026-10-27 · §3 · gains the consumes-from edge to `TOOL-dRankedPlan-24`, the hands-off edge to `TOOL-dRankedPlan-29`, each the reciprocal of that promoted unit's own edge (round-1 spec audit, `reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are `derive_activity`, the dormancy derivation TOOL-dRankedPlan-1 S3 extracts
from `render_live` (`tools/memory-tree/gen_build_index.py:2079`), and TOOL-dDeclaredLoop-3's
`loop_transition.py` with `write_transition`, the one writer of a move, beside the disposition record
of TOOL-dDeclaredLoop-16. `python tools/codebase-map/reuse_lookup.py "dispose a dormant build past
the activity threshold by an owner ratified move"` ranked name stems (`build`, `build_commit`,
`owners_of`); none disposes a build, so no existing seam fits the disposal and S3 adds it to the
transition writer's own CLI. Scout B cited `verb_rescope … defer` (`tools/unattended/unattended.sh:13300`):
it defers a unit inside a run that holds a live `RUN.md`, and a dormant build has none, so it does not
fit. The drift signal at `tools/drift-audit/drift_report.py:3479` stays report-only. The recall query
returned TOOL-aMendedFleet-12 and -54, the units that made dormancy a label and a drift count, and
TOOL-dRankedPlan-1's extraction of `derive_activity`, which this unit reads; source agrees with each.

Recall terms used: `python tools/memory-recall/query.py "how is a dormant build disposed rather than only labelled dormant" --terms "dormant build LIVE_DORMANT_DAYS render_live activity label pause defer disposition owner safe fix maintain.fixes"`
