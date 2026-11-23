**Serves:** journal TOOL-dTotalRecall-36
**Caused-by:** TOOL-dTotalRecall-36

# Brief — dTotalRecall: fold TOOL-dTotalRecall-36 over what order-18 units and the built unit 19 need from it

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 36 builds at order 17, after unit 21 and before unit 39; the order-18
re-grounds of units 48 and 49 and the build of unit 19 (CLOSED at `6ea003891`) each moved a claim it makes.

## The brief

### Goal

Revise the spec in place as one rev bump, with one revision-log line naming this brief by its file stem, so a builder
can build it as written over HEAD.

### Items

1. S4 mints `check_cause_line` WITHOUT wiring it into `tools/runlog/record.py#check_record_lines`: unit 48 rev-3 S1
   does that wiring at order 18, and wiring it here reds the runlog record schema on every tracked run record at this
   unit's tip. State the hand-off in Scope and keep the matching edge with unit 48.
2. Files touched gains `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`: the
   VIEW_HEAD change re-renders it (unit 49 rev-3 notes it); name on the gates section's leg line the legs its guards
   trip (the chain-packet self-test and policy fixtures among them).
3. Unit 19 is CLOSED at `6ea003891`: `tree_lib.py#read_header_edges`, the record door's `--caused-by` and `--edge`,
   `tools/memory-tree/record_causes.py` and the `legacy-records` population. Every claim this spec makes about the
   cause line, the header reader or the door is re-read against that code, and a criterion that writes a record names
   its resolving cause.
4. A §8 resolution mark is exactly `RESOLVED (agent, 2026-11-23, delegated)`: nothing else inside the parentheses (check
   12 strips code spans and refuses the rest); cite the brief after the mark. Cite code as `path#symbol` or blob-pinned,
   never a bare `path:line`; every number carries an id, a path:line, PINNED or DERIVED on its line.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-36` and
`python tools/check-spec-tokens.py --spec <path>`, and fix every finding they name in this spec. The status header keeps
`DEFERRED`; the write grant is the spec file alone, plus one edge bullet in a DEFERRED sibling where an edge needs its
mirror; do not commit.

### Acceptance

Both commands exit 0; the spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No change to Goal or Scope intent beyond what the items force.
