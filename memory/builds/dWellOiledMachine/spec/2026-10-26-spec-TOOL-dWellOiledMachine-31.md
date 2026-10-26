# TOOL-dWellOiledMachine-31 — a hook pack's refusal text: its rule, remedy and actor declared in the pack contract and checked at registration

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 12 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0309@3da1a616 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-48 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

A hook's remedy is typed ad hoc inside each deny string and nothing checks it: three guards name
remedies their target cannot perform (gap-roles-31), and no reader can tell which rule refused a call.
The night pass's point 6, S5, gives each hook pack's contract its refusal text, naming the rule and
the remedy, checked at registration (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:405-406`).
This unit declares that text in the pack contract (I9) as the refusal fields (I11), refuses a pack
whose declaration is missing or malformed when it registers, and makes every refusal the dispatcher
emits name its rule, its remedy and the remedy's actor from that declaration.

## 2. Scope (IN)

- **S1** — The refusal fields (I11), a `refusal` list in the pack contract of every pack whose `class`
  is `refuse`: one object per rule the pack enforces, `rule` (`^[a-z][a-z0-9-]*$`, unique in the pack),
  `remedy` (one line, 1 to 200 bytes, no control byte) and `actor`, one of TOOL-dBoundRoles-26 S1's
  set: `self`, `producer`, `driver`, `owner` or `build:<slug>`, the slug slug-shaped. A pack of class
  `warn` or `record` carries no `refusal`. Observed by AC1.
- **S2** — Checked at registration. `load_fragment` (`tools/settings-merge.py:252`), through which
  `--resolve-pack` and every render read a pack, refuses a `refuse` pack with no `refusal`, an empty
  list, a missing or malformed field, an actor outside the set, a repeated rule, and a `refusal` on a
  `warn` or `record` pack, each exit 2 naming the file, the rule and the field. A refused pack renders
  no table row, so it never reaches the dispatcher. The built-in `AGENT_CAP` (`:231-241`) is graded
  by the same function. Observed by AC1.
- **S3** — The rule named at refusal. A refusing pack ends its deny reason, stderr on exit 2 or the
  `reason` of a `{"decision":"block"}` object, with one line `rule — <rule>`. The dispatcher
  (`dispatch.js`, TOOL-dWellOiledMachine-10 S2) strips that line, looks the rule up in the pack's table
  row, and ends the reason it emits with the line
  `refusal — <pack> · rule <rule> · actor <actor> · remedy <remedy>`. A refusal with no rule line, or
  naming a rule the pack does not declare, is a failed pack under TOOL-dWellOiledMachine-10 S6, so
  under `runtime.hook-failure` `closed` the call is still refused, by the dispatcher's own line. The
  deny prefix `BLOCKED by <pack>:` on each pack's first line is kept. Observed by AC2.
- **S4** — Both ways at registration, an arm of check-wiring's `check_packs`: every rule a pack
  declares is spelled as a `rule — <rule>` literal in the pack's hook source, and every such literal in
  a hook source names a rule declared by a refusing pack whose hook is that file, so scratch-guard's
  `record` pack at `SubagentStart` shares its file without declaring; either miss is red, naming the
  pack and the rule. It prints
  `<n> refusal rule(s) over <m> refusing pack(s)`, and a population of zero is `unarmed`. Observed by
  AC3.
- **S5** — Today's refusing packs declared, each site naming its rule, from the inventory of §4: the
  five packs that refuse at this base and their 27 refusal sites. Each `remedy` is the one-line remedy
  the site's text already gives, and an `actor` other than `self` is the actor that site's remedy
  names. Observed by AC3, AC4.
- **S6** — The page `help/runtime.md` gains how a pack declares a refusal, the actor set, the
  `refusal —` line and what registration refuses. Observed by AC5.

## 3. Non-goals (OUT)

- Moving the refusal texts into templates: TOOL-dWellOiledMachine-21, which reads S1's fields and
  S3's line.
- Counting refusals per rule and routing an act to the remedy's actor: TOOL-dWellOiledMachine-49,
  `runtime.refusal-repeats`, which reads S3's line.
- Judging whether a declared remedy is one its actor can perform, or one another guard refuses: a
  semantic question no registration check can answer. S1 types the actor; the reviewer reads the
  remedy.
- The refusal arm of a role's return: TOOL-dBoundRoles-26's, whose field names and actor set S1
  reuses.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-10` — `dispatch.js`, whose refusal output S3 ends with the declared line, and the pack contract and `check_packs`, which S1 and S4 extend
- **hands-off** `TOOL-dWellOiledMachine-21` — `refusal`, the declared rule, remedy and actor that the hook-message templates fill and render
- **hands-off** `TOOL-dWellOiledMachine-49` — `refusal`, the `refusal —` line carrying the rule the breaker counts and the actor it routes to

## 4. Design

### Evidence

- Deny strings carry the prefix `BLOCKED by <hook>:` at 25 sites: 13 in `tools/hooks/scratch-guard.js`,
  9 in `tools/hooks/agent-cap.js`, 3 in `tools/unattended/gate-guard.js`; `stop-guard.js:193` and
  `format-guard.js:547` block a stop through `{decision:'block', reason}` (`git grep -c "BLOCKED by"`).
- The only typed remedy constant is the policy guard's `REMEDY` (`tools/policy/guard.py:41`).
- TOOL-dBoundRoles-26 S1 types a role's refusal as `rule`, `remedy` and `actor` with the actor set this
  unit reuses, and its §3 leaves the hook packs' refusal text to Runtime.
- A pack verdict reaches the dispatcher as exit 2 with stderr or as a JSON object
  (TOOL-dWellOiledMachine-10 §4 "The decision, per event shape").

### The contract, by example

```json
{"name": "gate-guard", "event": "PreToolUse", "matcher": "Bash|PowerShell|AskUserQuestion",
 "marker": "gate-guard.js", "hook_path": "{kit}/unattended/gate-guard.js",
 "owner": "unattended", "class": "refuse", "failure": "closed", "budget-ms": 2000, "key": "none",
 "refusal": [
   {"rule": "gate-shapes", "remedy": "leave the bar to the run's own gate stage", "actor": "self"},
   {"rule": "run-lease", "remedy": "resume the run through unattended.sh --resume", "actor": "self"}]}
```

### The inventory of today's refusal sites

| Pack | Sites (line at base) | Rule |
|---|---|---|
| scratch-guard | `:547` | `scratch-root` |
| scratch-guard | `:739` | `orientation-card` |
| scratch-guard | `:932` | `routed-path` |
| scratch-guard | `:1050`, `:1066` | `role-writer` |
| scratch-guard | `:1122`, `:1126` | `payload-target` |
| scratch-guard | `:1152`, `:1160` | `write-gate-conf` |
| scratch-guard | `:1383`, `:1439` | `role-gate` |
| scratch-guard | `:1555`, `:1604` | `guard-threw` |
| agent-cap | `:1475` | `spec-audit-optin` |
| agent-cap | `:1663` | `harness-call` |
| agent-cap | `:1785`, `:1789`, `:1794`, `:1896` | `settings-in-force` |
| agent-cap | `:1930` | `script-unreadable` |
| agent-cap | `:1943` | `verifier-fanout` |
| agent-cap | `:1961` | `review-join` |
| gate-guard | `:674` | `gate-shapes` |
| gate-guard | `:745`, `:746` | `run-lease` |
| stop-guard | `:193` | `run-open` |
| format-guard | `:547` | `micro-format` |

The rule names are this unit's; the pass asks each of
`python tools/lexicon/lexicon.py --suggest <rule> --as tag` and the table is re-derived at the pass by
`git grep -n "BLOCKED by\|decision: 'block'"` over the five sources, since a line number is PINNED at
this base and moves with any edit above it.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `refusal`, with `rule`, `remedy`, `actor` | pack contract field | every `refuse` pack's fragment, `AGENT_CAP` |
| `rule — <rule>` | the pack's last reason line | five hook sources |
| `refusal — <pack> · rule <rule> · actor <actor> · remedy <remedy>` | the dispatcher's last reason line | `tools/runtime/dispatch.js` |
| `REFUSAL_ACTORS`, `check_refusal_fields` | constant, function | `tools/settings-merge.py` |
| the refusal arm of `check_packs` | arm | `tools/check-wiring.sh` |

### Migration

Additive: the S5 declarations and rule lines land with the check, so no tracked pack is refused at
this unit's landing. An adopter's own refusing pack without the fields is refused at its next render,
naming the field, which is the point of a registration check; the help page says how to add them.

### Files touched (estimate)

- `tools/settings-merge.py`
- `tools/check-wiring.sh`
- `tools/check-wiring.test.sh`
- `tools/runtime/dispatch.js`
- `tools/runtime/dispatch.test.sh`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.fragment.json`
- `tools/hooks/agent-cap.js`
- `tools/hooks/format-guard.js`
- `tools/hooks/format-guard.fragment.json`
- `tools/unattended/gate-guard.js`
- `tools/unattended/gate-guard.fragment.json`
- `tools/unattended/stop-guard.js`
- `tools/unattended/stop-guard.fragment.json`
- `help/runtime.md`

### Alternatives rejected

- **The rule as a JSON field of the pack's output.** Every exit-2 pack would switch output shape; the
  reason's last line works for both shapes the harness reads.
- **Remedy text kept only in the source.** The registration check could not read it, and the
  dispatcher could not name it uniformly.

## 5. Production-readiness checklist

- security — a refusal whose rule is undeclared still refuses under `closed`; the remedy line is
  data from a tracked fragment, capped at 200 bytes and refused with a control byte.
- perf / scale — one table lookup per refusal; nothing on the admit path.
- error / empty / loading states — a malformed declaration refuses the pack at render, naming the field;
  zero refusing packs prints `unarmed`.
- observability — every refusal ends with one `refusal —` line naming rule and actor.
- risks — a pack edit that renames a rule without its declaration fails closed until both agree.
- testing — the fixture cases under AC1 to AC4 and the arms in §7.
- migration — §4 Migration.
- user docs — `help/runtime.md`, S6.

## 6. Acceptance criteria

- **AC1** — When `python settings-merge.py --resolve-pack` reads planted fragments of class `refuse`
  with no `refusal`, with an actor `boss`, with a remedy carrying a newline, with a rule repeated, and
  a `warn` fragment carrying `refusal`, each exits 2 naming the file and the field; a well-formed one
  prints its rules.
  Red when: any of the five planted fragments resolves.
- **AC2** — When `node dispatch.js PreToolUse` runs a planted refusing pack whose reason ends
  `rule — scratch-root`, the emitted reason ends `refusal — <pack> · rule scratch-root · actor self ·
  remedy <remedy>` and keeps its `BLOCKED by <pack>:` first line; with `rule — nope` the call is
  refused by `BLOCKED by dispatch:` naming the undeclared rule under `runtime.hook-failure = "closed"`.
  Red when: an undeclared rule's refusal passes as the pack's own, or the declared line is missing.
- **AC3** — When `check-wiring.sh` runs over the tracked packs, `check_packs` prints `18 refusal
  rule(s) over 5 refusing pack(s)`; a planted declaration whose rule no source line spells, and a
  planted source line naming an undeclared rule, each red.
  Red when: either one-sided miss reads green.
  figure: 18 and 5 are DERIVED from §4's inventory and re-derived at the pass.
- **AC4** — When `git grep -c "rule — "` runs over the five hook sources, each refusal site of §4's
  inventory carries one; and when one planted payload per rule is fed to its pack's hook on stdin,
  every emitted reason opens `BLOCKED by <pack>:` and ends `rule — <rule>`.
  Red when: a refusal site names no rule, or a deny loses its prefix.
- **AC5** — When `grep -n "refusal —" runtime.md` runs over the runtime kit's help page, it finds the
  line's shape and the five actors.
  Red when: the page omits the shape or an actor.

## 7. Gates

`settings-merge selftest` · `check-wiring self-test` · `govkit selftest` · `policy fixtures` · `format-guard self-test` · `transition-audit arms` · `straggler-guard arms` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `unattended kit gate` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/runtime/dispatch.test.sh · covers AC2 · a declared and an undeclared rule line, staged against a dispatcher that passes the pack's reason through · none
New arm: tools/check-wiring.test.sh · covers AC1 AC3 · five malformed declarations and both one-sided misses, staged against the base reader, which reads no `refusal` · none

## 8. Open questions

- **F1 — One refusal per pack, or one per rule?** (a) A list, one object per rule; (b) one object per
  pack, as I11's proposed spelling reads. (b) cannot carry scratch-guard's eight rules or agent-cap's
  six, so a pack would name one remedy for refusals with different remedies. Rung 3, the most capable
  option; I11's owner refines the spelling. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none ·
  relaxes: none
- **F2 — How does a pack name the rule it refused under?** (a) A last reason line `rule — <rule>`,
  stripped by the dispatcher; (b) a JSON field in the pack's output. (b) changes the output shape of
  every exit-2 pack and of none of the JSON ones. Rung 3. RESOLVED (agent, 2026-10-26, delegated):
  (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended are TOOL-dWellOiledMachine-10's pack contract, its reader `load_fragment`
(`tools/settings-merge.py:252`) and its `check_packs` arm, the dispatcher `dispatch.js`, and
TOOL-dBoundRoles-26 S1's `rule`, `remedy` and `actor` with its actor set, reused rather than
re-spelled. The probe `python tools/codebase-map/reuse_lookup.py "validate a hook refusal reason
naming its rule remedy and actor at registration"` ranked `refusal` (`tools/memory-recall/recall_conf.py`)
and `Refusal` classes by name stem: each is a module's own exception type, not a hook contract, so no
existing seam fits the declaration beyond the two above. Scout B's counts (agent-cap 9, scratch-guard
13, gate-guard 3) hold at this base; its `guard.py:41 REMEDY` is a constant inside one guard and
stays its own.

Recall terms used: `python tools/memory-recall/query.py "where is a hook refusal's rule and remedy
declared and checked" --terms "refusal remedy actor rule deny BLOCKED hook pack contract registration
fragment"`
