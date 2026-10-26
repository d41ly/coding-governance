# TOOL-dBoundRoles-42 — the retired hook's readers under `memory/` classed, append-only records left as written, and the live-carrier check scoped to what a reader can still be misled by

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 27 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md) | research | TOOL-dBoundRoles-37 TOOL-dBoundRoles-40 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |
| [2026-10-26-build-TOOL-dBoundRoles-64-round6-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-64-round6-fix-return.md) | research | TOOL-dBoundRoles-64 |
| [2026-10-26-prompt-TOOL-dBoundRoles-37-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-37-round1-fix-brief.md) | research | TOOL-dBoundRoles-37 TOOL-dBoundRoles-40 TOOL-dBoundRoles-43 |
| [2026-10-26-prompt-TOOL-dBoundRoles-64-round6-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-64-round6-fix-brief.md) | research | TOOL-dBoundRoles-64 |
| [2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 26 unit specs
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`) confirmed finding **id 42 at
HIGH**, report item **H3**. Id 3 is the same defect at MEDIUM, report item M3, and takes its own scope
item in `TOOL-dBoundRoles-44`.

`TOOL-dBoundRoles-25` AC14 runs
`git grep -l -F 'agent-cap.js' -- ':!memory/builds' ':!memory/ledger' ':!.governance/steps'` and admits
only `tools/hooks/kit.toml`, govkit's self-test module, the step program and govkit's fixtures. At base it
also prints 25 files under `memory/` that unit 25's S8 never disposes: `memory/DECISIONS.md`, the
archive's decision log and seven template snapshots, `memory/backlog/TOOL.md`, five gotcha pages, two
rendered guides, three map dossiers, four generated map files and `memory/project/spec-token-waivers.txt`.
`tools/check-dead-paths.sh` calls those records append-only and says rewriting one would falsify it, so
the only way to green AC14 as written is to falsify them.

This unit gives every `memory/` reader a class and a disposition, leaves every append-only record as
written, and restates AC14's live-carrier check over the population the dead-path leg itself grades, with
the step's own spellings declared where that leg reads its exceptions. It repairs `TOOL-dBoundRoles-25`
and builds one step after it (order 27).

## 2. Scope (IN)

- **S1** — The classes. The pass derives, at its own base, every file
  `git grep -l -F 'agent-cap.js' -- memory ':!memory/builds' ':!memory/ledger'` prints, and gives each one
  class of §4 "The classes" in its acceptance ledger. A file no class takes stops the unit and is returned
  to the main loop. Observed by AC1.
- **S2** — Append-only records stay as written. `memory/DECISIONS.md`, every file under `memory/archive/`,
  every shard under `memory/backlog/`, and everything under `memory/builds/` and `memory/ledger/` keep
  their bytes: this pass's diff and unit 25's touch none of them. Observed by AC2.
- **S3** — The generated map is regenerated, never edited. `memory/map/generated/CARDS.md`, `MAP.md`,
  `inventories.json` and `symbols.json` are rewritten by `python tools/codebase-map/gen_map.py --write` over
  the tree unit 25 leaves. A name still in them after that is a live source file's spelling, answered by
  that file's own disposition. Observed by AC3.
- **S4** — The live-carrier check, restated. Outside `memory/`,
  `git grep -l -F 'agent-cap.js' -- ':!memory' ':!.governance/steps'` prints only `tools/hooks/kit.toml`,
  `tools/govkit/steps/spawn_guard_pack.py`, `tools/govkit/selftest.py` and files under
  `tools/govkit/fixtures`. Under `memory/`, only the files S1 classes print, each in a class whose
  disposition is done. Observed by AC4.
- **S5** — The admitted spellings are declared where the dead-path leg reads its exceptions. Each line of
  `tools/hooks/kit.toml`, `tools/govkit/steps/spawn_guard_pack.py` and `tools/govkit/selftest.py` that
  `bash tools/check-dead-paths.sh --list` prints for the needles `agent-cap.js` and `agent-cap.test.sh`
  once the files are gone gets one row in `tools/dead-path-waivers.txt`, in that file's
  `<path>\t<ordinal>\t<line-text>\t<reason>` grammar, the reason "the upgrade step names the file it
  retires". So does each line of a before-image the step wrote under `.governance/steps/` in gov's tree,
  the reason "a before-image records the bytes the step replaced". Observed by AC5.
  **Readers:** by name: `tools/hooks/kit.toml` and `tools/govkit/selftest.py`, whose spellings this item
  keeps; `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`, whose rows id 26's item writes; every
  other reader unit 25 S8 lists and disposes; READER NOT IN TREE: the step program and its before-images,
  which unit 25 adds after base · by value: `tools/check-dead-paths.sh:85`, which reads
  `tools/dead-path-waivers.txt` and reds a needle line no row waives.

## 3. Non-goals (OUT)

- The gotcha pages and the frozen receipt fixture, `TOOL-dBoundRoles-44`'s items for ids 43 and 26, and
  the test-suite count waiver and the spec-token waiver rows for `tools/hooks/`, `TOOL-dBoundRoles-43`'s
  for ids 44 and 45. S1 classes those files and points at those items.
- Re-deriving unit 25's reader list against its S8 and recording the difference: `TOOL-dBoundRoles-44`'s
  items for ids 3 and 26.
- Rewording `TOOL-dBoundRoles-25` AC14. Its builder answers AC14 in unit 25's ledger in the AMENDED form,
  naming this unit's S4 as the population.
- The report's left-shift spec-lint over every AC's literal grep. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dBoundRoles-25` — the deletion of `tools/hooks/agent-cap.js` and its suite, S8's reader dispositions and AC14, whose population S4 restates (id 42)
- **hands-off** `TOOL-dBoundRoles-43` — S1's class table, whose registry rows id 44's and id 45's items dispose (ids 44 and 45)
- **hands-off** `TOOL-dBoundRoles-44` — S1's class table, whose gotcha and fixture rows id 43's and id 26's items dispose, and whose memory half id 3's item re-derives (ids 3, 26 and 43)
- **hands-off** `TOOL-dBoundRoles-50` — AC4's pathspec, S5's waived lines and the spawn-idiom registry, which unit 50 completes; this unit's ledger answers AC4 AMENDED, naming unit 50 (ids 27, 28, 33 and 37 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-51` — S2's clause, AC2 and the class table's `memory/guides/MERGE-BAR.md` row, which unit 51 observes per record class; this unit's ledger answers AC2 AMENDED, naming unit 51, and classes that guide live, edited in place (ids 7, 13 and 14 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-58` — AC2 and AC4, which unit 58 bumps with the text units 51 and 50 answer them by (id 48 of the round-1 audit of units 45 to 51)

## 4. Design

### Evidence

Re-run on this node on 2026-10-26 at base `462d20f3`, AC14's grep filtered to `memory/` printed 25 files.
`memory/project/spec-token-waivers.txt:29` names `.claude/hooks/agent-cap.js`, the copy
`TOOL-dRetiredFork-14` and `-21` removed, and waives it for `aDeclaredBound-4` AC10. `tools/check-dead-paths.sh`
greps the tree minus `memory/`, plus `memory/map/features/*` and `memory/gotchas/*`, and its header rules
that a record naming a file deleted after it was written is correct, not stale.

### The classes

| Class | Files at base | Disposition |
|---|---|---|
| append-only record | `memory/DECISIONS.md`, `memory/archive/DECISIONS.2026-08-10.md`, `memory/archive/parallel-coding-governance.template-v-2-1.md` to `-7.md`, `memory/backlog/TOOL.md` | historical, unchanged (S2) |
| rendered guide | `memory/guides/MERGE-BAR.md`, `memory/guides/REVIEW-PROTOCOL.md` | re-rendered from its template by unit 25 S8 |
| map dossier | `memory/map/features/agent-cap.md`, `review-harnesses.md`, `unattended.md` | rewritten by unit 25 S8's dossier row |
| generated map | `memory/map/generated/CARDS.md`, `MAP.md`, `inventories.json`, `symbols.json` | regenerated (S3) |
| gotcha page | the five pages under `memory/gotchas/` | `TOOL-dBoundRoles-44`, id 43 |
| registry | `memory/project/spec-token-waivers.txt` | row 29 unchanged: it waives the `.claude/hooks/` copy, which this unit does not touch; new rows are id 45's |

The table is the base population. S1 re-derives it at the build run's base and records the result.

### Inventory

Minted: the waiver rows of S5 and their two reason strings. No function, constant, plant or file.

### Migration

None: no stored data changes beyond the regenerated renders.

### Rollout

Live at landing, at order 27, after unit 25 and before `TOOL-dBoundRoles-43` and `-44` at orders 28 and 29.

### Files touched (estimate)

- `tools/dead-path-waivers.txt`
- `memory/map/generated/CARDS.md`
- `memory/map/generated/MAP.md`
- `memory/map/generated/inventories.json`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **List every record path as AC14's expected output.** It types a population the class rule already
  derives, and the list goes stale with the next record that names the file.
- **Edit the records to drop the name.** The dead-path gate's header rules that this falsifies them.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — one grep at the pass and one map regeneration.
- error / empty / loading states — a `memory/` file of no class stops the unit (S1).
- observability — the ledger records every file's class.
- risks — a waiver row keyed to a line the step later edits reds as stale, which `check-dead-paths.sh`
  reports by row.
- testing — AC1 to AC5 by grep, diff and the checker's `--list`; the bar at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `git grep -l -F 'agent-cap.js' -- memory ':!memory/builds' ':!memory/ledger'` runs at the
  pass's base, every file it prints has a class line in this unit's acceptance ledger.
  Red when: a `memory/` reader is left with no disposition, so AC14 stays red with no route.
  figure: the population is DERIVED at the pass; the table's 25 is PINNED at `462d20f3`.
- **AC2** — When `git diff --quiet <unit 25's parent sha> HEAD -- memory/DECISIONS.md memory/archive memory/backlog`
  runs after this pass, it exits 0.
  Red when: an append-only record is edited to clear a grep.
- **AC3** — When `python tools/codebase-map/gen_map.py --write` runs again on the built tree, `git status
  --porcelain memory/map/generated` prints nothing.
  Red when: a generated map file was edited by hand or left stale.
- **AC4** — When `git grep -l -F 'agent-cap.js' -- ':!memory' ':!.governance/steps'` runs on the built
  tree, it prints only `tools/hooks/kit.toml`, the step program unit 25 adds under the govkit steps
  folder, govkit's self-test module (S4 names its path) and paths under `tools/govkit/fixtures`.
  Red when: a live reader outside `memory/` still names the deleted file.
- **AC5** — When `bash tools/check-dead-paths.sh --list` runs on the built tree, every line it prints for
  the retired hook's two basenames in the three files of S5 or under the steps folder of `.governance` is
  marked waived.
  Red when: a spelling the step must keep reds the dead-path leg with no declared row.

## 7. Gates

`dead-path carriers (deleted files still named)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 25 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How is AC14's admitted set declared?** Options: (a) dead-path waiver rows for the step's own
  spellings, so the leg that grades the same population reads the exceptions; (b) the list typed in an
  acceptance criterion alone. (b) leaves the dead-path leg red on the step's files the moment the hook is
  deleted, which is a gate already in the bar. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  most feature-rich survivor, tie-broken by reuse of the waiver registry the leg owns. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 26 unit specs, id 42
  (HIGH, item H3; id 3 shares the defect at MEDIUM, item M3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dBoundRoles-50 and -51, the minors batches of the round-1 audit of units 37 to 44; they name AC2's and AC4's AMENDED answers. Nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-58, the minors batch of the round-1 audit of units 45 to 51; nothing else moved.

## 10. Reuse audit

The seams are the dead-path gate's population rule and its waiver registry (`tools/check-dead-paths.sh`,
header; `tools/dead-path-waivers.txt`, whose rows 55-58 already declare the frozen receipt's dead
lexicon path), and `tools/codebase-map/gen_map.py --write` for the generated map.
`python tools/codebase-map/reuse_lookup.py "classify files a deleted path is still named in as live or historical record"`
ranked `live`, `records`, `classify` and `build_spec_path_re`, none a carrier classifier, so no existing
seam fits beyond the gate named, whose population is the live-carrier rule.

Recall terms used: `python tools/memory-recall/query.py "which memory files may name a deleted hook and which are append-only records" --terms "dead-path carriers append-only records memory gotchas map dossiers generated agent-cap retired readers waiver"`
