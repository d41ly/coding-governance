**Serves:** research TOOL-dTendedCadence-1 TOOL-dTendedCadence-16

# dTendedCadence's specs against the parent specs revised by merge `362790f10`: a read-only cross-check

Node d, 2026-11-03, base `66c5b8dbf` (origin/main). dTendedCadence's spec run began at `7e48dac37`,
the parent of its first spec commit `0cde7925d`. That base holds every earlier re-ground merge
(`191ba7ab5`, `2bd5e10d4`, `933e67399`, `57bc3b918`, `0c0f3a183`, `7d0f5b756`) and the fork picks
`ccd1292ea`; `git merge-base --is-ancestor` puts each inside it and `362790f10` outside it. Between
`7e48dac37` and `66c5b8dbf` one commit, `66f7b8d32` (merge `362790f10`), moved any spec of the five
parents: TOOL-dWellOiledMachine-6, -41 and -58, which read TOOL-dTotalRecall-2 rev-7's owner-picked
holder verb. `git diff --name-only 7e48dac37 66c5b8dbf -- memory/builds/<parent>/spec/` names nothing
for dWitnessedBar, dRankedPlan, dIndexedDesign or dFurnishedOrders; dIndexedDesign has no re-ground
merge and its specs are byte-identical across the range. The owner asked for this pass on 2026-11-03
although an earlier triage said none was owed. This record is not an audit, and it owes no re-ground:
every assumption agrees.

**Counts:** 6 assumptions · 6 AGREES · 0 MISMATCH · 0 UNKNOWN UNTIL BUILT, over 6 specs (the 2
citation specs and 4 rule-wide candidates). No spec holds a MISMATCH, and no spec is revised.

## Method

- **Population by citation.** `grep -P` over `spec/*.md` for the four revised units, both
  `TOOL-<build>-<n>` and the bare `<build>-<n>`, plus continuation lists (tc16's `-6 S12 and -33
  S8`) and `wm`/`tr` aliases: 2 specs, 1 (wm6 S1) and 16 (wm6 S12). None cites wm41, wm58 or tr2, and
  none cites by `:<line>`.
- **Population by rule.** The revision applies one rule, RH: a build lease's `session`, `lease`-mode
  class and `epoch` are read through the one read-only holder verb over `read_claims` that tr2 §8 F6
  (a) picked, never through `--claims`' five fields, and no unit builds a second read or files a
  second ask (wm6:348-351). A probe for `--claims`, `read_claims`, `holder`, `epoch` and
  `refs/gov/leases` named 4 candidates: 2, 8, 50 and 69. The other hits (6, 9, 10, 48, 55, 59, 64,
  74) were judged by the main loop to name the policy value `lease-holder`, a lock's holder, a kit's
  version epoch, an epoch-seconds deadline or a spec's own §8 F6.
- **Reader.** One `gov-spec-reviewer` agent, read-only, by the brief
  [`2026-11-03-prompt-TOOL-dTendedCadence-1-parents-crosscheck`](../prompts/2026-11-03-prompt-TOOL-dTendedCadence-1-parents-crosscheck.md),
  its handoff beside it. Its return is
  [`2026-11-03-build-TOOL-dTendedCadence-1-crosscheck-returns`](2026-11-03-build-TOOL-dTendedCadence-1-crosscheck-returns.md).
- **The main loop** assembled the table below from the return's table by script and derived the
  counts from it. It changed no verdict.
- **Aliases:** `tcN:L` is line L of `spec/2026-11-01-spec-TOOL-dTendedCadence-N.md`; `wmN:L`, `trN:L`
  and `prN:L` of dWellOiledMachine's, dTotalRecall's and dPlacedRequest's spec N; all at `66c5b8dbf`.
- **What it does not check:** the rules the earlier re-grounds applied, all in this build's base;
  anything a parent's build run decides; the specs neither population reached. No skeptic re-ran the
  verdicts, and with no MISMATCH no writer re-read them.

## Why nothing moved

tc1 and tc16 rely on wm6 S1 (the supervisor walks a build by slug) and S12 (the `act-*` journal
classes), and `66f7b8d32` has no hunk in either. tc16 S1 also relies, uncited, on S6 and S7 journaling
`act-killed`, which rev-5 kept; it moved only where S6 and S7 read the epoch. The cadence program
learns its key from `GOV_CADENCE_KEY` (tc1 F3 (a)), rejecting a lease read-back for the same reason
tr2 F6 (c) and wm6 F4 (c) reject a second parser.

## Summary table

| # | Spec | Group | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | tc1 | A | The flow's executor is the supervisor. It asks `position.py <slug>`, so it walks a build keyed by slug, and no parent walks a cadence program keyed by (cadence, period). | cite | AGREES | tc1:156-158 "The flow's executor is the supervisor (TOOL-dWellOiledMachine-6 S1), which asks `position.py <slug>` … and so walks a build, keyed by slug" · wm6:45-50 "`python supervise.py run <slug> --epoch <n>` … the position engine's answer, read by running the loop kit's verb `python position.py <slug> --json`". S1 has no hunk in `66f7b8d32`. |
| 2 | tc1 | A | F2 (b): the supervisor walks only a build and has no key for a period, so `maintain.py` walks the items and ask TOOL-dTendedCadence-28 retires it. | cite | AGREES | tc1:293-296 "(b) the supervisor, which asks `position.py <slug>` and so walks only a build (TOOL-dWellOiledMachine-6 S1 …). (b) has no key for a period" · wm6:45-50, as above. |
| 3 | tc1 | A | The program never reads a lease holder. It learns its key from `GOV_CADENCE_KEY` (F3 (a)), and F3 rejects (c), reading back the lease and parsing the lease record. | RH | AGREES | tc1:301-304 "(c) reading back the lease this node holds … (c) parses a lease record format TOOL-dPlacedRequest-1 owns" · tr2:345-347 (c) "a second parser of the record its S2 keeps in `read_claims`", rejected; wm6:343-345 (c) "a second parser of the record `read_claims` is the one parser of". |
| 4 | tc16 | A | `act-launch`, `act-exit` and `act-killed` are journal classes wm6 S12 adds, each line keyed by `act=`. | cite | AGREES | tc16:38-39 "TOOL-dWellOiledMachine-6 S12 and -47 S4, the journal classes `act-launch`, `act-exit` and `act-killed`" · tc16:165 · wm6:141-143 "`act-launch`, `act-adopt`, `act-killed`, `act-exit`, `relaunch` and `limit-hold` join `JOURNAL_CLASSES` … each line keyed by `act=`". S12 is unchanged. |
| 5 | tc16 | A | S1's population: an `act-launch` with no later `act-exit` or `act-killed` is a missed reap, and "a supervisor that died mid-act leaves exactly this". The reconcile's kills close such lines with `act-killed`. | cite | AGREES | tc16:50-57 · wm6:100-106 (rev-5 S6): "every other live candidate has its tree killed through `run_kill_tree` … and is journaled `act-killed`". The revision moved only S6's epoch source (wm6:101-103, now the holder verb), not what it journals. The fence keeps `act-killed` too: wm6:110-111 "journal `act-killed` with `reason=fenced`". |
| 6 | tc16 | A | Under `lease-holder`, the period run (the holder itself) reads its own node-scoped rows and names as unread the nodes whose `<period>.<node>` node-pass lease key appeared in an earlier period but not this one. No foreign session or epoch is read. | RH | AGREES | tc16:101-107, tc16:339-345 "(a) reads only Maintain's own leases" · tr2:340-355 and wm6:97-111. The verb is needed only for `session`, `lease`-mode class or `epoch`, and the node is a segment of the lease key. |

## Rule-wide hits RH does not bind

The return's section 4 gives one line per hit: tc2's `lease-holder` and `every-session` read no
lease; tc8 and tc1's `run_cadence_period` take and release their own period lease; tc50 and tc69 cite
`read_claims` only as the fetch shape the maintain-record verb ports, over
`refs/gov/maintain-record/<key>`, not a lease.

## Parked for the owner

- **Parent text that looks wrong (not edited):** wm6's rev-5 cites tr2 §8 F6 as `tr2:337-354`, while
  F6 runs from tr2:340 to tr2:357.
