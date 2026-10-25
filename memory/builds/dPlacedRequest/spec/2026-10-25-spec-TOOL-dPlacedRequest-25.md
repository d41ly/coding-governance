# TOOL-dPlacedRequest-25 — a write that opens a holder's tenure renews the lease

**Status:** OPEN · rev-1 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 4 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-25-deviation-251.md](../build/2026-10-25-build-TOOL-dPlacedRequest-25-deviation-251.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 20 at HIGH**. It shares item **H1**, "a new holder inherits the previous holder's
renewing beat", with finding 1, which `TOOL-dPlacedRequest-26` closes. Under the default
`leases.renewal: progress`, `TOOL-dPlacedRequest-1` S8 writes `renews: no` on every write without a
witness, an acquire, a take-over and a draw included, so a fresh tenure opens on a commit that does
not renew, and a no-witness create has no renewing beat at all. This unit repairs
`TOOL-dPlacedRequest-1`'s writer: the write that opens a tenure, the one whose epoch differs from the
epoch it read or a create, renews the lease under every `leases.renewal` value but `none`, so the
record itself says when the new holder's clock started. Finding 1, the reader's half, is the other
unit of H1.

## 2. Scope (IN)

- **S1** — One derivation of `renews`, `derive_lease_renews <epoch read> <epoch written> <policy>
  <witness verdict>`, in `tools/unattended/unattended.sh`, prints `yes`, `no` or `-`. `<epoch read>` is
  empty on a create; `<witness verdict>` is `new` when the write carries a witness that passes
  `TOOL-dPlacedRequest-1` S8's test and differs from the record's, else `none`. Every lease write
  `TOOL-dPlacedRequest-1` builds sets `renews` from it and from nothing else. Observed by AC3.
- **S2** — The tenure rule. Under `none` it prints `-`. Under `progress`, `activity` and `fixed`, a
  create or a write whose epoch differs from the epoch read prints `yes`, witness or not. Otherwise
  `progress` prints `yes` for a `new` witness and `no` for none, `activity` prints `yes`, and `fixed`
  prints `no`. The rule is keyed on the epoch change and not on the act's name, so every act that
  opens a tenure takes it: the create, the take, the announced take, `take-over`, the first lease
  write over a legacy claim, and `TOOL-dPlacedRequest-16`'s take of a `released` lease and its draw.
  Observed by AC1, AC2 and AC3.
- **S3** — The stops guide's section 7 (`tools/unattended/STOPS.template.md`, rendered to
  `memory/guides/UNATTENDED-STOPS.md`) states, beside `leases.renewal`'s row, that a write opening a
  tenure renews under every value but `none`. Observed by AC4.

## 3. Non-goals (OUT)

- No change to how a lease is aged: the walk that stops at the tenure's start, and the verdict of a
  tenure with no renewing commit, are `TOOL-dPlacedRequest-26`'s.
- No change to what a witness is: `TOOL-dPlacedRequest-1` S8's trailer test stands.
- No new record key: `renews` and `epoch` are `TOOL-dPlacedRequest-1`'s I6 keys.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-1` — the lease writer, the `renews`, `witness` and `epoch` keys and `read_lease_policy`'s `leases.renewal`, whose per-write value this unit derives; without them there is no write to set `renews` on
- **hands-off** `TOOL-dPlacedRequest-16` — `derive_lease_renews`, through which the take of a `released` lease and the draw set `renews`, so each opens its tenure renewed

## 4. Design

### The table

| `leases.renewal` | create, or epoch changed | same epoch, new witness | same epoch, no new witness |
|---|---|---|---|
| `progress` | `yes` | `yes` | `no` |
| `activity` | `yes` | `yes` | `yes` |
| `fixed` | `yes` | `no` | `no` |
| `none` | `-` | `-` | `-` |

`fixed` reads as `TOOL-dPlacedRequest-1` §8 F6 resolved it, "renews only at acquisition"; this table
says what acquisition means to a writer: the write that opens a tenure. The `witness` key is written
as today, the witness given or `-`; only `renews` moves.

### Why the epoch, not the act

`TOOL-dPlacedRequest-1` S3 raises the epoch at a take and an announced take, `TOOL-dPlacedRequest-16`
S1 and S4 at the take of a `released` lease and at a draw, and a create writes 1. Each of those is a
holder starting a tenure. A rule spelled per act would have to be repeated by each unit that adds one;
a rule keyed on the epoch the writer already computes is inherited by construction.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_lease_renews` | shell function | `derive`, OK |

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `derive_lease_renews`, called by the lease writer
- `tools/unattended/unattended.test.sh`: the renewal arms
- `tools/unattended/STOPS.template.md`: section 7's renewal row
- `memory/guides/UNATTENDED-STOPS.md`: its render

### Alternatives rejected

- **Treat the tenure start as renewing on the reader's side only.** The record would still say
  `renews: no` for a commit that started a clock, so a reader of the ref sees one fact and the verdict
  another; `TOOL-dPlacedRequest-26` keeps a reader rule only for a tenure no writer marked.
- **A per-act list.** Every later act that opens a tenure would need its own line here.

## 5. Production-readiness checklist

- security — none: the same key, a derived value.
- perf / scale — one shell function call per lease write, no process.
- error / empty / loading states — an unreadable policy key reads its default, as
  `TOOL-dPlacedRequest-1` S12 states.
- observability — `renews: yes` on the commit that opened a tenure, readable with `git log`.
- risks — under `fixed`, a holder that re-takes its own lease at a higher epoch renews it; that is the
  same act as a new acquisition.
- testing — the probes of §6 and the arm in §7.
- migration — none: no lease exists before this build lands.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the kit.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-1` AC1's scratch clone and bare origin, `RUN_CLAIMS=on`.

- **AC1** — When session `s2` runs `--lease take-over build tFix` without `--witness` over a planted
  stale lease at epoch 1 under the default `progress`, the new record reads `epoch: 2` and
  `renews: yes`; a following `--lease renew build tFix` without `--witness` reads `renews: no`.
  Red when: a take-over opens its tenure on `renews: no`.
- **AC2** — When `--lease acquire build tNew` creates a lease without `--witness`, the record reads
  `epoch: 1` and `renews: yes`; with `leases.renewal` planted `none` it reads `renews: -`, and planted
  `fixed` a later renew reads `renews: no`.
  Red when: a create carries no renewing beat, or `none` renews.
- **AC3** — When a probe sources `unattended.sh` and calls `derive_lease_renews` over the twelve
  cells of §4's table, it prints each cell's value.
  Red when: a cell differs, the planted case being a scratch copy keyed on the act name that misses
  the announced take.
- **AC4** — When `grep -n 'tenure' tools/unattended/STOPS.template.md` runs, a section 7 line names
  `leases.renewal` and says a write opening a tenure renews.
  Red when: the guide omits the rule.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · the renewal arms over a planted stale lease and each planted policy value, staged by a scratch copy whose rule is keyed on the act name · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Which write opens a tenure?** (a) A create or any write whose epoch differs from the epoch
  read; (b) the acts named acquire, take-over and draw; (c) any write by a holder other than the
  tip's. (b) misses the announced take and the `released` take; (c) needs the previous holder's
  identity at every write, which the epoch already encodes. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 20 (HIGH, item H1,
  shared with finding 1).

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-1` S8's `renews` decision inside its lease writer, and its
S3 epoch rule, which already computes the read and written epochs this unit keys on; no code exists
at the pinned base, since the lease writer is that unit's. `python
tools/codebase-map/reuse_lookup.py "a lease write that opens a holder's tenure renews it"` ranked
`write`, `write_text`, `opened`, `holder` and `resolveLease`, name stems only; none decides a renewal,
so no existing seam fits beyond the unit this repairs. `python tools/memory-recall/query.py "when does
a lease write renew under the progress policy"` returned the spec brief's unit 1 row, unit 1's §2 and
scout A's row 1; none disagrees with the spec.

Recall terms used: renews witness progress acquisition take-over tenure epoch leases.renewal fixed activity
