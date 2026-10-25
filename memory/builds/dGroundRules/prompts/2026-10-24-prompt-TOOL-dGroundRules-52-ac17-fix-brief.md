**Serves:** research TOOL-dGroundRules-52

# AC17 fix brief — TOOL-dGroundRules-52's cold-case criterion through a probe that can move

## The prompt

> The builder of TOOL-dGroundRules-52 handed back a DIVERGENCE: `tools/policy/check_policy.py` sets `sys.dont_write_bytecode = True` at import, so `COLD_WRITING` (bytecode writing "on" through the environment) never writes a `.pyc.<digits>` temporary and AC17 cannot red. Its code for S6, S14, S15, S20 and S25 is written and saved as a patch.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-52.md` so S20 and AC17 observe the digit-tail cut's absence through a probe that can move. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. S20 drops its sentence that the cold case is observed with bytecode writing on, and states that the policy check sets `sys.dont_write_bytecode` at import, so no traced run writes a cache temporary.
2. AC17 is replaced by a direct probe, spelled whole in the fenced literal block: it imports `tools/policy/check_policy.py` and calls `add_source_read` on a read-mode `tools/govkit/__pycache__/govkit.cpython-314.pyc.123`, then prints whether that path landed in `UNMAPPED_READS` and whether `tools/govkit/govkit.py` landed in `SOURCE_READS`. On the built tree it prints the unmapped path and no source; its Red when names the staged break that restores the `.pyc.<digits>` cut in a scratch copy, under which the probe prints the source path instead.
3. `COLD_WRITING` leaves the spec; no other criterion consumes it.
4. The status header's rev rises by one, with a §9 line naming the divergence and the ruling. Every acceptance-section code span stays on one line; every acceptance bullet keeps a `Red when:` clause; no acceptance line starts at column 0 with `AC<n>`; no code span holds a path glued to a quote or a `rev:path` token; an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder; every command runs from the repository root.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Any other criterion or item of this spec; any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The builder's patch is in the run's scratchpad and is applied at the next dispatch.

### Reuse
`KEPT_PROBE` in this spec's literal block, whose shape the new probe follows.
