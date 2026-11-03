# TOOL-dCalibratedLens-2 — the shared value ledger: its snapshot, its view, its row grammar and the `price` verb

**Status:** DEFERRED · rev-6 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 1 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0459@facc646b whole
**Carries:** node:record-kind.value-ledger
**Carries:** node:item.loop.price
**Carries:** node:policy-key.review.loop.catch-source

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-2-chain-rounds.md](../build/2026-11-02-build-TOOL-dCalibratedLens-2-chain-rounds.md) | journal | — |
| [2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md) | journal | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |
| [2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-42 |
| [2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-reground-returns.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-reground-returns.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-42 |
| [2026-11-03-build-TOOL-dCalibratedLens-1-crosscheck-returns.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-crosscheck-returns.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 |
| [2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46 |
| [2026-11-03-build-TOOL-dCalibratedLens-1-reground-returns.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-reground-returns.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46 |
| [2026-11-03-build-TOOL-dCalibratedLens-2-deviation-22.md](../build/2026-11-03-build-TOOL-dCalibratedLens-2-deviation-22.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-2-deviation-23.md](../build/2026-11-03-build-TOOL-dCalibratedLens-2-deviation-23.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-2-deviation-24.md](../build/2026-11-03-build-TOOL-dCalibratedLens-2-deviation-24.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-2-deviation-25.md](../build/2026-11-03-build-TOOL-dCalibratedLens-2-deviation-25.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-2-deviation-26.md](../build/2026-11-03-build-TOOL-dCalibratedLens-2-deviation-26.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-edge-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-edge-fix-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-15 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-48 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-42 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-29 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-crosscheck.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-crosscheck.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-2-1-spec-reviewer.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-2-1-spec-reviewer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-2-2-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-2-2-spec-writer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-2-3-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-2-3-spec-writer.md) | journal | — |
| [2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-14 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing prices or retires a leg, rule or bug class, so the governing surface only grows (gap-maint-03).
This unit lands the shared value ledger every pricing clause of this build writes into: one generated
row per priced thing, `| kind | id | since | cost | catches | false-reds | last-catch | window | state |`
(layer-expansions:261), written by `python tools/loop/loop_review.py price` as a dated snapshot and
rendered as the library view `<MEMORY_ROOT>/views/value-ledger.md`, never typed. It ships the first row
kind, `leg`, because a catch is a leg's red, and reads catches from the source
`review.loop.catch-source` names: `verdict-records`, the default, or `node-journal`.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`: TOOL-dDeclaredLoop-1 (the loop
kit `tools/loop/`, its `kit.toml` and `loop.toml`) and TOOL-dDeclaredLoop-12 (the `[[item]]` row form
and `check_program`); TOOL-dLinkedLibrary-6 (`tools/memory-tree/library_views.py`, `VIEWS`,
`render_library_views` and `LIBRARY_VIEWS`); TOOL-dTotalRecall-1 (`tools/memory-tree/record-kinds.toml`
and its `record-kinds` leg); TOOL-dWitnessedBar-8 S3 (the flake record, the `verdict-records` source);
TOOL-dDeclaredLoop-110 in `memory/builds/dDeclaredLoop/BACKLOG.md` (AC8, id 26). The build run re-grounds on each and stops the unit when one is absent.

- **S1** — The module, `tools/loop/loop_review.py`, created by this unit with one verb, `price`, and the
  argparse frame unit 3 adds its verbs to (§8 F1). `read_loop_policy(root, key)` is the module's one
  policy reader: a bounded `policy.py get <key>` subprocess (30 s), the policy kit found through the
  inline `resolve_kit_dir` block (`tools/lib/resolve_kit_dir.py`, held byte-identical by
  `tools/lib/resolve-python.test.sh`'s parity table), the key a string literal at each call; a refused
  read, a timeout or no policy kit takes the catalogue default with one `NOTE:` line naming the key.
  `derive_loop_window(root, at)` reads `review.loop.window-days` through it once and returns the window
  `(start, end, days)`, `end` the UTC day of `at` and `start` that day less `days`; it is the one window
  every Loop Review reading takes (unit 3). Observed by AC2, AC3 and AC6.
- **S2** — The row grammar and the pricer. `derive_ledger_rows(rows, events, window)` joins the rows the
  providers return with the catch events the source returns, by `(kind, id)`, as §4 "The row" states:
  `catches` the own events in the window, `false-reds` the false ones, `last-catch` the newest own
  event's date at any age, `window` the window's days, and `state` from `derive_row_state(row, window)`:
  `catching` with a catch in the window, `new` when `since` falls inside it, `idle` otherwise.
  `PROVIDERS` maps a kind to its reader; this unit's one entry is `leg` (S3), and units 7, 9, 12 and 15
  each add one. Observed by AC1, AC3 and AC4.
- **S3** — The `leg` provider, `read_leg_rows(root, window)`: one row per leg of `tools/gate-legs.json`,
  `id` the leg's `name`; `since` the date of the first commit whose diff of that file adds the name,
  from one `git log --reverse -p --unified=0 -- tools/gate-legs.json` pass; `cost` the leg's
  `<max seconds>` and `<readings>` columns of `tools/run-gates/ceiling-evidence.txt` (its header,
  `:28`), spelled `<seconds>s/<readings>`, or `-` for a leg with no row there. Observed by AC1 and AC3.
- **S4** — (amended, ids 27, 48) The catch source, `read_catch_events(root, source, window)`, `source` the value of
  `review.loop.catch-source` read through S1. Under `verdict-records`, `read_flake_events(root)` reads
  every tracked flake record (`<MEMORY_ROOT>/builds/*/build/*-flake-*.md`, TOOL-dWitnessedBar-8 S3), its
  date the `Ended` field as `read_record_fields(text)` returns it (the `- **<Key>:** <value>` grammar of
  `FIELD`, `tools/memory-tree/deviation_join.py:150`, carried inline) and its rows the fenced `tsv`
  block, `<leg name>`, TAB, `<first rc>`, TAB, `<re-run rc or ->`: a non-zero first rc whose re-run rc
  is non-zero or `-` is an own event, one whose re-run rc is 0 a false one. Under `node-journal`, `read_journal_events(root)` runs `python <runlog
  kit>/runlog.py journal --producer gates` (`tools/runlog/runlog.py:151`, `:498-503`) and takes each
  `RED` bar's `fail.<n>` names as own events at the line's `t`; the journal cannot tell a flake, so
  `false-reds` reads `-` under this value. Each value is seen on its planted case. Observed by AC1 and
  AC2.
- **S5** — The `price` verb, `run_loop_price(root, key, at, dry_run)`, run as `python loop_review.py
  price [--key <key>] [--at <utc>] [--dry-run]`. The key is `GOV_CADENCE_KEY` (ask
  TOOL-dTendedCadence-27); `--key <key>` is admitted only with `--dry-run`, as TOOL-dTendedCadence-1 S3
  admits it, and `--key` without `--dry-run` exits 2. No key at all exits 2,
  `price — refused: no key; run under cadence.py run loop-review`. The key is held to the period-key
  grammar of §4 "The snapshot" at the write boundary, anything else exit 2 before a read; `at` is now, or `--at`. It takes the window from
  `derive_loop_window` (S1), builds the rows, and writes the snapshot through `write_ledger_snapshot`;
  `--dry-run` prints the table and writes nothing. It prints `price — <key> · <n> row(s) · source <value> · <path>`
  and exits 0. It commits nothing. Observed by AC1, AC5.
- **S6** — (amended, ids 36, 38) The snapshot, the record kind `value-ledger`: `render_ledger_snapshot(key, at, base,
  source, window, rows)` and `write_ledger_snapshot(root, ...)`, one file per key at
  `<MEMORY_ROOT>/loop-review/<date>-value-ledger-<key>.md`, written through a temp file and `os.replace`
  as `write_record` does (`tools/runlog/record.py:1179-1201`), contained under the home. Its registry
  row in `tools/memory-tree/record-kinds.toml` is §4 "The registry row". Observed by AC5 and AC7.
- **S7** — The view, a `VIEWS` row `value-ledger` at `views/value-ledger.md` in
  `tools/memory-tree/library_views.py`, its renderer `render_value_ledger(root, conf)` rendering the
  newest TRACKED snapshot under the home, an empty render the line `No value-ledger snapshot yet.` and
  no finding; `value-ledger` joins the armed set (`LIBRARY_VIEWS`, or `memory.library-views` once
  TOOL-dLinkedLibrary-52 S26 has moved it). The view's one writer is the library-view host's
  `cmd_write`, and its `--check` reds a hand-edited view (TOOL-dLinkedLibrary-6 S3, §8 F2). Its fixture
  cases `value-ledger`, `value-ledger-empty` and `value-ledger-hand-edit` join `library_views.py
  --fixture`. Observed by AC4.
- **S8** — (amended, id 1) The structure lint admits the home: check 3 of `tools/memory-tree/check-memory-hygiene.sh`
  adds `D:loop-review` to the memory root's sanctioned set (`:891`), and the check's prose in
  `tools/memory-tree/HYGIENE.template.md` names `loop-review/` and its two kinds, re-rendered into
  `memory/HYGIENE.md` by `adopt-memory-tree.sh --render`. Observed by AC7.
- **S9** — (amended, id 26) The item row `item.loop.price` in `tools/loop/loop.toml` (the spec brief's shared interface
  S5, in the row form of TOOL-dDeclaredLoop-12 §4 "Data model"): `step = "cadence.loop"`,
  `actor = "command:loop.price"`, `needs = []`,
  `inputs = ["layer.observability:the catch source and tools/gate-legs.json"]`, `allowance = "records"`,
  `outcomes = ["priced"]`, `routes = { priced = "stand-in:tools/loop/loop_review.py" }`,
  `returns = "record-kind.value-ledger"`, `witness = { class = "history", by = "the value-ledger snapshot" }`,
  `owner = "dCalibratedLens"`, the keys a non-role actor requires (TOOL-dDeclaredLoop-9 S1); unit 3 re-points `needs` to
  `item.loop.gather` and the route to `item.loop.file`, and unit 5 the route to `item.loop.propose`.
  Observed by AC8.
- **S10** — The catalogue row `review.loop.catch-source` (`tools/policy/catalogue.toml:1302-1306`)
  gains `summary` and `usage`, and `python tools/policy/policy.py lists --write` drains it from
  `tools/policy/unsummarised-keys.txt` (`:191`); values and default stay the row's. Observed by AC6.
- **S11** — (amended, id 42) The leg `loop-review selftest`, argv `python {prefix}/loop/loop_review.py --fixture`, guard
  `{prefix}/loop/`, its `enforces` the practice tag of the charter's `[derive]` rule as
  PLAY-dOrderedCharter-7 S3's tag set spells it at the build run, a `[[gate_leg]]` row of
  `tools/loop/kit.toml` written by `leg_factory.py new` (TOOL-dWitnessedBar-11 S1 to S3), or a hand-written row of
  `tools/gate-legs.json` until that factory lands. NOT OBSERVED by a criterion: a manifest row; the main
  loop observes it RED and GREEN at the close (§7).
- **S12** — (amended, id 39) The docs: a new page `help/loop-review.md` with the section "The value ledger" (the row,
  each column's source, the two catch sources, the snapshot and the view, `price` and `--dry-run`),
  carrying the usage anchor `python tools/govkit/docs_leg.py --list` names for `loop_review.py`, and
  its line in `help/README.md`. Observed by AC9.

## 3. Non-goals (OUT)

- The Loop Review's other items, its lease, its period and its record: unit 3. `price` here runs alone
  under `GOV_CADENCE_KEY`, or `--dry-run --key`, and inside unit 3's walk under `GOV_CADENCE_KEY`.
- Row kinds other than `leg`: `shape` (unit 7), `probe` (unit 9), `item` (unit 12) and `cap` (unit 15),
  each a `PROVIDERS` entry. Rules and bug classes get no row: no source attributes a catch to either
  (0 of 129 gotchas carry a catch field, research-observability-a's gap-obs-01), so a row would read
  `idle` for want of a source, not for want of a catch.
- The `kept` state and the keep record: unit 5 adds both to `derive_row_state`.
- Proposing a retirement from a row: unit 5's `propose`. The ledger proposes nothing.
- Committing the snapshot: unit 3's record step files the records-only intake that lands it.
- A catch history beyond what the two sources hold: Test's flake record is dWitnessedBar's.

### Edges

- **hands-off** `TOOL-dCalibratedLens-3` — the module `tools/loop/loop_review.py`, `read_loop_policy` and `derive_loop_window`, which gain `lease`, `gather`, `file`, `record` and the walk; the `item.loop.price` row, whose `needs` it re-points to `item.loop.gather` and its route to `item.loop.file`; the home `loop-review/`, where its record sits beside the snapshot
- **hands-off** `TOOL-dCalibratedLens-5` — `derive_row_state`, which gains `kept` from the keep records, and the `item.loop.price` route, re-pointed to `item.loop.propose`
- **hands-off** `TOOL-dCalibratedLens-7` — `PROVIDERS`, which gains the `shape` entry, `read_record_fields` and the `-` catches rule its act rows take
- **hands-off** `TOOL-dCalibratedLens-9` — `PROVIDERS`, which gains the `probe` entry
- **hands-off** `TOOL-dCalibratedLens-12` — `PROVIDERS`, which gains the `item` entry
- **hands-off** `TOOL-dCalibratedLens-15` — `PROVIDERS`, which gains the `cap` entry
- **hands-off** `TOOL-dCalibratedLens-4` — `PROVIDERS`, whose `cap` entry (TOOL-dCalibratedLens-15's `derive_cap_rows`) its caps step calls in-process for each cap's current cost (id 5)
- **hands-off** `TOOL-dCalibratedLens-17` — the module `tools/loop/loop_review.py`, `read_loop_policy` for `trace.cost`, and the help page `help/loop-review.md` it adds a section to
- **consumes-from** external — TOOL-dDeclaredLoop-1 and -12 (the loop kit and its item rows), TOOL-dLinkedLibrary-6 (the library-view seam), TOOL-dTotalRecall-1 (the registry), TOOL-dWitnessedBar-8 S3 (the flake record), each DEFERRED at base; `runlog.py journal`, landed
- **hands-off** `TOOL-dCalibratedLens-19` — `write_ledger_snapshot` and the `value-ledger` row, whose glob home that unit's `three-homes` plant grades (id 1)
- **hands-off** `TOOL-dCalibratedLens-20` — `render_ledger_snapshot` and `write_ledger_snapshot`, whose Serves line that unit's `serves-kinds` plant grades (id 36)
- **hands-off** `TOOL-dCalibratedLens-26` — `read_catch_events`, `derive_ledger_rows` and `price`, whose observed-leg rule that unit's catch plants prove (id 48)
- **hands-off** `TOOL-dCalibratedLens-30` — `price` and the `cost` grammar, which the minors batch's `cost-grammar` arm validates (id 9)
- **hands-off** `TOOL-dCalibratedLens-46` — the `loop-review selftest` row of S11, whose guard that unit widens, in the row's declaration, to the files the loop plants run (round-2 id 13, round-3 id 22)

## 4. Design

### Evidence

- The four catalogue rows this build's ledger reads exist: `review.loop.catch-source`
  (`tools/policy/catalogue.toml:1302-1306`, `verdict-records` default) and `review.loop.window-days`
  (`:1295-1300`, `60`), and `python tools/policy/policy.py get review.loop.catch-source` prints
  `verdict-records` at base.
- No committed record holds a leg's reds today: the gate ledger keeps each leg's last state, and the
  gates journal is node-local, `<git-common-dir>/runlog/gates.log` (`tools/run-gates/run-gates.sh:2466-2470`,
  `:2658`). The flake record is the committed per-leg verdict once TOOL-dWitnessedBar-8 lands, and
  `verdict.flakes` defaults to `quarantine` (`catalogue.toml:863-866`), which writes one at every
  `test.flakes`.
- `runlog.py journal --producer gates` prints one JSON object per good journal line, its keys the
  line's, `fail.<n>` among them (`tools/runlog/README.md:70-75`); `--by-leg` already counts reds per
  leg but over the whole journal with no window (`:80-88`), so S4 reads the per-line form.
- `tools/gate-legs.json` names 148 legs and its history adds 536 `name` lines (id 24); one `git log -p` pass over
  it took 0.28 s at `8bec4cef` (PINNED, 2026-11-02).

### The row

| Column | Value | Source |
|---|---|---|
| `kind` | the provider's key: `leg` here | `PROVIDERS` |
| `id` | the priced thing's name, `|` escaped as `\|` | the provider |
| `since` | ISO date it first existed | the provider |
| `cost` | `<number><unit>/<runs>`, unit `s` or `tok`, or `-` | the provider |
| `catches` | own events in the window, or `-` where the source names none for the kind | the catch source, or the provider |
| `false-reds` | false events in the window, or `-` | the same |
| `last-catch` | the newest own event's ISO date, or `-` | the same |
| `window` | `<days>d` | `review.loop.window-days` |
| `state` | `catching`, `new` or `idle` | `derive_row_state` |

A provider is `reader(root, window) -> (rows, events)`. A provider whose kind carries its own catches
(unit 7's shape rows, from their confirmed findings) returns them as events; every other row is joined
to the catch source's events. A row a provider returns with `catches` set to `-` keeps `-` in its three
catch columns, so a kind no source attributes a catch to never reads as one that caught nothing. An
event is `(kind, id, date, own|false)`. `-` is an absence, never `0`,
as the review-shape line's own rule (`tools/workflows/tier2-review.template.js:74-76`). Rows sort by
kind, then id.

### The snapshot

```markdown
# Value ledger — 2026-W45

**Key:** 2026-W45
**At:** 2026-11-02T09:00:00Z
**Base:** <40-hex sha the rows were read at>
**Source:** verdict-records
**Window:** 2026-09-03..2026-11-02 · 60d

| kind | id | since | cost | catches | false-reds | last-catch | window | state |
|---|---|---|---|---|---|---|---|---|
| leg | memory hygiene | 2026-06-30 | 41.2s/3 | 2 | 0 | 2026-10-28 | 60d | catching |
```

The key is held at the write boundary to `^\d{4}-(W\d{2}|\d{2})$` or `^n\d+\.[0-9a-f]{12}$`, so no
key is a path. Only the weekly form has a source at base: `derive_period` gives `weekly` and `daily` only
(TOOL-dWellOiledMachine-13 S5), and unit 3's monthly and `n<k>.<sha12>` forms come only from unit 3 §8
F2's ask, THE PERIOD KEY HAS NO MONTH AND NO LANDING COUNT. Until that ask lands, `GOV_CADENCE_KEY`
carries the weekly form alone. `<date>` in the file name is the
UTC day of `at`. The five `**Key:**`-line fields are the kind's `fields` form; the table is the
snapshot's body, written as the view will show it.

### The registry row

```toml
[[record-kind]]
name = "value-ledger"
tag = "record.value-ledger"
layer = "layer.observability"
home = "<MEMORY_ROOT>/loop-review/"
id-rule = "<date>-value-ledger-<key>.md"
schema = { form = "fields", fields = ["Key", "At", "Base", "Source", "Window"] }
writer = "loop_review.py price"
readers = ["library_views.py"]
lifecycle = "written once per Loop Review period, never edited; the view renders the newest"
check = "record-kinds"
```

### The view

`render_value_ledger` reads the tracked snapshots under the home (`git ls-files`), takes the newest by
file-name date and then key, and renders a generated-file comment, the H1 `# Value ledger — priced at
<key>`, the line `<n> rows · source <value> · window <days>d · from <relative link to the snapshot>`,
and the snapshot's table verbatim. It never re-prices: a snapshot holds node-local evidence under
`node-journal` and a window fixed at its `at`, so a render at check time from live sources would differ
by node and by day, and the view must equal its render on every node (§8 F2).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/loop_review.py` | module | none |
| `read_loop_policy`, `derive_loop_window`, `read_record_fields`, `derive_ledger_rows`, `derive_row_state`, `read_leg_rows`, `read_catch_events`, `read_flake_events`, `read_journal_events`, `run_loop_price`, `render_ledger_snapshot`, `write_ledger_snapshot` | functions in `loop_review.py` | `py.function`, each answered OK by `lexicon.py --suggest` at base |
| `PROVIDERS` | table in `loop_review.py` | none |
| `render_value_ledger` | function in `library_views.py` | `py.function`, OK at base |
| `value-ledger` | record kind, `VIEWS` row and view name | none |
| `catching`, `new`, `idle` | state values | none |
| `loop-review/` | memory-root folder, sanctioned by check 3 | none |
| `loop-review selftest` | gate leg | none |

§6 runs a sibling's file by its basename: `loop_lib.py` is `tools/loop/loop_lib.py` (TOOL-dDeclaredLoop-12).

### Amendments (round-1 spec audit)

The round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Each bullet supersedes the text it
names; the unit it names owns the finding and its proof.

- **id 1 · §4 "The registry row", S8 (H1, `TOOL-dCalibratedLens-19`)** — The row's home is
  `home = "memory/loop-review/*-value-ledger-*.md"`, the glob of its id-rule, spelled with this
  repository's memory root as TOOL-dTotalRecall-42 S1 spells the shape-run home. S8's check-3 prose
  names `loop-review/` and its three kinds, `value-ledger`, `loop-review` and `keep`.
- **id 36 · §4 "The snapshot", S6 (H2, `TOOL-dCalibratedLens-20`)** — The snapshot's third line is
  `**Serves:** value-ledger TOOL-dCalibratedLens-2`, and `value-ledger` joins the untyped part of
  `RECORD_KIND_TOKENS` in `tools/memory-tree/tree_lib.py` (TOOL-dTotalRecall-18 S7), not
  `TYPED_RECORD_KINDS`, which TOOL-dTotalRecall-1 S2 and PLAY-dOrderedCharter-42 S2-S3 tie to the
  factory's file-name form, and the closed `<kind>` list of
  `tools/memory-tree/HYGIENE.template.md`, rendered into `memory/HYGIENE.md`, in this pass, so
  TOOL-dTotalRecall-42 S5 grades the snapshot by its own row.
- **id 48 · S4, §5 (H8, `TOOL-dCalibratedLens-26`)** — A leg's `catches`, `false-reds` and
  `last-catch` are a count only when the source observed the leg run in the window, and `-`
  otherwise; `read_catch_events` answers the observed set beside the events. Under `verdict-records`
  a leg is observed when a tracked flake record whose `Ended` lies in the window carries its row
  (TOOL-dWitnessedBar-8 S3 writes a row per executed leg); `verdict.flakes = retry-only` writes
  none, so every leg reads `-`. Under `node-journal` a leg is observed when the journal read
  succeeded, a GREEN or RED bar lies in the window, and the leg is `always_run` in `build_leg_yield`
  or a windowed bar named it red; an absent or unreadable journal (exit 2), a timeout or no runlog
  kit observes none. `price` prints
  `NOTE: catch source <value> observed no run of <n> leg(s) · <why>` when any leg reads `-`.
- **id 27 · S4 (M11, `TOOL-dCalibratedLens-30`)** — Under `node-journal` the reds come from
  `runlog.py journal --producer gates --by-leg --legs tools/gate-legs.json`, never a second count of
  `fail.<n>` names: this unit adds an optional `--since <utc>` and `--until <utc>` filter on
  `started` to that verb, runs it windowed for `red` (the catches) and `unattributed`, and
  unwindowed for `last_red`; `price`'s summary line names `unattributed <n>` when it is above 0.
- **id 9 · §4 "The row" (M5, `TOOL-dCalibratedLens-30`)** — `cost` is `<number><unit>/<runs>` with
  unit `s`, `tok` or `B`, the last TOOL-dCalibratedLens-15's bytes times reads (`4433344B/212`), or
  `-`.
- **id 12 · §4 "The registry row" (L2, `TOOL-dCalibratedLens-30`)** —
  `writer = "loop_review.py price; loop_review.py record"`: `record` re-writes the snapshot in the
  patch build that lands it (TOOL-dCalibratedLens-3 S8).
- **id 37 · §4 "The registry row", AC7 (M17, `TOOL-dCalibratedLens-30`)** — The row carries
  `unarmed = "no snapshot is tracked until loop_review.py record lands the first period"`
  (TOOL-dTotalRecall-42 S2), and AC7 also runs `python tools/memory-tree/record_kinds.py --check`
  after the pass: exit 0. The check reds the key once the home matches a file, so the commit that
  lands the first snapshot, TOOL-dCalibratedLens-3 S8's patch build, drops `unarmed` from this row,
  and that unit's AC observes the dropped key.
- **id 38 · S6 (M18, `TOOL-dCalibratedLens-30`)** — After the row edit the pass runs
  `python tools/memory-tree/record_kinds.py --write`, which renders the `<!-- gen:record-kinds -->`
  region of `tools/memory-tree/HYGIENE.template.md`, then `adopt-memory-tree.sh --render` into
  `memory/HYGIENE.md`; both copies land in one commit.
- **id 39 · S12, AC9 (M19, `TOOL-dCalibratedLens-30`)** — `tools/govkit/usage.toml` gains the
  `[[usage]]` row `script:{prefix}/loop/loop_review.py#price` with the flags `--key`, `--at` and
  `--dry-run`, and the page's `<!-- usage: … -->` anchor carries its fingerprint; AC9 also runs
  `python tools/govkit/docs_leg.py --list` and finds the row. Every later unit that adds a
  `loop_review.py` verb or flag to the page adds or re-fingerprints its row.
- **id 42 · S11 (M22, `TOOL-dCalibratedLens-30`)** — The leg `loop-review selftest` is claimed under
  `[claims] gate-legs` by TOOL-dDeclaredLoop-1 S7's kit dossier `memory/map/features/loop.md`; its row names `subject` and `chunk`;
  `tools/govkit/subject-pins.tsv` is regenerated by `govkit.py selfcheck --write`; and a held leg
  gains its measured row in `tools/run-gates/selftest-budgets.txt`.
- **id 26 · S9 (M10, `TOOL-dCalibratedLens-30`)** — The `cadence.loop` step value is
  TOOL-dCalibratedLens-3 §8 F5's fork, mirrored here: the rows stay in `tools/loop/loop.toml`, and
  AC8's `loop_lib.py --check` passing them is a build-run precondition on F5's filed ask
  TOOL-dDeclaredLoop-110, THE LOOP KIT REFUSES A CADENCE STEP VALUE.
- **id 24 · §4 Evidence (L9, `TOOL-dCalibratedLens-30`)** — Corrected in place: the manifest's
  history adds 536 `name` lines across both forms at `8bec4cef`
  (`git log -p -- tools/gate-legs.json` lines matching `^+.*"name"`, PINNED 2026-11-02), the
  one-line `{ "name": ... }` rows of 2026-07-19 included, and `read_leg_rows` matches
  `"name": "<name>"` anywhere on an added line.

### Amendments (round-2 spec audit)

The round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Its ids restart at 1, so each bullet
spells `r2 id`; each supersedes the text it names, and the unit it names owns the finding and its
proof.

- **r2 id 17 · id 48's bullet (M9, `TOOL-dCalibratedLens-41`)** — Under `node-journal` an
  `always_run` leg counts as observed in a windowed GREEN or RED bar only when it declares no
  `doc_reads`; a leg declaring `doc_reads` is skipped by a docs-mode bar before its guard is read
  (`tools/run-gates/run-gates.sh:3257-3262`), so it is observed only when a windowed bar named it red,
  and otherwise its catch columns read `-`.

### Files touched (estimate)

- `tools/loop/loop_review.py`: new (S1 to S6)
- `tools/loop/loop.toml`: the `item.loop.price` row (S9)
- `tools/loop/kit.toml`: the module's file row and the leg row (S11)
- `tools/gate-legs.json`: the leg's row, rendered or hand-written (S11)
- `tools/memory-tree/library_views.py`: the `VIEWS` row, its renderer and three fixture cases (S7)
- `tools/memory-tree/record-kinds.toml`: the row (S6)
- `tools/memory-tree/check-memory-hygiene.sh`: check 3's set (S8)
- `tools/memory-tree/HYGIENE.template.md` and its render `memory/HYGIENE.md` (S8)
- `.memory-tree.conf`: `LIBRARY_VIEWS` gains `value-ledger` (S7)
- `tools/policy/catalogue.toml` and `tools/policy/unsummarised-keys.txt` (S10)
- `help/loop-review.md`: new, and `help/README.md` (S12)
- `tools/memory-tree/tree_lib.py` — `RECORD_KIND_TOKENS` gains `value-ledger` (id 36)
- `tools/runlog/runlog.py` and `tools/runlog/README.md` — `--since` and `--until` on `journal --by-leg` (id 27)
- `tools/govkit/usage.toml` — the `price` row (id 39)
- `memory/map/features/loop.md`, `tools/govkit/subject-pins.tsv` and `tools/run-gates/selftest-budgets.txt` — the leg's claim, pin and budget (id 42)

### Alternatives rejected

- **Price at render time, the view a pure function of live sources.** The test: render the fixture's
  view under `node-journal` on two clones with different `gates.log` files; the two renders differ, so
  `--check` reds on one of them with nothing changed.
- **The snapshot inside the Loop Review record.** That record is unit 3's, built after this unit
  (order 2), so the view would read a kind nobody has built; and `price` alone could never be observed.
  The record cites the snapshot by path instead, one fact in one place.
- **`price` writing the view itself.** A second writer of a file the library-view host already writes
  and compares (TOOL-dLinkedLibrary-6 S3), and a loop-kit import of a memory-tree module across a kit
  boundary.
- **A `rule` and a `bug-class` row kind now.** Neither has a catch source; see §3.

## 5. Production-readiness checklist

- security — the key is held to two anchored patterns before any path is built from it, the write is
  contained under the home and atomic, every subprocess takes an argument list and a timeout, and no
  value read from a record reaches a shell; the snapshot carries leg names, counts and dates only.
- perf / scale — one `git log -p` pass (0.28 s at base, PINNED), one read of each tracked flake record,
  one bounded journal subprocess, two policy reads; 148 rows today.
- error / empty / loading states — no flake record: every leg's `catches` reads `-` (id 48) and the line names
  `0 record(s)`; an absent journal: `runlog: <path> absent`, zero events; a leg with no evidence row:
  cost `-`; no snapshot: the view's empty line; a refused policy read: the default and a `NOTE:` line.
- observability — `price`'s summary line; the snapshot is the history, one per period.
- risks — under `node-journal` a snapshot reflects one node's bars only, as v2:1345 warns; the
  `Source` field says which.
- testing — the fixture cases of §6 and the arms of §7.
- migration — N/A: new files and one new row in each registry; no existing record changes.
- user docs — `help/loop-review.md` (S12).

## 6. Acceptance criteria

- **AC1** — When `python loop_review.py --fixture --plant catch-verdict-records` runs, a
  fixture whose flake record holds `alpha` at first rc 1 and re-run rc 1 and `beta` at first rc 1 and
  re-run rc 0, `price --dry-run --key 2026-W45` prints the `alpha` row with `catches` 1, `false-reds` 0 and that record's
  `Ended` date as `last-catch`, and the `beta` row with `catches` 0 and `false-reds` 1.
  Red when: a red-then-green row is counted a catch, or a flake is not counted a false red.
- **AC2** — When the plant `catch-node-journal` commits `review.loop.catch-source = "node-journal"` and
  writes one `RED` gates line naming `beta` in `fail.1`, `price --dry-run --key 2026-W45` prints `beta` with `catches` 1
  and `false-reds` `-`, ignores the flake record, and its summary names `source node-journal`; the
  plant `catch-source-refused`, a policy file the reader refuses, prints the `NOTE:` line and prices
  from `verdict-records`.
  Red when: the key's value is ignored, or a refused read prices from neither source.
  fixture: a throwaway repository and its common dir's `gates.log` under `%TEMP%` with a short
  name; policy is read at the committed revision, so the plant commits `.governance/policy.toml`.
- **AC3** — When the plant `window-edge` sets `review.loop.window-days = 30` and places one own event 31
  days before `--at` and a leg first added 10 days before it, `price --dry-run --key 2026-W45 --at <at>` prints the old
  event's leg with `catches` 0, its `last-catch` that event's date and `state` `idle`, and the young leg
  with `state` `new`.
  Red when: an event outside the window is counted, or `last-catch` is cut to the window.
  figure: dates DERIVED from the planted `--at`.
- **AC4** — When `python library_views.py --fixture --plant value-ledger` arms the
  view over two snapshots, the render's H1 names the newer key and its table equals that snapshot's;
  `value-ledger-empty` renders `No value-ledger snapshot yet.` with no finding; `value-ledger-hand-edit`
  edits one cell of the view and the host's check names `value-ledger.md` as drifted.
  Red when: the older snapshot renders, an empty home reds, or a hand edit passes.
- **AC5** — When `GOV_CADENCE_KEY=2026-W45 price --at 2026-11-02T09:00:00Z` runs in the fixture, it writes
  `<MEMORY_ROOT>/loop-review/2026-11-02-value-ledger-2026-W45.md` whose five fields read as §4 "The
  snapshot" states; `--dry-run --key 2026-W45` leaves `git status --porcelain` empty; `--dry-run --key
  ../x` and `--dry-run --key 2026-W4` each exit 2 naming the key, writing nothing; `--key 2026-W45`
  without `--dry-run` exits 2, and `price` with no `GOV_CADENCE_KEY` exits 2 printing `refused: no key`,
  each writing nothing.
  Red when: a malformed key reaches a path, a dry run writes, or `--key` writes outside `--dry-run`.
- **AC6** — When `grep -n -A8 'name = "review.loop.catch-source"' tools/policy/catalogue.toml` runs, it
  shows `summary` and `usage`; `grep -cx 'review.loop.catch-source' tools/policy/unsummarised-keys.txt`
  prints `0`; `grep -n '"review.loop.catch-source"' loop_review.py` names S4's literal read.
  Red when: a field is missing, or the key is read through a variable.
- **AC7** — (amended, id 37) When `grep -n 'name = "value-ledger"' record-kinds.toml` and `grep -n
  'D:loop-review' tools/memory-tree/check-memory-hygiene.sh` run, each prints one line, and the second
  sits inside check 3's sanctioned `case` arm.
  Red when: either line is absent, so a tracked snapshot reds check 3 as an unsanctioned directory.
- **AC8** — When `python loop_lib.py --check` runs over the tree, it refuses no row, and
  `grep -n 'item.loop.price' loop.toml` prints the row's tag line.
  Red when: the row's route names an undeclared item.
  permission: `loop_lib.py` is TOOL-dDeclaredLoop-12's, built before this unit's build run.
- **AC9** — (amended, id 39) When `grep -n 'review.loop.catch-source' loop-review.md` runs, it prints the section's
  line naming both values; `grep -n 'loop-review.md' help/README.md` prints the index line.
  Red when: the page or its index line is absent.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `memory-hygiene self-test` · `build-index selftest` · `policy check` · `policy fixtures` · `docs` · `lexicon naming predicates` · `check-wiring self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `codebase-map coverage + freshness`

The pass adds the leg `loop-review selftest` (S11), which the manifest does not hold at base, so it is
named here and not on the line above.

New arm: tools/loop/loop_review.py · covers AC1 AC2 AC3 AC5 · its `--fixture` cases, staged red by a reader that counts a red-then-green row as a catch, a source switch that always reads flake records, a window that keeps every event, and a writer that takes the key unchecked · none
New arm: tools/memory-tree/library_views.py · covers AC4 · the three view cases under `gen_build_index.py`'s run of every fixture case, staged red by a renderer that reads the oldest snapshot and one that re-prices · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC7 · a fixture tree holding `memory/loop-review/`, staged red by dropping `D:loop-review` from check 3's set · none

## 8. Open questions

- **F1 — Which unit creates `tools/loop/loop_review.py`?** The brief's S3 has unit 3 ship the module and
  unit 2 add `price` to it, while its build order puts this unit first (order 1) and unit 3 second. (a)
  This unit creates the module with `price` and `read_loop_policy`, unit 3 adds its verbs; (b) a second
  module for `price`, which splits one program into two; (c) reorder the build, which the brief fixes.
  (a) keeps the brief's one module and its order. Rung 3. RESOLVED (agent, 2026-11-02, delegated): (a),
  S1; unit 3's spec carries the mirror. widens: none · relaxes: none
- **F2 — Who writes the view, and from what?** The brief's S1 says the view is written only by `price`,
  which regenerates it. (a) `price` writes a dated snapshot and the library-view host renders the view
  from the newest tracked snapshot, one writer per file; (b) `price` writes the view, which the host
  would then re-render from live sources and red on any other node; (c) `price` writes the view and the
  row is not a `VIEWS` row, so nothing checks it. (a) keeps the view derived and checked both ways and
  keeps each Loop Review's priced snapshot (layer-expansions:80) as a record of its own, cited by unit
  3's record. Rung 3. RESOLVED (agent, 2026-11-02, delegated): (a), S6 and S7. widens: none · relaxes:
  none
- **F3 — Which row kind carries the catches this unit reads?** The brief lists providers for `shape`,
  `probe`, `item` and `cap` only, while both catch sources attribute their events to legs. (a) This unit
  adds `kind=leg`, cost from the ceiling evidence; (b) no leg rows, so every catch the source reads joins
  nothing and AC1 and AC2 could not be observed; (c) a later unit adds legs. (a) is the only option that
  observes the clause's own sources and closes gap-maint-03's leg half. Rung 3. RESOLVED (agent,
  2026-11-02, delegated): (a), S3. widens: none · relaxes: none
- **F4 — Where is the view armed?** TOOL-dLinkedLibrary-6 S2 arms views in `LIBRARY_VIEWS` of
  `.memory-tree.conf`, and TOOL-dLinkedLibrary-52 S26 moves that set to the catalogue key
  `memory.library-views`; both are unbuilt at base. (a) Name `value-ledger` in whichever home the landed
  reader reads, the build run re-grounding on dLinkedLibrary's state; (b) pin `.memory-tree.conf`, which
  S26 empties. Rung 1: the parent specs state the order. RESOLVED (agent, 2026-11-02, delegated): (a),
  S7. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft.
- rev-2 · 2026-11-02 · §3 §4 §5 §7 S4 S6 S8 S9 S11 S12 AC7 AC9 · amended at the disposal of the
  round-1 spec audit `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4
  "Amendments (round-1 spec audit)": ids 1 (`TOOL-dCalibratedLens-19`), 36
  (`TOOL-dCalibratedLens-20`), 48 (`TOOL-dCalibratedLens-26`), and 27, 9, 12, 37, 38, 39, 42, 26 and
  24 (`TOOL-dCalibratedLens-30`); §3 gains the hands-offs to units 19, 20, 26 and 30, and the
  hands-off to unit 4 now names `PROVIDERS` (id 5).
- rev-3 · 2026-11-02 · §3 §4 · amended at the disposal of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`, §4 "Amendments (round-2 spec audit)": r2 id
  17 (`TOOL-dCalibratedLens-41`), the docs-mode rule of id 48's observation; §3 gains the hands-off to
  unit 41.
- rev-4 · 2026-11-03 · §3 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`: §3's hands-off of the row's guard names
  `TOOL-dCalibratedLens-46` in place of unit 41, which takes the widening into the leg's declaration
  (r3 id 22).
- rev-5 · 2026-11-03 · S5 §3 §4 AC1 AC2 AC3 AC5 · re-grounded against the parents' specs, `--key`
  admitted only with `--dry-run` and no key refused `refused: no key` (TOOL-dTendedCadence-1 S3, AC3),
  and §4 "The snapshot" naming unit 3 §8 F2's ask as the only source of the monthly and `n<k>` forms,
  by the brief prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md (cross-check rows
  25, 26)
- rev-6 · 2026-11-03 · §2 S9 §4 · re-grounded against dTotalRecall's and dDeclaredLoop's specs, S9's
  row gains `inputs`, `allowance` and `witness`, id 26 names TOOL-dDeclaredLoop-110, the leg's claim
  moves to `loop.md`, `value-ledger` binds through `RECORD_KIND_TOKENS`, and unit 3 S8 drops
  `unarmed`, by the brief prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground.md
  (cross-check rows 11, 13, 14, 16, 20)

## 10. Reuse audit

The seams extended: the library-view seam of TOOL-dLinkedLibrary-6 (`VIEWS`, `render_library_views`
and its host in `gen_build_index.py`, `cmd_check` at `:2879` and `cmd_write` at `:3201` at this base,
where that spec cites `:2865` and `:3187`); the record-kind registry of TOOL-dTotalRecall-1; the loop
definition of TOOL-dDeclaredLoop-12; `runlog.py journal --producer gates` (`tools/runlog/runlog.py:151`);
`tools/run-gates/ceiling-evidence.txt`, the tracked per-leg cost; the flake record of
TOOL-dWitnessedBar-8 S3; the atomic contained write of `write_record`
(`tools/runlog/record.py:1179-1201`); the inline `resolve_kit_dir` block; and the policy route of
TOOL-dTendedCadence-6 S1. The probe `python tools/codebase-map/reuse_lookup.py "price each gate leg by
its cost and the reds it caught in a window, rendered as a generated table"` ranked name-stem matches
only (`legs`, `leg`, `resolve_generated_indexes`, `derive_window` in `tools/runlog/model.py`, a run
window and not a catch window), so no existing seam fits the ledger itself, and it is new over the seams
above. Where the scout's reading and source disagree at this base: the `trace.cost` row is at
`catalogue.toml:1601-1605`, as the brief says, and the four `review.loop.*` rows open one line before
the `name` lines a grep prints (`:1283`, `:1289`, `:1295`, `:1302`). The flake record's field reader is
the `FIELD` grammar of `tools/memory-tree/deviation_join.py:150`, carried inline because a kit imports
no sibling.

Recall terms used: `python tools/memory-recall/query.py "how is a gate leg priced by its catches and
cost, and how does a periodic loop review retire what catches nothing" --terms "value ledger loop review
catches false reds window retire price leg cadence lease snapshot"`
