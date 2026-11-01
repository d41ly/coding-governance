**Serves:** research KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28

# Spec brief — dKeptSession, the twenty-eight units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dKeptSession/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dKeptSession/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every row of "Shared interfaces" and "Edges", and the scout record your units
   cite: `memory/builds/dKeptSession/build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md` (units 1-4, 16,
   19, 20), `-b.md` (5, 6, 10, 21-25, 27, 28) and `-c.md` (7-9, 11-15, 17, 18, 26). Each holds a seam row per clause
   with path:line at `f8906bce8`, and a list of places where a parent spec and source disagree.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, the `[policies]`
rows the packet's Obligations list by v2 line, and the preset table at v2:1409-1722), `B/…-coordination.md` (items
6-8, the message kinds at :110-112), `B/…-orientation.md` (OR-*), `B/…-compaction-results.md` (CX-*),
`B/…-layer-runtime.md` (RT-1), `B/…-flow-roles.md` (FR-*), `B/…-flow-interactions.md` (FI-*), `B/…-night-pass.md`,
`B/…-night-pass-two.md` (NT-*), `B/…-project-map.md` (CS4-F1), `B/…-away-pass.md`, the gap register
`B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` (each gap the packet's Gaps section names, by line), the
prior-art checker `B/2026-10-19-build-PLAY-dClosedLoop-1-preset-check.py`, and the fork rungs in
`B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never edit an instrument, v2, the
as-built view or the packet: the packet's Non-goals.

## The parents are specced, not built

dDeclaredLoop and dPlacedRequest, this build's parents, landed their specs and are DEFERRED to their build runs.
dDeclaredLoop owns the loop kit `tools/loop/` (stage tags, item registry `loop.toml`, the transition record and its
writer `loop_transition.py`, the position engine `position.py`, breakpoints, dispositions, scenarios, `budget.py`,
`flow.wait-ceiling`, `flow.rework-budget`, the `[[stand-in]]` rows, `next`'s stand-in). dPlacedRequest owns
`build_gov_commit` and `write_gov_ref` (`tools/lib/gov-ref.sh`), the change feed `gov-feed.log`, the lease grammar
and its declared clock (`read_first_seen`, `check_deadline_passed`), `resolve_fleet_tag`, the build card ref
`refs/gov/builds/<slug>/card` with `print_replay`'s `resume —` line and `resume.context`. Their own parents are
specced too: dGroundRules (the policy file `.governance/policy.toml`, `tools/policy/catalogue.toml`, the one reader
`resolve` in `tools/policy/policy.py` with `RESOLUTION_ORDER`, the JS mirror `readPolicy`), dOrderedCharter (the
kinds register, the record factory, the charter renderer, `PRESET_LINE_PENDING`), dSafePassage and dFairHearing.
None of `tools/loop/`, `tools/policy/` or `tools/lib/gov-ref.sh` exists at HEAD. dGroundRules' kit is built on its
own branch, `branch/unattended-dgroundrules-e47ae1`, and not landed: scout A read it there and marks those cites
`GR:`; cite them by the spec id and section, and the build run re-grounds on the landed bytes.

Two facts about the tree since this run's base `462d20f3`: origin's main is at `e5de11e9e`, where dDeclaredLoop's
landing re-grounded 20 of its specs against dOrderedCharter's landed specs. When you cite a dDeclaredLoop spec,
read it as `git show origin/main:<path>` and cite the section that stands there; this branch takes those bytes at the
close's reconcile.

So every spec here cites the parent's spec by id and section, or its frozen v2 clause, as the interface, and names
the call it makes. Never spec a parent's mechanism, never add a copy of `resolve`, `write_gov_ref` or a card writer,
and never invent a policy route: a key this build owns gets its catalogue row through
`python tools/playbook/core.py new policy-key <name> … --owner dKeptSession` (TOOL-dDeclaredLoop-6 S4) and is read
through the reader of its language (I8), with the catalogue default v2 states until that reader lands, said in one
line.

## Every spec, whatever its unit

- Path `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-<n>.md`; H1
  `# KICK-dKeptSession-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order <k> ·
  advances KICK-dKeptSession-29`, with `<k>` your unit's order below. `OPEN` is the status token: `DRAFT` is not in
  `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py`). The shape is
  `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md` line 3.
- Binding lines, each at column 0 on a line of its own under the status line:
  `**Carries:** <Items id>@<hash8> whole`, and for a unit that owns a node, `**Carries:** node:<node>` (the owned-node
  table below). A unit carrying a clause in parts writes `part <k>/<n>` instead of `whole`, and every part is carried
  by a spec of this build.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 3, 4, 6, 15, 19, 20, 22, 23, 26, 28) still names its key words in backticks where they
  are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close. "Seen on strict's value" means the planted policy file names
  `preset = "strict"` and the case reads the key's strict cell from I1, the third column of v2:1478-1562.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `f8906bce8`: verify each line number before citing it.
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
- A later build's surface named in your clause (dTotalRecall, dWellOiledMachine, dIndexedDesign, dFurnishedOrders,
  dShippedRelease, dWitnessedBar) is a stand-in or a join that build arms: spec the stand-in this build ships and
  name the hand-over, never the later build's mechanism (packet Non-goals, Later builds named). Register a stand-in
  as a `[[stand-in]]` row (TOOL-dDeclaredLoop-13 S8).
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dKeptSession/build/2026-10-26-build-KICK-dKeptSession-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- A parent spec that must change for your clause to hold (scout B's disagreement 2, the lease's renewal witness;
  the scouts' note that TOOL-dDeclaredLoop-7 S4 names dWellOiledMachine where the mailbox is this build's) is never
  edited: state the needed change in §8 as an ask for that build, its target build, its accept line, and your
  return names it. The main loop files every such ask once, after the writers return, so no two writers mint an id
  in one foreign family (PLAY-dClosedLoop-32).
- Write nothing outside `memory/builds/dKeptSession/spec/` and `memory/builds/dKeptSession/build/`; temp files go
  under the scratch path your harness names.

### What the last four spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python presets.py …`) and keep its
  full path in §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it
  inside a quoted literal.
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
  one only where you mean it.
- **No link-shaped text**, a bracketed label followed by a parenthesised target, anywhere outside a real link,
  backticks included (hygiene check 2).
- **A §8 mark wraps whole.** `deviations.py` reads a `RESOLVED` mark's ruling, `widens:` and `relaxes:` from the mark
  itself: keep each mark one paragraph, with no list or blank line inside it.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` and `carries.py --report dKeptSession` after every writer returns.

## Owned nodes

| Node | Unit |
|---|---|
| `policy-key.preset` | 1 |
| `policy-key.card.pointers` | 13 |
| `policy-key.context.on-full`, `policy-key.context.threshold` | 14 |
| `policy-key.orient.budget` | 9 |
| `record-kind.mailbox-message` | 5 |
| `policy-key.mailbox.reads` | 10 |
| `item.mailbox.answer` | 25 |
| `policy-key.mailbox.notice`, `policy-key.mailbox.fetch-seconds`, `policy-key.deps.messaging` | 21 |
| `policy-key.deps.coordination`, `policy-key.deps.early-build` | 7 |
| `policy-key.actions.free` | 8 |
| `policy-key.notify.owner` | 11 |
| `policy-key.attendance` | 17 |

## Shared interfaces — one spelling for every writer

Fixed so twenty-eight specs by five writers agree on the interface axis (M2). Each row names its owner, the unit whose
spec defines it; every other unit names it exactly as spelled here and cites the owner. A spelling marked
"proposed" has no source yet; the owner may refine it in its spec, and says so in its return. A writer who finds one
wrong says so in its return and writes a deviation record rather than a second spelling.

| # | Interface | Spelling | Owner | Source |
|---|---|---|---|---|
| I1 | The preset store | `tools/policy/presets.toml`, one `[preset.<name>]` table per shipped preset (`velocity`, `standard`, `strict`, `guarded`) with quoted dotted keys, `never = [...]` (the keys presets never touch, the floor and `preset` itself), `pairs = [[<higher>, <lower>], …]` (`review.max-rounds` above `review.design.round-count` among them); a repository preset as `[presets.<name>] extends = "<shipped>"` in `.governance/policy.toml`; validated with GR `check_value(row, value)`, never a second allowed-value parser (proposed) | 1 | v2:1409-1447, v2:1474; `preset-check.py:30-72` |
| I2 | The preset kind | `kind.preset`, its `core-pending.txt` row filled, factory `python tools/playbook/core.py new preset <name>` | 1 | TOOL-dDeclaredLoop-6 S10; PLAY-dOrderedCharter-7 S6 |
| I3 | The absent-expansion refusal | `[[selects]]` rows `{key, value, point}` in `tools/loop/loop.toml`, judged by `check_expansion_value(key, value)`; `build.closes` rows added so `strict` and `guarded` refuse it on a core-only install | 1 | TOOL-dDeclaredLoop-2 S8 |
| I4 | The reader's preset step | one step in GR `RESOLUTION_ORDER` (`tools/policy/policy.py`) between the file and the default, signature `(path, row, table, rev_phrase)`, answering with source `preset`; the not-applied clause and the fixture case asserting it rewritten in the same unit; the build a read is for carried on the read dict as `read["build"]` (proposed) | 2 | TOOL-dGroundRules-3 S3; GR `policy.py:701-710` |
| I5 | The charter preset section | `python tools/policy/policy.py preset --diff` printing the preset's name and only the keys that differ from it; placeholder `PRESET_SECTION` with probe `preset_section` in `tools/govkit/entries/playbook.kit.toml`; the same verb fills PLAY-dOrderedCharter-4's `PRESET_LINE_PENDING`, never a second preset line (proposed) | 3 | `derive_role_roster` (`tools/playbook/render_playbook.py`); PLAY-dOrderedCharter-4 S2 |
| I6 | The intake answer | token `{preset}` in the policy kit's `[adopt] argv`, recorded by `cmd_intake` under deploy.toml's `[answers]` as `preset`, written by `render_scaffold` as the policy file's top-level `preset`; never deploy.toml's `[policy]` table, which the deployer owns | 4 | `tools/govkit/govkit.py` `needed_answers`, `cmd_intake` |
| I7 | The shrink-only list factory | `write_shrink_list` (with its `check_shrink_list` reader), one derive, check-against-base and write helper extracted from GR `check_list`/`write_list` at their third instance, its base read through `resolve_compare_base` (proposed) | 19 | GR `policy.py:991-1031` |
| I8 | The policy readers, one per language | Python `resolve(key)` (TOOL-dGroundRules-2 S6, `python tools/policy/policy.py get <key>`); shell `read_card_policy <key>` (TOOL-dPlacedRequest-2 S11) or `policy.py get` for kit shell; JS `readPolicy(key, {repo})` (TOOL-dGroundRules-5 S5); a refusal reads the catalogue default with one NOTE | each key's owner | as cited |
| I9 | The scenario's preset slot | `preset = "<name>"` and `overrides = { "<key>" = <value> }` on a TOOL-dDeclaredLoop-27 S3 scenario row, inherited through `extends`; read by a step after the file's own values in I4's order, for the builds whose transition record names the scenario (proposed) | 20 | TOOL-dDeclaredLoop-27 S3, S8 |
| I10 | The replay lines | `print_replay`'s order: `card —`, `route —`, `resume —`, `partial —` (TOOL-dPlacedRequest-2 §4), then `position — <answer> · next <item tag>`, then `context — <n>% of window · past <threshold> · fresh at next item boundary (context.on-full: <value>)` (proposed) | 12 | `skills/session-kickoff/manifest-check.sh` `print_replay` |
| I11 | The card's pointers | a `## pointers` card section written by `manifest-check.sh --card --pointers --build <slug>` (a member of TOOL-dPlacedRequest-2's `--card --publish/--follow/--lookup` family, under `CARD_CAP_BYTES`), lines `records — <tag> <path> …`, `forks — <spec path>§8 F<n> … · none`, `item — <instance key> · none`, `budget — <budget_state answer>` (unit 26), `mail — <unread ids> · none` (unit 5) (proposed) | 13 | v2:1240; TOOL-dPlacedRequest-2 S1, S4 |
| I12 | The item boundary | `derive_item_boundary` in `tools/loop/position.py`: the point where TOOL-dDeclaredLoop-7's `act` answer names an instance key (`<item tag>@<round·pass>#<inputs>`, TOOL-dDeclaredLoop-7 S3) other than the card's `item —` pointer; every item-boundary read (pointers, context, `actions.free`, `mailbox.reads`, `mailbox.notice`) calls it (proposed) | 13 | TOOL-dDeclaredLoop-7 S3, S4 |
| I13 | The context fill | `measure_context_fill <transcript>`: the share of the window the last turn used, input plus cache read plus cache write over a pinned window constant, extracted from `tools/runlog/extract.py` `measure_ready_tree` and imported by both readers, never copied (proposed) | 14 | `tools/runlog/extract.py:1231` |
| I14 | The recipient grammar | `build:<slug>`, `unit:<id>`, `node:<fleet tag>`, `project`; checked by `check_mail_recipient`, a `node:` tag against `resolve_fleet_tag` (TOOL-dPlacedRequest-1 S11) (proposed) | 28 | coordination.md:107; cl-0165 |
| I15 | The message id | `derive_message_id`, a caller of an extracted `derive_gov_id <field>…` (the first 12 hex of `git hash-object --stdin` over NUL-terminated fields; TOOL-dPlacedRequest-12 S3's `derive_problem_id` its other caller), over build, item instance key, pass, kind, subject and answered id, never the sender's session (proposed) | 22 | TOOL-dPlacedRequest-12 S3 |
| I16 | The mail ref and writer | `refs/gov/mail/<slug>/<fleet tag>/<session>`, the session segment through `derive_ref_segment`, cached at `refs/gov/remote/mail/…`; each post a `build_gov_commit` on the tip read under the fixed `gov-claim` identity, pushed by `write_gov_ref`; behind `RUN_CLAIMS` (TOOL-dPlacedRequest-12 S7); the session from `CLAUDE_CODE_SESSION_ID`, absent writing nothing | 5 | coordination.md:103; TOOL-dPlacedRequest-11 S1, S2, -12 S1 |
| I17 | The message record | header `gov-mail <slug>/<id>`, blank line, `key: value` lines `id`, `build`, `from-tag`, `from-session`, `to`, `kind`, `item`, `pass`, `subject`, `answers`, `seq`, `after`, `content-key`, `deadline`, `default`, blank line, body; one header-keys-body builder shared with TOOL-dPlacedRequest-12's register body at its second instance (proposed) | 5 | TOOL-dPlacedRequest-12 S6 |
| I18 | The closed message kinds | `confirm-request`, `confirmed`, `changed`, `overlap`, `takeover`, `landed`, `question`, `answer`, `ack`, `intake`, `withdrawn`, `superseded`, declared once in `tools/loop/loop.toml` and checked on write | 5 | coordination.md:110-112 |
| I19 | The coordination verbs | `unattended.sh --mail post`, `--mail read`, `--mail ack` (unit 5), `--mail answer` (unit 25), `--mail notice` (unit 21); the only writers of a mail ref | 5 | coordination.md item 6 |
| I20 | The one mail reader | `read_mailbox <slug> soft` or `strict`, one row per message: id, kind, to, seq, state (`open`, `answered`, `acked`, `expired`), first sighting; duplicate ids collapsed to the earliest sighting | 5 | `read_claims` (`tools/unattended/unattended.sh`) |
| I21 | The transition's disposal field | `disposed=<id>,<id>`, a registered extension field on TOOL-dDeclaredLoop-3's trailer and log | 5 | TOOL-dDeclaredLoop-3 S1 |
| I22 | Order and supersession | `seq: <n>` the message's first-parent depth on its own ref; `after: <id>` on a take-over's first message, naming its predecessor's last; `content-key: <12 hex>` over the interface text on `confirmed` and `changed`, a dependent acting on the recomputed key, never on arrival order (proposed) | 27 | P40, v2:1075-1079 |
| I23 | The mail deadline | `check_mail_deadline <message>`: TOOL-dPlacedRequest-17 S4's `check_deadline_passed` over the message's commit and `flow.wait-ceiling` hours, the asker's `default` answering past it; `expired` in I20 (proposed) | 24 | TOOL-dPlacedRequest-17 S1, S4; TOOL-dDeclaredLoop-33 S5 |
| I24 | The notice stamp | `<git-common-dir>/gov-mail-fetch.stamp`, its mtime the local copy's age; touched by every mail fetch (proposed) | 21 | `tools/process-monitor/procmon-hook.js` |
| I25 | The live ring | the channel `deps.messaging` picks carries only a message's ref and id; a registered doorbell attaches at dWellOiledMachine's Runtime `[extend]` point, a `[[stand-in]]` until then | 21 | v2:1167; coordination.md item 7 |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 1 → 2, 3, 4, 20, 9, 7 | `presets.toml` |
| 19 → 16 | `write_shrink_list` |
| 2 → 3, 20 | `RESOLUTION_ORDER` |
| 12 → 15, 14 | `print_replay` |
| 13 → 26, 15, 14, 8, 5 | `## pointers` |
| 13 → 14, 8, 10, 21 | `derive_item_boundary` |
| 14 → 9 | `measure_context_fill` |
| 28 → 5 | `check_mail_recipient` |
| 22 → 5, 27 | `derive_message_id` |
| 5 → 23, 27, 24, 10, 25, 21, 6, 7 | `read_mailbox` |
| 27 → 7 | `content-key` |
| 24 → 25 | `check_mail_deadline` |
| 21 → 6 | `deps.messaging` |

## The units

**Writer groups and build order.** The `order` value is the build order: the preset store before the reader step,
charter, intake and scenario slot that read it; the list factory before the purposes list that reuses it; the replay
line order and the card's pointers before every session behaviour that prints or reads them; the context reader
before the orientation cost that reuses it; the recipient grammar and the message id before the mailbox that keys on
them; the mailbox before every reader, deadline, answer, notice, live ring and dependency notice; the tool-call,
progress, attendance and repeat units last, each independent of the rest. The build harness splits the 28 orders into
five writer groups of consecutive orders; author every unit of your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 1 (1), 19 (2), 2 (3), 3 (4), 4 (5), 20 (6) |
| 2 | 16 (7), 12 (8), 13 (9), 26 (10), 15 (11), 14 (12) |
| 3 | 9 (13), 28 (14), 22 (15), 5 (16), 23 (17), 27 (18) |
| 4 | 24 (19), 10 (20), 25 (21), 21 (22), 6 (23), 7 (24) |
| 5 | 8 (25), 11 (26), 17 (27), 18 (28) |

Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **KICK-dKeptSession-1** — Items 1. I1, I2, I3: the four named presets as data, the completeness check (every
  catalogue key a preset may touch carries a value in each shipped preset, `never` keys none), the pair rules on
  presets and on a repository's overrides, each shipped preset loaded with only the core installed and refused only
  for a value on a core key that selects an absent expansion. Every red case the clause states: the planted
  override past `review.max-rounds`, a planted Absent clause that refuses by key, and a loader stubbed to accept every
  value. Promote `preset-check.py`'s logic into the kit; it is a record, not product. Scout A row 1.
- **KICK-dKeptSession-19** — Items 19 (gap-spine-10). I7: the catalogue's reader join, every catalogue key named by a
  unit on its owner build's row in the design view (`design_lib.read_design`, `extract_clause_tokens`), today's
  unnamed keys a shrink-only list written by the extracted factory, with dGroundRules' two lists moved onto it. The
  arm announces its population and grades nothing in an adopter whose `DESIGN_*` keys are blank. Scout A row 6.
- **KICK-dKeptSession-2** — Items 2. I4: the preset step, so a key the file does not override reads the named
  preset's value; the red case is a strict-named file with no override reading `hooks.bypass` as anything but
  `refused` (DA-M10). `hooks.bypass` is dWitnessedBar's key: read it, never re-declare it. Scout A row 2.
- **KICK-dKeptSession-3** — Items 3. I5: the charter's preset section, the name and only the keys that differ from it,
  rendered through dOrderedCharter's renderer and seen red on a planted override. Edits
  `coding-governance-agents.template.md` (a governance carrier: the grant line), never the rendered `AGENTS.md`.
  Scout A row 3.
- **KICK-dKeptSession-4** — Items 4. I6: policy at govkit intake, the preset asked once at intake and written into
  the scaffolded policy file. Settle by §8 whether intake defaults to `standard` or refuses with no answer
  (`cmd_intake` refuses a missing answer today). Scout A row 4.
- **KICK-dKeptSession-20** — Items 20. I9: a scenario's preset slot, scoped to the builds placed under the scenario,
  read through the one reader before the repository's own values, never a key in I1's `never`; seen on two builds
  under scenarios with different presets. Settle by §8 what "before the repository's own values" orders (scout A row
  7 names the two readings). Scout A row 7.
- **KICK-dKeptSession-16** — Items 16. The policy namespaces' purposes: each namespace of the catalogue carries a
  purpose, the existing ones listed as awaiting review on a shrink-only list (I7), a new namespace refused without
  one, reviewed as `memory.map-purpose`'s default `review` says, a stand-in read until dTotalRecall lands the key
  (CS4-F1). Scout A row 5.
- **KICK-dKeptSession-12** — Items 12. I10: the fresh-session recommendation in the build's worktree while the
  card-import fixture is red, `always-resume` read as `fresh-when-idle` and the override reported, seen on a planted
  `always-resume` with the fixture red. TOOL-dPlacedRequest-2 S7 already prints the override; carry the clause, call
  that section, name the worktree, and make the fixture's verdict the switch rather than the import line's presence
  (scout C's disagreement). Scout C row 5.
- **KICK-dKeptSession-13** — Items 13. I11, I12: the card's pointers by `card.pointers` (`every-item`,
  `at-transitions`), the latest records by tag, the open forks and the item in flight, so a compacted or fresh
  session reorients from them; the item boundary every later session unit reads. Scout C row 6.
- **KICK-dKeptSession-26** — Items 26. The `budget —` line of I11 from TOOL-dDeclaredLoop-30's `budget_state`, seen
  red on a planted card that omits it. Scout C row 11.
- **KICK-dKeptSession-15** — Items 15. The `position —` line of I10 from `python tools/loop/position.py <slug>`
  (TOOL-dDeclaredLoop-7 S7, witnesses only) and one notice that a compaction's summary is a lead, never a source.
  Scout C row 8.
- **KICK-dKeptSession-14** — Items 14. I10's `context —` line, I13: `context.on-full` (`compact-with-card`,
  `fresh-at-boundary`) and `context.threshold` (a share of the window, read only under `fresh-at-boundary`), the owner
  session only (layer-runtime:783-787). Settle the window constant by §8. Scout C row 7.
- **KICK-dKeptSession-9** — Items 9. Orientation cost recorded per stage in the runlog kit through I13 and the stage
  tags, held as `orient.budget` says, seen on strict's `warn-at-evidence-ceiling`. Settle by §8 what the evidence
  ceiling is and where `owner-ceiling`'s number lives; no source defines either (scout C). Scout C row 3.
- **KICK-dKeptSession-28** — Items 28. I14: a recipient names a build, a unit, a node by its fleet tag, or the whole
  project. Scout B row 10.
- **KICK-dKeptSession-22** — Items 22 (gap-conc-09). I15, and the duplicate check reading every one of the build's
  per-session refs, so a retried post is refused, a retry from a new session among them, while two answers to two
  messages both land; seen on a post retried after a crash, a retry from a new session, and two acknowledgements
  from one item. Scout B row 5 and its disagreement 3 (the reader collapses a cross-ref race).
- **KICK-dKeptSession-5** — Items 5 (gap-flow-06, gap-conc-04). I16-I21: the mailbox per build, one append-only ref
  per writing session, the closed kinds checked on write, written only through the coordination verbs, which pass
  the record door once dTotalRecall lands it and write the ref directly until then (a stand-in row), read at every
  transition, which is refused while a message addressed to the build is neither answered nor acknowledged until
  `flow.wait-ceiling` passes (seen red on a planted unanswered message), disposed there, shown on the card as I11's
  `mail —` line, kept in the transition log as I21. Scout B row 1.
- **KICK-dKeptSession-23** — Items 23. Every mail write appended to the change feed once its ref update lands, in the
  feed's census (TOOL-dPlacedRequest-13 S3, S9), red on a planted mail write that skips the append. Plant the shape
  the census reads (scout B's disagreement 4). Scout B row 6.
- **KICK-dKeptSession-27** — Items 27 (gap-conc-15). I22, seen red on a relayed `changed` that arrives before the
  `confirmed` it supersedes. Scout B row 9.
- **KICK-dKeptSession-24** — Items 24. I23: the deadline judged by the declared clock dPlacedRequest's leases use,
  seen on a planted question nobody answers and red on a reader whose clock runs a day ahead. Mail commits carry the
  `gov-claim` identity so the sightings walk sees them (scout B's disagreement 5). Scout B row 7.
- **KICK-dKeptSession-10** — Items 10. `mailbox.reads` (`every-item`, `transitions-only`,
  `every-item-amendments-at-transitions`) arming TOOL-dDeclaredLoop-7 S4's mailbox interrupt at I12's boundary, with
  the `intake` kind. The interrupt's text naming dWellOiledMachine is a parent defect: an ask (scout B's
  disagreement 1). Scout B row 3.
- **KICK-dKeptSession-25** — Items 25. `mailbox.answer` as an item row in `tools/loop/loop.toml`, a `question`
  answered by the role owning the asked interface or item, dispatched by `next`; until dWellOiledMachine lands
  `next`, a question to an unattended build answered by the asker's declared default under I23, the same stand-in
  covering its answering role; the recipient's transition refused meanwhile, a declared wait inside
  `flow.wait-ceiling` that `leases.renewal: progress` renews; seen red on a planted question to an unattended build
  whose lease lapses while it waits. The renewal witness set lacks a declared wait: an ask for dPlacedRequest
  (scout B's disagreement 2). Scout B row 8.
- **KICK-dKeptSession-21** — Items 21 (gap-conc-05). I24, I25: news shown as `mailbox.notice` says (`every-item`
  default, `every-tool-call`, `off`), the boundary's one bounded fetch of the mail refs, its fallback to the local
  copy with its age, the tool-call hook listing from the local copy with no network call and a detached fetch past
  `mailbox.fetch-seconds`, and every red case the clause states. Settle by a FACT-QUESTION which hook event's output
  reaches the model (scout B's disagreement 7). Scout B row 4.
- **KICK-dKeptSession-6** — Items 6. Live delivery where the harness has it: the post's tail rings I25's channel when
  `deps.messaging` admits a live channel, a stand-in until Runtime's doorbell point. Scout B row 2.
- **KICK-dKeptSession-7** — Items 7 (gap-flow-06). `deps.coordination` (`message-then-progress`,
  `wait-for-landing`, `order-only`) switching TOOL-dDeclaredLoop-7 S4's dependency gate, reachability by the parent's
  lease (TOOL-dPlacedRequest-1), interfaces confirmed at Design's exit by `confirmed` messages, `deps.early-build`
  (`confirmed-interfaces`, `design-only`, `anything-coordinated`), change and landing notices, each key seen on
  strict's value. Scout C row 1.
- **KICK-dKeptSession-8** — Items 8. `actions.free` (`read-only-probes`, `item-reads-only`, `recorded-anything`) at
  the tool call, an arm in `tools/hooks/scratch-guard.js` reading I12's `item —` pointer; every write, spawn,
  commit or push belongs to an item, and anything else is filed as an intake (orientation:310-312). Scout C row 2.
- **KICK-dKeptSession-11** — Items 11. `notify.owner` (`turn-micro-formats`, `park-and-landing`, `every-transition`,
  `park-only`) gating the progress emits that exist; progress only, no push channel (v2:1226, v2:1228). Scout C
  row 4.
- **KICK-dKeptSession-17** — Items 17 (gap-flow-16). `attendance` (`unattended`, `announce`, `confirm-steps`,
  `confirm-acts`) as a source of owner breakpoints in TOOL-dDeclaredLoop-19's `derive_breakpoints`, never selecting
  an item's actor, the driver or a binding; its arm seen red on a planted value that swaps an actor; the `step —`
  announcement (dWellOiledMachine) and live owner questions (dFurnishedOrders) as stand-in rows. Scout C row 9.
- **KICK-dKeptSession-18** — Items 18. The `repeat` disposition in the placement set and its `none` row in the
  transition table, routing a request onto a `playbook`. TOOL-dDeclaredLoop-16 S1 and -13 row B3 already spell the
  disposition and the row: carry the clause, cite them, add no second row, and spec the stand-in the clause names —
  a `repeat` request is filed as an ask until dIndexedDesign lands the playbook record kind — plus the arm that
  sees both. Scout C row 10.
