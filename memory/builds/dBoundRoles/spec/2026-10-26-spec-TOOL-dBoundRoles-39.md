# TOOL-dBoundRoles-39 — the return check grades a direct spawn only: a stop whose transcript is a harness stage's, or whose first record carries no handoff marker, passes untouched

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 16 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 26 unit specs
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`) confirmed finding **id 21 at
HIGH**, report item **H1**. Id 56 shares that item and takes `TOOL-dBoundRoles-40`.

`TOOL-dBoundRoles-5` wires `handoff.py check-return` on `SubagentStop` with matcher `*`, and its S2 exits
early only when `agent_type` is absent or names no agent-true role. Harness stages are spawned with the
same gov-* agent types (`tools/workflows/unattended-unit.js:333-337`,
`tools/workflows/unattended-build.js:541-543`, `tools/workflows/tier2-review.js:270-272`), so their stops
reach the check too. A harness stage returns through StructuredOutput against its stage schema, which
for the builder is `{committed, sha, why, summary}` (`unattended-unit.js:206-215`), while unit 2 gives
`gov-builder` the template `outcome:committed|returned, …`. The check would find no return object, block
the stage up to `roles.retries` times, and record it `valid: false` for `TOOL-dBoundRoles-26` to route.
Nothing in spec 5 separates a direct spawn from a harness agent.

This unit makes the check grade a direct spawn only, by two tests the payload and the transcript already
answer, and stay silent on every other stop. It repairs `TOOL-dBoundRoles-5` and builds one step after
it (order 16).

## 2. Scope (IN)

- **S1** — The route test, run first in `check-return` (`tools/roles/handoff.py`, `TOOL-dBoundRoles-5`
  S2), before the role is loaded or any record is read. A stop is a direct spawn's when both hold: the
  payload's `agent_transcript_path`, separators folded to `/`, holds no `/subagents/workflows/` segment
  pair; and the agent transcript's first `user` record opens with a marker line that
  `roles_lib.extract_prompt_marker` (`tools/roles/roles_lib.py:246`) parses. Any other stop exits 0
  with nothing on stdout or stderr, and writes no record under `return-check/`. Observed by AC1 and AC2.
- **S2** — The order of the verb's steps after this unit: the route test, then `TOOL-dBoundRoles-5` S2's
  role and template reads, then S3's retry and record. A stop that fails the route test never reaches
  the retry count, so no harness stage holds an attempt. Observed by AC1 and AC3.
- **S3** — The plants, in `tools/roles/render_agents.py --selftest` beside `TOOL-dBoundRoles-5`'s:
  `harness-typed-stop`, a payload with `agent_type` `gov-builder`, a transcript under
  `subagents/workflows/<run>/` whose first record is a harness's computed task and a
  `last_assistant_message` of plain text; and `unmarked-stop`, a payload whose transcript sits under
  `subagents/` with a first record carrying no marker. Each must print nothing and write no record.
  `TOOL-dBoundRoles-5`'s `stop-retry` plant, a marked direct spawn, still blocks. Observed by AC1, AC2
  and AC3.
- **S4** — The docs: `tools/roles/README.md`'s paragraph on `check-return` says it grades a direct
  spawn's return only, by the two tests of S1, and that a harness stage's return is graded by its stage
  schema. Observed by AC4.

## 3. Non-goals (OUT)

- The return grammar, `validate_return`, the retry and its record: `TOOL-dBoundRoles-5`'s, unchanged in
  what they do to a direct spawn.
- The gate that replays a recorded harness stop against every `SubagentStop` hook a settings file
  registers: `TOOL-dBoundRoles-40`'s, for id 56.
- A harness stage's own retry of a null return: `TOOL-dBoundRoles-5` S6's `spawnWithRetries`.
- What `TOOL-dBoundRoles-26` routes on a record. With no record written for a harness stage there is
  nothing for it to route.

### Edges

- **consumes-from** `TOOL-dBoundRoles-5` — `check-return`, its `SubagentStop` wiring and its first-record read, which S1 puts behind the route test (id 21)
- **hands-off** `TOOL-dBoundRoles-40` — the route test and the silence it gives a harness stop, which unit 40's replay arm observes through every registered `SubagentStop` hook (ids 21 and 56)
- **hands-off** `TOOL-dBoundRoles-43` — `check-return`'s transcript read, which id 39's item routes through the extended `load_agent_transcript` and `PATH_ID_RE`
- **hands-off** `TOOL-dBoundRoles-50` — S3's plants, S1's session layout and AC4's grep, which unit 50 completes (ids 12, 21 and 40 of the round-1 audit of units 37 to 44)

## 4. Design

### Evidence

- This stage of the harness is itself a typed workflow agent. Its transcript, read on this node on
  2026-10-26, is `subagents/workflows/wf_b19dd66d-878/agent-ad1797852e5d7334e.jsonl` under the session
  directory, its `.meta.json` carries `agentType` `gov-spec-writer`, and its first `user` record opens with
  `[Workflow harness — computed task]`, not a marker. The session's `SubagentStart` hook
  (`scratch-guard.js`) fired for it, so a typed harness agent raises subagent events.
- A direct spawn's transcript is `subagents/agent-<id>.jsonl`, its first record opening with the
  `gov:handoff` marker, which rule 6 admits only as the prompt's first line (`TOOL-dBoundRoles-7` §4,
  read on this node on 2026-10-25; `tools/hooks/agent-cap.js:2102-2129`).
- A sub-agent's end fires `SubagentStop` with `agent_id`, `agent_transcript_path` and `agent_type`
  (`memory/builds/aWokenSentinel/build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md:148-150`).

### Why two tests

The path test alone admits a direct spawn whose layout a later runtime moves; the marker test alone
grades a harness stage whose computed task happens to open with a marker line. Each covers the other's
miss, and both read what the payload and the first record already hold, so S1 adds no file read
`TOOL-dBoundRoles-5` S2 does not already make.

Whether `SubagentStop` fires for a workflow agent at all decides nothing here: if it does not, the route
test is never reached for one; if it does, the test keeps the check silent.

### Inventory

Minted: the plant names `harness-typed-stop` and `unmarked-stop`. The route test is a step of
`check-return`, not a new function; if the pass lifts it into one, its name is asked of
`python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Migration

None: no stored data changes, and no record exists before `TOOL-dBoundRoles-5` lands.

### Rollout

Live at landing, at order 16. Dispatch sorts a tie by id string (`tools/workflows/unattended-build.js:608-613`),
so `TOOL-dBoundRoles-10` builds first and `TOOL-dBoundRoles-40` after this unit.

### Files touched (estimate)

- `tools/roles/handoff.py`
- `tools/roles/render_agents.py`
- `tools/roles/README.md`

### Alternatives rejected

- **Exempt by agent type.** Harness stages and direct spawns share every gov-* type, so no type list
  can tell them apart.
- **Read the `.meta.json` for a harness field.** Its `workflowPhase` key is a runtime detail no record
  of this repository pins, and the path and the marker are what the hooks kit already reads.

## 5. Production-readiness checklist

- security — no new write path; the check writes less than before.
- perf / scale — a harness stop now costs one string test and no transcript read.
- error / empty / loading states — an absent `agent_transcript_path` or an unreadable first record fails
  the route test and exits 0 silent, as `TOOL-dBoundRoles-5` S5 already exits 0 on a broken check.
- observability — a direct spawn's record is unchanged; a harness stop leaves none.
- risks — a direct spawn rendered by hand without a marker is not graded; rule 6 refuses such a spawn
  before it starts.
- testing — AC1 to AC4 by plant and grep; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`; `help/roles.md`'s return-check bullet (`TOOL-dBoundRoles-5` S8) speaks
  of a role agent's direct return already.

## 6. Acceptance criteria

- **AC1** — When `python tools/roles/handoff.py check-return` reads the `harness-typed-stop` payload with
  `roles.retries` at 3, it exits 0, prints nothing on stdout or stderr, and no file appears under the
  fixture's `return-check/` folder.
  Red when: a harness stage's stop is graded, so its StructuredOutput return is blocked.
- **AC2** — When it reads the `unmarked-stop` payload, it exits 0, prints nothing and writes no record.
  Red when: the path test alone admits a stop whose first record carries no marker.
- **AC3** — When it reads `TOOL-dBoundRoles-5`'s `stop-retry` payload, it still prints a `decision` of
  `block` and the record reads 1 attempt.
  Red when: the route test silences a marked direct spawn, so the check grades nothing.
- **AC4** — When `grep -n "direct spawn" tools/roles/README.md` runs, it names the two tests on the
  `check-return` paragraph.
  Red when: the README still says the check grades every typed stop.

## 7. Gates

`roles render selftest` · `roles catalogue` · `roles adopter self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/roles/render_agents.py · covers AC1 AC2 AC3 · the `harness-typed-stop` and `unmarked-stop` plants beside `stop-retry`, staged by a `check-return` with the route test removed, which blocks the harness plant · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 5 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 26 unit specs, id 21
  (HIGH, item H1, shared with id 56).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dBoundRoles-50, the minors batch of the round-1 audit of units 37 to 44; nothing else moved.

## 10. Reuse audit

The seams are `TOOL-dBoundRoles-5` S2's first-record read and `roles_lib.extract_prompt_marker`
(`tools/roles/roles_lib.py:246`), the one reader of a prompt's opening marker, and the subagent layout
`tools/hooks/format-guard.js:101-103` already spells (`RUN_ID_RE`, `WORKFLOW_RUNS_DIR`).
`python tools/codebase-map/reuse_lookup.py "decide whether a subagent stop belongs to a direct spawn or a harness stage"`
ranked `resolve_harness_path`, `stage_or_fail`, `write_staged` and `cmd_staged`, none a route test, so no
existing seam fits beyond the two readers named.

Recall terms used: `python tools/memory-recall/query.py "does a SubagentStop hook fire for a workflow harness agent and how is a direct spawn told apart" --terms "SubagentStop SubagentStart workflow harness agent direct spawn transcript subagents workflows marker check-return"`
