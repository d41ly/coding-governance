# dOrderedCharter — unit 12's builder return

**Serves:** journal PLAY-dOrderedCharter-12

Run wf_e2700414-ab9, summarized from its return.

- Built at rev-5 as pass commit `9cc88e71d`. A follow-up, `ac86d2c08`, declares the lock's extension dark in
  `.lexicon.conf`; without it the lexicon refused the newly tracked `.lock` file.
- `tools/playbook/instruction_units.py` gains:
  - the six statement types and their modals;
  - `check_statement`, which resolves a pointer through unit 19's tag index;
  - `check_document`, which skips code fences;
  - `write_lock_row` and `read_lock`, the one writer and reader of `.governance/instructions.lock`;
  - the `lock --check` and `grammar` verbs;
  - three plants.
- `render_playbook.py` drops the version marker line from the rendered charter and writes the charter's lock row after
  the region. A new selftest arm covers it.
- Readers of the marker re-pointed to the lock: the kickoff Skill's fallback step, now 18206 bytes against its 18432
  cap, and five lines of `WIRE-INTO-PROJECT.md`.
- `AGENTS.md` is re-rendered, and `.governance/instructions.lock` is committed.
- The leg `instruction grammar (statement types, provenance lock)` carries its own rows.
- Owed by unit 42, done: the nested `git` helper in `tools/memory-tree/build_records.py` is now `run_git`, and the
  lexicon is back at its pin of 1216.
- `Decided:` trailers:
  - the lock row is written in write mode after the region, never inside `render()`;
  - bare `grammar` also runs the lock check;
  - a pointer's trigger is the first word from a closed list.
- Observed by probe:
  - AC1: one definition of the policy-value type.
  - AC2 to AC4: every plant, unit 13's included.
  - AC3: the grammar over `AGENTS.md` names the four legacy shapes.
  - AC5: a scratch render leaves no marker and reads its lock row.
  - AC6: the leg's rows.
  - `owed_rows.py`: 0 owed, 1 deferred.
- No divergence.
- Left for unit 9:
  - `read_lock` silently drops a `target` entry that is not a table;
  - the session-kickoff dossier still names Step 2's fallback after the marker.
- Owed at the close:
  - The new leg, refused to the builder.
  - The section-7 legs.
  - RED then GREEN for both `New arm:` lines, the plants and the render selftest's lock arm.
  - Watch govkit's fixture adopters, whose write-mode renders now write a lock too.
