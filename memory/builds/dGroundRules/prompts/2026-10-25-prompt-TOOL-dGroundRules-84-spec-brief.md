**Serves:** research TOOL-dGroundRules-84

# Spec brief — TOOL-dGroundRules-84, the shell sources and kit-path spellings this build left red on the bar

## The prompt

The close's bar pre-check at `cae57b1d8` failed ten legs, each green at the run's base `3c2b69be4`. A researcher triaged them into three units with disjoint write sets; the record is `memory/builds/dGroundRules/build/2026-10-25-build-TOOL-dGroundRules-84-research-bar-triage.md`, and this unit takes its legs 3, 4, 5, 7 and 9: the shell hygiene location probe, the twelve fork-on-builtin findings, the fixed-name temp, the 34 install-prefix spellings (plus the `check-install-prefix.sh` false positive on `limits:` operands) and the template-size harness arm A15. The per-leg output is in the run's scratchpad as `bar-reds-cae57b1d8.txt`.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-84.md`, a Tier-1 micro-spec at order 31, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-83.md` follows. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Re-derive every site in the research record's legs 3, 4, 5, 7 and 9 from the current tree (run each leg's checker read-only over the tree, since its output names the sites), and spec one fix per site in the record's shape, correcting the record wherever the tree disagrees and saying so. `tools/policy/policy-shim.sh` takes a registry row, not a conversion; the `spawn-idiom-sites.txt` rows (delete row for `agent-cap.test.sh`, add the shim row, lower the template-size var-pipe row) are this unit's.
2. The `check-install-prefix.sh` rule-3 operand split gains `:`. Before speccing it, run the candidate predicate over the real tree and record the offender set before and after: it must lose exactly `tools/policy/caps.toml:87` and nothing else. A new arm in `check-install-prefix.test.sh` pins it (`limits:.claude/skills/<kit>/X.md` counts nothing; a `HEAD:<kit>/x.sh` operand still counts) with a `New arm:` line.
3. Each acceptance criterion is a leg command the pass may run (the shell-hygiene, install-prefix and harness-arms checkers over the tree), never a self-test suite or the bar, and carries `Red when:` with a staged break that reds it by name. Unit -85 also writes `memory/project/spawn-idiom-sites.txt` rows for its own files and builds after this one; say so in §2.
4. §6 names the legs the touched files owe through `derive_guarded_legs`; adjust a floor or pinned count only where the change moves it, and say which.
5. §7 "Open questions" reads exactly `none`, with no bullet under it; any follow-up goes in the §8 revision log as prose. No line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet carries `Red when:`; keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no retirement word in §2; an untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Legs 1, 2, 6, 8 and 10 (units -85 and -86); `tools/memory-tree/check-memory-hygiene.sh` and `skills/session-kickoff/manifest-check.sh` fork costs; the govkit selftest's verdict (this unit edits `tools/govkit/selftest.py` for spellings only).

### Limitations
Measured by the main loop from the bar log at `cae57b1d8`.

### Reuse
Each lint's own printed remedy; the `adopt-branch-reconcile.sh:25` dirname form; the `run-held-wsl.sh` registry row's reason; `resolve_kit_dir`.
