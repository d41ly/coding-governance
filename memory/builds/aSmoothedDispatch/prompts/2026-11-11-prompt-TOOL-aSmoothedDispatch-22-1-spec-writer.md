**Serves:** journal TOOL-aSmoothedDispatch-22

# gov-spec-writer handoff — TOOL-aSmoothedDispatch-22

<!-- gov:handoff role=gov-spec-writer build=aSmoothedDispatch unit=TOOL-aSmoothedDispatch-22 path=memory/builds/aSmoothedDispatch/prompts/2026-11-11-prompt-TOOL-aSmoothedDispatch-22-1-spec-writer.md role-sha=d312d5ece1d4 task-sha=b0840a3d0a21 -->

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
after every writer returns. At a spec audit's disposal, a correction to an unbuilt sibling's spec
rewrites that sibling's text, with a rev bump and a revision-log line naming the repair unit and
the review record by its file stem, and a CLOSED sibling stays frozen.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## House rules

Before you return, check each spec you wrote or revised with the spec-token checker's one-spec mode,
where this repository holds `<prefix>/check-spec-tokens.py`, `<prefix>` being its tool root:
`python <prefix>/check-spec-tokens.py --spec <the spec's path>`. That run grades your one spec and is
not a gate leg. The checker run with no `--spec` is the gate leg, and it stays refused to you.
Exit 1 with hits prints one `spec-tokens: <spec path> [<kind>]` row per miss, naming its token,
then a `spec-tokens: <N> unwaived hit(s)` summary. Fix each miss your spec's own text can fix, then
run the check again. A hit your spec's text cannot fix goes in your return, with its row.
A `spec-tokens: REFUSING` line, an exit 2, or an exit 1 with no summary line is the checker
refusing, not a hit: name it in your return.

## Task

This handoff is for build `aSmoothedDispatch`, unit `TOOL-aSmoothedDispatch-22`.

### brief:goal

Revise `memory/builds/aSmoothedDispatch/spec/2026-11-11-spec-TOOL-aSmoothedDispatch-22.md` to rev-2, keeping it INPROGRESS. The builder's pass diverged on one fact. Main at `bdb633d94` carries TOOL-dPavedRoad-1 (commit `1b991ef0c`), which adds `spec tokens (a spec's own names resolve)` to gov-spec-writer's allowlist. It does this in `tools/roles/house/policy.toml:36` and in the `"gov-spec-writer"` entry of `.claude/roles.json`, at lines 177-181 at `bdb633d94`. The scratch-guard role-gate arm passes any G1 leg on the role's allowlist (`if (leg && allow.includes(leg.name)) continue`). So at the merge the hook admits the bare `python tools/check-spec-tokens.py` to gov-spec-writer, and §4's probe control printed `exit=0`, not `exit=2`. At `ba6c2f1f9` it printed `exit=2` only because that tip lacked main's grant. Every other criterion the builder reached held at the trial merge: S2/AC2, S3/AC3, with the floor of 235 recounted (165 `arm "` lines at the base, 179 on the branch, 172 on main, 176 merged), and S4/AC4. The builder did not reach S6 or S7.

### brief:items

1. §4 "S5 — the hook probe" and AC5: the probe's control must be a command the merged hook still refuses to gov-spec-writer. Pick it by reading `tools/hooks/scratch-guard.js` and `.claude/roles.json` at `bdb633d94` with `git show bdb633d94:<path>`. Candidates are the checker's suite, `bash tools/check-spec-tokens.test.sh` (the G3 suite shape), or a G1 leg not on the writer's allowlist. State the exit and the stderr line the control prints, and cite the rule by path and line. The two-operand `--spec` form stays as the admitted case.
2. §5 "security": rewrite the line. It says main grants the writer the bare spec-token leg (TOOL-dPavedRoad-1), that this unit leaves that grant as merged, and what the hook still refuses, the control from item 1.
3. §2 S5, and any other sentence claiming the hook refuses the bare leg to the writer: correct it. Keep §3's non-goal that rules out touching the grant, and name `tools/roles/house/policy.toml` and `.claude/roles.json` as carried as merged.
4. §2: note that the trial merge is re-taken at `e1f9cebb3`. The builder saw tree `6002767` there, with the same three files and region counts 8, 2 and 1. AC7's fixture says the builder re-takes the tree with its stated command rather than pinning `de33b5c7` alone.
5. Bump the status line to rev-2 and add one revision-log line naming this brief.

### brief:acceptance

The rev-2 spec's AC5 names a control the merged hook refuses, with that control's exit and stderr line cited to `tools/hooks/scratch-guard.js` at `bdb633d94`. No sentence in the spec says the hook refuses the bare spec-token leg to gov-spec-writer. `python tools/check-spec-tokens.py --spec` over the spec prints no hit the spec's own text can fix.

### brief:gates

The spec-token checker's `--spec` mode over the revised spec, the memory hygiene gate and the naming lexicon (writer); the rest are the unit's, unchanged.

### brief:non-goals

Any change to S2, S3, S4, S6 or S7, or to AC1-AC4, AC6 or the `New arm:` lines, beyond a sentence that states the corrected hook fact. Any change to the writer's grant. Committing, which is the main loop's.

### input:spec

memory/builds/aSmoothedDispatch/spec/2026-11-11-spec-TOOL-aSmoothedDispatch-22.md

### task:reuse

the --writes) arm and DP_WRITES, verb_list, the SPEC_TOKENS_CLI call in verb_dispatch, scratch-guard's role-gate allowlist and route reader.

### card:route

- build: aSmoothedDispatch
- unit: TOOL-aSmoothedDispatch-22 · spec memory/builds/aSmoothedDispatch/spec/2026-11-11-spec-TOOL-aSmoothedDispatch-22.md
- brief: memory/builds/aSmoothedDispatch/prompts/2026-11-11-prompt-TOOL-aSmoothedDispatch-22-reconcile.md

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
