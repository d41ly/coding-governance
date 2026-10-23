**Serves:** research PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55

# Promoted-fix brief — the round-2 promotions, before their commit

Fix the hits below over the round-2 spec audit's promotions, `PLAY-dOrderedCharter-50` to `-55`, and the
round-2 hands-off fold of `PLAY-dOrderedCharter-49`, so `python tools/check-spec-tokens.py` and
`bash tools/memory-tree/check-memory-hygiene.sh --staged` name no dOrderedCharter spec, changing nothing else.
Round 2 is the last spec review under the owner's cap
(`memory/builds/dOrderedCharter/prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-owner-review-cap.md`), so these
specs carry forward unaudited: fix only what the checks name.

- `[size]`: `PLAY-dOrderedCharter-49` grew to 50853 B with its rev-2 hands-off fold, over the 49152 B ceiling in
  `tools/template-size-limits.txt`. Trim prose under the ceiling, every finding id, criterion, fork and edge kept.
  Its rev-2 is uncommitted, so edit in place under rev-2 with no further bump.
- `[guards]`: `PLAY-dOrderedCharter-55`'s §4 files-touched names `tools/gate-legs.json`, whose guard trips leg
  `run-gates canary`, absent from its §7 leg line: name that leg on the §7 leg line.
- Hygiene check 12: acceptance bullets naming no backticked witness, `PLAY-dOrderedCharter-54` AC2 and AC4 and
  `PLAY-dOrderedCharter-55` AC5 and AC21: give each the backticked command or file its observation runs.
- Hygiene check 25: §2 items that retire a named thing with no `**Readers:**` clause, in `-50`, `-51`, `-52` and
  `-55` (the items are named below): write `**Readers:** by name:` with the readers that spell the name, then
  `by value:` with its value's readers or `NO VALUE READERS` and a reason, each reader found by a grep you run, as
  your token-fix pass did for `PLAY-dOrderedCharter-1` S6.
- The promoted specs are uncommitted at rev-1, so edit in place with no rev bump. Touch no deviation record and no
  spec numbered 1 to 48. Do not commit, stage, or render the index. Re-run check 12 and check 25 (`--only 12` and
  `--only 25`) and report their dOrderedCharter lines and spec 49's final size.

## The hits, verbatim

- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-55.md [guards] `run-gates canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates canary', absent from the §7 leg line
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [size] `size <- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md` — 50853 bytes, 1701 over the spec ceiling 49152; split the spec or move history out of it
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-50.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S2, S4
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-51.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S2, S5
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-52.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S2
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-54.md (acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF): 2026-08-15 -- AC2, AC4
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-55.md (acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF): 2026-08-15 -- AC5, AC21
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-55.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S1, S7, S10, S11, S12
