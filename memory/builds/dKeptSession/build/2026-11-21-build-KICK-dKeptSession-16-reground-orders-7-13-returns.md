**Serves:** research KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9

# Returns — dKeptSession build run: build orders 7 to 13 re-grounded on the run's tree

Four gov-spec-writer agents, one per brief under `prompts/` named
`2026-11-21-prompt-KICK-dKeptSession-<lead>-orders-<orders>-reground-brief`, re-grounded the ten specs of build orders
7 to 13 on the tree at the run's BASE `c2a407b0`, concurrently over disjoint spec sets. The main loop relayed each
writer's `interface-changes` to the writer whose spec they touched, and resumed the writer of specs 15 and 14 once
spec 13's rewrite moved what they read. The build harness's spec stage, run in the same window, added the missing
guarded legs to the Gates lines of specs 6, 7, 21, 24 and 25 as leg-line-only rev bumps; they ride the same commit.

## The revs reached

- Orders 7 to 8: spec 16 rev-3, spec 12 rev-4 (its header closes the ask KICK-dKeptSession-66).
- Orders 9 to 10: spec 13 rev-4, specs 37 and 38 rev-3, spec 26 rev-2.
- Orders 11 to 12: specs 15 and 14, folded once more over spec 13 rev-4.
- Order 13: spec 30 rev-3, spec 9 rev-6.

## Rulings the main loop took on the returns

- Spec 9's fork F6 (unit 9 builds `loop_lib.py --steps`) and spec 26's fork F3 (unit 26 builds `budget.py state`,
  closing TOOL-dDeclaredLoop-104) are accepted at their picks, on the reasoning that accepted spec 1's F5: the verb and
  its grammar stay as ruled, dDeclaredLoop landed without it, and waiting on a later dDeclaredLoop run is waiting on a
  run no plan schedules.
- Spec 12's S3 observes the `always-resume` switch TOOL-dPlacedRequest-2 S7 built and builds no second one, as the ask
  KICK-dKeptSession-66 asks.
- Unit 13 owns the boundary verb's shape: detached, `--out <file>`, a bound per step and no overall `BOUNDARY_BOUND_S`,
  and `CARD_POSITION_BOUND` minted at order 9 for unit 15 to reuse.

## Carried to later waves' re-ground briefs

- 44 S21/AC19: replay order is map block, stored card, card —, route —, resume —, partial —, later units' lines, now — (spec 12 F4: now — stays last); S21's 'stored card, now — and the computed lines' contradicts it; AC19 replay-order plant keeps its name.
- 44 S39/AC34: unit 14 builds the context-fill scenario (no context-fill.jsonl); S39 shrinks to observation; AC34 holds; drop its "(deleted)" Files-touched entry.
- 44 S35: already satisfied (unit 14 withdraws AC7, its S6 points at KICK-dKeptSession-13 AC5).
- 44 S14: orient-calls row fields and CAP_CASES entry now built by unit 9 S6, S10; S14 reduces to observation. 44 S40: unit 9 S4 reuses _derive_quartiles; only derive_spent_tokens left.
- 56 S21: read the main-file-only SessionTree unit 30 S1 builds; only derive_main_transcripts left. 56 S12: re-quote unit 30's non-goal ("about two seconds", 2.14 s main file only). 56 AC10: count derive_main_transcripts, not build_session_tree (as spec 62 S7 says). 56 S26: met for unit 30.
- 44 S8: assumes BOUNDARY_BOUND_S = 10 and an 8 s hook budget; unit 13 no longer mints it (detached verb, per-step bounds). 44 S10: met by 13's S6. 44 AC20 premise holds.
- 43: item — skipped form now ends ' · at <sha8>' (item — skipped: <why> · at <sha8>).
- 10, 21: the boundary verb's output reaches the session at the next shell call after it finishes (detached, --out <file>), not the same call.
- 56: read_claude_version prints 'unknown: <why>' with exit 1 when no version.
