**Serves:** research KICK-dKeptSession-24

# Brief — dKeptSession: KICK-dKeptSession-24's divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-24's builder (run `wf_e1f4f854-84e`) stopped before its first edit and returned a DIVERGENCE: S5 makes
an `open` message turn `expired` past its deadline, and an expired message no longer holds the build's moves, so two
shipped texts outside the spec's Files touched become false. The `mail —` bullet of `help/orientation-card.md` says an
open message holds the build's moves until it is answered or acknowledged, and the module docstring of
`tools/loop/claim.py`, in its paragraph on the KICK-dKeptSession-5 guard, says RECORD prints `claim held` until the
message is answered or acknowledged. The spec already amends the same clause in `MailHeld`'s message and in
`tools/loop/README.md`'s `open` row. Every other code claim in the spec held at the builder's base `0e5b281ab`. Revise
the spec to the main loop's rulings below.

### Items

1. F-texts: resolved by the main loop: both texts are corrected in this unit, in the same wording the spec gives
   `MailHeld` ("or past its deadline", or the spec's equivalent), since each becomes false the moment S5 lands. Add both
   to the §4 Shipped texts table under the clause that makes them false, add both paths to Files touched tied to that
   clause, and extend a criterion, or add one, that observes both texts corrected.
2. F-sweep: a repo-wide grep for "answered or acknowledged" also hits `help/loop.md`, which is already in Files touched:
   confirm every occurrence there is either rewritten by a clause or true after S5, and say which in the table.
3. F-legs: say in §7 which legs an edit to `tools/loop/claim.py` and to `help/orientation-card.md` moves (a docstring
   edit to a guarded path, and a help page's prose beside its usage anchors), and add any leg not already listed.
4. Bump the spec one rev, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`, pin
   every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep within
   the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-24` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-24's (other writers may be revising
other specs at the same time; read them, never edit them). Read files; edit only the spec, in the run worktree.
