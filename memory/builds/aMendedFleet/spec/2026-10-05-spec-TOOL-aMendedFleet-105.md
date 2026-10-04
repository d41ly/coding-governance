# TOOL-aMendedFleet-105 — the reaper's verification settles, so a member dying as it is signalled is not a survivor

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-1 · base 34a99ad1 · streams tooling · ratified 2026-10-05 · order 106

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The held `process-monitor census selftest` reds on the daily remote CI job in two of the three
census runs, always in one arm, `test_live_tree_dies_completely`, and always the same way: one walked
member answers `kill: <msys pid>: Permission denied` to the reaper's MSYS signal and is still listed
by the single census re-read that follows. The held-red census filed this as cause C9, class host.
It is not host-only: node a hit the same tuple once in six runs on 2026-09-17, recorded in the
`cMendedVintage` unit 11 acceptance ledger and left unattributed there. The cause is a race the
reaper already half-handles. Killing leaves first cascades, so a shell whose foreground child just
died is exiting on its own when the walk reaches it; the MSYS signal to an exiting process is
refused, and the one immediate re-read still lists it. This unit makes `tools/process-monitor/reap.py`
re-read until the kill set is gone or a bounded deadline passes, and counts a refused signal on a
member that settled re-read shows gone as already gone, which is how the reaper already counts a
cascade death.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/reap.py` gains `check_settled_survivors(report, backend, deadline_s)`
  and a module constant `SETTLE_S`. It re-reads the census through `census.scan_processes` and
  grades each read with the existing `check_survivors`, stopping when `survivors` is empty or the
  deadline has passed. It records the number of reads it took as `report["rereads"]`. After the last
  read, an entry of `errors` whose winpid is in `killed` moves to `already_gone`. An entry whose row
  is still present stays in `errors`, and that row stays in `survivors`. `check_survivors` itself is
  unchanged, so the fixture arm that calls it with a literal rescan keeps its meaning.
  Observed by AC1, AC2.
  **Readers:** by name: `render_kill` and `test_live_tree_dies_completely` spell the `errors` field,
  and `render_kill` spells `already_gone`. by value: `render_kill` counts and prints both lists, and
  `test_live_tree_dies_completely` asserts `errors` is empty; no other tracked file reads either
  field, by `grep -rn` over `tools/` at base.
- **S2** — The three places that verify a real kill call `check_settled_survivors` instead of one
  `census.scan_processes` read followed by `check_survivors`: `run_sweep` and the `--kill` path of
  `main` in `reap.py`, and `test_live_tree_dies_completely` in `tools/process-monitor/selftest.py`.
  The dry-run branches stay as they are. Observed by AC3, AC4.
- **S3** — `render_kill` prints the read count on its `killed` line, and the live arm's
  `walked` line prints it too, beside the command of every member left in `survivors` or `errors`.
  A future red then names its member and shows the settle ran. Observed by AC1, AC4.
- **S4** — `tools/process-monitor/selftest.py` gains two fixture arms, one per outcome of S1: a
  member listed by the first read and gone at the second, carrying a refused-signal error; and a
  member listed by every read until the deadline, carrying the same error. Observed by AC1, AC2.
- **S5** — `tools/process-monitor/README.md` gains the measurement under "Why it is not simpler than
  it looks", and that section's lead sentence stops counting its bullets. NOT OBSERVED by an
  acceptance criterion: a prose bullet has no behaviour to observe, and the close's README re-read
  (BUILD-METHOD M8) is what reads it against the code.

## 3. Non-goals (OUT)

- A native fallback that re-signals a refused member through `taskkill /PID <winpid> /F`. That is the
  fix for a member the MSYS signal can NEVER reach, and §8 F1 records why the evidence refutes that
  reading. It would also not fix this race: Windows refuses `TerminateProcess` on a process already
  terminating, so the fallback answers access denied for the same member. UNVERIFIED on the runner;
  the README of this kit records the opposite case, a native process MSYS cannot see at all, which
  the reaper already routes to `taskkill` before signalling.
- Changing the arm's expected tuple, its staged tree, its four member predicates or its cleanup probe.
  The arm is right to demand no survivors and no signal errors; the reaper was wrong to report them.
- A retry of the MSYS signal itself. A re-signal of an exiting process is refused again, and a second
  signal to a live one is what the settled re-read exists to make unnecessary.
- Moving the process-monitor kit version. The build moves every kit version it owes once, after the
  last pass that touches that kit, and the close's `kit epoch` leg grades that move.
- Every other held-red cause, C1 to C8, which units 97 to 104 own.
- The `aReapedSpinner` closing review's finding D9, an unsignalable row counted killed when it exits
  on its own. S1's reclassification reads `errors` only and leaves `unsignalable` as it finds it.

### Edges

- **hands-off** external — if the first scheduled runs after landing still red this arm with the
  member S3 names present past the deadline, the never-reachable reading of §8 F1 has become live,
  and the native fallback above is the next unit's mechanism, filed by whoever reads that run.

## 4. Design

### Evidence

Read at base `34a99ad1`. Every byte of `tools/process-monitor/reap.py` and
`tools/process-monitor/selftest.py` other than the kit-version marker is the same at the three
census heads, `4e0057a76`, `a587e82dc` and `c2ffcf878`; the only commits touching
`tools/process-monitor/` since the earliest of them are the `aHalvedInstall` kit-version moves.

- Runs `37114721791` and `36996269983`, read with `gh run view --log-failed`: the arm printed
  `walked 7 through C:\Program Files\Git\usr\bin\bash.EXE` and named all four staged members, then
  failed with `([], [2612], [(2612, 1, 'kill: 1197: Permission denied')])` and
  `([], [8828], [(8828, 1, 'kill: 265: Permission denied')])`. The cleanup probe found no stray.
- Run `37196051126`'s job `111418323033`, read with `gh run view --job ... --log`: the same walk of 7
  through the same launcher, the same four members, and the arm green.
- The `cMendedVintage` unit 11 acceptance ledger records the tuple
  `([], [28548], [(28548, 1, 'kill: 1128596: Permission denied')])` on node a, on the first of six
  runs at one revision, the other five clean. 1128596 is below `MSYS_SYNTHETIC_BIT` in
  `tools/process-monitor/census.py`, so that member was a real MSYS process, as 1197 and 265 are.
- `run_kill` probes each row with `kill -0` and then signals it with `kill -9`, so the refused member
  answered the probe and refused the signal a moment later.
- `run_kill`'s own comment records the cascade: killing leaves first, a member's descendants are
  gone before the walk reaches it, which is why `No such process` already lands in `already_gone`.
  The staged tree's two shells each run a foreground `sleep`, so each exits on its own when that
  `sleep` is killed, and the walk reaches each shell after its `sleep`.
- `run_sweep`, the `--kill` path of `main`, and the live arm each read the census ONCE after
  signalling. A process that has exited but whose handle its MSYS parent still holds can remain in
  that read; UNVERIFIED which of the two Windows reads, the CIM query or `ps -W`, kept 2612 listed.

### Mechanism

`check_settled_survivors` is a loop around two existing functions and adds no signal. Each pass calls
`census.scan_processes(backend)` and hands the rows to `check_survivors`, which already derives
`survivors` and `killed` from the kill set. The loop ends on the first read with no survivor, or on
the first read finishing past `SETTLE_S`, so it always reads at least once and the old behaviour is
the deadline-zero case. Between reads it sleeps a fraction of a second; one census read on Windows
spawns a PowerShell CIM query and a `ps -W`, so the read itself is most of each pass.

The reclassification runs once, after the loop, over the FINAL read. A refused signal on a member
that read shows gone is the cascade case and joins `already_gone`; a refused signal on a member still
present stays an error and that member stays a survivor. The settle therefore cannot launder a real
refusal: it only waits, and the verdict is still a census read, never a signal's exit status.
`SETTLE_S` is a module constant of ten seconds, PINNED at writing as a bound and not a measurement:
the census held bound for the suite is 160 s and the arm's own staging already waits three.

`report["rereads"]` is the liveness of the settle. An arm that went green without it would be an arm
reporting ok on a path it never took; S3 prints it and S4's arms assert it.

### Inventory

- `check_settled_survivors` — a `py.function` cell, leading with the declared verb `check`, the same
  verb as `check_survivors`, which it wraps. `python tools/lexicon/lexicon.py --suggest
  check_settled_survivors --as py.function` answers OK.
- `SETTLE_S` — a module constant beside `SIGNAL_TIMEOUT_S`, in its spelling.
- `rereads` — a report key, beside `killed` and `survivors`.
- `test_a_member_gone_at_the_settled_reread_is_not_a_signal_error` and
  `test_a_member_present_past_the_deadline_stays_a_survivor` — `py.function`, verb `test`.

### Files touched (estimate)

- `tools/process-monitor/reap.py`
- `tools/process-monitor/selftest.py`
- `tools/process-monitor/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The native fallback.** See §3 and §8 F1: it serves a reading the evidence refutes, and fails the
  race this unit fixes.
- **Treat every `Permission denied` as `already_gone`, as `No such process` is.** Rejected because it
  grades by the signal's message instead of by a census read, which is the one thing this reaper's
  header forbids; a live protected process would then read as gone.
- **Lengthen the arm's three-second staging wait, or sleep before its one re-read.** It moves the
  arm and leaves `run_sweep` and `--kill` reporting the same false survivor to the unattended driver
  that calls this reaper through `PROCMON_CMD`.
- **Skip the arm on the hosted runner.** The brief forbids it, and node a reds the same way.

## 5. Production-readiness checklist

- security — N/A: the kill set, the fence and the signal paths are unchanged; only verification waits.
- perf / scale — a clean kill costs one read as before; a racing one costs up to `SETTLE_S` more.
- error / empty / loading states — a member still present at the deadline stays a survivor and an
  error, exactly as today, so `--kill` still exits 1 for it.
- observability — S3: the read count on the kill line and the arm's naming of each leftover member.
- risks — a member that genuinely refuses the signal now costs ten seconds before it is reported.
- testing — S4's two fixture arms, AC4's repeated live arm on node a, and AC5 on the runner.
- migration — N/A: no stored state; the report gains one key.
- user docs — S5, in the kit README.

## 6. Acceptance criteria

- **AC1** — When a driver imports `tools/process-monitor/reap.py`, hands `check_settled_survivors` a
  report whose kill set holds one member with a `Permission denied` entry in `errors`, and replaces
  `census.scan_processes` with a stub listing that member on the first read only, the returned report
  carries no survivor, an empty `errors`, the member in `already_gone`, and `rereads` equal to 2.
  S4's first arm makes the same assertion.
  Red when: `SETTLE_S` is set to 0 as a staged break, so the loop stops after one read and the member
  is a survivor with its error intact; observed red before the break is unstaged.
- **AC2** — When the same driver's stub lists the member on every read, with `SETTLE_S` set to 1, the
  returned report keeps the member in `survivors` and its entry in `errors`, and `rereads` is at least 2.
  S4's second arm makes the same assertion.
  Red when: the reclassification moves an error without reading the final census, so a member still
  present is reported gone.
- **AC3** — When `grep -n "check_survivors(rep, fresh)" tools/process-monitor/reap.py tools/process-monitor/selftest.py`
  runs, it prints nothing, and `grep -c check_settled_survivors` over the same two files totals at
  least four: the definition and three call sites.
  Red when: any of the three verification sites still reads the census once.
  figure: the totals are DERIVED at observation time from the two files.
- **AC4** — When `test_live_tree_dies_completely` is called alone ten times on node a, by a driver
  that imports the census selftest module and calls that one function so no other arm runs,
  every call passes and every `walked` line prints its read count.
  Red when: any call answers a survivor or a signal error.
  cost: about two minutes, most of it the arm's staging wait and the census reads.
  figure: ten is PINNED, against the one-in-six rate node a recorded on 2026-09-17; a clean ten is
  evidence and not proof, which is why AC5 exists.
- **AC5** — When the first three scheduled runs of `.github/workflows/remote-ci.yml` after landing are
  listed with `gh run list --workflow remote-ci.yml --event schedule`, the job
  `held process-monitor census selftest` concluded `success` in each.
  Red when: any of them fails that job; S3 then names the member and its read count.
  permission: runs after landing, which no unit pass reaches; the close records the observation.
  figure: three is PINNED, against two red in the three census runs.

## 7. Gates

`process-monitor census selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/process-monitor/selftest.py · S4's settled-reread arm, staged red by setting `SETTLE_S` to 0 in reap.py · none
New arm: tools/process-monitor/selftest.py · S4's past-the-deadline arm, staged red by moving every refused entry to `already_gone` unconditionally · none

## 8. Open questions

- **FACT-QUESTION · F1** — Is the refused member one the MSYS signal can never reach, or one that was
  exiting when it was signalled?
  Probe: the census selftest's own output in the three census runs, read with `gh run view`, plus the
  `cMendedVintage` unit 11 ledger's run on node a. The observation that decides it: whether the
  refusal recurs at a fixed tree. Liveness: had all three runs and all six node-a runs red with the
  same walk, the never-reachable reading would stand and the native fallback would be the fix.
  Observed: the same walk of 7 with the same four members went red twice and green once on the
  runner, and red once then clean five times on node a, at bytes that did not change. A refusal that
  comes and goes at a fixed tree is timing, so the member was exiting.
  RESOLVED (agent, 2026-10-05, delegated): the exiting reading; this unit settles the verification,
  and the native fallback is recorded under §3 and handed off by §3's edge.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the held-red census's cause C9, the census arm's output in
  three scheduled runs, the `cMendedVintage` unit 11 ledger, and the reaper at base.

## 10. Reuse audit

The seam is `check_survivors` in `tools/process-monitor/reap.py`, which S1 wraps rather than changes,
and the per-row cascade rule `run_kill` already applies to `No such process`, which S1 extends to a
refused signal on a member the settled read shows gone. `python tools/codebase-map/reuse_lookup.py
"re-read the process census until killed members are gone, verify a kill"` and `"kill a process tree
and report survivors from a second census"` both ranked the census module's `CensusRefused` and
unrelated `read` and `report` stems; neither surfaced a retry-until-settled helper, and none exists
in the kit. Recall returned `TOOL-aReapedSpinner-4`, the reaper's own spec, whose S2 makes
verification a second census read and never a signal's exit status; this unit keeps that rule and
only repeats the read. It also returned that build's closing review finding D9, an unsignalable row
counted killed when it exits on its own. The code at base still does that: `check_survivors` derives
`killed` over the whole kill set, unsignalable rows included. It is a neighbouring defect in the same
function, not this race, and §3 leaves it out.

Where the report and the tree disagree: the census classed C9 as host-only; node a recorded the same
refusal on 2026-09-17, so it is a timing race on any Windows host, more frequent on the runner.

Recall terms used: `python tools/memory-recall/query.py "why does the process-monitor reaper report a survivor or a signal error for a member that was dying when it was signalled" --terms "reaper survivors check_survivors already_gone signal error Permission denied leaves-first cascade rescan census process-monitor kill -9"`
