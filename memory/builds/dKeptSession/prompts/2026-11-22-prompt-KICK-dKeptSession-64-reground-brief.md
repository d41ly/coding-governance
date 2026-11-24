**Serves:** research KICK-dKeptSession-64

# Brief — dKeptSession: KICK-dKeptSession-64 re-grounded on the landed tree

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-64 was grounded at c2a407b0. Since then origin/main 8b8b1374 was reconciled into the run branch (KICK-dKeptSession-69); KICK-dKeptSession-13 landed the item boundary, KICK-dKeptSession-1 landed `presets.toml` and the reader's preset step, the mail chain landed (KICK-dKeptSession-22, -5, -31, -23), and KICK-dKeptSession-39, -51, -27, -24 (16-column `read_mailbox`), -10 and -25 (the driver suite's `FLOOR_ASSERTIONS` 4137 and `FLOOR_SHARD_8` 1354) landed. KICK-dKeptSession-21, -6, -7, -35, -42, -8 (rev-6), -11 (rev-7), -43, -52, -53 (rev-9), -55, -17 (rev-6), -61 (rev-9), -18 (rev-6), -41 (rev-5), -44 (rev-6), -56 (rev-6), -57 (rev-4) and -62 (rev-5) and -63 land before this unit: read their specs as what lands first. No leg named `loop selftest` exists: name the real leg as KICK-dKeptSession-57 rev-4 S3 does. Several builders in this run stopped before editing because their specs
missed a shipped text the change made false or a claim about code that had moved. Re-ground this spec on the tree at its
current HEAD so its builder does not stop the same way.

### Items

1. F-claims: probe every claim the spec makes about current code (names, signatures, return codes, refusal texts, row
   shapes, suite floors and plant counts) against the tree, with the specs named above read as landed, and correct any
   that moved.
2. F-texts: grep every shipped text that states what this unit changes (guides and their templates, help pages, kit
   READMEs, `tools/policy/catalogue.toml` summaries, comments and docstrings in other files). For each text the clauses
   would make false, add a clause or extend one that rewrites it and list its path in Files touched; a text left as it is
   gets one sentence saying why it stays true. A catalogue summary edit moves the policy mirror `.governance/policy.json`
   (`python tools/policy/policy.py mirror --write`); a help page anchor carries a fingerprint from
   `python tools/govkit/docs_leg.py --fingerprints` taken at build time; a generated file is re-rendered by its generator,
   never hand-edited.
3. F-ceiling: if the unit edits `tools/unattended/unattended.sh`, its refusal sites sit at their harness-arms ceiling
   (347/347): say whether the spec adds a `fail`, `exit 1` or `status=1` site and how the ceiling is met; if it adds a
   suite plant or arm, name the suite's floor it raises and the budget row it re-prices.
4. Bump the spec one rev, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`, pin
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

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-64's (other writers may be revising other specs
at the same time; read them, never edit them). Read files; edit only the spec, in the run worktree.
