# Skeptic return: run A, batch 1

**Serves:** research PLAY-dClosedLoop-1

Dispatch 175's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-16-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- A4-F12: confirmed medium
  The defect is in architecture-v2 [chain] `cl-dClosedLoop-0002`, which reds "two specs carrying one clause whole and disagreeing". carries.py:17 reads "two specs carrying one clause whole, or pinning it to two hashes", and its code at :213-216 reds `len(whole) > 1` whatever the pins say. whole-audit [instruments] reads "a clause carried whole twice". The research-final-coverage p3 row calls its plant "disagreeing", but the arm that fires is `carried whole by 2 specs`. A product spec written to the clause's wording would let two agreeing whole carriers pass.
- A4-F10: confirmed medium
  At architecture-v2 [chain] `cl-dClosedLoop-0004`, `grep -i -c deviation` prints 0 for both layer-memory and memory-plan. design-map.txt has 79 `record-kind.` nodes and none is `deviation`; the only deviation node is `policy-namespace.deviation`. whole-audit [found] reports the same gap. `cl-dClosedLoop-0480` covers "every record kind on dTotalRecall's registry", so this kind has no row for it to cover.
- A4-F11: confirmed medium
  At architecture-v2 [chain] `cl-dClosedLoop-0004`, the clause reds "an approver below the risk". The risk-to-approver mapping is the `deviation.approval` row (v2:1164, Owner dDeclaredLoop), with values by-risk, owner-all and author-recorded, and `cl-dClosedLoop-0119` builds it later. cl-0004 names no stand-in. The design does name stand-ins elsewhere, for example cl-0229 ("standing in as the root … until dWellOiledMachine's intake … land"), so leaving one out here is a gap. deviations.py:82-86 hard-codes the by-risk ranks.
- A4-F1: confirmed high
  At architecture-v2 [chain] `cl-dClosedLoop-0016`, dGroundRules retires `.agent-cap.conf` and the 1-to-5 clamp "in the same unit", and the clause has no upgrade step. The step kind (cl-0018) and the step gate (cl-0027) arrive with dSafePassage, the next build. Working-tree `tools/hooks/agent-cap.js:68-72` makes `FANOUT_CAP=<n>` lower the cap to min(n, 5). The `runtime.agents-in-flight` default is 6 (v2:1089). Readers are re-pointed, but the adopter's value is never carried across, so a lowered cap silently rises (c3), against P38 "keeps working, or warns".
- A4-F7: refuted
  At architecture-v2 [chain] `cl-dClosedLoop-0028`, the clause does order the steps: the floor step is "the step kind's first step", so the schema-4 step comes after it. The claimed consequence does not follow:
  - cl-0019 skips each step "when its witness holds" and keeps it "re-runnable over its own partial state".
  - cl-0022 plants "each step killed after its first write and the re-run converging".
  - A schema-3 receipt already carries the vintage `gov_commit` (govkit.py:8020) for the receipt to advance.
  So a kill after the floor step re-runs as a witness skip, and nothing writes `steps` into a schema-3 receipt.
- A3-F6: confirmed medium
  The addresses are architecture-v2 [chain] `cl-dClosedLoop-0115` and `cl-dClosedLoop-0440`. The budget lives "in its transition record". layer-memory:436 says of the transition kind "every step's exit item writes it", and the originating build has no step exit after `deploy.close`. No clause or row names who writes a patch build's draw into the closed build's record, or how two concurrent draws are serialised.
- A4-F5: confirmed medium (the walker graded it high)
  At architecture-v2 [chain] `cl-dClosedLoop-0438`, flow-steps [adopt] (:611-615) holds rows for `adopt.census`, `test.seed`, `adopt.practices`, `adopt.decisions` and `adopt.reconstruct` only. Neither `adopt.declarations` nor `adopt.instructions` has a row in flow-steps or layer-expansions, although adopter-instructions:183 says the program "gains `adopt.instructions`". I grade it medium: cl-0438 itself carries the behaviour and a fixture, so S4's update still runs. The gap is a missing declaration that a spec writer trips over, not a failing scenario.
- A1-F3: confirmed high
  At architecture-v2 [enforcement] `P23`, my own parse of v2's [chain] finds 495 ids with only 0093 missing. `grep -rn cl-dClosedLoop-0093` over the copy's build/ matches only v2:1707. dDeclaredLoop's row goes from 0092 to 0094, [clause-ids] says "Retired: none", and no other clause carries P23's rule. Only cl-0164 recomputes a key, and only for interface messages. Critical under c5.
- A5-F10: confirmed high
  Same defect as A1-F3, observed the same way at architecture-v2 [enforcement] `P23`. Critical under c5.
- A2-F1: confirmed high
  Same defect as A1-F3, at architecture-v2 [enforcement] `P23` and [chain] dDeclaredLoop. Critical under c5.
- A3-F17: confirmed high
  Same defect as A1-F3, at architecture-v2 [enforcement] `P23`. Critical under c5.
- A2-F6: confirmed medium
  The addresses are architecture-v2 [chain] `cl-dClosedLoop-0134`, `cl-dClosedLoop-0138` and `cl-dClosedLoop-0162`. Only cl-0135, the `leases.expiry-hours` row (v2:1033) and cloud-and-scale:211-214 declare a clock, and all three apply it to lease expiry alone. cl-0138's `leases.offer-seconds`, cl-0162's `flow.wait-ceiling` and cl-0134's `leases.queued-claim-days` name no clock. S2 injects a skewed clock on node x.
- A2-F7: confirmed medium
  At architecture-v2 [chain] `cl-dClosedLoop-0293`, layer-runtime:837 lists "the clock offset" among the registry's runtime facts with no reference and no measurer. cloud-and-scale:211 joins the two expiry rules with "or", while the v2:1033 row joins them with "and", so which rule decides is undefined. The plant only applies a supplied offset, so it never tests how the offset is measured.
- A4-F6: confirmed medium (the walker graded it high)
  The addresses are architecture-v2 [chain] dShippedRelease and layer-expansions [design-distribution]:
  - layer-expansions:438 defines receipt schema 4 as "per-kit versions, the release tag, the source remote".
  - cl-0020 defines schema 4 as `steps`, and cl-0435 defines schema 5 without those fields.
  - No clause builds the release tag or the source remote, and govkit.py:8020 still writes `"gov_source": str(root)`.

  The "cuts a release" half is weaker: `kits.cut` exists as a dShippedRelease item row (layer-expansions:453), though no clause builds it. The S4 update walk itself does not fail. Only currency fails, and it blocks landings only under the strict preset. So I grade it medium.
- A2-F7 and A2-F6 aside, A2-F3: confirmed high
  At architecture-v2 [chain] `cl-dClosedLoop-0337`, the landing push carries "the build's release". cl-0134 makes a landed build's release terminal and refusing every acquisition. Yet flow-steps:369-376 runs `deploy.core` through `deploy.snapshot` after `deploy.land` and only then `deploy.unlease`, and cl-0133 requires every effect push to carry a lease beat. cl-0325's hand-over and cl-0332's pick ("never a terminal tombstone") cannot recover a build that dies between land and close, so it never reaches `deploy.close` (c2).
- A1-F9: refuted
  At architecture-v2 [enforcement] `P14`, the lens half is carried by the row's own clauses. flow-steps:47-51 says "Every work order loads its load set … the step's practice reach", and each step lists "reviewers at a breakpoint" among its roles (for example flow-steps:142). `review.lens` is an item (flow-steps:485). cl-0168 renders a work order per item, and cl-0051 hands "each practice's reach per step … as step-scoped units … in work orders". A lens therefore reads the active reach through its work order.
- A4-F13: confirmed medium
  At architecture-v2 [enforcement] `P3`, the row names only cl-0342 and cl-0344. Searching the clauses for remote-ci, backend and verdict slot finds only cl-0029, which is about the floor in CI, and cl-0279, the headless spike. layer-expansions:179 makes the verdict-backend registry a Flow core point in Test that dWitnessedBar builds, and no clause builds it. whole-audit [stage0] already lists this as a K5 lead.
- A4-F9: confirmed medium
  At architecture-v2 [policies] `install.retired-edits` (v2:1277), the allowed values are "order, keep, delete", and `install.on-shim-call` (v2:1276) allows "warn, journal, refuse". cl-0026 plants only the `order` grading, so `keep` and `delete` are never seen red, while cl-0023 does see each shim value. `delete` lets an owner override drop an adopter-edited file, against P8's "never overwrites or silently drops". `refuse` lets a shim fail inside its window, against P38's "keeps working, or warns". No preset selects either value (v2:1588-1589).
- A2-F11: confirmed medium
  At architecture-v2 [policies] `roles.model.<role>`, v2:1063 takes one model, and its default is "the role's declared model", which is a single field (layer-roles:476). v2:1064 lets a role run on "one or more" harnesses, and cl-0332 drops work whose model the node lacks. S2's cross-harness take therefore fails even with the key unset, which makes the defect stronger than the finding says.
- deploy.close S7: holds
  Builds that close before dShippedRelease close with today's tools standing in, as S7 declares.
- deploy.distill S7: holds
  It is a dShippedRelease item; earlier chain builds close with today's tools, and the item adds no requirement on them.
- entry.claim S2: holds
  The compare-and-swap creation of `refs/gov/claims/<slug>` decides two nodes racing, and its own row defines the own-key retry.
- design.input S6: holds
  Each S6 re-entry reaches one of its declared kinds. For example, `build.core`'s own red becomes a fix unit, routed to `design.unit-spec`.
- plan.triage-rule S7: holds
  Chain builds arrive already placed, so the triage rule is not decisive on the bootstrap path.
- plan.recommend S5: holds
  The superseding build Z passes through it with `plan.lease` as declared, and the withdrawal's injections act elsewhere.
- build.recommend S2: defect
  ### AS1-F1 — `build.recommend`'s need and `build.reuse-check`'s route are prose that the position engine cannot join
  - **Address:** flow-steps [build] `build.recommend`
  - **Class:** K1, K2
  - **Severity:** medium
  - **Scenario:** S2
  - **Evidence:**
    - flow-steps:239 has Needs "every unit built and reuse-checked", which names no item.
    - flow-steps:238 routes `build.reuse-check` "clean → the unit built", a target in no declared form.
    - cl-0092 derives the next item from witnesses, over cl-0094's declared needs.
    - whole-audit [stage0] lists "the Build step's five from `build.recommend` on" among items reached from no entry.
  - **Consequence:** In S2, X's units finish on two nodes. No declared need joins their reuse-check witnesses, so the engine cannot derive when `build.recommend` is ready, and X stalls before its closing items.
  - **Fix:** Declare the need as `build.reuse-check`, every instance of it clean. Route `build.reuse-check`'s clean outcome to `build.recommend`, seen red on a planted unit whose reuse-check is still open.
- deploy.land S7: holds
  Working-tree `tools/push-main.sh:188` and `:948-1008` match the row. `--land` reads `GOV_PUSH_MAIN_MAX_RETRIES`, and with 1, a race re-prepares and exits without a second push. The hook's allow and bar records it cites exist today.
- **Read outside the list above:** `memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-16-skeptic.md`, my own handoff record, which I read to confirm the task block. Probes wrote only `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-a1/clauses.py` and `clauses.tsv`.
