# TOOL-aUnblockedFleet-5 — the records this build closes, narrows and files

**Status:** SPECCED · rev-2 · 2026-08-31 · node a · Tier-1 · base 117de044 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-review-TOOL-aUnblockedFleet-1-specs-round1.md](../reviews/2026-08-31-review-TOOL-aUnblockedFleet-1-specs-round1.md) | spec-audit | TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 |
| [2026-08-31-review-TOOL-aUnblockedFleet-6-specs-round2.md](../reviews/2026-08-31-review-TOOL-aUnblockedFleet-6-specs-round2.md) | spec-audit | TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-6 |

<!-- /gen:spec-records -->

## 1. Goal

Three OPEN backlog rows describe the defect this build removes, from three angles. Leaving them open
after the fix means the next session re-researches a solved problem; closing all three means claiming
coverage this build does not have, because one of them is about staleness and this build refuses
nothing. Dispose of each honestly and file the one new row this build's change creates.

## 2. Scope (IN)

- **S1** — `TOOL-aFusedCharter-4` → CLOSED. Its subject is the three-way deadlock when several builds
  land on one trunk, and its own text names check 7 as one of the three guards. With check 7 no longer
  failing, three builds at `LANDING` no longer wedge anything. The close cites this build.
- **S2** — `TOOL-aBoundedVerdict-24` → CLOSED. Its subject is a run that closes but cannot land
  reddening every later run's bar. That was check 7 and only check 7.
- **S3** — `TOOL-aReapedTicket-5` → **NARROWED, not closed.** Its title is the liveness asymmetry, and
  its blocking half is gone; but its remaining content — a dead run's record is non-terminal forever
  with no signal distinguishing it from a live one — is TRUE after this build and is now the
  motivation for a report an operator has to read rather than a gate that fires. The row is rewritten
  to say exactly that, stays OPEN, and its scope becomes the staleness bound alone. Closing it would
  be the coverage claim §7 of the charter forbids.
- **S4** — a NEW row for the lander-marker race: two runs landing from one clone share
  `<git-common-dir>/unattended-landed`, so the second push overwrites the first's marker and the
  first run's `--landed` refuses on the equality check. It fails CLOSED and it was reachable before
  this build only because check 7 made two concurrent runs rare; this build makes it ordinary. Named
  in this build's README as an explicit non-goal, so the row is where it gets tracked.
- **S5** — a `memory/DECISIONS.md` row recording the finding, because the finding is the durable part:
  the tree-wide singularity rule protected a consumer that does not exist, measured by construction.
- **S6** — `TOOL-aBranchedMandate-8` is left OPEN and untouched. It is the same-slug clobber and this
  build does not reach it. Named here so its survival is a decision rather than an oversight.

## 3. Non-goals (OUT)

- Editing any archived backlog shard. Legacy id eras are frozen (charter §2).
- Rewriting `TOOL-aPrimedKeepalive-4` / `-7`. Both remain correct and their mechanism survives as the
  exclusion units 1 and 2 keep.
- A backlog row for the staleness bound as a SEPARATE id. S3 keeps it on the row that already owns it;
  a second row would be two answers to one question.

## 4. Design

Backlog rows are mutable with stable ids (charter §6), so S1 and S2 are status flips with a cited
reason and S3 is an in-place rewrite. `memory/DECISIONS.md` is append-only, so S5 is a new row and
supersedes nothing.

The one judgement is S3. The temptation is to close all three, because all three were symptoms of one
cause and the cause is gone. The reason not to: `TOOL-aReapedTicket-5`'s text is the only place in the
corpus that records WHY an abandoned record is undetectable, and after this build that fact stops
being enforced by anything at all. A closed row is a fact nobody reads again.

### Files touched (estimate)

| file | change |
|---|---|
| `memory/backlog/TOOL.md` | two rows to CLOSED with citations, one rewritten and kept OPEN, one new row |
| `memory/DECISIONS.md` | one appended row |
| `memory/builds/aUnblockedFleet/README.md` | the acceptance ledger and the closing status |

## 5. Production-readiness checklist

- security — N/A. perf / scale — N/A. a11y — N/A. i18n — N/A.
- error / empty / loading states — N/A, records.
- observability — the hygiene leg's id-join checks are what catch a row citing a build that does not
  exist; they run on the bar.
- risks — `id-matched-as-a-substring`, selected by `gotchas.py` for this build: every id ending in a
  1-up sequence is a prefix of nine others, so each row edit is anchored on the full id and verified
  by re-grepping the exact row after the edit.
- testing + left-shift gates — the memory hygiene leg covers record shape; no new gate.
- migration / rollback — revert. user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `grep -n "TOOL-aFusedCharter-4" memory/backlog/TOOL.md` runs, the row reads `CLOSED`
  and names `aUnblockedFleet`.
- **AC2** — When `grep -n "TOOL-aBoundedVerdict-24" memory/backlog/TOOL.md` runs, the row reads
  `CLOSED` and names `aUnblockedFleet`.
- **AC3** — When `grep -n "TOOL-aReapedTicket-5" memory/backlog/TOOL.md` runs, the row reads `OPEN`
  and its text names the staleness bound as its remaining scope and no longer claims a run is blocked.
- **AC4** — When the new marker-race row is grepped, it exists, reads `OPEN`, and names both
  `<git-common-dir>/unattended-landed` and the `--landed` equality check.
- **AC5** — When `grep -n "aUnblockedFleet" memory/DECISIONS.md` runs, exactly one appended row
  records the measured finding.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs at the push boundary, it is
  green over the edited records.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with `memory hygiene` binding.

## 8. Open questions

none — S3's fork (close all three, or narrow one) is decided in §4 and recorded there.
RESOLVED (agent, 2026-08-31, delegated): narrow `TOOL-aReapedTicket-5` rather than close it, because
this build removes its blocking half and does not address its staleness half.

## 9. Revision log

- rev-1 · 2026-08-31 · authored under the aUnblockedFleet mandate.
- rev-2 · 2026-08-31 · spec-audit round 1 fold. (order 7 -> order 6 on unit 6's retirement.) Order moved 5 -> 7 to sit last after unit 6's
  insertion. Scope unchanged: no finding landed on this unit.

## 10. Reuse audit

No code seam — this unit edits records only. The conventions it reuses are the charter's §6 record
rules (append-only decisions, mutable backlog with stable ids) and `memory/HYGIENE.md`'s row grammar,
both read rather than re-derived.

Recall terms are unit 1's. The four rows this unit disposes of are exactly the ones that query
returned, which is the probe doing its job: every prior record the corpus holds on this defect was
surfaced by one query and each one is now accounted for — two closed, one narrowed, one explicitly
left alone.

**Verified at writing time**: all four rows exist at the line numbers cited, all four read `OPEN`, and
`memory/DECISIONS.md` holds no row naming this build.
