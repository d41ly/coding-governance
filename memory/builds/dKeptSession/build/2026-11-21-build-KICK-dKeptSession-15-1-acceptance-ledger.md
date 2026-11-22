# KICK-dKeptSession-15 — acceptance ledger

**Serves:** journal KICK-dKeptSession-15

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `994dfe4e`.
AC1 to AC5 ran through the unit's own fixture CLI, `bash card-store.fixture.sh --plant <case>`, one
plant at a time, each over its own scratch remote and repository under a short drive-letter temp
directory, the spelling the suite hands the plants; the suite that loops over `--list` was not run.
AC6 ran as the grep it names. `python tools/lexicon/lexicon.py` exited 1 over the working tree on its
verb-offender pin, 1432 offenders over a pin of 1421 (DERIVED, that run), the count KICK-dKeptSession-26
read at its base; none of the four names this change adds is among them, `--suggest` grading
`render_position_line`, `render_lead_notice`, `run_card_replay` and `set_card_answer` OK as
`sh.function`, so the breach is not this change's and is owed to the close.

`render_position_line` and `render_lead_notice` were probed alone, evaluated out of the engine over a
stub module: an answer outside `ANSWERS`, an `act` whose `next` is null, an `act` whose item holds a
space, and an exit 3 each printed the unreadable skip; a `reason` string carrying an escaped
`"answer": "act"` ahead of the real `stuck` printed `position — stuck · next none`; a frontier row's
item ahead of `next` under exit 2 printed `position — act · next item.n`; `terminal` with a `next`
filled printed `next none`; a stub sleeping past a bound of 1 s (DERIVED, that probe's bound) printed the bound skip and returned
in 1 s (DERIVED, that probe); an empty slug printed the unrouted skip; the notice printed for
`compact` alone, not for `resume` or an empty source, and no scratch file was left under the card dir.
The real engine, `position.py dKeptSession --json` over this tree, answered in 8 s (DERIVED, that run),
and the two matches read `awaiting` and `item.build.base` from its output.

Owed to the close: every leg the spec's section 7 names, the manifest-check suite whole, whose loop
over `--list` now runs the six new plants and whose floor rises by six, and the `New arm:` line's
RED-first observation: a plant staged red by a copy of the engine whose position line prints the
card's stored `item —` key (`position-disagrees`), or whose notice prints after a resume
(`lead-resume`). The `manifest-check self-test` row of the budgets file is not re-priced here, as the
spec does not name it: the six plants took 23 s to 54 s each alone (DERIVED, those runs), about 184 s
together (DERIVED, the sum of those runs), for the main loop's re-price from its first reading.

## Decisions taken in the build

- The engine's answer set is spelled again in `render_position_line` as a `case`, citing
  `tools/loop/position.py#ANSWERS`, because the kickoff kit names no file of another and S1 forbids a
  second process.
- An `act` answer whose `next.item` the match does not read prints the unreadable skip, never `next
  none`: S1 names the item for `act`, so an `act` without one is output the match does not read.
- A scratch file that cannot be made under the card dir prints `position — skipped: no scratch file
  under <card dir> to capture the answer in`, the cause `derive_map_block` names for its own read.
- The plants' stub JSON carries a frontier row naming `item.design.unit-spec` ahead of `next`, so a
  match not anchored on `next` reads the wrong item and the AC1 and AC2 rows red.
- The bound plant times its slow replay against a control replay whose stub answers at once, as
  `lookup-hung` does, and holds the excess to the bound plus five seconds.

**Evidences:** KICK-dKeptSession-15
- AC1 — `bash card-store.fixture.sh --plant position-act`: the replay printed `position — act · next item.build.unit-pass` with a frontier row naming another item ahead of `next`; `position-awaiting` printed `position — awaiting · next none` though its JSON named a next item, then `position — invalid-input · next none` with the stub exiting 2.
  Each row held and each plant exited 0 (DERIVED, those runs).
- AC2 — the plant `position-disagrees`: the replayed card's `## pointers` section kept `item — item.design.unit-spec@TOOL-tFix-1#aaaa0001` while the line read `position — act · next item.build.unit-pass`.
  Both rows held, exit 0 (DERIVED, that run).
- AC3 — the plant `position-skips`: the unrouted card printed `position — skipped: the card routes no build` and its header and READY lines; a loop kit with `position.py` moved aside printed `position — skipped: no loop kit`; a stub sleeping past a lowered bound printed `position — skipped: position.py did not answer within 2s`; and a usage line exiting 2 printed `position — skipped: position.py printed no answer this replay reads` with no `invalid-input` line.
  Each failing replay still printed the card. The slow replay took 3 s over its control (DERIVED,
  that run), within the bound of 2 s the plant sets plus five (PINNED, the plant's own figure). Five
  rows held, exit 0, in 54 s (DERIVED, that run).
- AC4 — the plant `lead-compact`, its payload naming `"source": "compact"` piped on stdin with no `--session`: the `lead —` notice was the line directly after `position — act · next item.build.unit-pass`; `lead-resume`, `"source": "resume"`, printed the position line and no `lead —` line.
  Both plants exited 0 (DERIVED, those runs).
- AC5 — the plant `lead-compact`: `partial —`, `position —`, `lead —` and `now —` stood at lines 42, 43, 44 and 45 of the replay's output, increasing.
  (DERIVED, that run.)
- AC6 — `grep -n "lead —" help/orientation-card.md` printed the example line and the paragraph line naming both `lead —` and `position —`.
  (DERIVED, that probe.)
- `--list` prints six plants more than at the base (DERIVED, the PLANTS line's diff), and `FLOOR_ASSERTIONS` rises from 427 to 433 (PINNED, one ok row per new plant from the suite's loop).
