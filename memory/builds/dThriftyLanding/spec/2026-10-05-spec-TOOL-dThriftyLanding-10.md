# TOOL-dThriftyLanding-10 — govkit's policy-key scan sees a quoted multi-path value

**Status:** CLOSED · rev-1 · 2026-10-05 · node d · Tier-2 · base f765eb8e · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-dThriftyLanding-10-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-dThriftyLanding-10-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-dThriftyLanding-10-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-dThriftyLanding-10-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's finding 5 (HIGH): `GATE_DOC_PATHS` joined `POLICY_KEYS`, but selfcheck 7h3's
assignment pattern is `KEY=\S*`, which stops at the first space, so a quoted space-separated doc class —
the only useful spelling, and gov's own — never matches. The check would certify a kit-shipped file free
of a doc class it carries. This unit widens the pattern to a quoted value.

## 2. Scope (IN)

- **S1** — The assignment arm of the policy pattern accepts a double-quoted or single-quoted value
  holding spaces, beside the bare value, and keeps its tail: optional blanks, an optional comment, end
  of line. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The selftest arms that grade the pattern: `TOOL-dThriftyLanding-11`.

### Edges

- **hands-off** `TOOL-dThriftyLanding-11` — the arms that grade this pattern.

## 4. Design

### Evidence

Read at `f765eb8e`. `tools/govkit/govkit.py` compiles the 7h3 predicate from `POLICY_KEYS`; finding 5
ran it over `GATE_DOC_PATHS="memory/ README.md AGENTS.md"` and over `'a/ b/'` and neither matched,
while the single-element value did.

### Files touched (estimate)

- `tools/govkit/govkit.py`

### Alternatives rejected

- **Parse with `read_policy_key`'s rule.** That rule reads the last assignment of a key in a known file;
  7h3 scans every shipped line for any assignment, so it needs a line predicate, not a value parser.

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

- **AC1** — When the compiled pattern reads gov's own `GATE_DOC_PATHS` line from `.githooks/gate-env.sh`,
  it matches.
  Red when: the pattern at `f765eb8e` does not match it.
- **AC2** — When it reads `GATE_DOC_PATHS="a b" bash x`, it does not match, so an invocation is still not
  a policy.
  Red when: the widening also matches an invocation.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `kit epoch (shipped bytes move, the version moves)` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: none · the arms are TOOL-dThriftyLanding-11's · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · promoted from the closing diff review, round 1.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "scope the push-boundary bar to the legs a doc-only diff can affect"` was run for the build and cannot see `.sh`; no existing seam fits beyond the one named here. The seam is the 7h3 pattern compiled from `POLICY_KEYS`; the review record names the widening and
judged it sound, and found no tracked non-markdown file it would newly red.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent
