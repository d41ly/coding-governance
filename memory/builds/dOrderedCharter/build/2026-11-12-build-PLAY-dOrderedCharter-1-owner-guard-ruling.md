# dOrderedCharter — the owner's ruling on the policy guard

**Serves:** journal PLAY-dOrderedCharter-55

## The words

> What are you talking about, this whole process is unattended, how can there be files only the owner can commit.

> where did this rule come from at all? Fix it.

> no, you must be misinterpreting it. This is the first time this rule ever comes up, dozens of builds landed since 10-14 and
> it never appeared

— owner, 2026-11-12, after the run held on `--prepare` (`2026-11-12-build-PLAY-dOrderedCharter-1-owner-landing.md`).

## What the main loop found

- The rule's origin: the owner's design answer R4.2, "Owner-only gate-checked by default, but switchable mode per repo the same
  way as other switchable policies work" (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md`,
  section R4.2), asked about who may change a POLICY.
- TOOL-dGroundRules-6, committed `4c1f59ccd` on 2026-10-24, built a stand-in guard that enforces that default without reading the
  key, and listed three neighbours of the policy file beside it: its JSON mirror, `.governance/instructions.toml` and
  `.governance/deploy.toml`. The switch, the key's other two values, is TOOL-dDeclaredLoop-2, still DEFERRED.
- No non-merge commit since 2026-10-24 changed `.governance/policy.toml`, `.governance/deploy.toml` or
  `.governance/instructions.toml` (DERIVED at `deea5f18f` by `git log --no-merges --since=2026-10-24` over the three paths); the
  mirror passed through the guard's render exemption. So the guard never bit until this build, whose unit 55 and unit 31's upgrade
  step are the first changes to `deploy.toml` since it landed.

## The ruling, as the main loop acts on it

No file is owner-only to a run working under its build's mandate. Unit 84 makes the guard admit a guarded change committed by an
agent on the run branch of a live unattended run, and makes the lander's prepare commit what its upgrade steps write before it
regenerates. Hand edits outside a run keep the guard as it is.
