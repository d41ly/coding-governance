# TOOL-aRepatriatedFork-53 — every background task a run starts carries a heartbeat the audit reads

**Status:** SPECCED · rev-2 · 2026-10-01 · node a · Tier-2 · base 56c7befa · streams tooling · order 23

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-prompt-TOOL-aRepatriatedFork-53-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aRepatriatedFork-53-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

On 2026-10-01 a main-loop agent waited eight hours on the foreign-prefix leg and the owner had to
ask whether the run had hung. The idle-wake runs `unattended.sh --audit`, which grades only
driver-dispatched units against the tree's two clocks, so a main-loop agent, a long leg and a suite
started by hand are invisible to it. This unit gives every background task a run starts a declared
heartbeat file and makes `--audit` grade each one against a declared bound, printing STALLED by name
exactly as it does for a dispatched unit.

## 2. Scope (IN)

- **S1** — A new driver verb, `--register-task <slug> --task <name> --heartbeat <path>`, appends one
  tab-separated row, `<ISO> register <name> <path>`, to the sidecar file `tasks.<slug>.tsv` under
  the root `resolve_sidecar_dir` derives, which is `<git-dir>/unattended`. The STARTER registers a
  task before starting it: the main loop for an `Agent` or a background leg, a brief's author for a
  unit's own long command. It refuses a name carrying a tab or a newline, a heartbeat path that is
  not absolute, a name already registered and not yet released, and a run whose derived phase is
  terminal. Absolute is `/…` or a drive letter followed by `/` or `\`. An empty name or path, a
  path carrying a tab or a newline, and a slug with no run-state file refuse too. The terminal
  refusal is `refuse_if_terminal`'s check 26; every other refusal of both verbs is check 88.
  Observed by AC1, AC6 and AC8.
- **S2** — A second verb, `--release-task <slug> --task <name>`, appends `<ISO> release <name>`. A
  name with no open registration refuses. A released name may be registered again, and the newer
  registration is the one graded. Observed by AC6.
- **S3** — `--audit` grades every registered and unreleased task after its unit loop, one line each:
  `unattended-audit: task <name> · registered <ISO> · heartbeat <path> · last-beat <s>s ago|none · PROGRESSING|STALLED`.
  The heartbeat is the file's mtime, so a task beats by appending a line to it and a leg or suite
  beats by its own output log growing. STALLED is the heartbeat older than `TASK_STALL_BOUND`; an
  absent file reads `last-beat none` and is graded from the registration time, so a task gets one
  bound to write its first beat. A STALLED line is followed by one remedy line. Observed by AC1,
  AC2 and AC4.
- **S4** — With no registered and unreleased task, `--audit` prints
  `unattended-audit: no heartbeat-bearing tasks registered`, beside the existing
  `no unit is dispatched and open` line. A run with nothing registered therefore never reads as a
  clean audit of its tasks. Observed by AC3.
- **S5** — A heartbeat file that exists and that `stat -c %Y` cannot date is a dead probe and takes
  the existing refusal `fail 51`, exit 1, naming the file. A zero from it would read as beaten just
  now. Observed by AC5.
- **S6** — `TASK_STALL_BOUND` is a conf key read by `read_bound_key`, OPTIONAL on `GATE_BOUND`'s
  terms, with the kit default 5400 s: three of the thirty-minute beats the build briefs ask for, the
  same three-cadence rule `UNIT_STALL_BOUND_DEFAULT` records for its own figure. It is declared in
  `tools/unattended/.unattended.conf.example`, in the kit descriptor's optional keys, in the
  protocol's conf-key table, and in gov's own `.unattended.conf`. It is read at the top of
  `--audit`, before any line prints, and not at driver load, so its NOTE prints on the one verb
  that grades it rather than on every verb. Observed by AC7.
- **S7** — The idle-wake's instructions in `tools/unattended/SKILL.template.md` act on a task's
  STALLED line: read its heartbeat file, stop the task, record why with `--park` or a `Decided:`
  line, release it, and either re-run it bounded or leave it parked. An `Agent` stops by its task
  id; a process tree stops through the process-monitor kit's reap, because a stopped background
  shell can leave its detached children running. The protocol's idle-wake paragraph and the verbs
  reference gain the two verbs and the task line, and every rendered copy is re-rendered. Observed by
  AC9.
- **S8** — The unattended kit's version moves in every carrier, because its shipped bytes move.
  Observed by AC10.

## 3. Non-goals (OUT)

- Enforcing registration. Nothing refuses an `Agent` spawn or a background shell that was not
  registered first; §8 F1 records why, and the gap is stated in the verbs reference.
- Grading what a task is doing. A heartbeat proves something wrote a file, never that the work is
  useful; the foreign-prefix leg beat for hours after its verdict was decided. Making that leg stop
  at its verdict is `TOOL-aRepatriatedFork-52`'s fail-fast, not this unit's.
- Stopping a task. The audit stays read-only, as `--audit` is today. The idle-wake acts, and the
  reap is the process-monitor kit's.
- `--liveness` and the resume tick. They read a run from outside its session and keep their own
  signals; a heartbeat file is not added to `derive_last_move`.
- A per-task bound. One declared bound covers every task; a task that cannot beat inside it says so
  by beating more often.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-52` — the registration verb and the audit line that the
  redesigned foreign-prefix leg's one-line-per-suite progress feeds as its heartbeat, when the main
  loop registers that leg with its output log as the heartbeat path.

## 4. Design

### Evidence

- `print_audit` in `tools/unattended/unattended.sh` builds its population from the run-state file's
  `dispatch` rows only, and its comment says the process side is not its question. Read at
  `56c7befa`.
- The sidecar root is derived once, by `resolve_sidecar_dir` in `tools/unattended/lib-unattended.sh`,
  and check 32 of the kit gate counts that literal on one code line; `stall.<slug>.log` and
  `resume.<slug>.log` already live there, per slug. A third per-slug sidecar follows the same rule.
- `read_bound_key` is the one reader of a bound key; `UNIT_STALL_BOUND` already uses it, with its
  default and three-cadence reason beside `UNIT_STALL_BOUND_DEFAULT`.
- The run-gates kit already writes a heartbeat by mtime, `gate-queue-heartbeat`, which
  `derive_last_move` reads and never parses. A task heartbeat is read the same way.
- The memory note on silent background work, 2026-10-01, records the eight-hour silence and the
  owner's adoption of this unit.

### Data model

`<git-dir>/unattended/tasks.<slug>.tsv`, append-only, LF, one row per act:

```
<ISO-8601 UTC>\tregister\t<name>\t<absolute heartbeat path>
<ISO-8601 UTC>\trelease\t<name>
```

A task is open when its newest row is a `register`. The file is per worktree, because the sidecar
root is: the run's own worktree is where `--audit` runs, and a task working elsewhere is registered
there with an absolute path to its heartbeat, which is why S1 refuses a relative one.

### Inventory

Minted names, to be confirmed by `python tools/lexicon/lexicon.py --suggest <name>` before writing:
`write_task_register`, `write_task_release` and `print_task_audit` (the shell function cell);
`TASK_STALL_BOUND` and `TASK_STALL_BOUND_DEFAULT` (conf keys and their default); the verbs
`--register-task` and `--release-task`. A refusal renames, and the rename lands as a rev bump here
first.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/SKILL.template.md`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/kit.toml`
- `tools/unattended/README.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `.claude/skills/unattended/SKILL.md`
- `.unattended.conf`
- the unattended kit's version carriers

### Alternatives rejected

- Heartbeats under one fixed directory with the task name as the file name. A dispatched unit in a
  sibling worktree writes into its own git dir, which the run's audit never reads. Registering an
  absolute path from the starter covers both.
- A wrapper verb that runs the command and beats while it lives. It beats for exactly as long as
  the process is alive, which is what the eight-hour leg was, so it reports the stall it exists to
  catch as progress.
- Reading the harness's background-task list. It is session-scoped and in memory, the reason the
  protocol gives for the keepalive being the agent's on both ends.

## 5. Production-readiness checklist

- security — the sidecar is under the git dir and written by the driver alone; a name is refused if
  it could forge a second field, and the path is only ever passed to `stat`, never executed.
- perf / scale — one `stat` per open task per audit tick.
- error / empty / loading states — no registry, every task released, an absent heartbeat, and an
  undatable one each have their own line or refusal (S3 to S5).
- observability — the task line names the heartbeat path, so the idle-wake reads the evidence first.
- risks — a starter that forgets to register is still invisible (§3).
- testing — AC1 to AC8 as slices of `tools/unattended/unattended.test.sh`.
- migration — none; an absent registry is the no-task state.
- user docs — the verbs reference and the protocol, re-rendered (S7).

## 6. Acceptance criteria

- **AC1** — When the §7 new arm runs as a slice, a fixture run registers task `leg-a` with a
  heartbeat file written one second earlier, and `--audit` prints a `task leg-a` line ending
  `PROGRESSING`.
  Red when: the line is absent, as at `56c7befa`, where `--register-task` is an unknown verb.
- **AC2** — In the same slice, `touch -d` ages `leg-a`'s heartbeat past `TASK_STALL_BOUND`, and
  `--audit` prints `STALLED` for it followed by one `remedy` line naming `leg-a`; it still exits 0.
  Red when: an aged heartbeat reads PROGRESSING, or no remedy line follows.
- **AC3** — A fixture run with no `tasks.<slug>.tsv` makes `--audit` print
  `no heartbeat-bearing tasks registered`.
  Red when: the audit prints no task-population line, which reads as a clean audit.
- **AC4** — A task registered with a heartbeat path that does not exist yet prints `last-beat none`
  and PROGRESSING inside the bound, and STALLED once its registration row's time is older than the
  bound.
  Red when: an absent heartbeat is skipped, or is never graded STALLED.
- **AC5** — A `stat` stub on `PATH` that prints nothing for the heartbeat file makes `--audit` exit
  1 with `fail 51` naming that file.
  Red when: the audit exits 0, or grades the task PROGRESSING.
- **AC6** — `--release-task` closes `leg-a`: the next `--audit` prints no `task leg-a` line, a second
  `--release-task` refuses, and a fresh `--register-task` for `leg-a` is graded from its new row.
  Red when: a released task is still graded, or a double registration is accepted.
- **AC7** — A conf declaring `TASK_STALL_BOUND="0"` makes `--audit` exit 2 with the
  `read_bound_key` refusal, and a conf without the key prints its NOTE naming the 5400 s default.
  Red when: a zero bound is accepted, or the default is taken silently.
- **AC8** — `--register-task` with a relative `--heartbeat` path, or with a name holding a tab,
  refuses and appends no row to `tasks.<slug>.tsv`.
  Red when: a row is written.
- **AC9** — `bash tools/unattended/adopt-unattended.sh --check` exits 0 after the templates change,
  and `memory/guides/UNATTENDED-VERBS.md` names `--register-task`, `--release-task` and
  `TASK_STALL_BOUND`.
  Red when: a rendered copy is stale against its template.
- **AC10** — `bash tools/check-kit-versions.sh` exits 0 and
  `python tools/govkit/govkit.py epoch --base 56c7befa` names no kit whose bytes moved without its
  version.
  Red when: a carrier of the unattended kit's version was missed.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `check-wiring self-test` · `memory hygiene`

New arm: `tools/unattended/unattended.test.sh` · a fixture run with a registry holding a fresh, an aged, an absent and an undatable heartbeat, and one with no registry · the suite's assertion floor rises by the new arms

## 8. Open questions

- **F1 — does this unit also refuse an unregistered background spawn?** Option (a): no. The
  starter's obligation is written in the skill, the protocol and every brief, and §3 states the
  gap. Option (b): yes, through a PreToolUse hook that refuses a background `Agent` or shell under a
  live run with no registration row. Recommendation: (a). Option (b) is a second mechanism in the
  hooks kit, which M2 puts in its own unit, and a hook would have to map a session to a run slug it
  is not told.
  RESOLVED (agent, 2026-10-01, delegated): (a). Option (b) widens the hook's refusal surface beyond
  this unit's tier and is a separate mechanism; it is a follow-up for the owner, not this unit.
- **F2 — what is the bound's default?** Option (a): 1800 s, `UNIT_STALL_BOUND`'s figure. Option (b):
  5400 s, three of the thirty-minute beats the briefs ask for. Recommendation: (b). With (a), a
  task beating every thirty minutes reads STALLED on a single late beat, which the default's own
  three-cadence reason exists to prevent.
  RESOLVED (agent, 2026-10-01, delegated): (b).
- **F3 — where does the registry live?** Option (a): the sidecar root, `<git-dir>/unattended`,
  per slug. Option (b): the git common dir, so every worktree's tasks are in one file. Option (c):
  the run-state file. Recommendation: (a). Option (b) adds a second sidecar derivation that check
  32 exists to refuse, and (c) commits process-level facts into the shared record that M6 clause 3
  keeps out of parallel passes.
  RESOLVED (agent, 2026-10-01, delegated): (a), with the absolute heartbeat path covering a task
  that works in another worktree.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft from the owner's 2026-10-01 ruling adopting this unit.
- rev-2 · 2026-10-01 · build pass. The lexicon refused `verb_register_task` and
  `verb_release_task` (`verb` is not in the declared table), so §4 names `write_task_register` and
  `write_task_release`. S1 names the refusal numbers and the three empty, forged-path and no-run
  refusals the build adds. S6 reads the bound at the top of `--audit` rather than at driver load.
  The §7 arm lands in the suite unrun inside the pass; the pass verifies AC1 to AC8 with a direct
  fixture driving the driver, and the slice run of the arm is owed to the main loop.

## 10. Reuse audit

The seam is `print_audit` in `tools/unattended/unattended.sh`, extended with a second population,
with `resolve_sidecar_dir` and `read_bound_key` in `tools/unattended/lib-unattended.sh` reused as
they are. `python tools/codebase-map/reuse_lookup.py "heartbeat file for a background task read by
a stall audit"` returned only name-stem neighbours and reports `.sh` as an unscanned layer, so the
seam was found by reading the driver; the recall probe's first hits were `TOOL-aProbedUnit-11` and
`TOOL-aProbedUnit-3`, the decisions that built `--audit`, and this unit extends that verb rather
than adding a sibling.

Recall terms used: `audit STALLED UNIT_STALL_BOUND heartbeat keepalive idle-wake liveness sidecar dispatched gate-queue-heartbeat progress bound`.
