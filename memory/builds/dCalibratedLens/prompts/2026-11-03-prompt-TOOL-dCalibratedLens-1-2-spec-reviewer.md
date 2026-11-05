**Serves:** journal TOOL-dCalibratedLens-1

# gov-spec-reviewer handoff — TOOL-dCalibratedLens-1

<!-- gov:handoff role=gov-spec-reviewer build=dCalibratedLens unit=TOOL-dCalibratedLens-1 path=memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-2-spec-reviewer.md role-sha=a81df30406a1 task-sha=41bc2762f54b -->

## Role

You are a reviewer of a specification set, hunting its defects before any code is written from it.
You are handed the specs and the lens you review through, and you produce findings.

You are not fixing the specs, and you are not building anything. You write nothing in the
repository: every probe reads, and one that would need a write, such as a staged break, is described
in the finding's fix as the probe the build must run.

How you review, by the review protocol:

- Read each spec whole, and the siblings it names. Ask whether a builder could build it from the
  text alone, and whether each criterion can fail.
- Check a claim about code against the CODE, never against the spec's account of it. Grep the
  consumers of every name, value or path a spec renames, retires or changes.
- Run a criterion's own command when it is read-only and bounded: a criterion already green before
  the unit is built cannot fail. A command that is a gate, a suite or a `--selftest` run is
  described in your finding, never run: you run no gate (the build method's M6).
- Establish every finding with a probe, and record the command and what it printed.
- Hunt NEW defects. The project's recurring bug classes are a checklist to run, and what a spec
  states as a non-goal or a resolved fork is by design, not a finding.

Done means every finding is concrete enough for a skeptic to re-run: the spec and section, the
evidence, the consequence and a fix.

Return exactly the shape your task block or the harness names; the harness owns the severity rubric
and the probe rules it hands you, and you follow those as written. Leave the owner's wider prose,
and anything outside the specs you were handed, out of what you write and return.

## Task

This handoff is for build `dCalibratedLens`, unit `TOOL-dCalibratedLens-1`.

### input:spec

memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-1.md

### brief:goal

Classify every assumption the named dCalibratedLens specs make about a parent unit, surface, verb,
record or rule as AGREES, MISMATCH or UNKNOWN UNTIL BUILT, against the parents' DEFERRED specs as
they stand on origin/main at `66c5b8dbf`. The parents are dTendedCadence and dFairHearing. The
ancestors in scope are the parents' own parents, and only where a dCalibratedLens spec cites them
directly: dSafePassage (dFairHearing's parent) and dWitnessedBar, dRankedPlan, dWellOiledMachine,
dIndexedDesign and dFurnishedOrders (dTendedCadence's). This is a full cross-read, not a delta: no
parent spec changed after the spec run began, so a delta pass would be empty.

dCalibratedLens's spec run began at `22a8efac3`, the parent of its first spec commit `59d3d8e57`
(2026-11-02). `git diff --name-only 22a8efac3 66c5b8dbf -- memory/builds/<build>/spec/` names nothing
for dTendedCadence, dFairHearing, dSafePassage, dWitnessedBar, dRankedPlan, dIndexedDesign or
dFurnishedOrders. It names four files, all from one commit, `66f7b8d32` (merge `362790f10`,
2026-11-02, the owner's pick on TOOL-dTotalRecall-2 §8 F6), which is NOT in the spec base:

- **TOOL-dWellOiledMachine-6 rev-5:** §8 F4's epoch ask is served by tr2 F6 (a)'s holder verb; §2 S6
  and S7 read the epoch through it.
- **TOOL-dWellOiledMachine-58 rev-5:** §8 F5 resolved through tr2 F6 (a); §2 S4 (c) and S5 read the
  build lease's holder through the holder verb.
- **TOOL-dWellOiledMachine-41 rev-4:** §2 S2's driver check, §5 and §10 read the lease holder through
  the picked verb.
- **TOOL-dTotalRecall-2 rev-7** (a deeper ancestor, in scope only through the rule RH below): §8 F6
  RESOLVED (owner, 2026-11-02) to (a), one read-only holder verb over `read_claims`, widened by
  `epoch`.

No dCalibratedLens spec cites wm6, wm41, wm58 or tr2. `git show 66f7b8d32 -- <spec>` shows what
moved; `git show 22a8efac3:<spec>` reads a parent as this build's spec run read it.

The first population is by citation: every spec that cites a parent or in-scope ancestor unit, as
`TOOL-<build>-<n>`, a bare `<build>-<n>`, or a continuation list (`-3 and -13`), outside the
generated records tables. 28 specs. Every mention of dTendedCadence or dFairHearing by name, with no
unit id (cl1:12-15 "dFairHearing's catalogue", cl1:382, cl10:12 and :366 "dFairHearing's scorer
factory", cl13:324, cl30:368, cl8:256-258), is an assumption too: find the unit that owns what it
names.

The second population is by rule. Three rules bind specs that may never cite the unit stating them:

- **RH, the lease holder and epoch read.** A build lease's `session`, its `lease`-mode class (`mine`
  or foreign) and its `epoch` are read through the one read-only holder verb over `read_claims` that
  tr2 §8 F6 (a) picked, which dTotalRecall's build run asks of dPlacedRequest once (tr2:340-357).
  `unattended.sh --claims` prints fields 1 to 5 only, and none is `session` or `epoch`. No unit files
  a second ask or builds an epoch read of its own (wm6:348-351). A spec that reads a session,
  `lease`-mode class or epoch through `--claims`, parses a lease commit itself, files a second ask
  for the same verb, or reads tr2 F6, wm58 F5 or wm6 F4 as open, is a MISMATCH. A spec that takes and
  releases a lease of its own (a period lease) and reads no other session's holder or epoch is not
  bound: a line under 4. Reading only the holder's node, a segment of the lease key, is not bound
  either. A probe for `--claims`, `read_claims`, `refs/gov/leases`, `epoch`, `lease holder` and
  `--lease` named specs 3, 9, 12 and 15 (cl3:52, cl9:86, cl12:194 "its `Epoch` field, the lease
  epoch", cl15:83, :98, :121, :338, :346). The `epoch` hits in cl1:121, :146 and cl10:114, :317,
  :354 name a release epoch (`govkit.py shipped --epoch`) and are not bound.
- **RK, the cadence key.** A cadence step's program learns its period key from `GOV_CADENCE_KEY`
  (and its cadence from `GOV_CADENCE`), which `run_cadence_period` sets by ask TOOL-dTendedCadence-27;
  with no key it exits 2 `refused: no key` (tc1:68, :135, :197, :251, :301-305; tc11:74). A spec that
  supplies, reads or tests the key in another way, or in a key format the parent does not give, is a
  MISMATCH. Probe hits: specs 2, 3, 22, 27 and 41 (cl22:34, :115; cl41:93).
- **RB, a shared file's parent-changed fact.** Where a dCalibratedLens spec states a fact about a
  file at base (a constant, function, grammar, key, verb or flag, not a line number) that a
  dTendedCadence or dFairHearing unit's §2 Scope changes, the spec must name that unit or say why
  the fact survives it. A spec that relies on the at-base fact and names no parent unit is a
  MISMATCH when the parent's DEFERRED text changes the fact, and UNKNOWN UNTIL BUILT when only the
  parent's build run decides it. A line-number drift alone is never a row. The files both a parent's
  and a dCalibratedLens spec's "Files touched" list name are below, per group.

Verdicts:

- **AGREES:** today's parent text says what the assumption says.
- **MISMATCH:** today's parent text says something else: a renamed or retired surface, a different
  verb or grammar, a section renumbered, a fork resolved another way, a refusal the parent states, or
  a rule above that the spec breaks. Quote both sides with `file:line`, and state in one or two
  sentences the change the dCalibratedLens spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other. Check every assumption the group's specs make about a parent or
in-scope ancestor unit, then apply RH, RK and RB where the group line names them:

- **Group A, led by spec 1:** specs 1, 13, 14 and 24. Cited: fh2 fh3 fh9 fh12 fh13 id3 rp6 sp10 wb11
  wb28. RB files: `tools/workflows/lenses.toml`, `render_lenses.py`, `review_pin.py`,
  `tier2-review.js`, `tier2-review.template.js`, `tier2-review.test.sh`, `tools/workflows/README.md`,
  `tools/workflows/kit.toml`, `tools/roles/roles_lib.py`, `tools/roles/README.md`,
  `tools/policy/catalogue.toml`, `tools/unattended/unattended.sh`, `unattended.test.sh`,
  `VERBS.template.md`, `tools/govkit/selftest.py`, `tools/govkit/subject-pins.tsv`,
  `tools/run-gates/selftest-budgets.txt`, `tools/gate-legs.json`.
- **Group B, led by spec 10:** specs 10, 23, 36, 5 and 8. Cited: fh1 fh8 fh12 fh13 fh25 fo4 fo12 fo17
  tc1 wm32 wm53. RB files: `tools/workflows/replay_scorer.py`, `review_replay.py`,
  `tier2-review.js`, `tier2-review.template.js`, `unattended-build.js`,
  `unattended-build.template.js`, `tools/workflows/README.md`, `tools/workflows/kit.toml`,
  `tools/memory-tree/HYGIENE.template.md`, `tools/memory-tree/record-kinds.toml`,
  `tools/policy/catalogue.toml`, `tools/lib/resolve-python.test.sh`, `help/roles.md`,
  `tools/roles/README.md`, `tools/loop/README.md`, `tools/govkit/registry.toml`,
  `tools/govkit/subject-pins.tsv`, `tools/run-gates/selftest-budgets.txt`, `tools/gate-legs.json`.
- **Group C, led by spec 3:** specs 3, 30, 11, 6, 22 and 41. Cited: tc1 tc2 tc6 tc15 tc25 tc27 tc29
  tc30 rp1 rp6 rp13 rp16 wm4 wm13 wm27 wm48 wm59. RH on 3; RK on 3, 22 and 41. Specs 22 and 41 cite
  no parent unit: check them for RK, for RB, and for any uncited dTendedCadence surface (`maintain.py`,
  `run_cadence_period`, a `cadence.*` or `review.loop.*` policy key) only. RB files:
  `tools/runtime/points.toml`, `tools/memory-tree/record-kinds.toml`,
  `tools/memory-tree/HYGIENE.template.md`, `tools/policy/catalogue.toml`, `tools/runlog/runlog.py`,
  `tools/runlog/README.md`, `tools/runlog/selftest.py`, `tools/loop/README.md`, `tools/roles/README.md`,
  `tools/gate-legs.json`.
- **Group D, led by spec 9:** specs 9, 12, 16, 17, 20, 27 and 28. Cited: wm12 wm16 wm27 wm32 wm33 wm46
  wm47 wm49 wm50 wm52 wm53 wm79. RH on 9 and 12; RK on 27. RB files: `tools/loop/README.md`.
- **Group E, led by spec 2:** specs 2, 4, 7, 15, 26, 37, 46 and 47. Cited: tc27 wb4 wb8 wb11 wb29 wm16
  wm19 wm51 wm53. RH on 15; RK on 2. RB files: `tools/gate-legs.json`, `tools/govkit/registry.toml`,
  `tools/govkit/subject-pins.tsv`, `tools/run-gates/selftest-budgets.txt`, `tools/loop/kit.toml`,
  `tools/loop/README.md`, `tools/policy/catalogue.toml`, `tools/memory-tree/record-kinds.toml`,
  `tools/memory-tree/HYGIENE.template.md`, `tools/runlog/runlog.py`, `tools/runlog/extract.py`,
  `tools/runlog/README.md`, `tools/runlog/selftest.py`, `help/README.md`.

The spec files are `memory/builds/dCalibratedLens/spec/2026-11-0?-spec-TOOL-dCalibratedLens-<n>.md`.
A parent's or ancestor's is `memory/builds/<build>/spec/*-spec-TOOL-<build>-<n>.md`. Read every
mention of a parent or ancestor unit in each of your specs, then the cited parent text, its §9 rev
lines first, then the RB files' lines in the parents' §2 Scope. The precedent cross-check,
`memory/builds/dWellOiledMachine/build/2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md`,
shows the shape and the classes that turned up.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `clN:L` for line L of dCalibratedLens spec N, and `tcN:L`, `fhN:L`, `spN:L`, `wbN:L`,
   `rpN:L`, `wmN:L`, `idN:L`, `foN:L`, `trN:L`, `prN:L` for dTendedCadence, dFairHearing,
   dSafePassage, dWitnessedBar, dRankedPlan, dWellOiledMachine, dIndexedDesign, dFurnishedOrders,
   dTotalRecall and dPlacedRequest spec N. `Rule` is `cite` for a citation assumption (by id or by
   name), else `RH`, `RK` or `RB`. Group a spec's citations of one parent section into one row where
   they rest on the same fact.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dCalibratedLens
   spec needs, then `Cause:` either the revision (the parent text moved in `66f7b8d32`) or
   pre-existing (it already read so at `22a8efac3`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit a rule does not bind, one line saying why.
5. Parent text that looks wrong, one line each with `file:line`: never a row, never edited.

### brief:non-goals

- No file is written: every probe reads.
- No defect in dCalibratedLens's own design that no parent text causes.
- No verdict on a parent spec: parent text that looks wrong is one line under 5, never a row.
- No ancestor beyond the six named, except tr2 rev-7 through RH. A citation of dTotalRecall,
  dDeclaredLoop, dBoundRoles, dKeptSession, dLinkedLibrary, dPlacedRequest or dGroundRules is not a
  row.
- No line-number drift alone as a row.

### Charter rules

- [spec] Spec before code: every product-code unit commits its spec first, a micro-spec for a mechanical change and a full design pass for a substantive one.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [gate] A gate never seen red is not a gate: observe its failing case, state what it does not check, and never read a skip, an unmovable probe, an exemption or an empty population as coverage.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [docs] A user-facing change is not done until its page under `help/` is current.
- [security] Security first: validate once at the write boundary, deny by default, give automation the narrowest grant, and keep secrets out of files, memory and chat.
- [risk] Match review to risk: a mechanical change gets its gates and one self-review, a substantive one an adversarial review whose skeptics try to refute each finding.

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

### Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
