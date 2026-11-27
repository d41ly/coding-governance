**Serves:** journal TOOL-dTotalRecall-53
**Caused-by:** TOOL-dTotalRecall-53

# Brief — dTotalRecall: TOOL-dTotalRecall-53's first build pass diverged; fold the spec to rev-6

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 53's builder, dispatched at `f5a81b323`, returned a divergence and
built nothing: `memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-53-1-builder-return.md` holds it
whole.

## The brief

### Goal

Revise unit 53's spec in place as one rev bump, with one revision-log line naming this brief by its file stem, so a
builder can build it as written over HEAD. Read the builder return first and re-derive each point at HEAD before
acting on it.

### Items

1. S9's window: the builder matched the spec's 116 unanswered lines (DERIVED 2026-11-23 by the builder's probe) only
   by counting the literal's own line inside the window. Say so in S9 and AC9: a literal is answered by a
   `Caused-by` on its own line or the three below it.
2. Five unanswered literals sit inside a docstring or a triple-quoted string, where §4 admits neither a marker nor a
   cause line: `tools/workflows/review_replay.py` (its module docstring and the first line of its `LEGACY` fixture),
   `tools/memory-tree/build_records.py` (two docstrings) and `tools/runlog/record.py#check_serves_line`'s docstring.
   AC8 needs `review_replay.py` read as kept, never red. Decide by M3 and record in §8 as
   `RESOLVED (agent, 2026-11-23, delegated)` how such a literal is answered: (a) each docstring literal is reworded
   so it no longer spells the `**Serves:** ` literal, named per site, and the fixture literal answered as you decide;
   (b) the census skips a literal inside a string body; (c) a marker inside the string text is read as a marker.
   Weigh what each does to a fixture writer whose string body IS rendered into a record. Make S8, S9, S34, §4's
   placement rule, AC8 and AC9 agree with the pick, and re-derive the population at HEAD.
3. S36 cannot fit: `memory/guides/BUILD-METHOD.md` measures 30717 of its owner-set 30720-byte budget (DERIVED
   2026-11-23, LF bytes; its M1 Budget line), and raising or trimming it is the owner's. Move S36 and AC36 out of
   Scope into a non-goal that rides owner ask TOOL-dTotalRecall-113, filed today for it. Amend §8 F2 with a dated
   line saying so, and drop from Files touched, §7's leg line and the kickoff-manifest re-stamp every path and leg
   that only S36 needed.
4. A §8 resolution mark is exactly `RESOLVED (agent, 2026-11-23, delegated)`, the brief cited after the mark. Cite
   code as `path#symbol` or blob-pinned; every number carries an id, a path:line, PINNED or DERIVED on its line.
   Keep the spec under 49152 B (PINNED 2026-11-20), tightening prose you touch, never dropping a criterion.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-53` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding they name. The status header
keeps `INPROGRESS`; do not commit.

### Acceptance

Both commands exit 0; the spec carries the next rev and one revision-log line naming this brief; the return names
each of the three points with what the spec now says.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec outside unit 53.

### Reuse

The spec's §10 seam, re-verified at HEAD.
