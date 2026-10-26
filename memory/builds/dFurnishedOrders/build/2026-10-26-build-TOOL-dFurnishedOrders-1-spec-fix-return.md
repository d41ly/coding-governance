**Serves:** research TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15

# Spec fix pass — dFurnishedOrders, its return

The return of the agent dispatched from `memory/builds/dFurnishedOrders/prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-1-spec-writer.md`, run direct/a85a461b1c0aa8b5b, extracted from its transcript by script.

All five findings and the sweep are fixed in `memory/builds/dFurnishedOrders/spec/`. The hygiene gate is green in my clone. But I couldn't run `tools/check-spec-tokens.py` there after my fixes: scratch-guard blocks it for `gov-spec-writer`, whose allowlist is `memory hygiene` and `lexicon naming predicates`. That checker's acceptance half still needs the main loop's re-run on the real tree.

**What I could and couldn't verify**
- **Spec-token checker before the fixes:** one run got through before the hook started refusing it. It printed 27 hits, and every hit naming a spec in this folder was one of F2 to F4 (plus one on a prompts file, see below). I didn't try to get around the refusal.
- **Hygiene, checks 2, 12 and 25:** run in my clone with every spec committed, it exits 0 and prints no FAILED line. Every line naming a dFurnishedOrders spec is a `READER NOT IN TREE covers it` note (units 15, 16, 4), which the brief says is not a red.
- **Check 12 can catch this:** with the old unit 8 put back, it printed FAILED naming unit 6's consumes-from 8 with no hands-off back. With the fix it is clean.
- **My own stand-in for the token checker:** over all 20 specs it found 0 problems in three things. Every backticked token in a sibling hands-off bullet is named by the receiving spec. Every sibling consumes-from has a hands-off back. No backticked `*.test.sh` sits in any §6.
- **Leg names:** all 15 legs I added match a `name` in `tools/gate-legs.json`.

**The changes, by unit**
- **F1, unit 8:** added a hands-off bullet to unit 6 naming `### Method slices`. S3 already spells the token where unit 8 renders the block.
- **F2, unit 6:** S3 now names `check_answered_range`, with `checkAnsweredRange` as the JavaScript copy the hook calls.
- **F2, unit 7:** `compose_return_arms` is now `derive_return_arms` in S2, §3 Non-goals and the consumes-from edge.
- **F2, knock-on in unit 15:** its hands-off bullet to unit 7 also had `compose_return_arms` in backticks. Once unit 7 dropped that name, the bullet would have gone red. I reworded it to "J3's factory as the lexicon spells it (§8 F1)". The old name now stays only in unit 15's S1, Inventory and §8 F1, which record the rename, and in its bullet to unit 19 (unit 19 names it too).
- **F3, unit 10:** AC4 now describes its own scratch fixture (the handoff, transcript and answered-call record) instead of the suite's arm 9. The suite was already declared on a `New arm:` line in §7.
- **F3, unit 5:** AC7's second half now checks the rendered `tools/workflows/tier2-review.js`: `{{VERIFIER_CONTEXT}}` appears 0 times there and at least once in the template. I added `New arm: tools/workflows/check-protocol-parity.test.sh · covers AC7 · …` to §7.
- **F4:** added the named legs to the §7 leg lines of units 14, 6, 7 and 9, exactly as the brief lists them.
- **F5, unit 11:** S2 and the §4 block now say the `### code-notes` block is absent when `annotations.delivery` is `off`, pointing to unit 18's S5 and §8 F4.
- **F5, unit 4:** `ORDER_SLOTS` now includes `instructions`, and the hands-off bullet to unit 18 names the `instructions` slot (unit 18 names it).

Every spec stays rev-1 with no §9 line. Nothing is committed and no index was rendered.

**Two things outside my scope**
- The pre-fix checker run also printed a `[packet]` hit on `memory/builds/dFurnishedOrders/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`. It names no spec file, so it isn't covered by the acceptance criterion.
- `git diff` shows unstaged changes I didn't make: the `BACKLOG.md` files of dBoundRoles, dDeclaredLoop, dOrderedCharter, dPlacedRequest and dTotalRecall, plus reuse scouts b and c.

The scratch clone is at `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-furnished-orders-b4ef78\56bbd6e7-78b5-422f-b186-74bf31f37f19\scratchpad\clone`. The last hygiene output is `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-furnished-orders-b4ef78\56bbd6e7-78b5-422f-b186-74bf31f37f19\scratchpad\hyg.out`.

Specs edited, all in `C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\`:
- 2026-10-26-spec-TOOL-dFurnishedOrders-4.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-5.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-6.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-7.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-8.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-9.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-10.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-11.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-14.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-15.md
