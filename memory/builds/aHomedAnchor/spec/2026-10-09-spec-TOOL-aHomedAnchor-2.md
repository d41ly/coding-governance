# TOOL-aHomedAnchor-2 — the bar leg admits a local-anchored BASE when origin's default branch declares `local`

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-2 · base 11224126 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aHomedAnchor-1-runlog-5ac5d61b.md](../build/2026-10-09-build-TOOL-aHomedAnchor-1-runlog-5ac5d61b.md) | journal | TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7 |
| [2026-10-09-build-TOOL-aHomedAnchor-2-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aHomedAnchor-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aHomedAnchor-1-0-run-mandate.md](../prompts/2026-10-09-prompt-TOOL-aHomedAnchor-1-0-run-mandate.md) | journal | TOOL-aHomedAnchor-1 |
| [2026-10-09-prompt-TOOL-aHomedAnchor-1-1-reconstructed-build-briefs.md](../prompts/2026-10-09-prompt-TOOL-aHomedAnchor-1-1-reconstructed-build-briefs.md) | journal | TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7 |
| [2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md](../reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md) | diff-review | TOOL-aHomedAnchor-1 |

<!-- /gen:spec-records -->

## 1. Goal

Stop the unattended bar leg from redding every run the driver's local anchor authorizes, without
letting a run widen the leg by editing its own conf: the leg reads `ANCHOR_SCOPE` from the
`.unattended.conf` blob at the tip the remote advertises for its default branch, a byte the run
cannot write without landing through the bar.

## 2. Scope (IN)

- S1. `tools/unattended/check-unattended.sh` gains `read_origin_scope`, which evaluates nothing: it
  reads the last `ANCHOR_SCOPE=` assignment line of the conf blob at `ADV_HEAD`, quotes, comment and
  CR stripped, and sets `ORIGIN_SCOPE`. It is computed once per leg run, after the advertisement, and
  only when `ADV_HEAD_OK=1`; otherwise `ORIGIN_SCOPE` is empty, which is the strict reading.
  Observed by AC1 and AC2.
- S2. Check 9's not-published branch admits the recorded BASE when `ORIGIN_SCOPE` is `local` and
  the BASE is an ancestor of HEAD, and prints a `report` line saying so. Anything else refuses as
  today. Observed by AC1, AC2 and AC3.
- S3. Check 29 is skipped when `ORIGIN_SCOPE` is `local`, because that anchor admits every mode.
  Observed by AC4.
- S4. The leg's header and check 9's comment state what this does NOT check: that the local BASE
  predates the run. NOT OBSERVED: prose.

## 3. Non-goals (OUT)

- The working-tree conf: the leg never reads it for this decision, so a run cannot opt itself in.
- The driver: `TOOL-aHomedAnchor-1`.
- Check 15's landed-witness rule and check 13's README shape: neither asks whether BASE is
  published.
- An offline leg: no advertisement still fails closed, as today.

### Edges

- **consumes-from** `TOOL-aHomedAnchor-1` — the `local` value and what a local-anchored record pins

## 4. Design

`is_published` stays the question check 9 asks first. Only its NOT-published answer, return 1,
consults `ORIGIN_SCOPE`; a CANNOT-TELL answer, return 2, keeps its refusal, because a clone missing
advertised tips cannot be graded either way.

The scope is read off the remote's default-branch tip because every other place is the run's to
write. The working tree and the recorded BASE are the run's. So is the run branch's advertised
tip: the run pushes it. The default-branch tip moves only through a landing, and the landing
runs this leg first. So a run that commits `ANCHOR_SCOPE="local"` widens nothing until the change
is on origin's default branch, which is the opt-in the owner ruled for.

The reader parses rather than evaluates. The driver sources the conf, so the last assignment wins,
and the reader takes the last assignment line. A value spelled through shell expansion reads as
itself, not as `local`, and so keeps the strict reading: a parse that can only fail closed needs no
sentinel.

### Inventory

- `read_origin_scope` — a function, leading verb `read`.
- `ORIGIN_SCOPE` — a global set once.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`

## 5. Production-readiness checklist

- security — the widening is gated on a byte outside the run's reach; a misspelt or expanded value
  reads strict.
- perf / scale — one `git show` per leg run.
- error / empty / loading states — no advertised HEAD, or a HEAD this clone lacks, leaves
  `ORIGIN_SCOPE` empty.
- observability — the admitting `report` line names the BASE and the record.
- risks — the leg's BASE check weakens for every adopter that declares `local` on its default branch,
  which is the opt-in.
- testing — AC1 to AC4, arms in the leg suite, observed by a slice.
- migration — N/A — no record changes.
- user docs — N/A — the protocol text is `TOOL-aHomedAnchor-1`'s.

## 6. Acceptance criteria

- **AC1** — When `check-unattended.sh` grades a record whose BASE is unpublished and an ancestor of
  HEAD, with origin's default-branch conf declaring `ANCHOR_SCOPE="local"`, check 9 does not fail and
  the leg prints `admitted by the local anchor`. Red when: `read_origin_scope` is never consulted.
- **AC2** — When the same record is graded with `ANCHOR_SCOPE="local"` only in the working tree and
  `published` at origin's default branch, check 9 fails with `is not published on the remote`.
  Red when: the leg reads the working-tree conf.
- **AC3** — When origin declares `local` and the recorded BASE is not an ancestor of HEAD, check 9
  fails. Red when: the local admission skips the ancestry test.
- **AC4** — When origin declares `local` and the record's README is `slug` mode on an unpublished
  BASE, check 29 does not fail. Red when: check 29 still keys on the default-branch tip alone.

## 7. Gates

`unattended kit gate`

New arm: tools/unattended/check-unattended.test.sh · covers AC1 AC2 AC3 AC4 · a fixture remote whose default-branch conf declares local, a run BASE on an unpushed branch · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`reuse_lookup.py "authorize an unattended run from a local commit without a published branch
tip"` names no seam; the seams extended are check 9's `is_published` branch and check 29 in
`tools/unattended/check-unattended.sh`, and the parse shape is `read_rounds_of`'s, the leg's existing
reader of a conf blob.

Recall terms used: `--terms "ANCHOR_SCOPE published second anchor SECOND_ANCHOR_MODES slug mode
branch tip authorization reachable BASE merge-base dNarrowedAnchor"`, which returned
`TOOL-dNarrowedAnchor-1` and `TOOL-aStandingWrit-6`'s rule that the leg reads no run-writable ref.
