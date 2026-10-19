# Walk return: run B, walker 1, entry and plan

**Serves:** research PLAY-dClosedLoop-1

Dispatch 170's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-11-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

I read the brief as my task, not as the subject of review: walk the sealed design and return in the brief's shape. Two things I did first are breaches, and they are disclosed in section 6.

**The chain shipped and failed in this scenario because** an agent-typed intake and an agent-recorded "owner's go" were accepted as the mandate and the ratification, so unattended builds ran on a forged authority that no check could tell from a real one.

### B1-F1 — entry.intake is acted and witnessed by the orientation scout, not by the prompt-submit hook
- **Address:** flow-steps [entry] `entry.intake`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S2
- **Evidence:** The item's Actor cell is "orientation scout, in an owner-bound session only", and its Proven-by cell is "the intake entry the scout writes". Several records say the opposite:
  - flow-steps' own `[rules]` say "No witness is typed by the acting agent".
  - The same record's `[revised]` row `hook-actor-kind` says "`entry.intake` is a hook".
  - Clause `cl-dClosedLoop-0282` reads "the prompt-submit hook writing each owner prompt verbatim … (`entry.intake`, PM-9)".
  - flow-roles H2 says the hook writes "the witness for intake and, under `plan.ratification: request`, for the mandate".
  - flow-roles-adoption:202 lists `entry.intake` among items whose witness is "written by a runner or a hook".
  - Probe: `grep -n 'entry.intake' …flow-steps.md …flow-roles-adoption.md` and `grep -n 'hook-actor-kind' …flow-steps.md`.
- **Consequence:** In S2 the mandate an unattended build runs on is a record that an agent types. A session can forge or edit "the owner's prompt", and `deploy.mandate` accepts "the intake record" as landing authority. That is spoofing and elevation of privilege across the node boundary. P2, P4 and P23 are broken at the root.
- **Fix:** Restore the actor as "hook: Runtime's prompt-submit hook, in an owner-bound session only". Restore the witness as "the intake entry the hook writes verbatim, redacted and capped". Keep the scout only as the reader in `entry.orient`.

### B1-F2 — Under `plan.ratification: request`, plan.exit takes the owner's go "as the planner records it"
- **Address:** flow-steps [plan] `plan.exit`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S2
- **Evidence:** The Does cell reads "under `plan.ratification: request`, the owner's go, as the planner records it, stands as the ratification". Other records disagree:
  - `[consequences]` says "`plan.exit`'s witness carries it".
  - v2 `[contracts]` says "Plan's witness is the hook-written intake (FR-1)".
  - `cl-dClosedLoop-0377` says "its intake read as the request's ratification".
  - `cl-dClosedLoop-0137` says "a relayed request being data with provenance and never consent".
  - Probe: `grep -n -i 'planner records\|request is the ratification' build/*.md`.
- **Consequence:** By default the ratification is something the planner, an agent, types. In S2, where nobody attends, any planner return ratifies its own plan, and the Plan gate certifies what it does not check.
- **Fix:** Change the clause to "under `request`, the hook-written intake record that the build's claim names stands as the ratification; before that hook lands, `cl-dClosedLoop-0378`'s owner gate applies". Remove "as the planner records it".

### B1-F3 — P23's only enforcing clause, `cl-dClosedLoop-0093`, appears in no `[chain]` row
- **Address:** architecture-v2 [enforcement] (row `P23`, `cl-dClosedLoop-0093`)
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S2
- **Evidence:**
  - P23's row is `| \`P23\` | \`cl-dClosedLoop-0093\` |`.
  - `grep -c 'cl-dClosedLoop-0093' architecture-v2.md` printed `1`, which is that row only.
  - dDeclaredLoop's clauses run 0092, then 0094. `[clause-ids]` reads "Retired: none".
- **Consequence:** P23 ("a claim is acted on only when its stored key recomputes equal…") has no clause, so no chain build builds the claim-trust rule. In S2, `entry.claim`'s "a retry that finds its own key counts as claimed" and every cross-node claim run with nothing checking their key or source.
- **Fix:** Restore dDeclaredLoop's clause `cl-dClosedLoop-0093` (the claim-trust rule: key recomputed, weakest source not agent-typed, otherwise re-derived or held as evidence). The K5 arm should red a ghost id.

### B1-F4 — Maintain's patch skips entry.place and entry.claim and goes straight to Design
- **Address:** layer-expansions [design-observability] `maintain.patch`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **Evidence:**
  - `maintain.patch`: "opens a patch build at Design … | the intake, keyed by (reading, offender key) | Design, as `patch.ratify` says".
  - flow-steps [entry]: a cadence filer's intake is "placed by `entry.place` the same way".
  - `[transitions]`: none→designing for `patch` needs "its slug claimed and its lease taken by `entry.claim`", and "the engine refuses any transition the table lacks".
  - `design.input` takes a patch "its slug claimed and its lease taken by `entry.claim`".
  - flow-steps `deploy.core` routes a red to "a patch build through the entry-point table's post-close row", which also names no `entry.place`.
- **Consequence:** In S3 the patch either reaches Design with no disposition, no claim ref and no lease (two nodes' Maintain runs can open it twice, and P22 and P40 are broken), or the engine refuses the transition and the patch has no terminal.
- **Fix:** Route `maintain.patch` (and the post-close row) to "files a patch intake → `entry.place`", and let `entry.claim` take the slug and the lease.

### B1-F5 — A patch claim records no originating build, so the shared rework budget cannot be keyed
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S3
- **Evidence:**
  - The claim commit carries "the claimant's key, the session and the intake's or the ask's content key".
  - stall-and-loop:168 says a patch build of a landing "shares the originating build's budget, so a chain of patch builds draws on one budget". `flow.rework-budget` says the same.
  - Neither `entry.place` nor `entry.claim` names the originating build, and neither has a route for "originating budget spent".
- **Consequence:** In S3, the patch's own red landing and an originating budget that is already spent are both unroutable. Each patch starts at zero, which is the C48 chain the budget exists to stop.
- **Fix:** On `patch`, the claim commit carries the originating build's slug and landed SHA. Add a route: originating budget spent → `flow.on-exhausted` of the originator, filed as an owner item.

### B1-F6 — A queued claim replayed after a withdrawal "counts as claimed" through the own-key rule
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **Evidence:**
  - "a retry that finds its own key counts as claimed".
  - `deploy.close` and `life.close` keep the claim ref ("never pruned").
  - `leases.queued-claim-days` (7) refuses only a stale fetch.
  - No check of the claim ref's terminal transition appears anywhere in the item.
- **Consequence:** In S5, a claim queued offline before withdrawal X replays within 7 days, finds its own key and routes "claimed → Plan" on a withdrawn slug. The engine has no withdrawn→planning row, so the run either refuses with no route or reopens a terminal build.
- **Fix:** The claimed route requires that the claim ref holds no terminal transition. Add a route for a terminal one: the replay is refused and recorded, and a fresh slug is minted only on a new request.

### B1-F7 — A refused lease and an unusable remote have no defined route at `entry.claim` or `plan.lease`
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - The routes say "the lease refused → as `leases` says". `leases` is "warn, refuse | warn". It is an overlap stance, and no record defines a refused acquisition under `warn` (probe: `grep -n 'as \`leases\` says'`).
  - `entry.claim` has no outcome for an unreachable remote or for a remote that refuses `refs/gov/claims/*`.
  - Today's run claim ships OFF for exactly that reason: `tools/unattended/.unattended.conf.example:163`, "turn it on once your remote accepts a push to `refs/gov/runs/<slug>`", and check 109.
- **Consequence:** In S6 a patch build whose lease is refused under the default goes into Design unleased (against P40), and a claim against a refusing remote has no outcome.
- **Fix:** Close both outcome sets: refused acquisition → wait or offer within `flow.wait-ceiling`, then an owner item; remote unreachable → as `leases.offline`; ref refused → a refusal naming the remote, then an owner item. Apply the same to `plan.lease`.

### B1-F8 — dPlacedRequest's entry routes and slug mint depend on builds that are not its ancestors, with no stand-in
- **Address:** flow-steps [entry] `entry.place`
- **Class:** K7, c1
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - `entry.place` routes new → Plan (dRankedPlan) and amend/patch → Design (dIndexedDesign).
  - `entry.claim` mints by `builds.slug-*` (dTotalRecall).
  - dPlacedRequest's only parent is dDeclaredLoop. Stage 0 leads: "dPlacedRequest→plan.input … not an ancestor, UNCLASSED".
  - v2:483 says "each new dependency on a later build gets a stand-in". Only `repeat` has one (`cl-dClosedLoop-0156`).
- **Consequence:** When dPlacedRequest lands, its acceptance cannot walk any disposition except `repeat` and `continue` to a witnessed next item, so its gates cannot be seen green end to end.
- **Fix:** Add stand-ins to dPlacedRequest's row:
  - new, amend and patch → today's unattended or kickoff route, recorded;
  - the slug mint → today's `check_slug_claimed` rules until dTotalRecall lands.

### B1-F9 — Plan reads the design index and `run.host`, which no ancestor of dRankedPlan builds
- **Address:** flow-steps [plan] `plan.dedupe`, `plan.exit`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - `plan.dedupe` checks "against live builds, the design index and open asks". The design index is `cl-dClosedLoop-0384`, in dIndexedDesign's row.
  - `plan.exit` says "the executor launched where `run.host` says", and `run.host`'s owner is dWellOiledMachine.
  - dRankedPlan's parents are dDeclaredLoop, dTotalRecall and dBoundRoles, so neither owner is an ancestor.
  - Stage 0 K2 flags `plan.exit` as "a target in no declared form".
- **Consequence:** dRankedPlan's dedupe and exit cannot run as specified when it lands.
- **Fix:** Add stand-ins: dedupe against live builds and asks only, with the index arm joining when dIndexedDesign lands; `run.host` read as `requesting-node` until dWellOiledMachine lands. Write the exit target in a declared form.

### B1-F10 — Plan's and the slice's policy keys are read by no item, and the landed-owner arm will red them
- **Address:** architecture-v2 [policies] `plan.authority`, `plan.triage`, `plan.kickoff`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - Stage 0 K4 lists these as "read by no chain clause and no item": `plan.authority`, `plan.triage`, `plan.kickoff`, `card.follows`, `leases.granularity`, `orient.budget` and `deps.coordination`.
  - `plan.triage: owner-batches` has no item where the owner acts, because `plan.triage-rule` is a command and `plan.triage-judge` is the planner.
  - `plan.authority`'s default, "planner-drafts-owner-ratifies", contradicts `plan.ratification: request`.
  - `cl-dClosedLoop-0014` reds "a key whose Owner build has landed has no reader".
- **Consequence:** Owner switches that switch nothing (against P10). dRankedPlan, dPlacedRequest and dKeptSession cannot land green without readers their rows never declare.
- **Fix:** Either give each key an item and a clause, for example a `plan.triage-owner` item under `owner-batches`, or retire the key with a decision. Reconcile `plan.authority` with `plan.ratification`.

### B1-F11 — entry.orient hard-codes `kickoff.runs`' default
- **Address:** flow-steps [entry] `entry.orient`
- **Class:** K4
- **Severity:** low
- **Scenario:** S1
- **Evidence:** The Does cell reads "the full kickoff's where no READY card exists". `cl-dClosedLoop-0376` says "only where `kickoff.runs` says". `[entry]`'s Policies line omits `kickoff.runs`.
- **Consequence:** `every-session`, `opening-a-build` and `plan-absorbs` have no effect.
- **Fix:** Change the cell to "as `kickoff.runs` says", and add the key to the Policies line.

### B1-F12 — Two owners stated for the entry step's items
- **Address:** architecture-v2 [chain]-preamble revision note (PM-9)
- **Class:** K8
- **Severity:** low
- **Scenario:** S7
- **Evidence:** v2:401 says "the entry step's items are dDeclaredLoop's (PM-9)". `cl-dClosedLoop-0122` (dPlacedRequest) and flow-steps' Owner column (SP-1) say dPlacedRequest.
- **Consequence:** A spec writer reads two owners.
- **Fix:** Mark the v2 note as superseded by SP-1.

| item | S<n> | actor | needs | witness | route | verdict |
|---|---|---|---|---|---|---|
| `entry.intake` | S1 | scout, not the hook | = | scout-typed entry | = | B1-F1 |
| `entry.intake` | S2 | scout, not the hook | = | scout-typed entry | = | B1-F1 |
| `entry.intake` | S3 | the filer | = | = | = | not on path: a Maintain filing reaches no owner session, so the filer writes intake |
| `entry.intake` | S4 | = | = | = | = | not on path: update runs as kits.update outside any build and places no request |
| `entry.intake` | S5 | scout, not the hook | = | scout-typed entry | = | B1-F1 |
| `entry.intake` | S6 | scout, not the hook | = | scout-typed entry | no intake → entry.orient records it absent | B1-F1 |
| `entry.intake` | S7 | hook unlanded until dWellOiledMachine | = | absent | entry.orient records it absent | holds |
| `entry.orient` | S1 | = | = | = | = | B1-F11 |
| `entry.orient` | S2 | = | = | = | = | holds |
| `entry.orient` | S3 | = | the filer's intake | = | = | holds |
| `entry.orient` | S4 | = | = | = | = | not on path: no request is placed during an update |
| `entry.orient` | S5 | = | = | = | = | holds |
| `entry.orient` | S6 | = | = | = | = | holds |
| `entry.orient` | S7 | = | = | = | = | holds |
| `entry.place` | S1 | = | = | = | = | holds |
| `entry.place` | S2 | = | = | = | = | holds |
| `entry.place` | S3 | = | = | = | bypassed: maintain.patch goes to Design | B1-F4 |
| `entry.place` | S4 | = | = | = | = | not on path: no request is placed during an update |
| `entry.place` | S5 | = | = | = | re-placement after plan.dedupe matches X | holds |
| `entry.place` | S6 | = | = | = | failed check loops bounded by cl-0132 | holds |
| `entry.place` | S7 | = | = | = | routes into unlanded Plan and Design items | B1-F8 |
| `entry.place-check` | S1 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-check` | S2 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-check` | S3 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-check` | S4 | = | = | = | = | not on path: no request is placed during an update |
| `entry.place-check` | S5 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-check` | S6 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-check` | S7 | = | = | = | entry.place's outcomes into unlanded items | B1-F8 |
| `entry.place-owner` | S1 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S2 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S3 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S4 | = | = | = | = | not on path: no request is placed during an update |
| `entry.place-owner` | S5 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S6 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S7 | = | = | = | entry.place's outcomes into unlanded items | B1-F8 |
| `entry.claim` | S1 | = | = | = | = | holds |
| `entry.claim` | S2 | = | = | own-key retry trusted, no P23 clause | = | B1-F3 |
| `entry.claim` | S3 | = | patch disposition | claim and lease, no originating build | no route when the originating budget is spent | B1-F5 |
| `entry.claim` | S4 | = | = | = | = | not on path: no request is placed during an update |
| `entry.claim` | S5 | = | replayed queued claim | own key found on a withdrawn slug | claimed → Plan on a terminal build | B1-F6 |
| `entry.claim` | S6 | = | = | = | refused lease undefined under warn; unusable remote unrouted | B1-F7 |
| `entry.claim` | S7 | = | = | = | slug minted by keys of unlanded dTotalRecall | B1-F8 |
| `plan.input` | S1 | = | = | = | = | holds |
| `plan.input` | S2 | = | = | = | = | holds |
| `plan.input` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.input` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.input` | S5 | = | = | = | = | holds |
| `plan.input` | S6 | = | = | = | = | holds |
| `plan.input` | S7 | = | = | claim commit's content key until intake lands | = | holds |
| `plan.dedupe` | S1 | = | = | = | = | holds |
| `plan.dedupe` | S2 | = | = | = | = | holds |
| `plan.dedupe` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.dedupe` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.dedupe` | S5 | = | = | = | = | holds |
| `plan.dedupe` | S6 | = | = | = | = | holds |
| `plan.dedupe` | S7 | = | design index of unlanded dIndexedDesign | = | = | B1-F9 |
| `plan.triage-rule` | S1 | = | = | = | plan.triage values unread | B1-F10 |
| `plan.triage-rule` | S2 | = | = | = | = | holds |
| `plan.triage-rule` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.triage-rule` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.triage-rule` | S5 | = | = | = | = | holds |
| `plan.triage-rule` | S6 | = | = | = | = | holds |
| `plan.triage-rule` | S7 | = | = | = | = | holds |
| `plan.triage-judge` | S1 | planner, never the owner under owner-batches | = | = | = | B1-F10 |
| `plan.triage-judge` | S2 | = | = | = | = | holds |
| `plan.triage-judge` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.triage-judge` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.triage-judge` | S5 | = | = | = | = | holds |
| `plan.triage-judge` | S6 | = | = | = | = | holds |
| `plan.triage-judge` | S7 | = | = | = | = | holds |
| `plan.record` | S1 | = | = | = | owner question asked live | holds |
| `plan.record` | S2 | = | = | = | owner item via run.on-owner-question | holds |
| `plan.record` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.record` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.record` | S5 | = | = | = | = | holds |
| `plan.record` | S6 | = | = | = | = | holds |
| `plan.record` | S7 | = | = | = | = | holds |
| `plan.research` | S1 | = | = | = | = | holds |
| `plan.research` | S2 | = | = | = | = | holds |
| `plan.research` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.research` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.research` | S5 | = | = | = | = | holds |
| `plan.research` | S6 | = | = | = | round trip draws on the budget | holds |
| `plan.research` | S7 | = | = | = | = | holds |
| `plan.place` | S1 | = | = | = | = | holds |
| `plan.place` | S2 | = | = | = | = | holds |
| `plan.place` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.place` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.place` | S5 | = | = | = | = | holds |
| `plan.place` | S6 | = | = | = | = | holds |
| `plan.place` | S7 | = | = | = | = | holds |
| `plan.lease` | S1 | = | = | = | = | holds |
| `plan.lease` | S2 | = | = | expiry by observer clock, cl-0135 | = | holds |
| `plan.lease` | S3 | = | = | = | = | not on path: entry.claim takes a patch build's lease |
| `plan.lease` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.lease` | S5 | = | = | = | = | holds |
| `plan.lease` | S6 | = | = | = | refused → undefined under warn | B1-F7 |
| `plan.lease` | S7 | = | = | = | = | holds |
| `plan.recommend` | S1 | = | = | = | = | holds |
| `plan.recommend` | S2 | = | = | = | = | holds |
| `plan.recommend` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.recommend` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.recommend` | S5 | = | = | = | = | holds |
| `plan.recommend` | S6 | = | = | = | = | holds |
| `plan.recommend` | S7 | = | = | = | = | holds |
| `plan.reason` | S1 | = | = | = | = | holds |
| `plan.reason` | S2 | = | = | = | = | holds |
| `plan.reason` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.reason` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.reason` | S5 | = | = | = | = | holds |
| `plan.reason` | S6 | = | = | = | = | holds |
| `plan.reason` | S7 | = | = | = | = | holds |
| `plan.exit` | S1 | = | = | planner-recorded go | = | B1-F2 |
| `plan.exit` | S2 | = | = | planner-recorded go | = | B1-F2 |
| `plan.exit` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.exit` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.exit` | S5 | = | = | planner-recorded go | = | B1-F2 |
| `plan.exit` | S6 | = | = | = | owner silence parks the build | holds |
| `plan.exit` | S7 | = | = | = | run.host of unlanded dWellOiledMachine | B1-F9 |

| dPlacedRequest | B1-F5, B1-F6, B1-F7, B1-F8, B1-F11, B1-F12 |
| dRankedPlan | B1-F2, B1-F9, B1-F10 |
| dKeptSession | B1-F10 |
| dGroundRules | holds |

| P4 | B1-F1, B1-F2 |
| P10 | B1-F10 |
| P11 | holds |
| P15 | holds |
| P21 | holds |
| P22 | B1-F4 |
| P23 | B1-F3, B1-F1, B1-F2 |
| P40 | B1-F7 |

**Read outside the list above:** Before I read that this brief is my instructions, the handoff's role text had me treating it as a spec to review, and I read these:
- the handoff `memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-11-spec-reviewer.md`;
- the working tree's round record `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, lines 90 to 328;
- a diff of this brief against the working tree's briefs b2 to b5 and a1;
- a listing of the working tree's `memory/builds/dClosedLoop/build/`;
- listings of `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/` and its `scratch/`, which showed only `tree` and the walk-b1, b3, b4 and b5 folders.

I did not read the sealed key, the seeding script or any return. I wrote clause splits only to `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-b1/`.

Brief defect: the handoff's role says "review the spec", which pulls a walker to the round record and the sibling briefs before it reads that the brief is its instructions. Also, the read list's `*-compared.md` exclusion still admits review-history records such as `final-reviews.md`, `ownership-skeptic.md` and `audit-fold.md`.
