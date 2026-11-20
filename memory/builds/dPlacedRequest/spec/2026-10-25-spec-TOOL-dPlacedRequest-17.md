# TOOL-dPlacedRequest-17 — every lease deadline judged by the observer clock: expiry, an offer's deadline and a tombstone's prune age

**Status:** CLOSED · rev-5 · 2026-11-19 · node a · Tier-2 · base c63aabbb · streams tooling · order 4 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0135@55365bfa whole
**Carries:** node:policy-key.leases.expiry-hours
**Carries:** node:policy-key.leases.queued-claim-days

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-build-TOOL-dPlacedRequest-17-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dPlacedRequest-17-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dPlacedRequest-17-red-fix-7.md](../build/2026-11-19-build-TOOL-dPlacedRequest-17-red-fix-7.md) | red-fix | — |
| [2026-11-19-build-TOOL-dPlacedRequest-17-red-fix-8.md](../build/2026-11-19-build-TOOL-dPlacedRequest-17-red-fix-8.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-17-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-17-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dPlacedRequest-17-divergence-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-17-divergence-brief.md) | research | — |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

A deadline one node judges on a record another node stamped is judged by a declared clock: the time
since this node first saw the record, on this node's own clock, never this node's clock minus the
holder's stamp (v2:680, v2:1160, research-cloud-headless S4). Today `read_claims` ages every claim as
`age[1] - age[$11 + 1]`, the reader's `date` minus the holder's `beat-utc`
(`tools/unattended/unattended.sh#read_claims`, its verdict `awk`), so a reader whose clock runs a day ahead reads every claim a
day old and a reader a day behind never expires one (gap-conc-14). The change feed of
`TOOL-dPlacedRequest-13` already stamps each tip with the time this node first saw it; this unit reads
those stamps and makes every lease deadline a function of them.

## 2. Scope (IN)

- **S1** — The observer clock (I8), `read_first_seen`, in the `gov_feed_sh` block beside
  `add_feed_event`: given `<ref><TAB><sha>` pairs on stdin, one `awk` over `gov-feed.log` prints, per
  pair, the `seen-utc` of that key's line, or `-` when the feed holds none. It is the one reader of a
  first sighting. Observed by AC1 and AC5.
- **S2** — The commit set and the renewing beat, one rule: for each row, walk the first-parent chain
  from the row's own tip and stop at the current tenure's opening commit, the oldest commit whose
  `epoch` equals the tip's (an absent `epoch` reads 0, so a legacy chain is one tenure); that bound is
  the tenure `TOOL-dPlacedRequest-26` names, and a migrated lease's first commit, at epoch 1 over a
  legacy tip, is its opener, so the legacy commits beneath it never feed the renewing beat. The
  renewing beat is the newest commit of that walk whose `renews` reads `yes` or is absent (a legacy
  run claim carries none, so its tip renews), else the opener whatever its `renews` line says (§8 F5).
  Commits are tied to a row by the walk from its tip sha, never by their `gov-claim <tail>` header.
  Observed by AC3 and AC8.
- **S3** — The age pass of `read_claims` (`tools/unattended/unattended.sh#read_claims`): field 4,
  `beat-age-s`, becomes now minus the first sighting of the row's tip, and the verdict reads `stale`
  when now minus the first sighting of S2's renewing beat exceeds `leases.expiry-hours`, both on this
  node's clock through one `date -f` call. A tenure with no `renews: yes` commit is therefore aged from
  its opener's first sighting: `live` inside `leases.expiry-hours` of it and `stale` after (§8 F5). A
  row whose renewing beat carries `renews: -` (`leases.renewal: none`, under which every write carries
  it, so the opener does) never reads `stale`; a row whose tip or renewing beat the feed has not
  sighted reads `unknown` with age `-`, never `stale`. `held` and `terminal` keep their verdicts.
  Observed by AC1, AC2, AC3, AC4, AC6 and AC8.
- **S4** — The deadline, `check_deadline_passed <ref> <sha> <seconds>`: rc 0 when this node first saw
  `<sha>` at `<ref>` more than `<seconds>` ago, rc 1 when not yet, rc 2 when the feed has not sighted
  it. It is the one judgment the offer's deadline (`leases.offer-seconds`, `TOOL-dPlacedRequest-20`) and
  the tombstone's prune age (`leases.queued-claim-days`, `TOOL-dPlacedRequest-16`) call. Observed by AC5.
- **S5** — The bounds, read through `TOOL-dPlacedRequest-1`'s `read_lease_policy`: `leases.expiry-hours`
  (hours, default 24) and `leases.queued-claim-days` (days, default 7), the two keys this unit owns, and
  `leases.offer-seconds` (seconds, default 300), `TOOL-dPlacedRequest-20`'s, by
  `read_lease_bound expiry|offer|prune`, which prints seconds. Each default is v2:1160, :1163 and :1164;
  the catalogue rows are dGroundRules-1 S3's. Observed by AC2.
- **S6** — The fence beat: a write with no new witness, which `TOOL-dPlacedRequest-1` S8 writes
  `renews: no` under `progress`, moves the tip and leaves the renewing beat where it was, so the lease
  still expires on schedule. Observed by AC3.
- **S7** — The stops guide's verdict table (`tools/unattended/STOPS.template.md`, section 7 "The
  lease", its `| claim | verdict |` table, rendered to `memory/guides/UNATTENDED-STOPS.md`) states the
  observer rule, the three bounds and the `unknown` row for an unsighted record. Observed by AC7.
- **S8** — The existing arms re-staged: every arm of `tools/unattended/unattended.test.sh` that makes
  a claim stale by planting an old `beat-utc`, or seeds a lease with `renews: no`, is re-staged so its
  sighting is a planted feed line, and keeps its expected verdict under the observer clock. The arms
  known at rev-5 are the five-verdict AC2 arm, the `foreign-stale` rows of the claim-table arm, AC5,
  AC8, AC18, AC19, GH36 AC6 and DPR1 AC2, each by its label in the suite; the inventory is made by
  `git grep` over the suite at build time (AC9), never typed from this list alone. Observed by AC9.

## 3. Non-goals (OUT)

- No offer and no tombstone: `TOOL-dPlacedRequest-20` writes the offer and calls S4 for its deadline,
  and `TOOL-dPlacedRequest-16` writes tombstones and calls S4 for their prune age.
- No clock offset from the remote host's time: v2:1160's second rule is dWellOiledMachine's supervisor's,
  once it measures each node's offset at each beat; the observer rule stands alone until then.
- No change to the renewal rule itself: when a write renews is `leases.renewal`'s, set by
  `TOOL-dPlacedRequest-1`; this unit judges what the record says.
- No change to `RESUME_STALE_BOUND`'s other readers: the run-state liveness and the holder's quarter-bound
  due rule (`tools/unattended/unattended.sh#check_claim_writable`) keep it; the due rule now reads the tip's observer age.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-13` — `gov-feed.log`, whose first `seen-utc` per key is the clock
- **consumes-from** `TOOL-dPlacedRequest-1` — `refs/gov/leases/<slug>/build`, its `renews` field and `read_lease_policy`
- **hands-off** `TOOL-dPlacedRequest-16` — `read_first_seen` and `check_deadline_passed`, which judge a tombstone's prune age and a queued claim's age
- **hands-off** `TOOL-dPlacedRequest-20` — `read_first_seen` and `check_deadline_passed`, which judge an offer's deadline
- **hands-off** `TOOL-dPlacedRequest-26` — the age pass's walk and verdict `awk`, whose stop at the current tenure's opening commit is the bound that unit names and grades with its tenure arms
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### The rule

```
age(record) = now(this node) - seen-utc(this node's first sighting of the record)
expired     = age(the tenure's newest renewing beat, else its opening commit) > leases.expiry-hours
offer open  = age(the commit that set the offer) <= leases.offer-seconds
prunable    = age(the terminal tombstone) > leases.queued-claim-days
```

Both terms of every age are read on one node's clock, so a constant skew cancels: a reader a day ahead
stamped its sighting a day ahead too. What the rule does not see is a clock STEPPED between the sighting
and the judgment, which moves that node's ages by the step; it never moves another node's.

### The age pass

1. After the fetch, `TOOL-dPlacedRequest-13`'s `add_feed_sightings` has appended every unseen chain
   commit, so every cached tip and renewing beat normally has a line.
2. One `git log --first-parent --format='%x01%H %P%n%B' <every cached lease and legacy ref>` lists
   each commit on any cached ref's first-parent chain once, with its parents; one `awk` maps each sha
   to its first parent, its `epoch` (absent reads 0) and its `renews`. Then, per row, it walks from the
   row's own tip sha (field 4 of the rows `read_claims` builds) through first parents while the
   `epoch` equals the tip's: the first commit whose `renews` is `yes` or absent is the renewing beat,
   and the walk ends at the opener, the last commit with the tip's `epoch`, which is the renewing beat
   when none was found (S2, §8 F5). A commit shared by two refs, as a migrated lease shares its legacy
   chain, is listed once and read by each walk that reaches it; the `gov-claim <tail>` header ties no
   commit to a row.
3. `read_first_seen` over the tip and renewing pairs, then one `date -u -f` over `now` and every
   stamp, with the DEAD PROBE rule unchanged (`tools/unattended/unattended.sh#read_claims`, its
   `nask`/`ngot` count): a count mismatch reads every age `-`.
4. The verdict `awk` (`tools/unattended/unattended.sh#read_claims`, the `awk` reading `CL_AGES`)
   compares the renewing age with the expiry bound instead of the tip's beat age with
   `RESUME_STALE_BOUND`.

A chain grows by one commit per write, so step 2 reads every write a tenure has had, plus the
legacy chain a migrated lease sits on; at a write a minute for a day that is 1,440 commits per lease
(DERIVED: 60 × 24), read in one process.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_first_seen` | shell function, in `gov_feed_sh` | `read`, OK |
| `check_deadline_passed` | shell function | `check`, OK |
| `read_lease_bound` | shell function | `read`, OK |

### Migration

None. A claim fetched before its first sighting is sighted at the first read after this unit lands and
reads young from then, so the change can only delay an expiry by up to one bound, never advance one.

### Rollout

Live with `RUN_CLAIMS`, as every lease read is. The take-over of a dead foreign run moves from
`RESUME_STALE_BOUND` (5400 s, PINNED 2026-11-19 from `.unattended.conf`'s `RESUME_STALE_BOUND` key)
after its last beat to `leases.expiry-hours` (24 h, PINNED as S5's default) after its last renewing
beat, or its tenure's opener when it has none (§8 F5), the ratified expiry (night-pass-two:281).

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: `read_first_seen`
- `tools/unattended/unattended.sh`: the inline block, the age pass, `check_deadline_passed`,
  `read_lease_bound`; the kit version is minted by the lander (TOOL-aMendedFleet-65; TOOL-dPlacedRequest-34 S59)
- `tools/run-gates/post-merge.sh`: the inline block, carried
- `tools/unattended/unattended.test.sh`: the clock arms, and S8's re-staging of every existing arm
  that makes a claim stale by planting an old `beat-utc` or seeds a lease with `renews: no` (the
  five-verdict AC2 arm, the `foreign-stale` rows of the claim-table arm, AC5, AC8, AC18, AC19, GH36
  AC6, DPR1 AC2, and any other the build-time `git grep` of AC9 finds), each re-staged on planted
  feed lines so it keeps its verdict under the observer clock
- `tools/unattended/STOPS.template.md`: the verdict table
- `memory/guides/UNATTENDED-STOPS.md`: its render
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads,
  so `gen_map.py --check` exits 0 after the pass; `TOOL-dPlacedRequest-34` S38 is the final re-check
  only

### Alternatives rejected

- **The holder's stamp corrected by a measured offset.** v2:1160 admits it once dWellOiledMachine's
  supervisor measures offsets against the remote host; nothing measures one today.
- **The remote's push time.** Git keeps no server receive time a client can read; the commit's own
  stamps are the holder's clock.
- **A first-sighting cache beside the feed.** The feed already holds the stamp under the same key,
  and a second store is a second copy of one fact.

## 5. Production-readiness checklist

- security — no new input: every stamp read is one this node wrote; a forged `beat-utc` no longer
  moves any verdict.
- perf / scale — one `git log`, one feed `awk` and one `date` per read, replacing one `date`; linear in
  a lease's writes.
- error / empty / loading states — an unsighted record reads `unknown`, never `stale`; a feed that
  cannot be read reads every age `-`.
- observability — `--claims` prints the observer age in its fourth field, so a reader sees what its
  own node measured.
- risks — a dead foreign run is taken over after 24 h of no renewal rather than 90 min of no beat; a
  run that records no transition reads stale 24 h after its last renewal (`TOOL-dPlacedRequest-1` §8 F5).
- testing — the probes of §6 and the suite arms of §7; the existing suite arms that stage a stale
  claim by its `beat-utc` or seed `renews: no` leases are re-staged on planted feed lines (S8, AC9),
  since the observer clock otherwise flips their verdicts.
- migration — none.
- user docs — `memory/guides/UNATTENDED-STOPS.md`'s verdict table; `help/loop.md` anchors the driver's verbs beside its `--claims` paragraph, and this unit adds no verb.

## 6. Acceptance criteria

- **AC1** — When a fixture lease's only commit carries `renews: yes` and a `beat-utc` 25 hours before now,
  as a holder a day behind the reader stamps it, and this node sights it now, `--claims` prints it
  `live` with a fourth field under 60; a scratch copy of the driver whose age pass reads `beat-utc`
  prints it `stale`. This is the clause's reader whose clock runs a day ahead.
  Red when: the age is the reader's clock minus the holder's stamp.
  fixture: a scratch clone with a bare origin, `RUN_CLAIMS=on` and a feed the probe plants.
- **AC2** — When the same lease's feed line is planted with `seen-utc` 25 hours ago, `--claims` prints
  it `stale`; with `leases.expiry-hours` planted 48 it prints `live`.
  Red when: an unrenewed lease never expires, or the bound is not read.
- **AC3** — When the lease's chain is a `renews: yes` commit sighted 25 hours ago and a `renews: no`
  beat sighted a minute ago, `--claims` prints it `stale` with a fourth field under 120; with that beat
  planted `renews: yes`, it prints `live`.
  Red when: a fence beat with no witness renews the lease.
- **AC4** — When the lease's renewing commit carries `renews: -` and was sighted 1,000 hours ago,
  `--claims` prints it `live`.
  Red when: `leases.renewal: none` still expires.
- **AC5** — When `check_deadline_passed <ref> <sha> 300` runs over a record sighted 60 s ago whose
  `offer-deadline` field names a time a day past, it returns 1, and over one sighted 400 s ago it returns
  0; with the bound 604800, a tombstone sighted 6 days ago whose `beat-utc` reads 8 days ago returns 1,
  and one sighted 8 days ago returns 0; an unsighted sha returns 2. These are the clause's offer that must
  not pass early and tombstone that must not be pruned early, on a reader a day ahead.
  Red when: a stamp the record carries decides the deadline.
- **AC6** — When the feed is deleted after the fetch and before the age pass, `--claims` prints every
  row `unknown` with age `-`, and none `stale`.
  Red when: an unsighted record expires.
- **AC7** — When `grep -n 'first saw\|leases.expiry-hours\|leases.queued-claim-days\|leases.offer-seconds'`
  runs over `STOPS.template.md`, each is found in section 7.
  Red when: the guide still states the stale bound as the beat's age.
- **AC8** — When a fixture lease's chain is three commits at one `epoch`, all carrying `renews: no`,
  its opener's feed line planted with `seen-utc` 23 hours ago and the two later commits' a minute ago,
  `--claims` prints it `live`; with the opener's line planted 25 hours ago it prints `stale`. With the
  same tenure parented on a legacy `refs/gov/runs/*` chain whose commits carry no `renews` and were
  sighted a minute ago, both verdicts are unchanged.
  Red when: a tenure with no renewing commit reads `unknown`, never expires, or is renewed by a legacy
  commit beneath its opener.
  fixture: the AC1 scratch clone, its chain planted by `commit-tree` with explicit parents.
  figure: 23 and 25 hours PINNED, either side of the 24-hour default of `leases.expiry-hours`.
- **AC9** — When `git grep -n -e 'beat-utc' -e 'renews: no' -e seed_claim -e seed_lease -e seed_su_claim
  tools/unattended/unattended.test.sh` runs at build time, every arm it reaches that expects a `stale`
  verdict, a take-over or a refusal of a live claim plants its sighting as a feed line in the unit's
  diff, and `git diff` over the suite changes no expected verdict of those arms, only their staging;
  the builder's return lists that inventory, arm by label.
  Red when: an existing arm's expected verdict is edited to fit the observer clock, or an arm staging
  staleness by `beat-utc` alone is left unstaged.
  figure: the inventory's size is DERIVED by the `git grep` above at build time.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `scratch-guard self-test` · `tier2-review self-test` · `policy fixtures` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC8 · the clock arms over planted feed lines and lease chains, staged by a scratch copy whose age pass reads `beat-utc` · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14, and each covered criterion's own probe is the observation at landing
New arm: tools/unattended/unattended.test.sh · covers AC9 · S8's moved arms, staged red by running each inventoried arm's `beat-utc`-only staging against the observer-clock driver, then green on its planted feed lines · none, the arms' count is unchanged

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation, 2026-10-25: the tuple holds
  `OPEN`, `SPECCED`, `INPROGRESS`, `BLOCKED`, `DEFERRED`, `CLOSED` and `WONTDO`, and not `DRAFT`.
  Liveness: the tuple would show `DRAFT` if the vocabulary held it. RESOLVED (agent, 2026-10-25,
  delegated): `OPEN`, rung 2.
- **F2 — Does the expiry bound replace `RESUME_STALE_BOUND` in the claim verdict?** (a) Yes: `stale`
  is the expired lease, the one a take-over may take (coordination.md:89-91); (b) keep the beat bound
  for run claims and add the expiry beside it. (b) keeps a reader-clock age for runs, which the clause
  forbids for every lease, and run claims are build leases since `TOOL-dPlacedRequest-1`. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 1. widens: none · relaxes: none
- **F3 — What does a reader do with a record its feed has not sighted?** (a) `unknown`, never stale;
  (b) treat it as sighted now. (b) silently restarts a clock whenever a feed line is lost, and (a) is
  the DEAD PROBE rule the reader already applies to an unparsable stamp. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — Where does the clause's offer and prune judgment live, when the offer and the tombstone are
  later units'?** (a) Here, as `check_deadline_passed`, observed by its own probe and called by those
  units; (b) in each later unit. (b) spells the observer rule twice more. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F5 — What anchors the age of a lease whose chain carries no renewing commit?** (a) `unknown`, so it
  never expires and is never taken over; (b) the current tenure's opening commit counts as a renewing
  beat whatever its `renews` line says, so its first sighting anchors the age; (c) stale at once.
  RESOLVED (agent, 2026-11-19, delegated): (b), rung 3; (a) fails §5's own take-over risk and §4
  Rollout, (c) lets any node take a live run, a second driver (veto 3); TOOL-dPlacedRequest-25 makes
  the writer stamp the opener `renews: yes`, and this reader rule holds without it. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 17, scout A row 7 and Shared interface 6,
  v2:680, v2:1160, :1163-1164 and research-cloud-headless S4.
- rev-2 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-26,
  hands-off TOOL-dPlacedRequest-34, each the mirror of that promoted unit's own edge.
- rev-3 · 2026-11-19 · §4 Files touched · §7 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit`: finding 24 (H6), the kit version is the lander's to mint; finding 4 (M3), the unattended.test.sh arm cites README rule 8 and owes its clean reading to PLAY-dClosedLoop-14. §7 also names `scratch-guard self-test`, `tier2-review self-test`, `policy fixtures`, the leg(s) the spec-token guard join names for this spec's Files touched.
- rev-4 · 2026-11-19 · §4 Files touched · §5 · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 16 (M7), the user-docs line names
  `help/loop.md`, which anchors the driver's verbs; finding 17 (M8), this unit's own pass
  regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.
- rev-5 · 2026-11-19 · §1 · §2 S2 S3 S7 S8 · §3 · §4 · §5 · §6 AC8 AC9 · §7 · §8 F5 · §10 · folds
  `2026-11-19-prompt-TOOL-dPlacedRequest-17-divergence-brief`, the main loop's ruling on the builder's
  DIVERGENCE of run `wf_47eb729e-d38`: F5 resolved (b), a tenure with no renewing commit is aged from
  its opener (AC8); S2 and §4 step 2 state one commit set, the walk from each row's tip that stops at
  the current tenure's opener (hands-off TOOL-dPlacedRequest-26); S8 and AC9 re-stage the existing
  suite arms the observer clock flips; the four stale line citations name `read_claims`,
  `check_claim_writable` and section 7's `| claim | verdict |` table.

## 10. Reuse audit

The seam extended is `read_claims`' age pass (`tools/unattended/unattended.sh#read_claims`): its one
`date -f` and its DEAD PROBE rule stay, and only the stamps it ages change source, from the holder's
`beat-utc` to the change feed's first sighting (`TOOL-dPlacedRequest-13`, I4). `python
tools/codebase-map/reuse_lookup.py "age of a claim judged by the reader clock"` ranked `read`,
`read_text`, `claims` and `read_host_name`, name stems only; `read_claims`, whose age pass the gap
register's gap-conc-14 cites, is the seam, and no existing function reads a first sighting. Scout A's
row 7 holds against source: the age is `age[1] - age[$11 + 1]` in `read_claims`' verdict `awk`
(re-read 2026-11-19). `python
tools/memory-recall/query.py "how is a claim's age judged and what clock does it read"` returned scout
A's row 7 and its opening finding, the brief's unit row, the night-pass instruments' copy of the lease rows and
the as-built view; none disagrees with source.

Recall terms used: observer clock first seen expiry-hours beat-utc reader clock skew read_claims age stale offer tombstone prune
