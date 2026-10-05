# TOOL-aEvidencedLens-14 — check 19 walks a terminal record's exclusions when EITHER owner-held scan hits, so an owner's round raise never reds an archived record

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-14-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-14-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md) | diff-review | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-15 TOOL-aEvidencedLens-18 TOOL-aEvidencedLens-19 TOOL-aEvidencedLens-20 |
| [2026-10-05-review-TOOL-aEvidencedLens-12-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-12-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aEvidencedLens-9` S3 adds a round scan to check 19 of `tools/unattended/check-unattended.sh`
and re-scans it after the terminal walk's exclusions "exactly when the grant scan does". The round-1
spec audit confirmed finding 37 at HIGH: the walk runs only under
`if [ -n "$maywr" ] && [ "$maywalk" = 1 ]`, on a GRANT hit. With no grant hit, the round scan grades
the unwalked `base..witness` superset, which the arm's own header says holds every default-branch
commit landed since BASE. An owner commit on the default branch that changes `REVIEW_ROUNDS`, merged
into the run before its witness, then fails check 19 on an archived, append-only record on every
later bar, which is the forever-red that header was written to prevent. This unit makes the walk
fire on either scan's hit and re-runs both scans over the walked list. It closes finding 37 (HIGH)
of the round-1 spec audit.

## 2. Scope (IN)

- **S1** — In check 19, the condition that walks a record's exclusions becomes "the grant scan OR
  the round scan hit, and the record walks": the test reads `[ -n "$maywr$rndwr" ]` beside
  `[ "$maywalk" = 1 ]`, `rndwr` being the round scan's result over the superset, whatever name
  `TOOL-aEvidencedLens-9` built it under. This supersedes that unit's S3 "re-scans after the terminal
  walk's exclusions exactly when the grant scan does". Observed by AC1 and AC2.
- **S2** — After the walk, BOTH scans re-run over the walked list, from the one
  `read_run_exclusions` read, so the walk is still read once and still serves both. The fail-closed
  branch, which grades the whole superset when the walked list cannot be enumerated, keeps both
  scans' superset results and says so on the report channel, as it does for the grant scan today.
  The walk excludes only commits reachable from a merge's non-run parent: `read_run_exclusions`
  prints that PARENT and walks on, and `read_run_commits` keeps the merge commit itself. So a merge
  commit's own write, settled against every parent as unit 9's round scan settles it, is a run write
  the walk keeps, and an evil merge raising the bound still fails check 19. Observed by AC2 and AC3.
- **S3** — The superset-first order stays: a record whose superset hits neither scan is settled with
  no walk, so the ordinary bar pays nothing more. The header comment above the walk says the walk
  TRIGGER is shared by every scan that shares the walk, and why: a scan that grades the superset
  without the walk reds the default branch's own commits. Observed by AC4.
- **S4** — `tools/unattended/check-unattended.test.sh` gains the arms §7 names, written and not run
  in the pass. Observed by AC5.

## 3. Non-goals (OUT)

- What either scan reads or how it settles a commit. `scan_grant_writes` and `scan_round_writes` are
  unchanged; only the condition that walks, and the re-scan after it, move.
- Live records. A live record's range excludes the advertised tip and never walks, except a
  derived-landed LANDING, which already sets the walk flag and takes the same condition.
- A cutoff. The walk makes an owner raise read as no run write, so no archived record reds and
  nothing is grandfathered.
- `read_run_exclusions` and `read_run_commits`. Their contracts are `TOOL-dDerivedDocket-19`'s.
- A kit version bump. The main loop bumps once at the close (shared invariant 7).

### Edges

- **consumes-from** `TOOL-aEvidencedLens-9` — the round scan, `scan_round_writes` and its call in
  check 19; without it there is no second scan to share the walk's trigger.
- **hands-off** `TOOL-aEvidencedLens-21` — the closing diff review's batched minors, which amend what this unit built.

## 4. Design

### Evidence

Read at base `028b5cac`.

- Check 19's grant-write arm (`tools/unattended/check-unattended.sh:2352-2430`) sets `maywalk=1` for a
  terminal record with a resolvable witness and for a derived-landed LANDING, scans the superset with
  `scan_grant_writes`, and walks through `read_run_exclusions` only under
  `if [ -n "$maywr" ] && [ "$maywalk" = 1 ]`.
- The arm's header says the superset "is a SUPERSET of the run's own commits", holding "every
  default-branch commit landed since BASE", and that grading it would let an owner's own commit "red
  the bar for ever" once the record is archived.
- The walk is measured as costing about twenty seconds a bar over every terminal record here, which
  is why it runs only on a hit (same header). This unit keeps that: a walk happens only when some
  scan hits the superset.

### The arm after this unit

```text
superset := read_run_commits(witness, base)
grant := scan_grant_writes(superset);  rounds := scan_round_writes(superset)
if (grant or rounds) and walks:
    exclusions := read_run_exclusions(...)              # read once
    own := read_run_commits(witness, base, exclusions)  # or the superset, announced, on failure
    grant := scan_grant_writes(own);  rounds := scan_round_writes(own)
fail 19 per grant hit;  fail 19 per rounds hit
```

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **Walking every terminal record unconditionally.** It is correct and costs the measured twenty
  seconds on every bar to reach the empty answer the superset scan reaches for free.
- **A second walk for the round scan.** Two reads of one record's exclusions can disagree if the
  clone changes between them, and it pays the walk twice.
- **Folding the trigger into `TOOL-aEvidencedLens-9`'s spec.** The finding is HIGH, and the method
  promotes a HIGH to a unit whose mechanism closes it rather than folding it as text.

## 5. Production-readiness checklist

- security — the clause still narrows what a run can land; it reads git objects and writes nothing.
- perf / scale — unchanged on the ordinary bar, where neither scan hits the superset; one walk when
  either hits, never two.
- error / empty / loading states — a walk that fails grades the superset and says so, for both scans.
- observability — every fail line names the commit and the record, as before.
- risks — an owner raise and a run raise in one record's range: the walk keeps the run's own and
  drops the owner's, so the run raise still reds. AC2 holds both.
- testing — the arms of S4. The first two are observed RED against the leg as
  `TOOL-aEvidencedLens-9` built it; the evil-merge arm is green there too, since the unwalked leg
  also names a kept merge, so its red is a staged break, a walk that excludes the merge commit
  itself.
- migration — none.
- user docs — the clause header (S3).

## 6. Acceptance criteria

Each criterion runs `bash tools/unattended/check-unattended.sh` over a scratch fixture repository,
`git init` under a short directory beneath `%TEMP%`, its records built as the check suite's
grant-write fixture builds them. Each red of AC1 and AC2 is first observed against the leg at the
pass-start HEAD, read with `git show` into the scratchpad; AC3's is observed on the staged break it
names, because the pass-start leg names a kept merge too.

- **AC1** — When the fixture holds a TERMINAL run-state file whose `base..witness` range contains an
  owner commit on the default branch raising `REVIEW_ROUNDS="1"` to `"2"`, merged into the run branch
  before the witness, and no run commit touching `.unattended.conf`, check 19 names no round write.
  Against the pass-start leg the same fixture fails check 19 naming `1 -> 2`.
  Red when: an owner raise in a terminal record's superset reds check 19.
- **AC2** — When the same fixture also holds a run commit raising the bound to `"3"`, check 19 fails
  once, naming that run commit and `2 -> 3`, and does not name the owner commit.
  Red when: the walk drops the run's own write, or the owner commit is named.
- **AC3** — When AC1's fixture's merge of the default branch into the run is an EVIL merge, its
  resolution setting `REVIEW_ROUNDS="3"` where the default-branch parent holds `"2"` and the run
  parent `"1"`, check 19 fails once, naming that merge commit and not the owner commit; and a scratch
  copy of the leg whose walk also excludes the merge commit itself names nothing on the same fixture.
  Red when: the walk drops a merge commit's own write, so a run hides a raise in its own merge, or
  the staged break still names the merge, so the arm cannot tell a kept merge from a dropped one.
  fixture: a merge settled against every parent writes only when its value differs from each, as
  `TOOL-aEvidencedLens-9`'s round scan settles it.
- **AC4** — When `grep -n 'maywr\$' tools/unattended/check-unattended.sh` runs it prints the walk
  condition carrying both scans' results, and the comment above it names the shared trigger.
  Red when: the walk still fires on the grant scan alone.
- **AC5** — When `grep -c "round walk:" tools/unattended/check-unattended.test.sh` runs it prints at
  least 3, where the pre-pass file prints 0.
  Red when: an arm of §7 is missing.
  permission: a pass runs no suite; the arms are read at the main loop's VERIFYING run, which also
  reads them RED against the pass-start leg.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-unattended.test.sh · `round walk:` a terminal record whose superset holds an owner raise merged into the run, which the grant-only trigger reds · none
New arm: tools/unattended/check-unattended.test.sh · `round walk:` the same record with a run raise beside it, which a walk dropping too much would pass · none
New arm: tools/unattended/check-unattended.test.sh · `round walk:` an evil run merge whose resolution raises the bound, which the walk must keep and name; its red is a staged walk that excludes the merge commit itself · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, promoted from the round-1 spec audit's finding 37 (HIGH),
  repairing `TOOL-aEvidencedLens-9`.
- rev-2 · 2026-10-05 · §5 §6 §7 S2 AC3 · fold of the spec audit of units 12 to 14
  (`reviews/2026-10-05-review-TOOL-aEvidencedLens-12-spec-audit-round1.md`). Ids 3, 8 and 16
  (MEDIUM): AC3 and the third `round walk:` arm described a run commit in an "excluded merge", which
  the walk cannot produce, since it removes a merge's non-run parent side and keeps the merge commit.
  The finder's fix for id 3 was judged unsound, so the skeptic's correction is taken: AC3 becomes the
  keep case of ids 8 and 16, an evil run merge that must still fail check 19 after the walk, with its
  red on a staged walk that excludes the merge itself; S2 states that a merge's own write is a run
  write the walk keeps; and the §6 preamble and §5 testing line exempt that arm from the pass-start
  red, because the unwalked leg names a kept merge too. AC5's count stays at 3.
- rev-3 · 2026-10-05 · §3 · the mirror of `TOOL-aEvidencedLens-21`'s consumes-from edge, written by
  the main loop when the closing review's minors were promoted.

## 10. Reuse audit

The seam extended is check 19's superset-then-walk arm in `tools/unattended/check-unattended.sh`,
built by `TOOL-dDerivedDocket-19`: its `maycs` range, its one `read_run_exclusions` read and its
fail-closed superset branch are reused, and only the walk's trigger widens.
`python tools/codebase-map/reuse_lookup.py "walk a terminal run record's own commits past its exclusions only when a scan hits"`
returned name-stem neighbours only (`run`, `walk` in `corpus_ids.py`, `records`) and printed
`unscanned layers: .sh`, so the arm was read directly. The recall probe returned the round-1 finding,
`TOOL-dDerivedDocket-19`, whose spec built the walk-on-hit order, and `TOOL-aEvidencedLens-9`, whose
second scan this unit gives the same trigger.

Recall terms used: check 19 terminal witness superset read_run_exclusions walk grant scan_grant_writes maycs archived record forever red
