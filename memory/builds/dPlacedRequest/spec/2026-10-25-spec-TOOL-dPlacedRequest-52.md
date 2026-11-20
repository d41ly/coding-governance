# TOOL-dPlacedRequest-52 — the round-3 promotions' minors: a placed race inside its lock bound, an oracle that answers by status, one walk, and criteria that read what they name

**Status:** CLOSED · rev-10 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 27 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 |
| [2026-10-25-build-TOOL-dPlacedRequest-52-deviation-521.md](../build/2026-10-25-build-TOOL-dPlacedRequest-52-deviation-521.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-52-deviation-522.md](../build/2026-10-25-build-TOOL-dPlacedRequest-52-deviation-522.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-build-TOOL-dPlacedRequest-52-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-52-1-acceptance-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-52-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-52-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-52-orders-27-28-reground-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-52-orders-27-28-reground-brief.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 |
| [2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 |
| [2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-3 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md`)
exited CONVERGED with 30 confirmed findings. Its two highs are units 50 and 51. This unit is the
batch `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` makes
of the rest: 20 MEDIUM and 8 LOW findings by raw id, one scope item per id, each naming its finding
and, in brackets, the review item holding it (M1 to M14, L1 to L6). It sits above every unit of the
build, at order 27, after units 49 and 51 at 26.

| Item | Finding | Severity | Lands on |
|---|---|---|---|
| S1 to S4 | 4, 12, 23, 31 (M1) | MEDIUM | units 37, 48, 49 |
| S5, S6 | 5, 24 (M2) | MEDIUM | units 43, 48 |
| S7, S8 | 6, 18 (M3) | MEDIUM | units 36, 38, 49 |
| S9, S10 | 7 (M4), 25 (L5) | MEDIUM, LOW | units 43, 49 |
| S11 to S13 | 11, 29 (M5), 2 (L1) | MEDIUM, LOW | units 34, 44, 49 |
| S14 | 3 (M6) | MEDIUM | units 44, 45 |
| S15 | 13 (M7) | MEDIUM | unit 48 |
| S16 | 14 (M8) | MEDIUM | unit 49 |
| S17 | 17 (M9) | MEDIUM | unit 44 |
| S18, S19 | 20 (M10), 21 (M11) | MEDIUM | units 43, 49 |
| S20 | 32 (M12) | MEDIUM | unit 49 |
| S21, S22 | 34 (M13), 36 (M14) | MEDIUM | units 46, 47 |
| S23, S24 | 8, 26 (L2) | LOW | units 33, 49 |
| S25, S26 | 9, 35 (L3) | LOW | unit 46 |
| S27 | 15 (L4) | LOW | unit 48 |
| S28 | 27 (L6) | LOW | unit 44 |

Every unit the minors land on is now CLOSED, the charter's P19 keeps built work out of in-place
rewrites, and a builder writes no spec. Re-grounded on 2026-11-20 against the tree at `0d700d256` by
`2026-11-20-prompt-TOOL-dPlacedRequest-52-orders-27-28-reground-brief`, each item is one of four
kinds, and the scope ids are kept so the siblings that cite them still resolve:

| Kind | Items |
|---|---|
| builds a product change still owed | S3, S4, S19, S20, S25, S26 |
| observes built code or a checker by a probe | S5, S9, S10 |
| folded into the one version oracle, `TOOL-dPlacedRequest-55`'s §4 block, observed there | S11 to S14, S17 |
| closed by a landed unit, or resolved in §4 as text a closed spec froze | S1, S2, S6 to S8, S15, S16, S18, S21 to S24, S27, S28 |

## 2. Scope (IN)

No item edits a spec. Criterion ACn observes item Sn; the criteria of closed, resolved and folded
items are taken out.

- **S1** — finding 4 (M1). Closed by `TOOL-dPlacedRequest-48` rev-9: its §4 "The timing the arm
  rests on" bounds B's lock wait by the 5 s (PINNED) that
  `tools/unattended/unattended.sh#write_request_record` passes to `write_dir_lock_wait`, built by
  `TOOL-dPlacedRequest-43` S30, so the race needs no item of unit 49. NOT OBSERVED here: the
  `DPR48 AC1` rows run inside that wait.
- **S2** — finding 12 (M1). Closed by the same section of 48: B's 5 s wait (PINNED) ends before A's
  `until`, the take plus `NODE_LOCK_BOUND`, 10 s (PINNED), as `tools/lib/gov-feed.sh#write_dir_lock`
  writes it. The edge to `TOOL-dPlacedRequest-37` is resolved in §4. NOT OBSERVED here: spec text.
- **S3** — finding 23 (M1). The placed-race block of `tools/unattended/unattended.test.sh` counts
  the clone's health log, `<git-common-dir>/health.log` as `tools/lib/health-log.sh#resolve_health_log`
  derives it, before A and after B. A line gained carrying `node-lock-broken` and `requests.lock`
  marks the attempt as a placement overrun, and the block's printed line names that event, never a
  lock that does not serialise. Observed by AC3.
- **S4** — finding 31 (M1), the skeptic's corrected fix, on the block as unit 48 built it. Each
  attempt clears `$pr_h/once`, `$pr_h/held` and `$pr_h/release`, writes A's and B's texts with an
  attempt-numbered marker so their key is new to the store, and stamps `pr_t0` at `held` and `pr_t1`
  at B's end. An attempt whose B ends more than the bound after the hold, the bound read from the
  driver's `NODE_LOCK_BOUND=` line, or that gained S3's event, is discarded and the placement re-run,
  up to three attempts in all; the `DPR48` rows are judged on the first attempt kept. The block fails
  `request race placed past the lock bound` only when every attempt overran, and `request race never
  placed` still reds at once. Every attempt touches `$pr_h/release` and waits for A, whose hold the
  stub bounds at 60 s (PINNED). `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` move by the block's net
  assertion count, each with a `RAISED` comment. Observed by AC1 and AC4.
- **S5** — finding 5 (M2). Built by 43 S30: `write_request_record` copies with one `cp --` spawn
  onto the temporary sibling `requests/<key>.md.<pid>`, after the compare and under `requests.lock`,
  then `mv -n` onto `<key>.md`. Left, its observation. Observed by AC5.
- **S6** — finding 24 (M2). Resolved in §4: spec 48 cites the copy by `write_request_record`.
  NOT OBSERVED here: spec text.
- **S7** — finding 6 (M3). Closed by `TOOL-dPlacedRequest-49` S8 and S32:
  `tools/lib/resolve-python.test.sh#read_feed_carriers` lists the population with the parity loop's
  pathspec, the canonical kept, and `tools/lib/resolve-python.test.sh#check_feed_copies` hands the
  canonical `gov-feed.sh` the `health-log.sh` beside it, so a correct tree passes. NOT OBSERVED here:
  that arm's green case runs every carrier.
- **S8** — finding 18 (M3). Resolved in §4: the one carriage check is 49 S8's `check_feed_copies`.
  NOT OBSERVED here: spec text.
- **S9** — finding 7 (M4). Closed by 43 S22: its size item reads the cap
  `tools/check-spec-tokens.py#read_size_ceilings` answers over the live specs, never a typed figure,
  as 49 S13 records. Left, the join's reading of this build. Observed by AC9.
- **S10** — finding 25 (L5). Spec 43 before its revision log holds no old ceiling and names the cap's
  reader; 49 rev-7 carries no AC13 to gain a count. Observed by AC10.
- **S11** — finding 11 (M5). Folded: the oracle answers by its exit status, a found bump 1, a clean
  walk 0 and every refusal 2, in unit 55's §4 block (F5). NOT OBSERVED here: unit 55's AC1.
- **S12** — finding 29 (M5). Folded: the range comes only from a found merge that is this build's
  own, unit 54's own-merge test, else `version oracle: no prepared merge on HEAD` and exit 2, in unit
  55's block. NOT OBSERVED here: unit 55's AC3.
- **S13** — finding 2 (L1). Folded: the empty walk exits 2, in unit 55's block. NOT OBSERVED here:
  unit 55's AC4.
- **S14** — finding 3 (M6). Closed by `TOOL-dPlacedRequest-44` rev-9, whose §4 Evidence and AC2
  define the one fixture and its count, and `TOOL-dPlacedRequest-45`'s AC2 names it by 44's AC2;
  unit 55's AC1 builds it. NOT OBSERVED here: spec text.
- **S15** — finding 13 (M7). Closed by 48 rev-9: its AC4 cuts 43's AC30 paragraph by `awk` and
  squeezes it by `tr -s`. NOT OBSERVED here: spec text.
- **S16** — finding 14 (M8). Resolved in §4: 49 rev-7 carries no AC24, AC30 or AC31. NOT OBSERVED
  here: spec text.
- **S17** — finding 17 (M9). Folded: unit 55's block finds the merge by fact 1 of
  `tools/push-main.sh#check_prepared_merge` and walks `$t^1..$t^2`, its header
  `version oracle: <t8>^1..<t8>^2 · <n> commits`. NOT OBSERVED here: unit 55's AC5.
- **S18** — finding 20 (M10). Closed by 43 S19:
  `skills/session-kickoff/manifest-check.sh#run_driver_bounded` takes a bound, an out file, an err
  file and the verb's arguments, prints nothing, and returns 125 with `CARD_REF_WHY` where no driver
  runs. NOT OBSERVED here: spec text.
- **S19** — finding 21 (M11). A skip is signalled by `CARD_REF_WHY`. `run_driver_bounded` empties it
  on entry, and `skills/session-kickoff/manifest-check.sh#resolve_card_driver` sets it on each of its
  three skips: no working `timeout -k`, no `.unattended.conf`, no driver. Each of the four callers,
  `derive_overlaps_line`, `derive_claims_line`, `read_card_ref` and `write_card`, reads a skip only
  from rc 125 with `CARD_REF_WHY` non-empty, so a driver's own 125, or `timeout`'s, reaches the
  caller's failure branch. Observed by AC19.
- **S20** — finding 32 (M12). `tools/lib/gov-feed.sh#add_feed_event`'s `EXIT` trap clears a
  `gov-feed.lock` with no `owner` only when no `gov-feed.lock.break` guard exists; one whose `owner`
  reads this call's token it releases as now; it leaves every other lock. A breaker in
  `write_dir_lock` holds that guard from before its `rm -rf` until after it writes `owner`, so its
  window is never cleared. The block's header names the one window left (§5), the three carriers take
  the block byte for byte, and the release plant's trap text in `tools/lib/resolve-python.test.sh`
  follows it. Observed by AC20.
- **S21** — finding 34 (M13). Closed by `TOOL-dPlacedRequest-47`:
  `tools/unattended/unattended.sh#read_claims` admits a feed line to its sightings only when
  `seen-utc` matches the ISO shape spelled with repeated classes, so a torn stamp reads unsighted.
  NOT OBSERVED here: the `DPR47 AC2` and `DPR47 AC3` rows.
- **S22** — finding 36 (M14). Closed by `TOOL-dPlacedRequest-46` and 47: `read_claims`' walk tests
  the tenure's end, then `renews -`, then `renews yes` or absent, then the sighted threshold, then
  reads on, and an unsighted tip reads `unknown`. NOT OBSERVED here: the `DPR46` and `DPR47` rows.
- **S23** — finding 8 (L2). Closed by 43 S16, as 49 S1 records:
  `skills/session-kickoff/manifest-check.sh#write_card` publishes under `CARD_PUBLISH_BOUND`.
  NOT OBSERVED here: spec text.
- **S24** — finding 26 (L2). Resolved in §4: 49 rev-7's S1 records the close and re-points nothing.
  NOT OBSERVED here: spec text.
- **S25** — finding 9 (L3). The `DPR46 AC3` loop of `tools/unattended/unattended.test.sh` gains a
  `maybe` tip, sighted a minute ago over a `renews: no` commit of its tenure sighted 1,000 hours ago,
  which reads `stale`; the walk reads it on as `no` today. Observed by AC25.
- **S26** — finding 35 (L3). An empty `renews` value is outside the four and reads on as `no`.
  `read_claims`' walk reads the key on a line beginning `renews:`, its value trimmed, where today it
  matches `renews: ` alone, so a bare `renews:` reads as a missing key, a renewing beat.
  `add_lease_commit` writes a renews argument beginning `renews:` as the whole line, and the loop
  gains a `renews:` tip and a `renews: ` tip in S25's shape. Observed by AC26.
- **S27** — finding 15 (L4). Resolved in §4: spec 48's AC2 is frozen. NOT OBSERVED here: spec text.
- **S28** — finding 27 (L6). Resolved in §4: spec 44's AC4 is frozen and was observed against spec
  43 rev-11. NOT OBSERVED here: spec text.

## 3. Non-goals (OUT)

- No second mechanism for a high: units 50 and 51 own findings 1 and 10.
- No renumbering of any order: a moved number moves nothing already built.
- No copy of the version oracle: unit 55's §4 block is the one the close runs (F5).
- No edit to a CLOSED spec, whose text P19 freezes (F6).
- No new gate leg and no new bug-class record: each arm joins an existing suite, and each class the
  review names already has its record under `memory/gotchas/`.
- No change to `NODE_LOCK_BOUND`'s value or to how a lock is broken: `TOOL-dPlacedRequest-37`'s and
  `TOOL-dPlacedRequest-24`'s.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-33` — §5's risks line, frozen, whose fact S23 records closed by unit 43
- **consumes-from** `TOOL-dPlacedRequest-34` — AC59, frozen, whose oracle S11 folds into unit 55's block
- **consumes-from** `TOOL-dPlacedRequest-36` — AC3, frozen, whose carriage S7 records closed by unit 49
- **consumes-from** `TOOL-dPlacedRequest-37` — `NODE_LOCK_BOUND`, which S4 reads as its discard bound
- **consumes-from** `TOOL-dPlacedRequest-38` — the carrier arm and §3, frozen, which S8 resolves
- **consumes-from** `TOOL-dPlacedRequest-43` — S19, S22 and S30 as built, which S5, S9, S18 and S19 read
- **consumes-from** `TOOL-dPlacedRequest-44` — the oracle, its fixture and AC4, frozen, which S11 to S14, S17 and S28 resolve
- **consumes-from** `TOOL-dPlacedRequest-45` — AC2's fixture, frozen, which S14 records
- **consumes-from** `TOOL-dPlacedRequest-46` — the walk and the `DPR46 AC3` loop, which S25 and S26 extend
- **consumes-from** `TOOL-dPlacedRequest-47` — the sighted test and the walk, which S21 and S22 record closed
- **consumes-from** `TOOL-dPlacedRequest-48` — the placed-race block, which S3 and S4 re-run, and its text, which S1, S2, S6, S15 and S27 resolve
- **consumes-from** `TOOL-dPlacedRequest-49` — S6's trap, S8's carrier arm and S13, which S20, S7 and S9 read
- **hands-off** `TOOL-dPlacedRequest-53` — AC1, AC6 and AC9 as this rev leaves them, whose counts that unit observes
- **hands-off** `TOOL-dPlacedRequest-54` — §8 F1, which names that unit's own-merge test as superseding its pick since this rev
- **hands-off** `TOOL-dPlacedRequest-55` — S11 to S14 and S17, whose corrections that unit's §4 block carries and its criteria observe
- **hands-off** `TOOL-dPlacedRequest-56` — §6's `flat` note, the race arm, AC14, AC15, AC19, AC21, AC26, S14, S26, Edges and F1, which that unit's minors amend
- **hands-off** `TOOL-dPlacedRequest-58` — S4 and §4's race sketch as unit 56 restates them, in which that unit keeps the handshake clear
- **hands-off** `TOOL-dPlacedRequest-59` — AC12, AC29, §4's oracle and the hands-off edge to 53, which that unit's items for findings 3, 6, 9 and 21 amend
- **hands-off** `TOOL-dPlacedRequest-63` — AC11 to AC14 and AC17, which that unit's item for finding 1 gives the fixture's base
- **hands-off** `TOOL-dPlacedRequest-64` — the `### The oracle (S11 to S13, S17)` heading, which that unit's item for finding 19 names as the prefix of 59 AC13's section read

## 4. Design

### The oracle (S11 to S13, S17)

The close runs one version oracle: `TOOL-dPlacedRequest-55`'s §4 block, "The oracle the close runs"
(F5). It carries this unit's corrections, the exit contract, the empty-walk status and the lander's
derivation, with unit 54's own-merge test and unit 55's captured walk; spec 44's block is named
superseded there. This spec carries no copy, and the criteria that observed the oracle here moved with
it: AC11 and AC14 to unit 55's AC1, AC12 to its AC3 with unit 54's three refusal rows, AC13 to its
AC4, AC17 to its AC5, and unit 55's ordered AC29 to its AC2.

### The placed race, re-run (S3, S4)

```
bound=$(awk -F= '/^NODE_LOCK_BOUND=/{print $2; exit}' "$SCRIPT")
attempt n = 1..3:
  clear $pr_h/once $pr_h/held $pr_h/release; texts a.md, b.md carry zq-race-marker-48-<n>
  e0 = health.log line count; A in background; wait for $pr_h/held (30 s bound) -> pr_t0
     no held -> "request race never placed", red, stop
  B to its end -> pr_t1; e1 = health.log line count
  touch $pr_h/release; wait for A
  broke = a line past e0 carries node-lock-broken and requests.lock
  pr_t1 - pr_t0 <= bound and not broke -> judge the DPR48 rows on this attempt, stop
  else -> print the attempt's seconds and node-lock-broken if seen; discard
every attempt overran -> red "request race placed past the lock bound"
```

The 30 s bound is the block's own (PINNED, `tools/unattended/unattended.test.sh@e2a90889`).

### The skip signal (S19)

`run_driver_bounded` sets `CARD_REF_WHY=""` before `resolve_card_driver`. A caller's skip arm reads
`125` with `CARD_REF_WHY` set; `125` with it empty falls to the caller's failure branch, which prints
the driver's first line, as a 126 or 127 does today. `write_card` and `read_card_ref` share the one
variable with the lookup's reasons, so the empty-on-entry also keeps a lookup's reason out of a later
publish's skip line.

### The trap (S20)

```
trap '[ -z "$_fl_mine" ] || { [ -s "$d/gov-feed.lock/owner" ] || [ -e "$d/gov-feed.lock.break" ] \
       || rm -rf "$d/gov-feed.lock"; remove_dir_lock "$d/gov-feed.lock" "$tok"; }' EXIT
```

The `DPR39` and `DPR49` mutations anchor on the trap line's `trap '[ -z "$_fl_mine" ] || { …; }' EXIT`
shape, which the new line keeps.

### The out-of-set rows (S25, S26)

A one-commit tenure sighted 1,000 hours ago reads `stale` whether its value is read as `no` or as a
renewing beat, so such a row cannot fail. The rows put the value on a fresh tip over an old
`renews: no` commit: read as `no`, the tail ages from the old commit and prints `stale`; read as a
renewing beat or as `-`, it prints `live`. The match becomes
`/^renews:/ && cr == "\001" { cr = substr($0, 8); sub(/^[ \t]+/, "", cr); sub(/[ \t]+$/, "", cr) }`.

### The closed specs' text (S1, S2, S6, S8, S14 to S16, S18, S23, S24, S27, S28)

The closing mechanism is P19: a CLOSED spec is a frozen record, so its text stands as built, and the
fact each finding asked for stands here, or in the code an item of this unit builds.

- S1, S2: spec 48's S2 and Edges name no item of unit 49, and its §4 states B's wait and A's hold,
  the 5 s wait and the 10 s hold each PINNED in 48; `NODE_LOCK_BOUND` is the `gov_feed_sh` block's
  pinned literal (`TOOL-dPlacedRequest-49` S33), so 48 owes unit 37 no edge; this spec's edge to 37
  reads the bound S4 discards by.
- S6: spec 48's S1 and Evidence cite the copy by `write_request_record`, the code 43 S30 built.
- S8: spec 38's non-goal on carriage is frozen; 49 S8's `check_feed_copies` is the one carriage
  check, its missing-appender line the red.
- S14: the fixture is spec 44's AC2 fixture; spec 45's AC2 names it by that criterion.
- S15: spec 48's AC4 reads 43's AC30 paragraph, as the finding asked.
- S16: the criteria the finding named are not in spec 49 rev-7.
- S18: spec 43's S19 sketch is frozen; `run_driver_bounded` as built is S18's fact.
- S23, S24: spec 33's risks line names `CARD_FETCH_BOUND`; the publish's bound is
  `CARD_PUBLISH_BOUND`, read by `write_card` alone, and 49 S1 records it.
- S27: spec 48's AC2 names the compare's re-run as its red; the byte compare is unit 30's.
- S28: spec 44's AC4 greps spec 43 for `first-parent` and read 0 at 43 rev-11 (PINNED in 44).

### The folds (F4)

Unit 53 ordered AC1, AC6 and AC9 to count occurrences; this rev's AC1 counts nothing, AC6 is out
with S6, and AC9 reads the checker's join, so no criterion here asks a line count of a squeezed
line. Unit 54 ordered S12, S17, AC12, the fixtures and F1 restated, and unit 55 ordered S11, §4 and
an AC29: S12 and S17 name unit 55's block, AC12 and the fixtures moved there, F1 names unit 54, and
the AC29 is unit 55's AC2. The `flat` definition went with the last criterion that read it.

### Evidence

- `tools/unattended/unattended.test.sh#run_request_arm` drives the 43 block's lease fixture, and the
  placed-race block after it writes its stub to `$pr_h/bin/cp`, polls `held` for 30 s (PINNED) and
  judges the `DPR48 AC1` and `DPR48 AC2` rows once; read 2026-11-20 at blob `e2a90889`. Its header
  names the overrun re-run as left to this unit.
- `tools/lib/gov-feed.sh#write_dir_lock` appends `node-lock-broken`, the stem `node` plus
  `-lock-broken`, to `resolve_health_log` of `ROOT`, else of the lock's parent, after it re-makes a
  stale lock and writes `owner` and `until`; it holds `<lock>.break` from before its `rm -rf` until
  then. Read 2026-11-20.
- `skills/session-kickoff/manifest-check.sh#derive_claims_line` prints `claims — skipped:` and
  `CARD_REF_WHY` on rc 125, and `CARD_REF_WHY` is set only by `resolve_card_driver`'s skips and by
  `read_card_ref`, so a driver's own 125 prints the prefix with an empty or stale reason. Read
  2026-11-20.
- `read_claims`' walk matches `/^renews: /`, and `git commit-tree -m` keeps a trailing space on a
  `renews: ` line, measured 2026-11-20 on node a.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`: S3 and S4's block, S20's plant rows beside the `DPR49 AC6`
  rows, S25's and S26's rows with `add_lease_commit`'s literal line, and the floors
- `tools/lib/gov-feed.sh`: S20's trap and header, with its carried copies in
  `tools/unattended/unattended.sh`, `tools/run-gates/post-merge.sh` and `tools/push-main.sh`
- `tools/unattended/unattended.sh`: S26's match in `read_claims`
- `tools/lib/resolve-python.test.sh`: the release plant's trap text, S20
- `skills/session-kickoff/manifest-check.sh` and `skills/session-kickoff/manifest-check.test.sh`: S19
- `memory/guides/SESSION-KICKOFF.md`: its `last-audit` re-stamp, since its `watch:` line names
  `skills/session-kickoff/manifest-check.sh`
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads,
  so `gen_map.py --check` exits 0 after the pass; `TOOL-dPlacedRequest-34` S38 is the final re-check
  only

### Alternatives rejected

- **Two batches.** S20 and S26 write the driver's carried block and walk, and S3, S4, S20, S25 and
  S26 write `tools/unattended/unattended.test.sh`, so no split gives two disjoint write sets.
- **The review's literal out-of-set rows (S25, S26).** A lone commit sighted 1,000 hours ago reads
  `stale` both ways, so the row passes on the defect it exists to catch.
- **Release A once B makes its first lock attempt (finding 23's second fix).** The PATH stub sees only
  `cp`, not B's lock attempt, so the arm would need a hook in the driver.
- **A distinct return code for a skip (S19).** Every code is also a code a verb may exit with.

## 5. Production-readiness checklist

- security — S20 narrows the trap to locks this writer took; the one window left is a third writer's
  own `mkdir`-to-`owner` window after a peer broke this writer's lock and released it, reachable only
  by an append that outlives `NODE_LOCK_BOUND` and a full peer cycle, and the block's header names it.
- perf / scale — S4 runs at most three placements, each holding A at most 60 s (PINNED).
- error / empty / loading states — S19 gives every skip its reason and every other 125 a failure
  line.
- observability — S3's printed line names the break event and each attempt's seconds.
- risks — a slow node that overruns every attempt still reds, named; S26 changes how a hand-written
  `renews:` line ages, which no writer produces.
- testing — the probes of §6 and the arms of §7.
- migration — none: every surface is new in this build.
- user docs — none: no user-facing behaviour changes.

## 6. Acceptance criteria

The fixtures are the named units': the 43 block's lease fixture for the race, unit 26's chains for
the walk, the `DPR39` block's `gov_feed_sh` cut for the trap, and `manifest-check.test.sh`'s stub
driver for the card, each `RUN_CLAIMS=on` unless stated.

- **AC1** — When the placed-race block runs over the built driver, its first kept attempt passes the
  `DPR48 AC1` and `DPR48 AC2` rows; run with `SCRIPT` set to the driver of a worktree at `3fc16744c`,
  before unit 43's lock, B exits 0 inside the bound, the attempt is kept, and the `DPR48 AC1` rows
  fail.
  Red when: an unlocked driver's race is discarded as an overrun and the block passes.
- **AC3** — When a scratch copy of the block sleeps 11 s (PINNED) between `held` and B on its first
  attempt, B breaks A's lock as stale, the clone's `health.log` gains a `node-lock-broken` line naming
  `requests.lock`, and the block's printed line names `node-lock-broken` for that attempt.
  Red when: a stale break is reported as a lock that does not serialise.
  figure: the sleep PINNED one past the 10 s bound (PINNED), read 2026-11-20.
- **AC4** — When that sleep applies to the first attempt only, the block discards it and passes on
  the second; when it applies to every attempt, the block fails
  `request race placed past the lock bound`; after either, `jobs -p` in the block's shell prints
  nothing.
  Red when: an overrun reads as a lock defect, or A is left waiting.
- **AC5** — When `awk '/^write_request_record\(\)/{f=1} f; f&&/^}/{exit}'` cuts the body from
  `tools/unattended/unattended.sh` and `grep -n 'cp -- '` reads it, one line prints, naming the
  `$key.md.$$` sibling, after the line naming `write_dir_lock_wait` and before the line naming
  `remove_dir_lock`.
  Red when: the copy is a redirect, a `mv` or a Python write the race block's stub never sees.
- **AC9** — When `python tools/check-spec-tokens.py` runs, its `size join` line names the ceiling
  `read_size_ceilings` answers, and no `size <-` row names a spec under
  `memory/builds/dPlacedRequest/spec/`.
  Red when: a live spec of the build is over the cap.
  figure: the cap DERIVED by `read_size_ceilings` at the run; 49152 on 2026-11-20 PINNED.
- **AC10** — When `sed '/^## 9\./,$d' memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md`
  is piped to `grep -o 47104 | wc -l`, it prints 0, and the same cut holds `read_size_ceilings`.
  Red when: a typed ceiling stands in 43 beside the checker's.
  figure: 0 PINNED, read 2026-11-20.
- **AC19** — When `derive_claims_line` runs in a scratch tree whose resolved driver is a stub printing
  `FAILED: boom` and exiting 125, the cell prints `claims — skipped: FAILED: boom`; with no
  `.unattended.conf`, it prints `claims — skipped: no .unattended.conf in this tree`.
  Red when: a driver's own 125 reads as a skip with an empty or stale reason.
- **AC20** — When a plant on the `DPR39` block's cut, beside the `DPR49 AC6` rows, sets `_fl_mine`,
  stages a peer's break of `gov-feed.lock` (the `.break` guard made, the lock removed and made
  again, no `owner`) and ends the subshell, the lock directory survives; with no guard and no
  `owner`, it is cleared; with `owner` reading another token, it survives.
  Red when: the trap clears a lock a breaker holds.
- **AC25** — When the `DPR46 AC3` loop runs, the `maybe` tip reads `stale`; a scratch copy whose walk
  stops on any value but `no` reads it `live`.
  Red when: a value outside the four hides an expiry.
- **AC26** — When the loop's `renews:` and `renews: ` tips run, both read `stale`; a scratch copy of
  the driver whose walk matches `renews: ` alone reads the `renews:` tip `live`.
  Red when: an empty value reads as a legacy renewing beat.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `manifest-check self-test` · `scratch-guard self-test` · `push-main self-test` · `tier2-review self-test` · `policy fixtures` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC3 AC4 AC20 AC25 AC26 · each item's plant, a scratch copy of the block or the driver as its criterion states · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` move by the rows gained · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC19 · a stub driver exiting 125, staged against callers that read rc 125 alone · `FLOOR_ASSERTIONS` rises by the rows gained

## 8. Open questions

- **F1 — How does the oracle find its range (S12, S17)?** (a) The lander's fact-1 derivation alone,
  refusing with exit 2 when no merge is found; (b) (a) gated on `push-main.sh --prepared`; (c) (a)
  with a merge-base fallback whose remote comes from `tools/lib/resolve-remote.sh`. (b) reads the
  remote's advertised tip, which a fixture lacks and a read of local history does not need; (c)
  sources a canonical for a fallback no caller runs. RESOLVED (agent, 2026-10-25, delegated): (a),
  rung 3, the fewest open questions, and the seam `check_prepared_merge` found. widens: none ·
  relaxes: none. Superseded in part by `TOOL-dPlacedRequest-54` F1, whose own-merge test the one
  block in unit 55's §4 carries beside fact 1 (F4, F5).
- **F2 — Which ownerless lock may the trap clear (S20)?** (a) One this subshell's `mkdir` made, with
  no `.break` guard present; (b) one whose directory identity, read by `stat`, matches the one made;
  (c) none. (b) rests on inode numbers under Git Bash on NTFS, unmeasured here; (c) leaves an abort
  holding the lock until its deadline. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the
  review's fix judged sound, with its residual stated in §5. widens: none · relaxes: none
- **F3 — How does the placed race stay inside the lock bound (S1 to S4)?** (a) Stamp, discard and
  re-place up to three times; (b) release A once B makes its first lock attempt; (c) order 48 after
  49. (b) needs a driver hook; (c) renumbers a built unit. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3, the skeptic's corrected fix for finding 31, with finding 23's health-log read as its
  cause line. widens: none · relaxes: none
- **F4 — Are the amendments units 53, 54 and 55 order to this spec made at a pass or now?** (a) Now,
  once, in this text, each ordering unit reduced to observing it; (b) at this unit's pass; (c) at
  each ordering unit's pass. (b) and (c) have a builder write a spec, which no builder does.
  Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; this spec is DEFERRED,
  so each amendment is a spec act the re-grounding makes once, as the brief's fold rule names.
  widens: none · relaxes: none
- **F5 — Where does the corrected oracle live, so the close runs one?** (a) In unit 55's §4, the last
  of the three correcting units, this spec naming it; (b) in this spec's §4; (c) in spec 44's §4.
  (b) is the earliest text two later units correct again; (c) is CLOSED. Recommendation: (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; ruled whole at unit 55's F3, spec 44's block
  named superseded there, so the close runs one block. widens: none · relaxes: none
- **F6 — What becomes of an item that edits a CLOSED spec?** (a) A product change still owed is
  built and observed, and a text-only finding is resolved in §4 naming P19; (b) the closed spec is
  edited with a rev bump; (c) the item is dropped unrecorded. (b) rewrites built work; (c) loses the
  fact. Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; P19 freezes every
  unit these minors land on, and the kinds table of §1 sorts each item by what the tree holds.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-3 promotions' 20
  MEDIUM and 8 LOW findings.
- rev-2 · 2026-10-25 · the promoted fix brief's gate hits: AC7 cites `gov-feed.sh` by basename, the
  file `TOOL-dPlacedRequest-13` creates; AC22's red case on one `Red when:` line.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-4 promotions: the hands-off edges to `TOOL-dPlacedRequest-53`, `TOOL-dPlacedRequest-54`, `TOOL-dPlacedRequest-55`, `TOOL-dPlacedRequest-56`, mirroring their consumes-from.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the hands-off edges to `TOOL-dPlacedRequest-58` and `TOOL-dPlacedRequest-59`, mirroring their consumes-from.
- rev-5 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edge to `TOOL-dPlacedRequest-63`, mirroring its consumes-from.
- rev-6 · 2026-10-25 · §3 · the disposal of the spec audit of the round-8 promotions: the hands-off edge to `TOOL-dPlacedRequest-64`, mirroring its consumes-from.
- rev-7 · 2026-11-19 · §2 S20 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit` finding 15 (H3): the node lock is the shared `write_dir_lock` family, which `TOOL-dPlacedRequest-24` rev-5 S1 moves into `gov_feed_sh`, so every name of the lock factory this spec spells is that family's. §7 also names `tier2-review self-test`, the leg(s) the spec-token guard join names for this spec's Files touched.
- rev-8 · 2026-11-19 · §2 S9 · §6 AC9 · §7 · folds `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`:
  finding 2 (H1), S9 re-observes 43's 48128 and unit 34's size on the disposal's dated measurement;
  finding 23 (M11), §7 names `policy fixtures`.
- rev-9 · 2026-11-19 · §1 · §2 S9 · §4 Files touched · §6 AC9 · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: findings 1, 6 and 13 (M1), 47885 at rev-12
  and a cut in prose here; finding 5 (L2), the Goal names M5 among the six multi-id items; finding
  17 (M8), this unit's own pass regenerates `memory/map/generated/`, named in Files touched, and §7
  names its leg.
- rev-10 · 2026-11-20 · §1 · §2 S1 to S28 · §3 · §4 · §5 · §6 AC1 AC3 AC4 AC5 AC9 AC10 AC19 AC20
  AC25 AC26 · §7 · §8 F1 F4 F5 F6 · §10 · re-grounded by
  `2026-11-20-prompt-TOOL-dPlacedRequest-52-orders-27-28-reground-brief`: every unit the minors land
  on is CLOSED, so no item edits a spec (F6). Closed by landed units: S1, S2, S7, S14, S15, S18 and
  S21 to S23; resolved in §4's "The closed specs' text": S6, S8, S16, S24, S27 and S28; probes of
  built code or the checker: S5, S9 and S10, AC9 and AC10 read the checker's cap; folded into unit
  55's one oracle block (F5): S11 to S13 and S17, with their criteria; left to build: S3 and S4 on
  unit 48's block as built, S19 on `CARD_REF_WHY`, S20 on the guard, S25, and S26 on the
  `renews:` match. The amendments units 53, 54 and 55 ordered made here once (F4), `flat` going with
  the last criterion that read it; F1 names unit 54. The kickoff manifest added to Files touched;
  line citations swapped for symbol citations and a blob pin, the build method's section to its alias
  tag.

## 10. Reuse audit

Each item extends the code its finding names: the placed-race block and
`tools/unattended/unattended.test.sh#run_request_arm` for S3 and S4, with
`tools/lib/health-log.sh#resolve_health_log` for the health log's path; the `.break` guard of
`tools/lib/gov-feed.sh#write_dir_lock` for S20; `skills/session-kickoff/manifest-check.sh#resolve_card_driver`'s
reason variable for S19; and the walk of `tools/unattended/unattended.sh#read_claims`, the brief's
named claims seam beside `tools/unattended/unattended.sh#write_gov_ref`, for S26, whose
`add_lease_commit` helper writes the rows. `python tools/codebase-map/reuse_lookup.py "re-run a placed
race attempt that overran the lock hold bound"`, run 2026-11-20, ranked `run`, `run_git` and
`run_selftest_cases`, name stems only, none a placement re-run; the same tool on "a trap that clears
an ownerless lock only when no break guard exists" ranked `remove_dir_lock` and
`check_dir_lock_stale` first among lock names, the family S20 joins. `python
tools/memory-recall/query.py "re-run a placed race attempt that overran the lock hold bound"` with
the terms below returned `TOOL-dPlacedRequest-58`, this spec's race sketch and
`TOOL-dPlacedRequest-48`; none disagrees with source.

Recall terms used: placed race requests.lock overrun NODE_LOCK_BOUND node-lock-broken health log stub cp re-place attempt
