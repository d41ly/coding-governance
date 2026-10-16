# Research: code annotations and commentary, run B

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 76's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-23-researcher.md`, which dispatch 75 runs
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`.

---

## 1. Verdict

Every annotated block gets one inline head line: `gov:note <tags> — <definition> → <pointer> refs=<id|path>`. It holds only a definition and pointers. Any directive stays in the instruction unit it points to, so the annotation has no level of its own. History, narration and measurements move to records, under a size budget that applies to blocks only when they are touched.

Agents get annotations in three ways: an on-demand marker query (git grep, 0.057 s), the plain grep they already run, and a write-set slice in the builder's work order. There is no read hook. Read calls are only 3.1% of the calls that read code.

The resolve gate should cover every reference a comment cites, not just `gov:note` lines. Covered that way, it has a real population today and one real red.

## 2. Today

| Part | What it does | Measured | file:line |
|---|---|---|---|
| Comments in tools/, skills/, .githooks/, .claude/, .github/ | carry the orientation | 299 files, 89,435 of 288,669 lines (31.0%); 7.64 MB of 18.50 MB (41.3%) | census below |
| Long blocks (10+ lines) | rationale essays | 1,971 of 18,542 blocks (10.6%) hold 40.9% of comment bytes | census |
| Long blocks that also carry history, measurements or dates | narration | 931 blocks, 1.75 MB (22.9% of comment bytes) | e.g. `tools/drift-audit/drift_report.py:2179-2198`, `tools/memory-recall/extract.py:132-155` |
| Blocks that cite an id | pointers | 4,944 blocks (26.7%); 1,110 distinct ids, 6,596 cites; 31 ids appear nowhere under memory/, all fixtures or foreign families | census |
| Paths cited in comments | pointers | 162 distinct, 460 cites; 37 unresolved. 1 is real: `tools/unattended/check-brief-recorded.sh:526` cites `memory/gotchas/msys-mangles-rev-colon-dotpath`, which never existed (`git log --all` is empty) | probe |
| `gov:note` and `gov:feature` lines | the settled grammar | 0 files each | `git grep -c` |
| ANNOTATION-STYLE.md | a writing convention. A1 refuses any grammar, marker or gate; A2 keeps citing voluntary | 4,813 B, the same size as its template | `memory/guides/ANNOTATION-STYLE.md:5-10,17-29` |
| `gov:` markers read by gates | they work as markers | e.g. agent-cap reads `gov:bounded-fanout` | `tools/hooks/agent-cap.js:461,482` |
| The map's comment lexer | blanks comments to collect identifiers. No extensionless profile, and docstrings are treated as strings | `.githooks` has 11 files, 2,285 comment lines, none of them lexed | `tools/codebase-map/map_lib.py:659-670,697-716` |
| drift-audit's cited-id signal | scans all tracked non-memory text for ids only, never paths. Hard-coded `gateable: False`; pin 2 | — | `tools/drift-audit/drift_report.py:2201-2279`, `drift_signals.py:308` |
| check-dead-paths | flags only names this repo deleted, so it cannot see a path that never existed | — | `tools/check-dead-paths.sh:22-27` |
| The read hook | observes Read calls and injects nothing | matcher `Read` only | `.claude/settings.json:65-72`, `tools/memory-recall/recall-opened.js:3,24` |
| The work-order field seam | `TASK_FIELDS` already carries `reuse` | — | `tools/roles/handoff.py:97,354` |

**How agents read code** (1,626 transcripts since 2026-09-16):

| Channel | Calls | Characters returned |
|---|---:|---:|
| Read on code | 1,283 (91.8% of them sliced; median slice 4,323 chars, median whole file 14,837) | 9.76 M |
| Bash `sed -n` | 15,552 | 61.9 M |
| Bash grep or rg | 18,388 | 22.5 M |
| Bash cat, head or tail | 6,674 | 9.8 M |

- Comments are 30.7% of the characters Read returns from code.
- 60.8% of code Reads return a region that cites an id or a `memory/` path.
- Only 5.0% of those regions are followed within 5 reads by a read of that exact reference. The control, references from an unrelated region, is 0.2%.
- So for about 95% of cited regions, the agent takes the comment in place of the record, or ignores the pointer.

**Where the records and the code disagree:**
- layer-memory `[annotations]` (lines 670-673) says the resolve check's first green proves nothing because the population is empty. That holds only for `gov:note` lines. The class of references comments cite is non-empty and holds one real dangling path.
- research-memory-annotations line 30 counts 2,866 code Reads and leaves out the Bash channel, which returns about 94% of the code characters agents read.
- The handed facts say Runtime declares nine extension points; `layer-runtime:759` lists ten, with cadence items.
- The record counts 35 ids that resolve nowhere (`layer-memory:674`); I count 31. Both scopes are unpinned, and drift-audit's slug filter reports 2.

Commands and outputs:
```
python -I annb/census.py <worktree> annb/census.json
TOTAL 299 288669 89435 31.0% … essays 1971 essL% 42.8 ; bytes 18500588 comment 7637182 41.3%
python -I annb/union.py → ne_b 931 ne_by 1749908 ; ess_by 3125387 (40.9%)
python -I annb/reads3.py → code_reads 1283 sliced 91.8% ; comment chars 30.7% ;
  regions citing 780 (60.8%) ; followed 39 (5.0%) ; control 1/452 (0.2%)
python -I annb/bash.py → bash_grep 18388 / bash_sed 15552 / cat 6674 / Grep 369 ; chars sed 61.9M grep 22.5M
```

## 3. Across the layers

| Layer | Needs from it | Gives it |
|---|---|---|
| instruction | unit tags as pointer targets; R-D's statement types; R-I's reference check, which re-points or refuses a rename that strands a code pointer | for each unit, the code that enforces it: evidence for R-J's prune of "units no check enforces" |
| flow | `item.<step>.<name>` tags; the bar to host the leg | the `annotations` leg at Test; a fill of the `build.unit-pass` witness; where each item's command lives in code |
| roles | dBoundRoles' work-order render (`TASK_FIELDS`) | a `**Code notes:**` slot by write set for builder and reviewer |
| memory | homes for the migrated narration (the unit's spec, decision rows, bug classes); the id parser | `gov:feature` anchors (LR-6); path anchors for bug classes; owns the grammar, the resolve and budget checks, and the query |
| runtime | the command-adapter registration for the query, as a reading | head lines on hook-pack code that name their pack |
| observability | drift-audit's signal frame | a report-only drift signal: a head line older than its block's body |
| integrations | nothing | head lines on adapter code naming the adapter's registered name |
| distribution | ships the check and the guide template (they are paired by `kit-dogfood-parity.test.sh`) and the overlay's exemption classes | nothing new |

| Other system | Needs from it | Gives it |
|---|---|---|
| Tags | the registry and its namespaces (R-B), and a resolver call | the first population of tags in code; `gov:feature` tags |
| Instruction writing | the six statement types; unit tags | the rule that code never restates a directive and points instead; narration leaves code for records or `help/` |
| Role workflow shapes | each role's write set | the `**Code notes:**` slot; a reviewer item for comment drift |
| Memory structure | where narration lands, and record ids that resolve | about 0.7 MB less comment narration on the read path |

## 4. Candidates

**C1: an inline head line, an on-demand marker query, resolve over the whole class, and a budget.**
- Mechanism: one head line per annotated block. `git grep 'gov:note.*<tag>'` answers a tag query in one call. The resolve check covers every comment-cited id and `memory/` path.
- Efficiency:
  - Migration saves about 0.71 MB: 931 narrating blocks at 1.75 MB fall to about 1.04 MB once each is cut to a head line plus 12 lines.
  - Head lines add at most 0.54 MB, which is 4,944 id blocks at about 110 B each. Annotation is voluntary, so the real figure is lower.
  - The net change runs from −0.17 to −0.71 MB, 1 to 4% of code bytes. That is about 40 to 170 chars off each median slice.
  - Looking up "where is item X implemented" takes one query. Today no query can answer it, because no tag lines exist.
- Losing tests and results:

| Losing test | Result |
|---|---|
| (a) The gate's class population is empty, or has no real red, so the gate is vacuous | 1,110 ids, 162 paths, 1 real red: **passes** |
| (b) Agents follow code pointers no better than the control | 5.0% against 0.2%: **passes**, though weak in absolute terms |
| (c) The query costs more than 1 s | 0.057 s (`time git grep -nhoE "memory/…" -- tools skills .githooks .claude .github`): **passes** |

**C2: pushed at read.** A hook pack injects the records anchored to a file when it is opened (the `pushed-at-read` value).
- Mechanism: PostToolUse on Read, with per-session dedupe.
- Efficiency: 2.2 to 8.1 KB per distinct file, from the record.
- Losing test: the hook must see at least half the calls that read code.
- Result: Read is 1,283 of 41,857 such calls (3.1%) and 9.8 M of 104 M chars (9.4%). **LOSES.**
- Path rules (`.claude/rules/`) are triggered by Read too, so they share this result.

**C3: a sidecar manifest keyed by path and symbol.** Comments carry nothing, and the manifest is rendered into work orders.
- Mechanism: instruction-unit rows anchored to `path::symbol`.
- Losing test: anchors must survive at least 99% per month, and the text must appear where agents read.
- Result: 49 of 1,377 Python `path::symbol` anchors were lost in 30 days (3.6%). `python -I annb/churn.py <wt> e66125799` printed `defs then 1377 now 3190 … lost 49 3.6% … moved 16`. None of the 41.9k code-reading calls would show a sidecar. **LOSES.**

I stopped at three. A per-file header block is a granularity variant of C1. Rendering comments from a manifest into code inherits C3's anchor result and adds regeneration churn.

## 5. The pick, specified

**Grammar**, a superset of the settled line:
```
<comment> gov:note <ns.name>[,<ns.name>…] — <definition, ≤80 chars> → <unit.<tag>|path|`command`> [refs=<id|path>[,…]]
<comment> gov:feature <tag>
```
- Tags use R-B's namespaces. The head line holds a definition and pointers only.
- A body line holding MUST or NEVER needs `refs=` to the unit or record that states it.
- The annotation is no instruction unit. It loads at no load point and has no level. Its pointer resolves to a unit, which keeps its own level. In a work order it renders as a pointer list inside the level-6 task.

**What stays in a comment:** what the block implements, the counterfactual (A3), and a pointer.
**What goes to a record:** dates, "measured" numbers (A4's FROZEN numbers among them), and what a block used to do. For example, `drift_signals.py:151` cites `memory/project/in-flight/`, which "no longer exists".

| Owner | Part |
|---|---|
| dTotalRecall | grammar, resolve and budget checks; the query verb in memory-tree; the ANNOTATION-STYLE amendment and its template |
| dOrderedCharter | the tag registry the checks resolve against |
| dBoundRoles | the `**Code notes:**` field |
| dMindYourWords | nothing |

**The checks**, one `annotations` leg (git grep, then resolution):

| Check | Turns red when |
|---|---|
| Grammar | a head line lacks `—` or `→`; a namespace is unregistered; a description runs over 80 chars; MUST or NEVER appears without `refs=`; the marker sits in a string (map lexer, where installed) |
| Resolve | a dangling `refs=` id; a dangling `refs=` path; a `gov:feature` tag with no entry; a second anchor for one tag. On day one, `check-brief-recorded.sh:526`, unless the arming unit fixes it. The classes exempted by row: fixture slugs, foreign families (PKG, ARCH), adopter install paths (`.claude/hooks`), glob families (`BACKLOG.*`) |
| Budget | a touched block over 12 lines (1,235 legacy blocks exceed that); a head line over 160 B; a file's comment-byte share above its high-water mark (median 0.43, p90 0.67), shrink-only |
| Drift (report-only, Maintain) | a block body changes in a commit that leaves its head line untouched |

**Read-path cost:** the work-order slot stays at or under 2 KB. Running the query costs 0.057 s.

## 6. Items and policies

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `build.unit-pass` (fill) | builder | writes head lines for blocks implementing its items, and moves narration it touches into the unit's record | the `annotations` leg over the write set, at the unit's commit | red: the builder fixes it |
| `test.bar` leg (fill) | command | grammar, resolve and budget over the tree | the leg's verdict in the bar record | red: no landing |
| work-order render (fill) | command (`handoff render`) | runs the query over the write set into `**Code notes:**` | the slot's three states, byte-compared | none found: "searched, none" |
| `design.seams` (fill) | reuse scout | queries `gov:feature` and `gov:note` tags in scope | the seams record cites path:line | none: tree search |
| `review.report` (fill) | synthesizer | marks comment-drift findings `gate:annotations` or `class:<slug>` | the left-shift join | — |
| `maintain.annotation-drift` (new, observability) | command (drift-audit) | counts head lines older than their bodies | the drift report | count rises: an owner item at the Loop Review |

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `annotations.grammar` | voluntary, required, pushed-at-read | voluntary | settled by F4-2; see fork F3 |
| `annotations.budget` | refuse, warn, record | refuse (recommended) | mirrors `instructions.checks`; binds touched blocks only |
| `annotations.resolve-scope` | notes, every-comment-ref | every-comment-ref (recommended) | gate the class; not vacuous on day one |
| `annotations.work-order` | rendered, on-demand | rendered (recommended) | mirrors `reuse.delivery` |

## 7. Gaps

| Gap | Status | Evidence |
|---|---|---|
| `gap-mem-08` | closes: grammar, tags, query | 0 `gov:note` lines |
| `gap-mem-03`, partly | closes: `gov:feature` checked both ways | 0 lines |
| `gap-mem-12` | narrows: the C2 fallback is weak | Read is 3.1% of the calls that read code |
| New: comment pointers to records that never existed go unchecked | new, dTotalRecall | `check-brief-recorded.sh:526`; `check-dead-paths.sh:22-27` sees deleted names only; `drift_report.py:2246` reads ids only |
| New: the `pushed-at-read` value and its hook are blind to Bash reads | new, dTotalRecall | 40,574 Bash and Grep calls against 1,283 Reads |
| New: no budget on comment size; 41.3% of code bytes are comments, 22.9% of them narrating long blocks | new, dTotalRecall | census |

## 8. Forks

| Fork | Options | Recommendation |
|---|---|---|
| F1: resolve scope | `gov:note` refs only, as settled; or every comment-cited id and `memory/` path | every comment-cited reference: a real population and one real red today |
| F2: the index | a generated index kept with the map (LB-4's placement); or an on-demand marker query in core memory-tree | the query: 0.057 s, nothing to keep fresh, and the same one-marker scan the core already runs for `gov:feature`; the map's lexer only adds string exclusion |
| F3: `pushed-at-read` | keep; retire; or redefine it to also fire on PostToolUse Bash for `sed`, `cat` and grep paths | retire it, or redefine it and re-measure; as specified it reaches 3.1% |
| F4: migrating the narration | on touch, under the budget; or one sweep unit over the 931 narrating blocks | on touch, plus an optional sweep of the top three kits by comment bytes (unattended, memory-tree, govkit: 3.77 MB) |
| F5: the annotation's place in the ladder | levelless pointers (data); or level-4 path-rule units | levelless: comments are read incidentally, and a unit would put a second spelling of the rule in code |

The census.py run wrote its output, `census.json`, into the worktree root. I moved it to the scratchpad straight away, and `git status` matches the snapshot. I wrote and ran no other file in the repository.

The scripts and the census output are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/annb/`.
