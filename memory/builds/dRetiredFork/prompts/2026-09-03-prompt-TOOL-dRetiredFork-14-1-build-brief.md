# Build brief — TOOL-dRetiredFork-14

**Serves:** journal TOOL-dRetiredFork-14

## What is actually duplicated, resolved from the descriptors rather than assumed

All three pairs are byte-identical — 1610, 394 and 207 lines, 2211 duplicated tracked lines, exactly
as §1 measured. But they are not duplicated for the same reason, and the spec treats them as one
class:

- `agent-cap.js` — genuinely TWO descriptor destinations, `{prefix}/hooks/` and `.claude/hooks/`
- `scratch-guard.js` — the same, on the same descriptor row pair
- `recall-opened.js` — **ONE** destination, `tools/memory-recall/recall-opened.js`, role `forked`

So `.claude/hooks/recall-opened.js` is **claimed by no descriptor**. It is tracked in gov and gov
wires it, but nothing ships it and no `to =` produces it. Dropping a destination cannot remove it,
because there is no destination to drop — it is an undeclared duplicate in gov's own tree, which is
a different act from S2's descriptor edit and has to be recorded as one.

## The capability S1b names, and why S1 alone is a no-op

`HOOK_MARKER` is the bare basename `agent-cap.js` and `merge()` returns the object unchanged when
any command in the matcher group already contains it. The module docstring says so outright: the
dedup "deliberately does NOT rewrite a stale hook path". Every already-wired tree — gov's included —
is a no-op today, so passing `--hook-path` changes nothing without S1b.

F0 is ratified for a **fragment-level `hook_path` compare**, not a `--rewrite-stale-path` flag.

## The risk, and the ordering that contains it

gov wires all three through `.claude/hooks/`. Deleting those files while the settings still name
them unwires a security guard in gov's own tree, silently, until someone notices a hook not firing.
The settings rewrite and the file removal land in ONE commit, and `check-wiring.sh` must pass
immediately afterwards — gov is its own first adopter here.

For an adopter the same ordering is mandatory and is NOT automated: the wired command moves to the
surviving copy BEFORE the second copy is withdrawn. F2 is ratified as leaving the withdrawal to the
adopter; this unit deletes nothing from anyone else's tree.

## S3 is the interesting half

Both parity arms assume TWO copies. `scratch-guard.test.sh:183-190` hard-FAILS when the kit copy is
tracked and the wired copy is absent — which is precisely the state AC1 requires after this lands.
So the arms must become self-arming on the RESOLVED destination count, assert against whatever they
find, and REFUSE on zero. A parity arm over a population of one that assumes two is the
green-by-absence shape this repo already has a record of.

## Forks, folded

F0 fragment-level compare · F1 keep `.claude/hooks/` expressible but ship it unused · F2 the adopter
withdraws its own second copy, documented rather than automated.
