# Brief — aSwiftRefusal: the spec-token fold for TOOL-aSwiftRefusal-1 to -3

**Serves:** research TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3

## The brief

### Goal
`python tools/check-spec-tokens.py` exits 1 with 7 unwaived hits over the three uncommitted specs, so they cannot be committed. Fold each hit in the spec it names, as a rev bump with its revision-log line, and change nothing else:
- spec 1: a `[path]` hit on the inline python probe that carries `tools/memory-tree/check-arms.py` and `m.branches('.','tools/unattended/unattended.sh')` — the checker reads each backticked token with a slash and an extension as a path. Name the probe so no backticked token is path-shaped: cite `check-arms.py` and its `branches()` by basename and give the command outside backticks, or point at a tracked script that runs it.
- specs 1 and 3: `[path]` hits on `tools/unattended/VERBS.template.md)` and `memory/guides/UNATTENDED-VERBS.md)` — a `)` sits inside the backticks. Move it outside.
- spec 2: a `[bar]` hit on `tools/unattended/unattended.test.sh` in §6 — a suite is not an acceptance observation. Observe the predicate on a staged fixture or a probe instead, and name the suite on the §7 `New arm:` line only.

### Items
1. Each hit above folded in its own spec, rev bumped, one revision-log line naming the hit.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit naming a file under `memory/builds/aSwiftRefusal/spec/`.

### Gates
spec tokens · memory hygiene.

### Non-goals
Any change to a spec's scope, design, criteria or forks beyond the token's spelling. The other specs of the build.

### Limitations
Spec text only; no code, no commit. The main loop commits all three after the checker reads clean.

### Reuse
The build's brief, `prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-1-brief.md`, is unchanged and still governs.
