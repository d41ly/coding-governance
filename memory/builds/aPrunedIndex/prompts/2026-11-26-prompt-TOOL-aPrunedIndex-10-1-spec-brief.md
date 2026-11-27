# Spec brief — TOOL-aPrunedIndex-10: the closing review's four lows, batched

**Serves:** research TOOL-aPrunedIndex-10 TOOL-aPrunedIndex-4

## The prompt

> Fix lows first

The owner's answer in the building session, 2026-11-26, to "Land aPrunedIndex now, with the four low findings as a
follow-up unit, or fix them first?". `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` promotes a DIFF exit's lows into ONE unit naming them all; this is
that unit. The findings are L1 to L4 of
`memory/builds/aPrunedIndex/reviews/2026-11-26-review-TOOL-aPrunedIndex-1-2-3-4-diff-review-round1.md`; read them whole.

## The brief

- **L1 (id 3).** Reword the `tools/playbook/README.md` sentence that says the release sweep costs "one seek per released
  pair" so it states the ceiling the code's own ponytail comment states: one seek per pair against the trees, plus a
  scan of `dirty_path` for each pair no tree holds. Do NOT add the `dirty_path(blob)` index.
- **L2 (id 5).** Replace the lambda-bound `commit_texts` in `tools/playbook/gov_tag.py` with a nested `def` whose name
  leads with a `.lexicon.conf` VERBS word (`write_*` fits), and rename its call sites. The class-level gate (lexicon's
  `_python_defs` grading lambda-bound names) is out: a probe over the tree on 2026-11-26 found 54 lambda-bound names in
  tracked Python, most of which the gate would refuse, in files across several kits. It is filed as an ask instead.
- **L3 (id 6).** Add two steps to the `gc-predates` plant in `tools/playbook/gov_tag.py`, each with a worktree whose HEAD
  `git ls-tree` cannot read. Step A has its registry absent on disk, so the registry probe's `read_git` fails. Step B has
  the registry present and the conf absent on disk, so the conf probe's `read_git` fails. Both assert that `--gc` refuses
  and names the worktree, and that the row counts do not change. Each is a `New arm:` that is seen red under a staged
  `except TagError: skip` around its probe. Finding 2 of the review recorded that `ls-tree` exits 128 on the all-zero sha of
  an orphan worktree. That may serve as the unreadable HEAD; verify it yourself.
- **L4 (id 8).** Make no spec edit: spec 4 is CLOSED and frozen. This invocation's audit covers TOOL-aPrunedIndex-4 at
  rev-4 beside this unit, and that audit clears the build index's `moved past its audited revision` line.
- **Also in this unit:** two ask rows in `memory/builds/aPrunedIndex/BACKLOG.md`, one per review left-shift that no fix
  here gates, each with a KEEP row "awaiting the owner" like asks 5 to 9.
  - `naming-leg-grades-what-python-named`: lexicon grades lambda-bound names.
  - `closed-over-an-unaudited-spec-revision`: the build index refuses CLOSED over an id moved past its audited revision.
  - L1's class `observed-by-claim-no-arm-discharges` is not asked again: the reword states a ceiling, which is its cure.
  - L3's class `rule-stated-with-no-check-that-fails` is already ask 5.

## Cut-line

- No edit to `tools/playbook/tag_index.py`, nor to any other module in its import closure. On 2026-11-26
  `import_walk.derive_module_closure` printed that closure as:
  - `backlog`, `coverage_join`, `design_lib`, `id_grammar`, `import_walk`, `legacy_ledger`, `policy_value`, `tag_index`,
    `tree_lib`.
  - Every edit there is a new version of the `tag_index:*` extractors. Each node then pays a full re-parse at its next
    check, measured at 441 s on node a. (PINNED, 2026-11-26)
- `gov_tag.py` is in `instruction_units`' closure, beside `routed_commits.py`, which other sessions are landing. An edit
  to it therefore re-versions only the `instruction_units:*` extractors, and those already re-version at every such
  landing. That cost is accepted here. The main loop measures it at the close on the private copy.
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py` stay untouched.
- No ceiling or budget moves. If the two new steps lengthen `gc-predates` enough to matter, re-time the
  `tags bundle selftest` row (unit 4's AC8 method) and say so; do not move it otherwise.
- Tier: 1. Prose, a test-only rename and two plant steps; no write path changes.
