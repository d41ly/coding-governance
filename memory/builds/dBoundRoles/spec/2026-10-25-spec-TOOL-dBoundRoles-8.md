# TOOL-dBoundRoles-8 — the role-gate arm's field escape explained and closed

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 12 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0173@a66af889 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-c.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-7 TOOL-dBoundRoles-9 TOOL-dBoundRoles-16 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-25 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-9 |

<!-- /gen:spec-records -->

## 1. Goal

gap-orient-09's first half reads: "the role-gate arm let 34 typed gate runs through though a replay
of the same commands is refused, cause unknown" (`research-orientation-determinism.md:56-60`). This
unit records the cause the replay probe of §8 F1 convicts, and closes the one exit through which a
typed role can still run a gate unrefused, the `checkRoleGate` step that returns before rows G2 and
G3 when no checkout root resolves (§8 F2).

## 2. Scope (IN)

- **S1** — The convicted exit closed. `resolveRoleRoot(cwd, env)` (`tools/hooks/scratch-guard.js:1396`)
  takes the candidate commands as a third start: after the payload `cwd` and `CLAUDE_PROJECT_DIR`, the
  directory of each candidate's launched script, resolved against the payload `cwd`, so a gate run by
  absolute path from outside every checkout reads the index of the checkout that holds the script.
  When no start resolves, `checkRoleGate` (`scratch-guard.js:1421-1451`, its step 3 at `:1430-1433`)
  no longer returns: rows G2 and G3, which read no index, refuse a matching candidate with an empty
  allowlist, and only G1 is unarmed, with its witness line. Observed by AC1, AC2 and AC3.
- **S2** — Agent-cap's rule 6 reads its root through the same `resolveRoleRoot`, which it already
  imports (`tools/hooks/agent-cap.js:2278-2280`); it passes no candidates, so its verdict is unchanged.
  Observed by AC3.
- **S3** — The explanation, where the arm is documented: `tools/hooks/README.md`'s section
  "scratch-guard's fourth check" (`:491`) and the role-arm paragraph of scratch-guard's header
  (`scratch-guard.js:105-130`) state the field measurement's result: the counted runs were commands
  naming a gate script as an argument, which the arm correctly admits, and a field census of role gate
  runs replays the recorded commands through the exported `checkRoleGate` and `scanCommandHeads`
  rather than a regex of its own. The evaluation-order comment states S1's new start. Observed by AC4
  and AC5.

## 3. Non-goals (OUT)

- The `none` and `review` write classes, gap-orient-09's second half: TOOL-dBoundRoles-9.
- Shell writes, which this arm never judged: TOOL-dBoundRoles-7.
- An absent index in a governed tree: TOOL-dBoundRoles-6 refuses it at step 4 of this same function,
  before this unit's order; S1 leaves that step as unit 6 leaves it.
- A gate reached through an interpreter, an alias, a function or an assembled path: the arm's stated
  textual ceiling (`tools/hooks/README.md`, "Its ceiling"), unchanged.
- Editing the gap register or the research record: both are frozen design inputs (packet Non-goals);
  the explanation lands in the kit's own docs and in §8 here.

### Edges

none

## 4. Design

### What the replay found

The probe of §8 F1, run on 2026-10-25 over the subagent transcripts under `~/.claude/projects/`
(10262 subagent files; the surviving corpus opens at 2026-10-13T20:59Z):

| Reading | Count |
|---|---|
| Bash calls by a `gov-*` agent after the arm, matching the research's regex for a gate script anywhere in a segment | 2634, 10 refused |
| of those before 2026-10-15, at "command position" by a quote-unaware split and assignment-blind head | 35 (spec-writer 20, builder 8, spec-reviewer 4, skeptic 3), 0 refused |
| the same 1019 pre-2026-10-15 commands replayed through `scratch-guard.js` at each one's commit, `agent_type` and a checkout `cwd` set | 1018 admitted, 1 refused |
| commands whose shell-tokenized head, past assignments, launchers and redirections, is a gate script | 3, all `gov-diff-reviewer` on 2026-10-19, all 3 refused in the field |

The 35 match the research's 34 in shape and role mix: `f=tools/roles/adopt-roles.test.sh && sed -n …`,
`grep -E 'serve.sh|run-gates.sh|await.sh'` split inside its quotes, `sed -n 5p <x>.test.sh`. None runs
a gate; the arm's scanner reads the blanked view (`buildCommandView`, quote-aware) and admits each.
The cause is the measuring predicate, not the arm. Scout C's hypothesis, that runs between
`3a40e7daf` (2026-10-12 02:22) and `791ee13e5` (21:37) armed nothing, cannot be tested: no transcript
of that window survives.

### The exit the reading convicts

```
checkRoleGate('bash C:/projects/coding-governance/tools/run-gates/run-gates.sh',
              { agent_type: 'gov-builder', cwd: '<a directory in no checkout>' }, {})   -> null
checkRoleGate(<the same .test.sh run>, <the same payload>, {})                          -> null
checkRoleGate(<the same command>, { agent_type: 'gov-builder', cwd: '<gov checkout>' }, {}) -> deny, G2
```

Measured on 2026-10-25 through the exported function. A role agent whose working directory is outside
every checkout, with `CLAUDE_PROJECT_DIR` unset, runs the bar or a suite unrefused; with it set to a
directory in no checkout, it gets a witness line and runs.

### The new step 3

1. `top = resolveRoleRoot(cwd, env, cands)`: the payload `cwd`, then `CLAUDE_PROJECT_DIR`, then each
   candidate's launched script's directory, the first that resolves a toplevel.
2. `top` resolved: steps 4 to 7 as today.
3. `top` unresolved: each candidate is tried against G2 and G3 with an empty allowlist; a match
   refuses naming the row and saying no checkout root was found; otherwise one witness line names the
   three starts and that G1 is unarmed.

### Inventory

Minted: the third parameter of `resolveRoleRoot`; the refusal and witness lines of the new step 3.
Naming cells: none new; `resolveRoleRoot` keeps its name.

### Migration

None: a run inside a checkout is judged as today. A role agent running a gate from outside every
checkout is now refused, which is the rule.

### Rollout

Live at landing on the `scratch-guard self-test` leg's hook.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/agent-cap.js` (the shared call, S2)
- `tools/hooks/README.md`

### Alternatives rejected

- **Refuse every candidate when no root resolves.** G1 needs the manifest a root names; refusing a
  leg nobody can identify would refuse reads the textual match mistakes for runs.
- **A census tool in the kit.** The exported `checkRoleGate` already is the predicate; S3 names it as
  the instrument, and a second classifier is the defect the research's regex was.

## 5. Production-readiness checklist

- security — narrows: a typed role's gate run from outside a checkout is refused.
- perf / scale — one more toplevel walk per candidate, only when the first two starts fail.
- error / empty / loading states — an unresolved root now prints a witness naming three starts, and
  still refuses G2 and G3.
- observability — the refusal says no checkout root was found and names the row.
- risks — an adopter's own typed agent running a bar script outside every checkout is refused; the
  rule is that typed agents run no gate.
- testing — AC1 to AC5 by a pass through the exported function and planted payloads; the arm of §7 at
  the close.
- migration — none.
- user docs — none owed: no page under `help/` describes the role-gate arm; the hooks README changes
  by S3.

## 6. Acceptance criteria

- **AC1** — When `node -e` calls the exported `checkRoleGate` with a command running the bar runner by
  an absolute path outside every checkout, `agent_type` `gov-builder`, a `cwd` in no checkout and no
  `CLAUDE_PROJECT_DIR`, it returns a deny naming `G2 runner`.
  Red when: step 3 returns null before G2, as it does at base.
- **AC2** — When the AC1 call runs a shell suite script by absolute path instead, it returns a deny
  naming `G3 suite`; with `--help` appended it returns no deny.
  Red when: G3 is skipped with no root, or refuses an admitting word.
- **AC3** — When the AC1 call names a script inside a scratch adopter whose `.claude/roles.json` is
  not JSON, it returns a deny naming that index, and agent-cap's rule 6 for an `Agent` payload with the
  same outside `cwd` keeps its base verdict.
  Red when: the script's checkout is not read, so the broken index refuses nothing.
- **AC4** — When `node -e` calls `checkRoleGate` with `gov-builder` inside a checkout on each of three
  field shapes, a suite path assigned to a variable and read with `sed`, a `grep -E` whose quoted
  alternation names the bar runner, and a `sed` read of a suite file, each returns no deny.
  Red when: the arm refuses a read that only names a gate script, the false positive the explanation
  rules out.
- **AC5** — When `grep -n 'checkRoleGate' README.md` runs in `tools/hooks/`, the role-gate section
  names the replay through the exported function as the census instrument and states the three root
  starts.
  Red when: the section still reads "neither resolving adds no arm".

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 AC4 · a gov-builder payload running the bar runner and a suite by absolute path from a directory in no checkout · none

## 8. Open questions

- **FACT-QUESTION · F1 — Why did the field count 34 typed gate runs that passed while a replay refuses
  the same shapes (D5)?** Probe: every Bash call of a `gov-*` subagent in `~/.claude/projects/*/*/subagents/**`
  after `3a40e7daf`, its recorded command replayed through `scratch-guard.js` as of the last commit
  touching it before the call, in a scratch checkout carrying that commit's index and manifest, with
  the recorded `agent_type` and a checkout `cwd`; and each command shell-tokenized to its true head.
  Observation, 2026-10-25: the research-shaped predicate yields 35 runs before 2026-10-15, none with a
  gate script at its head; 1018 of the 1019 window commands are admitted by the arm at their commit;
  the only 3 true gate runs in the corpus were all refused in the field. Liveness: the probe finds
  refused true runs, so it can show an admitted one; it saw none. RESOLVED (agent, 2026-10-25,
  delegated): the cause is the measuring predicate, which split segments inside quotes and read an
  assignment or an argument as a launched script; no arm exit let a true run through in the surviving
  corpus, rung 2. widens: none · relaxes: none
- **FACT-QUESTION · F2 — Does a silent exit of `checkRoleGate` still admit a true gate run?** Probe: the
  exported `checkRoleGate` over planted payloads, one per early return (no `agent_type`, no candidate,
  no root, absent index). Observation, 2026-10-25: with no root resolved it returns null for the bar
  runner and for a `.test.sh` suite, while the same command from a checkout is denied (§4). Liveness:
  the in-checkout control denies, so the probe can tell an admitted run from a refused one. RESOLVED
  (agent, 2026-10-25, delegated): the no-root exit is convicted and closed by S1; the no-`agent_type`
  exit is the main loop's by design, and the absent-index exit is TOOL-dBoundRoles-6's, rung 2.
  widens: none · relaxes: none
- **F3 — How is the convicted exit closed?** Options: (a) the script's own checkout as a third root
  start, and G2 and G3 binding when nothing resolves; (b) G2 and G3 binding with no root, no third
  start; (c) refuse every candidate when no root resolves. (b) leaves a G1 leg run by absolute path
  from outside unread when its checkout's index would refuse it; (c) refuses reads the textual match
  mistakes for runs. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most feature-rich
  survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 8, the brief's D5, scout C's row for
  cl-0173, and the replay probe run over the transcript corpus and the source at `4283cb44`.

## 10. Reuse audit

The seams extended: `checkRoleGate` (`tools/hooks/scratch-guard.js:1421-1451`) and `resolveRoleRoot`
(`:1396`), both exported and already shared with agent-cap's rule 6; `scanCommandHeads` (`:1279`) and
`buildCommandView`, the quote-aware scanner the explanation names as the census instrument. The probe
itself reused the exported functions, as scout C proposed for the replay, and not the transcript
readers in `handoff.py`, which read agent records rather than tool calls. `python
tools/codebase-map/reuse_lookup.py "replay recorded role agent shell commands through the gate arm"`
ranked the selftest harnesses' `arm` and `run_arms` helpers and `gotchas.py`'s `records`, none a
replay of tool calls through a hook; the exported hook functions are the seam. The recall probe
returned scout C's row with its window hypothesis, which §4 records as untestable on the surviving
corpus.

Recall terms used: `python tools/memory-recall/query.py "why did typed role gate runs pass the
role-gate arm in the field" --terms "role-gate arm field escape agent_type checkRoleGate replay typed
gate runs CLAUDE_PROJECT_DIR resolveRoleRoot"`
