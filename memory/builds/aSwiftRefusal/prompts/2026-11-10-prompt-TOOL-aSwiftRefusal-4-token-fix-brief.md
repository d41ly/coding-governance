# Brief — aSwiftRefusal: the spec-token fold for TOOL-aSwiftRefusal-4

**Serves:** research TOOL-aSwiftRefusal-4

## The brief

### Goal
`python tools/check-spec-tokens.py` exits 1 with one unwaived hit, a `[bar]` hit in spec 4's §6 on the backticked token `tools/unattended/check-unattended.test.sh`: a suite is not an acceptance observation. Fold it as a rev bump with its revision-log line, and change nothing else: observe the check on a staged fixture or a probe of the code, cite a suite file in §6 without its full path in backticks if it must be named at all, and name the suite on the §7 `New arm:` line only.

### Items
1. The one hit folded in spec 4, rev-1 to rev-2, one revision-log line naming it.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit naming a file under `memory/builds/aSwiftRefusal/spec/`.

### Gates
spec tokens · memory hygiene.

### Non-goals
Any change to spec 4's scope, design, criteria or forks beyond the token's spelling. Specs 1 to 3.

### Limitations
Spec text only; no code, no commit. The main loop commits after the checker reads clean.

### Reuse
The unit's brief, `prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-4-round1-fix-brief.md`, is unchanged and still governs. Spec 2's rev-2 fold of the same hit class is the precedent.
