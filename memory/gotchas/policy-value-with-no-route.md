---
name: policy-value-with-no-route
description: a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run
kind: class
universal: false
---

# A catalogued value with nowhere to go

## Symptom

Every behaviour is a switchable policy, so a key lists its allowed values and a preset picks one. The
items that read the key are written for the default. A non-default value then has no witness arm, no
route or no owner item. A preset that selects it either behaves like the default or stops with no next
item. The catalogue row and the preset table both read complete, because each lists the value.

## Where it bit

The library round, 2026-10-16, in the step definitions
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`) and v2's catalogue
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`). The round's
review (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md`, M1, M2 and
M7) found three keys whose non-default values had no arm:
- `review.unclassed: reason` and `owner-rules` had no `none` disposition in `review.report`, and no
  owner route;
- `decisions.major: author-owner-ratifies`, the strict preset's value, had no owner item;
- `reuse.propose`'s witness typed the default's population in front of the key.

The expansion round, 2026-10-16, hit it seven times, though the class was on both of its review runs'
checklists (`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md`, `[patterns]`). `build.closes: after-release-verifies` held nothing; the
values `velocity` selects for five observability keys, `observability.run-record` among them, had no
arm; and `currency.on-behind: red`,
`any-commit`, `pull-only`, `every-landing`, `owner-approves-prod`, `deploy.runs` and
`verdict: remote-ci` routed nowhere. The fold's closing review found two more inside the fold: `app-only`
had no arm under `GATE_POST_MERGE=ci`, and `owner-cut` named no trigger and no key for its decline
(M3 and M4 of `memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold.md`).

It bit again in the shape audit, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`). Five more values with
no route: `commits.edge-check: commit-msg` and `commits.squash: refuse`, both in the strict preset, `accept-loss`,
`trace.identity: salted`, which no record defined, and `memory.legacy-anchors: retag`, whose adopter step had no owner.

It bit again in the last three folds' closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-folds-reviews-compared.md`).
`instructions.stale`'s `refuse`, which the strict preset selects, and `warn` had no arm: only the default `order` was
planted. Each value now has its arm and its planted semantic change.

It bit again in the night pass two's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two-reviews-compared.md`).
`budgets.enforce`'s `record` had no meaning or arm, and the presets selected `flow.scenario-conflict: declared-order`,
`flow.adapt: owner-approves`, `flow.promote: owner-only` and `build.unit-holders: driver-only`, which no reading
clause routed or witnessed.

It bit again in the flow and roles adoption's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-adoption-reviews-compared.md`).
Excluding a gov item that `review.breakpoints` names, or a lens `review.opt-in` selects, composed green, so the
breakpoint or the lens would never fire.

It bit again in the owner's answers' closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two-answers-reviews-compared.md`).
`memory.mirror` named an adapter that answers other nodes' reads, and no session-side read was routed to it.

It bit again in the parked debt's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-parked-debt-reviews-compared.md`).
`run.on-owner-silence` offered `remind-then-park` and `wait` with no route, `wait` never ended, and a set
`build.spend-cap` had no outcome at the cap.

## The fix

- For each key an item reads, write each catalogued value's arm into the item: its witness, its route,
  and any owner item, with every outcome routed.
- Never type the default's guard in front of the key: the key selects the population.
- Walk each preset through the transition table before calling a catalogue row done, and before the
  settlement commits: a checklist entry names the class, and only the walk finds the value.
- Walk the cross products too: each value of a key that names a witness against every value of the key
  that decides whether the witness exists, and each value that selects a trigger against the
  idempotence key it fires under.

The design records under `/build/` are its population. It has no machine gate yet: the join that
dDeclaredLoop owes beside the transition table (`gap-flow-15`) now names this walk.
