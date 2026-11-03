**Serves:** journal TOOL-dCalibratedLens-16

# gov-spec-reviewer handoff — TOOL-dCalibratedLens-16

<!-- gov:handoff role=gov-spec-reviewer build=dCalibratedLens unit=TOOL-dCalibratedLens-16 path=memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-16-1-spec-reviewer.md role-sha=a81df30406a1 task-sha=090000d5819a -->

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

This handoff is for build `dCalibratedLens`, unit `TOOL-dCalibratedLens-16`.

### input:spec

memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-16.md

### brief:goal

Classify every assumption the named dCalibratedLens specs make about a dTotalRecall or dDeclaredLoop
unit, surface, verb, record or rule as AGREES, MISMATCH or UNKNOWN UNTIL BUILT, against those builds'
DEFERRED specs as they stand on origin/main at `0d1c1dda4`. Both are deeper ancestors of
dCalibratedLens, which the first pass scoped out: its record is
`memory/builds/dCalibratedLens/build/2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck.md`.
This is a full cross-read, not a delta.

dCalibratedLens's spec run began at `22a8efac3`. Since then
`git diff --name-only 22a8efac3 0d1c1dda4 -- memory/builds/dTotalRecall/spec/ memory/builds/dDeclaredLoop/spec/`
names two files:

- **tr2, TOOL-dTotalRecall-2:** rev-7 (`66f7b8d32`, §8 F6 resolved by the owner to one read-only holder
  verb), then rev-8 (`58b395b6e`, the holder is read through TOOL-dPlacedRequest-34 S22's
  `--lease status`, and the F6 ask narrows to a seventh TAB field).
- **TOOL-dTotalRecall-1 rev-5** (`58b395b6e`): `hand` stays legal on any row tr2 S9 does not move.

`git show 22a8efac3:<spec>` reads an ancestor as this build's spec run read it. A MISMATCH whose
ancestor text moved in one of those two commits has Cause `revision`; any other is `pre-existing`.

The population is by citation: every spec that cites a dTotalRecall or dDeclaredLoop unit, as
`TOOL-<build>-<n>`, a bare `<build>-<n>` or a continuation list, outside the generated records
tables. 24 specs. A mention by name with no unit id is an assumption too: find the unit that owns
what it names. The name-only hits are cl1:40, :108, :128 and :436-441, cl3:325 and :527-530,
cl5:147, cl6:80, :286 and :338-342, cl7:93, cl19:122, cl20:75, and the H1 lines of cl32 and cl42.

Two checks ride the citations:

- **Asks filed on these builds.** cl1 §8 F4, cl3 §8 F2, cl6 §8 F4 and cl7 §8 F2 each name an ask that
  dTotalRecall or dDeclaredLoop is to serve. Check that the named BACKLOG row exists in that build's
  `BACKLOG.md` and says what the spec relies on, and whether the ancestor's DEFERRED spec already
  serves or refuses it. A spec that relies on an ask no BACKLOG holds is a MISMATCH.
- **RB, a shared file's ancestor-changed fact.** Where a dCalibratedLens spec states a fact about a
  file at base (a constant, function, grammar, key, verb or flag, not a line number) that a CITED
  dTotalRecall or dDeclaredLoop unit's §2 Scope changes, the spec must name that unit or say why the
  fact survives it. Compare each of your specs' "Files touched" with the cited units' §2 only. A
  line-number drift alone is never a row.

The lease rule RH of the first pass is not re-run: `0d1c1dda4` moves no row it read, and no
dCalibratedLens spec cites tr2.

Verdicts:

- **AGREES:** today's ancestor text says what the assumption says.
- **MISMATCH:** today's ancestor text says something else: a renamed or retired surface, a different
  verb or grammar, a section renumbered, a fork resolved another way, a refusal the ancestor states,
  or an ask no BACKLOG holds. Quote both sides with `file:line`, and state in one or two sentences
  the change the dCalibratedLens spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the ancestor's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other:

- **Group A, led by spec 14:** specs 14, 13, 9, 10, 11 and 15. Cited: dl1 dl7 dl16 dl20 dl24 dl26
  dl27 dl28 dl32 tr9 tr11 tr12 tr17.
- **Group B, led by spec 6:** specs 6, 5, 28, 48 and 8. Cited: dl2 dl12 dl20 tr1 tr9 tr12 tr14 tr17
  tr35 tr42.
- **Group C, led by spec 7:** specs 7, 33, 34 and 32. Cited: dl20 tr1 tr11 tr42 tr53.
- **Group D, led by spec 16:** specs 16, 2, 19 and 4. Cited: dl1 dl2 dl3 dl7 dl12 dl27 dl30 tr1 tr9
  tr42.
- **Group E, led by spec 1:** specs 1, 35, 3, 20 and 42. Cited: dl12 dl19 dl20 dl50 tr1 tr11 tr18 tr42
  tr53.

The spec files are `memory/builds/dCalibratedLens/spec/2026-11-0?-spec-TOOL-dCalibratedLens-<n>.md`.
An ancestor's is `memory/builds/<build>/spec/*-spec-TOOL-<build>-<n>.md`. Read every mention in each
of your specs, then the cited ancestor text, its §9 rev lines first. Seventeen specs were revised by
the first pass's re-ground on 2026-11-03: read them as they stand now, rev lines included. The
first-pass record shows the shape and the classes that turned up.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the ancestor | Rule | Verdict | Evidence |`,
   with `clN:L` for line L of dCalibratedLens spec N, and `trN:L`, `dlN:L` for dTotalRecall and
   dDeclaredLoop spec N (`prN:L` and the first pass's short forms for any other build a cited line
   leads to). `Rule` is `cite` for a citation assumption (by id or by name), `ask` for an ask check,
   else `RB`. Group a spec's citations of one ancestor section into one row where they rest on the
   same fact.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dCalibratedLens
   spec needs, then `Cause:` either `revision` (the ancestor text moved in `66f7b8d32` or
   `58b395b6e`) or `pre-existing`.
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Ancestor text that looks wrong, one line each with `file:line`: never a row, never edited.

### brief:non-goals

- No file is written: every probe reads.
- No defect in dCalibratedLens's own design that no ancestor text causes.
- No verdict on an ancestor spec: text that looks wrong is one line under 4, never a row.
- No build other than dTotalRecall and dDeclaredLoop as a row's subject; a first-pass parent is
  read only where a cited line leads to it.
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
