# dFoldedAudit — orientation: dClosedLoop against the new spec-audit rules

**Serves:** research TOOL-dFoldedAudit-1

## The question

# Orientation question 2: dClosedLoop's design against the new spec-audit principles

The owner is changing BUILD-METHOD M4 for SPEC audits only; closing DIFF reviews stay as they are. New rules:
R1. A declared review chain STOPS when no BLOCKER or HIGH stands and every spec is fully reviewed; units promoted by
    the audit are reviewed before the chain stops.
R2. Local fixes fold in place with revisions bumped.
R3. Spec reviews promote only findings that need new mechanisms.
R4. A repair unit may edit its sibling's spec with a rev bump.
R5. Stop at the first round whose highs all sit in the previous round's own promotions.

The owner said: review dClosedLoop's design and chain of specs for spec audit principles, and introduce these changes
only if applicable.

Read memory/builds/dClosedLoop/README.md, its held spec memory/builds/dClosedLoop/spec/2026-10-20-spec-PLAY-dClosedLoop-1.md,
the design records under memory/builds/dClosedLoop/build/ and the chain's driver builds' specs listed in the live index
memory/LIVE.md. Find every statement of a spec-audit principle: where a spec, ownership table, policy key, state
machine, gate or loop stage assumes promote-everything, the precision floor, REVIEW_ROUNDS or a chain stop. Also find
the reuse of M4 by dBoundRoles, dGroundRules, dTrueNorth, dDeclaredLoop and the other chain builds that are not yet landed.

Report, read-only:
A. Per statement: path:line, the quoted claim (under 15 words), whether it conflicts with R1 to R5, and the smallest
   change. Mark each as CONFLICTS, SILENT or AGREES.
B. Which chain builds are LANDED (changes then belong in tools/) and which are HELD (changes belong in their specs).
   Check `refs/gov/runs/<slug>` run claims and memory/LIVE.md, and name any held build whose spec we may not touch
   because a live run claims it.
C. Does the design make spec-audit stopping a POLICY key or a stage in a loop table? If so, which key and which file.

Write nothing in the repository. Return at most 80 lines. Cite every claim by path:line.

## The return, verbatim

# Orientation: dClosedLoop against spec-audit rules R1 to R5 (`TOOL-dFoldedAudit-1`)

**The rules apply to three unbuilt specs and M4 itself, not to dClosedLoop's own spec.** DL-32, DL-20 and FH-17 need changes. PLAY-dClosedLoop-1 needs none, because it restates no design fact (spec:659). v2 is frozen, so its clauses change only by deviation record (v2:1809-1811), and a change caused by an owner ruling needs the owner's quoted approval (FQ:194).
**Correction to the task's split:** a `landed` claim does not mean code landed. Only dTrueNorth and dGroundRules reached `tools/`. The other 15 landed spec runs, so their changes belong in specs (see B).

Paths: `ROOT` = `C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b`; `B` = `ROOT\memory\builds`.
- BM `ROOT\memory\guides\BUILD-METHOD.md` · spec `B\dClosedLoop\spec\2026-10-20-spec-PLAY-dClosedLoop-1.md` · README `B\dClosedLoop\README.md`
- Under `B\dClosedLoop\build\`, prefix `<date>-build-PLAY-dClosedLoop-1-`: v2 `2026-10-14…architecture-v2.md`, FS `2026-10-15…flow-steps.md`, GR `2026-10-14…gap-register.md`, EP `2026-10-20…execution-plan.md`, FQ `2026-10-19…final-questions.md`
- DL-n `B\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-n.md`; FH-n, BR-n, TN-n, ID-n, FO-n are `TOOL-<build>-n` specs under each build's `spec\`; DK-1 `B\dKeptSession\spec\2026-10-26-spec-KICK-dKeptSession-1.md`
- STOP `B\dFurnishedOrders\prompts\2026-10-27-prompt-TOOL-dFurnishedOrders-1-owner-review-stop.md`

## Card
**task:** Title: dClosedLoop against R1 to R5. Goal: find every spec-audit assumption in the design and chain. IN: the statements, build states and policy keys below. OUT: any write; closing DIFF reviews. To-do: A, B, C. Reuse: `review.design.rounds`, DL-20, DL-21, DL-32; no new seam. Acceptance: every claim cited, 80 lines or fewer. Gates: none in this pass. Slug: the parent's, none minted.
**manifest:** `ROOT\memory\guides\SESSION-KICKOFF.md`, stamped 2026-10-28 @ `c3292622a`. Audit NOT run: `scratch-guard` refused it as gate leg G1, so the main session owes it. BASE `f4597719e4b1ff0f0f779998bd7b8c2ce5213088` on `branch/gov-build-m4-spec-audit-694e7b`, 0 ahead and 0 behind `origin/main`.
**read:** BM:115-148, spec:628-983, README, `ROOT\memory\LIVE.md`, the skill's Steps 0-4, v2 by grep and row. BM is a rendered kit file: edit `ROOT\tools\memory-tree\BUILD-METHOD.template.md`; 29354 of 30720 bytes used (BM:8).
**records:** `TOOL-aProbedUnit-9` (`ROOT\memory\DECISIONS.md:114`), `TOOL-aWokenSentinel-30`, `TOOL-dLoggedFlight-34`, `TOOL-aProvenReuse-3`, STOP; round 14 was owed in dWitnessedBar (`B\dWitnessedBar\build\2026-10-25-build-TOOL-dWitnessedBar-1-departures-spec.md:19`). Top asks by rank are unrelated: `TOOL-dUnstuckLanding-11`, `-26`. Recall terms used: spec-audit REVIEW_ROUNDS BOUNDED CONVERGED promoted precision floor chain review.design.rounds disposition severity.
**classes:** 36 by anchor plus 6 universal; I read only the first 30 output lines, including `two-answers-to-one-question`, `fixture-passes-by-finding-nothing`, `guard-above-a-fold-makes-its-fallback-dead`.

## A. Statements
143 spec files across 17 chain builds cite "BUILD-METHOD M4". I read a sample plus every hit on the key terms, not all 143. "Historic" means the text records why a unit exists, so it stays as written.

| Where | Claim | Mark | Smallest change |
|---|---|---|---|
| BM:144 | "A SPEC subject takes `REVIEW_ROUNDS` rounds (protocol §8) and exits BOUNDED" | CONFLICTS R1 | A round bound can stop with a HIGH standing; add the R1 stop |
| BM:144 | "a MEDIUM or LOW is PROMOTED too" | CONFLICTS R2 R3 | Rewrite the disposal for spec subjects; DIFF text stays |
| BM:144 | "The CHAIN of promotions is bounded by PRECISION." | CONFLICTS R1 R5 | Replace it; only a tuning lever states a floor (`ROOT\memory\guides\REVIEW-PROTOCOL.md:179`), never read (GR:455) |
| BM:146-148 | "CONVERGED is terminal for its subject, rev bumps included" | CONFLICTS R1 R2 | Scope to DIFF, or a folded spec cannot be re-reviewed |
| README:41 | "the declared spec audit runs before any chain build opens" | SILENT | None |
| spec:659 | "This spec restates no design fact." | SILENT | None |
| spec:772-773 | "every finding is folded or rejected with its reason" | AGREES R2 | None |
| v2:1253, FS:816 | "1 spec review by default" | CONFLICTS R1 | The key counts one subject's rounds; see O1 |
| v2:1769 (`cl-0117`) | "whose findings are promoted", "never folded into another round" | CONFLICTS R1 R2 R3 R5 | Take spec subjects out, by deviation record |
| v2:1260 | "a blocking item's open work promoted to a new unit" | CONFLICTS R3 | Same deviation record |
| v2:1261 | "one budget per build" every review round after the first draws on | CONFLICTS R1 | Can end a chain with a HIGH standing; see O2 |
| v2:914-916 | "A built unit's spec is frozen" | AGREES R2, bounds R4 | Word R4 as an unbuilt sibling |
| FS:266-267, :575 | "Each round folds into the unbuilt specs before the next" | AGREES R2 | None |
| FQ:187 | Legitimate: "a review finding before close" | AGREES R2 R4 | None; approver re-audits changed sections |
| GR:455, FQ:176 | "a round's own fold caused 68% to 97%" of next findings | AGREES R5 | None; this is the design's own evidence |
| v2:1236 | "stops strictly falling, its findings promoted" | SILENT | None; closing review, out of scope |
| EP:741-742 | "a spec run may carry forward a `DEFERRED` unit it added" | SILENT | None |
| DL-32:21-26 | "ends at the first round whose blocker and high count does not strictly fall" | CONFLICTS R1 R2 R3 R5 | Split spec subjects out; keep for follow-ups and fix passes |
| DL-32:46-50 | "`until-no-high` and `after-high` the blockers and highs" | AGREES R1 | None; closest existing value, per subject |
| DL-20:127-128 | "unbuilt to `item.review.fold`" | AGREES R2 | None |
| DL-20:127-128 | "NON-CONVERGENT or CEILING promoted to units" | CONFLICTS R3 | Limit to built work or a new mechanism |
| DL-20:86-88 | "its default reading unchanged" | CONFLICTS R3 | Rebase S9 on the rewritten sentence at BM:144 |
| DL-21:315 | "`REVIEW_ROUNDS` bounds one subject while promotions mint fresh ones" | AGREES R1 | None; names the defect R1 fixes |
| FH-17:64-65 | "the floor's chain rule is BUILD-METHOD M4's" | CONFLICTS R1 | Re-point to the new stop rule |
| BR-66:26, DL-56:27, ID-38:26, FO-29:28 | "BUILD-METHOD M4 promotes every minor, batched into one unit" | CONFLICTS R3, historic | No edit; see O3 |
| FH-23:372, TN-10:135-136 | "the owner's 2026-10-05 ruling (BUILD-METHOD M4) folds none" | CONFLICTS R2, historic | No edit; resolved records |
| STOP:7, :24 | "stop reviewing once there are no HIGHs left"; "No audit names them." | AGREES, then CONFLICTS R1 | No edit; R1's second clause reverses it |

## B. Landed and held
| State | Builds | Evidence | Changes go to |
|---|---|---|---|
| Built, CLOSED | dTrueNorth (30 of 30), dGroundRules (80 CLOSED, 6 WONTDO) | Ids cited in 30 and 67 product files | `tools/` |
| Spec run landed, HELD | dOrderedCharter, dFairHearing, dDeclaredLoop, dPlacedRequest, dKeptSession, dBoundRoles, dFurnishedOrders, dTotalRecall, dLinkedLibrary, dMindYourWords, dWellOiledMachine, dWitnessedBar, dRankedPlan, dIndexedDesign | Claim `terminal`, 0 product-file cites, 0 landed-unclosed (`ROOT\memory\LIVE.md:9`) | Their specs, each edit re-owing review (BM:121-122) |
| **Do not touch: HELD, live run** | dSafePassage | Claim `live`, beat 821 s, `check 107` (`ROOT\memory\guides\UNATTENDED-STOPS.md:218`) | Nowhere until it ends |
| In flight, no spec on main | dShippedRelease (`live`, 2363 s); dScopedBuild (`stale`, 5906 s); dTendedCadence (`stale`, 7138 s) | Past the bound of 5400 (`ROOT\.unattended.conf:95`); `stale` is takeable by the driver, not by us (UNATTENDED-STOPS.md:220) | Leave alone; see O4 |
| Not started | dCalibratedLens, dConvergedCharter | No claim, 0 specs | Inherit the new M4 |

Verdicts come from `unattended.sh --claims` at about 18:39Z. Ignore the local `refs/gov/runs/dTrueNorth`: it reads `live` from 2026-10-22, but the remote reads `landed`. dWellOiledMachine has 1 CLOSED unit and dRankedPlan 2, yet neither has product-file cites; I did not trace why.

## C. Is stopping a policy key or a stage?
**Both by design, and neither is what stops an audit today.**
- **Policy key:** `review.design.rounds` with `review.design.round-count`, ceiling `review.max-rounds`, in `ROOT\tools\policy\catalogue.toml:710-727`; the effective value `one` is at `ROOT\.governance\policy.json:934-938`. No tool reads these keys. The real bound is `REVIEW_ROUNDS` (`ROOT\.unattended.conf:111`, `ROOT\tools\unattended\PROTOCOL.template.md:487`) until DL-21:65 retires it.
- **Loop stage:** the rows `item.review.dispose` and `item.review.fold` (DL-20:127-128) belong in `tools/loop/loop.toml` (DL-20:48), which is unbuilt: `tools/loop` has 0 tracked files.
- **Gaps:** no key or row holds a chain-level stop, so R1 and R5 have no home but M4. `review.findings` reads only built work (DL-20:127), so R3 has no key either. The owner is dDeclaredLoop (`catalogue.toml:713`); `2026-10-17-…-ownership.md:327` naming dCalibratedLens was overturned by `2026-10-18-…-audit-fold.md:30-32`.

## open
| Id | Question | Options | Decided by |
|---|---|---|---|
| O1 | Where does R1 live? | (a) M4 prose, key stays `one`; (b) default `until-no-high`; (c) new chain-level key | Owner: must R1 be adjustable per repo? (b) and (c) are policy-key changes (FQ:193) and touch presets (v2:1572-1574, DK-1:146) |
| O2 | Does a budget or ceiling outrank R1? | (a) budget wins, recorded incomplete; (b) R1 wins for spec audits; (c) park | Owner; `flow.on-exhausted` defaults to best-effort (v2:1262) |
| O3 | Do already-promoted minor batches stand? | (a) keep them; (b) retire `WONTDO` and fold into their targets (BM:58-59) | Owner: is R3 retroactive? (b) re-owes review of each target |
| O4 | Which M4 do in-flight runs use? | (a) finish under the old text; (b) adopt at the next pass boundary | Owner, by when the change lands relative to those runs |
| O5 | May R4 reach a built sibling? | (a) unbuilt only; (b) any | Owner's wording; (b) collides with P19 and FQ:187 |
| O6 | Declare `spec-audit:` for dFoldedAudit? | Yes or no; recommend yes if two or more units | Owner; README is empty, default unset (`ROOT\.unattended.conf:326`) |

## Run notes
- **Side effect:** my one recall query evicted the recall cache of the worktree `unattended-dshipped-release-1a351d`, whose dShippedRelease claim is live. Only a cache under the common git dir was affected; that run rebuilds it on its next query (13 s here). The tree is unchanged.
