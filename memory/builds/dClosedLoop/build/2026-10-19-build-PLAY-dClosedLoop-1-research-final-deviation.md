# Research: Spec deviation and its log: precedents, controls, hand-offs and the as-built view

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 157's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-30-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md`.

---

**Q3: spec deviation and its log (PLAY-dClosedLoop-1, researcher 30)**

**Short answer.** Today a deviation gets written down in many places (§9 revision lines, AMENDED ledger lines, `Decided:` trailers, `Revised:` paragraphs), but no gate catches a deviation that nobody wrote down. Almost none of what is written reaches anything a reader of the finished product reads. The recommendation is two parts:
- **C2:** a typed deviation record. Its population is computed from git history and joined at the commit and at the close.
- **C3:** a frozen design baseline, with an as-built view generated from it plus the deviation records. Help and the atlas render from that view.

C1, C5 and C6 stay on as carriers or detectors. C4 (amend the design record in place) is rejected.

## 1. Precedents

| # | Case | What departed, and how it was recorded | Does it reach a product reader? |
|---|---|---|---|
| 1 | dSweptBranches closing review | Round 1's blockers were "folded into unit 3 rev-3", a unit already built (`memory/builds/dSweptBranches/README.md:49-50`). The owner raised it as `gap-flow-05` (gap-register:108). | No. Spec rev line and README only. |
| 2 | dTieredTribunal run 2 | 4 of 9 audit defects came from amendments that left "the other half standing" (`memory/gotchas/amendment-leaves-its-other-half-standing.md`). | No. |
| 3 | dFramedEntrypoint round 2 | 25 of 62 findings were created by the fold and 17 were the fold misreading its finding (`memory/gotchas/fold-text-is-unreviewed-surface.md`). | No. Review record only. |
| 4 | aWindowedPass | A fold added `when` to a row shape. Code and revision log moved; the spec body and the kit README did not (`memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md`). Said so, but where nobody reads it. | No. The README a row author reads stayed stale. |
| 5 | TOOL-aDeferredBar-3 | The ledger said `exited 0`; the spec went to rev-5 in the same commit and the leg was red at the tip (`memory/gotchas/observation-before-the-last-fold-of-the-same-commit.md`). | No. |
| 6 | TOOL-dUnstalledConvoy-23 rev-1 | Spec written from review records named code its base had deleted: 4 of 7 scope items and 3 of 11 criteria had no subject (`memory/gotchas/spec-names-code-its-base-lacks.md`). A design-to-spec departure from reality. | No. |
| 7 | Owner ruling PM-12 | Carried into v2 (`architecture-v2.md:439-446`) and layer-memory (`:417`). Not carried into `ownership.md:499`, which still says dScopedBuild, and its `[amended]` log (from `:972`) has 0 hits for `acceptance`. Measured: 11 of 39 shared kind owners disagree between the two tables. | No. Rulings live in prose. |
| 8 | Answers fold, 2026-10-18 | v2 `[planned]` said gaps "would join" the register, which already held them (`memory/gotchas/two-answers-to-one-question.md`). The shape audit found 12 such cases. | No. |
| 9 | The 10-streak | A builder returned `DIVERGENCE:` for a hook refusal, not a spec defect (`research-stall-refusals.md:166`). The channel mixes refusals with deviations. | No. |
| 10 | `Decided:` trailers | 1,925 free-text lines across `git log --all`, e.g. "no review round after unit 7 — the owner's ruling". Not classified (`BUILD-METHOD.md:299,318`). | Only the M9 wrap-up turn, which is transient. |

**How deviations are recorded today, measured (all read-only):**
- **Revision logs:** 4,363 `- rev-N ·` lines across 1,322 specs; 1,083 specs reach rev-2 or higher.
- **Cause and approver:** of 3,048 rev-2+ entries, 691 name no cause class and 324 name an approval word. This is a word heuristic, so treat it as approximate.
- **Revised after building started:** 176 revisions in 105 specs are dated after the unit's first product commit. In a 40-spec sample, only 9 have a recoverable INPROGRESS anchor, and 7 of those 9 gained revision lines after it.
- **Acceptance ledger:** 280 AMENDED lines against 5,776 OBSERVED.
- **Spec audits:** 669 units were ever spec-audited, and only 1 audit record pins `@rev-N`. A spec revised after its audit is invisible; `gen_build_index.py:1459-1461` says so itself.
- **Divergence intake:** 0 revision records from the `diverged: true` path (`.claude/skills/build/SKILL.md:68`).
- **Design records:** 347 `Revised` paragraphs across 34 dClosedLoop records, 7 of them in v2.
- **What reaches a reader:** `help/` has 0 references. Kit READMEs carry 1 `rev-N` mention and 5 `**Migrating**` notes. There is no docs leg (`grep -c "help/" tools/gate-legs.json` → 0).

## 2. Existing controls

| Control | Hand-off | Catches | Misses |
|---|---|---|---|
| Write gate, route arm (`tools/hooks/scratch-guard.js:74-99, 868-912`) | spec→code | A product write with no routed, buildable spec | Whether the write matches the spec |
| Write gate, role arm (`scratch-guard.js:94-98`) | spec→code | A builder editing a spec beyond status and date | The untyped harness mode, where the builder self-amends (`tools/workflows/unattended-unit.js:270`) |
| `routed_commits.py` (`tools/memory-tree/routed_commits.py:1-30`) | spec→code | A product commit with no unit specced before it | Spec edits after code is written |
| `--check-commit` plus check-unattended check 23 (`memory/guides/UNATTENDED-VERBS.md:264-273`) | spec→code | Paths outside the declared write set | Meaning. A `--no-verify` commit is graded only at the close. |
| Memory-tree check 23, acceptance ledger (`memory/HYGIENE.md:596-628`) | code→record | Each criterion is OBSERVED or AMENDED rev-N | Shape and coverage only: not whether the amendment was justified or who approved it. Held under `--staged`. |
| Check 12 REV_SCOPE arm (`memory/TEMPLATE-SPEC.md:324-346`) | spec→spec | A rev-2+ entry names a §, S or AC token | Cause and approver. rev-1 is exempt (`check-memory-hygiene.sh:2099`). |
| `DIVERGENCE:` hand-back (`unattended-unit.js:265-271, 348`; `SKILL.md:68`) | spec→code | A typed builder can't self-amend | Never fired in tracked records; mixed with refusals |
| Spec audit and intent lens (`tools/workflows/tier2-review.js:727-729`) | spec→code (judged) | Code against the spec it is given | A deviation already folded into the spec reads as the intent. Not deterministic. Audit revision unpinned. |
| `--rescope` (`UNATTENDED-VERBS.md:209-217`) | roster | An amendment made with no record | "never a truthful-looking row attached to a different edit"; reaches the wrap-up only |
| `readme_mechanism_drift` (`tools/drift-audit/drift_report.py:1871`; README:133) | code→record | A README line older than a spec revision naming it | Report-only, live builds only |

**Planned in the design:**

| Mechanism | Catches | Misses |
|---|---|---|
| `build.scope` (dScopedBuild#9; flow-steps:237) | Paths outside the write set | Meaning |
| `build.acceptance` executor re-run (flow-steps:236; dDeclaredLoop#17) | Code that fails its spec | Spec and code changed together |
| Unit-pass routing ("spec wrong → spec writer; interface change → architect", flow-steps:235) and the `design.reentry` diff record (:182) | Classifies an amendment | Records no reason, approver or follow-through |
| `design.inventory` (:183) | A kept / amended / retired verdict per built unit after a plan revision | Revisions with no plan revision |
| P19 and dScopedBuild#2 | Built specs frozen; closes gap-flow-05 | Revisions before close |
| dBoundRoles#26 and dWellOiledMachine#49 | Separate refusals from divergence | — |
| dLinkedLibrary#1, #5, #23 | Decision kinds and a holds-now view | The decision kind has no writer named (layer-memory kinds table) |
| Composition check under `flow.adapt` (dDeclaredLoop#28) | Departures in the build's flow path | Spec content |
| dOrderedCharter#32-#35 | Overlay `amends` / `supersedes` pinned `<tag>@<hash>`; editorial/semantic classifier | — |
| dConvergedCharter#15 | `help/` rendered from `usage`, plus a docs leg | — |
| P35 | Every record names its cause | — |

No `deviation.*` policy key, no deviation record kind, and no writer for the design-record kind ("a core memory kind with no writer item") exist in v2 or layer-memory.

## 3. Hand-offs

| Hand-off | Deviation | Legitimate | Drift | Approver, by `[risk]` | Detector |
|---|---|---|---|---|---|
| Design → spec (chain clause → rev-1) | The spec narrows, widens, renames or drops its clause | A design defect with code evidence; an owner ruling; a reuse probe that changes the mechanism | A silent narrowing; a dropped "seen red on" clause; a renamed key | By risk class (below) | Declared `implements <clause-id>@hash` plus `Departs:` (deterministic), and the design-audit lens on meaning (judged) |
| Design revised under an existing spec | The baseline clause changes after a spec pins it | A Q1 fold; an owner ruling | An in-place `Revised:` edit | Owner for semantic changes | Clause-hash join, then a `design.inventory` verdict |
| Spec → revised spec | rev-N after the unit's first `Pass:` commit or its audited revision | A builder's discovery handed back; a review finding before close | A fold into a built unit (#1); the other half left standing (#2) | Spec writer, plus a re-audit of the changed sections, or the owner (below) | Computed from git history |
| Spec → code | Code meets a different criterion than the spec | None without a spec revision first (typed hand-back) | An AMENDED ledger line with no revision; building the intersection; behaviour in `Decided:` | No one at build time; it routes back to the spec writer | `build.acceptance`, `build.scope`, `DIVERGENCE` |
| Code → landed record | Ledger, README, help or as-built view disagrees with the code | None. After landing, a change is a new unit (P19). | #4, #5 | — | Check 23, the docs leg, render parity |

**Risk classes for approval:**
- **E, editorial:** the dOrderedCharter#33 classifier says mechanical. The author approves and the record is still written.
- **A, additive or stricter:** the spec writer approves, and the changed sections are re-audited at `@rev-N`.
- **L, loosening:** a dropped or weakened criterion, a WONTDO, or a narrowed scope. Feature re-entry, and the owner approves.
- **B, breaking:** an interface, a cross-build change, a principle, a policy key or a gap's owner. The owner approves.
- **Owner ruling as cause:** the owner is the approver and the record quotes the ruling.

**What the record carries:** id; hand-off; departed-from (`<clause-id>@<hash>` or `<unit>@rev-N §/S/AC`); before and after, or a diff reference; cause class (design-defect / owner-ruling / builder-discovery / review-finding / external); reason; evidence (path:line, commit or probe); risk class; approver and where the approval is recorded; follow-through (an overlay row, a new unit, a gap, an ask, a `usage` edit); and `caused-by` (P35).

## 4. Survey (all sources read 2026-10-19)

- **ADRs.** "If a decision is reversed, we will keep the old one around, but mark it as superseded" ([Nygard](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)). GDS requires the "superseded" status under the heading plus a link forward ([GDS Way](https://gds-way.digital.cabinet-office.gov.uk/standards/architecture-decisions.html)). Borrowed: the design stays frozen, and supersession is a forward link.
- **Engineering change proposals.** Class I is dispositioned by a configuration control board; Class II by the contracting officer ([AcqNotes](https://acqnotes.com/acqnote/careerfields/engineering-change-proposal-ecp)). Borrowed: the approver follows the change's class.
- **Deviations and waivers.** "A deviation does not change configuration documentation"; a request for deviation is "a specific written authorization to depart from a particular requirement" ([Wikipedia, Request for waiver](https://en.wikipedia.org/wiki/Request_for_waiver)). This is secondary: I could not read the MIL-HDBK-61A paragraph itself. Borrowed: the baseline stays fixed and the deviation sits beside it, which is C3.
- **ISO 9001 clauses 8.5.6 and 8.7.** Secondary summaries say the retained records must hold the nonconformity, the actions, any concession, and the authority ([isms.online](https://isms.online/iso-9001/clause-8-7-control-of-nonconforming-outputs)). I did not read the licensed text.
- **Spec-driven agent tools.** spec-kit's `/analyze` is "STRICTLY READ-ONLY", runs before implementation, and flags terminology drift and coverage gaps ([spec-kit analyze.md](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/analyze.md)). Kiro says "specs stay synced" when the agent is asked to update them ([Kiro](https://kiro.dev/blog/introducing-kiro/)). Neither logs a deviation's reason or approver, and nothing in either refuses one.
- **Contract tests.** Pact's `can-i-deploy` exits 1 on a failed verification ([Pact docs](https://docs.pact.io/pact_broker/can_i_deploy)). oasdiff's `--fail-on ERR` fails CI on definite breaking changes ([oasdiff](https://github.com/tufin/oasdiff/blob/v1.10.16/BREAKING-CHANGES.md)), and a Kestra blueprint adds owner approval on top ([Kestra](https://kestra.io/blueprints/openapi-breaking-change-gate)). That is, the diff gate still needs a log and an approver beside it.

## 5. Candidates

**C1 — Typed revision-log entries.** Mechanism: the rev-2+ line gains `cause`, `approver`, `evidence` and `follow` fields, enforced by extending the check 12 REV_SCOPE arm.
- Losing tests, run: (a) does a logged revision reach a product reader? 4,363 lines → 0 in `help/`, 1 in kit READMEs. **Loses.** (b) Is a design-to-spec departure caught at rev-1? rev-1 is exempt (`check-memory-hygiene.sh:2099`). **Loses.**
- Rejected as the whole answer by (a) and (b). Kept as today's carrier for spec→spec.
- Owner: dIndexedDesign (the spec kind). Before speccing: the line-tail convention. No key of its own.

**C2 — Deviation record kind, joined to a computed population (an ECO/request-for-deviation analogue).**
- Mechanism: one record per deviation. The population is computed, never declared: rev-2+ after the unit's first attributed `Pass:` commit or after its pinned audited revision; AMENDED ledger lines; `DIVERGENCE` intakes; `--rescope` rows; clause-hash moves. Each member must join a record whose approver meets its risk class.
- Gate: extend `routed_commits.py`'s commit attribution at the commit, and a check-23-style join at the close.
- Losing tests, run:
  - Anchor on INPROGRESS: 9 of 40 sampled specs recoverable. **That variant loses.**
  - Anchor on the first attributed product commit: 1,045 of 1,322 specs recoverable. The other 277 have no product commit, so there is no code to deviate from. **Passes.**
  - Anchor on the audit pin: 1 of 669 today. **Loses until pins are required.**
- Planted reds the build must show:
  - a rev-2 bump after a `Pass:` commit with no record → red;
  - an AMENDED ledger line with no record → red;
  - a mismatched `implements` hash → red;
  - an approver below the risk class → red;
  - a status-only edit → green.
- Owners: dIndexedDesign (the kind, extending the `diff` kind and `design.reentry`); dScopedBuild (the Build-exit join beside `build.scope`); dDeclaredLoop (the approval route, reusing dOrderedCharter#33).
- Before speccing: the record grammar and `@rev-N` audit pins.
- Keys:
  - `deviation.gate`: refuse | warn-and-ask | report. Default **refuse**.
  - `deviation.approval`: by-risk | owner-all | author-recorded. Default **by-risk**.

**C3 — Frozen design plus a derived as-built view.**
- Mechanism: v2 and the chain are pinned at a baseline. Each deviation carries an `amends` / `supersedes <clause-id>@<hash>` row, reusing dOrderedCharter#32/#35. A generator renders the as-built view with each overlaid clause citing its deviation. `help/` and the atlas render from the view.
- Losing tests, run:
  - Addressability: 484 of 484 clause texts are distinct. **Passes** with hash ids.
  - Positional ids: only 268 of 372 clauses kept their position after one day of folds (base `89e44048f`), and 192 texts were new or edited. **Positional ids lose.** Ids must be minted, and the baseline taken after the Q1 folds.
  - The build must show: a hand edit of the view → red; a deviation with no overlay → red; an overlaid clause with no citation → red.
- Owner: dLinkedLibrary (generated views, beside the holds-now view).
- Before speccing: the baseline tag, the minted clause table, and an instrument renderer.
- Key: `deviation.reflect`: derived-view | amend-in-place | log-only. Default **derived-view**.

**C4 — Amend the design record in place, in the same commit.**
- Losing tests, run: the other-half test on dClosedLoop's own records gives 11 of 39 owner disagreements, and PM-12's `acceptance` move is missing from `ownership.md` (#7). Contention: 104 commits touched v2 in 6 days, and 21 builds would share one 1,784-line file. The design-record kind has no writer item (no one door, against P30). **Rejected.**

**C5 — Executable conformance only (contract-test style).**
- Losing test: does a change made by moving the spec and the code together record its reason? The 176 post-build revisions pass every gate today; even oasdiff needs a separate approval step. **Loses as a standalone answer.** Kept as the spec→code detector (`build.acceptance`, dDeclaredLoop#17).

**C6 — Review lens only.**
- Losing test: is a planted silent deviation red deterministically? No. The intent lens takes the supplied spec as intent (`tier2-review.js:729`), and #3 shows folds create findings. **Rejected as a gate under `[gate]`.** Kept as the judge of design→spec meaning (dFairHearing#2 design-audit preset, with a "departure without a record" question).

No candidate further down the list differs in mechanism; variants such as a deviation as a decision subkind are details of C2.

## 6. Recommendation

Adopt **C2 + C3**. Keep C1 as the carrier until C2's kind lands, and C5 and C6 as detectors. The three new keys above add 3 to the 261, and new gaps go to the owners named.

**Must exist before speccing starts** (all doable today with no product code; `ROUTED_PATHS` doesn't cover `memory/`):
1. A design baseline commit taken after Q1's folds. From then on v2 takes no `Revised:` paragraphs; a design change becomes a deviation record.
2. Minted, stable clause ids with text hashes for the 484 clauses, generated by an instrument beside `2026-10-17-build-PLAY-dClosedLoop-1-map.py`.
3. A deviation register record per chain build, in the C2 field grammar. It would carry Serves kind `journal` provisionally, because check 21's kind set is closed; that is a stated stopgap.
4. Spec conventions:
   - a `Departs: <clause-id> · <entry>` bullet in §3 Non-goals;
   - a `· dev <entry>` tail on each rev-2+ line;
   - spec-audit Serves lines that pin `@rev-N`.
5. Builds dispatched only with `roles.builder`, so the builder hands back instead of self-amending.
6. An instrument `deviations.py`, beside the atlas and map generators, that computes the population and the as-built chain table, with plants as `map.py:558` does. It runs at each chain build's wrap-up. It is not a gate.

**Gate timing.** The gate needs product units: extend check 21's kinds, the check 23 join, and `routed_commits.py`. It should land before the first chain build's code, as a small bootstrap build. Waiting for dIndexedDesign or dScopedBuild leaves most of the 263-unit critical path ungated: their earliest finishes are units 187 and 221 (night-pass instruments `[final]`).

**Records that disagree:**
- **Two checks are numbered 23.** One is memory-tree's acceptance-ledger check (`check-memory-hygiene.sh:2985`); the other is check-unattended's undeclared-writes check. The handed facts file "check 23" under `tools/memory-tree`, while `flow-steps.md:237` means check-unattended's.
- **Who owns `build.acceptance` is inconsistent.** The handed facts, `flow-steps.md:236` and `ownership.md:188` say dScopedBuild. v2 dDeclaredLoop#17 and `ownership-verify.md:638` say dDeclaredLoop.

**For the other researchers, one line each:**
- Q2: its clause→unit coverage join needs the same minted clause table as item 2 above.
- Q4: help should render from the as-built view, not from v2.
- Q5: `atlas.py:426` reads v2's `Revised:` paragraphs and would need to point at the as-built view.
- Q1: the baseline must come after its folds.

I wrote nothing in the repository; the scratch folder `d157` has been deleted.
