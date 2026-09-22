# Build brief — TOOL-aLeakedHandle-1

**Serves:** journal TOOL-aLeakedHandle-1

The pass this brief was handed to builds unit 1 of `aLeakedHandle` at rev-3. The spec is
`memory/builds/aLeakedHandle/spec/2026-09-10-spec-TOOL-aLeakedHandle-1.md` and it is authoritative;
this brief adds only what the spec cannot carry, which is what the two audit rounds already settled
so the pass does not re-litigate them.

## What the pass builds

Both halves, in one unit. The `pass_commit` fix in `tools/unattended/lib-unattended.sh`, and the
scan that gates the CLASS across the tracked shell surface. The spec's section 4 files table is the
write set and it was declared with `--dispatch` before this brief existed.

## What the audit already decided, so the pass does not reopen it

- The process-substitution form is COUNTED and its count PRINTED. It is not in the failing
  population. Section 8 fork A carries the reasoning and a RESOLVED mark.
- The nineteen carried sites are a backlog row, not a drain this unit performs. Fork B.
- The two new leg names are two new `gate-legs` inventory keys, and the map claim is part of this
  unit rather than a follow-up. That was round 1's blocker.
- Both new legs' manifest fields are declared in section 5 in full, and the budget row and descriptor
  blocks those values imply are part of the write set.
- `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` gains a gating clause. It does NOT lose its
  existing coverage sentence, which is true and stays true. Round 1 D5 was exactly the attempt to
  delete it.

## The rules this pass is bound by

- The failing case of every new gate is OBSERVED RED before the unit closes. Stage the break, confirm
  red, unstage. A gate seen only passing is an assertion about nothing.
- Run the candidate predicate over the real tree and report hits AND near-misses. A predicate that
  reds an innocent file is the defect being guarded against.
- The `pass_commit` fix must preserve the `return` semantics the existing comment protects. A piped
  `while` runs in a subshell and breaks the function's return; that is why the heredoc is there. The
  recorded working shape is a redirect to a FILE, then a read of the file.
- Commit at the end of the pass with the unit id in the subject, then run
  `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names before
  anything else.
- Flip the spec's status header in the same commit as the code.

## What the pass must not do

- No ceiling VALUE is re-declared. The raise-or-optimise question is parked with the owner.
- No sibling unit's files. Unit 2 owns `derive-ceilings.py`; unit 3 owns the `report_one` tail.
- No widening of the write set without re-declaring it with `--dispatch` BEFORE the commit.
  Narrowing after the fact is refused, because that is how a write gets hidden.
