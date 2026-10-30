# DEPL-dShippedRelease-52 — a landing with no outcome record derives its prior tip from the nearest first-parent merge

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 12 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 71 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
BLOCKER, which shares item B2 with id 29 (DEPL-dShippedRelease-51). A second node holds no outcome
record, and unit 14 §4 says it reads the same first parent, which repeats the error on the node
where nothing else can correct it. This unit derives the value as `check_prepared_merge` does, and
says that it derived it.

## 2. Scope (IN)

- **S1** — The derivation, `derive_landing_prior_tip(sha, root)` in `tools/loop/deploy_items.py`.
  `T` is `git rev-list --first-parent --min-parents=2 --max-count=1 <sha>` and the value is `T^1`;
  with no such merge it exits 2 naming the SHA. Observed by AC1, AC3.
- **S2** — The reader. The no-record branch of `read_landing_outcome` calls S1 for
  `landing_prior_tip` and prints `prior-derived`, the word unit 27 writes. Observed by AC1.
- **S3** — The pin. `read_landing_pin` prints `base-source: prior-derived` when the outcome line
  says so. Unit 14 §4's second-node sentence is superseded. Observed by AC2.

## 3. Non-goals (OUT)

- The recorded arm: DEPL-dShippedRelease-51.
- The class a second node reads: DEPL-dShippedRelease-70.

### Edges

- **consumes-from** `DEPL-dShippedRelease-14` — the `--landing` pin, whose second-node sentence this unit supersedes
- **consumes-from** `DEPL-dShippedRelease-51` — `read_landing_pin` and `base-source`, which this unit gives its derived value
- **consumes-from** `DEPL-dShippedRelease-70` — the no-record branch of `read_landing_outcome`, where S2 sits
- **hands-off** `DEPL-dShippedRelease-78` — `derive_landing_prior_tip`, which that unit reads for review id 35

## 4. Design

### Evidence

- `check_prepared_merge` (`tools/push-main.sh:514`, its comment from `:505`) reads `rev-list --first-parent --min-parents=2
  --max-count=1` and calls that fact 1.
- A planted attended landing with no merge of its own yields an older merge: report id 35 records that the value then
  stays `prior-derived`, a provenance and not a claim.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_landing_prior_tip` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2
- `tools/workflows/review_pin.py`: S3
- `tools/loop/deploy_fixture.py`: the case of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — no merge on the line exits 2 naming the SHA, and the review is
  not pinned over a guess.
- observability — `prior-derived` on the outcome line and the pin's line.
- risks — an attended landing derives an older tip, so the range reads wider than the landing; a
  wider review costs lenses and misses nothing.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `deploy_fixture.py --case review-range-second-node` deletes the outcome record,
  `python deploy_items.py outcome <sha>` prints `T^1`'s SHA and `prior-derived`.
  Red when: the value is the SHA's own first parent, the commit under the close.
- **AC2** — When `python review_pin.py --landing <sha>` runs on the same case, it prints that `base`
  and `base-source: prior-derived`.
  Red when: a derived base reads as recorded, or the pin passes `<sha>^1`.
- **AC3** — When `--case review-range-no-merge` plants a linear history, `derive_landing_prior_tip`
  exits 2 naming the SHA.
  Red when: a history with no merge yields a guessed base.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `review-range-second-node`, its failing case `<sha>^1` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 71 (BLOCKER, item B2) of the round-1 spec audit.

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
