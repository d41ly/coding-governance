**Serves:** research TOOL-dGroundRules-70

# Spec brief — TOOL-dGroundRules-70, the unattended suite's reader-count arm after read_open_passes

## The prompt

> At the close (phase VERIFYING) the main loop ran `tools/unattended/unattended.test.sh --shard 4/8` at 4f76c4b39 and at 591cb00d7, and both runs failed one arm: `FAIL the driver's five readers call it rather than parsing the rows their own way: expected [5], got [4]`. The arm sits at `tools/unattended/unattended.test.sh:7591` and counts uncommented lines of `tools/unattended/unattended.sh` that spell `read_pass_declarations `. TOOL-dGroundRules-66 (cfdee9fd0) routed two readers, `print_audit` and `verb_dispatch`'s sibling set, through the new `read_open_passes`, which itself calls `read_pass_declarations` (`unattended.sh:13448`). So every reader still goes through the one shared derivation; only the literal count went stale. Shards 1, 3 and 5's other reds are inherited (identical at the run's base 3c2b69be4); shard 2 and 6 are green.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-70.md`, a Tier-1 micro-spec at order 24, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-69.md` follows. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. S1: respell the arm at `tools/unattended/unattended.test.sh:7591` so it grades what it claims, every reader going through the shared derivation, at HEAD's shape: the readers that call `read_pass_declarations` directly plus those that call `read_open_passes`, and `read_open_passes` itself calling `read_pass_declarations`. Measure each count at HEAD and give the expected values; keep the arm's label truthful (it says "five readers"). Decide whether one arm or two (a `read_open_passes` calls it arm) states it best, and keep the suite's `FLOOR_ASSERTIONS` and its shard floor consistent with any arm added.
2. AC1: the respelled predicates printed by a probe the pass may run (the arm's own `grep` pipelines copied into a scratch script over HEAD's `unattended.sh`), each matching its expected value. Red when: a reader is staged to parse the rows itself (e.g. one `read_open_passes` call replaced by an inline awk over the run-state file in a scratch copy). The suite is a self-test the pass may not run; the close's main loop runs shard 4 for the whole-suite observation.
3. §7 names the legs `python tools/check-spec-tokens.py --legs-for tools/unattended/unattended.test.sh` owes (read the guards join through `derive_guarded_legs`, not the first guard `--legs-for` prints), and a `New arm:` line only if an arm is added.
4. The main loop may fold a second item into this spec before commit: the hygiene suite's check-7 fixture (`check 7 emitted 0 findings, expected exactly 2`), if its base run shows TOOL-dGroundRules-9 caused it. Leave a clean seam for that (a separate S-item), but do not spec it now.
5. Keep every acceptance code span on one line; no acceptance line starts at column 0 with `AC<n>`; every AC bullet carries `Red when:`; no retirement word in §2; an untracked path sits in a fenced block.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Any other spec; `tools/unattended/unattended.sh`; the inherited reds of shards 1, 3, 5 and 7.

### Limitations
Measured by the main loop; logs in the run's scratchpad as `sr-ua*.log` and `sr-ua*-base.log`.

### Reuse
The arm block (e) at `tools/unattended/unattended.test.sh:7588`, and TOOL-dGroundRules-66's own arm region 4.
