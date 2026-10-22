**Serves:** research TOOL-dTrueNorth-27

# Divergence brief — TOOL-dTrueNorth-27, the decision row near-matches TOOL-aSweptBar-6

## The prompt

> Its builder handed TOOL-dTrueNorth-27 back as a DIVERGENCE: §4's verbatim TOOL-dTrueNorth-28 row fails hygiene check 27, which near-matches it to TOOL-aSweptBar-6 at 0.238 over floor 0.125, so the row must name that id or carry a relation token. The builder's tested wording names it, and check 27 then reads "1 near match(es), 1 satisfied". It also reported that `memory/DECISIONS.md` sits in SHARED_RECORDS (`.unattended.conf`), so `--dispatch` refuses it, and that its S8 build scrubs GOV_REMOTE and GOV_DEFAULT_BRANCH from the deviation self-test's fixtures, which the spec does not state.

## The brief

### Goal
Revise `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-27.md` so §4's decision row passes check 27 and the spec states what its builder found. Author only: no product code, no commit, no gate.

### Items
1. §4's TOOL-dTrueNorth-28 row text replaces "under TOOL-aSparedSpawn-14's rule and the standing ruling" with "under TOOL-aSparedSpawn-14's rule, as TOOL-aSweptBar-6 raised it 318 -> 319, and the standing ruling"; every other byte of the row stays.
2. §4 says the row is appended at the end of `memory/DECISIONS.md`, the append-only file whose newest rows sit below its last heading, not "at the end of its TOOL section".
3. §4 and S6 say the row lands in its own `Pass: none` records commit, because `memory/DECISIONS.md` is a shared record that `--dispatch` refuses; AC10 stays as written.
4. S8 states that the deviation self-test holds GOV_REMOTE and GOV_DEFAULT_BRANCH out of its fixtures' environment, since a post-merge run can export GOV_REMOTE and the fixtures carry no remote; §7's deviation GOV_REMOTE arm names this.
5. The status header's rev rises by one, with a §9 line naming what disagreed and the change.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on this spec; §4, S6, S8 and AC10 agree; every `**Derived:**` line, backticked token, the H1 and the §8 RESOLVED marks survive; the spec stays under 49152 bytes.

### Gates
No gate runs in this pass; the close runs the spec's §7 legs.

### Non-goals
Any other spec; product code; deviation records 28 to 30; the two raises' figures; a criterion naming a gate leg, a `*.test.sh` run or the bar.
