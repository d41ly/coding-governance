# TOOL-dFurnishedOrders-6 — the answered-call hook: a role agent's call its work order already answers refused, warned or recorded by `roles.answered-calls`, a verifier's read of its subject exempt, and each hook failure recorded

**Status:** DEFERRED · rev-3 · 2026-10-28 · node d · Tier-2 · base 2193e25d · streams tooling · order 11 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0197@ced122c4 whole
**Carries:** node:policy-key.roles.answered-calls

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-a.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-28-build-TOOL-dFurnishedOrders-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dFurnishedOrders-1-agent-ledger.md) | journal | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-43 TOOL-dFurnishedOrders-44 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-47 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-57 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61 |
| [2026-10-28-build-TOOL-dFurnishedOrders-6-deviation-61.md](../build/2026-10-28-build-TOOL-dFurnishedOrders-6-deviation-61.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |
| [2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-crosscheck.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61 |
| [2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-58 |
| [2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-16 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing sees or bounds an answered call: state, locate and method calls are 12.7% of 9,980 role calls
and 16.9% of the bytes role agents take in, and no hook compares a call with the work order
(`gap-roles-13`, gap register line 165; PINNED, measured by the roles round on 2026-10-15). P29's item
10 (`layer-roles.md:320-336`, settled as F3-2) is this unit: a PreToolUse hook that finds a role
agent's work order and, for a call whose answer the work order already holds, does what
`roles.answered-calls` says, `refuse` naming where the answer sits by default, `warn` or `record`. A
verifier's read of its subject is never an answered call, and neither is a read the packet does not
cover. Below CLI 2.1.295, where a rule on an ungated tool stays open when its hook fails (Runtime
`[enforce]`, RT-2), each failure is recorded.

## 2. Scope (IN)

- **S1** — The hook, `tools/roles/answered-calls.js` (the module TOOL-dFurnishedOrders-14 creates),
  gaining `main()` and `checkAnsweredCall(data, env)`: a `PreToolUse` hook on `Read|Grep|Bash` that
  judges a call only when the payload carries an `agent_type` naming a role of the index
  (`loadRoleIndex`, `tools/hooks/scratch-guard.js:952`); the main loop is never judged. Observed by
  AC3.
- **S2** — The work order, read by `readWorkOrderText(data)`: the first `user` record of the agent's
  transcript, located as TOOL-dBoundRoles-7 S4's `readWorkOrderAllowance` locates it, extracted at
  this, its second caller, into `tools/hooks/scratch-guard.js`'s exports so both read one locator.
  Its marker (`extractHandoffMarker`, `tools/hooks/agent-cap.js:1626`, with TOOL-dBoundRoles-17's
  `item=`) gives the role and the item. No transcript, no first record or no marker: the call runs and
  nothing is recorded. Observed by AC3.
- **S3** — The three answered classes, per §4 "The classes": a read of a handed range at the same
  blob, decided by TOOL-dFurnishedOrders-14's `deriveCallRead`, `readHandedRanges` and the matcher
  `checkAnsweredRange`, the JavaScript copy of `check_answered_range` the hook calls; a whole method document whose slice is handed, read from
  TOOL-dFurnishedOrders-8's `### Method slices` block by `readHandedSlices(text)`; and a state or
  locate call whose handed `cmd:` value still holds, by `checkStateCall` over the `STATE_READERS`
  table. Observed by AC1, AC6 and AC7.
- **S4** — The exemptions. A matched read of a range handed under `### input:<class>`, by a role whose
  `verifies` list (TOOL-dFurnishedOrders-5's field, J2, one of its `VERIFY_CLASSES` `subject`, `claim`
  and `verdict`, read from the role index where that unit's S4 writes it) names `<class>`, runs: a
  verifier's read of its subject. A call no handed range, slice or value covers runs. Neither is
  recorded. Observed by AC2 and AC3.
- **S5** — The policy, `roles.answered-calls`, read once per answered call and never before one is
  found (J1), by running dGroundRules' JS reader's own CLI as a subprocess at the payload's repository:
  `node <policy kit>/policy-mirror.js get roles.answered-calls --repo <repo>`
  (`tools/policy/policy-mirror.js:160-186`), `node` being `process.execPath`, under the 5-second bound
  the state class's re-run takes. A kit imports no sibling kit (TOOL-dGroundRules-1 §4), so the hook
  never `require`s the policy kit's module, as KICK-dKeptSession-8 S5 rules for its own hook; the file
  is located by that unit's `resolvePolicyHelper()`, exported from `tools/hooks/scratch-guard.js`.
  `refuse` exits 2 naming the anchor; `warn` exits 0 with one stderr line naming it; `record` exits 0
  silently. A spawn that fails or times out, a non-zero exit (the reader's refusal is exit 2), or a
  printed value outside the three is a hook failure (S7). Observed by AC1 and AC4.
- **S6** — The record (J12): one JSON line per decision appended to
  `<git common dir>/answered-calls/<session_id>.jsonl`, with `utc`, `agent_id`, `role`, `item`, `tool`,
  `verdict` (`refused`, `warned`, `recorded`, `hook-failed`) and `anchor`, the line capped at 1024
  bytes by cutting `anchor`. A `session_id` or `agent_id` outside `[A-Za-z0-9_-]{1,64}` writes no line;
  the decision still stands. The one reader is `read_answered_calls(root, session_id)` in
  `tools/roles/roles_lib.py`, returning `(records, malformed)`, `records` a list of the seven-field
  dicts and `malformed` the count of lines it skipped, or `None` when the session has no file.
  Observed by AC8.
- **S7** — The failure path. A throw anywhere in S2 to S6 is caught, writes a `hook-failed` record
  whose `anchor` is the error's first line, and then: below CLI 2.1.295, or where the session's
  version is unreadable, exits 0, the rule open as that CLI leaves it and the failure on record; at or
  above 2.1.295, exits 1, so the CLI's failure handling, which `runtime.hook-failure` decides,
  applies. The session's version is read from `AI_AGENT` by `readSessionCli(env)`, the rule
  `skills/session-kickoff/manifest-check.sh:406-415` states, spelled inline as that file spells it
  because a kit names no file of another. The threshold literal is `2.1.295`. Observed by AC5.
- **S8** — The wiring: `tools/roles/answered-calls.fragment.json` (event `PreToolUse`, matcher
  `Read|Grep|Bash`, marker `answered-calls.js`), laid out as TOOL-dBoundRoles-25 S2's
  `spawn-guard.fragment.json`; gov's `.claude/settings.json` wired by `settings-merge.py --fragment`;
  `adopt-roles.sh --scaffold` merging it as TOOL-dBoundRoles-5 S5 merges `return-check.fragment.json`;
  and the roles arm of `tools/check-wiring.sh` grading it. Observed by AC9.
- **S9** — The suite and its leg: `tools/roles/answered-calls.test.sh`, withheld from adopters as
  `project-owned` in `tools/roles/kit.toml`, run by a new leg `answered-calls self-test`. The leg is
  declared once, by `python tools/run-gates/leg_factory.py new --exempt <why>`, as an `[[exempt_leg]]`
  row of `tools/govkit/registry.toml` holding every manifest key (TOOL-dWitnessedBar-11 S1, S3). Its
  `enforces` is `["principle.p29"]`: v2's P29 `[enforcement]` row names `cl-dClosedLoop-0197`, which
  this unit carries (v2:1851), by step 1 of TOOL-dWitnessedBar-11 §4 "The enforces rule".
  `tools/gate-legs.json` is rendered by `leg_factory.py --write`, never edited, beside the other rows
  a new leg owes (`tools/govkit/subject-pins.tsv`,
  `tools/run-gates/selftest-budgets.txt`). Where `leg_factory.py` is not built at the pass, the pass
  records that a hand edit stood in for it. Observed by AC11; the suite is the leg's runner, observed
  RED then GREEN by the main loop at the close (§7).
- **S10** — The docs: `help/roles.md`'s "What the hooks refuse" gains the answered call, its three
  values and what never counts; `tools/roles/README.md` gains the hook's section. Observed by AC10.

## 3. Non-goals (OUT)

- The range matcher, the excerpt key, the call's read and the handed ranges: TOOL-dFurnishedOrders-14's,
  called here.
- `onFailure` on the fragment and the fail-closed choice at or above 2.1.295: `runtime.hook-failure`
  (`tools/policy/catalogue.toml:472`, owner dWellOiledMachine). This unit exits non-zero there and sets
  nothing.
- The supervisor's binding record a harness-route act would be found by (item 10's "the act's
  task-sha and the session's binding record"): dWellOiledMachine's. This unit finds the work order by
  the agent transcript, which every route writes.
- Counting the records into role metrics: TOOL-dFurnishedOrders-10's, through `read_answered_calls`.
- A PowerShell read, and a locate call by `Glob`: neither is an answered class here (§4 "What it does
  not check").

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-5` — `verifies`, the role field that makes a role a verifier and names the inputs its job reads; without it no read is exempt and a verifier is refused its subject
- **consumes-from** `TOOL-dFurnishedOrders-8` — `### Method slices`, the handed slice block whose headings name the document and range the method class answers
- **consumes-from** `TOOL-dFurnishedOrders-14` — `match_answered_range`, spelled `checkAnsweredRange` in the hook (that unit's §8 F2), with `deriveCallRead` and `readHandedRanges`
- **hands-off** `TOOL-dFurnishedOrders-10` — `read_answered_calls`, the one reader of the hook's records, which the role metrics count by verdict
- **consumes-from** external — TOOL-dBoundRoles-7 S4 (`readWorkOrderAllowance`'s transcript locator), TOOL-dBoundRoles-13 (the `cmd:` key), TOOL-dBoundRoles-17 S1 (`item=`), TOOL-dBoundRoles-25 S2 (the pack layout), TOOL-dBoundRoles-5 S5 (the roles arm of `check-wiring.sh`), KICK-dKeptSession-8 S5 (`resolvePolicyHelper`), TOOL-dWitnessedBar-11 S1 to S3 (the leg's declaration and render), each specced and unbuilt at base `2193e25d`
- **hands-off** `TOOL-dFurnishedOrders-23` — `checkAnsweredCall`'s exemption step and the suite's `### input:claim` plant, which unit 23 keys on `subject-reads` and replaces with the shipped population (id 48)
- **hands-off** `TOOL-dFurnishedOrders-29` — `answered-calls.js`, its suite and its leg, whose broken-index path, version fold, registries, guard and sibling reach unit 29 S1, S2 and S18 to S20 settle (ids 2, 23, 43, 44, 45)

## 4. Design

### The decision

```
checkAnsweredCall(data, env)
  no agent_type, or no role of the index           -> run
  text = readWorkOrderText(data); none or no marker -> run
  answer = read class (S3a) or method class (S3b) or state class (S3c); none -> run
  read class matched under ### input:<name>, name in role.verifies -> run      (S4)
  value = spawn policy-mirror.js get roles.answered-calls; fails -> S7
  refuse -> record refused, stderr deny, exit 2
  warn   -> record warned,  stderr notice, exit 0
  record -> record recorded, exit 0
  any throw -> record hook-failed; exit 0 below 2.1.295 or unknown, else exit 1   (S7)
```

### The classes

| Class | The call | Answered when | Anchor |
|---|---|---|---|
| read | `Read`, `Grep` content over one file, a `SHELL_READERS` command | `checkAnsweredRange` finds a handed `blob:` range at the file's blob now covering the read | the block heading and the key |
| method | `Read` with no `offset` and no `limit` | the work order's `### Method slices` block holds a `#### <tag> — <path>:<lo>-<hi>` heading for that path (the handed form; a `pointer` line hands no text and never answers) | the tag |
| state | a `Bash` simple command whose argv `STATE_READERS` lists | a handed `cmd:` fact's `argv12` equals the call's and the command, re-run in the payload's `cwd` under a 5-second bound, prints output whose `out12` equals the fact's | the block heading and the key |

`STATE_READERS` holds read-only git commands only: `git rev-parse`, `git branch --show-current`,
`git merge-base` and `git ls-files`. The hook recomputes the handed value at the call, as item 10
says, so once the role's own commit or a parallel pass moves it, the call runs.

### The refusal

```
BLOCKED by answered-calls: this Read of tools/x.py lines 40-44 is answered in your work order under
`### input:spec`, key blob:tools/x.py@9f0c1d2e3a4b:40-44. Use it as handed (P29). A read of lines
the work order does not hold runs; roles.answered-calls decides this refusal.
```

### The record

```json
{"utc":"2026-10-26T18:02:11Z","agent_id":"a1b2c3","role":"gov-builder","item":"item.build.unit-pass","tool":"Read","verdict":"refused","anchor":"input:spec blob:tools/x.py@9f0c1d2e3a4b:40-44"}
```

One file per session, appended with one `appendFileSync` per line, so concurrent agents of one session
interleave whole lines. Under `refuse` each attempt is a `refused` line and counts as refused, never
as zero (`layer-roles.md:549-550`).

### What it does not check

- A hook process killed before its catch runs (resource exhaustion, a timeout) records nothing; below
  2.1.295 that call runs unrecorded. The stall recorder and Runtime's breaker own that class.
- A PowerShell read, a `Glob`, and a `Grep` that lists files are no answered class, and run.
- A harness-route agent whose transcript the locator cannot find runs unjudged and unrecorded.
- A work order that hands nothing keyed is never matched.

### Inventory

Minted: `checkAnsweredCall`, `readWorkOrderText`, `readHandedSlices`, `checkStateCall`,
`readSessionCli`, `writeAnsweredCall`, `STATE_READERS` (JavaScript); `read_answered_calls` (Python);
the fragment `answered-calls.fragment.json`, the suite `answered-calls.test.sh`, the leg
`answered-calls self-test` and its `[[exempt_leg]]` declaration, the record directory `answered-calls/` under the git common dir, and the
deny prefix `BLOCKED by answered-calls:`. Each function name was asked of
`python tools/lexicon/lexicon.py --suggest <name> --as js.function` or `--as py.function` and
answered OK.

### Migration

Additive. A session with no work order is unjudged, so the main loop and any agent spawned without a
rendered handoff see nothing new. An adopter receives the fragment through `adopt-roles.sh
--scaffold` at its next update.

### Rollout

Live at landing, `refuse` by default as F3-2 settled. An owner who wants to observe first sets
`roles.answered-calls = record` in `.governance/policy.toml`.

### Files touched (estimate)

- `tools/roles/answered-calls.js`
- `tools/roles/answered-calls.fragment.json` (new)
- `tools/roles/answered-calls.test.sh` (new)
- `tools/roles/roles_lib.py`
- `tools/roles/kit.toml`
- `tools/roles/adopt-roles.sh`
- `tools/roles/README.md`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/check-wiring.sh`
- `.claude/settings.json`
- `tools/govkit/registry.toml` (the leg's declaration)
- `tools/gate-legs.json` (rendered by `leg_factory.py --write`, never edited)
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/selftest-budgets.txt`
- `help/roles.md`

### Alternatives rejected

- **The arm inside `scratch-guard.js`.** That hook's matcher holds no `Read` or `Grep`, its fail-open
  and fail-closed arms are per check, and the answered call is the roles layer's rule; a pack of its
  own keeps the matcher and the failure path this clause's.
- **Re-running any handed `cmd:` command at the call.** A hook that runs an arbitrary command on a
  match is an execution surface; `STATE_READERS` keeps it to read-only git.
- **Failing closed always.** That is `runtime.hook-failure`'s choice, and a defect here would block
  every role read.

## 5. Production-readiness checklist

- security — a new hook on every `Read`, `Grep` and `Bash` call: it writes only its own record under
  the git common dir, with both ids shape-checked before they reach a path; it runs no command but the
  four read-only git commands and the policy reader's `get`, each under a bound; it refuses only role agents, never the main loop.
- perf / scale — one node start per matched tool call; a transcript read and a blob hash only for a
  role agent; a policy read only on an answered call.
- error / empty / loading states — no work order, no marker or nothing keyed runs the call; a throw is
  S7's path, never silent.
- observability — every decision and every failure is one record line; the deny names the anchor and
  the key.
- risks — a refusal of a read the role truly needs: the partial-overlap and moved-blob rules make that
  read run, and `warn` or `record` turn the refusal off without a code change.
- testing — AC1 to AC11 by fixtures and probes a pass runs; the arms of §7 at the close.
- migration — none, per §4.
- user docs — `help/roles.md`, per S10.

## 6. Acceptance criteria

- **AC1** — When a `PreToolUse` payload with `agent_type` `gov-builder`, tool `Read`, the fixture's
  `a.txt` at `offset` 2 and `limit` 2, and a `transcript_path` whose agent transcript opens with a
  rendered work order handing `a.txt` lines 1 to 5 at its current blob is piped to
  `node answered-calls.js` in a fixture repository, it exits 2 with a deny naming the `input:` block
  and the key, and the session's record file gains one line whose `verdict` is `refused`.
  Red when: the hook allows the read, so a call the work order answers runs unbounded.
- **AC2** — When the AC1 payload carries `agent_type` `gov-skeptic`, whose index `verifies` is
  `claim`, and the range is handed under `### input:claim`, it exits 0 and no line is recorded; the
  same range handed under `### input:spec` is refused as AC1's is.
  Red when: a verifier is refused its subject, so its independence rests on the author's excerpt.
- **AC3** — When the AC1 payload reads lines 4 to 9 (a partial overlap), or `b.txt`, or carries no
  `agent_type`, or a transcript with no marker, each exits 0 with no record.
  Red when: a read the packet does not cover is refused, or the main loop is judged.
- **AC4** — When the fixture's policy file sets `roles.answered-calls` to `warn`, the AC1 payload
  exits 0 with one stderr line naming the anchor and records `warned`; set to `record`, it exits 0
  with no stderr and records `recorded`.
  Red when: the value is ignored, so `warn` still refuses.
  fixture: a scratch repository holding the policy kit, built by the pass under `%TEMP%`.
- **AC5** — When the fixture's `.claude/roles.json` is not valid JSON and the AC1 payload is piped
  with `AI_AGENT` set to `claude-code_2.1.292_x`, the hook exits 0 and records `hook-failed`; with
  `claude-code_2.1.308_x`, it exits 1 and records `hook-failed`.
  Red when: a crash below 2.1.295 admits the call with nothing on record.
- **AC6** — When the work order hands a `cmd:` fact for `git rev-parse HEAD` cut at the fixture's HEAD
  and a `Bash` payload runs that command, the hook exits 2; after a commit moves HEAD, it exits 0.
  Red when: a handed state value that no longer holds is still refused.
- **AC7** — When the work order holds a `### Method slices` block with a `#### ` heading for the
  fixture's `GUIDE.md` lines 10 to 20 and a `Read` of that file carries no `offset` and no `limit`, the
  hook exits 2 naming the slice's tag; the same block written in its `pointer` form exits 0.
  Red when: a whole method document is read while its slice is handed.
- **AC8** — When `python -c` calls `roles_lib.read_answered_calls` over the AC1 fixture's session, it
  returns one record holding the seven fields and `malformed` 0; after a non-JSON line is appended,
  `malformed` is 1; for the session id `../x` it raises naming the shape.
  Red when: the reader trusts a path built from an unchecked id.
- **AC9** — When `python settings-merge.py --fragment answered-calls.fragment.json` runs in the fixture
  and `bash check-wiring.sh --check` runs after it, the settings file holds a `PreToolUse` entry with
  matcher `Read|Grep|Bash` naming `answered-calls.js`, and check-wiring prints no `UNWIRED` line for it.
  Red when: the hook ships unwired, so no call is ever judged.
- **AC10** — When `grep -n 'roles.answered-calls' roles.md` runs in `help/`, it prints a line in the
  section "What the hooks refuse".
  Red when: a user meets the refusal with no page naming the key that turns it off.
- **AC11** — When `python tools/run-gates/leg_factory.py --check` runs it exits 0, and `--list` prints
  `answered-calls self-test` once, declared in `tools/govkit/registry.toml`; and `python -c` reading
  the rendered `tools/gate-legs.json` finds that row's `enforces` is `["principle.p29"]`. Where
  `leg_factory.py` is not built at the pass, the `python -c` read alone, with the hand edit recorded.
  Red when: the leg is written into the manifest beside its declaration, or carries no `enforces`.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `scratch-guard self-test` · `agent-cap self-test` · `hook destinations (every declared hook path ships)` · `hook destinations self-test` · `check-wiring self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `transition-audit arms` · `straggler-guard arms` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The leg `answered-calls self-test` is new in this unit and is not in the manifest at base, so it is
named here in prose.

New arm: tools/roles/answered-calls.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the planted refusal, verifier read, partial read, the two policy values, the crash at both versions, the moved HEAD and the whole-document read, staged by letting `checkAnsweredCall` treat every role as a non-verifier and every read as covered · none
New arm: tools/check-wiring.test.sh · covers AC9 · a fixture settings file lacking the answered-calls entry, staged by deleting the entry · none

## 8. Open questions

- **F1 — Who owns the answered-call hook: this build or dWellOiledMachine (brief D1)?**
  TOOL-dBoundRoles-13 §3 hands "the answered-call hook comparing a read with its handed key at the
  call" to dWellOiledMachine; clause `cl-dClosedLoop-0197` and v2's chain row give it to this build.
  RESOLVED (agent, 2026-10-26, delegated): this unit, rung 1, the carried clause. The disagreement is
  named in this writer's return for an ask in dBoundRoles' `BACKLOG.md`. widens: none · relaxes: none
- **F2 — What does the hook do with its own failure at or above CLI 2.1.295?** Options: (a) record and
  exit 0 at every version; (b) record, exit 0 below 2.1.295 and exit 1 at or above; (c) record and
  exit 2 at every version. (a) hides every failure from the CLI's `onFailure` switch, which a version
  at or above 2.1.295 honours; (c) is `runtime.hook-failure`'s choice, owned by dWellOiledMachine, and
  blocks every role read on a defect here. RESOLVED (agent, 2026-10-26, delegated): (b), rung 1,
  `layer-roles.md:331-333` ("there the rule holds while its hook runs, and a failure is recorded") and
  the catalogue's owner for the fail-closed key. widens: none · relaxes: none
- **F3 — Which answered classes does the hook judge?** Options: (a) the three item 10 names, reads,
  state and locate calls, and method documents; (b) reads alone. gap-roles-13 counts state, locate and
  method calls, which (b) leaves unseen. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1,
  `layer-roles.md:323-330`. widens: none · relaxes: none
- **F4 — Which state commands may the hook re-run?** Options: (a) the four read-only git commands of
  `STATE_READERS`; (b) any command a handed `cmd:` key names. (b) runs an arbitrary command inside a
  hook, an execution surface the tier did not price (veto 3). RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, the survivor. widens: none · relaxes: none
- **F5 — How does the hook recognise a handed slice?** TOOL-dFurnishedOrders-8 §4 "The block" renders
  `### Method slices` with a `#### <tag> — <path>:<lo>-<hi>` heading per slice under `handed` and a
  `- ` line under `pointer`, with no fact line. Options: (a) read those headings; (b) ask unit 8 for a
  fact line on each slice. (b) changes a sibling's block for one reader. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, tie-broken by reuse of the block as unit 8 renders it; the edge is named in
  this writer's return for unit 8's reciprocal line. widens: none · relaxes: none
- **F6 — Is a verifier's exemption every handed read, or its subject's only?** Options: (a) a read
  under `### input:<name>` where the role's `verifies` names `<name>`; (b) every read by a role whose
  `verifies` is not `none`. (b) exempts a verifier re-reading its handed criterion, which the clause
  does not. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the clause's "a verifier's read of
  its subject". widens: none · relaxes: none
- **F7 — Where does the hook read `verifies`?** Options: (a) the role index `.claude/roles.json`,
  where TOOL-dFurnishedOrders-5 S4 has `render_roles_index` (`tools/roles/render_agents.py:207`) write
  it; (b) the role files, parsed by the hook. (b) makes a hook a second reader of the role grammar.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, tie-broken by reuse of the sibling's index
  field, read through `loadRoleIndex`. widens: none · relaxes: none
- **F8 — The parents and siblings this unit calls are unbuilt.** TOOL-dBoundRoles-5, -7, -13, -17 and
  -25 are specced and DEFERRED at `2193e25d`; TOOL-dFurnishedOrders-5, -8 and -14 precede this unit.
  RESOLVED (agent, 2026-10-26, delegated): this spec calls them as their specs name them; the build
  run re-grounds on each and stops the unit if a cited section is still absent then, rung 1 (the
  brief's chain rule). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 6, the brief's J12 and D1, scout A's row
  for cl-0197, `layer-roles.md` `[trust]` item 10 and F3-2, `layer-runtime.md:175-185`, and the source
  at `2193e25d`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dFurnishedOrders-23, TOOL-dFurnishedOrders-29, promoted from the round-1 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`); nothing else moved.
- rev-3 · 2026-10-28 · §2 S5, S9; §3 Edges; §4 The decision, Inventory, Files touched; §5; §6 AC11 (new);
  §10 · re-grounded on the parents at `1a61f21a2` by the cross-check record
  `memory/builds/dFurnishedOrders/build/2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck.md`,
  rows 26 and 27.

## 10. Reuse audit

The seams extended: scratch-guard's role-agent payload handling and fail-closed wrap (`main`,
`tools/hooks/scratch-guard.js:1529`), `loadRoleIndex` (`:952`) and `resolveCommonDir` (`:652`), all
exported (`:1615`); the marker parse `extractHandoffMarker` (`tools/hooks/agent-cap.js:1626`);
the policy reader's CLI (`tools/policy/policy-mirror.js:160-186`), spawned as KICK-dKeptSession-8 S5
spawns it rather than `require`d as `readWriterBound` does (`tools/hooks/agent-cap.js:466-469`); the
leg factory's `new --exempt` (TOOL-dWitnessedBar-11 S3) for S9's declaration; the `AI_AGENT` rule (`skills/session-kickoff/manifest-check.sh:406-415`),
which the driver also reads (`read_cli_version`, `tools/unattended/unattended.sh:8936`); the fragment
shape of `tools/memory-recall/recall-opened.fragment.json`; and the transcript locator
TOOL-dBoundRoles-7 S4 specs, extracted here at its second caller.
`python tools/codebase-map/reuse_lookup.py "a PreToolUse hook that refuses a role agent's call its work
order already answers"` ranked name stems (`RolesError`, `load_roles`, `loadRoleIndex`,
`derive_tool_class`); no hook reads `Read` or `Grep` before the call (the only `Read` hook is the
observing `PostToolUse` `recall-opened.js`), so the pack is new. Scout A cited the driver's
`read_cli_version` at `:7732`, which is its call site in preflight; its definition is at `:8936`. The
recall probe returned the brief's rows, scout A's row, and the skeptic brief and walk records quoting
item 10's exemptions and its 2.1.295 clause, none disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "what does the answered-call hook refuse and how is a hook failure recorded below the fail-closed CLI version" --terms "answered-calls refuse warn record verifier subject hook failure onFailure 2.1.295 fail open PreToolUse"`
