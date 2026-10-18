**Serves:** journal TOOL-aScoutedSeam-3

# gov-spec-writer handoff — TOOL-aScoutedSeam-3

<!-- gov:handoff role=gov-spec-writer build=aScoutedSeam unit=TOOL-aScoutedSeam-3 path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-TOOL-aScoutedSeam-3-1-spec-writer.md role-sha=06b14b1ac42a task-sha=f1c01879759e -->

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

This handoff is for build `aScoutedSeam`, unit `TOOL-aScoutedSeam-3`.
Not supplied, optional: `task:reuse`, `card:route`.

### brief:goal

Revise TOOL-aScoutedSeam-3 so diff mode ships the measured design: the enumerated-coverage prompt
with a deterministic unit lister, at the `gov-reuse-scout` type's own level, `medium`. Close fork F2
on the measurements. This pass touches the spec only: no product code, and no commit.

### brief:items

1. **§8 F2: close it.** Record `RESOLVED (owner, 2026-10-18): medium, with the enumerated-coverage
   prompt`. Cite three records: the T1 trial `2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2-trial.md`,
   the method `2026-10-18-build-TOOL-aScoutedSeam-1-11-prompt-method.md`, and the judge and `low` record
   `2026-10-18-build-TOOL-aScoutedSeam-1-12-judge-and-low.md`. The figures, judged on the 23 diff cases:
   - the enumerated prompt at `medium` covers 14 primaries, with 11 misleading seams of 130;
   - the open prompt at `extra` covers 11, and at `medium` 7;
   - the enumerated prompt at `low` covers 8, with 19 misleading of 105.

   `high` with the open prompt was never run. It is no longer needed, because the composition carried
   the gain.
2. **S6 and S7: drop the `high` override.** Remove the `[effort.stages.reuse] diffCheck = "high"`
   table. `diffCheck` runs at the agent type's level, `medium` in gov, exactly as the existing S6 text
   says an `efforts` that omits it does. S7 keeps the `workflows.toml` `diffCheck` stage and the
   catalogue re-render, and loses the policy edit. That removes the reason the edits had to share one
   commit for R12. Restate S7's single-commit rule only if something still binds it; verify that
   against `check_roles.py`. Change §4's files list to match.
3. **S2: rewrite the prompt per the method record's recipe.**
   - The DIFF-lens instruction becomes a COVERAGE job over a supplied unit list.
   - For each listed unit, the agent returns one row: the unit, the nearest existing `path::symbol`
     (or `none` with what it searched), a verdict from `duplicate`, `should-extend`, `new` or
     `not-a-unit`, and a one-line why.
   - The agent then adds rows, marked `added`, for repeated literals, hardcoded design values, renamed
     copied bodies and rebuilt JSON nodes.
   - The prompt names the failure it guards against: "do not stop at the first duplicate; a listed
     unit without a row is incomplete".
   - A duplicate becomes a MUST seam and a should-extend a SHOULD seam. The wiring half for `## reuse`
     MUST lines stays.
   - The worked examples are the T1 handoffs, `prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-13` to
     `-35-reuse-scout.md`.
4. **New scope item: the deterministic unit lister.** It is a codebase-map kit CLI that reads
   `git diff <base>..<head>` and prints the units the diff adds in product files, with their kind and
   path. The measured rules are in `2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2.py`'s `extract_units`:
   - **Population:** it skips memory, docs, help, tests and lockfiles, and lists definitions,
     constants, shell functions, schema fields and JSON tree keys.
   - **CSS:** CSS patterns run only in style files.
   - **Hunks:** a hunk that adds 4 or more lines and names no unit becomes a `hunk` unit.
   - **Cap:** the list stops at 60 units, followed by a count of the rest.
   - **Empty list:** when the lister finds nothing, the prompt tells the agent to enumerate the units
     itself.

   The caller runs the lister and passes its output to `reuse-scout.js` as a new `units` arg, because a
   Workflow script cannot run git. Add `units` to S1's refusals and to the §4 data model. Place the
   lister by the kit's seams, and run the reuse probes M5 names before naming a file. Give it its own
   criterion, which goes red when a hunk adding logic inside an existing function gets no unit, or when
   a CSS pattern fires outside a style file.
5. **S3: caps.** Keep "at most 10 duplicates, MUST first", and adopt the orient mode's cap of five MUSTs
   with demotion from TOOL-aScoutedSeam-1. The judge's 11 misleading seams at `medium` are what the cap
   is for. Cite the record.
6. **AC3:** it runs at the type level, `medium`, on the same three gov cases. All three were solved at
   `medium` in T1. The cost line becomes three agents at `medium`, measured at 19 s to 4 min 57 s per
   diff. **AC5:** `harness-args reuse-scout` prints `diffCheck`, and no policy override is required.
   Verify what `stage-efforts reuse` prints for a stage with no override before you write the
   criterion.
7. **§4 alternatives rejected:** add the open prompt at `extra`, the enumerated prompt at `low` and the
   un-run `high`, each with the figures from item 1. **§5:** replace the perf line with the T1 cost and
   the judge's precision figure.
8. **§9:** add one revision line naming every section, scope item and criterion moved.

### brief:acceptance

TOOL-aScoutedSeam-3 carries the new §9 line, and §8 F2 reads RESOLVED with the figures. S2, S3, S6, S7
and the new lister item read as above, the lister has a criterion, and AC3 and AC5 are rewritten.
`python tools/check-spec-tokens.py`, `python tools/memory-tree/gen_build_index.py --check` and
`--check-format` pass after the main loop re-renders the indexes. The spec stays under the 49152-byte
ceiling.

### brief:gates

memory hygiene · spec tokens (a spec's own names resolve) · build README slot contract

### brief:non-goals

- No product code, and nothing under `tools/`, `skills/` or `.claude/`.
- No other unit's spec is edited. TOOL-aScoutedSeam-1's orient prompt adopting the method is a separate,
  untested question.
- No change to unit ids, order or titles, and no commit; the commit is the main loop's.

### input:spec

memory/builds/aScoutedSeam/spec/2026-10-11-spec-TOOL-aScoutedSeam-3.md

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
