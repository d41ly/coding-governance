# DEPL-dShippedRelease-51 — the landing review's base is the recorded tip before the push

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 12 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 29 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
BLOCKER, which shares item B2 with id 71 (DEPL-dShippedRelease-52). Unit 14 §4 and AC4 pin `base` as
`<sha>^1`. Under in-place the close commits records on the prepared merge and the lander pushes
HEAD, so `<sha>^1..<sha>` is the close's own one-file diff, a placed review certifies that, and
`check_landing_review` passes a landing nobody read. This unit reads `base` from the record the
lander wrote.

## 2. Scope (IN)

- **S1** — The pin. `read_landing_pin(sha, root)` takes `base` from `landing_prior_tip` as
  `python deploy_items.py outcome <sha>` prints it, reached through `resolve_kit_dir("loop", ...)`
  as a verb, because a kit imports no sibling kit. It prints `base-source: recorded`. Observed by
  AC1.
- **S2** — The reading. Unit 14 §4 "The range", AC4's `git rev-parse <sha>^1` and the §8 F1 option's
  `<sha>^1..<sha>` are superseded by S1; S3's own words, the landed merge's first parent, stand.
  Observed by AC1.
- **S3** — The stacked case. `--case review-range` plants a close commit on a prepared merge, and
  asserts the merge's content is in `<base>..<sha>`. It is the fixture rule for every range derived
  from a landed SHA. Observed by AC2.

## 3. Non-goals (OUT)

- A landing with no outcome record on this node: DEPL-dShippedRelease-52.
- The subject kind and the lenses: unit 14 §8 F1 and F2 stand, only the range moves.

### Edges

- **consumes-from** `DEPL-dShippedRelease-14` — `read_landing_pin` and the `--landing` flag, whose `base` this unit re-reads
- **consumes-from** `DEPL-dShippedRelease-12` — `landing_prior_tip` and `python deploy_items.py outcome`, the recorded tip before the push
- **hands-off** `DEPL-dShippedRelease-52` — `read_landing_pin` and `base-source`, to which that unit adds the derived arm

## 4. Design

### Evidence

- `tools/push-main.sh:975-977` pushes HEAD, "the SHA pushed, not the prepared one", because under in-place the close
  commits its records on the prepared merge.
- `tools/unattended/lib-unattended.sh:1688` answers the commit carrying the LANDING record, and report id 29 measured
  `f4597719e` as single-parent over one file, with merge `142feb0c1` six commits back.
- Unit 12 S7 records `landing_prior_tip` as `R` at `tools/push-main.sh:956`, the tip before the push, so the value the
  review needs is already written.

### Files touched (estimate)

- `tools/workflows/review_pin.py`: S1
- `tools/loop/deploy_fixture.py`: S3's case
- `tools/workflows/README.md`: S1

### Alternatives rejected

- **`<sha>^1` with the close forbidden on the merge.** It moves `--close`, which
  TOOL-dDerivedDocket-3 settled, to save one read.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — `base-source: recorded` on the pin's line, so a reader sees where the base came
  from.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `tools/workflows/README.md` states `--landing`'s base; `help/` is unit 14's and its
  sentence on the review stands.

## 6. Acceptance criteria

- **AC1** — When `python review_pin.py --landing <sha>` runs in `--case review-range`, a close
  commit on a prepared merge, it prints `base` equal to the prior tip the outcome record holds and
  `base-source: recorded`.
  Red when: `base` equals `git rev-parse <sha>^1`, the close's own parent.
- **AC2** — When `python deploy_fixture.py --case review-range` runs,
  `git diff --name-only <base> <sha>` holds the merge's planted file and the close's record.
  Red when: the range holds only the close commit's file, so a review reads the wrong diff.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 · `review-range`, its failing case `<sha>^1` passed as the base · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 29 (BLOCKER, item B2) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is `check_prepared_merge`'s graph read at `tools/push-main.sh:505`, its comment
naming `rev-list --first-parent --min-parents=2 --max-count=1`.
`python tools/codebase-map/reuse_lookup.py "find the nearest merge on the first parent line and its first parent as the prior tip"`
ranked name-stem helpers (`merge`, `check_line`, `render_line`) and no Python reader of the prepared
merge, so no existing seam fits the derived half and the one shell function stays the model it
restates. The recall probe surfaced TOOL-dDerivedDocket-3, which records that `--close` commits on
the prepared merge, and report item B2; both agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what is the tip before a landing when the close commits records on the prepared merge" --terms "landing_prior_tip first parent prepared merge close commit in-place records stacked range lander"`
