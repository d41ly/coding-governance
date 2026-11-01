**Serves:** spec-audit KICK-dKeptSession-1@rev-1 KICK-dKeptSession-19@rev-1 KICK-dKeptSession-2@rev-1 KICK-dKeptSession-3@rev-1 KICK-dKeptSession-4@rev-1 KICK-dKeptSession-20@rev-1 KICK-dKeptSession-16@rev-1 KICK-dKeptSession-12@rev-1 KICK-dKeptSession-13@rev-1 KICK-dKeptSession-26@rev-1 KICK-dKeptSession-15@rev-1 KICK-dKeptSession-14@rev-1 KICK-dKeptSession-9@rev-1 KICK-dKeptSession-28@rev-1 KICK-dKeptSession-22@rev-1 KICK-dKeptSession-5@rev-1 KICK-dKeptSession-23@rev-1 KICK-dKeptSession-27@rev-1 KICK-dKeptSession-24@rev-1 KICK-dKeptSession-10@rev-1 KICK-dKeptSession-25@rev-1 KICK-dKeptSession-21@rev-1 KICK-dKeptSession-6@rev-1 KICK-dKeptSession-7@rev-1 KICK-dKeptSession-8@rev-1 KICK-dKeptSession-11@rev-1 KICK-dKeptSession-17@rev-1 KICK-dKeptSession-18@rev-1

# Tier-2 spec audit — dKeptSession, the 28-unit spec set, ROUND 1

*This is an adversarial pre-code pass over the dKeptSession spec set at spec commit 5c2390bb3, dated 2026-10-26. Five lenses found the findings, and a skeptic tried to refute each one. The findings ran: coherence, grounding, reuse, blast-radius, failure-envelope. Only the confirmed findings appear below. Each item gives its address, its consequence, the fix, and a left-shift gate.*

Reviewed: memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md@5aba0607c14ad054104ce1496de7cd8f0406259f, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-19.md@a47eff0ff5e0f3f4c009ae50bc23d0c39705ceab, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-2.md@52f86d28f506aa97c1e2fb7b647834561b6cfef2, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-3.md@edd817eba911ebbd555427072dcf568f8b8c8af7, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-4.md@16194b7d596c3157f8c2afd3794807135632b192, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-20.md@a8aec563ed3e92ede50e0d313b0b527f0c46c951, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-16.md@dfce5b72a836e5e58eae5b2a1fb6877b8ade0b9f, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-12.md@65a835b4f25ac0ef7bdbf6d2368386abc27fea20, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-13.md@0c9a4ddc03adb38513b0deffd334b9a58889b301, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-26.md@2548e583f74698ed6ea2b7ff6b2b830c9593dcd0, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-15.md@d3e3ede987c389960570a17ea832991165bd6c98, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-14.md@aefff8d651d399e9e62d2eaa230aa3567c8ba759, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-9.md@1b5021bfc0e392465f66640e6ffca38e5e24a2b1, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-28.md@e578b59cc0be61c1b04294752ad6b9933bd2084b, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-22.md@f11aeda193577219c4d3f73ab412f11437057f35, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-5.md@b2e7bef673e55fc28c0c2530715934eb521be926, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-23.md@1e2c1929d5d74082944265da2941d43c2f2acd44, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-27.md@15085c9bf04be09d578a053af2b425e6ba419a34, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-24.md@fd6a79092a5c5065fd7e3fd18511bbf480f2d22f, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-10.md@93cff4ac84950bfbd4f62605c2ee14a2a14c35cc, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-25.md@e7cc42442b47abfdb31e072cf298fd5a5aa730e0, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-21.md@903acc82599a7d5d4fd225408b36f8965f02d7c2, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-6.md@4e9ff548b2d08dca46ea2887e65dc2eec3ee7973, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-7.md@c7a8b56b42497442c5d5a8d9fbdba0523bef981f, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-8.md@fe9139b1497ae14cbf679736ec1f0a0095b6fbd2, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-11.md@761a680b65d29eae7ea5adb6e8bd46e574b0c6b5, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-17.md@dab7d0cd34d68402f1c406faa08a1367962aa447, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-18.md@07679e38d5a19932e57c63d762f5568397f3d636

ROUND 1

## Verdict: BLOCKED

Two blockers stand: an item boundary that pins a 200k context window on a node that runs about 1M, and a mailbox message id that collides on every notice after the first. Twelve high findings stand beside them. The spec set must not go to Build until every blocker and high item below is fixed and re-audited.

By item the tally is 2 blocker, 10 high, 30 medium and 8 low, which makes 50 items. By raw confirmed finding it is 2 blocker, 12 high, 33 medium and 9 low, which makes 56. Items merge only findings that describe one defect at one binding grade.

Two defects were found at two different grades, and each grade keeps its own item. The message-id collision is B2 (id 54, blocker) and H3 (id 4, high). The pre-existing catalogue rows are H8 (id 45, high) and M4 (ids 7 and 34, medium). Fixing one item of each pair fixes the other.

## Review shape

The review ran at intensity full: raw 63, confirmed 56, refuted 7, unverified 0 (0 uncertain), precision 0.89.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 15 | 15 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 16 | 11 | 5 | 0 | 0 | 0.69 |
| reuse | yes | 13 | 11 | 2 | 0 | 0 | 0.85 |
| blast-radius | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 10 | 10 | 0 | 0 | 0 | 1.00 |

Run integrity:

- Lenses: 5 of 5 returned, and none died.
- Skeptic batches: 5 of 5 returned, and none died.
- Demoted or discarded verdicts: 0 contradictory, 0 orphaned duplicate refutations, 0 spurious and 0 duplicates.
- Fixes on confirmed findings: 48 judged sound, 8 judged UNSOUND, 0 with no proposal and 0 NOT JUDGED.
- Severity: 0 confirmed findings were left ungraded by the skeptic, and 6 were re-graded.
- Unverified findings: none.
- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: 1 spec document was supplied as sibling context.
- By design: none was supplied.
- Move check: no checked subject moved.

Lens notes were not supplied, so every lens ran on the kit's generic brief.

No checklist was swept, so a zero count in any class is not evidence that the project's recurring bug classes are absent.

Seven findings were refuted. Five were duplicates (25 of 24, 28 of 37, and 29, 30 and 31 of 34), and two were judged not defects (38, 39).

The skeptic re-graded six findings, and their binding grades are used below. Ids 3, 5, 33, 46 and 56 went from high to medium, and id 15 went from low to medium. I agree with all six grades.

The skeptic judged eight fixes UNSOUND: ids 4, 11, 13, 17, 27, 33, 47 and 55. For each of them the skeptic's corrected fix is the one written here.

## Blockers

### B1 — The context window is pinned at 200k on a node that runs about 1M (id 16)

- **Where:** KICK-dKeptSession-14, section 4 "The window", section 8 F2 and S1.
- **What:** The spec pins `CONTEXT_WINDOW_TOKENS = 200000` and marks it UNVERIFIED. It also says a larger window "errs towards going fresh".
  - On this node, the main-session usages summed to as much as 967091 tokens.
  - 27748 of 31116 main usages were above 200000.
- **Consequence:** The fill readout prints values of up to about 490%. The default 60% threshold fires at 120k tokens, which is about 12% of the real window. So under fresh-at-boundary, every owner session past 120k is told to end at its next item boundary. The spec treats this as a rare case, but on the main path it is the normal one.
- **Fix (skeptic judged SOUND):** Do not pin 200000. Use one of these:
  - derive the window per usage event, at least from the observed maximum;
  - read the window from the model id that the transcript records;
  - reopen F2 with this measurement and choose (b), or a policy key.

  Add an AC in which a fixture transcript with a 900k-token main turn reads under 100%.
- **Left-shift gate:** Add a checklist entry: a spec that pins a platform constant marked UNVERIFIED must cite a measurement taken on the node before it leaves Design.

### B2 — The message id leaves out the recipient and the content key, so notices collide (id 54)

- **Where:**
  - KICK-dKeptSession-22, section 2 S2;
  - KICK-dKeptSession-7, S4 and S5;
  - KICK-dKeptSession-27, S3.
- **What:** `derive_message_id` hashes six fields: build, item, pass, kind, subject and answers. The recipient `to` is not one of them, and neither is the `content-key`. Unit 7 posts `confirmed`, `changed` and `landed` with no `--item` or `--pass`, and it gives every dependent the same subject.
- **Consequence:**
  - When a parent has two dependents, the second dependent's `confirmed` is refused as a duplicate (rc 1).
  - Every `changed` after the first is refused, and so is the second `landed`.
  - Unit 7's rule that a failed notice "fails no transition" hides all of this.
  - Under `confirmed-interfaces`, each refused dependent stays `blocked: awaiting confirmed` until the parent lands.
  - dKeptSession itself has two child builds, so this is the main path.
  - AC7 tests one dependent and one `changed`, so it stays green.
- **Fix (skeptic judged SOUND):** Add `to` as a field of `derive_message_id` in S2. Also do one of these:
  - add the `content-key` as an id field when one is present;
  - have unit 7 pass a distinguishing `--pass` (the Design-exit witness) on every notice.

  Add a red case to unit 22 AC5 or unit 7 AC7, staged against the six-field id. One Design exit with two dependent READMEs must post two `confirmed` rows. Two later Design exits must post two `changed` rows with different keys.
- **Left-shift gate:** Add an arm to unattended.test.sh that posts N notices with distinct (recipient, content-key) pairs and asserts N distinct ids. Add a checklist entry: every dedup key names every field that tells two legitimate messages apart.

## High

### H1 — The scaffold writes standard-default literals that override the named preset (id 1)

- **Where:**
  - KICK-dKeptSession-4, section 2 S2;
  - KICK-dKeptSession-2, S1;
  - KICK-dKeptSession-3, S1 and AC3.
- **What:** `render_scaffold` writes dGroundRules' rows at their literal defaults. One of those rows is the presettable `budgets.enforce = warn`. S2 only adds `preset = "<name>"` above those tables. Unit 2 resolves the file value first, then the preset, then the default, so the file's literal wins.
- **Consequence:**
  - Every adopter that answers `strict` at intake ships `budgets.enforce = warn` instead of strict's `refuse`.
  - `preset --diff` then lists an owner exception nobody chose.
  - Unit 3 AC3 does not hold on a deployer-installed adopter.
- **Fix (skeptic judged SOUND):** In S2, make `render_scaffold(rows, preset)` leave out every row that the named preset assigns. It should write only `never` keys, or write presettable keys as comments. Add an AC that runs after `--preset strict` is applied:
  - `policy.py get budgets.enforce --explain` prints `refuse` with source `preset`;
  - `preset --diff` prints `- no key differs`.
- **Left-shift gate:** Add a policy fixture that scaffolds under each shipped preset and asserts `preset --diff` is empty.

### H2 — The preset store has no rule for the eight derived-default rows (ids 2, 17)

- **Where:**
  - KICK-dKeptSession-1, section 2 S1 and S2, and section 4 Data model;
  - KICK-dKeptSession-2, S1 and AC3.
- **What:** Eight presettable rows have derived catalogue defaults: `roles.effort.<role>`, `roles.effort.<workflow>.<stage>`, `roles.effort.default`, `roles.model.<role>.<harness>`, `maintain.fixes`, `review.<stage>`, `review.<stage>.effort` and `budgets.*`. In v2's table their cells are prose, such as "the role's effort" and "each cap's evidence-derived value", and `check_value` refuses prose. The spec has two rules for every non-`never` row: every preset assigns it, and `standard` equals its literal default. Neither rule can hold for these rows.
- **Consequence:**
  - If the store writes values for these rows, unit 2's step overrides the evidence-derived caps and role efforts in every repository that names any preset, `standard` included.
  - If the store writes nothing, unit 1 AC1 and unit 2 AC3 cannot both pass.
  - Strict's real override of `maintain.fixes` has no specified spelling.
- **Fix (skeptic's corrected fix; the finder's fix for id 17 was judged UNSOUND, and id 2's fix was judged SOUND and agrees with it):**
  - Name the eight rows in S1 and S2.
  - Where v2's cell only restates the derived default, leave the row unassigned in every preset. Exclude it from the completeness check and from the standard-equals-default rule.
  - Where a preset differs from the default, such as strict's `maintain.fixes` "reap, regenerate stale", give every preset a literal value that `check_value` admits. Write the full safe set as the catalogue default's named fixes, and give strict its own subset.
  - Derive AC1's count from that rule.
  - Have unit 2 S1 and AC3 say that the step answers None for an unassigned row.
  - Add a fixture case: `budgets.<cap>` under `preset = "strict"` reads its derived value with source `default`.
- **Left-shift gate:** Have arm_presets assert that every preset value passes `check_value`, and that no row with a derived default carries a value equal to its default's prose.

### H3 — Unit 7's notices collide on one id (id 4; the same defect as B2)

- **Where:** KICK-dKeptSession-7, section 2 S4, with KICK-dKeptSession-22 S2 and S3.
- **What:** Each `changed` uses the fixed subject `interfaces <slug>`, with no `--item`, no `--pass` and no answers. The content key is not an id field, and neither is the recipient. So the second dependent's `confirmed` collides at the very first Design exit, and every `changed` after the first collides too.
- **Consequence:** The post exits 1, the dependent never receives the new content key, and its Build items stay held until the parent lands. AC7 uses one dependent and two moves, so it sees neither collision.
- **Fix (skeptic's corrected fix; the finder's was judged UNSOUND):**
  - Make every notice's id distinct per dependent and per exit. Put the recipient in the subject (`interfaces <slug> to <dependent>`), or add `to` as an id field.
  - Pass `--pass <Design-exit ordinal>`, or the content key as an id field, on `confirmed` and `changed`.
  - Do the same for unit 7 S5's per-dependent `landed`.
  - Extend AC7 to two dependents and three Design exits, and require each post to land.
- **Left-shift gate:** The same arm as B2.

### H4 — The transition guard runs bare `bash`, which reaches WSL (id 22)

- **Where:** KICK-dKeptSession-5, section 2 S9.
- **What:** `write_transition` is a Windows python, and it runs bare `bash <prefix>/unattended/unattended.sh --mail read`. On this node the bare name reaches the WSL launcher, which sees another filesystem.
- **Consequence:** The driver path does not resolve under WSL, and S9 passes "an absent driver" with a NOTE. So the guard can pass with open mail and certify a check it never ran. This class is already recorded in `memory/gotchas/subprocess-resolves-a-different-shell.md`.
- **Fix (skeptic judged SOUND):** Resolve bash with a `resolve_bash` that runs each candidate, as govkit.py:1144 does, and never use the bare name. Add an AC with a WSL-like bare `bash` first on the loader path. The guard must still read the mailbox, or refuse as unknown, and must never pass as an absent driver.
- **Left-shift gate:** Add a lint over specs and kit Python for `subprocess` argv[0] == `"bash"` that does not come from `resolve_bash`.

### H5 — The compaction-fixture verdict is keyed to a binary the fixture never ran (ids 26, 58)

- **Where:** KICK-dKeptSession-12, section 2 S1 and S2.
- **What:** The verdict records, and later compares, the version from `AI_AGENT`, which is the session harness. On this node that is 2.1.308. The fixture runs `claude -p` from PATH, which is 2.1.292.
- **Consequence:**
  - A pass earned by the PATH binary switches off the always-resume override for a harness that was never tested.
  - A PATH upgrade never makes the verdict stale.
  - With `AI_AGENT` unset, both sides read `unknown` and compare equal.
- **Fix (skeptic judged SOUND):**
  - Record the version of the binary the fixture actually launched: `claude --version` from PATH, bounded the way `derive_cli_line` reads it.
  - In S2, compare it with both the PATH version and the session's `AI_AGENT` version, and answer `red` when they differ.
  - Treat `unknown` as `red: cli version unknown`, never as equal.
  - Add an S6 plant in which the recorded cli equals the session version but PATH differs. The reader must answer red.
- **Left-shift gate:** Add a checklist entry: a recorded test verdict is keyed to the identity of the artefact under test, never to an ambient environment variable.

### H6 — `mailbox-message` is not added to the typed record kinds (id 32)

- **Where:** KICK-dKeptSession-5, section 2 S12 and section 4 Files touched.
- **What:** S12 adds a factory row whose files are named `-mailbox-message-<n>.md`. It serves them as `**Serves:** journal <anchor id>`, and it never adds the kind to `TYPED_RECORD_KINDS`.
- **Consequence:** PLAY-dOrderedCharter-42 S2 refuses the factory's import when its table differs from `TYPED_RECORD_KINDS`. That breaks every kind, including the transition log channel the disposal writes through. Otherwise, under S3, the records are malformed.
- **Fix (skeptic judged SOUND):**
  - Serve the records as `**Serves:** mailbox-message <anchor id>`.
  - Add the kind to `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py` and to the closed kind list in `tools/memory-tree/HYGIENE.template.md`, and list both files under Files touched.
  - Add an AC: `gen_build_index.py --print-bindings` binds the AC6 record.
  - If the writer follows TOOL-dWitnessedBar-51 S7's `journal` binding instead, the spec must say so and state how that survives DOC-42 S2's import check.
- **Left-shift gate:** Add a hygiene check that every factory row's kind is in `TYPED_RECORD_KINDS` and matches its Serves kind.

### H7 — The preset store is not a freshness input to the JS mirror (id 47)

- **Where:** KICK-dKeptSession-2, the JS mirror bullet in section 3 Non-goals, and section 4 Files touched.
- **What:** `read_preset_value` adds `tools/policy/presets.toml` as a resolution input, but the spec does not add it to `LEGACY_INPUTS`. The mirror's freshness test compares only the policy, catalogue and `LEGACY_INPUTS` blob ids.
- **Consequence:** When `presets.toml` changes without a re-render, `policy-mirror.js` still reads FRESH. Every hook then gets the old values (scratch-guard's `actions.free`, agent-cap, mail-notice), while `policy.py get` returns the new ones.
- **Fix (skeptic's corrected fix; the finder's was judged UNSOUND):**
  - In spec 2 only, add the presets store's path, resolved as `derive_catalogue_rel` resolves its path, to `LEGACY_INPUTS`.
  - Correct the section 3 claim.
  - Add an AC: change `presets.toml` at a new commit without re-rendering, then `node policy-mirror.js get <key>` reports stale and answers the new value.
  - Leave spec 20 unchanged, because its step answers None at build=None and the mirror never reads a scenario.
- **Left-shift gate:** Add a policy fixture that enumerates the files the resolution order reads and asserts each one is in the mirror's recorded inputs.

### H8 — Three units mint catalogue rows that already exist (id 45; the same defect as M4)

- **Where:**
  - KICK-dKeptSession-8, S1, section 4 Files touched and AC8;
  - KICK-dKeptSession-11, S1 and AC6;
  - KICK-dKeptSession-17, S1 and AC7.
- **What:** Each unit runs `core.py new policy-key` unconditionally for `actions.free`, `notify.owner` and `attendance`. dGroundRules' catalogue already holds all three rows, with owner dKeptSession and the same defaults.
- **Consequence:**
  - The factory appends a duplicate `[[key]]` row, or the wrapped check goes red and restores the file.
  - The ACs read `r[0]` of the row that already stands, so they are green before the unit is built.
- **Fix (skeptic judged SOUND):** Re-ground each S1 as spec 13 S5 and spec 14 do:
  - write the row's `summary` and `usage`;
  - drain the key from `unsummarised-keys.txt`;
  - run `new policy-key` only where the landed catalogue lacks the row.

  Change the Files touched line to match. Rewrite each AC so that it can fail, for example by asserting exactly one row for the name and the summary text this unit writes.
- **Left-shift gate:** Make the factory refuse a name that already stands. Add a spec-audit check that every AC is red at the spec's base revision.

### H9 — Notices stay open forever and gate the dependent's transitions (id 55)

- **Where:**
  - KICK-dKeptSession-5, S7 and S9;
  - KICK-dKeptSession-7, S4 and S5;
  - KICK-dKeptSession-24, section 8 F2.
- **What:** Every message whose kind is not `answer` or `ack` stays `open` until something acknowledges it. An open row addressed to a build refuses that build's transitions. No unit acks unit 7's `confirmed`, `changed` or `landed`.
- **Consequence:** Every parent notice stalls each dependent's transitions until a session runs `--mail ack`, or until `flow.wait-ceiling` passes (72 h by default, 168 h under strict). An unattended dependent never acks.
- **Fix (skeptic's corrected fix; the finder's was judged UNSOUND):**
  - Keep notice kinds gating, which is the clause's rule, and make the consuming step post the ack.
  - When `check_interface_notice` accepts a `confirmed` or `changed` row in the dependent's gate, it posts `--mail ack <dependent> <id>`.
  - The dependent's transition writer acks the `landed`, `superseded` and `withdrawn` rows addressed to it once it has read them. It leaves `changed` to the re-entry that consumes it.
  - Add a red case, staged against the current guard: a parent's Design exit, then one dependent transition with no manual ack. The transition must succeed.
- **Left-shift gate:** Add a checklist entry: every gating message kind names its acker.

### H10 — The `actions.free` arm does not handle the `skipped:` pointer form (id 57)

- **Where:** KICK-dKeptSession-8, S3 and S7, against KICK-dKeptSession-13 S2.
- **What:** S3 reads the `item —` line only as an instance key or `none`. Unit 13 S2 also prints `item — skipped: <why>` when the engine does not resolve.
- **Consequence:** If the builder parses `skipped:` as a key, the arm fails open: every write, commit, push and spawn is admitted with no item in flight. If the builder treats it as a throw, every write is refused, including the commit that would repair the problem.
- **Fix (skeptic judged SOUND):**
  - Add the `skipped:` form to S3 and S7, treat it as unarmed, admit the act, and print `scratch-guard: actions.free unarmed — item pointer skipped: <why>`.
  - Add the plant `item-skipped`: `echo x > f` must exit 0 with that line. Stage it red against an arm that parses `skipped:` as a key.
- **Left-shift gate:** Add a checklist entry: a consumer of a produced line enumerates every form the producer's spec prints.

## Medium

### M1 — `arm_presets` is red on the shipped tree until a dDeclaredLoop ask lands (id 3; re-graded from high to medium)

- **Where:** KICK-dKeptSession-1, S4 and S5, AC6, AC7, AC9 and section 8 F2.
- **What:** S5 is red on "a row-named value that loads while the register attaches nothing". F2 concedes that TOOL-dDeclaredLoop-2 S8, as specced, admits `after-release-verifies`. No precondition in the build order covers that ask.
- **Consequence:** AC9 and AC6 cannot pass at landing. The policy leg goes red, or the arm is skipped and the skip is read as coverage.
- **Fix (skeptic judged SOUND):** Make the ask a build-order precondition, or split S4 and S5 into a later unit. Until the ask lands, S5 prints `presets-core-only · not graded · <why>` for the row-named half.
- **Left-shift gate:** Add a hygiene check that every "waits on <ask>" in a spec has a matching build-order precondition.

### M2 — Unit 25 AC4 cannot pass before dPlacedRequest accepts F4 (id 5; re-graded from high to medium)

- **Where:** KICK-dKeptSession-25, AC4, S4 and the section 7 New arm.
- **What:** AC4's own note says the arm stays red until the F4 ask is accepted. Section 7 still lists AC4 as covered.
- **Consequence:** The arm is red at landing, or it is skipped and counted as coverage. The clause's red case still ships: a waiting build loses its 24 h lease.
- **Fix (skeptic judged SOUND):** Make the F4 acceptance a stated precondition, or move AC4 and S4 into a later unit. Until then, drop AC4 from the "covers" list and state the gap as NOT OBSERVED.
- **Left-shift gate:** The same check as M1.

### M3 — Unit 10 uses `--local` before unit 21 adds it (id 6)

- **Where:** KICK-dKeptSession-10, S4, section 4 "The boundary step", AC2 and section 3 Edges.
- **What:** Unit 10 (order 20) passes `--local` to `--mail read`. Unit 21 (order 22) adds the flag, and unit 10 declares no edge to unit 21.
- **Consequence:** Against the real driver the flag is an unknown option at unit 10's build. AC2 passes only against a stub.
- **Fix (skeptic judged SOUND):** Move `--local` into unit 5's S8, or into unit 10, and have unit 21 consume it. Otherwise reorder unit 21 before unit 10 and add the reciprocal edge pair.
- **Left-shift gate:** Add a hygiene edge check that every flag a unit uses is introduced by itself or by a unit earlier in the build order that it declares an edge to.

### M4 — The catalogue rows already exist, so S1 is moot and the ACs cannot fail (ids 7, 34; the same defect as H8)

- **Where:** KICK-dKeptSession-8, S1 and AC8; KICK-dKeptSession-11, S1 and AC6; KICK-dKeptSession-17, S1 and AC7.
- **What:** The defect is the one in H8, as seen by the coherence and reuse lenses. Specs 9, 10 and 21 already say there are no new rows, and specs 13 and 14 run the factory only where the row is missing.
- **Fix (skeptic judged SOUND):** Rewrite each S1 as unit 13 S5 does. Cite `catalogue.toml:223`, `:543` and `:60` on the dGroundRules branch. Have each AC observe the summary, and that the key is gone from `unsummarised-keys.txt` after `lists --write`.
- **Left-shift gate:** The same as H8.

### M5 — Two specs disagree on whether PreToolUse carries `additionalContext` (ids 8, 37)

- **Where:** KICK-dKeptSession-21, section 8 F1 and S5, against KICK-dKeptSession-14 section 8 F1 and KICK-dKeptSession-13 S7.
- **What:** Unit 21 F1 says no PreToolUse builder was seen, so it adds a third hook registration, which unit 13 F1 rejected. On the installed 2.1.292 CLI the PreToolUse builder exists, and unit 21 S4 still routes through unit 13's PreToolUse step.
- **Consequence:** One platform fact has two answers. A reader who trusts unit 21 may "fix" a working channel, or add a surface that is not needed.
- **Fix (skeptic judged SOUND):**
  - Re-run one probe against the CLI version that RUN.md pins (2.1.308) and the node's (2.1.292).
  - Record the answer once in unit 13 S7, which owns the channel, and have units 14 and 21 cite it.
  - If the only reason for the new hook is coverage of non-Bash tools, say so in F1. Otherwise extend unit 13 S7's existing scratch-guard step.
- **Left-shift gate:** Add a checklist entry: one FACT-QUESTION, one owning record, and every other spec cites it.

### M6 — The boundary verb's 10 s bound is shorter than the steps it runs (id 9)

- **Where:** KICK-dKeptSession-13, S7 (`BOUNDARY_BOUND_S = 10`), against S4 and S6 and the steps that units 5, 21 and 26 add.
- **What:** These steps run in series inside the 10 s bound:
  - unit 21's notice fetch and unit 5's `mail —` read, each under `CARD_CLAIMS_BOUND = 15`;
  - unit 26's budget call, under 10 s;
  - a publish, which is a push.
- **Consequence:** On a slow remote the hook kills the verb and prints nothing, so the advice, the interrupts and the notices are lost. If `at` does not move, every later Bash call pays up to 10 s again.
- **Fix (skeptic judged SOUND):** Give the boundary verb one shared budget that sits under the hook's bound: pass a deadline down, or run the networked steps with `--local` and fetch detached. State that `at` moves even when a step times out. Add a plant with an unreachable remote and two Bash calls, in which the second call spawns no verb.
- **Left-shift gate:** Add a checklist entry: an outer bound must exceed the sum of the inner bounds it wraps.

### M7 — The tool-call hook binds the build only through a run lease (id 10)

- **Where:** KICK-dKeptSession-21, S5.
- **What:** `resolveLease` matches only unattended RUN.md records that carry a `session:` fact. Units 8, 13, 14 and 15 bind the build through the session card's `## route`.
- **Consequence:** Under `every-tool-call`, an attended routed session gets no tool-call notice but does get the boundary notice.
- **Fix (skeptic judged SOUND):** Bind through the card route (`readCard` and `extractRouteUnits`), falling back to `resolveLease`. Add an AC for an attended, card-routed session with no lease that prints the `additionalContext`.
- **Left-shift gate:** Add a shared build-binding helper that every hook calls, and add a checklist entry against a per-hook binding.

### M8 — Under `at-transitions` the item pointer is stale between transitions (id 11)

- **Where:** KICK-dKeptSession-8, S3, S4 and section 5 risks, against KICK-dKeptSession-13 S5 and S6.
- **What:** `actions.free` reads the build card's `item —` line. Under `card.pointers = at-transitions`, which is velocity's value, that line is written only at transitions.
- **Consequence:** Acts are judged against a stale item. Writes are refused while the pointer reads `none`, or admitted against a finished item.
- **Fix (skeptic's corrected fix; the finder's was judged UNSOUND):** Have unit 13 S6 rewrite the `item —` line locally, in both the session card and the build card file, at every crossing under both values, with `at-transitions` gating only the publish. Then have unit 8 S3 read that line. Add an AC that runs unit 8's plants under `card.pointers = at-transitions`.
- **Left-shift gate:** Run unit 8's fixture under every allowed value of `card.pointers`.

### M9 — Unit 9's one exit-1 path is never observed (id 15; re-graded from low to medium)

- **Where:** KICK-dKeptSession-9, S4 and S6.
- **What:** An `owner-ceiling` breach under a refusing `budgets.enforce` or `budgets.pinned` prints `orient REFUSED` and exits 1. AC5 checks only the warn path.
- **Consequence:** A build that ignores `budgets.enforce` passes, even though strict sets it to `refuse`.
- **Fix (skeptic judged SOUND):** Add a plant with `budgets.enforce = "refuse"`, or `budgets.pinned` naming `orient-calls`. A row past 30 must print `orient REFUSED` and exit 1.
- **Left-shift gate:** Add a spec-audit check that every exit code a spec names has an AC that observes it.

### M10 — Stale "not applied" text survives where S2 and AC6 cannot see it (id 19)

- **Where:** KICK-dKeptSession-2, the S2 Readers list and AC6.
- **What:** The `read_default_value` docstring (policy.py:689-690) and README:455 still describe the preset as unapplied. AC6 greps a phrase that neither text contains.
- **Consequence:** Stale docs ship and AC6 goes green over them.
- **Fix (skeptic judged SOUND):** Add policy.py:689-690, README:235 and README:455 to the Readers list. Make AC6 grep a class of wording, such as `not applied\|unapplied\|no step applies`, over the kit and help/.
- **Left-shift gate:** Grep ACs for retired wording by a class of phrasings, never by one exact phrase.

### M11 — `adopt-policy.sh` swallows the scaffold's refusal (id 20)

- **Where:** KICK-dKeptSession-4, S2 and AC4.
- **What:** The wrapper runs the scaffold with `2>/dev/null` and maps every failure to exit 1 with a generic line. AC4 expects exit 2 naming `lax` and the four shipped presets.
- **Fix (skeptic judged SOUND):** State in S2 that `adopt-policy.sh` passes the scaffold's exit 2 and its stderr through on a refusal, and keeps exit 1 for a write failure. Name the dGroundRules lines that change.
- **Left-shift gate:** Add a checklist entry: a wrapper that discards stderr cannot carry a refusal the spec promises.

### M12 — The `orient-calls` cap row lacks fields the census requires (ids 21, 46; id 46 re-graded from high to medium)

- **Where:** KICK-dKeptSession-9, S6 and section 4 Files touched.
- **What:** The row gives only class, unit, enforcer, home and family. The census also requires `research`, and because `ships` defaults to true it requires `kit` and `installed` as well. `CAP_CASES` also needs a `budgets-cap-orient-calls` case.
- **Consequence:** `read_cap_census` refuses the whole census, so `budgets.py resolve` and `budgets.py check` exit 2 for every cap, in gov and in every adopter. The census arm and the per-row fixtures would go red before landing.
- **Fix (skeptic judged SOUND):**
  - Spell the whole row: a stated `research` value, or a schema change that lets a non-research row carry none; `kit = "runlog"`; and `installed = "{prefix}/runlog/runlog.py"`. Alternatively, set `ships = false` with a reason.
  - Add the `CAP_CASES` case, and list check_policy.py under Files touched.
  - Add an AC: `budgets.py resolve orient-calls` exits 0.
  - Run `policy fixtures` over the new row.
- **Left-shift gate:** Add a checklist entry: a spec that adds a schema row cites the schema's required fields.

### M13 — Unit 10's mail read runs bare `bash` (id 23)

- **Where:** KICK-dKeptSession-10, S2 and S6.
- **What:** `read_mail_interrupts` runs bare `bash` from position.py, which reaches WSL on this node. S6 maps a failed read to `unarmed`.
- **Consequence:** Every boundary mail interrupt reads unarmed on node d.
- **Fix (skeptic judged SOUND):** Resolve bash as `govkit.resolve_bash` does, and say so in S2. Add a fixture arm with a decoy bare `bash`.
- **Left-shift gate:** The same lint as H4.

### M14 — Unit 7 runs bare `bash` and its interface listing can carry CRLF (id 24)

- **Where:** KICK-dKeptSession-7, S1, S3 and S4.
- **What:** S1 runs bare `bash … --claims`, which reaches WSL. The interface listing that S3 and S4 hash is written by Python with no stated newline mode.
- **Consequence:** Every parent reads `unreachable`, so Build is held. A listing written on Windows hashes differently from the same listing on Linux, so `check_interface_notice` stays `unconfirmed`.
- **Fix (skeptic judged SOUND):** Resolve bash as `govkit.resolve_bash` does. Write the listing as LF bytes (`newline='\n'`), or hash the ls-tree output directly. Add an AC that posts from a CRLF-configured clone and confirms on an LF clone.
- **Left-shift gate:** The same lint as H4, plus a checklist entry: any file that feeds a content hash states its byte encoding.

### M15 — The mail-notice hook's "no git, file reads only" claim is false (id 27)

- **Where:** KICK-dKeptSession-21, S5 and section 4 "The tool call, in order" with its cost paragraph.
- **What:** Each call runs `readPolicy('mailbox.notice')`, and that spawns git three times and bash once (about 0.27 s), or more when the mirror is stale. AC5 greps only mail-notice.js, so it cannot see those spawns.
- **Fix (skeptic's corrected fix; the finder's was judged UNSOUND):**
  - Have the boundary verb, which already reads `mailbox.notice` and `mailbox.fetch-seconds` through I8's shell form, write both resolved values into the per-worktree sidecar beside the stamp (F2's file).
  - Have the hook read them with the stamp's statSync/read and call no `readPolicy`.
  - Correct S5 and section 4's cost statement.
  - Add an AC: a stubbed git or bash on PATH is never invoked by one hook call.
- **Left-shift gate:** Make hot-path hook ACs observe spawns through a PATH stub, never through a source grep.

### M16 — Unit 10 builds a second mail-interrupt path beside the parent's slot (id 33; re-graded from high to medium)

- **Where:** KICK-dKeptSession-10, S2, section 8 F2 and AC1.
- **What:** Unit 10 adds `read_mail_interrupts` behind `--mail-interrupts`. It never says what becomes of the mail slot in TOOL-dDeclaredLoop-7 S4's `derive_interrupts`.
- **Consequence:** The parent's unarmed line is left in place after the mailbox lands, or it is removed with no parent text that authorises the removal.
- **Fix (skeptic's corrected fix; the finder's was judged UNSOUND):** Widen section 8 F3's ask so that TOOL-dDeclaredLoop-7 S4 itself drops the mailbox entry from `derive_interrupts`' default output, or prints it only under `--mail-interrupts`. The ask names unit 10's flag as the one mail reader. Rewrite AC1's "plain engine call" clause against the amended parent text.
- **Left-shift gate:** Add a checklist entry: a unit that arms a parent's slot either fills that slot or amends the parent through a filed ask.

### M17 — `read_dependents` re-derives an edge that memory-tree already inverts (id 35)

- **Where:** KICK-dKeptSession-7, S4, section 4 "The notices", the Inventory and section 10.
- **What:** `read_dependents` re-parses `parents:` from every build README. gen_build_index.py:2615-2626 already inverts it, and refuses a parent that is not a build.
- **Consequence:** The two readers can disagree. A missed dependent never gets its notices.
- **Fix (skeptic judged SOUND):** Expose the inverted `children` map through a read verb or a `tree_lib` helper, reached by subprocess through `resolve_kit_dir`, or read the rendered `<!-- gen:build-edges -->` region. Cite it in section 10, and drop `read_dependents`.
- **Left-shift gate:** Add a reuse checklist entry for any reader of `parents:`.

### M18 — The replay order drops the `map —` block that dOrderedCharter-4 put first (id 36)

- **Where:** KICK-dKeptSession-12, S5 (I10) and AC6.
- **What:** I10 starts with the stored card and leaves out `derive_map_block`. PLAY-dOrderedCharter-4 decided the map prints first, so that the 10,000-character hook cap cuts the card's tail and never the map.
- **Fix (skeptic judged SOUND):** Start I10's order with `derive_map_block`'s lines, then the stored card, then `now —`, then the computed lines. Add `map —`, or the map's first line, to AC6's ordering check.
- **Left-shift gate:** Have the replay arm assert that the map's first line is the first line out.

### M19 — The `records —` line is bounded on a closed set of five that is growing (id 40)

- **Where:** KICK-dKeptSession-13, section 8 F3 and S3.
- **What:** F3 assumes the record kinds stay a closed set of five (`tree_lib.py:406`). DOC-42 S1 makes the set `RECORD_KIND_TOKENS = (four base kinds) + TYPED_RECORD_KINDS`, which grows with each typed kind the chain mints.
- **Consequence:** The line outgrows its bound. Past `CARD_CAP_BYTES`, S4 refuses the whole pointers write, so the `item —`, `budget —` and `mail —` lines go unwritten.
- **Fix (skeptic judged SOUND):** Re-ground F3 on DOC-42's tuple. Restrict the line to a subset, such as `RECORD_KIND_TOKENS` minus `TYPED_RECORD_KINDS`, or cap it by bytes with a `… (+k)` cut. Add an AC that plants the full set of typed kinds under the cap.
- **Left-shift gate:** Add a checklist entry: a bound grounded on a set cites that set's decided future definition.

### M20 — Driver refusals grow past the census ceiling with no review planned (id 48)

- **Where:** KICK-dKeptSession-5, section 4 Files touched and section 7. Units 6, 7, 11, 21, 22, 24, 25, 27 and 28 have the same omission.
- **What:** `REFUSAL_CEILINGS` holds unattended.sh at 323. Ten units add fail and exit-1 sites to the driver. None of them names the budget, its `.memory-tree.conf` line, or the retirement review that raises it.
- **Consequence:** The `harness arms` leg goes red. The alternative is to raise the ceiling without the review the budget requires.
- **Fix (skeptic judged SOUND):**
  - In spec 5, add `.memory-tree.conf` (`REFUSAL_CEILINGS`, and `ARMS_FLOORS` for the `unattended.sh` pair) and `memory/DECISIONS.md` to Files touched.
  - Plan the retirement review, or route the new refusals through `check_verb_flag`/`VERB_REQUIRES` and `print_env_failure` so that the census does not grow.
  - Have each later driver spec state its census delta.
  - Run `check-arms.py --check` after each driver pass.
- **Left-shift gate:** Have the spec-audit brief list the budgeted legs that a touched file falls under.

### M21 — Edits to watched files owe a kickoff-manifest re-stamp that no spec declares (id 49)

- **Where:**
  - KICK-dKeptSession-12, section 4 Files touched;
  - units 5, 10, 13, 14, 15, 21 and 26, which edit manifest-check.sh;
  - unit 1, which edits gate-legs.json;
  - units 3 and 11, which edit the charter template.
- **What:** All of these files are on the `watch:` list in SESSION-KICKOFF.md, and no spec declares the re-stamp they owe.
- **Consequence:** The `kickoff-manifest ratchet` leg goes red, or the re-stamp is an undeclared write.
- **Fix (skeptic judged SOUND):** Add `memory/guides/SESSION-KICKOFF.md` (the `last-audit` re-stamp) to each affected spec's Files touched, and the `kickoff-manifest ratchet` leg to its section 7. Alternatively, fold one re-stamp into the build's close and say so in the README's build-level rules.
- **Left-shift gate:** Add a spec-audit check that warns when Files touched intersects `watch:` and leaves out SESSION-KICKOFF.md.

### M22 — The new hook and new symbols leave the codebase map unclaimed and stale (id 50)

- **Where:** KICK-dKeptSession-21, section 4 Files touched, and every spec that mints a function under tools/ or skills/.
- **What:** `mail-notice.js` becomes a new `harness-hooks` key that no dossier claims. The new functions also make `memory/map/generated/*` stale.
- **Consequence:** The `codebase-map coverage + freshness` leg fails twice, and the baseline cannot take the new key.
- **Fix (skeptic judged SOUND):**
  - Add `memory/map/features/unattended.md`, with the `PostToolUse tools/unattended/mail-notice.js` claim, to Files touched.
  - In every spec that mints a symbol, state the regen with the command that `map_lib.regen_cmd()` prints, or declare the generated artefacts a shared render in the build README.
  - Add the codebase-map leg to spec 21's section 7.
- **Left-shift gate:** The same brief extension as M20.

### M23 — The compaction fixture is not shipped, so `always-resume` is dead in adopters (id 51)

- **Where:** KICK-dKeptSession-12, S1-S3 and section 4 Files touched and Migration.
- **What:** The kickoff kit descriptor is `kind = "flat"` with an explicit `[[files]]` list, and that list leaves out `card-compaction.fixture.sh`.
- **Consequence:** In every adopter the verdict reads `red: no fixture installed`, so `always-resume` always reads as `fresh-when-idle`.
- **Fix (skeptic judged SOUND):** Add the fixture to `tools/govkit/entries/kickoff-manifest.kit.toml` `[[files]]` and to Files touched. Alternatively, state in section 3 and help/orientation-card.md that `always-resume` is honoured only where the fixture is installed. In both cases add an AC over a scratch install from the deployer.
- **Left-shift gate:** Have a govkit selfcheck assert that every file a shipped script reads by path is in its kit's `[[files]]`.

### M24 — The unattended kit gains an undeclared dependency on playbook-render (id 52)

- **Where:** KICK-dKeptSession-28, S3 and section 4 Files touched.
- **What:** `check_mail_recipient` now runs `render_playbook.py --fleet-tags`, and `tools/unattended/kit.toml`'s `requires` does not name `playbook-render`.
- **Consequence:** An adopter that installs unattended alone gets every `node:<tag>` recipient refused.
- **Fix (skeptic judged SOUND):** Add `playbook-render` to `requires` and list kit.toml under Files touched. Alternatively, declare the `node:` form optional, with its refusal text in the verbs guide. Add an AC over a scratch install with unattended selected alone.
- **Left-shift gate:** Have a govkit selfcheck assert that every cross-kit invocation is covered by `requires`.

### M25 — `--mail post` lets anyone ack or answer another build's question (id 56; re-graded from high to medium)

- **Where:** KICK-dKeptSession-5, S5, S7 and S8, with KICK-dKeptSession-25 S2.
- **What:** `--mail post` accepts `--kind ack` and `--kind answer` with any `--answers <id>`. S7 counts such replies whoever sent them.
- **Consequence:** A third build can release another build's question. A question can also be answered twice, or answered with no cites, which bypasses the checks in S8 and unit 25.
- **Fix (skeptic judged SOUND):** Refuse `--kind ack` and `--kind answer` on `--mail post` with exit 2, naming the dedicated verbs. Alternatively, count a reply only when its `build` is the build the answered row was addressed to. Add a red case to AC4: a third build's ack leaves the row `open`.
- **Left-shift gate:** Add a checklist entry: every check on a dedicated verb is either enforced at the shared write path, or that path refuses the verb's kinds.

### M26 — The transition guard fails open when the read exits non-zero (id 59)

- **Where:** KICK-dKeptSession-5, S9.
- **What:** S9 does not say what happens when `--mail read --open` exits non-zero for a reason other than a timeout. The likely build reads the empty output as zero rows.
- **Fix (skeptic judged SOUND):** Any exit other than 0 refuses with exit 2, prints the exit code and the first stderr line, and writes nothing. Only `mail — off` and a missing driver pass. Add a red case: a planted reader that exits 3 with no output.
- **Left-shift gate:** Add a checklist entry: every guard enumerates its read's non-zero exits, and the default is to refuse.

### M27 — A failed fetch before the duplicate check is unhandled (id 60)

- **Where:** KICK-dKeptSession-5, S5.
- **What:** S5 never says what the post does when its one bounded fetch fails.
- **Consequence:** The duplicate check runs on a stale cache, so a retry writes a second copy, which is gap-conc-09.
- **Fix (skeptic judged SOUND):** A failed or timed-out fetch refuses the post with exit 2 and the fetch's cause, before any commit. Alternatively, state offline posting as a known source of duplicates that the reader collapses. Add an AC: with the origin unreachable, the post exits 2 and builds no commit.
- **Left-shift gate:** The same checklist entry as M26, applied to every fetch that precedes a check.

### M28 — The detached spawn flashes a console window, and AC5 cannot see async spawns (id 61)

- **Where:** KICK-dKeptSession-21, S6 and AC5.
- **What:** The detached spawn sets no `windowsHide`, so on win32 it opens a console window. AC5 greps only `execFileSync|spawnSync`.
- **Fix (skeptic judged SOUND):** Add `windowsHide: true`, following format-guard.js:248 and stop-guard.js:113. Have AC5 stub `child_process` and assert exactly one spawn site, whose argv[0] is `bash` and whose argv[1] is the driver.
- **Left-shift gate:** Add a lint that every `spawn` or `exec*` in hook JS sets `windowsHide`.

### M29 — A repository preset may shadow a shipped preset name (id 62)

- **Where:** KICK-dKeptSession-1, S3, and KICK-dKeptSession-2 S1's use of `derive_preset_assignment`.
- **What:** Nothing stops a repository from declaring `[presets.strict]`. The resolver answers the shipped table for a shipped name.
- **Consequence:** The repository's declared overrides are ignored silently. A builder who lets the declaration win instead makes `strict` mean different things in different repositories.
- **Fix (skeptic judged SOUND):** `validate` refuses a `[presets.<shipped name>]` table, naming its line and the shipped name. Add that plant to AC5, which must exit 1.
- **Left-shift gate:** Add a checklist entry: every user-declared namespace states its rule on collision with shipped names.

### M30 — `emit_progress` has no time bound and no failure rule (id 63)

- **Where:** KICK-dKeptSession-11, S5.
- **What:** `emit_progress` runs a Python verb inside `verb_park` and `verb_landed` with no bound and no failure rule.
- **Consequence:** A hung or crashing reader, or the MS-Store python3 stub, stalls the lander's verbs or adds noise to them.
- **Fix (skeptic judged SOUND):** Bound the call with `REMOTE_BOUND`, or with a new 10 s constant. On a non-zero exit or a timeout, print one `NOTE — progress not emitted: <why>` and never change the verb's exit or lines. Add an AC with a progress verb stubbed to sleep: `--landed` still exits 0 within the bound.
- **Left-shift gate:** Add a lint that every subprocess call in unattended.sh is wrapped in `timeout`.

## Low

### L1 — Unit 18 AC3 is already green at HEAD (id 12)

- **Where:** KICK-dKeptSession-18, AC3.
- **What:** The ask that AC3 checks for, TOOL-dIndexedDesign-19, is already filed. So the AC cannot fail in the build run.
- **Fix (skeptic judged SOUND):** Have AC3 observe what the build produces: the help-page line on the path stand-in, or a fixture in which a `repeat` request routes by path. Alternatively, mark the ask as a spec-run artefact and leave it out of section 6.
- **Left-shift gate:** The same red-at-base check as H8.

### L2 — Unit 14 AC7 observes unit 13's code, not unit 14's (id 13)

- **Where:** KICK-dKeptSession-14, AC7.
- **What:** Unit 13 AC5, built earlier, already guarantees the `agent_type` skip that AC7 checks.
- **Fix (skeptic's corrected fix; the finder's was judged UNSOUND):** Drop AC7 and have S5 cite KICK-dKeptSession-13 AC5. Alternatively, if this unit is to own a check, first add a role check to S5's boundary act and observe it at `--card --boundary` directly.
- **Left-shift gate:** The same red-at-base check as H8.

### L3 — Unit 16 calls its list the third when it is the fourth (ids 14, 44)

- **Where:** KICK-dKeptSession-16, section 4 Files touched and section 10.
- **What:** KICK-dKeptSession-19 already adds `unnamed-keys.txt` as the third list.
- **Fix (skeptic judged SOUND):** Say "the fourth list, beside `unsummarised-keys.txt`, `legacy-homes.txt` and KICK-dKeptSession-19's `unnamed-keys.txt`".
- **Left-shift gate:** None fits. Add a checklist entry: avoid ordinals that sibling units can shift.

### L4 — Unit 1 cites a short range for v2's never list (id 18)

- **Where:** KICK-dKeptSession-1, S1 and the section 4 data-model comment.
- **What:** The never list runs from v2:1430 to v2:1437. The cited ranges, v2:1420-1433 and v2:1427-1433, miss its last four lines.
- **Fix (skeptic judged SOUND):** Cite v2:1424-1437: the pair rules at 1424-1429 and the never list at 1430-1437.
- **Left-shift gate:** Add a checklist entry: a range citation ends at the cited block's closing line.

### L5 — Unit 14 adds a second transcript fixture format (id 41)

- **Where:** KICK-dKeptSession-14, S6, AC1 and the Inventory.
- **What:** A standalone `context-fill.jsonl` sits beside `fixtures/transcripts.json`.
- **Fix (skeptic judged SOUND):** Add a `context-fill` scenario to `transcripts.json` and write it the way the other scenarios are written. AC1 then runs over the written main file.
- **Left-shift gate:** Add a reuse checklist entry for fixture stores.

### L6 — Unit 9 does not reuse `_derive_quartiles` or the token sum (id 42)

- **Where:** KICK-dKeptSession-9, S2, S4, the Inventory and section 10.
- **Fix (skeptic judged SOUND):** Call `_derive_quartiles` (runlog.py:210) for the quartiles. Extract the four-field token sum once, beside I13's `derive_context_tokens`, and use it in both `print_ready` and `measure_orient_tree`. Cite both in section 10.
- **Left-shift gate:** Add a reuse checklist entry.

### L7 — The pair rule is evaluated in a third place (id 43)

- **Where:** KICK-dKeptSession-20, S2, with the KICK-dKeptSession-1 section 4 Inventory.
- **Fix (skeptic judged SOUND):** Mint one `check_preset_pairs(assignment, pairs)` in `tools/policy/presets.py`, called by `check_presets` and `check_repo_presets`. Have unit 20 S2 call it through the policy kit's subprocess or verb, and name it in both inventories.
- **Left-shift gate:** Add a reuse checklist entry.

### L8 — Five specs declare a `subject-pins.tsv` regen that does nothing (id 53)

- **Where:** KICK-dKeptSession-6, section 4 Files touched. Units 7, 21, 24 and 25 carry the same line.
- **What:** The pins derive only from gate-legs.json, which none of these specs touches. Spec 5 rev-1 says exactly this and leaves the file out.
- **Fix (skeptic judged SOUND):** Drop the line from all five specs, or add the gate leg that would move a pin. Either way, keep spec 5 and its siblings in agreement.
- **Left-shift gate:** Add a spec-audit check that a declared regen names an input the spec changes.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=63 confirmed=56 refuted=7 unverified=0 blocker=2 high=12 medium=33 low=9 agents=11 out-tokens=302738

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-4.md:section 2 S2 (with KICK-dKeptSession-2 S1 and KICK-dKeptSession-3 S1/AC3) | high | high | confirmed | Ran git show 3c8c4718a:tools/policy/policy.py. render_scaffold writes r['default'] for every row where owner == SCAFFOLD_OWNER ('dGroundRules', :98) and the default is not derived. Over the catalogue at 3c8c4718a that gives policy-file.on-invalid=last-valid, runtime.agents-in-flight=6, budgets.enforce=warn and budgets.pinned=[]. v2:1427-1435's never list holds the other three but not budgets.enforce, and v2:1669 reads `budgets.enforce \| warn \| warn \| refuse \| warn`. Unit 2's RESOLUTION_ORDER is (read_file_value, read_preset_value, read_default_value), so the file's literal warn beats strict's refuse. Unit 4 S2 only adds the preset line 'above dGroundRules' tables' and never says to drop presettable keys. Every strict adopter gets the wrong value. | sound | - |
| 2 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md:section 2 S1/S2, section 4 Data model (with KICK-dKeptSession-2 S1, AC3) | high | high | confirmed | At 3c8c4718a the catalogue has derived defaults for budgets.*, roles.effort.<role>, roles.effort.<workflow>.<stage>, roles.effort.default, roles.model.<role>.<harness>, maintain.fixes and review.<stage>.effort. None of them is on v2's never list. v2's preset rows give prose for them ('each cap's evidence-derived value' :1668, 'the role's effort' :1512-1513, 'reap, regenerate stale' :1638). Unit 1 S1/S2 require every presettable key in each preset, and AC1 is red on a missing one. Unit 2 S1 says 'a preset that assigns the key no value answers None', but unit 2 AC3 requires every presettable key to read its preset value with source preset. Neither unit names a rule for these rows, so the store cannot satisfy both units as written. | sound | - |
| 3 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md:section 2 S4/S5, section 6 AC6 AC7 AC9, section 8 F2 | high | medium | confirmed | Unit 1 S5 (lines 68-72) says the arm is red on 'a row-named value that loads while the register attaches nothing at its point'. §8 F2 states that TOOL-dDeclaredLoop-2 S8 as specced admits after-release-verifies, and that 'this unit's AC6 to AC8 wait on it'. AC9 is not listed among the waiting criteria, yet it needs arm_presets at 0 findings over the shipped tree. That cannot hold until the ask lands. The README build order has no precondition for the ask (dDeclaredLoop is only listed as a parent build). The consequence is a red or skipped arm at landing, not a wrong shipped result, so this is medium. | sound | - |
| 4 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-7.md:section 2 S4 (with KICK-dKeptSession-22 S2/S3) | high | high | confirmed | Unit 22 S2 derives the id from build, item, pass, kind, subject and answers, with each absent field written none. Its risks line (:120) says equal fields make one message. Unit 5 S5 exits 1 on a duplicate. Unit 7 S4 posts subject `interfaces <slug>` with no --item and no --pass, and the content-key is not an id field. So the second `changed` repeats the first one's id. Worse, the recipient is not an id field either, and unit 5 S4 headers carry only `<slug>/<id>`. S4's 'one message per dependent' therefore collides on the second dependent's `confirmed` at the very first Design exit, and dKeptSession itself has two child builds. AC7 has one dependent and two moves, so it sees neither collision. | unsound | - |
| 5 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-25.md:section 6 AC4, section 2 S4, section 7 New arm | high | medium | confirmed | Unit 25 AC4 (:206-214) carries the note 'observable once dPlacedRequest accepts §8 F4's ask; before it, the planted case reads `stale` both ways and the arm stays red'. §7 (:228) still lists AC4 among the unattended.test.sh arm's coverage. §5 risks (:181) concedes that a 72-hour wait loses a 24-hour lease until then. Nothing in the build order makes the ask a precondition. The result is an arm that is red at landing, or skipped and counted as coverage. | sound | - |
| 6 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-10.md:section 2 S4, section 4 'The boundary step', section 6 AC2, section 3 Edges | medium | medium | confirmed | Ran grep -n -- '--local' over the spec set. Unit 10 uses it at :55, :111, :113 and :177-178, and its AC2 has a stub record `--mail read` with --local. Unit 21 :45 is where the flag is added ('This unit adds `--local` to'). Unit 5 S8 (:84) lists only `--mail read <who> [--open] [--ids]`. Unit 10's edges (:85-88) name units 13 and 5 and externals, and no unit-21 edge. The build order puts unit 10 at step 20 and unit 21 at step 22. | sound | - |
| 7 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-8.md:section 2 S1, section 6 AC8 (same in KICK-dKeptSession-11 S1/AC6 and KICK-dKeptSession-17 S1/AC7) | medium | medium | confirmed | Ran python with tomllib over git show 3c8c4718a:tools/policy/catalogue.toml. It holds actions.free (owner dKeptSession, default read-only-probes, no summary), notify.owner (dKeptSession, turn-micro-formats, no summary) and attendance (dKeptSession, unattended, no summary). Units 8, 11 and 17 S1 each create the row with `core.py new policy-key`. Unit 13 S5 (:63-67), by contrast, runs the factory 'only where the landed catalogue lacks the row'. AC8 of unit 8, AC6 of unit 11 and AC7 of unit 17 print owner and default, which already match the existing rows, so they are green before the units are built. | sound | - |
| 8 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-21.md:section 8 F1 (against KICK-dKeptSession-14 §8 F1 and KICK-dKeptSession-13 S7) | medium | medium | confirmed | Unit 21 F1 says 'no such builder was seen naming PreToolUse'. Unit 14 F1 says PreToolUse carries it. Unit 21 S4 (:63) still routes through unit 13 S7's PreToolUse output. I re-probed /c/Users/daily-agent/.local/bin/claude, which reports 2.1.292, with grep -a -o. It printed `type:"hook_additional_context",content:Te.additionalContexts,hookName:`PreToolUse:${n.name}`,toolUseID:s,hookEvent:"PreToolUse"`, so a PreToolUse builder exists on this node. 2.1.308 was not available to probe. The two records contradict each other, and unit 21's is false on the node's CLI. | sound | - |
| 9 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-13.md:section 2 S7 (`BOUNDARY_BOUND_S = 10`) against S4/S6 and the steps units 5, 21, 26 add | medium | medium | confirmed | skills/session-kickoff/manifest-check.sh:228 reads `CARD_CLAIMS_BOUND=${CARD_CLAIMS_BOUND:-15}`. Unit 13 S7 (:80) runs S6 under BOUNDARY_BOUND_S = 10, and a timeout prints nothing. The steps inside it carry longer or equal bounds: unit 21 S4's notice under CARD_CLAIMS_BOUND (15), unit 5 S13's `mail —` read under CARD_CLAIMS_BOUND (15), and unit 26 S1's CARD_BUDGET_BOUND = 10. Unit 13 S4 also publishes through publish_build_card. These run in series inside the 10 s outer bound. A slow remote makes the hook drop all output, and an incomplete pointer write re-triggers the verb on the next call. | sound | - |
| 10 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-21.md:section 2 S5 | medium | medium | confirmed | Unit 21 S5 (:66-75) binds the build through resolveLease(root, memoryRoot, sessionId), and 'a session bound to no build ... exit 0 in silence'. tools/unattended/run-lease.js:137-175 shows scanLeases reads only builds/<slug>/RUN.md records with a non-absent `session:` fact, and resolveLease filters those by session id. An attended session routed by its card has no such record. Unit 8 S3 (:43-44) and unit 13 S7 take the build from the session card's `## route`. So under every-tool-call an attended routed session gets no tool-call notice but does get the boundary notice. | sound | - |
| 11 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-8.md:section 2 S3/S4, section 5 risks (against KICK-dKeptSession-13 S5/S6) | medium | medium | confirmed | Unit 8 S3 (:43-49) reads the build card's `item —` line through `--card --path --build`, and both S3 and §5 risks (:173) say unit 13 rewrites it at each boundary. Unit 13 S5 says `at-transitions` writes at transitions only, and S6 runs S4 on a crossing only under every-item. v2:1562 reads `card.pointers \| at-transitions \| every-item \| every-item \| every-item`, so velocity takes at-transitions, and there the pointer is stale between transitions. | unsound | - |
| 12 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-18.md:section 6 AC3 | low | low | confirmed | Ran python tools/memory-tree/gen_build_index.py --asks --build dIndexedDesign. It printed `\| TOOL-dIndexedDesign-19 \| OPEN \| LOW \| — \| 2026-10-26 \| dIndexedDesign \| THE repeat ROUTE READS A PLAYBOOK BY PATH. dKeptSession carries… \|`, and memory/builds/dIndexedDesign/BACKLOG.md:7 holds it. Unit 18 AC3 (:148-151) observes exactly this listing, so it is green before the build run and cannot fail there. Its own fixture note admits the ask is filed by the spec run. | sound | - |
| 13 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-14.md:section 6 AC7 | low | low | confirmed | Unit 14 S5 (:66-69) places the owner-only rule on unit 13 S7's skip of payloads carrying agent_type, and adds no role check of its own. AC7 (:210-213) observes that same hook skip, which unit 13 AC5 (order 9) already guarantees before this unit (order 12). So this unit's change cannot turn AC7 red. | unsound | - |
| 14 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-16.md:section 4 Files touched, section 10 | low | low | confirmed | spec-16 line 161 says '`cmd_lists` grading the third list' and line 267 says 'which grades the third list'. spec-19 adds `unnamed-keys.txt` as the third list (S4, line 25: 'since this is the third') and calls unit 16's list 'the factory's fourth caller' (line 66). spec-16 line 48 also says 'never a fourth hand-rolled list'. Only the wording is wrong. | sound | - |
| 15 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-9.md:section 2 S4/S6 | low | medium | confirmed | spec-9 S4 (lines 54-55) names one exit-1 path: an owner-ceiling breach under `budgets.enforce`/`budgets.pinned` refuse prints `orient REFUSED`. S6 sends the breach through `check_cap`. AC5 (lines 194-198) plants only `budgets.orient-calls = 30` with the warn line, plus the missing-cap NOTE. No AC or plant sets enforce=refuse, so a build that ignores the switch passes every criterion. | sound | - |
| 16 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-14.md:section 4 "The window"; section 8 F2; S1 | blocker | blocker | confirmed | spec-14 line 125 pins `CONTEXT_WINDOW_TOKENS = 200000` and marks it UNVERIFIED. Line 127 says a larger window 'errs towards going fresh'. Its own goal (line 25) cites a compaction reading about 970k cached tokens. I ran a python probe over the 30 newest coding-governance transcripts. Main-session usages summed to at most 967091 tokens (claude-opus-5-5), and 27748 of 31116 main usages were above 200000. So on the main path the fill readout goes past 100%, and the 60% threshold fires at about 12% of the real window. | sound | - |
| 17 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md:section 2 S1, S2; section 4 Data model | high | high | confirmed | The v2 table rows (v2:1512-1515, 1638, 1657, 1668) read 'the role's effort', 'the role's model on that harness', 'the full safe set' and 'each cap's evidence-derived value'. The catalogue at 3c8c4718a has `default = {derived = ...}` for roles.effort.<role>, roles.effort.<workflow>.<stage>, roles.effort.default, roles.model.<role>.<harness>, maintain.fixes, review.<stage>, review.<stage>.effort and budgets.*. None of these is on v2's never list. S2's two rules, that every preset assigns every non-never row and that `standard` equals each row's literal default, cannot both hold for these rows. Prose such as "the role's effort" also fails the `name` item regex. I did not re-derive the 241/246 counts. | unsound | - |
| 18 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md:section 2 S1; section 4 Data model comment | low | low | confirmed | I numbered v2 lines 1418-1438 with awk. 1424 opens 'A pair rule binds two keys', 1430 opens 'Presets never touch the floor', and the list ends at 1437 with '`platforms.provision`:'. Lines 1434-1437 hold runtime.agents-in-flight, budgets.pinned, memory.mirror, the runtime harness/auth keys, roles.harness/auth.<role> and platforms.*. spec-1 cites v2:1420-1433 in S1 and v2:1427-1433 in the data-model comment (line 119), and both stop short of the list's end. | sound | - |
| 19 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-2.md:section 2 S2 Readers; section 6 AC6 | medium | medium | confirmed | `git show 3c8c4718a:tools/policy/policy.py` line 689-690 docstring: 'any `preset` the file names, which is not applied.'; README line 455: 'only `preset = "strict"` must read `warn` with the unapplied preset in its reason'. spec-2 S2 Readers lists policy.py :701-704/:708-709, check_policy.py :1662-1666, help/policy.md :57 and README :235, but not the docstring or README:455. AC6 greps 'not applied until dKeptSession', which neither stale text contains. The impact is stale docs, so it is contained. | sound | - |
| 20 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-4.md:section 2 S2; section 6 AC4 | medium | medium | confirmed | `git show 3c8c4718a:tools/policy/adopt-policy.sh` lines 99-103 run `policy.py scaffold` inside `{ ... } 2>/dev/null` and turn any failure into 'policy: the scaffold could not be written to $FILE' with exit 1. spec-4 S2 (lines 36-40) and AC4 (lines 144-146) require exit 2 naming `lax` and the four shipped presets. The Files-touched line for adopt-policy.sh names only '`--preset`, the kept-file line'. Nothing says the error path changes, so the wrapper as it stands swallows the refusal. AC4 would go red, so the gap would be caught. | sound | - |
| 21 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-9.md:section 2 S6 | medium | medium | confirmed | spec-9 S6 (lines 62-68) gives the row class, unit, enforcer, home and family only. `git show 3c8c4718a:tools/policy/budgets.py` sets FIELDS to include `research` (line 58) and requires SHIPPED (`kit`, `installed`) on any row with ships true (line 64). read_cap_census raises policy.Refusal on 'lacks ...' / '... ships and lacks ...', so the whole census refuses. check_policy.py line 712 adds 'has no budgets-cap-{name} case in CAP_CASES', and CAP_CASES sits at line 3487. spec-9's files touched (lines 144-148) leave out check_policy.py. The caps.toml header defines research as 'the caps research's row number', and orient-calls has none. | sound | - |
| 22 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-5.md:section 2 S9 | high | high | confirmed | spec-5 S9 (lines 89-95) has write_transition run bare `bash <prefix>/unattended/unattended.sh --mail read`. An absent driver passes with a NOTE, and a non-zero exit is not classed as fail-closed. I ran a probe from Windows python (scratch b.py): subprocess.run(['bash','-c','uname -a; pwd; ...']) printed 'Linux ... microsoft-standard-WSL2', pwd '/mnt/c/projects/...', and HAS_MNT_C. shutil.which('bash') named git-bash, and /c/Windows/System32/bash.exe exists. govkit.py:1144-1160 records the same measured failure and the gotcha subprocess-resolves-a-different-shell.md, and many kits carry resolve_bash. On this node the guard runs under WSL, so its outcome cannot be trusted. | sound | - |
| 23 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-10.md:section 2 S2, S6 | medium | medium | confirmed | spec-10 S2 (lines 36-38) runs bare `bash <kit>/unattended.sh --mail read <slug> --open` from position.py. S6 (lines 63-65) maps a non-zero read to `interrupt — mail · unarmed`, exit 0. My probe shows bare `bash` from a Windows python reaches WSL2 (uname printed microsoft-standard-WSL2), so on this node the read goes through the wrong shell and the boundary interrupt reads unarmed. The effect is that interrupts are not shown, and it is contained. | sound | - |
| 24 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-7.md:section 2 S1, S3, S4 | medium | medium | confirmed | spec-7 S1 (lines 39-40) runs bare `bash <kit>/unattended.sh --claims` from position.py, and that resolves to WSL, as my probe shows. An unreadable `--claims` reads `unreachable` and holds Build (line 186). S3/S4 (lines 54-67) hash `<file>`, a `git ls-tree -r` listing the tool derives, through derive_gov_id, which pipes raw bytes into `git hash-object --stdin` (spec-22 S1, line 30). Neither section says how the listing file is written. A Python text-mode write on Windows emits CRLF, so the poster's key and a Linux dependent's key would differ. | sound | - |
| 25 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-27.md:section 2 S3, S5 | high | - | refuted | duplicate of id=24. In the spec set, unit 7 is the only caller of `--interface` and check_interface_notice (grep finds only spec-7 and spec-27). Its `<file>` is a generated `git ls-tree -r <w>` listing (spec-7 lines 56-57), not a checked-out tracked file. Its bytes are blob ids and paths, which do not depend on core.autocrlf checkout conversion, so the 176 w/crlf working-copy files never feed the key. What is left is how that listing file is written (CRLF from a Windows text-mode write), and id=24 already covers it. | sound | - |
| 26 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-12.md:section 2 S1, S2 | high | high | confirmed | spec-12 S1 stamps the verdict with the version derive_cli_line reads from AI_AGENT, or `unknown`. S2 passes only when that version equals AI_AGENT's now. On this node `echo $AI_AGENT` printed claude-code_2-1-308_agent, while PATH's /c/Users/daily-agent/.local/bin/claude --version printed '2.1.292 (Claude Code)'. manifest-check.sh:405-420 exists to compare exactly these two. A fixture that drives a compaction through PATH's claude would therefore record a pass for 2.1.292 under 2.1.308. From a terminal with no AI_AGENT, the stamp is `unknown`, which never matches inside a session. The fixture file is not in this tree, so I could not read which binary it launches. The spec still keys the verdict to a binary it does not tie to the one that ran. | sound | - |
| 27 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-21.md:section 2 S5; section 4 'The tool call, in order' and its cost paragraph | medium | medium | confirmed | Spec-21 S5 (:73) says the hook 'spawns no git', and §4 (:150-155) has step 2 call readPolicy('mailbox.notice') on every call, before the stamp is read, and says 'The hook's whole cost is file reads'. `git show 3c8c4718a:tools/policy/policy-mirror.js` shows readPolicy (:132) calls runGit rev-parse --show-toplevel, then readLandedRevision -> runShim (bash, after resolveBash runs its candidates), then readMirrorAt -> runGit cat-file blob and cat-file --batch-check. A stale mirror adds runReader, another shim run. So every call pays those spawns even under the default every-item. AC (:253-255) only greps mail-notice.js for execFileSync/spawnSync, so it cannot see spawns made inside readPolicy. I did not re-time the four spawns. | unsound | - |
| 28 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-21.md:section 8 F1 | low | - | refuted | duplicate of id=37. I re-ran the grep over /c/Users/daily-agent/.local/bin/claude.exe (claude --version 2.1.292, not the 2.1.308 that spec-21 F1 cites). It printed 33 lines, hookEvent counts PreToolUse 1 and PostToolUse 5, and the PreToolUse builder `rn({type:"hook_additional_context",...,hookName:`PreToolUse:${n.name}`,...,hookEvent:"PreToolUse"})`. So F1's 'no such builder was seen naming PreToolUse' is false. id=37 reports the same false observation and its cross-spec consequence. | sound | - |
| 29 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-8.md:section 2 S1; section 6 AC8 | medium | - | refuted | duplicate of id=34. I confirmed the same facts there: 3c8c4718a catalogue.toml:223-226 holds actions.free with owner dKeptSession and default read-only-probes, and unsummarised-keys.txt:5 lists it. Spec-8 S1 (:32-36) still creates the row through `core.py new policy-key`, and AC8 (:207) reads r[0] of the standing row. | sound | - |
| 30 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-11.md:section 2 S1; section 6 AC6 | medium | - | refuted | duplicate of id=34. catalogue.toml:543-546 at 3c8c4718a holds notify.owner with owner dKeptSession and default turn-micro-formats, and unsummarised-keys.txt:142 lists it. Spec-11 S1 (:34-37) creates it through new policy-key, and AC6 (:170) reads the standing row. | sound | - |
| 31 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-17.md:section 2 S1 | medium | - | refuted | duplicate of id=34. catalogue.toml:60-63 at 3c8c4718a holds attendance with the same allowed set, default unattended and owner dKeptSession, and unsummarised-keys.txt:11 lists it. Spec-17 S1 (:34-38) creates it through new policy-key, and AC7 (:203) reads the standing row. | sound | - |
| 32 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-5.md:section 2 S12; section 4 Files touched | high | high | confirmed | Spec-5 S12 (:107-111) adds a factory row and names its files `-mailbox-message-<n>.md`, but serves them as `**Serves:** journal <anchor id>`. Its Files touched (:237) names only build_records.py, with no tree_lib.py TYPED_RECORD_KINDS or HYGIENE kind-list edit. PLAY-dOrderedCharter-42 at origin/main has two rules this breaks. S2: the factory's per-kind table is refused at import when its keys differ from TYPED_RECORD_KINDS. S3: a `-<kind>-<n>.md` file whose Serves kind is not <kind> is malformed. Sibling kits do the opposite: TOOL-dDeclaredLoop-16 and -17 add disposition and acceptance to TYPED_RECORD_KINDS, and -17's AC is red when the record 'serves as journal'. Built as written, either every factory import fails or the AC6 records are malformed. | sound | - |
| 33 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-10.md:section 2 S2; section 8 F2; section 6 AC1 | high | medium | confirmed | TOOL-dDeclaredLoop-7 S4 (origin/main :51-55) puts mailbox messages in the engine's ordered interrupts, 'printed unarmed until dWellOiledMachine lands the mailbox'. Spec-10 adds a separate reader, read_mail_interrupts behind --mail-interrupts (S2 :36-46), and says derive_position and every other engine call 'print no mail line'. AC1 (:166-171) requires the plain engine call to print no `interrupt — mail` line. The spec never says what happens to the parent's S4 mail slot in derive_interrupts. F3's ask (:221-228) only renames the armer. So the parent's unarmed line is either left in place after the mailbox lands, or removed without the parent's text authorising it. position.py is unbuilt at origin/main, so this is a contradiction between the specs. | unsound | - |
| 34 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-8.md:section 2 S1; section 6 AC8 (same defect in KICK-dKeptSession-11 S1/AC6 and KICK-dKeptSession-17 S1/AC7) | medium | medium | confirmed | `git show 3c8c4718a:tools/policy/catalogue.toml` has three rows, each owner dKeptSession: actions.free at :223-226 (default read-only-probes), notify.owner at :543-546 (default turn-micro-formats) and attendance at :60-63 (default unattended). 3c8c4718a is an ancestor of branch/unattended-dgroundrules-e47ae1. unsummarised-keys.txt lists all three keys (lines 5, 142, 11). Spec-8 S1, spec-11 S1 and spec-17 S1 each still create their row through `core.py new policy-key`. Their ACs (8:207, 11:170, 17:203) print r[0]['owner'], r[0]['default'] of the row that already stands, so that part is green before the units are built. By contrast, spec-13 S5 (:60-67) uses 'only where the landed catalogue lacks the row', and spec-7:93 and spec-21:104 say 'No catalogue rows'. | sound | - |
| 35 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-7.md:section 2 S4; section 4 'The notices' and Inventory (`read_dependents`); section 10 | medium | medium | confirmed | Spec-7 §4 (:141-142) reads dependents from every memory/builds/*/README.md front matter's parents:, and the Inventory mints read_dependents in tools/loop/position.py. The memory-tree kit already inverts parents: into children: gen_build_index.py:2625 `children.setdefault(p, []).append(b["slug"])`, and :2623 refuses a parent that is not a build folder. Spec-7 §10 cites only a reuse_lookup on 'dependency gate' and a recall query. It does not cite this derivation. The result is a second reader of one edge. | sound | - |
| 36 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-12.md:section 2 S5 (I10); section 6 AC6 | medium | medium | confirmed | PLAY-dOrderedCharter-4 'The replay' (:122-126) decides that print_replay prints derive_map_block first, then the stored card, then now —, so the 10,000-character cap cuts a card's tail and never the map. Spec-12 S5 (:57-62) gives the order as the stored card, then now —, then the computed lines, with no map, and makes the order of calls in print_replay, with an I10 comment, 'its one statement'. AC6 (:194-196) checks only now —, card —, route —, resume — and partial —. `grep -rn 'derive_map_block\\|map —'` over the dKeptSession spec folder printed nothing. | sound | - |
| 37 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-21.md:section 8 F1 (FACT-QUESTION); section 2 S5 | medium | medium | confirmed | I re-ran the grep over the installed claude.exe (2.1.292). It printed the PreToolUse hook_additional_context builder (hookEvent counts: PreToolUse 1, PostToolUse 5), so spec-21 F1's 'no such builder was seen naming PreToolUse' (:282-283) is false. It also cites version 2.1.308, while the installed CLI is 2.1.292. Spec-14 F1 (:232-237) observed that PreToolUse carries additionalContext. Spec-13 F1 (:277-283) rejected a new PostToolUse fragment because it 'adds a third hook registration... for the same reading'. Spec-21 adds exactly that registration (mail-notice.js plus its fragment), on the false negative. The two specs give opposite answers to one platform fact. | sound | - |
| 38 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-11.md:section 2 S2, S6; section 10 | medium | - | refuted | I read coding-governance-agents.template.md:57-80. `BUILD — <slug> · Tier-<n> · <done>/<total> <step> · left <ids>` is a progress-count state line, and it is not among the [events] rule's shapes. Spec-11's `progress — <slug> · <event> · <detail>` is an event notice (park, landing, transition), and §5 has it graded by check-microformats.sh. The two shapes share no field that could disagree, and format-guard's BUILD arms (format-guard.test.sh:176-200) check BUILD's own left cell. Choosing to merge the event into BUILD is a preference, and the finding names no defect the rubric grades. | none | - |
| 39 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-20.md:section 2 S5; section 4 'The order a build's read takes' | medium | - | refuted | TOOL-dDeclaredLoop-27 S7/S8 (origin/main :76-84) settle and record conflicts where two scenarios set 'one field of one row', and scenario-settled is written as <row tag>:<field>:<winner>:<loser>. Spec-20's slot (S4/S5 :50-58, §4 :82-92) is this unit's new overrides/preset slot, not a row field. So the transition record holds no slot settlement that a read could re-decide or contradict, and the 'second settlement of one conflict' premise does not hold. The finder's own fix concedes that slots may lie outside S7's rule. The leftover concern, that the slot is settled at read time under the live flow.scenario-conflict, is not established as a defect. The finder graded it medium. | none | - |
| 40 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-13.md:section 8 F3; section 2 S3 | medium | medium | confirmed | spec-13:294-295 resolves F3 on 'the kinds are a closed set of five (`tree_lib.py:406`)'. tree_lib.py:406 does hold five today. But PLAY-dOrderedCharter-42.md:94-95, on origin/main and HEAD, redefines it as `RECORD_KIND_TOKENS = ("spec-audit","diff-review","journal","research") + TYPED_RECORD_KINDS`, with four typed kinds. A git grep of node:record-kind.* under memory/builds lists many more typed kinds: acceptance, commit, disposition, exception, override, mailbox-message, lease, probe and others. So the stated basis for F3 does not hold. AC6 (spec-13:244) refuses the whole pointers section once the card passes CARD_CAP_BYTES, which makes the effect real but contained. | sound | - |
| 41 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-14.md:section 2 S6; section 6 AC1; section 4 Inventory | low | low | confirmed | spec-14:73 (S6) and :153 add a standalone `tools/runlog/fixtures/context-fill.jsonl`, and AC1 (:187-190) runs `runlog.py context` over it. transcripts.json already holds a `usage` scenario. Its about text says each scenario's main and agents files are written into a scratch projects root by the self-test. AC1 also needs 'a later subagent usage' inside one bare jsonl, which the scenario store already models as separate `agents` files. The cost is a duplicated fixture format, which is maintenance only. | sound | - |
| 42 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-9.md:section 2 S2, S4; section 4 Inventory; section 10 | low | low | confirmed | spec-9:39 defines a per-row four-field `tokens` sum, and :50 and :167 print per-stage quartiles. A grep of spec-9 finds no `_derive_quartiles`. runlog.py:210 defines `_derive_quartiles`, and :226 already computes `r["in"] + r["out"] + r["cache_read"] + r["cache_write"]` in print_ready. Section 10 (:248) names print_ready only as where the mode sits. The method could diverge between the two reports, a contained effect. | sound | - |
| 43 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-20.md:section 2 S2 (with KICK-dKeptSession-1 section 4 Inventory) | low | low | confirmed | The spec-1 inventory (:184) lists load_presets, derive_preset_assignment, check_presets, check_repo_presets, load_preset and write_preset, with no pair-rule function. The repository pair rule is described in prose at :174-177. spec-20 S2 (:36-41) judges 'the pair rules hold over the slot's assignment' in check_scenario_policy and names no shared function, so a third evaluation is the likely build. The drift risk is real but narrow. | sound | - |
| 44 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-16.md:section 4 Files touched; section 10 | low | low | confirmed | spec-16:161 says '`cmd_lists` grading the third list', and :267 says 'grades the third'. spec-19:66 calls spec 16's list 'the factory's fourth caller', and spec-19:128 has cmd_lists reading the third list, which is its own `unnamed-keys.txt`. The ordinal is wrong in spec 16, a cosmetic error. | sound | - |
| 45 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-8.md:section 2 S1, section 4 Files touched, section 6 AC8 (same defect in KICK-dKeptSession-11 S1/AC6 and KICK-dKeptSession-17 S1/AC7) | high | high | confirmed | spec-8:34, spec-11:36 and spec-17:36 each run `core.py new policy-key <name>` unconditionally. spec-13:63-67 conditions the same call 'only where the landed catalogue lacks the row'. On branch/unattended-dgroundrules-e47ae1 the catalogue.toml already holds `attendance` (:60, default unattended, owner dKeptSession), `actions.free` (:223, default read-only-probes, owner dKeptSession) and `notify.owner` (:543, default turn-micro-formats, owner dKeptSession). AC8, AC6 and AC7 read `r[0]` owner and default, so they would print the expected values before the unit runs, and they cannot fail on the row part. An unconditional factory call would also add a duplicate row or red the wrapped check. | sound | - |
| 46 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-9.md:section 2 S6, section 4 Files touched | high | medium | confirmed | spec-9:62-64 S6 gives the orient-calls row class, unit, enforcer, home and family only. In budgets.py on the dGroundRules branch, FIELDS at :58 includes `research` and OPTIONAL is {"ships": True}. SHIPPED (kit, installed) is required when ships is true (:135). read_cap_census raises Refusal with 'lacks ...' (:136-147). resolve_caps calls read_cap_census first, outside its try (:216), so every cap resolution would refuse with exit 2. The caps.toml header documents research, kit and installed as required. I grade it medium rather than high because the census arm and the per-row fixtures would red before landing, which contains the failure. | sound | - |
| 47 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-2.md:section 3 Non-goals (the JS mirror bullet), section 4 Files touched (same omission in KICK-dKeptSession-20 S4) | high | high | confirmed | In policy.py on the dGroundRules branch, :809-813 reads 'A unit adding a resolution input adds its path here' with `LEGACY_INPUTS = (LEGACY_FANOUT,)`. render_mirror (:881-882) records only catalogue_blob, legacy_blobs and policy_blob. spec-2:67-68 claims the mirror 'carries the preset's values without an edit' and adds no LEGACY_INPUTS entry, so a change to presets.toml leaves the mirror's recorded ids unchanged and it reads as fresh. The spec-20 half does not hold. spec-20:47-49 has read_scenario_value answer None with no build, and :66 says policy.json is rendered per revision and never per build, so the mirror never reads a scenario input. | unsound | - |
| 48 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-5.md:section 4 Files touched and section 7 (same omission in KICK-dKeptSession-6, -7, -11, -21, -22, -24, -25, -27 and -28, every unit adding refusals to tools/unattended/unattended.sh) | medium | medium | confirmed | .memory-tree.conf:641-649 sets `REFUSAL_CEILINGS="tools/unattended/unattended.sh:323:2026-10-22:TOOL-dTrueNorth-28 ..."`, raised to the census. Raising it again takes the retirement review with a dated decision id. A grep for REFUSAL_CEILINGS, ARMS_FLOORS, check-arms or 'harness arms' across the specs matched none of them; the only hits are the word 'census' in unrelated senses, in specs 9, 20 and 23. 17 specs touch unattended.sh, and the mail units add refusal sites, so the leg reds or the ceiling is raised without its review. | sound | - |
| 49 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-12.md:section 4 Files touched (same omission in -5, -10, -13, -14, -15, -21 and -26, which edit manifest-check.sh; -1, which edits tools/gate-legs.json; and -3 and -11, which edit coding-governance-agents.template.md) | medium | medium | confirmed | memory/guides/SESSION-KICKOFF.md:6 `watch:` includes tools/gate-legs.json, skills/session-kickoff/manifest-check.sh and coding-governance-agents.template.md. git log shows the prior re-stamps 6d2ed123a and e634ce986. A grep across the specs and the build README for 'kickoff-manifest ratchet', SESSION-KICKOFF, last-audit or re-stamp matched nothing. The ratchet leg (gate-legs.json:3) runs manifest-check.sh, so each pass that edits a watched file owes a write that no spec declares. | sound | - |
| 50 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-21.md:section 4 Files touched (and every spec minting a shell, Python or JS function under tools/ or skills/) | medium | medium | confirmed | map_extractors.py:203-206 derives `harness-hooks` from .claude/settings.json. spec-21:191 adds the PostToolUse mail-notice entry to .claude/settings.json. memory/map/features/unattended.md:14 claims only gate-guard, stop-guard and stall-recorder. memory/map/generated/ holds symbols.json, inventories.json, MAP.md and CARDS.md. No spec names memory/map, a dossier or gen_map, and the build README declares no shared render for them. | sound | - |
| 51 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-12.md:section 2 S1-S3, section 4 Files touched / Migration | medium | medium | confirmed | tools/govkit/entries/kickoff-manifest.kit.toml is `kind = "flat"` with explicit [[files]]: manifest-check.sh, manifest-check.test.sh, MANIFEST-TEMPLATE.md, the two fragments and so on, and no card-compaction.fixture.sh. PLAY-dOrderedCharter-8:199 adds the fixture as new and touches no kit.toml. spec-12 S2 (:41-46) answers 'no fixture installed' as red. spec-12 F1 (:213-215) chose (b) on the grounds that it 'holds in an adopter', which is false when the fixture is not shipped: always-resume is permanently read as fresh-when-idle in adopters. | sound | - |
| 52 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-28.md:section 2 S3, section 4 Files touched | medium | medium | confirmed | tools/unattended/kit.toml:12 has `requires = ["memory-tree", "review-harness", "settings-merge", "kickoff-manifest"]`, and tools/playbook/kit.toml:7 has id playbook-render. spec-28 S3 (:39-43) makes check_mail_recipient run render_playbook.py --fleet-tags. A grep found no current playbook reference in unattended.sh, so this is a new cross-kit edge. The files touched (:99-103) do not include tools/unattended/kit.toml. An install of unattended without playbook-render refuses every node: recipient. | sound | - |
| 53 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-6.md:section 4 Files touched (same line in KICK-dKeptSession-7, -21, -24 and -25) | low | low | confirmed | grep -n subject-pins prints the line 'tools/govkit/subject-pins.tsv, regenerated by ... selfcheck --write' at -21.md:199, -24.md:151, -25.md:162, -6.md:111 and -7.md:170. None of those five specs mentions gate-legs.json. govkit.py:2968-2975 builds `live` and `body` from `manifest` only, one row per leg. Spec -5.md:357-360 rev-1 gives exactly that reason for leaving the file out. So the five specs declare a write that is a no-op and contradict their sibling. The only effect is on the declared write set and the prose. | sound | - |
| 54 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-22.md:section 2 S2 (with KICK-dKeptSession-7 section 2 S4, S5 and KICK-dKeptSession-27 S3) | blocker | blocker | confirmed | spec-22.md:35-37: the id hashes six fields (build, item, pass, kind, subject, answers) and takes no session and no time. spec-5.md:65 calls it with the sender's slug. spec-7.md S4 posts one `confirmed` per dependent, to `build:<dependent>`, with subject `interfaces <slug>` (the parent's slug) and no --item or --pass. S5 posts `landed` per dependent with subject `landing <slug>`. spec-27.md S3 adds content-key as a record key, not an id field. So two dependents get the same id. check_mail_duplicate (spec-22 S3) runs over the sender's refs and refuses the second post with rc 1. Every later `changed` collides with the first `changed`. spec-22.md:120-121 says equal fields are one message by design. The README (line 30) names two child builds of dKeptSession, so this is the main path, and S5's 'never fails the verb' hides the refusal. | sound | - |
| 55 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-5.md:section 2 S7 and S9 (with KICK-dKeptSession-7 S4, S5 and KICK-dKeptSession-24 §8 F2) | high | high | confirmed | spec-5.md S7 (80-82): every row except `answer` and `ack` stays `open` until answered or acked. S9 (89-95) refuses a transition while open rows addressed to the build exist. spec-7 S4 and S5 post `confirmed`, `changed` and `landed` to `build:<dependent>`. A grep for '--mail ack' and 'acknowledg' over the specs finds only spec-5's own verb and AC, spec-21's non-goal and spec-24's deadline text. No unit acks a notice. spec-24 F2 relies on the 72 h deadline for exactly 'a changed nobody acknowledges', so each notice holds the dependent's transitions until the ceiling passes. | unsound | - |
| 56 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-5.md:section 2 S5, S7 and S8 (with KICK-dKeptSession-25 S2) | high | medium | confirmed | spec-5.md S3 refuses only a kind outside the closed set, and `answer` and `ack` are in it. S5's post takes --kind and --answers with no check of the answered row. S7 counts any cached `answer` or `ack` that names an id, whoever sent it. Only S8's `--mail ack` checks that the id is addressed to <slug>, and unit 25 S2 puts the open-question and cite checks only in `--mail answer`. So `--mail post --kind ack` or `--kind answer` bypasses both checks. The effect stays inside the cooperating sessions' mailbox. | sound | - |
| 57 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-8.md:section 2 S3 and S7 (against KICK-dKeptSession-13 S2) | high | high | confirmed | spec-8.md S3 (43-49) reads the `item —` line as 'an instance key, or `none`'. S7 (68-70) lists three unarmed cases: no session card, no routed build, no `## pointers`. It also says 'once armed, a throw anywhere in the arm refuses'. spec-13.md S2 (39-44) prints `skipped: <why>` on the item line when position.py does not resolve. spec-8 does not mention `skipped` anywhere. So with the loop kit absent, the arm either reads skipped as a key and admits everything, or throws and refuses every write. | sound | - |
| 58 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-12.md:section 2 S1 and S2 | high | high | confirmed | Re-probed. `command -v claude` printed /c/Users/daily-agent/.local/bin/claude. `claude --version` printed 2.1.292. AI_AGENT=claude-code_2-1-308_agent. spec-12 S1 records `cli <version>` from AI_AGENT, else `unknown`, and S2 passes when that equals the AI_AGENT version now. The dOrderedCharter-8 fixture (165-176) runs `claude -p` from PATH, which is a different binary from the one recorded. unknown==unknown also compares equal. So the always-resume switch is armed by a test of the PATH binary, while the session harness itself is never tested. | sound | - |
| 59 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-5.md:section 2 S9 | medium | medium | confirmed | spec-5.md S9 (89-95) covers open rows (exit 1), `mail — off`, an absent driver, zero rows (pass) and a timeout (exit 2). It does not cover a read that exits non-zero with no rows, and a builder would read that as zero rows. spec-10.md S6 (63-65) does handle the same read 'exiting non-zero'. So the guard fails open on a crash. | sound | - |
| 60 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-5.md:section 2 S5 | medium | medium | confirmed | spec-5.md S5 (62-68) runs one bounded fetch, then add_feed_sightings, then the id and check_mail_duplicate, with no branch for a failed or timed-out fetch. The only failed-fetch text (S6 line 77, AC line 296) is the reader's. spec-22.md:43 says the check reads the cache only and its caller fetches first. read_claims at unattended.sh:2136-2147 turns a fetch failure into CL_WHY and a refusal, a branch S5 does not copy. So a stale cache can let a retry write a duplicate. | sound | - |
| 61 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-21.md:section 2 S6 and section 6 AC5 | medium | medium | confirmed | spec-21.md S6 (76-80) spawns bash detached, with streams ignored and unref'd, and sets no windowsHide. On win32 a detached console child gets its own console window. `git grep windowsHide` prints only format-guard.js:248 and stop-guard.js:113, and the tree has no detached-spawn precedent. AC5 (250-255) greps only 'execFileSync\|spawnSync', so an async spawn('git') or execSync passes it. | sound | - |
| 62 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md:section 2 S3 (and KICK-dKeptSession-2 S1's use of derive_preset_assignment) | medium | medium | confirmed | spec-1.md S3 (53-60) lets a repository declare `[presets.<name>]` and does not forbid a shipped name. The text at 169-172 resolves 'a shipped name' to the shipped table, so a declared `[presets.strict]` is silently ignored. Neither the specs nor AC5 (262-266, which plants extends=lax and a never key) address a declared name that shadows a shipped one. | sound | - |
| 63 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-11.md:section 2 S5 | medium | medium | confirmed | spec-11.md S5 (49-55): emit_progress runs S3's Python verb from verb_park and verb_landed. Its only stated failure is 'loop kit unresolved prints nothing', and it states no time bound and no rule for a non-zero exit or a hang. unattended.sh:57 is `set -u` only, so a hung child blocks the verb. REMOTE_BOUND (line 162) is the existing bound pattern. spec-7 S5 states 'never fails the verb' for its own notice, but S5 here does not. The effect is limited to the two verbs. | sound | - |
