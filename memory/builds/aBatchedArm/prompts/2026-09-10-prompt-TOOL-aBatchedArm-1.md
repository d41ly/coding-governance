# The owner's prompt — rebuild the unattended self-checks, under 20 minutes

**Serves:** research TOOL-aBatchedArm-1

Handed to `/unattended --prompt` on 2026-09-10, node `a`. The value carried whitespace and named no
readable file, so it is the prompt itself and is recorded here verbatim. The bytes travel rather than
the reference: the build folder is the authorization and may not point at a file the run can edit.

## The prompt, verbatim

> Continue this session unattended - rebuild the unattended self-checks per your design, following
> the protocol. The checks MUST BE DESIGNED IN AN EFFICIENT WAY that does not take several hours to
> reach its result. Target - less than 20m from start to the final result.

## What "20m" measures, and why the reading is not the ambiguous one

The 20 minutes is the CHECKS' runtime, not this run's: "does not take several hours to reach its
result" is a sentence about the checks, and "from start to the final result" continues it. The
acceptance criterion is therefore a wall-clock figure over the rebuilt suite, which is observable and
is the one thing this build is graded on.

## The one owner turn, and the option chosen

Asked once under the prompt path's step 2, before any build folder existed. The question was which
of two stopping points binds, because the owner's earlier message asked for fewer invocations while
this one gives a wall-clock target, and the two point at different builds:

| offered | content |
|---|---|
| port first, batch only if needed | remove the assertion forks, scope with `--skip 28`, run the existing arms through `tools/lib/lib-selftest.sh`'s pool |
| **batch the arms as well** — CHOSEN | the above, plus a declarative arm table, a partition of independent breaks, one invocation per batch, set-equality of emitted signatures |
| batching only | leave the harness and the forks alone |

## THE OFFER WAS PARTLY WRONG, and the correction is recorded here rather than folded away

The port half of both surviving options is CLOSED by a ratified decision the recall probe surfaced
only after the owner had answered. `TOOL-aPooledSweep-3`: "a port and its own safety property are in
opposition — `arm` takes one POSITIVE substring, these suites assert negatives, so a port rewrites
the assertion and the inventory diff refuses it." This suite carries 101 `miss` and 27 `same`
assertions, none of which has a spelling under `arm`.

The recommendation offered first — "port, low risk, repeat of a port this repo already did" — was
therefore a recommendation to re-open something the repo had decided against, and its projected
~10 minutes rested on a pool whose wall clock cannot fall below its longest member, which is this
suite. Both halves of that recommendation were unfounded and the owner read them before answering.

**What survives the correction is the half the owner chose.** Batching is unblocked, and it is the
follow-up `TOOL-aPooledSweep-7` names without building: "Falling further means dividing that one
suite." No second owner turn was taken, because the chosen work is unaffected — only the option they
did not choose was closed, and the run says so here rather than discovering it in a wrap-up.

## What was already measured before this run, and is not re-derived

- `TOOL-aTracedSpawn-2` bounds de-spawning at roughly 2 s per invocation of real non-spawn work, so
  a ~586 s floor stands at 293 invocations. The target is reachable by cutting invocations only.
- `TOOL-aDrainedSluice-5` N17 found the batching premise FALSE for a sibling harness whose callers
  short-circuit. Reproduced against this suite on 2026-09-10: eight staged breaks emitted four
  checks, one of them tripping check 1, whose branch exits and truncated the run.
- `TOOL-aQuenchedHarness-9` records this suite RED at BASE, so the equivalence property is verdict
  identity per arm rather than a green run.
