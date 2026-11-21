# TOOL-dPlacedRequest-28 — every create of a lease ref reads the feed first, the offer's included

**Status:** CLOSED · rev-4 · 2026-11-19 · node a · Tier-2 · base c63aabbb · streams tooling · order 7 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-28-deviation-281.md](../build/2026-10-25-build-TOOL-dPlacedRequest-28-deviation-281.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-build-TOOL-dPlacedRequest-28-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dPlacedRequest-28-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dPlacedRequest-28-red-fix-13.md](../build/2026-11-19-build-TOOL-dPlacedRequest-28-red-fix-13.md) | red-fix | — |
| [2026-11-21-build-TOOL-dPlacedRequest-28-deviation-674.md](../build/2026-11-21-build-TOOL-dPlacedRequest-28-deviation-674.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-28-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-28-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dPlacedRequest-28-divergence-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-28-divergence-brief.md) | research | — |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 53 at HIGH**, its item **H7**. `TOOL-dPlacedRequest-20` S1 makes `--lease offer` on
an absent lease "a create at epoch 1", while `TOOL-dPlacedRequest-16` S5, which restores an absent
ref's epoch from the change feed and refuses `tombstone`, is scoped to "an acquisition", and an offer
is not one. A build or unit tombstone deleted outside the kit, or a pruned cadence lease, can then be
re-created by an offer as `released` at epoch 1: the closed build is freed for any node and the epoch
falls, the outcome `TOOL-dPlacedRequest-16` AC5 marks red.

The class is wider than the offer. Every lease commit is built in
`tools/unattended/unattended.sh#write_claim`, while the one feed read sits inline in
`tools/unattended/unattended.sh#run_lease_verb`. So the driver's own claim writes, which reach
`write_claim` with the `create` act and an empty tip from
`tools/unattended/unattended.sh#check_claim_writable`, build a parentless commit at epoch 1 over a ref
the feed last saw as a tombstone. This unit puts the read in `write_claim`, once, for every create on
an empty tip, and gives a feed tombstone the refusal each column already gives a tombstone on the
remote.

## 2. Scope (IN)

- **S1** — One reader, `read_feed_lease_tip <lease ref>`, in `tools/unattended/unattended.sh`, whose
  one caller is `tools/unattended/unattended.sh#write_claim`. It prints nothing when the feed holds no
  commit for the ref; `tombstone <commit>` when the newest feed commit for it is a build or unit
  tombstone, as `TOOL-dPlacedRequest-16` S3 defines one; and otherwise `<commit> <epoch>`, that commit
  and the epoch its record carries. It holds the read `tools/unattended/unattended.sh#run_lease_verb`
  makes inline today under its comment "THE EPOCH FOR LIFE (S5)", moved here with its `awk` and its
  `cat-file` unchanged, and `run_lease_verb` keeps no feed read of its own. Observed by AC4 and AC5.
- **S2** — Every create calls it, inside `write_claim`. When the act `check_claim_writable` chose is
  `create` and the tip read `CW_SHA` is empty, `write_claim` calls `read_feed_lease_tip` on the ref it
  writes before it builds the commit. That is every lease create: the `--lease` verbs `acquire`,
  `take-over` and `offer`, a draw, the offline branch's queued create, and the driver's own claim
  writes in every column of `tools/unattended/unattended.sh#check_claim_writable`.
  `<commit> <epoch>` makes the write a create parented on `<commit>` at `<epoch>` plus one, the ref
  still expected absent on the remote; nothing makes such a write a create at epoch 1.
  `tombstone <commit>` builds, pushes and queues nothing: `write_claim` returns 3, distinct from 1's
  lost race and 2's incomplete write, with `WC_WHY` naming the feed commit, and each column maps that
  return as §4 "The tombstone, by column" states. `TOOL-dPlacedRequest-16` S5's "an acquisition"
  therefore reads "every write that creates a lease ref". Observed by AC1, AC2, AC4, AC5 and AC6.
- **S3** — The offer over an absent ref. `tools/unattended/unattended.sh#write_lease_offer` resets no
  tip and no epoch of its own on a create, so its write reaches S2's read in `write_claim` as every
  create does: refused `tombstone`, or a create at the restored epoch with `status: released`, `offer`
  and `offer-deadline` as `TOOL-dPlacedRequest-20` S1 writes them, or a create at epoch 1 when the
  feed holds no commit for the ref. Observed by AC1, AC2 and AC3.
- **S4** — The class. `write_claim` is the one product caller of `build_gov_commit` (PINNED 2026-11-19
  by `git grep -n build_gov_commit -- tools/`, its two definitions and the test suites aside), and its
  read runs before every create on an empty tip. So no lease create builds a parentless commit over a
  ref the feed holds a commit for. Observed by AC5.

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
write_claim: CW_ACT create, tip read empty
  read_feed_lease_tip <ref>
    ""                   -> create, no parent, epoch 1
    tombstone <commit>   -> return 3, nothing built; WC_WHY: the remote no longer holds it,
                            and this node's feed last saw its tombstone <commit>
    <commit> <epoch>     -> create, parent <commit>, epoch <epoch> + 1
```

The read sits after `write_claim` derives its ref and before it computes the epoch, and a write whose
ref does not derive refuses as today, reading nothing. The acquire, the take-over, the draw, the
offer and the driver's claim writes differ only in the record they write; the parent and the epoch
come from one place.

The `--lease` verbs print the tree's line for a feed tombstone and exit 1:

```
lease refused — tombstone · <tail> · the remote no longer holds it, and this node's feed last saw its tombstone <commit>
```

It names the feed commit and no holder, because the remote holds no record to read one from.

### The tombstone, by column

`write_claim` maps return 3 once, in the refusal arm where it maps 1 and 2 today, keyed on the column
`tools/unattended/unattended.sh#check_claim_writable` graded. Every driver call of `write_claim`
follows a `check_claim_writable` call naming its column (read at each caller below), and that
function records the column it graded as `CW_MODE`. The policy argument cannot key the map, because
`strict` serves three columns: `verb_preflight`'s preflight, `run_takeover`'s take-over and
`verb_close`'s holder. The check numbers are the `fail` calls of `check_claim_writable`'s
`foreign-tombstone` arms (PINNED 2026-11-19).

| column | its `write_claim` callers | on return 3 |
|---|---|---|
| `preflight` | `tools/unattended/unattended.sh#verb_preflight` | check 107, its message carrying `tombstone` and `WC_WHY`; exit 1 |
| `take-over` | `tools/unattended/unattended.sh#run_takeover` | check 107, as above; exit 1 |
| `holder` | `tools/unattended/unattended.sh#verb_resume`, `tools/unattended/unattended.sh#verb_close`, `tools/unattended/unattended.sh#verb_dispatch` | check 108, its message carrying `tombstone` and naming `--abort <slug> --code claim-lost`; exit 1 |
| `status` | `tools/unattended/unattended.sh#verb_landed`, `tools/unattended/unattended.sh#verb_abort`, `tools/unattended/unattended.sh#run_hold`, `tools/unattended/unattended.sh#write_settle_claim`, the re-bind in `tools/unattended/unattended.sh#verb_resume` | the one `claim not written` line `soft` prints today, carrying `WC_WHY`; nothing written; exit unchanged |
| `beat` | `tools/unattended/unattended.sh#write_claim_beat` | nothing from `write_claim`; the verb's `skipped` line carries `WC_WHY`; exit 0, as its decline is today |
| `lease` | `tools/unattended/unattended.sh#run_lease_verb`, through `write_lease_offer` for an offer | nothing from `write_claim`; `run_lease_verb` prints the line above; exit 1, queued or not |

Three callers read a non-zero return by value, and each takes one edit:

- `tools/unattended/unattended.sh#verb_resume`'s two holder writes return 1 on a return of 1 only;
  they return 1 on 3 as well.
- `tools/unattended/unattended.sh#write_settle_claim` prints its retry line on any non-zero return; on
  3 it prints none, since a retry over a feed tombstone writes nothing either.
- `tools/unattended/unattended.sh#run_lease_verb` maps 3 to the refusal line before its queued branch
  reads the return, so an offline create refused at the feed exits 1, not 2.

Every other caller already ends on a non-zero return or ignores it, as the table's last column
requires.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_feed_lease_tip` | shell function | `read`, OK by `lexicon.py --suggest read_feed_lease_tip --as sh.function` |
| `CW_MODE` | shell global, set by `check_claim_writable` | none: the lexicon declares no `sh.constant` cell |
| return 3 of `write_claim` | return code | none |

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `read_feed_lease_tip`; `write_claim`'s read and its return-3 arm;
  `check_claim_writable`'s `CW_MODE`; `run_lease_verb`'s inline read moved out and its return-3 arm;
  `write_lease_offer`'s create reset; `verb_resume`'s two holder reads; `write_settle_claim`'s retry
  line; and the header comments of `write_claim`, `run_lease_verb` and `write_lease_offer`
- `tools/unattended/unattended.test.sh`: the offer-over-tombstone arms and the driver's create arms
- `tools/unattended/STOPS.template.md`: section 7's epoch-for-life sentence names every create
- `memory/guides/UNATTENDED-STOPS.md`: its render
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads,
  so `gen_map.py --check` exits 0 after the pass; `TOOL-dPlacedRequest-34` S38 is the final re-check
  only

### Alternatives rejected

- **Copy `TOOL-dPlacedRequest-16` S5's read into the offer.** Two copies of the epoch-for-life rule,
  one of which the next create path will miss.
- **Refuse an offer on an absent ref.** `TOOL-dPlacedRequest-20` S1 makes an absent lease offerable,
  which the head that offers whole units across builds needs.
- **The read at each caller (§8 F2's option b).** Seventeen call sites of `write_claim` (PINNED
  2026-11-19, `grep -c 'write_claim "' tools/unattended/unattended.sh`) and one more for each new
  writer, any of which can skip it.
- **The map at each caller.** Fifteen of those call sites are the driver's (PINNED 2026-11-19, the
  same count less the lease verbs' two), and `check_claim_writable` maps a tombstone on the remote in
  one arm keyed on the column; F3 maps the feed's tombstone exactly as that arm does.
- **The map keyed on the policy argument.** `strict` serves three columns, so it cannot tell check 107
  from check 108.

## 5. Production-readiness checklist

- security — closes the paths that freed a closed build to any node: the offer's create and the
  driver's own create over a deleted tombstone.
- perf / scale — one `awk` over the feed and one `cat-file` per create on an empty tip, as
  `TOOL-dPlacedRequest-16` §5 already counts.
- error / empty / loading states — a feed that holds no commit for the ref is a plain create, as
  today.
- observability — every refusal names `tombstone` and the feed commit; the driver's carries its
  column's check number.
- risks — none beyond `TOOL-dPlacedRequest-16` §5's: a node whose feed never named a pruned run lease
  restarts its epoch at 1.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; `help/loop.md` anchors the driver's verbs beside its `--claims` paragraph, and this unit adds no verb.

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
  it prints nothing, `tombstone <commit>` and `<commit> 4` for the three AC cases, and
  `--lease acquire unit tFix TOOL-tFix-2` over AC1's ref still exits 1 printing `tombstone` and the
  feed commit.
  Red when: the acquire and the offer read the feed differently.
- **AC5** — When a probe in the tree the unattended suite's claim fixture `arm_claim_fixture`
  builds, over a build lease `refs/gov/leases/tRun/build` planted `released` at epoch 4 by
  `seed_lease_at`, sighted and deleted on the origin with `update-ref -d`, sources
  `tools/unattended/unattended.sh`, runs `load_driver_conf`, `read_claims strict` and
  `check_claim_writable tRun preflight k1 s1 k1`, then calls `write_claim tRun live k1 strict`, it
  returns 0, and
  `git --git-dir=<origin> rev-parse refs/gov/leases/tRun/build^` prints the feed's commit while the
  ref reads `epoch: 5`.
  Red when: a staged copy of `unattended.sh` whose `write_claim` skips the read builds the driver's
  create as a parentless commit at `epoch: 1`.
  figure: epochs 4 and 5 PINNED, the fixture's planted epoch and its successor.
- **AC6** — When `unattended.sh --preflight tRun --keepalive-id k1` runs in the tree
  `arm_claim_fixture` builds, whose feed's newest commit for `refs/gov/leases/tRun/build` is a build
  tombstone and whose origin holds no such ref, it exits 1 printing check 107 and `tombstone`, and
  `git --git-dir=<origin> for-each-ref refs/gov/leases/tRun` prints nothing.
  Red when: the preflight's create revives the deleted tombstone, the origin gaining a `live` build
  lease at epoch 1.
  fixture: `seed_lease_at` plants the tombstone `landed`, a lease read sights it, and `update-ref -d`
  deletes it on the origin, as `TOOL-dPlacedRequest-16` AC5's arm does; the tree holds both helpers.
  figure: check 107 PINNED 2026-11-19, the `fail` call of the preflight column's tombstone arm in
  `check_claim_writable` of `tools/unattended/unattended.sh`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `scratch-guard self-test` · `tier2-review self-test`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the offer over a deleted tombstone, a deleted released lease and an unnamed ref, staged against `TOOL-dPlacedRequest-20`'s epoch-1 create, and the driver's create over a feed-named released lease and a feed tombstone, staged against a `write_claim` that skips the read · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How does the offer reach the epoch-for-life read?** (a) One reader every create calls; (b) the
  offer calls the acquire path's read inline; (c) the offer refuses an absent ref. (b) leaves the rule
  in two places; (c) contradicts `TOOL-dPlacedRequest-20` S1. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound. widens: none · relaxes: none
- **F2 — Where does the create's feed read live, when every lease commit is built in
  `tools/unattended/unattended.sh#write_claim`?** (a) In `write_claim`, once, for every create with an
  empty parent, the `--lease` verbs and the driver's own claims alike; (b) at each caller.
  RESOLVED (agent, 2026-11-19, delegated): (a), rung 3; one commit builder, one read, and no caller
  can skip it. widens: none · relaxes: none
- **F3 — What does the driver's create do over a feed tombstone?** (a) `write_claim` returns a code of
  its own for a tombstone, distinct from 1's lost race, and the driver's callers map it exactly as
  `TOOL-dPlacedRequest-16` §4 "The class order" maps a tombstone: the preflight and take-over columns
  fail check 107, the holder column check 108, each message carrying `tombstone`; the status column
  announces one line carrying `tombstone`, writes nothing and leaves the exit status unchanged; the
  `--lease` verbs print `lease refused — tombstone` and exit 1. (b) It shares 1's lost-race return.
  RESOLVED (agent, 2026-11-19, delegated): a distinct return code mapped as unit 16's class order maps
  a tombstone, rung 3; one refusal vocabulary for a tombstone wherever it is met. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 53 (HIGH, item H7).
- rev-2 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirrors
  hands-off TOOL-dPlacedRequest-42, hands-off TOOL-dPlacedRequest-43.
- rev-3 · 2026-11-19 · §4 Files touched · §5 · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 16 (M7), the user-docs line names
  `help/loop.md`, which anchors the driver's verbs; finding 17 (M8), this unit's own pass
  regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.
  §7 also names `scratch-guard self-test`, `tier2-review self-test`, the leg(s) the spec-token guard
  join names for this spec's Files touched.
- rev-4 · 2026-11-19 · §1 · S1 S2 S3 S4 · §4 · §5 · AC4 AC5 AC6 · §7 · §8 · folds
  `2026-11-19-prompt-TOOL-dPlacedRequest-28-divergence-brief` over the builder's DIVERGENCE in run
  `wf_2cdc917a-db6`: F2 puts the feed read in `write_claim` and moves `run_lease_verb`'s inline read
  into `read_feed_lease_tip`; F3 gives a feed tombstone return 3, mapped by column; AC5 is a behaviour
  probe of the driver's create; AC6 observes `--preflight` over a feed tombstone; the refusal line
  names the feed commit and no holder.

## 10. Reuse audit

The seam extended is `tools/unattended/unattended.sh#write_claim`, the compare-and-swap ref writer
that builds every lease commit, which this unit gives the feed read; the read itself is
`TOOL-dPlacedRequest-16` S5's, moved out of `tools/unattended/unattended.sh#run_lease_verb` into one
named reader, and the tombstone map is `tools/unattended/unattended.sh#check_claim_writable`'s
column-keyed arm, mirrored for the feed. `python tools/codebase-map/reuse_lookup.py "restore a lease
epoch from the change feed before a create"` ranked `before`, `changed`, `resolveLease` and
`check_lease_only_diff`, name stems only, and `python tools/codebase-map/reuse_lookup.py "map a claim
write refusal to the column that graded it"` ranked `write`, `write_text`, `Refusal` and `refusal`,
name stems only; none reads a feed or maps a claim column, so no existing seam fits beyond the code
named above. At rev-1, `python tools/memory-recall/query.py "how is a lease epoch kept rising after a
ref is deleted"` returned units 16 and 17 and the audit's H7. At rev-4, `python
tools/memory-recall/query.py "where does a driver claim create read the feed before it writes"` with
the terms below returned `TOOL-dPlacedRequest-42`, this spec and this revision's brief. None
disagrees with this spec's rule, though `TOOL-dPlacedRequest-42`'s §4 table still reads a bare
`tombstone` and a holder from the reader.

Recall terms used: `--terms "write_claim epoch for life feed tombstone create parentless check 107
108 class order column preflight holder"`
