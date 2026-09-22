# TOOL-dDerivedDocket-27 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-27

The declared gate wall is built. `GATE_WALL` is read at conf load through `read_bound_key` with an
empty default, unexported, and handed to `$GATE_CMD` alone. `GATE_PROFILE_CMD` is a declared command
the driver runs under `GATE_BOUND`, and the kit library parses its answer and compares the wall with
it, one predicate for the driver and the leg. `--preflight` pins the bar's backstop, wall + queue +
the `GATE_BACKSTOP_MARGIN` source constant, as the `gate-backstop` fact and refuses a wall below the
largest leg ceiling as check 85. `gates-green` bounds its bar by that fact through `run_bounded`'s
new per-call bound and reads how the bar ended: TREE MOVED runs once more, HOST prints a
`host-degraded` hold released by `probe host`, a kill before `gate queue: acquired` prints one
released by `probe gate`, a kill after it is the never-returned verdict, and exit 1 keeps the
inherited-red decision table. The runner's `--print-profile` gains `queue`, derived above the verb,
and `ceiling_max`. The kit leg gains check 42, the wall against that ceiling, and check 43, the
Skill's hold routing. Gov declares `GATE_WALL="21600"` and the runner's profile verb.

The spec moved to rev-10 before the code: AC14's first witness counted 3 at the parent, not 1, and
the protocol is already over its guide byte cap there. Section 9 names both and four readings the
design left open.

No merge bar, no gate leg and no `*.test.sh` suite ran in this pass. The driver suite's new backstop
block ran by hand behind a replica of that suite's helpers, over its own fixture: 50 assertions,
green, the nine kill arms included, and green again with the MIXED arm as extracted from the
staged suite, 55. The inherited-red block's new MIXED arm ran the same way over
that block's own fixture: 5 assertions, green. The leg suite's check 42 and 43 block ran behind a
replica of that suite's prologue: 24 assertions, green. Each then ran against staged breaks, one per
`Red when:` clause, and every break reddened the arms written for it:

- the bar bounded by `GATE_BOUND`: AC1 red, the 12 s queue killed at the 10 s bound;
- a kill before the acquire line read as a red bar: AC2 red, no hold line and the never-returned
  text printed;
- exit 3 read as a failed leg: both AC3 arms red; the re-run left without its bound: AC3 red on
  four runs where two were owed;
- the wall compared with the profile's own wall: AC4's driver arms red, the preflight writing its
  record; the same break in the leg reddened AC4's leg arms;
- HOST read as a red leg: AC7 red;
- every backstop kill mapped to `host-degraded`: AC11 red, a hold line printed after the acquire line;
- the declared wall never handed to the bar: AC12 red, `GATE_WALL=<unset>`; the driver's variable
  left exported and the `-u` dropped: AC12's blank arm red, `GATE_WALL=`;
- a profile that cannot answer refused at preflight: AC15 red, and every arm with it;
- a re-preflight that derives none leaving the earlier fact: the removal arm red;
- the decision table's quantifier made existential: AC13's MIXED arm red, the close MET over a MIXED
  red;
- in the leg, a blank profile command reddening check 42: AC15's leg arm red; the override case
  dropped from check 43: its arm red; check 43's order read by a search that resumes after each
  match: the `--hold`-first arm red, because a later sentence about `--hold` satisfied it.

The runner's `ceiling_max` program ran sliced out of the runner over the real manifest and three
fixtures: 16040, 30 over ceilings of 5, 30, "99", 0 and true, `-` for none, and exit 1 with no
output for a manifest that does not parse. The runner itself was not run in any form.

AC1, AC3, AC5, AC6, AC8, AC10, AC13 and AC15 carry `permission:` lines deferring them to VERIFYING,
so none of them gets a line here. AC1, AC3, AC13 and AC15 were nonetheless exercised by the replica
runs above; their lines are the orchestrator's.

**Evidences:** TOOL-dDerivedDocket-27
- AC2 — `probe gate` — a stub bar that never printed the acquire line, under a backstop of 3 pinned
  as `3 (wall 1 + queue 1 + margin 1)` by the margin seam, was killed and `gates-green` was UNMET
  printing the `host-degraded` hold line released by `probe gate`, reason "the bar was killed at its
  backstop before it acquired the repository", and the `--hold` it names, and no never-returned text.
- AC4 — `--preflight` — over a fixture declaring `GATE_WALL="10"` under a profile printing wall 40,
  queue 20 and ceiling_max 30, `--preflight` refused as check 85 naming 10s and 30s, printed that the
  run-state file is unchanged, and left the record byte-identical and the tree clean; at a wall of 30
  it pinned the backstop. The leg over the same declaration red check 42 naming both numbers, and
  reported the equal wall clear on its report channel.
- AC7 — `probe host` — a stub bar exiting 4 left `gates-green` UNMET printing
  `hold · host-degraded · until probe host · the runner exited HOST` and the `--hold` it names.
- AC9 — amended rev-8 — withdrawn with S11, as `TOOL-dDerivedDocket-61` deletes the lease bound
  it graded; rev-9 names what that unit carries of the property and what it does not.
- AC11 — `gate queue: acquired` — a stub bar that printed the acquire line and then hung past the
  same 3 s backstop left `gates-green` UNMET with "the merge bar did not answer within its 3s
  backstop (wall 1 + queue 1 + margin 1) and was killed after", and no `hold ·` line.
- AC12 — `GATE_WALL=7` — under `GATE_WALL="7"` the stub bar recorded `GATE_WALL=7` and the backstop
  read `wall 7`; under a blank wall, with `GATE_WALL=99` exported to the driver, it recorded
  `GATE_WALL=<unset>` and the driver printed the NOTE that the unattended bar runs under the gate
  runner's own profile wall.
- AC14 — amended rev-10 — `git cat-file -s` and `wc -l` read `memory/guides/UNATTENDED-PROTOCOL.md`
  at 64615 bytes and 704 lines at the parent and 64589 bytes and 704 lines at the build commit, and
  `tools/unattended/PROTOCOL.template.md` the same. In the template the row-anchored
  `^| .UNIT_STALL_BOUND. .*terms: absent takes the kit default and says so` counts 1 then 0 and
  `because the ceiling would fire first` 1 then 0, each moved passage counting 1 in
  `tools/unattended/README.md`. `UNIT_STALL_BOUND.*OPTIONAL, on` and
  `REVIEW_ROUNDS.*and so is a value at or above the runaway ceiling` each count 1 at the build
  commit, `GATE_PROFILE_CMD` counts 0 then 1, and `GATE_CMD.*GATE_WALL.*GATE_PROFILE_CMD` counts 1.
  The widened cell is 198 bytes against the row's 54, and the trims are 86 and 84. The protocol's
  line half, 704, is below `GUIDE_CAP_LINES`; its byte half is over `GUIDE_CAP_BYTES` at the parent
  already and carried by `memory/project/curation-debt.txt`, which is what rev-10 amended.
  `memory/guides/BUILD-METHOD.md` reads 27268 bytes and 349 lines, unchanged, below both guide caps
  and below its row in `tools/template-size-limits.txt`.
