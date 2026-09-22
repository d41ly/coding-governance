# Run mandate — cMendedVintage

**Serves:** journal DEPL-cMendedVintage-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `c`, 2026-09-16. The bytes
travel rather than a reference: the build folder is the authorization, so it may not point at a file
that can be edited after the run starts. The value carried whitespace and named no readable file, so
it is the prompt itself and not a path.

## The prompt

```
build the fix plan per the protocol
```

## What "the fix plan" refers to

The consolidated fix plan delivered in the turn immediately before this one, over an adopter
session's eight findings from running `govkit update --write` against inCMS and NicoCares. That plan
was produced by a five-lens verification fan with batched skeptics: 18 findings, all 18 diagnoses
held, 10 of 18 proposed fixes refuted and reworked. Its phases A–F are this build's units 1–22.

Three of the eight reported findings did not survive as reported and are NOT built here:

- "`update` runs none of the hook wirings" — `apply` does not wire fragments either, so this is not
  an `update` regression. Acting on it as reported would have put a byte-writing path on
  `.claude/settings.json`, which the `merged` role exists to keep gov out of.
- "`update` runs none of the version bumps" — `_resolve_ver_at` is called from all three mutating
  branches and receipt-row versions already advance. Only the in-artifact marker is stale, which is
  the render class.
- "an `index.lock` race" — govkit has no concurrency and cannot race itself. The real defect is
  unconditional and is unit 2.

## The owner's answers, 2026-09-16 — the only owner turn this run has

Asked as one `AskUserQuestion` before the build folder was written, per the prompt path's step 2.

**Scope — how much of the plan this run lands.** *All six phases A–F.* The alternatives offered were
Phase A alone, A+B, and A+B+C+D; the recommendation was A+B on the grounds that it is what stops the
five observed rollbacks. The owner took the full plan.

**Leg emission — `update` emits no gate legs, so every new `[[gate_leg]]` reaches an adopter only
when they re-run `apply`.** *Build it in this run.* The alternatives were a separate follow-up build
(recommended) and accepting it as a permanent manual step. It is coherent with the scope answer
because Phase E is in scope and the leg-emission stage reuses E's write stage; it is unit 13, and it
is sequenced after unit 10 for that reason.

## What the M5 probes changed before the roster was written

The recall probe surfaced three OPEN rows the synthesis did not have, and one of them moved the
plan:

- The regenerate DELETES fixture records govkit ships as engine rows, recorded open against
  `tools/govkit/govkit.py` as the eleventh dPolishedVitrine row. Flipping `GOVKIT_RERENDER` on by
  default without closing that first turns a recorded data-loss defect on for every adopter. It
  became unit 6, sequenced before unit 7.
- Landed sources sit outside the verify and rollback pass, so a kit whose only change is a landed
  file is never verified — the second dRatifiedSeam row, open and deferred there because the fix
  restructures the data-loss machinery. Adjacent to units 1 and 2, and recorded here as prior art
  those units extend rather than rediscover.
- `update --write --kits <one>` stamps `gov_commit` for the WHOLE receipt after grading only the
  scoped rows, which is the thirty-eighth dRetiredFork row. Out of scope for this build, left where
  it already sits.

Each is named descriptively rather than by bare id on purpose: a dash list item leading with an id
is an ANCHOR to `anchor_at`, so citing one that way inside a build folder makes this build appear to
DEFINE another build's id, which hygiene check 13 then reports as a two-folder collision. Observed on
this record's first draft.

The map probe returned no seam for "run a target-side render after landing bytes": the ranked
candidates are name-stem matches on `render_*` in `codebase-map` and `run` in thirteen unrelated
files. The honest answer is that `update`'s effect stage has no existing seam, which is what unit 10
and unit 13 build and what unit 5 declares against.
