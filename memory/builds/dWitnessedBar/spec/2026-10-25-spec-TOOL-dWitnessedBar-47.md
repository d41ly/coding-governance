# TOOL-dWitnessedBar-47 — a seed home is admitted when its directory exists, so a fresh install seeds before its first commit

**Status:** OPEN · rev-5 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 6 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 35 at HIGH**, its item **H8**, alone in that item. `TOOL-dWitnessedBar-15` §4 "The
rule" refuses a home whose parent directory holds no tracked file, and §5 applies the test to the
`--home` form too. S5 routes `adopt-codebase-map.sh`, which seeds into a just-scaffolded `memory/map/`,
and `adopt-drift-audit.sh`, which seeds into a just-copied kit directory, through that form, and govkit
apply runs adopters before anything in the target is committed. On a first adoption neither directory
holds a tracked file, so no `affordance-exempt.toml` is written and no `drift_signals.py` is seeded:
fresh installs of both kits break, and unit 15's AC7 re-runs over a fixture so it cannot see this. The
same test refuses a registered home on a fresh install too, since `adopt-memory-tree.sh` creates
`memory/project/` with `mkdir -p` (`tools/memory-tree/adopt-memory-tree.sh:515`) and commits nothing.
This unit takes the report's fix. It repairs `TOOL-dWitnessedBar-15`.

## 2. Scope (IN)

- **S1** — The admission rule. A home is admitted when its parent directory exists in the working
  tree, for a registered home and for the `--home` form alike; `seed` never creates a directory. A home
  whose parent is absent is unarmed with the reason `no directory <parent>`, and the `--home` form
  prints it on stderr and writes nothing. Observed by AC1 and AC3.
- **S2** — What it does not check, stated. `legacy_ledger.py`'s docstring and §4 of the kit README name
  the blind spot: a file name the hygiene structure check refuses inside an existing directory is
  written, and that check reds it at the next commit, never silently. Observed by AC2.
- **S3** — Fresh-install coverage. The codebase-map adopter suite runs `adopt-codebase-map.sh` once on a
  fresh `git init` target with nothing committed and observes `affordance-exempt.toml` written; the
  resolver suite's seed section runs `adopt-drift-audit.sh` likewise and observes `drift_signals.py`.
  Observed by AC1.

## 3. Non-goals (OUT)

- The seed verb, its states, its unarmed line and the two adopters' calls: `TOOL-dWitnessedBar-15`'s.
- A home with a parent but an unreadable file: the minors batch's id 56 item (`TOOL-dWitnessedBar-51`).
- How a seed argv's interpreter resolves: the minors batch's id 55 item.
- Every adopter e2e starting from an uncommitted `git init`, the report's left-shift: AC1 is that start
  for the two adopters this unit names.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-15` — `seed_population`, the `--home` form and its home test, which this unit replaces with the directory rule
- **hands-off** `TOOL-dWitnessedBar-46` — the directory rule, under which the memory-tree adopter's seed of `conf-scalar-pins` writes into the `memory/project/` it has just created
- **hands-off** `TOOL-dWitnessedBar-57` — the directory admission rule and its adopter arm, which the resolver and ledger minors batch contains within the work tree and points at the renamed file (ids 7, 45)
- **consumes-from** `TOOL-dWitnessedBar-61` — the null SHA a seed stamps on an unborn HEAD, without which a fresh `git init` target's ledger seed has no SHA to write
- **hands-off** `TOOL-dWitnessedBar-63` — this unit's pass commit, which the minors batch observes landing after unit 61's (id 2)
- **hands-off** `TOOL-dWitnessedBar-65` — this unit's pass commit at order 6, which the minors batch of the round-1 audit of unit 63 observes landing after unit 61's (id 1)

## 4. Design

### Evidence

- `adopt-codebase-map.sh:198-200` and `adopt-drift-audit.sh:241-246` hold the two absent-only guards
  unit 15 S5 re-routes; both run inside `govkit apply` before the target commits.
- `adopt-memory-tree.sh:515` runs `mkdir -p "$M/project" "$M/builds" "$M/backlog" "$M/guides"` and
  writes its registries there uncommitted.
- Unit 15 §8 F3 chose the tracked-file test because the hygiene check has no print mode; the directory
  rule keeps that reason, since it still asks no hygiene run per seed.

### The rule

| Parent directory | Home | Act |
|---|---|---|
| exists, tracked files or none | absent or unarmed | seed, per unit 15's table |
| exists | present and armed | unit 15's table |
| absent | any | write nothing; unarmed `no directory <parent>` |

### Inventory

Minted: the unarmed reason `no directory <parent>`. Nothing else.

### Migration

None. A repository whose homes already exist sees `present`.

### Rollout

Live at landing.

### Files touched (estimate)

- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`
- `tools/lib/resolve-python.test.sh`
- `tools/codebase-map/adopt-codebase-map.test.sh`
- `tools/memory-tree/README.md`

### Alternatives rejected

- **Exempt only the `--home` form.** A registered home on a fresh install meets the same untracked
  directory, so the next fresh install of a kit with a `[[ledger]]` home breaks the same way.
- **Admit by running the hygiene structure check over a staged write.** Unit 15 §8 F3 rejected the
  cost; nothing here changes it.

## 5. Production-readiness checklist

- security — the seed still writes only a registered home or an adopter-named path, never creates a
  directory, and writes by temp file and `os.replace`.
- perf / scale — one stat per home.
- error / empty / loading states — absent parent: unarmed with its reason, never a created directory.
- observability — the `unarmed` line names the missing directory.
- risks — a home in an existing directory the hygiene check refuses is written and reds at the next
  commit; S2 states it.
- testing — AC1 to AC3 by fixture; the arms of §7 at the close.
- migration — none.
- user docs — none under `help/`; the memory-tree README's seed paragraph at the pass.

## 6. Acceptance criteria

- **AC1** — When `adopt-codebase-map.sh` runs once on a fresh `git init` target under `%TEMP%` with
  nothing committed, `affordance-exempt.toml` exists under the target's map directory afterwards; when
  `adopt-drift-audit.sh` runs once on such a target, its `drift_signals.py` exists.
  Red when: the tracked-file test stays, so a fresh install writes neither file.
  fixture: fresh targets under `%TEMP%/<short-name>`, built by the suites.
- **AC2** — When `grep -n 'no directory' legacy_ledger.py` runs in `tools/lib/`, it names the refusal,
  and the module docstring names the structure-check blind spot.
  Red when: the rule ships with its blind spot unstated.
- **AC3** — When `python legacy_ledger.py seed --population p` runs in a fixture repository whose
  registration's home sits under a directory that does not exist, it prints `unarmed p no directory`
  and creates no directory; with the directory created and nothing committed, it prints `armed p`.
  Red when: `seed` creates the directory, or refuses an existing untracked one.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `codebase-map adopter e2e` · `codebase-map kit selftest` · `drift-audit selftest` · `memory hygiene` · `shell-hygiene selftest` · `codebase-map gate coverage`

New arm: tools/codebase-map/adopt-codebase-map.test.sh · covers AC1 · one adopt on a fresh uncommitted `git init` target, staged red by restoring the tracked-file test · none
New arm: tools/lib/resolve-python.test.sh · covers AC1 AC3 · section `2l`'s seed cases gain an untracked existing directory and an absent one, and a fresh drift-audit adopt, staged red by restoring the tracked-file test · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-15`'s clause. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Does the new rule apply to registered homes or the `--home` form only?** Options: (a) both, the
  directory existing; (b) the `--home` form only, registered homes keeping the tracked-file test. (b)
  leaves every registered home unseedable on a fresh install, the defect one row over. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the option that serves every fresh install. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 35 (HIGH, item H8).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the consumes-from bullet mirroring
  TOOL-dWitnessedBar-61's hands-off edge, promoted by the round-1 spec audit of units 52 to 57; nothing
  else moved.
- rev-4 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-63's
  consumes-from edge, promoted by the round-1 spec audit of units 58 to 62; nothing else moved.
- rev-5 · 2026-10-25 · §3 · the status header moves from order 5 to order 6, so unit 61, which this
  unit consumes from, closes a step before this unit is handed out. That is TOOL-dWitnessedBar-65 S6,
  closing the round-1 audit of unit 63's id 1 (MEDIUM, item M3). The Edges block gains the hands-off
  bullet mirroring TOOL-dWitnessedBar-65's consumes-from edge.

## 10. Reuse audit

The seam is unit 15's own home test in the `legacy_ledger_py` block, replaced in place and carried to
its copies by the existing parity row. `python tools/codebase-map/reuse_lookup.py "admit a seed home
whose directory an adopter just created"` ranked `seed`, `adopt`, `require_adopted_root`, `ask_home_of`,
`seed_affordances` and `resolve_adopter_argv`; `require_adopted_root` refuses an unadopted root, a
different question, and none admits a home, so no existing seam fits beyond the block.

Recall terms used: `python tools/memory-recall/query.py "why does the seed home test refuse a fresh install" --terms "seed home test tracked file fresh install adopter --home affordance-exempt drift_signals unarmed admit"`
