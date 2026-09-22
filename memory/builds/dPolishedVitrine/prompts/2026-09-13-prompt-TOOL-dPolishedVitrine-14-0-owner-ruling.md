# Owner ruling — what to do about a unit built by hand after its run landed

**Serves:** journal TOOL-dPolishedVitrine-14

The owner's choice, verbatim, as the orchestrating session relayed it on node `d`, 2026-09-13. It
travels here as bytes rather than as a reference, because a ruling that lives only in a chat
transcript cannot be re-read by the session that lands this build.

## The option chosen

> Waive + fix the kit (Recommended)

## The situation the question put to the owner

The question's own wording was not relayed. What was relayed is this description of it, which is
reproduced as the orchestrating session wrote it:

> a NicoCares unit (PKG-dPolishedVitrine-14) was built ATTENDED, by hand, a day after its build's
> unattended run had reached LANDED; closing its spec reds two unattended legs that grade every
> CLOSED unit in a build whose RUN.md pins a run base — pass-order (the spec and code went into one
> commit: a genuine miss, to be waived in nc) and brief-recorded ("BUILT at 85ca6662 with NO brief
> row in RUN.md at that commit").

## The kit fix the choice selected

> brief-recorded should check only units built DURING a run.

## What the ruling does and does not settle

It settles both halves of the two reds. The `pass-order` red is a real miss, because the spec and
the code went into one commit, so NicoCares WAIVES it in its own tree and the leg is not changed.
The `brief-recorded` red is the kit's defect, because no run was live to hand that unit a brief, so
the leg changes to grade only units built during a run.

It does not settle the mechanism: which predicate decides "during a run", how a retired run-state
record takes part, and whether anything stops a run from claiming it had finished. The spec's
section 4 records those with their grounds, and its section 8 marks them as delegated resolutions,
not the owner's.
