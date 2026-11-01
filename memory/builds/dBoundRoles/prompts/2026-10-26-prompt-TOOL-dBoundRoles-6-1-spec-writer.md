**Serves:** journal TOOL-dBoundRoles-6

# gov-spec-writer handoff — TOOL-dBoundRoles-6

<!-- gov:handoff role=gov-spec-writer build=dBoundRoles unit=TOOL-dBoundRoles-6 path=memory/builds/dBoundRoles/prompts/2026-10-26-prompt-TOOL-dBoundRoles-6-1-spec-writer.md role-sha=06b14b1ac42a task-sha=ca73a87a5555 -->

## Role

You are a code architect, writing the specification for one or more units of a larger build. You are
not writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design.

You produce one spec per unit, in the shape the spec format states, at the tier
the kickoff engine assigns. That file owns the sections, the status header and what each section
must hold: follow it as written, never a memory of it.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite it by path and line. A claim
  you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the memory hygiene gate and the naming lexicon over your specs, and no other gate.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3). Never decide one
  silently.

You are not building. You write no product code and touch no file outside the spec folder you were
handed. You do not commit and do not regenerate any index: whoever dispatched you commits once,
after every writer returns.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## Task

This handoff is for build `dBoundRoles`, unit `TOOL-dBoundRoles-6`.
Not supplied, optional: `card:route`.

### brief:goal

Revise the 15 dBoundRoles specs that the cross-check record names under "For the re-ground". Each one
should state its parents' surfaces the way their specs now spell them on origin/main at `c8d46e188`:
dDeclaredLoop as its re-ground `783f1ad3a` left it, dWitnessedBar as `443775a2f` left it, and
dPlacedRequest as `2740f0a3d` left it. Each spec keeps its own design, and only its assumptions about
the parents change.

### brief:items

Read the cross-check record first,
`memory/builds/dBoundRoles/build/2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck.md`. Its
summary table numbers every assumption (rows 1 to 53), and "The mismatches, both sides quoted" gives
both sides of each MISMATCH. Read each parent spec the record cites, at the lines it cites. This brief
summarises them, and where the two differ, the specs win. Before you edit for a row, re-read both
sides. A row the parent's text does not bear out is not edited: return it as refused, with the line
that refutes it.

Facts every revision uses:

- **A sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205; dl12 S4 and
  dl18 at rev-3; wb28:63-64). Code in one kit reaches another kit's verb by subprocess, found through
  an inline `resolve_kit_dir` block. A policy key is read by running `policy.py get <key>` as a
  subprocess, "the one seam a sibling kit may reach" (oc7:379-380); br15 S6 already reads so. Where
  the verb a spec needs does not exist, write a §8 fork open for the owner. The options are an ask to
  the parent for the verb, or a declared `requires_if` row like `tools/memory-tree/kit.toml:8`, with
  the reason the rule admits it. Recommend one. dDeclaredLoop's specs 12 F5, 18 F5 and 26 F5 and
  dWitnessedBar's spec 3 F6 are the precedent.
- **A leg.** dOrderedCharter unit 7 S3 reds a leg with no `enforces`, and the pending list only
  shrinks after dOrderedCharter's pass (oc7:58-63, :228). dWitnessedBar unit 11 declares each leg once,
  in a kit's `[[gate_leg]]` row or a `tools/govkit/registry.toml` `[[exempt_leg]]` row holding every
  manifest key, `enforces` among them; `leg_factory.py --write` renders `tools/gate-legs.json`, and
  `--check` reds a manifest that differs (wb11:36-49, :73-74). A spec that adds, renames or re-guards a
  leg does it in the declaration, names its `enforces`, and regenerates. Under `core.bypass = never` a
  guarded leg with `enforces` reds (oc7:109-111); wb11 F5 is open on it.
- **dDeclaredLoop's guard.** The pre-commit verdict is `tools/loop/guard.py --staged` (dl2:101). A
  staged change to `tools/policy/guarded-paths.txt` is refused for every agent commit under every value
  of `policy-file.guard` (dl2:58-59). Under `agents-with-reason` an agent's commit changing only
  `.governance/policy.toml` with a change record is admitted (dl2:190-192). dl2 S10's harness arm names
  `policy_edit.py` as the door (dl2:96-98).
- **The composition.** dl26 F5 is open on a `compose` verb a sibling runs by subprocess
  (dl26:280-291). dl27's `activatable` list admits a kind only when its build adds it (dl27:53-56).
- **An ask.** No dBoundRoles spec files a row in another build's `BACKLOG.md`. Where a fix needs a
  parent change, write a §8 fork open for the owner, with its options and a recommendation, and name
  the ask the build run would file.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every
spec of that group, and no other:

- **Group A, items, actors and composition, led by spec 1:** specs 1, 2, 12, 14 and 20.
- **Group B, policy reads and the placement return, led by spec 21:** specs 5, 11, 21, 22 and 43.
- **Group C, the guard and the legs, led by spec 6:** specs 3, 6, 23, 25 and 60.

The spec files are `memory/builds/dBoundRoles/spec/2026-10-2?-spec-TOOL-dBoundRoles-<n>.md`. Write
probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-silly-jang-ffa5af/b141ae93-c1d4-4429-8ac9-f3aa88a427dc/scratchpad/br-w<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; the sections moved; each fork
you added or re-resolved, with its mark; each record row you refused, and why; its byte count; and
any parent spec that looks wrong.

Per spec, by the record's rows:

1. **Spec 1** (rows 3, 8). S7's `check_item_roles` grades every composed item, repository rows
   included (dl24:46-50), or states which rows it skips and how it tells them apart, with a plant of a
   repository item whose actor is an expansion role. `check_layers.py` reaches the role files without
   importing `roles_lib`: a roles-kit verb or a generated file read by subprocess, or the fork.
2. **Spec 2** (row 11). F4's tester template carries a field for the `test.reason` answer and its
   evidence, or a closed outcome covering that act (wb23:29-31, :122).
3. **Spec 12** (row 25). `place` runs a roles-kit verb such as `handoff.py validate-return` by
   subprocess, or the fork for it (or for a `requires_if` row on `tools/loop/kit.toml`).
4. **Spec 14** (row 27). The extractors reach the roles grammar by a roles-kit verb run as a
   subprocess, or the fork for one; re-check br14:233's rejection of importing `roles_lib` with it.
5. **Spec 20** (rows 33, 34, 35).
   - S2's `kind.role` and `kind.workflow` rows name `binds`, `population`, `factory` (dl6's `new role`
     and `new workflow`) and `gate`, and the gate leg's `enforces` holds those binds (oc7:66-75,
     dl27:366-367).
   - S3 composes through the subprocess `compose` verb dl26 F5 recommends, with a fork tracking it.
   - S6's `check_actor_patch` is a roles-kit verb `loop_items.py` runs by subprocess, or the check
     moves into the loop kit reading `.claude/roles.json` as br1 S7 does; name the change to dl24 S4
     as an ask.
6. **Specs 5 and 11** (rows 14, 18). `roles.retries` and the owner-question key are read with
   `policy.py get <key>` by subprocess through the inline `resolve_kit_dir`, as br15 S6 does.
7. **Spec 21** (row 36). F2's chosen option cites an import dl18 no longer makes (dl18:146-147,
   :311-314). Re-resolve it on rung 1, naming dl18: `policy.py get` as a subprocess, one revision
   resolved and passed as `--rev`, or the fork for a batch `get` verb. Mark it
   `RESOLVED (agent, 2026-10-26, delegated)`.
8. **Spec 22** (rows 40, 41, 42). S5 reads `runtime.agents-in-flight` by `policy.py get` as spec 21
   now does. The row kinds are read through a loop-kit verb by subprocess, keeping the `seg`-shape
   fallback, or the fork. F2 states that dl27's `activatable` list does not hold the role and workflow
   kinds, and leaves to the owner whether spec 20 adds them or the work is unowned.
9. **Spec 43** (rows 49, 50, 51). It is at 49098 bytes: replace text, never append, and trim
   elsewhere without changing the design if you must.
   - `placement.py` runs a `handoff.py` verb that prints the agent's last text and meta role, by
     subprocess; S56 names that verb.
   - S21's `read_policy_setting` is the one subprocess caller of `policy.py get`; AC21 reds an import
     of `resolve` and admits only that subprocess.
   - S23's `reviewer_merge.py` reaches the overlay writer through a playbook verb by subprocess, or the
     fork naming the ask of dOrderedCharter (wb28:63-64).
10. **Spec 3** (row 12). S1 names the verb it runs; dl9 has only `loop_lib.py --check` and `--fixture`
    (dl9:156, :167-175). F4 becomes the fork for an ask to dDeclaredLoop for a one-item declaration
    verb, or S1 states another admitted read.
11. **Spec 6** (row 15). S2 names `tools/loop/guard.py --staged` as the pre-commit verdict, routes
    the `guarded-paths.txt` edit through the owner's terminal or a fork, states the admitted shape
    under each `policy-file.guard` value, and forks with dl2 S10 on which arm answers a write to
    `.claude/agents/<file>`.
12. **Spec 23** (row 43). S6, §4 "The floor" and AC5 cite dl2's verdict, limit the claim to
    `policy-file.guard = owner-only` or read provenance from dl2's change record, and AC5 plants each
    non-default value.
13. **Spec 25** (rows 44, 45). The renamed leg is declared once through the leg factory with a named
    `enforces`, the manifest regenerated; the guard's standing under oc7 S10 is stated while wb11 F5
    is open. The two exports `spawn-guard.js` shares with `scratch-guard.js` become a `tools/lib/`
    canonical block inlined into each kit under a parity row, or a `requires_if` row, not a cross-kit
    `require`. It is at 46025 bytes.
14. **Spec 60** (row 53). S20, F5 and AC12 widen the guard in the leg's declaration and regenerate
    with `leg_factory.py --write`, keeping or naming the leg's `enforces`.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-26, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record, with its row numbers.
- Replace each now-false sentence where it stands.
- A resolved fork whose chosen option a parent now rules out is re-resolved on rung 1, naming the
  parent, and marked `RESOLVED (agent, 2026-10-26, delegated)`. A fork this brief tells you to leave
  open for the owner stays open, with its recommendation. Re-open no other fork.
- Spell a `tools/` path inside an acceptance criterion as the spec already does.
- Stay under the class cap of 49152 bytes.

### brief:acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>`, and §9 holds the new line.
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `brN:L`
  prints nothing, or prints only the corrected sentence.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### brief:gates

Only the memory hygiene gate and the naming lexicon, as the role allows. The main loop runs the rest
and renders the index.

### brief:non-goals

- No file outside the spec files of your group. No commit, no stage into the real index, no
  deviation record: the main loop writes those.
- No file of dOrderedCharter, dDeclaredLoop, dWitnessedBar, dPlacedRequest, dSafePassage or
  dGroundRules. A parent spec that looks wrong is a line in your return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### input:spec

memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-6.md

### task:reuse

the last wave's procedure: memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md and 2026-10-26-...-parents-reground.md, its record build/2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck.md, its deviation records; tools/roles/handoff.py render for every handoff.

### Charter rules

- [yagni] YAGNI: build what this unit needs now, never scaffolding for later, and delete rather than disable.
- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [core] One shared core with thin adapters, so logic and authorization live once; data changes additively, with defaults and an upgrade step.
- [contract] A contract two parties share lands first, as one source with generated copies and a parity gate against a live re-derivation; deployables sharing one artifact release together.
- [derive] Derive over author: status, counts, inventories and indexes are generated or declared and checked both ways, never typed beside what they describe.
- [one-fact] One fact in one place: a document points at the source that owns a value, or a gate compares the two.
- [spec] Spec before code: every product-code unit commits its spec first, a micro-spec for a mechanical change and a full design pass for a substantive one.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [gate] A gate never seen red is not a gate: observe its failing case, state what it does not check, and never read a skip, an unmovable probe, an exemption or an empty population as coverage.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [small] Work in small units, one stream each, merged to local main often; risky behaviour lands dark behind a default-off switch.
- [docs] A user-facing change is not done until its page under `help/` is current.
- [security] Security first: validate once at the write boundary, deny by default, give automation the narrowest grant, and keep secrets out of files, memory and chat.

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
