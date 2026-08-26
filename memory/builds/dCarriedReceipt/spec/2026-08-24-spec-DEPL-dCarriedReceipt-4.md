# DEPL-dCarriedReceipt-4 — `coverage_rows()` and `plan --coverage`

**Status:** CLOSED · rev-6 · 2026-08-26 · node d · Tier-1 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-build-DEPL-dCarriedReceipt-4-acceptance-ledger.md](../build/2026-08-26-build-DEPL-dCarriedReceipt-4-acceptance-ledger.md) | journal | — |
| [2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round6.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round6.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-26-review-DEPL-dCarriedReceipt-13-diff-review-round1.md](../reviews/2026-08-26-review-DEPL-dCarriedReceipt-13-diff-review-round1.md) | diff-review | DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-15 |
| [2026-08-26-review-DEPL-dCarriedReceipt-4-diff-review-round1.md](../reviews/2026-08-26-review-DEPL-dCarriedReceipt-4-diff-review-round1.md) | diff-review | DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-15 |
| [2026-08-26-review-DEPL-dCarriedReceipt-5-diff-review-round2.md](../reviews/2026-08-26-review-DEPL-dCarriedReceipt-5-diff-review-round2.md) | diff-review | DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-15 |

<!-- /gen:spec-records -->

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
  case prints `gap 0` explicitly rather than printing nothing. Every count it prints is a count of
  ROWS, never of unique destinations. Two rules resolving to one `dest` are two triage items, and a
  destination-keyed tally is exactly what hid the collision §4's join now names.
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
- **Land-alone:** this unit leaves both trees green on its own and writes nothing anywhere. Its one
  unit dependency is an ORDER rather than a conflict, in the vocabulary `-14` §8 F3 ratifies: it
  lands after `-1`, because AC3 asserts the post-`-1` reading of `54` while the pre-`-1` tree prints
  `55`. A real inCMS reading additionally needs `.governance/deploy.toml` in that repo, since
  `load_deploy` (`:553`) refuses without one; `ABL-dPinnedVintage-1` writes it. That is a
  target-side prerequisite, not a landing partner.

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
| NicoCares | 143 | 0 | it took every file gov ships for its 15 declared kits |
| inCMS, pre-`-1` | 135 | 55 | 2 are `-1`'s resolver bug, 11 declarable, 1 a landed merged snippet, 41 absent |
| inCMS, post-`-1` | 135 | 54 | `.githooks/pre-push` resolves to a path inCMS already tracks |

The four-way join at NicoCares, stated here once so `-13`, ABL-2 and the audit record stop
disagreeing: **181 plan rows → 143 write rows → 136 of role `engine` → 142 unique destinations**,
which is exactly ONE destination collision, at `scripts/kit.toml`. That single collision IS ABL-2's
"1 not installed at all", masked by a destination-keyed join.

NicoCares reading zero is the calibration that makes a nonzero reading mean something. inCMS's two
`push-main` rows land at the target ROOT as `pre-push` and `pre-push.test.sh` at `9ddcc5c9`, which
is `-1`'s defect seen from the coverage side. This unit lands after `-1`, so what it prints is
`.githooks/pre-push.test.sh` under `.githooks/`, and `.githooks/pre-push` — which inCMS tracks —
has left the gap set entirely.

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
  absence without re-running; the per-kit tally is what makes inCMS's 54 post-`-1` gap rows
  triageable.
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
- **AC2** — After the change, the FULL command against NicoCares — `python tools/govkit/govkit.py
  plan --target <NC> --coverage --kits
  check-install-prefix,gate-lint,kickoff-manifest,lexicon,memory-tree,playbook,run-gates,settings-merge,agent-cap,codebase-map,drift-audit,memory-recall,playbook-render,unattended,review-harness`
  — reports `181` plan rows, `143` write rows and `gap 0`, and exits 0. The `--kits` list is not
  decoration: `resolve_selection` (`:410-429`) branches on `all` / `kits` / `default_kits(reg)` and
  never reads `deploy["kits"]`, so the same command without it resolves the registry default set and
  reports a different write-row count — a different question, correctly answered.

  **AMENDED at rev-6.** The three figures above are measurements at `9ddcc5c9` and are kept as
  history; they are not what the criterion asserts, because gov has shipped files since and a
  target that was complete then is behind now. What it asserts is the CALIBRATION: the command
  runs against the live target, the gap set is derivable, and every gap row it prints names a file
  gov ships today and the target does not track — checked row by row against `git ls-files` on both
  sides, which is the claim `gap 0` was standing in for. A gap row that survives that check is a
  real finding about the target rather than a fault in the join, and the reading of the day is
  recorded in the acceptance ledger with its date and both shas.
- **AC3** — Against inCMS with a `deploy.toml` declaring its 14 kits at `prefix = "scripts"` and
  the same `--kits` treatment, the one surviving `push-main` gap row is `.githooks/pre-push.test.sh`,
  sitting under `.githooks/` and NOT at the target root, and `.githooks/pre-push` is absent from the
  gap set because inCMS tracks it. That pair IS the criterion: it is `-1`'s resolver fix seen from
  the coverage side, and a reading that puts either row at the target root means `-1` regressed.

  **AMENDED at rev-6.** The gap and write-row counts are struck from the assertion and kept as
  history. `54` over `135` was measured at `9ddcc5c9`, and `55` before `-1`; gov has shipped files
  since, so the count moves with gov's own tree and pinning it would make this criterion red on
  every unrelated landing. The structural pair above does not move, which is why it is what
  survives. The reading of the day, its date and both shas go in the acceptance ledger.
  A target-side prerequisite stands unchanged: `load_deploy` refuses without
  `.governance/deploy.toml`, which inCMS does not carry and which the adopter-side build writes.
  A run taken before it lands must say, in the ledger, that it reconstructed one — from inCMS's own
  declared kit list and never from an invented one — and must not write it into that repository.
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
  for a real problem such as an unresolved answer, and a gap alone leaves it 0. inCMS's `54` —
  `55` before `-1` — is a state of the world, not a fault in the run, and a first honest run that
  exits 1 reads as a broken tool and teaches the operator to stop running it.
  RESOLVED (agent, 2026-08-24, delegated): report-only, under the full-scope approval.
- **F2 — does `--coverage` replace the ordinary plan output or add to it?** Add. The plan rows are
  what a reader needs to interpret a gap row, and a mode that hides them makes the operator run the
  verb twice.
  RESOLVED (agent, 2026-08-24, delegated): additive.

## 9. Revision log

- rev-6 · 2026-08-26 · BUILT and CLOSED on node `a`, session `aResumedRelay`. TWO criteria AMENDED,
  and both for one reason: AC2 and AC3 pinned gap and write-row COUNTS measured against the two
  live targets at a gov vintage that has since moved 83 commits. A count of what gov ships is not
  a property of this join, so pinning one made these criteria red on every unrelated landing — the
  value-in-prose-beside-the-source-that-owns-it class, one layer out. What each now asserts is the
  claim the count was standing in for: for AC2 the calibration, that every gap row names a file gov
  ships and the target does not track, checked on both sides; for AC3 the `-1` regression pair,
  which does not move. The struck figures are kept as history in place. Also AMENDED into AC3: a
  run taken before the adopter-side descriptor lands must record that it reconstructed one from
  inCMS's own declared kit list, and must not write it into that repository. Readings, dates and
  shas are in the acceptance ledger under `build/`.

- rev-5 · 2026-08-25 · round-5 fold: L1 — the rev-4 entry below recorded as done the one
  edit its own commit undid. It claimed AC2's `--kits` value is split at a comma across two
  indented lines and measured the wider half at 104 columns; the value is on ONE line, 195
  columns, because a newline inside the inline code span stops the FULL command being one shell
  argument. The entry now records the reversal and its reason. No spec text moved.
- rev-4 · 2026-08-25 · round-4 fold: L6 — the rev-3 rewrap had pushed AC2's `--kits` continuation
  to column 0, the only de-indented continuation in the corpus and one blank line from detaching
  from its criterion. It is re-indented two spaces and deliberately left on ONE line. A split at a
  comma was tried and withdrawn: the value sits inside the multi-line inline code span that IS the
  FULL command, and a newline mid-value breaks it. The line is 195 columns and stays that way —
  the over-width line is the narrower defect, and de-indenting is what this finding refuses.
- rev-3 · 2026-08-24 · round-2 fold: every LIVE statement of the gap count now carries its vintage.
  §5's observability line and §8 F1 read `54` (post-`-1`) where they read a bare `55` that rev-2's
  own AC3 defines as a regression alarm, and the rev-1 entry below keeps its `55` as the historical
  reading it always was. §3 gains the land-alone bullet every sibling spec carries, stating the
  `-1` dependency as an ORDER rather than a conflict. `resolve_selection` was re-read at `9ddcc5c9`
  and AC2's claim stands unchanged: it is `:410-429`, it branches on `all` / `kits` /
  `default_kits(reg)`, it never reads `deploy["kits"]`, and the registry default set is the six
  kits at `registry.toml:36` — so no scope item teaching `--coverage` to read `deploy["kits"]` is
  added here, and `ABL-dPinnedVintage-1` names the full `--kits` command instead.
- rev-2 · 2026-08-24 · folded the pre-code review: AC2 now names the FULL command, because
  `resolve_selection` never reads `deploy["kits"]` and the bare command measures the registry
  default set (69 write rows) rather than NicoCares' 15 declared kits — naming the command was
  chosen over adding a scope item that would teach `--coverage` to read `deploy["kits"]`, which is
  engine behaviour this read-only unit has no business inventing; S4 now states that the report
  counts ROWS, not unique destinations; §4 carries the four-way join (181 → 143 → 136 engine → 142
  unique destinations, one collision at `scripts/kit.toml`); and AC3 asserts the post-`-1` world it
  actually runs in — `54`, with the surviving row under `.githooks/` — keeping `55` as the labelled
  historical reading. Reproducing inCMS's figure needs the reconstructed descriptor to carry its
  `[kit.*]` layout overrides; without them the naive reconstruction reads high, which is why §4
  labels both rows by vintage rather than leaving one bare number.
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
