# TOOL-cSpliceWarden-4 — the archive repair: superseded, evacuated, and fifteen rows re-homed

**Status:** CLOSED · rev-2 · 2026-09-13 · node c · Tier-1 · base 09a22d2b · streams tooling · order 3 · ratified 2026-09-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-cSpliceWarden-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-cSpliceWarden-1-acceptance-ledger.md) | journal | TOOL-cSpliceWarden-1 TOOL-cSpliceWarden-2 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-5 |

<!-- /gen:spec-records -->

## 1. Goal

Make `memory/archive/TOOL.2026-08-17.md` true. Its header claims terminal rows only; it holds 90 rows
of which 66 are not. Prepend a supersession note stating every false claim, evacuate the rows that do
not belong under `cut`, and re-home the fifteen whose only surviving row is a stale OPEN about work
that closed a month ago.

## 2. Scope (IN)

- **S1** — a supersession note at the top of the archive, stating each false claim and quoting every
  removed row verbatim. Observed by **AC1**.
- **S2** — the evacuation: 49 rows the live shard already owns are deleted, 2 stale duplicate halves
  are deleted, 15 rows are moved out, 24 terminal rows survive. Observed by **AC2**.
- **S3** — the 15 re-homed rows land in `memory/backlog/TOOL.md` with status CLOSED and the BODY
  recovered from `origin/main`'s history, not the archive's stale body. Observed by **AC3**.
- **S4** — the archive's own header rewritten to claim only what survives, and
  `memory/backlog/TOOL.md`'s 2026-08-17 rotation note replaced, naming `TOOL.2026-08-17b.md` as the
  second archive of that date. Observed by **AC4**.

## 3. Non-goals (OUT)

- Editing `memory/archive/TOOL.2026-08-17b.md`. The audit found that 17 of its 23 rows are
  byte-identical duplicates of rows in `TOOL.2026-08-17.md`, so the archive PAIR does not reach
  cut-clean even after this repair. That is a real finding, it is outside the owner's scope of
  2026-09-12, and it is filed rather than fixed. The corrected header therefore must NOT claim
  exclusivity.
- Editing `TOOL.2026-08-14.md` or `DECISIONS.2026-08-10.md`. Both audited clean.
- Merging archive-side prose into a live row. Seven rows agree on status and differ in wording; the
  archive copy is deleted, and if any carried a fact the live row dropped, that is a small and stated
  information loss. Statuses were compared, sentences were not.

### Edges

- **hands-off** `TOOL-cSpliceWarden-3` — this unit must land FIRST, or the widened check 20 counts 5
  duplicates against an exact-match pin of 3.
- **hands-off** `TOOL-cSpliceWarden-2` — this unit adds the `TOOL.2026-08-17b.md` reference that
  unit's check reds on.

## 4. Design

### The partition — derived, and it corrects the brief

The brief scopes "17 archive-only ids". As IDS that is right. As ROWS it is 15, and the difference is
load-bearing. `TOOL-aBranchedMandate-2` and `-3` appear in the archive TWICE each: SPECCED at lines
86-87 and CLOSED at 94-95. They are simultaneously "archive-only and non-terminal" and "the stale
duplicate pair", so the brief's set (a) and set (c) overlap on exactly those two rows. Re-homing them
as SPECCED would plant two fresh cross-file status contradictions in a build whose entire subject is
cross-file status contradictions — and check 20 is per-file, so nothing would catch it.

Their CLOSED rows at 94-95 are correct and terminal, so under `cut` they belong exactly where they
already are. Nothing is re-homed for those two ids; only the stale halves are dropped.

| set | rows | disposition |
|---|---|---|
| live shard already owns the id | 49 | delete from the archive |
| archive-only, non-terminal, no terminal twin | 15 | re-home to `memory/backlog/TOOL.md` |
| stale half of an in-file duplicate pair | 2 | delete; the CLOSED twin survives |
| terminal survivors | 24 | keep |

49 + 15 + 2 + 24 = 90, verified as an exact partition with no row in two sets and none in none.

### The re-homed rows carry a recovered body, not the archive's

All 15 grade CLOSED — established twice over, from each id's spec status header and from the closing
commit on `origin/main`'s ancestry, agreeing in every case. The archive preserves the PRE-close body:
a closing commit often rewrote the sentence as well as the token, and 4 of the 15 differ. Re-homing
the archive text verbatim would re-assert claims the tree refutes — `TOOL-aStandingWrit-3`'s archive
body says the unattended instruction layer "is unowned in this tree", and `BUILD-METHOD.md` has
existed since. So each row is written with the body from its closing commit.

**Why the live shard and not a corrected token in place.** A row's status is owned where it can still
be corrected. Writing a re-derived status into an archive freezes it in a file that by definition is
never updated again; if the derivation is ever found wrong, there is nowhere to fix it. The live
shard is the right home for a row whose status this build has just re-derived, and a later rotation
under `cut` will move it out properly.

### The supersession note is PROSE, never a row

It is written as a blockquote. A dash-led line carrying an id would become a ROW under unit 3's
widened check 20 and join the file's id set — a supersession note that keys as a backlog row is a new
defect wearing the repair's clothes.

### Files touched (estimate)

`memory/archive/TOOL.2026-08-17.md` · `memory/backlog/TOOL.md`.

## 5. Acceptance criteria

- **AC1** — When the archive is read after S1, its note names all three false header claims and quotes
  the two dropped `TOOL-aBranchedMandate` rows verbatim, and `python tools/memory-tree/row_grammar.py --report`
  keys no row from the note.
  Red when: the note is written with a leading dash and an id, which would key as a row.
- **AC2** — When `python tools/memory-tree/row_grammar.py --report` re-parses the archive, it holds
  24 rows, all terminal, with zero duplicate ids.
  Red when: the count is not 24, which means the partition was applied wrongly.
  figure: DERIVED — the criterion re-parses the file.
- **AC3** — When `grep -c '· CLOSED ·' memory/backlog/TOOL.md` is compared before and after, it rises
  by exactly 15, and each re-homed row's body equals the closing commit's body.
  Red when: any re-homed row carries OPEN, or the archive's stale body.
- **AC4** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs with unit 2's check 10 in
  place, it reports no check-10 finding.
  Red when: `TOOL.2026-08-17b.md` is still referenced from nowhere.

## 6. Gates

`memory hygiene` · `memory-hygiene self-test` · `row-grammar selftest`

## 7. Open questions

- **F1 — the archive pair still overlaps.** After this repair, 17 of the 24 surviving rows are still
  byte-identical rows of `TOOL.2026-08-17b.md`. RESOLVED (agent, 2026-09-12, delegated): out of the
  owner's ratified scope; filed as a backlog row, the corrected header does not claim exclusivity,
  and the wrap-up names it.

## 8. Revision log

- rev-1 · 2026-09-12 · the first draft.
- rev-2 · 2026-09-13 · §4 · AC2 — the four-way partition and the (a)/(c) overlap written in after deriving it; AC2 given a backticked witness
