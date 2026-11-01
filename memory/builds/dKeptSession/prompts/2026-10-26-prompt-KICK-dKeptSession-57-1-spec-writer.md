**Serves:** journal KICK-dKeptSession-1 KICK-dKeptSession-57

# gov-spec-writer handoff — KICK-dKeptSession-1

<!-- gov:handoff role=gov-spec-writer build=dKeptSession unit=- path=memory/builds/dKeptSession/prompts/2026-10-26-prompt-KICK-dKeptSession-57-1-spec-writer.md role-sha=06b14b1ac42a task-sha=0d1c50f832a6 -->

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

This handoff is for build `dKeptSession`, and names no single unit.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dKeptSession specced and built, so that each of the 28 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 16 owned nodes (Owned nodes) is built, and each of its 8 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0139@065e06ab` · now `065e06ab`, as at the baseline · tokens: `build.closes`, `guarded`, `review.design.round-count`, `review.max-rounds`, `strict` — the named presets and their completeness check, with its pair rules, `review.design.round-count` held at or below `review.max-rounds` among them, seen red on a planted override past it, and each shipped preset loaded with only the core installed, refused only for a value on a core key that selects an absent expansion, seen red both ways: on a planted Absent clause that refuses by key, and on a loader stubbed to accept every value, since `strict` and `guarded` must be refused for `build.closes` on a core-only install
2. `cl-dClosedLoop-0140@6531184d` · now `6531184d`, as at the baseline · tokens: `hooks.bypass`, `refused` — the preset step added to dGroundRules's reader, so a key the file does not override reads the named preset's value, seen red when a strict-named file with no override reads `hooks.bypass` as anything but `refused` (DA-M10)
3. `cl-dClosedLoop-0141@4d07a3de` · now `4d07a3de`, as at the baseline · tokens: none, so the token arm cannot see this clause — the charter's preset section, the preset's name and the keys that differ from it, rendered through dOrderedCharter's renderer and seen red on a planted override (DA-M3)
4. `cl-dClosedLoop-0142@816ff525` · now `816ff525`, as at the baseline · tokens: none, so the token arm cannot see this clause — policy at govkit intake
5. `cl-dClosedLoop-0143@cafeb575` · now `cafeb575`, as at the baseline · tokens: `flow.wait-ceiling`, `refs/gov/mail/<slug>/<fleet tag>/<session>` — the mailbox per build, one append-only ref per writing session (`refs/gov/mail/<slug>/<fleet tag>/<session>`, revised by the night pass two, point 3, the owner's NT-16, and keyed by session by the night pass two's review, since a node's sessions would share a node's ref), its closed set of message kinds checked on write, written only through the coordination verbs, which pass the record door once dTotalRecall lands it and write the ref directly until then (the closing pair's door-misses-coordination-verbs), read at every transition, which is refused while a message addressed to the build is neither answered nor acknowledged until `flow.wait-ceiling` passes, seen red on a planted unanswered message, disposed there, shown on the card and kept in the build's transition log (coordination item 6, the whole-design audit's C2-F15)
6. `cl-dClosedLoop-0144@c41201f3` · now `c41201f3`, as at the baseline · tokens: none, so the token arm cannot see this clause — live delivery where the harness has it
7. `cl-dClosedLoop-0145@b38efe3e` · now `b38efe3e`, as at the baseline · tokens: `deps.coordination`, `deps.early-build` — dependency coordination by the parent's lease as `deps.coordination` says, interfaces confirmed at Design's exit, early building as `deps.early-build` admits, change and landing notices, each key seen on strict's value (the whole-design audit's C2-F11)
8. `cl-dClosedLoop-0146@a9c32df5` · now `a9c32df5`, as at the baseline · tokens: `actions.free` — `actions.free` at the tool call
9. `cl-dClosedLoop-0147@9a464fcd` · now `9a464fcd`, as at the baseline · tokens: `orient.budget`, `warn-at-evidence-ceiling` — orientation cost recorded per stage and held as `orient.budget` says, seen on strict's `warn-at-evidence-ceiling` (the whole-design audit's C2-F11)
10. `cl-dClosedLoop-0148@ab3d7b8c` · now `ab3d7b8c`, as at the baseline · tokens: `intake`, `mailbox.reads` — the mailbox read at every item boundary by `mailbox.reads`, with the `intake` message kind
11. `cl-dClosedLoop-0149@d9aa0a3a` · now `d9aa0a3a`, as at the baseline · tokens: `notify.owner` — progress reported by `notify.owner`
12. `cl-dClosedLoop-0150@1c3b5ca1` · now `1c3b5ca1`, as at the baseline · tokens: `always-resume`, `fresh-when-idle`, `resume.context` — a fresh session in the build's worktree recommended until the card-import fixture passes, the fixture winning over `resume.context`: while it is red, `always-resume` read as `fresh-when-idle` and the override reported, never silent, seen on a planted `always-resume` with the fixture red that resumes no idle session and reports the override (the owner's FK-1-6)
13. `cl-dClosedLoop-0151@32b6ed5a` · now `32b6ed5a`, as at the baseline · tokens: `card.pointers` — the card's pointers updated as the build progresses, by `card.pointers`: the latest records by tag, the open forks and the item in flight, so a compacted or fresh session reorients from them
14. `cl-dClosedLoop-0152@da455c7f` · now `da455c7f`, as at the baseline · tokens: `context.on-full`, `context.threshold` — what a session does as its window fills, by `context.on-full` and `context.threshold`
15. `cl-dClosedLoop-0153@9a9b7d43` · now `9a9b7d43`, as at the baseline · tokens: none, so the token arm cannot see this clause — a compaction's summary read as a lead, never a source
16. `cl-dClosedLoop-0154@62e72743` · now `62e72743`, as at the baseline · tokens: `memory.map-purpose`, `review` — the policy namespaces' purposes, reviewed as `memory.map-purpose`'s default, `review`, says, a stand-in until dTotalRecall lands the key (the whole-design audit's CS4-F1)
17. `cl-dClosedLoop-0155@6d913746` · now `6d913746`, as at the baseline · tokens: `attendance`, `step —` — the attendance rule: `attendance` places owner breakpoints and has owner questions asked live, and never selects an item's actor, the driver or a binding, its arm seen red on a planted value that swaps an actor, the `step —` announcement joining when dWellOiledMachine lands it, and owner questions asked live joining when dFurnishedOrders lands them (night pass, point 1)
18. `cl-dClosedLoop-0156@c935df77` · now `c935df77`, as at the baseline · tokens: `none`, `playbook`, `repeat` — the `repeat` disposition in the placement set and its `none` row in the transition table, routing a request onto a `playbook`, filed as an ask until dIndexedDesign lands that record kind (night pass, point 1)
19. `cl-dClosedLoop-0157@7d569b91` · now `7d569b91`, as at the baseline · tokens: none, so the token arm cannot see this clause — the catalogue's reader join: every key named by a unit on its owner build's row, today's unnamed keys a shrink-only population (the away pass's closing review)
20. `cl-dClosedLoop-0158@19d3fbd9` · now `19d3fbd9`, as at the baseline · tokens: none, so the token arm cannot see this clause — a scenario's preset slot: a named preset and overrides scoped to the builds placed under the scenario, read through the one reader before the repository's own values, never a key presets never touch, seen on two builds under scenarios with different presets (the night pass two, point 1, the owner's NT-3)
21. `cl-dClosedLoop-0159@ad40c608` · now `ad40c608`, as at the baseline · tokens: `deps.messaging`, `every-tool-call`, `mailbox.fetch-seconds`, `mailbox.notice` — news shown as `mailbox.notice` says, at every item by default and at every tool call where the owner's policy sets it: at an item boundary the notice runs one fetch of the mail refs, bounded by a timeout, before it lists the unread message ids addressed to the session's build or item, falling back to the node's local copy and naming its age when the fetch fails, and at a tool call a hook lists them from the node's local copy, with no network call, starting a detached fetch when the copy is older than `mailbox.fetch-seconds`, the live channel `deps.messaging` picks carrying only a message's ref and id so a lost ring costs only latency, and the disposal still at items and transitions, seen on a message posted on one node shown on another at its next item boundary after the post, red where the boundary's fetch misses it, on that fetch planted to fail, the local copy shown with its age, and under `every-tool-call` at its next tool call within twice the fetch interval (the night pass two, point 3, the owner's NT-17, the answers' review)
22. `cl-dClosedLoop-0160@3e3e0128` · now `3e3e0128`, as at the baseline · tokens: none, so the token arm cannot see this clause — each message's id derived from its build, its item's instance key, its pass, its kind, its subject and the id it answers, never from its sender's session, and from its act once Runtime mints acts, the duplicate check reading every one of the build's per-session refs, so a retried post is refused as a duplicate, a retry from a new session among them, while two answers to two messages both land, seen on a post retried after a crash, on a retry from a new session and on two acknowledgements from one item (the night pass two, point 4, the owner's NT-18, the answered id added by the night pass two's review, the session dropped by the owner's FK-1-7)
23. `cl-dClosedLoop-0161@10c6cad1` · now `10c6cad1`, as at the baseline · tokens: none, so the token arm cannot see this clause — every mail write appended to the change feed once its ref update lands, in the feed's census, red on a planted mail write that skips the append (the owner's NT-14, the answers' review)
24. `cl-dClosedLoop-0162@6ce67958` · now `6ce67958`, as at the baseline · tokens: `flow.wait-ceiling` — a message awaiting an answer declaring `flow.wait-ceiling` as its deadline, judged by the declared clock dPlacedRequest's leases use, the time since the waiter first saw the message, past which the asker's declared default answers it and the build's transitions go on, seen on a planted question nobody answers and red on a reader whose clock runs a day ahead (P39, the whole-design audit's A2-F6)
25. `cl-dClosedLoop-0504@b051ecfa` · now `b051ecfa`, as at the baseline · tokens: `flow.wait-ceiling`, `leases.renewal: progress`, `mailbox.answer`, `next`, `question` — `mailbox.answer`: a `question` addressed to a build answered by the role that owns the asked interface or item, dispatched by `next` when the question arrives, and until dWellOiledMachine lands `next`, a question to an unattended build answered by the asker's declared default under cl-0162, the same stand-in covering its answering role (the closing pair's answer-dispatch-non-ancestor), and the recipient's transition, refused meanwhile, a declared wait inside `flow.wait-ceiling` that `leases.renewal: progress` renews, seen red on a planted question to an unattended build whose lease lapses while it waits (the whole-design audit's A2-F5, the owner's FK-5-4)
26. `cl-dClosedLoop-0163@709e57f9` · now `709e57f9`, as at the baseline · tokens: none, so the token arm cannot see this clause — the card showing the build's remaining rework budget beside its pointers, seen red on a planted card that omits it (P39, the parked debt's review)
27. `cl-dClosedLoop-0164@148f5fda` · now `148f5fda`, as at the baseline · tokens: `changed`, `confirmed` — each message carrying its session's sequence number, a take-over naming its predecessor's last message, and `confirmed` and `changed` carrying the interface's content key, a dependent acting on the recomputed key and never on arrival order, seen red on a relayed `changed` that arrives before the `confirmed` it supersedes (P40)
28. `cl-dClosedLoop-0165@8c92ee12` · now `8c92ee12`, as at the baseline · tokens: none, so the token arm cannot see this clause — a mailbox recipient naming a node by its fleet tag, or the whole project (P40, the owner's CL-4)

### brief:acceptance

- At the Design exit, `carries.py --build dKeptSession --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dKeptSession` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dKeptSession --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 481 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dKeptSession by <decision>` line.
- Any path outside `memory/builds/dKeptSession/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.
- The surfaces of dTotalRecall, dWellOiledMachine, dIndexedDesign, which this build's clauses use as stand-ins only (Later builds named).

### input:spec

memory/builds/dKeptSession/prompts/2026-10-26-prompt-KICK-dKeptSession-57-promoted-fix-brief.md

### task:reuse

dGroundRules' policy reader and catalogue, dDeclaredLoop's loop kit, dPlacedRequest's leases and card ref, as the scouts record.

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
