**Serves:** research TOOL-dTrackedAtlas-3

# Build brief — TOOL-dTrackedAtlas-3: the page knows what it was generated from, and `--check` reds a stale one

Build `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-3.md` (rev-3, READY) as written: the
generator and template edits and the acceptance ledger its Files touched names. The spec is the design; diverge
only by returning `diverged: true` with the section and the reason. Units 1 and 2 are CLOSED: use unit 1 only through its module's
interface (its `derive` and the constants it exports, such as `GIT_TIMEOUT`), never by re-deriving a build's state.
The spec is rev-3: its new function names were renamed to declared verbs after the first dispatch diverged.

- Unit 1's pass legs redded on three things this pass must not repeat: every figure typed before a unit word in
  the ledger carries a pin on its line (a sha, a `path:line`, PINNED or DERIVED) or sits in a code span; every
  new function name leads with a verb `.lexicon.conf` declares (`python tools/lexicon/lexicon.py --suggest <name>
  --as py.function`); every symbol citation is `<repository path>#<symbol>`, never a bare basename.
- Unit 4 reaches the page check through the CLI this spec states in its section 4; build it exactly as stated, its exit codes included.
- Each AC's red case is observed on the real shape it names, never a synthetic stand-in, and recorded in the
  ledger beside its green. The page goes to a scratch path, never into the repository.
- Run no gate, suite or bar. Fixture clones go under `%TEMP%/<short>` and are removed after.
- No path under `tools/`; no new file under `memory/builds/dClosedLoop/build/`.
- Commit once, with a `Pass: TOOL-dTrackedAtlas-3` trailer and `Co-Authored-By: Claude Opus 5.5
  <noreply@anthropic.com>`. The pre-commit hook takes minutes: bound the commit at ten minutes. Never `--no-verify`,
  never `git add -A`. Leave the spec's status flip to the main loop.
