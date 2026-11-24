**Serves:** research KICK-dKeptSession-31

# Brief — dKeptSession: KICK-dKeptSession-31 re-grounded on the landed tree

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-31 was grounded at c2a407b0. Since then origin/main 8b8b1374 was reconciled into the run branch
(KICK-dKeptSession-69), `tools/unattended/unattended.sh` changed a great deal there, and KICK-dKeptSession-28 added
`check_mail_recipient` and `check_mail_addressed` beside `check_fleet_tag`. KICK-dKeptSession-22, which derives each
message's id from what it says, is building now and lands just before this unit: read its spec as what lands first.
Several builders in this run stopped before editing because their specs missed a shipped text the change made false or a
claim about code that had moved. Re-ground this spec on the tree at its current HEAD so its builder does not stop the
same way.

### Items

1. F-claims: probe every claim the spec makes about current code (function names, signatures, return codes, refusal
   texts, the suite's `FLOOR_ASSERTIONS`, which is 4072 at this HEAD, and its shard floors) against the tree, with
   KICK-dKeptSession-22's spec read as landed, and correct any that moved.
2. F-texts: grep every shipped text that states what this unit changes (`memory/guides/UNATTENDED-VERBS.md` and its
   template, the protocol guides, help pages, kit READMEs, comments in other files). For each text S-clauses would make
   false, add a clause or extend one that rewrites it and list its path in Files touched; a text left as it is gets one
   sentence saying why it stays true.
3. F-ceiling: `tools/unattended/unattended.sh`'s refusal sites sit at their harness-arms ceiling (347/347). If the spec
   adds a `fail`, `exit 1` or `status=1` site, say so and name how the ceiling is met (reuse of an existing site, or the
   ceiling's recorded decision); otherwise say the spec adds none.
4. Bump the spec one rev, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`, pin
   every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep within
   the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-31` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-31's (other writers are revising
other specs at the same time; read them, never edit them). Read files; edit only the spec, in the run worktree.
