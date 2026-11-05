**Serves:** research TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32

# dDeclaredLoop — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record [`2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck`](2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group A, citation, led by spec 21 (specs 21 and 32)

Group A (specs 21 and 32): 21 rows, of which 11 AGREES, 9 MISMATCH and 1 UNKNOWN UNTIL BUILT. All probes were reads at `ab976b5b3` (the worktree HEAD), with `git show 63669d505` for the diff and `git show 783f1ad3a:` for the earlier state.

1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| dl21:53-56 | `review_state` keeps fh17's `deriveRoundState` test order: zero, then non-decrease, then ceiling, then bound | cite | AGREES | fh17:89-95, fh17:97-99 |
| dl21:55-56 | the ceiling is one round past the limit (`n + 1 > max-rounds`) and the bound is reached at the limit | cite | AGREES | fh17:92-93; fh17:99-102 says "one run past the caller's limit, and its bound becomes the limit itself" |
| dl21:61-63, dl21:197 | fh17 S5's parity arm slices the `RUNAWAY_CEILING=` line, so dl21 re-points it to take the ceiling "as its own variable" with fh17's domain unchanged | cite | MISMATCH | fh17:173-174 checks "a limit of 1 to 4 with the round at or below it"; dl21 does not say what value the arm's ceiling variable takes (see bullet M1) |
| dl21:61-63 | the parity arm already exists in `tools/workflows/tier2-review.test.sh` when dl21 builds | cite | UNKNOWN UNTIL BUILT | fh17 is DEFERRED; `grep -c "deriveRoundState\|RUNAWAY_CEILING" tools/workflows/tier2-review.test.sh tools/workflows/tier2-review.js` printed 0 and 0 |
| dl21:125-126, dl21:138 | the convergence routing (dl32) passes `review.max-rounds` to fh17's harness as `roundLimit` | cite | MISMATCH | fh17:79-80 is the parent's edge; no dDeclaredLoop scope item passes `roundLimit` (bullet M2) |
| dl21:62-63 (the harness reads no key) | the limit reaches fh17 only as the caller's argument | cite | AGREES | fh17:62-63 |
| dl21:301 | rev-1 read fh17 at base `ed497191` | cite | AGREES | a record line only; fh17 §9 rev-4 at fh17:379-380 moves nothing dl21 reads |
| dl21:149-154 | a spec audit's rounds read `NON-CONVERGENT` "when the count did not fall" | SA | MISMATCH | dl32:52-55 and dl32:125 now gate the non-decrease test with `no-fall` (bullet M3) |
| dl21:124-126 | promoting a NON-CONVERGENT or CEILING round's findings is dl32's, on every subject | SA | MISMATCH | dl32:23-26 says M4's spec-audit rule disposes a spec audit's findings (bullet M4) |
| dl21:83-87 | an `until-*` value's stopping rule is dl32's, bounded by `review.max-rounds` | SA | AGREES | dl32:47-55: target or bound, with `no-fall` |
| dl21:41-43 | the spec bound under `until-*` is `review.max-rounds`, and no chain stop is read from it | SA | AGREES | dl32:23-25; fh17:64-65; `memory/guides/BUILD-METHOD.md:148` |
| dl21:73, F4 at dl21:292-296 | the `REVIEW_ROUNDS` reader in `BUILD-METHOD.template.md` is at :144 | SA | MISMATCH | the M4 rewrite split it: `grep -n REVIEW_ROUNDS tools/memory-tree/BUILD-METHOD.template.md` prints :144 and :148, and :148 is the chain paragraph fh17:64-65 now points at (bullet M5) |
| dl21:241-244 (AC4) | `review_state` called with three positional arguments | SA | AGREES | dl32:123 makes arguments 4 to 6 optional, so the three-argument call is unchanged |
| dl32:98-100 | `deriveRoundState` already counts blockers plus highs, and the parity arm holds where arguments 4 and 6 are unset | cite | AGREES | fh17:110-111; fh17:173-174 (three-argument domain) |
| dl32:351-356 (F1) | fh17's parity arm holds the closed set of five tokens | cite | AGREES | fh17:89-95, fh17:175-176 |
| dl32:396-398 | fh17's reuse audit agrees with source | cite | AGREES | fh17:384-390 (but see line 6 on its stale cite) |
| dl32:105-106 | "the `roundLimit` it passes" | cite | MISMATCH | same cause as dl21:125-126 (bullet M2) |
| dl32:132-137 | the four existing tests "stay as that unit leaves them", and "with neither new argument" the function is byte-for-byte its predecessor | SA | MISMATCH | dl32:125 rewrites the second test, and there are now three new arguments (bullet M6) |
| dl32:175, dl32:227 | "A review loop's open findings go to asks once the budget is spent"; "turns the rule on for every subject" | SA | MISMATCH | dl32:56-63 and dl32:21-25 (bullet M7) |
| dl32:72-75 (S6) | check 2's non-decrease reading adds `round-highs` and applies to every subject | SA | MISMATCH | `tools/unattended/check-unattended.sh:1008` and :1058-1059 (bullet M8) |
| dl32:112-113 | dl20's `review.dispose` promotes by the ` · to units` / ` · to asks` target dl32 writes | SA | MISMATCH | dl20:128 routes by budget itself (bullet M9) |

2. MISMATCH

- **M1 (dl21:61-63).** dl21 says the arm "slices the constant's line and takes the ceiling as its own variable instead". The parent's domain is "a limit of 1 to 4 with the round at or below it" (fh17:173-174), and today's driver ceiling is 8 (`tools/unattended/unattended.sh:911`), which no row of that domain reaches. After dl21 the ceiling is `n + 1 > max-rounds`. If the arm sets that variable to the default 3, as dl21:63-64 does for the `ceiling of 8` arms, then the row with limit 4 and round 4 reads CEILING in the driver and BOUNDED in the harness. **Change:** S3 states the value: the arm sets the ceiling variable to each row's limit (or to at least 4). **Cause:** pre-existing.
- **M2 (dl21:125-126 / dl32:105-106).** dl21 says dl32's routing "also passes `review.max-rounds` to dFairHearing-17's harness as `roundLimit`". The parent says "dDeclaredLoop's convergence routing passes `review.max-rounds` as `roundLimit` and routes on `roundState`" (fh17:79-80; fh17:345-346 adds "one rule replaces both"). But `grep -n roundLimit\|roundState` over the dDeclaredLoop specs finds only dl21:126, dl21:138 and dl32:106: no scope item makes that call or routes on `roundState`. dl32:98-100 and :253-254 keep the two rules apart. There is also an SA problem: `deriveRoundState` has no `no-fall`, so passing `review.max-rounds` for a spec subject would stamp NON-CONVERGENT on a flat round and BOUNDED at max-rounds instead of at the spec bound. **Change:** either dl32 gains a scope item that passes `roundLimit` for the build slug only, or dl21:125-126, :138 and dl32:106 drop the claim and say that no dDeclaredLoop unit takes up fh17's edge. **Cause:** pre-existing; rev-3 widened the SA side of it.
- **M3 (dl21:151-152).** dl21 reads "`NON-CONVERGENT` when the count did not fall", applied to the spec-audit row at :149. dl32:52-53 says "A spec subject takes no non-decrease test: `verb_review` passes `review_state` a sixth argument, `no-fall`", and dl32:125 gates the test. **Change:** §4 says the non-decrease reading applies to the closing-review subject only, and that a spec audit passes `no-fall` (dl32 S3) and ends at its target, `BOUNDED` or `CEILING`. **Cause:** revision `63669d505`.
- **M4 (dl21:124-126).** dl21 says "no promotion of a NON-CONVERGENT or CEILING round's findings: TOOL-dDeclaredLoop-32's convergence routing". dl32:24-26 says "BUILD-METHOD M4's spec-audit rule disposes its findings and stops its chain. A follow-up's or a fix pass's open findings are promoted…". **Change:** the non-goal names dl32 for follow-ups and fix passes, and M4's spec-audit rule through dl20's dispose row for spec audits. **Cause:** revision `63669d505`.
- **M5 (dl21:73).** dl21 lists the reader as "`tools/memory-tree/BUILD-METHOD.template.md` (:144)". The template now has a second mention at :148: "Each generation is a FRESH subject, so `REVIEW_ROUNDS` bounds no chain". That is the derived-verdict paragraph fh17:64-65 points at. **Change:** S4 lists :144 and :148 and rewords :148 so that no policy key reads as a chain stop. AC5's `git grep` over `tools` would catch it anyway. **Cause:** revision `63669d505` (fh17 rev-4 points at M4 as `5699553e8`, TOOL-dFoldedAudit-1, rewrote it after `783f1ad3a`).
- **M6 (dl32:132-137).** dl32 says "The four existing tests and their order are `TOOL-dDeclaredLoop-21`'s and stay as that unit leaves them … With neither new argument the function is byte-for-byte its predecessor". Its own grammar at dl32:125 reads "no-fall unset, prior non-empty and count >= last prior -> NON-CONVERGENT", and dl32:123 has three new arguments. **Change:** the paragraph says the second test is gated by `no-fall`, and that with the 4th, 5th and 6th arguments all unset the behaviour equals dl21's (behaviour, not bytes). **Cause:** revision `63669d505`.
- **M7 (dl32:175 and dl32:227).** dl32:175 says "A review loop's open findings go to asks once the budget is spent". dl32:227 says "The landing turns the rule on for every subject at once." Against these, dl32:61-63 says "A spec subject's target is always ` · to units`", and dl32:21-25 limits the strict-fall rule to follow-ups and fix passes. **Change:** :175 reads "A closing-review loop's", and :227 reads "every closing-review and fix-pass subject". **Cause:** revision `63669d505`, which edited the second sentence at :227 and left the first.
- **M8 (dl32:72-75).** S6 says check 2's "non-decrease reading (`:842`) adds `round-highs` to `blockers`" for every subject. The code is now at `check-unattended.sh:1008` (`if (it in last && b >= last[it]) flat[it] = …`), and :1058-1059 reds "blocker counts did not shrink … so the loop is non-convergent" whenever a subject has no terminal token. A `no-fall` spec subject that is legally CONVERGING on a flat count, with the run stopped before its bound, is read as non-convergent. **Change:** S6 limits the `flat` reading to the build slug and fix-pass rows, adds an AC7 plant of a flat non-terminal spec subject that must stay green, and updates the line cite. **Cause:** revision `63669d505`.
- **M9 (dl32:112-113).** dl32's edge says "`review.dispose` promotes by the ` · to units` or ` · to asks` target this unit writes", and dl32:61-63 says a spec subject always gets ` · to units` "because a budget does not outrank a spec audit's chain stop". dl20:128 instead says "NON-CONVERGENT or CEILING on built work or for a new mechanism promoted to units while budget remains and to asks after", reading `flow.rework-budget`. **Change:** dl20's dispose row (its owner, Group B) says a spec subject's new-mechanism promotion takes dl32's target, which is always units. Until then, dl32's edge states the exception explicitly. **Cause:** revision `63669d505` (both texts came from that one commit).

3. UNKNOWN UNTIL BUILT

- dl21:61-63: whether fh17's parity arm exists, and slices `RUNAWAY_CEILING=` as fh17:171-172 writes it, before dl21 builds. dFairHearing's build run decides this. If fh17 lands after dl21, its arm fails on a missing line (fh17:177).

4. Hits no rule binds

- dl32:42 and dl32:128: the route-back NON-CONVERGENT. dl32:43 passes route-backs for the build slug only, so no spec audit can reach it.
- dl32:148-151 `while-finding` minors-only NON-CONVERGENT: this is a closing-review follow-up, which keeps strict fall.
- dl32 AC1, AC3 and AC10's bare slices (dl32:279, :289, :325): these are calls on no subject, and none is a spec audit.
- dl32:196 fix-pass NON-CONVERGENT: fix passes keep strict fall under SA.

5. Revised parent sections no assumption depends on

- dl21: fh17 §3's chain-stop non-goal (fh17:64-65, rev-4) is not depended on. M5 is caused by the M4 rewrite it points at, not by the non-goal itself.
- dl32: fh17 §3's chain-stop non-goal (fh17:64-65) is not depended on either.

6. Parent text that looks wrong

- fh17:79-80 and fh17:345-346 hand `roundLimit` passing and routing on `roundState` to a dDeclaredLoop unit that does not exist.
- fh17 S4 (fh17:164-165): every synthesis stamps `state=` from a rule with no `no-fall`, so an attended flat spec-audit round records `NON-CONVERGENT`, which SA says a spec subject never reads.
- fh17:384 cites `review_state` at `unattended.sh:12594-12618`. That range now holds `declared_list`, `RUNAWAY_CEILING=` is at :911, and the function has moved.

## Group B, siblings, SA only, led by spec 30 (specs 2, 10, 13, 14, 18, 22, 30, 31, 33, 48, 49, 50 and 56)

No dDeclaredLoop spec was edited. Every probe below was a read against `ab976b5b3`. Group B came out as 3 MISMATCH, 13 AGREES and 0 UNKNOWN. All three mismatches come from the dl32 rev-3 revision (`63669d505`), and two of them are in spec 30, which leads this group. `git diff --stat 783f1ad3a ab976b5b3` is empty for specs 30, 31 and 13, so their text did not move: dl32 moved under them.

1. Table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| dl30 | dl32 owns "the strict-decrease routing of every `until-*` and `while-*` value, and promoting a non-converging loop's findings" | SA | MISMATCH | dl30:92-94 vs dl32:21-25, dl32:52-55, dl32:110-111 |
| dl30 | Past `flow.route-backs`, any item's loop ends `non-converging`, a spec subject included, since S4 draws `review-round` per subject | SA | MISMATCH | dl30:47-48, dl30:52-53, dl30:62-63, dl30:217-218 vs dl32:43 |
| dl30 | A `review-round` draw that answers `exhausted` stops the repetition at every subject's later round, so a spent budget ends a spec audit before its target or bound | SA | MISMATCH | dl30:52-57, dl30:139-142 vs dl32:23-24, dl32:53-55, dl32:61-63 |
| dl30 | dl32 calls `promotion_target` and `count_returns` and promotes against them | SA | AGREES for the build slug and for fix passes, which is all dl30 claims | dl30:104; dl32:56-60, dl32:69-70, dl32:108-109 |
| dl30 | dl32 S2's route-back test counts `review-round` draws per subject after its first round | SA | AGREES | dl30:52-53; dl32:42-43 |
| dl31 | "When a loop ends and where its findings go" is dl32's convergence routing, for every loop | SA | MISMATCH | dl31:83-84 vs dl32:23-25, dl32:110-111 |
| dl31 | dl32 records ` · to on-exhausted` for a fix-pass loop past route-backs once the budget is spent | SA | AGREES | dl31:104-105; dl32:67-70, dl32:114-115, dl32:173 |
| dl13 | B10: `item.review.dispose` in `building`, outcome "built: a new unit", goes to `designing` | SA | AGREES | dl13:145, dl13:236-237; dl20:128 ("built work and a new mechanism to new units") |
| dl14 | The per-item route-back limit on a re-dispatch of a refused instance belongs to units 30 and 32 | SA | AGREES (a re-dispatch is not a spec subject, so the rev-3 cut in dl32 S2 does not reach it) | dl14:55-56; dl30:62-66; dl32:43 |
| dl22 | A binding `review` score prints the trigger line dl20's verb takes | SA | AGREES (the trigger row and S2 were not revised) | dl22:105-106; dl20:51-53, dl20:127 |
| dl50 | dl20's dispose and fold rows route "as `TOOL-dDeclaredLoop-20` §4", and the dispose actor is the driver | SA | AGREES (it defers to the routes, so it picks up the rev-3 text) | dl50:87-88; dl20:128-129 |
| dl50 | dl20 S1, §3 and AC1 name the four rows with bare actors, and dl20's verbs, fields and counts stay unchanged | SA | AGREES (these parts were not revised) | dl50:22-30, dl50:54, dl50:63; dl20:48, dl20:127-130, dl20:275 |
| dl56 | S6: `refusal` joins the read-side `PARK_KINDS` copies "as dl32 does for `fix-pass`" | SA | AGREES | dl56:109-111; dl32:70-71, dl32:198-199 |
| dl56 | S23: dl20's class count reads the appendix (`measure_class_occurrences`) | SA | AGREES (S6 was not revised) | dl56:165-168, dl56:264; dl20:74-77 |
| dl56 | S35: every spelled `--review` carries dl32's `--round-highs` | SA | AGREES | dl56:201-203, dl56:275; dl32:34-36, dl32:76-78 |
| dl56 | The fix-pass kind and the flag are dl32's, and dl56 assumes no `review_state` shape | SA | AGREES | dl56:275; dl32:123 (dl56 never calls `review_state`) |

2. MISMATCH

- **dl30 Non-goal: the strict-decrease routing.**
  - dl30:92-94: "the strict-decrease routing of every `until-*` and `while-*` value, and promoting a non-converging loop's findings, are TOOL-dDeclaredLoop-32's".
  - dl32:23-25: "A spec audit under `review.design.rounds`' `until-*` values ends at its target or its bound, and BUILD-METHOD M4's spec-audit rule disposes its findings and stops its chain".
  - dl32:52-53: "A spec subject takes no non-decrease test".
  - Change: limit the non-goal to `while-*` follow-ups and fix passes. Then add that a spec audit's stop and disposal belong to M4's spec-audit rule (`memory/guides/BUILD-METHOD.md:146-148`), not to dl32.
  - Cause: the revision (`63669d505`, dl32 rev-3 §1 and S3). At `783f1ad3a`, dl32:1 read "every until and while loop ends on a non-decrease".

- **dl30 S6 and AC5: the per-item early limit.**
  - dl30:62-63: "`count_returns(build, item)` counts the draws naming the item; past `flow.route-backs` that item's loop ends `non-converging`".
  - dl30:52-53 has `verb_review` draw `review-round` "for every round of a subject after its first", and dl30:47-48 makes the subject the draw's `<item>`. A spec subject therefore counts as such an item.
  - dl32:43: "`verb_review` passes it for the build slug and for no spec subject".
  - Change: S6 should say the early limit ends follow-up, fix-pass and route-back items only, and that a spec subject's draws are counted but never end its loop (dl32 S2, S3).
  - Cause: the revision. At `783f1ad3a`, dl32:41 read "`verb_review` passes it for every subject".

- **dl30 S4 and "The driver, in shell": `exhausted` stops a spec audit round.**
  - dl30:57: "Each site reads `exhausted` and stops the repetition".
  - dl30:141-142: "`exhausted` exits 3, and the verb refuses the repetition with a line naming the budget and `flow.on-exhausted`".
  - That applies to every subject's `review-round` (dl30:52-53).
  - dl32:53-55: "an `until-*`, `one` or `fixed-count` subject ends at its target or its bound, and whether another generation runs is the chain's verdict, not this loop's".
  - dl32:61-62: "a budget does not outrank a spec audit's chain stop".
  - Change: dl30 S4 must say whether a spec subject's `review-round` draw refuses the round at `exhausted`. If it does, dl32 S3 must name that third exit for a spec subject and say where its open findings go under M4. If it does not, S4 must exempt spec subjects from the stop and keep the row.
  - Cause: the revision. Before rev-3, dl32 had every loop promote by budget, so a budget stop was consistent with it.

- **dl31 Non-goal: when a loop ends.**
  - dl31:83-84: "When a loop ends and where its findings go: `TOOL-dDeclaredLoop-32`'s convergence routing. Its ` · to on-exhausted` target is what sends a build here."
  - dl32:24-25: "BUILD-METHOD M4's spec-audit rule disposes its findings and stops its chain".
  - dl32:110-111: "consumes-from external — BUILD-METHOD M4's spec-audit rule, which owns a spec subject's disposal and its chain stop".
  - Change: limit the line to follow-up and fix-pass loops, and name M4's spec-audit rule as the owner of a spec audit's end and disposal. The ` · to on-exhausted` sentence is unaffected.
  - Cause: the revision (dl32 rev-3 §1 and §3).

3. UNKNOWN UNTIL BUILT

None.

4. Hits no rule binds

- dl2:294, dl2:374: `review.max-rounds` is a guarded policy key in a fixture. The key belongs to dl21, not dl20 or dl32.
- dl18:76: `policy-key.review.max-rounds` is cited only as an example of a `carries.py` node id.
- dl33:269, dl33:278: `review.max-rounds` is a raised loop bound in the `raise` rule. dl33:151-156 terminates loops by the dl30 budget's counted edges, not by dl32's stopping rule.
- dl10:57: the budget draw for a route back is dl30's (`flow.rework-budget`), which the revision did not touch.
- dl48:1, dl48:25-26, dl48:40: the budget's home and draw sites are dl30's. Nothing there relies on dl20 or dl32.
- dl49:1, dl49:25-26: the spent count across records is dl30's. Nothing there relies on dl20 or dl32.
- dl22:352-353: `review_state` appears only as a `reuse_lookup` hit in the reuse audit, with no shape assumed.
- dl56:532 (AC35), dl56:216 (S40): `review.design.rounds` in the review-rounds upgrade step. That step is dl21's, and its value set and stopping rule are not assumed.
- dl30:267 (F3): "TOOL-dDeclaredLoop-20's items" refers only to item tags, which the revision left alone.
- dl14:120, dl14:163, dl14:191: `chain` is a frontier fixture plant name. It is not a review chain.

5. Citation specs

None: Group B is siblings only and SA only, with no fh17 citation population.

6. Parent text that looks wrong

- dl20:128 sends "NON-CONVERGENT or CEILING ... for a new mechanism ... to units while budget remains and to asks after". dl32:61-63 says a spec subject's target "is always ` · to units`". A spec audit's new-mechanism finding with the budget spent therefore routes two different ways.
- dl20:129 (the `item.review.fold` row) and dl20:83-85 (S8) still give the spec fold a NON-CONVERGENT route. Under dl32:52-55 (`no-fall`), a spec subject never reads NON-CONVERGENT.

The dDeclaredLoop specs are at `C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dDeclaredLoop\spec\` (`2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`). M4 is at `C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\guides\BUILD-METHOD.md`, lines 146-148.
