**Serves:** journal TOOL-dTotalRecall-2

# Brief — dTotalRecall: TOOL-dTotalRecall-2's F6 resolution mark in its canonical form

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The first build pass of TOOL-dTotalRecall-2 diverged
(`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-2-1-builder-return.md`): the pre-commit hook's
memory hygiene check 12 refused the spec's move to CLOSED, because §8 F6 carries no conforming resolution mark.

## The brief

### Goal

Revise `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md` in place as a rev-13 bump, with one
revision-log line naming this brief by its file stem, so §8 F6 carries the canonical mark.

### Items

1. The mark grammar is `tools/memory-tree/check-memory-hygiene.sh#check_mark`: `RESOLVED (agent, YYYY-MM-DD, delegated)`,
   read after code spans are removed. F6 reads `RESOLVED (agent, 2026-11-22, delegated by` followed by a code span; rewrite
   it to `RESOLVED (agent, 2026-11-22, delegated): (b), …` and cite the fold brief after the mark, outside the parentheses.
2. Check every other §8 F-item's mark against the same grammar and fix any that would fail it the same way.
3. Change nothing else; the status header keeps `INPROGRESS`.

Before returning, run `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <path>`, `bash
tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-2` and `python tools/check-spec-tokens.py
--spec <path>`, and fix every finding they name. Then confirm the mark passes as a CLOSED spec would grade it: copy the
spec to the scratch directory, set its status to CLOSED there, and run check 12 over that copy with `--spec`. The write
grant is the spec file alone; do not commit.

### Acceptance

Check 12 passes over the spec and over the CLOSED copy; the other two commands exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other change to spec 2; no other spec.
