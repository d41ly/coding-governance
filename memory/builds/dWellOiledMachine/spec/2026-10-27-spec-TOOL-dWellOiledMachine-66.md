# TOOL-dWellOiledMachine-66 — refusal rows and rule lines for the act-binding and in-flight admission packs

**Status:** DEFERRED · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 37 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-66-deviation-661.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-66-deviation-661.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-79 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 5, item H3, at HIGH. TOOL-dWellOiledMachine-7 S5 declares the two act-binding packs and
TOOL-dWellOiledMachine-43 S2 the in-flight admission pack, all of class `refuse`, and neither declares
the `refusal` rows TOOL-dWellOiledMachine-31 S1 requires nor ends a deny with `rule — <rule>`. Unit 31
(order 12) refuses such a pack at render, so no act-binding pack is registered and
TOOL-dWellOiledMachine-10 S8 denies every gated call of an act session, the named Workflow call
included; registered anyway, each deny would count as a failed pack. This unit repairs both units,
which is why it sits after the later of the two, 43.

## 2. Scope (IN)

- **S1** — The act-binding rows. `tools/runtime/act-binding.fragment.json` and
  `act-binding-early.fragment.json` each carry a `refusal` list (31 S1), one row per rule of
  TOOL-dWellOiledMachine-7 S4 that answers `deny`:

  | rule | 7 S4 case | actor | remedy |
  |---|---|---|---|
  | `no-binding` | 1, binding absent or naming another act | `driver` | the supervisor relaunches the act, whose SessionStart writes its binding |
  | `stale-epoch` | 2, binding `not-local`, `malformed` or on another epoch | `driver` | the supervisor fences or relaunches under the held epoch |
  | `unnamed-call` | 4, a Workflow call that is not the named one, or repeated | `self` | call only the Workflow the work order names, once |
  | `agent-call` | 5, a main-loop `Agent` call | `self` | spawn agents only inside the named Workflow |
  | `shell-allow` | 6, a shell call no `allow` entry matches | `self` | use only the shell commands the work order allows |
  | `write-tool` | 7, a main-loop write tool in a Workflow act | `self` | write only from inside the named Workflow's role agents |

  Observed by AC1.
- **S2** — The act-binding rule lines. `act-binding.js` ends each deny it emits with
  `rule — <rule>` (31 S3), the rule of S1's table for the case that answered, keeping the first line
  `BLOCKED by act-binding: <rule> · <act> · <what differs>` (7 S4). Observed by AC2.
- **S3** — The admission row. `tools/runtime/inflight-admit.fragment.json` carries a `refusal` list of
  one row, `held-past-hold` (actor `driver`, remedy "the admission queue takes the call over and
  re-asks once a slot frees"), and `inflight.py admit` ends the deny TOOL-dWellOiledMachine-43 S3 emits
  past its hold with `rule — held-past-hold`. Observed by AC1, AC3.
- **S4** — Registration proved. `python settings-merge.py --resolve-pack` resolves each of the three
  fragments, and the rendered `.claude/hook-packs.json` lists all three. Observed by AC1.

## 3. Non-goals (OUT)

- No `remedy-call` field: TOOL-dWellOiledMachine-49 S7 adds it later and requires it on every `self`
  row; this unit's four `self` rows are handed to that unit (§3 Edges).
- No change to the decisions of 7 S4 or the hold of 43 S3: only the declared rows and the rule line
  are added.
- No message templates: a deny is rendered as 7 S4 and 43 S3 spell it, plus the rule line.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-7` — the act-binding packs and `act-binding.js`'s deny texts this unit gives refusal rows and rule lines
- **consumes-from** `TOOL-dWellOiledMachine-43` — the in-flight admission pack and its deny past the hold
- **consumes-from** `TOOL-dWellOiledMachine-31` — the `refusal` contract, its registration check and the dispatcher's `refusal —` line
- **hands-off** `TOOL-dWellOiledMachine-49` — this unit's four `self` rows (`unnamed-call`, `agent-call`, `shell-allow`, `write-tool`), each owed a `remedy-call` once 49 S7 requires one

## 4. Design

### Evidence

- 31 S2 refuses a `refuse` pack with no `refusal` list at `load_fragment`, so it renders no table row
  (`spec-31.md:34-39`); 31 S3 makes a refusal with no `rule —` line a failed pack
  (`spec-31.md:40-47`).
- 7 S5 declares both packs class `refuse` (`spec-7.md:66-73`) and its deny shape carries no rule line
  (`spec-7.md:65`); 43 S2 declares `inflight-admit` class `refuse` (`spec-43.md:40-47`); neither spec
  has a `refusal` row.

### Files touched (estimate)

- `tools/runtime/act-binding.fragment.json`, `tools/runtime/act-binding-early.fragment.json`
- `tools/runtime/act-binding.js`
- `tools/runtime/inflight-admit.fragment.json`, `tools/runtime/inflight.py`

### Alternatives rejected

- **Declaring the packs class `warn`.** A warn pack never blocks (TOOL-dWellOiledMachine-10 S2), so
  the act binding would decide nothing.

## 5. Production-readiness checklist

- security — the act binding becomes registrable, so its deny-by-default rules actually run; every
  deny keeps its first line and gains its rule.
- perf / scale — none.
- error / empty / loading states — an undeclared rule a source emits stays a failed pack (31 S3).
- observability — the dispatcher's `refusal — <pack> · rule <rule> · actor <actor> · remedy` line
  names who acts.
- risks — the `self` rows lack `remedy-call` until TOOL-dWellOiledMachine-49 adds it; handed off.
- testing — AC1 to AC3 and the arms in §7.
- migration — one re-render of the pack table on `update`.
- user docs — none beyond the remedies the dispatcher prints.

## 6. Acceptance criteria

- **AC1** — When `python tools/settings-merge.py --resolve-pack act-binding.fragment.json`
  runs, and likewise for `act-binding-early.fragment.json` and `inflight-admit.fragment.json`, each
  exits 0 printing its `refusal` rules, and the rendered `hook-packs.json` lists all three
  packs.
  Red when: a pack is refused at registration for a missing `refusal` list.
- **AC2** — When `python act_binding.py --fixture --plant named-call` sends a repeated named
  `Workflow` call through `node dispatch.js PreToolUse`, the deny ends with
  `refusal — act-binding · rule unnamed-call · actor self`, and `--plant stale-epoch` ends with
  `rule stale-epoch · actor driver`.
  Red when: a deny reaches the dispatcher with no rule line and is counted a failed pack.
- **AC3** — When `python inflight.py --fixture --plant second-run` holds a call past a planted
  `hook-hold-seconds` of 20, the deny ends with `rule — held-past-hold`.
  Red when: the deny past the hold carries no rule line.

## 7. Gates

`check-wiring self-test` · `settings-merge selftest` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/runtime/act_binding.py · covers AC2 · the two plants staged against an `act-binding.js` whose deny carries no rule line · none
New arm: tools/runtime/inflight.py · covers AC3 · the held plant staged against an admit whose deny carries no rule line · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 5 (H3).

## 10. Reuse audit

The seam extended is TOOL-dWellOiledMachine-31's `refusal` contract and its registration check in
`load_fragment` (`tools/settings-merge.py:252`), filled for three packs that omitted it. The probe
`python tools/codebase-map/reuse_lookup.py "declare refusal rows for a refuse class hook pack"` ranked
`rows`, `row`, `refusal` and `Refusal` by name stem, generic row and refusal helpers, none a pack's
refusal list; the contract itself is unit 31's and unbuilt at this base, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "what refusal rule remedy actor must a refuse
pack declare" --terms "refusal rows rule remedy actor refuse pack act-binding inflight-admit dispatcher
registration"`
