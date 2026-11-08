**Serves:** journal TOOL-dScopedBuild-1

# gov-spec-reviewer handoff — TOOL-dScopedBuild-1

<!-- gov:handoff role=gov-spec-reviewer build=dScopedBuild unit=TOOL-dScopedBuild-1 path=memory/builds/dScopedBuild/prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-1-spec-reviewer.md role-sha=a81df30406a1 task-sha=4f0fafd05d6e -->

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

This handoff is for build `dScopedBuild`, unit `TOOL-dScopedBuild-1`.

### input:spec

memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-1.md

### brief:goal

Classify every assumption the named dScopedBuild specs make about a revised parent unit as AGREES,
MISMATCH or UNKNOWN UNTIL BUILT, against the parents' specs as they stand on origin/main at
`66c5b8dbf`. dScopedBuild's spec run began at `5f0b11f12`, the parent of its first spec commit
`807775940`. That base holds every earlier re-ground merge (dWitnessedBar `191ba7ab5`, dTotalRecall
`2bd5e10d4`, dLinkedLibrary `933e67399`, dFurnishedOrders `57bc3b918`, dWellOiledMachine `0c0f3a183`,
dRankedPlan `7d0f5b756`) and the fork picks `ccd1292ea`. It does not hold merge `362790f10`
(2026-11-02, commit `66f7b8d32`), the owner's pick on TOOL-dTotalRecall-2 §8 F6. That one commit is the
only change to any spec of the four parents (dIndexedDesign, dWitnessedBar, dWellOiledMachine,
dFurnishedOrders) between `5f0b11f12` and `66c5b8dbf`; `git diff --name-only 5f0b11f12 66c5b8dbf --
memory/builds/<parent>/spec/` names nothing else, and dIndexedDesign's specs are byte-identical. It
revised three parent units, and one grandparent unit they read:

- **TOOL-dWellOiledMachine-6 rev-5:** §8 F4's epoch ask is served by tr2 F6 (a)'s holder verb; §2 S6
  and S7 read the epoch through it (wm6:97-111, :338-351, :366-369).
- **TOOL-dWellOiledMachine-58 rev-5:** §8 F5 resolved through tr2 F6 (a); §2 S4 (c) and S5 read the
  build lease's holder through the holder verb (wm58:76-84, :353-359, :372-374).
- **TOOL-dWellOiledMachine-41 rev-4:** §2 S2's driver check, §5 and §10 read the lease holder through
  the picked verb (wm41:45-55, :172-173, :239-242, :247-248).
- **TOOL-dTotalRecall-2 rev-7** (not a parent; the three above read it): §8 F6 RESOLVED (owner,
  2026-11-02) to (a), one read-only holder verb over `read_claims`, widened by `epoch`
  (tr2:340-356).

The deviation records are
`memory/builds/dTotalRecall/build/2026-11-02-build-TOOL-dTotalRecall-2-deviation-24.md` and
`memory/builds/dWellOiledMachine/build/2026-11-02-build-TOOL-dWellOiledMachine-{6-deviation-64,41-deviation-413,58-deviation-584}.md`.
`git show 66f7b8d32 -- <spec>` shows what moved; `git show 5f0b11f12:<spec>` reads a parent as this
build's spec run read it.

The first population is by citation: every spec that cites a revised unit, as `TOOL-<build>-<n>` or a
bare `<build>-<n>` (2 specs): 1 (wm6, the executor's transition record) · 7 (wm6 S1 and S8,
`point.command-adapters`, `points.toml`). None cites wm58, wm41 or tr2.

The second population is by rule. The revision applies one rule that binds specs which never cite the
unit stating it:

- **RH, the lease holder and epoch read.** A build lease's `session`, its `lease`-mode class (`mine` or
  foreign) and its `epoch` are read through the one read-only holder verb over `read_claims` that
  tr2 §8 F6 (a) picked, which dTotalRecall's build run asks of dPlacedRequest once (tr2:348-356).
  `unattended.sh --claims` prints fields 1 to 5 only, and none of them is `session` or `epoch`
  (pr1:204-208). No unit files a second ask or builds an epoch read of its own (wm6:348-351). A spec
  that reads a session, `lease`-mode class or epoch through `--claims`, parses a lease commit itself,
  files a second ask, or still reads tr2 F6, wm58 F5 or wm6 F4 as open, is a MISMATCH when it relies
  on one of the revised units for that read.

A text probe for `--claims`, `read_claims`, `holder`, `epoch`, `refs/gov/leases`, `lease` and `§8 F6`
over all 34 specs named no candidate: its one hit, spec 5's "§8 F6", is that spec's own fork. Apply RH
to specs 1 and 7 anyway, and if, reading them, you meet a lease read elsewhere in the set, report it
under 4 with its `file:line`.

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not the revision touched
  it.
- **MISMATCH:** today's parent text says something else: a moved reader, a fork resolved another way,
  a section renumbered, or RH broken. Quote both sides with `file:line`, and state in one or two
  sentences the change the dScopedBuild spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

One group, one reviewer, led by spec 1: specs 1 and 7. Check every assumption each makes about wm6
(and any wm58, wm41 or tr2 surface it reaches through it), and RH.

The spec files are `memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-<n>.md`. The
revised parents' are `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-{6,41,58}.md`
and `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md`. Read every mention of a
revised unit in each of your specs, then the cited parent text, its §9 rev lines first. The precedent
cross-check,
`memory/builds/dWellOiledMachine/build/2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md`,
shows the shape.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `sbN:L` for line L of dScopedBuild spec N, `wmN:L` for dWellOiledMachine spec N and `trN:L`
   for dTotalRecall spec N. `Rule` is `cite` for a citation assumption, else `RH`.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dScopedBuild spec
   needs, then `Cause:` either the revision (the parent text moved in `66f7b8d32`) or pre-existing (it
   already read so at `5f0b11f12`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit RH does not bind, one line saying why.
5. One line per citation spec: the revised parent sections it cites that none of its assumptions
   depend on.

### brief:non-goals

- No file is written: every probe reads.
- No re-audit of rules the earlier re-grounds applied (dWellOiledMachine's brief's R1 to R9): those
  parents were in this build's base, and its own spec run read them.
- No defect in dScopedBuild's own design that no revised parent unit causes.
- No verdict on a parent spec: parent text that looks wrong is one line under 4, never a row.

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
