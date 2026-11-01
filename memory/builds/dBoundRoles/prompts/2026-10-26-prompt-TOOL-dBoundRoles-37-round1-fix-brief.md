**Serves:** research TOOL-dBoundRoles-37 TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43

# Round-1 fix brief — dBoundRoles, the promoted specs' reds before their commit

The round-1 spec audit (`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`)
promoted its findings into TOOL-dBoundRoles-37 to -43, authored by the harness's disposal stage and not yet
committed. `python tools/check-spec-tokens.py` and `bash tools/memory-tree/check-memory-hygiene.sh` then printed the
reds below on those specs. Fix each in the spec it names and nothing else; every spec stays `rev-1`, since none is
committed yet. The spec brief `memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md`
still binds.

## R1 · suites inside acceptance criteria (spec-tokens `[bar]`)

TOOL-dBoundRoles-37, -40, -42 and -43 each name `tools/govkit/selftest.py` inside a criterion. A criterion observes
the unit's own checker on a staged break, a `--selftest` flag of the unit's own tool or a fixture, never a suite:
rewrite each to observe the checker or fixture directly, and move the suite to a `New arm:` line in §7.

## R2 · retirements with no Readers clause (hygiene check 25)

TOOL-dBoundRoles-42 §2 S5 and TOOL-dBoundRoles-43 §2 S5, S10, S25, S27, S28, S38 and S41 retire a named thing and
carry no `**Readers:**` clause. Write each one: `**Readers:**`, then `by name:` and every reader spelling the name,
then `by value:` and the readers of its value, or `NO VALUE READERS` and a reason, each found by `git grep` over the
tree.

## R3 · TOOL-dBoundRoles-43 is over the spec ceiling (spec-tokens `[size]`)

It is 60120 bytes against a ceiling of 49152. It is the round's minors batch, and BUILD-METHOD M4 admits TWO batch
units only when the minors split into two disjoint write sets that can build concurrently. Measure first:

- If its scope items split into two groups whose Files touched do not intersect, split it: keep TOOL-dBoundRoles-43
  for the first group and author TOOL-dBoundRoles-44 for the second, at the next `order` value after 43's, with the
  same status header shape, its own §6, §7 and §10, and the finding ids it takes named in its §1. Each stays under
  49152 bytes. Name the split, the two write sets and the evidence they are disjoint in your return, so the main
  loop records the `--rescope` row.
- If they do not split disjointly, keep one spec and bring it under the ceiling by cutting what the clause and the
  findings do not need: restated design-source prose, duplicated citations, long examples. Never drop a finding.

## Return

The files you changed or created, one line each with the R-items taken; for R3, which branch you took and why. Commit
nothing, and run the build-index generator only in a throwaway clone. You may run
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` there with every dBoundRoles spec committed.
