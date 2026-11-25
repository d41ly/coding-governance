# TOOL-aPrunedIndex-4 — `--gc` skips a worktree that predates the tag registry, and still refuses one it cannot read

**Status:** SPECCED · rev-3 · 2026-11-26 · node a · Tier-2 · base 3d6c1702 · streams tooling · order 4 · closes KICK-dKeptSession-87

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md](../build/2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 |
| [2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 |
| [2026-11-25-prompt-TOOL-aPrunedIndex-3-revision.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-3-revision.md) | research | TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 |
| [2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1.md](../reviews/2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1.md) | spec-audit | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 |

<!-- /gen:spec-records -->

## 1. Goal

`gov_tag.py --gc` refuses while any live worktree holds no tag registry, so on this node nothing
retires a dead extractor version. Four of its 106 worktrees are checked out at commits older than the
registry. Such a worktree derives no version, so `--gc` can drop nothing it reads. After this unit
`--gc` skips it, naming it, and collects. It still refuses a worktree whose registry should be there
and cannot be read.

KICK-dKeptSession-87 accepts a `--gc` that "names an unreadable worktree and collects the versions no
readable one derives". Its stated case is a worktree that predates the registry, and the brief draws
the line there.

## 2. Scope (IN)

- **S1** — `tools/playbook/tag_index.py#read_live_versions` skips a worktree when two things hold: no
  file stands at its registry path, and the tree its own HEAD names holds none at that path. It
  derives nothing from a skipped worktree: no version pair, no digest and no conf key. Observed by AC1
  and AC5.
- **S2** — Every other worktree is read as today, and one that cannot be read refuses the whole
  collection, naming it, and no row moves. That covers a registry HEAD holds and the working tree
  lacks, a registry on disk that does not parse, an unreadable extractor module, a HEAD git cannot
  read, and a `.memory-tree.conf` that cannot be read. The last is one that does not decode or open, one
  at whose path something other than a file stands, and one HEAD holds and the working tree lacks. A
  worktree that holds none in either place derives the default key, as today. Observed by AC2 and AC7.
- **S3** — A registry on disk is read even when HEAD holds none, so the versions of a worktree merging
  the registry in, or adding it uncommitted, stay live. Observed by AC3.
- **S4** — When no worktree yields a version, `--gc` refuses and no row changes. An empty live set
  would otherwise collect the whole index. Observed by AC4.
- **S5** — `tools/playbook/gov_tag.py#run_gc` prints one line per skipped worktree before its
  collected line, which keeps its bytes. Observed by AC1.
- **S6** — A new plant, `gc-predates`, in `tools/playbook/gov_tag.py`, and its row in `SELFTEST_ROWS` of
  `tools/playbook/tag_bundle.py`. Observed by AC1, AC2, AC3, AC4 and AC7.
- **S7** — The sentence stating what `--gc` refuses, in `tools/playbook/README.md`, `help/tags.md` and
  the `gov_tag.py` module docstring, says what it skips too. Observed by AC6.
- **S8** — The `tags bundle selftest` row of `tools/run-gates/selftest-budgets.txt`, and that leg's row of
  `tools/run-gates/ceiling-evidence.txt`, carry a reading of the leg with this build's five plants in it.
  Observed by AC8.

## 3. Non-goals (OUT)

- Any run of `--gc`, VACUUM or a deletion on either live index file. Every criterion here runs in a
  fixture, or reads git and the registries without opening an index.
- Any run, from the building worktree before the owner's go, of what opens the live index: the legs
  `tags (the resolver's checks)`, `instruction edits (manifest checks)`,
  `edges (every declared edge parses, is registered and resolves)` and `instruction units selftest`, and a
  `gov_tag.py` verb outside `--fixture`. This unit is verified by `--fixture` plants and private copies.
- Collecting on a plain build, and evicting by age.
- Skipping a worktree that is merely unreadable, whatever the reason.
- Looking for a registry at another kit path than the collecting worktree's own.
- A change to `remove_unheld_rows` or to what `--gc` sweeps after the versions. Unit 3 owns the sweep,
  and `--gc` keeps the full one.
- A bare main repository entry, which refuses today and still does.
- The speed of `read_live_versions`, about a second per worktree on this node.

### Edges

- **consumes-from** `TOOL-aPrunedIndex-1` — its `dead-versions` row, one of the five AC8 times.
- **consumes-from** `TOOL-aPrunedIndex-2` — its `named-probe` row, for the same.
- **consumes-from** `TOOL-aPrunedIndex-3` — its `released-rows` and `released-cost` rows, for the same, and
  the split of the sweep into `remove_dead_holders` and `remove_unheld_rows(con)`, which
  `remove_dead_versions` calls.
- **hands-off** external — the first collection of the live index, which the owner runs or orders in
  the building session.

## 4. Design

### Evidence

`tools/playbook/tag_index.py#read_live_versions` iterates the top-level paths
`read_worktree_trees` returns, reads each registry, and raises on the first `TagError`. It is called
by `remove_dead_versions` alone, before the write lock, and `remove_dead_versions` is called by
`run_gc` alone. `read_worktree_trees` also serves `remove_dead_holders`, after unit 3 splits the sweep, and
`read_index_rows`, and the latter calls `.discard` on both returned sets, so its return shape stays.

The rule was run over the real tree first, with no index opened. On 2026-11-25, PINNED, it read 106
worktrees and skipped four: `blissful-khayyam-69a7df`, `deterministic-attended-workflows-943570`,
`deterministic-reuse-workflows-f70c33` and `full-repo-bar-tests-2591de`. Those are the four the
diagnosis names. It found none unreadable, and 6 live versions of the citations extractor. The run
took 123 s.

### Mechanism

1. `read_worktree_heads(root)` returns one `(top, head)` pair per entry of
   `git worktree list --porcelain`. `top` is spelled by `derive_worktree_key`, and `head` is the sha of
   the entry's `HEAD` line, `""` when it has none. `read_worktree_trees` builds both of its sets from
   that list, so the listing is parsed once.
2. `read_live_versions` iterates `sorted(read_worktree_heads(root))`. Inside its existing `try`, before
   it reads the registry, it skips the worktree when `os.path.lexists(registry)` is false and
   `read_git(root, "ls-tree", "--full-tree", "--name-only", head, "--", rel)` is empty. `rel` is
   `kit_rel` joined to `namespaces.toml` in POSIX form. The skipped `top` joins a list, which becomes
   the fourth element of the return.
   Inside the same `try`, before `load_conf`, it refuses when `.memory-tree.conf` is no regular file there
   and either `os.path.lexists` finds something at that path or the same `ls-tree` finds that name in
   `head`. `load_conf` moves inside the `try`, which takes `OSError` and `UnicodeDecodeError` too, so every
   one of these names the worktree. `load_conf` itself answers an empty map for a path that is no file, for
   every other caller, and is not edited.
3. After the loop, an empty `pairs` raises
   `--gc: no worktree holds <rel>, so nothing is collected`.
4. `remove_dead_versions` returns `(rows, versions, skipped)`.
5. `run_gc` prints, for each skipped worktree,
   `tag-index — skipped: worktree <top> predates <kit_rel>/namespaces.toml`, then its collected line.

The head comes from the listing and is read in `root`, never through `git -C <top>`. A worktree
directory whose `.git` file is gone sits inside the main checkout on this node, so git run there would
answer with the main checkout's HEAD.

`git ls-tree` exits 0 with no output when the tree lacks the path. It fails on the all-zero sha of an
unborn branch and on the empty string; both were run on 2026-11-25. A failure is a `TagError` inside
the `try`, so it refuses as S2 says, and a git failure is never read as absence.

The disk test comes first, so a worktree holding a registry costs no extra git call.

### What it cannot see

- A worktree whose kit sits at another path reads as predating. Its rows are collected, its next build
  parses them again, and the skip is printed.
- A worktree whose directory is gone and whose HEAD predates the registry is skipped. An uncommitted
  registry it once held cannot be observed.
- The live set is read before the write lock, as today. A worktree that gains a registry in between
  loses rows its next build writes again.

### The plant

`gc-predates` runs in the fixture's own scratch repository. The tables it counts are `blob_row`,
`path_row` and `blob_parsed`, at one version of `fixture_tags:extract_declared`.

1. It builds `root` and adds the worktrees `wt2`, `wt3` and `wt4`. It commits `EDITED_EXTRACTOR` in
   `wt2`, builds it and takes its version, dumps the rows of `root`, then removes and prunes `wt2`. Its
   rows are now dead, and their count must be above 0.
2. It commits the removal of the registry in `wt3`, so that HEAD holds none, and deletes the registry
   of `wt4` from disk alone. `run_gc` must raise a `TagError` naming `wt4`, and the dead count must not
   move.
3. It restores `wt4`, writes the registry and `THIRD_EXTRACTOR` uncommitted in `wt3`, and builds `wt3`.
   `run_gc` must exit 0, print no skipped line, leave 0 dead rows, and leave the rows of `wt3` as they
   were and above 0.
4. It deletes the registry of `wt3` from disk. `run_gc` must exit 0, print exactly one skipped line,
   which names `wt3`, leave 0 rows of its version, and leave the dump of `root` equal to step 1's.
5. It calls `run_gc` with the kit path `tools/nokit`, which no worktree holds. It must raise a
   `TagError` naming the `tools/nokit` registry path, and the rows of `root`, above 0, must not move.

6. It commits in `wt4` a `.memory-tree.conf` whose `CHARTER` is not the default and that charter, builds
   `wt4`, and counts the `path_row` rows of its conf key, which must be above 0. It deletes the conf from
   disk, then puts a directory at its path, then bytes that do not decode. After each, `run_gc` must raise
   a `TagError` naming `wt4`, and the count must not move. It restores the conf, and `run_gc` must exit 0
   with the count unmoved.

It prints one line per step. Its last line is printed only when every condition holds, and ends
`refused on wt4, wt3 read and then skipped by name, refused on none, refused on a conf`. It exits 0 then,
and 1 otherwise.

A prototype of this plant, over a patched `read_live_versions` held in scratch, ran green on
2026-11-25, step 6 included, whose conf key held 16 rows. These breaks of it each turned a step red:

| break | first step that reds |
|---|---|
| today's code, no skip | 2, refusing on `wt3`; 4 reds too |
| skip on absence from disk alone | 2, collected with `wt4` unreadable |
| skip on absence from HEAD alone | 3, the live rows of `wt3` collected |
| no refusal on an empty live set | 5, the rows of `root` collected |
| no refusal on an absent or non-file conf | 6, the 16 rows of `wt4`'s conf key collected |

### Migration

None. No schema, row or file name moves. The edit to `tag_index.py` is a new extractor version, so
each worktree parses once more after taking it, as for units 1 to 3, which land with it.

### Rollout

Live at landing. `--gc` runs only when a person types it.

### Inventory

One function, `read_worktree_heads`; the lexicon's `--suggest` answered OK for cell `py.function`. One
plant, `gc-predates`, and one output line, `tag-index — skipped:`, which no cell grades.

### Files touched (estimate)

- `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`, `tools/playbook/tag_bundle.py`
- `tools/playbook/README.md`, `help/tags.md`
- `memory/map/generated/symbols.json`, regenerated by `gen_map.py --write` for the new function
- `tools/run-gates/selftest-budgets.txt`, `tools/run-gates/ceiling-evidence.txt`
- `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-4-1-acceptance-ledger.md`, the
  acceptance ledger, one line per criterion

### Alternatives rejected

- The plant's row in the tag resolver's plant table of `tools/playbook/adopt-playbook.sh`, for the leg time
  unit 1 states.
- A refusal only where the conf is absent from disk and held by HEAD. A directory at its path is neither
  absent nor an error to `load_conf`, so it would still derive the default key.
- Skip every unreadable worktree, the widest reading of the ask. A registry deleted by mistake, or a
  half-written one, would then lose that worktree's live rows with only a printed line.
- Ask HEAD alone. The prototype collected the live rows of a worktree holding an uncommitted registry.
- Compare commit dates with the commit that added the registry. A branch cut earlier and merged since
  holds it, and an adopter's history has another such commit.
- Return the heads from `read_worktree_trees` as a third element or a mapping. Its callers would each
  change for the one that reads it.

## 5. Production-readiness checklist

- security: no new write path or grant. The sha and path passed to git are git's own output and the
  kit's own location.
- perf / scale: one `git ls-tree` per worktree with no registry on disk, four on this node today, and one
  per worktree with no conf on disk, none on this node on 2026-11-25.
- error / empty / loading states: every git failure refuses. An empty live set refuses.
- observability: one line per skipped worktree, and the refusal still names its worktree.
- risks: a wrong skip costs a re-parse and never a wrong row, because reads join on the reading
  worktree's own versions. A reader open in that worktree during the collection can miss rows. A
  skipped worktree holds no registry at the kit path, so `gov_tag.py` there has nothing to read with.
- testing: the `gc-predates` plant, its five breaks, and the read-only run over the real worktrees.
- migration: N/A — no stored shape moves.
- user docs: `help/tags.md` and `tools/playbook/README.md`.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant gc-predates` runs, `run_gc` in its
  step 4 exits 0, prints one `tag-index — skipped:` line naming `wt3`, and leaves 0 rows of that
  version and an equal dump of the live worktree. The plant exits 0.
  Red when: the skip is removed, so `--gc` refuses on `wt3`.
  cost: 19 s to 35 s for the prototype, on a machine running other bars.
- **AC2** — When `gc-predates` runs step 2, `--gc` refuses naming `wt4`, and the rows of the dead
  version are above 0 and unmoved.
  Red when: the skip tests the disk alone, so the deleted registry reads as predating.
- **AC3** — When `gc-predates` runs step 3, `--gc` prints no skipped line, and leaves 0 rows of the
  dead version and every row of `wt3`.
  Red when: the skip tests HEAD alone, so the uncommitted registry is not read.
- **AC4** — When `gc-predates` runs step 5, `--gc` refuses naming the `tools/nokit` registry path, and
  the rows of `root` are above 0 and unmoved.
  Red when: the empty-set refusal is removed, so every version is collected.
- **AC5** — When a Python probe calls `read_live_versions` with this repository and its
  `tools/playbook`, its skipped list equals the worktrees of `git worktree list --porcelain` that hold
  no registry file and whose HEAD `git ls-tree` shows none, and the list is not empty.
  Red when: a worktree whose HEAD holds the registry is skipped, or an older one is not.
  cost: about two minutes. The call opens no index file.
  fixture: the worktrees of the node; four qualified on 2026-11-25. With none left, the unit's record
  says so and AC1 stands alone.
  figure: DERIVED at observation time.
- **AC6** — When `grep -n "predates" tools/playbook/README.md help/tags.md tools/playbook/gov_tag.py`
  runs, each file prints the sentence on what `--gc` skips.
  Red when: a page still says only that `--gc` refuses.
- **AC7** — When `gc-predates` runs step 6, `--gc` refuses naming `wt4` for a conf deleted from disk, for a
  directory at its path and for bytes that do not decode, with the rows of its conf key above 0 and
  unmoved, and collects nothing of them once the conf is back.
  Red when: `load_conf` runs with no test ahead of it, so an absent or non-file conf reads as the default
  key and the rows are collected, or stands outside the `try`, so the last is a traceback naming no
  worktree.
- **AC8** — When the main loop times `tags bundle selftest` alone once, after the last unit of the build is
  built, its wall is below the leg's 300 s `ceiling` of `tools/gate-legs.json`. The budget row carries 1.5
  times that reading, floored at 60, and names it, and the evidence row is written from it by
  `derive-ceilings.py --write`.
  Red when: the five plants take the leg to its ceiling, so it is killed before it reports an arm.
  permission: a pass runs no self-test leg, so this reading is the main loop's, at the close.
  cost: the leg read 22 s before this build. The plants' prototypes took 8 to 22 s for `dead-versions`, 3 to
  5 s for `named-probe` and 17 to 35 s for `gc-predates`, on a machine running other bars; unit 3 names the
  seconds of its two.
  figure: DERIVED at observation time.

## 7. Gates

`tags (the resolver's checks)` · `instruction edits (manifest checks)` · `edges (every declared edge parses, is registered and resolves)` · `instruction units selftest` · `lexicon naming predicates` · `tags bundle selftest` · `playbook render selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

Those of the line that open the live index, the four section 3 lists, are owed at the close, after the
owner's go, and by no pass before it.

New arm: tools/playbook/tag_bundle.py · covers AC1 AC2 AC3 AC4 AC7 · the `gc-predates` row; staged red five times, once per break in section 4's table · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft.
- rev-2 · 2026-11-25 · §2 §3 §4 §5 §6 §7 S2 S6 S8 AC7 AC8 · folded
  `2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1`: finding 6 (`remove_dead_holders` is
  the caller after unit 3), 12 (the plant's row moves to `tags bundle selftest`, and AC8 times that leg), 14
  (the legs that open the live index), 15 (the symbol map), 18 (a conf that cannot be read refuses, the
  class-level fix, with step 6).
- rev-3 · 2026-11-26 · §2 §3 §4 S8 AC8 · TOOL-aPrunedIndex-3's revision on finding 16 of
  `2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1` takes out its `moved-view` plant, so
  five rows are timed. Section 4 names the acceptance ledger.

## 10. Reuse audit

The seams extended are `read_live_versions`, `read_worktree_trees` and `run_gc`, and the
`--fixture --plant` runner with its `two-versions` helpers. The probe
`tools/codebase-map/reuse_lookup.py "which worktrees predate a file: skip a worktree whose HEAD tree holds no registry"`
returned no function that answers it: `read_head_sha` and `load_registry` read one known tree, and no
candidate walks the worktree list. The recall answered KICK-dKeptSession-87 first, then
PLAY-dOrderedCharter-51, whose S5 is the refusal this unit narrows and whose ledger records the
deleted-registry probe that AC2 repeats.
Recall terms used: gov_tag gc refuses worktree registry namespaces.toml dead versions collect read_live_versions predates HEAD tree shared index
