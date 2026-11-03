# TOOL-dCalibratedLens-25 — the `returned` line's units field sits before the agent id, and the format guard's fixtures and guard follow the fence

**Status:** DEFERRED · rev-3 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 12 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-25-deviation-251.md](../build/2026-11-02-build-TOOL-dCalibratedLens-25-deviation-251.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 |
| [2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 35, HIGH, item H7 of the round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`). Unit 5 S1 widens the
charter's `returned` micro-format with a plain trailing `· units <units>`. The format guard's
`checkCarries` (`tools/hooks/format-guard.js:431-435`) requires the text after a line's LAST ` · ` to
end `/<agentId>`, so every returned line carrying the field fails, the live hook included; and
`tools/hooks/format-guard.test.sh` copies the live fence (`:310-315`) while its fixtures R1, R2 and R3
(`:485-489`) carry no units field, so the suite reds. The `format-guard self-test` leg's guard names
neither `AGENTS.md` nor the charter template, so the unit lands green and the red appears on an
unrelated change. This unit places the field before the run field as an optional bracket and gives
the fixtures their units cases. The renderer that prints the bracket's content
(`TOOL-dCalibratedLens-31`) and the guard that makes a fence change select the leg
(`TOOL-dCalibratedLens-37`) are the round-2 audit's repairs of this unit. It repairs
`TOOL-dCalibratedLens-5`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 5's text (rev-2, its §4
  "Amendments (round-1 spec audit)", id 35): the shape is `returned — <role> · <outcome> · <wall> ·
  <tokens> out[ · units <units>] · run <run-id|direct>/<agent-id>`, in
  `coding-governance-agents.template.md` and its render `AGENTS.md`. The agent id stays last, so
  `checkCarries` is unchanged; the bracket is optional to `buildShapeRegex`
  (`tools/hooks/format-guard.js:164-179`), so a returned line without the field still matches; and
  `print_agent_lines` writes the field always, `-` when the result carries none. The bracket never
  reaches an emission: `render_shape_line` renders a `[ · …]` group as its content when the fields
  hold its placeholders and leaves it out otherwise, `TOOL-dCalibratedLens-31`'s S1 (round-2 id 30).
  Observed by AC1.
- **S2** — The fixtures, in `tools/hooks/format-guard.test.sh`: R1, R2 and R3 stay as they are (the
  optional form), and three twins R1u, R2u and R3u carry ` · units unit.reuse-first` before their run
  field; each allow arm that asserts allow for R1 to R3 asserts it for the twin too, and one deny arm
  asserts a line whose units field follows the run field is refused. The suite's assertion floor rises
  by the arms added. Observed by AC2.
- **S3** — The leg's guard is `TOOL-dCalibratedLens-47`'s (round-3 id 23, which takes the guard edit
  round-2 id 24 gave `TOOL-dCalibratedLens-37`): it adds `AGENTS.md`, a pathspec govkit's check 7c
  classes `exempt`, because the bare template path falls into no class, and it adds it in the leg's
  declaration. This unit edits no guard. NOT OBSERVED here — `TOOL-dCalibratedLens-47` AC1 observes
  the selection.
- **S4** — The build probe: the suite is read at the main loop's close RED against a fence whose units
  field trails the run field, and GREEN on S1's fence. Observed by AC2.

## 3. Non-goals (OUT)

- Changing `checkCarries` or `buildShapeRegex`. Placing the field before the run field keeps both
  as they are, which is the smaller change the skeptic's fix offers first.
- The `units` content and its tag grammar: unit 5 S1 and id 29 (`TOOL-dCalibratedLens-30`).
- The `agent` line: it carries no units field.
- The renderer's bracket rule and its arm: `TOOL-dCalibratedLens-31` (round-2 id 30). The guard:
  `TOOL-dCalibratedLens-47` (round-3 id 23), which takes it from `TOOL-dCalibratedLens-37` (round-2
  id 24) with the corrected guard command (round-2 ids 5, 16, 23 and 39, `TOOL-dCalibratedLens-41`).
- AC1 reads the fence a sibling's pass writes and is green once unit 5 lands; it is a precondition of
  this unit's arms, not an observation of them (the round-2 audit's ids 4, 18 and 29).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-5` — the `returned` fence of `coding-governance-agents.template.md` and `AGENTS.md`, and `print_agent_lines`' `units` field; without them there is no field whose position the fixtures hold
- **hands-off** `TOOL-dCalibratedLens-31` — the fence's `[ · units <units>]` group, which that unit's renderer prints as its content and its arm feeds to the guard (round-2 id 30)
- **hands-off** `TOOL-dCalibratedLens-47` — the fence change and the suite arms, which that unit's guard on `AGENTS.md` selects (round-3 id 23)

## 4. Design

### Evidence

- `tools/hooks/format-guard.js:431-435` at base: `checkCarries` takes the text after `lastIndexOf(' · ')`
  and tests `endsWith('/' + agentId)`.
- `tools/hooks/format-guard.test.sh:313` at base copies `$ROOT/AGENTS.md` into the fixture repository
  CR-stripped; `:485-489` define A1 to A3 and R1 to R3, none with a units field.
- `AGENTS.md:66` and `coding-governance-agents.template.md:70` at base: `returned — <role> · <outcome> ·
  <wall> · <tokens> out · run <run-id|direct>/<agent-id>`.
- `tools/gate-legs.json` at base: the `format-guard self-test` guard is
  `{prefix}/hooks/format-guard.js`, `{prefix}/hooks/format-guard.test.sh`, `{prefix}/hooks/scratch-guard.js`,
  `{prefix}/runlog/prose.py`, `{prefix}/runlog/extract.py` and `{prefix}/lib/`, with no charter path.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `R1u`, `R2u`, `R3u` | fixture variables in `format-guard.test.sh` | none |

### Files touched (estimate)

- `tools/hooks/format-guard.test.sh` — S2

### Alternatives rejected

- **Amend `checkCarries` to skip a trailing units field.** It teaches the hook one field's name and
  leaves the next trailing field to break it the same way.
- **Units as a mandatory field.** Every returned line written before unit 5 lands, and every adopter's,
  would stop matching.

## 5. Production-readiness checklist

- security — the hook's refusal set is unchanged; a line with the field after the run field is
  refused, as any malformed line is.
- perf / scale — three fixture lines and four arms.
- error / empty / loading states — a result with no units renders `· units -`, never an empty field.
- observability — the hook's existing refusal lines.
- risks — a fence edit selects this suite only once `TOOL-dCalibratedLens-47` lands its guard.
- testing — S2's arms, read RED and GREEN at the close.
- migration — N/A: the field is new.
- user docs — N/A: the fence is the definition; `help/roles.md` is unit 5's.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'out\[ · units <units>\] · run' AGENTS.md coding-governance-agents.template.md`
  runs after this unit's pass, each file prints one line.
  Red when: the field trails the run field, or is mandatory.
- **AC2** — When `grep -c 'R1u\|R2u\|R3u' tools/hooks/format-guard.test.sh` runs, it counts at least
  six, and the suite's arms are read at the close RED against a trailing-field fence and GREEN on S1's.
  Red when: the fixtures carry no units twin, or a trailing field passes.
  permission: a pass runs no suite; the RED and GREEN reads are the main loop's.

## 7. Gates

`format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `micro-format definitions` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/format-guard.test.sh · covers AC2 · the units twins R1u to R3u and a trailing-field deny case, staged red by a fence whose units field follows the run field · the suite's assertion floor, raised by the arms added

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 35 (HIGH, item H7) of the round-1 spec audit;
  unit 5 amended at the disposal (its rev-2).
- rev-2 · 2026-11-02 · §1 §3 §4 §5 S1 S3 AC3 · amended at the disposal of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`: S1 names the renderer's group rule (id 30,
  `TOOL-dCalibratedLens-31`); the guard of S3 and its criterion go to `TOOL-dCalibratedLens-37` with
  `AGENTS.md` alone (id 24), carrying the corrected command of ids 5, 16, 23 and 39; AC1 stated a
  precondition (ids 4, 18, 29), both `TOOL-dCalibratedLens-41`; §3 gains the hands-offs to units 31
  and 37.
- rev-3 · 2026-11-03 · §3 §5 S3 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`: the guard of S3 moves from
  `TOOL-dCalibratedLens-37` to `TOOL-dCalibratedLens-47`, which makes it in the leg's declaration
  (id 23); §3's hands-off names unit 47 in place of unit 37.

## 10. Reuse audit

The seam extended is the format guard's own shape grammar, the `[ · …]` optional bracket
`buildShapeRegex` already admits (`tools/hooks/format-guard.js:164-179`), and its suite's fixture
lines; nothing new is parsed. `python tools/codebase-map/reuse_lookup.py "isolate each reader so one
failure becomes an unread line, never the walk's exit"`, run once for the set, ranked name stems only;
the hook and its suite were read by hand at base. The recall probe returned TOOL-cMendedVintage-19,
the placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
