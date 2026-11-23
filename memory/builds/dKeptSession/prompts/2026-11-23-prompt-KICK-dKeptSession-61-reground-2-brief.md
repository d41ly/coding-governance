**Serves:** research KICK-dKeptSession-61

# Brief — dKeptSession: KICK-dKeptSession-61 re-grounded on what landed since rev-9

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-61 was re-grounded at rev-9 on `bfc0a4e4`. Since then KICK-dKeptSession-24, -10, -25 and -21 merged
(`read_mailbox` prints 16 columns with `deadline` and `default`; `read_mail_rows(local=False)`; `--mail answer`;
`--mail notice` and `read_mailbox`'s `local` mode, at `fcd13aa2d`), and KICK-dKeptSession-53 rev-9 now adds
`tools/loop/placement.py#write_fixture_gov_ref`'s `parent=None` keyword and its sha return, which this spec's S4 also
adds. KICK-dKeptSession-63 rev-5, -64 rev-4 and -65 rev-3 read this spec's rev-9 as landing first. Re-ground it so its
builder does not stop.

### Items

1. F-claims: probe every claim the spec makes about current code against the tree, with KICK-dKeptSession-53 rev-9 read
   as landing first: S4's `parent=` keyword and sha return become an observation of what 53 lands, not a second edit of
   the helper; correct any other claim that moved.
2. F-texts: grep every shipped text that states what this unit changes; for each text the clauses would make false, add
   a clause or extend one and list its path in Files touched; a text left as it is gets one sentence saying why it stays
   true. A help page anchor carries a fingerprint taken at build time.
3. F-ceiling: if the unit edits `tools/unattended/unattended.sh`, say whether it adds a `fail`, `exit 1` or `status=1`
   site and how the 347/347 ceiling is met; name each suite floor it raises (the driver suite's `FLOOR_ASSERTIONS` is 4156
   and `FLOOR_SHARD_8` 1373 at this tree) and each budget row it re-prices. The `loop transition record` leg's 120 s (PINNED
   2026-11-23, tools/gate-legs.json) ceiling stays parked for the owner.
4. Bump the spec one rev, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`, pin
   every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep within
   the live-spec size cap, leave no fork open, and leave no bare `path:line` citation that the positional ledger would
   need a row for.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-61` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-61's (other writers may be revising
other specs at the same time; read them, never edit them). Read files; edit only the spec, in the run worktree.
