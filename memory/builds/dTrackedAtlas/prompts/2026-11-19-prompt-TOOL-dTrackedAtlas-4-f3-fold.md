# Revision — dTrackedAtlas: TOOL-dTrackedAtlas-4 rev-7, fork F3 resolved by the owner

**Serves:** research TOOL-dTrackedAtlas-4

## The prompt

> Rewrite the branch to drop the four Red-fix trailers, re-pin the schedule, approve unit 4's loop.toml row then land it

## The brief

### Goal
The owner approved option (a) of fork F3 in `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md` on 2026-11-19, in the words quoted above. Fold that into the spec as rev-7, so unit 4 builds: one `[[hook]]` stage row in `tools/loop/loop.toml` claims its `PostToolUse` hook, beside the dossier claim rev-5 added.

### Items
1. Mark F3 resolved with the closed fork mark the spec format states, naming the owner and the date: `RESOLVED (owner, 2026-11-19): (a), the one [[hook]] row in tools/loop/loop.toml, stage = ["step.deploy"].` Correct every sentence citing F3 as open, including the F1 sentence that points at it.
2. Specify the row exactly in section 4, in the shape the other `[[hook]]` rows of `tools/loop/loop.toml` take (read them), and add `tools/loop/loop.toml` to Files touched. A `tools/` path makes this a shipped kit edit: set the tier the kickoff engine assigns to one.
3. Set the status token from DEFERRED to SPECCED, drop the trailing `advances TOOL-dTrackedAtlas-7` and write `closes TOOL-dTrackedAtlas-7` in its place, keeping every other field of the header.
4. Add to section 7 the legs that grade the row (the `loop stage coverage` leg and any loop-table leg that reads `[[hook]]` rows), by their names in `tools/gate-legs.json`.
5. Bump the rev and add one revision-log line naming this record and the owner's resolution; no other design change.

### Acceptance
`bash tools/unattended/unattended.sh --plan dTrackedAtlas --paths` grades TOOL-dTrackedAtlas-4 READY, not FORKED; `--check-specs dTrackedAtlas TOOL-dTrackedAtlas-4` prints no refusal; `check-memory-hygiene.sh --only 12 --spec <path>` and `check-spec-tokens.py --spec <path>` are clean; every figure typed before a unit word carries a pin on its line or sits in a code span on that line.

### Gates
The spec-format, spec-token and naming-lexicon checks the role allows; no other gate.

### Non-goals
No change to the hook's design; no product code; no commit and no index render, which the main loop does.
