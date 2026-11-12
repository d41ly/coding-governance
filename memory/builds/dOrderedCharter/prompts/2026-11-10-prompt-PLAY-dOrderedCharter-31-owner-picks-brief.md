**Serves:** research PLAY-dOrderedCharter-31

# Brief: spec 31 rev-13 — the owner's picks for F8 to F11, and a pre-check against HEAD

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. The picks are recorded in `memory/builds/dOrderedCharter/build/2026-11-10-build-PLAY-dOrderedCharter-1-owner-fork-picks.md`.

## The brief

### Goal

Revise spec 31 so a builder can build it as written over HEAD, with F8 to F11 resolved as the owner picked.

### Items

1. **Resolve the forks.** Mark F8, F9, F10 and F11 `RESOLVED (owner, 2026-11-10)` in the template's shape, each for the option its own
   text recommends: F8 `surfaces = []`; F9 option (b), one predicate in govkit's update; F10 option (b), the selection resolver reads a
   retired id through its `[[retired]]` row, so gov's guarded deploy file is not edited; F11 option (a), `playbook-render` joins the
   default selection. Fold each pick into the scope, design and acceptance it changes: F10 and F11 each add a mechanism the spec's
   scope does not yet name, so give each a scope item, its files touched and a criterion that can fail.
2. **Pre-check every claim against HEAD.** Units built since rev-11 include PLAY-dOrderedCharter-33's later commit, 37, 40, 75, 76 and
   77, which changed the overlay, the tag index, the step gate's classes, the docs leg, govkit's registry and the render. For every
   symbol, file, row, signature, key or count the spec names, read the code; probe with `python -I` in a scratch folder of your own
   where a read cannot settle it.
3. **The spec-token check grades a live spec's acceptance bullets word by word**: write no acceptance command whose words include a path
   that is not a tracked file, never name a test suite or the self-test runner as the observation, keep each backticked span on one
   line, and put every leg the files touched trip on the gates section's leg line. Cite code as `path#symbol` or a blob-pinned line,
   never a bare `path:line`.
4. Every section 8 fork carries a resolution mark; every new fact is pinned, keyed or marked DERIVED on its own line, outside backticks.
5. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

In the spec: bump the **Status:** rev by one, dated 2026-11-10, status kept `DEFERRED`, with a revision-log line naming this brief and
the sections, scope ids and acceptance ids it touches. Every function name it mints passes `python tools/lexicon/lexicon.py --suggest
<name> --as py.function`. Edit the spec in the repository directly; no builder is running.

### Acceptance

- Spec 31 builds as written over HEAD with the four picks folded, and passes the pinned-facts check, memory hygiene's spec-shape check
  and the positional check.

### Gates

Run the pinned-facts check, memory hygiene's spec-shape check and the positional check over the spec, and report each.

### Non-goals

- No code. No edit to any other spec or file.
