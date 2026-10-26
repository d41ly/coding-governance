**Serves:** spec-audit TOOL-dBoundRoles-1@rev-1 TOOL-dBoundRoles-10@rev-1 TOOL-dBoundRoles-11@rev-1 TOOL-dBoundRoles-12@rev-1 TOOL-dBoundRoles-13@rev-1 TOOL-dBoundRoles-14@rev-1 TOOL-dBoundRoles-15@rev-1 TOOL-dBoundRoles-16@rev-1 TOOL-dBoundRoles-17@rev-1 TOOL-dBoundRoles-18@rev-1 TOOL-dBoundRoles-19@rev-1 TOOL-dBoundRoles-2@rev-1 TOOL-dBoundRoles-20@rev-1 TOOL-dBoundRoles-21@rev-1 TOOL-dBoundRoles-22@rev-1 TOOL-dBoundRoles-23@rev-1 TOOL-dBoundRoles-24@rev-1 TOOL-dBoundRoles-25@rev-1 TOOL-dBoundRoles-26@rev-1 TOOL-dBoundRoles-3@rev-1 TOOL-dBoundRoles-4@rev-1 TOOL-dBoundRoles-5@rev-1 TOOL-dBoundRoles-6@rev-1 TOOL-dBoundRoles-7@rev-1 TOOL-dBoundRoles-8@rev-1 TOOL-dBoundRoles-9@rev-1

# Tier-2 spec audit — dBoundRoles, the 26 unit specs (round 1)

Provenance: the dBoundRoles spec stage, written 2026-10-25 and recorded at the spec commit 4914545b1. Finders ran as gov-spec-reviewer, skeptic batches as gov-skeptic, and this synthesis as gov-synthesizer.

Reviewed: memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md@1a8b713c1e72e8e508503542bbb9dc82bf487819, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-10.md@aa9085df5e071db3e99a107960b4a1c4805e7cbc, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-11.md@861d210a209f0cb9df47e07157f7c3b6b41ee6c2, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-12.md@56ba26a0430979f6b2ba901f3c150716a6e3dd10, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md@34612dafcc6beb5d3631651b46e762640c8e68e3, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md@79b4c7aaa6ea08117816f8ddee92c5570cc4c645, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-15.md@3d782825c2cb765a428f98c2e32bf0173d82595f, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-16.md@3a93c94500c56f952812951a3ce727db1d091e1e, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md@da9db7ef4afa652576dcd9096371bf27b118187f, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-18.md@45c778d9ee0472c61265d578ac1227371ea527e7, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-19.md@dadb1b5a4ab0d1de53ac0a266e0925a39eac7b6d, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-2.md@37971026662e45d96d101bfe225b8f86fc083fd7, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-20.md@6463e0773da582b763b188848cc42c86a61e337d, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md@dc713135e2e65b7bbab7e1ff08a77ff8ca87379f, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-22.md@8650c0d687de44a1b3e7ccb7f898747da669c12d, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-23.md@7cfeb8732a96c23487d23c755051c72bf14dec92, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-24.md@96afddc80e97d3953b2a918fb86f1a7c45c653e0, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md@22697fcfa8fbaa43aeb33740de5d748c29e3f6ae, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-26.md@13ce75b41c6394e377f164af7be3ccfa2cffc38a, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-3.md@e5bb8cea81e6781cb11df2040c88c795c18ac073, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-4.md@bbaf5b081560f25d7099ab1265fa18ec2666d2a5, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-5.md@e8a86f1fc9eea5aae38a5f3ed6c6e03bee1d1182, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-6.md@c2da5573f7544c0c176485206b49dbc1853bdf38, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-7.md@5aa2bebfdff93ee93ca825fb44e6e0605187d86b, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-8.md@1e88005abcd28ea06964b712bdfa4c1b56286871, memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-9.md@0a97517ecb00eb7a90a261f913933268335be90a

ROUND: 1

## Verdict: CLEAN WITH FIXES

No blocker survived the skeptics. Six high findings did, in five items, and every one of them must be fixed in its spec before the build pass that implements that unit.
The tally is 57 items over 63 confirmed findings: 0 blocker, 5 high items (6 findings), 39 medium items (43 findings), 13 low items (14 findings).
No project bug-class checklist was swept, so the zero blocker count is not evidence that the project's recurring classes are absent.
Each fix below is a spec edit. No code is touched by this report.

## Review shape

Intensity full, raw 64, confirmed 63, refuted 1, unverified 0 (0 uncertain), precision 0.98.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 20 | 20 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 10 | 9 | 1 | 0 | 0 | 0.90 |
| reuse | yes | 11 | 11 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 10 | 10 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |

The adjudicated tally counted by item: 0 blocker, 5 high, 39 medium, 13 low (57 items).
The same tally counted by raw confirmed finding: 0 blocker, 6 high, 43 medium, 14 low (63 findings).
The one refuted finding, id 23, was a duplicate of id 16.

### Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 57 judged sound, 6 judged UNSOUND (ids 22, 33, 34, 45, 52, 61), 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 left ungraded by the skeptic, 9 re-graded by the skeptic (ids 1, 2, 3, 33, 48, 53, 54, 55, 57).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 1 spec document was supplied as `specs`, as sibling context.
- Checklist: none swept.
- By design: none supplied, from neither the caller nor a block.
- Move check: no checked subject moved.

Every integrity counter that would make the run incomplete is zero, so the run is complete within the lenses it ran.

Three defects were each found once at high and once at medium. They are split across two items because items merge only findings of one binding grade. Each pair cross-references the other, and no id is counted twice. The pairs are id 22 with id 53, id 42 with id 3, and id 4 with id 47.

## High

### H1. check-return grades and blocks every typed harness stage (ids 21, 56)

- **Where:** TOOL-dBoundRoles-5, section 2 S2 and S3, and section 4 "The direct route" and Rollout.
- **What is wrong:** check-return is wired on `SubagentStop` with matcher `*`. It exits early only when `agent_type` is missing or names no agent-true role. Harness stages are spawned with gov-* agent types (unattended-unit.js:333-337, unattended-build.js:542, tier2-review.js:271), so their stops fire the hook too. The spec treats SubagentStop as an event that only direct spawns raise. Nothing separates a direct spawn from a harness agent.
- **Consequence:** A harness agent returns through StructuredOutput against its stage schema. For gov-builder that schema is {committed, sha, why, summary}, while unit 2 gives the role the template `outcome:committed|returned, ...`. The hook finds no return object, or a missing `outcome`, and answers `{"decision":"block"}` up to `roles.retries` times (default 3). It then records `valid: false` under `return-check/<agent_id>.json`, and TOOL-dBoundRoles-26 routes on that record. This hits every unattended unit build and every typed tier2 finder, skeptic and synthesizer.
- **Fix (skeptic judged it sound):** In S2, grade only a direct spawn. A direct spawn is one whose agent transcript's first user record opens with a `gov:handoff` marker that MARKER_RE parses. Exit 0 and print nothing otherwise, and also when `agent_transcript_path` lies under `subagents/workflows/`. State this in section 4. Add a plant `harness-typed-stop`: a SubagentStop payload with agent_type gov-builder (or gov-reviewer) whose transcript sits under `subagents/workflows/<run>/`, with no marker and a plain-text last message, must print nothing and write no record. Add an AC that goes red when such a payload is blocked. Confirm with a recorded payload that SubagentStop fires for workflow agents.
- **Left-shift gate:** A hook self-test arm that replays a recorded harness-stage SubagentStop payload against every new SubagentStop or SubagentStart hook and fails on any output.

### H2. The anchor check refuses work orders that hand over specs quoting the key grammar (id 22)

- **Where:** TOOL-dBoundRoles-24, section 4 "What an anchor is" (the corpus measurement), section 4 "The check", and section 4 Migration.
- **What is wrong:** The claim that the check raises no false red was measured over `memory/builds/*/prompts/` at base, where handed inputs are paths. After TOOL-dBoundRoles-13, specs, briefs and cards are handed as raw content inside `## Task`. check_anchors scans the whole section and strips only fenced blocks. 27 backticked `blob:`/`record:`/`cmd:` spans in 6 tracked specs fail KEY_FORMS. These include TOOL-dBoundRoles-13 and -24 themselves, PLAY-dOrderedCharter-9:51 and aEvidencedLens-3:223.
- **Consequence:** `handoff.py render` refuses the builder work order for unit 24, for unit 13, and for any spec that quotes the grammar or the evidence convention. A review finding handed as input carries the same `cmd: ...` spans. The Migration line "the first render after landing refuses nothing that rendered before" is false. Item M30 (id 53) is the same defect at medium.
- **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Have render_handoff leave each handed fact's content out of the check by the block extents it assembled itself, not by scanning for headings. Call check_anchors over the task section with every handed input or fact body omitted, so only framing, upstream and typed-argument text is graded. Add a plant that renders a builder handoff whose `input:spec` is a spec quoting `cmd:<command>` and a well-formed example key in prose, outside any fence. It must render, and the AC goes red if it refuses.
- **Left-shift gate:** Re-measure a refusal predicate's false-red rate over the population it will actually read after its predecessors land, and record that population in the spec's measurement line.

### H3. Unit 25's AC14 can pass only if append-only records are rewritten (id 42)

- **Where:** TOOL-dBoundRoles-25, section 6 AC14 and section 2 S8 Readers.
- **What is wrong:** AC14's grep `git grep -l -F 'agent-cap.js' -- ':!memory/builds' ':!memory/ledger' ':!.governance/steps'` must print only kit.toml, the govkit selftest, the step program and govkit fixtures. At HEAD it also prints 21 memory files that S8 leaves out: memory/DECISIONS.md, memory/archive/DECISIONS.2026-08-10.md, seven archive template-v-2 files, memory/backlog/TOOL.md, five gotcha pages, four memory/map/generated renders, and memory/project/spec-token-waivers.txt (row 29).
- **Consequence:** AC14 stays red after a correct pass. The only way to green it is to edit records that check-dead-paths.sh's own header calls append-only, which falsifies them. Item M3 (id 3) is the same defect at medium.
- **Fix (skeptic judged it sound):** Scope AC14 to live carriers. Either exclude `':!memory'` and grade memory/gotchas and memory/map/features on their own (see M22), or list the record paths as expected output. Add spec-token-waivers.txt and the memory/map/generated renders to S8's dispositions.
- **Left-shift gate:** A spec-lint check that runs each AC's literal grep at the spec's base and flags any hit under an append-only record folder.

### H4. Fact lines inside handed content read as executor lines (id 52)

- **Where:** TOOL-dBoundRoles-13, section 2 S3 and S4, and section 4 "The fact line" and "The re-cut".
- **What is wrong:** S3 pastes handed content into `## Task` raw, with no fence or escape. S4's spawn guard re-derives every FACT_RE line in the task section, so a quoted fact line looks exactly like one the executor wrote. TOOL-dBoundRoles-13's own line 99 is such a line, keyed to a missing `memory/builds/tFix/...` path. Three tracked specs (aOrientedCast-2, -7, PLAY-dOrderedCharter-5) hold `<!-- gov:handoff role=` lines.
- **Consequence:** Handing spec 13 to its builder makes the re-derive refuse every time, so that unit can never be spawned by the direct route. A quoted line also carries a class its author typed, which breaks P29's rule that no agent types a class. A quoted marker breaks TOOL-dBoundRoles-4's exactly-one-marker rule.
- **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** In S3, wrap each handed block's content in a backtick fence longer than the longest backtick run in that content, with the fact line outside and before the fence. Make FACT_RE's Python reader and its JS copy in S4 fence-aware, so they skip every line inside a block's fence. Apply the same rule to spec 4's marker reader for the prompt writer's file. Add an AC that hands over a scratch spec holding three things: a FACT_RE line with a made-up path, a `### ` heading followed by a fact line, and a `<!-- gov:handoff role=` line. The render's fact set, the spawn guard and the single-marker rule must all ignore them.
- **Left-shift gate:** A bug-class checklist entry: "untrusted content embedded in a machine-read document must be fenced, and every reader of that document must be fence-aware".

### H5. govkit's self-test hard-codes the counts unit 1 changes (id 4)

- **Where:** TOOL-dBoundRoles-1, section 4 Files touched and section 7 Gates, against S2 and S3.
- **What is wrong:** `tools/govkit/selftest.py:2837-2838` checks `len(agents) == 9` and ten house overlays. Unit 1 adds four roles with empty overlays and removes two, which gives about 11 agent types and 12 overlays. Neither selftest.py nor the `govkit selftest` leg appears in unit 1's write set or gate line.
- **Consequence:** The leg's guard covers `{prefix}/govkit/` and not tools/roles, so a guarded run skips it. The break then surfaces on a later, unrelated govkit change and misleads that change. Unit 19 re-points "the OC8 count of ten", a count unit 1 has already broken. Item M25 (id 47) is the same defect at medium.
- **Fix (skeptic judged it sound):** Add `tools/govkit/selftest.py` (the OC8 AC4 counts, derived rather than typed) to unit 1's S3 Readers and Files touched, and `govkit selftest` to its section 7 leg line. In unit 19, re-point the derived count, not "ten".
- **Left-shift gate:** Widen the `govkit selftest` leg guard in tools/gate-legs.json to cover tools/roles/ seed and agent paths, or derive the counts so that no literal is left to drift.

## Medium

### M1. Unit 2's return grammar rejects five of its own templates (id 1)

- **Where:** TOOL-dBoundRoles-2, section 4 "The return template", against S4 and AC3.
- **What is wrong:** The grammar `value ("|" value)+` needs two or more values, and the spec makes a set of one value an R2 defect. The table nevertheless gives one-value outcomes to gov-spec-writer (`done`), gov-skeptic (`judged`), gov-synthesizer (`reported`), gov-orienter (`oriented`) and gov-session (`sent`).
- **Consequence:** R2 reds five gov roles, so AC3's "over the tree it exits 0" cannot pass. The builder would have to quietly change either the grammar or the templates.
- **Fix (skeptic judged it sound):** Do one of two things. Either admit a one-value closed set for `outcome` (for example `value ("|" value)*`) and say so in S4, or give each of the five roles a second outcome value that its base `returns` sentence supports. Add a criterion that runs `check_roles.py` over gov's real tree with the ten templates.
- **Left-shift gate:** Every spec that adds a catalogue rule gets an AC that runs the checker over gov's own tree.

### M2. Unit 25's AC3 asks for a shape refusal that no unit builds (id 2)

- **Where:** TOOL-dBoundRoles-25, section 6 AC3, against TOOL-dBoundRoles-16 section 4 "The readers" and section 8 F3.
- **What is wrong:** AC3 wants the moved guard to refuse a role whose index `shapes` lacks the harness entry's `kind`. Unit 16's F3 leaves agent-cap's `args.roles` refusal unchanged, and its index records no harness kind. Unit 25 moves each rule as it finds it.
- **Consequence:** Nothing produces AC3's exit 2, so the criterion cannot pass. The section 3 edge from unit 16 contradicts unit 16.
- **Fix (skeptic judged it sound):** Either drop AC3 and its edge text, or give one unit an S-item that renders each harness entry's `kind` into the index and adds the shape refusal to `checkHarnessCall`. That unit would be unit 16 with F3 reversed, or unit 25 as a stated change. Then AC3 and its New arm observe that S-item.
- **Left-shift gate:** A spec-lint join under which every AC must cite an S-item of its own unit or a landed predecessor's.

### M3. Unit 25's AC14 grep catches historical memory files (id 3)

- **Where:** TOOL-dBoundRoles-25, section 6 AC14 and section 2 S8 Readers.
- **What is wrong and its consequence:** This is the defect in H3 (id 42), found by the coherence lens and graded medium by the skeptic. AC14 excludes only `memory/builds`, `memory/ledger` and `.governance/steps`. Historical and generated memory files would still match: DECISIONS, the archive, the backlog, the gotchas, map/generated and spec-token-waivers. A builder either fails AC14 or edits frozen history.
- **Fix (skeptic judged it sound):** Add the historical record folders to AC14's exclusions, or list them in S8 with the disposition "historical, unchanged". Say whether map/generated and spec-token-waivers.txt are regenerated or re-pointed. Re-derive the reader list with the stated command.
- **Left-shift gate:** As H3.

### M4. Unit 1 claims three tools/workflows readers but leaves them out of its write set (id 5)

- **Where:** TOOL-dBoundRoles-1, section 2 S3 Readers against section 4 Files touched, and TOOL-dBoundRoles-18 AC7.
- **What is wrong:** S3 re-keys `tools/workflows/README.md`, `tier2-review.test.sh` and `unattended-build.test.sh` "in this unit", but Files touched leaves them out.
- **Consequence:** Files touched is machine-read to decide which legs are owed, so the legs for these files are missed. Unit 18's AC7 grep depends on the edit.
- **Fix (skeptic judged it sound):** Add the three files to unit 1's Files touched with their re-keying (the FULL maps, OC_ROLES and the README examples). Add a criterion such as unit 18's grep, run at unit 1's pass. Alternatively move the files into unit 18's write set and change its S7 to match.
- **Left-shift gate:** A spec-lint join under which every path an S-item names as edited must appear in Files touched.

### M5. Unit 26's refusal rule reds gov's own prompt writer (id 6)

- **Where:** TOOL-dBoundRoles-26, section 4 "The arm", against TOOL-dBoundRoles-4 S2.
- **What is wrong:** Unit 26 refuses any role whose `return` redeclares `outcome: refused`. Unit 4, which lands earlier, gives gov-prompt-writer `outcome:framed|refused, ...`.
- **Consequence:** The `roles catalogue` leg reds on gov's own role, and the fix lies outside unit 26's write set. If the checker does not match a `refused` value, the rule fails to do what it claims.
- **Fix (skeptic judged it sound):** Either have unit 4 drop `refused` and re-point its render refusal to the arm's `outcome: refused`, or add `gov-prompt-writer.agent.md` and the change to unit 26's S1 and Files touched. Add a criterion that `check_roles.py` over gov's tree exits 0.
- **Left-shift gate:** As M1.

### M6. Unit 21 moves the gate rows but not the `## Ceiling` reader (id 7)

- **Where:** TOOL-dBoundRoles-21, S6 and S7, against TOOL-dBoundRoles-2 section 4 "The rendered block".
- **What is wrong:** Unit 2 hands the re-point of `render_role(..., gates=)` to unit 21. Unit 21's reader list never names it.
- **Consequence:** Once the house rows move, gov-builder and gov-spec-writer render "gate legs: none" while the index still grants them legs. Unit 2's AC5 regresses without anything going red.
- **Fix (skeptic judged it sound):** Add both `render_role` callers to S7, reading the role field with the house row as fallback (the `check_gate_names` path). Add a criterion that `.claude/agents/gov-builder.md`'s `## Ceiling` still lists the leg after the move.
- **Left-shift gate:** A spec-lint join under which a hand-off phrase "TOOL-X re-points ..." must appear in TOOL-X's reader list.

### M7. Unit 15's `budget` schema row does not follow unit 2's grammar (ids 8, 32)

- **Where:** TOOL-dBoundRoles-15, S2 and section 4 Data model, against TOOL-dBoundRoles-2 S1 and section 4 "The schema".
- **What is wrong:** Unit 15 writes the row with `type = "integer"` and `meaning`, and adds `budget` by hand to `FRONT_MATTER_KEYS`. Unit 2 derives that tuple from `role-schema.toml` rows keyed `key`/`owner`/`shape`/`required`. Its closed shape set has no integer shape.
- **Consequence:** `load_role_schema` refuses the invalid row with an R2 RolesError, so every roles run refuses at load. The alternative is a key typed beside the schema, which unit 2's AC6 reds.
- **Fix (skeptic judged it sound):** Write one `[[field]]` row in unit 2's grammar (`key = "budget"`, `owner = "gov"`, `shape = "int"`, `required = "every"`). Drop `type`, `meaning` and the hand edit to `FRONT_MATTER_KEYS`. Add an `int` shape to spec 2's shape table now, or name the unit that adds it. Units 1, 16 and 21 also need their shapes (`layer`, `acts-as`, `effort`, `shapes`) in that table.
- **Left-shift gate:** Validate every schema row quoted in a spec against the schema grammar stated in the spec that owns it.

### M8. Unit 19 counts the base tree's ten house files (id 9)

- **Where:** TOOL-dBoundRoles-19, S5 and S6, Files touched, AC1 and AC2.
- **What is wrong:** "Ten" and "the other nine" are base figures. After unit 1 the kit holds twelve house files.
- **Consequence:** AC1 and AC2 cannot be met as stated, and unit 1's overlays could be left behind under a seed rule that no longer lists them.
- **Fix (skeptic judged it sound):** Derive the count from the kit's seed list at the pass ("every seeded `house/*.md`"). Drop "ten" and "nine", and name unit 1's four new overlays in S6.
- **Left-shift gate:** A checklist entry: a spec's numeric figures must be stated against the tree its predecessors leave, not against base.

### M9. Unit 18 appends house text that unit 19 no longer renders (id 10)

- **Where:** TOOL-dBoundRoles-18, S6 and AC6, against TOOL-dBoundRoles-19 S3.
- **What is wrong:** Unit 18 carries an old reviewer's house text into `house/gov-reviewer.md`. Unit 19 lands first and stops `render_role` reading house files.
- **Consequence:** The text reaches no agent, yet AC6 certifies that it is "not lost".
- **Fix (skeptic judged it sound):** Write the text as a level-5 `[[unit]]` selecting `role.gov-reviewer` through `write_overlay_units`. Change AC6 to assert the unit in the overlay and the text in the rendered `gov-reviewer.md`.
- **Left-shift gate:** As M8.

### M10. A repository role's slot is spelled two ways (id 11)

- **Where:** TOOL-dBoundRoles-20, AC2 and AC6, against TOOL-dBoundRoles-1 section 4 "The item arm".
- **What is wrong:** The index keys the role `triager`, while the actor patch names `role:adopter.triager`.
- **Consequence:** `check_item_roles` resolves the actor to no index role, so AC6's admitted case fails, or the two arms disagree on which role is meant.
- **Fix (skeptic judged it sound):** Fix one slot spelling across the index key, the agent file stem, the actor id and the `role.adopter.<name>` tag (for example the key `adopter.triager`). State it in S3 and use it in AC2 and AC6.
- **Left-shift gate:** A spec-lint check that every identifier spelled in an AC matches the form the spec's S-items define.

### M11. Unit 10's no-spawn default breaks unit 15's stand-in case (id 12)

- **Where:** TOOL-dBoundRoles-10, S4 and Files touched, against TOOL-dBoundRoles-15 AC2 and the New arm.
- **What is wrong:** The default `roles.no-spawn = executor-role-session` refuses every `--stand-in` where the policy kit is installed. Unit 15 adds such a case to `adopt-roles.test.sh`.
- **Consequence:** The `roles adopter self-test` leg reds once unit 10 lands, and the suite lies outside unit 10's write set.
- **Fix (skeptic judged it sound):** Add `tools/roles/adopt-roles.test.sh` to unit 10's Files touched, setting `roles.no-spawn = "recorded-stand-in"` in unit 15's fixture. Alternatively have unit 15's AC2 set that value, and note the dependency in both specs.
- **Left-shift gate:** For every new default, the spec lists the existing test fixtures that exercise the defaulted path.

### M12. The refusal arm is rendered outside the one shared composition (ids 13, 36)

- **Where:** TOOL-dBoundRoles-26, S1 and section 4 "The arm", against TOOL-dBoundRoles-2's `render_role` and TOOL-dBoundRoles-15 S1.
- **What is wrong:** The arm is appended in `render_agent_file` only. Unit 2 makes `render_role`'s `## Return` the composition both routes call. Unit 15 reduces `render_agent_file` to front matter plus `render_static_block`, the block R5 budgets.
- **Consequence:** Handoff `## Role` sections, stand-ins and gov-session never carry the arm. Its bytes escape every role's budget and the `role-sha` hash. AC3 checks only `.claude/agents/`, so it cannot see either gap.
- **Fix (skeptic judged it sound):** Compose the arm inside `render_role`'s `## Return`, after the role's template, from `role-schema.toml`'s `[return.refusal]` table. Change Files touched from `render_agents.py` to `roles_lib.py` (`render_role`). Extend AC3 with a handoff render (`handoff.py render --role gov-session … --stdout`) that carries `outcome: refused` once.
- **Left-shift gate:** A render-parity test asserting that the agent-file route and the handoff route emit the same role block.

### M13. Unit 1 does not update the method-carriers registry (ids 24, 46)

- **Where:** TOOL-dBoundRoles-1, S3 Readers, section 4 Files touched and section 7.
- **What is wrong:** `memory/project/method-carriers.txt` declares `.claude/agents/gov-diff-reviewer.md` and `gov-spec-reviewer.md`. Every rendered agent file names BUILD-METHOD.md. Unit 1 deletes the two and renders four new agent files without touching the registry.
- **Consequence:** The unguarded `method carriers (every pointer declared)` leg reds at unit 1's commit. Check 4 fires on the two gone carriers and check 3 on each of the four undeclared ones.
- **Fix (skeptic judged it sound):** Add the registry to S3's readers and to Files touched: drop the two old rows and add one row per new rendered agent. Name the leg in section 7. Re-derive with `git grep -l -E 'gov-(spec|diff)-reviewer'` and `check-method-carriers.sh` over the rendered tree.
- **Left-shift gate:** A spec-lint check that a spec deleting or creating a rendered agent file lists method-carriers.txt.

### M14. Unit 18's up leaves the adopter's method-carriers registry stale (id 25)

- **Where:** TOOL-dBoundRoles-18, S4 to S6 and section 4 "The program".
- **What is wrong:** adopt-memory-tree.sh seeds the adopter's registry from every file that mentions BUILD-METHOD.md, rendered agents included. The up removes the old reviewer types without re-keying that registry.
- **Consequence:** The adopter's method-carriers leg reds after `govkit update` while the step's witness exits 0.
- **Fix (skeptic judged it sound):** Have the up replace any row naming either old type's path with one de-duplicated `.claude/agents/gov-reviewer.md` row. Include it in the before-image and the down. Add a selftest case `reviewer-merge-carriers`.
- **Left-shift gate:** An upgrade step's witness runs the adopter's own gate legs over the files it touched.

### M15. Unit 25's reader list misses the frozen receipt fixture (id 26)

- **Where:** TOOL-dBoundRoles-25, S8 Readers.
- **What is wrong:** S8 claims to be what `git grep -l -F 'agent-cap.js'` printed at base, but it omits 27 files. One of them is `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`, whose `{prefix}/hooks/agent-cap.*` entries the dead-path leg scans. The disposition table has no frozen-fixture class.
- **Consequence:** Deleting agent-cap makes those references dead paths, and the leg reds. The nearest disposition class would lead the builder to edit a frozen receipt.
- **Fix (skeptic judged it sound):** Regenerate S8 from the stated command with only memory/builds/ excluded. Add a frozen-fixture class: waiver rows in `tools/dead-path-waivers.txt`, and the fixture is never edited. Add that file to Files touched. Make the pass diff its re-derivation against the spec's list and record any difference in the acceptance ledger.
- **Left-shift gate:** A spec-lint check that re-runs any command a spec quotes as the source of a list and diffs the output.

### M16. Half of unit 10's AC6 can never go red (id 27)

- **Where:** TOOL-dBoundRoles-10, AC6.
- **What is wrong:** Grepping `tomllib` in two JavaScript hooks is green at base and can never fail, because JS never spells a Python module.
- **Consequence:** A hook that reads `.governance/policy.toml` directly, the I8 violation the AC names, passes. The S5 seam goes uncertified.
- **Fix (skeptic judged it sound):** Replace the JS half with `git grep -n -E "policy\.toml|\.governance/"` on the two hooks, which must print only the `readPolicy` import and locator lines. Alternatively plant a policy value the catalogue reader rejects and expect the reader's refusal. Observe the criterion red against a hook copy that reads the file with fs.
- **Left-shift gate:** Every AC records a red-first observation against a planted violation.

### M17. The default refuses Grep, but the kickoff Skill still tells the main loop to use it (id 28)

- **Where:** TOOL-dBoundRoles-10, section 4 Migration and section 5 risks.
- **What is wrong:** `state-reads-only` refuses the main loop's Grep and Glob. `skills/session-kickoff/SKILL.md:21` still says "do the mechanical checks yourself (shell/Read/Grep)".
- **Consequence:** Each kickoff runs into refusals that its own instruction provokes.
- **Fix (skeptic judged it sound):** Add SKILL.md line 21 to S7 and Files touched: main-loop search goes through Bash `grep`/`git grep` or a scout. Add an AC: `grep -n 'Read/Grep' skills/session-kickoff/SKILL.md` prints nothing.
- **Left-shift gate:** A spec that refuses a tool greps every shipped instruction carrier for that tool's name.

### M18. The roles kit gets four policy-read paths (id 31)

- **Where:** TOOL-dBoundRoles-15 S6 and section 5 perf, with TOOL-dBoundRoles-10 S5, -11 S5 and -5 S4.
- **What is wrong:** Unit 21 builds `read_policy_setting`, the kit's one reader. Unit 15 reads through a `policy.py get` subprocess, and units 10, 11 and 5 import `resolve` themselves.
- **Consequence:** Missing-kit, refusal and landed-revision handling diverge across readers. The next key will copy whichever path it finds first.
- **Fix (skeptic judged it sound):** Make `read_policy_setting` the only Python reader. Units 15, 10, 11 and 5 cite and call it. In unit 15, None means the default `when-not-static`, and section 5 drops the subprocess. Widen unit 21's AC7 to refuse `policy.py` subprocess calls under `tools/roles/*.py`.
- **Left-shift gate:** Unit 21's widened AC7 is that gate.

### M19. The library would have to import its own importer (id 35)

- **Where:** TOOL-dBoundRoles-2, section 4 "The rendered block", and TOOL-dBoundRoles-3, S3 and section 4 "The allowance".
- **What is wrong:** `render_role` and `derive_allowance` in roles_lib.py read `WRITE_FOLDERS` from check_roles.py, which imports roles_lib. The move into the library comes only in unit 9, at order 13.
- **Consequence:** Built in order, the code either has a circular import or a second copy of the folders, and the copy reds unit 9's AC6.
- **Fix (skeptic judged it sound):** Move `WRITE_FOLDERS` into roles_lib.py in unit 2 and list it among spec 2's readers. Reduce unit 9 S1 to the index render. Re-point spec 2 and spec 3 to `roles_lib.WRITE_FOLDERS`. Probe: after unit 2, `grep -n "^WRITE_FOLDERS = "` prints one line, in roles_lib.py.
- **Left-shift gate:** A build-order check that a seam a spec cites exists at that unit's order.

### M20. Unit 18 adds a second overlay writer (id 37)

- **Where:** TOOL-dBoundRoles-18, S6 and section 4 "Re-keying the other keys" (`write_overlay_values`).
- **What is wrong:** The step edits `.governance/instructions.toml` with its own tomllib value edit. PLAY-dOrderedCharter-32 S8 declares `write_overlay_units` the one writer of that file.
- **Consequence:** The second writer keeps none of S8's invariants (ordering, byte-identity on refusal, one place for the guard to see overlay writes). Unit 19 states the opposite rule.
- **Fix (skeptic judged it sound):** Give `write_overlay_units`, or a sibling in its module, a re-key mode for `select`/`amends`/`supersedes` values. Have `reviewer_merge.py` call it, and file the ask in dOrderedCharter's BACKLOG.md if that unit must add it. Until then, declare the step in section 8 as a sanctioned second door and name the invariant it re-checks.
- **Left-shift gate:** A gate that refuses a write to `.governance/instructions.toml` from any module except the declared writer.

### M21. No extractor declares `role.adopter.<name>` (ids 38, 63)

- **Where:** TOOL-dBoundRoles-20, S1 and section 4 "The composition, and who reads it", against TOOL-dBoundRoles-14 section 3.
- **What is wrong:** Unit 14 hands the adopter role form to unit 20. Unit 20 adds overlay extraction only for `workflow.adopter.<name>`, while adopter roles live only as overlay `[[role]]` rows.
- **Consequence:** Unit 14 S6's cited-but-undeclared join reds every citation of an adopter role tag, AC6 and AC7's `role.adopter.triager` among them. The S9 `role` class and S5's binding join cannot see adopter roles.
- **Fix (skeptic judged it sound):** Extend `extract_role` (or a sibling) to the overlay's `[[role]]` rows, yielding `role.adopter.<name>`, and add `.governance/instructions.toml` to the `role` namespace's `source`. Add a plant `role-rows-adopter` to AC1. Add an AC that an overlay role cited by an actor patch is declared and the join stays green.
- **Left-shift gate:** A join under which every hand-off of a tag form between units names the extractor that declares it.

### M22. Unit 25 omits the gotcha pages the dead-path leg grades (id 43)

- **Where:** TOOL-dBoundRoles-25, S8 Readers, Files touched and section 7.
- **What is wrong:** Deleting agent-cap.js and agent-cap.test.sh makes both basenames needles for the unguarded `dead-path carriers (deleted files still named)` leg. That leg grades memory/gotchas, and six gotcha pages name the files.
- **Consequence:** The bar reds at unit 25's commit, and the builder has no disposition for those pages.
- **Fix (skeptic judged it sound):** Add the six gotcha pages to S8 and Files touched, re-pointed to spawn-guard.js, scratch-guard.js or the moved rule's home, or give each a dead-path waiver row. Name the leg in section 7.
- **Left-shift gate:** A spec deleting a tracked file runs `check-dead-paths.sh` as if the file were already gone and lists the hits.

### M23. Unit 25 leaves a waiver for a suite it removes (id 44)

- **Where:** TOOL-dBoundRoles-25, section 4 Readers disposed, Files touched and section 7.
- **What is wrong:** `memory/project/testsuite-count-waivers.txt:10` waives `tools/hooks/agent-cap.test.sh`, and check-testsuite-counts.sh reds a waiver naming a suite the manifest no longer runs. The new spawn-guard.test.sh has no count disposition.
- **Consequence:** The `testsuite counts (every bar self-test prints one)` leg reds.
- **Fix (skeptic judged it sound):** Add the waiver file to Files touched. Move the row to `tools/roles/spawn-guard.test.sh`, or make the new suite print its count and drop the row. Name the leg in section 7.
- **Left-shift gate:** As M22, extended to every registry under memory/project/ that names a deleted path.

### M24. Live specs cite the files units 1 and 25 delete (id 45)

- **Where:** TOOL-dBoundRoles-25, S8 and AC14, and TOOL-dBoundRoles-1, S3.
- **What is wrong:** The `spec tokens` leg grades backticked paths in live specs' ACs. Unit 25 deletes agent-cap.js and .test.sh, which aDeclaredBound-4, dBoundRoles-10 AC6 and unit 25's own AC14 cite. Unit 1 deletes `tools/roles/house/gov-diff-reviewer.md`, which unit 18's AC6 cites.
- **Consequence:** `spec tokens (a spec's own names resolve)` reds at unit 1's commit and at unit 25's commit. The repair then lands as unplanned edits to another build's spec.
- **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** In unit 25, add `memory/project/spec-token-waivers.txt` rows for `tools/hooks/agent-cap.js` and `tools/hooks/agent-cap.test.sh`, keyed to aDeclaredBound-4 and the dBoundRoles specs that cite them, and add the file to Files touched. In unit 1, add a spec-token-waivers row for `tools/roles/house/gov-diff-reviewer.md` as cited by unit 18's AC6, or reword that AC to describe the old house file in prose rather than as a backticked path or basename. Name `spec tokens` as the leg each change trips. Citing by basename does not work: the bare-basename check still reds once the tracked files are gone.
- **Left-shift gate:** A spec deleting a tracked path runs `check-spec-tokens.py` with that path removed from the tracked set.

### M25. Unit 1 leaves govkit's agent-type count unhandled (id 47)

- **Where:** TOOL-dBoundRoles-1, S2 and S3 and Files touched, and TOOL-dBoundRoles-19 S5.
- **What is wrong and its consequence:** This is the defect in H5 (id 4), seen from the blast-radius lens. Unit 19 re-points only the house-overlay count, so nothing re-points the agent-type count. The govkit selftest red surfaces at unit 19, 18 or 25 and is blamed on a unit that did not cause it.
- **Fix (skeptic judged it sound):** Add `tools/govkit/selftest.py` (OC8 AC4, :2837-2838 and the docstring at :2769) to unit 1's Files touched. Derive both counts from the index's agent-true roles and the kit's seed list. Name `govkit selftest` in unit 1's section 7.
- **Left-shift gate:** As H5.

### M26. Unit 17 seeds a project file the hygiene check refuses (id 48)

- **Where:** TOOL-dBoundRoles-17, S6 and Files touched.
- **What is wrong:** `memory/project/work-order-legacy.txt` is seeded in gov and in every adopter. Hygiene check 3 admits only named F: cases or PROJECT_REGISTRY_EXTRA.
- **Consequence:** The `memory hygiene` leg reds in gov at the seed commit, and adopters receive a file that their own check refuses. Fixing it through PROJECT_REGISTRY_EXTRA would hide the adopter defect.
- **Fix (skeptic judged it sound):** Add `tools/memory-tree/check-memory-hygiene.sh`, its HYGIENE.template.md row and its test to Files touched. Admit `F:work-order-legacy.txt` as a named kit-shipped case beside `F:role-stand-in-waiver.txt`. Add an AC running `check-memory-hygiene.sh --only 3` over a seeded fixture.
- **Left-shift gate:** A spec that seeds a file under `<M>/project/` must list the hygiene check in Files touched.

### M27. Unit 13's SKILL line does not fit the 3 bytes left (id 49)

- **Where:** TOOL-dBoundRoles-13, S7, AC6, Files touched and section 7.
- **What is wrong:** The render `.claude/skills/unattended/SKILL.md` is 10237 bytes against a 10240-byte ceiling. Files touched also omits `memory/guides/UNATTENDED-VERBS.md`, the render of the VERBS template it edits.
- **Consequence:** Any line that satisfies AC6 reds the unguarded size leg, and raising the ceiling is an owner change, so an unattended run stalls. The VERBS guide drifts from its template.
- **Fix (skeptic judged it sound):** Price the addition. Either trim the same template, or carry a ceiling raise as a deviation with its owner route. Name `unattended skill size` and `template size <=48KiB` in section 7. List UNATTENDED-VERBS.md as a render.
- **Left-shift gate:** A spec that adds text to a size-budgeted template states the remaining headroom and the added bytes.

### M28. Unit 22's reader list misses `print_stage_efforts` (id 50)

- **Where:** TOOL-dBoundRoles-22, S2.
- **What is wrong:** `handoff.py:484` requires `stages` to be a dict, and S2 does not list it. Other `get("stages")` hits (handoff.py:463, roles_lib.py:576) are also unlisted.
- **Consequence:** `handoff.py stage-efforts` refuses every workflow, which breaks the build Skill and every harness call.
- **Fix (skeptic judged it sound):** Add print_stage_efforts (handoff.py:474-488) to S2 so it tests the derived rows. List every `get("stages")` hit at the run's base: handoff.py:463 and :484, roles_lib.py:443 and :576, and check_roles.py:297.
- **Left-shift gate:** A shape change's reader list is the output of a stated grep, recorded with the command.

### M29. Unit 21 regenerates the policy mirror in-branch, outside its write set (id 51)

- **Where:** TOOL-dBoundRoles-21, S8 and Files touched.
- **What is wrong:** `policy.py mirror --write` writes `.governance/policy.json`, a path TOOL-dGroundRules-6 guards, in a second in-branch commit. Files touched does not name it.
- **Consequence:** Once dGroundRules-6 lands, the guard refuses the commit. Before that, the step writes outside its declared set and duplicates the landing regeneration.
- **Fix (skeptic judged it sound):** Drop the in-branch mirror step and leave regeneration to the landing (dGroundRules-5 S3). If the mirror must move in-branch, name the file and the guard route that admits it.
- **Left-shift gate:** As M4.

### M30. The anchor check's scan scope includes handed content (id 53)

- **Where:** TOOL-dBoundRoles-24, S3 and section 4 "Why the whole `## Task` section".
- **What is wrong and its consequence:** This is the defect in H2 (id 22), graded medium by the skeptic because the effect is a loud refusal on a narrow set of hand-overs. "Resolves by construction" covers only the fact line, not the content under it. Work orders handing TOOL-dBoundRoles-13 or -24, or the brief, cannot render.
- **Fix (skeptic judged it sound):** Scope the S3 scan to text the work order authors (framing blocks, input values, upstream rows), skipping handed-fact block content by the delimiter TOOL-dBoundRoles-13 adopts (see H2 and H4). Re-run the corpus measurement over specs and briefs. Add an AC rendering a work order that hands TOOL-dBoundRoles-24's own spec as `input:spec`, expecting exit 0.
- **Left-shift gate:** As H2.

### M31. Unit 7 does not say which `### allowance` block wins (id 54)

- **Where:** TOOL-dBoundRoles-7, S4 and section 4 "The allowance as the hook reads it".
- **What is wrong:** The real block sits in the `boundaries` slot, after `### framing:job` and the handed material. A handed spec or the job text can hold an earlier `### allowance`. TOOL-3's and TOOL-7's own specs do.
- **Consequence:** A first-match reader takes the shadow block, which can come from a `writes = none` agent or any handed file. A builder's shell writes are then held to its paths, inside the class bound.
- **Fix (skeptic judged it sound):** Name the block exactly: the `### allowance` heading inside the `boundaries` slot (for example the last one before `### return`). Alternatively require exactly one heading outside handed-content and framing blocks, and deny when there are more. Add a plant `allowance-shadowed`.
- **Left-shift gate:** As H4.

### M32. Prompt-writer fields can forge executor lines (id 55)

- **Where:** TOOL-dBoundRoles-4, S3 ("each holding its field verbatim") and section 5 security.
- **What is wrong:** `job`, `population`, `added` and `nostop` are copied verbatim into the hashed `## Task`, checked only as non-empty text. Nothing refuses `### ` headings, fact lines, marker lines or `Framed by:` lines.
- **Consequence:** A `writes = none` agent can write bytes that the executor and the hooks trust, such as a forged fact line or an earlier `### allowance`. Section 5's "no new write path" is wrong.
- **Fix (skeptic judged it sound):** Before placing a field, refuse it if any line matches `^#{1,3} `, FACT_RE, MARKER_RE or `^Framed by:`, naming the field and the line. State this in section 5. Add an AC refusing a fixture `job` holding a `### allowance` line and a fact line.
- **Left-shift gate:** As H4.

### M33. Unit 18's step claims to be resumable but refuses its own partial state (id 57)

- **Where:** TOOL-dBoundRoles-18, section 4 "The step row" and "The program" (up steps 1 and 5).
- **What is wrong:** No `resume` key means "re-runnable over its own partial state". But the up refuses when a carrier differs from HEAD, and it re-keys carriers in step 3 before the render in step 5.
- **Consequence:** A failure or kill after step 3 wedges the adopter's update with a half-migrated tree. Only a manual down recovers it.
- **Fix (skeptic judged it sound):** Either declare `resume = "atomic"` and restore from the before-image on any failure after step 2, or compare carriers against the before-image's after-state when it exists. Add an AC that stubs `render_agents.py` to exit 1 and checks atomic restoration or a completing second run.
- **Left-shift gate:** A selftest arm, for every upgrade step without `resume = "atomic"`, that kills the up midway and re-runs it.

### M34. Unit 19's step refuses its own partial state (id 58)

- **Where:** TOOL-dBoundRoles-19, S2 and section 4 "The step".
- **What is wrong:** The up refuses when the overlay already holds a unit's tag, yet its missing `resume` promises re-runnability.
- **Consequence:** A kill between a unit write and its file removal leaves a state that the re-run refuses.
- **Fix (skeptic judged it sound):** Skip a file whose unit already exists with a byte-equal body, then remove it. Refuse only on a tag holding different text. Alternatively declare `resume = "atomic"`. Add a kill-and-rerun AC.
- **Left-shift gate:** As M33.

### M35. Large work orders silently lose their allowance (id 59)

- **Where:** TOOL-dBoundRoles-7, section 5 perf ("first 256 KB") and the S4 fallback.
- **What is wrong:** After TOOL-dBoundRoles-13 the first record holds the handed specs verbatim. TOOL-13 assumes specs stay under 49152 bytes, but 90 specs exceed that, the largest at 156459 bytes.
- **Consequence:** A work order over 256 KB falls back to the class verdict with only a witness line, which drops the allowance on the largest work orders.
- **Fix (skeptic judged it sound):** Read the first JSONL line in full, or bound it by a real prompt-size limit. Deny for a typed agent whose first record could not be parsed. Correct TOOL-13's Migration assumption. Add a 300 KB fixture AC.
- **Left-shift gate:** A checklist entry: "a security reader's fallback on unparseable input must deny, not admit".

### M36. Unit 10 does not say how the read arm behaves on a policy refusal (id 60)

- **Where:** TOOL-dBoundRoles-10, S1, S2 and S5, and section 4 "The read arm".
- **What is wrong:** A verdict is given only for a missing policy kit. A `PolicyRefusal` or a throw is unspecified, and the hook already mixes fail-closed and fail-open precedents.
- **Consequence:** A fail-closed copy locks the driver out of every Read, including the reads needed to repair the broken mirror.
- **Fix (skeptic judged it sound):** State that a refusal or a throw in `checkDriverRead` admits, with one witness line. Alternatively refuse Grep and Glob and always admit Read. Add a plant `policy-refusal`.
- **Left-shift gate:** Every new hook arm states its verdict on reader throw and refusal, and a plant exercises it.

### M37. Unit 25's up drops rule 7 on targets without the roles kit (id 61)

- **Where:** TOOL-dBoundRoles-25, section 4 "The step" and section 5 security.
- **What is wrong:** The up unwires agent-cap everywhere but wires the pack only where the roles kit is installed. Rule 7 is armed by the policy kit, not a role index.
- **Consequence:** Adopters with the hooks and policy kits but no roles kit silently lose the agents-in-flight check, and the witness exits 0. Section 5 contradicts itself.
- **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** When the target has the policy kit but no roles kit, the up refuses, naming the roles kit as rule 7's new home and the command that installs it. The witness checks the same condition. Section 5 drops "No rule is weakened" and names the refusal instead. Add a selftest case: a target with the hooks and policy kits but no roles kit, where the up exits non-zero and leaves agent-cap wired.
- **Left-shift gate:** A rule-move spec tables each moved rule's arming condition against the new home's install condition.

### M38. Unit 25's close restores the harness without guarding the restore (id 62)

- **Where:** TOOL-dBoundRoles-25, section 4 Rollout ("This build's own close").
- **What is wrong:** The close overwrites the working-tree harness with `git show <L>:<rel>` and restores it with `git checkout`. It has no interruption handling and no check that the restore happened.
- **Consequence:** A missed restore leaves older bytes over the build's edits, and the write gate cannot see it. A later commit silently reverts them.
- **Fix (skeptic judged it sound):** Run the landed harness from a copy outside the tree (a scratch worktree or a temp path). Otherwise make the restore unconditional with a trap, check `git diff --quiet -- <rel>` afterwards, and record the result in the acceptance ledger.
- **Left-shift gate:** A checklist entry: "no procedure overwrites a tracked file in the working tree to run it".

### M39. Unit 12's placement return is not bound to the scout's transcript (id 64)

- **Where:** TOOL-dBoundRoles-12, S3 and S4.
- **What is wrong:** The driver writes the scout's return to a file for `place --return <file>`. Only validate_return and the answered marker are checked, and the driver can copy the `answers` value.
- **Consequence:** Driver-typed text can become an `agent` placement, which is the judgment this unit exists to exclude.
- **Fix (skeptic judged it sound):** Replace `--return <file>` with `--from-agent <agent-id>`, reading the scout's final return from its transcript and checking agent type `gov-orienter`. Alternatively require the file's bytes to equal that transcript's last assistant text. Add an AC refusing a hand-written return file.
- **Left-shift gate:** A checklist entry: "a record attributed to an agent is read from that agent's transcript, never from a driver-written file".

## Low

### L1. Unit 4 cites `READ_KEYS`, a seam unit 14 has replaced (ids 15, 33)

- **Where:** TOOL-dBoundRoles-4, S1, S2 and section 10, against TOOL-dBoundRoles-14 S4, S7 and F1.
- **What is wrong:** Unit 4 adds `input:work-order` to the `READ_KEYS` literal at roles_lib.py:36-40 and spells the prompt writer's reads in colon form. Unit 14, at order 1, derives `READ_KEYS` from `READ_FAMILIES`, and its F1 puts gov's role files in tag spelling.
- **Consequence:** The citation misleads, and the colon form contradicts F1. Neither reds.
- **Fix (id 15's fix was judged sound; id 33's fix was judged UNSOUND, and this is the skeptic's corrected fix):** Re-point S1 and section 10 to unit 14's seam by adding `"work-order"` to `READ_FAMILIES["input"]`. Spell the reads `field.input.question, field.input.work-order`. State that `--input` admission (`handoff.py` INPUT_NAMES) stays closed to work-order, because `render --for` fills it. Add the criterion that `parse_read_key('field.input.work-order')` returns `('input:work-order', False)` and that the tag index holds `field.input.work-order`. Do not derive INPUT_NAMES from READ_FAMILIES: that would let the driver retype the work order on the CLI.
- **Left-shift gate:** As M19.

### L2. Unit 12 leaves gov-orienter's `outcome` ambiguous (id 14)

- **Where:** TOOL-dBoundRoles-12, S1 and AC4, against TOOL-dBoundRoles-2 S4.
- **What is wrong:** The rewritten `return` names four placement keys and never says whether `outcome` and `card` stay.
- **Consequence:** AC4 and unit 2's R2 disagree on what template is valid.
- **Fix (skeptic judged it sound):** Spell the full template in section 4, including `outcome` with its closed set and `card`, and make AC4's passing return carry `outcome`.
- **Left-shift gate:** As M1.

### L3. Unit 11's Migration claims every spec writes the fork tail (id 16)

- **Where:** TOOL-dBoundRoles-11, section 4 Migration.
- **What is wrong:** Only units 11, 12, 19, 20, 24 and 26 write the `admitted-by:` tail. The other 20 specs do not.
- **Consequence:** The sentence misleads whoever sets `FORK_RECORD_CUTOFF`. Nothing reds, because specs dated before the cutoff are not graded.
- **Fix (skeptic judged it sound):** State the measured fact, and state that the cutoff must fall after 2026-10-25, or that the specs gain tails before the cutoff arms.
- **Left-shift gate:** Back any claim about the spec set with the command that measured it.

### L4. Unit 24 promises a help page sentence that nothing writes (id 17)

- **Where:** TOOL-dBoundRoles-24, section 5 user docs.
- **What is wrong:** Section 5 says `help/roles.md` gains a sentence. No S-item, Files touched entry or AC carries it.
- **Consequence:** The docs promise is unbacked.
- **Fix (skeptic judged it sound):** Add an S-item, Files touched entry and grep criterion, or change section 5 to "none owed" with its reason.
- **Left-shift gate:** A spec-lint join: every path named in section 5 appears in Files touched.

### L5. Unit 23 numbers the effort order by unit 21's steps (id 18)

- **Where:** TOOL-dBoundRoles-23, S5 and the section 4 "The floor" table.
- **What is wrong:** Unit 22 has made the order six steps. Unit 23 still says "steps 4 and 5".
- **Consequence:** The reference points at the wrong step, though the behaviour is recoverable from the table.
- **Fix (skeptic judged it sound):** Re-number to unit 22's order (steps 4, 5 and 6), citing unit 22's section 4.
- **Left-shift gate:** As M8.

### L6. Unit 25 lists an incomplete set of rule-6 changes (id 19)

- **Where:** TOOL-dBoundRoles-25, S2 and the first section 3 non-goal.
- **What is wrong:** The list of rule-6 changes omits TOOL-dBoundRoles-3's card binding and TOOL-dBoundRoles-13's fact re-cut in `checkHandoffSpawn`.
- **Consequence:** A builder reading S2 as the list could fail to carry them. Only AC8's ledger would show it.
- **Fix (skeptic judged it sound):** Add both to S2 and section 3. Optionally add their planted payloads to the New arm.
- **Left-shift gate:** A spec that moves a function lists every earlier unit that edits that function.

### L7. Unit 9's population of `none` roles is stale (id 20)

- **Where:** TOOL-dBoundRoles-9, section 4 Migration.
- **What is wrong:** Unit 9 names "the two reviewers". Unit 1 has merged them and added gov-prompt-writer and gov-tester as `none`.
- **Consequence:** The new `none` roles are never checked against the claim that no `none` role writes a repository file.
- **Fix (skeptic judged it sound):** Re-derive from `.claude/roles.json` at the pass, including gov-session, and state each role's write behaviour.
- **Left-shift gate:** As M8.

### L8. Unit 15's budget invariant ignores unit 2's sections (id 29)

- **Where:** TOOL-dBoundRoles-15, section 4 Pricing and section 5 risks.
- **What is wrong:** "Headroom equals base body headroom" ignores unit 2's `## Never`, `## Ceiling` and `## Return` sections, which spend that headroom.
- **Consequence:** Only the rationale is affected. The table's measurements are correct.
- **Fix (skeptic judged it sound):** Price over the post-unit-2 render, or state that those sections spend base headroom and record the per-role headroom in the acceptance ledger before landing R5.
- **Left-shift gate:** As M8.

### L9. Unit 13's reuse audit cites the wrong line (id 30)

- **Where:** TOOL-dBoundRoles-13, section 10 Reuse audit.
- **What is wrong:** The audit cites `unattended.sh:13004`, which is a comment. The `GIT hash-object` call is at :13029.
- **Consequence:** A builder looking for the precedent is pointed at the wrong line.
- **Fix (skeptic judged it sound):** Cite `tools/unattended/unattended.sh:13027-13029`.
- **Left-shift gate:** Spec-lint that resolves `path:line` citations and checks the cited text.

### L10. `handoff.py` keeps its own copy of two read-key families (id 34)

- **Where:** TOOL-dBoundRoles-14, S4 and section 4 "The read-key vocabulary".
- **What is wrong:** `TASK_FIELDS` and `INPUT_NAMES` stay typed as literals in handoff.py:97-98.
- **Consequence:** The vocabulary keeps two homes, which breaks "joins by one `READ_FAMILIES` entry" in a contained way.
- **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** In S4, set `TASK_FIELDS = lib.READ_FAMILIES["task"]` in handoff.py and name handoff.py as a reader. Derive `INPUT_NAMES` from `READ_FAMILIES["input"]` minus an explicit, named set of render-filled inputs, so a later render-filled member is never admissible on the CLI. Add a criterion that `grep -nE '^TASK_FIELDS = \(' tools/roles/handoff.py` prints nothing.
- **Left-shift gate:** A grep gate refusing literal vocabulary tuples outside roles_lib.py.

### L11. check-return re-implements transcript and id readers (id 39)

- **Where:** TOOL-dBoundRoles-5, S2 and S3.
- **What is wrong:** A fresh JSONL walker and id regex are written although `load_agent_transcript`, `PATH_ID_RE` and `lib.extract_prompt_marker` already exist.
- **Consequence:** Two readers in handoff.py can disagree on what a transcript holds.
- **Fix (skeptic judged it sound):** Extend `load_agent_transcript` to also return the first user record's text and the last assistant text. Read the marker with `extract_prompt_marker` and check ids with `PATH_ID_RE`. Name all three in S2.
- **Left-shift gate:** The reuse audit (section 10) and the S-items must name the same seams.

### L12. Unit 4 cites a closure as its seam (id 40)

- **Where:** TOOL-dBoundRoles-4, S3 and section 10.
- **What is wrong:** `read_transcript` is a closure inside `print_agent_lines`, and it returns no return text and no first record.
- **Consequence:** The seam cannot be called from `render_handoff`.
- **Fix (skeptic judged it sound):** Lift it to a module-level `resolve_agent_transcript(session_dir, agent_id)`, and read the return text through the extension proposed in L11. Cite both.
- **Left-shift gate:** As L9.

### L13. scratch-guard re-types format-guard's session-layout constants (id 41)

- **Where:** TOOL-dBoundRoles-7, S4.
- **What is wrong:** `readWorkOrderAllowance` re-types `RUN_ID_RE`, `WORKFLOW_RUNS_DIR` and the session-dir derivation that format-guard.js already holds.
- **Consequence:** Two copies to change if the subagent transcript layout changes.
- **Fix (skeptic judged it sound):** Lift them into scratch-guard.js's `module.exports`, have format-guard.js import them (it already requires scratch-guard), and name the lift in S4 and section 10.
- **Left-shift gate:** A duplicate-constant gate across the hooks kit.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=64 confirmed=63 refuted=1 unverified=0 blocker=0 high=6 medium=43 low=14 agents=11 out-tokens=316097

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-2.md:section 4 "The return template" (grammar and gov's template table) against section 2 S4 and section 6 AC3 | high | medium | confirmed | Spec 2 :156 has `type := ... \| value ("\|" value)+`, which needs two or more values. :160-161 makes "an unknown type, a set of one value" an R2 defect. The table at :168-177 gives gov-spec-writer `outcome:done`, gov-skeptic `outcome:judged`, gov-synthesizer `outcome:reported`, gov-orienter `outcome:oriented` and gov-session `outcome:sent`. Each is a one-value closed set, or by the grammar an unknown type. AC3 (:270-272) still says "over the tree it exits 0". The spec contradicts itself and the check reds on gov's own roles. A builder would hit this at once, so the effect is contained: medium. | sound | - |
| 2 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md:section 6 AC3 against TOOL-dBoundRoles-16 section 4 "The readers" and section 8 F3 | high | medium | confirmed | Spec 25 AC3 (:352-354) wants the pack to refuse a role whose index `shapes` lacks the harness entry's `kind`. Its non-goal (:124-127) says -16's shape reading moves "as those units leave them", with no change to what any rule refuses. Spec 16 leaves agent-cap's args.roles refusal "unchanged" (:193, F3 :309-315) and keeps the harness list (`extract_workflow_harnesses`) unchanged. Its only index change is per-role `shapes`, so the index records no harness kind. A grep of spec 25 for shapes/kind turns up only the edge (:140) and AC3: no S-item builds the check. AC3 therefore has nothing behind it. | sound | - |
| 3 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md:section 6 AC14 and section 2 S8 Readers | high | medium | confirmed | I re-ran `git grep -l -F 'agent-cap.js' -- ':!memory/builds' ':!memory/ledger' ':!.governance/steps' \| grep ^memory/`. It printed memory/DECISIONS.md, memory/archive/DECISIONS.2026-08-10.md, seven archive template-v-2-* files, memory/backlog/TOOL.md, five memory/gotchas files, four memory/map/generated files and memory/project/spec-token-waivers.txt, along with the guides and features that S8 does list. S8's reader list (:81-100) and the Readers-disposed table (:234-247) leave out the historical and generated files. AC14 (:398-401) allows only kit.toml, the govkit selftest, the step program and the fixtures, so it cannot pass unless frozen history is edited. | sound | - |
| 4 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md:section 4 Files touched and section 7 Gates (against S2/S3) | high | high | confirmed | tools/govkit/selftest.py:2837-2838 hard-codes `len(agents) == 9` and a house overlay count `== 10`. The base tree holds ten role files (gov-session is the one non-agent) and ten house .md files. Unit 1 (order 3) adds four roles with empty overlays and removes two (spec 1 :44-47, :207), which gives about 11 agent types and 12 overlays. Unit 1's Files touched (:204-218) and gate line (:282) do not name govkit/selftest.py or `govkit selftest`. That leg's guard in gate-legs.json covers {prefix}/govkit/, hooks/kit.toml, settings-merge.py and codebase-map/kit.toml, not tools/roles. So a guarded run skips the leg, and the break turns up later on an unrelated govkit change. That misleads the next change. | sound | - |
| 5 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md:section 2 S3 Readers against section 4 Files touched; TOOL-dBoundRoles-18 section 6 AC7 | medium | medium | confirmed | The grep reproduces: tools/workflows/README.md:393,397, tier2-review.test.sh:1865-1941 and unattended-build.test.sh:2776-2777 all spell the old stems. Spec 1 S3 (:51-56) names the three files as readers re-keyed "in this unit", so the claim that nobody writes them is overstated. The S-item gives them to unit 1, and unit 18 S7 agrees. The defect that holds is that unit 1's Files touched (:204-218) leaves them out. TEMPLATE-SPEC :467 says those paths are machine-read to decide which legs are owed. The write set and the §7 leg line therefore miss them, and unit 18's AC7 depends on the edit. | sound | - |
| 6 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-26.md:section 4 "The arm" against TOOL-dBoundRoles-4 section 2 S2 | medium | medium | confirmed | Spec 26 :91-92 refuses "a role whose `return` redeclares `outcome: refused`", and AC3 (:209-211) checks that. Spec 4 S2 (:43), at order 17, before unit 26 at order 22, gives gov-prompt-writer `outcome:framed\|refused, ...`, and its AC path (:173) relies on that `refused` outcome. Unit 26's Files touched (:157-169) leaves out tools/roles/agents/. If the checker matches a `refused` value, the catalogue leg reds on gov's own role. If it does not, the rule is not doing what it says ("the arm cannot drift per role"). | sound | - |
| 7 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md:section 2 S6/S7 against TOOL-dBoundRoles-2 section 4 "The rendered block" | medium | medium | confirmed | Spec 2 (order 2) :202-205 has both render_role callers reading `gates` from load_policy's [gates], and says "the grant TOOL-dBoundRoles-21 re-points to the role field". Spec 21 (order 4) S6 moves gov's two [gates] rows out of the house seed into the role files. It re-points render_roles_index and checkRoleGate, but S7 (:66-70) never names render_agent_file's or render_handoff's gates argument. A grep finds no `render_role` or `Ceiling` anywhere in spec 21. Once the rows move, the rendered `## Ceiling` falls back to none while the index still grants the legs. | sound | - |
| 8 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-15.md:section 4 "Data model" against TOOL-dBoundRoles-2 section 2 S1 and section 4 "The schema" | medium | medium | confirmed | Spec 15 :158-163 writes the budget row as `key`/`type = "integer"`/`meaning`. Spec 2 S1 (:30-33) and the schema table (:97-114) fix the row keys as key/owner/shape/required. The closed shapes are slot, text, list, class, bool, entries and template, with no integer shape, and :118-120 refuses an invalid file. The hedge at spec 15 :165 does not supply a `shape` that does not exist. As written the interface has two spellings, and the row is invalid under unit 2's grammar. | sound | - |
| 9 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-19.md:section 2 S5, S6; section 4 Files touched; section 6 AC1, AC2 | medium | medium | confirmed | Spec 19 (order 24) S5 (:58) says "The ten house/*.md files leave the kit" and the reader "the OC8 count of ten" (:69-71). S6 (:72) says "Gov's ten house files", and Files touched (:204) says "the ten .md files removed". Unit 1 (order 3) seeds four new empty overlays and removes two (spec 1 :46, :207), so the kit holds twelve at the pass. The figures are base figures, not what the predecessors leave. A builder working from them could leave unit 1's overlays in place under a seed rule that no longer lists them. | sound | - |
| 10 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-18.md:section 2 S6 and section 6 AC6 against TOOL-dBoundRoles-19 section 2 S3 | medium | medium | confirmed | Spec 18 S6 (:57-63) appends an old stem's house text to `house/gov-reviewer.md`, and AC6 (:285-291) certifies that text ends up in that file. Spec 19 S3 (:48-53) at order 24, which lands before unit 18 at order 25, stops render_role reading house/<name>.md. At unit 18's pass, text appended to a house file reaches no render, yet AC6 still certifies it "not lost". S6 frames the branch as the case where 19's step is absent, but AC6 requires it unconditionally. The path is narrow, so medium. | sound | - |
| 11 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-20.md:section 6 AC2 and AC6 against TOOL-dBoundRoles-1 section 4 "The item arm" | medium | medium | confirmed | Spec 20 consumes unit 14's `role.<slot>` tag (:116), so `role.adopter.triager` gives the slot `adopter.triager`. Yet AC2 (:269-272) says the index lists `triager`, and AC6 (:287-289) patches the actor to `role:adopter.triager`. Spec 1 :176-185 has check_item_roles read index.roles[<slot>] from `role:<slot>`, and an actor naming no index role is the actor arm's refusal. Spec 20 never states a slot rule for repository roles (its grep for slot/stem finds none), so the two spellings disagree. | sound | - |
| 12 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-10.md:section 2 S4 and section 4 Files touched against TOOL-dBoundRoles-15 section 6 AC2 and section 7 New arm | medium | medium | confirmed | Spec 10 (order 16) S4 (:53-59) and the table at :129-135 make the default `executor-role-session` refuse every `--stand-in` where the policy kit is installed (S5 :64-66). Spec 15 (order 7) AC1/AC2 (:228-240) use a fixture with the policy kit installed and require a `gov-researcher --stand-in` render under a waiver row to succeed. Its New arm (:275) puts that case in tools/roles/adopt-roles.test.sh. Unit 10's Files touched (:158-169) does not list adopt-roles.test.sh, so the roles adopter suite reds once unit 10 lands. | sound | - |
| 13 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-26.md:section 2 S1 against TOOL-dBoundRoles-2 section 4 "The rendered block" and TOOL-dBoundRoles-15 section 2 S1 | medium | medium | confirmed | Spec 26 S1 (:34-38) renders the refusal arm in `render_agent_file` only. Its Files touched names render_agents.py and not render_role, and its AC3 checks only .claude/agents files. Spec 2 :58-62 and :204-205 make render_role the one composition that both the agent file and the handoff route call. Spec 15 S1 (order 7, :30-35) turns render_agent_file into front matter plus render_static_block, the block that R5 budgets. The arm would therefore be missing from handoff `## Role` sections and would sit outside the budgeted block. | sound | - |
| 14 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-12.md:section 2 S1 and section 6 AC4 against TOOL-dBoundRoles-2 section 2 S4 | low | low | confirmed | Unit 12 S1 (lines 31-35) gives gov-orienter's `return` field as the four placement keys "beside the card body the role already returns". AC4 (lines 183-186) says the passing return carries "the card body and all four keys of ... `return` field". Unit 2's table at :173 makes the template `outcome:oriented, card:text`, and S4 (:43-45) requires a closed-set `outcome` on every role. Unit 12 never says whether `outcome` and `card` stay in the template, and AC4 counts the field as four keys. So the template a builder writes and the return AC4 passes are left ambiguous. The gap is wording only. | sound | - |
| 15 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-4.md:section 2 S1 and S2 against TOOL-dBoundRoles-14 section 2 S4/S7 and section 8 F1 | low | low | confirmed | Unit 4 S1 (:34) adds `input:work-order` to "`READ_KEYS` (`tools/roles/roles_lib.py:36-40`)", the literal at base (I read roles_lib.py:36-40). The README build order puts unit 14 at step 1 and unit 4 at step 17. Unit 14 S4 (:44-49) makes READ_KEYS derived from a new `READ_FAMILIES` literal and says a later family "joins by one `READ_FAMILIES` entry". F1 resolves (a): gov's role files carry the tag spelling. Unit 4 S2 still spells reads `input:question, input:work-order`, which stays legal. So the seam cited in unit 4 is stale, and its spelling goes against unit 14 F1. | sound | - |
| 16 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-11.md:section 4 Migration | low | low | confirmed | I ran grep -c per spec. `admitted-by:` is non-zero only in units 11 (9), 12 (3), 19 (3), 20 (5), 24 (3) and 26 (4). The other 20 specs carry 2-6 `RESOLVED (agent` marks each and no tail. So Migration's line 177, "The specs of this build already write the tail", is false. The harm is contained, because the same paragraph sets FORK_RECORD_CUTOFF "at or after the landing date" and grades only specs dated on or after it. Specs dated 2026-10-25 are therefore not graded, and the false sentence misleads without reddening anything. | sound | - |
| 17 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-24.md:section 5 user docs against section 2 and section 4 Files touched | low | low | confirmed | Spec 24 §5 (:169-170) promises that `help/roles.md` gains a sentence under "How a task reaches an agent". `grep -n 'help/'` finds only that line. Files touched (:140-145) lists roles_lib.py, handoff.py, adopt-roles.test.sh and tools/roles/README.md. S5 names only tools/roles/README.md, and no AC greps help/roles.md. The docs promise has nothing behind it. | sound | - |
| 18 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-23.md:section 2 S5 and section 4 "The floor" table against TOOL-dBoundRoles-22 section 4 "The effort" | low | low | confirmed | Spec 23 S5 (:61) applies the floor at "steps 4 and 5 of TOOL-dBoundRoles-21's order", and its table (:142-144) calls the role's declared effort "step 5". Spec 22 §4 "The effort" (:134-139) re-orders the steps: 5 is the stage row's effort and 6 the role's declared effort. Unit 22 is build step 5 and unit 23 is step 18. The table's last row does cover the stage row, so only the numbering is stale. | sound | - |
| 19 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md:section 2 S2 and section 3 first non-goal | low | low | confirmed | Spec 25 S2 (:41-42) and the §3 non-goal (:124-127) list only units -4, -6, -10, -16, -17 and -20 as shaping rule 6. Unit 3 S5 adds the card binding in `checkHandoffSpawn` (spec 3 :52-57), and unit 13 S4 adds the fact re-cut in `checkHandoffSpawn` (spec 13 :47-52). Both land before unit 25. S1's inventory taken at base would catch them, so the incomplete list misleads but does not decide the behaviour. | sound | - |
| 20 | coherence | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-9.md:section 4 Migration | low | low | confirmed | Spec 9 Migration (:155-160) names "the two reviewers" among the `none` roles "(`.claude/roles.json` at base)". Spec 1's roster (:105-119) merges them into gov-reviewer and adds gov-prompt-writer and gov-tester as `none`. gov-session is also `none`. Unit 1 lands at step 3 and unit 9 at step 13, so the account of the roles newly refused is stale when unit 9 runs. The fix's parenthetical list leaves out gov-session, but its main instruction is to re-derive the list from roles.json at the pass, which would catch it. | sound | - |
| 21 | grounding | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-5.md:section 2 S2, section 4 "The direct route", section 4 Rollout | high | high | confirmed | Spec 5 S2 exits early only when `agent_type` is absent or names no agent-true role. The marker is read only to find the work order, never as a condition for checking, and no other spec excludes harness stops (I grepped check-return against harness, workflow and marker across the set). The agent-type probe record (:38-51) shows a typed Workflow child carries `agent_type gov-probe`. The keepalive research (:148-150) shows a sub-agent's end fires SubagentStop under the parent's session. unattended-unit.js:333-337 spawns `agentType: builder` with UNIT_SCHEMA {committed, sha, why, summary} (:207-214), while unit 2 gives gov-builder an `outcome:committed\|returned,...` template. As built, check-return would grade typed harness stages against that template and print block decisions up to roles.retries times on a narrow but recurring path, every typed harness stage. | sound | - |
| 22 | grounding | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-24.md:section 4 "What an anchor is" (the corpus measurement), section 4 "The check", section 4 Migration | high | high | confirmed | I re-ran the git grep: 27 backticked `(blob\|record\|cmd):` spans across 6 tracked specs, including dBoundRoles-13 and -24 themselves (for example S1's `blob:<path>@<blob12>:<lo>-<hi>`), dOrderedCharter-9:51 `cmd:<command>` and aEvidencedLens-3:223. Unit 13 S3 hands spec and prompt inputs as file content inside `## Task`. Unit 24 S3 checks the whole section, and S2 strips only fenced blocks, so these prose spans are graded as malformed and the render refuses. Spec 24 §4 itself admits the brief holds three grammar spans and dismisses it as "not a rendered work order", but after unit 13 the brief is handed as content via input:prompt. The Migration claim of no new refusals is therefore false for these inputs. The fix is unsound. Option (a) stops skipping at the next `### ` heading, but handed specs contain their own `### ` subsections (the spans in spec 24 sit under `### What an anchor is`), so most of the content is still graded. Option (b) still refuses a well-formed example key that is not in the handed set, such as spec 24 AC1's `blob:roles_lib.py@0123456789ab:1-4`. | unsound | - |
| 23 | grounding | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-11.md:section 4 Migration | medium | - | refuted | duplicate of id=16. The same false Migration sentence in spec 11, on the same evidence: admitted-by is non-zero only in units 11, 12, 19, 20, 24 and 26. The extra harm claimed here, FORKED refusals of the build's own units, does not follow. The same Migration paragraph sets FORK_RECORD_CUTOFF "at or after the landing date" and grades only specs dated on or after it, so specs dated 2026-10-25 are not graded. | sound | - |
| 24 | grounding | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md:section 2 S3 Readers, section 4 "Files touched" | medium | medium | confirmed | memory/project/method-carriers.txt:26 and :31 declare `.claude/agents/gov-diff-reviewer.md` and `gov-spec-reviewer.md` as carriers, and gov-spec-reviewer.md mentions BUILD-METHOD. check-method-carriers.sh fails 4 on a declared carrier that is gone and fails 3 on a file that mentions the method without being declared. Spec 1 S3's Readers (:51-59) does not name the registry, and `grep method-carriers` over the spec set prints nothing. Deleting the two reviewer agents and rendering new ones reds the method-carriers leg at landing. The gate catches it, so the effect is contained. | sound | - |
| 25 | grounding | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-18.md:section 2 S4-S6 (the carriers the up re-keys), section 4 "The program" | medium | medium | confirmed | adopt-memory-tree.sh:649-662 seeds method-carriers.txt from git ls-files plus find, writing a row for every file that greps BUILD-METHOD.md, with no exclusion for .claude/agents/. An adopter whose rendered reviewer agents existed at scaffold time therefore declares them. In spec 18, the only hits for 'carrier' are the up's own policy, house and overlay carriers, and `grep method-carriers` over the spec set prints nothing. After the up deletes the old types, that adopter's method-carriers leg reds while the step's witness passes. The damage is conditional on adoption order and contained to that leg. | sound | - |
| 26 | grounding | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md:section 2 S8 Readers ("what git grep -l -F 'agent-cap.js' printed at base 4ed9e567") | medium | medium | confirmed | `git grep -l -F 'agent-cap.js' 4ed9e567`, filtered to drop memory/builds/, prints 72 files. S8's by-name list (:81-104) does not include tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json. That fixture carries `{prefix}/hooks/agent-cap.js` and `agent-cap.test.sh` at :108, :112, :358 and :369, and tools/dead-path-waivers.txt:55-58 already waives the same fixture's dead lexicon path, so the dead-path leg scans it. Neither the receipt nor dead-path-waivers.txt appears in spec 25. The §4 disposition table has no frozen-fixture class, and its nearest class, "a fixture copying the file", would wrongly lead the pass to edit the receipt. S8's claim that the list is what the command printed is false. | sound | - |
| 27 | grounding | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-10.md:section 6 AC6 | medium | medium | confirmed | spec-10.md:222-225 AC6 greps `tomllib` in tools/hooks/scratch-guard.js and agent-cap.js. On re-probe, `git grep -n tomllib` on those two files gave rc=1 at HEAD, so this half is already green. A JS hook can never spell a Python module, so the half cannot go red on the fs-read violation of S5/I8 that it names. Only the handoff.py half can fail. | sound | - |
| 28 | grounding | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-10.md:section 4 Migration and section 5 risks (who loses Grep and Glob under the default) | medium | medium | confirmed | skills/session-kickoff/SKILL.md:21 reads 'Posture: do the mechanical checks yourself (shell/Read/Grep)'. spec-10 S1 and the §4 table make `state-reads-only` the default, and under it the main loop's Grep and Glob are refused. The only carriers spec-10 updates are help/roles.md (S7) and the two READMEs (§5). Its pricing (:125-126, :187-188) weighs only BUILD-METHOD M7, and no line of spec-10 names the kickoff Skill. So the kickoff runs in the main loop and tells it to use a tool the default refuses. | sound | - |
| 29 | grounding | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-15.md:section 4 Pricing, section 5 risks | low | low | confirmed | spec-15.md:129-131 prices budget as the BODY_CEILINGS row plus the charter block, and claims 'the headroom left over the rendered role is exactly the base body's headroom today'. spec-2.md:183-205 has render_role append ## Never, ## Ceiling and ## Return. Unit 2 is build step 2 and unit 15 is step 7. Those sections fall inside render_static_block's whole block but in neither term of the budget, so they spend base-body headroom. The table itself, re-derived at the pass, is not wrong. Only the stated invariant and its 'no role reds' reasoning are false, so the effect is contained to the rationale. | sound | - |
| 30 | grounding | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md:section 10 Reuse audit | low | low | confirmed | `sed -n 13004p tools/unattended/unattended.sh` at HEAD, and at 4ed9e567 (spec-13's base), prints a roster/shape comment ('they refuse is also off the roster...'). The `h=$(GIT hash-object "$path" ...)` call is at :13029, after the clean-filter comment at :13027-13028. spec-13.md:259-260 cites :13004 and calls scout B's correct :13029 the aside. | sound | - |
| 31 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-15.md:section 2 S6, section 5 perf/scale (with TOOL-dBoundRoles-10 S5, -11 S5, -5 S4) | medium | medium | confirmed | spec-15.md:62-64 reads instructions.task-charter through a `policy.py get` subprocess, with its own resolve_kit_dir and LookupError note (:122-125), and :213 prices one subprocess per render. spec-21.md:35-42 builds `read_policy_setting` as the roles kit's one policy read, at step 4 before 15. spec-21.md:196-198 rejects the per-key `policy.py get` subprocess. spec-5 S4 (:58) and spec-10 S5 (:64) import `resolve` directly through resolve_kit_dir, and spec-11:146 reads 'read once through resolve()'. Grep shows read_policy_setting cited only in spec-21 and spec-23. Several readers follow divergent paths. spec-5:78 S7 (`policy.py get` in SKILL/VERBS text) is a driver CLI instruction, not a Python read, and the fix's AC widening to tools/roles/*.py correctly leaves it alone. | sound | - |
| 32 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-15.md:section 2 S2; section 4 Data model | medium | medium | confirmed | spec-15.md:37-40 adds `budget` 'once to FRONT_MATTER_KEYS'. Its data model (:160-166) gives the row `type = "integer"` and `meaning`. spec-2.md:28-33 derives FRONT_MATTER_KEYS from role-schema.toml rows that carry key/owner/shape/required. Its shape table (:106-114) has no integer shape. load_role_schema refuses an invalid file with an R2 RolesError, and AC6 (:285-289) reds a key typed beside the schema. spec-15:166 defers 'other keys' to spec 2's grammar, but it still prescribes the hand-typed tuple edit and keys that grammar does not have. | sound | - |
| 33 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-4.md:section 2 S1; section 10 | medium | low | confirmed | spec-4.md:35 and §10 :253-254 name READ_KEYS at roles_lib.py:36-40 as the seam. spec-14 S4 (:44-50, :153-157, :165-166) makes READ_KEYS a frozenset derived from READ_FAMILIES, and says a later key 'joins by one READ_FAMILIES entry'. Unit 14 is step 1 and unit 4 is step 17, so spec 4 cites a stale seam. The finding's INPUT_NAMES part does not hold. On re-probe, handoff.py:965-972 shows INPUT_NAMES gates only CLI `--input` names, and spec-4 S1 fills input:work-order through `render --for`, not `--input`, so that gate never refuses it. Because READ_KEYS is visibly derived after unit 14, a builder is unlikely to splice into it, so the consequence is mainly a misleading citation. The fix is unsound: deriving INPUT_NAMES from READ_FAMILIES['input'] would admit `--input work-order=<text>` on the CLI. The driver could then retype the work order, which spec-4's 'never retyped by the driver' framing forbids. | unsound | - |
| 34 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md:section 2 S4; section 4 "The read-key vocabulary" | low | low | confirmed | `sed -n 97,98p tools/roles/handoff.py` shows TASK_FIELDS and INPUT_NAMES typed as literal tuples. Their readers are handoff.py:354-358 (the label zip) and :970 (the --input gate). spec-14 S4 (:44-50) claims one vocabulary home in roles_lib's READ_FAMILIES, and neither re-points nor names these two. The duplication is real, mainly for TASK_FIELDS. The fix is unsound: binding INPUT_NAMES to READ_FAMILIES['input'] would, once unit 4 adds work-order, admit `--input work-order` on the CLI. The work order is meant to be filled by `render --for` and never handed by the driver. Not every input-family read key is a driver-supplied CLI input. | unsound | - |
| 35 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-2.md:section 4 "The rendered block" (and TOOL-dBoundRoles-3 S3/§4 "The allowance") | medium | medium | confirmed | `grep -n '^WRITE_FOLDERS = '` finds it only at check_roles.py:99, and check_roles.py:82 imports roles_lib as lib. render_role lives in roles_lib.py:579. spec-2:202-205 has render_role's ## Ceiling take the class folder from WRITE_FOLDERS at check_roles.py:99-101. spec-3:44-46 and :100-107 put derive_allowance in roles_lib, reading WRITE_FOLDERS and 'never typed here'. Only spec-9 S1 (:31-33), at step 13, moves WRITE_FOLDERS into roles_lib, after units 2 (step 2) and 3 (step 11). Built in order, the library must either import its own importer or keep a second copy, and the copy would red spec-9 AC6. A builder would likely notice, so the effect is contained. | sound | - |
| 36 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-26.md:section 2 S1; section 4 "The arm" | medium | medium | confirmed | spec-26.md:34-38 renders the refusal arm in render_agent_file 'after the role's own template'. Its Files touched (:162) is render_agents.py, and AC3 (:209-212) counts only .claude/agents/. spec-2:183-205 makes render_role's ## Return the one composition both routes call. spec-15 S1 (:31-36), at step 7, before 26 at step 22, reduces render_agent_file to front matter plus render_static_block, and R5 measures render_static_block. Built as written, the arm is missing from handoff ## Role sections (stand-in and gov-session) and sits outside the budgeted block, and AC3 cannot see either gap. | sound | - |
| 37 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-18.md:section 2 S6; section 4 "Re-keying the other keys"; section 4 Inventory (`write_overlay_values`) | medium | medium | confirmed | spec-18.md:57-61 S6 and :178-180 edit .governance/instructions.toml with the step's own tomllib value edit, and the inventory (:196) mints write_overlay_values in reviewer_merge.py. PLAY-dOrderedCharter-32.md:94-98 S8 declares write_overlay_units the one function that writes .governance/instructions.toml, with the doors, including the upgrade-step kind, as its only callers. spec-19:189-190 states that the overlay is written only through that one writer. Unit 18 adds a second writer beside the declared one, and nothing in the spec acknowledges it. | sound | - |
| 38 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-20.md:section 2 S1; section 4 "The composition, and who reads it" | medium | medium | confirmed | spec-20 S1 (:36-41) adds an overlay arm only to extract_workflow (workflow.adopter.<name>). spec-20:165-167 makes an adopter role a row in .governance/instructions.toml, 'never a file under the kit's agents/'. spec-14's role namespace has source = tools/roles/agents/*.agent.md (:103). spec-14:72-74 hands role.adopter.<name> to unit 20 on the premise that 'an adopter role file joins as data'. That premise is false under unit 20's overlay-row design. Grep finds extract_role only in spec-14, so no extractor yields role.adopter.<name>. | sound | - |
| 39 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-5.md:section 2 S2 and S3 | low | low | confirmed | spec-5 S2 (:45-49) and S3 (:54-56) describe a fresh transcript read and an id regex `[A-Za-z0-9_-]{1,64}`. handoff.py:121 already has PATH_ID_RE with that same regex, :616 has load_agent_transcript (a JSONL walker), and roles_lib.py:246 has extract_prompt_marker. S2 names none of them, while §10 (:288-289) cites load_agent_transcript as the seam extended. The duplication is contained to handoff.py. | sound | - |
| 40 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-4.md:section 2 S3; section 10 | low | low | confirmed | handoff.py:825-828 is `def read_transcript(folder, aid):`, a closure inside `print_agent_lines` (def at :798). It returns `load_agent_transcript(...)`, whose dict (handoff.py:623-624) holds type/description/effort/model/wall/tokens/files, with no return text and no first record. spec-4 S3 (:47-49) and §10 (:253) cite it as the seam `--framed-by` extends. render_handoff cannot call it as written. The effect is only on which seam the builder reuses. | sound | - |
| 41 | reuse | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-7.md:section 2 S4 | low | low | confirmed | format-guard.js:101 `RUN_ID_RE = /^[A-Za-z0-9_-]{1,64}$/`, :103 `WORKFLOW_RUNS_DIR = 'workflows'`, :335 builds the subagents/workflows/<run>/ path, and :91 requires scratch-guard.js. spec-7 S4 (:53-57) restates the same shape and layout for scratch-guard. Its §10 (:307-309) says only that it 'follows' format-guard's rule. It names no lift, so the kit ends up with two copies. scratch-guard's module.exports (:1615) does not hold these names today, so lifting them into scratch-guard keeps the import direction acyclic. | sound | - |
| 42 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md:section 6 AC14 (and section 2 S8 Readers) | high | high | confirmed | I re-ran AC14's git grep and it printed 72 files. These include memory/DECISIONS.md, memory/archive/DECISIONS.2026-08-10.md, archive template v-2-1..7, memory/backlog/TOOL.md, five gotcha pages, memory/map/generated/{CARDS.md,MAP.md,inventories.json,symbols.json} and memory/project/spec-token-waivers.txt (row 29 names .claude/hooks/agent-cap.js). spec-25 S8's reader list (:81-104) names none of them, and AC14 (:398-402) admits only kit.toml, the govkit selftest, the step program and govkit fixtures. The criterion cannot go green without editing append-only records, and that steers the builder toward falsifying them. | sound | - |
| 43 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md:section 2 S8 Readers, section 4 Files touched, section 7 | medium | medium | confirmed | check-dead-paths.sh:192-197 greps the whole tree minus memory/, plus 'memory/map/features/*' 'memory/gotchas/*'. Its needles are basenames git once tracked and no longer does. `--needles` today prints no agent-cap entry, because the file is still tracked. Once unit 25 deletes it, it becomes a needle. `git grep -l 'agent-cap\.test\.sh' memory/gotchas` adds inline-marker-breaks-a-line-continuation.md to the agent-cap.js pages. In gate-legs.json the 'dead-path carriers (deleted files still named)' leg has guard None. spec-25 names no gotcha page apart from an unrelated one at :263, and it does not list the leg. | sound | - |
| 44 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md:section 4 Readers disposed / Files touched, section 7 | medium | medium | confirmed | memory/project/testsuite-count-waivers.txt:10 is `tools/hooks/agent-cap.test.sh`. check-testsuite-counts.sh:136-145 fails on a waiver naming a suite the manifest does not run. spec-25 S5 replaces the suite with tools/roles/spawn-guard.test.sh under a new leg. It never mentions the waiver file or the 'testsuite counts' leg (guard None), and `grep -i 'assertion\\|FLOOR' spec-25` finds no count disposition for the new suite. | sound | - |
| 45 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md:section 2 S8, section 6 AC14; also TOOL-dBoundRoles-1 section 2 S3 | medium | medium | confirmed | check-spec-tokens.py:1515-1526 grades every path-shaped word in an AC bullet against git ls-files, and LIVE (:299) covers OPEN\|SPECCED\|INPROGRESS\|BLOCKED. The citations are real: aDeclaredBound-4 (Status OPEN) cites tools/hooks/agent-cap.test.sh and agent-cap.js in its ACs (:281-307), dBoundRoles-10 AC6 cites tools/hooks/agent-cap.js, unit 25 AC14 cites both, and unit 18 AC6 (OPEN, order 25) cites `tools/roles/house/gov-diff-reviewer.md`, which unit 1 (order 3) deletes (spec-1:55-56,138). spec-token-waivers.txt holds only the .claude/hooks row (:29). Neither spec disposes of these citations. The fix is unsound for unit 18: at a root install, check_bare_shaped (:1142-1150) grades a bare basename against the tracked basenames. Unit 1 deletes both tracked gov-diff-reviewer.md files (.claude/agents and house), so a backticked `gov-diff-reviewer.md` would still red. The basename route offered for the agent-cap citations fails the same way, because agent-cap.js leaves the tree. Only the waiver-row route works. | unsound | - |
| 46 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md:section 4 Files touched, section 7 | medium | medium | confirmed | method-carriers.txt declares .claude/agents/gov-diff-reviewer.md and gov-spec-reviewer.md. `grep -c BUILD-METHOD .claude/agents/*.md` printed 1 for all nine agents. check-method-carriers.sh:114 fails 3 on an undeclared mentioning file and :122 fails 4 on a declared file that is gone. spec-1 S8 re-renders .claude/agents/ and AC (:269) requires the two reviewer files to be gone. `grep -l method-carriers` over the spec set printed nothing. The leg's guard is None. | sound | - |
| 47 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md:section 2 S2/S3, section 4 Files touched; also TOOL-dBoundRoles-19 section 2 S5 | medium | medium | confirmed | govkit/selftest.py:2837 checks `len(agents) == 9` and :2838 checks `== 10` house overlays. Unit 1 changes the roster (two reviewers out, four roles in) and the house seed list (spec-1:138,207), and its files never name selftest.py. Unit 19 S5 (:65-67) re-points only 'the OC8 count of ten'. Units 18, 20 and 25 touch selftest.py for other cases, and none of them re-points the agent-type count. The govkit selftest guard does not cover tools/roles/, so the red surfaces at a later unit. | sound | - |
| 48 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md:section 2 S6, section 4 Files touched | high | medium | confirmed | check-memory-hygiene.sh:718-765 admits only the named F: cases (including role-stand-in-waiver.txt and substitution-fed-loops.txt) or PROJECT_REGISTRY_EXTRA. The comment at :732-738 records the kit-shipped-registry block. .memory-tree.conf:917 PROJECT_REGISTRY_EXTRA does not hold work-order-legacy.txt. spec-17 seeds memory/project/work-order-legacy.txt (:59,:169) and never touches the hygiene check. The 'memory hygiene' leg (guard None) reds at the seed commit, and adopters receive a file their own check refuses. The bar catches this in gov, so the effect is contained, but the easy fix of PROJECT_REGISTRY_EXTRA would hide the adopter defect. | sound | - |
| 49 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md:section 2 S7, section 6 AC6, section 4 Files touched, section 7 | medium | medium | confirmed | `wc -c .claude/skills/unattended/SKILL.md` printed 10237. template-size-limits.txt:151 sets the ceiling at 10240, leaving 3 bytes. spec-13 S7 and AC6 (:213-215) require a `handoff.py facts` line in tools/unattended/SKILL.template.md. §7 (:220) does not list 'unattended skill size' (guard None). Files touched (:164-165) lists VERBS.template.md, which unattended kit.toml:79 includes and renders to memory/guides/UNATTENDED-VERBS.md (that file exists), but does not list the render. | sound | - |
| 50 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-22.md:section 2 S2 | medium | medium | confirmed | handoff.py:484 in print_stage_efforts reads `if not isinstance(entry.get("stages"), dict): raise RolesError(... has no stages table ...)`. spec-22 S2 (:33-39) lists handoff.py:453, check_roles.py:297-310, roles_lib.py:430-451 and check_roles.py:121-141 as the readers to re-point, but not :484. Once stages become an array of tables, stage-efforts refuses for every workflow. `git grep '.get("stages"'` also shows handoff.py:463 and roles_lib.py:576. AC3 would show the break red, but the reader population the spec gives is incomplete. | sound | - |
| 51 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md:section 2 S8, section 4 Files touched | medium | medium | confirmed | spec-21 S8 (:72-76) runs `policy.py mirror --write` in a second in-branch commit. dGroundRules-5 S2 says --write writes .governance/policy.json, which embeds the catalogue blob id, and its S3 regenerates the mirror at landing. dGroundRules-6 (:21-26) refuses an agent commit touching the JSON mirror outside the one budgets.* shape. spec-21 never names .governance/policy.json. All dGroundRules specs are DEFERRED and tools/policy is not tracked at HEAD, so the guard refusal depends on dGroundRules-6 landing first. Even so, the step writes a file outside the declared write set and duplicates the landing regeneration. | sound | - |
| 52 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md:section 2 S3 and S4; section 4 "The fact line" and "The re-cut" | high | high | confirmed | spec-13 S3 (:41-46) renders a fact line and 'then the content' with no fence or escape, and S4 (:47-52) reads 'every fact line of the task section' through FACT_RE (:104). spec-13:99 itself is a FACT_RE-matching line keyed to memory/builds/tFix/..., and `ls memory/builds/tFix` fails, so handing spec-13 to its builder makes the re-derive refuse. A quoted line also carries an author-typed class. Three tracked specs (aOrientedCast-2, -7, PLAY-dOrderedCharter-5) hold `^<!-- gov:handoff role=` lines, which would break spec-4's exactly-one-marker rule (:59,:123) once handed as content. spec-13 has no fence, escape or sentinel rule. The fix is unsound as offered: its second option (match FACT_RE only on the line right after a `### ` heading, plus a sentinel) does not cure the defect. Untrusted content can hold a `### ` heading followed by a fact line, and spec-13:96-99 is already that shape. Only the fence option, with fence-aware readers, closes it. | unsound | - |
| 53 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-24.md:section 2 S3; section 4 "Why the whole `## Task` section" | high | medium | confirmed | The claim holds. TOOL-13 S3 and the §4 example put the handed spec's bytes into ## Task with no fence, straight after the fact line. TOOL-24 S2/S3 strips only fenced blocks and then scans the whole ## Task section. I re-ran the scan over dBoundRoles/spec with fences stripped. It found 19 unfenced backticked prefix spans in TOOL-13 (first one `blob:<path>@<blob12>:<lo>-<hi>`) and 11 in TOOL-24 (`blob:`, `record:`, `cmd:`). All of them are malformed under S1, so a work order that hands either spec as input:spec cannot render. The §4 'resolves by construction' sentence covers only the fact line. The corpus measurement in §4 was taken over prompts/ only. I grade it medium, not high: the effect is a loud refusal on a narrow set of hand-overs, never a wrong result. | sound | - |
| 54 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-7.md:section 2 S4; section 4 "The allowance as the hook reads it" | high | medium | confirmed | TOOL-7 S4 says only 'the `allowance` block of that prompt's `## Task` section' and never says which block wins when there are several. TOOL-23's slot table puts `material` (the handed reads content, unfenced per TOOL-13) and `### framing:job` ahead of `boundaries`. TOOL-7's own §4 shows a literal `### allowance` block, and a reader of the transcript that does not strip fences sees it as a block. So a first-match reader can take a shadow allowance. The class verdict still bounds this ('Only an allowance narrows'), which limits the consequence to medium. | sound | - |
| 55 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-4.md:section 2 S3 ("each holding its field verbatim"); section 5 security | high | medium | confirmed | TOOL-4 S3 places each framing field 'verbatim' inside the bytes the task-sha covers. TOOL-5's value table accepts `text` as any non-empty string. No clause refuses `### `, FACT_RE, marker or `Framed by:` lines in a field. The prompt writer is also handed the destination's allowance as content under input:work-order, so echoing a `### allowance` into `job` (slot 1, ahead of boundaries) is plausible. §5 security says only 'no new write path'. The consequence is contained by the class verdict and by TOOL-13's re-derivation of keys, so medium. | sound | - |
| 56 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-5.md:section 2 S2 and S3; section 4 "The direct route" | high | high | confirmed | TOOL-5 S2 filters only on a missing agent_type or a non-agent-true role. S5 wires it on SubagentStop with matcher `*`. I re-ran the grep: harness stages pass gov-* agent types (unattended-build.js:542, tier2-review.js:271). TOOL-7 §4 records that harness transcripts live under subagents/workflows/. SubagentStart demonstrably fires for workflow agents in this very session. No clause exempts a harness agent, which returns through StructuredOutput, not a fenced json block. So every harness agent can be blocked up to roles.retries times and recorded valid:false, and TOOL-26 routes on that record. | sound | - |
| 57 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-18.md:section 4 "The step row" and "The program" (up step 1 and step 5) | high | medium | confirmed | The TOOL-18 step row (§4) has no `resume` key. dSafePassage-1's data model (line 194) says an absent `resume` means 'the up is re-runnable over its own partial state'. Up step 1 exits 1 on 'a carrier differing from its blob at HEAD', and step 3 re-keys the carriers before step 5's render. After a failure past step 3, the old stems are gone from the carriers, so the early no-op exit can miss (types under .claude/agents remain), and step 1 then refuses. Nothing covers failure after step 3. The before-image still allows a manual down, so the harm is contained: medium. | sound | - |
| 58 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-19.md:section 2 S2; section 4 "The step" | medium | medium | confirmed | TOOL-19 S2 writes a unit for each file and then removes the file. §4 says 'A unit whose tag the overlay already holds refuses the up'. The step row declares no `resume`, which under dSafePassage-1:194 promises re-runnability over partial state. A kill between the unit write and the file removal leaves a state that the re-run refuses. Contained, since the down remains. | sound | - |
| 59 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-7.md:section 5 perf / scale ("bounded to its first 256 KB"); section 2 S4 fallback | medium | medium | confirmed | TOOL-7 §5 bounds the first-record read to 256 KB, and S4 falls back to the class verdict when that record cannot be read. TOOL-13 §4 Migration assumes 'a unit's spec is under 49152 bytes by the spec cap'. I re-ran the count: 90 specs exceed 49152. The largest is dGatedProse-1 at 156459 bytes, and a recent one, dRedressedBar-19, is 96214. check-template-size's 49152 default does not gate specs. Briefs reach about 36 KB. A large spec plus its brief plus JSON escaping can approach or pass 256 KB. The 'normal path' framing is overstated, since this build's specs are all under 42 KB, but the silent drop on large work orders and the false cap assumption are real. | sound | - |
| 60 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-10.md:section 2 S1, S2 and S5; section 4 "The read arm" | medium | medium | confirmed | TOOL-10's S5, the §4 read-arm diagram and §5's error states give a verdict only for an absent policy kit. dGroundRules-5 §4:193-215 states that readPolicy throws a PolicyRefusal (stale or absent mirror, exit 2). TOOL-10 has no branch for a refusal or a throw. In scratch-guard.js, the write gate fails closed (:1549) and the Bash checks fail open (:1569), so the builder has two contradictory precedents to copy. | sound | - |
| 61 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md:section 4 "The step" (up: "A target without the roles kit loses the guard, which matches what it had"); section 5 security | medium | medium | confirmed | dGroundRules-10 S5 arms rule 7 by the policy kit for every Agent/Workflow call, not by a role index. TOOL-25 F1 moves rule 7 into the roles pack. The up's rationale 'rule 6 is armed only by a role index' therefore does not cover rule 7. §5 security says 'No rule is weakened in the move', while §5 risks admits 'An adopter whose roles kit is absent loses rule 7 with rule 6'. The spec contradicts itself, and those adopters do lose rule 7 on update. | unsound | - |
| 62 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md:section 4 Rollout, "This build's own close" | medium | medium | confirmed | TOOL-25 §4 Rollout ('This build's own close') overwrites the working-tree harness with `git show <L>:<rel>` and restores it with `git checkout -- <rel>` after the call. No clause handles interruption, a failed Workflow call or a background run, and nothing verifies the restore. TOOL-7 §4 lists `git checkout` among the writes the gate does not see. A missed restore leaves the older landed bytes over the build's committed edits, where a later commit can pick them up. | sound | - |
| 63 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-20.md:section 2 S1 (namespace extraction); edge with TOOL-dBoundRoles-14 section 3 | medium | medium | confirmed | TOOL-14's non-goals defer `role.adopter.<name>` to TOOL-20, and its namespace row's source is only tools/roles/agents/*.agent.md. TOOL-20 S1 adds overlay extraction only for `workflow.adopter.<name>`. My grep found `role.adopter` only in TOOL-14:72, the TOOL-20:133 comment and TOOL-20's ACs, with no S-clause. Adopter roles live as overlay [[role]] rows, so no extractor declares their tag, and TOOL-14 S6 reds every citation of one. | sound | - |
| 64 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-12.md:section 2 S3 and S4 | medium | medium | confirmed | TOOL-12 S3 promises 'no driver-typed text becomes an `agent` placement'. Yet S4 has the driver write the return to the request's file and pass `--return <file>`, and S2/S3 check only validate_return and the marker on the answered work order. The driver can copy that work order's `answers` value. Nothing binds the file's bytes to the scout's transcript, unlike TOOL-4's `--framed-by`, which reads the transcript. | sound | - |
