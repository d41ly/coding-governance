# TOOL-dPlacedRequest-41 — a second offline write to a queued lease chains on the queued commit

**Status:** DEFERRED · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 5 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-build-TOOL-dPlacedRequest-41-deviation-411.md](../build/2026-10-25-build-TOOL-dPlacedRequest-41-deviation-411.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
confirmed **finding 33 at HIGH**, its item **H4**, which holds no other finding. `TOOL-dPlacedRequest-24`
S3 drops any offline write whose ref and cached tip match a queued line, printing `queued — already`.
Offline, `TOOL-dPlacedRequest-1` S10 builds every write on the cached tip and moves no ref, so an
acquire followed by a release, a renew with a new witness or a take-over of the same ref share one key:
the release is silently discarded while the user is told it was queued, the flush lands the acquire,
and the remote shows a lease the node believes it released, held until expiry or for ever under
`leases.renewal none`. The finder's fix was judged unsound; this unit builds the skeptic's corrected
fix. It repairs `TOOL-dPlacedRequest-24` at order 5.

## 2. Scope (IN)

- **S1** — The chain. An offline lease write to a ref that already has a line in `gov-queue.log` is
  built on the newest queued commit for that ref, not on the cached tip: the act reads that commit's
  record as an online write reads the remote tip's, the new commit's parent is that commit, and the
  appended line records that commit as its expected tip. Observed by AC1 and AC2.
- **S2** — The narrowed dedupe. A write built on a queued commit whose record, less the stamp keys
  `beat-utc`, `last-fetch` and `renews`, equals that commit's record appends nothing and prints
  `queued — already · <tail>`; every other write is appended. This replaces `TOOL-dPlacedRequest-24`
  S3's ref-and-cached-tip key. Observed by AC1 and AC3.
- **S3** — The flush keeps a chain whole. `write_gov_queue` pushes a ref's lines oldest first; a line
  whose earlier line on the same ref was kept (rc 2) is kept unpushed, and a line whose earlier line
  on the same ref yielded yields with it, printing `yield` and its `lease-yielded` event, since its
  expected tip never reached the remote. Observed by AC2 and AC4.

## 3. Non-goals (OUT)

- No change to the lock, the resolved-lines rewrite or the landed-on-loss read:
  `TOOL-dPlacedRequest-24` S1, S4 and S5.
- No change to which acts may run offline or to `leases.offline`'s values: `TOOL-dPlacedRequest-1`
  S10 and `TOOL-dPlacedRequest-23`.
- No encoding of an empty cached tip: findings 7 and 25, items of `TOOL-dPlacedRequest-43`.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-24` — `add_gov_queue`, `write_gov_queue` and S3's dedupe, which this unit narrows and chains; without the guarded queue there is no line to chain on
- **consumes-from** `TOOL-dPlacedRequest-1` — S10's offline branch and S6's `acquire` that renews on `mine`, which build the write this unit rebases; without them there is no offline write
- **hands-off** `TOOL-dPlacedRequest-49` — the offline write's read of the newest queued commit, which that unit's items for findings 36 and 38 route through `derive_queue_tip` and refuse when unreadable

## 4. Design

### The offline write

```
offline branch of a lease write (leases.offline warn)
  lock gov-queue.lock
  q = newest queued line for ref
  base = q ? q.commit : cached tip                          (S1)
  build the act on base's record, parent base
  q and record(new) less stamps == record(q.commit) less stamps
        -> unlock; "queued — already · <tail>"              (S2)
  append ref TAB (q ? q.commit : cached tip) TAB new TAB queued-utc
  unlock; "queued"
```

A re-run offline acquire builds on its own queued acquire, which `TOOL-dPlacedRequest-1` S6 reads as
`mine` and renews; the renew differs only in its stamps, so it is `queued — already`, and
`TOOL-dPlacedRequest-24` AC1 still holds. A release after the acquire changes `status`, so it chains.

### The flush, per ref

```
lines oldest first; for each line of ref r:
  an earlier line of r kept     -> keep, push nothing
  an earlier line of r yielded  -> yield, health event, resolved
  else                          -> write_gov_ref r tip commit, as TOOL-dPlacedRequest-24 S4 and S5
```

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the offline branch's base, `add_gov_queue`'s dedupe and
  `write_gov_queue`'s per-ref rule
- `tools/unattended/unattended.test.sh`: the chain arms
- `tools/unattended/STOPS.template.md`: section 7's offline queue sentence names the chain
- `memory/guides/UNATTENDED-STOPS.md`: its render

### Alternatives rejected

- **Dedupe on the act name.** A renew with a new `witness` would be dropped though it changes what the
  remote must hold.
- **Replace the queued line with the newer write.** The flush would land a release whose parent is a
  commit the remote never held, and lose the acquire's history.
- **Keep the ref-and-cached-tip key (the finder's fix narrowed by act).** Judged unsound by the
  skeptic: any two distinct acts still share the key.

## 5. Production-readiness checklist

- security — closes a silent drop that left a remote lease held against its holder's intent.
- perf / scale — one `git cat-file` of the newest queued commit per offline write to a queued ref.
- error / empty / loading states — a chain whose head is lost yields whole, each line named.
- observability — `queued`, `queued — already` and each line's `yield` say what the queue did.
- risks — a long offline session chains many lines on one ref; each is one compare-and-swap at flush.
- testing — the probes of §6 and the arm in §7.
- migration — none: the queue is new in this build.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the kit.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-1` AC7's scratch clone and bare origin, `RUN_CLAIMS=on`, the
origin renamed away to make it unreachable.

- **AC1** — When `--lease acquire build tOff` then `--lease release build tOff --as withdrawn` run
  offline, `gov-queue.log` holds two lines, the second's expected-tip field equals the first's commit,
  and `git rev-parse <second commit>^` prints the first commit.
  Red when: the release prints `queued — already` and is dropped, the staged case being
  `TOOL-dPlacedRequest-24` S3's ref-and-cached-tip key.
- **AC2** — When the origin is restored after AC1 and `--lease flush` runs, it exits 0, the remote
  `refs/gov/leases/tOff/build` reads `status: withdrawn` with the acquire commit as its parent, and the
  queue is empty.
  Red when: the remote shows the lease held after the flush.
- **AC3** — When `--lease acquire build tOff` runs offline twice, the second prints `queued — already`
  and `grep -c '' gov-queue.log` prints 1.
  Red when: the narrowed dedupe re-queues an identical act.
- **AC4** — When the remote ref is planted at a foreign commit before AC2's flush, both lines print
  `yield`, the health log gains two `lease-yielded` lines, the remote keeps the foreign commit, and
  the queue is empty.
  Red when: the second line is pushed on a tip the remote never held.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · each pair of distinct offline acts on one ref, flushed, asserting the remote ends in the last act's state, staged against the ref-and-cached-tip key · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How does a second offline write to a queued ref enter the queue?** (a) Built on the newest
  queued commit and chained, deduped only when its record less stamps equals that commit's; (b)
  appended on the cached tip beside the first; (c) the finder's fix. (b) makes the flush's second
  compare-and-swap lose to the first; (c) was judged unsound by the skeptic. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the skeptic's corrected fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  33 (HIGH, item H4).
- rev-2 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-24`'s `add_gov_queue` and `write_gov_queue` and
`TOOL-dPlacedRequest-1` S10's offline branch; nothing queues a write at the pinned base
(`grep -n add_gov_queue tools/unattended/unattended.sh` prints nothing). `python
tools/codebase-map/reuse_lookup.py "queue two offline writes to one ref as a chain"` ranked `queue`
(the turnstile's test helper), `build_self_chain` and `writeSidecarLine`, name stems only, none a ref
queue. `python tools/memory-recall/query.py "how do two offline writes to one lease ref queue"`
returned `TOOL-dPlacedRequest-24`, this audit's H4 and scout A's row on the queue; none disagrees with
source.

Recall terms used: offline queue gov-queue.log chain queued commit cached tip dedupe flush yield release acquire
