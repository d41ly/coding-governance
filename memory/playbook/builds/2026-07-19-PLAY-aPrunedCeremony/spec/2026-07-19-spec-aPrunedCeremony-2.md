# PLAY-aPrunedCeremony-2 — diff-scoped gates are fail-closed and coarse

**Status:** INPROGRESS · rev-2 · 2026-07-19 · node a · Tier-1 · base bf7f2c22 · reviewed wf_2f11fd07 · ratified 2026-07-19

## 1. Goal

Capture the most expensive lesson of inCMS `ARCH-aTrimmedGauntlet-2` (its RD15 reversal) as a
gate-discipline rule: diff-scoping which legs run is safe ONLY when it is fail-closed and coarse. An
unclassified path runs the full bar; a leg must not be guarded on a path set NARROWER than the
complete input whose change can flip its verdict — because a test reads its real inputs INDIRECTLY
(through a shared module), and a too-narrow guard silently skips the leg the diff needed. The trap is
indirection, not the guard mechanism itself.

## 2. Scope (IN)

- S1 — Add the fail-closed-and-coarse scoping rule to `parallel-coding-governance.domain-rules.md`
  §10 (the uncapped overflow companion), NOT the template — the template has 86 bytes of headroom
  under a hard gate (review R-PLAY-2-HIGH). It sits alongside PLAY-aPrunedCeremony-3's vacuous-gate
  entry as a green-by-absence discipline.
- S2 — If the template §7 needs a pointer at all, add at most a byte-neutral half-clause folded onto
  an existing §7 line (e.g. PLAY-aPrunedCeremony-1's reworded gate line), never a new bullet;
  re-measure `check-template-size.sh` after.
- S3 — Name the real failure the rule prevents (a scoped run skipping the leg the diff needed) and
  cite its ACTUAL home in the kit: the green-by-absence family at template §7 L133 (glob/collection)
  and §16 L205 (skipped-leg reporting) — NOT "§10", which had no such phrase before this build
  (review R-PLAY-2-MED).

## 3. Non-goals (OUT)

- Not shipping a scope-surface artifact (inCMS's `gate-scope.json`) into the kit — `run-gates.sh`'s
  `leg_if_changed` scopes only its own self-test legs on their own source; this spec is the guardrail
  WORDING, not an artifact.
- Not banning the kit's own `leg_if_changed` — it guards a self-test on the exact source that flips
  its verdict, which is the SAFE case (guard = full input set, no indirection). Only NARROWER-than-
  inputs guards are the trap (review R-PLAY-2-MED, §4).

## 4. Design

### Inventory

| Edit site | Change |
|-----------|--------|
| `.domain-rules.md` §10 | Add the fail-closed-coarse scoping rule (S1). |
| template §7 (optional, byte-neutral) | At most a half-clause pointer folded onto an existing line (S2). |

Proposed `.domain-rules.md` §10 entry (house style — one dense sentence + fix):

```
- Diff-scoping which gate legs run is legitimate economy but ONLY fail-closed and coarse: an
  unclassified/unrecognized path runs the FULL bar, and never guard a leg on a path set NARROWER than
  the complete input whose change can flip its verdict — a test reads its inputs INDIRECTLY (through a
  shared module), so a too-narrow guard skips the leg the diff needed and the scoped run passes
  green-by-absence (template §7/§16). Guarding a self-test on its OWN source is safe (guard = full
  input); a per-file "this file → these tests" map that omits the indirect readers is the trap.
```

### Alternatives rejected

- **Put the rule in the template §7.** Rejected: 86-byte headroom under a hard gate (wf_2f11fd07);
  domain-rules is the kit's designated overflow companion (`check-template-size.sh` L25-26).
- **Ban per-path guards outright (rev-1 wording).** Rejected: that bans the kit's own
  `leg_if_changed`, which §3 praises. Discriminate on indirection (guard narrower than the verdict's
  full input set), not on the map shape.
- **"Two tiers is the ceiling" (rev-1).** Softened: two tiers is the recommended default, not a hard
  ceiling for a project-agnostic playbook — the invariant is fail-closed + no-narrower-than-inputs.

## 6. Acceptance criteria

- AC1 — When `.domain-rules.md` §10 is read, it contains a rule that an unclassified path runs the
  full bar and that a leg is never guarded on paths narrower than its verdict's full input set,
  citing the green-by-absence family at template §7/§16.
- AC2 — When `bash tools/check-template-size.sh` runs after any (byte-neutral) template pointer edit,
  it exits 0. The `.domain-rules.md` addition has no machine size cap (it is the overflow companion),
  so its acceptance is a read confirming the rule is present and fits §10.

## 8. Open questions

- **Fork — domain-rules §10 vs a new gate-discipline sub-head?** RECOMMEND: §10 (recurring bug
  classes) — the rule prevents the green-by-absence bug class and sits next to PLAY-3's vacuous-gate
  entry; a new sub-head is more ceremony than a one-liner warrants.

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
- rev-2 · 2026-07-19 · folded review wf_2f11fd07: externalize to `.domain-rules.md` §10 (template
  budget, R-PLAY-2-HIGH); corrected the green-by-absence citation to template §7 L133 / §16 L205 (not
  §10); reworded "never a per-path map" to discriminate on indirection so the kit's own
  `leg_if_changed` is not banned; softened "two tiers is the ceiling"; status → SPECCED.
