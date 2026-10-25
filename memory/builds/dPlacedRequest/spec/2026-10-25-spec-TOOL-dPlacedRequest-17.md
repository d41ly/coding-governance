# TOOL-dPlacedRequest-17 — every lease deadline judged by the observer clock: expiry, an offer's deadline and a tombstone's prune age

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 4 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0135@55365bfa whole
**Carries:** node:policy-key.leases.expiry-hours
**Carries:** node:policy-key.leases.queued-claim-days

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

A deadline one node judges on a record another node stamped is judged by a declared clock: the time
since this node first saw the record, on this node's own clock, never this node's clock minus the
holder's stamp (v2:680, v2:1160, research-cloud-headless S4). Today `read_claims` ages every claim as
`age[1] - age[$11 + 1]`, the reader's `date` minus the holder's `beat-utc`
(`tools/unattended/unattended.sh:2180`), so a reader whose clock runs a day ahead reads every claim a
day old and a reader a day behind never expires one (gap-conc-14). The change feed of
`TOOL-dPlacedRequest-13` already stamps each tip with the time this node first saw it; this unit reads
those stamps and makes every lease deadline a function of them.

## 2. Scope (IN)

- **S1** — The observer clock (I8), `read_first_seen`, in the `gov_feed_sh` block beside
  `add_feed_event`: given `<ref><TAB><sha>` pairs on stdin, one `awk` over `gov-feed.log` prints, per
  pair, the `seen-utc` of that key's line, or `-` when the feed holds none. It is the one reader of a
  first sighting. Observed by AC1 and AC5.
- **S2** — The renewing beat: for each lease row, the newest commit on its first-parent chain whose
  `renews` reads `yes` (a legacy run claim, which carries no `renews`, reads every commit as renewing),
  found for every row by one `git log --topo-order --first-parent` over the cached lease refs, each
  commit naming its lease by its `gov-claim <tail>` header. Observed by AC3.
- **S3** — The age pass of `read_claims` (`:2172-2186`): field 4, `beat-age-s`, becomes now minus the
  first sighting of the row's tip, and the verdict reads `stale` when now minus the first sighting of the
  renewing beat exceeds `leases.expiry-hours`, both on this node's clock through one `date -f` call.
  A row whose renewing beat carries `renews: -` (`leases.renewal: none`) never reads `stale`; a row
  whose tip or renewing beat the feed has not sighted reads `unknown` with age `-`, never `stale`.
  `held` and `terminal` keep their verdicts. Observed by AC1, AC2, AC3, AC4 and AC6.
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
- **S7** — The stops guide's verdict table (`tools/unattended/STOPS.template.md:198-204`, rendered to
  `memory/guides/UNATTENDED-STOPS.md`) states the observer rule, the three bounds and the `unknown` row
  for an unsighted record. Observed by AC7.

## 3. Non-goals (OUT)

- No offer and no tombstone: `TOOL-dPlacedRequest-20` writes the offer and calls S4 for its deadline,
  and `TOOL-dPlacedRequest-16` writes tombstones and calls S4 for their prune age.
- No clock offset from the remote host's time: v2:1160's second rule is dWellOiledMachine's supervisor's,
  once it measures each node's offset at each beat; the observer rule stands alone until then.
- No change to the renewal rule itself: when a write renews is `leases.renewal`'s, set by
  `TOOL-dPlacedRequest-1`; this unit judges what the record says.
- No change to `RESUME_STALE_BOUND`'s other readers: the run-state liveness and the holder's quarter-bound
  due rule (`:2269-2275`) keep it; the due rule now reads the tip's observer age.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-13` — `gov-feed.log`, whose first `seen-utc` per key is the clock
- **consumes-from** `TOOL-dPlacedRequest-1` — `refs/gov/leases/<slug>/build`, its `renews` field and `read_lease_policy`
- **hands-off** `TOOL-dPlacedRequest-16` — `read_first_seen` and `check_deadline_passed`, which judge a tombstone's prune age and a queued claim's age
- **hands-off** `TOOL-dPlacedRequest-20` — `read_first_seen` and `check_deadline_passed`, which judge an offer's deadline
- **hands-off** `TOOL-dPlacedRequest-26` — the age pass's walk and verdict `awk`, which that unit bounds to the current holder's tenure
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### The rule

```
age(record) = now(this node) - seen-utc(this node's first sighting of the record)
expired     = age(the newest renewing beat) > leases.expiry-hours
offer open  = age(the commit that set the offer) <= leases.offer-seconds
prunable    = age(the terminal tombstone) > leases.queued-claim-days
```

Both terms of every age are read on one node's clock, so a constant skew cancels: a reader a day ahead
stamped its sighting a day ahead too. What the rule does not see is a clock STEPPED between the sighting
and the judgment, which moves that node's ages by the step; it never moves another node's.

### The age pass

1. After the fetch, `TOOL-dPlacedRequest-13`'s `add_feed_sightings` has appended every unseen chain
   commit, so every cached tip and renewing beat normally has a line.
2. One `git log --topo-order --first-parent --format='%x01%H%n%B' <every cached lease and legacy ref>`;
   one `awk` keeps, per `gov-claim` tail, the first commit seen (the tip, since a child precedes its
   parent in topo order) and the first whose `renews` is `yes` or absent.
3. `read_first_seen` over the tip and renewing pairs, then one `date -u -f` over `now` and every
   stamp, with the DEAD PROBE rule unchanged (`:2174-2176`): a count mismatch reads every age `-`.
4. The verdict `awk` (`:2178-2185`) compares the renewing age with the expiry bound instead of the
   tip's beat age with `RESUME_STALE_BOUND`.

A chain grows by one commit per write, so step 2 reads every write a lease has had; at a write a minute
for a day that is 1,440 commits per lease, under 0.6 MB, read in one process.

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
`RESUME_STALE_BOUND` (5400 s in `.unattended.conf:95`) after its last beat to `leases.expiry-hours`
(24 h) after its last renewing beat, the ratified expiry (night-pass-two:281).

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: `read_first_seen`
- `tools/unattended/unattended.sh`: the inline block, the age pass, `check_deadline_passed`,
  `read_lease_bound`, `KIT_UNATTENDED_VERSION` moved
- `tools/run-gates/post-merge.sh`: the inline block, carried
- `tools/run-gates/run-gates.sh`: `KIT_RUN_GATES_VERSION` moved
- `tools/unattended/unattended.test.sh`: the clock arms
- `tools/unattended/STOPS.template.md`: the verdict table
- `memory/guides/UNATTENDED-STOPS.md`: its render
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`

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
- testing — the probes of §6 and the suite arms of §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-STOPS.md`'s verdict table; no `help/` page covers the kit.

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

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the clock arms over planted feed lines and lease chains, staged by a scratch copy whose age pass reads `beat-utc` · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff

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

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 17, scout A row 7 and Shared interface 6,
  v2:680, v2:1160, :1163-1164 and research-cloud-headless S4.
- rev-2 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-26,
  hands-off TOOL-dPlacedRequest-34, each the mirror of that promoted unit's own edge.

## 10. Reuse audit

The seam extended is `read_claims`' age pass (`tools/unattended/unattended.sh:2172-2186`): its one
`date -f` and its DEAD PROBE rule stay, and only the stamps it ages change source, from the holder's
`beat-utc` to the change feed's first sighting (`TOOL-dPlacedRequest-13`, I4). `python
tools/codebase-map/reuse_lookup.py "age of a claim judged by the reader clock"` ranked `read`,
`read_text`, `claims` and `read_host_name`, name stems only; `read_claims`, which the gap register's
gap-conc-14 cites at exactly these lines, is the seam, and no existing function reads a first sighting.
Scout A's row 7 holds against source: the age is `age[1] - age[$11 + 1]` at `:2180`. `python
tools/memory-recall/query.py "how is a claim's age judged and what clock does it read"` returned scout
A's row 7 and its opening finding, the brief's unit row, the night-pass instruments' copy of the lease rows and
the as-built view; none disagrees with source.

Recall terms used: observer clock first seen expiry-hours beat-utc reader clock skew read_claims age stale offer tombstone prune
