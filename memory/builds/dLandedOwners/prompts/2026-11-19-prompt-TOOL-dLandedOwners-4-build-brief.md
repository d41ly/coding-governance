**Serves:** research TOOL-dLandedOwners-4

# Build brief — TOOL-dLandedOwners-4: the closing review's promoted findings

Build `memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-4.md` (rev-1, READY) as written, with the
acceptance ledger its Files touched names. Its design input is the closing review record
`memory/builds/dLandedOwners/reviews/2026-11-19-review-TOOL-dLandedOwners-1-3-closing-diff-round1.md`, items M1 to M5 and L1 to L4, over units 1 to 3 as built. The spec
is the design; diverge only by returning `diverged: true` with the section and the reason.

- This is a shipped kit edit under `tools/policy/` and `tools/govkit/`. Every figure typed before a unit word in the ledger carries a pin
  on its line (a sha, a `path:line`, PINNED or DERIVED); a pin inside a code span does not count. Every new function
  name, nested ones included, leads with a verb `.lexicon.conf` declares, graded by
  `python tools/lexicon/lexicon.py --suggest <name> --as py.function`. Every citation is `<repository path>#<symbol>`
  or a blob-pinned `<path>@<sha>:<line>`, never a bare basename or a positional section number.
- Each AC's red case is observed on the real shape it names, never a synthetic stand-in, and recorded in the ledger
  beside its green. Fixture clones go under `%TEMP%/<short>` and are removed after; the real repository's refs are
  never written.
- Run no gate, suite or bar; the direct checks each AC names are allowed.
- Commit once, with a `Pass: TOOL-dLandedOwners-4` trailer and the co-author trailer the charter names. The
  pre-commit hook takes minutes: give the commit ten minutes. Never `--no-verify`, never `git add -A`. The spec's
  status at the commit is what the dispatch states.
