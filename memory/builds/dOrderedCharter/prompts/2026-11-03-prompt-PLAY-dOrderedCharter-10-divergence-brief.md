**Serves:** research PLAY-dOrderedCharter-10

# Brief: unit 10's divergence — the `kit` namespace against unit 19's built tag checks

## The prompt

> dOrderedCharter

— owner, 2026-11-02, invoking `/unattended` for the build run. Unit 10's builder (run wf_3907208d-a9f) returned
`DIVERGENCE:` before writing code. Registering spec 10's eight namespaces as written turns unit 19's built `tags` leg
red: (1) `kit.toml` is a backticked span 43 times in tracked Markdown outside `memory/builds/` (`WIRE-INTO-PROJECT.md`,
`help/roles.md`, `help/step-gate.md`, `help/upgrade-steps.md`, `tools/*/README.md`, `memory/gotchas/*`,
`memory/map/features/*`), and `SPAN_RE` reads each as a citation into `kit`, which `check_resolves`
(`tools/playbook/tag_index.py:568`) and S4's cited-but-undeclared join both red; (2) every row sits in
`layer.instruction`, a core layer, and the `kit` extractor mints `kit.<id>` at each descriptor's own path, so
`check_owned` (`tag_index.py:646`) reds the eight non-core kits (codebase-map, lexicon, memory-recall, gate-lint,
pytest-parallel-guardrails, branch-reconcile, drift-audit, runlog).

## The brief

### Goal

Revise spec 10 so registering its namespaces leaves unit 19's `tags` leg green over the tree, and every namespace still
joins both ways.

### Items

1. **The `kit.toml` collision.** Decide by M3 between at least: a namespace name that no file name shares; a rule,
   stated in spec 10 and consistent with unit 19's built `SPAN_RE` and `_derive_span_ns`, that excludes a
   file-name-shaped span (a known extension after the namespace) from the citation population; or another mechanism
   you find. Record the loser and the observation that rejected it (M12) in §8, delegated. A choice that edits unit
   19's code is in this unit's Files touched, never a reopening of spec 19.
2. **`owned` against non-core kits.** Say for the `kit` row (and any other namespace whose tags are minted inside a
   non-core kit's tree) either which core-held source mints them, or that the row takes a layer `check_owned` admits,
   or how `owned` treats it; measure the choice over the tree with unit 19's own functions.
3. **The member count.** §4 pins `kit` at 29 members; HEAD holds 18 `tools/*/kit.toml` descriptors and 12
   `tools/govkit/entries/*.kit.toml` files declaring 15 ids. Say which population "each descriptor's id" means and
   derive the count at the pass, never pin it.
4. **Migration and Rollout.** Re-state what the shape check's first run grades, with the count left red over the tree
   (it must be 0) written into §6 from a probe of unit 19's functions.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-03, the status kept `DEFERRED`, and add one §9 line naming this brief.
- Run the spec-token reading on your own revision's §6 and §7 by eye against `tools/check-spec-tokens.py`'s `BAR`
  pattern: no AC observes a suite, a bar or `gov_tag.py check` over the tree.
- Verify every path, count and line you cite against the tree at HEAD; stay under the 47000-byte authored budget.

For the run:

- Writes stay in spec 10 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question: a fork no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return the new rev, the §8 decisions with their losers, and the red count item 4 measures.

### Acceptance

- Spec 10's §6 carries item 4's measured red count, and it is 0.
- The Status line is one rev higher, and §9 holds the new line.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no spec but 10; spec 19 stays frozen.

### Limitations

The items above, "For the run".

### Reuse

`tools/playbook/tag_index.py` (`SPAN_RE`, `_derive_span_ns`, `check_resolves`, `check_owned`) as unit 19 built it
(`9cb93347d`); `tools/playbook/namespaces.toml`.
