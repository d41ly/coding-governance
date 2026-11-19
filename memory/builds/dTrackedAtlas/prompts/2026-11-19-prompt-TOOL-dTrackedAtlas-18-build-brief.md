**Serves:** research TOOL-dTrackedAtlas-18

# Build brief — TOOL-dTrackedAtlas-18: the schedule instrument re-pinned, packets and door

Build `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-18.md` (rev-1, READY) as written, with
the acceptance ledger its Files touched names. Its design input is the owner's word of 2026-11-19 and ask
`TOOL-dTrackedAtlas-6` in `memory/builds/dTrackedAtlas/BACKLOG.md`. The spec
is the design; diverge only by returning `diverged: true` with the section and the reason.

- Earlier passes of this build redded on three things this pass must not repeat. Every figure typed before a
  unit word in the ledger carries a pin on its line (a sha, a `path:line`, PINNED or DERIVED) or sits in a code
  span that opens and closes on that line. Every new function name, nested ones included, leads with a verb
  `.lexicon.conf` declares, graded by `python tools/lexicon/lexicon.py --suggest <name> --as py.function`. Every
  citation is `<repository path>#<symbol>` or a blob-pinned `<path>@<sha>:<line>`, never a bare basename.
- Each AC's red case is observed on the real shape it names, never a synthetic stand-in, and recorded in the
  ledger beside its green. Fixture clones go under `%TEMP%/<short>` and are removed after; the real
  repository's refs are never written.
- Run no gate, suite or bar; the `chain-packet self-test` suite is held and is not yours to run. Under `tools/`, only
  `tools/chain-packet.py`; no new file under `memory/builds/dClosedLoop/build/`. The packets change only through
  `packet.py --repin`, never by hand.
- Commit once, with a `Pass: TOOL-dTrackedAtlas-18` trailer and the co-author trailer the charter names. The
  pre-commit hook takes minutes: give the commit ten minutes. Never `--no-verify`, never `git add -A`. Leave
  the spec's status flip to the main loop.
