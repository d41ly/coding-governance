# Research: the instruction writing system, run A

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 77's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-24-researcher.md`, which dispatch 78 runs
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`.

---

## 1. Verdict

Every loaded instruction becomes a typed unit: one TOML row in its kit's manifest, about 200 characters long, carrying the fields the settled layer names. A small, closed set of document-kind templates assembles units into each load point by tag. A template holds only slot selectors, no prose. One renderer extends `roles_lib.render_charter_blocks` and the playbook `PROBES`. One gate refuses any file in a harness load path that is not byte-equal to its render. Authored units hold only judgment. Facts, policy values and pointers are derived. Rationale goes to `help/`. Today a role spawn carries about 8.7 KB of fixed instruction text, and an agent reads whole method documents averaging 34 KB. The pick holds that fixed text to about 4.8 KB and replaces item-decided whole-document reads with handed slices, and a check can hold both numbers.

## 2. Today

| Part | What it does | Measured | Cite |
|---|---|---|---|
| Charter render | Template, `kit:`/`when:` fences (24 markers), `{{X}}` placeholders, `PROBES`-derived facts | 13,695 B template → 16,732 B `AGENTS.md` | `tools/playbook/render_playbook.py:115-117,562-575` |
| One-line grader | Each rule is a `- ` bullet of at most 200 chars inside `<!-- one-line -->` | the only text grammar beyond micro-formats | `render_playbook.py:124-126,664-695` |
| Role renderer | Role body plus the charter rules picked by its `rules:` tags, plus Protocols and Facts carried whole | 9 agent files, 45,213 B; sources 14,956 B body + 4,590 B front matter | `roles_lib.py:61,67,279-300`; `check_roles.py:85-89` (`BODY_CEILINGS` 1,536 to 4,096) |
| Handoff renderer | Role, then the task fields `reads` declares, then the **same charter blocks again** | 584 handoffs, median 3,320 B; researcher task part median 9,608 B | `handoff.py:312,402-416` |
| Whole-document templates | Token substitution only (`{{MEMORY_ROOT}}` ×46, `{{KIT_DIR}}` ×44, `{{TOOL_ROOT}}` ×29), plus parity tests | 17 `.template.md` docs; 426,612 B of live renders | `tools/memory-tree/kit-dogfood-parity.test.sh:1-30`; `tools/workflows/check-protocol-parity.test.sh` |
| Hand-written load-path docs | No source, no render | MERGE-BAR 7,884; SESSION-KICKOFF 19,626; `.claude/rules/product.md` 3,011; kickoff `SKILL.md` 18,310; deploy-governance `SKILL.md` 11,258 (60,089 B) | `git cat-file -s` |
| Gates over output | Template size, micro-formats, line length, playbook parity (S4), placeholders, roles catalogue and render, two doc-parity legs, format-guard, agent-cap restatement | about 34 of 140 legs | `tools/gate-legs.json` |
| Budgets | High-water ratchet | **7** rows | `tools/template-size-limits.txt:48,60,85,126,143,151,167` |

**Load per reader:**
- **Main session:** `AGENTS.md` (16,732 B), the auto-memory index (13,187 B per `layer-instruction:250`) and 16 agent and Skill descriptions (2,811 B).
- **Role spawn:** a system prompt of 5,872 chars and a task of 7,478 to 9,868 chars (`layer-roles:81-84`).
- **On demand:** 811 method-class reads went to whole documents across 171 agents (`layer-roles:148-157`). Weighted by calls, the mean document read is **34,013 B**: (131×39,335 + 130×29,326 + 59×19,626 + 43×58,542 + 17×16,732) / 380.

**Statement-type mix, sample 1: `AGENTS.md`, every line** (awk byte sums by line range):

```
render markers/comments: 384   provenance title+para+italic: 546   label headings: 110
node registry table+lines: 1158   stale-typed facts (173,176): 194
rules 15-50: 5327; mf rules 72-81: 1532; repo 87-95: 1121   microformat defs 56-68: 955
tools 1815; roles 1383; protocols 373   facts 1850
```

- P11 deletes 1,234 B (7.4%) outright.
- The node table (1,158 B) is never acted on, which brings the waste to 14.3%.
- Everything that remains classifies as directive, definition, pointer or fact.

**Sample 2: `REVIEW-PROTOCOL.md` lines 1-70, hand-classified.**

```
sample 1-70: 4692   load-bearing (8-10,13-14,20-21,32-34,36): 777
provenance 3-5: 296; history 15-18: 389; measurements 23-30: 313; mechanism narration 38-70: 2632
```

Only **16.6%** of the sample bears load. Corpus-wide, guides, Skills and templates (472,433 B) are 74.4% paragraphs, 10.9% bullets, 7.5% tables and 5.2% code. The charter is 88.4% bullets.

**Duplication:**
- Verbatim, it is near zero: 3 of 3,181 sentences of 60 chars or more repeat (scratch `dup.py`).
- Paraphrased, it is not. The re-render rule appears in **8** live documents, the verify-agent cap in **5**, and spec-first in **4**:

  ```
  git grep -cE "never (hand-)?edit the rendered|never hand-edit|re-render" -- $L
  → cleanup 2, drift-audit 1, runlog 1, AGENTS 4, HYGIENE 3, TEMPLATE-SPEC 1, SESSION-KICKOFF 1, UNATTENDED-VERBS 3
  ```

- Charter blocks are repeated: 48 handoffs carry 148,824 B of charter blocks that the agent file also carries. For the researcher that is 2,879 B per spawn (rules 555 + Protocols 463 + Facts 1,861).

**Where a record and the code disagree:**
- `layer-instruction:267` says six load points carry budgets. The file has a seventh row, `memory/builds/*/spec/` (`template-size-limits.txt:167`), and the high-water file records five specs above it (49,730 to 80,139 B).
- `layer-roles:89` says the charter reaches a role "only as its file's `## Charter` section". `handoff.py:402-407` also appends it to the task, unconditionally.

## 3. Across the layers

| Layer | What the system needs from it | What it gives it |
|---|---|---|
| instruction | the ladder, envelopes, `instructions.*`, the R-I manifest | the unit schema, grammar, templates, renderer, checks and command (it is this layer's writing engine) |
| flow | items with declared actors, triggers and policy reads; the regen leg | `<step>.<item>` load sets; templates for the card frame and the protocol slice; step-scoped practice reach |
| roles | static-block fields (job, never-list with enforcer, allowance, trust profile, return template) | the role-static and work-order templates; per-role and per-item refusals; no repeated charter blocks |
| memory | record kinds for the change record and the render ledger; the promotion route (R-H) | the data fence (records are level 7); one renderer factory for record templates and the HYGIENE view |
| runtime | the harness adapters' load globs (R-K); a write-guard hook pack; spawn-backend capability ("loads static block") | the hook-message template (`gap-rt-13`); the act-session load set (`gap-rt-12`) |
| observability | journal reader for render-ledger rows | the loaded-units witness R-J prunes on |
| integrations | none (core never depends) | the notification text template |
| distribution | install of render targets; overlay merge | manifests merge deterministically; rendered views re-render after install |

| Other system | What it needs from that system | What it gives that system |
|---|---|---|
| Tags | a namespace for unit ids (R-B lists none for units); selector expression syntax; the retired-tag lifecycle | the largest selector population, and the join checks' populations |
| Code annotations | stable `anchor` tags that pointer units and handed excerpts can target | the grammar checker as a library; the rule that comments are data unless registered as units |
| Role workflow shapes | the item list per role; static-block field set | templates, budgets and refusals per role and item |
| Memory structure | record kinds; one template factory with P30 | units never live in memory; the promotion target |

## 4. Candidates

| Candidate | Mechanism | Efficiency (method) | Smallest losing test | Result |
|---|---|---|---|---|
| **A. Unit store + kind templates** | Units are TOML rows. A template per document kind is an ordered list of slots (selector, type filter, budget). Every load point is a render, and a non-render is refused. | Spawn fixed text about 4.8 KB vs 8.7 KB. Item-decided method reads go from whole documents (34 KB mean) to handed slices. | (a) Load-bearing text cannot be atomized. (b) The charter cannot fit 32 KiB under the v2 front door. | (a) Passes: the charter is 88.4% one-line bullets, and in the guide sample the load-bearing 16.6% is sentence-sized. (b) **Passes only if** practice reach renders as step-scoped units: inline reach is estimated at 31,342 B, leaving 4% headroom (fork F2). |
| B. Annotated markdown in place, plus a slicer | Documents stay the source; each unit is tagged inline; a slicer cuts load sets. | Same slicing as A, cheapest migration | A unit needed by several load points must be copied or pointed at, and slices cut out of context break. | **Loses.** 17 of 22 cited rule tags load into 2 or more roles plus the charter (the `rules:` count). The guides hold 104 context-dependent references ("above", "below", "the following"). |
| C. Fully generated controlled language | No authored text: every sentence is generated from structured sources by phrase templates. | Lowest bytes | Judgment text that no structured field produces | **Loses as the whole system.** 76.5% of role source bytes are authored body (14,956 of 19,546). C survives inside A as the `derived` source kind. |
| D. Pull on demand | Nothing is pushed; agents call `instructions show <tag>` when a trigger holds. | One call or more per slice | Lookups per orientation; P27's "too little" refusal must be decidable at render | **Loses.** Today's Protocols pointers already are D at document size: 811 reads, and briefed agents spend 15.1% of calls on method documents (`layer-roles:173`). A pull cannot satisfy a refusal at render. D survives for triggers that depend on what the role finds (`layer-roles [tags]`). |

Commands for B's test:

```
grep -h "^rules:" tools/roles/agents/*.agent.md | … | uniq -c → verify 6, class 5, … "tags cited by >=2 roles: 17"
git grep -ciE "\b(above|below|this section|as noted|the following|…)\b" -- $L → TOTAL 104
```

## 5. The pick, specified (A, with C's derived source kind and D for found triggers)

**The unit**, in `tools/<kit>/instructions.toml` (parts allowed), the adopter's in its overlay, rows sorted by tag:

```toml
[[unit]]
tag = "practice.verify"        # its id; namespace from the tag system
type = "directive"             # directive|constraint|definition|pointer|policy|fact
level = 0
scope = ["reader.every"]       # selectors only
when = ""                      # the directive's condition / the pointer's trigger
text = "Verify before claiming done: …"   # one line, at most 200 chars (ONE_LINE_MAX)
source = "authored"            # authored | derived:<probe|checklist|role|schema|policy>#<key>
enforced-by = ["leg.…"]        # P16 join; empty only with unenforced = "<why>"
required-by = ["role.builder"]
budget = "line"
help = "help/practices.md#verify"   # rationale, never loaded
kit = "playbook"
status = "active"              # retired keeps a forward tag
```

**Per-type fields and checks:**
- A directive needs a modal (`must`, `never` or `always`).
- A constraint needs `value` and `enforced-by`.
- A definition needs `term`, and may carry a `rows` table (the micro-formats).
- A pointer's `target` must resolve to a unit, a slice tag or a registered command, never a document path.
- A policy unit carries `key`.
- A fact carries `probe` and has no authored `text`.

**Templates.** There is one per document kind: `charter`, `instruction-map`, `role-static`, `work-order`, `protocol-slice`, `skill-entry`, `path-rule`, `hook-message`, and `spec-instruction-fields` (the grammar of P12's directive fields; the record template itself comes from P30). Each template is a skeleton:

```toml
[template]
kind = "role-static"
level = 5
budget-carrier = "BODY_CEILINGS"

[[slot]]
heading = "heading.role-job"     # headings are directive units
select = "role.{role}"
types = ["directive", "constraint"]
on-empty = "refuse"              # or omit | optional-slot
```

Harness variants come from the Runtime adapters (R-K). `help/` is outside every load set.

**Owners.** The instruction layer owns the system. dOrderedCharter builds the schema, grammar, renderer, the four core templates and the command. dBoundRoles builds role-static and work-order. dWellOiledMachine builds hook-message. dConvergedCharter builds protocol-slice and skill-entry. The engine's kit is `tools/playbook/`, reusing `roles_lib.render_charter_blocks`, `PROBES` and `tomllib` (used in 16 files today).

**Records:** an instruction change record (row diff, proof, commit) and a render ledger row (spawn, unit tags, bytes, hashes). Both are declared in the memory contract.

**Checks, each with the case that turns it red:**

| Check | Red case |
|---|---|
| Unit schema | a fact with no `probe`; text over 200 chars; a directive with no modal |
| Grammar over every render | today's `AGENTS.md:4-8` provenance, `:12` "## 1.", "the marker below", `:173` "Worktrees: none yet" |
| Render-or-refuse | a hand edit to `.claude/agents/gov-builder.md`; `memory/guides/MERGE-BAR.md` unregistered (red on 5 files today) |
| Load-point budget (extends `check-template-size.sh`) | a role-static block over `BODY_CEILINGS`; a work order over its packet budget |
| Joins, both ways (R-B) | a role with no unit; a unit with no selector |
| References | a pointer to a retired tag; a rename that strands `required-by` |
| One text, one unit | two units whose normalized text is equal (the 3 verbatim cross-role sentences found today) |
| Write guard (Runtime hook pack plus git pre-commit) | `Edit AGENTS.md` |

All of these are stdlib parsing over about 0.5 MB, so each fits the 300 ceiling today's instruction legs carry.

**Read-path cost:**

| Load point | Today | Pick |
|---|---|---|
| Charter | 16,732 B | about 23.0 KB with reach as step units (14,340 kept + principles 5,400 + drive 1,800 + map 1,450) |
| Researcher spawn, fixed text | 5,872 + 2,879 = 8,751 B | static block ≤3,072 + rules 555 + envelope about 200 + item units about 1,000 = about 4.8 KB |
| Method, item-decided trigger | whole document, 34 KB mean | handed slice at its budget class (about 1.5 KB) |

At about 4 bytes per token, that is roughly 1,000 tokens saved per spawn on fixed text, and up to about 8,000 per whole-document read avoided.

**How to measure it:** the render ledger (bytes per load point per spawn), the harness `.prefix.json` records, and the runlog extractor's method-class calls per role and item, before and after on the same item tags. The checks hold the budgets.

## 6. Items and policies

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `design.instruction-units` | spec writer | declares the unit rows a unit adds or changes, as spec fields | the schema check on the spec | invalid → back to the spec writer |
| `build.instruction-render` | command (the renderer) | re-renders affected load sets in the unit's commit | render-or-refuse green at the commit | drift → the builder |
| `test.instruction-checks` | command (bar leg) | the eight checks above | verdict | red → Build |
| `<step>.<item>` spawn render (fills every role item) | executor | renders the static block and work order, with refusals | render-ledger row, hook-written | over budget or missing → ask naming the overage (R-C) |
| owner edit (owner control) | owner via `instructions` | add, edit, retire; writes the row and change record in one commit | the commit plus `instructions.proof` | proof fails → refused; an agent → proposal record |
| `maintain.instruction-prune` | the Loop Review | prunes units that load but nothing enforces or cites | ledger plus findings citing tags | → proposal |

| Key | Values | Default | Why |
|---|---|---|---|
| `instructions.task-charter` | `when-not-static`, `always` | `when-not-static` | removes the 2,879 B repeat per spawn; `always` serves backends that load no static block |
| `instructions.found-triggers` | `slice-pointer`, `hand-all` | `slice-pointer` | D's residue: hand every slice and pay the bytes, or point at a slice and pay a call |
| Existing: `instructions.checks`, `instructions.edit`, `instructions.proof` | as settled | as settled | the hand-written refusal is one of the checks, so LR-1 softening applies |

## 7. Gaps

**Closed:**
- `gap-found-11`: the grammar.
- `gap-found-12`: slices, not monoliths.
- `gap-found-15`: the command and change record.
- `gap-orient-07`: handed slices.
- `gap-rt-12`: the act-session template.
- `gap-rt-13`: the hook-message template.

**Partly closed:**
- `gap-found-09`: needs the tag system.
- `gap-found-10`: injected load points are only measured.
- `gap-found-13`: the skill-entry template.
- `gap-found-03`: ranked envelopes in every template.

**New gaps exposed:**

| Gap | Evidence | Owner |
|---|---|---|
| A typed spawn loads its charter blocks twice | `handoff.py:402-407` plus `render_agents`; 48 handoffs, 148,824 B | dBoundRoles |
| Nothing stops new hand-written instruction text before dConvergedCharter, the chain's last build | v2 `[chain]` parents; needs a shrink-only list of 33 load-path docs from dOrderedCharter on | dOrderedCharter |
| Two template engines are planned and four parity mechanisms exist | dTotalRecall renders HYGIENE as a view and generates templates; `adopt-playbook --check`, `adopt-roles --check`, kit-dogfood-parity, protocol-parity | dOrderedCharter (factory) |
| The charter cap is at risk under inline reach | 31,342 B estimate against 32,768 | dOrderedCharter |
| A budget row stands below its own high-water | `template-size-limits.txt:167` vs 5 specs at 49,730 to 80,139 B | dIndexedDesign |

## 8. Forks

| Fork | Options | Recommendation |
|---|---|---|
| F1 Source format | TOML row store; markdown with inline annotations | TOML: rows merge additively and units render into many targets (B's test) |
| F2 Practice reach | as step-scoped units in work orders, with the charter keeping one line per practice; inline in the charter (v2 `[front-door]`) | Step units: about 30% headroom vs about 4% |
| F3 Migration timing | each chain build converts the guides of its step (BUILD-METHOD and TEMPLATE-SPEC → dIndexedDesign, HYGIENE → dTotalRecall, REVIEW → dFairHearing, UNATTENDED-* → dWellOiledMachine, MERGE-BAR → dWitnessedBar, SESSION-KICKOFF → dRankedPlan), with a shrink-only list from dOrderedCharter; or all at dConvergedCharter | Per build |
| F4 Rendered modal | MUST, NEVER or ALWAYS rendered literally; imperative mood with the modal kept as a field | Literal at levels 0 to 2, imperative below (about 180 B on 36 rules) |
| F5 Migration import | `instructions import` splits a document into candidate units and sends unclassifiable text to `help/`; hand conversion | The import, with each result reviewed in its unit: the sample shows about 83% of guide text leaves the load path |

No file was written. The only scratch output (`a.md`, `dup.py`) is under `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\`.
