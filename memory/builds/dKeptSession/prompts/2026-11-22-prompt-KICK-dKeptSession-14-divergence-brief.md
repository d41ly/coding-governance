**Serves:** research KICK-dKeptSession-14

# Brief — dKeptSession: KICK-dKeptSession-14's divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-14's builder (run `wf_b7427991-64d`) stopped before its first edit and returned a DIVERGENCE: S2 and
AC8 add `summary` and `usage` to the catalogue rows `context.on-full` and `context.threshold` in
`tools/policy/catalogue.toml`, and that moves two generated or listed artifacts the spec's Files touched does not name.
`help/reference/policy.md` is rendered from the catalogue by the playbook kit's
`render_playbook.py#render_reference_page`, and the help-reference-pages leg compares the page with its render, so both
keys leave its `## Not yet summarised` list and the page must be re-rendered in the same commit. And
`memory/project/docs-undocumented.txt` lists `policy:context.on-full` and `policy:context.threshold`; once either key has
an anchor, `tools/govkit/docs_leg.py#read_docs_state` drains its row, so both rows leave the list in the same commit.
KICK-dKeptSession-13 did the same for `card.pointers` beside its catalogue edit. Every other code claim in the spec held
at the builder's base. Revise the spec to the main loop's rulings below.

### Items

1. F-anchor-home: resolved by the main loop: the two `<!-- usage: policy:context.on-full <fp> -->` and
   `context.threshold` anchors go on `help/orientation-card.md`, in S9's paragraph, as `card.pointers`' anchor sits on
   that page, so the reference page renders both keys as documented there. Say so in S9, with the fingerprints taken from
   `python tools/govkit/docs_leg.py --fingerprints` at build time, not typed in the spec.
2. F-files: add to Files touched `help/reference/policy.md` (re-rendered by the playbook kit's renderer in its
   `--reference` mode, never hand-edited) and `memory/project/docs-undocumented.txt` (the two `policy:context.*` rows
   drained), each tied to the clause that moves it, and extend a criterion, or add one, that observes the reference page
   current against its render and the two rows gone.
3. F-stale-page: the builder also found the reference page stale at its base: `card.pointers` still sits under
   `Not yet summarised` although `help/orientation-card.md` anchors it, because the reconcile merge of
   KICK-dKeptSession-69 dropped KICK-dKeptSession-13's re-render. State in the spec that this unit's re-render also
   carries `card.pointers` to its documented section, as an observation, not a new clause.
4. Bump the spec to rev-6, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`,
   pin every figure with DERIVED or PINNED, keep within the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-14` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check and the driver's
`--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-14's. Read files; edit only the
spec, in the run worktree.
