**Serves:** journal TOOL-dTotalRecall-1

# gov-spec-reviewer handoff — TOOL-dTotalRecall-1

<!-- gov:handoff role=gov-spec-reviewer build=dTotalRecall unit=TOOL-dTotalRecall-1 path=memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-5-spec-reviewer.md role-sha=a81df30406a1 task-sha=127f3d40a739 -->

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

This handoff is for build `dTotalRecall`, unit `TOOL-dTotalRecall-1`.

### input:spec

memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md

### brief:goal

Classify every assumption the named dTotalRecall specs make about a parent unit as AGREES, MISMATCH or UNKNOWN
UNTIL BUILT, against the parents' specs as they stand on origin/main at `c8d46e188`. dTotalRecall's spec run
began at `fb872a37e`, which holds none of its parents' re-grounds:

- **dDeclaredLoop**, re-grounded at `783f1ad3a` and landed as `e5de11e9e`. It revised units
  1, 2, 3, 4, 5, 6, 12, 16, 17, 18, 22, 24, 25, 26, 27, 28, 33, 34, 46 and 56. Its record, `memory/builds/dDeclaredLoop/build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`, and each revised spec's new §9 line say what moved.
- **dWitnessedBar**, re-grounded at `443775a2f` and landed as `191ba7ab5`. It revised units
  1, 3, 6, 8, 11, 12, 14, 15, 16, 18, 23, 25, 28, 51 and 56. Its record, `memory/builds/dWitnessedBar/build/2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck.md`, and each revised spec's new §9 line say what moved.
- **dPlacedRequest**, re-grounded at `2740f0a3d` and landed as `60d90cb71`. It revised units
  1, 2, 3, 4, 5, 6, 7, 9, 21 and 34. Its record, `memory/builds/dPlacedRequest/build/2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md`, and each revised spec's new §9 line say what moved.

The first population is by citation: every spec that cites a revised unit, as `<FAMILY>-<build>-<n>`
or a bare `<build>-<n>` (13 specs). By the revised units each cites (`dl` dDeclaredLoop, `wb`
dWitnessedBar, `pr` dPlacedRequest): 1 (wb15, pr1, pr7) · 2 (pr1) · 3 (pr1) · 4 (wb15, pr2) · 6 (pr1, pr2) · 11 (wb1) · 18 (dl12) · 19 (pr1) · 59 (wb51) · 62 (wb51) · 68 (wb16) · 76 (wb51) · 88 (wb14).

The second population is by rule (30 specs). A parent re-ground applied a rule that binds specs
that never cite the unit stating it. A text probe over the other specs named these candidates, by
the rule each hit: 7, 8, 23, 26, 36, 47, 53, 69, 75, 77 and 79 (a leg with no `enforces`), 9, 14, 15, 16, 22, 43, 48 and 50 (a leg with no `enforces` and a record kind), 5, 20, 25, 40, 42, 51, 93 and 94 (a record kind), and 81, 87 and 92 (an in-process sibling import). The probe is a heuristic. Verify every hit: a hit the rule does not
bind is a line in your return, not a row.

The rules, each as the parents now apply it. The parent specs win where this summary differs:

- **R1, a new leg's `enforces`.** PLAY-dOrderedCharter-7 S3 reds a `tools/gate-legs.json` row with no
  `enforces`, and the pending list `core-pending.txt` only shrinks after dOrderedCharter's pass
  (oc7:58-63, :228), so a later build cannot excuse its leg there. Under `core.bypass = never` the
  meta-check also reds a leg whose `enforces` is non-empty and that carries a `guard` (oc7:109-111).
  The parents' re-grounds gave their legs `enforces` (dl25, dl26, dl28, wb11, pr4, pr7, pr21). dl56 F5
  is still open on who writes it for other units, recommending each unit's own pass. A spec that adds
  or reshapes a leg row and names no `enforces` for it is a MISMATCH.
- **R2, a typed record kind.** PLAY-dOrderedCharter-42 S2 and S3 make `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the record factory's kind list, and read a `-<kind>-<n>.md` file
  whose Serves kind differs as malformed; S5 keeps the closed list in the HYGIENE template. The
  parents now serve their records as their own kinds: dl3, dl16, dl17 and dl22 (`transition`,
  `acceptance` and the rest), wb1, wb8, wb14, wb25 and wb51 (`gate-health`, `flake`, `widen`,
  `leg-tail`), pr2 (`card`) and pr7 (`probe`, `probe-trigger`). A spec that adds a kind without
  joining it to all three, serves a typed record as `journal`, or reads a parent's record under a kind
  the parent no longer serves, is a MISMATCH.
- **R3, a sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4, restated by
  oc7:202-203, dl12 S4, wb3 and wb28 at their re-grounds). Code in one kit reaches another kit's verb
  by subprocess, through an inline `resolve_kit_dir`; where the verb does not exist, the parents write
  a §8 fork for an ask. A spec whose code imports or calls another kit's module in process is a
  MISMATCH, unless a declared `requires_if` row admits it.
- **R4, the loop program's rows.** dl12 S1 to S3: an item belongs to its own step's table, and adopt,
  entry, lifecycle and probe items are never steps of the five (dl12:80-81); every input names a layer
  tag of `tools/playbook/layers.toml` (dl12:43); `returns` names a `record-kind.*` tag (dl12:113);
  `routes` holds exactly the outcomes as keys (dl12:147-148).
- **R5, the disposition door.** dl16 at rev-3 claims no `build_records.py new disposition` verb; a
  writer names the factory's flags and the build run re-grounds the call (pr3, pr5, pr21).
- **R6, the overlay composition's reads.** Every read the composition makes passes `--rev HEAD`
  (oc46 S6, oc35 S5), an unborn `HEAD` reading the default; a stale patch follows
  `instructions.stale`'s mode and files an order (oc35 S7, S8).
- **R7, dDeclaredLoop's guard.** dl2's `guard.py --staged` runs at pre-commit, when no commit message
  exists, so it reads no trailer; the `Gov-Policy:` trailer is checked by `--push-range`; the owner
  proof tests stderr (dl2 S5).
- **R8, the witness channels and the budget edges.** dl3 S2 names the channel set a witness may use
  (pr1's trailer-only witness was a mismatch); dl33 S3 says contention never draws on the budget.

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not a re-ground touched
  it.
- **MISMATCH:** today's parent text says something else: a renamed surface, a moved reader, a fork
  resolved another way, a refusal the parent now states, or a rule above that the spec breaks. Quote
  both sides with `file:line`, and state in one or two sentences the change the dTotalRecall spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other. A citation group checks every assumption about a revised unit and
applies R1 to R8 to its own specs. A rule-wide group checks only R1 to R8, on the hits named above:

- **Group A, citation, led by spec 1:** specs 1, 2, 3, 4, 6, 11, 18, 19, 59, 62, 68, 76 and 88.
- **Group B, rule-wide, led by spec 7:** specs 7, 8, 9, 14, 15, 16, 22, 23, 26, 36, 43, 47, 48, 50, 53, 69, 75, 77 and 79.
- **Group C, rule-wide, led by spec 5:** specs 5, 20, 25, 40, 42, 51, 81, 87, 92, 93 and 94.

The spec files are `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-<n>.md`. The parents' are
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`,
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md`,
`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`,
and `memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`. Read every
mention of a parent unit in each of your specs, then the cited parent text, its §9 rev lines first.
`git show <re-ground commit> -- <spec>` shows what each re-ground moved.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `trN:L` for line L of dTotalRecall spec N, `dlN:L` for dDeclaredLoop spec N, `wbN:L` for dWitnessedBar spec N, `prN:L` for dPlacedRequest spec N, and `ocN:L` for dOrderedCharter spec N. `Rule`
   is `cite` for a citation assumption, else the R-number.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dTotalRecall spec needs, then
   `Cause:` either the re-ground (the parent text moved in the re-ground commit) or pre-existing (it
   already read so at `fb872a37e`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit the rule does not bind, one line saying why.
5. One line per citation spec: the revised parent units it cites that none of its assumptions depend
   on.

### brief:non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent restates one of their surfaces
  that the dTotalRecall spec relies on through it.
- No defect in dTotalRecall's own design that no parent causes.
- No verdict about a sibling build (dKeptSession, dBoundRoles): none reads another's specs.

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
