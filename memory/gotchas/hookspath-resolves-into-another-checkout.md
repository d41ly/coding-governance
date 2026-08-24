---
name: hookspath-resolves-into-another-checkout
description: core.hooksPath is repo-global and absolute, so in a multi-worktree layout every push is gated by whatever the primary tree currently has checked out
kind: class
universal: false
---

# The hook that gates your push comes from somebody else's branch

## Symptom

A worktree lands a change to `.githooks/`, the bar is green, the push succeeds — and none of the
new hook logic ran. The hook that executed was an older copy of the same file, sitting in another
worktree's checkout, on a branch that has nothing to do with the change.

Nothing reports it. The push output looks exactly like a correct one, because the RUNNER comes from
your tree and only the HOOK comes from elsewhere.

## Where it bit

`TOOL-dUnstalledConvoy-26` through `-33`. The build added a predicate to `.githooks/pre-push` and a
policy file the hook sources. It landed from a worktree on `main`, and `core.hooksPath` in this repo
is the absolute path `C:\projects\coding-governance\.githooks` — the PRIMARY tree's working
directory, which at that moment was checked out on an unrelated contrib branch.

So the push ran that branch's `pre-push`: no `gate-env.sh` sourcing, no predicate 8. `GATE_SELFTESTS`
was never set, 39 legs were held, and the boundary's new coverage check did not exist. The pushed
tree was verified anyway — a separate full bar with the switch on had already gone green and stamped
that exact commit — but the boundary itself was the old one, and nothing said so.

## Why it survives review

`core.hooksPath` is set once, per repository, and it is SHARED by every linked worktree — that is
git's design, not a misconfiguration. The wiring checker asserts it is set and points at the tracked
`.githooks/`, which it does. What no check asks is *which revision of `.githooks/` is sitting there
right now*, because the answer depends on a different worktree's HEAD.

It is invisible in the ordinary case, where the primary tree is on the default branch and its
`.githooks/` is the landed one. It bites exactly when the primary tree is parked on a feature branch
— which the charter already calls the root cause of concurrent-session collisions, for other reasons.

## What to do

**Before trusting a push boundary, resolve which file actually ran.** Two commands, and neither is
inferable from the push output:

```bash
git config core.hooksPath
git -C "$(dirname "$(git config core.hooksPath)")" rev-parse --abbrev-ref HEAD
```

If that branch is not the one you landed, the hook that gated you is not the one you shipped.

**Do not fix it by editing the other checkout.** That is another session's working tree. Either land
when the primary tree is back on the default branch, or verify the boundary's obligations yourself —
run the full bar with every switch the boundary would have set, and say in the landing report which
hook actually ran.

**A gate on this is possible and is not written.** `check-wiring.sh` already resolves
`core.hooksPath`; it could compare the resolved directory's blob against the tracked one at HEAD and
report a mismatch. That is a check about the OPERATOR's environment rather than the tree, which is
why it is worth stating as a documented check here first.

## Related

[[fresh-worktree-crlf-reds-the-bar]] is the same shape from the other side — a property of the
worktree you are in rather than of the commit you are making. Both are cases where the thing being
verified is not the thing that will run.

## Its gate

**No machine gate on the bar, and the reason is that the fact lives outside the tree.** Every leg
grades a commit; this grades which file a DIFFERENT worktree has checked out at the moment you push,
which no commit can pin and no bar can reproduce.

What replaces it is a **documented check**, run at the landing boundary and nowhere else: resolve
`core.hooksPath`, resolve the branch of the checkout it points into, and say in the landing report
which hook ran. A landing report that does not name it is a report that assumed it.

The nearest thing to a gate is `tools/check-wiring.sh`, which already resolves `core.hooksPath` and
already runs at SessionStart — it could compare the resolved directory's `pre-push` against the
tracked blob at HEAD and report a mismatch. That is opened as a backlog item rather than written
here, because a check whose subject is the operator's environment needs a decision about whether it
reds or reports, and this record is not the place to take it.
