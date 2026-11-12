# dOrderedCharter — unit 33's builder return

**Serves:** journal PLAY-dOrderedCharter-33

Run wf_c5f80ace-714, summarized from its return.

- Built at rev-6 as pass commit `f75582e3c`, with the policy mirror regenerated in `a9ee875fa` as the spec's rollout asks.
- What the unit landed:
  - `tools/playbook/pins.py`: each gov change record's mark checked against its Before and After text, a pinned edge walked to standing,
    stale, renamed or orphaned, and a `drift` verb with its fixture plants.
  - An empty `tools/playbook/spelling-map.toml`.
  - The govkit update reads `instructions.stale` and runs the drift verb for a target claiming the playbook entry, holding the playbook
    kit on a refused read or a red, and returning before any write under `refuse`.
  - `tools/govkit/fixtures/stale_edges.py`, the update criterion's fixture, recorded as deviation 335.
  - The `instructions.stale` catalogue row's summary and usage, and the overlay help page's drift section.
- Decided in the pass: a pin no change record reaches is held stale; the mark check runs inside the drift verb; the tally key is
  `unit:<state>`.
- Observed by probe: every plant green and red with one function stubbed; both update plants with and without the stub; AC10's
  commands. After the pass the main loop read the arms check with no new site.
- AC7 and AC11 wait on fork F5's later commit, once unit 40 tracks a gov unit row: the `unit` class row in the surface classes and the
  `unit` usage row, both paths in this unit's dispatch.
- Refusal sites with no arm: the change-mark check's `is not committed` and `does not match its change`.
- The update's mode check keeps its own copy of the three modes, refused for edit once the spec was CLOSED.
- Owed at the close: RED then GREEN for the render selftest arm, the govkit selftest arm and the step gate's surface-classes arm; AC7 and
  AC11 after unit 40.
