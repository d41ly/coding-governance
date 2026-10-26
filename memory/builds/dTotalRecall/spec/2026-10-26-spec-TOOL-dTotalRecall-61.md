# TOOL-dTotalRecall-61 — unit 53 keeps the build-folder rows of its two file-keyed constants through its own pass, so no keep it needs lands after it

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 19 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 |
| [2026-10-26-build-TOOL-dTotalRecall-61-round4-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-61-round4-fix-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-61-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-61-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-61-round4-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-61-round4-fix-brief.md) | research | — |
| [2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-62 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 54 to 60
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item. `TOOL-dTotalRecall-53`
(order 29) S34 makes the file-keyed constants `CAUSE_WRITER_KEPT` and `ALIAS_COMPARE_KEPT` give way
to an in-file marker, and its AC34 requires both gone at its own tip. Their build-folder rows cannot
take a marker: unit 50 §4 keeps eight build-folder scripts by `CAUSE_WRITER_KEPT`, and S22 keeps the
pinned `deviations.py:380` compare. The path-keyed table that holds them instead lands with
`TOOL-dTotalRecall-55` and `TOOL-dTotalRecall-56` at order 30, one step after unit 53's pass. So
at unit 53's tip those hits have no keep. Writing a marker into them moves pinned blobs and stops
the run at `packet.py --check` (README:38-39); not writing one leaves 53's AC22, AC28, AC34 and AC35
red at its own pass, and no later step can make that pass green.

The defect sits in the hand-off from unit 50's keep, the eight rows it writes at order 18, to unit
53's retirement. This unit amends the four specs that hand-off runs through, at the step after unit
50 and long before unit 53's pass: unit 53 keeps each build-folder row in its constant, and units 55
and 56 move those rows to the table and end the constants. Unit 53's own pass then needs nothing
that lands after it. It repairs `TOOL-dTotalRecall-50`.

## 2. Scope (IN)

- **S1** — Unit 53 keeps the build-folder rows. `TOOL-dTotalRecall-53` S34, S22 and AC34 take §4's
  text: the two constants give way to the marker for every file under the tool root, and each row
  naming a file under `memory/builds/*/build/` stays in its constant through unit 53's pass. Its two
  hands-off lines to units 55 and 56 say so. Observed by AC1 and AC2.
- **S2** — Units 55 and 56 end the constants. `TOOL-dTotalRecall-55` S2 moves the eight cause rows,
  the last of `CAUSE_WRITER_KEPT`, into its table, and `TOOL-dTotalRecall-56` S2 moves the
  `deviations.py` alias row, the last of `ALIAS_COMPARE_KEPT`, so each constant ends at that unit's
  pass. Each gains the criterion that observes it. Observed by AC1 and AC3.
- **S3** — Unit 57 follows unit 56. `TOOL-dTotalRecall-57`'s AC2 reads both constants gone, so its
  §3 gains a consumes-from edge to unit 56, mirrored in 56's §3, and its §4 sequencing line names
  both units. Observed by AC3.
- **S4** — The amendments land before their units build. Each is a rev bump with its §9 line naming
  this unit, committed in this unit's pass at order 19. Observed by AC1.

## 3. Non-goals (OUT)

- The keep table, its accessor and its drain: `TOOL-dTotalRecall-55`'s, with the batch
  `TOOL-dTotalRecall-66` re-keying the drain.
- Moving units 55 or 56 to order 29. A reorder written mid-run changes no roster the harness already
  handed out, so the narrowing is the route that needs no reorder.
- Any code. This unit writes spec text only; the code it describes is units 53, 55 and 56's.
- Editing a build-folder script or moving a pin: the owner's.

### Edges

- **consumes-from** `TOOL-dTotalRecall-50` — the eight build-folder rows of `CAUSE_WRITER_KEPT` its §4
  writes, which this unit keeps standing through unit 53's pass
- **hands-off** `TOOL-dTotalRecall-53` — S34, S22 and AC34 amended so the build-folder rows of
  `CAUSE_WRITER_KEPT` and `ALIAS_COMPARE_KEPT` stay in their constants through that unit's pass
- **hands-off** `TOOL-dTotalRecall-55` — S2 amended so its pass moves the last rows of
  `CAUSE_WRITER_KEPT` into its table and ends the constant
- **hands-off** `TOOL-dTotalRecall-56` — S2 amended so its pass moves the last row of
  `ALIAS_COMPARE_KEPT` into the table and ends the constant
- **hands-off** `TOOL-dTotalRecall-57` — a consumes-from edge to unit 56, since its AC2 reads both
  constants gone
- **hands-off** `TOOL-dTotalRecall-67` — the amendments of §4 to units 55, 56 and 57, which that unit reads by their own text at step 20 and writes where this pass left one out (the round-1 audit of units 61 to 66, id 1)
- **hands-off** `TOOL-dTotalRecall-70` — AC2 and AC3 as built, which that unit re-reads by their own commands and by ancestry at the tip (the round-1 audit of units 61 to 66, ids 8 and 12)

## 4. Design

### The amendments

Each block below is the text the pass writes, as a rev bump on that spec with a §9 line of the form
`rev-<N> · <date> · S34 S22 AC34 §3 · amended by TOOL-dTotalRecall-61 (id 1, item H1) ...`.

Unit 53 S34, its first sentence kept and the rest reading:

> The file-keyed constants `ALIAS_COMPARE_KEPT` and `CAUSE_WRITER_KEPT` give way to it for every file
> under the tool root, each such kept line marked with the reason the constant held. A row naming a
> file under `memory/builds/*/build/` stays in its constant at this pass, because no pass may write
> that file's bytes: unit 50 §4's eight cause rows and S22's alias row. `TOOL-dTotalRecall-55` and
> `TOOL-dTotalRecall-56` move them to the path-keyed table, and each constant ends there.

Its **Readers:** clause is kept as written.

Unit 53 S22, the keep clause reading: "the pinned `deviations.py` `!= "journal"` (`:380`) is kept by
an `ALIAS_COMPARE_KEPT` row with the reason `pinned instrument`, never by a marker in its bytes, until
`TOOL-dTotalRecall-56` moves that row to the path-keyed table".

Unit 53 AC34:

> When a `python -c` probe reads `CAUSE_WRITER_KEPT` and `ALIAS_COMPARE_KEPT` at the tip, every row
> names a file under `memory/builds/*/build/`, and `git grep -c "census: kept"` over those files
> prints nothing; an unmarked writer added to a kept file under the tool root reds
> `record_causes.py --check`. Red when: a row naming a file under the tool root survives, or a
> build-folder file carries the marker.

Unit 53's hands-off lines to units 55 and 56 read "which S34 leaves in `CAUSE_WRITER_KEPT`" and
"which S34 leaves in `ALIAS_COMPARE_KEPT`" where they now read "which S34 does not mark".

Unit 55 S2 gains: "The eight rows move out of `CAUSE_WRITER_KEPT`, whose last rows they are after
unit 53, so the constant ends at this pass." Its AC1 gains: "and
`git grep -n CAUSE_WRITER_KEPT -- tools` prints nothing". Its consumes-from line to unit 53 reads
"S34's marker, which leaves `CAUSE_WRITER_KEPT` holding only the build-folder rows this unit moves".

Unit 56 S2 gains: "The row moves out of `ALIAS_COMPARE_KEPT`, whose last row it is after unit 53, so
the constant ends at this pass." It gains the criterion "When `git grep -n ALIAS_COMPARE_KEPT -- tools`
runs at the pass tip it prints nothing. Red when: the constant survives." Its §3 gains the hands-off
to unit 57, and unit 57's §3 the consumes-from to unit 56; unit 57 §4's sequencing line reads "this
one follows units 55 and 56".

### Why order 19

The amendments touch nothing a pass between step 19 and step 29 reads, and they must precede unit
53's pass. Step 19 is one above unit 50, the unit whose keep they carry.

### Inventory

Minted: nothing in code. Amended: the four spec files below.

### Files touched (estimate)

- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-53.md`
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-55.md`
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-56.md`
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-57.md`

### Alternatives rejected

- **Order units 55 and 56 at 29, ahead of unit 53.** The skeptic's first option. It moves two order
  verbs mid-run, and the roster the build run starts from is not re-derived by a pass.
- **Place this repair at order 30, after unit 53.** Unit 53's criteria are red at its own pass, the
  placement H1 faults.
- **Unit 53 builds the table itself.** Units 55 and 56 already design it, and two units designing one
  body is H3's defect.

## 5. Production-readiness checklist

- security — no surface: spec text only.
- perf / scale — none.
- error / empty / loading states — none at runtime; a missing amendment is AC1's red.
- observability — each amended spec's §9 line names this unit and the finding.
- risks — the amended specs' revs move after their audit; their new text is this spec's §4
  verbatim, which the audit of this unit reviews.
- testing — AC1 by the pass; AC2 at unit 53's pass; AC3 at unit 57's pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `grep -n "stays in its constant at this pass"` runs over
  `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-53.md` at this pass's tip it
  prints S34's line, and `grep -c TOOL-dTotalRecall-61` over the §9 of units 53, 55, 56 and 57 prints
  at least 1 for each.
  Red when: a spec §4 names is unamended, or its rev bump has no §9 line.
- **AC2** — When unit 53's pass tip is reached, `python record_causes.py --check` run from
  `tools/memory-tree/` exits 0 with the eight build-folder files kept by `CAUSE_WRITER_KEPT`,
  `check_alias_compares` lists `deviations.py:380` kept `pinned instrument`,
  `python record_causes.py --cause-writers` prints every census file with a disposition, and
  `git log --no-merges --first-parent --name-only 462d20f3..HEAD -- 'memory/builds/*/build/*.py'`
  prints no path.
  Red when: unit 53's AC22, AC28, AC34 or AC35 is red at its own tip, or a pass wrote a build-folder
  script.
- **AC3** — When unit 57's pass tip is reached, `git grep -nE "ALIAS_COMPARE_KEPT|CAUSE_WRITER_KEPT" -- tools`
  prints nothing, and `git log --format=%s` lists unit 56's pass commit before unit 57's.
  Red when: either constant survives step 30, or unit 57 builds before unit 56.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: this unit writes spec text, and the criteria it amends carry their units' own arms.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 54 to 60, id 1
  (HIGH, item H1).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-67, TOOL-dTotalRecall-70, each the other end of an edge a unit the round-1 spec audit of units 61 to 66 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is the pair of file-keyed constants already in the design, `CAUSE_WRITER_KEPT`
(`TOOL-dTotalRecall-36` S7, rows from unit 50 §4) and `ALIAS_COMPARE_KEPT` (`TOOL-dTotalRecall-40`),
kept one step longer, and unit 55's path-keyed table, which receives their last rows. No mechanism is
minted. `python tools/codebase-map/reuse_lookup.py "amend a sibling spec before its unit builds"`
ranked name-stem neighbours (`before`, `build`, `units`) and no seam for sequencing an amendment, so
no existing seam fits beyond the constants and the table named here.

Recall terms used: `python tools/memory-recall/query.py "how does a repair land before the unit whose own pass it must make green" --terms "order repair promoted spec-audit step hands-off consumes-from amendment rev-bump pass tip supersede"`
