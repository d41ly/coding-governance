# TOOL-dPlacedRequest-10 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-10

The unit was built from its spec at rev-4 (PINNED) on base `c965feaac`. `tools/loop/placement.py` gains
`tools/loop/placement.py#derive_entry_fact` over the table `tools/loop/placement.py#ENTRY_FACTS` (shared
interface I20), the scenario arm of `tools/loop/placement.py#check_placement` in
`tools/loop/placement.py#check_placement_scenarios`, the default-aware selection
`tools/loop/placement.py#derive_placed_scenarios`, the write-boundary readers
`tools/loop/placement.py#parse_placement_scenarios` and `tools/loop/placement.py#parse_placement_facts`
with `tools/loop/placement.py#render_placement_facts`, the block and return keys `scenarios` and `facts`,
and the record's two lines in `tools/loop/placement.py#print_claim_lines`. The spec's
`select_scenarios(facts, composition)` is TOOL-dDeclaredLoop-27 S5's function, shipped and specced there as
`tools/loop/scenario.py#derive_admitted_scenarios(facts, rows, default)` after the lexicon refused the
first name; this unit calls it over `tools/loop/scenario.py#read_scenario_rows` and
`flow.scenario-default`, and never re-specs it. A tree with no scenario composition prints
`placement: scenario · unread` and checks no scenario, as the transition writer does. The fixture gains
`tools/loop/placement.py#write_scenario_composition`, which copies the kinds register, the namespaces
table, the scenario schema and gov's pack into a plant's repository, less the tags a plant drops.

No gate, suite or bar ran in this pass, and no `--selftest`: the role hook refused the `--fixture` run
over every plant as the `loop placement fixtures` leg. Each criterion below was observed by a probe of the
changed code, one `python tools/loop/placement.py --fixture --plant <case>` per plant, run by direct CLI
over each of the 21 (DERIVED) plants of `tools/loop/placement.py#PLANTS`, every one printing `held`
(the run's node, 2026-11-20, PINNED).

**Evidences:** TOOL-dPlacedRequest-10
- AC1 — `--plant predicate-fails`: a `new` block naming `scenario.patch` exited 1 under `refuse` printing
  `placement: refused — new · scenario-predicate scenario.patch`; the block naming `scenario.feature`
  exited 0 with `check: pass`.
- AC2 — `--plant scenario-missing`: a `new` block with `design-only=true` naming `scenario.feature` alone
  exited 1 printing `scenario-missing scenario.design-only`; under `placement.check` = `record` it exited 0
  and the block's `scenarios:` read `scenario.feature+scenario.design-only`.
- AC3 — `--plant entry-mismatch`: a `new` block whose facts typed `entry=patch` exited 1 printing
  `entry-mismatch patch feature`.
- AC4 — `--plant continue-with-scenario`: a `continue` block naming no scenario passed, exit 0, and one
  naming `scenario.feature` exited 1 printing `scenario-not-placed scenario.feature`, the lease fact
  passing, so the scenario arm alone refused it.
- AC5 — `grep -n "scenarios · facts"` over `tools/roles/agents/gov-orienter.agent.md` found its `returns:`
  line; `python tools/roles/render_agents.py --write` wrote the orienter's render and
  `python tools/roles/check_roles.py --write` reported 0 (DERIVED) defects with the catalogue region of
  `tools/roles/README.md` re-rendered.
- AC6 — `--plant no-admit`: over a pack with `scenario.amendment` dropped, an `amend` block naming no
  scenario exited 0 printing `facts — entry=amendment`, and the block read
  `scenarios: scenario.feature (default)` with `check: pass`.
- AC7 — `--plant claim-lines`: `record` on the passed `patch` block printed exactly `disposition`,
  `build`, `playbook`, `reason`, then `scenarios: scenario.patch` and
  `facts: entry=patch; design-only=false`; the passed `new` block printed its `scenarios` and `facts`
  lines after `reason`, and a refused block printed nothing, exit 1.
- The checklist's refusal branches — `--plant scenario-refusals`: a tag outside `scenario.<segment>`, a
  tag twice, a fact of another shape and a fact twice each exited 1 at `place` with no block written; a
  block naming the shared scenarios out of order exited 1 printing `scenario-order`; and a
  `flow.scenario-default` naming a scenario the plant's pack lacks exited 1 naming the key; a block
  appended by hand with a malformed tag exited 1 at `check`. `--plant observation` printed
  `placement: scenario · unread` over a tree with no composition. These two plants were extended by the
  checklist pass over the first commit, and the module's docstring now states that the scout's facts
  but `entry` are evaluated as written.

**Owed at the close (main loop):** the `loop placement fixtures` leg over every plant; the `New arm:` line
of the spec's Gates section, its failing case staged by `predicate-fails` with the predicate re-run
removed, observed RED and then GREEN; and the rest of that section's legs.
