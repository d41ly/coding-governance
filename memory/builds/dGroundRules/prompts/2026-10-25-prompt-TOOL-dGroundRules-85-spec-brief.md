**Serves:** research TOOL-dGroundRules-85

# Spec brief — TOOL-dGroundRules-85, the per-cap budget readers this build added put two checkers over their fork ceilings

## The prompt

The close's bar pre-check at `cae57b1d8` redded the spawn budget leg: the memory-hygiene probe forks 240 against its ceiling 189, and the manifest-check probe 105 against 90 (rows 19 and 20 of `memory/project/fork-ceilings.txt`). Both were green at the run's base `3c2b69be4`. The researcher's triage, `memory/builds/dGroundRules/build/2026-10-25-build-TOOL-dGroundRules-84-research-bar-triage.md` leg 6, traces both to `69aa76517` (TOOL-dGroundRules-9): per-cap `$(printf | awk)` readers at `tools/memory-tree/check-memory-hygiene.sh:527,534` with a per-key `grep -qE` loop, and `read_budget_field` called three times at `skills/session-kickoff/manifest-check.sh:1337` plus a new `resolve_python`, `resolve_kit_file` and python start. Its estimate: parsing the budgets answer once in-shell recovers about 50 forks for memory-hygiene but about 6 of manifest-check's 15.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-85.md`, a Tier-1 micro-spec at order 32, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-83.md` follows, that brings both probes back under their ceilings without changing what either checker decides. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Measure first: run the spawn-budget checker's own `--only <id> --sites` for `memory-hygiene` and `manifest-check` at HEAD and at the base (a scratch clone for the base), and attribute every added fork to its line. Record the counts in the spec.
2. Design the fix from the measurement so both counts land at or under their ceilings: read the budgets answer once and split it with builtins, and drop per-key subshells and greps. If manifest-check cannot reach 90 that way, find a design that does (one reader call for all caps, or reading the policy file's budgets without the python start where the policy kit's own reader contract allows it) and name the reader contract it keeps. The ceilings in `fork-ceilings.txt` only shrink: a row edit upward is never the fix; lower a row only where the measured count falls below it and say by how much.
3. The checkers' verdicts must not move: an acceptance criterion runs each checker over a tree whose budgets refuse and over one whose budgets pass, and compares its findings before and after. `spawn-idiom-sites.txt` rows for these two files change only where the conversion moves a count; unit -84 builds before this one and also edits that file, so this spec names its rows by file.
4. Each acceptance criterion is a leg command the pass may run (the spawn-budget checker with `--only`, the two checkers over scratch trees), never a self-test suite or the bar, and carries `Red when:` with a staged break that reds it by name. §6 names the legs the touched files owe through `derive_guarded_legs`.
5. §7 "Open questions" reads exactly `none`, with no bullet under it; any follow-up goes in the §8 revision log as prose. No line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet carries `Red when:`; keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no retirement word in §2; an untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Legs 1-5 and 7-10 (units -84 and -86); any other probe's fork count; the budgets' values.

### Limitations
If no design reaches 90 for manifest-check, the spec says so in §1 with the measured floor and the reason; the main loop then rules.

### Reuse
The policy kit's existing budgets reader and the `read_budget_field` call sites; the spawn-budget checker's `--sites` output.
