---
slug: dPlacedRequest
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-22 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49
spec-audit: 2026-10-21
parents: dDeclaredLoop
may: PLAY-dClosedLoop-3
---

# dPlacedRequest — the Entry build of the dClosedLoop chain

## The problem this build exists to solve

dPlacedRequest owns 18 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-flow-07,
gap-conc-01, gap-conc-02, gap-orient-01, gap-orient-02, gap-orient-04, gap-orient-11, gap-flow-18, gap-orient-20,
gap-conc-06, gap-conc-07, gap-conc-08, gap-conc-12, gap-conc-13, gap-conc-14, gap-conc-17, gap-conc-18, gap-conc-19.
Closing every one is this build's goal bound.

## Expected improvements

- Each of the 21 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 18 owned gaps above close.

## Detriments if this is not built

- Its 18 owned gaps stay open.
- Its 3 child builds wait on it: dKeptSession, dBoundRoles, dTotalRecall.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dPlacedRequest` green before the first pass; a moved instrument blob
  is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dPlacedRequest`, a record per member "recorded by nobody", the same with `--write` (commit
  it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-14.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dPlacedRequest-1` | `cl-dClosedLoop-0120@5d655f07` | the coordination feature: one lease grammar for builds |
| 2 | `TOOL-dPlacedRequest-2` | `cl-dClosedLoop-0121@2f58beed` | the build's orientation card at level 1 |
| 3 | `TOOL-dPlacedRequest-3` | `cl-dClosedLoop-0122@938c9643` | the entry step's items: the card's orientation |
| 4 | `TOOL-dPlacedRequest-4` | `cl-dClosedLoop-0123@626c316e` | the placement predicate and its check |
| 5 | `TOOL-dPlacedRequest-5` | `cl-dClosedLoop-0503@65f19d46` | the `breakpoint` disposition in the placement set: an owner's request for a review on a live build |
| 6 | `TOOL-dPlacedRequest-6` | `cl-dClosedLoop-0124@b8ada8e4` | the items' declarations of the `map` slot and their unfolds |
| 7 | `TOOL-dPlacedRequest-7` | `cl-dClosedLoop-0125@4e0727e5` | the probe program (`probe.trigger` |
| 8 | `TOOL-dPlacedRequest-8` | `cl-dClosedLoop-0126@b35ab44f` | each item's declared code seed: its write set |
| 9 | `TOOL-dPlacedRequest-9` | `cl-dClosedLoop-0127@4f0c1452` | the kickoff manifest's facts as level-2 instruction units the card reads (the memory plan's `[pockets]`) |
| 10 | `TOOL-dPlacedRequest-10` | `cl-dClosedLoop-0128@e0109d47` | a build's scenarios chosen at `entry.place`: the orientation scout's return naming each scenario whose admission predicate holds over the request's facts |
| 11 | `TOOL-dPlacedRequest-11` | `cl-dClosedLoop-0129@30a0ceda` | each lease and claim written as a commit whose parent is its ref's previous tip |
| 12 | `TOOL-dPlacedRequest-12` | `cl-dClosedLoop-0130@57d242df` | create-only registers on the remote |
| 13 | `TOOL-dPlacedRequest-13` | `cl-dClosedLoop-0131@3532cbe6` | the change feed: an ordered |
| 14 | `TOOL-dPlacedRequest-14` | `cl-dClosedLoop-0132@6096ecb9` | the pre-claim budget: placement loops before `entry.claim` drawing on a budget keyed to the request's content key |
| 15 | `TOOL-dPlacedRequest-15` | `cl-dClosedLoop-0133@231564d8` | the fenced effect push: every effect push carrying the holder's new lease beat in one atomic push under a compare-and-swap on the lease tip it read |
| 16 | `TOOL-dPlacedRequest-16` | `cl-dClosedLoop-0134@bacb3ef7` | a lease never deleted: each release a hand-over |
| 17 | `TOOL-dPlacedRequest-17` | `cl-dClosedLoop-0135@55365bfa` | a lease's expiry |
| 18 | `TOOL-dPlacedRequest-18` | `cl-dClosedLoop-0136@c9686488` | the cadence segment of the lease grammar taking any name the tag grammar admits |
| 19 | `TOOL-dPlacedRequest-19` | `cl-dClosedLoop-0137@39b3ef9d` | a request that is not yet a build written as a project-level record any node may claim by lease |
| 20 | `TOOL-dPlacedRequest-20` | `cl-dClosedLoop-0138@b6141505` | lease acquisition taking an optional offer |
| 21 | `TOOL-dPlacedRequest-21` | `cl-dClosedLoop-0501@e1101a14` | `entry.claim` writing a patch or repeat build's derived plan record |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 48 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13
ids TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-22 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25
ids TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37
ids TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dPlacedRequest-11 — one compare-and-swap writer for every governance ref, each commit parented on the tip it read, and no lock the lander holds](spec/2026-10-25-spec-TOOL-dPlacedRequest-11.md) | 1 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-13 — the change feed: every governance ref write appended once on its node, replayable and rebuilt equal from git](spec/2026-10-25-spec-TOOL-dPlacedRequest-13.md) | 2 | 2 | OPEN | rev-4 | 2026-10-25 |
| [TOOL-dPlacedRequest-1 — one lease grammar for builds, units and cadence runs, with an epoch, run claims migrated onto it, and its verbs and four policy keys](spec/2026-10-25-spec-TOOL-dPlacedRequest-1.md) | 3 | 2 | OPEN | rev-4 | 2026-10-25 |
| [TOOL-dPlacedRequest-27 — the change feed skips only an immediate retry: the append-once test reads the ref's newest event](spec/2026-10-25-spec-TOOL-dPlacedRequest-27.md) | 3 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dPlacedRequest-17 — every lease deadline judged by the observer clock: expiry, an offer's deadline and a tombstone's prune age](spec/2026-10-25-spec-TOOL-dPlacedRequest-17.md) | 4 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-23 — a strict claim read stays strict: `leases.offline` never reaches the preflight, a take-over or the close](spec/2026-10-25-spec-TOOL-dPlacedRequest-23.md) | 4 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-24 — the offline queue under one guarded node lock, appended once and flushed honestly](spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md) | 4 | 2 | OPEN | rev-4 | 2026-10-25 |
| [TOOL-dPlacedRequest-25 — a write that opens a holder's tenure renews the lease](spec/2026-10-25-spec-TOOL-dPlacedRequest-25.md) | 4 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dPlacedRequest-16 — a lease never deleted: a release is a hand-over or a terminal tombstone, the epoch rises for life, and only a run's tombstone is ever pruned](spec/2026-10-25-spec-TOOL-dPlacedRequest-16.md) | 5 | 2 | OPEN | rev-4 | 2026-10-25 |
| [TOOL-dPlacedRequest-26 — the renewing-beat walk stops at the current holder's tenure](spec/2026-10-25-spec-TOOL-dPlacedRequest-26.md) | 5 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-36 — the node-lock factory writes its health events through the lock's own common dir](spec/2026-10-25-spec-TOOL-dPlacedRequest-36.md) | 5 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-37 — the node lock's deadline is the block's own bound, never the driver's `REMOTE_BOUND`](spec/2026-10-25-spec-TOOL-dPlacedRequest-37.md) | 5 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-38 — the parity leg runs every inline `gov_feed_sh` copy under `set -u` with nothing from its carrier](spec/2026-10-25-spec-TOOL-dPlacedRequest-38.md) | 5 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-39 — a feed append that aborts never takes its carrier down](spec/2026-10-25-spec-TOOL-dPlacedRequest-39.md) | 5 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-41 — a second offline write to a queued lease chains on the queued commit](spec/2026-10-25-spec-TOOL-dPlacedRequest-41.md) | 5 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-20 — a lease acquisition that honours an offer, and the epoch fence on a stale take](spec/2026-10-25-spec-TOOL-dPlacedRequest-20.md) | 6 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-18 — the cadence segment of the lease grammar takes any tag-grammar name](spec/2026-10-25-spec-TOOL-dPlacedRequest-18.md) | 7 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-28 — every create of a lease ref reads the feed first, the offer's included](spec/2026-10-25-spec-TOOL-dPlacedRequest-28.md) | 7 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-12 — create-only decision and problem registers on the remote](spec/2026-10-25-spec-TOOL-dPlacedRequest-12.md) | 8 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-42 — an offline lease create reads the feed first, as every create on an empty parent does](spec/2026-10-25-spec-TOOL-dPlacedRequest-42.md) | 8 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-15 — the fenced effect push: the lander's push carries the holder's lease beat atomically](spec/2026-10-25-spec-TOOL-dPlacedRequest-15.md) | 9 | 2 | OPEN | rev-4 | 2026-10-25 |
| [TOOL-dPlacedRequest-19 — the project-level request record: pushed by its content key, its text kept where it was typed](spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md) | 10 | 2 | OPEN | rev-4 | 2026-10-25 |
| [TOOL-dPlacedRequest-29 — the lander's fence survives its own holder's write: a same-holder move re-fences and retries](spec/2026-10-25-spec-TOOL-dPlacedRequest-29.md) | 10 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-30 — a request whose words key alike but differ is refused, never merged](spec/2026-10-25-spec-TOOL-dPlacedRequest-30.md) | 11 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-31 — consent is bound to the bytes a session typed](spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md) | 11 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-32 — an absent session is no identity: no consent, and no lease held on session alone](spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md) | 11 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-9 — the kickoff manifest's facts as level-2 instruction units the card reads](spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md) | 11 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-2 — the build's orientation card kept per build: a remote ref, a clone cache and a snapshot, following its build](spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md) | 12 | 2 | OPEN | rev-4 | 2026-10-25 |
| [TOOL-dPlacedRequest-40 — the id-less refusal gates the holder acts by name and lets every other lease act run](spec/2026-10-25-spec-TOOL-dPlacedRequest-40.md) | 12 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-33 — the card's remote ref is written by the driver, dark behind `RUN_CLAIMS`](spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md) | 13 | 2 | OPEN | rev-4 | 2026-10-25 |
| [TOOL-dPlacedRequest-8 — each item's declared code seed: its write set, its scope paths or its question's paths](spec/2026-10-25-spec-TOOL-dPlacedRequest-8.md) | 13 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-6 — the items' declarations of the `map` slot and their unfolds](spec/2026-10-25-spec-TOOL-dPlacedRequest-6.md) | 14 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-7 — the probe program: eight items, the `probe` and `probe-trigger` records, and the four `probe.*` keys](spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md) | 15 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-4 — the placement predicate and its check: a disposition for every request, recorded with its reason](spec/2026-10-25-spec-TOOL-dPlacedRequest-4.md) | 16 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-10 — a build's scenarios chosen at `entry.place`, every admission predicate re-evaluated by `placement.check`](spec/2026-10-25-spec-TOOL-dPlacedRequest-10.md) | 17 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-14 — the pre-claim budget: placement loops before `entry.claim` drawing on a budget keyed to the request's content key](spec/2026-10-25-spec-TOOL-dPlacedRequest-14.md) | 18 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-5 — the `breakpoint` disposition: an owner's request for a review on a live build, fired through `review.trigger`](spec/2026-10-25-spec-TOOL-dPlacedRequest-5.md) | 19 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-21 — `entry.claim`: the claim ref, a patch or repeat build's derived plan record, `patch.ratify`, and every refusal routed by its cause](spec/2026-10-25-spec-TOOL-dPlacedRequest-21.md) | 20 | 2 | OPEN | rev-4 | 2026-10-25 |
| [TOOL-dPlacedRequest-3 — the entry step's five items: the card's orientation, the three placing items and the claim](spec/2026-10-25-spec-TOOL-dPlacedRequest-3.md) | 21 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-34 — the round-1 spec audit's minors: one fetch and one cache, honest censuses and counts, every reader of a moved name, and bounded walks](spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md) | 22 | 2 | OPEN | rev-5 | 2026-10-25 |
| [TOOL-dPlacedRequest-35 — the bounded age walk ends a tail at its tenure before it reads an age](spec/2026-10-25-spec-TOOL-dPlacedRequest-35.md) | 23 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-43 — the round-1 promotions' minors: behavioural class checks, honest outcomes, every reader of a changed spelling, and the sizes kept](spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md) | 24 | 2 | OPEN | rev-3 | 2026-10-25 |
| [TOOL-dPlacedRequest-46 — the bounded age walk stops on a `renews: -` commit before any threshold test](spec/2026-10-25-spec-TOOL-dPlacedRequest-46.md) | 24 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-47 — the bounded age walk never compares an unsighted commit with the threshold](spec/2026-10-25-spec-TOOL-dPlacedRequest-47.md) | 24 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-44 — the version-bump oracle walks the build's side of the prepared merge](spec/2026-10-25-spec-TOOL-dPlacedRequest-44.md) | 25 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-45 — the default-branch merge class names the walk from a prepared merge, and selects the file that builds one](spec/2026-10-25-spec-TOOL-dPlacedRequest-45.md) | 25 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-48 — the request-lock race is placed by an announcing stub, not left to the scheduler](spec/2026-10-25-spec-TOOL-dPlacedRequest-48.md) | 25 | 2 | OPEN | rev-2 | 2026-10-25 |
| [TOOL-dPlacedRequest-49 — the round-2 promotions' minors: one bound per question, traps before takes, every carrier observed, and criteria that can fail](spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md) | 26 | 2 | OPEN | rev-2 | 2026-10-25 |
<!-- /gen:build-units -->

Records: 52 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49.

Ids whose spec moved past its audited revision: TOOL-dPlacedRequest-1@rev-2 TOOL-dPlacedRequest-10@rev-1 TOOL-dPlacedRequest-11@rev-2 TOOL-dPlacedRequest-12@rev-2 TOOL-dPlacedRequest-13@rev-2 TOOL-dPlacedRequest-14@rev-2 TOOL-dPlacedRequest-15@rev-2 TOOL-dPlacedRequest-16@rev-2
TOOL-dPlacedRequest-17@rev-1 TOOL-dPlacedRequest-18@rev-2 TOOL-dPlacedRequest-19@rev-2 TOOL-dPlacedRequest-2@rev-2 TOOL-dPlacedRequest-20@rev-2 TOOL-dPlacedRequest-21@rev-2 TOOL-dPlacedRequest-23@rev-1 TOOL-dPlacedRequest-24@rev-2 TOOL-dPlacedRequest-26@rev-1 TOOL-dPlacedRequest-28@rev-1
TOOL-dPlacedRequest-29@rev-1 TOOL-dPlacedRequest-3@rev-1 TOOL-dPlacedRequest-30@rev-2 TOOL-dPlacedRequest-31@rev-2 TOOL-dPlacedRequest-32@rev-2 TOOL-dPlacedRequest-33@rev-2 TOOL-dPlacedRequest-34@rev-2 TOOL-dPlacedRequest-35@rev-1 TOOL-dPlacedRequest-36@rev-1 TOOL-dPlacedRequest-37@rev-1
TOOL-dPlacedRequest-38@rev-1 TOOL-dPlacedRequest-39@rev-1 TOOL-dPlacedRequest-4@rev-2 TOOL-dPlacedRequest-40@rev-1 TOOL-dPlacedRequest-41@rev-1 TOOL-dPlacedRequest-42@rev-1 TOOL-dPlacedRequest-43@rev-2 TOOL-dPlacedRequest-5@rev-1 TOOL-dPlacedRequest-6@rev-1 TOOL-dPlacedRequest-7@rev-2
TOOL-dPlacedRequest-8@rev-2 TOOL-dPlacedRequest-9@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dPlacedRequest's 21 clause(s) and 37 owned node(s), over 48 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 21
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-25-spec-TOOL-dPlacedRequest-23.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-25.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-25-spec-TOOL-dPlacedRequest-26.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-27.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-28.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-29.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-25-spec-TOOL-dPlacedRequest-30.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-35.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-36.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-37.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-25-spec-TOOL-dPlacedRequest-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-39.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-40.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-41.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-25-spec-TOOL-dPlacedRequest-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-44.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-45.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-25-spec-TOOL-dPlacedRequest-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-47.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-48.md` (PLAY-dClosedLoop-2), `spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0122, cl-dClosedLoop-0126, cl-dClosedLoop-0129, cl-dClosedLoop-0133, cl-dClosedLoop-0136, cl-dClosedLoop-0137
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dPlacedRequest-11` | no |
| 2 | `TOOL-dPlacedRequest-13` | no |
| 3 | `TOOL-dPlacedRequest-1`, `TOOL-dPlacedRequest-27` | yes |
| 4 | `TOOL-dPlacedRequest-17`, `TOOL-dPlacedRequest-23`, `TOOL-dPlacedRequest-24`, `TOOL-dPlacedRequest-25` | yes |
| 5 | `TOOL-dPlacedRequest-16`, `TOOL-dPlacedRequest-26`, `TOOL-dPlacedRequest-36`, `TOOL-dPlacedRequest-37`, `TOOL-dPlacedRequest-38`, `TOOL-dPlacedRequest-39`, `TOOL-dPlacedRequest-41` | yes |
| 6 | `TOOL-dPlacedRequest-20` | no |
| 7 | `TOOL-dPlacedRequest-18`, `TOOL-dPlacedRequest-28` | yes |
| 8 | `TOOL-dPlacedRequest-12`, `TOOL-dPlacedRequest-42` | yes |
| 9 | `TOOL-dPlacedRequest-15` | no |
| 10 | `TOOL-dPlacedRequest-19`, `TOOL-dPlacedRequest-29` | yes |
| 11 | `TOOL-dPlacedRequest-30`, `TOOL-dPlacedRequest-31`, `TOOL-dPlacedRequest-32`, `TOOL-dPlacedRequest-9` | yes |
| 12 | `TOOL-dPlacedRequest-2`, `TOOL-dPlacedRequest-40` | yes |
| 13 | `TOOL-dPlacedRequest-33`, `TOOL-dPlacedRequest-8` | yes |
| 14 | `TOOL-dPlacedRequest-6` | no |
| 15 | `TOOL-dPlacedRequest-7` | no |
| 16 | `TOOL-dPlacedRequest-4` | no |
| 17 | `TOOL-dPlacedRequest-10` | no |
| 18 | `TOOL-dPlacedRequest-14` | no |
| 19 | `TOOL-dPlacedRequest-5` | no |
| 20 | `TOOL-dPlacedRequest-21` | no |
| 21 | `TOOL-dPlacedRequest-3` | no |
| 22 | `TOOL-dPlacedRequest-34` | no |
| 23 | `TOOL-dPlacedRequest-35` | no |
| 24 | `TOOL-dPlacedRequest-43`, `TOOL-dPlacedRequest-46`, `TOOL-dPlacedRequest-47` | yes |
| 25 | `TOOL-dPlacedRequest-44`, `TOOL-dPlacedRequest-45`, `TOOL-dPlacedRequest-48` | yes |
| 26 | `TOOL-dPlacedRequest-49` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dDeclaredLoop](../dDeclaredLoop/README.md)
- **Child builds:** [dBoundRoles](../dBoundRoles/README.md), [dKeptSession](../dKeptSession/README.md), [dTotalRecall](../dTotalRecall/README.md)
<!-- /gen:build-edges -->
