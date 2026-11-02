# TOOL-dCalibratedLens-37 — a fence edit selects the format guard's suite through `AGENTS.md` alone, a guard pathspec check 7c classes exactly once

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 13 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-37-deviation-371.md](../build/2026-11-02-build-TOOL-dCalibratedLens-37-deviation-371.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 24, HIGH, item H4 of the round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`). Unit 25 S3 adds the bare root
path `coding-governance-agents.template.md` to the `format-guard self-test` guard. govkit's check 7c
(`tools/govkit/govkit.py:2317-2337`) needs every guard pathspec to fall into exactly one declared
class, and that path falls into none: it is under no memory, verbatim, renamed or kit directory, no
`[[exempt]]` row names it, and no kit declares it a root conf. The unguarded `govkit selfcheck` leg
then reds and unit 25 cannot land, and unit 25 §7 does not name that leg. This unit takes the guard
change out of unit 25 and makes it on `AGENTS.md` alone, which the registry already classes
`exempt` and which every fence edit reaches through the render. It repairs `TOOL-dCalibratedLens-25`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 25's text (rev-2, id 24): unit 25
  edits no guard, its S3 and its third criterion name this unit, and its Files touched no longer lists
  `tools/gate-legs.json`. Observed by AC1.
- **S2** — The guard, in `tools/gate-legs.json`: the `format-guard self-test` row's `guard` gains
  `AGENTS.md`, and only that. A fence edit lands in `coding-governance-agents.template.md` and its
  render `AGENTS.md` in one commit (the playbook kit's render), so the rendered file selects the leg
  for both. Observed by AC1 and AC2.
- **S3** — The leg line names `govkit selfcheck`, the always-run leg whose check 7c grades the new
  pathspec, so the close bar observes the classification this unit relies on. Observed by AC3.

## 3. Non-goals (OUT)

- A new pathspec class in `tools/govkit/govkit.py` for root template files, the review's other
  option. It widens a governance kit's taxonomy for one file the render already covers.
- The units field, its fixtures and their arms: `TOOL-dCalibratedLens-25` S1 and S2, unchanged.
- A spec-token join that owes `govkit selfcheck` to every spec editing a guard, the finding's
  left-shift line. Run over the live specs at base, the predicate reds two specs of other builds
  (`aMendedLedger-1` and `aQuarriedLantern-1`) besides unit 25; a join that reds other builds'
  records is not this build's to land.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-25` — the fence change and the suite arms the guard exists to select; without them a fence edit selects a suite that tests no units field

## 4. Design

### Evidence

- `tools/govkit/govkit.py:2317-2337` at base: the classes are memory-root-relative, verbatim-repo-root,
  renamed, exempt, kit-relative and root-conf, and a pathspec in other than one fails.
- `tools/govkit/registry.toml:335-337` at base: an `[[exempt]]` row with `path = "AGENTS.md"`.
- `python tools/check-spec-tokens.py --legs-for AGENTS.md` at base prints only `policy fixtures <-
  AGENTS.md`; the same query for `coding-governance-agents.template.md` prints `no guarded leg`.
- The predicate "a live spec lists `tools/gate-legs.json` under Files touched and its §7 lacks
  `govkit selfcheck`", run over the 59 live specs at base (2026-11-02, PINNED), matched 3 of the 8
  that list the manifest.

### Inventory

No identifier is minted.

### Files touched (estimate)

- `tools/gate-legs.json` — S2

### Alternatives rejected

- **An `[[exempt]]` row for the template.** The template sits inside the registry's declared surface,
  so an exemption would narrow what the surface ships, which the review rules out.
- **Leave the template in the guard and add `govkit selfcheck` to §7.** The leg would observe the
  red, not prevent it.

## 5. Production-readiness checklist

- security — N/A: a selector edit.
- perf / scale — the suite runs on every edit to `AGENTS.md`, a cost of seconds.
- error / empty / loading states — N/A.
- observability — `--legs-for` names the leg for the path.
- risks — a template edit landed without its render: the render's own wiring check reds that drift,
  so the guard's reach through the render holds.
- testing — AC1 to AC3.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py --legs-for AGENTS.md` runs after this unit's pass,
  it prints `format-guard self-test <- AGENTS.md`.
  Red when: a fence edit still selects no format-guard leg.
- **AC2** — When `python -c "import json;print([l['guard'] for l in json.load(open('gate-legs.json')) if l['name']=='format-guard self-test'][0])"`
  runs from the `tools` directory, its list holds `AGENTS.md` and no
  `coding-governance-agents.template.md`; at base it prints the six entries with neither.
  Red when: the template's bare root path is in the guard.
- **AC3** — When a `python -c` probe reads `registry.toml`'s `[[exempt]]` paths with `tomllib` from
  the govkit kit directory, every entry of that guard either opens `{prefix}/` or equals one of them.
  Red when: an entry falls into no class check 7c declares.

## 7. Gates

`format-guard self-test` · `govkit selfcheck` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 24 (HIGH, item H4) of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; unit 25 amended at the disposal (its rev-2),
  its guard change moving here.

## 10. Reuse audit

The seam extended is the `format-guard self-test` row of `tools/gate-legs.json` and the registry's
existing `AGENTS.md` exemption, which check 7c already classes; no class is added. `python
tools/codebase-map/reuse_lookup.py "render an optional bracket group of a shape definition into an
emitted line"`, run once for this disposal's set, ranked name stems only; the guard taxonomy was read
by hand in `tools/govkit/govkit.py`, and `--legs-for` of `tools/check-spec-tokens.py` is the query
the criteria use. The recall probe returned TOOL-cMendedVintage-19, the placement ruling this unit's
order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
