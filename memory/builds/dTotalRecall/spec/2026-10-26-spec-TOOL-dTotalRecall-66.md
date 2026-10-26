# TOOL-dTotalRecall-66 — the round-1 spec audit of units 54 to 60: its 40 minors, batched

**Status:** DEFERRED · rev-4 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 32 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-65 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 54 to 60
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md`)
exited CONVERGED with 45 confirmed findings. Its five highs, ids 1, 2, 3, 22 and 27, are units 61 to
65. This unit is the batch BUILD-METHOD M4 makes of the rest: the 27 MEDIUM findings, ids 4, 5, 6, 7,
8, 12, 13, 14, 15, 16, 24, 25, 28, 31, 32, 33, 34, 37, 39, 40, 41, 42, 43, 44, 45, 46 and 47 (items
M1 to M21), and the 13 LOW findings, ids 9, 10, 11, 18, 19, 20, 21, 23, 29, 35, 38, 48 and 50 (items
L1 to L11). Each keeps its report id and its own scope item. The minors land on units 54 to 60, so
this unit repairs none in particular and builds after every unit: order 32, above the 31 that units
60 and 65 hold. The review record holds each item's text.

Two minors report at a lower grade a defect another finding also carries: id 32 is the AC2 half of
H2, which `TOOL-dTotalRecall-62` amends, and id 29 is M7's literal memory root at its narrower
consequence. Their items re-observe that fix or add what the finding asks beyond it.

## 2. Scope (IN)

Each item states its change to the unit it lands on, as that unit was built; a landed spec is frozen
and is not edited. "The registry" is `census-kept-paths.txt`, `TOOL-dTotalRecall-65`'s.

- **S1** — id 4 (M1). Unit 55's drain is keyed on the census's own hit: a `check_cause_writers` row of
  the registry is red, naming it, when `check_cause_writers` would not list its file, because the file
  spells a cause line, spells no Serves literal, or is untracked. Observed by AC1.
- **S2** — id 40 (M1). The two ways a hit leaves that unit 55 AC2 never planted are planted:
  `kept-row-caused`, a kept script that gains a `Caused-by` line, and `kept-row-untracked`. Observed by
  AC1.
- **S3** — id 24 (M2). The drain reaches the alias census: a `check_alias_compares` row is red when its
  file holds no raw compare of a `KIND_ALIASES` key below its binding head, or is untracked. Observed
  by AC2.
- **S4** — id 41 (M2). The plant `alias-row-drained` keeps its row while its raw compare is cut.
  Observed by AC2.
- **S5** — id 13 (M3). Unit 56's AC3 is read against the pin the packet records at the tip, so an
  owner's `--repin` that moves the deviations blob satisfies it. Observed by AC3.
- **S6** — id 5 (M4). `check_alias_compares` reports `read_kept_path`'s domain refusal as a red finding
  naming the row and never aborts its walk, as `check_cause_writers` does; unit 61 sequences unit 57
  after unit 56. Observed by AC4.
- **S7** — id 6 (M5). `absorbs` is absent from the canonical ledger factory, both inline copies and
  `tools/memory-tree/kit.toml`. Observed by AC5.
- **S8** — id 31 (M5). Unit 59's plant `merged-home-gained` lives in section `2l` of
  `tools/lib/resolve-python.test.sh`, the factory's arm home (`TOOL-dWitnessedBar-13` S8), and any
  edit of the canonical `legacy_ledger.py` lands in its two inline copies in the same commit, held by
  `PARITY_ROWS`. Observed by AC5.
- **S9** — id 7 (M6). `cmd_new_spec` refuses, as a `Problem` naming the id and before
  `render_spec_skeleton` is reached, an id its own match (`gen_build_index.py:8590-8591`) and
  `FAMILIES` admit but the tree's grammar refuses: `TOOL-dFoo1-3`, which `backlog.SLUG_RE` admits and
  `grammar_for(root).ID_RE` refuses for the digit in its slug, both probed here at HEAD. Observed by
  AC6.
- **S10** — id 16 (M6). That refusal is observed red first: with unit 60's S8 check staged off in a
  scratch copy, the same command raises a traceback or writes a file, and the ledger records it.
  Observed by AC6.
- **S11** — id 8 (M7). `KEPT_PATH_DOMAIN` is built from the conf's `MEMORY_ROOT`, the root
  `record_paths` reads (`tools/memory-tree/tree_lib.py:421-425`), and spells no literal memory root.
  Observed by AC7.
- **S12** — id 12 (M8). Unit 58's AC2 is read over this run's own commits: `git log --no-merges
  --first-parent` from the run's pinned base, and each instrument's blob against the packet's pin at
  the tip. A pin moved on `main` is the owner's to repin. Observed by AC8.
- **S13** — id 14 (M9). A registry row's path is matched segment by segment,
  `^<memory_root>/builds/[^/]+/build/[^/]+$`, and a row with a `..` segment is refused; `fnmatch` is
  not used, since its `*` crosses `/`. Observed by AC9.
- **S14** — id 42 (M9). No registry row this build adds names a file in its own build folder, which
  README:50 puts inside its write set; the engine admits that folder for an adopter, and this pass's
  rule refuses it here. Observed by AC9.
- **S15** — id 15 (M10). The marker reader's domain is per census: a `slug-grammar` marker is honoured
  under the slug census's reader roots, the tool root, `skills/` and `.githooks/`, and the other two
  censuses' markers under the tool root. Observed by AC10.
- **S16** — id 43 (M10). The slug census's population is stated in the ledger as unit 5's `--readers`
  roots, correcting unit 58's non-goal, and fixture markers under `skills/` and `.githooks/` are
  honoured. Observed by AC10.
- **S17** — id 25 (M11). The `govkit:generated` block is the pair `marker_pair("hash-comment",
  "govkit:generated")` returns, located by `find_block` and spliced by `write_block`
  (`tools/govkit/govkit.py:5762`, `:5776`, `:5806`); only its body is built, by a sibling of
  `lf_pin_block`. Observed by AC11.
- **S18** — id 33 (M12). Every govkit site that reads gov's `.gitattributes` block reads both: apply
  (`:7703`), the dirty carve-out (`:7380`), keyed by path and block, update (`:9917`), withdrawal
  (`:10459`), which withdraws each block only when its own population empties, and adopt (`:12965`).
  `WIRE-INTO-PROJECT.md` (`:1398-1409`) describes both regions. Observed by AC12.
- **S19** — id 28 (M13). The marker reader tests a hit's path against the tool root
  `tree_lib.kit_rel()`'s parent derives, never the literal `tools/`. Observed by AC13.
- **S20** — id 37 (M14). The first-seed window is bounded: at the tip every `causes` key of the merged
  home, re-keyed by unit 52's triple, is a key unit 19's seed commit held, so a row added to quiet the
  causes check reds. Observed by AC14.
- **S21** — id 32 (M15). Unit 52's AC2, restated by unit 62 to the first-seed reading, is recorded green
  at unit 52's own tip. Observed by AC15.
- **S22** — id 34 (M16). Unit 59's fixture runs with `GOV_REMOTE`, `GOV_DEFAULT_BRANCH` and every
  `GIT_*` variable out of its environment, as `tools/branch-reconcile/selftest.py:53-62` scrubs, its
  remote made with `-b main` and `origin/HEAD` set. Observed by AC16.
- **S23** — id 39 (M17). `parse_id_parts` refuses a seq-bearing id whose slug the grammar refuses:
  `TOOL-x-3` and `TOOL-9-3`, which `ID_RE` refuses at HEAD (probed here), join the parser arm's refused
  plants. Observed by AC17.
- **S24** — id 44 (M18). One cause-line rule, keyed on the Serves line's prefix: `BIND_RE` captures it
  as the named group `prefix` (`#+`, `//`, `;` or empty), a non-markdown record with a prefix gets
  `<prefix> **Caused-by:**`, and one with an empty prefix is listed `not backfilled`, whatever its
  extension. Observed by AC18.
- **S25** — id 45 (M19). `record_causes.py --backfill --build <slug>` refuses with exit 2 a value the
  slug grammar's `BUILD_SLUG_RE` (`TOOL-dTotalRecall-5` S1) does not match whole, or that names no
  tracked build README. Observed by AC19.
- **S26** — id 46 (M20). `CAUSE_WRITER_PINNED`'s ask id must be a filed ask, a key of
  `backlog._read_asks(corpus)`, before `check_hold_live` is asked its liveness. Observed by AC20.
- **S27** — id 47 (M21). The split census exempts `[0]` on `.split("-")` at any maxsplit and on
  `.rsplit("-")` with none; an `rsplit` with a maxsplit of 2 or more is listed whatever its index.
  Observed by AC21.
- **S28** — id 9 (L1). Unit 60's AC32 is read where the citation lives: the acceptance-ledger line
  answering its S32 cites `tree_lib.py:410-412` and `:421`. Observed by AC22.
- **S29** — id 20 (L1). Those cited lines are confirmed at `462d20f3` to hold `BIND_RE` and
  `def record_paths`. Observed by AC22.
- **S30** — id 50 (L1). A ledger line citing other lines is red whatever the base holds, so the base
  read alone is never the criterion. Observed by AC22.
- **S31** — id 10 (L2). Unit 60's AC10 is decided by its ordering half; the ledger records its grep half
  as certifying nothing. Observed by AC23.
- **S32** — id 11 (L3). Unit 56's AC1 is observed with `grep -c`, which prints `0` on no match.
  Observed by AC24.
- **S33** — id 18 (L4). The unpinned count is derived, six, from the registry against `packet.py`'s
  `INSTRUMENTS`, and the ledger cites it for units 57 and 58. Observed by AC25.
- **S34** — id 19 (L5). The fixtures of unit 59 AC3 and unit 60 AC14 and AC23 are made in
  `tempfile.TemporaryDirectory()`, as `tools/codebase-map/selftest.py:1815` does, and no arm spells
  `%TEMP%`. Observed by AC26.
- **S35** — id 21 (L6). `parse_id_parts` keeps its compiled regex in a module dict keyed by the
  resolved root. Observed by AC27.
- **S36** — id 23 (L7). One keep table: `CAUSE_WRITER_PINNED`'s row joins the registry with two more
  fields, its record glob and its ask id, and the constant gives way to that row (§8 F3). Observed by
  AC28.
  **Readers:** by name: READER NOT IN TREE — `CAUSE_WRITER_PINNED` is minted by `TOOL-dTotalRecall-50`
  in this build and is absent at base `462d20f3` · by value: `check_cause_writers` and the ask read of
  S26, which read the row's fields through `read_kept_path` after this item.
- **S37** — id 29 (L8). The domain is `re.escape(memory_root)` followed by the anchored build-folder
  segments, so a fixture with `MEMORY_ROOT=docs/memory` admits its build-folder row. Observed by AC7.
- **S38** — id 35 (L9). S9's fixture reaches the parse path: where unit 60 S14 re-pointed
  `cmd_new_spec`'s match onto `parse_id_parts`, the refusal carries the parser's `ValueError` text, and
  the ledger names which path refused. Observed by AC6.
- **S39** — id 38 (L10). `parse_id_parts` lets `ConfError` propagate unchanged from a root with no usable
  conf (§8 F2), and unit 54's error states gain it in the ledger. Observed by AC29.
- **S40** — id 48 (L11). The figure guard of unit 60's AC18 runs over joined paragraphs and matches a
  single digit, `[0-9][0-9,]*`. Observed by AC30.

## 3. Non-goals (OUT)

- The five highs: units 61 to 65.
- Editing any landed spec's text, frozen at CLOSED, as §2's opening states.
- The spec lints and checklist entries the report suggests as gates; the close's left-shift step
  (BUILD-METHOD M8) takes them.

### Edges

- **consumes-from** `TOOL-dTotalRecall-5` — `slug_grammar` and its `BUILD_SLUG_RE` (id 45)
- **consumes-from** `TOOL-dTotalRecall-19` — the seed commit of the legacy home (id 37)
- **consumes-from** `TOOL-dTotalRecall-50` — `CAUSE_WRITER_PINNED` and its ask (ids 23, 46)
- **consumes-from** `TOOL-dTotalRecall-53` — the marker reader of its S34 (ids 15, 28, 43)
- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts` and its arm (ids 21, 38, 39)
- **consumes-from** `TOOL-dTotalRecall-55` — the drain and `read_kept_path` (ids 4, 40)
- **consumes-from** `TOOL-dTotalRecall-56` — the alias row and its criteria (ids 11, 13, 24, 41)
- **consumes-from** `TOOL-dTotalRecall-57` — `KEPT_PATH_DOMAIN` and its refusal (ids 5, 8, 14, 18, 29,
  42)
- **consumes-from** `TOOL-dTotalRecall-58` — the marker's domain and its AC2 (ids 12, 15, 18, 28, 43)
- **consumes-from** `TOOL-dTotalRecall-59` — the fixture and its plant (ids 6, 19, 31, 34, 37)
- **consumes-from** `TOOL-dTotalRecall-60` — S8, S13, S19, S20, S23, S24 and AC10, AC18, AC32 (ids 7,
  9, 10, 16, 19, 20, 25, 33, 35, 44, 45, 46, 47, 48, 50)
- **consumes-from** `TOOL-dTotalRecall-62` — unit 52's restated AC2 (id 32)
- **consumes-from** `TOOL-dTotalRecall-65` — `census-kept-paths.txt` and `read_kept_path`'s root
- **consumes-from** `TOOL-dTotalRecall-68` — S36's pinned-writer row in the factory grammar, told apart by its `records` field and `keep:` disposition, as that unit amends S36 before this pass (the round-1 audit of units 61 to 66, id 16)
- **hands-off** `TOOL-dTotalRecall-70` — S18's attributes sites, S34's fixtures, S36's pinned row and AC14, AC22, AC23 and AC28, which that unit re-reads and completes at the tip (the round-1 audit of units 61 to 66, ids 6, 11, 12, 25, 26, 27 and 30)
- **hands-off** `TOOL-dTotalRecall-76` — its seven registry plants, its docs-root plant and its S26 ask read with `pinned-ask-is-spec`, which that batch re-stages and re-reads at the tip (the round-1 audit of units 67 to 70, ids 19, 20, 28)
- **hands-off** `TOOL-dTotalRecall-88` — its registry plants, which that batch rebuilds on one fixture base with a tracked registration and a remote (the round-1 audit of units 71 to 76, ids 25, 26)

## 4. Design

### How the batch builds

One pass, after every unit is terminal. The items share `tree_lib.py`, `record_causes.py`,
`record_kinds.py` and `id_grammar.py`, and every half would regenerate `memory/map/generated/` with
its generator, so BUILD-METHOD M6 keeps them one unit. Within the pass the order is: the registry
items S36, S11, S37, S13 and S14 first, since S1 to S6 read rows through the domain; then S1 to S6;
the marker items S15, S16 and S19; then the code items in unit order; then the ledger items S12, S21,
S28 to S33 and S39.

### The registry row after S36

```text
check_cause_writers	<deviations.py path>	pinned instrument	<record glob>	<ask id>
```

A row with three fields is a plain keep; a row with five is a pinned writer whose records are read
by its glob and whose ask S26 resolves. `read_kept_path` returns the row; the census reads its fields.

### The domain after S11, S13 and S37

```python
def build_kept_path_re(memory_root: str):
    return re.compile(r"^" + re.escape(memory_root) + r"/builds/[^/]+/build/[^/]+$")
```

It is a sibling of `build_spec_path_re` (`tools/memory-tree/tree_lib.py:200-203`), which builds the
spec folder's selector the same way. A path with a `..` segment is refused before the match, and
`KEPT_PATH_DOMAIN` names the compiled value for the conf's root.

### Inventory

Minted: `build_kept_path_re` in `tools/memory-tree/tree_lib.py`; the `BIND_RE` group `prefix`; the
registry's two optional fields; the plants `kept-row-caused`, `kept-row-untracked`,
`alias-row-drained`, `alias-row-outside-domain`, `kept-row-traversal`, `kept-row-nested`,
`kept-row-docs-root`, `marker-under-skills`, `marker-under-githooks`, `marker-vendor-root`,
`build-slug-traversal`, `build-slug-absent`, `pinned-ask-is-spec`, `json-prefixed`, `js-prefixed` and
`html-bare`. Naming cell: `build_kept_path_re` is asked of
`python tools/lexicon/lexicon.py --suggest build_kept_path_re --as py.function` at the pass.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/record_causes.py`, `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/id_grammar.py`, `tools/memory-tree/gen_build_index.py`
- `tools/govkit/govkit.py`, `tools/govkit/selftest.py`, `WIRE-INTO-PROJECT.md`
- `tools/lib/resolve-python.test.sh`, `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`, `tools/gate-lint/legacy_ledger.py`
- `memory/project/census-kept-paths.txt`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Fold each minor into its unit's spec.** M4 refuses folding at the exit.
- **Split into two batches.** Both halves would regenerate `memory/map/generated/` with its generator,
  which M6 clause 3 forbids two concurrent passes to share, and the domain items are read by the drain
  items on both sides.

## 5. Production-readiness checklist

- security — S13 refuses a traversal row; S25 validates a path-forming argument at its boundary.
- perf / scale — S35 compiles one regex per root; S27 and S40 add a shape and a join to two scans.
- error / empty / loading states — S6 reports a refusal as a finding; S25 exits 2 naming the value;
  S39 lets a misconfigured tree's `ConfError` name its conf.
- observability — every new red names its row, file or value.
- risks — S36 changes the pinned row's home; its two readers move in the same commit.
- testing — AC1 to AC30 by the pass; the arms of §7 at the close.
- migration — S36 moves one row; S18's carve-out keeps the lf-pins behaviour for an adopter with one block.
- user docs — `WIRE-INTO-PROJECT.md` describes both `.gitattributes` regions (S18); no `help/` page
  covers the censuses.

## 6. Acceptance criteria

- **AC1** — When `python record_causes.py --fixture --plant kept-row-caused` and `--plant
  kept-row-untracked` run from `tools/memory-tree/` and `--check` follows each, it exits 1 naming the
  row. Red when: a row with no hit behind it passes.
- **AC2** — When the record-kinds fixture plants `alias-row-drained`, `python record_kinds.py --check`
  exits 1 naming the row. Red when: a drained alias row passes.
- **AC3** — When `git hash-object` runs on the deviations instrument at the tip, it prints the `blob`
  the Pins line of `memory/builds/dTotalRecall/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
  names at HEAD. Red when: the two differ.
- **AC4** — When the record-kinds fixture plants `alias-row-outside-domain`, a row naming a file under
  the fixture's tool root, `python record_kinds.py --check` exits 1 naming it and prints no traceback.
  Red when: the census aborts or keeps the row.
- **AC5** — When `git grep -n absorbs -- '*legacy_ledger.py' tools/memory-tree/kit.toml` runs at the
  tip it prints nothing, and `grep -c merged-home-gained resolve-python.test.sh` run from `tools/lib/`
  prints at least 1. Red when: a copy keeps the field, or the plant lives outside the factory's arm.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --new-spec TOOL-dFoo1-3 --tier 2` runs at
  the tip it exits non-zero naming the id, writes no file and prints no traceback; with unit 60's S8
  check staged off in a scratch copy, it does one of those, and the ledger records both runs and
  which path refused. Red when: the refusal comes from no new check.
- **AC7** — When `python record_causes.py --fixture --plant kept-row-docs-root` builds a fixture with
  `MEMORY_ROOT=docs/memory` and a row under its build folder, `--check` keeps the row, and
  `grep -c '"memory/builds' tree_lib.py` prints `0`. Red when: the row is refused for its root.
- **AC8** — When `git log --no-merges --first-parent --name-only 462d20f3..HEAD -- 'memory/builds/*/build/*.py'`
  runs at the tip it prints no path, and each instrument's blob equals its Pins line. Red when: a
  pass of this run wrote an instrument.
- **AC9** — When the plants `kept-row-traversal` and `kept-row-nested` run through
  `python record_causes.py --fixture`, `--check` exits 1 naming each, and a `python -c` probe over the
  registry prints no row under `memory/builds/dTotalRecall/`. Red when: a traversal or nested row is
  admitted, or the build keeps a file of its own folder by row.
- **AC10** — When `python id_grammar.py --readers` runs from `tools/memory-tree/` over the plants
  `marker-under-skills` and `marker-under-githooks`, it honours both. Red when: a slug-grammar keep
  outside the tool root is refused.
- **AC11** — When `python tools/govkit/govkit.py update` runs twice on an unchanged scratch adopter, its
  `.gitattributes` holds exactly one `# govkit:generated` and one `# /govkit:generated` line.
  Red when: the block is appended again or written under another spelling.
- **AC12** — When a scratch adopter holds an uncommitted line inside the `govkit:generated` block,
  `govkit.py apply` and `update` proceed; withdrawing the last lf-pin kit leaves that block in place.
  Red when: an edit inside a gov block refuses a write, or a withdrawal takes the other block.
- **AC13** — When `python record_causes.py --fixture --plant marker-vendor-root` lays the tool root at
  `vendor/gov/`, a marker there is honoured and one in a build-folder script is refused. Red when: the
  literal `tools/` decides.
- **AC14** — When a `python -c` probe compares the merged home's `causes` keys at the tip with
  `git show <unit 19's seed commit>` of `legacy-records.txt`, run from `memory/project/`, re-keyed by
  the triple, it prints no key the seed lacked. Red when: a `causes` row added after the seed passes.
- **AC15** — When `grep -n "first seed record-kinds-legacy"` runs over unit 52's acceptance-ledger entry,
  it prints the line recorded at unit 52's tip. Red when: unit 52's AC2 was not observed there.
- **AC16** — When unit 59's AC3 fixture is rebuilt with `GOV_REMOTE=nope` exported, its
  `compare_to_base` probe still names the planted key `gained`. Red when: the fixture reads the
  caller's environment.
- **AC17** — When the probe calls `parse_id_parts` with `TOOL-x-3` and `TOOL-9-3`, each raises
  `ValueError`. Red when: either returns a tuple.
- **AC18** — When `--backfill` runs over the plants `json-prefixed`, `js-prefixed` and `html-bare`, the
  first two gain `// **Caused-by:**` and the third is listed `not backfilled`. Red when: a prefixed
  record is skipped or a bare one is written.
- **AC19** — When `record_causes.py --backfill --build ..` and `--build absentBuild` run over a fixture,
  each exits 2 and writes nothing. Red when: either writes.
- **AC20** — When `record_causes.py --fixture --plant pinned-ask-is-spec` builds a row whose ask id is an
  open spec id, `--check` exits 1 naming the row. Red when: a spec id passes as an ask.
- **AC21** — When `python id_grammar.py --readers` runs over a fixture holding `x.rsplit("-", 2)[0]`,
  it lists that line. Red when: the census exempts it.
- **AC22** — When `git grep -n "tree_lib.py:410-412" -- memory/builds/dTotalRecall` runs at the tip it
  prints the ledger line for unit 60's S32, which also cites `:421`, and `git show 462d20f3` of
  `tree_lib.py`, run from `tools/memory-tree/`, holds `BIND_RE` and `def record_paths` there. Red when: the ledger cites other lines.
- **AC23** — When `git log --format=%s` lists the pass commits at the tip, unit 54's precedes unit 45's,
  and the ledger names AC10's grep half void. Red when: unit 45 built first.
- **AC24** — When `grep -c "census: kept"` runs over the deviations instrument at the tip it prints `0`.
  Red when: a marker sits in the instrument.
- **AC25** — When a `python -c` probe counts registry rows whose path `packet.py`'s `INSTRUMENTS` does
  not pin, it prints `6`, the figure the ledger cites. Red when: the ledger cites another count.
- **AC26** — When `git grep -n "%TEMP%" -- tools/lib/resolve-python.test.sh tools/govkit/selftest.py`
  runs at the tip it prints nothing. Red when: an arm spells a cmd.exe variable.
- **AC27** — When a probe calls `parse_id_parts` twice with one root, the module's cache holds one
  entry. Red when: the regex compiles per call.
- **AC28** — When `git grep -n CAUSE_WRITER_PINNED -- tools` runs at the tip it prints nothing, and
  `python record_causes.py --check` keeps the pinned writer's records by its five-field row.
  Red when: two keep tables remain.
- **AC29** — When the probe calls `parse_id_parts("TOOL-dFoo-3", root)` with a root holding no
  `.memory-tree.conf`, it raises `ConfError` naming the missing conf. Red when: it raises another class.
- **AC30** — When the AC18 guard runs over a scratch file whose figure `9` wraps onto the line before
  `journal`, it lists the figure. Red when: a wrapped or single-digit figure escapes.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `build-index selftest` · `tier2-review self-test` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `python resolver (behaviour + inline parity + idiom ban)` · `shell-hygiene selftest` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC1 AC7 AC9 AC13 AC18 AC19 AC20 AC28 · the plants of §4's Inventory for the cause census, staged by skipping each new test · none
New arm: tools/memory-tree/record_kinds.py · covers AC2 AC4 · `alias-row-drained` and `alias-row-outside-domain`, staged by skipping the drain and the refusal · none
New arm: tools/memory-tree/id_grammar.py · covers AC10 AC17 AC21 AC27 · the marker roots, `TOOL-x-3`, `TOOL-9-3` and the maxsplit-2 `rsplit`, staged by restoring the old predicates · none
New arm: tools/memory-tree/gen_build_index.py · covers AC6 · the `--new-spec TOOL-dFoo1-3` case, staged by skipping S8's check · none
New arm: tools/govkit/selftest.py · covers AC11 AC12 · the twice-updated adopter and the carve-out per block, staged by hand-spelled markers · none
New arm: tools/lib/resolve-python.test.sh · covers AC5 AC16 · section `2l`'s `merged-home-gained` under `GOV_REMOTE=nope`, staged by keeping the caller's environment · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of one unit's clause, which would split a clause that unit carries whole. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How does `parse_id_parts` answer a root with no usable conf (S39)?** Options: (a) let
  `ConfError` propagate, its message naming the conf; (b) re-raise it as `ValueError`, which the readers
  catch as a malformed id. (b) reports a misconfigured tree as a bad id and hides the refusal the error
  carries. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the option that keeps both refusals
  distinct. widens: none · relaxes: none
- **F3 — Which table holds the pinned writer's row (S36)?** Options: (a) the registry, with two optional
  fields; (b) `CAUSE_WRITER_PINNED`, widened with a census column for the other rows. (b) keeps a
  constant in engine bytes naming a path of this repository, the defect unit 65 closes. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 54 to 60, its 40
  minors batched (27 MEDIUM, 13 LOW).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-68, TOOL-dTotalRecall-70, each the other end of an edge a unit the round-1 spec audit of units 61 to 66 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-76, the other end of an edge a unit the round-1 spec audit of units 67 to 70 promoted wrote; nothing else moved.
- rev-4 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names, cited in the item: unit 55's drain and
`read_kept_path`, unit 57's domain, unit 53 S34's marker reader, `tree_lib.kit_rel()`
(`tools/memory-tree/tree_lib.py:48`), govkit's `marker_pair`, `find_block` and `write_block`
(`tools/govkit/govkit.py:5762`), `backlog.check_hold_live` (`tools/memory-tree/backlog.py:878`), the
fixture scrub of `tools/branch-reconcile/selftest.py:53` and unit 65's registry. `build_kept_path_re` is
the one new function. `python tools/codebase-map/reuse_lookup.py "project registry of exempt paths read from the memory root"`
ranked name-stem neighbours, and the registry reader it missed is unit 65's.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
