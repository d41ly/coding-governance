# Research: today's tools, function by function, and their fates

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 104's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-8-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`.

---

## 1. Verdict

Several inventories of today's tools exist, but none of them is at function level and carries a fate. Dispatch 26 lists every kit (tool counts, runs, legs, asks), and `layer-memory` `[tools]` derives a kit-level keep / re-engineer / retire table from it, dated 2026-10-15. Since then the expansions, retrofit, systems and audit rounds have changed at least nine of those 25 verdicts, and `[tools]` still states the old ones. The only part-level inventory with a fate is layer-runtime's hook-owner table, and it covers hooks only. The design map's today-nodes are derived live and match the tree, but they carry no fate, and the `layer` link on every kit node is empty (0 of 19). So the inventory helps as a count, but it does not answer the owner's question. The table in section 3 does, at 118 function rows: 26 STAYS, 56 RESHAPED, 19 MERGED, 6 RETIRED, 11 UNDECIDED. None of the 19 kits is retired outright. agent-instructions is absorbed whole, and pytest-parallel-guardrails is undecided.

## 2. Inventories that exist

Abbreviations: `v2:N` is a line of `2026-10-14-...-architecture-v2.md`; the `[chain]` rows sit at 1185 (dGroundRules) to 1200 (dConvergedCharter). `lm`, `li`, `lr`, `lx` and `rf` are layer-memory, layer-instruction, layer-runtime, layer-expansions and retrofit.

| Inventory | Grain | Staleness | Use |
|---|---|---|---|
| Dispatch 26, `research-memory-tooling.md` §1 and §5 | kit, top-level check, Skill; runs, legs, asks, overlaps O1 to O7 | Counts re-measured today still hold (below). Its verdicts predate every later round | the best census, at kit level |
| `lm` `[tools]` 842-872 | 25 kit-level verdict rows | stale in at least 9 rows (section 5) | a summary only, not a disposition |
| `lm` `[current]` 262-278 | the tool population and 7 overlaps | still accurate | evidence |
| `li` `[layers]` kit-to-layer table 222-243 | 19 kit rows: layer, core or expansion | two placements contradicted later (section 5). It is the atlas's and the map's kit source, and its prose layer cells never join (section 6) | the layer map |
| Gap register, implicit loop 15-45 | the stages as a picture, not a tool list | 2026-10-14 | supports "middle deep, ends thin"; holds no fates |
| `lr` `[current]` 118-251 and hook-owner table 590-602 | every hook entry (13), each with its pack and layer | current: 13 entries in `.claude/settings.json` | the only part-level fate inventory |
| `memory/map/features/` (31 dossiers) | feature | gated against the code, so current | job descriptions; no fate |
| `tools/gate-legs.json`, 17 `kit.toml` | leg and file | current | population only |
| `map.py` today-nodes | kit 19, feature 31, hook 17, leg 140 | derived live | no fate field; layer link empty |

The measurements I re-ran:
```
$ python -c "...len(json.load(open('tools/gate-legs.json')))"     -> legs 140
  legs per kit: memory-tree 21, run-gates 14, workflows 9, ...     (matches dispatch 26)
$ git grep -l -E '^\s*resolve_python\s*\(\)\s*\{' | wc -l             -> 73
$ grep -E '^#   unattended[.]sh ' tools/unattended/unattended.sh | awk '{print $3}' | sort -u | wc -l  -> 30
$ git grep -n -E '^\s*read_policy_key\s*\(\)'   -> .githooks/pre-push:1303, tools/push-main.sh:404,
                                                   tools/run-gates/post-merge.sh:168, tools/unattended/unattended.sh:9380
$ map.py --check  -> map: 2166 nodes in 30 namespaces; ... unarmed none   (exit 0)
$ ls -d tools/*/ (19); kit.toml present 17; missing: govkit, lib
```
One small drift: dispatch 26 counts 16 process-monitor files, and 13 are tracked today.

## 3. The disposition

Fates are STAYS, RESHAPED, MERGED, RETIRED and UNDECIDED. "STAYS (kit)" means only the kit-level `[tools]` verdict covers the part; no record names the function itself.

| Kit | Function | Today's job | Fate | Where it goes | Citation |
|---|---|---|---|---|---|
| agent-instructions | harness wiring | one charter file, aliased per harness | RESHAPED | dOrderedCharter's one renderer absorbs the wiring; each harness's files come from dWellOiledMachine's harness adapters | v2:1186; li:227 |
| playbook | `render_playbook.py` | renders the charter template | RESHAPED | dOrderedCharter: the one renderer, the charter in its level-0 envelope | v2:1186 |
| playbook | `adopt-playbook --check` | checks the render's wiring | MERGED | into the one renderer | v2:1186 |
| playbook | `fleet.toml`, `--claim-node` | node registry | RESHAPED | node registry's runtime facts (dWellOiledMachine); fleet identity in the lease grammar (dDeclaredLoop) | v2:1188,1192 |
| roles | `agents/*`, `house/*.md` | role definitions | RESHAPED | twelve core roles with structured fields and typed returns (dBoundRoles) | v2:1189 |
| roles | spec-reviewer, diff-reviewer | two reviewer roles | MERGED | one reviewer with a lens per step | roles:333; v2:1189 |
| roles | gov-session | hands work to another session | MERGED | the prompt writer ("session-handoff template folds") | roles:345 |
| roles | gov-orienter | orientation | RESHAPED | the orientation scout, composing the card in a sidechain | roles:338; v2:1189 |
| roles | `workflows.toml` stages | stage order 0 to 7 | MERGED | the loop kit; its seven readers re-pointed (dDeclaredLoop) | v2:1188 |
| roles | `workflows.toml` entries | workflow table | RESHAPED | shapes registry: kind, fan, checklist, merge, cap (dBoundRoles) | v2:1189 |
| roles | `handoff.py` | hashed prompt file | RESHAPED | a work order per item, hashed into the spawn marker (dBoundRoles) | v2:1189; lr:219 |
| roles | `render_agents.py` | renders agent types | MERGED | the one renderer ("roles render wiring") | v2:1186 |
| roles | `check_roles.py` | role, table and doc agree | RESHAPED | role-by-step matrix joined both ways (dBoundRoles); policy reader re-pointed (dConvergedCharter) | v2:1189,1200 |
| roles | `house/policy.toml` | effort and gates | STAYS | until dConvergedCharter folds it; on dGroundRules's legacy list until then | v2:1185,1189 |
| workflows | `tier2-review.js` | review harness | RESHAPED | presets, opt-in lenses, skeptic batches (dFairHearing), run at breakpoints (dDeclaredLoop) | v2:1187,1188 |
| workflows | `REVIEW-PROTOCOL.template.md` | protocol text | RESHAPED | corrected by dFairHearing, then a rendered view (dConvergedCharter) | v2:1187,1200 |
| workflows | `unattended-build.js`, `unattended-unit.js` | unit harnesses | RESHAPED | role harnesses inside act sessions, the deferral block, persisted returns (dWellOiledMachine) | lr:892; v2:1192 |
| workflows | `review_replay.py` | recall scorer | STAYS | dFairHearing's replays use it | v2:1187 |
| workflows | `drift-audit-*.js` | drift harnesses | UNDECIDED | no record names them | — |
| workflows | `orient-counterfactual.js` | kickoff experiment | UNDECIDED | — | — |
| workflows | four harness checks | syntax, fan-out, join, parity | STAYS (kit) | — | lm:864 |
| memory-tree | scaffold, `--new-build`, `--new-spec` | creates records | RESHAPED | the `record` write command (dTotalRecall) | v2:1190; lm:1144 |
| memory-tree | `gen_build_index.py` | index, README regions | RESHAPED | generated views, README schema, routing region (dTotalRecall); drift import becomes an optional slot (dOrderedCharter) | v2:1190,1186 |
| memory-tree | hygiene gate, `HYGIENE.md` | structural checks | RESHAPED | the kind registry generates the schema checks; `HYGIENE.md` becomes its view (dTotalRecall) | v2:1190; lm:1146 |
| memory-tree | `backlog.py` | asks | STAYS | grammar kept; acceptance at filing and counter-ref ids added (dTotalRecall) | lm:851; v2:1190 |
| memory-tree | `gotchas.py` | bug classes | STAYS | handed by write set (dTotalRecall); check-18 probe becomes an optional slot | v2:1190,1186 |
| memory-tree | `corpus_ids.py` | id grammar | RESHAPED | one exported slug and id grammar, with recall's parser moved in | v2:1186,1190 |
| memory-tree | merge-rows | row-keyed merge driver | STAYS | also merges ledger TSVs (dWitnessedBar) | v2:1193 |
| memory-tree | `transition_audit.py` | check 26 | STAYS | an append-only history population; `read_modes` re-pointed (dConvergedCharter) | rf:218; v2:1200 |
| memory-tree | `check-verdict-epoch.sh` | version dates verdicts | MERGED | the one version check (dShippedRelease, gap-tool-02) | gap-register:170 |
| memory-tree | method, spec and annotation templates | guides | RESHAPED | spec as a tagged contract (dIndexedDesign); guides as views (dConvergedCharter) | v2:1195,1200 |
| memory-tree | method-carriers, slot-limit lists | registries | RESHAPED | ledger populations (dWitnessedBar) | rf:219; v2:1193 |
| memory-tree | `routed_commits`, `check-arms`, `row_grammar`, `migrate_backlog` | various checks | UNDECIDED | only their re-pointings are named | v2:1186 |
| memory-tree | `DECISIONS.md` | decision log | RESHAPED | split by kind; the log keeps its path, with a holds-now view (dTotalRecall) | lm:642; v2:1190 |
| codebase-map | `gen_map.py`, dossiers | inventory map | STAYS | optional component; caller map and symbol anchors added (dTotalRecall) | v2:1190; li:241 |
| codebase-map | `map_lib` join and base | coverage, compare base | MERGED | `tools/lib` join factory (dOrderedCharter, H5) | v2:1186 |
| codebase-map | `reuse_lookup` + agent, rank, replay | reuse ranker | RETIRED | 0 of 24 solved; replaced by the house index via **Reuse:** (dTotalRecall) | lm:702,848 |
| codebase-map | stale-dossier signal | freshness | RESHAPED | observability reading; map freshness (dTendedCadence) | lx:210; v2:1198 |
| codebase-map | `map_diff`, `check_gate_coverage` | range digest, gate check | UNDECIDED | — | — |
| memory-recall | `query.py` | full-text search | RESHAPED | a record finder, `record find` (dTotalRecall) | lm:853; v2:1190 |
| memory-recall | `extract.py` grammar, `recall_conf` | id parser | MERGED | into memory-tree (dOrderedCharter) | v2:1186 |
| memory-recall | `recall-opened.js` | Read observer | RESHAPED | optional hook pack (dWellOiledMachine); shell reads too (dTotalRecall) | lr:599; v2:1190 |
| memory-recall | `bench`, `check-recall`, `union` | retrieval bench | UNDECIDED | — | — |
| lexicon | `lexicon.py` gate and pin | naming gate | RESHAPED | definition classes, keyed debt ledger, forced packs (dMindYourWords) | v2:1191 |
| lexicon | `canon`, `scaffold_lexicon` | vocabulary | RESHAPED | noun canon seeded and frozen; packs chosen by census | v2:1191 |
| lexicon | `subtokens`, tokenizers | splitting | MERGED | `tools/lib` extraction primitive (dTotalRecall, LX-2) | v2:1190 |
| lexicon | its two drift signals | gating | MERGED | the lexicon's leg pack (dMindYourWords) | lx:195; v2:1191 |
| runlog | `runlog_lib` grammar | line grammar | MERGED | the core journal (dWellOiledMachine) | v2:1192; lr:892 |
| runlog | reader, extract, model, prose | reader | STAYS | observability's reader half; role metrics read it (dBoundRoles) | lx:210; v2:1189 |
| runlog | `record.py` | run record | RESHAPED | run-record kind through `record`, owned by dWellOiledMachine | ownership:115; lx:82 |
| drift-audit | seven gateable signals | drift gating | RESHAPED | five core legs and two lexicon legs (dTendedCadence gap-maint-09; dMindYourWords) | lx:190-197,490 |
| drift-audit | report-only signals | readings | RESHAPED | observability detectors with owners (dTendedCadence) | lx:210; v2:1198 |
| drift-audit | `SHRINK_ONLY`, `PINS` lists | hand-typed lists | RETIRED | population index derived from the ledger (dWitnessedBar) | rf:270-272 |
| drift-audit | dangling-pointer signal | dead pointers | RESHAPED | Maintain's detector (dTendedCadence) | v2:1198; lm:867 |
| drift-audit | remote-CI signal | dead today | RESHAPED | fixed (dTendedCadence, gap-maint-11) | lx:492 |
| unattended | `--plan`, `--status` | position | MERGED | loop kit position engine (dDeclaredLoop) and `next` (dWellOiledMachine) | v2:1188,1192 |
| unattended | transition verbs (brief, review, pass, landed, close, park, settle) | run state | RESHAPED | per-level transition tables and the transition record (dDeclaredLoop) | v2:1188 |
| unattended | `--hold`, `--resume`, `--abort` | owner control | RESHAPED | pause, resume, withdraw, supersede (dWellOiledMachine) | lr:348-350 |
| unattended | `--claims`, `--overlaps` | run claims | MERGED | the one lease grammar (dDeclaredLoop) | v2:1188 |
| unattended | `--authorization`, `--attest` | mandate | RESHAPED | the plan ratification is the mandate (dRankedPlan) | v2:33,1194 |
| unattended | `resume-tick.sh` | out-of-process resumer | RESHAPED | the supervisor (dWellOiledMachine) | lr:356 |
| unattended | `RESUME_SCHEDULE_*` | desktop restart task | RETIRED | the node tick hosts the supervisor | lr:370 |
| unattended | `gate-guard.js` | run guard | RESHAPED | dispatcher pack (dWellOiledMachine) | lr:595 |
| unattended | `stop-guard.js`, cron keepalive | continuation | RETIRED | for act sessions and cadence; the supervisor's beat replaces them | lr:600,785 |
| unattended | `stall-recorder.js` | API-stall record | STAYS | the supervisor's limit signal | lr:395 |
| unattended | `run-lease.js` | hook binder | UNDECIDED | — | — |
| unattended | playbook mode (record-piece, record-set, `check-playbook`) | repeatable content | UNDECIDED | the record says only that Maintain never rides it | v2:1198 |
| unattended | check-unattended, pass-order, brief-recorded, arms-groups | kit legs | UNDECIDED | — | — |
| unattended | drift and runlog calls, `read_policy_key` | cross-kit edges | RESHAPED | optional slots (dOrderedCharter); re-pointed (dConvergedCharter) | v2:1186,1200 |
| unattended | guide templates, Skill | protocol | RESHAPED | views (dConvergedCharter); the Skill becomes a client of `run` | v2:1200; lr:352 |
| hooks | `agent-cap.js` | fan-out guard | STAYS | spawn-guard pack; its arm becomes a fragment; slot reservation added | lr:578,592 |
| hooks | `scratch-guard.js` | write gate | STAYS | roles write-gate pack | lr:594 |
| hooks | `format-guard.js` | final-message format | RESHAPED | statement-grammar check (dOrderedCharter) | li:487-489; lr:601 |
| process-monitor | reap, scope, classify | reaping | STAYS | Runtime, at the act ceiling | lr:383,892 |
| process-monitor | census, procmon-hook | report | RESHAPED | observability node reading | lx:210 |
| branch-reconcile | report, cleanup Skill | prune report | STAYS | expansion; its layer is disputed (section 5) | lr:717 |
| gate-lint | scans | source hygiene | STAYS | leg pack, expansion | li:232 |
| pytest-parallel-guardrails | xdist guard | bounded parallel tests | UNDECIDED | "Demote"; gap-tool-05's owner clause is silent | lm:872; v2:1200 |
| run-gates | `run-gates.sh` | the bar | RESHAPED | runner-written verdict, attribution, held legs by policy, leg factory (dWitnessedBar) | v2:1193 |
| run-gates | `gate-legs.json` | leg manifest | RESHAPED | `tag` and `purpose` fields (dWitnessedBar); JSON-or-packs UNDECIDED | v2:1193 |
| run-gates | turnstile | bar semaphore | STAYS | core | li:235 |
| run-gates | `post-merge.sh` | landed-SHA bar | RESHAPED | `deploy.core`; core checks before release (dShippedRelease) | v2:1197; lx:342 |
| run-gates | held halves, WSL, selftests, profile, ceilings | bar tooling | STAYS (kit) | `held_halves` re-pointed (dConvergedCharter) | v2:1200 |
| run-gates | `regen.py`, `check-receipt.py` | regenerate, receipt | STAYS | `regen.py` re-pointed for a lib descriptor | v2:1197 |
| run-gates | `read_held_reds` | remote-CI read | RESHAPED | the `verdict:remote-ci` integration | lx:322 |
| govkit | install and update, receipt | copy deploy | RESHAPED | release tags, receipt names its release, `kits.offer` (dShippedRelease) | v2:1197 |
| govkit | epoch, selfcheck 5c | version arms | MERGED | the one version check | gap-register:170 |
| govkit | `govkit check` | wiring | MERGED | absorbs check-wiring's install arms and check-placeholders | lx:435 |
| govkit | `adopters.toml` | adopter list | RESHAPED | the fleet register | v2:1197; lx:427 |
| govkit | census, matrix, refusal_join, runbook parity | self-checks | STAYS (kit) | runbook becomes derived | lm:860; v2:1197 |
| govkit | no descriptor | — | RESHAPED | gets a `kit.toml` (DA-M16) | v2:1197 |
| lib | resolvers, render-doc, health-log, arms | primitives | STAYS | inline copies generated (gap-tool-04); marked not installable | v2:1197 |
| top-level | `check-wiring.sh` install arms | wiring | MERGED | govkit | lx:435 |
| top-level | `check-wiring.sh` session and class arms | session check | RESHAPED | fail-closed class arm (dWellOiledMachine) | lr:575 |
| top-level | `check-placeholders.sh` | version lockstep | MERGED | govkit, one version check | lx:435 |
| top-level | `check-kit-versions.sh` | version markers | MERGED | one version check | gap-register:170 |
| top-level | `check-playbook-parity.sh` | playbook claims | MERGED | the one renderer | v2:1186 |
| top-level | `check-microformats.sh` | micro-formats | RESHAPED | statement-grammar check | v2:1186; li:487 |
| top-level | `check-template-size.sh` | size ceilings | RESHAPED | load-set budgets per reader and load point | v2:1186 |
| top-level | `check-agent-cap-restatement.sh` | restated bound | UNDECIDED | `[tools]` says generalise; no clause carries it | lm:862 |
| top-level | `check-line-length.sh` | prose lines | STAYS | extended by the grammar check | li:487-489 |
| top-level | `check-spec-tokens.py` | spec tokens | STAYS | Design's pack | lm:869 |
| top-level | `check-dead-paths.sh` | dead references | STAYS | the shared function is undecided | lm:867 |
| top-level | prefix, remotes, hook destinations, placeholders, counts | distribution and test checks | STAYS | packs; two re-pointed (dShippedRelease) | lm:870; v2:1197 |
| top-level | `push-main.sh` | the lander | RESHAPED | command adapter and hardening (dWellOiledMachine); landing queue and core re-check (dShippedRelease) | v2:1192,1197 |
| top-level | `settings-merge.py` | hook wiring | RESHAPED | one dispatcher entry per event, `onFailure` | lr:573 |
| top-level | waiver, limit and high-water files | exemptions | RESHAPED | ledger populations (RF-5) | rf:216-221; v2:1193 |
| skills | manifest-check card hooks | card | RESHAPED | per-worktree card file (dOrderedCharter); card ref (dDeclaredLoop); compact re-inject (dWellOiledMachine) | v2:1186,1188,1192 |
| skills | kickoff procedure | orientation | RESHAPED | orientation scout (dBoundRoles); `kickoff.runs` (dRankedPlan); thin entry | v2:1189,1194,1200 |
| skills | manifest ratchet | manifest audit | UNDECIDED | — | — |
| skills | deploy-governance | operator Skill | RETIRED | no reader, 0 loads; govkit's verbs replace it | li:517; gap-register:173 |
| skills | rendered Skills (7) | entries | RESHAPED | thin level-4 entries; build and unattended become clients of `next` and `run` | li:506-519; lr:352 |
| .githooks | pre-commit | fast leg | RESHAPED | derived list (dWitnessedBar); witness and signal trap (dWellOiledMachine) | v2:1193,1192 |
| .githooks | commit-msg | transition audit | STAYS | gains a signal trap | v2:1192 |
| .githooks | pre-push | the bar | RESHAPED | reads the runner verdict; trusted copy; policy re-point | v2:1193,1192,1200 |
| .githooks | pre-rebase, straggler-guard | straggler refusal | STAYS | gains a signal trap | v2:1192 |
| .githooks | `gate-env.sh` | bar settings | RESHAPED | owner keys folded (dConvergedCharter); mechanics stay | v2:1185 |
| guides | hand-written guides | protocols | RETIRED | rendered views; rationale moves to `help` fields (dConvergedCharter) | v2:1200 |

## 4. Kit summary

Counts are STAYS / RESHAPED / MERGED / RETIRED / UNDECIDED.

- **Survive as core engine kits, reshaped:**
  - roles 1/5/4/0/0
  - workflows 2/3/0/0/2
  - memory-tree, which becomes the memory contract's engine and absorbs recall's grammar: 4/7/1/0/1
  - unattended, which becomes Runtime's supervisor; its ladder, transitions and claims go to the loop kit: 1/7/2/2/3
  - hooks, which becomes the dispatcher: 2/1/0/0/0
  - process-monitor 1/1/0/0/0
  - run-gates 3/4/0/0/0
  - playbook, the instruction engine (li:111): 0/2/1/0/0
  - lib, the home of three new factories: 1/0/0/0/0
- **Survive as expansion or optional kits:**
  - codebase-map 1/1/1/1/1
  - memory-recall 0/2/1/0/1
  - lexicon 0/2/2/0/0
  - runlog 1/1/1/0/0
  - drift-audit 0/4/0/1/0
  - govkit 1/3/2/0/0
  - branch-reconcile 1/0/0/0/0
  - gate-lint 1/0/0/0/0
- **Absorbed whole:** agent-instructions 0/1/0/0/0.
- **The loop kit is new** (dDeclaredLoop). It takes 4 parts merged from roles and unattended (the stage table, the ladder, the claims) and reshapes unattended's transition verbs.
- **No kit is retired.** pytest-parallel-guardrails is 0/0/0/0/1.
- **Not in kits:**
  - top-level `tools/` 4/6/4/0/1
  - `skills/` and rendered Skills 0/3/0/1/1
  - `.githooks` 2/3/0/0/0
  - guides 0/0/0/1/0
- **Totals:** 26 / 56 / 19 / 6 / 11, over 118 rows.

## 5. Contradictions and stale verdicts

1. **DECISIONS.md.** `[tools]` says "Retire" (lm:850). `[decisions]` says "The log keeps its path" (lm:642), and v2:1190 builds a holds-now view of it.
2. **check-wiring.** `[tools]` folds it whole into govkit (lm:860). Later records keep its session arm and add a fail-closed class arm under Runtime (lr:575), and fold only its install arms into govkit (lx:435).
3. **workflows.** `[tools]` says "Keep" (lm:864). dFairHearing, dBoundRoles and dWellOiledMachine each reshape it (v2:1187,1189,1192).
4. **push-main, session-kickoff, process-monitor, settings-merge.** `[tools]` says "Keep, live and needed" (lm:866). All four are reshaped (rows above), and process-monitor's census moves to observability (lx:210).
5. **drift-audit.** `[tools]` says "Keep" (lm:867). It loses its seven gateable signals (lx:190-197) and its hand-typed lists (rf:270).
6. **lexicon.** `[tools]` says the pin "becomes shrink-only" (lm:854). v2:1191 says the pin is held as a keyed ledger population, never as a count.
7. **run-gates.** `[tools]` says "legs read from the kit packs" (lm:857). v2:1193 keeps `gate-legs.json`, adds `tag` and `purpose` fields and reviews its 140 legs, and the charter's Facts single-source the JSON. gap-tool-01 is owned by dWitnessedBar, but no clause picks the direction: UNDECIDED.
8. **lib.** `[tools]` covers only the 73 copies (lm:861). Since then, the record widened the class to 261 markers over 17 primitives (gap-register:172), lib became home to the join, ledger and extraction factories (v2:1186,1193,1190), and it gains a non-installable `kit.toml` (v2:1197).
9. **branch-reconcile's layer.** Records say Runtime expansion (li:240, lr:717) and observability engine kit (lx:210).
10. **process-monitor's layer.** Records say "core" (li:237) and also move its census to observability (lx:210).
11. **The order.** `[tools]` still states "Flow first" (lm:874). It is superseded by RC-4, instruction first (v2 `[owed]`).
12. **Record against code: the map.** The map renders kit nodes with a `layer` link, but `map.py`:193-216 compares li's prose cells ("Instruction: renders the charter") and compound keys ("codebase-map, lexicon, memory-recall") with lowercase tags. My probe found 0 of 19 kits with a layer link, and `--check` stays green.
13. **Gap register.** Its owner column reads "—" for every gap, so the tooling gaps get their owners only from `[chain]`. That is not a contradiction, but the register alone states no fate.

## 6. Keeping it current

Three candidates, each with the test that could make it lose:

- **C. Derive each fate from `[chain]` by name.** It loses if most parts go unnamed. Measured: 15 of 19 kits and 31 of 147 non-test scripts are named in `[chain]`. **Rejected.**
- **B. A `fate` field on the product descriptors** (`kit.toml`, leg rows, hook fragments). It loses if any today-node has no descriptor that can be written now. govkit and lib have no `kit.toml`, and the brief's non-goals forbid writing under `tools/`. **Rejected for now.** It becomes the right home once dShippedRelease's kit factory (gap-tool-07, DA-M16), dWitnessedBar's leg `purpose` field and dWellOiledMachine's pack fields land.
- **A. A disposition table in a dClosedLoop record, read by `map.py` as declared `fate` and `into` links on today-nodes.** It is read the way the ownership table already feeds `OWNED` and `DECLARED` (`map.py`:37-39). It loses if today-nodes cannot key function rows. Measured: no function namespace exists (kit, feature, hook and leg only), so function rows need a key such as `kit.unattended#plan-ladder` under their kit node. **Survives with that key.**

**Recommendation: A.** The fate should be a declared field, never derived, joined both ways. The `map.py --check` arms that would hold it:

1. Every kit, hook and leg node has at least one row, and every feature node is covered through its kit.
2. Every row's key resolves to a today-node, so there are no ghost rows.
3. `fate` is one of the five values.
4. A STAYS, RESHAPED or MERGED row names a chain build. Where it names an owned node (item, policy key, point, record kind, tag namespace or system), that node's owner equals that build.
5. A RETIRED row names its replacement, or `none` with a reason.
6. In reverse, every owned node or `[chain]` clause that names a today-part is matched by that part's row.
7. UNDECIDED rows are counted and exit 2, the way an unarmed namespace does, so they never read green.

Each arm needs a planted case that turns it red (drop-row, ghost-row, wrong-owner, empty-into), and so does the empty-layer case from section 5 item 12, which the current check misses.

The key files, under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`:
- `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`
- `2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md`
- `2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`
- `2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`
- `2026-10-17-build-PLAY-dClosedLoop-1-map.py`
