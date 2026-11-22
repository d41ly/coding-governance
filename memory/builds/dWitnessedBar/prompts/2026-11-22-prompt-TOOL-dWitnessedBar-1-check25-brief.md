**Serves:** journal TOOL-dWitnessedBar-1

# Brief — dWitnessedBar: eight live specs' readers clauses answer for three moved paths

## The prompt

> Yes, sweep them

— owner, 2026-11-22, on the close's seventeen own red legs; this brief is the `memory hygiene` leg's check 25.

## The brief

### Goal

Make check 25 of `tools/memory-tree/check-memory-hygiene.sh` green over the eight `by name:` halves it reds. Three paths
moved under dWitnessedBar, and each half below still lists a path's old spelling, which no reader spells now. Revise
each spec in place, as a rev bump with one revision-log line naming this brief by its file stem.

### Items

1. In each half below, either re-point the listed name to the path's current home where a reader spells that home, or
   append `READER NOT IN TREE` and a one-clause reason naming the move (HYGIENE.md, "Which half is graded how"). Keep
   every other byte of the clause, and change nothing else in the spec.
   - `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-2-u1-journal-relocation.md` §2 S6, and
     `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-6-u6-doc-truth.md` §2 S5: they list
     `tools/dead-path-waivers.txt`, moved to `memory/project/dead-path-waivers.txt` by TOOL-dWitnessedBar-16 S14.
   - `memory/builds/bConvergentLodestar/spec/2026-07-22-spec-bConvergentLodestar-1.md` §2 S4: it lists
     `memory/map/affordance-exempt.toml`, converted to `memory/map/affordance-exempt.txt` by the
     `codebase-map/affordance-exempt-to-ledger` step.
   - `memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md` §2 S1 and S2,
     `memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md` §2 S1,
     `memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-41.md` §2 S2, and
     `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-28.md` §2 S7: they list
     `tools/policy/legacy-homes.txt`, moved to `memory/project/legacy-homes.txt` by TOOL-dWitnessedBar-20.
2. A spec whose status header is CLOSED is not edited; name it in your return instead.

Before returning, run `bash tools/memory-tree/check-memory-hygiene.sh` and confirm its output holds no
`check 25 FAILED` line naming these specs, and run `python tools/check-spec-tokens.py --spec <path>` over each spec
you edited, fixing every finding either names.

### Acceptance

check 25 names none of the eight halves; each edited spec carries the next rev and one revision-log line naming this
brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside the eight halves. No product code. No change to any clause's intent.
