**Serves:** research KICK-dKeptSession-48

# Brief — dKeptSession: KICK-dKeptSession-48 re-grounded on the landed runlog context surface

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-48 was grounded at c2a407b0. Since then KICK-dKeptSession-14, -30, -45 and -46 landed the runlog
kit's context surface, and four consecutive builders of that chain stopped before editing because their specs missed a
shipped text the change made false, most often the `context` paragraph of `tools/runlog/README.md`. KICK-dKeptSession-47,
built just before this unit, now also rewrites that paragraph's compaction clause to count only compactions whose
newest earlier main usage is on the same model. Re-ground this spec on the tree at its current HEAD, with 47's rev-6 read
as what lands first, so its builder does not stop the same way.

### Items

1. F-texts: grep every shipped text that states what this unit changes (the window source, the harness variable
   `CLAUDE_CODE_MAX_CONTEXT_TOKENS`, the mixed-window limit): `tools/runlog/README.md`, the docstrings in
   `tools/runlog/extract.py` and `tools/runlog/runlog.py`, `tools/policy/catalogue.toml`'s context summaries,
   `help/orientation-card.md`, and anything under `skills/`. For each text S1 to S3 would make false or leave
   incomplete, add a clause or extend one that rewrites it, list its path in Files touched tied to that clause, and
   correct section 5's user-docs line, which today names only `help/orientation-card.md`. A text left as it is gets one
   sentence saying why it stays true.
2. F-claims: probe every claim the spec makes about current code (names, signatures, return shapes, the selftest's
   `ASSERTION_FLOOR`, which is 1624 at this HEAD) against the tree, and correct any that moved: `derive_context_fill`
   now takes `(ev, *, window=None, root=None)` and requires one of the two, `measure_context_fill` returns
   `(share, tokens, source)`, and `derive_context_window(model, root=None, held=None)` reads its default root through
   `resolve_projects_root`.
3. Bump the spec to rev-6, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`,
   pin every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep
   within the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-48` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-48's (KICK-dKeptSession-47's spec
is being revised by another writer at the same time; read it, never edit it). Read files; edit only the spec, in the run
worktree.
