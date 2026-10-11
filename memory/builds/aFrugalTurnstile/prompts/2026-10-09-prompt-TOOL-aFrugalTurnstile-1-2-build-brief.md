**Serves:** journal TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1

# Build brief — aFrugalTurnstile, every unit

You build ONE unit, the one your dispatch names, from its spec. The spec is the design; the design
record `memory/builds/aFrugalTurnstile/build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md`
explains why, and its §6 revisions outrank its §3 where they differ. The mandate is the owner's
prompt beside this file. Your spec is already committed; do NOT re-author it except as a rev bump.

1. **Stage by name, never `git add -A` or `git add .`.** Other units' work runs in this worktree at
   the same time. Stage exactly the paths you declared with `--dispatch`, your acceptance ledger,
   AND `memory/builds/aFrugalTurnstile/RUN.md` (it carries your `--dispatch` and `--brief` rows,
   which the `brief-recorded` leg reads AT your build commit; the commit-msg check exempts it). If
   you need another path, declare it with `--dispatch` BEFORE the commit, with a 600 s bound.
2. **The acceptance ledger is owed: every unit is Tier-2.** Write
   `memory/builds/aFrugalTurnstile/build/2026-10-09-build-<FAMILY>-aFrugalTurnstile-<n>-1-acceptance-ledger.md`,
   opening `# <unit id> — acceptance ledger`, then `**Serves:** journal <unit id>`, a short
   paragraph saying which direct checks ran and which suite arms the close still owes, then
   `**Evidences:** <unit id>` and one line per criterion your spec numbers, in the form
   ``- AC<n> — `<observation token>` — what was observed``. A criterion you could not observe as
   written is `- AC<n> — amended rev-<n> — <the change>`, which needs a spec rev bump with its §9
   line in the same commit. There is no third form. Grammar: `memory/HYGIENE.md`, "Acceptance
   ledger". Every token must share a backticked token with the criterion it answers.
3. **Observe every new behaviour RED first** against the file as it is at base `bef97330`
   (`git show bef97330:<path>` into your scratch fixture), then GREEN against your edit. Write both
   observations in the ledger paragraph. Arms you ADD to a `*.test.sh` suite are written but not run:
   gate-guard refuses suites on the run branch before VERIFYING, and the main loop runs them then.
4. **No merge bar, no suite, no `*.test.sh` run, no `run-gates.sh` over this repo.** Your fixture is a
   scratch repo under the scratch path in your ground text, or a SHORT root such as
   `%TEMP%/ft<n>` when a path-length limit bites (a clone or push under the long scratch path fails
   with "Filename too long"). Copy the hook and the runner into it; never drive the real repo's hook.
5. **Regenerate the codebase map in your own commit** when the pre-commit hook asks for it, and
   always after adding or renaming a shell function: `python tools/codebase-map/gen_map.py --write`,
   then stage only the generated files it changed, declared with `--dispatch` first. Delete any
   slice or helper script you put under `tools/` before running it: `gen_map` reads untracked files.
6. **Flip your spec to CLOSED** (status token only, same rev) and run
   `python tools/memory-tree/gen_build_index.py --write`; stage only the generated files it changed
   under `memory/LIVE.md`, `memory/ledger/` and `memory/builds/aFrugalTurnstile/`, declared with
   `--dispatch` first. The pre-commit hook reds a stale index.
7. **No kit-version bump, no `memory/DECISIONS.md` edit, no backlog edit.** A discovery goes in your
   `summary`. A spec defect you find goes in as a rev bump with its §9 line, in your commit.
8. **Shell edits:** author `.sh` and hook changes with the Edit tool, never a heredoc or Python
   text-mode I/O: both have corrupted backslashes and bare CR bytes here. Working copies may be
   CRLF, so a multi-line Python `str.replace` can silently match nothing. `python3 - <file>` does
   NOT read stdin on this host (the launcher runs the next argument as a script): write a script
   file and run it.
9. **Node a's traps:** `TMPDIR` is empty, so `$TMPDIR/x` is `/x`. A git spawn costs about 0.75 s and
   the host is loaded by other sessions' bars, so batch git calls and bound every command. A fixture
   push through the real hook costs 70 to 140 s even for a four-leg stub bar: plan for it.
10. **Unit-specific:**
   - **`.githooks/pre-push` units (1, 2, 4, 7)** run strictly in that order and each starts from the
     previous one's commit. `.githooks/pre_push_bar_selftest.py` anchors on `set +f` spelled once.
     Every message keeps the hook's one-line-per-decision shape.
   - **`tools/run-gates/run-gates.sh` units (1, 5, 4, 6):** the held-count summary line (~3693)
     belongs to the concurrent run aBenchedProbe; do not touch it.
   - **Text units (TOOL-10, PLAY-1, DEPL-1):** after a close, the landing push SCOPES over the
     close's own record commit; it is NOT `covered` (design §6). Say nothing the code units do not
     build. `WIRE-INTO-PROJECT.md`'s working copy is CRLF: edit with the Edit tool and check the
     staged bytes with `git diff --cached | cat -A | head`.
11. **Commit ONLY your paths, by pathspec, and retry on a held lock.** Up to four unit passes share
   this worktree concurrently, and a bare `git commit` would sweep a sibling's staged files into
   yours. Commit with `git commit -F <message file> -- <every path you stage>` (git's `--only` form,
   which commits exactly those paths whatever else is staged), the message ending in its `Pass:
   <unit id>` trailer and the `Co-Authored-By:` line. When git reports `index.lock` exists, a
   sibling's commit hook is running: wait 30 s and retry, for up to 20 minutes, and never delete the
   lock.
