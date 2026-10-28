**Serves:** journal TOOL-dFurnishedOrders-46

# gov-spec-writer handoff — TOOL-dFurnishedOrders-46

<!-- gov:handoff role=gov-spec-writer build=dFurnishedOrders unit=TOOL-dFurnishedOrders-46 path=memory/builds/dFurnishedOrders/prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-46-1-spec-writer.md role-sha=06b14b1ac42a task-sha=f70b9d64795a -->

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

This handoff is for build `dFurnishedOrders`, unit `TOOL-dFurnishedOrders-46`.
Not supplied, optional: `card:route`.

### brief:goal

Revise the 22 dFurnishedOrders specs that the cross-check record names under "For the re-ground".
Each one should state its parents' surfaces the way their specs now spell them on origin/main at
`1a61f21a2`: dBoundRoles as its re-ground `ac8ab8d5f` left it, dTotalRecall as `794a0f5fb` left it,
dKeptSession as `ff44fb2a2` left it, and the rules dOrderedCharter, dDeclaredLoop, dWitnessedBar and
dPlacedRequest apply to every spec. Each spec keeps its own design, and only its assumptions about the
parents change.

### brief:items

Read the cross-check record first,
`memory/builds/dFurnishedOrders/build/2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck.md`.
Its summary table numbers every assumption (rows 1 to 127). Section 2 of each group's return in
`memory/builds/dFurnishedOrders/build/2026-10-28-build-TOOL-dFurnishedOrders-1-crosscheck-returns.md`
quotes both sides of each MISMATCH and states its `Change:`. Read each parent spec the record cites, at
the lines it cites. This brief summarises them, and where the two differ, the specs win. Before you
edit for a row, re-read both sides. A row the parent's text does not bear out is not edited: return it
as refused, with the line that refutes it.

Facts every revision uses:

- **A catalogue-default read.** `read_policy_setting(key, root)` (br21 S1) is the roles kit's one
  runner of `policy.py get`, found through `resolve_kit_dir("policy", "policy.py", here)`; it returns
  None both for a key at its catalogue default and for no policy kit found, and its `with_default`
  argument is the form a read with a catalogue default takes (br21:41-50). br43 S21 makes every caller
  use `with_default` where it reads the catalogue default, and says no file under `tools/roles/` runs
  `get` outside it or imports the policy kit (br43:105-110); br43 AC21's predicate is
  `git grep -n -E "policy\.py.*get|from policy import|import policy" -- 'tools/roles/*.py'`
  (br43:427-429). With `with_default=True`, None means only that no policy kit was found: a spec keeps
  a typed value only as that fallback, with its note, and drops the roles-kit copy of the default.
- **A sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205). A by-file load
  (`importlib`, `spec_from_file_location`, `load_kit_module`) or a `sys.path` insert of another kit's
  directory is an in-process import. Code in one kit reaches another kit's verb by subprocess, found
  through the inline `resolve_kit_dir`; br12, br14, br20 and br43 are the precedents for adding a verb
  to the kit that owns the data. A hook spawns `node <policy kit>/policy-mirror.js get <key>` instead of
  `require`-ing it (ks8:62-66). Where the verb does not exist, write a §8 fork open for the owner: an
  ask to the owning build for the verb, or a declared `requires_if` row on `tools/roles/kit.toml`
  (today it holds one only for review-harness, `tools/roles/kit.toml:19`), with the reason the rule
  admits it. Recommend one.
- **A leg.** oc7 S3 reds a leg with no `enforces` (oc7:58-63). wb11 declares each leg once, in its kit's
  `[[gate_leg]]` row or a `tools/govkit/registry.toml` `[[exempt_leg]]` row holding every manifest key,
  `enforces` among them; `leg_factory.py --write` renders `tools/gate-legs.json`, and `--check` reds a
  manifest that differs (wb11:36-49, :154). `govkit selftest` is the `[[exempt_leg]]` row at
  `tools/govkit/registry.toml:439`: a spec that re-guards it edits that row and renders. The
  `answered-calls self-test` leg is declared once, by fo6 S9, with `leg_factory.py new` and a named
  `enforces`; fo29 S19 and fo37 S24 re-guard that declaration. An AC reads the rendered row or
  `leg_factory.py --check`. Where `leg_factory.py` is not built at the pass, the pass records that a
  hand edit stood in for it.
- **br3's `--item` render.** br3 S1 runs `loop_lib.py declaration --item <tag> --json` in a subprocess,
  and a tag the loop does not declare or no loop kit found refuses with exit 1 and writes nothing
  (br3:39-47). A stub `loop_lib.py` in a fixture answers `declaration` as well as `seed`. The verb
  itself is br3 F5's open ask to dDeclaredLoop.
- **An ask.** No dFurnishedOrders spec files a row in another build's `BACKLOG.md`. Where a fix needs a
  parent change, write a §8 fork open for the owner, with its options and a recommendation, and name
  the ask the build run would file.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every spec
of that group, and no other:

- **Group A, catalogue defaults, led by spec 2:** specs 2, 5, 8, 16 and 18.
- **Group B, policy reads and the loop render, led by spec 17:** specs 7, 11, 12, 17 and 20.
- **Group C, the roles kit's cross-kit loads and the `answered-calls` leg, led by spec 29:** specs 3,
  6, 10, 14, 29, 37 and 42.
- **Group D, the `govkit selftest` leg and the tester template, led by spec 46:** specs 15, 46, 48, 50
  and 58.

The spec files are `memory/builds/dFurnishedOrders/spec/2026-10-2?-spec-TOOL-dFurnishedOrders-<n>.md`.
Write probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-beautiful-lalande-23ce8b/a46c346a-6f74-4403-a01d-0c3480a8d930/scratchpad/fo-w<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; the sections moved; each fork
you added or re-resolved, with its mark; each record row you refused, and why; its byte count; and any
parent spec that looks wrong.

Per spec, by the record's rows; each row's `Change:` in the returns record is the starting point:

1. **Spec 2** (row 6). `prompts.batch` read with `with_default=True`; the roles-kit `per-batch` copy
   goes; F3 keeps its no-kit meaning.
2. **Spec 5** (row 19). Both keys read with `with_default=True`; `keyed` and `cold` stay only as the
   no-policy-kit fallback, with a note.
3. **Spec 8** (row 35). `instructions.slices` read with `with_default=True`; the typed `handed` goes.
4. **Spec 16** (row 63). `attendance` read with `with_default=True`; a no-kit None takes S1's
   `unread: <why>` path.
5. **Spec 18** (row 77). `annotations.delivery` read with `with_default=True`; the literal stays only
   for the no-kit None.
6. **Spec 7** (rows 32, 33). `roles.on-contradiction` through `read_policy_setting(...,
   with_default=True)`; the backlog rows rendered through a memory-tree verb by subprocess, or the fork.
7. **Spec 11** (rows 46, 47). Both keys through `read_policy_setting(..., with_default=True)`; the
   ledger registrations read through a memory-tree verb by subprocess, or the fork.
8. **Spec 12** (rows 50, 51). F1's probe re-pinned to a content-anchored grep over br1's roster table;
   both keys through `read_policy_setting(..., with_default=True)`.
9. **Spec 17** (rows 68, 71, 72, 73). The Edges bullet names asks TOOL-dTotalRecall-102 and -103 as what
   would make tr8 land the `neighbourhood` reader; AC2's stub answers `declaration --item`; the
   no-loop-kit branch goes from the `--item` path; both keys through `read_policy_setting(...,
   with_default=True)`, the AC1 fixture line reworded from `resolve` to `get`.
10. **Spec 20** (rows 86, 88). The no-loop-kit branch goes from the `--item` path; `read_claims` passes
    both `refs/gov/leases` and `refs/gov/runs` to a namespace reader that fetches a list in one bounded
    fetch (pr1:76-80).
11. **Spec 3** (rows 11, 12). `notices.record` read by `policy.py get` by subprocess; runlog reached
    through a runlog verb by subprocess, or a declared `requires_if` row.
12. **Spec 6** (rows 26, 27). `answered-calls self-test` declared once with `leg_factory.py new` and a
    named `enforces`, rendered by `--write`, with a `--check` criterion; `answered-calls.js` spawns
    `policy-mirror.js get roles.answered-calls`.
13. **Spec 10** (row 43). F3 re-resolved to a runlog verb run by subprocess; S7 reads the matrix
    through `loop_items.py matrix --json`.
14. **Spec 14** (row 55). Open repair asks read through a memory-tree verb by subprocess, or the fork.
15. **Spec 29** (rows 98, 99, 104, 105, 107). S9's five keys with `with_default=True`, and its end
    state restated as no `get` run or policy import outside `read_policy_setting`; AC7 takes br43
    AC21's predicate; AC8's stub logs its verb and counts `seed` lines; S6 and S11 reach runlog and the
    playbook kit by subprocess verbs or declared `requires_if` rows; S19's guard sits on fo6 S9's
    declaration and is rendered.
16. **Spec 37** (rows 113, 114). S2's check also flags by-file loads of another kit's file that no
    `requires_if` row admits; S24's guard sits on the declaration.
17. **Spec 42** (row 120). The cap read through a policy-kit verb by subprocess, or the fork; the
    `sys.path` insert goes.
18. **Spec 15** (row 60). The tester template keeps br2 F4's `answered` outcome and `answer:text?`
    beside `designed` and `judged`; the body returns `answered` for `test.reason`.
19. **Spec 46** (rows 122, 123). S8's guard files go on the `govkit selftest` `[[exempt_leg]]` row and
    are rendered; S5 runs the lexicon check through a lexicon verb by subprocess, or the fork.
20. **Specs 48, 50 and 58** (rows 124, 126, 127). Each guard or home-row edit goes on the `govkit
    selftest` `[[exempt_leg]]` row at `tools/govkit/registry.toml:439` and is rendered by
    `leg_factory.py --write`; Files touched gains the registry; fo58 S25 says the declaration, the
    render and the waiver rows land in one commit.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-28, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record, with its row numbers.
- Replace each now-false sentence where it stands.
- A resolved fork whose chosen option a parent now rules out is re-resolved on rung 1, naming the
  parent, and marked `RESOLVED (agent, 2026-10-28, delegated)`. A fork this brief tells you to leave
  open for the owner stays open, with its recommendation. Re-open no other fork.
- Spell a `tools/` path inside an acceptance criterion as the spec already does.
- Stay under the class cap of 49152 bytes; replace text rather than append where a spec is near it.

### brief:acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>`, and §9 holds the new line.
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `foN:L`
  prints nothing, or prints only the corrected sentence.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### brief:gates

Only the memory hygiene gate and the naming lexicon, as the role allows. The main loop runs the rest
and renders the index.

### brief:non-goals

- No file outside the spec files of your group. No commit, no stage into the real index, no deviation
  record: the main loop writes those.
- No file of dBoundRoles, dTotalRecall, dKeptSession, dOrderedCharter, dDeclaredLoop, dWitnessedBar,
  dPlacedRequest, dSafePassage or dGroundRules. A parent spec that looks wrong is a line in your
  return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### input:spec

memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-46.md

### task:reuse

the last wave's procedure: memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md and -parents-reground.md, its record build/2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck.md, its deviation records; tools/roles/handoff.py render|agents for every handoff and ledger row.

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
