# PLAY-dOrderedCharter-18 — the moved grammar: every name the core imports from the recall kit moved into memory-tree, and every by-path reader re-pointed in the same unit

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base ce13efbe · streams playbook · order 1 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0048@aab14736 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md) | research | PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-28 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

The id grammar, the conf layer it binds to and check 27's eight names move out of the memory-recall
kit into one memory-tree module, `tools/memory-tree/id_grammar.py`, and memory-recall imports them
from there. Every reader that reaches memory-recall's `extract.py` or `recall_conf.py` by path is
found by a query over `tools`, `skills` and `.githooks`, never typed, and re-pointed in this unit, so
the move never lands half done (the whole-design audit's C1-F6). This is the precondition unit 16's
dependency check lands on (v2 `[layers]`, P28; layer-library `[consult]`, check-27 row), and the
scan-set change is proven by a staged break in the moved module that reds
`check-verdict-epoch.sh` (DA-H4).

## 2. Scope (IN)

- **S1** — The module `tools/memory-tree/id_grammar.py` (shared interface S1). It holds, moved and
  not copied: from `tools/memory-recall/recall_conf.py` the conf layer, `repo_root`, `load_conf`,
  `ConfError`, `Conf` with `Conf.digest`, and `resolve`; from `tools/memory-recall/extract.py` the
  eras, `Grammar`, `grammar_for`, `anchor_at` and the four record readers check 27 imports,
  `corpus_inputs`, `extract_records`, `extract_supersessions` and `derive_supersession_map`, with
  the helpers they call; from `tools/memory-recall/bench.py` check 27's other four, `build_index`,
  `match_expr`, `terms` and `ALIAS_WEIGHT`, with the tokenizer they read. Observed by AC1.
- **S2** — Importing `id_grammar` resolves no conf. The kit-install-root grammar binds on first use
  and is cached per process, so a memory-tree module may import it at module level and a tree with no
  `.memory-tree.conf` still imports every memory-tree module. Observed by AC5.
- **S3** — memory-recall imports the moved names. `extract.py`, `recall_conf.py` and `bench.py`
  keep their file names and re-export every moved name from `id_grammar`, reached through the
  `resolve_kit_dir` copy each already carries (`resolve_kit_dir("memory-tree", "id_grammar.py",
  here)`, the declared `requires = ["memory-tree"]` of `tools/memory-recall/kit.toml:7`).
  `KIT_MEMORY_RECALL_VERSION` stays in `recall_conf.py`, where `version_from` reads it. The recall
  kit's own corpus output is byte-identical across the move. Observed by AC4.
- **S4** — `Conf.digest` stops folding the recall kit's version (§8 F1): it folds the SHA-1 of
  `id_grammar.py`'s own bytes, line endings normalised to LF, in that version's place, so the
  transition audit's cache key (`tools/memory-tree/transition_audit.py:710-715`) and recall's
  `conf_digest` (`tools/memory-recall/query.py:450`) still move when the grammar does, and no
  memory-tree module reads a recall constant. Observed by AC7.
- **S5** — The by-path inventory, derived by the query §4 "### The inventory query" states and
  re-run at the pass, never copied into a file. Each hit is dispositioned by the rule of §4: a reader
  that reaches a moved name is re-pointed to `id_grammar`; a reader that names a file or constant
  that does not move is kept and its disposition recorded in the pass commit's `Decided:` trailer;
  `tools/runlog/extract.py` and its readers are out of the population by construction. Observed by
  AC2 and AC3.
- **S6** — The memory-tree readers re-pointed: `backlog.py`'s `_resolve_anchor_at`,
  `corpus_ids.py`'s `GRAMMAR_DIR`, `grammar` and `_anchor`, `merge-rows.py`'s `anchors`,
  `transition_audit.py`'s `resolve_recall_kit` and `resolve_anchor`, `gen_build_index.py`'s
  anchor arm, `row_grammar.py`'s `load_recall_kit` and `derive_relation_successors`, `gotchas.py`'s
  check-18 probe through `corpus_ids`, and `migrate_backlog.py`'s `seed_recall_kit`, which seeds no
  recall kit once nothing in the fixture needs one. Each imports `id_grammar` as a sibling, so
  memory-tree probes the recall kit for nothing. Observed by AC3 and AC5.
- **S7** — `check-verdict-epoch.sh`'s scan set and its DELEGATES: `$_recall` and its resolution
  (`tools/memory-tree/check-verdict-epoch.sh:177-182`) leave, and `${_kit}id_grammar.py` joins
  DELEGATES (`:194`). Its import-closure walk then reaches `id_grammar` from every delegate that
  imports it. Observed by AC6.
- **S8** — The readers outside memory-tree that reach a moved name re-pointed to `id_grammar`:
  drift-audit's `_resolve_ident` and `_resolve_anchors` (`tools/drift-audit/drift_report.py:604-665`),
  and `check-unattended.sh`'s `RECALL_CLI` probe (`tools/unattended/check-unattended.sh:2028-2065`),
  whose anchor judgement reads the grammar from the memory-tree kit and no longer skips on a blank
  `RECALL_CLI`. Observed by AC3 and AC8.
- **S9** — The suite fixtures and arms the move changes, each re-pointed and its arm seen red again
  at the close (§7 `New arm:` lines): `merge-rows.test.sh`'s fixture copies, `manifest-check.test.sh`'s
  F1 arm, which hides `extract.py` and expects the grammar's NOTE and now asserts no NOTE because the
  grammar ships in memory-tree, `straggler-guard.test.sh`, `transition-audit.test.sh`,
  `check-memory-hygiene.test.sh`'s check-27 copy-install fixture, `check-wiring.test.sh`'s fixture
  and its dead-grammar arm, the drift-audit self-test's grammar-equality arm, and the self-test arms
  of `corpus_ids.py`, `gotchas.py`, `row_grammar.py`, `backlog.py`, `merge-rows.py` and
  `migrate_backlog.py` that plant an absent or outdated recall kit, each re-planted as an absent or
  outdated `id_grammar.py`. `check-unattended.test.sh`'s copy is amended under README rule 8.
  NOT OBSERVED by a criterion of this spec: the arms are suites, observed at the close.
- **S10** — The two `requires_if` rows of `tools/memory-tree/kit.toml:8` whose reason is the
  grammar (the `DEAD_PATH_PIN`/`ORPHAN_ID_PIN` row and the `BACKLOG_MODE` row) are deleted, since
  their edge no longer exists. Observed by AC9.
  **Readers:** by name: `tools/govkit/govkit.py`, whose selfcheck check 7 reads each `requires_if`
  row's `kit` and `when_any_key_set` keys and reads the rows that remain unchanged · by value: NO VALUE READERS —
  no reader counts the rows or derives from the two deleted ones, which select no install.
- **S11** — `check-kit-versions.sh` is in the inventory and kept: it reads
  `KIT_MEMORY_RECALL_VERSION` from `recall_conf.py` (`tools/check-kit-versions.sh:128,332-336`), a
  constant that does not move, and its arm is seen red again on a planted mismatch. Observed by AC10.

## 3. Non-goals (OUT)

- The layer register, the dependency check and its kinds of edge: unit 16's.
- The optional slots for the edges that remain after the move: unit 17's.
- Any change to what recall ranks, chunks or caches beyond the digest's version term; `CACHE_VERSION`
  in `query.py` is untouched.
- dTotalRecall's slug grammar on the moved parser (clause 0046 names it as that build's).
- A durable gate over by-path readers. The class is core-to-optional edges, and unit 16's check over
  path probes, file copies and shell references is that gate; this unit's query is a one-time
  inventory.
- Moving `KIT_MEMORY_RECALL_VERSION`, `extract_chunks`, `query.py` or recall's CLI.

### Edges

- **hands-off** `PLAY-dOrderedCharter-16` — the dependency check over every edge kind, which lands after this move and keeps the edges this unit removed from returning
- **hands-off** `PLAY-dOrderedCharter-17` — the edges the move does not remove: `drift_report`, the lexicon call, the drift-audit and runlog calls, each made an optional slot
- **hands-off** `PLAY-dOrderedCharter-28` — the moved `grammar_for`, from which the `FAMILY-<slug>-<seq>` native-id class resolves
- **hands-off** `PLAY-dOrderedCharter-19` — `repo_root` and the moved grammar, through which the `doc` namespace reads the charter's path from the conf

## 4. Design

### The module

`id_grammar.py` is one file because the clause moves one population, the names the core imports from
the recall kit, and splitting it would give the dependency check two modules to keep in step. Its
public names keep their spellings, so every caller changes only where it imports from. The module
carries no `resolve_kit_dir` copy and imports nothing outside the standard library at module level.
`extract_records` reads `parse_spec_h1` from its sibling `tree_lib.py` directly, where
`load_parse_spec_h1` reached it across kits through `resolve_kit_dir` (`tools/memory-recall/extract.py:113-121`);
`tree_lib.py` imports nothing of `id_grammar`, so no import cycle forms.

The module-level grammar `extract.py` binds at import (`tools/memory-recall/extract.py:62-188`) becomes
a function of the cached default `Grammar`: `grammar_for()` with no root returns it, built on first
call. `extract.py` re-binds its own module constants (`ID`, `ID_RE`, the four anchors, `FAMILIES`,
`ERAS`) from that call at its import, so recall's CLI and `query.py` read exactly what they read today.

### The inventory query

Run at the pass, before the first edit, and again after the last:

```bash
git grep -nE '\b(extract|recall_conf|bench)\.py\b' -- tools skills .githooks \
  ':!tools/memory-recall/' ':!tools/runlog/'
git grep -nE 'import (extract|recall_conf|bench)\b|\b(extract|recall_conf|bench)\.(grammar_for|anchor_at|repo_root|resolve|Conf|corpus_inputs|extract_records|extract_supersessions|derive_supersession_map|build_index|match_expr|terms|ALIAS_WEIGHT)\b' \
  -- tools skills .githooks ':!tools/memory-recall/' ':!tools/runlog/'
```

The first is the clause's by-path query; `bench.py` joins it because check 27's four index names move
too. The second is the by-name query, which catches a reader that imports a moved name without
spelling a path. `tools/runlog/extract.py` shares the basename, so the runlog kit is excluded by
pathspec and `tools/gate-legs.json:374`'s hit, which names runlog's file, is out of the population.

**The rule.** A hit is re-pointed when the reader reaches a moved name, or copies `extract.py` or
`recall_conf.py` to give a fixture the grammar. It is kept when it names the recall kit's directory,
its CLI, its version constant or a file that stays, and the keep is stated with the reader. A hit in a
comment is re-worded where it states where the grammar lives, and left where it narrates history.

At `ce13efbe` the first query returns 26 files and the second is non-empty, adding
`tools/memory-tree/gen_build_index.py:6766`, which imports `extract` with no path on its line. Both
figures are DERIVED by the query at the pass, and the dispositions below are its reading at the base:

| Reader | Disposition |
|---|---|
| `tools/memory-tree/backlog.py`, `corpus_ids.py`, `merge-rows.py`, `transition_audit.py`, `gen_build_index.py`, `row_grammar.py`, `gotchas.py`, `migrate_backlog.py` | re-point (S6) |
| `tools/memory-tree/check-verdict-epoch.sh` | re-point (S7) |
| `tools/drift-audit/drift_report.py`, `tools/drift-audit/selftest.py` | re-point (S8, S9) |
| `tools/unattended/check-unattended.sh` | re-point (S8) |
| `tools/memory-tree/merge-rows.test.sh`, `tools/memory-tree/transition-audit.test.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`, `skills/session-kickoff/manifest-check.test.sh`, `.githooks/straggler-guard.test.sh`, `tools/check-wiring.test.sh`, `tools/unattended/check-unattended.test.sh` | re-point (S9) |
| `tools/check-kit-versions.sh` | keep: the version constant stays (S11) |
| `tools/check-hook-destinations.test.sh`, `tools/govkit/selftest.py`, `tools/govkit/govkit.py` | keep: they name the recall kit's directory or its shipped files, which stay |
| `tools/codebase-map/scen-adversarial.json`, `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json` | keep: recorded scenarios and a recorded receipt, data about a past tree |
| `tools/push-main.test.sh`, `tools/gate-legs.json` | out: every hit names runlog's `extract.py` |

### Conf.digest

Today `digest()` folds `KIT_MEMORY_RECALL_VERSION` because the eras lived in `extract.py`
(`tools/memory-recall/recall_conf.py:242-271`). After the move the eras live in `id_grammar.py`, so
the term that dates them is that file's bytes: `hashlib.sha1(<id_grammar.py bytes, CRLF folded to
LF>).hexdigest()[:12]`, read through `__file__`. Every other term of the blob is unchanged.

### The staged break (DA-H4)

In a scratch clone, one behaviour-bearing line of `id_grammar.py` is changed and committed with
`KIT_MEMORY_TREE_VERSION` unmoved; `check-verdict-epoch.sh <base>` exits 1 naming the module. Before
this unit the same edit to `extract.py` was caught only when the recall kit resolved
(`check-verdict-epoch.sh:179-182`). A second break removes `${_kit}id_grammar.py` from DELEGATES,
and the import-closure walk exits 2 naming it and an importer.

### Migration

Additive for an adopter that installs both kits: memory-recall's three files still export every name.
An adopter with memory-tree alone gains checks 13-16 and 26 without the sibling. An adopter whose
memory-recall predates this unit and whose memory-tree is current runs the old recall files, which
still carry their own grammar; recall's next update re-exports. Both kit versions bump at the lander.

### Rollout

Live at landing; no switch, since the move changes no verdict on gov's tree (AC4, AC5).

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py` (new)
- `tools/memory-recall/extract.py`
- `tools/memory-recall/recall_conf.py`
- `tools/memory-recall/bench.py`
- `tools/memory-tree/backlog.py`
- `tools/memory-tree/corpus_ids.py`
- `tools/memory-tree/merge-rows.py`
- `tools/memory-tree/transition_audit.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/migrate_backlog.py`
- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/merge-rows.test.sh`
- `tools/memory-tree/transition-audit.test.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `.githooks/straggler-guard.test.sh`
- `tools/check-wiring.test.sh`

### Alternatives rejected

- **A copy of the grammar in memory-tree, recall keeping its own.** Two grammars that disagree
  silently are the defect `grammar_for`'s docstring records (`tools/memory-recall/extract.py:573-583`).
- **Two modules, the grammar and the index names apart.** The dependency check would then join two
  files for one population; the brief's S1 fixes one module, and nothing in the clause splits it.
- **Re-pointing by-path readers in a later unit.** The clause forbids it, and DELEGATES would red in
  between (`check-verdict-epoch.sh:206-266`).

## 5. Production-readiness checklist

- security: no new write path; the module reads the conf and the tree as `recall_conf.py` and `extract.py` did.
- perf / scale: one lazy grammar build per process, the cost `extract.py` paid at import; the digest reads one file of about 40 KB, DERIVED at the pass by `wc -c`.
- error / empty / loading states: a conf refusal is raised as `ConfError` on first use, never at import; an absent `id_grammar.py` in an install is an ImportError named by each caller's existing refusal text, re-worded to name memory-tree.
- observability: unchanged lines; each re-worded refusal names `id_grammar.py`.
- risks: a reader the two queries miss, a computed path or an `importlib` load, survives the move; unit 16's check over those kinds is what finds one.
- testing: AC1 to AC10, and the suite arms of S9 at the close.
- migration: §4 "### Migration".
- user docs: N/A — no user-facing surface moves; `tools/memory-recall/README.md` names the grammar's new home in one line.

## 6. Acceptance criteria

- **AC1** — When `git grep -nE "^(def (grammar_for|anchor_at|repo_root|resolve|corpus_inputs|extract_records|extract_supersessions|derive_supersession_map|build_index|match_expr|terms)\b|class (Grammar|Conf)\b|ALIAS_WEIGHT =)" -- tools` runs, every hit is in `id_grammar.py`.
  Red when: a definition stays in `tools/memory-recall/`, so two copies exist.
- **AC2** — When the first query of §4 "### The inventory query" runs after the pass, every hit is a
  `keep` row of that section or a comment that narrates history, and the pass commit's `Decided:`
  trailer names each kept reader.
  Red when: a reader that reaches a moved name by path is still listed.
  figure: the count is DERIVED by the query at the pass.
- **AC3** — When the second query of §4 "### The inventory query" runs, it prints nothing; run at
  `ce13efbe` in a scratch clone, it prints at least the `backlog.py:1808` import.
  Red when: a reader still imports a moved name from the recall kit.
  fixture: a clone at `ce13efbe` under `%TEMP%`, for the liveness half.
- **AC4** — When `python tools/memory-recall/extract.py . <out> --rev ce13efbe` runs on the tree after
  the pass and in a clone at `ce13efbe`, `cmp` finds the two output directories' files identical, and
  `python tools/memory-recall/query.py "where does the id grammar live" --terms "id grammar anchor extract recall memory-tree kit move grammar_for anchor_at"` exits 0 with at least one hit.
  Red when: a moved name's behaviour changed in the move, or recall no longer imports.
  fixture: both runs write under the run's scratch path.
- **AC5** — When a scratch copy of the tree with `tools/memory-recall/` deleted runs
  `python tools/memory-tree/corpus_ids.py --print-defined-ids`, it exits 0 and prints ids, and
  `python tools/memory-tree/gotchas.py --for-paths tools/memory-tree/` exits 0 with no line naming
  memory-recall; at `ce13efbe` the first exits 3.
  Red when: a memory-tree module still needs the recall kit for the grammar, or `id_grammar` resolves
  a conf at import.
  fixture: a copy under `%TEMP%`, since the deletion must not touch the worktree.
- **AC6** — When a scratch clone commits one changed non-comment line of
  `id_grammar.py` with `KIT_MEMORY_TREE_VERSION` unmoved and runs
  `bash tools/memory-tree/check-verdict-epoch.sh <the clone's base>`, it exits 1 naming
  `id_grammar.py`; with `${_kit}id_grammar.py` deleted from DELEGATES it exits 2 naming it and an
  importer; without either plant it exits 0.
  Red when: the scan set does not hold the moved module, so its change dates nothing.
  fixture: a clone under `%TEMP%`.
- **AC7** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import id_grammar as g; print(g.resolve().digest())"` runs before and after a comment line is appended to `id_grammar.py` in a scratch copy, the two digests differ; and `git grep -nE "recall_conf|KIT_MEMORY_RECALL_VERSION" -- tools/memory-tree/` prints nothing.
  Red when: the digest folds no grammar epoch, or memory-tree reads a recall constant.
- **AC8** — When a scratch clone sets `RECALL_CLI=""` in `.unattended.conf`, plants a file in one build
  folder whose row anchors another build's id, and calls `scan_foreign_anchors` on that folder from a
  shell that sources the function out of `tools/unattended/check-unattended.sh`, it returns 0 and
  `ASK_ANCHORS` names the planted line; at `ce13efbe` the same call returns 1 with the blank-key reason.
  Red when: the arm still reaches the grammar through `RECALL_CLI`.
  permission: the unattended kit's suite is waived for this landing (README rule 8), so this is a direct call of the changed function on a fixture, never its suite.
  fixture: a clone under `%TEMP%`.
- **AC9** — When `grep -c 'kit = "memory-recall"' tools/memory-tree/kit.toml` runs, it prints `0`.
  Red when: a `requires_if` row still declares an edge the move removed.
- **AC10** — When a scratch copy changes `KIT_MEMORY_RECALL_VERSION` in `tools/memory-recall/recall_conf.py`
  alone and runs `bash tools/check-kit-versions.sh`, it exits non-zero naming the constant.
  Red when: the version reader lost its file in the move.

## 7. Gates

`verdict epoch (kit version dates the engine)` · `kit version markers` · `memory hygiene` · `recall floor` · `row-driver view refusal` · `drift-audit records` · `unattended kit gate` · `drift-audit selftest` · `lexicon naming predicates` · `manifest-check self-test` · `scratch-guard self-test` · `tier2-review self-test` · `transition-audit arms` · `straggler-guard arms`

New arm: tools/memory-tree/check-verdict-epoch.test.sh · covers AC6 · a case staging a changed line of `id_grammar.py` with the constant unmoved, and one dropping it from DELEGATES · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC5 · the F1 arm hides memory-recall's `extract.py` and now asserts ids are checked, no NOTE · none
New arm: tools/memory-tree/merge-rows.test.sh · covers none · the fixture copies `id_grammar.py` instead of the recall pair, and the absent-grammar arms plant an absent `id_grammar.py` · none
New arm: tools/memory-tree/corpus_ids.py · covers AC5 · the selftest's `nowhere` and `oldkit` plants re-planted as an absent and an outdated `id_grammar.py` · none
New arm: tools/memory-tree/row_grammar.py · covers none · check 27's two refusal arms re-planted on `id_grammar.py` · none
New arm: tools/check-wiring.test.sh · covers none · the dead-grammar AC10 arm redefines `anchor_at` in `id_grammar.py` · none

## 8. Open questions

- **F1 — Which epoch `Conf.digest` folds once it moves.** Options: (a) keep folding
  `KIT_MEMORY_RECALL_VERSION`, which makes the core read a recall constant, the edge unit 16 refuses;
  (b) fold `KIT_MEMORY_TREE_VERSION`, read from `check-memory-hygiene.sh:68`, which moves on every
  memory-tree bump and rebuilds the recall cache about 6 s each time for changes that are not the
  grammar's; (c) fold the hash of `id_grammar.py`'s own bytes, which moves exactly when the grammar's
  code does and is derived rather than typed. RESOLVED (agent, 2026-10-23, delegated): (c), rung 3,
  the most capable survivor of the vetoes; the digest's own docstring states the property it wants,
  the term moving when the grammar moves, and (c) has it without a typed constant. widens: none ·
  relaxes: none
- **F2 — Whether `check-kit-versions.sh` is re-pointed.** The brief puts it in the inventory. It reads a
  constant that stays. RESOLVED (agent, 2026-10-23, delegated): kept, its arm re-observed (AC10),
  rung 1: the clause re-points the moved grammar's consumers, and this reader consumes no moved name.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.

## 10. Reuse audit

The seam extended is the grammar itself: `grammar_for`, `anchor_at`, `Grammar`
(`tools/memory-recall/extract.py:551-601`) and `resolve`, `Conf.digest`, `repo_root`
(`tools/memory-recall/recall_conf.py:66,207-271,277`), moved and not rewritten, and the
`resolve_kit_dir` copy recall already carries (`tools/memory-recall/extract.py:66`), through which
recall reaches memory-tree. `reuse_lookup.py "move a shared module into another kit and re-point every
reader that loads it by path"` ranked `read`, `load_conf` and `resolve_kit_dir` (fan-in 12, installs
72): the last is the probe every by-path reader goes through, which is why the first query anchors on
file names rather than on it. No seam re-points readers; the query is the scout's
(`2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md:21`). Where the scout and source disagree:
`check-unattended.sh`'s `RECALL_CLI` probe that reads `extract.py` is at `:2028-2065`, not `:267`,
which is the key's declaration; the scout's list missed the by-name readers of `bench.py`
(`tools/memory-tree/row_grammar.py:1020`, `check-memory-hygiene.test.sh:3947`), which this spec adds.

Recall terms used: `python tools/memory-recall/query.py "how were memory-recall's extract.py and recall_conf.py readers found by path and re-pointed when the grammar moved" --terms "extract.py recall_conf grammar_for anchor_at resolve_kit_dir DELEGATES scan set verdict-epoch by-path reader memory-recall memory-tree"`
