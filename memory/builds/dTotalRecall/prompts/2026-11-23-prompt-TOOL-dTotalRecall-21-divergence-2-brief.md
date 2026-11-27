**Serves:** journal TOOL-dTotalRecall-21
**Caused-by:** TOOL-dTotalRecall-21

# Brief — dTotalRecall: TOOL-dTotalRecall-21's second build pass diverged; fold the spec to rev-5

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The unit's second builder returned a DIVERGENCE at base `3b34ddf02`,
recorded whole in `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-21-2-builder-return.md`.

## The brief

### Goal

Revise the spec in place as a rev-5 bump, with one revision-log line naming this brief and that builder return by their
file stems, so the next builder can build it as written over HEAD.

### Items

1. S4 and §8 F3 name the govkit entry `playbook` as recall's new requirement; that entry
   (`tools/govkit/entries/playbook.kit.toml`) lands no file. The kit that ships `tools/playbook/tag_index.py` is
   `playbook-render` (descriptor `tools/playbook/kit.toml`, home `playbook`). Re-point S4, F3 and its grant line to
   `playbook-render`, re-reading `govkit.py#derive_unsatisfied_requires` for what the edge then demands of a selection.
2. Files touched gains `tools/govkit/selftest.py`, and the gates section's leg line gains `govkit selftest`: once recall
   requires `playbook-render`, the selftest's `apply --kits memory-recall,memory-tree` selections and `pin_target`'s
   `kits = ["memory-recall"]` must add the required closure, or `apply` refuses them. State that change in Scope.
3. State the two advisories the return names: the query path needs a born HEAD (`tag_index.load_view` reads
   `HEAD^{tree}`), so the S4 refusal on a repository with no commit names its own remedy; and AC6's grep over `tools/`
   bars the README's upgrade note from spelling the retired budget key.
4. A §8 resolution mark is exactly `RESOLVED (agent, 2026-11-23, delegated)`: nothing else inside the parentheses (check
   12 strips code spans and refuses the rest); cite the brief after the mark. Keep every other rev-4 decision; cite code
   as `path#symbol` or blob-pinned; every number carries an id, a path:line, PINNED or DERIVED on its line.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-21`,
`python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/writing_practice.py check pinned-facts`, and
fix every finding they name in this spec. The status header keeps `INPROGRESS`; the write grant is the spec file alone;
do not commit.

### Acceptance

The three commands exit 0 or read green; the spec carries rev-5 and one revision-log line naming this brief and the
return.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-21. No product code.
