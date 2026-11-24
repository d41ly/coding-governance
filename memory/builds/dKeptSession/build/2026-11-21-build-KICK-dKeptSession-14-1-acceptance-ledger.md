# KICK-dKeptSession-14 — acceptance ledger

**Serves:** journal KICK-dKeptSession-14

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands: `render_playbook.py --reference --check` and
`check-install-prefix.sh` were each refused by the role hook as a gate, and the runlog self-test was
not run. The criteria were observed on win32 at the pass's base `18138076`. AC3 to AC6 and AC10 ran
through the unit's own fixture CLI, `bash card-store.fixture.sh --plant <case>`, one plant at a time,
each over its own scratch remote and repository under a short drive-letter temp directory; the suite
that loops over `--list` was not run. AC1 ran as a probe that writes the `context-fill` scenario the
way the self-test's `build_scenario` does and runs the CLI over it; the self-test case itself did not
run. `python tools/lexicon/lexicon.py` exited 1 on its verb-offender pin, 1432 offenders over a pin of
1421 (DERIVED, that run), the count KICK-dKeptSession-15 read at its base; none of the names this change
adds is among them, `--suggest` grading `measure_context_fill`, `derive_context_fill`,
`derive_context_tokens`, `cmd_context` and `test_extract_context_fill` OK as `py.function` and
`render_context_line` and `run_context_boundary` OK as `sh.function`.

`render_context_line` and `read_card_policy`'s two keys were probed alone, evaluated out of the engine
over a stub policy kit and a stub runlog kit: a share of 60 at a threshold of 60 printed the past line,
59 the `under` line; the boundary form printed the fresh-now line at 72 and nothing at 41, with no
transcript, under `compact-with-card` and under a refused threshold; the replay form printed one
`context — skipped:` line each for no transcript path, a path naming no file, an answer of `none`, an
answer that is no share, the CLI's own exit-2 message, no runlog kit, and a stub sleeping past a bound
of 2 s (PINNED, the probe's own bound), which returned in 2 s (DERIVED, that probe); and no scratch file
was left under the card dir. `read_card_policy context.threshold` took `0%`, `9%`, `10%`, `99%` and
`100%` and refused `101%`, `05%`, `60` and `x%` naming the row's pattern.

Owed to the close: every leg the spec's section 7 names; the manifest-check suite whole, whose loop
over `--list` now runs the five `fill-*` plants and whose floor rises by five; the runlog self-test,
whose new case and floor are below; and both `New arm:` lines' RED-first observations. Also owed: the
suite's exact-replay arms (the card block's AC5 replay check and `check_replay`'s map arms) compare
the lines between the stored card and `now —` to nothing, and the replay of a card that routes no
build already printed `position — skipped: the card routes no build` there before this unit
(KICK-dKeptSession-15); this unit adds `context — skipped: no transcript path names the session` on
the same replays, so those arms read two computed lines where they expect none.

## Decisions taken in the build

- At a boundary a refused `context.on-full` or `context.threshold` read prints nothing: S3 says any
  skip prints nothing there and section 5 that a boundary failure prints nothing, so S2's refusal line
  is the replay's, where every failure is one `skipped:` line.
- One function holds both outputs: `render_context_line` takes `boundary` to print only the fresh-now
  line, and `run_context_boundary` is the boundary verb's call of it, so the read, the bound and the
  match are written once and no name past section 4's inventory is minted.
- The CLI exits 2 naming the path when it names no file, as `prose --transcript` does; the engine
  checks the path first and prints its own skip, so the exit is the CLI's alone.
- The share is rounded to nine places before the floor, since a share of 0.29 times 100 reads 28.999…
  in floating point and would print 28.
- The stub runlog kit answers from the plant file the stub loop kit already reads, under the keys
  `fill` and `fill-delay`, as the stub budget does, so the fixture adds no second plant file.
- AC2's grep finds `derive_context_tokens` defined, called in `measure_ready_tree`, and called in
  `derive_context_fill`, which `measure_context_fill` calls for the share: S1 makes the share of one
  event `derive_context_fill`, so `measure_context_fill` reads the sum through it.

**Evidences:** KICK-dKeptSession-14
- AC1 — the probe writing the `context-fill` scenario under a scratch projects root ran `python tools/runlog/runlog.py context` over its main file and printed `60%`, exit 0; over the agent file alone it printed `none`.
  `measure_context_fill` with `until` before the compaction read 0.9, and the whole tree's last usage was the agent's at 0.95 (DERIVED, that probe), the decoy the share does not read.
- AC2 — `grep -n "derive_context_tokens" tools/runlog/extract.py` found the definition and the calls in `measure_ready_tree` and `derive_context_fill`; `grep -c 'ev\["in"\] + ev\["cache_read"\]' tools/runlog/extract.py` printed `1`.
  (DERIVED, that probe.)
- AC3 — the plant `fill-fresh-past`: the crossing `none → K1` under `fresh-at-boundary` and `60%`, the stub answering `72%`, printed `context — 72% of window · past 60% · fresh now, at this item boundary (context.on-full: fresh-at-boundary)`.
  The row held, exit 0, in 25 s (DERIVED, that run).
- AC4 — the plant `fill-under`: the crossing at `41%` printed no `context —` line, and the next boundary, none crossed, at `72%` printed none either.
  Both rows held, exit 0 (DERIVED, that run).
- AC5 — the plant `fill-compact`: under `compact-with-card` the crossing at `72%` printed no `context —` line, and the stub policy kit's log held `context.on-full` and no `context.threshold`.
  Both rows held, exit 0 (DERIVED, that run).
- AC6 — the plant `fill-replay`, a compaction replayed with the payload's `transcript_path`: `position —`, `context — 72% of window · past 60% · fresh at next item boundary (context.on-full: fresh-at-boundary)` and `now —` stood at lines 43, 45 and 46, increasing; under `compact-with-card` the line read `context — 72% of window (context.on-full: compact-with-card)`, and at `41%` `context — 41% of window · under 60%`.
  Three rows held, exit 0, in 45 s (DERIVED, that run).
- AC8 — `python tools/policy/policy.py get context.on-full` and `get context.threshold` printed `fresh-at-boundary` and `60%` in this tree, whose policy file sets neither; after `policy.py lists --write`, which drained the two rows, `grep -c '^context\.' tools/policy/unsummarised-keys.txt` printed `0`.
  (DERIVED, that probe.)
- AC9 — `grep -n "context.on-full" help/orientation-card.md` found the example line and S9's paragraph, which names `fresh-at-boundary`, `compact-with-card` and `context.threshold` and carries both keys' usage anchors.
  (DERIVED, that probe.)
- AC10 — the plant `fill-slow`: the stub sleeping past `CARD_CONTEXT_BOUND=2` printed `context — skipped: runlog.py did not answer within 2s` and the replay still ended with its `now —` line; the slow replay took 1 s over its control (DERIVED, that run), within the bound plus five (PINNED, the plant's own figure).
  Both rows held, exit 0, in 36 s (DERIVED, that run).
- AC11 — `python tools/playbook/render_playbook.py --reference` re-rendered the page after the anchors stood; `grep -n -A1` over it showed each `context.*` key's section followed by a `Documented on [help/orientation-card.md]` line, and `card.pointers` moved there off `## Not yet summarised`, now counting 223 rows (DERIVED, that render); `grep -cP '^policy:context\.' memory/project/docs-undocumented.txt` printed `0`; `docs_leg.py --fingerprints` named `help/orientation-card.md` for both keys.
  The `--check` form is the close's.
- The plants `fixture-run`, `replay-order` and `lead-compact` still held over the changed engine and stub policy kit (DERIVED, those runs). `--list` prints five plants more than at the base (DERIVED, the PLANTS line's diff); `FLOOR_ASSERTIONS` rises from 433 to 438 and `ASSERTION_FLOOR` from 1580 to 1587 (PINNED, the counts each comment prices).
- seen-red — `runlog selftest` — red `f6a0d7aaf` — green `f6a0d7aaf` — `test_extract_context_fill`: a later usage, whoever made it, read as the main session's
- seen-red — `manifest-check self-test` — red `45016a2c4` — green `45016a2c4` — `fill-fresh-past`: a crossing past the threshold that prints nothing
- seen-red — `manifest-check self-test` — red `f6a0d7aaf` — green `f6a0d7aaf` — `fill-under`: a fill under the threshold read as past it
- seen-red — `manifest-check self-test` — red `f6a0d7aaf` — green `f6a0d7aaf` — `fill-replay`: a replay that prints no `context —` line
