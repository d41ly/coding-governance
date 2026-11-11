**Serves:** research TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-5

# dPlacedRequest's specs against the parent revisions it had not read: a read-only cross-check

Node d, 2026-11-05, base `ab976b5b3` (origin/main). dPlacedRequest's last cross-read was `2740f0a3d`. Since then `git log 2740f0a3d..ab976b5b3 -- memory/builds/<parent>/spec/` over its parents (dDeclaredLoop) names `63669d505` (2026-11-02, TOOL-dFoldedAudit-8: TOOL-dDeclaredLoop-20 and -32 to rev-3, TOOL-dFairHearing-17 to rev-4), generated-region rewrites and the no-op merge `e5de11e9e` apart. The owner asked for this pass on 2026-11-05, after a verification found these revisions unread. This record is not an audit: no spec was edited by it, and its mismatches feed the re-ground brief [`2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-reground`](../prompts/2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-reground.md).

**Counts:** 17 assumptions · 16 AGREES · 1 MISMATCH · 0 UNKNOWN UNTIL BUILT, over 6 specs with rows. 1 spec holds a MISMATCH: 5 (row 6). By rule: 1 cite.

## Method

- **Population by citation.** the same probe over the three revised units: 4 specs, 3 (dl20 at :182, :342), 5 (dl20 at :70, :89, :267, :280, :288), 7 (dl20 at :71, :174, :402) and 34 (dl20 at :269). None cites dl32 or fh17.
- **Population by rule.** The SA probe named 3 (:383), 14 (:40, :246, :252) and 16 (:28, :84); every hit is a rework-budget line or a past exit and none relies on a revised unit. The rules: **SA**, the spec-audit rules: a spec subject takes `no-fall`, ends at its target or bound and is promoted ` · to units`; dl20's dispose row folds a local finding on an unbuilt spec; a chain's stop is BUILD-METHOD M4's derived verdict (dl32:47-63, dl20:86-89, :128, fh17:64-65).
- **Readers.** One `gov-spec-reviewer` agent, read-only, one per group of the brief [`2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md), their handoffs beside it (group A, led by spec 3). Their returns, every MISMATCH's both sides quoted with its `Change:` and `Cause:`, are [`2026-11-05-build-TOOL-dPlacedRequest-1-crosscheck-returns`](2026-11-05-build-TOOL-dPlacedRequest-1-crosscheck-returns.md).
- **The main loop** assembled the table below from the returns' tables by script, stable-sorted by spec, and derived the counts from it. It re-read both sides of the rows the re-ground brief names and changed no verdict.
- **Aliases:** `prN:L` is line L of this build's spec N; `dlN:L`, `fhN:L`, `trN:L`, `prN:L`, `ksN:L`, `brN:L` and `llN:L` of dDeclaredLoop's, dFairHearing's, dTotalRecall's, dPlacedRequest's, dKeptSession's, dBoundRoles' and dLinkedLibrary's spec N; all at `ab976b5b3`.
- **What it does not check:** the rules this build's 2026-10-26 cross-read applied; anything a parent's build run decides. dOrderedCharter's and dFairHearing's live build runs on node a were not read, only their specs on main. The probes are a text heuristic. No skeptic re-ran the verdicts; the writer re-reads both sides before it edits.
- **The fork fold.** A sibling session was folding the owner's picks on the chain's 47 open forks while the readers ran. Rows are read at `ab976b5b3`; the re-ground re-checks every row that fold moved before it edits.

## Summary table

| # | Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | 3 | A row tagged `item.review.trigger` exists in the loop definition and takes the `breakpoint` route (pr3:182, "TOOL-dDeclaredLoop-20 S1") | cite | AGREES | dl20:48-50 S1 lists four rows in `tools/loop/loop.toml`, tagged `item.review.trigger` and three others. Row at dl20:127. rev-3 did not touch S1. |
| 2 | 3 | The trigger fires with `--cause placement` (pr3:182) | cite | AGREES | dl20:51-52: "`<c>` is one of `owed`, `opt-in`, `recommendation`, `placement`". Also dl20:139. |
| 3 | 3 | dl20 adds its own rows to `tools/loop/loop.toml` as rows, with no factory (pr3:342, F3 "as TOOL-dDeclaredLoop-12 and -20 land gov's own rows") | cite | AGREES | dl20:48 S1 rows in `tools/loop/loop.toml`. dl20:132-133 "The rows take the field names `TOOL-dDeclaredLoop-9` and `TOOL-dDeclaredLoop-12` give every item row". |
| 4 | 5 | A placed breakpoint fires through dl20's `--trigger <slug> --subject <s> --cause placement`, with no new verb (pr5:70-71) | cite | AGREES | dl20:51-52 S2. dl20:139 "`--trigger <slug> --subject <s> --cause owed\ | opt-in\ | recommendation\ | placement`". |
| 5 | 5 | The `--trigger` verb, its causes and `review.blocks` belong to dl20 and are called by name (pr5:89) | cite | AGREES | dl20:51-58 S2, dl20:79-82 S7. |
| 6 | 5 | The roster's hand-out is held until a placed spec audit's verdict is terminal, whatever `review.blocks` is (pr5:81-82 S7; goal pr5:28-29 "cannot pass that position without it"; flow pr5:116-118) | cite | MISMATCH | dl20:80 "`owed-only`, held only when the trigger cause is `owed`"; dl20:149-150; dl20:202-203 "under `owed-only` with a cause other than `owed`, the hand-out follows the audit's start". pr5:71 fires with `--cause placement`. |
| 7 | 5 | Provenance: rev-1 drafted from dl20, read at base `c63aabbb` (pr5:267) | cite | AGREES | This is history and makes no claim about today's text. dl20's S1, S2 and S7 are unchanged by rev-3 (`git show 63669d505` touches only dl20 S9 and the row at :128). |
| 8 | 5 | dl20's closed cause set already holds `placement`, so pr5 is only a caller (pr5:280) | cite | AGREES | dl20:52, :139-140 ("refuse a cause outside the set"). |
| 9 | 5 | `check_review_ended` is the name dl20 gives the predicate at `unattended.sh:12762` when it extracts it (pr5:286-288) | cite | AGREES | dl20:53-54. dl20:147 "`check_review_ended` is the grep pipeline at `tools/unattended/unattended.sh:12762`". |
| 10 | 5 | A placed spec audit runs on `<slug>-specs` until its verdict is terminal. pr5 states no exit word (pr5:74, :82) | SA | AGREES | dl32:52-55: a spec subject ends "at its target or its bound". BOUNDED, CONVERGED and CEILING are still terminal. pr5 names no NON-CONVERGENT exit, no budget route, no fixed `review_state` shape and no chain stop. |
| 11 | 7 | `probe.trigger` copies `review.trigger`'s flag shape (pr7:70-71, :174, :402, "TOOL-dDeclaredLoop-20 S2") | cite | AGREES | dl20:51-52 `--trigger <slug> --subject <s> --cause <c>`. S2 is untouched by rev-3. |
| 12 | 7 | `review.trigger`'s cause set is a literal held in the driver, and the review harness also reads it. Moving it onto the table would re-point both readers (pr7:162-164, F3 at :376-380) | cite | AGREES | dl20:52 (the literal set in the driver verb). dl20:59-61 S3 (harness "taking `trigger` as an argument validated in the closed set S2 names"). |
| 13 | 7 | SA applied: pr7 states no spec-audit routing | SA | AGREES | No probe hit beyond record-table and rev-log lines (pr7:36, :176, :388). |
| 14 | 14 | SA applied: no spec-audit exit or disposal | SA | AGREES | Hits pr14:40, :246, :252 are rework-budget lines (see section 4). |
| 15 | 16 | SA applied: no spec-audit exit or disposal | SA | AGREES | Hits pr16:28, :84 are rework-budget lines (see section 4). |
| 16 | 34 | dDeclaredLoop's loop kit `tools/loop/` exists before this run with `kit.toml`, `selftest.py` and `loop_lib.load_tree_lib`, and dl20 is one of the units that builds it (pr34:269) | cite | AGREES | dl20:227-229 Files touched: `tools/loop/loop.toml`, `review_dispose.py`, `selftest.py`. dl20:330 adds an arm on `tools/loop/selftest.py`. dl92:50-58 owns `load_tree_lib`. None of this changed in rev-3. |
| 17 | 34 | SA applied: a spec audit's findings disposed by severity (pr34:29-33) | SA | AGREES | This disposal rests on BUILD-METHOD M4, not on dl20, dl32 or fh17, and it records a past exit (see section 4). |

## The one MISMATCH

Row 6 is pre-existing, not the revision's: pr5 S7 holds the roster's hand-out until a placed spec audit's verdict is terminal (pr5:81-82), while pr5:71 fires that audit with `--cause placement` and dl20 S7 holds the hand-out under `review.blocks = owed-only` only when the cause is `owed` (dl20:80, :202-203). AC1 checks only the preflight's owed line, so it stays green either way. dl20 S7 read the same at `2740f0a3d`.

## The seventh `--lease status` field

TOOL-dTotalRecall-2 rev-8, this build's child, asks pr34 S22's `--lease status` for a seventh TAB field after `<epoch>`. No dPlacedRequest spec pins the line at six fields: pr34 S22 names the six in prose (pr34:106-108), AC22 (pr34:468-470) and pr49 AC28 (pr49:358-360) check only the session and exit 0, and a grep for `six (tab )?fields|six-field|NF ?==|exactly (six|6)` over every dPlacedRequest spec printed nothing. The appended field reds no criterion; S22's prose takes the seventh field when dTotalRecall's run files the ask.

## Parent text that looks wrong (not edited)

- dl20 S8, the fold row at dl20:129 and AC1 at dl20:278 still give `item.review.fold` a NON-CONVERGENT route, which a spec subject under dl32's `no-fall` never reaches. Folded by dDeclaredLoop's re-ground of the same date, its own spec.
- dl20:127 and dl20:114-115 refuse a round past `flow.route-backs` for every subject, while dl32:43 applies that bound to the build slug only. Folded by dDeclaredLoop's re-ground.

## For the re-ground

One spec, by one row: pr5, row 6. The fold taken, by the owner's standing rule that a question with a no-worse option is decided and recorded: S6 fires the Design-exit audit with `--cause owed` once `AUTH_SPEC_AUDIT_FROM` holds `placement`, which is what the preflight's owed line AC1 reads already says it is, and keeps `placement` for the at-once firing past the position; AC1 or AC6 gains a plant under `review.blocks = owed-only` that reds when the hand-out is not held. The alternative, S7 conceding the hold under `owed-only`, breaks pr5's goal (pr5:28-29).

## After the re-ground

The owner's fork fold landed on origin/main at `11ebd1e87` after the readers ran, and this branch fast-forwarded to it before any spec was edited. Three rows (1 to 3) sit on pr3, which the fold revised; none of the lines they cite changed, and they still read AGREES.

The writers' returns are [`2026-11-05-build-TOOL-dPlacedRequest-1-reground-returns`](2026-11-05-build-TOOL-dPlacedRequest-1-reground-returns.md). The writer re-read both sides at the tip and refused no row. pr5 moved to rev-5. Past the item's letter, S5 and AC5 changed too, since dl19 S6 fires a breakpoint with the cause S5 lists: a placed spec audit at Design's exit is listed `owed`, every other placed name `placement`.

Two points go to the build pass, unedited: a record placed mid-run by the lease holder is listed `owed` though `--close`'s term is not owed until the next preflight; and dl19 S2 may list a second `spec audit` breakpoint at Design's exit with cause `opt-in`, beside pr5's `owed` one, with no rule merging two breakpoints at one position (dl19's text, predating both revisions).

Each revised spec carries one spec-revised record: [`2026-11-05-build-TOOL-dPlacedRequest-5-deviation-53`](2026-11-05-build-TOOL-dPlacedRequest-5-deviation-53.md). No fork was opened or resolved.
