**Serves:** research TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-5

# dPlacedRequest — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` return the cross-check record [`2026-11-05-build-TOOL-dPlacedRequest-1-parents-crosscheck`](2026-11-05-build-TOOL-dPlacedRequest-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group A, citation and SA, led by spec 3 (specs 3, 5, 7, 14, 16 and 34)

1. Assumption table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 3 | A row tagged `item.review.trigger` exists in the loop definition and takes the `breakpoint` route (pr3:182, "TOOL-dDeclaredLoop-20 S1") | cite | AGREES | dl20:48-50 S1 lists four rows in `tools/loop/loop.toml`, tagged `item.review.trigger` and three others. Row at dl20:127. rev-3 did not touch S1. |
| 3 | The trigger fires with `--cause placement` (pr3:182) | cite | AGREES | dl20:51-52: "`<c>` is one of `owed`, `opt-in`, `recommendation`, `placement`". Also dl20:139. |
| 3 | dl20 adds its own rows to `tools/loop/loop.toml` as rows, with no factory (pr3:342, F3 "as TOOL-dDeclaredLoop-12 and -20 land gov's own rows") | cite | AGREES | dl20:48 S1 rows in `tools/loop/loop.toml`. dl20:132-133 "The rows take the field names `TOOL-dDeclaredLoop-9` and `TOOL-dDeclaredLoop-12` give every item row". |
| 5 | A placed breakpoint fires through dl20's `--trigger <slug> --subject <s> --cause placement`, with no new verb (pr5:70-71) | cite | AGREES | dl20:51-52 S2. dl20:139 "`--trigger <slug> --subject <s> --cause owed\|opt-in\|recommendation\|placement`". |
| 5 | The `--trigger` verb, its causes and `review.blocks` belong to dl20 and are called by name (pr5:89) | cite | AGREES | dl20:51-58 S2, dl20:79-82 S7. |
| 5 | The roster's hand-out is held until a placed spec audit's verdict is terminal, whatever `review.blocks` is (pr5:81-82 S7; goal pr5:28-29 "cannot pass that position without it"; flow pr5:116-118) | cite | MISMATCH | dl20:80 "`owed-only`, held only when the trigger cause is `owed`"; dl20:149-150; dl20:202-203 "under `owed-only` with a cause other than `owed`, the hand-out follows the audit's start". pr5:71 fires with `--cause placement`. |
| 5 | Provenance: rev-1 drafted from dl20, read at base `c63aabbb` (pr5:267) | cite | AGREES | This is history and makes no claim about today's text. dl20's S1, S2 and S7 are unchanged by rev-3 (`git show 63669d505` touches only dl20 S9 and the row at :128). |
| 5 | dl20's closed cause set already holds `placement`, so pr5 is only a caller (pr5:280) | cite | AGREES | dl20:52, :139-140 ("refuse a cause outside the set"). |
| 5 | `check_review_ended` is the name dl20 gives the predicate at `unattended.sh:12762` when it extracts it (pr5:286-288) | cite | AGREES | dl20:53-54. dl20:147 "`check_review_ended` is the grep pipeline at `tools/unattended/unattended.sh:12762`". |
| 5 | A placed spec audit runs on `<slug>-specs` until its verdict is terminal. pr5 states no exit word (pr5:74, :82) | SA | AGREES | dl32:52-55: a spec subject ends "at its target or its bound". BOUNDED, CONVERGED and CEILING are still terminal. pr5 names no NON-CONVERGENT exit, no budget route, no fixed `review_state` shape and no chain stop. |
| 7 | `probe.trigger` copies `review.trigger`'s flag shape (pr7:70-71, :174, :402, "TOOL-dDeclaredLoop-20 S2") | cite | AGREES | dl20:51-52 `--trigger <slug> --subject <s> --cause <c>`. S2 is untouched by rev-3. |
| 7 | `review.trigger`'s cause set is a literal held in the driver, and the review harness also reads it. Moving it onto the table would re-point both readers (pr7:162-164, F3 at :376-380) | cite | AGREES | dl20:52 (the literal set in the driver verb). dl20:59-61 S3 (harness "taking `trigger` as an argument validated in the closed set S2 names"). |
| 7 | SA applied: pr7 states no spec-audit routing | SA | AGREES | No probe hit beyond record-table and rev-log lines (pr7:36, :176, :388). |
| 14 | SA applied: no spec-audit exit or disposal | SA | AGREES | Hits pr14:40, :246, :252 are rework-budget lines (see section 4). |
| 16 | SA applied: no spec-audit exit or disposal | SA | AGREES | Hits pr16:28, :84 are rework-budget lines (see section 4). |
| 34 | dDeclaredLoop's loop kit `tools/loop/` exists before this run with `kit.toml`, `selftest.py` and `loop_lib.load_tree_lib`, and dl20 is one of the units that builds it (pr34:269) | cite | AGREES | dl20:227-229 Files touched: `tools/loop/loop.toml`, `review_dispose.py`, `selftest.py`. dl20:330 adds an arm on `tools/loop/selftest.py`. dl92:50-58 owns `load_tree_lib`. None of this changed in rev-3. |
| 34 | SA applied: a spec audit's findings disposed by severity (pr34:29-33) | SA | AGREES | This disposal rests on BUILD-METHOD M4, not on dl20, dl32 or fh17, and it records a past exit (see section 4). |

2. MISMATCH

- **pr5 S7 against dl20 S7.**
  - pr5:81-82: "The build harness then holds the roster's hand-out until the audit's verdict is terminal". pr5:71 fires "`--trigger <slug> --subject <s> --cause placement`".
  - dl20:80: "`owed-only`, held only when the trigger cause is `owed`". dl20:202-203: "Under `none` and under `owed-only` with a cause other than `owed`, the hand-out follows the audit's start rather than its terminal verdict".
  - Under `review.blocks = owed-only`, a placed audit fired with cause `placement` is not held. That breaks pr5's goal (pr5:28-29). AC1 (pr5:198-203) only checks the preflight's owed line, so it stays green either way.
  - Change: pr5 should do one of two things. Either S7 says the hold holds under `every-review` and, under `owed-only`, only when the audit fires as `owed`. Or S6 fires the Design-exit audit with `--cause owed` once `AUTH_SPEC_AUDIT_FROM` holds `placement`, keeping `placement` for the at-once firing past the position. Either way, AC1 or AC6 gains a plant under `review.blocks = owed-only` that reds when the hand-out is not held.
  - Cause: pre-existing. dl20 S7 read the same at `2740f0a3d` (`git show 2740f0a3d:…dDeclaredLoop-20.md | sed -n 79,81p` printed the same S7), and `git diff --stat 2740f0a3d ab976b5b3 -- …dPlacedRequest-5.md` is empty.

3. UNKNOWN UNTIL BUILT

- None.

4. Probe hits no rule binds, and the seventh field

- pr3:383 "spends the rework budget on contention": this is about dl33's `counted` rule for a claim's `awaiting` self-route, not a spec audit. dl33 is not one of the revised units.
- pr14:40, :246, :252 "rework budget": this is dl30 S1's `flow.rework-budget` sizing for a pre-claim draw. No spec audit is involved, and dl30 is not revised.
- pr16:28, :84 "rework budget": this is a patch build's draw on its closed root's budget, which is dl30 S7's. No spec audit is involved.
- pr34:29-33 "exited CONVERGED with 70 confirmed findings, its eleven highs units 23 to 33. This unit is BUILD-METHOD M4's batch of the other 50 MEDIUM and 9 LOW": a severity disposal of a spec audit. It records a past exit and rests on M4, not on dl20, dl32 or fh17, so SA's "when it relies on one of the three revised units" does not bind it.
- pr3:33, pr5:21, pr7:36, pr14:18, pr16:18, pr34:23 and the rev-log lines that say "spec audit": these are record-table rows or history, with no rule content.
- `--lease status`'s seventh field: no dPlacedRequest spec pins the line at exactly six fields.
  - pr34:106-108 S22 names the line's six fields in prose ("prints one TAB line, `<tail> <fleet tag> <session> <status> <verdict> <epoch>`"). It states no count and no "exactly".
  - AC22 (pr34:468-470) only checks that the holder's session is printed. pr49:358-360 AC28 only checks exit 0 and that "the status line" prints.
  - `grep -n -i -E 'six (tab )?fields|six-field|NF ?==|field count|exactly (six|6)'` over all dPlacedRequest specs printed nothing.
  - So the appended field reds no criterion. S22's prose would need a rev to name a seventh field before the ask is built (tr2:345-369 states the six-field prefix is kept).

5. Revised parent sections cited but not depended on

- pr3: it cites dl20 S1 and the rows. It does not depend on rev-3's `item.review.dispose` row (dl20:128) or S9 (dl20:86-89).
- pr5: it cites dl20 S2, S7 and the `check_review_ended` extraction. It does not depend on dl20:128 or S9.
- pr7: it cites dl20 S2 and S3's closed set. It does not depend on dl20:128 or S9.
- pr34: it cites dl20's files in `tools/loop/`. It does not depend on dl20:128 or S9.

6. Parent text that looks wrong

- dl20:83-85 S8, the fold row at dl20:129 and AC1 at dl20:278 still give a NON-CONVERGENT route to `item.review.fold`, the fold of an unbuilt spec. dl32:43 passes no route-backs to a spec subject, and dl32:52-55 gives it `no-fall`, so a spec subject can no longer reach NON-CONVERGENT.
- dl20:127, the trigger row, and dl20:114-115, the dl32 edge, refuse a round "past … `flow.route-backs`" with no subject limit. dl32:43 now applies that bound "for the build slug and for no spec subject".
