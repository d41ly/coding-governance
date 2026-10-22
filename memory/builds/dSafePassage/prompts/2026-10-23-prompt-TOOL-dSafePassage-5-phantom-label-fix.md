**Serves:** research TOOL-dSafePassage-5

# Brief — dSafePassage: the phantom AC2 head in TOOL-dSafePassage-5's acceptance section

## The prompt

> The spec commit stage did not commit. HYGIENE check 12 FAILED on
> memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-5.md: acceptance bullets naming no backticked
> witness, and no failure mode, at AC2.

— the unattended-build harness's spec commit stage, run wf_1c1e65a6-959

## The brief

### Goal

Make check 12 read TOOL-dSafePassage-5's §7 as the criteria it actually holds, by rewording the one prose line it
misreads as a second AC2 head. Nothing a criterion says changes.

### Items

1. Line 277 of the spec opens at column 0 with `AC2 to AC10 and AC12 build the release-0 tree first;`. The bullet
   head pattern in `tools/memory-tree/check-memory-hygiene.sh` (near line 2009) admits a label at column 0 with no
   list marker, so this prose line closes the real AC2 bullet and opens a phantom one with no witness. Change its
   start to `Criteria AC2 to AC10 and AC12 build the release-0 tree first;`, keeping the rest of the sentence.
2. Reword the same way any other column-0 line in §7 that opens with an `AC<n>` label but is not a criterion bullet.

### Acceptance

`grep -nE '^(\*\*)?AC[0-9]' memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-5.md` prints no line.

### Gates

None. A role agent runs no gate; the main loop's commit runs the memory hygiene hook.

### Non-goals

No rev bump, because the spec is rev-1, uncommitted and unreviewed. No other content change. No commit, no stage,
and no write outside that one file.

### Limitations

This is an unattended run, so nobody will answer a question.

### Reuse

None needed: a one-line rewording.
