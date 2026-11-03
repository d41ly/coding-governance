**Serves:** research PLAY-dOrderedCharter-38

# Owner instruction — speed the build run up, keeping it unattended

## The prompt

> any way to speed this build up?

> execute keeping the build unattended

— owner, 2026-11-03, after 13 of 57 units had closed, roughly two in three of them after a builder `DIVERGENCE:`
hand-back against specs written at `ce13efbe`.

## What the run was proposing

1. A read-only drift sweep: spec-reviewer agents read the next batch of DEFERRED specs against the code at HEAD and list
   every place a spec no longer matches what the units before it built; one spec-writer pass folds the findings
   before those units dispatch.
2. The main loop's spec-commit chain stops running `tools/check-spec-tokens.py` before the commit; `--dispatch` runs it
   over the tree before every pass, so a red spec still cannot build.
3. The main loop runs the cheap lint legs (layer dependencies, tags, lexicon) after each unit's bookkeeping, so an own
   red surfaces at the unit that caused it.

## How the run applies it

- The drift sweep is not a spec-audit round under `memory/builds/dOrderedCharter/prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-owner-review-cap.md`:
  it records no `--review` round and files no spec-audit record; it is a drift probe of specs against built code, and
  its findings are folded as divergences are, one spec-writer pass at a time. This instruction is the owner's leave to
  run it.
- Each sweep covers the next units in build order only, since every landed unit moves what later specs assume; the
  sweep repeats as the build advances.
- The run stays unattended: nothing here adds an owner turn.
