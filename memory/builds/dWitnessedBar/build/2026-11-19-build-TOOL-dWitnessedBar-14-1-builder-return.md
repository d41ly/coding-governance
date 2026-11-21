**Serves:** journal TOOL-dWitnessedBar-14

# TOOL-dWitnessedBar-14 — builder return 1 (run `wf_13be9fe3-afa`), a divergence, nothing committed

## Why

DIVERGENCE: rev-9 cannot be built as written. Every finding from the pre-build probe of the spec at dabb1aa23 is listed here, in one report.

(1) §2 S3, the §4 "The pack" line saying a leg with no base reads `unresolved` and is never green, and §4 "Rollout" ("Live at landing ... never gains grades conf-scalar-pins alone") cannot both hold.
- `conf-scalar-pins` is the first `[[ledger]]` registration, and this pass is what adds its home.
- `resolve_compare_base` in this worktree answers 9e21ac760dc0, the merge-base of HEAD and origin/main. `git cat-file -e 9e21ac760dc0:memory/project/conf-scalar-pins.txt` exits 128.
- `tools/lib/legacy_ledger.py#compare_to_base` therefore returns (None, "no <home> at <sha>") for that population.
- Under the spec, that makes `ratchet (never gains)` and `ratchet (seed laundering)` print `unresolved` and go red, at the close and at the push boundary, until the push lands the home. The bar cannot be green before the push, and the push needs a green bar.
- The spec has to say how a population whose registration and home are new on the branch is graded against a base that holds neither. One option: it is printed `new at <base>` and held only by its own leg and `both ways`. The other is to state that it reds.

(2) §2 S8 and AC4 depend on a unit built after this one.
- S8 says `populated` reads `unarmed` until the leg's registration has a seen-red record (I16).
- That record's grammar and reader belong to TOOL-dWitnessedBar-7, which is DEFERRED at order 26, after this unit's order 9. §3 lists it as a non-goal. No seen-red reader exists in tools/ (the only hits are tools/loop/loop.toml rows).
- So AC4's `--plant populated-empty-armed` (populated exits 1) can only be observed if this unit writes its own parser of unit 7's I16 line. That breaks §3 and the ordering axis of M2's cross-read.
- The spec has to say what arms `populated` before unit 7 lands, or move AC4's populated half to unit 7.

(3) §2 S6 and §5 disagree.
- At landing the only registration names `ratchet (keys, not a scalar)`, so `ratchet (both ways)` has no population of its own. It prints that one registration as `graded by` and would read green over an empty population.
- That goes against §5 ("an empty population reads unarmed") and practice.gate. The spec has to say what `both ways` prints and exits with no registration of its own.

(4) §4 Inventory's naming cell `--as cli.flag` does not exist. `tools/lexicon/lexicon.py --suggest <verb> --as cli.flag` refuses with: "unknown surface 'flag' in 'cli.flag'; the closed set is function type file constant". §4 has to name a cell that exists, or drop the verb-naming step, since the verbs are already fixed by the Inventory.

(5) §4 Files touched is missing paths the change needs.
- `memory/guides/SESSION-KICKOFF.md` needs a re-stamp, because its `watch:` list holds `tools/gate-legs.json` and `.memory-tree.conf`, both of which this unit edits. The main loop's dispatch already declares it.
- The dispatch also declares `.lexicon.conf`, which the spec does not list.
- In the other direction, the dispatch omits `.memory-tree.conf` (PROJECT_REGISTRY_EXTRA has to name conf-scalar-pins.txt) and `.gitattributes`, which the spec does list. A re-dispatch should declare both.

Nothing was written or committed.

## Summary

I built nothing: the probe of rev-9 against the tree found two problems a build cannot work around and three smaller defects. All five are listed in `why`. The worktree is clean at base dabb1aa23d29720bdad63e7c886b9030fddcef6a.

- **Brief:** the `--brief` verb answered "already recorded, unchanged" at d10430e4a002, so nothing changed.
- **Spec claims that held against source:**
  - The nine `*_PIN=` assignments, at 1 each; two of them empty.
  - `retrofit.widen` in `tools/policy/catalogue.toml`.
  - `read_policy_value` in `tools/memory-tree/tree_lib.py`.
  - `TYPED_RECORD_KINDS`, plus `KINDS`, `DOORS` and `write_record` in `tools/memory-tree/build_records.py`.
  - The HYGIENE count "The nine after `research`" at line 662 of the template and of `memory/HYGIENE.md`.
  - The `legacy_ledger` block functions, including `run_seed_argv` and `read_home_state`, present in both copies.
  - `leg_factory.py`'s `new` verb (it has no `--pack` flag, so `pack` would go into `kit.toml` by hand), `derive_leg_tag`, and `pack` in `LEG_KEYS`.
  - 6 legs (DERIVED) carrying `"pack": "tags"`.
  - No `[[ledger]]` table tracked anywhere.
  - The `[claims] gate-legs` list in `memory/map/features/memory-tree-hygiene.md`.
  - `owed_rows.py` exists.
- **Policy probe:** a scratch fixture (under %TEMP%/rk1, since removed) confirmed that `policy.py get retrofit.widen` reads `record-reason` by default. With `[retrofit] widen = "refuse"` committed at a remote-tracking ref, it reads `refuse`. So S13's base setup works as described.
- **Lexicon:** the function names I planned all pass `lexicon.py --suggest --as py.function`.
- **Checks run:** none, and none stood in for any gate; this pass committed nothing. The gotchas checklist (`gotchas.py --for-diff`) did not run, because there was no commit for it to read. Every §6 criterion (AC1 to AC11) and the `New arm:` line for `tools/memory-tree/ratchet.py` (`ratchet selftest`, RED on `gain`, `gain-refused`, `laundering`, `rename`) are still owed, for a rebuild after the spec is revised.
- **Commands skipped for timeout:** none.
