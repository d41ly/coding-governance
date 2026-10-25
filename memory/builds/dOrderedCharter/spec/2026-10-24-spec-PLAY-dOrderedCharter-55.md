# PLAY-dOrderedCharter-55 — the round-2 spec audit's 31 minors: criteria observed where they can pass, one reader per fact, and seams that hold in any order

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 41 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-46-mark-rewrap-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-46-mark-rewrap-return.md) | research | PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-53 |
| [2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md) | research | PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-54 |
| [2026-10-24-build-PLAY-dOrderedCharter-55-deviation-551.md](../build/2026-10-24-build-PLAY-dOrderedCharter-55-deviation-551.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-55-deviation-552.md](../build/2026-10-24-build-PLAY-dOrderedCharter-55-deviation-552.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 |
| [2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 |
| [2026-10-25-build-PLAY-dOrderedCharter-55-deviation-553.md](../build/2026-10-25-build-PLAY-dOrderedCharter-55-deviation-553.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-54 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit of this build's promoted units
(`memory/builds/dOrderedCharter/reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md`) exited
with 36 confirmed findings; its five highs are units 50 to 54. This unit is BUILD-METHOD M4's batch of
the rest, every MEDIUM and LOW, each report id its own §2 item. The minors land on units 39 to 49, so
this unit is ordered above every unit, and each item names the part of a spec it supersedes; the
repaired spec's §3 names this unit as the hand-off for the part. Where a minor is a criterion observed
too early, the item moves its observation to the pass that makes it passable, and the repaired unit's
§3 carries that rule to its builder.

The report's items and their ids, MEDIUM as M and LOW as L: M1 1 · M2 2 · M3 3 · M4 4 · M5 5, 12 ·
M6 6 · M7 7 · M8 8 · M9 10, 22 · M10 11 · M11 14 · M12 15 · M13 16 · M14 19 · M15 20 · M16 24 · M17 26 ·
M18 28 · M19 31 · M20 32 · M21 34 · M22 37 · M23 40 · M24 41 · L1 9 · L2 17 · L3 18 · L4 29 · L5 35.
Scope items S1 to S31 take these ids one each, grouped by the unit they land on; each item names its
id, and S<n>'s criterion is AC<n>.

The fixes the skeptic judged unsound (ids 1, 2, 3, 4, 6, 28, 29, 31 and 32) are built from the
skeptic's corrected fix, as the report states it.

## 2. Scope (IN)

### Order and observation

- **S1** — id 1. `PLAY-dOrderedCharter-39` S3's probe reads the adopter's argument `case` from `<D>^`,
  `D` the commit `git log --diff-filter=D -1` names for
  `tools/agent-instructions/adopt-agent-instructions.sh`, through `tree_lib.read_blobs_at`
  (`tools/memory-tree/tree_lib.py:328`), so it runs at unit 39's own pass after unit 31 deleted the
  directory, and reads `--card` there. Unit 39 S2's names go in unit 39's own pass trailer. The wiring
  leg's rows unit 31 removed are re-written at unit 39's pass as `PLAY-dOrderedCharter-50`'s probe
  names them. This supersedes unit 39 S3's "Before the directory leaves" and S2's "Unit 31's
  retirement names". Observed by AC1.
  **Readers:** by name: the adopter is unit 31's retirement, and this item reads it at D's parent; a grep
  for adopt-agent-instructions outside memory/builds and memory/backlog finds `.memory-tree.conf`,
  `tools/gate-legs.json`, `tools/govkit/registry.toml`, `tools/agent-instructions/kit.toml`,
  `tools/agent-instructions/README.md`, `tools/agent-instructions/adopt-agent-instructions.test.sh`,
  `memory/project/spawn-idiom-sites.txt`, `memory/project/testsuite-count-waivers.txt`,
  `memory/project/unarmed-branches.txt` and `memory/map/generated/symbols.json`, each unit 31's to
  re-point or delete. by value: the adopter's options, read by `tools/gate-legs.json:296` and
  `tools/agent-instructions/kit.toml:44`, which S12's table maps.
- **S2** — id 2. Every criterion `PLAY-dOrderedCharter-49` S16 to S24, S60, S61, S69 and S71 corrects
  is observed at unit 49's pass, never at the repaired unit's: unit 18 AC1, AC3 and AC7; unit 1 AC1 and
  AC7; unit 5 AC3; unit 30 AC6; the pathspecs of unit 2 AC7, unit 6 AC7, unit 28 AC3, unit 31 AC12,
  unit 34 AC11, unit 35 AC14 and unit 36 AC11 and AC12; unit 12 AC1 and AC5; unit 26 AC10. The repaired
  unit's pass changes no code to satisfy that criterion, and its acceptance ledger line takes the
  OBSERVED form from the observation made at unit 49's pass, naming that pass. Observed by AC2.
- **S3** — id 3. Unit 1's pass lands no `legacy` key on the `cross-os` `[[block]]` row, so unit 1's AC4
  holds at its own pass; `PLAY-dOrderedCharter-41` S1's "Where unit 1 landed the key, this unit takes
  it off the row" is superseded. Unit 37's AC1 and AC8 are observed at `PLAY-dOrderedCharter-40`'s
  pass, by S2's ledger rule. Observed by AC3.
- **S4** — id 4. The index after units 10 and 44 equals a cold build whichever lands first at order 5:
  a plant `register-before-ledger` builds an index under unit 19's blob-only rule with unit 10's
  extractors registered, then opens it under unit 44's stamp and `PLAY-dOrderedCharter-51`'s keys.
  Observed by AC4.

### One source per fact

- **S5** — id 5. `PLAY-dOrderedCharter-40` AC1 filters `x.origin == 'playbook-render'`, the `id =`
  `tools/playbook/kit.toml:7` declares, which unit 9 S2 derives as the origin. Observed by AC5.
- **S6** — id 12. `read_units` asserts each row's `origin` equals the `id =` of the `kit.toml` beside
  its manifest, never the directory name, and a fixture whose directory name differs from its kit id
  shows the id. Observed by AC6.
- **S7** — id 6. `tools/playbook/edge_checks.py`, which unit 25 builds at order 10, is deleted at this
  pass with every row `PLAY-dOrderedCharter-50`'s probe names for it, and both `--only` arms of
  `gov_tag.py check` call unit 24's `check_edges`. Unit 49's AC32 is observed at this pass. This
  supersedes unit 49 S41's "is not built". Observed by AC7.
  **Readers:** by name: READER NOT IN TREE — edge_checks.py is built at unit 25's pass (order 10), and
  a grep for edge_checks outside memory/builds finds no reader today; at this pass its readers are unit
  25's leg row in tools/gate-legs.json and the two --only arms of gov_tag.py check, which this item
  re-points. by value: NO VALUE READERS — both arms keep their verdicts, computed by unit 24's
  `check_edges`.
- **S8** — id 7. The record factory's per-kind table admits a declared-pending entry,
  `{"pending": "<unit id>"}`, for a kind whose fields a later unit owns; `new <kind>` on a pending kind
  exits 2 naming that unit, and unit 42 S2's key equality counts a pending entry. Unit 42's pass enters
  the override and change kinds as pending on units 2 and 15. Observed by AC8.
- **S9** — id 8. Unit 49 S11's census step re-renders with `--overlay-from` naming the overlay it has
  just written (`PLAY-dOrderedCharter-46` S3 and S4), so the charter carries the census units before
  any commit. Unit 49's pass builds it, since `step-rows-frozen` freezes that step's program at unit
  49's landing (TOOL-dSafePassage-1 S9); this pass observes AC9 and changes no code for it.
  Observed by AC9.
- **S10** — id 10. Unit 39's retirement deletes `memory/map/baseline.toml`'s `agent-instructions
  self-test` line (`:14`); the `agent-instructions wiring` line (`:15`) stays with no dossier claim, or
  leaves in the commit where `memory/map/features/playbook.md` claims the key. `codebase-map coverage +
  freshness` joins unit 39's gates. Observed by AC10.
  **Readers:** by name: a grep for agent-instructions self-test finds `memory/map/baseline.toml:14`,
  `memory/map/generated/MAP.md:16`, `memory/map/generated/inventories.json:9`,
  `tools/gate-legs.json:382`, `tools/govkit/registry.toml:523`, `tools/govkit/subject-pins.tsv:16`,
  `tools/run-gates/ceiling-evidence.txt:32` and `tools/run-gates/selftest-budgets.txt:52`, each leaving
  with the leg in unit 39's commit as unit 50's owed-rows probe names it. by value:
  `codebase-map coverage + freshness`, whose coverage join reads the baseline line.
- **S11** — id 22. The generated map, `memory/map/generated/MAP.md` and
  `memory/map/generated/inventories.json`, is re-rendered in that commit, so no generated file names
  the retired self-test leg. Observed by AC11.
  **Readers:** by name: `memory/map/generated/MAP.md:16` and `memory/map/generated/inventories.json:9`,
  the two generated lines that grep finds. by value: `tools/codebase-map/gen_map.py`, which renders
  both from `memory/map/baseline.toml`.
- **S12** — id 11. Unit 39 S3's probe is keyed on behaviour: a table maps each adopter option to the
  renderer argv replacing it (`--check` to `--check-render --scope entry-files`, `--aliases` to that
  scope's alias source, `--card` to `--card`), each option either mapped or named retired, and the
  pass trailer carries the table. This supersedes S3's "finds it among the options
  `render_playbook.py --help` prints". Observed by AC12.
  **Readers:** by name: a grep for the adopter's options finds the parser
  `tools/agent-instructions/adopt-agent-instructions.sh:37-39`, the `agent-instructions wiring` argv
  `tools/gate-legs.json:296` and the kit's argv rows `tools/agent-instructions/kit.toml:37` and
  `tools/agent-instructions/kit.toml:54`. by value: the wiring leg's `--aliases` value `claude`, read
  by `tools/gate-legs.json:296`, which the table maps to the entry-files scope's alias source.

### The index (units 44 and 51)

- **S13** — id 14. The build summary counts extractor runs per worktree version, and a plant
  `three-versions` builds three worktrees of three extractor versions round-robin twice, the second
  round reporting `0 extractor runs` in each. Observed by AC13.
- **S14** — id 16. Unit 49 AC26 runs `handoff.py render` with `--build <slug> --unit <id>`, which
  `tools/roles/handoff.py:934` requires and `help/roles.md:36` spells; it is observed at this pass.
  Observed by AC14.
- **S15** — id 19. An extractor's version is the first 12 hex characters of the SHA-256 over its
  module's bytes and every module of its import closure, in path order, the closure from unit 16's
  `import_walk.derive_import_closure`, reached through `resolve_kit_dir`. A plant `helper-edit` edits a
  module the extractor imports. This supersedes unit 44 S3's module-only hash and its §5 risk line.
  Observed by AC15.
- **S16** — id 31. A schema mismatch rebuilds in place inside one `BEGIN IMMEDIATE` transaction,
  dropping and recreating the tables and setting `user_version`, never unlinking the file; the file is
  named `<git-common-dir>/gov/index-s<INDEX_SCHEMA>.db`, so two schemas never share one. A plant
  `held-open` holds a reader open across the rebuild. This supersedes unit 44 S4's "starts the file
  again" and its Flow step 1. Observed by AC16.
- **S17** — id 32. An extractor removed from or renamed in the registry has no row served: unit 51 S3's
  filter is over the reading worktree's current registry, and unit 51 S5 collects only versions no live
  registry names. A plant `extractor-removed` compares the filtered dump with a cold build's.
  Observed by AC17.
- **S18** — id 18. Unit 10's registration after a stamped index re-runs only its own extractors: the
  plant `ten-after-ledger` registers unit 10's eight namespaces over an index unit 44 stamped and
  reports runs for those extractors alone. Observed by AC18.

### The overlay, the lock and the dirty rows

- **S19** — id 20. `read_overlay(root)` reads `HEAD:.governance/instructions.toml` through
  `tree_lib.read_blobs_at(root, [("HEAD", path)])`, reached through `resolve_kit_dir("memory-tree",
  "tree_lib.py", here)`; a `None` answer at a born `HEAD` is the absent state. This supersedes
  `PLAY-dOrderedCharter-46` S1's "through `git cat-file`". Observed by AC19.
- **S20** — id 40. The playbook adopter writes the `.governance/instructions.lock merge=ours` line into
  every target that holds a lock, and wires `merge.ours.driver true` as `bash tools/check-wiring.sh
  --fix` does for gov (`.gitattributes:82-83`); `lock --check` names the re-render as the remedy for a
  merge outside the lander. Unit 49 AC24 gains a scratch-repository merge. Observed by AC20.
- **S21** — id 41. A dirty row's worktree key is the path `git rev-parse --show-toplevel` prints,
  slashes forward and the drive letter lower-cased, compared with `git worktree list --porcelain`'s
  `worktree` lines after the same normalisation; unit 49 S50's stale-path drop runs before the
  caller's own write. Observed by AC21.

### The merge table class (units 45 and 52)

- **S22** — id 34. Chunks are compared and emitted with line terminators folded to the file's
  dominant terminator from `_dominant` (`tools/memory-tree/merge-rows.py:742`, site 6), the folded
  comparison deciding both "changed" and "same bytes", and a missing final terminator supplied before a
  chunk is appended. Unit 45 S4's byte identity holds modulo the terminator. Observed by AC22.
- **S23** — id 35. `main()` (`tools/memory-tree/merge-rows.py:1538-1552`) gains an `except
  TableConflict` arm before the generic one, writing the body through `write_conflict_body` with the
  label `theirs (conflicting: <keys>)` and printing the keys after the body is written, as the
  `ViewShardRefused` arm does. Observed by AC23.

### The positional check (units 47, 48 and 53)

- **S24** — id 15. A spec under `memory/builds/*/spec/` added before the check and rev-bumped after it
  is graded on every line the bump wrote, by `PLAY-dOrderedCharter-53`'s per-line rule; a plant
  `positional-spec-revbump` appends `x.py:3` to such a spec. Observed by AC24.
- **S25** — id 37. A bulk move of records after the check, renamed with a line edited in each, keeps
  each untouched line grandfathered and grades each edited one; a plant `positional-bulk-move` moves
  three records from `build/` to `reviews/` in one commit. This supersedes unit 47 §5's rename-silent
  risk line. Observed by AC25.
- **S26** — id 28. The positional plants of units 47, 48 and 53 run in `tags positional selftest`, the
  suite unit 26 S7 mints for the positional population, as well as under `playbook render selftest`,
  and unit 19's `tags (the resolver's checks)` leg grades their limbs over the tree. Observed by AC26.

### This build's specs and legs

- **S27** — id 24. `PLAY-dOrderedCharter-49`'s spec is brought under the live-spec cap
  `budgets."memory/builds/*/spec/"`, 49152 bytes CR-stripped, read through `budgets.py resolve`
  (TOOL-dGroundRules-9 S2), by a revision that cuts the items units 50 and
  55 supersede to one-line pointers, every id, criterion and fork kept (§8 F2). Observed by AC27.
- **S28** — id 26. The adopter population of the moved `agent-instructions wiring` leg is recorded:
  the `playbook-render` entry's leg set gains it for every adopter, and `govkit apply` over a fixture
  target selecting `playbook-render` without `agent-instructions` shows the leg in its manifest
  (§8 F3). This supersedes unit 39 F2's `widens: none`. Observed by AC28.
- **S29** — id 9. Unit 41 AC4 asserts on the line: the line holding "minor behind" also says "no
  reseed note", and no line of `render_playbook.py` or the charter page says a minor-older template
  gets one. Observed by AC29.
- **S30** — id 17. `playbook render selftest`'s guard (`tools/gate-legs.json:1678-1681`) gains
  `{prefix}/govkit/entries/playbook.kit.toml` and `coding-governance-agents.template.md`, the inputs
  unit 41's arm stages its failing case in. Observed by AC30.
- **S31** — id 29. Unit 20's `instruction render (one renderer of record)` leg carries `--card` in
  gov's manifest, set by `PLAY-dOrderedCharter-43` S4, and checks every scope; units 43 and 39 name
  it as the leg S4 edits. Observed by AC31.

## 3. Non-goals (OUT)

- Any high of the same audit: units 50 to 54.
- Re-ordering any unit: the orders stand, and where a minor is a criterion observed too early, the
  item moves the observation and the repaired unit's §3 carries the rule.
- Changing a repaired unit's clause or carries line.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-1` — its AC1, AC4 and AC7 (S2, S3)
- **consumes-from** `PLAY-dOrderedCharter-2` — its AC7 pathspec (S2)
- **consumes-from** `PLAY-dOrderedCharter-5` — its AC3 (S2)
- **consumes-from** `PLAY-dOrderedCharter-6` — its AC7 pathspec (S2)
- **consumes-from** `PLAY-dOrderedCharter-9` — `read_units` and the origin it derives (S5, S6)
- **consumes-from** `PLAY-dOrderedCharter-12` — its AC1 and AC5 (S2)
- **consumes-from** `PLAY-dOrderedCharter-16` — `import_walk.derive_import_closure` (S15)
- **consumes-from** `PLAY-dOrderedCharter-18` — its AC1, AC3 and AC7 (S2)
- **consumes-from** `PLAY-dOrderedCharter-19` — the index, its fixture and the dirty rows (S4, S16, S21)
- **consumes-from** `PLAY-dOrderedCharter-20` — the renderer-of-record leg (S31)
- **consumes-from** `PLAY-dOrderedCharter-25` — `edge_checks.py`, which S7 deletes
- **consumes-from** `PLAY-dOrderedCharter-26` — its AC10 and `tags positional selftest` (S2, S26)
- **consumes-from** `PLAY-dOrderedCharter-28` — its AC3 pathspec (S2)
- **consumes-from** `PLAY-dOrderedCharter-30` — its AC6 (S2)
- **consumes-from** `PLAY-dOrderedCharter-31` — its AC12 pathspec and the deletion S1 reads before (S1, S2)
- **consumes-from** `PLAY-dOrderedCharter-34` — its AC11 pathspec (S2)
- **consumes-from** `PLAY-dOrderedCharter-35` — its AC14 pathspec (S2)
- **consumes-from** `PLAY-dOrderedCharter-36` — its AC11 and AC12 pathspecs (S2)
- **consumes-from** `PLAY-dOrderedCharter-37` — its AC1 and AC8 (S3)
- **consumes-from** `PLAY-dOrderedCharter-39` — the kept leg, its probe and its retirement rows (S1, S10, S11, S12, S28, S31)
- **consumes-from** `PLAY-dOrderedCharter-40` — its AC1 filter and unit 37's observation point (S3, S5)
- **consumes-from** `PLAY-dOrderedCharter-41` — the live `cross-os` block and its AC4 (S3, S29, S30)
- **consumes-from** `PLAY-dOrderedCharter-42` — the per-kind table (S8)
- **consumes-from** `PLAY-dOrderedCharter-43` — the card option on the renderer-of-record leg (S31)
- **consumes-from** `PLAY-dOrderedCharter-44` — the ledger, the version and the schema stamp (S4, S13, S15, S16, S18)
- **consumes-from** `PLAY-dOrderedCharter-45` — the table class (S22, S23)
- **consumes-from** `PLAY-dOrderedCharter-46` — `read_overlay` and the candidate read (S9, S19)
- **consumes-from** `PLAY-dOrderedCharter-47` — `L` and the grandfathered print (S24, S25, S26)
- **consumes-from** `PLAY-dOrderedCharter-48` — the producers limb's plants (S26)
- **consumes-from** `PLAY-dOrderedCharter-49` — the census step, AC24, AC26, AC32, S50 and its own size (S2, S7, S9, S14, S20, S21, S27)
- **consumes-from** `PLAY-dOrderedCharter-50` — the owed-rows probe (S1, S7)
- **consumes-from** `PLAY-dOrderedCharter-51` — the per-version tables and the read filter (S4, S13, S17)
- **consumes-from** `PLAY-dOrderedCharter-52` — `TABLE_ENVELOPE` (S22, S23)
- **consumes-from** `PLAY-dOrderedCharter-53` — the per-line grandfather verdict (S24, S25)

## 4. Design

### Evidence

Read at `ce13efbe`; each finding's evidence is the report's appendix row, and the code citations in §2
were re-read at that base: `tools/roles/handoff.py:934` (`--build` required on `render`),
`tools/playbook/kit.toml:7` (`id = "playbook-render"`), `memory/map/baseline.toml:14-15` (both
agent-instructions legs), `tools/agent-instructions/adopt-agent-instructions.sh:36-40` (`--source`,
`--aliases`, `--mode`, `--check`, `--force`), `tools/memory-tree/tree_lib.py:302` and `:328`, the
merge driver's `_dominant` (`:742`) and `main()` (`:1538-1552`), `.gitattributes:82-83` and
`tools/gate-legs.json:1678-1681`. The acceptance ledger's two forms, OBSERVED and AMENDED, are
`memory/HYGIENE.md`'s "Acceptance ledger" section; S2 uses the first.

### Order

Order 41, above every unit: the minors land on eleven units, the latest of them unit 49 at order 39,
and unit 54 sits at 40. Items that change what an earlier pass does (S1, S2, S3, S8, S9, S12) reach that
pass through the repaired spec's §3 hand-off to this unit, which its builder reads; this unit's pass
observes them.

### Inventory

Minted: the pending entry `{"pending": "<unit id>"}`; the plants `register-before-ledger`,
`three-versions`, `helper-edit`, `held-open`, `extractor-removed`, `ten-after-ledger`,
`positional-spec-revbump` and `positional-bulk-move`; the file name `index-s<INDEX_SCHEMA>.db`; the
merge label `theirs (conflicting: <keys>)`. Naming cells: `lexicon naming predicates` grades the
Python names.

### Files touched (estimate)

- `tools/playbook/render_playbook.py`
- `tools/playbook/tag_index.py`
- `tools/playbook/gov_tag.py`
- `tools/playbook/instruction_units.py`
- `tools/playbook/overlay.py`
- `tools/playbook/positional.py`
- `tools/playbook/instructions_edit.py`
- `tools/playbook/adopt-playbook.sh`
- `tools/playbook/kit.toml`
- `tools/playbook/edge_checks.py` (deleted)
- `tools/govkit/subject-pins.tsv`
- `tools/govkit/registry.toml`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/merge-rows.py`
- `tools/memory-tree/merge-rows.test.sh`
- `tools/gate-legs.json`
- `memory/map/baseline.toml`
- `memory/map/generated/MAP.md`
- `memory/map/generated/inventories.json`
- `.gitattributes`
- `memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md` (S27)

### Rollout

Live at landing. Its write set meets units 44, 45, 46, 47, 49, 51, 52 and 53, so it runs last and
alone, save S27, which §8 F2 places.

### Alternatives rejected

- **Folding each minor into its unit's spec**: the exit promotes and never folds (BUILD-METHOD M4).
- **Two batches**: no split gives two disjoint write sets; the index, positional and merge items all
  meet `tools/playbook/gov_tag.py` or `tools/memory-tree/merge-rows.py` across halves.

## 5. Production-readiness checklist

- security: S20 writes one attribute line and one config key per adopter target, both the existing
  gov wiring; nothing widens a write surface.
- perf / scale: S15 hashes an import closure once per build; S16 rebuilds in place once per schema.
- error / empty / loading states: S8's pending kind refuses `new` naming its unit; S16's rebuild holds
  the write lock; S23 names every conflicting key.
- observability: S13's per-version counts; S23's label.
- risks: S27 edits a spec that is closed once unit 49 lands, which §8 F2 resolves; S28 widens the
  `playbook-render` leg set, recorded there.
- testing: AC1 to AC31, each a probe or a plant of the repaired unit's own fixture.
- migration: S16's file name moves every node's index once; S20 takes effect on the next merge.
- user docs: S20's remedy line; unit 37's page for the lock names the attribute.

## 6. Acceptance criteria

- **AC1** — When `git show <D>^:tools/agent-instructions/adopt-agent-instructions.sh` runs, `D` from
  `git log --diff-filter=D -1`, the probe's table names every case arm, `--card` among them, and unit
  39's pass trailer names `check_card_import`.
  Red when: the probe reads a deleted file and certifies nothing.
- **AC2** — When `git grep -n "PLAY-dOrderedCharter-49" -- memory/builds/dOrderedCharter/build/` runs
  after the build, each criterion S2 lists has an OBSERVED ledger line naming unit 49's pass.
  Red when: a repaired unit observes a criterion that only unit 49 makes passable.
- **AC3** — When `python -c "import tomllib,sys; print([b for b in tomllib.load(open(sys.argv[1],'rb'))['block'] if b.get('id')=='cross-os'])" tools/govkit/entries/playbook.kit.toml`
  runs, the row carries no `legacy` key, and `render_playbook.py --check` exits 0 over gov.
  Red when: unit 1 lands `legacy` and unit 1's AC4 refuses.
- **AC4** — When `python gov_tag.py --fixture --plant register-before-ledger` runs, the dump equals
  a cold build's.
  Red when: extractors registered before the ledger read a stale population.
- **AC5** — When unit 40's corrected AC1 probe, filtering `x.origin == 'playbook-render'`, runs, it
  prints the four reference tags.
  Red when: the filter names a directory, not the kit id.
- **AC6** — When `read_units` reads a fixture kit whose directory is `pbk` and whose `id` is
  `playbook-render`, each row's `origin` is `playbook-render`.
  Red when: origin follows the directory name.
- **AC7** — When `git ls-files -- '*edge_checks.py'` runs, it prints nothing, and both `--only` arms red
  one planted edge as unit 28's leg does.
  Red when: a second checker of one predicate remains.
- **AC8** — When `python build_records.py --fixture --plant pending-kind` runs, the module imports
  with a pending entry, and `new` on that kind exits 2 naming its unit.
  Red when: a field-less kind blocks the import, or invents fields.
- **AC9** — When unit 49 S11's step's up runs in a fixture and `render_playbook.py` reads the charter before
  any commit, the census unit's line is present.
  Red when: a render after the census write drops the moved lines.
- **AC10** — When `git grep -n "agent-instructions" -- memory/map/baseline.toml` runs after unit 39's
  pass, it prints no self-test line, and the wiring key is baselined or claimed, never both.
  Red when: the coverage leg reds a stale or doubly-held key.
- **AC11** — When `git grep -n "agent-instructions self-test" -- memory/map/` runs, it prints nothing.
  Red when: a generated map names a retired leg.
- **AC12** — When the probe runs with the `entry-files` scope removed from a scratch copy of
  `render_playbook.py`, it reds on `--check`.
  Red when: an option counts as carried by its spelling alone.
- **AC13** — When `python gov_tag.py --fixture --plant three-versions` runs, each worktree's second
  build reports `0 extractor runs`.
  Red when: round-robin builds re-parse the shared population.
- **AC14** — When `python tools/roles/handoff.py render --role gov-builder --build dOrderedCharter --unit PLAY-dOrderedCharter-55 --input code=<file> --stdout`
  runs, it prints a `### input:code` block.
  Red when: argparse exits 2 for a missing required flag.
- **AC15** — When `--plant helper-edit` runs, the build after the helper edit re-runs the extractor.
  Red when: a helper edit leaves stale rows on a warm index.
- **AC16** — When `--plant held-open` runs a schema rebuild with a reader holding the file, the rebuild
  completes, no rows vanish, and the index file is named `index-s<n>.db`.
  Red when: the rebuild unlinks a held file.
- **AC17** — When `--plant extractor-removed` runs, the filtered dump equals a cold build's.
  Red when: a deregistered extractor's rows are served.
- **AC18** — When `--plant ten-after-ledger` runs, the summary lists runs for unit 10's extractors only.
  Red when: a registration re-runs every extractor.
- **AC19** — When `git -C tools/playbook grep -n "cat-file" -- overlay.py` runs, it prints nothing.
  Red when: a second `<rev>:<path>` reader exists.
- **AC20** — When two branches of a scratch adopter repository each render and are merged, the lock is
  ours' bytes with no conflict, and `git check-attr merge` on the lock's path prints `ours`.
  Red when: the attribute is set and the merge falls back to text.
- **AC21** — When `python gov_tag.py show` runs from a backslashed cwd of a fixture worktree, its own
  dirty rows survive and a pruned worktree's rows leave.
  Red when: one worktree's spellings disagree and its rows drop.
- **AC22** — When `python instructions_edit.py fixture --plant merge-crlf-mixed` and
  `--plant merge-unterminated` run, each exits 0 with one terminator throughout.
  Red when: an append joins two lines or mixes endings.
- **AC23** — When `--plant merge-both-edit` runs, the conflict label names `unit.<tag>`.
  Red when: the label is the generic `merge-rows failed`.
- **AC24** — When `python gov_tag.py --fixture --plant positional-spec-revbump` runs, the appended
  `x.py:3` reds.
  Red when: a rev bump's new citation is print-only.
- **AC25** — When `--plant positional-bulk-move` runs, the untouched lines print as grandfathered and
  the edited ones red.
  Red when: a bulk move strips or extends grandfathering.
- **AC26** — When `tags positional selftest`'s case list is read, it holds the plants of units 47, 48
  and 53, and a staged break of one reds that leg.
  Red when: a positional plant runs only under a suite whose population is elsewhere.
- **AC27** — When `git cat-file -s` runs on spec 49's blob after S27, CR-stripped, it is under the value
  `budgets.py resolve "memory/builds/*/spec/"` prints.
  Red when: the spec stays over its ceiling.
- **AC28** — When `govkit apply` runs over a fixture target selecting `playbook-render` alone, its
  manifest names `agent-instructions wiring`.
  Red when: the widening is unrecorded or absent.
- **AC29** — When `git grep -n "minor behind" -- tools/playbook/render_playbook.py help/` runs, each hit's
  line says "no reseed note".
  Red when: a sentence of the wrong rule passes.
- **AC30** — When a probe reads `tools/gate-legs.json`, `playbook render selftest`'s guard names
  `playbook.kit.toml` and the template.
  Red when: the arm's inputs sit outside its guard.
- **AC31** — When a probe reads the `instruction render (one renderer of record)` row of
  `tools/gate-legs.json`, its argv carries `--card`.
  Red when: the leg S4 edits is unnamed and unchecked.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `row-keyed merge driver replay` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

Unit 19's `tags (the resolver's checks)` leg, unit 26's `tags positional selftest` and unit 20's
`instruction render (one renderer of record)` run S16 to S18, S24 to S26 and S31 over the tree; none
is in `tools/gate-legs.json` at base, so they stay off the line above.

New arm: tools/playbook/adopt-playbook.sh · covers AC4 AC13 AC15 AC16 AC17 AC18 AC21 AC24 AC25 · the playbook-render selftest runs the index and positional plants, each failing case staged by the repaired unit's base rule · none
New arm: tools/memory-tree/merge-rows.test.sh · covers AC22 AC23 · the newline plants and the conflict label, staged by an unfolded comparison and the generic arm · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) parts of eleven units'
  clauses. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — When S27's trim of spec 49 runs (id 24).** Options: (a) at this unit's order, 41; (b) as a
  spec revision of unit 49 before the build run's first dispatch; (c) a high-water row holding spec 49.
  (a) edits a spec frozen at order 39, and (c) is refused once this run's edge mirrors grow it. The
  ceiling binds only while spec 49 is live. RESOLVED (agent, 2026-10-24, delegated): (b), rung 3, the
  main loop making the revision with its §9 line before order 1, this unit's pass observing it.
  widens: none · relaxes: none
- **F3 — Which adopters get the moved wiring leg (id 26).** Options: (a) every `playbook-render`
  adopter, recorded; (b) only targets that held the retired entry, through its `[[retired]]` successor
  mapping. (b) needs a selector a descriptor's `[[gate_leg]]` row does not carry at base.
  RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: the `playbook-render` entry's leg set gains `agent-instructions wiring` for every adopter · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-2 spec audit's 26 MEDIUM and 5 LOW findings batched by
  report id.
- rev-2 · 2026-10-24 · §2 · §3 · §4 · §6 · re-grounded on the parents' landed specs by the cross-check record `../build/2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck.md`, U1 and U7: S27 and AC27 read the `budgets."memory/builds/*/spec/"` cap through `budgets.py resolve`, and S9 is built at unit 49's pass into its census step, which `step-rows-frozen` freezes at that landing.

## 10. Reuse audit

Each item extends the seam its finding names, cited in §2 and §4: `tree_lib.read_blobs_at`, unit 16's
`derive_import_closure`, the merge driver's `_dominant` and `main()`, `handoff.py`'s render parser,
the factory's per-kind table, the overlay's candidate read, `check-wiring.sh`'s ours driver and unit
50's owed-rows probe. `python tools/codebase-map/reuse_lookup.py "move a criterion's observation to
the pass that makes it passable"` ranked `pass_commit`, `read_pass_declarations` and `measure_pass` by
name stem, none an observation rule, so no existing seam fits S2's rule and it lives in this spec and
the repaired units' §3; the batch mints no reader a finding did not ask for. The recall query returned
TOOL-dFairHearing-32 and TOOL-aGraftedHelix-36, precedent batches of a review's minors, and
TOOL-dTrueNorth-20, the `read_blobs_at` and `read_adding_commits` unit S1 and S19 reuse.

Recall terms used: `python tools/memory-recall/query.py "how were a spec audit's medium and low findings batched into one unit" --terms "minors batch promoted MEDIUM LOW report id scope item round-2 spec audit disposition"`
