**Serves:** research PLAY-dClosedLoop-1

# Phase 0: the schedule script's red tests, re-run at the branch tip

Dispatch 237's record, from `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-brief-schedule.md`. It re-runs the
thirteen red-test rows of P0.4 (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-0]`), the done
rule as `tree_state` applies it, and the plain run, against `build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`.
The script, v2, the plan and every other record are unchanged.

## [verdict]

- **Twelve rows MATCH**: rows 1 to 8 and 10 to 13.
- **Row 9 DIFFERS.** Its figure and its node set match, but the note the row names is never printed. `run()` builds
  the note for the "a and d alone" figure, and `main()` discards it (script lines 373-374). The docstring's line 27
  also promises it is printed.
- **The done rule's five arms MATCH.** Two inputs its paragraph does not decide both read done: a clause released by a
  `**Deferred:**` line, and a clause carried by one `part 1/2` line only. They are recorded under `[done-rule]` as
  open questions for the owner, not as differences.
- **The plain run** exits 0, with makespan 271 and "a and d alone" 273.

## [setup]

- **Script.** Blob `bc733fd33f55` at the branch tip `4bfca2c74`, run from disk in the clone.
- **Tree.** A `git clone --shared` of the `branch/p0-schedule` worktree at `4bfca2c74`, in the builder's scratch
  folder. Before each case the clone was reset to `4bfca2c74` and cleaned, and every ref under `refs/gov/remote/runs/`
  was deleted. Spec plants and the v2 edit were committed in the clone, so `--ref HEAD` reads them. No fetch, no push
  and no `unattended.sh --claims` ran anywhere.
- **Claims.** Each one is planted where the docstring says the script reads it (line 19): a commit on the empty
  tree under `refs/gov/remote/runs/<slug>`, its message in the form `write_claim` builds
  (`tools/unattended/unattended.sh:2411-2412`). "Now" is the plant time, 2026-10-20T17:34:07Z, seconds before each
  run. "Stale" is two hours earlier: 7200 s against `RESUME_STALE_BOUND="5400"` (`.unattended.conf:95`).
- **Specs.** Each planted spec is `memory/builds/<slug>/spec/2026-10-20-spec-plant-<n>.md`. It holds an H1
  `# <slug> plant-<n>`, the status header `**Status:** <TOKEN> · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7
  · streams playbook` (TEMPLATE-SPEC:58; left out where an arm says so), and its body lines, each part after a blank
  line. A carry line is `**Carries:** <id>@00000000 whole`, the form in `carries.py:8`. The hash is a placeholder,
  because the script's `CARRY` pattern (line 73) reads the id and never the hash. The file names avoid the unit-id
  shape, since the script reads every `.md` under `spec/` whatever its name (lines 120-121).
- **Command.** `python <script> --ref HEAD` from the clone's root, unless a row names another command. `python` is
  `python3` 3.14.5, as `tools/lib/resolve-python.sh` resolves it. stderr was empty in every case. Where a block shows a
  `tree_state` line, that line is not the script's output: it is a direct call of the script's own
  `tree_state("HEAD", ids)` on the same commit, imported from the clone.

## [rows]

### Row 1: `cl-dClosedLoop-0509` dropped from v2

**Row:** Exit 1: "holds 22 builds and 508 clause ids … not 22 and 509".

**Plant:** in v2 (`build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`), line 1783, which is dTendedCadence's
`[chain]` row, the one `; `-separated unit that carries the id was removed, its leading `; ` included:

```text
memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md: removed the one '; ' unit carrying the id, 534 chars:
; `maintain.on-breach`'s three values at `maintain.file`: `file-ask` filing the ask into Plan's triage, `red-leg` filing nothing and registering a leg at Test's leg-pack point that reads the newest maintenance record offline, as distribution's currency leg reads its own record, red while an offender stands over its pin, and `report` filing nothing and sending the maintenance record through the notification adapter, each value seen on its planted offender (the owner's FK-5-5, the whole-design audit's B5-F11) `cl-dClosedLoop-0509`
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 1

```text
schedule: v2's [chain] at HEAD holds 22 builds and 508 clause ids (508 by the '; ' split), not 22 and 509; the schedule is derived from nothing
```

**MATCH.** Exit 1 with the row's words. Both counts read 508, the ids and the `; ` split.

### Row 2: two dTrueNorth specs carrying `cl-dClosedLoop-0001` to `-0006`, at `DEFERRED`

**Row:** Its whole run still starts at 0: a whole run is done only when it lands.

**Plant:**

```text
memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-1.md:
# dTrueNorth plant-1

**Status:** DEFERRED · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0001@00000000 whole
**Carries:** cl-dClosedLoop-0002@00000000 whole
**Carries:** cl-dClosedLoop-0003@00000000 whole

memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-2.md:
# dTrueNorth plant-2

**Status:** DEFERRED · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0004@00000000 whole
**Carries:** cl-dClosedLoop-0005@00000000 whole
**Carries:** cl-dClosedLoop-0006@00000000 whole
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
tree_state (spec done, build done): {"dTrueNorth": [true, false]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 1, builds landed 0
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | a 0-7, slack 0 |
  a: whole dTrueNorth at 0
  0 a whole dTrueNorth · 7 a spec dGroundRules · 11 a build dGroundRules · 11 d spec dSafePassage
```

**MATCH.** The spec phase reads done and the build phase does not, so dTrueNorth's whole run is `a 0-7`, the first
start.

### Row 3: the same specs at `CLOSED`

**Row:** dTrueNorth reads `done`; dGroundRules' spec run starts at 0.

**Plant:** row 2's two files with `DEFERRED` replaced by `CLOSED`:

```text
memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-1.md:
# dTrueNorth plant-1

**Status:** CLOSED · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0001@00000000 whole
**Carries:** cl-dClosedLoop-0002@00000000 whole
**Carries:** cl-dClosedLoop-0003@00000000 whole

memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-2.md:
# dTrueNorth plant-2

**Status:** CLOSED · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0004@00000000 whole
**Carries:** cl-dClosedLoop-0005@00000000 whole
**Carries:** cl-dClosedLoop-0006@00000000 whole
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
tree_state (spec done, build done): {"dTrueNorth": [true, true]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 1, builds landed 1
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | done |
| dGroundRules | Policy | dTrueNorth | 11 | a 0-4, slack 0 | a 4-11, slack 0 |
  a: spec dGroundRules at 0
  0 a spec dGroundRules · 4 a build dGroundRules · 4 d spec dSafePassage · 11 d build dSafePassage
```

**MATCH.** dTrueNorth's cell reads `done`, and dGroundRules' spec run is `a 0-4`.

### Row 4: a cached `live` claim of user `agent5` on dGroundRules, beat now

**Row:** Its spec run is pinned to node b at 0, and its build run goes to a full-pace node.

**Plant:**

```text
refs/gov/remote/runs/dGroundRules -> 7e8f62c6d4ee, message:
gov-claim dGroundRules

slug: dGroundRules
node: agent5
host: DESKTOP-3J1O6CD
session: absent
keepalive: absent
status: live
lease-utc: 2026-10-20T17:34:07Z
beat-utc: 2026-10-20T17:34:07Z
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
claims cached on chain builds: dGroundRules live on b
| dGroundRules | Policy | dTrueNorth | 11 | b 0-15, slack 0 | a 15-22, slack 0 |
node b: busy 177 of 275 (64%), work 44 of 510 units, 7 runs: 7 spec, 0 build, 0 whole
  b: spec dGroundRules at 0
  0 a whole dTrueNorth · 0 b spec dGroundRules · 15 a build dGroundRules · 15 d spec dSafePassage
```

**MATCH.** The spec run is `b 0-15` and the build run is `a 15-22`, on full-pace node a.

### Row 5: a claim naming user `nobody`

**Row:** Exit 1: the fleet names no such node.

**Plant:**

```text
refs/gov/remote/runs/dGroundRules -> 8e6e4d5d0f90, message:
gov-claim dGroundRules

slug: dGroundRules
node: nobody
host: absent
session: absent
keepalive: absent
status: live
lease-utc: 2026-10-20T17:34:07Z
beat-utc: 2026-10-20T17:34:07Z
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 1

```text
schedule: the claim on dGroundRules names node user 'nobody', which tools/playbook/fleet.toml does not
```

**MATCH.** Exit 1, naming the user and the fleet file that lacks it.

### Row 6: a cached `live` claim of user `d41ly` on dGroundRules, beat older than `RESUME_STALE_BOUND`

**Row:** Printed "stale on d: take over per [coordination]", left unpinned, and its table cell marked "take over
(stale)"; the same claim with a fresh beat is pinned to d.

**Plant, stale:**

```text
refs/gov/remote/runs/dGroundRules -> 585d66d6598f, message:
gov-claim dGroundRules

slug: dGroundRules
node: d41ly
host: absent
session: absent
keepalive: absent
status: live
lease-utc: 2026-10-20T15:34:07Z
beat-utc: 2026-10-20T15:34:07Z
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
claims cached on chain builds: none live or held; other: dGroundRules stale on d: take over per [coordination]
| dGroundRules | Policy | dTrueNorth | 11 | a 7-11, slack 0, take over (stale) | a 11-18, slack 0 |
  0 a whole dTrueNorth · 7 a spec dGroundRules · 11 a build dGroundRules · 11 d spec dSafePassage
```

**Plant, fresh:**

```text
refs/gov/remote/runs/dGroundRules -> 51ada6908494, message:
gov-claim dGroundRules

slug: dGroundRules
node: d41ly
host: absent
session: absent
keepalive: absent
status: live
lease-utc: 2026-10-20T17:34:07Z
beat-utc: 2026-10-20T17:34:07Z
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
claims cached on chain builds: dGroundRules live on d
| dGroundRules | Policy | dTrueNorth | 11 | d 0-4, slack 0 | a 7-14, slack 0 |
  d: spec dGroundRules at 0
```

**MATCH.** The stale claim prints the row's words, pins nothing ("none live or held"), and its run is placed as in the
plain run (`a 7-11`) with the mark. The fresh claim is pinned: `d 0-4`, d's first run.

### Row 7: the same stale claim of user `daily-agent` on dTrueNorth

**Row:** Its table cell and a's first-wave line both read "whole dTrueNorth at 0, take over (stale)".

**Plant:**

```text
refs/gov/remote/runs/dTrueNorth -> 4d7c6a3ae6aa, message:
gov-claim dTrueNorth

slug: dTrueNorth
node: daily-agent
host: COMPEETO-AGENT
session: absent
keepalive: absent
status: live
lease-utc: 2026-10-20T15:34:07Z
beat-utc: 2026-10-20T15:34:07Z
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
claims cached on chain builds: none live or held; other: dTrueNorth stale on a: take over per [coordination]
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | a 0-7, slack 0, take over (stale) |
  a: whole dTrueNorth at 0, take over (stale)
```

**MATCH.** a's first-wave line reads the row's words exactly. dTrueNorth's table cell carries the same run and mark in
the cell's own form, `a 0-7, slack 0, take over (stale)`.

### Row 8: a cached `live` claim of user `d41ly` on dGroundRules with no `beat-utc` line

**Row:** Pinned to d, and printed "dGroundRules beat unreadable on d: kept pinned".

**Plant:**

```text
refs/gov/remote/runs/dGroundRules -> 1ed97e0ae96f, message:
gov-claim dGroundRules

slug: dGroundRules
node: d41ly
host: absent
session: absent
keepalive: absent
status: live
lease-utc: 2026-10-20T17:34:07Z
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
claims cached on chain builds: dGroundRules live on d; other: dGroundRules beat unreadable on d: kept pinned
| dGroundRules | Policy | dTrueNorth | 11 | d 0-4, slack 0 | a 7-14, slack 0 |
  d: spec dGroundRules at 0
```

**MATCH.** Pinned (`d 0-4`, d's first run), with the row's words.

### Row 9: a fresh `live` claim of user `agent5` on dFairHearing

**Row:** "a and d alone" reads 273, the same as with no claim, from a and d only, and the note says the claim is absent
from that run and left unpinned. Seen red on the script before this fold, which put the claim on a hidden pace-1 node
and printed 216.

**Plant:**

```text
refs/gov/remote/runs/dFairHearing -> 934632c00cf5, message:
gov-claim dFairHearing

slug: dFairHearing
node: agent5
host: DESKTOP-3J1O6CD
session: absent
keepalive: absent
status: live
lease-utc: 2026-10-20T17:34:07Z
beat-utc: 2026-10-20T17:34:07Z
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
claims cached on chain builds: dFairHearing live on b
| dFairHearing | Review harness | dSafePassage | 18 | b 0-24, slack 19 | d 27-39, slack 16 |
  a and d alone: 273
```

**The pre-fold red.** The fold is `a93477abc`. The same plant was run under the script as it stood at `a93477abc^`
(`d26d19a8e`, blob `b4d7320e645c`), written untracked into the clone as `prefold-schedule.py`:

**Command:** `python prefold-schedule.py --ref HEAD` · **Exit:** 0

```text
claims cached on chain builds: dFairHearing live on b
  a and d alone: 216
```

**The note.** No line of the run's output says the claim is absent from the "a and d alone" run, or that it was left
unpinned there. A probe planted the same claim again, so its commit differs, then called the script's
`run(..., with_b=False)` directly and printed the nodes and notes it returns, then the script lines that receive them:

```text
refs/gov/remote/runs/dFairHearing -> 155fa641eb2d, message:
held: {'dFairHearing': ('b', 'live')}
a and d alone: nodes ['a', 'd'] makespan 273 notes ['dFairHearing claimed on b, absent from this run: left unpinned']
27:     the three nodes that the current figure leaves out (node b in "a and d alone") is left unpinned and printed.
51: the runs in flight then, and node b's pace swept from 0.25 to 0.5 beside a and d alone. Exit 0, or 1 when v2's
373:     T3, s3, f3, w3, sp3, _ = run(names, parents, ids, state, held, a.s, a.b, with_b=False)
374:     print(f"  a and d alone: {max(f3.values(), default=0.0):.0f}")
```

**DIFFERS.** The figure matches: 273, the plain run's figure. The node set matches: a and d only. The pre-fold red
reproduces: 216. The note does not print. `run()` returns it ("dFairHearing claimed on b, absent from this run: left
unpinned"), but `main()` line 373 binds it to `_`, and line 374 prints the makespan alone. The script is unchanged
here, as the brief requires.

### Row 10: a live `agent5` claim on dGroundRules whose specs read done

**Row:** Printed as a spec-only node's claim on a build run and left unpinned: no build run goes to b.

**Plant:** two dGroundRules specs carrying its eleven clauses at `INPROGRESS`, committed, then the claim:

```text
memory/builds/dGroundRules/spec/2026-10-20-spec-plant-1.md:
# dGroundRules plant-1

**Status:** INPROGRESS · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0007@00000000 whole
**Carries:** cl-dClosedLoop-0008@00000000 whole
**Carries:** cl-dClosedLoop-0009@00000000 whole
**Carries:** cl-dClosedLoop-0010@00000000 whole
**Carries:** cl-dClosedLoop-0011@00000000 whole
**Carries:** cl-dClosedLoop-0012@00000000 whole

memory/builds/dGroundRules/spec/2026-10-20-spec-plant-2.md:
# dGroundRules plant-2

**Status:** INPROGRESS · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0013@00000000 whole
**Carries:** cl-dClosedLoop-0014@00000000 whole
**Carries:** cl-dClosedLoop-0015@00000000 whole
**Carries:** cl-dClosedLoop-0016@00000000 whole
**Carries:** cl-dClosedLoop-0017@00000000 whole

refs/gov/remote/runs/dGroundRules -> 84420b6f83da, message:
gov-claim dGroundRules

slug: dGroundRules
node: agent5
host: DESKTOP-3J1O6CD
session: absent
keepalive: absent
status: live
lease-utc: 2026-10-20T17:34:07Z
beat-utc: 2026-10-20T17:34:07Z
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
tree_state (spec done, build done): {"dGroundRules": [true, false]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 1, builds landed 0
claims cached on chain builds: dGroundRules live on b; dGroundRules claimed on b, which takes spec runs only: its build run is left unpinned
| dGroundRules | Policy | dTrueNorth | 11 | done | a 7-14, slack 0 |
node b: busy 162 of 268 (61%), work 41 of 506 units, 6 runs: 6 spec, 0 build, 0 whole
  b 0.25: 268; a 96% d 78% b 61%; spec dFairHearing 14-38, spec dPlacedRequest 61-89, spec dFurnishedOrders 113-139, spec dRankedPlan 139-160, spec dMindYourWords 160-183, spec dShippedRelease 183-224
  b 0.30: 262; a 97% d 81% b 52%; spec dFairHearing 14-34, spec dPlacedRequest 57-81, spec dFurnishedOrders 109-131, spec dRankedPlan 131-149, spec dMindYourWords 153-172, spec dShippedRelease 172-206
  b 0.35: 257; a 96% d 82% b 54%; spec dFairHearing 14-31, spec dPlacedRequest 55-74, spec dFurnishedOrders 106-125, spec dRankedPlan 125-140, spec dLinkedLibrary 140-164, spec dMindYourWords 164-180, spec dShippedRelease 180-209
  b 0.40: 251; a 100% d 81% b 54%; spec dFairHearing 14-29, spec dPlacedRequest 52-70, spec dFurnishedOrders 104-120, spec dRankedPlan 120-134, spec dLinkedLibrary 134-154, spec dMindYourWords 154-168, spec dShippedRelease 168-194, spec dScopedBuild 194-206
  b 0.45: 243; a 100% d 82% b 59%; spec dFairHearing 14-28, spec dPlacedRequest 51-67, spec dBoundRoles 74-93, spec dTotalRecall 93-112, spec dRankedPlan 112-124, spec dLinkedLibrary 124-142, spec dMindYourWords 142-155, spec dShippedRelease 155-178, spec dScopedBuild 178-189
  b 0.50: 239; a 99% d 77% b 72%; spec dFairHearing 14-26, spec dDeclaredLoop 27-49, spec dPlacedRequest 51-65, spec dBoundRoles 74-91, spec dTotalRecall 91-108, spec dRankedPlan 108-119, spec dFurnishedOrders 119-132, spec dMindYourWords 140-151, spec dShippedRelease 151-172, spec dScopedBuild 172-182, spec dTendedCadence 182-194, spec dCalibratedLens 194-205
```

**MATCH.** The specs read done and the build does not. The claim is printed as the row says. The build run goes to a
(`a 7-14`), and b's runs hold no build run, at pace 0.25 or in the sweep.

### Row 11: a live claim of user `agent-0`, node c, on dGroundRules

**Row:** Printed "held off-fleet on c": the run stays off every node's table.

**Plant:**

```text
refs/gov/remote/runs/dGroundRules -> c21d21fae581, message:
gov-claim dGroundRules

slug: dGroundRules
node: agent-0
host: DESKTOP-8BKM8GN
session: absent
keepalive: absent
status: live
lease-utc: 2026-10-20T17:34:07Z
beat-utc: 2026-10-20T17:34:07Z
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
claims cached on chain builds: dGroundRules live on c; dGroundRules held off-fleet on c
| dGroundRules | Policy | dTrueNorth | 11 | c 0-4, slack 0 | a 7-14, slack 0 |
node a: busy 257 of 268 (96%), work 257 of 510 units, 20 runs: 7 spec, 12 build, 1 whole
node d: busy 208 of 268 (78%), work 208 of 510 units, 16 runs: 7 spec, 9 build, 0 whole
node b: busy 162 of 268 (61%), work 41 of 510 units, 6 runs: 6 spec, 0 build, 0 whole
  a: whole dTrueNorth at 0
  d: spec dSafePassage at 7
  b: spec dFairHearing at 14
runs the owner starts, 43, at 36 distinct times, in order (time, node, run):
  0 a whole dTrueNorth · 0 c spec dGroundRules · 7 a build dGroundRules · 7 d spec dSafePassage
```

**MATCH.** The row's words are printed. No node line or first-wave line names the run: a, d and b hold 20, 16 and 6
runs, 42 of the 43. The row does not speak to two places the held run still prints: dGroundRules' table cell
(`c 0-4, slack 0`) and the owner-start list (`0 c spec dGroundRules`).

### Row 12: `--b 0.5`

**Row:** b's lines name twelve spec runs and no build run; with the `SPEC_ONLY` filter removed from the dispatch, the
same run gives b two build runs.

**Plant:** none for the first run. For the second, the script was copied untracked into the clone with one cut in
`simulate()`, line 232:

```text
variant-nospeconly.py, untracked in the clone: the script with `(n not in SPEC_ONLY or t[0] == "spec") and ` cut from simulate()
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD --b 0.5` · **Exit:** 0

```text
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.5; specs done 0, builds landed 0
node b: busy 171 of 243 (70%), work 85 of 510 units, 12 runs: 12 spec, 0 build, 0 whole
  b: spec dFairHearing at 18
  b 0.50: 243; a 99% d 76% b 70%; spec dFairHearing 18-30, spec dDeclaredLoop 30-53, spec dPlacedRequest 55-69, spec dBoundRoles 78-95, spec dTotalRecall 95-112, spec dRankedPlan 112-123, spec dFurnishedOrders 123-136, spec dMindYourWords 144-155, spec dShippedRelease 155-175, spec dScopedBuild 175-185, spec dTendedCadence 185-197, spec dCalibratedLens 197-208
```

**Command:** `python variant-nospeconly.py --ref HEAD --b 0.5` · **Exit:** 0

```text
node b: busy 186 of 242 (77%), work 93 of 510 units, 12 runs: 10 spec, 2 build, 0 whole
  b 0.50: 242; a 98% d 74% b 77%; spec dFairHearing 18-30, spec dDeclaredLoop 30-53, spec dPlacedRequest 55-69, spec dBoundRoles 78-95, spec dTotalRecall 95-112, spec dRankedPlan 112-123, spec dFurnishedOrders 123-136, build dFurnishedOrders 136-163, spec dMindYourWords 163-174, spec dScopedBuild 174-184, spec dTendedCadence 184-196, build dScopedBuild 196-216
```

**MATCH.** At pace 0.5, b's node line and sweep line name twelve spec runs and no build run. With the filter cut, b
takes 10 spec runs and 2 build runs, dFurnishedOrders' and dScopedBuild's.

### Row 13: dTrueNorth's six clause specs `CLOSED` and the extra unit's spec `OPEN`

**Row:** dTrueNorth is not done: its whole run still starts at 0.

**Plant:**

```text
memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-1.md:
# dTrueNorth plant-1

**Status:** CLOSED · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0001@00000000 whole

memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-2.md:
# dTrueNorth plant-2

**Status:** CLOSED · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0002@00000000 whole

memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-3.md:
# dTrueNorth plant-3

**Status:** CLOSED · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0003@00000000 whole

memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-4.md:
# dTrueNorth plant-4

**Status:** CLOSED · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0004@00000000 whole

memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-5.md:
# dTrueNorth plant-5

**Status:** CLOSED · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0005@00000000 whole

memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-6.md:
# dTrueNorth plant-6

**Status:** CLOSED · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Carries:** cl-dClosedLoop-0006@00000000 whole

memory/builds/dTrueNorth/spec/2026-10-20-spec-plant-7.md:
# dTrueNorth plant-7

**Status:** OPEN · rev-1 · 2026-10-20 · node d · Tier-1 · base 4bfca2c7 · streams playbook

**Derived:** P0.8 row 1 (the extra unit's decision row)
```

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
tree_state (spec done, build done): {"dTrueNorth": [false, false]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 0, builds landed 0
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | a 0-7, slack 0 |
  a: whole dTrueNorth at 0
```

**MATCH.** Neither phase reads done, and dTrueNorth's whole run is `a 0-7`, the first start.

## [done-rule]

The paragraph: "A build is done only when its specs carry every clause of its row and every spec in its folder, the
extra unit's included, is `CLOSED` or `WONTDO`." Rows 2, 3, 10 and 13 already exercise it. Each arm below is row 13's
seven dTrueNorth files changed as stated, except arm 4, which plants dGroundRules. The command is
`python <script> --ref HEAD` in every arm, and every arm exits 0.

| Arm | Plant | `tree_state` (spec, build) | Script reads | Against the paragraph |
|---|---|---|---|---|
| 1. Every clause carried, every spec `CLOSED` | `plant-7` at `CLOSED` | (true, true) | builds landed 1; cell `done` | MATCH |
| 2. The extra unit's spec `WONTDO` | `plant-7` at `WONTDO` | (true, true) | builds landed 1; cell `done` | MATCH |
| 3. One clause uncarried | `plant-6` not written (`cl-dClosedLoop-0006` uncarried); `plant-7` at `CLOSED` | (false, false) | builds landed 0; whole run `a 0-7` | MATCH |
| 4. A split build, every clause carried and `CLOSED` | row 10's two dGroundRules files at `CLOSED`, no claim | (true, true) | both cells `done` | MATCH |
| 5. A spec with no status | `plant-7` with no `**Status:**` line | (false, false) | builds landed 0; whole run `a 0-7` | MATCH |
| 6. A clause released, not carried | `plant-6`'s body `**Deferred:** cl-dClosedLoop-0006 by P0.8 row 1`; `plant-7` at `CLOSED` | (true, true) | builds landed 1; cell `done` | OPEN |
| 7. A clause carried in part only | `plant-6`'s body `**Carries:** cl-dClosedLoop-0006@00000000 part 1/2`, no part 2/2 anywhere; `plant-7` at `CLOSED` | (true, true) | builds landed 1; cell `done` | OPEN |

```text
arm 1
tree_state (spec done, build done): {"dTrueNorth": [true, true]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 1, builds landed 1
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | done |
  a: spec dGroundRules at 0
arm 2
tree_state (spec done, build done): {"dTrueNorth": [true, true]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 1, builds landed 1
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | done |
  a: spec dGroundRules at 0
arm 3
tree_state (spec done, build done): {"dTrueNorth": [false, false]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 0, builds landed 0
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | a 0-7, slack 0 |
  a: whole dTrueNorth at 0
arm 4
tree_state (spec done, build done): {"dGroundRules": [true, true]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 1, builds landed 1
| dGroundRules | Policy | dTrueNorth | 11 | done | done |
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | a 0-7, slack 0 |
arm 5
tree_state (spec done, build done): {"dTrueNorth": [false, false]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 0, builds landed 0
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | a 0-7, slack 0 |
  a: whole dTrueNorth at 0
arm 6
tree_state (spec done, build done): {"dTrueNorth": [true, true]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 1, builds landed 1
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | done |
  a: spec dGroundRules at 0
arm 7
tree_state (spec done, build done): {"dTrueNorth": [true, true]}
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 1, builds landed 1
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | done |
  a: spec dGroundRules at 0
```

**The two open arms.** The paragraph says "carry" and does not define it. Arm 6: the docstring says "carry or
release" (lines 16-17), and the `CARRY` pattern (line 73) counts a `**Moved:**`, `**Retired:**` or `**Deferred:**`
line as carrying the clause. Arm 7: the pattern counts any one `part k/n` line as carrying the whole clause. Neither the
paragraph nor the docstring says how parts count. The plan's line 777 names `part k/n` as a carry form, and carries.py
has a clause in parts carried by n specs (`carries.py:9`). Whether a build is done in either case is the owner's call.
Neither arm is a P0.4 row.

## [plain]

The unplanted clone at `4bfca2c74`, with no claim cached.

**Command:** `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref HEAD` · **Exit:** 0

```text
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 0, builds landed 0
claims cached on chain builds: none live or held
makespan 271 units; with unlimited nodes 198; whole builds after their parents land 277; serial on one node 510 (v2's 509 and 1 unit beyond it)

| Build | Stage | Parents | Units | Spec run: node, start-end, slack | Build run: node, start-end, slack |
|---|---|---|---|---|---|
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | a 0-7, slack 0 |
| dGroundRules | Policy | dTrueNorth | 11 | a 7-11, slack 0 | a 11-18, slack 0 |
| dSafePassage | Supersession | dGroundRules | 13 | d 11-15, slack 3 | d 18-27, slack 4 |
| dOrderedCharter | Foundation | dSafePassage | 37 | a 18-30, slack 0 | a 30-55, slack 0 |
| dFairHearing | Review harness | dSafePassage | 18 | b 18-42, slack 19 | d 42-54, slack 16 |
| dDeclaredLoop | Spine | dOrderedCharter, dFairHearing | 34 | d 54-65, slack 14 | a 65-88, slack 0 |
| dWitnessedBar | Test | dDeclaredLoop | 30 | d 65-75, slack 13 | a 88-108, slack 0 |
| dPlacedRequest | Entry | dDeclaredLoop | 21 | b 65-93, slack 22 | d 93-107, slack 6 |
| dKeptSession | Session | dDeclaredLoop, dPlacedRequest | 28 | d 107-116, slack 11 | a 117-135, slack 7 |
| dBoundRoles | Roles | dDeclaredLoop, dWitnessedBar, dPlacedRequest | 26 | a 108-117, slack 12 | a 135-153, slack 3 |
| dTotalRecall | Memory | dDeclaredLoop, dWitnessedBar, dPlacedRequest | 26 | d 116-125, slack 12 | d 145-162, slack 3 |
| dFurnishedOrders | Orders | dBoundRoles | 20 | b 117-143, slack 41 | a 161-174, slack 30 |
| dWellOiledMachine | Runtime | dBoundRoles, dTotalRecall, dKeptSession | 61 | d 125-145, slack 0 | d 162-203, slack 0 |
| dLinkedLibrary | Library | dTotalRecall | 25 | a 153-161, slack 25 | a 174-191, slack 16 |
| dIndexedDesign | Design | dDeclaredLoop, dTotalRecall, dKeptSession, dBoundRoles, dLinkedLibrary | 16 | a 191-196, slack 28 | a 196-207, slack 16 |
| dRankedPlan | Plan | dDeclaredLoop, dTotalRecall, dBoundRoles | 16 | b 143-164, slack 45 | d 203-214, slack 33 |
| dTendedCadence | Maintain | dWitnessedBar, dRankedPlan, dWellOiledMachine, dIndexedDesign, dFurnishedOrders | 18 | a 207-213, slack 21 | d 214-226, slack 0 |
| dMindYourWords | Lexicon | dWellOiledMachine, dWitnessedBar, dLinkedLibrary, dFurnishedOrders | 17 | b 164-186, slack 47 | a 224-235, slack 12 |
| dCalibratedLens | Review | dTendedCadence, dFairHearing | 17 | a 218-224, slack 6 | d 226-237, slack 0 |
| dShippedRelease | Deploy | dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine, dLinkedLibrary, dFurnishedOrders | 31 | b 186-227, slack 33 | a 235-256, slack 3 |
| dScopedBuild | Build | dIndexedDesign, dWitnessedBar, dWellOiledMachine, dFurnishedOrders | 15 | a 213-218, slack 35 | d 237-247, slack 13 |
| dConvergedCharter | Convergence | dScopedBuild, dShippedRelease, dCalibratedLens, dMindYourWords | 23 | d 247-255, slack 4 | a 256-271, slack 0 |

node a: busy 261 of 271 (96%), work 261 of 510 units, 21 runs: 8 spec, 12 build, 1 whole
node d: busy 208 of 271 (77%), work 208 of 510 units, 16 runs: 7 spec, 9 build, 0 whole
node b: busy 162 of 271 (60%), work 41 of 510 units, 6 runs: 6 spec, 0 build, 0 whole

first wave, each node's first run:
  a: whole dTrueNorth at 0
  d: spec dSafePassage at 11
  b: spec dFairHearing at 18

runs the owner starts, 43, at 37 distinct times, in order (time, node, run):
  0 a whole dTrueNorth · 7 a spec dGroundRules · 11 a build dGroundRules · 11 d spec dSafePassage
  18 d build dSafePassage · 18 b spec dFairHearing · 18 a spec dOrderedCharter · 30 a build dOrderedCharter
  42 d build dFairHearing · 54 d spec dDeclaredLoop · 65 a build dDeclaredLoop · 65 b spec dPlacedRequest
  65 d spec dWitnessedBar · 88 a build dWitnessedBar · 93 d build dPlacedRequest · 107 d spec dKeptSession
  108 a spec dBoundRoles · 116 d spec dTotalRecall · 117 a build dKeptSession · 117 b spec dFurnishedOrders
  125 d spec dWellOiledMachine · 135 a build dBoundRoles · 143 b spec dRankedPlan · 145 d build dTotalRecall
  153 a spec dLinkedLibrary · 161 a build dFurnishedOrders · 162 d build dWellOiledMachine · 164 b spec dMindYourWords
  174 a build dLinkedLibrary · 186 b spec dShippedRelease · 191 a spec dIndexedDesign · 196 a build dIndexedDesign
  203 d build dRankedPlan · 207 a spec dTendedCadence · 213 a spec dScopedBuild · 214 d build dTendedCadence
  218 a spec dCalibratedLens · 224 a build dMindYourWords · 226 d build dCalibratedLens · 235 a build dShippedRelease
  237 d build dScopedBuild · 247 d spec dConvergedCharter · 256 a build dConvergedCharter

landings of build and whole runs, with the runs in flight then and the surfaces the landing's clauses touch:
     7 dTrueNorth lands; in flight: none; surfaces: spec-format 0001,0002
    18 dGroundRules lands; in flight: none; surfaces: charter 0012; hooks 0011
    27 dSafePassage lands; in flight: spec dOrderedCharter on a, spec dFairHearing on b; surfaces: lander 0025; bar 0026,0029; hooks 0023,0024,0026..
    54 dFairHearing lands; in flight: build dOrderedCharter on a; surfaces: charter 0082; bar 0075,0080,0083..
    55 dOrderedCharter lands; in flight: spec dDeclaredLoop on d; surfaces: driver 0032,0047,0048..; lander 0047; charter 0031,0032,0036..; roles 0051; bar 0047,0048; hooks 0038
    88 dDeclaredLoop lands; in flight: spec dPlacedRequest on b; surfaces: driver 0099,0106,0108..; bar 0092,0102,0115; hooks 0091
   107 dPlacedRequest lands; in flight: build dWitnessedBar on a; surfaces: driver 0120,0123,0134; lander 0129; charter 0121; roles 0130
   108 dWitnessedBar lands; in flight: spec dKeptSession on d; surfaces: driver 0344; lander 0342; bar 0339,0342,0344..; hooks 0342,0344
   135 dKeptSession lands; in flight: spec dFurnishedOrders on b, spec dWellOiledMachine on d; surfaces: driver 0504; charter 0141; hooks 0140,0159
   153 dBoundRoles lands; in flight: spec dRankedPlan on b, build dTotalRecall on d; surfaces: charter 0180,0190; roles 0166,0168,0182..; bar 0188,0190; hooks 0190
   162 dTotalRecall lands; in flight: spec dRankedPlan on b, build dFurnishedOrders on a; surfaces: roles 0215,0220,0223..; bar 0237
   174 dFurnishedOrders lands; in flight: build dWellOiledMachine on d, spec dMindYourWords on b; surfaces: driver 0195; method 0195; roles 0202,0203,0209..; hooks 0197,0201,0205
   191 dLinkedLibrary lands; in flight: build dWellOiledMachine on d, spec dShippedRelease on b; surfaces: driver 0240; spec-format 0500; hooks 0244
   203 dWellOiledMachine lands; in flight: spec dShippedRelease on b, build dIndexedDesign on a; surfaces: driver 0280,0281,0301..; lander 0288,0311,0318..; charter 0320; roles 0310,0320; bar 0288,0318,0322..; hooks 0279,0282,0288..
   207 dIndexedDesign lands; in flight: spec dShippedRelease on b, build dRankedPlan on d; surfaces: spec-format 0383; roles 0397
   214 dRankedPlan lands; in flight: spec dShippedRelease on b, spec dScopedBuild on a; surfaces: hooks 0377
   226 dTendedCadence lands; in flight: spec dShippedRelease on b, build dMindYourWords on a; surfaces: bar 0499
   235 dMindYourWords lands; in flight: build dCalibratedLens on d; surfaces: charter 0278; roles 0270; bar 0270
   237 dCalibratedLens lands; in flight: build dShippedRelease on a; surfaces: charter 0462; roles 0463; bar 0468
   247 dScopedBuild lands; in flight: build dShippedRelease on a; surfaces: spec-format 0400; method 0404
   256 dShippedRelease lands; in flight: none; surfaces: driver 0426; lander 0413,0507,0414..; bar 0431; hooks 0427,0431,0437
   271 dConvergedCharter lands; in flight: none; surfaces: driver 0485,0486,0494..; lander 0485; charter 0479,0486,0490..; roles 0485; bar 0485; hooks 0490

node b's pace swept (makespan; busy share of a, d, b; b's runs):
  b 0.25: 271; a 96% d 77% b 60%; spec dFairHearing 18-42, spec dPlacedRequest 65-93, spec dFurnishedOrders 117-143, spec dRankedPlan 143-164, spec dMindYourWords 164-186, spec dShippedRelease 186-227
  b 0.30: 265; a 97% d 80% b 51%; spec dFairHearing 18-38, spec dPlacedRequest 61-84, spec dFurnishedOrders 113-135, spec dRankedPlan 135-152, spec dMindYourWords 157-176, spec dShippedRelease 176-210
  b 0.35: 261; a 96% d 81% b 54%; spec dFairHearing 18-35, spec dPlacedRequest 58-78, spec dFurnishedOrders 110-129, spec dRankedPlan 129-144, spec dLinkedLibrary 144-167, spec dMindYourWords 167-183, spec dShippedRelease 183-212
  b 0.40: 254; a 100% d 80% b 53%; spec dFairHearing 18-33, spec dPlacedRequest 56-73, spec dFurnishedOrders 108-124, spec dRankedPlan 124-137, spec dLinkedLibrary 137-158, spec dMindYourWords 158-172, spec dShippedRelease 172-198, spec dScopedBuild 198-210
  b 0.45: 247; a 100% d 81% b 58%; spec dFairHearing 18-31, spec dPlacedRequest 55-70, spec dBoundRoles 78-97, spec dTotalRecall 97-116, spec dRankedPlan 116-128, spec dLinkedLibrary 128-146, spec dMindYourWords 146-158, spec dShippedRelease 158-181, spec dScopedBuild 181-192
  b 0.50: 243; a 99% d 76% b 70%; spec dFairHearing 18-30, spec dDeclaredLoop 30-53, spec dPlacedRequest 55-69, spec dBoundRoles 78-95, spec dTotalRecall 95-112, spec dRankedPlan 112-123, spec dFurnishedOrders 123-136, spec dMindYourWords 144-155, spec dShippedRelease 155-175, spec dScopedBuild 175-185, spec dTendedCadence 185-197, spec dCalibratedLens 197-208
  a and d alone: 273
```

## Finding 15

The revision record's finding 15 (`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-revision.md`), built from
`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-brief-carries-2.md` (dispatch 242), its recommended option 1:
print the notes on the "a and d alone" line. `main()` now binds the notes `run(..., with_b=False)` returns, where it
bound them to `_`. It appends them to that line in the claims line's own form, `; ` before each. With no note, the
line is as before.

**Where they ran.**
- `S` is this dispatch's scratch folder, the `d242` sibling of d237's.
- `S/plant` is a `--shared` clone of the session's worktree at `bcc416ced`. Its script is the old code, blob
  `bc733fd33f55`, the blob [setup] names. `N` is the new script, in `S/build`, the linked worktree of a second clone
  on the branch `p0-carries-2`, run by its absolute path from `S/plant`.
- `S/driver.py` is d237's driver, copied. Its clone is `S/plant` and its reset base is `bcc416ced`. Its output folder
  and the script it runs come from `OUT` and `RUN`, and each `.out` header still shows the repo-relative script path,
  so a before and an after run compare byte for byte.
- Plants and claims are made only in `S/plant`, as [setup] describes. No fetch, push or `unattended.sh --claims` ran.

| # | Command | Exit | The line that proves it |
|---|---|---|---|
| 1 | `git -C S/plant hash-object <script>` | 0 | `bc733fd33f553e6b9ee9709991ae603d3d525522` |
| 2 | `OUT=S/s-before python S/driver.py plain`, the old code | 0 | `plain: exit 0`, with `makespan 271 units; …` and `  a and d alone: 273` |
| 3 | `OUT=S/s-before python S/driver.py r01 r02 … r13` | 0 | rows 1 and 5 exit 1, every other case 0. Row 9's last line is `  a and d alone: 273`, with no note: the note absent before |
| 4 | `cmp` of each `S/s-before/*.out` against d237's own outputs, `d237/out/` in the same scratchpad | 0 each | all 17 identical, so at `bcc416ced` the old code prints what [rows] and [plain] quote |
| 5 | `OUT=S/s-after RUN=N python S/driver.py plain r01 r02 … r13`, the new code | 0 | every case exits as in rows 2 and 3 |
| 6 | `cmp` of each `S/s-after/*.out` against `S/s-before`, and `diff` of each that differs | `cmp` 0 for 13, `diff` 1 for 4 | 13 identical. Four differ, each on its "a and d alone" line alone: row 9's reads `  a and d alone: 273; dFairHearing claimed on b, absent from this run: left unpinned`, the note printed after |
| 7 | the same `diff`, the other three | 1 each | row 4: `  a and d alone: 273; dGroundRules claimed on b, absent from this run: left unpinned`. Row 10: `  a and d alone: 270; dGroundRules claimed on b, absent from this run: left unpinned`. Row 11: `  a and d alone: 270; dGroundRules held off-fleet on c` |
| 8 | `python S/recordcheck.py <this record> S/s-before`: each row's quoted output lines in [rows], row 9's probe block skipped, looked up in its `.out` | 0 | every row `0 missing`, 66 quoted lines in all |
| 9 | `python S/recordcheck.py <this record> S/s-after` | 1 | `row 9: 2 blocks, 5 quoted lines, 1 missing`, the line `  a and d alone: 273`. Every other row `0 missing` |
| 10 | a `python -c` looking up the [plain] block's lines in each `plain.out`, run twice, the second time exiting 1 on any miss | 0 | `s-before 83 lines, 0 missing` and `s-after 83 lines, 0 missing` |
| 11 | `git add` of the script by name in `S/build`, `git diff --quiet` on it, `git ls-files --eol` | 0 | `i/lf    w/lf    attr/text eol=lf`, the index entry `5aa5421e265b`, no CR byte |
| 12 | `OUT=S/s-staged RUN=N python S/driver.py plain r01 r02 … r13` | 0 | `cmp` of all 17 outputs against `S/s-after` prints nothing |

**Verdict.**
- Row 9 now matches the plan's row. "a and d alone" reads 273, from a and d only, and the line carries the note that
  the claim is absent from that run and left unpinned. The pre-fold red still prints 216.
- Every line [rows] quotes for rows 1 to 8 and 10 to 13 is unchanged. So is every line of the plain run: makespan 271,
  and "a and d alone" 273 with no note.
- Rows 4, 10 and 11 gain a note on their "a and d alone" line, which [rows] does not quote. Rows 4 and 10 hold a claim
  on node b, absent from that figure as row 9's is. Row 11's off-fleet note repeats the one its claims line prints.
  The plan's Result cells for those three rows do not speak to that line.

**What this does not check.** The sweep lines and the claims line print the notes of the run with node b, as before.
Nothing here re-runs the done-rule arms, which do not read the notes.
