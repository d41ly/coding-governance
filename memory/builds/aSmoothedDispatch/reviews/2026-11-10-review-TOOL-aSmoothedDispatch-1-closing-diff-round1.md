**Serves:** diff-review TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7

# Tier-2 diff review: build aSmoothedDispatch, seven units

*Adversarial review of the attended Tier-2 build that removes mechanical refusals from unattended runs. 2026-11-10, ROUND 1.
Finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
Every finding below survived a skeptic prompted to refute it.*

Reviewed range: ae6735c1f237423022016714b3da193f8ed971b7...38c44ea9d458d35eb24ad98ceffef69e737a85b2

## Verdict: CLEAN WITH FIXES

The review found no blocker and no high.
Five items hold six confirmed findings: three medium items (four raw medium findings) and two low items (two raw low findings).
No finding shows a write or dispatch admitted that nothing authorized: the unit 4 admit predicate and cache, and the unit 6 fallback, are correct today.
Each medium is a contained defect: a misleading writer instruction, or an unguarded regression path at the dispatch boundary.

## Review shape

Review shape: intensity full, raw 7, confirmed 6, refuted 0, merged 1, unverified 0 (0 uncertain), precision 1.00.
Adjudicated tally by item: 0 blocker, 0 high, 3 medium, 2 low (5 items).
Adjudicated tally by raw confirmed finding: 0 blocker, 0 high, 4 medium, 2 low (6 findings).

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 0 | 0 | 1 | 0 | 0 | 1.00 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

## Run integrity

Lenses: 5/5 returned, 0 died.
Skeptic batches: 4/4 returned, 0 died.
Verdict handling: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 1 duplicate refutation counted as a merged confirmation (id 2 into id 1), 0 spurious verdicts discarded, 0 duplicates.
Fixes on confirmed findings: 3 judged sound, 0 judged unsound, 3 judged instance-only, 0 none proposed, 0 not judged.
Severity: 0 ungraded by the skeptic, 2 re-graded by the skeptic (ids 3 and 4, high to medium).
Unverified findings: 0 answered uncertain, 0 with no usable verdict.
Lens notes: none supplied, so every lens ran on the kit's generic brief.
Intent: 7 spec documents supplied beside the range's commit messages.
Checklist: 57 items from `--for-diff ae6735c1f237423022016714b3da193f8ed971b7..HEAD`, split security 12, correctness 12, seams 11, verification 11, intent 11.
By design: the caller's byDesign, plus 1 invariant from the checklist's by-design block.
Refuted findings shown: 0. Same-address pairs shown: 0. No twin flags.
Every count above is zero where it should be, so this run is complete.
The security lens returned zero findings, and with every lens returned that zero is evidence, though not proof, that the boundaries hold.

## Items

### 1. MEDIUM: the spec-writer overlay names a `spec-tokens: HIT` row that exit 1 never prints (ids 1, 6; id 2 merged)

**Where:** `tools/roles/house/gov-spec-writer.md:5`. The same text is in the render `.claude/agents/gov-spec-writer.md:56`. The `--spec` docstring at `tools/check-spec-tokens.py:260` makes the same claim ("only HIT and NEAR rows naming the file are printed"). Spec 7 repeats it at `memory/builds/aSmoothedDispatch/spec/2026-11-10-spec-TOOL-aSmoothedDispatch-7.md:81` and `:97`, and cites the wrong line (:1881).

**What is wrong:** unit 7 tells the spec writer that exit 1 prints one `spec-tokens: HIT` row per miss.
The checker prints the `HIT   ` label only under `--list` (`tools/check-spec-tokens.py:1927-1930`), and that path returns 0.
A plain `--spec <path>` run prints each unwaived hit as `spec-tokens: <file> [<kind>] `<tok>` — <why>` (line 2044), then the `N unwaived hit(s), M stale row(s)` summary (line 2048).
Exit 1 also comes from the checker's refusal paths, such as a missing gate-legs.json, CLAIM_CANARY, or the carries or packet loaders, and those print no hit row at all.

**Consequence:** a writer looking for `HIT` rows after exit 1 finds none.
It may mistake real hits for a refusal, or return without fixing them.
The token misses unit 7 exists to catch early then still reach `--dispatch` or the bar.
The effect is contained, because the rows that do print name the file, kind and token, so a careful writer can still act on them.

**Grades:** id 1 medium, id 6 medium (both binding). Id 2 (seams) is the same defect, recorded as a merged confirmation and not counted again.

**Fix (skeptic judged both finders' fixes INSTANCE-ONLY; this is the skeptic's class-level fix):**
Make the row shape match what the checker prints in every place that states it: the house overlay, the rendered agent (re-render with `python tools/roles/render_agents.py --write`), the `--spec` docstring at `tools/check-spec-tokens.py:260`, and spec 7's evidence row and quoted overlay text (lines 81 and 97, with the citation moved from the `--list` row to the exit-1 print).
The overlay should say that exit 1 prints one `spec-tokens: <spec path> [<kind>]` row per miss, then a `spec-tokens: <N> unwaived hit(s)` summary.
Add a suite arm that runs `--spec` on a planted red spec and greps stdout for the exact prefix the overlay quotes.
The finders' proposals cure the cited instance alone. They re-word the overlay and docstring, optionally say that a `spec-tokens: REFUSING` line is a checker refusal to report, or have writers use `--spec <path> --list`, which would also require changing the exit-code sentences because `--list` exits 0.

**Left-shift gate:** add an arm to the `spec-tokens self-test` leg that greps a red `--spec` run's stdout for the literal row prefix quoted in `tools/roles/house/gov-spec-writer.md`. The arm should read the prefix from the overlay itself, so the doc and the checker cannot drift apart again.

### 2. MEDIUM: the refusing half of unit 4's admit predicate has no lasting suite arm (id 3)

**Where:** `tools/unattended/unattended.sh:14315`, the admit predicate. Missing arms in `tools/unattended/unattended.test.sh` near the only new unit 4 arm at :7643-7665.

**What is wrong:** spec 4's AC2 ("both": an own hit next to a foreign hit) and AC3 ("stale", "uncounted", "unattributed", "nosummary") were observed only by the throwaway probe `$SCRATCH/sd4.sh`, which was deleted after the pass.
The suite has one foreign-only arm, where tRun's spec is clean, and the existing own-only arm (n=1, nfar=0).

**Consequence:** the predicate is correct today.
But if a later edit drops the `"${#ownq[@]}" = 0` clause or the `"$m" = 0` clause, both existing arms still pass.
A dispatch whose own spec reds next to a foreign red would then be admitted at the dispatch boundary while the bar stays green.

**Grade:** medium. The finder graded it high. The skeptic re-graded it medium because nothing wrong ships now and the gap is a contained regression guard.

**Fix (skeptic judged SOUND):** in region three, add arms that use the real checker:
(a) tRun's spec and tOther's spec both name the flagged bar: assert the check-49 refusal quotes the tRun line.
(b) The foreign-only tree plus a waiver row no spec produces: assert a refusal.
(c) A stub checker that prints a foreign hit line and exits 1 with no summary line: assert a refusal.
Stage each arm RED by deleting its clause from line 14315, then raise FLOOR_ASSERTIONS and FLOOR_SHARD_3.

**Left-shift gate:** the `unattended-build self-test` leg carries the arms. Add a checklist entry that every acceptance criterion observed by a `$SCRATCH` probe either becomes a suite arm or is declared as pass-time-only in the spec.

### 3. MEDIUM: unit 4's spec-token cache invalidation has no lasting suite arm (id 4)

**Where:** `tools/unattended/unattended.sh:14338` (cache use), key derivation at `derive_spec_token_key` (:14329-14335), the "spec-token cache off" branch at :14384. The arm is at `tools/unattended/unattended.test.sh:7656-7665`.

**What is wrong:** no arm shows that an edited working tree, a new HEAD or another slug misses the cache, that a refused check records no key, or that a missing fingerprint turns the cache off (spec AC5, AC6, AC7).
In the AC4 arm, call 2 asserts only the glob refusal and never that the checker re-ran, even though the arm's comment says it does.

**Consequence:** the cache is correct today: it keys on slug, checker, launcher, HEAD and the whole-tree fingerprint.
A regressed key that leaves out the fingerprint or HEAD, or even a constant key, keeps every assertion green.
That cache would skip the checker on a changed tree, which is the stale-cache admission the security model calls a blocker, and no gate would fail.

**Grade:** medium. The finder graded it high. The skeptic re-graded it medium because the code is correct today and the defect is an unguarded regression path.

**Fix (skeptic judged SOUND):** extend the arm.
Assert that call 2 printed a checker report line and no "skipped" line.
Edit a tracked file under tRun, run `--dispatch`, and assert the checker ran again. Make a commit and assert the same.
Dispatch a second slug and assert the checker runs.
Run a refused dispatch twice and assert it never skips.
Remove the copied `run-gates/gate-fingerprint.sh` and assert "spec-token cache off" and that no key file is written.
Stage each RED by dropping `$fp` or `$hd` from the hash-object input.

**Left-shift gate:** the `unattended-build self-test` leg carries the arms. Add a checklist entry that every cache must have an arm per key component, showing that changing that component causes a miss and staged RED by dropping it from the key.

### 4. LOW: unit 1's no-value `--writes` branch has no suite arm, and one carriage-return arm is missing (id 5)

**Where:** `tools/unattended/unattended.sh:15201`, `[ "$_dw_n" -gt 0 ] || DP_WRITES+=("")`.

**What is wrong:** no arm drives `--writes` followed directly by a flag or by the end of argv (spec 1 AC3). The only empty-path arm, `--writes ''`, goes through the `${#_dw[@]} -eq 0` branch at :15198 instead.
Spec 1 S3 says both space-holding arms move to a carriage-return value, but only one carriage-return arm was added and both space-holding arms were deleted.

**Consequence:** if a regression drops the :15201 append, `--writes --writes a.sh`, or a trailing bare `--writes` after `--writes a.sh`, quietly declares only a.sh and skips the empty-path refusal.
A call with no paths at all is still refused by `check_verb_flag`, so the effect is contained.

**Grade:** low (binding).

**Fix (skeptic judged the finder's fix INSTANCE-ONLY; this is the skeptic's class-level fix):**
Add suite arms for every shape with no field that the split must turn into one empty path, each hitting "given an empty --writes path":
`--writes --writes ${PFX}a.sh`, a bare `--writes` at the end of argv after `--writes ${PFX}a.sh`, and `--writes '  ' --writes ${PFX}a.sh`.
Stage the first two RED by deleting `|| DP_WRITES+=("")`, and the third by deleting the `DP_WRITES+=("")` in the empty-array branch.
Restore the second carriage-return arm, or correct S3's count.
The finder's proposal covers only the cited instance. It adds the single `--writes --writes ${PFX}a.sh` arm and restores the arm or corrects the count.

**Left-shift gate:** `unattended-build self-test` carries the arms. Add a checklist entry for argv splitters that requires one arm per shape with no field: flag next, end of argv, and whitespace only.

### 5. LOW: renderRouteContext reports the dispatch-row fallback where the gate never reaches it (id 7)

**Where:** `tools/hooks/scratch-guard.js:1596`, in renderRouteContext (lines 1595-1604). The gate is checkRouted (lines 1255-1263).

**What is wrong:** spec 6 S3 (line 137) says the context reads the dispatched units "only where the gate would reach step 9".
The code calls readDispatchedUnits and adds a "buildable through its dispatch row ... which scratch-guard counts as routed" line even when a card-routed unit is already buildable.
In that case checkRouted admits at step 9a and never reaches step 9b.

**Consequence:** the write verdict is unchanged.
The effect is one misleading SubagentStart context line, plus one extra file read and folder walk per subagent start.

**Grade:** low (binding).

**Fix (skeptic judged SOUND):** skip the step-6 block unless every card unit's verdict was not-buildable. Either collect an `anyBuildable` flag in renderVerdict, or check `route.units.some(u => !checkBuildable(...))`. The context then reads the rows exactly where checkRouted's step 9b does.

**Left-shift gate:** add a `scratch-guard self-test` arm with a buildable card unit and a buildable dispatched unit, asserting that the context carries no dispatch-row line.

## Already carried by the main loop (severity judged, not counted)

Unit 6's builder found that the `scratch-guard self-test` leg in `tools/gate-legs.json` does not guard `tools/unattended/`, even though its new D-AC6 row reads the driver (class held-suite-guard-misses-a-sibling-kit).
Severity judged: **medium.**
A change to the driver's RUN.md dispatch-row format could break scratch-guard's 9b fallback without the leg that tests it running locally.
That is a contained regression-guard gap at the write boundary, in the same family as items 2 and 3, and not a current wrong result.
This review adds no finding for it and does not count it.

review-shape kind=diff-review round=1 intensity=full at=synth raw=7 confirmed=6 refuted=0 merged=1 unverified=0 blocker=0 high=0 medium=4 low=2 agents=10 out-tokens=101523
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/roles/house/gov-spec-writer.md:5 | medium | medium | confirmed | Observed: tools/roles/house/gov-spec-writer.md:5 and .claude/agents/gov-spec-writer.md:56 both say exit 1 prints one `spec-tokens: HIT` row per miss. In tools/check-spec-tokens.py the `HIT   ` label is printed only inside `if listing:` (line 1927-1930, listing = '--list' in argv at line 1543). A run without --list returns through lines 2043-2048, which print `spec-tokens: <f> [<kind>] `<tok>` — <why>` plus the `N unwaived hit(s)` summary. The --spec docstring this diff added at line 260 makes the same claim ('only HIT and NEAR rows naming the file are printed'). This diff introduced all three texts. The effect is contained: the writer still gets exit 1 and rows that name the file, kind and token, so this medium is a misleading instruction, not a hole in a boundary. | instance | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 2 | seams | tools/roles/house/gov-spec-writer.md:5 | medium | - | refuted | duplicate of id=1. It is the same defect: the overlay at tools/roles/house/gov-spec-writer.md:5, rendered at .claude/agents/gov-spec-writer.md:56, names a `spec-tokens: HIT` row that only --list prints (tools/check-spec-tokens.py:1927-1930), while plain --spec prints the line-2044 shape. I verified that independently here too. | instance | - | - |
| 3 | verification | tools/unattended/unattended.sh:14315 | high | medium | confirmed | The claim holds. In unattended.test.sh, the only new unit-4 arm (lines 7643-7665) is the tOther foreign-only fixture, where tRun's spec is clean. A grep for check_spec_token_hits, 'stale row', 'unwaived hit' and a mixed own+foreign fixture finds nothing else in the suite. Spec 4 section 7 itself scopes the New arm to 'covers AC1 AC4', and AC2/AC3 are observed only by `bash "$SCRATCH/sd4.sh"`. The predicate at unattended.sh:14315 is correct today: the ownq==0, m==0 and n==nfar clauses all refuse as the spec says. So nothing wrong ships now. The gap is that deleting the `${#ownq[@]} = 0` clause still passes both the own-only arm and the foreign-only arm, because the foreign-only fixture has no own hit. Dropping `$m = 0` passes too. That is a contained regression-guard gap at the dispatch boundary, not a current wrong result, so the grade is medium. | sound | - | class:observed-by-claim-no-arm-discharges |
| 4 | verification | tools/unattended/unattended.sh:14338 | high | medium | confirmed | The claim holds. In the arm at unattended.test.sh:7656-7665, call 1 asserts the admit note and 'dispatch declared'. Call 2, the first glob --writes, asserts only the glob refusal, never that the checker ran. Call 3 asserts 'skipped' and the absence of a 'spec-tokens: ' line. With a constant key from derive_spec_token_key (unattended.sh:14329-14335), or one that leaves out $fp or $hd, call 2 skips silently and call 3 skips, so every assertion stays green. No arm edits the tree, moves HEAD, switches slug, repeats a refused dispatch, or removes gate-fingerprint.sh to reach the 'spec-token cache off' branch at line 14384. The arm's comment says 'the first re-runs the checker', but nothing asserts it. The current code does key on slug, checker, launcher, HEAD and the whole-tree fingerprint, and gate-fingerprint.sh covers HEAD^{tree} plus porcelain plus untracked blobs. So the cache is correct today, and the defect is an unguarded regression path. Grade: medium. | sound | - | class:observed-by-claim-no-arm-discharges |
| 5 | verification | tools/unattended/unattended.sh:15201 | low | low | confirmed | Checked the diff of tools/unattended/unattended.test.sh. Unit 1 added the multi-path arm, the whitespace-joined arm and exactly ONE carriage-return arm, and deleted both space-holding arms. S3 in spec 1 says 'its two suite arms move from a space-holding value to a carriage-return value', so one arm is missing. No suite arm drives `--writes` followed by a flag or by the end of argv. That branch is `[ "$_dw_n" -gt 0 ] \|\| DP_WRITES+=("")` at unattended.sh:15201. AC3 observes it only by a pass-time probe, and the only empty-path suite arm is the existing `--writes ''`, which goes through the `${#_dw[@]} -eq 0` branch at :15198 instead. If a regression drops the :15201 append, `--writes --writes a.sh` quietly declares only a.sh. The finder is right that a call with no paths at all is still refused elsewhere, so the effect is contained and the grade is low. | instance | - | class:observed-by-claim-no-arm-discharges |
| 6 | intent | tools/roles/house/gov-spec-writer.md:5 | medium | medium | confirmed | Read tools/roles/house/gov-spec-writer.md line 5 and the render at .claude/agents/gov-spec-writer.md:56. Both say 'Exit 1 prints one `spec-tokens: HIT` row per miss'. In tools/check-spec-tokens.py the `HIT   ` spelling exists only in the --list branch at :1930, and that path returns 0 at `if listing: return 0`. The exit-1 path prints `spec-tokens: {f} [{kind}] `{tok}` — {why}` at :2044, then the `unwaived hit(s)` summary at :2048. So the row the overlay tells the writer to look for never appears on exit 1. The rows that do appear still name the file, so a careful writer may still act on them, which keeps the effect contained. But the instruction is wrong, and it weakens the early catch unit 7 exists to add. | instance | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 7 | intent | tools/hooks/scratch-guard.js:1596 | low | low | confirmed | In tools/hooks/scratch-guard.js, renderRouteContext (lines 1595-1604) calls readDispatchedUnits and adds a verdict line for every buildable dispatched unit that is not on the card. It does this whether or not a card unit is buildable. checkRouted (lines 1255-1263) returns at step 9a on the first buildable card unit, so it never reaches step 9b. Spec 6 §S3 (line 137) says the context reads the dispatched units 'only where the gate would reach step 9'. So the code departs from the spec as the finding describes. The write verdict does not change, and the extra line only says the dispatched unit would also count, which is not false about what the gate would do. The effect is one misleading context line and an extra file read, so low. | sound | - | class:decision-re-derived-by-a-second-process |
