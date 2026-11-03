# TOOL-dCalibratedLens-47 — the `format-guard self-test` guard gains `AGENTS.md` and the roles renderer in the leg's declaration, rendered where the manifest is a render

**Status:** DEFERRED · rev-1 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 14 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dCalibratedLens-47-deviation-471.md](../build/2026-11-03-build-TOOL-dCalibratedLens-47-deviation-471.md) | deviation | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 23, HIGH, item H5 of the round-3 spec audit
(`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`). `TOOL-dCalibratedLens-37` S2
added `AGENTS.md` to the `format-guard self-test` guard by editing `tools/gate-legs.json` alone. The
leg is an `[[exempt_leg]]` of `tools/govkit/registry.toml`; once TOOL-dWitnessedBar-11 lands that row
holds the whole declaration, guard included, and the manifest is rendered from it with `--check`
exiting 1 on any difference. The hand edit is then refused, or erased by the next render, and a fence
edit again selects no format-guard leg, so unit 25's units-field arms go unselected with nothing
reporting it. This unit takes the guard edit from unit 37, makes it in the leg's declaration under
whichever state the build run finds, and observes check 7c's classing of the new entries. It
repairs `TOOL-dCalibratedLens-37`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text: unit 37
  (rev-2, id 23) hands its S2 and S3 here and lists no file; unit 25 (rev-3, r3 id 23) hands its
  fence change and arms here in place of unit 37. Observed by AC1.
- **S2** — Which declaration, decided at the pass by `test -f tools/run-gates/leg_factory.py` and
  named in the pass's commit as a `Decided:` trailer. Factory case: the entries go in the
  `format-guard self-test` `[[exempt_leg]]` row of `tools/govkit/registry.toml`, which then carries
  the leg's whole row (TOOL-dWitnessedBar-11 S1), and `python tools/run-gates/leg_factory.py --write`
  renders `tools/gate-legs.json`. Hand case: the entries go in that leg's row of
  `tools/gate-legs.json`, the only spelling of its guard, since the registry row carries `name` and
  `why` alone and no descriptor declares the leg. Observed by AC1 and AC3.
- **S3** — The entries: `AGENTS.md`, the render every fence edit lands in beside its template, so a
  fence edit selects the suite whose arms read it; and `{prefix}/roles/handoff.py` and
  `{prefix}/roles/roles_lib.py`, the renderer and library `TOOL-dCalibratedLens-31`'s shape arm in
  `tools/hooks/format-guard.test.sh` runs, so a renderer edit selects the arm as a guard edit does
  (id 6, M5, carried from `TOOL-dCalibratedLens-48`). Nothing else. Observed by AC1 and AC2.
- **S4** — The leg line names `govkit selfcheck`, the always-run leg whose check 7c grades each new
  pathspec. NOT OBSERVED — a §7 leg line, read by the spec-token leg join and never by a criterion
  of this unit (ids 7, 16 and 26, L1, carried from `TOOL-dCalibratedLens-48`).

## 3. Non-goals (OUT)

- A pathspec class for root template files: unit 37 §3, unchanged.
- The factory, and any other leg's guard: TOOL-dWitnessedBar-11 and `TOOL-dCalibratedLens-46`.
- The bare template path `coding-governance-agents.template.md` in any guard: check 7c classes it
  into no class (unit 37 §1).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-25` — the fence change and the units-field arms the guard exists to select; without them a fence edit selects a suite that tests no units field
- **consumes-from** `TOOL-dCalibratedLens-31` — the shape arm in `tools/hooks/format-guard.test.sh`, which runs the roles renderer S3 adds to the guard
- **consumes-from** `TOOL-dCalibratedLens-37` — its S2 and S3, the guard edit and leg line this unit builds in its place
- **consumes-from** external — TOOL-dWitnessedBar-11 (`leg_factory.py`), DEFERRED at base; its absence at the pass selects the hand case of S2

## 4. Design

### Evidence

- `tools/govkit/registry.toml:578-580` at base: the `format-guard self-test` `[[exempt_leg]]` row,
  `name` and `why` only, its `why` saying the leg is not a `[[gate_leg]]` in any descriptor.
- `tools/gate-legs.json` at base: that leg's guard is `{prefix}/hooks/format-guard.js`,
  `{prefix}/hooks/format-guard.test.sh`, `{prefix}/hooks/scratch-guard.js`, `{prefix}/runlog/prose.py`,
  `{prefix}/runlog/extract.py` and `{prefix}/lib/`; the two runlog entries are TOOL-aHeardState-5's,
  the precedent for naming a sibling kit's file a parity arm runs.
- `tools/run-gates/run-gates.sh:3070-3082`: under `GATE_SELFTESTS=changed` a leg no govkit entry
  ships selects by its guard plus its suite file; `tools/hooks/kit.toml:93-95` withholds
  `format-guard.test.sh` as `project-owned`, so its guard is what selects it.
- `tools/govkit/registry.toml:335-337`: the `[[exempt]]` row `path = "AGENTS.md"`, which check 7c
  classes `exempt`.
- `tools/run-gates/leg_factory.py` is absent at `8bec4cef`; TOOL-dWitnessedBar-11 is DEFERRED.

### Inventory

No identifier is minted.

### Files touched (estimate)

- `tools/gate-legs.json` — S2 and S3, in either case
- `tools/govkit/registry.toml` — S2, in the factory case

### Alternatives rejected

- **Edit `tools/gate-legs.json` alone, as unit 37 did.** Right only while the factory is absent.
- **A guard on `roles adopter self-test` naming the hooks file.** That leg is held under `changed`
  by its own kit's selection, and a guard narrows a leg that runs today on every self-test bar.

## 5. Production-readiness checklist

- security — N/A: selector edits.
- perf / scale — the suite runs on edits to `AGENTS.md` and two roles files, a cost of seconds.
- error / empty / loading states — a factory present but failing `--check` after the render stops
  the pass.
- observability — `--legs-for` names the leg for each entry; the commit's `Decided:` trailer names
  the case.
- risks — a template edit landed without its render: the render's own wiring check reds that drift,
  so the guard's reach through the render holds.
- testing — AC1 to AC3 by the pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py --legs-for AGENTS.md tools/roles/handoff.py
  tools/roles/roles_lib.py` runs after the pass, each path names `format-guard self-test`.
  Red when: a fence edit or a renderer edit still selects no format-guard leg.
- **AC2** — When `python tools/govkit/govkit.py selfcheck` runs after the pass, it prints no check 7c
  failure naming the `format-guard self-test` guard; with the bare
  `coding-governance-agents.template.md` added to that guard in a scratch copy of the tree, it prints
  one.
  Red when: an entry falls into no class, or the staged entry passes.
  cost: one selfcheck, about a minute.
- **AC3** — In the factory case, when `leg_factory.py --check` runs from its S2 path after the pass,
  it exits 0 and the rendered guard holds the three entries. In the hand case, when
  `grep -n '"AGENTS.md"' tools/gate-legs.json` runs, it names the `format-guard self-test` row.
  Red when: the entries live in a spelling the next render discards.
  fixture: which case holds is the build run's, decided by S2's probe.

## 7. Gates

`format-guard self-test` · `govkit selfcheck` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, promoted from id 23 (HIGH, item H5) of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, carrying id 6 (M5) and ids 7, 16 and 26
  (L1) from `TOOL-dCalibratedLens-48`; units 37 and 25 amended at the disposal (their rev-2 and rev-3).

## 10. Reuse audit

The seams extended are the leg's own declaration, the registry's existing `AGENTS.md` exemption, and
in the factory case TOOL-dWitnessedBar-11's `leg_factory.py --write`; no class and no renderer is
added. `python tools/codebase-map/reuse_lookup.py "add a path to a gate leg guard pathspec"` ranked
name stems only (`legs`, `leg`, `resolve_tool_path`); the guard taxonomy was read by hand in
`tools/govkit/govkit.py`. The recall probe below returned TOOL-dWitnessedBar-11's reuse scout and
spec; TOOL-aHeardState-5, the precedent for a parity arm's sibling-kit entries, came from the shape
arm's probe recorded in `TOOL-dCalibratedLens-44` §10.

Recall terms used: `python tools/memory-recall/query.py "how is a declared gate leg guard widened
when the leg manifest is rendered from declaring rows" --terms "gate leg guard declaring row rendered
manifest leg factory exempt_leg registry hand-written fallback"`
