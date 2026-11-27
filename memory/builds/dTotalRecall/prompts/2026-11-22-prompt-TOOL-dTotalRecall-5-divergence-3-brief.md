**Serves:** journal TOOL-dTotalRecall-5

# Brief — dTotalRecall: TOOL-dTotalRecall-5's third build pass diverged; settle the fixture population once

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The unit's third builder returned a DIVERGENCE at base `17f07b292`
before writing anything, recorded whole in
`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-5-3-builder-return.md`. This is the third
divergence of this unit; each found a population the spec had not measured.

## The brief

### Goal

Revise `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-5.md` in place as a rev bump, with one
revision-log line naming this brief and the builder return by their file stems, so a fourth builder meets no
unmeasured population.

### Items

1. Read the builder return whole. Its finding: S7 and S13 point every reader at `slug_class`, which refuses the
   short fixture slugs many suites feed through those readers (`x`, `s`, `a`, `bx`, `fx`, `dX`, `tA`, `tFix2` and
   others), in suites §7 expects green; the builder's search found them in the files it lists (its output is
   `C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/fixture-slugs-pass3.txt`). Decide the fixture population as a fork F13 by the build method's M3, marked
   RESOLVED in §8: (a) lift S13's re-spelling rule to S7 and re-spell every refused fixture id, every suite file in
   Files touched, the population fixed by a stated search command; (b) readers whose only refused population is
   fixtures keep a looser class, with the reason and where the two classes are held equal; or another option you
   measure. Weigh each against `[one-fact]` and against the size and risk of the write set.
2. Re-derive the population for the option you choose with one stated command over the whole tree, the builder's
   search as a model, and give every hit a disposition: re-pointed, re-spelled, or kept with its reason. Include the
   test-side copies of re-pointed readers the return names (`merge-rows.test.sh`'s `ORACLE`, `hygiene-parity.test.sh`,
   `tools/runlog/selftest.py`, `tools/govkit/selftest.py`).
3. Then do the full caller-and-suite trace once more: for every function and regex S4, S7 and S13 change, every
   suite that feeds it an id and what that suite asserts, so no fourth population is left.
4. If the write set your choice forces is larger than one builder pass can carry, say so in your return with its
   size; do not split the unit yourself.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-5`,
`python tools/check-spec-tokens.py --spec <path>` and `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec
<path>`, and fix every finding they name. The status header keeps `INPROGRESS`; the write grant is the spec file
alone; do not commit.

### Acceptance

Every command exits 0; the spec carries its next rev and one revision-log line naming this brief and the return.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but unit 5's. No product code. No change to Goal or Scope intent beyond what the findings force.
