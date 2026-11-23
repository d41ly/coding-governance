**Serves:** journal TOOL-dBoundRoles-26

# TOOL-dBoundRoles-26 — the main loop's decision over the first builder's divergence

Run `wf_9a71755a-a4e` read rev-5 against `4fb8c2401` and wrote nothing. §4 Migration's claim that no role's `outcome`
set holds `refused` stopped holding when TOOL-dBoundRoles-4 (`5f0e8eaf8`) gave `gov-prompt-writer` the return
`outcome:framed|refused` with a `why` field. The builder also named three gaps in the producer route, the reader's
signature and AC4's fixture. Direct spawns of a spec writer are still refused on this run, because the session's spawn
guard predates TOOL-dBoundRoles-17's `item=`. So the main loop settles each item by M3 as a delegated resolution, and
the next builder builds the result under the one deviation record its brief names. widens: none · relaxes: none.

1. **The prompt writer moves onto the arm.** Options: (a) migrate `gov-prompt-writer` to the arm: its `return` drops
   `refused` and `why`, so its outcome is `framed` alone and it refuses through the arm's `rule`, `remedy` and
   `actor` like every other role, and its body's two lines that say "return `refused` with `why`" are restated to name
   the arm; (b) narrow the catalogue rule and S2's branch to leave that one role's own `refused` alone. (b) keeps two
   refusal shapes in one catalogue, the drift §8 F1 rejects, and the clause asks for the typed refusal in "every role's
   return template". Pick (a). `tools/roles/agents/gov-prompt-writer.agent.md` joins the write set with its renders.
   TOOL-dBoundRoles-4's `read_framing` in `tools/roles/handoff.py` names the refusal's `remedy` where it named `why`,
   and its `refused` outcome still refuses the render by name. The render self-test's arm 24 plants in
   `tools/roles/render_agents.py` that carry `refused` with `why` move to the arm's fields; that file joins the write
   set. options: (a) > (b) · pick: (a) · admitted-by: principle.p18
2. **The producer route reads the answered work order.** `route-refusal` finds the work order the way
   `check-return-file` does, through the return's `answers` line. The producing item is the item of the first row of
   that work order's `### upstream:rows` block, in the rows' own order. It is printed as one trailing field after the
   re-offer: `refusal — producer · route route-back · re-offer never · item <tag>`, so AC1's expected text stays a
   prefix of the line. A return with no `answers` line, or a work order with no upstream rows, answers `driver` and
   says so in that trailing field. AC1's producer plant carries a work order with an `### upstream:rows` block.
3. **`route_refusal(refusal, role, build, repo, budget_spent=False)`.** `role` and `build` come from the answered
   work order's marker, read through `MARKER_RE`; `role` selects the `roles.retries` bound for a `self` route, and
   `build` names the run on the route line. `repo` is what `resolve_owner_question` reads the policy through, and
   `budget_spent` is S5's flag. With no answered work order, `role` and `build` are `-`.
4. **AC4's arm uses the suite's own fixture pair.** The arm in `tools/unattended/unattended.test.sh` records its
   refusal on the item and key the `tRun` fixture's position engine already holds, `item.build.base` with its fixture
   key. The pair at `tools/loop/position.py@710b2d07:173` belongs to the loop kit's own plant and is not reused.
