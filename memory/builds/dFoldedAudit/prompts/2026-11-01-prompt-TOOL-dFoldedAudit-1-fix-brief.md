# Fix brief — dFoldedAudit: the spec-token hits and the first builder's finding

**Serves:** research TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7

## The brief

### Goal
Clear every spec-token hit that makes `--dispatch` refuse this build's units, and fold the one arm the first builder showed cannot go RED, so unit 7 can be dispatched again. Commit nothing; the main loop commits and runs the checker.

### Items
1. TOOL-dFoldedAudit-1 §6 AC5 spells `git show 74274869:tools/memory-tree/BUILD-METHOD.template.md` as one word, which the paths join reads as an untracked path. Respell it so the sha and path are not one word, for example `git show <base>:tools/memory-tree/BUILD-METHOD.template.md` with `<base>` stated as `74274869`.
2. TOOL-dFoldedAudit-4's Files touched names `memory/map/features/spec-tokens.md`, which trips the guards of legs `recall floor` and `recall floor arms`. Satisfy the [guards] join: read what `tools/check-spec-tokens.py` wants and add what it requires to §7, the way a sibling spec does.
3. TOOL-dFoldedAudit-6's Files touched names `memory/builds/dRankedPlan/README.md`, which trips the same two guards. Same fix.
4. TOOL-dFoldedAudit-7 §7's AC7 arm cannot go RED as written. A `PARITY_ROWS` row only compares process and in-process output, status and tree (`tools/unattended/unattended.test.sh:2361-2366`), so deleting the shape case changes both sides alike. Rewrite that `New arm:` line and its AC to a positive assertion of the refusal text beside the row.

### Acceptance
Each named spec carries a rev bump and a §9 line. The main loop's `python tools/check-spec-tokens.py` then reports no hit naming this build.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass. Hygiene checks 5, 12 and 25 in a scratch clone.

### Non-goals
No design tag is re-opened, no code, no write outside this build's `spec/`.
