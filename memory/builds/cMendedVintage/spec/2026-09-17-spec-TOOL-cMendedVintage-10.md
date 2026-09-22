# TOOL-cMendedVintage-10 — a superseded dispatch declaration is not an open pass

**Status:** CLOSED · rev-3 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams tooling · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-TOOL-cMendedVintage-10-acceptance-ledger.md](../build/2026-09-17-build-TOOL-cMendedVintage-10-acceptance-ledger.md) | journal | — |
| [2026-09-17-prompt-TOOL-cMendedVintage-10-2-build-brief.md](../prompts/2026-09-17-prompt-TOOL-cMendedVintage-10-2-build-brief.md) | journal | — |
| [2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md](../reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md](../reviews/2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 DEPL-cMendedVintage-22 DEPL-cMendedVintage-23 DEPL-cMendedVintage-24 DEPL-cMendedVintage-25 DEPL-cMendedVintage-26 DEPL-cMendedVintage-27 DEPL-cMendedVintage-28 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-11 TOOL-cMendedVintage-12 |

<!-- /gen:spec-records -->

## 1. Goal

`check_pass_open` in `tools/unattended/unattended.sh` closes a dispatch row only when a commit naming
that unit WROTE inside that row's own declared set. A unit that re-declares — narrowing because it
discovered it needs fewer files — leaves every earlier row permanently open, because no commit will
ever write inside a set the unit abandoned. Check 49 then refuses every later unit declaring any path
that abandoned row still names. Close a row that a later row for the same unit supersedes.

## 2. Scope (IN)

- **S1** In `check_pass_open`, a dispatch row is CLOSED when a dispatch row carrying a DIFFERENT set
  follows it for the same `(group, unit)` pair. The last such row is then the one whose openness
  decides the pass, by the predicate that already exists. Observed by AC1.
- **S2** The announcement that fires when the sibling set is empty keeps firing on the same
  condition, so a proof over nobody still says so. A row closed by S1 is not a sibling. Observed by
  AC3.
- **S3** `--audit` and check 49 answer the same question through the same predicate. Today the audit
  grades a re-declaring unit's pass closed while check 49 treats that unit's superseded row as open;
  after S1 they agree about it because there is one reading. Observed by AC2.

## 3. Non-goals (OUT)

- No change to whether NARROWING a declaration is permitted. The verb allows it and the unattended
  Skill's text says it is refused; that contradiction is real and is parked for the owner, not
  resolved here. This unit makes the permitted act stop wedging the driver, which is true under
  either resolution.
- No change to check 49's disjointness rule itself. Two open passes claiming one path remain a
  refusal; what changes is which rows count as open.
- No retroactive rewriting of `RUN.md`. The abandoned rows stay on the record — they are what the
  unit declared at the time, and the record is append-only.

### Edges

- **consumes-from** `DEPL-cMendedVintage-15` — that unit's four declarations are the live instance
  this predicate wedges on, and its narrowing is what exposed the defect.
- **hands-off** `DEPL-cMendedVintage-17` — that unit's declaration of `tools/govkit/govkit.py` is
  refused until this lands, and it is the next unit in the roster.

## 4. Design

`check_pass_open` receives `(group, unit, run-state file, declared set)` and today answers from the
commit alone. It gains one earlier test: if the run-state file holds a LATER dispatch row for the
same `(group, unit)`, this row is superseded and the pass it describes is closed.

The rows are timestamped and append-only, so "later" is position in the file, which the existing
readers already walk in order. No new state and no new file.

WHICH ROW THE DECLARED SET NAMES is the part rev-1 left unsaid, and it decides whether this is a
narrow fix or a wrecked stall clock. The function is handed a SET, not a row, so the test resolves
the row by scanning that unit's rows at that group for the LAST one whose set is identical to the one
handed in, and calls the row superseded when a further row follows it. Two consequences, both load
bearing. A unit that re-declares the IDENTICAL set supersedes nothing, because both rows resolve to
the same position — so the disjointness reservation survives the driver's own published repair for a
pass that needs more paths. And a set matching NO row falls through to the commit test unchanged,
which is what `--audit` hands in: the union of a unit's same-anchor rows, already spanning through
the last of them. Without that fall-through the audit would grade every re-declaring unit closed and
could never report one STALLED, which is a worse defect than the one being fixed.

Why this is the narrow fix rather than closing a pass when its unit's spec reaches CLOSED: a spec
status is authored, and a disjointness proof must not rest on a field a run can write about itself.
Supersession is structural — a second declaration exists or it does not.

## 5. Production-readiness checklist

- security — none. The predicate decides which rows a refusal CONSIDERS, never what is written, and
  `check_pass_open` reads the run-state file it is already handed.
- perf / scale — one extra scan of the dispatch rows per row examined, over a file that holds tens of
  rows in the largest build this repo has run. No new process and no new read.
- error / empty / loading states — a row nothing supersedes behaves exactly as at BASE, including the
  unresolvable-anchor case that leaves a pass OPEN by choice. A run-state file holding a single
  dispatch row is the ordinary case and is unchanged, and so is one holding only repeats of one set.
- observability — the existing empty-sibling announcement is the observable, and S2 keeps it firing
  on the same condition so a proof over nobody still says so.
- risks — the real risk is closing a row that nothing supersedes, which would let two genuinely
  concurrent passes claim one path. `AC3` is written against exactly that and is the criterion this
  unit would most plausibly fail.
- testing — `AC1` to `AC3` are runs of the real `--dispatch` verb against a scratch run-state file,
  not a copy of the predicate. The permanent arms are declared in section 7.
- migration — none. The change is to a predicate, not to recorded data, and no `RUN.md` is rewritten.
- user docs — none owed. The unattended Skill describes re-declaring a wider set, which this makes
  work as described; it states nothing this unit falsifies.

## 6. Acceptance criteria

- **AC1** — When a unit has two dispatch rows and its commit wrote inside only the later one, a
  second unit declaring a path named ONLY by the earlier row is ACCEPTED by `--dispatch`. Red when:
  that declaration is refused by `check 49` naming the earlier row.
- **AC2** — For a unit `--audit` does not list as dispatched and open, check 49 refuses no
  declaration on the grounds of that unit's open sibling row. Red when: the two disagree about the
  same unit on the same tree, which is the state at BASE and is observable there.
- **AC3** — When a unit's only dispatch row is its first, `no sibling pass is open` prints exactly
  as it does at BASE. Red when: `check_pass_open` closes a row that nothing supersedes.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` ·
`shell hygiene (a loop fed by a command substitution)`

## 8. Open questions

- **F1 — whether the abandoned rows should also stop counting toward the run's own records.**
  RESOLVED (agent, 2026-09-17, delegated): no. They are an honest record of what the unit declared
  when it declared it, `RUN.md` is append-only by design, and `--status` counting them costs nothing.
  Only the DISJOINTNESS predicate needs to stop reading them.

## 9. Revision log

- rev-1 · 2026-09-17 · initial draft, authored mid-build by the main loop after check 49 refused
  `DEPL-cMendedVintage-17`'s declaration. Adopted under the protocol's strictly-beneficial rule as a
  blocker between this run and its own landing.
- rev-2 · 2026-09-17 · built. Section 4 gains the rule that resolves WHICH row a declared set names,
  and the two behaviours that fall out of it — an identical re-declaration supersedes nothing, and a
  set matching no row falls through unchanged. Both were implied by rev-1's design and neither was
  stated; the second is the difference between this fix and one that silently disables the stall
  clock. AC2 is AMENDED: rev-1 phrased it as `--audit` reporting no unit dispatched and open at all,
  and by the time the unit was built the audit correctly listed THIS unit's own dispatch row, so the
  criterion as written had no true premise on any tree it would ever be graded against. The
  disagreement it exists to catch is per-unit and was reproduced per-unit on
  `DEPL-cMendedVintage-15`. No scope item, gate or other criterion moved.
- rev-3 · 2026-09-17 · editorial, from this unit's own bug-class checklist run. S1 and section 5's
  empty-states bullet still read "a LATER row" and "no later sibling", which rev-2's section 4
  falsifies for the identical re-declaration: a later row exists and supersedes nothing. Both now
  spell the condition section 4 implements. No criterion, gate or non-goal moved.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "close a declared pass when a later declaration
supersedes it"` returns no seam: the map holds `check_pass_open` and `pass_commit` as the only
readers of pass openness and neither answers supersession. NO EXISTING SEAM FITS, and the evidence is
that both candidates decide from a COMMIT while supersession is decided from the row list.

`check_pass_open` already takes the run-state file as an argument, so the test has its inputs in hand
and needs no new parameter; `pass_commit` beside it is untouched. S1 therefore adds the test inside
the function that already asks the question rather than beside it.

Recall terms used: unattended dispatch declaration disjointness pass open superseded row check 49
narrowing write set sibling run-state append-only.
