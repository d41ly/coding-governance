# TOOL-dUnstalledConvoy-29 — built, and what each arm was observed against

**Serves:** journal TOOL-dUnstalledConvoy-29

Thirteen assertions in `tools/govkit/selftest.py`, twelve of them discriminating. The red-first run
reverted `tools/govkit/govkit.py` to `8161b104` — the tree with `subject` present, agreed and
criterion-documented, and with no ratchet — and re-ran the suite unchanged.

## The arms, and the break each one was observed against

| arm | red-first verdict |
|---|---|
| LIVENESS: a pin that disagrees with the manifest REDS | RED — no comparison existed, so a wrong pin was not a wrong anything |
| AC4 `selfcheck --write` regenerates the pin | RED — `govkit: selfcheck takes no arguments` |
| AC4 the generated pin is exactly the derived population | RED — after the sharpening below |
| CONTROL a tree whose pin was just regenerated is GREEN | **passes without the mechanism, by construction** |
| AC1 flipping a subject without moving its pin REDS | RED — the flip was invisible |
| AC1 the refusal names the leg and BOTH values | RED |
| AC1 it says what the move does — leaving the automatic bar | RED |
| AC1 it says it grades the change rather than the value | RED |
| AC2 moving the pin in the same commit passes | RED — `--write` refused |
| AC2 the moved pin records the new value and drops the stale row | RED — after the sharpening below |
| AC3 a NEW leg with no pin row REDS rather than passing | RED |
| a pin row naming a leg the manifest no longer declares REDS | RED |
| AC5 the generated pin's header states it grades change, not correctness | RED |

## The two arms that passed the first red-first run, and why

Both asserted CONTENT of the pin file, and the fixture's hand-written pin already held the bytes
they were looking for. So a `--write` that refused outright left the file already saying what the
arm wanted to read, and the arm was green over a build with no ratchet in it. This is the
`fixture-passes-by-finding-nothing` class arriving through the fixture's initial state rather than
through its population.

Both were sharpened and re-observed:

- the pin is CORRUPTED before the regeneration, so regeneration is what the arm measures;
- the corruption plants a STALE ROW (`zzz gone`) that only a real regeneration removes, so the
  content assertion cannot be satisfied by the starting state.

`CONTROL` is the one arm that stays non-discriminating, and it is labelled rather than dropped: an
assertion that a correct tree is GREEN cannot fail when the mechanism is absent. It is kept because
a ratchet that reds on a correct tree is the other way this fails, and nothing else would catch it.

## The two fixtures the ratchet broke, and what that measured

Adding the pin file broke two existing fixtures at once, in opposite directions, and both breaks
were the check working:

- `scratch_gov(kit_toml)` builds its gov tree with `shutil.copytree(HERE, ...)`, so it inherited
  gov's OWN 85-row pin into a tree with one leg — 85 stale-pin refusals plus one unpinned leg.
- `scratch_gov(mutates, guard)` copies `govkit.py` alone, so it arrived with no pin at all and hit
  the missing-pin refusal.

Each now writes a pin for its own manifest. A third defect surfaced while wiring the arms: that
second helper names its directory from a hash of its arguments alone, so a second call with the
same pair met a directory that already existed and died with `FileExistsError` rather than reusing
or refusing. It takes an optional `tag` now.

## What this does NOT establish

Nothing here is evidence that any leg's subject is RIGHT. The check grades change and says so in
its own header, in the generated file's header, and in every refusal it prints. The criterion that
decides correctness is stated once, at the `subject` field declaration in
`tools/run-gates/run-gates.sh`, and applying it is a review judgement.
