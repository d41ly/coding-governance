**Serves:** research TOOL-dMindYourWords-1 TOOL-dMindYourWords-11

# Brief: dMindYourWords' spec 11 re-grounded against TOOL-dTotalRecall-2

## The prompt

> If a build has mismatches, write a re-ground brief in its `prompts/`. `gov-spec-writer` agents fold
> the brief, with rev bumps, §9 lines and deviation records as the 2026-10-28 re-grounds did.

— the dClosedLoop session's hand-off to this session, 2026-11-03, relaying the owner's ask for a full
cross-read of dMindYourWords, dShippedRelease, dScopedBuild and dTendedCadence.

## The brief

### Goal

Revise TOOL-dMindYourWords-11 so S10's sentence on the `lexicon-declaration` row's writer says what
TOOL-dTotalRecall-2 states on origin/main at `66c5b8dbf`. The spec keeps its own design; only the one
sentence about the door changes.

### Items

Read the cross-check record first,
`memory/builds/dMindYourWords/build/2026-11-03-build-TOOL-dMindYourWords-1-parents-crosscheck.md`. It
has one MISMATCH, its row 2. Section 2 of the return in
`memory/builds/dMindYourWords/build/2026-11-03-build-TOOL-dMindYourWords-1-crosscheck-returns.md`
quotes both sides and states the change. Re-read both sides before you edit. A row the parent's text
does not bear out is not edited: return it as refused, with the line that refutes it.

- **Row 2, the writer stays `hand`.** myw11:113-115 says "the writer is `hand` because the
  declaration is edited by hand and admitted by S3, until TOOL-dTotalRecall-2 registers a door". tr2
  S9 (tr2:80-84) gives `writer = "gov_record.py new <kind>"` only to `hand` rows whose `schema.form`
  is `fields`, and says "a `hand` row of another form keeps `hand`, and the pass commit's `Decided:`
  trailer names the unit or kit owning its door"; tr2:57-58 writes a non-`fields` row only by a kind
  verb of S7; tr2:175-176 adds only `build-readme` and `spec`. S10's row has `schema` form `rows`, so
  tr2 adds no door for it. Drop "until TOOL-dTotalRecall-2 registers a door" and say the row keeps
  `writer = hand` because it is a `rows` kind tr2 S9 leaves at `hand` (tr2:80-84), with no door
  planned. Do not invent a door or an ask.
- **Row 3 is not a row to fold.** It is UNKNOWN UNTIL BUILT: tr2's build run decides how the
  factory's stand-in verb behaves for the `change` row. Edit nothing for it.

Each revision:

- bumps the **Status:** line to `rev-3` and its date to `2026-11-03`, leaving every other field;
- adds one §9 line in the existing form: `- rev-3 · 2026-11-03 · §2 S10 · <what moved>, by the brief
  prompts/2026-11-03-prompt-TOOL-dMindYourWords-1-parents-reground.md`;
- re-opens no fork and resolves none.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-3`, and §9 holds the new line.
- `grep -n "until TOOL-dTotalRecall-2 registers" <spec>` prints nothing.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your spec staged into it through `GIT_INDEX_FILE`, names nothing of your spec. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### Gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### Non-goals

- No file outside TOOL-dMindYourWords-11's spec. No commit, no stage into the real index, no deviation
  record: the main loop writes those.
- No file of dTotalRecall or dWellOiledMachine. A parent spec that looks wrong is a line in your
  return, not an edit.
- No change to what the unit builds.

### Reuse

The parents' specs as the interface; the cross-check record as the map of what moved.
`memory/builds/dWellOiledMachine/prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md`
as the precedent for a re-ground revision.
