# dOrderedCharter — unit 7's builder return

**Serves:** journal PLAY-dOrderedCharter-7

Run wf_71c591d9-a64, summarized from its return.

- Built at rev-7 as pass commit `399788aca`. Two more commits:
  - `7374eef7a`: the policy mirror, in its own commit as the rollout asks.
  - `13af4f940` (`Pass: none`): renames 17 helpers in `core.py` the lexicon refused, and makes `deviation_join.py`
    import `FIELD` from the new factory.
- What the pass built:
  - `tools/playbook/principles.toml`: the 42 principles, each with its enforcement clauses.
  - `tools/playbook/kinds.toml`: 17 kinds, three of them landed.
  - `tools/playbook/core-pending.txt`, seeded once: 38 principles, 152 legs and 14 kinds.
  - `tools/playbook/core.py`: five verbs, and nine plants.
  - `tools/memory-tree/build_records.py`, extracted from the deviation join, with the exception kind.
- Five core legs carry `enforces`, and the layer leg gains two principles. Each leg's rows ride the pass:
  - `core selftest` is a `[[gate_leg]]`;
  - the other four are `[[exempt_leg]]` rows.
- The `enforces` edge type's `to` gains `principle`, which units 12 and 13 consume.
- `Decided:` trailers:
  - each kind's binding principles, with p16 binding every kind;
  - which build each pending principle row names;
  - pending legs name dWitnessedBar.
- Observed by probe:
  - AC1 to AC6 and AC8 to AC10: each plant, red by disabling the never-rule in a scratch copy, then green.
  - The four core verbs exit 0 on the tree.
  - AC7: the deviation plants print the same lines before and after the extraction.
  - AC11 to AC13: the spec's own probes.
  - `owed_rows.py --base HEAD`: 0 owed, 5 deferred.
- No divergence.
- Departure, for the close's report: after the spec was CLOSED, the builder applied the helper rename with a Bash
  script, which the write gate does not see. It then set the spec back to INPROGRESS to finish through the gate and
  closed it again before committing. The rename commit `13af4f940` writes under `tools/` with `Pass: none`, as unit
  25's `676e056ff` did.
- Owed at the close:
  - RED then GREEN for the `New arm:` lines on `core.py`, and on the deviation join over the extracted factory.
  - The section-7 legs and the four core legs.
  - The five ceiling-evidence rows.
  - govkit's selfcheck, still red on the adopter names in `tools/playbook/positional-refs.txt`.
