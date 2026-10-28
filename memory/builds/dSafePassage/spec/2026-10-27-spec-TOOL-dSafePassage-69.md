# TOOL-dSafePassage-69 — the floor step's down grades a rollback to the pin under the floor the pin's code needs, and a refused down's reason reaches the step's tail

**Status:** CLOSED · rev-2 · 2026-10-27 · node d · Tier-2 · base 60d90cb7 · streams tooling · order 7 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dSafePassage-69-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-69-ledger.md) | journal | — |
| [2026-10-27-prompt-TOOL-dSafePassage-69-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-69-1-spec-writer.md) | research | — |
| [2026-10-27-prompt-TOOL-dSafePassage-69-2-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-69-2-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dSafePassage-69-build-brief.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-69-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md) | research | TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-5 TOOL-dSafePassage-51 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |
| [2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-brief.md) | research | TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-8 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-13 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-46 TOOL-dSafePassage-50 TOOL-dSafePassage-57 TOOL-dSafePassage-58 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

A rollback to the pin passes the floor step's down whenever the code it restores runs under the
floor the pin really had. When the down refuses, its reason is in the step's `tail`, which is what
the walk, the leg and the operator read. A step that fails and writes nothing on stderr can no longer
stop a walk with an empty reason.

Every line cited below was read at the run branch's HEAD `dbd1d6b01`. The floor step is not on the
default branch yet: `upgrade_steps.py list` prints `lib/python-floor-3.15 · unlanded` against
`origin/main`, which is the pin `60d90cb7`. So the header's `base` is the run's merge base, as on
TOOL-dSafePassage-62 to -68, and the row is still editable (the `step-rows-frozen` leg grades landed
rows only).

## 2. Scope (IN)

- **S1** — The prior floor. The floor row's down in `tools/govkit/steps.toml:34` names `3.12`, not
  `3.11`: `["bash", "{gov}/lib/python-floor.sh", "down", "3.12", "{target}", "{to}"]`. The row's
  comment (`:23-30`) says why: the pin declared no floor, and its own code needs 3.12 (§4).
  Observed by AC1, AC5 and AC7.
- **S2** — The static mode honours the floor. In `check_down_floor`'s static branch
  (`tools/lib/python_floor.py:345-368`), the four PEP 701 shapes `_scan_pep701` finds (`:357`) are
  findings only when the restored floor is below 3.12, the version that made them legal. The module
  docstring's "WHAT THE STATIC MODE DOES NOT SEE" (`:22-24`) says so. Observed by AC2.
- **S3** — The down's report on stderr. `python_floor.py down` (`:403-422`) prints its mode line,
  each finding, its count line and its success lines on stderr, one stream, in today's order. The
  count line also names the first finding, so the walk's one persisted line names a cause:
  `python-floor down: <n> finding(s) under the floor <prior>, the first <path>:<line>: <what>;
  nothing was written`. The `check` verb keeps stdout. Observed by AC3.
- **S4** — The class, guarded at the one spawn. In `run_step_isolated`
  (`tools/govkit/upgrade_steps.py:1129-1130`), an `up` or a `down` that exits non-zero with
  nothing but whitespace on stderr gets a one-line `tail`:
  `<id> <phase>: exit <rc> with nothing on stderr, where a step writes its failure; stdout's last
  line: <line or (none)>`. Every other result keeps stderr's last 20 lines, as today. Observed by
  AC4.
- **S5** — The arms. `tools/lib/resolve-python.test.sh` arm 1e (`:278-314`) gains three checks, and
  `check_step_isolation` in `tools/govkit/selftest.py` (`:3432`) gains one `[dSP-69]` check (§4 "The
  arms"). Observed by AC2, AC3 and AC4, which they re-observe.
- **S6** — The pages. `help/python-floor.md:72-81` names the down as `down 3.12`, says why 3.12, and
  says the down reports on stderr. `help/upgrade-steps.md`'s two stop lines (`:161`, `:240`) say
  what a stop reads when the step wrote nothing on stderr. Observed by AC6.

## 3. Non-goals (OUT)

- **The leg's summary arithmetic.** The measured `--case down` run printed
  `down -1 passed 2 red` (`scratchpad/down68.log:6`). The summary computes `n - k`
  (`tools/govkit/upgrade_walk.py:944`), and a case can count more reds than runs. It is a separate
  defect in a separate function, handed off below, and no criterion here reads that count.
- Deriving the prior floor from `<to>`'s own `python-floor.txt`. The first raise has nothing to
  derive from, since no commit before it carries the file, and a later raise's row names the floor
  it replaces by TOOL-dSafePassage-11's rule. Build it when a second raise lands.
- Rewriting `tools/memory-recall/check-recall.py:394` or any pin-era file. The pin is frozen, and
  this unit changes what the down asks of it.
- Gating the TOML 1.1 scan by the floor. 3.12's `tomllib` reads TOML 1.0, so `_scan_toml11` is
  right at the new value. A floor whose `tomllib` reads 1.1 is a later raise's question.
- Any change to the `check` verb, `write_floor`, `read_down_population`, or the population S11 of
  TOOL-dSafePassage-26 chose.
- The step contract's other argvs. §4 "The class" measured each one, and none needs an edit.

### Edges

- **consumes-from** `TOOL-dSafePassage-5` — the `upgrade-walk` leg and its `kill` and `down` cases, which AC5 and AC7 run; without them the rollback to the pin is observed only by hand
- **consumes-from** `TOOL-dSafePassage-11` — the floor row, `python-floor.sh down`, `python_floor.py`'s down and its static mode; without them there is no down to correct
- **consumes-from** `TOOL-dSafePassage-26` — S10's `{to}` and S11's population read at `<to>`, which is what makes the pin's own code the thing graded
- **hands-off** external — the leg's summary line, whose `n - k` printed `down -1 passed 2 red` on the measured `--case down` run (`tools/govkit/upgrade_walk.py:944`); recommended as its own unit

## 4. Design

### What was measured

PINNED 2026-10-27 on node `d` at HEAD `dbd1d6b01`, by read-only calls of `check_down_floor` with
target `.`, which grades gov's whole tracked `.py` and `.toml` set at `<to>`, 199 files at the pin.

| `<to>` | prior | mode | findings |
|---|---|---|---|
| pin `60d90cb7` | 3.10 | static | `tools/memory-recall/check-recall.py:394: a # in a replacement field` |
| pin `60d90cb7` | 3.11 | static | the same one |
| pin `60d90cb7` | 3.12 | interpreter (uv's CPython 3.12) | none |
| pin `60d90cb7` | 3.12 | static, interpreter stubbed out | the same one, which is S2's defect |
| pin `60d90cb7` | 3.12 | static, `_scan_pep701` stubbed out | none |
| `ed135af16^`, the raise's parent | 3.11 | static | that one, and `tools/govkit/upgrade_steps.py:2864: a backslash in a replacement field` |
| `ed135af16^` | 3.12 | interpreter | none |
| `ed135af16^` | 3.12 | static, `_scan_pep701` stubbed out | none |

The leg measured the same refusal twice. `--case kill --step lib/python-floor-3.15` stopped with
`the rollback's reverse walk stopped at lib/python-floor-3.15: down exit 1: .`
(`scratchpad/kill68-floor.log:4`, 369 s). The coordinator's `--case down` stopped the same way
(`scratchpad/down68.log:4`, 214 s), so a plain `update --rollback --to <pin>` meets it, not only a
killed walk. The empty text after `down exit 1:` is `tail`'s last line, and the down wrote its
finding on stdout, which `run_step_isolated` discards.

### The prior floor: 3.12, and why not the other option

The pin declared no floor. Its resolver imposed none: the pin's `tools/memory-tree/merge-rows.test.sh:352`
reads "`resolve_python` imposes NO version floor". The 3.11 in the row came from govkit's `tomllib`
guard (`tools/govkit/govkit.py:104-112` at the pin), which is one kit's import, not a floor the
tree's code was held to. The tree's code needed 3.12 from `9d41abb16` (2026-08-17), which added
`print(f"{'#':>3} ...")` at `check-recall.py:394`. TOOL-dSafePassage-11's ledger found that line and
`upgrade_steps.py:2864` on 2026-10-26
(`memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-11-ledger.md:59-66`) and left
them as out of its write set. TOOL-dSafePassage-26 S10 then pointed the down at `<to>`, so the pin's
own bytes became the graded population and the latent finding became a refused rollback.

So the step declares 3.12, the floor the pin's code measures. Raising the value never refuses a
`<to>` that 3.11 passed: `ast.parse` at a higher `feature_version` accepts more, S2 removes the PEP 701
shapes at 3.12, and 3.12 removed no syntax 3.11 accepted. An older `<to>` is UNVERIFIED beyond that
argument; the two `<to>` above are measured. An adopter can roll back only to a commit gov landed,
and the newest landed commit is the pin.

The other option was that the down stop grading findings that already stand at `<to>`. Since S10 the
gov-shipped population is read at `<to>`, so every gov-shipped finding already stands there, and the
option reduces the down to the target's `.governance/*.toml`. It is rejected. It drops a check that
three CLOSED criteria observe as live, TOOL-dSafePassage-11 AC6, TOOL-dSafePassage-26 AC9 and
TOOL-dSafePassage-35 AC19, each a PEP 701 plant at `<to>` under `down 3.11` that must refuse. It also
leaves `write_floor` restoring 3.11 into gov's tree over code that does not run there. S1 and S2 keep
all three criteria as written, since they call `down 3.11` directly.

### S2's gate

```
static branch, per .py file:
  ast.parse(data, rel, feature_version=feature)          # unchanged
  if feature < (3, 12):                                  # new: PEP 701 made these legal in 3.12
      found += [... for ln, what in _scan_pep701(data)]
```

The interpreter mode needs nothing: a real interpreter at the prior floor already accepts what its
own grammar accepts, as the 3.12 rows of the table show.

### S3's stream

`run_step_isolated` keeps stderr's last 20 lines as `tail` (`tools/govkit/upgrade_steps.py:1130`),
and the reverse walk persists only the last one, `down exit <rc>: <last line>` (`:1538`), which
`govkit update` prints after `the rollback's reverse walk stopped at <id>:`
(`tools/govkit/govkit.py:10946`). The whole down report moves to stderr, not only the findings,
because arm 1e captures `2>&1` and requires the output to begin with the mode line
(`tools/lib/resolve-python.test.sh:293-296`). Split across two streams, a block-buffered stdout
would land its mode line after the line-buffered stderr's findings and red that arm. The count line
names the first finding because it is the last line, and the last line is all the walk records.

### The class: a step whose failure text goes to stdout

The population is every argv of every declared step row, read by `upgrade_steps.py list`: 3 rows,
9 argvs, 3 programs. PINNED 2026-10-27 at HEAD `dbd1d6b01`. The walk reads a step's text only on an
`up` or a `down` that exits non-zero (`:1407`, `:1538`). A `witness` or `reverted` exit is a
verdict, and nothing reads its text.

| Program | Its non-zero exits | Where the text goes |
|---|---|---|
| `tools/govkit/steps/receipt_schema_4.py` | every refusal | stderr (`:85-99`) |
| `tools/govkit/steps/fanout_cap.py` | refusals, usage | stderr (`:219-225`); its witness's `not applied` exit 1 is on stdout (`:211-213`), a verdict |
| `tools/lib/python-floor.sh preflight` | below the floor | stderr, the resolver's refusal block (`tools/lib/resolve-python.sh:171`) |
| `tools/lib/python-floor.sh down` | a finding | **stdout** (`tools/lib/python_floor.py:410-416`), the one member |

The cheap predicate exists and sits where every caller routes through: `run_step_isolated` is the
step kind's one spawn, held there by the `callers` probe (`upgrade_steps.py:2067-2080`).
`phase in ("up", "down") and rc != 0 and not stderr.strip()` fires on the floor down today and on no
other member. It is a guard rather than a red gate, and it covers what a gate over gov's tree cannot
see: a step a later descriptor declares. Its response names the breach and carries stdout's last line,
so the stop is never empty again. Its arm is S5's `[dSP-69]` check.

**What it does not check.** A step that writes a misleading line on stderr. A failing step's stdout
beyond its last line. A `witness` or `reverted` that writes nothing, which is correct for a verdict.
A step that exits 0 having failed.

### The arms

```
resolve-python.test.sh, arm 1e, after the existing planted-f-string run (:296):
  out=$(bash python-floor.sh down 3.11 "$FD" <head> 2>/dev/null)
  [ -z "$out" ] || bad "the down printed on stdout, which the step's tail never reads"
  rerun with 2>&1 >/dev/null: the last line matches "1 finding(s) under the floor 3.11, the first planted.py:2: "
  a committed plant `v = f"{'#':>3}"` at <to>, graded by
    "$PY" -I -c 'import python_floor as pf; pf.resolve_floor_interpreter = lambda v: None;
                 print(pf.check_down_floor(<fd>, "3.12", <to>)); print(pf.check_down_floor(<fd>, "3.11", <to>))'
  the 3.12 grade carries no finding for the plant, and the 3.11 grade names it
selftest.py, check_step_isolation, after :3642:
  a git-initialised scratch target; argv ["python", "-c", "print('the reason'); raise SystemExit(3)"]
  check("[dSP-69] an up that fails with nothing on stderr stops with a tail naming that and its stdout",
        run_step_isolated(row, "up", target, GOV_ROOT)["tail"] names `fixture/x up`, `nothing on stderr`
        and `the reason`, and the same row's witness keeps tail "")
```

The static half calls `check_down_floor`, not the shell verb, because a passing shell down writes the
floor into the fixture. `GOV_ROOT` is `tools/govkit/selftest.py:70`. A target that is not a git
repository is refused before any spawn (`upgrade_steps.py:1113-1117`), and a `gov_root` without a
registry is refused by `derive_tool_root`, both measured while writing this spec.

### Inventory

Minted: no function, flag, conf key, gate leg, receipt field or policy key. One check label prefix,
`[dSP-69]`, and the new text of two output lines (S3's count line, S4's tail line).

### Migration

None. The row is unlanded, so its down is edited in place, not superseded by a new row.

### Rollout

Live at landing, at order 7.

### Files touched (estimate)

- `tools/govkit/steps.toml`
- `tools/lib/python_floor.py`
- `tools/govkit/upgrade_steps.py`
- `tools/lib/resolve-python.test.sh`
- `tools/govkit/selftest.py`
- `help/python-floor.md`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Grade only what the rollback does not restore from `<to>`.** Rejected above.
- **Only the findings to stderr.** The arm's mode-line-first check reds on interleaving (above).
- **Make `tail` stdout plus stderr for every step.** It changes what every caller of every phase
  reads, and a passing step's stdout would crowd a failure's lines out of the 20.
- **A static gate over the step programs' sources.** Whether a non-zero exit's text reaches stderr
  is not decidable from a grep, and it would miss a step a later descriptor declares. S4's guard sees
  every spawn.

## 5. Production-readiness checklist

- security: N/A — no write path, input or surface. S4's line repeats one line the step already
  printed, to the same reader of the same run.
- perf / scale: none; S2 removes a token scan at 3.12 and S4 adds one string test per spawn.
- error / empty / loading states: S4 is this unit's empty state: a failure with no stderr is named,
  never blank.
- observability: the walk's one persisted line names the first finding (S3) or the breach (S4).
- risks: a `<to>` older than the two measured is graded under 3.12 by argument only (§4).
- testing: S5's arms, and the leg's `kill` and `down` cases (AC5, AC7).
- migration: none.
- user docs: S6, `help/python-floor.md` and `help/upgrade-steps.md`.

## 6. Acceptance criteria

- **AC1** — When a `python -I -c` probe reads the floor row's `down` argv from
  `tools/govkit/steps.toml` with `tomllib`, takes its fourth element as the prior, and calls
  `check_down_floor` from `tools/lib/python_floor.py` with target `.`, that prior and `<to>`
  `60d90cb7`, it prints the prior `3.12` and the findings list `[]`.
  Red when: the row still names `3.11`, as at HEAD `dbd1d6b01`, where it prints `3.11` and the
  finding in `tools/memory-recall/check-recall.py` at line 394.
  cost: about a minute on a node that resolves a 3.12 interpreter, which compiles 199 files.
  figure: 199 files at the pin, PINNED 2026-10-27.
- **AC2** — When the same probe runs with `pf.resolve_floor_interpreter = lambda v: None` set first,
  so the grade is static, it prints `3.12 []`. With `'3.11'` in place of the row's value it prints a
  list naming `tools/memory-recall/check-recall.py` at line 394, a # in a replacement field.
  Red when: `_scan_pep701` runs at every floor, as at HEAD, where the static 3.12 grade names that
  line; or the gate drops the scan at every floor, and the 3.11 grade prints `[]`.
- **AC3** — When `python -I tools/lib/python_floor.py down 3.11 . 60d90cb7 2>/dev/null` runs, it
  prints nothing and exits 1. When it runs with `2>&1 >/dev/null`, it prints the mode line first, then
  the finding naming `tools/memory-recall/check-recall.py` at line 394, a # in a replacement field,
  then last a line beginning `python-floor down: 1 finding(s) under the floor 3.11, the first` and
  carrying that same finding.
  Red when: the report is on stdout, as at HEAD, where the first run prints three lines.
  permission: never run it with a prior the pin passes, since a down with no finding on gov's own
  tree writes the floor into the working tree.
- **AC4** — When `run_step_isolated` runs a row whose `up` argv is
  `["python", "-c", "print('the reason'); raise SystemExit(3)"]` over a `git init` scratch target
  with `gov_root` this checkout, it returns `verdict` `failed`, `rc` 3, and a one-line `tail` naming
  `fixture/x up`, `nothing on stderr` and `the reason`. The same row's `witness` returns `tail` `""`.
  Red when: the guard is absent, as at HEAD, where the `up` returns `tail` `""`; or it fires on a
  `witness`.
- **AC5** — When `python -I tools/govkit/upgrade_walk.py --case kill --step <id>` runs, with `<id>`
  the floor row's id, lib/python-floor-3.15, its output carries no line where `stopped at` names
  that id, and no `RED:` line.
  Red when: the floor down refuses the rollback to the pin, as in `scratchpad/kill68-floor.log:4`.
  cost: about 6 minutes, PINNED 2026-10-27 by that log's 369 s on node `d`.
  fixture: release-0, built by the leg from `tools/govkit/fixtures/release-0/pin.txt`.
- **AC6** — When `git grep -n -e "down 3.11" -e "under 3.11" -- help/python-floor.md` runs, it
  prints nothing, and `git grep -n -F "down 3.12" -- help/python-floor.md` prints the step's line.
  Red when: the page still describes the 3.11 down.
- **AC7** — When `python -I tools/govkit/upgrade_walk.py --case down` runs, its output carries no
  line where `stopped at` names the floor row's id, and no `RED:` line.
  Red when: the floor down refuses the rollback to the pin, as in `scratchpad/down68.log:4`.
  cost: about 4 minutes, PINNED 2026-10-27 by that log's 214 s on node `d`.
  fixture: release-0, as AC5. The summary's pass count is not read (§3).

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `python resolver (behaviour + inline parity + idiom ban)` · `upgrade-walk` · `step-rows-frozen` · `step-gate` · `docs` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lib/resolve-python.test.sh · covers AC2 AC3 · three checks in arm 1e, their failing case staged by a working copy whose `python_floor.py` keeps HEAD's stdout report and its ungated `_scan_pep701` · none
New arm: tools/govkit/selftest.py · covers AC4 · one `[dSP-69]` check in `check_step_isolation`, its failing case staged by a working copy whose `run_step_isolated` keeps HEAD's stderr-only `tail` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, from the main loop's floor-step kill case after
  TOOL-dSafePassage-68 and the coordinator's `--case down` run, by
  `2026-10-27-prompt-TOOL-dSafePassage-69-2-spec-writer.md`.
- rev-2 · 2026-10-27 · AC1 AC2 AC3 AC5 AC7 · the backticked tokens the spec-token join read as
  untracked paths reworded, the probe and the observations unchanged, at the coordinator's request.

## 10. Reuse audit

The seams extended: the floor row in `tools/govkit/steps.toml:23-39`; `check_down_floor`'s static
branch and `main`'s `down` verb in `tools/lib/python_floor.py`; the step kind's one spawn,
`run_step_isolated` in `tools/govkit/upgrade_steps.py:1096-1130`, so every walk, the reverse walk,
gov first and the leg inherit S4. The arms extend arm 1e of `tools/lib/resolve-python.test.sh` and
`check_step_isolation` in `tools/govkit/selftest.py`. `python tools/codebase-map/reuse_lookup.py "a
subprocess failure whose explanation went to stdout while the caller keeps only stderr's tail"` ranked
`read_stderr_tail` (`tools/unattended/unattended.sh`), which reads a log tail for the unattended kit
and is not on the step path, and found no stream-contract helper for step argvs. The recall probe
found the run's rescope line (`memory/builds/dSafePassage/RUN.md:281`) and
TOOL-dWitnessedBar-24's reuse scout, which recorded that `tools/lib/resolve-python.sh` had no floor
before the raise, the fact §4 rests on.

Recall terms used: `python tools/memory-recall/query.py "the floor step's down refuses a rollback because the restored code needs a newer python than the prior floor" --terms "python-floor down prior floor 3.11 3.12 PEP 701 check_down_floor static mode tail stderr stdout rollback pin"`
