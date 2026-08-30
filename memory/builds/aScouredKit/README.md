---
slug: aScouredKit
node: a
opened: 2026-08-30
streams: tooling+playbook
roster: TOOL
ids: TOOL-aScouredKit-1 TOOL-aScouredKit-2
authorized-by: prompt
---

# aScouredKit — a full adversarial review of the kit, on five axes the owner named

## The problem this build exists to solve

The kit has thirteen descriptor-carrying tools under `tools/` and has never been audited as ONE
product. Every prior review was scoped to a diff or a spec, so five whole-corpus questions have no
answer on disk: what is dead, what is hardcoded where an adopter needs a knob, whether every tool can
actually be deployed into a foreign repo, whether any instrument is blind the way `reuse_lookup.py`
was blind to Python, and whether the instruction documents can be cut without losing a rule. The
owner's prose is the mandate and is recorded verbatim under
[prompts/](prompts/2026-08-30-prompt-TOOL-aScouredKit-1.md); base `14e21399`.

## Expected improvements

- Each of the five axes gets a written verdict backed by a path and a command, not an impression.
- Every confirmed finding becomes a unit of this build, a backlog row, or a park with its reason.
- The two audit records join to this build, so the next session extends them instead of re-running.

## Detriments if this is not built

- The kit keeps shipping to adopters with unmeasured blind spots in its own instruments.
- Hardcoded install assumptions stay latent until an adopter at a foreign prefix hits them, which is
  how `TOOL-aRootedPrefix-1` and `TOOL-aGradedDoorway-2` were both found — late, by an adopter.
- The instruction corpus keeps growing with nothing measuring whether a reader can still afford it.

## Build-level rules

- **Classification (M2), written before acting**: units 1 and 2 are READY at Tier 1. Every unit this
  build adds later is MISSING until its spec lands, and is specced at the tier its own risk earns.
- The roster is PROVISIONAL by construction: the fix units cannot be named before the audit names
  them. They arrive through `--rescope --act add`, and the branch is re-pushed after each roster
  change so the authorization comparison holds.
- **Already tracked is not a finding.** 199 open `memory/backlog/TOOL.md` rows and 8 `DEPL.md` rows
  are fed to both waves as `byDesign`. A wave may report one is still live or worse; it may not
  re-report one as new.
- **The prose axis touches governance carriers, so its bound is stated once here.** M3 veto 2 makes a
  governance-carrier change an owner turn. The owner's own prompt asks for it, so it is in scope as
  the GOAL; what stays out is any edit that changes what a rule DEMANDS. A trim that is not provably
  meaning-preserving is parked, never taken.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aScouredKit-1` | OPEN | wave 1 — dead code, unwired surface, duplication, inefficiency, instrument integrity, over the whole kit |
| 2 | `TOOL-aScouredKit-2` | OPEN | wave 2 — hardcoded values, govkit deploy/update/wire convergence, instruction-prose load |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 2 unit(s) · node a · opened 2026-08-30 · streams tooling+playbook
ids TOOL-aScouredKit-1 TOOL-aScouredKit-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aScouredKit-1 — wave 1: dead, unwired, duplicated, inefficient, and lying instruments](spec/2026-08-30-spec-TOOL-aScouredKit-1.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-2 — wave 2: hardcoded values, govkit convergence, instruction-prose load](spec/2026-08-30-spec-TOOL-aScouredKit-2.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 2 record folder(s).

Ids no record names: TOOL-aScouredKit-1 TOOL-aScouredKit-2.

Ids no `spec-audit` record has ever named: TOOL-aScouredKit-1 TOOL-aScouredKit-2.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
