**Serves:** research TOOL-dQuietDisk-2

# Spec task — dQuietDisk: unit 2's first-pass divergences, ruled

You write specs only. Do not commit. Unit 2's first pass (unit harness run `wf_977d5bd9-59b`) built the whole unit,
observed it with probes and saved it as a patch. It then stopped on a divergence, because rev-5 asks for one git
command that refuses what the spec needs and leaves three decisions open. The run has ruled on each point
(`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`). Write the rulings into
TOOL-dQuietDisk-2, rev-5 → rev-6, and add a revision-log line naming this task by its file stem.

## The rulings

1. **The batched short-sha read.** `git rev-parse --short` implies `--verify` and takes a single revision: with three
   it prints `fatal: Needed a single revision` and exits 128, seen in the builder's scratch fixture. S6, section 4's
   "The run" step 5 and the warm-bound tally row each name instead one
   `GIT log --no-walk=unsorted --format=%h <sha>... --`, which prints every sha in argument order with git's own
   abbreviation. The builder's patch used it, and old against new read byte-identical at every AC1 point.

2. **A build commit with no parent.** The `unit` body grammar has no outcome for a root commit. Today such a unit counts
   as unbuilt-in-range and joins `inrange_ids` (`tools/unattended/check-pass-order.sh@638bb1d0c2a6:663`, `:668`).
   **Ruling:** a unit whose candidate is a root commit is never stored, so it is graded afresh on every run, exactly as
   today. Say so in section 4 "The items", and name it in S4's list of the cases the store never holds.

3. **The tie rule's read.** S4's tie rule needs each in-range candidate's committer second, and no read in "The run"
   supplies one. **Ruling:** one lazy `GIT log --format='%H %ct' HEAD`, run only at the first built miss with two or
   more candidates, so only on a cold or moved run. Name it in "The run" and count it in the tally of a run that
   misses.

4. **The `anchors` cell's key.** The cell is keyed by `<slug>`, the folder's basename. The README walk is
   `ls-tree -r | grep /README.md$`, so a nested README would give two folders one slug. **Ruling:** key the cell by
   the folder's path under `<MEMORY_ROOT>/builds/`, which reads the same as the slug for every top-level build. None
   is nested at this tree.

5. **The tally on the fixture.** The tally says 39 for a warm run on the fixture; the builder measured 35, because the
   fixture's `hooks.bypass` read spawns no git. Correct the fixture figure and mark it PINNED with its measurement.
   The bound of 45 is unchanged.

6. **The shell-line ledger.** The patch grows `tools/unattended/check-pass-order.sh` well past its row in
   `memory/project/shell-role.txt`. The unit does not edit the ledger; the main loop widens the row after the pass,
   as it did for unit 1. Say that in section 7 and leave Files touched as it is.

## The saved patch

The next pass applies it:
`C:/Users/d41ly/AppData/Local/Temp/claude/b3f6db677b077b04/0840beea-0651-4dc3-9fe7-f227915b6b42/scratchpad/TOOL-dQuietDisk-2-built.patch`.
You need not mention it in the spec. The brief carries it.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-2`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Mark every figure you add PINNED, DERIVED or with an id on its own line.
