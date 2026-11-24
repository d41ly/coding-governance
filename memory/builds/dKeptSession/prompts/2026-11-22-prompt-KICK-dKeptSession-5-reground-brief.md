**Serves:** research KICK-dKeptSession-5

# Brief — dKeptSession: KICK-dKeptSession-5 re-grounded on the landed tree

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-5, the per-build mailbox, was grounded at c2a407b0 and touches more files than any unit left: the
unattended driver and its suite, the verbs guide and its template, the loop kit, the memory-tree kit, the kickoff engine
and its fixture, and two help pages. Since then origin/main 8b8b1374 was reconciled into the run branch
(KICK-dKeptSession-69), and KICK-dKeptSession-37, -38, -26, -15, -14, -30, -9 and -28 landed in those same files.
KICK-dKeptSession-22 and -31, both on the mail id, land just before this unit: read their specs as what lands first.
Several builders in this run stopped before editing because their specs missed a shipped text the change made false or
a claim about code that had moved. Re-ground this spec on the tree at its current HEAD so its builder does not stop the
same way.

### Items

1. F-claims: probe every claim the spec makes about current code (function and verb names, signatures, row columns,
   return codes, refusal texts, `manifest-check.sh`'s `POINTER_LINES` and the replay's line order, the suites' floors:
   the unattended suite's `FLOOR_ASSERTIONS` is 4072 and the manifest-check suite's is 438 at this HEAD) against the tree,
   with KICK-dKeptSession-22's and -31's specs read as landed, and correct any that moved.
2. F-texts: grep every shipped text that states what this unit changes (the verbs guide and its template, the protocol
   guides, `help/loop.md`, `help/orientation-card.md`, kit READMEs, `tools/policy/catalogue.toml` summaries, comments in
   other files). For each text the clauses would make false, add a clause or extend one that rewrites it and list its
   path in Files touched; a text left as it is gets one sentence saying why it stays true. A catalogue summary edit moves
   the policy mirror `.governance/policy.json` (re-written by `python tools/policy/policy.py mirror --write`), and a help
   page anchor carries a docs fingerprint taken from `python tools/govkit/docs_leg.py --fingerprints` at build time.
3. F-ceiling: `tools/unattended/unattended.sh`'s refusal sites sit at their harness-arms ceiling (347/347). If the spec
   adds a `fail`, `exit 1` or `status=1` site, say so and name how the ceiling is met (reuse of an existing site, or the
   ceiling's recorded decision); otherwise say the spec adds none.
4. F-arms: `skills/session-kickoff/manifest-check.test.sh`'s exact replay-order arms already miss the `position —` and
   `context —` lines KICK-dKeptSession-15 and -14 added; if this unit adds a replay line, name the arm it re-arms.
5. Bump the spec one rev, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`, pin
   every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep within
   the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-5` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-5's (other writers are revising
other specs at the same time; read them, never edit them). Read files; edit only the spec, in the run worktree.
