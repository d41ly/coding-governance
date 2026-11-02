# Spec brief — TOOL-dFoldedAudit-16: the flagged bar's own reds cleared

**Serves:** research TOOL-dFoldedAudit-16

## The brief

### Goal
Write TOOL-dFoldedAudit-16's spec at Tier-2: clear the two bar legs this build turned red, as `build/2026-11-02-build-TOOL-dFoldedAudit-16-1-first-bar.md` attributes them. Read `build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md` first; its tags bind. Header `order 160`, status OPEN. Commit nothing.

### Items
1. Shell hygiene (a fork spent on builtin work): `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'` reports five rows above their `memory/project/spawn-idiom-sites.txt` counts: `tools/unattended/unattended.sh` `pure-fn-subst` 41 to 43; `tools/unattended/unattended.test.sh` `cat-file` 17 to 24 and `printf-subst` 23 to 25; `tools/workflows/unattended-build.test.sh` `printf-subst` 66 to 67 and `var-pipe` 62 to 63. Convert each site this build added to the no-fork form the row names. Where a site must keep its substitution, as that driver row says check 28 requires for `declared_list` and `declared_scalar`, raise that one row by the count with the reason in place. The registry rows are shrink-only; name every raise in §4.
2. Drift-audit records: `cutoff_keys_armed = 37 (pin 36)`. Raise the pin in `tools/drift-audit/drift_signals.py` to 38, with a comment line in the existing history giving both keys, `SPEC_SUPERSEDE_CUTOFF` (TOOL-dFoldedAudit-4) and `SPEC_FOLD_CUTOFF` (TOOL-dFoldedAudit-7, armed at the close), and the decision row TOOL-dFoldedAudit-16, which the main loop has already landed.
3. Acceptance: the sh_hygiene command above prints no finding for those three files, and `python tools/drift-audit/drift_report.py --check` prints no `cutoff_keys_armed` line. Each as a criterion; the suite arms already exist.

### Acceptance
The spec carries order 160, each item as a Scope line with an observation, and §7 names `shell hygiene (a fork spent on builtin work)` and `drift-audit records`.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass.

### Non-goals
No other leg, no behaviour change, no write outside this build's `spec/`.
