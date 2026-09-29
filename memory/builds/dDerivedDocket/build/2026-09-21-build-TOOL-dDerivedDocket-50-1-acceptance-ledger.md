# TOOL-dDerivedDocket-50 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-50

The kit's one public route to the anchor grammar, its two named refusals, the target-root mapping,
and the example-conf parity arm over the kit's Python modules. AC1, AC2, AC3, AC4 and AC9 each carry
a `permission:` line putting their observation on a held `chunk = selftests` leg, so they get no
line here and the orchestrator writes them after the VERIFYING bar. Every arm behind those five was
still observed RED by hand in this pass, against a staged break in a COPY of the two kits inside a
scratch git repository: the route bound to the kit's own repo instead of the given root, a second
bundle-to-answer call site, a `walk()` reaching the route with no bundle, the route inheriting
`grammar()`'s pin cause and pin cure, only the first refusal point re-caused, and the sibling kit's
`ConfError` left to escape. The parity block was staged RED four ways too: the shipped example as it
stood at the parent commit, the receiver narrowed back to `conf`, the empty-derivation refusal
deleted, and the exemption's second direction deleted. No merge bar, no gate leg and no `*.test.sh`
suite was run.

**Evidences:** TOOL-dDerivedDocket-50
- AC1 — `corpus-ids selftest` — at 364278a8 the leg,
  `python3 tools/memory-tree/corpus_ids.py --selftest`, prints `PASS — corpus_ids: all arms held`,
  exit 0, and its arm answering the GIVEN root's own id on a heading and a table row, and `None` on
  a citation, through `resolve_anchor` reads ok.
- AC2 — `corpus_ids.py --selftest` — as the `corpus-ids selftest` leg at 364278a8 its call-graph
  arm reads ok: `anchor_at` named once, `_anchor`'s only caller the route, and `walk()` resolving
  one bundle and handing it over. Its expected answer, in the module's source at that commit, is
  `anchor_at=1 _anchor callers=['resolve_anchor'] grammar( in walk=1 route args in walk=[2]`,
  counting `anchor_at` reached through any expression.
- AC3 — `GRAMMAR_DIR` — as the `corpus-ids selftest` leg at 364278a8 all six refusal arms read ok,
  over a `GRAMMAR_DIR` holding no `extract.py` and over one whose `extract.py` has no `grammar_for`:
  in each the anchor route's refusal states its own cause and its install or update cure and names
  neither pin, and `grammar()`'s own refusal keeps the pin cause and the parent's cure verbatim.
- AC4 — `memory-hygiene self-test` — at 364278a8 the leg prints `PASS (521 assertions)` against
  that commit's floor of 516, exit 0, with no `FAIL` line. At that commit the python example-conf
  block prints a `FAIL` line on each miss: a derivation naming no key, one missing `MEMORY_ROOT` or
  `ROTATION_MODE`, a fixture read through `conf` not redding, and `ucfg["RECALL_CLI"]` not redding.
- AC5 — amended rev-2 — `FLOOR_ASSERTIONS` — the criterion's exemption clause named only the
  `os.environ` reads; re-measured on this tree the unconstrained receiver also pulls in two module
  constants reached through `globals()` and one fixture view key, so the clause is widened and §9's
  rev-2 entry logs it with the rest of the corrected measurement. Observed as amended: the block's
  own `sed`/`grep` derivation, sliced out of the suite by marker and executed STANDALONE over
  `tools/memory-tree/*.py`, yields twenty-four names; every one is declared in
  `tools/memory-tree/.memory-tree.conf.example` or named on the exemption list, and every one of the
  ten exemptions names a key some module still reads. Nine assertions, no finding. The floor reads
  416 at the parent with `git show` and 425 here, which is higher; the equality against the suite's
  own PASS line is the half its `permission:` line defers to the VERIFYING bar.
- AC6 — `ARMS_FLOORS` — declared in `tools/memory-tree/.memory-tree.conf.example` and blank, with a
  comment naming its reader by basename. The leg that reads it, run over a scratch git tree whose
  conf declares it blank, exits 0. The same tree with `ARMS_FLOORS="tools/gate-gone.sh:9:9"` exits 1
  naming that path, so exit 0 is the blank value turning the floors off rather than a leg that
  cannot red.
- AC7 — `resolve_anchor` — in `TOOL-dDerivedDocket-15`'s spec at this commit, the retired conf key
  occurs exactly once and inside §9, which is the rev entry that records its removal; AC13's
  `fixture:` line names `corpus_ids.resolve_anchor(root)`; §10 names that route once; and §9 carries
  a rev-6 entry whose scope names AC13. The paragraph parking H2 left with the key, and H3's
  hand-off is untouched.
- AC8 — `memory/map/generated/symbols.json` — regenerated with `gen_map.py --write` and staged in
  the same commit as the `.py`. `resolve_anchor` appears in it; `_check_grammar_installed` does not,
  and the artifact carries no leading-underscore Python function at all, re-measured here. The
  dossier `memory/map/features/memory-tree-hygiene.md` now describes the project-key block as three
  example-conf parity arms and states what the unconstrained receiver buys.
- AC9 — `resolve_anchor` — as the `corpus-ids selftest` leg at 364278a8 all six target-root arms
  read ok: over a root with no `.memory-tree.conf`, one declaring no `MEMORY_ROOT` and one declaring
  no usable `FAMILIES`, each call raises this kit's `Problem` naming the root, and each refusal
  names which declaration was missing. A `ConfError` reaching the caller fails those arms by
  construction.
