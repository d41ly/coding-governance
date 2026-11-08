**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10

# dCalibratedLens — the parents cross-check readers' returns, verbatim

The five `gov-spec-reviewer` returns the cross-check record [`2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck`](2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-crosscheck`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group A, led by spec 1 (specs 1, 13, 14 and 24)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-1-2-spec-reviewer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-2-spec-reviewer.md).

1. Assumption table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | dFairHearing gives the harness a lens catalogue in `lenses.toml`, and four stage literals can be added to it (by name, with no id) | cite | AGREES | cl1:31-34; fh13:31-33 (S1), fh13:133-136 |
| 1 | A stage literal opens with `// gov:lens-slots <stage>` and holds the one line `{{LENS_SLOTS}}`, the form fh13 S3 gives | cite | AGREES | cl1:40-43; fh13:38-42, :171 |
| 1 | `PRESETS` (fh2 S1) gains four names; the marked receiver gains one ternary arm per literal | cite | AGREES | cl1:43-45; fh2:31-38, :137 |
| 1 | The receiver has seven literals in all (three from the parents plus four new) | cite | MISMATCH | cl1:143-145, :249, :319, :339; fh23:82-85 (S15), fh2:76, rp6:106-109 |
| 1 | fh2 S3's design-audit rows include `grounding`, `coherence` and `failure-envelope`, and those keys can recur under disjoint presets | cite | AGREES | cl1:47-49; fh2:40-43, :104-123; fh13:154, :336-342 |
| 1 | Slots follow file order, so each stage's new rows come first and the drawn rows follow in the table's order (deploy: `grounding` then `coherence`; maintain: `grounding`, `coherence`, `failure-envelope`) | cite | MISMATCH | cl1:163-176, AC1 :327-331; fh13:114, :172; fh2:104-123, AC2 :184-187 |
| 1 | Every stage row is `spec-audit` (rule 5); no key equals a literal name (rule 7); `cost` is legal beside the opt-in `cost` row because their presets are disjoint (rule 6, fh13 §8 F2) | cite | AGREES | cl1:176-179; fh13:152-155, :336-342; fh3:174 |
| 1 | `review_pin.py` (fh3 S8) reads the harness beside it the way `read_spec_subject_path` reads `SPEC_SUBJECT_PATH`; the subject mapping stands for `design`, `build` and an absent stage | cite | AGREES | cl1:51-56, :195-197; fh3:61-66, :191-197 |
| 1 | The literal set `--stage` admits is "a stage that a `gov:lens-slots` marker … declares" | cite | MISMATCH | cl1:51-54; fh13:133-136, fh2:36, fh23:82-83 |
| 1 | The marker set is read by a new `read_lens_literals` in `review_pin.py` | cite | MISMATCH | cl1:54-56, :220; fh23:153-156 (S35) |
| 1 | `PLAN_RECORD_PRESET` (rp6 S1) is `unit-spec` and is left for this build to re-point | cite | AGREES | cl1:56-57, :453-455; rp6:42, :69-71, :88 |
| 1 | AC5's fixture is a plan record whose first `**Serves:**` word is `plan`, as rp6 S3 plants | cite | AGREES | cl1:347; rp6:58-61, :180-181 |
| 1 | Re-pointing flips three rp6 arms in `tier2-review.test.sh`: its AC1, AC3 and AC4 | cite | MISMATCH | cl1:257-261; rp6:213, :195-197, :199-204 |
| 1 | rp6 S4's `help/loop.md` paragraph says the preset stays `unit-spec` until the Plan lenses land | cite | AGREES | cl1:261-263; rp6:62-65 |
| 1 | id3 S4's step 1a, with `DESIGN_REVIEW_WORKFLOWS` = `spec-review`, `spec-write`; `closing-review` is the Build review; id3 §3 and §8 F7 hand the other stages' effort to dCalibratedLens | cite | AGREES | cl1:33, :59-63, :208-211, :424-426; id3:60-69, :95-96, :170-178, :318 |
| 1 | Step 1a can be widened to `read_policy_setting(f"review.{stage}.effort", root)` | cite | MISMATCH | cl1:59-61; id3:70-73 (S5), :291-295 (AC7) |
| 1 | fh2 §4 measured a three-literal receiver as admitted by `agent-cap.js --only=scripts`, and AC3 re-measures the seven-literal receiver through the hook | cite | MISMATCH | cl1:143-145, :335-339; fh2:92-95; fh16:35-43 (S2), :229-232 (AC3) |
| 1 | AC2: `check-verifier-fanout.sh`'s `slots` line names each stage literal holding 5 | cite | UNKNOWN UNTIL BUILT | cl1:332-334; fh13:201, :207, :294-295; fh23:172-175 |
| 1 | fh2 S1 refuses `preset` beside the diff kind, and fh13 rule 5 admits one kind per literal (F2); v2:706's "dFairHearing's preset" is a spec-audit preset | cite | AGREES | cl1:397-402; fh2:31-34; fh13:152-153 |
| 1 | fh2 S5 logs the preset; fh13 escapes briefs | cite | AGREES | cl1:309-310, :316-317; fh2:47-49; fh13:182, :256-258 |
| 1 | fh3 and fh9 own the opt-in swap, lens notes after a swap and the six opt-in rows; `review.opt-in` is keyed by literal name; fh3 S11 files the six losing tests as an ask | cite | AGREES | cl1:97-102; fh3:39-43, :58-60, :67-69, :74-75; fh9:1, :38 |
| 1 | `review.<stage>.effort` row: `allowed` and `default` unchanged; no dTendedCadence or dFairHearing unit's §2 changes the row, `resolve_stage_efforts`, `stage-efforts`, `EFFORT_LEVELS` or `--trigger` | RB | AGREES | cl1:59-68, :75-77; catalogue.toml:1241-1245; probe: grep of every tc/fh spec for these names hits only fh11:354 (§10 prose); tc48:143-145 S37 touches only the workflow-count wording in `workflows.toml` |
| 13 | fh13 moves gov's lenses into `lenses.toml`; the lens kind, namespace and overlay rows are dCalibratedLens's | cite | AGREES | cl13:22-24; fh13:72-73 |
| 13 | The slot count lives in `check-verifier-fanout.sh` (`parser=…check-verifier-fanout.sh#LENS_SLOTS`), "its one home in the fan-out leg" | cite | MISMATCH | cl13:33-34, :67-72, :168, :173-176; fh13:204 vs fh23:172-175 (S42), fh13:89 |
| 13 | A tag `lens.<key>` per row is derived from the key alone; AC1 prints one tag per row and `gov_tag.py show lens.coherence` resolves to "that row"; AC7's member count equals the catalogue's row count | cite | MISMATCH | cl13:45-46, :185, :278-283, :301-303; fh13:154, :336-342; fh2:40-43; fh3:172-174; step_gate.py:32-33 |
| 13 | A gov row is `default_in = []`, `optin = false` until its losing test (fh13 §4); the key pattern is `^[a-z][a-z0-9-]*$`; `check_catalogue` can gain a rule | cite | AGREES | cl13:53-55, :185-187, F3; fh13:126, :138-139, :143-160 |
| 13 | fh3 S6 renders `OPTIN_LENSES` from `optin = true` rows; an `adopter-<name>` key passes fh3 S1's key check | cite | AGREES | cl13:63-64, :265-267; fh3:35-37, :55-57; fh23:78-81 |
| 13 | `review.opt-in`'s grammar is fh3 S9's map; the catalogue spells it as a set (F2's ask on dFairHearing) | cite | AGREES | cl13:73-74, :326-338; fh3:67-69; catalogue.toml:417-422 |
| 13 | A `[[class]]` row in `surface-classes.toml` (sp10 S1); the reader contract at `step_gate.py:32-35`; `--fixture --plant`; the `RED … vanished` line | cite | AGREES | cl13:83-93; sp10:42-46 (CLOSED); step_gate.py:32-35, :65, :253; surface-classes.toml:1-12 |
| 13 | The leg is made by `leg_factory.py new` (wb11) as a `[[gate_leg]]` row rendered into `gate-legs.json` | cite | AGREES | cl13:94-96; wb11:36-50 |
| 13 | The leg kind keeps its class functions in its own kit's module (wb28) | cite | AGREES | cl13:356-357; wb28:126-130 |
| 13 | `tools/workflows/kit.toml`, `gate-legs.json`, `subject-pins.tsv`, `selftest-budgets.txt`, `govkit/selftest.py`: a row is added, and no at-base fact is relied on | RB | AGREES | cl13:94-96, :231-234; fh16:64-70, fh23:122-125, fh27 (row additions only) |
| 14 | Swap removal stays fh3's `optIn`; the run literal is fh3 S8's preset; an exclusion compiles to an fh3 S2 swap; the literal keeps five (fh13 §8 F3) | cite | AGREES | cl14:35-40, :154, :161, :373-377; fh3:39-43, :61-66; fh13:343-347 |
| 14 | A replay is fh12's `replay_scorer.py`, run by whoever chooses to; `replay` names its committed output | cite | AGREES | cl14:44-47, :105-106, :121; fh12:30-31, :91, :229 |
| 14 | fh13's `check_catalogue` rule 2 is amended "where that unit lands it" to admit `replay` on an overlay row | cite | AGREES | cl14:239-243; fh13:148-149 |
| 14 | `flow.promote` row: `allowed` and `default` as at base; no parent changes it or the `instructions.exclude` read in `unattended.sh` | RB | AGREES | cl14:47-54, :135-137; catalogue.toml:826-830; probe as in the cl1 RB row (no hit) |
| 24 | fh2's measurement cited the same bare `agent-cap.js --only=scripts` command | cite | AGREES | cl24:20-24; fh2:92-95 |
| 24 | The hook at `agent-cap.js` denies a looped receiver with `spawns one agent per item` (`agent-cap.test.sh:2325`), so the payload pipe can red and green the stage receiver | RB | MISMATCH | cl24:39-43, :64-69, :111-116; fh16:35-43 (S2), :64-67 (S5), :229-232 (AC3); agent-cap.js:1940-1943 at base |

2. MISMATCHes

- **cl1, seven literals.** cl1:144 says "Seven literals are UNVERIFIED until the build pass", and cl1:339 says "the receiver's ternary over seven literals". But fh23:82-84 says `tier2-review.template.js` "carries a `WHOLE_DESIGN_LENSES` literal … the preset receiver gains a fourth branch selecting it, and the fan-out leg counts four marked literals". rp6:108-109 lists the parents' literals as "`diff-review`, `unit-spec`, `design-audit` and `whole-design`". Change: count eight literals in §4 Evidence, §4 id 16, §5 risks and AC3. Add TOOL-dFairHearing-18 and -23 to the build-run precondition (cl1:84) and to "Waits on" (cl1:119), and say that `PRESETS` then holds `whole-design` too. Revision: rev-4. Cause: pre-existing.
- **cl1, slot order.** cl1:175-176 says "each stage's new rows sit in the table's order and a drawn row fills its stage's slot after them". cl1:167-168 puts deploy `grounding` at slot 4 and `coherence` at 5, and cl1:171-173 orders maintain `grounding`, `coherence`, `failure-envelope`. But fh13:114 says "a row's place in the file is its slot order", and fh13:172 says the token is "replaced by each default row of that literal, in file order". fh2's rows sit in the order `coherence` (:104), `grounding` (:112), `reuse`, `failure-envelope` (:121), and fh2 AC2 (:185-186) pins that order. fh2's rows also come earlier in the file than any row this unit appends. So the render gives `coherence` before `grounding`, and puts drawn rows before the new ones, and AC1 ("in slot order") reds on the parents' renderer. Change: make §4 "The rows" follow file order: the drawn rows in fh2's relative order, and new rows placed where the table claims (S2 must say where in the file they go). Alternatively, drop the slot-number claims from AC1. Revision: rev-4. Cause: pre-existing.
- **cl1, `--stage` admits every marked literal.** cl1:52-54 says "a stage that a `gov:lens-slots` marker of the rendered harness beside it declares prints that literal as `preset`". But fh13:133-134 says "A LITERAL NAME is what a marker declares: `diff-review` for the diff kind's one literal, and a preset name of the spec-audit kind otherwise", and fh2:36 and fh23:82-83 add the `design-audit` and `whole-design` markers. So `--stage diff-review`, `unit-spec`, `design-audit` or `whole-design` prints a preset. `diff-review` is not in `PRESETS` (fh2:137), so the harness refuses it. Change: S3 and AC4 admit only `REVIEW_STAGES` members that a marker declares, and exit 2 on any other marked literal. Revision: rev-4. Cause: pre-existing.
- **cl1, a second marker predicate.** cl1:55-56 says "The marker set is read by `read_lens_literals` from the rendered `tier2-review.js`". But fh23:153-156 says "One predicate finds a marked literal: `render_lenses.py --markers <file>` prints the line number of each line matching the renderer's own anchored marker regex … A comment that names `gov:lens-slots` is not a marker". Change: `read_lens_literals` calls `render_lenses.py --markers` or imports the renderer's anchored regex, and cites fh23 S35 instead of minting a second regex. Revision: rev-4. Cause: pre-existing.
- **cl1, the rp6 arms that flip.** cl1:258-261 says it "flips three arms of TOOL-dRankedPlan-6 … its AC1 … its AC3 five spawns at the Plan lens keys, and its AC4 a `gov:lens-slots` marker naming the Plan literal". But rp6:213 says "New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3". AC4 (rp6:199-204) is a grep probe, not a suite arm. rp6 AC3's harness run passes "`preset: unit-spec`" itself (rp6:195-196), which a `PLAN_RECORD_PRESET` change never reaches. Change: id 43 names only rp6 AC1's arm (`{"preset": "plan"}`) as flipped. It states that rp6 AC3's harness arm is untouched unless it is rewired through `review_pin.py`, and that rp6 AC4 is a probe that reads red once the Plan literal lands. Revision: rev-4. Cause: pre-existing.
- **cl1, step 1a as an f-string.** cl1:60 says "`read_policy_setting(f"review.{stage}.effort", root)`". But id3:70-71 says "Both reads spell their key first as a literal, the shapes the policy kit's reader-coverage arm counts". id3:291-294 (AC7) says "`grep -c 'read_policy_setting("review.design.effort"' tools/roles/roles_lib.py` … prints 1 … Red when: a key is built from a variable". The parent's AC7 reads 0 after this unit, and cl1 names no supersession. Change: keep a literal read per stage (six literal calls, or a literal table), or state that id3 AC7's first grep is superseded. If the latter, show that `READER_SHAPES` (check_policy.py:425-435) resolves `review.{stage}.effort` to the `review.<stage>.effort` row. Revision: rev-4. Cause: pre-existing.
- **cl1 AC3 and §4 Evidence: the hook stops judging the receiver.** cl1:143-144 says "TOOL-dFairHearing-2 §4 measured a three-literal ternary admitted by `node tools/hooks/agent-cap.js --only=scripts`", and cl1:339 says "Red when: the receiver's ternary over seven literals is denied". But fh16:35-43 says "The review kit's `check-verifier-fanout.js` … holds rule 2: `fanoutFindings` with the receivers it admits, the `gov:fixed-verifiers` … markers … `MAX_LENSES` … moves with rule 2". fh16:229-231 (AC3) says "When `node tools/hooks/agent-cap.js --only=scripts < …` runs after the pass deletes rule 2, it exits 0". Once the parent lands, AC3 cannot red. Change: AC3 runs fh16 AC2's form, `node tools/workflows/check-verifier-fanout.js --hook tools/hooks/agent-cap.js tools/workflows/tier2-review.js`, and expects exit 0. §4 Evidence says the receiver rule moved with fh16 S2. Revision: rev-4. Cause: pre-existing.
- **cl13, the slot count's home.** cl13:69 says "`default_in` fixed by `parser=tools/workflows/check-verifier-fanout.sh#LENS_SLOTS`", and cl13:175 says "the slot count keeps its one home in the fan-out leg (TOOL-dFairHearing-13 §4)". But fh23:172-175 says "The slot count lives in `tools/workflows/check-verifier-fanout.js` beside rule 2 … no `measureSlots` lexer remains, and `LENS_SLOTS = 5` is the one home of the number", and fh13:89 hands that change to fh23 ("`LENS_SLOTS` its one home (its S34, S42 …)"). Change: S4, §4 "The schema" and the prose cite `tools/workflows/check-verifier-fanout.js#LENS_SLOTS` and TOOL-dFairHearing-23 S42, and add fh23 to the build-run preconditions (cl13:33-39). Revision: rev-3. Cause: pre-existing.
- **cl13, tags are not unique per row.** cl13:45-46 says the extractor "yields `lens.<key>` for each gov row", and cl13:278-280 (AC1) says it "prints one `lens.<key>` line per `[[lens]]` row … and `python gov_tag.py show lens.coherence` resolves the tag to that row". cl13:301-302 (AC7) says it "prints the class `lens` with a member count equal to the catalogue's row count". But fh13:340-341 resolves F2 to "(b) Unique per literal: a key may recur in rows whose `presets` are disjoint". fh2:41-42 says "`coherence`, `grounding`, `reuse` and `failure-envelope` reuse their keys in rows of their own". fh3:172-174 adds `security` and `cost` rows beside same-keyed defaults. step_gate.py:32-33 says "A reader returns an empty set". So `lens.coherence` names two rows, and the member count (distinct keys) is below the row count. Change: derive the tag from the key and say a tag addresses every row of that key, or add the literal to the tag. AC1 counts distinct keys, and AC7 compares with the distinct-key count. Revision: rev-3. Cause: pre-existing.
- **cl24, the red twin goes green.** cl24:41-42 says the copy "exits 2 and prints the hook's `spawns one agent per item` line", and cl24:68-69 says "`tools/hooks/agent-cap.test.sh:2325` at base denies `boundedParallel(all.map(...))` under `--only=scripts`". But fh16:35-36 says "`check-verifier-fanout.js` … holds rule 2: `fanoutFindings`". fh16:64-67 says "The arms of `tools/hooks/agent-cap.test.sh` over rules 0, 2 and 5 move to `tools/workflows/check-verifier-fanout.test.sh` … and the hook's suite gains one arm per moved rule asserting it now admits that rule's planted case". fh16:229-232 says the hook "exits 0, where the hook at the pass's starting commit exits 2". The base deny at agent-cap.js:1940-1943 leaves the hook. Change: S1, S3, AC2 and AC3 and §4 "The observation" run `check-verifier-fanout.js --hook tools/hooks/agent-cap.js <copy>` (fh16 AC2) and expect exit 1 naming the looped line. Name TOOL-dFairHearing-16 as the reason the at-base hook fact does not survive, and re-cite the moved deny case in `check-verifier-fanout.test.sh`. Revision: rev-3. Cause: pre-existing.

3. UNKNOWN UNTIL BUILT

- cl1 AC2 (`slots` line naming each stage literal): fh13 contradicts itself, and fh23 S42 moves the count. fh13:207 has the clean line print only a count ("`slots — <m> lens-slot literal(s), each holding 5`"), fh13 AC4 (:294-295) has it "naming every marked literal", and fh23 S42 moves the count to `check-verifier-fanout.js`. Only dFairHearing's build run decides the line that ships.

4. Rule-wide hits the rules do not bind

- cl1:140 ("release notes against the epoch") and cl1:165 ("since the last epoch") name a release epoch, not a lease epoch. RH does not bind them.
- cl14:52 `review.loop.window-days` is a `review.loop.*` key, but its catalogue owner is `dCalibratedLens` (catalogue.toml:1296-1299), and no dTendedCadence spec names it (grep returns nothing). It is not a parent surface.
- No spec in Group A reads `--claims`, `read_claims`, `refs/gov/leases`, a lease holder, `GOV_CADENCE*`, `run_cadence_period` or `maintain.py` (grep over cl1, cl13, cl14 and cl24). RH and RK are not on this group's line and have no hit.
- RB files whose parent change cl1, cl13, cl14 or cl24 rely on at no base fact: `tools/unattended/unattended.sh` and `VERBS.template.md` (tc6 and others never touch `--trigger`), `tools/roles/README.md` (tc10 catalogue region, tc48 S37 counts), `tools/govkit/selftest.py` (tc73, fh12), `subject-pins.tsv` (fh27), `selftest-budgets.txt` (fh23 S26), `gate-legs.json` and `workflows/kit.toml` (legs added). Every overlap there is an added row, not a changed fact.

5. Parent text that looks wrong

- fh2:92-95 and fh3:114-117 record a measurement "from `node tools/hooks/agent-cap.js --only=scripts`" with no payload named. A bare run exits 0 on unparsable stdin (agent-cap.js, cl24:64-65), so the measurement may have read no harness.
- fh13:207 and fh13:294-295 disagree on whether the `slots` line names the marked literals.
- fh13:204 calls `LENS_SLOTS=5` in `check-verifier-fanout.sh` "its one home". fh23:174-175 gives the one home to `check-verifier-fanout.js`, and fh16:41-42 says "the exact slot count that unit's native arm holds stays its own".
- rp6:213 declares no suite arm for AC4 (rp6:199-204), while AC4's "Red when" reads as an arm's.

## Group B, led by spec 10 (specs 10, 23, 36, 5 and 8)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-10-1-spec-reviewer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-10-1-spec-reviewer.md).

Group B (specs 10, 23, 36, 5 and 8) has 11 MISMATCH findings, all pre-existing. None comes from `66f7b8d32`: since `22a8efac3` only wm6, wm41 and wm58 moved, and no Group B spec cites them. Every probe was a read.

#### 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 10 | The factory `replay_scorer.py` holds `INSTANCES`, `read_raw_output` and `derive_paired_cases`, and a third instance is one more row (cl10:34-35, :102, :114, :120, :422) | cite | AGREES | fh12:30-39 ("It holds the `INSTANCES` table"), fh12:146-147 ("a third adds a row") |
| 10 | The factory re-derives every figure from committed outputs and runs no agent (cl10:380-382, F2) | cite | AGREES | fh12:21-22, fh12:90-91 |
| 10 | The instance's arms are `--fixture --plant` cases "run inside `review-replay selftest`" (cl10:311, :362) | cite | MISMATCH | fh12:166-168 and F3 fh12:315-317: later arms go in `replay_scorer.run_selftest` and count against `ARMS_DECLARED`. fh12:130-135 lists no `--fixture` mode |
| 10 | The new `INSTANCES` row needs only readers and a measure function (cl10:62-70, :201, :422) | RB (`replay_scorer.py`) | MISMATCH | fh14:41-44: each instance must declare `case_evidence`, and "An instance registered without the hook refuses at load" |
| 10 | A case's known rows are fh1's grammar: a `**Population:**` line and `\| tag \| address \| grade \| escaped \|` rows, read by `parse_known_set` (cl10:36, :42-44, :154-158) | cite | AGREES | fh1:47-57 |
| 10 | A case built from a finding (`address` is the row's `ref`, e.g. `:[§10]`) is scored through fh1 S3's adjudicated matches (cl10:48, :158, :170-171, :189-190) | cite | MISMATCH | fh1:59-61: a pair's `ref` must cite "the known row's `[tag]`". fh1:238-240 (AC2) exits 2 on a pair that cites none. fh12:50-51: a tag is "a lower-case slug in brackets" |
| 10 | The seed's `**Known:**` is fh1's known set, and its no-score baseline is `0/59` (cl10:72-74) | cite | MISMATCH | fh1:49 "`**Population:** 65 · reviewed 59 · escaped 6 · high 8`"; fh1:234-235 "returns 65 rows" |
| 10 | fh25's verdict record states one "reviewed score" for the seed's replay (cl10:73-74, :216-218) | cite | MISMATCH | fh25:34-35 "the two design-audit runs"; fh25:181-184 "Each run's … prints `reviewed <k>/59`" |
| 10 | The seed's `**Replayed:**` sha (and `**Base:**`) come from fh25's replay (cl10:73, :146, :161) | cite | MISMATCH | fh32:82-90 (S14) supersedes fh25 S6's single commit: the record names an orchestrating commit and each clone's `HEAD` separately. fh25:39-41 and fh32:103-107: the clone's `HEAD` is a transient placement commit |
| 10 | A replay runs "in an isolated clone at `**Base:**` as TOOL-dFairHearing-1 S5 runs its replay" (cl10:94-95) | cite | MISMATCH | fh25:26-27: fh1's clone step "exits 128". fh23:89-92 (S17) and fh32:99-101 (S17): the README replay section is "the procedure every later replay runs" |
| 10 | The seed loads lenses.toml, the three rendered audit agents and the charter template (cl10:75-79, :257-263) | cite (fh13, by surface) | AGREES | fh13:31 creates `tools/workflows/lenses.toml` at order 1, before fh25 at order 20. It is absent at HEAD (probe) |
| 10 | Those six paths are what fh25's replay agents loaded (cl10:78, :163) | cite | UNKNOWN UNTIL BUILT | fh1:143-148: `scriptPath` is this repo's `tier2-review.js`, `repo` is the clone at `6cfd21619` |
| 10 | The appendix row is fh8 S8's columns plus `units`, read by header name (cl10:189) | cite | AGREES | fh8:66-67 |
| 10 | A gov-only leg is a hand row in `gate-legs.json` plus an `[[exempt_leg]]` row shaped like `tier2-review self-test`'s, i.e. name and why only (cl10:62-68, :132-133, :277-278) | RB (`gate-legs.json`, `registry.toml`) | MISMATCH | tc7:82-87 (S4): the `[[exempt_leg]]` row "carries the leg's whole row under TOOL-dWitnessedBar-11 S1", and "`tools/gate-legs.json` is that row's render through `leg_factory.py --write`" |
| 10 | The `project-owned` rule at `kit.toml:36-37` gains `evals/**` (cl10:65-66, :134) | RB (`kit.toml`) | AGREES | fh16:69 widens the same rule "as it withholds its siblings". Base `kit.toml:35-37` read |
| 10 | The budget row, subject pin and `help/roles.md` / README sections are added (cl10:93-96, :226-228, :281-282) | RB | AGREES | fh23, fh27 and tc10/fh4/fh11 add rows or sections only. No parent §2 changes the row grammar these lines rely on |
| 23 | The seed's score and baseline are "the adjudicated score TOOL-dFairHearing-25's verdict record states" (cl23:35-37, :144, :181) | cite | MISMATCH | Same as the cl10 rows: two runs (fh25:34-35, :181-184), 65 known rows (fh1:49), and two commits per record (fh32:82-90) |
| 23 | Replayed sha = "TOOL-dFairHearing-25's replay"; the edits to the seed's loads since then are this build's units 5 and 1 (cl23:83-90) | cite | MISMATCH | Six parent units after fh25 (order 20) edit `tier2-review.template.js`. Files touched: fh27:227 (21), fh30:117 (21), fh35:144 (22), fh32:258 (23), fh37:186 (24), fh40:316 (26). §2 Scope: fh32 S1 (template `:1021`); fh40 S1 states unit 37 edits it |
| 23 | The `close-bar` `--fixture` plant is an arm inside `review-replay selftest` (cl23:53-57, :145, :156) | cite | MISMATCH | Same as the cl10 arm row: fh12:166-168, :315-317 |
| 36 | The replayed sha is fh25's; the edits since it are units 5 and 1 only (cl36:22, :26, :45-46, :86-90) | cite | MISMATCH | Same as the cl23 edits row (fh27…fh40) |
| 36 | The `seed-loads` `--fixture` plant (cl36:49-62, :105) | cite | MISMATCH | Same as the cl10 arm row |
| 5 | fh8 S8 gives the tenth column `disposition`, after `classes`; `units` goes after it (cl5:45-46, :58, :423-425, :565) | cite | AGREES | fh8:66-67 |
| 5 | `FINDING_SCHEMA` and `SPEC_FINDING_SCHEMA` are the finding schemas that gain `units` (cl5:56-58) | RB (`tier2-review.template.js`) | UNKNOWN UNTIL BUILT | fh18:47 (S4) and fh18:169-173: the whole-design walker schema is "`SPEC_FINDING_SCHEMA` … plus a required `walk` array" |
| 5 | The act record is written once per harness session (cl5:495, F1 b) | cite | AGREES | wm32:74, :86-87 "writes it once, at the act's exit" |
| 5 | `P90_MIN_ROWS` floor is 10 (cl5:509, F3 b) | cite | AGREES | wm53:273-276 |
| 5 | A new `review_replay.py --confirmed-rows` verb prints `parse_appendix_rows`' rows (cl5:305-307) | RB (`review_replay.py`) | AGREES | fh12:40-47: the parser moves to the factory, but `review_replay.py` "keeps its CLI … importing the moved names", so the fact survives |
| 5 | The `review.loop.retire` row at `catalogue.toml:1289-1293` has no `summary` (cl5:124-125, :180) | RB (`catalogue.toml`) | AGREES | No tc or fh spec names `review.loop.retire` (grep). Base catalogue `:1289-1292` and `unsummarised-keys.txt:192` read |
| 5 | A new `PARITY_ROWS` row in `resolve-python.test.sh` (cl5:310) | RB | AGREES | tc18:49 adds a row the same way. Base `:351` read |
| 5 | The keep kind joins `record-kinds.toml` and the HYGIENE kind list (cl5:359, :371-372) | RB | AGREES | tc4/6/17/43 and fh23/34/40 add their own rows or reword lines. None changes the row form or the list grammar cl5 writes to |
| 8 | fh8 S8's `disposition` column comes before `units` and `cause` (cl8:37, :46, :115, :122) | cite | AGREES | fh8:66-67 |
| 8 | fh8 S7 allows exactly one disposition per finding, in four forms (cl8:103-104, :295-301, :353-354) | cite | AGREES | fh8:56-62 |
| 8 | "A workflow script has no filesystem", as fh13 §4 cites the map (cl8:108-109) | cite | AGREES | fh13:99; `review-harnesses.md:48` |
| 8 | A work order is the union of "the slices, the `map` slot and the `code` slot" (fo4 S1), so its paths are those three together (cl8:60-61) | cite | MISMATCH | fo4:37-38: `ORDER_SLOTS` has nine points, and fo4:51 makes the `bug-classes` slot print each class's path |
| 8 | The map state is read from the line `slot map · filled` (cl8:67-69, :255) | cite | AGREES | fo4:35-36, fo12:121 |
| 8 | The `code` slot exists, and the not-in-view cause is this build's to compute (cl8:39, :97, :115) | cite | AGREES | fo17:44-46 (S1); fo17:86 "The not-in-view cause computed from the `code` slot: dCalibratedLens (`cl-dClosedLoop-0465`)" |
| 8 | AC6's dTendedCadence handoff carries a `role=gov-spec-writer` marker (cl8:270-273) | cite (tc1) | AGREES | Probe: `…-TOOL-dTendedCadence-1-5-spec-writer.md:5` `<!-- gov:handoff role=gov-spec-writer build=dTendedCadence unit=- …>`. Three `-reuse-scout.md` siblings exist |
| 8 | `parse_appendix_rows`, `extract_line_ref`, `extract_subject_pins`, `read_record_kind` and `LINE_REF` live in `review_replay.py`, and id 33 factors `parse_appendix_rows` there (cl8:48, :53-54, :128, :137-138, :150, :186-192, :216, :338) | RB (`review_replay.py`) | MISMATCH | fh12:40-45 (S2) moves these, `review_replay.py:87-305` and the constants `:64-81`, "into the factory unedited". Base probe: `LINE_REF` `:74`, `extract_line_ref` `:87`, `extract_subject_pins` `:127`, `parse_appendix_rows` `:151` |

#### 2. MISMATCH

- **cl10/cl23/cl36: the instance's arms.**
  - cl10:362: "the instance's `--fixture` plants, run inside `review-replay selftest`".
  - cl23:156 and cl36:49 say the same of `close-bar` and `seed-loads`.
  - fh12:166-167: "`replay_scorer.run_selftest` declares its own `ARMS_DECLARED` … `review_replay.py --selftest` exits 0 only when both runners reach their declared totals".
  - fh12:315-317: "an arm a later unit adds … lands in that runner".
  - **Change:** cl10 S1 and §7 make every plant an arm of `run_selftest` that raises `ARMS_DECLARED` (as fh27 S19 and fh32 S9 do), and mint `--fixture`/`--plant` in the Inventory, or drop them. cl23 and cl36 each add their arm to that count.
  - **Cause:** pre-existing.
- **cl10: `case_evidence`.**
  - cl10:201 mints `instruction-eval` as an `INSTANCES` key and names no `case_evidence`.
  - fh14:41-44: "Each instance in `INSTANCES` declares `case_evidence(case)` … An instance registered without the hook refuses at load".
  - **Change:** cl10 S1 names fh14 S2 and defines the hook (for example, the case's `**Subject:**` at `**Base:**` plus its known rows).
  - **Cause:** pre-existing.
- **cl10: tagless known rows.**
  - cl10:190: "`address` the row's `ref`". Example cl10:158: `…TOOL-dExample-3.md:[§10]`.
  - fh1:59-61: "Each pair's candidate must be a confirmed appendix row … whose `ref` cites the known row's `[tag]` somewhere".
  - fh1:238-240 (AC2): such a pair "exits 2".
  - Real unit-spec refs read `…:section 2 S3, S4` (probe of the round-1 audit's appendix), so they carry no tag. No pair against a case built from a finding can be adjudicated, so an `absent` case can never score `fell`.
  - **Change:** cl10 S2 and §4 either scope "A case from a finding" to tagged refs, or define its own address check for section and line keys (`extract_tag_ref`'s int key) instead of fh1 S3's tag rule.
  - **Cause:** pre-existing.
- **cl10: the seed's denominator.**
  - cl10:74: "`none` and `0/59`". cl10:49-50 scores "the known rows matched … as `<k>/<n>`".
  - fh1:49: "`**Population:** 65 · reviewed 59 · escaped 6 · high 8`"; fh1:234 "returns 65 rows".
  - **Change:** cl10 S2 and S5 state `n`: either 65, or the 59 `escaped no` rows, which matches fh25's `reviewed <k>/59`. Then fix the `0/59` literal (also cited at cl23:81) to agree.
  - **Cause:** pre-existing.
- **cl10/cl23: one score from two runs.**
  - cl10:73-74: "the reviewed score TOOL-dFairHearing-25's verdict record states for that replay". cl23:35-37 says the same.
  - fh25:34-35: "the two design-audit runs". fh25:181-182: "Each run's `review_replay.py --known-set …` prints `reviewed <k>/59`".
  - **Change:** cl10 S5 names which run's report is the seed's `<candidate src>`, and the rule for picking it (or one seed per run).
  - **Cause:** pre-existing.
- **cl10/cl23/cl36: the replayed sha.**
  - cl23:83: "The owed rule diffs from the seed's replayed sha, TOOL-dFairHearing-25's replay". cl36:22 says the same. cl10:146 `**Base:** <40-hex sha the item ran at>`.
  - fh32:82-84 (S14): the record "names the orchestrating commit … distinct from each clone's `HEAD`", and supersedes fh25 S6's "the commit the runs started from".
  - fh32:103-105 (S18): the placement commit is "referenced only by a transient ref".
  - **Change:** cl10 S5 cites fh32 S14. `**Replayed:**` carries the orchestrating commit. `**Base:**` is `6cfd21619` plus fh25 S2's placement step, because the clone's `HEAD` is unreachable here and would leave the seed `owed` forever.
  - **Cause:** pre-existing.
- **cl10: the replay procedure.**
  - cl10:94-95: "the item run in an isolated clone at `**Base:**` as TOOL-dFairHearing-1 S5 runs its replay".
  - fh25:26-27: "Spec 1's own clone step … is the step spec 23 AC10 names as exiting 128".
  - fh32:99-101: "The replay section of `tools/workflows/README.md` … is the procedure every later replay runs".
  - **Change:** cl10 S8 points to the README's "Replaying a review blind" section (fh23 S17, fh32 S17/S18) instead of fh1 S5.
  - **Cause:** pre-existing.
- **cl10: the leg declaration.**
  - cl10:62: "A row `instruction-eval` in `tools/gate-legs.json`". cl10:68: "an `[[exempt_leg]]` row … in the form `tier2-review self-test`'s takes", which is name and why only (`registry.toml:666-668`).
  - tc7:84-87: the `[[exempt_leg]]` row "carries the leg's whole row under TOOL-dWitnessedBar-11 S1 … `tools/gate-legs.json` is that row's render through `leg_factory.py --write`".
  - **Change:** cl10 S4 names tc7 S4 / wb11 S1-S3. The leg becomes one `[[exempt_leg]]` row carrying every manifest key, written with `leg_factory.py new --exempt` and rendered with `--write`, never hand-added to `gate-legs.json`.
  - **Cause:** pre-existing.
- **cl23/cl36: edits since the replay.**
  - cl23:87-90 and cl36:86-90 list only this build's units 5 and 1. cl36:26: "lists every edit to them since the replay".
  - Parent units after fh25 (order 20) edit the template: fh27 (21), fh30 (21), fh35 (22), fh32 (23; S1 edits `tier2-review.template.js:1021`), fh37 (24), fh40 (26). Files touched lines are fh27:227, fh30:117, fh35:144, fh32:258, fh37:186, fh40:316.
  - **Change:** cl23 and cl36 §4 count parent edits to the seed's loads after fh25's orchestrating commit too. AC6's `owed` detail may then name paths no dCalibratedLens unit moved.
  - **Cause:** pre-existing.
- **cl8: what a work order holds.**
  - cl8:60-61: "A work order is the rendered union of the slices, the `map` slot and the `code` slot it hands (TOOL-dFurnishedOrders-4 S1)".
  - fo4:37-38: `ORDER_SLOTS = ("memory", "code-notes", "legacy", "house-index", "map", "code", "problems", "bug-classes", "instructions")`. fo4:51: the bug-classes rows print "its description and path".
  - **Change:** cl8 S3 either limits the view to the slices plus the `map` and `code` slot bodies, or states that every slot's paths count and widens §5's over-read risk to match.
  - **Cause:** pre-existing.
- **cl8: the moved appendix parser.**
  - cl8:48: "`parse_appendix_rows` (`tools/workflows/review_replay.py:151`), the kit's one appendix parser". cl8:186-187: it "is factored in `tools/workflows/review_replay.py`".
  - fh12:40-45: "`review_replay.py`'s scoring core moves into the factory unedited: `extract_line_ref`, … `extract_subject_pins`, … `parse_appendix_rows` …, with the constants they read".
  - **Change:** cl8 S1, S2 and id 33 name fh12 S2. `read_appendix_table` goes in `replay_scorer.py` beside `parse_appendix_rows`, and Files touched adds that file. The import may stay through `review_replay.py`'s re-export.
  - **Cause:** pre-existing.

#### 3. UNKNOWN UNTIL BUILT

- **cl10 seed `**Loads:**`:** fh25's build run decides whether its agents load this repo's `.claude/agents/*.md` and charter, or the clone's copies at `6cfd21619`. fh1:143-148 sets `repo` to the clone, and fh32 S14 records only the README, `tier2-review.js` and `replay_scorer.py` blobs.
- **cl5 S2 `units` on whole-design findings:** fh18's build decides whether its walker schema builds on `SPEC_FINDING_SCHEMA`'s item definition (so `units` is inherited) or copies it (fh18:169-173).

#### 4. Hits a rule does not bind

- **cl10:128, :331, :368 `govkit.py shipped --epoch`:** a release epoch, not a lease epoch, so RH does not bind.
- **cl5:495 (wm32 S7 act record, which has `Session` and `Epoch` fields):** cl5 rejects that option and reads no lease holder or epoch, so RH does not bind.
- **cl5:92, :445, :516 `Session`:** this is an override record's field (PLAY-dOrderedCharter-2), not a lease holder's, so RH does not bind.
- **cl5:120 `step = "cadence.loop"` and cl10:379 F2 option (c):** an item row and a rejected option. Neither reads, supplies or tests `GOV_CADENCE_KEY`, and the Group B line names no RK.

#### 5. Parent text that looks wrong

- **fh1:136-139:** still gives `git clone --branch fh-base "$TEMP/fhb/h.bundle"` as the isolation recipe, which fh25:26-27 says exits 128. Only fh25 and fh23 S17 correct it, through hands-off bullets.

Files:
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-10.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-23.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-36.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-5.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-8.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dFairHearing\spec\2026-10-23-spec-TOOL-dFairHearing-1.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dFairHearing\spec\2026-10-23-spec-TOOL-dFairHearing-12.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dFairHearing\spec\2026-10-23-spec-TOOL-dFairHearing-14.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dFairHearing\spec\2026-10-23-spec-TOOL-dFairHearing-25.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dFairHearing\spec\2026-10-23-spec-TOOL-dFairHearing-32.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dTendedCadence\spec\2026-11-01-spec-TOOL-dTendedCadence-7.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dFurnishedOrders\spec\2026-10-26-spec-TOOL-dFurnishedOrders-4.md`

## Group C, led by spec 3 (specs 3, 30, 11, 6, 22 and 41)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-3-1-spec-reviewer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-3-1-spec-reviewer.md).

#### Group C parent cross-read: dCalibratedLens specs 3, 30, 11, 6, 22 and 41 against origin/main `66c5b8dbf`

I found 4 mismatches: two in cl3, one in cl11 and one in cl41. All four were already in the parent text at `22a8efac3`; none comes from `66f7b8d32`. Two RK assumptions are unknown until built, and the other rows agree. Every probe only read. dTendedCadence asks 25, 27, 29 and 30 are not spec files, so their text is quoted from `memory/builds/dTendedCadence/BACKLOG.md` (written `BL:N` below).

### 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 3 | The build-run preconditions are wm59 S1–S3 (point, row check, tick), wm13 S5 and S6 (`derive_period`, `run_cadence_period`) and wm27 S1 (`intake.py file --origin cadence`). | cite | AGREES | cl3:40-48, :153, :537-540 · wm59:35-60, wm13:54-69, wm27:33-39 |
| 3 | Ask tc27: `run_cadence_period` sets `GOV_CADENCE_KEY`; its severity line says a program that re-derives its period can disagree with its lease. | cite | AGREES | cl3:43, :68, :394-395 · BL:13, BL:32, tc1:301-307 |
| 3 | Ask tc29 gives a cadence row `period-key`; `derive_period` takes `daily` and `weekly`, and tc29 adds `every-session`. | cite | AGREES | cl3:43, :76, :172-173 · BL:15, wm13:54-56, tc2:308-313 |
| 3 | Ask tc30 gives the `session-start` host; `maintain.host` defaults to `session-start`, so the review runs at session start. | cite | AGREES | cl3:44, :411-412 · BL:16, tc2:50-55, :148-150, catalogue.toml:1146 |
| 3 | The `loop-review` row sits at `point.cadence-items` with `host-key = "maintain.host"`, the expansion's one host key. A row requires a `host-key` naming a catalogue row. | cite | AGREES | cl3:73-79, :473-478 · wm59:35-46, tc11:58-59, tc13:35, tc2:36-37 |
| 3 | "This is TOOL-dTendedCadence-1 S2's walk"; after an exit 1 the next wake runs the period again. | cite | MISMATCH | cl3:61-63 · tc48:123-125 |
| 3 | Exit 1 releases the lease as a hand-over (wm13 S6 step 5). | cite | AGREES | cl3:61-63 · wm13:67-69 |
| 3 | `item.loop.lease`'s actor is the executor, spelled as `item.maintain.lease` is (tc1 S1). | cite | AGREES | cl3:197 · tc1:177 |
| 3 | The period segment admits a dot, as tc2's `<event>.<sha12>` keys do. | cite | AGREES | cl3:190-191 · tc2:365-368 |
| 3 | The `file` item files through `intake.py file --origin cadence --filer`. Its text carries no period, so the content key is the filing key, a recurrence is `seen` and a new key is `filed` (wm4's rule, the route tc15 S2 takes). | cite | AGREES | cl3:96-100, :396-398 · wm27:33-39, wm4:47-49, tc15:65-69 |
| 3 | The record lands as a records-only intake with JSON text that the patch build re-writes, "as TOOL-dTendedCadence-1 S6 lands a maintenance record". | cite | MISMATCH | cl3:108-112 · tc71:36-40, tc49:48-51, :141-143, wm4:54 |
| 3 | The home follows `maintenance-record` (tc6 S6, S8) under `point.memory.record-home`, with a contained atomic write. | cite | AGREES | cl3:245-246, :541-542 · tc6:210-215, :386-392 |
| 3 | tc1 F1 placed Maintain's rows in its kit descriptor and rejected `loop.toml` against EX-1. Ask tc25 says `read_items` reads only `loop.toml` and `check_program` needs a `[[step]]` exit row. The ponytail names tc25. | cite | AGREES | cl3:302-309, :501-514 · tc1:286-291, :211-214, BL:11 |
| 3 | tc2 §4 already ran the literal-rows test: such rows certify empty periods. | cite | AGREES | cl3:388-391 · tc2:302-306 |
| 3 | `cadence.py` is `tools/runtime/cadence.py`, which wm59 builds. | cite | AGREES | cl3:260, :430 · wm59:43-50 |
| 3 | The program reads its key from `GOV_CADENCE_KEY`. `--key` works only with `--dry-run`. With no key it exits 2 with `refused: no key; run under cadence.py run loop-review`. | RK | AGREES | cl3:65-72, :419-423 · tc1:68-71, :251-253, BL:13 |
| 3 | The `weekly` key is the ISO week, `^\d{4}-W\d{2}$`. | RK | AGREES | cl3:184 · wm13:54-56 |
| 3 | The `monthly` key is `YYYY-MM` and the `every-n-landings` key is `n<k>.<sha12>`, the tick deriving both. | RK | UNKNOWN UNTIL BUILT | cl3:185-186, :479-491 · wm13:54-56 gives only `daily` and `weekly`; tc29 adds only `every-session` (tc2:310-311) |
| 3 | Reads no lease session, `lease`-mode class or epoch. | RH | AGREES (not bound, see 4) | cl3:65-67 |
| 3 | RB `tools/runtime/points.toml`: one new row; no at-base fact about the file. tc2, tc11 and tc13 add rows only. | RB | AGREES | cl3:73-79 · tc2:36-49, tc11:58-59, tc13:35 |
| 3 | RB `tools/policy/catalogue.toml`: the `review.loop.*` rows answer `weekly` and `60`; `maintain.host` defaults to `session-start`. No parent unit edits `review.loop.*`; tc2 S8 keeps `maintain.host`'s values and default. | RB | AGREES | cl3:169-171, :411 · tc2:107-110; `grep -rn "review\.loop\."` over the tc and fh specs printed nothing |
| 3 | RB `tools/memory-tree/record-kinds.toml`: a new row; tc4, tc6, tc17 and tc43 add or read other rows. | RB | AGREES | cl3:113-114, :231-243 · tc6:100-104 |
| 3 | RB `HYGIENE.template.md`: the closed `<kind>` list gains `loop-review`. fh23 and fh40 change only review-guidance sentences. | RB | AGREES | cl3:272-274 · fh23:182, fh40:94-95 |
| 30 | Unit 3's F5 places the rows against tc1 F1 and ask tc25. | cite | AGREES | cl30:74-77 · tc1:286-291, BL:11 |
| 30 | Moving the preset flips three arms of rp6 (AC1, AC3, AC4), and rp6 S4 wrote `help/loop.md`'s Plan Review paragraph. | cite | AGREES | cl30:121-123 · rp6:180-200, :63, :213 |
| 30 | "The dFairHearing promoted-fix brief that caps a batch spec's size." The owner is `dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md` §2, ceiling 49152 bytes from `tools/template-size-limits.txt`. cl30 is 26913 bytes (`wc -c`). | cite | AGREES | cl30:374-378 · fh20 brief:14-19 |
| 11 | `decide_owner_items` (wm48 S4) walks the open owner items; one shared reader can be pulled out of it. | cite | AGREES | cl11:38, :72, :98, :343-344 · wm48:34-38 |
| 11 | `find_plan_record` and `read_plan_fields` are rp16 S4's. `derive_affected_systems` is rp13 S3's, with its degraded floor (rp13 S5). rp13 hands scope drift to dCalibratedLens. | cite | AGREES | cl11:38, :65-66, :334, :345 · rp16:78-86, rp13:52-66, :119-120, :134 |
| 11 | `drift --paths` refuses an entry "as TOOL-dRankedPlan-13 S2 refuses a scope path". | cite | MISMATCH | cl11:212-214 · rp13:52-54 |
| 11 | Reads policy through a bounded subprocess found by the inline `resolve_kit_dir`, as tc6 S1 does. | cite | AGREES | cl11:160-162 · tc6:46-50 |
| 11 | wm4's intake home `<git-common-dir>/requests/*` is node-local. | cite | AGREES | cl11:298-301, :359-360 · wm4:40-41, :79 |
| 11 | RB runlog files: the `rounds` verb sits beside `check-records`, and the record's `rounds` rows are read through `parse_record`. tc6 S1, S2 and S10 and tc9 add a policy read, a write rule, an anomaly list and the `reads` verb; none touches `rounds`. | RB | AGREES | cl11:55-63, :266-270 · tc6:46-60, :109-112, tc9:23 |
| 6 | rp1's scout cites `render_handoff` at `handoff.py:312`. | cite | AGREES | cl6:376-378 · `grep` found `tools/roles/handoff.py:312: def render_handoff`, also at `8bec4cef` |
| 6 | RB `tools/roles/README.md` and catalogue `memory.item-budget`: tc10 re-renders the catalogue region, fh23 the marker line, tc48 S37 a count. No parent edits `memory.item-budget`, `MARKER_RE` or the `check` and `roster` verbs. | RB | AGREES | cl6:33-34, :72-74 · tc10:60, :192; fh23:75; tc48:145 |
| 22 | The plant runs `run` with `GOV_CADENCE_KEY=2026-W45`, an ISO week key. | RK | AGREES | cl22:43, :124 · tc1:247, :268 (the same channel), wm13:54-56 |
| 41 | `record-refuses` runs with `GOV_CADENCE_KEY=2026-W45` "as the executor supplies it". | RK | AGREES | cl41:102 · BL:13, wm13:54-56 |
| 41 | At base, the `tier2-review self-test` guard is `{prefix}/workflows/` and `{prefix}/memory-tree/gen_build_index.py`. | RB | MISMATCH | cl41:151-152 · fh17:45-47, :183-184 |

### 2. Mismatches

- **cl3 S8 lands its record the way tc1 S6 used to, but tc49 and tc71 replace that landing.**
  - cl3:108-112: "its stable text the record's and the snapshot's content as JSON, so the patch build that takes it re-writes both with `python loop_review.py record --key <key> --base <sha>`, the JSON on stdin, and lands them, as TOOL-dTendedCadence-1 S6 lands a maintenance record."
  - tc71:36-40: "S6's landing sentence reads: the walk passes the written record's path to `write_record_landing` (TOOL-dTendedCadence-49 S4), whose intake names the payload commit and its digest, and the records-only patch build lands it with `maintenance.py land` (TOOL-dTendedCadence-50); no readings JSON."
  - tc49:141-143 rejects exactly this route: "The intake text is redacted and cut to `INTAKE_CAP_BYTES` (TOOL-dWellOiledMachine-4 S2), so a large period's readings are cut, and a redacted value changes the bytes". wm4:54 sets that cap at 65536.
  - **Change:** remove "as TOOL-dTendedCadence-1 S6 lands". Then take one of two routes:
    - carry the record and snapshot bytes as tc49 does: a parentless commit under a `refs/gov/` ref, named in the intake with a SHA-256, landed by a `loop_review.py land` verb that verifies them; or
    - keep the JSON, refuse any text over `INTAKE_CAP_BYTES`, and say why redaction cannot alter it.

    Either way, add a criterion that plants a snapshot over 64 KiB.
  - **Cause:** pre-existing. tc49 and tc71 were already in the tree at `22a8efac3` (`git cat-file -e` succeeded), and no dTendedCadence file changed after it.

- **cl3 S2 calls its walk tc1 S2's walk, but tc48 S28 gives that walk a re-run contract cl3 doesn't have.**
  - cl3:61-63: "exits 1 when an item raises or refuses, so `run_cadence_period` releases the lease as a hand-over and the next wake runs the period again (TOOL-dWellOiledMachine-13 S6 step 5). This is TOOL-dTendedCadence-1 S2's walk over another step's rows."
  - tc48:123-125: "The re-run contract: the walk appends each completed item to `<git-common-dir>/maintain-walk/<key>`, and a re-run under the same key starts after the last completed item, so a hand-over taken on the same node files no second receipt."
  - **Change:** either adopt the contract (a `<git-common-dir>/loop-walk/<key>` journal, plus a plant where `record` raises after `file` and the re-run files no second receipt), or say the Loop Review re-runs from the lease and why a second `seen` receipt per proposal is harmless. Either way, stop calling it tc1 S2's walk.
  - **Cause:** pre-existing.

- **cl11 §5 copies only two of rp13 S2's four path refusals.**
  - cl11:213-214: "each refused when absolute or carrying a `..` segment, as TOOL-dRankedPlan-13 S2 refuses a scope path."
  - rp13:52-54: "The check refuses an absolute path, a drive letter, a `..` segment or an empty entry".
  - **Change:** name all four refusals for `drift --paths`, or run them through rp13's own check rather than a second copy.
  - **Cause:** pre-existing.

- **cl41 states the base guard of `tier2-review self-test`, which fh17 S5 changes.**
  - cl41:151-152: "`tools/gate-legs.json` at base: the `tier2-review self-test` guard is `{prefix}/workflows/` and `{prefix}/memory-tree/gen_build_index.py`." That matches `8bec4cef` and HEAD, per a `python -c` read of the file.
  - fh17:45-47: "the driver's path added to that suite's leg guard in `tools/gate-legs.json`". fh17:183-184: "`{prefix}/unattended/unattended.sh` joins that leg's `guard` list".
  - **Change:** name TOOL-dFairHearing-17 S5. State that the widening of S27, which `TOOL-dCalibratedLens-46` builds, adds `{prefix}/hooks/agent-cap.js` next to whatever entries the guard holds at that pass, re-read then, and never rewritten from the base list.
  - **Cause:** pre-existing.

### 3. Unknown until built

- **cl3 `monthly` and `every-n-landings` keys (and the `landings` field that `check_cadence_row` must admit):** decided only when dWellOiledMachine builds cl3's own §8 F2 ask, on top of tc29's `period-key`. A `grep` for "PERIOD KEY HAS NO MONTH" or `every-n-landings` over every `BACKLOG.md` printed nothing, so that ask is not filed anywhere yet.

### 4. Rule-wide hits no rule binds

- **RH, cl3 (the `lease` hits, e.g. cl3:52, :65-67):** the lease belongs to the executor, which takes and releases it inside `run_cadence_period`. cl3 reads no session, `lease`-mode class or epoch, and does not parse a lease commit.
- **cl3:215, the "148 legs" surface count from `gate-legs.json`:** pinned at `8bec4cef` as an illustration, and "every value is DERIVED at the walk" (cl3:226-227), so the spec does not rely on it.
- **cl41:155-157, `--legs-for` over `handoff.py` and `tree_lib.py`:** no tc or fh §2 adds a leg guarding either file. tc73:45 explicitly declines to add `tools/roles/` to a guard.
- **cl22:54, `review.loop.retire`, and cl30:77, `cadence.loop`:** the first is dCalibratedLens's own key (unit 5 S7). The second is a step value, not a `cadence.*` policy key.
- **cl6:79 and :316, dWellOiledMachine named without a unit id:** an ancestor named by name, not a parent. The surface it names, the slice manifest's producer, is ask TOOL-dTotalRecall-35, which is out of scope.
- **cl3:134, :154, :480, :484, dWellOiledMachine by name:** these name the target of cl3's own F2 ask, already covered by the rows above.

### 5. Parent text that looks wrong

- tc1:100-104 still describes the readings-JSON landing, while tc49:48-51 and tc71:36-40 replace it. The two deferred texts contradict each other until tc71's build pass corrects tc1.
- tc15:66-68 says a recurrence appends a receipt to the intake on record. But wm4:40-41 keeps that record node-local and never committed, so a recurrence filed on another node starts a fresh intake there.
- tc2:51 lists `requesting-node` as a `maintain.host` value. The enum at `tools/policy/catalogue.toml:1145` is `session-start`, `os-scheduler` and `cloud-routine`, though its registry text adds "another registered host".

Files:
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-3.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-11.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-41.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dTendedCadence\spec\2026-11-01-spec-TOOL-dTendedCadence-48.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dTendedCadence\spec\2026-11-01-spec-TOOL-dTendedCadence-49.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dTendedCadence\spec\2026-11-01-spec-TOOL-dTendedCadence-71.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dFairHearing\spec\2026-10-23-spec-TOOL-dFairHearing-17.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-13.md`

## Group D, led by spec 9 (specs 9, 12, 16, 17, 20, 27 and 28)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-9-1-spec-reviewer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-9-1-spec-reviewer.md).

Group D (specs 9, 12, 16, 17, 20, 27 and 28) cross-read against the parent specs at `66c5b8dbf`. Every MISMATCH below already read the same way at `22a8efac3`. None of these specs depends on what `66f7b8d32` moved (wm6, wm41, wm58, tr2).

**1. Assumptions**

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 9, 12 | The act record carries `Item`, `Tokens-In`, `Tokens-Out` and `Wall`, and `trace.cost` writes `withheld` (cl9:34, :238; cl12:33, :77) | cite | AGREES | wm32:85-86 field list; wm32:97-99 `tokens` writes `Wall: withheld`, `none` writes all three `withheld` |
| 9, 12, 17 | `read_act_records(repo, build=None)` exists in `ledgers.py`, the runtime kit's one act reader (cl9:35, :334; cl12:34, :151-152, :223; cl17:37, :46-48, :222) | cite | AGREES | wm53:69-77 |
| 9, 16 | `ledgers.py acts` "calls `read_act_records(repo, build)` once" and prints `act` per record; cl16 id 50 maps each `Act` to its build and `Item` through it (cl9:40-43; cl16:52, :193-195) | cite | MISMATCH | wm53:76-77 reads only `Item`, `Wall`, `Tokens-In`, `Tokens-Out` per row |
| 9 (id 51) | `acts` reads the tracked act records with one `git ls-files` and one `git cat-file --batch`, "never one `gov_record.py show` per act" (cl9:183-188) | cite | MISMATCH | wm53:70-77 reads through `find` plus `show` per row; wm32:322-329 owner fork F6 rejected (c), the `git ls-files` listing, and picked (b) `find --all` |
| 28, 16 | `read_act_records` pages past `find`'s 40-row cap (cl28:35-36, :66, :137; cl16:194-195) | cite | UNKNOWN UNTIL BUILT | wm53:73-76 splits by `--paths` glob; wm32:325-329 (owner, 2026-10-29) says wm53 "meet[s] the same cap" and is served by `find --all` |
| 9 | `Gov-Act: <act>` is written on act commits, and an owner's commit carries none (cl9:35, :55-56, :288, :335) | cite | AGREES | wm33:40-45; wm33:48-50 commit queue |
| 9, 16 | The journal is node-local `<git common dir>/runlog/runtime.log`; `PRODUCER_FILES` gains `runtime` in both copies; `compaction` is a class (cl9:36, :69-71, :95-96; cl16:42-45, :115-117) | cite | AGREES | wm16:56-63 |
| 9 | A `compaction` line carries `item=<tag\|none>`, and "an act-less session counts as `unattributed`" (cl9:37, :310-314, :341) | cite | MISMATCH (second half only) | wm12 S8: "The item is the act record's `item` for an act session, else the item TOOL-dDeclaredLoop-7's `position.py <slug> --json` names for the binding's build, else `none`" |
| 9, 12 | Wall time, and the reservation estimate per item kind, are wm53's (cl9:98-99; cl12:62-63) | cite | AGREES | wm53:65-69 |
| 12 | `derive_build_spend` sums a build's act records read through `read_act_records` (cl12:22, :64-65, :224) | cite | AGREES | wm51:41-44 (S2) |
| 12 | An act record's date is the `<date>` its file name opens with, minted by the door at the act's exit (cl12:92-93, :203-206) | cite | AGREES | wm32:81-82 id-rule `<date>-build-<unit id>-act-<n>.md`; wm32:86-89 written once at exit, door mints `<date>` |
| 12 | The act record's `Epoch` field is the lease epoch (cl12:204) | cite | AGREES | wm32:50 "`epoch` (the lease epoch, or `none`)"; wm32:85 |
| 16 | `journal.py` has the verbs `write` and `prune`, and `classes` joins them (cl16:30-31, :357) | cite | AGREES | wm16:65-68 (S4), :69-79 (S5) |
| 16 | `point.journal-readers`: a reader opens a file only through `read_journal`, and runlog is the first reader (cl16:44-45, :226-227, :355-356) | cite | AGREES | wm16:85-88 |
| 16 | wm79 S12 drops `budget-spent`, `deadline-passed`, `cycle` and `secret-hit` "which no unit writes" (cl16:87, :112-114, :308-313, :366-367) | cite | AGREES | wm79:93-95 |
| 16 | `NOT_TRENDED` lists the tuple's classes that are no stall or loop event: `refusal`, `compaction`, `map-read-outside-slice`, `hook-failure`, `ledger-refused` (cl16:33-37) | cite | MISMATCH | wm6:141-142 S12 adds `act-launch`, `act-adopt`, `act-killed`, `act-exit`, `relaunch` and `limit-hold` to `JOURNAL_CLASSES` |
| 16 | `ledger-refused` is wm53's class (cl16:36) | cite | AGREES | wm53:56-58 |
| 16 | `key=` is on `no-progress` and `repeat`; the progress ledger's `new: yes/no` rows are node-local (cl16:118, :133) | cite | AGREES | wm46:41-50 (S1), :51-54 (S2), :55-63 (S3) |
| 16 | `rule=` is on `refusal` and `breaker-open` lines (cl16:119) | cite | AGREES | wm49:42, :147-150 |
| 16 | `stall` is a class wm47 journals (cl16:224) | cite | AGREES | wm47:58-59, :79 |
| 16 | F1's ask: a `budget-spent` line when `record_draw` returns `exhausted`, and a `deadline-passed` line when a wm47 wait reaches its deadline (cl16:319-321) | cite | UNKNOWN UNTIL BUILT | wm79:93-95 drops both; wm47:58-59 journals `stall reason=hold-ceiling` at that point |
| 16 | wm50 "produce[s] the lines"; F1 asks for a `cycle` line keyed `act=` or `session=` when wm50 raises a cycle owner item (cl16:85-86, :322-323) | cite | MISMATCH | wm50:86-87 non-goal: "No journal line: a node-tick sweep carries neither the `act` nor the `session` key TOOL-dWellOiledMachine-16 S3 requires; the owner item is the cycle's record." |
| 16 | The journal is pruned by `runtime.journal`, 60 days by default (cl16:68, :228-230) | cite | AGREES | wm16:69-79; `tools/policy/catalogue.toml:512-514` default 60 |
| 16 | `runtime.act-ceiling` evidence is the act record's `Wall` (cl16:132) | cite | AGREES | wm32:85-86, :92-99 |
| 17 | `beat.py`, `NODE_BEAT_KEYS`, `members` judging live beats, the closed key set keeping project names out, `help/runtime.md` (cl17:35-36, :56-59, :80, :139, :219, :331) | cite | AGREES | wm52:37-49 (S1), :57-61 (S3), :70-77 (S5), :78-79 (S6) |
| 17 | `members` reads the `node-` fields through the read-only verb wm52 §8 F3 asks of dPlacedRequest, and parses no lease record (cl17:36, :58-59, :106-107) | cite | AGREES | wm52:221-234, RESOLVED (owner, 2026-10-29) to (a); wm52:73-77 |
| 17 | `read_node_ledgers`; the `plan.json` pool fields; an expired reservation reads released; ledgers sit outside every repository, and the own ledger knows no fleet tag (cl17:50-54, :92-93, :145-147) | cite | AGREES | wm53:37-44 (S1), :54-60 (S3) |
| 17 | `derive_estimate_hours` is the one estimate: nearest-rank p90 of `Wall` per `Item`, `P90_MIN_ROWS` 10, else `runtime.act-ceiling`; `tokens`/`none` keep it at the ceiling (cl17:41-49, :85-86, :120-122, :237-244) | cite | AGREES | wm53:65-69; wm53:273-276 (F2); wm53:246-250 (AC6, 0.15 h and 1.5) |
| 17 | `Wall: withheld` under `tokens` and `none` (cl17:38, :118) | cite | AGREES | wm32:97-99 |
| 20 | wm32 joins `act` to `TYPED_RECORD_KINDS` and HYGIENE's closed list in one pass (cl20:39, :174) | cite | AGREES | wm32:74-79 |
| 27 | `intake.py file` is wm27's verb (cl27:66) | cite | AGREES | wm27:33-38 |
| 27 | `run_cadence_period` releases the lease as a hand-over on a non-zero exit, and the next wake re-runs the period (cl27:21-22, :83-84; by name, no unit id) | cite | AGREES | wm13:68, :126 |
| 27 | The plant supplies the key as `GOV_CADENCE_KEY=2026-W45`; `--key` is admitted only with `--dry-run` (cl27:52-53, :135, :140) | RK | AGREES | tc1:68-70; tc1:301-306 ask TOOL-dTendedCadence-27, `GOV_CADENCE_KEY=<period key>`, weekly key shape `2026-W44` |

**2. MISMATCH**

- **cl9 S1 and cl16 id 50: the act read's fields.**
  - cl9:40-43: "`python ledgers.py acts [--build <slug>]`, which calls `read_act_records(repo, build)` once and prints one JSON object per act record on stdout: `key`, `act`, `item`, `tokens-in`, `tokens-out` and `wall`".
  - cl16:193-195: "Acts are mapped to builds and items from `ledgers.py acts --build <slug>`".
  - wm53:76-77: "Each row's `Item`, `Wall`, `Tokens-In` and `Tokens-Out` are read through `gov_record.py show <key>`". `Act` is not among them, yet cl9 S3/S4's trailer join and cl16 S4's act-to-item map both key on it.
  - Change: cl9 rev-3 S1 states that it widens wm53's `read_act_records` to also read `Act` (and `Node` if wanted), names wm53 S4 as the function changed, and gives AC1 a red case for a missing `act`.
  - Cause: pre-existing.
- **cl9 id 51: the act-read route.**
  - cl9:183-186: "reads the tracked act records in one process (one `git ls-files`, one `git cat-file --batch`), never one `gov_record.py show` per act".
  - wm53:70-77: `read_act_records` runs `gov_record.py find --kind act` and then "`gov_record.py show <key>`" per row.
  - wm32:322-329 (owner, 2026-10-29): option (c), "list the kind's `home` glob through `git ls-files`", is "a second reader of the records beside the index". The owner picked "(b) the uncapped `find --all`", and F6 names wm53 among the readers that one ask serves.
  - cl9 S1 still says `acts` "calls `read_act_records`", so id 51 either rewrites wm53's reader the way the owner refused or bypasses it. In both cases cl12 S1, cl16 id 50 and cl28 S1 lose the reader they rely on.
  - Change: cl9 rev-3 drops the `git ls-files`/`cat-file` route and meets AC1's 500-record timing through `read_act_records` over `find --all` (wm32 F6 (b)). Failing that, it records that it overrides wm32 F6, files an ask on dWellOiledMachine, and moves cl12, cl16 and cl28 with it.
  - Cause: pre-existing.
- **cl9 §8 F4: the act-less session.**
  - cl9:312-313: "the line already carries `item=<item tag|none>`, the act record's `item` for an act session ... so the count reads the line alone and an act-less session counts as `unattributed`".
  - wm12 S8: "else the item TOOL-dDeclaredLoop-7's `position.py <slug> --json` names for the binding's build, else `none`".
  - Change: cl9 rev-3 rewords F4: an act-less session in a build counts under its position item, and only a session with neither an act nor a build counts as `unattributed`. The code is unaffected, since it reads the line alone.
  - Cause: pre-existing.
- **cl16 S2: `NOT_TRENDED` leaves out wm6's classes.**
  - cl16:33-37: "`NOT_TRENDED` holds the classes that are no stall or loop event: `refusal` ..., `compaction` ..., `map-read-outside-slice`, `hook-failure` and `ledger-refused`".
  - wm6:141-142: "The journal classes `act-launch`, `act-adopt`, `act-killed`, `act-exit`, `relaunch` and `limit-hold` join `JOURNAL_CLASSES`".
  - As written, every launch and exit line is trended as a stall or loop event.
  - Change: cl16 rev-3 cites wm6 S12 and either adds the classes that are no stall or loop event (at least `act-launch`, `act-adopt`, `act-exit`) to `NOT_TRENDED` or says why each is trended. AC2's `stall-new-class` plant stays as it is.
  - Cause: pre-existing.
- **cl16 §3 and §8 F1: the `cycle` line.**
  - cl16:85: "TOOL-dWellOiledMachine-46, -47, -49 and -50 produce the lines".
  - cl16:322-323: "`cycle` when TOOL-dWellOiledMachine-50 raises a cycle owner item, each line keyed `act=` or `session=`".
  - wm50:86-87: "No journal line: a node-tick sweep carries neither the `act` nor the `session` key TOOL-dWellOiledMachine-16 S3 requires; the owner item is the cycle's record."
  - The ask's accept condition is one the parent refuses. Since cl16 "refuses while the clause's six are not all trended", this precondition never clears.
  - Change: cl16 rev-3 names wm50 §3. It then either reads `cycle` from the cycle owner item (F1 option (b), for that class only), or widens the ask to a sessionless key that wm16 S3's writer would have to admit.
  - Cause: pre-existing.

**3. UNKNOWN UNTIL BUILT**

- **cl28 S1 and cl16 id 50, whether `read_act_records` pages past the cap.** dWellOiledMachine's build run decides whether `read_act_records` delivers the whole population through wm53 S4's glob split or through wm32 F6's `find --all`.
- **cl16 §8 F1, the `budget-spent` and `deadline-passed` writers.** dWellOiledMachine's build run decides whether it takes the ask, given that wm79 S12 drops both classes and wm47 already journals the deadline outcome as `stall`.

**4. Rule-wide hits a rule does not bind**

- **RH, cl9:96 ("the lease holder's node").** It reads only the node the walk runs on (cl9:151), under cl3's period lease. That is a node and no session or epoch.
- **RH, cl12:204 ("its `Epoch` field, the lease epoch").** This is a rejected F2 option naming the act record's field. Nothing reads a lease epoch.
- **RH, cl17:36, :58-59 (lease fields through wm52 F3's verb).** The group line does not name cl17 for RH. It reads `node-` keys, plus the tag and verdict from `--claims` fields 2 and 5, and no session, mode class or epoch.
- **RB, `tools/loop/README.md`.** tc18 S11 (tc18:187-188) only adds a leg mention. cl9 S8, cl12 S5 and cl17 S6 add prose and state no fact about the file at base. `tools/loop/` does not exist at `66c5b8dbf`: `git ls-tree --name-only 66c5b8dbf tools/` lists neither `loop` nor `runtime`.

**5. Parent text that looks wrong**

- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-16.md:56-60`: S3 still lists `budget-spent`, `deadline-passed`, `cycle` and `secret-hit`, though wm79:93-95 says "spec 16 takes a rev bump dropping them".
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-53.md:73-76`: S4 splits `find` by a `--paths` glob ending in the act id's hex digits ("the act id is 12 hex digits"). But wm32:306-312 (F4) names the record `<date>-build-<unit id>-act-<n>.md`, with the id "not part of the name", so the split has nothing to split on.
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-53.md:73-77`: S4 was not moved after wm32:325-329's owner pick of `find --all`, which names wm53 as served by it.
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-52.md:221-234`: F3 asks dPlacedRequest for a read-only `read_claims` verb printing "a lease's fields after the fifth by name". tr2 F6 (a) (`memory/builds/dTotalRecall/spec/*-spec-TOOL-dTotalRecall-2.md`, F6 at :340-357) files "one ask" for a holder verb over `read_claims` and does not mention wm52. So two asks may cover overlapping verbs, and F3's verb would also print `session` and `epoch`.
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-32.md:98` cites `trace.cost` at `catalogue.toml:1572`, but the row's `name` line is `tools/policy/catalogue.toml:1602`. This is line drift only, and cl12:229 already records it.

## Group E, led by spec 2 (specs 2, 4, 7, 15, 26, 37, 46 and 47)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-2-1-spec-reviewer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-2-1-spec-reviewer.md).

The cross-read of Group E (specs 2, 4, 7, 15, 26, 37, 46 and 47) against origin/main `66c5b8dbf` finds four MISMATCH rows and two UNKNOWN UNTIL BUILT rows; all other rows AGREE. None of the four comes from `66f7b8d32`: wm6, wm41 and wm58 are the only parent specs that moved since `22a8efac3`, and no Group E spec cites them. tc27 has no spec file; it is an ask row in `memory/builds/dTendedCadence/BACKLOG.md`.

1. Table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 2 | `run_cadence_period` sets `GOV_CADENCE_KEY` (and `GOV_CADENCE`) by ask TOOL-dTendedCadence-27 | cite | AGREES | cl2:78-79 · tc BACKLOG.md:13 ("accept `run_cadence_period` sets `GOV_CADENCE=<cadence>` and `GOV_CADENCE_KEY=<period key>`"), :48 DEFERRED; tc1:68-69, :304-307 |
| 2 | Inside unit 3's walk, `price` reads its key from `GOV_CADENCE_KEY` | RK | AGREES | cl2:124-125 · tc1:68-69 |
| 2 | `price --key <key>` writes a snapshot, and no refusal is stated for a missing key | RK | MISMATCH | cl2:77-80, AC5 cl2:406-409 · tc1:69-70, AC3 tc1:251-253 |
| 2 | The key grammar admits `^\d{4}-\d{2}$` and `^n\d+\.[0-9a-f]{12}$` as well as the weekly form | RK | MISMATCH | cl2:209-210 · wm13:54-55 (`derive_period` gives `weekly` `2026-W44` and `daily` only); tc BACKLOG.md:15 (tc29 adds `every-session` only) |
| 2 | The policy route: a bounded 30 s `policy.py get` subprocess through the inline `resolve_kit_dir`, with a refused read taking the default plus one line (TOOL-dTendedCadence-6 S1) | cite | AGREES | cl2:46-50, :494 · tc6:46-51 |
| 2, 26 | The flake record's name, its `Ended` field in the `- **Key:** value` grammar, its tsv rows `<leg>\t<first rc>\t<re-run rc or ->` with one row per executed leg, and that `retry-only` writes none while `quarantine` writes one (TOOL-dWitnessedBar-8 S3, S4) | cite | AGREES | cl2:67-72, :162-164, :273-275; cl26:35-37, :83-84 · wb8:48-51, :61-65, :128-149 |
| 2, 26 | A flake record is written for every Test-step bar, so it is "the committed per-leg verdict" and observes green legs | cite | UNKNOWN UNTIL BUILT | cl2:162-164; cl26:36-37, :166-167 · wb8:45-46 (the `flakes` route only for a red leg whose re-run reads `ok`), wb3:65-68 (`route` runs "on every red bar"), against wb30:37-40 ("A Test-step bar therefore executes the leg and `test.flakes` records its row") |
| 2, 4, 37, 46, 47 | The leg declaration: a `[[gate_leg]]` row in the kit descriptor or an `[[exempt_leg]]` row holding the whole row, the `[gate_leg.gov]` sub-table, `leg_factory.py new`, `--write` rendering the manifest and `--check` exiting 1 (TOOL-dWitnessedBar-11 S1 to S3) | cite | AGREES | cl2:111-115; cl4:80-84; cl37:74-75; cl46:36-45, :81-84; cl47:34-40 · wb11:36-50 |
| 2, 46 | A `loop-review selftest` row hand-written into `tools/gate-legs.json` before the factory lands ends up as a `[[gate_leg]]` row of `tools/loop/kit.toml` | cite | UNKNOWN UNTIL BUILT | cl2:114-115; cl46:38-40 · wb11:36-38 ("a `[[gate_leg]]` row in its kit's descriptor when an adopter receives it, else an `[[exempt_leg]]`"), :73-74 (S8) |
| 4 | `derive_estimate_hours` is TOOL-dWellOiledMachine-53 S3 | cite | MISMATCH | cl4:124 · wm53:54 (S3 is `read_node_ledgers`), wm53:61-68 (S4 holds `derive_estimate_hours`) |
| 4 | `P90_MIN_ROWS` is 10 (wm53) | cite | AGREES | cl4:373 · wm53:68 |
| 4 | The spend trend is a p90 (TOOL-dWellOiledMachine-51 S3) | cite | AGREES | cl4:125 · wm51:50-53 |
| 7 | The non-review act's shape-run record comes from `gov_record.py new shape-run --act`, with `Kind` `act`, `Workflow`, `Shape`, `Shape-match`, `Agents`, `Efforts`, `Out-tokens` and `Caused-by`, as wm19 §8 F2's ask of dTotalRecall (TOOL-dWellOiledMachine-19 S6) | cite | AGREES | cl7:24, :33, :64-65, :89-91, :224 · wm19:81-87, :228-237 |
| 15 | Each `warned` and `warn.<k>` value is `<leg>\t<class>\t<subject>\t<unit>`, and a held, skipped or reused leg's marker is not read (TOOL-dWitnessedBar-29 S3, S7) | cite | AGREES | cl15:34-35, :45-46, :186-187, :289 · wb29 S3, S7 (`warn.<k><TAB><leg name><TAB><class><TAB><subject><TAB><unit>`), wb29:117-120 |
| 15 | The verdict record's `tree` key, or `-` (TOOL-dWitnessedBar-4 S1) | cite | AGREES | cl15:35, :49-50 · wb4:42-44 |
| 15 | No journal class records a breach (TOOL-dWellOiledMachine-16 `JOURNAL_CLASSES`) | cite | AGREES | cl15:418 · wm16:57, :160; `grep -rn 'breach'` over wm16, wm34, wm53, wm6, wm65 and wm79 finds no breach class |
| 15 | `runlog.py reads` is a new verb, and "no seam counts a document's reads" | RB | MISMATCH | cl15:53-54, :197, :415 · tc9:46-56 |
| 15 | The extract.py readers `resolve_projects_root`, `read_records` and `derive_tool_class` survive unchanged | RB | AGREES | cl15:57, :164, :267 · tc9:48-51 reuses them unchanged; tc43 only cites `read_records` |
| 2 | `runlog.py journal --producer gates` / `--by-leg` as at base, which id 27 widens with `--since` and `--until` | RB | AGREES | cl2:72-74, :280-284 · tc6 S1, S2 (`read_run_record_policy`, `cmd_record`) and tc9 S1 (`reads`) change runlog.py, and none touches `journal` (`grep -- '--by-leg\|cmd_journal'` over the tc and fh specs: no hit) |
| 46 | At base the `tier2-review self-test` guard is `{prefix}/workflows/` and `{prefix}/memory-tree/gen_build_index.py`, and S5 adds three entries to it | RB | MISMATCH | cl46:85-87, :57-59 · fh17:45-47, :183-184, AC8 fh17:299-301 |
| 47 | The `format-guard self-test` guard and its `[[exempt_leg]]` row (name and why only) as at base | RB | AGREES | cl47:68-72 · no tc or fh §2 names that leg (`grep 'format-guard self-test'` over the tc and fh specs hits §7 gate lines only) |
| 2 | The catalogue rows `review.loop.catch-source` and `review.loop.window-days`, and `verdict.flakes` defaulting to `quarantine` | RB | AGREES | cl2:156-164 · `grep 'review\.loop\|verdict\.flakes'` over the tc and fh specs: no hit |
| 2, 4, 46 | `tools/loop/kit.toml` gains this build's `[[gate_leg]]` rows | RB | AGREES | cl2:336; cl4:251; cl46:100 · tc18:125-128 adds two loop-kit rows of its own, which is additive and contradicts no stated fact |
| 2 | The `record-kinds.toml` row, the `HYGIENE.template.md` kind list and check-3 prose, the `help/README.md` line, and the `subject-pins.tsv` and `selftest-budgets.txt` regeneration | RB | AGREES | cl2:339-348 · tc6 S8, tc4, tc8, tc17 and tc43 add other kinds' rows; fh23:182, fh34:25 and fh40:95 edit other prose and the version markers; tc15:117, tc48 S34 and fh17 add other help lines; fh27 and fh23 regenerate the pins and budgets. None changes a fact these specs state. |

2. MISMATCH

- **cl2, RK (`--key` writes):** cl2:77-80 says "The key is `GOV_CADENCE_KEY` (ask TOOL-dTendedCadence-27) or `--key` … anything else exit 2". AC5 cl2:406-409 runs "`price --key 2026-W45 --at …` … writes `<MEMORY_ROOT>/loop-review/2026-11-02-value-ledger-2026-W45.md`". On the parent side, tc1:69-70 says "`--key <key>` is admitted only with `--dry-run`, which reads and routes and writes, files and fixes nothing; no key at all exits 2", and tc1:251 says "with no `GOV_CADENCE_KEY` it exits 2 with `refused: no key`". cl3:70-71 mirrors the parent. **Change:** rev-5 of cl2 S5 admits `--key` only with `--dry-run`, and with neither key exits 2 `price — refused: no key; run under cadence.py run loop-review`. AC5's writing case then sets `GOV_CADENCE_KEY=2026-W45`, and a new red case covers `--key` without `--dry-run`. **Cause:** pre-existing.
- **cl2, RK (key forms):** cl2:209-210 says "The key is a period key of unit 3's three forms, held … to `^\d{4}-(W\d{2}|\d{2})$` or `^n\d+\.[0-9a-f]{12}$`". On the parent side, wm13:54-55 says "`weekly` gives the ISO week, `2026-W44` … `daily` the ISO date", and tc BACKLOG.md:15 (tc29) adds only `every-session`. The monthly and `n<k>.<sha12>` forms rest on cl3 §8 F2's own ask, which is not filed anywhere: `git grep -n 'NO MONTH' -- memory` hits only cl3:484. **Change:** rev-5 of cl2 §4 "The snapshot" names cl3 §8 F2's ask as the only source of the two forms. Until that ask lands, `GOV_CADENCE_KEY` carries only `^\d{4}-W\d{2}$`. **Cause:** pre-existing.
- **cl4, cite (section):** cl4:124 says "`derive_estimate_hours` (TOOL-dWellOiledMachine-53 S3, `tools/runtime/ledgers.py`)". On the parent side, wm53:54 begins "**S3** — The reader, `read_node_ledgers(home=None)`", and wm53:61-68 begins "**S4** — The charge at admission … `derive_estimate_hours(kind, repo)`: the nearest-rank p90". **Change:** rev-5 of cl4 §4 Evidence cites TOOL-dWellOiledMachine-53 S4. **Cause:** pre-existing.
- **cl15, RB (`runlog.py reads`):** cl15:53-54 says "`python runlog.py reads --since <epoch> [--transcripts <dir>] [--entry <path>]... <subject>...`, a new verb of `tools/runlog/runlog.py`, calls `measure_subject_reads`". cl15:415 says "no seam counts a document's reads, which is why S3 adds one". On the parent side, tc9:46-56 (DEFERRED rev-2) says "`measure_path_reads(projects_root, repo_root, since)` in `tools/runlog/extract.py` … counts each `Read` tool call … `python runlog.py reads [--days <n>] [--projects-root <dir>]` prints one `<path><TAB><count>` line per path". These are two verbs of one name with two grammars, and two readers of one source; tc9 §8 F5 (tc9:344-348) rejected a second reader for exactly that reason. **Change:** rev-3 of cl15 S3 names TOOL-dTendedCadence-9 S1 and takes one of two routes. It can extend tc9's `reads` with `--since`, `--entry` and subject arguments, through `measure_path_reads`. Or it can name the verb differently and say why tc9's counter cannot serve. Either way §10 drops "no seam counts a document's reads". **Cause:** pre-existing (`git show 22a8efac3:…-TOOL-dTendedCadence-9.md | sed -n 55p` prints the same verb).
- **cl46, RB (`tier2-review self-test` guard):** cl46:85-87 says "the `tier2-review self-test` `[[exempt_leg]]` row holds `name` and `why` only, and `tools/gate-legs.json` holds its guard, `{prefix}/workflows/` and `{prefix}/memory-tree/gen_build_index.py`". On the parent side, fh17:46-47 says "the driver's path added to that suite's leg guard in `tools/gate-legs.json`", and fh17:183 says "`{prefix}/unattended/unattended.sh` joins that leg's `guard` list". **Change:** rev-2 of cl46 §4 Evidence and S5 name TOOL-dFairHearing-17 S5. In both cases the declaration must keep fh17's `{prefix}/unattended/unattended.sh` beside the three new entries: the `[[exempt_leg]]` row in the factory case, the manifest row in the hand case. AC3 compares the full list. **Cause:** pre-existing.

3. UNKNOWN UNTIL BUILT

- **cl2 and cl26, flake records:** whether `test.flakes` runs on every Test-step bar, as wb30 S2 reads it, or only on a red bar routed `flakes`, as wb8 S2 with wb3 S6 reads it. TOOL-dWitnessedBar-8's build run decides. If it is only routed red bars, the `verdict-records` source never holds a run whose reds were all real, and a green leg is observed only in runs that also flaked.
- **cl2 and cl46, the loop leg's declaration:** where TOOL-dWitnessedBar-11's build pass puts a loop-kit leg that is already hand-written into the manifest, a `[[gate_leg]]` in `tools/loop/kit.toml` or an `[[exempt_leg]]`. The adopter test in its S1 decides, and cl46's factory case edits whichever declaration that pass creates.

4. Rule-wide hits a rule does not bind

- **cl15:53, :298-301 `--since <epoch>`:** a Unix time bound on transcript records, not a lease epoch, so RH does not bind it.
- **cl15:94, :109, :132, :349, :357 "the lease holder's node":** the node the walk itself runs on. The spec reads no other session's holder, `session` or epoch, so RH does not bind it. The brief's line numbers :83, :98, :121, :338 and :346 have drifted to these lines.
- **cl4:133, :169 and cl15:157, :304, :343 `session`:** a path (`skills/session-kickoff/`) or a transcript session, not a lease, so RH does not bind them.
- **RK in cl26, cl4, cl7, cl37, cl46 and cl47:** none reads or supplies a cadence key, so RK does not bind them.

5. Parent text that looks wrong

- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-8.md:45-46` (`flakes` routed only for a red leg, and wb3:65-68 routes only red bars) contradicts `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-30.md:37-40` and wb8:147-148 (a record per Test-step bar, "thirty verdicts per leg").
- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md:46-47, :183` hand-edits the `tier2-review self-test` guard in `tools/gate-legs.json`, which wb11:43-47 and :73-74 make a render. fh17 states no declaration case.
