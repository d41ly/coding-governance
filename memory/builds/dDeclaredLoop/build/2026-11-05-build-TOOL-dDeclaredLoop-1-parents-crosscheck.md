**Serves:** research TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32

# dDeclaredLoop's specs against the parent revisions it had not read: a read-only cross-check

Node d, 2026-11-05, base `ab976b5b3` (origin/main). dDeclaredLoop's last cross-read was `783f1ad3a`. Since then `git log 783f1ad3a..ab976b5b3 -- memory/builds/<parent>/spec/` over its parents (dOrderedCharter and dFairHearing) names `63669d505` (2026-11-02, TOOL-dFoldedAudit-8: TOOL-dDeclaredLoop-20 and -32 to rev-3, TOOL-dFairHearing-17 to rev-4), generated-region rewrites and the no-op merge `e5de11e9e` apart. The owner asked for this pass on 2026-11-05, after a verification found these revisions unread. This record is not an audit: no spec was edited by it, and its mismatches feed the re-ground brief [`2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground`](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md).

**Counts:** 37 assumptions · 22 AGREES · 14 MISMATCH · 1 UNKNOWN UNTIL BUILT, over 9 specs with rows. 4 specs hold a MISMATCH: 21 (rows 5, 7, 10, 11 and 14); 30 (rows 17, 18 and 19); 31 (row 22); 32 (rows 27, 28, 29, 30 and 31). By rule: 11 SA, 3 cite.

## Method

- **Population by citation.** the same probe for TOOL-dFairHearing-17, the one revised parent unit: 2 specs, 21 (fh17 at :56, :62, :126, :197, :301) and 32 (fh17 at :354, :397).
- **Population by rule.** `63669d505` also revised two of this build's own units, dl20 and dl32, from another build, after every sibling was written and cross-read. The SA probe outside the generated regions named 2, 10, 13, 14, 18, 22, 30, 31, 33, 48, 49, 50 and 56; a sibling relying on dl20's dispose row or S9, or on dl32's stopping rule, target rule or grammar, is bound as if it cited them. The rules: **SA**, the spec-audit rules: a spec subject takes `no-fall`, ends at its target or bound and is promoted ` · to units`; dl20's dispose row folds a local finding on an unbuilt spec; a chain's stop is BUILD-METHOD M4's derived verdict (dl32:47-63, dl20:86-89, :128, fh17:64-65).
- **Readers.** Two `gov-spec-reviewer` agents, read-only, one per group of the brief [`2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md), their handoffs beside it (group A, led by spec 21; group B, led by spec 30). Their returns, every MISMATCH's both sides quoted with its `Change:` and `Cause:`, are [`2026-11-05-build-TOOL-dDeclaredLoop-1-crosscheck-returns`](2026-11-05-build-TOOL-dDeclaredLoop-1-crosscheck-returns.md).
- **The main loop** assembled the table below from the returns' tables by script, stable-sorted by spec, and derived the counts from it. It re-read both sides of the rows the re-ground brief names and changed no verdict.
- **Aliases:** `dlN:L` is line L of this build's spec N; `dlN:L`, `fhN:L`, `trN:L`, `prN:L`, `ksN:L`, `brN:L` and `llN:L` of dDeclaredLoop's, dFairHearing's, dTotalRecall's, dPlacedRequest's, dKeptSession's, dBoundRoles' and dLinkedLibrary's spec N; all at `ab976b5b3`.
- **What it does not check:** the rules this build's 2026-10-26 cross-read applied; dOrderedCharter, whose specs did not move; anything a parent's build run decides. dOrderedCharter's and dFairHearing's live build runs on node a were not read, only their specs on main. The probes are a text heuristic. No skeptic re-ran the verdicts; the writer re-reads both sides before it edits.
- **The fork fold.** A sibling session was folding the owner's picks on the chain's 47 open forks while the readers ran. Rows are read at `ab976b5b3`; the re-ground re-checks every row that fold moved before it edits.

## Summary table

| # | Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | 13 | B10: `item.review.dispose` in `building`, outcome "built: a new unit", goes to `designing` | SA | AGREES | dl13:145, dl13:236-237; dl20:128 ("built work and a new mechanism to new units") |
| 2 | 14 | The per-item route-back limit on a re-dispatch of a refused instance belongs to units 30 and 32 | SA | AGREES | dl14:55-56; dl30:62-66; dl32:43 |
| 3 | 21 | (dl21:53-56) `review_state` keeps fh17's `deriveRoundState` test order: zero, then non-decrease, then ceiling, then bound | cite | AGREES | fh17:89-95, fh17:97-99 |
| 4 | 21 | (dl21:55-56) the ceiling is one round past the limit (`n + 1 > max-rounds`) and the bound is reached at the limit | cite | AGREES | fh17:92-93; fh17:99-102 says "one run past the caller's limit, and its bound becomes the limit itself" |
| 5 | 21 | (dl21:61-63, dl21:197) fh17 S5's parity arm slices the `RUNAWAY_CEILING=` line, so dl21 re-points it to take the ceiling "as its own variable" with fh17's domain unchanged | cite | MISMATCH | fh17:173-174 checks "a limit of 1 to 4 with the round at or below it"; dl21 does not say what value the arm's ceiling variable takes (see bullet M1) |
| 6 | 21 | (dl21:61-63) the parity arm already exists in `tools/workflows/tier2-review.test.sh` when dl21 builds | cite | UNKNOWN UNTIL BUILT | fh17 is DEFERRED; `grep -c "deriveRoundState\ | RUNAWAY_CEILING" tools/workflows/tier2-review.test.sh tools/workflows/tier2-review.js` printed 0 and 0 |
| 7 | 21 | (dl21:125-126, dl21:138) the convergence routing (dl32) passes `review.max-rounds` to fh17's harness as `roundLimit` | cite | MISMATCH | fh17:79-80 is the parent's edge; no dDeclaredLoop scope item passes `roundLimit` (bullet M2) |
| 8 | 21 | (dl21:62-63 (the harness reads no key)) the limit reaches fh17 only as the caller's argument | cite | AGREES | fh17:62-63 |
| 9 | 21 | (dl21:301) rev-1 read fh17 at base `ed497191` | cite | AGREES | a record line only; fh17 §9 rev-4 at fh17:379-380 moves nothing dl21 reads |
| 10 | 21 | (dl21:149-154) a spec audit's rounds read `NON-CONVERGENT` "when the count did not fall" | SA | MISMATCH | dl32:52-55 and dl32:125 now gate the non-decrease test with `no-fall` (bullet M3) |
| 11 | 21 | (dl21:124-126) promoting a NON-CONVERGENT or CEILING round's findings is dl32's, on every subject | SA | MISMATCH | dl32:23-26 says M4's spec-audit rule disposes a spec audit's findings (bullet M4) |
| 12 | 21 | (dl21:83-87) an `until-*` value's stopping rule is dl32's, bounded by `review.max-rounds` | SA | AGREES | dl32:47-55: target or bound, with `no-fall` |
| 13 | 21 | (dl21:41-43) the spec bound under `until-*` is `review.max-rounds`, and no chain stop is read from it | SA | AGREES | dl32:23-25; fh17:64-65; `memory/guides/BUILD-METHOD.md:148` |
| 14 | 21 | (dl21:73, F4 at dl21:292-296) the `REVIEW_ROUNDS` reader in `BUILD-METHOD.template.md` is at :144 | SA | MISMATCH | the M4 rewrite split it: `grep -n REVIEW_ROUNDS tools/memory-tree/BUILD-METHOD.template.md` prints :144 and :148, and :148 is the chain paragraph fh17:64-65 now points at (bullet M5) |
| 15 | 21 | (dl21:241-244 (AC4)) `review_state` called with three positional arguments | SA | AGREES | dl32:123 makes arguments 4 to 6 optional, so the three-argument call is unchanged |
| 16 | 22 | A binding `review` score prints the trigger line dl20's verb takes | SA | AGREES | dl22:105-106; dl20:51-53, dl20:127 |
| 17 | 30 | dl32 owns "the strict-decrease routing of every `until-*` and `while-*` value, and promoting a non-converging loop's findings" | SA | MISMATCH | dl30:92-94 vs dl32:21-25, dl32:52-55, dl32:110-111 |
| 18 | 30 | Past `flow.route-backs`, any item's loop ends `non-converging`, a spec subject included, since S4 draws `review-round` per subject | SA | MISMATCH | dl30:47-48, dl30:52-53, dl30:62-63, dl30:217-218 vs dl32:43 |
| 19 | 30 | A `review-round` draw that answers `exhausted` stops the repetition at every subject's later round, so a spent budget ends a spec audit before its target or bound | SA | MISMATCH | dl30:52-57, dl30:139-142 vs dl32:23-24, dl32:53-55, dl32:61-63 |
| 20 | 30 | dl32 calls `promotion_target` and `count_returns` and promotes against them | SA | AGREES | dl30:104; dl32:56-60, dl32:69-70, dl32:108-109 |
| 21 | 30 | dl32 S2's route-back test counts `review-round` draws per subject after its first round | SA | AGREES | dl30:52-53; dl32:42-43 |
| 22 | 31 | "When a loop ends and where its findings go" is dl32's convergence routing, for every loop | SA | MISMATCH | dl31:83-84 vs dl32:23-25, dl32:110-111 |
| 23 | 31 | dl32 records ` · to on-exhausted` for a fix-pass loop past route-backs once the budget is spent | SA | AGREES | dl31:104-105; dl32:67-70, dl32:114-115, dl32:173 |
| 24 | 32 | (dl32:98-100) `deriveRoundState` already counts blockers plus highs, and the parity arm holds where arguments 4 and 6 are unset | cite | AGREES | fh17:110-111; fh17:173-174 (three-argument domain) |
| 25 | 32 | (dl32:351-356 (F1)) fh17's parity arm holds the closed set of five tokens | cite | AGREES | fh17:89-95, fh17:175-176 |
| 26 | 32 | (dl32:396-398) fh17's reuse audit agrees with source | cite | AGREES | fh17:384-390 (but see line 6 on its stale cite) |
| 27 | 32 | (dl32:105-106) "the `roundLimit` it passes" | cite | MISMATCH | same cause as dl21:125-126 (bullet M2) |
| 28 | 32 | (dl32:132-137) the four existing tests "stay as that unit leaves them", and "with neither new argument" the function is byte-for-byte its predecessor | SA | MISMATCH | dl32:125 rewrites the second test, and there are now three new arguments (bullet M6) |
| 29 | 32 | (dl32:175, dl32:227) "A review loop's open findings go to asks once the budget is spent"; "turns the rule on for every subject" | SA | MISMATCH | dl32:56-63 and dl32:21-25 (bullet M7) |
| 30 | 32 | (dl32:72-75 (S6)) check 2's non-decrease reading adds `round-highs` and applies to every subject | SA | MISMATCH | `tools/unattended/check-unattended.sh:1008` and :1058-1059 (bullet M8) |
| 31 | 32 | (dl32:112-113) dl20's `review.dispose` promotes by the ` · to units` / ` · to asks` target dl32 writes | SA | MISMATCH | dl20:128 routes by budget itself (bullet M9) |
| 32 | 50 | dl20's dispose and fold rows route "as `TOOL-dDeclaredLoop-20` §4", and the dispose actor is the driver | SA | AGREES | dl50:87-88; dl20:128-129 |
| 33 | 50 | dl20 S1, §3 and AC1 name the four rows with bare actors, and dl20's verbs, fields and counts stay unchanged | SA | AGREES | dl50:22-30, dl50:54, dl50:63; dl20:48, dl20:127-130, dl20:275 |
| 34 | 56 | S6: `refusal` joins the read-side `PARK_KINDS` copies "as dl32 does for `fix-pass`" | SA | AGREES | dl56:109-111; dl32:70-71, dl32:198-199 |
| 35 | 56 | S23: dl20's class count reads the appendix (`measure_class_occurrences`) | SA | AGREES | dl56:165-168, dl56:264; dl20:74-77 |
| 36 | 56 | S35: every spelled `--review` carries dl32's `--round-highs` | SA | AGREES | dl56:201-203, dl56:275; dl32:34-36, dl32:76-78 |
| 37 | 56 | The fix-pass kind and the flag are dl32's, and dl56 assumes no `review_state` shape | SA | AGREES | dl56:275; dl32:123 (dl56 never calls `review_state`) |

## The MISMATCHes

Eleven of the fourteen are the revision's: dl32 rev-3 took spec audits out of the strict-fall and budget routing (dl32:21-25, :52-55, :61-63), and four places that say otherwise were left behind.

- **dl21, rows 10, 11 and 14 (SA).** §4 reads a spec audit's rounds as NON-CONVERGENT on a flat count (dl21:149-154); the non-goal at dl21:124-126 gives a spec audit's promotion to dl32; S4 lists the `REVIEW_ROUNDS` reader at `BUILD-METHOD.template.md:144` only, while the M4 rewrite added a second at :148, the chain paragraph fh17:64-65 now points at.
- **dl30, rows 17, 18 and 19 (SA).** The non-goal gives dl32 every `until-*` value's strict-decrease routing (dl30:92-94); S6 ends any item's loop past `flow.route-backs`, a spec subject included (dl30:62-63), while dl32:43 passes route-backs for the build slug only; S4 stops every subject's repetition on an `exhausted` draw (dl30:57, :141-142), while dl32:61-62 says a budget does not outrank a spec audit's chain stop.
- **dl31, row 22 (SA).** The non-goal gives "when a loop ends and where its findings go" to dl32 for every loop (dl31:83-84).
- **dl32, rows 28 to 31 (SA), the rev-3 fold's own text.** §4 still calls the function byte-for-byte its predecessor "with neither new argument" though its grammar now has three (dl32:132-137); :175 and :227 still route every review loop to asks and turn the rule on for every subject; S6 widens check 2's non-decrease reading to every subject, though `check-unattended.sh:1058-1059` would then red a legally flat `no-fall` spec subject; :112-113 says `review.dispose` promotes by the target dl32 writes, while dl20:128 routes a spec audit's new mechanism by the budget itself.
- **Three pre-existing (cite): rows 5, 7 and 27.** dl21 S3 does not say what ceiling the re-pointed parity arm takes, so fh17's limit-4 row reads CEILING in the driver and BOUNDED in the harness (dl21:61-63, fh17:173-174); dl21:125-126, :138 and dl32:105-106 say dl32 passes `review.max-rounds` to fh17's harness as `roundLimit`, which no dDeclaredLoop scope item does.

## Unknown until built

- Row 6: whether fh17's parity arm exists, slicing `RUNAWAY_CEILING=`, before dl21 builds. dFairHearing's build run, live on node a, decides it.

## Sibling text found wrong, folded here

dl20 is this build's own spec, so what the readers report about it is folded by this re-ground rather than parked:
- dl20:128 sends a spec audit's new-mechanism finding to asks once the budget is spent, while dl32:61-63 gives a spec subject ` · to units` always (dl-A M9, dl-B line 6).
- dl20 S8 (dl20:83-85), the fold row (dl20:129) and AC1 (dl20:278) give `item.review.fold` a NON-CONVERGENT route a `no-fall` spec subject never reaches (dl-B line 6, dPlacedRequest's reader).
- dl20:127 and dl20:114-115 refuse a round past `flow.route-backs` for every subject, while dl32:43 bounds the build slug only (dPlacedRequest's reader).
- dl20:128 lists no plan-revision or landing-record route, while dl20:106-108 and :133-134 say both are its declared routes (dRankedPlan's reader; pre-existing).

## Parent text that looks wrong (not edited)

- fh17:79-80 and :345-346 hand `roundLimit` passing and routing on `roundState` to a dDeclaredLoop unit that does not exist.
- fh17 S4 (fh17:164-165) stamps every synthesis's `state=` from a rule with no `no-fall`, so an attended flat spec-audit round records NON-CONVERGENT.
- fh17:384 cites `review_state` at `unattended.sh:12594-12618`; the range now holds `declared_list` and `RUNAWAY_CEILING=` is at :911.
dFairHearing's build run is live on node a; these three go to its owner, not into its specs.

## For the re-ground

Four specs from the rows and one from the sibling text: dl21 (rows 5, 7, 10, 11, 14), dl30 (rows 17, 18, 19), dl31 (row 22), dl32 (rows 27 to 31) and dl20 (the four sibling items). The decisions taken: the `roundLimit` claim is dropped from dl21 and dl32 and fh17's edge is reported, since adding a unit to take it up is a new mechanism; a spec subject's `review-round` draw is still counted but an `exhausted` answer does not refuse its round; a spec audit's end and disposal are named as BUILD-METHOD M4's spec-audit rule's; check 2's flat reading is limited to the build slug and fix-pass rows, with a plant of a flat non-terminal spec subject that stays green.

## After the re-ground

The owner's fork fold landed on origin/main at `11ebd1e87` after the readers ran, and this branch fast-forwarded to it before any spec was edited. Twenty-four rows sit on dl13, dl14, dl21, dl30 or dl56, which the fold revised for TOOL-dDeclaredLoop-56 F5 (a)'s `enforces` lines; none of the lines they cite changed, and every verdict stands.

The writers' returns are [`2026-11-05-build-TOOL-dDeclaredLoop-1-reground-returns`](2026-11-05-build-TOOL-dDeclaredLoop-1-reground-returns.md). Both writers re-read both sides at the tip and refused no row. dl32 and dl20 moved to rev-4 under group A, dl30 and dl21 to rev-4 and dl31 to rev-3 under group B. Three edits went past an item's letter, each named in its spec's §9: dl32's S4 sentence and target-table rows say closing review; dl31's S5, §4 "The lap refusal" and AC2 except a spec subject's round, to agree with dl30 S4 as revised; dl21 leaves the parity arm's ceiling variable unnamed, because naming `MAX_ROUNDS` reds hygiene check 25 with no tracked reader.

Left for the build passes, unedited: dl20 S5 and "The unverified route" still count a `block` verification round against `flow.route-backs` on every subject; dl32 §4 "The target" cites `check-unattended.sh:845-848`, now near :1028-1033; dl32 S6 widens check 2's stalled-loop arm to `fix-pass` rows, which today matches `review` rows only; and BUILD-METHOD template :144 still says a spec subject "exits BOUNDED", which dl21 S4's rewording should bring to "its target or its bound".

Each revised spec carries one spec-revised record: [`2026-11-05-build-TOOL-dDeclaredLoop-20-deviation-201`](2026-11-05-build-TOOL-dDeclaredLoop-20-deviation-201.md), [`2026-11-05-build-TOOL-dDeclaredLoop-21-deviation-213`](2026-11-05-build-TOOL-dDeclaredLoop-21-deviation-213.md), [`2026-11-05-build-TOOL-dDeclaredLoop-30-deviation-303`](2026-11-05-build-TOOL-dDeclaredLoop-30-deviation-303.md), [`2026-11-05-build-TOOL-dDeclaredLoop-31-deviation-311`](2026-11-05-build-TOOL-dDeclaredLoop-31-deviation-311.md), [`2026-11-05-build-TOOL-dDeclaredLoop-32-deviation-321`](2026-11-05-build-TOOL-dDeclaredLoop-32-deviation-321.md). No fork was opened or resolved.
