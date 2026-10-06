# Acceptance ledger — TOOL-aGraftedHelix-5

**Serves:** journal TOOL-aGraftedHelix-5

Node `a`, 2026-10-05. The build commit is `4f689c124`, over the spec's rev-5 commit `280e70131`;
`ff4f21845` follows it with one more arm, for S2's override refusal, and a control on AC14. Three
spec revisions preceded the code: rev-3 (the runner as merged from origin/main at `909c5e0b9`, one
write per sample, AC2 and AC5 made able to fail), rev-4 (`cleanup` stops the turnstile ticker, AC14)
and rev-5 (AC4 with the wall off). No merge bar and no self-test suite ran in this pass. Every
criterion below was observed through slices of `run-gates.evidence.test.sh` assembled under
`tools/run-gates/` (the suite's prologue, its run-record helpers and the census blocks), with
`TMPDIR` on a short `%TEMP%` root, and deleted after each run. The full slice printed 25 ok lines
against the build commit's tree, then 2 more for the follow-up's arms, and a slice of the existing
ceiling-admission block printed 40 assertions green over the eighth-field fixture rows. Each new arm
was then observed red against a staged break in the working tree, restored byte-for-byte from a
scratchpad copy and compared with `cmp` after every run. The whole suite is the main loop's at
VERIFYING; its floor rose 84 -> 110.

**Evidences:** TOOL-aGraftedHelix-5
- AC1 — `foreign` — a fixture bar over a 5 s `fx/load.sh` leg, with an outside `exec bash fx/load.sh 120` alive, wrote
  the leg's eighth field as 1 or 2 across runs and a census root `<outside pid>:fx/load.sh`. With the
  token match deleted from `measure_foreign` the field read 0 and no line named the outside pid.
- AC2 — `GATE_CENSUS_EVERY=1` — through a `bash -c` wrapper naming the runner's path, with a leg running nest.sh and a nested
  nest.sh, the census took 7 samples and no root was the wrapper's, runner's, leg's or nested pid.
  With the ancestor walk deleted, the wrapper's pid was a root and the arm redded.
- AC3 — `run-gates: NOTE` — with a `ps` stub exiting 1, one printing no PID or PPID column, and one omitting the runner,
  every `.leg` row read `unknown` and the verdict line equalled the stub-free run's; under the failing
  stub every census line read `unknown` and stderr carried exactly one NOTE naming the census. With
  the observer test deleted, the third stub's rows read 1.
- AC4 — `GATE_WALL=0` — at `GATE_JOBS=1` both legs reported and the capture returned 0 to 1 s after the verdict's `ended`
  stamp; with the wall on the same fixture returned 28 s after it, the wall watcher's own poll, which
  is why rev-5 turned it off. With the sampler's `disown` deleted the runner wrote no verdict inside
  the arm's 240 s bound and the capture returned at 243 s.
- AC5 — `GATE_CENSUS_EVERY=2` — over a leg that touched `.git/cn-started` then slept 15 s, with an outside 8 s load started on
  that marker, the census held 8 lines, a line after the first named the outside pid and the leg's
  field read 1 or 2. With the loop's sample replaced by a no-op the census held 1 line and redded.
- AC6 — `gate-ledger.tsv` — after a two-leg bar `awk -F'\t' 'NF != 5'` printed nothing over its two rows. With the
  ledger read's trailing `_` deleted, the key absorbed the eighth field and the arm redded.
- AC7 — `# set aside:` — `derive-ceilings.py --report` over L at 10 s/0, 50 s/2, 60 s/unknown, 70 s with seven fields and
  M at 30 s/1 printed `L 10.0 1 100 90 120 UNDER 3`, `# set aside: 2 contended, 2 uncensused`, and M on
  the SET ASIDE line and not the UNBACKED one. With the census filter disabled L read 70.0 from 4.
- AC8 — `2 contended` — `--write` over that fixture held L's row at 40.0 and its summary read `set aside 2 contended, 2
  uncensused reading(s)`; over M's reading alone it exited 0 with no DEAD PROBE and every row
  byte-identical; over no reading it exited 2 with DEAD PROBE. With the liveness test reading the
  admitted map alone, the M-only fixture exited 2 with DEAD PROBE and the arm redded.
- AC9 — `tools/run-gates/ceiling-evidence.txt` — its header equals the one `--write` renders: the tracked file was re-rendered by one
  `--write` over a copy whose only reading was a seven-field row, every one of its 119 rows
  byte-identical, and `grep -n 'foreign' tools/run-gates/README.md` names the run-record section's
  field list `name · status · rc · seconds · started · ended · key · foreign`.
- AC10 — `bash tools/check-kit-versions.sh` — at `4f689c124` it printed `kit-versions: clean — 16 declared carrier(s) under tools/`;
  `python tools/govkit/govkit.py epoch --base 5bdfb0455` printed `epoch: run-gates · clean · 1.25`, and
  `bash skills/session-kickoff/manifest-check.sh` exited 0 with no check 5 line; run-gates moved
  1.24 -> 1.25 in its two carriers and the manifest's `last-audit` was re-stamped in that commit.
- AC11 — `GATE_CENSUS_EVERY` — left at 60, at width 2, two `peek.sh` legs each found the census file already written when
  they started, under a `ps` that sleeps 2 s, carried numeric `foreign` fields, and started no earlier
  than its first stamp; no census NOTE was printed. With the first sample moved into the detached loop
  both legs found it unwritten, both fields read `unknown` and a NOTE printed, red on two runs of two.
- AC12 — `.retry.leg` — the canary's spinner and contended pair passed on the serial retry, and `1.retry.leg` held eight
  fields with a census verdict in the eighth; with its field emptied on retries the arm redded.
  `derive_foreign`, sliced out of the runner, read `2 0 unknown 2` for an unknown and a 2, zeros, an
  unknown and a 0, and a sample 15 s before the leg; with `unknown` ranked first it read
  `unknown 0 unknown 2`, and with the reach set to zero it read `2 0 0 unknown`.
- AC13 — `--observed` — `--write --observed 'L=55' --how 'quiet host, no other session'` exited 0 and wrote L at 55.0 with
  that text as its source, and the header it rendered says an `--observed` reading is admitted
  uncensused; the README's ceiling section names the route under TOOL-cMendedVintage-17. With that
  README sentence's clause deleted the arm redded.
- AC14 — `ps -ef` — two seconds after a fixture bar with the turnstile held exited, no process line named its runner
  path; before rev-4 the first fixture bar's ticker, pid 1907364, was still listed with parent 1 and
  a `sleep 300` child. With `ts_tick_stop` deleted from `cleanup` the arm redded.
