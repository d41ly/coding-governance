**Serves:** journal TOOL-aOrientedCast-28

# Brief record — fold TOOL-aOrientedCast-28: two path tokens, and the commit stage's missing token check

## The prompt

The build harness's spec stage wrote TOOL-aOrientedCast-28's spec and committed it at `3153388f3`.
Its commit stage never ran the spec-token checker, and the checker now reds over the live tree on
two of that spec's tokens, so `--dispatch` refuses every pass in the build:

```text
spec-tokens: memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md [path] `require('./tools/unattended/gate-guard.js');` — not tracked by git ls-files
spec-tokens: memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md [path] `require('./.claude/roles.json').roles;` — not tracked by git ls-files
```

## The brief

### Goal

TOOL-aOrientedCast-28's spec passes the spec-token checker, and the harness it specifies can no
longer commit a spec that checker reds.

### Items

1. **Respell the two tokens** so each backticked path token is exactly a tracked path, or is no
   path token at all. Read `tools/check-spec-tokens.py` for its path predicate without running it.
2. **Add to the unit's scope, files and acceptance:** the commit stage of
   `tools/workflows/unattended-build.js`, for both its spec stage and the new fold stage, runs the
   spec-token checker over the specs it is about to commit, and refuses the commit, naming each hit,
   when the checker reds on any of them. Name the staged break of its `New arm:` line.
3. Bump the rev with its §9 line.

### Acceptance

`python tools/check-spec-tokens.py` reports no hit on TOOL-aOrientedCast-28's spec, and the new
criterion is a direct check a builder may run.

### Gates

The close runs `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1` once on the reconciled tree.

### Non-goals

- Any spec other than TOOL-aOrientedCast-28's.
