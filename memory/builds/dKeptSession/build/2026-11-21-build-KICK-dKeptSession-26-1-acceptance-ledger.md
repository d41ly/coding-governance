# KICK-dKeptSession-26 — acceptance ledger

**Serves:** journal KICK-dKeptSession-26

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `4b77f659`.
AC1 to AC4 ran through the unit's own fixture CLI, `bash card-store.fixture.sh --plant <case>`, one
plant at a time, each over its own scratch remote and repository under a short drive-letter temp
directory, the spelling the suite hands the plants; the suite that loops over `--list` was not run.
The neighbouring plants `pointers-render`, `pointers-boundary` and `pointers-cap` printed `held` for
every row the same way, so the stub `budget.py` and the fourth `POINTER_LINES` word move none of them.
AC6 ran through the module's own `--fixture --plant state-answers`. `python tools/lexicon/lexicon.py`
exited 1 over the working tree on its verb-offender pin, 1432 offenders over a pin of 1421 (DERIVED,
that run), the same count KICK-dKeptSession-38 read at its base; neither name this change adds is
among them, `--suggest` grading `render_budget_line` and `read_card_budget` OK as `sh.function`, so
the breach is not this change's and is owed to the close.

`render_budget_line`'s four failure branches were probed alone, the function evaluated out of the
engine over a stub module: an answer `open 1/4` carrying a BEL byte, a CR and a second line printed
`budget — open 1/4x`; an exit 2 printed `budget — skipped: budget.py state exited 2`; a stub sleeping
past `CARD_BUDGET_BOUND=2` printed `budget — skipped: budget.py state did not answer within 2s`; and
no kit printed `budget — skipped: no loop kit` (DERIVED, that probe, 2.3 s for all four).

Owed to the close: every leg the spec's section 7 names, the manifest-check suite whole, whose loop
over `--list` now runs the five new plants and whose floor rises by five, the `loop budget fixtures`
leg, whose `plants=` token now reads 42, and both `New arm:` lines' RED-first observations: the
`budget-omitted` plant's second row staged red by a copy of the engine whose `POINTER_LINES` lacks
`budget`, and the `state-answers` case staged red by a `state` verb printing a line `budget_state`
did not answer.

## Decisions taken in the build

- The check's `POINTERS —` line now ends `; --card --pointers --build <slug> --session <sid> renders
  it`, which the spec's Migration paragraph says it names; the K13 arm's substring still matches.
- The K13 arm's planted section in `manifest-check.test.sh` gains `budget — b`, so it still lacks one
  word, `forks`, and its count of one `POINTERS —` line holds under the fourth word.
- An answer that exits 0 and prints nothing reads `budget — skipped: budget.py state exited 0 and
  printed nothing`, a form section 4's table does not list, so the section is never left without the
  line.
- `state-answers` plants its three builds as three scratch repositories, as the `value` case does:
  one frozen by the move out of designing and drawn once, one under `flow.rework-budget = 0`, and one
  never frozen.

**Evidences:** KICK-dKeptSession-26
- AC1 — `--plant budget-open` planted `budget=open 3/10` and the key K1 in the stub's file, appended
  the READY body and read the ref's card: the line directly after `item —` in its `## pointers`
  section read `budget — open 3/10`; `--plant budget-spent` read `budget — spent` and `--plant
  budget-unfrozen` read `budget — unfrozen 1/4` there. Each row held and each plant exited 0
  (DERIVED, those runs).
- AC2 — `--plant budget-omitted` wrote the section with `--card --pointers`: `--card --check
  --session t1` exited 0 on the card as written, its line after `item —` reading `budget — open
  0/4`, the stub's default; with the `budget —` line cut it exited 1 and its output named `no 'budget
  —' line`. Both rows held, exit 0 (DERIVED, that run).
- AC3 — `--plant budget-no-kit` took the copied `budget.py` out of the scratch repository with `git
  rm`, after which `resolve_kit_file loop budget.py` answered nothing; the published card's line after
  `item —` read `budget — skipped: no loop kit`, and `--card --check` exited 0 on the session card
  carrying it. Three rows held, exit 0 (DERIVED, that run).
- AC4 — the same `budget-open` plant then ran `--card --boundary` once, planted K2 and `open 4/10`,
  and ran it again: the second printed `boundary — K1 → K2` and the ref's card read `item — K2 · at
  …` followed directly by `budget — open 4/10`. The row held; the plant took 58 s (DERIVED, that run).
- AC5 — `grep -n "budget —" help/orientation-card.md` printed the example line `budget — open 3/10`,
  and the bullet's line naming `budget — open <n>/<total>`, `budget — spent` and `budget — unfrozen
  <n>/<total>` (DERIVED, that probe).
- AC6 — `python tools/loop/budget.py --fixture --plant state-answers` printed `open 1/6`, `spent`
  and `unfrozen 0/6`, each beside the same `budget_state` answer, then `loop: fixture · state-answers
  · held`, exit 0, in 3.5 s (DERIVED, that run). Over this repository `state --build dKeptSession`
  printed `open 11/132`, exit 0, in 0.7 s (DERIVED, that run), and `state` with no `--build` exited 2.
- AC7 — `python tools/govkit/docs_leg.py --fingerprints` printed the row
  `script:tools/loop/budget.py#state` with fingerprint `7be78ec8` and page `help/loop.md` (DERIVED,
  that run, after the bullet carried its anchor).
- AC8 — the probe `len(m.PLANTS)` printed `42` and `state-answers` is a key of it, and the grep of the
  `loop budget fixtures` row printed `plants=42` (DERIVED, those probes). Its note gains the re-read
  as PINNED proxy r 181.2 s, the 177.7 s already there plus the case's 3.5 s, and 1.5 r rounds up to
  272 s, under the row's 498 s, which stands (DERIVED, from the case's reading).
- `--list` prints 51 plants, five more than at the base (DERIVED, `--list` piped into `grep -c .`),
  and `FLOOR_ASSERTIONS` rises from 422 to 427 (PINNED, one ok row per new plant from the suite's
  loop).
