# dOrderedCharter — unit 25's builder return

**Serves:** journal PLAY-dOrderedCharter-25

Run wf_1c073568-840, summarized from its return.

- Built at rev-7 as pass commit `dc84ea200`, with two `Pass: none` follow-ups:
  - `1fd4a9c6d`: the policy mirror, in its own commit as S9 asks.
  - `676e056ff`: renames `fold_rows` to `derive_folds` and `inlined` to `check_inlined`, which the naming lexicon flagged.
- New `tools/playbook/tag_bundle.py` holds:
  - the bundle builder and the row fold;
  - the `--inline --bytes` budget;
  - the two `check --only` arms, calling unit 28's `check_edges` and `run_resolve`;
  - eight fixture cases and a selftest.
- `gov_tag.py` gains the `bundle` verb and `check --only`. Its `refs` and the bundle share a `read_refs` helper.
- The `tags bundle selftest` leg landed with its own rows: the dossier claim, the subject-pins row, a `[[gate_leg]]` in
  `tools/playbook/kit.toml` and the regenerated map.
- `gen_build_index` dropped asks 58 and 60 from the live backlog list.
- `Decided:` trailers:
  - one row per type, path and span;
  - fold rows neither inline nor end the inline run;
  - the `--only` arms read trailers only under `--base`.
- Observed by probe:
  - AC1 to AC8: each `bundle-*` plant.
  - The tree: bundles of `doc.build-method` and `doc.hygiene`.
  - Both `--only` arms over the tree read 8165 edges, 0 red.
  - AC9: the catalogue rows.
  - AC10: the leg's rows, and `owed_rows.py --base HEAD` with 0 owed.
- No divergence.
- Found, not this unit's: govkit's selfcheck reports that `tools/playbook/positional-refs.txt` names two adopters, which a shipped kit file may not. It is owed at the close.
- Owed at the close:
  - RED then GREEN for the `New arm:` line on `tag_bundle.py`.
  - The `tags` leg, the section-7 legs and the policy legs.
  - govkit selftest and its order pin.
  - The new leg's ceiling-evidence row.
