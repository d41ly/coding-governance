**Serves:** research TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30

# Spec brief — dWitnessedBar, the thirty units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dWitnessedBar/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dWitnessedBar/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every entry of "Shared interfaces", and the scout record your units cite:
   `memory/builds/dWitnessedBar/build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md` (units 1-8, 21, 23,
   25, 29, 30), `-b.md` (9-12, 19, 22, 24, 28) and `-c.md` (13-18, 20, 26, 27). Each holds a seam table row per
   clause, with path:line at `3f2b31b5`.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, and the
`[policies]` rows the packet's Obligations list by v2 line), the gap register `B/…-gap-register.md` (the packet's
Gaps cite each gap's line), `B/…-flow-steps.md` (lines 278-420 the Build and Test items, 704-720 retrofit's
`adopt` and `test.seed`, 900-1065 the amends), `B/…-retrofit.md` (`[ledger]` 187-272, pins and cutoffs 287-309,
`[seed]` 310-338, `[ratchet]` 424-443), `B/…-research-retrofit-a.md`, `-b.md`, `B/…-research-test.md`,
`B/…-systems.md` (the tag rule, 244-271), `B/…-flow-roles-adoption.md` (FA-1 to FA-7), `B/…-layer-expansions.md`
(the witness rule, 325-345), `B/…-research-integrations-a.md` and `-b.md`, `B/…-research-observability-trace.md`,
`B/…-night-pass.md` (points 4 and 6, NP-22), `B/…-night-pass-two.md` (point 5, NT-23), `B/…-away-pass.md` (AP-22,
AP-31, AP-33), `B/…-stall-and-loop.md` (P39), `B/…-research-python-floor.md`, `B/…-walk.md` (WK-1), and the fork
rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never edit an instrument, v2,
the as-built view or the packet: the packet's Non-goals.

## Every parent is specced; only dTrueNorth is built

dGroundRules (the policy file `.governance/policy.toml`, its one reader `tools/policy/policy.py`, its catalogue
`tools/policy/catalogue.toml`, `budgets.*`, the legacy-homes list `tools/policy/legacy-homes.txt`, and
`tools/lib/resolve_bash.py` at TOOL-dGroundRules-25 S28), dOrderedCharter (the kinds register
`tools/playbook/kinds.toml`, the record factory `build_records.py` at PLAY-dOrderedCharter-7 S7, the leg row keys
`enforces` at -7 S2 and `pack` at -19 S12, the tag grammar and `namespaces.toml` at -19 S1/S2, `compute_coverage`
and `resolve_compare_base` moved to `tools/lib/coverage_join.py` at -19 S9, the edge grammar at -24 and -28, the
overlay rows at -35 and -36, the positional, legacy and unpinned lists at -19 S11, -20 S4 and -29 S2), dSafePassage
(the step rows `tools/govkit/steps.toml` read by `upgrade_steps.read_steps`, the surface classes at -10, the
interpreter floor `tools/lib/python-floor.txt` at -11), dFairHearing and dDeclaredLoop (the loop kit, the item tags
`item.test.*`, the disposition record, `flow.wait-ceiling` at TOOL-dDeclaredLoop-33) each landed their specs and
are DEFERRED to their build runs, which the chain runs before this build's build run. None of those product files
exists at HEAD. So every spec here cites the parent's landed spec by id and section as the interface, and names
the call it makes; the build run re-grounds against the landed parent. Never spec a parent's mechanism, never add a
copy of a parent's reader, and never invent a policy route: a policy key this build owns is a row of
dGroundRules' catalogue, read through `policy.py`'s reader once it lands, with the default v2's `[policies]` row
states until then, and the spec says so in one line.

## Every spec, whatever its unit

- Path `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md`; H1
  `# TOOL-dWitnessedBar-<n> — <title>`, an EM DASH, never a colon.
- Status header `OPEN`, `rev-1`, `2026-10-25`, `node d`, `Tier-2`, `base cdfbd1cf`, `streams tooling`, the `order`
  verb your roster row names, and `advances TOOL-dWitnessedBar-31` (the build's own open ask; the build run's last
  unit closes it). Copy a landed sibling's line shape, e.g.
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md` line 3, with `OPEN` for its status.
- Binding lines, each at column 0 on a line of its own: `**Carries:** <Items id>@<hash8> whole`, and for the unit
  that owns a node, `**Carries:** node:<node>` (the owned-node table below). A unit carrying a clause in parts writes
  `part <k>/<n>` instead of `whole`, and every part of that clause is carried by a spec of this build.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close. The unattended kit's own self-test suites are waived for this build's
  landing (the README's self-test waiver rule): a criterion they would observe is amended citing that rule.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in "The units" are a scout's reading at `3f2b31b5`: verify each line number against source before
  citing it.
- §8 forks: settle each by the README's rungs (the execution plan lines 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`; a choice the README's `may: PLAY-dClosedLoop-3` grant
  lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave an open question: a FACT-QUESTION names its probe
  and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` and `.claude/roles.json` from `tools/roles/`, `memory/guides/*.md` from
  their kit templates, and `tools/workflows/*.js` from their `.template.js`: name the source as the edit and the
  render as its copy.
- A later build's surface named in your clause (dScopedBuild's `build.acceptance` writer for unit 7, dBoundRoles'
  role re-founding for unit 23) is a stand-in or a join that build arms: spec the stand-in this build ships and name
  the hand-over, never the later build's mechanism (packet Non-goals, Later builds named).
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dWitnessedBar/build/2026-10-25-build-TOOL-dWitnessedBar-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md` shows (Serves, Departs
  from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with `<k>` = your
  unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and `author-recorded`
  (the README's deviation-values rule). Do not commit it.
- An ask your spec owes another build (a parent spec's row that disagrees with yours, say) is NOT filed by you: name
  it in your return and the main loop files it as a row in that build's `BACKLOG.md` (the README's writes rule).
- Write nothing outside `memory/builds/dWitnessedBar/spec/` and `memory/builds/dWitnessedBar/build/`; temp files go
  under the scratch path your harness names.

### What the earlier spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python leg_factory.py …`) and keep its
  full path in §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it
  inside a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. When you hand off to a unit another writer owns, name the token exactly as "Shared interfaces" spells
  it, and that writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours (a later unit never hands off to an earlier one:
  the earlier unit reads whatever rows exist when it builds, and the later one's rows join as data). The edge list in
  "Edges" is the one to declare; add an edge only when your spec truly reads or produces it, and say so in your
  return so the other writer adds the reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a file) owes a `**Readers:**` clause naming every reader
  by path and by value (hygiene check 25), each found by `git grep` over the tree.
- **No link-shaped text**, `[x](y)`, anywhere outside a real link, backticks included (hygiene check 2).
- **A §8 mark's parenthesis is closed**: `RESOLVED (agent, 2026-10-25, delegated)`, provenance after the paren.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); the gate reads tracked files only, so run it in a throwaway clone
  under your scratch path with your specs committed there. A red it prints on your files is yours to fix. The main
  loop runs `check-spec-tokens.py` after every writer returns.

## HEAD differs from four clauses — settle each in its unit, never silently

- **D1 · 28 registries, not 27 (unit 16).** `memory/project/temp-name-sites.txt` (TOOL-dRedressedBar-24, after the
  baseline) is shrink-only debt, so HEAD's census is 18 shrink-only, 2 append-only, 7 declared sets and 1 ceiling.
  Unit 16 converts every registry a derivation over `memory/project/` finds at build time, the class and not a typed
  count ([class]), and writes a deviation record from the clause's "27" and "17" (risk stricter).
- **D2 · cutoffs (unit 17).** HEAD holds 23 `*_CUTOFF=` keys in `.memory-tree.conf` and 10 in `.unattended.conf`,
  33 where `retrofit.md:296` measured 34. The clause states no count: register every cutoff a derivation over the
  confs finds, and write no deviation for the count.
- **D3 · the H5 move has not happened (units 13, 14).** `compute_coverage`, `resolve_compare_base` and
  `derive_baseline_additions` are still in `tools/codebase-map/map_lib.py`. The clause names dOrderedCharter's move
  (PLAY-dOrderedCharter-19 S9, `tools/lib/coverage_join.py`), which the chain builds first: cite S9 as the import,
  and say in §8 that the build run re-grounds on it.
- **D4 · 142 legs, not 140 (unit 19).** Review every leg `tools/gate-legs.json` holds at the build run's base, derived
  rather than counted; "today's 140" is the clause's measurement of the same population, so no deviation is owed for
  the count, and §8 says so.

## Shared interfaces — one spelling for every writer

Fixed so thirty specs by five writers agree on the interface axis (M2). A writer who finds one wrong says so in its
§8 as a fork and settles it there by the rungs; it never silently respells one. "Owned by" is the unit that specs
the interface; every other unit named reads it as written here.

- **I1 · the leg row key set.** Today `KNOWN` is spelled twice in `tools/run-gates/run-gates.test.sh` (`:244` and
  `:580`). Unit 12 extracts it into one constant both arms read ([reuse], second instance), and every later unit
  adding a row key adds it there once. New keys, one spelling each: `tag` (unit 12), `pack` (PLAY-dOrderedCharter-19
  S12's, value the bare pack word), `tests` and `enforces` (unit 22; `enforces` is PLAY-dOrderedCharter-7 S2's),
  `purpose` (unit 19), `precommit` (unit 10, an argv array), `level` (unit 9). The govkit emitter's floors for them are
  one table `LEG_KEY_FLOORS` beside `govkit.py`'s `*_FLOOR_RUN_GATES` constants, owned by unit 12, never a new
  hand-copied constant per key. Owned by unit 12.
- **I2 · the tag forms.** `leg.<owner-seg>.<name-seg>`, with `leg.adopter.<name>` for a repository's own legs;
  `check.<kit>.<name>`; `pack.<word>` with the words `ratchet` (unit 14), `portability` (unit 24) and `adopter`
  (unit 28). Grammar `seg := [a-z0-9][a-z0-9-]*` under PLAY-dOrderedCharter-19 S1's `TAG_RE`; the rows go in its
  `tools/playbook/namespaces.toml`. The free-text leg `name` stays the join key of every name-keyed file
  (`ceiling-evidence.txt`, `selftest-budgets.txt`, `windows-only-legs.txt`, `silenced_legs`; systems.md:262-271):
  a record keyed by leg is keyed by `name`. Owned by unit 12.
- **I3 · the leg factory.** `tools/run-gates/leg_factory.py` generates `tools/gate-legs.json` from the packs'
  `[[gate_leg]]` declarations (kit `kit.toml` rows, the `[[exempt_leg]]` rows of `tools/govkit/registry.toml` folded
  in), registered as a `[[generated]]` output that `tools/run-gates/regen.py` writes and checks; its conformance gate
  is the leg kind's `gate` in `tools/playbook/kinds.toml` (PLAY-dOrderedCharter-7 S4), absorbing govkit selfcheck
  7h's both-ways join. Owned by unit 11. Units 9, 10, 14, 24 and 28 register through it.
- **I4 · the ledger factory.** `tools/lib/legacy_ledger.py`, one file per population, each registration declaring
  `population`, `seed` (an argv measured at a SHA), `key` (`site` | `key` | `record` | `cutoff`), `drain` (`hunk` |
  `key` | `none`), `direction` and `home` (retrofit.md:189-195). Directions spelled `shrink-only`, `append-only`,
  `declared-set`, `ceiling`. Rows TAB-separated, key fields then count, SHA and disposition, never a line number;
  dispositions `seeded`, `carried:<unit>`, `deferred:<ask>`, `keep:<ask>`, `widened:<record>`. Its merge class is
  `check_ledger(path)` in `tools/memory-tree/merge-rows.py`, beside `check_build_backlog`, with a per-path row
  predicate (a TSV row fails today's bullet `_ROW_RE`). It reaches copy-installed kits as an inline block under
  `tools/lib/resolve-python.test.sh`'s `PARITY_ROWS`. Owned by unit 13; units 14-18, 20, 24 and 28 register through
  it.
- **I5 · `test.seed`.** The seed verb on the ledger factory: seeds only an absent population, at that SHA, after that
  only a widened predicate's new keys as `widened:<record>`; a failed or dead-probe seed records the population
  unarmed (retrofit.md:310-338). Owned by unit 15; `retrofit.unseeded` is its key.
- **I6 · the bash resolver.** `tools/lib/resolve_bash.py`, block `# >>> resolve_bash_py` (TOOL-dGroundRules-25 S28
  spells it; unit 26 lands it if dGroundRules has not), and its JavaScript twin `tools/lib/resolve_bash.js`, block
  `// >>> resolve_bash_js`, both under `PARITY_ROWS`. `GOV_BASH` stays the one override name. Owned by unit 26.
- **I7 · the wrong-shell predicate.** Block `# >>> refuse_wrong_shell` in `tools/lib/refuse-wrong-shell.sh`, beside
  `resolve_python` in the same entry-point population, keyed on a `/mnt/<drive>/` path over a Windows gitdir so the
  deliberate WSL mirror of `run-held-wsl.sh` on WSL's own disk stays green. Owned by unit 27; unit 26's resolvers
  call the same predicate.
- **I8 · the verdict record.** The runner's `<git-dir>/gate-run/<run id>/verdict`, `<key>TAB<value>` lines, read by
  `read_record_keys` (`run-gates.sh`), the hook's `check_verdict_record` and `drift_report.py`. New keys, additive:
  `tree` (unit 4), `run_id` and `cause` and `tail.<n>` (unit 25), `held.<n>` (unit 5), `warn.<n>` (unit 29), an
  all-digit suffix an index (runlog's grammar). The per-tree verdict the runner writes and the pre-push hook reads is
  `<common-dir>/gate-verdict/<tree hash>`, placed as `gate-full-green.shared` is; unit 6's remote verdict carries the
  same tree key. `record-kind.verdict` owned by unit 4.
- **I9 · red classes and routes.** `OWN`, `INHERITED`, `MIXED`, `CONTENDED`, `DEAD PROBE`, the attribution row as
  `run-gates.sh` writes it. `verdict.blocks` values `own-mixed-contended`, `every-red`, `own-only`;
  `verdict.red-route` values `fix-pass-or-design`, `always-new-unit`. The tester judges OWN and blocking MIXED reds
  only. Owned by unit 3.
- **I10 · the same-tree re-run.** `runleg "$i" .rerun`, beside `.retry` and `.sample`, writing `<i>.rerun.leg`, under
  `test.verdict`'s env. A red-then-green leg is nondeterministic and reaches `test.flakes`. Owned by unit 8.
- **I11 · the hold.** One hold predicate (today `run-gates.sh`'s `subject == kit OR chunk == selftests`, spelled three
  times: extract it once) extended by a held-source word, `kit` or `quarantine`, and one
  `GATE held  <leg>  (<source> …)` line. `verdict.held` values `peer-or-cadence`, `push-selected`, `on-demand`.
  Owned by unit 5; units 8 and 30 add the `quarantine` source and its release.
- **I12 · the flake record and the gate-health record.** `record-kind.flake`: leg name, run id, SHA, tree, first rc,
  re-run rc; `test.flakes` is its one writer (unit 8). The gate-health record: `measured <count>/<window>` and the
  verdict ids it came from, written by unit 1 at each gate-health measurement and read by unit 8's hold as data
  (2 in 10 until it holds a threshold). Both are minted through PLAY-dOrderedCharter-7 S7's record factory and
  registered in its `kinds.toml`; each spec names its home and the factory call, and cites S7 as the interface.
- **I13 · the leg ask.** One function `file_leg_ask`, keyed by leg name and reused across every `BACKLOG.md`,
  extracted at this second instance from `write_held_asks` (`tools/unattended/unattended.sh`). Unit 8 extracts it and
  names its home in §4; units 30 and 6 call it.
- **I14 · the tester.** Role `gov-tester`, slot files `tools/roles/agents/gov-tester.agent.md` and
  `tools/roles/house/gov-tester.md`, `writes: none` (scratch only), joining the `gate-bar` workflow's `roles`; its
  return's judgment set closed at `code-miss` | `spec-wrong`. Owned by unit 23; units 3 and 21 read it.
- **I15 · a leg's own files.** The words of its `argv` that name tracked files, read as the runner's held census
  already reads them, plus its gate script, plus the targets of its `tests` edge where declared. Units 21 and 28.
- **I16 · seen-red records.** `record-kind.seen-red`, keyed by leg name and red SHA, one per gate a build adds or
  changes. Until dScopedBuild lands `build.acceptance` as its writer, the attended or unattended main loop's arm
  observation (BUILD-METHOD M8, "Observe the owed arms") writes it as an acceptance-ledger line in a grammar unit 7
  fixes, and `test.seen-red` reads that line as the record. Owned by unit 7; unit 28 reads it.
- **I17 · item tags.** `item.test.merge`, `item.test.select`, `item.test.verdict`, `item.test.route`,
  `item.test.attribute`, `item.test.flakes`, `item.test.seen-red`, `item.test.exit`, `item.test.seed`, as
  dDeclaredLoop's specs spell them. Every unit naming a Test item uses these.
- **I18 · policy keys.** Exactly as v2 spells them, each a row of `tools/policy/catalogue.toml` (dGroundRules) read
  through `policy.py`, owned per the table below. Values and defaults are the packet's Obligations rows verbatim.
  `instructions.exclude` is PLAY-dOrderedCharter-35 S5's and `flow.wait-ceiling` TOOL-dDeclaredLoop-33's; units 28
  and 30 read them and never re-declare them.

## Owned nodes

| Node | Unit |
|---|---|
| `policy-key.verdict`, `policy-key.verdict.remote.trust`, `policy-key.verdict.remote.pin-scope`, `policy-key.verdict.remote.pin` | 6 |
| `policy-key.hooks.bypass` | 2 |
| `item.test.route`, `record-kind.attribution`, `record-kind.routing`, `policy-key.verdict.blocks`, `policy-key.verdict.red-route` | 3 |
| `item.test.merge`, `item.test.verdict`, `item.test.exit`, `record-kind.verdict`, `policy-key.verdict.tree` | 4 |
| `item.test.select`, `record-kind.selection`, `policy-key.verdict.held` | 5 |
| `item.test.seen-red`, `record-kind.seen-red` | 7 |
| `item.test.flakes`, `record-kind.flake`, `policy-key.verdict.flakes`, `policy-key.verdict.flakes.entry` | 8 |
| `policy-key.verdict.flakes.release` | 30 |
| `policy-key.tests.product`, `policy-key.tests.landing-levels`, `policy-key.tests.without-cadence` | 9 |
| `tag-namespace.leg`, `tag-namespace.check`, `tag-namespace.pack` | 12 |
| `system.retrofit` | 13 |
| `policy-key.retrofit.widen` | 14 |
| `item.test.seed`, `policy-key.retrofit.unseeded` | 15 |
| `item.test.attribute` | 23 |
| `policy-key.trace.leg-output` | 25 |

Each node is one `**Carries:** node:<node>` line, one per line, in its unit's spec.

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one. A writer who finds an edge false removes it from its
own spec and says so in its return.

| Producer → consumers | Token |
|---|---|
| 26 → 27 | `resolve_bash_py` |
| 13 → 15, 14, 16, 17, 18, 20, 24, 28 | `legacy_ledger.py` |
| 15 → 14, 16 | `test.seed` |
| 12 → 22, 19, 11, 14, 24, 28 | `tag` |
| 22 → 11, 24 | `enforces` |
| 22 → 21 | `tests` |
| 19 → 11 | `purpose` |
| 11 → 14, 10, 24, 9, 28 | `leg_factory.py` |
| 14 → 16 | `retrofit.widen` |
| 9 → 5 | `tests.landing-levels` |
| 4 → 25, 3, 6, 2 | `gate-verdict` |
| 25 → 29 | `run_id` |
| 23 → 3, 21 | `gov-tester` |
| 3 → 8, 30 | `verdict.blocks` |
| 5 → 8, 30 | `verdict.held` |
| 8 → 1, 30 | `record-kind.flake` |
| 8 → 6 | `file_leg_ask` |
| 7 → 28 | `record-kind.seen-red` |
| 6 → 2 | `verdict` |

## The units

**Writer groups and build order.** The `order` value is the build order: the resolver and the ledger before every
population registered through them, the tag field and the edge fields before the leg factory that emits them, the
factory before the packs and the derived lists, the verdict record before the attribution, hold and flake machinery
that write into it, the tester before the routes that hand it reds, and the overlay's legs last, once the factory,
the ledger and the seen-red record exist. The build harness (`tools/workflows/unattended-build.js`) splits the 30
orders into five writer groups of six consecutive orders and hands each writer its group; author every unit of your
group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 26 (1), 27 (2), 13 (3), 15 (4), 12 (5), 22 (6) |
| 2 | 19 (7), 11 (8), 14 (9), 16 (10), 17 (11), 18 (12) |
| 3 | 20 (13), 24 (14), 10 (15), 9 (16), 4 (17), 25 (18) |
| 4 | 23 (19), 3 (20), 5 (21), 8 (22), 1 (23), 30 (24) |
| 5 | 29 (25), 7 (26), 21 (27), 6 (28), 2 (29), 28 (30) |

Six Tier-2 specs is a long pass: keep each spec to what its clause and its shared interfaces need, cite the scout
record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **TOOL-dWitnessedBar-26** — Items 26 (gap-tool-20, AP-33). One resolver, I6, extracted from the execution-based
  pair `profile_bar.resolve_bash` and govkit's `resolve_bash`, keeping both contracts, and replacing every site scout
  C lists (the seven loops over `bash.exe` and `bash`, `regen.py`, `resolve_bash_shell`, `resolve_launcher`,
  `stop-guard.js`'s `spawnSync('bash', …)`, `resolve_shell_argv`'s bare fall-back), found by a query over tracked
  Python and JavaScript that is itself the arm (widen `measure_legs.py`'s `test_no_bare_bash_argv` repo-wide). The
  candidate order, refusals and acceptance arms are the clause's, verbatim.
- **TOOL-dWitnessedBar-27** — Items 27 (AP-33). I7 at every entry point the `resolve_python` block reaches, plus the
  Python and JavaScript entries through unit 26's resolver; seen red on a WSL-bash-over-`/mnt/` plant, green on the
  WSL mirror leg's own-disk path and on a Linux node's bash.
- **TOOL-dWitnessedBar-13** — Items 13 (gap-test-14). I4: the factory, its directions and homes, rename-carry
  (`-M`), the both-ways arm and base through D3, the merge class with the append-collision case of
  `merge-rows.test.sh` run on a planted ledger conflict, and the copy-install route. Re-point `sh_hygiene.py`'s and
  `encoding_posture.py`'s two copies of the count ratchet onto it (the second instance).
- **TOOL-dWitnessedBar-15** — Items 15. I5 at every check's registration (the factory's registration and a leg's
  row), retiring the absent-only seed guards of `adopt-codebase-map.sh` and `adopt-drift-audit.sh` onto it.
- **TOOL-dWitnessedBar-12** — Items 12. I1 and I2: the `tag` field beside every leg's `name`, the three namespace
  rows with their extractors, the extracted `KNOWN` constant and `LEG_KEY_FLOORS`.
- **TOOL-dWitnessedBar-22** — Items 22 (night pass point 4). `tests` and `enforces` on leg rows. Settle in §8 the
  target set of `enforces`: PLAY-dOrderedCharter-7 S2 admits `principle.*` and `practice.*`, PLAY-dOrderedCharter-24's
  edge row says `unit` or `practice`; follow -7 S2, the leg-row grammar, and name the ask for -24's row in your
  return. The declaring site of `tests` is the leg row (the clause); the dossiers' `gate-legs` front matter is the
  map's (dTotalRecall): derive or compare, never edit it here, and name that ask in your return.
- **TOOL-dWitnessedBar-19** — Items 19 (PM-5, D4). `purpose` on every leg: each derived from what the leg carries
  (its dossier, its descriptor, its name's parenthetical) by a rule the spec states, and every leg the rule cannot
  derive listed as an owner question in a record of this build, never guessed.
- **TOOL-dWitnessedBar-11** — Items 11 (gap-tool-01). I3: one declaration per leg, the factory, its conformance gate
  over the whole population, and every leg's `enforces` naming the principles it enforces.
- **TOOL-dWitnessedBar-14** — Items 14 (gap-test-15, gap-test-16). The `ratchet` pack's legs, all eleven rows of
  retrofit.md's `[ratchet]` table including `populated`, `seed laundering`, rename and merge, each value of
  `retrofit.widen` seen on a planted growth.
- **TOOL-dWitnessedBar-16** — Items 16 (RF-5, D1). Every registry converted in place onto I4 with the readers scout C
  names re-pointed, drift's hand-typed `SHRINK_ONLY`, `PINS` and `BASELINES` retired with their `**Readers:**`
  clause, `derive_low_waters` surviving. Start from retrofit.md's confirming probe on readme-contract.
- **TOOL-dWitnessedBar-17** — Items 17 (D2). The seven pins scout C lists (two unset, registered unseeded) as keyed
  populations, and every date cutoff registered as a `cutoff` population; `VERB_OFFENDER_PIN` and
  `SUFFIX_OFFENDER_PIN` are dMindYourWords' and stay out.
- **TOOL-dWitnessedBar-18** — Items 18. Registration only: the positional references, IW-1's legacy list and the
  unpinned facts from dOrderedCharter's keyed lists, and dSafePassage's step rows as an `append-only` population
  keyed by step id, read through `upgrade_steps.read_steps`.
- **TOOL-dWitnessedBar-20** — Items 20 (M4). `tools/policy/legacy-homes.txt` as a population keyed by conf and key;
  settle in §8 whether its `<home> <key> <mark>` rows convert into I4's grammar or register as their own key kind.
- **TOOL-dWitnessedBar-24** — Items 24 (P37, AP-31; gap-tool-13, -15, -21, gap-test-09). The `portability` pack: a
  line-ending class leg over every tracked execution-sensitive file, the encoding arms (stdout, JavaScript, Python,
  the last moved in from `encoding_posture.py`), `sh_hygiene.py`'s legs beside them, the path, temp-file, quoting
  and bare-shell-name arms, the interpreter-floor arm running a real interpreter at TOOL-dSafePassage-11's floor
  with a feature census, and the shell-role ledger on I4; `ps-hygiene.py` given its leg. Each arm seen red on a
  planted case. The pairing table is PLAY-dOrderedCharter-30's.
- **TOOL-dWitnessedBar-10** — Items 10 (gap-test-07, -08). The pre-commit list derived from the factory's rows (each
  leg's `precommit` argv and its guard) replacing `.githooks/pre-commit`'s hand-named five; multi-node cost evidence
  on `ceiling-evidence.txt`'s node column and a committed whole-bar wall record.
- **TOOL-dWitnessedBar-9** — Items 9 (gap-test-03). The product-test contract: `level` on legs, the three `tests.*`
  keys, runner adapters (the guardrails kit's pytest pack as the first), each `tests.product` value seen on a
  planted repository.
- **TOOL-dWitnessedBar-4** — Items 4 (gap-test-02, gap-test-05). I8's per-tree verdict, written by the runner and
  read by the pre-push hook in place of the hook-written `write_bar_green`; `verdict.tree` with `test.merge` as the
  lander's `--prepare`; `test.exit`'s verified tree.
- **TOOL-dWitnessedBar-25** — Items 25 (P35, gap-test-20). `run_id` and `cause` on the verdict, and a failing leg's
  output tail kept by hash under `trace.leg-output`, its committed home registered with HYGIENE.
- **TOOL-dWitnessedBar-23** — Items 23 (WK-1). I14, the stand-in dBoundRoles re-founds; it plays `test.attribute`,
  `test.reason` and the fix pass's wrong-spec judgment.
- **TOOL-dWitnessedBar-3** — Items 3. Attribution decides what blocks: I9 turns `run_attribution`'s report-only
  classes into the blocking decision `verdict.blocks` names, `test.route` routing each red by class, and
  `verdict.red-route` deciding a fix pass or a new Design unit; `INHERITED_RED` retired onto it with its
  `**Readers:**` clause.
- **TOOL-dWitnessedBar-5** — Items 5. I11 by `verdict.held`, a held leg's result in the verdict record
  (`held.<n>`), and `test.select` reading `tests.landing-levels` and the held set.
- **TOOL-dWitnessedBar-8** — Items 8 (gap-test-04). I10, I12's flake record, the hold at `verdict.flakes.entry`
  (2 in 10 until the gate-health record holds a threshold), and I13 extracted; seen on a fixture leg that reds then
  greens and red on a leg planted below the threshold.
- **TOOL-dWitnessedBar-1** — Items 1 (gap-test-10). Gate health measured as a sibling of drift's
  `measure_legs_retried_after_timeout`, the `measured` threshold derived by the clause's rule once every leg has 30
  verdicts, written to I12's gate-health record; the clause's three seen cases.
- **TOOL-dWitnessedBar-30** — Items 30 (P39). Release after `verdict.flakes.release`' streak, a quarantined leg run
  at least daily whatever `verdict.held` says, a blocking CONTENDED red re-run once on a quiet host (the turnstile's
  census), a red there routed and never re-run, and an owner item past `flow.wait-ceiling`.
- **TOOL-dWitnessedBar-29** — Items 29 (NT-23, gap-test-22). Every warning a passing leg prints, in the runner's
  summary and the verdict record (`warn.<n>`), attributed to the unit that grew the file
  (`routed_commits.py --newest-unit`); a machine marker on `check-template-size.sh`'s WARN line.
- **TOOL-dWitnessedBar-7** — Items 7 (gap-test-06; FK-4-12, FK-5-2). I16: the ledger-line grammar, `test.seen-red`
  reading it beside hygiene check 23, a planted gate with no recorded red turning it red; the dScopedBuild hand-over.
- **TOOL-dWitnessedBar-21** — Items 21 (gap-test-19; night pass point 6). A fix pass's allowance less I15's files of
  the red leg, enforced at `--dispatch --writes` and `--check-commit`; a change to them routed through the tester's
  `spec-wrong` judgment to Design as a new unit; a fix pass after a failed acceptance leaving the acceptance
  commands' own files alone; seen red on a planted fix pass writing the red leg's test file.
- **TOOL-dWitnessedBar-6** — Items 6 (gap-test-02, -11, -12, -13). The backend registry under `verdict` (local hook,
  peer-node verifier, remote verdict as the `remote-ci` slot), the remote verdict's witness rule and pin as the
  clause states it, `read_held_reds` moved out of the unattended kit and registered as the remote verdict's reader;
  seen red on a swapped workflow and on a planted unregistered backend. `verdict.remote.pin` is written only by the
  owner's guarded command.
- **TOOL-dWitnessedBar-2** — Items 2. Each bypass recorded (the lander's UNGATED landing, a `--no-verify` commit the
  commit check cannot see) under `hooks.bypass`; `refused` needs the off-node witness of unit 6.
- **TOOL-dWitnessedBar-28** — Items 28 (FA-1, FA-2, FA-5; gap-test-21). A repository's legs from its overlay's leg
  rows through I3, registered at `point.flow.leg-pack` as the `adopter` pack, counted once each has its I16 record;
  pinned patches, `instructions.exclude`, the fixed set, the canary key set, widening directions and today's
  hand-added rows on an I4 `shrink-only` list; every seen case of the clause, replacing `write_gate_legs`' withhold
  and silent re-append.
