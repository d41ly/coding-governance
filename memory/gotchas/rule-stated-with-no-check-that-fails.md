---
name: rule-stated-with-no-check-that-fails
description: a principle, a constraint between two keys or another rule is added in prose with no check that can fail on its breach, so it binds nothing and nobody can see that it does not
kind: class
universal: false
---

# A rule with nothing that fails on it

## Symptom

A design adds a rule: a principle's clause, a constraint between two keys, an ordering. It is stated
clearly, often in a Why column or a principle's last sentence, and every reader agrees with it. No check
names it, so a configuration or a kit that breaks it loads green, and the rule's presence reads as its
enforcement.

## Where it bit

The expansion round, 2026-10-16:
- `runtime.journal` had to be at least `review.loop.window-days`, stated only in the Why column of the
  catalogue in `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`,
  while the preset check refused only a missing key or a value outside the key's own schema (review A's
  L7, review B's M19);
- P28 gained EX-1's rule that expansions meet only through the core, and no check in the chain could
  fail on one expansion using a point another declares (review B's M18).

It bit again in the answers fold, 2026-10-18 (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-answers-reviews-compared.md`): the `Gov-Session:`
trailer was to be written "as `trace.identity` says", and `runtime.act-auth` was to try api-key last, each with no check
that could fail. Both now name planted arms, seen red once built.

It bit again in the shape audit, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`). Seven rules of the
converged design had no check that could fail: P38's upgrade step for every adopter-visible change, P35's `not-local`
and `pruned` states, P34's rationale apart, three of P37's seven legs, the plan's claim that every hop of the cycle
closes, the `[docs]` rule over `help/`, and two settled owner answers no clause carried. Each now names its arm, the
step gate first.

## The fix

- A rule lands with the check that fails on its breach, named in the same commit: a pair rule in the
  preset check, a principle's arm in the layer check.
- The check is seen red on a planted breach before it counts.
- A rule with no check yet names the gap that owes one.

It has no machine gate yet: dDeclaredLoop's preset check owes the pair rules, and dOrderedCharter's
layer check owes EX-1's arm (`gap-found-17`).

Related: `armed-but-unreachable-rule` is a rule whose check exists but cannot fire.
