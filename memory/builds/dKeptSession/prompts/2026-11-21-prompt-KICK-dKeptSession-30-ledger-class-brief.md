**Serves:** research KICK-dKeptSession-30 KICK-dKeptSession-32 KICK-dKeptSession-35 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65

# Brief — dKeptSession: the other-unit-ledger class, resolved across the remaining specs

## The prompt

> /unattended dKeptSession

## The brief

### Goal

Units 49 and 50 each diverged at build for the same reason. Their spec answered another unit's superseded text in
that other unit's acceptance ledger, which a later unit may never write. Specs 49, 50, 47, 48, 51, 53, 55 and 61
now answer in their own ledgers, under the ruling of KICK-dKeptSession-49 rev-6 (in its open-questions section) and of
the brief `2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief`. The writer who applied that ruling found the
same shape in fifteen more specs:

- Specs 30, 32, 35, 37, 38, 41, 44, 45, 46, 56, 57 and 62 answer in another unit's ledger.
- Specs 63 (AC19, AC20, AC27), 64 (AC2, AC4, AC17) and 65 (AC13) have criteria that grep other units' ledgers.

Spec 63's AC20 now goes red for certain: it greps unit 53's ledger for `KICK-dKeptSession-61`, which unit 61 now
records in its own ledger. Revise these fifteen specs to the same ruling.

### Items

1. F-own-ledger: in each spec, every sentence that answers in another unit's acceptance ledger moves its answer to this unit's own ledger (`memory/builds/dKeptSession/build/2026-11-21-build-<this unit's id>-1-acceptance-ledger.md`). That ledger quotes the other unit's spec text it supersedes and joins Files touched. Where it trips a guarded leg (`recall floor`, `recall floor arms`, or a kit's fixtures leg whose guard covers a touched path), that leg joins section 7's leg line. Record the fork in the spec's open-questions section, resolved: `RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a CLOSED unit's records are never written by a later unit, as KICK-dKeptSession-49 rev-6 ruled.` Rejected: (a), writing the other unit's ledger. Add a criterion, or extend one, that observes the quoted passages in this unit's ledger.
2. F-ledger-reads (63, 64, 65): a criterion that greps another unit's ledger stands only if that unit, by its own spec at its current rev, writes the text grepped into its own ledger and builds before this one. Every other such criterion greps the ledger that now holds the text, as 63's AC20 must grep unit 61's own ledger. Re-check each one against the current rev of the spec it reads, including 47, 48, 51, 53, 55 and 61 as just revised.
3. F-behaviour: confirm every grep phrase a new or changed criterion counts appears in the source text it quotes, flattened the same way the criterion flattens it. No `path:number` token stands unless it is a blob pin. Re-cite every changed line as `path#symbol`. Keep within the live-spec size cap, pin every figure, and leave no fork open. Where a spec carries no instance of the class, say so and leave it at its rev.

### Acceptance

Each spec you changed is at a new rev, carrying the ruling and one revision-log line that names this brief by its
file stem. `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`,
`python tools/check-spec-tokens.py --spec <path>`, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
and `bash tools/unattended/unattended.sh --check-specs dKeptSession <its id>` report nothing for each.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip, and no spec outside these fifteen. Spec 31 matches too,
but another writer is checking 22, 31 and 5; read them, never write them. Unit 50 is being built: read its spec,
never write it.
