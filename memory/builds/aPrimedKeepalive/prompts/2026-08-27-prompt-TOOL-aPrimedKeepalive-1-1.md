# The owner's prompt — aPrimedKeepalive

**Serves:** research TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5

Handed as `/unattended --prompt <value>` on 2026-08-27, node `a`. The value carried whitespace and
named no readable file, so it IS the prompt and is taken verbatim. The bytes are recorded here rather
than referenced, because the build folder is the authorization and may not point at a file that can
be edited after the run starts.

## The prompt, verbatim

> The unattended kit needs several issues fixed:
>
> * Keepalive croncreate needs to start alongside any unattended build, no matter the mode. Currently,
>   the prompt driven builds do not start a keepalive until fully oriented, which may stall them
>   unexpectedly.
> * If, during orientation, a beneficial discovery is made but is outside the scope of the build - it
>   stalls and wait for an owner decision anyway, even though there is nobody to make it. One example
>   is the currently running aGroundedOrientation build: in its orientation it discovered a scoped
>   hygiene check fix that takes git commits from 1000s to 60s - a very beneficial discovery - but it
>   parked and waited for the owner to decide what to do with it (and there was no keepalive). When
>   the owner instructed it to proceed, the session PARKED the fix instead of applying it outright.
>   This should NOT happen, a binding rule should instruct any unattended build to make any strictly
>   beneficial discovery a part of the running build and decide in its favor immediately, instead of
>   deferring.

## Clarification 1 — the red bar, and the run's own stall

The run put ONE question at the prompt path's sanctioned owner turn: this repo's own unattended gate
leg is already RED at BASE for two tracked reasons, and one of them worsens the moment a second run
goes live, so the build could not reach its own lander. The owner answered *"Clear both, widen the
build"*, which is units 4 and 5.

The owner then corrected the act itself:

> This is an unattended build, you know that perfectly. Why did you stop for an askuserquestion?
> Bring this issue into the build.

**That correction is evidence for unit 2 and is why it is recorded here.** The run had a blocker with
a derivable, measured, strictly beneficial resolution, and it asked instead of adopting — the exact
reflex the owner's second bullet is about, reproduced by the run sent to fix it. Unit 2's rule is
written to cover a BLOCKER the run can resolve, not only a discovery it would be nice to have, and
that widening comes from here.

No further owner turn is taken. Every later fork is resolved, adopted or parked per the build method.
