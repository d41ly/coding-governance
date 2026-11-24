**Serves:** research TOOL-dQuietDisk-3

# Spec task — dQuietDisk: unit 3's first-pass divergences, ruled

You write specs only. Do not commit. Unit 3's first pass (unit harness run `wf_10a96845-9d5`) built the whole unit,
observed it with probes and saved it as a patch. It then stopped on a divergence. The run has ruled on each point
(`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`). Write the rulings into
TOOL-dQuietDisk-3, rev-4 → rev-5, and add a revision-log line naming this task by its file stem.

## The rulings

1. **The batched short-sha read.** This is the wall TOOL-dQuietDisk-2 met and ruled in its rev-6:
   `git rev-parse --short` takes a single revision, and with two it exits 128. S6, section 4's "The run" step 6, the
   warm-run bound row, the section 5 perf line and AC4's count each name instead one
   `GIT log --no-walk=unsorted --format=%h --stdin` after the loop, given each distinct sha once on stdin, so input
   order holds and no argument-length limit applies. Where that batch answers other than one line per sha, the leg
   falls back to one `GIT rev-parse --short` per sha, the read the base leg makes. The builder's patch already has
   this shape.

2. **The code paths the store hashes.** S1 and section 4's "The store as built" name the code paths relative to the
   repository root through `derive_self_rel`. But `tools/lib/history_store.py#derive_code_digest` resolves a relative
   path against the repository the CLI runs in, which is the graded one, not the checkout the leg sits in. Run by path
   from another checkout, as AC1's new leg is, relative names would hash the graded repository's copies.
   **Ruling:** the leg passes a relative name only where `$ROOT/<rel>` is the leg's own directory, and an absolute
   path otherwise. Items stay shared across worktrees, because the store names an absolute in-repo path relative to
   its repository. State the condition in S1 and in "The store as built".

3. **The shell-line ledger.** The patch grows the leg and its suite past their rows in
   `memory/project/shell-role.txt`. The unit does not edit the ledger; the main loop widens the rows after the pass,
   as it did for units 1 and 2. Say that in section 7, and leave Files touched as it is.

## The saved patch

The next pass applies it:
`C:/Users/d41ly/AppData/Local/Temp/claude/b3f6db677b077b04/0840beea-0651-4dc3-9fe7-f227915b6b42/scratchpad/TOOL-dQuietDisk-3-pass1.patch`.
You need not mention it in the spec. The brief carries it.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-3`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Mark every figure you add PINNED, DERIVED or with an id on its own line. A section number before a noun reads as a
  count, so word around it.
