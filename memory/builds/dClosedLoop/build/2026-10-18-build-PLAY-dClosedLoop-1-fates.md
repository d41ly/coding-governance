# Today's parts and their fates

**Serves:** research PLAY-dClosedLoop-1

The owner's point 8 asked what becomes of each of gov's tools under the new architecture. This record answers it, part
by part: every shipped kit, each function in it, and its fate. Dispatch 104 derived the first table
(`build/2026-10-18-build-PLAY-dClosedLoop-1-research-tool-fates.md`). The night pass updated it with the night's
decisions and proposed a fate for every part no record decided
(`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[p8-fates]`).

## [words] The owner's question, 2026-10-18

> 8. The inventory and mapping of the current Gov tools and their functionality - has it been done at any stage, is it helpful? We need a clear understanding of how the current kit is getting rebuilt under the new architecture - what functions stay and different shape, which functions go, what tools will stay, what tools with disappear?

## [inventories] What existed, and why it did not answer

- **Several inventories existed, none at function level with a fate.**
  - Dispatch 26's census (`research-memory-tooling.md`) counted every kit's tools, runs, legs and asks.
  - Memory's tooling map (`layer-memory` `[tools]`) turned it into 25 kit-level verdicts on 2026-10-15.
  - The gap register's implicit loop pictures the stages, not the tools.
  - The runtime layer's hook-owner table is the only part-level inventory with a fate, and covers hooks alone.
  - The codebase map's dossiers, `tools/gate-legs.json` and the kits' descriptors list parts with no fate.
  - The design map's kit, feature, hook and leg nodes are derived live, but carry no fate.
- **The kit-level map went stale.** The expansions, retrofit, systems and audit rounds overtook at least nine of its
  25 verdicts, and it still states them (`[stale]`). It is marked superseded.
- **It helped as a count, not as an answer.** The owner's question is about functions, so the table below is.

## [kits] Each kit's fate

A kit's fate is one of four:
- **kept:** it stays a kit, its functions kept or reshaped in place;
- **optional:** it stays as an optional component or an expansion's kit, which the core never needs (P28);
- **absorbed:** its directory goes, and its functions move into other kits;
- **retired:** it goes with no successor.

| Kit | Fate | What becomes of it |
|---|---|---|
| agent-instructions | absorbed | the one renderer takes its wiring (dOrderedCharter), and each harness's files come from the harness adapters (dWellOiledMachine) |
| branch-reconcile | optional | observability's prune fix (dTendedCadence) |
| codebase-map | optional | its symbols become the core `code` record (dTotalRecall); its dossiers and owner views stay optional, and `reuse_lookup.py` retires |
| drift-audit | optional | its gateable signals become core legs, and its report half is observability's (dTendedCadence) |
| gate-lint | optional | a Flow leg pack (dWitnessedBar), less its Python text-IO scan and shell-hygiene mode, which move into the core portability pack (dWitnessedBar) |
| govkit | optional | distribution's engine: release tags, the receipt, the one version check (dShippedRelease) |
| hooks | kept | its guards become packs on the one enforcement surface (dWellOiledMachine) |
| lexicon | optional | rebuilt by dMindYourWords |
| lib | kept | the shared primitives, and the join, ledger, extraction, region-parser and scorer factories |
| memory-recall | optional | narrowed to its why-search (dLinkedLibrary), its bench and union an `experiment` instance (dBoundRoles), its finder dTotalRecall's `record find` (SA-6) |
| memory-tree | kept | the memory contract's engine: the kind registry, `record` and the `code` record (dTotalRecall) |
| playbook | kept | the instruction engine, the one renderer (dOrderedCharter) |
| process-monitor | kept | Runtime's reaping (dWellOiledMachine); its census an observability reading |
| pytest-parallel-guardrails | optional | an adopter-only Flow leg pack (the owner, NP-22, 2026-10-18) |
| roles | kept | the roles kit: the core roles, work orders and shapes (dBoundRoles) |
| run-gates | kept | Test's verdict runner (dWitnessedBar) |
| runlog | optional | observability's reader; its line grammar becomes the core journal (dWellOiledMachine) |
| unattended | absorbed | dissolved: the loop kit takes its ladder, transitions and claims (dDeclaredLoop), and the runtime's own kit its supervisor seam, hooks and controls (dWellOiledMachine); `/unattended` retires at dConvergedCharter |
| workflows | kept | the role harnesses (dBoundRoles, dWellOiledMachine) and the Tier-2 review (dFairHearing) |

- **Two kits are new:** the loop kit (dDeclaredLoop) and the runtime's own kit (dWellOiledMachine), whose name the
  lexicon gives it (gap-lex-09).
- **Two kits disappear:** agent-instructions and unattended, both absorbed. No kit is retired outright.
- **Beside the kits:** the top-level checks fold into packs or into govkit's one version check, `skills/`
  loses `deploy-governance`, and loses `session-kickoff` once the entry step and the orientation scout take its
  procedure (SA-9), the git hooks
  stay with their bar and trap changes, and the hand-written guides retire into rendered views.

## [table] Every part, function by function

The fate is one of STAYS, RESHAPED, MERGED and RETIRED. "Where it goes" names the chain build that keeps or receives
it. "Decided by" names the record that decides it, a line-number citation of dispatch 104's resolved to its section
tag, or "the owner, NP-22, 2026-10-18" for a part the night pass proposed and the owner decided row by row. Counts: 24 stay,
72 reshaped, 25 merged and 16 retired, over 137 rows.

| Kit | Function | Today's job | Fate | Where it goes | Decided by |
|---|---|---|---|---|---|
| agent-instructions | harness wiring | one charter file, aliased per harness | RESHAPED | dOrderedCharter's one renderer absorbs the wiring; each harness's files come from dWellOiledMachine's harness adapters | v2 `[chain]` dOrderedCharter; layer-instruction `[layers]` |
| playbook | `render_playbook.py` | renders the charter template | RESHAPED | dOrderedCharter: the one renderer, the charter in its level-0 envelope | v2 `[chain]` dOrderedCharter |
| playbook | `adopt-playbook --check` | checks the render's wiring | MERGED | into the one renderer (dOrderedCharter) | v2 `[chain]` dOrderedCharter |
| playbook | `fleet.toml`, `--claim-node` | node registry | RESHAPED | node registry's runtime facts (dWellOiledMachine); fleet identity in the lease grammar (dPlacedRequest) | v2 `[chain]` dPlacedRequest; v2 `[chain]` dWellOiledMachine |
| roles | `agents/*`, `house/*.md` | role definitions | RESHAPED | twelve core roles with structured fields and typed returns (dBoundRoles) | v2 `[chain]` dBoundRoles |
| roles | spec-reviewer, diff-reviewer | two reviewer roles | MERGED | one reviewer with a lens per step (dBoundRoles) | roles `[forks]`; v2 `[chain]` dBoundRoles |
| roles | gov-session | hands work to another session | MERGED | the prompt writer ("session-handoff template folds") (dBoundRoles) | roles `[forks]` |
| roles | gov-orienter | orientation | RESHAPED | the orientation scout, composing the card in a sidechain (dFurnishedOrders) | roles `[forks]`; v2 `[chain]` dFurnishedOrders |
| roles | `workflows.toml` stages | stage order 0 to 7 | MERGED | the loop kit; its seven readers re-pointed (dDeclaredLoop) | v2 `[chain]` dDeclaredLoop |
| roles | `workflows.toml` entries | workflow table | RESHAPED | shapes registry: kind, fan, checklist, merge, cap (dBoundRoles) | v2 `[chain]` dBoundRoles |
| roles | `handoff.py` | hashed prompt file | RESHAPED | a work order per item, hashed into the spawn marker (dBoundRoles) | v2 `[chain]` dBoundRoles; layer-runtime `[current]` |
| roles | `render_agents.py` | renders agent types | MERGED | the one renderer ("roles render wiring") (dOrderedCharter) | v2 `[chain]` dOrderedCharter |
| roles | `check_roles.py` | role, table and doc agree | RESHAPED | role-by-step matrix joined both ways (dFurnishedOrders); policy reader re-pointed (dConvergedCharter) | v2 `[chain]` dFurnishedOrders; v2 `[chain]` dConvergedCharter |
| roles | `house/policy.toml` | effort and gates | MERGED | into `.governance/policy.toml` (dConvergedCharter); on dGroundRules's legacy list until then | v2 `[chain]` dGroundRules; v2 `[chain]` dBoundRoles |
| roles | `.claude/roles.json` | the rendered role index | RESHAPED | the role index beyond every worker's reach, `role-sha` compared at spawn (dBoundRoles) | v2 `[chain]` dBoundRoles; the shape audit, run B's M10 |
| roles | the `/build` Skill | drives an attended build through the harness pipeline | RETIRED | a client of `run` once the supervisor drives attended builds (dWellOiledMachine), removed after the deprecation window (dConvergedCharter) | the owner, SK-1, 2026-10-19 |
| workflows | `tier2-review.js` | review harness | RESHAPED | presets, opt-in lenses, skeptic batches (dFairHearing), run at breakpoints (dDeclaredLoop) | v2 `[chain]` dFairHearing; v2 `[chain]` dDeclaredLoop |
| workflows | `REVIEW-PROTOCOL.template.md` | protocol text | RESHAPED | corrected by dFairHearing, then a rendered view (dConvergedCharter) | v2 `[chain]` dFairHearing; v2 `[chain]` dConvergedCharter |
| workflows | `unattended-build.js`, `unattended-unit.js` | unit harnesses | RESHAPED | role harnesses inside act sessions, the deferral block, persisted returns (dWellOiledMachine) | layer-runtime `[contract]`; v2 `[chain]` dWellOiledMachine |
| workflows | `review_replay.py` | recall scorer | STAYS | dFairHearing's replays use it | v2 `[chain]` dFairHearing |
| workflows | `drift-audit-*.js` | drift audit harnesses | RESHAPED | observability's detectors, read as Maintain's cadence readings (dTendedCadence) | the owner, NP-22, 2026-10-18 |
| workflows | `orient-counterfactual.js` | a one-off kickoff experiment | RETIRED | the `experiment` shape kind (dBoundRoles), of which it is an early instance | the owner, NP-22, 2026-10-18 |
| workflows | four harness checks | syntax, fan-out, join, parity | STAYS | kept (dBoundRoles, whose role harnesses they check) | layer-memory `[tools]` |
| memory-tree | scaffold, `--new-build`, `--new-spec` | creates records | RESHAPED | the `record` write command (dTotalRecall) | v2 `[chain]` dTotalRecall; layer-memory `[revised]` |
| memory-tree | `gen_build_index.py` | index, README regions | RESHAPED | generated views (dLinkedLibrary), README schema and routing region (dTotalRecall); drift import becomes an optional slot (dOrderedCharter) | v2 `[chain]` dLinkedLibrary; v2 `[chain]` dTotalRecall; v2 `[chain]` dOrderedCharter |
| memory-tree | hygiene gate, `HYGIENE.md` | structural checks | RESHAPED | the kind registry generates the schema checks; `HYGIENE.md` becomes its view (dTotalRecall) | v2 `[chain]` dTotalRecall; layer-memory `[revised]` |
| memory-tree | `backlog.py` | asks | STAYS | grammar kept; acceptance at filing and counter-ref ids added (dTotalRecall) | layer-memory `[tools]`; v2 `[chain]` dTotalRecall |
| memory-tree | `gotchas.py` | bug classes | STAYS | handed by write set (dLinkedLibrary); check-18 probe becomes an optional slot | v2 `[chain]` dLinkedLibrary; v2 `[chain]` dOrderedCharter |
| memory-tree | `corpus_ids.py` | id grammar | RESHAPED | one exported slug and id grammar, with recall's parser moved in (dOrderedCharter, dTotalRecall) | v2 `[chain]` dOrderedCharter; v2 `[chain]` dTotalRecall |
| memory-tree | merge-rows | row-keyed merge driver | STAYS | also merges ledger TSVs (dWitnessedBar) | v2 `[chain]` dWitnessedBar |
| memory-tree | `transition_audit.py` | check 26 | STAYS | an append-only history population; `read_modes` re-pointed (dConvergedCharter) | retrofit `[ledger]`; v2 `[chain]` dConvergedCharter |
| memory-tree | `check-verdict-epoch.sh` | version dates verdicts | MERGED | the one version check (dShippedRelease, gap-tool-02) | gap-tool-02 |
| memory-tree | method, spec and annotation templates | guides | RESHAPED | spec as a tagged contract (dIndexedDesign); guides as views (dConvergedCharter) | v2 `[chain]` dIndexedDesign; v2 `[chain]` dConvergedCharter |
| memory-tree | method-carriers, slot-limit lists | registries | RESHAPED | ledger populations (dWitnessedBar) | retrofit `[ledger]`; v2 `[chain]` dWitnessedBar |
| memory-tree | `routed_commits` | every commit on a product path names a unit specced before it | MERGED | `build.scope`'s commit check and the touch join (dScopedBuild) | the owner, NP-22, 2026-10-18 |
| memory-tree | `check-arms` | a check's armed-population rows | RESHAPED | the ledger's armed populations (dWitnessedBar) | the owner, NP-22, 2026-10-18 |
| memory-tree | `row_grammar` | check 20, row grammar and id collisions in one file | RESHAPED | the record-kind registry's generated schema checks (dTotalRecall) | the owner, NP-22, 2026-10-18 |
| memory-tree | `migrate_backlog` | plans and relocates the backlog from shards to builds | RESHAPED | an update's upgrade step, run attended, retired once no tree is left on shards (dShippedRelease) | the owner, NP-22, 2026-10-18 |
| memory-tree | `DECISIONS.md` | decision log | RESHAPED | split by kind; the log keeps its path, with a holds-now view (dLinkedLibrary) | layer-memory `[decisions]`; v2 `[chain]` dLinkedLibrary |
| codebase-map | `gen_map.py`, its symbols | the inventory map and its public-name index | RESHAPED | the core `code` record (dTotalRecall) and `gov map code` (dLinkedLibrary) | the owner's point 3 (night pass); v2 `[chain]` dTotalRecall; v2 `[chain]` dLinkedLibrary |
| codebase-map | dossiers, `MAP.md`, `CARDS.md` | feature prose and the owner's views | STAYS | optional: dossiers anchored to symbol keys (dTotalRecall), their header the feature node as NP-16 settles (dLinkedLibrary) | the owner's point 3 (night pass); layer-memory `[map]` |
| codebase-map | `map_lib` join and base | coverage, compare base | MERGED | `tools/lib` join factory (dOrderedCharter, H5) | v2 `[chain]` dOrderedCharter |
| codebase-map | `reuse_lookup` + agent, rank, replay | reuse ranker | RETIRED | 0 of 24 solved; replaced by the house index via **Reuse:** (dLinkedLibrary) | layer-memory `[reuse]`; layer-memory `[tools]` |
| codebase-map | stale-dossier signal | freshness | RESHAPED | observability reading; map freshness (dTendedCadence) | layer-expansions `[design-observability]`; v2 `[chain]` dTendedCadence |
| codebase-map | `map_diff` | a range's feature digest, and stale dossiers | RESHAPED | a range read over the `code` record (dTotalRecall), and enrichment staleness by body hash (dLinkedLibrary) | the owner, NP-22, 2026-10-18 |
| codebase-map | `check_gate_coverage` | the adopter's gate compares every artifact the engine writes | MERGED | into `govkit check`, the one install check (dShippedRelease) | the owner, NP-22, 2026-10-18 |
| memory-recall | `query.py` | full-text search | RESHAPED | a record finder, `record find` (dTotalRecall) | layer-memory `[tools]`; v2 `[chain]` dTotalRecall; the owner, SA-6, 2026-10-19 |
| memory-recall | `extract.py` grammar, `recall_conf` | id parser | MERGED | into memory-tree (dOrderedCharter) | v2 `[chain]` dOrderedCharter |
| memory-recall | `recall-opened.js` | Read observer | RESHAPED | optional hook pack (dWellOiledMachine); shell reads too (dLinkedLibrary) | layer-runtime `[enforce]`; v2 `[chain]` dLinkedLibrary |
| memory-recall | `bench`, `union` | the retrieval bench and its union of runs | RESHAPED | an `experiment` shape instance over recall's corpus (dBoundRoles) | the owner, NP-22, 2026-10-18 |
| memory-recall | `check-recall` | recall's floor check | RESHAPED | the record finder's leg (dTotalRecall) | the owner, NP-22, 2026-10-18 |
| lexicon | `lexicon.py` gate and pin | naming gate | RESHAPED | definition classes, keyed debt ledger, forced packs (dMindYourWords) | v2 `[chain]` dMindYourWords |
| lexicon | `canon`, `scaffold_lexicon` | vocabulary | RESHAPED | noun canon seeded and frozen; packs chosen by census (dMindYourWords) | v2 `[chain]` dMindYourWords |
| lexicon | `subtokens`, tokenizers | splitting | MERGED | `tools/lib` extraction primitive (dTotalRecall, LX-2) | v2 `[chain]` dTotalRecall |
| lexicon | its two drift signals | gating | MERGED | the lexicon's leg pack (dMindYourWords) | layer-expansions `[design-observability]`; v2 `[chain]` dMindYourWords |
| runlog | `runlog_lib` grammar | line grammar | MERGED | the core journal (dWellOiledMachine) | v2 `[chain]` dWellOiledMachine; layer-runtime `[contract]` |
| runlog | reader, extract, model, prose | reader | STAYS | observability's reader half; role metrics read it (dFurnishedOrders); its timeline model read through the core reader and index (dWellOiledMachine) | layer-expansions `[design-observability]`; v2 `[chain]` dFurnishedOrders |
| runlog | `record.py` | run record | RESHAPED | run-record kind through `record`, owned by dWellOiledMachine | ownership `[look]`; layer-expansions `[agree-observability]` |
| drift-audit | seven gateable signals | drift gating | RESHAPED | five core legs and two lexicon legs (dTendedCadence gap-maint-09; dMindYourWords) | layer-expansions `[design-observability]`; layer-expansions `[gaps-proposed]` |
| drift-audit | report-only signals | readings | RESHAPED | observability detectors with owners (dTendedCadence) | layer-expansions `[design-observability]`; v2 `[chain]` dTendedCadence |
| drift-audit | `SHRINK_ONLY`, `PINS` lists | hand-typed lists | RETIRED | population index derived from the ledger (dWitnessedBar) | retrofit `[ledger]` |
| drift-audit | dangling-pointer signal | dead pointers | RESHAPED | Maintain's detector (dTendedCadence) | v2 `[chain]` dTendedCadence; layer-memory `[tools]` |
| drift-audit | remote-CI signal | dead today | RESHAPED | fixed (dTendedCadence, gap-maint-11) | layer-expansions `[gaps-proposed]` |
| unattended | `--plan`, `--status` | position | MERGED | loop kit position engine (dDeclaredLoop) and `next` (dWellOiledMachine) | v2 `[chain]` dDeclaredLoop; v2 `[chain]` dWellOiledMachine |
| unattended | transition verbs (brief, review, pass, landed, close, park, settle) | run state | RESHAPED | per-level transition tables and the transition record (dDeclaredLoop) | v2 `[chain]` dDeclaredLoop |
| unattended | `--hold`, `--resume`, `--abort` | owner control | RESHAPED | pause, resume, withdraw, supersede (dWellOiledMachine) | layer-runtime `[decide]` |
| unattended | `--claims`, `--overlaps` | run claims | MERGED | the one lease grammar (dPlacedRequest) | v2 `[chain]` dPlacedRequest |
| unattended | `--authorization` | the build folder or prompt record as the mandate | RESHAPED | the request is the mandate under `plan.ratification: request` (dRankedPlan), its intake written by the hook (dWellOiledMachine); ANCHOR_SCOPE and AUTH_PARAM retired | the owner's point 1 (night pass); v2 `[chain]` dRankedPlan |
| unattended | `--attest` | a typed attestation of a directive | RETIRED | none: an agent-typed witness, which P2 forbids; witnesses are computed | the owner's point 1 (night pass) |
| unattended | `resume-tick.sh` | out-of-process resumer | RESHAPED | the supervisor (dWellOiledMachine) | layer-runtime `[supervise]` |
| unattended | `RESUME_SCHEDULE_*` | desktop restart task | RETIRED | the node tick hosts the supervisor | layer-runtime `[supervise]` |
| unattended | `gate-guard.js` | run guard | RESHAPED | dispatcher pack (dWellOiledMachine) | layer-runtime `[enforce]` |
| unattended | `stop-guard.js`, cron keepalive | continuation | RETIRED | for act sessions and cadence; the supervisor's beat replaces them | layer-runtime `[enforce]`; layer-runtime `[schedule]` |
| unattended | `stall-recorder.js` | API-stall record | RESHAPED | the supervisor's limit signal, in the runtime's own kit (dWellOiledMachine) | layer-runtime `[supervise]` |
| unattended | `run-lease.js` | binds a session to its run for the three hooks | RESHAPED | the session binding record (dWellOiledMachine) | the owner, NP-22, 2026-10-18; layer-runtime `[act]` |
| unattended | playbook mode (`--record-piece`, `--record-set`, `check-playbook`) | repeatable content as pieces and sets | RESHAPED | the playbook record kind and `check-playbook` as Design's pack (dIndexedDesign), pieces built as units (dScopedBuild), the set check, registered at Test (dIndexedDesign), a cyclic playbook's filer (dTendedCadence), reached by the `repeat` disposition (dKeptSession) | the owner's point 1 (night pass) |
| unattended | `check-unattended` | the kit's own gate | RETIRED | none: it gates the unattended kit itself, which dissolves at convergence (dConvergedCharter) | the owner, NP-22, 2026-10-18 |
| unattended | `RUNAWAY_CEILING` and the runaway detector | the round-count bound | MERGED | the loop kit's definition, moved in the unit that retires `REVIEW_ROUNDS` (dDeclaredLoop) | v2 `[chain]` dDeclaredLoop; the shape audit, run A's M22 and run B's M5 |
| unattended | `check-pass-order`, `check-brief-recorded` | pass order and brief records | RESHAPED | the work order's hash and the shape-run rows (dBoundRoles) | the owner, NP-22, 2026-10-18; `research-unattended-core.md` |
| unattended | `check-arms-groups` | lints the batched self-test's groups | RETIRED | none: it lints the kit's own self-test file, which dissolves with the kit (dConvergedCharter) | the owner, NP-22, 2026-10-18 |
| unattended | drift and runlog calls, `read_policy_key` | cross-kit edges | RESHAPED | optional slots (dOrderedCharter); re-pointed (dConvergedCharter) | v2 `[chain]` dOrderedCharter; v2 `[chain]` dConvergedCharter |
| unattended | guide templates (PROTOCOL, VERBS, STOPS, ASKS) | the protocol text | RESHAPED | rendered views of the loop's checklists (dConvergedCharter) | v2 `[chain]` dConvergedCharter |
| unattended | the `/unattended` Skill | starts, resumes or closes a run | RETIRED | a client of `run` until dConvergedCharter retires it, unattended being the default state (NP-4) | the owner's point 1 (night pass) |
| hooks | `agent-cap.js` | fan-out guard | STAYS | spawn-guard pack; its arm becomes a fragment; slot reservation added (dWellOiledMachine) | layer-runtime `[enforce]` |
| hooks | `scratch-guard.js` | write gate | STAYS | roles write-gate pack (dBoundRoles, packed by dWellOiledMachine), its card and route reads re-pointed to the session binding (dWellOiledMachine) | layer-runtime `[enforce]` |
| hooks | `format-guard.js` | final-message format | RESHAPED | statement-grammar check (dOrderedCharter) | layer-instruction `[recommendations]`; layer-runtime `[enforce]` |
| process-monitor | reap, scope, classify | reaping | STAYS | Runtime, at the act ceiling (dWellOiledMachine) | layer-runtime `[supervise]`; layer-runtime `[contract]` |
| process-monitor | census, procmon-hook | report | RESHAPED | observability node reading (dTendedCadence) | layer-expansions `[design-observability]` |
| branch-reconcile | report, cleanup Skill | prune report | STAYS | observability's prune fix (dTendedCadence; `[stale]` 9) | layer-runtime `[isolate]` |
| gate-lint | scans | source hygiene | STAYS | leg pack, expansion, less the two below (dWitnessedBar, at Test's leg-pack point) | layer-instruction `[layers]` |
| gate-lint | `encoding_posture.py` and the shell-hygiene mode | Python text IO and shell hygiene | MERGED | the core portability pack, so every P37 rule has a core leg (dWitnessedBar) | v2 `[chain]` dWitnessedBar; the shape audit, run B's M11 |
| pytest-parallel-guardrails | xdist guard | bounded parallel tests | STAYS | an adopter-only Flow leg pack, declared so in gov, which runs no xdist suite (dWitnessedBar) | the owner, NP-22, 2026-10-18 |
| run-gates | `run-gates.sh` | the bar | RESHAPED | runner-written verdict, attribution, held legs by policy, leg factory (dWitnessedBar) | v2 `[chain]` dWitnessedBar |
| run-gates | `gate-legs.json` | leg manifest | RESHAPED | `tag` and `purpose` fields, and one manifest whose rows the leg factory generates from the packs' declarations (dWitnessedBar) | v2 `[chain]` dWitnessedBar; the owner, NP-22, 2026-10-18 |
| run-gates | turnstile | bar semaphore | STAYS | core (dWitnessedBar) | layer-instruction `[layers]` |
| run-gates | `post-merge.sh` | landed-SHA bar | RESHAPED | `deploy.core`; core checks before release (dShippedRelease) | v2 `[chain]` dShippedRelease; layer-expansions `[design-integrations]` |
| run-gates | held halves, WSL, selftests, profile, ceilings | bar tooling | STAYS | `held_halves` re-pointed (dConvergedCharter) | v2 `[chain]` dConvergedCharter |
| run-gates | `regen.py`, `check-receipt.py` | regenerate, receipt | STAYS | `regen.py` re-pointed for a lib descriptor (dShippedRelease) | v2 `[chain]` dShippedRelease |
| run-gates | `read_held_reds` | remote-CI read | RESHAPED | the `verdict:remote-ci` integration (dWitnessedBar, which owns gap-test-13) | layer-expansions `[design-integrations]` |
| govkit | install and update, receipt | copy deploy | RESHAPED | release tags, receipt names its release, `kits.offer` (dShippedRelease) | v2 `[chain]` dShippedRelease |
| govkit | epoch, selfcheck 5c | version arms | MERGED | the one version check (dShippedRelease, which owns gap-tool-02) | gap-tool-02 |
| govkit | `govkit check` | wiring | MERGED | absorbs check-wiring's install arms and check-placeholders (dShippedRelease) | layer-expansions `[design-distribution]` |
| govkit | `adopters.toml` | adopter list | RESHAPED | the fleet register (dShippedRelease) | v2 `[chain]` dShippedRelease; layer-expansions `[design-distribution]` |
| govkit | census, matrix, refusal_join, runbook parity | self-checks | STAYS | runbook becomes derived (dShippedRelease) | layer-memory `[tools]`; v2 `[chain]` dShippedRelease |
| govkit | no descriptor | — | RESHAPED | gets a `kit.toml` (DA-M16) (dShippedRelease) | v2 `[chain]` dShippedRelease |
| lib | resolvers, render-doc, health-log, arms | primitives | STAYS | inline copies generated (gap-tool-04); marked not installable (dShippedRelease) | v2 `[chain]` dShippedRelease |
| top-level | `check-wiring.sh` install arms | wiring | MERGED | govkit (dShippedRelease) | layer-expansions `[design-distribution]` |
| top-level | `check-wiring.sh` session and class arms | session check | RESHAPED | fail-closed class arm (dWellOiledMachine) | layer-runtime `[enforce]` |
| top-level | `check-placeholders.sh` | version lockstep | MERGED | govkit, one version check (dShippedRelease) | layer-expansions `[design-distribution]` |
| top-level | `check-kit-versions.sh` | version markers | MERGED | one version check (dShippedRelease, which owns gap-tool-02) | gap-tool-02 |
| top-level | `check-playbook-parity.sh` | playbook claims | MERGED | the one renderer (dOrderedCharter) | v2 `[chain]` dOrderedCharter |
| top-level | `check-microformats.sh` | micro-formats | RESHAPED | statement-grammar check (dOrderedCharter) | v2 `[chain]` dOrderedCharter; layer-instruction `[recommendations]` |
| top-level | `check-template-size.sh` | size ceilings | RESHAPED | load-set budgets per reader and load point (dOrderedCharter) | v2 `[chain]` dOrderedCharter |
| top-level | `check-agent-cap-restatement.sh` | the fan-out bound restated | RESHAPED | generalised to a policy value restated outside the catalogue (dOrderedCharter) | the owner, NP-22, 2026-10-18; layer-memory `[tools]` |
| top-level | `check-line-length.sh` | prose lines | STAYS | extended by the grammar check (dOrderedCharter, whose statement grammar extends it) | layer-instruction `[recommendations]` |
| top-level | `check-spec-tokens.py` | spec tokens | STAYS | Design's pack (dIndexedDesign) | layer-memory `[tools]` |
| top-level | `check-dead-paths.sh` | dead references | MERGED | into Maintain's dead-pointer detector, which keeps its merge-bar leg (dTendedCadence) | layer-memory `[tools]`; the owner, NP-22, 2026-10-18 |
| top-level | prefix, remotes, hook destinations, placeholders, counts | distribution and test checks | STAYS | packs; two re-pointed (dShippedRelease) | layer-memory `[tools]`; v2 `[chain]` dShippedRelease |
| top-level | `push-main.sh` | the lander | RESHAPED | command adapter and hardening (dWellOiledMachine); landing queue and core re-check (dShippedRelease) | v2 `[chain]` dWellOiledMachine; v2 `[chain]` dShippedRelease |
| top-level | `settings-merge.py` | hook wiring | RESHAPED | one dispatcher entry per event, `onFailure` (dWellOiledMachine) | layer-runtime `[enforce]` |
| top-level | waiver, limit and high-water files | exemptions | RESHAPED | ledger populations (RF-5) (dWitnessedBar) | retrofit `[ledger]`; v2 `[chain]` dWitnessedBar |
| top-level | `help/` pages | user documentation | RESHAPED | rendered from each user-facing unit's `usage` field, with the docs leg (dConvergedCharter) | the owner, SA-5, 2026-10-19 |
| skills | manifest-check card hooks | card | RESHAPED | per-worktree card file (dOrderedCharter); card ref (dPlacedRequest); compact re-inject (dWellOiledMachine) | v2 `[chain]` dOrderedCharter; v2 `[chain]` dPlacedRequest; v2 `[chain]` dWellOiledMachine |
| skills | kickoff procedure | orientation | RESHAPED | orientation scout (dFurnishedOrders); `kickoff.runs` (dRankedPlan); the Skill itself retired (dConvergedCharter) | v2 `[chain]` dFurnishedOrders; v2 `[chain]` dRankedPlan; v2 `[chain]` dConvergedCharter; the owner, SA-9, 2026-10-19 |
| skills | manifest ratchet | the kickoff manifest audit | RESHAPED | the guarded instruction manifest (dOrderedCharter) | the owner, NP-22, 2026-10-18 |
| skills | deploy-governance | operator Skill | RETIRED | no reader, 0 loads; govkit's verbs replace it | layer-instruction `[recommendations]`; gap-tool-05 |
| skills | rendered Skills, five of seven, `/unattended` and `/build` apart | entries | RESHAPED | thin level-4 entries generated from their commands' drive rows and renamed `gov-<name>`: `/gov-recall` and `/gov-runlog` core, `/gov-lexicon`, `/gov-drift-audit` and `/gov-cleanup` with their kits (dConvergedCharter) | layer-instruction `[recommendations]`; layer-runtime `[decide]`; the owner, SK-2, 2026-10-19 |
| skills | the `/session-kickoff` Skill and its per-machine link | the manual kickoff entry, linked from each machine to gov's live checkout | RETIRED | a forwarding stub for `install.deprecation-window` releases, then removed, each node's dangling link reported by its preflight (dConvergedCharter) | the owner, SA-9, 2026-10-19 |
| .githooks | pre-commit | fast leg | RESHAPED | derived list (dWitnessedBar); witness and signal trap (dWellOiledMachine) | v2 `[chain]` dWitnessedBar; v2 `[chain]` dWellOiledMachine |
| .githooks | commit-msg | transition audit | STAYS | gains a signal trap (dWellOiledMachine) | v2 `[chain]` dWellOiledMachine |
| .githooks | pre-push | the bar | RESHAPED | reads the runner verdict; trusted copy; policy re-point (dWitnessedBar, dWellOiledMachine, dConvergedCharter) | v2 `[chain]` dWitnessedBar; v2 `[chain]` dWellOiledMachine; v2 `[chain]` dConvergedCharter |
| .githooks | pre-rebase, straggler-guard | straggler refusal | STAYS | gains a signal trap (dWellOiledMachine) | v2 `[chain]` dWellOiledMachine |
| .githooks | `gate-env.sh` | bar settings | RESHAPED | owner keys folded (dConvergedCharter); mechanics stay | v2 `[chain]` dGroundRules |
| guides | hand-written guides | protocols | RETIRED | rendered views; rationale moves to `help` fields (dConvergedCharter) | v2 `[chain]` dConvergedCharter |
| unattended | the kit as a kit | the unattended-run kit | RETIRED | dissolved: its ladder, transitions and claims into the loop kit (dDeclaredLoop), its supervisor seam, hooks and controls into the runtime's own kit (dWellOiledMachine) | the owner's point 1 (night pass) |
| unattended | slug mode | a run started on a named build | RETIRED | none: every run is a placed request, continue among `entry.place`'s dispositions (dPlacedRequest) | the owner's point 1 (night pass) |
| unattended | ask mode | a run started on ask ids | RETIRED | none: asks enter through Plan's triage (dRankedPlan) | the owner's point 1 (night pass) |

## [stale] Where the records disagreed, and what stands

Dispatch 104 found thirteen places where a later round overtook an earlier verdict, or records disagree. What stands:
1. **`DECISIONS.md`:** `[tools]` retires it, but `layer-memory` `[decisions]` keeps its path with a holds-now view, and
   v2's dTotalRecall row builds that view. The later design stands.
2. **check-wiring:** only its install arms fold into govkit (`layer-expansions` `[design-distribution]`). Its session
   arm stays, with a fail-closed class arm under Runtime (`layer-runtime` `[enforce]`).
3. **workflows:** reshaped by dFairHearing, dBoundRoles and dWellOiledMachine, not kept as is.
4. **push-main, process-monitor and settings-merge:** reshaped, not kept as is, and session-kickoff retired once its
   procedure is reshaped (SA-9). The census of process-monitor moves to observability.
5. **drift-audit:** its seven gateable signals leave it for core and lexicon legs, and its hand-typed lists retire.
6. **The lexicon's pin:** held as a keyed ledger population, not a shrink-only count (v2's dMindYourWords row).
7. **The leg manifest:** decided as one manifest whose rows the leg factory generates from the packs' declarations
   (dWitnessedBar, the owner's NP-22), which keeps `tools/gate-legs.json` the single read source the charter names.
8. **lib:** the class widened to 261 markers over 17 primitives, and lib became the home of the join, ledger and
   extraction factories, with a descriptor that marks it not installable (v2's dShippedRelease row).
9. **branch-reconcile's layer:** observability's prune fix stands (`layer-expansions` `[design-observability]`).
10. **process-monitor's layer:** reaping is Runtime's, and its census observability's. Both stand.
11. **The tooling order:** the instruction layer first (RC-4), not "Flow first".
12. **The design map's kit lines** carried no layer: the map compared prose cells with tags. Fixed in the night pass,
    with an arm seen red (`night-pass` `[instrument]`).
13. **The gap register's owner column** reads "—" throughout. Owners come from v2's `[chain]`, by design.

## [check] How the table stays true

The design map reads this record, as it reads the ownership table:
- each kit line renders its fate from `[kits]` as `fate=`;
- every kit node has a `[kits]` row and at least one `[table]` row;
- every `[table]` row's kit is a kit node, or one of `top-level`, `skills`, `.githooks` and `guides`;
- every fate is in its closed set, for kits and for rows alike;
- every STAYS, RESHAPED or MERGED row names a chain build in "Where it goes";
- every RETIRED row's "Where it goes" names something other than a bare "none";
- no STAYS part sits in a kit whose fate is absorbed or retired;
- the rows match the counts this record states, fate by fate;
- each kit node's `fate` equals its `[kits]` row.

The record is read by name, so a renamed or missing record stops the check, and a row of the wrong width stops it too
(the night pass's closing review, H3, M8 and M14). Each arm is seen red on a planted case (`night-pass`
`[instrument]`). What the check does not do:
- it does not prove that a row's fate is right, only that every part has one, in the closed set, landing in a build
  that exists;
- it does not judge a RETIRED row's replacement or reason, only that one is named;
- it does not catch one part named in two rows under different kits;
- it does not derive the shipped-part population from the tree: convergence's exit check does, over `git
  ls-files` (v2's `[chain]` dConvergedCharter);
- whether each part reaches its fate is dConvergedCharter's exit check (v2's `[chain]`).
