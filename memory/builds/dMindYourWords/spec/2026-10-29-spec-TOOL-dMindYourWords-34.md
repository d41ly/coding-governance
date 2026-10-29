# TOOL-dMindYourWords-34 — a kit's root ledger home joins govkit's `root-conf` guard class

**Status:** DEFERRED · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 3 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-prompt-TOOL-dMindYourWords-34-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-34-promoted-fix-brief.md) | research | TOOL-dMindYourWords-37 |
| [2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-30 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-35 TOOL-dMindYourWords-31 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 22 of `reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md`,
HIGH, item H3. TOOL-dMindYourWords-27 S1 adds `.lexicon-debt.txt` to the `lexicon naming predicates`
guard and claims it joins "the kit's existing root-file class", but govkit's `root-conf` class is derived
from each descriptor's single `[config] file` alone, so the pathspec falls into no class and check 7c of
`govkit selfcheck`, which runs on every bar, reds from unit 27's pass onward. This unit derives the class
from every root file a kit declares as its own, its conf and its `[[ledger]]` homes, so a root ledger a
descriptor registers is classed, and a root file no descriptor declares still reds.

## 2. Scope (IN)

- **S1** — The class population. `derive_root_confs(descs)` in `tools/govkit/govkit.py` returns each
  loaded descriptor's `[config] file` and each `home` of its `[[ledger]]` tables (TOOL-dWitnessedBar-13's
  registration), each kept only when non-empty and carrying no `/`. Still DERIVED, never listed: a kit
  that registers a root ledger widens the class the day it lands. Observed by AC1 and AC2.
- **S2** — 7c2 grades the ledger too. The same population feeds check 7c2
  (`tools/govkit/govkit.py:2606-2655`), so a guarded bar leg whose argv file names a declared root
  ledger must carry it in its guard, for the reason it must carry a conf: a ledger-only commit moves the
  leg's verdict. Observed by AC3.
- **S3** — The docstring and the 7c comment (`tools/govkit/govkit.py:1654-1660`, `:2550-2554`) say the
  class holds a kit's declared root files, its conf and its ledger homes. NOT OBSERVED as behaviour:
  prose has no grader beyond the carriers' own legs.

## 3. Non-goals (OUT)

- The guard row itself and the ledger move: TOOL-dMindYourWords-27 S1 and S2.
- A new descriptor field: the `[[ledger]]` table and its `home` already exist in the factory's
  registration, and this unit reads them.
- Renaming the class or `derive_root_confs`: the name stays, its docstring widens, and no reader of the
  class name moves.
- The spec-lint rule the report names as H3's left-shift gate: a gate is its own unit (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-27` — S1's `[[ledger]]` `home = ".lexicon-debt.txt"` and the guard pathspec naming it; without them no root ledger is declared and nothing needs the class
- **hands-off** `TOOL-dMindYourWords-38` — the widened 7c2 population, whose argv read that unit resolves through `{prefix}` (review id 7)
- **hands-off** `TOOL-dMindYourWords-51` — the ledger-home population, which the govkit minors batch widens to the registry's `[[ledger]]` tables and validates (review ids 4, 18)

## 4. Design

### Evidence

- `derive_root_confs` reads only `(d.get("config") or {}).get("file")` and keeps it when it carries no
  `/` (`tools/govkit/govkit.py:1653-1667`).
- Check 7c fails any guard pathspec that falls into a number of classes other than one; a bare root file
  is not `memory/`, verbatim, renamed, exempt or kit-relative, so it lands in the `root-conf` class or
  none (`tools/govkit/govkit.py:2544-2583`). The `govkit selfcheck` leg has no guard, so it runs on every
  bar (`tools/gate-legs.json`).
- `read_descriptors` loads each descriptor whole (`tools/govkit/govkit.py:13238-13252`), so a
  `[[ledger]]` array reaches `derive_root_confs` as `d["ledger"]`.
- The registration's `home` is a literal repo-relative path
  (`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-13.md:118-129`), and unit 27 S1
  sets it to `.lexicon-debt.txt`.
- The emitter keeps a token-free guard pathspec when the target tracks it
  (`tools/govkit/govkit.py:4383-4392`), so an adopter's rendered manifest carries the root ledger once
  the scaffold has written it, and drops it, by name, before then.
- The class's arms open at `tools/govkit/selftest.py:6139`, on a scratch gov tree whose one kit
  declares `.lexicon.conf`.

### The population

```
out = set()
for d in descriptors:
    for f in [d.config.file] + [t.home for t in d.ledger]:
        if f and "/" not in f: out.add(f)
```

### Inventory

Minted: none.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-27, whose guard row this classes; the close's bar
is the first to run `govkit selfcheck` over both.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2, S3
- `tools/govkit/selftest.py`: the arms of §7

### Alternatives rejected

- **Drop `.lexicon-debt.txt` from the guard**, the report's second route: a ledger-only commit, the
  shape of every drain, then skips the leg whose verdict it moves, the defect the `root-conf` class was
  minted to remove (TOOL-dDerivedDocket-21 S4).
- **A new `[config] files` list or a declared root-data field**: a second place to spell a fact the
  registration's `home` already states.

## 5. Production-readiness checklist

- security — N/A — a classifier over the deployer's own manifest; no write path or surface.
- perf / scale — one pass over the descriptors' ledger tables, a handful of rows.
- error / empty / loading states — a descriptor with no `[[ledger]]` table contributes its conf alone; a
  ledger `home` carrying a `/` is not a root file and stays outside the class.
- observability — 7c's existing line names any pathspec still unclassed, with its leg.
- risks — 7c2 now names a guarded leg whose argv file spells a root ledger it does not guard; that is
  the class's purpose, and on gov's tree no argv file spells the literal after unit 27 S3.
- testing — AC1 to AC3 and the arms of §7.
- migration — none.
- user docs — N/A — govkit's internal check.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys, pathlib; sys.path.insert(0, 'tools/govkit'); import govkit;
  root = pathlib.Path('.'); r = govkit.Report(); print(sorted(govkit.derive_root_confs(
  govkit.read_descriptors(root, govkit.load_registry(root), r))))"` runs after unit 27's pass, it prints
  a list holding `.lexicon-debt.txt` beside `.lexicon.conf`.
  Red when: the population still reads `[config] file` alone.
- **AC2** — When `python <prefix>/govkit/govkit.py selfcheck` runs in a scratch gov tree whose one kit
  declares `[[ledger]]` with `home = ".demo-debt.txt"` and a leg guarding `.demo-debt.txt` and
  `.nosuch.txt`, it prints a `falls into 0 declared classes` line naming `.nosuch.txt` and none naming
  `.demo-debt.txt`.
  Red when: the declared ledger is unclassed, or the undeclared root file is admitted with it.
  fixture: a scratch gov tree under `%TEMP%/<short>` holding one kit, its `kit.toml` declaring the
  ledger home and the guarded leg above, the planted break the ledger rows cut out of
  `derive_root_confs`.
- **AC3** — When the same scratch tree's guarded bar leg has an argv file naming `.demo-debt.txt` and a
  guard without it, the run exits 1 printing `reads root conf .demo-debt.txt`.
  Red when: 7c2's population omits the ledger.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures`

New arm: tools/govkit/selftest.py · covers AC2 AC3 · a scratch kit declaring a root `[[ledger]]` home, its failing case the ledger rows cut out of `derive_root_confs`, under which `.demo-debt.txt` falls into 0 classes · none

## 8. Open questions

- **F1 — How does a root ledger's guard pathspec get a class?** Options: (a) derive the `root-conf`
  population from the conf and the `[[ledger]]` homes; (b) a new declared field listing root data
  files; (c) drop the ledger from the guard. (b) states a fact the registration already states, and (c)
  lets a drain commit skip the leg it moves. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the
  derived population TOOL-dDerivedDocket-21 S4 already uses, extended to the registration's own field.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 22 (HIGH, item H3) of the round-1 audit of
  units 22 to 29.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 30 to 37
  declare toward this unit (TOOL-dMindYourWords-38, TOOL-dMindYourWords-51); no scope, design or criterion moved.

## 10. Reuse audit

The seam is `derive_root_confs` (`tools/govkit/govkit.py:1653-1667`), the derived population check 7c
and 7c2 already read, extended to the factory registration's `home` field; its arms opening at
`tools/govkit/selftest.py:6139` are the fixture this unit extends. `python
tools/codebase-map/reuse_lookup.py "derive a guard pathspec class for a root file a kit declares"`
ranked `repo_root`, `resolve_kit_dir` and `kit_rel`, none of which classes a pathspec, so the existing
function is the one seam that fits. The recall probe surfaced TOOL-aWalkedCorpus-5, the ask the class
was minted to answer for `.lexicon.conf`, and this audit's H3 item.

Recall terms used: `python tools/memory-recall/query.py "how does govkit classify a guard pathspec naming a root file a kit owns" --terms "root-conf guard pathspec class derive_root_confs 7c selfcheck ledger home config file root file"`
