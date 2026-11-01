**Serves:** research TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15

# Spec brief — dScopedBuild, the fifteen Build units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dScopedBuild/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys and Obligations sections bind every unit.
2. The build README, `memory/builds/dScopedBuild/README.md`: its build-level rules bind every spec, the fork rule
   above all. Its `BACKLOG.md` holds ask TOOL-dScopedBuild-16, which the LAST unit in build order (unit 13) names in
   its header's `closes`; every other unit's header says `advances TOOL-dScopedBuild-16`.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5, M12. Every unit is Tier 2: each is a new
   or changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every row of "Owned nodes", "Shared interfaces" and "Edges", and the scout
   record your units cite, all under `memory/builds/dScopedBuild/build/`:
   `2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md` (units 1, 6, 7, 14, 15),
   `2026-11-01-build-TOOL-dScopedBuild-3-reuse-scout-b.md` (3, 5, 8, 9),
   `2026-11-01-build-TOOL-dScopedBuild-2-reuse-scout-c.md` (2, 4, 13) and
   `2026-11-01-build-TOOL-dScopedBuild-10-reuse-scout-d.md` (10, 11, 12). Each holds a seam row per clause with
   path:line at `2bba66753`, and a section on where a record and source disagree. Those disagreements are findings
   you act on.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below), each named
`2026-10-*-build-PLAY-dClosedLoop-1-<name>.md`. The PRIMARY one is the Build item table in `B/…-flow-steps.md`
:284-300 (`build.base` to `build.resolve`, each item's actor, needs, proof and routes). Then architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id; `[policies]` :1292, :1297, :1298,
:1337, :1380-1383; `[owed]` :1984), `B/…-research-build.md` (the build-flow research, candidates A and B), the gap
register `B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` (each gap the packet's Gaps section names, by line),
`B/…-retrofit.md` `[drain]` :378-417 (units 8, 9), `B/…-walkthrough.md` :498-536 (walks B1, B3: units 3, 4),
`B/…-night-pass.md` (units 10, 11) and `B/…-night-pass-two.md` (units 6, 12, 13), `B/…-research-scoutedseam-apply.md`
(unit 12), `B/…-final-questions.md` FQ-3 (unit 14), and the fork rungs in
`B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 36-61 and 900-946. You never edit an instrument, v2,
the as-built view or the packet: the packet's Non-goals.

## Every spec, whatever its unit

- Path `memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-<n>.md`; H1
  `# TOOL-dScopedBuild-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order <k> ·
  advances TOOL-dScopedBuild-16`, with `<k>` your unit's order below (unit 13 writes `closes TOOL-dScopedBuild-16`
  in place of `advances`). `OPEN` is the status token: `DRAFT` is not in `STATUS_TOKENS`
  (`tools/memory-tree/tree_lib.py`). The shape is `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-1.md`
  line 3.
- Binding lines, each at column 0 on a line of its own under the status line:
  `**Carries:** <Items id>@<hash8> whole`, and for each node the owned-node table gives your unit,
  `**Carries:** node:<node>`. A unit carrying a clause in parts writes `part <k>/<n>` instead of `whole`, and every part
  is carried by a spec of this build: never split a clause without saying so in your return.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 1, 3, 5, 6, 7, 11, 13) still names its key words in backticks where they are code.
- Each clause's own "seen red on" and "each value seen on its planted case" cases are acceptance criteria, each
  observed RED on its planted case and green without it, by a probe or fixture of the unit's own code a pass can run.
  No criterion names the merge bar, a `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm
  goes on a `New arm:` line in §7, and the main loop observes it at the close. A policy key's non-default value is
  seen by a planted `.governance/policy.toml` naming that value, read through I4; each allowed value of a key your
  unit owns is a planted case.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `2bba66753`: verify each line number before citing it. Record each
  candidate you rejected and the test that rejected it (M12), under `### Alternatives rejected`.
- §8 forks: settle each by the README's rungs (the execution plan lines 36-61 and 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`, ON THE SAME LINE as the ruling; a `relaxes:` value joins
  a record with `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a
  choice the README's `may: PLAY-dClosedLoop-3` grant lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave
  an open question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/`, `memory/guides/*.md`, `memory/HYGIENE.md` and
  `memory/TEMPLATE-SPEC.md` from their kit templates, `tools/workflows/*.js` from their `.template.js`,
  `tools/gate-legs.json` from the kits' `[[gate_leg]]` declarations, the installed Skills under `.claude/skills/`
  from each kit's `SKILL.template.md`, and the installed kickoff skill from `skills/session-kickoff/`: name the source
  as the edit and the render as its copy.
- A parent's surface is specced and NOT built (next section). Cite the parent's spec by id and section as the
  interface and name the call you make; never re-spec it, never add a copy of it. Where your unit cannot run until it
  lands, say so in §2 as a build-run precondition, and where the clause names a stand-in, spec the stand-in and
  register it as a `[[stand-in]]` row (TOOL-dDeclaredLoop-13 S8).
- Each policy key this build owns already has its catalogue row in `tools/policy/catalogue.toml` (`deviation.gate`
  :950, `build.scope` :980, `build.reuse-check.second-pass` :986, `review.build.when` :1224, the four `retrofit.*`
  keys :1488-1509, owner dScopedBuild) and its name in `tools/policy/unsummarised-keys.txt`: the owner unit fills the
  row's missing summary and drains its name from that file, and never adds a second row. Its allowed values and
  default are that row's, verbatim. Once every unit of this build is terminal, the policy kit's reader-coverage arm
  reds any owned key no literal call reads, so the owner unit of each key names that literal reader in its acceptance.
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dScopedBuild/build/2026-11-01-build-TOOL-dScopedBuild-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- A parent spec, or a spec of another build, that must change for your clause to hold is never edited: state the
  needed change in §8 as an ask for that build, its target build, its accept line, and your return names it. The main
  loop files every such ask once, after the writers return, so no two writers mint an id in one foreign family
  (PLAY-dClosedLoop-32).
- Write nothing outside `memory/builds/dScopedBuild/spec/` and `memory/builds/dScopedBuild/build/`; temp files go
  under the scratch path your harness names.

### What the last spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename and keep its full path in §2, §4 and
  Files touched. A command that reads a file takes it as an argument rather than spelling it inside a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. Name the token exactly as "Shared interfaces" spells it, and the other writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours. The table under "Edges" is the set to declare;
  add an edge only when your spec truly reads or produces it, and say so in your return so the other writer adds the
  reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a file, a sentence a fixture asserts) owes a
  `**Readers:**` clause naming every reader by path and by value (hygiene check 25), each found by `git grep` over
  the tree. Check 25 reads any retirement word ("drops", "retired", "replaces") beside a backticked token in §2: use
  one only where you mean it. Units 2 (M8's in-place blocker fold), 6 (the per-pass checklist) and 14
  (`HOST_POLICY`) retire named things.
- **No link-shaped text**, a bracketed label followed by a parenthesised target, anywhere outside a real link,
  backticks included (hygiene check 2).
- **A §8 mark wraps whole.** `deviations.py` reads a `RESOLVED` mark's ruling, `widens:` and `relaxes:` from the mark
  itself: keep each mark one paragraph, with no list or blank line inside it, and `widens:` and `relaxes:` on one
  line.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- **A cited id leading a table cell defines it** (hygiene check 13): cite a foreign id inside prose, never as the
  first token of a table cell.
- **An acceptance criterion's ledger token** is written in backticks before the line first wraps (check 23).
- **Names you introduce** (a function, a module, a CLI mode, a conf block) are asked of the lexicon first:
  `python tools/lexicon/lexicon.py --suggest <name> --as <cell>`. A spec proposing a name the gate refuses hands the
  builder a red.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` and `carries.py --report dScopedBuild` after every writer returns.

## The parents are specced, not built

Every parent surface this build calls is specced and DEFERRED at HEAD; the scout records list each by spec id and
section. The ones the scouts named: dWitnessedBar — the seen-red line, its reader and `derive_owed_gates`
(TOOL-dWitnessedBar-7 S1-S4), the legacy ledger factory `tools/lib/legacy_ledger.py` (TOOL-dWitnessedBar-13 §4, S5),
the fix-pass red values `--fix-of leg:<name>|acceptance` (TOOL-dWitnessedBar-21 S3). dWellOiledMachine — the executor
`tools/runtime/supervise.py` and its `[[adapter]]` rows in `tools/runtime/points.toml` (TOOL-dWellOiledMachine-6 S1,
S8), the point registry (TOOL-dWellOiledMachine-20 S4). dFurnishedOrders — the retired dispatch keys and their witness
(TOOL-dFurnishedOrders-4 S5, -25, -30 S1), the legacy slot `render_legacy_slot` and the `not-installed: <why>`
spelling (TOOL-dFurnishedOrders-11 S3, §4). dIndexedDesign — the playbook set identity (TOOL-dIndexedDesign-10 S2,
-11 S1), the reuse-scout seam rows `seam-<n>` and `read_reuse_scouts` (TOOL-dIndexedDesign-13 S3, S6), the derived
ready state (TOOL-dIndexedDesign-16 S6). Grandparents and others, DEFERRED too: dDeclaredLoop (`review.findings`
TOOL-dDeclaredLoop-20 S4; the `upstream` rows and `join_upstream` TOOL-dDeclaredLoop-29 S3-S8; rework draws
TOOL-dDeclaredLoop-30 S3, S6; `derive_position` TOOL-dDeclaredLoop-7 S1), dPlacedRequest (`probe.py trigger` and
`pin`, TOOL-dPlacedRequest-7 S3-S6; the `kit-dirs` overlap reducer TOOL-dPlacedRequest-1 S9), dOrderedCharter (a
leg is core when its `enforces` is non-empty, PLAY-dOrderedCharter-7 S2, S9; the move of `drop_touched_exemptions`
to `tools/lib/coverage_join.py`, PLAY-dOrderedCharter-19 S9), dBoundRoles (`checkShellWrites`,
TOOL-dBoundRoles-7 S1, S3, S5), dTotalRecall (the code record `code_record.py`, TOOL-dTotalRecall-8 S2, S7),
dFairHearing (the scouted-seam bench instance, TOOL-dFairHearing-12 S4, -14). None of their files exists at HEAD.
dOrderedCharter, dBoundRoles, dTotalRecall, dPlacedRequest and dFairHearing are not this build's parents: where your
unit needs one of them, say so in §8 and route it as the rungs say (a build-run precondition, an ask, or a stand-in),
never by assuming it lands first.

Landed and readable now: dTrueNorth's `tools/memory-tree/deviation_join.py` (the join, `check_material`,
`read_first_passes`, `read_decision_ref`, `render_lines`), `tools/memory-tree/design_lib.py` (`read_spec_writes`,
`check_guard_trips`, `check_writes_intersect`) and `tools/check-spec-tokens.py`; `tools/memory-tree/routed_commits.py`
(the push-time leg NP-22 merged into `build.scope`, `night-pass.md:687`); dGroundRules' `tools/policy/` (`policy.py
get`, `catalogue.toml`, `policy-mirror.js` and `policy-shim.sh`); `tools/lib/compare_base.py`; the unattended driver
`tools/unattended/unattended.sh` (`--close`'s DoD arms, `--dispatch`, `--check-commit`, `--review`, `--record-piece`,
`--propose`, `derive_ask_seq`, `write_ask_rows`); `tools/run-gates/` (the attribution row); `tools/hooks/scratch-guard.js`;
`tools/codebase-map/` (`map_lib.drop_touched_exemptions`, `map_diff._drop_affordance_exempt`); `tools/workflows/`.

Where a scout found that a design record, a parent spec or source disagree, v2's clause governs; a parent spec it
contradicts gets an ask (the rule above), never an edit. Where the clause itself names something source shows wrong
(a function that is not where the clause puts it, a reader that does not read), the spec says what source shows,
carries the clause's intent, and writes a deviation record naming the difference.

## Owned nodes

| Node | Unit |
|---|---|
| `item.build.base` | 1 |
| `item.build.exit` | 1 |
| `policy-key.deviation.gate` | 14 |
| `item.build.scope` | 3 |
| `record-kind.scope` | 3 |
| `policy-key.build.scope` | 3 |
| `item.build.revert-pass` | 3 |
| `item.build.resolve` | 3 |
| `item.build.unit-pass` | 8 |
| `policy-key.retrofit.drain` | 8 |
| `policy-key.retrofit.drain-cap` | 8 |
| `policy-key.retrofit.claim-on-touch` | 8 |
| `policy-key.retrofit.claim-cap` | 8 |
| `item.build.unit-lease` | 5 |
| `item.build.core` | 7 |
| `record-kind.core-result` | 7 |
| `item.build.distill` | 7 |
| `item.build.acceptance` | 15 |
| `item.build.fix-pass` | 15 |
| `item.build.reuse-check` | 12 |
| `policy-key.build.reuse-check.second-pass` | 12 |
| `policy-key.review.build.when` | 4 |
| `item.build.ratify` | 4 |

Units 2, 6, 9, 10, 11 and 13 own no node; each still names the nodes it reads, in prose. A unit carrying an item no
clause of this row spells beyond its name (`item.build.revert-pass`, `item.build.resolve`, `item.build.unit-lease`,
`item.build.distill`, `item.build.ratify`) specs the item as `flow-steps.md` :284-300 states it, at the size that item
needs, and keeps it inside the unit's one mechanism: revert-pass and resolve are the refused-stray and conflict routes
of the write set unit 3 grades; unit-lease is the write set unit 5's gate reads; distill writes the decision-log rows
unit 7's core run covers; ratify is the owner's ruling the closing review's disposal precedes. Where an item cannot
be built without a parent this build does not have, spec its stand-in and say so.

## Shared interfaces — one spelling for every writer

Fixed so fifteen specs by five writers agree on the interface axis (M2). Each row names its owner, the unit whose spec
defines it; every other unit names it exactly as spelled here and cites the owner. A spelling marked "proposed" has
no source yet; the owner may refine it in its spec, and says so in its return. A writer who finds one wrong says so in
its return and writes a deviation record rather than a second spelling. Every new name is asked of `--suggest` first.

| # | Interface | Spelling | Owner | Source |
|---|---|---|---|---|
| I1 | The history-derived base | `read_first_passes` moved from `deviation_join.py:325` into `tools/memory-tree/routed_commits.py` beside `read_routed_commits`, `deviation_join.py` importing it; a CLI `routed_commits.py --build-base <slug>` printing the parent of the oldest first pass. It decides WHICH commits are the build's; whose red it is stays the bar's attribution base R, the advertised tip (`run-gates.sh:4349-4353`): never one base for both (proposed) | 1 | scout A interface 1, disagreement 1 |
| I2 | The both-mode exit | one exit contract both modes run: a driver verb `unattended.sh --build-exit <slug>` the attended `/build` Skill's last stage (`tools/roles/SKILL.template.md`) and `--close` both call, refusing while a red the build's own commits introduced stands on a core leg; the existing `gates-green` arm and `read_gates_record` are its unattended half, never a second reader (proposed) | 1 | scout A row 1, interface 2 |
| I3 | Whose red | the bar's `attribution` TSV row, read only through `read_gates_record` (`unattended.sh:9617`); a new column goes before `reason` | 1 | scout A interface 2 |
| I4 | The policy read | `python tools/policy/policy.py get <key> [--rev <R>]` by subprocess (`policy.py:1332`), key a string literal at every call site; keys and values verbatim from `catalogue.toml` | 14 | scout A interface 4; scout B interface 2 |
| I5 | The three outcomes | `refuse`, `warn-and-ask`, `report`, rendered by one function both `deviation.gate` and `build.scope` call, its ask written through `derive_ask_seq` and `write_ask_rows` (`unattended.sh:9780`, `:9984`) as `write_inherited_asks` (`:10020`) does, never a new ask writer (proposed: the renderer lives in `routed_commits.py`) | 14 | scout A interface 5; scout D ask filing |
| I6 | The `build.scope` host | `tools/memory-tree/routed_commits.py`, arms after `check_deviation_join` (`:334`), output lines prefixed `routed-commits: scope` and `routed-commits: touch` beside `routed-commits: deviation`; the deviation gate and `build.scope` both read at the push range and at the Build exit through this one host | 3 | scout B interface 1; NP-22 |
| I7 | The unit's write set | attended: `design_lib.read_spec_writes` filtered by `check_dir_shaped`; dispatched: the `--dispatch --writes` rows; matched only through `check_guard_trips` / `check_writes_intersect` (`design_lib.py:589`, `:601`), never a third matcher | 3 | scout B interface 3 |
| I8 | The unit's own commits | `routed_commits.extract_unit_ids` over subject plus `Pass:` trailer, the union rule (`routed_commits.py:119`), non-merges only, within I1's base | 3 | scout B interface 4, disagreement 6 |
| I9 | The hunk set | one pure reader `read_touched_hunks(repo, shas)` returning `{path: [(start, count)]}` over `git diff-tree -U0 --no-merges -M -r -p <sha>`, renames re-keyed as `carry_renames` does (TOOL-dWitnessedBar-13 S5) (proposed) | 9 | scout B interface 5 |
| I10 | The touch-drop | `drop_touched_exemptions(exempt, touched)`, imported from `map_lib` until PLAY-dOrderedCharter-19 S9 moves it to `tools/lib`; the writer `_drop_affordance_exempt` (`map_diff.py:107-125`) behind a point row in `tools/runtime/points.toml`; the claim arm prints `not-installed: <why>` where the map is absent (no `.codebase-map.conf`) | 9 | scout B interfaces 6, 7 |
| I11 | The commit-time host | one `deviation_join.py --staged` verb called from a new hygiene check that passes `--staged` through as checks 29 and 30 do (`check-memory-hygiene.sh:1802`, `:1843`), run by `.githooks/pre-commit`'s existing `memory/**` call; it holds the `deviation.gate` arm (unit 14) and the frozen-spec arm (unit 2); the check number is the next one no tracked spec claims, found by grepping `memory/builds/*/spec/` (proposed) | 14 | scout C interface 3 |
| I12 | The landed predicate | `read_landed_units(root, units)` in `deviation_join.py`, each spec's header read at `read_decision_ref(root)` (`:676`), CLOSED there meaning landed; HEAD's header is not enough, because the harness writes CLOSED on the run branch (proposed) | 2 | scout C interface 2, disagreement 1 |
| I13 | The closing-review predicate | `check_closing_review_recorded <slug> <when>`, lifted out of the `closing-review-recorded` arm (`unattended.sh:11767`) and called from I2; subjects `<slug>` per-build, `<slug>:<unit id>` per-unit, `<slug>@<landing sha7>` per-landing, read the same way by `review_last_reason` (`:12630`) (proposed) | 4 | scout C interfaces 5, 6 |
| I14 | The rows a closing review is handed | `upstream: [{id, kind, text}]` on `tier2-review.template.js` beside `priorFindings`, joined into its input print; answers a required `upstream` array on `FINDING_SCHEMA`; row lines `- <row id> · <kind> · <text>`, answers `- <row id> · used|bypassed|not-applicable · <reason>` (TOOL-dDeclaredLoop-29 S3, S5); criterion rows `criterion-<unit id>-AC<n>`, seam rows `seam-<n>` (proposed) | 13 | scout C interfaces 7, 10, 11 |
| I15 | The MUST-seam reader | `read_spec_musts(spec_text)`, reading the `- seam-<n> · seam · <path> :: <symbol>` lines a spec's §10 carries, filtered to `binding` MUST (TOOL-dIndexedDesign-13 S3, S6); one reader unit 12 and unit 13 share (proposed) | 12 | scout C interface 8; scout D disagreement 4 |
| I16 | The reuse-check rows and record | verdicts `duplicate`, `should-extend`, `new`, `not-a-unit` (each with its nearest symbol or what was searched), MUST answers `used`, `bypassed`, `not-applicable`, the fix-pass reply `disputed`; `UNIT_CAP = 60`, the overflow and no-stop sentences ported from aScoutedSeam's instrument; the record `memory/builds/<slug>/build/<date>-build-<unit id>-reuse-check-<n>.md` with `**Serves:** reuse-check <unit id>` (proposed) | 12 | scout D row vocabulary, literals, record |
| I17 | The fix-pass reds | `--fix-of acceptance` (TOOL-dWitnessedBar-21 S3) beside a new `--fix-of reuse-check`; the fix pass's allowance is the unit's write set less the red check's own files (`flow-steps.md` `build.fix-pass` row) (proposed) | 15 | scout D fix-pass red |
| I18 | Core legs | a manifest row with a non-empty `enforces` (PLAY-dOrderedCharter-7 S2); no `core` tag or chunk is invented; until it lands, the core set is `not-installed` and the exit says so | 7 | scout A interface 3 |
| I19 | The seen-red line | ``- seen-red — `<leg>` — red `<sha>` — green `<sha>` — <break>`` under `**Evidences:** <unit>` (TOOL-dWitnessedBar-7 S1), owed set `derive_owed_gates(root, slug, base)` (S4), the base I1's | 15 | scout A interface 7 |
| I20 | Ask filing | every unit that files an ask (a proposal to amend a playbook, open reuse rows past `flow.route-backs`, a `warn-and-ask` outcome) goes through `derive_ask_seq` and `write_ask_rows`; no new ask writer | 11 | scout D ask filing |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 1 → 3, 7, 15 | `read_first_passes` |
| 1 → 7, 4 | `--build-exit` |
| 14 → 2 | `--staged` |
| 14 → 3 | `policy.py get` |
| 3 → 9, 5 | `read_spec_writes` |
| 9 → 8 | `read_touched_hunks` |
| 15 → 12 | `--fix-of` |
| 11 → 12 | `write_ask_rows` |
| 12 → 13 | `read_spec_musts` |
| 4 → 13 | `check_closing_review_recorded` |

## The units

**Writer groups and build order.** The `order` value is the build order: the base and the exit first, because the
range every later check grades and the host every later exit check runs in come from it; the deviation gate, whose
commit-time host the frozen-spec arm joins; the freeze; the scope at the push, which creates the `build.scope` host;
the touch join, which becomes its one check, and the drain and claim it grades; the write gate, whose backstop is the
push-time arm; the checklist's retirement witness; the core checks at the exit; acceptance and its seen-red record,
which own the fix pass; the playbook pieces and the ask route; the reproduction; the reuse check, which reads the fix
pass, the ask route and the MUST seams; the closing review recorded under `review.build.when`; and the closing review
handed its rows last, because it reads both. The harness splits the 15 orders into five writer groups of consecutive
orders; author every unit of your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 1 (1), 14 (2), 2 (3) |
| 2 | 3 (4), 9 (5), 8 (6) |
| 3 | 5 (7), 6 (8), 7 (9) |
| 4 | 15 (10), 11 (11), 10 (12) |
| 5 | 12 (13), 4 (14), 13 (15) |

Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **TOOL-dScopedBuild-1** — Items 1 (gap-spine-03). I1, I2, I3. One exit contract both modes run, its base derived
  from history (the parent of the build's oldest first pass) for WHICH commits are the build's, and the bar's
  attribution base for WHOSE red; the exit refused while a red the build's own commits introduced stands. The
  unattended half is the `gates-green` arm (`unattended.sh:11098`, `:11121`, `read_gates_record` `:9617-9651`); the
  attended half is the `/build` Skill's last stage, which today runs a bare bar. Core legs (I18) are unit 7's; until
  they exist, say which reds the exit refuses. Seen red: a planted build whose own commit reds a leg, refused at the
  exit in both modes; a planted inherited red, not refused.
- **TOOL-dScopedBuild-14** — Items 14. I4, I5, I11. `deviation_join.py`'s `POLICIES` (`:142`) gains `warn-and-ask`
  and `HOST_POLICY` (`:144`) becomes the `deviation.gate` value, read at the commit (I11, new) and at the Build exit
  (I6, I2: the join has no exit host today, scout A disagreement 2). Fork: the catalogue default `refuse` would flip
  gov's own pre-push; settle whether gov's `.governance/policy.toml` declares a value, by the rungs, and record it.
  Seen red: each of the three values on a planted unrecorded deviation, at the commit and at the exit.
- **TOOL-dScopedBuild-2** — Items 2 (gap-flow-05). I12, reads I11. A revision of a spec whose unit has landed
  refused at the commit, with or without a deviation record, through `check_material` (`deviation_join.py:436`, the
  status-only predicate) and I12; and every closing-review finding disposed as new units by `review.findings`
  (TOOL-dDeclaredLoop-20 S4, cite it), so M8's in-place blocker fold (`BUILD-METHOD.template.md:274`) and the
  attended Skill's Stage 6 stop prescribing it. Say in §2 that the motivating case (a fold before landing,
  dSweptBranches rev-3) is caught by the disposal half and unit 14, not by the freeze (scout C disagreement 2).
  Seen red: a planted in-place edit of a landed unit's spec, refused with and without a deviation record; green on a
  status-only edit.
- **TOOL-dScopedBuild-3** — Items 3 (gap-build-01). I6, I7, I8, I5. A scope arm in `routed_commits.py` beside
  `check_deviation_join`: each pushed commit's paths inside its named unit's write set, at the push for attended and
  unattended alike, graded by `build.scope`; kit-directory granularity (research-build.md: file granularity 20.5% red
  loses, kit 7.2% survives) with the `kit-dirs` reducer cited, never a third; the scope report as
  `record-kind.scope`; a refused stray routed to `build.revert-pass`; `build.resolve`'s allowance the units' write
  sets. Seen red: each of the three values on a planted stray commit; green on an in-scope one.
- **TOOL-dScopedBuild-9** — Items 9 (gap-mem-23). I9, I10, reads I6, I8. The touch join as `build.scope`'s one
  check, graded by its value, over the union of `git diff-tree -U0 --no-merges -M` across the unit's own commits
  (never `--first-parent`), calling the pure `drop_touched_exemptions` (I10: it is in `map_lib.py:1373` at HEAD, not
  `tools/lib`; a deviation or a `**Moved:**` line, scout B disagreement 1), the writer behind a point, the claim arm
  `not-installed` where the map is absent. gov's grace list is empty, so every red case is planted. Seen red: a
  planted core-only tree (H5), and a planted touched exemption dropped.
- **TOOL-dScopedBuild-8** — Items 8 (gap-build-05). Reads I9, I10. `build.unit-pass` and `build.scope` draining the
  legacy a unit touches as `retrofit.drain` says (`hunk`, `file`, `off`) under `retrofit.drain-cap`, and claiming the
  baselined map keys its write set holds under `retrofit.claim-cap`, carrying them with an ask, or neither, as
  `retrofit.claim-on-touch` says; the ledger is TOOL-dWitnessedBar-13's; no key-to-path deriver exists
  (`KEYED_ATTRIBUTORS = ()`, scout B row 8), so spec it or its stand-in. Seen red: each value of each of the four keys
  on a planted unit.
- **TOOL-dScopedBuild-5** — Items 5 (gap-build-03). Reads I7. The write gate (`checkBuildable`,
  `scratch-guard.js:873`, inside `checkRouted` `:1113`) reading derived state, witnesses only, instead of a typed
  status, through a Python reader behind a shim as `policy-mirror.js` reaches `policy-shim.sh`; Bash and PowerShell
  writes through TOOL-dBoundRoles-7's `checkShellWrites` (not a parent: route it), the main loop's shell writes
  backstopped by unit 3's push arm; the lease's write set as `item.build.unit-lease`. Seen red: a planted typed
  status that would admit a write the derived state refuses; a planted Bash write to a routed path.
- **TOOL-dScopedBuild-6** — Items 6 (gap-build-04). The per-pass checklist's retirement witnessed at Build: a
  planted pass that calls the lookup by a write set's paths reds. The retirement itself is TOOL-dFurnishedOrders-4
  S5 and -30 S1, the witness verb -25: cite them, do not re-spec them; this unit adds the planted pass Build reads,
  and the M6 sentence (`BUILD-METHOD.template.md:187-190`) that still owes the checklist. gap-build-04's second half
  (uncounted harness agents) is not in the clause: say so. Seen red: the planted pass.
- **TOOL-dScopedBuild-7** — Items 7. I18, reads I1, I2. The core checks run by the executor
  (TOOL-dWellOiledMachine-6 S1, S8, an `idempotent` adapter row) over the build's range at Build's exit, the
  executor-written result as `record-kind.core-result`, an own red routed to a fix unit through Design or excepted
  under `core.exceptions`; a core-only run is a separate call, because `--close` scrubs `GATE_LEGS` from its bar.
  `build.distill`'s decision-log rows are in the range. Seen red: a planted own red on a core leg; a planted
  excepted one.
- **TOOL-dScopedBuild-15** — Items 15 (gap-test-06). I17, I19, reads I1. `build.acceptance` writing the seen-red
  record: the executor re-running each new or changed gate's planted red beside the unit's acceptance commands, one
  record per gate keyed by leg and red SHA, which dWitnessedBar's `test.seen-red` reads; a planted red that stays
  green failing the acceptance and routing to `build.fix-pass`. A leg at a SHA runs through the bar's runner, never by
  sourcing `lib-attribute.sh` from another kit. An attended build has no `RUN.md`, so its base is I1's. Seen red: a
  planted gate whose red never ran.
- **TOOL-dScopedBuild-11** — Items 11. I20. A playbook's pieces built as units, the piece record gaining a `unit:`
  field (`record_piece`, `unattended.sh:13115`) joined to the unit's build commit by hash (`build_commit`,
  `lib-unattended.sh:1186`), the set identity TOOL-dIndexedDesign-11 S1's; `--propose` (`verb_propose` `:12940`)
  filing an ask through I20 instead of a RUN.md park row. Seen red: a planted piece whose hash matches no unit's build
  commit; a proposal filed as an ask.
- **TOOL-dScopedBuild-10** — Items 10. A `reproduction` probe (TOOL-dPlacedRequest-7 S3, S4, not a parent: route it)
  fired before a patch build's first `build.unit-pass` when the build comes from a bug report; no parent marks a
  patch's origin, so the predicate is this unit's, its fork settled by the rungs (scout D row 10). Seen red: a
  planted patch build from a bug report reaching its first pass with no reproduction.
- **TOOL-dScopedBuild-12** — Items 12 (gap-build-06, `[owed]` v2:1984). I15, I16, reads I17, I20. `build.reuse-check`
  per unit before the closing review, at medium (`tools/roles/house/policy.toml`), the lister ported from
  aScoutedSeam's T1 (`extract_units`, `UNIT_CAP`, the overflow and no-stop sentences) over the code record or its
  stand-in `memory/map/generated/symbols.json` (the clause's record is TOOL-dTotalRecall-8's, absent; scout D
  disagreements 1, 2), MUST rows through I15, `duplicate` or `bypassed` routing to a fix pass, the second pass under
  `build.reuse-check.second-pass`, disputed rows to the closing review, re-entries bounded by `flow.route-backs`. Its
  acceptance is the reproduction of aScoutedSeam's figures on its 23 tuning and 12 held-out cases (29 of 35 with the
  card, 31 of 35 for the system, parsed replies first); the host trees live only on node d (scout D disagreement 6),
  so say where it runs. Seen red: a planted false `duplicate`; sixty-one added units whose last is a duplicate.
- **TOOL-dScopedBuild-4** — Items 4 (gap-build-02). I13, reads I2. The closing review recorded, as
  `review.build.when` says, per build, per unit or per landing, for attended builds as for unattended, through I13
  inside I2's exit; `verb_review` today reads every non-slug subject as a spec audit (`unattended.sh:12694`), so the
  per-unit subject is new; `build.ratify` follows the review's disposal. Seen red: each value on its planted case.
- **TOOL-dScopedBuild-13** — Items 13 (gap-flow-22). I14, reads I13, I15. The closing review handed, beside its
  range, each unit's acceptance criteria (`extract_acceptance`, `check-spec-tokens.py:539`) and the MUST seams its
  spec carried as rows each finder answers, recorded in TOOL-dDeclaredLoop-29 S8's record, gating once a measurement
  passes (gate `record` until a `measured-by` record exists). Closes TOOL-dScopedBuild-16. Seen red: a planted finder
  return that leaves a handed row unanswered.
