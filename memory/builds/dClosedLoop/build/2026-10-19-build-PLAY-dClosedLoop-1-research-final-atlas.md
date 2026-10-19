# Research: The in-repo atlas: what it shows, where it derives from, and how it stays current

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 159's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-32-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md`.

---

**The in-repo atlas: research return (PLAY-dClosedLoop-1, question 5)**

**Recommendation:** commit the atlas as generated Markdown pages with Mermaid diagrams under `help/atlas/`, built from the as-built registries. It is kept current by the repository's existing `[[generated]]` and `regen.py` mechanism, and owned by dTotalRecall. Four other candidates were tested; each lost a named test, and the static HTML page survives only as an optional local render.

I wrote nothing in the repository. The scratch folder is deleted, and `git status` shows the same five untracked prompt files as at the start.

## 1. Today's atlas and map, measured

**The atlas page** (`2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`, `.html`)
- **Views:** 12 tabs (`…-atlas.html:428-439`): Layers, Today vs target, Flow, Lifecycle, Roles, Memory, Chain, Policies, Principles, Decisions, Progress, Records. The browser draws the diagrams as SVG when the page opens (`…-atlas.html:494`); the generator draws none.
- **What it reads:** design records only, never product code: v2, the gap register, flow-steps, the layer records, fates and memory-plan (`atlas.py:43-46`), plus every record whole (`atlas.py:238-275`).
- **`--check` today:** `atlas: derived — 223 records, 3694 sections, 210 decision sections, 16 comparison areas, 40 principles`, exit 0, in 0.5 s.
- **Plants:** I ran three of the seven, and each exited 1:
  - `kind-unplaced`
  - `view-unread`
  - `instruments-decision`
- **Size:** `--out` wrote 13,352 KB (13,672,603 B, 3,851,080 B gzipped).
  - The data blob is 13,520,345 B, and 12,662,778 B of it (94%) is the embedded record text.
  - The template is 152,260 B over 2,219 lines.
- **Determinism:** two renders are byte-identical.
- **Dependencies:**
  - Python standard library only.
  - The page loads Google Fonts (`…-atlas.html:6-8`) and marked 4.3.0 from cdnjs (`…-atlas.html:470`).
  - Offline, Markdown falls back to a `<pre>` block (`…-atlas.html:550`).
  - The browser pane refused a `file://` open of the 4 MB page (`atlas-instruments [procedure]`).
- **What it does not check:**
  - `--check` writes nothing and compares the derivation to no published page. Nothing witnesses whether the published artifact is stale (`gap-deploy-23`, owned by dShippedRelease, LOW).
  - The step list is typed by hand (`atlas.py:61`). That list silently dropped `[adopt]` until the map's parity caught it (`project-map [test-run-found]` item 1).

**The design map** (`2026-10-17-build-PLAY-dClosedLoop-1-map.py`)
- **`--check`:** `map: 2609 nodes in 30 namespaces; 32065 B of 32768 (degraded: purposes 40); folded 14; unarmed none`, plus `purposes declared 1799, derived 312, pending 498`, exit 0.
- **It imports `atlas.derive()`** (`map.py:56-58, 109`).
- **The parity arm is partly circular** (`map.py:686-695`). Layers, chain builds and gaps come from the atlas's own data (`map.py:117, 143, 368`), so for those three the check shares state with what it guards. That breaks the `[class]` rule. Steps and items are read independently (`map.py:149-163`).

**What the design already plans for an in-repo view**
- **One clause in the whole chain:** dLinkedLibrary u14, "the atlas re-rendered from the same node table" (v2 `[chain]`, line 1594).
- **The records disagree on its owner:** `project-map [owners]` gives that same item to dTotalRecall.
- **The map is a view, never committed,** cached beside the index (`project-map [placement]`).
- **No record plans** a committed atlas, a place for it in `help/`, a gate on it, a size budget for it, or a policy key for it.
- **`help/`** is rendered from `usage` fields only at dConvergedCharter u15, the chain's last build: it finishes at unit 263 of 263 on the critical path (`night-pass-instruments [final]`).
- **No leg in `tools/gate-legs.json`** (140 legs) names `help/`.

## 2. What the as-built atlas should show and read

- **It reads the one index's node table, the same table `gov map` reads**, never the design records. Each source and the build that lands it:

| Source | Lands with |
|---|---|
| Step and item tables | dDeclaredLoop u24 |
| Policy catalogue and presets | dGroundRules u1, dKeptSession u1 |
| Record-kind registry | dTotalRecall u1, u18 |
| Roles | dBoundRoles u1, u20 |
| Legs (`tools/gate-legs.json`, 140 legs today) | already exists |
| Hooks and extension points | dWellOiledMachine |
| Kits (`kit.toml`, 17 today; govkit and lib have none) | dShippedRelease |
| Principle registry | dOrderedCharter u7 |
| The `code` record | dTotalRecall u8 |

- **The `code` record is shown as one counted line per kit, never drawn.** There are 395 tracked files under `tools`, `skills` and `.githooks`, 236 of them code.
- **Design against built:** each planned unit (484, from v2 `[chain]`) is joined to its landed status, derived from history, and to its deviation records. The atlas renders those joins and owns none of them. The plan ledger is question 2's; the deviation log is question 3's.
- **Links with `help/`:** each atlas node links to its unit's `help/` page, through the `usage` field from dConvergedCharter u15, and each page links back to its atlas anchor. A resolves check is red on a dead link either way.

## 3. Candidates

| Candidate | Mechanism | Test it could lose | Result |
|---|---|---|---|
| **A. Static HTML, script and data inlined, committed** | Today's generator pointed at the registries | Does a reader browsing the repository on GitHub see it rendered? | **Loses.** GitHub serves a raw `.html` file as text/plain ([GitHub blog, nosniff](https://github.blog/2013-04-24-heads-up-nosniff-header-support-coming-to-chrome-and-firefox/); [discussion #144037](https://github.com/orgs/community/discussions/144037), both read 2026-10-19). Diffs: with the compact one-line JSON blob, a planted one-key change rewrites 334,989 B; with one node per line it is 451 B. The template's 152 KB of script is hand-written and not derived. Kept only as an optional local render. |
| **B. Generated Markdown + Mermaid, committed** | One page per namespace; the renderer emits Mermaid fences and tables | Does any fence pass Mermaid's defaults (`maxTextSize` 50,000, `maxEdges` 500, [Mermaid config](https://mermaid.js.org/config/schema-docs/config.html), read 2026-10-19)? Is a one-key diff local? | **Survives.** A 16-page scratch render is 275,094 B. Its largest fence is 1,876 characters with 53 edges; the whole item graph would be 13,423 characters and 195 edges. A one-key change is 2 lines, 137 B. **Limits:** a chain-with-units diagram would need 537 edges, which exceeds 500, so units must be tables, not diagrams. GitHub documents no Mermaid version or limit ([GitHub diagrams doc](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams), read 2026-10-19), so the build must push a fixture holding the largest fence and view it. Offline, a clone without a Mermaid viewer shows the diagrams as source; the tables stay readable. |
| **C. Generated SVG committed** | Layout computed when generating; Markdown embeds the image | Is a one-node change local? | **Loses.** A python-only layered layout of the chain DAG moved 24 lines, 11 of them existing, for one planted build; Mermaid source changed 1 line. No layout engine is installed on this node (dot, d2, mmdc, Java all absent). |
| **D. C4 diagrams as code (Structurizr DSL, D2)** | A model file rendered by an outside tool | Does it derive from the registries, render on GitHub, and run on bash + python3? | **Loses.** A hand-written model is a second statement of the registries (`[derive]`, `[one-fact]`). A generated one reduces to C. GitHub's diagrams doc lists Mermaid, GeoJSON, TopoJSON and STL only. D2 is a Go tool under MPL-2.0 ([github.com/terrastruct/d2](https://github.com/terrastruct/d2)). Structurizr's DSL docs list its CLI and Lite under "End of life" ([docs.structurizr.com/dsl](https://docs.structurizr.com/dsl)). C4 itself is tooling-independent ([c4model.com](https://c4model.com/)). All read 2026-10-19. |
| **E. Render on demand, nothing committed** | The map's own placement: a cached view | Does a fresh clone or a GitHub reader see the atlas without running a command? | **Loses** the owner's "in the repo" requirement, and `gap-deploy-23` stays open. Kept as a policy value. |

## 4. Recommendation

- **Format: B.** Generated Markdown with Mermaid fences under `help/atlas/`, one page per namespace and the plan split per build. Units and code are tables or counted lines, never diagrams.
  - Each page opens with a "generated by … do not hand-edit" header, as `memory/LIVE.md` does.
  - A's interactive page stays available as `gov atlas --page --out <file>`, never committed.

- **Regeneration and its gate:** reuse the existing seam.
  - A `[[generated]]` row in memory-tree's `kit.toml`, with `write`, `check` and `stage = 3`. Stage 3 is the slot after the indexes over records, as `tools/run-gates/regen.py:15-21` defines it. `run-gates.sh:1440-1450` already refuses a stale output before the first leg.
  - `--check` byte-compares a fresh render with the committed pages.
  - **Planted reds:**
    - a catalogue default changed without regenerating. Measured on a scratch copy: flipping `memory.map-overflow` made the byte-compare exit 1.
    - a hand edit to one cell of a committed page.
    - a namespace registered but not rendered, which reads unarmed and never green (the map's populated arm).
    - a newly registered step that appears with no renderer change: no hand-typed lists.
  - The parity arm parses the committed pages back and compares them with index rows read on their own, never with the renderer's own data. That closes today's circular check.

- **Size budget:** 275 KB measured in total. Each page is capped; over the cap a page splits by segment and no node is ever dropped, following the map's `[fit]` order. Whether to refuse or warn is read from `budgets.enforce` (dGroundRules u9).
  - The 13.4 MB today is 94% embedded records, which the as-built atlas links to rather than carries.
  - For scale: an unpacked repository grows 4.49 MiB per regeneration of today's page; packed, two versions take 3.69 MiB. GitHub warns at 50 MiB per file ([GitHub large-files doc](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), read 2026-10-19).

- **Policy keys:**

| Key | Values | Default |
|---|---|---|
| `docs.atlas` | committed, on-demand, off | committed |
| `docs.atlas-page-budget` | 32k, 64k, 128k | 64k |
| `docs.atlas-diagrams` | mermaid, none | mermaid |

  - `docs.atlas-diagrams` exists for adopter hosts with lower Mermaid caps; GitLab once capped at 2,000 characters ([GitLab MR 60490](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/60490), read 2026-10-19).
  - The page format and the node-table source are structural choices, so they carry no key.

- **Owning build and unit: dTotalRecall**, as a unit beside u14's map renderer: same node table, same kit, finishing at unit 147.
  - The design-against-built page is a second unit that reads question 2's ledger and question 3's log.
  - dConvergedCharter u15 owns the two-way `help/` links and their resolves check.
  - dLinkedLibrary u14 moves to dTotalRecall, which also resolves the two records' disagreement.

- **Landing early:** nothing lands before dTotalRecall. The node table does not exist earlier, and a stopgap reader of the registries would be built and then replaced.
  - dTotalRecall's unit backfills the namespaces of the eight builds that land before it (dGroundRules through dKeptSession).
  - From then on, the unarmed-namespace check makes each build that registers a namespace keep its pages current.
  - The losing test for this choice: if dTotalRecall's unit needs per-namespace code beyond the extractors those builds registered, move the renderer to dOrderedCharter, where the index is born (u19).

- **Adopters:** the generator ships in memory-tree, a kept kit, and each adopter renders its own composition (gov's packs plus its overlay) under `docs.atlas`. `regen.py`'s path tokens (`tools/run-gates/regen.py:48`: kit, prefix, memory_root, map_root) have no help-root token. A token is needed, owned by dWitnessedBar.

## 5. What must exist before speccing starts

1. The owner's rulings on the three keys, entered in v2 `[policies]` with their owners.
2. A v2 revision giving the atlas one owner, dTotalRecall, and removing dLinkedLibrary u14.
3. dTotalRecall's units cell gains the atlas clause: the committed path, the `[[generated]]` row, the byte-compare check, the four planted reds, the budget, and the design-against-built sources.
4. dConvergedCharter u15 gains the two-way links and their resolves check.
5. A help-root token clause in dWitnessedBar.
6. A new gap, "no in-repo atlas: the design's atlas is an online artifact derived from design records", owned by dTotalRecall.

**For other researchers, one line each:**
- v2 `[policies]` holds 256 rows, not 261; the 261 figure appears in no record I searched (whole-design audit).
- The latest atlas version the records name is 60 (`session-log:2764`), not 69 (whole-design audit).
- `memory.map-overflow` is a size-cap switch outside `budgets.enforce` (whole-design audit).

**Files:**
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.html
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/run-gates/regen.py
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/run-gates/run-gates.sh
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/memory-tree/kit.toml

**Sources, all read 2026-10-19:**
- [GitHub: creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)
- [Mermaid config schema](https://mermaid.js.org/config/schema-docs/config.html)
- [GitHub: about large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)
- [GitHub blog: nosniff](https://github.blog/2013-04-24-heads-up-nosniff-header-support-coming-to-chrome-and-firefox/)
- [GitHub community discussion #144037](https://github.com/orgs/community/discussions/144037)
- [GitHub community discussion #23920](https://github.com/orgs/community/discussions/23920), the informal README limit of about 500k characters, which is a community estimate, not documented
- [terrastruct/d2](https://github.com/terrastruct/d2)
- [D2 intro](https://d2lang.com/tour/intro)
- [Structurizr DSL](https://docs.structurizr.com/dsl)
- [C4 model](https://c4model.com/)
- [GitLab MR 60490](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/60490)
