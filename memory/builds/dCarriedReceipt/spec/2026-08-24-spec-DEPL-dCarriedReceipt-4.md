# DEPL-dCarriedReceipt-4 — `coverage_rows()` and `plan --coverage`

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

## 1. Goal

Nothing in this deployer answers "which files gov ships does this target not hold". `plan` previews
what `apply` would write, `check` and `update` both refuse without a receipt, and the only
partial-adoption signal that exists is WHOLE-KIT: the `available (not installed)` line `cmd_update`
prints at `:3027`, which needs the receipt neither live adopter has. So a target that took 80 files
of a kit and left 20 is indistinguishable from one that took all 100, and inCMS — which took
exactly that shape — cannot be measured by any verb at `9ddcc5c9`. Coverage is the read-only join
that needs no receipt and writes nothing, which makes it the one unit in this build that returns a
number for a real adopter today.

## 2. Scope (IN)

- **S1** — `coverage_rows(root, target, deploy, descs, selection, r)`, added between
  `planned_writes` (`:1359`, returning at `:1426`) and `cmd_plan` (`:1429`). It joins
  `planned_writes()` destinations against `tracked(target)` (`:111`) and returns one row per
  destination the target does not hold, carrying `kit`, `dest` and the gov `src` it came from.
- **S2** — the population is the `kind == "write"` rows and nothing else. `order`, `side-effect`,
  `covered` and `blocked` are each a promise gov does NOT make (`ROLE_KINDS` `:1242`, `KIND_MARKS`
  `:1258`), so counting one as a gap would report a target for a file gov never ships.
- **S3** — a row whose `missing` list is non-empty is not a coverage row. `planned_writes` already
  turns that into an `r.fail`, and a destination still carrying a brace is not a path.
- **S4** — `plan --coverage` prints one line per gap row, a per-kit tally, and a total. The clean
  case prints `gap 0` explicitly rather than printing nothing.
- **S5** — `--emit-declines` prints paste-ready `[[decline]]` skeletons to STDOUT, one per gap row,
  carrying `kit`, `dest` and an empty `why`. It never opens `.governance/deploy.toml`.
- **S6** — both flags are parsed in `parse_args` (`:3316`) and named in `USAGE` (`:3298`).

## 3. Non-goals (OUT)

- **Not** rename detection. A gap row for `scripts/check-memory-hygiene.sh` at a target holding
  `scripts/check-docs-hygiene.sh` reports as absent. Declaring that pair is `-5`'s `[[decline]]`,
  and automatic rename detection for coverage is on this build's ratified OUT list.
- **Not** writing anything into the target. `--emit-declines` produces text for a human to paste,
  because a deployer that edits the file carrying the owner's decisions has made one for them.
- **Not** grading declines. The three staleness arms are `-5`.
- **Not** measuring bytes. Coverage answers PRESENCE. A present-but-hand-edited file reads as
  covered here, and sameness needs the two identities `-7` introduces.
- **Not** the whole-kit case. `cmd_update`'s `available (not installed)` line keeps it.

## 4. Design

### Data model

No on-disk shape changes. A coverage row is in-memory only.

| field | source | why it is carried |
|---|---|---|
| `kit` | the `planned_writes` row | a gap is triaged per kit, not per file |
| `dest` | the resolved destination | the thing the target does not hold |
| `src` | the gov path the bytes come from | tells a rename from an absence without a re-run |

### Alternatives rejected

- *Test the worktree with `dp.exists()` instead of the index.* An untracked file present in a
  worktree is not a file the target holds, and this file already states that reasoning in the leg
  guard comment at `:2657-2660`, where a guard is dropped on tracked-ness rather than existence.
  Two answers to "does the target have this" is the class this repo has paid for twice.
- *Derive the shipped set from `claims`.* Arm 7h3's own comment measured `claims` covering 13 of 58
  file rules in this tree, so a claims-derived population would report a confident zero over the
  rest — the could-not-fail shape arriving as an under-derived population.
- *Make coverage an arm of `check`.* `cmd_check` refuses without `.governance/install.json`
  (`:1481-1485`), which is precisely the thing coverage must not need.

### Inventory

Measured at `9ddcc5c9` against both live targets, by running `planned_writes` and joining against
`git ls-files` — the same two seams S1 wires together:

| target | write rows | gap | note |
|---|---|---|---|
| NicoCares | 143 | 0 | it took every file gov ships for its 15 kits |
| inCMS | 135 | 55 | 2 are `-1`'s resolver bug, 11 declarable, 1 a landed merged snippet, 41 absent |

NicoCares reading zero is the calibration that makes a nonzero reading mean something. inCMS's two
`push-main` rows land at the target ROOT as `pre-push` and `pre-push.test.sh`, which is `-1`'s
defect seen from the coverage side.

### Files touched (estimate)

`tools/govkit/govkit.py` (~55 lines across `coverage_rows`, `cmd_plan`, `parse_args`, `USAGE`),
`tools/govkit/selftest.py` (4 arms), `WIRE-INTO-PROJECT.md` (one step).

## 5. Production-readiness checklist

- security — read-only: no write path, no receipt read, no new egress. `--emit-declines` prints
  target-relative paths, which is the population `plan` already prints.
- perf / scale — one `git ls-files -z` per run on top of the descriptor walk `planned_writes`
  already performs; no per-row git process. Both live targets complete inside the existing run.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — `gap 0` prints explicitly, because a skip that looks like a pass
  is indistinguishable from coverage. A kit named in `deploy.toml` that no registry entry resolves
  is reported by name rather than dropped from the selection in silence.
- observability — every row prints `kit`, `dest` and `src`, so a reader can tell a rename from an
  absence without re-running; the per-kit tally is what makes 55 rows triageable.
- risks — the real risk is a number that means less than it looks like: coverage answers presence
  only, so a hand-edited file reads as covered. Stated here and in §3 rather than implied away, and
  it is what `-7` measures instead.
- testing + left-shift gates — AC5 is the left-shift. The class is "a non-`write` kind counted as a
  gap", gated over the whole `ROLE_KINDS` table rather than over the one role that exposed it.
- migration / rollback — none. Nothing is written anywhere, and a revert removes two flags.
- user docs — `WIRE-INTO-PROJECT.md` gains the coverage step beside `plan`; `USAGE` gains both flags.

## 6. Acceptance criteria

- **AC1** — At `9ddcc5c9`, `python tools/govkit/govkit.py plan --target <NC> --coverage` exits 2
  with `unknown or incomplete argument: --coverage` from `parse_args`. Observe this first: it is
  what "no coverage measurement exists in this tool" looks like from the outside.
- **AC2** — After the change, the same command against NicoCares reports `143` write rows and
  `gap 0`, and exits 0. Zero is the calibration reading, so it is an acceptance criterion.
- **AC3** — Against inCMS with a `deploy.toml` declaring its 14 kits at `prefix = "scripts"`, the
  same command reports `55` gap rows over `135` write rows, and the rows named `pre-push` and
  `pre-push.test.sh` sit at the target root — `-1`'s defect, reported rather than hidden.
- **AC4** — `plan --target <t> --coverage --emit-declines` writes one `[[decline]]` block per gap
  row to stdout with an empty `why`, and `git -C <t> status --porcelain .governance/deploy.toml`
  is empty afterwards.
- **AC5** — A fixture whose descriptor declares a `project-owned` rule (kind `order`) and a
  `merged` rule (kind `blocked`) for paths absent from the target reports `gap 0`. This is the
  false-positive arm and it fails against a first draft that joins on every row of `planned_writes`.
- **AC6** — A fixture missing exactly one planned write reports exactly that `dest`; with the same
  file present in the worktree but NOT `git add`-ed, it still reports it. The index is the answer.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs. Adds four arms to `tools/govkit/selftest.py` and no new leg file. It adds no
refusal branch, so `BRANCH_PIN` in `tools/govkit/refusal_join.py` does not move — a coverage gap is
a measurement, not a finding, which is F1 below.

## 8. Open questions

- **F1 — does a nonzero gap change the exit code?** No. The verb reports; `r.emit()` still exits 1
  for a real problem such as an unresolved answer, and a gap alone leaves it 0. inCMS's 55 is a
  state of the world, not a fault in the run, and a first honest run that exits 1 reads as a broken
  tool and teaches the operator to stop running it.
  RESOLVED (agent, 2026-08-24, delegated): report-only, under the full-scope approval.
- **F2 — does `--coverage` replace the ordinary plan output or add to it?** Add. The plan rows are
  what a reader needs to interpret a gap row, and a mode that hides them makes the operator run the
  verb twice.
  RESOLVED (agent, 2026-08-24, delegated): additive.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass. Both target readings were
  re-measured at `9ddcc5c9` while writing, by importing `govkit` and running `planned_writes`
  against each tree: NicoCares 143/0 and inCMS 135/55, with the two root-level `push-main` rows
  confirmed as `-1`'s resolver defect. Two brief corrections are folded in. The insertion point is
  `:1427-1428`, the blank between `planned_writes`' `return out` at `:1426` and `cmd_plan` at
  `:1429`. And "needs no receipt" is exact but incomplete: coverage still needs
  `.governance/deploy.toml`, because `load_deploy` (`:553`) refuses without one — inCMS has none,
  so its 55 was measured against a descriptor reconstructed from `.governance/kits.json`, and a
  real reading there waits on inCMS writing its own. That is recorded as a cross-unit dependency,
  not as scope here.

## 10. Reuse audit

The unit is a JOIN of two existing seams and introduces no third answer to any question this file
already answers. `planned_writes` (`:1359`) is the destination population, so coverage cannot drift
from what `apply` writes; `tracked` (`:111`) is the one index reader; `resolve_dests`,
`resolve_tokens` (`:516`) and `target_context` (`:535`) are reached only through `planned_writes`,
never re-called here; `Report` (`:565`) carries the findings. Arm 7h3 builds a `shipped_owner` map
at `:1067-1082` and it is deliberately NOT reused: that map is keyed on gov SOURCE paths for a
gov-side predicate, while coverage needs resolved TARGET destinations, which only `planned_writes`
produces. Naming the near-miss rather than silently passing it is the point of this section.
