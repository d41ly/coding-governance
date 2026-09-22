# Build brief — DEPL-cMendedVintage-9

**Serves:** journal DEPL-cMendedVintage-9

`TOOL-cMendedVintage-2` withdrew the one live descriptor landing a file under
`{memory_root}/project/`. This unit makes the class unrepeatable. Read the spec whole first.

*Standing note: briefs in this build have carried five claims measurement disproved. Anything below
I have not run is marked UNVERIFIED.*

## Why a gate and not just the withdrawal

`{memory_root}/project/` is a CLOSED name set. Check 3 of the hygiene gate admits a hardcoded
whitelist plus whatever the target declares in `PROJECT_REGISTRY_EXTRA`, and gov can widen neither at
an adopter: the whitelist reaches them only on a later `update --kits memory-tree`, and a FORKED
checker takes it never — inCMS's is forked, which is why widening was never the fix.

So a descriptor landing a file there ships a red gate to somebody else's repo, and the only place gov
can catch it is in its own `selfcheck`, before anyone installs anything.

## What I verified myself, so you need not re-derive it

The withdrawal landed clean and atomically in `3ca2f144`: the seed rule is gone, the template is
deleted, and the `[[gate_leg]]` argv lost its registry element — all in one commit, which was the
hard constraint.

I also measured the thing the withdrawal rested on: `sh_hygiene.py` with NO registry exits 1 and
reports the undeclared sites, and with an EMPTY registry exits 1 reporting the same. Absent and empty
are the same verdict, so removing the seed changed no adopter's first-install outcome. Gov's own leg
still passes because `tools/gate-legs.json` keeps the registry argument — 19 declared sites, rc 0.

So there is exactly zero live instance for your gate to trip over, and it should go green here.

**If it reds, do not relax it.** That means a second descriptor lands under the reserved prefix and
the gate has found a real one on its first run. Report it.

## Observe the RED, and build the fixture

Stage a fixture descriptor whose destination resolves under `{memory_root}/project/`, see the refusal
name it, unstage. Do not stage the break by editing a real descriptor and leaving it. The previous
gate unit did this well: it observed its red twice, once on a fixture and once against the shipped
descriptors in a detached worktree at BASE, because a fixture proves a mechanism only for the
fixture's own values.

## The refusal-join pins

`refusal_join.py` carries an anchor set and two shrink-only pins. Adding a refusal branch moves them.
Update both in the same commit, and say the numbers you measured rather than guessing them — a
derived count typed into prose beside its source is the two-answers class and the checklist has
caught it twice in this build.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`. Spell no `tools/<kit>/…` path in
shipped prose — this unit edits `WIRE-INTO-PROJECT.md`, which is the single highest-leverage file for
that ban, because it PRESCRIBES install paths. Re-declare with `--dispatch` if your write set grows.
