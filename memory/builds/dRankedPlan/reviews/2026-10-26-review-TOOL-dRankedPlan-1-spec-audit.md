**Serves:** spec-audit TOOL-dRankedPlan-16@rev-1 TOOL-dRankedPlan-1@rev-1 TOOL-dRankedPlan-9@rev-1 TOOL-dRankedPlan-10@rev-1 TOOL-dRankedPlan-2@rev-1 TOOL-dRankedPlan-14@rev-1 TOOL-dRankedPlan-13@rev-1 TOOL-dRankedPlan-11@rev-1 TOOL-dRankedPlan-12@rev-1 TOOL-dRankedPlan-3@rev-1 TOOL-dRankedPlan-4@rev-1 TOOL-dRankedPlan-5@rev-1 TOOL-dRankedPlan-15@rev-1 TOOL-dRankedPlan-6@rev-1 TOOL-dRankedPlan-8@rev-1 TOOL-dRankedPlan-7@rev-1

# Tier-2 spec audit — dRankedPlan, the sixteen unit specs (round 1)

Provenance: Tier-2 adversarial review of the dRankedPlan spec run. The finders were gov-spec-reviewer on five lenses, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer. The build's purpose is read from memory/builds/dRankedPlan/README.md and its run mandate.

Reviewed: memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md@e03567df0052a114734a096bed5606b31ce8b975, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-1.md@e51ec128743f20548506eca5653c56d4361c0d87, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-9.md@52ea63d7dabce7944df442c1983be17689fbfbf7, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-10.md@47d794d3eac05364d814e1a953258dbf687025c0, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-2.md@1d7537928f3bfb4fe3c8ba9b83f7f39910f0bff7, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-14.md@af45256b7ef263588d5ed27de10af9e246bd1015, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-13.md@2b538bc2e90066e1a93389ca2a78b3a3bcf06ce4, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-11.md@3bd9b9f2a7c1fcfebcf169eaeecf5de55332827e, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-12.md@065bee90e0177a2893743ace265d87d93bb616cd, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-3.md@2f16657771aeae01b66fadb1a845fe168dacf85f, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-4.md@afb76f1de9a3d7a83a866dcac99cd7d22936689c, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-5.md@6753cb220d1f613a96fe57a2e7f021b60f803a3c, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-15.md@692bf3cce8b3a51d407c3deb487544e4e0b56bec, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-6.md@a647d48194829b41f633d1511c3f4ba4947e5def, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-8.md@5534d7813c36ca184108285bb41f98de0449bf5c, memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-7.md@21d368dde96e44baa3caf8274ba9206ad251ebef

ROUND: 1

## Verdict: BLOCKED

One blocker stands: the specs say `plan.exit` needs every reached item's witness, and no unit builds that rule (item B1). Nine high findings in seven items also stand. Two of them (items H5 and H6) would stop their units at the bar as written.

## Review shape

Review shape: intensity full, raw 49, confirmed 49, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 12 | 12 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 10 | 10 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |

The adjudicated tally by item is 40 items: 1 blocker, 7 high, 20 medium and 12 low.

The tally by raw confirmed finding is 49: 1 blocker, 9 high, 27 medium and 12 low.

Merges join findings of one binding grade only. Findings 4 (high) and 38 (medium) describe one defect at two binding grades, so they stay in separate items that cross-reference each other.

### Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified.
- Discards: 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 47 judged sound, 2 judged UNSOUND (ids 22 and 25, whose skeptic-corrected fixes are written below), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic, 3 RE-GRADED by the skeptic (ids 2, 22 and 23).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 1 spec document was supplied as `specs`, as sibling context.
- Checklist: NONE swept, because it is absent. A zero count is not evidence that the project's recurring bug classes are absent.
- By design: none supplied, with no caller byDesign and no block.
- Move check: no checked subject moved.

Every count above is clean, so the run is complete on its own terms. The missing checklist sweep is the one gap in coverage.

## Blocker

### B1 — `plan.exit` is said to need every reached item's witness, and no unit builds that rule (id 1)

- **Where:** TOOL-dRankedPlan-12 §2 S5, §8 F2 and §6 AC5. TOOL-dRankedPlan-13 §2 S9. TOOL-dRankedPlan-10 §2 S4/S5.
- **What:** Units 12 and 13 say `plan.exit` cannot pass while an owed probe is open or a field check refuses, because "plan.exit needs every reached item's witness". Unit 10 owns `item.plan.exit`. Its `check_plan_exit` admits the move on the ratification answer, on the pre-placement exemption or on a disposition record. It never reads `item.plan.record`'s witness (`check_plan_record`). No other unit builds the rule.
- **Consequence:** A build crosses into Design with unreturned owed probes, a mismatched `Affected systems` value or an over-budget read set. AC5's red-when names `plan.exit`, but AC5 only runs the schema check. The criterion therefore certifies a gate that nothing implements.
- **Fix (skeptic judged it SOUND):** Pick one owner for the rule. One option is that unit 10 S4's `check_plan_exit` also requires `plan_record.py check <slug>` to print `witnessed` (or reads every reached Plan item's witness through `read_plan_item_witness`) before it admits the move. The other option is that units 12 and 13 drop the plan.exit claim and their clauses name another gate. Either way, add a criterion that drives the real move: `loop_transition.py record --item item.plan.exit` is refused with exit 1 over a plan record with an open owed probe, and admitted once the probe returns.
- **Left-shift gate:** A spec-audit check that every "X cannot pass while Y" claim names the unit and function that enforces it. Also require each AC whose red-when names a transition to run that transition.

## High

### H1 — `Scenario: none` on patch and repeat plan records is read as a re-pick, so their step transitions are refused (id 2)

- **Where:** TOOL-dRankedPlan-14 §2 S1/S2 and §8 F3, with TOOL-dRankedPlan-16 §2 S8 and AC8.
- **What:** Unit 16 S8 writes every patch or repeat build's plan record with `Scenario: none`. Unit 14 S1 takes only an absent, empty or pin-equal `Scenario` as the pin, so it reads `none` as a re-pick of `scenario.none`. S2 refuses that re-pick, and S3 runs the check on every transition into a step. The pin is "the first transition record into planning", which a patch build never makes.
- **Consequence:** Once unit 14 lands, every patch or repeat build that `--placed-build` opens is refused at each step transition, and its pin is undefined.
- **Grade note:** The finder graded this blocker. The skeptic re-graded it high because it blocks work rather than shipping a wrong result. The binding grade is high.
- **Fix (skeptic judged it SOUND):** In unit 14 S1, read `none` as absent, as S1 already does for `Scenario reason`. Define the pin for a build that has no `planning` transition as its first transition record. Add a plant `plan-patch` with a unit-16 S8 record whose step transition is admitted. The alternative is that unit 16 S8 leaves `Scenario` absent and §8 F3 says so.
- **Left-shift gate:** A cross-unit fixture arm: each writer's canonical output, here unit 16 S8's patch record, is fed to every reader unit's check.

### H2 — Unit 2 judges row ratification through a session-scoped predicate, so other sessions can reorder ratified rows (ids 3, 37)

- **Where:** TOOL-dRankedPlan-2 §2 S3, §4 "The authority" and §8 F5. The predicate is TOOL-dRankedPlan-9 §2 S2.
- **What:** S3 counts a row as ratified only while `read_plan_ratification` answers a witness, and the S4 pre-commit hook evaluates this at commit time. Under the default `plan.ratification: request`, the witness exists only when this session's id is a line of the request's node-local `.typed` file. Under unit 10's fallback, the only live path until dWellOiledMachine lands, the owner ratifies by a disposition record, and the predicate never reads that record.
- **Consequence:** In a later session, an unattended run or on another node, every row reads unratified. Under the default `planner-drafts-owner-ratifies`, an agent commit there may reorder builds the owner ratified, and the hook admits it. AC3 uses a stub predicate, so no criterion tests across sessions.
- **Fix (skeptic judged it SOUND for both findings):** Make "ratified" a durable fact rather than a re-evaluated session predicate. For example, a row is ratified once its build has crossed `plan.exit`: read the `ratification=<how>` field unit 10 writes on that transition's trailer, or the disposition unit 10 S4 accepts. Another option is a ratification record written once while the witness holds. Add a plant: `dA` and `dB` are ratified in session S1, then an agent commit in session S2 (with no `.typed` line) reorders them, and the commit must exit 1.
- **Left-shift gate:** A checklist entry: a commit-time or later guard must never call a session-scoped consent predicate. Back it with a cross-session plant in every ratification-reading arm.

### H3 — Unit 15's `show` and the gate that releases the second `plan.exit` give different ratification answers (id 4)

- **Where:** TOOL-dRankedPlan-15 §2 S5 and §8 F3.
- **What:** `show` judges a revision's ratification by calling `read_plan_ratification` afresh. The gate that actually releases the second `plan.exit` is unit 10's `check_plan_exit`, which can admit on `intake-not-installed`, `disposition` or `before-placement`, none of which the predicate counts. F3's "under request the standing request ratifies the revision" holds only in the typing session.
- **Consequence:** A revision whose exit the owner legitimately released through the fallback still makes `show` exit 1 with "design re-entered without ratification", and that line is what Design receives. Conversely, `show` can print "ratified" for an exit the gate released on something else.
- **Fix (skeptic judged it SOUND):** S5 reads the `ratification=` field unit 10 writes on the re-entry move's trailer (`witness`, `intake-not-installed`, `disposition` or `before-placement`). Add a plant where the fallback is released by a disposition record with no typed request, and observe `show` printing `ratified`.
- **Related:** Item M17 (id 38, medium) is the cross-session face of the same defect. Both close with this one fix.
- **Left-shift gate:** Any surface that reports how a gate was passed must read the gate's own record of that, never re-ask the gate's inputs. Enforce it with a plant where the inputs have since changed.

### H4 — A disposition from an earlier crossing releases a later `plan.exit` (ids 5, 21, 39)

- **Where:** TOOL-dRankedPlan-10 §2 S4 and §3 last bullet. TOOL-dRankedPlan-9 §2 S4 (`terminal-command`). TOOL-dRankedPlan-15 §2 S5 and flow step 5.
- **What:** Unit 10 S4 admits Plan's exit on any disposition record that names `item.plan.exit` and that `check_disposition_record` admits, with no freshness bound. §3 says a revised plan "crosses plan.exit again through S4 unchanged". Unit 9 S4 has the same unbounded lookup under `terminal-command`. Units 9 and 10 each re-derive the lookup, and neither applies the "added after its newest transition" rule unit 4 S3 applies to the same records. Finding 39 also raised a second half: a record whose Disposition is `ask` or `none` may release the gate. The skeptic did not establish that half, because item.plan.exit's outcome set is unconfirmed.
- **Consequence:** After unit 15's B6 move back to `planning`, the first exit's disposition record is still in `build/`, and it releases the second exit. The revised plan re-enters Design with no new owner act. That breaks I20 / clause 0497 ("ratified as the plan is") and FR-1/FL-P6. It applies under the `request` fallback (every `request` build until dWellOiledMachine lands) and under `terminal-command`.
- **Fix (skeptic judged it SOUND for all three findings):** Spec ONE reader of a build's disposition records by item in the loop kit, minted by unit 9 (order 3). For example, `read_item_disposition(repo, slug, item)` returns only records added after the build's newest transition into the item's step, read through `read_transitions`. Unit 10 S4, unit 9 S4 and unit 4's `read_build_disposition` (order 11) all call it. Require a releasing Disposition word: `ask` and `none` keep the gate shut. Add plants under `request`-fallback, `terminal-command` and `codex-adapter`: first exit disposed, B6 back to planning, then a second `plan.exit` move with no new record exits 1, and is admitted once a new disposition record is committed.
- **Left-shift gate:** A checklist entry: every evidence-record lookup that releases a re-enterable gate is bounded to the current crossing. Back it with a re-entry plant in each such gate's arm.

### H5 — gov-spec-writer gains `plan:` reads keys that the roles vocabulary refuses (id 27)

- **Where:** TOOL-dRankedPlan-16 §2 S7 and §4 Files touched.
- **What:** S7 adds `plan:goal?, plan:acceptance?, plan:non-goals?` to gov-spec-writer's `reads:`. `READ_KEYS` in tools/roles/roles_lib.py is a closed set with no `plan:` family. Files touched omits roles_lib.py and the generated `gen:roles-catalogue` region of tools/roles/README.md.
- **Consequence:** check_roles.py rule R3 refuses the agent file ("reads key 'plan:goal?' is outside the vocabulary"). The `roles catalogue` leg, which the spec's own §7 names, goes red on the first pass, and the README region drifts. The unit cannot land as specified.
- **Fix (skeptic judged it SOUND):** Add tools/roles/roles_lib.py (`READ_KEYS` gains `plan:` and the field names S7 renders) and tools/roles/README.md (the gen:roles-catalogue region, re-rendered by its tool) to S7 and Files touched. Add a criterion: `python tools/roles/check_roles.py` exits 0 with gov-spec-writer reading `plan:goal?`, and is seen red on a staged reads key `plan:bogus`.
- **Left-shift gate:** A spec-audit check: a spec that adds a value to a closed vocabulary must list the vocabulary's defining file in Files touched.

### H6 — The new `triage` and `dupes` record kinds skip the binding reader, the factory table and the HYGIENE kind list (id 28)

- **Where:** TOOL-dRankedPlan-3 §2 S5 and S7, and §4 Files touched.
- **What:** S5 and S7 mint the kinds `triage` and `dupes` (`**Serves:** triage|dupes <id>`) but register them only as rows in record-kinds.toml. tree_lib.py `RECORD_KIND_TOKENS`/`TYPED_RECORD_KINDS`, build_records.py's kind table and HYGIENE.template.md with its memory/HYGIENE.md render are all unnamed. Spec 16 names all of them for `plan`.
- **Consequence:** The bindings parser reads any other first token as malformed. The factory refuses at import when its table and `TYPED_RECORD_KINDS` differ. Every triage or dupes record therefore cannot be written, or reads as a malformed binding, and the generated HYGIENE kind list drifts.
- **Fix (skeptic judged it SOUND):** Add tools/memory-tree/tree_lib.py (`triage` and `dupes` join `TYPED_RECORD_KINDS`), tools/memory-tree/build_records.py (kind-table entries and required fields), tools/memory-tree/HYGIENE.template.md and memory/HYGIENE.md (rendered) to S5/S7 and Files touched. Name `kit/dogfood doc parity` in §7. Add a criterion: `gen_build_index.py --print-bindings` lists a planted triage record as bound, and the same record reads malformed once the kind is dropped from the tuple.
- **Left-shift gate:** A single registration path. `record_kinds.py new` should refuse, or print the full list of files, when it is not paired with the tree_lib and factory entries. Alternatively, a parity leg reds a record-kinds.toml row missing from `TYPED_RECORD_KINDS`.

## Medium

### M1 — Unit 5's AC1 grep already matches unrelated files, so it cannot pass (ids 6, 14)

- **Where:** TOOL-dRankedPlan-5 §6 AC1.
- **What:** `git grep -l "item.entry.place-owner" -- memory/builds` must list exactly one record per population build's `build/` folder and none in a chain build's folder. At base it already lists 12 files. Three are .tsv files in dClosedLoop/build/ (a population build), and others sit in the chain builds dPlacedRequest and dRankedPlan.
- **Consequence:** The criterion is red before any record is written and can never go green on a correct build.
- **Fix (skeptic judged it SOUND):** Grade disposition records only, for example `git grep -l '^\*\*Item:\*\* item.entry.place-owner' -- 'memory/builds/*/build/*-disposition-*.md'`. Compare the result against F1's population, and pin the base count (0) so the criterion is seen red first.
- **Left-shift gate:** Every AC observation command is run at base, and its output is recorded in the spec as the red half.

### M2 — Unit 5's ratification cannot witness in the unattended build run (id 7)

- **Where:** TOOL-dRankedPlan-5 §2 S4, §8 F3 and §6 AC1-AC3.
- **What:** F3 picks the predicate path because the owner-terminal path "leaves the unit unbuildable unattended". Unit 9's `request` arm witnesses only with a claim ref for the build and a `.typed` line for the session. dRankedPlan has no `refs/gov/claims/*`, and its run mode is `slug`.
- **Consequence:** `ratify.py dRankedPlan` prints "unratified — request · no claim names a request". Unit 5 writes nothing, and AC1-AC3 cannot pass in a build run that defers no unit.
- **Fix (skeptic judged it SOUND):** State in F3 that unit 5 needs the owner, through the terminal path or an owner disposition via unit 10's fallback. Plan it as an owner-attended step of the build run, and re-word AC3 to the chosen witness.
- **Left-shift gate:** A preflight check that each unit's ratification witness is producible under the run's mode and claims.

### M3 — A paused, withdrawn or superseded build can stay the plan's next build (ids 8, 43)

- **Where:** TOOL-dRankedPlan-7 §2 S1/S3, with TOOL-dRankedPlan-1 §2 S2 and TOOL-dRankedPlan-4 §2 S1.
- **What:** Unit 7 takes the first placed row of `PLAN.md` as the next build. Unit 1 excludes only builds that are terminal by unit status. Unit 4 marks paused, withdrawn and superseded builds only in the `Dormant` cell and leaves them live and placed.
- **Consequence:** `offer-next` offers a parked build. Under `plan.kickoff: binding`, R8 refuses every route but the one to that build. The owner can recover by changing `plan.kickoff`.
- **Fix (skeptic judged it SOUND for both findings):** Either unit 1's `derive_plan_order` drops or sinks builds whose `derive_activity` is paused, withdrawn or superseded, or unit 7's `read_plan_next` skips such a row. Add a plant: PLAN.md's first row is a paused `aFirst` under `binding`, a route naming `aSecond` lands, and the cell names `aSecond`.
- **Left-shift gate:** A cross-unit fixture: each lifecycle state unit 4 writes is run through every unit-1/unit-7 reader.

### M4 — A refused `plan.triage` read falls back to `rules`, and AC5 never plants a refusal (ids 9, 17, 44)

- **Where:** TOOL-dRankedPlan-3 §2 S2 and §6 AC5, against TOOL-dRankedPlan-9 §8 F5.
- **What:** S2 takes a refused `plan.triage` read as the default `rules` and writes rows at once, printing one `NOTE:`. Unit 9 F5 denies by default on a refused read of a ratification-bearing key, and `owner-batches` is such a hold. AC5's `default` plant uses "no policy file". policy.py does not treat that as a refusal: it returns the catalogue default with exit 0 and no NOTE. So AC5 is red against S2, and no criterion exercises a real refusal. Real refusals arise when there is no valid revision, when `on-invalid = refuse`, or when the kit is unresolved.
- **Consequence:** On a refused read, a repository set to `owner-batches` gets SEV and SCOPE rows appended to every home BACKLOG.md (434 asks at base) and `gen_build_index --write` run, with no owner ratification.
- **Fix (skeptic judged it SOUND for all three findings):** On a refused read, `pass` exits 2 and writes nothing. If a fallback is wanted, it goes to `owner-batches`, never to `rules`. Split AC5 into (a) an absent policy file, which gives `rules` with no NOTE, and (b) a planted real refusal, for example a fixture whose first policy revision is invalid or whose landed ref names no commit, which writes no backlog file.
- **Left-shift gate:** A checklist entry: a refused policy read of a hold-bearing key fails closed. Every policy-reading arm plants a real refusal, distinct from an absent file.

### M5 — Unit 2's AC6 commits the policy locally, but the reader reads the landed revision (id 13)

- **Where:** TOOL-dRankedPlan-2 §6 AC6, with §5 security and S3.
- **What:** AC6 sets `plan.authority = "owner-orders"` in a local `--no-verify` commit in a scratch clone. The policy reader reads `refs/remotes/<remote>/<branch>`, which at base has no `[plan]` table, so it reads the default `planner-drafts-owner-ratifies`.
- **Consequence:** The expected refusal cannot happen. Making AC6 pass would require reading HEAD, and that breaks §5's guarantee that an agent cannot loosen the policy in the same commit.
- **Fix (skeptic judged it SOUND):** Put the policy on the landed revision. Use a fixture with no remote (or with `GOV_DEFAULT_BRANCH` set) whose default branch carries the `[plan]` commit, or push the setup commit to a bare origin before the probe commit. State in S3 that the value is read at the landed revision. Observe the fixture red while the policy is committed only locally.
- **Left-shift gate:** A shared policy-fixture helper in the test lib that always lands the policy commit on the read revision.

### M6 — Unit 1's AC4 compares LIVE.md bytes across commits that legitimately change it (id 15)

- **Where:** TOOL-dRankedPlan-1 §6 AC4 and S3 ("LIVE.md's bytes do not move").
- **What:** AC4 requires `memory/LIVE.md` at the pass tip to be byte-identical to its render at base. LIVE.md moves with any records commit: since base it has changed by 12 lines across commits that only add records and specs.
- **Consequence:** The criterion is red at every pass tip and never grades the `derive_activity` extraction.
- **Fix (skeptic judged it SOUND):** Restate AC4 as a same-input equivalence: render the tip's tree with the base blob's `render_live` and with the extracted version, and require identical bytes. Alternatively, add a selftest arm comparing `render_live` before and after the extraction over one fixture.
- **Left-shift gate:** A checklist entry: refactor-equivalence criteria hold the input fixed and vary only the code.

### M7 — Unit 9's AC6 ignores the `last-valid` fallback for an invalid policy file (id 16)

- **Where:** TOOL-dRankedPlan-9 §6 AC6, with S1 and S7's fixture.
- **What:** AC6 expects `plan.ratification = "email"` to make the reader refuse with exit 2. Under the default `policy-file.on-invalid = last-valid`, the reader refuses only when no valid revision precedes the invalid one. Otherwise it returns the earlier value. S1 never mentions the fallback.
- **Consequence:** AC6 fails on S7's fixture, or the builder adds a second value check. In real repositories a mistyped value silently reads the previous rule.
- **Fix (skeptic judged it SOUND):** State the fallback in S1. Make the "email" commit the file's first revision, or set `[policy-file] on-invalid = "refuse"` in an earlier valid revision. Add a case showing the last-valid answer.
- **Left-shift gate:** Same as M5: a shared fixture helper documenting the reader's revision and fallback semantics.

### M8 — The harness name never reaches `check_plan_exit` (id 18)

- **Where:** TOOL-dRankedPlan-10 §2 S3/S5 and §6 AC1/AC2.
- **What:** S5 has `write_transition` call `check_plan_exit(repo, slug, harness)` but names no source for the harness. The AC1/AC2 move command passes no harness, yet the ACs expect `harness=codex` and `harness=claude-code`.
- **Consequence:** Every move runs with harness `unknown` and takes the fallback. AC2 ("admitted with no disposition") cannot hold, and the drain path is untestable.
- **Fix (skeptic judged it SOUND):** Name the channel in S5. For example, `loop_transition.py record` gains `--harness <name>`, or reads a declared env var, and passes it to `check_plan_exit`. Spell that channel in the AC1/AC2 commands.
- **Left-shift gate:** A spec-audit check that every parameter a gate reads has a named producer at its call site.

### M9 — Unit 3 specs a new backlog-row writer that duplicates `migrate_backlog.add_row` (id 20)

- **Where:** TOOL-dRankedPlan-3 §4 "Rows" (line 193), §4 Inventory (line 260) and §10 (lines 439-442).
- **What:** `append_disposition_rows` duplicates `add_row(text, section, line, replaces, slug)` in tools/memory-tree/migrate_backlog.py:1589. `add_row` already appends under `## Dispositions`, creates the section when it is missing, and handles CRLF and the `replaces` edit. §10 wrongly claims that only the bash `write_backlog_rows` exists.
- **Consequence:** Two Python writers of backlog verb rows can drift on blank lines, section creation, `replaces` (which V4 depends on) and CRLF.
- **Fix (skeptic judged it SOUND):** Write rows through `migrate_backlog.add_row`, moved into backlog.py beside `H_DISPOSITIONS` if the import is too heavy. Drop `append_disposition_rows` from the Inventory and name `add_row` in §10. Add an arm that asserts the bytes equal `add_row`'s output, both with and without an existing section.
- **Left-shift gate:** The reuse scout's grep covers Python and bash writers of the same file region before §10 may say that no seam exists.

### M10 — Unit 4's new Activity values read as "unjudgeable" in the drift signal (ids 24, 33)

- **Where:** TOOL-dRankedPlan-4 §2 S1, §4 Evidence (lines 91-92) and §10.
- **What:** S1 writes `paused`, `withdrawn` and `superseded` into LIVE.md's Activity column. The drift signal `live_builds_without_activity` (tools/drift-audit/drift_report.py:3479-3517) counts any cell other than `active` or `dormant` as unjudgeable. The spec says the signal "moves nothing". The drift README:149, the `LIVE_DORMANT_DAYS` doc in .memory-tree.conf.example:446-450 and the memory-tree README:20 document only `active`/`dormant`.
- **Consequence:** Each disposed build shows as an "unjudgeable Activity cell" defect and drops out of the `of` denominator. The documentation becomes wrong for every adopter. The signal is report-only.
- **Fix (skeptic judged it SOUND for both findings):** Add drift_report.py's `build_live_builds_without_activity` (counting the three words as their own judged state), its selftest fixture, tools/drift-audit/README.md:149 and the conf-example paragraph to S1 and Files touched. Add a drift selftest arm with a `paused` row that reports unjudgeable 0.
- **Left-shift gate:** A spec-audit grep: a spec that adds a value to a rendered column lists every reader of that column.

### M11 — The new generated `memory/PLAN.md` has no `[[generated]]` row (id 29)

- **Where:** TOOL-dRankedPlan-1 §2 S3/S5 and §4 Files touched. kit.toml is named only for the version bump.
- **What:** No `[[generated]]` row in tools/memory-tree/kit.toml declares PLAN.md. LIVE.md and the ledger each have one. regen.py would still refresh PLAN.md through the LIVE.md row's `--write`.
- **Consequence:** The unattended driver's check 23 counts a PLAN.md write as undeclared, and `--dispatch --writes` does not pair it with its generator.
- **Fix (skeptic judged it SOUND):** Add a row with `path = "{memory_root}/PLAN.md"`, `generator = "gen_build_index.py"`, and the LIVE.md row's `write`, `check` and `stage = 2`. Add a criterion that regen.py names memory/PLAN.md. Stage a pass that writes only PLAN.md and observe that check 23 does not count it.
- **Left-shift gate:** A kit-check leg that reds any file the generator writes without a `[[generated]]` row.

### M12 — Unit 13's new held leg omits its budget row and foreign-prefix declaration (id 30)

- **Where:** TOOL-dRankedPlan-13 §2 S10 and §4 Files touched.
- **What:** The `plan-fields selftest` leg lists only subject-pins.tsv, ceiling-evidence.txt and the map claim. It omits the tools/run-gates/selftest-budgets.txt row and the WHOLE_RUN entry in foreign-prefix.gov.test.sh (or marker support). The manifest row has no `chunk` or `ceiling`.
- **Consequence:** `run-selftests.sh --check` reds ("HELD legs carry no budget row"), and so does the foreign-prefix parity leg. Neither leg is in §7.
- **Fix (skeptic judged it SOUND):** Add the budget row, the WHOLE_RUN entry (as for `corpus-ids selftest`) or the marker arm, and the `chunk`/`ceiling` fields. Name `every held leg is budgeted, every budget row resolves` in §7.
- **Left-shift gate:** A checklist entry, or a generated "rows a new leg owes" list in the spec template, derived from the legs that reference gate-legs.json.

### M13 — Unit 15's new leg omits its map claim, ceiling-evidence row and foreign-prefix declaration (id 31)

- **Where:** TOOL-dRankedPlan-15 §2 S6 and §4 Files touched.
- **What:** `loop plan revision` owes "the rows a new leg owes", but Files touched has no memory/map/features dossier claim (and loop.md does not exist yet), no ceiling-evidence.txt row and no foreign-prefix declaration.
- **Consequence:** `codebase-map coverage + freshness` reds the unclaimed gate-legs key, which the shrink-only baseline cannot absorb. The held foreign-prefix leg reds the row too.
- **Fix (skeptic judged it SOUND):** Add the dossier claim, the ceiling-evidence row and the foreign-prefix declaration. Name `codebase-map coverage + freshness` in §7.
- **Left-shift gate:** Same as M12.

### M14 — Seven specs edit kickoff-watched files without re-stamping SESSION-KICKOFF.md (id 32)

- **Where:** TOOL-dRankedPlan-1 §4 Files touched and §7. The same omission is in specs 7, 8, 11, 12, 13 and 15.
- **What:** These specs edit files on the kickoff manifest's `watch:` list: check-memory-hygiene.sh, manifest-check.sh, skills/session-kickoff/SKILL.md and gate-legs.json. None lists memory/guides/SESSION-KICKOFF.md or names the `kickoff-manifest ratchet` leg.
- **Consequence:** That always-run leg reds ("watched files changed since last-audit with no re-stamp") on each pass.
- **Fix (skeptic judged it SOUND):** In each of the seven specs, add memory/guides/SESSION-KICKOFF.md (the §B re-audit and the `last-audit` re-stamp) to Files touched, and name the leg in §7.
- **Left-shift gate:** A spec-audit check that intersects Files touched with the manifest's `watch:` line.

### M15 — Unit 1's `refuse-new` makes three printed `--new-build` recipes stale (id 34)

- **Where:** TOOL-dRankedPlan-1 §2 S7.
- **What:** Under `plan.unplaced = refuse-new`, `--new-build` refuses without `--priority`. Three carriers print the command without the flag: `print_scaffold_recipe` (tools/unattended/unattended.sh:5495), tools/unattended/ASKS.template.md:31 with its render memory/guides/UNATTENDED-ASKS.md:31, and tools/memory-tree/README.md:339.
- **Consequence:** The driver's own remedy prints a command that the generator refuses, and the guides teach the old form.
- **Fix (skeptic judged it SOUND):** `print_scaffold_recipe` adds ` --priority <n>`, or adds it when `read_plan_unplaced` answers refuse-new. The template, its render and README:339 name `--priority`. Name `unattended kit gate` in §7.
- **Left-shift gate:** A spec-audit grep for every literal spelling of a CLI whose arguments the spec changes.

### M16 — Unit 5 writes outside the build's write boundary, undeclared and not idempotent (ids 35, 42)

- **Where:** TOOL-dRankedPlan-5 §2 S3, §4 Files touched and §8 F2 (`widens: none`).
- **What:** S3 writes 26 disposition records into 26 other builds' `build/` folders. The README's rules forbid this, and F2 rejects option (d) for the very same reason, yet F2 records `widens: none`. The spec declares no `--dispatch --writes` set. Nothing covers a door refusal midway or a re-run: a re-run writes a second record per build.
- **Consequence:** The departures report shows 26 unplanned writes, and 26 foreign README regions move. An unattended pass counts or refuses the writes as undeclared. A partial run leaves the population half-mapped, and a re-run breaks AC1's "exactly one" while `derive_mapping`'s "newest" read hides which record counts.
- **Fix (skeptic judged it SOUND for both findings):** Set F2's `widens:` to the 26 `memory/builds/<slug>/build/` paths, with a `**Surface:**`/`**Reason:**` record. List the `--dispatch --writes` set, and name the regenerated foreign README regions as shared renders. Make S3 idempotent by skipping a build that already holds an `item.entry.place-owner` record. Pre-validate every build before the first write, or make the pass resumable. Add a plant that runs the mapping twice, where the second run writes nothing.
- **Left-shift gate:** A spec-audit check that compares Files touched against the build README's write boundary and requires `widens:` to name any excess.

### M17 — `show` re-asks the session-scoped predicate when Design runs it (id 38)

- **Where:** TOOL-dRankedPlan-15 §2 S5.
- **What:** `show` evaluates `read_plan_ratification` when it runs, not as it stood when Design re-entered.
- **Consequence:** A properly ratified re-entry, read in a later session or by an unattended run, prints "design re-entered without ratification" and exits 1. Design receives a false refusal.
- **Fix (skeptic judged it SOUND):** S5 reads the `ratification=` and `harness=` fields unit 10 S5 writes on the re-entering `planning -> designing` move's trailer. Add an `unratified-reentry` counter-plant whose stub answers no witness at `show` time while the trailer carries `ratification=witness`. It must print `ratified`.
- **Related:** This is the same defect as H3 (id 4), kept separate because the binding grades differ. One fix closes both.
- **Left-shift gate:** As H3.

### M18 — `plan_record.py field` uses exit 1 for "absent", which a crashed reader also returns (id 40)

- **Where:** TOOL-dRankedPlan-16 §2 S4 and S7, and TOOL-dRankedPlan-14 S1.
- **What:** Exit 1 means both "no record" and "no such field", and Python also exits 1 on an uncaught exception. S7 and unit 14 S1 read exit 1 as absent. Neither says what happens when `resolve_kit_dir` finds no memory-tree kit.
- **Consequence:** A broken reader silently becomes "no plan". Briefs ship with every `plan:` key marked not supplied, and a planner's scenario re-pick is dropped.
- **Fix (skeptic judged it SOUND):** Give each answer its own exit code that Python never emits on its own, for example 0 value, 3 no record, 4 no field and 5 two records. Callers treat any other code, and an unresolved kit, as a refusal that names the cause. Add a plant that stubs `plan_record.py` to raise, and require the render to refuse.
- **Left-shift gate:** A checklist entry: no CLI contract may give exit 1 a domain meaning.

### M19 — `plan_fields.py scope` hands on paths without re-validating them (id 41)

- **Where:** TOOL-dRankedPlan-13 §2 S8 and §5 security.
- **What:** `scope` passes `Scope` paths to a role's code slot without S2's path validation (no absolute path, drive letter or `..`). §5's "validated once, at S2's check" ordering is not enforced: the record can be edited after the check, or never checked.
- **Consequence:** `../x` or `C:/y` reaches the code slot through `resolve_item_seed`. The effect is contained to which files fill that slot.
- **Fix (skeptic judged it SOUND):** S8 runs S2's validator on every entry. When an entry fails, it prints `unarmed — scope-paths: <slug>'s Scope refuses <entry>` and no path. Extend AC7 with `Scope: ../z, tools/ok.py`, which must print the unarmed line and no path.
- **Left-shift gate:** A checklist entry: validate untrusted paths at the point of use, not at an earlier check that the caller cannot prove ran.

### M20 — `--priority` is never validated before the scaffold is written (id 45)

- **Where:** TOOL-dRankedPlan-1 §2 S7 and AC6.
- **What:** `--new-build ... --priority <n>` writes the value without holding it to S1's `[1-9][0-9]*` grammar, and a repeated flag is not refused. `read_new_build_args` today parses only the slug and `--asks`.
- **Consequence:** `--priority 0` writes a README that makes every later generator run raise, `--check` on the bar included, until someone edits it by hand.
- **Fix (skeptic judged it SOUND):** Validate the value in `read_new_build_args` with S1's pattern before any write. Refuse `0`, non-digits and a second flag, naming the flag. Extend AC6 so that `--priority 0` exits non-zero and writes nothing.
- **Left-shift gate:** A checklist entry: a writer validates with the same grammar its reader enforces, and the grammar is shared as one constant.

### M21 — `revise` has no recovery when B6 fails after the revision commit (id 46)

- **Where:** TOOL-dRankedPlan-15 §2 S3 and §5 error states.
- **What:** `revise` commits `Revision <n>` and then records B6 through `write_transition`. If B6 fails, a retry mints `Revision <n+1>` over an orphan entry. `check_plan_revisions` grades only shape and numbering. Unstaged edits to the same file may be swept into the pathspec commit.
- **Consequence:** The region claims a revision that never moved the build, and the planner's half-done edits may be committed as part of it.
- **Fix (skeptic judged it SOUND):** Before appending, `revise` checks whether the newest entry has a matching B6 trailer. If it has none, it retries B6 for that entry instead of minting n+1. `check_plan_revisions` or `show` reds an entry with no B6. `revise` refuses when the plan record has unstaged modifications. Add a plant that fails `write_transition` after the commit and reruns `revise`; it must not write `Revision 2`.
- **Left-shift gate:** A checklist entry: every two-step write states its recovery for a failure between the steps.

## Low

### L1 — Unit 7 places its `plan —` cell after a `kickoff —` cell that is never stored (id 10)

- **Where:** TOOL-dRankedPlan-7 §2 S2 and §3 Edges (consumes-from TOOL-dRankedPlan-8).
- **What:** Unit 7 places `plan —` "after the `kickoff —` cell" in `render_card`. Unit 8 F3 makes `kickoff —` a computed line printed after the card and never stored.
- **Consequence:** Only line placement differs.
- **Fix (skeptic judged it SOUND):** Have unit 7 S2 and its edge say `plan —` follows `live —` inside `render_card`, with unit 8's `kickoff —` line printed after the stored card.
- **Left-shift gate:** An edge-pair check that the consumer's quoted interface matches the producer's final F-decision.

### L2 — Unit 16 S3 misdescribes which units add calls to `check_plan_record` (id 11)

- **Where:** TOOL-dRankedPlan-16 §2 S3.
- **What:** S3 says units 11 to 14 add calls inside `check_plan_record`. Only unit 13 adds the one `check_plan_fields` call, which carries units 11 and 12. Unit 14's check runs in scenario.py at step transitions. S3 also cites unit 2's output line form, though unit 2 is ordered later (5 against 1).
- **Consequence:** The text misstates what the `item.plan.record` witness grades. The effect is contained.
- **Fix (skeptic judged it SOUND):** Re-word S3 to that effect and state the line form inline.
- **Left-shift gate:** An edge-pair check, as in L1.

### L3 — Unit 2 §3 says "arms five" where it arms four (id 12)

- **Where:** TOOL-dRankedPlan-2 §3, second bullet.
- **What:** §3 says "This unit arms five". S5 and AC9 arm four, and `item.plan.dedupe` is unit 3's to arm.
- **Consequence:** A cosmetic count mismatch that could lead a builder to delete the dedupe stand-in.
- **Fix (skeptic judged it SOUND):** Write "arms four; `item.plan.dedupe` is TOOL-dRankedPlan-3's".
- **Left-shift gate:** None proportionate. This is a self-review item.

### L4 — Unit 16 pins a handoff count that the base sha does not reproduce (id 19)

- **Where:** TOOL-dRankedPlan-16 §4 Evidence and §5 perf.
- **What:** The figure "697 ... PINNED at `0689e7fa1`" does not match: the same grep counts 695 at that sha and 697 at later commits.
- **Consequence:** None on behaviour. A pinned number that a re-run cannot reproduce misleads the next reader.
- **Fix (skeptic judged it SOUND):** Re-pin with `git grep -l -F '<!-- gov:handoff ' 0689e7fa1 -- 'memory/builds/*/prompts/*' | wc -l` (695), or mark the figure DERIVED.
- **Left-shift gate:** A PINNED-figure check that re-runs each pinned command at its named sha.

### L5 — Unit 6 adds a second reader of the `**Serves:**` kind (id 22)

- **Where:** TOOL-dRankedPlan-6 §2 S1 (lines 35-44) and §4 Inventory (line 129).
- **What:** `read_subject_kind` in review_pin.py duplicates `read_record_kind` (tools/workflows/review_replay.py:118) with a different line rule: "the first line opening `**Serves:**`" against the first non-blank line.
- **Consequence:** The two readers disagree only on records whose binding is not on the first line, which the hygiene grammar already forbids.
- **Grade note:** The finder graded this medium. The skeptic re-graded it low because the effect is contained. The binding grade is low.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Extract a generic `read_serves_kind(text)` in review_replay.py that returns the first non-blank line's `**Serves:**` first word, or None. `read_record_kind` wraps it and keeps its spec-audit/diff-review filter, so its three callers are unchanged. review_pin.py calls `read_serves_kind`. Drop `read_subject_kind` from the Inventory and name the seam in §10.
- **Left-shift gate:** The reuse scout greps for an existing parser of the same header before §10 may claim no seam exists.

### L6 — Unit 13 re-specs the repo-relative path refusal that `read_asks_args` already holds (id 23)

- **Where:** TOOL-dRankedPlan-13 §2 S2 (lines 44-47) and §10.
- **What:** S2 re-specs the refusal of absolute paths, drive letters and `..` that `read_asks_args` already does inline (gen_build_index.py:3337-3343).
- **Consequence:** Today both copies encode the same rules. A later tightening of one copy would let them diverge.
- **Grade note:** The finder graded this medium. The skeptic re-graded it low because behaviour is identical today. The binding grade is low.
- **Fix (skeptic judged it SOUND):** Extract `check_repo_relative_path(value)`, call it from `read_asks_args` and from S2, and name it in §4 Evidence and §10. AC8 runs the same four inputs through `--asks --path` and asserts both refuse the same three.
- **Left-shift gate:** As L5.

### L7 — Unit 16 spells the handoff marker again in record-kinds.toml with no parity check (id 25)

- **Where:** TOOL-dRankedPlan-16 §2 S5 and §4 Data model (line 163).
- **What:** The `[[level]]` row spells `<!-- gov:handoff ` as a literal. The roles kit owns that grammar as `MARKER_RE`.
- **Consequence:** If the roles marker changes, the level check silently grades a different set of files.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Keep the literal in record-kinds.toml. Add a parity arm on the roles side, in check_roles.py or adopt-roles.test.sh, where roles already resolves memory-tree: every line `MARKER_RE` fullmatches starts with the `[[level]]` row's literal, and a planted marker-shape change reds it. Name the seam in §10.
- **Left-shift gate:** That parity arm is the gate.

### L8 — Unit 8 F6 settles a question that unit 7 S7 settles the other way (id 26)

- **Where:** TOOL-dRankedPlan-8 §8 F6 (lines 236-244) and §5 risks.
- **What:** F6 leaves `read_card_policy kickoff.runs` reader coverage to dPlacedRequest (TOOL-dPlacedRequest-73). Unit 7 S7 adds that `READER_SHAPES` row in this same build.
- **Consequence:** The effect is prose only. Unit 8 misdirects readers about who closes the ask, and when.
- **Fix (skeptic judged it SOUND):** Align F6 with unit 7 S7. Cite TOOL-dPlacedRequest-73 and state that unit 7's row covers `kickoff.runs` if dPlacedRequest has not landed it. Drop or reword the §5 risk.
- **Left-shift gate:** A spec-brief pass that de-duplicates shared asks across sibling units.

### L9 — memory/README.md and the adopter scaffold omit PLAN.md (id 36)

- **Where:** TOOL-dRankedPlan-1 §2 S9.
- **What:** memory/README.md:4 and tools/memory-tree/adopt-memory-tree.sh:519 name only LIVE.md and the ledger as generated indexes.
- **Consequence:** A documentation gap: PLAN.md looks like a stray file in the memory root.
- **Fix (skeptic judged it SOUND):** Add both files to S9 and Files touched, each naming PLAN.md beside LIVE.md.
- **Left-shift gate:** A doc-parity grep for "Generated index" lines against kit.toml's `[[generated]]` rows.

### L10 — A refused `plan.unplaced` read silently drops `refuse-new` (id 47)

- **Where:** TOOL-dRankedPlan-1 §2 S6.
- **What:** Under `refuse-new`, a refused or unresolved read reverts to `warn`, so the opener stops refusing builds that have no priority.
- **Consequence:** A build can be opened unplaced. It is contained and visible under `## Unplaced`.
- **Fix (skeptic judged it SOUND):** Under a refused read, `cmd_new_build` refuses a call without `--priority` and names the refusal, keeping `warn` only for the view line. Alternatively, record the fail-open as an accepted choice in §8. Add the case to the `plan-unplaced` arm.
- **Left-shift gate:** As M4: a refused read of a policy key fails closed.

### L11 — Unit 10's capability reader does not cover a malformed adapters.toml (id 48)

- **Where:** TOOL-dRankedPlan-10 §2 S1.
- **What:** A parse error, `events` given as a string (where `in` becomes a substring test), and duplicate `name` rows are all unspecified.
- **Consequence:** `events = "no-prompt-submit"` could drain the fallback. A parse error holds the gate safely, but it surfaces as a traceback.
- **Fix (skeptic judged it SOUND):** Refuse each case as a `fallback` with its own `<why>`, for example `capability table malformed: <cause>`. Add a `malformed-table` plant.
- **Left-shift gate:** A checklist entry: every TOML reader type-checks list fields and rejects duplicate keys.

### L12 — `Probes owed` and `Open questions` split on `; ` with no ban on `; ` inside a question (id 49)

- **Where:** TOOL-dRankedPlan-12 §2 S1, and TOOL-dRankedPlan-13 S6.
- **What:** Entries are joined by `; `, and a question containing `; ` is split into a malformed second entry.
- **Consequence:** The planner gets a refusal that names the wrong rule.
- **Fix (skeptic judged it SOUND):** State in unit 12 S1 and unit 13 S6 that a question may not contain `; `, and that the refusal names that rule. Have S4 compare the question after the same normalisation the probe door applies to `Subject`. Add the case to `probes-shape`.
- **Left-shift gate:** A checklist entry: every delimited one-line field states its escaping or ban rule.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=49 confirmed=49 refuted=0 unverified=0 blocker=1 high=9 medium=27 low=12 agents=11 out-tokens=258374

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-12.md:section 2 S5, section 8 F2, section 6 AC5; with TOOL-dRankedPlan-13 section 2 S9 and TOOL-dRankedPlan-10 section 2 S4/S5 | blocker | blocker | confirmed | Re-read TOOL-dRankedPlan-10.md:51-56. S4 `check_plan_exit` admits on S3 `met`, on the pre-placement exemption, or on a disposition record naming item.plan.exit. It never reads `check_plan_record` or any item witness. S5 wires only S4 into write_transition. TOOL-dRankedPlan-12.md:59-62 (S5), :220-222 (F2) and TOOL-dRankedPlan-13.md:80-87 (S9) all assert that plan.exit 'cannot pass' because it 'needs every reached item's witness'. grep of 'plan.exit' across the 16 specs found no other unit that builds that rule. grep for 'reached item' in the dDeclaredLoop and dPlacedRequest specs printed nothing. dDeclaredLoop-3:100 says the writer makes 'No judgement that a witness holds beyond resolving it'. flow-steps (dClosedLoop build record) gives plan.exit's witness as 'the transition record over the reached items' witnesses', so the specs claim the rule but no unit builds it. AC5 (12.md:193-196) only runs the schema check, yet its red-when names plan.exit. | sound | - |
| 2 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-14.md:section 2 S1 and S2, section 8 F3; with TOOL-dRankedPlan-16 section 2 S8 and AC8 | blocker | high | confirmed | TOOL-dRankedPlan-16.md:92-96 S8 writes the patch or repeat plan record with 'every other field `none`', and S3 (:48-51) makes `none` the written form of an empty field. TOOL-dRankedPlan-14.md:30-40 S1 namespaces a bare tag (`feature` -> `scenario.feature`). It special-cases `none` only for `Scenario reason`, and treats only an 'absent, empty or equal to the pin' Scenario as the pin. So `Scenario: none` reads as a re-pick of `scenario.none`. S2 (:41-50) refuses that as re-picked without a reason, or as not registered. S3 (:51-56) runs S2 on every transition into a step. The pin is defined as the first transition into `planning`, which a patch build never makes (unit 1 says a patch 'never reaches Plan'), so the pin is undefined. Every --placed-build patch or repeat build is refused at its step transitions. That blocks work rather than shipping a wrong result, so I grade it high. | sound | - |
| 3 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-2.md:section 2 S3, section 4 'The authority', section 8 F5 | high | high | confirmed | TOOL-dRankedPlan-2.md:56-57 (S3) and :139-140 make a row ratified only while `read_plan_ratification` answers a witness, and F5 (:311-315) picks that predicate. TOOL-dRankedPlan-9.md:42-49 (S2, `request`, the default) witnesses only when `--request-consent` exits 0 for this session's typed request, and answers unratified when no claim exists. It never reads a disposition record under `request`. Unit 10's fallback releases the gate by disposition alone. So any other session sees owner-ratified rows as unratified, and under planner-drafts-owner-ratifies the S4 hook admits an agent commit that reorders them. | sound | - |
| 4 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-15.md:section 2 S5, section 8 F3 | high | high | confirmed | TOOL-dRankedPlan-15.md:66-80 S5 judges ratification by calling `read_plan_ratification(slug)` afresh. When that call gives no witness it exits 1 with 'design re-entered without ratification', and this is the line Design receives. TOOL-dRankedPlan-10.md:163-170 shows the gate can admit plan.exit on `intake-not-installed`, `disposition` or `before-placement`, none of which the predicate counts. F3 (15.md:288-292) rests on 'the standing request ratifies the revision', which holds only in the typing session (9.md S2). The two answers diverge on the common fallback path. | sound | - |
| 5 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-10.md:section 2 S4; section 3 last bullet | high | high | confirmed | TOOL-dRankedPlan-10.md:51-56 S4 admits plan.exit whenever a disposition record names item.plan.exit and `check_disposition_record` admits it. dDeclaredLoop-16 S5 (lines 57-61) only checks that the Disposition is in the item's outcome set, with no freshness test. 10.md:95-96 says a revised plan crosses plan.exit again 'through S4 unchanged'. So after unit 15's B6 move back to planning, the first exit's disposition releases the second. Unit 4 S3 (4.md:41-44) does filter to records 'added after its newest transition', so the fix's precedent is real. | sound | - |
| 6 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-5.md:section 6 AC1 | medium | medium | confirmed | I re-ran `git grep -l "item.entry.place-owner" -- memory/builds`. It printed the same 12 files: three dClosedLoop/build owners-v-*.tsv, three dPlacedRequest/build files, dRankedPlan/build/...spec-stage-returns.md, plus prompts and spec files. TOOL-dRankedPlan-5.md:37 and :89 put dClosedLoop in the population, so its folder will list 4 matches, not 'exactly one'. The chain build dRankedPlan's build/ folder already matches before any record is written. AC1 (:171-174) cannot pass as written. The fix's `**Item:**` anchor matches the disposition field form shown in dDeclaredLoop-16.md:112. | sound | - |
| 7 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-5.md:section 2 S4, section 8 F3, section 6 AC1-AC3 | medium | medium | confirmed | `git for-each-ref refs/gov/claims` and `git ls-remote origin 'refs/gov/claims/*'` both printed nothing. RUN.md:17 says `mode: slug`. Under 9.md S2, no claim answers unratified 'no claim names a request'. 5.md S4 (:48-52) does hold the unit for the owner, so the hold itself is stated. But F3 (:215-221) justifies option (a) by saying it keeps the unit buildable unattended, which is false here. AC3 (:180-182) requires ratify.py to print a witness, which the owner-terminal path never gives, so AC3 cannot go green. The README (:35-36) says the build run defers no unit again. | sound | - |
| 8 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-7.md:section 2 S1 and S3; with TOOL-dRankedPlan-1 section 2 S2 and TOOL-dRankedPlan-4 section 2 S1 | medium | medium | confirmed | 7.md:29-33 S1 takes the first data row of PLAN.md's table. 1.md:43-46 S2 excludes only builds that are 'not terminal', and 1.md:133 defines terminal by unit status. 4.md:29-35 S1 surfaces paused, withdrawn and superseded only in the Dormant/Activity column. Unit 4's S3/S4 record a loop transition and do not touch unit statuses. So a paused or withdrawn build keeps its row and can stay the plan's next build. | sound | - |
| 9 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-3.md:section 2 S2, section 6 AC5; against TOOL-dRankedPlan-9 section 8 F5 | medium | medium | confirmed | 3.md:42-45 S2 takes a refused `plan.triage` read as the default `rules` and goes on writing rows. tools/policy/policy.py:30-31 and :46 show that real refused reads exist (an invalid file, exit 2), so a repository that set owner-batches can have its hold skipped. 9.md:249-252 F5 denies by default for the ratification read, citing the charter's [security] rule. 3.md:343-345 AC5 plants 'no policy file' while its red-when speaks of a refused read, so the refusal path is never observed. | sound | - |
| 10 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-7.md:section 2 S2, section 3 Edges (consumes-from TOOL-dRankedPlan-8) | low | low | confirmed | 7.md:34-36 S2 places `plan —` 'after any `kickoff —` cell TOOL-dRankedPlan-8 placed there', and the edge at :128-129 consumes 'render_card, with the `kickoff —` cell that unit adds'. 8.md:41-46 S3 and :222-227 F3 make `kickoff —` a computed line printed after the card and never stored, and 8.md:76 says it leaves render_card's cell list as is. The two specs disagree only on the line's position. | sound | - |
| 11 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md:section 2 S3 | low | low | confirmed | spec-16:52-57 says field owners' checks are calls 'which units 11 to 14 add' inside check_plan_record, and its output is 'in the line form of TOOL-dRankedPlan-2's plan_items.py witness'. spec-13:80-88 (S9): 'This unit's pass adds the one call check_plan_fields(root, slug)' which 'carries every entry of FIELD_CHECKS, TOOL-dRankedPlan-11's and -12's included'. In spec-14, grep for plan_record finds only line 32, the field reader. Its check_plan_scenario runs in scenario.py at the step boundary (S2/S3) and is never called inside check_plan_record. The README gen:build-order puts 16 at step 1 and 2 at step 5. | sound | - |
| 12 | coherence | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-2.md:section 3 second bullet | low | low | confirmed | spec-2:95 reads 'This unit arms five and adds no row'. S5 (:67-68) answers four items: input, research, place and lease. :98 and :110 give item.plan.dedupe's stand-in row and its arming to TOOL-dRankedPlan-3, and spec-3 S11 (:98-101) arms dedupe. The 'five' matches the five Carries lines, not the number this unit arms. | sound | - |
| 13 | grounding | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-2.md:section 6 AC6 (with section 5 security and S3) | medium | medium | confirmed | tools/policy/policy.py:24-27 says the reader reads the file 'as committed at the landed revision, never from the working tree'. derive_landed_revision (:475-502) builds `refs/remotes/{remote}/{branch}` whenever a remote exists. A scratch clone has an origin, and AC6's `[plan]` commit is local and made with --no-verify, so S3's read through resolve never sees authority=owner-orders. grep of .governance/policy.toml shows no [plan] or authority, so the read falls to the catalogue default, under which adding a priority line is admitted. AC6 therefore cannot go red-then-green as written. | sound | - |
| 14 | grounding | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-5.md:section 6 AC1 | medium | medium | confirmed | I re-ran `git grep -l "item.entry.place-owner" -- memory/builds`. It printed 12 paths, including three dClosedLoop/build/*.tsv files and three dPlacedRequest/build/*.md files, plus specs and prompts. AC1 (spec-5:171-174) requires exactly one record per population build's build/ folder and none in a chain build's folder, so it is red at base and stays red. The narrowed command in the fix printed 0 at base, and the disposition kind's name `<date>-build-<unit>-disposition-<n>.md` with an `Item` field (dDeclaredLoop-16 S4) matches its glob. | sound | - |
| 15 | grounding | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-1.md:section 6 AC4 (and S3 'LIVE.md's bytes do not move') | medium | medium | confirmed | spec-1 AC4 (:220-223) requires memory/LIVE.md at the pass tip to be byte-identical to its render at base, and it is red when 'LIVE.md moves'. `git diff --stat 0689e7fa1 HEAD -- memory/LIVE.md` printed '12 ++++++------' across commits that are records and specs only. LIVE.md therefore moves with any records commit, and the criterion cannot grade the derive_activity extraction. | sound | - |
| 16 | grounding | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-9.md:section 6 AC6 (with S1 'A refused policy read raises' and S7's fixture) | medium | medium | confirmed | policy.py:631-663 read_last_valid_value raises a Refusal only when no valid revision precedes the invalid one, or when on-invalid is not last-valid. Otherwise it returns the earlier revision's value with source last-valid. catalogue.toml:84-86 has default = "last-valid". spec-9 S7 (:69-71) commits a policy file on the fixture's default branch, and AC6 (:207-209) never says the 'email' commit is the file's first revision. S1 says only 'A refused policy read raises', with no mention of the fallback. | sound | - |
| 17 | grounding | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-3.md:section 6 AC5 vs section 2 S2 | medium | medium | confirmed | spec-3 S2 (:42-45) prints the NOTE only when 'a refused read' takes the default 'rules'. AC5 (:343-345) runs the `default` plant 'with no policy file' and expects one NOTE. policy.py:700 treats an absent file as a catalogue default (reason '... is absent'), not a Refusal, so S2 as built prints no NOTE, and no criterion plants a refused plan.triage read. | sound | - |
| 18 | grounding | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-10.md:section 2 S3/S5 and section 6 AC1, AC2 | medium | medium | confirmed | spec-10 S3 (:49-50) and :172 say a harness not passed is 'unknown', which no row names. S5 (:57-62) has write_transition call S4 but names no source for the harness. AC1 and AC2 (:253-263) run `loop_transition.py record ... --witness <sha>` with no harness flag, yet expect harness=codex / harness=claude-code in the trailer. The only channel the spec names is ratify.py's --harness, and :102 hands 'the --harness its executor passes' off to dWellOiledMachine. Nothing threads it into the move. | sound | - |
| 19 | grounding | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md:section 4 Evidence (the 697-file population) and section 5 perf | low | low | confirmed | spec-16:144-146 pins 697 at 0689e7fa1. `git grep -l -F '<!-- gov:handoff ' 0689e7fa1 -- 'memory/builds/*/prompts/*' \| wc -l` printed 695. The same grep printed 697 at 9fd80b4bd and at 911a70393, so the figure was measured at a later commit and labelled with the base sha. The qualitative claim does not depend on the count. | sound | - |
| 20 | reuse | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-3.md:section 4 "Rows" (line 193), section 4 Inventory (line 260), section 10 (lines 439-442) | medium | medium | confirmed | tools/memory-tree/migrate_backlog.py:1589-1620 add_row(text, section, line, replaces, slug) appends a row at the end of a named section and creates the section when it is absent, with H_DISPOSITIONS ordering, CRLF-tolerant matching and the replaces edit. build_texts_with (:1622) applies it per record. spec-3:193 instead specs a new append_disposition_rows that creates the section when missing. :439-442 claims the only existing seam is bash write_backlog_rows, which is false. | sound | - |
| 21 | reuse | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-10.md:section 2 S4 (line 51-56); also TOOL-dRankedPlan-9 section 2 S4 (line 54-57) and TOOL-dRankedPlan-15 section 2 S5 | high | high | confirmed | I re-read the cited lines. spec-10 S4 (lines 51-56) admits plan.exit when 'a disposition record ... names `item.plan.exit` and ... `check_disposition_record` admits it'. spec-9 S4 (54-58) requires only that build/ 'holds a disposition record ... whose Item is item.plan.exit and Channel terminal'. Neither sets a recency bound. grep for newest/after/older in specs 9, 10 and 15 finds none tied to the disposition read. TOOL-dDeclaredLoop-16 S5's check_disposition_record checks only that the Disposition is in the item's outcome set, so it adds no freshness either. Spec-4 S3 line 43 does apply 'added after its newest transition'. Spec-15 S5 (66-71) routes a revision's re-exit through plan.exit 'held by whatever plan.ratification and unit 10's fallback hold'. So the record from the first exit still in build/ re-admits the exit after the B6 revision. | sound | - |
| 22 | reuse | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-6.md:section 2 S1 (line 35-44), section 4 Inventory (line 129) | medium | low | confirmed | tools/workflows/review_replay.py:118-124 holds read_record_kind, which reads the first non-blank line's **Serves:** binding. Spec-6 S1 (35-37) specs a second reader in the same kit: 'the first line of the file opening `**Serves:** `'. Inventory line 129 lists read_subject_kind as new, and §10 says no existing seam fits. The two line rules differ, so the claim holds. The divergence only shows on a record whose binding is not on its first line, which the hygiene grammar already forbids, so the effect is contained. The fix is unsound. read_record_kind's callers depend on it returning only spec-audit or diff-review. Line 241 refuses kind-mismatch when the returned kind differs from mode. Line 295 does `read_record_kind(known_text) or "diff-review"`. Line 367 compares the result to diff-review. If it returned any kind word (plan, journal), a known record with another binding would get mode 'plan' at 295, and 241 would refuse candidates. | unsound | - |
| 23 | reuse | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-13.md:section 2 S2 (line 44-47), section 10 | medium | low | confirmed | At tools/memory-tree/gen_build_index.py:3338-3343, read_asks_args refuses inline a leading '/', a drive letter or a '..' segment, then calls resolve_ask_path (3256-3262, which only normalises). Spec-13 S2 (44-47) cites resolve_ask_path and re-specs the same refusal as a new check. So the predicate would have two copies in one kit. Today both encode the same three rules, so the behaviour is identical and only a later divergence matters. | sound | - |
| 24 | reuse | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-4.md:section 2 S1 (line 29-35), section 4 Evidence (line 91-92), section 10 | medium | medium | confirmed | tools/drift-audit/drift_report.py:3479-3517 counts only 'active' and 'dormant'. Any other Activity cell takes unjudgeable += 1 and a note 'unjudgeable Activity cell ...', and drops out of `of`. tools/drift-audit/README.md:149 says 'any other cell is unjudgeable'. Spec-4 S1 (28-34) makes LIVE.md's Activity print paused/withdrawn/superseded. §4 (91-92) says the signal 'reports the same rows and moves nothing'. Files touched (142-146) omits drift_report.py and its README. The signal is report-only (gateable False), so the effect is contained. | sound | - |
| 25 | reuse | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md:section 2 S5 and section 4 Data model (line 163) | low | low | confirmed | Spec-16:163 hard-codes `marker = "<!-- gov:handoff "` in record-kinds.toml, and S5 (72-78) selects the brief population by that prefix. The grammar lives in tools/roles/roles_lib.py:79 MARKER_RE, re-exported at handoff.py:107 and used at :437. That makes two spellings of one marker with no parity check. The fix is unsound. Its primary option makes the memory-tree check depend on the roles kit, which may not be installed beside memory-tree. Its premise that S7 'already reaches into the kit' is backwards: S7 has roles' handoff.py find memory-tree's plan_record.py, not the reverse. | unsound | - |
| 26 | reuse | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-8.md:section 8 F6 (line 236-244), section 5 risks | low | low | confirmed | Spec-8 F6 (236-244) settles the read_card_policy reader-coverage gap as an ask to dPlacedRequest, filed as TOOL-dPlacedRequest-73 (memory/builds/dPlacedRequest/BACKLOG.md:9). Spec-8's risks line (163-164) and Non-goal line (72) repeat this. Spec-7 S7 (78-82) adds a READER_SHAPES row for `read_card_policy <key>` in this same build, which covers kickoff.runs as well. So one question has two settlements, and unit 8's risk reads stale. The effect is prose only. | sound | - |
| 27 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md:section 2 S7; section 4 Files touched | high | high | confirmed | tools/roles/roles_lib.py:36-40 READ_KEYS is a closed set of the task:/card:/brief:/input: families with no plan: family. tools/roles/check_roles.py:200-205 adds R3 'reads key ... is outside the vocabulary' for any key not in READ_KEYS. Spec-16 S7 (86-91) has gov-spec-writer read plan:goal?, plan:acceptance?, plan:non-goals?. Files touched (217-227) omits roles_lib.py and the README gen:roles-catalogue region (tools/roles/README.md:354-385, row 382 prints gov-spec-writer's reads, checked via check_roles.py:114). grep of spec-16 for roles_lib/READ_KEYS/R3/vocabulary/roles-catalogue finds nothing. The unit as written cannot pass the roles check. | sound | - |
| 28 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-3.md:section 2 S5, S7; section 4 Files touched | high | high | confirmed | tools/memory-tree/tree_lib.py:406 RECORD_KIND_TOKENS has five kinds, and :544-565 marks any other first token malformed. PLAY-dOrderedCharter-42 S1/S2 and dTotalRecall-11/18 make typed kinds join TYPED_RECORD_KINDS, with the factory table required to equal it. Spec-16 S2 (40-47) lists tree_lib, build_records and HYGIENE.template/HYGIENE.md for plan, as dDeclaredLoop-16 S4 does for disposition. Spec-3 S5/S7 register triage and dupes only through record_kinds.py new. Its record sample (line 214) is `**Serves:** triage TOOL-aFoo-3`. Its Files touched (275-285) and a grep for TYPED_RECORD_KINDS/build_records/HYGIENE/RECORD_KIND_TOKENS find none of these files. So every triage and dupes record would read as a malformed binding, or be refused by the factory. | sound | - |
| 29 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-1.md:section 2 S3/S5; section 4 Files touched (tools/memory-tree/kit.toml named only for 'the kit version moved') | medium | medium | confirmed | tools/memory-tree/kit.toml:459-485 declares each generated output in its own [[generated]] row: LIVE.md, and also ledger, which comes from the same --write. Per the block comment, the unattended driver reads these rows for check 23 and --dispatch. Spec-1 renders memory/PLAN.md (S3, Files touched 176). Its kit.toml line (179) says only 'the kit version moved', and grep finds no [[generated]] row for PLAN.md. One overstatement: regen.py would still refresh and check PLAN.md, because the LIVE.md row's --write/--check covers every artifact of plan(). The check-23 undeclared-write and dispatch-pairing gaps are real. | sound | - |
| 30 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-13.md:section 2 S10; section 4 Files touched | medium | medium | confirmed | Spec-13 S10 (89-97) and Files touched (192) name only subject-pins.tsv, ceiling-evidence.txt and the map claim for the new kit-subject leg. tools/run-gates/run-selftests.sh:829-840 reds any gate-legs.json leg with subject 'kit' that has no selftest-budgets.txt row. foreign-prefix.gov.test.sh:48-50 reds a row that neither prints the probe marker nor appears in WHOLE_RUN (its :125 list). The precedent leg corpus-ids selftest has rows in selftest-budgets.txt:60 and foreign-prefix.gov.test.sh:129. grep of spec-13 for selftest-budgets/foreign-prefix/chunk/budget finds none, and S10 gives the manifest row no chunk or ceiling. | sound | - |
| 31 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-15.md:section 2 S6; section 4 Files touched | medium | medium | confirmed | Spec 15's Files touched (lines 188-198) lists gate-legs.json, registry.toml, subject-pins.tsv, kit.toml, selftest-budgets.txt, loop.toml, loop_transition.py and help/loop.md. It lists no memory/map/features dossier and no ceiling-evidence.txt row. tools/codebase-map/map_extractors.py:196 builds a `gate-legs` inventory from tools/gate-legs.json. test_codebase_map.py:141 asserts that every inventory key is claimed or baselined, and :155 says the baseline never gains a key, so an unclaimed new leg name reds. memory/map/features/loop.md does not exist yet. The siblings name these rows explicitly: spec 13 at :192-193 and TOOL-dDeclaredLoop-3 at :236-237 list ceiling-evidence and the map claim. tools/run-gates/foreign-prefix.gov.test.sh:48 reds an undeclared row that prints no probe marker, and S6 says nothing about FOREIGN_PREFIX_PROBE. Spec 15 S6 points to 'the rows a new leg owes', but its own Files touched leaves those rows out. | sound | - |
| 32 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-1.md:section 4 Files touched and section 7 (same omission in specs 7, 8, 11, 12, 13, 15) | medium | medium | confirmed | The `watch:` line in memory/guides/SESSION-KICKOFF.md:6 includes check-memory-hygiene.sh, gate-legs.json, manifest-check.sh and skills/session-kickoff/SKILL.md. I extracted each spec's Files touched. Spec 1 lists check-memory-hygiene.sh; 7 lists manifest-check.sh; 8 lists manifest-check.sh and SKILL.md; 11 and 12 list check-memory-hygiene.sh; 13 lists gate-legs.json and check-memory-hygiene.sh; 15 lists gate-legs.json. A grep for SESSION-KICKOFF or kickoff-manifest across all seven specs returned nothing. In manifest-check.sh, lines 1525-1541 raise fail 5 when a watched file moved and last-audit was not re-stamped. The leg `kickoff-manifest ratchet` sits in gate-legs.json with no guard. Earlier specs, such as aBatchedArm-4 and aBlindedTrial-5, do name SESSION-KICKOFF. | sound | - |
| 33 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-4.md:section 2 S1; section 4 Evidence (drift_report.py:3479 'reports the same rows and moves nothing') | medium | medium | confirmed | In drift_report.py, lines 3479-3513 count `active` and `dormant` and treat any other Activity cell as unjudgeable, recorded with a detail note and left out of `of`. Spec 4 S1 (:32-33) writes `paused`, `withdrawn` or `superseded` into LIVE.md's Activity column. Yet spec 4 §4 (:91-92) says the signal 'reports the same rows and moves nothing', and its Files touched lists only gen_build_index.py, loop_transition.py and help/plan.md. .memory-tree.conf.example:446-450 documents Activity as `dormant` or `active` only, and tools/memory-tree/README.md:20 says the same. | sound | - |
| 34 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-1.md:section 2 S7 (refuse-new refuses `--new-build` without `--priority`) | medium | medium | confirmed | Spec 1 S7 (:76-80) refuses `--new-build` without `--priority` under refuse-new. In unattended.sh, print_scaffold_recipe at :5495 prints `--new-build <new-slug> --asks %s` with no priority. ASKS.template.md:31 and memory/guides/UNATTENDED-ASKS.md:31 spell the command the same way. Spec 1 does list tools/memory-tree/README.md in Files touched, but S9 (:84-86) only touches the generator row (:20), so :339 keeps the old form. Neither unattended.sh nor ASKS.template is named anywhere in spec 1 (grep for unattended/ASKS returned nothing). | sound | - |
| 35 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-5.md:section 2 S3; section 4 Files touched; section 8 F2 (widens: none) | medium | medium | confirmed | memory/builds/dRankedPlan/README.md:49-50 limits writes to this build's folder and the `--dispatch --writes` paths. Outside that, it admits only ask rows in another build's BACKLOG.md and the shared renders. Spec 5 S3 (:42-47) and Files touched (:139-140) write a disposition record into every population build's own `build/` folder. F2 (:208-214) rejects option (d) because it 'writes into other builds' READMEs outside the write boundary', and §4 (:150-151) rejects `absorbed-by:` for the same reason. Yet F2 records `widens: none` for (a), which also writes outside that boundary. The spec declares no dispatch write set or departure for those paths. | sound | - |
| 36 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-1.md:section 2 S9 (docs) | low | low | confirmed | memory/README.md:4 reads 'Generated index: [LIVE.md](../../../LIVE.md) (builds with a non-terminal unit) + `ledger/<month>.md` shards'. adopt-memory-tree.sh:519 echoes 'Generated index: [LIVE.md](../../../LIVE.md) + `ledger/<month>.md` shards'. In spec 1 the only mention of adopt-memory-tree.sh is the HYGIENE render line (:175), and memory/README.md is never named. S9 updates only help/plan.md and the generator row in the kit README. The consequence is a documentation gap and nothing else. | sound | - |
| 37 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-2.md:section 2 S3, section 4 "The authority" | high | high | confirmed | Spec 2 S3 (:56-57) treats a row as ratified when read_plan_ratification answers a witness, and the S4 pre-commit hook evaluates that at commit time. Spec 9 S2 (default `request`) ratifies only when `--request-consent <key>` exits 0. Per dPlacedRequest-19 S5 (:58-62), that exit 0 happens only when this session's id is a line of requests/<key>.typed. In a later session, an unattended run or on another node, every row therefore reads unratified. §4 'The authority' (:144) lets an agent commit under the default `planner-drafts-owner-ratifies` 'change any line of an unratified row', so in those sessions an agent can reorder builds the owner ratified. AC3 uses a stub predicate, so no criterion tests across sessions. The guard fails on a common path, though only under defaults. | sound | - |
| 38 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-15.md:section 2 S5 | medium | medium | confirmed | Spec 15 S5 (:66-76) has `show` read the ratification through read_plan_ratification(slug) when it runs, and exits 1 with 'design re-entered without ratification' when that answers no witness. Under `request`, the witness is session-scoped (spec 9 S2; dPlacedRequest-19 S5). So a re-entry that was properly ratified, then read by Design in a later session, gives a false exit 1. Spec 10 S5 (:59-61) already records `ratification=<how>` on the plan.exit move's trailer. Spec 15 reads that move order but does not read the trailer field. | sound | - |
| 39 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-10.md:section 2 S4; section 3 last bullet | high | high | confirmed | Spec 10 S4 (:53-56) admits Plan's exit when any disposition record names item.plan.exit and check_disposition_record admits it. Nothing ties the record to the current crossing. §3 (:95-96) says a revised plan crosses plan.exit again 'through S4 unchanged', and spec 15 step 5 (:149-151) relies on the owner's disposition record to ratify the revision. A record left from the first crossing stays in build/ and releases the second crossing without any new owner act. The same is true of spec 9 S4 terminal-command. On the Disposition-value half: dDeclaredLoop-16 S5 checks only set membership, against the item's own outcome list or the dispositions set. I could not confirm which set item.plan.exit declares (dDeclaredLoop-13 uses `--outcome pass`), so `ask`/`none` admission is not established. The staleness half alone confirms the finding. | sound | - |
| 40 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md:section 2 S4 and S7 | medium | medium | confirmed | Spec 16 S4 (:69-70) uses exit 1 for both 'no record' and 'no such field'. S7 (:89-90) reads exit 1 as absent. Spec 14 S1 (:31-38) reads Scenario through the same CLI and answers the pin when it is absent. A Python process that dies on an uncaught exception also exits 1, so a crashed reader looks like 'no plan': the brief shows the keys as not supplied, and a planner's scenario re-pick is silently dropped. S7 does not say what happens when resolve_kit_dir finds no memory-tree kit. | sound | - |
| 41 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-13.md:section 2 S8; section 5 security | medium | medium | confirmed | Re-read unit 13. S2 (:44-47) puts the path refusals (absolute path, drive letter, `..`, empty entry) in the `check` verb. S8 (:75-79) has `plan_fields.py scope <slug>` pass its output straight through, with no validation and only three unarmed reasons (no plan record, scopes none, no kit). §5 (:210-211) claims Scope is validated once at S2's check before S8 hands paths on, but nothing enforces that order. S9 ties `check` only to `item.plan.record`'s witness at `plan.exit`. The seed `item.design.inventory` (AC7) runs later, against whatever the record holds at that point. AC7 plants only valid paths. The effect is contained to which files fill a role's code slot. | sound | - |
| 42 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-5.md:section 2 S3; section 4 Files touched; section 8 F2 | medium | medium | confirmed | The build README rule (README.md:49-50) reads: 'Writes stay in this build's folder ...; outside, only an ask row in another build's BACKLOG.md and the shared renders. The departures report lists the rest.' Unit 5 S3 and Files touched write 26 disposition records into other builds' `build/` folders, yet F2 marks `widens: none`. F2's own rejection of option (d) cites the write boundary, and that boundary covers these records just as much. On the second half: §5 and Rollout cover only a held ratification. A door refusal midway leaves some builds mapped. Nothing makes S3 skip a build that already holds an `item.entry.place-owner` record, so a re-run writes a second record. AC1's 'exactly one' would then go red, and S6's 'newest' read would hide which record counts. The effect is contained, because AC1 catches a double record. | sound | - |
| 43 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-7.md:section 2 S1 and S3 | medium | medium | confirmed | Unit 7 S1 (:29-33) takes the first data row of PLAN.md's table, and greps of unit 7 and unit 1 find no paused, withdrawn or superseded filter. Unit 1 S2 defines 'placed' as having a priority and not being terminal. Unit 4 S1 (:31-37) prints paused, withdrawn and superseded only in the `Dormant` column of a build that stays live, and its units do not become terminal. So a paused top-priority build becomes the plan's next build, and under `binding` R8 (S3) refuses every route that names another build. S3's 'binding holds nothing' path covers only an absent next build or a refused key. The owner can recover by changing `plan.kickoff`, so the effect is contained. | sound | - |
| 44 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-3.md:section 2 S2; AC5 | medium | medium | confirmed | Unit 3 S2 (:43-45) has a refused read of `plan.triage` take the catalogue default `rules` and print one NOTE. S4 says `rules` writes rows into each home BACKLOG.md, while `owner-batches` writes nothing to a backlog. AC5 makes the fallback mandatory ('Red when: a refused read stops the pass or takes another value'). policy.py:30-31 and :741 show that an invalid file usually falls back to its last valid revision, and an absent file reads its default rather than a refusal. So a true refusal is narrower than the finding implies: no valid revision, on-invalid=refuse, or an unresolved kit. It is still reachable, and on that path an owner who chose `owner-batches` gets unratified labels written. Unit 9 F5 denies by default for the same kind of mandate. On the fix: AC5's no-policy-file plant is not a refused read under policy.py, so the changed AC5 needs a plant that actually produces a refusal. | sound | - |
| 45 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-1.md:section 2 S7; AC6 | medium | medium | confirmed | Unit 1 S7 (:76-80) writes `priority: <n>` from the flag but names no validation. S1 makes `parse_front_matter` raise a Problem on any value outside `[1-9][0-9]*`. The current `read_new_build_args` (gen_build_index.py:3969-3987) parses only the slug and `--asks`, and raises on any other option, so the new flag's parse is entirely unspecified. AC6 exercises only `--priority 4`. With `--priority 0` the scaffold is written, and every later generator run, `--check` on the bar included, raises until someone edits the README by hand. That failure is loud, so the effect is contained. | sound | - |
| 46 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-15.md:section 2 S3; section 5 error states | medium | medium | confirmed | Unit 15 S3 (:49-60) refuses only on the wrong state, a staged foreign path, or bad --what/--why. It then appends the entry, commits, and records B6 through `write_transition`, with no recovery named if that second step fails. §5 (:217) says 'every refusal ... writes nothing', which a failure after the commit cannot meet. After such a failure the build stays in `designing`, so a re-run passes the state test and appends Revision n+1 over an orphan entry. `check_plan_revisions` grades only the shape and the numbering. 'Commits the plan record alone' does not say what happens to unstaged edits of that same file, which a pathspec commit would include. | sound | - |
| 47 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-1.md:section 2 S6 | low | low | confirmed | Unit 1 S6 (:68-75) reads: 'No kit, or a refusal, reads the default `warn` and prints its reason once.' So under a refused read, S7's refuse-new refusal does not fire, and a build without a priority is opened. That build shows under `## Unplaced`, so the effect is contained and visible. | sound | - |
| 48 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-10.md:section 2 S1 | low | low | confirmed | Unit 10 S1 (:33-40) names only an absent table, an absent row and a row with no `measured` as degraded cases. The closed `<why>` list (:144-146) holds no malformed case, and a grep for malformed, parse, duplicate or tomllib in unit 10 finds nothing. A non-list `events`, duplicate `name` rows and a parse error are all unspecified. The table is not shipped by this unit, and a parse error would hold the gate. | sound | - |
| 49 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-12.md:section 2 S1 | low | low | confirmed | Unit 12 S1 (:32-37) splits entries on `; ` and lists refusals only for kind, empty and repeated, with no rule against `; ` inside a question. Unit 13 S6 (:63-67) has the same join. A question containing `; ` splits into a malformed second entry, and the refusal it gets names the wrong rule. The normalisation half of the finding is speculative, but the missing ban is real. The effect is a misleading refusal only. | sound | - |
