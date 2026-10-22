**Serves:** research TOOL-dTrueNorth-12

# Divergence brief — TOOL-dTrueNorth-12, a fixture design that keeps plants composing

## The prompt

> Its builder handed TOOL-dTrueNorth-12 back as a DIVERGENCE: S3 and §4 "The fixture design" give the fixture's own design two builds with four clauses, while TOOL-dTrueNorth-4 §4 "The fixture", which this unit leaves in force, says every plant is its own unit, clause or row, so plants compose. At HEAD eleven fixture roles each move a separate clause; four clauses force eight plants to share one, and the builder measured the composed run falling from 29 members to 22 and printing a false late-record finding.

## The brief

### Goal
Revise `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-12.md` so its fixture design agrees with TOOL-dTrueNorth-4 §4's compose rule, the run's ruling (a): the fixture's own `[chain]` holds one clause per clause-moving role, at least eleven, and the spec names which role moves which clause. Author only: no product code, no commit, no gate.

### Items
1. S3 and §4 "The fixture design": the fixture design carries at least eleven clauses across dFixA and dFixB (for example `cl-dFix-0001` to `cl-dFix-0011`), and a table maps each clause-moving role to its own clause: the base's owner amendment, the `baseline` plant, the `clause` plant, the six APPROVER_PLANTS and the two RISK_PLANTS, as `tools/memory-tree/deviation_join.py` names them at HEAD (read it; do not trust this list's count over the code).
2. The fixture's units, `RUN.md` and records move from `memory/builds/dTrueNorth/` to a fixture build folder named in the fixture design, because the chain builds are the view's Build column and a spec outside them is no chain-build spec. State the folder and what moves.
3. S2's live refusal resolves the gen-region strip up front in the live join; today `read_gen_strip` resolves only when a revision is graded. State where the resolution moves.
4. The record-late arm reaches the host through `routed_commits.check_routed_commits`, so the identity strip S2's skip runs under reaches that live host path too, not only the self-test's call into the fixture. State it in S2 or S3, whichever owns it.
5. AC lines that observe the composed run state its member count, derived by the fixture's own count, and that it prints no late line but record-late's.
6. The status header's rev rises by one, with a §9 line naming what disagreed and the ruling.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on this spec; S3, §4 and every AC agree with TOOL-dTrueNorth-4 §4's compose rule; every `**Carries:**` and `**Derived:**` line, backticked token, the H1 and the §8 RESOLVED marks survive.

### Gates
No gate runs in this pass; the close runs the spec's §7 legs.

### Non-goals
TOOL-dTrueNorth-4's spec and any other spec; product code; a criterion naming a gate leg, a `*.test.sh` run or the bar; inside §6, an untracked file named by full path inside a backticked token (quote it inside a command, or write it bare).
