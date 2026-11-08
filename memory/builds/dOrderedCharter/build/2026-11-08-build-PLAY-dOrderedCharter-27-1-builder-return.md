# dOrderedCharter — unit 27's builder return

**Serves:** journal PLAY-dOrderedCharter-27

Run wf_33dcace8-fa2, summarized from its return.

- Built at rev-6 as pass commit `8d235ff58`.
- What the unit landed:
  - The `code` slot: `load_sets.py#read_code_slot` reads `memory.code-budget` at 1,000 bytes per `k`, refusing a malformed value by
    name, and every role's load set gains its `code` line.
  - The `code-slot` census row in `tools/policy/caps.toml`, a family cap homed in policy, with `budgets.py` refusing a policy home on a
    row that is not a family.
  - The handoff's `code` input: its block's bytes are measured through the load-set check, and every role reads `input:code?`.
  - A policy case for the slot and its family-home refusal, eight plant rows, and the roles and size-caps help pages.
- Observed by probe: AC1 to AC4 and each plant row one at a time. AC2's command omits the builder's required `--input spec=`, which the
  probe added.
- Every handoff now names `input:code` as not supplied; the roles render selftest's golden output may move.
- The arms check reads no new unarmed site after this pass.
- Owed at the close: RED then GREEN for the eight rows and the policy case; the cap census arm and its fixtures guard; the tags leg.
