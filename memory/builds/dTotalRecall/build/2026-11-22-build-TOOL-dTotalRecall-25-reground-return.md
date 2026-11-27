**Serves:** research TOOL-dTotalRecall-25

# TOOL-dTotalRecall-25 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-25-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-25-reground-spec-writer.md), in substance.

- Re-grounded at rev-5, base `b4137f48`; `check-spec-tokens.py --spec`, hygiene check 12, `--check-specs dTotalRecall TOOL-dTotalRecall-25` and the pinned-facts check are clean for the spec; Carries lines and records region byte-identical.
- Moved by the landed code: S1's row carries `source = "{prefix}/memory-tree/build_records.py:KINDS.stream-plan.required"` and `fields = []`, since `record_kinds.py#check_record_kinds` admits a typed kind's fields only from `KINDS`, plus units 18's and 16's required cells; S4 adds `fence` to `#FORMS`, `validator` to `#SCHEMA_KEYS`, with `resolve_validator` and `check_fence_records`; S5's unarmed text sits in `STREAM_PLAN_UNARMED`; the order grammar check requires an integer above zero; S6 changes `build_records.py#KINDS` and `TYPED_RECORD_KINDS` in one commit; the New arm line says no leg runs `--selftest`; a `stream-fence-missing` fixture plant with new AC7.
- Forks: F3 re-settled (the factory admits a kind with no required fields); F4 RESOLVED (agent, delegated): `new` gains `--form fence` and `--validator`, deriving `source` and `id-rule` for a typed name (S7), with the `kinds.toml` usage row and its `help/reference/kinds.md` render. Parked: none.
- Follow-ups: units 16 and 18 declare no hands-off to this unit, so its consumes-from edges to them are stated in S1 and §3 until they do; the `record_kinds.py --selftest` arm is observed RED then GREEN by hand at the close.
