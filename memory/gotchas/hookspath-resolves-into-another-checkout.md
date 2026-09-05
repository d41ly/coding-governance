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

**A check on this IS WRITTEN, as of `TOOL-aWeldedTribunal-7`, 2026-09-04.** `tools/check-wiring.sh`
check H compares the resolved `pre-commit` and `pre-push` against this tree's tracked blobs and
reports a divergence naming both hashes, the resolved path, and the branch the supplying checkout is
on. A hook this tree does not TRACK prints a `skip` rather than a finding.

**It reports at `note` severity and not as a wiring failure, and that is a decision.** The reasoning
is at the call site in `tools/check-wiring.sh`, beside the list it acts on, and is deliberately not
repeated here: this record owns the CLASS, the call site owns why this instance takes the severity
it takes. The two used to carry the same paragraph word for word.

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

`tools/check-wiring.sh` now does exactly this, at SessionStart and on `--check`, over both tracked
hooks. What it does NOT do is PREVENT the divergence: a push made after the report still runs the
other checkout's hook, and closing that window needs a refusal inside the hook itself — which is a
separate decision about what the push boundary REFUSES, and is a filed follow-up rather than
something this record should imply is done.

So the landing-boundary documented check below still stands. The report tells you which hook will
run; it does not make the right one run.
