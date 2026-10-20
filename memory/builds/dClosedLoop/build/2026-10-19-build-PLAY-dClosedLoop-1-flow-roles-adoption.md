# Flow and roles adoption: each repository's own steps, items, gates and roles, and how they survive gov's updates

**Serves:** research PLAY-dClosedLoop-1

The adopter-instructions round settled how a repository adds its own instructions and changes gov's. The owner then
chose the same lens for the Flow and Role layers: how a repository adds its own steps, items, gates and roles, or
adjusts gov's, how those render, and how they survive gov's updates. Three researchers each took one question, and
their returns are saved verbatim beside this record. This record answers the question, recommends a design that
extends the instruction answer from text to structure, and puts the choices it cannot make itself to the owner.

## [words] The owner's request, 2026-10-19

> Run the reviews of the same shape (medium effort, twice) for the last three folds. While they're running, we'll
> review the next piece of the Flow and Role layers.

Asked which piece came next, the owner chose "Adoption and customization (Recommended)", whose option read: "The same
lens as the instruction piece, applied to flow and roles: how an adopter adds its own steps, items, gates and roles,
or adjusts gov's; how those render; and how they survive gov's updates. The new instruction overlay already takes in
the roles' house files, so this is the direct continuation."

## [questions] Three researchers, one question each

| Dispatch | Question | Return |
|---|---|---|
| 123 | How can an adopter add to gov's flow and roles or change them today, and what does the next update do to each change? Measured on a scratch install. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-flow-today.md` |
| 124 | What does the converged design decide about an adopter's own flow and roles and its changes to gov's, and what does it leave open? | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-flow-design.md` |
| 125 | How do systems outside gov let users add steps, checks and roles and change the shipped ones, and keep the changes through upstream updates? | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-flow-prior-art.md` |

Each pass's commands and probes are in `build/2026-10-19-build-PLAY-dClosedLoop-1-research-flow-instruments.md`.

## [today] What gov does today, measured

From the scratch install, gov at `320c79646` installed into an empty repository, with gov's later changes made as
synthetic commits (dispatch 123):
- **Three things add beside gov's:**
  - a row in the shared gate-leg manifest, kept by name, though nothing on the adopter's side registers or checks it;
  - the unattended run's vocabularies in `.unattended.conf` (`PHASES_EXTRA`, `DOD_EXTRA` and their kin), never
    touched by an update, though an extra phase is vocabulary only and an extra definition-of-done item is satisfied
    by an attested fact;
  - a role file dropped beside gov's, with its house overlay, which survives and renders.
- **An adopter's role or workflow cannot register without editing gov's engine.** `check_roles.py` types
  `BODY_CEILINGS`, `WORKFLOW_NAMES` (closed at ten) and `DRIVERS`, and the review harness types `KINDS`, `ROLE_KEYS`
  and its lens arrays. Read from the code, the catalogue leg reds a role file with no ceiling row. The registering
  edit conflicted with gov's change on the fixture, and the whole roles kit was held back and rolled back.
- **Changing gov's flow mostly fails:**
  - a leg's `ceiling` override is kept;
  - an edited argument list withheld every gate leg the update built, rc 1;
  - a deleted gov leg came back, and no line said so;
  - `.claude/roles.json` and the rendered harnesses lost their edits silently;
  - the seeded `house/policy.toml` kept the adopter's retune, but gov's own change to it never arrived
    (`reseed-available`).
- **Nothing reports it.** No update line named an adopter's role, overlay or leg, or the restored gov leg, and the
  fixture's update exited 1 on two unrelated holes, so the exit code cannot tell a lost edit.
- **Gov customizes in place.**
  - 73 of its 140 legs come from no kit descriptor, each an `[[exempt_leg]]` row of `tools/govkit/registry.toml`,
    measured at `67995cb6f`. The design pass's 91 counted `kit.toml` files only, without `tools/govkit/entries/`.
  - Gov edits `workflows.toml` and `house/policy.toml` in place, so its own retune, the builder at `xhigh`
    (`175f86981`), becomes every adopter's seed.
  - Its house overlays are empty, and it never runs `update` on itself.
- **A defect outside the question.** In a default adopter install, `roles.json` names the review harnesses where the
  kit is not installed, and the spawn guard refused gov's own `tier2-review.js`, rc 2. It was offered to the owner as
  a separate task, and `[gaps]` records it.

## [decided] What the converged design decides, and what it leaves open

From the records (dispatch 124):
- **Decided:**
  - breakpoints by `review.breakpoints`, and probe points by `probe.points`;
  - presets that extend a shipped one, playbooks and practices;
  - policy values, a repository's own keys among them;
  - role prose, as overlay units selecting their role (IA-1);
  - lexicon packs;
  - product tests by `tests.product`, and CI test jobs imported as legs;
  - environments and fixes, by registered name.
- **Open:**
  - an item, a transition row or a role inside a core step;
  - amending, replacing, disabling or reordering a gov item, route, leg, workflow or role field;
  - a lens added without editing the harness;
  - a repository's own legs once the manifest is generated from packs;
  - destination keys for the house file's efforts and gate grants, and a key for a role's model;
  - surviving a gov change to any of these. The step gate names no item, leg, role or workflow tags, no change record
    marks a structured row editorial or semantic, a policy value naming a renamed boundary is not re-pointed, and a
    seed never receives gov's change;
  - the flow and role half of IA-6's census.
- **Contradictions found:**
  - `[gates]` has two homes, the policy file and each role's ceiling;
  - the records give the builder `high` while the seeded file says `xhigh`;
  - a lens registers three ways in three records;
  - the leg manifest is generated from packs in one record, while govkit keeps adopter-written rows in it;
  - the roles layer's R3-A still calls the house files seeds, which IA-1 superseded;
  - overlays sit under distribution, an expansion, while the core's dOrderedCharter owns the overlay.

## [outside] What systems outside gov teach

From the prior-art pass (dispatch 125), eight families:
- **A fixed skeleton with typed slots** (Azure Pipelines `extends`, reusable workflows, Maven's lifecycle) adds
  safely, and allows no change to what is shipped.
- **Keyed override, the user's key winning** (GitLab `extends`, pre-commit, Renovate, Claude Code subagents) loses
  upstream's change silently. A pre-commit probe kept the user's arguments over upstream's new required flag, exit 0.
- **A dependency graph checked when composed** (Gradle, GitLab `needs`, LangGraph) is loud on a dangling reference.
  In a LangGraph probe, a renamed node raised an error, while an orphan node compiled and never ran.
- **A pinned revision bumped by a validating update** (pre-commit `autoupdate`) refused an update missing a hook the
  user named. Upstream's new hook never ran for the user, because new hooks are opt-in.
- **Policy at load time** (Airflow's cluster policies) inspects, rewrites or rejects definitions. It suits a fixed
  set.
- **Copy-and-own** (Jira's workflow schemes) never receives upstream's change.
- **Versioning a running process** (Temporal's patching, pinned versus auto-upgrade) keeps a run on its path through
  a change.
- **A registry keyed by id** (Backstage's actions, Claude Code's plugin-scoped names) is loud on a collision. No
  system declares which shapes a role may run in.

The combination the pass picked, an own namespace, pinned edges, a typed graph checked at composition, roles declaring
their shapes, a pinned revision and pinned runs, failed loudly on every scenario the pass modelled but one. An
upstream item that changes what an adopter item's input means, under an unchanged key and type, passes every
mechanism. Two mitigations narrow it: version an output's type when its meaning changes, and list gov's new ancestors
of an adopter's items at each update.

## [answer] The owner's question, answered

1. **Can a repository add its own steps, items, gates and roles?** Today it can add legs by hand, run vocabularies,
   and role files that the catalogue then refuses. It cannot add an item, a workflow or a lens without editing gov's
   engine. The design adds breakpoints, probes, presets, playbooks, policy values and role prose. It does not add
   items, roles in core steps, lenses, or legs once the manifest is generated.
2. **Can it adjust gov's?** Today only a leg's ceiling and a seeded effort; every other change is refused, lost, or
   holds a kit back. The design adjusts only role prose.
3. **How do they render?** Today by whole-file renders that drop edits, while an adopter's rows render only where a
   renderer happens to glob. The design composes text, and must say what composing means for a structured row.
4. **How do they survive gov's updates?** Today only by sitting where gov never writes, or by one field's keep rule.
   The design's step gate, pins and change records cover instruction units only.

The instruction answer extends to structure with two changes. An amendment of a row is a field patch, never text
placed after gov's. And "render both" has no meaning for one row, since two rows under one tag red `unique`. Its
structural counterpart re-applies the patch over gov's new row and files an order, holding the patch only where it no
longer applies.

## [design] The recommendation: one composition, every kind

Every flow and role declaration that runs in a repository, gov included, is the composition of gov's packs and the
repository's own rows, read at the landed revision. The repository keeps its rows in its overlay, in each kind's
shipped schema, and changes gov's rows only through typed, pinned edges from its own rows, or excludes them. Every
existing check runs on the composition. Nobody edits a shipped declaration or a rendered view, and an update never
writes the repository's rows. This is the instruction round's "compose, never edit", carried from text to structure.

1. **One home.** The repository's flow and role rows live in its overlay, `.governance/instructions.toml`, beside
   its units, each in its kind's shipped schema: item, role, workflow, lens and leg, and a repository stage's splice rows (FA-3, revised 2026-10-19, the flow adoption's review). The layer-instruction record's
   R-I already counts these structured sources as instruction sources. One file keeps one guard, one door
   (`instructions.edit`), one report and one exclusion list (FA-1).
2. **Tags.** A repository row carries its kind's tag with the `adopter` segment where an owner would sit:
   `item.<step>.adopter.<name>`, `role.adopter.<name>`, `workflow.adopter.<name>`, `lens.adopter.<name>` and `leg.adopter.<name>`,
   and for a repository stage `step.adopter.<name>`, its items `item.adopter.<stage>.<name>` (FA-3, revised 2026-10-19,
   the flow adoption's review).
   Gov never ships the segment, so no repository tag collides with a gov tag. `owned` admits the segment for the
   repository, and the row's `origin` is the repository, outside the `owner` edge and `one-owner`. Prose units keep
   IA's `repo.<segment>`. The segment is `adopter`, never `repo`, since `repo` names the units' namespace and the tag
   grammar forbids a namespace word as a name's first segment (renamed 2026-10-19, the owner's tag-grammar answer). Two namespaces join: `workflow`, owned by dBoundRoles, and `lens`, by dCalibratedLens.
3. **Add.**
   - **An item** sits in a gov step as `item.<step>.adopter.<name>`, with every field an item declares: actor, needs,
     inputs, allowance, return template, a closed outcome set with `probe`, witness and routes. Its witness is
     computed, never typed (P2). Its routes may lead to gov items, and a gov item waits for it only through an
     amendment of that item's `needs`.
   - **A step:** the five stages stay fixed (P20). A repository's own step is a group of its items inside a stage, a
     program at item boundaries that `review.breakpoints` and `probe.points` place, or a cadence program at
     Runtime's cadence-item point (FA-3). The owner chose repository stages instead; `[folded]` gives the design.
   - **A role** is `role.adopter.<name>`, with the structured fields, a typed return template and its ceiling, and
     declares the shape kinds it runs in. It acts in repository items, and in a gov item only through an amendment
     of that item's actor (FA-4).
   - **A workflow** is an entry of a registered shape kind (single, per-unit, panel, twin, experiment), naming its
     roles. The kinds stay fixed.
   - **A lens** is a catalogue row whose brief is a unit, selected by `review.opt-in`. The harness keeps its
     five-slot literal and fills each slot from the catalogue as data, so the merge bar's harness check counts slots,
     never names (agent-cap's count until the night pass two's point 7).
   - **A gate leg** is `leg.adopter.<name>`, in the leg-pack schema, registered at Test's leg-pack point as the
     repository's pack, generated into the manifest by the leg factory like any pack's, and counted only once its
     seen-red record exists. After adoption has converted today's hand-added rows, a manifest row with no source
     reds.
   - **Already decided:** breakpoints, probe points, presets, playbooks, policy values, practices and lexicon packs.
4. **Amend, by a field patch.** A repository row with `amends=<tag>@<hash>` names gov's row and the fields it
   changes. A set field takes `add` and `remove`, and a scalar takes a value. Every field the patch leaves alone keeps
   flowing from gov's row. A patch touching a fixed field (item 9), or widening one, is refused (revised
   2026-10-19, the flow adoption's review). Typical patches: a gov item's `needs` gains a repository item, an allowance narrows, an
   actor becomes a repository role, a leg's ceiling or arguments change.
5. **Replace.** A repository row with `supersedes=<tag>@<hash>` answers to gov's tag in the composition, so
   dependents' `needs` and the witnesses keyed by gov's tag resolve to it. Gov's later changes no longer reach it, so
   its pin matters most. A replacement of a fixed row (item 9) is refused (revised 2026-10-19, the flow adoption's review).
6. **Exclude.** `instructions.exclude` takes any gov tag in the overlay's kinds. It refuses a fixed row, and a row
   another active row needs, names as its actor or grants, or a policy value names, naming the requirer or the key
   (the policy value revised 2026-10-19, the flow adoption's review). A role left acting in no item is
   excluded with it, or the matrix arm reds.
7. **Reorder** only through `needs`. The stages keep P20's order, item numbers are display order only, and the
   composition's graph checks hold.
8. **Parameterize** by policy values, as designed. The tunables today's house file holds get destination keys:
   `roles.effort.<role>`, `roles.effort.<workflow>.<stage>`, `roles.effort.default` and `roles.model.<role>`, so a
   preset can set them, a stage's effort defaulting to its role's key, then to the blanket `roles.effort.default`,
   then to the role's declared value, as today's resolver reads, and a role's model to its declared value (revised
   2026-10-19, the flow adoption's review). A role's gate grant stays a field of its definition, v2's ceiling of
   gate legs, changed by a patch (FA-6).
9. **Fixed rows and fields.** IA-4's three sources carry over: what the principles fix, the floor, and what gov's
   tools parse.
   - The flow's frame: the five stages and their order, each level's transitions between gov's stages except
     where a repository stage is spliced (FA-3, revised 2026-10-19), the terminal and disposition sets, and the
     position engine's answer set.
   - Items: every floor item whole, its witness written by a runner or a hook (`test.verdict` and `entry.intake`
     among them), and every step's exit item. In any gov item, its tag, its step, its witness and its outcome set.
   - Roles: the matrix arms, each core role's write class and return schema, and the cycle roles, the prompt writer
     and the driver, whole.
   - Shapes: the kinds, each stage's cap at or under `runtime.agents-in-flight` (revised 2026-10-19, the night
     pass two, point 7, the owner's NT-27: it was `FANOUT_CAP`'s bound) and the five lens slots.
   - Legs: the canary's key set, and the legs that check the composition itself.
   - Every other row and field is open. The class is derived, never typed, as the closing review settled for units.
   - Each kind's build declares its fixed list, and dOrderedCharter's row checks refuse an `amends`, a widening, a
     `supersedes` or an exclusion touching it, each seen red on that kind's own planted row (revised 2026-10-19, the
     flow adoption's review).
10. **Widening.** A patch may widen an open field, a role's tools or gate grant among them. The overlay's write
    already carries the owner's proof, and the update's report names every widening (FA-5). Each kind declares the
    direction that widens each open field: `add` on a permission set, `remove` on a constraint set such as `needs`,
    and a declared order on a scalar, so a ceiling widens as it rises. The report's widening list is compared with
    the classifier's (revised 2026-10-19, the flow adoption's review).
11. **The composition, checked and rendered.** One composer per kind reads gov's packs and the overlay at the
    landed revision, never the working tree. Every check runs on its output:
    - the schema, `owned` and `unique`;
    - the needs graph acyclic, every need resolving, and every route joined to its level's transition table
      both ways, the join `gap-flow-15` owes;
    - the matrix arms and the floor;
    - typed inputs: every input an item declares is produced by an item it needs, at its record kind's version;
    - a role spawned only in the shape kinds it declares;
    - the fixed set: no `amends`, widening, `supersedes` or exclusion touching a fixed row or field;
    - every leg's seen-red record.
    A row that fails reds at the push, as the render gate does for text. The renders follow the composition: the
    checklist views, the agent files, the role index, the manifest and the review briefs, each marking the
    repository's rows as the repository's.
12. **No closed table in code.** Each population a checker types today becomes a declaration the composition
    extends, or a fixed set its owner declares once. `BODY_CEILINGS` becomes a role field, `WORKFLOW_NAMES` the
    workflow registry, and the lens arrays the catalogue. `DRIVERS`, `KINDS` and `ROLE_KEYS` stay fixed. `PHASES_CORE`
    and `DOD_CORE` dissolve into items with the unattended kit.
13. **Pins and drift.** A pin is `<tag>@<hash>` over gov's row in canonical form, its keys sorted and its values
    normalised. Gov's change records mark each row change `editorial` or `semantic`, checked as the closing review
    settled for units. A pin behind editorial changes stands. On a semantic change, `instructions.stale` decides, read
    for rows as for units (FA-2):
    - `order` re-applies the patch over gov's new row, so gov's change flows into every field the patch leaves alone.
      It runs the composition's checks and files an order. Where the patch no longer applies, because a patched field
      is gone or the composition fails a check, the patch is held, gov's row runs as shipped, and the order says why.
      A replacement keeps running, stale, with an order;
    - `refuse` holds the update until the owner re-pins;
    - `warn` re-applies the patch, prints and journals the stale edge, and files no order. Where the patch no longer
      applies, it is held and gov's row runs, as under `order`, with a warning line saying why (revised 2026-10-19,
      the flow adoption's review).
14. **Maps.** Gov's change records carry the successors of structured tags as they do units'. A rename re-points the
    repository's edges, needs, routes and grants, and every policy value that names the boundary, `review.breakpoints`
    and `probe.points` among them. A split or retirement orphans them with an order. The step gate's population takes
    item, step, role, workflow, lens and leg tags, a repository stage's among them, each joined by the build that
    registers its namespace and seen red there on a planted tag removed with no change record (revised 2026-10-19,
    the flow adoption's review).
15. **Builds in flight.** A build moves to a new composition at its next step boundary. Its transition record into a
    step pins the composition's revision, its position derives from that revision inside the step, and the change
    records' successors carry its witnesses across. An item retired under it files an order for its owner (FA-7).
16. **The report.** The update's report, the instruction round's item 14, covers every kind:
    - every gov row's state in the repository: unchanged, amended, replaced, excluded, stale or orphaned;
    - every repository row, and every widening;
    - every new gov row upstream of a repository item in the needs graph, listed for review, since a change of meaning
      under an unchanged type passes every mechanical check.
    Gov also versions a record kind whenever an output's meaning changes, so a repository item reading the old
    version reds at composition.
17. **Adoption of today's customizations.** At install and update, the `adopt` program proposes each of today's
    customizations as overlay rows, for the owner to rule once:
    - a hand-added manifest leg as a `leg.adopter.*` row;
    - a leg's ceiling or argument override as a patch;
    - the house file's efforts as `roles.effort.*` values, and its grants as patches;
    - `.unattended.conf`'s extension vocabularies as items with computed witnesses, or drops;
    - an adopter's role files as `role.adopter.*` rows with their workflow entries.
18. **Gov as its own adopter.** IA-6's census extends to flow and roles: the 73 legs no descriptor declares, gov's
    own efforts and grants, and its `.unattended.conf` and `gate-env.sh` values. The owner rules on each, and the
    gov-only ones move to gov's overlay and policy file, so a gov retune stops becoming every adopter's default.
19. **Seeds retire.** `house/policy.toml` stops being a seed. Gov's defaults ship in the role definitions, engine
    files every release updates, and a repository's values live in its policy file and overlay. The seed's measured
    cost: the records' lowered efforts (RS-2) never reach an adopter.

## [scenarios] How each case fares

| Case | Today | Under the recommendation |
|---|---|---|
| The adopter adds a check before landing | a run vocabulary with no position, satisfied by an attested fact | an item in Test, with a computed witness, and a patch adding it to the landing item's `needs` |
| The adopter adds a role | the file renders, the catalogue reds it, and registering it edits gov's engine and holds the kit back | a `role.adopter.*` row declaring its shapes, checked at composition, with no engine edit |
| The adopter adds a gate leg | a manifest row, kept by name and never registered | a `leg.adopter.*` row in its pack, generated into the manifest, counted once seen red |
| The adopter adds a lens | per-call notes only | a catalogue row whose brief is a unit, chosen by `review.opt-in` |
| The adopter changes a gov leg's arguments | the whole manifest withheld, rc 1 | a patch, while every other leg lands |
| The adopter drops a gov leg | re-appended with no line naming it | excluded and reported, refused if fixed or required |
| The adopter retunes a role's effort | kept in the seed, while gov's later change is lost | a policy value, gov's default still flowing |
| Gov changes an item the adopter patched | the edit lost, or the kit held back | re-applied, with an order to re-pin, or held with an order where it no longer applies |
| Gov renames an item the adopter's row needs | not applicable | re-pointed by the change record |
| Gov splits or retires it | not applicable | an order, and a build in flight moves at its next step boundary |
| Gov adds an item that changes what an adopter item's input means | not applicable | a versioned kind reds a typed change; an unchanged type is listed for review only |
| The adopter excludes an item another needs | not applicable | refused, naming the item that needs it |
| The adopter's item has no witness | an attested fact | refused by the item schema |
| The adopter's role is spawned by a shape it does not declare | the spawn guard checks only declared harnesses | red at composition |
| Gov itself | edits its seeds in place, and ships its retunes | its own overlay and policy file, ruled by census |

## [chain] Where it lands

Each clause sits on the build that registers its kind, or on a descendant of every build whose schema it reads:
- **dOrderedCharter:** the overlay's row mechanism for any kind a later build registers: `owned` admitting the
  `adopter` segment in a registered namespace, field patches as `amends`, whole rows as `supersedes`,
  `instructions.exclude` over any registered kind's tags, pins over a row's canonical form, and the change
  record's marks and successors covering rows, and the row checks over a fixture kind: the fixed set refused to
  every patch, widening, supersession and exclusion, the exclude refusals naming the requirer or the key, and the
  widening classifier. Each kind's own build admits its rows, declares its fixed list and widening directions, and
  plants its own reds, below.
- **dFairHearing:** the lens catalogue as data in the review kit, the harness's five slots filled from it, and
  the merge bar's harness check counting slots (agent-cap's until the night pass two's point 7).
- **dDeclaredLoop:** the `item` kind in the kinds register with its factory, repository items composed with the
  loop definition at the landed revision, the composition's graph and typed-input checks, item tags joined to the
  step gate, a build's composition pinned per step, every policy value naming a boundary re-pointed on a rename, and
  repository stages spliced between adjacent gov stages, tagged `step.adopter.<name>`, seen red on a planted remove,
  reorder or replace and on a stage before Plan, after Deploy or across non-adjacent stages.
- **dBoundRoles:** repository roles and workflow entries, roles declaring their shape kinds, `BODY_CEILINGS` and
  `WORKFLOW_NAMES` turned into declarations, the matrix arms reading the composition, role and workflow tags joined
  to the step gate, the `workflow` namespace with gov's entries tagged in it, `roles.effort.*` and `roles.model.*`
  read before the house file, which stays a fallback until the seed retires, the gate grant as a role field, and
  the harness paths `roles.json` names resolved in the install.
- **dWitnessedBar:** repository legs from the overlay through the leg factory, a manifest row with no source red,
  leg tags joined to the step gate, and a gov leg's patched arguments and ceiling.
- **dCalibratedLens:** the `lens` kind and namespace, gov's lenses tagged in it and their briefs made units,
  repository lenses from the overlay, and lens tags joined to the step gate.
- **dShippedRelease:** `adopt.declarations`, proposing today's flow and role customizations as overlay rows, and the
  update's report extended to every kind, its widening list compared with the classifier's.
- **dConvergedCharter:** `house/policy.toml`'s seed retired, its values folded into the keys and patches above, the
  closed tables' last readers re-pointed, `.unattended.conf`'s extension keys retired with the kit, and the census
  of gov's own flow and role settings.

## [gaps] Gaps this adds to the register

| Key | Stage | Sev | Gap | Owner |
|---|---|---|---|---|
| `gap-flow-19` | Flow | HIGH | An adopter cannot add an item to a step or change one of gov's: the unattended run's extra phases are vocabulary with no position, and its extra definition-of-done items are satisfied by attested facts. | dDeclaredLoop |
| `gap-roles-24` | Roles | HIGH | An adopter's own role or workflow cannot exist beside gov's: the role checker and the review harness type their populations in code, so the catalogue reds an adopter's role file, and the registering edit conflicts and holds the roles kit back. | dBoundRoles |
| `gap-roles-25` | Roles | HIGH | In a default adopter install, `roles.json` names the review harnesses where the kit is not installed, and the spawn guard refuses gov's own `tier2-review.js`. | dBoundRoles |
| `gap-roles-26` | Roles | MED | The seeded `house/policy.toml` never receives gov's change, so the records' lowered efforts never reach an adopter. | dConvergedCharter |
| `gap-test-21` | Test | HIGH | An override of a gov leg other than its ceiling withholds the whole manifest, a deleted gov leg is re-appended with no line naming it, and an adopter's own leg is registered and checked by nothing. | dWitnessedBar |
| `gap-review-17` | Review | MED | A lens exists only as a literal in the harness, so an adopter's lens has no home beyond per-call notes. | dCalibratedLens |
| `gap-deploy-28` | Deploy | MED | No update line names an adopter's role, overlay or leg, or a restored gov leg, and an update exits 1 on unrelated holes, so an adopter cannot tell a lost change from the exit code. | dShippedRelease |
| `gap-found-32` | Foundation | MED | Gov's own flow and role settings ship as every adopter's defaults: its retunes edit the shipped `workflows.toml` and the seeded `house/policy.toml` in place, and 73 legs no descriptor declares sit in its manifest. | dConvergedCharter |

## [forks] For the owner, 2026-10-19

| Fork | Question | Options, the recommendation first |
|---|---|---|
| FA-1 | Where do a repository's own flow and role rows live? | the one overlay, `.governance/instructions.toml`, each row in its kind's shipped schema; a second guarded overlay for structured rows, `.governance/flow.toml`; per kit, as today |
| FA-2 | When gov changes a row the repository changed, what does the update do? | re-apply the change over gov's new row and file an order, holding it where it no longer applies; hold the repository's change, run gov's row and file an order; hold the update until the owner re-pins |
| FA-3 | May a repository add a step of its own? | no new stage: its steps are groups of its items inside a stage, programs at item boundaries, or cadence programs; a repository stage between two of gov's, P20 amended |
| FA-4 | May a repository's role act in one of gov's items? | yes, through an amendment of the item's actor, checked at composition; only in the repository's own items; only as an expansion role, through a layer contract |
| FA-5 | May a repository widen what a gov row allows? | yes, outside the fixed set, every widening named in the update's report; narrow only, anything wider being the repository's own row |
| FA-6 | Where does a repository tune a role's effort, model and gate grant? | effort and model as policy keys that presets can set, the grant a field of the role's definition patched in the overlay; all three as patched role fields; all three as policy keys |
| FA-7 | When an update or an overlay change alters the flow under a build in flight, when does the build move? | at its next step boundary, its witnesses carried by the change records; at once; never, keeping the flow it opened under until it lands |

## [owed] Owed to later builds

- The catalogue and render-wiring legs run on a fixture holding an adopter role, confirming the verdicts dispatch
  123 read from the code, since the scratch-guard refused that researcher the legs.
- the roles pack admitting a harness whose five lens slots are filled from data, where agent-cap admitted it
  until the night pass two's point 7, tested at dFairHearing.
- The whole-row pin's noise for structured rows, measured over gov's history of `workflows.toml`, the leg manifest
  and the role files. The prior-art pass measured it on a model only.
- A build positioned on an item that an update renames, splits or retires, run end to end at dDeclaredLoop.

## [answers] The owner's answers, 2026-10-19

Put to the owner in two batches, each question with its recommendation first. The owner's words, verbatim:

| Fork | The owner's answer |
|---|---|
| FA-1 | "One overlay (Recommended)" |
| FA-2 | "Re-apply, file order (Recommended)" |
| FA-3 | "Repository stages" |
| FA-4 | "Yes, by amendment (Recommended)" |
| FA-5 | "Yes, reported (Recommended)" |
| FA-6 | "Keys + role field (Recommended)" |
| FA-7 | "Next step boundary (Recommended)" |

Six took the recommendation. FA-3 chose the alternative: a repository may insert a stage of its own between two of
gov's, and P20 is amended. The foundations record's closed set of extension kinds already lists `stage`.

## [folded] Where the answers went, 2026-10-19

- **A repository stage (FA-3).** A repository stage is spliced between two adjacent gov stages by pinned rows of the
  build's transition table. Gov's five stages stay whole and in order, so the splice can neither remove, reorder nor
  replace one, and the transitions between gov's stages stay fixed except where a splice sits. The stage's items and
  its exit item are witnessed as a gov step's are, and its boundaries are reviewed through `review.breakpoints`.
  Every build that passes its two neighbours passes it, unless a route of its own skips it. dDeclaredLoop builds it,
  seen red on a planted stage that removes, reorders or replaces a gov stage, and green on one spliced between Test
  and Deploy. P20 reads: "A build passes gov's five steps, Plan, Design, Build, Test and Deploy, with any stage its
  repository inserts between two adjacent ones (FA-3)."
- **v2:**
  - P8 says the composition covers every kind, and P20 admits repository stages.
  - The distribution layer only seeds overlays, which the core composes, closing the sixth contradiction.
  - `instructions.exclude` takes any kind's tag, and `instructions.stale` reads rows as FA-2 says.
  - The catalogue and presets gain `roles.effort.<role>`, `roles.effort.<workflow>.<stage>` and `roles.model.<role>`,
    and the house file's `[gates]` folds into each role definition's gate grant, closing the first contradiction.
    `roles.model.<role>` joins the keys presets never touch, since its values are the harness adapter's, as
    `runtime.act-harness`'s are; the preset check reddened on it once, before that. The flow adoption's review took
    it off again: the owner's FA-6 chose keys that presets can set, so every shipped preset keeps the role's model
    and a repository's own preset may name one (revised 2026-10-19).
  - dOrderedCharter gains the overlay's row mechanism, and dFairHearing the lens catalogue as data.
  - dDeclaredLoop gains repository items, repository stages and the per-step composition pin.
  - dBoundRoles gains repository roles and workflows, the harness-path check and the tuning keys.
  - dWitnessedBar gains repository legs, and dCalibratedLens repository lenses.
  - dShippedRelease gains `adopt.declarations` and the report over every kind.
  - dConvergedCharter gains the seed's retirement and the census.
  - `[owed]` carries this record's four checks, and a revision note records the answers.
- **The systems record:** `workflow` is dBoundRoles' namespace and `lens` dCalibratedLens', the unit's row grammar
  admits the overlay's flow and role rows, and the role shapes' effort names its destination keys. The design map
  first left both namespaces out, since it reads their names from the namespaces' "plus" line, which now names
  them.
- **The memory plan:** the instruction overlay's pocket and the unit site take the flow and role rows.
- **The gap register:** `gap-flow-19`, `gap-roles-24` to `gap-roles-26`, `gap-test-21`, `gap-review-17`,
  `gap-deploy-28` and `gap-found-32`, each on its owning build's row.
- **The fates record:** `house/policy.toml` folds as FA-6 says, and `workflows.toml`, `tier2-review.js` and the leg
  manifest take a repository's rows. `.unattended.conf`'s extension vocabularies gain a row of their own.

## [reviewed] The closing review, 2026-10-19

The owner asked, "run the review pair on both folds, medium effort." Two independent light diff reviews read
`67995cb6f..e1a54ac67`, and `build/2026-10-19-build-PLAY-dClosedLoop-1-flow-adoption-reviews-compared.md` compares them. Every confirmed defect is folded. The fixed set gained its row
checks, effort one home with a blanket default, a repository stage its tag, and `roles.model.<role>` its place among
the keys presets set, as FA-6 chose.

## [renamed] The owner segment, renamed, 2026-10-19

The flow adoption's review left one fork, found while folding: the tag grammar forbids a namespace word as the first
segment of a tag's name, and `repo`, a namespace since IA-1, was the owner segment of every repository row. Put to the
owner with the recommendation to admit the segment as an exception, the owner answered, verbatim:
"rename that segment to conform to tag grammar". The segment is `adopter` in every tag form above, in v2, the systems
record, the memory plan and the adopter-instructions record, and a repository's own policy keys sit under `adopter.`
in the policy file. The `repo` namespace keeps a repository's prose units.

The same rule caught four of the catalogue's keys, whose first segment is `policy`. Asked whether to rename them and
add a check, the owner answered, verbatim: "yes, rename them and add the check but also -  shouldn't lexicon integrate with the tag grammar? Will this be accounted for?" The keys are `policy-file.guard`, `policy-file.proof`,
`policy-file.on-invalid` and `policy-file.on-missing-expansion`. dOrderedCharter's core shape check now states the
grammar's rules and refuses a name whose first segment is a namespace word, reading the namespace words from the
registry, and dDeclaredLoop arms it over every catalogue key. The lexicon was already designed to check tag names at
the name-check point (dMindYourWords). It now grades every tag's name and policy key, answers tag names through
`--suggest`, and reads the namespace words from the same registry, and `gap-lex-10` holds it to that.
