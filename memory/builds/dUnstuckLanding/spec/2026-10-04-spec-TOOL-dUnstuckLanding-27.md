# TOOL-dUnstuckLanding-27 — the implementation review's three HIGH findings closed

**Status:** CLOSED · rev-2 · 2026-10-04 · node d · Tier-2 · base 98926870 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-dUnstuckLanding-27-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-27-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the implementation range,
`reviews/2026-10-04-review-TOOL-dUnstuckLanding-13-implementation-diff-round1.md`, returned three HIGH
items. By the severity rule they are promoted to this unit. Each is a defect in code this build wrote:

- **H1:** a false red in the history legs this build narrowed.
- **H2:** a run that is still live can be settled as abandoned.
- **H3:** the hand-off exit refuses after an inherited-red close.

Close each one with the corrected fix the report records. Their duplicates are M1, M2 and M3.

## 2. Scope (IN)

- **S1 — H1.**
  - **Change:** in `tools/unattended/check-brief-recorded.sh`, the built-before-its-run exemption
    probe walks `build_commit "$base" … "$PREANCHOR_CAP" ""`, with no range exclusion beside the
    base. An exemption looks
    behind BASE, and everything behind BASE is on the tip by construction.
  - **Unchanged:** the in-range walk keeps `^<tip>`. `check-pass-order.sh`'s probe keeps its token,
    because it DETECTS violations rather than exempting them.
  - Observed by AC1.
- **S2 — H2.**
  - **Change:** in `tools/unattended/unattended.sh` `run_settle`, the lease-dead arm admits UNBOUND in
    two cases only:
    - the record predates the lease, meaning it carries no `lease-utc` fact;
    - for a leased record whose session reads absent, `LV_STALE` is `yes` and `LV_ALIVE` is not
      `yes`.
  - **Refusal:** otherwise it refuses with the arm's existing numbered refusal, fail 101 as the report
    names it. If that number has since moved, take the arm's current number.
  - Observed by AC2, AC3.
- **S3 — H3.**
  - **Change:** the paths that gates-green's own close step stages are recorded beside the
    `gates-run` fact. They are the run-state file, the build's `BACKLOG.md` that
    `write_inherited_asks` staged, and the paths `write_ask_views` reports staging.
    `check_bar_tied`'s `record-only` mode then excludes exactly that recorded set, and never the whole
    build folder. A record that names no set falls back to excluding the run-state file alone, which
    is today's behaviour.
  - Observed by AC4, AC5.
- **S4 — the arms.** Each new arm is staged RED against the current code before it lands (§7):
  - one RANGE-mode arm in `check-brief-recorded.test.sh`;
  - two `--settle` arms in the driver suite;
  - two hand-off arms in the driver suite.

  Observed by AC1 to AC5.

## 3. Non-goals (OUT)

- **The MEDIUM and LOW items.** They are folded into their own units' specs as `rev-N` bumps, by the
  severity rule, in passes of their own.
- **Gov's own `LANDING_NODES`.** It stays undeclared, as spec 20 decided.

### Edges

- **consumes-from** external — the committed code of this build's CLOSED units 14, 16, 17 and 20,
  which this unit corrects.

## 4. Design

Each fix is the review's corrected design, applied where the review cites it. For S3, the recorded
set is a new fact in the run-state file, `gates-staged: <path> <path> …`. It is written on the same
MET path that writes `gates-run`, and `check_bar_tied` reads it. A new fact owes PROTOCOL §2's fact
list. The protocol has about 470 bytes of room. If the fact does not fit, pay for it with history
prose only, as unit 20 did.

Three details the build settled (rev-2):

- **No stale set.** Gates-green also writes `gates-run` on an UNMET bar. There, a record that already
  carries `gates-staged` has it rewritten to the record alone, so a later bar never inherits an older
  close's set. A record that never carried the fact gains none.
- **The memory root bounds the set.** `check_bar_tied` excludes only entries under the memory root,
  because the close stages nothing else. Any other entry is named on a NOTE line and not excluded.
- **The fallback is announced.** With no fact, the tie prints one NOTE line, once per process, saying
  it excludes the run-state file alone.

### Files touched (estimate)

- `tools/unattended/check-brief-recorded.sh`
- `tools/unattended/check-brief-recorded.test.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`

## 5. Production-readiness checklist

- security — S2 narrows an admit, and S3 narrows an exclusion to a recorded set. Both move in the
  safe direction.
- perf / scale — none.
- error / empty / loading states — a record with no `gates-staged` fact falls back to today's
  behaviour, and the fallback is announced.
- observability — each refusal names its condition.
- risks — S3's fact is written by the close and read by `--handoff`, so it is a new pair of readers.
  AC4 drives the real producer for exactly that reason.
- testing — the five arms in S4.
- migration — none. The fact is additive, and its absence is the old behaviour.
- user docs — PROTOCOL §2's fact row.

## 6. Acceptance criteria

- **AC1** — When a RANGE-mode fixture holds a pre-base build commit for unit U with its brief row,
  and an in-range repair commit naming U with none, `check-brief-recorded.sh` reports `built before its run`
  and exits 0. Red when: it reports U as built with no brief row, which is today's behaviour.
- **AC2** — When `--settle` runs on a leased record whose `session` reads absent and whose last move
  is seconds old, it refuses naming the lease. Red when: it writes `abandoned`.
- **AC3** — When `--settle` runs on a record carrying no `lease-utc` fact, which is spec 14 AC6's
  legacy shape, it settles as before. Red when: S2 refuses the legacy record.
- **AC4** — When a hand-off-node fixture closes over an all-INHERITED red under `land`, with
  `ASKS_CMD` declared and no reusable ask, and the staged records are committed,
  `--handoff --code owner-landing` is admitted. Red when: it fails 83, which is today's behaviour.
- **AC5** — When the same fixture also changes a spec under the build folder after the bar,
  `--handoff --code owner-landing` still fails 83. Red when: S3 widens the exclusion beyond the
  recorded set.

## 7. Gates

`unattended kit gate` · `brief-recorded` · `memory hygiene` · `unattended protocol size` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/check-brief-recorded.test.sh · a RANGE fixture with a pre-base build and an in-range repair · none
New arm: tools/unattended/unattended.test.sh · a leased, session-absent, fresh record handed to --settle; a real inherited-red close on a hand-off node · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from the implementation review's round-1 HIGH items.
- rev-2 · 2026-10-04 · built; §4 records three details the build settled: the UNMET path rewrites a stale
  `gates-staged` to the record alone, the tie excludes only entries under the memory root, and the
  fallback prints one NOTE line.

## 10. Reuse audit

No existing seam fits beyond the three functions corrected: `build_commit`'s exemption call in
`check-brief-recorded.sh`, `run_settle`'s lease-dead arm, and `check_bar_tied`. Each is the seam the
review cites. The recall probe returns `TOOL-dUnstuckLanding-14` and `-20` as the binding records.

Recall terms used: settle UNBOUND lease abandoned record-only bar tie handoff brief-recorded range exemption
