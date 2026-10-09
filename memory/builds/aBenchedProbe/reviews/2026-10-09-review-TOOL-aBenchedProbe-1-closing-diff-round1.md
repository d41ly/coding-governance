**Serves:** diff-review TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2

# Tier-2 closing diff review: aBenchedProbe, ROUND 1

*This is the closing review of build aBenchedProbe (gov, node `a`, 2026-10-09). It covers the
cumulative diff of the build's four units at the integration boundary. Every finding below survived
a skeptic prompted to REFUTE it. The author of this report re-read the load-bearing lines in the
tree rather than transcribing them from a lens: the 7j4 arm at `tools/govkit/govkit.py:3260-3295`,
the pre-initialisation at `:2673`, the keep rule and its receipt write at `:4148-4182`, and the CE4
block at `tools/govkit/selftest.py:2398-2412`.*

**Reviewed range:** 2b26f187f03cc991edbf40b25550e6590e97d26e...91c34abf72cfc7a1f3326d4941c8881dc156845b. **ROUND:** 1.

## Verdict: CLEAN WITH FIXES

No blocker survived. One HIGH finding (id 2) must be fixed before the close can land. It does not
ship a wrong result. The problem is that the new 7j4 arm reds the govkit selftest leg on that
suite's own minimal fixtures, so the close's suite run fails loudly until the fix lands. The
remaining findings are missing regression guards (five MEDIUM) and two LOW cosmetic or precision
issues. The shipped behaviour of all four units is correct today.

## Review shape

Intensity full: raw 9, confirmed 8, refuted 1, unverified 0 (0 uncertain), precision 0.89.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |

The adjudicated tally, counted two ways:

- **By item:** 0 BLOCKER, 1 HIGH, 2 MEDIUM, 2 LOW, which is 5 items.
- **By raw confirmed finding:** 0 blocker, 1 high, 5 medium, 2 low, which is 8 findings.

The two MEDIUM items merge findings. H-M1 covers ids 1, 4 and 6, which are the same gap reported by
three lenses. H-M2 covers ids 7 and 8, which share one class and one fixture.

**Run integrity.** Every count here is zero or complete, so the run is complete:

- Lenses: 5 of 5 returned, 0 died.
- Skeptic batches: 5 of 5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 6 judged sound, 2 judged UNSOUND (ids 2 and 4; each skeptic's
  corrected fix is written below), 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 1 re-graded by the skeptic (id 2, from
  blocker to high).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 4 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 20 items, each assigned to exactly one of 5 lenses (security 4, correctness 4,
  seams 4, verification 4, intent 4).
- By design: the caller's byDesign list.

## HIGH

### H1. The 7j4 arm reds the govkit selftest suite on its own fixtures (id 2)

- **Where:** `tools/govkit/govkit.py:3289` (the liveness reds at `:3261-3262`, `:3289-3290` and `:3291-3293`).
- **Grade:** high. The finder graded it blocker, and the skeptic re-graded it high. This report
  takes the binding grade, high, and agrees with it: the failure is loud, it blocks landing, and
  nothing wrong ships.
- **Defect:** 7j4 runs unconditionally in every `selfcheck`. Its three liveness reds fire on the
  minimal scratch-gov trees that `tools/govkit/selftest.py` builds and expects to be green. Those
  reds are a manifest that is absent, zero legs graded, and zero self-test-shaped legs. The spec's
  gate list named only `govkit selfcheck` over the real tree, and its non-goal (DEPL-aBenchedProbe-1
  line 59) declined to touch selftest.py.
- **Impact:** in each case below, a fixture's selfcheck exits 1 where the suite asserts
  `returncode == 0`:
  - `scratch_gov` at selftest.py:3101 has one leg (`engine.sh`, no chunk). Zero legs are shaped,
    so the check at 3166 fails.
  - `scratch_gov` at 5019 has one leg (`true`, no chunk). Zero legs are shaped, so the check at 5128
    fails, and so does every later green assertion on trees derived from it: 5226, 5248, 5253,
    5268, 5275, 5322, 5334, 5381, 5394, 5413, 5509 and 5544.
  - The AC5 fixture (5426-5446) sets chunk `selftests` with subject `repo`, which is exactly 7j4's
    red predicate, so the check at 5446 fails.
  - `build_scratch_gov_kit` (5079) writes no gate-legs.json, so every selfcheck there also carries
    the 7j4 "absent" problem.
- **Fix (REJECTED by the skeptic; this is the skeptic's corrected fix):**
  1. Raise the zero-graded and zero-shaped liveness reds only when the population exists, meaning
     some row in gov's manifest has `chunk == 'selftests'`. Otherwise emit `r.note`.
  2. When gate-legs.json is absent, note it instead of failing, unless some descriptor declares a
     `[[gate_leg]]`.
  3. In AC5, keep subject `repo` and keep the pin-row assertion `_rowsc == ["demo\trepo\tselftests"]`.
     Change the exit expectation to `_wc.returncode == 1`, and assert that the output names
     `7j4: entry 'demo' gate leg 'demo'`. First confirm that `selfcheck --write` still writes the
     pin on a red run.
  4. Then run the full `python tools/govkit/selftest.py`.
- **Left-shift gate:** this class is a hand-named gate list that stays green while the bar reds.
  Make a spec's gate list for any unit that edits `tools/govkit/govkit.py` derive the govkit
  selftest leg from `tools/gate-legs.json`, rather than leaving it to the author. The cheapest way
  is a spec-tokens guard that maps `govkit.py` to the `govkit selftest` leg, so a spec naming only
  `govkit selfcheck` is refused. A unit that adds an unconditional `selfcheck` arm then owes the
  suite run that exercises the fixtures.

## MEDIUM

### H-M1. Nothing checks that the receipt records gov's ceiling after a keep, or that a kept bound survives a second update (ids 1, 4, 6)

- **Where:** `tools/govkit/selftest.py:2400`, `:2404` and `:2408` (the CE4 block). The guarded line
  is `tools/govkit/govkit.py:4179` (`"ceiling": _ce`).
- **Grade:** medium for all three findings, which is the binding grade. They are one gap reported
  by the security, seams and verification lenses.
- **Defect:** the S4 keep rule relies on the receipt recording gov's computed `_ce` and never the
  kept value. Both the spec (lines 111-113) and the comment at govkit.py:4176-4178 say so. No arm
  checks this:
  - CE4 runs one re-apply and reads only the target row.
  - CE5 rewrites both the row and the receipt by hand before its own apply.
- **Impact:** suppose line 4179 changes to `row.get("ceiling")`, which is the natural copy of its
  sibling lines. CE1 through CE5 all stay green. In production the receipt would then hold 3600, so
  the next update would see the target and the receipt agree and would silently overwrite the
  adopter's hand-raised bound with 1780. That is the clobber the security model forbids. Today's
  code is correct, so this is a missing guard and not a live defect.
- **Fix:** the skeptics judged the fixes for ids 1 and 6 SOUND. They REJECTED id 4's fix, and the
  corrected fix below agrees with the two sound ones. Apply it once:
  1. After the CE4 checks, assert `read_emitted().get(leg, {}).get("ceiling") == 1780`, so the
     receipt records gov's value and not the kept one.
  2. Call `settle(t, "the keep")`. Only then run a second
     `run("apply", "--target", str(t), "--kits", "push-main")`, with no edit to the row.
  3. Assert that the second apply has `returncode == 0` and `read_rows()[leg]["ceiling"] == 3600`,
     and that its stdout and stderr again contain "kept the target's ceiling".
  4. Leave the CE5 block unchanged after this. Its leading settle commits this apply.
- **Left-shift gate:** this class is containment tested one way. Every "keep the adopter's value"
  rule in govkit should carry a two-apply arm: apply, edit, apply, apply. The arm asserts the
  receipt's state between the two applies, and the third apply is the one that proves persistence.
  This could become a §10 checklist entry for the deployer stream: "a keep rule is tested across two
  re-applies, and the receipt is read between them".

### H-M2. Nothing that persists can fail 7j4's red and exempt branches, or the 7h ceiling clause (ids 7, 8)

- **Where:** `tools/govkit/govkit.py:3278` (7j4 exempt and subject test, id 7) and
  `tools/govkit/govkit.py:2758` (the 7h ceiling-agreement clause, id 8).
- **Grade:** medium for both findings, which is the binding grade.
- **Defect:** both arms were observed red only by manual staged breaks (AC1 and AC2 for 7j4, AC6
  for 7h), and those breaks left nothing behind:
  - **7j4 (id 7):** the S4 liveness reds do not catch an arm that exempts everything. If line 3278
    becomes `if chunk:`, the three chunk=selftests legs go into `_j4_exempt`. `_j4_shaped` is
    incremented before the exempt test, so it stays non-zero, and the arm stays green while it
    checks nothing. A weakened subject comparison has the same effect.
  - **7h (id 8):** the clause can be deleted, or lose its `d_ce != m_ce`, bool or positive-int
    conditions, and the real tree stays green, because its 1780 equals the manifest's 1780. The
    emitter does no validation of its own (N4), so a bad descriptor ceiling would then ship to
    every adopter unchecked.
- **Fix (both judged SOUND by the skeptics):** add a staged-break arm to selftest.py's gov-copy
  block, following the `check_halved_install_arms` precedent:
  - **7j4:** set `pre-push self-test` to subject `repo` in the copy's descriptor and gate-legs.json,
    and assert that selfcheck exits non-zero with a `7j4:` line naming the leg. Next, delete the
    `chunk` key from one chunk-bearing, filename-shaped row, and assert a 7j4 line naming the argv
    element. Restore the copy and assert green. If a fixture stays out of scope, the minimum is to
    count the legs that reach the subject comparison and red when that count is zero. That count
    catches the exempt-everything mutation.
  - **7h:** set the copy's push-main `pre-push self-test` ceiling to 1781, and then to `true`. In
    each case assert that selfcheck exits non-zero with a line containing "with ceiling" and naming
    push-main and the leg. Restore the copy and assert green.
- **Left-shift gate:** §7 says "a new gate is not landed until its failing case has been observed".
  A staged break that leaves no artifact cannot be re-observed. Add a §10 checklist entry, or a
  hygiene-style check on spec section 5 "testing", that refuses "manual staged break" as the only
  evidence for a new selfcheck arm unless a committed staged-break arm names it.

## LOW

### H-L1. A dead pre-initialisation of `manifest_chunk`, with a false comment (id 3)

- **Where:** `tools/govkit/govkit.py:2673`.
- **Grade:** low, which is the binding grade.
- **Defect:** `manifest_chunk: dict = {}` carries the comment "7j4 reads it unconditionally and
  refuses on an absent manifest". That comment is false. 7j4 reads the map only in the `else` of its
  own `if not legs_path.is_file()` guard (`:3261`), and on that path the 7h block has already
  rebound the map from the manifest. Nothing rebinds `legs_path` in between.
- **Impact:** behaviour does not change. The comment invites a later reader to drop 7j4's
  absent-manifest guard as redundant. Without that guard, 7j4 would go silently green on a tree
  with no manifest.
- **Fix (judged SOUND by the skeptic):** delete the pre-initialisation and its comment.
  Alternatively, keep the line only as a static-binding default and reword the comment to say that
  7j4 reads the map solely under its own `is_file` guard.
- **Left-shift gate:** this class is a guard above a fold that makes its fallback dead, and it is
  not mechanically gateable. Make it a §10 checklist entry: "a comment claiming a reader is
  unconditional is checked against that reader's own guard".

### H-L2. CE4's "naming the leg" check is not tied to the keep line (id 9)

- **Where:** `tools/govkit/selftest.py:2404` (the assertion at 2406-2407).
- **Grade:** low, which is the binding grade.
- **Defect:** the check `"kept the target's ceiling" in out and f"'{leg}'" in out` is two separate
  substring tests over the whole output. AC4 (spec lines 203-206) asks that the keep line itself
  name the leg. Other govkit prints quote the leg name in the same shape, for example the note at
  4099 and the UNGUARDED note at 4183. If one of them fired, CE4 would pass even when the keep print
  named the wrong leg.
- **Fix (judged SOUND by the skeptic):** assert on a single line, for example
  `f"gate leg '{leg}': kept the target's ceiling 3600" in out`, or
  `any("kept the target's ceiling" in ln and f"'{leg}'" in ln for ln in out.splitlines())`.
- **Left-shift gate:** add a §10 checklist entry: "an arm asserting that a line names X matches X
  within that line, never over the whole output".

## Refuted

- **Id 5** (seams, `tools/govkit/govkit.py:4154`) was refuted. The "(gov's is None)" wording in the
  keep message is accurate below CEILING_FLOOR_RUN_GATES, because None is what gov emits and what
  the receipt records there. The message gives no reason for the difference, so it cannot give a
  wrong one.

review-shape kind=diff-review round=1 intensity=full at=synth raw=9 confirmed=8 refuted=1 unverified=0 blocker=0 high=1 medium=5 low=2 agents=11 out-tokens=97922

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/govkit/selftest.py:2404 | medium | medium | confirmed | govkit.py:4176-4179 records `"ceiling": _ce` in the receipt, and the comment at 4160-4167 says the keep rule depends on that. No arm checks it. CE1 reads the receipt only after the first apply, where the row and _ce are both 1780, so a change to `row.get("ceiling")` would still pass. CE4 runs one re-apply and only reads the target row. CE5 rewrites the receipt's ceiling by hand before its apply. Under the hypothetical change, CE4's single re-apply would still keep 3600, because prev holds 1780 from the first apply, and the receipt would then hold 3600 with nobody reading it. The next real update would see the target and receipt agree and overwrite the adopter's bound with 1780, and CE1-CE5 would all stay green. Today's code is correct, so this is a missing regression guard on the security invariant, not a live defect. Graded medium. | sound | containment-tested-one-way |
| 2 | correctness | tools/govkit/govkit.py:3289 | blocker | high | confirmed | 7j4 (govkit.py:3260-3295) runs unconditionally inside selfcheck. selfcheck has no early return between 1738 and 3539, and Report.emit returns 1 on any problem. The diff leaves every selftest.py fixture unchanged; its only selftest change adds check_ceiling_emission. Fixture 1 (selftest.py:3101-3166): scratch_gov writes one manifest leg, 'demo leg', with argv engine.sh and no chunk, and the descriptor matches. The leg is graded (1) but not shaped (0), so 3292 reds and r0.returncode == 0 at 3166 fails. Fixture 2 (5019-5128): one leg, 'demo', with argv ['true'] and no chunk, so the same zero-shaped red fires. The 'GREEN when both facts agree' check at 5128 fails, and so does every later green assertion on trees derived from it. AC5 (5426-5446): the manifest row is set to chunk 'selftests' and the descriptor keeps subject 'repo', which is exactly 7j4's red predicate, so `_wc.returncode == 0` fails. The govkit selftest suite therefore goes red. The DEPL-aBenchedProbe-1 spec's non-goal (line 59) declined to add or touch selftest.py fixtures, so nothing caught this. The failure is loud: the close's suite run reds and blocks landing. Nothing wrong ships, so this is graded high rather than blocker. | unsound | hand-named-gate-list-green-while-the-bar-reds |
| 3 | correctness | tools/govkit/govkit.py:2673 | low | low | confirmed | The diff added govkit.py:2673. The only reads of manifest_chunk are at 2832, which sits inside the 7h `if legs_path.is_file():` block, and at 3271, which sits in the `else` of 7j4's own `if not legs_path.is_file():` guard at 3261. The only bindings of legs_path are at 2438 and 2672, so nothing rebinds it in between. On every path that reads the map, line 2683 has already rebound it from the manifest. That makes the pre-initialisation dead at runtime. Its comment says 7j4 reads the map unconditionally, which is false: 7j4 reads it conditionally and has its own refusal. Behaviour is unaffected, so the only harm is a misleading comment. | sound | guard-above-a-fold-makes-its-fallback-dead |
| 4 | seams | tools/govkit/selftest.py:2400 | medium | medium | confirmed | check_ceiling_emission (selftest.py:2328-2422) was added by this diff. CE4 runs one re-apply and checks only the row value (3600), the keep message, and that no drift refusal appears. It never reads the receipt's ceiling afterwards. CE5 then rewrites both the row and the receipt to 1000. Mutating govkit.py:4179 from `"ceiling": _ce` to `row.get("ceiling")` would leave 3600 in the receipt, and CE4 and CE5 would both still pass. On the next real update, govkit.py:4150 would then see tgt == prev == 3600, skip the keep, and silently write gov's 1780 over the adopter's raised bound. The production code is correct today, and a comment guards the line, so this is a missing test for the rule's stated main property, not a shipped wrong result. Its effect is contained. | unsound | - |
| 5 | seams | tools/govkit/govkit.py:4154 | low | - | refuted | At govkit.py:4105-4108, `_ce` is the ceiling gov actually emits to this target. Below CEILING_FLOOR_RUN_GATES gov emits none, so None is the value gov supplies there. It is also what the receipt records at line 4179 and what the keep comparison at line 4152 runs against. So "(gov's is None)" accurately describes gov's contribution to this target. The message claims no reason for the difference, so it cannot state one wrongly. The path is also narrow: a below-1.2 target whose adopter hand-added a ceiling key their runner may not read. At most this is a wording preference with no behavioural effect. | sound | - |
| 6 | verification | tools/govkit/selftest.py:2408 | medium | medium | confirmed | I traced the proposed mutation (line 4179 `"ceiling": _ce` changed to `row.get("ceiling")`) through check_ceiling_emission (selftest.py:2328-2426). CE1 passes because row and receipt both hold 1780 on a fresh install. CE4 passes because it checks only that the row is 3600, the keep line printed, and there is no drift refusal; it never reads the receipt after the keep. CE5 passes because it overwrites both row and receipt to 1000 before applying, so it never sees what the receipt recorded after the keep. No other check reads the emitted ceiling: grep finds only the CE arms, and selfcheck 7h at govkit.py:2758 grades the descriptor, not the receipt. The mutation therefore survives. In production it would record 3600, so on the next update the row matches the receipt and no keep fires. The adopter's hand-raised ceiling silently drops back to 1780, the exact overwrite the keep rule exists to prevent. Nothing ships wrong today; the gap only leaves a load-bearing property unguarded, so medium. | sound | - |
| 7 | verification | tools/govkit/govkit.py:3278 | medium | medium | confirmed | Confirmed. The diff adds nothing to tools/govkit/selftest.py that runs 7j4. The only new selftest code is check_ceiling_emission, which never calls selfcheck. The spec's own non-goal (DEPL-aBenchedProbe-1 line 59) gives the reason as 'S4 liveness reds catch a predicate that stops matching'. That reason is wrong for the finder's mutation. If line 3278 becomes `if chunk:`, the three chunk=selftests legs go into _j4_exempt. _j4_shaped stays non-zero because the increment happens before the exempt test. So neither liveness red fires, and the real tree (all three legs subject kit) stays green. The same holds if the subject test is weakened. AC1/AC2 were manual staged breaks that left nothing behind. The repo already has a precedent for exactly this class: check_halved_install_arms, whose docstring says hand-observed reds were committed as staged breaks after an earlier closing review. The spec non-goal is not in the BY DESIGN list; item (8) covers only the zero-population reds. Graded medium: the arm is correct today, and the gap only lets a future regression of the arm through. | sound | - |
| 8 | verification | tools/govkit/govkit.py:2758 | medium | medium | confirmed | Confirmed. The 7h ceiling clause (govkit.py ~2758) is exercised only by AC6, which DEPL-aBenchedProbe-2 section 5 'testing' calls a manual staged break. check_ceiling_emission tests the emitter and the keep rule only; it never runs selfcheck on a descriptor whose ceiling disagrees. In the real tree the descriptor's 1780 equals the manifest's 1780. So deleting the clause, or dropping its bool, positive-int or equality conditions, leaves every bar green. N4 says the emitter does no validation and relies on S5, so a bad descriptor value would then reach adopters' manifests unchecked. Graded medium: the code is correct today, and the gap is a missing regression guard for a gov-authored input. | sound | - |
| 9 | intent | tools/govkit/selftest.py:2404 | low | low | confirmed | selftest.py:2406-2407 asserts `"kept the target's ceiling" in out and f"'{leg}'" in out`. These are two separate substring checks over the whole combined stdout+stderr, so nothing ties the leg name to the keep line. AC4 (spec lines 203-206) asks for the keep line naming the leg. govkit.py has other prints that quote the leg name in the same `gate leg '{nm}':` shape, for example the doc_reads-omitted note at 4099 and the UNGUARDED note at 4183. If one of those fired for 'pre-push self-test', CE4 would pass even when the keep print at 4154 named a different leg or no leg. This was introduced by this diff (check_ceiling_emission is new). The effect is limited to a self-test arm that checks less than its label claims. Shipped behaviour does not change, and the arm still catches the keep line going missing altogether. Low. | sound | - |
