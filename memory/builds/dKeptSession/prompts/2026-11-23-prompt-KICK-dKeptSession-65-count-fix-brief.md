**Serves:** research KICK-dKeptSession-65

# Brief — dKeptSession: KICK-dKeptSession-65's count of unit 61's loop-kit paths

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-61 rev-10 dropped `tools/loop/placement.py` from its Files touched: its plant now uses the `parent`
keyword and sha return KICK-dKeptSession-53 rev-9 S7 lands, and no longer edits the helper. This spec's S10 and AC6 still
speak of "unit 61's three loop-kit paths" and list `tools/loop/placement.py` among them. Everything else 63 rev-5, 64
rev-5 and 65 rely on in 61 (S1's `sent` under `local`, S2's signature, S3's ledger answer, the plant, `sent=True`) is
unchanged in 61 rev-10. This spec was re-grounded at rev-3; revise only what the items below name.

### Items

1. F-count: correct S10 and AC6 to unit 61 rev-10's loop-kit paths, probed from its Files touched, with the count pinned
   DERIVED; say whether the fixture stub at `tools/loop/placement.py` is still needed and keep or drop it accordingly.
   Where this spec cites "61 rev-9", cite 61 without a stale rev.
2. Bump the spec one rev, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`, pin
   every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep within
   the live-spec size cap, leave no fork open, and leave no bare `path:line` citation.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-65` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-65's. Read files; edit only the
spec, in the run worktree.
