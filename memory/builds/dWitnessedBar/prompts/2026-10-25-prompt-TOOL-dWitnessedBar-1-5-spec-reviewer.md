**Serves:** journal TOOL-dWitnessedBar-1

# gov-spec-reviewer handoff — TOOL-dWitnessedBar-1

<!-- gov:handoff role=gov-spec-reviewer build=dWitnessedBar unit=TOOL-dWitnessedBar-1 path=memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-5-spec-reviewer.md role-sha=a81df30406a1 task-sha=7d151b9ed5d5 -->

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

This handoff is for build `dWitnessedBar`, unit `TOOL-dWitnessedBar-1`.

### input:spec

memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-1.md

### brief:goal

Classify every assumption the 26 exposed dWitnessedBar specs make about a dOrderedCharter unit or a
dDeclaredLoop unit as AGREES, MISMATCH or UNKNOWN UNTIL BUILT. Compare against dOrderedCharter's specs
as they stand on origin/main at `462d20f35`, and against dDeclaredLoop's specs as this branch's
dDeclaredLoop re-ground commit leaves them (`git log -1 -- memory/builds/dDeclaredLoop/spec`).

dWitnessedBar's spec run began at `ad002a024`, which holds neither dOrderedCharter's re-ground
(`555e623a7`, landed as `c63aabbb4`) nor the owner's fork picks (`1e9b2dad5`, landed as
`60d60e694`). Those two commits revised 27 dOrderedCharter units: 1, 2, 3, 4, 6, 7, 9, 11, 14, 15,
19, 20, 25, 26, 27, 30, 31, 32, 33, 34, 35, 36, 37, 46, 49, 50 and 55. Each revised spec's §9 rev-4
and rev-5 lines say what moved. dDeclaredLoop's re-ground revised 20 units: 1 to 6, 12, 16, 17, 18,
22, 24 to 28, 33, 34, 46 and 56. Its record,
`memory/builds/dDeclaredLoop/build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`,
and each revised spec's new §9 line say what moved.

The exposed specs, by the units each cites (`oc` dOrderedCharter, `dl` dDeclaredLoop, each as
`<FAMILY>-<build>-<n>` or a bare `<build>-<n>`): 1 (oc7) · 2 (oc7) · 3 (oc7, dl12) · 4 (dl3, dl12)
· 6 (oc6, dl2, dl6) · 7 (dl6, dl12) · 8 (oc7, dl16) · 11 (oc1, oc7, oc19, oc50) · 12 (oc15, oc19,
oc50, dl18) · 13 (oc19) · 14 (oc7, oc50) · 15 (dl1, dl12) · 16 (oc50) · 17 (oc50) · 18 (oc19, oc20,
oc26, oc50) · 19 (oc50) · 22 (oc7, oc19, oc50) · 23 (dl12, dl22) · 24 (oc7, oc19, oc30) · 25 (oc7)
· 28 (oc35, oc36) · 30 (dl16, dl33) · 46 (oc50) · 51 (oc50) · 56 (dl2) · 84 (oc3).

Verdicts:

- **AGREES:** the parent text the assumption names says the same thing today, whether or not a
  re-ground touched that unit.
- **MISMATCH:** today's parent text says something different: a renamed surface, a moved reader, a
  fork resolved another way, a key read at another revision, a refusal the parent now states, a
  file that no longer exists. Quote both sides with `file:line`, and state in one or two sentences
  the change the dWitnessedBar spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check
every spec of that group, and no other:

- **Group A, led by spec 1:** specs 1, 2, 11, 13, 14, 16, 17 and 18 (dOrderedCharter only).
- **Group B, led by spec 19:** specs 19, 22, 24, 25, 28, 46, 51 and 84 (dOrderedCharter only).
- **Group C, led by spec 3:** specs 3, 4, 6, 7, 8, 12, 15, 23, 30 and 56 (both parents).

The spec files are `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md`,
`memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md` and
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`. Read every mention of
a parent unit in each of your specs, then the cited parent text at the lines it names, its §9 rev
lines first. For dOrderedCharter, `git show 555e623a7 -- <spec>` and `git show 1e9b2dad5 -- <spec>`
show what each revision moved. For dDeclaredLoop, `git show <its re-ground commit> -- <spec>` does.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Verdict | Evidence |`,
   with `wbN:L` for line L of dWitnessedBar spec N, `ocN:L` for dOrderedCharter spec N and `dlN:L`
   for dDeclaredLoop spec N.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dWitnessedBar spec
   needs, then `Cause:` either the re-ground (the parent text moved after `ad002a024`) or
   pre-existing (it already read so at `ad002a024`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. One line per spec: the revised parent units it cites that none of its assumptions depend on.

### brief:non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent revision restates one of their
  surfaces that the dWitnessedBar spec relies on through it.
- No defect in dWitnessedBar's own design that a parent does not cause.
- No verdict about a parent unit no re-ground revised, unless the exposed spec's assumption about it
  depends on a revised unit.

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
