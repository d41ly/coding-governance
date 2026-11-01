**Serves:** journal TOOL-dWellOiledMachine-38

# gov-spec-reviewer handoff — TOOL-dWellOiledMachine-38

<!-- gov:handoff role=gov-spec-reviewer build=dWellOiledMachine unit=TOOL-dWellOiledMachine-38 path=memory/builds/dWellOiledMachine/prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-38-1-spec-reviewer.md role-sha=a81df30406a1 task-sha=f3eb13771a2b -->

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

This handoff is for build `dWellOiledMachine`, unit `TOOL-dWellOiledMachine-38`.

### input:spec

memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-38.md

### brief:goal

Classify every assumption the named dWellOiledMachine specs make about a parent unit as AGREES,
MISMATCH or UNKNOWN UNTIL BUILT, against the parents' specs as they stand on origin/main at
`d1721ef20`. dWellOiledMachine's spec run began at `ab864dfc8`, the parent of its first spec commit
`4bc4aaf90`. That base holds dKeptSession's re-ground (`0689e7fa1`) and the second wave's, but not
these two:

- **dBoundRoles** re-grounded at `ac8ab8d5f`, landed as `fffe4aadf`. It revised units 1, 2, 3, 5, 6,
  11, 12, 14, 20, 21, 22, 23, 25, 43 and 60. Its record is
  `memory/builds/dBoundRoles/build/2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck.md`, and
  each revised spec's newest §9 line says what moved.
- **dTotalRecall** re-grounded at `794a0f5fb`, landed as `2bd5e10d4`. It revised units 1, 2, 4, 8, 9,
  11, 15, 18, 19, 20, 22, 25, 26, 43 and 76. Its record is
  `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck.md`.

Spec 127 was written after both merges and is out of scope.

The first population is by citation: every spec that cites a revised unit, as `TOOL-<build>-<n>` or
a bare `<build>-<n>` (23 specs). By the revised units each cites (`br` dBoundRoles, `tr`
dTotalRecall): 3 (tr1) · 4 (tr1) · 7 (br3, br22, br25) · 8 (br5, tr1, tr2) · 9 (br22) · 11 (tr2) · 16
(tr18) · 19 (br22, br25, tr2, tr11) · 27 (tr19) · 30 (tr11) · 32 (tr1, tr2, tr9) · 34 (tr9) · 39
(tr19) · 42 (br1) · 43 (br22, br25) · 44 (tr9) · 45 (br22) · 48 (br11) · 51 (tr9) · 53 (tr9) · 54
(br2, br21, tr25) · 56 (br21) · 58 (tr1, tr2).

The second population is by rule (44 specs). The re-grounds applied rules that bind specs that never
cite the unit stating them. A text probe over the other 102 specs named these candidates, by the rule
each hit:

- R1: 1, 2, 12, 17, 20, 23, 31, 33, 38, 79, 90, 94, 97 and 108.
- R2: 22 and 92.
- R3: 1, 5, 10, 15, 17, 47, 57, 64, 81, 90, 93, 96, 108 and 126.
- R4: 12, 20, 22, 61, 74 and 79.
- R5: 97. R6: 26 and 36. R7: 31 and 61.
- R8: 1, 2, 5, 6, 10, 12, 13, 17, 21, 23, 24, 25, 28, 29, 31, 38, 40, 41, 46, 49, 57, 59, 79, 90, 97
  and 108.
- R9: 1, 10, 14, 33, 40, 41, 49, 55, 59.

The probe is a heuristic. Verify every hit: a hit the rule does not bind, such as the roles kit
importing its own `roles_lib`, or the word `budget` meaning something other than dl33's edges, is a
line in your return, not a row.

The rules, as the parents now apply them. The parent specs win where this summary differs:

- **R1, a new leg's `enforces`.** PLAY-dOrderedCharter-7 S3 reds a leg with no `enforces`, and the
  pending list only shrinks after dOrderedCharter's pass (oc7:58-63), so a later build cannot excuse
  its leg there. dWitnessedBar unit 11 declares each leg once, in its kit's `[[gate_leg]]` row or a
  `tools/govkit/registry.toml` `[[exempt_leg]]` row, and `leg_factory.py --write` renders
  `tools/gate-legs.json` (wb11:36-49, :154). The re-grounds gave br25's and br60's legs, and every
  dTotalRecall leg, their `enforces`, and moved tr8's leg to memory-tree's `kit.toml`. A spec that
  adds, reshapes or re-guards a leg by hand in `tools/gate-legs.json`, or names no `enforces` for it,
  is a MISMATCH.
- **R2, a typed record kind.** PLAY-dOrderedCharter-42 S2, S3 and S5 make `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the factory's kind list, read a `-<kind>-<n>.md` file whose Serves
  kind differs as malformed, and keep the closed list in the HYGIENE template. No parent claims a
  `build_records.py new <kind>` door: a writer names the parent's own command or the factory and its
  per-kind flags (tr1, tr43 S4). tr1 now rows the four untyped tokens and joins the typed ones through
  `TYPED_RECORD_KINDS`; tr25 makes `stream-plan` typed; tr4's routing region routes every typed kind.
  A spec that adds a kind without joining all three, serves a typed record as `journal`, names a
  `new <kind>` door, or reads a parent's record under a kind the parent no longer serves, is a
  MISMATCH.
- **R3, a sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205;
  wb28:63-64). Code in one kit reaches another kit's verb by subprocess, found through an inline
  `resolve_kit_dir`; a policy key is read by `policy.py get` as a subprocess (oc7:379-380). The re-grounds
  applied it everywhere: dTotalRecall's govkit steps reach memory-tree and the playbook kit by
  subprocess or a fork (tr18, tr20), dBoundRoles' cross-kit reads go through roles-kit verbs
  (`handoff.py check-return-file`, `check_roles.py --print-tag-rows`, `check_roles.py
  --check-actor-patch`, `handoff.py agent-return`) or a declared `requires_if` row (br25), and
  dKeptSession's hooks spawn `node <policy kit>/policy-mirror.js get <key>` (ks8:62-66). A spec whose
  code imports or calls another kit's module in process, loads one by file (`importlib`,
  `spec_from_file_location`, `load_kit_module`), or puts another kit's directory on `sys.path`, is a
  MISMATCH unless a declared `requires_if` row admits it. Which kit a spec's code lives in is read
  from its Files touched.
- **R4, the loop program's rows.** dl12 S1 to S3: an item belongs to its own step's table; every input
  names a layer tag of `tools/playbook/layers.toml`; `returns` names a `record-kind.*` tag; `routes`
  holds exactly the outcomes as keys. br3 S1 now renders an item through `loop_lib.py declaration
  --item <tag> --json` in a subprocess, refusing with exit 1 and writing nothing when the loop does not
  declare the tag or no loop kit is found (br3:39-47); the verb is br3 F5's open ask to dDeclaredLoop.
- **R5, the disposition door.** dl16 claims no `build_records.py new disposition` verb.
- **R6, the overlay composition's reads.** Every read the composition makes passes `--rev HEAD`
  (oc46 S6, oc35 S5).
- **R7, dDeclaredLoop's guard.** dl2's `tools/loop/guard.py --staged` is the pre-commit verdict and
  reads no trailer; the `Gov-Policy:` trailer is checked by `--push-range`; dl2 refuses an agent
  commit to `guarded-paths.txt` under every value (br6 and br23 now apply it so).
- **R8, the witness channels and the budget edges.** dl3 S2 names the channel set a witness may use;
  dl33 S3 says contention never draws on the budget. dPlacedRequest's `--claims` prints fields 1 to 5
  only, and `read_claims` fetches `refs/gov/leases/*` from the remote in one bounded fetch
  (pr1:76-80, :206-208).
- **R9, a catalogue-default read.** br21 rev-3 gives `read_policy_setting(key, root)`, the roles kit's
  one runner of `policy.py get`, a `with_default` argument, and it is the form a read with a catalogue
  default takes (br21:41-50). br43 S21 makes every roles-kit caller use it, and says no file under
  `tools/roles/` runs `get` outside it or imports the policy kit (br43:105-110; AC21's predicate at
  br43:427-429). Without `with_default`, None means the key sits at its catalogue default or no policy
  kit was found; with it, None means only no policy kit. A roles-kit spec that reads None as the
  default and types the default's value, or reads a key outside `read_policy_setting`, is a MISMATCH.
  Outside the roles kit, R3's `policy.py get` subprocess is the rule.

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not a re-ground touched
  it.
- **MISMATCH:** today's parent text says something else: a renamed surface, a moved reader, a fork
  resolved another way, a refusal the parent now states, or a rule above that the spec breaks. Quote
  both sides with `file:line`, and state in one or two sentences the change the dWellOiledMachine spec
  needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other. A citation group checks every assumption about a revised unit and
applies R1 to R9 to its own specs. A rule-wide group checks only R1 to R9, on the hits named above:

- **Group A1, citation, led by spec 3:** specs 3, 4, 7, 8, 9, 11, 16, 19, 27, 30 and 32.
- **Group A2, citation, led by spec 34:** specs 34, 39, 42, 43, 44, 45, 48, 51, 53, 54, 56 and 58.
- **Group B1, rule-wide, led by spec 1:** specs 1, 2, 5, 6, 10, 12, 13, 14, 15, 17, 20, 21, 22, 23,
  24, 25, 26, 28, 29, 31, 33 and 36.
- **Group B2, rule-wide, led by spec 38:** specs 38, 40, 41, 46, 47, 49, 55, 57, 59, 61, 64, 74, 79,
  81, 90, 92, 93, 94, 96, 97, 108 and 126.

The spec files are `memory/builds/dWellOiledMachine/spec/2026-10-2?-spec-TOOL-dWellOiledMachine-<n>.md`.
The parents' are `memory/builds/dBoundRoles/spec/2026-10-2?-spec-TOOL-dBoundRoles-<n>.md`,
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-<n>.md`, and for the rules
`memory/builds/dKeptSession/spec/2026-10-2?-spec-KICK-dKeptSession-<n>.md`,
`memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`,
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`,
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md` and
`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`. Read every mention of
a parent unit in each of your specs, then the cited parent text, its §9 rev lines first.
`git show <re-ground commit> -- <spec>` shows what each re-ground moved; `git show ab864dfc8:<spec>`
reads a parent as dWellOiledMachine's spec run read it. The sibling build dFurnishedOrders was
cross-checked against the same two re-grounds; its record,
`memory/builds/dFurnishedOrders/build/2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck.md`,
shows the classes that turned up.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `wmN:L` for line L of dWellOiledMachine spec N, `brN:L` for dBoundRoles spec N, `trN:L` for
   dTotalRecall spec N, and `ksN:L`, `ocN:L`, `dlN:L`, `wbN:L`, `prN:L` for the others. `Rule` is
   `cite` for a citation assumption, else the R-number.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dWellOiledMachine
   spec needs, then `Cause:` either the re-ground (the parent text moved in the re-ground commit) or
   pre-existing (it already read so at `ab864dfc8`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit the rule does not bind, one line saying why.
5. One line per citation spec: the revised parent units it cites that none of its assumptions depend
   on.

### brief:non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent restates one of their surfaces
  that the dWellOiledMachine spec relies on through it.
- No defect in dWellOiledMachine's own design that no parent causes.
- No verdict about spec 127, written after both merges.

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
