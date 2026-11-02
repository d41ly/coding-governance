**Serves:** research TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18

# Spec stage returns — dTendedCadence

Each agent's structured result, written from the workflow journal `wf_45791024-ea1` by script, never retyped; each long field is quoted, so a quoted line defines no id.

## dTendedCadence · TOOL-dTendedCadence-11 TOOL-dTendedCadence-13 TOOL-dTendedCadence-2 · spec-write

- agent: `a50e9531bdc85cb6a`
- authored: ["TOOL-dTendedCadence-11", "TOOL-dTendedCadence-13", "TOOL-dTendedCadence-2"]
- alreadyPresent: []
- refused: []

**summary:**

> I wrote all three specs at Tier 2, with base f4597719 and streams tooling, and committed nothing. Only TOOL-dTendedCadence-2's header carries `closes TOOL-dTendedCadence-19`; the other two have `advances`. The hygiene gate (checks 2, 12 and 25) shows one red on these files, a one-sided edge to unit 10 (see the edges list below). That gate only grades tracked files, so I ran it in a throwaway clone under %TEMP% with the build folder staged.
>
> Files:
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-11.md (order 16). Carries cl-dClosedLoop-0452@6c0e77f7 whole.
>   - A playbook declares `cycle` (daily or weekly) and `cycle_pieces` in its declaration block.
>   - check 11 of check-playbook.sh validates both keys, and a new `--cycles --at <sha>` mode lists the playbooks that declare them.
>   - Two cadence rows, `playbook-cycle-daily` and `playbook-cycle-weekly`, so each period lease acts as the once-per-cycle witness.
>   - The filer is `run_repeat_intakes` in `tools/drift-audit/playbook_cycle.py`. It goes through `item.maintain.patch`'s keyed filing, so a repeat whose last cycle is still open adds a `seen` clause instead of a second intake.
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-13.md (order 17). Carries cl-dClosedLoop-0454@ef9a7f8a whole, plus node:policy-key.maintain.security-review.
>   - A weekly `security-review` row with `events = ["landed"]`.
>   - Each review covers one range, from the last `security-head` to the landed tip, run in a scratch worktree and launched through `launch_act` as a full five-lens diff review. Only `security` findings are filed, through `item.maintain.file`; the others are counted.
>   - It introduces `tools/drift-audit/cadence_events.py` (`run_event_runs`, `EVENT_PRODUCERS`, `EVENT_WAKES`), which `every-landing` needs, called from resume-tick.sh.
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/build/2026-11-01-build-TOOL-dTendedCadence-13-deviation-131.md. The review reads each landed range once instead of the whole tree, because the harness diffs base...head and refutes any defect already present at the base. The new clause hash is 3bb6c0f8, Risk is loosening and the approver value is author-recorded.
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-2.md (order 18). Carries cl-dClosedLoop-0443@06da9bab whole, plus the nodes for maintain.host, maintain.cadence and maintain.events.
>   - The `maintain` row, with `period-key = "maintain.cadence"`.
>   - Maintain's three events added to unit 13's tables. `release-verify-failed` prints `not-installed: integrations` when integrations is absent.
>   - `session-start-breach` fires when the newest drift-history group (the source of the card's `drift —` cell) holds a dead signal.
>   - The `session-start` host row, its SessionStart fragment and the `maintain_session.py` hook.
>   - A parity check, `cadence_events.py --check`, and summaries for the three catalogue rows.
>
> New asks for the main loop to file (lettered Q and R so they don't collide with other writers' G and H):
> - **Q**, for dWellOiledMachine: a cadence row may carry `period-key`, and `derive_period` gains an `every-session` kind keyed by `GOV_SESSION_ID` (unit 2, §8 F1).
> - **R**, for dWellOiledMachine: a host row may carry `fragment`, so readiness follows the hook being wired, and `cadence.py tick --host <name>` runs only that host's rows (unit 2, §8 F2).
>
> Existing asks these specs rely on:
> - **G**, which TOOL-dTendedCadence-1 §8 F3 already states (`GOV_CADENCE_KEY`). Units 11, 13 and 2 reuse it and add no second ask.
> - **A** needs an extended accept line for unit 11: "or, for a `playbook-cycle-*` row, the playbook's `cycle` key at the landed revision". Until it lands, a cyclic repeat goes to the owner's breakpoint.
> - **D** applies to unit 11, which supplies the piece count.
>
> Edges the other writers need to add back:
> - **Unit 10:** hands-off to TOOL-dTendedCadence-13 naming `gov-maintainer`. This is a new edge and the one hygiene red.
> - **Unit 8:**
>   - hands-off to TOOL-dTendedCadence-13 and TOOL-dTendedCadence-2 naming the I7 event run key.
>   - the table's 8→11 `item.maintain.patch` edge stands.
>   - the table's 8→13 `item.maintain.patch` edge does not hold, because a security finding names no fix in `maintain.fixes`.
> - **Unit 6:** hands-off to TOOL-dTendedCadence-13 naming `maintenance-record`. Its writer must also write `security-head` on every completed review, whatever `maintain.record-when` says.
>
> Unit 15→13 and unit 1→2 already match.
>
> Disagreements to pass on:
> - **I7 wording:** I7 says the event run key passes `check_cadence_segment`, but that check covers only the cadence segment (TOOL-dPlacedRequest-18 S1). The period segment `<event>.<sha12>` is checked by `check_lease_segment` (TOOL-dPlacedRequest-1 S1), which accepts the dot.
> - **Unit 8's I6:** it must accept caller-supplied request text, so unit 11 can file a `repeat`.
> - **Event arguments:** event runs pass no `--event` or `--sha` arguments; programs read the event from `GOV_CADENCE_KEY`, in line with unit 1.

## dTendedCadence · TOOL-dTendedCadence-17 TOOL-dTendedCadence-16 TOOL-dTendedCadence-9 · spec-write

- agent: `a1c0ac69264456836`
- authored: ["TOOL-dTendedCadence-17", "TOOL-dTendedCadence-16", "TOOL-dTendedCadence-9"]
- alreadyPresent: []
- refused: []

**summary:**

> I wrote all three specs in roster order, each OPEN at rev-1, Tier-2, base f4597719. Each header carries its `order` (13, 14, 15) and `advances TOOL-dTendedCadence-19`, plus its clause's Carries line at its hash, whole, and its owned policy-key node. Nothing is committed, no index was regenerated, and I wrote no deviation records because no unit departs from its clause. My final run of hygiene checks 2, 12 and 25 exited 0 over the tree. That pass is weaker than it sounds: the one-sided edges listed below did not red it, so I would not rely on it for edge reciprocity.
>
> Files:
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-17.md
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-16.md
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-9.md
>
> **What each unit does**
> - **Unit 17 (interpreter end of life):** adds the table `tools/lib/python-eol.tsv` and a reader for it beside dSafePassage-11's floor reader. A new reading, `interpreter_floor_near_end_of_life`, opens its window on the first day of the sixth month before the end-of-life month. Under `file` it files an intake through unit 15's ask, whatever `maintain.on-breach` says. `warn` produces a "not asked" record whose note is the warning, and `off` reads nothing. It adds a new record kind, `interpreter-floor`, on the runtime layer, so the reading has an owner.
> - **Unit 16 (four node-scoped readings):** acts past `runtime.act-ceiling`, closed runs with no run record, pushed commits missing required keys, and directives never promoted. Each is filed as an ask and never becomes a leg. It also owns `maintain.node-readings`, through a node pass (`maintain.py --scope node`) and `derive_node_reading_turn`. The commit reading is repo-scoped; the other three are node-scoped.
> - **Unit 9 (retrofit heat):** a path-keeping read counter in runlog (`runlog.py reads`), and the reading `maintain.retrofit-heat` (scope node, kind `baseline`). Each period it files one sweep, the path ranked highest by reads times lifetime touches. Under `hot-first` the receipt names the standing ask (ask A). The card's fourth segment reads `reads <p>%`, and `reads not installed` where observability is absent.
>
> **New interface: the row key `route`**
> Unit 17 adds an optional key `route` to the `[[reading]]` row (I3) and builds its value `ask`. A breach from such a row is filed through `write_breach_ask` under every value of `maintain.on-breach` and is never held for the red leg. Unit 16 reuses `ask`. Unit 9 adds the value `patch`, which makes unit 3's `derive_fix_route` answer `patch` whatever the row's fix. Unit 8 owns I3 and should spell the key in its spec.
>
> **New asks for the main loop to file** (numbered by unit so they cannot collide with other writers' letters):
> - **16-1, dWellOiledMachine:** `commit_keys.py --check` should take `--repo` and `--default-tip` the way `bindings.py --check` does.
> - **16-2, dWellOiledMachine:** a cadence row declaring `per-node = true`, its lease keyed `<period>.<node>`, so every node runs it once a period.
> - **9-1, dPlacedRequest:** a patch's origin may be a ledger population.
>
> Unit 9 also cites the existing ask A.
>
> **Reverse edges other writers must add**
> - Unit 3 hands-off to unit 9 (`maintain.py`, `derive_fix_route`).
> - Unit 15 hands-off to unit 9 (`read_policy_value`).
> - Unit 2 consumes-from unit 16 (`--scope node`), and registers the per-node cadence row once ask 16-2 lands.
>
> Every other edge I declared is either in the brief's edge table, already written by its sibling (unit 1 to unit 16 on `item.maintain.lease`), or between my own units (17 to 16 and 17 to 9 on `route`). I dropped the edge to unit 1 for units 17 and 9 because I2 turned out to be unit 15's `read_policy_value`.
>
> **Defect found in unit 15's spec**
> Unit 15's policy read, `read_policy_value(root, key)`, passes the key as the second argument. The policy kit's reader-coverage scan only recognises a call whose first argument is the key literal (`READER_SHAPES`, `tools/policy/check_policy.py:423-427`). So once this build lands, that arm cannot see any owned key read this way. Either the signature should take the key first or the scan needs a new shape. My acceptance criteria grep for the `read_policy_value(root, "<key>")` form.
>
> **For unit 6**
> Two maintenance-record fields need adding to I10's grammar: `unread-nodes:` (unit 16) and `retrofit-heat: <value>/<of>` (unit 9).

## dTendedCadence · TOOL-dTendedCadence-4 TOOL-dTendedCadence-14 TOOL-dTendedCadence-18 · spec-write

- agent: `a7e25ed332fae5c14`
- authored: ["TOOL-dTendedCadence-4", "TOOL-dTendedCadence-14", "TOOL-dTendedCadence-18"]
- alreadyPresent: []
- refused: []

**summary:**

> I wrote all three specs in my group, in roster order. Each is a Tier-2 spec with status `OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order <k> · advances TOOL-dTendedCadence-19` and carries its clause whole. Nothing is committed and I did not run the index generator. The only gate I ran was `check-memory-hygiene.sh --only 2,12,25` over the final files: exit 0, no findings. I wrote no deviation records because none of the three departs from its clause.
>
> Files, all under C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/:
> - 2026-11-01-spec-TOOL-dTendedCadence-4.md — order 4, carries `cl-dClosedLoop-0445@768c9f5b` and `node:policy-key.maintain.reading-admission`
> - 2026-11-01-spec-TOOL-dTendedCadence-14.md — order 5, carries `cl-dClosedLoop-0455@238dcec0` and `node:policy-key.maintain.tiers`
> - 2026-11-01-spec-TOOL-dTendedCadence-18.md — order 6, carries `cl-dClosedLoop-0499@2480b868` and `node:policy-key.maintain.reading-tree` and `node:policy-key.maintain.dead-after`
>
> **Unit 4.** Admission runs in drift_report.py, right after each reading is paired with its pin (`:4327`). It adds `derive_reading_owner`, `read_record_layers` and `check_reading_admission`, with three verdicts: `admitted`, `unowned` and `refused`. The spec tables what each of the 27 readings has as a pin today. Five have none (fact-question F2): `dangling_pointers_in_own_ledger`, `lexicon_marginal_offense_rate`, `live_backlog_rows_per_shard`, `open_asks_cited_by_product_source` and `live_builds_without_activity`. Under F1 their tolerance becomes 0, and gov gets a pin at each one's measured value. It also defines drift-audit's `read_policy_value(key, root, rev=None)` and `PolicyRefused`, following PLAY-dOrderedCharter-7 §4.
>
> **Unit 14.** It adds `derive_reading_band` and `run_band_probe`. The bands are `in-pin`, `log`, `diagnose` and `act`; the walk routes an unowned or refused reading down the log band, so nothing is filed for it. At landing every gov reading gets `edges = [0, 0]` (F4), so no response changes. The diagnose band depends on ask C (F3).
>
> **Unit 18.** It extracts the factory as a `tools/lib/signal_leg.py` block with a parity row. The five signals move to:
> - memory: tools/memory-tree/memory_signals.py
> - flow: tools/loop/flow_signals.py (F1: TOOL-dDeclaredLoop-1 S1 specs the loop kit with `layer.flow`)
> - instruction: tools/playbook/instruction_signals.py
>
> Each home gets two legs (signals and selftest), and the bounds move into ledger populations in the homes. `handkept` now reads a `[[handkept]]` descriptor table (F2, which the grant allows). The flow signals' declarations, including `PRODUCT_GLOBS`, move to `tools/loop/flow_layer.py`. The `drift-audit records` leg stays and keeps all its readers (F4). Two mechanisms are added: `resolve_reading_tree`, and a `--readings` pass that runs the base's own engine (F5). `maintain.dead-after` replaces `DEFAULT_DEAD_READINGS_LIMIT`; `DEAD_FILED` stays for unit 15 to retire.
>
> **Interfaces I changed from the brief's proposals:**
> - **I8:** the edges go on the `[[reading]]` row, not on `drift-pins.txt`. A ledger row's count must be a positive integer, so the 14 readings with a pin of 0 have no `drift-pins.txt` row to hold them.
> - **I9:** the log line is the existing drift-history row, unchanged. Adding a `band` column would make every node's existing history file unreadable, because the reader rejects a header missing a required column. `ev=reading` is not an event the journal accepts either.
> - **I12:** the factory checks bounds but does not apply ratchets; the `ratchet` pack already guards raises.
>
> **Edges.** Every pair is already matched except these:
> - 18 → 5, 12 and 16 hand off `maintain.reading-tree`. Those writers' specs must say `consumes-from TOOL-dTendedCadence-18` and spell that token.
> - Unit 1 already consumes from 14 and 18, so those pairs match.
> - I added no new edge that another writer has to answer.
>
> **Asks:** only C (for 14) and F (for 18). There are no new ones.
>
> **Problems I found in specs other writers already wrote:**
> - Unit 15's S6 defines its own `read_policy_value(root, key)`, a second copy in the same kit. With `root` first, the policy kit's reader-coverage check will not count the call, and the close will fail on unit 15's keys. It should call unit 4's adapter as `read_policy_value("<key>", root)`.
> - Under `maintain.tiers: pins`, unit 15 calls the band `pin`, but unit 1 and unit 14 call it `act`.
>
> **A parent-spec problem, not needed for these clauses:** TOOL-dWitnessedBar-13's ledger rows require a positive count. TOOL-dWitnessedBar-16 moves the existing pins of 0 into `drift-pins.txt` rows, which therefore cannot be written.
>
> **Decisions for the commit trailers:**
> - Admission runs in the engine's pin join, where a refused reading fails `--check`.
> - The five readings that had no pin get tolerance 0, plus a gov pin at the measured value where that value is above 0.
> - Edges `[0, 0]` at landing.
> - The leg-pack homes are memory-tree, loop and playbook.
> - `drift-audit records` stays.

## dTendedCadence · TOOL-dTendedCadence-15 TOOL-dTendedCadence-1 TOOL-dTendedCadence-3 · spec-write

- agent: `abcafde4563c4dcee`
- authored: ["TOOL-dTendedCadence-15", "TOOL-dTendedCadence-1", "TOOL-dTendedCadence-3"]
- alreadyPresent: []
- refused: []

**summary:**

> I wrote all three specs, Tier-2, in the shape TEMPLATE-SPEC.md gives. Nothing was committed and the index was not regenerated. The hygiene gate (`--only 2,12,25`) exits 0, but it only grades tracked files, so it did not grade these untracked specs. I checked edge reciprocity myself by reading the spec folder, and five one-sided edges remain (listed below).
>
> Files:
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md (order 7, advances -19)
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md (order 8, advances -19)
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-3.md (order 9, advances -19, closes TOOL-dTendedCadence-20)
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/build/2026-11-01-build-TOOL-dTendedCadence-1-deviation-11.md (deviation record, not committed)
>
> Main choices, each one a §8 fork marked RESOLVED (agent, delegated, rung 1 or 3, widens and relaxes both none):
> - Unit 15 (`maintain.file`): under `file-ask` the ask goes in as a cadence intake that Entry places as an `ask`. No backlog row is written directly and no ask id is minted, because no build is Maintain's and a run may not open one (`gen_build_index.py:4123`). A repeat adds a `seen` clause to the placed ask, or a receipt to the intake. No `SEV` row is written. The red leg `maintain breach record` (`pack = "maintain"`) is always declared and prints `not asked` unless the value is `red-leg`. It reads the record through unit 6's `read_newest_record`, and with no committed record it is a dead probe. `report` uses the ask B sender.
> - Unit 1 (the Maintain program): six `[[item]]` rows in `tools/drift-audit/kit.toml`, walked in `needs` order by `maintain.py` inside `run_cadence_period`. Recipe mode is rejected, citing research-maintain:97-108, walkthrough:686-687 and coordination:48. Readings come from `drift_report.py --readings`, bands from unit 14 (`run_band_probe`). Unit 6 hands this unit the job of committing the maintenance record; the walk commits nothing and instead files a records-only patch intake for each written record (F4).
> - Unit 3 (the safe fixes): the `maintain.fixes` catalogue row becomes a closed `of` set with a literal default. A refused read applies no fix. Routes: `reap` and `prune landed` direct, three fixes by patch, `defer dormant` by `--dormant` plus `dispose`. It adds two node-scoped readings, `idle_processes_past_ceiling` and `landed_branches_unpruned`, so the direct fixes have something to clear.
>
> New asks for the main loop to file (letters A to F already exist; E and B are cited):
> - **G**, for dWellOiledMachine: `run_cadence_period` sets `GOV_CADENCE=<cadence>` and `GOV_CADENCE_KEY=<period key>` in its argv's environment. Accept: a stub argv run by `cadence.py run nightly-audit --period 2026-W44 -- <stub>` prints `nightly-audit 2026-W44` from its environment.
> - **H**, for dDeclaredLoop: `position.py` answers a cadence program's next item keyed by (cadence, period). Accept: a fixture program of two items, the second needing the first, is answered first-then-second across two wakes of one period, and the supervisor runs the answer.
> - Ask E applies: `read_items` reads only `tools/loop/loop.toml`, and `check_program` needs a `[[step]]` exit row that a cadence program does not have.
>
> Cross-writer fixes needed. These are edits to other writers' specs, which I did not make:
> 1. Unit 4 needs a hands-off to units 1, 3 and 15 for `read_policy_value`. All three now call unit 4's `read_policy_value(key, root)` and `PolicyRefused` instead of a copy of their own.
> 2. Units 9, 16 and 17 cite `read_policy_value` as unit 15's, with the arguments in the order `(root, key)`. They should cite TOOL-dTendedCadence-4 and use `(key, root)`. Unit 9's consumes-from on unit 15 is then one-sided.
> 3. Unit 16 needs a consumes-from on unit 3 for `act-direct`: its node pass must route a node-scoped reading with a direct fix to `item.maintain.direct`, or reap and prune never run.
> 4. Units 8 and 14 disagree about where band `edges` live. Unit 8's row allows eight keys and puts edges on `drift-pins.txt`; unit 14 adds `edges = [e1, e2]` to the `[[reading]]` row. My specs only say "where -8 and -14 place them".
> 5. Unit 6 says the Maintain program commits the record. Unit 1 (F4) files a patch intake for it instead, so unit 6's edge text may want rewording.
>
> Edges I added beyond the brief's table: 15 consumes from 4; 15 hands off to 1 and 3; 1 consumes from 4, 14, 15 and 18; 1 hands off to 16; 3 consumes from 4 and 15; 3 hands off to 5, 9 and 16. Of these, 1, 3 and 15 to 4, and 3 to 16, have no matching edge yet. The other units already declare theirs back.

## dTendedCadence · TOOL-dTendedCadence-7 TOOL-dTendedCadence-5 TOOL-dTendedCadence-12 · spec-write

- agent: `a1fe24ba2ecf9f388`
- authored: ["TOOL-dTendedCadence-7", "TOOL-dTendedCadence-5", "TOOL-dTendedCadence-12"]
- alreadyPresent: []
- refused: []

**summary:**

> I wrote all three specs in my group, in roster order, and committed nothing. They are under C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/:
> - 2026-11-01-spec-TOOL-dTendedCadence-7.md (order 10)
> - 2026-11-01-spec-TOOL-dTendedCadence-5.md (order 11)
> - 2026-11-01-spec-TOOL-dTendedCadence-12.md (order 12)
>
> Each one is Tier-2, OPEN, rev-1, base f4597719, `advances TOOL-dTendedCadence-19`, and carries its clause whole. None of the three owns a node. The hygiene gate (`--only 2,12,25`) prints nothing against these files. I wrote no deviation record and found no new ask.
>
> **TOOL-dTendedCadence-7 (the dead-pointer detector).**
> - A new module, `tools/drift-audit/dead_pointers.py`, holds both populations, and each keeps its own oracle:
>   - Auto-memory notes use the tracked-set test. `signal_dangling_pointers` moves into the module, and `drift_report.py` re-imports it so existing callers still resolve.
>   - Text outside `memory/`, map dossiers and gotcha pages use the history needles. This half reads a new `check-dead-paths.sh --offenders` mode. `--check` output does not change.
> - The leg keeps its name. Its argv becomes `dead_pointers.py --leg`, which bounds the result at 0 through `run_signal_leg` and gets `pack = "maintain"` on its `[[exempt_leg]]` row.
> - There are two `[[reading]]` rows:
>   - The text reading has `kind = "code"`.
>   - The auto-memory reading has scope `node` and no kind, so its owner derives as Runtime, as unit 4 S1 says.
>   - Both get `drift-pins.txt` entries at count 0 with `edges 0/0`.
>
> **TOOL-dTendedCadence-5 (map freshness).**
> - The reading uses `measure_dossier_staleness` as TOOL-dTotalRecall-8 S12 changes it.
> - `build_stale_dossiers` detail rows are cut down to `dossier`, `feature` and `refreshed`. Today the offender key changes with every commit that touches a dossier's paths, which would file a second patch while the first is still open.
> - The row declares `kind = "dossier"` and `fix = "regenerate stale"`.
>
> **TOOL-dTendedCadence-12 (bundle members whose code moved under an unchanged head line).**
> - New `annotations.py behind --json` verb: for each `gov:note`, the head commit comes from `git blame`. A definition span is checked by body hash; a `gov:end` span by `git log -L` over its lines.
> - New drift-audit reading `notes_older_than_their_code`, with `kind = "annotation-index"`.
> - `check_body_moved` is extracted at its second caller, and `measure_dossier_staleness` is re-pointed at it.
>
> **For the main loop to reconcile:**
> 1. **The `check_body_moved` home changed.** I16 proposed `code_record.py`. I put the helper in the `extract_code` block (canonical `tools/lib/extract_code.py`, plus its kit copies) because codebase-map may not import memory-tree, so `map_lib.py` could not call it there. Unit 12 §8 F1 records this.
> 2. **I disagree with unit 4 S5 on the auto-memory pin.** Unit 4 says `dangling_pointers_in_own_ledger` "takes no gov entry". Unit 7 §8 F3 gives it a `drift-pins.txt` entry at 0 with `edges 0/0`. Without that entry, band admission refuses the reading and gap-orient-10 stays report-only. A 0 bounds no node wrongly, and unit 16 does the same for its readings.
> 3. **Edges I added beyond the table:**
>    - Unit 5 consumes from TOOL-dTendedCadence-3 for `regenerate stale`. Unit 3 already declares the matching hands-off.
>    - Units 7 and 12 use I8 `edges` in prose only, with no §3 edge to unit 14.
> 4. **Things unit 18's writer should confirm:** that `run_signal_leg` exits 1 on a dead gateable signal, and that `maintain` is an accepted `pack` value.
> 5. **Edges that are one-sided until other specs land:** the specs for units 8 and 18 were not on disk when I finished. Each needs a hands-off to 7 (`[[reading]]`, `run_signal_leg`, `maintain.reading-tree`), to 5 (`[[reading]]`, `item.maintain.patch`, `maintain.reading-tree`) and to 12 (`[[reading]]`, `maintain.reading-tree`). Unit 15's hands-off to 7 and 12 and unit 3's to 5 already match.

## dTendedCadence · TOOL-dTendedCadence-10 TOOL-dTendedCadence-6 TOOL-dTendedCadence-8 · spec-write

- agent: `a3970c9fb73a1a44e`
- authored: ["TOOL-dTendedCadence-10", "TOOL-dTendedCadence-6", "TOOL-dTendedCadence-8"]
- alreadyPresent: []
- refused: []

**summary:**

> I wrote all three specs in my group, in roster order. Each is a Tier-2 spec with status OPEN, rev-1, base f4597719, node a, its order verb (1, 2, 3) and `advances TOOL-dTendedCadence-19`. Nothing is committed, the index was not regenerated, and I wrote nothing outside spec/. I wrote no deviation records and no unit briefs: no unit departs from its clause, and briefs are outside my write scope.
>
> Checks run: hygiene `--only 2,12,25` exits 0 with no finding on these files, and every new function name got OK from lexicon `--suggest` (two refused names were renamed). Each spec is under 31 KB. Paths named in the acceptance criteria are either tracked at HEAD or written as bare file names.
>
> Files:
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-10.md
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-6.md
> - C:/projects/coding-governance/.claude/worktrees/unattended-dtendedcadence-e82dac/memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-8.md
>
> **TOOL-dTendedCadence-10** (the maintainer's definition)
> - Defines `gov-maintainer` in the roles kit: layer observability, item role, writes nothing, read-only tools, a new `maintain` workflow, and a house overlay.
> - Adds one new check to `check_layer_roles`: an expansion row registers a slot that has no role file. It only applies where a kit descriptor joins that layer, so `gov-deployer` just prints a note.
> - The base tables `BODY_CEILINGS` and `WORKFLOW_NAMES` versus their dBoundRoles replacements is settled by a probe at build time (§8 F6).
> - Uses the PLAY-dClosedLoop-3 grant for the regenerated charter roster line.
>
> **TOOL-dTendedCadence-6** (the maintenance record and the run record)
> - Source differs from the scout record: the driver already writes the run record at `--close` and `--abort`, right after its own end line (unattended.sh:14281-14361). The agent-instructed step is a leftover, so this unit finishes the move rather than starting it.
> - The run-record writer now reads `observability.run-record`, writes only when the journal shows a closing end line, and gains four anomaly kinds: `refusal`, `ceiling-breach`, `dead-probe`, `red-bar`.
> - The driver also writes at `--landed` under primary. The instructed step is removed from the VERBS and SKILL templates and their renders, with a Readers clause and the grant.
> - New `tools/drift-audit/maintenance.py` for the maintenance record, kept in `<MEMORY_ROOT>/maintenance/` under the grant.
> - I refined I10 as its owner:
>   - the record has three `**Key:**` fields (Key, Base, Read);
>   - then lowercase I10 lines at column 0: `log-band:`, `security-head:`, `retrofit-heat:`, `unread-nodes:`, and `over-pin:` lines. These match how units 9, 13, 15 and 16 already spell them.
> - The newest-record reader uses unit 15's F3 rule, so the two agree on which record is newest.
>
> **TOOL-dTendedCadence-8** (readings, keys, patch intakes, event keys)
> - I refined I3 as its owner: `name` and `scope` (repo, node or outside) are required. `layer` defaults to the descriptor's and `pin` to the reading's name. I added `route`, as unit 17 asked. `edges` and `live` are accepted as keys whose rules are units 14 and 18's.
> - A both-ways check between the rows and the signals `SIGNALS` emits rides `--check` and `--offenders`.
> - New `--readings` output keys every reading that is over its pin.
> - Patch intakes have stable text, so a repeat becomes a receipt on the same intake; ask A applies.
> - I7 correction: `check_cadence_segment` only grades the `maintain` segment. The `<event>.<sha12>` part is checked by `check_lease_segment` instead.
>
> **Edges added beyond the brief's table**, each matching a consumes-from the sibling already declares:
> - 8 → TOOL-dTendedCadence-2 and 8 → TOOL-dTendedCadence-13, both for the event key `<event>.<sha12>`; unit 13 says it never calls the patch intake.
> - 10 → TOOL-dTendedCadence-13, for `gov-maintainer`.
>
> **For the main loop to reconcile** (no new asks; only ask A is cited):
> 1. TOOL-dTendedCadence-13 S4 has `gov-maintainer` run the `tier2-review.js` workflow. That needs a `Workflow` tool this definition does not grant (unit 10 §3 and F4).
> 2. TOOL-dTendedCadence-17 puts `edges 0/0` on the `drift-pins.txt` row, but TOOL-dTendedCadence-14, which owns I8, settled `edges` as a key on the reading row.
> 3. TOOL-dTendedCadence-7 declares a row for `dangling_pointers_in_own_ledger`, which unit 8 already creates among the 27 rows. It should extend that row, since unit 8's check refuses the same name twice.

## dTendedCadence · specs · commit

- agent: `ad75a73aa3fc92c3f`
- committed: false
- sha: "7e48dac37d0c4e7f93cba2ef22e6e4fa518d16c5"
- specs: [{"id": "TOOL-dTendedCadence-10", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-10.md"}, {"id": "TOOL-dTendedCadence-6", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-6.md"}, {"id": "TOOL-dTendedCadence-8", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-8.md"}, {"id": "TOOL-dTendedCadence-4", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-4.md"}, {"id": "TOOL-dTendedCadence-14", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-14.md"}, {"id": "TOOL-dTendedCadence-18", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-18.md"}, {"id": "TOOL-dTendedCadence-15", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md"}, {"id": "TOOL-dTendedCadence-1", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md"}, {"id": "TOOL-dTendedCadence-3", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-3.md"}, {"id": "TOOL-dTendedCadence-7", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-7.md"}, {"id": "TOOL-dTendedCadence-5", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-5.md"}, {"id": "TOOL-dTendedCadence-12", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-12.md"}, {"id": "TOOL-dTendedCadence-17", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-17.md"}, {"id": "TOOL-dTendedCadence-16", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-16.md"}, {"id": "TOOL-dTendedCadence-9", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-9.md"}, {"id": "TOOL-dTendedCadence-11", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-11.md"}, {"id": "TOOL-dTendedCadence-13", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-13.md"}, {"id": "TOOL-dTendedCadence-2", "path": "memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-2.md"}]
- checklist: ""

**why:**

> The build-index generator refused. `python -B tools/memory-tree/gen_build_index.py --write` exited 1, and set -e stopped the block before the second stage and before the commit. Its output, verbatim: "build-index: memory/builds/dTendedCadence/README.md: front matter declares 'status: OPEN' but 18 spec(s) carry a status header — the build status is DERIVED from them, and two answers to one question is exactly the drift this index removes. Delete the 'status:' key." Before the refusal, git printed CRLF-to-LF warnings for the working copies of the TOOL-dTendedCadence-1, -15 and -3 specs. State left behind: HEAD is unchanged at 7e48dac37d0c4e7f93cba2ef22e6e4fa518d16c5. The 18 specs are staged as additions, from the block's first `git add`. Nothing else is staged, and no generated view was written. The two untracked foreign deviation files under memory/builds/dTendedCadence/build/ were not touched. Fixing this means deleting the `status:` key from the build README's front matter. That README is not a spec and is outside this stage's write set, so I did not edit it and did not retry. Once it is fixed, the block can be re-run as is, because a repeat `git add` of the staged specs does nothing. A first attempt that passed the block inline through a heredoc failed with a shell parse error (unexpected EOF looking for a matching quote) before any line ran, and I confirmed it had staged nothing. The block was then run unmodified as ONE bash process from C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dtendedcadence-e82dac/d0ebabbc-fb8a-4ad6-a3f0-13d769046272/scratchpad/spec-commit.sh. The gotchas checklist (step 6) did not run, because no commit was made.

**summary:**

> Not committed: the build-index generator refused because memory/builds/dTendedCadence/README.md declares 'status: OPEN' in its front matter while 18 specs carry status headers. HEAD is unchanged at 7e48dac37. The 18 specs are staged as additions and no views were rendered. To unblock, delete the README's `status:` key, then re-run the block unchanged.
