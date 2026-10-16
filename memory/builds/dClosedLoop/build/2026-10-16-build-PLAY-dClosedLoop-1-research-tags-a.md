# Research: the tag system, run A

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 73's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-22-researcher.md`, which dispatch 74 runs
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`.

---

## 1. Verdict

I recommend **one namespaced grammar, with a derived index**. Tags are spelled `<ns>.<name>`. Section tags are local to their document and cited as `<doc> [name]`. Ids keep memory's own grammar and resolve through the same resolver.

Each tag is declared once, in place, at the site its owning layer already writes: a heading, an item row, a policy schema row, a role file, `gov:feature`. Generated extractors read those sites into an index keyed by the tree id. The index is cached and never committed. The only fact anyone writes by hand is an alias row for a rename or a retirement.

The resolver returns the smallest slice in one call. Both-ways joins reuse `map_lib.compute_coverage`, extracted to `tools/lib`, and they gate.

Measured gains: 1 call instead of 3 to resolve a tag, and a 2.2 KB median slice instead of a 35.9 KB median file. Deriving the whole tree takes 0.90 s.

## 2. Today

| Part | What it does | Measured | Where |
|---|---|---|---|
| Charter rule tags | `- [tag] ` lines under `## 1.` | 46 tags; 22 joined to roles by `rules:` across 10 role files | `AGENTS.md:12`; `roles_lib.py:61-65` |
| `check_rule_tags` | checks a role's `rules:` against section 1; the only tag join that exists | gate leg "roles catalogue" | `roles_lib.py:252-276` |
| `charter [x]` citations in live files | prose citations | 48 citations, 13 distinct, 0 dangling, **no check reads them** | measured below |
| Record section tags | `## [tag] Title`, cited `` record `[tag]` `` | 358 headings in 34 files, all in dClosedLoop; 201 distinct; 50 reused across files (`[words]` ×15); **no resolver anywhere in tools/** | measured below |
| Numbered headings | `## N.`, `§N`, `M\d` | 14,181 `## N.` headings under memory/; the spec template numbers its sections differently per tier | `TEMPLATE-SPEC.md:172-205` vs `:424-599` |
| Hygiene check numbers | 28 numbered checks, append-only | 2,168 live `check N` citations (shared with check-unattended's 70-plus) | `HYGIENE.md:192` |
| Method steps | M1–M12 | 923 live `M\d` hits. M1–M12 were never renumbered in 247 commits (only M4 was retitled). 87 code files use `M\d`, and only 39 of them mention the method | `BUILD-METHOD.md:4-335` |
| Handle registries | `DIRECTIVES_CORE` joins 17 handles to **M-numbers**; `DOD_CORE` has 13 handles | — | `unattended.sh:868,1042` |
| Id grammar | `FAMILY-slug-seq`, minted by hand (grep, then re-roll) | 2,268 distinct ids; 1,219 cited in code. One parser (`grammar_for`) has 8 importers; 62 shell lines spell their own pattern | `extract.py:569`; `HYGIENE.md:168-190` |
| Gap ids | `gap-<area>-NN`, minted by hand | 193 rows; 7 cited ids are unregistered (`gap-obs-01..05` and two probe fixtures) | gap register |
| Map features | `feature = "<name>"` plus `[claims]` joins, both ways, with a shrink-only baseline | 31 features, 10 inventories, 36 baseline lines; **the generic join engine** | `map_lib.py:1404-1432` |
| Gate legs | free-text names used as join keys | 140 legs, 139 not tag-shaped | `gate-legs.json` |
| Lexicon cells | `<lang>.<kind>` → case; verbs | 4 cells, 1 pin, ~25 verbs | `.lexicon.conf` |
| `gov:` markers | `kit` 65, `handoff` 56, `playbook` 21, `block` 1; `gov:note` and `gov:feature` 0 | — | tree-wide |
| Gotchas | kebab slugs, already tag-shaped | 133 | `memory/gotchas/` |

**Design records already settle:** R-B (`layer-instruction` `[recommendations]`): the `<ns>.<name>` spelling, 12 namespaces, selectors vs descriptors, joins armed by their populations, and the lexicon at an extension point. R-I settles the retired-tag forward pointer. `layer-roles` `[tags]` settles `role.*`. `layer-memory` `[annotations]` settles the annotation grammar and `[names]` moves the id parser into memory-tree. dOrderedCharter's row (v2 `[chain]`) owns "the namespaced tag system".

**What they lack:**
- a resolver;
- a slicing rule;
- where the index lives;
- the mint door for each namespace;
- an answer to bare citations;
- namespaces the tree already uses (`feature`, `bug-class`, `leg`, `section`, `ext`, `command`, `pack`);
- the short-name collisions;
- the fact that numbers act as ids.

**Records disagree with code in three places:**
- `check-playbook-parity.sh:14,350` says "v4.0 has no numbered sections". But `AGENTS.md:12,84,98` are `## 1.` to `## 3.`, and `roles_lib.py:61` (`SECTION_ONE_RE`) refuses a charter without them.
- `TEMPLATE-SPEC.md:161` says "§8 must read `none`". §8 is Revision log in Tier-1 (`:205`) and Open questions in Tier-2 (`:553`). The hygiene code keys on titles, not numbers (`check-memory-hygiene.sh:2044,2115`).
- v2 `[open]` says numbered method steps carry CV2's reordering defect. The history shows no reordering. The defect it shows is **overload**: `M12` in `.githooks/pre-push.test.sh:1386` and `M4`/`M5` in `runlog/model.py:414` mean something else.

**Measuring commands (outputs abridged):**
```
$ python scratchpad/tags.py .        # section tags and citations, dClosedLoop/build
files 84 tagged sections 358 distinct tags 201
tags defined in >1 file 50
section bytes median 2204 mean 4048 max 41069; holding-file bytes median 35938
backticked [tag] citations 1438 {'rule-tag': 86, 'unique': 540, 'ambiguous': 788, 'none': 24}
unresolved sample: ['solid','dry','tdd','check','effort','gates','claims','paths','config']
$ git grep -nF '## [' -- tools skills .claude .github | grep -v '\.md:'   # a section-tag resolver?
(only `## [0-9]+[.]` spec-heading readers: check-spec-tokens.py:243,265,310; hygiene :1860-2115)
$ LIVE=...; git grep -hoE '§ ?[0-9]+' -- $LIVE | wc -l      -> 980 live (109 files), 44,078 in records
$ awk '/^## M5 /,/^## M6 /' BUILD-METHOD.md | wc -c -> 1814 of 29326 ; hygiene check 27 -> 1628 of 58542
```

**How an agent resolves a tag today:**
1. ls or Glob for the record.
2. Grep for the tag. Over the whole build folder, `[annotations]` returns 16 hits (5,788 B), only 1 of them a heading.
3. Read with an offset, or read the whole file.

That is **3 calls**. It misses when the cited tag is unqualified (788 of 1,438 citations), when it is a TOML table that looks like a tag (`[claims]`, `[config]`), or when nothing defines it (24). Role agents make 811 method-class reads of whole documents (`layer-roles` `[current]`, record evidence).

## 3. Across the layers

| Layer | Needs from it | Gives it |
|---|---|---|
| instruction | owns the grammar, the namespace table and the resolver; declares the `tag-namespaces` extension point; unit rows carry their tag and scope tags | load by tag: a unit's pointer resolves to a slice; `required-by` joins; R-B's joins armed |
| flow | item and step declarations in the loop kit as declaring sites; leg ids | `<step>.<name>` checked for uniqueness and ownership; `design.tags`; step and item ↔ unit joins |
| roles | role files as `role.*` sites; `rules:` | the load set per role and per item, by selector; the role-by-step matrix derived |
| memory | the id parser and the slicer, moved into memory-tree (`[names]`); `record.<kind>` from the memory contract; `record` renders tagged headings | section-level reads; card pointers by tag; `refs=` and `gov:feature` resolved; recall by tag |
| runtime | `tag` registered as a read-only command adapter; the cache under the git dir; `ext.*`, `command.*` and `pack.*` sites from its registries | extension names checked for shape and uniqueness when a key selects one |
| observability | a detector slot | a frozen-record dangling-citation detector; R-J's "broken" counted by unit tag |
| integrations | adapter rows as sites in its registered namespaces | adapter names validated |
| distribution | `kit.toml` declares its id and layers (`kit.*`); overlays may declare `repo.*` | aliases ship with a kit release, so an adopter's citations survive an upgrade |

| Other system | Needs from it | Gives it |
|---|---|---|
| code annotations | `gov:note <tags>` and `gov:feature <name>` use this grammar; the annotation index is an extractor | resolve and uniqueness checks; slices behind `refs=` |
| instruction writing | headings carry `[tag]` (P11: headings are directives); template slots named by tags | pointer statements resolve; tag-sliced views (R-E) |
| role workflow shapes | item and role declarations as sites | per-item, per-role selection |
| memory structure | the parser, slicer and record-kind declarations in core memory-tree | one-call section reads instead of whole files |

## 4. Candidates

| | Mechanism | Efficiency | Smallest losing test | Result |
|---|---|---|---|---|
| **A. Status quo, extended** | each kind keeps its own parser; numbers act as ids; no shared resolver | 3 calls per resolve; whole-file reads (median 35.9 KB) | do short names collide across kinds, and do bare citations resolve uniquely? | **Loses.** 15 short names sit in 2 or more namespaces, `build.scope` among them as both item and policy; 788 of 1,438 citations are ambiguous; spec §8 differs by tier |
| **B. One authored registry** (`tags.toml`) | every tag is a row; the index is generated from the rows | 1 call; but every tag is authored twice | how many definitions already carry their tag in place, so a row would restate them? | **Loses** on charter [one-fact] and [derive]: 1,236 of 1,236 definitions found already declare in place; 87 of the last 300 commits touch a site, so would also rewrite the one file |
| **C. Derived index from declaring sites** (pick) | per-namespace extractors registered by the owning layer; the index is cached by tree id; aliases are the only authored rows | 1 call; slice median 2.2 KB; full derivation 0.90 s | (1) a kind with no in-place site; (2) derivation over 2 s; (3) a rename stranding frozen citations | **Passes.** All 10 kinds probed have sites. 0.90 s over 64.6 MB. 0 heading renames so far, and R-I's forward-pointer alias covers future ones |
| **D. Grep at call time, no index** | the resolver is a site-grammar grep run per query | 69 ms per query | can a line grep find a definition uniquely? | **Loses.** `build.scope` returns 3 rows (`architecture-v2.md:666,860`, `flow-steps.md:210`) from three table kinds; telling them apart needs a structured parse, which is C |

Federated per-layer resolvers would differ from C only in where the union of all tags is built. The joins and the uniqueness checks need that union anyway, so I stopped there.

```
$ python scratchpad/scan.py .
scan 0.90s over 64598823 memory bytes; 1236 definitions
item defs=120 distinct=110 | policy defs=348 distinct=164 | leg 140, not-tag-shaped=139 | kit 38, 4 not shaped
short names in 2+ namespaces: {'roles':['feature','kit','practice'], ...10 kit/feature pairs...,
 'design.reentry':['item','policy'],'build.scope':['item','policy'],'maintain.record':[...],'distribution.install':[...]}
keys whose first segment is a namespace word: ['policy.guard','policy.proof','policy.on-missing-expansion']
$ for c in $(git rev-list --no-merges -n 300 HEAD); ... -> 87 of 300 recent non-merge commits change a tag definition site
$ git grep one tag over memory/: 69 ms ;  cached index load+lookup 0.3 ms; index bytes 43500 (synthetic 1,300 rows)
$ git grep -hE '^\| `build.scope` \|' -- memory | wc -l  -> 3
```

## 5. The pick, specified

**Grammar.**
```
tag     := ns "." seg ("." seg)*        seg := [a-z0-9][a-z0-9-]*   (roles_lib.py:65)   ≤ 64 B
short   := seg ("." seg)*               only where a context fixes ns (checklist, policy.toml, rules:, heading)
section := doc-ref " [" seg "]"         doc-local; doc-ref = doc.<name> | record name | id
id      := memory's grammar (FAMILY-slug-seq, gap-<area>-NN, fork letters); minted by `record`, never aliased
```
- A first segment may not be a namespace word. Three policy keys fail this today; they do not ship yet, so renaming them is free.
- A bare `[seg]` resolves only to a charter practice, under `tags.bare-refs`.

**Namespace table.** It is one TOML in the playbook kit, with columns ns, owner layer, class (selector, descriptor or anchor), declaring site, door and extractor:
- R-B's 12 namespaces;
- `section` and `doc` (instruction);
- `feature` and `bug-class` (memory);
- `leg` and `check` (flow);
- `ext`, `command` and `pack` (runtime).

Expansions and optional components add rows at the instruction layer's `tag-namespaces` point, such as `lex.*` and `detector.*`.

**Minting, renaming and retiring.**
- A tag is minted by writing its site through its namespace's door: the instruction command for units, the loop kit for items, the policy schema for keys, the memory contract for record kinds, `record` for ids and record headings.
- Renaming or retiring a tag appends an alias row beside that source: `retired <tag> → <tag>|none <date>`. A retired name is never reused (R-I).
- Two layers cannot mint one tag. An extractor may emit only into namespaces its layer owns, and full spellings are unique across the index.

**Index.** It is derived JSON at `<git-dir>/gov/tags/<tree-oid>.json`, with one row per tag: full name, ns, path, line, byte range, blob SHA, state, forward pointer and owner. It is rebuilt whenever its key misses (P23) and never committed.

**Resolver.** `tag show|where|refs|check <ref>` returns the smallest slice:
- a section, from its heading to the next heading at the same or a higher level, by `extract_records`' rule (`extract.py:606-615`);
- an item or key row, with its header;
- a rule line;
- a policy key's schema row and its current value;
- an id's anchored record.

**Kits.**
- The slicer moves to memory-tree with the id parser.
- `compute_coverage` is extracted to `tools/lib` as the join factory. This is its second instance, and the map is optional, so core cannot import it from there.
- The command and its checks live in playbook.
- The owner is the instruction layer, built by dOrderedCharter. dDeclaredLoop, dBoundRoles and dTotalRecall each register their own namespaces.

**Checks (gates; they soften under `instructions.checks`, never skip).**

| Check | Red case |
|---|---|
| T1 shape | a leg tagged `template size <=48KiB`; `policy.policy.guard` |
| T2 unique | a second `plan.input` row in the loop kit |
| T3 owned | a lexicon pack emitting `role.x` |
| T4 resolve (live files) | a planted `charter [nope]` in `memory/guides`; a bare `` `[claims]` `` |
| T5 retired | a retired name re-minted |
| T6 joins (R-B; roles `[tags]`; annotations) | a role with no unit; reports "unarmed" while its population is empty |
| T7 cost | the leg running over 2 s on gov's tree |

Citations in frozen records are reported only, by the observability detector.

**Read-path cost.**
- 1 call per resolve.
- About the slice size plus 150 B: a 2,204 B median section instead of a 35,938 B median file (17.4×). M5 is 1,814 B instead of 29,326 B; hygiene check 27 is 1,628 B instead of 58,542 B.
- The five protocol pointers fall from 212,986 B of whole documents to their slices.

## 6. Items and policies

| Item | Actor | Needs | Does | Witness | Routes |
|---|---|---|---|---|---|
| `design.tags` (new) | command | `design.decompose` | derives the tags the spec set declares; runs T1–T3 and T5 against the base tree's index | the tag-check record keyed by tree id | clean → `design.ready`; collision → that unit's spec writer |
| `build.core` (filled) | executor | as declared | T1–T6 join the core checks | the executor-written result | as declared |
| `entry.orient` (filled) | orientation scout | as declared | the card's pointers carry tags (`card.pointers`), resolved by the scout | the card's keys | as declared |
| the work-order render (filled; dBoundRoles) | command | the item | selects units by role, item and step tags | the render's loaded-unit record (R-J) | over budget → refused |

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `tags.bare-refs` | `charter-only`, `unique`, `never` | `charter-only` | 86 bare citations of rule tags resolve at level 0; 788 bare section citations do not |

Strictness is not a new key. It reuses `instructions.checks` (one fact in one place).

## 7. Gaps

**Closed, by id:**
- **gap-found-09**: the joins and the registry.
- **gap-roles-12**: whole-document pointers become slices.
- **Part of gap-mem-06**: every reader goes through one parser through the resolver.
- **Part of gap-mem-08**: the grammar and the resolve check.
- **Part of gap-found-12**: the slicer that tag-sliced views need.

**New, proposed for registration:**

| Proposed id | Owner | Evidence |
|---|---|---|
| gap-found-20 | dOrderedCharter | No section-tag resolver or citation check exists (1,438 citations; 788 ambiguous; 24 resolve nowhere; 48 live `charter [x]` citations unchecked). `## 1.` is still load-bearing (`roles_lib.py:61`), while `check-playbook-parity.sh:14` says it is gone |
| gap-found-21 | dOrderedCharter | R-B's namespace list lacks `feature`, `bug-class`, `leg`, `section`, `ext`, `command` and `pack`. 4 item/policy spellings collide, and `flow-steps.md:210` cites `build.scope` (the policy) inside the `build.scope` item's own row. 3 keys start with `policy.` |
| gap-design-10 | dIndexedDesign | Spec section numbers vary by tier: `TEMPLATE-SPEC.md:161` vs `:205` and `:553` |
| gap-test-14 | dWitnessedBar | 139 of 140 legs are named in free text and used as join keys in 31 dossiers' claims |
| gap-tool-08 | dConvergedCharter | `M\d` is overloaded: 48 of 87 code files use it for something other than the method; `DIRECTIVES_CORE` keys on M-numbers (`unattended.sh:1042`) |

## 8. Forks

| Fork | Options | Recommendation |
|---|---|---|
| T-1 Bare `[name]` citations | charter practices only; any unique name; never | **charter-only**: practices are level 0, and a bare section citation is ambiguous 55% of the time |
| T-2 Numbered ids (M-steps, hygiene checks, R, V and S rules) | name tags, with the numbers kept as alias rows and live citations migrated by Convergence; rewrite every citation now; keep the numbers as ids | **alias, then migrate the live files.** The numbers were never renumbered; their defect is overload. Spec §N migrates in every option, because it is truly positional |
| T-3 Where the index lives | cache keyed by tree id; a committed generated file | **cache**: 29% of commits would rewrite a committed file |
| T-4 Gate-leg keys | a `leg.<slug>` id with the name kept for display; free-text names | **ids**: a renamed display name stops breaking claims |
| T-5 The namespace word for steps | `step`, with kit.toml's `stage = N` renamed to regen order (`regen.py:191`); `stage` | **`step`**: the flow records and R-B already use it, and `stage` already means regeneration order |
| T-6 Policy keys under `policy.` | rename the 3 keys; allow the doubled spelling | **rename**: nothing ships them yet |

The probe scripts are in the session scratchpad, `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\` (`tags.py`, `scan.py`, `coll.py`). Nothing was written to the repository.
