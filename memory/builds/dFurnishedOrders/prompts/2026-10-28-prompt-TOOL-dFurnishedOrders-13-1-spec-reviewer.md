**Serves:** journal TOOL-dFurnishedOrders-13

# gov-spec-reviewer handoff — TOOL-dFurnishedOrders-13

<!-- gov:handoff role=gov-spec-reviewer build=dFurnishedOrders unit=TOOL-dFurnishedOrders-13 path=memory/builds/dFurnishedOrders/prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-13-1-spec-reviewer.md role-sha=a81df30406a1 task-sha=bc39a4756cf1 -->

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

This handoff is for build `dFurnishedOrders`, unit `TOOL-dFurnishedOrders-13`.

### input:spec

memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-13.md

### brief:goal

Classify every assumption the named dFurnishedOrders specs make about a parent unit as AGREES,
MISMATCH or UNKNOWN UNTIL BUILT, against the parents' specs as they stand on origin/main at
`1a61f21a2`. dFurnishedOrders' spec run began at `1a3ce03dd`, the parent of its first spec commit
`4d726ef27`. That base holds the second wave's re-grounds (dDeclaredLoop, dWitnessedBar,
dPlacedRequest) but none of the third wave's:

- **dBoundRoles**, the parent, re-grounded at `ac8ab8d5f` and landed as `fffe4aadf`. It revised units
  1, 2, 3, 5, 6, 11, 12, 14, 20, 21, 22, 23, 25, 43 and 60. Its record,
  `memory/builds/dBoundRoles/build/2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck.md`, and
  each revised spec's new §9 line say what moved.
- **dTotalRecall**, which specs 11, 17, 41 and 45 cite, re-grounded at `794a0f5fb` and landed as
  `2bd5e10d4`. It revised units 1, 2, 4, 8, 9, 11, 15, 18, 19, 20, 22, 25, 26, 43 and 76. Its record
  is `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck.md`.
- **dKeptSession**, which specs 42 and 46 cite, re-grounded at `ff44fb2a2` and landed as `0689e7fa1`.
  It revised units 1, 5, 7, 8, 9, 10, 11, 12, 13, 18, 20, 25, 36, 44 and 56. Its record is
  `memory/builds/dKeptSession/build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md`.

The first population is by citation: every spec that cites a revised unit, as `<FAMILY>-<build>-<n>`
or a bare `<build>-<n>` (30 specs). By the revised units each cites (`br` dBoundRoles, `tr`
dTotalRecall, `ks` dKeptSession): 1 (br12) · 2 (br2, br5, br21, br22) · 3 (br5) · 4 (br3, br23) · 5
(br1, br2, br3, br20, br21) · 6 (br5, br25) · 7 (br2, br5, br11) · 8 (br1, br2, br21) · 9 (br1, br3,
br20) · 10 (br5) · 11 (tr9) · 12 (br1, br2, br3) · 14 (br3, br25) · 15 (br1, br2, br5, br43) · 16
(br11, br21) · 17 (tr8) · 18 (br3, br21, br23) · 19 (br2, br3, br5) · 20 (br3, br23) · 22 (br1, br2) ·
24 (br5) · 27 (br11) · 28 (br11) · 29 (br5, br20, br21) · 32 (br1) · 37 (br5) · 41 (tr20) · 42 (br1,
br5, br43, ks44) · 45 (tr20) · 46 (ks44).

The second population is by rule (21 specs). The parents' re-grounds applied rules that bind specs
that never cite the unit stating them. A text probe over the other 30 specs named these candidates,
by the rule each hit: 23, 30, 48, 50, 52, 53, 54, 55, 56, 58, 59, 60 and 61 (a leg named,
`tools/gate-legs.json` edited or `enforces` missing), 13, 25, 26, 31, 33, 34, 39, 48, 54, 58 and 61 (a
module of another kit named, `sys.path`, `importlib` or an in-process read), and 49 and 60 (budget
contention). The probe is a heuristic. Verify every hit: a hit the rule does not bind, such as the
roles kit importing its own `roles_lib`, is a line in your return, not a row.

The rules, each as the parents now apply it. The parent specs win where this summary differs; the
full statements, with their parent cites, are the R1 to R8 bullets of
`memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md`:

- **R1, a new leg's `enforces`.** PLAY-dOrderedCharter-7 S3 reds a leg with no `enforces`, and the
  pending list only shrinks after dOrderedCharter's pass (oc7:58-63), so a later build cannot excuse
  its leg there. dWitnessedBar unit 11 declares each leg once, in its kit's `[[gate_leg]]` row or a
  `tools/govkit/registry.toml` `[[exempt_leg]]` row, and `leg_factory.py --write` renders
  `tools/gate-legs.json`. The re-grounds gave br25's and br60's legs, and every dTotalRecall leg,
  their `enforces`, and moved tr8's leg to memory-tree's `kit.toml`. A spec that adds,
  reshapes or re-guards a leg by hand in `tools/gate-legs.json`, or names no `enforces` for it, is a
  MISMATCH.
- **R2, a typed record kind.** PLAY-dOrderedCharter-42 S2, S3 and S5 make `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the factory's kind list, read a `-<kind>-<n>.md` file whose Serves
  kind differs as malformed, and keep the closed list in the HYGIENE template. No parent claims a
  `build_records.py new <kind>` door: a writer names the parent's own command or the factory and its
  per-kind flags (tr1, tr43 S4). tr1 now rows the four untyped tokens and joins the typed ones through
  `TYPED_RECORD_KINDS`; tr25 makes `stream-plan` typed; tr4's routing region routes every typed kind. A
  spec that adds a kind without joining all three, serves a typed record as `journal`, names a
  `new <kind>` door, or reads a parent's record under a kind the parent no longer serves, is a
  MISMATCH.
- **R3, a sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205;
  wb28:63-64). Code in one kit reaches another kit's verb by subprocess, found through an inline
  `resolve_kit_dir`; a policy key is read by `policy.py get` as a subprocess (oc7:379-380). The third
  wave applied it everywhere: dTotalRecall's govkit steps reach memory-tree and the playbook kit by
  subprocess or a fork (tr18, tr20), dBoundRoles' cross-kit reads go through roles-kit verbs
  (`handoff.py check-return-file`, `check_roles.py --print-tag-rows`, `check_roles.py
  --check-actor-patch`, `handoff.py agent-return`) or a declared `requires_if` row (br25), and
  dKeptSession's hooks spawn `policy-mirror.js get`. A spec whose code imports or calls another kit's
  module in process, or puts another kit's directory on `sys.path`, is a MISMATCH unless a declared
  `requires_if` row admits it. Which kit a spec's code lives in is read from its Files touched. dBoundRoles' re-ground also
  gave br21's `read_policy_setting` a `with_default` argument, br43 making it the one caller of
  `get`.
- **R4, the loop program's rows.** dl12 S1 to S3: an item belongs to its own step's table; every input
  names a layer tag of `tools/playbook/layers.toml`; `returns` names a `record-kind.*` tag; `routes`
  holds exactly the outcomes as keys.
- **R5 to R8**, as the dTotalRecall brief states them, with R7 as br6 and br23 now apply it
  (`tools/loop/guard.py --staged` the pre-commit verdict): no `new disposition` door (dl16), every overlay
  composition read at `--rev HEAD` (oc46 S6, oc35 S5), dl2's guard reads no trailer at pre-commit, and
  dl3 S2's witness channels with dl33 S3's budget edges. dPlacedRequest's `--claims` prints fields 1 to
  5 only, and `read_claims` fetches `refs/gov/leases/*` from the remote (pr1:206-208, :76-77).

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not a re-ground touched
  it.
- **MISMATCH:** today's parent text says something else: a renamed surface, a moved reader, a fork
  resolved another way, a refusal the parent now states, or a rule above that the spec breaks. Quote
  both sides with `file:line`, and state in one or two sentences the change the dFurnishedOrders spec
  needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other. A citation group checks every assumption about a revised unit and
applies R1 to R8 to its own specs. A rule-wide group checks only R1 to R8, on the hits named above:

- **Group A1, citation, led by spec 1:** specs 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15 and 16.
- **Group A2, citation, led by spec 17:** specs 17, 18, 19, 20, 22, 24, 27, 28, 29, 32, 37, 41, 42, 45
  and 46.
- **Group B, rule-wide, led by spec 13:** specs 13, 23, 25, 26, 30, 31, 33, 34, 39, 48, 49, 50, 52, 53,
  54, 55, 56, 58, 59, 60 and 61.

The spec files are `memory/builds/dFurnishedOrders/spec/2026-10-2?-spec-TOOL-dFurnishedOrders-<n>.md`.
The parents' are `memory/builds/dBoundRoles/spec/2026-10-2?-spec-TOOL-dBoundRoles-<n>.md`,
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-<n>.md`,
`memory/builds/dKeptSession/spec/2026-10-2?-spec-KICK-dKeptSession-<n>.md`, and for the rules
`memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`,
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`,
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md` and
`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`. Read every mention of
a parent unit in each of your specs, then the cited parent text, its §9 rev lines first.
`git show <re-ground commit> -- <spec>` shows what each re-ground moved; `git show 1a3ce03dd:<spec>`
reads a parent as dFurnishedOrders' spec run read it.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `foN:L` for line L of dFurnishedOrders spec N, `brN:L` for dBoundRoles spec N, `trN:L` for
   dTotalRecall spec N, `ksN:L` for dKeptSession spec N, and `ocN:L`, `dlN:L`, `wbN:L`, `prN:L` for the ancestors. `Rule` is `cite` for
   a citation assumption, else the R-number.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dFurnishedOrders spec
   needs, then `Cause:` either the re-ground (the parent text moved in the re-ground commit) or
   pre-existing (it already read so at `1a3ce03dd`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit the rule does not bind, one line saying why.
5. One line per citation spec: the revised parent units it cites that none of its assumptions depend
   on.

### brief:non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent restates one of their surfaces
  that the dFurnishedOrders spec relies on through it.
- No defect in dFurnishedOrders' own design that no parent causes.
- No verdict about dLinkedLibrary, the sibling build cross-checked beside this one.

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
