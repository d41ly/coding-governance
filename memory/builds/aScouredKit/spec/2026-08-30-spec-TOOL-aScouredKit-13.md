# TOOL-aScouredKit-13 — `plan` and `apply` honour the target's own declared kit list

**Status:** OPEN · rev-1 · 2026-08-30 · node a · Tier-2 · base 093730e4 · streams tooling+deployer

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-14 TOOL-aScouredKit-15 |
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round2.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round2.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-6 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-15 |

<!-- /gen:spec-records -->

## 1. Goal

Make the documented no-`--kits` install path install what the TARGET declared, rather than silently
substituting gov's registry default and then failing on an answer the operator was never asked for.

## 2. Scope (IN)

- S1. `resolve_selection` takes the target's `deploy.toml` and, in its default branch, prefers a
  non-empty `kits` list from it over the registry default.
- S2. An entry named there that is not a registry entry is a REFUSAL naming it, matching the
  refusal `--kits` already gives, so a typo cannot silently install a smaller set.
- S3. `plan` and `apply` pass the descriptor they already load one line above the call.

## 3. Non-goals (OUT)

- `intake`. It is the verb that WRITES `deploy.toml` and has none to read, so it keeps the registry
  default and this is stated in the function's docstring rather than left to be rediscovered.
- `adopt`, which already reads the list by choosing the `kits` mode at its call site. It is the
  precedent this unit follows, not a site it changes.
- `--all` and explicit `--kits`, both of which are operator overrides and outrank the file.

## 4. Design

Four verbs resolve a selection and one of them read the target's declaration. The consequence is not
a smaller install — it is a REFUSAL: a target declaring `kits = ["check-wiring"]` gets a six-kit
preview from `plan`, and then `apply` exits 2 over an unanswered hole belonging to a kit the target
never asked for. Because `plan` previews the same wrong set, nothing warns before the failure.

### Data model

`resolve_selection` gains an optional `deploy: dict | None = None`. The default branch reads
`deploy['kits']`, validates every name against the descriptor set, and falls through to the registry
default only when the target declares none. Optional-with-default keeps `intake`'s call site
untouched and makes the omission at that one site a deliberate, documented choice.

### Alternatives rejected

Deciding the mode at each call site, as `adopt` does. That spreads the rule across four functions
and is how three of them came to disagree in the first place. The default branch is where every
caller lands, so the rule belongs there.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Engine | `tools/govkit/govkit.py` | the parameter, the branch, two call sites |

## 5. Production-readiness checklist

- security — the target's `deploy.toml` is target-authored input, and the values reach only a
  membership test against the descriptor set. No value reaches an argv or a path. Unknown names are
  refused rather than defaulted.
- perf / scale — N/A.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an empty or absent `kits` list falls through to the registry
  default, which is the behaviour every existing target already gets.
- observability — `plan` now previews the set `apply` will install, which is the point.
- risks — a target whose `deploy.toml` names a narrower list than it has actually been receiving
  will see a SMALLER install after this change. That is the declaration being honoured, and it is
  visible in `plan` before `apply` runs.
- testing + left-shift gates — `python tools/govkit/selftest.py`.
- migration / rollback — no artifact format changes; no receipt field moves.
- user docs — `WIRE-INTO-PROJECT.md` documents the three-command path and does not describe the old
  substitution, so it needs no edit.

## 6. Acceptance criteria

- **AC1** — When a target's `.governance/deploy.toml` declares `kits = [...]` and
  `python tools/govkit/govkit.py plan` runs with no `--kits`, the preview names exactly that set.
- **AC2** — When the same target is applied with no `--kits`, it installs that set and does not
  exit 2 over a hole belonging to an entry the target did not name.
- **AC3** — When a target declares an entry that is not in `tools/govkit/registry.toml`, the run
  REFUSES naming it, rather than installing a subset.
- **AC4** — When `python tools/govkit/selftest.py` runs, it is green.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · the full bar at the push
boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.

## 10. Reuse audit

The seam is `cmd_adopt`'s existing read of `deploy['kits']` at `tools/govkit/govkit.py`, which is
the behaviour this unit generalizes rather than re-invents, and `resolve_selection`'s own `--kits`
branch, whose refusal text is the model for S2's. No new function and no new validation helper: the
membership test is the one already written twenty lines above. The build's reuse probe is recorded
in `TOOL-aScouredKit-1` §10 and is not re-composed.
