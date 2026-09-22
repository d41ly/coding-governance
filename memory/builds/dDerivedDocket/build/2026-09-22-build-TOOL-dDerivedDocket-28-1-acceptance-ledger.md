# TOOL-dDerivedDocket-28 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-28

The run-owned process ledger is built. `run_bounded` starts its command in the background under a
wrapper whose `$0` is the repository root, records it by identity in `<slug>.procs` beside the lease,
and waits for it. One classifier reads a record back as gone, reused, live, orphan or untokened, and
every reader asks it: the reap `--preflight`, `gates-green`, `--hold` and the two lease-holding
`--resume` rows make through `PROCMON_CMD --kill-msys`, the `orphans <n>` field on `--status`, the
`--hold` refusal 84 over a live recorded process, and the removal at `--abort`, a primary `--landed`
and an in-place `--landed` observation. The stops companion gains section 14 and the Skill a bullet
stating that a process not in the ledger is never killed, graded by the kit leg's new check 41. The
protocol's key table gains `PROCMON_CMD`, funded by moving the `BRIEF_RECORDED_CUTOFF` argument to
the kit README, and gov declares process-monitor's reaper. The spec moved to rev-9 for AC13's
ceiling on the protocol, which is already over its guide cap at this unit's parent.

No merge bar, no gate leg and no `*.test.sh` suite ran in this pass. The driver suite's new block ran
by hand behind a replica of that suite's prologue, from the scratch root, over its own fixture: 59
assertions, all green, with AC1's arm run through the REAL process-monitor reaper and its fence, and
green again as extracted back out of the suite after insertion. The derived-terminal block, through
the in-place `--landed` arm that carries AC12's second half, ran the same way: 15 assertions, green.
Both ran once more against staged breaks of the driver, one per `Red when:` clause, and every break
reddened the arms written for it:

- the pid alone as the identity: AC3 and AC8 red, the reused and the untokened pid reaped;
- a blank reaper falling back to `kill`: AC4 red;
- `--status` reaping: AC5 and AC9 red, the ledger rewritten by a read verb;
- `--hold` holding over a running bar: AC6 red, a HELD record written over it;
- only `--resume` reaping: all three AC11 arms red;
- a refusal row reaping: AC9 red, the ledger rewritten and the orphan killed;
- no removal at `--abort`, and removal ignoring a live record: the two AC12 arms red;
- no removal at the in-place `--landed` observation: the derived-terminal block's AC12 arm red;
- the wrapper without the root token: AC1 red, the reaper answering `REFUSED — winpid … is not in
  scope` for a tree whose parent is gone.

One inherited defect was found on the seam this unit changes and repaired in the same file: the
driver suite's first `run_bounded` harness sourced the function without assigning the lease pair it
reads, so under `set -u` the suite died silently at that harness's first call, before its floor
check and with no FAIL or PASS line. Reproduced against the driver at this unit's parent.

Check 41's block, sliced out of the shipped leg, read green over the kit, red naming the file for
each carrier with the sentence reworded, green over the sentence wrapped across two lines, and
announced an absent carrier on the report channel.

AC1, AC7 and AC10 carry `permission:` lines deferring them to VERIFYING, so none of them gets a line
here. AC1 was nonetheless exercised by the block above; its line is the orchestrator's.

**Evidences:** TOOL-dDerivedDocket-28
- AC2 — `--status` — a sleeper whose parent subshell had exited, recorded nowhere, was alive after
  `--status` printed `orphans 1` for the one RECORDED orphan beside it and after the holder's
  `--resume` reaped that orphan; the stub reaper's log never named the stray pid, and a second
  `--status` printed no `orphans` field at all.
- AC3 — `exited, pid reused` — a record naming a live sleeper under a start token of `1` printed
  `NOT reaped <pid> — exited, pid reused` at the holder's `--resume`; the sleeper was alive after,
  the stub reaper was never called, and the record was gone from the ledger.
- AC4 — `PROCMON_CMD` — declared blank, the holder's `--resume` over a killed driver's orphan printed
  `reaping is OFF because PROCMON_CMD is blank, so 1 orphan(s) of tRun are counted and left
  running: <pid>` and `orphans 1`; the orphan was alive after and no reaper was reached.
- AC5 — `orphans 1` — `--status` over one live orphan printed `· orphans 1`, the orphan was alive
  after, and the ledger was byte-unchanged.
- AC6 — `--hold` — with a recorded `sleep 63` alive under a live driver, `--hold` refused as check 84
  naming `<pid> (sleep 63)`, left the run-state file byte-unchanged and reached no reaper; after the
  sleeper exited, the same `--hold` printed `phase HELD · code platform-limit`.
- AC8 — `--resume` — with the procfs seam pointed at a directory that does not exist, the killed
  driver's record carried `-` in both token fields; the holder's `--resume` printed
  `NOT reaped <pid> — no procfs token` and `orphans 1`, the orphan was alive after, and the stub
  reaper was never called.
- AC9 — `--resume --keepalive-id B` — over a fresh lease held by k1 and a live orphan, the no-id
  `--resume` refused as check 59 after its status block counted `orphans 1`, and
  `--resume --keepalive-id kB` refused as check 58; the ledger and the lease were byte-unchanged,
  the orphan was alive and no reaper was called.
- AC11 — `gates-green` — after a driver was killed mid-command, `--close` logged `reap <pid>` BEFORE
  `bar` in the stub bar's own log; a same-id `--preflight` printed `reaped orphan <pid>` and
  `preflight OK`; `--hold` printed `reaped orphan <pid>` and `phase HELD`. After each, the orphan
  was gone and a record planted for an already-exited pid was gone from the ledger.
- AC12 — `--abort` — over a ledger holding one exited record, asserted present first, `--abort`
  printed `phase ABORTED` and the ledger was gone; over one naming a live `sleep 67` under a live
  driver it printed `the process ledger is KEPT … <pid> (sleep 67)` and the file remained. The
  in-place half rode the derived-terminal block's `--landed` arm: a ledger asserted present before
  the observation was gone after it.
- AC13 — amended rev-9 — `git cat-file -s` reads `memory/guides/UNATTENDED-PROTOCOL.md` at 64719
  bytes and 704 lines at the parent and 64615 bytes and 704 lines at the build commit, and
  `tools/unattended/PROTOCOL.template.md` the same; `grep -c 'unlike the sibling above'` counts 1
  then 0 with the moved text in `tools/unattended/README.md`, and `grep -c 'PROCMON_CMD'` counts 0
  then 1. `UNATTENDED-STOPS.md` reads 35330 bytes and 530 lines and `memory/guides/BUILD-METHOD.md`
  27268 bytes and 349 lines, unchanged, each below `GUIDE_CAP_BYTES` and `GUIDE_CAP_LINES` as
  `tools/memory-tree/check-memory-hygiene.sh` declares them, and BUILD-METHOD below its 27648-byte
  row. The protocol is over the guide byte cap at the parent already, grandfathered by
  `memory/project/curation-debt.txt`, which is what rev-9 amended; §9 records it.
