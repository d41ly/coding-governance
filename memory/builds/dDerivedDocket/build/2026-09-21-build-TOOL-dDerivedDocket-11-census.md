**Serves:** journal TOOL-dDerivedDocket-11

# The backlog migration census — TOOL-dDerivedDocket-11

Computed by `migrate_backlog.py --plan` at b8a773375bf26c48004a06c303d2968963370bc3 · signed none · design-named none. Every figure below is DERIVED at run time; none of them is authored anywhere, here or in a spec.

## The corpus

- 668 row copies over 4 live shard(s) and 3 family archive(s); 668 distinct ids.
- 590 live copies and 78 archived ones.
- 97 slugs own rows; 153 ids equal a spec H1.
- 334 ask(s) derive OPEN on a build whose derived status is terminal, over 59 such build(s).
- prospective family view sizes, in bytes, uncapped by owner ruling D3: DEPL 5414 · KICK 1682 · PLAY 1373 · TOOL 69492.
- 96 of 118 indexed builds are terminal.

## Findings the switch-over's commit must absorb

### Prospective ask files over the declared row cap

- none.

### Slugs owning rows with no build README — the prospective filing homes

- slug aFlaggedScaffold owns rows and has no tracked README
- slug aResumedRelay owns rows and has no tracked README
- slug aSiftedFork owns rows and has no tracked README
- slug aTracedSpawn owns rows and has no tracked README
- slug aWidenedGuide owns rows and has no tracked README
- slug aWiredReckoning owns rows and has no tracked README

### Rows whose text cites a backlog archive the switch-over deletes — 5 backticked citation(s), the population unit 34's fifth normalization rewrites

- memory/backlog/TOOL.md:482 cites TOOL.2026-08-17.md and TOOL.2026-08-17b.md and memory/archive/TOOL.2026-08-17.md and memory/archive/TOOL.2026-08-17b.md
- memory/backlog/TOOL.md:133 cites TOOL.2026-08-17b.md

## The conservation proof

- status-slot-removed: 668
- filed-inserted: 668
- unit-inserted: 0
- wrapped-row-joined: 1
- relative-link-rebased: 0
- archive-citation-unbackticked: 5
- every one of the 668 prospective ask rows re-parsed to its own id and its own normalized text; no other difference was found.
