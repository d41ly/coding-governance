**Serves:** journal TOOL-dWitnessedBar-26

# Brief — dWitnessedBar: unit 26's spec revised over its first builder's divergence

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 26's first builder (run `wf_9a057cc8-2c5`) stopped at a divergence
before keeping any code; its return is `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-26-1-builder-return.md`.

## The brief

### Goal

Revise the spec of TOOL-dWitnessedBar-26 in place, as a rev bump (rev-5) with one revision-log line naming the builder
return by its file stem, so a builder can build it as written over HEAD on node d.

### Items

1. Read the builder return whole; it measured each finding on node d. Its draft canonical, which runs every candidate
   after `GOV_BASH`, is at
   `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/u26/resolve_bash.draft.py`.
2. The probe (§4 "The rule"): name a probe whose first output line is `uname -s`'s own, so a WSL launcher run under any
   name answers `Linux` and AC1's `answered Linux` and AC3's posix case are reachable. State that the launcher drops the
   positional arguments, so `test -f "$1"` never refuses it and only the uname test does. Re-measure the probe you name
   against a copy of `C:/Windows/System32/bash.exe` outside System32 and against Git's `bin/bash.exe` before writing it.
3. The order (§4 versus AC1): state whether the resolver stops at the first candidate that passes or probes every
   candidate after `GOV_BASH` and reports each on a `tried:` line. This is a fork: decide it by the build method's M3
   (the most feature-rich option that survives the vetoes), mark it RESOLVED in §8, make §6 AC1 and §5's cost line
   agree with the choice, and say which in your return.
4. The sites: add `tools/loop/factories.py`'s `resolve_bash(...) or "bash"` and `tools/run-gates/regen.py`'s
   `shutil.which(run[0]) or run[0]` fall-back to the sites table, Files touched and the gates section's legs their guards name; say
   whether the S6 query should find each shape and, where it should, widen the query in §4 "The query".
5. The adapters: `loop_witness.resolve_bash` is imported by name by `tools/loop/breakpoints.py`, `budget.py`,
   `factories.py`, `loop_lib.py` and `position.py`, so it keeps its `path or None` contract through an adapter. State
   one rule for the name clash between the block's `resolve_bash` / `resolveBash` and every adapter that keeps that
   name (`profile_bar`, `upgrade_steps`, `corpus_ids`, the lexicon and runlog selftests, `handoff`, `loop_witness`), and
   rename `policy-mirror.js`'s internal `resolveBash`.
6. govkit selftest's `check_floor_bash` arms `[dSP-94]` and `[dSP-95]` assume no bash resolves once PATH is staged;
   with Git's `bin/bash.exe` as step 2 that premise fails on a Git for Windows node. State the staging that restores it,
   and the anchor the narrowed-catch arm reads once the block is inlined.
7. Run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-26` and
   `python tools/check-spec-tokens.py --spec memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-26.md`
   before returning, and fix every finding either names.

### Acceptance

Both commands in item 7 exit 0; the spec carries rev-5 and one revision-log line naming the builder return's file stem;
§8 carries the item-3 fork RESOLVED.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. Scope items unaffected by items 2 to 6 stay as written.

### Limitations

The status header stays `INPROGRESS`. The write grant is this spec file alone.

### Reuse

The builder's draft canonical in item 1.
