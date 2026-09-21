# TOOL-dDerivedDocket-49 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-49

The `next:` line comes off a declared five-rung ladder instead of three guarded assignments spread
across two loops. No merge bar, no gate leg and no `*.test.sh` suite was run in this pass. The
direct check was the DRIVER itself, run over four scratch fixture repositories built under this
run's scratch root, and compared line for line against the same driver at this unit's parent commit;
the source-level arms were evaluated against a scratch copy of the driver. Every arm was observed
RED against a staged break before it was allowed to pass — eight breaks, twenty observations, listed
under the criteria they belong to.

AC8 carries a `permission:` line deferring its suite run and the `harness arms` leg to the bar the
main loop runs after the last unit is terminal. Its `ARMS_FLOORS` half is answered here, because it
is a measurement over source and not a run.

Two criteria moved in rev-2, which was written before the code as the brief requires, and the
revision log says why each one did.

**Evidences:** TOOL-dDerivedDocket-49
- AC1 — `derive_next_shape` — over a scratch fixture holding one READY unit and nothing else, the
  patched driver's whole `--plan` output is byte-identical to the same run against the parent
  driver, and the same holds over all four fixtures this pass built, including the two that print a
  MISSING shape and the one that grades nothing. The source arm reads the driver with full-line
  comments dropped and finds no `|| next=` left in code, and exactly one line calling the selector.
  Staged RED twice: restoring one guarded assignment to `next` in the live-unit branch takes the
  first arm to 1, and deleting the single call site takes the second to 0.
- AC2 — `EXMP-tRun-2` — over a fixture whose roster names that id with no tracked spec while its
  one tracked spec is CLOSED, `--plan` prints `next: EXMP-tRun-2 (MISSING - spec it first)`; with
  that one roster row removed and nothing else changed, the same run prints
  `next: none - every tracked spec is terminal`. Both runs match the parent driver byte for byte.
  Staged RED two ways: the terminal rung promoted to rung 1, and the MISSING rung deleted outright —
  each prints the terminal wording over a build with a planned unit nobody has specced.
- AC3 — `--plan` — over a fixture holding a READY unit and a roster id with no spec, the line reads
  `next: ARCH-tPlan-1 (READY - build it)`, the MISSING id keeps its own row, and the id never
  reaches the line. Staged RED two ways: the MISSING rung moved above the live-unit rung, and the
  terminal rung promoted to rung 1.
- AC4 — `--plan` — over a fixture whose only spec carries an indented status header and whose units
  region is empty, the run prints a `NOT A UNIT (no status header)` row and
  `next: none - no tracked spec grades as a unit (see the NOT A UNIT rows above)`, never the
  terminal wording. Staged RED by collapsing the nothing-graded rung's shape onto the terminal one,
  which is exactly the state leg check 30 exists to catch.
- AC5 — `tools/unattended/unattended.sh` — the declared block read back out of the driver's source
  gives five `rung ` lines at column 0, in the order live-unit, missing-unit, undecided-ask,
  nothing-graded, everything-terminal. The undecided-ask rung is third, after both unit rungs and
  before both terminal ones. Staged RED exactly as the criterion's own Red-when asks: the ask rung
  moved above the MISSING rung, which takes both the rung-2 and the rung-3 assertions red at once.
  A second break, the MISSING rung moved above the live-unit rung, reds the rung-1 assertion.
- AC6 — `git cat-file -p` — the three shape literals are byte-identical between this commit and its
  parent, each now a whole line of the rung table rather than the tail of an `echo`. The terminal
  wording is present verbatim, once, as its own line; so is the nothing-graded wording. Staged RED
  by re-punctuating the terminal literal with a trailing full stop, which reds the source arm and
  also stops the existing runtime assertion hitting. The criterion's second clause was AMENDED at
  rev-2 — the string it named was the printed line with its `next: ` prefix, which the refactor
  moves to one print site — and the revision log's rev-2 entry logs it.
- AC7 — `git cat-file -s` — `memory/map/features/unattended.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` are byte-equal
  and line-equal at this commit and at its parent, at 20467 B / 274 lines and 60036 B / 673 lines
  twice over, because this unit opens none of them. The criterion's pinned headroom figure was
  AMENDED in rev-2 rather than re-cited: it fell from 93 B at the base to 13 B at this parent,
  spent by units that landed in between. It moves no verdict here and would have moved one for any
  unit that wrote a dossier byte.
- AC8 — amended rev-2 — the criterion asks that the `ARMS_FLOORS` pair for
  `tools/unattended/unattended.sh` name a new count, and it does not move. That gate counts
  `fail <n> "` call sites; measured at 256 at this commit and 256 at its parent, because the ladder
  adds no refusal at all and `.memory-tree.conf` therefore left the write set unwritten. What DID
  move is the suite's own executed-assertion floor, raised by the 26 assertions the new arms add,
  all of them in region two, so `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` each carry +26 and
  `FLOOR_SHARD_1` is untouched; the count is derived from the block's own assertion lines, never
  from a suite run this pass may not make. Each of those arms was observed RED by hand against a
  staged break, which is the direct check the criterion names. The suite run and the
  `harness arms (fail branches armed or pinned)` leg are deferred by the criterion's own
  `permission:` line.
- AC9 — `git show` — `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md`
  read at this commit: AC18's first run asserts `next:` reads the MISSING shape naming `-2` while a
  unit shape remains, a second arm over the same fixture with both MISSING units retired asserts the
  flip to the UNDECIDED shape naming the earlier-listed mandated ask, and that spec's revision log
  carries the entry naming AC18 and this unit. The rung order this unit pins therefore has a failing
  case in the spec that consumes it, and a later re-fold of AC18 cannot re-open it silently.
