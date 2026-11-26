**Serves:** journal TOOL-dTotalRecall-58
**Caused-by:** TOOL-dTotalRecall-58

# Brief — dTotalRecall: TOOL-dTotalRecall-58's first build pass diverged; fold the spec to rev-4

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 58's builder, dispatched at `fa67a5614`, returned a divergence and
built nothing: `memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-58-1-builder-return.md` holds it
whole.

## The brief

### Goal

Revise unit 58's spec in place as one rev bump, with one revision-log line naming this brief by its file stem, so a
builder can build it as written over HEAD. Read the builder return first and re-derive each point at HEAD before
acting on it.

### Items

1. AC4 and S4 contradict section 4: the new `check_marker_domain` calls `read_kept_reason`, so it is a fourth caller.
   AC4 lists the definition, the three callers S4 names and `id_grammar.py#check_marker_domain`, red on a caller
   beyond those; S4 keeps the three as the pre-pass measure and adds the fourth, the only caller that reads
   build-folder lines, to refuse them.
2. S1 and S3 name `CAUSE_WRITER_KEPT` and `ALIAS_COMPARE_KEPT`, retired at HEAD: the keep is
   `tree_lib.py#CENSUS_KEPT_PATHS` read through `read_kept_path`.
3. Section 4 says what `check_marker_domain` returns (`(line number, finding)` pairs) and that marker reds stay
   outside each build-folder count line's `N red`, as the drained-row red does, unless HEAD shows a reason against it.
4. A section 8 resolution mark is exactly `RESOLVED (agent, YYYY-MM-DD, delegated)`. Every number carries an id, a
   path:line, PINNED or DERIVED on its line. Touch nothing the three points above do not need.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-58` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding they name. The status header
keeps `INPROGRESS`; do not commit.

### Acceptance

Both commands exit 0; the spec carries the next rev and one revision-log line naming this brief; the return names
each of the three points with what the spec now says.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec outside unit 58.

### Reuse

The spec's section 10 seam, re-verified at HEAD.
