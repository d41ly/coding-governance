**Serves:** journal TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2

# Build brief — aBenchedProbe, every unit

You build ONE unit, the one your dispatch names, from its spec. The spec is the design. This brief
adds what the harness prompt does not carry. The mandate is the owner's prompt beside this file,
`2026-10-09-prompt-TOOL-aBenchedProbe-1.md`.

1. **Stage by name, never `git add -A` or `git add .`.** Other units' work and the run record share
   this worktree. Stage exactly the paths you declared with `--dispatch`, plus your ledger record,
   AND `memory/builds/aBenchedProbe/RUN.md`, which carries this pass's `--dispatch` and `--brief`
   rows: a pass commit without it leaves the brief row one commit late and `brief-recorded` reds the
   unit at the close. If you need another path, declare it with `--dispatch` BEFORE the commit.
2. **A Tier-2 unit owes an acceptance ledger** (TOOL-aBenchedProbe-1 and DEPL-aBenchedProbe-2). Write
   `memory/builds/aBenchedProbe/build/2026-10-09-build-<FAMILY>-aBenchedProbe-<n>-1-acceptance-ledger.md`,
   opening `# <unit id> — acceptance ledger`, then `**Serves:** journal <unit id>`, a short paragraph
   saying which direct checks ran and which suite the close still owes, then `**Evidences:** <unit id>`
   and one line per criterion your spec numbers, in the form
   ``- AC<n> — `<observation token>` — what was observed``. A criterion you could not observe as
   written is `- AC<n> — amended rev-<n> — <the change>`, which needs a spec rev bump with its §9 line
   in the same commit. There is no third form. Grammar: `memory/HYGIENE.md`, "Acceptance ledger".
   Every token must share a backticked token with the criterion it answers. Tier-1 units owe no ledger.
3. **Observe every new or moved arm RED first**: stage its break, see it fail, restore, see it pass.
   Write both observations in the ledger paragraph (Tier-2) or the commit body (Tier-1).
4. **Regenerate the codebase map in your own commit** when you add or rename a function, or the
   pre-commit hook asks: `python tools/codebase-map/gen_map.py --write`, then stage only the generated
   files it changed, declared with `--dispatch` first. Delete any slice script BEFORE running it:
   gen_map reads untracked files under `tools/`.
5. **No kit-version bump, no `memory/DECISIONS.md` edit, no backlog edit.** A discovery goes in your
   `summary`.
6. **Run `python tools/memory-tree/gen_build_index.py --write` after flipping your spec to CLOSED**
   and before committing. Stage only the generated files it changed under `memory/LIVE.md`,
   `memory/ledger/` and `memory/builds/aBenchedProbe/`, declared with `--dispatch` first.
7. **Shell edits** (`tools/run-gates/run-gates.sh`, `tools/run-gates/run-gates.test.sh`): author them
   with the Edit tool, never with a heredoc or Python text-mode I/O. Working copies may be CRLF, so a
   multi-line Python `str.replace` can silently match nothing. In `run-gates.sh` touch ONLY the one
   summary line: the concurrent run aFrugalTurnstile edits other regions of that file.
8. **Node a's traps:** `TMPDIR` is empty, so `$TMPDIR/x` is `/x`, and the scratch guard denies it.
   Put fixtures under the scratch path your ground text names. A git spawn costs ~0.75 s, so batch git
   calls. The host is contended by suites other sessions started under `%TEMP%`: never kill a process
   you did not start, and bound every command you run.
9. **Unit-specific:**
   - **TOOL-aBenchedProbe-1** regenerates `tools/govkit/subject-pins.tsv` with
     `python tools/govkit/govkit.py selfcheck --write`; stage that file, nothing else it may touch.
   - **TOOL-aBenchedProbe-2** observes the run-gates canary's summary assertion through a slice: the
     prologue plus the one block, in a temp script INSIDE `tools/run-gates/`, run, then DELETED before
     staging anything. Never the whole `run-gates.test.sh`.
   - **DEPL-aBenchedProbe-1 and -2** edit `tools/govkit/govkit.py`. A comment sentence there naming
     `update` together with a re-render word reds selfcheck 7l unless it names `GOVKIT_RERENDER`;
     read `tools/govkit/README.md` (or the 7l header) before writing comments. The lexicon leg grades
     new function names: ask `python3 tools/lexicon/lexicon.py --suggest <name> --as <cell>` before
     naming one. govkit's selftest pins the common dir's HEAD in a linked worktree: run ONE function,
     as the spec's §6 says, never the suite.
