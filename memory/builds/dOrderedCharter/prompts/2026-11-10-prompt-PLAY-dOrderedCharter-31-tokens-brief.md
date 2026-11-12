**Serves:** research PLAY-dOrderedCharter-31

# Brief: spec 31 rev-13 — three acceptance tokens the spec-token check refuses

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. The main loop's pre-dispatch run of `python tools/check-spec-tokens.py` with spec 31 live reds three acceptance
tokens, caught before any builder runs.

## The brief

### Goal

Make spec 31 pass the spec-token check as a live spec, keeping its design.

### Items

1. Two acceptance tokens hold an inline `python -c` whose words include `tomllib.load(open('tools/govkit/entries/playbook.kit.toml',`
   and `tomllib.load(open('tools/govkit/entries/check-microformats.kit.toml',`: a word holding a `/` and a dotted last segment must be
   a tracked path, so the check reds each. Restate each observation with no such word, for example a `git grep` over the entry file.
2. One acceptance token is `tools/govkit/govkit.py#derive_unsatisfied_requires`: acceptance bullets spell plain tracked paths, never a
   `path#symbol`. Name the plain path in the bullet and leave the symbol to the design text, or observe the behaviour by a command.
3. Keep every other acceptance bullet as it is; check the spec for any other bullet with the same two shapes and fix it the same way.
4. Edit the spec in the repository directly; no builder is running. Keep its status `DEFERRED` and its rev-13, and add this brief's
   change to the rev-13 revision-log line, naming the acceptance ids it touches; rev-13 is committed, so if the template's rule for a
   committed revision requires it, make it rev-14 instead.

### Acceptance

- `python tools/check-spec-tokens.py` reports no hit on spec 31 with its status read live; the pinned-facts, spec-shape and positional
  checks stay clean.

### Gates

Run the pinned-facts check, memory hygiene's spec-shape check and the positional check over the spec; the main loop runs the
spec-token check.

### Non-goals

- No code. No edit to any other spec or file. No design change.
