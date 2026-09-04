---
slug: aMendedWarden
node: a
opened: 2026-09-04
streams: tooling
roster: TOOL
status: OPEN
authorized-by: prompt
ids: TOOL-aMendedWarden-1 TOOL-aMendedWarden-2 TOOL-aMendedWarden-3 TOOL-aMendedWarden-4 TOOL-aMendedWarden-5 TOOL-aMendedWarden-6 TOOL-aMendedWarden-7 TOOL-aMendedWarden-8 TOOL-aMendedWarden-9 TOOL-aMendedWarden-10
---

# aMendedWarden — eleven confirmed defects in the guards, closed where they fail open

## The problem this build exists to solve

Eleven backlog rows were confirmed live at `d0a18683` by an adversarial triage that re-checked each
one against the tree and refuted four others. They are not eleven unrelated bugs. Nine of them share
one shape: a control that reports success on a path it never took. The fan-out guard goes blind below
an unterminated backtick and admits an unbounded burst. The unattended driver writes its terminal
phase before the check that would refuse it, leaving a record no verb can repair. Five Python readers
re-implement a conf the shell gate sources, so a legal comment removes coverage instead of failing.
This build closes each at its mechanism rather than at its symptom.

## Expected improvements

- The fan-out cap fails CLOSED on a scan it could not complete, and its loop and literal predicates
  stop admitting three spellings that were measured passing at exit 0.
- A refused `--landed` leaves a repairable record, so one failed verb no longer wedges a box's bar.
- `govkit apply` stops crashing half-applied on Windows, and `govkit update` can land a file gov
  started shipping instead of reporting it as a gap forever.
- A Tier-2 review record can say its own finder set was incomplete, rather than reading as clean.
- The push-boundary hook is compared against what is tracked, not assumed from a resolved path.

## Detriments if this is not built

- The one mechanical control against a rate-limiter wipeout has three measured bypasses and one
  fail-open, and every session in this repo and every adopter runs under it.
- Each `--landed` refusal costs a hand-edited record and a red bar until someone notices.
- Adopters keep receiving a playbook fixture that cannot pass at any prefix but gov's own.

## Build-level rules

**Classification is written here before it is acted on, per M2.** Ten units for eleven ids:
`TOOL-dScaffoldedMirror-22` and `TOOL-aGroundedOrientation-4` are one defect in one function and are
one unit; `TOOL-dTieredTribunal-28` is a third re-report of the same write and closes with it.

**Self-modification is sequenced, not assumed away.** This run edits `agent-cap.js`, which grades its
own M4 and M8 review Workflows, and `unattended.sh`, whose `verb_landed` it will itself call. The
spec audit runs BEFORE any hook or harness unit is built; the hook units build last; and
`tier2-review.js` is piped to the patched hook before the closing review is dispatched.

**No unit returns the unattended kit's `*.test.sh` legs to `tools/gate-legs.json`** — owner ruling,
2026-08-23, inherited from aBoundedCeiling and restated because this build edits that kit.

**Cut-line.** The eleven named rows and the duplicates that fold into them. A strictly beneficial
discovery is ADOPTED per directive `discoveries-adopted`; anything else found becomes a backlog row.

## Parked decisions

None yet. Recorded in `RUN.md` with the options seen and the reason each was refused.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aMendedWarden-1` | 2 | the cap rule fails closed on a scan that could not complete |
| 2 | `TOOL-aMendedWarden-2` | 2 | the loop-header predicate sees every loop opener, not two of them |
| 3 | `TOOL-aMendedWarden-3` | 2 | an empty array literal is not a bounded receiver |
| 4 | `TOOL-aMendedWarden-4` | 2 | the landing verb validates before it mutates |
| 5 | `TOOL-aMendedWarden-5` | 1 | the pathspec travels over stdin, so argv cannot bound it |
| 6 | `TOOL-aMendedWarden-6` | 2 | update classifies a descriptor source with no receipt row |
| 7 | `TOOL-aMendedWarden-7` | 1 | the review report carries the run-integrity counters it computes |
| 8 | `TOOL-aMendedWarden-8` | 2 | the wiring check compares hook content against the tracked blob |
| 9 | `TOOL-aMendedWarden-9` | 2 | the playbook fixture is rendered at deploy, not shipped verbatim |
| 10 | `TOOL-aMendedWarden-10` | 2 | the memory tree's conf has one parser, not six |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aMendedWarden-1 TOOL-aMendedWarden-2 TOOL-aMendedWarden-3 TOOL-aMendedWarden-4 TOOL-aMendedWarden-5 TOOL-aMendedWarden-6 TOOL-aMendedWarden-7 TOOL-aMendedWarden-8 TOOL-aMendedWarden-9 TOOL-aMendedWarden-10

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
