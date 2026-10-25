# TOOL-dPlacedRequest-42 — an offline lease create reads the feed first, as every create on an empty parent does

**Status:** DEFERRED · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 8 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-43 |
| [2026-10-25-build-TOOL-dPlacedRequest-42-deviation-421.md](../build/2026-10-25-build-TOOL-dPlacedRequest-42-deviation-421.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-43 |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
confirmed **finding 36 at HIGH**, its item **H5**, which holds no other finding.
`TOOL-dPlacedRequest-28` S2 has `read_feed_lease_tip` called only by a write "whose read finds the ref
absent on the remote". `TOOL-dPlacedRequest-1` S10's offline branch never reads the remote: it builds
on the cached tip, and when that is empty it queues a parentless epoch-1 create without consulting
the feed. After a tombstone is deleted outside the kit and a pruning fetch drops its cache ref, an
offline `--lease acquire` queues a create whose compare-and-swap on the absent ref lands at flush,
bringing the closed build back as held at epoch 1. `TOOL-dPlacedRequest-28` AC5 matches only the
literal `build_gov_commit ""`, so the class check misses it. This unit repairs `TOOL-dPlacedRequest-28`,
at order 7, so it sits at order 8.

## 2. Scope (IN)

- **S1** — The class, stated once: every lease commit built on an empty parent calls
  `read_feed_lease_tip <lease ref>` first, whether the remote answered absent or the offline branch
  found neither a queued line for the ref nor a cache ref `refs/gov/remote/<tail>`. The feed is
  node-local, so the offline branch reads it with no remote. Observed by AC1, AC2 and AC3.
- **S2** — The offline outcomes. `tombstone` refuses with `TOOL-dPlacedRequest-1`'s refusal line and
  cause `tombstone`, exit 1, nothing queued; `<commit> <epoch>` builds the create on `<commit>` at
  `<epoch>` plus one and queues it with an empty expected tip, so the flush creates the remote ref;
  nothing makes the plain epoch-1 create. Observed by AC1, AC2 and AC3.
- **S3** — The behavioural arm. The offline create over a sighted, deleted tombstone is observed by
  what it does, never by a spelling of the call; it stands beside `TOOL-dPlacedRequest-28` AC5 as the
  offline half of S4's class. Observed by AC1.

## 3. Non-goals (OUT)

- No change to the reader: `read_feed_lease_tip` is `TOOL-dPlacedRequest-28` S1's.
- No change to an offline write to a ref with a queued line: it builds on that line's commit
  (`TOOL-dPlacedRequest-41` S1), so it is no create.
- The online create paths' behavioural class check is findings 4's and 19's, items of
  `TOOL-dPlacedRequest-43`.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-28` — `read_feed_lease_tip` and S2's create rule, which this unit extends to the offline branch; without the reader there is no feed read to call
- **consumes-from** `TOOL-dPlacedRequest-1` — S10's offline branch and the cache ref it builds on, whose empty case this unit routes through the feed; without it there is no offline create
- **hands-off** `TOOL-dPlacedRequest-49` — the offline create's empty-tip queue line, which that unit's item for finding 36 writes through `derive_queue_tip`

## 4. Design

### The offline create

```
offline branch, warn (TOOL-dPlacedRequest-1 S10)
  queued line for ref?            yes -> build on it (TOOL-dPlacedRequest-41)
  cache ref refs/gov/remote/<tail>?  yes -> build on it, as today
  neither: read_feed_lease_tip <ref>
    ""                  -> create, no parent, epoch 1, queued with an empty tip
    tombstone           -> lease refused — tombstone · <tail> · <holder>   exit 1, nothing queued
    <commit> <epoch>    -> create, parent <commit>, epoch <epoch> + 1, queued with an empty tip
```

The online branch already reads the feed on an absent ref (`TOOL-dPlacedRequest-28` §4); this is the
same table on the one path that skipped it.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the offline branch's empty-tip case
- `tools/unattended/unattended.test.sh`: the offline-create arms
- `tools/unattended/STOPS.template.md`: section 7's epoch-for-life sentence names the offline create
- `memory/guides/UNATTENDED-STOPS.md`: its render

### Alternatives rejected

- **Refuse every offline create.** `TOOL-dPlacedRequest-1` S10 queues an offline acquire under `warn`,
  and a ref the feed never named has nothing to protect.
- **Keep AC5's spelling grep as the class check.** A create passed `"$tip"` escapes it, which is how
  this path was missed.

## 5. Production-readiness checklist

- security — closes a path that brought a closed build back as held.
- perf / scale — one `awk` over the feed per offline create with no cache ref, as the online create
  already pays.
- error / empty / loading states — a feed that never named the ref is a plain create, as today.
- observability — the refusal names `tombstone` and the ref.
- risks — none beyond `TOOL-dPlacedRequest-28` §5's.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the kit.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-16` AC5's: a scratch clone with a bare origin and `RUN_CLAIMS=on`.
A lease is written and sighted, deleted on the remote outside the kit, `--claims` then fetches with
`--prune` so the cache ref is gone, and the origin is renamed away.

- **AC1** — When the deleted lease was a build tombstone for `tFix` and `--lease acquire build tFix`
  runs offline, it exits 1 printing `tombstone`, and `gov-queue.log` is absent or unchanged.
  Red when: the offline branch queues a parentless epoch-1 create, the staged case being
  `TOOL-dPlacedRequest-1` S10's branch as written.
- **AC2** — When the deleted lease was `released` at epoch 4 and the same acquire runs offline, the
  queue gains one line whose commit reads `epoch: 5` and whose `git rev-parse <commit>^` is the feed's
  commit.
  Red when: the offline create restarts the epoch.
- **AC3** — When the ref was never named by the feed and the acquire runs offline, the queued commit
  reads `epoch: 1` and has no parent.
  Red when: an unnamed ref is refused offline.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · the offline create over a deleted tombstone, a deleted released lease and an unnamed ref, staged against the cached-tip-only offline branch · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Where does the offline create learn the epoch-for-life facts?** (a) The node-local feed
  through `read_feed_lease_tip`, as the online create; (b) refuse an offline create with no cache
  ref; (c) nothing, as written. (b) refuses what `TOOL-dPlacedRequest-1` S10 queues; (c) is the
  defect. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's fix judged sound.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  36 (HIGH, item H5).
- rev-2 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-28`'s `read_feed_lease_tip`, called unchanged from the one
create path that skipped it, inside `TOOL-dPlacedRequest-1` S10's offline branch; neither exists at
the pinned base. `python tools/codebase-map/reuse_lookup.py "lease create on an empty parent reads the
change feed for a tombstone"` ranked `read`, `read_text`, `changed` and `read_conf`, name stems only.
`python tools/memory-recall/query.py "how does an offline lease create learn of a tombstone"` returned
`TOOL-dPlacedRequest-16`, this audit's H5 and `TOOL-dPlacedRequest-28`; none disagrees with the specs.

Recall terms used: offline create cached tip read_feed_lease_tip tombstone epoch for life feed gov-queue.log empty parent
