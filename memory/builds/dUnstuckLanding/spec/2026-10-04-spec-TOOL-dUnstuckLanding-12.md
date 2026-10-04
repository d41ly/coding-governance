# TOOL-dUnstuckLanding-12 — design rev-2: the closing review's five HIGH findings closed

**Status:** CLOSED · rev-1 · 2026-10-04 · node d · Tier-1 · base a587e82d · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-dUnstuckLanding-12-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-12-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-12-build-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-12-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review, round 1, converged with five HIGH items, H1 to H5, in
`reviews/2026-10-04-review-TOOL-dUnstuckLanding-1-2-closing-diff-round1.md`. The severity rule
promotes them to this unit. Close each one in the records the build ships — the census, the design
and the asks — so that a builder taking an ask is not misled. Left-shift H1, which is a new class.

## 2. Scope (IN)

- **S1 — H1, the witness predicate.**
  - **What is fixed.** The census and the design stop claiming that witness ancestry tells landed
    work from discarded work. For an ABORTED record read from the tip, ancestry is structural: the
    record's commit descends from its witness, because `verb_abort` writes `witness` = HEAD
    (`unattended.sh:4746-4749`).
  - **What replaces it.** `--settle` and the signal rest on a CONTENT predicate. Attributable commits
    in `base..witness`, an off-base witness, and no revert on the tip.
  - **Ask arms.** Asks 4 and 5 carry negative arms from that population: a witness equal to base, a
    foreign-tree witness, and merged-then-reverted work.
  - **The census rows.** The aMeteredTurnstile row is corrected.

  Observed by AC1, AC2.
- **S2 — H2 and H5, where the escalation lives.** An aged leg has no introducer by construction:
  `derive_age` returns `aged` before any bisection, `run-gates.sh:2876-2879`. So the escalated ask
  stays in the CLOSING build's backlog and LIVE carries the line, and the closing run writes no other
  build's folder. ABSORB is then unchanged in fact, and the design says why. Observed by AC3.
- **S3 — H3, the stamp predicate.** Section 3's owes add `run-gates.sh`'s `ATTR_LANDABLE` predicate,
  which today counts only numeric-age legs (`:3026-3051`), together with the `:2785-2788` comment and
  the pre-push stamp read. The design states that an age-unproven INHERITED leg lands too. Ask 6's
  accept ends at a pre-push over the fixture tree. Observed by AC3.
- **S4 — H4, the carriers.** Section 2's owes add five carriers:
  - STOPS §1, for its terminal writers and its `--preflight`-over-HELD refusal;
  - STOPS §8, for a matrix row;
  - PROTOCOL §3's "two ends" sentence;
  - `lib-unattended.sh` `read_landing_commit`, which returns nothing unless HEAD's copy reads LANDING;
  - `--preflight`'s order of derivation against the HELD refusal.

  Ask 4 gains a `--preflight` arm. Observed by AC4.
- **S5 — the left-shift.** A gotcha class records H1's shape: a liveness negative drawn from another
  population than the one the probe acts on. Observed by AC5.

## 3. Non-goals (OUT)

- The MEDIUM and LOW items. They fold into the units' specs as `rev-2` bumps, by the severity rule.
- Any kit file. The build still changes no code.

### Edges

- **consumes-from** `TOOL-dUnstuckLanding-2` — the design record and the asks this unit corrects.

## 4. Design

The unit edits records in place. For each H item, the edit lands where the review located it, and the
design's revision note names the item.

### Files touched (estimate)

- `memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-2-design.md`
- `memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-1-census.md`
- `memory/builds/dUnstuckLanding/BACKLOG.md`
- `memory/gotchas/liveness-negative-from-another-population.md`

## 6. Acceptance criteria

- **AC1** — When the design's `## 2.` section is read, it states that ancestry is structural for an
  ABORTED record on the tip, and it names the content predicate.
  Red when: any sentence still says that ancestry separates landed from not-landed.
- **AC2** — When `BACKLOG.md`'s rows for asks 4 and 5 are read, each carries a witness-equals-base arm,
  a foreign-witness arm and a reverted-work arm, and each arm reads OFF.
  Red when: an arm's negative comes from a LANDING stamp or a free-standing sha.
- **AC3** — When ask 6's row in `BACKLOG.md` is read, it files the escalated ask in the closing
  build's backlog, names the `ATTR_LANDABLE` change, and ends at a pre-push.
  Red when: it names an introducing build's backlog.
- **AC4** — When the design's section 2 owes list is read, it names STOPS §1, STOPS §8,
  PROTOCOL §3 and `read_landing_commit`.
  Red when: any one of the four is missing.
- **AC5** — When `python tools/memory-tree/gotchas.py --check` runs, the new class record is accepted
  with a live anchor. Red when: check 19 reports it unanchored or inert.

## 7. Gates

`memory hygiene` · `build README slot contract` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from the closing review's round-1 HIGH items.

## 10. Reuse audit

No existing seam fits, because this unit corrects records. The gotcha catalogue,
`memory/gotchas/`, is the seam the left-shift extends. The nearest existing class is
`fixture-passes-by-finding-nothing`, and it is not this shape: this probe can read negative, but it
was asked the wrong population.
Recall terms used: ABORTED landed attended inherited red gates-green absorb hold close override terminal phase abort code
