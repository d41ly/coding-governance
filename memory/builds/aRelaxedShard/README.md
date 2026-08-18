---
slug: aRelaxedShard
node: a
opened: 2026-08-17
streams: tooling
roster: TOOL
ids: TOOL-aRelaxedShard-1 TOOL-aRelaxedShard-2 TOOL-aRelaxedShard-3 TOOL-aRelaxedShard-4
---

# aRelaxedShard — the backlog budget stops being something rotation can pay

Node `a` · opened 2026-08-17 · streams tooling.

The owner reported that the backlog budgets are too low for the current rate of development, both on
this repo and in every tree the memory-tree kit is installed into, and asked for an overview before any
change. The overview is below. The measurement is worse than "low": the budget is spent, and the remedy
the gate names has nothing left to pay with.

## What was measured

The per-document figures, the row length, the minting rate and the live-set growth are all derived at
base sha `43eb6b10` and live in the spec's §4 Inventory, which owns them. This overview states only what
they add up to, so that there is one place to correct when the tree moves.

The tooling backlog shard is at 93.5% of its cap. Its remaining headroom is **0.65 days** of measured
net growth. That figure is the finding — not the percentage, which has read like a tight budget for a
week.

## Why rotation is finished as a remedy

Rotation moves terminal rows only. The tooling shard has none left, so a fourth rotation leaves the
whole file exactly where it is: the floor is **93.5%** of the cap, the file's own current size, and the
rotation announcements in its head stay too. It has already rotated three times in four days, twice on
one of them.

`TOOL-cSettledDocket-16` is OPEN in that shard and already says this. The unit closes it rather than
landing a duplicate beside it.

**On the tree this will land into it is already past tight.** The local default branch advanced 37
commits during the build, and at that tip the shard holds **20,345 of 20,480 bytes — 135 left, half of
one row** — with 80 rows and still nothing terminal. The next backlog row that tree receives reds the
gate. That forces a landing order, in the spec's §4 Rollout: the conf change lands before this build's
own decision rows, because writing the records first is red.

This was predicted. `memory/builds/cSteadyMetronome/README.md` recorded it on 2026-08-14, including the
detail that the unit it needed could not be given a backlog row because there was no room left to write
one. That is still true today.

## What the adopters inherit

Three separate problems, not one.

1. **No knob exists.** The cap is hardcoded in the engine's per-class cap block. Every sibling threshold
   in this kit is a conf key, so this is the one bound an adopter cannot set without editing the kit,
   which then reds kit/dogfood parity and forces a kit-version bump.
2. **The cap moves with their line endings.** `TOOL-aRootedPrefix-3` is open against checks 6 and 7 for
   measuring raw working-tree bytes. At the pre-kickoff base the tooling shard measured 20,408 bytes as
   LF and 20,492 as CRLF, so it was already over cap on a CRLF checkout. The inflation is under half a
   percent and it lands exactly where the margin is thinnest.
3. **The two halves of the rule bind on different populations, and nothing says so.** Of the 29 row
   documents, the byte bound decides 7 — the four backlog shards, the decision log, `LIVE.md` and one
   run-state file — and the line bound decides the other 22, all 12 dossiers among them. rev-1 read the
   first half as the whole rule and the audit caught it. The byte figure also ships in prose across eight
   carriers, two of which state the CLASS COUNT rather than a number and so cannot be found by grepping
   for one — which is why moving it is a sweep, not an edit.

## The unit set

Two units. **`TOOL-aRelaxedShard-1` is BUILT and not landed**, at rev-7 and `INPROGRESS`: authored here,
audited at M4 twice, both rounds folded, regrounded onto the default branch, then built and gate-verified.
Its five forks are resolved — F1, F3 and F5 ratified by the owner; F2 and F4 built on recommendations put
to the owner and not overruled. It stays `INPROGRESS` rather than `CLOSED` for two honest reasons: it is
not landed, and F4's recommended fixture was never scoped and is not built.

**`TOOL-aRelaxedShard-4` is the re-shape, authored 2026-08-18 and unreviewed.** It is the unit the owner
sequenced second, and its own measurement turned both mechanisms it was sequenced FOR into non-goals.

Both rounds are recorded under `reviews/`, and each owns its own shape measurements and finding list.
Round 1 returned **BLOCKED** on 21 distinct defects; rev-2 is its fold. Its blocker RESCOPED the unit and
six further findings were downstream of one omission — an Inventory table that measured 7 of the 29
documents in the class it claimed to enumerate. Round 2 audited only what rev-4 and rev-5 changed and
returned **CLEAN WITH FIXES** on 17 distinct defects with no blocker; rev-6 is its fold, and it says
plainly that round 3 is not warranted because building is now the stricter test. Its sharpest finding was
that two of the three arms rev-5 added to prevent a vacuous fixture were themselves vacuous.

### What unit 2 found, and why it is not what it was sequenced to be

Unit 1 bought about 18 days at the census rate. Unit 2 was meant to shard the backlog below `FAMILY` or give it a spill tier.
Measured first, both are the wrong shape:

- **Minting runs 18.9 ids/day against closure at 10.1**, so the live set grows +8.8 rows/day, about
  2,233 B/day, monotonically. A shard relocates that, a spill hides it, a bigger cap postpones it. Only
  minting less or closing more changes the slope, and neither is a file layout.
- **53 of the 82 rows name no kit at all.** Sharding by kit would put 65% in a catch-all and the largest
  real cluster is 11% — one file with the same problem plus nine small ones.
- **A spill tier is blocked on unit 1's F4**, the untested claim that rotating a backlog orphans the ids
  its moved rows defined. Two units now depend on that answer and it has been carried on a reading since
  2026-08-14.

So `-4` proposes the smallest thing that acts on the real variable: build F4's fixture, and add a
per-shard live-row drain signal against a shrink-only pin, so the growth becomes a decision rather than a
discovery. Its §8 asks whether to build even that on 18 days of runway.

## Owner decision menu

**All five forks resolved by the owner, 2026-08-17.**

- **F1 — the declared cap value.** **61,440 bytes**, derived as 250 rows at the measured 253.7 B/row.
  About 21 days of runway. The kit's shipped default stays at 20,480, so this declares a value for this
  tree only and no adopter inherits this corpus's number.
- **F5 — the row line bound.** **Retired outright.** Asked twice. rev-1 recommended it on a premise the
  audit falsified, so it went back with the measured population — 22 of 29 row documents line-bound
  first, all 12 dossiers among them, a 3.3x-to-4.3x dossier loosening that `TOOL-aWidenedGuide-1` had
  refused — and both alternatives. The owner chose outright retirement with that in front of them, so the
  spec records it as a deliberate relaxation of a ratified curation discipline. §4 prices what it costs
  and §3 states it as given up on purpose, so it can never read as an oversight inherited from rev-1.

**Building on a recommendation that was put to the owner and not overruled.** F2 — absent and blank both
resolve to the shipped default, and no value disables the bound. F4 — confirm by fixture that rotating a
backlog does not orphan the ids the moved rows defined.

- **F3 — the dossier bound.** **Its own conf key**, `DOSSIER_CAP_BYTES`, declared 20,480. F5's answer
  had left a dossier bounded only at 61,440 — 820 to 1,200 lines across the measured class, with check 6
  its only size gate. The key holds the loosening to **1.10x at the densest dossier and 1.60x at the
  sparsest** (274 and 400 lines) instead of 3.29x-to-4.80x. The cap block becomes three classes, keyed on
  the engine's existing `MAP_SUB` under an emptiness guard — unguarded it would resolve to `memory/` and
  cap every row document at the dossier bound.

Every fork is resolved, so the spec carries `ratified 2026-08-17`.

## What this build found on the way in

Two things worth recording separately from the cap change itself.

The byte half of check 6 has never been armed. Two of its three fixtures trip on line count and the
third, `memory/guides/twide.md` at 401 lines, is a deliberate SILENT control — so the bound that fires in
production has no test behind it. Retiring the row line bound makes fixing that mandatory rather than
merely worthwhile: the one row-class fixture is line-only, and three separate contracts are asserted
THROUGH it, so S9 grows it past the byte cap instead of letting it fall silent. The guide arms stay
untouched, because they are the only proof the two classes are still separate.

`memory/guides/BUILD-METHOD.md` and its kit template both cite hygiene rule 6 for a budget rule 6 does
not impose on a guide — the guide class is three times wider. The self-imposed discipline is real,
because the build method is re-read whole at every pass boundary; the citation is wrong. Both carriers
are in this unit's prose sweep anyway, so S16 corrects the attribution while it is there.

The table below is GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 2 unit(s) · node a · opened 2026-08-17 · streams tooling
ids TOOL-aRelaxedShard-1 TOOL-aRelaxedShard-2 TOOL-aRelaxedShard-3 TOOL-aRelaxedShard-4

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aRelaxedShard-1 — the row class becomes declared byte bounds](spec/2026-08-17-spec-TOOL-aRelaxedShard-1.md) | INPROGRESS | rev-7 | 2026-08-17 |
| [TOOL-aRelaxedShard-4 — the backlog's slope, not its ceiling](spec/2026-08-18-spec-TOOL-aRelaxedShard-4.md) | OPEN | rev-3 | 2026-08-18 |

Records live under `spec/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-17-review-TOOL-aRelaxedShard-1-round2.md](reviews/2026-08-17-review-TOOL-aRelaxedShard-1-round2.md) | spec-audit | TOOL-aRelaxedShard-1 |
| [2026-08-17-review-TOOL-aRelaxedShard-1.md](reviews/2026-08-17-review-TOOL-aRelaxedShard-1.md) | spec-audit | TOOL-aRelaxedShard-1 |
| [2026-08-18-review-TOOL-aRelaxedShard-4.md](reviews/2026-08-18-review-TOOL-aRelaxedShard-4.md) | spec-audit | TOOL-aRelaxedShard-4 |
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-17-spec-TOOL-aRelaxedShard-1.md](spec/2026-08-17-spec-TOOL-aRelaxedShard-1.md)
  - [2026-08-18-spec-TOOL-aRelaxedShard-4.md](spec/2026-08-18-spec-TOOL-aRelaxedShard-4.md)
- **`reviews/`**
  - [2026-08-17-review-TOOL-aRelaxedShard-1-round2.md](reviews/2026-08-17-review-TOOL-aRelaxedShard-1-round2.md)
  - [2026-08-17-review-TOOL-aRelaxedShard-1.md](reviews/2026-08-17-review-TOOL-aRelaxedShard-1.md)
  - [2026-08-18-review-TOOL-aRelaxedShard-4.md](reviews/2026-08-18-review-TOOL-aRelaxedShard-4.md)
<!-- /gen:build-docs -->
