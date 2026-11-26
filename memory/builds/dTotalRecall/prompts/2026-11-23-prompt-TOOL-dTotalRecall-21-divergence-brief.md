**Serves:** journal TOOL-dTotalRecall-21
**Caused-by:** TOOL-dTotalRecall-21

# Brief — dTotalRecall: TOOL-dTotalRecall-21's first build pass diverged; fold the spec to its next rev

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The unit's first builder returned a DIVERGENCE at base `e0cd68745`,
recorded whole in `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-21-1-builder-return.md`.

## The brief

### Goal

Revise the spec in place as one rev bump, with one revision-log line naming this brief and the builder return by their
file stems, so the next builder can build it as written over HEAD.

### Items

1. Read the builder return whole. Section 4 "The rows" claims `tag_index.py#load_index`'s schema reset drops recall's
   FTS5 tables with its own; at HEAD the reset drops every `sqlite_master` table name in turn, an FTS5 table's drop
   removes its shadow tables first, and the next DROP raises `no such table: fts_record_data`, so the reset refuses for
   good and `gov_tag.py#remove_index` with it. Settle it as a §8 fork decided by the build method's M3: the reset made
   FTS5-tolerant (virtual tables first, or re-reading the list at each step), with `tools/playbook/tag_index.py`
   (`load_index` and its module docstring) joining Files touched and the departure from the CLOSED parent
   PLAY-dOrderedCharter-55 S16 named as F5 names its own; or another seam that stops a reset bricking the shared file.
   Give the choice a criterion whose red is a second reset refusing.
2. Files touched gains `memory/guides/SESSION-KICKOFF.md` (`.memory-tree.conf` is on the kickoff manifest's `watch:`
   list, so its staging re-stamps the manifest) and the deviation record F5 says this pass writes, named by its
   folder; name on the gates section's leg line any leg their guards trip.
3. Every record a criterion writes names a resolving cause: unit 19 (CLOSED at `6ea003891`) reds the record-causes
   leg on a record with no `**Caused-by:**`.
4. A §8 resolution mark is exactly `RESOLVED (agent, 2026-11-23, delegated)`: nothing else inside the parentheses (check
   12 strips code spans and refuses the rest); cite the brief after the mark. Keep every other decision; cite code as
   `path#symbol` or blob-pinned; every number carries an id, a path:line, PINNED or DERIVED on its line.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-21`,
`python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/writing_practice.py check pinned-facts`, and
fix every finding they name in this spec. The status header keeps `INPROGRESS`; the write grant is the spec file alone;
do not commit.

### Acceptance

The three commands exit 0 or read green; the spec carries the next rev and one revision-log line naming this brief and
the return.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-21. No product code.
