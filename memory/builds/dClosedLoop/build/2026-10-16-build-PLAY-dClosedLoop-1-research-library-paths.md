# Research: memory's library side, its four filling paths and two placements

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 49's return, verbatim, except that its title line is demoted to keep one H1 per
record. Its question is in `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-18-researcher.md`, and its
use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md`.

---

**Library side: four filling paths and two placements (dClosedLoop, PLAY-dClosedLoop-1)**

All four paths are filled by hand today, and nothing notices when a path is skipped. The repo already has a seam for each one: the review harness's appendix column, the spec's §10 reuse seam, hygiene check 27 and the `**Serves:** research` binding. My picks extend those seams. On the placements: dossiers should stay with the map, and the annotation index is not core. Everything below was read-only; scratch scripts went to the session scratchpad.

## Inventory

| Path | Writer today | Trigger | Record written | Readers | What lets it be skipped |
|---|---|---|---|---|---|
| Finding → bug class | Hand-authored `memory/gotchas/<slug>.md` in a fold commit | Prose only: "Left-shift every confirmed finding … a finding fixed and not left-shifted returns" (`memory/guides/BUILD-METHOD.md:275-276`) | A class record (front matter `name`, `description`, `kind`, `universal`; `gotchas.py:233-258`) | `gotchas.py --for-diff/--for-paths` checklist (`gotchas.py:776`, `BUILD-METHOD.md:186-191,253`); the harness's `checklist` → lenses (`tools/workflows/tier2-review.js:450-489,854-860`) | No check joins confirmed findings to classes. `--for-diff` exits 0 whenever it prints (`BUILD-METHOD.md:193`). |
| Feature → reuse entry | None. Nearest: dossier `seam:` paragraphs, the spec's §10 seam, the card's `**Reuse:**` | Spec §10 "seam you will extend … or no existing seam fits" (`BUILD-METHOD.md:160-162`); card field (`skills/session-kickoff/MANIFEST-TEMPLATE.md:59`, `manifest-check.sh:89`) | Dossier prose; card in `.git/orientation/<sid>.md` (`manifest-check.sh:312-316`), untracked | `reuse_lookup.py`, the roles skill reading the card (`tools/roles/SKILL.template.md:41`) | Nothing proposes. The card is transient. `gov:feature` appears in 0 code lines (measured below). |
| Decision → log row | Hand edit to `memory/DECISIONS.md` in any commit; `merge-rows.py` only merges (`merge-rows.py:6-9`) | None. M9 lists "rows this build minted" as an input (`BUILD-METHOD.md:299`) | One bullet row | Recall spine (`tools/memory-recall/extract.py:27-28,222-225`), row_grammar checks 20/24/27/28, `corpus_ids.py`, `reuse_lookup.py:98-120`, drift-audit | No rule requires a row, and no predicate says what is major. |
| Research → library | Researcher writes `build/…-research*.md`, headed by `**Serves:** research <id>` | `plan.research` / `design.research` dispatch | A research record bound by kind (`memory/HYGIENE.md:574-575`) | `gen_build_index.py --print-bindings`; recall's chunk set (`extract.py:30-31,302-320`) | Nothing indexes research for planners except recall, which is optional. |

| Placement | Today |
|---|---|
| Dossiers | `memory/map/features/*.md`, 31 files. Hygiene reads them only when `MAP_SUB` is set (`tools/memory-tree/check-memory-hygiene.sh:903,1094`), so they are map-dependent. |
| Annotation index | No persisted index exists. drift-audit builds an in-memory cited-id map at report time (`tools/drift-audit/drift_report.py:2201-2247`). Its signal is "Gateable: no" (`tools/drift-audit/README.md:121,147`). Each `gov:` marker kind is grepped inline by its own reader (table under Measurements). |

**What `gotchas.py --check` grades when a class is written** (`gotchas.py:493-564`):

- 17: INDEX is fresh.
- 18: the body names a gate or says "no machine gate" (`DECLARES_RE`, `:74`).
- 19: the record derives an anchor or is marked universal, its anchors are not inert, and universal records stay under budget.
- Checks 27 and 28 in hygiene: a near-duplicate must name its relation, and duplicate text is refused (`HYGIENE.md:531-561`). 27 is armed `red:0.125` (`.memory-tree.conf:725`).

None of these checks reads a review.

## Sequence

1. **Finding → class.** The tier2 harness writes an appendix with a `classes` column. That column is filled only when a finding's claim opens with a checklist label `C<n>`, which maps to an existing slug (`tier2-review.js:1501-1514,1532,1560-1566`). The fold fixes blockers. Left-shifting the rest is prose. A new class is hand-written later, and nothing in the class points back to the finding or the review.
2. **Feature → reuse.** The spec's §10 records the seam it extends. The unit builds. If the map is installed, someone may add a `seam:` paragraph to a dossier. Nothing marks the code and nothing reaches the owner.
3. **Decision → row.** An author appends a row by hand. On a full run, hygiene checks 7 (300-char cap, `HYGIENE.md:257`; `check-memory-hygiene.sh:154,1084`), 20 (one id per document), 24 (rotation), 27 and 28 grade it.
4. **Research.** The researcher writes a bound record, and check 21 grades the binding. Its only cross-build reach is recall's chunks, or a reader who already knows the file name.

## Measurements

**P1. Classes and findings** (appendix parser over every review carrying the 9-column header):

```
files 36 confirmed with class 183 without 724
non-dClosedLoop files 24 with 109 without 258
distinct classes cited 60
class names resolving to a record 50 of 60 unresolved ['C14','C66','C41','C18','C64','C17']
```

- 60 appendices exist in total. 24 older ones have no `classes` column (8-column header).
- The 10 unresolved names are the harness's bare-label fallback (`tier2-review.js:1510`).
- A filled `classes` cell means the finding matched an existing class. It never means a class was filed for the finding.

Provenance of the 124 records (125 files minus INDEX: 121 `class`, 3 `invariant`, 0 `note`):

```
cite reviews/ path: 9 · cite -review- filename: 7 · review-path OR finding-number: 13
cite a unit id: 75 · neither unit id nor review cite: 47 · "## Where it bit": 100
```

No front-matter key carries provenance. The only keys used are `name`, `description`, `kind`, `universal` and `decision`.

- 109 class files were added in 60 days, in 70 commits.
- No backlog shard row uses the literal kind `LEFT-SHIFT OWED`. `memory/backlog/TOOL.md` has 4 left-shift asks, 2 of them DEFERRED.

**P2. Reuse records and how often later builds find them:**

```
specs: 1322 · cite a dossier: 308 · say no seam fits: 256 (in 67 of 163 builds)
specs since 2026-09-15: 656, of which cite dossier: 150
"MUST reuse" in any spec: 2
stored cards: 20 · with **Reuse:** filled: 4 · "no seam fits": 0
seam: lines added to dossiers in 60d: 55 · new non-test .py/.sh/.js under tools in 60d: 87
git grep 'gov:feature [a-z]' outside memory: 0
```

`gov:` markers in product code: `gov:kit` 198, `gov:fixed-verifiers` 50, `gov:bounded-fanout` 42, `gov:sequential-agents` 35, and others. Every one is read by its own gate:

| Marker | Read by |
|---|---|
| `gov:fixed-verifiers`, `gov:bounded-fanout`, `gov:sequential-agents` | `agent-cap.js` |
| `gov:handoff` | `tools/roles/roles_lib.py` |
| `gov:argv`, `gov:conf-allow` | `check-unattended.sh` |
| `gov:kit` | `check-kit-placeholders.py` |

None of them marks a feature.

**P3. Decision rows:**

```
rows: 200 · bold-id rows: 59 · owner-tagged "(owner": 20 · rows with "reuse": 0
rows added 60d: 160 · Decided: trailers 60d: 1829 (in 837 commits)
commits touching DECISIONS.md 60d: 142 — merge 35, unit-id 27, records 26, fix 10, feat 8, decide 2
```

My awk counts 87 rows at ≥280. It counts bytes, while your handed figure of 79 within 20 of the cap counts characters, so the two are not in conflict. No file defines "major": a search for `major` across BUILD-METHOD, AGENTS and TEMPLATE-SPEC returns nothing.

**P4. Research records.** `gen_build_index.py --print-bindings` (read-only; it always exits 0) found 265 `research` bindings, of which 63 are prompts and 202 are records, across 41 builds.

```
records 202 builds 41 · cited from ANOTHER build folder 22 · named in a commit message 8
non-dClosedLoop 132, cited cross-build 24 (incl. gotchas/tools citers)
research-named files not bound research: 3 of 61
```

Recall does index them: every tracked `.md` under the memory root enters the chunks set (`extract.py:302-320`), and only `.memory-tree.conf:680`'s archive pattern is excluded.

**P5. Dossiers against a reuse entry:**

| Reuse entry must hold | Dossier holds | Measured |
|---|---|---|
| Feature tag | `feature =` key | 31/31 |
| Directive "MUST reuse X wherever Y" | `seam: X — reuse for Y; extend via Z` | 76 seam entries; 51 with "reuse for"; 37 with "extend via"; 0 with MUST |
| Code anchor `gov:feature <tag>` | `[paths] globs` (file level) | 28/31 stale by ancestry (handed). 51/65 seam tokens literal-grep in code, and about 57 once dotted names are split |
| Proposer and build | `decisions = […]` | 17/31 non-empty |
| Owner disposition | `status` building/shipped | 0/31 |

Bytes per section across the 31 dossiers:

| Section | Bytes |
|---|---|
| Constraints & why | 144,820 |
| Gaps | 59,081 |
| Shared seams | 53,981 |
| Other | 33,510 |
| Reuse affordance | 22,309 |

The reuse-shaped part (Reuse affordance) is 7.1% of dossier text.

**P6. Cost of a one-marker scan:** `git grep 'gov:feature'` took 0.048 s, and a scan for every unit id across `tools` and `skills` (7,633 hits) took 0.056 s.

## Gaps

1. 724 confirmed findings have no class and no disposition field. Left-shift exists only as prose (`BUILD-METHOD.md:275-276`).
2. 13 of 124 records cite their review or finding, so a class cannot be traced back to its finding.
3. No reuse entry exists, nothing proposes one, and no code carries a feature anchor. The card's `**Reuse:**` is untracked and filled in 4 of 20 cards.
4. Nothing decides that a decision is major. 59 bold rows and 20 owner-tagged rows do not line up with the 12 major decisions.
5. Research is found across builds only through recall or by name: 22 of 202 records are cited from another build.
6. Two records disagree with the code:
   - `ANNOTATION-STYLE.template.md:6-9` says no gate reads comment citations. drift-audit's `source_cited_ids_resolving_to_no_record` does read them, though it is report-only and pinned at 2 (`drift_signals.py:308`).
   - `HYGIENE.md:692` lists a `note` kind, and the catalogue holds none.

## Candidates

| # | Candidate (mechanism) | Losing test | Result |
|---|---|---|---|
| **P1-A** | Extend the appendix `classes` column into a per-confirmed-finding **left-shift disposition**: `class:<slug>` · `gate:<leg>` · `none — <why>`. The fold fills it, and a check reads the fold's round. | Loses if appendix class cells cannot be joined to records. | 50/60 names resolve; the 10 misses are the `C<n>` fallback, which the build must refuse. **Survives.** |
| P1-B | A provenance key `from: <review path>#<id>` on new classes, graded by `gotchas.py --check`. | Loses if it cannot see a finding that has no class. | It cannot: it grades only records that exist. **Rejected as the sole mechanism**, kept as P1-A's back-link (13/124 cite today). |
| P1-C | A backlog "left-shift owed" ask per unclassed finding. | Loses if the asks pile up deferred. | 2 of 4 such asks are DEFERRED, and 0 rows use the kind label. **Rejected.** |
| **P2-A** | Proposal at unit close, triggered by §10 "no seam fits": the unit built a new seam, so its close carries `reuse: proposed <tag>` or `reuse: none — <why>`. | Loses if the volume swamps the owner. | 256 specs over 67 of 163 builds, about 1.6 per build that builds a new seam. **Survives.** |
| P2-B | Proposal from a dossier `seam:` added in the diff. | Loses if core would depend on the map. | It would: dossiers are read only under `MAP_SUB`. **Rejected.** |
| P2-C | Proposal from every new code file. | Loses on precision. | 87 new non-test files in 60 days, against 55 seams. It over-selects helpers. **Rejected.** |
| **P3-A** | Keep the hand-written row, plus an added-row grammar: a `major` token, and a `MUST reuse` directive where one applies. Graded on added rows by row_grammar, the same identity-at-merge-base seam check 27 uses. | Loses if an existing token already marks major. | Bold 59 and owner 20, against 12 major: no existing token fits, so a new one is needed. **Survives.** |
| P3-B | Derive the log from `Decided:` trailers and §8 marks. | Loses on volume. | 1,829 trailers in 60 days, against 160 rows added. **Rejected.** |
| **P4-A** | A derived research catalogue: `--print-bindings` filtered to `research`, outside `prompts/`, with path and term filters. Check 21 is already the witness of binding. | Loses if research records go unbound. | 3 of 61 research-named files are unbound. **Survives.** |
| P4-B | An authored research index of rows. | Loses on `[memory]`, because the catalogue is derivable. | P4-A's test passed, so P4-B is derivable. **Rejected.** |
| P4-C | Recall only. | Loses on "core never depends on optional components". | Recall is optional (handed). **Rejected for core**; it stays the optional slot. |
| **P5-A** | Dossiers stay with the map. Reuse entries are core. When the map is installed, a dossier `seam:` may seed a proposal and cite the entry's tag. | Loses if a reuse entry needs dossier content. | It needs 7.1% of it: about 4 of 5 fields are missing or partial, disposition 0/31. **Survives.** |
| P5-B | Merge dossiers into reuse entries. | Loses if most dossier content has no entry field. | 92.9% has none. **Rejected.** |
| **P6-A** | The annotation index stays a map and drift concern. Core checks `gov:feature` with a one-marker grep, the way each existing marker gate does. | Loses if a core check needs a persisted index. | 0 persisted indexes and 0 core readers; a grep costs 0.048 s. **Survives.** |
| P6-B | Make the annotation index core. | Same test as P6-A. | No core reader exists. **Rejected.** |

## Pick

| Path | Step and item | Actor | Witness a check can read |
|---|---|---|---|
| Finding → class | Review · `review.left-shift` | The fold (main loop); the owner rules on any `none` | Every confirmed row of the fold's latest appendix carries a disposition. `class:` resolves to `memory/gotchas/<slug>.md`, and `gate:` resolves to a leg in `tools/gate-legs.json`. A new class carries `from:`, which must resolve to that review. Bare `C<n>` is refused. |
| Feature → reuse | Build · unit close (`build.reuse-propose`) | The builder proposes; the owner disposes through the instruction command | A unit whose §10 says "no seam fits" has a `reuse:` line, either `proposed <tag>` or `none — <why>`. An accepted entry has at least one `gov:feature <tag>` in code, and a `removal-pending` entry has none left. |
| Decision → row | Plan / Design · `*.decide` | The owner's ruling; the author writes the row | Each added row (absent at the merge-base) carries the `major` token, plus a `MUST reuse` directive where one applies. Checks 7, 27 and 28 as today. |
| Research → library | Plan / Design · `*.research` | Researcher | Check 21's `research` binding. The planner's recall slot is optional, and the core fallback is the derived `--print-bindings` research view. |

- **Dossiers:** keep them in the map, as an optional component.
- **Annotation index:** keep it in the map and drift kit. The one core need, `gov:feature` anchors, is met by a one-marker scan.

Files referenced:
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/memory-tree/gotchas.py`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/workflows/tier2-review.js`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/guides/BUILD-METHOD.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/HYGIENE.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/memory-recall/extract.py`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/drift-audit/drift_report.py`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/map/features/`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/skills/session-kickoff/manifest-check.sh`
