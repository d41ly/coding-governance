# Acceptance ledger — DEPL-dRetiredFork-1

**Serves:** journal DEPL-dRetiredFork-1

Tier-2 · node d · 2026-09-03

## F1, the central fact, answered — and the answer is the awkward one

F1 asked how many of NicoCares' nineteen forks actually move, with an explicit liveness note: a
ZERO answer is real, and if the residual-byte problem dominates then "this unit's value collapses
onto `DEPL-dRetiredFork-7` and the owner should see that before it is built."

**Measured after the fix: still ZERO `relocate` rungs at NicoCares.**

The mechanism is NOT broken, and the two are separable. Isolated on a fixture with no residual byte:

| needle source | rung |
|---|---|
| the global map (what the proof read before) | `None` |
| the row's own overlay (what it reads now) | **`relocate`** |
| the row's own overlay, plus ONE residual byte | `None` |

So S1 does exactly what it claimed — it turns `None` into `relocate` for a fanned directory — and it
moves nothing at that adopter because every row there carries a residual byte. Every
`nc carve-out N/20` comment is such a byte. §3 puts that out of scope and names
`DEPL-dRetiredFork-7`; this measurement is the evidence for the ordering rather than an assertion
about it.

## Acceptance criteria

**Evidences:** DEPL-dRetiredFork-1

- AC1 — MET on the mechanism, by `python tools/govkit/selftest.py` arms `[-1] S1`: a fanned gov
  directory is still dropped from the global map, the row's own overlay supplies the needle, and the
  rung is `relocate` where the map gave `None`. A fourth arm pins the limit — one residual byte and
  it falls to three-way — so the first three cannot be read as a general promise
- AC2 — MET — `govkit update` now names the ROWS in each drop. Measured at NicoCares: 7 drop
  messages, each followed by the paths it freezes. A message naming only a directory does not tell an operator which files are
  affected
- AC3 — MET, and NARROWED from what I first built — `derive_carry_map` plus the caller's guard.
  The refusal fires on an empty map over rows that
  DO name a gov directory, with nothing dropped as ambiguous — the case where the lift had subjects
  and produced nothing. It does not fire on a receipt of root-level rows, where an empty map is the
  correct answer
- AC4 — **NOT MET.** `relocate` is 0 at NicoCares, not "strictly greater than zero". Recorded with
  the isolation above, which is what makes it a finding rather than a failure
- AC5 — MET — `python tools/govkit/selftest.py` exits 0, all arms held, with seven added
- AC6 — **NOT MET, and deliberately not attempted** — it requires `update --write` against a tree
  gov does not own. See below
- AC7 — MET as EMPTINESS, not as single-character — `derive_carry_map` raises `Refusal` on an empty
  or whitespace fragment. The single-character half was measured to break 16 arms in other units and
  is recorded below as a stated residual rather than built
- AC8 — MET — `python tools/govkit/govkit.py selfcheck` exits 0
- S6 before-counts, on the record: **32** `evidence: "unattributed"` rows at NicoCares, **30** at
  inCMS, 7 dropped carry directories, 0 `relocate`

## AC6 was not attempted, and that is a decision rather than an omission

S7 requires driving NicoCares' unattributed count to zero, which means `update --write` against a
repository gov does not own, with no owner present. **Parked.** Three independent reasons, none of
which a run may overrule on its own authority:

- §9 — automation writes are draft-only by default, and an autonomous irreversible action sits
  behind an explicit default-OFF gate
- this build's own repeated boundary — `DEPL-dRetiredFork-7`, `TOOL-dRetiredFork-14` and
  `TOOL-dRetiredFork-21` each state that gov owns none of an adopter's tree and that removal happens
  on the adopter's own timing
- the authorization — a committed build folder in gov authorizes landing THIS build in gov, not
  writing to a different repository whose owner may have live work in it

The spec's own §5 names the failure mode as silent data loss in a repository gov does not own. That
is precisely the case where an owner turn is worth more than a green criterion.

## Two things I built wrong first, both caught by arms belonging to other units

**S3b refused too much.** The risk §5 names is a needle whose width exceeds the path it names, and
the wide reading — refuse anything under two characters — broke 16 arms, because gov's own fixtures
legitimately use single-letter directory names. The grade now covers emptiness, which is the case §5
actually names, and the **residual is stated rather than hidden**: a one-character needle is
permitted and would match widely if a real receipt produced one. What contains it is what contains
every wrong needle — the rung is proved by whole-file equality before any write.

**S3 refused too much as well**, and for a different reason: an empty map is legitimate when every
row is a root-level file, since those lift to the empty needle and are skipped by design. The same
16 arms failed again until the predicate learned to ask whether the lift had subjects at all.

Both were mine, both were found by running the suite rather than by reading the diff, and neither
would have been visible in gov's own tree.
