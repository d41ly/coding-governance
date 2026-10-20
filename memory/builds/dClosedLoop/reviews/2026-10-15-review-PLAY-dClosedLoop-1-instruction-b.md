**Serves:** spec-audit PLAY-dClosedLoop-1

# Tier-2 review, run B: the instruction layer's design record for dClosedLoop

Provenance: a Tier-2 spec audit with five lenses (finders gov-spec-reviewer), five skeptic batches (gov-skeptic) and synthesis (gov-synthesizer). It was run on 2026-10-15 as run B of the two independent rounds the owner asked for on layer 1. ROUND 1.

Reviewed: memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md@3cfd547af6f355c5df687331f71a945f56a2e140

## Verdict: CLEAN WITH FIXES

No finding is a blocker. Four confirmed findings are high, in three items. They cover the roles kit's existing tag-to-role join, which the record calls absent; the shipped, ratcheted byte budgets, which the record also calls absent; and an instruction command that cannot tell the owner from an agent. Fix all three before the record is settled. Many medium and low items come from later layers (runtime, memory) that changed what this record states.

Review shape: intensity full, raw 47, confirmed 36, refuted 11, unverified 0 (0 uncertain), precision 0.77.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 7 | 5 | 2 | 0 | 0 | 0.71 |
| reuse | yes | 10 | 6 | 4 | 0 | 0 | 0.60 |
| blast-radius | yes | 7 | 4 | 3 | 0 | 0 | 0.57 |
| failure-envelope | yes | 14 | 12 | 2 | 0 | 0 | 0.86 |

Adjudicated tally by item: 32 items, of which 0 are blockers, 3 high, 19 medium and 10 low.

Adjudicated tally by raw confirmed finding: 36 findings, of which 0 are blockers, 4 high, 21 medium and 11 low.

Every confirmed finding keeps its binding grade. Items merge only findings that share a grade. Where one defect was confirmed at two grades, the two items point at each other.

Run integrity:

- Lenses: 5/5 returned, 0 died. Skeptic batches: 5/5 returned, 0 died.
- Demotions: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 34 judged sound, 2 judged unsound (ids 38 and 47, whose skeptic-corrected fixes are written below), 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 6 re-graded by the skeptic (ids 7, 13, 22, 38, 43 and 44, each from medium to low).
- Unverified findings: none, so 0 answered uncertain and 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 6 spec documents supplied as `specs`, as sibling context.
- Checklist: 11 items, each assigned to exactly one of 5 lenses (coherence 3, grounding 2, reuse 2, blast-radius 2, failure-envelope 2).
- By design: the caller's byDesign.
- Move check: no checked subject moved.

Every integrity count is zero where it should be, so the run is complete.

Eleven findings were refuted (ids 11, 15, 21, 23, 24, 25, 29, 31, 32, 35 and 37). Ids 11, 31 and 32 were refuted as duplicates of confirmed ids 18, 40 and 39, and those items carry their substance.

All addresses below are sections of the reviewed record unless another file is named.

## High

### H1. The roles kit's tag-to-role join is called absent, so R-B would build a second one (ids 10, 17)

- **Where:** [current] charter state (line 240), [fit] tag-system row (line 252), [uncovered] gap 1 (lines 264-268), [charter-today] 'Don't load what the reader never acts on' (lines 320-321), and [recommendations] R-B.
- **What is wrong:** The record says the charter's rule tags 'key the renderer and nothing else' and that 'no loader can select an agent's instructions by its role'. Both claims are false.
  - Each role file in tools/roles/agents/*.agent.md carries a `rules:` line. For example, gov-builder lists 'yagni, reuse, core, derive, verify, gate, security, bytes, cross-os?, tools'.
  - roles_lib.check_rule_tags (roles_lib.py:265-275) checks each tag against the charter's section-1 rule tags.
  - render_charter_blocks (:279-297) renders the cited lines under '### Charter rules', and handoff.py composes them into every role render.
  - [charter-today] also says the driver-only reach of [bytes] 'belongs in the work orders of the roles they bind', but the `rules:` lines already provide that reach.
- **Consequence:** R-B and gap-found-09 design a role join and an 'every tag used is registered' check from scratch, without naming the one that ships. dOrderedCharter would then build a second source of truth for which rules a role carries. Its re-keying of tags and sections would also break the existing join (see M10). The false gap is entered in the register, so it misleads every later build that reads it.
- **Fix (skeptic judged sound):**
  - Restate [current], [fit], gap 1 and gap-found-09: role scoping exists through each role's `rules:` line. roles_lib.check_rule_tags (check_roles R4) checks it, and roles_lib.render_charter_blocks renders it through handoff.py. What is missing is joins for step, item and policy.
  - In R-B, name roles_lib's join as the existing implementation of the `role` namespace, to be extended to the other namespaces rather than rebuilt.
  - Name that join's consumers: parse_charter's SECTION_ONE_RE and CARRIED_SECTIONS, check_rule_tags, and render_agents.py. Require dOrderedCharter's re-key to re-point them in the same unit.
  - Probe for the build: render the agents against a charter with '## 1.' renamed, and see the R0 refusal.
- **Left-shift gate:** Add a bug-class checklist entry: a gap claim that 'nothing does X' is grepped against tools/ before it is registered. A spec-lint could also require every [uncovered] gap to cite the probe that showed the absence.

### H2. Gap 2 says no load point has a budget, but ratcheted per-file budgets already ship (id 18)

- **Where:** [uncovered] gap 2 (line 270), the [fit] HOW MUCH row, and [recommendations] R-C.
- **What is wrong:** Gap 2 says 'No load point declares a budget or is measured; the 32 KiB cap binds the charter alone'. In fact tools/template-size-limits.txt declares six per-file ceilings, and check-template-size.sh enforces them as a gate leg. The ceilings are:
  - the template, 49152
  - the session-kickoff SKILL.md, 18432
  - AGENTS.md, 20480
  - BUILD-METHOD.md, 30720
  - UNATTENDED-PROTOCOL.md, 66860
  - the unattended SKILL.md, 10240

  The file also declares a spec class row of 49152, and template-size-highwater.txt ratchets the ceilings. The charter's binding budget is therefore 20480, not 32 KiB. The owner has already decided who may raise a row (TOOL-aOrientedCast-23).
- **Consequence:** R-C would create a second budget declaration and a second refusal, so one load point could carry two budgets that disagree. Its silence on raise authority reopens a question the owner has decided.
- **Fix (skeptic judged sound):** Rewrite gap 2 and the [fit] row: six load points already carry declared byte ceilings with an argued history and a high-water ratchet. What is missing is budgets over composed load sets, and line counts. R-C extends template-size-limits.txt with load-set rows or class rows, as the spec class row already does. R-C cites TOOL-aOrientedCast-23 for raise authority.
- **Left-shift gate:** The same checklist entry as H1, that absence claims cite their probe. A check could also refuse a design record that declares a byte budget for a path already listed in template-size-limits.txt without citing that file.

### H3. The instruction write path takes no proof that its caller is the owner (id 34)

- **Where:** [recommendations] R-I (lines 430-445), and [settled] Two policies, `instructions.edit` (lines 522-526).
- **What is wrong:** R-I says 'The owner uses it directly' and 'An agent only proposes'. But the write boundary validates only schema, tags, grammar, budgets and conflicts, and nothing checks who the caller is. v2 gives policy writes `policy.guard` and `policy.proof` (tty-cli, signed, both), but `instructions.edit` has no proof key. The runtime layer's `one-door` invariant routes every instruction change through this command, yet the command cannot tell the owner from an agent.
- **Consequence:** Any model session that can run the CLI, at least the attended driver, can add, edit or remove a level-0 MUST or NEVER unit and re-render every load set. An agent can therefore rewrite its own constraints, and the change lands as a recorded, valid owner-path change.
- **Fix (skeptic judged sound):** R-I states the boundary proof for the owner verbs. Either reuse `policy.proof` (an interactive terminal or a signature), or add `instructions.proof` beside `instructions.edit`. Agents get only a `propose` verb, which writes a proposal record. Add a fixture: a non-tty add, edit or remove invoked from an agent session is refused.
- **Left-shift gate:** Add a bug-class checklist entry: every owner-only write path names its caller proof. A spec check could refuse any policy key with an owner-command value that has no paired proof key.

## Medium

### M1. Reuse entries settled by the memory layer do not fit this record's grammar, ladder or manifest (id 1)

- **Where:** [recommendations] R-D (line 375), R-G level 3 (line 417), R-I (line 431) and R-A (owning kit).
- **What is wrong:** layer-memory.md:395-408 settles reuse entries as level-3 instruction units with strength MUST or SHOULD. Each lives in a per-feature `<feature>.reuse.toml` sidecar or in FOUNDATION, and changes only through R-I. This record allows none of that:
  - R-D allows only MUST, NEVER or ALWAYS.
  - R-G's level 3 holds only rendered methods, protocols and templates.
  - R-I has one manifest per kit, and R-A gives every unit an owning kit.
- **Consequence:** With `instructions.checks=refuse` as the default, the grammar check refuses every SHOULD reuse entry. A sidecar beside an adopter feature has no kit manifest to live in and no owning kit to declare. dTotalRecall's reuse delivery therefore cannot be written through R-I without changing this layer's code.
- **Fix (skeptic judged sound):** Fold the memory layer's settlement into this record:
  - R-D's directive type takes a declared strength set (MUST, SHOULD, NEVER, ALWAYS), or reuse entries are restated as MUST-only.
  - R-G's level 3 lists reuse entries and FOUNDATION conventions as hand-written units.
  - R-I names manifest homes beyond kits (feature sidecars and FOUNDATION), and a unit's owner can be a feature or a convention as well as a kit.
  - Probe for the build: plant a SHOULD reuse entry in a sidecar, run the instruction command's check, and see it accepted.
- **Left-shift gate:** Add a bug-class checklist entry: a later layer that settles a unit of an earlier layer's kind re-reads that layer's grammar and homes. This is the two-answers-to-one-question class.

### M2. R-B's 'every item has a unit' join conflicts with P11 and R-J on command items (id 2)

- **Where:** [recommendations] R-B joins (lines 353-354), against R-D/P11 and R-J.
- **What is wrong:** R-B requires every step, item and role to have at least one unit. In flow-steps.md, 35 of 55 items have actor `command` and 2 more have `command: the executor`. Command items get no work order, so no model reads a unit attached to them. P11 ('Prose that bears no load does not exist') and R-J's pruning forbid units that load nowhere.
- **Consequence:** The join reds on command items unless filler units are written. The Loop Review prunes those fillers, which turns the join red again. The two checks cannot both pass on a correct build.
- **Fix (skeptic judged sound):** Restrict R-B's item arm to items whose actor is a role, using the actor kind the loop declares. Command, hook, executor and owner items need no unit. Show the arm red on a role item with no unit, and green on a command item with none.
- **Left-shift gate:** Add a checklist entry: every completeness join states its domain against the declared actor kinds. A probe could run R-B's join over flow-steps.md before the record settles.

### M3. A unit scoped only by a descriptive namespace passes R-B and loads nowhere (id 3)

- **Where:** [recommendations] R-B namespaces (lines 349-353), against R-C's load-set selectors (lines 363-368).
- **What is wrong:** R-B accepts any of eleven namespaces as a unit's one required scope tag. R-C selects units only by top level, role, item, the step's practice reach and the item's policy values. A unit tagged only `kit`, `kind`, `record`, `principle` or `layer` passes the join, and no load set selects it. No check requires every unit to land in some load set.
- **Consequence:** A builder can register an instruction that never loads while every check is green. This is the fixture-passes-by-finding-nothing shape.
- **Fix (skeptic judged sound):** In R-B, separate selector namespaces (role, item, step, practice, policy, and level for the top level) from descriptive ones (layer, kit, kind, record, principle). Require every unit to carry at least one selector tag. Add a check that every registered unit appears in at least one derived load set, and see it red on a unit tagged only `kit.run-gates`.
- **Left-shift gate:** Make the orphan-unit check from the fix a gate leg of the instruction command.

### M4. P27's only enforcer can be switched off by a policy, which foundations C6 forbids (id 4)

- **Where:** [settled] Principles (P27's enforcing check, lines 503-508), and [settled] Two policies (`instructions.checks`, lines 518-521).
- **What is wrong:** [settled] names the load-set render check as P27's enforcer. It then makes that check's refusal switchable to warn or record, and v2 sets `velocity` to warn. foundations.md:290-291 (C6) says 'no switch turns a principle or its check off', and v2's P16 says principles are fixed.
- **Consequence:** Under the shipped `velocity` preset, an over-budget or incomplete load set renders, while the principle registry still records P27 as enforced. A check then certifies what it does not enforce, on a narrow but shipped path.
- **Fix (skeptic judged sound):** Choose one answer.
  - Either P27's render check always refuses, `instructions.checks` tunes only the non-principle checks (grammar style, manifest lint), and `velocity` loses warn for budgets.
  - Or P27 is restated so that refusal is a policy default, and the owner amends foundations C6.

  Have the meta-check refuse a principle whose only enforcer can be policy-set to a non-refusing mode.
- **Left-shift gate:** The meta-check rule in the fix is itself the gate.

### M5. No unit builds P28's enforcer, and 'layer' is not an extension kind (id 5)

- **Where:** [layers] ('Every layer fills one contract ... makes "extendable" a mechanism', lines 187-195), and [settled] P28's enforcer (line 508).
- **What is wrong:** The record makes a new expansion 'a filled contract' and names 'the layer contract's conformance gate' as P28's enforcer. But foundations C3's closed set of extension kinds has no 'layer', so a layer has no factory (C4) and no conformance gate (C5). dOrderedCharter's chain row (v2:732) ends at the layer register, the contract and the one-way check.
- **Consequence:** An expansion layer cannot be added through `new`, and C3's rule against unregistered kinds would refuse it. P28 is registered with an enforcer no build delivers. The meta-check would either go red on landing or be satisfied by the one-way check alone, which leaves contract conformance unchecked.
- **Fix (skeptic judged sound):** Add 'layer', with its contract, to C3's kinds through [settled]. Add 'the layer factory and the layer contract's conformance gate' to dOrderedCharter's planned units in v2 [chain]. Probe for the build: register a stub expansion through the factory with no code edit, and see the conformance gate red on a contract missing its extension-points field.
- **Left-shift gate:** Add a spec check that every enforcer a principle names appears in some chain row's planned units.

### M6. dOrderedCharter reads two policy keys whose reader lands in its child build (id 6)

- **Where:** [settled] Two policies (`instructions.checks`, `instructions.edit`), and the chain units placed on dOrderedCharter.
- **What is wrong:** The render check and instruction command that read these keys are dOrderedCharter units (v2:732). The policy file, its schema, its one reader, the presets and the guard/TTY CLI land with dDeclaredLoop (v2:733), which is dOrderedCharter's child. v2 [owed] does not weigh this read dependency.
- **Consequence:** When dOrderedCharter lands, its units can do one of two things, and both are wrong:
  - hard-code refuse and owner-command, which leaves `velocity`'s warn unimplemented;
  - add a second policy reader, which breaks P10's 'one policy file, one reader, one guard'.
- **Fix (skeptic judged sound):** State in [settled] how dOrderedCharter reads these keys before dDeclaredLoop exists. Either:
  - move the policy file, schema and reader into dOrderedCharter's core units, beside the `core.*` policies it already owns; or
  - record that dOrderedCharter ships with the defaults fixed and dDeclaredLoop wires the keys, with a test that flips `instructions.checks` to warn and sees the render pass with a warning.
- **Left-shift gate:** Add a chain-order check that every policy key a build's units read has its reader in that build or an ancestor.

### M7. Dropping the node registry from the loaded charter blanks the card's node cell (ids 12, 36)

- **Where:** [charter-today] 'Don't load what the reader never acts on' (line 319) and 'Don't name sections by provenance'.
- **What is wrong:** The record drops the node registry because 'the card already names the session's node', but the dependency runs the other way. The manifest's `registry:` key names AGENTS.md (memory/guides/SESSION-KICKOFF.md:10). manifest-check.sh derive_node_tag (lines 376-401) builds the card's `node —` cell from the first table under `## Node registry` in that file. The record names no new home for the registry, and none of the consumers that read the same table:
  - render_playbook.py's --claim-node (:1785-1790);
  - MANIFEST-TEMPLATE's {{REGISTRY_PATH}};
  - the runtime supervisor's facts.
- **Consequence:** If the table is removed or re-headed, every card prints 'node — UNKNOWN: no Machine/user cell ...' and still writes. Node identity, which also feeds claims, degrades silently in every session.
- **Fix (skeptic judged sound):**
  - Keep the registry's data in an unloaded, registered file. Re-point the manifest's `registry:` key and render_playbook's --claim-node to it in the same unit.
  - Keep the heading `## Node registry` until manifest-check's reader moves to the unit registry.
  - Name these consumers in the record or in dOrderedCharter's row.
  - Probe: point `registry:` at a charter with no node registry and see the card print UNKNOWN. Fixture: a card rendered after the move resolves this node.
- **Left-shift gate:** Add a bug-class entry: a retirement inventory names every reader by value (retirement-inventory-misses-readers-by-value). A gate could also refuse a card whose `node —` cell reads UNKNOWN.

### M8. The kit-to-layer table, which v2 defers to, contradicts the runtime layer (id 14)

- **Where:** [layers] kit table (lines 212-224) and runtime list (lines 140-146), and the last paragraph of [settled] (lines 537-538).
- **What is wrong:** v2:219 points to this record for 'the kit-to-layer map', and the map no longer agrees with the runtime layer:
  - It puts `next` in Flow's loop kit, though RT-3 (layer-runtime.md:19) and this record's own line 144 give it to Runtime.
  - 'unattended: the executor' and 'workflows: the always-spawn harness grows here' predate Runtime's supervisor, act sessions and [spawn].
  - runlog is filed as an Observability expansion, though the runtime layer moves the journal grammar into the core (layer-runtime.md:775).
  - [settled] still says Runtime gets a chain build 'once its layer review settles'. That build is now dWellOiledMachine.
- **Consequence:** A chain build that reads the map gets the wrong owner for `next` and for the journal grammar. It would file a core dependency under an expansion, which breaks the P28 one-way rule this record sets.
- **Fix (skeptic judged sound):** Amend the kit table and [settled] to the runtime layer's outcome: `next` and the controls in Runtime (RT-3), the journal grammar in the core, the executor owned by dWellOiledMachine, and the build named. Alternatively, move the kit-to-layer map into v2 [layers] and retire this copy.
- **Left-shift gate:** Single-source the kit-to-layer map as data, with a check that each kit appears under exactly one layer. The same defect was also confirmed at low grade from a reader's angle; see L6.

### M9. Six shipped instruction-layer gates are missing from the kit table, and R-D rebuilds one of them (id 19)

- **Where:** [layers] kit table, the [fit] 'HOW: no ambiguous prose' row, and [recommendations] R-D.
- **What is wrong:** This build's research-memory-tooling.md:51-60 classes the following gates as Instruction, and none appears in the record:
  - check-microformats.sh, which already grades a closed grammar over a fenced charter block;
  - check-line-length.sh, check-agent-cap-restatement.sh, check-playbook-parity.sh and check-placeholders.sh;
  - the format-guard hook (gate-legs.json:349-355).

  [fit] says 'no grammar, no check', and R-D designs a grammar checker from scratch.
- **Consequence:** R-D's checker would be built beside check-microformats.sh's existing fence-and-grammar mechanism. The kit table, which is the layer contract's inventory, would leave six instruction gates with no layer.
- **Fix (skeptic judged sound):**
  - Add the top-level instruction checks to the [layers] kit table under Instruction. Their verdict legs are check-template-size, check-microformats, check-line-length, check-agent-cap-restatement, check-playbook-parity, check-placeholders and the format-guard hook.
  - Restate the [fit] HOW row as 'one fenced grammar enforced (micro-formats); no grammar over the rest'.
  - In R-D, name check-microformats.sh as the seam the six-type grammar extends.
- **Left-shift gate:** Add a check that every leg in tools/gate-legs.json is assigned to exactly one layer in the kit map.

### M10. Retiring section numbers breaks the roles kit, which keys on '## 1.' (id 20)

- **Where:** [charter-today] 'sections are numbered', and [recommendations] R-B 'numbers are display order only'.
- **What is wrong:** The record retires the numbers but names no consumer that must migrate. roles_lib.py:61 has SECTION_ONE_RE = '^## 1\. ', and line 193 selects the rules by it. With no such heading and no legacy '## §n —' heading, lines 201-205 raise R0. render_agents.py:82's FIXTURE_DOC also uses '## 1. Practices'.
- **Consequence:** Built as written, check_roles, every handoff.py render and every typed-agent render refuse the charter. The failure is loud, but it blocks every role spawn path.
- **Fix (skeptic judged sound):**
  - In [charter-today] or R-B, list the consumers of the numbered section-1 heading: roles_lib.SECTION_ONE_RE with its R0 messages, and render_agents.py's FIXTURE_DOC.
  - Require dOrderedCharter to re-key them to the governing-practices section's tag in the same unit.
  - Probe: rename '## 1. Governing practices' in a scratch copy and run check_roles.py and handoff.py render to see R0. Run them again after the re-key.

  The skeptic found that the finder's list of consumers also named check-playbook-parity S4, wrongly but harmlessly. S4 forbids citing a section by number and does not key on the heading, so it needs no re-key.
- **Left-shift gate:** The retirement-inventory bug-class entry from M7. This defect shares its seam with H1.

### M11. R-B's core tag-name check depends on the lexicon, an expansion, which breaks P28 (ids 27, 45)

- **Where:** [recommendations] R-B ('the lexicon checks tag names', line 356), against the [layers] dependency rule (lines 181-182), the kit table (line 223) and [settled] P28 (line 504).
- **What is wrong:** R-B's joins are core, and dOrderedCharter builds them. One leg is 'the lexicon checks tag names', but:
  - the record's own kit table files lexicon under Knowledge, an expansion;
  - dMindYourWords builds the lexicon later in the chain (v2:161, 736);
  - v2:732 repeats the dependency.

  The record turns two other breaks of 'Core never depends on an expansion' into optional slots (:183-186), but not this one.
- **Consequence:** A core-only adopter either loses the tag-name check silently or fails its core check. P28's one-way dependency check must either flag the instruction layer itself or be given an exemption, and an exemption would certify one-way dependency where it does not hold.
- **Fix (skeptic judged sound):**
  - Give the core its own lexicon-free floor: a registered-name and grammar check for tag names in the tag registry.
  - State the lexicon's check as an optional extension slot that strengthens it, the way [layers] treats the builder's bug-class field and the scout's dossier field. List it among R-B's joins as optional.
  - Add the slot to the extension points the instruction layer's contract declares.
  - Probe: run the P28 dependency check over dOrderedCharter's declared dependencies with the lexicon kit absent, and see it pass.
- **Left-shift gate:** Run the P28 one-way dependency check over each layer record's named dependencies at design time, not only at build.

### M12. R-F keeps deploy-governance as a core Skill that the memory layer retires (id 28)

- **Where:** [recommendations] R-F core entries (lines 398-402).
- **What is wrong:** R-F lists 'deploy-governance: adoption' among its core Skill entries. The memory layer retires that Skill: layer-memory.md:266 says it has no reader and 0 loads and repeats govkit's verbs, :549 retires it, and :640 assigns the retirement to dConvergedCharter. v2:745 also gives dConvergedCharter 'Skills converged to level-4 thin entries'.
- **Consequence:** dConvergedCharter is told both to converge the Skill into a core thin entry and to retire it. R-F's 'declares its layer' check would carry a retired Skill.
- **Fix (skeptic judged sound):** Drop deploy-governance from R-F's core entries, and record that adoption is reached through govkit's own command. That command belongs to Distribution, an expansion, so it has no Skill. Alternatively, mark the entry superseded by the memory layer's [tools] verdict. Keep R-F's list in line with the tooling map's Retire rows.
- **Left-shift gate:** Add a cross-record check that no name on one layer's Retire rows appears in another layer's keep lists.

### M13. No layer declares which paths are instruction files, though Runtime's one-door guard needs that set (id 30)

- **Where:** [recommendations] R-A (line 342), R-E (lines 389-390) and R-I.
- **What is wrong:** Runtime's `one-door` invariant (layer-runtime.md:764) and its `coverage` fixture (:1000) refuse a direct write to an instruction file, but no record declares which paths those are. R-E makes the loop's checklists, role definitions, record schemas and policy catalogue the structured sources of instruction views. Those sources have their own write doors: `record`, the policy CLI, and `new` per kind.
- **Consequence:** If the guard covers only rendered targets, a direct edit to a structured source changes what agents load without passing the instruction command's validation. If it covers the sources, it collides with their own write doors. Either way the coverage fixture can pass on a set that misses instruction-bearing files.
- **Fix (skeptic judged sound):**
  - Have R-A/R-I declare the instruction path set as data the manifest renders: the rendered targets (AGENTS.md, CLAUDE.md, .claude/agents, Skills, rules) plus each kit's manifest.
  - State which structured sources stay under their own kind's write door, and that a change to one re-renders through the instruction command.
  - Expose the set as an extension point that the runtime hook pack reads.
  - Probe: a direct write to each path in the set, and to one structured source, each meets its declared door.
- **Left-shift gate:** Add a checklist entry: every guard names its path set as data owned by one layer.

### M14. R-H budgets the harness's memory index, which gov neither renders nor measures (id 39)

- **Where:** [recommendations] R-H (line 427), R-C, and R-K's Claude Code row (line 457).
- **What is wrong:** R-H makes the memory index 'a load point with a budget' and defers the mechanism to the memory layer. The memory layer settles only promotion through R-I (layer-memory.md:437-439). MEMORY.md is written by the harness's auto-memory to ~/.claude/projects/<slug>/memory/, outside the repository, with one copy per machine and per worktree slug. Here it is 13187 bytes. R-K's Claude Code row omits it.
- **Consequence:** R-C's 'the render refuses a set over budget' can never fire at this load point. The index keeps loading unmeasured on every node while the gap looks closed.
- **Fix (skeptic judged sound):**
  - State R-H's enforcement surface. Either a SessionStart or PreCompact check measures the harness's index for this worktree and records or refuses, or a setting disables auto-memory under gov.
  - Add the index to R-K's Claude Code row as a load point gov measures but does not render.
  - Add a fixture with an over-budget index that turns the check red.
- **Left-shift gate:** Add a checklist entry: every declared budget names the step that measures it.

### M15. R-K's Codex row budgets a file the override replaces, and splits harness load points across two kits (id 40)

- **Where:** [recommendations] R-K, Codex row (line 458).
- **What is wrong:** The row reads 'AGENTS.md within 32 KiB, plus the card's override file'. Three measured facts contradict it:
  - Codex reads AGENTS.override.md or AGENTS.md, one file per directory (research-orientation-preserve.md:29). A root override therefore replaces the charter rather than adding to it, and orientation.md:328-330 already sizes the override as the charter plus a full card.
  - Codex has no SessionStart (layer-runtime.md:719-721).
  - layer-runtime.md:743 gives 'how a harness loads instructions' to the harness adapters, while R-K gives per-harness load points to the instruction manifest.
- **Consequence:** The 32 KiB budget sits on a file that does not load. Nothing re-renders the override at session start, so the card goes stale. Adding a harness means touching two kits with no stated split between them.
- **Fix (skeptic judged sound):**
  - Restate the row: the override carries the charter plus the card, and the 32 KiB budget binds that combined file.
  - Name the override's writer, since there is no SessionStart: the card writer or the supervisor, on every card change.
  - Give R-K's render targets to the runtime harness adapter as the single extension point, or state which kit owns what.
- **Left-shift gate:** Add a checklist entry: every per-harness row cites the measured load behaviour from a research return.

### M16. R-D's grammar check is proven only on planted prose, not on the shipped defects (id 41)

- **Where:** [recommendations] R-D (line 385).
- **What is wrong:** The check's only acceptance criterion is 'seen red on planted prose'. The defects the record itself lists in [uncovered] 3 (lines 274-280) and [charter-today] (311-325) take other shapes: a provenance italic paragraph, numbered headings, a dangling pointer ('the marker below') and typed facts.
- **Consequence:** A check that is red on a planted line can still pass every one of those shapes. The gate would then certify today's charter while [uncovered] 3's defects still load.
- **Fix (skeptic judged sound):** Make R-D's red case the real tree. Run the check on today's rendered AGENTS.md and template, and require it to name each [uncovered] 3 and [charter-today] instance by line: the title, the provenance paragraph, '## 1. Governing practices', 'the marker below' and 'Worktrees: none yet'. Add planted cases only after that.
- **Left-shift gate:** Add a bug-class entry: a staged break uses the real defect, not a synthetic value (staged-break-substitutes-a-synthetic-value).

### M17. R-C's 'missing a required unit' has nothing to compare against, and warn mode's load is undefined (id 42)

- **Where:** [recommendations] R-C (line 371) and R-A (lines 335-343), and [settled] `instructions.checks` (lines 518-521).
- **What is wrong:** R-A's unit row has no field saying which units a role or item requires, so R-C's too-little refusal reduces to R-B's 'at least one unit'. Under `instructions.checks=warn` (the `velocity` preset), the record never says what an over-budget set loads.
- **Consequence:** A role whose work order loses its write-gate or return-format unit still renders green, provided one unit remains. Under `velocity`, each builder picks its own truncation, so the loaded content differs per harness and per run.
- **Fix (skeptic judged sound):**
  - Add a `required` relation to R-A's row. Either a role or item declares its required unit tags, or a unit declares itself mandatory for its scope. The too-little check compares against that relation.
  - Define the warn behaviour. Either load the whole set and record the overage, or cut by level and then by budget class and record the cut units.
- **Left-shift gate:** Add a fixture that removes a required unit from a role and sees the render refuse.

### M18. R-J prunes on unit citations that no return schema carries (id 46)

- **Where:** [recommendations] R-J (line 448), and [settled] chain rows (lines 533-535).
- **What is wrong:** R-J needs returns and findings to cite the unit tags they followed or broke. No chain row gives the roles' return schema that field; only v2's dCalibratedLens row (line 744) assumes it exists. 'Followed' is also self-reported by a model and cannot be checked.
- **Consequence:** Either nothing populates the signal and gap-found-16 cannot close, or the Loop Review prunes on self-reported citations. In the second case, a load-bearing unit that agents obey without citing would be removed.
- **Fix (skeptic judged sound):**
  - Add a chain row: dBoundRoles' return schema carries `units.broke`, which is machine-checkable against findings and refusals, and `units.cited` if that is kept.
  - State that pruning acts only on mechanically observed signals: a unit loaded and never cited across N runs, with no refusal referencing it.
  - State that pruning goes through the owner write path and is never automatic.
- **Left-shift gate:** Add a spec check that every signal a measurement consumes has a producing field in some chain row.

### M19. R-D does not say how handed content in a work order is fenced off from directives (id 47)

- **Where:** [recommendations] R-D ('Every loaded unit is one of six types', line 374) and R-A (work orders assembled from units, line 345).
- **What is wrong:** layer-roles (line 175 and its [trust] section) puts handed content into the level-6 task block: record fields, code excerpts and findings, keyed and classed. This record never says three things about that content:
  - whether it is outside the grammar;
  - how it is budgeted;
  - how it is marked as data inside the work order's own envelope.
- **Consequence:** If the grammar check covers the whole work order, it refuses every order that quotes evidence. If it covers only units, quoted 'MUST' or 'NEVER' text reaches the agent unchecked and reads as a directive. That is the injection path that foundations' data-envelope rule exists to close.
- **Fix (skeptic judged UNSOUND; this is the skeptic's corrected fix):** Leave the six statement types intact, since P11's six types are owner-ratified in [settled]. State that R-D's grammar applies to units only, and that handed content is not a unit. Handed content is carried as data: each fact sits in its own data envelope, bearing the key and class from roles [trust], and counts toward the load point's budget. Add a fixture: 'NEVER push' quoted inside a handed-content envelope passes the grammar check and is not treated as a directive, and the same text outside any envelope in the work order is refused.
- **Left-shift gate:** Make the fixture above a leg of the instruction command's check.

## Low

### L1. A policy value's level is ambiguous between R-G and the charter's level-0 envelope (id 7)

- **Where:** [recommendations] R-G (level 2, line 415), against R-A (lines 344-345) and v2 [front-door] (lines 374-385).
- **What is wrong:** R-G puts policy values at level 2, but the charter renders the preset and overrides inside its level-0 envelope. R-A does not say whether a unit keeps its own level inside a document's envelope.
- **Consequence:** Builders of the envelope gate and of the load-set render may disagree. The skeptic re-graded this finding from medium to low: both renderings come from the one policy file, so the values cannot actually conflict.
- **Fix (skeptic judged sound):** State in R-A that a unit keeps its own level wherever it renders, and that an envelope carries the highest level among its units plus per-unit level markers. Alternatively, have the charter render only a pointer to the policy values, never the values. Add a check that every rendered unit's level marker matches its registry row.
- **Left-shift gate:** The level-marker check in the fix.

### L2. R-B's example item tags do not match the settled loop (id 8)

- **Where:** [recommendations] R-B, example item tags (line 357).
- **What is wrong:** `plan.intake` and `build.unit-commit` come from the research item audit. The settled loop names those items `plan.input` (flow-steps.md:67) and `build.unit-pass` (:156).
- **Consequence:** The defect is cosmetic, unless a builder seeds the tag registry or a fixture from the examples.
- **Fix (skeptic judged sound):** Replace the examples with `plan.input` and `build.unit-pass`, or cite flow-steps as the source of item tags.
- **Left-shift gate:** Add a lint that every backticked item tag in a layer record resolves in flow-steps.md.

### L3. No chain unit moves guide explanation into `help/` before the guides retire (id 9)

- **Where:** [recommendations] R-E (line 393).
- **What is wrong:** R-E sends human explanation to `help/`, which today holds only README.md and roles.md. dConvergedCharter's row (v2:745) retires the hand-written guides and names no destination for their rationale.
- **Consequence:** The explanatory prose in roughly 409 KB of guides can be dropped, and no unit is accountable for carrying it over.
- **Fix (skeptic judged sound):** Add 'explanation moved to `help/` before each guide retires' to dConvergedCharter's planned units. Add a check that no guide is deleted while a section of it maps to no view and no `help/` page.
- **Left-shift gate:** The section-mapping check in the fix.

### L4. The session-start Skill load point is mis-inventoried (id 13)

- **Where:** [current] session-start row (line 232), [uncovered] gap 5 (line 289), and [recommendations] R-F.
- **What is wrong:** The record counts 'nine Skill descriptions', but the load point actually lists:
  - seven project Skills from .claude/skills;
  - session-kickoff, as a user-level symlink into the main checkout;
  - ten non-gov user Skills.

  deploy-governance is not installed at all.
- **Consequence:** The budgeted point holds at least 18 descriptions, and gov cannot budget the foreign ones. In a worktree, session-kickoff resolves to the main checkout's copy rather than the worktree's. The skeptic re-graded this finding from medium to low: R-F's per-Skill budget still works for gov's own entries.
- **Fix (skeptic judged sound):** Re-measure the point as what the harness lists, which is project, user-level and plugin Skills, and name gov's share. In R-F and R-C, state that the budget covers gov's own descriptions only, and that foreign entries are a share of the point gov cannot budget.
- **Left-shift gate:** Add a checklist entry: a load-point inventory is measured from the harness's own listing.

### L5. Stale counts in [fit] and R-E (id 16)

- **Where:** [fit] policies row (line 249) and [recommendations] R-E (line 391).
- **What is wrong:** The record says '94 keys' and 'P1 to P26 fixed', but v2 now has 119 catalogue rows and P27 to P30. R-E's '67 KB whole' names UNATTENDED-PROTOCOL.md, but the largest guide is UNATTENDED-VERBS.md at 85,684 bytes.
- **Consequence:** Readers who size the policy surface or the trigger-read slice get understated figures. Behaviour is not affected.
- **Fix (skeptic judged sound):** Replace the counts with pointers to v2 [policies] and [principles], or re-measure them. Cite the 86 KB maximum in R-E.
- **Left-shift gate:** Add a checklist entry: counts of another record's contents are pointers, never typed numbers.

### L6. Stale Runtime and kit claims stand after the later layers settled (ids 26, 33)

- **Where:** [layers] kit table, and [settled] 'v2 [owed]' (lines 537-538).
- **What is wrong:** Several claims are stale or contradict each other:
  - [settled] still says 'Runtime gets its own chain build at the re-cut, once its layer review settles', though v2:168 and :737 name dWellOiledMachine.
  - Line 144 lists `next` under Runtime, while line 214 files it under Flow.
  - process-monitor is 'supervision' (line 221), but the runtime layer gives supervision to unattended and reaping to process-monitor.
  - runlog is Observability-only, though the journal grammar moved into the core.
  - Knowledge still lists 'the reuse lookup' (line 158), which layer-memory.md:548 retires.
- **Consequence:** A reader takes the wrong owner for `next`, supervision and the journal grammar, and believes Runtime's build is undecided. v2 and the runtime record carry the truth, so no behaviour ships wrong.
- **Fix (skeptic judged sound):** Add a dated supersession note under [layers] and [settled], pointing at layer-runtime's [settled] section and v2's chain row. The note states:
  - `next` is Runtime's verb over Flow's position function (dWellOiledMachine);
  - supervision belongs to unattended, and process-monitor reaps;
  - the journal grammar is in the core;
  - the reuse lookup is retired (memory F4-3);
  - Runtime's build is dWellOiledMachine.
- **Left-shift gate:** Add a bug-class entry, amendment-leaves-its-other-half-standing: settling a later layer greps the earlier records for the deferral it answers. The kit-map defect is also confirmed at medium grade from the chain-build angle; see M8.

### L7. 'Worktrees: none yet' is an ambiguous label, not a stale fact, and the existing derive-at-render seam goes unnamed (id 22)

- **Where:** [charter-today] 'Don't type facts that go stale' (line 315) and [uncovered] gap 3 (line 279).
- **What is wrong:** The line renders {{WORKTREE_SCRIPT}}, which playbook.kit.toml:228-230 declares as 'the one script that bootstraps a sibling worktree'. 'None yet' therefore means no bootstrap script exists, which is still true. Derive-at-render already exists as render_playbook.PROBES (:562) and the registry's `probe =` rows, and the record does not name them.
- **Consequence:** gap-found-11 records something that is not a defect, and its prescription invites a live worktree count in level-0 text. The skeptic re-graded this finding from medium to low: the rule still stands on the trailer-model example.
- **Fix (skeptic judged sound):** Drop the worktrees example from [charter-today] and gap 3, or restate it as an ambiguous label: the fact names a script, while the label reads as a state. Name render_playbook.PROBES and the registry's `class = "asked"` versus `probe = ...` rows as the mechanism that R-D's 'fact, derived, with its source' type extends.
- **Left-shift gate:** Add a checklist entry: a cited defect example is traced to its placeholder's declared meaning.

### L8. Foundations R2 still uses the old rank numbering, and R-A sends builders there (id 38)

- **Where:** [recommendations] R-G and [settled] The ladder, reached through R-A (line 345).
- **What is wrong:** The ladder now puts the card at level 1 and retires the special rule. Foundations R2, which R-A cites for envelopes, still says 'inside the rank-1 envelope' (:82), 'only the charter holds rank 1' (:91) and 'rank 0 is the platform' (:95). It carries no supersession note.
- **Consequence:** A builder who follows R-A into foundations R2 builds an envelope gate that either refuses the card at level 1 or keeps the retired rule. The skeptic re-graded this finding from medium to low: v2's body and chain row already use levels, and v2's hits are dated revision-log history.
- **Fix (skeptic judged UNSOUND; this is the skeptic's corrected fix):** Add a dated supersession note to foundations R2 and its ladder that maps rank to level: the charter is level 0, the card is level 1, and the platform sits above the ladder. Have R-G or [settled] cite that note. State the envelope gate's predicate as 'only the charter holds level 0; only the card holds level 1'. Leave v2's dated revision-log entries unchanged.
- **Left-shift gate:** The retirement-inventory bug-class entry from M7, applied to renumbered values.

### L9. R-I's write boundary does not re-check referential integrity on remove, rename or prune (id 43)

- **Where:** [recommendations] R-I (remove verb, lines 433-440), R-J (pruning, lines 448-449) and R-B (joins).
- **What is wrong:** The boundary validates schema, tags, grammar, budgets and same-level conflicts. It does not re-run R-B's joins or check inbound pointers on removal, and the record defines no lifecycle for renaming or retiring a tag.
- **Consequence:** A removal or prune can strand pointer units or citing records, and they are caught later and less precisely, if at all. The skeptic re-graded this finding from medium to low: 'every tag used is registered' and R-C's render refusal partly cover the case.
- **Fix (skeptic judged sound):**
  - Add to R-I's boundary: the R-B joins re-run on the post-change registry, and no inbound pointer may name a removed tag.
  - Require a rename to rewrite or alias every referrer.
  - Define tag retirement: a tag retires with an alias, and a tag that records cite is never deleted.
- **Left-shift gate:** A fixture that removes a pointed-to unit and sees the write refused.

### L10. R-I's lock does not reconcile renders and the change record across clones (id 44)

- **Where:** [recommendations] R-I ('merge deterministically ... under a lock', lines 431-432).
- **What is wrong:** One lock is the only concurrency rule, yet the product runs on several machines and in many worktrees. The record never says how rendered views and the change record reconcile at merge.
- **Consequence:** Concurrent edits conflict in generated text or fork the change history. The skeptic re-graded this finding from medium to low: the merge bar's render-parity legs would likely catch a stale render.
- **Fix (skeptic judged sound):** State that the lock is per clone only. Rendered views are never merged by hand; they are re-rendered after merge, and a post-merge or gate check byte-compares the render against the manifests. The change record is append-only with per-change ids, so it merges cleanly.
- **Left-shift gate:** Add the render byte-compare check from the fix as a bar leg.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=47 confirmed=36 refuted=11 unverified=0 blocker=0 high=4 medium=21 low=11 agents=11 out-tokens=248455

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-D (directive types), R-G (level 3 row), R-I (one manifest per kit), R-A (owning kit) | medium | medium | confirmed | I confirmed the record is at the pinned blob 3cfd547a. R-D at :375 allows only 'MUST, NEVER or ALWAYS', R-G level 3 at :417 holds only rendered methods, protocols and templates, R-I at :431 has 'one manifest per kit', and R-A gives every unit an 'owning kit'. layer-memory.md:395-408 settles reuse entries as level-3 units with 'strength (MUST or SHOULD)', homed in a `<feature>.reuse.toml` sidecar or FOUNDATION, and changed only through R-I. A grep for SHOULD across build/*.md hits only layer-memory.md:396. The later layer's settlement contradicts this record's grammar and manifest home. | sound | two-answers-to-one-question |
| 2 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-B joins ('every step, item and role has at least one unit') against R-D/P11 and R-J | medium | medium | confirmed | I re-ran the actor count over flow-steps.md. Of 55 items, 35 have actor 'command', 2 'command: the executor', and 3 more are other command forms (the bar, the lander, the prompt-submit hook). The [rules] section of flow-steps loads a load set per work order, and command items get no work order. R-B at :353-354 requires every item to have at least one unit. P11 (v2:255-257, 'Prose that bears no load does not exist') and R-J ('prunes units that bear no load') forbid units that load nowhere. So the join and the pruning conflict on command items. | sound | - |
| 3 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-B (namespaces, 'every unit carries at least one scope tag') against R-C (load-set selectors) | medium | medium | confirmed | R-B (:349-353) lists eleven namespaces and requires only 'at least one scope tag'. R-C (:363-368) selects units by top level, role, item, the step's practice reach and the item's policy values only. P13 (v2:308) counts 'layers' among scope tags, but no load-set rule selects on layer. No check that every unit lands in some load set appears in R-B, R-C or the dOrderedCharter row (v2:732). A unit tagged only layer.* or kit.* therefore passes the join and loads nowhere. R-J's later pruning is a measurement, not a refusal at registration. | sound | - |
| 4 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[settled] Principles (P27's enforcing check) and [settled] Two policies (`instructions.checks`) | medium | medium | confirmed | [settled] at :503-508 names the load-set render check as P27's enforcer. :518-521 makes that check's refusal switchable (refuse, warn, record), and v2:642 sets `instructions.checks` to warn in the first preset column. foundations.md:290-291 C6 says 'no switch turns a principle or its check off', and v2 P16 says 'Principles are fixed: policies tune behaviour inside them'. Under that preset the only enforcer of P27 refuses nothing, while the registry still records P27 as enforced. The settled answer contradicts the foundations record, which the BY DESIGN block allows a finding to show. | sound | two-answers-to-one-question |
| 5 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[layers] 'Every layer fills one contract ... makes "extendable" a mechanism'; [settled] P28's enforcer ('the layer contract's conformance gate') | medium | medium | confirmed | The record (:187-195) makes a new expansion 'a filled contract', and :508 names 'the layer contract's conformance gate' as P28's enforcer. foundations.md C3 lists kit, command, governing document, policy key, preset, gate leg, role, workflow, hook, Skill, practice, record kind and stage, with no layer. My grep for 'conformance gate' across v2 and the layer records finds kit and record-kind gates but no layer gate. The dOrderedCharter row (v2:732) ends at 'the layer register, the layer contract and the check that the core never depends on an expansion'. No build delivers the named enforcer or a layer factory. | sound | - |
| 6 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[settled] Two policies (`instructions.checks`, `instructions.edit`) and the chain units placed on dOrderedCharter | medium | medium | confirmed | v2:732 puts the dOrderedCharter units that read `instructions.checks` and `instructions.edit` on dOrderedCharter, whose parent is dClosedLoop. v2:733 puts `.governance/policy.toml`, the schema, the one reader, the presets and the guard/TTY CLI on dDeclaredLoop, whose parent is dOrderedCharter. v2:254 P10 requires 'One policy file, one reader, one guard'. The [owed] items at v2:795-812 cover only Flow-first versus instruction-first and kit confs, not this read dependency. Neither this record nor v2 says how the earlier build reads these keys. | sound | - |
| 7 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-G (level 2: 'the loop and the policy values') against R-A (the charter assembled from units) and v2 [front-door] | medium | low | confirmed | R-G at :415 puts 'the loop and the policy values' at level 2. v2 [front-door] (:374-385) puts the charter's whole content in the level-0 envelope, including 'the repository's current preset and overrides'. R-A (:344-345) assembles documents from units and wraps them in envelopes, but says neither whether a unit keeps its own level nor what an envelope over mixed-level units carries. Graded low: both renderings come from the one policy file, so the values cannot actually disagree. The defect is an ambiguous rule for builders, not a live conflict. | sound | two-answers-to-one-question |
| 8 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-B, example item tags | low | low | confirmed | A grep for plan.intake and unit-commit across memory/builds/dClosedLoop hits only layer-instruction.md:357, research-flow-items-a.md and review instruction-a. flow-steps.md:67 declares `plan.input` and :156 declares `build.unit-pass`. The example tags name items the settled loop does not declare. The effect is cosmetic. | sound | two-answers-to-one-question |
| 9 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-E ('Explanation for humans lives outside every load set, under `help/`') | low | low | confirmed | A grep for 'help/' across the dClosedLoop build records hits only layer-instruction.md:393. `ls help` lists only README.md and roles.md. The dConvergedCharter row (v2:745) retires 'the hand-written guides' without naming a destination for their explanatory prose. A grep for 'explanation', 'rationale' and 'for humans' across v2, the overview and foundations finds no owner. No chain unit carries R-E's human-explanation half. | sound | - |
| 10 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[current] charter state (line 240); [fit] tag-system row (line 252); [uncovered] gap 1 (lines 264-268); [recommendations] R-B; [charter-today] 'Don't load what the reader never acts on' (lines 320-321) | high | high | confirmed | The tree contradicts the record's claim that the charter's tags 'key the renderer and nothing else' and that no loader can select by role. tools/roles/agents/*.agent.md carry `rules:` lines; for example, gov-builder has 'yagni, reuse, core, derive, verify, gate, security, bytes, cross-os?, tools' and gov-skeptic has 'verify, class, risk'. roles_lib.render_charter_blocks (:280-297) selects the section-1 rule lines those tags cite. .claude/agents/gov-skeptic.md:36-38 carries '### Charter rules' with '[verify]'. roles_lib.py:61 SECTION_ONE_RE = '^## 1\. ', :67 CARRIED_SECTIONS = ('Protocols', 'Facts'), and :200-202 raises R0 on a charter with neither. AGENTS.md still has '## 1. Governing practices'. The record, v2 and the roles layer never name this existing join, so R-B would design a second one, and re-keying the charter's sections would break the roles render. | sound | - |
| 11 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[uncovered] gap 2 (lines 269-273); [fit] HOW MUCH row (line 255); [recommendations] R-C | medium | - | refuted | duplicate of id=18. The premise does hold on re-probe. tools/template-size-limits.txt carries rows for the template 49152, AGENTS.md 20480, two SKILL.md files, BUILD-METHOD.md 30720 and UNATTENDED-PROTOCOL.md 66860, plus a spec class row. gate-legs.json names check-template-size.sh in several legs, and the script's head records the 32->48 KiB owner move. The record's gap 2 line 270 still says 'No load point declares a budget'. But id=18 reports the same false gap, against the same sections, with the same consequence of a parallel budget. | sound | - |
| 12 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[charter-today] 'Don't load what the reader never acts on' (line 319) | medium | medium | confirmed | memory/guides/SESSION-KICKOFF.md:10 reads 'registry: AGENTS.md'. manifest-check.sh derive_node_tag (lines 376-401) builds the card's `node —` cell from the first table under '## Node registry' in that file. When nothing matches it prints 'node — UNKNOWN: no Machine/user cell ...' and still writes the card. AGENTS.md:102 and template:101 carry that section, and render_playbook.py:1785-1790 refers to it too. So the card names the node only because the registry loads, which is the reverse of what record line 319 implies. The record names none of these consumers. | sound | - |
| 13 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[current] session-start row (line 232); [uncovered] gap 5 (line 289); [recommendations] R-F | medium | low | confirmed | .claude/skills holds 7 Skills. ~/.claude/skills holds 11 entries: session-kickoff is a symlink to /c/projects/coding-governance/skills/session-kickoff, and the other 10 are non-gov Skills. deploy-governance is not installed at either level. The session-start load point therefore lists 8 gov descriptions plus at least 10 foreign ones, not the 'nine Skill descriptions' at line 232, and the record never says the foreign share exists. Graded low: this is a mis-inventory in the record's account, and R-F's per-Skill description budget still works for gov's own entries. | sound | - |
| 14 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[layers] kit table (lines 212-224) and runtime list (lines 140-146); [settled] last paragraph (lines 537-538) | medium | medium | confirmed | The record's kit table line 214 puts `next` in Flow's loop kit. Line 219 has 'unattended: the executor' and line 224 files runlog as an Observability expansion. The runtime layer contradicts all three. layer-runtime.md:19 says Runtime owns the `next` verb (RT-3). Its line 775 has unattended as the supervisor whose verbs become next/run, and 'the journal grammar, moved from runlog into the core'. [settled] line 537 still says Runtime gets a chain build 'once its layer review settles'. v2 now names that build, dWellOiledMachine (v2:168, 737, 775), and v2:219 points to this record for the kit-to-layer map. | sound | - |
| 15 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-G level-1 row (line 414) | low | - | refuted | The finding is graded low and I cannot establish it. OR-5's own words are 'A build orientation card should be priority 1 along the charter'. Under L3 the card sits at level 1, so the literal 'priority 1' does match. Line 414 also says outright that 'the charter outranks it by level alone and the special rule retires', so the record already acknowledges the change from equal rank. Whether 'along' meant equal rank is an interpretation. Recording the supersession in orientation.md is a preference about a record outside the subject. | sound | - |
| 16 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[fit] policies row (line 249); [recommendations] R-E (line 391) | low | low | confirmed | An awk count of '\| `' rows in v2 [policies] (lines 405-531) prints 119, against the record's '94 keys'. v2 defines P27 to P30 (lines 115, 140, 153, 329, 358), against '[fit] P1 to P26 fixed'; the record's own [settled] adds P27 and P28. wc -c puts UNATTENDED-VERBS.md at 85684, the largest guide, so R-E's '67 KB whole' understates the maximum. These are stale counts in the record's account, with no behavioural effect. | sound | - |
| 17 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[current] charter state; [uncovered] gap 1; [recommendations] R-B | high | high | confirmed | tools/roles/agents/*.agent.md carry `rules:` front-matter, e.g. 'gov-builder ... rules: yagni, reuse, ...'. roles_lib.py:265-275 checks each tag against the charter's section-1 rule tags and reports 'rules tag ... names no section 1 rule'. render_charter_blocks (:279) renders the cited rule lines under '### Charter rules'. handoff.py:13-15 composes them into every role render. So the charter's tags do feed role-scoped selection. The record's lines 240 ('key the renderer and nothing else') and 267-268 ('no loader can select an agent's instructions by its role') are false. R-B designs a fresh role join and an 'every tag used is registered' check without naming this seam. That will mislead dOrderedCharter into building a second join. | sound | - |
| 18 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[uncovered] gap 2; [fit] HOW MUCH row; [recommendations] R-C | high | high | confirmed | Re-probed: grep -v '^#' tools/template-size-limits.txt prints six per-file ceilings: the template 49152, session-kickoff SKILL.md 18432, AGENTS.md 20480, BUILD-METHOD.md 30720, UNATTENDED-PROTOCOL.md 66860 and the unattended SKILL.md 10240. It also prints the spec class row 49152. check-template-size.sh enforces them, gate-legs.json lists it, and its head records the owner's 32->48 KiB move. The sibling layer-runtime.md:904-905 already budgets against these size legs. The record's line 270 ('No load point declares a budget ... the 32 KiB cap binds the charter alone') is false. R-C designs a parallel budget and refusal without naming the existing one, which will mislead the build. | sound | - |
| 19 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[layers] kit table; [fit] 'HOW: no ambiguous prose' row; [recommendations] R-D | medium | medium | confirmed | A grep of the subject for microformat, line-length, parity, placeholder, format-guard, template-size and restatement hits only line 329, which is about the micro-formats themselves. Yet tools/check-microformats.sh ('grade the charter's micro-format DEFINITIONS against their own grammar'), check-line-length.sh, check-agent-cap-restatement.sh, check-playbook-parity.sh and check-placeholders.sh all exist. gate-legs.json:349-355 carries format-guard. This build's research-memory-tooling.md:51-60 classes them as Instruction. The kit table leaves these out. [fit] says 'no check', and R-D builds its grammar checker without naming the closed-grammar seam that check-microformats already provides. | sound | - |
| 20 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[charter-today] 'sections are numbered'; [recommendations] R-B 'numbers are display order only' | medium | medium | confirmed | roles_lib.py:61 has SECTION_ONE_RE = '^## 1\. ', and line 193 selects section 1 by it. Lines 201-205 raise R0 when no rule tag is found and no '## §n — ' heading exists. AGENTS.md:12 is '## 1. Governing practices', and render_agents.py:82's FIXTURE_DOC uses '## 1. Practices'. The owner's direction to retire section numbers (record line 58) would therefore make the roles kit refuse the charter, and the record names no consumer to migrate. Fix: it cures the defect, though one consumer it lists is wrong. check-playbook-parity S4 forbids citing a charter section by number (line 14). It does not key on the numbered heading, so it needs no re-key; listing it is harmless. | sound | - |
| 21 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-D 'Render provenance lives in a sidecar lock, never in loaded text' | medium | - | refuted | Premise false on re-probe. The impact says five tools read the version marker "from the loaded charter", and that moving it breaks lockstep and parity checking. That is not what the code does. check-placeholders.sh:29,58-70 greps $TEMPLATE=coding-governance-agents.template.md. check-playbook-parity.sh:270 reads $TEMPLATE. render_playbook.py:1000 searches the template text read at :998. govkit.py:2221 is a comment about the descriptor's version_from.kind exemption. None of these read the rendered AGENTS.md, so moving provenance out of rendered/loaded text leaves lockstep and parity untouched. The only reader of a rendered marker is session-kickoff SKILL.md:87. It is an engine-only fallback used when no manifest exists, and it greps instantiated docs. Saying the record does not name govkit's install.json receipt is reuse detail for the build's own spec (BY DESIGN). The receipt is per-install while render provenance is per-render, so no duplication defect is shown. | unsound | - |
| 22 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[charter-today] 'Don't type facts that go stale'; [uncovered] gap 3 | medium | low | confirmed | Re-probed. AGENTS.md:173 reads 'Worktrees: none yet — worktrees are created by hand under .claude/worktrees/.' It renders template:196 '{{WORKTREE_SCRIPT}}'. playbook.kit.toml:228-230 declares that key class="asked", why "the one script that bootstraps a sibling worktree". So 'none yet' means no bootstrap script exists, which is still true. It is an ambiguous label, not a stale fact, yet [charter-today] and gap 3 (record :279, :315) both cite it as a stale typed fact beside 13 worktrees. render_playbook.py:562 PROBES and the registry's probe rows (:866) are an existing derive-at-render seam, and the record does not name them. The rule 'don't type facts that go stale' still stands on the trailer-model example, so the effect is limited to a misdiagnosed example. | sound | - |
| 23 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[uncovered] gap 8; [recommendations] R-J | medium | - | refuted | prose.py:1-14 measures narration, interjections and BUILD/SPEC pair emission. It is report-only ("Nothing here writes, gates or prints message text") and keyed to the micro-format fence. It records no unit tags and nothing about which units were loaded, followed or broken, so gap 8's 'Nothing records which units an agent loaded, followed or broke' holds at unit granularity. The feared duplicate transcript predicate is not what the design builds. v2:744 states dCalibratedLens's mechanism as 'instruction effectiveness measured from returns and findings that cite unit tags', not a transcript adherence measure. No defect is established. | sound | - |
| 24 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-K | medium | - | refuted | adopt-agent-instructions.sh:2-10 installs ONE canonical AGENTS.md and wires each alias (GEMINI.md, .github/copilot-instructions.md, .cursorrules, .windsurfrules) to it as a pointer, symlink or synced copy, so every 'rest' harness loads AGENTS.md's content. R-K's 'The rest \| AGENTS.md' is accurate for what is loaded, and nothing in R-K retires the alias wiring. The record's [layers] table (:210) already assigns the per-harness render targets to agent-instructions, so R-K does not disagree with it. A regression of the alias outputs is not shown. | sound | - |
| 25 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-I | medium | - | refuted | R-I (:430-445) sets the mechanism at design level: one manifest per kit, merged with the adopter's overlay, and one command. [layers] (:209,:211) already places playbook as the core engine that renders the charter and roles as the core engine for definitions. Naming render_playbook.py, --check and roles_lib.render_role's house overlay (roles_lib.py:569-581, observed) as the seams to extend is unit-spec reuse detail that the BY DESIGN block leaves to each chain build. The house overlay is the adopter's overlay for roles, which R-I's merge generalises. A second, conflicting level-5 override mechanism created by the design as written is not shown. | sound | - |
| 26 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[settled] 'v2 [owed]' | low | low | confirmed | Record :537-538 still reads 'v2 [owed]: Runtime gets its own chain build at the re-cut, once its layer review settles what that build holds.' The later runtime layer settled that build: v2:168 'The chain gains dWellOiledMachine, Runtime's own build', and v2:737 carries the chain row. The task counts a statement that a later layer changed as a finding. The clause now reads as an open deferral, while v2's rows are correct. | sound | amendment-leaves-its-other-half-standing |
| 27 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-B (with [settled] Principles, P28) | medium | medium | confirmed | Record :356 lists 'the lexicon checks tag names' among R-B's joins, which are checked both ways and built by dOrderedCharter. :223 files lexicon under Knowledge, an expansion, and :181 says 'Core never depends on an expansion'. The record turns the two other breaks of that rule into optional slots (:183-186) but not this one. v2:732 repeats 'its names checked by the lexicon' in dOrderedCharter's core row, and v2:161/736 has dMindYourWords, the lexicon's build, as a child of dTotalRecall, later in the chain. lexicon.md:26-27 says 'The core never depends on it (P28)'. Built as written, the P28 one-way dependency check (:508) meets a core check that names an expansion. The effect is contained to the tag-name check and the dependency gate's verdict. | sound | - |
| 28 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-F (core entries) | medium | medium | confirmed | Record :398-402 lists 'deploy-governance: adoption' among R-F's core Skill entries. The later memory layer retires that Skill: layer-memory.md:266 'the deploy-governance Skill has no reader and 0 loads, and repeats govkit's verbs', :549 '\| Retire \| the deploy-governance Skill \|', and :640 names gap 5's owner as dConvergedCharter. v2:745 gives dConvergedCharter 'Skills converged to level-4 thin entries', so the same build is told both to keep the Skill as a core entry and to retire it. That is a later-layer contradiction that misleads the build. | sound | - |
| 29 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[current], [recommendations] R-C and R-K | medium | - | refuted | The cited sections already cover it. R-A (:344) says 'a work order [is] each assembled from units by their tags', and R-C (:369-371) states as a general rule that 'Each load point declares a budget', with the render refusing over-budget or missing-unit sets. A work order cut through dBoundRoles' renderer (runtime :371) is such a rendering, and the act session is a load point under that rule. Runtime :774 lists the act session's static block as an instruction unit, so it falls under R-A as well. [current] measures today's load points, and act sessions do not exist yet, so leaving them out of that table is correct. Mapping a refusal to `next`'s outcomes is runtime's own concern, not something this layer omits. | sound | - |
| 30 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-A, R-E and R-I | medium | medium | confirmed | layer-runtime.md:764 states the one-door invariant 'instructions only through the instruction command', and :1000 adds the coverage fixture 'a direct write to ... an instruction file ... is refused'. A grep of the runtime, memory and roles records and a read of the instruction record found no declared set of instruction paths. R-A (:342) gives each unit a source, and R-E (:389-390) makes the loop's checklists, role definitions, record schemas and policy catalogue structured sources. Those sources have their own write doors: `record`, the policy CLI (record :258), and `new` per kind. That leaves the guard's scope undefined and open to collision. The instruction layer owes this mechanism to runtime and does not provide it. | sound | - |
| 31 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-K (Codex row) | medium | - | refuted | duplicate of id=40. Pinned blob line 458 reads '\| Codex \| `AGENTS.md` within 32 KiB, plus the card's override file \|', and layer-runtime.md:719-721 says Codex has 'no SessionStart, PostToolUse, Stop or PostCompact'. Id 40 makes the same point, that nothing re-renders the override at Codex session start so the card goes stale, and also covers the replace-not-add defect. | none | - |
| 32 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-H | low | - | refuted | duplicate of id=39. Both findings say R-H's 'memory index is a load point with a budget' has no enforcement point, because the harness writes and injects MEMORY.md outside the repository. I re-observed the same evidence: blob line 427, layer-memory.md:437-439, which settles only promotion through R-I, and wc -c of ~/.claude/projects/C--projects-coding-governance/memory/MEMORY.md, which printed 13187. | none | - |
| 33 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[layers] kit table, and [settled] v2 [owed] | low | low | confirmed | Pinned blob line 144 lists 'the `next` CLI' under Runtime, but line 214 files `next` under the loop kit (Flow). Line 221 gives process-monitor 'Runtime: supervision', while layer-runtime.md's contract row gives the supervisor to unattended and 'process-monitor: reaping', and moves 'the journal grammar ... from runlog into the core'. Line 158 still lists 'the reuse lookup', which layer-memory.md:548 retires ('\| Retire \| `reuse_lookup.py` and its agent file \|'). Line 537 says Runtime gets a build 'at the re-cut', but v2 (Revised after the runtime layer) and layer-runtime [build] name dWellOiledMachine. These are internal and cross-record contradictions. v2 and the runtime record carry the truth, so the record misleads readers but ships no behaviour. | sound | - |
| 34 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-I; [settled] Two policies (instructions.edit) | high | high | confirmed | Blob lines 430-445 call R-I a 'guarded write path' and say 'The owner uses it directly' and 'An agent only proposes'. The write-boundary validations listed are schema, tags, grammar, budgets and conflicts, with no check of who the caller is. Lines 522-526 define instructions.edit with no proof key. v2:420-421 gives only policy writes `policy.guard` and `policy.proof` (tty-cli, signed, both). I grepped layer-runtime.md for tty, proof and owner-only and found no caller proof for the instruction command. Runtime's `one-door` invariant (runtime:764) routes every instruction change through that command, yet the command does not tell owner from agent. Built as written, a session that can run the CLI can rewrite level-0 units through a recorded, valid path. The owner-command-agents-propose default is therefore unenforced. | sound | - |
| 35 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[charter-today] (micro-formats kept with the driver); [recommendations] R-A, R-D | high | - | refuted | The premise does not hold on re-probe. The blob never retires the `<!-- microformats -->` fence. [charter-today] says 'Do keep the micro-formats with the driver', and R-D's 'never in loaded text' covers render provenance, not structural fences. The claimed consequence, a gate that stays green, is also false. tools/check-microformats.sh:43 fails red when the fence pair is missing ('the definition block is not delimited by exactly one fence pair'), and tools/gate-legs.json lists check-microformats.sh as a bar leg (lines 38, 51 and 1595). A charter rendered without the fence would therefore turn the bar red, even though format-guard.js:26 allows a stop when the fence is missing. The remaining kernel, a per-reader consumer inventory, is unit-level detail that the BY DESIGN block covers. | none | - |
| 36 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[charter-today] 'Don't load what the reader never acts on' (node registry); 'Don't name sections by provenance' | medium | medium | confirmed | Blob line 319 says the node registry should not load because 'the card already names the session's node', and the record names no new home for the registry. skills/session-kickoff/manifest-check.sh:376-388 derives the card's `node —` cell from the first table under `## Node registry` in the file named by the manifest's `registry:` key. memory/guides/SESSION-KICKOFF.md:10 has 'registry: AGENTS.md', and AGENTS.md:102 holds '## Node registry'. Moving the registry out of the charter without re-pointing that key therefore makes every card print 'node — UNKNOWN', which removes the very fact the record relies on. layer-runtime [harness] also has the supervisor read runtime facts from the node registry. The card still writes, so the effect is contained. | sound | retirement-inventory-misses-readers-by-value |
| 37 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-D ('Render provenance lives in a sidecar lock, never in loaded text') | medium | - | refuted | I could not establish the defect, and the finder graded it medium. R-D's rule covers 'Render provenance', meaning the template-version line (AGENTS.md:10 `<!-- governance-template: v4.4 -->`, the 'render provenance loads every session' item in [uncovered] 3). It does not cover structural region delimiters. render_playbook.py:118-119 REGION_OPEN/CLOSE and govkit/matrix.py:726 do exist, but matrix.py:726 is an install-matrix test assertion, not runtime adoption detection. Both failure paths the finding describes depend on a builder misreading 'provenance' as 'every marker'. v2's dOrderedCharter row also renders the project block from its own overlay, so the record does not show that hand text outside a region is the target design. | none | - |
| 38 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-G; [settled] The ladder | medium | low | confirmed | Foundations still uses the old numbering: :82 'inside the rank-1 envelope', :91 'only the charter holds rank 1', and :95 'rank 0 is the platform'. It carries no revision or supersession note (grep for renumber, level 0 and Revised printed nothing). R-A (blob line 345) sends builders to 'the envelopes foundations R2 already designs', and R-G and [settled] inventory none of these values. The v2 hits at 73, 79 and 85 are dated revision-log entries, which are history rather than live contradictions. v2's body (392-403) and the dOrderedCharter chain row (732) already use levels. The impact is therefore confined to a reader who follows R-A into foundations R2. | unsound | retirement-inventory-misses-readers-by-value |
| 39 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-H, R-C, R-K (Claude Code row) | medium | medium | confirmed | Blob line 232 records MEMORY.md as 'injected by the harness', and line 427 makes it 'a load point with a budget' whose 'mechanism is settled with the memory layer'. layer-memory.md:437-439 settles only promotion through R-I, and grep for auto-memory and MEMORY.md across the memory, runtime, v2 and roles records found no budget mechanism. There is no memory/MEMORY.md in the repository (ls failed). The file is ~/.claude/projects/C--projects-coding-governance/memory/MEMORY.md, 13187 bytes, with one project directory per worktree slug. gov renders nothing at that load point, so R-C's 'the render refuses a set over budget' can never fire there. R-K's Claude Code row (line 457) also omits the index. The budget is therefore unenforced as written, with a contained effect. | sound | - |
| 40 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-K (Codex row) | medium | medium | confirmed | Blob line 458 reads 'AGENTS.md within 32 KiB, plus the card's override file'. research-orientation-preserve.md:29 measures that Codex reads 'AGENTS.override.md/AGENTS.md ... one file per directory', so a root override replaces AGENTS.md rather than adding to it, and the 32 KiB budget then sits on a file that does not load. orientation.md:328-330 already sizes the override as 'the charter plus a full card ... 24,924 bytes', which agrees with the finding and contradicts the row. layer-runtime.md:719-721 measures that Codex has no SessionStart, so the card's freshness depends on whatever last wrote the file. layer-runtime.md:743 gives 'how a harness loads instructions' to the harness adapters, while R-K gives per-harness load points to the instruction manifest. That leaves two uncoordinated extension points with no stated split. | sound | - |
| 41 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-D ('A check enforces the grammar and is seen red on planted prose') | medium | medium | confirmed | At blob 3cfd547 line 385, R-D's only acceptance for the grammar check is 'seen red on planted prose'. The real defect classes the record lists, in [uncovered] 3 (lines 274-280) and [charter-today] (311-325), are different shapes: a numbered or provenance heading, a pointer to text that is never loaded ('the marker below'), render provenance, and stale typed facts. No criterion requires the check to go red on those, so a check proven only on a planted line could pass today's charter. v2 row dOrderedCharter (line 732) carries the same 'the statement grammar and its check' with no stronger acceptance. The effect is contained to a weak gate. | sound | staged-break-substitutes-a-synthetic-value |
| 42 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-C, R-A; [settled] instructions.checks | medium | medium | confirmed | R-A's row fields (lines 335-343) are tag, level, statement type, scope tags, trigger, budget class, source and owning kit. No field says which units are required. The only completeness join in R-B (line 354) is 'every step, item and role has at least one unit', so R-C's 'missing a unit its role or item requires' (line 371) has nothing to compare against. v2's dOrderedCharter row (line 732) repeats 'missing a required unit' and also defines no relation. [settled] instructions.checks (lines 518-521) sets velocity to warn but never says what an over-budget set loads. | sound | - |
| 43 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-I (remove verb), R-J (pruning), R-B (joins) | medium | low | confirmed | R-I's write-boundary list (lines 433-440) is schema, tags, grammar, budgets and same-level conflicts. It does not say that the R-B joins or inbound pointers are re-checked when a unit is removed. No lifecycle for renaming or retiring a tag appears anywhere in the record, and R-J's prune (448-449) is silent on referrers. Partly mitigated: 'the tags' plus 'every tag used is registered' plausibly catches a dangling pointer, and 'records every change and re-renders every affected load set' with R-C's too-little refusal would catch a role left with no units at render. That makes the consequence mostly a later and vaguer catch, so I grade it low. | sound | - |
| 44 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-I ('Manifests merge deterministically with the adopter's overlay, under a lock') | medium | low | confirmed | R-I (lines 431-432) gives 'merge deterministically ... under a lock' as the only concurrency rule. The record never says how rendered views and the change record reconcile when two clones or branches edit manifests, even though the product runs on several machines. The impact is bounded: the merge bar runs at landing and already carries render-parity legs (tools/gate-legs.json: 'playbook parity', 'playbook validity gate'), so a stale render would most likely be caught rather than shipped. The omission is real but contained. | sound | - |
| 45 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-B ('the lexicon checks tag names') against [layers] dependency rule and kit table | medium | medium | confirmed | R-B (line 356) says 'the lexicon checks tag names'. The record's own kit table (line 223) lists lexicon as a Knowledge expansion, and [layers] (lines 181-182) together with P28 (line 504) say the core never depends on an expansion. v2's dOrderedCharter core row (line 732) repeats 'its names checked by the lexicon', and v2 line 198 lists the lexicon under the knowledge expansion. A core join that rests on an expansion contradicts P28, and P28's own one-way dependency check would flag it. | sound | - |
| 46 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-J; [settled] chain rows | medium | medium | confirmed | R-J (line 448) requires returns and findings to cite the unit tags they followed or broke. A grep of layer-roles, layer-runtime, layer-memory and architecture-v2 finds the citation only in v2's dCalibratedLens row (line 744, 'measured from returns and findings that cite unit tags'). Neither dBoundRoles' row nor the roles layer's return or [trust] mechanism gives a return a units field, and [settled]'s chain rows (lines 533-535) add none. The signal therefore has no producer, and 'followed' would be self-reported and uncheckable. | sound | - |
| 47 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:[recommendations] R-D ('Every loaded unit is one of six types'), R-A (work orders assembled from units) | medium | medium | confirmed | R-A (line 345) says a work order is 'assembled from units by their tags', and R-D (374) puts every loaded unit under six types. Yet layer-roles line 175 and its [trust] section put handed content (record fields, code excerpts, findings, keyed and classed) in the level-6 task block. The instruction record never reconciles this: it does not say whether handed content is outside the grammar, how it is budgeted, or how it is marked as data inside the work order's own envelope. Foundations (lines 83-85) makes text without a valid envelope data, but handed content sits inside an enveloped work order, so the boundary really is undefined. The fix is unsound because it adds a seventh statement type. [settled] (lines 501-502) records P11 as owner-ratified with exactly 'six statement types', so the fix would re-argue a settled decision. | unsound | - |
