# KICK-dKeptSession-38 — acceptance ledger

**Serves:** journal KICK-dKeptSession-38

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria AC1 to AC6 were observed on win32 at the pass's base
`cf66fda7`. AC1 to AC3 and AC5 ran through the unit's own fixture CLI, `bash card-store.fixture.sh
--plant <case>`, one plant at a time, each over its own scratch remote and repository under a short
drive-letter temp directory, the spelling the suite hands the plants; the suite that loops over
`--list` was not run. The neighbouring plants `context-fixture-red`, `fixture-run` and
`fixture-run-cli` printed `held` for every row the same way. No function was added or renamed, so the
lexicon grades nothing new: the diff adds no definition line. `python tools/lexicon/lexicon.py` exited
1 over the working tree on its verb-offender pin, 1432 offenders over a pin of 1421 (DERIVED, that
run), none of them a name this change wrote, so the breach is not this change's and is owed to the
close.

Owed to the close: every leg the spec's section 7 names, the manifest-check suite whole, whose loop
over `--list` now runs the two new plants and whose floor rises by two, and the `New arm:` line's
RED-first observation, the two new plants and the two re-pointed ones staged red by a copy of the
engine whose reader compares with `read_session_cli_version` alone.

## S4 — the passages of KICK-dKeptSession-12 this unit supersedes

KICK-dKeptSession-12 S2 says the reader prints `pass` only when the recorded verdict is `pass`, its
blob equals the installed fixture's blob now, "and its version equals `read_session_cli_version`'s
answer now", and names among its reasons "`recorded under cli <old>, now <new>`". Both are superseded
by name: by S1, a pass also needs the recorded version to equal `read_claude_version`'s answer now,
PATH's `claude`, and the one version reason splits into `recorded under cli <old>, PATH now <new>` and
`fixture ran cli <x>, this session runs <y>`, tested in that order after the verdict word and the
blob; and by S2, an unknown version on the recorded, PATH or session side reads `red: cli version
unknown · <which>`, never an equality. Unit 12 is CLOSED, so neither its spec nor its acceptance
ledger is written here (F1, resolved (b)).

**Evidences:** KICK-dKeptSession-38
- AC1 — `fixture-cli-path-differs` exported `AI_AGENT=claude-code_9-9-2_agent`, planted a recorded
  `pass` at `cli 9.9.2` for the installed fixture's blob under `resume.context: always-resume`, and put
  a stub `claude` answering `9.9.1 (Claude Code)` first on PATH: the replay's `resume —` line read
  `fresh recommended: idle …` with the override reason `card-import fixture red: recorded under cli
  9.9.2, PATH now 9.9.1`, and the row held (DERIVED, that run).
- AC2 — the same plant then put a stub answering `9.9.2` first on PATH and exported
  `AI_AGENT=claude-code_9-9-3_agent`: the reason read `fixture ran cli 9.9.2, this session runs
  9.9.3`; with `AI_AGENT` back at 9.9.2 the line read `resume — resume recommended (resume.context:
  always-resume)` whole. Three rows held and the plant exited 0 (DERIVED, that run).
- AC3 — `fixture-cli-unknown` unset `AI_AGENT` and planted a recorded `pass` at `cli unknown`: the
  reason read `cli version unknown · recorded`. Its two further rows observe S2's other sides: a
  recorded 9.9.2 under a PATH stub printing nothing and exiting 1 read `cli version unknown · PATH`,
  and a PATH stub answering 9.9.2 with `AI_AGENT` unset read `cli version unknown · session`. Three
  rows held and the plant exited 0 (DERIVED, that run).
- AC4 — `grep -n "PATH" help/orientation-card.md` printed the verdict paragraph's lines naming both
  comparisons, the tested version "both PATH's `claude` now and the version of the session reading
  it", and both reasons (DERIVED, that probe).
- AC5 — from a shell whose PATH held no `claude`, `command -v claude` answering nothing, `--plant
  context-always-resume` printed its one row held and `--plant fixture-stale` its two, the second now
  reading `recorded under cli 1.0.0, PATH now 9.9.2`; each exited 0 (DERIVED, those runs). Each now
  puts a stub `claude` answering 9.9.2 first on PATH, the version its `AI_AGENT` names.
- AC6 — `tr -s ' \r\n' ' '` over this ledger piped into `grep -c "and its version equals"` printed
  `1` and into `grep -c "recorded under cli <old>, now <new>"` printed `1` (DERIVED, those probes), and
  `git diff --name-only` from the pass base over unit 12's spec and its acceptance ledger printed
  nothing (DERIVED, that probe, over the committed pass).
- `--list` prints 46 plants, two more than at the base (DERIVED, `--list` piped into `grep -c .`), and
  `FLOOR_ASSERTIONS` rises from 420 to 422 (PINNED, one ok row per new plant from the suite's loop).
