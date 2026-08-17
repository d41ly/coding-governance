# TOOL-cBriefedPilot-20 — the records this build leaves, and one row it should not have had to close

**Status:** CLOSED · rev-3 · 2026-08-16 · node c · Tier-1 · base 37c05e1b · streams tooling

## 1. Goal

Leave the tree's records describing the tree: two dossiers re-derived rather than carried forward,
every backlog row this build closes closed, one stale row retired with the evidence that it was
already owned, and the charter's own count of what the kit's leg checks brought back into agreement
with the leg.

## 2. Scope (IN)

- **S1** — `memory/map/features/unattended.md`: the Gaps section re-derived against the tree. The
  "shipped protocol's version marker is not paired by any gate" gap is struck by unit 17, and the
  directive layer changes what the kit IS, so the Constraints section gains it.
- **S2** — `memory/map/features/build-method.md`: Gaps re-derived. The headroom figure is re-measured
  after units 15 and 16 spend it, and the "unattended-side pointers are conditional prose" gap
  narrows to the half that survives — the Skill's step 0 is unconditional after unit 9 and
  `--preflight` refuses an absent carrier after unit 4, while `verb_resume`'s echo is still guarded
  by `[ -f "$M/guides/BUILD-METHOD.md" ]`.
- **S3** — `memory/backlog/TOOL.md`: every `TOOL-cBriefedPilot-*` row to its terminal token, EXCEPT
  `TOOL-cBriefedPilot-23`, which stays OPEN. That row is the residual unit 1's §8 filed on 2026-08-15
  when M3 veto 1 discarded the shared newline refusal: unit 3 closes the `--waive` half only, and the
  `override` and `abort` park kinds keep the hole. Closing it here would silently undo the veto;
  `TOOL-cFinalBerth-3` CLOSED against unit 17; `TOOL-aStandingWrit-3` CLOSED as STALE, naming
  `aWrittenMethod` as what owned the instruction layer and this build as what made it default.
- **S4** — `memory/DECISIONS.md` rows for the decisions this build minted that outlive it: the
  registry is a kit constant and not a conf key, a waiver is taken at preflight and nowhere else, and
  the contract names zero handles.
- **S4b** — a `memory/DECISIONS.md` row for unit 21's recorded verdict token, whichever branch it
  names. The token decides unit 15 and unit 16's index count, so a build that leaves it only in a
  review recording leaves the next run to re-derive a decision this one made. Stated conditionally so
  branch A and branch B each have a home.
- **S5b** — a second NEW backlog row carrying the per-route "one thing that would have to change"
  from unit 21's recording, so a route the hunt rejected is re-openable on evidence rather than
  re-argued from scratch.
- **S5** — the F4 read-budget finding filed as a NEW backlog row, MEASURED at close in this tree and
  not copied. Today the charter's fixed read path is 68,989 B across six files against a
  `READ_PATH_CEILING` of 86,476; the RECURRING cost — M7 re-reading the method whole at every pass
  boundary — is counted by nothing. Measured, not built.
- **S6** — `AGENTS.md`'s unattended bullet, VERIFIED rather than moved. Units 12, 13 and 14 each add
  one check and each move the count by one, fifteen to sixteen to seventeen to eighteen; unit 22 adds
  arms D and E to check 16 and moves a clause, not a number. This unit re-reads the bullet against
  `check-unattended.sh`'s own header after all four have landed, corrects any residue, and confirms
  the enumeration names checks 16, 17 and 18 and what unit 22's join now covers.

## 3. Non-goals (OUT)

- **Building anything the measurement suggests.** S5 files a number. A per-pass read budget is a
  design with its own veto to survive, and M3's veto 2 plus plain YAGNI keep it out of this build.
- **Any dossier `[claims]` edit.** Measured: this build adds no gate leg, kit, git hook, workflow
  script, skill engine, rendered skill, guide or backlog shard. Leg checks 16, 17 and 18 are checks
  INSIDE `tools/unattended/check-unattended.sh`, which `unattended kit gate` already runs and
  `unattended.md` already claims. So the four-gates-at-once hazard a new leg trips does not fire
  here, and `tools/gate-legs.json` takes no edit.
- **Closing `TOOL-aStandingWrit-6` and `-7`.** The leg's own anchor independence and the absence of
  any binding between executing kit code and code an owner approved are untouched by this build and
  are named in the protocol's §9.
- **Editing the design pass recording.** It is a dated record of what a panel returned. Its
  corrections live in the specs that supersede it, not in it.

## 4. Design

### Why the dossiers are re-derived and not amended

`memory/map/features/unattended.md` says it in its own Gaps preamble: dossier PROSE is ungated — only
the `[claims]` tables are — so the section rots silently and is worth re-deriving whenever the feature
is touched. It has already carried three stale claims at once. Amending the two lines this build
falsifies would leave the rest carried forward on trust.

### The stale row, and why it is worth its own sentence

`TOOL-aStandingWrit-3` says the unattended instruction layer "is unowned in this tree: no branch,
worktree, build or row named it on 2026-08-11". Measured: `memory/builds/aWrittenMethod/README.md`
reads CLOSED with six units, and the layer it built is `memory/guides/BUILD-METHOD.md`. The row was
true when written and false the next day, and nothing looked. It closes naming the build that owned
it, not this one — a row that closes against the wrong build is how a second false claim replaces a
first.

### What the map gate can still catch here

One route only. If the closing review left-shifts a finding into a new `memory/gotchas/` class, that
class becomes a new inventory key: it needs an `INDEX.md` re-render and a claim in some dossier, or
`codebase-map coverage + freshness` reds. Named because it is the single way this build reaches the
map, and it is not knowable until the review runs.

### Files touched (estimate)

`memory/map/features/unattended.md` · `memory/map/features/build-method.md` ·
`memory/backlog/TOOL.md` · `memory/DECISIONS.md` · `AGENTS.md` · the generated
`memory/map/gen/` artifacts by re-render, never by hand.

### Alternatives rejected

Giving this unit the COUNT as well as the verification. That was the first draft, and it loses: the
count is not unassigned — units 12, 13 and 14 each carry the same bullet in their own files-touched,
one check each, and the README's own ordering constraint says nothing may land in a state a later
unit repairs. A charter that reads fifteen for six units while the leg reads eighteen is exactly that
state. What is genuinely unassigned is the RECONCILIATION, because nothing reds in the interval:
`handkept_inventories_disagreeing_with_source` counts gate-leg SCRIPT PATHS the charter does not
cite, is pinned at 0, and reads the manifest rather than the prose, so a stale check count is
invisible to it. A number four units edit in sequence with no gate watching is a number worth reading
once at the end, and that is what S6 is.

## 5. Production-readiness checklist

- security · perf / scale · a11y · i18n · observability — N/A, records.
- error / empty / loading states — N/A.
- risks — the one live risk is a dossier re-derivation that carries a stale claim forward under a new
  date, which is worse than the stale claim alone. Every Gaps bullet is re-checked against the tree
  or deleted.
- testing + left-shift gates — `memory hygiene`, `codebase-map coverage + freshness`,
  `drift-audit records`. None of them reads dossier prose, which is why §4 states the discipline.
- migration / rollback — N/A.
- user docs — the charter bullet in S6 is the user doc for the leg's check set.

## 6. Acceptance criteria

- **AC1** — `python tools/codebase-map/test_codebase_map.py` is green, including the
  generated-artifact freshness re-render.
- **AC2** — `bash tools/memory-tree/check-memory-hygiene.sh` is green with the closed rows, and
  check 20's `ROW_DUPLICATE_PIN` is unmoved at its current value.
- **AC3** — `python tools/drift-audit/drift_report.py --check` is green and
  `handkept_inventories_disagreeing_with_source` is still 0.
- **AC4** — `TOOL-aStandingWrit-3` reads CLOSED and its row names `aWrittenMethod` as what owned the
  layer; `TOOL-cFinalBerth-3` reads CLOSED and names unit 17.
- **AC5** — The F4 row carries a byte figure measured in this tree at close, and names both the fixed
  read path and the recurring cost that nothing counts.
- **AC6** — No Gaps bullet in either dossier claims something a unit of this build closed, checked by
  reading each bullet against the tree rather than against the previous revision.
- **AC7** — `AGENTS.md`'s unattended bullet states the leg's check count as the number
  `check-unattended.sh`'s own header states, and enumerates the three new checks.

## 7. Gates

`memory hygiene (20 checks)` · `codebase-map coverage + freshness` · `drift-audit records` ·
`drift-audit wiring` · `template size ≤32 KiB` (the charter is not the template, but the edit sits
next to it and the leg is unguarded) · the full bar at the push boundary.

## 8. Open questions

none — every fork this build carried was resolved in the build README or in the unit that owned it,
and a records unit inherits no new one. The one judgement made here is S6's ownership of the charter
edit, argued in §4 rather than left open.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Extends that pass's unit 20 with S6, which
  it assigned to nobody, and re-measures the read path it reported at 68,889 B: the figure in this
  tree today is 68,989 B, which is why S5 requires a measurement at close rather than a copy.
- rev-2 · 2026-08-14 · S6 turns from a MOVE into a VERIFICATION, and its §4 alternative is rewritten
  around what the cross-read measured: `AGENTS.md`'s gate-suite bullet is already in the
  files-touched of units 12, 13, 14 and 22, so this spec's premise that the design pass left it
  unassigned was false and its count was wrong twice over — the moves are one per unit, fifteen to
  sixteen to seventeen to eighteen, not one jump by unit 12. Measured: `AGENTS.md:129` and
  `tools/unattended/check-unattended.sh:2` both read fifteen today. What is unowned is the final
  reconciliation, which no gate watches, and that is all S6 now claims.

- rev-3 · 2026-08-15 · §8's audit fold. S3 now EXCLUDES `TOOL-cBriefedPilot-23`, the residual the M3 veto deliberately
  preserved, which S3 would otherwise have closed and silently undone. S4b and S5b give unit 21's
  verdict token a record owner, so the next run reads a decision instead of re-deriving it.

## 10. Reuse audit

- **`memory/map/features/*.md`'s Gaps sections** — the seam extended, and the one this repo has
  already recorded as ungated. The re-derivation discipline is stated in `unattended.md`'s own
  preamble and is followed rather than reinvented.
- **`memory/backlog/TOOL.md`'s row grammar** — one status token leading each row, read by hygiene
  check 8 and by the row-grammar classifier. Closing a row is an edit to an existing row, never a
  second row for the same id.
- **`memory/DECISIONS.md`** — append-only, one row per decision, and on the charter's read path at
  8,460 B, so a row costs read-path budget as well as a line.
- **`tools/memory-tree/gen_build_index.py`** — re-renders `memory/LIVE.md`, the ledger shard and the
  build README's generated region from the spec status headers this build's other units move. No
  hand-edit reaches any of them.

No new seam, and none wanted: a records unit that invents a mechanism is a records unit that has
stopped recording.

Recall terms used: dossier gaps re-derive stale row backlog close instruction layer owned map
coverage claim drift records charter count.
