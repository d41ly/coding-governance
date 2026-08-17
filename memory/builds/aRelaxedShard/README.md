---
slug: aRelaxedShard
node: a
opened: 2026-08-17
streams: tooling
roster: TOOL
ids: TOOL-aRelaxedShard-1
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
3. **The two halves of the rule bind on different populations, and nothing says so.** The byte bound
   decides the backlog shards and the decision log; the line bound decides the other 22 row documents,
   dossiers above all. rev-1 read the first half as the whole rule and the audit caught it — see F5. The
   byte figure also ships in prose in eight carriers, which is why moving it is a sweep, not an edit.

## The unit set

Classification per the build method, written before acting: unit 1 was **MISSING**, was authored this
run, was audited at M4, and is now **FORKED** at rev-2 — its §8 carries five items, and with no standing
mandate they are the owner's.

The audit is recorded at `reviews/2026-08-17-review-TOOL-aRelaxedShard-1.md`, which owns its shape
measurements and its finding list. Verdict **BLOCKED**, and rev-2 is the fold. The blocker RESCOPED the
unit — see F5 — and six further findings were downstream of one omission: an Inventory table that
measured 7 of the 29 documents in the class it claimed to enumerate.

The owner sequenced two units. Unit 1 is the knob and the correction. The second is the re-shape —
sharding a backlog below `FAMILY`, or a spill tier like the run-state file's — and its id is minted when
its spec is authored rather than reserved here, so that nothing in this folder cites an id check 14
would call an orphan.

The honest limit of unit 1, stated here because it is the thing an overview must not oversell: no byte
cap compatible with a readable file buys a quarter of runway at this minting rate. Unit 1 buys weeks.
The re-shape is what changes the slope, which is why the owner put it second rather than instead.

## Owner decision menu

Five forks, each carrying a recommendation in the spec's §8 and none of them resolved. **F5 is the one
that needs your attention first: it is a fork you already answered, and the answer rested on a premise
the audit falsified.**

- **F5 — the row line bound, re-opened.** You chose to retire it on rev-1's recommendation that it
  "cannot fire". Measured over the real population it is the bound that binds FIRST on 22 of 29 row
  documents, all 12 map dossiers among them, and check 6 is the only gate that bounds a dossier at all.
  Retiring it would loosen the dossier allowance 3.3x to 4.3x — the exact loosening a ratified decision
  refused. Recommended now: **do not retire it.** The goal is met by the byte bound alone, and that
  narrowing is a smaller diff which leaves the raise inert for the 22 line-bound documents, so it reaches
  only the shards you asked about.
- **F1 — the declared cap value for this repo.** 61,440 bytes recommended, derived from 250 rows at the
  measured 253.7 B/row. Runway about 21 days. Two alternatives are priced in §8, including an 80-day one
  listed in order to be rejected on readability. The kit's shipped default stays at today's value, so
  this fork decides only what this tree declares and no adopter inherits this corpus's number.
- **F2 — absent-and-blank semantics.** Recommended that both resolve to the shipped default and that no
  value disables the bound. This argues against the conf's own local idiom, so it is the fork most worth
  overruling if the consistency cost reads higher than the off-switch risk.
- **F3 — one row-class key, or a per-kind matrix.** One key recommended; the matrix is a config surface
  for a case nobody has.
- **F4 — a stale claim, confirm or park.** cSteadyMetronome recorded that rotating a backlog orphans
  every id the moved rows defined. The source says otherwise and three landed rotations agree with the
  source. Recommended: confirm by fixture in this unit, because the re-shape unit's options depend on
  whether rotation is live or dead.

## What this build found on the way in

Two things worth recording separately from the cap change itself.

The byte half of check 6 has never been armed. Two of its three fixtures trip on line count and the
third, `memory/guides/twide.md` at 401 lines, is a deliberate SILENT control that must stay one — so the
bound that fires in production has no test behind it. Unit 1 ADDS a byte-axis arm rather than rebuilding
the line-axis ones, which is a coverage gain wider than this unit and, per the audit, the safer half of
the two options.

`memory/guides/BUILD-METHOD.md` and its kit template both cite hygiene rule 6 for a budget rule 6 does
not impose on a guide — the guide class is three times wider. The self-imposed discipline is real,
because the build method is re-read whole at every pass boundary; the citation is wrong. Both carriers
are in this unit's prose sweep anyway, so S12 corrects the attribution while it is there.

The table below is GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node a · opened 2026-08-17 · streams tooling · ids TOOL-aRelaxedShard-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aRelaxedShard-1 — the row-document byte cap becomes a declared value](spec/2026-08-17-spec-TOOL-aRelaxedShard-1.md) | OPEN | rev-2 | 2026-08-17 |

Records live under `spec/` and `reviews/`.
<!-- /gen:build-index -->
