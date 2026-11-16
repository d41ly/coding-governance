**Serves:** journal TOOL-dDeclaredLoop-33

# Builder return — TOOL-dDeclaredLoop-33, dispatch 1: the reachable rule reds gov's own composition on item.build.resolve, whose one need lies in the test program

## Why

DIVERGENCE: S3 (rule `reachable`), as rev-6 writes it, reds gov's own composition at landing. AC10 and §5 Rollout need that composition to exit 0, and §4 "Gov's own cycles at landing" bounds only cycles, so the spec as written cannot be built. The facts below were read at HEAD e8018d94f.

What S3 says: each program's items are walked from "its items with no needs", along routes to declared items and from each need to the item needing it. `item.build.resolve` is in the step.build program, and its one need is `item.test.merge`, which belongs to the test step. The only route into it is `item.test.merge` conflict -> resolve. Walking from the build program's entry, `item.build.base`, never reaches it. That gives one `reachable` finding on gov's rows, so AC10 is red.

This is not caused by later units. The row was already at the spec's own measuring tip, 250b236f (line 1555 of tools/loop/loop.toml there), and units 50, 51 and 19 did not add it. It also reds every build's composition, so S11's step boundary would refuse every move that applies a change.

Changing only the entry does not fix this. Following the need edges from S3's own wording, every item reaches back through its needs to an entry of its own program. So the only items this rule can ever flag are those whose needs leave their program, and `item.build.resolve` is the only one in gov. If an item whose needs all lie outside its program counted as an entry, no item could ever be flagged. The rule would then check nothing, and AC3's `orphan-item` plant could not go red.

What I measured with the gov rows at HEAD:
- Walking routes only from each program's own entries leaves `item.build.resolve`, `item.deploy.snapshot`, `item.deploy.unlease` and `item.review.cost` unreached.
- Walking routes and needs from every program's entries reaches everything.
- Walking routes and needs from each program's own entries (rev-6's reading) leaves only `item.build.resolve` unreached.

What the spec would have to say: S3, AC3 and AC10, plus §4's rules table or "Gov's own cycles at landing", need to state how an item reached only through another program counts. For example, the walk could start from every program's entries but grade only this program's items, with AC3's orphan rebuilt so it still goes red. Or `item.build.resolve` could get a declared bound, for example a third pending-row kind.

Everything else I checked holds:
- `scan_cycles` is inline in loop_lib.py. `check_program`, `read_transition_rows`, `derive_direction`, `ENDING_OUTCOMES` and `DYNAMIC_TO` exist as cited.
- In budget.py, `CAUSES` holds route-back and fix-pass. In the policy kit, `derive_bounds`, `DEADLINE_TYPES`, `derive_landed_owners` and `check_reader_coverage` exist, and the catalogue has the `flow.wait-ceiling` and `run.owner-deadline` rows.
- `render_state_row`, `STATE_ROW` and `write_flow_states` are in adapt.py. `write_transition`'s truncate span is in loop_transition.py. The composition lines of `derive_position_into` are in position.py.
- In unattended.sh, `verb_dispatch`'s fix-pass draw is at #verb_dispatch, and `WIRING_CEILING` and `PREFLIGHT_CEILING` exist. `CLAIM_WAIT_CEILING` is in push-main.sh.
- In registry.toml, `loop budget fixtures` is an `[[exempt_leg]]`. scenario.py has the `then-cycle` plant. The `loop adapt fixtures` budget row reads 225. `git log --grep=Gov-Transition:` prints no live build.
- The terminal rule holds on gov's build level: every open state reaches a terminal. `item.build.ratify` is the only item with an owner actor.

One count moved and would have been a deviation record, not a divergence: gov's item-route cycles are now 23 PINNED at e8018d94f, up from the spec's 21. The two new ones are unit 50's `item.review.dispose -> item.review.fold` and `item.review.dispose -> item.review.fold -> item.review.trigger -> item.review.pin -> item.review.report`. The build table still leaves one cycle, `paused -> paused` on `item.life.request` pause, as F5 says.

## Summary

TOOL-dDeclaredLoop-33 is not built and nothing is committed: rev-6's `reachable` rule (S3) would make gov's own composition fail at landing on `item.build.resolve`, which AC10 forbids. The spec writer needs to revise S3, AC3, AC10 and §4; the details are in `why`.

I stopped before my first write. I made no product edits, so there is no patch to save. I did not run `--dispatch` or `--brief`: the brief is already recorded in memory/builds/dDeclaredLoop/RUN.md (the brief row for this unit, reason 2c0873edcaa9), and there was no write set to declare. The untracked prompt files in the worktree belong to other units and I left them alone.

Checks that ran: read-only `python -c` probes over the gov definition at HEAD, using the kit's own readers:
- `scan_cycles` over item routes: 23 cycles; the build-table edges under F5's set-aside rule leave one cycle, `paused -> paused`.
- Reverse reachability to the build terminal set: every open state reaches one.
- The `reachable` walk read three ways, which is how the divergence was found.
- Greps confirming the spec's other citations in unattended.sh, push-main.sh, registry.toml, selftest-budgets.txt, catalogue.toml and policy.py.

These probes stand in for nothing: no gate, suite or bar ran.

Owed when the unit is dispatched again:
- Gov's composition at HEAD stays at 23 item-route cycles, PINNED at e8018d94f, not 21. Record that in a deviation record.
- F7's departure needs its own deviation record.
- The `New arm:` observations for AC1 to AC5, AC7 to AC9 and AC11 are the main loop's, at the close.
