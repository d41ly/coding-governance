---
slug: bConvergentLodestar
node: b
opened: 2026-07-22
streams: tooling
roster: TOOL
ids: TOOL-bConvergentLodestar-1
---

# TOOL-bConvergentLodestar-1 — reuse-convergence layer for codebase-map

**Status:** SPECCED · rev-2 · awaiting owner scope approval · node b · 2026-07-22 · base 7b01979ad7 · adversarial review `wf_69de6d2e-926` folded

The convergence half of the reuse-discovery line: `codebase-map` gives identity coverage (what exists,
who owns it); this layer makes a repo *converge* — new work discovers and wires through existing seams
instead of reinventing. Extends `codebase-map`'s engine/project-layer split; extracted from and re-adopted
by inCMS (ARCH-bThriftyCompass-1, which shipped the prevention-forward half).

- **Spec:** [`spec/2026-07-22-spec-bConvergentLodestar-1.md`](spec/2026-07-22-spec-bConvergentLodestar-1.md) — Tier-2, five scope items S1–S5.
- **Reviews:** `reviews/` (adversarial review pending).

## Scope at a glance

- **S1** `## Reuse affordance` pinned dossier section (forward reuse menu, parseable first line).
- **S2** symbol recall index (`symbols.json`: every public symbol + `fanin`) — machine recall over old+new.
- **S3** `reuse-lookup` — behavior→seam discovery entrypoint (CLI corpus + agent ranking).
- **S4** retroactive convergence — touch-triggered backfill + `--seed-affordances --top N` big-bang.
- **S5** the closing loop + metric, as a `map_diff --converge` mode: `collision_flags` (a new export colliding with a high-fan-in seam, no new edge — shipped reinvention, over ALL new code) surfaced as a review WARN → reinvention backlog, plus `new_clones`. Falsifiable; converges when both trend to zero.

rev-2 reframed S5 around the shipped-reinvention closing loop (rev-1's metric was not falsifiable and the design had no force on the reinvention rate — the review's two blockers).

## Owner scope-approval menu (the §8 forks — decide before build)

- **F1** symbol recall depth: (a) grep-`fanin` heuristic *(rec)* · (b) resolved import graph.
- **F2** affordance enforcement: (a) presence-gated + shrink-only grace + parsed first line *(rec)* · (b) advisory · (c) strict grammar gate.
- **F3** lookup form: (a) CLI corpus + agent-instruction *(rec)* · (b) bundled Workflow · (c) pure-CLI lexical.
- **F4** big-bang scope: (a) top-N by fanin *(rec)* · (b) full sweep · (c) touch-triggered only.
- **F5** metric home: (a) `converge-report` CLI, reporting-only *(rec)* · (b) a gate leg that fails on regression.
- **F6** reuse-decision record: (a) DoD line + optional per-repo spec section *(rec)* · (b) force `## 10` into the shared TEMPLATE-SPEC.
- **F7** collision-WARN / backlog home: (a) append to the reinvention backlog file, dedup by {new,resembles} *(rec)* · (b) stdout-only · (c) per-node sharded log.
- **F8** collision precision knobs: (a) token stem + fan-in threshold · (b) + structural signal *(rec)* · (c) + affordance cross-check; threshold in `.codebase-map.conf`.

<!-- gen:build-index -->
**Build status:** SPECCED · 1 unit(s) · node b · opened 2026-07-22 · streams tooling
ids TOOL-bConvergentLodestar-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-bConvergentLodestar-1 — reuse-convergence layer for codebase-map](spec/2026-07-22-spec-bConvergentLodestar-1.md) | SPECCED | rev-2 | 2026-07-22 |

Records live under `spec/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-07-22-review-TOOL-bConvergentLodestar-1-1.md](reviews/2026-07-22-review-TOOL-bConvergentLodestar-1-1.md) | spec-audit | TOOL-bConvergentLodestar-1 |
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-07-22-spec-bConvergentLodestar-1.md](spec/2026-07-22-spec-bConvergentLodestar-1.md)
- **`reviews/`**
  - [2026-07-22-review-TOOL-bConvergentLodestar-1-1.md](reviews/2026-07-22-review-TOOL-bConvergentLodestar-1-1.md)
<!-- /gen:build-docs -->
