# Research: flow and roles adoption, the converged design

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 124's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-6-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md`.

---

I wrote nothing in the repository. Every probe was a read: the records, `tools/govkit/govkit.py`, `tools/run-gates/`, `tools/roles/`, `tools/hooks/agent-cap.js` and `tools/workflows/tier2-review.js`, plus one python count over `tools/gate-legs.json` and the kits' `kit.toml` files.

**Record keys** (all in `memory/builds/dClosedLoop/build/`): v2 = architecture-v2 · FS = flow-steps · LF = layer-flow · LR = layer-roles · LRT = layer-runtime · LE = layer-expansions · SYS = systems · LI = layer-instruction · RS = review-system · RF = retrofit · FD = foundations · LX = lexicon · FT = fates · NP = night-pass · AI = adopter-instructions · WT = walkthrough · MP = memory-plan.

## Decided

**What a repository can already add**

| Part | Where it is stored | How it is registered and checked | Owner | Core or expansion |
|---|---|---|---|---|
| A **step** | nowhere: an adopter cannot add one | A build passes five fixed steps (v2 [principles] P20), principles change only by an owner-ratified amendment (FD [core] K2, C6), and cadence programs attach only at Runtime's cadence-item point (LRT [extend]; LE [core-points]). No record speaks of an adopter's own step. The "own steps" of DR R1.2 are product-deploy steps, not flow steps. | dDeclaredLoop | core is fixed; cadence steps are expansion |
| A **breakpoint** | `review.breakpoints`, a set of item boundaries in `.governance/policy.toml` | placed by policy, one mechanism with `review.<stage>` and `autonomy` (v2 [policies]; FS [breakpoint]; LF [settled]) | dDeclaredLoop | core |
| A **probe point** | `probe.points`, in `review.breakpoints`' grammar | v2 [policies]; FS [probe] | dPlacedRequest | core |
| A **lens** | only swaps from a shipped catalogue, by `review.opt-in` | checked once at the argument boundary (RS [lenses]). A new lens needs "an edit to the harness's literal catalogue" (RS [lenses]; FS [breakpoint] extension points). | dFairHearing | core harness |
| A **role** | expansion roles only, through their layer contract | the core roster never names them (LR [roster]; v2 [chain] dBoundRoles). The matrix arms red an undeclared actor, and red an expansion role in a core item (LR [matrix]). | dBoundRoles registers; dShippedRelease and dTendedCadence define | expansion |
| A **role's prose** | the house files become level-5 units in `.governance/instructions.toml`, each selecting its role | v2 [chain] dBoundRoles, last clause (IA-1); FT [table] row 80 | dBoundRoles | core |
| A **role's effort** | `tools/roles/house/policy.toml`, seeded to the adopter and never rewritten (`tools/roles/kit.toml:31-40`) | on dGroundRules' legacy list until dConvergedCharter folds it into the policy file (v2 [policies]; FT row 89) | dBoundRoles, then dConvergedCharter | core |
| A **workflow shape** | none for a repository | the registry is gov's `tools/roles/workflows.toml` (SYS [design-role-shapes]); a factory and gate for workflows exist (v2 [chain] dDeclaredLoop) | dBoundRoles | core |
| A **gate leg or pack** | (a) product tests by `tests.product`, with runner adapters (WT T4; FS [test]); (b) CI test jobs imported as legs through an integrations adapter row with a grant, and a deploy job refused (RF [seed], [practices]; v2 dShippedRelease); (c) packs at Test's leg-pack point (FS [test]; LF F-F) | today the code keeps an adopter's own rows by name in its runner manifest (govkit.py:4143-4159) | dWitnessedBar; dShippedRelease for imports | core point; imports are expansion |
| A **lexicon pack** | the repository's lexicon declaration, changed through the instruction write path, in the shipped packs' shape | LX [forks] L-5, settled | dMindYourWords | optional component |
| A **preset** | the policy file; each must extend a shipped preset | the same completeness check as shipped presets (v2 [presets]) | dKeptSession | core |
| A **playbook** | the `playbook` record kind, amended by proposal | followed through the `repeat` disposition; its set check registers at Test's leg-pack point (v2 dIndexedDesign; NP [p1-unattended] 6; FS [transitions]) | dIndexedDesign | core |
| A **policy value** | overrides on a preset in `.governance/policy.toml`. The repository's own keys live under `repo.` and are read only by its own units. | schema and reader (v2 [policies]; v2 dGroundRules; AI [design] 7) | dGroundRules | core |
| A **practice** | `charter.practices` takes catalogue or repo-declared practices | v2 [policies]; FD R1 | dOrderedCharter | core |
| **Environments and fixes** | `release.environments` and `maintain.fixes` take registered names only | LRT [extend]; v2 [policies] | dShippedRelease, dTendedCadence | expansion |

**What each operation on gov's flow and roles already has**
- **ADD an item, route or transition row:** nothing gives a repository this. A new step, role or rule is a "filled contract" for a layer only (LRT [extend]). The `owned` check reds "an expansion declaring `item.build.x`" (SYS [design-tags]).
- **AMEND:** only role prose, through IA's `amends` edge on the role's level-5 units (AI [design] 4). For a leg, the code today keeps an adopter-changed ceiling, and reports a hand-edited argv, guard or `doc_reads` on a gov row as drift and withholds that leg (govkit.py:4231-4248). No record carries this keep rule.
- **DISABLE:** only what a key selects: lens swaps, breakpoints, `maintain.fixes`, held legs.
- **REORDER:** a step's order is fixed by P20. Items are ordered by `Needs`, and "numbers are display order only" (FS [rules]; v2 dDeclaredLoop).
- **PARAMETERIZE:** catalogue keys, presets, and `repo.` keys (v2 [policies]; AI [design] 7).
- **SURVIVE:** the step gate covers policy keys, agents, commands and gov's instruction-unit tags, with "each later class … joining when its owning build lands it" (v2 dSafePassage). Retired tags redirect (SYS [design-tags]).

**What gov's tools parse, and so belongs in a fixed set**
- **The flow's frame:** the five steps (P20); the terminal set (FS [transitions]); the closed disposition set (LF [settled]); the engine's answer set: act, awaiting, blocked, terminal, stuck, invalid-input, stale-remote (v2 dDeclaredLoop).
- **The item schema:** tag, actor, needs, allowance, return template, closed outcome set with `probe`, witness and routes (FS [rules]).
- **The actor kinds:** registered only at Runtime's point (LRT [extend]).
- **The witness rules:** the floor's "no stage witness reads actor-typed state" (v2 [floor]), and items whose witness is runner- or hook-written (`test.verdict`, `entry.intake`).
- **The two programs:** the breakpoint program's items and the probe program's items (FS [breakpoint], [probe]).
- **The roster arms:** the matrix arms (LR [matrix]) and the twelve core roles (LR [roster]).
- **Role limits:** each role's allowance ceiling, tools, write classes, gate legs and return template, each limit paired with its enforcer (v2 dBoundRoles). The shape's agent cap, bounded by `FANOUT_CAP`.
- **The lens literal:** at most five slots, which `agent-cap.js:497` counts (`MAX_LENSES = 5`).
- **The leg manifest's key set:** pinned, and checked by the run-gates canary leg (govkit.py:4165-4170).
- **The loop's contracts:** IA's fixed set already names them (AI [design] 8).

**Gov as its own adopter**
- 91 of gov's 140 manifest legs are declared by no kit's `[[gate_leg]]`, and 64 are kit self-tests (`subject = "kit"`). Gov ships only the 49 legs that `kit.toml` files declare, so the manifest is already gov-only beyond those 49.
- The seeded efforts in `house/policy.toml` are gov's owner rulings (builder `xhigh`, from commit `175f86981`). Every adopter receives them once.
- Gov's house files are 0 bytes, so nothing gov-only travels there.
- IA-6's census covers practices only (AI [design] 16).

## Undecided

- **ADD an item, transition row or role acting in a core item.** No core point adds an item inside a step: LF F-F lists seams, leg packs, release, detectors and notifications only. Neither tag spelling works:
  - `item.<step>.x` reds `owned`;
  - `repo.x` leaves the `item` namespace, so the item join and the programs never see it (LI R-B).
  - The matrix arm refuses any role that is not a declared core role (LR [matrix]).
  - FD C3's closed set of extension kinds names no `item`, `transition`, `lens` or `shape` kind.
  - No owner value exists for a repository's item: the owner check wants exactly one chain build per node (v2 revision PM-8, PM-10).
- **ADD a leg after the manifest becomes generated.** "One manifest whose rows the leg factory generates from the packs' declarations" (FT [stale] 7, row 169) gives an adopter's own hand-written row, which the code keeps today, no source.
- **ADD a lens.** It is possible only by editing `tier2-review.js` (RS [lenses]), an engine file that an update overwrites or merges.
- **AMEND, REPLACE or DISABLE a gov item, route, transition row, leg or shape, and a role's structured fields.**
  - LI R-I says "a rendered unit changes at its structured source", and the sources live in kits (`tools/loop/`: WT S1b; `workflows.toml`; the legs manifest).
  - No overlay home exists for structured sources: MP [pockets] has none for the loop definition, the legs or the shapes.
  - `instructions.exclude` takes unit tags only.
- **REORDER an item's `Needs`.** Undecided, the same as AMEND.
- **PARAMETERIZE a role's effort and its gate grants after the fold.** v2 [policies] folds `house/policy.toml`'s `[effort]` and `[gates]` into the policy file, but the catalogue has only `review.<stage>.effort`. No key receives `[effort.roles]`, `[effort.stages.*]` or `[gates]`. A role's model has no key either (LR R3-A lists "its model").
- **SURVIVE a gov change to an item, leg, role, shape or transition row.**
  - The step gate does not name item, leg, role, shape or transition-row tags. It names unit tags, agents and policy keys only.
  - No editorial or semantic change record exists for structured rows. Those marks belong to `instructions.edit`'s units (AI [design] 9).
  - A policy value that names a gov boundary (`review.breakpoints`, `probe.points`) is not re-pointed by any record on a rename.
  - A seeded file never receives gov's change. RS-2's lowered efforts (SYS [answers]) cannot reach an adopter through the seed.
- **Gov-only flow and role settings.** No census rules on gov's 91 kit-less legs, now that the manifest is to be generated from packs, nor on the seeded efforts.

## Contradictions

1. **Two homes for `[gates]`.** v2 [policies] 896 and FT row 89 put it in `.governance/policy.toml`, which has no key for it. v2 dBoundRoles puts "a ceiling of … gate legs" in each role's definition.
2. **Efforts, record against code.** SYS [design-role-shapes] and v2 dBoundRoles set the orientation scout to medium and the builder to high (RS-2). `tools/roles/house/policy.toml` holds `xhigh` for both, as a seed that update never rewrites.
3. **How a lens is registered.** LR [roster] says an expansion "registers its roles and lenses through its layer contract", and LRT [extend] says a filled contract adds no code. RS [lenses] redefines registering a lens as a catalogue entry plus an edit to the harness literal.
4. **The leg manifest, record against code.** FT [stale] 7 makes it generated from packs. govkit keeps an adopter's own hand-written rows in the same file and refuses to overwrite them (govkit.py:4143-4159).
5. **House files, stale record.** LR R3-A still calls them seeds in the kit home rendered as `## House rules`. IA-1, v2 dBoundRoles and FT row 80 move them to the overlay.
6. **Who owns overlays.** v2 [layers] lists "overlays" under distribution, an expansion. dOrderedCharter, in the core, owns the overlay, and research-distribution-a:67 reads it as "distribution seeds, the core renders". A structured overlay would have to follow the same reading, since the core position engine must read it.

## Candidates

| # | Mechanism | Smallest losing test | Result |
|---|---|---|---|
| A | IA's text edges applied as they stand: `amends` renders after gov's row, `supersedes` in its place, and a stale pin renders both | (1) Does an `amends` on `item.build.scope` change position? (2) Does "render both" pass on a row? | **LOSES.** (1) Position is "a pure function of the declaration, the witnesses and the policy" (LRT [invariants]), and a render is none of them. (2) Two rows under one tag red `unique` ("a second `plan.input` row", SYS [design-tags]). It holds only for role prose, which is already decided. |
| B | Edit the kit's structured files in place, and three-way merge them at update | Does the edit survive gov touching the same row, and stay out of what gov ships? | **LOSES.** The kit is held back and rolled back (AI [today], measured by dispatch 118). In gov's tree the edit becomes the shipped default, which breaks P8. |
| C | **A repository pack in the shipped schema.** Repository rows (items, transition rows, legs, shapes, role fields) sit in a guarded overlay beside `instructions.toml`, owned by `repo`. A change to a gov row is a field-level patch pinned `<tag>@<hash>` of gov's canonical row, plus whole-row replace and an exclude list. The merge is read at the landed revision, and every existing check runs on the merged declaration. | (1) Does a repository item pass `owned` and the item join? (2) Is a patch that swaps `test.verdict`'s actor refused? (3) Does excluding `design.seams` red? (4) Do a rename and a semantic change survive? | **(1) Loses as written.** It needs a decided spelling: `repo` admitted as an owner under `item.<step>.*`, as IA admitted it for units. **(2) Passes**, if checks run after the merge: the floor's witness rule and FS [rules] catch it. **(3) Passes, with a refusal naming who needs it:** the reuse scout acts in no core item and the matrix arm reds, and `Needs` strand under the `gap-flow-15` join. **(4) Passes only if** the step gate joins item, leg and role tags, and the stale rule becomes "hold the patch, run gov's row, file an order", since "render both" fails test A(2). Existing seams it reuses: govkit's name-keyed leg rows (ownership in the receipt, drift reported, ceiling kept), and the lexicon's custom pack. |
| D | The adopter ships its own kit or layer, registered at the core's points | (1) Can it amend or disable a gov item? (2) Can it add an item inside a core step? (3) Can its role act in a core item? | **LOSES on all three.** (1) Refused by EX-1, P28 and `owned`. (2) No such point (LF F-F). (3) The matrix arm reds it. It passes only for adapters, cadence programs and leg packs. |
| E | Policy values only | Can a value declare a new item? | **LOSES.** "Structural choices are decisions, not policies" (P10), and a value takes registered names only (LRT [extend]). It passes for PARAMETERIZE, and for DISABLE where a key already selects. |

## Pick

I pick **C**, with **E** for parameterizing what is already registered. C's repository pack registers at the same core points D names, under the owner `repo`. IA's other parts extend unchanged: the `repo` owner, the pins, the successor maps, the fixed classes, orders, the delta report and the exclusion refusal. Two parts do not. `amends` has to mean a field-level patch rather than text placement, and IA-3's "render both" has to become "hold the patch, run gov's row, file an order" for structured rows.

**What C leaves for the owner:**
- the spelling and ownership of repository rows inside the `item`, `leg` and `role` namespaces, and the owner check's value for them;
- the fixed field list per kind, including whether an adopter may widen a role's allowance or only narrow it;
- whether a repository role may act in a core item, which P28's arm forbids today;
- a lens route that is data, not code. The build must test whether `agent-cap` admits a five-slot literal whose briefs are read from data;
- where an adopter's own legs come from once the manifest is generated;
- the destination keys for `[effort.roles]`, `[effort.stages.*]` and `[gates]`;
- step-gate joins for item, leg, role and transition-row tags, and a change record for each structured row;
- re-pointing a policy value that names a renamed gov boundary;
- the flow and role half of the IA-6 census: gov's 91 kit-less legs and the seeded efforts;
- factory kinds for items, transitions and lenses, which FD C3 does not list.

**Files read:**
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `...\build\2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`, `...-layer-flow.md`, `...-layer-roles.md`, `...-layer-runtime.md`, `...-layer-instruction.md`, `...-review-system.md`, `...-lexicon.md`
- `...\build\2026-10-16-build-PLAY-dClosedLoop-1-systems.md`, `...-layer-expansions.md`
- `...\build\2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`
- `...\build\2026-10-14-build-PLAY-dClosedLoop-1-foundations.md`, `...-walkthrough.md`, `...-design-rounds.md`
- `...\build\2026-10-18-build-PLAY-dClosedLoop-1-fates.md`, `...-memory-plan.md`, `...-night-pass.md`
- `...\build\2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md`, `...-research-adopter-design.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\govkit\govkit.py`, `tools\run-gates\kit.toml`, `tools\run-gates\run-gates.sh`, `tools\gate-legs.json`, `tools\roles\kit.toml`, `tools\roles\house\policy.toml`, `tools\hooks\agent-cap.js`, `tools\workflows\tier2-review.js`
