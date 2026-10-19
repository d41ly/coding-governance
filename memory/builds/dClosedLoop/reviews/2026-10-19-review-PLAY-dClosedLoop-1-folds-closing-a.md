**Serves:** diff-review PLAY-dClosedLoop-1

# Tier-2 review: the closing folds of PLAY-dClosedLoop-1 (run A)

Provenance: run A of two independent runs on the same diff. Round 1. Finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.

Range: dd1ebb01b67238e98c5f9d328050e92e6d955cbb...320c79646344adcdc022a0e9f08df2eaa6d8935c

## Verdict: CLEAN WITH FIXES

There are no blockers. One item is high: dSafePassage now depends on a receipt field that only a later build adds.
By item, the tally is 0 blocker, 1 high, 16 medium and 3 low (20 items).
By raw confirmed finding, it is 0 blocker, 1 high, 19 medium and 4 low (24 findings).
This was a light-intensity run, so it is not a full review.
The security and intent lenses did not run. Their classes were covered only through the checklist items shared out to the other lenses.

## Subjects reviewed

The diff is three folds, reviewed as a design change:

1. 23baa12de folds the whole-design shape audit (SA-1 to SA-12).
2. 17355b8b1 and a0b1a06c4 fold the owner's answers on the remaining Skills (SK-1 and SK-2).
3. 926106e87 and 320c79646 record the adopter-instructions research and fold the owner's answers IA-1 to IA-6.

## Review shape

Intensity light: raw 30, confirmed 24, refuted 6, unverified 0 (0 uncertain), precision 0.80.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 11 | 9 | 2 | 0 | 0 | 0.82 |
| seams | yes | 12 | 8 | 4 | 0 | 0 | 0.67 |
| verification | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |

### Run integrity

- All 3 of 3 lenses returned, and none died.
- All 5 of 5 skeptic batches returned, and none died.
- No contradictory verdict was demoted to unverified, no spurious verdict was discarded, and there were no duplicates.
- Fixes on confirmed findings: 23 judged sound, 1 judged UNSOUND (id 25, whose corrected fix is given below), 0 with no fix proposed, 0 not judged.
- Severity: the skeptic graded every confirmed finding, and re-graded 3 of them from high to medium (ids 12, 24 and 25).
- Unverified findings: none.
- No lens notes were supplied, so every lens ran on the kit's generic brief.
- Intent: 35 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 34 items, shared out as correctness 12, seams 11 and verification 11.
- The finding set is complete for the three lenses that ran. It is not evidence about the security or intent classes.

## Items

### HIGH

#### H1. dSafePassage's walk and gov-first need the receipt's `steps` field, which only dShippedRelease adds (id 1)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1444`, against v2:1460 and `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md:219`.
- **What is wrong:** The fold gives dSafePassage several clauses that need per-step state in the receipt:
  - the receipt advances per completed step;
  - the receipt names the last completed step;
  - the `upgrade-walk` arm wants the receipt naming step k-1;
  - gov's source-mode receipt lists every declared step id.

  Per-step state reaches the receipt only through schema 4's `steps` field, and v2:1460 gives that field to dShippedRelease, a descendant. Today `tools/govkit/govkit.py:49` holds `RECEIPT_SCHEMA = 3`, and the envelope written at govkit.py:8020 has no steps field.
- **Consequence:** At dSafePassage's landing, its kill-midway arm, its exit-1 arm and its gov-first receipt listing cannot be built or seen red. The adopter-instructions record's [chain] also still gives gov's receipt and self-update to dShippedRelease, so one fact has two homes.
- **Fix (the skeptic judged it sound):** Choose one of two options:
  - Move the `steps` field, with its schema bump, upgrade step, down and by-value reader inventory, from dShippedRelease's row into dSafePassage's.
  - Restate the walk's progress so that it uses only schema-3 fields, with `gov_commit` set to each step's introducing commit.

  Either way, align the adopter-instructions [chain] dShippedRelease line with the build that owns gov's receipt.
- **Left-shift gate:** Add a chain-ancestry check that reds a build row which names a field, kind or key first introduced by a descendant's row. Record it in the bug-class checklist entry `step-depends-on-a-later-build`.

### MEDIUM

#### M1. `instructions.stale` has values with no route, arm or witness (ids 4, 12)

- **Where:** v2:992 (the catalogue row), v2:1268 (presets) and v2:1445 (dOrderedCharter's pins-and-drift clause).
- **What is wrong:** The key offers `order`, `refuse` and `warn`, and the strict preset selects `refuse`. The pins clause says only "filing an order as `instructions.stale` says", and it plants cases (editorial, semantic, rename, split, retirement), never values. The design record's item 9 (lines 158-159) says what `refuse` means, but no record plans an arm or witness for `refuse` or `warn`. The orphan cases always file an order, whatever the key says.
- **Consequence:** Strict selects a value that no unit implements, and nothing could fail if it were ignored. The key breaks the row's own pattern, which gives every `instructions.edit` value its own arm. This is the `policy-value-with-no-route` class that the same fold extended.
- **Fix (the skeptic judged it sound):** Give each value its own arm, witness and planted red:
  - `order` files the order and renders both.
  - `refuse` holds the update, naming the stale edge, until `instructions.edit` re-pins it.
  - `warn` prints, journals, renders both and files nothing.

  Plant each value on a semantic change. State whether the orphan cases follow the key or always file an order.
- **Left-shift gate:** Add a catalogue check that reds any enumerated policy value that has no arm and planted case named in its owning build's row. This is the `policy-value-with-no-route` gotcha turned into a gate.

#### M2. The deploy-overlay pocket gives `deploy.toml` units and a door that it no longer has (ids 6, 14)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:64`.
- **What is wrong:** The new row says `.governance/deploy.toml` is "node: units at level 0, written only through `instructions.edit`". After IA-1 the file holds only install answers and the kit selection, which are not units. govkit writes it itself: `intake` at govkit.py:8746-8762, and `add_deploy_kits` at govkit.py:999-1025, which rewrites `kits`. `[doors]` lists no install or update writer for it. The IA fold also adds two writers of the instruction overlay that no door lists: dBoundRoles' house-file upgrade step, and dOrderedCharter's absorption of `[charter] adopter_rules`.
- **Consequence:** The one-door check reads `[doors]`, so it would red every kit install and every edit to the answers. The alternative is that a spec writer re-routes kit selection through the instruction command.
- **Fix (the skeptic judged it sound):** Restate the row:
  - `deploy.toml` holds install answers and the kit selection, and no units.
  - Its writers are govkit's `intake`, install and update, plus the owner's edit under dGroundRules' minimal guard.

  Keep the level-0 units and `instructions.edit` on the instruction-overlay row only. Add govkit install/update and the upgrade-step kind to `[doors]`. Plant a kit install and assert that the one-door check stays green.
- **Left-shift gate:** Make the one-door check run against a fixture install as part of the memory plan's planted cases, so a pocket row whose door omits a real writer goes red.

#### M3. The systems record's unit schema was not amended for the IA design (ids 7, 18)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md:348-354` ([design-instruction-writing]) and systems:252.
- **What is wrong:** The diff touched only the systems record's namespace lines (238 and 277). The unit fields still lack:
  - an owner or origin field;
  - `class` (fixed or open);
  - `edges` carrying pinned `<tag>@<hash>` targets for `amends` and `supersedes`.

  `status` is still a single `retired:<forward-tag>`, and the change record's `retired → <new>` still names one successor. Three texts need these fields: v2:1445 (every gov unit declares its class and owner), design item 8 (class) and design item 10 (the successor widens to a list for a split and to `none` for a retirement).
- **Consequence:** Two copies of the unit schema now disagree. A builder working from the systems record has no field for the fixed class that IA-4 refuses on. The builder also cannot encode a split's successors, so the split and retirement cases cannot satisfy the step gate's change-record requirement.
- **Fix (the skeptic judged it sound):** Amend [design-instruction-writing]:
  - Add `owner` or origin (kit or repository), `class` (fixed or open), and `edges` with the `<tag>@<hash>` pin form.
  - Widen `status` to `retired:<tag>[,<tag>]` or `retired:none`.
  - Revise systems:252 to match.
  - Cite IA-2 and IA-4.
- **Left-shift gate:** Add a checklist entry: when a design record says it shares a schema with another record, the fold must diff both schemas' field lists. Add a meta-check that compares declared unit fields across the two records.

#### M4. dOrderedCharter registers native-id classes that later builds own and register (id 2)

- **Where:** v2:1445, against v2:1447, 1455 and 1460, and memory plan [frame] lines 21-22.
- **What is wrong:** The new edge-grammar clause registers native-id classes "with their owners": commits as dDeclaredLoop's, acts and sessions as dWellOiledMachine's, and landings as dShippedRelease's. It also requires a native-id edge to be planted and resolved. All three are later builds, and each registers its class again in its own row. No build registers the plan's `FAMILY-<slug>-<seq>` ids or gap keys, although P33 requires every class to have an owner.
- **Consequence:** At dOrderedCharter's landing no native-id class exists. The native-id arm either waits on dDeclaredLoop or passes over an empty population. Two rows claim each registration.
- **Fix (the skeptic judged it sound):**
  - Have dOrderedCharter register only the mechanism, and arm the native-id edge per class as each owning build registers that class, the way the namespace joins work.
  - Name the build that registers the FAMILY-id and gap-key classes. dTotalRecall's record kind is the likely home.
  - Plant dOrderedCharter's native-id edge on a class it owns.
- **Left-shift gate:** Use the same later-build-reference check as H1. A row must not name a descendant's kind.

#### M5. dOrderedCharter's own upgrade steps omit the two adopter-visible changes the IA fold gave it (id 3)

- **Where:** v2:1445, the "its own upgrade steps" clause.
- **What is wrong:** The clause names only agent-instructions' wiring and the map_lib re-export. The same row now does two more things:
  - It moves `deploy.toml`'s `[charter] adopter_rules` into `.governance/instructions.toml`, which removes a conf key.
  - It retires the seeded charter template, which retires an installed file.

  No `[[upgrade]]` or `[[retired]]` row is planned for either change.
- **Consequence:** dSafePassage's step gate, an ancestor, reds dOrderedCharter's own landing. Failing that, adopters' rules and seeded templates are dropped with no step to carry them. This is the `rows-lack-steps` defect coming back.
- **Fix (the skeptic judged it sound):**
  - Add an upgrade step, with a down, that converts each `adopter_rules` entry into a `repo.` level-0 unit.
  - Add a `[[retired]]` row and step for the template that orders an edited copy and never deletes it.
  - See each one red at the step gate without its row.
- **Left-shift gate:** Add a fold-time checklist item: every removal or retirement clause added to a row must name its step or retired row in the same row. The step gate's planted cases would catch this once they are built.

#### M6. The `/session-kickoff` retirement inventories by value only and misses the directory's path readers (id 5)

- **Where:** v2:1463, dConvergedCharter's SA-9 clause.
- **What is wrong:** The clause lists a closed set of readers and then removes `skills/session-kickoff/`. The unattended clause beside it inventories "by path and by value". `git grep` finds path readers the list omits:
  - `.claude/settings.json:38,47`: session-start hooks run `skills/session-kickoff/manifest-check.sh`, which v2 re-points and does not move.
  - `tools/gate-legs.json` lines 6, 155, 294, 297, 342 and 1427.
  - `tools/govkit/registry.toml:29`.
  - `tools/govkit/entries/kickoff-manifest.kit.toml:6`.
  - `check-hook-destinations.sh`.
  - `check-wiring.sh:1759-1801`, which tells each node to `ln -sfn` the link back.
- **Consequence:** Removing the directory as written breaks fail-closed session hooks and gate legs, and the wiring check re-creates the retired link.
- **Fix (the skeptic judged it sound):**
  - Inventory by path and by value over the tree.
  - Name the hook commands, the leg rows, the kit entry, the registry glob and check-wiring's link arm.
  - Move or keep `manifest-check.sh` and its fragments before the directory goes.
  - See the retirement red on a scratch clone where a path reader survives.
- **Left-shift gate:** Extend the `retirement-inventory-misses-readers-by-value` checklist entry to require "by path and by value" wording on every retirement clause. Add a design lint that flags a retirement clause carrying only one of the two.

#### M7. The bug-class selector still sits on dLinkedLibrary in the fates record (id 13)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:103`.
- **What is wrong:** The `gotchas.py` row still reads "handed by write set (dLinkedLibrary)". SA-7 gave the selector to dFurnishedOrders (v2:1451) and struck dLinkedLibrary's clause. The SA-6 rows in fates (47 and 122) were amended, but this row was not.
- **Consequence:** The selector again has two owners across the records. The fates `[check]` (fates:237-248) only requires that some chain build is named, so it passes the wrong owner.
- **Fix (the skeptic judged it sound):** Change "Where it goes" to "handed by write set through `gotchas.py --for-paths` (dFurnishedOrders)", and cite "the owner, SA-7, 2026-10-19" in "Decided by".
- **Left-shift gate:** Make the fates `[check]` cross-read v2: a fates row's named build must be the row in v2 that carries the subject.

#### M8. The step gate has two different artifacts that let a unit tag leave its population (id 15)

- **Where:** v2:1444, dSafePassage's step-gate clause.
- **What is wrong:** The red condition admits only an `[[upgrade]]` or `[[retired]]` row naming the member in `surfaces`. The unit-tag sentence admits "a change record naming its successor". The clause never says whether the change record replaces the row or must come with it. Design item 10 and systems:252 keep the successor in `instructions.edit`'s change record, and dOrderedCharter re-points adopter edges by that record.
- **Consequence:** A gov unit rename that carries only a change record reds the gate. Requiring both artifacts keeps the successor in two places that can disagree, so the gate and the edge re-pointing could follow different rename maps.
- **Fix (the skeptic judged it sound):** Pick one admitting artifact for unit tags. Either the gate's predicate reads the change record's successor (`retired → <new>`, `→ none`, or a list for a split), or the change record renders a `[[retired]]` row. Plant a rename that carries only the chosen artifact and see it green. Plant one that carries neither and see it red.
- **Left-shift gate:** Add a checklist entry: one fact, one artifact. A gate's admitting condition must name exactly one artifact for each population class.

#### M9. The unit field "owner, a kit or the repository" clashes with the `owner` edge and the one-owner rule (id 17)

- **Where:** v2:1445, against memory plan lines 138, 180 and 195.
- **What is wrong:** The registry clause changed from "owning kit" to "owner, a kit or the repository". In the memory plan, `one-owner` requires an owning build or layer, `owner` is typed node → chain build or layer, and an edge whose target is outside its namespaces goes red.
- **Consequence:** Every `repo.` unit fails `one-owner` and the edge-namespace check. Otherwise the field means something different from the edge of the same name. Gov's units are also owned by a kit in one record and by a build in another.
- **Fix (the skeptic judged it sound):** Do one of the following:
  - Rename the field to what it holds, for example `origin: kit | repository`, kept apart from the `owner` edge.
  - Widen `owner` and `one-owner` to accept a kit or the repository.

  Plant a `repo.` unit and assert that `one-owner` is green.
- **Left-shift gate:** Add a lexicon check that reds a record field whose name matches an edge type in the memory plan but whose value set differs.

#### M10. The SK-2 Skill renames take no reader inventory (id 20)

- **Where:** v2:1463, dConvergedCharter's SK-2 clause.
- **What is wrong:** Each `gov-<name>` rename ships as an upgrade step with a forward, but names no reader inventory. The `/build` and `/session-kickoff` clauses beside it, and v2's own revision note at line 580, require one. Readers pinned by value include:
  - `tools/lexicon/kit.toml:74,115,145,194` and `tools/drift-audit/kit.toml:54,151`;
  - `tools/branch-reconcile/kit.toml:32,51,64`, `tools/memory-recall/kit.toml:63,102,115` and `tools/runlog/kit.toml:50`;
  - `adopt-lexicon.sh:123`, `adopt-drift-audit.sh:66` and `adopt-branch-reconcile.sh:45`;
  - the eol pattern at `tools/govkit/selftest.py:4470`.
- **Consequence:** The step gate is satisfied because an upgrade row exists. Meanwhile the `must_exist` probes, gitattributes patterns and selftests keep comparing the old spelling. This is `a-spelling-change-strands-its-readers`.
- **Fix (the skeptic judged it sound):**
  - Add a by-value reader inventory: each kit's `to`, `probe` and `pattern` rows, the adopt scripts and selftest's eol rows.
  - Re-point those readers in the rename's unit.
  - Plant a stale probe path and see it red.
- **Left-shift gate:** Make the step gate's rename arm grep the tree for the old spelling and red on any surviving reader.

#### M11. The retired-edited check is pinned to arm 3c, which never reads a receipt row (id 24; the skeptic re-graded it from high to medium)

- **Where:** v2:1444, clause 8 ("a planted row of the state not graded as a fork by arm 3c").
- **What is wrong:** Arm 3c (`tools/govkit/govkit.py:1915-1932`) loops over descriptor `files` rules with role `forked`. Its own comment says a receipt row "is never validated by it". A planted `retired-edited` receipt row never enters that loop. Fork grading actually happens in the role-to-verdict map (govkit.py:3659) and the report counts (govkit.py:4829 and 7533).
- **Consequence:** The planned check passes whether or not update grades the row as a fork, so dSafePassage's builder would be pointed at a check that cannot fail. Selfcheck arm 7g also covers the new state, which bounds the effect. That is why the skeptic graded this medium.
- **Fix (the skeptic judged it sound):**
  - Point the check at update's verdict mapping.
  - Plant a `retired-edited` receipt row, run `update --dry-run`, and assert that the verdict is the order and not FORK.
  - Record it going red on a mapping stubbed to `forked`.
  - Drop the arm-3c wording.
- **Left-shift gate:** Add a checklist entry: a planned check that cites an existing arm must quote the arm's input. Every planned check must name its seen-red stub.

#### M12. Nothing checks the `editorial` mark that exempts a pin from drift (id 25; the skeptic re-graded it from high to medium)

- **Where:** v2:1445 (pins and drift) and the adopter-instructions record step 9 (lines 154-160).
- **What is wrong:** A pin that is behind only editorial changes "stands". The mark is written by gov's own author on gov's own change record, and no check, review or seen-red case tests whether it is true. The [owed] list (lines 243-246) does not mention it.
- **Consequence:** A semantic change marked `editorial` keeps every adopter's `amends`/`supersedes` edge green against changed meaning, with no order filed. That is the silent failure the pin exists to catch. It requires gov's own author to mark a change wrongly, so the effect is contained.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):**
  - Record a reviewer's verdict on each change record's `editorial` mark.
  - Make a change record marked `editorial` with no recorded verdict red at the landing.
  - Plant one such record and see it red.

  If that is not adopted, add a line to the adopter record's [owed] and to v2's [owed]: the mark is unchecked, and dOrderedCharter is the build that closes it.
- **Left-shift gate:** Extend the `inputs-inside-the-subjects-reach` checklist entry. An exemption keyed on a mark that the subject writes needs a recorded independent verdict.

#### M13. No owning build carries the step gate's later population joins (id 26)

- **Where:** v2:1444, and the rows at v2:1445, 1447 and 1452.
- **What is wrong:** Record-kind schemas, policy keys and gov's unit tags join the step gate's population "when its owning build lands it". The rows of dOrderedCharter, dDeclaredLoop and dTotalRecall carry no join clause and no seen-red case. dSafePassage plants only a file rename, an agent rename and a registry removal. The tag-namespace clause, by contrast, names each owning build's join.
- **Consequence:** A later build that forgets the join leaves the gate green over a partial population. The adopter design's claim that a gov unit vanishes only with a change record (adopter-instructions record, line 166) is never tested.
- **Fix (the skeptic judged it sound):** Give each owning build's row its join clause and a seen-red case:
  - dOrderedCharter: a gov unit tag removed with no change record.
  - dDeclaredLoop: a policy key.
  - dTotalRecall: a record-kind schema.

  Alternatively, make the gate refuse to go green while a registered class has no members in its population.
- **Left-shift gate:** Use the gate's own empty-class refusal (the alternative above) as the structural gate.

#### M14. The edited-render behaviour (IA-2) has no planted case (id 27)

- **Where:** v2:1444, "an edited rendered file named at update and held with an order, never reported as `re-rendered`".
- **What is wrong:** Every seen-red case in the clause belongs to the retired-edited state. Today `govkit.py:9624-9625` maps diverged or stale adopter-owned files to `re-rendered`.
- **Consequence:** A build could leave that line in place and still satisfy every listed check. That would break the adopter record's step 13 and its scenario at line 204.
- **Fix (the skeptic judged it sound):**
  - Plant a rendered file that was hand-edited since its last render.
  - Assert that update names it, holds it and files an order.
  - Show it red against today's mapping.
- **Left-shift gate:** Add a design lint: every behavioural clause in a chain row must name a planted or seen-red case.

#### M15. The pinned edge form `<tag>@<hash>` has no malformed-input cases (id 28)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:150`, against v2:1445.
- **What is wrong:** The edge checks plant and resolve tag, section and native-id targets. The pins-and-drift clause plants only well-formed pins. No case parses a pinned target with no `@`, a malformed hash, or a hash that matches no historical text.
- **Consequence:** The whole IA-3 drift mechanism rides on a parse that has no check able to fail.
- **Fix (the skeptic judged it sound):** Add the pinned form to the edge grammar's planted cases. A well-formed pin resolves its tag and checks the hash against the unit's history. A missing `@`, a malformed hash and a hash matching no history each go red.
- **Left-shift gate:** Add a checklist entry: every new target or address syntax gets malformed-input planted cases in the same fold.

#### M16. dLinkedLibrary's `adopt.instructions` promises have no fixture (id 29)

- **Where:** v2:1453 (IA-5).
- **What is wrong:** The clause promises three things: "none overwritten", "every harness file wired at once" and a shrink-only legacy list. It names no check, fixture or seen-red case for them. The research measured today's installer doing the opposite (gap-deploy-26, adopter record line 205). The shrink-only direction may come from the render gate's existing IW-1 list and dWitnessedBar's ledger factory. The no-overwrite and wiring promises are unverified.
- **Consequence:** Nothing would fail if the installer regressed to today's behaviour.
- **Fix (the skeptic judged it sound):**
  - Build a fixture: an empty repository holding a pre-existing CLAUDE.md, GEMINI.md and Copilot instructions file.
  - Install, then assert that each file's bytes are kept in the legacy block and each harness file is wired.
  - Show it red on today's installer.
  - Register the legacy list as a shrink-only ledger population, with a planted added row seen red.
- **Left-shift gate:** Use the M14 design lint: every behavioural clause must name its planted case.

### LOW

#### L1. P8 leaves out `instructions.exclude` and in-document repository parts (ids 10, 22)

- **Where:** v2:675-678.
- **What is wrong:** P8 says a repository changes gov's units "only through its own units' typed edges", and renders its rules "as a separate project block". IA-2, the revision note (v2:590-592) and the catalogue row (v2:991) also let a repository drop a gov unit through the policy value `instructions.exclude`. The composition clause (v2:1445) renders level-3 to level-5 repository units in a marked part of their documents.
- **Consequence:** For now this is wording drift only. A meta-check or reviewer working from P8 would flag `instructions.exclude` and the in-document parts.
- **Fix (the skeptic judged it sound):** Reword P8. A repository adds units at their level, changes gov's units through pinned `amends`/`supersedes` edges, and excludes them through `instructions.exclude`. Level-0 units form the project block, and higher levels render in a marked part of their documents.
- **Left-shift gate:** Add a checklist entry: a fold that adds a route must grep the principles for "only" statements covering that route.

#### L2. dBoundRoles moves "the roles kit's house files" without scoping out `policy.toml` (id 11)

- **Where:** v2:1450.
- **What is wrong:** `tools/roles/house/` holds `policy.toml` beside the `gov-*.md` overlays. The same row keeps `policy.toml` in place until dConvergedCharter folds it into `.governance/policy.toml`. The fates rows scope the move to `house/*.md` (fates:80) and route `policy.toml` elsewhere (fates:89).
- **Consequence:** The records give two answers about `policy.toml`. The words "selecting their role" partly settle the reading, so the effect is imprecision.
- **Fix (the skeptic judged it sound):** Scope the clause to the house `*.md` role overlays, and leave `house/policy.toml` on its policy-file route.
- **Left-shift gate:** Make the fates `[check]` compare path scopes with the v2 clause that moves the same files.

#### L3. The test clause has no per-value case for `instructions.stale` (id 30)

- **Where:** v2:1445 (pins and drift).
- **What is wrong:** "Each case seen on a planted release" covers only the default `order` routing. `refuse`, which strict uses (v2:1268), and `warn` are never exercised. dGroundRules' reader arm checks only that the key has a reader.
- **Consequence:** A strict install could ignore `refuse` and stay green.
- **Fix (the skeptic judged it sound):** Extend the clause: "each `instructions.stale` value seen on a planted semantic change". Under `refuse` the update is held and goes red. Under `warn` no order is filed and a warning is printed.
- **Left-shift gate:** Use the M1 catalogue check.
- **Why this is a separate item:** This is the test-clause facet of the defect in M1. It stays a separate item because its binding grade is low, and items merge only findings of one binding grade. On its own it would be medium as part of M1. The fix is shared with M1, so one edit closes both.

## Refuted, for the record

Six findings were refuted by the skeptics: ids 8, 9, 16, 19, 21 and 23. Their reasons are in the appendix.

review-shape kind=diff-review round=1 intensity=light at=synth raw=30 confirmed=24 refuted=6 unverified=0 blocker=0 high=1 medium=19 low=4 agents=9 out-tokens=243467

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1444 | high | high | confirmed | v2:1444 (dSafePassage) now says the receipt advances per completed step, names the last completed step, names step k-1 in the upgrade-walk leg, and lists every declared step id in gov's source-mode receipt. None of this was in that row at base. At base, gov-first and the source-mode receipt sat in dShippedRelease, the same row as the schema-4 `steps` field. In the new text, the per-step receipt field is still only in v2:1460 (dShippedRelease: 'the receipt's schema 4 gaining `steps`...'), and dShippedRelease is a descendant of dSafePassage in the chain table. govkit.py:49 has RECEIPT_SCHEMA = 3. So the fold put clauses on dSafePassage that depend on a later build's field. The adopter-instructions [chain] line still gives 'gov's receipt and its self-update' to dShippedRelease, alongside dSafePassage's gov-first. | sound | step-depends-on-a-later-build |
| 2 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1445 | medium | medium | confirmed | This clause is new at v2:1445 and is absent at base. dOrderedCharter registers native-id classes 'with their owners, commits dDeclaredLoop's, acts and sessions dWellOiledMachine's and landings dShippedRelease's', so it names later builds' kinds. It also requires a native-id edge to be planted and resolved. Those same classes are registered again at v2:1447 (`commit` class), 1455 (acts and sessions) and 1460 (`landing` class). The memory plan's [frame] (lines 21-22) also lists `FAMILY-<slug>-<seq>` ids and gap keys as native-id classes registered with their owner. A grep of the chain rows finds no build that registers either one. | sound | step-depends-on-a-later-build |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1445 | medium | medium | confirmed | At v2:1445, the 'its own upgrade steps' clause names only agent-instructions' wiring and the map_lib deprecation. The same row now absorbs 'deploy.toml's adopter rules as level-0 units' (which removes the `[charter] adopter_rules` conf key) and 'the seeded charter template retired'. dSafePassage's step gate (v2:1444, an ancestor) counts conf keys and installable paths, and it reds a removal or retirement that no `[[upgrade]]` or `[[retired]]` row names. No step or retired row is planned for either change. | sound | amendment-leaves-its-other-half-standing |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1445 | medium | medium | confirmed | v2:992 declares `instructions.stale` with the values order, refuse and warn, and v2:1268 sets presets warn/order/refuse/order. The pins clause at v2:1445 says only 'filing an order as `instructions.stale` says', and it plants cases, not values. The orphan cases always carry 'each with an order'. The same row gives every `instructions.edit` value 'its arm, witness and planted red', so this new key breaks the row's own pattern. The design record (lines 158-159, IA-3) does define what refuse means (hold the update until re-pinned), which narrows the defect: the meaning is stated, but no arm or witness is planned for it. | sound | rule-stated-with-no-check-that-fails |
| 5 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1463 | medium | medium | confirmed | The SA-9 clause at v2:1463 is new. It inventories readers 'by value' and lists a closed set: charter lines, write-gate text, SESSION-KICKOFF.md, the junction rule and the runbook link step. Then it removes `skills/session-kickoff/`. The unattended clause beside it says 'by path and by value over the tree'. `git grep` confirms path readers the list omits: .claude/settings.json:38,47 run skills/session-kickoff/manifest-check.sh as session hooks, and v2 elsewhere re-points that script and does not move it. The others are tools/gate-legs.json:6,155,294,297,342,1427, registry.toml:29, kickoff-manifest.kit.toml:6 (home = skills/session-kickoff), and check-wiring.sh among others. | sound | retirement-inventory-misses-readers-by-value |
| 6 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:64 | medium | medium | confirmed | The deploy-overlay row at memory-plan:64 is new; base has no deploy row. It says 'node: units at level 0, written only through `instructions.edit`', while the same row moves the adopter rules out (IA-1). The adopter-instructions record [design] 1 says deploy.toml 'keeps the install answers and the kit selection', and those are not units. govkit writes deploy.toml itself (govkit.py:1000-1025 appends `kits`). So 'written only through instructions.edit' contradicts its real writer and the IA-1 split. | sound | - |
| 7 | correctness | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md:348 | medium | medium | confirmed | The systems record's [design-instruction-writing] unit fields (systems:348-354) are unchanged by the diff, which touched that file only to add the `repo` namespace (lines 238 and 277). They still give `status` as `active` or `retired:<forward-tag>` and carry no class field. The adopter-instructions design (item 8: 'A gov unit declares its class'; item 10: the successor 'widened to a list for a split and `none` for a retirement') and v2:1445 ('every gov unit declaring its class') need fields the schema does not hold. The pinned `amends`/`supersedes` form is in the memory plan's row (line 150), but not in the systems schema the design says it shares ('the same row grammar'). So the two records disagree. The effect stays inside the design records until dOrderedCharter specs the unit. | sound | - |
| 8 | correctness | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md:154 | medium | - | refuted | The systems schema defines a unit as its row: a `fact` carries `source` in place of `text`, and its change record is an `instructions.edit` on that row. Hashing 'gov's unit text' therefore naturally means the declared row, and a change in a derived value is not a change to gov's unit, so no change record is missing. Whether the hash covers the declaration or the rendered value is unit-level detail that this design-only build leaves, by design, to dOrderedCharter's unit specs. The finder shows only an ambiguity, not a defect the fold introduced. | unsound | - |
| 9 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1453 | low | - | refuted | v2's chain makes dOrderedCharter (Foundation) an ancestor of dLinkedLibrary: dOrderedCharter -> dDeclaredLoop -> dTotalRecall -> dLinkedLibrary. Every unit that closes gap-deploy-26 has therefore landed when dLinkedLibrary exits, so its exit does not claim a gap that is still open. Owning a two-part gap by the latest build that completes it follows the register's one-owner rule (gap-register:10). dLinkedLibrary's adopt.instructions clause also covers wiring every harness file at install. | sound | - |
| 10 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:675 | low | low | confirmed | v2:675-677 P8 reads 'A repository changes gov's units only through its own units' typed edges'. v2's revision note at 590-592, IA-2 and the catalogue row at 991 also let a repository drop a gov unit through the policy value `instructions.exclude`, which is not an edge. The principle's 'only' leaves out a path the owner chose. That is wording drift between two statements of one rule, with no behaviour yet. | sound | - |
| 11 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1450 | low | low | confirmed | `tools/roles/house/` holds `policy.toml` beside the ten `gov-*.md` role overlays. v2:1450's new dBoundRoles clause moves 'the roles kit's house files' into the overlay, unqualified. The same row's shapes clause keeps effort in `tools/roles/house/policy.toml` until dConvergedCharter folds it, and the fates rows scope the move to `house/*.md` (line 80) and route `house/policy.toml` to `.governance/policy.toml` (line 89). The words 'selecting their role' partly settle the reading, so the effect is imprecision. | sound | - |
| 12 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:992 | high | medium | confirmed | v2:992 catalogues `instructions.stale` as order, refuse, warn, and the strict preset row at v2:1268 selects `refuse`. dOrderedCharter's pins clause (v2:1445, segment 33) says only 'filing an order as `instructions.stale` says', and plants per case, never per value. In the same row, segment 15 gives each `instructions.edit` value 'its arm, witness and planted red'. The design record's item 9 (line 159) names the values but gives no route. Nothing says what `refuse` refuses or what `warn` does. This is the class memory/gotchas/policy-value-with-no-route.md records, and the same fold extended that record. The design-level effect is contained. | sound | policy-value-with-no-route |
| 13 | seams | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:103 | medium | medium | confirmed | fates.md:103 still reads `gotchas.py` ... 'handed by write set (dLinkedLibrary)', citing v2 [chain] dLinkedLibrary. Meanwhile v2:1451 (dFurnishedOrders) now says bug classes are 'selected by `gotchas.py --for-paths`, the one selector (SA-7)', and the comparison record's SA-7 answer (lines 187, 210, 277) strikes dLinkedLibrary's clause. The fold amended the SA-6 rows in fates (memory-recall's kit row and query.py, 'the owner, SA-6, 2026-10-19') but left this row alone, so the selector is still assigned to two builds across the records. That is one of the stale states the review was asked to look for. The effect stays in the records and does not reach behaviour. | sound | - |
| 14 | seams | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:64 | medium | medium | confirmed | The diff adds the memory-plan pocket row (line 64), which says `.governance/deploy.toml` is 'node: units at level 0, written only through `instructions.edit`'. The adopter-instructions design item 1 (line 134) says 'deploy.toml keeps the install answers and the kit selection'. govkit.py:999-1025 `add_deploy_kits` rewrites the `kits` array in that file. The plan's one-door rule now says 'each node has one writer, a door [doors] lists', with a write by an unlisted writer going red. [doors] names no install or update writer for deploy.toml. So the new row contradicts both the tree and the IA design. | sound | - |
| 15 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1444 | medium | medium | confirmed | v2:1444's step-gate clause, new in this diff, lists gov's instruction-unit tags in the population, then says 'a unit tag vanishing only with a change record naming its successor'. It then says the gate 'reds a landing that removes, renames or retires a member with no `[[upgrade]]` or `[[retired]]` row naming it in `surfaces`'. The clause never says whether the change record replaces the row for the unit-tag class or must come with it. The design record (item 10) and systems:252 put the successor in `instructions.edit`'s change record, and dOrderedCharter re-points adopter edges by that record. A spec writer reading the red condition as written would require a second, separately kept successor, or would red a gov unit rename that carries only a change record. | sound | - |
| 16 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1444 | medium | - | refuted | At the base (dd1ebb01b), dShippedRelease already had the stale-lock reclaim ('a stale lock reclaimed'), with no holder-publication detail. The fold moved it under SA-2 and added only 'once its holder is dead'. How a lock and its holder record are published atomically is unit-level mechanics. The by-design list says unit-level detail is absent and owed to the chain builds' specs, and the gap the finder names was already there at the base. The finder does not show that the fold introduced a defect at design level. | none | beacon-published-before-it-is-complete |
| 17 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1445 | medium | medium | confirmed | At the base, v2 read '...source, owning kit)'. Now v2:1445 reads '...source, owner, a kit or the repository, and class, fixed or open)'. memory-plan:138's one-owner rule says 'every node names one owning build or layer', checked by `one-owner`, and its edge table types `owner` as 'node → chain build or layer', with an edge whose target is outside its namespaces going red. A `repo.` unit, new in this diff, is owned by 'the repository', which is neither a build nor a layer. So the fold reuses the edge's name for a field holding a different value set, and new repository units cannot pass the one-owner rule as written. The kit-valued part was there at the base. The repository value and the name clash are new. | sound | - |
| 18 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md:348 | medium | medium | confirmed | The diff touches only the systems record's namespace lines (238, 277). [design-instruction-writing] (around line 348) still lists the unit's fields without `class` or an owner/origin field, without `edges` carrying `<tag>@<hash>` pins, and with `status` `retired:<forward-tag>` holding a single successor. The adopter-instructions design item 10 says the change record's successor widens to a list for a split and to `none` for a retirement, and item 1 says the overlay uses the kits' row grammar. Its own [decided] section lists 'merged by row key' and 'the owning-kit field' as contradictions in the systems record, yet the fold left that schema stale against v2's dOrderedCharter row. | sound | - |
| 19 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1445 | medium | - | refuted | The pinned form is planted and read in the same dOrderedCharter row (v2:1445). Clause 32 defines the overlay's `amends`/`supersedes` targets 'pinned as `<tag>@<hash>`' and requires 'each operation seen on a planted overlay and each refusal red'. Clause 33 (pins and drift) reads the hash and plants every drift case on a planted release. The address in a pinned target is still a tag, which is one of P33's three forms; `@hash` qualifies the tag rather than adding a fourth address form. The grammar clause's only restriction on a target is no space, comma or bracket, and `@` breaks none of them. The memory plan's site table (plan:150) states the pin at the instruction-unit site. The claim that 'no clause plants or resolves the pinned form' does not match the row, and the red on the resolves check is speculation. | sound | - |
| 20 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1463 | medium | medium | confirmed | The SK-2 clause in dConvergedCharter's row (v2:1463, clause 9) ships each `gov-<name>` rename as an upgrade step with a forward, and it names no reader inventory. The sibling clauses do: /session-kickoff (clause 16) and /build (clause 17) each say 'readers inventoried by value', and the unattended clause inventories by path and by value. The same fold's revision note (v2:580) says 'every rename and retirement inventories its readers by value'. A git grep confirms readers pinned by value: tools/lexicon/kit.toml:74,115,145,194; tools/drift-audit/kit.toml:54,151; adopt-lexicon.sh:123; adopt-drift-audit.sh:66; tools/memory-recall/kit.toml:63,102,115; tools/runlog/kit.toml:50; govkit/selftest.py:4470; and the kits' selftests. The step gate checks only that an upgrade row exists, so these readers would be stranded. The fold introduced this, and the effect stays inside one future unit's scope. | sound | a-spelling-change-strands-its-readers |
| 21 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:347 | low | - | refuted | Every gap in v2's rows has exactly one owner: no gap key appears in two build rows, so the fix's 'list gap-found-29 in dSafePassage's row too' would break that convention. Where several builds close parts of a gap, the single owner is the descendant whose landing completes the closure. dOrderedCharter descends from dSafePassage, the closer of gap-found-29's `re-rendered` half. dLinkedLibrary descends from dOrderedCharter through dTotalRecall and dDeclaredLoop, so the alias half lands before gap-deploy-26's owner. The gap join therefore never credits a closure before every half has landed, and the 'if the alias clause slips' path does not arise from the ancestry. | unsound | - |
| 22 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:676 | low | low | confirmed | The new P8 (v2:676-678) says a repository changes gov's units 'only through its own units' typed edges, pinned'. The owner's IA-2 recommendation (adopter-instructions record :237) is 'amend, replace, and a policy list to exclude', and the same fold's revision note and catalogue row (v2:592, 991) add `instructions.exclude`, which is a policy value and not an edge. P8's 'as a separate project block' wording is inherited, but the fold's composition clause (v2:1445) now renders level-3 to level-5 repository units 'in a marked part of their documents'. The principle and the chain clause disagree, and only wording is affected. | sound | - |
| 23 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1126 | low | - | refuted | This is pre-existing. At dd1ebb01b the catalogue row already offered `order, keep, delete` (base v2:1091). dShippedRelease's base clause ('an edited retired file kept as a `forked` row with an order, as `install.retired-edits` says') also specified only the order behaviour, with no keep or delete arm and no plant. The fold moved the clause and changed the state to `retired-edited`, but the missing arms and plants for keep and delete are unchanged from the base. | sound | policy-value-with-no-route |
| 24 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1444 | high | medium | confirmed | At tools/govkit/govkit.py:1915-1932, arm 3c loops only over descriptor `files` rules with role `forked`. Its own comment reads 'THE DEMAND IS ON THE DESCRIPTOR AND NOWHERE ELSE. A receipt row is READ by `update`'s report printer and is never validated by it'. A planted `retired-edited` receipt row never enters that loop, so the check the fold plans (v2:1444, clause 8: 'a planted row of the state not graded as a fork by arm 3c') passes whether or not update grades the row as a fork. The fork grading lives in the role-to-verdict map (govkit.py:3659 `"forked": "forked"`) and the report counts (4829). The same clause also brings the new state under selfcheck arm 7g, which bounds the consequence. This is design text that would mislead dSafePassage's builder into a check that cannot fail, so I grade it medium rather than high. | sound | - |
| 25 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1445 | high | medium | confirmed | v2 line 1445 (dOrderedCharter, pins and drift) says only 'each gov change record marked `editorial` or `semantic`, a pin behind editorial changes alone standing'. The adopter record's step 9 (lines 154-160) has the same text. A grep for 'editorial' across the build records finds no other clause: no check, review or seen-red case tests whether the mark is true. The [owed] list (lines 243-246) covers the pin's noise and the restructuring map, not the mark. The prior-art return (line 183) shows the upstream author is meant to set the mark, so the exemption and who marks it are the owner's IA-3 direction. The missing check on the mark is new text added by this fold. A mis-marked semantic change silently keeps adopters' edges green. That is the failure the pin exists to catch, but it needs gov's own author to get the mark wrong, so the effect is contained: medium, not high. | unsound | inputs-inside-the-subjects-reach |
| 26 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1444 | medium | medium | confirmed | The step gate is new in this diff: the base v2 has no 'step gate' text. v2 line 1444 says 'each later class, record-kind schemas, policy keys and gov's instruction-unit tags among them, joining when its owning build lands it'. The only other mention of the step gate is in dConvergedCharter's row (line 1463, the docs leg). The rows of dOrderedCharter (1445), dDeclaredLoop (1447) and dTotalRecall (1452) carry no clause joining their class to the step gate and no seen-red case for it. The tag-namespace clause shows the record's own convention: it names each owning build's join ('step, item and policy by dDeclaredLoop, role by dBoundRoles...'). The step gate's join names none. The adopter record's step 10 (line 166) rests on this join, and dSafePassage's planted cases cover only a file rename, an agent rename and a registry removal. | sound | - |
| 27 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1444 | medium | medium | confirmed | In v2 line 1444, the clause '... and a planted row of the state not graded as a fork by arm 3c, and an edited rendered file named at update and held with an order, never reported as `re-rendered` (P38, SA-2, IA-2)' plants only the retired-edited row. The edited-render behaviour has no planted case or seen-red case. govkit.py still maps diverged or stale adopter-owned files to `re-rendered` (`if how == "adopter" and v in ("diverged", "stale"): v = "re-rendered"`). That matches the adopter record's line 40 citation of govkit.py:9624-9625 and its line 204 scenario. Nothing listed would turn red if that line survived. | sound | - |
| 28 | verification | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:150 | medium | medium | confirmed | The memory plan's diff adds the instruction-unit site's '`amends` or `supersedes` target pinned as `<tag>@<hash>`' (line 150). The edge checks in v2's dOrderedCharter row still read 'one edge per address form, tag, section and native id, planted and resolved'. The planted cases for malformed edges cover only the two-type block and gov:note refs. The pins-and-drift clause plants release scenarios (editorial, semantic, rename, split) on well-formed pins. No case parses a pinned target that is missing its `@`, carries a malformed hash, or names a hash matching no historical text. The finder's claim about what the resolve arm would do is speculative, but the missing planted case is real. | sound | - |
| 29 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1453 | medium | medium | confirmed | v2 line 1453's `adopt.instructions` clause (IA-5) reads 'rendered verbatim as a legacy block after the project block, on a shrink-only list, every harness file wired at once and none overwritten, then each paragraph proposed ...' and names no fixture, check or seen-red case. Sibling clauses in the same rows do name them (for example 'each value seen on a planted ...', 'seen red on a planted ...'). The adopter record (line 205, gap-deploy-26) records today's opposite behaviour, so a regression is a known risk. One part is weaker: the render gate's 'shrink-only legacy list (IW-1)' already existed at base, and dWitnessedBar's ledger factory declares each population's direction. The direction check may therefore come from those, but the no-overwrite and wiring promises are unverified. | sound | - |
| 30 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1445 | low | low | confirmed | `instructions.stale` is new: catalogue line 992 lists order, refuse and warn, and preset line 1268 gives strict `refuse`. In the pins-and-drift clause, line 1445 says only 'filing an order as `instructions.stale` says ... each case seen on a planted release'. That is the default routing. The same row requires 'each `instructions.edit` value given its arm, witness and planted red', and sibling keys use 'each value seen on a planted ...'. This key gets no per-value case, so `refuse` and `warn` are never exercised. It is a gap in the test clause only, graded low as the finder graded it. | sound | - |
