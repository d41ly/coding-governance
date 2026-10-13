**Serves:** journal TOOL-aOrientedCast-25

# Brief record — fold TOOL-aOrientedCast-25: AC13's probe token

## The prompt

TOOL-aOrientedCast-25 rev-5 is committed at `8500e23c8`, and the spec-token checker reds on it:

```text
spec-tokens: memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-25.md [path] `s.scan_file(open('tools/check-microformats.sh',` — not tracked by git ls-files
```

## The brief

### Goal

TOOL-aOrientedCast-25's spec passes the spec-token checker again.

### Items

1. **Respell AC13's probe** so its command names `tools/check-microformats.sh` as an exact path
   token: for example pass the path to `python -c` as an argument read through `sys.argv`, the way
   TOOL-aOrientedCast-28's AC10 passes its paths to `node -e`. Keep what the probe prints and its
   Red when case unchanged.
2. Bump the rev with its §9 line. The spec sits about 124 bytes under the 49152-byte ceiling after
   the index renders, and every new record naming the unit adds a row: trim at least 300 bytes of
   prose elsewhere so the fold and the next records rows fit.

### Acceptance

`python tools/check-spec-tokens.py` reports no hit on the spec, its size included.

### Gates

The close runs `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1` once on the reconciled tree.

### Non-goals

- Any change to scope or to a criterion's meaning.
- Any spec other than TOOL-aOrientedCast-25's.
