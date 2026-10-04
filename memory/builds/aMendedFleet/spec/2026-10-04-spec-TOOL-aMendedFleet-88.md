# TOOL-aMendedFleet-88 — `map_imports.py` is deleted, having no consumer

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 88

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`map_imports.py` was rescued out of the lexicon kit on 2026-09-06 so a variant harness could resolve
imports by AST. That harness shipped as `rank_harness.py` and does not import it, and nothing else in
the tree does except the kit selftest, whose parity arm now always skips because the original is
gone. A seam with no caller is dead code that the map's dossier and the kit README advertise as a
seam. This unit deletes the module, its three selftest arms and the canonical copy only those arms
used, and removes the prose that advertises it.

## 2. Scope (IN)

- **S1** — Before any other edit, the pass re-verifies at its own base that no tracked file but the
  kit selftest imports the module. If another importer exists the pass leaves the tree untouched and
  parks with the importer named. Observed by AC1.
- **S2** — `tools/codebase-map/map_imports.py` is deleted. Observed by AC2.
  **Readers:** by name: `tools/codebase-map/selftest.py`, `tools/codebase-map/README.md`,
  `memory/map/features/codebase-map.md` and `memory/map/generated/symbols.json` spell
  `map_imports.py`, `resolve_import` or `build_module_index`.
  by value: `tools/codebase-map/selftest.py` alone calls `resolve_import` and `build_module_index`,
  through the three arms S3 deletes; no other module imports it.
- **S3** — `tools/codebase-map/selftest.py` drops its `import map_imports as mi` line, the three arms
  registered as `map_imports: the rescued resolver's case table`, `map_imports: no sibling-kit import
  (AC7)` and `map_imports: same candidates as the kit it was rescued from (AC1)`, their functions and
  the `RI_FILES`, `PY_IMPORTER` and `JS_IMPORTER` fixtures. Its inlined `resolve_kit_dir` canonical
  copy, called only by the deleted parity arm, is deleted with them, and any import left unused is
  removed. Observed by AC2 and AC4.
  **Readers:** by name: `tools/codebase-map/selftest.py` spells the three arm names, the fixture
  names and its `resolve_kit_dir` copy; `memory/map/generated/symbols.json` lists the arm functions.
  by value: NO VALUE READERS — the arms report to the selftest's own pass count and nothing reads
  their names; the canonical-copy parity suite in `tools/lib/resolve-python.test.sh` finds carriers
  with `git grep -l` at run time and pins no list.
- **S4** — The `map_imports.py` row of `tools/codebase-map/README.md` and the dossier paragraph in
  `memory/map/features/codebase-map.md` calling it the tree's one AST import resolver are deleted,
  and no sentence replaces them: the history is this spec and git, not dossier prose.
  `memory/map/generated/symbols.json` is re-rendered by `gen_map.py --write`. Observed by AC2 and
  AC3.
  **Readers:** by name: `memory/map/features/codebase-map.md` and `tools/codebase-map/README.md`.
  by value: NO VALUE READERS — prose; the generated file is compared by the freshness leg, which
  AC3 runs directly.

## 3. Non-goals (OUT)

- Giving the module a consumer. §8 F1 records why deletion wins.
- The lexicon kit's epitaph prose for its deleted predicate, which names `resolve_import` as that
  kit's own former function and points at nothing here.
- Closed build records quoting the module. They are frozen and are not rewritten.
- The codebase-map kit version bump, owed once at the build's close.

### Edges

- **hands-off** external — the kit version bump at the close.

## 4. Design

### Evidence

Read at base `7af5f564`; `git diff --stat 7af5f564 HEAD` over `tools/codebase-map` and `memory/map`
is empty at `8312d315`.

- `git grep -l map_imports` outside `memory/builds` lists the module, the kit selftest, the kit
  README, the `codebase-map` dossier and the generated `symbols.json`, and nothing else. No
  `kit.toml`, gate leg, conf or lexicon declaration names it; the kit ships `**`, so no file list
  changes.
- The rescue spec, `TOOL-dTracedLattice-6`, names the variant harness of its sibling unit as the
  consumer. `tools/codebase-map/rank_harness.py`, which that build shipped, imports no resolver.
- `tools/lexicon/lexicon.py` defines neither `resolve_import` nor `build_module_index`, so the
  parity arm raises `Skipped` on every run: a check that can no longer move.
- The selftest's inlined `resolve_kit_dir` is called once, at the parity arm's lookup of the lexicon
  kit. The canonical-copy suite discovers carriers by `git grep -l`, so dropping a carrier needs no
  registry edit.
- Unit 42, earlier in the order, counts canonical-copy install sites; its figure is DERIVED at
  observation, so one carrier fewer moves no pinned number.

### Inventory

Nothing is minted; this unit only deletes.

### Files touched (estimate)

- `tools/codebase-map/map_imports.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/README.md`
- `memory/map/features/codebase-map.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Keeping the module with its parity arm.** The arm skips forever and the module is advertised as
  a seam nobody calls; both are the could-not-fail shape §7 of the charter names.
- **Keeping the module and dropping only the parity arm.** It leaves an advertised seam with no
  caller, which is the finding.

## 5. Production-readiness checklist

- security — N/A — a deletion of an unreferenced module.
- perf / scale — N/A — nothing runs that did not run before, and three selftest arms fewer.
- error / empty / loading states — S1's re-verify parks the pass rather than deleting a module
  something imports.
- observability — N/A — nothing is left to observe; this spec and the commit record the deletion.
- risks — an adopter with its own caller of the module loses it on the next kit upgrade; none is
  known, and the bytes stay in git history at the rescue commit.
- testing — AC1 to AC4 run directly; the kit selftest runs at the close.
- migration — N/A — no data and no conf key.
- user docs — S4.

## 6. Acceptance criteria

- **AC1** — When `git grep -l -E "^[[:space:]]*(import|from) map_imports" -- "*.py"` runs at the
  pass's base, before any deletion, it prints exactly one path, the codebase-map kit's selftest.
  Red when: a second importer exists, and the pass parks instead of deleting.
- **AC2** — When `git grep -n "map_imports" -- tools memory/map` and
  `git grep -n -E "\bmi\.|^# >>> resolve_kit_dir|^def resolve_kit_dir" -- tools/codebase-map/selftest.py`
  run after the unit's commit, both print nothing. The second grep names the dead copy's marker and
  definition rather than the bare name, because `TOOL-aMendedFleet-42`'s install-site arm, earlier in
  the order, may spell the helper's name in a fixture.
  Red when: a reader, a fixture or the dead canonical copy survives, or the module is still named
  anywhere in the kit or the map.
- **AC3** — When `python tools/codebase-map/gen_map.py --check` runs after the unit's commit, it
  exits 0.
  Red when: `symbols.json` still lists the deleted functions.
- **AC4** — When `PYTHONPATH=tools/codebase-map python -B -c "import selftest"` runs after the unit's
  commit, it exits 0.
  Red when: a removed import or fixture is still referenced at module level.

## 7. Gates

`codebase-map coverage + freshness` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `kit epoch (shipped bytes move, the version moves)` · `python resolver (behaviour + inline parity + idiom ban)` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No arm is added; three are deleted with the module they covered.

## 8. Open questions

- **F1 — Give the module a consumer, or delete it?**
  The report offers both. A consumer would be the reference index resolving import edges so fan-in
  counts imports, a ranking change unit 41's floor would have to price and unit 42 declined to make
  for the same reason. No criterion in this build needs import resolution, and a consumer built to
  keep a module alive is the speculative option.
  RESOLVED (agent, 2026-10-04, delegated): delete. The owner's prompt asked for every report point
  worked out and this point names deletion; the rescue's purpose was a consumer that never
  materialised, and the bytes stay recoverable from history.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#46], unit 42's F1 census and a
  re-read of every reader at base.
- rev-2 · 2026-10-04 · AC2 · the M2 cross-read: AC2 required no `resolve_kit_dir` anywhere in the
  kit selftest, while `TOOL-aMendedFleet-42` adds an install-site arm to the same file before this
  unit, whose fixture may spell that name; AC2 now greps the dead copy's opening marker and `def`.

## 10. Reuse audit

No existing seam fits, and none is needed: this unit deletes rather than builds. `python
tools/codebase-map/reuse_lookup.py "resolve an import statement to the repo paths it may denote"`
returned `resolve` in the recall kit's conf module, `repo_root` and the `resolve_kit_dir` copies,
name-stem neighbours that resolve roots and kit directories, and not `resolve_import` itself, which
is a measured point for the deletion: the probe that ranks seams does not surface this one for its
own job. The probe printed `unscanned layers: .sh`; the only shell reader of the canonical-copy
marker is the parity suite, which S3 accounts for. The recall probe returned the rescue spec, the
dossier paragraph, the lexicon kit's decision deleting the original predicate and unit 42's census.
Where the report and the tree disagree: nowhere; every claim in unit 42's F1 reproduces at base.

Recall terms used: `python tools/memory-recall/query.py "who consumes the rescued AST import resolver
map_imports and should it be deleted" --terms "map_imports resolve_import build_module_index rescued
lexicon P3 predicate variant harness rank_harness consumer deletion parity arm skip"`
