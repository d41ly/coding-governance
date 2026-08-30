---
slug: aScouredKit
node: a
opened: 2026-08-30
streams: tooling+playbook
roster: TOOL
ids: TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-10 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 TOOL-aScouredKit-16 TOOL-aScouredKit-17 TOOL-aScouredKit-18 TOOL-aScouredKit-19 TOOL-aScouredKit-20 TOOL-aScouredKit-21 TOOL-aScouredKit-22 TOOL-aScouredKit-23 TOOL-aScouredKit-24 TOOL-aScouredKit-25 TOOL-aScouredKit-26 TOOL-aScouredKit-27 TOOL-aScouredKit-28 TOOL-aScouredKit-29
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
| 1 | `TOOL-aScouredKit-1` | CLOSED | wave 1 — dead code, unwired surface, duplication, inefficiency, instrument integrity, over the whole kit |
| 2 | `TOOL-aScouredKit-2` | CLOSED | wave 2 — hardcoded values, govkit deploy/update/wire convergence, instruction-prose load |
| 3 | `TOOL-aScouredKit-3` | CLOSED | one predicate decides a gate leg's hold, and the pin file sees both fields |
| 4 | `TOOL-aScouredKit-4` | CLOSED | a shrink-only list seeded empty stops being a permanent offender |
| 5 | `TOOL-aScouredKit-5` | CLOSED | drift-audit's conf parser matches the source its docstring claims to copy |
| 6 | `TOOL-aScouredKit-6` | CLOSED | three per-file grep loops on the bar batch, at byte-identical output |
| 7 | `TOOL-aScouredKit-7` | CLOSED | the unattended kit stops shipping a scope helper with no caller |
| 8 | `TOOL-aScouredKit-8` | CLOSED | drift-audit stops printing a cardinality its own source retracted |
| 9 | `TOOL-aScouredKit-9` | CLOSED | drift-audit-state.js gains its sibling's run-integrity fields |
| 10 | `TOOL-aScouredKit-11` | CLOSED | the gate-leg manifest is withheld only by problems the LEGS step raised |
| 11 | `TOOL-aScouredKit-12` | CLOSED | two gate legs receive the path the descriptor already holds |
| 12 | `TOOL-aScouredKit-13` | CLOSED | plan and apply honour the target's own declared kit list |
| 13 | `TOOL-aScouredKit-14` | CLOSED | three prose defects in the load-bearing documents |
| 14 | `TOOL-aScouredKit-15` | CLOSED | the drift-audit Skill stops pointing at a directory govkit never creates |

*`TOOL-aScouredKit-10` and `-16` through `-26` are NOT units of this build and deliberately carry
no spec. They are the findings this run reported rather than built, each landed as a row in*
`memory/backlog/TOOL.md` *with its own measurement. They were recorded through `--rescope --act
add` as the run found them, which was the wrong verb for a backlog row and is said here rather
than rewritten out of an append-only record.*

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 14 unit(s) · node a · opened 2026-08-30 · streams tooling+playbook
ids TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-10 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15
ids TOOL-aScouredKit-16 TOOL-aScouredKit-17 TOOL-aScouredKit-18 TOOL-aScouredKit-19 TOOL-aScouredKit-20 TOOL-aScouredKit-21 TOOL-aScouredKit-22 TOOL-aScouredKit-23 TOOL-aScouredKit-24 TOOL-aScouredKit-25 TOOL-aScouredKit-26 TOOL-aScouredKit-27 TOOL-aScouredKit-28 TOOL-aScouredKit-29

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aScouredKit-1 — wave 1: dead, unwired, duplicated, inefficient, and lying instruments](spec/2026-08-30-spec-TOOL-aScouredKit-1.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-11 — the gate-leg manifest is withheld only by problems the LEGS step raised](spec/2026-08-30-spec-TOOL-aScouredKit-11.md) | — | 2 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-12 — two gate legs receive the path the descriptor already holds](spec/2026-08-30-spec-TOOL-aScouredKit-12.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-13 — `plan` and `apply` honour the target's own declared kit list](spec/2026-08-30-spec-TOOL-aScouredKit-13.md) | — | 2 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-14 — three prose defects in the load-bearing documents](spec/2026-08-30-spec-TOOL-aScouredKit-14.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-15 — the drift-audit Skill stops pointing at a directory govkit never creates](spec/2026-08-30-spec-TOOL-aScouredKit-15.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-2 — wave 2: hardcoded values, govkit convergence, instruction-prose load](spec/2026-08-30-spec-TOOL-aScouredKit-2.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-3 — one predicate decides a gate leg's hold, and the pin file sees both fields](spec/2026-08-30-spec-TOOL-aScouredKit-3.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-4 — a shrink-only list seeded empty stops being a permanent offender](spec/2026-08-30-spec-TOOL-aScouredKit-4.md) | — | 1 | OPEN | rev-2 | 2026-08-30 |
| [TOOL-aScouredKit-5 — drift-audit's conf parser matches the source its docstring claims to copy](spec/2026-08-30-spec-TOOL-aScouredKit-5.md) | — | 1 | OPEN | rev-2 | 2026-08-30 |
| [TOOL-aScouredKit-6 — three per-file grep loops on the bar batch, at byte-identical output](spec/2026-08-30-spec-TOOL-aScouredKit-6.md) | — | 1 | OPEN | rev-3 | 2026-08-30 |
| [TOOL-aScouredKit-7 — the unattended kit stops shipping a scope helper with no caller](spec/2026-08-30-spec-TOOL-aScouredKit-7.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-8 — drift-audit stops printing a cardinality its own source retracted](spec/2026-08-30-spec-TOOL-aScouredKit-8.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
| [TOOL-aScouredKit-9 — drift-audit-state.js gains its sibling's run-integrity fields](spec/2026-08-30-spec-TOOL-aScouredKit-9.md) | — | 1 | OPEN | rev-1 | 2026-08-30 |
<!-- /gen:build-units -->

Records: 11 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aScouredKit-1 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
