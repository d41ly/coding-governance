# TOOL-dBoundRoles-5 — returns through a schema-forced channel on both routes, residual failures retried by `roles.retries`

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 15 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0170@d33b224b whole
**Carries:** node:policy-key.roles.retries

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-17 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 |

<!-- /gen:spec-records -->

## 1. Goal

A harness stage returns through a schema-forced tool (94 of 94 structured), while a direct spawn's
return is free text no code reads (48 of 48), the role's `returns` line is prose, and no subagent-stop
check exists (gap-roles-04, gap register `:156`; `roles.md:359-366`, RL-7). This unit gives the direct
route a channel of the same strength: one `validate_return` in the roles library checks a direct
spawn's final message against its role's typed `return` template at `SubagentStop`, and a residual
failure, a value that does not resolve, is sent back to the agent up to `roles.retries` times. On the
harness route the schemas stay as they are, and a stage that comes back empty is re-run up to the same
count.

## 2. Scope (IN)

- **S1** — `validate_return(role, text, root=None, work_order=None)` in `tools/roles/roles_lib.py`,
  shared interface I16, the call TOOL-dBoundRoles-12 and TOOL-dBoundRoles-26 make
  (`validate_return("gov-orienter", text)`): `role` is a slot, whose `return` template the function
  reads through `load_roles` and `parse_return_template` (TOOL-dBoundRoles-2 S4). The return object is
  the last fenced `json` block of `text`, or `text` itself when it parses as one JSON object, or, for a
  template with no `list` field, the `key: value` lines naming the template's fields, the block shape
  TOOL-dPlacedRequest-4 S3 gives the orientation return. It returns a list of defect lines, each naming
  a field and the rule: no return object; a required field absent; a field the template does not name;
  a value of the wrong type; a closed-set value outside its set; a `sha` that names no commit in `root`;
  a `path` that names no file under `root`; an `answers` value (shared interface I14) off
  TOOL-dBoundRoles-17's `ANSWERS_RE`; and, when `work_order` is given, an `answers` value other than
  its `<prompt path> task-sha=<12hex>`. `root` defaults to the toplevel of the working directory. An
  empty list is a valid return. Observed by AC1, AC2 and AC3.
- **S2** — The verb `python tools/roles/handoff.py check-return`, reading a `SubagentStop` hook payload
  on stdin. It reads the role from `agent_type` through `load_roles`; the return from the payload's
  `last_assistant_message`, else the last assistant text of `agent_transcript_path`; and the work order
  from the agent transcript's first `user` record, whose marker `MARKER_RE` parses. A payload with no
  `agent_type`, or one naming no `agent`-true role, exits 0 printing nothing. Observed by AC4.
- **S3** — The retry. On defects, while the attempts recorded for the agent are fewer than
  `roles.retries`, it prints `{"decision": "block", "reason": …}` on stdout and exits 0; the reason
  names every defect, the role's template and the instruction to return one corrected `json` block.
  Once the attempts reach `roles.retries`, it exits 0 printing nothing and one stderr witness line. The
  attempts live in `<git common dir>/return-check/<agent_id>.json`, with `agent_id` admitted only in the
  shape `[A-Za-z0-9_-]{1,64}`, rewritten on every armed stop with the attempt count, the verdict and the
  defects: the witness record the driver reads, since a stop hook's exit code is no witness
  (`research-runtime-hooks.md:159`, B3). Observed by AC4 and AC5.
- **S4** — `roles.retries` read through TOOL-dGroundRules-2 S6's `resolve`, located through
  `roles_lib.resolve_kit_dir`, never with `tomllib` over `.governance/policy.toml` (shared interface
  I8). Its catalogue row is TOOL-dGroundRules-1 S3's, written from v2's `[policies]` row (v2:1181, "a
  retry count", default 3, owner dBoundRoles); this unit reads it and writes no second row. Observed
  by AC5.
- **S5** — The hook wiring: `tools/roles/return-check.sh`, a launcher that resolves Python with the
  inline `resolve_python` copy `adopt-roles.sh` carries (`tools/roles/adopt-roles.sh:83-112`) and
  runs S2 with the payload on stdin, and `tools/roles/return-check.fragment.json`, event
  `SubagentStop`, matcher `*`, interpreter `bash`, merged by `settings-merge.py --fragment` from
  `adopt-roles.sh --scaffold` and graded by a roles arm in `tools/check-wiring.sh`. A launcher or verb
  that fails exits 0: a broken return check never blocks a stop. Observed by AC8.
- **S6** — The harness route: each of `tools/workflows/unattended-build.template.js`,
  `tier2-review.template.js` and `unattended-unit.js` takes `retries`, a non-negative integer passed
  in `args` the way `efforts` travels, refused before any agent when malformed, and spawns every
  schema-bearing stage through one `spawnWithRetries(prompt, opts)` per file, which re-runs a stage
  whose return is null or undefined up to `retries` times and logs each re-run. Absent, `retries` is
  0 and one log line says so, as an absent `efforts` key is logged
  (`unattended-build.template.js:533-534`). Observed by AC6 and AC7.
- **S7** — The callers pass it: the build Skill's harness-call paragraph
  (`tools/roles/SKILL.template.md:26-27`) and the verbs guide's (`tools/unattended/VERBS.template.md:731-734`)
  add `retries` from `policy.py get roles.retries` beside `efforts`. Observed by AC9.
- **S8** — The user page `help/roles.md`, section "What the hooks refuse" (`:103`), gains the bullet
  for a role agent's direct return that fails its template, sent back up to `roles.retries` times.
  Observed by AC9.

## 3. Non-goals (OUT)

- The `return` template, its grammar and `parse_return_template`: TOOL-dBoundRoles-2's.
- What the driver does with a return that stays invalid after the last retry, the park RL-7 settles:
  TOOL-dBoundRoles-26's outcome table reads the witness record S3 writes.
- Resolving values inside a harness: the workflow runtime has no tree, so a harness stage's `sha` is
  not resolved there; a null return is the residual failure the harness can see.
- The `answers` field's presence on every return, and the legacy population of unmarked returns:
  TOOL-dBoundRoles-17's. S1 compares the value when one is required by the template or present.
- A record return's `**Answers:**` line: TOOL-dBoundRoles-17's grammar, graded where records are.
- A return schema rendered per work order from its upstream rows: TOOL-dDeclaredLoop-29 S6's
  `join_upstream` (`night-pass-two.md:313-317`). The template this unit checks is per role.

### Edges

- **consumes-from** `TOOL-dBoundRoles-2` — the `return` key and `parse_return_template`, which `validate_return` reads; without them there is no template to check against
- **consumes-from** `TOOL-dBoundRoles-17` — the `answers` value a return names, `<prompt path> task-sha=<12hex>`, which `validate_return` compares with the work order
- **hands-off** `TOOL-dBoundRoles-4` — `validate_return`, which checks the prompt writer's return before `--framed-by` takes its framing
- **hands-off** `TOOL-dBoundRoles-12` — `validate_return`, the typed channel the orientation scout's placement return is bound to
- **hands-off** `TOOL-dBoundRoles-23` — `validate_return`, which the default frame extends with the bound each `list` field's return contract states
- **hands-off** `TOOL-dBoundRoles-26` — `validate_return` and the witness record of S3, which the refusal outcome table routes on
- **hands-off** `TOOL-dBoundRoles-39` — `check-return` and its first-record read, which unit 39 puts behind the route test so a harness stage's stop is never graded (id 21 of the round-1 spec audit)
- **hands-off** `TOOL-dBoundRoles-40` — the return check's `SubagentStop` fragment, the first member of the population unit 40 replays a recorded harness stop against (id 56 of the round-1 spec audit)
- **hands-off** `TOOL-dBoundRoles-43` — `check-return`'s transcript read and its `roles.retries` read, which unit 43 routes through `load_agent_transcript` and `read_policy_setting` (ids 31 and 39 of the round-1 spec audit)

## 4. Design

### The direct route

```
SubagentStop payload ──> return-check.sh ──> handoff.py check-return
   agent_type -> role, an agent-true slot of load_roles
   last_assistant_message | agent_transcript_path -> text
   agent transcript, first user record -> MARKER_RE -> work order (path, task-sha)
   defects = validate_return(role, text, root, work_order)
   record  = <git common dir>/return-check/<agent_id>.json   {attempts, valid, defects}
   defects and attempts < roles.retries -> stdout {"decision":"block","reason":…}, attempts += 1
   otherwise                            -> exit 0, the record left as the verdict
```

The recorded `SubagentStop` stdin carries the `Stop` fields, `last_assistant_message` and
`stop_hook_active` among them, plus `agent_id`, `agent_transcript_path` and `agent_type`, under the
parent's `session_id`; and a `Stop` block printed as `{"decision":"block","reason":…}` on exit 0
continued the run, the reason reaching the model as hook feedback
(`memory/builds/aWokenSentinel/build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md:139-150`).
The count lives in a file because `stop_hook_active` says only that some block preceded, not how many;
`format-guard.js` keeps its per-session state under the git dir the same way
(`tools/hooks/format-guard.js:57-60`).

### The value rules

| Type | A value passes when |
|---|---|
| `text` | a non-empty string |
| `sha` | a string of 7 to 40 hex digits that `git cat-file -e <sha>^{commit}` resolves in `root` |
| `path` | a repo-relative string with no `..` segment naming a file under `root` |
| `list` | a JSON array |
| `int` | a JSON integer |
| closed set | one of the template's values |

An optional entry may be absent; a present one is graded. A field the template does not name is a
defect, `answers` excepted when the work order requires it. Only the `sha` and `path` rules are
"residual" in RL-7's sense; the rest are format failures a forced channel prevents and this channel
catches the same way.

### Inventory

Minted: `validate_return`; the verb `check-return`; `tools/roles/return-check.sh`;
`tools/roles/return-check.fragment.json`; the record folder `return-check/` under the git common dir;
the harness argument `retries` and `spawnWithRetries` in each of the three harness files; the
fixture plants of §7's arms (`return-valid`, `return-no-object`, `return-unknown-field`,
`return-bad-sha`, `return-answers-mismatch`, `stop-retry`, `stop-exhausted`, `harness-null-twice`).
Each name is asked of `python tools/lexicon/lexicon.py --suggest <name>` at the pass, with
`--as py.function` or `--as js.function`.

### Migration

None stored. A role whose agent is spawned before the roles kit's `return` templates land meets
`check-return` with no template, which S2 reads as no `agent`-true role and exits 0.

### Rollout

Live at landing for direct spawns once `adopt-roles.sh --scaffold` merges the fragment; the harness
argument is inert until a caller passes it, which S7's two paragraphs make the default.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/return-check.sh`
- `tools/roles/return-check.fragment.json`
- `tools/roles/adopt-roles.sh`
- `tools/roles/README.md`
- `help/roles.md`
- `tools/roles/SKILL.template.md` (rendered to `.claude/skills/build/SKILL.md`)
- `tools/check-wiring.sh`
- `.claude/settings.json`
- `tools/workflows/unattended-build.template.js` (rendered to `tools/workflows/unattended-build.js`)
- `tools/workflows/tier2-review.template.js` (rendered to `tools/workflows/tier2-review.js`)
- `tools/workflows/unattended-unit.js`
- `tools/unattended/VERBS.template.md` (rendered to `memory/guides/UNATTENDED-VERBS.md`)

### Alternatives rejected

- **A node hook with its own validator.** A second validator beside `validate_return` is the copy I16
  forbids; the launcher keeps one in Python.
- **Counting retries from `stop_hook_active`.** It is a boolean and cannot bound a count above one.
- **Re-dispatching from the driver instead of blocking the stop.** It puts the retry in the main
  loop's context, the noise RL-4 and RL-5 keep out, and loses the agent's own state.

## 5. Production-readiness checklist

- security — the hook reads payload paths only through ids in a fixed shape and the payload's own
  transcript path; it writes one record under the git dir; no network.
- perf / scale — one Python launch per subagent stop, with one `git cat-file` per `sha` field; the
  harness retries spawn at most `retries` extra agents per stage.
- error / empty / loading states — no role, no template, an unreadable transcript or a launcher
  failure each exit 0; a malformed `retries` refuses the harness before any agent.
- observability — the record per agent holds attempts, verdict and defects; each harness re-run is
  logged.
- risks — a retried builder re-enters a tree its first attempt touched; its prompt already demands a
  restored tree on a returned divergence. A platform that ignored a `SubagentStop` block would leave
  the record at one attempt, invalid, for TOOL-dBoundRoles-26 to route (§8 F1).
- testing — the plants of §4's inventory through the verb and a stubbed harness runtime; the arms in §7
  are observed RED then GREEN by the main loop at the close.
- migration — none.
- user docs — `help/roles.md` (S8), `tools/roles/README.md` and the build Skill.

## 6. Acceptance criteria

- **AC1** — When `validate_return("gov-builder", text, root)` checks a reply against the builder's
  template `outcome:committed|returned, commit:sha?, why:text?, checks:list`, whose `json` block is
  `{"outcome": "committed", "commit": <a fixture repository's HEAD>, "checks": []}`, it returns no
  defect; with `"commit": "deadbeef"` it returns one naming `commit`; and for `gov-orienter`, a reply
  of `key: value` lines naming its scalar fields is read as its return object.
  Red when: a `sha` is graded by shape alone, so a commit that does not exist passes.
- **AC2** — When it checks a reply with no `json` block, one whose `outcome` is `maybe`, and one adding
  a field `extra`, it returns a defect naming `return object`, `outcome` and `extra` in turn.
  Red when: an unknown field or a value outside the closed set passes.
- **AC3** — When the work order is a prompt `p.md` under `memory/builds/x/prompts` at task-sha
  `aaaaaaaaaaaa` and the reply's `answers` names task-sha `bbbbbbbbbbbb`, it returns a defect naming `answers`.
  Red when: `answers` is read for presence only.
- **AC4** — When `python tools/roles/handoff.py check-return` reads a fixture `SubagentStop` payload
  for a `gov-builder` agent whose `last_assistant_message` lacks `outcome`, with `roles.retries` at 3
  and no record, it prints a `decision` of `block` whose reason names `outcome`, and its record reads
  1 attempt; at 3 recorded attempts it prints nothing, exits 0 and writes a stderr witness; a payload
  with no `agent_type` prints nothing.
  Red when: the verb blocks past `roles.retries`, or a valid return is blocked.
- **AC5** — When the fixture's policy file, `policy.toml`, sets `roles.retries = 1`, the verb blocks the
  first invalid stop and passes the second, the value read through `resolve`.
  fixture: needs TOOL-dGroundRules-1 and -2 built; the build run re-grounds on them.
  Red when: the count is a literal, so the planted value is not read.
- **AC6** — When `unattended-unit.js` runs under a stub runtime whose `agent` returns null twice then
  a valid object, with `args.retries` 2, its result is the object and its log names two re-runs; with
  `args.retries` 1, it takes the dead-agent path its return already has.
  Red when: a null return is taken as final whatever `retries` says.
- **AC7** — When any of the three harness files reads `args.retries` of `-1` or `"3"`, it throws
  before any agent, naming `retries`.
  Red when: a malformed count is coerced, so a stage runs with a count nobody set.
- **AC8** — When `bash tools/check-wiring.sh --resolve-fragment` reads the new fragment, it prints the
  launcher path, and `grep -c "return-check.sh" .claude/settings.json` prints 1 under a
  `SubagentStop` group.
  Red when: the fragment is not merged, so no stop is checked.
- **AC9** — When `grep -n "retries" tools/roles/SKILL.template.md tools/unattended/VERBS.template.md`
  runs, each names `policy.py get roles.retries` beside `efforts` on the harness-call line, and
  `grep -n "roles.retries" help/roles.md` finds the return check's bullet.
  Red when: a caller is told to pass `efforts` alone, so `retries` is always 0.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `lexicon naming predicates` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `workflow script syntax` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/render_agents.py · covers AC1 AC2 AC3 AC4 · its self-test runs `validate_return` and `check-return` over the plants of §4's inventory, staged by a `validate_return` that skips the `sha` rule · none
New arm: tools/workflows/unattended-build.test.sh · covers AC6 AC7 · a stub runtime returns null twice, staged by a `spawnWithRetries` that returns the first result · none

## 8. Open questions

- **F1 — Does a `SubagentStop` block continue the subagent, as a `Stop` block continues the main
  agent?** The `Stop` case was measured (aWokenSentinel-1-0 `:139-142`) and the `SubagentStop` stdin
  was recorded as the `Stop` set plus the agent fields (`:148-150`); the block on `SubagentStop` was
  not exercised there. Options: (a) retry by blocking the stop, with S3's record as the witness either
  way; (b) retry by re-dispatch from the driver. (b) is the alternative §4 rejects. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3; should the platform end the agent despite the block, the record
  reads one attempt and invalid, and TOOL-dBoundRoles-26 routes it, so no criterion but AC4's block
  line depends on the answer, and the close observes AC4 in a live session. widens: none · relaxes:
  none
- **F2 — Where does the direct-route validator run: Python called from a hook, or a node hook with its
  own copy?** Options: (a) a bash launcher with the inline resolver, running `handoff.py check-return`;
  (b) a node hook carrying a JS validator. (b) is a second validator, which I16 forbids. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the shape `settings-merge.py`'s `interpreter` field
  already admits (`tools/settings-merge.py:48-51`). widens: none · relaxes: none
- **F3 — The harness default when a caller passes no `retries`.** Options: (a) 0, logged, the caller
  passing the policy value as S7 says; (b) 3, v2's default typed into each harness. (b) is a second
  copy of a policy value in code. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, one fact in one
  place. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 5, the brief's shared interfaces I8, I14
  and I16, scout B's row for cl-0170, TOOL-dBoundRoles-2's return grammar, and the harnesses and hooks
  at base `4ed9e567`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullets mirroring the edges of TOOL-dBoundRoles-39, TOOL-dBoundRoles-40, TOOL-dBoundRoles-43, promoted by the round-1 spec audit of the 26 unit specs; nothing else moved.

## 10. Reuse audit

The seams extended are the harness stage options (`renderStageOpts`,
`tools/workflows/unattended-build.template.js:541-543` and `tier2-review.template.js:270-272`) and the
schema-bearing `agent()` calls they feed (`unattended-unit.js:333-337`, `tier2-review.template.js:1222`),
the `efforts` argument path a value already travels (`unattended-build.template.js:505-537`), the
roles library's role loader and marker parser (`load_roles`, `roles_lib.py:330`; `MARKER_RE`, `:79`),
`handoff.py`'s transcript reading (`load_agent_transcript`, `:616`), and the fragment wiring of
`tools/settings-merge.py`. the probe `reuse_lookup.py` over the phrase "validate a subagent return against a typed template and retry" ranked `measure_typed_counts`, `derive_fact_templates` and the
SubagentStart inventory row; none validates a return, and `git grep -i retr` over `tools/workflows/`
and `tools/roles/` finds no retry loop (scout B, confirmed at base), so no existing seam fits for the
validator or the retry. Scout B's row agreed with source; its `renderStageOpts` citation `:541` is the
build harness's, and the review harness holds its own at `:270`.

Recall terms used: `python tools/memory-recall/query.py "how does a direct spawn return get validated and retried" --terms "SubagentStop return schema-forced channel roles.retries validate_return typed template direct spawn harness"`
