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

Every figure here was derived at base sha `43eb6b10`, not read from prose.

| row document | bytes | rows | share of the 20,480-byte cap |
|---|---|---|---|
| `memory/backlog/TOOL.md` | 19,152 | 73 | 93.5% |
| `memory/DECISIONS.md` | 12,328 | — | 60.2% |
| `memory/ledger/2026-08.md` | 3,240 | — | 15.8% |
| `memory/LIVE.md` | 2,054 | — | 10.0% |
| `memory/backlog/PLAY.md` | 1,741 | 9 | 8.5% |
| `memory/backlog/DEPL.md` | 1,734 | 11 | 8.5% |
| `memory/backlog/KICK.md` | 373 | 4 | 1.8% |

- **Row length** is 251 bytes, from 18,314 bytes across 73 rows in the tooling shard.
- **Minting rate** is 17.9 ids per day, from 161 distinct `TOOL-` ids first appearing over nine active
  days across the live shard and its three archives. The last four of those days average 20.3.
- **Live-set growth** is 8.1 rows per day, about 2,034 bytes, from the 73 non-terminal rows those nine
  days left standing.
- **Remaining headroom** is 1,328 bytes, which is **0.65 days**. That figure is the finding.

## Why rotation is finished as a remedy

Rotation carries forward every non-terminal row, so a live shard's floor is its live row set. The
tooling shard holds 73 live rows and zero terminal ones: its floor is its current 18,314 bytes, 89.4%
of the cap, and a fourth rotation would move nothing. It has already rotated three times in four days,
twice on one of them.

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
3. **Half the rule cannot fire.** At the 300-char entry budget a 250-line row document may hold 75,000
   bytes, so the byte bound decides every real case and the line bound needs rows averaging under 82
   bytes. Measured mean is 251. The retired figures also ship in prose in six carriers.

## The unit set

Classification per the build method, written before acting: unit 1 was **MISSING**, was authored this
run, and is now **FORKED** — its §8 carries four items, and with no standing mandate they are the
owner's. It is unreviewed by definition, so the M4 spec audit is the next pass.

The owner sequenced two units. Unit 1 is the knob and the correction. The second is the re-shape —
sharding a backlog below `FAMILY`, or a spill tier like the run-state file's — and its id is minted when
its spec is authored rather than reserved here, so that nothing in this folder cites an id check 14
would call an orphan.

The honest limit of unit 1, stated here because it is the thing an overview must not oversell: no byte
cap compatible with a readable file buys a quarter of runway at this minting rate. Unit 1 buys weeks.
The re-shape is what changes the slope, which is why the owner put it second rather than instead.

## Owner decision menu

Four forks, each carrying a recommendation in the spec's §8 and none of them resolved.

- **F1 — the ratified cap value.** 61,440 bytes recommended, derived from the line bound's own evident
  intent of 250 scannable rows at the measured row length. Runway about 21 days. Two alternatives are
  priced in §8, including the 90-day one, which is listed in order to be rejected on readability.
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

The byte half of check 6 has never been armed. All three of its fixtures trip on line count, so the
bound that fires in production has no test behind it, and retiring the line bound would have left the
row class with no arm at all. Rebuilding those arms on the byte axis is a coverage gain wider than this
unit.

`memory/guides/BUILD-METHOD.md` and its kit template both cite hygiene rule 6 for a budget rule 6 does
not impose on a guide, which gets 61,440 bytes and 750 lines. The self-imposed discipline is real,
because the build method is re-read whole at every pass boundary; the citation is wrong. Both carriers
are in this unit's prose sweep anyway.

The table below is GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node a · opened 2026-08-17 · streams tooling · ids TOOL-aRelaxedShard-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aRelaxedShard-1 — the row-document cap becomes one declared byte bound](spec/2026-08-17-spec-TOOL-aRelaxedShard-1.md) | OPEN | rev-1 | 2026-08-17 |

Records live under `spec/`.
<!-- /gen:build-index -->
