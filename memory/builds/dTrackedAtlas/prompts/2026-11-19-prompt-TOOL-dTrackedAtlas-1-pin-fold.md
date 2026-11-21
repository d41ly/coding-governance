# Revision — dTrackedAtlas: the four specs pin their figures, and unit 1's `predecessors` takes a declared verb

**Serves:** research TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4

## The prompt

> Fold the pass legs' reds over this build's specs, found after unit 1's pass commit `390c2bc05`, into the four specs as a rev bump each.

## The brief

### Goal
The pass legs run after unit 1's pass commit `390c2bc05` redded on this build's own specs. The `writing practice (records and units)` leg's `pinned-facts` arm reds a figure typed before a unit word with no pin on its line (an 8-to-40-hex sha, a `path:line`, or the word PINNED or DERIVED; a figure inside a backtick code span is not graded). The `lexicon wiring` leg reds unit 1's interface name `predecessors`, whose leading token is no declared verb (`python tools/lexicon/lexicon.py --suggest predecessors --as py.function`). Fold both into the specs, so the builders build from specs the bar accepts.

### Items
1. In `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-1.md`, pin the figure `900 s` on its line, and rename the interface function `predecessors` to `derive_predecessors` everywhere the spec names it (interface table, prose, the schedule's edit). Write in its revision log that the built code is renamed by the main loop's inline red fix in the same commit.
2. In `…-TOOL-dTrackedAtlas-2.md`, pin `17 MB`, `22 rows` and `509 rows` on their lines; in `…-TOOL-dTrackedAtlas-3.md`, pin `16 MB`; in `…-TOOL-dTrackedAtlas-4.md`, pin `1 s`, `2 s`, `10 s`, `13 s`, `60 s`, `300 s`, `1500 s` and `2400 s` on their lines, wherever each sits. Use PINNED for a measured figure, DERIVED for one computed from another source, or a `path:line` or sha where the line already cites its source; a figure that is a constant this spec declares may instead sit in a code span.
3. Where a spec cites a symbol by a bare basename, such as `lib-unattended.sh#read_landing_commit` or `design_lib.py#parse_chain_cell`, give the repository-relative path, `tools/unattended/lib-unattended.sh#read_landing_commit` and `tools/memory-tree/design_lib.py#parse_chain_cell`, so the positional check resolves it.
4. In specs 2, 3 and 4, any reference to unit 1's `predecessors` follows the rename.
5. Bump each touched spec's rev and add one revision-log line naming this record and what moved; no other design change.

### Acceptance
`bash tools/unattended/unattended.sh --plan dTrackedAtlas --paths` grades units 1 to 4 READY; `--check-specs dTrackedAtlas TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4` prints no refusal; `check-memory-hygiene.sh --only 12 --spec <path>` and `check-spec-tokens.py --spec <path>` are clean for each; no spec line holds a figure before a unit word without a pin, outside a code span.

### Gates
The spec-format and spec-token checks the role allows; no other gate.

### Non-goals
No design change beyond the rename and the pins; no product code; no commit and no index render, which the main loop does.
