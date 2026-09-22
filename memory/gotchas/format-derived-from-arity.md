---
name: format-derived-from-arity
description: a producer that picks its output FORMAT from the number of items has two shapes, and a consumer written against the many-item one reads the single-item case as empty
kind: class
---

# One item is a different format, and the consumer reads it as none

## Symptom

A producer is taught to handle several items where it handled one. To keep every existing caller
byte-identical, the framing that separates the items is emitted only when there is more than one:
one item, no framing; two or more, framed. It reads as careful backward compatibility, and every
existing caller is genuinely unaffected.

The new consumer parses the frames. Handed a population of one, it finds none of the lines it is
looking for and concludes the producer graded NOTHING. If that consumer has a liveness assertion —
and a consumer that counts verdicts usually does — the assertion fires and reports a broken producer
over a perfectly healthy one.

It survives testing because the developing corpus is large. Every fixture written while building the
feature has many items, because that is the case the feature was built for. The one-item shape is
never produced by any test the author writes, and it is the shape every small adopter has.

## Where it bit

`TOOL-aQuenchedHarness-10`, node `a`, 2026-09-07. `tools/unattended/unattended.sh`'s `--plan` verb
gained the ability to take several build slugs in one process, framing each build's output with
`unattended-plan-open:` and `unattended-plan-rc:` lines. The framing was conditioned on `$# -le 1`
so that the single-slug form stayed byte-identical.

`tools/unattended/check-unattended.sh` check 30 reads those frames to count verdicts. On the real
corpus it always asks about several builds, so it always got frames, and the whole-corpus A/B was
byte-identical across three runs. `cross-component.test.sh`'s fixtures hold ONE build. There the ask
was one slug, the driver emitted no frames, the loop counted zero verdicts, and the check red three
arms with *the driver returned no verdict for any build this check asked it about* — over a driver
that had answered correctly.

Two rounds were spent on the wrong cause first: the liveness canary was widened from one build to a
sample of three, which is a real improvement and fixed nothing here, because the fixtures have only
one build to sample.

## The fix

**Make the format a DECLARED MODE, never a consequence of the item count.** The caller that parses
frames asks for frames:

```sh
bash unattended.sh --plan --framed "$@"     # framed at any arity, one slug included
bash unattended.sh --plan "$slug"           # the historical shape, unchanged
```

The producer then has one shape per declared mode instead of one shape per population size, and
backward compatibility is still exact — it is carried by the absent flag rather than by a count.

**And test the boundary the corpus cannot reach.** A feature built for many items needs a fixture
holding exactly one, and one holding zero. Those are the two the developing corpus never supplies,
and they are every new adopter's starting state.

## What it is not

Not `empty-field-collapses-unless-it-is-last`, which is about a field vanishing inside a line the
producer did emit. Here the lines are absent entirely and the parse is correct on what it received.

Not a backward-compatibility failure: every pre-existing caller was byte-identical throughout, which
is exactly why the change looked safe.

## The gate

There is **no general machine gate** — nothing in a tree can know which of a producer's shapes a
given consumer parses. What replaces it is a documented check, one line: **a producer whose output
format varies must vary it on a declared mode, and any consumer that parses that format is exercised
against a population of one and of zero.** Run it as part of the recurring-bug-class checklist over
any diff that teaches a single-item interface to take many.
