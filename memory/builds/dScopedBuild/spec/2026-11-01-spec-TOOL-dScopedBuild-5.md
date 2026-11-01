# TOOL-dScopedBuild-5 — a write gate reading derived state: the routed unit's step from the position engine and its lease's write set, never its status line

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 7 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0403@3c89f2a1 whole
**Carries:** node:item.build.unit-lease

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-3-reuse-scout-b.md](../build/2026-11-01-build-TOOL-dScopedBuild-3-reuse-scout-b.md) | research | TOOL-dScopedBuild-3 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-1 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

The write gate admits a product write on a routed unit by reading what the unit's commits and its
lease witness, not the `**Status:**` line its agent writes, which is the charter's `[class]` defect
gap-build-03 and theme T2 name (`scratch-guard.js:88-90`). A role agent's Bash and PowerShell writes
meet the same verdict through dBoundRoles' shell check, and the main loop's meet unit 3's push arm.

## 2. Scope (IN)

- **S1** — The lease reader, `read_unit_lease(root, slug, unit, target)` in
  `tools/memory-tree/routed_commits.py`, beside TOOL-dScopedBuild-3's `read_unit_writes`, and its CLI
  `python routed_commits.py --unit-lease <slug> <unit> <target>`, which prints one JSON object
  `{unit, spec, step, answer, lease, writes, inside, reason}` (§4 "The answer"). The step is the
  unit's `units[].step` from the position engine, TOOL-dDeclaredLoop-7 S7's `position.py <slug>
  --json`, run under `sys.executable` as a subprocess bounded at 30 seconds and found by
  `resolve_kit_dir("loop", "position.py", HERE)`, imported from `backlog` as `deviation_join.py:44`
  names it (`tools/memory-tree/backlog.py:1758`), so the engine's witnesses decide it and no status
  header does. Observed by AC1, AC2, AC3 and AC6.
- **S2** — `item.build.unit-lease`, the lease's write set, I7, read through TOOL-dScopedBuild-3 S2's
  `read_unit_writes(unit, spec_text, run_rows, tracked)` and never re-read: its dispatched rows, else
  the spec's words through `read_spec_writes`, each reduced by S1's `derive_kit_dir`. `lease` is
  `dispatched` where a dispatch row names the unit, `attended` where only the spec declares, and
  `undeclared`, with an empty set, where neither does, the word unit 3's report prints. `inside` is
  true when `check_guard_trips` (`tools/memory-tree/design_lib.py:589`) holds for the target against
  one reduced entry, the test unit 3's scope arm applies to a pushed path (its S3), so the gate and
  the push read one write set at one granularity. Observed by AC3 and AC4.
- **S3** — The shell half, `tools/memory-tree/lease-shim.sh`, run as
  `bash lease-shim.sh <slug> <unit> <target>` in the target's toplevel, as `policy-shim.sh` is run for
  the policy mirror (`tools/policy/policy-shim.sh:1-17`), because a hook resolves no python launcher.
  It resolves the launcher through the inline canonical `resolve_python` block, as `policy-shim.sh:71`
  carries it, and runs its own kit's `routed_commits.py --unit-lease`, passing its stdout and exit
  through. Where no launcher is found it prints `{"answer": "not-installed", "reason": <why>}` and
  exits 0; a wrong invocation exits 2. Observed by AC5.
- **S4** — `checkBuildable` (`tools/hooks/scratch-guard.js:873`) keeps its route-line, spec-path and
  H1 checks byte for byte, then asks `readUnitLease(top, build, unit, rel)`, which spawns S3, found at
  `<tool root>/memory-tree/lease-shim.sh` from the hook's own directory as `agent-cap.js:465` finds
  the policy helper, through a bash found by `resolveBash`, exported from
  `tools/policy/policy-mirror.js` (`:66-80`) as its second caller instead of a copy. A unit is
  buildable when `answer` is neither `invalid-input`, `terminal` nor `error` and its `step` is
  `designed` or `built`; any other step refuses with `derived step <step>: <reason>`. A spawn failure,
  a non-zero exit, a non-JSON answer or an `error` answer refuses, naming it: the gate fails closed as
  it does today (`tools/hooks/README.md:357-359`). `BUILDABLE_STATUS` (`:796`) and `readStatusCells`
  (`:861`) are read only on the `not-installed` answer (S6). Observed by AC1, AC2 and AC6.
- **S5** — The lease arm. Among the routed units S4 admits, the write is admitted by one whose
  `inside` is true. Where none is, `build.scope` decides, read at the target's toplevel through
  `readPolicy("build.scope")` (`policy-mirror.js:132`), the hook's form of I4's `policy.py get`
  (`tools/policy/policy.py:1332`): `refuse` denies, naming the target, each admitted unit, its `lease`
  and its `writes`; `warn-and-ask` and `report` admit, the push-time arm of TOOL-dScopedBuild-3
  grading the commit as that value says. A `PolicyRefusal` denies with its line. The role arm (step
  9a) runs after an admission exactly as at base. Observed by AC4.
- **S6** — Not installed. Where S3 or S1 answers `not-installed`, or the hook finds no bash
  `resolveBash` can run, or no `lease-shim.sh` (no launcher, no memory-tree kit, no loop kit
  `resolve_kit_dir` finds), the gate reads the typed status as at base, and every refusal and every
  route-context verdict line names `not-installed: <why>`, so an adopter without the loop kit keeps
  its gate and is told which reading it got. Observed by AC6.
- **S7** — Shell writes. TOOL-dBoundRoles-7 S3's `checkShellWrites` judges a role agent's Bash or
  PowerShell target by calling `checkRouted` on a synthetic `Write` payload, so S4 and S5 hold it with
  no shell code in this unit. A payload with no `agent_type`, the main loop's, is not refused by the
  hook; TOOL-dScopedBuild-3's push arm grades its commit. Observed by AC7.
- **S8** — The route context. `renderRouteContext` (`scratch-guard.js:1470`), whose verdict line reads
  `readStatusCells` at `:1508`, prints `<unit> is buildable: step <step> · lease <lease>` from
  S1's answer, or the not-installed line of S6. Observed by AC2.
- **S9** — The text. The hook header's "WHAT ESCAPES THE WRITE GATE" sentence on a status flipped to
  INPROGRESS (`scratch-guard.js:88-90`), the README's BUILDABLE definition and ceiling paragraph
  (`tools/hooks/README.md:338-342`, `:363-365`), and the user page's product-write line
  (`help/roles.md:108-109`) state the derived step and the lease, and what still escapes (§4).
  Observed by AC8.

## 3. Non-goals (OUT)

- The position engine and its witnesses: TOOL-dDeclaredLoop-7. This unit reads `units[].step` and
  `answer` and nothing else of the `Position`.
- The shell write scanner and `checkShellWrites`: TOOL-dBoundRoles-7 S1 and S3, a build-run
  precondition (§8 F4). The main loop's shell writes: TOOL-dScopedBuild-3's push arm.
- The rest of `build.unit-lease`'s row (`flow-steps.md:288`): taking the lease, waiting on a declared
  dependency's clean `build.reuse-check`, and the overlap refusal. The driver's `--dispatch` takes the
  unattended lease today (`unattended.sh:13624`) and TOOL-dPlacedRequest-1 S9 owns the overlap; this
  unit reads the lease's write set, the part the gate needs.
- The card's home: TOOL-dWellOiledMachine-38 re-points `readCard` to the session binding, and the
  route this unit reads arrives through whichever reader holds then.
- Grading `build.scope` at the push, its ask and its `record-kind.scope` report: TOOL-dScopedBuild-3.
- Retiring `BUILDABLE_STATUS`: it stays as S6's not-installed reading.

### Edges

- **consumes-from** `TOOL-dScopedBuild-3` — `read_spec_writes`, through `read_unit_writes` and `derive_kit_dir`, I7's write set at the grain its scope arm grades; without it the gate and the push read two write sets
- **consumes-from** external — TOOL-dDeclaredLoop-7 S7's `position.py <slug> --json`, TOOL-dBoundRoles-7 S3's `checkShellWrites`, and dGroundRules' landed `policy-mirror.js` and `policy-shim.sh`
- **hands-off** `TOOL-dScopedBuild-35` — S2's and §4's lease word and S4's `readUnitLease` arity, S3; S4's spawn bound, S25; and AC8's per-file grep, S35 (ids 6, 43, 9)

## 4. Design

### The order

`checkRouted`'s steps 1 to 8 are unchanged. Step 9 becomes:

```
for each routed unit u:
  structural = checkBuildable's route-line, spec-path and H1 checks          (unchanged)
  a = readUnitLease(top, memRoot, build, u.unit, rel)                         (S3 -> S1)
  a.answer == not-installed      -> the typed read at base, reason + "not-installed: <why>"   (S6)
  a.answer in {invalid-input, terminal, error}, or step not in {designed, built} -> refused (S4)
  else buildable; keep a
buildable == []                  -> deny, each unit's reason                               (as at base)
some buildable a.inside          -> step 9a (the role arm)                                  (S5)
else build.scope: refuse         -> deny naming target, units, leases, writes
     warn-and-ask | report       -> step 9a; the push arm grades the commit
```

### The answer

```json
{"unit": "TOOL-x-1", "spec": "<repo-relative path>", "step": "designed|built|tested|deployed|none",
 "answer": "<the engine's answer, or not-installed, or error>", "lease": "dispatched|attended|none",
 "writes": ["<path>", ...], "inside": true, "reason": "<one line>"}
```

`answer` is the engine's `Position.answer` (TOOL-dDeclaredLoop-7 §4, one of its seven), `not-installed`
when a kit the reading needs is absent, or `error` when the engine exits non-zero or prints no JSON.
`step` is the unit's row of `units`, `none` when the engine lists no row for it.

### Why `designed` and `built`

`designed` is the engine's witness that the spec is committed and derives READY (TOOL-dDeclaredLoop-7
S2), the derived form of the M2 hard floor the typed INPROGRESS stood in for; `built` admits the fix
and follow-up passes `build.fix-pass` routes to a unit already built (`flow-steps.md:291`). `tested`
and `deployed` refuse: a landed unit changes through new units (cl-dClosedLoop-0400). The owner's
approval the typed INPROGRESS recorded is no longer read here: in the loop it is the Design exit
the engine's step already reflects, and §8 F5 asks dIndexedDesign about the one reader that leaned on
the typed admission.

### What it does not check

A hook-less or `--bare` run fires no hook. A main-loop shell write reaches only the push. A write a
script makes from inside a file it runs escapes TOOL-dBoundRoles-7 S1's scanner, as its §3 says. A
dispatch row the run itself writes is read as the lease, since the driver writes it through
`--dispatch`; the push arm and check 23 grade the commit against the same rows afterwards. A route on
a hand-written card still names which units are asked about; it no longer decides whether they are
buildable. Under `not-installed` the base gate, its typed read included, is what runs.

### Inventory

| Name | What | Cell |
|---|---|---|
| `read_unit_lease` | Python function, `routed_commits.py` | `py.function`, answered OK |
| `--unit-lease` | `routed_commits.py` CLI mode | none |
| `lease-shim.sh` | shell file, memory-tree kit | none declared |
| `readUnitLease` | JS function, `scratch-guard.js` | `js.function`, answered OK |
| `resolveBash` | existing JS function, now exported | `js.function`, unchanged name |

### Rollout

Live at landing where the loop kit is installed, which in gov is after TOOL-dDeclaredLoop-7 lands
(§8 F4); `not-installed` elsewhere, named on every verdict. No conf key and no default-off switch:
the not-installed reading is the dark state, and its reason says so.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/README.md`
- `tools/policy/policy-mirror.js`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/lease-shim.sh`
- `help/roles.md`

### Alternatives rejected

- `derive_ready_state` (TOOL-dIndexedDesign-16 S6) as the derived state. Rejected by reading its S6:
  it prints `plan_state`'s token over a spec's text, which an agent writes as surely as a status line,
  and it holds no witness of a commit; the `[class]` test (gap-register T2) is what it fails.
- The typed status kept beside the derived step. Rejected by the clause's own seen-red case: a planted
  typed status that admits where the derived step refuses must refuse (AC1), which a conjunction
  passes only by reading the derived step alone.
- A write-set reader of the gate's own, or `read_pass_declarations` called from the shim. Rejected by
  I7's one matcher and the interface axis (BUILD-METHOD M2): the push arm grades
  `read_unit_writes`'s set, so a gate reading any other set refuses or admits what the push decides
  the other way; §8 F6 carries the one disagreement found.
- A file-granularity lease refusing every out-of-set write. Rejected by research-build.md:128-136:
  candidate B refuses 20.5% of historical commits mid-pass at file granularity, and the push arm
  grades at kit granularity under `warn-and-ask` by default.

## 5. Production-readiness checklist

- security — the gate stays deny-by-default: every failure of the derived reading refuses, and only
  a `not-installed` answer, which names itself, reads the base gate. No new write path.
- perf / scale — each routed write now spawns bash, python and the engine, which spawns git; not
  measured at writing, and AC1's `cost:` line says what to record.
- error / empty / loading states — no engine, no launcher, no kit: `not-installed`; a crashed engine
  or non-JSON answer: `error`, refused; an empty lease: `none`, every target outside it.
- observability — every refusal names the derived step, the lease source and the reason line.
- risks — the walkthrough's: this replaces the decision path every product write crosses
  (`walkthrough.md:511`); the not-installed reading bounds an adopter's exposure to it.
- testing — the hook suite's new arms (§7) with a stub engine; AC7 waits on TOOL-dBoundRoles-7.
- migration — none: no conf key, no record. An adopter installing the loop kit moves from the typed
  reading to the derived one on its next write.
- user docs — `help/roles.md` (S9).

## 6. Acceptance criteria

- **AC1** — When `node tools/hooks/scratch-guard.js` reads a `Write` payload for a product path in a
  fixture repository whose card routes a spec headed `Tier-2` at `INPROGRESS` while the fixture's
  `position.py` answers that unit `step` `none`, it exits 2 and its stderr names `derived step none`.
  Red when: the typed status admits the write the derived step refuses.
  fixture: a scratch repository under `%TEMP%` with a conf, a card, the spec and a stub engine, built by the pass.
  cost: record the hook's wall time per write on this node beside the verdict.
- **AC2** — When the AC1 fixture's spec header reads `OPEN` and its engine answers `designed`, the
  same payload exits 0, and `renderRouteContext` prints `is buildable: step designed · lease attended`.
  Red when: the gate refuses on the status cell, or the context line reads the status.
- **AC3** — When `python tools/memory-tree/routed_commits.py --unit-lease` runs in the AC1 fixture for
  unit `TOOL-x-1`, whose build's `RUN.md` holds two dispatch rows for it and one for `TOOL-x-2`, it
  prints `lease` `dispatched` with the reduced paths of the first two rows only; with no row it prints
  `lease` `attended` with the spec's Files touched reduced; over a spec with no such sub-head and no
  row, `lease` `undeclared` and `writes` `[]`; each `writes` equals what `read_unit_writes` returns.
  Red when: another unit's row enters the set, or the lease and unit 3's write set differ.
- **AC4** — When the AC2 fixture's lease holds one file of kit directory a, the payload targets a file
  of kit directory b, and a planted `.governance/policy.toml` names `build.scope = "refuse"`, the hook
  exits 2 naming the target, the unit and `lease attended`; `"warn-and-ask"`, `"report"` and no policy
  file each exit 0, and a target inside the lease exits 0 under `refuse`.
  Red when: a value grades the out-of-lease write as another value does, or an in-lease write refuses.
- **AC5** — When `bash lease-shim.sh` runs over the AC3 fixture, it prints the line `--unit-lease`
  prints; with the fixture's loop kit removed it prints `answer` `not-installed` naming `position.py`,
  and with no launcher on the path it prints `not-installed` naming `resolve_python`.
  Red when: the shim answers other than the reader, or a missing kit reads as a step.
- **AC6** — When the fixture's `position.py` exits 3, the hook exits 2 naming `error`; with the loop
  kit removed and the spec at `INPROGRESS`, it exits 0 and the route context names
  `not-installed: position.py`, and at `SPECCED` it exits 2 with the base reason and that line.
  Red when: a broken engine admits, or the not-installed reading is silent.
- **AC7** — When a `Bash` payload carrying `agent_type` `gov-builder` redirects `printf x` into a
  product path of the AC1 fixture, `checkShellWrites` denies it with `derived step none`; the same
  payload with no `agent_type` is not refused by the hook.
  Red when: a role agent's shell write is admitted where its `Write` would not be.
  fixture: TOOL-dBoundRoles-7 S3 landed; the build run's precondition (§8 F4).
- **AC8** — When `grep -n "flipped to INPROGRESS"` runs over `tools/hooks/scratch-guard.js` and
  `tools/hooks/README.md` it prints nothing, and `grep -n "derived step" help/roles.md` prints a line.
  Red when: a carrier still says the gate reads a status the agent writes.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `format-guard self-test` · `policy fixtures` · `policy check` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the fixture repository with a stub `position.py` and planted `build.scope` values, its failing case a `Tier-2` `INPROGRESS` spec whose engine answers `none` admitted · none

## 8. Open questions

- **F1 — Which derived steps admit a write?** Options: (a) `designed` and `built`; (b) `designed`
  only; (c) only when the engine's `next` item is a Build item of the unit. orientation.md:214-216
  answers that the gate "reads the derived position"; (b) refuses every fix pass `build.fix-pass`
  routes to a unit already `built` (`flow-steps.md:291`), and (c) refuses a parallel unit whose item
  is not the build's first. Rung 1 for the reading, rung 3 among what survives. RESOLVED (agent,
  2026-11-01, delegated): (a). widens: none · relaxes: none
- **F2 — What does the gate do with a write outside the lease?** Options: (a) always refuse; (b) grade
  it by `build.scope`; (c) not read the lease. (c) drops the lease half of orientation.md:214-216;
  (a) refuses at the act what the default `warn-and-ask` admits at the push, the 20.5% file-granularity
  loss of research-build.md:128-136; (b) honours each of the key's three values at both points. Rung 3,
  the most feature-rich survivor. RESOLVED (agent, 2026-11-01, delegated): (b). widens: none · relaxes:
  none
- **F3 — What does the gate read where the derived reading is not installed?** Options: (a) the base
  typed reading, named `not-installed: <why>` on every verdict; (b) refuse every product write; (c)
  admit every product write. (c) widens the write surface (veto 3); (b) leaves an adopter without the
  loop kit no product write at all, which no criterion asks; (a) keeps the base gate where nothing
  better can run and says so. Rung 3. RESOLVED (agent, 2026-11-01, delegated): (a). widens: none ·
  relaxes: none
- **FACT-QUESTION · F4 — Do dDeclaredLoop and dBoundRoles, which this unit calls and the packet does
  not list as parents, land before this build?** Probe: `grep -m1 "^parents:"` over the READMEs of
  dWitnessedBar and dFurnishedOrders. Observation that decides: each build named on a parent's
  `parents:` line, which the chain lands first. Liveness: a build named on no parent's line prints
  nothing and is routed as a stand-in. Run at writing: dWitnessedBar names dDeclaredLoop, dFurnishedOrders
  names dBoundRoles. RESOLVED (agent, 2026-11-01, delegated): both are build-run preconditions, and
  no stand-in is specced. widens: none · relaxes: none
- **F5 — dIndexedDesign's `design.handoff` value `status-and-tier` leaves its status and tier admission
  to this gate's `BUILDABLE_STATUS` (TOOL-dIndexedDesign-1 §8 F1 (a)), which this unit reads only
  under `not-installed`.** Options: (a) an ask for dIndexedDesign; (b) keep the typed read beside the
  derived step; (c) nothing. (b) fails AC1; (c) leaves that value's admission graded by nobody where
  the loop kit is installed. Rung 3. RESOLVED (agent, 2026-11-01, delegated): (a), the ask for build
  dIndexedDesign: "THE HAND-OFF'S STATUS-AND-TIER VALUE LOSES ITS GRADER WHEN THE WRITE GATE READS THE
  DERIVED STEP", accept "TOOL-dIndexedDesign-1's `status-and-tier` names the check that grades a unit's
  status and tier once `checkBuildable` reads the position engine's step, seen red on a Tier-2 unit at
  SPECCED dispatched under that value". widens: none · relaxes: none

- **F6 — Which dispatched rows make the lease?** Options: (a) `read_unit_writes`'s, every row naming
  the unit in its build's `RUN.md` and rotated `RUN.*.md` (TOOL-dScopedBuild-3 S2); (b)
  `read_pass_declarations <RUN.md> current`, the key holding the unit's last row
  (`lib-unattended.sh:1116`), which the commit-time `--check-commit` reads. (b) makes the gate admit
  a set the push arm grades otherwise, the two-answers class, at the act and at the push of one
  write. Rung 3, the survivor that keeps the interface axis; the disagreement between (a) and (b),
  a second reader of dispatch rows beside the one `lib-unattended.sh:1105-1112` names, is unit 3's to
  answer and is named in this writer's return. RESOLVED (agent, 2026-11-01, delegated): (a). widens:
  none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam extended is `checkBuildable` in `tools/hooks/scratch-guard.js` (`:873`), inside
`checkRouted` (`:1113`), keeping its structural checks; the bridge is the `policy-mirror.js` to
`policy-shim.sh` pattern, `resolveBash` exported rather than copied; the write set is I7 through
TOOL-dScopedBuild-3's `read_unit_writes` and `derive_kit_dir`, over `design_lib.read_spec_writes` and
`check_guard_trips` (`:528`, `:589`); the kit lookup is `backlog.resolve_kit_dir`.
`reuse_lookup.py "write gate admits a product write when the routed unit is buildable"` ranked
name-token neighbours only (`write`, `build`, `units`, `build_commit`) and missed `checkBuildable`, an
answer recorded rather than retried; the recall query found scout B's row and TOOL-dIndexedDesign-1's
F1, which is §8 F5. Scout B's line numbers were re-read at `5f0b11f12`: `checkBuildable` `:873`,
`checkRouted` `:1113`, `BUILDABLE_STATUS` `:796`, `WRITE_TOOLS` `:794` and `scanWriteTargets` `:339`
agree; its `:1191` is the loop over `route.units`, whose `checkBuildable` call is `:1192`.

Recall terms used: `python tools/memory-recall/query.py "how does the write gate decide a routed unit is buildable without reading a typed status" --terms "scratch-guard checkBuildable checkRouted BUILDABLE_STATUS derived position witness lease write set ROUTED_PATHS shell writes"`
