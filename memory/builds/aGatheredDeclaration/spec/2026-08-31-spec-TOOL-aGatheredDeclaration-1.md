# TOOL-aGatheredDeclaration-1 — the adopter review, and the schema union it implies

**Status:** INPROGRESS · rev-1 · 2026-08-31 · node a · Tier-1 · base 44734f15 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGatheredDeclaration-1-adopter-review.md](../build/2026-08-31-build-TOOL-aGatheredDeclaration-1-adopter-review.md) | research | — |
| [2026-08-31-prompt-TOOL-aGatheredDeclaration-1.md](../prompts/2026-08-31-prompt-TOOL-aGatheredDeclaration-1.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Record what `d41ly/incms` and `nicocares` declare and execute as their gate bar today, so the
canonical declaration this build introduces is derived from three real corpora rather than from one.
The output is a build record; no shipped file changes under this unit.

## 2. Scope (IN)

- **S1** — inCMS: the manifest schema, the runner's mode surface, its lane model, its opt-in
  mechanism and its ceiling policy, each cited to a line.
- **S2** — NicoCares: which kit version it runs, what its manifest declares, and what it therefore
  cannot express.
- **S3** — coding-governance: the same three facts, for the comparison to be three-way.
- **S4** — the SCHEMA UNION: every field any of the three declares, with the one repo that proves
  each is load-bearing, and a ruling on which enter the canonical declaration.
- **S5** — the harvest list: mechanisms inCMS has that gov does not, each mapped to the unit that
  takes it.

## 3. Non-goals (OUT)

- Editing either adopter. Owner ruling, 2026-08-31: review, ship the upgrader, touch neither.
- Porting inCMS's `scripts/gate.sh`. It is 863 lines carrying a PowerShell twin and a parity
  ratchet, and its docker/postgres provisioning is product-specific.
- Deciding the TOML surface syntax. That is `TOOL-aGatheredDeclaration-2`; this unit supplies the
  FIELD SET it must cover, not the spelling.

## 6. Acceptance criteria

- **AC1** — the record `build/2026-08-31-build-TOOL-aGatheredDeclaration-1-adopter-review.md` exists,
  carries `**Serves:** research TOOL-aGatheredDeclaration-1`, and every numeric claim in it is cited
  to a file and a line or to a command whose output is quoted.
- **AC2** — the record's schema-union table names every key present in any of the three manifests,
  and for each one names the repo it was observed in. Verified by re-deriving the three key sets
  with `python -c` over the three files and diffing against the table.
- **AC3** — the record states, for each field the union proposes to DROP, why dropping it loses
  nothing — an unverifiable claim is written as `UNVERIFIED` rather than asserted.
- **AC4** — every mechanism in the harvest list names the unit id that takes it, and every unit id
  named exists in the build README's roster, verified by grepping each id against `memory/builds/aGatheredDeclaration/README.md`.

## 7. Gates

`bash tools/run-gates/run-gates.sh` scoped to the memory tree — the hygiene gate is what grades a
record's `**Serves:**` binding and its filename grammar. No new leg: this unit ships no executable.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · authored. Tier-1 light profile: sections 4, 5 and 10 are omitted under the
  tier rule rather than left hollow, because this unit ships no code to design, no production
  surface to check, and its reuse audit is the whole of §2.
