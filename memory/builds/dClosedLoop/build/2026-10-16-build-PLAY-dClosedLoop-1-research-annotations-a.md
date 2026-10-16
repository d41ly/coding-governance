# Research: code annotations and commentary, run A

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 75's return, verbatim, except that its three citations of dUnstalledConvoy's unit 21,
an id no record defines, carry the `missing:` form, so the build index joins it to no roster. Its question
is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-23-researcher.md`, which dispatch 76 runs
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`.

---

## 1. Verdict

Use the settled inline head line and pull it on demand. A `gov:note` head line sits at the top of a block, and a block is at most 8 lines: the head line plus 7 lines of reason. The reason says what would break without the code. History, narration and measurements move to the record that `refs=` names. An annotation is not an instruction unit. It is code-resident evidence at level 7, and it may hold only a definition, a pointer, or a constraint or fact that carries its A4 disposition. A directive can only point at the unit that holds it.

Delivery has two paths: the work order's optional `Annotations` slot, picked by the item's tags and capped at 2 KB, and a query by tag. A Read hook is not a delivery path, because the Read tool carries only 5.4% of the calls agents make to read code.

The core check is a one-marker scan that takes 0.05 s. The map adds the block budget and the index.

## 2. Today

| Part | What it does | Measured | file:line |
|---|---|---|---|
| ANNOTATION-STYLE guide | A writing convention. A1 refuses any grammar, marker or gate; A2 makes citing a record voluntary | 4,813 B, byte-identical to its template | `memory/guides/ANNOTATION-STYLE.md:7-8,17-26`; `tools/memory-tree/ANNOTATION-STYLE.template.md` |
| `gov:` waiver markers | Inline markers that gates read. Some already use the shape `gov:<m> — <reason>` | 22 of the code markers carry ` — reason`, e.g. 17 `gov:literal-python —` | `tools/check-wiring.sh:594`, `tools/hooks/agent-cap.js:461,482`, `.githooks/pre-commit:103`, `tools/unattended/check-unattended.sh:155,169` |
| `gov:note` / `gov:feature` | — | **0 files each**, so the population is empty | `git grep -c` |
| drift-audit's cited-id signal | Ids in tracked non-memory text that no record anchors. Report-only (`gateable: False`), pin 2, with a RATCHETS row | value **2**, of 1,250 cited ids (`missing:TOOL-dUnstalledConvoy-21`, `-22`) | `tools/drift-audit/drift_report.py:2201-2264`; `drift_signals.py:308,455` |
| check-dead-paths | Refuses basenames of files git deleted or renamed. A path that was never tracked is invisible to it | misses `memory/gotchas/msys-mangles-rev-colon-dotpath`, which never existed (`git log --all` is empty) | `tools/check-dead-paths.sh:122,131`; `tools/unattended/check-brief-recorded.sh:526` |
| map comment lexer | `_LEX_PROFILES` table. It **strips** comments, and an extensionless file gets no profile, so nothing is stripped there either | strips at :698; `None` profile at :714-716; the hooks under `.githooks/` are extensionless | `tools/codebase-map/map_lib.py:663-670,698-716` |
| Read hook | PostToolUse `Read` → `recall-opened.js`. It observes and injects nothing | — | `.claude/settings.json:65-71`; `tools/memory-recall/recall-opened.js:15-19` |
| Path rule | Harness-native: `paths:` front matter, loaded when a matching file is opened | 1 rule | `.claude/rules/product.md:1-4` |
| Work-order fields | `TASK_FIELDS` holds the render slots, including `reuse` | 8 fields | `tools/roles/handoff.py:97` |
| Design: grammar, anchor, index, gate | settled | — | layer-memory `[annotations]`; layer-library `[placements]`, `[consult]` |

**The comment census.** I ran `python -I annsys/census.py . cites.json` over 299 tracked code files: tokenize plus ast docstrings for Python, `//` and `/* */` for JS, `#` for the rest, and a shebang for extensionless files.

| Kit | Files | Comment / nonblank lines | Comment bytes | Lines in blocks of 8+ |
|---|---:|---:|---:|---:|
| unattended | 30 | 22,643 / 58,136 (38.9%) | 47.2% | 50.1% |
| memory-tree | 27 | 11,000 / 35,397 (31.1%) | 40.1% | 49.3% |
| govkit | 22 | 10,382 / 31,445 (33.0%) | 40.6% | 57.2% |
| run-gates | 28 | 7,713 / 23,435 (32.9%) | 42.7% | 48.9% |
| lexicon | 10 | 4,430 / 11,535 (38.4%) | 48.8% | 58.6% |
| roles | 9 | 663 / 3,344 (19.8%) | 27.4% | 52.8% |
| branch-reconcile | 4 | 275 / 2,267 (12.1%) | 18.2% | 33.8% |
| **Total** | 299 | **87,349 / 269,674 (32.4%)** | **7.66 MB of 18.50 MB (41.4%)** | **51.6%** (2,765 blocks; median block 3 lines, p90 10) |

**Comment kinds, over all comment lines:**

| Kind | Lines | Share of lines | Share of blocks |
|---|---:|---:|---:|
| Build ids | 6,464 | 7.40% | 26.7% |
| Positional references (§ 313, AC<n> 2,633, id S<n> 1,929) | — | ~5.6% | — |
| History (dates, SHAs, "used to"…) | 2,440 | 2.79% | 10.0% |
| Measurements | 1,629 | 1.86% | 7.0% |
| Directives (MUST, NEVER) | 341 | 0.39% | — |
| `memory/` pointers | 262 | 0.30% | — |
| Charter tags | 1 | 0.00% | — |
| Namespaced tags | 0 | 0 | — |

The 2,765 essay blocks (8 lines or more) break down as follows: 44% carry history or a measurement, 55% a "because / otherwise", 58% an id, and 76% an all-caps headline phrase, which is a head line in all but name.

**What resolves nowhere** (`python -I annsys/dangle.py`):
```
ids distinct 1102 ... absent from memory/ 30 {'TOOL': 17, 'ARCH': 9, 'PKG': 4}; 19 only in test files
paths distinct 173 unresolved 75 (34 'other' — adopter-side/example literals)
memory/ pointers 130, gotcha pointers 42, unresolved 3 (2 line-wrapped, 1 real)
```
Real dangling citations: 2 ids, which drift-audit sees and which never block a merge, plus 1 gotcha path that no check sees.

**How agents read code.** I ran `annsys/tx.py` and `annsys/txbash.py` over the transcripts since 2026-09-16, reading the tool results themselves rather than HEAD:
```
Read tool on code: 1,110 calls (1,064 sliced, 46 whole); 8.48M chars; comment share 29.5%; whole-read p50 17.4k chars
shell reads of code: sed 8,989 / grep 9,219 / cat 688 / other 450 = 19,346 calls; 63.6M chars; comment share 37.1%
code Reads whose region cites an id or memory/ path: 618; exact follow within 3 calls 47 (7.6%), within 10 calls 86 (13.9%)
Grep tool calls naming gov: or an id: 16 of 651
```
- Agents read comments at volume: about 26M chars in 30 days, about 6.5M tokens at 4 chars per token.
- They rarely follow a comment's pointer to its record, so the comment stands in for the record.
- 94.6% of code-read calls never pass through the Read tool.

**Where the records and the code disagree:**
- research-memory-annotations:69 says "No real dangling id was found", and layer-memory `[annotations]` (:674) lists 35 as fixtures or foreign. drift-audit finds 2 real ones, `missing:TOOL-dUnstalledConvoy-21` and `-22`. A gate leg built on that signal is **red at tolerance 0 on its first run**, not vacuously green.
- layer-memory `[map]` (:642) says 28 of 31 dossiers are stale. Today's signal is 25 of 31.
- layer-library `[consult]` (:307) files the read hook's absence under **Recall**. `[placements]` (:241) homes the annotation index with the **map**, which is what such a hook would serve.

## 3. Across the layers

| Layer | Needs from it | Gives it |
|---|---|---|
| instruction | the six statement types (R-D); the namespaced tag registry (R-B) as pointer targets; the rule that handed content is data | a code-side join: a `→ <tag>` that resolves to a unit, item or policy. A confirmed breach can name a code location (R-J) |
| flow | `item.*` and `step.*` tags as targets; the bar to host the leg | the `test.annotations` leg; the `gov:feature` anchor in `build.unit-pass`'s witness |
| roles | the work-order render (`handoff.py:97` `TASK_FIELDS`) with one more optional slot | write-set orientation rows for builders and reviewers; a comment-drift line in the reviewer's checklist |
| memory | the memory contract declaring the generated `annotation-index` kind; the id parser moving into memory-tree; the map's lexer | anchors for reuse entries; `refs=` into the trail; a home for migrated history (the unit's records) |
| runtime | a command-adapter row for `map annotations`. No hook pack (see C) | nothing. Under the pick it registers no pack |
| observability | drift-audit's RATCHETS for an essay-lines row and for the resolve pin | the comment-load signal and the follow-through measure (`gap-mem-12`) to the Loop Review |
| integrations | none | none: remote CI runs the leg unchanged |
| distribution | govkit to ship the leg with memory-tree; guide and template parity (`kit-dogfood-parity`) | the adopter's annotation guide template |

| Other system | Needs from it | Gives it |
|---|---|---|
| tags | a registered `feature.` namespace, or reuse-entry tags; retired tags with forward pointers; the tag-shape check | a real usage population in code, so its "every tag used is registered" join has members outside the instruction text |
| instruction writing | the head-line template as one registered micro-format; R-D's checker reused on the head line | a second consumer of the statement grammar, outside loaded text |
| role workflow shapes | each role's work order declares whether it takes the `Annotations` slot (builder and reviewer: yes; driver: no) | slot rows sized ≤2 KB |
| memory structure | the record kind that receives migrated history and measurements; the generated-kind door for the index | evidence that comments, not records, are what agents read (7.6% follow-through), so the read path should be shaped at the code |

## 4. Candidates

| # | Mechanism | Efficiency (method) | Smallest losing test | Result |
|---|---|---|---|---|
| **A. Status quo** | Voluntary prose; ids caught by a report-only drift signal | 26M comment chars read per 30 days; 7.6% follow-through | "A dangling pointer in a comment reds some gate" | **Loses.** `drift_report.py --json` gives `"value": 2, "pin": 2, "gateable": false`, and the dangling gotcha path is caught by nothing |
| **B. Inline head line, pulled (pick)** | `gov:note` and `gov:feature` lines; core marker scan; map-built index queried by tag; work-order slot; block budget | Check: 0.053 s marker scan (`time git grep -n "gov:[a-z]"` gives 401 lines, real 0m0.053s); full lexer probe 4.56 s. Load: +2,765 head lines × ~110 B ≈ +0.30 MB; trimming essays to 8 lines removes ~23k lines ≈ 2.0 MB, a net −1.7 MB (−22% of comment bytes). Read path: about −22% of comment chars read, ≈ −5.7M chars (≈ 1.4M tokens) per 30 days, assuming reads hit lines uniformly | (1) The predicate must red each planted case, pass a clean block, and report "unarmed" on an empty population. (2) Owed: the 30-block mutation probe; follow-through after landing above 13.9% within 10 calls | **(1) Passes.** Real tree: `population gov:note=0 gov:feature=0 ... UNARMED`. Fixture: `findings 7`: refs-id-dangling, refs-path-dangling ×2 (one in an extensionless hook), feature-no-entry, head-shape, budget 9 > 8, history-in-note; `good.py` is clean. (2) Not run, because it needs the build |
| **C. Pushed at open** (a Read-hook pack, or rendered `.claude/rules` path rules) | Inject the rows anchored to a file when it is opened | 2.2 to 8.1 KB per file without dedupe (research); a per-file table of contents reaches 68 KB for `unattended.sh` (570 blocks of 4+ lines × 120 B) | "The opening event must see at least 50% of code-read calls" | **Loses.** It sees 1,110 of 20,456 calls (5.4%), and 8.5M of 72.1M chars (11.8%). The path-rule variant also loses on portability: Codex loads `AGENTS.md` alone (layer-instruction R-K) |
| **D. Out of band** | The code carries nothing; rationale lives in sidecar records anchored by path or symbol, like dossiers | Code bytes −41%, but every orientation costs one extra record lookup | "The sidecars stay as fresh as their code" | **Loses.** `dossiers_older_than_their_paths` is 25 of 31, and agents follow pointers 7.6% of the time |

I stopped at four. A per-file header block, or a per-kit table of contents, is a granularity of B. A Bash-aware PostToolUse hook is C with a parser bolted onto `sed` and `grep` output. That parser is fragile, and the 2.2–8.1 KB load makes it lose regardless.

## 5. The pick, specified

**Grammar.** It extends the existing `gov:<marker> — <reason>` waiver shape, so it is one micro-format in the instruction registry.
```
<comment> gov:note <tag>[,<tag>…] — <definition, ≤90 chars> → <pointer> [refs=<id|path>[,…]]
<comment> <≤7 lines: the counterfactual, constraints with an A4 disposition>
<comment> gov:feature <feature-tag>
```
- **Tags** are R-B namespaced: `kit.`, `layer.`, `step.`, `item.`, `policy.`, `practice.`, `kind.`, `feature.`.
- **The pointer** is a registered tag (a unit, item or policy), a command in backticks, or `path#[tag]`. It never names a section by number.
- **Statement types:**
  - the definition is the description;
  - the pointer is the `→`;
  - a constraint or fact needs FROZEN, GATED or POINTED (A4);
  - a directive appears only as `→ <unit tag>`, and the comment never originates one.
- **Level:** none of its own. Rendered into a work order, the rows are fenced data at level 7, and a pointed-to unit keeps its own level.

**What goes where:**

| Stays in the comment | Moves to the record `refs=` names |
|---|---|
| what the block implements; the counterfactual (A3); a constraint that carries its disposition | history ("rev-2 named…", "round 2 caught"), dates, SHAs; measurements that are not gated; narration of how a bug was found |

**Migration.**
- Bind the grammar at a cutoff: a new or touched block over 8 lines takes a head line and moves its history out.
- 76% of essays already carry an all-caps headline. A migration helper drafts the head line from it, and the author confirms.
- The essay-lines ratchet drains the legacy population.

**Ownership.**
- Layer: memory. The core part is the marker scan and the `gov:feature` anchors in memory-tree. The index and the budget are the map's.
- Chain build: dTotalRecall.
- The head-line micro-format registers with dOrderedCharter's registry.

**Records and kits.**
- The `annotation-index` kind: generated by `gen_map.py`'s comment lexer, with a shebang profile and docstrings added. Its home is under `memory/map/`, and it is queried as `map annotations --tag|--path`, never loaded whole.
- The ANNOTATION-STYLE guide and its template, amended together.
- A new drift-audit RATCHETS row: `comment_essay_lines`.

**Checks:**

| Check | Engine | Turns red on |
|---|---|---|
| head grammar | memory-tree marker scan (core) | `gov:note kit.k missing the arrow` |
| resolve | gate leg on `build_source_cited_ids_with_no_record`, extended to read `refs=` and `gov:feature` | `refs=TOOL-dXray-9`; `refs=memory/gone.md`; `gov:feature no-such-entry` |
| one anchor per tag | the same scan | a second `gov:feature` line for one tag |
| block budget | map lexer | a `gov:note` block of 9 lines or more |
| history in a note | map lexer | a body holding `rev-2`, `2026-10-01` or a SHA |
| essay ratchet | drift-audit RATCHETS | the tree-wide count of lines in 9+ line blocks rises (today 45,108) |

All six red cases above were seen red in the fixture probe, apart from the duplicate anchor, which I did not plant. The resolve leg arms only after `missing:TOOL-dUnstalledConvoy-21` and `-22` are fixed, or pinned at 2.

**Read-path cost.**
- Work-order slot: at most 2 KB, about 16 rows.
- A query: one call returning rows of `file:line tag — desc → ptr`.
- No per-open injection.
- Core check 0.05 s; lexer pass about 5 s.

## 6. Items and policies

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `test.annotations` (new) | command (the bar) | grammar, resolve, anchor and budget over the tree and the diff | the leg's verdict in the bar's log; "unarmed" while the population is empty | red goes to the unit's builder; unarmed is reported, never green |
| `build.unit-pass` (filled) | role (builder) | adds or updates `gov:note` on touched blocks; `gov:feature` on an accepted entry | `test.annotations` green at the unit's commit; the anchor resolves | red sends the unit back |
| `design.seams` (filled) | role (reuse scout) | queries the index by the build's tags | the seams record names the rows it used, or "searched, none" | map absent: "not installed", with the tree search named |
| work-order render (filled, dBoundRoles) | command | fills the `Annotations` slot from the item's tags and write set | the slot holds one of three states | over 2 KB: truncated to a query hint |
| `maintain.comment-load` (new, observability) | command | reads the essay ratchet and follow-through | drift-audit signal values | rising essays or flat follow-through go to the Loop Review |

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `annotations.grammar` (exists) | `voluntary`, `required` (fork: drop `pushed-at-read`) | `voluntary` | F4-2. C loses on reach |
| `annotations.delivery` | `work-order`, `on-demand`, `off` | `work-order` | the only surface every role reaches |
| `annotations.budget` | `ratchet`, `diff-refuse`, `off` | `ratchet` | 293 of 1,020 commits in 30 days (29%) added a block of 9 lines or more, so `diff-refuse` would red about 3 in 10 commits on day one |
| `annotations.history` | `refuse`, `warn` | `refuse` | it binds only `gov:note` blocks, a voluntary and empty population, so it costs nothing today |

## 7. Gaps

| Gap | Effect |
|---|---|
| `gap-mem-03` | Closed in part: the `gov:feature` anchor check, both ways |
| `gap-mem-12` | Feeds it: the baseline is 7.6% within 3 calls and 13.9% within 10, exact, 30 days. The record's 2.5% and 11.0% used a different window and HEAD content |
| `gap-mem-11` | Extended: three records contradict the code (§2) |
| `gap-found-09` | Closed in part: code joins to items and units through `→` |

New gaps, with the id left to the register owner:
- **(MED, dTotalRecall) The Read event reaches 5.4% of code reads,** so `pushed-at-read` cannot deliver. Evidence: `tx.py` and `txbash.py`, above.
- **(MED, dTotalRecall) Two real dangling ids pass every gate,** and one gotcha path resolves nowhere, with no check that can see it. Evidence: the drift report, `check-brief-recorded.sh:526`.
- **(MED, dTotalRecall) Comment load is unbudgeted:** 51.6% of comment lines sit in blocks of 8 or more, 44% of those carry history or measurements, and 29% of commits add one.

## 8. Forks

1. **`pushed-at-read`:**
   - (a) retire the value;
   - (b) keep it as a Bash-aware hook;
   - (c) keep it as is.

   I recommend (a). The hook reaches 5.4% of code reads.
2. **The block budget:**
   - (a) a ratchet only;
   - (b) refuse on the diff from the cutoff;
   - (c) refuse on the diff once the ratchet halves.

   I recommend (c).
3. **The legacy essays:**
   - (a) a per-kit drain unit in dTotalRecall;
   - (b) migrate only touched blocks.

   I recommend (b), plus the ratchet.
4. **The resolve leg's first run:**
   - (a) fix `dUnstalledConvoy-21` and `-22` first;
   - (b) pin it at 2.

   I recommend (a).
5. **An annotation as an instruction unit, at level 4, against code-resident evidence at level 7.** I recommend level 7. Making it a unit puts about 7,460 candidate blocks into the manifest, and none of them is a load point.

The scripts (census, dangle, tx, txbash, essays, perfile, noteprobe) and the planted fixture are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/annsys/`.
