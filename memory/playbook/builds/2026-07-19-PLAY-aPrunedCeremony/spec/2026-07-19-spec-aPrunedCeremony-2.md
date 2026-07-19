# PLAY-aPrunedCeremony-2 — diff-scoped gates are fail-closed and coarse

**Status:** OPEN · rev-1 · 2026-07-19 · node a · Tier-1 · base bf7f2c22

## 1. Goal

Capture the most expensive lesson of inCMS `ARCH-aTrimmedGauntlet-2` (its RD15 reversal) as a §7
gate-discipline rule: diff-scoping which legs run is safe ONLY when it is fail-closed and coarse. An
unclassified path runs the full bar; precise per-path "this file → exactly these tests" targeting is
a trap, because tests read a path INDIRECTLY (through an app module) and a narrow bucket silently
skips the guard that would have caught the break. Two tiers (full-by-default + a proven-safe skip
set), never N clever buckets.

## 2. Scope (IN)

- S1 — Add one §7 bullet stating the fail-closed-and-coarse scoping discipline, near the
  `{{GATE_RUNNER}}` definition (template §7, around L128).
- S2 — Name the failure mode it prevents (a scoped run green-by-absence on the very gate the diff
  needed) and tie it to §10's green-by-absence family and PLAY-aPrunedCeremony-3.
- S3 — State the safe shape: an unrecognized path selects the full bar (fail-closed); the skip set
  is an allowlist of paths PROVEN to trigger no full-suite gate, not a denylist.

## 3. Non-goals (OUT)

- Not shipping a scope-surface artifact (inCMS's `gate-scope.json`) into the kit — `run-gates.sh`
  already scopes per-leg via `leg_if_changed` and fails safe to "run" when the base is unresolvable.
  This spec is the guardrail WORDING that the runner's behavior already embodies but the charter
  does not state.
- Not forbidding future per-tier surfaces — only forbidding the precise per-path targeting that
  RD15 proved unsafe.

## 4. Design

### Inventory

| Edit site | Change |
|-----------|--------|
| template §7 (~L128, after the `{{GATE_RUNNER}}` bullet) | Add the fail-closed-coarse scoping bullet (S1-S3). |

Proposed bullet:

```
- Scoping which legs run to the diff is legitimate economy, but ONLY fail-closed and coarse: an
  unclassified/unrecognized path runs the FULL bar, and the skip set is an allowlist of paths proven
  to trigger no whole-suite gate — never a per-path "this file → these tests" map. Tests read a path
  indirectly (through a shared module), so a narrow bucket skips the guard the diff needed and the
  scoped run passes green-by-absence (§10). Two tiers — full default + proven-safe skip — is the
  ceiling; when in doubt, run the bar.
```

### Alternatives rejected

- **Ship `gate-scope.json` as kit doctrine.** Rejected here: it is a tooling artifact
  (TOOL-aPrunedCeremony-1 territory), and the *lesson* — fail closed, stay coarse — is what
  generalizes. A project can encode tiers however it likes; the rule is the invariant.

## 6. Acceptance criteria

- AC1 — When template §7 is read, it contains a rule that an unclassified path runs the full bar and
  bans precise per-path test targeting, citing the green-by-absence risk.
- AC2 — When `check-template-size.sh` runs after the edit, it stays green (≤32 KiB).

## 8. Open questions

- **Fork — wording-only, or also a `.domain-rules.md` §7 cross-link?** RECOMMEND: wording-only in
  the template §7, with a half-clause pointing at §10's green-by-absence family — no new companion
  section. The rule is short enough to live inline.

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
