# TOOL-dPlacedRequest-28 — every create of a lease ref reads the feed first, the offer's included

**Status:** DEFERRED · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 7 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-28-deviation-281.md](../build/2026-10-25-build-TOOL-dPlacedRequest-28-deviation-281.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 53 at HIGH**, its item **H7**. `TOOL-dPlacedRequest-20` S1 makes `--lease offer` on
an absent lease "a create at epoch 1", while `TOOL-dPlacedRequest-16` S5, which restores an absent
ref's epoch from the change feed and refuses `tombstone`, is scoped to "an acquisition", and an offer
is not one. A build or unit tombstone deleted outside the kit, or a pruned cadence lease, can then be
re-created by an offer as `released` at epoch 1: the closed build is freed for any node and the epoch
falls, the outcome `TOOL-dPlacedRequest-16` AC5 marks red. This unit repairs `TOOL-dPlacedRequest-20`
by giving the feed read one function that every write creating a lease ref calls, the offer's absent
path included.

## 2. Scope (IN)

- **S1** — One reader, `read_feed_lease_tip <lease ref>`, in `tools/unattended/unattended.sh`: it
  prints nothing when the feed never named the ref; `tombstone` when the newest feed commit for it is a
  build or unit tombstone, as `TOOL-dPlacedRequest-16` S3 defines one; and otherwise
  `<commit> <epoch>`, the newest feed commit and the epoch its record carries. It holds the read
  `TOOL-dPlacedRequest-16` S5 specifies, moved here unchanged. Observed by AC3 and AC4.
- **S2** — Every create calls it. A lease write whose read finds the ref absent on the remote calls
  `read_feed_lease_tip` before it builds a commit: `--lease acquire`, `take-over`, the driver's run
  claim as a build lease, and `--lease offer`. `tombstone` refuses with `TOOL-dPlacedRequest-1`'s
  refusal line and cause `tombstone`, exit 1, nothing written; `<commit> <epoch>` makes the write a
  create parented on `<commit>` at `<epoch>` plus one; nothing makes a plain create at epoch 1.
  `TOOL-dPlacedRequest-16` S5's "an acquisition" therefore reads "every write that creates a lease
  ref". Observed by AC1, AC2 and AC4.
- **S3** — The offer over an absent ref. `write_lease_offer`'s absent-lease branch takes S2's result:
  refused `tombstone`, or a create at the restored epoch with `status: released`, `offer` and
  `offer-deadline` as `TOOL-dPlacedRequest-20` S1 writes them, or a create at epoch 1 when the feed
  never named the ref. Observed by AC1, AC2 and AC3.
- **S4** — The class check. No lease create reaches `build_gov_commit` with an empty parent except
  through S2's "never named" branch. Observed by AC5.

## 3. Non-goals (OUT)

- No change to the offer's rules on a `released` or held lease: `TOOL-dPlacedRequest-20` S1-S5.
- No handling of a feed-named commit the clone can no longer read: finding 61's, an item of
  `TOOL-dPlacedRequest-34`, which extends `read_feed_lease_tip`.
- No skipping of the feed's deletion events in the walk: finding 3's, an item of
  `TOOL-dPlacedRequest-34`, which extends the same reader.
- The finding's medium twin, finding 11, is an item of `TOOL-dPlacedRequest-34` observed over this
  unit.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-20` — `write_lease_offer` and its absent-lease branch, which this unit routes through the feed; without it there is no offer create to guard
- **consumes-from** `TOOL-dPlacedRequest-16` — S5's feed read of an absent ref and the `tombstone` cause, which this unit extracts into `read_feed_lease_tip`; without it there is no epoch-for-life rule to apply
- **hands-off** `TOOL-dPlacedRequest-34` — `read_feed_lease_tip`, which that unit's items for findings 3, 11 and 61 extend and observe
- **hands-off** `TOOL-dPlacedRequest-42` — `read_feed_lease_tip`, which that unit calls from the offline branch's empty-tip create
- **hands-off** `TOOL-dPlacedRequest-43` — S4's class, which that unit's items for findings 4 and 19 observe by behaviour over every online create

## 4. Design

### The create, once

```
read lease ref on the remote: absent
  read_feed_lease_tip <ref>
    ""                  -> create, no parent, epoch 1
    tombstone           -> lease refused — tombstone · <tail> · <holder in the feed's record>   exit 1
    <commit> <epoch>    -> create, parent <commit>, epoch <epoch> + 1
```

The acquire, the take-over, the run claim and the offer differ only in the record they write after
this; the parent and the epoch come from one place.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_feed_lease_tip` | shell function | `read`, OK |

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `read_feed_lease_tip`, its callers and `write_lease_offer`'s
  absent branch
- `tools/unattended/unattended.test.sh`: the offer-over-tombstone arms
- `tools/unattended/STOPS.template.md`: section 7's epoch-for-life sentence names every create
- `memory/guides/UNATTENDED-STOPS.md`: its render

### Alternatives rejected

- **Copy `TOOL-dPlacedRequest-16` S5's read into the offer.** Two copies of the epoch-for-life rule,
  one of which the next create path will miss.
- **Refuse an offer on an absent ref.** `TOOL-dPlacedRequest-20` S1 makes an absent lease offerable,
  which the head that offers whole units across builds needs.

## 5. Production-readiness checklist

- security — closes a path that freed a closed build to any node.
- perf / scale — one `awk` over the feed and one `cat-file` per create of an absent ref, as
  `TOOL-dPlacedRequest-16` §5 already counts.
- error / empty / loading states — a feed that never named the ref is a plain create, as today.
- observability — the refusal names `tombstone` and the ref.
- risks — none beyond `TOOL-dPlacedRequest-16` §5's: a node whose feed never named a pruned run lease
  restarts its epoch at 1.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the kit.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-16` AC5's: a scratch clone with a bare origin, `RUN_CLAIMS=on`, a
lease written and sighted, then deleted on the remote outside the kit.

- **AC1** — When a sighted unit tombstone `refs/gov/leases/tFix/unit/TOOL-tFix-2` is deleted on the
  remote and `--lease offer unit tFix TOOL-tFix-2 --to b` runs, it exits 1 printing `tombstone` and the
  remote holds no such ref.
  Red when: the offer re-creates a deleted tombstone, the planted case being `TOOL-dPlacedRequest-20`'s
  epoch-1 create.
- **AC2** — When a sighted `released` lease at epoch 4 is deleted on the remote and the same offer
  runs on it, the remote ref reads `epoch: 5`, `status: released`, `offer: b`, and its parent is the
  feed's commit.
  Red when: the offer's create restarts the epoch.
- **AC3** — When the offer runs on a ref the feed never named, the remote ref reads `epoch: 1` and has
  no parent.
  Red when: an unnamed ref is refused.
- **AC4** — When a probe sources `unattended.sh` and calls `read_feed_lease_tip` over a planted feed,
  it prints nothing, `tombstone` and `<commit> 4` for the three AC cases, and `--lease acquire unit
  tFix TOOL-tFix-2` over AC1's ref still exits 1 printing `tombstone`.
  Red when: the acquire and the offer read the feed differently.
- **AC5** — When an `awk` over `tools/unattended/unattended.sh` lists each function body that calls
  `build_gov_commit ""` and spells `refs/gov/leases` or `derive_lease_ref`, it lists only the function
  holding S2's "never named" branch.
  Red when: a second lease create builds a parentless commit, the planted case being a scratch copy
  whose `write_lease_offer` keeps its own create.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · the offer over a deleted tombstone, a deleted released lease and an unnamed ref, staged against `TOOL-dPlacedRequest-20`'s epoch-1 create · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How does the offer reach the epoch-for-life read?** (a) One reader every create calls; (b) the
  offer calls the acquire path's read inline; (c) the offer refuses an absent ref. (b) leaves the rule
  in two places; (c) contradicts `TOOL-dPlacedRequest-20` S1. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 53 (HIGH, item H7).
- rev-2 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirrors
  hands-off TOOL-dPlacedRequest-42, hands-off TOOL-dPlacedRequest-43.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-16` S5's feed read of an absent ref, moved into one named
reader, and `TOOL-dPlacedRequest-20`'s `write_lease_offer`; neither exists at the pinned base. `python
tools/codebase-map/reuse_lookup.py "restore a lease epoch from the change feed before a create"`
ranked `before`, `changed`, `resolveLease` and `check_lease_only_diff`, name stems only; none reads a
feed, so no existing seam fits beyond the two units this repairs. `python
tools/memory-recall/query.py "how is a lease epoch kept rising after a ref is deleted"` returned units
16 and 17 and the audit's H7; none disagrees with the specs.

Recall terms used: epoch for life feed tombstone offer create absent lease cat-file prune
