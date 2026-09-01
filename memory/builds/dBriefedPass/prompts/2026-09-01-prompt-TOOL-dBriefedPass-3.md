# Build brief — TOOL-dBriefedPass-3

**Serves:** journal TOOL-dBriefedPass-3

What the pass building this unit is handed, recorded by `--brief` and hash-joined to these bytes.

*This file first existed as a FIXTURE, written while proving that `--status`'s staleness reader
grades the latest row per unit rather than every row — the case a two-unit corpus can see and a
one-unit corpus cannot. Its first brief row therefore describes placeholder bytes and is superseded
by the row recording this content. The superseded row stays in the append-only region as the history
it is, which is the same property the reader was changed to respect.*

## The unit

`TOOL-dBriefedPass-3` — a build pass on an unspecced, THIN or out-of-order unit is REFUSED. Its spec
is `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` at rev-4, and that spec
is the only design input. Build what it says; to diverge, bump its rev first and say what moved.

## What this build already established that the pass must not re-derive

- The check ships in a NEW script, `tools/unattended/check-pass-order.sh`. It may not live inside
  `check-unattended.sh`: that script's argv contract accepts only `""`, `--only 28` and `--skip 28`,
  its sole manifest row is the `unattended kit gate` which is already about 44 s over its declared
  `BUDGET_kit_gate=120`, and §3 forbids scoping an existing leg to make room.
- **A row in `tools/gate-legs.json` is not a declared leg.** Five declarations land in one commit:
  the row, a `[[gate_leg]]` block in `tools/unattended/kit.toml`, a `tools/govkit/subject-pins.tsv`
  row, the leg name in `memory/map/features/unattended.md`'s `gate-legs` claim, and the regenerated
  `memory/map/generated/`. `govkit selfcheck` and `codebase-map coverage + freshness` are both
  unguarded, so a row landing alone reds the bar from this unit through to landing.
- `PASS_ORDER_CUTOFF` lands with its protocol carrier in the same commit. Check 22 joins conf keys
  in BOTH directions against the protocol's section-8 key table.
- The dispatch refusal names the unit ID and the STATE, never the empty SECTION. `plan_state`'s
  contract is one bare token by a recorded decision and `TOOL-dBriefedPass-1` §3 declines to widen it.
- The liveness line names THREE counts: builds graded, builds skipped by cutoff, units
  `unbuilt-in-range`.
- Arms split by subject: the dispatch refusals go in `tools/unattended/unattended.test.sh`, the
  history check in the new `tools/unattended/check-pass-order.test.sh`.
