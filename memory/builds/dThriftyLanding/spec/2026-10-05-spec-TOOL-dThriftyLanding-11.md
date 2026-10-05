# TOOL-dThriftyLanding-11 — the policy selftest grades every spelling of a doc class

**Status:** CLOSED · rev-1 · 2026-10-05 · node d · Tier-2 · base f765eb8e · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-dThriftyLanding-11-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-dThriftyLanding-11-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-dThriftyLanding-11-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-dThriftyLanding-11-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's finding 10 (HIGH): selftest M5 grades the 7h3 pattern over the single-element
`GATE_DOC_PATHS="memory/"` only, so a pattern blind to the multi-path spelling stayed green — a guard
over a population of one. This unit adds the spellings the key is written in.

## 2. Scope (IN)

- **S1** — M5 asserts the pattern matches a double-quoted and a single-quoted multi-element value, and
  gov's real line read from `.githooks/gate-env.sh`. Observed by AC1.
- **S2** — M5 asserts the pattern does not match the same value followed by a command. Observed by AC1.

## 3. Non-goals (OUT)

- The pattern itself: `TOOL-dThriftyLanding-10`.

### Edges

- **consumes-from** `TOOL-dThriftyLanding-10` — the pattern these arms grade.

## 4. Design

### Evidence

Read at `f765eb8e`. `tools/govkit/selftest.py` M5 imports `POLICY_KEYS`, compiles the pattern the
same way the engine does, and checks one `GATE_DOC_PATHS` value.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **Grade the engine's compiled object directly.** M5 already asserts that the engine's source
  compiles the same alternation, which keeps the copy honest.

## 5. Production-readiness checklist

- perf / scale — no new process on the common path.
- security — narrows nothing the push boundary decides; each change makes a skip rarer or a check wider.
- error / empty / loading states — unchanged.
- observability — each refusal or decision names its reason.
- testing — each arm observed RED against `f765eb8e` first.
- migration — none.
- user docs — the carriers unit 6 wrote, where this unit's change touches them.
- risks — none beyond the finding's own.

## 6. Acceptance criteria

- **AC1** — When the new M5 arms run against the pattern at `f765eb8e`, the multi-element and real-line
  arms fail; against the widened pattern, all pass, the invocation arm included.
  Red when: an arm passes against the narrow pattern.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · multi-path GATE_DOC_PATHS spellings against the f765eb8e pattern · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · promoted from the closing diff review, round 1.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "scope the push-boundary bar to the legs a doc-only diff can affect"` was run for the build and cannot see `.sh`; no existing seam fits beyond the one named here. The seam is M5's existing predicate and its policy-line and invocation-control lists.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent
