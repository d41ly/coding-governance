**Serves:** journal TOOL-aGraftedHelix-37

# Spec brief — TOOL-aGraftedHelix-37, adopted mid-run

Tier-2, streams tooling, `order 21`. The shared brief beside this file
(`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`) states the twelve invariants that bind it.
Read the CURRENT `write_claim` in `tools/unattended/unattended.sh` and `check_claim_push_clear` in
`tools/push-main.sh` before designing; unit 36 (`17c9d4dbe`) built both. In your OWN return, name the
spec you author in `authored` by its unit id, `TOOL-aGraftedHelix-37`, never by its path.

## What was observed

Unit 36 serialised the claim writer and the lander with a directory lock, `claim-push.lock`, in the
git dir. A lock whose recorded deadline has passed, or that carries none and is older than two
minutes, is treated as stale: the writer does `rm -rf` and then `mkdir`. Unit 36's builder reported
the limit and left it unfixed. Two writers that find the same stale lock at the same moment can both
break it. A breaks it and takes it. B, which read the same stale deadline before A's `mkdir`, then
removes A's FRESH lock and takes its own. Both proceed, and the serialisation the lock exists for is
gone. It needs a crash to leave the stale lock, then two writers in one git dir inside one window.
That is narrow but reachable: a beat and a resume tick share a git dir, and a crash is exactly when a
resume tick fires.

## What to decide

Make breaking a stale lock a step only one writer can win, and make the winner re-read the lock it is
about to remove, so it never removes a lock another writer has just taken. Use no new dependency, and
it must work under MSYS bash on node a as well as Linux. Decide what breaks the break-step itself if a
writer crashes inside it, and bound that so it cannot wedge every later writer. Say what the
mechanism still does not cover in the function's header (`WHAT THIS DOES NOT CHECK`), because unit
36's header was silent on this race. The arm must reproduce the double-take on the CURRENT code
before the fix: two writers released together over a pre-staged stale lock, with the count of
writers that proceed recorded. It must show at most one proceeds after the fix, over enough trials to
have seen the race before it.
