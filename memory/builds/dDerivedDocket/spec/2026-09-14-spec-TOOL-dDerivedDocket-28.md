# TOOL-dDerivedDocket-28 — run-owned process ledger

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 28

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

When a session dies, the commands its driver started keep running with no parent. One run found
earlier bars' legs still executing and competing with its own (i26, `aFusedCharter/RUN.md:36`), and
another found six abandoned processes, five of them another repository's, and rightly refused to
kill anything by command line (i1, `aBoundedCeiling/RUN.md:33`). Record every process the driver
starts, by identity, in a per-slug ledger; reap only a recorded process whose starting driver is
gone, through process-monitor's fenced kill; and make the rule both entries asked for the kit's
rule: nothing kills a process this run did not start.

## 2. Scope (IN)

- **S1** `run_bounded` (`tools/unattended/unattended.sh:182`) starts its command in the background,
  records it, and waits for it; the file capture and the `timeout -k` wrapper are unchanged. The
  record is one line in a per-slug ledger beside the lease under the git common dir. Observed by AC1.
- **S2** A record is an IDENTITY, not a name: the MSYS pid, its start token read from procfs, the
  driver's own pid and start token, the keepalive id, the time, and the first three argv words for
  the reader. Where procfs is absent the token is `-`, and a `-` record is counted and never reaped,
  announced. Observed by AC3 and AC8.
- **S3** An ORPHAN is a recorded process that is alive with its recorded start token while its
  recorded driver is not. `--preflight`, `--resume`, `gates-green` before it starts a bar, and `--hold`
  reap every orphan of their own slug, one at a time, through `$PROCMON_CMD --kill-msys <pid>`, and
  prune records whose process is gone. Observed by AC1 and AC2.
- **S4** The wrapper `run_bounded` starts carries the repository root as an argument token, so the
  process-monitor fence still admits the tree once its parent is gone; the runner's own re-exec
  through its absolute path gives the runner the same property. Observed by AC1.
- **S5** `PROCMON_CMD` in `.unattended.conf` names the reaper; gov declares process-monitor's
  `reap.py`. Blank turns reaping off, announced, and orphans are still counted. Observed by AC4.
- **S6** `--status` prints `orphans <n>` when n is positive, derived from the ledger with each
  identity checked, and kills nothing. Observed by AC5.
- **S7** The `--hold` precondition the HELD unit left for this unit: after reaping orphans, `--hold`
  refuses while any recorded process of the slug is alive, naming it — a run cannot hold while its
  own bar is still running. Observed by AC6.
- **S8** The rule, in the stops companion guide and the Skill: a process not in the ledger is
  reported and never killed, whatever its command line says. Observed by AC7.
- **S9** The unattended kit version moves once for this build. Observed by AC9.
- **S10** The unattended suites run once at the unit's end under attribution. Observed by AC10.

## 3. Non-goals (OUT)

- **Processes the agent starts in its own shell** — a suite run at a unit's end, an ad-hoc bar. The
  driver cannot observe a process it did not start (F1). Under this build's method the one bar a run
  owes is `gates-green`'s, which S1 records.
- **Killing by command line, age or spin rate.** Those are process-monitor's sweep modes, which the
  explicit `--kill-msys` path bypasses by design while keeping the fence.
- **The fence, the census and the kill itself.** They are process-monitor's and are called, not
  changed.
- **The runner's absolute argv.** The scratch-hygiene unit's re-exec provides it.
- **Another slug's or another node's processes.** A ledger is per slug and per clone.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-4` — the named `--hold` precondition S7 fills, the lease
  whose directory the ledger shares, and the `--status` line the orphan count joins.
- **consumes-from** `TOOL-dDerivedDocket-25` — the runner re-executed through its absolute path,
  without which the fence refuses to reap a runner whose parent is gone.

## 4. Design

### Data model

```
<git-common-dir>/unattended/<slug>.procs      one line per started command, appended:
  <msys pid> <start token|-> <driver pid> <driver token|-> <keepalive id> <iso-utc> <argv0> <argv1> <argv2>
.unattended.conf     PROCMON_CMD="python tools/process-monitor/reap.py"
--status             ... · orphans <n>
reap output          unattended: reaped orphan <pid> (<argv0 argv1 argv2>), started <iso> by driver <pid>, now gone
                     unattended: NOT reaped <pid> — <exited, pid reused | no procfs token | fence refused: <why>>
```

The start token is field 22 of `/proc/<pid>/stat`, the process start time in clock ticks, read once
at record time and again at reap time. Two processes that share a pid do not share it.

### Why the driver's death defines an orphan

| Candidate definition | What it does to a live run |
|---|---|
| any recorded process alive | kills the bar a background `--close` is still waiting on |
| recorded under a different keepalive id | never reaps a same-session orphan, which is i26's case: the harness killed the driver mid-bar and the session lived on |
| recorded process alive, its driver gone | reaps exactly the processes nobody is waiting for |

The driver waits on every command it starts, so a live driver means a live consumer. A driver pid
that was reused by another process reads as alive, which withholds the reap: the error direction is
a process left running, never one killed.

### Reaping through the fence

`reap.py --kill-msys` translates an MSYS pid to its Windows pid from its own census
(`tools/process-monitor/reap.py:296`) and "bypasses the MODE, never the FENCE"
(`tools/process-monitor/reap.py:321`). The fence admits a process whose own command line carries a
token under a declared root, and everything descending from one. An orphan has no living ancestor, so
its own argv must carry the root: S4's wrapper passes the root as a harmless argument, and the runner
re-executes itself through its absolute path. A reap the fence refuses is reported with the refusal
and the record is kept, so a later reap can succeed and a person can read why this one did not.

### Pruning and concurrency

Appends are single short lines. Pruning rewrites the ledger by tmp-then-rename and happens only in
the four reaping verbs, all of which run under the slug's lease, so the rewrite cannot race an append
from another session. A record is pruned when its process is gone or its token no longer matches. At
a terminal write the ledger is removed when no recorded process is alive, and kept with a line saying
so when one is.

### Inventory

In the `sh.function` cell: the recorder, the orphan reader and the reaper, each named at build time
through `python tools/lexicon/lexicon.py --suggest <identifier> --as sh.function`. The conf key
`PROCMON_CMD`; the ledger file `<slug>.procs`; the `--status` field `orphans`.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.test.sh` · the stops
companion template · `tools/unattended/SKILL.template.md` · `tools/unattended/.unattended.conf.example`
· `.unattended.conf` · the rendered guides and Skill · `memory/map/features/unattended.md`.

### Alternatives rejected

- **Matching orphans by command line**, the remedy a gotcha records. Rejected by i1 itself: five of
  six matching processes belonged to another repository and another session.
- **The driver killing the recorded pid itself.** A bare `kill -9` on a tree's top left all four
  descendants of a three-deep tree alive, and a native process ignores the MSYS signal (the reaper's
  own measurements, in its header). The reaper walks leaves first and verifies by re-census.
- **Recording the command's pid by searching the process table after start.** A table search is a
  name match at one remove; `$!` names the process the driver started and nothing else.

## 5. Production-readiness checklist

- security — the kill surface narrows: only a process this slug's driver started, still carrying its
  recorded start token, with its driver gone, and admitted by the fence. Anything else is reported.
- perf / scale — one appended line per started command; one ledger read and one procfs read per
  record in the four reaping verbs; a reaper call only per orphan.
- error / empty / loading states — no ledger reads as zero orphans; a blank `PROCMON_CMD` counts and
  announces; a record without a token is never reaped; a fence refusal keeps the record.
- observability — the `orphans` field in `--status`, one line per reap or non-reap with its reason.
- risks — the fence admits by command-line token, so a foreign process whose argv happens to carry
  this root is in scope; the ledger is what excludes it, because it is not recorded. A platform
  without procfs gets a ledger that counts and never reaps.
- testing — driver arms over a scratch repository with a stub gate that sleeps, a driver killed
  mid-bar, a same-argv foreign sleeper and a reused-pid record; each staged RED first.
- migration — additive; no ledger exists until the first recorded command.
- user docs — the stops companion's rule, the Skill's line and the conf example's key.

## 6. Acceptance criteria

- **AC1** — When `tools/unattended/unattended.test.sh` kills a fixture driver while its stub bar
  sleeps, and then runs `--resume` with `PROCMON_CMD` set, the stub's process is gone and the output
  names it as a reaped orphan; a sleeper started outside the driver with the same argv is still alive.
  Red when: orphans are matched by command line, so the foreign sleeper dies too.
- **AC2** — When the fixture holds an unrecorded process whose parent is gone, no reaping verb kills
  it, and `--status` does not count it.
  Red when: the reap walks the process table instead of the ledger.
- **AC3** — When a ledger line names a pid whose current start token differs from the recorded one,
  the reap reports `exited, pid reused` and kills nothing.
  Red when: identity is the pid alone, so a reused pid is killed.
- **AC4** — When `PROCMON_CMD` is blank, `--resume` over a live orphan prints that reaping is off and
  counts it, and the orphan is still alive.
  Red when: a blank reaper falls back to a direct `kill`, which bypasses the fence.
- **AC5** — When `--status` runs over a fixture with one live orphan, it prints `orphans 1` and the
  orphan is still alive afterwards.
  Red when: `--status` reaps, which turns a read verb into a kill.
- **AC6** — When `--hold` runs while a recorded bar of the slug is alive under a live driver, it
  refuses naming the pid; after the bar exits, the same `--hold` proceeds.
  Red when: `--hold` holds over a running bar, leaving a HELD record with its own work in flight.
- **AC7** — When `bash tools/unattended/check-unattended.sh` and the skill-wiring check run over the
  rendered tree, the stops companion and the Skill state that a process not in the ledger is never
  killed.
  Red when: the Skill leaves the kill of a stray process undirected, which is how i1 had to be parked.
- **AC8** — When the fixture points the procfs seam at a directory that does not exist, new records
  carry `-`, `--resume` counts them and reaps none, and says why.
  Red when: a record without a token is reaped on the pid alone.
- **AC9** — When `bash tools/check-kit-versions.sh` runs, the unattended version constant and every
  rendered marker agree.
  Red when: the constant moves and a render keeps the old marker.
- **AC10** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once at the
  unit's end, it reports no NEW failure.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: the brief lists this unit among those allowed to run the unattended suites (D12-i8).

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `process-monitor wiring` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · a driver killed mid-bar, a same-argv foreign sleeper, a reused-pid record and a missing procfs · none

## 8. Open questions

- **F1 — which processes does the ledger record?** Options: (a) every command the driver starts; (b)
  those plus a verb the Skill routes agent-started suites through; (c) the runner registering itself
  through an environment variable the driver exports. (b) is a new public verb and (c) a new
  cross-kit contract, and both trip M3 veto 2. RESOLVED (agent, 2026-09-14, delegated): (a), the one
  survivor, with the residual stated in §3.
- **F2 — what is an orphan?** Options in §4's table. RESOLVED (agent, 2026-09-14, delegated): a
  recorded process alive with its recorded token while its recorded driver is gone.
- **F3 — what identifies a process where procfs is absent?** Options: the pid alone, or nothing. The
  pid alone can kill a stranger. RESOLVED (agent, 2026-09-14, delegated): nothing; such a record is
  counted and never reaped.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR 21.4 U27. Departs from DR in naming the reaper's flag:
  DR writes `reap.py --kill <pid>`, and BASE's reaper keys `--kill` on a Windows pid while a
  shell-recorded pid needs `--kill-msys`, which exists for exactly this caller. Adds the fence
  requirement S4 and the start token S2, neither of which DR states. One edge the brief's table does
  not list is added, already declared by its producer: consumes-from unit 25.

## 10. Reuse audit

- **Probe result.** `reuse_lookup.py` over "record and reap processes an unattended run started after
  its session died" named `scan_processes` in `tools/process-monitor/census.py` as a seam and
  `ReapRefused` in `tools/process-monitor/reap.py`; `.sh` is unscanned, so the driver side came from
  reading source. The seams this unit extends: the driver's `run_bounded`, the reaper's `--kill-msys`
  path with its fence, and the runner's own delegation to that path, whose calling shape
  (`PROCMON_ROOT` set, a bounded `timeout`) is the precedent at `tools/run-gates/run-gates.sh:1004`.
- **DR against BASE.** DR's `--kill` is the Windows-pid flag; BASE's MSYS translation lives in
  `--kill-msys`. TOOL-aReapedSpinner-12 records that the delegated kill was never proven end to end
  because every runner in that environment was unattributable; S4 and the scratch-hygiene unit's
  re-exec are what make the join reachable, and AC1 is its first end-to-end observation.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: orphan reap process-monitor fence reap.py kill-msys ledger pid session keepalive
  preflight resume foreign — passed as `--terms` with the question "which orphaned processes may an
  unattended run kill and how does it know they are its own". Top hits: TOOL-aReapedSpinner-14,
  TOOL-aReapedSpinner-12, the aReapedSpinner closing reviews and TOOL-aPromptedMandate-11.
