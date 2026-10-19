# Walk return: run C, walker 1, dTrueNorth to dOrderedCharter

**Serves:** research PLAY-dClosedLoop-1

Dispatch 185's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-26-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed because one of these clauses left out a rule its records had already settled for it. dOrderedCharter re-founded the charter, moved the join factory and put the tags pack in place. In doing that it dropped the `required-by` field, the charter's section-1 reader, three tag keys and the adopter path for `tools/lib`. Its landing then went red or broke every adopter's update.

### C1-F1 — The unit registry leaves out `required-by`, so the missing-unit refusal has nothing to read
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0039, read with cl-dClosedLoop-0041
- **Class:** K6, c3
- **Severity:** high
- **Evidence:** layer-instruction `[recommendations]` R-A lists the unit row's fields, including "`required-by`: the roles and items that require it, which R-C's 'too little' refusal reads". Systems `[design-instruction-writing]` also lists "`required-by`, `enforced-by`". cl-0039 lists the fields as "tag, level, statement type, scope tags, trigger, budget class, source, origin … `usage` … `help` … and class", with no `required-by`. cl-0041 still says load sets are "refused when missing a required unit". I grepped `[chain]` for `required-by`: there are 0 hits, so no clause registers the field.
- **Consequence:** The P27 load-set check has no declared list of required units. It either stays green over nothing, or the builder makes the field up. The adopter-instructions item 6 exclusion refusal ("one another active unit requires") also has nothing to read.
- **Fix:** Add `required-by` and `enforced-by` to cl-0039's field list. Make cl-0041 read `required-by`, and plant a red: a unit named in `required-by` that is missing from a load set.

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

### C1-F14 — dGroundRules' witness needs load sets and a composition that only dOrderedCharter builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0015
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0015 is "seen … on a load set missing a required unit and a composition over a harness's own limit, both still refused under `warn`". Load sets are cl-0041's and the composition is cl-0064's, both in dOrderedCharter, a descendant.
- **Consequence:** dGroundRules' acceptance cannot be run when it lands.
- **Fix:** Plant today's consumer limit at dGroundRules (agent-instructions' `CODEX_MAX`), and move the load-set and composition cases to cl-0041 and cl-0064.

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

### C1-F17 — The render gate's legacy list is hard-wired shrink-only, so strict's `instructions.legacy: refuse` has no arm
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0050
- **Class:** K9
- **Severity:** low
- **Evidence:** Catalogue: "`instructions.legacy` | shrink-only, refuse | … IW-1 arms the render gate at dOrderedCharter". The strict preset sets `refuse`. cl-0050 says "the render gate armed with a shrink-only legacy list (IW-1)".
- **Consequence:** Under strict, a legacy document is still admitted.
- **Fix:** In cl-0050, read the gate's mode from `instructions.legacy`, with each value planted.

### C1-F18 — "A ninth join": spec-tokens already has nine
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0002
- **Class:** K6
- **Severity:** low
- **Evidence:** cl-0002 calls the carries join "a ninth join of the spec tokens leg". Probe on `tools/check-spec-tokens.py`:
  - The docstring names legs, paths, cites, bar, guards, claims, handoff (seventh) and size (eighth).
  - Line 960 has "THE COVERS JOIN (TOOL-aMendedFleet-75)".
- **Consequence:** The count is stale, and a builder looking for the ninth slot finds `covers` there.
- **Fix:** Call it "a further join".

### C1-F19 — "Instruction packs … into the preset catalogue" clashes with the rule that presets never touch `charter.practices`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0045
- **Class:** K9
- **Severity:** low
- **Evidence:** cl-0045: "instruction packs extending `charter.practices` into the preset catalogue". v2 `[presets]`: "Presets never touch … `charter.practices`".
- **Consequence:** A builder may add packs to the policy presets and go against the never-touch rule.
- **Fix:** Name it "a pack catalogue", separate from the policy presets.

### C1-F20 — The card for other harnesses goes through Runtime harness adapters, which dWellOiledMachine builds later
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0038
- **Class:** K6
- **Severity:** low
- **Evidence:** cl-0038: "another harness's through its Runtime harness adapter". layer-instruction R-K: load points per harness "come from Runtime's harness adapters" (`runtime.harnesses`, Owner dWellOiledMachine).
- **Consequence:** There is no adapter to deliver through when the build lands, and no stand-in is named.
- **Fix:** Name agent-instructions' wiring as the stand-in until the adapters land.

| clause | build | read against | verdict |
|---|---|---|---|
| cl-dClosedLoop-0001 | dTrueNorth | final-questions [spine] [coverage]; whole-audit [instruments]; v2 P33, P41; memory-plan [edges] | C1-F8 |
| cl-dClosedLoop-0002 | dTrueNorth | final-questions [coverage] join arms; tools/check-spec-tokens.py | C1-F18 |
| cl-dClosedLoop-0003 | dTrueNorth | final-questions [coverage] owner's report, [bootstrap]; gap-design-13 | holds |
| cl-dClosedLoop-0004 | dTrueNorth | final-questions [deviation] [spine]; stage0 leads; v2 catalogue deviation.approval; gap-build-07 | C1-F7, C1-F9 |
| cl-dClosedLoop-0005 | dTrueNorth | final-questions [bootstrap]; memory/HYGIENE.md record bindings | holds |
| cl-dClosedLoop-0006 | dTrueNorth | final-questions [spine] [deviation]; cl-0058 and cl-0063; gap-mem-47 | C1-F7 |
| cl-dClosedLoop-0007 | dGroundRules | v2 [policies] empty-set rule; shape-reviews `empty-sets`; final-questions [folded]; gap-spine-06 | holds |
| cl-dClosedLoop-0008 | dGroundRules | v2 [policies]; tools/push-main.sh, .githooks/pre-push read_policy_key | holds |
| cl-dClosedLoop-0009 | dGroundRules | v2 [policies], [presets] rules; standard vs defaults comparison | holds |
| cl-dClosedLoop-0010 | dGroundRules | v2 `policy-file.on-invalid` row; [presets] | holds |
| cl-dClosedLoop-0011 | dGroundRules | v2 [policies] mirror text, `policy-file.on-invalid` | holds |
| cl-dClosedLoop-0012 | dGroundRules | shape-reviews SA-12; adopter-instructions [chain]; v2 [witnesses] | holds |
| cl-dClosedLoop-0013 | dGroundRules | v2 [policies] kit-conf passage; .githooks/gate-env.sh header and keys; .githooks/pre-push GATE_POST_MERGE | holds |
| cl-dClosedLoop-0014 | dGroundRules | v2 catalogue Owner column; stage0 K4 leads | holds |
| cl-dClosedLoop-0015 | dGroundRules | night-pass-two [p5-caps]; v2 `budgets.*`, `budgets.enforce`, `budgets.pinned`; P9; gap-tool-24 | C1-F13, C1-F14 |
| cl-dClosedLoop-0016 | dGroundRules | night-pass-two [p7-agent-cap] [answers]; v2 `runtime.agents-in-flight`; tools/hooks/agent-cap.js, README.md; P38; gap-rt-34 | C1-F5 |
| cl-dClosedLoop-0017 | dGroundRules | v2 P39, `run.on-owner-silence`, `flow.rework-budget` rows | holds |
| cl-dClosedLoop-0018 | dSafePassage | shape-reviews `released-steps-frozen`; P38; gap-deploy-15, gap-deploy-16 | holds |
| cl-dClosedLoop-0019 | dSafePassage | shape-reviews `walk-failure-route`, SA-2; gap-deploy-19 | holds |
| cl-dClosedLoop-0020 | dSafePassage | shape-reviews `receipt-schema`; tools/govkit/govkit.py RECEIPT_SCHEMA and back-fill scope | holds |
| cl-dClosedLoop-0021 | dSafePassage | shape-reviews `walk-failure-route`; gap-deploy-17 | holds |
| cl-dClosedLoop-0022 | dSafePassage | shape-reviews SA-8; gap-tool-10 | holds |
| cl-dClosedLoop-0023 | dSafePassage | v2 `install.deprecation-window`, `install.on-shim-call`, pair rule; SA-8; gap-deploy-24 | holds |
| cl-dClosedLoop-0024 | dSafePassage | shape-reviews `step-contract`; dShippedRelease cl-0435 | holds |
| cl-dClosedLoop-0025 | dSafePassage | shape-reviews SA-3; adopter-instructions [reviewed]; gap-deploy-20 | holds |
| cl-dClosedLoop-0026 | dSafePassage | v2 `install.retired-edits`; research-supersession F5; govkit selfcheck 7g; gap-deploy-18 | C1-F15 |
| cl-dClosedLoop-0027 | dSafePassage | shape-reviews SA-11; flow-roles-adoption item 14; gap-deploy-25 | holds |
| cl-dClosedLoop-0028 | dSafePassage | P37; v2 `platforms.provision`; shape-reviews `floor-query`; tools/settings-merge.py; merge-rows.test.sh PEP 701 ban; gap-tool-12, gap-tool-22 | C1-F16 |
| cl-dClosedLoop-0029 | dSafePassage | gap-tool-23; shape-reviews `emitted-ci-pins` | holds |
| cl-dClosedLoop-0030 | dSafePassage | final-questions [help]; v2 `help.enforce`; P42; gap-found-35 | holds |
| cl-dClosedLoop-0031 | dOrderedCharter | foundations step 1 settled; v2 `charter.practices`, P14 | holds |
| cl-dClosedLoop-0032 | dOrderedCharter | v2 [front-door]; foundations step 1; layer-instruction R-B; tools/roles/roles_lib.py; gap-flow-02, gap-found-18; stage0 K3 override | C1-F2, C1-F10, C1-F11, C1-F12 |
| cl-dClosedLoop-0033 | dOrderedCharter | foundations R2; P13 | holds |
| cl-dClosedLoop-0034 | dOrderedCharter | foundations R2 re-derivation; gap-found-01 | holds |
| cl-dClosedLoop-0035 | dOrderedCharter | foundations step 1; gap-found-03 | holds |
| cl-dClosedLoop-0036 | dOrderedCharter | foundations R3, F1-6; night-pass-two [p5-caps] item 5; tools/template-size-limits.txt | holds |
| cl-dClosedLoop-0037 | dOrderedCharter | foundations [core] C1 to C7; stage0 K3 exception lead; gap-found-07, gap-found-08 | C1-F12 |
| cl-dClosedLoop-0038 | dOrderedCharter | layer-instruction R-K; gap-orient-13 | C1-F20 |
| cl-dClosedLoop-0039 | dOrderedCharter | layer-instruction R-A; systems [design-instruction-writing] unit fields; memory-plan [sites] | C1-F1 |
| cl-dClosedLoop-0040 | dOrderedCharter | systems [design-tags] grammar, namespaces, owners; flow-roles-adoption [renamed] | holds |
| cl-dClosedLoop-0041 | dOrderedCharter | layer-instruction R-C; P27; night-pass-two [p5-caps]; v2 `instructions.checks`, `budgets.*`; gap-found-10, gap-found-34 | C1-F1, C1-F13 |
| cl-dClosedLoop-0042 | dOrderedCharter | layer-instruction R-D; P11; gap-found-11 | holds |
| cl-dClosedLoop-0043 | dOrderedCharter | layer-instruction R-G; v2 [front-door] ladder | holds |
| cl-dClosedLoop-0044 | dOrderedCharter | layer-instruction R-H; P30; gap-found-14 | holds |
| cl-dClosedLoop-0045 | dOrderedCharter | layer-instruction R-I; v2 `instructions.edit`, `instructions.proof`, [presets] never-touch list; gap-found-15 | C1-F19 |
| cl-dClosedLoop-0046 | dOrderedCharter | P28; tools/memory-tree imports from memory-recall (row_grammar.py, backlog.py, corpus_ids.py, merge-rows.py, transition_audit.py, gen_build_index.py); gap-found-17 | holds |
| cl-dClosedLoop-0047 | dOrderedCharter | P28; core-kit references to optional kits over tools/; gap-found-17 | holds |
| cl-dClosedLoop-0048 | dOrderedCharter | grep of extract.py and recall_conf readers by path; check-verdict-epoch.sh DELEGATES | C1-F6 |
| cl-dClosedLoop-0049 | dOrderedCharter | systems [design-tags]; v2 tags.* keys; stage0 K4; tools/codebase-map/map_lib.py consumers; tools/lib inline rule; gap-found-33 | C1-F3, C1-F4 |
| cl-dClosedLoop-0050 | dOrderedCharter | systems [design-instruction-writing] renderer and checks; v2 `instructions.legacy`; gap-found-23 | C1-F17 |
| cl-dClosedLoop-0051 | dOrderedCharter | v2 [front-door] (IW-2); P14; gap-found-02 | holds |
| cl-dClosedLoop-0052 | dOrderedCharter | v2 `memory.map-purpose`; owed PM-5 | holds |
| cl-dClosedLoop-0053 | dOrderedCharter | P4, P20; v2 `attendance` | holds |
| cl-dClosedLoop-0054 | dOrderedCharter | P33; memory-plan [edges]; gap-found-24, gap-found-25 | holds |
| cl-dClosedLoop-0055 | dOrderedCharter | v2 `tags.bundle`, `tags.bundle-rows`; systems [design-tags] | holds |
| cl-dClosedLoop-0056 | dOrderedCharter | v2 `tags.positional`; night-pass NP-17; gap-found-26 | holds |
| cl-dClosedLoop-0057 | dOrderedCharter | v2 `memory.code-budget`; P27, P32 | holds |
| cl-dClosedLoop-0058 | dOrderedCharter | memory-plan [sites] [edges]; shape-reviews `edge-grammar`, `p33-addresses`; gap-mem-35 | C1-F8 |
| cl-dClosedLoop-0059 | dOrderedCharter | memory-plan [practice] [doors]; shape-reviews `p34-rationale-owned` | holds |
| cl-dClosedLoop-0060 | dOrderedCharter | P37; shape-reviews `p37-legs-missing`; gap-tool-19 | holds |
| cl-dClosedLoop-0061 | dOrderedCharter | adopter-instructions [design] items 16 and 17; shape-reviews `unattended-inventory`; P38; gap-found-30 | holds |
| cl-dClosedLoop-0062 | dOrderedCharter | adopter-instructions [design] items 1 to 8, [reviewed]; systems [design-tags]; P8; gap-found-29 | holds |
| cl-dClosedLoop-0063 | dOrderedCharter | adopter-instructions items 9 and 10, [reviewed]; v2 `instructions.stale` | holds |
| cl-dClosedLoop-0064 | dOrderedCharter | adopter-instructions items 12, 14 and 16; night-pass-two [p5-caps]; P8; gap-found-31 | holds |
| cl-dClosedLoop-0065 | dOrderedCharter | flow-roles-adoption [design] items 2 to 6, 13 and 14, [renamed] | holds |
| cl-dClosedLoop-0066 | dOrderedCharter | flow-roles-adoption [design] items 6, 9 and 10, [chain] | holds |
| cl-dClosedLoop-0067 | dOrderedCharter | final-questions [help]; P42; systems unit `usage` and `help` fields | holds |

| dTrueNorth | C1-F7, C1-F8, C1-F9, C1-F18 |
|---|---|
| dGroundRules | C1-F5, C1-F13, C1-F14 |
| dSafePassage | C1-F15, C1-F16 |
| dOrderedCharter | C1-F1, C1-F2, C1-F3, C1-F4, C1-F6, C1-F8, C1-F10, C1-F11, C1-F12, C1-F13, C1-F17, C1-F19, C1-F20 |

**Read outside the list above:** `C:\Users\d41ly\.claude\projects\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\tool-results\b8lzzp252.txt` and `C:\Users\d41ly\.claude\projects\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\tool-results\bjlpxtsi1.txt`. The harness saved two of my own command outputs over the sealed copy to these files when they ran long. I opened the second one, which holds v2's four `[chain]` rows split at the clause ids, to read those rows.
