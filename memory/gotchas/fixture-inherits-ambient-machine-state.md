---
name: fixture-inherits-ambient-machine-state
description: a hermetic-looking fixture silently reads machine-global config, so it passes everywhere it was written and fails where it was not
kind: class
---

# A fixture that reads ambient machine state it never declared

## Symptom

A self-test is green on every machine that happens to carry some global configuration, and red on
the one that does not. The failure names something inside the KIT, so it reads as a product
regression rather than as an unconfigured fixture — which is what makes it expensive.

## Where it bit

`tools/unattended/unattended.test.sh`. It builds one scratch worktree and sets `user.email` /
`user.name` on it, so it LOOKS hermetic. But it also creates a BARE origin, and check 30 builds its
ahead-commit with `git --git-dir="$ORIGIN" commit-tree` inside that bare repo. A bare repo inherits
nothing from the worktree beside it, so the call resolved identity from global config.

Node `a` has no git identity at all — no `~/.gitconfig`, no `user.*` in any config file,
`git var GIT_AUTHOR_IDENT` errors. So `commit-tree` died, `$ahead` came back EMPTY, `update-ref`
reported `fatal: : not a valid SHA1`, the arm's expected refusal never appeared, and the leg failed
naming the kit's own check-30 message. The bar had 84 of 85 green and the one red pointed at the
wrong component.

It also cost a second diagnosis: the same leg had failed in an earlier run alongside six others that
WERE environmental, so the batch got one explanation and this one rode along inside it.

## The fix

The scratch repo that gets an identity is not the only repo the fixture writes objects into. Every
repo a fixture COMMITS in gets its own identity at creation, bare ones included — not the one that
happens to be a worktree.

Ambient state a fixture can inherit without saying so: git identity, `core.autocrlf`, `init.defaultBranch`,
`$HOME`, locale, `TMPDIR`. A fixture that needs one declares it.

No machine gate. The generalisable protection is that an empty capture is never fed onward — the
`$ahead` above was empty and got passed straight to `update-ref`, which is what turned a clear
identity error into an unrelated SHA1 complaint two steps later.
