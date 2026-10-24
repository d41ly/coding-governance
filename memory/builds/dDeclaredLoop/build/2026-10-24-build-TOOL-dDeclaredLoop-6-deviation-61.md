# TOOL-dDeclaredLoop-6 deviation 61 — the preset kind left on the pending list for dKeptSession, which takes presets

**Serves:** deviation TOOL-dDeclaredLoop-6

- **Departs from:** `cl-dClosedLoop-0091@48218b99` [factories]
- **Hand-off:** design-to-spec
- **Before:** the factories and conformance gates for commands, policy keys, presets, stages, hooks, roles and workflows
- **After:** the factories and conformance gates for commands, policy keys, stages, hooks, roles and workflows, the preset kind held on the shrink-only pending list naming dKeptSession, which takes presets
- **Cause:** design defect
- **Reason:** The clause gives this build the preset kind's factory and gate, and v2 gives presets themselves to dKeptSession, "the session, takes presets", with the `preset` key's owner dKeptSession and the policy reader's preset step waiting for it. No preset store exists for a factory to write into or a gate to read, so a factory here must invent dKeptSession's store, which the packet's non-goals forbid; and leaving it out fails the clause's word. Every option fails a bound, so the fork rule's rung 6 relaxes the weakest one (execution plan lines 924-946, TOOL-dDeclaredLoop-6 §8 F1). The non-goal is the owner's packet and the clause's word is the strongest tier, so the clause's word is the bound relaxed: the preset kind stays on dOrderedCharter-7's shrink-only pending list, its arming build dKeptSession, exactly the place foundations C3 to C5 give a kind whose factory has not landed. The relaxed bound is stated in the clause's text, so the clause's text moves and the as-built view's row and hash move with it, to `b0158e81`.
- **Evidence:** the clause, `memory/builds/dDeclaredLoop/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md:26`; v2's dKeptSession row, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:507`, and its `preset` row, v2:1141; the reader's preset step, `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-3.md` S3; the pending-list rule, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-foundations.md:383-388`; rung 6, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:924`; the new hash, `derive_clause_hash` (`tools/memory-tree/design_lib.py:169`) over the After text, which returns `48218b99` over the Before text
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of dDeclaredLoop's spec run, citing ER:328, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0091@48218b99
- **Caused-by:** TOOL-dDeclaredLoop-6
- **Bound:** the clause's factory and conformance gate for presets at this build
- **Tier:** strongest, a bound the carried clause states in its text
