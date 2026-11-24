**Serves:** research KICK-dKeptSession-53

# Brief — dKeptSession: KICK-dKeptSession-53's `acks-later-key` plant, made buildable

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-61's re-ground (rev-9) found that this spec's `acks-later-key` plant puts message `c` on ref `s2`,
which already holds `b`, through `tools/loop/placement.py#write_fixture_gov_ref`. As that helper stands at HEAD it
pushes a parentless commit, so git rejects the second push to `s2` as non-fast-forward and the plant cannot be built.
KICK-dKeptSession-61 adds `parent=None` to the helper, but it builds after this unit, so this spec needs its own fix.
Every other claim in this spec was re-grounded at rev-8. Revise the spec to the main loop's rulings below.

### Items

1. F-plant: resolved by the main loop: this unit makes the plant buildable itself, and does not wait on
   KICK-dKeptSession-61. Probe the helper at HEAD and pick the smallest change that lets a plant put a second message on
   a ref that already holds one: either the `parent=` keyword KICK-dKeptSession-61 rev-9 S-clauses describe, added here
   (then say in §4 that KICK-dKeptSession-61 finds it landed, and that its spec is re-grounded at its turn), or placing `c`
   on a ref of its own if the plant's assertion still holds that way. Say which, and why, in one sentence. If the helper
   changes, add `tools/loop/placement.py` to Files touched tied to the clause, list the texts it makes false, and name
   the legs it moves in §7.
2. F-columns: KICK-dKeptSession-24 (merged at `84b64ab7e`) made `read_mailbox` print 16 columns, adding `deadline` and
   `default` as columns 15 and 16, and left the comment above `MAIL_COLUMNS` naming only the later columns 12 to 14. This
   spec's S-clause that rewrites that comment names all five later columns.
3. Bump the spec one rev, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`, pin
   every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep within
   the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-53` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-53's (other writers may be revising
other specs at the same time; read them, never edit them). Read files; edit only the spec, in the run worktree.
