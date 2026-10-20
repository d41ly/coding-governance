# Research: the tag system, run B

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 74's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-22-researcher.md`, which dispatch 73 runs
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`.

---

## 1. Verdict

I recommend one tag grammar, `<ns>.<seg>[.<seg>]`, split into namespaces. A section anchor `<doc> [<seg>]` is scoped to its document, and ids keep the memory contract's own grammar. There is no authored registry. Each namespace has one declaring source in the layer that owns it. Each source registers an extractor at a new instruction-layer point, `tag sources`, and the extractors derive an index that is cached and never loaded whole. One command, `gov tag`, resolves an address to the smallest leaf slice. A rename or retire is written by the source's own write path, and its change record supplies the redirect. Joins are gates. Measured gains:
- **Lookups:** 3 → 1 per citation, and 0 when the work order already carries the slice.
- **Bytes per section:** median 2.2 KB against 25 KB for the whole record.
- **Check cost:** 0.18 s for 735 rows.

## 2. Today

| Kind | Grammar / where written | Reader | Check | Measured |
|---|---|---|---|---|
| Charter rule tags | `- [tag] ` under `## 1.` (`AGENTS.md:12`; `roles_lib.py:61,63`) | `render_charter_blocks` (`roles_lib.py:279`). This is the only code that resolves a tag | `check_rule_tags` (`roles_lib.py:252`), role→rule direction only. R1 asks only that some tag is cited (`check_roles.py:16`) | 46 rules. 10 roles bind 22 of them, and 24 rules bind no role |
| Record section tags | `## [tag] Title` | nothing; agents grep | none | 358 headings in 34 files of 4,134, all in dClosedLoop. 50 tags repeat across files. 1,438 citations, 499 of them qualified by a record name, none by path |
| Handoff read keys | `<family>:<field>`, a closed set of 25 (`roles_lib.py:36-40`) | handoff render | R3 | 32 uses in role files |
| Unattended handles | `DOD_CORE` 13 (`unattended.sh:868`), `DIRECTIVES_CORE` 17 (`:1042`), each handle mapped to an `Mn` number | unattended driver | unit tests | 30 |
| Ids | `FAMILY-<slug>-<seq>`, minted by hand-grep (`HYGIENE.md:168-191`) | `grammar_for` (`memory-recall/extract.py:569`), imported by 6 files | hygiene checks 13 and 14 | 2,126 distinct |
| Gap ids | `gap-<area>-NN` | none | none | 200 distinct, in 18 areas |
| Gate legs | free prose with spaces (`gate-legs.json:14`) | runner; the map's `[claims]` | the map's coverage | 140. 139 fail a tag shape |
| Lexicon cells | `<lang>.<kind>` (`.lexicon.conf:506`) | lexicon | lexicon | 4 cells |
| `gov:` markers | `gov:<name>` | each owning reader | `marker-contract.test.sh` for some | about 25 kinds. `gov:feature` and `gov:note` appear 0 times outside `memory/` |
| Both-ways join engine | `compute_coverage` (`codebase-map/map_lib.py:1404`) | 11 inventories (`map_extractors.py:189`) | the map's leg | the one generic join today, but it sits in an optional component |

**How an agent resolves `layer-memory [annotations]` today.** It takes three calls: Glob for the dated path, Grep for the heading, then Read with a guessed limit. The measured sizes:

```
$ python3 -I slices.py
tagged files 34 sections 358
median slice B 2212.5 mean 4104 max 41069
median whole file B (tagged files) 24999.0
mean slice/whole ratio 0.100
 big layer-runtime.md design 41069
```

The citations miss in four ways:
- **Overloaded brackets:** `[x]` means four things. 10 charter rule tags are also section tags (`[reuse]`, `[records]`, `[roles]` and others). 9 cited `[x]` are TOML tables or practices that are declared nowhere: `[check]`, `[config]`, `[claims]`, `[effort]`, `[tdd]` and others.
- **Short names:** at most 7 of 499 qualified citations fail to resolve, because "roles" can mean `layer-roles` or `flow-roles`.
- **Renames:** the Knowledge→library rename leaves 38 mentions in 9 frozen records. The only redirect is a hand-typed constant (`debt-reviews-compared-instruments.md:80`), and it is repeated into every handoff, this one included.
- **Method guide:** "M5 and M12" sends a reader to `BUILD-METHOD.md`, which is 29.3 KB, when the two slices are 4.0 KB.

**Positional references still standing.** This is an upper-bound grep (`git grep -ohE <regex> | wc -l`):

| Kind | Code (404 files) | Docs (17) | Records, frozen (4,085) |
|---|---|---|---|
| `§n` | 737 | 242 | 43,935 |
| `Mn` | 794 | 96 | 12,601 |
| `check n` | 2,087 | 125 | 9,493 |
| `Rn` / `Vn` | 1,122 / 241 | 7 / 0 | 3,814 / 722 |
| `Sn` / `ACn` | 4,350 / 8,277 | 5 / 17 | 47,695 / 58,110 |
| `section n` | 405 | 33 | 5,285 |

The hygiene gate itself requires positional `§n/Sn/ACn` scope tokens (`check-memory-hygiene.sh:106`). The playbook-parity S4 arm already refuses charter citations by number (`check-playbook-parity.sh:14`).

**What the design already settles:**
- R-B: namespaced spelling, 12 namespaces, selectors and descriptors, four joins, unarmed until populated (`layer-instruction.md:402-441`).
- A retired tag keeps a forward pointer and is never reused (`:569`).
- `role.<name>` (`layer-roles.md:344`).
- `gov:note` and `gov:feature` (`layer-memory.md:649-691`).
- dOrderedCharter owns the grammar and the resolver (`architecture-v2.md:942`).

**What it lacks:**
- one resolver and an address form for sections;
- where aliases come from;
- namespace ownership, and what stops two layers minting one tag;
- tags for legs, points, hooks, commands, features, classes, fields and units;
- an owner for the positional inventory (v2 `[open]`, `:967`, has no gap).

**Where the records and the code disagree:**
- `layer-memory [names]` names 2 memory-tree importers of `grammar_for`. The code has 5: `gen_build_index.py:5006`, `merge-rows.py:263` and `transition_audit.py:180` beside the two named.
- "Stage" means three things. The handed fact keys stages to the loop kit. R-B's namespace is `step`. `workflows.toml:37` uses camelCase harness stage keys such as `specWriter`.

## 3. Across the layers

| Layer | Needs from it | Gives it |
|---|---|---|
| instruction | unit rows carrying tag and scope (R-A) | selectors for P27 load sets, and level-3 views sliced by tag |
| flow | item and step rows in the loop kit as the sole declarer | item→unit joins; `next —` lines and card pointers by tag |
| roles | role rows, `rules:`, fields | `role.*` and `field.*` selection; slices in place of the 811 method-document reads (`layer-roles.md:963`) |
| memory | the record contract's `record.<kind>`; `record` writing rename rows | section slices for the trail; `class.*` and `feature.*` for the library; an index for recall |
| runtime | `gov tag` as a read-only command adapter; refusal at spawn render | tags for points, hook packs and commands; journal events keyed by item tag |
| observability | reads the journal and the index only | detectors: unused tags (R-J pruning) and the positional trend |
| integrations | none from the tag system | registers adapter names under its own prefix at core points |
| distribution | `layers =` and kit tags in `kit.toml`; deterministic overlay merge | redirect rows ship with a release, so adopters' citations survive renames |

| System | It needs from that system | It gives that system |
|---|---|---|
| Annotations | anchors as full spellings; a core line-scan extractor for `gov:` lines | the grammar, the `feature` and `class` namespaces, and T3 resolution of `refs=` and anchors |
| Instruction writing | template headings as tagged directives; the manifest as the declarer for `unit.*` | unit tags, selectors, and pointer units whose target is a tag |
| Role shapes | each shape's items and fields declared once | selection by role and item, and slices inside work orders |
| Memory structure | `record` as the door for renames; the id parser | section slicing, the `record` namespace, and aliases derived from change records |

## 4. Candidates

| | Mechanism | Efficiency (method: tool calls from citation to text; bytes read; scan wall time; rows authored twice) | Smallest losing test | Result |
|---|---|---|---|---|
| **A. Federated, derived index** | Each namespace's owning source declares it. Registered extractors derive a cached index, and `gov tag show` returns the leaf slice | 1 call; 2.2 KB median; 0.18 s; 0 rows authored twice | Some namespace has no single declarer, or the index needs authored rows, or the scan takes over 1 s | **Survives.** The probe builds 735 rows from 7 sources, with 0 authored, 0 duplicate (ns, name) and 0.178 s (output below) |
| **B. Central authored `tags.toml`** | Rows are minted through `gov tag new`, and targets reference them | 1 call; same bytes; 735 + 75 items + 146 policy keys = 956 duplicated rows | The registry restates a fact another source already declares | **Loses.** All 735 probe rows already have a declarer, so B breaks one-fact and still needs A's extractors to catch drift |
| **C. No registry, grep at query time** | Namespaces are told apart by syntax; the resolver greps anchors | 2–3 calls (grep gives no end line); about 80 B of redirect prose per handoff | A rename cited by frozen records resolves with no hand-typed redirect, and the bracket form is unambiguous | **Loses.** Knowledge: 38 mentions in 9 frozen records, redirected only by the typed constant at `:80`. 10 rule/section collisions and 9 TOML citations. Items and policies live in tables, so per-source parsers are needed anyway, which is A without the index |
| **D. Opaque stable ids** | Hashed ids with display names; renames are free | 1 call per citation, and every citation needs one | A citation tells its reader what it names with no lookup | **Loses.** 0 of 1,438 would. P11 and CV2 require tags that "clearly define sections" |

The probe that tests A (read-only; writes nothing):

```
$ python3 -I proto_index.py
rows 735 {'section': 358, 'practice': 46, 'leg': 140, 'kit': 17, 'role': 10, 'class': 133, 'feature': 31}
build seconds 0.178
json bytes 109647
dup (ns,name): 0 []
leg names failing a [a-z0-9-] tag shape: 139 of 140
```

A grep of every heading over `memory/` takes 0.06 s, which is the floor C shares. I stop at four: a tracked index against a cached one differs from A only in detail (fork F2).

## 5. The pick, specified

**Grammar.** There are three address forms, and `gov tag` tells them apart by shape.

| Form | Shape | Unique within |
|---|---|---|
| Tag | `<ns>.<seg>(.<seg>)*`, where seg is `[a-z0-9][a-z0-9-]*`, at most 64 characters | the whole tree |
| Section | `## [<seg>] Title`, cited as `<doc> [<seg>]`, where doc is a registered record short name or a unit tag | its document |
| Id | the memory contract's parser (`FAMILY-…`, `gap-…`) | the id family |

- **Short form:** the short form stands only where the context fixes the namespace: checklists, the policy file, the charter's `[reuse]`, and `rules:`.
- **Namespaces:** R-B's twelve, plus `section`, `unit`, `field`, `leg`, `point`, `hook`, `command`, `feature` and `class` (F4).

**Namespace register.** It is a field in each layer contract: a namespace's owning layer, its declaring source, its extractor, whether it is a selector or a descriptor, and its prefix owners. Examples of prefix owners: `item.<step>.*` belongs to the step's declarer, and `policy.<area>.*` to the area's layer. An expansion mints only under its own prefix, at a core point.

**Mint, rename, retire.**
- A tag is minted by adding a row through its source's write path: the instruction command, `record`, or the unit that edits the loop definition.
- A rename writes a new row and a `retired → new` row, one hop, never reused.
- The redirect is derived from that write path's append-only change record, so no alias text loads.

**Index and resolver.**
- The index is an untracked cache keyed by tree id (F2), never loaded whole.
- `gov tag show <addr>` prints path:line, the blob SHA and the leaf slice (`tags.slice`).
- `gov tag where <tag>` lists citations and uses.
- Owner: the instruction layer, kit `playbook`, chain build dOrderedCharter. It declares the `tag sources` point. Extractors ship with their populations:

| Chain build | Extractors |
|---|---|
| dDeclaredLoop | step, item, policy |
| dBoundRoles | role, field |
| dTotalRecall | section, record, feature, class, code anchors |
| dWitnessedBar | leg |

**Checks.** All run in the `tags` leg pack and at render, and soften only through `instructions.checks`.

| Check | Turns red on |
|---|---|
| T1 shape and registered namespace | `item.Build.Scope`; `legs.x` |
| T2 unique; a section unique within its document | a second `## [design]` in one record (0 today, so planted) |
| T3 every citation, `rules:` entry and `refs=` resolves | `layer-memory [nmes]` |
| T4 no new text cites a retired tag; no reuse; no chain or cycle | `layer.knowledge` declared again |
| T5 each namespace owned by one contract; expansions stay under their own prefix | an observability contract declaring `item.build.x` |
| T6 R-B's joins, armed per population, non-empty | a step with no unit. Until armed it reports "unarmed" |
| T7 positional references per kind in live text at or below the pin | a new "see M5" in a guide |

**Read-path cost.** Nothing new is always loaded. Each citation costs 10–25 B. Each resolution is one call returning a leaf slice, which on the mean slice/whole ratio is 10% of the document.

## 6. Items and policies

The pick adds no item. It fills six:

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `design.unit-spec` | role spec-writer | declares new, renamed and retired tags as a spec field | the return's hash | as declared |
| `design.overlaps` | command | flags two live builds declaring one full tag | the command's record | overlap → its existing route |
| `build.unit-pass` | command | the render refuses T1–T4 | the render's record | refusal → frontier |
| `test.verdict` | command | runs the `tags` leg pack | the bar's verdict | red → `test.route` |
| `test.merge` | command | runs T2 and T5 on the prepared merge, catching concurrent mints | the merge verdict | red → `test.route` |
| Maintain detector (observability) | command | measures unused tags and the positional trend | the detector reading | filed into triage |

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `tags.slice` | `leaf`, `subtree` | `leaf` | the median leaf is 2.2 KB, while parent sections reach 41 KB |
| `tags.retired-cites` | `refuse-new`, `warn`, `allow` | `refuse-new` | frozen records resolve through the redirect, while new text cannot cite a dead name |
| `tags.positional` | `shrink-only`, `refuse`, `report` | `shrink-only` | Convergence migrates the references, and the ratchet holds the line meanwhile |

These keys come before the policy file exists, which v2 `[owed]` already lists as `charter-before-policy`. They run on their defaults until dDeclaredLoop.

## 7. Gaps

- **Closes** `gap-found-09`, together with the population builds that arm T6.
- **Serves** `gap-mem-08` (anchors and T3) and `gap-mem-06` (the resolver reads the one id parser).
- **New gaps.** The owner session mints the ids; I propose them in Foundation, after `gap-found-19`.
  1. **Positional references have no gap and no ratchet.** The counts are in section 2, and v2 `[open]` holds only an interpretation.
  2. **One spelling means several things.** Four separators are in use (`.`, `:`, `[]`, `-`). 10 rule/section collisions, 9 TOML citations, and 2 item/policy short names that collide with policy keys (`build.scope`, `design.reentry`).
  3. **Populations have no tag.** 139 of 140 leg names fail the tag shape, and points, hooks, commands, features, classes, fields and units sit outside R-B's twelve namespaces.
  4. **Renames have no redirect.** The Knowledge redirect is typed prose repeated into every handoff.

## 8. Forks

| Fork | Options | Recommendation |
|---|---|---|
| F1: the `task:title` read keys | migrate to `field.task.title` in dBoundRoles; or keep `:` | migrate, so one separator remains |
| F2: the index | untracked cache keyed by tree id; or tracked and generated with a freshness gate | cache: 0.18 s to rebuild, and no merge conflicts |
| F3: section scope | document-scoped; or globally unique | document-scoped, since 50 tags already repeat across files |
| F4: namespaces | add the nine listed in section 5; or keep twelve and qualify the rest by `kind` | add them |
| F5: frozen positional references | redirect rows only (`BUILD-METHOD M5` → its tag); or rewrite records | redirect rows: P19 freezes records, and they hold 43,935 `§` references |
| F6: "stage" or "step" | one namespace `step`, with the harness stage keys renamed to `field` | `step` |

The probe scripts are in the scratchpad, not the repository:
- `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/proto_index.py`
- `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/slices.py`
- `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/cites.py`
