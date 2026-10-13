**Serves:** diff-review TOOL-dSweptBranches-19 TOOL-dSweptBranches-20 TOOL-dSweptBranches-21

# Tier-2 diff review — dSweptBranches follow-up (TOOL-dSweptBranches-19 to -21), round 1

*Provenance: synthesized from a bounded `tools/workflows/tier2-review.js` run. Three lenses each found candidates, and an adversarial skeptic tried to refute every finding. This record was written by the synth agent on 2026-10-13. Round 1.*

Reviewed range: 942b587e03ae3f7f0e31eacaf1e1aff99f84a5cc...d8c538c7ca14854542f9a9bd4880391aaab4fd73

## Verdict: CLEAN WITH FIXES

There are no blockers. The one high is the stranded `/branch-reconcile` render. Spec 19 says `govkit update` moves an adopter's copy, and it does not. Every adopter that updates keeps a duplicate, ungated skill beside the new `/cleanup`, and the spec tells the next change that this case is already handled. The process-monitor findings are coverage gaps and log text. No shipped verdict is wrong today.

## Review shape

Review shape: intensity light, raw 14, confirmed 10, refuted 4, unverified 0 (0 uncertain), precision 0.71.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 5 | 2 | 3 | 0 | 0 | 0.40 |
| seams | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| verification | yes | 5 | 4 | 1 | 0 | 0 | 0.80 |

The adjudicated tally is 7 items by item: 0 blocker, 1 high, 4 medium, 2 low. By raw confirmed finding it is 10: 0 blocker, 1 high, 5 medium, 4 low. Findings of one binding grade that name one defect were merged: ids 1 and 10 into one medium item, and ids 5, 9 and 14 into one low item. Id 6 names the same defect as 1 and 10, but it holds a binding high, so it stays a separate item.

### Run integrity

- Lenses: 3/3 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 7 judged sound, 3 judged UNSOUND, 0 with no fix proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 2 RE-GRADED by the skeptic (ids 10 and 12).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intensity: **light**. The security and intent lenses were NOT run. Their classes were swept only through the checklist shares. This is not a full review, and a zero in either of those classes is not evidence of absence.
- Intent: 3 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 15 items, each assigned to exactly one of 3 lenses: correctness 5, seams 5, verification 5.
- By design: none was supplied. There was no caller byDesign and no block.

No lens or skeptic batch died, so the confirmed set is complete for the three lenses that ran. It is still not complete for the review as a whole, because the run was light.

## Findings

### HIGH

#### H1 — The renamed skill strands the adopter's old render, and spec 19 says govkit moves it (id 6)

- **Ref:** [tools/branch-reconcile/kit.toml:32](../../../../tools/branch-reconcile/kit.toml), with the false claim in spec 19 §4 (lines 68-69) and its risks and migration lines (line 85).
- **Lens:** seams, class `shipped-checker-edit-is-an-adopter-contract-change`. The binding grade is high, and the skeptic also graded it high.
- **Defect:** The rendered row's `to`, the outcome probe, the LF pin and the shipped `gate_leg` name all move from `branch-reconcile` to `cleanup`. govkit's rename path keys on `renames.get(row['source'])`, through `derive_rename_map` and `resolve_renamed` (govkit.py ~8399 and ~9196). The source, `tools/branch-reconcile/SKILL.template.md`, did not move, so the old receipt row never becomes `renamed`.
- **Why the old copy survives:** Even a `renamed` rendered row would only be reported, never written (govkit.py ~10124-10133). The row's role re-resolves to None, it grids to stale, and it is capped to `re-rendered` (~9607). `[[regenerate]] --scaffold` then writes only `.claude/skills/cleanup/SKILL.md`.
- **Consequence:** Every updating adopter of branch-reconcile@1.3 keeps `.claude/skills/branch-reconcile/SKILL.md`, which still carries `name: branch-reconcile` and the same triggers. It sits beside `/cleanup`, and no gate watches it:
  - `--check` reads only the new path.
  - The descriptor's LF pin no longer names the old path.
  - The old copy is never re-rendered when the template changes.
- **Manifest side effect:** The adopter's manifest keeps its `branch-reconcile skill wiring` leg row. A second `cleanup skill wiring` row arrives as an order with the same argv.
- **Why high:** Spec 19's §4, risks and migration lines say the opposite, which will mislead the next change. That is the rubric's high.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):**
  - Do not have `--scaffold` silently delete or `git mv` the old render.
  - Add a WIRE-INTO-PROJECT maintenance entry for this kit vintage with these manual steps:
    1. `git rm .claude/skills/branch-reconcile/SKILL.md`.
    2. Remove its receipt row, or run `govkit adopt --re-adopt` so the receipt records `.claude/skills/cleanup/SKILL.md` instead.
    3. Rename the manifest's `branch-reconcile skill wiring` leg row to `cleanup skill wiring` instead of adding a second one.
    4. Change the `.gitattributes` LF pin to the new path.
  - Optionally, have `--check` fail and name these steps while the old path still exists.
  - Correct spec 19 §4 and its risks and migration lines to say that update does NOT move a rendered destination whose source is unchanged.
  - Ids 1 and 10 carry a different corrected fix for the same defect. Reconcile the two at the fix: see M1.
- **Left-shift gate:** Add a govkit selfcheck over the diff of every shipped `kit.toml`. A `[[rendered]]` (or any written) row whose `to` changed while its `from` did not must be matched by one of two things: a WIRE-INTO-PROJECT maintenance entry naming the old destination, or a kit-side withdrawal of it. Run the predicate over the tree's history first to confirm it fires on this commit and on nothing already handled.

### MEDIUM

#### M1 — Same defect, medium angle: no check covers the stranded render, and the spec's claim is false (ids 1 and 10)

- **Ref:** [tools/branch-reconcile/kit.toml:32](../../../../tools/branch-reconcile/kit.toml).
- **Lenses:** correctness (id 1), and verification (id 10, class `a-spelling-change-strands-its-readers`).
- **Mechanism:**
  - `classify_row` takes a rename only when `t_state == "absent"` (govkit.py 8536-8537).
  - `resolve_renamed` returns None unless `renames.get(row['source'])` is set (9218-9223).
  - Neither condition holds, because only `to` changed.
  - The old row's `now` is None (9315-9317), so it stays a `rendered`/adopter row and is graded, not moved.
  - `--scaffold` renders a second copy at `cleanup/`, and nothing unlinks the old path.
  - branch-reconcile is a registry entry (registry.toml:95), so adopters exist.
  - Every gate named in spec 19 §7 runs against gov's own tree, where the move was a `git mv`. All of them stay green.
- **Grades:** The binding grade is medium for both ids. The finder graded id 10 high, and the skeptic re-graded it medium. The leftover is a duplicate skill that still routes to the same, unmoved CLI. Only adopters who installed between TOOL-dSweptBranches-5 and this change are affected, and the false claim sits in a closed spec. The mislead-the-next-change consequence is carried at high by H1. I see no reason to depart from the binding grades.
- **Fix:** The two ids carry different fix judgments.
  - Id 1, finder's fix UNSOUND. The skeptic's corrected fix:
    - Have `--scaffold` delete the old render with a plain `rm`, not `git rm`. It does this only when the file carries the kit's render marker and `name: branch-reconcile`.
    - Otherwise `--scaffold` prints the file as a leftover the operator must remove.
    - Make `--check` exit non-zero while `.claude/skills/branch-reconcile/SKILL.md` exists.
    - Have `govkit update` report a `rendered` receipt row whose destination the descriptor no longer resolves as withdrawn, and drop that row, so the receipt stops tracking a deleted path.
    - Correct spec 19 §4/§5 to say the move is the kit's job, not govkit's rename path.
  - Id 10, judged SOUND:
    - Add a govkit selftest arm with a fixture adopter whose receipt holds a rendered row at the old `to`.
    - Update that adopter to a descriptor whose `to` changed while the source stayed put.
    - Assert the old file is moved or withdrawn, not left behind.
    - If govkit cannot do this, make `adopt-branch-reconcile.sh --check` (or `--scaffold`) refuse while the old path still exists.
    - Either way, correct spec 19's claim.
  - Reconciling with H1: H1's corrected fix forbids a silent delete by `--scaffold`. Id 1's corrected fix allows a guarded, marker-checked `rm`. The common ground of all three corrected fixes:
    - `--check` reds while the old path exists.
    - The receipt row is dropped or re-adopted.
    - Spec 19 is corrected.
    - The id-10 selftest arm pins the behaviour.
  - Whether `--scaffold` removes the file itself is the open choice. Make it once, at the fix.
- **Left-shift gate:** The id-10 govkit selftest arm is the gate for this class: a rendered `to` that moves while its source stays put must not leave the old destination on disk unreported. Observe the arm red against this commit before the fix lands.

#### M2 — `backstopped` is computed and returned, and nothing reads or asserts it (id 7)

- **Ref:** [tools/process-monitor/reap.py:272](../../../../tools/process-monitor/reap.py).
- **Lens:** seams, class C11 `observed-by-claim-no-arm-discharges`. The binding grade is medium.
- **Defect:** `run_kill` appends to `backstopped` (:240) and returns it (:272). Nothing else reads it:
  - `render_kill` does not print it.
  - Neither `tree-killed` health event (~:378, ~:468) carries it.
  - `run_sweep`'s counts and the `--kill` output ignore it.
  - The AC2 arm `test_msys_signal_is_backstopped_by_winpid` (selftest.py:742-768) never asserts `rep['backstopped']`.
- **Consequence:** Spec 21 S2 says AC2/AC3 observe the field. In fact it can be dropped or mis-populated while every arm stays green, and an operator never sees which members needed the winpid backstop.
- **Lost error text:** When both the MSYS signal and the taskkill fail with a non-gone error, `done` stays the MSYS result (243-245). Only the MSYS blob reaches `errors`, and the taskkill's message is lost.
- **Why medium:** Kill behaviour is unaffected, and the census still grades survival.
- **Fix (judged SOUND):**
  - Render the field in `render_kill`, for example `· backstopped %d`, plus the backstop's own message when it failed.
  - Carry the count into the health event.
  - Add `sorted(rep['backstopped']) == [1, 2, 4]` to the AC2 arm's checked tuple.
- **Left-shift gate:** Add a checker over `tools/process-monitor/reap.py`: every key in the dict that `run_kill` returns must be read by `render_kill` or a health event, AND must be named in at least one selftest assertion. Run the predicate over the current tree first. It should flag `backstopped` and nothing else, or list the other offenders before it is armed.

#### M3 — Spec 21 §7 declares an AC1 arm with a staged five-second delay, and no shipped arm stages one (id 8)

- **Ref:** [memory/builds/dSweptBranches/spec/2026-10-13-spec-TOOL-dSweptBranches-21.md:110](../spec/2026-10-13-spec-TOOL-dSweptBranches-21.md).
- **Lens:** seams, class `observed-by-claim-no-arm-discharges`. The binding grade is medium.
- **Defect:** §7 says an arm in `tools/process-monitor/selftest.py` covers AC1 with "a five-second delay staged in the tree's body". The live arm's body (selftest.py ~1131-1141) stages no delay, and grep finds no `sleep 5`. AC1 was evidenced by a scratch edit whose bytes were restored, per the ledger.
- **Consequence:** AC1's red-when is "the poll is replaced by the fixed wait", and no shipped arm enforces it. Restoring `time.sleep(3)` would stay green on almost every run, because the undelayed tree usually spawns in under 3 s.
- **Refuted counterpart:** Id 11 made the related claim that the `New arm:` field promises a permanently staged condition. The skeptic refuted it on TEMPLATE-SPEC.md:280. Id 8 survives on a different ground: no shipped arm can fail when the poll regresses to the fixed wait.
- **Fix (judged SOUND):** Either of these:
  - Add an arm, or a parameter of the live arm, that stages `sleep 5;` ahead of the members in the body and asserts the poll still finds the whole tree.
  - Amend §7 and AC1 to say AC1 was observed by hand and no arm discharges it.
- **Left-shift gate:** Add a spec-tokens check over §7 `New arm:` lines whose staging field names a condition ("a ... delay staged", "staged in the body"). The named arm must contain a literal for that staging in the shipped bytes, or the line must be marked observed-by-hand. If the predicate is too fuzzy to gate, add this to the project's bug-class checklist under `observed-by-claim-no-arm-discharges`.

#### M4 — The backstop's two non-landing outcomes have no arm that can fail (id 13)

- **Ref:** [tools/process-monitor/reap.py:244](../../../../tools/process-monitor/reap.py).
- **Lens:** verification. The binding grade is medium.
- **Defect:** The new branch is `if done.returncode != 0 and (backstop.returncode == 0 or check_gone_blob(backstop)): done = backstop`. Only the `backstop.returncode == 0` disjunct is exercised, because the AC2 stub returns rc 0 for every taskkill. Two cases have no arm:
  - MSYS is refused and the backstop reports "not found". The member should land in `already_gone`.
  - MSYS is refused and the backstop also fails. The member should land in `errors`.
- **Source grep proves nothing:** `test_already_gone_is_not_a_signal_error` (selftest.py:779) only greps reap.py for `already_gone` and `not found`. Since `not found` now lives in `check_gone_blob`, the grep stays green whether or not either call site uses the helper.
- **Consequence:** Three edits each leave the suite green:
  - Dropping the gone disjunct.
  - Swapping which result replaces `done`.
  - Losing the backstop's error text.
- **Why medium:** No defect in today's logic was found. The effect is untested new code.
- **Fix (judged SOUND):**
  - Extend the stubbed arm, or add one, with three refused members:
    - backstop rc 0;
    - backstop rc 128 with `ERROR: The process "N" not found.`;
    - backstop rc 1 with `Access is denied`.
  - Assert they land respectively in neither list, in `already_gone`, and in `errors`.
  - Replace the source-grep arm with a behavioural one.
- **Left-shift gate:** Add a selftest-lint rule over `tools/*/selftest.py`: an arm whose only assertion is a substring test against another module's source text is refused unless it carries an explicit `# source-shape:` waiver naming why no behavioural arm is possible. Run it over the real tree first to size the population before arming it.

### LOW

#### L1 — The spawn poll prints "whole" even when it timed out with members missing (ids 5, 9 and 14)

- **Ref:** [tools/process-monitor/selftest.py:1176](../../../../tools/process-monitor/selftest.py).
- **Lenses:** correctness (id 5, class `one-value-field-records-a-mixed-outcome`), seams (id 9) and verification (id 14). The binding grade is low for all three.
- **Defect:** The poll loop (~1160-1175) leaves by an identical `break` whether the tree completed or `TREE_SPAWN_BOUND` expired. Line 1176 then always prints "the staged tree was whole in the census after %.1fs".
- **Consequence:** On a timeout, the log says the tree was whole after ~30 s just above the FAIL that names the missing member. That points triage away from the spawn race this loop exists to diagnose. It also misses spec 21's observability line for the timeout case. The verdict is still graded afterwards from `missing`, so only log text is wrong.
- **Fix (judged SOUND for all three):** Set a `whole` flag at the completion `break`. Print "whole after N s" or "NOT whole after N s (bound %d s)" from that flag.
- **Left-shift gate:** No gate fits a log string economically. Add an entry to this project's bug-class checklist under `one-value-field-records-a-mixed-outcome`: a loop with more than one exit must not be followed by a message that asserts one exit's outcome.

#### L2 — No arm asserts `rep['backstopped']` (id 12)

- **Ref:** [tools/process-monitor/reap.py:240](../../../../tools/process-monitor/reap.py).
- **Lens:** verification. The binding grade is low. The finder graded it medium, and the skeptic re-graded it low.
- **Defect:** `test_msys_signal_is_backstopped_by_winpid` asserts the taskkill calls, `errors` and `signalled`, but never `rep['backstopped']`. `render_kill` (reap.py:321-337) has no backstopped line.
- **Why low:** Today the key is filled correctly, and spec 21 S2 promises only that the field is "reported", which the dict does. Nothing reads it, so a regression changes no behaviour.
- **Overlap with M2:** This is the coverage half of M2 (id 7). It stays a separate item only because its binding grade differs. A fix for M2 closes it.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Add `sorted(rep['backstopped'])` to the checked tuple with expected `[1, 2, 4]`. Optionally add a `backstopped %d` count to `render_kill`'s killed line.
- **Left-shift gate:** M2's returned-key reader-and-assertion checker covers this class.

## Refuted (recorded, not carried)

The full verdicts are in the appendix.

| id | claim | why refuted |
|---|---|---|
| 2 | The backstop opens a new pid-reuse window. | It is the same census-snapshot exposure the native path already has, and spec 21 §4 accepts it. |
| 3 | The backstop failure path mis-classifies a member. | The classification is unchanged from base. |
| 4 | `backstopped` records issuance, not landing. | Spec 21 S2 defines it that way. |
| 11 | The staged-delay field promises shipped code. | TEMPLATE-SPEC.md:280 defines that field as prose. |

review-shape kind=diff-review round=1 intensity=light at=synth raw=14 confirmed=10 refuted=4 unverified=0 blocker=0 high=1 medium=5 low=4 agents=9 out-tokens=83386

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/branch-reconcile/kit.toml:32 | medium | medium | confirmed | Confirmed by reading govkit.py. classify_row (8536-8537) takes a rename only when `t_state == "absent"`, meaning gov's SOURCE is gone at to_commit. Here tools/branch-reconcile/SKILL.template.md still exists and only the kit.toml `to` changed, so the old receipt row `.claude/skills/branch-reconcile/SKILL.md` never resolves as renamed. Its re-resolved role `now` is None, because resolve_entry no longer writes that path. That skips the role-move branch at 9318, and the row keeps its recorded `rendered` role, which maps to `adopter`. At 9607 the disposition caps diverged/stale at `re-rendered`, which is only a report. The [[regenerate]] argv (`--scaffold`) writes `.claude/skills/cleanup/SKILL.md` (SKILL_REL in adopt-branch-reconcile.sh), and nothing in the adopter or govkit unlinks the old path. branch-reconcile is a registry entry (registry.toml:95), so adopters exist. Every adopter therefore keeps a `name: branch-reconcile` skill next to the new `cleanup` one, and `--check` now only compares cleanup/. Spec 19 §4 says "govkit update moves an adopter's copy", and §5 repeats it under risks and migration. That is false and misleads the next change. The impact is contained to a stale duplicate skill with no data loss, so medium. | unsound | - |
| 2 | correctness | tools/process-monitor/reap.py:241 | medium | - | refuted | Spec 21 §4 explicitly accepts this exposure, and the claim that it is a new, distinct window does not hold up. The backstop signals the winpid from the same census read that the native path at reap.py:226 already signals. That path routinely signals winpids of members that already died in the leaves-first cascade, which is the documented reason `already_gone` exists ("a clean 8-of-8 kill reported four signal errors"). So force-killing a pid from a census snapshot whose owner may have just exited is the pre-existing exposure, not a new one. The extra gap after a successful `kill -9` is the few milliseconds of one subprocess spawn. Windows also cannot reuse the pid while the walk is leaves-first, because the still-unsignalled parent shell holds the child's process handle. Spec 21 also measured that the gated alternative (taskkill only after a refused MSYS signal) stays red 1 run in 8, in the accepted-and-survived case. Finder graded medium, and no reachable harm is established. | unsound | destructive-step-before-its-precondition |
| 3 | correctness | tools/process-monitor/reap.py:243 | medium | - | refuted | The diff did not introduce this defect. At base 942b587e, a failed MSYS signal was classified only by its own message, so an MSYS `No such process` went to already_gone, and a member that survived was listed in both already_gone and survivors. When the backstop also fails, the new code keeps exactly that classification (done stays the MSYS result), so behaviour on this path is unchanged from base. The dual already_gone and survivors listing is also pre-existing, since check_settled_survivors has never pruned already_gone. The run's verdict (survivors, and exit 1 at reap.py:473/483) still comes from the census, so an unkillable survivor is still reported and still reds. A taskkill `Access is denied` right after MSYS reports the process gone is also the expected answer from a process that is terminating (the cascade case), not evidence it lives on. What is lost is a second diagnostic message on a path whose classification already matched base. Finder graded medium, and no new defect is established. | sound | one-value-field-records-a-mixed-outcome |
| 4 | correctness | tools/process-monitor/reap.py:240 | low | - | refuted | Spec 21 S2 defines the field as the members the backstop followed: 'follows every MSYS signal with a single-pid taskkill ... The members backstopped are reported as `backstopped`. Whether a member died stays the census's answer.' The code does exactly that. Every MSYS-signalled member gets a backstop, and it is appended once the backstop is issued. The spec deliberately does not record landings, because death is graded by the census re-read. A backstop that fails after a refused MSYS signal already shows up in `errors`, because `done` is not replaced. The spec's observability item names only the arm's spawn-time print (§5) and never asks render_kill to print `backstopped`. So the absent render line breaks no stated contract. This is a by-design reporting choice, not a defect. | sound | one-value-field-records-a-mixed-outcome |
| 5 | correctness | tools/process-monitor/selftest.py:1176 | low | low | confirmed | selftest.py's poll loop leaves by an identical `break` on completion and when `time.time() - started > TREE_SPAWN_BOUND` passes. The print right after it ('the staged tree was whole in the census after %.1fs') runs on both paths. So a timeout logs 'whole after 30.xs' just above the FAIL that names the missing member. The verdict is still right because `missing` is graded later from the walk. Only the diagnostic line is wrong, and the diff introduced it. | sound | one-value-field-records-a-mixed-outcome |
| 6 | seams | tools/branch-reconcile/kit.toml:32 | high | high | confirmed | Spec 19 §4 says `govkit update` moves an adopter's copy to the new destination. It does not. `derive_rename_map` builds old-source -> new-source from gov's git R rows, and `resolve_renamed` looks up `renames.get(row['source'])`. The source `tools/branch-reconcile/SKILL.template.md` did not move, so the old receipt row never becomes `renamed`. Even a `renamed` rendered row would get only 'reported only ... never written by `update`' (govkit.py ~10124-10133, `a['how'] != 'table'`). The role re-resolution (~9308) finds no write or unlanded entry at the old path, so `now` is None and no move happens. The row grids to stale, is capped to `re-rendered` (~9607), and `[[regenerate]]` runs `--scaffold`. That writes only `SKILL_REL=.claude/skills/cleanup/SKILL.md`, and nothing in adopt-branch-reconcile.sh or govkit deletes or moves the old render. `measure_rendered_rows` then re-stamps the old row against the old file, which is still present. The adopter ends up with `.claude/skills/branch-reconcile/SKILL.md` (`name: branch-reconcile`, the same triggers) beside the new `/cleanup` skill. `--check` reads only the new path and the descriptor's LF pin no longer names the old one, so no gate covers the stale copy, and it never re-renders on later template edits. Every adopter that updates reaches this. The spec's §4, risks and migration lines state the opposite, which will mislead the next change. | unsound | shipped-checker-edit-is-an-adopter-contract-change |
| 7 | seams | tools/process-monitor/reap.py:272 | medium | medium | confirmed | reap.py:240 appends to `backstopped` and :272 returns it, but nothing else in tools/process-monitor reads it. `render_kill` prints killed/survivors/already gone/unsignalable/signal errors/census reads only, and neither tree-killed health event (around :378 and :468) carries it. reap has no JSON output, so the field never leaves the process. The AC2 arm (selftest.py:742-768) asserts the taskkill argv list, `errors` and `signalled`, never `rep['backstopped']`, so the field could be dropped or mis-populated and every arm would stay green. Spec 21 S2 says backstopped members are reported as `backstopped`, observed by AC2/AC3. Only the dict key exists; nothing observes it. The sub-claim also holds: when the MSYS signal and the taskkill both fail with a non-gone error, `done` stays the MSYS result (lines 243-245), so only the MSYS blob reaches `errors`. Kill behaviour is unaffected, and survival is still judged by the census, so the effect is contained: medium. | sound | - |
| 8 | seams | memory/builds/dSweptBranches/spec/2026-10-13-spec-TOOL-dSweptBranches-21.md:110 | medium | medium | confirmed | Spec 21 §7 line 110 declares a new arm in selftest.py covering AC1 with a five-second delay staged in the tree's body. The shipped body (selftest.py around lines 1131-1136) stages no delay, and no arm or parameter anywhere stages one: grep finds no `sleep 5`. The ledger confirms AC1 was observed through a scratch edit whose bytes were restored. AC1's red-when ("the poll is replaced by the fixed wait") is enforced by nothing shipped. The undelayed tree usually spawns in under 3 s, so restoring `time.sleep(3)` would mostly stay green while the spec claims an arm guards it. The consequence is a regression back to the original flaky red that goes undetected, not a wrong shipped result, so medium. | sound | observed-by-claim-no-arm-discharges |
| 9 | seams | tools/process-monitor/selftest.py:1176 | low | low | confirmed | The poll loop (selftest.py around lines 1164-1175) breaks either when every member is present or when `time.time() - started > TREE_SPAWN_BOUND`. Line 1176 then unconditionally prints "the staged tree was whole in the census after %.1fs", so on a timeout it claims the tree was whole after about 30 s just before the member check reports a member missing. This only affects log text: the verdict still comes from the member check, so low. | sound | - |
| 10 | verification | tools/branch-reconcile/kit.toml:32 | high | medium | confirmed | The claim holds. The change edits only `to` in kit.toml; the source tools/branch-reconcile/SKILL.template.md stays where it was. govkit's resolve_renamed (govkit.py:9220-9223) returns None unless renames.get(row['source']) is set, and classify_row only asks it when t_state == 'absent' (8536-8537). Neither condition can hold here. An adopter's receipt row at .claude/skills/branch-reconcile/SKILL.md re-resolves to no destination (`now` is None at 9315-9317), so it falls through as a plain `rendered`/adopter row and is graded, not moved. The [[regenerate]] --scaffold then renders a second copy at cleanup/SKILL.md. derive_unclaimed_candidates and the rename-dests logic only handle gov source moves, and nothing in govkit drops or moves a row whose descriptor `to` changed. So spec 19 §4/§5's 'govkit update moves an adopter's copy' is false, and after this diff no --check covers the old copy. Graded medium, not high: the leftover is a duplicate skill that still routes to the same, unmoved CLI. Only adopters who installed the kit between TOOL-dSweptBranches-5 and this change can be affected, and the false claim sits in a closed spec rather than in live docs. | sound | a-spelling-change-strands-its-readers |
| 11 | verification | tools/process-monitor/selftest.py:1159 | medium | - | refuted | The finding misreads the §7 line. memory/TEMPLATE-SPEC.md:280 defines the third field of a `New arm:` line as '<what stages its failing case>'. It is prose that describes how the arm was observed red; it does not promise a permanently staged condition. The AC2 row uses the same field for 'the backstop removed from run_kill', which is plainly a mutation and not shipped code. The arm covering AC1, the reworked test_live_tree_dies_completely with its bounded poll, does ship. The ledger records the staged five-second delay as the measurement, bytes restored, which is exactly what the template's field describes. The 'never completes' path falls through to the existing member check, which names the missing member. No declared arm is missing. | unsound | - |
| 12 | verification | tools/process-monitor/reap.py:240 | medium | low | confirmed | This is factually true. test_msys_signal_is_backstopped_by_winpid asserts the taskkill calls, errors and signalled, but never rep['backstopped']. render_kill (reap.py:321-337) prints no backstopped line, and grep finds no reader of the key. The impact is a coverage gap, not wrong behaviour: the key is filled correctly today, and spec 21 S2 promises only that it is 'reported', which the report dict does. Spec 21's observability item concerns the arm's spawn-time print, not render_kill. Nothing reads the field, so a regression there changes no behaviour. | unsound | - |
| 13 | verification | tools/process-monitor/reap.py:244 | medium | medium | confirmed | In reap.py lines 231-245, this diff adds the backstop branch `if done.returncode != 0 and (backstop.returncode == 0 or check_gone_blob(backstop)): done = backstop`. The only arm that drives it is test_msys_signal_is_backstopped_by_winpid. Its stub_run returns rc 0 for every taskkill call, so only the `backstop.returncode == 0` disjunct is ever exercised. No arm covers the case where MSYS is refused and the backstop reports 'not found' (the result should land in already_gone). No arm covers the case where both are refused (the result should land in errors). The live arm runs a real tree, so it cannot reach either case deterministically. test_already_gone_is_not_a_signal_error (selftest.py:779) only greps reap.py's source for 'already_gone' and 'not found'. 'not found' now lives in check_gone_blob, so that grep stays green whether or not either call site uses the helper. Dropping the `or check_gone_blob(backstop)` disjunct, or swapping which result replaces `done`, leaves the suite green. The source-grep weakness itself existed before this diff, but the untested backstop arms are new. I could not find a defect in the logic itself today, so the effect is limited to missing coverage of new code. | sound | - |
| 14 | verification | tools/process-monitor/selftest.py:1176 | low | low | confirmed | In selftest.py around lines 1160-1176, the poll loop has two `break` exits: one when the tree is complete, one when `time.time() - started > TREE_SPAWN_BOUND`. Both fall through to the same line, `print("  the staged tree was whole in the census after %.1fs" ...)`. When the loop exits on the bound with members missing, the log claims the tree was whole, and then the `missing` check below goes red. That points whoever reads a CI failure away from the spawn race this loop exists to diagnose. The loop and the print are both new in this diff. The defect only affects a log line, not any verdict. | sound | - |
