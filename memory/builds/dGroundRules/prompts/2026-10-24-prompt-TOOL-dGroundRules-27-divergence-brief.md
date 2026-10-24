**Serves:** research TOOL-dGroundRules-27

# Divergence brief — TOOL-dGroundRules-27, a snapshot already built and a rule another unit owns

## The prompt

> Its builder probed TOOL-dGroundRules-27 at HEAD 7599845c2 and handed it back as a DIVERGENCE before writing anything. S4/AC4 forbid any line of `tools/policy/check_policy.py` outside `run_govkit` from spelling the deployer's file name, but `budgets-ships-join` (TOOL-dGroundRules-23) loads the source's deployer in-process at :3479 through importlib, and its message at :3489 spells the name; TOOL-dGroundRules-34 S7's `resolve_govkit` is the unit that sanctions that load. §1, §4 Evidence and S2/S3 are stale: units 25 and 26 already put `legacy-homes-withheld-install` and `census-default-adopter` on the source snapshot through `build_install_target` and `run_install_verb` (:1067), so AC1 and AC2 and the `New arm:` line are green at HEAD and cannot tell this unit built. §10 says no helper runs the deployer for a fixture, but `run_install_verb` is that seam. §4 Rollout cites `tools/unattended/unattended.sh:13845-13880` for `--dispatch` condition 1, now at :13966. The small build left is: `run_govkit(snapshot_root, source_root, *argv)` replacing `run_install_verb`, refusing equal resolved roots as WRONG naming the root and `build_source_snapshot`, taking over the deployer-path check and derivation, and rewording the docstrings and messages that spell the file name.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-27.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. S4 and AC4 scope the rule to deployer runs: no line outside `run_govkit` runs the deployer as a process or derives its path for a run; `budgets-ships-join`'s in-process load is named as the one exception until TOOL-dGroundRules-34 S7's `resolve_govkit` sanctions it, and AC4's grep excludes that function's lines by name. Building `resolve_govkit` here is refused: it is TOOL-dGroundRules-34's scope.
2. §1, §4 Evidence, S2 and S3 say the two cases already run from the snapshot at HEAD (units 25 and 26) and that this unit's change is `run_govkit` replacing `run_install_verb`, its equal-root refusal, and the moved path check and derivation; S2/S3 say what remains for each case, or that it already holds.
3. §10 names `run_install_verb` as the seam `run_govkit` replaces, so no second helper is added.
4. AC1 and AC2 are restated so they observe this unit's change, and the `New arm:` line's break targets `run_govkit`'s refusal (for example `run_govkit` staged to accept equal roots, so a case run against the source root passes when it must WRONG); AC3 stays the refusal probe.
5. §4 Rollout cites `--dispatch` condition 1 by its text or symbol, not by line.
6. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; introduce no retirement word in §2; no path inside a code span is followed by a quote or other punctuation, and a fixture-relative path carries the target placeholder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The builder's probes at 7599845c2 stand: both fixtures print `0 wrong` at HEAD from a snapshot, and the govkit citations :7533, :7882-7884, :6706 and :13238 hold.

### Reuse
`run_install_verb` at `tools/policy/check_policy.py:1067` is the seam.
