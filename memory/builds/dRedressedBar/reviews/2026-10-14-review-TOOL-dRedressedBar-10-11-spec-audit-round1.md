**Serves:** spec-audit TOOL-dRedressedBar-10 TOOL-dRedressedBar-11

# Tier-2 spec audit: build dRedressedBar, units 10 and 11, ROUND 1

*Synthesized 2026-10-14 from five lenses and five skeptic batches. Every item below survived a skeptic told to refute it. Each item gives the address in the spec, the defect, its consequence, the fix with the skeptic's verdict on it, and a left-shift gate.*

**Reviewed subjects, pinned at blob:**

- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md`@`5b0dba25e5c82ee7471600aae6da59ab908f94c4`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md`@`1b4ea08c879530e74bac8e92d11c8b69e95a79ed`

ROUND 1.

## Verdict: CLEAN WITH FIXES

No blocker survived. One high survived: unit 11's refusal on the narrower-apply route lasts one run (H1). Fix it in spec 11 before unit 11 is built. Four items at MEDIUM cover 5 raw confirmed findings. Seventeen items at LOW cover 18 raw confirmed findings. That is 22 items over 24 raw findings, and each finding sits in exactly one item. Fix each medium item in its spec before that unit is built.

## Review shape

Intensity full, raw 24, confirmed 24, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: blocker 0, high 1, medium 4, low 17. By raw confirmed finding: blocker 0, high 1, medium 5, low 18.

**Run integrity.**
- 5 of 5 lenses returned, and none died.
- 5 of 5 skeptic batches returned, and none died.
- Demoted to unverified: 0 contradictory verdicts and 0 orphaned duplicate refutations. Discarded: 0 spurious verdicts. Duplicates: 0.
- Fixes on confirmed findings: 22 judged sound, 2 judged UNSOUND (ids 1 and 8; the skeptics' corrected fixes are written below), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 findings were UNGRADED by the skeptic. 1 was RE-GRADED by the skeptic: id 16, from medium to low.
- Unverified findings: 0 answered UNCERTAIN, and 0 with no usable verdict.
- No lens notes were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: 10 spec documents were supplied as `specs`, as sibling context.
- Checklist: 27 items, each assigned to exactly one of 5 lenses (coherence 6, grounding 6, reuse 5, blast-radius 5, failure-envelope 5).
- By design: none was supplied. There was no caller byDesign, and the block held 0.
- Move check: no checked subject moved.

The run is complete on these counts. The zero blocker count comes from a run in which every lens returned.

## HIGH

### H1. Unit 11's refusal on the narrower-apply route lasts one run, then the false accept returns (id 23)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-11.md` §4 "Which receipt bytes" and the "What an adopter sees change" table, row 1. Also §6 AC3, and S5's [dRB-11] fixture A.
- **What is wrong:** Take a target whose agent-cap hook sits at a home only the receipt records. The first `apply --kits settings-merge` refuses correctly: it exits 1 and names `cannot read`. The same run then still writes `.governance/install.json`. That receipt carries `kits: selection` and only the selection's rows (govkit.py:7393, :8016-8022), so agent-cap's row is dropped. A CONFIGURE refusal only calls `r.fail` and does not return. On the second identical apply, `resolve_kit_dir` finds the hook at neither static home and in no receipt row. The adopter exits 2 before it reads settings.json, the `must_not_resolve` term holds, and the verb exits 0 printing `no-agent-cap-to-wire [accepted stop]`.
- **Consequence:** settings.json stays malformed and the hook stays unwired, while the verb reports success. Unit 11 claims to close "settings-merge's last false-accept route". On this narrow path, which needs a receipt-only hook home plus a narrower apply, the claim misleads. AC3 and fixture A run the apply once after the plant, so both pass over a build that ships this.
- **Fix (judged SOUND):** State the re-run in §4, and close it or hand it off explicitly. To close it, either have a CONFIGURE refusal keep the prior receipt's rows for kits outside the selection, or have a narrower apply carry forward every installed kit's rows, as the `pins` union at govkit.py:7402 already does for kits. If neither is in scope, add a hands-off edge naming the narrower-apply receipt drop as an open false-accept route, and correct the table's "After" cell. In both cases, extend AC3 and fixture A to run the same apply a third time and assert it still exits 1 and prints no `no-agent-cap-to-wire`. The build must also observe that this third run exits 0 over the unfixed design, in a scratch target under %TEMP%.
- **Left-shift gate:** Add a bug-class checklist entry "verdict-printed-before-the-step-that-reverts-it": every refused-stop arm re-runs the same verb once more after the refusal and asserts the refusal holds.

## MEDIUM

### M1. Unit 10 AC5's false-sentence half cannot go red, because spec 8 wraps the sentence across two lines (ids 1, 8)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §6 AC5 (the spec-8 half, line 364), against §2 S5.
- **What is wrong:** AC5 checks that the false sentence is gone with a line-wise `grep -n 'reads none of this file'` over spec 8. Spec 8 wraps that sentence across lines 352-353: "...argv excludes `*.test.sh`, so it reads" / "none of this file." So the grep already prints nothing at HEAD. The only other half needs `scan_spawn_tree` somewhere in the Gates cut.
- **Consequence:** A build can add a sentence naming `scan_spawn_tree` and leave the false sentence in place, and AC5 still passes. S5's in-place correction is then certified when it was never made. That is the exact defect (round-1 ids 5 and 12) this unit exists to close. The effect is contained to one prose correction.
- **Fix (judged UNSOUND; the skeptics' corrected fix):** Join the lines before grepping, so the check sees the wrapped sentence: `sed -n '/^## 6. Gates/,/^## 7/p' <spec8> | tr '\n' ' ' | grep -c 'reads none of this file'` must print 0 at the tip. Record that the same pipeline prints 1 over the pinned spec 8 before the pass. A skeptic re-probed it, and it prints 1 today.
- **Left-shift gate:** Add a spec-lint check: every absence half of an AC must print a match at the pinned blob. Failing that, add a checklist entry: "a line-wise grep for prose must be run against wrapped text; join lines first."

### M2. Unit 10 requires rewriting spec 7's AC4 text, while its own §3, §4 and §5 forbid rewriting a sibling's criteria (id 2)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §2 S9 (lines 92-96), the §4 bump-table row for spec 7 (line 291) and §6 AC9 (line 389). These conflict with §3's first non-goal (line 152), §4 Alternatives row 2 (line 315) and §5 risks (line 329).
- **What is wrong:** S9 renames spec 7 AC4's "each kit that units 1 to 6 moved", and AC9 greps all of spec 7 for `units 1 to 6|six units`, which matches spec 7 line 235 inside its acceptance criteria. Yet §3 excludes "Rewriting a sibling's criteria", §4 rejects in-place criterion rewrites because the ledger would answer text that no longer exists, and §5 says "no criterion text moves, so no ledger is contradicted".
- **Consequence:** A builder cannot satisfy both. Leaving AC4 alone reds AC9. Editing AC4 makes unit 7's acceptance ledger answer reworded text, which is the contradiction §4 and §5 say cannot happen.
- **Fix (judged SOUND):** Pick one. Either drop the AC4 wording from S9 and the §4 table, scope AC9's grep to spec 7's §1, §4 and Edges, and note AC4's stale range only in the revision line. Or state in §3 and §5 that spec 7's AC4 wording is the single criterion edit, and say why its ledger is not contradicted.
- **Left-shift gate:** Add a checklist entry: "an AC that greps a whole sibling spec must exclude that sibling's §6 unless the spec names a criterion edit."

### M3. Unit 11's fixture B rebuilds the vintage rewind by hand instead of calling `write_vintage_receipt` (id 17)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-11.md` §6 AC4 (lines 361-372) and §4 "The witnessing arms" (lines 255-262), fixture B of the [dRB-11] block.
- **What is wrong:** Fixture B plants `scripts/hooks/agent-cap.js` "at the old vintage, with one receipt row at that vintage's identities". The selftest already has `write_vintage_receipt` (tools/govkit/selftest.py:617-673). It writes the bytes and sets `commit`, `sha256` and `gov_oid` at a vintage, and `stale_target` already calls it. The spec names neither.
- **Consequence:** The builder re-derives the identities with a separate `git show` plus `_sha`/`blob_oid`. That duplicates logic whose header records 9 and then 27 arms going red from mixed-vintage rows. A wrong identity sends `update` to the S9 refusal instead of the adopter-exit-2 path, so AC4 can read red for the wrong reason. The extra `git` call would also sit outside `run`, which threatens S6/AC7's pinned selftest.py site counts of 24 and 1. AC4's "Before the commit" is also inexact, because `stale_target` has already settled.
- **Fix (judged SOUND):** State in §4 and AC4 that the block appends the agent-cap row (path `scripts/hooks/agent-cap.js`, source from `resolve_entry`) to the receipt, then re-runs `write_vintage_receipt(govroot, t, OLD)` before `settle`. The helper is idempotent over rows already rewound. Alternatively give `stale_target` an optional row-planting hook that runs before its rewind. Name the helper in the arm's description.
- **Left-shift gate:** Add a checklist entry for the reuse lens: "a fixture that plants a receipt row at a vintage names `write_vintage_receipt`."

### M4. Unit 10's matrix row invites a hand `{prefix}` replace that the resolver idiom-ban leg fires on, and §7 omits that leg (id 18)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §4 "S22 — the false-accept routes, and the narrowing", the matrix-row paragraph (lines 273-276), and the §7 leg line (line 459).
- **What is wrong:** The row's path is described as agent-cap's destination "with settings-merge's `{prefix}` replaced by that prefix's parent". Written as `.replace("{prefix}", …)` in matrix.py, that trips the ban in `python resolver (behaviour + inline parity + idiom ban)` (resolve-python.test.sh:491-507). §7 does not name that leg. Its guard is broad, so the spec-tokens guards join drops it (BROAD_LEG_FLOOR=5).
- **Consequence:** The unit's close reports green, and the red shows only in the full bar, after unit 11 has stacked on top. It is caught before merge.
- **Fix (judged SOUND):** In §4, require the row's path to come from `govkit.resolve_prefix_token(<term>, <parent prefix>)` (the marked canonical copy at tools/govkit/govkit.py:179-190), or from `resolve_tokens` with a parent-prefix context, and never from a hand `.replace`. Add `python resolver (behaviour + inline parity + idiom ban)` to the §7 leg line. Build probe: `git grep -nE "\.replace\([\"'][{]prefix[}]" -- tools/govkit/matrix.py` prints nothing.
- **Left-shift gate:** Have check-spec-tokens flag spec prose saying "`{prefix}` replaced" without naming `resolve_prefix_token` or `resolve_tokens`.

## LOW

### L1. Unit 10 S17's spec-9 half is observed by no criterion (id 3)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §2 S17 (lines 118-122), against §6 AC14 (lines 417-422).
- **What is wrong:** S17 says "Spec 9 carries the same note for `check_outcome_states`". AC14 reads only spec 2's Scope and §7 and symbols.json. AC19 checks only that spec 9's revision line names id 17.
- **Consequence:** Spec 9 can be left without the codebase-map note while every criterion passes.
- **Fix (judged SOUND):** Add an AC14 half that cuts spec 9's §7 with `sed -n '/^## 7. Gates/,/^## 8/p'` and greps for `codebase-map coverage + freshness`, or for wherever the note goes. Show it prints nothing at the pinned blob.
- **Left-shift gate:** Spec lint: each S-paragraph sentence naming a sibling spec maps to an AC that reads that spec.

### L2. Unit 10 AC8's `project-owned` half already passes, on the hands-off line (id 4)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §6 AC8, the `project-owned` half.
- **What is wrong:** `grep -n 'project-owned'` over spec 4 already prints line 56, the hands-off to unit 10 under Edges, which cites `tools/roles/kit.toml:47-48`.
- **Consequence:** That half is green before the build. AC8's red signal rests on its other halves.
- **Fix (judged SOUND):** Cut the non-goal list first: `sed -n '/^## 3. Non-goals/,/^### Edges/p'`, then grep. A skeptic confirmed this reads red today.
- **Left-shift gate:** Same as M1: every AC half must read red at the pinned blob.

### L3. Unit 10 §1 says the findings land on eight specs; they land on nine (id 5)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §1 Goal (line 19), against §4 "The sibling rev bumps" (line 280) and AC19.
- **What is wrong:** The id table, the §4 bump table and AC19 cover specs 1 to 9.
- **Consequence:** Cosmetic. A builder might read the wrong count of rev bumps, but the table and AC19 govern.
- **Fix (judged SOUND):** Change "eight specs" to "nine specs".
- **Left-shift gate:** Checklist entry "two-answers-to-one-question": a stated count must equal its table's rows.

### L4. Unit 11 adds a fourth row element to `check_outcome_states` but leaves the three-element contract stated (id 6)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-11.md` §4 "The witnessing arms" (lines 239-241) and §2 S4 (lines 41-45).
- **What is wrong:** Spec 9 (lines 199-200) and the helper's docstring describe `(label, present paths, expected verdict)` rows. Unit 11 adds an optional path-to-text mapping, written before classifying and deleted after, and names no update to either.
- **Consequence:** The next reader sees a three-element contract while the code takes four. Documentation only.
- **Fix (judged SOUND):** Have S4 state that the docstring records the fourth element. Note in §3 Edges that spec 9's row-shape sentence goes stale, or correct it in place.
- **Left-shift gate:** Checklist entry "a-folded-field-leaves-its-row-shape-docs-behind".

### L5. Unit 11's new key rule has no label format, which can make AC6's `lexicon ` count ambiguous (id 7)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-11.md` §2 S4, against §6 AC6 (lines 380-382).
- **What is wrong:** The key rule records "one label per shipped `[[outcome]]` block" with no format. AC6 requires the two labels opening `lexicon ` to equal unit 10 AC7's pinned pair. A label opening with the entry id, such as `lexicon block code 1 …`, makes three.
- **Consequence:** A natural spelling reds AC6 or makes it ambiguous. Existing rules avoid this with the `accepted stops:` prefix (matrix.py:178-215).
- **Fix (judged SOUND):** Fix the label prefix in S4, e.g. `outcome probe keys: '%s' …`. Alternatively have AC6 match the two pinned lexicon labels exactly.
- **Left-shift gate:** Checklist entry: a new matrix rule states its label prefix.

### L6. Unit 10 AC3's `n` half matches any shell line (id 9)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §6 AC3 (line 354).
- **What is wrong:** The `FOREIGN_PREFIX_PROBE:-0` line must read "`fail` and `n`". Any `if` line contains the letter n (`then`, `echo`), as adopt-agent-instructions.test.sh:19 does.
- **Consequence:** A stop that reports a wrong counter, e.g. `${count:-1}`, passes. Spec 1 S5's counter requirement is not observed.
- **Fix (judged SOUND):** Require the expansions with `grep -F '${n:-'` and `grep -F '${fail:-'` over that line. Keep the case-sensitive `grep -F '${pass'` absence half.
- **Left-shift gate:** Spec lint: flag an AC token of one or two letters matched without anchoring.

### L7. Unit 11 S4's agreement-rule change is observed by no arm (id 10)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-11.md` §2 S4 and §6 AC6 (lines 378-386).
- **What is wrong:** S4 makes `derive_probe_paths` read keys by their `want` through `govkit.OUTCOME_PROBE_KEYS` and claims AC6 observes it. The agreement rule (matrix.py:203-215) reaches only pairs of `ok = true` blocks in one descriptor. settings-merge has one block, so `must_not_resolve` is never in a pair.
- **Consequence:** A build that keeps the typed `must_exist`/`must_not_exist` pair at matrix.py:209 stays green. A later contradicting descriptor goes unseen.
- **Fix (judged SOUND):** Add a staged half to AC6: patch `govkit.read_descriptors` so one descriptor has two `ok = true` blocks, one `must_exist` and one `must_not_resolve` on the same path. Their agreement label must record false. Name it in the §7 matrix `New arm:` line.
- **Left-shift gate:** Checklist entry "observed-by-claim-no-arm-discharges".

### L8. Unit 11 §4 describes a README edit as pending that has already been made (ids 11, 21)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-11.md` §4 "Order, and unit 7" (lines 230-235).
- **What is wrong:** The paragraph says step 7 is added to the build-order region "on the dispatcher's regen", and that the Build-level sentence calling unit 7 "measured last" "has been inexact since unit 10", an edit the dispatcher owes. README.md at 29c72f51a already says units 10 and 11 follow 7 and touch only govkit-exempt files (lines 56-60), and line 125 already lists step 7.
- **Consequence:** A builder or dispatcher acting on the paragraph may duplicate or overwrite a correct README rule. The record misreads, with no effect on behaviour.
- **Fix (judged SOUND):** Restate the paragraph in the past tense, or replace it with a pointer to README.md's Build-level rules, or drop it.
- **Left-shift gate:** Checklist entry "amendment-leaves-its-other-half-standing": when the README edit lands, re-read the specs that called it pending.

### L9. Unit 10's "exactly as wide as unit 9's" claim fails when the target's parent holds `hooks/agent-cap.js` (id 12)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §4 S22, the prefix `.` sentence (lines 261-263). Also `2026-10-14-spec-TOOL-dRedressedBar-11.md` §5 security.
- **What is wrong:** With `prefix = "."`, the parent-home term resolves to `<target>/../hooks/agent-cap.js`. `classify_outcome` (govkit.py:6311-6325) tests it with no containment check, and the resolver's static probes (govkit.py:221) have none either. Containment applies only to receipt rows (:219).
- **Consequence:** If the parent directory holds the hook, units 10 and 11 refuse an exit 2 that unit 9 accepts. This is a spurious failure on an unlikely path. It fails closed, so it is not a false accept.
- **Fix (judged SOUND):** State the condition in unit 10 §4 ("reads absent unless the target's parent directory holds hooks/agent-cap.js"), and in spec 11 §5 (containment covers receipt rows only; the static second probe may leave the tree). Alternatively gate the term on the resolved path staying inside the target.
- **Left-shift gate:** Checklist entry: any probe term with `..` states whether it may leave the target.

### L10. Unit 11's new stderr tail decodes with the host codepage, and the fixtures ran under PYTHONUTF8=1 (id 13)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-11.md` §4 "The refused exit names its reason" (lines 199-201).
- **What is wrong:** CONFIGURE runs with `capture_output=True, text=True` and no encoding (govkit.py:7744). settings-merge writes UTF-8 stderr with an em dash (settings-merge.py:1047, :1058). The spec-time runs had PYTHONUTF8=1 ambient.
- **Consequence:** On a host without UTF-8 mode, the new problem line prints mojibake. AC3 and AC4 match only ASCII `cannot read`, so they pass either way. Display only.
- **Fix (judged SOUND):** State the host dependency in §4, or decode the tail as UTF-8 (this moves the encoding-posture count §4 pins at 36). Alternatively note AC3/AC4 were observed under PYTHONUTF8=1 and add a PYTHONUTF8=0 run to the arm.
- **Left-shift gate:** Checklist entry "fixture-inherits-ambient-machine-state": spec-time measurements record the ambient PYTHONUTF8 and PYTHONIOENCODING.

### L11. Unit 10 S5 claims all six registry classes are observed; AC5 compares five (id 14)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §2 S5 (lines 74-76) and §6 AC5 (lines 359-363).
- **What is wrong:** S5 names six rows at spawn-idiom-sites.txt:214-219 and says the pass is "observed to add no counted site". AC5 leaves out `pure-fn-subst`, counted at 11 for run-gates.test.sh.
- **Consequence:** A new `$(resolve_mp_record …)` substitution moves a row while AC5 reads equal. The fork leg still grades it at the bar.
- **Fix (judged SOUND):** Narrow S5's claim to the five library-free classes, or derive the counts through `scan_spawn_tree` (or give `scan_spawn_file` the library bodies) and compare all six rows.
- **Left-shift gate:** Spec lint: an AC that compares registry rows must cover every row its S-paragraph names.

### L12. Unit 10 says the probe keys have two readers; the matrix class rule is a third (id 15)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §4 S22, the sentence after the toml block (line 261).
- **What is wrong:** "No reader of the probe keys exists outside those two" misses tools/govkit/matrix.py:181-185, which reads `must_exist` in the accepted-stops liveness loop.
- **Consequence:** The design is unaffected, because that reader reads only `must_exist`. The next change that trusts the inventory will miss a reader.
- **Fix (judged SOUND):** Name the class rule at matrix.py:181-185 as a third reader that unit 10 leaves untouched.
- **Left-shift gate:** Checklist entry: a reader inventory cites the `git grep` that produced it.

### L13. Unit 10 AC5 and AC12 re-type the leg's count and comparison instead of reusing its seams (id 16)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §6 AC5 (lines 360-369) and AC12 (lines 405-412), and §10's reuse claim (lines 506-507).
- **What is wrong:** Both ACs count "sites per class from `scan_spawn_file`", whose lists include near misses flagged False. They do not use `build_spawn_measured` (sh_hygiene.py:872-879), `read_registry` (:384) or `check_registry` (:444). A list-length count over run-gates.test.sh gives cat-file 29 and printf-subst 56 against registry rows 25 and 2. Over unattended-build.test.sh, printf-subst has 288 entries but 71 sites.
- **Consequence:** AC5's pinned figure resolves the ambiguity for AC5. AC12's unattended-build half has no pinned figure, so a natural count reads red on a correct build. Effect contained to how one criterion is observed.
- **Severity note:** The finder graded this medium. The skeptic re-graded it low, because the effect is limited to one criterion's observation, and that binding grade holds here.
- **Fix (judged SOUND):** Shape `scan_spawn_file`'s output as `scan_spawn_tree` does, `(rel, line, site, code)` tuples, then pass it through `build_spawn_measured`. Compare that with `read_registry(memory/project/spawn-idiom-sites.txt, SPAWN_KEY_SHAPE)` through `check_registry`, keyed on the named files, and expect no problems. At minimum, state that only entries whose is-site flag is True count. Correct §10 to name these seams.
- **Left-shift gate:** Checklist entry for the reuse lens: an AC reusing a leg's classifier also reuses its counter and comparator.

### L14. Unit 10 §7 omits `spec tokens` and `encoding posture` (id 19)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-10.md` §7 leg line (line 459).
- **What is wrong:** Both legs are unguarded, so the join never adds them. `spec tokens (a spec's own names resolve)` grades the nine rewritten sibling specs, including new hands-off lines and the new `kit.toml:40-41` and `registry.toml:295-297` cites. `encoding posture (text IO names its encoding)` grades matrix.py. That half is weaker, because S22 adds one row through unit 9's helper.
- **Consequence:** A missing hands-off payload or a cite past end of file shows only in the full bar.
- **Fix (judged SOUND):** Add both legs to §7's leg line. Unit 11's §7 already names the second for the same files.
- **Left-shift gate:** Have check-spec-tokens require every unguarded leg whose subject the spec's Files touched names.

### L15. Unit 11 omits its acceptance ledger from Files touched, so §7 misses `recall floor` and `memory hygiene` (id 20)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-11.md` §4 "Files touched (estimate)" (lines 279-284) and §7 (line 400).
- **What is wrong:** §6 defines `<p11>` through "their acceptance ledgers" (lines 325-326), so the pass writes a ledger under memory/. Files touched lists only four tools/govkit files.
- **Consequence:** A malformed ledger goes ungraded at the unit's close. The full bar catches it. Unit 10 names its ledger and both legs.
- **Fix (judged SOUND):** Add `memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-11-1-acceptance-ledger.md` to Files touched, and add `recall floor` and `memory hygiene` to §7, as spec 10 does at :308 and :459.
- **Left-shift gate:** Spec lint: a spec that names an acceptance ledger lists it in Files touched.

### L16. No unit updates the settings-merge code-2 block's comment after its probe changes (id 22)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-11.md` §2 S2 (lines 33-35), with `2026-10-14-spec-TOOL-dRedressedBar-10.md` §2 S22.
- **What is wrong:** Unit 9 ships the block "with a comment stating why" one `must_not_exist` term suffices. Unit 10 adds a second term and unit 11 a receipt term. S2 says "Nothing else in the descriptor moves".
- **Consequence:** The comment describes a one-term probe. Comment only.
- **Fix (judged SOUND):** In unit 11 S2 (or unit 10 S22), name the block comment as updated to state the three-term probe and its receipt reading. Add an AC1 line grepping the comment for `must_not_resolve` or the receipt.
- **Left-shift gate:** Checklist entry: a change to a probe updates the comment that justifies it.

### L17. Unit 11's security line prices one adopter's stderr; the tail now reaches every adopter (id 24)

- **Where:** `2026-10-14-spec-TOOL-dRedressedBar-11.md` §5 security (lines 302-306), with §2 S3.
- **What is wrong:** §5 reasons only about settings-merge's stderr. The §4 table applies the tail to "any other refused adopter exit in either loop": 14 bash adopters. Some echo target conf values, e.g. adopt-memory-tree.sh:35's `$KIT_REL` and adopt-roles.sh:164's render-token message.
- **Consequence:** The security statement covers less than the change. The values found are paths, not secrets.
- **Fix (judged SOUND):** Restate §5 over the class: every adopter that CONFIGURE or the gained loop runs can print up to three stderr lines on a refused exit, as the regenerate site already does. Either confirm by a grep of the adopters' `>&2` lines that none echoes a secret-bearing value, or state that the tail is printed verbatim from target-side code.
- **Left-shift gate:** Checklist entry: a security line names the full set of producers whose output the change exposes.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=24 confirmed=24 refuted=0 unverified=0 blocker=0 high=1 medium=5 low=18 agents=11 out-tokens=203596

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 6 AC5 (the spec-8 half), against section 2 S5 | medium | medium | confirmed | Re-probed. Spec 10 hashes to the pinned blob 5b0dba25. In spec 8 the sentence wraps across lines 352-353: 'excludes `*.test.sh`, so it reads' / 'none of this file.' `grep -n 'reads none'` over spec 8 matched only line 62, the hands-off text 'reads none of `tools/run-gates/run-gates.test.sh`'. So AC5's `grep -n 'reads none of this file'` already prints nothing at HEAD. That half of AC5 cannot go red. The other half needs only `scan_spawn_tree` somewhere in the Gates cut, so a build could add that name and leave the false sentence in place. The consequence is contained: one prose correction is certified falsely, and no product behaviour changes. | unsound | fixture-passes-by-finding-nothing |
| 2 | coherence | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 2 S9 and section 6 AC9, against section 3 first non-goal, section 4 Alternatives row 2 and section 5 risks | medium | medium | confirmed | Confirmed by reading spec 10. S9 (lines 92-96) renames AC4's 'each kit that units 1 to 6 moved'. The §4 bump table row for spec 7 (line 291) lists 'AC4 wording'. AC9 (line 389) greps all of spec 7 for 'units 1 to 6\|six units'. Spec 7 line 235, inside its §6 Acceptance criteria, matches that grep. Against this: §3 line 152 lists 'Rewriting a sibling's criteria' as a non-goal, §4 line 315 rejects rewriting a criterion in place because of the ledger, and §5 line 329 says 'no criterion text moves, so no ledger is contradicted'. The spec contradicts itself. A builder cannot satisfy AC9 without breaking the §3 and §5 invariant. | sound | - |
| 3 | coherence | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 2 S17 (the spec-9 half) against section 6 AC14 | low | low | confirmed | S17 (lines 118-122) says 'Spec 9 carries the same note for `check_outcome_states`'. AC14 (lines 417-422) reads only spec 2's Scope, spec 2's §7 and symbols.json. AC18 reads spec 9's §4 and §5 for the routes and unit 11, not for a map note. AC19 checks only that the revision line names the id. A grep of spec 9 for 'codebase-map' found nothing. Its §7 gates (line 317) carry no codebase-map leg. The only staleness mention is inside the hands-off to unit 10 at line 78. So the spec-9 half of S17 is observed by no criterion. | sound | - |
| 4 | coherence | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 6 AC8, the `project-owned` half | low | low | confirmed | `grep -n 'project-owned'` over spec 4 printed only line 56. That line is in the hands-off to TOOL-dRedressedBar-10 under Edges and already cites `tools/roles/kit.toml:47-48`. So AC8's 'prints the corrected non-goal' half is satisfied today. Cutting the section with `sed -n '/^## 3. Non-goals/,/^### Edges/p'` and grepping it printed no 'project-owned' line. It printed only line 44, which holds the base sentence 'from the roles kit'. So the proposed cut tells the corrected non-goal apart from the hands-off line, and it would read red today. | sound | fixture-passes-by-finding-nothing |
| 5 | coherence | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 1 Goal, against section 4 'The sibling rev bumps' and AC19 | low | low | confirmed | Spec 10 line 19 says 'The findings land on eight specs'. Its id table assigns findings to units 1, 2, 3, 4, 5, 6 (id 14), 7, 8 and 9, which is nine. Line 280 itself says 'Each of the nine sibling specs', the §4 table lists specs 1 to 9, and AC19 says 'each of specs 1 to 9'. The miscount is cosmetic: the table and AC19 govern the bumps. | sound | two-answers-to-one-question |
| 6 | coherence | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 4 'The witnessing arms' and section 2 S4 | low | low | confirmed | Spec 9 lines 199-200 state the row contract as '(label, present paths, expected verdict)' rows. Spec 11 §4 'The witnessing arms' (lines 239-241) adds an optional fourth element, a path-to-text mapping that is written before classifying and deleted after. Neither S4 (lines 41-45) nor the non-goal at lines 59-61 says that the helper's docstring or spec 9's sentence gets updated. The stale three-element contract is real, but it affects documentation only. | sound | a-folded-field-leaves-its-row-shape-docs-behind |
| 7 | coherence | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 2 S4 (the new key rule) against section 6 AC6 | low | low | confirmed | Spec 11 AC6 (lines 380-382) requires 'one label per shipped [[outcome]] block' from the key rule, and requires that 'the two labels opening `lexicon `' equal unit 10's pinned pair. S4 gives the key rule no label format. In matrix.py:178-215 the existing class and agreement labels open 'accepted stops:', and only line 240's engine-agrees labels open 'lexicon '. A key-rule label that starts with the entry id, for example 'lexicon block code 1 ...', would make three labels open 'lexicon ', and AC6's count would be ambiguous or red. This is an underspecified label, and its effect is contained. | sound | - |
| 8 | grounding | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 6 AC5 (and S5) | medium | medium | confirmed | Spec 8 at HEAD splits the sentence across lines 352-353: line 352 ends '...the fork leg's argv excludes `*.test.sh`, so it reads' and line 353 begins 'none of this file.' A line-wise `grep -n 'reads none of this file'` therefore matches nothing even before any correction, so the 'false sentence stands' red case of spec 10 AC5 (line 364) can never fire. Only the scan_spawn_tree half is left, and it says 'in the corrected sentence', which is a judgment call rather than a mechanical check. | unsound | - |
| 9 | grounding | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 6 AC3 | low | low | confirmed | adopt-agent-instructions.test.sh:19, the shape unit 1 copies, contains the letter n in 'then', 'echo' and 'assertions'. Any such `if` line therefore satisfies 'reads `fail` and `n`' (spec 10 AC3, line 354) whatever counter it actually uses. Spec 1 S5 (lines 123-124) requires the counters `fail` and `n`, and that requirement is not observed. Only the `pass` absence half can red. | sound | - |
| 10 | grounding | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 2 S4 / section 6 AC6 | low | low | confirmed | matrix.py:203-215 reaches derive_probe_paths only for pairs of ok=true blocks within one descriptor. settings-merge.kit.toml at HEAD has no outcome block (grep found nothing), and units 9-11 give it exactly one block, so must_not_resolve never takes part in a pair. AC6 (lines 378-386) checks only that every label is true, plus the key-rule and receipt-row halves of the must_not_resolves rename. Nothing in it exercises the agreement rule's union by `want`, so a build that keeps the typed must_exist/must_not_exist pair at line 209 stays green. | sound | observed-by-claim-no-arm-discharges |
| 11 | grounding | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 4 'Order, and unit 7' | low | low | confirmed | Spec 11 at blob 1b4ea08 §4 'Order, and unit 7' (lines 230-235) says the order 7 'adds step 7 to the derived build-order region on the dispatcher's regen', and that the Build-level sentence calling unit 7 'measured last over the code the others leave' 'has been inexact since unit 10. It should say ... The dispatcher owns that README edit.' Both are written as pending. The README at HEAD (29c72f51a, the same commit that adds this blob) already carries both changes. Lines 56-60 read '7, ... is measured over the code units 1 to 6, 8 and 9 leave. Units 10 and 11 follow 7 in that order. Each touches only govkit-exempt files and adds no function'. Line 125 holds '\| 7 \| `TOOL-dRedressedBar-11` \| no \|'. grep for 'is measured last' finds nothing. The spec describes a README edit that has already been made. The only effect is on how the record reads. | sound | amendment-leaves-its-other-half-standing |
| 12 | grounding | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 4 'S22 — the false-accept routes, and the narrowing' (prefix `.` sentence); also spec 11 section 5 security | low | low | confirmed | Spec 10 §4 S22 (lines 261-263) says without condition that with prefix `.` the new term 'resolves outside the target and reads absent there, which leaves the stop exactly as wide as unit 9's'. classify_outcome (govkit.py:6311-6325) evaluates `(target / resolved).exists()` with no containment check, so `./../hooks/agent-cap.js` reads whatever sits in the target's parent directory. The resolver's static probes, `probes = (here / home, here.parent / home)` at govkit.py:221, also have no containment check; containment is applied only to receipt rows (:219). If the parent holds hooks/agent-cap.js, settings-merge.py:213-223 hits `except ValueError: pass` and falls back to a path that does not exist, so main refuses with exit 2 (:1046-1052). Unit 9's block accepts that exit and unit 10's refuses it, so the claim that the stop is exactly as wide as unit 9's is false on that edge path. Spec 11 §5 itself is literally accurate about receipt rows, but it says nothing about the static probe leaving the tree. The failure is fail-closed and the path is unlikely. | sound | - |
| 13 | grounding | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 4 'The refused exit names its reason' | low | low | confirmed | govkit.py:7744 runs CONFIGURE as `subprocess.run(..., capture_output=True, text=True)` with no encoding. Spec 11 §4 (line 199-201) keeps it that way and will print the stderr tail. settings-merge.py:1058 reconfigures stderr to UTF-8, and its refusal text contains an em dash (:1047). The ambient env here prints PYTHONIOENCODING=utf-8 and PYTHONUTF8=1, so the spec's fixture runs would not see a locale-codepage decode. Without UTF-8 mode on Windows, text=True decodes as cp1252, so non-ASCII text in the tail prints as mojibake. AC3/AC4 match only ASCII 'cannot read' and pass either way. The decode already happens at HEAD, so the new code adds no crash path; the effect is display only. | sound | fixture-inherits-ambient-machine-state |
| 14 | grounding | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 2 S5 / section 6 AC5 | low | low | confirmed | sh_hygiene.py:600-609 registers six classes, pure-fn-subst included. spawn-idiom-sites.txt has `tools/run-gates/run-gates.test.sh	pure-fn-subst	11 ... resolve_mp_record×11` beside the other five rows. Spec 10 S5 (line 74-76) names 'the six rows at spawn-idiom-sites.txt:214-219' and says 'Unit 8's pass is observed to add no counted site. Observed by AC5'. AC5 (lines 359-363) compares only cat-file, date-fmt, path-subst, printf-subst and var-pipe, and its figure lists five numbers. So S5's 'observed' claim covers one class that AC5 never reads. The fork leg still grades the class at the bar, which contains the effect. | sound | - |
| 15 | grounding | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 4 'S22', the sentence after the toml block | low | low | confirmed | Spec 10 line 261 says 'No reader of the probe keys exists outside those two' (classify_outcome, and derive_probe_paths in the agreement rule). `git grep must_exist\|must_not_exist` excluding toml shows tools/govkit/matrix.py:181-185. In the accepted-stops liveness loop, that code reads `probe = b.get("probe")` and checks `bool(probe.get("must_exist"))`, outside derive_probe_paths. That is a third reader. It reads only must_exist, which unit 10 leaves alone, so the design is unaffected. The inventory is still wrong and could mislead the next change. | sound | - |
| 16 | reuse | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 6 AC5 and AC12 (and section 10's claim that AC5 and AC12 reuse the leg) | medium | low | confirmed | Re-probed with a scratch program, verify-b4/s.py, that imports sh_hygiene and calls scan_spawn_file at HEAD. For run-gates.test.sh it printed (all, is-site): cat-file (29,25), printf-subst (56,2), path-subst (12,12), date-fmt (1,1), var-pipe (141,141). For unattended-build.test.sh it printed printf-subst (288,71) and var-pipe (70,70). The registry rows at spawn-idiom-sites.txt:214-219 are 25/1/12/2/141. scan_spawn_file (sh_hygiene.py:798-818) does return near misses with the flag False, and build_spawn_measured (:872-879) counts only `if site:`. AC5 (spec 10:360-369) and AC12 (:405-412) name only scan_spawn_file. Neither says to count only flagged entries or to use build_spawn_measured or check_registry. Section 10 (:506-507) claims reuse. The ambiguity is partly resolved for AC5: §4 evidence (:212-214) and AC5's figure pin 25/1/12/2/141, which only the is-site count gives. AC12's unattended-build half is DERIVED with no pinned figure, so a list-length count would read red there on a correct build. The effect is contained to how one criterion is observed, so I grade it low. | sound | - |
| 17 | reuse | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 6 AC4 and section 4 'The witnessing arms' (fixture B of the [dRB-11] block) | medium | medium | confirmed | selftest.py:617-673 write_vintage_receipt sets commit, sha256 (gk._sha) and gov_oid (gk.blob_oid) at the vintage, and writes the bytes. stale_target (:3237-3249) calls it, then settle. Spec 11 AC4 (:361-372) and §4's witnessing-arms paragraph (:255-262) ask for a hand-planted agent-cap row 'at that vintage's identities'. They name make_target/settle/stale_target/run and never the rewind helper. §4 also requires that the block's 'process calls go through run', and run invokes govkit, not git. Planting old-vintage bytes without the helper therefore needs a separate git read plus identity derivation, which duplicates the logic whose header records that 9 and then 27 arms went red. I checked feasibility: OLD resolves to 24f39915, and `git cat-file -e 24f39915:tools/hooks/agent-cap.js` succeeds, so the helper would keep the row rather than drop it. One part of AC4 is also inexact: it says 'Before the commit', but stale_target has already settled. The fixture duplication is real and its effect is contained to a test fixture. | sound | - |
| 18 | blast-radius | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 4 'S22 — the false-accept routes, and the narrowing' (the matrix-row paragraph) and section 7 | medium | medium | confirmed | Spec 10:273-276 says the row's path is agent-cap's destination 'with settings-merge's `{prefix}` replaced by that prefix's parent'. That wording directs a hand replacement of the token. resolve-python.test.sh:491-507 scans every tracked *.py and fires on `\.replace\(["'][{]prefix[}]` outside a `# >>> resolve_prefix_token` block. The marked canonical copy is at govkit.py:179-190. gate-legs.json:304-314 gives that leg the guard ["{prefix}/","{prefix}/lib/",".githooks/"]. check-spec-tokens.py:262 sets BROAD_LEG_FLOOR=5, and derive_guarded_legs (:506-523) drops broad guards from the join, so the join cannot ask for this leg. Spec 10 §7 (:459) omits it. The literal build would pass the unit's close and red only in the full bar. The red is caught before merge, so the effect is contained. | sound | - |
| 19 | blast-radius | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:section 7 Gates leg line | low | low | confirmed | I read gate-legs.json. `spec tokens (a spec's own names resolve)` and `encoding posture (text IO names its encoding)` both carry no guard key. Spec 10 §7 (:459) names neither leg, although the unit rewrites nine sibling specs and adds new hands-off lines and cites that spec tokens' handoff and cites joins grade. For encoding posture, spec 10 says little about any new text IO in matrix.py: S22 adds one row, through unit 9's helper. So that half is weaker, but the spec-tokens omission stands. The consequence is a later red in the full bar, not a shipped defect. | sound | - |
| 20 | blast-radius | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 4 'Files touched (estimate)' and section 7 | low | low | confirmed | Spec 11:325-326 defines <p11> as the commit of unit 11's build pass 'as their acceptance ledgers name them', so the pass writes a ledger. Files touched (:279-284) lists only the four tools/govkit files. §7 (:400) names `recall floor arms` but neither `recall floor` nor `memory hygiene`. gate-legs.json shows `recall floor` guarded by 'memory/' and `memory hygiene` unguarded. Spec 10, by contrast, lists its ledger (:308) and both legs (:459). The effect is a missed check at the unit's close, caught by the full bar. | sound | - |
| 21 | blast-radius | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 4 'Order, and unit 7', last paragraph | low | low | confirmed | I read README.md lines 56-60. They already say: "Units 10 and 11 follow 7 in that order. Each touches only govkit-exempt files and adds no function, so neither moves a kit version or the symbol index unit 7 regenerates." Spec 11 lines 231-235, at blob 1b4ea08, still say the sentence "has been inexact since unit 10" and that "The dispatcher owns that README edit". So the spec describes an edit that has already been made. That is a stale statement in the build's own record and has no effect on behaviour. | sound | - |
| 22 | blast-radius | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 2 S2 (with spec 10 section 2 S22) | low | low | confirmed | Spec 9 S1 (lines 26-29) ships the code-2 block "with a comment stating why", and that block has one must_not_exist term. Spec 10 S22, at blob 5b0dba2, adds a second term and a matrix row. Grepping spec 10 for 'comment' finds nothing about the descriptor comment. Spec 11 S2 (lines 33-35) adds must_not_resolve and says "Nothing else in the descriptor moves". Its only 'comment' hit is unrelated. Neither spec updates the comment, so it will describe a one-term probe after two units have changed it. The effect is limited to a comment. | sound | - |
| 23 | failure-envelope | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 4 "Which receipt bytes" and "What an adopter sees change" row 1; section 6 AC3; S5 ([dRB-11] fixture A) | high | high | confirmed | I checked this against the code. The claim holds. At govkit.py:1094-1102, `--kits` mode returns only the named kits through derive_install_order, and settings-merge.kit.toml has requires = []. `rows` starts empty at :7393 and is filled only from `for eid in selection`. The one carry-forward at :7582-7593 copies adopter-owned rows for the selection's own destinations only. In the CONFIGURE block (:7744-7772) a non-accepted non-zero exit only calls r.fail. Grepping :7440-8020 for return or raise finds none, so the receipt write at :8016-8022 still runs, with "kits": selection and "files": rows. That drops agent-cap's row. resolve_kit_dir (:196-230) finds a renamed home only through a receipt row, and its static probes are here/hooks and here/../hooks. On the second identical apply, settings-merge.py:1046-1052 therefore returns 2 before it reads settings.json. The must_not_resolve term holds and the stop is accepted, while the settings.json is still malformed. Spec 11 AC3 and the [dRB-11] fixture A run the apply once after the plant, so they cannot catch this. This happens only on a narrow path: a receipt-only hook home plus a narrower apply. The unit's claim to close the last false-accept route therefore misleads, which is why I grade it high. | sound | verdict-printed-before-the-step-that-reverts-it |
| 24 | failure-envelope | memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md:section 5 security; S3 | low | low | confirmed | Spec 11 section 5 security (lines 302-306) checks only the content of settings-merge's stderr: "settings-merge's stderr carries paths and parse positions, never settings values". The section-4 table's last row applies the stderr tail to "any other refused adopter exit in either loop". tools/memory-tree/adopt-memory-tree.sh:35 echoes the computed '$KIT_REL' to stderr, and tools/roles/adopt-roles.sh:164 echoes a render-token message. The security statement therefore covers less than the change does. The values I found are paths, not secrets, so the effect is contained and I grade it low. | sound | - |
