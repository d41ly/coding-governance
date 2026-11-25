**Serves:** journal TOOL-dTotalRecall-115
**Caused-by:** TOOL-dTotalRecall-114

# Brief — dTotalRecall: TOOL-dTotalRecall-115 to -121, the closing review's promoted findings

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Write seven specs (PINNED 2026-11-25, this brief's list), one per unit below, from the closing review's report
`memory/builds/dTotalRecall/reviews/2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md`, each Tier-2,
each `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-<n>.md`, so one builder pass closes each.

- TOOL-dTotalRecall-115, order 43: H1, the change feed's record walk and its check (findings 4, 8, 19).
- TOOL-dTotalRecall-116, order 44: H2, `read_section` with a blob (findings 2, 6).
- TOOL-dTotalRecall-117, order 45: H3, the record door's `exists` key (finding 5).
- TOOL-dTotalRecall-118, order 46: H4, the memory re-measure's root-wide search (finding 9).
- TOOL-dTotalRecall-119, order 47: H5, the orphan walk's claim root (finding 12).
- TOOL-dTotalRecall-120, order 48: H6, the causes leg over an empty population (finding 17).
- TOOL-dTotalRecall-121, order 49: the minors batch, M1 to M10 and L1, one scope item each.

### Items

1. Read the report whole. Each spec's scope is its item's Where, Consequence, Fix and Left-shift gate; build the fix the
   report names as class-level or SOUND, never an INSTANCE-ONLY one. Ground every claim in source at HEAD first: where
   the report is wrong about the code, say so in the spec and scope what holds.
2. Every item ends in an arm seen red on today's code, declared on a `New arm:` line, or in a gotcha class where no arm
   fits. The two `new:` classes the report's dispositions name are authored by TOOL-dTotalRecall-117 and -119 in
   `memory/gotchas/`, `<MEMORY_ROOT>/gotchas/INDEX.md` regenerated.
3. Scaffold each through the door, `python tools/memory-tree/gov_record.py new spec <id> --tier 2 --order <n>`, and rename
   each to the path above where the door dates it otherwise. The shape to follow is
   `2026-10-26-spec-TOOL-dTotalRecall-114.md`, its binding line included (its F1).
4. A carried block a spec moves names every carrier in its files touched, and a shipped kit's suite arm raises its
   suite's declared floor or count where one exists. A spec whose edit moves a `shell-role` row, a fork row, a manifest
   row or `SESSION-KICKOFF.md`'s stamp says so: the close's bar grades them (the reds record
   `2026-11-25-build-TOOL-dTotalRecall-100-close-bar-reds` lists what was missed before).
5. The write sets: where two of the seven touch one file, the later order consumes the earlier by an edge.
6. Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall <each id>` and
   `python tools/check-spec-tokens.py --spec <path>` over each, and fix every finding naming them. Every number carries
   an id, a path:line, PINNED or DERIVED on its line, and no code line is cited bare as a file, a colon and a number.

### Acceptance

The commands name no finding of the seven specs (PINNED 2026-11-25, this brief's list); every finding of the report is in
exactly one spec's scope with an acceptance criterion.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

The `d0e02120b` limits red and any history rewrite. The units held on owner asks. A policy key or a bound moved so that a
red passes.

### Limitations

The write grant is the seven spec files alone (PINNED 2026-11-25). The status is `OPEN`, rev-1, base `acbb74bb3`. Temporary files go under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/115/`, spelled absolute. Do not commit.
A command past two minutes runs in the background and is waited for, never polled. An isolated worktree session refuses
an inline command that embeds git: put it in a script file. Run no gate leg: each criterion is a probe the builder can make.

### Reuse

The report's own Fix paragraphs, and each finding's named readers.
