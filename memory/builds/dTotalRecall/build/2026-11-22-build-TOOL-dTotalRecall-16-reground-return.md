**Serves:** research TOOL-dTotalRecall-16

# TOOL-dTotalRecall-16 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-16-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-16-reground-spec-writer.md), in substance.

- Re-grounded at rev-3, base `a3d6d07e`; `check-spec-tokens.py --spec`, `unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-16` and hygiene check 12 exit 0; Carries lines and records region byte-identical.
- Moved by the landed code: `memory.map-purpose` reads through `tree_lib.py#read_policy_value`; AC2's `new` passes `--home` and unit 18's `--layer`, `--lifecycle`, `--readers-none`; `chain.toml` rows hold `purpose` as a plain string (`tag_index.py#check_chain_registry`), the chain path read by `ast` from `tag_index.py#CHAIN_REGISTRY`; the catalogue row re-renders `help/reference/policy.md` and the unit drains `policy:memory.map-purpose` from `memory/project/docs-undocumented.txt` (new AC7); `kinds.toml` usage and `help/reference/kinds.md` gain `--purpose`; no leg runs `record_kinds.py --selftest`, said on the New arm line.
- Forks RESOLVED (agent, delegated): F4 namespace members leave the review and the write (PLAY-dOrderedCharter-22's landed `purpose` check already reds a member missing it); F5 a record kind's derived purpose takes `--from <path>`; F6 a chain row keeps a string purpose, its source cited in the review record; F7 under `ledger` the setting repository registers `purpose-pending`, the write refusing until it does; F8 no policy kit resolving reads the catalogue default `review` with one line. Parked: none.
- Follow-ups: TOOL-dTotalRecall-18 declares no `hands-off TOOL-dTotalRecall-16`, so unit 16's consumes edge sits as a §3 line until it does; TOOL-dTotalRecall-8 S10 fills a catalogue row but does not drain `policy:memory.code-languages` from `memory/project/docs-undocumented.txt`.
