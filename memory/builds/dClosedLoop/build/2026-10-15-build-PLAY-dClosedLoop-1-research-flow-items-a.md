# Research: the flow layer's items, Plan, Design and Build

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 20's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-1-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md`, under `[audit]`.

---

I've drafted a minimal declaration for each of the 31 Plan, Design and Build items. Measured against the flow layer's requirements, I found 22 problems, listed with their fixes in section 3. Four matter most:

- **The driver judges in two places.** At `plan.disposition` it decides where a request goes (F1). At `plan.review-gate` and `design.review-gate` it writes the recommendation's reasoning (F2).
- **Three Build witnesses are typed by the acting builder:** acceptance results, the bug-class trailer and the scope check timing (F5, F6, F16).
- **Three core items need knowledge-layer inputs that no core input replaces:** the reuse probes, the bug-class trailer and the builder's lexicon (F6 to F8).
- **The checklist text in `flow.md` no longer matches what was settled later**, in three items (F15).

All sources are under `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/`. File keys: **v2** = `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` · **flow** = `…-flow.md` · **fr** = `2026-10-15-…-flow-roles.md` · **roles** = `…-roles.md` · **li** = `2026-10-15-…-layer-instruction.md` · **sm** = `…-session-model.md` · **or** = `…-orientation.md` · **co** = `…-coordination.md` · **fd** = `…-foundations.md` · **gr** = `…-gap-register.md`.

Layer labels: [I] instruction, [F] flow, [R] roles, [M] memory, [Rt] runtime, [K] knowledge, [O] observability, [In] integrations. "Fn" in a flags cell points to section 3.

**Scope shared by every item, stated once rather than per row:**
- **Every item:** `mailbox.reads`, `actions.free`, `card.pointers` (v2 `[policies]`).
- **Every role item, added:** `prompts.author`, `prompts.batch`, `roles.retries`, `roles.no-spawn`, `notices.record`, `run.on-owner-question`, and the role's level-5 static instructions.
- **The driver:** `driver.reads`.
- **Practice reach:** the reach entries in the tables are candidates. Only `[yagni]`'s per-stage reach is declared anywhere (fd `[step-1]` R1); the catalogue is gap-found-02's.

## 1. Tables

### Plan (flow `[plan]` Draft checklist, 11 items)

| tag | actor | witness | inputs by layer | instruction scope | routes | fan-out, depends on | flags |
|---|---|---|---|---|---|---|---|
| `plan.intake` | command: the prompt-submit hook (fr `[forks]` settled H2; roles `[map]` Plan 1). sm `[plan]` row 1, "the session", is superseded. | Hook-written verbatim intake-log entry. Other sources: the ask, filing or proposal record at its SHA. Adopter feedback: **not stated**. | [Rt] hook; [M] intake log, asks, Maintain filings, Loop Review proposals; [In] adopter feedback (optional) | Policies: `plan.ratification` (this record is its witness under `request`). Reach: `[records]`, `[security]`. Template: intake-record schema (none under `memory/`). | `recorded` → `plan.dedupe`; failure: **none** | Once per intake item; first item | F10, F11 |
| `plan.dedupe` | command (roles `[map]` Plan 2) | Dupes record carrying its derived-index key (sm `[plan]` row 2; key-trusted per or `[trust]`) | [M] intake, plan view, design index, open asks | Policies: no key governs it at Plan. Reach: `[reuse]`, `[one-fact]`. | `none`, `duplicate-of`, `overlaps` → `plan.disposition`; stale key → re-derive (or `[trust]`, not in flow) | Once per intake; after `plan.intake` | F11, F13 |
| `plan.triage-rule` | command by rule; planner where no rule decides (roles `[map]` Plan 3). fr `[steps]` Plan "1 to 4: commands" leaves the planner out. | Triage record naming the rule (sm row 3). Planner branch: only its validated return. | [M] intake, dupes record; [I] declared triage rules (level 2) | Policies: `plan.triage`. Reach: `[risk]`. Template: rule table. | `rule:<id>` → `plan.disposition`; `no-rule` → planner; failure: **none** | Once per intake; after `plan.dedupe` | F4, F11, F15 |
| `plan.disposition` | **driver** (roles `[map]` Plan 4; fr `[steps]` Entry row 2), under `placement: agent-places` | Disposition and reason in the intake record, **typed by the driver**; only its facts are checked (`placement.check`, or `[placement]`) | [M] intake, the scout's placement evidence, plan view, design index, asks; [Rt] lease refs | Policies: `placement`, `placement.check`, `kickoff.runs`. Template: disposition enum. | `new` → `plan.record`; `amend` → Design re-entry (an `intake` message if another session holds the lease, FR-8); `patch` → patch build at Design (flow `[maintain]` entry points); `continue` → that build's `next`; `ask` → filed; `none` → relayed. `placement.check` refusal: **no route** | Once per intake. Decided at Entry, though the checklist orders it after triage. | **F1**, F11, F12, F13 |
| `plan.record` | planner (roles `[map]` Plan 5) | Plan record's fields check (sm row 5): a schema check over the persisted return (fr `[cycle]` step 6) | [M] intake, triage, dupes, the owner's answers; [K] research records (v2 `[layers]`) | Policies: `plan.authority`, `deps.coordination`. Reach: `[yagni]` at Plan, `[small]`. Template: plan-record schema (none yet; FL-P2). | `drafted` → `plan.reach`; `research-request` → researcher → planner; `owner-question` → owner, else best effort, recorded (FR-4), though fr Plan row 5–6 says "parks"; unresolved value → retries → item parks (roles RL-7) | Once per build, again per revision; needs disposition `new` | F9, F15 |
| `plan.reach` | planner, in the same dispatch as `plan.record` (fr "5, 6") | One reach field per active practice (sm row 6) | [I] `charter.practices`, the reach catalogue; [M] plan record | Policies: `charter.practices`. Reach: every active practice's Plan reach. | `answered` → `plan.view`; an answer that rejects the need (`[yagni]`): **no route** | Per active practice; after `plan.record` | F11 |
| `plan.view` | command (roles `[map]` Plan 7) | Placement predicate (v2 `[contracts]` Plan) | [M] plan record priority and `parents:`, plan view | Policies: `plan.unplaced`. Reach: `[derive]`. | `placed` → `plan.build-lease`; `unplaced` → handled by `plan.unplaced` | Once per build; after `plan.record` | — |
| `plan.build-lease` | command (roles `[map]` Plan 8) | Lease ref written by compare-and-swap; its history is the witness (co `[design]` unit 1) | [M] remote lease refs, plan record; write set: **none produced at Plan** | Policies: `leases`, `leases.granularity`, `leases.renewal`, `leases.expiry-hours`, `leases.overlap`, `leases.offline`. Reach: `[isolate]`. | `held`; `overlap` → card, transition record, the other build's mailbox (co unit 3); `refused` under `leases: refuse`: **no route**; `offline` → `leases.offline` | Once per build; after `plan.view` | F11, F19 |
| `plan.review-gate` | command scores, **driver reasons**; review roles when the review runs (roles `[map]` Plan 9) | Recommendation line (sm row 9): score mechanical, **reasoning driver-typed**; report path when the review runs | [M] pinned plan record, past findings; [O] value ledger (optional) | Policies: `review.plan`, `review.plan.effort`, `review.recommendation`, `review.recommendation.source`, `review.blocks`, `review.left-shift`. Lens: order, dependencies, duplicates, readiness (flow `[review]`). Template: REVIEW-PROTOCOL "The Tier-2 pattern". | `no-review` → `plan.ratify`; a run review blocks the transition; each finding → a planner revision (fr) | Once per build, plus rounds; after `plan.reach` and `plan.view` | **F2**, F4 |
| `plan.ratify` | owner (roles `[map]` Plan 10) | The intake record (flow `[walked]`; fr FR-1). v2 `[contracts]` still says "the ratification change". | [M] intake log; [Rt] hook (`hook-keyword`) or TTY CLI (`terminal-command`) | Policies: `plan.ratification`, `autonomy`, `plan.authority`, `policy.proof` | `ratified` → `plan.exit`; under a non-`request` value with no ratification yet: **no route** | Once per build; under `request` it needs only `plan.intake` | F11, F14, F15 |
| `plan.exit` | command | Transition record, written three ways (sm row 11) | [M] all witnesses, mailbox; [Rt] executor launch | Policies: `transitions.record`, `card.follows`, `card.store`, `card.snapshot`, `notify.owner`, `run.host`, `review.blocks`, `context.on-full`, `context.threshold` | `recorded` → card re-rendered, executor launched by `run.host`, Design input; `refused` (unwitnessed item, or an unanswered message, v2 `[open]`) → `next` names the first unwitnessed item (or `[position]`) | Once per build; after every item above | — |

### Design (flow `[design]` Draft checklist, 10 items)

| tag | actor | witness | inputs by layer | instruction scope | routes | fan-out, depends on | flags |
|---|---|---|---|---|---|---|---|
| `design.input` | command (roles `[map]` Design 1) | Input pinned by SHA (sm `[design]` 1) | [M] plan record, plan revision, `intake` mailbox message, a patch's derived plan record | Policies: `design.reentry`, `patch.ratify`, `deps.messaging` | `plan-record` → `design.reuse-probes`; `amendment` → unit- or feature-level re-entry (additive stays unit, FL-B4); `plan-revision` → re-design inventory (flow `[plan]` settled); `patch` → micro-spec. An amendment outside the goal: **no route** | Once per entry; after `plan.exit` or a re-entry trigger | F11, F15 |
| `design.reuse-probes` | reuse scout | Seams, each with its probe's digest, re-derived by the executor (sm `[design]` 2) | [M] goal, scope, open asks; **[K] map dossiers, recall, bug classes** (flow D2; fr Design row 2) | Reach: `[reuse]`, `[derive]`. Method view: BUILD-METHOD M5. | `seams` or `none-found` → `design.decompose`; digest mismatch → retries → park | Once per build, or per re-entry scope; after `design.input` | **F7** |
| `design.decompose` | architect | **Not stated** | [M] plan record, seams, design index, parents' `confirmed` interfaces; [K] research records | Policies: `design.forks`, `design.reentry`, `deps.early-build`, `build.worktree`. Reach: `[yagni]` at Design, `[small]`, `[contract]`, `[core]`. Method views: BUILD-METHOD M2, M3. Template: feature-design schema (none). | `decomposed` → `design.unit-spec`; `fact-fork` → researcher → architect; `goal-fork` → plan revision under the mandate (FR-12) | Once per build; per feature on feature re-entry; after `design.reuse-probes` | F9, F10 |
| `design.unit-spec` | spec writer, one per unit, in parallel up to the bound | Spec path and SHA; the executor checks the file and its format (sm `[design]` 4) | [M] unit row, feature design, interfaces, seams, design-index overlaps | Policies: `design.forks`. Reach: `[spec]`, `[verify]`, `[contract]`, `[gate]`, `[docs]`. Template: TEMPLATE-SPEC. | `authored` → reach and overlap items; `unit-fork` → resolved by `design.forks`; `feature-level` → architect | Per unit; after `design.decompose` | — |
| `design.reach` | spec writer, in the same dispatch (fr "4 to 7") | Reach fields inside the spec (sm `[design]` 5) | [I] `charter.practices`, reach catalogue; [M] spec | Policies: `charter.practices` | `answered`; a rejecting answer: **no route** | Per unit × practice; after `design.unit-spec` | F11 |
| `design.fork-resolve` | architect (feature), spec writer (unit), researcher (fact) (roles `[map]` Design 6) | Fork records: option, alternatives, reason (flow `[design]` settled). "No open fork" inside derived READY. The join is **not stated**. | [M] fork records, research records; [I] P18 decision principles | Policies: `design.forks`, `plan.authority` | `resolved` → `design.ready`; `goal-fork` → plan revision and re-design. The item text "the run has stopped" contradicts FR-12. | Per fork; after the item that raised it | F4, F10, F15 |
| `design.overlap-ack` | command finds; spec writer acknowledges | Design index (v2 `[contracts]`, warn); the acknowledgment sits in the spec's boundaries | [M] design index, specs | Policies: `design.overlap`, `deps.messaging` | `acknowledged` or `none`; under `refuse`: **no route** | Per overlap; after `design.unit-spec` | F4, F11 |
| `design.review-gate` | command and **driver**; review roles; spec writer folds (roles `[map]` Design 8) | Recommendation line; report path | [M] spec set at its revision; [O] value ledger (optional) | Policies: `review.design`, `review.design.effort`, `review.recommendation`, `review.recommendation.source`, `review.blocks`, `review.left-shift`. Method views: BUILD-METHOD M4, REVIEW-PROTOCOL. Lens: specs plus the cross-build index. | Each finding → a spec-writer revision, re-reviewed "while rounds still find" (fr Design row 8) | Once per build, plus rounds; after the reach, fork and overlap items | **F2**, F4, F18 |
| `design.ready` | command | Derived READY per unit (or `[position]`) | [M] specs, fork records | Policies: `design.handoff` | `ready` → `design.exit`; THIN, FORKED or MISSING: **no route** | Per unit; after all of the above | F11 |
| `design.exit` | command | Transition record | [M] witnesses, mailbox | Policies: as at `plan.exit`, plus `deps.early-build`, `deps.coordination`, `deps.messaging` | `recorded` → `confirmed` interfaces posted to dependents (co unit 8); `refused` → `next` | Once per build (whole build, FL-D1); after `design.ready` | — |

### Build (flow `[build]` Draft checklist, 10 items)

| tag | actor | witness | inputs by layer | instruction scope | routes | fan-out, depends on | flags |
|---|---|---|---|---|---|---|---|
| `build.base` | command | BASE pinned from history (or `[trust]`); the mandate is the intake record | [M] history, intake | Policies: `autonomy`, `plan.ratification`, `run.host` | `pinned` → `build.unit-lease`; no mandate: **no route** | Once per build; after `design.exit` | F11 |
| `build.unit-lease` | command | Unit lease ref (co units 1–2) | [M] remote lease refs, the roster's write sets | Policies: `leases.*`, `build.worktree` | `held`; `overlap` → warn; `refused`: **no route** | Per unit at its start; after `build.base` and its order predecessors | F11 |
| `build.unit-commit` | builder, one per unit, in order; disjoint units in parallel; commits queued by the executor (FR-5) | Commit with the unit id and trailers, resolved by the executor (sm `[build]` 3) | [M] spec at its SHA, write set, acceptance commands; **[K] bug classes** (li `[layers]`); **[K] lexicon** in the builder's ceiling | Policies: `build.worktree`, `build.scope`, `design.forks`, `design.reentry`, `resume.partial`. Reach: `[small]`, `[spec]`, `[bytes]`, `[cross-os]`, `[security]`, `[migrations]`, `[docs]`, `[yagni]` at Build. Method view: BUILD-METHOD M6. | `committed` → `build.acceptance`; `diverged:spec-wrong` → spec writer; `diverged:interface-change` → architect; `diverged:fork` → `design.forks` (fr Build rows 3–5) | Per unit, per pass; after `build.unit-lease` | F8 |
| `build.acceptance` | builder | The builder's "checks run" field (roles `[roster]` settled), **typed by the builder**; or `[position]` names no source for the acceptance record | [M] spec's acceptance commands, the commit | Reach: `[verify]`, `[gate]` | `pass` → next pass or unit; a failure the builder cannot fix: **no route** | Per unit; after `build.unit-commit` | **F5**, F11 |
| `build.bug-class-trailer` | builder | Commit trailer, **typed by the builder** | **[K] bug classes only** | Policies: `review.left-shift`. Reach: `[left-shift]`. | Trailer present → next; failure: **none** | Per pass; after `build.unit-commit` | **F6** |
| `build.divergence` | driver routes the enum (table, compliant); spec writer or architect | **Not stated** (fr Build row 6: "—") | [M] returns, specs | Policies: `design.reentry`, `design.forks`, `transitions.record` (backward transitions, H10) | By the enum table, back to READY, then the builder | Per divergence; after `build.unit-commit` | F4, F10 |
| `build.scope-check` | command | Scope report from history; v2 `[contracts]` says "at the push", but Build never pushes | [M] commits, write sets | Policies: `build.scope` | `in-scope`; `stray` → warn and file an ask (fr); `refuse`: **no route** | Per commit; after `build.unit-commit` | F11, F16 |
| `build.closing-review` | review roles (diff lens); command disposes by `review.findings`; spec writer specs new units; builder builds them | Report path under `reviews/`; finding-to-new-unit join **not stated** | [M] build range from its base; [O] value ledger (optional) | Policies: `review.build`, `review.build.effort`, `review.build.when`, `review.findings`, `review.follow-up`, `review.blocks`, `review.left-shift`. Reach: `[risk]`, `[bound]`. Method views: REVIEW-PROTOCOL, BUILD-METHOD M8. | `clean` → `build.core-clean`; findings → new units → `design.unit-spec` → `build.unit-commit`; a follow-up round after a HIGH (FR-9). The item text says "blockers folded". | Once per build, plus follow-ups; after `build.scope-check` | F4, F15, F17 |
| `build.core-clean` | command, which the executor runs at the Build-to-Test transition (FR-11, H11) | Executor-written core-check result | [I] principle registry; [Rt] core checks; [M] attribution, exception register | Policies: `core.bypass`, `core.exceptions`, `floor`, `hooks.bypass` | `clean` → `build.exit`; own red → exit refused (v2 `[chain]` dScopedBuild); the fix route: **not stated** | Once per build; after `build.closing-review` | F11 |
| `build.exit` | command | Transition record | [M] witnesses, mailbox | Policies: as at `plan.exit` | → Test; `refused` → `next` | Once per build; after all of the above | — |

## 2. Extension points per step

No record declares any flow extension point yet (F20). Two optional slots are named, in li `[layers]` and v2 `[chain]` dBoundRoles. The rest are derived from the items' expansion inputs, so they are UNVERIFIED as declared points.

- **Plan:**
  - intake sources: trackers and adopter feedback ([In]);
  - the planner's optional slot for decisions and the research library ([K]);
  - recommendation signals from the value ledger and cost telemetry ([O]);
  - at `plan.exit`: `notify.owner` channels beyond the turn, and `run.host: cloud-routine` ([In]).
- **Design:**
  - `design.reuse-probes` slots: map dossiers, recall, bug classes ([K]);
  - the lexicon at Design (li R-F) ([K]);
  - the research library ([K]);
  - audit cost to the value ledger ([O]);
  - live delivery of `confirmed` messages ([In]?, UNVERIFIED).
- **Build:**
  - the builder's work-order slot for bug classes, and its lexicon ([K]);
  - `build.bug-class-trailer` as a whole ([K]);
  - `review.left-shift`'s target, where a first occurrence becomes a bug class ([K]);
  - review cost and run logs ([O]).

## 3. Findings

**F1. The driver decides placement.** Breaks P25 (`driver.reads: state-reads-only`) and P2.
- Evidence: roles `[map]` Plan 4; fr `[steps]` Entry row 2; or `[design]` ("Placement is the one judgment left").
- Fix: the orientation scout's return carries the disposition, from the closed set, with its reason. The driver records it and runs `placement.check`, which keeps `agent-places`.

**F2. The driver writes the review recommendation's reasoning.** Breaks P25.
- Evidence: roles `[map]` Plan 9 and Design 8; flow `[review]` settled ("the agent records the score with its reasoning").
- Fix: a command maps the score to the recommendation by table. Any reasoning comes as a field of the step's producing role's return: the planner at Plan, the architect at Design.

**F3. No record says the driver's hand-off to the prompt writer is rendered.** Breaks P25 and P26. This affects every role item in all three steps.
- Evidence: fr `[cycle]` step 2; gap-roles-05.
- Fix: declare the hand-off as rendered from the item's declaration (v2 `[chain]` dDeclaredLoop, "items declared with actor, inputs…"). The driver passes the render and its hash.

**F4. Seven items have more than one actor.** Breaks P24 (one actor per item). The items are `plan.triage-rule`, `plan.review-gate`, `design.fork-resolve`, `design.overlap-ack`, `design.review-gate`, `build.divergence` and `build.closing-review` (roles `[map]`).
- Fix: split each into single-actor items:
  - `plan.triage-judge` (planner);
  - `*.review-score` (command) and `*.review-run` (review roles);
  - `design.fact-research` (researcher), with feature and unit fork resolution kept inside the raising role's return;
  - `design.overlap-find` (command), with the acknowledgment inside `design.unit-spec`;
  - `build.findings-dispose` (command).

**F5. Acceptance results are claimed by the builder.** Breaks P2 and P23.
- Evidence: roles `[roster]` settled (builder returns "checks run"); sm `[build]` 3 (the executor resolves only the commit).
- Fix: the executor re-runs the spec's acceptance commands on the commit and writes the acceptance record.

**F6. The bug-class trailer is builder-typed, and its only input is knowledge.** Breaks P2 and P28.
- Evidence: flow `[build]` item 5; v2 `[layers]` knowledge row; gr gap-build-04.
- Fix: declare the item as a knowledge extension point, recorded as not applicable when no pack is installed. The trailer becomes evidence only.

**F7. The reuse probes have no core input that replaces the knowledge inputs.** Breaks P28.
- Evidence: flow `[design]` item 2; fr Design row 2; li `[layers]` (which names the breach).
- Fix: declare a tree search over the plan's scope paths, plus the open asks, as the required inputs. Map, recall and bug classes become optional slots.

**F8. The builder's ceiling includes the lexicon.** Breaks P28.
- Evidence: roles `[roster]` gov-builder ceiling; v2 `[layers]` knowledge row.
- Fix: make it an optional slot.

**F9. Research records are classed as knowledge, but core items route to the researcher.** Breaks P28.
- Evidence: v2 `[layers]` knowledge row; fr Plan "on request"; roles `[map]` Design 6.
- Fix: class a build's own research records as memory (the trail). The cross-build research library stays in knowledge.

**F10. No record states the witness for several items.** Breaks P2 and P24.
- Evidence: `plan.intake` for adopter feedback, `design.decompose`, the `design.fork-resolve` join and `build.divergence` (sm `[design]`; fr Build row 6). flow states no per-item witness for any item: "each witnessed by a check".
- Fix: declare per item:
  - the roster and interface schema check;
  - raised forks joined to recorded resolutions;
  - each `diverged` return joined to a later READY SHA and a `committed` pass;
  - each finding joined to a new unit id.

**F11. Sixteen items have no failure route.** Breaks P24 (an item's return routes).
- Evidence: the "—" routes in fr `[steps]`, and the items marked F11 above.
- Fix: one default route in the loop definition: a refusal is recorded, and `next` names the first unwitnessed item (or `[position]`). Add an explicit route only where a policy value refuses: `leases`, `design.overlap`, `build.scope`, `placement.check`.

**F12. Two records give different disposition sets.** A record disagreement.
- Evidence: flow `[plan]` Draft scope has {attach, new, defer, refuse}; or `[placement]` has {continue, amend, new, patch, ask, none}.
- Fix: one closed set in the loop definition that maps defer and refuse-as-duplicate.

**F13. The checklist order does not match when disposition happens.**
- Evidence: placement is decided at Entry (fr `[steps]` Entry; sm `[plan]` row 4), but flow orders it after `plan.dedupe` and `plan.triage-rule`.
- Fix: `plan.disposition` takes the Entry placement as input and depends only on `plan.intake`. A mismatch with `plan.dedupe` routes back to placement.

**F14. Two policies conflict over who ratifies the plan record.**
- Evidence: under `plan.ratification: request`, ratification exists at intake, before the planner drafts anything. `plan.authority`'s default says the owner ratifies the planner's draft. The v2 header (2026-10-15, FR revision) reconciles only `autonomy`'s gate.
- Fix: one sentence in `plan.authority`'s definition saying how its owner clause is met under `request`.

**F15. Checklist and record text no longer matches what was settled.**
- Evidence:
  - flow Design item 6 and its Draft scope say "the run has stopped", against FR-12;
  - fr Plan row 5–6 says "parks while the owner is away", against FR-4;
  - flow Build item 8 says "blockers folded", against FL-B3 and P19;
  - v2 `[contracts]` gives Plan's witness as "the ratification change", against FR-1;
  - roles `[map]` Plan 3 and fr Plan "1 to 4" name different actors;
  - flow's three Design inputs against the four in the `[maintain]` entry points.
- Fix: reword these when the items are tagged.

**F16. Build's scope witness happens at the push, which Build does not do.**
- Evidence: v2 `[contracts]` Build ("at the push"); flow `[build]` Draft boundaries ("Does not … land or push").
- Fix: compute it from history at `build.exit`.

**F17. Build carries no recommendation item.** Breaks P7.
- Evidence: flow `[build]` checklist; v2 `[presets]` sets `review.build: opt-in` under velocity, so in that preset a transition would carry no recommendation.
- Fix: `build.closing-review` emits the recommendation when the review is not owed.

**F18. Design audit rounds have no stopping rule.**
- Evidence: fr Design row 8 ("while rounds still find"). `review.follow-up` covers Build only (FR-9). gr gap-design-08: 0 of 254 audits came back clean.
- Fix: extend `review.follow-up`'s reach to Design's audit.

**F19. The build lease needs a write set that Plan does not produce.**
- Evidence: co `[design]` units 1 and 3 (write set evaluated at acquisition); flow `[plan]` Draft boundaries ("Does not choose a mechanism or a seam").
- Fix: the build lease's write set is empty at Plan. It grows at `build.unit-lease`, which co unit 3 already re-evaluates.

**F20. The flow layer declares no extension points.**
- Evidence: v2 `[layers]` (the layer contract requires them); li names only two slots.
- Fix: the flow's layer contract lists the points in section 2.

**F21. Some item names would equal existing policy keys.** Risks R-B's lexicon join.
- Evidence: `plan.triage`, `plan.ratification`, `design.forks`, `design.overlap`, `build.scope` are all keys in v2 `[policies]`.
- Fix: item tags use distinct forms, as in the tables.

**F22. The practice reach catalogue is undeclared.** As a result, P27 would leave the load sets for `plan.reach` and `design.reach` with no reach units.
- Evidence: fd `[step-1]` R1 declares only `[yagni]`'s reach.
- Fix: none new. It is already owned as gap-found-02, by dOrderedCharter, which is dDeclaredLoop's parent.

**UNVERIFIED:**
- the design index and lease refs filed as [M], since v2 `[layers]` lists neither;
- that no intake, plan-record or feature-design template exists: I checked only `memory/` and `memory/guides/`;
- the meaning of `placement: declared-checked`.

I wrote no files and changed nothing in the repository.
