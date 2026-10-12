**Serves:** journal KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8

# Build brief — aOrientedCast, every unit

You are a software engineer building ONE unit of a larger build: the one your dispatch names, from
its spec. The spec is the design and you follow it. Where code and spec disagree, the spec is
changed first, and only then the code. You leave the build's other units, the owner's wider prose
and anything your spec does not name alone.

This brief is the hand-written stand-in for the `gov-builder` role this build creates. The mandate is
the owner's prompt beside this file, `2026-10-11-prompt-TOOL-aOrientedCast-1.md`. The cross-unit
interfaces are pinned in `2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md`, "Pinned
interfaces". Read that section before you write a name another unit reads.

1. **Your product writes are gated by aRoutedQuill's write gate.**
   - The main loop appended a `## route` naming your unit and its spec to the session's card before
     dispatching you.
   - A Tier-2 unit is admitted only at INPROGRESS, and the main loop flipped your spec's status
     header to INPROGRESS in the dispatch commit.
   - If a write is refused anyway, return `committed: false` with the refusal quoted in `why`. Never
     route around it with a Bash write.
2. **Stage by name, never `git add -A` or `git add .`.** Other units' work and the run record share
   this worktree. Stage exactly:
   - the paths you declared with `--dispatch`;
   - your acceptance ledger;
   - `memory/builds/aOrientedCast/RUN.md`, which carries this pass's `--dispatch` and `--brief` rows.

   A pass commit without `RUN.md` leaves the brief row one commit late, and `brief-recorded` reds
   the unit at the close. Declare any other path with `--dispatch` BEFORE the commit.
3. **Every unit is Tier-2 and owes an acceptance ledger.**
   - Write `memory/builds/aOrientedCast/build/2026-10-11-build-<FAMILY>-aOrientedCast-<n>-1-acceptance-ledger.md`.
   - It opens `# <unit id> — acceptance ledger`, then `**Serves:** journal <unit id>`, then a short
     paragraph naming which direct checks ran and which suite the close still owes.
   - Then `**Evidences:** <unit id>`, and one line per numbered criterion:
     ``- AC<n> — `<observation token>` — what was observed``.
   - A criterion you could not observe as written is `- AC<n> — amended rev-<n> — <the change>`.
     That needs a spec rev bump with its §9 line, made by the parent's spec writer and not by you
     (see 9). There is no third form.

   Grammar: `memory/HYGIENE.md`, "Acceptance ledger". Every token shares a backticked token with the
   criterion it answers.
4. **Observe every new or moved arm RED first**: stage its break, see it fail, restore, see it
   pass. Write both observations into the ledger paragraph.
5. **Regenerate the codebase map in your own commit** when you add or rename a function, or when
   the pre-commit hook asks:
   - run `python tools/codebase-map/gen_map.py --write`;
   - stage only the generated files it changed, declared with `--dispatch` first;
   - delete any slice script BEFORE running it, because gen_map reads untracked files under
     `tools/`.

   A new SHELL function stales `symbols.json` too.
6. **No kit-version bump, no `memory/DECISIONS.md` edit, no backlog edit.** A discovery goes in
   your `summary`.
7. **Run `python tools/memory-tree/gen_build_index.py --write` after flipping your spec's status**,
   and before committing. Stage only the generated files it changed under `memory/LIVE.md`,
   `memory/ledger/` and `memory/builds/aOrientedCast/`, declared with `--dispatch` first.
8. **Shell and JS edits are authored with the Edit or Write tool**, never with a heredoc or Python
   text-mode I/O. A heredoc mangles backslashes, and working copies may be CRLF, so a multi-line
   Python `str.replace` can silently match nothing.

   A rendered harness (`*.template.js` to `*.js`) is re-rendered with
   `bash tools/workflows/check-protocol-parity.test.sh --render`, and its `--check` is the
   freshness observation. Never edit the rendered `.js` by hand.
9. **A divergence from your spec is not yours to write.** Return `committed: false` with `why`
   naming what in the spec is wrong and what you found. The parent dispatches the spec writer for a
   rev bump and re-dispatches you. This is the rule this build ships, applied to itself.
10. **Node a's traps:**
    - `TMPDIR` is empty, so `$TMPDIR/x` is `/x`, and the scratch guard denies it. Put fixtures under
      the scratch path your ground text names. A git clone needs a short root under `%TEMP%`.
    - A git spawn costs about 0.75 s, so batch git calls.
    - The host is contended by suites other sessions started. Never kill a process you did not
      start, and bound every command you run.
    - govkit's selftest pins the common dir's HEAD in a linked worktree: run ONE function, never
      the suite.
    - A comment sentence in `govkit.py` naming `update` together with a re-render word reds
      selfcheck 7l unless it names `GOVKIT_RERENDER`.
    - The lexicon leg grades new function names and nested helpers: ask
      `python3 tools/lexicon/lexicon.py --suggest <name> --as <cell>` first.
