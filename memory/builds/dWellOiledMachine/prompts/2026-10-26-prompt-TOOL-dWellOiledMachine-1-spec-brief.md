**Serves:** research TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61

# Spec brief — dWellOiledMachine, the sixty-one units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dWellOiledMachine/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens (item N is unit `TOOL-dWellOiledMachine-N`);
   its Acceptance, Gates, Non-goals, Pins, Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind
   every unit.
2. The build README, `memory/builds/dWellOiledMachine/README.md`: its build-level rules bind every spec, the fork
   rule above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every row of "Shared interfaces" and "Edges", and the scout record your units
   cite, under `memory/builds/dWellOiledMachine/build/`: `2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md`
   (units 1, 6-9, 19, 25, 30, 32, 36, 37, 39, 43, 45-47, 49, 53, 56), `-b.md` (3-5, 10, 12, 14, 20-23, 26-29, 31, 38,
   42, 44, 48), `-c.md` (2, 11, 33-35, 40, 41, 54, 58-60) and `-d.md` (13, 15-18, 24, 50-52, 55, 57, 61). Each holds a
   seam row per clause with path:line at `0689e7fa1`, its own shared-interface proposals, and the places a parent
   spec and source disagree. Where a scout's proposal and this brief differ, this brief wins.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, Runtime's `[extend]`
and the `[policies]` rows the packet's Obligations list by v2 line), `B/…-layer-runtime.md` (the Runtime layer:
`[decide]`, `[act]`, `[enforce]`, `[isolate]`, `[sessions]`, `[schedule]`, `[extend]`, the fixtures list), the
`B/…-research-runtime-*.md` records (executor, floor, hooks, sessions, spawn, instruments), `B/…-layer-roles.md`,
`B/…-layer-memory.md` and the memory plan (`[doors]`, `[pockets]`), `B/…-coordination.md`, `B/…-orientation.md`,
`B/…-flow-roles.md`, `B/…-flow-interactions.md`, `B/…-night-pass.md`, `B/…-night-pass-two.md`, the stall-and-loop and
cloud-and-scale records, the gap register `B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` (each gap the
packet's Gaps section names, by line), and the fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`
lines 900-946. You never edit an instrument, v2, the as-built view or the packet: the packet's Non-goals.

## The parents are specced, not built

dBoundRoles, dTotalRecall and dKeptSession, this build's parents, landed their specs and are DEFERRED to their build
runs; so are their own parents dDeclaredLoop, dPlacedRequest, dWitnessedBar, dOrderedCharter, dSafePassage and
dFairHearing. dGroundRules' policy kit IS built and landed: `tools/policy/` (`catalogue.toml`, `policy.py` with
`resolve` at :752 and `check_value` at :143, `policy-mirror.js` with `readPolicy` at :132, `policy-shim.sh get`,
`guard.py`, `guarded-paths.txt`). Every policy key this build owns or reads already has its catalogue row
(`catalogue.toml`; scouts A-D cite each line), so a unit adds readers and enforcement, never a second row; where a
row's shape is wrong for its clause (scout A: `runtime.spawn-backend` is a literal enum where `[extend]` says names
are validated against the registry), change it in the unit and say so in §2.

None of these exist at HEAD, so each is a parent spec id and section, never a file you cite as built: `tools/loop/`
(TOOL-dDeclaredLoop-*: item registry `loop.toml`, transition record, position engine `position.py`, breakpoints,
budget `budget.py`, endings, scenarios, the `next` stand-in), `tools/lib/gov-ref.sh` (`write_gov_ref`,
`build_gov_commit`, TOOL-dPlacedRequest-11), the change feed (TOOL-dPlacedRequest-13), the lease grammar and declared
clock (`check_deadline_passed`, TOOL-dPlacedRequest-1, -17), the build card ref (TOOL-dPlacedRequest-2), the request
record (TOOL-dPlacedRequest-19), `tools/lib/commit_trailers.py` (`read_commits`, TOOL-dDeclaredLoop-23),
`tools/playbook/namespaces.toml`, `edges.toml` and `kinds.toml` (PLAY-dOrderedCharter-*), `gov_record.py` and
`record-kinds.toml` (TOOL-dTotalRecall-2), `record find`/`record show` (TOOL-dTotalRecall-9), the mailbox
(KICK-dKeptSession-5), the roles pack and its spawn guard (TOOL-dBoundRoles-25), Roles' resolver (TOOL-dBoundRoles-21).
Cite the spec by id and section, name the call you make, and never re-spec a parent's mechanism or add a copy of
`resolve`, `write_gov_ref`, `read_commits` or a card writer. Scout A notes three dBoundRoles specs cite
`agent-cap.js` lines that moved; cite source at HEAD and the spec by section.

## Every spec, whatever its unit

- Path `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-<n>.md`; H1
  `# TOOL-dWellOiledMachine-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order <k> ·
  advances TOOL-dWellOiledMachine-62`, with `<k>` your unit's order below. `OPEN` is the status token: `DRAFT` is not in
  `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py:28`). The shape is
  `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-5.md` line 3.
- Binding lines, each at column 0 on a line of its own under the status line:
  `**Carries:** <Items id>@<hash8> whole`, and for each owned node the table below gives your unit,
  `**Carries:** node:<node>`. A unit carrying a clause in parts writes `part <k>/<n>` instead of `whole`, and every
  part is carried by a spec of this build.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 5, 7, 8, 12, 13, 14, 18, 21, 22, 24, 30, 31, 52, 57, 60, 61) still names its key words
  in backticks where they are code.
- Each clause's own "seen red on" and "seen on" cases are acceptance criteria, each observed RED on its planted case
  and green without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge
  bar, a `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7,
  and the main loop observes it at the close. A case that needs a live harness (the spike, the conformance fixture,
  the hold case) names its live fixture, the binary version it pins and what it records, and has a stubbed-transcript
  arm a pass can run offline. "Seen on strict's value" means the planted policy file names `preset = "strict"` and the
  case reads the key's strict cell from KICK-dKeptSession-1's preset store.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `0689e7fa1`: verify each line number before citing it.
- §8 forks: settle each by the README's rungs (the execution plan lines 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`; a `relaxes:` value joins a record with `**Bound:**`,
  `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a choice the README's
  `may: PLAY-dClosedLoop-3` grant lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave an open
  question: a FACT-QUESTION names its probe and you run it, and a probe READS, it never builds an arm (M3).
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/`, `memory/guides/*.md` from their kit templates,
  `tools/workflows/*.js` from their `.template.js`, `.claude/settings.json` from the fragments by the settings merge,
  and the installed kickoff skill from `skills/session-kickoff/`: name the source as the edit and the render as its
  copy.
- A later build's surface named in your clause (dRankedPlan, dShippedRelease, dConvergedCharter, dTendedCadence) is a
  stand-in or a join that build arms: spec the stand-in this build ships and name the hand-over, never the later
  build's mechanism (packet Non-goals, Later builds named). Register a stand-in as a `[[stand-in]]` row
  (TOOL-dDeclaredLoop-13 S8).
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dWellOiledMachine/build/2026-10-26-build-TOOL-dWellOiledMachine-<n>-deviation-<k>.md`, in
  the grammar `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- A parent spec that must change for your clause to hold (scout C: TOOL-dPlacedRequest-20's `offer` names a fleet
  tag only where cl-0319 offers to a session too; scout C: the lease record's raw `session:` against `salted`) is never
  edited: state the needed change in §8 as an ask for that build, its target build and its accept line, and your
  return names it. The main loop files every such ask once, after the writers return, so no two writers mint an id
  in one foreign family (PLAY-dClosedLoop-32).
- Write nothing outside `memory/builds/dWellOiledMachine/spec/` and `memory/builds/dWellOiledMachine/build/`; temp
  files go under the scratch path your harness names.

### What the last five spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python spike.py …`) and keep its full
  path in §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it inside
  a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. When you hand off to a unit another writer owns, name the token exactly as "Shared interfaces" spells
  it, and that writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours. The table under "Edges" is the set to declare;
  add an edge only when your spec truly reads or produces it, and say so in your return so the other writer adds the
  reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a file, a sentence a fixture asserts) owes a
  `**Readers:**` clause naming every reader by path and by value (hygiene check 25), each found by `git grep` over
  the tree. Check 25 reads any retirement word ("drops", "retired", "replaces") beside a backticked token in §2: use
  one only where you mean it. Units 28, 38 and 42 retire named things; the clauses list some readers and the scouts
  found more (scout B: `tools/roles/house/gov-session.md`, `.claude/roles.json:43`, `handoff.py resolve_card_path`).
- **No link-shaped text**, a bracketed label followed by a parenthesised target, anywhere outside a real link,
  backticks included (hygiene check 2).
- **A §8 mark wraps whole.** `deviations.py` reads a `RESOLVED` mark's ruling, `widens:` and `relaxes:` from the mark
  itself: keep each mark one paragraph, with no list or blank line inside it.
- **Serves lines.** A record whose filename names a unit id lists that id on its `**Serves:**` line (hygiene check
  21): a deviation record for unit n serves `TOOL-dWellOiledMachine-<n>`.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,21,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` and `carries.py --report dWellOiledMachine` after every writer returns.

## Owned nodes

Each of the packet's 69 owned nodes is carried by exactly one unit, as `**Carries:** node:<node>`. A unit that reads
a node another unit owns names it in its text and declares the edge; it does not carry it.

| Node | Unit |
|---|---|
| `point.spawn-backends`, `policy-key.runtime.spawn-backend` | 1 |
| `record-kind.journal`, `policy-key.runtime.journal`, `point.journal-readers` | 16 |
| `record-kind.node-profile` | 61 |
| `tag-namespace.hook`, `tag-namespace.point` | 20 |
| `policy-key.runtime.secret-scan` | 17 |
| `point.harness-adapters`, `policy-key.runtime.harnesses` | 14 |
| `point.host-adapters` | 13 |
| `policy-key.runtime.binary`, `policy-key.runtime.owner-harness` | 36 |
| `point.hook-packs`, `policy-key.runtime.hook-failure`, `policy-key.runtime.attended-judge`, `policy-key.runtime.attended-allowance` | 10 |
| `record-kind.act`, `policy-key.trace.identity`, `policy-key.trace.cost` | 32 |
| `record-kind.session-binding` | 12 |
| `policy-key.memory.default-load` | 23 |
| `record-kind.workspace`, `policy-key.build.worktree` | 11 |
| `policy-key.commits.edge-check` | 33 |
| `policy-key.build.push` | 40 |
| `item.life.unlease`, `item.life.quiesce`, `record-kind.quiesce` | 58 |
| `point.command-adapters`, `policy-key.run.host`, `policy-key.runtime.relaunch` | 6 |
| `policy-key.runtime.secret-home` | 37 |
| `policy-key.runtime.act-harness`, `policy-key.runtime.act-auth`, `policy-key.roles.harness.<role>`, `policy-key.roles.auth.<role>` | 56 |
| `record-kind.return` | 8 |
| `point.role-harnesses`, `policy-key.roles.shape-enforce` | 19 |
| `policy-key.runtime.admission-scope`, `record-kind.node-ledger` | 53 |
| `item.entry.intake`, `record-kind.intake` | 4 |
| `item.life.notify`, `point.notification-adapters`, `policy-key.notify.channel`, `policy-key.notify.owner-items`, `policy-key.run.owner-deadline`, `policy-key.run.on-owner-silence` | 48 |
| `item.life.request`, `item.life.close`, `item.life.snapshot`, `policy-key.attendance.scope`, `record-kind.attendance-override`, `record-kind.lifecycle-request` | 3 |
| `policy-key.runtime.act-ceiling`, `policy-key.runtime.hold-ceiling`, `policy-key.runtime.restarts` | 47 |
| `policy-key.runtime.no-progress` | 46 |
| `policy-key.runtime.refusal-repeats` | 49 |
| `policy-key.build.unit-holders` | 41 |
| `policy-key.trace.rows` | 34 |
| `policy-key.build.spend-cap` | 51 |
| `point.cadence-items` | 59 |
| `point.memory-mirrors`, `policy-key.memory.mirror` | 44 |
| `point.actor-kinds` | 25 |

Scout D notes the packet lists no `point.lease-stores`, `point.doorbells` or `point.offer-sources` though v2:1905
declares them: unit 55 declares those three points as rows of I4 and records the gap as a deviation, never as a
packet edit.

## Shared interfaces — one spelling for every writer

Fixed so sixty-one specs by six writers agree on the interface axis (M2). Each row names its owner, the unit whose
spec defines it; every other unit names it exactly as spelled here and cites the owner. A spelling marked "proposed"
has no source yet; the owner may refine it in its spec, and says so in its return. A writer who finds one wrong says
so in its return and writes a deviation record rather than a second spelling.

| # | Interface | Spelling | Owner | Source |
|---|---|---|---|---|
| I1 | The runtime kit | `tools/runtime/`, a kit with its own `kit.toml` and adopter (the repository's kinds rule), created by the spike so the spike is the platform's first artifact; the unattended kit's hooks and supervisor seam move into it at unit 28 (proposed) | 1 | NP:75 "the runtime's own kit"; scouts A, B, C |
| I2 | The act launcher | `launch_act(item, work_order, harness, env)` in `tools/runtime/launch.py`, the one builder of a harness argv and its launch environment, extracted from `check_policy.py run_live_session` (:4289) at its second instance, never a copy; `resume-tick.sh:385`'s launch moved onto it at unit 6 (proposed) | 1 | `check_policy.py:4289-4304`; `resume-tick.sh:383-386` |
| I3 | The journal | runlog grammar v1 (`runlog_lib.py` `parse_line`, `check_line`, `render_line`, `read_journal`) moved into the core with its readers re-pointed, a producer file `runtime.log` added to `PRODUCER_FILES`, event classes `no-progress`, `repeat`, `budget-spent`, `deadline-passed`, `breaker-open`, `cycle`, `refusal`, `stall`, `compaction`, `map-read-outside-slice`, `secret-hit`, each line keyed by `act=` or `session=`; one writer `write_journal_line <class> <k=v>…` per language; retention by `runtime.journal` pruned at the node tick | 16 | `tools/runlog/runlog_lib.py:30-40,148-322`; LR:938; stall-and-loop.md:251-253 |
| I4 | The point registry and adapter rows | `tools/runtime/points.toml`: `[[point]]` rows `name = "point.<x>"`, `purpose`, `contract` (unit 20 creates the file and the two namespaces' rows in `tools/playbook/namespaces.toml`); `[[adapter]]` rows `point`, `name`, `grant = { service, scopes, secret = "<ref>" | "anonymous" }`, `tenancy`, `retention`, `region`, a host row adding `custom-refs` and `auth-class`; `check_value`'s `registry` arm resolves a registered name against it (proposed) | 20 (rows), 17 (`grant`) | `policy.py:143-159`; LR:857-878; scout D I6 |
| I5 | The node home | `resolve_node_home`, override `GOV_NODE_HOME`, refactored out of `tools/runlog/extract.py resolve_state_dir` (:201) into a `tools/lib` block shipped inline like `health_log.py`; files `<home>/profile.toml` (61), `<home>/facts.toml` (15), `<home>/ledgers/` (53) | 61 | `extract.py:201-229`; `tools/lib/health_log.py:9` |
| I6 | The node profile | `<home>/profile.toml`, `schema = <major>.<minor>`, `fleet-tag`, `[hardware]`, `capacity`, `[[harness]]` `name`, `plan-tier`, `pool`, `[[project]]` `name`, `share`; read whole by `read_node_profile`, written only by the guarded owner command `gov profile set`; a credential shape refused through I12 (proposed) | 61 | `render_playbook.py:347 read_fleet`; `tools/policy/guard.py` |
| I7 | The harness capability table | `tools/runtime/harnesses/<adapter>.toml`, `[[capability]]` rows `name`, `value`, `measured-on`, `binary-version`; names include `prompt-submit`, `subagent-stop`, `permission-request`, `preset-session-id`, `headless-fork`, `schema-return`, `live-inbox`, `hook-hold-seconds`, `browser`, `credential-read`; kept apart from `workflows.toml`'s `harness` field (proposed) | 14 | LR:825-855; scout B I6 |
| I8 | The node facts | `<home>/facts.toml`, rows per binary `binary`, `version`, `os`, `shell`, `bash`, `path`, `interpreters`, `measured-utc`, and `[clock] offset-seconds`, `read-utc`, `source`; one writer `write_node_fact`; read by `runtime.binary`, `runtime.owner-harness`, `runtime.act-harness` (proposed) | 15 | LR:848-855; scout D |
| I9 | The hook pack | a `*.fragment.json` gaining `owner`, `class` (`refuse`, `warn`, `record`), `failure` (`closed`, `open`, rendered as `onFailure`), `budget-ms`, `key` and `refusal = {rule, remedy, actor}`; both readers changed together (`settings-merge.py load_fragment` :252, `check-wiring.sh read_fragment_keys` :159) | 10 | LR:596-717; `settings-merge.py:47-55` |
| I10 | The dispatcher | one entry per event, `node "${CLAUDE_PROJECT_DIR}/<prefix>/runtime/dispatch.js" <Event>`, running every registered pack for that event in registration order; govkit's per-fragment wiring replaced at unit 28 (proposed) | 10 | LR:620-632; scout B I2 |
| I11 | The refusal fields | `rule`, `remedy`, `actor` with TOOL-dBoundRoles-26 S1's actor set (`self`, `producer`, `driver`, `owner`, `build:<slug>`), the deny string prefix `BLOCKED by <pack>:` kept, checked at registration | 31 | TOOL-dBoundRoles-26 S1; `guard.py:41 REMEDY` |
| I12 | The secret scanner | `scan_secrets(text)` and `render_redacted(text)` with `redaction.tsv`, moved beside the journal grammar by unit 16 and extended by unit 17 with the value scan and its witness fields `resolved: yes|no|anonymous`, a count per population, a salted match id; `measure_legs.derive_redacted` folded into it or declared a subset | 17 | `runlog_lib.py:418-420,522,553`; LR:891-910 |
| I13 | The `next —` line | `next — <item tag> · actor <actor> · key <instance key>` and the terminal `next — none · <reason>`, one shape in the charter template's micro-format fence; `[[command]]` rows in each kit's `kit.toml` carrying `terminal = true` for a command that declares itself terminal; the laggard list a waiver file in `tools/dead-path-waivers.txt`'s shape (proposed) | 2 | TOOL-dDeclaredLoop-7 §4; `unattended.sh:5882-5920`; v2 P15 |
| I14 | The item instance key | `<item tag>@<round·pass>#<inputs>`, TOOL-dDeclaredLoop-7 S3's, never a second spelling; a spawn site adds `@site=<n>` for the return store | 2 (cites) | TOOL-dDeclaredLoop-7 S3 |
| I15 | The act | act id `act-<12 hex>` over node, item instance key and launch time (proposed); the act record of kind `act` with fields `act`, `item`, `work-order`, `harness`, `harness-session` (`pending` until the start event), `node`, `cause`, `epoch`, `task-sha`, `transcript=`, `cost`, `wall`; written through TOOL-dTotalRecall-2's `gov_record.py new act` | 32 | LR:376-388; v2 P35, P36 |
| I16 | The minimal binding | `refs/gov/bindings/<act>`, a parentless commit over the empty tree holding `act:`, `epoch:`, `node:`, `task-sha:` and under `salted` `digest:`, written by `write_gov_ref` (and `write_claim`'s pattern until it lands); the reader `read_binding <act>` falls back to the ref and answers `not-local` when the ref lacks it | 39 | `unattended.sh:2077-2087,2396`; TOOL-dPlacedRequest-11 |
| I17 | The session binding | `<git-common-dir>/gov/session-bindings/<session id>.md`, fields `session`, `owner` (yes or the act), `build`, `act`, `node`, `started-utc`, `after`, keeping today's card's `## route` section so `extractRouteUnits` reads it unchanged (proposed) | 12 | scout B I3; `scratch-guard.js:667,839` |
| I18 | The `Gov-*` trailers | `Gov-Act:`, `Gov-Session:`, `Gov-Unit:`, `Gov-Item:`, each a `[[trailer]]` row in `tools/playbook/edges.toml`, read only through `read_commits`; `Pass:` kept beside them | 33 | PLAY-dOrderedCharter-28 S5; TOOL-dDeclaredLoop-23 §4 |
| I19 | The commit queue | `tools/runtime/commit_queue.py`: one serial queue per build that commits role returns at their item's witness, the lander's lock never taken, its pushes routed by `build.push` (unit 40) and through the fence (unit 60) (proposed) | 11 | `unattended-build.template.js:1173-1266`; `lib-unattended.sh:1026` |
| I20 | The workspace | record kind `workspace` with `build`, `unit`, `path`, `branch`, `lease`, `allocated-utc`; root from `derive_worktree_root` (`render_playbook.py:560`); the sweep reaps only workspaces the supervisor allocated, branch-reconcile excluding leased ones | 11 | LR:719-760 |
| I21 | The supervisor | `tools/runtime/supervise.py`, started and restarted by `resume-tick.sh` at the node tick (`gov-resume-tick`), one act session per role act through I2, reconciling before its first beat; command items through registered command adapters, each declared `idempotent` or `reconcile` (proposed) | 6 | LR:357-486 |
| I22 | The slot ledger | one counting-semaphore module `tools/runtime/slots.py` extracted from run-gates' turnstile grammar (tickets, nonce-named beacons with a ttl, nonce-guarded reap; `run-gates.sh:1474-1515,1654,1734,1804`) at its second instance; a reservation sized by the stage's declared `fan` (TOOL-dBoundRoles-22), slots keyed by `agent_id`, runs by run id; the limit read through `resolve("runtime.agents-in-flight")` | 9 | scout A I4 |
| I23 | The node ledgers | `<home>/ledgers/plan.json` and `hardware.json`, `schema = <major>.<minor>`, one local writer `charge_reservation` / `release_reservation`, a reader refusing a newer major with a journaled reason (proposed) | 53 | `run-gates.sh:1474-1479` |
| I24 | The admission queue | `admit(call, reservation)` over I22 and I23, FIFO, never refusing for want of a slot, a held call's notice `admission — waiting · <n> in flight · <m> reserved · limit <k>` (proposed) | 45 | LR:452-454 |
| I25 | The return store | `<git-common-dir>/gov/returns/<run id>/<spawn site>.json` keyed by I14 plus spawn site, written at SubagentStop; the shared deferral block `{exit:'deferred-platform', key, pending, durable}` held byte-identical across the workflow templates with a parity check (proposed) | 8 | `tier2-review.js:1312-2020`; `unattended-unit.js:333-348` |
| I26 | The shape digest | the first 12 hex of SHA-256 over `handoff.py harness-args` JSON and `stage-efforts` JSON, as `derive_section_sha` (`handoff.py:307`) computes | 19 | scout A I11 |
| I27 | The intake record | `<git-common-dir>/requests/<key>.md` keyed by `derive_request_content_key` (TOOL-dPlacedRequest-19 S1), fields `origin` (`hook`, `mailbox`, `cadence`), `session`, `received-utc`, `redacted`, `bytes`; the hook writes verbatim text redacted through I12 and capped (proposed). KICK-dKeptSession-10's mail kind `intake` is the mailbox origin of this record, and govkit's `intake` verb is unrelated: unit 27 says so | 4 | FR:280-281; TOOL-dPlacedRequest-19 |
| I28 | The owner item | `raise_owner_item <kind> <build> <deadline>` writing a mailbox `question` to the owner and the line `owner item — <kind> · <build> · deadline <utc>`; answered through TOOL-dBoundRoles-11 S5's `resolve_owner_question` (proposed) | 48 | TOOL-dPlacedRequest-4 S8 |
| I29 | The wait | a wait record `wait — <kind> · <record id> · <build> · deadline <utc>` keyed by the waited record's id and the build, woken by that record's arrival on the change feed, the deadline judged by `check_deadline_passed`; one generic sweep over every declared wait at the node tick (proposed) | 18 | TOOL-dPlacedRequest-13, -17 S4 |
| I30 | The `step —` line | `step — <build> · <step> · <item> · <role> · <why> · writes <set>`, one shape in the micro-format fence, rendered from I13's answer and the item's declaration | 26 | NP:97-99 |
| I31 | The policy readers | Python `resolve(key)` (`policy.py:752`), shell `policy-shim.sh get <key>`, JS `readPolicy(key, {repo})` (`policy-mirror.js:132`); never a second reader | each key's owner | as cited |
| I32 | The writer check at the door | `check_writer_binding <ref> <writer>` in the record door TOOL-dTotalRecall-2 S1 ships, comparing a coordination write's ref path or sender to the writer's I17 session binding; every `gov` coordination verb writes through it | 58 | memory-plan `[doors]`; LR `[act]` |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 1 → 36, 6, 37, 56 | `launch_act` |
| 1 → 43, 45 | `hook-hold-seconds` |
| 16 → 24, 34, 46, 47, 49, 12 | `write_journal_line` |
| 61 → 15, 53, 52, 54 | `resolve_node_home` |
| 61 → 52, 53, 54 | `read_node_profile` |
| 20 → 22, 17, 14, 13, 10, 55, 44 | `points.toml` |
| 17 → 57, 4, 29, 13 | `scan_secrets` |
| 14 → 36, 10, 5, 29, 23 | `[[capability]]` |
| 13 → 15, 59 | `point.host-adapters` |
| 15 → 36, 52 | `write_node_fact` |
| 10 → 31, 4, 43, 24, 28, 7 | `dispatch.js` |
| 31 → 21, 49 | `refusal` |
| 2 → 23, 40, 26, 25 | `next —` |
| 32 → 39, 33, 6, 51, 53 | `act` |
| 39 → 33, 7, 35 | `refs/gov/bindings` |
| 12 → 38, 23, 35, 58, 7 | `session-bindings` |
| 11 → 33, 40, 41 | `commit_queue` |
| 33 → 35, 34 | `Gov-Act:` |
| 40 → 60, 41 | `build.push` |
| 55 → 60 | `point.lease-stores` |
| 58 → 57, 3, 41 | `check_writer_binding` |
| 6 → 37, 8, 7, 9, 47, 46, 25, 28 | `supervise.py` |
| 9 → 43, 45 | `slots.py` |
| 45 → 53, 47 | `admit` |
| 53 → 52 | `charge_reservation` |
| 19 → 30 | `shape-digest` |
| 4 → 27, 5 | `requests/` |
| 48 → 3, 47, 50 | `raise_owner_item` |
| 18 → 3, 47, 50 | `wait —` |
| 41 → 54, 42 | `offer` |
| 27 → 42 | `intake` |

## The units

**Writer groups and build order.** The `order` value is the build order: the platform spike and the runtime kit
first; then the journal, the node home and profile, the point namespaces and their purposes, the secret scanner and
grants, the harness capability tables, host adapters and node facts, and the conformance fixture that measures them;
the hook packs, refusal text and templates; `next`; the act, its binding and the session binding with the card and
default-load readers on it; workspaces, the commit queue, its trailers, the session node, the branch push, the
transport points, the fenced push, the record door and its secret scan; the supervisor, the launch preflight and the
per-role harness; the return store, the act and shape checks, experiment acts; slots, the in-flight ledger, admission
and its node scope and the beat; intake; owner items, waits, lifecycle requests, deadlines, the wait graph, progress
and the refusal breaker; unit holders, discovery and `gov-session`'s retirement; trace, spend, map reads, cadence,
the mirror and the browser row; and last `step —`, the only-driver switch and the unattended kit's dissolution.

The harness splits the 61 orders into six writer groups of consecutive orders; author every unit of your group, in
order, and nothing else. Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk
as soon as it is done.

| Order | Unit | Order | Unit | Order | Unit | Order | Unit |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 17 | 12 | 33 | 19 | 49 | 49 |
| 2 | 16 | 18 | 38 | 34 | 30 | 50 | 41 |
| 3 | 61 | 19 | 23 | 35 | 9 | 51 | 54 |
| 4 | 20 | 20 | 11 | 36 | 43 | 52 | 42 |
| 5 | 22 | 21 | 33 | 37 | 45 | 53 | 34 |
| 6 | 17 | 22 | 35 | 38 | 53 | 54 | 51 |
| 7 | 14 | 23 | 40 | 39 | 52 | 55 | 24 |
| 8 | 13 | 24 | 55 | 40 | 4 | 56 | 59 |
| 9 | 15 | 25 | 60 | 41 | 27 | 57 | 44 |
| 10 | 36 | 26 | 58 | 42 | 5 | 58 | 29 |
| 11 | 10 | 27 | 57 | 43 | 48 | 59 | 26 |
| 12 | 31 | 28 | 6 | 44 | 18 | 60 | 25 |
| 13 | 21 | 29 | 37 | 45 | 3 | 61 | 28 |
| 14 | 2 | 30 | 56 | 46 | 47 | | |
| 15 | 32 | 31 | 8 | 47 | 50 | | |
| 16 | 39 | 32 | 7 | 48 | 46 | | |

- **TOOL-dWellOiledMachine-1** — Items 1. I1, I2: the platform spike, the first artifact. A role-typed Workflow agent
  run inside a headless act session with the headless backend measured beside it; the hold case (the longest a
  PreToolUse entry holds a call on the pinned harness version, and what the harness does when the hold times out)
  recorded as I7's `hook-hold-seconds`; whether SubagentStop fires for a Workflow agent, an owner-stopped one, one
  failed by stalls and a killed session (the arming facts units 43 and 45 read); the result setting
  `runtime.spawn-backend`'s default for single-agent acts, read at each act's launch. Scout A row 1 (LR:1089-1100).
- **TOOL-dWellOiledMachine-16** — Items 16. I3: the journal grammar moved into the core and its retention by
  `runtime.journal`, the readers re-pointed. Owns the journal-readers point. Scout D row 3.
- **TOOL-dWellOiledMachine-61** — Items 61. I5, I6: the node profile at the node's home, read whole, an owner-only
  write through its guarded command, schema-validated at write and read, every red case the clause states. Scout D
  row 12.
- **TOOL-dWellOiledMachine-20** — Items 20. I4's `[[point]]` rows and the two tag namespaces registered as
  PLAY-dOrderedCharter-19/-10 register one, the hook extractor reading fragment names. Scout B row 7.
- **TOOL-dWellOiledMachine-22** — Items 22. Hook and point purposes reviewed, a purpose field per row
  (PLAY-dOrderedCharter-22 S1/S2) and the unnamed ones a shrink-only list through KICK-dKeptSession-19's
  `write_shrink_list`, its second instance. Scout B row 9.
- **TOOL-dWellOiledMachine-17** — Items 17. I4's `grant`, enforced on every adapter row at registration, and I12's
  value scan at every publishing boundary with its shape report under `runtime.secret-scan: value-gate+shape-report`,
  seen on a planted token shape. Scout D row 4.
- **TOOL-dWellOiledMachine-14** — Items 14. I7: harness adapters with capability tables, `runtime.harnesses`, the
  hard-coded `.claude/` install destinations read through the adapter. Scout B row 6.
- **TOOL-dWellOiledMachine-13** — Items 13. Host adapters (the OS scheduler first) registered under I4, and
  per-period cadence witnesses on `refs/gov/leases/run/<cadence>/<period>` (TOOL-dPlacedRequest-1, -18). Scout D row 1.
- **TOOL-dWellOiledMachine-15** — Items 15. I8: the node registry's runtime facts, the clock offset measured at each
  beat against the remote host's time read through unit 13's host adapter, correcting a holder's stamp where
  `leases.expiry-hours` is judged, both red cases. Scout D row 2.
- **TOOL-dWellOiledMachine-36** — Items 36. The harness conformance fixture over I2, its rows written to I7 and I8,
  read by `runtime.binary`, `runtime.owner-harness` and `runtime.act-harness`; scout A's note that the policy kit's
  live launcher passes a permission-bypass flag unit 37 will refuse. Scout A row 10.
- **TOOL-dWellOiledMachine-10** — Items 10. I9, I10: the kits' fragments as packs, one dispatcher entry per event,
  ask rules answered only by the PermissionRequest entry, `runtime.attended-judge`, `runtime.attended-allowance`,
  `runtime.hook-failure` with `onFailure` on every entry, each value on its planted case, the owner-pack table, signal
  traps on every git hook, the trusted hooks copy and lander hardening. Scout B row 4.
- **TOOL-dWellOiledMachine-31** — Items 31. I11 declared in the pack contract and checked at registration. Scout B
  row 15.
- **TOOL-dWellOiledMachine-21** — Items 21. Hook-message and harness-prompt templates as PLAY-dOrderedCharter-20 S7
  slot-line templates, the deny texts scout B lists moved into them. Scout B row 8.
- **TOOL-dWellOiledMachine-2** — Items 2. I13, I14: the `next` verb over the loop kit's position function, the check
  that every declared command ends with one or declares itself terminal, the laggard list draining to empty, the
  readers of `--plan` and `--status` re-pointed. Scout C row 1.
- **TOOL-dWellOiledMachine-32** — Items 32. I15: the act as the key, `session: pending`, a start event that never
  arrives failing the launch, `trace.identity`, `trace.cost`, the run log's closed-schema leg reading the same key.
  Scout A row 9.
- **TOOL-dWellOiledMachine-39** — Items 39. I16 and every reader's range `<current default>..HEAD` with `--no-merges`,
  `not-local` never passed, the two green cases and the red one. Scout A row 12.
- **TOOL-dWellOiledMachine-12** — Items 12. I17: sessions bound on every source (the `fork` matcher included), a
  resume that delivers no card diagnosed, the compact hook re-injecting the build card, the PreCompact flush and its
  keep-list, each compaction journaled through I3, the card's size check against the harness's measured
  re-attachment cap. Scout B row 5.
- **TOOL-dWellOiledMachine-38** — Items 38. The card's readers re-pointed to I17 with the four suites the clause names,
  the old path read for `install.deprecation-window` releases as an upgrade step. Scout B row 16.
- **TOOL-dWellOiledMachine-23** — Items 23. `memory.default-load` at startup, resume and compaction, ending with I13's
  line, the hook channel's cap measured with a 32 KiB map before the default is armed. Scout B row 10.
- **TOOL-dWellOiledMachine-11** — Items 11. I19, I20: workspaces by `build.worktree`, the commit queue, integration
  before release and the sweep. Scout C row 2.
- **TOOL-dWellOiledMachine-33** — Items 33. I18 written by the commit queue and the lander's four commit sites, the
  `prepare-commit-msg` filler, the `commit-msg` arm, every value of `trace.identity` with its red case, `salted`'s
  per-node salt in the credential store. Scout C row 3.
- **TOOL-dWellOiledMachine-35** — Items 35. The session node from I16 and I17, `runs-in` and `after`, acts and sessions
  as native-id classes (PLAY-dOrderedCharter-28 S2). Scout C row 5.
- **TOOL-dWellOiledMachine-40** — Items 40. Each role return committed at its item's witness and the branch pushed as
  `build.push` says; the verdict-file move is TOOL-dPlacedRequest-11 S4's, cited, never re-specced. Scout C row 6.
- **TOOL-dWellOiledMachine-55** — Items 55. The lease-store, doorbell and offer-source points as I4 rows, the git-refs
  adapter wrapping `write_gov_ref`, its conformance probes. Scout D row 10.
- **TOOL-dWellOiledMachine-60** — Items 60. The lander's push, the lease beat and the landed notice in one atomic push
  through TOOL-dPlacedRequest-15's fence, its three red cases. Scout C row 11.
- **TOOL-dWellOiledMachine-58** — Items 58. I32 and every admission and refusal the clause states, its limit stated
  openly. Scout C row 9.
- **TOOL-dWellOiledMachine-57** — Items 57. I12 over lease, mail, beat, mirror and request payloads and the door's
  token-shape refusal, the request record bound to its intake by the owner binding's proof. Scout D row 11.
- **TOOL-dWellOiledMachine-6** — Items 6. I21: `resume-tick.sh` grown, `run.host`, `runtime.relaunch` each value on a
  planted relaunch, `RESUME_ATTEMPTS`, the reconcile before the first beat, exactly one act session after a kill and
  restart. Scout A row 2.
- **TOOL-dWellOiledMachine-37** — Items 37. Preflight refusing a hook- or permission-skipping launch, the trusted-hook
  hash check, the launch-environment allowlist, the credential order and `runtime.secret-home: env-injected`, each
  class on a planted node, worktree pointers written relative. Scout A row 11.
- **TOOL-dWellOiledMachine-56** — Items 56. `runtime.act-harness` and `runtime.act-auth` per role through
  TOOL-dBoundRoles-21's resolver, the launch pinned out of bare mode. Scout A row 19.
- **TOOL-dWellOiledMachine-8** — Items 8. I25. Scout A row 4.
- **TOOL-dWellOiledMachine-7** — Items 7. Act binding and the epoch check at the Workflow, Agent and shell call in the
  dispatcher's PermissionRequest entry, in-script spawns declared and reconciled. Scout A row 3.
- **TOOL-dWellOiledMachine-19** — Items 19. I26, `roles.shape-enforce`, the journal reconciled against the shape and
  each non-review act's shape-run row (TOOL-dTotalRecall-11 §4). Scout A row 6.
- **TOOL-dWellOiledMachine-30** — Items 30. Experiment acts bound and journaled as shape-run rows, read at the
  experiment kind's harness. Scout A row 8.
- **TOOL-dWellOiledMachine-9** — Items 9. I22, the supervisor's reservations under `runtime.agents-in-flight`. Scout A
  row 5.
- **TOOL-dWellOiledMachine-43** — Items 43. The in-flight ledger pack at SubagentStart and SubagentStop over I22,
  armed by unit 1's facts, its split fallback, every seen and red case. Scout A row 13.
- **TOOL-dWellOiledMachine-45** — Items 45. I24, every seen and red case the clause states. Scout A row 14.
- **TOOL-dWellOiledMachine-53** — Items 53. I23 under `runtime.admission-scope`, shares and capacity from I6, every red
  case. Scout A row 15.
- **TOOL-dWellOiledMachine-52** — Items 52. The node beat's payload, stdlib-read load (settle scout D's Windows
  load-reading question as a FACT-QUESTION), never another project's names. Scout D row 9.
- **TOOL-dWellOiledMachine-4** — Items 4. I27, the prompt-submit pack. Scout B row 1.
- **TOOL-dWellOiledMachine-27** — Items 27. Intake from the mailbox and a cadence filer, origin marked, only owner
  origin ratifying, the interim roots TOOL-dTotalRecall-19 stands in drained. Scout B row 11.
- **TOOL-dWellOiledMachine-5** — Items 5. The re-pointed readers (TOOL-dPlacedRequest-4 S7, TOOL-dDeclaredLoop-19 S3),
  RC-9's fallback drained per harness by I7's `prompt-submit` row; only dRankedPlan's lands-second branch is a
  stand-in. Scout B row 3.
- **TOOL-dWellOiledMachine-48** — Items 48. I28 and every key and red case the clause states. Scout B row 19.
- **TOOL-dWellOiledMachine-18** — Items 18. I29, the release ceiling's arm left to dShippedRelease. Scout D row 5.
- **TOOL-dWellOiledMachine-3** — Items 3. Pause, resume, withdraw, supersede through the guarded command mapped onto
  today's verbs, the pause an I29 wait within `flow.wait-ceiling`, attend and unattend writing an `attendance override`
  scoped by `attendance.scope`, the mailbox copied before the ref is pruned. Scout B row 2.
- **TOOL-dWellOiledMachine-47** — Items 47. Every red case the clause states; the 115-wake loop replayed. Scout A row 16.
- **TOOL-dWellOiledMachine-50** — Items 50. The wait graph at half a wait's deadline, `deps.on-parent-withdrawn`.
  Scout D row 7.
- **TOOL-dWellOiledMachine-46** — Items 46. The progress ledger per I14 instance, the detectors journal-only until the
  replay. Scout A row 17.
- **TOOL-dWellOiledMachine-49** — Items 49. The refusal breaker reading I11. Scout A row 18.
- **TOOL-dWellOiledMachine-41** — Items 41. Unit offers under `build.unit-holders`; the widened `offer` value is an ask
  for dPlacedRequest (scout C). Scout C row 7.
- **TOOL-dWellOiledMachine-54** — Items 54. Discovery and the pure pick, the preset check widened. Scout C row 8.
- **TOOL-dWellOiledMachine-42** — Items 42. `gov-session` retired, every reader by value. Scout B row 17.
- **TOOL-dWellOiledMachine-34** — Items 34. `gov trace` and `gov why`, `build_run_model` re-pointed, the four-event
  fixture. Scout C row 4.
- **TOOL-dWellOiledMachine-51** — Items 51. Spend from `trace.cost` rows, `build.spend-cap` measured then set. Scout D
  row 8.
- **TOOL-dWellOiledMachine-24** — Items 24. Map reads outside a slice journaled; the `map` slot is dBoundRoles' work
  still unbuilt (scout D). Scout D row 6.
- **TOOL-dWellOiledMachine-59** — Items 59. A cadence run's own budget on its period lease. Scout C row 10.
- **TOOL-dWellOiledMachine-44** — Items 44. The memory-mirror point and its stand-in adapter, every verdict local.
  Scout B row 18.
- **TOOL-dWellOiledMachine-29** — Items 29. The measured `browser` row and the `visual.capture` command adapter,
  registered at unit 6's command-adapter point. Scout B row 14.
- **TOOL-dWellOiledMachine-26** — Items 26. I30, rendered from I13 and the item's declaration, armed by changing
  KICK-dKeptSession-17's `announce` stand-in. Scout B row 13.
- **TOOL-dWellOiledMachine-25** — Items 25. The supervisor the only driver, `/build` a client of `run` in the same
  unit. Scout A row 7.
- **TOOL-dWellOiledMachine-28** — Items 28. The unattended kit dissolved, every reader of each retired name
  inventoried; the owner ask PLAY-dClosedLoop-15 applies to its suites. Scout B row 12.
