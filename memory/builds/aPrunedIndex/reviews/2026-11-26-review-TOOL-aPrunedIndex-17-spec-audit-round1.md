**Serves:** spec-audit TOOL-aPrunedIndex-17@rev-1

# aPrunedIndex — spec audit of unit 17, round 1

*2026-11-26. A Tier-2 adversarial pass over spec 17, the unit that holds fixed git answers across the five held tag plants so `tags bundle selftest` costs fewer spawns. Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.*

Reviewed: memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md@25d1377455e33ad176087db6f257c0bad6335b9a

Round: 1

## Verdict: CLEAN WITH FIXES

No blocker and no high survived. Ten items hold the 14 confirmed findings: five medium items (9 raw findings) and five low items (5 raw findings). Every item is a spec amendment; no shipped behaviour is wrong.

Review shape: intensity full, raw 15, confirmed 14, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.93. Adjudicated tally by item: 0 blocker, 0 high, 5 medium, 5 low. By raw confirmed finding: 0 blocker, 0 high, 9 medium, 5 low.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| coherence | yes | 5 | 5 | 0 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 3 | 2 | 1 | 0 | 0 | 0 | 0.67 |
| blast-radius | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses 5/5 returned, 0 died. Skeptic batches 5/5 returned, 0 died.
- 0 contradictory verdicts demoted, 0 orphaned duplicate refutations demoted, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 11 judged sound, 3 judged UNSOUND (ids 1, 3, 9), 0 instance-only, 0 none proposed, 0 not judged.
- Severity: 0 ungraded by the skeptic, 2 re-graded (ids 1 and 9, high to medium).
- Unverified findings: 0 uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Preset unit-spec: coherence, grounding, reuse, blast-radius, failure-envelope.
- Intent: 6 spec documents supplied as `specs`, as sibling context.
- Checklist: 24 items, each assigned to one lens (coherence 5, grounding 5, reuse 5, blast-radius 5, failure-envelope 4).
- By design: none supplied.
- Move check: no checked subject moved.
- Refuted findings shown: 1. Same-address pairs shown: 9.
- Dispositions: unclassed refuse; 24 class slugs handed; 226 leg names read from tools/gate-legs.json.

The run is complete: every count above that must be zero is zero.

Twins: refuted id 10 (AC7's load gauge does not reuse `measure_spawn_cost`) shares the §6 address with nine confirmed findings. It is a twin of none of them. Each of those findings is a different defect at that address, so no twin is flagged.

## Medium

### M1. AC8's evidence-row command is refused on the green path (ids 1, 6, 9, 12)

**Where:** spec 17, section 6 AC8 and section 2 S6.

**What is wrong:** AC8 names `python tools/run-gates/derive-ceilings.py --write --observed` as the evidence-row write. That route is monotone. At tools/run-gates/derive-ceilings.py@b8c1709f:600-611, `if prev and prev[0] >= obs_secs` prints "does not raise its recorded maximum ... MONOTONE. Nothing was written" and returns 1. The stored row is ceiling-evidence.txt:149, `tags bundle selftest 106.0 ... a`. AC8 is green only when the worst reading is at most 106 s, so on every green outcome, including exactly 106.0, the named command exits 1 and writes nothing. On a reading above 106 s it would raise the row, which S6 forbids ("neither row moves up"). The command as spelled also lacks the `'<leg>=<seconds>'` value and `--how`, which `parse_observed` (:425-438) refuses, and `GOV_NODE`, which :515-517 refuses. It does not say which of the three readings is recorded. (PINNED, 2026-11-26)

**Consequence:** S6's promise that the evidence row is rewritten from the new readings cannot be kept as specced. The close step fails, the row keeps the TOOL-aPrunedIndex-4 reading from d5288a92d, and the Files-touched list claims a change that never lands. A builder who hand-edits the row instead breaks the file's "do not hand-edit" header. The stale 106.0 is still a true maximum, so nothing wrong ships; all four findings grade medium, ids 1 and 9 re-graded from high by their skeptics on that ground.

**Fix:** The skeptics judged id 6's and id 12's fixes sound, and rejected id 1's and id 9's proposals with corrections. The corrected fixes split on whether the green path lowers the row. Pick one and state it in both S6 and AC8:

- Lower it (id 6, sound; id 9's correction agrees). Use one combined call: `GOV_NODE=a python tools/run-gates/derive-ceilings.py --write --reset 'tags bundle selftest' --observed 'tags bundle selftest=<worst>' --how '<the three readings and their gauges>'`. The reset drops this node's row before the `--observed` block, so `prev` is None and the observed row lands. Add a Red-when line: the call exits non-zero, or the row afterwards does not read `<worst>`. `--reset` alone is not the route, because it re-derives only from retained gate-run files, and AC8's standalone readings are not in them. One edge stays open: if a finished bar run leaves an ok reading of the leg in gate-run before the write, the reset re-derives from it (:245-248) and the refusal can still fire.
- Leave it (id 12, sound; id 1's correction agrees for the green path). State that the evidence row stays at 106.0 by the file's monotone rule, so only the budget row is rewritten. Drop ceiling-evidence.txt from section 4's Files touched, or mark it as touched on the red path only.

Whichever is picked, the red path follows M5: no evidence write. Id 1's correction would `--observed`-raise the row on red, which conflicts with S6 and with M5's sound fix, so that half is not adopted. Probe the refusal in a scratch copy, never the tracked file: `GOV_NODE=a python tools/run-gates/derive-ceilings.py --write --observed 'tags bundle selftest=100' --how x` should exit 1 with the MONOTONE line.

**Left-shift gate:** extend `spec tokens (a spec's own names resolve)` so that a spec's named `derive-ceilings.py` invocation is checked for its required arguments (`GOV_NODE`, `<leg>=<seconds>`, `--how`). Add a bug-class checklist line: a criterion that writes through a monotone tool states the write's direction against the stored value.

### M2. AC4 observes two of the five held plants (ids 4, 13)

**Where:** spec 17, section 6 AC4 against section 2 S3 and the five section 7 New arm lines.

**What is wrong:** S3 puts five plants in `HELD_PLANTS` and says AC4 and AC5 observe them. AC4 (lines 245-250) bounds only `gc-predates` (at most 90) and `released-rows` (at most 210), plus `rebuild` at 32. The 'with' column for `dead-versions`, `named-probe` and `released-cost` (lines 104-106: 20/17/31) feeds no criterion. `HELD_PLANTS` is a plain tuple that nothing checks against `PLANTS` (tools/playbook/gov_tag.py@27cfdb44:420-439). Section 4's spawn table (:102-108) also has no `rebuild` row, so the 32 that AC4 calls PINNED at f963331d is never recorded.

**Consequence:** A `HELD_PLANTS` that drops or misspells one of the three small plants passes every criterion. AC1, AC5 and AC6 are unchanged by holding, and AC7's noisy wall cannot see a 3-4 spawn change. The New arm lines would then claim those plants' breaks were "re-observed under the held answers" when the run was never held. That is a false certification, but contained: the plants' verdicts hold, and only their few spawns are lost. Medium.

**Fix (judged SOUND for both findings):** Make AC4 cover the whole class. Assert `set(HELD_PLANTS)` equals the five names and that each is in `PLANTS`. Bound all five spawn counts by section 4's 'with' column: `dead-versions` <= 20, `named-probe` <= 17, `released-cost` <= 31, `gc-predates` <= 90, `released-rows` <= 210. The Red-when names any of the five whose count stays at its 'without' value. Add the `rebuild` count of 32 to section 4's spawn table.

**Left-shift gate:** a bug-class checklist line under `observed-by-claim-no-arm-discharges`: a criterion over a named set bounds every member, or asserts the set equals its listed members.

### M3. AC7's red condition passes a no-op build (id 2)

**Where:** spec 17, section 6 AC7.

**What is wrong:** AC7 is red only when "the fastest round after is not faster than the slowest round before", i.e. iff min(after) >= max(before). Any overlap of the two spreads passes.

**Consequence:** For six readings from one distribution, as a no-op edit gives, the chance that all three 'after' readings sit above all three 'before' readings is 1/C(6,3) = 1/20. A build that changes nothing passes about 95% of the time, and section 4 itself calls the wall noisy. AC4's spawn counts still detect the change, so only the wall-time claim goes uncertified. Medium.

**Fix (judged SOUND):** Make AC7 red when the slowest round after is not faster than the fastest round before (max(after) >= min(before)), so the spreads must not overlap. Alternatively, compare gauge-normalised per-round sum ratios against a stated bound, such as at most 0.85.

**Left-shift gate:** a bug-class checklist line: every timing criterion states the probability that a no-op build passes it, and that probability must be small.

### M4. AC8 passes the unbuilt tree on a quiet node (id 3)

**Where:** spec 17, section 6 AC8.

**What is wrong:** AC8's pass condition is exit 0, under 300 s, and a worst reading at most 106 s (so the 1.5x budget stays at or below 159). The 106 s reading behind selftest-budgets.txt:146 (159) and ceiling-evidence.txt:149 (106.0) was itself taken at d5288a92d, a tree before this unit. AC8 records the load gauge but bounds nothing by it. (PINNED, 2026-11-26)

**Consequence:** Read on a quiet node, AC8 cannot tell a built unit from an unbuilt one. Under load, section 4 predicts about 400 s, so AC8 goes red whatever the build does. The hand-off decision AC8 makes therefore follows when the readings are taken, not the change. AC4 and AC7 carry the build's discrimination, so the effect is contained. Medium. (PINNED, 2026-11-26)

**Fix (the finder's proposal was REJECTED; the skeptic's correction):** Take AC8's comparison readings in one session: three runs of `tag_bundle.py --selftest` on the pre-edit tree and three on the built tree, back to back, each with its AC7 gauge. Bound the after-over-before ratio of the worst readings at a stated value below 1. State the gauge band all six readings must fall in.

**Left-shift gate:** the same checklist line as M3 (no-op pass probability). Add: a criterion compared against a stored reading states the load it was taken under.

### M5. The close has no rule for the two rows when AC8 reds (id 14)

**Where:** spec 17, section 2 S6 and section 6 AC8.

**What is wrong:** Section 4 (lines 121-126) predicts AC8's red, about 400 s under load. On red, AC8 says only "Either red is the hand-off" and gives no rule for the budget and evidence rows. S6 says both rows are rewritten "and neither row moves up". Any reading above 106 s fed to `--observed` raises the evidence row, and the budget rule (1.5 x worst, at most 159) cannot be met. The green-path command is also incomplete (no `<leg>=<seconds>`, no `--how`, which tools/run-gates/derive-ceilings.py@b8c1709f:434 exits on), and nothing says the worst reading is the one recorded. That overlap with M1 is the incomplete spelling only; this item's defect is the red path. (PINNED, 2026-11-26)

**Consequence:** On the path the spec expects, a builder at the close has no rule. It could write a raised row S6 forbids, hand-fit the rows, or leave them stale with the hand-off open. The command fails loudly, and a raised row would be caught in review, so the effect is contained. Medium.

**Fix (judged SOUND):** In S6 and AC8, state the red path: when the worst reading exceeds 106 s or reaches 300 s, write neither row, record the three readings and gauges in the ledger, and open the section 3 hand-off. Spell the green-path command in full, with `<worst reading>` named as the recorded value. M1 settles whether that green command lowers the row or is dropped. (PINNED, 2026-11-26)

**Left-shift gate:** a bug-class checklist line under `owner-item-without-its-reject-outcome`'s spirit: every criterion that writes a record names what is written on each of its outcomes, red included.

## Low

### L1. The README's row 6 promises what unit 17 hands off (id 5)

**Where:** memory/builds/aPrunedIndex/README.md:54, build-order row 6, against spec 17 section 4 and AC8.

**What is wrong:** The row promises "fewer git spawns, index opens and verb runs per plant, so `tags bundle selftest` fits its ceiling under load". The spec rejects fewer verb runs (:53, :194-196), predicts about 400 s against the 300 s ceiling under load (:121-126), and hands the remainder to an unminted pool unit (:67-69). (PINNED, 2026-11-26)

**Consequence:** A reader of the overview will take the leg as fixed under load once unit 17 closes. The record misleads; behaviour does not change. Low.

**Fix (judged SOUND):** Amend the spec's section 1 or Edges to name the README row and say unit 17 delivers fewer spawns only, with the ceiling-under-load outcome owed to the hand-off pool unit. Restate the README row to match.

**Left-shift gate:** a checklist line: a spec whose design narrows its build-order row's promise restates that row in the same change.

### L2. AC5's scratch-path token has no stated normaliser (id 7)

**Where:** spec 17, section 6 AC5 (and section 4 line 114).

**What is wrong:** AC5 says to replace "each run's scratch directory path with one token" before diffing, but never gives the spelling. `gc-predates` (and probably `released-rows`) print that path through `derive_worktree_key` (tools/playbook/tag_index.py@4d1a9ef3:714-719): forward slashes, a lower-cased drive letter. Line 712 makes it with `tempfile.mkdtemp(prefix="gt")`, so the suffix is random per run.

**Consequence:** A builder substituting the native spelling leaves every printed worktree line unmatched, and the diff reds although the held answers are correct. Otherwise the builder invents a normaliser. It affects a builder check only. Low.

**Fix (judged SOUND):** State the normaliser in AC5, e.g. `re.sub(r'(?i)[a-z]:[\\/].*?[\\/]gt[a-z0-9_]+', '<SCRATCH>', line)`, applied to stdout and stderr. Have the builder confirm it before the edit: two runs of `gc-predates` must already diff empty.

**Left-shift gate:** a checklist line: a diff criterion over output with run-varying text names its normaliser and proves it on two pre-edit runs.

### L3. AC5's and AC7's stated costs undershoot section 4's timings (id 8)

**Where:** spec 17, section 6 AC5 cost (line 254) and AC7 cost (line 269).

**What is wrong:** Section 4 (lines 116-117) pins one round at 223.6 s without and 157.7 s with, under a 0.21-0.23 s gauge. AC5's two runs cost 381 s (about 6.4 min), not "about five minutes on a loaded node". AC7's six rounds cost 3 x 381 = 1144 s (about 19 min), not "ten to fifteen minutes". (PINNED, 2026-11-26)

**Consequence:** Time planning only. Under the load behind the 521 s reading, the real cost is several times larger. Low. (PINNED, 2026-11-26)

**Fix (judged SOUND):** Derive each cost from section 4's PINNED sums: AC5 about 6.5 min at a 0.21 s gauge, AC7 about 19 min. Say that both scale with the gauge.

**Left-shift gate:** a checklist line: a criterion's stated cost is computed from the spec's own pinned timings and names its gauge.

### L4. The reuse audit misses two prior instances of the pattern (id 11)

**Where:** spec 17, section 10 Reuse audit (line 311).

**What is wrong:** Section 10 says "no existing seam stores a git answer". tools/chain-packet.py#set_reads (from line 189) keeps a `cache = {}`, answers `show <ref:path>` from it, and installs `schedule.git = read_git`. tools/playbook/gov_tag.py@27cfdb44:1632/1636 already swaps `ti.read_git` for a block inside try/finally at the `worktree-spelling` plant.

**Consequence:** The audit sentence is false, and the next reuse search starts from "nothing exists". The design is unaffected, since neither can be imported as a seam here. Low.

**Fix (judged SOUND):** Cite tools/chain-packet.py#set_reads and the `worktree-spelling` swap in tools/playbook/gov_tag.py#run_plant as prior instances of rebinding a module's git reader for a block. Say why S2 lifts neither: one is a hyphenated script, the other an inline try/finally.

**Left-shift gate:** a checklist line: a reuse audit's "nothing exists" claim names the grep it ran (here, assignments to a module's `git` or `read_git` attribute).

### L5. The hold key is wider than its reason (id 15)

**Where:** spec 17, section 4 Mechanism item 1, second bullet (line 134), and AC2.

**What is wrong:** The rule holds any rev-parse or ls-tree read in which some element is a 40-hex id, with no limit on the other elements. `rev-parse <sha> HEAD` or `ls-tree <sha> HEAD:<path>` would be held although part of the answer moves. The stated reason is "a full id names one object". AC2's eight reads include no mixed case.

**Consequence:** None today: every current caller (tools/playbook/tag_index.py@4d1a9ef3:794, 843, 960/967; tools/playbook/gov_tag.py@27cfdb44:279) passes only an id or `id^{tree}` with fixed flags and paths. The next read added inside a held plant that mixes an id with a moving ref would get a stale answer, and no criterion would notice. Low.

**Fix (judged SOUND):** Narrow the bullet so the 40-hex element (alone or with `^{tree}`) is the only revision argument. Every other element must be a fixed flag from {`--full-tree`, `--name-only`, `-r`, `-z`, `--`} or a path after `--`. Add a ninth AC2 read, `rev-parse <id> HEAD`, expected False.

**Left-shift gate:** the ninth AC2 case is the gate. Add a checklist line: a cache key rule is stated as an allow-list of every element, not as the presence of one fixed element.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=15 confirmed=14 refuted=1 merged=0 unverified=0 blocker=0 high=0 medium=9 low=5 agents=11 out-tokens=97051 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC8 (and section 2 S6) | high | medium | confirmed | I read tools/run-gates/derive-ceilings.py. In the --observed branch, `if prev and prev[0] >= obs_secs:` prints 'does not raise its recorded maximum ... MONOTONE. Nothing was written' and returns 1. ceiling-evidence.txt:149 holds `tags bundle selftest 106.0 ... a`. AC8 (spec @25d13774) passes only when the worst reading is at most 106 s, and it names `--write --observed` as the evidence write. So on every passing build the named command exits 1 and writes nothing. A reading of exactly 106.0 is refused too. AC8 also leaves unsaid which reading goes into `--observed` and omits `--how` and GOV_NODE. Graded medium: the stored row stays at 106, which is still a true maximum, so nothing wrong ships. The cost is a step at the close that cannot run as written. | unsound | criterion-asserts-what-its-own-command-cannot-show | class:criterion-asserts-what-its-own-command-cannot-show (PINNED, 2026-11-26) |
| 2 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC7 | medium | medium | confirmed | The spec @25d13774 has AC7 red only when 'the fastest round after is not faster than the slowest round before', which is red iff min(after) >= max(before). Any overlap of the two spreads passes. For six readings from one distribution, the chance all three 'after' readings sit above all three 'before' readings is 1/C(6,3) = 1/20, so a no-op edit passes about 95% of the time. Section 4 itself calls the wall noisy. Graded medium: AC4's spawn counts still detect the change, so only the wall-time claim goes uncertified. | sound | - | new:timing-criterion-passes-a-no-op-build |
| 3 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC8 | medium | medium | confirmed | selftest-budgets.txt:146 holds 159 and ceiling-evidence.txt:149 holds 106.0. Both rows record that the 106 s reading was taken at d5288a92d, a tree before this unit, with 'other sessions working on the node'. So the unbuilt tree has already produced a reading that meets AC8's pass condition (exit 0, under 300 s, at most 106 s). AC8 sets no load condition, and section 4 predicts about 400 s under heavy load whatever the build does. AC8's verdict therefore follows the load, not the change. Graded medium: AC4 and AC7 carry the build's discrimination, so the effect is contained to the hand-off decision. | unsound | - | new:timing-criterion-passes-a-no-op-build (PINNED, 2026-11-26) |
| 4 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC4 against section 2 S3 | medium | medium | confirmed | I re-read spec blob 25d13774. Lines 31-34 (S3) list five plants in HELD_PLANTS and say they are observed by AC4 and AC5. AC4 at :245-250 bounds only gc-predates (at most 90) and released-rows (at most 210), plus rebuild at 32. Its red case only catches a skip that leaves gc-predates at 152. AC1, AC5 and AC6 pass the same way whether a plant is held or not, because verdicts and lines do not change. So a HELD_PLANTS missing dead-versions, named-probe or released-cost passes every criterion. The spawn table at :102-108 has the five plants and no rebuild row, so the 32 that AC4 calls PINNED at f963331d is never recorded in section 4. The effect is contained: an unheld small plant only stays slower, and every verdict still holds. | sound | - | class:observed-by-claim-no-arm-discharges |
| 5 | coherence | memory/builds/aPrunedIndex/README.md:build-order row 6 (overview acceptance against the subject's section 4 and AC8) | low | low | confirmed | grep printed README.md:54: '\| 6 \| TOOL-aPrunedIndex-17 \| ... fewer git spawns, index opens and verb runs per plant, so `tags bundle selftest` fits its ceiling under load'. The spec says the opposite in three places. :53 and :194-196 reject fewer verb runs. :121-126 predicts about 400 s against the 300 s ceiling under load. :67-69 hands the rest to an unminted pool unit. No criterion makes the overview's claim true. The README is not under audit and the unit's behaviour does not change, so this is a misleading record only. | sound | - | new:overview-row-promises-what-the-unit-hands-off (PINNED, 2026-11-26) |
| 6 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC8 (and section 2 S6) | medium | medium | confirmed | I read tools/run-gates/derive-ceilings.py. At :600-611, when prev[0] >= obs_secs it prints 'MONOTONE. Nothing was written. Lowering one is `--write --reset`' and returns 1. ceiling-evidence.txt:149 holds 'tags bundle selftest 106.0 ... a ... (TOOL-aPrunedIndex-4 AC8)'. So on AC8's green path (worst reading at or under 106) the spelled command writes nothing and exits 1. On a reading above 106 it would raise the row, which S6 forbids. The spelled command also lacks the '<leg>=<seconds>' value and --how, which parse_observed (:425-438) refuses, and GOV_NODE, which :515-517 refuses. The fix's route works on today's tree: :580-590 drops a reset leg's row from this node, and the leg has no retained gate-run readings (my grep of gate-run/*/*.leg printed nothing), so prev is None and the observed row lands. One remaining edge: if a finished bar run puts an ok reading of the leg into gate-run before the write, the reset re-derives from it (:245-248) and the refusal can still fire. This is not introduced by the fix. | sound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 7 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC5 | low | low | confirmed | I checked the spec at blob 25d13774. AC5 (line 252) and section 4 (line 114) say only 'replaces each run's scratch directory path with one token' and never give the spelling. tools/playbook/tag_index.py@4d1a9ef3:714-719 derive_worktree_key turns backslashes into forward slashes and lower-cases the drive letter. Line 712 of the same file makes the directory with tempfile.mkdtemp(prefix="gt"), so the suffix is random on every run. The printed path is therefore neither the native spelling nor the same string from one run to the next. I did not re-run the plant, but the code alone supports the claim. The effect is a false red, or a normaliser the builder has to make up, during a builder check. No shipped verdict changes, so the grade is low. | sound | - | new:diff-criterion-leaves-its-normaliser-unstated |
| 8 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC5 cost and AC7 cost | low | low | confirmed | Section 4 (lines 116-117) pins one round at 223.6 s without and 157.7 s with, under a 0.21-0.23 s gauge. AC5 (line 254) costs its 'two runs of the five', one before and one after, at 'about five minutes on a loaded node', but 223.6 + 157.7 = 381 s, about 6.4 min, and that was measured on a quieter node. AC7 (line 269) says 'ten to fifteen minutes' for six rounds, but 3 x 381 = 1144 s, about 19 min. Both stated costs are below the spec's own pinned sums. Only time planning is affected, so the grade is low. | sound | - | new:stated-cost-below-its-own-pinned-timings (PINNED, 2026-11-26) |
| 9 | reuse | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC8 (and section 2 S6) | high | medium | confirmed | AC8 (line 275) names `derive-ceilings.py --write --observed` with no value, no --how and no GOV_NODE. Its pass case keeps the worst reading at or under 106 s. In derive-ceilings.py, lines 606-611 refuse any --observed at or under the stored maximum: they print 'does not raise its recorded maximum ... Nothing was written' and return 1. The stored row is ceiling-evidence.txt:149 'tags bundle selftest 106.0 ... a'. So on every green outcome the named command exits 1 and S6's 'rewritten from the new readings' cannot be met by it. The effect is contained: the stale evidence row stays at 106.0, which is conservative, and the refusal message is loud. That is medium, not high. The proposed fix is unsound. Its primary command, `--reset` alone, re-derives only from retained gate-run files. AC8's standalone readings are not in those files. If no retained run holds an ok reading for the leg, lines 578-588 drop the row and leave the leg UNBACKED, so it is not rewritten from AC8's readings either. Combining the two flags does work. The reset drops this node's row before the --observed block, so `prev` at line 605 is None and the observed reading is written. | unsound | - | class:criterion-asserts-what-its-own-command-cannot-show (PINNED, 2026-11-26) |
| 10 | reuse | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC7 (the load gauge, also used by AC8 and S5) | low | - | refuted | (6) preference. The spec at AC7 (line 265) does define a separate gauge, the mean wall of 20 `git --version` spawns, and measure_spawn_cost does exist at tools/run-gates/run-gates.sh@4325d3c0:4202. But the comparability harm the finding claims is false. tools/run-gates/measure_legs.py@864b01c1:461 runs the census sampler as `SPAWN_CMD=\n ... measure_spawn_cost 3`, so the census SPAWN_US times a spawn of `true` (the default branch at 4211), not of git. Taking the existing function with SPAWN_CMD=git --version would not be comparable to the census either. No sibling spec or ledger in the build records any gauge (a grep for gauge, git --version and spawn_cost found nothing outside spec 17), so there is no other in-tree reading to diverge from. The spec's gauge times exactly the spawn this unit removes. No defect the rubric grades. | unsound | - | - |
| 11 | reuse | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 10 Reuse audit | low | low | confirmed | Section 10 (spec line 311) says 'none holds an answer, so no existing seam stores a git answer.' tools/chain-packet.py#set_reads (from line 189) keeps a `cache = {}`, answers `show <ref:path>` from it, and installs `schedule.git = read_git`. That is an existing seam that stores git answers, so the sentence is false. tools/playbook/gov_tag.py@27cfdb44:1632/1636 also swaps ti.read_git for a block inside try/finally, a prior instance of rebinding the reader for one block. Neither changes the design, so the effect is limited to the audit prose. | sound | - | new:reuse-audit-misses-a-prior-instance |
| 12 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 2 S6, section 6 AC8 | medium | medium | confirmed | ceiling-evidence.txt:149 holds `tags bundle selftest 106.0 1 a`, the only row for that leg. tools/run-gates/derive-ceilings.py@b8c1709f:606-611 returns 1 and writes nothing when prev[0] >= obs_secs. AC8 is red when the worst reading exceeds 106 s, so on every green outcome on node a the command AC8 names (spec line 275) refuses. S6's 'rewrites ... that leg's row of ceiling-evidence.txt from the new readings' and the Files-touched entry cannot happen. The file's header also bans hand-editing it. On another node the command would add a new row rather than rewrite this one, which still does not match S6. The effect is a failed close step and a stale record, contained to the records. | sound | - | class:criterion-asserts-what-its-own-command-cannot-show (PINNED, 2026-11-26) |
| 13 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC4 (with S3 and the five section 7 New arm lines) | medium | medium | confirmed | I re-read the spec at blob 25d13774. AC4 (lines 245-249) bounds only gc-predates (at most 90), released-rows (at most 210) and rebuild (32). The 'with' column for dead-versions, named-probe and released-cost (lines 104-106: 20/17/31) feeds no criterion. tools/playbook/gov_tag.py@27cfdb44:420-439 PLANTS holds all five names, and S3 makes HELD_PLANTS a plain tuple that nothing checks against PLANTS, so a misspelled or missing entry raises nothing. Such a plant would run unheld with the same output, so AC1, AC5 and AC6 stay green. AC7 sums noisy walls and cannot see a 3-4 spawn change. The New arm lines 290-294 would still claim each row was 're-observed under the held answers'. That is a false certification, but the plants' verdicts are unaffected and the cost is the small plants' few spawns, so the effect is contained: medium. | sound | - | class:observed-by-claim-no-arm-discharges |
| 14 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 2 S6 and section 6 AC8 | medium | medium | confirmed | Re-probed. selftest-budgets.txt:146 reads 159 and ceiling-evidence.txt:149 reads 106.0. tools/run-gates/derive-ceilings.py@b8c1709f:434 exits with '--observed needs --how', and its docstring at line 47 gives the full form '--observed <leg>=<seconds> --how <...>'. AC8 (lines 271-277) names only `derive-ceilings.py --write --observed`, with no leg=seconds value, no --how and no rule for which of the three readings to feed. On red it says only 'Either red is the hand-off', with no rule for the two rows. Section 4 (lines 121-126) predicts exactly that red. A builder at the close therefore has no rule for the rows on the path the spec expects. The command as written fails loudly, and a raised row is caught only by review, so the effect is contained: medium. | sound | - | new:red-outcome-leaves-its-record-writes-unruled |
| 15 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 4 Mechanism item 1, second bullet (and AC2) | low | low | confirmed | Spec line 134 holds any rev-parse or ls-tree read where some element is a 40-hex id, with no limit on the other elements. So `rev-parse <sha> HEAD` would be held, which goes beyond the stated reason ('a full id names one object'). AC2's eight reads include no mixed case. I checked the current callers: tools/playbook/tag_index.py@4d1a9ef3:794 (ls-tree -r -z --full-tree tree), 843 (head^{tree}), 960/967 (ls-tree --full-tree --name-only head -- path) and tools/playbook/gov_tag.py@27cfdb44:279 (base^{tree}). Each uses only fixed flags and paths beside the id. Nothing breaks today; the risk is the next added read, so low. | sound | - | new:cache-key-wider-than-its-reason |
