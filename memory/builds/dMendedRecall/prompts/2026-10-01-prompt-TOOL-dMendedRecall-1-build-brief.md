**Serves:** journal TOOL-dMendedRecall-1..3

# Build brief — dMendedRecall, one unit per dispatch

You build exactly the unit you were dispatched for. Its SPEC is the design; this brief carries only
what a spec does not: the build's own rules and the record shapes the gates grade. Where the spec
and this brief disagree about the DESIGN, the spec wins and you change the spec first (rev-N bump
with its section 9 line). Where they disagree about a RECORD SHAPE below, this brief wins.

## The build's rules

- **The unattended kit's own self-test suites are WAIVED for this landing** (owner, 2026-10-01, the
  build README's build-level rule). Never run `tools/unattended/*.test.sh`,
  `run-unattended-gates.sh` or `run-selftests.sh`, in any form. A new `fail` branch in the driver
  still gets its arm line written in `tools/unattended/unattended.test.sh` for the arms meta-gate;
  that arm's RUN is not observed, and your ledger says so.
- **Kit versions are not yours.** Do not bump `KIT_UNATTENDED_VERSION`, the memory-tree version or
  any `gov:kit` marker; the orchestrator makes one version sweep at VERIFYING.
- **`tools/unattended/check-unattended.sh` carries raw CR bytes on purpose.** Edit it through a
  binary-safe read and write (Python `open(p, 'rb')` / `'wb'`, or `newline=""` both ways), never a
  text-mode rewrite, and count the CR bytes before and after: the count must not change.
- **Write every temporary script to a file under the scratch root**, never through a shell heredoc:
  a heredoc halves backslashes before Python sees them.
- **A template edit re-renders its copy in the same commit.** The kit gate
  `bash tools/unattended/check-unattended.sh` and `bash tools/memory-tree/check-memory-hygiene.sh`
  are direct checks you MAY run; they are not suites.
- **A new check is not done until its failing case was observed.** Stage the break, run the checker,
  see it RED, unstage the break. Stage your real changes BEFORE a negative arm that ends in
  `git checkout --`, or the restore eats your edits.
- **Stage explicit paths.** Never `git add -A`.
- **Declare EVERY path your commit writes with `--dispatch`**, generated ones included: the build
  README, the spec's records region, `memory/LIVE.md`, `memory/ledger/<month>.md`,
  `memory/backlog/<FAMILY>.md`, every render. Re-declare WIDER before the commit when the render
  touches one you missed. `--dispatch` refuses `RUN.md`, and the kit gate's check 23 excludes it. The
  corpus sat one write under `UNDECLARED_WRITE_CEILING` during the previous build, so a single undeclared path in
  your commit reds the bar at the close.

## What your ONE build commit carries

1. The code and doc changes your spec names, with their renders.
2. Your spec's status header flipped to `CLOSED` (the harness requires this).
3. Your ACCEPTANCE LEDGER, a new file
   `memory/builds/dMendedRecall/build/2026-10-01-build-<your unit id>-1-acceptance-ledger.md`:

   ```
   # <unit id> — acceptance ledger

   **Serves:** journal <unit id>

   <two or three sentences: what was built, and which checks ran instead of which gates>

   **Evidences:** <unit id>
   - AC1 — `<a token from the observation, in backticks, BEFORE the first line wrap>` — <what was run and what it printed>
   - AC2 — amended rev-<n> — <why this criterion could not be observed here>
   ```

   Every §6 criterion gets exactly one line. An OBSERVED line carries its backticked token on the
   FIRST line of the bullet. A criterion only the waived suites could observe is AMENDED: write the
   `amended rev-<n>` form AND bump your spec's rev with a section 9 line citing the build README's
   waiver rule.
4. `memory/builds/dMendedRecall/RUN.md`, because `--brief` only STAGES its row and the row must ride
   this commit.
5. Any generated artifact your change makes stale: run
   `python tools/memory-tree/gen_build_index.py --write` after your spec flip and commit every file
   it rewrites.

Commit subject: `build(dMendedRecall): <unit id> — <what it does>`, and end the message with
`Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Pass `timeout: 600000` to the commit: the
pre-commit hook can outlast the default.
