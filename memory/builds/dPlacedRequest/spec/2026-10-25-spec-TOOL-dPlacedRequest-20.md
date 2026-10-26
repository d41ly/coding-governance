# TOOL-dPlacedRequest-20 — a lease acquisition that honours an offer, and the epoch fence on a stale take

**Status:** DEFERRED · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 6 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0138@b6141505 whole
**Carries:** node:policy-key.leases.offer-seconds

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

Let something outside a node offer it work without assigning it. A lease may carry an offer, the
fleet tag of the node it was made for and a window of `leases.offer-seconds`; inside the window only
that node may acquire the lease, and once the window passes the offer is ignored and any node may
claim. Every acquisition stays a compare-and-swap on the lease tip it read, so a take built from an
old read, and so an old epoch, is refused as `epoch-fence` (gap-conc-19; P40, the owner's CL-2).

## 2. Scope (IN)

- **S1** — The offer write: `unattended.sh --lease offer <kind> <name> [<sub>] --to <fleet tag>`, a new
  act of TOOL-dPlacedRequest-1's `--lease` verb, writes the lease record (I6) with `status: released`,
  `offer: <fleet tag>` and `offer-deadline: <seconds>`, the seconds `read_lease_bound offer` prints at
  the write. It builds the commit with `build_gov_commit <tip read> <message>` and writes it with
  `write_gov_ref <lease ref> <tip read> <commit>`, keeping the epoch it read; an absent lease is a
  create at epoch 1. It is legal on an absent lease and on a `released` one; a `live` or `held` lease
  refuses `live-holder`, a terminal one `terminal`, each on TOOL-dPlacedRequest-1's refusal line, and a
  tag `resolve_fleet_tag`'s registry does not hold is refused before any read. Observed by AC1, AC2.
- **S2** — The `offered` class: `CLAIM_READS` (`tools/unattended/unattended.sh:2219`) gains `offered`,
  derived for the `lease` mode TOOL-dPlacedRequest-1 adds when the record's `offer` names another fleet
  tag and `check_deadline_passed <lease ref> <tip> <offer-deadline>` returns 1, not yet. `acquire` and
  `take-over` reading `offered` print `lease refused — offered · <tail> · <target tag>` and write
  nothing; the `status` mode announces it, and `beat` declines it as it declines every foreign class.
  Observed by AC3.
- **S3** — The named node and the expired offer: for the node the offer names, and for every node once
  `check_deadline_passed` returns 0, the offer is ignored and the lease classes as the `released` lease
  it is. An acquisition writes `offer: -` and `offer-deadline: -`, so an acquired lease carries no
  stale offer. A record whose `offer` reads `-` carries no offer. Observed by AC4, AC5.
- **S4** — The unsighted offer: when `check_deadline_passed` returns 2, the feed has not seen the tip,
  and the offer holds, its window opening at this node's first sighting. A window that is not a whole
  number reads as an expired offer. Observed by AC5.
- **S5** — The epoch fence is TOOL-dPlacedRequest-1's: a create writes 1, a take the read epoch plus
  one, and a compare-and-swap lost between the read and the write is `epoch-fence` (its S3 and S6).
  This unit adds no second check and keeps both of its own writes inside that one: `--lease offer`
  keeps the epoch it read, and an acquisition of an offered lease derives its epoch from the read whose
  tip it compares and swaps. The clause's red case, an acquisition carrying an old epoch, is observed
  here. Observed by AC6.
- **S6** — The window's policy key: `leases.offer-seconds`, seconds, default `300` (v2:1164), whose
  catalogue row is dGroundRules-1 S3's, read through TOOL-dPlacedRequest-17's `read_lease_bound offer`
  and so through TOOL-dPlacedRequest-1's `read_lease_policy` and dGroundRules-2 S6's `resolve(key)`; the
  catalogue default stands until that reader resolves an unset key. Observed by AC7.
- **S7** — The documentation: the stops guide's section 7 gains the `offered` row of the mode by class
  table and the two record keys' meaning, and the verbs guide the `offer` act. Observed by AC8.

## 3. Non-goals (OUT)

- Who makes offers. The head that offers whole units across builds, its offer source registered at a
  point the core declares, is the `fleet` expansion's (v2:1898-1910, gap-conc-19's second half). This
  unit ships the record keys' behaviour, the write and the acquisition rule the head will call.
- Assignment of any kind. An offer reorders who may claim first; the named node still acquires by its
  own compare-and-swap, or does not (P40).
- The lease grammar, the record's other keys, the `--lease` verb's other acts, the `lease` mode and the
  epoch: TOOL-dPlacedRequest-1's. The observer clock and `check_deadline_passed`:
  TOOL-dPlacedRequest-17's. The change feed: TOOL-dPlacedRequest-13's.
- A queued offline claim's own age refusal: TOOL-dPlacedRequest-16's `last-fetch` rule.
- An explicit expected-epoch argument on the acquisition (§8 F2).
- The catalogue row: dGroundRules-1 S3 writes one row per v2 `[policies]` row, this key's among them.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-1` — the lease grammar `refs/gov/leases/<slug>/build` and its unit and run forms, the `--lease` verb and its `lease` mode, the record's `offer`, `offer-deadline` and `epoch` keys, `resolve_fleet_tag` and the refusal line; without it there is no lease to offer
- **consumes-from** `TOOL-dPlacedRequest-17` — `read_first_seen` behind `check_deadline_passed`, and `read_lease_bound offer`, the observer clock an offer's window is judged on and the window itself; without it the deadline would be judged on the reader's raw clock, which clause 0135 forbids
- **consumes-from** external — dGroundRules' catalogue row for `leases.offer-seconds` and its reader `python tools/policy/policy.py get <key>`, which the chain builds before this build's build run
- **hands-off** `TOOL-dPlacedRequest-28` — `write_lease_offer`'s absent-lease branch, which that unit routes through `read_feed_lease_tip`
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### Evidence

- The claim-read classes and modes are declared once, `CLAIM_READS` and `CLAIM_MODES`
  (`tools/unattended/unattended.sh:2219-2220`), and the mode by class table is the `case` in
  `check_claim_writable` (`:2243`, the table at `:2284-2301`); a class added there without a typed cell
  reds the suite's per-cell arm, so `offered` gets a cell in every mode column.
- A compare-and-swap write that lost reads `(stale info)` or `(fetch first)` on its porcelain line
  and returns 1 (`write_claim`, `:2434`); TOOL-dPlacedRequest-11 moves that parse into `write_gov_ref`
  unchanged (I1).
- The record is `key: value` lines under a `gov-claim <ref tail>` header, parsed by `read_claims`' awk,
  which takes the first value of each wanted key (`:2155-2172`); TOOL-dPlacedRequest-1 S2 adds `offer`
  and `offer-deadline` to that set, written `-` until this unit fills them.
- The fleet registry is `tools/playbook/fleet.toml`, one `[[node]]` row per tag (`:20-42`), read by
  `read_fleet` (`tools/playbook/render_playbook.py:347`), which TOOL-dPlacedRequest-1 S11 reaches
  through `resolve_fleet_tag`.

### The offer record

| Key | Value | Written by |
|---|---|---|
| `status` | `released` | `--lease offer` |
| `offer` | the target node's fleet tag, one registered tag | `--lease offer` |
| `offer-deadline` | an integer number of seconds, `read_lease_bound offer` at the write | `--lease offer` |
| `epoch` | the epoch read, unchanged; 1 on a create | `--lease offer` |

`offer-deadline` holds a window, never a timestamp, because a timestamp is a stamp one node writes
and another would compare with its own clock (clause 0135). The window is opened, on each node, by
that node's first sighting of the tip carrying the offer.

### The class derivation

The offer test sits before the identity rows of the class derivation, in the `lease` mode only:

```
offer   = record's `offer`; `-` or empty is no offer
window  = record's `offer-deadline`; not a whole number reads as expired
open    = check_deadline_passed <lease ref> <tip> <window> returns 1 or 2
offered = offer present, offer != resolve_fleet_tag's tag, and open
```

`offered` routes `acquire` and `take-over` to the refusal line, `status` to its announce line and
`beat` to its silent decline. A malformed window frees the lease rather than holding it for ever,
because an offer is advisory and a lease held by a typo would be an assignment.

### The epoch, and why the tip is the fence

```
read once -> (tip, epoch, record)
take      -> new epoch = epoch + 1, built on the same read
             write_gov_ref <lease ref> <tip> <new commit>
rc 1      -> lease refused — epoch-fence (TOOL-dPlacedRequest-1 S6), nothing written
```

The epoch moves only with the tip, so a compare-and-swap on the tip read refuses every acquisition
built from an older read, whatever epoch it carries. A planted take that re-reads the tip before its
push but keeps the old read's epoch writes a second record at an epoch already used; AC6's history
check reads that as red.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `offer` | an act of the `--lease` verb, with `--to <fleet tag>` | `tools/unattended/unattended.sh` |
| `write_lease_offer` | function | `tools/unattended/unattended.sh` |
| `offered` | claim-read class and refusal cause | `CLAIM_READS`, the refusal line |
| `offer`, `offer-deadline` | record keys, given behaviour here (I6 declares them) | the lease record |

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/STOPS.template.md`, rendered to `memory/guides/UNATTENDED-STOPS.md`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **An offer that writes the target as holder.** That is an assignment, which P40 forbids: the target
  may be offline, and the unit would wait on it for a whole lease expiry instead of an offer window.
- **An absolute deadline in the record.** A reader would compare it with its own clock, the defect
  clause 0135 closes.
- **A separate offer ref beside the lease.** Two refs for one unit's claim order would race each
  other; the offer has to ride the tip the acquisition compares and swaps.

## 5. Production-readiness checklist

- security — a new write onto `refs/gov/leases/*`, through the one writer `write_gov_ref`; the target
  tag is validated against the fleet registry at the write, the window is an integer, and no free text
  enters the record. An offer holds a lease from other nodes for at most one window per sighting.
- perf / scale — one lease read and one push per offer; the class test adds one feed lookup per read
  of an offered lease.
- error / empty / loading states — an unsighted tip holds the offer from this node's first sighting;
  a malformed window reads as expired; an unreachable remote is TOOL-dPlacedRequest-1's
  `leases.offline` rule.
- observability — the refusal line names `offered` and the target tag; `--claims` rows keep their
  shape.
- risks — a node offered work it never claims holds that unit for one window; the default is 300
  seconds.
- testing — the fixture cases under AC1 to AC6 and the suite arm in §7.
- migration — none: a record whose `offer` reads `-`, or carries no such key, carries no offer.
- user docs — the stops guide's section 7 and the verbs guide; no page under `help/` describes leases.

## 6. Acceptance criteria

The fixture for every criterion below is a bare remote and two clones under `%TEMP%` with short
names, clone A tagged `a` and clone B tagged `b` in a fixture `fleet.toml`, and `RUN_CLAIMS` on. The
unattended kit's own suites are waived for this build's landing (README rule 8), so each probe below
is the observation.

- **AC1** — When clone A runs `unattended.sh --lease offer unit fx u1 --to b` on an absent lease, the
  bare remote's `refs/gov/leases/fx/unit/u1` carries `status: released`, `offer: b`, an integer
  `offer-deadline` and `epoch: 1`; the same act against a lease clone B holds `live` prints
  `lease refused — live-holder` and leaves the tip unmoved.
  Red when: the offer is written over a live lease, or the record lacks either offer key.
- **AC2** — When `unattended.sh --lease offer unit fx u1 --to zz` runs with `zz` absent from the
  fixture registry, it refuses before any remote read and the remote holds no such ref.
  Red when: an unregistered tag is written.
- **AC3** — When clone A runs `unattended.sh --lease acquire unit fx u1` on the lease offered to `b`
  within its window, it prints `lease refused — offered`, the remote tip is unmoved, and `CLAIM_READS`
  names `offered`.
  Red when: a node the offer does not name takes it before the window passes.
- **AC4** — When clone B runs `unattended.sh --lease acquire unit fx u1` within the window, the
  acquisition lands at `epoch: 2` and the new record carries `offer: -` and `offer-deadline: -`.
  Red when: the named node is refused, or its record keeps the offer.
- **AC5** — When clone A's `gov-feed.log` records the offer tip's first sighting `offer-deadline` plus
  one seconds ago and clone A acquires, the acquisition lands; with no sighting of the tip, it refuses
  `offered`.
  Red when: an expired offer still holds its unit for the node it named, or an unsighted offer is
  read as expired.
  fixture: the sighting is planted as one line of the feed TOOL-dPlacedRequest-13 writes.
- **AC6** — When clone A reads lease `u1` at epoch `n`, clone B then takes it over to epoch `n+1`,
  and clone A's take is replayed from its own read, A prints `lease refused — epoch-fence`, the remote
  record names `b` at epoch `n+1`, and `git log --format=%B refs/gov/leases/fx/unit/u1` on the bare
  remote shows each `epoch:` value once, never falling.
  Red when: A's take lands, or two records on the ref carry one epoch; the planted case is an
  acquisition carrying an old epoch.
- **AC7** — When `python policy.py get leases.offer-seconds` runs in the built tree it prints `300`,
  and `--lease offer` writes `offer-deadline: 300`.
  Red when: the window is typed in the driver rather than read through `read_lease_bound offer`.
- **AC8** — When `grep -n "offered" tools/unattended/STOPS.template.md` and
  `grep -n "lease offer" tools/unattended/VERBS.template.md` run, each finds its row.
  Red when: either guide omits the class or the act.

## 7. Gates

`unattended kit gate` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC3 AC4 AC5 AC6 · the offered class and its per-cell row, an expired and an unsighted offer and a replayed stale take, staged against the base driver, which has no offer act · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — What does `offer-deadline` hold?** (a) A window in seconds, opened by each node's first
  sighting of the offer's tip on the observer clock; (b) an absolute UTC deadline stamped by the
  offering node. (b) is a stamp one node writes and another judges with its own clock, which clause
  0135 forbids by name for this very deadline. Rung 1, clause 0135's "an offer for
  `leases.offer-seconds`" judged by an observer. RESOLVED (agent, 2026-10-25, delegated): (a).
  widens: none · relaxes: none
- **F2 — Does an acquisition carry an explicit expected epoch?** (a) No: the epoch moves only with the
  tip, so the compare-and-swap on the tip read is the fence, and the new epoch is derived from that
  same read; (b) an `--epoch <n>` argument compared before the push. (b) adds a second channel saying
  what the tip already says, and a caller could pass an epoch that disagrees with its tip. Rung 3, the
  most capable option with the fewest open questions: (a) meets AC6 and adds no surface. RESOLVED
  (agent, 2026-10-25, delegated): (a). widens: none · relaxes: none
- **F3 — Who may write an offer?** (a) Any caller of `--lease offer`, its target validated against the
  fleet registry, legal only on an absent or `released` lease; (b) only the lease's last holder, as a
  hand-over. (b) leaves a never-held unit with no way to be offered, which is the head's main case
  (v2:1898-1910). Rung 1, P40: anything above a unit may offer. RESOLVED (agent, 2026-10-25,
  delegated): (a). widens: none · relaxes: none
- **F4 — Does an unsighted offer hold?** `check_deadline_passed` returns 2 when the feed has never seen
  the tip. (a) It holds, the window opening at this node's sighting; (b) it reads as expired. (b) lets
  a node that has just fetched the offer for the first time claim over the node it names, which is the
  clause's red case. Rung 1. RESOLVED (agent, 2026-10-25, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: §7's leg line gains `recall floor` and
  `recall floor arms`, the legs `memory/guides/UNATTENDED-STOPS.md` in Files touched trips.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-28,
  hands-off TOOL-dPlacedRequest-34, each the mirror of that promoted unit's own edge.

## 10. Reuse audit

The seams extended are TOOL-dPlacedRequest-1's `--lease` verb and its `lease` mode, over the
claim-read class set and table in `check_claim_writable` (`tools/unattended/unattended.sh:2219-2220`,
`:2243`), which gain one class and one cell per mode; the one compare-and-swap writer `write_gov_ref`
and `build_gov_commit` that TOOL-dPlacedRequest-11 extracts from `write_claim` (`:2396`, the
lost-race parse at `:2434`); and TOOL-dPlacedRequest-17's `check_deadline_passed` and
`read_lease_bound`, rather than the age pass `read_claims` runs today (`:2173-2186`), which reads the
reader's clock against the holder's stamp. The probe `python tools/codebase-map/reuse_lookup.py "offer
a unit to one node with a deadline before any node may claim it"` ranked `write_claim`,
`check_claim_writable` and `check_claim_push_lock_stale` among name-stem hits and nothing that offers
or waits on a deadline. Scout A's row gave the table as `:2284-2301` and the stale-info parse as
`:2434`; both agreed with source at `c63aabbb`.

Recall terms used: `python tools/memory-recall/query.py "how does a head offer a unit to a node
without assigning it" --terms "offer lease deadline offer-seconds claim reorder expired free epoch
stale acquisition head"`
