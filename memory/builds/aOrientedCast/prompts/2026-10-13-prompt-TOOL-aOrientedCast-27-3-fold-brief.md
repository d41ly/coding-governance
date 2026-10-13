**Serves:** journal TOOL-aOrientedCast-27

# Brief record — fold the owner's sixth addendum into TOOL-aOrientedCast-27

## The prompt

The owner's sixth addendum, recorded with the run's reading in
`memory/builds/aOrientedCast/prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-8-owner-addendum.md`.
Verbatim:

```text
another addition to the build - 'unattended-unit' workflows carry only their generic workflow names and description (Builds exactly ONE unit...) with no pointers to the build slug or unit id. More information needs to be included with each started agent/workflow to clearly indicate what they're and what they're doing to the owner.
```

## The brief

### Goal

Every harness run tells the owner what it is and what it is doing, inside the limits the `Workflow`
tool sets: a run's title and description are its script's literal `meta` block and cannot be set per
call, so the run announces itself in its first log line, its agents' labels and the head of its
return.

### Items

1. **Fold TOOL-aOrientedCast-27** (`memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-27.md`)
   as a rev bump with its §9 line. Add to its scope, files and acceptance:
   - each of `tools/workflows/unattended-build.js`, `unattended-unit.js` and `tier2-review.js` logs
     `<slug> · <unit-or-scope> · <action>` as its FIRST log line, before any stage runs, in the same
     spelling its agent labels take;
   - each leads its return value with that same identity, in a field the caller reads first;
   - the roles README and `help/roles.md` say where the owner reads a run's identity, and that the
     run's title is fixed by the tool.
   Keep the unit's existing scope and criteria; add, do not rewrite. Its write set is unchanged
   except for the docs, which it already names. Its spec measures about 39.6 KB; stay well under
   the 49152-byte ceiling, since its generated records region grows with every new record.

### Acceptance

The fold leaves `python tools/check-spec-tokens.py` with no hit on TOOL-aOrientedCast-27, and each
new criterion is a direct check a builder may run, with a `New arm:` line where a suite arm proves it.

### Gates

The close runs `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1` once on the reconciled tree.

### Non-goals

- Renaming a `Workflow` run's title, which the tool takes from the script.
- Any unit other than TOOL-aOrientedCast-27.
