# TOOL-dBoundRoles-5 — returns through a schema-forced channel on both routes, residual failures retried by `roles.retries`

**Status:** CLOSED · rev-6 · 2026-11-23 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 15 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0170@d33b224b whole
**Carries:** node:policy-key.roles.retries

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-17 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-5-deviation-51.md](../build/2026-10-26-build-TOOL-dBoundRoles-5-deviation-51.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-5-deviation-52.md](../build/2026-10-26-build-TOOL-dBoundRoles-5-deviation-52.md) | deviation | — |
| [2026-11-22-build-TOOL-dBoundRoles-5-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dBoundRoles-5-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dBoundRoles-5-deviation-53.md](../build/2026-11-22-build-TOOL-dBoundRoles-5-deviation-53.md) | deviation | — |
| [2026-11-23-build-TOOL-dBoundRoles-5-1-main-loop-decision.md](../build/2026-11-23-build-TOOL-dBoundRoles-5-1-main-loop-decision.md) | journal | — |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-6 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-37 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-69 |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-6 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-25 TOOL-dBoundRoles-43 TOOL-dBoundRoles-60 |
| [2026-11-22-prompt-TOOL-dBoundRoles-5-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-5-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dBoundRoles-5-crossunit-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-5-crossunit-brief.md) | journal | TOOL-dBoundRoles-4 TOOL-dBoundRoles-12 TOOL-dBoundRoles-23 TOOL-dBoundRoles-39 TOOL-dBoundRoles-41 TOOL-dBoundRoles-3 TOOL-dBoundRoles-24 TOOL-dBoundRoles-13 |
| [2026-11-22-prompt-TOOL-dBoundRoles-5-crossunit-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-5-crossunit-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dBoundRoles-5-reground-c-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-5-reground-c-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dBoundRoles-5-reground-j-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-5-reground-j-brief.md) | journal | TOOL-dBoundRoles-10 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 |
| [2026-11-22-prompt-TOOL-dBoundRoles-5-reground-j-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-5-reground-j-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dBoundRoles-5-spec-tokens-c-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-5-spec-tokens-c-brief.md) | journal | TOOL-dBoundRoles-10 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-4 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-12 TOOL-dBoundRoles-41 TOOL-dBoundRoles-11 TOOL-dBoundRoles-26 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 |

<!-- /gen:spec-records -->

## 1. Goal

A harness stage returns through a schema-forced tool, while a direct spawn's return is free text no
code reads, the role's `returns` line is prose, and no subagent-stop check exists (gap-roles-04,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md@cd15c089:156`).
RL-7's reply measured 48 of 48 direct returns free text and 94 of 94 harness returns structured
(PINNED, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-roles.md@e29e16d7:363-364`).
This unit gives the direct route a channel of the same strength: one `check_return` in the roles
library checks a direct spawn's final message against its role's typed `return` template at
`SubagentStop`, and a residual failure, a value that does not resolve, is sent back to the agent up to
`roles.retries` times. On the harness route the schemas stay as they are, and a single-call stage that
comes back empty is re-run up to the same count (§8 F4).

## 2. Scope (IN)

- **S1** — `check_return(role, text, root=None, work_order=None)` in `tools/roles/roles_lib.py`,
  shared interface I16, the call TOOL-dBoundRoles-12 and TOOL-dBoundRoles-26 make
  (`check_return("gov-orienter", text)`), the name §8 F7 resolves: `role` is a slot, whose
  `return` template the function reads through `load_roles` (`tools/roles/roles_lib.py#load_roles`)
  and `parse_return_template` (`tools/roles/roles_lib.py#parse_return_template`, landed by
  TOOL-dBoundRoles-2 S4), which yields `(name, type, optional)` triples, a closed set as a tuple. The
  return object is the last fenced `json` block of `text`, or `text` itself when it parses as one JSON
  object, or, for a template with no `list` field, the `key: value` lines naming the template's fields,
  the block shape TOOL-dPlacedRequest-4 S3 gives the orientation return. It returns a list of defect
  lines, each naming a field and the rule: no return object; a required field absent; a field the
  template does not name; a value of the wrong type; a closed-set value outside its set; a `sha` that
  names no commit in `root`; a `path` that names no file under `root`; an `answers` value (shared
  interface I14) off the body of TOOL-dBoundRoles-17's `ANSWERS_RE` without its bold prefix, the form
  that unit's §4 "The answers value" grades a harness return's `answers` by; and, when `work_order` is
  given, an `answers` value other than the `<prompt path> task-sha=<12hex>` its `derive_answers_value`
  writes for that work order. `root` defaults to the toplevel of the working directory. An empty list
  is a valid return. Observed by AC1, AC2 and AC3.
- **S2** — The verb `python tools/roles/handoff.py check-return`, reading a `SubagentStop` hook payload
  on stdin. It reads the role from `agent_type` through `load_roles`; the return from the payload's
  `last_assistant_message`, else the last assistant text of `agent_transcript_path`; and the work order
  from the agent transcript's first `user` record, whose marker `MARKER_RE`
  (`tools/roles/roles_lib.py#MARKER_RE`, as TOOL-dBoundRoles-17 S1 leaves it) parses. A payload with no
  `agent_type`, or one naming no `agent`-true role, exits 0 printing nothing. Observed by AC4.
- **S3** — The retry. On defects, while the attempts recorded for the agent are fewer than
  `roles.retries`, it prints `{"decision": "block", "reason": …}` on stdout and exits 0; the reason
  names every defect, the role's template and the instruction to return one corrected `json` block.
  Once the attempts reach `roles.retries`, it exits 0 printing nothing and one stderr witness line. The
  attempts live in `<git common dir>/return-check/<agent_id>.json`, the directory
  `common_git_dir` (`tools/roles/handoff.py#common_git_dir`) names, with `agent_id` admitted only in
  the shape `[A-Za-z0-9_-]{1,64}`, rewritten on every armed stop with the attempt count, the verdict and
  the defects: the witness record the driver reads, since a stop hook's exit code is no witness (B3,
  `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-hooks.md@b0dc01b0:159`).
  Observed by AC4 and AC5.
- **S4** — `roles.retries` read through TOOL-dBoundRoles-21 S1's
  `read_policy_setting("roles.retries", root, with_default=True)`, the roles kit's one runner of
  TOOL-dGroundRules-2 S7's `policy.py get` (`tools/policy/policy.py#cmd_get`), built at order 4 and
  checked against that unit's spec (§8 F5): a kit imports no sibling kit (PLAY-dOrderedCharter-7 §4
  "The policy reads"), and no `tomllib` reads `.governance/policy.toml` (shared interface I8). `get`
  reads the policy file as committed at the landed revision, never the working tree
  (`tools/policy/policy.py@b1894836:30-37`). With `with_default` the catalogue default is the value
  where the file sets none. Its catalogue row is TOOL-dGroundRules-1 S3's, landed at
  `tools/policy/catalogue.toml@25076c3d:271-276` (type `retry-count`, minimum 0, default 3, owner
  dBoundRoles), written from v2's `[policies]` row (v2:1181, "a retry count"); this unit reads it and
  writes no second row. Observed by AC5.
- **S5** — The hook wiring: `tools/roles/return-check.sh`, a launcher that resolves Python with the
  inline `resolve_python` copy `adopt-roles.sh` carries (`tools/roles/adopt-roles.sh@8fb723b3:86-250`),
  whose parity population is derived from the marker line, so the launcher joins it with no list edit
  (`tools/lib/pyrun.sh@da2eb384:14-18`), and runs S2 with the payload on stdin; and
  `tools/roles/return-check.fragment.json`, event `SubagentStop`, matcher `*`, interpreter `bash`. An
  install wires the fragment as it wires every kit's: govkit's `run_fragment_merges`
  (`tools/govkit/govkit.py#run_fragment_merges`) merges each landed `*.fragment.json` through the
  target's `settings-merge.py --fragment` (§8 F6). Gov's own `.claude/settings.json` is merged once by
  the pass with `settings-merge.py --fragment tools/roles/return-check.fragment.json`. A roles arm in
  `tools/check-wiring.sh` grades it through `check_fragments` (`tools/check-wiring.sh#check_fragments`),
  the one per-fragment grader `check_scratch_guard` calls. A launcher or verb that fails exits 0: a
  broken return check never blocks a stop. Observed by AC8.
- **S6** — The harness route: each of `tools/workflows/unattended-build.template.js`,
  `tier2-review.template.js` and `unattended-unit.js` takes `retries`, a non-negative integer passed
  in `args` the way `efforts` travels, refused before any agent when malformed or above the re-run
  bound below, and re-runs a single-call schema-bearing stage whose return is null or undefined up to
  `retries` times, logging each re-run (§8 F4). The re-run is ONE loop per file, the shape the fan-out
  rule admits (`tools/workflows/check-verifier-fanout.js@06239a6f:81-95`): `for (const n of ATTEMPTS)`
  under `gov:sequential-agents(5)`, `ATTEMPTS` a five-element array literal, one awaited `agent()` in
  its body, as `tools/workflows/orient-counterfactual.js@1d7c62d3:161-163` lands it, so a `retries`
  above `ATTEMPTS.length - 1` is refused. In the two templates the loop is the body of one
  `runWithRetries(prompt, opts)`; in `unattended-unit.js` it wraps that file's one spawn inline
  (`tools/workflows/unattended-unit.js@3aa27411:435-440`), and its header's shape paragraph
  (`tools/workflows/unattended-unit.js@3aa27411:20-36`) names the marked loop as its second exception.
  A stage spawned inside a fan keeps its direct `agent()` call and is not re-run: the build harness's
  spec-writer groups, and the review harness's finders and verifiers. The build harness forwards
  `retries` in `dispatch.args` and in the audit's review call beside `efforts`
  (`tools/workflows/unattended-build.template.js@55695bb4:1821`, `@55695bb4:3179-3180`). Absent, `retries` is 0
  and one log line says so, as an absent `efforts` key is logged
  (`tools/workflows/unattended-build.template.js@55695bb4:613-614`). Observed by AC6 and AC7.
- **S7** — The callers pass it: the build Skill's harness-call paragraph
  (`tools/roles/SKILL.template.md@43c0de5f:30-32`) and its three call lines that list `efforts`
  (`tools/roles/SKILL.template.md@43c0de5f:54-55`, `@43c0de5f:72-74`, `@43c0de5f:84-86`), and the verbs guide's
  harness-call paragraph (`tools/unattended/VERBS.template.md@8192ac37:1193-1203`), add `retries` from
  `policy.py get roles.retries` beside `efforts`. Observed by AC9.
- **S8** — The user page `help/roles.md`, section "What the hooks refuse"
  (`help/roles.md@50d4a1c0:201`), gains the bullet for a role agent's direct return that fails its
  template, sent back up to `roles.retries` times. Observed by AC9.

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
  `join_upstream`
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md@e3bafb8b:313-317`).
  The template this unit checks is per role.
- A re-run of a stage spawned inside a fan, the build harness's spec writers and the review harness's
  finders and verifiers: each fan's total is what the fan-out rule bounds, and a re-run inside it is a
  count that rule cannot size (§8 F4).
- Wiring the fragment from `adopt-roles.sh`: govkit's apply wires every landed fragment (§8 F6).

### Edges

- **consumes-from** `TOOL-dBoundRoles-2` — the `return` key and `parse_return_template`, which `check_return` reads; without them there is no template to check against
- **consumes-from** `TOOL-dBoundRoles-17` — the `answers` value a return names, `<prompt path> task-sha=<12hex>`, which `check_return` compares with the work order
- **hands-off** `TOOL-dBoundRoles-4` — `check_return`, which checks the prompt writer's return before `--framed-by` takes its framing
- **hands-off** `TOOL-dBoundRoles-12` — `check_return`, the typed channel the orientation scout's placement return is bound to
- **hands-off** `TOOL-dBoundRoles-23` — `check_return`, which the default frame extends with the bound each `list` field's return contract states
- **hands-off** `TOOL-dBoundRoles-26` — `check_return` and the witness record of S3, which the refusal outcome table routes on
- **hands-off** `TOOL-dBoundRoles-39` — `check-return` and its first-record read, which unit 39 puts behind the route test so a harness stage's stop is never graded (id 21 of the round-1 spec audit)
- **hands-off** `TOOL-dBoundRoles-40` — the return check's `SubagentStop` fragment, the first member of the population unit 40 replays a recorded harness stop against (id 56 of the round-1 spec audit)
- **hands-off** `TOOL-dBoundRoles-43` — `check-return`'s transcript read, which unit 43 routes through `load_agent_transcript`, and its `roles.retries` read, which S4 already makes through `read_policy_setting` and unit 43 holds to it (ids 31 and 39 of the round-1 spec audit)

## 4. Design

### The direct route

```
SubagentStop payload ──> return-check.sh ──> handoff.py check-return
   agent_type -> role, an agent-true slot of load_roles
   last_assistant_message | agent_transcript_path -> text
   agent transcript, first user record -> MARKER_RE -> work order (path, task-sha)
   defects = check_return(role, text, root, work_order)
   record  = <git common dir>/return-check/<agent_id>.json   {attempts, valid, defects}
   defects and attempts < roles.retries -> stdout {"decision":"block","reason":…}, attempts += 1
   otherwise                            -> exit 0, the record left as the verdict
```

The recorded `SubagentStop` stdin carries the `Stop` fields, `last_assistant_message` and
`stop_hook_active` among them, plus `agent_id`, `agent_transcript_path` and `agent_type`, under the
parent's `session_id`; and a `Stop` block printed as `{"decision":"block","reason":…}` on exit 0
continued the run, the reason reaching the model as hook feedback
(`memory/builds/aWokenSentinel/build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md@0f264e3b:140-150`).
The count lives in a file because `stop_hook_active` says only that some block preceded, not how many;
`format-guard.js` keeps its per-session state under the git dir the same way, an id joined into a path
only in the shape `[A-Za-z0-9_-]{1,64}` (`tools/hooks/format-guard.js@cbfbcff2:58-65`).

### The harness re-run

```
runWithRetries(prompt, opts)                     // one per template; inline in unattended-unit.js
  const ATTEMPTS = [0, 1, 2, 3, 4]               // a bounded literal the fan-out rule sizes
  for (const n of ATTEMPTS) {                    // gov:sequential-agents(5)
    if (n > retries) break
    r = await agent(prompt, opts)                // the loop body's one awaited agent()
    if (r !== null && r !== undefined) break
    log a re-run line naming the stage and n + 1
  }
  return r
```

The fan-out rule denies an `agent()` in any loop body unless the loop carries
`gov:sequential-agents(<K>)`, iterates an identifier the file proves bounded, holds one awaited
`agent()` and is the file's only marked loop, `K` at most `MAX_VERIFIERS`
(`tools/workflows/check-verifier-fanout.js@06239a6f:81-95`, `@06239a6f:693`, `@06239a6f:713`;
`tools/hooks/agent-cap.js@935a910d:427`). A loop over `retries` itself is "a caller-settable knob
wearing a constant's clothes" to it, and a helper called from inside a fan hides that fan's `agent()`
from the rule, which is why a fan stage keeps its direct call. What the rule does not check: the
helper's call sites, so a file whose single-call stages each run it spawns up to five agents per
stage, a total read off the stages and not off the marker.

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

Minted: `check_return`; the verb `check-return`; `tools/roles/return-check.sh`;
`tools/roles/return-check.fragment.json`; the record folder `return-check/` under the git common dir;
the harness argument `retries` in each of the three harness files, `ATTEMPTS` and its marked loop in
each, and `runWithRetries` in the two templates; the fixture plants of §7's arms (`return-valid`,
`return-no-object`, `return-unknown-field`, `return-bad-sha`, `return-answers-mismatch`,
`stop-retry`, `stop-exhausted`, `harness-null-twice`). Each name is asked of
`python tools/lexicon/lexicon.py --suggest <name>` at the pass, with `--as py.function` or
`--as js.function`: `runWithRetries` leads with the declared `run`, where `spawn` is no declared verb,
and `check_return` with the declared `check`, which `lexicon.py --suggest check_return --as
py.function` answered OK on 2026-11-22 (§8 F7).

### Migration

None stored. Every role carries a `return` template since TOOL-dBoundRoles-2, the row required on
every role (`tools/roles/role-schema.toml@4f6926e9:82-86`), so the verb meets no role without one. A
role file `load_roles` cannot parse raises `RolesError`, which the verb reads as no role and exits 0
with one stderr witness line, as S5's fail-open says.

### Rollout

Live at landing for direct spawns in this tree once the pass merges the fragment, and in an install at
its next apply or update, whose `run_fragment_merges` wires the landed fragment; the harness argument
is inert until a caller passes it, which S7's paragraphs make the default.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/return-check.sh`
- `tools/roles/return-check.fragment.json`
- `tools/roles/README.md`
- `help/roles.md`
- `tools/roles/SKILL.template.md` (rendered to `.claude/skills/build/SKILL.md`)
- `tools/check-wiring.sh`
- `.claude/settings.json`
- `tools/workflows/unattended-build.template.js` (rendered to `tools/workflows/unattended-build.js`)
- `tools/workflows/tier2-review.template.js` (rendered to `tools/workflows/tier2-review.js`)
- `tools/workflows/unattended-unit.js`
- `tools/workflows/README.md`, whose harness-argument entries list `efforts`
  (`tools/workflows/README.md@1316da7b:825-836`)
- `tools/unattended/VERBS.template.md` (rendered to `memory/guides/UNATTENDED-VERBS.md`)

### Alternatives rejected

- **A node hook with its own validator.** A second validator beside `check_return` is the copy I16
  forbids; the launcher keeps one in Python.
- **Counting retries from `stop_hook_active`.** It is a boolean and cannot bound a count above one.
- **Re-dispatching from the driver instead of blocking the stop.** It puts the retry in the main
  loop's context, the noise RL-4 and RL-5 keep out, and loses the agent's own state.

## 5. Production-readiness checklist

- security — the hook reads payload paths only through ids in a fixed shape and the payload's own
  transcript path; it writes one record under the git dir; no network.
- perf / scale — one Python launch per subagent stop, with one `git cat-file` per `sha` field, and one
  `policy.py get` subprocess inside `read_policy_setting`; the harness retries spawn at most `retries`
  extra agents per single-call stage, `retries` at most `ATTEMPTS.length - 1`.
- error / empty / loading states — no role, an unparseable role file, an unreadable transcript or a
  launcher failure each exit 0; a malformed `retries`, or one above the bound, refuses the harness
  before any agent.
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

- **AC1** — When `check_return("gov-builder", text, root)` checks a reply against the builder's
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
  first invalid stop and passes the second, the value read through `read_policy_setting`'s
  `policy.py get` subprocess.
  fixture: a repository whose `.governance/policy.toml` is committed at its landed revision, since
  `get` never reads the working tree; `tools/hooks/scratch-guard.test.sh@1bae0749:1282-1296` builds one
  by a commit on a branch `GOV_DEFAULT_BRANCH` names. TOOL-dGroundRules-1 and -2 are landed at HEAD.
  Red when: the count is a literal, so the planted value is not read.
- **AC6** — When `unattended-unit.js` runs under a stub runtime whose `agent` returns null twice then
  a valid object, with `args.retries` 2, its result is the object and its log names two re-runs; with
  `args.retries` 1, it takes the dead-agent path its return already has.
  Red when: a null return is taken as final whatever `retries` says.
- **AC7** — When any of the three harness files reads `args.retries` of `-1` or `"3"`, it throws
  before any agent, naming `retries`; and
  `node tools/workflows/check-verifier-fanout.js --hook tools/hooks/agent-cap.js tools/workflows/unattended-build.js tools/workflows/tier2-review.js tools/workflows/unattended-unit.js`
  exits 0 over the rendered files.
  Red when: a malformed count is coerced, so a stage runs with a count nobody set, or the re-run is a
  loop the fan-out rule denies.
- **AC8** — When `bash tools/check-wiring.sh --resolve-fragment` reads the new fragment, it prints the
  launcher path, and `grep -c "return-check.sh" .claude/settings.json` prints 1 under a
  `SubagentStop` group, which `.claude/settings.json` holds none of at HEAD.
  Red when: the fragment is not merged, so no stop is checked.
- **AC9** — When `grep -n "retries" tools/roles/SKILL.template.md tools/unattended/VERBS.template.md`
  runs, each names `policy.py get roles.retries` beside `efforts` on the harness-call paragraph, and
  the Skill on each of its three call lines too, and
  `grep -n "roles.retries" help/roles.md` finds the return check's bullet.
  Red when: a caller is told to pass `efforts` alone, so `retries` is always 0.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `lexicon naming predicates` · `verifier fan-out` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `workflow script syntax` · `recall floor` · `recall floor arms` · `policy fixtures` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/render_agents.py · covers AC1 AC2 AC3 AC4 · its self-test runs `check_return` and `check-return` over the plants of §4's inventory, staged by a `check_return` that skips the `sha` rule · none
New arm: tools/workflows/unattended-build.test.sh · covers AC6 AC7 · a stub runtime returns null twice, staged by a re-run loop that returns the first result · none

## 8. Open questions

- **F1 — Does a `SubagentStop` block continue the subagent, as a `Stop` block continues the main
  agent?** The `Stop` case was measured (aWokenSentinel-1-0,
  `memory/builds/aWokenSentinel/build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md@0f264e3b:140-142`)
  and the `SubagentStop` stdin was recorded as the `Stop` set plus the agent fields
  (`@0f264e3b:148-150`); the block on `SubagentStop` was
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
  already admits (`tools/settings-merge.py@54bc224f:46-48`). widens: none · relaxes: none
- **F3 — The harness default when a caller passes no `retries`.** Options: (a) 0, logged, the caller
  passing the policy value as S7 says; (b) 3, v2's default typed into each harness. (b) is a second
  copy of a policy value in code. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, one fact in one
  place. widens: none · relaxes: none
- **F4 — How does a harness re-run a stage, given the fan-out rule over every committed harness?**
  The rule denies an `agent()` in any loop body but one marked `gov:sequential-agents(<K>)` over an
  identifier the file proves bounded, one per script, `K` at most `MAX_VERIFIERS` (§4 "The harness re-run"); it
  stood at base as agent-cap's rule 2 and is the review kit's `check-verifier-fanout.js` since
  TOOL-dFairHearing-16, run by the unguarded `verifier fan-out` leg. Rev-4's "every schema-bearing
  stage through one helper" named no shape. Options: (a) a loop over `retries` around each call; (b) a
  helper that calls itself with one retry fewer, which no loop header shows the rule; (c) one marked
  loop per file over a five-element literal, re-running the single-call stages only, a fan stage
  keeping its direct call, and a `retries` above four refused; (d) park. (a) is denied by the rule, so
  it fails a gate this spec names (veto 1). (b) passes by being invisible to the rule, and wrapping a
  fan's `agent()` in a helper is the evasion the build harness's header names
  (`tools/workflows/unattended-build.template.js@55695bb4:84-97`). RESOLVED (agent, 2026-11-22,
  delegated): (c), rung 3, the one survivor holding AC6 and AC7 and the leg, in the shape
  `tools/workflows/orient-counterfactual.js` already lands. widens: none · relaxes: a stage spawned
  inside a fan is not re-run, and a `retries` above `ATTEMPTS.length - 1` is refused at the harness
- **F5 — Which reader reads `roles.retries`?** Options: (a) TOOL-dBoundRoles-21 S1's
  `read_policy_setting` with `with_default`, built at order 4, the roles kit's one runner of
  `policy.py get`, which TOOL-dBoundRoles-43 S21 names this unit as calling; (b) this unit's own
  `policy.py get` subprocess, as rev-3 wrote. (b) is a second policy runner in one kit, the fork
  TOOL-dBoundRoles-15 §8 F6 resolved for its key. RESOLVED (agent, 2026-11-22, delegated): (a), rung
  3, the seam M5 names and that precedent. widens: none · relaxes: none
- **F6 — Who wires the fragment in an install?** Options: (a) govkit's `run_fragment_merges`, which
  wires every landed `*.fragment.json` on apply and on update, gov's own settings merged once by the
  pass; (b) `adopt-roles.sh --scaffold` running `settings-merge.py --fragment`, as rev-4 wrote. (b) is a
  second wirer of one fragment, and no adopter at HEAD merges its own: memory-recall's prints the
  command (`tools/memory-recall/adopt-memory-recall.sh@48d9ddb1:356-361`). RESOLVED (agent, 2026-11-22,
  delegated): (a), rung 3, the tie-break's reuse of the seam an apply already runs, and the population
  TOOL-dBoundRoles-40 replays. widens: none · relaxes: none
- **F7 — Which name does shared interface I16 carry, when `.lexicon.conf` declares `check` "NOT
  `validate`" (`.lexicon.conf@c256a48f:736`) and `lexicon.py --suggest validate_return` answers
  `use check_return`?** Options: (a) keep `validate_return`, the pass re-measuring `VERB_OFFENDER_PIN`
  (`.lexicon.conf@c256a48f:427`) with a comment naming it, as TOOL-dGroundRules-4 re-measured it when
  `validate` arrived in `tools/policy/policy.py` (`.lexicon.conf@c256a48f:315-319`); (b) rename it
  `check_return`, the name the lexicon answers, and revise each spec that calls it to that name. (a)
  raises the verb pin, a declared ceiling, which is the owner's to move (the build method's M3), so no
  delegated resolver may take it. RESOLVED (agent, 2026-11-22, delegated): (b), rung 1, the ruling of
  `2026-11-22-prompt-TOOL-dBoundRoles-5-crossunit-brief`, which renames it in TOOL-dBoundRoles-4, -12,
  -23 and -39 in the same pass, TOOL-dBoundRoles-26 already spelling `check_return`; the pin does not
  move. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 5, the brief's shared interfaces I8, I14
  and I16, scout B's row for cl-0170, TOOL-dBoundRoles-2's return grammar, and the harnesses and hooks
  at base `4ed9e567`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullets mirroring the edges of TOOL-dBoundRoles-39, TOOL-dBoundRoles-40, TOOL-dBoundRoles-43, promoted by the round-1 spec audit of the 26 unit specs; nothing else moved.
- rev-3 · 2026-10-26 · S4 · AC5 · re-grounded per
  `build/2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck.md` row 14: `roles.retries` is read by
  the `policy.py get` subprocess, the one seam PLAY-dOrderedCharter-7 §4 lets a sibling kit reach,
  never by an in-process `resolve`.
- rev-4 · 2026-11-22 · §7 · re-grounded by the live-spec token brief `2026-11-22-prompt-TOOL-dBoundRoles-5-spec-tokens-c-brief`: the leg line gains `policy fixtures`, as `tools/roles/roles_lib.py` in Files touched trips its guard; nothing else moved.
- rev-5 · 2026-11-22 · §1 · S1 S2 S3 S4 S5 S6 S7 S8 · §3 · §4 · §5 · AC5 AC7 AC8 AC9 · §7 · §8 · §10 ·
  re-grounded at HEAD `a3efb1d50` by `2026-11-22-prompt-TOOL-dBoundRoles-5-reground-j-brief`. Every
  code citation re-pointed to a symbol or a blob-pinned line, the cited records pinned too. S4 reads
  through `read_policy_setting` (F5) and S5 leaves the wiring to govkit's `run_fragment_merges` (F6),
  `adopt-roles.sh` leaving Files touched; S6 names the re-run shape the fan-out rule admits, single-call
  stages only, `spawnWithRetries` renamed `runWithRetries` for the lexicon's declared verb (F4); the
  `validate_return` name is kept with a pin re-measure (F7), `.lexicon.conf` and
  `tools/workflows/README.md` joining Files touched; S7 adds the Skill's three call lines. Claims on
  earlier units were checked against their specs: TOOL-dBoundRoles-21 S1 for `read_policy_setting`,
  TOOL-dBoundRoles-17 S1 and §4 "The answers value" for `MARKER_RE` and the bare `answers` body; unit 2's
  template grammar and every role's template were read at HEAD, where it is CLOSED. §7 gains the
  `verifier fan-out` leg; AC5's fixture names the landed-revision read and AC7 the fan-out rule.
- rev-6 · 2026-11-22 · §1 · S1 · §3 · §4 · AC1 · §7 · §8 F7 · folded by
  `2026-11-22-prompt-TOOL-dBoundRoles-5-crossunit-brief`, item 1. F7 re-resolved to (b): the checker is
  `check_return`, the name the lexicon answers, since raising `VERB_OFFENDER_PIN` moves a declared
  ceiling, the owner's. `.lexicon.conf` leaves Files touched; no criterion or leg re-measured the pin,
  and `lexicon naming predicates` stays on the leg line, its guard tripped by `tools/`. The §10 recall
  terms keep the old name, the arguments as they were passed; nothing else moved.

## 10. Reuse audit

The seams extended are the harness stage options
(`tools/workflows/unattended-build.template.js#renderStageOpts` and
`tools/workflows/tier2-review.template.js#renderStageOpts`) and the single-call schema-bearing
`agent()` calls they feed (`tools/workflows/unattended-unit.js@3aa27411:435-440`, and the review
harness's probe and synthesis calls), the `efforts` argument path a value already travels
(`tools/workflows/unattended-build.template.js@55695bb4:585-623`), the one loop shape the fan-out rule
admits (`tools/workflows/orient-counterfactual.js@1d7c62d3:161-163`), the roles library's role loader
and marker parser (`tools/roles/roles_lib.py#load_roles`, `tools/roles/roles_lib.py#MARKER_RE`) and
its policy runner (TOOL-dBoundRoles-21 S1's `read_policy_setting`), `handoff.py`'s transcript reading
(`tools/roles/handoff.py#load_agent_transcript`) and common-dir resolver
(`tools/roles/handoff.py#common_git_dir`), govkit's fragment wiring
(`tools/govkit/govkit.py#run_fragment_merges`) and check-wiring's per-fragment grader
(`tools/check-wiring.sh#check_fragments`). the probe `reuse_lookup.py` over the phrase "validate a subagent return against a typed template and retry" ranked `measure_typed_counts`, `derive_fact_templates` and the
SubagentStart inventory row; none validates a return, and `git grep -i retr` over `tools/workflows/`
and `tools/roles/` finds no retry loop, at base (scout B) and at HEAD `a3efb1d50` alike, so no
existing seam fits for the validator or the retry. Scout B's row agreed with source at base; its
`renderStageOpts` citation was the build harness's, and the review harness holds its own.

Recall terms used: `python tools/memory-recall/query.py "how does a direct spawn return get validated and retried" --terms "SubagentStop return schema-forced channel roles.retries validate_return typed template direct spawn harness"`
