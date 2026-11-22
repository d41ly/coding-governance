**Serves:** journal TOOL-dWitnessedBar-14

# Brief — dWitnessedBar: TOOL-dWitnessedBar-14 revised over its first builder's divergence

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 14's first builder stopped at a divergence before writing any
code; the spec is revised by its writer before a second dispatch.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so a
builder can build it as written over HEAD.

### Items

1. Read the first builder's return, `build/2026-11-19-build-TOOL-dWitnessedBar-14-1-builder-return.md`, whole, and
   settle all five of its points in one revision:
   - A population whose registration and home are both new on the branch: the compare base (the merge-base with the
     remote default branch) holds neither, so `compare_to_base` answers "no home at the base" and the spec's
     `unresolved` rule reds the pack until the push lands it, while the push needs a green bar. Say how such a
     population is graded against a base that holds neither.
   - `populated` arms on a seen-red record whose grammar and reader belong to TOOL-dWitnessedBar-7, which builds
     later. Say what arms `populated` before unit 7 lands, or move AC4's populated half to unit 7, without this unit
     parsing unit 7's line itself.
   - `both ways` has no registration of its own at landing; say what it prints and exits with over an empty
     population, so it never reads green over nothing.
   - The Inventory's naming cell `--as cli.flag` does not exist in the lexicon's closed set; name a cell that exists
     or drop the step.
   - Files touched gains `memory/guides/SESSION-KICKOFF.md` (its watch list names two files this unit edits) and
     `.lexicon.conf` if the unit moves a pin; `.memory-tree.conf` and `.gitattributes` stay listed.
   Every other claim the builder probed held at `cf254a004`; leave those as they are.
2. Built so far, each landed on this branch: units 26, 27, 48, 49, 13, 50, 15, 12, 61, 22, 47, 19 and 11
   (`0ccc23626`: the gate-leg factory; its `new` verb has no `--pack` flag). Units 16 and 46 are being re-grounded
   beside this revision and read this spec as the contract; their specs are not yours to edit.
3. A choice the revision forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-14` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding either names. Write no numeric
fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0; the spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-14. No product code. No change to Goal or Scope intent beyond what the divergence
forces.

### Limitations

The status header keeps its status. The write grant is
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-14.md` alone.

### Reuse

The spec's §10 seam, re-verified at HEAD.
