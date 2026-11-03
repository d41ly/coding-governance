**Serves:** journal PLAY-dOrderedCharter-47

# gov-spec-writer handoff — PLAY-dOrderedCharter-47

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-47 path=memory/builds/dOrderedCharter/prompts/2026-11-03-prompt-PLAY-dOrderedCharter-47-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=4ea99ee39194 -->

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

## Task

This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-47`.

### brief:goal

Revise specs 47, 48, 25 and 7 so each matches the tree at HEAD on every finding below.

### brief:items

1. Fold every finding below into its spec. Re-verify each cited path and line at HEAD before writing it: units may
   have landed since the sweep read the tree.
2. A finding marked NEW MECHANISM is a fork: decide it by M3, and record the loser and the observation that rejected
   it (M12) in §8, delegated.
3. **A new leg's own rows.** Every new leg's rows are written in its own pass, the way unit 26 rev-7 writes
   `tags positional selftest`'s. Those rows are the dossier claim in `memory/map/features/playbook.md` (with
   `memory/map/generated/*`, which the map generator rewrites), the `tools/govkit/subject-pins.tsv` row, and the claiming row.
   - For a leg an adopter cannot carry, the claiming row is an `[[exempt_leg]]` row in `tools/govkit/registry.toml`,
     as units 16, 19 and 28 wrote at `:707`, `:711` and `:715`.
   - Otherwise it is a `[[gate_leg]]` row in the kit's `kit.toml`.
   - Files touched lists those paths, and §7 names the legs they trip. Check them with
     `python tools/check-spec-tokens.py --legs-for <path>`.
4. **`enforces` into `principle.*`.** The main loop decided this across the sweep. Unit 7, at order 11, adds `principle` to the
   `enforces` row's `to` in `tools/playbook/edges.toml` in its own pass. Units 13 and 12 consume that through a §3 Edges line.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-11-03, with the status kept `DEFERRED`.
- Add one §9 line naming this brief.
- §7's leg line names every leg whose guard a Files-touched path trips.
- No AC observes a suite, a bar or a gate leg.
- Stay under the 47000-byte authored budget.
- An H1 names another build's unit as "<build>'s unit N", never by its id.

For the run:

- Writes stay in specs 47, 48, 25 and 7 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question. A fork that no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check. The main loop re-renders the packet, renders the index and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return each spec's new rev, each §8 decision with its loser, and any finding you did not fold, with the reason.

**The findings.**

Cross-cutting: specs 25 and 7 add legs but omit the rows unit 50 says a new leg owes in its own pass (dossier claim in memory/map/features/playbook.md + memory/map/generated/, tools/govkit/subject-pins.tsv, tools/playbook/kit.toml [[gate_leg]], ceiling-evidence.txt) and the legs those paths trip (recall floor, recall floor arms, govkit selftest, govkit refusal join). Specs 47 and 48 aim their positional plants at the playbook-render selftest; unit 26 rev-7 runs them in its `tags positional selftest` leg.

**Spec 47.**
- 47-1 §7 New arm names tools/playbook/adopt-playbook.sh + playbook-render selftest for `positional-forked-before`; that file is not in Files touched; gov_tag plants run via `run_plant_rows tags` (adopt-playbook.sh:258) and PLANTS tuple (gov_tag.py:317). Unit 26 rev-7 §3 Edges places 47/48/53 positional plants in `tags positional selftest`. Re-point the arm there (or add the file).
- 47-2 §5 user docs edits tools/playbook/README.md, not in Files touched (its legs already on §7). Add it.
- 47-3 §5 risk says a re-added record is graded from its new add; tree_lib.py:303/:324 keeps the OLDEST add, so it is graded from the original add. Restate.

**Spec 48.**
- 48-1 Same as 47-1 for `positional-producer-new`/`-stale`; also tools/playbook/README.md missing from Files touched.
- 48-2 §4 cites tools/hooks/README.md:119; the file:line text now sits at :130.
- 48-3 §4 Evidence candidate lines moved: tools/workflows/README.md:489→:498, :522→:531; tools/workflows/REVIEW-PROTOCOL.template.md:193→:155; tools/workflows/check-review-join.test.sh:159→:279. Re-point or mark as base lines (41-hit count still holds at HEAD).

**Spec 25.**
- 25-1 S1/§4/§10: bundle reads "every inbound edge `gov tag refs` returns, grouped by edge type"; `refs` (gov_tag.py:98-106) returns only span citations {path,line}, no edge type. Typed edges come from edge_grammar.read_tree_edges (edge_grammar.py:560), derive_inverse_edges (:672), resolve_edge (:493). Re-point the read; refs supplies only the `cites` view.
- 25-2 S5/S6/§4/Files touched: unit 28 already ships both checks — check_edges (edge_grammar.py:396, unregistered type) and run_resolve (:537, unresolved target), under the `edges (...)` leg in the tags pack, plants from :731. Drop tools/playbook/edge_checks.py; the two `--only` arms call check_edges and run_resolve; mirror into unit 55's hands-off.
- 25-3 S5 "cites, derived, is never declared and never graded": a declared cites is red (edge_grammar.py:411-413, plant `declared-cites` :733). Restate as unit 24's rule.
- 25-4 AC1/AC7: edges.toml:54-58 registers `instructs` to=["selects"]; check_edges (:430) reds a target outside a selects namespace; doc is a describes namespace. Plants must address a selects-namespace tag.
- 25-5 AC1/AC6/AC7 name doc.fixture; unit 19's fixture defines doc.alpha (gov_tag.py:448,668; memory/guides/ALPHA.md :444). Use doc.alpha or state the guide the bundle cases add.
- 25-6 New leg `tags bundle selftest`: owed rows and legs per the cross-cutting note (unit 50 §4 at spec-50:131-136; playbook.md:11 shows units 19/28 claimed theirs in their own passes).
- 25-7 §4 Rollout "after units 19, 24 and 28" — §3 consumes tools/run-gates/owed_rows.py from unit 50 (absent at HEAD); add unit 50 to the ordering.

**Spec 7.**
- 7-1 S3/§3/§10: compute_coverage is not "inline under a PARITY_ROWS row" nor at map_lib.py:1404; canonical tools/lib/coverage_join.py:46, copy tools/memory-tree/coverage_join.py:49, parity row is a module copy (tools/lib/resolve-python.test.sh:370, :402-405); tag_index.py:984 does `from coverage_join import compute_coverage`. core.py imports it the same way.
- 7-2 S2 writes principle.p28/p16 into a leg's `enforces`; edges.toml:63-70 registers enforces to=["unit","practice"]. Widen `to` with principle in this pass (add edges.toml to Files touched).
- 7-3 Five new legs (core meta-check, core kinds, core skills conformance, core practices conformance, core selftest): owed rows and legs per the cross-cutting note.
- 7-4 §10 deviation_join.py lines: FIELD :145→:150, RECORD_NAME :160→:165, read_record :212→:217, read_records :268→:273.
- 7-5 §1 "142 rows of tools/gate-legs.json": 151 today; pin the count or re-derive.

### brief:acceptance

- Each finding above is either folded, or listed in the return with the reason it was not.
- Each revised spec's Status line is one rev higher, and its §9 holds the new line.

### brief:gates

The spec-token check, run over the tree by the next `--dispatch`.

### brief:non-goals

- No code.
- No spec outside the four above.
- No finding about another spec.

### input:spec

memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-47.md

### task:reuse

each spec's §10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-26 · spec memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-26-build-brief.md

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
