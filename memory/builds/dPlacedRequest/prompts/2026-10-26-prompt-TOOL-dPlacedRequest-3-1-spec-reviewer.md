**Serves:** journal TOOL-dPlacedRequest-3

# gov-spec-reviewer handoff — TOOL-dPlacedRequest-3

<!-- gov:handoff role=gov-spec-reviewer build=dPlacedRequest unit=TOOL-dPlacedRequest-3 path=memory/builds/dPlacedRequest/prompts/2026-10-26-prompt-TOOL-dPlacedRequest-3-1-spec-reviewer.md role-sha=a81df30406a1 task-sha=ab334695b326 -->

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

This handoff is for build `dPlacedRequest`, unit `TOOL-dPlacedRequest-3`.

### input:spec

memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-3.md

### brief:goal

Classify every assumption the 14 exposed dPlacedRequest specs make about a dDeclaredLoop unit or a
dOrderedCharter unit as AGREES, MISMATCH or UNKNOWN UNTIL BUILT. Compare against dDeclaredLoop's
specs as this branch's dDeclaredLoop re-ground commit leaves them
(`git log -1 -- memory/builds/dDeclaredLoop/spec`), and against dOrderedCharter's specs as they stand
on origin/main at `462d20f35`.

dPlacedRequest's spec run began at `5352805c8`, which holds dOrderedCharter's re-ground
(`c63aabbb4`) but not the owner's fork picks (`1e9b2dad5`, landed as `60d60e694`). For
dOrderedCharter, check only the units those picks revised: 1, 6, 7, 11, 15, 19, 31, 32, 33, 34, 35,
36 and 46 (`git show 1e9b2dad5 -- <spec>`). dDeclaredLoop's re-ground revised 20 units: 1 to 6, 12,
16, 17, 18, 22, 24 to 28, 33, 34, 46 and 56. Its record,
`memory/builds/dDeclaredLoop/build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`,
and each revised spec's new §9 line say what moved (`git show <that commit> -- <spec>`).

The exposed specs, by the units each cites (`dl` dDeclaredLoop, `oc` dOrderedCharter, each as
`<FAMILY>-<build>-<n>` or a bare `<build>-<n>`): 1 (dl3) · 2 (dl3, dl6, oc7) · 3 (dl1, dl12, dl16,
dl24, dl33) · 4 (dl16, dl27) · 5 (dl16) · 6 (dl12, dl18, oc19) · 7 (dl6, dl12, dl17, dl26, oc7) · 8
(dl1, dl12, dl24, oc36) · 9 (dl3, oc15, oc31, oc32) · 10 (dl3, dl27) · 14 (dl33) · 18 (oc19) · 21
(dl3, dl16, dl27, dl33, oc7) · 34 (oc19).

Verdicts:

- **AGREES:** the parent text the assumption names says the same thing today, whether or not a
  re-ground touched that unit.
- **MISMATCH:** today's parent text says something different: a renamed surface, a moved reader, a
  fork resolved another way, a key read at another revision, a refusal the parent now states, a
  file that no longer exists. Quote both sides with `file:line`, and state in one or two sentences
  the change the dPlacedRequest spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check
every spec of that group, and no other:

- **Group A, led by spec 3:** specs 1, 2, 3, 4, 5, 10 and 14.
- **Group B, led by spec 7:** specs 6, 7, 8, 9, 18, 21 and 34.

The spec files are `memory/builds/dPlacedRequest/spec/2026-10-2?-spec-TOOL-dPlacedRequest-<n>.md`,
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md` and
`memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`. Read every mention
of a parent unit in each of your specs, then the cited parent text at the lines it names, its §9 rev
lines first.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Verdict | Evidence |`,
   with `prN:L` for line L of dPlacedRequest spec N, `dlN:L` for dDeclaredLoop spec N and `ocN:L`
   for dOrderedCharter spec N.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dPlacedRequest spec
   needs, then `Cause:` either a re-ground (the parent text moved after `5352805c8`) or pre-existing
   (it already read so at `5352805c8`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. One line per spec: the revised parent units it cites that none of its assumptions depend on.

### brief:non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent revision restates one of their
  surfaces that the dPlacedRequest spec relies on through it.
- No defect in dPlacedRequest's own design that a parent does not cause.
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
