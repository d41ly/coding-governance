# TOOL-aScouredKit-7 — the unattended kit stops shipping a scope helper with no caller

**Status:** OPEN · rev-1 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Resolve `scopes()` and `is_scope()` in `tools/unattended/unattended.sh`, which have no caller other
than each other, so the anchor-scope vocabulary has exactly one definition site.

## 2. Scope (IN)

- S1. Read `check_waiver_scope` and decide between two dispositions: delete both helpers, or call
  `is_scope` where the refusal would improve. Deletion is the default and wiring wins only if it
  produces a BETTER refusal than the current one.
- S2. Whichever is taken, the vocabulary ends up defined once. If wiring is taken,
  `tools/unattended/check-unattended.sh:197`'s hand-rebuilt `AUTH_SCOPES="all $AUTH_MODES"` is the
  second spelling and is reconciled in the same pass.

## 3. Non-goals (OUT)

- Changing the anchor-scope vocabulary itself, or what any scope means.
- Any other dead-symbol claim in the kit. This unit is the one instance the audit verified by
  exhaustive search; a sweep is a separate question.

## 4. Design

`is_scope()` at `tools/unattended/unattended.sh:498` has exactly one occurrence repo-wide — its own
definition — and `scopes()` at `:496` has no other caller, so both are unreachable. The real
consumer rebuilds the set by hand in a sibling file, beside a comment defending derivation. That is
the `two-readers-of-one-config-one-re-derived` class with the derived reader switched off.

The disposition is genuinely open between delete and wire, and it is decided by reading one
function rather than by preference, so it is not a fork: `check_waiver_scope` at `:1139` currently
answers a malformed scope with `fail 45`, which blames the run's MODE. If wiring `is_scope` there
produces a refusal that names the scope instead, wiring is strictly better and is taken; if it
cannot, both helpers go.

## 5. Production-readiness checklist

- security — N/A. perf / scale — N/A. a11y — N/A. i18n — N/A.
- error / empty / loading states — if S1 chooses wiring, a malformed scope gains its own refusal.
- observability — N/A.
- risks — deleting a helper an adopter's fork calls. The kit ships verbatim and adopters do not fork
  it, which is what the copy-install model buys.
- testing + left-shift gates — `bash tools/unattended/run-unattended-gates.sh` on demand, since the
  kit's `*.test.sh` suites left the bar by owner ruling of 2026-08-23.
- migration / rollback — N/A. user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'is_scope' tools/unattended/unattended.sh` runs, it returns either zero
  lines or a definition plus at least one call site, never a definition alone.
- **AC2** — When `bash tools/unattended/run-unattended-gates.sh` runs, it is green, and the result
  is recorded here because that suite is not on the automatic bar.
- **AC3** — When the disposition is wiring, a malformed `ANCHOR_SCOPE` value produces a refusal
  naming the scope; when it is deletion, `scopes` has no occurrence in the file either.

## 7. Gates

`unattended run-state records` · `unattended playbooks` · `unattended skill wiring` · the full bar at
the push boundary. The kit self-tests run on demand.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.

## 10. Reuse audit

No new seam: this deletes or wires an existing helper inside one file. The build's reuse probe is
recorded in `TOOL-aScouredKit-1` §10 and is not re-composed.
