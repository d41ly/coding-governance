---
name: core-depends-on-an-optional-part
description: a core item, leg, field or preset cannot run, or cannot be enforced, without an expansion or an optional component, and the dependency hides behind the guard or Absent clause that seems to degrade it
kind: class
universal: false
---

# The core reaching into an optional part

## Symptom

P28 lets an expansion attach to the core, never the other way. A design moves something into the core,
or writes how the core behaves without an expansion, and the dependency survives in a form that reads
as safe: a guard that turns a missing component into "not asked", an Absent clause that refuses by key,
or a core field whose only enforcement lives in the expansion that uses it. Each piece reads as
degrading gracefully, so nothing looks wrong until the optional part is absent.

## Where it bit

The expansion round, 2026-10-16, in
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`. Its two
reviews (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-a.md` and
run B's report beside it) found four:
- the two lexicon drift signals became core legs, though they import the optional lexicon kit through
  the `resolve_kit_dir` calls in `tools/drift-audit/drift_report.py` (run A's M15, run B's M4);
- distribution's Absent clause refused any preset naming `release.cadence` or `deploy.currency`, which
  every shipped preset names, so a core-only install could select no preset (run A's M4, run B's H4);
- the grant on every adapter row was a core field, enforced only by integrations' gates and keys (run
  B's M9);
- under `GATE_POST_MERGE=ci` with integrations absent, `deploy.core` had no producer for its witness
  (run B's M6).

## The fix

- Before a thing moves into the core, grep its source for an import or a resolver call that reaches an
  optional kit. Move only what has none; what reads an optional part stays that part's, as a pack it
  registers at a core point.
- A core field is enforced by the core layer that declares it.
- An expansion's Absent clause says its keys go unread, never refused. `policy.on-missing-expansion`
  governs only a value, on a key the core reads, that selects an expansion's behaviour (LR-4).
- Probe: install the core alone and load each shipped preset. Expect a refusal only for a value, on a
  key the core reads, that selects an absent expansion, and none for a key an absent expansion owns.
  Walked by hand over v2's presets on 2026-10-16: `strict` and `guarded` are refused for
  `build.closes: after-release-verifies` (LR-4), and no preset is refused for any other key.

It has no machine gate yet. dOrderedCharter owes the check that the core never depends on an expansion
or an optional component (`gap-found-17`), and dDeclaredLoop's preset check owes the core-only preset
load above. Until they land, this entry is the guard.
