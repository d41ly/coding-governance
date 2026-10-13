**Serves:** journal TOOL-aOrientedCast-25

# Brief record — fold TOOL-aOrientedCast-25 on its builder's divergence

## The prompt

TOOL-aOrientedCast-25's builder returned `committed: false` with this divergence, and saved its work
as a patch for the next pass:

```text
§4 "The criterion amendments": the liveness twin `v=$(sed -n 's/^KIT_UNATTENDED_VERSION=//p' tools/unattended/unattended.sh)` keeps the line's trailing comment (`KIT_UNATTENDED_VERSION=1.106 # gov:kit unattended@1.106 — …`), so `git grep -l "gov:kit unattended@$v"` prints nothing. The spelling `v=$(sed -n 's/^KIT_UNATTENDED_VERSION=\([0-9.]*\).*/\1/p' tools/unattended/unattended.sh)` yields 1.106 and the search lists the kit's carriers.
```

## The brief

### Goal

TOOL-aOrientedCast-25's spec states commands that give the results it claims, so a builder can
build it as written.

### Items

1. **Respell the liveness twin** in §4 "The criterion amendments". As written,
   `v=$(sed -n 's/^KIT_UNATTENDED_VERSION=//p' tools/unattended/unattended.sh)` keeps the line's
   trailing `# gov:kit …` comment, so the `git grep -l "gov:kit unattended@$v"` it feeds prints
   nothing. The builder probed
   `v=$(sed -n 's/^KIT_UNATTENDED_VERSION=\([0-9.]*\).*/\1/p' tools/unattended/unattended.sh)`,
   which yields the bare version and lists the kit's carriers. Use that form, and make AC8's wording
   and the ledger sub-head §4 prescribes agree with what it prints.
2. **AC7's three runs of `tools/check-microformats.sh`** are a gate leg ("micro-format
   definitions") that the role gate refuses a builder, even on a scratch copy. Give AC7 a
   `permission:` line naming the main loop at the close, the way AC11 is given one, and keep any part
   a builder can observe by a direct probe.
3. **Line references:** `checkAgentLines` is now at `tools/hooks/format-guard.js:429`, not `:396-415`;
   re-read every `path:line` the spec cites into a file another unit has since changed.
4. Bump the rev with its §9 line. The spec sits near the 49152-byte spec ceiling: add no prose
   beyond what these items need, and trim elsewhere if they need room.

### Acceptance

`python tools/check-spec-tokens.py` reports no hit on the spec, its size included, and every command
the spec states gives the result it claims when run against the current tree.

### Gates

The close runs `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1` once on the reconciled tree.

### Non-goals

- Any change to the unit's scope.
- Any spec other than TOOL-aOrientedCast-25's.
