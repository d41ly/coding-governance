# Skeptic brief: run C, batch 1

**Serves:** research PLAY-dClosedLoop-1

**Your task is to refute each finding below, and then to break each clean cell after them.** This brief is your
instructions, not the subject of your review: do not review it, the audit's seal or its instruments. A defect you see
in them goes in one line at the end of your return, and nowhere else.

You are one of four skeptics in run C of the whole-design audit (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, whose `[rubric]` grades
what you confirm). Each finding below was returned by a walker reading the sealed copy of the design at
`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Then try to break each clean cell listed after them, a
cell a walker judged to hold.

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index, and **Stage 0's leads,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md`,
   which some findings cite.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-c1/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

### C1-F8 — Clause ids and the `Carries` relation are never registered as an address form or an edge, and they collide with the `carries` edge
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0001, read against cl-dClosedLoop-0058
- **Class:** K6
- **Severity:** medium
- **Evidence:**
  - P33: a node is "addressed by a tag, a section or a native id whose class is registered with its owner … typed edges from one closed set".
  - cl-0058 registers "one edge per address form, tag, pinned tag, section and FAMILY id". It also reds a pinned target "whose hash matches no text in its unit's history". A clause's `<hash8>` is a different hash.
  - memory-plan `[edges]` defines `carries` as "landing → unit, commit".
  - cl-0001 parses `**Carries:** cl-…@<hash8>` lines.
- **Consequence:** Once the edge checks land, either every chain spec's Carries line and every deviation pin goes red, or they stay outside the closed set, as prose relations P34 forbids.
- **Fix:** In cl-0058, register `cl-<slug>-NNNN` as a native-id class owned by dTrueNorth, and register its `@hash8` pin form. Rename the spec relation, for example `carries-clause`, or widen `carries`'s from/to rows.

### C1-F18 — "A ninth join": spec-tokens already has nine
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0002
- **Class:** K6
- **Severity:** low
- **Evidence:** cl-0002 calls the carries join "a ninth join of the spec tokens leg". Probe on `tools/check-spec-tokens.py`:
  - The docstring names legs, paths, cites, bar, guards, claims, handoff (seventh) and size (eighth).
  - Line 960 has "THE COVERS JOIN (TOOL-aMendedFleet-75)".
- **Consequence:** The count is stale, and a builder looking for the ninth slot finds `covers` there.
- **Fix:** Call it "a further join".

### C1-F9 — The deviation record is no registered kind and is missing fields its record sets
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0004
- **Class:** K3
- **Severity:** medium
- **Evidence:**
  - Stage 0's lead: "The deviation record is no registered kind … no owner, writer or reader is declared for it".
  - final-questions `[deviation]` sets the record's fields: "its id; the hand-off; … the approver and where the approval is recorded; … and its cause (P35)".
  - cl-0004's fields: "the departure's address, before and after, cause class, reason, evidence, risk class, approver and follow-through". The hand-off, the approval's location and the cause are missing, and the hand-off is what selects the approver.
- **Consequence:** The record has no home, door or reader. Without the hand-off, the "approver meets its risk" join cannot pick the approver.
- **Fix:** Give the record a home and a writer in cl-0004, and register it with dTotalRecall's kind registry when that lands. Add the hand-off, the approval location and `caused-by`.

### C1-F7 — The deviation clauses rely on a later build's overlay grammar and approval rule, with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0006 (also cl-0004)
- **Class:** K7
- **Severity:** medium
- **Evidence:**
  - final-questions `[spine]`: "each carrying an `amends` or `supersedes <clause-id>@<hash8>` row in dOrderedCharter's overlay grammar". `[deviation]`: "an editorial change, by dOrderedCharter's classifier".
  - cl-0006 says "each deviation's amends or supersedes row applied". cl-0004 is "red on … an approver below the risk".
  - The risk-to-approver rule is `deviation.approval` (Owner dDeclaredLoop), and the classifier is cl-0063's.
  - dTrueNorth comes before dGroundRules, so no policy file exists yet either.
- **Consequence:** dTrueNorth's join and as-built view cannot be built from what is landed at the chain's root.
- **Fix:** Have cl-0004 and cl-0006 name their stand-ins: a fixed by-risk table and a local row form. Each is re-pointed when dOrderedCharter and dDeclaredLoop land.

### C1-F14 — dGroundRules' witness needs load sets and a composition that only dOrderedCharter builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0015
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0015 is "seen … on a load set missing a required unit and a composition over a harness's own limit, both still refused under `warn`". Load sets are cl-0041's and the composition is cl-0064's, both in dOrderedCharter, a descendant.
- **Consequence:** dGroundRules' acceptance cannot be run when it lands.
- **Fix:** Plant today's consumer limit at dGroundRules (agent-instructions' `CODEX_MAX`), and move the load-set and composition cases to cl-0041 and cl-0064.

### C1-F13 — Cap values have two homes, and `budgets.*` is read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0015 and cl-dClosedLoop-0041
- **Class:** K4
- **Severity:** medium
- **Evidence:**
  - Catalogue: "`budgets.*` | each cap's value, the owner's … | dCalibratedLens". night-pass-two `[p5-caps]`: "Each cap's value stays the owner's under `budgets.*`".
  - cl-0015: "each cap's value read from its one declaration". cl-0041: "extending `template-size-limits.txt`".
  - Stage 0's K4 lead: "budgets.*: read by no chain clause and no item".
- **Consequence:** Load-point caps are declared in `template-size-limits.txt`, while the catalogue puts them under `budgets.*`. That is two answers to one fact, and the owner's policy write moves nothing a gate reads.
- **Fix:** Have cl-0015 name the one declaration. Either the policy file's `budgets.*`, with `template-size-limits.txt` migrated to it, or `template-size-limits.txt` as the only home, with `budgets.*` re-scoped to name it.

### C1-F5 — dGroundRules retires an adopter's `FANOUT_CAP` before any upgrade step exists, which silently raises a lowered limit
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0016
- **Class:** K10, c3
- **Severity:** high
- **Evidence:**
  - cl-0016 retires "agent-cap's slot ledger … retired in the same unit with `.agent-cap.conf`".
  - P38: "A build that changes what an adopter can see ships its successor with an upgrade step". The step kind and the step gate arrive only in dSafePassage, the child build.
  - Probe: `tools/hooks/agent-cap.js:68` reads "A REPO MAY LOWER IT … `FANOUT_CAP=<n>` in a tracked `.agent-cap.conf`", and `tools/hooks/README.md:234` reads "Lowering the cap — `.agent-cap.conf`".
- **Consequence:** An adopter that set `FANOUT_CAP=2` updates and is held to `runtime.agents-in-flight`'s default of 6. Its own limit is loosened with no step, order or warning.
- **Fix:** In cl-0016, translate a present `FANOUT_CAP` into the policy file's `runtime.agents-in-flight`, or hold the conf as a read legacy home, until dSafePassage ships the step. Plant a fixture with `FANOUT_CAP=2` and check it still caps at 2.

### C1-F15 — `install.retired-edits`' `keep` and `delete` values have no arm, and `delete` loses edits
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0026
- **Class:** K9
- **Severity:** medium
- **Evidence:** Catalogue allowed values: "order, keep, delete". research-supersession:175 says "`keep` is today's silent `patched`; `delete` loses edits". cl-0026 says "ordered as `install.retired-edits` says … extended with the order arm". Only `order` is built.
- **Consequence:** The schema accepts two values that no code routes. If `delete` is ever wired, it removes an adopter's edited file (P19/P38).
- **Fix:** Give `keep` and `delete` their arms and planted cases in cl-0026, or drop them from the allowed values.

### C1-F16 — The floor's down step checks TOML only, while the up step removes the guard against newer Python syntax
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0028
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0028 describes the down as "restoring the old declaration and refusing while a tracked TOML file fails to parse under the floor it restores". It also has "the PEP 701 text ban in `merge-rows.test.sh` retired". Probe: `tools/memory-tree/merge-rows.test.sh:355` printed `nested same-quote f-string (PEP 701, 3.12+)`. gap-tool-22 says the old floor is 3.11.
- **Consequence:** After the raise, 3.12+ syntax can land. A rollback then restores a 3.11 floor under tracked Python that will not compile.
- **Fix:** Make the down refuse while any tracked `.py` fails `compile()` under the floor it restores. Plant a case: a PEP 701 f-string landed after the raise.

### C1-F10 — The re-founded charter leaves out the core principles and the decision principles that outrank practices
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032
- **Class:** K8
- **Severity:** medium
- **Evidence:**
  - v2 `[front-door]` lists "the core principles, fixed; the decision principles that resolve unattended forks …, which outrank the practices". gap-flow-02, owned by dOrderedCharter, says "nothing ranks them above the charter's adjustable practices".
  - cl-0032's list: "front door, precedence and override rule …, instruction map, active practices, one line each, hand-off to the loop, the repository's project block".
  - P18's only enforcing clauses are cl-0176 and cl-0390, on later builds.
- **Consequence:** gap-flow-02 is owned but closed by no clause, and P18's ranking over practices never reaches the charter.
- **Fix:** Add the fixed core principles, rendered from cl-0037's registry, and the ranked decision principles to cl-0032's envelope list.

### C1-F11 — gap-found-18, the `up —` password prompt, is owned by dOrderedCharter but carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032
- **Class:** K8
- **Severity:** medium
- **Evidence:** layer-expansions:506 has "`gap-found-18` | … The `up —` micro-format asks for a password value, inviting a secret into chat | dOrderedCharter". dOrderedCharter's "Gaps owned" cell includes gap-found-18. A grep of v2 for `password` and `up —` found no clause.
- **Consequence:** The re-founded charter keeps a micro-format that asks for a secret in chat, which goes against the charter's [security] rule.
- **Fix:** In cl-0032 or cl-0042, rewrite the `up —` micro-format to name where a credential lives, never its value. Add a grammar red on a micro-format that asks for one.

### C1-F2 — Re-founding the charter breaks the roles kit's reader of the section-1 rule tags
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032 (also cl-0042 and cl-0043)
- **Class:** K10, c1
- **Severity:** high
- **Evidence:** layer-instruction R-B: "Retiring a section number re-points its readers in the same unit. The charter's readers are `roles_lib.py`'s `SECTION_ONE_RE`, which finds the rules under `## 1. ` and refuses with R0 without it, and the review harness prompts that grade by section number." R-D counts "a numbered heading" as a red case. Probes:
  - `grep -n SECTION_ONE_RE tools/roles/roles_lib.py` printed `61:SECTION_ONE_RE = re.compile(r"^## 1\. ")`.
  - Lines 193–204 raise `R0 — the governing doc carries neither a section 1 rule tag nor a '## §<n> — ' heading`.
  - A grep of `[chain]` for `roles_lib`, `section 1` and `SECTION_ONE_RE` found only dConvergedCharter's `load_policy` clause.
- **Consequence:** The level-0 charter has no `## 1.` heading, and cl-0042's grammar reds a numbered heading. Every role render then fails with R0, so dOrderedCharter cannot land green.
- **Fix:** In cl-0032, re-point `SECTION_ONE_RE` and the roles `rules:` join to the practice units' tags in the same unit, along with the harness prompts that grade by section number. Prove it with a role render on the re-founded charter.

### C1-F12 — The override record and the exception register have no kind, home or door
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032 and cl-dClosedLoop-0037
- **Class:** K3
- **Severity:** medium
- **Evidence:**
  - Stage 0's K3 leads: "override: no writer item: `charter.override` and its record" and "exception: the exception register beside the `core.*` policies; writer item not named".
  - foundations: "the agent then records the override (the rule it set aside and the owner's words)". Every exception "carries its principle, the part it excuses and a reason".
  - Neither clause names a home or a writer, and memory-plan `[doors]` lists neither.
- **Consequence:** Both are records that P30 says go through one door, but they have none before dTotalRecall. The Loop Review's audit of the exception register has nothing to read.
- **Fix:** Have cl-0032 and cl-0037 name each record's home, fields and writer, as stand-ins that dTotalRecall's registry adopts.

### C1-F20 — The card for other harnesses goes through Runtime harness adapters, which dWellOiledMachine builds later
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0038
- **Class:** K6
- **Severity:** low
- **Evidence:** cl-0038: "another harness's through its Runtime harness adapter". layer-instruction R-K: load points per harness "come from Runtime's harness adapters" (`runtime.harnesses`, Owner dWellOiledMachine).
- **Consequence:** There is no adapter to deliver through when the build lands, and no stand-in is named.
- **Fix:** Name agent-instructions' wiring as the stand-in until the adapters land.

### C1-F1 — The unit registry leaves out `required-by`, so the missing-unit refusal has nothing to read
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0039, read with cl-dClosedLoop-0041
- **Class:** K6, c3
- **Severity:** high
- **Evidence:** layer-instruction `[recommendations]` R-A lists the unit row's fields, including "`required-by`: the roles and items that require it, which R-C's 'too little' refusal reads". Systems `[design-instruction-writing]` also lists "`required-by`, `enforced-by`". cl-0039 lists the fields as "tag, level, statement type, scope tags, trigger, budget class, source, origin … `usage` … `help` … and class", with no `required-by`. cl-0041 still says load sets are "refused when missing a required unit". I grepped `[chain]` for `required-by`: there are 0 hits, so no clause registers the field.
- **Consequence:** The P27 load-set check has no declared list of required units. It either stays green over nothing, or the builder makes the field up. The adopter-instructions item 6 exclusion refusal ("one another active unit requires") also has nothing to read.
- **Fix:** Add `required-by` and `enforced-by` to cl-0039's field list. Make cl-0041 read `required-by`, and plant a red: a unit named in `required-by` that is missing from a load set.

### C1-F19 — "Instruction packs … into the preset catalogue" clashes with the rule that presets never touch `charter.practices`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0045
- **Class:** K9
- **Severity:** low
- **Evidence:** cl-0045: "instruction packs extending `charter.practices` into the preset catalogue". v2 `[presets]`: "Presets never touch … `charter.practices`".
- **Consequence:** A builder may add packs to the policy presets and go against the never-touch rule.
- **Fix:** Name it "a pack catalogue", separate from the policy presets.

### C1-F6 — The inventory of by-path readers for the moved grammar misses three readers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0048
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0048 says "from an inventory of every reader of `extract.py` and `recall_conf.py` by path:" and names only check-verdict-epoch.sh, migrate_backlog.py and merge-rows.test.sh. The probe `grep -rln 'extract\.py\|recall_conf' tools skills .githooks` found more readers:
  - `skills/session-kickoff/manifest-check.test.sh:1325` hides `extract.py` and expects "NOTE: id citations unchecked — … the id grammar lives in the memory-recall kit".
  - `.githooks/straggler-guard.test.sh:84`.
  - `tools/unattended/check-unattended.sh:2035`.
- **Consequence:** After the move, the kickoff F1 arm hides a file that no longer holds the grammar. It either goes red on the bar or passes without testing the no-grammar path.
- **Fix:** Derive cl-0048's inventory with that grep and name these three readers. Each one gets re-pointed and its arm re-seen red.

### C1-F4 — The join factory moves to `tools/lib`, which no adopter receives
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0049
- **Class:** K10, c2
- **Severity:** high
- **Evidence:**
  - cl-0049: "`compute_coverage` moved to `tools/lib` as the join factory … while `map_lib` re-exports the moved names … the template re-copied into adopters through govkit's update".
  - The charter's Kinds fact: "tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead".
  - Probe: `grep -rn 'inline\|gov-internal' tools/lib/*.sh` printed `resolve-python.test.sh:160: <prefix>/lib/ is gov-internal and ships nothing, so a copy-installed kit cannot source a shared library and must carry the function inline`.
  - No clause or record says the moved functions are carried inline.
- **Consequence:** After an update, an adopter's copy-installed codebase-map re-exports from a module that was never installed, so its imports fail. The tags-pack joins that use the factory cannot run in any adopter.
- **Fix:** Make cl-0049 carry the factory inline in every shipped kit that imports it, with a parity leg as for `resolve-python.sh`, or declare `tools/lib` a shipped kit with an install row. Prove it with a copy-install fixture run.

### C1-F3 — Three guard-bearing tags keys owned by dOrderedCharter have no reader, so cl-0014's arm goes red when it lands
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0049 (also cl-0040 and cl-0059)
- **Class:** K4, c1
- **Severity:** high
- **Evidence:**
  - Systems `[design-tags]`: "resolves, with bare references as `tags.bare-refs` says", "retired | new text citing a retired tag", and `gov tag show` returns "the smallest leaf slice" (research-tags-b: "the leaf slice (`tags.slice`)").
  - The v2 catalogue gives `tags.slice`, `tags.retired-cites` and `tags.bare-refs` the Owner dOrderedCharter.
  - Stage 0's K4 leads: "tags.bare-refs: read by no chain clause and no item (guard-bearing)", "tags.retired-cites … (guard-bearing)", "tags.slice …".
  - cl-0049 says only "one resolver (`gov tag show`, `where`, `refs` and `check`) … the `tags` leg pack".
  - cl-0014 is "an arm red when a key whose Owner build has landed has no reader".
- **Consequence:** At dOrderedCharter's landing, dGroundRules' own arm goes red on three keys. If the build lands anyway, `refuse-new` on retired cites and the `never`/`unique` bare-reference rules exist only as catalogue values.
- **Fix:** In cl-0049, name the `resolves` check under `tags.bare-refs`, the `retired` check under `tags.retired-cites`, and `gov tag show`'s slice under `tags.slice`. Each value needs its planted case.

### C1-F17 — The render gate's legacy list is hard-wired shrink-only, so strict's `instructions.legacy: refuse` has no arm
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0050
- **Class:** K9
- **Severity:** low
- **Evidence:** Catalogue: "`instructions.legacy` | shrink-only, refuse | … IW-1 arms the render gate at dOrderedCharter". The strict preset sets `refuse`. cl-0050 says "the render gate armed with a shrink-only legacy list (IW-1)".
- **Consequence:** Under strict, a legacy document is still admitted.
- **Fix:** In cl-0050, read the gate's mode from `instructions.legacy`, with each value planted.

### C2-F6 — dFairHearing's breakpoint items depend on, and route to, items owned by a later build
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0070` and `cl-dClosedLoop-0075`
- **Class:** K6
- **Severity:** medium
- **Evidence:**
  - flow-steps `review.pin` (fs:484), owned by dFairHearing, needs `review.trigger`.
  - `review.report` (fs:487) routes to `review.dispose`.
  - Both `review.trigger` and `review.dispose` belong to dDeclaredLoop (0105), a descendant of dFairHearing.
  - Stage 0: "K2 dFairHearing→review.dispose: order: … not an ancestor, UNCLASSED".
  - Neither 0070 ("`review.pin` maps from `review.opt-in`") nor 0075 declares a stand-in.
- **Consequence:** dFairHearing's acceptance cannot run its items end to end in order, or it quietly reaches into dDeclaredLoop's program.
- **Fix:** Add a stand-in to 0075 and 0070: until dDeclaredLoop lands, the harness is invoked directly with its pin arguments, and the report's dispositions are written to the review record.

### C2-F16 — "The panel's internals" does not carry the untyped harness agent gap that dFairHearing owns
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0078`
- **Class:** K1
- **Severity:** low
- **Evidence:** gap-review-13: "The review harness spawns an untyped agent that no stage declares", owned by dFairHearing. The systems record's checks say "every stage a declared role". 0078 says only "the panel's internals".
- **Consequence:** A spec writer cannot tell from 0078 that the untyped spawn must be typed and declared.
- **Fix:** Add to 0078: "every agent the harness spawns typed and declared in a stage, seen red on a planted untyped spawn".

### C2-F9 — dDeclaredLoop's guard-bearing keys `floor` and `transitions.record` are named by no clause
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0087` and `cl-dClosedLoop-0088`
- **Class:** K4
- **Severity:** medium
- **Evidence:**
  - Stage 0 K4: "`floor`: read by no chain clause and no item (guard-bearing)" and "`transitions.record`: … (guard-bearing)".
  - 0087 reads "the guard, the TTY CLI and the default floor". 0088 reads "the transition record three ways". Neither names its key.
  - [floor] says the invariants are "each switchable only under the policy guard".
- **Consequence:** The switch that turns a floor invariant off, and the subset choice of transition-record channels, have no specced reader. A spec can ship the floor hard-wired and the key unread, so it fails open.
- **Fix:** Name `floor` in 0087 and `transitions.record` in 0088, each with a planted value seen red: an invariant switched off without the guard is refused, and an empty channel set is refused.

### C2-F8 — The spine's transition table routes to and witnesses items owned by later builds
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0098` and `cl-dClosedLoop-0100`
- **Class:** K6
- **Severity:** medium
- **Evidence:**
  - Stage 0: "dDeclaredLoop→build.distill, build.ratify, deploy.notify, design.ready, plan.exit, plan.input, test.exit: order: … not an ancestor, UNCLASSED".
  - flow-steps [transitions] rows read "planning | `plan.exit` | designing", "testing | `test.exit` | deploying".
  - 0098 says only "the engine refusing any transition it lacks".
- **Consequence:** dDeclaredLoop's engine is specced against witnesses no ancestor produces, so its acceptance cannot be planted from real items.
- **Fix:** In 0098, have each row name the exit item by tag, with a fixture witness until its build lands. Class the seven Stage 0 leads in [stage0-classes].

### C2-F3 — The runaway ceiling gets two homes and two rules for whether a round count at the ceiling is allowed
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0106`, against `cl-dClosedLoop-0139`
- **Class:** K9
- **Severity:** medium
- **Evidence:**
  - 0106: "`RUNAWAY_CEILING`, moved into the loop kit's definition … and a planted round count at the ceiling refused".
  - The catalogue (v2:1127): `review.design.round-count` is "held at or below `review.max-rounds`, the loop kit's runaway ceiling, which dDeclaredLoop moves out of unattended into the policy file". v2:1128 says `review.max-rounds` is "`RUNAWAY_CEILING` made a policy value".
  - The pair rule (v2:1299): "`review.design.round-count` is at most `review.max-rounds`". 0139 says the same: "held at or below `review.max-rounds`".
  - The code today refuses at or above the ceiling: `tools/unattended/unattended.sh:783` reads `[ "$REVIEW_ROUNDS" -lt "$RUNAWAY_CEILING" ]`.
- **Consequence:** A repository that sets `round-count = max-rounds` passes dKeptSession's preset check and is refused by dDeclaredLoop's arm. The ceiling also ends up both as a loop-kit constant and as a policy key, so a spec writer has to pick one.
- **Fix:** In 0106, say the ceiling becomes the policy key `review.max-rounds`, and plant "a round count above `review.max-rounds` refused, one equal to it admitted", matching the pair rule.

### C2-F14 — The commit kind's position-engine reader has no writer until the commit queue lands
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0108`
- **Class:** K3
- **Severity:** medium
- **Evidence:**
  - 0108: "… and the position engine reading them".
  - Stage 0 K3: "commit: no writer item … written by the commit queue". memory-plan:157 names the writer as "the commit queue from the act binding", which is dWellOiledMachine's.
  - gap-spine-08: "0 of 6,084" commits carry the item, act or session that made them.
- **Consequence:** Between dDeclaredLoop and dWellOiledMachine, the engine reads `Gov-*` trailers that no commit carries. Position then falls back to subject parsing with no rule saying so.
- **Fix:** State 0108's interim: until the commit queue writes the trailers, the engine reads the subject view, seen on today's commits. Name the writer by tag.

## Clean cells to attack

- `cl-dClosedLoop-0079` in dFairHearing
- `cl-dClosedLoop-0092` in dDeclaredLoop
- `cl-dClosedLoop-0378` in dRankedPlan
- `cl-dClosedLoop-0421` in dShippedRelease
- `cl-dClosedLoop-0167` in dBoundRoles
- `cl-dClosedLoop-0429` in dShippedRelease
- `cl-dClosedLoop-0336` in dWellOiledMachine
- `cl-dClosedLoop-0439` in dShippedRelease

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <clause> <build>: holds`, or `- <clause> <build>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `CS1-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-c1/` only. Your effort is the one the owner's
role definition sets.
