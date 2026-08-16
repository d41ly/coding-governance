---
slug: aTetheredConvoy
node: a
opened: 2026-08-16
streams: deployer+tooling
roster: DEPL
ids: DEPL-aTetheredConvoy-1 DEPL-aTetheredConvoy-2 DEPL-aTetheredConvoy-3 DEPL-aTetheredConvoy-4 DEPL-aTetheredConvoy-5 DEPL-aTetheredConvoy-6 DEPL-aTetheredConvoy-7
---

# aTetheredConvoy — finish the deployer, add the update verb, and ratchet both

Node `a` · opened 2026-08-16 · streams deployer and tooling.

`govkit` lands an install, cannot move one forward, and performs three of the steps its own contract
defines. Every repo that adopted it is an upgrade orphan the moment gov commits again — the sentence
the deployer research opened with about the era before govkit, one layer up. This build closes both:
the `update` verb, and the unbuilt halves of `apply` and `check`.

Underneath sits the question that decides whether either stays true: nothing forces a NEW moving part
in this repo to ship govkit-ready. The surface predicate forces a new `tools/` directory to be
CLAIMED. It does not force that claim to be complete, to name the kit's gate legs, to claim its
version constant, to cover a file added inside it, or to deploy anything at all.

## Start here

**State.** Seven units, all OPEN, none built. Unit 1 is at rev-2; the rest are rev-1. The unit map
below IS the scope; it is ordered, and the order is a contract rather than a preference — each spec's
§3 names the units it supersedes and the ones it assumes.

**Read the grounding before any of them.** Every finding is measured, most by driving `govkit` end to
end into throwaway repositories. A twelve-agent audit and adversarial pass returned BLOCKED on all
three lenses with ten blockers. The three that decide the shape of this build:

- **Role precedence does not exist, and it is a live data-loss path.** `codebase-map`'s
  `include = "**"` engine rule enumerates every tracked file under its home and stamps role `engine`
  on `map_extractors.py` — a file the SAME descriptor declares `project-owned`. Measured: every row
  of a reference install carries role `engine`, and gov's own FILLED extractors land in the target.
  The contract spec states "the apply layer has no code path that writes a file whose role is
  project-owned"; that is measurably false. Three consumers dispatch on `role`, and `update` would
  overwrite an operator's authored file because the receipt lies about what it is.
- **The receipt is not a stable inventory.** Two identical applies of a seed-bearing kit leave the
  file list EMPTY and the sums sidecar empty with it. Every evidence loop this build adds would then
  iterate zero rows and exit 0 with the same output as a verified target.
- **The combined work is not one unit.** Specced together it produced, inside its own design, two
  incompatible spellings of the gate-runner declaration, two check-state vocabularies, three step-id
  grammars and four receipt schemas — this repo's named core defect, committed in the design meant to
  close it. Seven ordered units is the answer, not a smaller scope.

**What is IN.** All of it. The `merged` role, the `.gitattributes` writer and its renormalize, the
gate-runner and CI emitter, the baseline phase, every unbuilt `check` arm, the acceptance matrix and
the runbook parity gate — everything `apply` reports as SKIPPED, and everything the contract designed
that nobody ever wrote down. Nothing was cut; it was ordered.

**What stays OUT across the whole build.** `remove`, fleet fan-out, the copier-style three-way for
living documents, adding kits to an existing install, and gate-runner grammars beyond one. Each is
named with its reason in the unit that would otherwise absorb it.

**The deployer's own docstring undercounts its gaps, and its two lists disagree.** One names the
`.gitattributes` block and the leg emitter; the other names the merged region and the leg emitter.
Three distinct unbuilt things across two lists of two — and the BASELINE phase, a full third of the
hard order, is in neither and is announced by no line of `apply`'s output. The file that exists to end
silent partial installs is silently partial about its largest missing piece. Unit 1 makes the step
vocabulary data so that cannot recur.

## The unit map

| # | Unit | What it owns | Why it is where it is |
|---|---|---|---|
| 1 | truthful core | receipt schema 2 · role precedence · one file-set expansion · the role-landing closure · the check-state vocabulary · the step-id vocabulary | every later unit dispatches on these; four of them were independently re-decided when the work was specced as one |
| 2 | `update` | the six-verdict table, the three-way, the conflict outbox | needs a receipt that does not shrink and roles that are true — nothing else |
| 3 | convergence ratchet | leg · version · file correspondences, the widened surface, the deployability leg | lands EARLY so units 4–7's new declarations are forced to be claimed as they arrive |
| 4 | S13 end to end | the `[gate_runner]` declaration, intake writer, baseline read, state machine, policy knobs, hook probe, leg emitter, CI writer, `check --observe` | splitting the declaration from its consumers is what produced two incompatible shapes |
| 5 | check's evidence | integrity · provenance · adopter fan-out · rendered equality · machine orders · the `[[outcome]]` evaluator · the outbox reader | needs only the receipt, no runner |
| 6 | merged role | the region writer, the `.gitattributes` block, LF pins, the renormalize | supersedes unit 2's merged refusal, and says so in its own §3 |
| 7 | harness | acceptance matrix · the refusal-arm cross-check · runbook parity | LAST, so its arms are written once against a settled refusal population |

**The ordering is load-bearing and each spec carries it.** Unit 6 makes unit 2's merged refusal stale;
unit 7's cross-check is a function of the refusal population units 1–6 add to; unit 3's leg
correspondence grades units 4–6's new legs. Landing them out of order costs rewritten criteria, not
merely rework.

The table below is GENERATED
from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** OPEN · 7 unit(s) · node a · opened 2026-08-16 · streams deployer+tooling · ids DEPL-aTetheredConvoy-1 DEPL-aTetheredConvoy-2 DEPL-aTetheredConvoy-3 DEPL-aTetheredConvoy-4 DEPL-aTetheredConvoy-5 DEPL-aTetheredConvoy-6 DEPL-aTetheredConvoy-7

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [DEPL-aTetheredConvoy-1 — the truthful core: roles, the receipt, and one expansion](spec/2026-08-16-spec-DEPL-aTetheredConvoy-1.md) | OPEN | rev-3 | 2026-08-16 |
| [DEPL-aTetheredConvoy-2 — update, the verb that moves an install forward](spec/2026-08-16-spec-DEPL-aTetheredConvoy-2.md) | OPEN | rev-2 | 2026-08-16 |
| [DEPL-aTetheredConvoy-3 — the convergence ratchet: nothing new ships un-deployable](spec/2026-08-16-spec-DEPL-aTetheredConvoy-3.md) | OPEN | rev-2 | 2026-08-16 |
| [DEPL-aTetheredConvoy-4 — the gate-runner declaration, end to end](spec/2026-08-16-spec-DEPL-aTetheredConvoy-4.md) | OPEN | rev-2 | 2026-08-16 |
| [DEPL-aTetheredConvoy-5 — check stops printing states and starts carrying evidence](spec/2026-08-16-spec-DEPL-aTetheredConvoy-5.md) | OPEN | rev-2 | 2026-08-16 |
| [DEPL-aTetheredConvoy-6 — the merged role, the attributes block, and the renormalize](spec/2026-08-16-spec-DEPL-aTetheredConvoy-6.md) | OPEN | rev-2 | 2026-08-16 |
| [DEPL-aTetheredConvoy-7 — the acceptance matrix, the refusal join, and the runbook parity gate](spec/2026-08-16-spec-DEPL-aTetheredConvoy-7.md) | OPEN | rev-2 | 2026-08-16 |

Records live under `spec/`.
<!-- /gen:build-index -->
