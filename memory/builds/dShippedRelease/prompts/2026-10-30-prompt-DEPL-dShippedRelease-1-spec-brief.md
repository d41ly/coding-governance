**Serves:** research DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31

# Spec brief — dShippedRelease, the thirty-one Deploy units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dShippedRelease/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys and Obligations sections bind every unit.
2. The build README, `memory/builds/dShippedRelease/README.md`: its build-level rules bind every spec, the fork rule
   above all. Its `BACKLOG.md` holds ask DEPL-dShippedRelease-32, which the LAST unit in build order (unit 9) names in
   its header's `closes`; every other unit's header says `advances DEPL-dShippedRelease-32`.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5, M12. Every unit is Tier 2: each is a new
   or changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every row of "Shared interfaces", "Pinned choices" and "Edges", and the scout
   record your units cite, each under `memory/builds/dShippedRelease/build/`:
   `2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md` (units 1, 2, 4, 5, 13, 14),
   `-11-reuse-scout-b.md` (11, 12, 27, 30), `-3-reuse-scout-c.md` (3, 6, 8, 15, 19, 22, 26),
   `-7-reuse-scout-d.md` (7, 16, 17, 18, 20, 25, 28, 29, 31) and `-9-reuse-scout-e.md` (9, 10, 21, 23, 24). Each holds
   a seam row per unit with path:line at `f4597719`, numbered disagreements between records and source, proposed
   interfaces, order constraints and forks. Those disagreements are findings you act on.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below). Deploy's PRIMARY
source is `B/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`: its Deploy table :430-512, the release slot and
`deploy.released` :498-511, the entry and post-close material :574, `kits.*` :788-790. Then
`B/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`: `[design-integrations]` :295-330, the `release.*` program
:375-423, kit descriptors :441-456, the distribution program :457-477. Then architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id; `[policies]` lines the packet cites),
`B/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md` :426-440 (the record kinds), the gap register
`B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` (each gap by its packet line), the research records
`B/*research-deploy.md`, `B/*research-distribution-a.md`, `-b.md`, `B/*research-integrations-a.md`, `-b.md`,
`B/*flow-roles.md`, and the fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 36-61 and
900-946. You never edit an instrument, v2, the as-built view or the packet: the packet's Non-goals.

## Every spec, whatever its unit

- Path `memory/builds/dShippedRelease/spec/2026-10-30-spec-DEPL-dShippedRelease-<n>.md`; H1
  `# DEPL-dShippedRelease-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order <k> ·
  advances DEPL-dShippedRelease-32`, with `<k>` your unit's order below (unit 9 writes `closes DEPL-dShippedRelease-32`
  in place of `advances`). `OPEN` is the status token: `DRAFT` is not in `STATUS_TOKENS`
  (`tools/memory-tree/tree_lib.py`). The shape is `memory/builds/dMindYourWords/spec/2026-10-29-spec-TOOL-dMindYourWords-1.md`
  line 3.
- Binding lines, each at column 0 on a line of its own under the status line:
  `**Carries:** <Items id>@<hash8> whole`, and for each node the owned-node table gives your unit,
  `**Carries:** node:<node>`. One unit carries one clause whole: the README's roster is one unit per clause. A long
  clause keeps its behaviours as separate S-items of its one spec; never split it into parts without saying so in your
  return.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 1, 6, 9, 10, 23) still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close. A policy key's non-default value is seen by a planted
  `.governance/policy.toml` naming that value; each allowed value of a key your unit owns is a planted case.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `f4597719`: verify each line number before citing it. Record each
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
- Each policy key this build owns already has its catalogue row in `tools/policy/catalogue.toml`, and its name in
  `tools/policy/unsummarised-keys.txt`: the owner unit fills the row's missing summary and usage and drains its name
  from that file, and never adds a second row. Its allowed values and default are that row's, verbatim. Once every
  unit of this build is terminal, the policy kit's reader-coverage arm reds any owned key no literal call reads, so
  the owner unit of each key names that literal reader in its acceptance.
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dShippedRelease/build/2026-10-30-build-DEPL-dShippedRelease-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- A parent spec, or a spec of another build, that must change for your clause to hold is never edited: state the
  needed change in §8 as an ask for that build, its target build, its accept line, and your return names it. The main
  loop files every such ask once, after the writers return, so no two writers mint an id in one foreign family
  (PLAY-dClosedLoop-32).
- Write nothing outside `memory/builds/dShippedRelease/spec/` and `memory/builds/dShippedRelease/build/`; temp files go
  under the scratch path your harness names.

### What the last spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python ci_emit.py …`) and keep its
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
  one only where you mean it. Unit 25 retires `gov_source`, and scout D's disagreements 6 and 7 list readers the clause
  does not name; unit 31 renames `fleet`-spelled surfaces, and scout D's disagreement 13 lists a parsed one.
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
  `check-spec-tokens.py` and `carries.py --report dShippedRelease` after every writer returns.

## The parents are specced, not built

Every parent surface this build calls is specced and DEFERRED at HEAD, and the scout records list each by spec id.
`parents:` names dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine, dLinkedLibrary and dFurnishedOrders;
dPlacedRequest, dKeptSession, dDeclaredLoop, dFairHearing, dOrderedCharter and dSafePassage reach this build only
transitively, and the scouts' per-unit tables need them all, so name each as a build-run precondition. None of
`tools/loop/`, `tools/runtime/`, `tools/lib/gov-ref.sh`, `tools/lib/commit_trailers.py`, `tools/playbook/core.py`,
`tools/playbook/kinds.toml`, `tools/playbook/namespaces.toml`, `tools/memory-tree/record-kinds.toml`,
`tools/govkit/upgrade_steps.py` or `tools/govkit/shims.py` exists at HEAD. dScopedBuild, dCalibratedLens, dRankedPlan
and dTendedCadence hold no spec at all: dScopedBuild and dCalibratedLens are this build's stand-ins (the packet's
"Later builds named"), and dRankedPlan and dTendedCadence are outside its closure.

Landed and readable now: `tools/push-main.sh`, `.githooks/pre-push`, `tools/run-gates/`, `tools/unattended/`,
`tools/govkit/`, `tools/policy/`, `tools/roles/`, `tools/hooks/`, `tools/memory-tree/design_lib.py` and
`tools/check-spec-tokens.py`.

Where a scout found that a design record, a parent spec or source disagree, v2's clause governs; a parent spec it
contradicts gets an ask (the rule above), never an edit. Where the clause itself names something source shows wrong,
the spec says what source shows, carries the clause's intent, and writes a deviation record naming the difference.

## Owned nodes

| Node | Unit |
|---|---|
| `record-kind.landing`, `item.deploy.record` | 1 |
| `item.deploy.distill` | 2 |
| `item.kits.cut`, `policy-key.kits.cadence`, `record-kind.kit-release` | 3 |
| `item.deploy.current`, `item.deploy.mandate`, `item.deploy.notify`, `item.deploy.snapshot`, `item.deploy.unlease`, `item.deploy.close`, `record-kind.comparison` | 4 |
| `item.deploy.released`, `policy-key.build.closes`, `policy-key.build.release-hold`, `policy-key.build.release-ceiling` | 5 |
| `item.kits.currency`, `item.kits.adopters`, `record-kind.currency`, `policy-key.deploy.currency`, `policy-key.currency.max-behind`, `policy-key.currency.on-behind`, `policy-key.kits.host`, `policy-key.kits.watch-cadence` | 7 |
| `item.kits.version` | 10 |
| `item.deploy.parents`, `policy-key.deps.landing` | 11 |
| `item.deploy.land`, `policy-key.landing.order` | 12 |
| `item.deploy.core` | 13 |
| `item.release.pick`, `item.release.approve-auto`, `item.release.approve-owner`, `item.release.promote`, `item.release.verify`, `item.release.route`, `item.release.record`, `record-kind.release`, `record-kind.release-exit`, `policy-key.deploy.runs`, `policy-key.deploy.promotion`, `policy-key.deploy.on-verify-fail`, `policy-key.release.environments` | 15 |
| `item.kits.offer` | 16 |
| `item.kits.install`, `item.kits.update`, `item.kits.install-attended`, `item.kits.update-attended` | 17 |
| `policy-key.integrations.tracker` | 22 |
| `policy-key.install.guards` | 24 |
| `record-kind.receipt`, `policy-key.install.from`, `policy-key.install.steps` | 25 |
| `policy-key.platforms.supported`, `policy-key.platforms.verify` | 26 |
| `policy-key.commits.squash` | 27 |
| `item.adopt.declarations` | 28 |
| `record-kind.adopter-register`, `record-kind.adopters` | 31 |

Units 6, 8, 9, 14, 18, 19, 20, 21, 23, 29 and 30 own no node; each still names the nodes it reads, in prose.

## Gaps — which unit closes each

| Gap | Unit |
|---|---|
| `gap-deploy-01` | 15 |
| `gap-deploy-02`, `gap-deploy-10` | 13 |
| `gap-deploy-03` | 8 |
| `gap-deploy-04` | 7 |
| `gap-deploy-05` | 20 |
| `gap-deploy-06` | 14 for review, 23 for the role, 3 for the changelog |
| `gap-deploy-08` | 9 |
| `gap-deploy-09`, `gap-flow-08` | 12 |
| `gap-deploy-11` | 3, with 10 for the version slot |
| `gap-deploy-12` | 25 |
| `gap-deploy-13` | 16 |
| `gap-deploy-14` | 24 |
| `gap-deploy-21`, `gap-deploy-22`, `gap-deploy-23` | 27 |
| `gap-deploy-27` | 17 |
| `gap-deploy-28` | 29 |
| `gap-deploy-29` | 31 |
| `gap-tool-02`, `gap-tool-07` | 10 |
| `gap-tool-04` | 21 |
| `gap-tool-11` | 26 |

## Pinned choices — one answer for every writer

These cross several units, so each is pinned here and the owner unit records it in §8 as `RESOLVED (agent, 2026-10-30,
delegated)` by the rung named. A writer who finds a pin wrong says so in its return and writes a deviation record
rather than a second answer.

- **C1, the core Deploy code's home (rung 3).** No new core kit. The programs of core `deploy.*` items live in one
  module, `tools/loop/deploy_items.py`, with their `[[item]]` rows in `tools/loop/loop.toml` and their shell verbs in
  `tools/unattended/unattended.sh`; the lander stays `tools/push-main.sh`. Units 1, 2, 4, 5, 11, 12, 13, 14, 27 and 30
  extend that module and each names only its own functions. Expansions live in the `integrations` kit,
  `tools/integrations/`, which v2 names and unit 15 creates through unit 10's factory, and in `tools/govkit/`.
- **C2, the landing record's home (rung 3; owner unit 1).** A ref-held record, `refs/gov/landing/<sha>`, written by
  `deploy.record` through `write_gov_ref` (TOOL-dPlacedRequest-11), so a second node reads it and no post-push tree
  commit is needed to make it readable. `read_landing <sha>` is its one reader. This answers scout A's forks 1 and 3.
  A ref write is no tree change, so what no bar grades is the record's content, which every reader must treat as a
  claim its `sha` and `core` fields can be checked against.
- **C3, what reaches the tree after the landing (rung 3; owner unit 4).** The mailbox's copies, the terminal snapshot
  and the transition's folder copy ride ONE records-only commit landed through the lander, gated as any landing, and
  the mailbox ref is pruned only once its copy is on the default branch. Nothing bypasses the lander, and a landing's
  own records-only commit raises no second landing record (scout A disagreements 1, 2 and 7).
- **C4, the lease stays live until `deploy.unlease` (rung 1; owner unit 4).** cl-dClosedLoop-0508 governs:
  `--landed`'s lease write at `unattended.sh:6381-6384` stops writing a terminal status, so a killed supervisor's build
  can be taken over and closed. TOOL-dPlacedRequest-16 S2 contradicts this and gets an ask.
- **C5, the mailbox closes before the tombstone (rung 1; owner unit 4).** TOOL-dWellOiledMachine-58 S5 needs the live
  lease to prune, so the order is mailbox, then tombstone, whatever the clause's wording order; a deviation records the
  difference.
- **C6, one post-landing verdict record (rung 3; owner unit 13).** `read_core_verdict <sha>` returns `verdict`,
  `published` and `run_id`, held at a ref a second node can read, apart from `refs/gov/verdict/<sha>`, because
  `gap-deploy-02` asks verdict and publication apart on every exit path, a failed publication included.
  TOOL-dWitnessedBar-6 does not supply it (scout A disagreement 6). `GATE_POST_MERGE=ci` (`gap-deploy-10`) is unit
  13's, reading through `remote_verdict.py` (TOOL-dWitnessedBar-6 S7), with `policy-file.on-missing-expansion`
  deciding when no backend is registered.
- **C7, the turn is a cadence-shaped lease (rung 3; owner unit 12).** `--lease acquire run landing <branch>`, never
  the turnstile, which is a host semaphore. `landing.order`'s default, `plan-priority-then-first-verified`, reads
  `first-verified` with a recorded reason while no plan priority exists, because dRankedPlan is outside this build's
  closure (scout B disagreement 11, fork F6). No parent is added.
- **C8, the draw lives on the root's lease (rung 1; owner unit 30).** The clause says the draw appends and releases
  in one push and the transition is "minted under the build's claim ref", so the draw row is a commit on the root's
  lease ref and TOOL-dDeclaredLoop-30's tracked-file row gets an ask. An absent ref on a pre-lease root is a closed
  root whose first draw mints its tombstone (scout B disagreement 5, fork F5).
- **C9, the patch's intake (rung 3; owner unit 13).** Origin `landing`, ratified through the originating build's
  mandate. TOOL-dWellOiledMachine-27 S1, S3 and S4 refuse it as specced (scout A disagreement 10) and get an ask.
  The "post-close row" exists only at `B/2026-10-14-build-PLAY-dClosedLoop-1-flow.md:628`: unit 13 states it, unit 30
  cites it. `derive_red_key <landed sha>` is unit 13's and unit 30 reads it, so one red files one patch.
- **C10, `session-start` is registered here (rung 3; owner unit 3).** `kits.host`'s default registers nothing until
  someone acts (TOOL-dWellOiledMachine-13 §3 and -59 §3), so unit 3, the first reader, registers the host row, and unit
  7, the key's owner, reads it. `every-landing`, `owner-cut` and `every-session` are this build's own program over
  TOOL-dWellOiledMachine-59's rows, because S1 admits only `daily` and `weekly`; an ask offers the extension back.
- **C11, `release/<E>` calls `--lease` directly (rung 3; owner unit 15).** `release.pick` acquires and `release.record`
  releases with no `--as`, a hand-over. It is no cadence-items row (scout C disagreement 6). Environment names are
  policy, never `tools/runtime/points.toml`, which update overwrites.
- **C12, the deployer's actor (rung 5; owner unit 23).** `gov-deployer` is `layer.distribution` and
  `layer.integrations`, `acts-as` `item`. TOOL-dBoundRoles-1 S7 and AC6 refuse a composed item with a deployer actor
  (scout E disagreement 7), so unit 23 asks and records the departure.

## Shared interfaces — one spelling for every writer

Each row names its owner, the unit whose spec defines it; every other unit names it exactly as spelled here and cites
the owner. A spelling marked "proposed" has no source yet; the owner may refine it in its spec, and says so in its
return. Every new name is asked of `--suggest` first.

| # | Interface | Spelling | Owner | Source |
|---|---|---|---|---|
| I1 | The landing record | `refs/gov/landing/<sha>`, fields `sha`, `builds`, `units`, `outcome`, `pre-push`, `core`, `patch-key`, `closes`, `distill`, `review`, `carries`; read by `read_landing <sha>` (proposed) | 1 | scout A row 1, flow-steps:439 |
| I2 | The unarmed line | `distill: unarmed · <reason> · <sha>`, the `test.seed` grammar (proposed) | 2 | scout A row 2 |
| I3 | The kit schema | `tools/playbook/kit-schema.toml`, `[kind]`, `[[field]]`; `kind.kit`, `core.py new kit`, leg `kit conformance`; `read_kit_rows()` in install order; `read_python_floor()` (proposed) | 10 | scout E interfaces |
| I4 | The not-installable mark | `installable = false` and `why_not_installable` on a descriptor; `purpose` on every descriptor; `[[inline]]` rows on lib's (proposed) | 21 | scout E interfaces |
| I5 | The deployer | `gov-deployer`, `layer.distribution` and `layer.integrations`, `acts-as` `item` | 23 | scout E, TOOL-dBoundRoles-1 S5 |
| I6 | The register | `tools/govkit/adopters.toml` rows with `key`, `names`, `remote`, `branch`, `grant`; `adopter_rows(root)` the one reader (proposed) | 31 | scout D §3 |
| I7 | The parent state | `read_parent_state <slug>` answering `landed`, `held`, `withdrawn`, `superseded` or `absent` (proposed) | 11 | scout B §3 |
| I8 | The lander's outcome | `read_landing_outcome <sha>`, classes `landed-gated`, `landed-ungated`, `nothing-pushed`, `refused`, `unreachable`, `argument`, with `landing_prior_tip`, the tip before the push, because `<current default>..HEAD` is empty once pushed (proposed) | 12 | scout A, scout B disagreement 8 |
| I9 | The verdict | `read_core_verdict <sha>`, C6; `derive_red_key <landed sha>`, C9 (proposed) | 13 | scout A, scout B |
| I10 | The closer | `run_unlease <slug> --as landed\|withdrawn`, the one body under `life.unlease` and `deploy.unlease`; `deploy.close`'s terms `check_unleased`, `check_released`, `check_core_settled`, with unit 14 adding `check_landing_review` (proposed) | 4 | scout A §3 |
| I11 | The adapter header | `check_adapter_header(row)` in `tools/integrations/adapters.py`, fields `kind`, `grant`, `secret`, `witness-source`, `probe`, `fallback`, `cas` (proposed) | 15 | scout C §3, layer-expansions:300-308 |
| I12 | The engine verbs | `read-current <E>`, `promote <E> <sha> --expect <id>`, `rollback <E> <sha> --expect <id>`, `read-back <E> <sha>`, a distinct exit for a compare-and-swap refused (proposed) | 15 | scout C §3 |
| I13 | The release records | `release`, one per (SHA, environment); `release-exit`, keyed by SHA with outcome, environment and release id, at `refs/gov/release-exit/<sha>` (proposed) | 15 | layer-memory:432-433 |
| I14 | The release wait | wait kind `deploy.released`, outcome `release-hold`, owner-item kind `release-hold`, `count_keep_waiting <build> <sha>` (proposed) | 5 | scout A, scout B |
| I15 | The tag and notes | tag `gov/v<date>.<n>`; `read_release_tags()` in place of TOOL-dSafePassage-6's stand-in; `govkit.py cut`, `derive_release_notes(prev, head)`, `check_release_notes` (proposed) | 3 | scout C §3 |
| I16 | The receipt | `RECEIPT_SCHEMA` 5, `release`, `source_remote`, `superseded`, `deprecations`, `prior_commit`, `python_floor`; `read_receipt_release(receipt)` (proposed) | 25 | scout D §3 |
| I17 | The offer mode | `OFFER_MODE`, a disposition column on `SHELL_EXEC_SITES` (`govkit.py:4731`), so a new spawn reds (proposed) | 16 | scout D §3 |
| I18 | The attended order | `render_attended_order(kind, argv, why)`, one writer shared with TOOL-dSafePassage-2 S5's order (proposed) | 20 | scout D §3 |
| I19 | The update's report | `derive_kit_report(...)` over `render_delta_report` (PLAY-dOrderedCharter-34 S6) (proposed) | 29 | scout D §3 |
| I20 | The action pins | `tools/integrations/ci/action-pins.toml`, `[[action]]` `name`, `sha`, `tag`; `ci_emit.py render` and `check` (proposed) | 8 | scout C §3 |
| I21 | The platform runners | `point.flow.platform-runners`, rows `windows-gitbash`, `linux` (proposed) | 26 | scout C §3 |
| I22 | The settings target | `derive_settings_target(root)`, `guard = true` on a hook fragment (proposed) | 24 | scout E §3 |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 10 → 21, 9, 26 | `kit-schema.toml` |
| 10 → 17, 9 | `read_kit_rows` |
| 10 → 25, 26 | `read_python_floor` |
| 21 → 17, 9 | `installable` |
| 23 → 15, 3 | `gov-deployer` |
| 31 → 7 | `adopter_rows` |
| 11 → 12 | `read_parent_state` |
| 12 → 1, 27 | `landing_prior_tip` |
| 12 → 1 | `read_landing_outcome` |
| 1 → 2, 13, 4, 14, 27, 5, 30, 3 | `read_landing` |
| 13 → 4, 30 | `read_core_verdict` |
| 13 → 30 | `derive_red_key` |
| 4 → 14, 5 | `run_unlease` |
| 15 → 6, 19, 22 | `check_adapter_header` |
| 15 → 6 | `promote` |
| 15 → 5 | `release-exit` |
| 15 → 27 | `record-kind.release` |
| 5 → 30 | `count_keep_waiting` |
| 3 → 25, 7, 18 | `read_release_tags` |
| 3 → 7 | `session-start` |
| 25 → 7 | `read_receipt_release` |
| 25 → 16 | `install.steps` |
| 25 → 26 | `python_floor` |
| 16 → 20 | `OFFER_MODE` |
| 20 → 17 | `render_attended_order` |
| 27 → 17 | `codex-retrust` |
| 17 → 28, 29 | `kits.update` |
| 8 → 26 | `action-pins.toml` |

## The units

**Writer groups and build order.** The `order` value is the build order. The harness splits the 31 orders into six
writer groups of consecutive orders; author every unit of your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 10 (1), 21 (2), 23 (3), 31 (4), 11 (5), 12 (6) |
| 2 | 1 (7), 2 (8), 13 (9), 4 (10), 14 (11), 15 (12) |
| 3 | 6 (13), 27 (14), 5 (15), 30 (16), 3 (17), 25 (18) |
| 4 | 7 (19), 16 (20), 20 (21), 17 (22), 28 (23), 29 (24) |
| 5 | 18 (25), 24 (26), 8 (27), 26 (28), 19 (29), 22 (30) |
| 6 | 9 (31) |

Why this order: the kit factory and descriptors come first because every new kit and field passes through them; the
role and the register are small and free-standing; the queue precedes the landing record because the record reads the
lander's outcome; the landing record precedes everything that reads a landing; the verdict precedes the engine whose
close reads it; release precedes the wait that release wakes and the adapters that register at it; the tag precedes
what reads tags; the receipt precedes currency and the offer; the offer precedes the hooks; the walk precedes what the
walk carries; CI precedes the platform matrix; and the runbook is last because it renders what the others declare.
Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **DEPL-dShippedRelease-10** — Items 10 (`gap-tool-02`, `gap-tool-07`, `item.kits.version`). I3. The factory is the
  third schema of its shape, so extract rather than copy (`[reuse]`): `kind.kit` on PLAY-dOrderedCharter-7 S4-S6,
  the pattern of TOOL-dWitnessedBar-11 and -45. Forks: where the gate lives (scout E F3; source favours a core home),
  the P28 fields (F9), `version_from = {none}` on the 10 entries, and the one version check against `gap-tool-02`'s
  five, whose retirement meets PLAY-dOrderedCharter-16 AC1 (F11). `item.kits.version` is the behaviour `cmd_mint`
  already performs: its `[[item]]` row and its `test.merge` slot are the build. Scout E disagreements 11-14.
- **DEPL-dShippedRelease-21** — Items 21 (`gap-tool-04`). I4. Forks F1, F2 and F10. Each named consumer states its
  treatment and its leg runs on a tree with both descriptors; two of the named consumers read the registry and not the
  glob, and three more consumers exist (scout E disagreements 1, 2): cover all of them. govkit is not installable
  either (disagreement 3), and `registry.toml:199`, `:680`, `:684` go stale (disagreement 4). Seen red: a planted lib
  descriptor.
- **DEPL-dShippedRelease-23** — Items 23 (`gap-deploy-06`'s role half; v2:1970). I5, C12. The role-landing recipe of
  TOOL-dWitnessedBar-23 §4 is the file list. "Release notes for distribution" means verifying generated notes, since
  cl-dClosedLoop-0414 generates them (scout C disagreement 15). The workflow it joins is fork F8.
- **DEPL-dShippedRelease-31** — Items 31 (`gap-deploy-29`). I6. Rename the adopter sense of `fleet` (scout D
  disagreement 13's list), leave a node's sense, and rule on the third sense in `check-unattended.sh:4415` with its
  parsed reader `drift_report.py:3197`, a parsed interface. The `swydee`-less row with no `key` (disagreement 14) and
  the registration verb (`layer-memory.md:438`) are here. Shipped files may name no adopter: a fixture included.
- **DEPL-dShippedRelease-11** — Items 11. I7. The wait through `WAIT_KINDS` (TOOL-dWellOiledMachine-18), the withdrawn
  route through TOOL-dDeclaredLoop-15. `landed` is the parent's landing commit on the advertised tip, the `landed`
  notice being the wake, so this unit reads nothing unit 1 writes (scout B F3). `deps.landing`'s two values, each
  planted.
- **DEPL-dShippedRelease-12** — Items 12 (`gap-flow-08`, `gap-deploy-09`). I8, C7. The lander's outcome record is the
  gated half of `gap-deploy-09`. Forks F1, F2, F7. The turn release sits in the EXIT trap (`push-main.sh:217`), and a
  turn write stays out of the marker window `:967-988` until TOOL-dPlacedRequest-11 lands (scout B §4). Seen red: two
  nodes' planted landings taking one turn, and an `owner-orders` landing admitted with no order.
- **DEPL-dShippedRelease-1** — Items 1. I1, C2. The clause is three words and token-blind, so the spec states the
  fields itself: flow-steps:439 and `layer-memory.md:430`. The `landing` native-id class is unit 27's.
- **DEPL-dShippedRelease-2** — Items 2. I2. Unarmed read from the `[[stand-in]]` row for `item.build.distill`. Seen
  red: a planted empty join read green. No spec of dScopedBuild exists: the armed path is specified only as far as the
  stand-in row's retirement.
- **DEPL-dShippedRelease-13** — Items 13 (`gap-deploy-02`, `gap-deploy-10`). I9, C6, C9. The lander only starts the
  bar and does not check it (scout A disagreement 3), so `deploy.core` starts or finds the run and reads its verdict
  by SHA; `flow-steps.md:469` cannot be followed as written (disagreement 4). `core.exceptions`' default admits any
  session's record and its fields carry no landed SHA (disagreement 11): settle the join in §8. Seen red: both cases
  of the clause.
- **DEPL-dShippedRelease-4** — Items 4. I10, C3, C4, C5. `deploy.current`, `deploy.mandate`, `deploy.notify`,
  `deploy.snapshot`, `deploy.unlease` and `deploy.close`. The engine here is core `deploy.*` only: adapters are unit 6
  and promotion unit 15 (scout A disagreement 15, fork 9). `--close` and `deploy.close` are two acts (disagreement 2):
  keep both names apart and say which term runs when. `life.unlease` needs changing to share the body (disagreement 8):
  ask. Seen red: both cases of the clause.
- **DEPL-dShippedRelease-14** — Items 14 (`gap-deploy-06`'s review half). `review.pin` is an item and a stand-in, not a
  key, and it maps no landing preset (scout A disagreement 12); the default `review.deploy` places nothing
  (disagreement 13), so "blocks the close" must not read vacuous green there; the `landed` notice precedes the review
  (disagreement 14). Settle subject and preset in §8. Seen on a tree holding no Deploy lens.
- **DEPL-dShippedRelease-15** — Items 15 (`gap-deploy-01`). I11, I12, I13, C11. The `integrations` kit is created here,
  with the header factory (scout C disagreement 8). The seven `release.*` items and the `deploy.*` release keys. How an
  environment and an engine get values is yours: `read_catalogue_row` refuses a key with no row and the item regex
  admits names illegal as ref segments (disagreement 7). What wakes `release.*` after a close under `at-landing` is
  fork 4. Seen red: a stale holder's rollback after a take-over.
- **DEPL-dShippedRelease-6** — Items 6. Named for the engine, never an adopter (`check_adopter_names`-style arm 10 at
  `govkit.py:3731`). Signed container images on compose and systemd hosts have no native compare-and-swap, so the
  adapter either builds one or declares the gap and runs only under `deploy.runs: operator`, against the `landing-node`
  default, and the cross-key check is yours (scout C fork 10). Sources name no tool: M12 applies.
- **DEPL-dShippedRelease-27** — Items 27 (`gap-deploy-21`, `-22`, `-23`). Five behaviours in one spec, one S-item each:
  `carries` read from `landing_prior_tip`, never `check_carry_set` (scout B disagreements 7, 8); the `landing` class;
  a publication as a `release` record per (SHA, artifact environment), the atlas first; `commits.squash`, whose hosted
  squash never runs the lander (disagreements 9; fork F8); and Codex targets with `codex-retrust`, the `settings` kind's
  one-path limit (disagreement 15).
- **DEPL-dShippedRelease-5** — Items 5. I14. A `WAIT_KINDS` row, no new sweep or clock. TOOL-dWellOiledMachine-18 does
  not fit in three ways (scout A disagreement 9): ask, and settle the clock in §8. Exit records are planted until unit
  15's run. Seen red: a ceiling opening a second item, and a killed supervisor's build closed by a second node.
- **DEPL-dShippedRelease-30** — Items 30. C8, C9. One red files one patch; a chain walks `origin-slug` to the root
  (`resolve_budget_root`, scout B disagreement 4); a live root has no defined draw (disagreement 6); a release retry
  has no draw cause (disagreement 12). "Third" is a constant or a key: fork F9, and the count's store cannot be
  create-only decision refs. Every seen-red case of the clause is an acceptance criterion: there are five.
- **DEPL-dShippedRelease-3** — Items 3 (`gap-deploy-11`, `gap-deploy-06`'s changelog half). I15, C10. A sibling of
  `cmd_mint`. No tag exists, so the first baseline is a fork (scout C fork 9). Each `kits.cadence` value on its planted
  case. Seen red: planted notes that miss a landing.
- **DEPL-dShippedRelease-25** — Items 25 (`gap-deploy-12`). I16. Schema 4 is unbuilt; only a step raises a receipt
  after TOOL-dSafePassage-3. `python_floor` joins the list (scout C disagreement 11, a deviation). Readers beyond the
  clause's three (scout D disagreement 7), `deploy.toml`'s same-named key kept apart (disagreement 6), a source
  receipt's value, and what a step writes for `release` while no tag exists (fork 4). A "release-tag receipt" needs a
  marker the clause does not name (disagreement 9). The ninth spawn kind's isolation is TOOL-dSafePassage-7's.
- **DEPL-dShippedRelease-7** — Items 7 (`gap-deploy-04`). The second instance of `resolve_measurer_currency`'s read, so
  extract `remote_probe_py` into `tools/lib/`. Whether the currency record is committed (scout D fork 2), whether
  `deploy.currency` is per row (fork 3), and who can read a shim journal: only the adopter (disagreement 4). Each
  value of the five keys planted.
- **DEPL-dShippedRelease-16** — Items 16 (`gap-deploy-13`). I17. Every kind in the refuse table of scout D's unit 16
  row, and the git-config class TOOL-dSafePassage-24 found: `core.hooksPath` alone is not enough (disagreement 3). The
  sixteen git writes (disagreement 2). A refused push's order has no destination in the adopter's tree (disagreement
  12; fork 1). A kit with rendered files may reduce an offer to an order (fork 5): say so.
- **DEPL-dShippedRelease-20** — Items 20 (`gap-deploy-05`). I18. The offer runs neither hook; its order names the
  adopter's own run of each. `gap-deploy-05`, outbox orders graded by nothing, is closed here by a grader over the
  receipt's `orders`.
- **DEPL-dShippedRelease-17** — Items 17 (`gap-deploy-27`). Ordering alone cannot close `gap-deploy-27` (scout D
  disagreement 5, measured on two empty repositories, evidence in its scratch files, summarised in the record):
  `memory/` comes from the seed at LAND, and five adopters stop for reasons no order changes. Define "one pass"
  (fork 6). The migration step, dSafePassage's outcomes, each outcome's planted walk.
- **DEPL-dShippedRelease-28** — Items 28. Through `core.py adopt` (TOOL-dLinkedLibrary-8), the sibling of -23 there, rows
  through PLAY-dOrderedCharter-46's door. The fixture holds each input, a house `default` other than medium among
  them, and TOOL-dBoundRoles-23's owner authorization governs a value below the floor (fork 7).
- **DEPL-dShippedRelease-29** — Items 29 (`gap-deploy-28`). I19. Over PLAY-dOrderedCharter-34, -35, -36. The widening
  list compared with `derive_widenings`; the lost change told apart from unrelated holes. Seen red: a release dropping
  a widening of each direction.
- **DEPL-dShippedRelease-18** — Items 18. Mostly TOOL-dSafePassage-8; the new part is `kits.cut` refusing a tag at a
  SHA with no green gov-first record (scout D disagreement 16). Say so plainly rather than re-speccing it.
- **DEPL-dShippedRelease-24** — Items 24 (`gap-deploy-14`). I22. "Core guards" has no list (scout E disagreement 15):
  name it. Managed-settings paths are harness facts: a FACT-QUESTION with a probe where one exists, otherwise rung 3 or
  5. A committed policy file expressing a per-machine setting is fork F12.
- **DEPL-dShippedRelease-8** — Items 8 (`gap-deploy-03`). I20. Gov's workflow reads one declaration; rendered or
  parity-gated is scout C fork 2, and a render moves the blob `verdict.remote.pin` covers. `remote-ci.yml:15-16` and
  TOOL-dSafePassage-12 AC2 are touched (disagreement 14). Seen red: a planted tag-pinned `uses:`.
- **DEPL-dShippedRelease-26** — Items 26 (`gap-tool-11`). I21. Generalize `held_halves.py`'s `HOSTS` and
  `run-held-wsl.sh`, which refuses to start outside Windows (scout C disagreement 12). Runner adapters are unowned in
  spec: this clause takes them. `platforms.verify: ci` has no gov Linux job (disagreement 13; fork 11). The Linux job
  sets up Python at the floor. Each value of both keys planted.
- **DEPL-dShippedRelease-19** — Items 19. Through TOOL-dLinkedLibrary-8's census class and ruling kind. "Test job" is
  not decidable from the census (scout C disagreement 10; fork 7). Local re-run or remote conclusion is fork 6. Seen
  red: a registration check on a planted deploy job.
- **DEPL-dShippedRelease-22** — Items 22. Reads asks through `tools/memory-tree/backlog.py`, never a journal (scout C
  disagreement 9). No service is named: an abstract adapter row with a declared target, and no external dependency.
- **DEPL-dShippedRelease-9** — Items 9 (`gap-deploy-08`). Regions, not a whole-file render, over OC-20's renderer as a
  new scope (scout E F5, F6). `INSTRUCTION_PATHSPECS` excludes `WIRE-INTO-PROJECT.md` and "render parity" is defined
  nowhere (disagreement 8): define it here. `gap-deploy-08`'s `[isolate]` ports and `up —` half has no clause
  (disagreement 9; F13): settle it by the rungs. `read_kit_rows` gives the order, and a core renderer reaching an
  expansion kit's order is F4. This unit `closes DEPL-dShippedRelease-32`.
