# DEPL-dCarriedReceipt-1 — `{relpath}` resolves through `rule_relpath` in the seam that writes

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

## 1. Goal

`{relpath}` has two resolutions in this file. `rule_relpath` (`:172`) resolves it against the rule's
base and its docstring names the basename form as **a measured defect**, citing push-main's hook
rule by name. `resolve_dests` (`:2085`) — the seam `plan`, the write loop and the wildcard exclusion
all call — resolves it as `PurePosixPath(src).name`, which is that same defect, live. So gov's
`pre-push` hook resolves to a bare `pre-push` at the **target root** while the rule's own `claims`
spell `.githooks/pre-push`: two spellings of one destination inside one rule, and the writer holds
the wrong one. `resolve_dests`' own docstring opens by claiming to be "ONE spelling", which is the
whole defect stated as a virtue.

## 2. Scope (IN)

- **S1** — `resolve_dests` resolves `{relpath}` by calling `rule_relpath(desc, rule, src)` instead
  of taking the basename. The `desc` is already in scope at that call site.
- **S2** — the same substitution in any other `{relpath}` resolution site, established by grep
  rather than by memory; every hit either routes through `rule_relpath` or is recorded here as
  deliberately not routed, with its reason.
- **S3** — one `selftest.py` arm asserting push-main's hook rule resolves to `.githooks/pre-push`,
  and one asserting a rule whose source *is* directly under `home` still resolves to its basename —
  the case the buggy form got right, so the fix must not regress it.
- **S4** — a `selfcheck` arm asserting, over every registry entry, that a rule declaring both `to`
  and `claims` resolves `to` to a member of `claims`. That is the general shape of this defect, and
  it is the gate the class earns rather than the instance.

## 3. Non-goals (OUT)

- **Not** changing `rule_relpath` itself; it is already correct.
- **Not** changing any descriptor to work around the resolver. The `claims` spelling is right and
  the resolver is wrong; editing the data to match a broken reader is how the wrong answer becomes
  permanent.
- **Not** landing gov's `pre-push` hook into any adopter. That destination becoming *correct* is
  this unit; whether an adopter takes it is `-4`'s coverage report and the adopter's decision.

## 4. Design

### Alternatives rejected

- *Delete `rule_relpath` and keep the basename.* It would make the two spellings agree by keeping
  the wrong one, and push-main's hook would land at the target root forever.
- *Fix only the write loop.* `plan` must promise exactly what `apply` performs. Fixing one of the
  three callers re-creates the divergence one level down, which is the defect this unit closes.

### Files touched (estimate)

`tools/govkit/govkit.py` (~4 lines), `tools/govkit/selftest.py` (2 arms),
`tools/govkit/govkit.py` selfcheck section (1 arm).

## 5. Production-readiness checklist

- security — the current behaviour writes a file to a path the descriptor did not declare, at the
  target's **root**. That is the shape a traversal guard exists to stop, reached through a resolver
  rather than through a path; narrowing it is a security improvement, not a neutral fix.
- perf / scale — N/A; one function call replaces one string operation.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a rule whose source sits outside its `home` keeps the basename
  fallback `rule_relpath` already implements; no new failure state.
- observability — `plan`'s printed destination changes for affected rules, which is how an operator
  sees the fix; called out in the unit's landing note because a changed plan line reads as drift
  otherwise.
- risks — the real risk is a target that already took the *wrong* destination and now holds a stray
  `pre-push` at its root. Measured across both live targets: neither has one, because neither has
  ever been `apply`-ed. Stated so a later adopter with a receipt gets a coverage row, not a surprise.
- testing + left-shift gates — S4 is the left-shift: the class is "a rule's `to` and `claims`
  disagree", gated over every entry, not the one rule that exposed it.
- migration / rollback — none; no on-disk shape changes.
- user docs — none needed; no documented behaviour describes the broken form.

## 6. Acceptance criteria

- **AC1** — `resolve_dests(<push-main desc>, <hook rule>, '.githooks/pre-push', ctx, 'tools')[0][0]`
  equals `.githooks/pre-push`. Observe RED first: at `9ddcc5c9` it returns `pre-push`.
- **AC2** — A rule whose source is a direct child of `home` still resolves to its basename under the
  entry's kit directory — the pre-existing correct behaviour, asserted so the fix cannot regress it.
- **AC3** — `python tools/govkit/govkit.py plan --target <NC>` prints `.githooks/pre-push` rather
  than a root-level `pre-push` for any rule that reaches it, and the run's write/order counts are
  otherwise unchanged from `9ddcc5c9`.
- **AC4** — The new `selfcheck` arm reds when a registry entry's `to` is hand-edited to resolve
  outside its own `claims`, and is green across the shipped registry.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs. Adds three arms and one standing `selfcheck` predicate; adds no new leg file.

## 8. Open questions

- **F1 — should AC4's predicate red, or report?** Red. It compares two spellings inside one
  descriptor that the descriptor's own author wrote; a disagreement there is always a defect, and a
  reported-only check over gov's own data is a check nobody clears.
  RESOLVED (agent, 2026-08-24, delegated): red, under the full-scope approval.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold); both
  resolutions read in source at `9ddcc5c9` and the disagreement confirmed.

## 10. Reuse audit

This unit exists *because* a seam was duplicated: `rule_relpath` is the intended one and
`resolve_dests` re-implemented it inline. The fix is a reuse, not an addition — it deletes the
second implementation and calls the first. `resolve_dests` already receives `desc`, so no signature
changes and no new seam is created. The `selfcheck` arm in S4 extends the existing per-entry
descriptor sweep rather than adding a second pass over the registry.
