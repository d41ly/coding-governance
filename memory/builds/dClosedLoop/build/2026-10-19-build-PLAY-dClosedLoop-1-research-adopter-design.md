# Research: what the converged design decides about an adopter's own instructions, and what it leaves open

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 119's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-2-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md`.

---

The design decides who may write adopter instructions and that the repository's rules render in their own block. It does not decide how an adopter's own unit relates to a gov unit it changes, and a working mechanism needs a few additions. My pick is the adopter's own units carrying typed `supersedes` and `amends` edges, a pin on the version of the gov unit they change, and gov's upgrade steps moving those edges when gov renames or splits a unit. Everything below was checked by reading the records, and the current-code points against the tree. I wrote nothing.

Record keys: **v2** = architecture-v2, **LI** = layer-instruction, **SYS** = systems, **MP** = memory-plan, **RF** = retrofit, **FD** = foundations, **WT** = walkthrough (holds CV1), **DR** = design-rounds, **LR** = layer-roles, **FT** = fates, **LE** = layer-expansions. All sit in `memory/builds/dClosedLoop/build/`.

## Decided

**Adopter-authored instruction kinds**

| Kind | Where it is stored | How it renders and ranks | Owning build |
|---|---|---|---|
| Project block | the repository's "own overlay" | after the preset and overrides, inside the level-0 charter, "gov's included" (v2 [front-door] 857-858; v2 [principles] P8; WT CV1). MP [pockets] row 64 says `.governance/deploy.toml`, "units at level 0" | dOrderedCharter (v2 [chain]); gap-found-19 is the gap (LE 509) |
| Adopter's own units in general | `.governance/instructions.toml`, "merged by row key" (SYS [design-instruction-writing] 347-348). The owner field is "its owning kit, or the repository for an adopter's own unit" (LI [recommendations] R-A). "A repository registers its own documents onto [the ladder]" (FD settled step 1) | by level and scope tags, like any unit (v2 P13) | dOrderedCharter |
| Repo-declared practices | not stated | allowed in `charter.practices`, which presets never touch (v2 [policies] 896, v2 [presets] 1136-1137; FD R1 "an adopter may declare its own"). Reach renders as step-scoped units in work orders (SYS [answers] IW-2) | dOrderedCharter |
| Repo-declared presets | the policy file | each must extend a shipped preset and pass the same completeness check (v2 [presets] 1149-1150; v2 [policies] 894) | dKeptSession |
| Policy values and overrides | `.governance/policy.toml` | rendered as level-2 units inside the charter, preset name plus the keys that differ (v2 [presets] 1125-1127; v2 [front-door] ladder) | dGroundRules (file, schema, reader); dKeptSession (preset render) |
| Promoted units: reuse entries and directives from memory | `memory/map/conventions/` and manifest parts beside features | level 3, carrying a `promoted-from` edge written by `instructions.edit` (MP [pockets] row 72, MP [edges] 191; v2 [chain] dLinkedLibrary; SYS [answers] MS-1) | dLinkedLibrary; the edge is dOrderedCharter's |
| Recorded overrides | an override record | a live event only. The charter wins unless the owner overrides "in so many words", and a standing override "becomes a charter amendment rather than a habit" (FD settled step 1; v2 [policies] 895) | dOrderedCharter |
| Per-role house overlays | `tools/roles/house/<role>.md`, seeded once and never rewritten | appended as `## House rules` (LR 476-479, R3-A) | dBoundRoles |
| Packs | not stated | instruction packs extend `charter.practices` into a preset catalogue (LI R-I 581; v2 [chain] dOrderedCharter) | dOrderedCharter |

**Operations and safeguards already decided**
- **Who may write.** `instructions.edit` (default owner-command-agents-propose) and `instructions.proof` (default tty-cli). Presets never touch either (v2 [policies] 978-979; LI [settled]).
- **What one command does.** It adds, edits, removes, lists, renders and checks units. The same checks run as a gate leg and at every render, including over "an overlay edit or a kit install" (LI R-I 553, 560-568).
- **Principles are fixed** and change only by an owner-ratified amendment (FD K2, C6; v2 P16; LI R-I 579).
- **Adding a unit:** decided in principle (the project block plus R-A's owner value "the repository").
- **Disabling a practice:** decided, by removing it from `charter.practices`.
- **Parameterizing:** decided for catalogue keys. A unit can render a value read from the policy file (SYS 349: `source` derived), and the adopter overrides the key.
- **Ordering:** a conflict resolves "by level, never by load order", and tags survive reordering (v2 P11, P13). Order inside a document is fixed by its template (SYS [design-instruction-writing] "Templates").
- **Hand edits to rendered files are refused.** The render gate reds any instruction-path file whose bytes differ from its render (SYS [design-instruction-writing] "The renderer and its gate"; armed at dOrderedCharter, IW-1).
- **Policy overrides survive gov updates.** The step gate covers policy keys and conf keys (v2 [chain] dSafePassage), and the legacy homes are the translation window's population (v2 P38).
- **Gov renaming or retiring a tag** writes `retired → <new>` or `→ none`. The redirect is derived and a retired name is never reused (SYS [design-tags] 250; MP [practice] 138). New text citing a retired tag reds (SYS 271; `tags.retired-cites`).
- **Edited kit files on update:** three-way merged, seeds never rewritten, and an edited retired file kept as `retired-edited` with an order (v2 [catalogue] `install.retired-edits` 1113; v2 [chain] dSafePassage).

**What the registry says about gov's units versus the repository's (point 4)**
- `source` does not mean provenance. It means "written text or rendered from a structured definition" (LI R-A; SYS 349). Gov's units are told from the repository's by "owning kit, or the repository" (LI R-A).
- The registry's unit list carries "source, owning kit" (v2 [chain] dOrderedCharter).
- A unit row can carry `edges` in the shared grammar (MP [sites] 149). `supersedes` and `amends` are node-to-node edges declared at the new or amending node (MP [edges] 176-177). So a reference to the gov unit being changed is expressible. Nothing gives it render meaning.

**Adopting a repository that already has instructions (point 5)**
- The repository's instruction files are seeded onto IW-1's shrink-only legacy list. They migrate "per step", and the owner "retires its own documents" (RF [cross] 158-159; RF [practices] 481).
- `adopt.census` counts the repository's practices: lint configs, CI jobs, decision-shaped documents, CODEOWNERS and comment conventions (RF [seed] 347-348).
- `adopt.practices` asks the owner once per practice: import, translate, keep alongside or retire. Until a ruling the practice stays alongside (`retrofit.practice-pending`) (RF 357-359, 552).
- `adopt.decisions` routes decision candidates through two raters, and `adopt.reconstruct` follows `retrofit.reconstruct`. Neither turns instruction text into units (RF 360-368).
- Nothing is rewritten without the owner's ask (RF [never]).

## Undecided

- **ADD (partly):**
  - The home has two answers (contradiction 1).
  - No tag namespace exists for the repository's own units. The namespace list in SYS [design-tags] and LI R-B has none, and the `owned` check reds a part declaring outside its own namespace (SYS 269).
  - Nothing says whether the project block may hold units below level 0, though FD lets a repository register documents at any level.
- **AMEND a gov unit's text:** nothing decides it.
  - R-I's "Manifests merge deterministically with the adopter's overlay" (LI 551) names no precedence.
  - `amends` has no render rule (MP [edges] 177).
  - Editing an installed `tools/<kit>/instructions.toml` would fall to govkit's file-level three-way merge, and nothing decides whether that file is an engine file or a guarded manifest (v2 [chain] dGroundRules minimal guard names "the instruction manifest", singular).
- **REPLACE:** undecided.
  - "merged by row key" (SYS 348) suggests a same-tag row wins, but the `unique` check reds "a second `plan.input` row" (SYS 268).
  - "One fact in one unit" reds two active units with one subject (SYS 374).
  - `supersedes` has no render rule.
- **DISABLE or EXCLUDE a non-practice unit:** undecided.
  - Only `charter.practices` selects.
  - Exclusion is limited by the `required-by` joins (LI R-B, R-C) and by K2 for principles.
  - No row shape for a pure exclusion fits P11's six statement types.
- **REORDER or re-rank** (move a gov unit to another level): undecided. Order within a template is not adopter-settable and has no stated use.
- **PARAMETERIZE with adopter-defined values:** undecided. "A new key cannot land without a value in every shipped preset" (v2 [presets] 1128-1130) leaves no stated route for a key the repository defines.
- **SURVIVE a gov update:**
  - *Reword:* a content-only edit "needing none" passes the step gate (v2 dSafePassage). No pin detects that a gov unit an adopter changed has moved since. `pinned-at` allows only record, probe or claim as its source (MP 188), and an off-namespace edge reds (MP 194).
  - *Rename:* the redirect is derived (SYS 250), but nothing re-points an adopter edge to it automatically.
  - *Split:* `retired → <new>` has a single target, so a split is undefined.
  - *Retire:* detected by `retired` and `resolves`, and nothing orders a fix.
  - *Add:* a new gov unit can collide with an adopter unit under R-I's "conflicts at the same level", which refuses with no resolution route.
  - Instruction units and tags are not named in the step gate's surface population, which joins "each later class … when its owning build lands it" (v2 [chain] dSafePassage).
- **Project block ranking:** CV1's "charter is the foundation" is not expressed by level. The block sits at level 0 beside gov's practices (v2 [front-door]; MP row 64), so a conflict between them is refused rather than ranked.
- **Turning an existing AGENTS.md into the project block:** undecided. The adopter's AGENTS.md is the path gov renders the charter to, so it cannot sit on the legacy list and be rendered at once. No `adopt.*` step turns its prose into units (RF 481 says only "migration per step").

## Contradictions

1. **Two homes for the adopter's rules.**
   - SYS [design-instruction-writing] 347-348 puts them in `.governance/instructions.toml`.
   - MP [pockets] row 64 puts them in `.governance/deploy.toml`: "the repository's answers and adopter rules, rendered into the charter … units at level 0".
   - v2 dGroundRules's minimal guard lists both "the instruction manifest" and `.governance/deploy.toml`.
2. **"Merged by row key" (SYS 348) versus the `unique` check (SYS 268) and R-I's same-level conflict check (LI 567).**
   - Research B says the driver extends `merge-rows.py` (research-instruction-writing-b 118).
   - The code shows `merge-rows.py` is a cross-branch three-way git driver for one file (`tools/memory-tree/merge-rows.py:6`), not a rule for which row wins between gov's manifest and the adopter's overlay. Record and code disagree on what the seam can carry.
3. **The owning-kit field.** LI R-A and v2 dOrderedCharter list "owning kit". SYS 348-349's field list has no owner or kit field, though research-instruction-writing-a 108-125 had `kit = "playbook"`. MP [practice] 137's `one-owner` asks for "owning build or layer", which has no value for an adopter's unit.
4. **Gov's own rules (P8).**
   - DR R1.1 says gov-only rules leave the shipped charter, and WT CV1 plus WT's Convergence unit 1 say "rules that govern only gov move to gov's overlay".
   - That clause was in v1 (`v1 [chain]` 142) and in v2's first dConvergedCharter row ("regrouped … with every adopter's overlay, gov's included").
   - Commit `aa0d778b1` moved the block render to dOrderedCharter and dropped the move-out. No v2 row now separates gov-only practices from the shipped default set.
   - That default is "the governance foundation set" (v2 896), which FD calls "gov's governance rules".
5. **Role house overlays.** LR R3-A keeps adopter-owned house overlays as seeds inside the kit home. FT row 79 marks `house/*.md` RESHAPED into core roles. Research-distribution-a 75 and 197 say overlays live outside kit homes. The unit model would carry role rules as overlay units with `select=role.*`. That is three answers.
6. **`install.retired-edits` owner.** The v2 revision note at 548 says it "moves to dShippedRelease". v2's catalogue row at 1113 says dSafePassage (SA-2).

## Candidates

| # | Mechanism | Smallest losing test | Result |
|---|---|---|---|
| A | Project block only: append-only adopter units in their own tags; gov units changed only through `charter.practices` and live overrides | Can it express AMEND or REPLACE of a gov unit without a refused conflict? | **LOSES.** A contradicting adopter unit sits at level 0 beside gov's practices, and R-I's same-level conflict check refuses it (LI 567; MP row 64). The owner's ask explicitly includes "adjusting existing ones". |
| B | Same-tag shadowing: an overlay row with gov's tag replaces gov's row ("merged by row key") | (1) Does the `unique` check pass? (2) Is a gov reword of a shadowed unit visible? | **LOSES on both.** The `unique` check reds a second row with the same tag (SYS 268). A shadow carries no base, so a gov reword is invisible, which fails supersession's "no adopter edit is lost silently" (research-supersession 121). |
| C | Edit gov's kit manifests in place; govkit three-way merges them on update | Does the edit render from the repository's own overlay as a separate block, and does gov's own edit stay out of what it ships? | **LOSES.** P8 and CV1 require the repository's own overlay, and overlays live outside kit homes (distribution-a 75, 197). In gov's tree a kit-manifest edit is the shipped default, which breaks gov-as-adopter. |
| D | Adopter units with their own tags in one overlay manifest, each change typed by `supersedes=` or `amends=` to the gov unit, pinned to that unit's text hash or change-record id; the renderer applies them before the one-fact and conflict checks | (1) Can a unit row carry these edges? (2) Do the tag checks pass? (3) Can it pin the base? | **Survives (1) and (2), loses (3) as written.** Rows carry `edges` (MP 149) and both types are node-to-node (MP 176-177). The tag is the adopter's own, so `unique` passes. `pinned-at` admits only record, probe or claim as source, and an off-namespace source reds (MP 188, 194), so the pin needs `pinned-at` widened to `unit`, as `decides` and `after` were widened. K2 needs a check that reds `supersedes` or `amends` on a principle unit. |
| E | Upgrade-step kind: gov ships `[[upgrade]]` steps that re-point adopter overlay edges when it renames, splits or retires units | (1) Does it express ADD or AMEND alone? (2) Does a unit rename red the step gate today? | **Loses as a standalone design:** it expresses no operation. **Survives as the survival half:** the step gate's population joins "each later class … when its owning build lands it", and dOrderedCharter is dSafePassage's child (v2 [chain]), so it can join unit tags. Not joined today. |
| F | `charter.override` records as standing adopter changes | Is an override standing? | **LOSES.** "A standing override becomes a charter amendment rather than a habit" (FD settled). |
| G | Policy-valued units (`source` from a policy key) for PARAMETERIZE | Can an adopter add a key? | **Passes for catalogue keys, loses for adopter keys.** Completeness requires a value in every shipped preset (v2 1128-1130). |

## Pick

D for expressing changes, with E for surviving updates, G for values, and `charter.practices` for practice selection. In detail:
- **One home:** a single adopter overlay manifest. This settles contradiction 1 and absorbs the house overlays (contradiction 5).
- **Ownership:** each row carries its owner as "the repository". This settles contradiction 3, and gov's own overlay is the same thing.
- **Changing a gov unit:** a gov unit is changed only through a unit with its own tag and a `supersedes` or `amends` edge, pinned to the target's base.
- **Survival on update:**
  - A moved base makes a stale amendment, which becomes an owner order, the same pattern as `retired-edited`.
  - Gov's `retired → <new>` redirects re-point the edges automatically.
  - Splits and retirements ship `[[upgrade]]` steps or orders.
  - Unit tags join the step gate's surface population.

**Still undecided under the pick:**
- the tag namespace for repository units;
- whether an amending unit may change the target's level or `select` (re-rank);
- how a pure exclusion is typed under P11's six types, and how it squares with `required-by`;
- what a split's `retired → a,b` means;
- a route for repository-defined policy keys;
- whether the project block's foundation-first ranking is a level or a check;
- which of today's 36 practices are gov-only and leave the shipped foundation set. That unit was lost at `aa0d778b1`, and the owner needs to re-home it.
- the `adopt.*` step that turns an adopter's existing AGENTS.md or CLAUDE.md prose into project-block units.

Files cited:
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-16-build-PLAY-dClosedLoop-1-systems.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-foundations.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-18-build-PLAY-dClosedLoop-1-fates.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-architecture-v1.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\.governance\deploy.toml`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\memory-tree\merge-rows.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\roles\kit.toml`
