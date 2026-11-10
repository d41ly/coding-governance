# Revision brief — aSmoothedDispatch: specs 1, 2 and 3 carry spec-token hits

**Serves:** research TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3

## The brief

### Goal
`python tools/check-spec-tokens.py` over the tree with specs 1 to 5 staged printed 10 unwaived hits, all in specs 1, 2 and 3. Each hit is a word the checker split out of a backticked shell command in §6, then graded as an untracked path: `words/x.sh'"`, `tools/unattended/unattended.sh;`, `memory/builds/s/RUN.md` and its variants, and `memory/builds/tRun/RUN.md`. The checker skips fenced blocks (`render_unfenced`) and clears any single backticked token that holds a space. Revise only the spec you are handed, as a rev bump with its revision-log line naming this record. Move each offending command, or the expected output line, out of inline backticks into an indented fenced block inside its bullet. Change no criterion's meaning, command or expected output.

### Items
The hits per spec:
- spec 1: AC6's `grep -cF -- "--writes 'two words/x.sh'" …` command;
- spec 2: AC1's `bash -c '. tools/unattended/unattended.sh; remove_run_state_writes …'` command and its expected output line; AC2's `declare -f verb_dispatch` command and its grep; AC3's and AC4's `run --dispatch tRun …` calls;
- spec 3: AC5's `GOV_RUNLOG=0 bash tools/unattended/unattended.sh; echo "rc=$?"` command.

Fix any other inline-backticked command in your spec's §6 that splits into an untracked path-shaped word the same way.

### Acceptance
The same checker run, with your spec staged, prints no hit naming your spec.

### Gates
Spec tokens, run by the main loop after you return; memory hygiene check 12 on the revision-log line.

### Non-goals
Any change to scope, design, criteria, or another unit's spec.

### Limitations
Edit only your own spec. Do not stage or commit.
