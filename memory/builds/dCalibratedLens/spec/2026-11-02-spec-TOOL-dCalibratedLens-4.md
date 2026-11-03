# TOOL-dCalibratedLens-4 — the measured-value factory, and the `budgets.*` caps re-derived from evidence and review cost

**Status:** OPEN · rev-4 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 7 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0461@ea09b304 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-14 |

<!-- /gen:spec-records -->

## 1. Goal

A cap's value is the owner's, and nothing re-derives one from evidence (gap-review-03; P9, v2:887-891):
every `budgets.*` value sits where its legacy home put it. This unit ships the one measured-value
factory three clauses of this build share (`derive_measured_value`, the brief's S9), and uses it first:
the Loop Review measures each cap's subjects over its window, derives the cap a nearest-rank p90 of
that evidence would set, prices it with the review cost the value ledger already holds, and proposes
every movement to the owner through the guarded policy command, writing no policy value itself.

## 2. Scope (IN)

- **S1** — The factory, `tools/loop/measure.py` (new, the loop kit). `derive_measured_value(rows,
  field, min_rows)` takes a list of mappings and returns `Measured(value, n, skipped, refused)`: the
  nearest-rank p90 of the numeric `field` over the rows, the element at index `(9 * n + 9) // 10 - 1`
  of the sorted values, `n` the usable count. A row whose field is absent, a boolean, or not a
  non-negative number is skipped and counted in `skipped`, never read as zero. Below `min_rows` usable
  rows it returns `value = None` and `refused = "<n> of <min_rows> rows"`. It reads nothing and writes
  nothing. Observed by AC1.
- **S2** — The proposal, `render_measured_proposal(key, measured, current, repo)` in the same module:
  `hold` when the value equals `current`, `refused: <why>` when the factory refused, and otherwise
  `raise` or `lower` followed by the lines `python tools/loop/policy_edit.py propose <key> <value>`
  prints when run in `repo` as a bounded subprocess (TOOL-dDeclaredLoop-2 S4). That verb writes
  nothing and prints the row diff and the command that applies it; this function never calls `set`
  or `raise`. One line on stderr and the direction alone, with no command, when the subprocess fails
  or times out. Observed by AC2 and AC6.
- **S3** — The census verb, `python tools/policy/budgets.py census`: one row per `[[cap]]` row of
  `tools/policy/caps.toml` through `read_cap_census` (`tools/policy/budgets.py:112`), in file order,
  `<name>\t<class>\t<unit>\t<family>\t<home>`, the family flag spelled `true` or `false`; a census that
  refuses prints its refusal and exits 2, as `resolve` does. It is the loop kit's read of the cap
  population, since a kit imports no sibling. Observed by AC8.
- **S4** — (amended, ids 6, 32) The evidence, `read_cap_evidence(repo, cap, window_days, now)` in `measure.py`, for a cap
  whose census `home` opens `limits:`. A measured-file cap (its name a tracked path) gives one row per
  first-parent commit of `HEAD` inside the window that changed the file, `{"bytes": <n>}`, `<n>` the
  blob's size counted without its CR bytes, as the template-size gate measures it. The class row
  `memory/builds/*/spec/` gives one row per (path, commit) for every path under a directory that glob
  matches. The window is `review.loop.window-days`, read through `policy.py get` (S8 of the brief).
  Every other home form returns no rows and the reason `no evidence source · <home form>`. Observed by
  AC3 and AC4.
- **S5** — The current value, read through `python tools/policy/budgets.py resolve <cap>` as a
  subprocess, its `<value>` and `<source>` columns (`budgets.py:389-391`), so the value is
  `resolve_caps`' answer (`budgets.py:206`) and never re-read from a home. A `-` value reads as
  unset. A refusal of the resolve prints its line and gives that cap `refused: resolve refused`.
  Observed by AC2.
- **S6** — (amended, id 5) The review cost: each cap's row of kind `cap` in the value ledger view
  `<MEMORY_ROOT>/views/value-ledger.md` (the brief's S1), its `cost` cell, read through the view's
  reader that TOOL-dCalibratedLens-2 ships, the rows TOOL-dCalibratedLens-15 provides. No view, or no
  row naming the cap, reads `cost searched-none`. The cost rides the proposal beside the derived value
  and never moves it (§8 F3). Observed by AC7.
- **S7** — (amended, ids 2, 6) The step, `derive_cap_readings(repo, now)` in `measure.py`, run by `loop_review.py gather` as one of
  its steps (the brief's S3), over every census row of class `switch` with `family = false`: a
  `consumer`, `correctness` or `exempt` cap is outside the switch and a family cap's value is per
  subject, so neither is a `budgets.*` value (`budgets.py:259-265`, `:346-348`). It returns one line
  per cap, `<cap> · <unit> · current <value> (<source>) · rows <n> · p90 <value> · <direction> · cost
  <cost>`, with S2's proposal lines beneath a `raise` or `lower`. Observed by AC2, AC3, AC4 and AC5.
- **S8** — (amended, ids 2, 3) The field: the `loop-review` record kind (the brief's S4, TOOL-dCalibratedLens-3) gains the
  field `caps`, the S7 lines of the period, written by `loop_review.py record`, so each review keeps
  the cap readings it proposed from. Each `raise` or `lower` line is a proposal keyed (`cap`, `<cap>`),
  which `loop_review.py file` files as it files every proposal (TOOL-dCalibratedLens-3). Observed by
  AC9.
- **S9** — (amended, id 42) The leg: one `[[gate_leg]]` row `loop measure fixtures` in `tools/loop/kit.toml`, running
  `python tools/loop/measure.py --fixture`, rendered into `tools/gate-legs.json` by
  `python tools/run-gates/leg_factory.py --write` (TOOL-dWitnessedBar-11 S1, S2), its `guard`
  `["{prefix}/loop/measure.py"]`; and `measure.py`'s `[[files]]` row in the same descriptor. Observed
  by AC10.
- **S10** — The docs: `help/size-caps.md` gains a section "Re-derived from evidence": which caps have
  an evidence reader, the window, the p90 and its 30-row floor, the review cost beside the value, and
  that every movement is a proposal the owner applies. Observed by AC11.

## 3. Non-goals (OUT)

- Writing any policy value. A raise through `check_raise_shape` (`tools/policy/guard.py:141`) and its
  `memory/DECISIONS.md` row stays the route of a build unit whose own change takes a measured file past
  its row, on the four conditions of `tools/template-size-limits.txt:16-24`; a Loop Review changes no
  subject, so it never meets condition 1 and only proposes (§8 F2).
- An evidence reader for a cap whose home is `conf:`, `file:` or `constant:`. Each such cap's subjects
  are its enforcer's own selection, and a glob typed into the census beside it would be one fact twice;
  those caps print `no evidence source` until a later unit gives the census a derived subject set.
- The `propose` verb of the Loop Review and its retirement proposals: TOOL-dCalibratedLens-5's. This
  unit's step runs at `gather`, sequenced before that verb exists (§8 F1).
- The value ledger, its `kind=cap` rows and how a breach is priced: TOOL-dCalibratedLens-2 and
  TOOL-dCalibratedLens-15. The policy command: TOOL-dDeclaredLoop-2.
- Build-run preconditions, each landed before this unit's build pass: TOOL-dDeclaredLoop-2 (the
  command `policy_edit.py` and its `propose` verb), TOOL-dWitnessedBar-11 (`leg_factory.py` and the
  `[[gate_leg]]` row), TOOL-dCalibratedLens-2, -3 and -15.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-3` — `tools/loop/loop_review.py`, its `gather`, `record` and `file` verbs and the `loop-review` record kind, which carry S7's step, S8's field and its proposals
- **consumes-from** `TOOL-dCalibratedLens-2` — `PROVIDERS`, the table whose `cap` entry S6 calls in-process for the period's cost (id 5)
- **consumes-from** `TOOL-dCalibratedLens-15` — the `kind=cap` rows of the value ledger, each breach priced by its bytes and its reads
- **hands-off** `TOOL-dCalibratedLens-6` — `derive_measured_value` and `render_measured_proposal` in `tools/loop/measure.py`, which each role's item budget derives and proposes through
- **hands-off** `TOOL-dCalibratedLens-16` — `derive_measured_value` and `render_measured_proposal` in `tools/loop/measure.py`, which the rework budget, the deadlines and the thresholds derive and propose through
- **consumes-from** external — TOOL-dDeclaredLoop-2's `policy_edit.py propose`; TOOL-dWitnessedBar-11's `leg_factory.py`; the policy kit's `budgets.py` and `policy.py get`, landed
- **hands-off** `TOOL-dCalibratedLens-21` — the caps step as a `METRICS` entry, whose lines that unit's `metrics-multi` plant writes (id 2)
- **hands-off** `TOOL-dCalibratedLens-30` — `derive_cap_readings` under the walk's window, which the minors batch's `at-year-back` arm runs (id 6)
- **hands-off** `TOOL-dCalibratedLens-46` — the `loop measure fixtures` row of S9, whose guard that unit widens, in the row's declaration, to the files the measure plants run (round-2 id 13, round-3 id 22)

## 4. Design

### Evidence

- No quantile helper exists under `tools/` at this base: `grep -rn "p90\|percentile\|nearest" tools
  --include=*.py` finds prose and `statistics.median` calls only. The p90s specced elsewhere stay
  their kits' own: `derive_estimate_hours` (TOOL-dWellOiledMachine-53 S3, `tools/runtime/ledgers.py`),
  the spend trend (TOOL-dWellOiledMachine-51 S3) and `tools/run-gates/derive-ceilings.py`; a kit
  imports no sibling (TOOL-dGroundRules-1 §4), so this factory is the loop kit's, for the three
  clauses of this build that need one (4, 6 and 16).
- The census holds 33 rows, 27 of class `switch`, 3 of them family caps, and 7 homes opening `limits:`
  (6 measured files and the class row `memory/builds/*/spec/`). PINNED: read from
  `tools/policy/caps.toml` at `8bec4cef`; the step derives its population from `census` on every run.
- The evidence volume: the six measured files changed between 8 and 78 times on `origin/main`'s
  first-parent history in the 60 days to 2026-11-02 (`AGENTS.md` 26,
  `coding-governance-agents.template.md` 17, `skills/session-kickoff/SKILL.md` 8,
  `memory/guides/BUILD-METHOD.md` 58, `memory/guides/UNATTENDED-PROTOCOL.md` 78,
  `.claude/skills/unattended/SKILL.md` 77), and spec files in 4,242 (path, commit) rows over 341 commits (id 20). PINNED, measured 2026-11-02 by
  `git log --first-parent --since="60 days ago"`. So at a 30-row floor three of the six refuse today.
- `budgets.py` refuses a value held in both homes (`budgets.py:288-289`), so a proposal for a cap
  whose source is its legacy home is applied by moving the value, which the command's printed row diff
  shows; this unit only reports `source`.

### The factory

```python
Measured = namedtuple("Measured", "value n skipped refused")

def derive_measured_value(rows, field, min_rows):
    vals, skipped = [], 0
    for r in rows:
        v = r.get(field)
        if isinstance(v, bool) or not isinstance(v, (int, float)) or v < 0:
            skipped += 1
            continue
        vals.append(v)
    n = len(vals)
    if n < min_rows:
        return Measured(None, n, skipped, f"{n} of {min_rows} rows")
    return Measured(sorted(vals)[(9 * n + 9) // 10 - 1], n, skipped, None)
```

`(9 * n + 9) // 10` is `ceil(0.9 * n)` in integers, the nearest rank, so 30 rows of 1 to 30 give 27
and 10 rows of 1 to 10 give 9. `min_rows` is the caller's: 30 for every caller in this build (§8 F4).

### The caps step, by example

```
caps — AGENTS.md · bytes · current 20480 (default) · rows 30 · p90 27000 · raise · cost 4433344B/212
  policy_edit.py propose budgets."AGENTS.md" 27000
  <the row diff and the command policy_edit.py prints>
caps — skills/session-kickoff/SKILL.md · bytes · current 18432 (default) · rows 8 · p90 - · refused: 8 of 30 rows · cost searched-none
caps — guide-bytes · bytes · current - (none) · rows 0 · p90 - · no evidence source · conf · cost searched-none
```

The key is spelled as `policy.py`'s `parse_key` reads it (`tools/policy/policy.py:533`): a name
carrying `/`, `.` or `*` is one quoted segment, `budgets."AGENTS.md"`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_measured_value`, `render_measured_proposal`, `read_cap_evidence`, `derive_cap_readings` | Python functions in `tools/loop/measure.py` | `py.function`, OK |
| `Measured` | namedtuple | none |
| `census` | CLI verb of `tools/policy/budgets.py` | none |
| `caps` | `loop-review` record field | none |
| `loop measure fixtures` | gate leg | none |
| `caps —` | output line | none |

Each function name was asked of `python tools/lexicon/lexicon.py --suggest <name>
--as py.function` and printed OK.

### Waits on

**Waits on:** TOOL-dDeclaredLoop-2 (`policy_edit.py propose`), TOOL-dWitnessedBar-11 (the leg factory),
TOOL-dCalibratedLens-2 (`PROVIDERS`, id 5), TOOL-dCalibratedLens-3 (the module, `gather`,
`record`, `file`, the record kind) and TOOL-dCalibratedLens-15 (the `kind=cap` rows).

### Migration

None: the leg, the verb and the field are new, and no policy value moves.

### Amendments (round-1 spec audit)

The round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Each bullet supersedes the text it
names; the unit it names owns the finding and its proof.

- **id 2 · S7, S8, AC9 (H3, `TOOL-dCalibratedLens-21`)** — The caps step is a `METRICS` entry `caps`
  answering one `(value, source)` pair per cap (TOOL-dCalibratedLens-3 S5 as amended), so the record
  carries one `caps:` Metrics line per cap; there is no `caps` field and the registry row is not
  edited. The proposal lines are not written into the record: they are the proposals of the next
  bullet. AC9 reads the `caps:` Metrics lines.
- **id 3 · S8, AC9 (H4, `TOOL-dCalibratedLens-22`)** — Each `raise` or `lower` is answered to the
  walk as
  `{"kind": "cap-value", "id": <cap>, "action": "raise"|"lower", "accept": "<the policy_edit.py set command S2 printed> applied by the owner, or <current> kept", "row": <the caps line>}`,
  and the walk files it (TOOL-dCalibratedLens-3 S7 as amended); AC9's proposal is keyed `cap-value`
  and `AGENTS.md`. `cap-value` keeps it apart from TOOL-dCalibratedLens-15's breach raise, keyed
  `cap`.
- **id 5 · S6, Edges, Waits on (M1, `TOOL-dCalibratedLens-30`)** — The cost is read in-process from
  `PROVIDERS["cap"]`, TOOL-dCalibratedLens-15's `derive_cap_rows` over its cached
  `read_cap_breaches`, in the same kit and the same walk, so it is the CURRENT period's cost; no
  reader of the view exists or is needed. A cap whose subject has no row reads `cost -`, the class
  row `memory/builds/*/spec/` among them; an unread provider reads `cost unread`. Waits on's "the
  ledger view and its reader" reads `PROVIDERS`.
- **id 32 · S4, S6 (M1, `TOOL-dCalibratedLens-30`)** — S4 takes the walk's window rather than
  re-reading `review.loop.window-days`, as the next bullet states, and S6's cost is the same
  period's.
- **id 6 · S4, S7 (M2, `TOOL-dCalibratedLens-30`)** — `read_cap_evidence(repo, cap, window)` and
  `derive_cap_readings(repo, window)` take the walk's `(start, end, days)` from `derive_loop_window`
  and read no policy value; a plant `caps-at` runs `gather --dry-run --at` a year before now and
  every evidence row falls inside that window.
- **id 9 · AC7 (M5, `TOOL-dCalibratedLens-30`)** — AC7's planted `cost` is `4433344B/212`,
  TOOL-dCalibratedLens-15's grammar, and the line ends `cost 4433344B/212` verbatim; with no `cap`
  row it ends `cost -`.
- **id 17 · AC2 (M7, `TOOL-dCalibratedLens-30`)** — AC2's fixture runs `git -c core.autocrlf=false`
  for every commit of the CRLF bodies and asserts that `git cat-file -s` of one planted blob exceeds
  its CR-stripped length before scoring, so the CR-counting break can fire on a node whose system
  config sets `core.autocrlf=true`.
- **id 42 · S9 (M22, `TOOL-dCalibratedLens-30`)** — The leg `loop measure fixtures` is claimed in
  `memory/map/features/loop-review.md` (TOOL-dCalibratedLens-2's id 42), its `subject` and `chunk`
  named on its row, `tools/govkit/subject-pins.tsv` regenerated, and a held leg's row added to
  `tools/run-gates/selftest-budgets.txt`.
- **id 20 · §4 Evidence, §5 (L5, `TOOL-dCalibratedLens-30`)** — Corrected in place: the class row's
  population is 4,242 (path, commit) rows over 341 commits at `8bec4cef`.
- **id 21 · §4 "The caps step, by example" (L6, `TOOL-dCalibratedLens-30`)** — Corrected in place:
  `guide-bytes` prints `current - (none)`, as `budgets.py resolve guide-bytes` answers.

### Files touched (estimate)

- `tools/loop/measure.py` — S1, S2, S4, S6, S7, the fixture (new)
- `tools/loop/loop_review.py` — S7's step in `gather`, S8's field in `record`
- `tools/loop/kit.toml` — S9's `[[gate_leg]]` and `[[files]]` rows
- `tools/gate-legs.json` — S9, the render of the leg row
- `tools/policy/budgets.py` — S3
- `tools/policy/check_policy.py` — S3's fixture case `budgets-census`
- `tools/policy/README.md` — S3's line under "The size caps"
- `help/size-caps.md` — S10
- `memory/map/features/loop-review.md`, `tools/govkit/subject-pins.tsv` and `tools/run-gates/selftest-budgets.txt` — the leg's claim, pin and budget (id 42)

### Alternatives rejected

- **The Loop Review raising a measured-file cap itself through `policy_edit.py raise`.** Its condition
  1 is the working tree's file over the old value because the unit's own change took it there
  (TOOL-dDeclaredLoop-2 §4; `tools/template-size-limits.txt:18`). A cadence run changes no subject, so
  the test is any review run: it has no unit and no change that crosses a row.
- **Review cost as a factor that scales the derived value.** No key declares a review-cost budget to
  scale against, so the factor would be a constant this unit invents (§8 F3).
- **The census read with `tomllib` in the loop kit.** A second parser of `caps.toml` beside
  `read_cap_census`, whose refusals (`budgets.py:136-147`) it would not share.

## 5. Production-readiness checklist

- security — the step writes no policy, decision or limits file; it reads git objects, two CLIs and a
  view, and runs `policy_edit.py propose`, a verb that writes nothing, with an argument list and a
  timeout. The command's own guard (TOOL-dDeclaredLoop-2 S1) is untouched.
- perf / scale — one `git log` per measured file and one per class row per run, and one `cat-file`
  per changed blob; 4,242 (path, commit) spec rows over 341 commits in 60 days are the largest population today (id 20), read in one
  `cat-file --batch`.
- error / empty / loading states — no view: `cost searched-none`; fewer than 30 rows: `refused`; a
  home the step cannot measure: `no evidence source`; a resolve or command failure: one stderr line,
  the cap still listed.
- observability — one `caps —` line per switch cap on every run, and the `caps` field in each
  review's record, so a cap that stops being re-derived is visible as a line, never as an absence.
- risks — a p90 near the current size proposes a cap with no headroom; that is the limits file's own
  rule for several rows, and the owner decides each proposal.
- testing — the fixture plants of §6, behind the new leg (§7).
- migration — none (§4).
- user docs — `help/size-caps.md` (S10).

## 6. Acceptance criteria

- **AC1** — When `python measure.py --fixture --plant factory` runs, it prints
  `derive_measured_value` returning 27 over rows 1 to 30 at `min_rows` 30, 9 over rows 1 to 10 at
  `min_rows` 10, `refused 29 of 30 rows` over rows 1 to 29, and `skipped 2` over 30 numeric rows plus
  one `true` and one `"12"`, the value still 27.
  Red when: a skipped row counts as zero, or the rank is taken as `int(0.9 * n)`.
  figure: every expected value is DERIVED by the nearest-rank rule over the planted rows.
- **AC2** — (amended, id 17) When `python measure.py --fixture --plant caps-raise` commits `AGENTS.md` 30
  times at 1000 to 30000 bytes with CRLF endings, and a limits row `AGENTS.md` at 20480, the step
  prints `caps — AGENTS.md · bytes · current 20480 (default) · rows 30 · p90 27000 · raise` and,
  beneath it, the output of `policy_edit.py propose budgets."AGENTS.md" 27000`; `caps-lower`, the row
  at 40000, prints `lower`; `caps-hold`, the row at 27000, prints `hold` and no command.
  Red when: the bytes count CRs, or a `hold` prints a command.
  fixture: a scratch repository under `%TEMP%` with a short name; the loop kit runs from the tree.
- **AC3** — When `python measure.py --fixture --plant caps-thin` commits `AGENTS.md` 29
  times, the step prints `rows 29 · p90 - · refused: 29 of 30 rows` and no command.
  Red when: a cap with too little evidence is proposed.
- **AC4** — When `python measure.py --fixture --plant caps-class` commits 30 changes across
  three files under `memory/builds/tX/spec/` and one under `memory/builds/tX/build/`, the
  `memory/builds/*/spec/` line prints `rows 30`; a commit outside the window `review.loop.window-days`
  names, planted at 61 days before `--now`, is not counted.
  Red when: a path outside the class glob or outside the window is a row.
- **AC5** — When the same fixture's step runs over the tree's census, it prints one `caps —` line per
  `switch` row whose family flag is `false`, a `conf:` cap's line ending `no evidence source · conf`,
  and no line for `orientation-card`, `cited-file-cap` or `line-length`.
  Red when: a cap outside the switch or a family cap gets a line, or a switch cap gets none.
  figure: the line count is DERIVED from `budgets.py census`.
- **AC6** — When `python measure.py --fixture --plant caps-raise` finishes, the scratch
  repository's `.governance/policy.toml`, `tools/template-size-limits.txt` and `memory/DECISIONS.md`
  hash as they did before the step, and `git status --porcelain` there prints nothing.
  Red when: a re-derivation writes the policy directly, the shape the recheck finding C5-F6 names.
- **AC7** — (amended, id 9) When `python measure.py --fixture --plant caps-cost` writes a value ledger view
  holding a `kind=cap` row for `AGENTS.md` with `cost` 5400, the line ends `cost 5400` and its p90 is
  the same 27000 as `caps-raise`; with no view the line ends `cost searched-none`.
  Red when: the cost changes the derived value, or a missing view reads as `cost 0`.
- **AC8** — When `python tools/policy/budgets.py census` runs on the tree, it prints as many rows as
  `grep -c '^\[\[cap\]\]' tools/policy/caps.toml` counts, the first
  `coding-governance-agents.template.md`, tab-separated, `switch`, `bytes`, `false`,
  `limits:coding-governance-agents.template.md`.
  Red when: a row is dropped, reordered or its family flag misspelt.
  figure: the row count is DERIVED by the `grep`.
- **AC9** — (amended, ids 2, 3) When `python measure.py --fixture --plant caps-record` runs `loop_review.py
  gather` and `record` in the scratch repository, the written `loop-review` record carries a `caps`
  field holding the step's lines, and `loop_review.py file --dry-run` names one proposal keyed `cap`
  and `AGENTS.md`.
  Red when: the field is absent or a `raise` line files no proposal.
  permission: `loop_review.py` is TOOL-dCalibratedLens-3's, built before this unit's pass.
- **AC10** — When `python leg_factory.py --check` runs after the pass, it exits 0, and
  `grep -n '"loop measure fixtures"' tools/gate-legs.json` names the rendered leg.
  Red when: the leg is edited into the manifest alone, so the factory's check reds.
- **AC11** — When `grep -n "Re-derived from evidence" help/size-caps.md` runs, it names the section.
  Red when: the section is absent.

## 7. Gates

`policy fixtures` · `policy check` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `docs` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `codebase-map coverage + freshness` · `recall floor`

New arm: tools/loop/measure.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC9 · the fixture plants, staged against a rank of `int(0.9 * n)`, a CR-counting measure, a step that writes `.governance/policy.toml`, and a cost that scales the value · none
New arm: tools/policy/check_policy.py · covers AC8 · the case `budgets-census`, staged against a census verb that drops the family flag · none

## 8. Open questions

- **F1 — The clause's re-derivation is `loop.propose`'s (layer-expansions:262, "and re-derives the
  caps"), and `propose` is TOOL-dCalibratedLens-5's at order 11, after this unit at order 7. Where does
  this unit's step run?** (a) A `gather` step writing the `caps` field, whose `raise` and `lower` lines
  are proposals `file` files; (b) the `propose` verb's cap arm, which needs unit 5 built first and so
  breaks the build order; (c) reorder this unit after unit 5, which moves the factory after its two
  callers' orders 8 and 9 as well. (a) keeps the order, needs no verb this build has not built, and
  gathers "surface size from git", which layer-expansions:260 already gives `gather`. Rung 3.
  RESOLVED (agent, 2026-11-02, delegated): (a). widens: none · relaxes: none
- **F2 — May the Loop Review raise a measured-file cap itself?** v2:1346 lets "a run" raise one "under
  the file's four conditions"; condition 1 is that unit's own change taking the subject past the row
  (`tools/template-size-limits.txt:18`), and `policy_edit.py raise` checks it as the working tree's
  file over the old value (TOOL-dDeclaredLoop-2 §4). A review run changes no subject. Rung 1, v2:1346
  read with the file it points at: no, every movement is proposed. RESOLVED (agent, 2026-11-02,
  delegated): propose only, through `policy_edit.py propose`. widens: none · relaxes: none
- **F3 — How does review cost enter a re-derived cap?** (a) Beside the value, on the proposal, for the
  owner to weigh; (b) as a factor scaling the value, against a budget no key declares; (c) not at all,
  which fails the clause's "and review cost". (a) meets the clause, keeps the value's evidence plain,
  and leaves a cap's value the owner's (P9). Rung 3. RESOLVED (agent, 2026-11-02, delegated): (a).
  widens: none · relaxes: none
- **F4 — What row floor does the caps step pass the factory?** The clause names none; its siblings 6
  and 16 name 30 (v2:1370, the clause of unit 16). (a) 30, one floor for the build's three callers;
  (b) 10, `P90_MIN_ROWS` of TOOL-dWellOiledMachine-53, which refuses less evidence; (c) a new policy
  key, a public surface no clause names. (a) refuses three of the six measured files today (§4) and
  re-derives the other three and the class row. Rung 3. RESOLVED (agent, 2026-11-02, delegated): (a),
  a module constant `MIN_ROWS = 30`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft.
- rev-2 · 2026-11-02 · §3 §4 §5 §7 S4 S6 S7 S8 S9 AC2 AC7 AC9 · amended at the disposal of the
  round-1 spec audit `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4
  "Amendments (round-1 spec audit)": ids 2 (`TOOL-dCalibratedLens-21`), 3
  (`TOOL-dCalibratedLens-22`), and 5, 32, 6, 9, 17, 42, 20 and 21 (`TOOL-dCalibratedLens-30`); the
  Files touched row of the registry is withdrawn (id 2); §3 gains the hands-offs to units 21 and 30,
  and the consumes-from unit 2 now names `PROVIDERS` (id 5).
- rev-3 · 2026-11-02 · §3 · amended at the disposal of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`: §3 gains the hands-off to unit 41, which
  widens the `loop measure fixtures` guard (r2 id 13).
- rev-4 · 2026-11-03 · §3 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`: §3's hands-off of the row's guard names
  `TOOL-dCalibratedLens-46` in place of unit 41, which takes the widening into the leg's declaration
  (r3 id 22).

## 10. Reuse audit

The seams extended: the cap census's one reader `read_cap_census` (`tools/policy/budgets.py:112`)
behind a new `census` verb beside `resolve` and `check` (`budgets.py:360-400`); `resolve_caps`
(`budgets.py:206`) through its existing `resolve` CLI for each cap's value; TOOL-dDeclaredLoop-2's
`policy_edit.py propose` as the one write-free route to the owner; the loop review module, record kind
and verbs of TOOL-dCalibratedLens-3; and the value ledger view of TOOL-dCalibratedLens-2. For the
factory itself no existing seam fits: `python tools/codebase-map/reuse_lookup.py "derive a measured
value from recorded evidence rows as a p90 and suggest it to the owner without writing it"` ranked
name-stem neighbours only (`rows`, `write`, `derive_tool_root`, `measure_typed_counts`), none a
quantile, and the grep in §4 finds none; the specced p90s are other kits' and a kit imports no sibling.
Where the brief and source disagree at this base: the brief's "a raise only through
`check_raise_shape` with its DECISIONS row" describes the guard's admitted shape (`guard.py:141-178`,
`:181-191`), whose module docstring admits "one agent shape: a single measured-file cap under
`budgets` raised", and the limits file's condition 1 keeps a review run out of it (F2). The recall hits agree with source: the
four-condition rule is `TOOL-aOrientedCast-23` (`memory/DECISIONS.md:138`).

Recall terms used: `python tools/memory-recall/query.py "how are size caps re-derived from evidence
and a raise argued through the guard with a decisions row" --terms "budgets cap raise measured-file
check_raise_shape resolve_caps census p90 evidence re-derived owner proposal"`
