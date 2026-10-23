**Serves:** research TOOL-dSafePassage-51

# Brief — dSafePassage: TOOL-dSafePassage-51's title is longer than the index line cap

## The prompt

> HYGIENE check 7 FAILED — index entry lines over their declared cap: memory/builds/dSafePassage/README.md (356
> chars > 350)

— the memory hygiene gate, run `--staged` by the main loop over the round-6 disposal's output

## The brief

### Goal

Shorten TOOL-dSafePassage-51's H1 title, so the build-units row the index generator renders from it fits check 7's
350-character cap. Change nothing else.

### Items

1. The H1 of `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md` renders into the README's
   generated `gen:build-units` region as a row of 356 characters, 6 over the cap. Rewrite the title after the em
   dash so the row is at most 330 characters, a margin for later column growth. It must still name what the unit
   does. Keep the exact `# TOOL-dSafePassage-51 — ` prefix, with an EM DASH.
2. If the spec repeats the old title anywhere, such as §1, leave that prose alone. Only the H1 is the index's input.

### Acceptance

`python tools/memory-tree/gen_build_index.py --print-bindings` is not needed. Instead, the H1's length is at most
195 characters, since the row adds about 135 characters around the title (the 356-character row carries a
221-character H1 title portion). Measure with `head -1 <spec> | wc -m`.

### Gates

None. A role agent runs no gate here; the main loop re-renders and runs the hook.

### Non-goals

No rev bump, because the spec is rev-1, uncommitted and unaudited until round 7. No other change, no commit, no
stage, and no write outside that one file.

### Limitations

This is an unattended run, so nobody will answer a question.

### Reuse

None needed.
