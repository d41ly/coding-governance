# TOOL-dMindYourWords-51 — the audit of units 30 to 37: the minors on govkit's root-file class, batched — the registry's ledger tables join the population, read and validated once

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 4 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-51-deviation-511.md](../build/2026-10-29-build-TOOL-dMindYourWords-51-deviation-511.md) | deviation | — |
| [2026-10-29-prompt-TOOL-dMindYourWords-38-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-38-promoted-fix-brief.md) | research | TOOL-dMindYourWords-38 TOOL-dMindYourWords-40 TOOL-dMindYourWords-48 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 30 to 37
(`memory/builds/dMindYourWords/reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`)
confirmed 15 MEDIUM and 5 LOW findings. BUILD-METHOD M4 batches them, and they split into two disjoint
write sets by M6: the two of item M1 touch only `tools/govkit/`, every other one touches the lexicon kit,
its suite or the memory-tree carriers. This unit is the govkit half, the MEDIUM ids 4 and 18, both
landing on TOOL-dMindYourWords-34, so it builds at order 4, one above that unit. The lexicon half is
TOOL-dMindYourWords-52.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 4, 18 | S1, S2 |

TOOL-dMindYourWords-34 S1 derives the root ledgers from each descriptor's `[[ledger]]` tables only,
while TOOL-dWitnessedBar-13 defines the registration population as every `kit.toml`'s `[[ledger]]`
tables plus those of `<tool root>/govkit/registry.toml`, the home for a population no descriptor owns.
Two derivations answer "which ledgers exist" and disagree, on membership and on validation.

## 2. Scope (IN)

- **S1** — id 18, item M1, landing on unit 34. `derive_root_confs(descs, reg)` in
  `tools/govkit/govkit.py` also reads each `home` of the `[[ledger]]` tables of the registry `reg`,
  which check 7c already holds from `load_registry(root)` (`tools/govkit/govkit.py:247`), beside the
  descriptors' conf and ledger homes, each kept only when non-empty and carrying no `/`. A root ledger
  registered only in `govkit/registry.toml` is classed. Observed by AC1.
- **S2** — id 4, item M1, landing on unit 34. One validation for both sources: a ledger table whose
  `home` is not a string, or a root `home` declared by two declarers, a descriptor and the registry or
  two of either, fails selfcheck naming both declarers and the home, never classing it twice or
  silently. When TOOL-dWitnessedBar-13's `read_registrations(root)` lands, its reader replaces this
  read, carried inline as govkit carries `resolve_kit_dir` (`tools/govkit/govkit.py:197`). Observed by
  AC2.

## 3. Non-goals (OUT)

- Any high: units 38 and 39 (H5), on the same function's argv read.
- The lexicon half of the minors: TOOL-dMindYourWords-52.
- Building `read_registrations`: TOOL-dWitnessedBar-13, DEFERRED in its own build.
- The checklist entry the report names under M1: a checklist is its own artifact (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-34` — S1's ledger-home population, which S1 widens to the registry and S2 validates

## 4. Design

### Why two batches

M4 admits two batch units only when the minors split into two disjoint write sets by M6's clauses.
This unit writes `tools/govkit/govkit.py` and `tools/govkit/selftest.py`; TOOL-dMindYourWords-52 writes
the lexicon kit, its suite, `tools/gate-legs.json` and the memory-tree carriers. Neither reads a file the
other writes as a contract, and neither touches `memory/DECISIONS.md`, a backlog shard, the run-state
file or a generated index with its generator. The split also lets M1 close at order 4, one step after
the unit it repairs, rather than after the whole roster.

### Evidence

- `derive_root_confs(descs)` reads only descriptors (`tools/govkit/govkit.py:1653-1667`) and is called
  once, at `:2555`, where `reg` is in scope.
- `tools/govkit/registry.toml` declares no `[[ledger]]` table at base (`grep -c '^\[\[ledger'
  tools/govkit/registry.toml` prints 0), so S1 classes nothing new on gov's tree today; the effect is
  latent, as the report states.
- TOOL-dWitnessedBar-13 S2 and §4 "The registration" define the population over descriptors and
  `govkit/registry.toml` (`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-13.md`).

### Inventory

Minted: none. `derive_root_confs` gains a parameter; its one caller passes `reg`.

### Rollout

Live at landing, after TOOL-dMindYourWords-38 and -39 at the same order, which sort first.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2
- `tools/govkit/selftest.py`: the arms of §7

### Alternatives rejected

- **Stating in unit 34's §3 that registry ledgers are excluded**, the report's third route: it leaves
  two answers to one question and names the gap instead of closing it.
- **Waiting for `read_registrations`**: it is DEFERRED in another build, and the class would stay wrong
  until it lands.

## 5. Production-readiness checklist

- security — N/A — a classifier over the deployer's own manifest and registry.
- perf / scale — one pass over the registry's ledger tables, none at base.
- error / empty / loading states — a registry with no `[[ledger]]` contributes nothing; S2 names a
  malformed or doubly declared home.
- observability — 7c's unclassed line and S2's failure name the file that declares the home.
- risks — none on gov's tree, which declares no registry ledger.
- testing — AC1, AC2 and the arms of §7.
- migration — none.
- user docs — N/A — govkit's internal check.

## 6. Acceptance criteria

- **AC1** — When `python <prefix>/govkit/govkit.py selfcheck` runs in a scratch gov tree whose
  `tools/govkit/registry.toml` declares `[[ledger]]` with `home = ".reg-debt.txt"`, no descriptor declaring
  it, and a leg guarding `.reg-debt.txt`, it prints no `falls into 0 declared classes` line naming
  `.reg-debt.txt`.
  Red when: the registry's ledger is unclassed and 7c reds a correct guard.
  fixture: a scratch gov tree under `%TEMP%/<short>`, as unit 34 AC2's.
- **AC2** — When the same tree's one kit descriptor also declares `[[ledger]]` with `home =
  ".reg-debt.txt"`, the run exits 1 naming `.reg-debt.txt`, the descriptor and `registry.toml`.
  Red when: a doubly declared home is classed silently.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · a scratch registry declaring a root `[[ledger]]` alone and then beside a descriptor declaring the same home, its failing case the registry read cut from `derive_root_confs`, under which `.reg-debt.txt` falls into 0 classes · none

## 8. Open questions

- **F1 — One batch or two?** Options: (a) one unit holding all 20 minors; (b) two, item M1 apart. M4
  permits (b) only for disjoint write sets, which §4 shows, and (b) closes M1 at order 4 instead of
  22. RESOLVED (agent, 2026-10-29, delegated): (b), rung 3, the option that closes each minor nearest
  the unit it repairs. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from the round-1 audit of units 30 to 37's MEDIUM ids 4
  and 18, one scope item per raw id.

## 10. Reuse audit

The seam is `derive_root_confs` (`tools/govkit/govkit.py:1653-1667`) and the registry `load_registry`
already loads (`:247`), with unit 34's arms at `tools/govkit/selftest.py:6139` as the fixture.
`python tools/codebase-map/reuse_lookup.py "derive a guard pathspec class for a root file a kit
declares"` ranked `repo_root`, `resolve_kit_dir` and `kit_rel`, none of which reads ledger tables, and
`read_registrations` does not exist in the tree (`git grep -n read_registrations -- tools` prints
nothing), so the existing function is the one seam that fits.

Recall terms used: `python tools/memory-recall/query.py "how does govkit classify a guard pathspec naming a root file a kit owns" --terms "root-conf guard pathspec class derive_root_confs 7c selfcheck ledger home registry registration"`
