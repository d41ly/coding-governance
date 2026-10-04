# TOOL-dUnstuckLanding-27 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-27

No merge bar and no self-test suite ran in this pass. The criteria were observed through two
hermetic probes assembled from the suites' own setup. The first was the brief-recorded suite's
prologue, its RANGE fixture helpers and the new RANGE arm. The second was the driver suite's
prologue, the settle block's fixture with its AC6 arms and the new S2 arms, and the landing-node
block's fixture with the new S3 arms. Each built its repositories and bare origins under the user
temp directory. Against the fixed code the first probe passed its 4 assertions and the second its 44.
Against the code at the unit's start, the first redded 3 of 4: the leg exited 1 and named the repair
as a briefless build. The second redded the AC2 and AC4 arms: the fresh leased record was settled as
abandoned, no `gates-staged` fact was written, and the hand-off failed 83 with `the bar it names ran
at`. Two staged mutations redded the rest. One admitted no UNBOUND record at all, and the AC6 legacy
arm and the stale leased arm went red. The other excluded the whole build folder, and the AC5 arm went
red. The suites themselves are owed to the close.

**Evidences:** TOOL-dUnstuckLanding-27
- AC1 — `built before its run` — a RANGE fixture whose run 2 is based at the advertised tip carried
  ARCH-tBR-1's build commit, with its brief row, behind the base and a `fix(tBR): ARCH-tBR-1` repair
  in range with no row. The leg exited 0, its summary named the range, it printed `ARCH-tBR-1 was
  built before its run`, and it never printed `ARCH-tBR-1 — BUILT at`. The code at the unit's start
  exited 1 and named the repair.
- AC2 — `--settle` — a record leased with `session: absent` and a lease-utc of now
  read `verdict: UNBOUND`. `--settle` printed fail 101's new text, which names `the lease written at`
  and reads `stale no and pid-alive`, and the record's blob was unchanged. The code at the unit's
  start wrote `abandoned`.
- AC3 — `lease-utc` — AC6's record with no `lease-utc` fact, which reads UNBOUND, still settled as
  abandoned with `work-landed-at`. The same leased, session-absent record committed in 2000, with
  no gate log, also settled. Both went red under the mutation that refused every UNBOUND record.
- AC4 — `--handoff --code owner-landing` — a hand-off node, `primary`, ran a stub bar that writes an
  all-INHERITED red record and the leg's manifest at the tip, with an ask generator that reads
  ARCH-tLn-2 back OPEN.
  `--close` filed ARCH-tLn-2 into the build's BACKLOG.md and failed 105. The `gates-staged` fact
  opened with the record and named the BACKLOG.md, and every staged path was in that set. After the
  commit, `--handoff --code owner-landing` printed `phase HELD · code owner-landing · until owner`.
  The code at the unit's start failed 83 with `the bar it names ran at`.
- AC5 — `--handoff --code owner-landing` — the same close, followed by an edit to the build's
  `spec/one.md` committed with the staged records, made the same hand-off fail 83 with `the bar it names ran at`, and no HELD
  phase was written. The mutation that excluded the whole build folder admitted it. A forged set
  naming the folder by a wildcard and by a `..` segment still failed 83. The first commit of this
  unit admitted it, because its tie globbed the set in the shell and handed git a glob pathspec, and
  each of the two hardenings is load-bearing on its own.
