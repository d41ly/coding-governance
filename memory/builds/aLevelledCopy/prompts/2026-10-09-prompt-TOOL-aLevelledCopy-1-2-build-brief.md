**Serves:** journal TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 DEPL-aLevelledCopy-1

# Build brief — aLevelledCopy, every unit

You build ONE unit, the one your dispatch names, from its spec. The spec is the design. This brief
adds what the harness prompt does not carry. The mandate is the owner's prompt beside this file,
`2026-10-09-prompt-TOOL-aLevelledCopy-1.md`.

1. **Stage by name, never `git add -A` or `git add .`.** Other units' work and the run record share
   this worktree. Stage exactly the paths you declared with `--dispatch`, plus your ledger record.
   If you need another path, declare it with `--dispatch` BEFORE the commit.
2. **The acceptance ledger is owed: every unit is Tier-2.** Write
   `memory/builds/aLevelledCopy/build/2026-10-09-build-<FAMILY>-aLevelledCopy-<n>-1-acceptance-ledger.md`,
   opening `# <unit id> — acceptance ledger`, then `**Serves:** journal <unit id>`, a short
   paragraph saying which direct checks ran and which suite the close still owes, then
   `**Evidences:** <unit id>` and one line per criterion your spec numbers, in the form
   ``- AC<n> — `<observation token>` — what was observed``. A criterion you could not observe as
   written is `- AC<n> — amended rev-<n> — <the change>`, which needs a spec rev bump with its §9
   line in the same commit. There is no third form. Grammar: `memory/HYGIENE.md`, "Acceptance
   ledger". Every token must share a backticked token with the criterion it answers.
3. **Observe every new arm RED first**: stage its break, see it fail, restore, see it pass. Write
   both observations in the ledger paragraph.
4. **Regenerate the codebase map in your own commit** when the pre-commit hook asks for it:
   `python tools/codebase-map/gen_map.py --write`, then stage only the generated files it changed,
   declared with `--dispatch` first. The hook's map leg refuses a stale `symbols.json` whenever code
   is staged, so deferring it to the main loop is not possible. (Corrected after
   DEPL-aLevelledCopy-1's pass found this; the first version of this item said the opposite.)
5. **No kit-version bump, no `memory/DECISIONS.md` edit, no backlog edit.** A discovery goes in your
   `summary`.
6. **Run `python tools/memory-tree/gen_build_index.py --write` after flipping your spec to CLOSED**
   and before committing. Stage only the generated files it changed under `memory/LIVE.md`,
   `memory/ledger/` and `memory/builds/aLevelledCopy/`, and declare them with `--dispatch`
   first. The pre-commit hook reds a stale index.
7. **Shell edits:** author `.sh` changes with the Edit tool, never with a heredoc or Python
   text-mode I/O. Both have corrupted backslashes and bare CR bytes in this repo. Working copies here
   may be CRLF, so a multi-line Python `str.replace` can silently match nothing.
8. **Node a's traps:** `TMPDIR` is empty, so `$TMPDIR/x` is `/x`, and the scratch guard denies it.
   Put fixtures under the scratch path your ground text names, or a short `%TEMP%\<name>` directory
   when a path-length limit bites. A git spawn costs ~0.75 s, so batch git calls in any loop.
9. **Unit-specific:**
   - **TOOL-aLevelledCopy-3, AC6** runs on WSL's own filesystem:
     `wsl.exe -e sh -c '<commands>'`, fixture under a `mktemp -d` there, the checker reached
     through `/mnt/c/projects/coding-governance/.claude/worktrees/friendly-napier-49e2c6/tools/check-wiring.sh`.
     `/mnt/c` reports every file 0777, so the fixture must not live there.
   - **DEPL-aLevelledCopy-1:** the govkit self-test pins the common dir's HEAD, so in a linked
     worktree the whole suite grades the primary's revision. Run only your one function, as your
     spec's §6 shows, under the default `%TEMP%`. A comment sentence in `govkit.py` naming `update`
     plus a re-render without `GOVKIT_RERENDER` reds selfcheck 7l; read `tools/govkit/README.md`
     before editing comments there.
   - **TOOL-aLevelledCopy-2 and -3** both edit `tools/check-wiring.sh` and its header. They run in
     that order, so -3 appends to the lists -2 leaves.
