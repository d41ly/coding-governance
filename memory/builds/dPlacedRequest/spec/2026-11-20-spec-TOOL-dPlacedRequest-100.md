# TOOL-dPlacedRequest-100 — the entry claim takes over a stale build lease instead of waiting on it

**Status:** CLOSED · rev-1 · 2026-11-21 · node d · Tier-2 · base 2b4cc0bd · streams tooling · order 38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-21-build-TOOL-dPlacedRequest-1-runlog-d54afa03.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-runlog-d54afa03.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-96 TOOL-dPlacedRequest-97 TOOL-dPlacedRequest-98 TOOL-dPlacedRequest-99 |
| [2026-11-21-build-TOOL-dPlacedRequest-100-1-acceptance-ledger.md](../build/2026-11-21-build-TOOL-dPlacedRequest-100-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-100-deviation-735.md](../build/2026-11-21-build-TOOL-dPlacedRequest-100-deviation-735.md) | deviation | — |
| [2026-11-21-build-TOOL-dPlacedRequest-100-red-fix-36.md](../build/2026-11-21-build-TOOL-dPlacedRequest-100-red-fix-36.md) | red-fix | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-100-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-100-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-100-owner-chain-stop.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-100-owner-chain-stop.md) | research | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-100-pin-fact-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-100-pin-fact-brief.md) | research | — |
| [2026-11-21-prompt-TOOL-dPlacedRequest-100-owner-merge-ruling.md](../prompts/2026-11-21-prompt-TOOL-dPlacedRequest-100-owner-merge-ruling.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 95 to 99
(`memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md`)
confirmed item **H4** at HIGH, finding id 29, and its disposal promoted it to this unit. A `patch` or
`repeat` entry claim takes its build lease through `--lease acquire build <slug>`. Over a lease whose
foreign holder is stale, acquire refuses `live-holder` with the take-over hint, and
`tools/unattended/unattended.sh#run_entry_claim` routes the first word, `live-holder`, to the wait
route of `tools/loop/claim.py#derive_claim_route`. So the claim waits on a dead holder, exits 4 until
`flow.wait-ceiling` passes, then raises an owner item. This unit routes that refusal to the
`--lease take-over` act the hint names, so the claim proceeds on a stale lease, and gates it.

## 2. Scope (IN)

- **S1** — H4, finding id 29, the record's scope-in fix. In `run_entry_claim`, an acquire refusal
  whose line carries the stale hint runs `run_lease_verb take-over build <slug>` once. A take-over
  that writes is the claim's lease, and the claim goes on to its scaffold as after an acquire. A
  take-over refused is routed by its own cause through `claim.py route`, as an acquire refusal is
  today. A take-over not written exits 2. The hint's text is spelled once, as the constant
  `LEASE_STALE_HINT`, written by `run_lease_verb`'s refusal line and read by the new branch. Observed
  by AC1 and AC2.
- **S2** — The left-shift the record names, an AC or arm per consumer a Goal names as repaired: the
  loop kit's claim fixture gains the plant `stale-holder`, the `--entry-claim` run the record asks
  for. Observed by AC1.
- **S3** — The user pages that state the entry claim's routes name the new one: `help/loop.md`, and
  the verb guide in `tools/unattended/VERBS.template.md` with its dogfooded copy
  `memory/guides/UNATTENDED-VERBS.md`. Observed by AC3.

## 3. Non-goals (OUT)

- No new refusal cause and no change to `claim.py`'s cause sets, shared interface I9: acquire still
  refuses `live-holder`, as `tools/unattended/STOPS.template.md` section 7's table states.
- No change to how a lease becomes stale, which stays `TOOL-dPlacedRequest-17`'s observer clock.
- No change to what the `--lease` verbs decide or print: their refusal line reads the constant and
  prints the same bytes, and `TOOL-dPlacedRequest-96` restores the stale row they read.
- No new exit code of `--entry-claim`: every new path leaves by a code its header already lists.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-96` — the restored `lease:foreign-stale` row, which sets the
  take-over hint on an acquire refusal and lets `take-over` write; without it the hint never prints and
  the take-over this unit runs is refused
- **consumes-from** `TOOL-dPlacedRequest-99` — S5's `plants=<n>` token on the `loop claim fixtures`
  budget row, which this unit raises by its one plant, and S8's arm over `run_entry_claim`'s returns,
  which the new branch satisfies by literal codes

## 4. Design

### The branch

```
acquire build <slug>  (as at the base)
  rc 0                                 -> as at the base
  rc 1, line ends with LEASE_STALE_HINT
       take-over build <slug>, its output printed
         rc 0 -> "entry-claim — <slug> · the stale build lease taken over"; on to the scaffold
         rc 1 -> its own `lease refused — <cause>` line routed by claim.py route, as below
         rc 2 -> "claim not written — <slug> · the stale build lease was not taken over"; return 2
  rc 1 otherwise                       -> routed by claim.py route, as at the base
  rc 2                                 -> as at the base
```

The take-over runs at most once per entry claim. A take-over refused names the cause the lease now
reads, `live-holder` where the holder beat again since the acquire, and that cause takes the existing
route, so a holder that came back is waited on as before. Every return in the branch is a literal
code the header lists, `1`, `2` or `4`, so `TOOL-dPlacedRequest-99` S8's arm reads them.

`LEASE_STALE_HINT=' · stale, so --lease take-over takes it'` is set once beside `run_lease_verb`.
That verb's refusal line appends it where `CW_HINT` is set, and `run_entry_claim` tests the acquire
line's suffix against it. One spelling, so a reworded hint cannot silently disable the branch.

Cited at the base: the acquire and its refusal routing are `tools/unattended/unattended.sh#run_entry_claim`;
the hint is typed in the refusal line at `tools/unattended/unattended.sh@0e8038fd:4235`, inside
`tools/unattended/unattended.sh#run_lease_verb`; the wait route is `tools/loop/claim.py#derive_claim_route`
over `WAIT_CAUSES` at `tools/loop/claim.py@40976268:91`; the stale reading is
`tools/unattended/unattended.sh#read_first_seen`'s first sighting.

### The plant

`stale-holder` in `tools/loop/claim.py`'s `PLANTS`, beside `live-holder`, over the same fixture
`write_claim_fixture` builds. It writes the foreign build lease as `tools/loop/placement.py#write_foreign_lease`
does, then appends that lease commit's first sighting, 25 hours back, to the fixture clone's
`gov-feed.log` in the row shape `add_claim_sighting` in `tools/unattended/unattended.test.sh` writes,
past the catalogue's 24-hour `leases.expiry-hours`. A repeat's `--entry-claim` then exits 0 `claimed`,
prints `take-announced`, leaves the remote lease's `epoch:` one above the planted one, and adds no
`wait-since:` to the claim.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the branch in `run_entry_claim`, the constant, its use in
  `run_lease_verb`'s refusal line, and `run_entry_claim`'s header comment naming the route
- `tools/loop/claim.py`: the `stale-holder` plant, its `PLANTS` row and its case
- `tools/run-gates/selftest-budgets.txt`: the `loop claim fixtures` row, its `plants=` token raised by
  one and its proxy re-priced by the plant's direct-CLI reading, in the row's own PINNED-proxy shape
- `help/loop.md`: the entry claim's paragraph
- `tools/unattended/VERBS.template.md`: the `--entry-claim` entry
- `memory/guides/UNATTENDED-VERBS.md`: the same entry, the dogfooded copy
- the unattended kit's and the loop kit's version carriers, each moved once by the kit-epoch rule

### Alternatives rejected

- **A `stale` cause in `claim.py` routed to take-over.** It changes the acquire refusal's cause word,
  which the stops guide's table pins as `live-holder`, and the shared cause interface I9; the hint
  already carries the fact.
- **Scope the entry claim out and correct the Goal of `TOOL-dPlacedRequest-96`.** The record offers it.
  It leaves a dead holder costing every patch and repeat `flow.wait-ceiling`, 72 hours by default, and
  an owner item that the lease's own recovery act answers.
- **Take over without the hint, on any `live-holder` refusal.** It would take a live lease; the stale
  reading is the observer clock's, and only the hint carries it to this caller.

## 5. Production-readiness checklist

- security — the take-over is the existing announced act, written only where the observer's own clock
  reads the lease stale; the claim takes nothing a human running `--lease take-over` could not.
- perf / scale — one more lease write on the stale path only.
- error / empty / loading states — a take-over refused takes the acquire refusal's routes; one not
  written exits 2 with no folder written, as an acquire not written does.
- observability — the claim prints the take-over's own `take-announced` line and names the take.
- risks — two claimants racing a stale lease: the take-over's compare-and-swap lets one write, and the
  other's take-over is refused `live-holder` and waits, the existing route.
- testing — AC1's plant and the arm in §7.
- migration — none; no data moves.
- user docs — `help/loop.md` and the verb guide name the route, observed by AC3.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/claim.py --fixture --plant stale-holder` runs, it exits 0 with
  its `stale-holder` line ending `· held`, the plant having observed the repeat's `--entry-claim` exit
  0 printing `take-announced`, the remote lease's `epoch:` one above the planted one and no
  `wait-since:` on the claim.
  Red when: `run_entry_claim` routes the stale refusal by its cause word alone; staged by the tip's
  `claim.py` beside the driver of 2b4cc0bd4, the claim exits 4 printing `claim waiting`, its RED-first
  reading.
  fixture: the throwaway repository and bare remote the plant builds; the tree holds none.
  cost: one plant, under a minute on node d (UNVERIFIED, an estimate from the row's PINNED 120 s proxy over 13 plants).
- **AC2** — When `grep -c 'stale, so --lease take-over takes it' tools/unattended/unattended.sh` runs,
  it prints 1, and `grep -c 'LEASE_STALE_HINT' tools/unattended/unattended.sh` prints at least 3.
  Red when: the hint is typed in two places; at 2b4cc0bd4 the second grep prints 0, its RED-first
  reading.
- **AC3** — When `grep -c 'a stale build lease is taken over' help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md`
  runs, it prints 1 for each file.
  Red when: a page omits the route; at 2b4cc0bd4 each count is 0, its RED-first reading.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `scratch-guard self-test` · `tier2-review self-test` · `loop claim fixtures` · `every held leg is budgeted, every budget row resolves` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates`

New arm: tools/loop/claim.py · covers AC1 · the stale-holder plant, staged by the tip's claim.py beside the driver of 2b4cc0bd4, whose entry claim waits on the stale lease · the loop claim fixtures row's plants token raised by one

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft, promoted by the disposal of
  2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit, item H4 (HIGH, finding id 29), as the repair
  of `TOOL-dPlacedRequest-96`, whose Goal this unit's disposal corrected.
- rev-1 · 2026-11-20 · editorial, no criterion moved: AC1's cost line marks the budget row's figure
  it cites, per 2026-11-20-prompt-TOOL-dPlacedRequest-100-pin-fact-brief.

## 10. Reuse audit

The seam extended is `tools/unattended/unattended.sh#run_entry_claim`'s acquire branch, which already
reads the refusal line, and the act it reaches is the landed `--lease take-over`; the arm is a plant
of the loop kit's claim fixture beside `live-holder`, over `write_claim_fixture` and
`write_foreign_lease`, with the feed row shape the unattended suite's `add_claim_sighting` writes.
`python tools/codebase-map/reuse_lookup.py "entry claim routes a stale lease refusal to take-over"`
ranked `Refusal`, `refusal`, `claims` and `resolveLease` in `tools/unattended/run-lease.js`, name
stems only, then `check_claim_writable` and `write_claim`, the column and writer the take-over already
goes through; no other seam fits. The recall query below returned the audit's H4, the round-1 closing
record's H2, whose third consequence this is, and `TOOL-dPlacedRequest-21`'s scout on the claim's
refusal routes; none disagrees with the source read above.

Recall terms used: run_entry_claim entry-claim stale build lease take-over live-holder WAIT_CAUSES derive_claim_route CW_HINT claim waiting flow.wait-ceiling
