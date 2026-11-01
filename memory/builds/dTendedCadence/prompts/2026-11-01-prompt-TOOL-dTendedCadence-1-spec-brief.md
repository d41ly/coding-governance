**Serves:** research TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18

# Spec brief — dTendedCadence, the eighteen Maintain units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dTendedCadence/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys and Obligations sections bind every unit.
2. The build README, `memory/builds/dTendedCadence/README.md`: its build-level rules bind every spec, the fork rule
   above all. Its `BACKLOG.md` holds asks TOOL-dTendedCadence-19 (the build itself) and -20 (`defer dormant`).
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5, M12. Every unit is Tier 2: each is a new
   or changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every row of "Shared interfaces" and "Edges", and the scout record your units
   cite: `memory/builds/dTendedCadence/build/2026-11-01-build-TOOL-dTendedCadence-1-reuse-scout-a.md` (units 1, 2, 3,
   6, 8, 10), `-4-reuse-scout-b.md` (4, 14, 15, 16), `-5-reuse-scout-c.md` (5, 7, 12, 17, 18) and `-9-reuse-scout-d.md`
   (9, 11, 13). Each holds a seam row per clause with path:line at `e90cf41b3`, a section on where a record and source
   disagree, and the forks the scout left open. Those disagreements and forks are yours to act on.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below). The PRIMARY one is
the expansions review `B/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`: the observability layer and its
Maintain items `:170-290` (item table `:218-235`, readings `:189-216`, the run record `:251-253`), the currency-leg
rule `:463-467`, and the gap rows `:490-510`. Then architecture v2 `B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
(grep your clause id; `[policies]` `:1319-1333`, `:1389`; presets `:1636-1647`, `:1709`; `[owed]` `:1970`, `:1990`),
`B/2026-10-14-build-PLAY-dClosedLoop-1-research-maintain.md`, the night pass `B/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`
and its instruments (units 11, 12, 13, 14), `B/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md` `:355-380` (unit
16), the retrofit record `B/*retrofit.md` `:487-584` (unit 9), the gap register (each gap the packet names, by line),
and the fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 36-61 and 900-946. You never
edit an instrument, v2, the as-built view or the packet: the packet's Non-goals.

## Every spec, whatever its unit

- Path `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-<n>.md`; H1
  `# TOOL-dTendedCadence-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order <k> ·
  advances TOOL-dTendedCadence-19`, with `<k>` your unit's order below. Unit 2 (order 18, the last) writes
  `closes TOOL-dTendedCadence-19` in place of `advances`; unit 3 also writes `closes TOOL-dTendedCadence-20`, in the
  verb grammar `memory/TEMPLATE-SPEC.md` states for a header naming two asks. `OPEN` is the status token: `DRAFT` is
  not in `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py`). The shape is
  `memory/builds/dMindYourWords/spec/2026-10-29-spec-TOOL-dMindYourWords-1.md` line 3.
- Binding lines, each at column 0 on a line of its own under the status line: `**Carries:** <Items id>@<hash8> whole`,
  and for each node the owned-node table gives your unit, `**Carries:** node:<node>`. A unit carrying a clause in parts
  writes `part <k>/<n>` instead of `whole`, and every part is carried by a spec of this build: never split a clause
  without saying so in your return.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 1, 3, 5, 8, 10, 12) still names its key words in backticks where they are code.
- Each clause's own "seen" cases are acceptance criteria, each observed RED on its planted case and green without it,
  by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a `GATE_*=` prefix,
  a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and the main loop
  observes it at the close. A policy key's non-default value is seen by a planted `.governance/policy.toml` naming
  that value, read through I2; each allowed value of a key your unit owns is a planted case.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The scouts found the lookup answers name stems only here: say so where it does. The seams in the scout records are
  a reading at `e90cf41b3`: verify each line number before citing it. Record each candidate you rejected and the test
  that rejected it (M12), under `### Alternatives rejected`.
- §8 forks: settle each by the README's rungs (the execution plan lines 36-61 and 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`, ON THE SAME LINE as the ruling; a `relaxes:` value joins
  a record with `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a
  choice the README's `may: PLAY-dClosedLoop-3` grant lifted carries `grants: PLAY-dClosedLoop-3 <change>`. The grant
  covers the governance-carrier and public-surface changes this build's own clauses name, nothing else. Never leave
  an open question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/` and `tools/roles/house/`, `memory/guides/*.md`,
  `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md` from their kit templates, `tools/workflows/*.js` from their
  `.template.js`, `tools/gate-legs.json` from the kits' `[[gate_leg]]` declarations, `drift_signals.py` from
  `drift_signals.template.py`, and the installed Skills under `.claude/skills/` from each kit's `SKILL.template.md`:
  name the source as the edit and the render as its copy.
- A parent's surface is specced and NOT built (next section). Cite the parent's spec by id and section as the
  interface and name the call you make; never re-spec it, never add a copy of it. Where your unit cannot run until it
  lands, say so in §2 as a build-run precondition, and where the clause names a stand-in, spec the stand-in and
  register it as a `[[stand-in]]` row (TOOL-dDeclaredLoop-13 S8).
- Each policy key this build owns already has its catalogue row in `tools/policy/catalogue.toml` (`:1114-1199` and
  `:1542-1546`, owner dTendedCadence) and its name in `tools/policy/unsummarised-keys.txt` (`:111-123`, `:144`,
  `:170`): the owner unit fills the row's missing summary and drains its name from that file, and never adds a second
  row. Its allowed values and default are that row's, verbatim. Once every unit is terminal, the policy kit's
  reader-coverage arm reds any owned key no literal call reads, so each key's owner unit names that literal reader in
  its acceptance.
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dTendedCadence/build/2026-11-01-build-TOOL-dTendedCadence-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- A parent spec, or a spec of another build, that must change for your clause to hold is never edited: state the
  needed change in §8 as an ask for that build, its target build, its accept line, and your return names it. The main
  loop files every such ask once, after the writers return, so no two writers mint an id in one foreign family
  (PLAY-dClosedLoop-32). "Asks already known" below lists the ones the scouts found: cite the letter, do not restate.
- Write nothing outside `memory/builds/dTendedCadence/spec/` and `memory/builds/dTendedCadence/build/`; temp files go
  under the scratch path your harness names.

### What the last spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python maintain.py …`) and keep its
  full path in §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it
  inside a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. When you hand off to a unit another writer owns, name the token exactly as "Shared interfaces" spells
  it, and that writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours. The table under "Edges" is the set to declare; add
  an edge only when your spec truly reads or produces it, and say so in your return so the other writer adds the
  reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a constant, a file, a sentence a fixture asserts) owes a
  `**Readers:**` clause naming every reader by path and by value (hygiene check 25), each found by `git grep` over
  the tree. Check 25 reads any retirement word ("drops", "retired", "replaces") beside a backticked token in §2: use
  one only where you mean it. Units 7, 15 and 18 retire or move named things (`DEFAULT_DEAD_READINGS_LIMIT`,
  `DEAD_FILED`, the five signals' `drift-audit records` gating, `signal_dangling_pointers`' report-only path).
- **No link-shaped text**, a bracketed label followed by a parenthesised target, anywhere outside a real link,
  backticks included (hygiene check 2).
- **A §8 mark wraps whole.** `deviations.py` reads a `RESOLVED` mark's ruling, `widens:` and `relaxes:` from the mark
  itself: keep each mark one paragraph, with no list or blank line inside it, and `widens:` and `relaxes:` on one
  line.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- **A cited id leading a table cell defines it** (hygiene check 13): cite a foreign id inside prose, never as the
  first token of a table cell.
- **An acceptance criterion's ledger token** is written in backticks before the line first wraps (check 23).
- **Names you introduce** (a function, a module, a CLI mode, a conf block, a row kind) are asked of the lexicon first:
  `python tools/lexicon/lexicon.py --suggest <name> --as <cell>`. A spec proposing a name the gate refuses hands the
  builder a red. The proposed spellings below were not asked: ask before you write them.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` and `carries.py --report dTendedCadence` after every writer returns.

## The parents are specced, not built

At HEAD there is no `tools/runtime/`, no `tools/loop/`, no `tools/run-gates/leg_factory.py`, no
`tools/lib/legacy_ledger.py`, no `tools/playbook/layers.toml`, no `tools/memory-tree/code_record.py` or
`annotations.py`, and no `tools/lib/python_floor.py`. Every parent surface below is a spec id and section, DEFERRED:

- dWellOiledMachine (Runtime): the cadence row at `point.cadence-items`, `check_cadence_row` and `cadence.py tick`
  (TOOL-dWellOiledMachine-59 S1-S3); hosts and `hosts.py ready`, the period lease `run_cadence_period` and
  `derive_period` (-13 S1-S6); event wake (-18 S1-S3); `intake.py file --origin cadence --filer <tag>` (-27 S1-S4);
  journal readers at `point.journal-readers` (-16 S7); `launch_act` (-1 S2, S3); the act ceiling journal lines (-47
  S4); the commit reading handed to this build (-39 :106-121, rules -33 S7); notification adapters and
  `secret_scan.py payload adapter` (-48 S7).
- dDeclaredLoop (Flow): the `[[item]]` row schema and `check_program` (TOOL-dDeclaredLoop-12 S1, S3, S5),
  `loop_items.py new` (-24 S6), `[[stand-in]]` rows (-13 S8).
- dPlacedRequest: `probe.py trigger` (TOOL-dPlacedRequest-7 S3), the `patch` and `repeat` facts and `entry.place`
  (-4 §4), `entry.claim` and the derived README (-21 S2-S7), `check_cadence_segment` (-18 S1), the lease ref grammar
  (-1 S1).
- dRankedPlan: `triage.py pass` (TOOL-dRankedPlan-3 S2); `gen_build_index.py --dormant` and `loop_transition.py
  dispose` (-4 S2-S5), which ask TOOL-dTendedCadence-20 binds.
- dWitnessedBar: the leg factory `leg_factory.py new` and `[[gate_leg]]` rows (TOOL-dWitnessedBar-11 S1-S3, S8), the
  keyed ledger population factory and `seed_population` (-13, -15 S1), `drift-pins.txt` (-16 S8, table :191), the
  slot line `slot point.flow.leg-pack · filled` (-28 S10).
- dBoundRoles: `layers.toml` rows, `roles = [...]` and `check_layer_roles` (TOOL-dBoundRoles-1 S1, S5, §4 :177-192).
- dOrderedCharter: optional slots and their `not-installed` fallback (PLAY-dOrderedCharter-16 S2, -17 S9),
  `point.runtime.reading` (-17 :96-103), the `pack` key (-19 S12), `memory_index.py directives` and `scan_directives`
  (-14 S2, S5), `gov tag bundle` (-25).
- dTotalRecall: `record-kinds.toml` with its `layer` column (TOOL-dTotalRecall-1 S1), `code_record.py` and the body
  hash test in `measure_dossier_staleness` (-8 S2, S8, S12).
- dLinkedLibrary: `parse_note_line`, `scan_annotations` (TOOL-dLinkedLibrary-4 S2), `derive_note_span` (-17 S4),
  the retrofit progress cell `reads <share>` and `RETROFIT_PERIOD_DAYS` (-10 S2, S5).
- dIndexedDesign: `check-playbook.sh --resolve <path> --at <sha>` (TOOL-dIndexedDesign-10 S2, S4).
- dSafePassage (landed? check `git log --oneline -3 -- tools/lib/` before you cite it): `read_floor` over
  `tools/lib/python-floor.txt` (TOOL-dSafePassage-11 S1).
- Not ancestors: dShippedRelease (the release slot, `release-verify-failed`, the currency leg, the landing record),
  dCalibratedLens (the Loop Review step), dMindYourWords (TOOL-dMindYourWords-16, the first signal move), dFairHearing
  is an ancestor (the `security` lens, TOOL-dFairHearing-2 S1, -3 S2-S3). A non-ancestor's surface is never assumed to
  land first: route it by the rungs (a build-run precondition, an ask, or a stand-in).

Landed and readable now: `tools/drift-audit/` (`drift_report.py`, `drift_signals.py`, `selftest.py`), `tools/runlog/`
(`record.py write_record`, `model.py ANOMALY_KINDS`, `runlog_lib.py read_journal`, `extract.py`),
`tools/process-monitor/reap.py run_sweep`, `tools/branch-reconcile/branch_reconcile.py`, `tools/memory-tree/backlog.py`
(`render_ask_row`, `render_sev_row`, `render_scope_row`), `tools/policy/` (`policy.py get`, `catalogue.toml`),
`tools/codebase-map/map_lib.py measure_dossier_staleness`, `tools/check-dead-paths.sh`, `tools/unattended/`
(`resume-tick.sh`, `check-playbook.sh`, the recipe arm), `tools/workflows/tier2-review.js` (`DIFF_LENSES` security
slot), `tools/run-gates/lib-attribute.sh add_scratch_worktree`, `tools/roles/`.

Where a scout found that a design record, a parent spec or source disagree, v2's clause governs; a parent spec it
contradicts gets an ask (the rule above), never an edit. Where the clause itself names something source shows wrong,
the spec says what source shows, carries the clause's intent, and writes a deviation record naming the difference.

## Settled for every writer

These close forks the scouts left open across groups, so no two writers settle one differently. Each is a decision
of this spec run, recorded as a `Decided:` trailer on the spec commit; a writer who finds one wrong says so in its
return and writes a deviation record rather than a second answer.

1. **The Maintain home is the drift-audit kit**, observability's engine kit (layer-expansions:211), not a new kit:
   a new install location trips veto 2 and no clause names one. The program is `tools/drift-audit/maintain.py`; its
   item rows are `[[item]]` rows in `tools/drift-audit/kit.toml` read through TOOL-dDeclaredLoop-12's `check_program`
   (the scouts found no parent gives an expansion's item rows a home: unit 1 states the home and files ask E if the
   loop kit must read it). Names are the lexicon's to confirm.
2. **The reading registration is a `[[reading]]` row** in the owning kit's `kit.toml` (I3), owned by unit 8. The pin
   it names lives on the `drift-pins.txt` row (TOOL-dWitnessedBar-16 S8), never in a second dict beside `PINS`.
3. **Test's leg-pack point** is a `[[gate_leg]]` row carrying `pack = "<name>"`, declared through `leg_factory.py
   new` and announced by the slot line `slot point.flow.leg-pack · filled` (TOOL-dWitnessedBar-28 S10;
   PLAY-dOrderedCharter-17:105). No spec mints a `point.test.*` row.
4. **The red leg reads a committed maintenance record**, never drift's node-local history (`drift_report.py:3860`),
   and with no record it is a dead probe, never green (layer-expansions:465-467).
5. **An ask `maintain.file` files carries no `SEV` row**, so `triage.py pass` reads it into Plan's triage and sets its
   level (TOOL-dRankedPlan-3 S2); the reading's band travels as a clause of the ask instead.
6. **The signal-move factory is extracted here** (the charter's [reuse] rule at the kind's second instance):
   `tools/lib/signal_leg.py`, owned by unit 18; TOOL-dMindYourWords-16 is re-pointed at it by ask F.

## Asks already known

The main loop files each once after the writers return. Cite the letter in your §8; add a new one only with its
target build and accept line.

- **A** · dWellOiledMachine · a `cadence` receipt ratifies when the policy key naming its run holds its standing-ask
  value (`retrofit.cadence: hot-first`, a fix in `maintain.fixes`), since TOOL-dWellOiledMachine-27 S3-S4 lets a
  cadence intake be placed only as `breakpoint` or `ask` (scout D disagreement 1; units 8, 9, 11).
- **B** · dWellOiledMachine · one sender over a notification adapter's `run` and the secret scan for a non-owner item,
  beside `push_owner_item` (scout B disagreement 7; unit 15 `report`).
- **C** · dPlacedRequest · `probe.py trigger` takes a cadence target, the content key of (reading, offender key)
  (scout B disagreement 2; unit 14 diagnose band).
- **D** · dPlacedRequest · a `repeat` build's derived README carries `authorized-by: recipe` and `pieces:`, which the
  driver reads (`unattended.sh:3958`, `:4220`; scout D disagreement 3; unit 11).
- **E** · dDeclaredLoop · the loop kit reads an expansion's `[[item]]` rows from its kit's `kit.toml` (scout A open
  point 1; unit 1), filed only if unit 1 finds `check_program` cannot read them as specced.
- **F** · dMindYourWords · TOOL-dMindYourWords-16 calls `tools/lib/signal_leg.py` rather than its own copy (scout C
  interface 4; unit 18).

## Owned nodes

| Node | Unit |
|---|---|
| `policy-key.maintain.host` | 2 |
| `policy-key.maintain.cadence` | 2 |
| `policy-key.maintain.events` | 2 |
| `item.maintain.lease` | 1 |
| `item.maintain.read` | 1 |
| `item.maintain.levels` | 1 |
| `policy-key.maintain.fixes` | 3 |
| `item.maintain.direct` | 3 |
| `policy-key.maintain.reading-admission` | 4 |
| `item.maintain.record` | 6 |
| `record-kind.maintenance-record` | 6 |
| `record-kind.run-record` | 6 |
| `policy-key.observability.run-record` | 6 |
| `policy-key.maintain.record-when` | 6 |
| `item.maintain.patch` | 8 |
| `policy-key.retrofit.cadence` | 9 |
| `policy-key.maintain.security-review` | 13 |
| `policy-key.maintain.tiers` | 14 |
| `policy-key.maintain.on-breach` | 15 |
| `item.maintain.file` | 15 |
| `policy-key.maintain.node-readings` | 16 |
| `policy-key.maintain.interpreter-eol` | 17 |
| `policy-key.maintain.reading-tree` | 18 |
| `policy-key.maintain.dead-after` | 18 |

Every other unit owns no node; each still names the nodes it reads, in prose.

## Shared interfaces — one spelling for every writer

Each row names its owner, the unit whose spec defines it; every other unit names it exactly as spelled here and cites
the owner. A spelling marked "proposed" has no source yet; the owner may refine it in its spec, and says so in its
return. Every new name is asked of `--suggest` first.

| # | Interface | Spelling | Owner | Source |
|---|---|---|---|---|
| I1 | The Maintain program | `tools/drift-audit/maintain.py`, one argv the cadence row's `run` names; item rows `[[item]]` in `tools/drift-audit/kit.toml` with tags `item.maintain.{lease,read,direct,patch,file,levels,record}`, walked in `needs` order through `run_cadence_period` (TOOL-dWellOiledMachine-13 S6) (proposed) | 1 | scout A row 1; layer-expansions:218-235 |
| I2 | The policy read | a bounded subprocess `python tools/policy/policy.py get <key>`, the kit found through `resolve_kit_dir`, the key a string literal at every call site (TOOL-dWellOiledMachine-59 S3) | 1 | scouts A, B I7, D 7 |
| I3 | The reading row | `[[reading]]` in the owning kit's `kit.toml`: `name` (the engine's long signal name), `layer`, `scope = "repo" \| "node"`, `kind` (a `record-kinds.toml` name, so the owner is derived and never typed), `pin` (a `drift-pins` key), `edges`, `fix` (optional, a `maintain.fixes` member), `events`, `live` (proposed) | 8 | scouts B I1, C 2; layer-expansions:177 |
| I4 | The reading record | drift-audit's dict `{signal, value, of, tolerance, gateable, live, unjudgeable, detail, not_asked}` (`drift_report.py:536-552`), unchanged; signal names stay the engine's long names (`ledger_rows_contradicting_git`, `non_terminal_specs_cited_by_product_source`, `closed_specs_with_no_product_commit`, `handkept_inventories_disagreeing_with_source`, `cutoff_keys_armed`, `dangling_pointers_in_own_ledger`, `remote_ci_red_streak`, `dossiers_older_than_their_paths`) so `drift-history.tsv` streaks survive | 8 | scout C interfaces 1, 3 |
| I5 | The offender and filing keys | offender key `<signal>\t<detail key>` as `render_drift_offenders` emits it (`drift_report.py:3985`); filing key `(reading, offender key)`; a recurrence adds a `seen` clause through `render_scope_row(target, [("seen", …)])` (`backlog.py:1528`) keyed by period or `<event>.<sha12>`; no new verb | 8 | scouts B I3-I4, A |
| I6 | The patch intake | `python tools/runtime/intake.py file --origin cadence --filer item.maintain.patch` for every patch-routed reading (TOOL-dWellOiledMachine-27 S1); unit 11's filer is its cadence row's `name` | 8 | scouts A, C 8, D 3 |
| I7 | The event run key | `refs/gov/leases/run/maintain/<event>.<sha12>` beside the period ref `refs/gov/leases/run/maintain/<period>`, each passing `check_cadence_segment` (TOOL-dPlacedRequest-18 S1); events verbatim `default-branch-red`, `release-verify-failed`, `session-start-breach` (proposed) | 8 | scout A |
| I8 | Band edges | `edges <e1>/<e2>` on the `drift-pins.txt` row, two non-negative integers; with `d = value − pin`: log for `0 < d ≤ e1`, diagnose for `e1 < d ≤ e2`, act for `d > e2`; admission refuses a row without `edges` under `maintain.tiers: bands` (proposed) | 14 | scout B I2 |
| I9 | The reading journal line | `ev=reading reading=<name> sha=<sha> value=<n> of=<n> key_hash=<16hex> band=log\|diagnose\|act`, `key_hash` as `drift_report.py:3761-3780` computes it (proposed) | 14 | scout B I5 |
| I10 | The maintenance record | kind `maintenance-record` (a `record-kinds.toml` row beside `run-record`); per-period fields `over-pin: <offender key>` lines, `log-band: <n>`, `security-head: <40-hex>`, `retrofit-heat: <share>`; the run record written by a journal reader at `point.journal-readers` through `write_record` (`tools/runlog/record.py:1179`) under `observability.run-record` (proposed) | 6 | scouts A, B I6, D 6 |
| I11 | The fix names and routes | exactly `reap`, `prune landed`, `regenerate stale`, `defer dormant`, `records-only fixes`, `close finished run records`; `direct` for the first two, `patch` for regenerate, records-only and close, `defer dormant` the dRankedPlan-4 proposal plus owner-gated `dispose` | 3 | `catalogue.toml:1129`; v2:1321 |
| I12 | The signal-leg factory | `tools/lib/signal_leg.py` with `run_signal_leg(signals, bounds)` applying PINS, BASELINES, RATCHETS and DECLARED_EMPTY and printing `<signal> <value> of <of> · <state>` (TOOL-dMindYourWords-16 S2's line); copy-installed kits carry it inline (proposed) | 18 | scout C interface 4 |
| I13 | The pack registration | `[[gate_leg]]` with `pack = "<name>"` through `leg_factory.py new`; values `memory`, `flow`, `instruction` (unit 18) and `maintain` (units 7, 15) | 18 | scout C interface 5; settled 3 |
| I14 | The reading tree and liveness | `maintain.reading-tree: clean-base` reads in a scratch worktree from `add_scratch_worktree <path> <base_sha>` (`tools/run-gates/lib-attribute.sh:59`) at `resolve_base_ref`'s sha, `worktree` reads in place; `maintain.dead-after` replaces `DEFAULT_DEAD_READINGS_LIMIT = 10` (`drift_report.py:3863`), and a dead reading is filed to the source its `kind` derives | 18 | scout C interfaces 6-7 |
| I15 | The maintainer role | `gov-maintainer` on `layer.observability` with the lens `maintenance-run` (TOOL-dBoundRoles-1 §4), a new `maintain` workflow in `tools/roles/workflows.toml` so `WORKFLOW_NAMES` admits it (proposed) | 10 | scout A row 10, open point 2 |
| I16 | The body-moved test | one helper in `tools/memory-tree/code_record.py` answering "did this definition's body hash move since commit X", extracted at its second caller; unit 5 calls it through `measure_dossier_staleness` (TOOL-dTotalRecall-8 S12) (proposed) | 12 | scout C interface 9 |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 6 → 15, 1, 16, 9, 13 | `maintenance-record` |
| 8 → 4, 14, 18, 7, 5, 12, 17, 16 | `[[reading]]` |
| 8 → 15, 1, 3, 9, 11, 13 | `item.maintain.patch` |
| 14 → 15 | `edges` |
| 18 → 7, 15 | `run_signal_leg` |
| 18 → 7, 5, 12, 16 | `maintain.reading-tree` |
| 15 → 7, 12, 17, 16, 13 | `item.maintain.file` |
| 1 → 3, 2 | `maintain.py` |
| 5 → 12 | `measure_dossier_staleness` |

## The units

**Writer groups and build order.** The `order` value is the build order: the maintainer definition first, since it
reads nothing of this build; the maintenance record, which every reading writes into; the reading row, then its
admission and its bands; the signal-leg factory and the reading tree, which the detectors and the red leg reuse; the
breach routes; the Maintain program and its fixes; the detectors; the node-scoped readings; the three cadence items;
and the cadence registration last, because turning Maintain on needs everything it runs. The harness splits the 18
orders into six writer groups of three consecutive orders; author every unit of your group, in order, and nothing
else:

| Writer | Units (order) |
|---|---|
| 1 | 10 (1), 6 (2), 8 (3) |
| 2 | 4 (4), 14 (5), 18 (6) |
| 3 | 15 (7), 1 (8), 3 (9) |
| 4 | 7 (10), 5 (11), 12 (12) |
| 5 | 17 (13), 16 (14), 9 (15) |
| 6 | 11 (16), 13 (17), 2 (18) |

Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **TOOL-dTendedCadence-10** — Items 10 (v2:1970 `[owed]`). I15. The maintainer's definition: `gov-maintainer`
  under `tools/roles/agents/` with its house overlay, its `BODY_CEILINGS` row (`check_roles.py:87`), the workflow
  value `WORKFLOW_NAMES` admits (`:92`), registered on `layer.observability` through TOOL-dBoundRoles-1 S5's
  `check_layer_roles`, which says no role file defines it. Its item role is Maintain's filings (layer-roles:481).
  Seen: `check_layer_roles` red on the planted row with no role file, green with it; `render_agents.py --check` green.
- **TOOL-dTendedCadence-6** — Items 6 (gap-maint-05, gap-maint-14). I10. The `maintenance-record` kind and its home
  (`point.memory.record-home`, PLAY-dOrderedCharter-16 §4 :133), written per `maintain.record-when` (`every-period`,
  `on-finding`); the run record moved from an agent-instructed close step (`tools/unattended/VERBS.template.md:909`,
  `SKILL.template.md:159`) to a journal reader under `observability.run-record` (`per-run`, `on-anomaly`, `none`),
  each value seen on a planted run. Scout A disagreement 5: `write_record` skips a run serving no spec unit
  (`record.py:1183`) and `ANOMALY_KINDS` lacks ceiling breach and dead probe: decide both in §8. Owns I10's fields
  that units 13, 14, 15 and 9 write.
- **TOOL-dTendedCadence-8** — Items 8. I3, I4, I5, I6, I7. Maintain as a cadence step of the observability
  expansion: readings registered by layer as `[[reading]]` rows, keyed readings from `--offenders` (`:4221`), patch
  intakes rendered from them, event runs keyed by event; dCalibratedLens's Loop Review step is named and left to it.
  `SIGNALS` (`drift_report.py:3521`) becomes the registry's reader, its 27 signals each given a row. Ask A applies.
- **TOOL-dTendedCadence-4** — Items 4 (gap-maint-02). Reads I3. Admission: an ownerless or pinless reading refused at
  registration under `refuse-unowned` and admitted and reported under `report-unowned`, nothing filed until an owner
  is derived from its `kind`; each value seen on a planted ownerless reading. Today "report only, no pin" is legal
  (`:4322-4326`): `refuse-unowned` reverses it, so say what each of the 27 rows declares.
- **TOOL-dTendedCadence-14** — Items 14 (gap-maint-13). I8, I9. The three bands under `maintain.tiers: bands`, `pins`
  keeping one severity per pin; edges declared beside the pin at registration and admission refusing one without
  them; the log band a journal line and a count in the maintenance record, the diagnose band a read-only `probe.py
  trigger --cause observation` with the reading as its observation (ask C), its record attached to the ask
  `maintain.file` files, the act band routed by its fix. Each band and the edgeless refusal seen on its planted
  reading. `probe.trigger` is the clause's token: spell it.
- **TOOL-dTendedCadence-18** — Items 18 (gap-maint-09, -10, -11). I12, I13, I14. The five gateable signals moved to
  core legs owned by memory, flow and instruction through the factory; flow's kit is unbuilt (layer-instruction:231),
  so its home is a §8 fork; `handkept` reads drift-audit's own README (`drift_signals.py:215`), a fork too. After the
  move `drift_report.py --check` holds no gateable signal: say whether the `drift-audit records` leg
  (`tools/gate-legs.json:1052`) stays as a ratchet leg, moves or retires, with `**Readers:**`. `maintain.reading-tree`
  seen on a planted reading that differs between the two trees; the `gh` reading registered with its liveness, dead
  past `maintain.dead-after`, filed to its source, seen on a planted node without `gh`. Ask F applies.
- **TOOL-dTendedCadence-15** — Items 15. Reads I5, I8, I10, I12, I13. `maintain.on-breach` at `maintain.file`:
  `file-ask` through `render_ask_row` (`backlog.py:1516`) with no `SEV` row (settled 5); `red-leg` a `pack =
  "maintain"` leg reading the newest committed maintenance record offline, red while an offender stands over its pin,
  dead with no record (settled 4); `report` through the notification adapter (ask B). Each value seen on its planted
  offender. The currency leg has no carrier: cite layer-expansions:463-467 only.
- **TOOL-dTendedCadence-1** — Items 1. I1, I2. The Maintain run as its step checklist on the flow's executor, never a
  recipe-mode playbook: the `[[item]]` rows, their `needs` order, `maintain.lease` through `run_cadence_period`, and
  `maintain.levels`. Name why recipe mode is rejected (research-maintain:97-108). Ask E if it applies.
- **TOOL-dTendedCadence-3** — Items 3 (gap-maint-07; `closes TOOL-dTendedCadence-20`). I11. The six fixes and their
  routes, `maintain.direct` for `reap` (`run_sweep`, `reap.py:345`) and `prune landed` (`branch_reconcile.py --write`);
  `close finished run records` over `build_nonterminal_merged_runs` (`drift_report.py:2512`); `defer dormant` per ask
  -20's accept line. Scout A disagreement 1: `policy.py get maintain.fixes` refuses on the `{derived = …}` default:
  make it a literal set in the catalogue row. Each fix seen on a planted case, an empty `maintain.fixes` too.
- **TOOL-dTendedCadence-7** — Items 7 (gap-orient-10, gap-maint-08). Reads I3, I12, I13, I14. One detector over two
  populations with two oracles kept apart: `check-dead-paths.sh`'s history needles over repo text and the tracked-set
  test over auto-memory (`signal_dangling_pointers`, `drift_report.py:968`); the script's leg kept as a `pack =
  "maintain"` leg (NP-22). The tokens `check-dead-paths.sh` and `memory/` appear verbatim. `DEAD_PATH_PIN` is out.
- **TOOL-dTendedCadence-5** — Items 5 (gap-maint-06). Reads I3, I16. Map freshness on its caller map (v2:1990): the
  code record of TOOL-dTotalRecall-8 is that map; the reading calls `measure_dossier_staleness` as -8 S12 changes it
  and routes `regenerate stale` through `maintain.patch`. Seen on a planted dossier whose definition body moved.
- **TOOL-dTendedCadence-12** — Items 12. I16, reads I3. Bundle members whose code changed while their head line did
  not (night pass point 4, `:243-268`): no seam in source; it calls dLinkedLibrary-4 and -17 and dTotalRecall-8, and
  extracts the body-moved helper at its second caller. Seen on a planted member whose body moved under an unchanged
  head line.
- **TOOL-dTendedCadence-17** — Items 17 (gap-maint-15). Reads I3, I6. The EOL detector under
  `maintain.interpreter-eol` (`file`, `warn`, `off`, each seen): an EOL table beside the floor file, since
  TOOL-dSafePassage-11 S1's `read_floor` refuses anything but `<major>.<minor>` (proposed `tools/lib/python-eol.tsv`,
  seeded from research-python-floor:57-64); the intake filed six months before the floor's end of life.
- **TOOL-dTendedCadence-16** — Items 16 (gap-maint-14). Reads I3, I5. The four node-scoped readings (an act past
  `runtime.act-ceiling`, a node's run left unrecorded, a pushed commit missing a required key from the commit-key
  leg's registration on, a standing directive in auto-memory not promoted), each filed as an ask and never a bar or
  push leg, under `maintain.node-readings` (`every-node`, `lease-holder`, each seen). The `[gates]` token appears.
- **TOOL-dTendedCadence-9** — Items 9 (RF-6). Reads I6, I10. `maintain.retrofit-heat` filing each period's sweep as a
  patch build under `retrofit.cadence: hot-first`'s standing ask (ask A) and sweep asks only under `off`, and the
  progress cell's share of reads (`reads <share>`, dLinkedLibrary-10 S5, `RETROFIT_PERIOD_DAYS` imported); read only
  where observability is installed. Scout D disagreement 2 (a sweep patches no terminal build) is a §8 fork. The
  path-keeping read counter is new: `derive_tool_class` discards inputs by design (`tools/runlog/extract.py:532`).
- **TOOL-dTendedCadence-11** — Items 11 (night pass point 1). Reads I6. A cyclic playbook's cadence item filing
  `repeat` intakes: where a playbook declares its cycle is a §8 fork (scout D row 11); its derived README must pass
  the recipe preflight (ask D). "The owner will expand it later; this is its seat" (night-pass:110): spec the seat.
- **TOOL-dTendedCadence-13** — Items 13 (gap-maint-12, NP-19). Reads I10. The recurring security review, a cadence
  item running dFairHearing's `security` lens over the landed tree under `maintain.security-review` (`weekly`,
  `every-landing`, `off`, each seen). A whole-tree reading is impossible today (the diff is `base...head`, the skeptic
  refutes a defect present at the base): settle a period-range reading from the last `security-head` in §8, launched
  through `launch_act`. `every-landing` has no event (scout D disagreement 6): a fork. Findings go through
  `maintain.file`.
- **TOOL-dTendedCadence-2** — Items 2 (gap-maint-01; `closes TOOL-dTendedCadence-19`). I7, reads I1. The cadence on
  Runtime's hosts: the `maintain` row at `point.cadence-items` with `host-key = "maintain.host"`, its period from
  `maintain.cadence`, its event runs for `maintain.events`, `release-verify-failed` rendered not installed where
  integrations is not installed; each value seen on its planted case. Scout A disagreements 2-3: `every-session` has
  no `derive_period` kind and the `session-start` default host has no tick: settle both in §8, registering the
  `session-start` host the parent hands to this build (TOOL-dWellOiledMachine-59 §3).
