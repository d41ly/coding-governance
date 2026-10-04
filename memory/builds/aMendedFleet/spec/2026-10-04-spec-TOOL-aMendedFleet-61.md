# TOOL-aMendedFleet-61 — preflight pins the launching CLI version and every resume compares it, and a missing resume tick is announced loudly

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 61

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

An unattended run is launched by one Claude Code CLI and may be resumed by another: the resume tick
starts `claude -p --resume` from the PATH CLI, which on node a is 2.1.178 while the session that
launched this very build runs 2.1.286. Nothing records which CLI launched a run, so a resume through
an older CLI is invisible. And the one place that reports whether the out-of-process resume tick is
registered is an `INFO` line in the adopter's `--check`, which no run reads; a run sat 13.3 hours
with no driver call on a node where it was not. This unit pins the launching version at
`--preflight`, compares it on every resume, and moves the tick's registration into preflight as a
loud line. Neither refuses anything: the review rejected refusing preflight over the tick, and
rejected an authored version floor in favour of the launching session's own version.

## 2. Scope (IN)

- **S1** — `read_cli_version` in `tools/unattended/unattended.sh` reads the running session's CLI
  version from `AI_AGENT`, whose Claude Code shape is `claude-code_<major>-<minor>-<patch>_<kind>`.
  It takes the field between the first and second underscore, turns its dashes into dots, and
  prints it only when the result is two to four dot-separated integers; anything else, an unset
  variable included, returns 1 and prints nothing. Observed by AC1 and AC4.
- **S2** — `--preflight` pins the fact `cli-version` ONCE, the way it pins `base`: written only when
  the record carries none, with the literal `absent` when S1 returns 1. It is written beside
  `write_lease` and never inside it, because the lease-only difference `--landed` admits is a
  closed set of six fact lines. Preflight prints one line naming the pinned value and its source.
  Observed by AC1 and AC5.
- **S3** — `print_cli_version_drift` takes the run-state file and is the first call inside
  `print_resume_orientation`, so every resume row that proceeds prints it once. It compares S1's
  answer against the pinned fact, field by field as integers, and prints exactly one of four lines:
  the same version; a `WARNING` naming both versions when this session's CLI is OLDER than the one
  that launched the run; a `NOTE` naming both when it is newer; and an `UNKNOWN` line naming which
  side is missing. It returns 0 on every path and never writes. Observed by AC2, AC3 and AC4.
- **S4** — `read_tick_registration` in `tools/unattended/lib-unattended.sh` is the one probe of
  whether the scheduled task `gov-resume-tick` exists: under MSYS, Git-Bash or Cygwin
  `schtasks //query //tn gov-resume-tick`, elsewhere the crontab listing, exactly the two probes the
  adopter runs at base. It returns 0 registered, 1 not registered, and 2 with `TR_WHY` set when the
  probing command itself is not on PATH. Observed by AC5 and AC6.
- **S5** — `--preflight` calls S4 after the lease and prints one line per answer: registered; a
  `WARNING` that no scheduled task named `gov-resume-tick` exists on this node, so a run that stalls
  here waits for a human to start a session, with the kit README as the remedy; or a `WARNING` that
  the registration is UNKNOWN, quoting `TR_WHY`. Preflight's exit code does not move on any answer.
  Observed by AC5.
- **S6** — `tools/unattended/adopt-unattended.sh --check` sources the kit library beside itself, as
  the driver and the tick already do, and calls S4 instead of its own copy of the probe. Its
  not-registered line reads `WARNING` where it read `INFO`; the registered line and the exit code
  are unchanged. Observed by AC6.
- **S7** — `tools/unattended/README.md`, where it describes `--preflight`, says that preflight pins
  `cli-version`, that every resume compares against it, and that the tick line is a warning and
  never a refusal. Observed by AC7.
- **S8** — An arm in `tools/unattended/unattended.test.sh` preflights a fixture run under one
  `AI_AGENT` value and resumes it under an older one, and a second arm stubs `schtasks` absent.
  NOT OBSERVED by a criterion here: the suite runs once at the close, and the arm is declared under
  `New arm:` in §7.

## 3. Non-goals (OUT)

- Refusing preflight or a resume on either answer. The review rejected refusing preflight over the
  tick, and a version difference is a fact for the run to report, not a reason to stop it.
- Registering the tick. That is an owner act on node a and is parked in this build's `RUN.md`.
- Updating the CLI on node a, parked beside it for the same reason.
- An authored minimum-version constant. The review rejected it: the comparison is against the
  version that launched the run.
- The session card's NOTE when the PATH CLI is older than the running session. That is `KICK-aMendedFleet-4` (split from unit 77), in
  the kickoff engine, and reads no run-state fact.
- A comparison inside `resume-tick.sh` before it launches. The session it launches runs `--resume`
  under its own `AI_AGENT`, so the comparison happens in the process whose version matters.
- Adding `cli-version` to the protocol's numbered fact list. The protocol already says the set is
  the driver's `set_fact` keys, and its render has 418 bytes of headroom shared with every unit.
- Bumping the unattended kit version, owed once at the close.

### Edges

none

## 4. Design

### Evidence

Read at the worktree HEAD `725b1449`, whose bytes under `tools/` equal base `7af5f564`'s.

- This session's environment carries `AI_AGENT=claude-code_2-1-286_agent` and
  `CLAUDE_CODE_EXECPATH` ending in `claude-code/2.1.286/<hash>/claude.exe`, while `claude --version`
  on PATH prints `2.1.178 (Claude Code)`. PINNED, node a, 2026-10-04.
- The PATH binary, `~/.local/bin/claude.exe` at 2.1.178, bundles the assignment: when `AI_AGENT` is
  unset or already starts with `claude-code_` or `claude-code/`, it sets
  `claude-code_` plus its VERSION with dots turned to dashes plus `_` plus a kind. So a session the
  tick launches from that binary overwrites any inherited value with its own version. Read from the
  binary's bundled source with `grep -a`, PINNED 2026-10-04; the `claude-code/` prefix form is
  UNVERIFIED as an emitted value, so S1 reads only the underscore form and treats the other as
  unknown.
- `write_lease` writes six facts and `check_lease_only_diff` in the library admits a working-tree
  difference only on those six lines, so a seventh line written by every lease would break the
  re-bound landing `--landed` relies on. Hence S2 writes outside it.
- `verb_preflight` pins `base` and the anchor triple with the `[ -n "$(fact …)" ] || set_fact …`
  shape, which S2 copies.
- `print_resume_orientation` has four callers: the holder row, the two take-over endings and the
  same-session restart. Each is a resume that proceeds; every refusal returns before it.
- `adopt-unattended.sh` runs the tick probe inline in its `--check` branch and prints `INFO` on
  both answers (`TOOL-aWokenSentinel-5` S9). It sources no library today. The library's header says
  it defines functions and nothing else, so sourcing it has no side effect.
- `schtasks //query //tn gov-resume-tick` on node a answers `ERROR: The system cannot find the file
  specified.`, recorded by that unit's acceptance ledger and still true: the build's `RUN.md` parks
  the registration as an owner act.
- Node d's `dUnstuckLanding` branch adds no CLI-version or tick code under `tools/unattended/`, so
  there are no bytes to reuse.

### Data model

One new run-state fact, `cli-version`, valued `<major>.<minor>.<patch>` or `absent`, pinned once by
`--preflight` and never rewritten by any verb.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `read_cli_version` | shell function | `sh.function`; `python tools/lexicon/lexicon.py --suggest read_cli_version --as sh.function` answered OK |
| `print_cli_version_drift` | shell function | `sh.function`; the lexicon answered OK |
| `read_tick_registration` | shell function | `sh.function`; the lexicon answered OK |
| `TR_WHY` | shell global | not graded |
| `cli-version` | run-state fact key | none |

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/adopt-unattended.sh`
- `tools/unattended/README.md`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Read the version from `claude --version`.** It answers for the PATH binary, which is exactly the
  one that differs from the running session on node a; it measures the wrong process.
- **Read it from `CLAUDE_CODE_EXECPATH`.** The path segment is an install layout, measured only for
  the desktop host; `AI_AGENT` is set by the CLI itself on both binaries read.
- **Write `cli-version` in `write_lease`.** It would record the resuming version over the launching
  one, and it breaks the six-line lease-only difference.
- **Keep the tick probe in the adopter and copy it into the driver.** Two spellings of one probe is
  the two-answers class; the library exists to hold the one spelling.

## 5. Production-readiness checklist

- security — reads two environment values and runs two fixed read-only probes; nothing from them
  reaches a command line, and the version is validated as integers before it is written.
- perf / scale — one `schtasks` or `crontab -l` spawn at preflight, under a second on node a; the
  resume comparison spawns nothing.
- error / empty / loading states — an unset or foreign `AI_AGENT` pins `absent` and every resume
  says UNKNOWN; a missing probe command says UNKNOWN with its reason; neither changes an exit.
- observability — the preflight lines and the resume line are the record of which CLI ran the run.
- risks — a future CLI could change the `AI_AGENT` shape; S1 then reads UNKNOWN rather than a wrong
  number, which is the safe direction.
- testing — AC1 to AC7 here; the arms in S8.
- migration — a record pinned before this unit has no `cli-version`; S3 reads that as UNKNOWN.
- user docs — S7.

## 6. Acceptance criteria

- **AC1** — When a scratch script built from the unattended suite's prologue and its preflight
  fixture builder runs `bash tools/unattended/unattended.sh --preflight` on a fixture run with
  `AI_AGENT=claude-code_2-1-286_harness` exported, the fixture's `RUN.md` carries the line
  `cli-version: 2.1.286` and stdout names that value.
  Red when: the fact is absent, or the dash-to-dot turn is staged out and the line reads `2-1-286`.
  cost: under a minute; the suite whole is never run.
  fixture: built by the suite prologue under a short `%TEMP%` root, never the scratchpad.
- **AC2** — When the same fixture is then resumed with `--resume` under its own keepalive and
  `AI_AGENT=claude-code_2-1-178_harness`, stdout carries one `WARNING` line naming `2.1.178` and
  `2.1.286`, the verb exits 0, and `grep cli-version` over the fixture's `RUN.md` still prints
  `2.1.286`.
  Red when: no warning prints, or the resume rewrote the pinned fact.
- **AC3** — When the resume is repeated with `AI_AGENT` unset, stdout carries one `UNKNOWN` line
  naming this session's side as missing, and the exit code equals AC2's.
  Red when: an unset variable prints nothing or reads as equal.
- **AC4** — When the resume is repeated with `AI_AGENT=claude-code_2-1-286_harness`, no `WARNING`
  or `NOTE` line names the CLI version; with `AI_AGENT=claude-code_2-1-290_harness` one `NOTE` line
  names both; and with `AI_AGENT=claude-code_2-1-99_harness` one `WARNING` line names both.
  Red when: the comparison is a string comparison, which orders `2.1.99` after `2.1.286` and reads
  the older CLI as newer, or equal versions warn.
- **AC5** — When a scratch shell sources `tools/unattended/lib-unattended.sh` with a stub
  `schtasks` first on PATH that exits 1, `read_tick_registration` returns 1; with the stub exiting 0
  it returns 0; with PATH holding no `schtasks` and no `crontab` it returns 2 and `TR_WHY` names the
  missing command. In the AC1 fixture with the exit-1 stub, preflight's stdout carries the
  `WARNING` line naming `gov-resume-tick` and preflight exits 0.
  Red when: the probe's answer is staged to a constant, so the two stubs read alike.
- **AC6** — When `bash tools/unattended/adopt-unattended.sh --check` runs on node a, where
  `schtasks //query //tn gov-resume-tick` fails today, its output carries a `WARNING` line naming
  `gov-resume-tick` and no `INFO` line naming it, and it exits 0 as it did at base.
  Red when: the adopter still prints `INFO`, or the new wording moves its exit.
  fixture: node a's unregistered state, which the build's `RUN.md` parks as an owner act; a node
  that registers the task observes the registered line instead.
- **AC7** — When `grep -n "cli-version" tools/unattended/README.md` runs, it hits the description
  of `--preflight`.
  Red when: the driver pins a fact its README never names.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a fixture run preflighted under one `AI_AGENT` value and resumed under an older, an equal and an unset one; a stub `schtasks` exiting 1, 0 and absent; staged red by deleting the `print_cli_version_drift` call · none

## 8. Open questions

- **F1** — Is this one mechanism or two?
  Options: one unit for the version pin and the tick line; two units. Both are what preflight
  records or announces about whether a resume of this run will work, both print at the same two
  driver points, and this build's mandate record parks the tick registration with the words "unit
  61 makes the missing tick loud". Splitting would give two units one write set.
  RESOLVED (agent, 2026-10-04, delegated): one mechanism, as the roster states it.
- **FACT-QUESTION · F2** — Which value names the running session's CLI version on every binary a
  run uses?
  Probe: the live environment of this session, and `grep -a` over the 2.1.178 PATH binary for the
  assignment of `AI_AGENT`. The observation that decides it is whether both binaries set it from
  their own version. Liveness: the same `grep -a` over the same binary for a name it never sets,
  `CLAUDE_CLI_FLOOR`, counts 0 and exits 1, so the probe can answer no.
  RESOLVED (agent, 2026-10-04, delegated): `AI_AGENT`, read in its underscore shape only, per S1.
- **F3** — Where does the comparison print?
  Options: in `verb_resume` before its rows; in `print_resume_orientation`; in the tick. Before the
  rows it would print on refused resumes too, and the tick is the wrong process. The orientation is
  the one function every proceeding resume reaches.
  RESOLVED (agent, 2026-10-04, delegated): `print_resume_orientation`, per S3.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 61, report items [B#40] and
  [B#13], the live session environment, the PATH binary's bundled source, and a read of
  `verb_preflight`, `write_lease`, `print_resume_orientation` and the adopter's `--check` at base.
- rev-2 · 2026-10-04 · §3 points the stale-CLI card note at `KICK-aMendedFleet-4`, split from unit 77.

## 10. Reuse audit

The seams extended are the adopter's tick probe in `tools/unattended/adopt-unattended.sh`, which
moves into `tools/unattended/lib-unattended.sh` as the one spelling, the pin-once `set_fact` shape
`verb_preflight` uses for `base`, and `print_resume_orientation`, the one function every proceeding
resume calls. `python tools/codebase-map/reuse_lookup.py "record the launching CLI version at
preflight and compare it when a run resumes"` returned name-stem neighbours in the runlog kit, such
as `build_run_model` and `scan_preflights`, none of which records a CLI version; it prints
`unscanned layers: .sh`, so `git grep` for `AI_AGENT`, `CLAUDE_CODE_EXECPATH` and `claude --version`
over `tools/` was the shell probe, and it found no existing reader of either. Recall returned
`TOOL-aWokenSentinel-5`, the tick and its adopter `INFO` line, `TOOL-aWokenSentinel-1` and
`TOOL-dDerivedDocket-61` on the lease facts, which is why S2 stays outside `write_lease`, and this
build's own parked owner acts. Where the report and the tree disagree: none found; the PATH CLI is
still 2.1.178.

Recall terms used: `python tools/memory-recall/query.py "is the claude CLI version recorded by the
unattended driver and compared when a run is resumed, and why is the resume tick check only INFO"
--terms "CLI version resume tick gov-resume-tick INFO preflight lease session AI_AGENT unattended
resume schtasks registered"`
