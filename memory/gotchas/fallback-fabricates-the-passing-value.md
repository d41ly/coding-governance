---
name: fallback-fabricates-the-passing-value
description: a degraded-mode substitute spelled with the value some assertion reads as clean turns a broken subject into a silent green
kind: class
---

# A degraded-mode fallback whose substitute IS the passing value

## Symptom

A helper cannot answer honestly — the subprocess died, the reply will not parse, the lookup missed —
so it hands its callers a placeholder and lets them carry on. Every caller's failure branch is
written correctly. The leg still goes green on a genuinely broken subject, and nothing anywhere
mentions the degradation.

The tell is a fallback whose substitute is a *specific* value rather than a refusal. Ask one question
of it: **is there any assertion downstream for which this exact pair is the passing answer?** If yes,
the fallback has a silent-green mode by construction.

## Where it bit

`tools/unattended/check-unattended.sh`, round 7 of `dScriptedRepeat`. Four parser specimen loops were
batched into one `bash -c` per parser to cut process spawns. When the reply had fewer lines than
specimens, the batcher filled every slot with the batch's own exit status and the empty string —
correct, and byte-identical to the unbatched wrapper, *for the shape it was written for*: a body that
would not run at all, which exits nonzero.

The same branch is reached when the batch **ran fine** and the reply merely misaligned, because one
answer contained a newline. Then the exit status is **0**, and `(rc 0, "")` is exactly what both
template arms read as a clean parse:

```
if [ "$rc" -ne 0 ] … elif [ -n "$got" ] … fail
```

A `declared_scalar` patched to emit one extra line **only when its argument spans multiple lines** —
which is the shape the shipped template block has and the shape a comment-leak regression takes — left
the whole leg at **rc 0 with zero output**, in the loop that is the shipped template's only grader.
The single-line specimen batches stayed aligned and passed, so every fixed arm was green.

The equivalence corpus written to justify the batching missed it: gutting the parser for *all* inputs
makes the specimen arms fail first, and their failures made the output identical either way. The
template loop's new silence was hidden behind noise from arms that were still working.

## The fix

Split the degraded shapes and refuse the one you cannot answer for. Empty reply — the body did not
run — keeps the honest substitute, because that is what the un-batched caller saw. A reply that
arrived and will not line up gets its own failure naming what was sent and what came back, and every
slot is filled with a sentinel status no real answer uses, so every caller's rc branch fires.

Two design rules fall out, and they generalise past batching:

- **A degraded-mode substitute must never be a value some assertion reads as clean.** Prefer a
  sentinel that cannot be confused with success, or refuse.
- **When you replace a per-item call with a batched one, the framing is now part of the contract.**
  Either make it unambiguous — a length prefix, a NUL terminator — or assert the reply's shape before
  trusting any of it.

**A staged break must be scoped to the shape under test.** Break the subject for every input and the
arms you already have will fire and mask the new hole; break it for the one input shape the new code
handles differently, and the hole is what you see.

There is **no machine gate** for the class. The documented check is the question above, asked of every
fallback at review time — and for each batched call site, an arm that makes the reply misalign and
asserts the leg reds.
