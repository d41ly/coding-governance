# TOOL-aSparedSpawn-19 — the spawn-budget leg never passes a run that graded nothing it could have

**Status:** OPEN · rev-1 · 2026-10-12 · node a · Tier-2 · base 8444f597 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close HIGH finding 20 (H3) of the round-1 closing review
(`memory/builds/aSparedSpawn/reviews/2026-10-12-review-TOOL-aSparedSpawn-1-15-closing-diff-round1.md`)
with its duplicates, findings 4 and 15 (M1), as one change, following the report's reconciliation.
`check_budgets` in `tools/gate-lint/fork-count.sh` ends on `[ "$red" = 0 ]`, so a run that graded
no row exits 0 and the `spawn budget (forks per hot entrypoint)` leg prints `GATE ok`. That holds
for a mistyped `--only`, for every row skipped by a failed setup, and for a bash no row declares,
which is CI's. After this unit the first two refuse, and the third keeps owner ruling F1(a)'s
skipped shape but says loudly that nothing was measured.

## 2. Scope (IN)

Every site was re-read at f479ba42, whose `tools/gate-lint/fork-count.sh` is unchanged at 8444f597;
line numbers are that tree's.

- **S1** — Finding 4. An `--only` id that names no declared row refuses with exit 2, printing the
  declared ids, after `read_budgets` (`:206`) and before any row is traced. Today
  `--only no-such-id` prints `0 passed · 0 red · 0 skipped` and exits 0. Observed by AC1.
- **S2** — Finding 20. A run that grades zero rows while at least one row in its selection IS
  declared for the running bash, every such row skipped because its fixture setup failed or it wrote
  no trace, refuses with exit 2 and names the running bash. Observed by AC2.
- **S3** — Findings 20 and 15. A run on a bash for which NO row in its selection is declared keeps
  owner ruling F1(a): each entrypoint prints the `skipped` shape and the run exits 0. It also prints
  one distinct line, `fork-count: NOT MEASURED — no row declares bash <major.minor>, so the spawn
  budget was not measured on this bash`, so the leg's log shows the gap rather than a quiet pass.
  Observed by AC3.
- **S4** — The script's header (`:21`-`:30`) and the `fork-count.sh` section of
  `tools/gate-lint/README.md` state the three outcomes of a run that grades nothing: a typo refuses,
  a declared bash with nothing graded refuses, and an undeclared bash prints the NOT MEASURED line
  and passes. Observed by AC4.
- **S5** — `run_selftest` gains one arm per outcome above, each against a scratch ceilings file, and
  its PASS line counts five assertions. Observed by AC5.

## 3. Non-goals (OUT)

- Declaring bash 5.2 rows in `memory/project/fork-ceilings.txt`, measured on CI's Git Bash. They
  cannot be measured on node a, which runs bash 5.3, so this is carried to the build's exit as an
  ask. Until they exist, CI's bar prints the NOT MEASURED line and passes, by ruling F1(a).
- Making a run on an undeclared bash refuse. The report's reconciliation orders the rows first;
  without them every CI bar would red.
- Running any suite or the bar inside the build pass, and a kit version bump, which the main loop
  makes once after the build's last unit.

### Edges

none

## 4. Design

`check_budgets` already keeps `ok`, `red` and `skip` and a `have` map of the ids it ran. One count
joins them: `declared`, the selected rows whose version equals the running bash. The `--only` check
reads the `ids` map the function already builds first. The decision after the loop is:

| Selection | Rows for this bash | Graded | Outcome |
|---|---|---|---|
| `--only <id>`, id not in `ids` | any | none | exit 2, the declared ids listed |
| any | at least one | zero | exit 2, the running bash named |
| any | none | zero | the skipped lines, the NOT MEASURED line, exit 0 |
| any | at least one | at least one | today's rule: exit 1 on a red, else 0 |

Every new line is built with `printf` and parameter expansion, so the script adds no site to
`memory/project/spawn-idiom-sites.txt` and no fork to any row it measures.

### Inventory

No new function is minted; the arms live inside `run_selftest`, so the lexicon leg sees no new
definition.

### Files touched (estimate)

- `tools/gate-lint/fork-count.sh`
- `tools/gate-lint/README.md`

### Alternatives rejected

- **Exit 2 whenever nothing was graded.** It reds every CI bar until 5.2 rows exist, which the
  reconciliation rejects.
- **Leave the undeclared-bash case silent.** It is the could-not-fail shape the review found: a
  green row that measured nothing, indistinguishable from a measured one.

## 5. Production-readiness checklist

- security: N/A — a counting gate over local fixtures; no input, write path or authority moves.
- perf / scale: two counters in a loop that already runs; the refusals exit before any trace.
- error / empty / loading states: S1 and S2 refuse with the remedy in the line; S3 announces the unmeasured bash.
- observability: the NOT MEASURED line rides the leg's log on every CI bar until 5.2 rows land.
- risks: a node on a new bash minor prints NOT MEASURED until its rows are declared, which is the intended signal.
- testing: three selftest arms, each observed red at f479ba42's script first.
- migration: none; the ceilings file's grammar is unchanged.
- user docs: `tools/gate-lint/README.md`'s `fork-count.sh` section states the three outcomes.

## 6. Acceptance criteria

- **AC1** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only no-such-id`
  runs, it exits 2 and lists every declared id. Red when: the typo exits 0, which is f479ba42's
  behaviour.
- **AC2** — When `fork-count.sh` runs over a scratch ceilings file holding one row for the running
  bash whose setup is `exit 1`, it exits 2 and names the running bash. Red when: it exits 0 with
  `0 passed · 0 red · 1 skipped`, which is f479ba42's behaviour.
- **AC3** — When `fork-count.sh` runs over a scratch ceilings file holding one row declared for bash
  `9.9`, it exits 0 and prints the `NOT MEASURED` line naming the running bash. Red when: the line
  is absent, or the run exits non-zero.
- **AC4** — When `grep -n 'NOT MEASURED' tools/gate-lint/fork-count.sh tools/gate-lint/README.md`
  runs, it prints the header's rule and the README's. Red when: either file is silent on it.
- **AC5** — When `bash tools/gate-lint/fork-count.sh --selftest` runs, it prints
  `PASS (5 assertions)`. Red when: any of the three new arms fails, or the count stays at 2.

## 7. Gates

`spawn budget (forks per hot entrypoint)` · `shell-hygiene selftest` ·
`shell hygiene (a fork spent on builtin work)` · `harness arms (fail branches armed or pinned)` ·
`lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/gate-lint/fork-count.sh · covers AC1 AC2 AC3 AC5 · an `--only` typo, a declared row whose setup fails, a file declaring another bash · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft, from `TOOL-aSparedSpawn-16` rev-1's S7 and AC7, promoted with
  findings 20 and 15 to a unit of its own by the converged closing review under the owner rulings of
  2026-10-04.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "refuse a selector naming no declared row"` ranks generic `row`
and `rows` helpers from other kits' suites; no existing seam fits. The refusals extend
`check_budgets` and sit beside `read_budgets`'s own empty-file refusal in
`tools/gate-lint/fork-count.sh`, which is the same "graded NOTHING" shape this unit applies to the
selection.

Recall terms used: spawn budget fork ceilings check_budgets read_budgets skipped bash version F1 vacuous
selector empty population graded nothing
