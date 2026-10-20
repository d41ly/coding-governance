# Second look: run B

**Serves:** research PLAY-dClosedLoop-1

Dispatch 191's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-32-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- B1-F6: refuted
  flow-steps [entry] `entry.claim`: a replay cannot reopen the withdrawn build. Flow-steps [transitions] says "the engine refuses any transition the table lacks", and the table has no withdrawn→planning row. `life.unlease` leaves terminal tombstones, which "refuse every acquisition" (cloud-and-scale [design] 3). dShippedRelease's row is "seen red on a queued claim replayed against an unleased build, which is refused". The default refusal route in [rules] then records the refusal, which is the outcome the fix asks for.
- B1-F7: refuted
  flow-steps [entry] `entry.claim` / `plan.lease`: no build goes on unleased. `plan.recommend` needs `plan.lease`, and the patch row (none → designing) needs "the lease record" as its witness. An unreachable remote is covered by `leases.offline`, whose `warn` value "queues a claim", and [entry] lists `leases.*` among its policies. A remote that cannot write refs "uses a branch-namespaced fallback or acquires nothing" (cloud-and-scale [design] 11). If the item is left with nothing to do, the position function answers `blocked` or `stuck` and raises an owner item (layer-runtime [decide]).
- B1-F8: confirmed medium
  flow-steps [entry] `entry.place`: new routes to Plan (dRankedPlan) and amend/patch to Design (dIndexedDesign). Neither is an ancestor of dPlacedRequest (its only parent is dDeclaredLoop). Stage 0 marks these routes "not an ancestor, UNCLASSED". The slug mint reads dTotalRecall's `builds.slug-*`, and dTotalRecall comes after dPlacedRequest. Only `repeat` gets a stand-in (cl-0156, "filed as an ask until dIndexedDesign lands"), against v2's rule that "each new dependency on a later build gets a stand-in, a class row or a move".
- B1-F12: refuted
  architecture-v2 [chain] preamble (PM-9): v2:401 sits in a dated 2026-10-17 revision log. The later 2026-10-18 note in the same record (v2:504-508, SP-1) says "dPlacedRequest, the entry, takes … the entry items" and that "each moved … item … changes owner with its clause". So v2 states one current owner, and it matches flow-steps:99 and cl-0122.
- B2-F4: refuted
  architecture-v2 [policies] `flow.rework-budget` / cl-0115: the clause says "the base alone before that freeze" (a single freeze) and "keyed to the build so units a loop mints cannot reset it". It also owes "seen red on a planted loop that mints a new unit each lap", which is the growing-budget case the finding describes. stall-and-loop [design] 1 adds that "a chain of patch builds draws on one budget".
- B2-F7: confirmed high
  layer-runtime [isolate]: under the default `build.worktree: shared`, the build has "the build's one worktree" and a commit queue on the holding node. "Integration before release" covers unit branches only. Meanwhile cloud-and-scale [design] 8 has any node pick "ready, unleased units" across builds, and `design.streams` hands one build's units to several node units. Nothing says where node x commits or how its pass joins the build branch. Its fenced push to an advanced branch has no declared route, so S2 has no path to integration (c2).
- B2-F13: refuted
  architecture-v2 [chain] cl-0407: cl-0049 on dOrderedCharter's row already names the move: "`compute_coverage` moved to `tools/lib` … with … the pure `drop_touched_exemptions` beside it, so no core build imports codebase-map (H5), its consumers rewritten in the move's unit while `map_lib` re-exports the moved names". dOrderedCharter is an ancestor of dScopedBuild. Today the function is at `tools/codebase-map/map_lib.py:1373`, so this is a planned move, not a misplaced citation.
- B2-F15: confirmed medium
  architecture-v2 [enforcement] P18: the row cites only cl-0176 ("resolved by the role that meets it and recorded") and cl-0390 ("fork resolution by `design.forks`"). The fork record carries only "its id, its resolver and its declared class" (flow-steps `design.decompose` / `design.unit-spec`). No clause or check requires the options ranked by feature-richness and then expandability. The ranking appears only in the charter render (v2:973) and the default value's name.
- B3-F4: confirmed high
  flow-steps [deploy] `deploy.mandate` / [breakpoint]: an owner breakpoint is resolved by `run.on-owner-question` "when it is raised, never for a ratification". Its witness may be "under `best-effort-recorded`, the supervisor's recorded choice". `best-effort-recorded` is the default, and no pair rule ties it to `autonomy: three-gates`. So an owner who sets three-gates and keeps the default gets a landing gate the supervisor fills, which `deploy.mandate` then accepts as the owner's disposition (c3).
- B3-F8: refuted
  flow-steps [test] `test.merge` / [deploy] `deploy.land`: a build does not sit with no owner item. The position function answers `stuck` ("no frontier, while the build is not terminal", which "raises an owner item at once") or `blocked` (layer-runtime [decide]). A refused instance left on the frontier is re-dispatched against the budget until `flow.on-exhausted` ends the build ([rules]). The transitions table also has the row "deploying | `deploy.land`'s class refused before the push | testing".
- B4-F13: confirmed medium
  flow-steps [breakpoint]: once an owner item is decided (by the supervisor's choice when raised, or by the recommendation applied past the deadline), no item, transition row or clause says what an owner disposition arriving afterwards does. S1 injects exactly that late answer, and searches for late or after-deadline handling in the design records find none.
- B5-F7: refuted
  layer-expansions [design-distribution] `kits.offer`: the row names the eighth kind of target-side code as "dShippedRelease's update hook calling `test.seed` and the `adopt` program … which the offer leaves to the adopter's own run". It routes "an update that needs target-side execution … → an outbox order the adopter runs itself". cl-0430 and retrofit [seed] state that order. So an update bringing a new check does get an order, and under `refuse` the adopter's lander also refuses the update until the seed runs.
- B5-F9: refuted
  flow-steps [adopt] `adopt.reconstruct`: on-touch reconstruction is carried by cl-0406 on dScopedBuild's row: `build.unit-pass` and `build.scope` "claiming the baselined map keys its write set holds (dossiers)". Retrofit [origin] counts "a first-touch dossier" as `reconstructed@<sha8>`. Leaving untouched code unreconstructed under `on-touch` is the design's rule, retrofit [never]: "No reconstructed record for code no unit touched".
- B5-F12: refuted
  layer-runtime [schedule]: each period's key, witness and cadence lease are unique to that period, and the witness is checked before and after the lease is taken. A node seconds slow at a boundary derives the previous period, which is either already witnessed (so it skips) or genuinely missed ("a missed period runs at the next wake"). A fast node runs the next period early, and the other node then skips it. No period gets two runs or two records.
- B5-F13: refuted
  layer-expansions [design-distribution] `kits.currency`: the receipt does record the installed commit. `kits.currency` itself counts "release tags dated after the installed commit", and schema 4 extends today's receipt, which carries `gov_commit` and per-file `sha256` rows (`tools/govkit/govkit.py:8020`, `RECEIPT_SCHEMA = 3` at `:49`). So other bytes would not sit "under the same receipt". The date-skew miscount only matters within seconds of a periodic cut.
- **Read outside the list above:** none.
