# KICK-dKeptSession-12 — acceptance ledger

**Serves:** journal KICK-dKeptSession-12

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria AC1 to AC7 were observed on win32 at the pass's base
`6b476eb5`. AC1 to AC6 ran through the unit's own fixture CLI, `bash card-store.fixture.sh --plant
<case>`, one plant at a time, each over its own scratch remote and repository under a short temp
directory; the suite that loops over `--list` was not run. The re-pointed and untouched plants of the
replay block, `context-idle`, `context-always-fresh`, `context-transcript-absent`, `partial-restart`
and `terminal-route`, printed `held` for every row the same way. The four new functions and the
fixture's helper `set_card_verdict` were each graded OK by `python tools/lexicon/lexicon.py
--suggest <name> --as sh.function`, and `python tools/lexicon/lexicon.py` exited 0 over the change.

Owed to the close: every leg the spec's section 7 names, the manifest-check suite whole, and the `New
arm:` line's RED-first observation, the plants staged red against the engine at `6b476eb5`, where no
reader is defined and no `· in` text is printed.

**Evidences:** KICK-dKeptSession-12
- AC1 — `context-fixture-red` planted `CLAUDE.md` with the card import line, `resume.context`
  `always-resume`, a transcript dated 1800 seconds back (PINNED by the plant) and a recorded verdict
  `red A` for the installed fixture's blob under `cli 9.9.2`. Its one replay, through the engine's
  own reader, printed a `resume — fresh recommended: idle` line carrying `always-resume read as
  fresh-when-idle · card-import fixture red: red A`; the plant printed `held` and exited 0 (DERIVED,
  that run).
- AC2 — `context-always-resume` recorded `pass` for the installed fixture's blob, `b79ea803`
  (DERIVED, `git hash-object` that run), under `cli 9.9.2` with `AI_AGENT=claude-code_9-9-2_agent`
  exported; the replay printed `resume — resume recommended (resume.context: always-resume)` whole,
  with no override, and the plant exited 0 (DERIVED, that run). `context-idle` under
  `fresh-when-idle` still recommended fresh, held.
- AC3 — `fixture-stale` recorded a pass for blob `00000000` (PINNED by the plant): the line named
  `recorded for fixture 00000000, now b79ea803`; then a pass for the installed blob under `cli 1.0.0`
  (PINNED by the plant): the line named `recorded under cli 1.0.0, now 9.9.2`. Both rows held and
  the plant exited 0 (DERIVED, that run).
- AC4 — `fixture-run` ran `--card --fixture-run <dir>` over three `CARD_FIXTURE` stubs: exit 0
  recorded `pass`, exit 1, whose last line names `FAILED limb B`, recorded `red B`, exit 2 recorded
  `absent`; each time the verb exited 0 (DERIVED, that run) and printed the line the file holds. A
  file listing of the scratch tree before and after, less the stub dirs and the plant's output,
  differed in the verdict file alone. With `CARD_FIXTURE` naming no file the verb exited 2 (DERIVED,
  that run) and no verdict file was left. Probed by hand at the worktree: `--fixture-run` with no
  directory, and with `--build`, each refused with exit 2 (DERIVED, that probe).
- AC5 — `worktree-named` published the build card from a linked worktree and replayed in the
  primary: the fresh line carried `· in` and the worktree's toplevel as git prints it, not the
  primary's. With that worktree removed, the next replay carried `· in a new worktree of tFix`. Both
  rows held (DERIVED, that run).
- AC6 — `replay-order` placed the stored card's `READY — tFix` line, `card —`, `route —`, `resume —`,
  `partial —` and `now —` on lines 33 to 38 in that order (DERIVED, that run), held.
- AC7 — `grep -n "card-fixture.verdict" help/orientation-card.md` matched the new paragraph of "When a
  session resumes" (DERIVED, that run), which names `--fixture-run`; the section's example `resume —`
  line carries the `· in` text.
- `read_session_cli_version`, probed alone: `AI_AGENT=claude-code_9-9-2_agent` printed `9.9.2`, a
  value with no `claude-code_` prefix returned 1 with nothing printed, and `derive_cli_line` still
  printed its `cli —` cell from it. `grep -c 'claude-code_\*' manifest-check.sh` printed 1 (DERIVED,
  that probe).
