# TOOL-aScouredKit-2 — wave 2: hardcoded values, govkit convergence, instruction-prose load

**Status:** CLOSED · rev-1 · 2026-08-30 · node a · Tier-1 · base 14e21399 · streams tooling+playbook

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-prompt-TOOL-aScouredKit-1.md](../prompts/2026-08-30-prompt-TOOL-aScouredKit-1.md) | research | TOOL-aScouredKit-1 |
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 |
| [2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md) | spec-audit | TOOL-aScouredKit-1 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 TOOL-aScouredKit-30 TOOL-aScouredKit-31 TOOL-aScouredKit-32 |
| [2026-08-30-review-TOOL-aScouredKit-2-wave2-lens-convergence.md](../reviews/2026-08-30-review-TOOL-aScouredKit-2-wave2-lens-convergence.md) | research | — |
| [2026-08-30-review-TOOL-aScouredKit-2-wave2-lens-hardcoded.md](../reviews/2026-08-30-review-TOOL-aScouredKit-2-wave2-lens-hardcoded.md) | research | — |
| [2026-08-30-review-TOOL-aScouredKit-2-wave2-lens-prose.md](../reviews/2026-08-30-review-TOOL-aScouredKit-2-wave2-lens-prose.md) | research | — |
| [2026-08-30-review-TOOL-aScouredKit-2-wave2-report.md](../reviews/2026-08-30-review-TOOL-aScouredKit-2-wave2-report.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Answer the three owner axes that `drift-audit-code.js` does not cover, with a second bounded review
wave whose lenses are written for them, and land its report as a joined record.

## 2. Scope (IN)

- S1. A three-lens `Workflow` wave, run AFTER wave 1 and never beside it, over the kit at base
  `14e21399`. Lens A: hardcoded values an adopter needs as a knob. Lens B: govkit convergence — can
  every `kit.toml`-carrying tool be deployed, updated and wired into a foreign repo. Lens C: the
  instruction corpus's prose load.
- S2. Batched default-refute skeptics within the cap, then one synthesis pass, matching the shape
  `memory/guides/REVIEW-PROTOCOL.md` binds.
- S3. The report renamed to hygiene check 5's grammar under `memory/builds/aScouredKit/reviews/`,
  with its `**Serves:**` binding line and a `## Verdict:` opening line.
- S4. Triage identical to unit 1's S3.

## 3. Non-goals (OUT)

- A new committed workflow script. This wave runs as an inline `Workflow` script, which
  `agent-cap.js` reads on the tool call, so it needs no descriptor, no kit version and no gate leg.
- Any prose edit that changes what a rule demands. That is the build README's stated bound.
- Re-running wave 1's four lenses.

## 4. Design

Three lenses, not five: the lens allowance is `MAX_LENSES` in `tools/hooks/agent-cap.js` and this
wave needs three, so the array is a literal of three elements and the hook proves the bound without
a marker. The verify stage batches every finding across at most the hook's total, keyed by an
orchestrator-assigned integer, per the protocol's measured shape.

### Inventory

| Lens | Population it must enumerate first |
|---|---|
| A — hardcoded | every `tools/*/kit.toml`, every `adopt-*.sh`, every `*.test.sh` fixture prefix |
| B — convergence | the thirteen `kit.toml` descriptors against `tools/govkit/govkit.py`'s verbs |
| C — prose | the files `memory/project/method-carriers.txt` and the charter cite as mandatory |

### Alternatives rejected

Adding three lenses to `drift-audit-code.js`. That would take its literal array to eight, past
`MAX_LENSES`, and a caller-settable lens array cannot be proven bounded by `agent-cap.js` — the
guard decides this, not taste.

## 5. Production-readiness checklist

- security — N/A, records only.
- perf / scale — bounded fan-out; run strictly after wave 1 because the cap is fleet-wide.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a lens with no findings records that answer.
- observability — the report plus three per-lens writeups.
- risks — lens C can propose a trim that silently drops a rule; the README's bound makes any
  non-provable trim a park.
- testing + left-shift gates — the full bar at the push boundary.
- migration / rollback — N/A, additive records.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When wave 2 completes, its report is under `memory/builds/aScouredKit/reviews/` and
  `bash tools/memory-tree/check-memory-hygiene.sh` is green on the filename and the binding line.
- **AC2** — When lens B's writeup is read, it names every one of the `tools/*/kit.toml` descriptors
  and gives each a deploy verdict, so a missing tool is visible rather than absent — checked by
  `ls tools/*/kit.toml` against the writeup's table.
- **AC3** — When lens C proposes a trim, the writeup names the rule the trimmed bytes carried and
  where that rule still lives afterwards, or marks the trim `PARK`.
- **AC4** — When triage completes, every confirmed finding is named by a unit id, a
  `memory/backlog/TOOL.md` row, or a `--park` entry in `RUN.md`.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `python3 tools/memory-tree/gen_build_index.py
--check-format` · `bash tools/check-template-size.sh` where lens C touches the template · the full
bar at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.

## 10. Reuse audit

Same probe pass as `TOOL-aScouredKit-1` §10; the terms are recorded there and are not re-composed.
No existing seam fits THIS unit: `drift-audit-code.js` and `drift-audit-state.js` both carry
five-element literal lens arrays that cannot be extended past `MAX_LENSES`, and `tier2-review.js`
refuses any `kind` outside `diff-review | spec-audit`, neither of which describes a whole-corpus
prose or descriptor audit. The evidence is the `KINDS` guard at `tools/workflows/tier2-review.js`
and the `LENSES` const in each drift-audit script. An inline script is therefore the answer, and it
deliberately ships nothing: a fourth committed harness would owe a descriptor, a version marker and
a gate leg for one run.
