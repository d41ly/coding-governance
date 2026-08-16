# TOOL-aMooredAnchor-1 — reproduction transcript, the anchor defeats

**Serves:** journal TOOL-aMooredAnchor-1

Ran 2026-08-11 at base `af6de23`, before the spec was written. Harness:
`2026-08-11-build-TOOL-aMooredAnchor-1-1-repro.sh`, invoked as
`bash <harness> "$(pwd)/tools/unattended"`. It builds the same scratch fixture
`check-unattended.test.sh` builds, copies the kit in, and gives every defeat a control.

## Why there are two controls

Control A proves the fixture is not red for unrelated reasons. Control B is the one that matters: it
forges the mandate and leaves the refs **untouched**, so the leg must red. Without B, a green in the
defeat arms would be indistinguishable from a leg that never ran.

The first draft of this harness had a bug worth recording. Its reset helper deleted every
`refs/remotes/origin/*` ref except `main`, and `refs/remotes/origin/HEAD` is matched by that filter,
so `origin/HEAD` was silently gone in every arm. The arms still went green, but for the wrong
reason, and one of them was measuring a hole nobody had asked about. Deleting a symbolic ref with
`git update-ref -d` also dereferences by default and removes the ref it points at, not itself, which
made the state harder to read. Fixed with `--no-deref` and a full rebuild of `refs/remotes/`, plus
an `assert_refs` line printed by every arm so the fixture state is visible rather than assumed. The
accidental finding became R4, which is real and has no attacker in it.

## Transcript

```
======== CONTROL A — honest tree, unmodified refs. Must be green.
  refs: origin/HEAD=origin/main origin/main=6264942
  >>> GATE GREEN (exit 0, silent) — the honest state

======== CONTROL B — forged mandate, refs UNTOUCHED. Must RED, or nothing below means anything.
  refs: origin/HEAD=origin/main origin/main=6264942
  >>> gate reds (exit 1): UNATTENDED check 9 FAILED — a recorded BASE is not the merge-base this
      history reproduces, and every mandate assertion hangs on that value: recorded dc08909b…,
      computed 62649425… in memory/builds/tRun/RUN.md

======== DEFEAT 1 — run rewrites refs/remotes/origin/main with update-ref (NO env var, no push)
  refs: origin/HEAD=origin/main origin/main=291b665
  merge-base=291b66531277  HEAD=ed2779fbb68c
  >>> GATE GREEN (exit 0, silent) — same forged mandate, now accepted
  driver rc=0 :: unattended: preflight OK — base 291b665312775f5ba0799af076706bd476c842b5 ·
      keepalive k1 · region copied from memory/builds/tRun/README.md

======== DEFEAT 2 — env-var shape: GOV_DEFAULT_BRANCH names a remote-tracking ref the run created
  refs: origin/HEAD=origin/main origin/main=6264942
  >>> GATE GREEN (exit 0, silent) — the gate read the same env var the driver reads

======== DEFEAT 3 — GOV_DEFAULT_BRANCH names nothing; recorded base is 40 zeros
  refs: origin/HEAD=origin/main origin/main=6264942
  var UNSET      -> 1 check-9 line(s)
  var=nosuchref  -> 0 check-9 line(s)
  >>> GATE GREEN (exit 0, silent) — one env var disarms the only BASE assertion on the bar

======== DEFEAT 4 — a clone with NO origin/HEAD (passive degradation, no attacker needed)
  refs: origin/HEAD=UNSET origin/main=6264942
  >>> GATE GREEN (exit 0, silent) — recorded BASE is 40 zeros and the leg never looks
```

## Readings

**R1 is a blocker and is not on the finding's fix list.** The finding treats
`refs/remotes/origin/<default>` as the trustworthy anchor and `GOV_DEFAULT_BRANCH` as the tainted
input. Only the second half is true. `refs/remotes/` is an ordinary local ref namespace;
`git update-ref` writes it with no push, no network and no change to `origin/HEAD`, which answers
`origin/main` throughout. Applying the four listed fixes closes R2, R3 and R4 and leaves R1 open.

**The source says otherwise, in as many words.** `tools/unattended/unattended.sh:113` reads that a
remote-tracking ref is the weakest thing the run cannot rewrite, and that moving it requires a push.
The second clause is false. A comment asserting the hole cannot exist is a plausible reason the hole
survived a Tier-2 review that reproduced three sibling defects.

**R3's differential is the useful part.** The same tree emits one check-9 line with the variable
unset and zero with it set to an unresolvable name. The check is not being made wrong, it is being
switched off, which is why no arm caught it: every existing arm exports `GOV_DEFAULT_BRANCH=main`
at fixture setup, so the suite cannot observe the gate's behaviour without it.

**R4 needs no adversary.** A clone lacking `origin/HEAD` is ordinary — this repo's own docs already
carry `git remote set-head origin -a` as a remedy for two other tools. In that state the gate accepts
a recorded base of forty zeros in silence.
