# TOOL-dPlacedRequest-6 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-6

The unit was built from its spec at rev-4 (PINNED) on base `844063a15`. `tools/loop/loop.toml` declares
`map = "base"` on the ten (DERIVED) items of the spec's declarations table and `unfolds = ["kit",
"policy"]` on `item.design.inventory`. The loop reader gained `tools/loop/loop_lib.py#check_item_maps`,
run by `--check` after the seeds, with the namespace words read from the playbook kit's
`namespaces.toml` through `tools/loop/loop_lib.py#resolve_kit_dir`, and four plants.
`tools/loop/loop_lib.py#read_seed_values` takes the schema row's name, so the `map` value set is the
`widens` order of the item kind's `map` row and is typed nowhere beside it. `help/loop.md` gains the
paragraph on `map` and `unfolds` after the seed section.

No gate, suite or bar ran in this pass. Each criterion below was observed by a probe of the changed
code: `python tools/loop/loop_lib.py --check` over this tree, its own `--fixture --plant` command, or a
`python -c` call of `check_item_maps`.

**Evidences:** TOOL-dPlacedRequest-6
- AC1 — `--check` over the tree exited 0 (PINNED) and printed one `loop: map <tag>` line for each of
  the 67 (DERIVED) items: `map base` on exactly `item.plan.triage-judge`, `item.plan.research`,
  `item.plan.reason`, `item.design.inventory`, `item.design.seams`, `item.design.decompose`,
  `item.design.research`, `item.design.unit-spec`, `item.design.reason` and `item.review.fold`;
  `item.design.inventory`'s line ending `· unfolds kit, policy`; every other line `map none`; then
  `loop: maps · 10 declared · 57 none` (DERIVED) and
  `loop: unfolds · 2 word(s) checked against 15 namespace(s)` (DERIVED). The unit workers,
  `item.build.unit-pass` among them, read `map none`.
- AC2 — `--fixture --plant map-bad` exited 1 (PINNED) with
  `loop: refused · the item item.build.unit-pass map 'full' is not one of none base`.
- AC3 — `--fixture --plant unfold-unregistered` exited 1 (PINNED) with
  `loop: refused · the item item.design.inventory unfolds 'legs', which is no ns of the namespace registry`;
  `--fixture --plant unfold-no-map` exited 1 (PINNED) with
  `loop: refused · the item item.build.unit-pass unfolds kit with map none: nothing renders the nodes it would list`.
- AC4 — `--fixture --plant no-registry`, the same `unfolds = ["legs"]` row with the registry resolved
  from an empty scratch directory, exited 0 (PINNED), printed
  `loop: unfolds · unarmed — no namespace registry resolves` and no refusal; with the registry
  restored, `unfold-unregistered` above is the same row and exits 1 naming `legs`.
  TOOL-dDeclaredLoop-12 AC7's `scope-no-kit` plant now also resolves the registry from its kitless
  scratch directory, printed the same `unarmed` line and still exited 0 (PINNED). The item listing
  still shows the row's declared `unfolds legs`: the criterion's "names no unfold word" is read as
  S3's "checks no unfold word", the listing being the declaration and no verdict.
- AC5 — `grep -n "unfolds" loop.md` in `help/` finds the new paragraph, which names `map`'s values
  `none` and `base` and says an unfold lists the namespace words whose nodes the map slot spells out.
- Other answers, by probe: `check_item_maps` called on an `unfolds` that is a string or holds a
  non-string refused each naming the item as no list of namespace words, and a `map` that is a list
  was refused as outside the values; with `namespaces` None a row unfolding `nope` drew no refusal and
  the `unarmed` line. The `conf-readers-declared` plant still held, exit 0 (PINNED).

**The checklist, acted on.** The bug-class checklist over the pass commit `5770e6f85` selected 29
classes (DERIVED: 23 by an anchor and 6 universal). Two needed a change.
rule-stated-with-no-check-that-fails: two refusal branches had no arm, so `unfold-not-list` sets
`item.design.inventory`'s `unfolds` to the string `kit` and exited 1 (PINNED) naming the item, and
`registry-bad` resolves the registry from a scratch directory whose `namespaces.toml` is no TOML and
exited 1 (PINNED) naming the registry; the registry's read failures now share one refusal, as the
lexicon's `tools/lexicon/lexicon.py#read_tag_words` does. ledger-token-wrapped-across-a-line-joins-nothing:
this ledger's quoted refusal lines were wrapped mid-token and are now one line each. The rest named
nothing in this diff: each plant triggers the arm it is owed, never a vacuous pass; the rows were
inserted after their own unique `tag` lines and `--check` lists exactly the ten (DERIVED); the help
text opens no fence; the map's value set is read from the schema, never typed beside it. Not driven by
any arm: the schema missing its `map` row, the `LoopError` branch the seeds' check shares.

**Note on the spec's actor column.** The declarations table gives `item.design.reason` the architect;
the tree's row carries `role:gov-spec-writer`. The declaration is by item, never by actor, so the build
is unaffected; the column is the delivery table's reading, not the row's.

**Owed at the close.** The `New arm:` line of section 7: the `map-bad`, `unfold-unregistered`,
`unfold-no-map` and `no-registry` plants under `--selftest`, each owed the exit and line `PLANT_OWED`
declares beside it, RED-first on `unfold-unregistered`'s staged break; the checklist's
`unfold-not-list` and `registry-bad` plants ride the same `loop definition fixtures` leg. The
`loop definition` leg, the `loop item kind` leg over the changed rows, the docs leg, the spec-token
leg, the codebase-map leg and the recall floor legs are the close's.
