**Serves:** research TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21

# Spec brief — dPlacedRequest, the twenty-one units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dPlacedRequest/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dPlacedRequest/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every entry of "Shared interfaces", and the scout record your units cite:
   `memory/builds/dPlacedRequest/build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md` (units 1, 11-13,
   15-18, 20), `-b.md` (2-5, 9, 10, 14, 19, 21) and `-c.md` (6-8). Each holds a seam table row per clause, with
   path:line at `c63aabbb`.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, and the
`[policies]` rows the packet's Obligations list by v2 line), `B/…-coordination.md`, `B/…-orientation.md` and its
`B/…-research-orientation-*.md` records, `B/…-flow-steps.md` (the entry and probe items, `[rules]`, `[probe]`),
`B/…-flow-roles.md`, `B/…-layer-runtime.md`, `B/…-layer-memory.md`, `B/…-memory-plan.md` (`[pockets]`, `[sites]`),
`B/…-night-pass.md`, `B/…-night-pass-two.md` (NT-*), `B/…-research-scenarios-design.md`,
`B/…-research-exec-coordination.md`, `B/…-whole-audit.md` (C2-F*, A1-F5), the gap register
`B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` (each gap the packet's Gaps section names, by line) and the
fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never edit an instrument,
v2, the as-built view or the packet: the packet's Non-goals.

## The parents are specced, not built

dDeclaredLoop, this build's parent, landed its 100 specs and is DEFERRED to its build run: the loop kit `tools/loop/`,
the stage tags and item registry, the transition record, stage claims, the position engine, the review program's
`review.trigger` row, `flow.rework-budget`, `flow.wait-ceiling` and the scenarios. Its own parents are specced and
deferred too: dGroundRules (the policy file `.governance/policy.toml`, its one reader, `budgets.*` and the minimal
guard), dSafePassage (the `[[upgrade]]` and `[[retired]]` step kind), dOrderedCharter (the kinds register, the typed
build-folder record factory, the tag grammar and namespace registry, the instruction overlay) and dFairHearing (the
review harness). The chain builds them before this build's build run. So every spec here cites the parent's landed
spec by id and section, or its frozen v2 clause, as the interface, and names the call it makes; the build run
re-grounds against the landed parent. Never spec a parent's mechanism, never add a copy of `read_policy_key`, and
never invent a policy route: a policy key this build owns is declared in the catalogue the guard reads and read
through dGroundRules' reader once it lands, with the catalogue default v2 states until then, and the spec says so in
one line.

## Every spec, whatever its unit

- Path `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`; H1
  `# TOOL-dPlacedRequest-<n> — <title>`, an EM DASH, never a colon.
- Status header `DRAFT`, `rev-1`, `2026-10-25`, `node a`, `Tier-2`, `base c63aabbb`, `streams tooling`, the `order`
  verb your roster row names, and `advances TOOL-dPlacedRequest-22` (the build's own open ask; the build run's last
  unit closes it). Copy a landed sibling's line shape, e.g.
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-3.md` line 3.
- Binding lines, each at column 0 on a line of its own: `**Carries:** <Items id>@<hash8> whole`, and for the unit
  that owns a node, `**Carries:** node:<node>` (the owned-node table below). A unit carrying a clause in parts writes
  `part <k>/<n>` instead of `whole`, and every part of that clause is carried by a spec of this build.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 3, 8, 11, 15, 18, 19) still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close. The unattended kit's own self-test suites are waived for this build's
  landing (README rule 8): a criterion they would observe is amended citing that rule.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in "The units" are a scout's reading at `c63aabbb`: verify each line number against source before
  citing it.
- §8 forks: settle each by the README's rungs (the execution plan lines 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`; a `relaxes:` value joins a record with `**Bound:**`,
  `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a choice the README's
  `may: PLAY-dClosedLoop-3` grant lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave an open
  question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/`, `memory/guides/*.md` from their kit templates,
  `tools/workflows/*.js` from their `.template.js`, and the installed kickoff skill from `skills/session-kickoff/`:
  name the source as the edit and the render as its copy.
- A later build's surface named in your clause (dWellOiledMachine, dRankedPlan, dBoundRoles, dKeptSession,
  dTotalRecall) is a stand-in or a join that build arms: spec the stand-in this build ships and name the hand-over,
  never the later build's mechanism (packet Non-goals, Later builds named).
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dPlacedRequest/build/2026-10-25-build-TOOL-dPlacedRequest-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- Write nothing outside `memory/builds/dPlacedRequest/spec/` and `memory/builds/dPlacedRequest/build/`; temp files go
  under the scratch path your harness names.

### What the last three spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build will CREATE by its basename (`python lease.py …`) and keep its full path in
  §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it inside a
  quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. When you hand off to a unit another writer owns, name the token exactly as "Shared interfaces" spells
  it, and that writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours. The edge list under "Edges" is the one to declare;
  add an edge only when your spec truly reads or produces it, and say so in your return so the other writer adds the
  reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a file) owes a `**Readers:**` clause naming every reader
  by path and by value (hygiene check 25), each found by `git grep` over the tree. Check 25 reads any retirement
  word ("drops", "retired", "replaces") beside a backticked token in §2: use one only where you mean it.
- **No link-shaped text**, `[x](y)`, anywhere outside a real link, backticks included (hygiene check 2).
- **A §8 mark wraps whole.** `deviations.py` reads a `RESOLVED` mark's ruling, `widens:` and `relaxes:` from the mark
  itself: keep each mark one paragraph, with no list or blank line inside it.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` and `carries.py --report dPlacedRequest` after every writer returns.

## Owned nodes

| Node | Unit |
|---|---|
| `record-kind.lease`, `policy-key.leases`, `policy-key.leases.granularity`, `policy-key.leases.renewal`, `policy-key.leases.overlap`, `policy-key.leases.offline` | 1 |
| `record-kind.card`, `policy-key.card.follows`, `policy-key.card.store`, `policy-key.card.snapshot`, `policy-key.resume.context`, `policy-key.resume.partial` | 2 |
| `item.entry.orient`, `item.entry.place`, `item.entry.place-check`, `item.entry.place-owner`, `item.entry.claim` | 3 |
| `policy-key.placement`, `policy-key.placement.check` | 4 |
| `item.probe.trigger`, `item.probe.pin`, `item.probe.design`, `item.probe.experiment`, `item.probe.run`, `item.probe.judge`, `item.probe.judge-claimed`, `item.probe.return`, `record-kind.probe`, `record-kind.probe-trigger`, `policy-key.probe.points`, `policy-key.probe.raise`, `policy-key.probe.observations`, `policy-key.probe.experiment.authority` | 7 |
| `policy-key.leases.expiry-hours`, `policy-key.leases.queued-claim-days` | 17 |
| `policy-key.leases.offer-seconds` | 20 |
| `policy-key.patch.ratify` | 21 |

Each node is one `**Carries:** node:<node>` line, one per line, in its unit's spec.

## Shared interfaces — one spelling for every writer

Fixed so twenty-one specs by five writers agree on the interface axis (M2). Each row names its owner, the unit whose
spec defines it; every other unit names it exactly as spelled here and cites the owner. A writer who finds one wrong
says so in its return and writes a deviation record rather than a second spelling.

| # | Interface | Spelling | Owner | Source that already spells it |
|---|---|---|---|---|
| I1 | The one compare-and-swap ref writer | `write_gov_ref <ref> <expected sha or empty> <src>`, rc 0 written, 1 lost (`(stale info)` or `(fetch first)`), 2 not completed, the cause in `GOVREF_WHY`; the bounded runner passed in by name; canonical in `tools/lib/gov-ref.sh` with byte-identical inline copies in `tools/unattended/unattended.sh` and `tools/run-gates/post-merge.sh`, gated as `health_log` is | 11 | `write_claim` (unattended.sh:2396) and `write_red_ref` (post-merge.sh:273), the two hand copies it merges |
| I2 | The parented commit | `commit-tree -p <tip read>` under the fixed `gov-claim` identity; a create (empty tip) is the one parentless commit | 11 | unattended.sh:2419 |
| I3 | The verdict-file clear in the pre-push hook | the clear at `.githooks/pre-push:490` runs only when the push carries the default branch, so no `refs/gov/*` write takes a lander lock | 11 | NT-19's fold, night-pass-two:672-675 |
| I4 | The change feed | `<git-common-dir>/gov-feed.log`, one TAB line per event: `seq`, `ref`, `kind`, `blob`, `commit`, `seen-utc`; the key (ref, blob, commit) makes an append idempotent; every `write_gov_ref` call appends | 13 | memory-plan:97; the path derivation of `derive_health_log` (health-log.sh:27) |
| I5 | The lease ref grammar | `refs/gov/leases/<slug>/build`, `refs/gov/leases/<slug>/unit/<id>`, `refs/gov/leases/run/<cadence>/<period>`; `<cadence>` any segment the tag grammar admits (I7) | 1 | coordination.md:79-81 |
| I6 | The lease record message | the eight keys today's claim writes (unattended.sh:2411-2412) plus `epoch`, `kind` (`build`, `unit`, `run`), `fleet-tag`, `renews` (`yes`, `no`), `witness` (the `Gov-Transition` sha), `offer` (a fleet tag), `offer-deadline`, `last-fetch`; statuses `live held released landed aborted withdrawn`, `released` the hand-over and the last three terminal; header line `gov-claim <ref tail>` so `read_claims` stays the one reader. Unit 1 defines every key; units 16, 17 and 20 give `released`/`last-fetch`, `renews`/`witness` and `offer`/`offer-deadline` their behaviour | 1 | unattended.sh:2411-2412, :2162; STOPS.template.md §7 |
| I7 | The cadence segment | `seg := [a-z0-9][a-z0-9-]*`, at most 64 bytes, read through PLAY-dOrderedCharter-19 S1's `TAG_RE` once it lands, `RULE_KEY_RE`'s shape (tools/roles/roles_lib.py:65) as the stand-in | 18 | PLAY-dOrderedCharter-19 S1 |
| I8 | The observer clock | `read_first_seen <ref> <sha>`: the first `seen-utc` of that tip in the feed; every age (expiry, offer deadline, prune, queued-claim age) is now minus it, never the reader's clock minus the holder's stamp | 17 | v2:680, v2:1160 |
| I9 | The refusal causes | `tombstone`, `terminal`, `epoch-fence`, `live-holder`, `overlap`, `offline`, `offered`, one word per refusal line, routed by flow-steps:53-60 | 1 | flow-steps:53-60 |
| I10 | The create-only registers | `refs/gov/decisions/<build>/<key>`, `refs/gov/problems/<encoded subject>/<problem id>`; `encode_ref_segment` escapes a leading dot, `.lock`, a space, `:` and `~` | 12 | night-pass-two:331-335, memory-plan:95-96 |
| I11 | The request content key | `request_content_key`: the first 12 hex digits of SHA-256 over `derive_content_key(text)` (tools/memory-tree/row_grammar.py:1475) | 19 | `derive_section_sha` (tools/roles/handoff.py:307) for the 12-digit convention |
| I12 | The request record | `refs/gov/requests/<content key>`, its commit carrying only the key, the fleet tag and the session; the text kept on the typing node at `<git-common-dir>/requests/<content key>.md` until dWellOiledMachine publishes it redacted | 19 | v2:1862 (P40); the node-local precedent at manifest-check.sh:310-314 |
| I13 | The card ref and cache | `refs/gov/builds/<slug>/card`; the cache `<git-common-dir>/orientation/<slug>.md` keyed by the ref's object id; `manifest-check.sh --card --path` the one path reader, which `tools/hooks/scratch-guard.js` and `tools/roles/handoff.py` both call | 2 | research-orientation-preserve.md:82-84, orientation.md:322-343 |
| I14 | The pocket units | the manifest facts as level-2 instruction-unit rows under PLAY-dOrderedCharter-15's manifest, through PLAY-dOrderedCharter-20's factory, rendered by `render_card` into a `## pockets` card section | 9 | memory-plan.md:72 |
| I15 | The `seed`, `map` and `unfolds` item fields | rows in `tools/loop/item-schema.toml` in TOOL-dDeclaredLoop-24 §4's field shape: `seed` scalar of `write-set`, `scope-paths`, `question-paths`, `none`; `map` scalar of `none`, `base`; `unfolds` a set of namespace words of `tools/playbook/namespaces.toml`, `widens = "add"`. Unit 8 lands the schema rows for all three in one edit, unit 6 the role rows and the check | 8 | TOOL-dDeclaredLoop-29 S1 (the `upstream` field) |
| I16 | The seed's path list | `resolve_item_seed <item>`: repo-relative, forward-slash, deduplicated paths normalised by `resolve_ask_path` (gen_build_index.py:3185), `unarmed` for a source with no reader yet | 8 | `read_files_touched` (unattended.sh:3389) |
| I17 | The probe items, kinds and verdicts | `item.probe.trigger`, `.pin`, `.design`, `.experiment`, `.run`, `.judge`, `.judge-claimed`, `.return`; record kinds `probe` and `probe-trigger`; verdicts `confirmed`, `refuted`, `inconclusive`, `unrunnable` (verification, reproduction) and `measured`, `within-noise`, `aborted`, `unrunnable` (experiment); trigger causes `point`, `owner`, `observation`, `raised`, `reproduction`; `probe.run` and `probe.judge` call TOOL-dDeclaredLoop-17's `loop_witness.py rerun`, never a second runner | 7 | flow-steps.md:605-675; TOOL-dDeclaredLoop-17 S4 |
| I18 | The disposition set | `continue`, `amend`, `new`, `patch`, `repeat`, `unit`, `breakpoint`, `ask`, `none`, each recorded with its `reason` | 4 | flow-steps.md:124 |
| I19 | The orientation scout's return | `gov-orienter`'s `returns:` gains `disposition · reason · evidence · observations` (unit 4) and `scenarios · facts` (unit 10) | 4 | tools/roles/agents/gov-orienter.agent.md:10 |
| I20 | Disposition to scenario fact | `new` to `feature`, `amend` to `amendment`, `patch` to `patch`, `repeat` to `playbook-run`, read by TOOL-dDeclaredLoop-27 S5's `select_scenarios` | 10 | TOOL-dDeclaredLoop-27 S4 |
| I21 | The pre-claim budget draw | TOOL-dDeclaredLoop-30's `budget.py draw` with a `--request <content key>` selector; the draw rows live on the request record until a build exists | 14 | TOOL-dDeclaredLoop-30 §3 hands it here by name |
| I22 | The breakpoint firing | TOOL-dDeclaredLoop-20's `--trigger <slug> --subject <s> --cause placement`, never a new verb | 5 | TOOL-dDeclaredLoop-20 §4 |
| I23 | The claim ref and body | `refs/gov/claims/<slug>`, written through `write_gov_ref`; body keys `claimant-key`, `content-key`, `disposition`, `reason`, and on a patch `origin-slug`, `origin-sha` | 21 | flow-steps.md:127 |
| I24 | The policy reader | dGroundRules-2 S6 `resolve(key)` (`python tools/policy/policy.py get <key>`), the catalogue default of v2's row as the stand-in until it lands; `RUN_CLAIMS` stays the dark-landing switch until unit 1's migration retires it | each key's owner | dGroundRules-2 S6 |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 11 → 13, 1, 12, 15, 19, 2, 21 | `write_gov_ref` |
| 13 → 17 | `gov-feed.log` |
| 1 → 17, 16, 20, 18, 15, 19, 21 | `refs/gov/leases/<slug>/build` |
| 17 → 16, 20 | `read_first_seen` |
| 19 → 7, 4, 14, 21 | `request_content_key` |
| 9 → 2 | `## pockets` |
| 2 → 3 | `refs/gov/builds/<slug>/card` |
| 8 → 6 | `item-schema.toml` |
| 7 → 4 | `item.probe.trigger` |
| 4 → 10, 14, 5, 21, 3 | `disposition` |
| 10 → 3 | `select_scenarios` |
| 21 → 3 | `refs/gov/claims/<slug>` |

## The units

**Writer groups and build order.** The `order` value is the build order: the shared writer and its feed before every
ref that rides them, the lease grammar before the clock, tombstones, offers and cadence names that refine it, the
request record before everything keyed by its content key, the card's inputs before the card, the item fields before
the probe program, the probe trigger before the placement that routes to it, placement before the scenarios, budget,
breakpoint and claim that read its disposition, and the entry items last, once every behaviour they register
exists. The build harness splits the 21 orders into five writer groups of consecutive orders; author every unit of
your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 11 (1), 13 (2), 1 (3), 17 (4), 16 (5) |
| 2 | 20 (6), 18 (7), 12 (8), 15 (9), 19 (10) |
| 3 | 9 (11), 2 (12), 8 (13), 6 (14), 7 (15) |
| 4 | 4 (16), 10 (17), 14 (18), 5 (19), 21 (20) |
| 5 | 3 (21) |

Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **TOOL-dPlacedRequest-11** — Items 11 (gap-conc-06, gap-conc-07). I1, I2, I3: extract `write_gov_ref` from the two
  hand copies, parent every lease and claim commit on the tip it read, and move the pre-push clear so the
  `push-main-active` refusal in `write_claim`, `claim-push.lock` and push-main's `check_claim_push_clear` retire,
  each with its `**Readers:**` clause. Files touched include `.githooks/pre-push`, `tools/push-main.sh` and
  `tools/lib/gov-ref.sh`. Scout A row 2 and its Shared interfaces 2, 3 and 9.
- **TOOL-dPlacedRequest-13** — Items 13. I4: the feed appended by every `write_gov_ref` call, the bar-red write
  included, idempotent on its key, rebuilt equal from the refs; each red case the clause states. Scout A row 4.
- **TOOL-dPlacedRequest-1** — Items 1 (gap-conc-01, gap-conc-02). I5, I6, I9: the lease grammar, the epoch bumped at
  each take-over, `refs/gov/runs` claims migrated onto it behind `RUN_CLAIMS`, the acquire, renew, release and
  take-over verbs, `leases.granularity`, `leases.renewal` (`progress`, renewing only at a transition record's
  witnessed item boundary, never on a beat), `leases.overlap` (replacing the constant 0 of
  `check_cross_run_overlap`), `leases.offline` and the fleet tag from `tools/playbook/fleet.toml`; each value seen on
  its planted case. Keep the row shape of `print_claims` stable for TOOL-dDeclaredLoop-8. Scout A row 1.
- **TOOL-dPlacedRequest-17** — Items 17 (gap-conc-14). I8: expiry, the offer deadline, the prune age and the
  queued-claim age judged by the observer clock; `leases.expiry-hours`, `leases.queued-claim-days`; a beat with no
  witness renews nothing; the reader-a-day-ahead fixture red. Scout A row 7.
- **TOOL-dPlacedRequest-16** — Items 16 (gap-conc-13). A lease never deleted: release a hand-over (`released`) or
  terminal, the epoch carried across a take, a terminal build or unit refusing all but a draw on a closed root, the
  queued claim carrying its `last-fetch` and refused past `leases.queued-claim-days`, a prune that touches run claims
  only. Scout A row 6.
- **TOOL-dPlacedRequest-20** — Items 20 (gap-conc-19). `offer` and `offer-deadline`, `leases.offer-seconds`, the
  `offered` refusal class in the mode-by-class table of `check_claim_writable`, a stale take refused by the epoch
  compare-and-swap. Scout A row 9.
- **TOOL-dPlacedRequest-18** — Items 18 (gap-conc-18). I7: the cadence segment takes any tag-grammar name in place of
  the literal list at coordination.md:81. Scout A row 8.
- **TOOL-dPlacedRequest-12** — Items 12. I10: both registers create-only through `write_gov_ref` with an empty
  expected sha, the second decision on one key refused, each of the encoder's escapes seen red. Scout A row 3.
- **TOOL-dPlacedRequest-15** — Items 15 (gap-conc-12). The lander's two effect pushes (push-main.sh:978, :1128)
  carry the holder's new lease beat in one `--atomic` push under `--force-with-lease` on the lease tip read. The
  remote's support for `--atomic` is unproven (research-cloud-headless:45): spec it as the unit's first acceptance
  criterion, observed against the real remote in the build run, and spec the fail-closed fallback for a remote that
  refuses it. Scout A row 5.
- **TOOL-dPlacedRequest-19** — Items 19 (gap-conc-17). I11, I12: a request that is not yet a build as a project-level
  record any node may claim by lease, pushed with only its content key, its text kept local, relayed only by its
  record's id; the redactor `scan_secrets` (tools/runlog/runlog_lib.py:522) never bypassed. Scout B row 8.
- **TOOL-dPlacedRequest-9** — Items 9 (gap-orient-20). I14. Scout B row 5.
- **TOOL-dPlacedRequest-2** — Items 2 (gap-orient-11, gap-orient-02, gap-flow-07). I13: the card at level 1 kept as a
  ref per build, cached by build and object id, snapshotted per `card.snapshot`, the stores `card.store` selects,
  re-rendered as `card.follows` says (hooking TOOL-dDeclaredLoop-3's `write_transition`), resumed per
  `resume.context` and `resume.partial`; each value seen on its planted case. Scout B row 1.
- **TOOL-dPlacedRequest-8** — Items 8. I15 (the schema rows for all three fields), I16. The reviewer's "pinned range"
  (project-map.md:623) is a fourth seed source the clause does not list: settle it as a §8 fork by the rungs. Scout C
  row 3.
- **TOOL-dPlacedRequest-6** — Items 6. I15's `map` and `unfolds` on the role rows project-map.md:615-629 names, and
  the check that each unfold names a registered namespace. It reads neither `memory.project-map` nor
  `memory.map-unfold`, which are dBoundRoles'. Scout C row 1.
- **TOOL-dPlacedRequest-7** — Items 7 (gap-flow-18). I17: the eight probe items, the two record kinds through
  PLAY-dOrderedCharter-7 S7's factory, `probe.trigger` in the flag shape of `review.trigger` with its cause set as
  data, `probe.points`, `probe.raise`, `probe.observations`, `probe.experiment.authority`, the `probe` outcome on every
  role item, the entry-time probe keyed by I11 and filed on the request record, and a stand-in for each later part.
  Scout C row 2.
- **TOOL-dPlacedRequest-4** — Items 4 (gap-orient-01). I18, I19: `placement` and `placement.check`, a disposition for
  every request recorded with its reason, an unattended prompt placed the same way (the prompt path at
  unattended.sh:3763 calls it), the disposition carried in the claim commit until dWellOiledMachine's intake kind
  lands, and the owner-item stand-in when a placement routes to Plan or Design (C2-F7). Scout B row 3.
- **TOOL-dPlacedRequest-10** — Items 10. I19, I20: `select_scenarios` over the request's facts at `entry.place`,
  `placement.check` re-evaluating every predicate, a request no scenario admits placed under the default; red on a
  planted placement whose predicate fails. Scout B row 6.
- **TOOL-dPlacedRequest-14** — Items 14. I21: placement loops before `entry.claim` draw on a budget keyed to the
  request's content key. Scout B row 7.
- **TOOL-dPlacedRequest-5** — Items 5. I22: the `breakpoint` disposition, its witness the intake record and the
  disposition; red on a planted owner prompt to audit the specs of a build past Design's exit with no spec audit.
  Scout B row 4.
- **TOOL-dPlacedRequest-21** — Items 21. I23: `entry.claim` writes a patch or repeat build's derived plan record,
  `patch.ratify`, refusals routed by cause, the slug probe `check_slug_claimed` reused. Scout B row 9.
- **TOOL-dPlacedRequest-3** — Items 3 (gap-orient-04). The five `item.entry.*` rows through TOOL-dDeclaredLoop-24's
  item factory, each naming the verb units 2, 4, 10 and 21 ship as its body, with the orientation scout its actor;
  kickoff Step 1 stops re-deriving what the card printed. Scout B row 2.
