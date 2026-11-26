**Serves:** journal TOOL-dTotalRecall-124
**Caused-by:** TOOL-dTotalRecall-122

# Brief — dTotalRecall: TOOL-dTotalRecall-124, the closing review's round 3, its promoted high

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Write one spec, `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-124.md`, Tier-2, build order 52, from
`memory/builds/dTotalRecall/reviews/2026-11-26-review-TOOL-dTotalRecall-122-closing-diff-review-round3.md`: its item H1,
tracked paths reaching ctags as `-L -` lines, where ctags reads a leading `-` as an option. The review loop ended at round 2,
so the build method's M4 severity rule promotes the high to a unit of its own.

### Items

1. Read the report whole, the appendix included. The scope is H1's Where, Consequence, Fix and Left-shift gate; build the
   fix the report names as SOUND or the skeptic's corrected or class-level one, never an INSTANCE-ONLY one. Ground every
   claim in `tools/playbook/code_record.py` at HEAD first; where the report is wrong, say so and scope what holds.
2. The fix closes the class, not the instance: every path the code record hands an external tool through a list-file or
   argv input is made unambiguous as a file name. Name every such call site in the file, and any other kit that feeds
   tracked paths to a tool's list input, found by a grep you state.
3. It ends in an arm seen red on today's code, declared on a `New arm:` line naming the break it is red on. ctags is not
   installed on node a (DERIVED 2026-11-26, the review's skeptic), so the arm must run without it: a stub or the argv the
   reader builds, not a live ctags. The `new:` class `path-list-input-read-as-options` is authored in `memory/gotchas/`,
   its feature dossier under `memory/map/features/` claiming it and `INDEX.md` regenerated.
4. Files touched names every carrier, floor, `shell-role` row and generated output the pass moves, the `gen_build_index.py`
   write set among them.
5. Scaffold through the door, `python tools/memory-tree/gov_record.py new spec TOOL-dTotalRecall-124 --tier 2 --order 52`,
   renamed to the path above where the door dates it otherwise. The shape to follow is
   `2026-10-26-spec-TOOL-dTotalRecall-122.md`, its binding line included.
6. Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-124`,
   `python tools/check-spec-tokens.py --spec <path>` and `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec
   <path>`, and fix every finding naming the spec. Every number carries an id, a path:line by blob, PINNED or DERIVED.

### Acceptance

The commands name no finding, and H1 is one scope item with an acceptance criterion and an arm.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

The minors of the same report, which TOOL-dTotalRecall-125 owns. The `d0e02120b` limits red and any history rewrite. The units
held on owner asks.

### Limitations

The write grant is that spec file alone. The status is `OPEN`, rev-1, base `33706662e`. Scratch goes under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/124/`, spelled absolute. Do not commit.
Run no gate leg: each criterion is a probe the builder can make. Another spec writer writes spec 125 at the same time;
touch nothing of it.

### Reuse

The report's own Fix paragraph for H1, and the code record's existing `./` stripping on the output side.
