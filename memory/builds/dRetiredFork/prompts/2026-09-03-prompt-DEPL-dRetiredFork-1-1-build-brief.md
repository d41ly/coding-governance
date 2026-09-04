# Build brief — DEPL-dRetiredFork-1

**Serves:** journal DEPL-dRetiredFork-1

## S4 first, because F1 decides whether the unit is worth building

Run read-only before any code. Measured against `C:/projects/nicocares/main`:

- **7 gov directories DROPPED** from the carry map, each named: `skills/session-kickoff`,
  `tools/drift-audit`, `tools/hooks`, `tools/memory-recall`, `tools/memory-tree`,
  `tools/unattended`, `tools/workflows`
- **0 `relocate` rungs**, exactly as §1 claims
- **32 `evidence: "unattributed"` rows** at NicoCares, **30** at inCMS — the spec's numbers reproduce

F1's liveness note says a ZERO answer is real and would collapse this unit onto
`DEPL-dRetiredFork-7`. Seven dropped directories is not zero, so the mechanism has subjects.

## The write this run will NOT perform

S7 and AC6 require driving NicoCares' unattributed count to zero, which means `update --write`
against a repository gov does not own. **PARKED, and the mechanism is built without it.** Three
reasons, none of which a run may overrule on its own authority:

- §9 — automation writes are draft-only by default; an autonomous irreversible action sits behind an
  explicit default-OFF gate
- this build's own repeated boundary — `DEPL-dRetiredFork-7`, `TOOL-dRetiredFork-14` and
  `TOOL-dRetiredFork-21` all state that gov owns none of an adopter's tree
- the authorization — a committed build folder in gov authorizes landing THIS build in gov, not
  writing to a different repository whose owner may have live work in it

The spec's own §5 names the failure mode as silent data loss in a repository gov does not own. AC6
is recorded NOT MET with its before-count, rather than met by an action nobody authorised.

## What IS built, and the risk it carries

S1 makes a fanned gov directory yield needles PER ROW instead of dropping. S2 keeps the drop for the
genuinely ambiguous case and names the ROWS, because a message naming a directory does not tell an
operator which files are frozen. S3 refuses an empty needle map. S3b grades every derived needle.

**§5 calls a wider needle map the highest-severity risk in the build**: a needle is a path fragment
used in a byte substitution over file content, so a wrong one writes gov's bytes over a target's real
edit. Two things contain it and both must hold — the rung is proved by WHOLE-FILE EQUALITY before any
write, so a row whose bytes are not exactly the carried form still falls to three-way; and S3b
refuses a degenerate fragment, since an empty or single-character needle matches far more than the
path it names. rev-1 built nothing for S3b and the §5 row is where the obligation is written down.

F2 ratified: the `carry` field records the RUNG, not the map, so no schema change — and the selftest
asserts that rather than assuming it.
