**Serves:** research TOOL-dTrueNorth-29

# Spec brief — TOOL-dTrueNorth-29, the self-test reds the flagged bar found

## The prompt

> The flagged bar `GATE_FULL=1 GATE_SELFTESTS=1` at e583a7f42, run at VERIFYING after every unit closed and the plain bar went green, reds 9 legs. Their FAIL lines are excerpted in `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-29-flagged-bar.md`. Each leg was run again at the base 271aa59de in a scratch clone: five legs carry reds this build caused, the rest are inherited or flaky. One unit clears this build's reds before the close.

## The brief

### Goal
Author TOOL-dTrueNorth-29, one Tier-2 unit whose pass turns each red this build caused green, fixing the cause in code or in the suite's own fixture, never by loosening an assertion. Author only: no product code, no commit, no gate.

### Items
1. `spec-tokens self-test`: the six AC6 arms of `tools/check-spec-tokens.test.sh` (the block after its `# AC6 — the staged breaks` comment) write each broken copy of the checker to `$base`, a scratch directory with no `memory-tree` kit beside it. Since TOOL-dTrueNorth-27 S5 inlined `resolve_kit_dir`, such a copy refuses with `REFUSING — the memory-tree kit's design_lib.py does not resolve` before it reaches `CLAIM_CANARY`, so every arm reds. Place the copies where the inlined resolver finds the kit, keeping each arm's stated break. The suite's two `parity:` arms (the measure-legs ceiling of 500 s above the 300 s bound) are red at the base too and are not this unit's.
2. `row-grammar selftest`: the arm `no sibling engine in this kit imports corpus_ids or gen_build_index` finds `deviation_join.py:473`, the `import gen_build_index as gbi` TOOL-dTrueNorth-4 added in `read_population` for the binding classifier and the header grammar. Remove the sibling import (move what it uses to a module both may import, or read it another way the rule allows); the arm is not loosened.
3. `tier2-review self-test`: the arm `spec-audit: a spec that is also a subject is refused` passes `specs: ['s.md']` while the suite's `SPEC` fixture subject is now `memory/builds/dX/spec/s.md` (it was `s.md` at the base), so the harness's exact-path overlap check finds no overlap. Make the arm name the subject's own path; say whether the harness should also match a differently spelled path, and if so, specify it.
4. `unattended-build self-test`: `TN5-AC3 a caller subject with no id is refused naming the field` no longer sees `THROW unattended-build: subject 0's \`id\` is not a unit id`, and the suite executed 342 assertions against its floor of 343. Find whether the substitution the arm stages still matches the roster it edits, or the harness now names another field first, and fix the cause; account for the one unreached assertion.
5. `memory-hygiene self-test`, three findings, each red only at HEAD:
   - `tools/memory-tree/.memory-tree.conf.example` declares none of `DESIGN_BASELINE`, `DESIGN_NODES`, `DESIGN_RECORD`, `DESIGN_VIEW`, which the kit's modules read; declare each, blank, with its meaning, as the example declares the other keys.
   - two check 21 arms (`the audit-pin arm did not count the record an older harness wrote as exempt`, and `a record an older harness wrote, merged after the pinning harness landed, fails check 21`): the writer test no longer exempts the older harness's record in the suite's fixture, after TOOL-dTrueNorth-14, -19, -20 and -27 moved the harness reach to a stand-in resolver and a `harness/` directory. Fix the fixture or the reach so the exemption holds.
   - the partition arm: the unscoped run prints `check 29: coverage off` and `check 30: as-built view: off` lines that no scoped run prints. Make the scoped runs partition the unscoped run's lines again. At the base this arm reds only on the check 26 `cache hits` count, which differs between runs; that half is not this unit's.
6. Not this unit's, and the spec says so in §3: `measure-legs selftest` (red at the base), `pre-push self-test` (green alone at HEAD in a scratch clone; its one red arm, TOOL-aSparedSpawn-33 AC1's bar reuse, ran beside four neighbours), `foreign-prefix parity` (it re-runs every self-test, so it follows the others), and `govkit selftest` unless the base run says otherwise (the main loop adds it if so).
7. The spec carries `**Derived:** PLAY-dClosedLoop-2`, `order 12`, Tier-2, status OPEN, path `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-29.md`, and one AC per item that a pass can observe with a probe on the touched files: the suites themselves are the close's, and a unit runs none of them.
8. Write `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-29-deviation-31.md` for the unit itself: Departs from `dTrueNorth [roster]`, design-to-spec, builder discovery, additive, spec writer under author-recorded, `new unit TOOL-dTrueNorth-29`, Caused-by `PLAY-dClosedLoop-2`.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on the spec; every AC is a probe a pass can run; the record reads with no malformed field under `python tools/memory-tree/deviation_join.py`.

### Gates
No gate runs in this pass; the spec's §7 names the five legs and every leg its files trip.

### Non-goals
Any other spec; product code; loosening an assertion; a waiver row; the inherited reds of item 6; inside §6, an untracked file named by full path inside a backticked token.
