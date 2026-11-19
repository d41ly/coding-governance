**Serves:** research TOOL-dTrackedAtlas-10

# Build brief — TOOL-dTrackedAtlas-10: a promoted finding of the closing review

Build `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-10.md` (rev-1, READY) as written, with
the acceptance ledger its Files touched names. Its design input is its item in
`memory/builds/dTrackedAtlas/reviews/2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md`. The spec
is the design; diverge only by returning `diverged: true` with the section and the reason.

- Earlier passes of this build redded on three things this pass must not repeat. Every figure typed before a
  unit word in the ledger carries a pin on its line (a sha, a `path:line`, PINNED or DERIVED) or sits in a code
  span that opens and closes on that line. Every new function name, nested ones included, leads with a verb
  `.lexicon.conf` declares, graded by `python tools/lexicon/lexicon.py --suggest <name> --as py.function`. Every
  citation is `<repository path>#<symbol>` or a blob-pinned `<path>@<sha>:<line>`, never a bare basename.
- Each AC's red case is observed on the real shape it names, never a synthetic stand-in, and recorded in the
  ledger beside its green. Fixture clones go under `%TEMP%/<short>` and are removed after; the real
  repository's refs are never written.
- Run no gate, suite or bar. No path under `tools/`; no new file under `memory/builds/dClosedLoop/build/`.
- Commit once, with a `Pass: TOOL-dTrackedAtlas-10` trailer and the co-author trailer the charter names. The
  pre-commit hook takes minutes: give the commit ten minutes. Never `--no-verify`, never `git add -A`. Leave
  the spec's status flip to the main loop.
