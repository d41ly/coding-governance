# TOOL-aShardedFloor-2 — the shard contract, and the driver selftest split by it

**Status:** OPEN · rev-1 · 2026-08-21 · node a · Tier-2 · base 36d0ad3b · streams tooling

## 1. Goal

`unattended driver selftest` IS the bar's floor. Split `tools/unattended/unattended.test.sh` into two
bar legs so the floor halves, and define — once, here — the shard contract its sibling adopts
verbatim. Discharges `TOOL-aPacedTurnstile-8` jointly with `TOOL-aShardedFloor-3`; neither alone
buys anything worth having.

## 2. Scope (IN)

- **S1** — a `--shard i/n` FLAG on the script, parsed above the first `mktemp -d` so a refusal costs
  ~50 ms and creates nothing. Parsed as a flag, never position-read: the runner execs the manifest's
  argv list, so `$1` is the literal `--shard`.
- **S2** — two guarded contiguous regions, wrapped WITHOUT reindenting. Four inserted lines. The
  arms meta-gate scans lines and skips comments, so an unindented wrapper leaves every arm signature
  byte-identical and the armed floor untouched.
- **S3** — six hoisted definitions so region 2 can rebuild the fixture epochs region 1 establishes.
  The set and its call sites are named in the research record and are not restated here.
- **S4** — a mode-selected assertion floor. Without it every shard leg reds forever on the
  unsharded floor.
- **S5** — two manifest rows on the same script with byte-identical `guard` arrays and the same
  `chunk`. Divergent guards inside a pair let a diff run one half and skip the other while the
  summary reads green.
- **S6** — the CONTRACT, written in the script as prose a sibling can copy: flag grammar, refusal
  set, floor selection, and the cover arm that proves no shard index went missing.
- **S7** — gov-canary arms: complete cover over shard indices, and the reverse direction — a script
  declaring no shard arity may not be called with `--shard`, and one that declares it must be.

## 3. Non-goals (OUT)

No physical file split — refuted by a gate, not by taste: the arms meta-gate maps one gate to exactly
one sibling test and `.memory-tree.conf` pins its armed floor. That pin DECIDES the mechanism. No
reindentation of the wrapped bodies. No third shard: past two the bar is throughput-bound at ~766 s
and further splitting buys exactly zero. No per-arm hash assignment — the file has fixture epochs
that must run contiguously.

## 4. Design

§"Unit A" of [the research record](../build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md), including
the seam line, the six hoists, every gate pin, and the five staged breaks. Three things bind and are
repeated here because the unit fails on exactly these:

**The seam is MEASURED, not argued.** Both halves were built and run in a scratchpad before this spec
existed: whole file `PASS (398)`, shard 1 `PASS (196)` at 242 s, shard 2 `PASS (206)` at 145 s, and
`196 + 206 = 398 + 4` where the 4 are prologue arms both shards pay. Duplication costs ≈ 4.2 s of
leg-seconds, which refines the report's ~2.75 s per-split estimate upward for this split.

**Leg naming is not cosmetic, and the warm-ledger case is a REGRESSION rather than a null.** The
dispatch hint keys an unknown leg name at `0.0` and every known leg at a negative, so on a warm
ledger a NEW name sorts DEAD LAST — a floor shard starting after ~87 others. Keep shard 1's existing
name so it inherits its warm row, and give shard 2 a name differing in a letter, never a
digit-bearing parenthetical, which the descriptor grammar refuses.

**The hoist is behaviour-preserving only if the calls sit exactly where the inline code sat.** A call
a few blocks off silently changes what every downstream arm sees, and those arms still PASS. The
assertion count cannot see it; AC1, AC7 and AC8 can.

## 5. Production-readiness checklist

- security — N/A: a test harness argument; both shards build their own scratch repo and bare origin.
- perf / scale — the entire point. Floor halves; leg-seconds rise ~4.2 s.
- a11y · i18n — N/A.
- error / empty / loading states — five argument refusals, each firing before any temp dir exists.
- observability — each sharded run prints which region it ran and that the other was NOT exercised.
- risks — the warm-ledger sort penalty, and a future region-2 arm depending on region-1 state that
  passes the unsharded run a developer habitually types and reds only on the bar. The header text is
  the only mitigation for the second; there is no gate for it, and the spec says so rather than
  implying coverage it does not have.
- testing + left-shift gates — two new gov-canary arms, both directions.
- migration / rollback — revert is one manifest edit plus four lines; the ledger self-heals in a bar.
- user docs — N/A: internal harness.

## 6. Acceptance criteria

- **AC1** — the no-argument run exits 0 at `PASS (398 assertions)` with output byte-identical to the
  pre-change run.
- **AC2** — `--shard 1/2` exits 0 with n ≥ 196 and `--shard 2/2` with n ≥ 206, and the identity
  `FLOOR_SHARD_1 + FLOOR_SHARD_2 = FLOOR_ASSERTIONS + 4` is asserted in EVERY mode. This is a
  tripwire over three authored constants, not a measurement, and its header says so.
- **AC3** — each sharded run of `tools/unattended/unattended.test.sh` prints which region it ran and
  that the other was not exercised.
- **AC4** — the header of `tools/unattended/unattended.test.sh` states what a sharded run does NOT
  check.
- **AC5** — `bash tools/check-testsuite-counts.sh` green with no new waiver row.
- **AC6** — `python tools/memory-tree/check-arms.py --check` green with the armed floor unchanged and
  no new row in `memory/project/unarmed-branches.txt`.
- **AC7** — all five staged breaks RED with a message naming the defect, and green on unstage. The
  break that matters most is #2, the silent-ignore shape live TODAY: the script parses no argv, so
  two `--shard` rows would both run the full suite — bar green, wall unchanged, leg-seconds doubled.
- **AC8** — in both modes `git rev-parse "$BCP^{tree}"` is identical between the unsharded run and
  `--shard 2/2`, failing with both values named. The TREE, never the commit, whose parent and message
  differ by construction. This is the only check that distinguishes a shard that REPRODUCED the
  fixture epoch from one that merely survived it.
- **AC9** — `--shard 2/2` and the unsharded suite produce byte-identical output over the region-2
  slice, captured per arm.
- **AC10** — `python tools/govkit/govkit.py selfcheck` green; descriptor rows match the manifest.
- **AC11** — codebase-map coverage + freshness green in BOTH directions, generated artifacts
  regenerated in the same commit — `memory/map/generated/inventories.json` and
  `memory/map/generated/MAP.md`.
- **AC12** — both shard legs' in-pool durations, read from `<git-dir>/gate-run/<id>/*.leg`, are
  below the ~766 s throughput bound.
- **AC13** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` green, with the charter's measured pair
  and both halves of its gov-canary arm moved in the SAME commit as the last span-moving landing.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, full at the push boundary. Named legs: `unattended driver
selftest` (both shards), `unattended gate selftest`, `run-gates gov canary`, `run-gates canary`,
`testsuite counts`, `harness arms`, `govkit selfcheck`, `codebase-map coverage + freshness`,
`kickoff-manifest ratchet`, `memory hygiene`. This unit adds gov-canary ARMS, not a leg.

## 8. Open questions

none — the forks this unit had are RESOLVED and marked here. (1) *Flag in `argv` or a new manifest
key?* `argv`: the manifest key set is pinned and a new key would move that pin for nothing.
(2) *Shard 1's name?* Keep the existing name and append a letter to shard 2 — the warm-ledger sort
penalty then falls on the smaller shard only, and map churn halves. Resolver: this session, under
the standing authority to settle forks the specs already state; the alternative (symmetric renaming)
is tidier and takes the penalty on both, and is recorded here so the choice is visible rather than
silent. (3) *Does `TOOL-aPacedTurnstile-8` split into two ids?* It does not: one row, discharged
jointly by this unit and `TOOL-aShardedFloor-3`, because they must land together to buy anything.

## 9. Revision log

- rev-1 · 2026-08-21 · initial, from the design pass at
  [`build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md`](../build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md).
  A skeptic refuted the first brief's mechanism and the corrections are folded in: the flag must be
  PARSED not position-read (the original would have made both legs exit 2 on every bar forever), the
  hoist set is six and not five, the assertion floor must be mode-selected or every shard leg reds
  forever, and the warm-ledger dispatch case is a regression rather than the null the brief assumed.

## 10. Reuse audit

**No existing seam fits, and the evidence is a gate rather than a search.** There is no shard
mechanism anywhere in this repo to extend:
`python tools/codebase-map/reuse_lookup.py "split one test suite into two independently runnable halves selected by an argument"`
returns no seam that partitions a suite, and the map's own refusal applies again — bash has no symbol
extractor, so a bash seam would not surface and the hand check is what decides. The hand check found
the constraint instead of a seam: `tools/memory-tree/check-arms.py` maps one gate to exactly one
sibling test and `.memory-tree.conf` pins that pair's armed floor, which REFUTES the physical-split
mechanism outright. So the contract this unit writes IS the seam, and
`TOOL-aShardedFloor-3` is its second instance — which is why the contract is stated as prose a
sibling copies rather than invented twice.

**Recall terms used:**
`python tools/memory-recall/query.py "has this repo decided before how to split a long gate leg, and what constrains a test suite growing a second manifest row" --terms "shard gate leg manifest argv floor assertions armed branches sibling test suite split selftest chunk selftests guard"`
