# Fold re-audit — did the M4 fold disagree with itself

Scoped to the fold commit, three lenses (the fold disagreeing with itself · did each edit actually
close its finding · are the fold's new source claims true), batched skeptics, one synthesis. Thirty
candidates, three refuted, twenty-seven surviving, eight blockers.

This pass exists because this repo has a measured history: a large fold's defects are almost never the
findings it missed, they are disagreements between two paragraphs the fold wrote in the same pass. It
found exactly that shape. The first fold rewrote scope items and acceptance criteria wherever a
finding pointed, and left the design paragraphs those criteria are derived from untouched — so four
blockers reopened one level down.

The most consequential finding is about CODE, not prose, and it was verified independently before
folding: driving the resolver over both shipped carve-out descriptors with and without their
project-owned rule yields an IDENTICAL writes map. Destination last-wins already elects the seed
template, so the carve-out changes no byte on this tree and the criterion written to grade it had no
red state. Every edit below is folded.

## Verdict: BLOCKED

The fold is sound in kind but not in coverage: it rewrote scope items and acceptance criteria wherever a finding pointed at them and left the §4 design paragraphs those criteria are supposed to be derived from untouched, so four blockers reopened one level down — in the exact shape this repo's history predicts, a fold edit disagreeing with a paragraph the same fold left in place. Sixteen findings survive across units 1, 2, 3, 4, 5 and 7; every blocker is a design-versus-criteria contradiction inside one document, and each is a two-to-five-line repair with no re-resolution and no new measurement required (source claims were re-verified against `tools/govkit/govkit.py`, the descriptors and `tools/gate-legs.json` — three of them are false and are listed below). A builder cannot start on unit 1: unit 1 carries two of the blockers, one of which (R4) makes the unit's headline mechanism unobservable on today's tree and leaves its liveness fixture with no red state, which is a resolution question, not a wording one. Fold the sixteen edits — R4 is the only one needing a decision, the rest are mechanical — and unit 1 is startable.

| id | severity | unit | where | defect | edit |
|----|----------|------|-------|--------|------|
| R1 | blocker | 4 | §4 "The baseline…" (untouched) vs S3, AC3, S1 (rewritten) | Three regimes for the run-everything escape in one document: S3 is NO-ESCAPE with intersection scoring, §4 still says both reads run WITH the escape, and S1 justifies `run_all_env` by "the baseline needs one" while S3 says `check --observe` needs it | Rewrite §4 to the no-escape regime + intersection compare, carry S3's rejection reason, drop the doubled-wall-clock sentence; restate S1's refusal reason as `check --observe`; re-price §5's "full bar runs twice per apply" |
| R2 | blocker | 4 | §4 "Observation…" (untouched) vs S12, AC20, AC11 (rewritten) | §4 still mandates whole-line anchoring — the rule S12 measures as matching NOTHING and both liveness halves as unreachable | Restate §4 as line-anchored PREFIX, keeping the anchor argument (a target's longer line, the indented per-leg body) which survives under prefix matching |
| R3 | blocker | 1 (+2, 5) | §4 receipt role table (untouched), unit 5 S1 (untouched) vs S1, S2, F1, AC1b (rewritten) | Re-resolved F1 makes `project-owned` win zero destinations and asserts its absence from the whole receipt, but the frozen table still reserves a row "filled by this unit" justified by write-if-absent ("after the first"), and units 2 and 5 dispatch on it | Delete the row or mark it reserved-with-no-instance; strike `project-owned` from unit 5 S1's dispatch; state what AC5's "names the destination" means for a carve-out rule, which has none |
| R4 | blocker | 1 | §4 "Precedence" worked example vs S1, AC2b (rewritten) | Measured: driving `resolve_entry` over the two carve-out descriptors with and without the `project-owned` rule yields an identical `writes` map — destination-keyed last-wins already elects the seed template, so the carve-out changes no byte and AC2b's fixture has no red state; §4 claims a byte-level effect S1 already concedes is unobservable | Either state the carve-out is an absence claim only and re-key AC2b on a scratch descriptor whose carved source reaches an otherwise-unwritten destination, or drop the source-keyed operation and rest on destination last-wins; AC2's derived count must count carve-outs that CHANGE a write |
| R5 | high | 3 | S7 (rewritten) vs §4 "The repairs S7 carries" (untouched) | S7 defers the seven leg-name repairs "in the direction §4 states"; §4's five bullets name no leg-name repair and no direction, nor the unclaimed file or the `claims` row S7 added | Add three bullets to §4 with the direction stated once — rename gov's manifest legs to the descriptors' portable names — and enumerate the seven pairs, since three are near-misses |
| R6 | high | 3 | S5, AC7 (rewritten) vs §4 "The deployability leg" (untouched) | §4 still says one exclusion; S5 says three. `lands_nothing` and the merged trio are absent from §4, and §4 spells the no-landable-rule case as the engine's printed per-role reason while S5/AC7 require a declared key whose absence is AC7's liveness half — two spellings inside the unit whose subject is that class | Rewrite §4 to S5's three exclusions, pick the declared `lands_nothing` spelling, add the key to §4's Descriptors files-touched row |
| R7 | high | 3 | S4 vs S3 (both fold edits) and the kickoff-manifest descriptor | S4 says kickoff-manifest "claims no `home`" — it declares `home = "skills/session-kickoff"` — and says "the other four flat entries" when seven descriptors are `kind = "flat"` (five declare `home = "tools"`, which is S3's figure) | Say "declares a `home` that `entry_members` does not claim as a surface path"; delete the count; note `playbook` as a third shape (flat, no `home` key) |
| R8 | high | 3 | S2 (fold edit) vs the readers of `version_from` | The list form is normalized for `foreign_kit_present` and the new arms only; `entry_version` (receipt path, quantified by unit 1 AC11) and selfcheck arms 5 and 5b still read it as a dict and raise on a list — the crash moves from pre-write to mid-write | Name all four call sites in S2 and §4's files-touched row, all routed through the one helper; otherwise AC4's "`apply` runs to completion" is unreachable inside §3's no-repairs-beyond-S7 bound |
| R9 | high | 2 | S2 (untouched) vs §4 verdict table (rewritten) | The fold added the `converged` row for the doubly-deleted cell, making eight verdicts; S2 still says "Seven verdicts", and S6's new grid arm quantifies over the same grid | Delete the number: "The verdicts are §4's table", matching what unit 1 S7 and unit 5 S10 did in this same fold |
| R10 | high | 7 | §10 Reuse audit (rewritten) vs S3, §4, AC3 (rewritten) | §10 adopts a `corpus_ids.py`-style execution trace and keeps manual registration "alongside" it; S3, §4 and AC3 define the join solely as enumerated anchors versus arm-REGISTERED anchors. Two mechanisms for the unit's central predicate | Pick one in S3: add the trace half explicitly with its own liveness AC, or narrow §10 to "the doctrine is reused; the trace hook is not, because …" |
| R11 | high | 7 | §4 "Discovering the population" (untouched) vs AC4, AC4b (rewritten) | §4 still says the FILE-count pin catches the refactor this build makes likely; AC4 says that in that scenario both pins pass and neither grades it | Rewrite §4: the file-count pin catches a narrowed discovery rule, the enumerated anchor SET catches a branch moved into a new module, neither pin catches the latter |
| R12 | medium | 4 | §4 "The emitter" (untouched) vs AC13 (rewritten); rev-3 log | §4 asserts every non-empty guard is already token-spelled — false: the push-main descriptor declares `guard = ["{prefix}/push-main.sh", ".githooks/"]`. AC13 says the opposite and rev-3 claims the measurement was corrected | Correct §4 to name the one verbatim repo-root pathspec and say the emitter passes that class through unchanged |
| R13 | medium | 2 | S6, §4 `converged` row (fold edits) vs §6 (untouched) | The fold's only two additions to this unit are the only ones with no acceptance criterion: AC9 still grades the role-enum arm alone; nothing grades the grid arm or the new verdict | Add AC9b (deleting one grid CELL reds selfcheck) and an AC for `converged` over a fixture deleted in the target and at the new gov commit, asserting nothing is written and no restore is attempted |
| R14 | medium | 1 (+4, 6) | S7 + §4 step-id table (added by fold) vs unit 4 S8/§1 and unit 6 §1 (untouched) | The new eleven-step tuple brackets the contract sequence with BASELINE at 1 and RECEIPT at 11, making unit 4's "last step of the hard order" and unit 6's "first step of the hard order" both false | Reword unit 4 S8 to "the last CONTENT step, step `LEGS`", unit 6 §1 to "step `ATTRIBUTES`" — or rename the tuple to the apply-phase order |
| R15 | medium | 1 | S6 (untouched) vs unit 4 S9 and unit 5 S7 (fold edits) | S6 claims sole ownership of the check-state vocabulary and a spelled count of five, while unit 4 adds a recoverable-partial-install state "to unit 1's vocabulary" and unit 5 re-keys `undischargeable` on the RULE — S6 still says machine-scoped entries, of which there are none | Delete the count from S6, re-word `undischargeable` as rule-scoped, list the new unit 4 state, add both to the §3 SUPERSEDES paragraph the fold already rewrote |
| R16 | medium | 3 | AC1b (fold edit) vs the gate manifest | "Gov's manifest names two legs with a count in the name" is false by AC1b's own predicate — three carry a digit-bearing parenthetical, and two more carry digits without one. Two of the three are unit 3's own S7 renames, not unit 6's | Delete the figure, name the legs and their owning units, state whether the predicate is digit-bearing-parenthetical or any digit, and add a scratch-descriptor liveness half since no descriptor leg name carries a digit today |

## Fixes to fold

**Unit 1**
1. §4 receipt role table — delete the `project-owned` row, or restate it as reserved-with-no-instance whose only observable is the carve-out census, with AC1b's whole-receipt absence as its assertion. Strike the "after the first" clause either way.
2. §4 "Precedence" worked example — resolve R4: either state that on today's tree the carve-out changes no write and re-key AC2b's red state on a scratch descriptor whose carved source reaches a destination no landable rule reaches, or delete the source-keyed operation and rest A1 on destination-keyed last-wins. Then make AC2's derived count count carve-outs that change a write, reddening at zero.
3. §4 — state whether a carved source produces a receipt row at all; if it does, key it on the SOURCE and reconcile with AC1's `role = "seed"` and AC12's sidecar count.
4. S6 — delete the spelled state count; re-word `undischargeable` as reserved for unit 5's machine-scoped RULES; add `recoverable-partial-install` as reserved for unit 4; add both to the §3 SUPERSEDES paragraph.
5. §4 step-id table — keep as is, but see the unit 4 and unit 6 rewordings below, or rename the tuple to the apply-phase order.

**Unit 2**
6. S2 — replace "Seven verdicts, §4's table." with "The verdicts are §4's table."
7. §4 role table — one sentence recording that `project-owned` has no instance after unit 1's re-resolution, so no loop is written over it.
8. §6 — add AC9b: removing one CELL from the verdict grid reds `selfcheck`. Add an AC for `converged`: a fixture whose recorded file is deleted both in the target and at the new gov commit, asserting `update --write` touches nothing and never attempts a restore.

**Unit 3**
9. §4 "The repairs S7 carries" — add three bullets: rename gov's manifest legs to the descriptors' portable names (with the seven pairs enumerated and the direction stated once); the file rule or exemption for the one file under a non-flat home; the `claims = ["skills/session-kickoff"]` row.
10. §4 "The deployability leg" — three exclusions in S5's words, including `lands_nothing` and the merged trio with its expire-in-unit-6 note; spell the no-landable-rule case as the declared `lands_nothing` key only. Add `lands_nothing` to §4's Descriptors files-touched row.
11. S4 — "declares a `home` that `entry_members` does not claim as a surface path"; delete "the other four"; note `playbook` as flat-with-no-`home`.
12. S2 and §4's files-touched row — name `entry_version`, selfcheck arm 5, arm 5b and `foreign_kit_present` as the four readers routed through the one normalization helper.
13. AC1b — delete the two-legs figure; name the legs and which unit repairs each; state the predicate's boundary; add a scratch-descriptor liveness half.

**Unit 4**
14. §4 "The baseline…" — both reads run WITHOUT the escape, state machine compares the INTERSECTION of legs scored in both maps, carry S3's reason for rejecting the escape regime, delete the doubled-wall-clock sentence.
15. §5 — restate "the target's full bar runs twice per apply" as the guard-respecting read.
16. S1 — parenthetical becomes "`check --observe` needs one", not "the baseline needs one".
17. §4 "Observation…" — line-anchored PREFIX, keeping the anchor rationale; note that prefix matching re-opens the case where one leg name is a prefix of another.
18. §4 "The emitter" — every non-empty guard is token-spelled EXCEPT the verbatim repo-root pathspecs (measured: one, `.githooks/` on the push-main self-test leg), which the emitter passes through unchanged; say which class the drop test applies to.
19. S8 and §1 — "the last CONTENT step, step `LEGS` in unit 1's table" instead of "the last step of the hard order".

**Unit 5**
20. S1 — strike `project-owned` from the role-scoped integrity dispatch, leaving `generated`.

**Unit 6**
21. §1 — "step `ATTRIBUTES`, the first step of the contract's LAND sequence" instead of "the first step of the hard order".

**Unit 7**
22. S3 — resolve R10: add the trace half explicitly (a line recorder mapped back to anchors through the same AST walk, registration supplying only which arm asserts what, plus an AC for the trace's own liveness), or narrow §10 to doctrine-reuse with the reason the trace hook is not reused.
23. §4 "Discovering the population" — the file-count pin catches a narrowed discovery rule, the enumerated anchor set catches a branch moved into a new module, neither pin catches the latter.