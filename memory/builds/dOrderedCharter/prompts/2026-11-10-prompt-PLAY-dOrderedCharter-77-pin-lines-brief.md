**Serves:** research PLAY-dOrderedCharter-77

# Brief: spec 77 — pin its file:line citations with the positional tool

## The prompt

> I see that a lot of units are being refused this build and that's wasting tokens

— owner, 2026-11-10. After unit 77's pass at `26eda4214`, the main loop's run of `python tools/playbook/positional.py check`
reds eighteen unlisted file:line citations, all in spec 77's own text, carried from the close bar's attribution.

## The brief

### Goal

Rewrite spec 77's unlisted file:line citations into blob-pinned lines with the tool built for it, so the positional check names
nothing in spec 77, changing no design text.

### Items

1. Run `python tools/playbook/positional.py pin memory/builds/dOrderedCharter/spec/2026-11-10-spec-PLAY-dOrderedCharter-77.md --at
   51cd8b402`, the spec's base, so every citation pins the line it meant when written. Read its diff and confirm each rewritten
   citation still names the same line text it named at that commit.
2. Add one revision-log line naming this brief, the sections whose citations moved and the tool, and saying no design text moved.
   The spec is CLOSED: keep its status `CLOSED` and its rev, and add the log line only, as a citation-form change is not a revision of
   its design.
3. Run `python tools/playbook/positional.py check` and the pinned-facts check, and report each.

### Acceptance

- The positional check and the pinned-facts check name nothing in spec 77, and its design text is unchanged.

### Gates

The two checks above.

### Non-goals

- No code. No edit to any other file.
