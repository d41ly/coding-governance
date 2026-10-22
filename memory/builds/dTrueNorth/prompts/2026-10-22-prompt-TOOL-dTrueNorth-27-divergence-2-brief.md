**Serves:** research TOOL-dTrueNorth-27

# Divergence brief 2 — TOOL-dTrueNorth-27, the decision row over check 7's cap

## The prompt

> Its second builder handed TOOL-dTrueNorth-27 back as a DIVERGENCE: §4's verbatim TOOL-dTrueNorth-28 row is 478 characters and hygiene check 7 caps every `memory/DECISIONS.md` entry line at 300, so the records commit was refused. The main loop has since committed a 298-character row at 53321feef, ahead of the pass as the builder ordered it, and check 27 reads it as 1 near match, 1 satisfied. The builder also found that the GOV_REMOTE and GOV_DEFAULT_BRANCH hold sits in `run_plant_arms`, which both `run_selftest` and routed_commits.py's selftest call, not in `run_selftest`.

## The brief

### Goal
Revise `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-27.md` so §4 agrees with the row already committed and S8 names where the hold lives. Author only: no product code, no commit, no gate.

### Items
1. §4 "The decision row" quotes the row exactly as the last line of `memory/DECISIONS.md` at 53321feef reads, says it landed in that `Pass: none` records commit ahead of the pass because check-arms refuses a REFUSAL_CEILINGS token whose decision no row holds, and says the retirement review and the two key names live in deviations 29 and 30, not in the row; S6 and the Files-touched entry for `memory/DECISIONS.md` say the pass does not edit that file.
2. S8 and §7's deviation arm line name `run_plant_arms` as where the two variables are held out, so both selftests that call it are covered.
3. The status header's rev rises by one, with a §9 line naming what disagreed and the change.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on this spec; §4's quoted row equals the file's last line byte for byte; AC10 is unchanged; every `**Derived:**` line, backticked token, the H1 and the §8 RESOLVED marks survive; the spec stays under 49152 bytes.

### Gates
No gate runs in this pass; the close runs the spec's §7 legs.

### Non-goals
Any other spec; product code; `memory/DECISIONS.md`; deviation records 28 to 30; a criterion naming a gate leg, a `*.test.sh` run or the bar.
