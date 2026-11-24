**Serves:** research KICK-dKeptSession-64

# Brief — dKeptSession: KICK-dKeptSession-64's AC18 count, made true

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-65's re-ground (rev-3) found that this spec's AC18, `grep -c -e "git log" -e "rev-list"` over the
`gov_ref_sh` block, prints `1` at the current tree, not the `0` it asserts, because the block's header comment spells
`git log <ref>`. KICK-dKeptSession-65's AC9 drops comment lines before it counts. This spec was re-grounded at rev-4;
revise only what the items below name.

### Items

1. F-count: rewrite AC18 so it counts only code lines of the `gov_ref_sh` block (drop comment lines before counting, in
   the same shape KICK-dKeptSession-65 rev-3 AC9 uses), probe the rewritten command at the current tree, and pin what it
   prints there with DERIVED. If any other criterion of this spec greps that block the same way, fix it the same way.
2. Bump the spec one rev, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`, pin
   every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep within
   the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-64` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-64's (other writers may be revising
other specs at the same time; read them, never edit them). Read files; edit only the spec, in the run worktree.
