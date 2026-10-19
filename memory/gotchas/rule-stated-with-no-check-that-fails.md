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

It bit again in the last three folds' closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-folds-reviews-compared.md`). Five more: the step
gate's later classes joined with no build arming them; an edited render held at update with no planted case; a pinned
target that no edge check parses; `adopt.instructions`' no-overwrite and wiring promises with no fixture; and a
repository's own policy keys with no schema or reader.

It bit again in the night pass two's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two-reviews-compared.md`).
`budgets.enforce`, read by every size gate, was proven on one file. The spike that arms the in-flight ledger never
planted the four end kinds it certifies. A bug class's gated mark, which takes it off review, was self-declared and
checked by nothing.

It bit again in the flow and roles adoption's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-adoption-reviews-compared.md`).
The flow and roles adoption's fixed set, its headline guarantee, had no check that refused an `amends` or a
`supersedes` touching it, only an exclusion. Its widened exclude refusals, its four new step-gate joins and FA-5's
every widening reported had no red case either.

It bit again in the owner's answers' closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two-answers-reviews-compared.md`).
The change feed's ordered, rebuilt-equal promise, the mirror's never-read-by-a-verdict invariant and the pass push's
freedom from the lander's lock each landed with no case that could fail.

## The fix

- A rule lands with the check that fails on its breach, named in the same commit: a pair rule in the
  preset check, a principle's arm in the layer check.
- The check is seen red on a planted breach before it counts.
- A rule with no check yet names the gap that owes one.

It has no machine gate yet: dDeclaredLoop's preset check owes the pair rules, and dOrderedCharter's
layer check owes EX-1's arm (`gap-found-17`).

Related: `armed-but-unreachable-rule` is a rule whose check exists but cannot fire.
