# TOOL-dDerivedDocket-22 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-22

A `LANDING` record whose own commit the advertised tip holds now reads `LANDED`: the kit library's
`read_landing_commit` finds that commit by content, the driver's `read_derived_phase` tests it
against a quiet, once-per-process observation, and the leg's check 7 exclusion, fact-set arm and
grant arm read the same commit. In-place `--landed` observes and writes nothing to the tree; the
close freezes the roster and the asks; `--preflight` writes a derived record `LANDED` in a scratch
copy, names it from that copy, stages it, checks the blob and only then moves it. No merge bar, no
gate leg and no `*.test.sh` suite ran in this pass. What ran instead, from a scratch root outside
the tree:

- the driver-suite block this unit adds, behind a replica of that suite's own helpers — 87
  assertions, green — and RED under six staged breaks of the driver (no derivation at all, the lease
  row gone, `check_single_live` counting a derived record, the lander marker back to equality, the
  close writing no freeze, the pre-move stage removed) and one of the leg (check 19's terminal row
  taking no exclusion at a merge);
- the leg-suite additions, the same way over the ask block, the grant block and the shared fixture —
  40 assertions, green — and RED under eight staged breaks, one per arm class;
- existing arms re-run against the new code: the driver's `--landed` and lander-marker arms (61,
  green), and the leg's ask and grant blocks (93, green). The driver's rotation, HELD-lease and
  in-place blocks were run against both the new driver and HEAD's: three reds are inherited at HEAD
  (the phase-writer count reads 7, unit 4's unreachable-node history row, and the in-place
  could-not-commit arm), and the ABORTED rotation arms that are red at HEAD pass now.
- the new dating over the real tree, as a read: floored, `memory/builds/dUnstalledConvoy/RUN.md`
  moves from 2026-08-20 to 2026-08-24, past `LANDED_ANCHOR_CUTOFF`, and it is a terminal LANDED
  record with no anchor kind. So the anchor cutoff reads the unfloored `--follow` date and only the
  new fact-set arm floors; with its cutoff at 2026-09-21 that arm grades no record on this tree.

Found on the way and fixed, both logged in the spec's rev-7 line: `--preflight` refused every
rotation made under a new keepalive, and the driver suite's `iprun` helper ran `env` on a command
named `n`, so every in-place arm graded the driver's absence.

AC11 and AC13 carry `permission:` lines deferring them to the post-build run and get no line here,
and so does AC9's one reading over the real tree.

**Evidences:** TOOL-dDerivedDocket-22
- AC1 — `--status` — a committed LANDING pushed to the fixture's bare remote prints
  `phase LANDED (derived: <C8> on refs/heads/main at <C8>)`; merged into local main only it prints
  `phase LANDING (not on the remote: its landing commit … is not on refs/heads/main at …)`; and with
  an earlier LANDING commit of the path on the remote and the current one only staged it prints
  `phase LANDING (not on the remote: the LANDING record is not committed as it stands`. RED with the
  derivation removed.
- AC2 — `--status` — the lander stub pushes and is killed with `kill -9` before any marker, and
  `--status` still prints the derivation naming the pushed commit.
- AC3 — `asks-at-landing` — under in-place a real `--close` over a prepared merge commits a record
  carrying `units-at-landing: ARCH-tRun-1` and `asks-at-landing: EXMP-tRun-1=OPEN`; with the ask
  stub exiting 1 it refuses under code 77 with the record and HEAD unchanged; under primary the close
  stages a record carrying neither. RED with the close writing no freeze.
- AC4 — `--landed` — in-place, with the landing commit on the advertised tip, it exits 0, prints
  `observed, not written`, leaves `git status --porcelain` empty, makes no commit and is not refused
  as finished; merged into local main only it refuses under code 80 naming the LOCAL default branch;
  unpushed, and staged-not-committed, it refuses under code 80 with their own messages.
- AC5 — `--hold` — with `origin` pointed at a missing path, `--status` on a LANDING record exits 0
  and prints `the remote did not answer: origin`; `--hold` and `--abort` exit exactly as they do on a
  working record over the same remote, 0, with no `UNATTENDED check` line.
- AC6 — `landed-derived` — `--resume` on a derived-LANDED record prints nothing to resume and the
  stub's log stays empty; `--preflight` then writes it LANDED, and `git show :<archive>` reads
  `phase: LANDED`, the landing commit as witness and in `landed-derived:`, the index blob begins with
  the name's `blob8`, and `git diff --quiet` passes. The whole leg over that tree, after an owner
  `may:` commit after BASE, reports no check 4, 15 or 19 failure naming the archive; where the run's
  own commit wrote the grant, check 19 reds on the archive naming that commit. RED with the pre-move
  stage removed, and with check 19 taking no exclusion.
- AC7 — `--no-ff` — under primary, a marker naming the landing merge, the witness its second parent
  and the record commit already on the tip: `--landed` writes `phase: LANDED` with anchor remote; a
  marker naming a commit the remote does not advertise refuses on check 34. RED with equality.
- AC8 — `derived LANDED` — the leg counts a LANDING record whose witness is pushed and record commit
  is not (`2 concurrent`), and prints `check 7 EXCLUDED … — derived LANDED` once the record commit is
  pushed; `--preflight tOther` over the driver's fixture announces the record live, then excluded.
  RED with check 7 reading the witness, and with `check_single_live` counting a derived record.
- AC9 — `--follow` — over fixtures: a LANDED record first committed after `LANDED_FACTS_CUTOFF`
  without `units-at-landing` reds naming the fact; a pre-cutoff record rotated after the cutoff is
  graded by neither cutoff and dates 2026-01-01; a blank cutoff reports the arm OFF; and a live
  record in a rotated folder dates 2026-03-01, its own tenancy, while the anchor cutoff's unfloored
  reading of it stays 2026-01-01 and does not red it for naming no anchor kind. RED without
  `--follow` and without the floor. The `memory/builds/dCarriedReceipt/RUN.md` reading is deferred.
- AC10 — amended rev-7 — the ban's token follows S1's rename to `read_landing_commit` (section 9,
  rev-7); the grep over `tools/memory-tree/gen_build_index.py` prints 0 at the build commit.
- AC12 — `LANDED_FACTS_CUTOFF` — under primary, a derived-LANDED record first committed after a
  2000-01-01 cutoff and lacking `units-at-landing` is refused under code 81 naming `--landed tRun`,
  with the record, the tree and the archive set unchanged; with a 2999-01-01 cutoff it rotates.
- AC14 — `asks-at-landing:` — in the ask fixture under in-place, a committed LANDING carrying
  `asks:` and no freeze reds check 15 naming the record; under primary it does not, and with the
  freeze present it passes. RED with the arm grading LANDED alone.
- AC15 — `released <iso> landed` — in-place `--landed` leaves the lease reading
  `released <iso> landed` over a clean tree; with `origin` missing and the record commit dated 2020,
  `--status` names the observation and prints no `presumed-stopped`, and
  `--resume --keepalive-id C` prints nothing to resume, writes nothing and never calls the lander.
  RED with the lease row removed.
- AC16 — `LANDER_MODE=in-place` — a hand-committed LANDING with no roster reds as population
  `landing` and the count line reads `committed LANDING 1`; with no graded record it reads 0 and says
  so; under primary the pushed record is reported naming `--landed tRun` and not graded.
- AC17 — `may:` — a derived-LANDED in-place record over a prepared merge whose first parent carries
  the owner's grant reds only on the run's own grant; under primary, after a plain mid-run reconcile,
  the run's earlier grant reds and the owner's does not. RED with the record read as live.
- AC18 — `landed-derived` — a `RUN.LANDED.` record whose witness is on the tip and whose
  `landed-derived` names a commit the tip lacks reds check 15 naming both; naming a commit on the tip
  passes. RED with the evidence accepted untested.
- AC19 — `GUIDE_CAP_BYTES` — `git cat-file -s` and `wc -l` read the protocol and its template at
  59634 bytes and 670 lines on the parent and 59228 and 666 at the build commit, under 61440 and 750;
  the two trimmed phrases count 1 then 0 and sit in `tools/unattended/README.md`; both rules still
  read in section 2; `LANDED_FACTS_CUTOFF` counts 0 then 1; the stops guide reads 28366 bytes and 432
  lines; gross growth is 298 bytes.
