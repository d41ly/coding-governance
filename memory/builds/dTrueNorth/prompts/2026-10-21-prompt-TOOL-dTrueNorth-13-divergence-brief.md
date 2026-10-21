**Serves:** research TOOL-dTrueNorth-13

# Divergence brief — TOOL-dTrueNorth-13, one rule for a missing `Reviewed:` path

## The prompt

> Its builder handed TOOL-dTrueNorth-13 back as a DIVERGENCE: §2 S4 and §5 give opposite rules for a `Reviewed:` path with no blob at HEAD, and AC4 is silent on it.

## The brief

### Goal
Revise `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-13.md` so it states one rule for a path on a spec-audit record's `Reviewed:` line that has no blob at HEAD, the run's ruling (a): such a path makes EVERY id of that record owe a pin, exactly as a record with no `Reviewed:` line does. Author only: no product code, no commit, no gate.

### Items
1. §2 S4 states the missing-path rule. Today it says an id owes a pin only when a named path is a spec file whose H1 defines that id, so a missing path never makes an id owe one.
2. §5's "error / empty / loading states" line agrees with S4.
3. AC4's fixture commits the two `build/` files its design-only record names, so that record still prints no P row, and AC4 gains a missing-path case, a record naming one path absent at HEAD, that prints a P row for every id the record serves.
4. Scope states that this unit moves the review suite's spec-audit fixtures to spec-shaped paths. About 30 fixtures in `tools/workflows/tier2-review.test.sh` use paths with no `builds/<slug>/spec/` segment (`a.md`, `s.md`, `m.md`, `u.md`, `v.md`, `one.md`, `two.md`, `three.md`) and carry `rev`, so under S1 they become design subjects and are refused, and the pin arms near its line 225 would stop refusing. The `renderAuditBinding` arm near line 239 passes subjects with no `path`. `tools/workflows/unattended-build.test.sh` near line 816 (`MT_ARGS`) runs the real harness with subject path `s1` plus a `rev`. Both suites are already in Files touched.
5. The stale line citations are refreshed: the review harness's 1767-1768 is now 1799-1800, the build harness's 2499 and 2507-2508 are now 2550 and 2566-2567. Verify each against the tree before writing it.
6. §3 Non-goals says the build harness's own caller-subject check, which requires `id` and `rev` on every subject, is unchanged by this unit.
7. The status header's rev rises by one, with a §9 line naming what disagreed and the ruling.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on this spec; S4, §5 and AC4 each state the same missing-path verdict; every `**Carries:**` and `**Derived:**` line, backticked token, the H1 and the §8 RESOLVED marks survive.

### Gates
No gate runs in this pass; the close runs the spec's §7 legs.

### Non-goals
Any other spec; product code; a criterion naming a gate leg, a `*.test.sh` run or the bar; inside §6, an untracked file named by full path inside a backticked token (quote it inside a command, or write it bare), since the spec-tokens paths join reads every live spec at each `--dispatch`.
