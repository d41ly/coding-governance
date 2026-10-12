# TOOL-aPairedSlots-4 — a doc-only bar takes its own key and never queues

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-2 · base b6cd02bc · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPairedSlots-4-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPairedSlots-4-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 |
| [2026-10-11-prompt-TOOL-aPairedSlots-1.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1.md) | research | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 |
| [2026-10-12-review-TOOL-aPairedSlots-1-9-diff-review-round1.md](../reviews/2026-10-12-review-TOOL-aPairedSlots-1-9-diff-review-round1.md) | diff-review | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 |

<!-- /gen:spec-records -->

## 1. Goal

A doc-only bar, one run with `GATE_DOCS_BASE` resolved, is admitted at once on a turnstile key of
its own instead of waiting behind whatever non-doc bar holds the host. It still writes a beacon, so
it is visible, its legs' runners nest under it, and its holder is reaped when it dies. The owner
chose no cap on how many run at once (2026-10-11).

## 2. Scope (IN)

- **S1 — who is doc-only.** A run whose `DOCS_BASE` is non-empty after its resolution above the
  turnstile, and which is not nested. `GATE_FULL` already empties `DOCS_BASE`, so a full bar is
  never doc-only. Observed by AC1, AC4.
- **S2 — the docs key.** Such a run takes no ticket and claims no slot. It creates
  `$TS_HOST/gate-docs-beacon/<run id>` with the six beacon files a slot holder writes, exports
  `GATE_TURNSTILE_HOLDER` as its nonce, starts the ticker on it, and arms the same release traps,
  each nonce-guarded on that directory alone. Observed by AC1, AC2.
- **S3 — its lines.** It prints `gate queue: docs-only — admitted on the docs key, not queued`,
  then `gate queue: waited 0s` and `gate queue: acquired <utc> from docs`, and records `queued` 0
  and `queued_from` `docs`. Observed by AC1.
- **S4 — nesting sees it.** The nested test, which reads every slot (TOOL-aPairedSlots-2), also
  reads each docs beacon's nonce, so a runner started by a doc-only bar's leg nests under it.
  Observed by AC3.
- **S5 — a dead docs beacon is swept.** A doc-only run, before creating its own, clears each docs
  beacon whose `pid` is dead or whose heartbeat is older than its `ttl`, guarded by the nonce it
  judged, printing one line per beacon swept. Nothing waits on a docs beacon, so a leftover delays
  no bar; the sweep only keeps the directory from growing. Observed by AC5.
- **S6 — non-doc bars do not see it.** A non-doc waiter's queue line, its reap and its held count
  read slots only, so a doc-only bar never delays, narrows or is named by a non-doc bar.
  Observed by AC4.
- **S7 — the text.** The turnstile block's header comment and the README's turnstile section
  state the key, its lines and `docs` among the `queued_from` values. NOT OBSERVED — prose.

## 3. Non-goals (OUT)

- A cap on doc-only bars; the owner chose none.
- Deciding which pushes are doc-only. That is `.githooks/pre-push`'s, which sets
  `GATE_DOCS_BASE`, and the push boundary is aFrugalTurnstile's.
- `--hold`, which is never a doc-only run.

### Edges

- **consumes-from** `TOOL-aPairedSlots-2` — the nested test this unit extends to the docs key.
- **consumes-from** external — `GATE_DOCS_BASE` as `.githooks/pre-push` sets it, and the docs
  mode's resolution in `tools/run-gates/run-gates.sh`, both unchanged.

## 4. Design

A doc-only bar runs the legs that declare doc reads and whose reads moved, plus any leg that
declares none, so it is usually short, and the owner's complaint was a doc landing waiting half an
hour behind a full bar. Its own key keeps every property the turnstile gives a bar except the wait:
the beacon names it, its nonce is what its legs nest under, and its ticker and traps release it.

The key is a directory of beacons rather than one beacon because nothing caps it; one directory per
run id keeps two doc-only bars from ever contending for a path. The run id is the one the run record
already uses, so a beacon and its record name each other.

### Messages

| Event | Line |
|---|---|
| admitted | `gate queue: docs-only — admitted on the docs key, not queued` |
| swept | `run-gates: sweeping the docs beacon of a dead holder (pid <pid>)` or `… of a stalled holder (heartbeat <s>s old, ttl <s>s)` |

### Inventory

New shell variable: `TS_DOCS` (1 for a doc-only run). New paths: `gate-docs-beacon/` and its
`<run id>` children. New `queued_from` value: `docs`. Minted function, in the `sh.function` cell:
`scan_dead_docs_beacons`.

### Rollout

A runner older than this unit queues a doc-only bar as it does today. The two interoperate: a
doc-only bar on this runner and a non-doc bar on an older one run side by side, which is the
owner's intent for doc-only bars.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/run-gates/README.md`

### Alternatives rejected

- **No beacon at all.** A doc-only bar's leg that starts a runner would then queue behind the
  host's holder rather than nest, and nothing could name the bar while it runs.
- **One docs slot.** The owner chose unbounded; two doc landings would still serialize.

## 5. Production-readiness checklist

- security — N/A — the same host directory and the same nonce rule as the slots; nesting still
  decides contention and never a verdict.
- perf / scale — the point: a doc-only bar's queue wait becomes 0. Unbounded doc-only bars beside
  two non-doc bars can load the host more than two bars do; the owner chose that.
- error / empty / loading states — a docs beacon that cannot be created runs the bar UNQUEUED with
  a NOTE, as an unticketed run does today.
- observability — the admitted line and `queued_from` `docs`.
- risks — the docs mode is the hook's declaration; a bar wrongly classified doc-only skips the
  queue. The classification is unchanged by this unit.
- testing — AC1 to AC5 in the turnstile suite's fixtures, a fixture doc class declared by the arm.
- migration — none; the directory is created on first use.
- user docs — the README's turnstile section.

## 6. Acceptance criteria

The fixtures are the turnstile suite's scratch repositories with a declared doc class and one leg
declaring `doc_reads`, and a second commit touching only a doc path, so `GATE_DOCS_BASE=HEAD~1`
resolves.

- **AC1** — When a non-doc bar holds the only slot and a doc-only bar starts, the doc-only bar
  prints `gate queue: docs-only — admitted on the docs key, not queued` and finishes while the
  holder still runs; its header records `queued_from` `docs`.
  Red when: the doc-only bar takes a ticket, and prints `queued at position`.
- **AC2** — When the doc-only bar exits, its directory under `gate-docs-beacon` is gone, and a
  second doc-only bar's directory, live beside it, is not.
  Red when: the release removes the key directory rather than its own run id.
- **AC3** — When a leg of a doc-only bar starts a runner with `GATE_TURNSTILE_HOLDER` inherited,
  that runner prints `gate queue: nested under`.
  Red when: the nested test reads slots only.
- **AC4** — When a doc-only bar holds its key and a non-doc bar starts with the slot free, the
  non-doc bar prints `gate queue: waited 0s` and no `at dispatch` line; and a full bar
  with `GATE_DOCS_BASE` set queues as a non-doc bar.
  Red when: the docs key is counted as a held slot, or a full bar takes it.
- **AC5** — When a docs beacon names a dead pid, the next doc-only bar prints
  `sweeping the docs beacon of a dead holder` and the directory is gone.
  Red when: the sweep is absent and the dead beacon stays.

## 7. Gates

`run-gates turnstile` · `run-gates canary`

New arm: tools/run-gates/run-gates.turnstile.test.sh · covers AC1 AC2 AC3 AC4 AC5 · a runner copy with the docs branch removed, so a doc-only bar queues · none

## 8. Open questions

- **F1 — How many doc-only bars may hold the docs key at once?** Options put to the owner: own key
  unbounded, own key one slot, own key at the `slots` value. RESOLVED (owner, 2026-10-11): own key,
  unbounded.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

The seam is TOOL-aFrugalTurnstile-5's beacon in `tools/run-gates/run-gates.sh`: its six files,
`ts_tick_start`, `ts_release` and its traps, reused for one more holder kind, and the docs mode
resolution (`DOCS_BASE`), read and not changed. `reuse_lookup.py` named no doc-only admission
seam. Recall returned TOOL-aReapedTicket-2's dead-waiter sweep, whose two-signal rule S5 follows.

Recall terms used: `python tools/memory-recall/query.py "why does the gate turnstile serialize bars and admit only one at a time" --terms "turnstile beacon queue ticket serialize concurrent bars width contended CPU host-wide nonce heartbeat reap slots"`
