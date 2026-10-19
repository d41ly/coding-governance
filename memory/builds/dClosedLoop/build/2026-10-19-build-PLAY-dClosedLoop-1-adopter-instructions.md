# Adopter instructions: each repository's own rules, and how they survive gov's updates

**Serves:** research PLAY-dClosedLoop-1

The owner opened a review of the instruction layer's rendering and adoption with one case left out before: every
repository that adopts gov, gov included, wants its own principles, rules and instructions, and wants to adjust gov's,
and those changes must survive gov's updates. Four researchers each took one question. Their returns are saved
verbatim beside this record. This record answers the owner's two questions, tests the owner's hypothesis, recommends a
design, and puts the choices it cannot make itself to the owner.

## [words] The owner's request, 2026-10-19

> let's review the instruction layer's rendering and adoption. One important part we didn't review previously -
> custom instruction rendering per adopter (including Gov itself). Case: Gov's default charter/methods/protocols/prompts
> ship with a set, predefined number of instructions. However, it's unreasonable to expect every adopter to operate
> only of that limited instruction set - every adopter would want to render in their own principles, rules, and
> instructions and tailor Gov to their own project. Problems arise: 1. does Gov account for a flexible design to add
> custom instructions/adjusting existing ones in the adopted template files? 2. how do custom instructions/edits
> survive Gov updates without breaking them? As we're deploying relational syntax and tagging, seems to be an easy
> problem to solve - tag every edit and render updates around it but I want you to run a research/design pass on this
> matter and come up with a fitting recommendation for the architecture we're designing.

## [questions] Four researchers, one question each

| Dispatch | Question | Return |
|---|---|---|
| 118 | How can an adopter add to gov's instructions or change them today, and what does the next update do to each change? Measured on a scratch install. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-adopter-today.md` |
| 119 | What does the converged design decide about an adopter's own instructions and its changes to gov's, and what does it leave open? | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-adopter-design.md` |
| 120 | How do systems outside gov let users customize shipped defaults and keep the changes through upstream updates? | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-adopter-prior-art.md` |
| 121 | If every adopter edit were keyed to a gov unit's tag, how often would gov's own history collide with it? | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-adopter-history.md` |

## [today] What gov does today, measured

From the scratch install (dispatch 118):
- **Only composition survives.** Two seams carried an adopter's text through an update into the render: the
  overlay's `[charter] adopter_rules`, rendered into the charter's section 2, and the roles kit's house files,
  appended to each rendered agent. Both only add. A `[charter]` key that names a gov rule is refused.
- **An edit to a rendered instruction is lost.** The charter's generated region, the Skills, the rendered agents,
  `HYGIENE.md`, `TEMPLATE-SPEC.md`, the build method and the protocols are rewritten whole. The update overwrote every
  sentinel edit, and printed `re-rendered` for edited and unedited files alike (`govkit.py:9624-9625`). A tagged edit,
  made by the runbook's carve-out contract, was lost the same way, since nothing reads the tag.
- **An edit to gov's own source merges until gov touches the same line.** Then the whole kit is held back and rolled
  back, with an order.
- **A seeded charter template freezes.** It stays at its install vintage, `reseed-available`, edited or not.
- **Pre-existing instruction files meet install badly.** The adopter's `AGENTS.md` kept its text, with the region
  appended. `CLAUDE.md`, `GEMINI.md` and Copilot's instructions stayed unwired until `--force`, which overwrites them,
  and a copy-mode alias goes stale at every charter change with no check at update.
- **Gov never runs this path on itself.** It has no install receipt and is never updated.
- **A fresh install needed manual steps.** On an empty repository the kickoff seed created `memory/` before the memory
  tree's adopter ran, which then refused, and the agent-instructions adopter ran before the charter existed.

## [decided] What the converged design decides, and what it leaves open

From the records (dispatch 119):
- **Decided:** who may write units (`instructions.edit`, owner proof by `instructions.proof`); the repository's own
  units in an overlay, `.governance/instructions.toml`, merged with each kit's manifest (systems
  `[design-instruction-writing]`); the project block rendered from it (P8); repository-declared practices and presets;
  policy values; units promoted from memory; recorded live overrides; refusing a hand edit to a rendered file; and
  principles fixed but for an owner-ratified amendment (foundations K2).
- **Open:** amending, replacing or masking a gov unit; re-ranking one; a repository's own policy keys; surviving a
  gov reword, rename, split or retirement of a unit the repository changed; a tag namespace for repository units; and
  turning an adopter's existing `AGENTS.md` into units at adoption.
- **Contradictions found:** two homes for the repository's rules (the systems record's `instructions.toml`, the memory
  plan's `deploy.toml`); "merged by row key" against the `unique` check; the owning-kit field; the roles' house
  overlays answered three ways; and gov's own rules, whose move out of the shipped set into gov's overlay, decided by
  the walk, was dropped at `aa0d778b1`.

## [outside] What systems outside gov teach

From the prior-art pass (dispatch 120), eight families:
- **Joined layers** (Claude Code's `CLAUDE.md`, `AGENTS.md`, Cursor's rules) leave conflicts to the model, silently,
  and the harnesses disagree on which file wins.
- **Keyed values** (git config, Helm, NixOS) fit values, not prose. NixOS alone fails the build on two definitions.
- **Patches keyed to a base** (Kustomize, JSON Patch's `test`) pin the base, and a pinned patch fails loudly when
  upstream moves it.
- **Override by id** (Docusaurus swizzling, WordPress child themes, systemd drop-ins) wrap or replace a shipped unit.
  A wrap lets upstream's change through; a replacement shadows it. `systemd-delta` reports every override.
- **Three-way merge of a vendored copy** (copier, ucf) leaves conflict markers inside the file.
- **Patch queues** (quilt, patch-package) misplaced an edit with exit 0 in a probe, when upstream added matching
  context.
- **Keep-or-replace with a side copy** (dpkg, RPM) silently keeps the user's file when unattended.
- **Ejection** stops every update.

The pass's probe of tag-keyed amendments with a pinned base reddened a reword, a rename with no declared step and a
split, and passed a rename the step declared. It missed one case: a new upstream unit, under its own tag, that
contradicts an adopter's. No family catches that mechanically.

## [history] The hypothesis against gov's own history

From gov's history, 2026-07-01 to 2026-10-19 (dispatch 121):
- **A bare tag misses most changes.** Of 797 text edits gov landed, 778 kept their anchor, so an edit keyed by tag
  alone would be reapplied over changed text, unseen. In 36 of them the body was largely replaced.
- **A tag plus a hash of gov's base text catches them.** A whitespace-normalised hash flagged no whitespace-only
  change over the whole history. Its cost is coarse flags: 65% of flagged edits change under a tenth of the unit's
  words.
- **Tags held best.** Heading anchors were orphaned at 0.0077 per touch, role fields at 0.0273, and rule tags at 0 in
  their ten days. Positions moved twelve times as often as anchors were renamed, and fuzzy matching misplaced or lost
  9.9% of edits.
- **Orphans come in bursts.** Four restructuring commits carry 63 of the 102 orphan events, rewritten past any
  matcher, so a restructure must ship its map of renames, splits and retirements.
- **The noise follows unit size.** Today's hot units run to thousands of words, so an adopter who amended 20 units
  would meet a changed one in 33% of landings and in most weekly pulls. Units of one line each flag only when that
  line changes.

## [answer] The owner's two questions, answered

1. **Does gov let an adopter add instructions and adjust gov's?** It lets them add: to the charter's section 2, to
   each role through its house file, and in files gov never touches, such as their own path rules. It gives no way to
   adjust or remove a gov instruction: the edit is either refused, lost at the next update, or merged until it holds a
   whole kit back.
2. **How do custom instructions survive gov's updates?** Today, only by sitting where gov's renderers never write.
   The design must make survival hold by construction.

**The hypothesis holds, with three corrections.** Tagging is the right key, and the rule tags the charter carries now
were the most stable anchor in gov's history. But:
- **Tag the change, never the rendered text.** A tag inside a rendered file was lost, since the renderer rewrites the
  whole file. The adopter's change must be a unit of its own, in the adopter's overlay, pointing at gov's tag.
- **Pin the change to the text it was written against.** A tag alone would have missed 778 of 797 changes.
- **Ship a map with every restructure.** Renames, splits and retirements must travel with the update, or the change
  is orphaned.

One case stays beyond any mechanism: a new gov unit, under its own tag, that contradicts an adopter's. It can only be
listed for review.

## [design] The recommendation: compose, never edit

Every repository, gov included, keeps its own instructions as units in its own overlay, and changes gov's units only
through typed, pinned edges from its own units. One renderer composes every document from gov's units and the
repository's. Nobody edits a rendered file, and an update never writes the repository's units.

1. **One home.** The repository's overlay is `.governance/instructions.toml`, the systems round's home, in the same
   row grammar as each kit's `instructions.toml`, and it is the instruction manifest dGroundRules' minimal guard names.
   It absorbs `deploy.toml`'s `[charter] adopter_rules`, as level-0 units, and the roles' house files, as level-5
   units selecting their role. `deploy.toml` keeps the install answers and the kit selection. Each row's owner is the
   repository.
2. **Its own namespace.** Repository units are tagged `repo.<segment>`, a namespace gov never ships, so no repository
   tag can collide with a present or future gov tag. A unit contributed upstream is re-tagged when gov ships it, and
   the release maps the repository's unit to gov's.
3. **Add.** A repository unit takes its place by its level, `select` and `when`, like any unit: level 0 renders as the
   charter's project block (P8); levels 3, 4 and 5 render inside their documents, in a part marked as the
   repository's. The repository cannot write the card (level 1), the task (level 6) or memory (level 7).
4. **Amend, the default.** A repository unit with `amends=<tag>@<hash>` renders right after gov's unit, which keeps
   rendering, so gov's later wording still reaches the repository. This is the wrap of prior art.
5. **Replace.** A repository unit with `supersedes=<tag>@<hash>` renders in gov's unit's place. Gov's later wording no
   longer reaches the repository, so its pin matters most.
6. **Exclude.** A policy value, `instructions.exclude`, lists the gov units the repository drops, as
   `charter.practices` does for practices. Exclusion is refused for a fixed unit and for one another active unit
   requires, naming the requirer.
7. **Parameterize.** Gov's units read policy values and install answers, as designed. A repository may declare its
   own keys under `repo.`, read only by its own units and outside the presets' completeness check.
8. **Fixed units.** A gov unit declares its class. A fixed unit cannot be amended, replaced or excluded: the core
   principles, the floor's invariants, and every unit a gov tool parses, such as the micro-format grammar and the
   loop's contracts. Every other unit is open.
9. **Pins.** The `@<hash>` in an edge is a whitespace-normalised hash of gov's unit text when the edge was written.
   Each gov change record declares itself `editorial` or `semantic`. A render that finds a pin behind gov's current
   text walks gov's change records between them:
   - only editorial changes: the pin stands, and nothing flags;
   - a semantic change: gov's new text and the repository's change both render, and the edge is stale. The update
     files an order for the repository's owner, as `instructions.stale` says (order by default, refuse, or warn), and
     re-pinning is an `instructions.edit` call that records the review.
10. **Maps.** A gov unit's change record carries its successor, `retired:<tag>`, widened to a list for a split and
    `none` for a retirement:
    - a rename re-points the repository's edges to the successor, keeping the pin;
    - a split or a retirement orphans the edge. An orphaned amendment is held out of the render, and an orphaned
      replacement renders on its own as the repository's unit. Either way an order names it.
    - dSafePassage's step gate takes gov's unit tags into its population, so a gov unit can vanish only with a
      change record naming its successor.
11. **New gov units beside the repository's.** The update lists every new gov unit at a level and `select` where the
    repository has units, for the owner's review. This is advisory: a contradiction under different tags is semantic.
12. **Budgets and harnesses.** The repository's units count against each document's budget. Over budget, the render
    refuses and names the largest contributors by owner, never truncating. One unit renders for every harness the
    same way, so an alias is a render, never a copy.
13. **Edited renders.** The render gate already refuses a hand edit at the push. An update that finds a rendered file
    edited since its last render names it and holds that file with an order, never overwriting it as `re-rendered`.
    `instructions.edit` can propose the edit back as overlay units.
14. **The report.** One view lists every gov unit's state in the repository (unchanged, amended, replaced, excluded,
    stale or orphaned), every repository unit, and the new gov units beside them. This is `systemd-delta`'s report,
    shown at every update.
15. **Adoption of existing instructions.** At install, the repository's own instruction files are never overwritten
    or left unwired. Their text renders verbatim as a legacy block after the project block, on a shrink-only legacy
    list, and every harness file is wired at once. Retrofit's `adopt` program gains `adopt.instructions`, which
    proposes each paragraph as a repository unit, as an amendment of a gov unit, or as a drop, for the owner to rule
    once.
16. **Gov as its own adopter.** Gov's own rules live in gov's own overlay, like any repository's. The shipped
    foundation set keeps only what every adopter needs. Gov gets a receipt and updates itself every release, with
    dSafePassage's gov-first, so the survival path runs on gov before any adopter.
17. **Seeds retire.** No adopter carries a seeded copy of gov's charter template. Gov's units are engine files that
    every release updates, and the repository's changes are in its overlay.

## [scenarios] How each case fares

| Case | Today | Under the recommendation |
|---|---|---|
| The adopter adds a rule | section 2 and house files only | a `repo.` unit at its level, rendered in its document |
| The adopter adjusts a gov rule | refused, or lost at update | an `amends` unit; gov's text keeps flowing |
| The adopter replaces a gov rule | lost at update | a `supersedes` unit, pinned |
| The adopter drops a gov rule | not possible | `instructions.exclude`, refused for fixed and required units |
| Gov rewords a rule the adopter changed | the edit is lost silently | both render; an order to re-pin, unless the change is editorial |
| Gov renames it | lost | the edge re-points by the change record's successor |
| Gov splits or retires it | lost | an order; an amendment held, a replacement kept on its own |
| Gov adds a rule that contradicts the adopter's | both load silently | listed for review; no mechanism can see the contradiction |
| The adopter's units overflow a budget | not checked | the render refuses, naming the largest contributors |
| Two harnesses | aliases copied and go stale | each harness renders the same units |
| The adopter edits a rendered file | overwritten as `re-rendered` | refused at the push; held with an order at update |
| A repository adopts gov with its own `CLAUDE.md` | left unwired until `--force` overwrites it | its text becomes a legacy block, wired at once, then proposed unit by unit |
| Gov itself | never updates; its rules ship to adopters | its own overlay, updated every release first |

## [chain] Where it lands

- **dGroundRules:** the minimal guard's instruction manifest is the repository's overlay,
  `.governance/instructions.toml`.
- **dSafePassage:** the step gate's population takes gov's unit tags when dOrderedCharter lands them; an update holds
  an edited render with an order.
- **dOrderedCharter:** the overlay, its `repo.` namespace and the four operations; fixed units; pins, the change
  records' editorial and semantic marks, stale and orphaned edges; composition, the budget refusal and the report;
  gov's own rules moved to gov's overlay; the seeded template retired, and aliases rendered.
- **dBoundRoles:** the house files become overlay units selecting their role.
- **dLinkedLibrary:** `adopt.instructions`, the legacy block and its proposals.
- **dShippedRelease:** gov's receipt and its self-update every release, beside dSafePassage's gov-first, and a fresh
  install in a single pass.

## [gaps] Gaps this adds to the register

| Key | Stage | Sev | Gap | Owner |
|---|---|---|---|---|
| `gap-found-29` | Foundation | HIGH | No seam changes or removes a gov instruction and keeps the change: the overlay slot and house files only add, an edit to a rendered instruction is overwritten at update and named only `re-rendered`, a tagged edit is lost, and an edit to gov's source holds the kit back on a conflict. | dOrderedCharter |
| `gap-found-30` | Foundation | MED | A seeded charter template freezes at its install vintage, edited or not. | dOrderedCharter |
| `gap-found-31` | Foundation | MED | Gov's own rules ship in the set every adopter receives: their move to gov's overlay was dropped. | dOrderedCharter |
| `gap-deploy-26` | Deploy | MED | An adopter's existing `CLAUDE.md`, `GEMINI.md` and Copilot instructions stay unwired at install until `--force` overwrites them, and a copy-mode alias goes stale at every charter change with no check at update. | dLinkedLibrary |
| `gap-deploy-27` | Deploy | MED | A fresh install of every kit needs manual steps: on an empty repository the kickoff seed creates `memory/` before the memory tree's adopter, which then refuses, and the agent-instructions adopter runs before the charter exists. | dShippedRelease |

## [forks] For the owner, 2026-10-19

| Fork | Question | Options, the recommendation first |
|---|---|---|
| IA-1 | Where does a repository's own instruction text live? | one guarded overlay, `.governance/instructions.toml`, absorbing the charter's adopter rules and the roles' house files; per artifact, as today |
| IA-2 | How does an adopter change one of gov's units? | its own units with typed, pinned edges: amend, replace, and a policy list to exclude; replace and exclude only; edit the rendered text and three-way merge it at update |
| IA-3 | When gov changes a unit an adopter changed, what does the update do? | render both and file an order, editorial changes exempt; hold the update until the owner re-pins; warn only |
| IA-4 | Which of gov's units may an adopter change? | all but a fixed set: the core principles, the floor, and what gov's tools parse; everything, principles by the repository owner's ratified record; practices only |
| IA-5 | What happens to an adopter's existing instruction files at install? | a legacy block, wired at once, then proposed unit by unit for the owner; left beside the charter, as today |
| IA-6 | Should rules only gov needs leave the set gov ships? | yes: a census of today's practices, each ruled by the owner, the gov-only ones moved to gov's overlay; no, keep shipping them |

## [owed] Owed to later builds

- The pin's noise re-measured at dOrderedCharter's first unit, over units of one line, against gov's history.
- The map every restructuring release ships, checked by the step gate from the first release that moves a unit.

## [answers] The owner's answers, 2026-10-19

Put to the owner in two batches, each question with its recommendation first. The owner's words, verbatim:

| Fork | The owner's answer |
|---|---|
| IA-1 | "One overlay (Recommended)" |
| IA-2 | "Own units, typed edges (Recommended)" |
| IA-3 | "Render both, file order (Recommended)" |
| IA-4 | "All but a fixed set (Recommended)" |
| IA-5 | "Legacy block, then proposals (Recommended)" |
| IA-6 | "Yes, by census (Recommended)" |

Every answer took the recommendation, as `[forks]` words it.

## [folded] Where the answers went, 2026-10-19

- **v2:** P8 says how a repository changes gov's units; the catalogue gains `instructions.exclude` and
  `instructions.stale`, the first among the keys presets never touch and the second with a preset row; dGroundRules'
  minimal guard names the overlay; dSafePassage's step gate takes gov's unit tags and its update holds an edited
  render; dOrderedCharter's registry gains a unit's owner and class and the `repo` namespace, and three units: the
  overlay and its operations, pins and drift, and composition with the census of gov-only rules; dBoundRoles moves the
  house files into the overlay; dLinkedLibrary gains `adopt.instructions`; dShippedRelease installs every kit in one
  pass; `[owed]` keeps the pin's noise to re-measure; and a revision note.
- **The memory plan:** the deploy overlay's adopter rules move to a new instruction-overlay pocket, and the unit site
  carries the pinned target.
- **The gap register:** `gap-found-29`, `gap-found-30`, `gap-found-31`, `gap-deploy-26` and `gap-deploy-27`.
- **The fates record:** the seeded charter template retires, and the house files become overlay units.

The design map reddened once on the fold: the `repo` namespace named no owning build, since a namespace's owner
is declared on the systems record's `[design-tags]` owner lines. `repo` is declared there now, beside the
namespaces that record lists, and v2's tag-system list keeps R-B's twelve.
