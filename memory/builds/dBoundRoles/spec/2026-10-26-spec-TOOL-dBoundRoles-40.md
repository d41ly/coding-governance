# TOOL-dBoundRoles-40 — a recorded harness-stage stop replayed against every `SubagentStop` hook a default install registers, red on any output, any block or any record

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 16 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 |
| [2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md) | research | TOOL-dBoundRoles-37 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |
| [2026-10-26-prompt-TOOL-dBoundRoles-37-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-37-round1-fix-brief.md) | research | TOOL-dBoundRoles-37 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 |
| [2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 26 unit specs
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`) confirmed finding **id 56 at
HIGH**, report item **H1**. Id 21 shares that item and takes `TOOL-dBoundRoles-39`.

Id 56 is the failure envelope of the same wiring: every typed harness agent, every unattended unit build
and every typed tier2 finder, skeptic and synthesizer, stops through a `SubagentStop` hook wired with
matcher `*`, and nothing in the tree observes what such a hook does to a stop it was never meant to
grade. `TOOL-dBoundRoles-39` fixes the one hook this build adds. This unit is the gate for the class: a
recorded harness-stage stop is replayed against every `SubagentStop` command a default install's
settings file registers, and any stdout, any blocking exit or any return-check record is red. A hook a
later unit wires on that event is in the population the day it is merged. It repairs
`TOOL-dBoundRoles-5` and builds one step after it (order 16).

## 2. Scope (IN)

- **S1** — The recorded stop. The arm writes, under the scratch target it already builds, a session
  directory holding `subagents/workflows/wf_fixture-1/agent-afixture000001.jsonl`, whose first `user`
  record is a harness's computed task opening `[Workflow harness — computed task]` and whose last record
  is an assistant `StructuredOutput` call, and a `SubagentStop` payload naming it: `session_id`,
  `transcript_path`, `cwd`, `hook_event_name` `SubagentStop`, `stop_hook_active` false,
  `last_assistant_message` of plain text, `agent_id`, `agent_transcript_path` and `agent_type`
  `gov-builder`. A second payload is the same with `stop_hook_active` true. The field set is §4
  "Evidence"'s. Observed by AC1.
- **S2** — The population, derived. The arm reads the scratch target's `.claude/settings.json` after
  `TOOL-aOrientedCast-8`'s default apply in `check_roles_install` (`tools/govkit/selftest.py:2767`) and
  lists every command under `hooks.SubagentStop`, whatever its matcher. A population of zero is red, so
  the arm cannot pass by reading nothing: at landing it holds `TOOL-dBoundRoles-5`'s return check.
  Observed by AC2.
- **S3** — The replay. Each command runs once per payload with the payload on stdin, the target as its
  working directory and `CLAUDE_PROJECT_DIR` set to the target, bounded by a timeout. A run is red when it
  exits non-zero, prints any byte on stdout, or leaves a new path under the target's
  `<git common dir>/return-check/`. Each red names the command, the payload and what it printed.
  Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- The route test inside `check-return`: `TOOL-dBoundRoles-39`'s, for id 21. This unit observes it
  through the wiring and changes no hook.
- `SubagentStart` hooks. They cannot block a stop, and `scratch-guard.js` legitimately prints context
  on that event, so the event is outside the population (§4).
- Gov's own `.claude/settings.json`. Its `SubagentStop` commands are the kits' fragments, which the
  default install merges the same way; a hook gov wires by hand outside every kit is not seen.
- A recorded direct-spawn stop. Grading one is the return check's job, observed by
  `TOOL-dBoundRoles-5`'s plants and `TOOL-dBoundRoles-39`'s AC3.

### Edges

- **consumes-from** `TOOL-dBoundRoles-5` — the return check's fragment on `SubagentStop`, merged by the default install, which is the population's first member (id 56)
- **consumes-from** `TOOL-dBoundRoles-39` — the route test, under which the return check prints nothing and writes nothing for the replayed stop, so the arm reads green after unit 39 lands (ids 21 and 56)
- **hands-off** `TOOL-dBoundRoles-50` — S3's replay, which unit 50 bounds by a timeout and runs through the resolved bash (id 38 of the round-1 audit of units 37 to 44)

## 4. Design

### Evidence

- The `SubagentStop` stdin carries the `Stop` fields plus `agent_id`, `agent_transcript_path` and
  `agent_type`, under the parent's `session_id`; a block printed on exit 0 continues the run
  (`memory/builds/aWokenSentinel/build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md:139-150`).
- A typed harness agent's transcript sits under `subagents/workflows/<run id>/`, its first `user` record
  the harness's computed task. Read on this node on 2026-10-26 from this stage's own transcript,
  `wf_b19dd66d-878/agent-ad1797852e5d7334e.jsonl`, whose `.meta.json` names `gov-spec-writer`.
- At base `462d20f3`, `.claude/settings.json` registers no `SubagentStop` hook and one `SubagentStart`
  hook, `tools/hooks/scratch-guard.js`.

### Why the default install, and why `SubagentStop` alone

`check_roles_install`'s default apply merges every default kit's fragments into one settings file, so
its population is every hook an adopter receives on the event. A suite inside one kit would see that
kit's hooks only. `SubagentStart` is left out because its output is context the runtime hands the new
agent, which `scratch-guard.js` prints by design for an unrouted session, and because no start hook can
block a return.

### Inventory

Minted: the fixture run id `wf_fixture-1`, the agent id `afixture000001`, and the check labels of S2 and
S3. No function; if the pass lifts the replay into one, its name is asked of
`python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 16. Dispatch sorts a tie by id string (`tools/workflows/unattended-build.js:608-613`),
so `TOOL-dBoundRoles-39` builds before this unit and the arm reads green at its own pass.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **The replay inside the roles adopter suite.** Its fixture installs the roles kit's hooks only, so a
  `SubagentStop` hook another kit adds is never in its population.
- **Red on any stderr byte.** Every launcher in the tree prints a witness line on stderr when it fails
  open (`TOOL-dBoundRoles-5` S3, S5), and stderr on exit 0 reaches no agent; stdout and the exit are what
  the runtime acts on.

## 5. Production-readiness checklist

- security — no new write path in product code; the arm writes under its scratch target only.
- perf / scale — one bounded hook run per registered command per payload, two payloads.
- error / empty / loading states — an empty population is red (S2); a hook that hangs is cut by the
  timeout and named.
- observability — each red names the command, the payload and its output.
- risks — a future `SubagentStop` hook that must speak on a harness stop reds here; that hook owes a
  stated reason in this arm, which is the review the class needs.
- testing — AC1 to AC3 by a one-case slice and staged copies of it; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

The slice below is
`python -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.check_roles_install(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`,
run from the repo root under the default temp root: it calls the one case function S2 and S3 extend and
runs no suite, as `DEPL-aBenchedProbe-2` §6 runs its case. A staged break is made in a scratch copy of
the module, imported in its place.

- **AC1** — When the slice runs over the built tree, its default apply replays S1's two payloads against
  every registered `SubagentStop` command, and `FAILURES` holds no entry under S2's or S3's labels: each
  command exits 0, prints nothing on stdout, and leaves no path under the target's `return-check/` folder.
  Red when: a hook grades a harness stage's stop, so it blocks the stage or records it invalid.
  cost: one default apply, about a minute.
- **AC2** — When the slice runs a scratch copy whose case deletes the `SubagentStop` group from the
  target's `.claude/settings.json` after the apply, `FAILURES` names an empty population.
  Red when: the arm passes over zero hooks.
- **AC3** — When the slice runs a scratch copy whose case replaces the target's return-check launcher,
  after the apply, with one calling `check-return` with `TOOL-dBoundRoles-39`'s route test removed,
  `FAILURES` names the launcher, the payload and the `decision` line it printed.
  Red when: a hook that blocks a harness stop passes the arm.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the recorded harness-stage stop replayed against every `SubagentStop` command of the default install, staged by a return-check launcher whose verb skips the route test, and by a settings file with the event removed · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 5 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Which suite holds the replay?** Options: (a) `tools/govkit/selftest.py`'s default install case;
  (b) `tools/roles/adopt-roles.test.sh`; (c) `tools/check-wiring.test.sh`. (b) sees one kit's hooks, and
  (c) grades wiring shape and runs no hook. Only (a) reaches the class the left-shift gate names, every
  hook on the event. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich
  survivor, on the install `check_roles_install` already builds. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 26 unit specs, id 56
  (HIGH, item H1, shared with id 21).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dBoundRoles-50, the minors batch of the round-1 audit of units 37 to 44; nothing else moved.

## 10. Reuse audit

The seam is `check_roles_install` (`tools/govkit/selftest.py:2767`), whose default apply already builds a
target holding every default kit's merged settings, and the recorded payload shape of
`TOOL-aWokenSentinel-1-0`. `python tools/codebase-map/reuse_lookup.py "replay a recorded hook payload against every registered hook and fail on output"`
ranked `fail`, `records`, `read_git_output` and `extract_records`, none a replay over registered hooks,
so no existing seam fits beyond the install case named.

Recall terms used: `python tools/memory-recall/query.py "does a SubagentStop hook fire for a workflow harness agent and how is a direct spawn told apart" --terms "SubagentStop SubagentStart workflow harness agent direct spawn transcript subagents workflows marker check-return"`
