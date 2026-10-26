# TOOL-dBoundRoles-12 — the orientation scout's placement return through the typed channel, recorded and checked by the driver

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 20 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0177@4a09db23 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-17 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 |

<!-- /gen:spec-records -->

## 1. Goal

Placement is the one judgment left at entry, and it is the orientation scout's, never the driver's:
the driver reads state only (`driver.reads`, v2:1179) and records what the scout returned (the flow
items research, `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-a.md:97`).
TOOL-dPlacedRequest-4 specs the disposition grammar, the record and `placement.check`; nothing makes
the record rest on a return the orientation scout actually produced in that shape. This unit binds the
scout's placement return to the typed return channel, so a return missing a key or answering another
role's work order is refused before it is recorded, and gives the attended driver its step: record the
return, then run `placement.check`.

## 2. Scope (IN)

- **S1** — The orientation scout's return template. `gov-orienter`'s `return` field (shared interface
  I1, the field TOOL-dBoundRoles-2 adds) holds the placement block's four keys, `disposition`,
  `reason`, `evidence` and `observations`, spelled exactly as TOOL-dPlacedRequest-4 S3 and S4 spell
  them (I20), beside the card body the role already returns. The grammar is that unit's; this unit
  writes no key of its own. Observed by AC4.
- **S2** — The typed channel at the record. `place --return <file>` in `tools/loop/placement.py`
  (TOOL-dPlacedRequest-4 S1) calls `validate_return("gov-orienter", text)` (I16, TOOL-dBoundRoles-5)
  before it reads a key, the function located through `resolve_kit_dir("roles", "roles_lib.py",
  here)`. A refusal prints each of `validate_return`'s lines under `placement: refused — return —`,
  exits 1 and appends no block. Observed by AC1.
- **S3** — The return answers an orientation work order. The work order the return answers, as
  `validate_return` reads its `answers` value (I14), carries a marker whose `role` is `gov-orienter`,
  read through `MARKER_RE` (I5). A return answering any other role's work order, or one whose answered
  file carries no marker, is refused naming the role it found, so no other role and no driver-typed
  text becomes an `agent` placement. Observed by AC2.
- **S4** — The driver's step. The `/build` Skill's "Stage 1 — orient" (`tools/roles/SKILL.template.md:34-36`,
  rendered at `.claude/skills/build/SKILL.md`) states it: when the orientation scout returned a
  placement, the driver writes the return to the request's file, runs `placement.py place --request
  <content key> --return <file>`, then `placement.py check --request <content key>`, and acts only on a
  check that passes; a refusal of either routes back to orientation, never to the driver's own
  placement. Observed by AC3.
- **S5** — `help/roles.md`, "How a task reaches an agent", gains one step after kickoff naming the
  scout's placement return and the driver's record and check. Observed by AC5.

## 3. Non-goals (OUT)

- The disposition set, the record block, `place`, `check`, the `placement` and `placement.check` keys
  and their values: TOOL-dPlacedRequest-4's and TOOL-dDeclaredLoop-16's, called here.
- The entry items and their bodies: TOOL-dPlacedRequest-3's rows. `item.entry.place`'s body is `place`,
  so the binding of S2 reaches the loop's route with no row changed.
- The unattended prompt path: TOOL-dPlacedRequest-4 S9's `check_prompt_placement` already places and
  checks there through the same `place`, so S2 covers it.
- The retry of a refused direct-spawn return under `roles.retries`: TOOL-dBoundRoles-5's SubagentStop
  check. The driver re-spawns the scout; this unit retries nothing.
- `validate_return`, `answers` and the marker grammar: TOOL-dBoundRoles-5's, -17's and -17's.
- The orienter's rename and its definition file's other fields: TOOL-dBoundRoles-1's and -2's (D6 keeps
  the stem `gov-orienter`).

### Edges

- **consumes-from** `TOOL-dBoundRoles-5` — `validate_return`, the one checker of a role's return against its `return` template; without it the placement record rests on untyped text
- **consumes-from** external — TOOL-dPlacedRequest-4's `tools/loop/placement.py` with `place --return` and `check`, and its record block, specced and unbuilt at base `4ed9e567`
- **hands-off** `TOOL-dBoundRoles-43` — the orientation return and the driver's placement step, which unit 43 spells in full and binds to the scout's transcript (ids 14 and 64 of the round-1 spec audit)

## 4. Design

### Where the binding lives

Every route that records an `agent` placement goes through `placement.py place --return`: the loop's
`item.entry.place` names it as its body (TOOL-dPlacedRequest-3 §4, the item table), and the unattended
prompt path places through it (TOOL-dPlacedRequest-4 S9). Putting the check inside `place` is one call
site for every route, the charter's one-core rule, where a wrapper verb in the roles kit would leave
the item body and the prompt path unbound.

```
place --request <key> --return <file>
  1. text = read <file>
  2. lines = roles_lib.validate_return("gov-orienter", text)       # I16, unit 5
     lines non-empty            -> "placement: refused — return — <line>" each; exit 1
  3. answered = the work order `answers` names                     # I14, read as validate_return reads it
     MARKER_RE over answered    -> role != gov-orienter, or no marker
                                -> "placement: refused — return — answers a <role> work order"; exit 1
  4. TOOL-dPlacedRequest-4 S1: read the block, resolve the disposition, append, as specced
```

The loop kit locates the roles library the way every kit locates a sibling,
`resolve_kit_dir` (`tools/roles/roles_lib.py:96-133`, carried inline in each kit by the
`resolve_kit_dir` parity row), and imports nothing by a typed path. Where the roles kit is not
installed, `place --return` refuses naming the three places it looked: an untyped placement is the
gap this unit closes, so it never falls back to reading the block unchecked.

### Why the answered work order's role, and not the return's own claim

A return can say anything about who wrote it. The work order it answers is a rendered file whose
marker carries the role and a task-sha the spawn guard compared at spawn
(`tools/hooks/agent-cap.js:2135-2136`). Reading the role from there is reading a witnessed fact
rather than a claimed one, the [trust] classes' distinction
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md:240-248`).

### The driver's step

At base the `/build` Skill's Stage 1 says `/session-kickoff` ran orientation and nothing runs there
(`tools/roles/SKILL.template.md:34-36`). Kickoff's engine is not the place: it measures 18310 bytes
against its 18432-byte leg (`kickoff engine size <=18KiB`), PINNED at `4283cb44`, and the scout's
spawn is not a kickoff step today. Stage 1 gains three sentences: the two commands of S4 in order, that
the driver acts on a passing check only, and that a refusal of either routes back to the scout. The
Skill is rendered by the roles adopter, so the rendered copy is the template's.

### Inventory

Minted: the two refusal line shapes of §4 under `placement: refused — return —`, and the plants of §7's
arm, `return-untyped` and `return-wrong-role`. No function, key or file is minted.

### Migration

None at base: no placement record exists, since `tools/loop/` is unbuilt (scout B). A record written
before this unit lands, by TOOL-dPlacedRequest-4's own build, stays as written; only new `place` calls
are checked.

### Rollout

Live at landing on every `place --return`.

### Files touched (estimate)

- `tools/loop/placement.py` (the binding in `place`, the two plants)
- `tools/roles/agents/gov-orienter.agent.md` (its `return` field's four keys)
- `.claude/agents/gov-orienter.md` (its render, by `tools/roles/render_agents.py`)
- `.claude/roles.json` (re-rendered beside it)
- `tools/roles/SKILL.template.md` (Stage 1)
- `.claude/skills/build/SKILL.md` (its render, by `tools/roles/adopt-roles.sh`)
- `help/roles.md`

### Alternatives rejected

- **A wrapper verb in the roles kit**, `handoff.py` chaining validate, place and check. The loop's item
  body and the unattended prompt path call `place` directly and would stay unbound.
- **The step in kickoff's engine.** It has 122 bytes of headroom under its leg and does not spawn the
  scout today.
- **Trusting a `role:` line in the return.** It is a claim the return makes about itself.

## 5. Production-readiness checklist

- security — narrows a write path: `place` writes a placement block only from a typed return that
  answers an orientation work order, so a driver or another role cannot type an `agent` placement.
- perf / scale — one function call and one marker read per placement.
- error / empty / loading states — an absent roles kit, an unreadable answered file and an empty
  return each refuse naming the cause; nothing is recorded on any refusal.
- observability — every refusal prints under `placement: refused — return —`, the prefix
  TOOL-dPlacedRequest-4 already uses.
- risks — a scout spawned without a rendered work order has no `answers` target and is refused; that
  is the point, and the Skill's step names the render.
- testing — the plants of §7's arm and the probes of §6; the main loop observes the arm RED then GREEN
  at the close.
- migration — none, per §4.
- user docs — `help/roles.md` per S5; `help/loop.md`'s placement section is TOOL-dPlacedRequest-4's.

## 6. Acceptance criteria

- **AC1** — When `python placement.py --fixture --plant return-untyped` runs, its orientation return
  lacking `reason`, the plant's `place` exits 1 printing `placement: refused — return —` with the line
  `validate_return` gives for `reason`, and the request's `.placement` file holds no block; with
  `reason` restored the same plant appends one block and exits 0.
  Red when: `place` reads the block without calling `validate_return`, so the block is appended.
- **AC2** — When `python placement.py --fixture --plant return-wrong-role` runs, its return valid and
  answering a work order whose marker names `role=gov-researcher`, `place` exits 1 naming
  `gov-researcher`; re-pointed at a `role=gov-orienter` work order it is accepted.
  Red when: the role is read from the return's own text, or not read at all.
- **AC3** — When `grep -n "placement.py check" SKILL.template.md` runs in `tools/roles/`, it names
  Stage 1's step, after a line naming `placement.py place`, and the rendered
  `.claude/skills/build/SKILL.md` carries the same lines.
  Red when: Stage 1 still reads that nothing runs there, so no driver step records or checks the
  scout's return.
- **AC4** — When `validate_return("gov-orienter", text)` runs over today's card-only return, it
  refuses naming `disposition`; over a return carrying the card body and all four keys of
  `gov-orienter.agent.md`'s `return` field it returns no line.
  Red when: the template lacks a key, so a return without it validates.
- **AC5** — When `grep -n "placement.py" help/roles.md` runs, it names the step S5 adds.
  Red when: the page does not say the driver records and checks the scout's return.

## 7. Gates

The pass adds no leg: TOOL-dPlacedRequest-4's `loop placement fixtures` leg runs the placement plants,
and this unit's two join it.

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/placement.py · covers AC1 AC2 · the `return-untyped` and `return-wrong-role` plants, the failing case staged by removing the `validate_return` call from `place` · none

## 8. Open questions

- **F1 — Where does the typed-channel binding live?** Options: (a) inside `placement.py place --return`,
  one call site for every route; (b) a roles-kit wrapper verb the driver calls; (c) the driver's prose
  step alone. (b) leaves the loop's item body and the prompt path unbound; (c) binds nothing. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the most feature-rich survivor, every route bound.
  options: (a) > (b) > (c) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F2 — Where is the attended driver's step written?** Options: (a) the `/build` Skill's Stage 1;
  (b) kickoff's engine; (c) `help/roles.md` alone. (b) has 122 bytes of headroom under the `kickoff
  engine size <=18KiB` leg, measured at `4283cb44`, and would breach it; (c) is a page no driver reads as
  procedure. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, with the page of S5 beside it.
  options: (a) > (c) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F3 — `placement.py`, `validate_return` and `answers` are TOOL-dPlacedRequest-4's,
  TOOL-dBoundRoles-5's and TOOL-dBoundRoles-17's, all specced and unbuilt at base `4ed9e567`.** Options:
  (a) build against them as specced and re-ground at the build run; (b) restate them. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 1, the brief's rule; the build run re-grounds on each and stops this
  unit if one is still absent then. options: (a) > (b) · pick: (a) · admitted-by: principle.p18 ·
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 12, the brief's I14, I16 and I20, scout B's
  row for cl-0177, and TOOL-dPlacedRequest-3 and -4 at base `4ed9e567`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring the edges of TOOL-dBoundRoles-43, promoted by the round-1 spec audit of the 26 unit specs; nothing else moved.

## 10. Reuse audit

The seam extended is TOOL-dPlacedRequest-4's `place` verb in `tools/loop/placement.py`, specced and
DEFERRED, with TOOL-dBoundRoles-5's `validate_return` as the checker it calls; at base the only live
seams are the orienter's prose `returns:` line (`tools/roles/agents/gov-orienter.agent.md:11`) and the
`/build` Skill's empty Stage 1 (`tools/roles/SKILL.template.md:34-36`). `python
tools/codebase-map/reuse_lookup.py "validate a role agent return and record the placement disposition"`
ranked generic record helpers (`records`, `render_record`, `write_record` in `tools/runlog/record.py`)
and the roles library's `RolesError` and `load_roles`, none a return validator, which matches scout B: no
direct-spawn return is checked at base. The recall probe returned scout B's row, this build's brief row,
the flow items research's F1 ("the driver records it and runs `placement.check`") and the
dPlacedRequest brief; none disagreed with source. Scout B named `skills/session-kickoff/` as the driver
step's home; kickoff's size and its lack of a scout spawn moved it to the `/build` Skill (§8 F2).

Recall terms used: `python tools/memory-recall/query.py "how does the orientation scout return a placement disposition and the driver check it" --terms "orientation scout orienter placement disposition reason evidence placement.check return validate driver kickoff"`
