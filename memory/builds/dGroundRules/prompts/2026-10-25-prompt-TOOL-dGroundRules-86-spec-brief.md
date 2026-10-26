**Serves:** research TOOL-dGroundRules-86

# Spec brief — TOOL-dGroundRules-86, the records and runbook this build's code left stale

## The prompt

The close's bar pre-check at `cae57b1d8` failed ten legs, each green at the run's base `3c2b69be4`. The researcher's triage, `memory/builds/dGroundRules/build/2026-10-25-build-TOOL-dGroundRules-84-research-bar-triage.md`, hands this unit legs 1, 2, 8 and 10:

- the kickoff-manifest ratchet (`memory/guides/SESSION-KICKOFF.md` has 20 watched commits since `last-body-change: f221e1135`; §B lines 171-172 still call raising the template ceiling an owner decision, while since `69aa76517` the ceiling is read through the policy kit's `budgets.<cap>`);
- memory hygiene check 25 (`memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md` S30 **Readers:** names `loadDeclaredCap`, which `2ebafd441` removed) and check 23 (the TOOL-dGroundRules-34 ledger's AC32 answer lacks the token `gen:build-order`);
- method carriers (`tools/policy/caps.toml:63,67` and `tools/policy/check_policy.py:3488,3757` need rows in `memory/project/method-carriers.txt`);
- govkit runbook parity (the registry entry `policy` has no `<!-- govkit:entry policy -->` section in `WIRE-INTO-PROJECT.md`).

The main loop ruled that this unit revs dSafePassage-26 (DEFERRED, rev-4), a live spec of another build, because this build's TOOL-dGroundRules-10 removed the symbol its Readers clause names; the rev touches only that clause and its §8 log.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-86.md`, a Tier-1 micro-spec at order 33, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-83.md` follows. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Re-derive each leg's findings by running its checker read-only over the current tree, and spec one fix per finding, correcting the research record wherever the tree disagrees.
2. The manifest re-audit reads §B whole against the tree, not only the one stale claim the researcher found, and follows the stamp rule the manifest itself states (every stamp that rule names, not only `last-body-change`). This unit builds after -84 and -85, so its stamps name the commit the builder audits at, not a sha fixed in the spec.
3. The dSafePassage-26 rev points the Readers clause at the code that reads `FANOUT_CAP` now (`read_legacy_fanout` and `LEGACY_FANOUT` in `tools/policy/policy.py`; confirm by grep), bumps its rev and logs why in its §8, and leaves its status as it is.
4. The runbook section spells kit paths only as `<tool-root>/…` (the runbook sits in the install-prefix population) and follows an existing `govkit:entry` section's shape.
5. Each acceptance criterion is a leg command the pass may run (the manifest ratchet, memory hygiene, method carriers, the govkit runbook-parity check), never a self-test suite or the bar, and carries `Red when:` with a staged break that reds it by name. §6 names the legs the touched files owe through `derive_guarded_legs`; the runbook-parity pin of 18 moves only if the count does, and the spec says which.
6. §7 "Open questions" reads exactly `none`, with no bullet under it; any follow-up goes in the §8 revision log as prose. No line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet carries `Red when:`; keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no retirement word in §2; an untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Legs 3-7 and 9 (units -84 and -85); any other clause of dSafePassage-26; the policy kit's code.

### Limitations
Measured by the main loop from the bar log at `cae57b1d8`.

### Reuse
The TOOL-dTrueNorth-27 re-audit at `d85890512`; the `tools/template-size-limits.txt` row of `method-carriers.txt`; an existing `govkit:entry` runbook section.
