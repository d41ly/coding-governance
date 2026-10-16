# TOOL-dRedressedBar-18 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-18

Written by TOOL-dRedressedBar-27 on 2026-10-16, after the unit closed with no ledger, from what its
builders recorded. Nothing was re-run for it. This build's `-1-` record for unit 18 is the
set-aside work of its first build, which diverged. The unit was then built against spec 18 rev-4
in two commits: the pass commit `6783992aa`, which restored the set-aside code verbatim and
changed it only where rev-4 requires, and `997fc294f`, which renamed four nested helpers and
re-ran the serial and concurrent fixture manifests with the same readings. The readings below are
the rev-4 builder's, from those commits' bodies and from its return in
`2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`, under the heading
`2026-10-14T22:31:47 · gov-builder · wf_0e7a57a1-02c/acf19d67f5fb8f3f3` at line 5556, collected
into that record by TOOL-dRedressedBar-27. AC8's reading is the first build's, under the heading
`2026-10-14T21:36:47 · gov-builder · wf_2e958a62-4b6/af9e8721f060c270a` at line 5496. Every
reading is a direct run of the tool on node d or a probe of its code. No merge bar, no self-test
suite and no gate leg ran in the build pass, and the full `--selftest` run was owed to the close.

Spec 18's rev-5 to rev-8 are records fixes. Of them, only rev-7 moved criterion text, in AC1, AC2
and AC5, and it says "Unit 18 built against its criteria as written". Those three lines are
AMENDED and carry the rev-4 reading. AC15 was never observed, and spec 18's rev-9 records that.

**Evidences:** TOOL-dRedressedBar-18
- AC1 — amended rev-7 — spec 18's rev-7 entry, a records fix for TOOL-dRedressedBar-22, rewrote
  this criterion after the build: its resolution red half now says `TOOL-dRedressedBar-22` first
  read both legs at verdict `ok` (its AC15). The rev-4 reading, from the return's table: on the
  serial fixture run, `spawn six` 8 less `spawn none` 2 read 6, under the interpreter
  `C:/Users/d41ly/AppData/Local/Python/pythoncore-3.14-64/python.exe`, and the spawn leg held 6
  child rows, each with every field. With the resolution disabled the difference read 0. With the
  breakaway staged, the run refused with exit 2 naming the interpreter, and with the verification
  also skipped the difference read 0.
- AC2 — amended rev-7 — spec 18's rev-7 entry rewrote this criterion after the build: its
  resolution red half now says `TOOL-dRedressedBar-22` first read memio's verdict and its
  `memio: wrote 200 MiB` line (its AC15). The rev-4 reading, from the return's table: the memio
  leg's `peak_job_mem_b` read 225 MB and its `write_bytes` 209715204, and `spawn_s_est` matched
  its formula. With the resolution disabled, `peak_job_mem_b` read 6963200 and `write_bytes` 0.
  The rev-4 table gives no reading of the `extract_runner_function` red half; the first build's
  return says the extraction refusal held.
- AC3 — `census.FIELDS` — unchanged. The row carried `peak_mem_b` and `mem_b` as ints and its
  `command` intact, the POSIX rows read None, and the red staging read `'300'`.
- AC4 — `concurrent.json` — on the concurrent fixture run no admission sat above 80% CPU while a
  leg ran, and the cap was exercised.
- AC5 — amended rev-7 — spec 18's rev-7 entry rewrote this criterion after the build: it names the
  widened call `check_admit(mode, pending, running, cpu, mem, fresh)` and a loop half, both
  `TOOL-dRedressedBar-22`'s (its AC6). The rev-4 reading, over the five rows as rev-4 wrote them:
  `check_admit` returned hold, admit, hold, hold and admit.
- AC6 — `sleep` — the stall leg held 1 episode with `sleep` in its tree, the steady leg held none,
  and every leg's rc read 0.
- AC7 — `churn.py` — the churn leg held no episode, and 5 of its windows were decided by the job
  veto.
- AC8 — `measure_foreign` — the first build's parity probe: the runner's own `measure_foreign`,
  with `ps` shimmed, and the port both gave 2 roots, `200:lib9/runner.sh` and
  `300:probe/two/selftest.py`, and the port without the `selftest.py` rule gave 1. The rev-4 return
  says that code is unchanged from the set-aside build and was not re-run, and `6783992aa`
  restored the set-aside code verbatim.
- AC9 — `serial.json` — the return's table reads AC9 as holding on the serial fixture run, and
  gives no finer reading.
- AC10 — `envelope.json` — the return's table reads AC10 as holding on the same serial run: the run
  dir held the records the criterion lists.
- AC11 — `printenv.py` — the return's table reads AC11 as holding on the same serial run, whose
  `printenv.py` leg carries the planted credential.
- AC12 — `linux` — `resolve_job_backend` refused, naming `linux` and the Job Object API.
- AC13 — `measure-legs selftest` — all four declaration files carry the leg, with equal name,
  subject and argv.
- AC14 — `help/measure-legs.md` — the run-gates marker pair read an equal 1.41, the process-monitor
  markers all read 0.19, and the help page carries every required token.
- AC15 — amended rev-9 — NOT OBSERVED. Spec 18's rev-9 entry records that this criterion was never
  observed. The rev-4 return says "the turnstile arm runs the real runner's hold verb, so I did not
  run it", and owes it at the close with "the full `--selftest` run", which no pass may run. No
  record of this build observes it since. Never observed: `<ml> --selftest`'s turnstile arm and
  `queued.sh`'s `ts_wait_s`.
- AC16 — `check_app_alias` — it returned True for the alias and False for its own interpreter and
  for a missing path. The `SUBSTITUTED` line printed, and the `substitutions` entry, its `applied`,
  the probe's counts 3 and 2, and `GOV_PYTHON` in the log all held. With an `islink` test staged,
  the run refused with exit 2, naming `python3`.
- AC17 — `scratch_posix` — on AC1's run both converted spellings start with a drive letter,
  `scratch` is a directory, and both posix spellings start with `/`. With the bash spelling
  printed, the run refused, naming the scratch dir. The half on AC15's run is owed: the return says
  "Neither half of AC17 on AC15's run was observed either".
