# dOrderedCharter — unit 71's builder return

**Serves:** journal PLAY-dOrderedCharter-71

Run wf_dc35bf5e-529, summarized from its return. Run wf_524c8b05-135 was refused at `--dispatch` before any write, because rev-1 carried no binding, and rev-2 added it.

- Built at rev-2 as pass commit `2781348a1`.
- What the unit landed:
  - `tools/govkit/govkit.py#selfcheck`: the adopter-name ban keeps a row only when its role is in `EPOCH_ROLES`, and its comment says what it does not check.
  - `tools/govkit/adopters.toml`'s header names the `--epoch` population.
  - A selftest arm after unit 70's source-rows arm.
  - Unit 70's three names renamed: `derive_terminated`, `add_known_twin` and `add_warn_breach`.
- Observed by probe:
  - AC1: the ban's population over this tree went from 392 files to 301, and none of the 301 names an adopter.
  - AC2: with `positional-refs.txt` moved back into a shipping role, it rejoins the population.
  - AC3 to AC7, and `lexicon OK` at 1209.
- No divergence, and no deviation record.
- Owed at the close:
  - `govkit selfcheck` itself, and `govkit selftest` with the new arm's RED-first observation.
  - `owed_rows.py --selftest`, the tags leg, and the section-7 legs.
