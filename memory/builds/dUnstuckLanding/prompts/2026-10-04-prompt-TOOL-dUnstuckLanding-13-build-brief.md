# TOOL-dUnstuckLanding-13 to -20 — build brief (the kit fix)

**Serves:** journal TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20

node d · 2026-10-04 · one brief for the eight unit builders. Each is dispatched alone, in order 13 to
20, after the previous unit committed. Your spec is the design. This brief is what the spec assumes
you know.

## Read first

- Your spec, whole. Then every spec it names as `consumes-from`: that unit is already built and
  committed, so read its code as committed, not as its spec describes it.
- The design record's section for your unit:
  `memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-2-design.md`.
- `tools/unattended/README.md`, and the header comment of every function you change.

## Rules the close will enforce on what you write

- **No suite, no bar.** You WRITE the new arms your spec names in their `*.test.sh` files, and you do
  not RUN those files. The kit self-tests run once, at the close, by owner ruling
  `TOOL-dUnstuckLanding-24`.
- **Verify directly.** Use a hermetic probe built from the suite's own setup: copy the fixture
  helper into the session scratchpad and drive the verb on a throwaway repository under
  `%TEMP%/<short-name>`. Or run a checker over a staged break. Name, in your `summary`, every
  criterion you could not observe this way.
- **Arm every numbered branch.** Every new `fail N` gets an arm in its sibling `*.test.sh` that asserts
  a literal slice of its own message. `fail N` numbers and run-state fact numbers are the NEXT FREE
  ones at the moment you build; grep the driver for the current maximum first.
- **New conf keys** join the allow-list in `tools/unattended/check-unattended.sh`, the kit example
  conf, and PROTOCOL §8's key table, all in the same commit. Check 22 joins the three.
- **Templates and their renders move together.** After editing any
  `tools/unattended/*.template.md`, run `bash tools/unattended/adopt-unattended.sh` and commit the
  re-copied renders under `memory/guides/` and `.claude/skills/unattended/`. A render that differs
  from its template reds the kit gate.
- **Gov's own `.unattended.conf`.** Where your spec adds a key gov must declare, declare it there too.
  An example: `HOLD_FLOOR=7` for unit 13.
- **No literals outside the kit.** A kit file names nothing outside itself by literal; derive paths.
  Read the ban in `tools/hooks/README.md` before you add a path.
- **Leave the version alone.** Do not bump `KIT_UNATTENDED_VERSION`; the orchestrator does that once.
- **LF only** in `.sh` and template files.

## Records your commit carries

- **The code, the arms, and the re-copied renders.**
- **Your spec's status header, set to `CLOSED`**, or `WONTDO` with a reason. Where you had to
  diverge, bump the spec first (rev-N plus a §9 line).
- **An acceptance ledger**, at
  `memory/builds/dUnstuckLanding/build/2026-10-04-build-<unit id>-1-acceptance-ledger.md`. It opens
  with `**Serves:** journal <unit id>`, then one `**Evidences:** <unit id>` block, then one line per
  AC: `- AC<n> — \`<token shared with the AC>\` — what you observed`, or `- AC<n> — amended rev-<n> —
  what changed`. There is no third form. The token has to appear in the AC itself, on one line, never
  wrapped across two.
- **The generated files.** Run `python tools/memory-tree/gen_build_index.py --write` and
  `python tools/memory-tree/gotchas.py --write` where a gotcha moved, and stage EVERY file they
  rewrite.
- **The pre-commit.** Before you commit, stage everything and run
  `bash tools/memory-tree/check-memory-hygiene.sh` and `python tools/check-spec-tokens.py`. The
  pre-commit hook can take minutes, so give the commit call a 600000 ms timeout.

## Traps measured on this node

- Python fed on stdin through a heredoc loses one level of backslash escapes. Write the script to a
  file in the scratchpad and run it from there.
- `$TMPDIR` is unset in the Bash tool. Spell the scratchpad path out literally.
- A text-mode read in Python rewrites a lone CR. Open with `newline=""`, both reading and writing.
- A gate sees tracked files only. Stage a new file before you run any check over it.
