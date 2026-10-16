# Research: the instruction writing system, run B

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 78's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-24-researcher.md`, which dispatch 77 runs
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`.

---

1. **Verdict**

The instruction writing system should treat the **unit** as the source and every instruction document as a **render**. Each statement is one row in a per-kit TOML manifest, carrying its tag, statement type, level, selectors, text or derivation source, budget and required-by. One renderer fills one template per document kind (charter, role static block, work order, protocol slice, Skill entry, path rule, hook message, harness prompt, spec instruction fields). A single `instructions check` leg refuses any file at an instruction path that is not byte-equal to its render. Unmigrated documents sit on a shrink-only legacy list. Measured against today, the main saving comes from handing slices instead of whole guides. For a builder item, instruction bytes fall from 35.6 KB to about 8.4 KB (−76%).

---

2. **Today**

Byte counts are committed blob sizes (`git cat-file -s HEAD:<f>`).

| Part | What it does | Measured | file:line |
|---|---|---|---|
| Charter | Rendered from the template by `render_playbook.py`: placeholders, `kit:`/`when:` fences, one-line regions capped at 200 B, `PROBES` | 16,732 B; 46 tagged rules, all unique, longest 193 B | `AGENTS.md:1-177`; `tools/playbook/render_playbook.py:115-126,562` |
| Role agents | `render_agents.py` combines the body, the house overlay and `render_charter_blocks` | 9 files, 45,213 B. Sources are 19,586 B. Charter blocks are 2,487–4,220 B of each file | `tools/roles/render_agents.py:135`; `tools/roles/roles_lib.py:279-298` |
| Handoffs | `handoff.py render` writes a Role section and a Task section, then the charter blocks a second time | 60 role handoffs; task median 8,495 B, p90 16,453 B | `tools/roles/handoff.py:402-416` |
| Guides | Kit templates rendered by token substitution only (template ≈ render) | 308,445 B across 10 files; the unattended four are 216,448 B. MERGE-BAR and SESSION-KICKOFF have no template | `tools/memory-tree/BUILD-METHOD.template.md` (8 tokens); `tools/unattended/*.template.md` (0 tokens) |
| Skills | `SKILL.template.md` rendered by adopters, plus two hand-written Skills | 77,368 B across 9 files | `tools/*/SKILL.template.md` |
| Harness prompts | String literals inside the Workflow scripts | unattended-build.js: 312 lines, 29,517 B. tier2-review.js: 43 lines, 8,899 B. Line 880 says "Read BUILD-METHOD.md WHOLE" | `tools/workflows/unattended-build.js:880` |
| Directive handles | 17 handles mapped to M-sections | 17 handles over 10 sections; mean 2,633 B of section per handle | `tools/unattended/unattended.sh:1042` |
| Gates over instruction text | Size, micro-formats, line length, playbook parity (S4 refuses section numbers), placeholders, method carriers, restatement, protocol parity, kit/dogfood parity, render wirings, roles catalogue | 29 of the 140 legs | `tools/gate-legs.json`; `tools/check-playbook-parity.sh:11-14` |
| Budgets | `template-size-limits.txt` (6 rows), `BODY_CEILINGS` (1,536–4,096 B) | — | `tools/check-template-size.sh`; `tools/roles/check_roles.py:84-89` |

**Load per reader (instruction bytes, handed data excluded)**

| Reader | Default load | On demand |
|---|---|---|
| Main session | `CLAUDE.md` 11 + `AGENTS.md` 16,732 + auto-memory `MEMORY.md` 14,005 (record said 13,187, so it has grown) + `product.md` 3,011 when a product path is touched | Whole guides: 4,813–85,684 B each |
| Researcher spawn (this one) | Agent 4,731 + duplicated charter block 2,879 = 7.6 KB | `BUILD-METHOD` whole, 29,326 → 36.9 KB |
| Builder stage | Agent 6,310 + `BUILD-METHOD` whole (forced by line 880) 29,326 = 35.6 KB | — |

**Statement-type mix (P11)**

| Sample | Directive / constraint | Pointer | Definition | Fact | P11 would delete |
|---|---|---|---|---|---|
| `AGENTS.md`, all 16,733 B, classified line by line | 50.3% | 21.3% | 5.7% | 11.1% typed, 1.2% stale-prone | **11.5%**: provenance 546, markup 384, non-directive headings 81, node table 717, stale facts 194 |
| `BUILD-METHOD` M1+M5, 4,094 B, hand-classified | — | — | — | — | **~38%**: M1 budget history (lines 8-21) ~1,390 B, rationale clauses ~120 B, numbered headings 50 B |
| Whole corpus, 31 files, 545,635 B, by proxy | — | — | — | — | Lines dated or carrying a unit id: 5.3% (lower bound). Positional references (`§n`, `Mn`, `Sn`): **343** |

**Duplication**

| Measure | Result |
|---|---|
| Charter Protocols + Facts in a role's spawn | Twice per spawn, in 48 of 60 handoffs; median 2,880 B, **30.2%** of the median task block |
| "Verify every claim about current code" | 4 instruction files plus 51 handoffs |
| "at most 5 verify agents" | 6 files |
| "read a tool's refusal" | 4 files |
| "one mechanism per spec" | 4 files |
| How duplication is policed today | Instance by instance: `check-agent-cap-restatement.sh:17-25` says its noun list missed carriers three times; `memory/project/method-carriers.txt` holds 16 hand-kept rows |

**Commands run (abridged)**
```
python3 -I -c "...roles_lib.parse_charter(AGENTS.md)"   -> shape tagged rules 46 unique 46 max len 193
handoff scan of memory/builds/*/prompts                  -> 60 handoffs; 48 carry the charter block; median 2880; 30.2%
grep -cE "^\s*'.*' *\+?,?$" unattended-build.js          -> 312 lines, 29517 bytes
classify AGENTS.md                                       -> 8421 directive / 3571 pointer / 546 narration / 384 markup / 717 unused fact
git grep -lF "[$tag]" over the 36 practices              -> 18 named by any tool or hook file
```

**Where a record and the code disagree**

| Record claim | What the code shows |
|---|---|
| layer-roles `[tags]`: `BODY_CEILINGS` is the static block's budget | The ceilings price the **base body only** (`check_roles.py:84`). The 2,487–4,220 B of charter blocks in each rendered agent carry no budget. |
| layer-instruction `[current]`: `MEMORY.md` is 13,187 B | It now measures 14,005 B. |
| layer-instruction `[uncovered]` 4: protocols are "hand-written" | True at the source. All guides except MERGE-BAR and SESSION-KICKOFF are kit templates rendered by token substitution, so the rendering pipe already exists and only its source is prose. |

---

3. **Across the layers**

| Layer | It needs | It gives |
|---|---|---|
| instruction | (its home) | Units, templates, renderer, `instructions check`, the write command |
| flow | Item and step tags, actor kinds, each item's checklist order (procedures become items, not units); `required-by` targets | Each item's unit set; procedure views rendered from checklists; the `instructions.*` items |
| roles | Role declarations, trust profiles, return templates | Static-block and work-order templates; one charter carry per spawn |
| memory | Record-kind schemas from the P30 contract; the `record` door for change and loaded records; reuse entries stored as manifest parts | Directive units for each spec and record field; promotion of a standing directive into a unit (R-H) |
| runtime | Harness adapters' render targets; hook packs; a command adapter for the instruction command; act-launch cut | Hook text from units (gap-rt-13); the act session's load set (gap-rt-12); a write guard over render targets |
| observability | Journal reader | The loaded record and units cited by findings, feeding R-J pruning |
| integrations | Nothing in the core | An optional slot for notification text |
| distribution | govkit installs targets and merges overlay manifests; currency triggers re-render | Instruction packs as presets; overlay manifests |

| Sibling system | It needs from it | It gives it |
|---|---|---|
| Tags | Namespace registry, shape check, both-way joins, retired state; **a namespace for a unit's own identity** (R-B has none; `DIRECTIVES_CORE` handles need one) | The largest tag population and its joins |
| Code annotations | Excerpt anchors (P29 cuts at anchors); a `gov:note` that states a rule must point at a unit tag | Units' `enforcer` field resolving to an anchor; `ANNOTATION-STYLE` migrated into units |
| Role workflow shapes | Spawn counts and fan per item; static-block cacheability | Static and task templates with budgets; the per-item load set |
| Memory structure | Record schemas, promotion route, reuse-entry home | Field directives; `instructions.*` record kinds to declare |

---

4. **Candidates**

| | A. Lint in place | B. Tagged sections | **C. Unit rows + templates + render parity** | D. Derive only |
|---|---|---|---|---|
| Mechanism | Hand-written documents stay the source; add an envelope, a grammar lint and budgets | Documents stay the source; each heading carries a tag; the renderer slices sections | Each statement is a manifest row; per-kind templates assemble the documents; parity refuses any hand-edited target | No authored text; every line generated from structured fields by phrase templates |
| Builder item, instruction bytes | 35.6 KB (whole method) | 6.3 + 6.9 = 13.2 KB (M5–M7 whole) | about 4.1 + 4.3 = **8.4 KB** | Not reachable |
| Smallest losing test | Can a per-item load set be smaller than the whole document? | (a) Is a section about one unit's size? (b) Can a hand-written document be refused? | (a) Can today's already-unitized charter become rows losslessly? (b) Is a per-item set smaller than B's? | Does every practice have a structured source? |
| Result | **Loses.** Nothing selects below the document; `unattended-build.js:880` forces 29,326 B per item, so P27 cannot hold | **Loses.** (a) 2,633 B per handle against a 149 B mean unit; M6 and M8 each carry 3 handles. (b) No: the document is the source, so the four instance gates stay | **Passes.** (a) 46 rules, 46 unique tags, longest 193 B, inside `ONE_LINE_MAX`. (b) 8.4 KB against 13.2 KB (estimate) | **Loses.** 18 of 36 practices are named by no tool (`yagni`, `voice`, `signal`, `tokens`…). D survives as C's `source=` field |

**Estimation method.** A slice is the bytes of the handle's section × (1 − 0.38), where 0.38 is the measured narration share. A static block is the role's ceiling plus the bound rules at 149 B each. Tokens are bytes ÷ 4.

**C's risk.** The corpus has 191 ordered-step lines that have no unit type. They render from dDeclaredLoop's items, so until that build lands they stay legacy.

---

5. **The pick, specified**

**Unit row** (`<kit>/instructions.toml`, overlay at `.governance/instructions.toml`, merged by a row-keyed driver that extends `merge-rows.py`):
```toml
[[unit]]
tag = "unit.reuse-first"            # identity namespace: owed by the tags system
type = "directive"                  # directive|constraint|definition|pointer|policy-value|fact
modal = "must"                      # directive: must|never|always
text = "probe the map, then recall, once per spec set; record the seam or 'no seam fits'"
when = "item.design.spec-set"       # condition the renderer resolves
level = 3
select = ["item.design.spec-write", "role.spec-writer"]
describe = ["layer.instruction", "principle.p11"]
source = ""                         # or policy:<key> | probe:<name> | item:<tag>#<field> -> rendered, never typed
budget = "line"                     # line <=200 B | block <=600 B
required-by = ["item.design.spec-write"]
enforcer = "gate:spec tokens"       # or "none"
status = "active"                   # or "retired:<forward-tag>"
```

**Grammar.**
- Directive: modal + action + optional `when`.
- Constraint: subject + value + unit; the value comes from `source`.
- Definition: a registered term + meaning.
- Pointer: trigger + target tag or command; the target must be loadable.
- Policy value: rendered only.
- Fact: requires `source`; a typed fact is refused.
- Headings are directive units.

**Templates** (one per kind): charter (L0), card slots (L1), protocol slice (L3), Skill entry and path rule (L4), role static block (L5), work order (L6, handed data fenced), hook message, harness prompt module, spec field directives, `help/` page (never loaded).

**Owner.** Layer `instruction`. The mechanism, charter, role and work-order templates and the write command belong to dOrderedCharter. Guide migration and slices belong to dConvergedCharter. Hook and act templates belong to dWellOiledMachine. Kits: `playbook` (renderer) extended; `roles` re-pointed to the shared renderer. Records: `instructions.change` and `instructions.loaded`, declared in the memory contract.

**Checks** (all in one leg, also run at render):

| Check | Turns red when |
|---|---|
| I1 schema | A row lacks `type` or `level` |
| I2 grammar | A provenance paragraph, a numbered heading, "the marker below", or "Worktrees: none yet" (`AGENTS.md:4-8,12,173`) |
| I3 positional | `§n`, `Mn` or `Sn` appears in a unit (343 today) |
| I4 one fact | Two active units share a subject and value (replaces the restatement and method-carrier gates) |
| I5 parity | A target's bytes differ from its render |
| I6 unregistered | A new `memory/guides/X.md` or `.claude/agents/x.md` outside the registry and the legacy list |
| I7 budget | A set is over its load-point row (too much) or misses a `required-by` unit (too little) |
| I8 joins | A selector names an undeclared role or item |
| I9 single carry | A unit appears twice in one spawn (red today on 48 handoffs) |

**Read-path cost.** About 2.9 KB static plus 2.5 KB of slices per researcher item, and 8.4 KB per builder item. The charter drops to about 14.8 KB. Whole-guide reads for triggers the item decides go to 0.

**Measurement.** Re-render the 60 recorded handoffs through the new templates and diff the loaded records. Read `input_tokens` and cache-read tokens per spawn from transcripts; this needs `handoff.py:616` extended, since today it reads output tokens only.

---

6. **Items and policies**

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `instructions.propose` | role | Returns a proposed unit diff | Proposal record committed through `record` | accept → `edit`; reject → closed |
| `instructions.edit` | owner | Writes the row and its change record in one commit | Commit plus change record with proof verified by the command adapter | check red → refused, ask filed |
| `instructions.render` | command (regen) | Re-renders affected targets | I5 green at that commit | drift → commit refused |
| `instructions.load` | executor | Cuts the load set at spawn | Hook-written loaded record (tags, bytes per load point) | over budget → ask or route-back (R-C) |
| `instructions.measure` | hook | Measures injected points at session start | Hook-written measurement | breach → reported |
| `instructions.migrate` | builder | Dispositions each source paragraph as unit, item, `help/` or deleted | Ledger sums to 100%; legacy list shrinks | — |

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `instructions.slices` | `handed`, `pointer` | `handed` | Removes method-document reads (gap-orient-07); `pointer` trades tokens for a stable cached prefix |
| `instructions.legacy` | `shrink-only`, `refuse` | `shrink-only` | Arms I6 before Convergence lands |

The existing keys `instructions.checks`, `instructions.edit` and `instructions.proof` are served unchanged.

---

7. **Gaps**

**Closed:**

| Gap | Closed by |
|---|---|
| gap-found-09 | Joins (with the tags system) |
| gap-found-10 | Load sets and budgets |
| gap-found-11 | Grammar |
| gap-found-12 | Rendered slices |
| gap-found-13 | Skill template |
| gap-found-15 | Write path |
| gap-found-16 | Loaded record (input only) |
| gap-orient-07 | Handed slices |
| gap-rt-12 | Act-session load set |
| gap-rt-13 | Hook text from units |

**New:**

| Gap | Evidence | Suggested owner |
|---|---|---|
| N1. Every role spawn carries the charter blocks twice | 48 of 60 handoffs; median 2,880 B, 30.2% of the task block; `render_agents.py:135` and `handoff.py:402-407` call the same function | dBoundRoles |
| N2. Workflow harness prompts are an unregistered load point with no grammar, budget or parity | 38.4 KB of prompt literals, including the "WHOLE" order at `unattended-build.js:880` | dWellOiledMachine (role-harness point) |
| N3. The static block's budget covers only its base body | The 2,487–4,220 B charter blocks per role sit outside `BODY_CEILINGS` (`check_roles.py:84`) | dBoundRoles |
| N4. One-fact is gated per instance, never as a class | `check-agent-cap-restatement.sh:17-25`; `method-carriers.txt` | dOrderedCharter (I4) |

---

8. **Forks**

| Fork | Options | Recommendation |
|---|---|---|
| Unit source format | TOML rows; one-line Markdown `- [tag] text` plus an attribute sidecar | **TOML.** `tomllib` is already used in 13 tools files, and every field sits in one place |
| When I6 is armed | At dOrderedCharter with a shrink-only legacy list; only after dConvergedCharter | **At dOrderedCharter.** Otherwise the guides stay unrefused until the last build |
| How harness prompts get units | Generated data module checked by parity; read at runtime through `instructions view` | **Generated module.** It does not depend on a shell inside the Workflow |
| Human-readable whole guides | `help/` rationale only, with slices rendered on demand; also commit whole rendered views | **`help/` only.** A committed whole view is a second copy |
