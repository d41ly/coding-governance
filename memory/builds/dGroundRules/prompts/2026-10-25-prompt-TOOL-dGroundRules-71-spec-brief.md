**Serves:** research TOOL-dGroundRules-71

# Spec brief — TOOL-dGroundRules-71, the hygiene suite's check-7 arms read the cap rule suffix

## The prompt

> At the close the main loop ran `tools/memory-tree/check-memory-hygiene.test.sh` at 4f76c4b39 and at the run's base 3c2b69be4. At the base it failed one arm, `the scoped runs do not partition the unscoped run's lines` (inherited). At 4f76c4b39 it failed that arm and three more: `FAIL check 7 emitted 0 findings, expected exactly 2 (fence, comment and separator are exempt; the 300-byte row is under the cap)`, `FAIL missing exact line: memory/backlog/ARCH.md:7 (301 chars > 300)`, `FAIL check 7 reported ''; expected the offending row at UNFENCED line 5 (raw line 8)`. `HYGIENE check 7 FAILED` still matched, so the check fires. TOOL-dGroundRules-9 (69aa76517) rewrote check 7's emitter (`tools/memory-tree/check-memory-hygiene.sh:1242`) to pass tab-separated fields to `check_cap_findings` (`:539-555`), which prints a refused finding as `<finding> · <cap rule>` (`:550`), the rule read by `read_cap_rule`. The arms at `tools/memory-tree/check-memory-hygiene.test.sh:1505-1515` (and the `UNFENCED line 5` arm after them) still grep the bare `(N chars > M)$` form.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-71.md`, a Tier-1 micro-spec at order 25, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-70.md` follows. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Verify the premise by running the checker itself (not the suite) on a scratch tree shaped like the fixture's `memory/backlog/ARCH.md` (the suite's own fixture builder may be copied into a scratch script), and record the exact refused-finding lines it prints, cap rule suffix included. If the lines carry anything beyond the `· <rule>` suffix (a tab, a mode field), that is a product defect in check 7's output and the spec says so instead of respelling the test; stop and say which.
2. S1 (if the premise holds): respell every check-7 arm of the suite that reads a finding line to the shape the checker prints now, keeping each arm's intent (exactly 2 findings; line 7 named at 301 > 300; line 6 not named; the unfenced numbering). Name the rule text the fixture's tree yields and why it is stable (the fixture's conf or policy, not gov's).
3. AC1: a scratch script holding the respelled arms' greps, run over the checker's real output on that scratch tree, prints the expected counts. Red when: the respelled grep is run over the output with the cap staged one higher (the row then under the cap) — or another staged break that reds by name. The suite is a self-test the pass may not run; the close runs it.
4. §6/§7 names the legs `--legs-for tools/memory-tree/check-memory-hygiene.test.sh` owes through `derive_guarded_legs`, and a `New arm:` line only if an arm is added; floor changes only if the assertion count moves.
5. Keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no acceptance line starts at column 0 with `AC<n>`; every AC bullet carries `Red when:`; no retirement word in §2; an untracked path sits in a fenced block.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Any other spec; the inherited partition arm; check 7's cap values.

### Limitations
Measured by the main loop; logs in the run's scratchpad as `sr-g_hyg.log` and `sr-hyg-base.log`.

### Reuse
The suite's own check-7 block and its fixture builder.
