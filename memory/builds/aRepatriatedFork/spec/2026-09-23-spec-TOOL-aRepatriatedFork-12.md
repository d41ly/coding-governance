# TOOL-aRepatriatedFork-12 — memory-recall reads the adopter's corpus shape from conf

**Status:** CLOSED · rev-3 · 2026-09-24 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-24-build-TOOL-aRepatriatedFork-12-1-acceptance-ledger.md](../build/2026-09-24-build-TOOL-aRepatriatedFork-12-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-TOOL-aRepatriatedFork-12-build-brief.md](../prompts/2026-09-23-prompt-TOOL-aRepatriatedFork-12-build-brief.md) | journal | — |
| [2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md](../reviews/2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md) | diff-review | DEPL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

The memory-recall kit hardcodes four facts about a corpus that belong to the adopter: the node-tag
class, which families an id may carry, where rotated archives live, and where a node's traffic
export goes. inCMS therefore cannot run `tools/memory-recall/extract.py` or `query.py` verbatim, and
its forks of both sit `forked`/`unattributed` in the receipt. This unit moves those facts into
`.memory-tree.conf` keys read by `tools/memory-recall/recall_conf.py`, so inCMS runs gov's bytes
and declares its shape in four conf lines.

## 2. Scope (IN)

- **S1** — `RECALL_NODE_TAG_CLASS`, an optional conf key holding the body of a regex character class
  (`a-f`, `a-z`). Absent means `a-z`, today's constant at `tools/memory-recall/recall_conf.py:43`,
  so no adopter's grammar moves without a declaration. A value outside `[a-z0-9-]+` is a ConfError
  refusal, never a silent fallback. Observed by AC2 and AC6.
- **S2** — `RECALL_CITED_FAMILIES`, an optional space-separated list of family tokens the id grammar
  RECOGNISES but the corpus does not HOME. Each token joins the `ID` alternation built at
  `tools/memory-recall/extract.py:106` and does NOT join the `_IDX` alternation that `DURABLE` builds
  at `:144`, so a cited family gains ids and gains no durable home. A token failing `_FAMILY_RE`
  (`recall_conf.py:154`) or already in `FAMILIES` is a refusal. Observed by AC3 and AC6.
- **S3** — `DURABLE`'s archive alternation at `tools/memory-recall/extract.py:148` admits one
  optional directory segment AFTER `archive/` as well as before it. No key: the widening is inert on
  every tree measured and exact on the one that needs it (§4 Data model). Observed by AC1.
- **S4** — `RECALL_BUILD_QID_CUTOFF`, an optional conf key of `<tag>:<qid>` pairs, replaces the code
  literal `BUILD_QID_CUTOFF: dict[str, int] = {}` at `tools/memory-recall/query.py:174`. The
  literal's own comment (`:160-163`) already says rows are added "only from a value READ from that
  node's live log", which is adopter data sitting in a file `govkit update` overwrites. Observed by
  AC4.
- **S5** — `RECALL_EXPORT_DIR`, an optional repo-relative directory for `query.py --export`. Absent
  or blank keeps today's destination beside the log under the common git dir
  (`tools/memory-recall/query.py:1096`). A value resolving outside the repo root is refused before
  any write. The export's header sentence claiming the file sits OUTSIDE the worktree (`:969-971`)
  is rendered from the resolved destination rather than asserted. Observed by AC5.
- **S6** — `Conf.digest()` (`recall_conf.py:204-230`) keeps hashing `node_tag_class` and gains the
  cited families, because both change which strings are ids. The cutoff and the export dir stay out
  of it, as the cache budget already does (`:196-199`). `recall_conf.py` prints the four resolved
  values beside the existing KEY=VALUE lines (`:294-298`). Observed by AC6.
- **S7** — `KIT_MEMORY_RECALL_VERSION` moves from `1.11` to `1.12`, because S1 through S3 change the
  grammar and the digest carries the version (`recall_conf.py:229`). The kit read `1.9` when this
  spec was drafted; `TOOL-aRepatriatedFork-2` and `-3` took it to `1.11` on this branch first.
  `tools/memory-recall/README.md` documents the four keys, and its sentence at `:43` saying the node-tag class "is not a conf key"
  is rewritten. Observed by AC7.
- **S8** — The adopter half, recorded here so the build can observe it: inCMS declares
  `RECALL_NODE_TAG_CLASS="a-f"`, `RECALL_CITED_FAMILIES="PKG"`, `RECALL_BUILD_QID_CUTOFF="a:163"`,
  `RECALL_EXPORT_DIR="memory/archive/project"` and `RECALL_CACHE_BUDGET_MB="2048"`, and takes gov's
  `extract.py`, `query.py` and `recall_conf.py` byte-for-byte. §4 `### Adopter deletions` lists what
  goes. Observed by AC8.

## 3. Non-goals (OUT)

- Node-letter auto-derivation. inCMS `scripts/recall/query.py:760-797` parses `CLAUDE.md`'s node
  registry so `--export` needs no `--tag`; gov removed it on purpose (`query.py:905-908`) and
  requires `--tag` (`:1179-1187`). No automated caller in inCMS passes `--export` without `--tag`
  (measured 2026-09-23: `git grep` over `.claude/`, `scripts/` and the charter finds only prose). gov
  already carries three registry parsers that disagree on the match rule —
  `tools/drift-audit/drift_report.py:2073`, `tools/playbook/render_playbook.py:153` and
  `skills/session-kickoff/manifest-check.sh:202` — and a fourth is the catalogue-drift class. §8 F2.
- inCMS's `scripts/recall/selftest.py` and `scripts/check_recall.py`. Both are `project-owned` at
  inCMS by the receipt and by `.governance/kits.json`. With gov's `query.py` the selftest's
  in-process `Q.main` calls inside `_throwaway_repo()` (inCMS `scripts/recall/selftest.py:470-487`)
  resolve the REAL repo, because gov anchors `repo_root()` on the kit's own file
  (`recall_conf.py:50-116`, `TOOL-aCollapsedScan-7`). They log synthetic refusals into the live
  shared log, and `_log_rows` (`:945-947`) then reads an absent fixture log. gov met the same defect
  in its own selftest on 2026-09-22 and repaired the SUITE by running a fixture copy of the kit
  (`tools/memory-recall/selftest.py:1620-1627`). The repair is the same at inCMS and is inCMS work.
- The recall-opened fragment's `{kit}/memory-recall/` token and `corpus_ids.py`/`merge-rows.py`
  looking for the recall kit only at gov's two homes. Both are prefix-derivation defects, and the
  brief assigns them to `TOOL-aRepatriatedFork-2`; this unit does not name that unit as an edge
  because nothing here rests on it.
- A conf key for the cache budget. `RECALL_CACHE_BUDGET_MB` exists (`recall_conf.py:265`); inCMS only
  declares it.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-19` — inCMS's `scripts/check-wiring.sh:549` seds the
  family list out of `scripts/recall/extract.py`'s `FAMILIES = (…)` tuple. gov's `extract.py` spells
  `FAMILIES = CONF.families` (`:68`), so the sed reads nothing and the merge arm reports UNWIRED
  (`:560`). inCMS cannot take this unit's bytes until it can take gov's `check-wiring.sh`, which
  already reads the conf (`tools/check-wiring.sh:784`). AC8 rests on that.
- **hands-off** external — inCMS's recall selftest fixture repair, per the second non-goal above.
- **hands-off** `DEPL-aRepatriatedFork-20` — gov's `extract.py` running at inCMS, which gov's
  `corpus_ids.py` and `merge-rows.py` import `grammar_for` from after the convergence.

## 4. Design

### Data model

Four new keys in `.memory-tree.conf`, all optional, all read only by `recall_conf.resolve()`
(`tools/memory-recall/recall_conf.py:236-270`), which is already the kit's single reader. No flag
is added anywhere: the module docstring (`:13-16`) forbids a second declaration channel, and this
unit keeps that rule.

| Key | Absent means | Shape | In `digest()` | Read by |
|---|---|---|---|---|
| `RECALL_NODE_TAG_CLASS` | `a-z` | `[a-z0-9-]+` | yes | `extract._eras` via `Conf.node_tag_class` |
| `RECALL_CITED_FAMILIES` | none | `_FAMILY_RE` tokens, disjoint from `FAMILIES` | yes | `extract.FAMILIES` for `ID`, never `_IDX` |
| `RECALL_BUILD_QID_CUTOFF` | `{}` | `<letter>:<int>` pairs | no | `query.build_cutoff` |
| `RECALL_EXPORT_DIR` | common git dir | repo-relative, inside root | no | `query.export` |

`FAMILIES` keeps meaning "families this corpus homes". That is what every other reader of the key
needs: `tools/memory-tree/check-memory-hygiene.sh:260-279` builds the rotated-archive and
build-folder alternations from it, and `tools/check-wiring.sh:849-865` requires every family a
merge=rows index row LEADS with to be declared there. A cited family belongs in neither place.
Measured on inCMS on 2026-09-23 (PINNED): the rows of `memory/DECISIONS.md` and
`memory/backlog/*.md` lead with ten families and zero `PKG`, while inCMS cites 22 `PKG-*` ids
(`scripts/check-docs-hygiene.sh:1293`) and waives 13 of them in check 17.

The archive widening, measured over `git ls-files <MEMORY_ROOT>` with each tree's own conf on
2026-09-23 (PINNED; re-derive by applying both patterns to the listing):

| Tree | gov `DURABLE` | widened | inCMS local `DURABLE` |
|---|---|---|---|
| gov (`PLAY KICK TOOL DEPL`) | 9 | 9 | — |
| nc (`PKG BRAND`) | 13 | 13 | — |
| inCMS (ten families) | 56 | 71 | 71, the same 71 files |

The 15 inCMS files the widening admits are exactly `memory/archive/<discipline>/{DECISIONS,BACKLOG}.<date>.md`,
which inCMS's own pattern (`scripts/recall/extract.py:75-80`) already selects. That is audit-B §9's
"stage A is EMPTY" failure in inCMS's `check_sieve_stages_are_ordered_disjoint_and_closed`.

### Inventory

- Conf keys: `RECALL_NODE_TAG_CLASS`, `RECALL_CITED_FAMILIES`, `RECALL_BUILD_QID_CUTOFF`,
  `RECALL_EXPORT_DIR`. The repo declares no naming cell for conf keys; they follow the existing
  `RECALL_*` family (`RECALL_CACHE_BUDGET_MB`, `RECALL_EXTRA_SOURCES`, `RECALL_FLOOR`).
- `Conf` gains slots `cited_families`, `build_qid_cutoff` and `export_dir` (`py.type` cell for the
  class is unchanged; attributes are not graded).
- No new function. `build_cutoff` (`query.py:177`) reads the conf instead of a module dict, and the
  module name `BUILD_QID_CUTOFF` stays as the resolved value so its two readers
  (`query.py:179`, `:990` in prose) keep spelling it.

### Migration

gov's own `.memory-tree.conf` declares none of the four keys and keeps every current value. nc
declares none and keeps them too; nc runs the recall kit verbatim today (measured: zero diff lines
on `extract.py`, `query.py`, `recall_conf.py` and `recall-opened.fragment.json` against a7c78ad2),
so nc is this unit's control. The version bump rebuilds every warm cache once, which
`Conf.digest()` already accepts as the price of a kit bump (`recall_conf.py:222-225`).

### Adopter deletions

inCMS, once it holds gov's three files and the five conf lines:

| Artefact | Where | Action |
|---|---|---|
| `scripts/recall/extract.py` fork | receipt row `forked`/`unattributed` | gov bytes, row re-measured `engine` |
| `scripts/recall/query.py` fork | receipt row `forked`; kits.json `project-owned` | gov bytes; kits.json row to `engine` |
| `owned_why` for `scripts/recall/query.py` | `.governance/kits.json` memory-recall | deleted; its "no behaviour gov lacks" claim is contradicted by audit-B §10 |
| `version_none` for memory-recall | `.governance/kits.json` | deleted; it says inCMS "does not carry" `recall_conf.py`, and inCMS carries it byte-identical to gov |
| `role_dispositions` rows for `extract.py` and `query.py` | `.governance/kits.json` | deleted |
| `BUILD_QID_CUTOFF = {"a": 163}`, `DEFAULT_CACHE_BUDGET_MB = 2048.0` | inCMS `scripts/recall/query.py:135`, `:102` | become conf lines |
| INCMS PATCH 5 | `scripts/check-wiring.sh:545-566` | goes with the `TOOL-aRepatriatedFork-19` pull |

nc deletes nothing.

### Files touched (estimate)

- `tools/memory-recall/recall_conf.py`
- `tools/memory-recall/extract.py`
- `tools/memory-recall/query.py`
- `tools/memory-recall/selftest.py`
- `tools/memory-recall/README.md`
- `tools/memory-recall/SKILL.template.md`

### Alternatives rejected

- **Declare `package:PKG` in inCMS's `FAMILIES`.** audit-B §9 measured that it clears the 13 PKG
  rows. It also puts PKG into the hygiene engine's rotated-archive and build-folder alternations and
  into check-wiring's merge-family join, none of which should know a family with no home. One
  declaration would carry two meanings.
- **A `RECALL_ARCHIVE_LAYOUT` key.** Every measured tree is served by the one widened pattern, and a
  key nobody needs to set is a knob with one value.
- **An env override or a `--tag-class` flag.** The docstring at `recall_conf.py:13-16` records why
  the kit has no flags; an env var is the same second channel and leaves no diff.

## 5. Production-readiness checklist

- security — `RECALL_EXPORT_DIR` is a write destination, so it is resolved and refused when it
  escapes the repo root, before the file is opened. The export stays aggregate-only
  (`query.py:939-942`); a tracked destination carries no query text.
- perf / scale — one extra alternation branch per cited family in `ID_RE`; one cache rebuild per
  adopter at the version bump.
- error / empty / loading states — every malformed value is a `ConfError` carrying the key, the
  value and the accepted shape, printed by `recall_conf.py`'s refusal path (`:290-292`), exit 2.
- observability — `python tools/memory-recall/recall_conf.py` prints the four resolved values.
- risks — a cited family that later gains a home must move to `FAMILIES`; S2's disjointness refusal
  makes a stale double declaration loud rather than silent.
- testing — selftest arms per key, each observed red against the pre-change parse (§7).
- migration — none for gov or nc; inCMS per §4 `### Adopter deletions`.
- user docs — `tools/memory-recall/README.md` and the rendered Skill's conf section.

## 6. Acceptance criteria

- **AC1** — When `extract.DURABLE`, imported at gov's root, is searched against the inCMS-shaped
  path memory/archive/architecture/DECISIONS.2026-07-27.md it matches, and applied to
  `git ls-files memory` it selects the same 9 files it selects at a7c78ad2.
  Red when: the archive alternation still requires the segment before `archive/` and the search
  returns `None`.
  figure: 9 is PINNED 2026-09-23 against gov's tree.
- **AC2** — When a scratch repo's `.memory-tree.conf` declares `RECALL_NODE_TAG_CLASS="a-f"`,
  `python <kit>/recall_conf.py` prints `NODE_TAG_CLASS=a-f` and `extract.ID_RE` does not match
  `ARCH-xFoo-3`; with the key absent it prints `NODE_TAG_CLASS=a-z`, and with `a-f]` it exits 2
  naming the key.
  Red when: the value is ignored and `a-z` is printed, or `a-f]` reaches the regex.
- **AC3** — When the conf declares `FAMILIES="architecture:ARCH"` and
  `RECALL_CITED_FAMILIES="PKG"`, `extract.ID_RE` matches `PKG-dCandidLodestar-5` and
  `extract.DURABLE` does not match the path memory/backlog/PKG.md; `RECALL_CITED_FAMILIES="ARCH"`
  exits 2.
  Red when: PKG is not an id, or it gains a durable home, or the overlap is accepted.
- **AC4** — When the conf declares `RECALL_BUILD_QID_CUTOFF="a:163"`, `query.build_cutoff("a")`
  returns `163` and `query.build_cutoff("b")` returns `0`; `"a163"` exits 2 naming the key.
  Red when: the conf value is not read and `build_cutoff("a")` returns `0`.
- **AC5** — When the conf declares `RECALL_EXPORT_DIR="memory/archive/project"`,
  `python <kit>/query.py --export --tag a` writes recall-traffic-a.md under that directory inside
  the scratch repo; with `"../out"` it exits 2 and writes nothing; with the key absent it
  writes under the common git dir exactly as today.
  Red when: the key is ignored, or a traversal value writes outside the root.
- **AC6** — When `RECALL_NODE_TAG_CLASS` or `RECALL_CITED_FAMILIES` changes, the `CONF_DIGEST` line
  of `python <kit>/recall_conf.py` changes; when only `RECALL_BUILD_QID_CUTOFF` or
  `RECALL_EXPORT_DIR` changes, it does not.
  Red when: a grammar key leaves a warm cache valid, or a non-corpus key forces a rebuild.
- **AC7** — When `bash tools/check-kit-versions.sh` runs, it exits 0 with
  `KIT_MEMORY_RECALL_VERSION = "1.12"`, and `grep -n 'not\*\* a conf key' tools/memory-recall/README.md`
  prints nothing.
  Red when: the shipped bytes moved and the version did not, or the README still denies the key.
- **AC8** — When gov's three recall files and the §2 S8 conf lines are placed in a shared clone of
  inCMS, its `recall_conf.py` prints `NODE_TAG_CLASS=a-f`, and its `corpus_ids.py --check ids`
  reports no `PKG-*` row and no `ARCH-xFoo-3` row.
  Red when: either class of row survives, which is audit-B §9's measured state.
  permission: inCMS is another repository; the observation runs in a `git clone --shared` scratch
  clone, as audit-B's did, and edits nothing in inCMS.
  fixture: the clone also needs gov's `check-wiring.sh` (the Edges consumes-from) or its merge arm
  reds on the family sed. Per §8 F3, `corpus_ids.py`'s sieve classes `PERF-aSwiftHourglass-2` as
  `grammar`, the class inCMS's own `extract.py` gives it.
  cost: about a minute for the clone and one `corpus_ids.py` pass.

## 7. Gates

`memory-recall kit selftest` · `memory-recall skill wiring` · `recall floor` · `recall floor arms` · `row-keyed merge driver replay` · `hook destinations self-test` · `kit version markers` · `lexicon naming predicates`

New arm: `tools/memory-recall/selftest.py` · a fixture conf per key, each observed against the
pre-change `resolve()` that ignores it, plus the archive-segment path against the a7c78ad2
`DURABLE` · none

## 8. Open questions

- **F1 — should `RECALL_NODE_TAG_CLASS` live in the memory-tree conf contract rather than recall's?**
  The memory-tree hygiene engine admits `node [a-z]` in a status header
  (`tools/memory-tree/check-memory-hygiene.sh:1275`) and inCMS's registry uses `a-f`. Option (a):
  a recall-scoped key, as specified. Option (b): a memory-tree `NODE_TAGS` key that both kits read.
  Recommendation: (a). The hygiene engine accepts any letter by design and only the id grammar pays
  for a wide class; (b) is the right move when a second reader appears, not before.
  RESOLVED (owner, 2026-09-23): (a), a recall-scoped key, as recommended.
- **F2 — should gov ship a node-tag derivation for `--export`?** Recommendation: no, per §3. If the
  owner wants it, the precondition is ONE registry reader replacing the three gov already has,
  which is its own unit.
  RESOLVED (owner, 2026-09-23): no, as recommended.
- **FACT-QUESTION · F3 — why does `PERF-aSwiftHourglass-2` move from `grammar` to `glossed` under
  gov's `extract.py`?** audit-B §9 measured the move and did not explain it. The id sits at inCMS
  `memory/backend-test-harness.md:8` and in `scripts/corpus-id-unresolved.txt:75`. Probe: diff
  inCMS `scripts/corpus_ids.py`'s classification of that one line under both `extract.py` builds.
  Recommendation: answer it before AC8 is observed, because a grammar difference this spec did not
  name is a fifth hardcoded fact.
  RESOLVED (agent, 2026-09-24, delegated): not a fifth fact; it is S3. The probe was run. That id's
  one citation in a record home is `memory/archive/performance/DECISIONS.2026-07-27.md:144`, and
  stage A of the sieve fires only on a `RECORD_HOME` (`extract.DURABLE`) path. gov's `DURABLE` at
  a7c78ad2 returns no match for that path; inCMS's and the S3-widened one both match. With no stage
  A hit the id falls to stage B, which `memory/backend-test-harness.md:8` glosses. Liveness: the
  same probe returns a match for the widened pattern, so it can produce either answer. AC8 stops
  excluding the id and observes that it classifies `grammar` again.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, from the brief's unit 12 and audit-B §9 and §10, with the
  archive-pattern and leading-family measurements taken for this spec.
- rev-2 · 2026-09-23 · §3 gains the **hands-off** edge back to `DEPL-aRepatriatedFork-20`,
  which declared its **consumes-from** here and met no matching edge (hygiene check 12).
- rev-3 · 2026-09-24 · S7 · AC7 · AC8 · §8 F3 · the version target moves from `1.10` to `1.12`,
  because two earlier units of this build took the kit to `1.11` first. F3 is resolved by its stated
  probe, and AC8 now includes the id it had excluded. S2 also reaches `extract.grammar_for(root)`,
  the accessor `corpus_ids.py` and `drift_report.py` call, because it builds its own `ID`.

## 10. Reuse audit

The seam is `recall_conf.resolve()` in `tools/memory-recall/recall_conf.py`, which
`reuse_lookup.py` ranks with `load_conf` (fan-in 15) and `grammar_for` (fan-in 4) as the corpus's
existing answer; every key here extends that one reader, and `RECALL_CACHE_BUDGET_MB` and
`RECALL_EXTRA_SOURCES` are the precedent for an optional recall-scoped key. The recall probe
surfaced `TOOL-aQuarriedLantern-1`, whose §8 Q1 left the node-tag key open, and
`TOOL-aWeighedCompass-5`, which first made `DURABLE`'s directory segment optional.

Recall terms used: `NODE_TAG_CLASS`, `recall_conf`, `FAMILIES`, `DURABLE`, `archive`, `rotated`,
`BUILD_QID_CUTOFF`, `export`, `tag`, `conf_digest`, `grammar_for`, `forked`.
