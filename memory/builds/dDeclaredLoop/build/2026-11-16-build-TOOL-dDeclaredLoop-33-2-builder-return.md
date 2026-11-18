**Serves:** journal TOOL-dDeclaredLoop-33

# Builder return — TOOL-dDeclaredLoop-33, dispatch 2: rev-7's boundary check refuses the adapt plants' compositions, gov's pending list goes stale over a build's exclusions, and F7's amends record moves the carried clause's hash

## Why

DIVERGENCE: rev-7 still cannot be built as written. Three checks fail, two in the spec's design and one in how F7's record has to land. All were read at HEAD 3918078c9, before any write.

(1) S11 and the §5 sweep row for `write_transition`. The sweep says adapt.py's additive, owner-approves and loosening plants "compose gov's green composition". At HEAD they do not. S1 and S3 read the programs through `check_program`, and it refuses every composition those plants apply:
- The add row in `tools/loop/adapt.py#run_adapt_plant`, `item.build.adopter.lint-pass`, carries only tag, step, actor and needs. A probe of `check_program` over gov's rows plus that row raised "the item item.build.adopter.lint-pass carries no outcomes".
- The loosening plant's applied `exclude item.test.flakes` composes with exit 0. It leaves `item.test.route`'s `nondeterministic` route aimed at the excluded item, and the probe raised "the item item.test.route routes nondeterministic to 'item.test.flakes', which is no declared item".
So S11's check refuses the plants' moves: additive, owner-approves, mid-step and loosening. Those are four plants of `loop adapt fixtures`, and AC9's second clause runs the loosening plant. The spec has to say either that the plants change (a whole item row, a different exclusion; adapt.py's plant edits are not in its Scope) or what the boundary does with a composition `check_program` refuses.

(2) §4 "The pending list" and S5. A cycle row goes stale once the graph `check_counted` builds no longer holds the cycle. A wait row goes stale once its item is gone. The list is gov's, and the push and S11 also grade every build's composition. A build that excludes or supersedes an item on a pending row would then report stale findings and be refused at every boundary. For example, excluding `item.test.flakes` drops two pending test cycles: flakes -> select -> verdict -> route, and flakes -> verdict -> route. The spec has to say whether staleness is graded over gov's composition only, or how a build's composition reads gov's list.

(3) F7's deviation record. A record departing from `cl-dClosedLoop-0118@4c8ef789` must carry an `amends` or `supersedes` row; `tools/memory-tree/asbuilt_view.py` reports a clause departure without one. An `amends` puts the record's **After:** text in the as-built view, which moves the clause's hash in the view. I re-derived the hash: `derive_clause_hash` over the view's row reads `4c8ef789` today. The move makes this spec's `**Carries:** cl-dClosedLoop-0118@4c8ef789 whole` a stale pin in the carries join, `tools/check-spec-tokens.py#scan_carries`. The join grades CLOSED specs, only WONTDO is set aside, and the spec is dated after SPEC_CARRIES_CUTOFF 2026-10-21. That pin sits under §7's `spec tokens (a spec's own names resolve)`. The clause's backticked tokens must also stay in a carrier. Re-pinning the Carries line is a spec edit a builder may not make, and once the pass closes the spec is frozen. The precedent is deviation 61: unit 6's spec writer wrote the `amends` record and re-pinned `cl-dClosedLoop-0091@b0158e81` in the same spec commit. So the F7 record, with the amended clause text and the re-pinned Carries line, has to land with the spec revision before the build pass.

Fold these too while revising; they do not block on their own:
- §4's cycle row grammar says `<tag> -> <tag>`, but the build-table cycle F5 leaves is a cycle of states, `paused -> paused`. Its owner is dWellOiledMachine, through the `item.life.request` stand-in.
- AC2: every open build state is left by the `@open` pause row and the `@any` ending rows, so "a build state no row leaves" can only be planted by narrowing those rows' `from`. Say so.
- §4 Data model: `derive_direction` needs the step orders, and the composition does not hold them.
- §4 rule 2: say whether the first-dispatch route, `item.build.unit-lease` held -> `item.build.unit-pass`, and the cross-step routes into gov-builder items (`item.test.merge` conflict, `item.test.attribute` code-miss, `item.test.seen-red` missing) carry `fix-pass`. The cross-step ones are already counted by their backward build rows.

## Summary

I built nothing and committed nothing: rev-7 diverges from the code at HEAD in three places, all found by the sweep before any write. The details are in `why`.

I made no product edits, so there is no patch to save. I also did not run `--dispatch`, because there was no write set to declare, and I did not run `--brief`. The brief is already recorded in `memory/builds/dDeclaredLoop/RUN.md` (the brief row for TOOL-dDeclaredLoop-33, reason 2c0873edcaa9), and a re-run would have left that file modified with nothing to commit.

What I re-derived at HEAD 3918078c9, using only read-only `python -c` probes and a probe script under the scratchpad (`C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/probe33.py`) that calls the kit's own readers:
- Gov's composition: 23 item-route cycles over 45 edges, PINNED at 3918078c9, matching rev-7's figure. There are 105 PINNED routes between declared items.
- F12's reachable walk leaves no item unreached on gov's rows.
- `item.build.ratify` is the only item with an owner actor.
- No composed stage, and no live build: `git log --grep=Gov-Transition:` prints nothing.
- `derive_landed_owners` reads aNimbleMend, dFoldedAudit, dGroundRules and dOrderedCharter as landed. dWellOiledMachine and dDeclaredLoop are not landed.
- Units 52 and 53 changed no `[[item]]` row.
- `VERB_OFFENDER_PIN` reads 1215 PINNED, and all ten new names in the spec's inventory pass `lexicon.py --suggest <name> --as py.function`.

Those probes and the lexicon's suggest verb stand in for no gate, suite or bar: none ran.

The divergence probes:
- `check_program` over gov's rows plus adapt.py's lint-pass plant row raised "carries no outcomes".
- `read_composition` with `{"exclude": "item.test.flakes"}` exited 0, and `check_program` over the result raised "item.test.route routes nondeterministic to 'item.test.flakes', which is no declared item".
- `design_lib.derive_clause_hash` over the as-built view's row for `cl-dClosedLoop-0118` printed 4c8ef789.

Owed when the unit is dispatched again:
- The F7 `amends` record and the matching Carries re-pin belong to the spec writer's revision.
- The sweep's rows for `write_transition` and the pending list need re-deriving once the spec says how the adapt plants and a build's view of gov's pending list are graded.
- The `New arm:` observations for AC1 to AC5, AC7 to AC9 and AC11 stay with the main loop at the close.
