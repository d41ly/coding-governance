# TOOL-dTendedCadence-17 — the interpreter floor's end-of-life reading, filing an intake six months before it as `maintain.interpreter-eol` says

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 13 · advances TOOL-dTendedCadence-19

**Carries:** cl-dClosedLoop-0457@2214ebfb whole

**Carries:** node:policy-key.maintain.interpreter-eol

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 |
| [2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-18 |
| [2026-11-01-build-TOOL-dTendedCadence-5-reuse-scout-c.md](../build/2026-11-01-build-TOOL-dTendedCadence-5-reuse-scout-c.md) | research | TOOL-dTendedCadence-5 TOOL-dTendedCadence-7 TOOL-dTendedCadence-12 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-18 |
| [2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-1 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-18 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing watches the interpreter floor's end of life, so the next floor raise is discovered rather
than planned (gap-maint-15, gap-register:434; the owner's AP-35, away-pass:327 and :458). This unit
adds the end-of-life table beside the floor declaration and a Maintain reading over the two that, as
`maintain.interpreter-eol` says, files an intake six months before the floor's end of life (`file`),
warns in the maintenance record and files nothing (`warn`), or reads nothing (`off`).

## 2. Scope (IN)

Build-run preconditions, each specced and DEFERRED at this base: TOOL-dSafePassage-11 S1, the floor
declaration `tools/lib/python-floor.txt` and its reader `read_floor` in `tools/lib/python_floor.py`
(neither exists at `f4597719`: `git log --oneline -3 -- tools/lib/` shows dGroundRules' commits only);
TOOL-dWellOiledMachine-27 S1, the filer `tools/runtime/intake.py file --origin cadence --filer <item
tag>`; TOOL-dTotalRecall-1 S1 and -18, `tools/memory-tree/record-kinds.toml` with its `layer`
column; and this build's
TOOL-dTendedCadence-1 (`maintain.read`, which routes an `act` reading to `item.maintain.file`), -8
(the `[[reading]]` row, I3, and the offender key, I5), -4 (admission, and `read_policy_value`, drift-audit's one policy adapter, S6), -14 (`edges`, I8) and -15
(`item.maintain.file`'s `run_breach_route` and `write_breach_ask`).

- **S1** — The end-of-life table, `tools/lib/python-eol.tsv`, beside the floor declaration and not
  inside it, since TOOL-dSafePassage-11 S1 has `read_floor` refuse any content but `<major>.<minor>`.
  Its `#` lines name the source (devguide.python.org/versions, as research-python-floor.md:55 cites
  it) and the date it was read; each other line is `<major>.<minor>` TAB `<YYYY-MM>`. Seeded with
  the six rows of research-python-floor.md:57-64, `3.10` to `3.15`, PINNED as read on 2026-10-18:
  `3.10 2026-10`, `3.11 2027-10`, `3.12 2028-10`, `3.13 2029-10`, `3.14 2030-10`, `3.15 2031-10`.
  Observed by AC1.
- **S2** — The table's reader, `read_floor_eol(root)` in `tools/lib/python_floor.py`, beside
  `read_floor`: it returns `{(major, minor): (year, month)}`, skips `#` and blank lines, and refuses,
  naming `python-eol.tsv:<line>`, a row of any other shape, a month outside `01`..`12` and a version
  listed twice. The module's CLI gains the verb `eol`: `python python_floor.py eol` prints the
  floor's row, `3.15<TAB>2031-10`, exit 0; exit 1 printing `eol — <floor> has no row` when the table
  lacks the floor; exit 2 on a refusal. Observed by AC1.
- **S3** — The reading, `measure_interpreter_eol(root, today)` in a new
  `tools/drift-audit/interpreter_eol.py`, returning drift-audit's record shape unchanged (I4:
  `signal`, `value`, `of`, `tolerance`, `gateable`, `live`, `unjudgeable`, `detail`, and
  `not_asked` where `_build_not_asked` would set it, `tools/drift-audit/drift_report.py:1238`). Its
  signal is `interpreter_floor_near_end_of_life`. It loads `python_floor.py` by path from
  `<prefix>/lib/`, the kit's own parent's `lib` directory, and calls `read_floor(root)` and
  `read_floor_eol(root)` on the tree it is given. The window opens on the first day of the month six calendar months before the
  end-of-life month, `derive_eol_window(year, month)`: 2031-10 opens on 2031-04-01. `value` is 1 when
  `today` is on or after that day and 0 before it, `of` 1, `tolerance` 0, `gateable` False, `live`
  True, and `detail` one row `{"floor": "3.15", "end-of-life": "2031-10", "window-opens":
  "2031-04-01"}` when `value` is 1, else empty. No floor module or no `python-floor.txt` in that tree is
  `not asked: no interpreter floor is declared in this tree`; a table that is absent, refused or holds no
  row for the floor is a dead probe, `live` False and `value` -1, its note naming which. Observed by
  AC2 and AC3.
- **S4** — The key, read through I2 at its one call site,
  `read_policy_value("maintain.interpreter-eol", root)` (TOOL-dTendedCadence-4 S6), the key first as a string literal. Its allowed values and default are the
  catalogue row's, verbatim: `file`, `warn`, `off`, default `file` (`tools/policy/catalogue.toml:1187-1191`).
  `file` returns S3's record, so under `maintain.interpreter-eol: file` a reading at 1 files through
  `item.maintain.file`'s ask (TOOL-dTendedCadence-15, the row's `route = "ask"`, S8 and S11). `warn` returns S3's record where `value` is 0 and, where it is 1, a `not
  asked` record whose note is `warn — Python <floor> reaches its end of life in <YYYY-MM>; the window
  opened <date>; maintain.interpreter-eol: warn files nothing` (§8 F2). `off` returns `not asked:
  maintain.interpreter-eol: off` and reads neither file. A refused read takes I2's answer, the
  default `file` with its `NOTE:` line. Observed by AC4 and AC5.
- **S5** — The module's CLI, `python interpreter_eol.py [--root <dir>] [--today <date>]`,
  prints one line, `<signal> <value> of <of> · <state>`, the state `ok`, `over`, `not asked: <why>`
  or `dead probe: <why>` (the line TOOL-dMindYourWords-16 S2 spells and I12 carries), and exits 0;
  `--json` prints the record instead. `--root` defaults to the working directory and `--today`, an ISO
  date such as `2026-11-01`, to the local date; exit 2 on usage. A reading reports and never gates, so no exit reflects `over`.
  Observed by AC2, AC3 and AC4.
- **S6** — The registration. One `[[reading]]` row (I3) in `tools/drift-audit/kit.toml`: `name =
  "interpreter_floor_near_end_of_life"`, `layer = "layer.observability"`, `scope = "repo"`, `kind =
  "interpreter-floor"` (S7), no `fix`, `events = []`,
  `route = "ask"` (S11, §8 F1) and `edges = [0, 0]` beside its pin, as TOOL-dTendedCadence-14 S1 settles
  them. Its pin is 0, the record's `tolerance` 0 as TOOL-dTendedCadence-4 §8 F1 states, and it takes no
  `drift-pins.txt` entry, since a ledger row's count is a positive integer and a pin of 0 has no row
  (TOOL-dTendedCadence-34); so under `maintain.tiers: bands` a value of 1 is in the act band and under `pins` it is over its pin.
  The registry reader TOOL-dTendedCadence-8 makes of `SIGNALS` (`drift_report.py:3521`) reaches
  `measure_interpreter_eol` by the row's `name`, passing the run's root and date. drift-audit's README
  signal table (`tools/drift-audit/README.md`, `## The signals`) gains the row, since
  `read_signal_table_names` (`tools/drift-audit/drift_signals.py:215`) compares that table with the
  engine's names. Observed by AC6.
- **S7** — The owner, derived and never typed. A `[[record-kind]]` row `interpreter-floor` in
  `tools/memory-tree/record-kinds.toml` (TOOL-dTotalRecall-1 S1's columns): `tag =
  "record.interpreter-floor"`, `layer = "layer.runtime"`, `home = "<prefix>/lib/python-floor.txt"`,
  `schema` form `rows`, `writer` TOOL-dSafePassage-11's `write_floor`, `lifecycle =
  "current-state"`, `check` the resolver leg `python resolver (behaviour + inline parity + idiom
  ban)`, `readers` naming `interpreter_eol.py`. Unit 4's admission derives the reading's owner,
  Runtime, from it (§8 F3). Observed by AC6.
- **S8** — The filing. `maintain.read` hands the `act` reading to `item.maintain.file` as a breach
  (TOOL-dTendedCadence-1 S4), and `route = "ask"` files it through `write_breach_ask`
  (TOOL-dTendedCadence-15 S2) whatever `maintain.on-breach` holds: `intake.py file --origin cadence
  --filer item.maintain.file`, its text naming the floor, its end-of-life month and the window's first
  day, its acceptance the reading back under its pin for this offender, keyed by (reading, offender
  key) with the offender key `<signal>	<detail key>` as `render_drift_offenders` spells it
  (`drift_report.py:3985`, I5); a second period's reading of the same floor adds a `seen` clause to
  the open ask and files no second one. A `cadence` receipt never ratifies (TOOL-dWellOiledMachine-27
  S3), so Entry places the intake as an `ask` (its S4) and `triage.py pass` sets its level: the owner
  plans the raise, which is TOOL-dSafePassage-11's upgrade-step kind. A dead probe past
  `maintain.dead-after` readings is filed to its source through `maintain.file`
  (layer-expansions:223). Observed by AC7.
- **S9** — The catalogue row's missing fields, and its name drained. The `maintain.interpreter-eol`
  row gains `summary = "What the interpreter floor's end-of-life reading does once the floor is
  within six months of its end of life: file an intake for the raise, warn in the maintenance record,
  or read nothing."` and `usage = 'maintain.interpreter-eol = "warn"'`; `python
  tools/policy/policy.py lists --write` then re-renders `tools/policy/unsummarised-keys.txt` without the name
  (`:116`). No second row. Observed by AC8.
- **S10** — The docs: `help/maintain.md`, the Maintain page, gains the section `## The interpreter
  floor's end of life`, naming the table, the reading, the window, each value of the key and where
  the intake goes, creating the page where no earlier unit of this build has. Observed by AC9.
- **S11** — The row field `route`, its first value. The `[[reading]]` row reader
  (TOOL-dTendedCadence-8, I3) admits one optional key, `route`, its one value here `ask`, and refuses
  any other value naming the row; TOOL-dTendedCadence-9 adds `patch`. `run_breach_route`
  (`tools/drift-audit/maintain_file.py`, TOOL-dTendedCadence-15 S1) sends a breach whose reading
  declares `route = "ask"` to `write_breach_ask` under every value of `maintain.on-breach`, its route
  `filed`, `seen` or `pending` and never `held` or `reported`, so no `over-pin:` line the red leg
  counts (TOOL-dTendedCadence-15 S3, S4) ever names it. A row with no `route` is routed as before.
  Observed by AC7 and AC10.

## 3. Non-goals (OUT)

- Raising the floor. The raise is an upgrade step (TOOL-dSafePassage-11's kind, its `write_floor`),
  built by the patch build the owner places; the reading files and never edits.
- The floor's declaration, its reader and the resolver's refusal below it: TOOL-dSafePassage-11 S1,
  S2, called.
- A floor in a copy-installed adopter. `<prefix>/lib/` is gov-internal and ships nothing
  (`tools/lib/compare_base.py:3`), so an adopter's tree holds no `python-floor.txt` and the reading is
  `not asked` there. The floor is gov's to raise, and an adopter receives the raise as a kit update.
- Refreshing the table from the network. A new Python release adds a row by hand; an absent row for
  the floor is a dead probe Maintain files to its source, so a stale table is visible.
- The reading registry, admission, bands and `maintain.file`'s ask: TOOL-dTendedCadence-8, -4, -14
  and -15, cited; S11 adds one key to the row and one branch to the route, nothing else of either.

### Edges

- **consumes-from** `TOOL-dTendedCadence-8` — the `[[reading]]` row (I3) S6 declares and S11 adds the key `route` to, and the offender key (I5) S8 files under; without them nothing runs the reading
- **consumes-from** `TOOL-dTendedCadence-15` — `item.maintain.file`: `run_breach_route`, which S11 gives its `route = "ask"` branch, `write_breach_ask`, which S8 files through
- **consumes-from** `TOOL-dTendedCadence-4` — `read_policy_value`, drift-audit's one policy adapter, which S4 reads the key through
- **hands-off** `TOOL-dTendedCadence-16` — `route`, the row key S11 adds, whose value `ask` that unit's four readings declare
- **hands-off** `TOOL-dTendedCadence-9` — `route`, the row key S11 adds, to which that unit adds the value `patch`
- **consumes-from** external — TOOL-dSafePassage-11 S1 (`python-floor.txt`, `read_floor`), TOOL-dWellOiledMachine-27 S1 (`intake.py file`), TOOL-dTotalRecall-1 S1 and -18 (`record-kinds.toml`, its `layer` column)
- **hands-off** `TOOL-dTendedCadence-38` — the `route` key S11 adds, which that unit makes unit 8's closed set and whose AC10 case it re-states (review id 4)
- **hands-off** `TOOL-dTendedCadence-48` — the recurrence observation, the refused read and the route citation, which the minors batch repairs (review ids 9, 20, 49)

## 4. Design

### Evidence

No floor is declared at this base: the only interpreter-version gates in source are `>= (3, 12)`
rmtree shims (`tools/policy/check_policy.py:4457`), and `resolve_python`
(`tools/lib/resolve-python.sh:24-54`) runs each candidate without a version test. The end-of-life
dates live only in research-python-floor.md:57-64. TOOL-dSafePassage-11 S1 declares the floor
`3.15` and its reader refuses anything but `<major>.<minor>`, which is why the dates need a file of
their own (scout C, interface 10). The key's row exists (`catalogue.toml:1187-1191`) with no summary
(`unsummarised-keys.txt:116`).

### The window

```
window_opens(EOL year Y, month M) = the first day of month M-6 of year Y, borrowing a year when M <= 6
3.11 -> 2027-10 -> 2027-04-01        3.15 -> 2031-10 -> 2031-04-01
```

The table holds months, as the devguide publishes them, so the window is a month boundary and the
reading's answer for a date never depends on the day the end of life falls.

### Inventory

Names this unit mints, each asked of `python tools/lexicon/lexicon.py --suggest <name> --as
py.function` at this base and answered OK: `read_floor_eol`, `measure_interpreter_eol`,
`derive_eol_window`. The `py.file` cell is undeclared at this base (`.lexicon.conf:568-578` declares
function and type cells only), so the module name `interpreter_eol.py` and the table name
`python-eol.tsv` are graded by nothing. Also minted: the signal `interpreter_floor_near_end_of_life`,
the record kind `interpreter-floor`, the `eol` verb of `python_floor.py`, and the row field `route`
(S11, §8 F1), a key of I3, TOOL-dTendedCadence-8's row, that this unit adds.

### Files touched (estimate)

- `tools/lib/python-eol.tsv` (new)
- `tools/lib/python_floor.py` (TOOL-dSafePassage-11's module: `read_floor_eol`, the `eol` verb)
- `tools/lib/resolve-python.test.sh` (the floor module's arms live in this suite, TOOL-dSafePassage-11 §7)
- `tools/drift-audit/interpreter_eol.py` (new)
- `tools/drift-audit/drift_report.py` (the registry reader reaching the reading by name, and admitting `route`)
- `tools/drift-audit/maintain_file.py` (TOOL-dTendedCadence-15's: the `route = "ask"` branch of `run_breach_route`)
- `tools/drift-audit/kit.toml` (the `[[reading]]` row)
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `tools/memory-tree/record-kinds.toml` (the `interpreter-floor` row)
- `tools/policy/catalogue.toml` (the row's `summary` and `usage`)
- `tools/policy/unsummarised-keys.txt` (rendered by `policy.py lists --write`, never edited)
- `help/maintain.md`

### Alternatives rejected

- **The dates inside `python-floor.txt`.** Rejected by TOOL-dSafePassage-11 S1: `read_floor` refuses
  any content but `<major>.<minor>`, and its parity population copies that file's value into every
  resolver block.
- **The table inline in the reading.** Rejected: the table is data the floor raise reads beside the
  floor, and a constant in an observability kit puts a core fact in an expansion
  (`memory/gotchas/core-depends-on-an-optional-part.md`).
- **An inline copy of `read_floor` in drift-audit.** Rejected: the copy would only ever run where
  `<prefix>/lib/` exists, gov's own tree, and there the canonical module is on disk; a copy is a
  second parser of one file.
- **Leaving the route to `maintain.on-breach`.** Rejected by §8 F1's test: under `red-leg` a floor six
  months from its end of life reds every bar, and under `report` nothing is filed, so `file` would not
  file.

## 5. Production-readiness checklist

- security — the reading reads two tracked files and the date, and writes nothing; the intake text
  carries a version and two dates, no path outside the tree and no secret.
- perf / scale — two small files and one bounded policy subprocess per period.
- error / empty / loading states — no floor: `not asked`; no table, a refused table or no row for the
  floor: a dead probe, filed to its source past `maintain.dead-after`; a refused policy read: `not
  asked`, naming it.
- observability — the reading's line, its journal line (I9) and the maintenance record; the intake's
  receipt.
- risks — a hand-kept table goes stale at a new release; the floor's own row going missing is the dead
  probe that surfaces it.
- testing — the probes of §6; the arms of §7.
- migration — N/A: two new files, one new row in each of three registries, no data moved.
- user docs — `help/maintain.md` (S10).

## 6. Acceptance criteria

The floor fixture is a scratch git repository under `%TEMP%` with a short name, holding a copy of
gov's `tools/` at the build run's tip with `lib/python-floor.txt` reading `3.15`, `lib/python-eol.tsv`
as S1 seeds it and a `main` branch carrying one commit. Each command runs with the fixture as its
working directory, its modules addressed under the fixture's `tools/`.

- **AC1** — When `python python_floor.py eol` runs in the floor fixture, it prints `3.15<TAB>2031-10`
  and exits 0; with the `3.15` row's month planted as `13` it exits 2 naming `python-eol.tsv:<line>`,
  and with the row removed it exits 1 printing `eol — 3.15 has no row`.
  Red when: a month outside `01`..`12` parses, or a missing floor row reads as a date.
- **AC2** — When `python interpreter_eol.py --today 2031-03-31` runs in the floor fixture, it prints
  `interpreter_floor_near_end_of_life 0 of 1 · ok`; with `--today 2031-04-01` it prints `1 of 1 ·
  over`, and `--json` shows the detail row naming `3.15`, `2031-10` and `2031-04-01`.
  Red when: the window opens on any day but the first of the sixth month before the end of life.
- **AC3** — When `python interpreter_eol.py --today 2031-04-01` runs in the floor fixture with the
  `3.15` row removed from the table, it prints `dead probe:` naming the missing row; with
  `python-floor.txt` removed it prints `not asked: no interpreter floor is declared in this tree`.
  Red when: a floor with no table row reads `ok`, or a tree with no floor reads `dead probe`.
- **AC4** — When `python interpreter_eol.py --today 2031-04-01` runs in the floor fixture whose `main`
  commits `.governance/policy.toml` setting `maintain.interpreter-eol = "warn"`, it prints `not asked:
  warn — Python 3.15 reaches its end of life in 2031-10`; set to `"off"` it prints `not asked:
  maintain.interpreter-eol: off`; with no policy file, the default `file`, it prints `1 of 1 · over`.
  Red when: `warn` or `off` reads `over`, or the default reads `not asked`.
  fixture: the policy kit's `policy.py get` reads the landed revision, so each value is committed on
  `main` (`tools/policy/policy.py:472`).
- **AC5** — When `grep -cE 'read_policy_value\("maintain\.interpreter-eol", root\)' interpreter_eol.py`
  runs, it prints 1.
  Red when: the key reaches the reader through a variable, which no reader-coverage scan can see.
- **AC6** — When `grep -n "interpreter_floor_near_end_of_life" tools/drift-audit/kit.toml
  tools/drift-audit/README.md` runs, it finds the `[[reading]]` row carrying `route = "ask"`,
  `scope = "repo"` and `kind = "interpreter-floor"`, and the signal table's row; and `grep -n 'name =
  "interpreter-floor"' record-kinds.toml` finds the kind row with `layer = "layer.runtime"`.
  Red when: the row is missing a field S6 names, or the kind has no row, so admission refuses it.
- **AC7** — When the Maintain run (`python maintain.py`, I1) runs twice over the floor fixture with
  its clock at 2031-04-01 and `main` committing `maintain.on-breach = "red-leg"`, the first run writes
  one intake receipt `origin=cadence filer=item.maintain.file` whose text names `3.15`, `2031-10` and
  `2031-04-01`, the second adds one `seen` clause to its ask and writes no second receipt, and
  `python maintain_file.py leg` stays green over the record the run wrote; under `"report"` the ask
  is filed all the same.
  Red when: `red-leg` holds the offender or `report` files nothing, or a second period files a
  second intake.
  fixture: needs TOOL-dTendedCadence-1, -6, -8 and -15 and TOOL-dWellOiledMachine-27 built; before
  them AC2 and AC6 are the observation.
- **AC8** — When `grep -c "^maintain.interpreter-eol$" tools/policy/unsummarised-keys.txt` runs, it
  prints 0, and `grep -n -A6 'name = "maintain.interpreter-eol"' tools/policy/catalogue.toml` shows
  the row's `summary` and `usage`.
  Red when: the name stays listed, or a second row for the key appears.
- **AC9** — When `grep -n "maintain.interpreter-eol\|python-eol.tsv" maintain.md` runs in `help/`,
  each matches.
  Red when: the page omits the key or the table.
- **AC10** — When the row reader reads a planted `[[reading]]` row declaring `route = "file"`, it
  refuses naming the row and the value; a row declaring no `route` is read as before, and `python
  maintain_file.py route` given a breach of a `route = "ask"` reading under `maintain.on-breach =
  "red-leg"` prints `file — interpreter_floor_near_end_of_life · key <hash> · filed`.
  Red when: an unknown value is admitted, or `red-leg` prints `held` for a `route = "ask"` breach.
  fixture: needs TOOL-dTendedCadence-8 and -15 built.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `policy fixtures` · `policy check` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC2 AC3 AC4 AC10 · the floor fixture with the window's two edge dates, the floor's table row removed, the floor file removed and each value of the key committed on main, and a planted row with an unknown `route`, staged against a module absent at this base · none
New arm: tools/lib/resolve-python.test.sh · covers AC1 · a planted month 13, a duplicate version and a removed floor row in `python-eol.tsv` · none

What the arms do not check: that the table's dates are the devguide's, which only a person reading it
can; and the intake's placement at Entry, which is TOOL-dWellOiledMachine-27's arm.

## 8. Open questions

- **F1 — How does the reading's offender come to be filed as an intake whatever `maintain.on-breach`
  says?** (a) The row declares `route = "ask"`, an optional `[[reading]]` key S11 adds, and
  `run_breach_route` files such a breach through `write_breach_ask`, whose filing is the cadence
  intake `intake.py file --origin cadence --filer item.maintain.file` (TOOL-dTendedCadence-15 S2),
  under every value of `maintain.on-breach`; (b) `route = "patch"`, the offender handed to
  `item.maintain.patch`; (c) a seventh member of `maintain.fixes`, `raise floor`; (d) no `fix` and
  no key, so `maintain.on-breach` decides, as for any fixless reading (TOOL-dTendedCadence-7 S5).
  The test: under each, does `file` file an intake under every value of `maintain.on-breach`? (d)
  fails: `red-leg` files nothing and reds every bar for six months, `report` files nothing, so the
  clause's "filing an intake" fails, veto 1. (c) changes v2:1321's safe-fix set, whose six names I11
  fixes exactly, and a floor raise is not a fix Maintain may apply, veto 1. (b) files a patch
  intake, which Entry places as a patch of a terminal build (TOOL-dPlacedRequest-4 §4, the `patch`
  fact), and a floor raise patches no build, so the placement is refused. (a) files under every
  value and reuses the ask TOOL-dTendedCadence-15 already writes, as its hand-off to this unit names
  it. Rung 3, the most feature-rich survivor.
  RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none
- **F2 — What does `warn` do?** (a) A `not asked` record whose note is the warning, so the
  maintenance record and the reading's line carry it and nothing is routed or filed; (b) the
  ordinary breach route, `maintain.file` as `maintain.on-breach` says; (c) the log band, a journal
  line and a count. (b) fails: under `red-leg` a warning reds the bar and under `file-ask` it files,
  which is `file`'s answer by another door. (c) needs band edges that differ with the key's value,
  and edges are one registration per reading (I8). (a) files nothing, whatever the other keys hold,
  and keeps the warning in every place a reading is read. Rung 3.
  RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none
- **F3 — Which record kind, and so which owner, does the reading carry?** (a) A new
  `interpreter-floor` row in `record-kinds.toml` on `layer.runtime`, the layer whose resolver every
  node runs against the floor (TOOL-dSafePassage-11 S2) and whose node registry records each node's
  interpreters (TOOL-dWellOiledMachine-15 S1); (b) no kind, admitted under `report-unowned` only;
  (c) an existing kind. (b) is refused under the default `refuse-unowned`
  (`catalogue.toml:1157-1161`), so the reading would never file, veto 1. (c): no kind
  TOOL-dTotalRecall-1 S2 registers has the floor declaration among its rows. Rung 3.
  RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 38, 48); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended: TOOL-dSafePassage-11's floor module `tools/lib/python_floor.py`, which gains the
table's reader beside `read_floor`; drift-audit's record shape and its `not asked` builder
(`tools/drift-audit/drift_report.py:536-552`, `:1238`), reused unchanged; the `[[reading]]` row of
TOOL-dTendedCadence-8 (I3) and the ask TOOL-dTendedCadence-15's `write_breach_ask` files; the record-kind registry of TOOL-dTotalRecall-1
for the owner. The probe `python tools/codebase-map/reuse_lookup.py "file an intake months before
the interpreter floor reaches its end of life"` returned name-stem matches only (`before`,
`corpus_files`, `ask_filed_in`, `resolve_kit_file`), none of which reads a version or a date, so no
existing seam fits the reading itself and it is new over the seams above. Where scout C's record and
source disagree: its `resolve-python.sh:24-54` and `check_policy.py:4457` hold at this base; its
"no floor is declared anywhere" holds (`tools/lib/` has no `python-floor.txt`); its table rows match
research-python-floor.md:57-64.

Recall terms used: `python tools/memory-recall/query.py "how does Maintain watch the interpreter
floor's end of life and file an intake before it" --terms "interpreter floor end-of-life
python-floor read_floor maintain.interpreter-eol intake cadence reading AP-35 dSafePassage"`
