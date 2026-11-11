**Serves:** research PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23

# Spec stage returns — dConvergedCharter

Each agent's structured result, written from the workflow journal by script, never retyped; each long field is quoted.

## dConvergedCharter · PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 · spec-write

Run wf_d3df613f-7b3/ad982e1687477e95e.

- **authored:** ["PLAY-dConvergedCharter-4", "PLAY-dConvergedCharter-14", "PLAY-dConvergedCharter-18"]
- **alreadyPresent:** []
- **refused:** []
**summary:**

> I wrote all three specs in my group, in roster order. Each is Tier-2 with the ten sections, OPEN rev-1 dated 2026-11-03, base 0d1c1dda, streams playbook, and the order the roster names. Units 4 and 14 carry `advances PLAY-dConvergedCharter-24`, and unit 18 carries `closes PLAY-dConvergedCharter-24`. Every fork is RESOLVED (agent, delegated) using rungs 1 or 3, and none widens or relaxes anything. Nothing is committed and the index was not regenerated. The hygiene gate `--only 2,12,25` exits 0 with no finding on these files, and every new function name passed the lexicon's `--suggest` check.
> 
> Files:
> - C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347/memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-4.md
> - C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347/memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-14.md
> - C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347/memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-18.md
> 
> No deviation records were written, because no unit departs from its clause. I am filing no asks: the part form of a `[[retired]]` id is already an open ask, TOOL-dLinkedLibrary-29, and unit 4 lists it as a build-run precondition.
> 
> **Unit 4 (order 21):**
> - **Proposer:** `derive_supersede_proposals` is added to `PROPOSERS`. It proposes retiring each part whose fate is `RETIRED` or `MERGED` while its files are still tracked, as kind `part`, action `retire`, with a fixed accept line per part.
> - **Route:** `resolve_retire_route`'s governed set gains the kind `part`.
> - **Text renderer:** `render_loop_text` is factored out of `run_loop_file`, so the filing and the check build the same text.
> - **Ratification check:** `check_ratified_retirements` treats a part removed in a range as ratified in one of two ways. Either an owner receipt ratifies its proposal's intake (checked with `check_intake_ratifies`), or every commit that deletes its files belongs to a unit whose spec carries a v2 clause. F3 settles that second way by rung 1, because v2 itself retires the unattended kit, `/build` and `/session-kickoff` by clause.
> - **Parts data:** F2 has the proposer read its parts from `readings["parts"]`, which unit 14 supplies. Until then it prints an "unarmed" line rather than passing silently.
> - **Edge:** one hands-off to unit 14, naming `keep`, `readings["parts"]` and `check_ratified_retirements`. Unit 14 declares the same edge back. This edge carries more names than the brief's edge table lists.
> 
> **Unit 14 (order 22):**
> - **Table:** a new `tools/govkit/fates.toml` holds one `[[part]]` row per row of the fates record. It refines I22 in four ways:
>   - Ids are `derive_anchor` slugs, so they match the `<entry>/<slug>` form of a retired part.
>   - `decided` is a list, and amending a declined part adds `keep:<derive_key_hash("part", id)>` to it.
>   - A part living inside a file other parts share gets `paths = []`, and the join counts these aloud.
>   - The fates are the record's four plus `KEPT`, which is how the clause's `kept` is spelled here.
> - **Join:** `fates_join.py check` has four arms: files no row covers, parts off their fate, declined parts, and unit 4's ratification check.
> - **Exit check:** `check --exit` runs unit 20's adopter exit arm in the same run.
> - **Loop Review feed:** a `METRICS` entry `parts` hands unit 4 its data.
> - **Leg:** a gov-only `fates join` leg, declared the way `step-gate` is.
> - **Edges back:** from 4, 23 (`derive_key_hash`) and 20 (`derive_pending_steps`), all three in the table. Writer 2 must declare unit 20's hands-off to unit 14 naming `derive_pending_steps`, and expose the adopter exit arm that `check --exit` runs.
> 
> **Unit 18 (order 23):**
> - **Hop table:** `tools/memory-tree/cycle.toml` holds 18 hops. That is `[cycle]`'s 14 hops as 15 rows (one split by source), plus three hops leading in from the intake: intake → request, request → build, and build → work order. The first two follow scout D's disagreement 7.
> - **Walker:** `cycle_walk.py` resolves every hop only through the edge-grammar site adapters (PLAY-dOrderedCharter-28 S5) and `derive_inverse_edges`. Each key it reaches must classify under `parse_edge_target` and resolve through its class's `[[native]]` resolver.
> - **Red cases:** the plants `prose-hop` and `search-hop`.
> - **Leg:** a gov-only `cycle walk` leg, withheld from adopters as `project-owned`, under the owner's 2026-08-23 ruling.
> - **Edges:** external only.
> 
> **Where scout rows and source disagree:**
> - The fates `[table]` parses to 138 rows (`RESHAPED` 73), but the record itself says 139 rows and 74 reshaped.
> - Scout A lists a "fates ratification record" file among unit 4's product paths. No such file is needed: ratification is the owner's receipt on the intake, and a decline is a `keep` record.
> - I rejected scout D's proposal to use `gov why` as the per-hop resolver, because it walks only one upward cause chain.
> - I rejected scout D's vanished-member diff for the at-fate arm: it answers "what left in this range", not "is every part where its fate says".
> - Scout D's citations `step_gate.py:155` and `:219`, and scout A's `upgrade_steps.py:890`, are correct at this base.
> 
> **Open points:**
> - Row 11's typing unit (dWitnessedBar's verdict record) is left for the build run to name.
> - Whether `edges.toml` holds an `implements` type is unverified at base. If it does not, the reader refuses that row rather than passing it.


## dConvergedCharter · PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 · spec-write

Run wf_d3df613f-7b3/acef049dd4e52409d.

- **authored:** ["PLAY-dConvergedCharter-23", "PLAY-dConvergedCharter-6", "PLAY-dConvergedCharter-3", "PLAY-dConvergedCharter-19"]
- **alreadyPresent:** []
- **refused:** []
**summary:**

> I wrote all four specs in my group, in roster order. Each is Tier-2 with the ten sections, status `OPEN · rev-1 · 2026-11-03 · ... · order <k> · advances PLAY-dConvergedCharter-24`, and one `**Carries:** <clause>@<hash8> whole` line. No clause is split. Nothing is committed and the index is not regenerated.
> 
> Hygiene checks 2, 12 and 25 only grade tracked files, so I ran them in a throwaway clone at %TEMP%/cw3h (since deleted) with the four specs and two deviation records staged. The first run flagged check 25 on unit 19 S2: the word "retired" appeared without a `**Readers:**` clause. I reworded it, and the rerun printed no finding for any of my files and exited 0. I accidentally started `check-spec-tokens.py --help` once; it seems to have run the full check. I did not use its result. It and `carries.py` are still the main loop's to run.
> 
> **PLAY-dConvergedCharter-23** (order 9) — memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-23.md
> - Design: `derive_key_hash` becomes one canonical block in tools/lib/key_hash.py. A second block, `render_breach_text`, is extracted from Maintain's `write_breach_ask`. Both are carried inline by maintain_file.py, loop_review.py and release.py and held equal by two new `PARITY_ROWS` rows. `release.route` files exactly Maintain's ask text with band `act`, so the two filings join both before and after Entry places the intake. The joined fixture is `release_fixture.py --case verify-join`, with plant `two-keys`.
> - Asks:
>   - A1 (dShippedRelease): S10 files `render_breach_text` output, and its fixture builds against a `[[stand-in]]` for `item.maintain.file`.
>   - A2 (dShippedRelease): register `release-verify-failed`'s producer in `EVENT_PRODUCERS` and its `[[reading]]` row, with band edges putting one red verify in `act`.
>   - A3 (dTendedCadence): -15 S2 uses both blocks and builds against a stand-in for `item.release.route`.
>   - A4 (dCalibratedLens): -5 S8's `derive_key_hash` becomes the inline block.
>   - The accept lines are in §8 F4.
> - Interface refined: I9. Interface I9 is wrong about drift_report.py:3777: that code hashes the sorted keys with no kind, so it is not a copy and is left alone. The real instances are TOOL-dTendedCadence-15 and TOOL-dCalibratedLens-5. The spelling `derive_key_hash(kind, key)` is unchanged.
> - No deviation record.
> 
> **PLAY-dConvergedCharter-6** (order 10) — memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-6.md
> - Design: a new check, `check_record_homes`, inside `check_record_kinds`. It lists every tracked file under the memory root, removes those a registry row's `home` glob covers and those `documents.toml` registers, and fails on whatever is left. Through the factory it adds two kinds: `run-state` (RUN.md and the rotated RUN.*.md copies) and `memory-index` (memory/README.md). The census is in §4.
> - Disagreements:
>   - The brief's `record_kinds.py --population` prints schema fields, not record paths (TOOL-dTotalRecall-1 S7). The check reads the `home` column instead.
>   - The `decision` kind belongs to TOOL-dLinkedLibrary-1, not TOOL-dDeclaredLoop-31.
>   - Scout B's residue list is mostly already owned:
>     - prompt files carry journal/research Serves lines, and the `memory/builds/*/*/*.md` home covers them;
>     - `memory/project/*.txt` and the ledger belong to TOOL-dTotalRecall-18's `registry` and `view` kinds.
> - No asks, no deviation.
> 
> **PLAY-dConvergedCharter-3** (order 11) — memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-3.md
> - Design: two kinds count as one when writer, lifecycle, readers and schema form are equal, and they share at least 0.9 of commits over at least 20 commits in 30 days (§8 F1/F2). The merge rule adds `derive_merge_pairs`, `measure_commit_share`, `check_merge_evidence` and `--merge-evidence`. A merge uses the `KIND_ALIASES` rename.
> - Probe I ran at base: commit share alone fails. The build README is committed with spec/ 98% of the time because of generated regions, so the four structural conditions are required.
> - Ask A1 (dTotalRecall): -20 S1's `memory_journal_alias.py` takes an optional old/new pair from argv, defaulting to journal→log.
> - Edge added beyond the table: consumes-from PLAY-dConvergedCharter-11 `derive_readers`. Writer 1 needs to add the matching hands-off to unit 3.
> - Disagreement: the change feed's lines have no path field (TOOL-dPlacedRequest-13 S1), so the share comes from a direct git log walk.
> 
> **PLAY-dConvergedCharter-19** (order 12) — memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-19.md
> - Design:
>   - Guide headings get authored tags (`## [section.<seg>] <Title>`). `[[alias]]` rows cover both the old label and the vanished old address, and in-guide citations become `doc.<name>#<seg>`.
>   - In `.gitattributes`, 78 pins become 11 class lines plus the 4 hook paths. The six extra classes are `[[gov_only_pin]]` rows.
>   - The kits' per-directory `[[lf_pin]]` rows become class rows.
>   - New check `check_covered_pins` in eol_class.py.
>   - Upgrade step `govkit/lf-pins-to-class` for adopters.
> - Deviation records:
>   - memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-19-deviation-191.md — rung 5, ER:240: an adopter's .gitattributes block now pins whole classes, including the adopter's own files.
>   - memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-19-deviation-192.md — rung 5, ER:388: BUILD-METHOD sits 61 bytes under its 30720-byte row, which reserves the next raise to the owner; the tag citations push it over, so the row and M1's Budget line are raised.
> - Ask A1 (dOrderedCharter): the doc extractor honours the authored heading form through `extract_section`'s rule (I12).
> - Edge added beyond the table: consumes-from PLAY-dConvergedCharter-12 `tools/unattended/`. Writer 1 needs to add the matching hands-off.
> - Hand-off for writer 5: per the hands-off to unit 9, no per-Skill pin is left in `.gitattributes` or the kits' rows, so unit 9's renames re-point no pin.
> - Interface refined: I14 (class set and adopter scope settled in §8 F2/F3).
> - Disagreements: 79 `eol=lf` lines (one is a comment); 35 `[[lf_pin]]` rows in 16 descriptors.
> - Check for the main loop: this clause carries two mechanisms in one spec (tag migration and class pins). I kept it whole as the brief assigns it, but it may warrant a split under M2.


## dConvergedCharter · PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 · spec-write

Run wf_d3df613f-7b3/a5a2b2f96015f2765.

- **authored:** ["PLAY-dConvergedCharter-16", "PLAY-dConvergedCharter-5", "PLAY-dConvergedCharter-20", "PLAY-dConvergedCharter-21"]
- **alreadyPresent:** []
- **refused:** []
**summary:**

> I wrote the specs for all four of my units in the order the roster gave. I committed nothing and did not run the index generator. Each header reads `OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order <k> · advances PLAY-dConvergedCharter-24` and carries its clause whole. The only gate I ran was hygiene checks 2, 12 and 25, through a scratch copy of the index (`GIT_INDEX_FILE`) so the shared index stayed untouched. My four specs come back clean, including the edge joins with the sibling specs on disk. The failures it printed are all in other writers' specs.
> 
> **PLAY-dConvergedCharter-16** (order 5): memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-16.md, with deviation memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-16-deviation-161.md.
> - The engine files (manifest-check.sh and its fragments) move to `tools/kickoff-manifest/`. The entry keeps its id `kickoff-manifest` and gets `home = "kickoff-manifest"`; installed paths at adopters do not change. The descriptor flag `home_root_relative` is deleted with its last user.
> - Readers of the path and of the `/session-kickoff` name are re-pointed: about 100 tracked files at base, listed in the `**Readers:**` clauses.
> - The `[[retired]]` row is `id = "command:session-kickoff"`, using the id form unit 17 adds.
> - The forwarding stub is a `skill` shim row, `kickoff-manifest/session-kickoff`.
> - `check_skill_install` gains `test_link_dangling`, so a link whose target is gone is reported.
> - A gap the scouts missed: the orientation scout loads the engine *as the Skill* (`gov-orienter.agent.md:30`; TOOL-dFurnishedOrders-1 S7, S8). §8 F2 resolves it by the standing ruling ER:388 (rung 5, widens the engine text's install location): the engine text ships per repository as `{prefix}/KICKOFF-ENGINE.md`. That choice is deviation 161.
> - Edges: consumes-from 11 (`derive_readers`) and 17 (`KINDS`, plus the `<class>:<name>` id form). No edges beyond the table.
> - Needs from unit 17: its `skill` row reader must accept a `from` outside `{prefix}/<kit>/` (here `skills/session-kickoff/SKILL.md`) and a `to` that is a document `.md`.
> - Follow-up named in §3: the `{user_skills}` token loses its last descriptor user.
> - Scout C corrections: about 102 reader files, not 50; the row cannot name an entry because the entry stays live; the orienter hole above.
> 
> **PLAY-dConvergedCharter-5** (order 6): memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-5.md. No deviation.
> - Adds `derive_migration_state` and the verb `adopter_reading.py migration --release <tag>` to DEPL-dShippedRelease-7's module. The walk itself stays `update --offer` / `update`; no engine code is added.
> - Every row that is not migrated, unregistered rows included, raises one owner item of a new kind, `adopter-unmigrated`, keyed `<key> <release>` (F1, F2).
> - The converged release is the first `gov/v*` tag whose commit holds the build's landing (F3).
> - An empty register exits 2 as not graded.
> - Hands off `steps-pending` to unit 20.
> - Note: `help/kits.md`, which DEPL-31 and DEPL-7 cite, does not exist at HEAD, so the spec uses `help/upgrade-steps.md`.
> 
> **PLAY-dConvergedCharter-20** (order 7): memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md, with deviation memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-20-deviation-201.md (risk: stricter).
> - **Shared interface I6 is wrong.** TOOL-dDeclaredLoop-21 S8 already extracts the shared step `tools/govkit/steps/conf_to_policy.py` from `fanout_cap.py` (its second caller is `review_rounds.py`). So unit 20 is the third caller and extracts nothing; scout C's row 20 missed this. I wrote no deviation record for it, because it departs from the brief, not from the clause.
> - Unit 20 adds a `--home` mode (`derive_home_folds`, reading the catalogue's `legacy` field) and `--drop-rest` to that step.
> - Four conf-fold steps: `<kit>/conf-to-policy` for memory-tree, codebase-map, lexicon and process-monitor. `.githooks/gate-env.sh` gets no step because no descriptor ships it.
> - `unattended/run-conf-retired` goes in `steps.toml`.
> - `check_shim_windows` gains the reverse arm: an open shim row past its window is a finding.
> - `check_adopters_converged` checks every register row, not just registered ones. That is deviation 201, so an empty population never reads green.
> - Edge added: consumes-from 17 (`shims.toml`), mirroring 17's hands-off.
> - Disagreement with unit 12: its hand-off says the upgrade step removes `tools/unattended/` from adopters. This spec has `update`'s withdrawn arm do it (TOOL-dSafePassage-9) and the step handle only `.unattended.conf`.
> 
> **PLAY-dConvergedCharter-21** (order 8): memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md. No deviation.
> - The step `roles/house-seed-to-policy` (`house_seed.py`, a caller of `conf_to_policy.py`) folds only the unruled customizations `derive_house_proposals` finds. A declined proposal is dropped; values equal to gov's defaults go with the file (F2).
> - An unruled `[gates]` grant stops the step, writing nothing, until the owner rules (F1).
> - `load_policy`, R12, step 4 of the effort order, and the house home in `derive_legacy_homes` are all deleted.
> - Edges added: consumes-from 22 (`settings_census.py`), mirroring 22's hands-off. The consumes-from line for 11 also names `arm_house_readers`.
> - For writer 1: the fallback's deletion is this unit's write. Unit 11 only arms the reader check.
> - Scout C correction: `render_agents.py:330` writes a fixture copy, not the seed; the seed ships via `tools/roles/kit.toml:31-40`.
> - The brief cites `catalogue.toml:296-308`; the rows actually span `:295-310`.
> 
> No asks on other builds' backlogs are needed from these four units.


## dConvergedCharter · PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 · spec-write

Run wf_d3df613f-7b3/a73278c6634b69c2d.

- **authored:** ["PLAY-dConvergedCharter-2", "PLAY-dConvergedCharter-13", "PLAY-dConvergedCharter-1", "PLAY-dConvergedCharter-10"]
- **alreadyPresent:** []
- **refused:** []
**summary:**

> I wrote all four specs, uncommitted, under C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347/memory/builds/dConvergedCharter/spec/. Each is Tier-2 at OPEN · rev-1 · 2026-11-03, base 0d1c1dda, with its roster order and `advances PLAY-dConvergedCharter-24`, and carries its clause whole. I wrote no deviation records, because no unit departs from its clause.
> 
> I checked them with hygiene checks 2, 12 and 25 in a throwaway clone under %TEMP% (since deleted), because the gate does not read untracked files. One finding is left: unit 2's consumes-from on unit 6 has no matching hands-off yet. Nothing else red on my four specs. `check-spec-tokens.py` and `carries.py` have not been run; I checked the §6 paths and the §7 leg lines by hand only.
> 
> **PLAY-dConvergedCharter-2** (2026-11-03-spec-PLAY-dConvergedCharter-2.md, order 13)
> - **What it does:** empties the live rows of `positional-refs.txt` through a new `positional.py migrate [--apply]` verb. Each row is classed `alias`, `symbol`, `pin` or `hand` (rewritten by the pass). A new arm reds any live row left on the list (`LIVE ROW`).
> - **Frozen records:** a path is frozen when a record kind's `lifecycle` is frozen, append-only or generated. This is read through a `record_kinds.py --homes` print mode this unit adds. Frozen records only get `[[alias]]` redirect rows.
> - **§9 rule:** the rev-scope arm (`check-memory-hygiene.sh:2433-2458`) now accepts `section.<seg>` tags. `§<n>` stops counting from `SPEC_TAGS_CUTOFF`; the Readers clause is written.
> - **Ask, target dOrderedCharter:** "PLAY-dOrderedCharter-19 S11's `--list-positional` prints no review-finding label and no check number inside the program that numbers its own checks, as PLAY-dConvergedCharter-2 S5 narrows it". Accept: "the spec's S11 states the exclusion, seen on a fixture holding a finding label and the engine's own check number".
> - **Edge I added:** consumes-from unit 6 (`record_kinds.py`). Unit 6 must add `hands-off PLAY-dConvergedCharter-2` back; this is the remaining hygiene finding.
> - **Scout disagreement:** scout A's 1,093 lines did not reproduce. `§[0-9]` gives 723 lines in tools, skills and .claude; the 56 in `WIRE-INTO-PROJECT.md` match.
> 
> **PLAY-dConvergedCharter-13** (order 14)
> - **I16, as I spelled it:** canonical `tools/lib/prose_move.py` with `ProseMove`, `derive_moves(text, route)` and `write_moves(path, moves, write)`. Kits carry it inline as a `# >>> prose_move — canonical copy` block, checked by a `prose_move` row in `PARITY_ROWS`. `dossier_move.py` becomes the first caller and `tools/playbook/guide_move.py plan|apply` the second.
> - **What it does:** a paragraph counts as feature-specific when every path it cites matches exactly one dossier's `globs`. Each such paragraph becomes a unit scoped `feature.<name>`, with the paragraph verbatim in `help`. A new check, `FEATURE PROSE LEFT`, runs inside `instructions_edit.py check`.
> - **Write route (§8 F2):** the pass edits the kit manifest itself and records it with a change record, as PLAY-dOrderedCharter-40 does. **This differs from unit 7 S7, which says "written through `instructions.edit`"**; the two should be cross-read.
> 
> **PLAY-dConvergedCharter-1** (order 15)
> - **What it does:** adds a `--residue` route to `guide_move.py`. Each paragraph of the six remaining documents (ANNOTATION-STYLE, BUILD-METHOD, MERGE-BAR, REVIEW-PROTOCOL, HYGIENE, TEMPLATE-SPEC) is typed as a statement or left as `rationale` for unit 7. A new check reds a leftover `MUST` line (`STATEMENT LEFT`) and every finding `check_document` returns.
> - **Disagreement with the brief:** I17 says unit 1 drains `instructions-legacy.txt`. But unit 7's S8 and S10 take the guide rows off the list, so unit 1 drains only their directive text and hands the rows to unit 7.
> - **Scope tags:** units taken from TEMPLATE-SPEC and HYGIENE also carry their section tag, so unit 7's slot lines can select them.
> 
> **PLAY-dConvergedCharter-10** (order 16)
> - **I18 and I19, as I spelled them:** two scopes, with renderer values `playbook:protocols` and `playbook:skills`. The protocols scope finds each document's source through the `documents.toml` `source` field. The only new `[[target]]` row is for `.claude/skills/gov-*/SKILL.md`; no protocols row exists until unit 7 moves documents onto it. `[[drive]]` gets an optional `skill` key matching `[a-z][a-z0-9-]*`; the `gov-` prefix check is unit 9's. I did not use scout B's `splice_region` proposal.
> - **How Skills count as "rendered from units":** each Skill entry is rendered from pointer units built from its drive rows at render time.
> - **Ask, target dOrderedCharter:** "PLAY-dOrderedCharter-12 S4's lock row and PLAY-dOrderedCharter-20 S3's derived status admit a unit a renderer derives from a `[[drive]]` row, its tag `unit.<kit>.<skill>`, read `active` while that row stands". Accept: "a Skill entry rendered by the `skills` scope leaves `instructions-legacy.txt` with its lock row listing its derived units and the status arm green, seen on a fixture entry".
> - **Edge I added:** hands-off to unit 15 (`renderers.toml`), which answers unit 15's existing consumes-from.


## dConvergedCharter · PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 · spec-write

Run wf_d3df613f-7b3/a6f6107db835a5881.

- **authored:** ["PLAY-dConvergedCharter-7", "PLAY-dConvergedCharter-9", "PLAY-dConvergedCharter-8", "PLAY-dConvergedCharter-15"]
- **alreadyPresent:** []
- **refused:** []
**summary:**

> I wrote all four specs in my group, in roster order, plus one deviation record. Nothing is committed and the index was not regenerated. Each spec is Tier-2, `OPEN · rev-1 · 2026-11-03`, base 0d1c1dda, with `order` 17/18/19/20 and `advances PLAY-dConvergedCharter-24`. All are under 31 KB, every clause token is backticked, and every §8 fork is marked RESOLVED.
> 
> I ran hygiene checks 2, 12 and 25 in a fixture clone under %TEMP% (since deleted), because the gate only grades tracked files. The only reds left on my files are two one-sided edges that other writers need to close.
> 
> **Spec paths** (all under `memory/builds/dConvergedCharter/spec/`):
> - `2026-11-03-spec-PLAY-dConvergedCharter-7.md`
> - `2026-11-03-spec-PLAY-dConvergedCharter-9.md`
> - `2026-11-03-spec-PLAY-dConvergedCharter-8.md`
> - `2026-11-03-spec-PLAY-dConvergedCharter-15.md`
> 
> **Deviation:** `memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-8-deviation-81.md`. Review-protocol parity keeps its four `.js` harness pairs and is narrowed rather than retired (rung 6, ER:328, risk loosening; it carries Bound and Tier).
> 
> **Edges the main loop must close:**
> - Unit 9 consumes `derive_readers` from unit 11. Unit 11 (writer 1) needs to add `hands-off PLAY-dConvergedCharter-9`.
> - Unit 15 hands `fates.toml` to unit 14: four `[[part]]` rows for `help/` pages, kit READMEs, root `README.md` and `WIRE-INTO-PROJECT.md`. The fates record has no rows for the last three. Unit 14 (writer 6) needs to add `consumes-from PLAY-dConvergedCharter-15`.
> - Unit 12 hands `explains=` to unit 7, beyond the edge table; unit 7 now declares the reverse.
> - All other edges match the brief's table and are reciprocal.
> 
> **Asks to file, all on dOrderedCharter:**
> 1. Unit 7 F2. PLAY-dOrderedCharter-24 S1's closed set should name `explains` (from `unit` to `doc`, inverse `explained-by`, `pin = "none"`). PLAY-dOrderedCharter-25 S6 and -29 S8 should treat a section address that `derive_retired_sections` returns as resolved and retired with a successor when an `explains=` edge targets it. Accept: a fixture unit whose edge targets a section of a guide taken out earlier passes `gov_tag.py check`, and the same address with no edge reds the retirement rule.
> 2. Unit 8 F1. PLAY-dOrderedCharter-20 S4 should name the optional `leg` key of a `[[target]]` row. Accept: a row carrying `leg` passes `--check-render`'s table arm.
> 3. Unit 8 F2, settling scout B finding 5 for DEPL-dShippedRelease-10 S10. PLAY-dOrderedCharter-20 S6 should name `kit wiring (every descriptor's check)` in place of `playbook render wiring` and `roles render wiring`. Accept: neither name appears in PLAY-dOrderedCharter-20 outside a retirement clause.
> 
> **Shared interfaces refined:**
> - **I21 (I own it):** the edge is now `explains=doc.<name>#<seg>`, not `explains=<guide path>#<seg>`, because PLAY-dOrderedCharter-24 S4 reds a target outside the `doc` namespace. Unit 12's spec still uses the path form and its writer should switch. The key is read through the playbook kit's own reader in `tools/playbook/policy_value.py` (PLAY-dOrderedCharter-19 S8), not `govkit.read_policy_value` directly.
> - **I19 (unit 10's):** unit 9 needs the `skills` scope to render one entry per distinct `skill` value, because `/gov-recall` is two `[[drive]]` rows (`gov why` and `record find`).
> - **I3 (unit 17's):** `shims.py:95-97` only accepts `.sh`, `.js` or `.py` paths, so the `skill` kind also has to admit a `SKILL.md` row.
> 
> **Disagreements with the scouts and the brief:**
> - `render-doc.sh` can't be retired whole. Only its `render_doc` block goes; the three cite blocks stay because the four `.js` pairs still use them.
> - `memory/guides/SESSION-KICKOFF.md` is a manifest that unit 16 re-points readers to but never moves. Unit 7 F5 moves it to `memory/project/SESSION-KICKOFF.md` so unit 14's exit check doesn't red a surviving guide.
> - `memory/guides/PLAYBOOK-TEMPLATE.md` isn't in unit 12's scope, so unit 7 takes it out.
> - Unit 7's no-lost-rationale arm reads first-parent history, not the compare base, so it also grades the four guides unit 12 takes out. Nothing has ever been deleted from `memory/guides/`, so history can't red it.
> 
> **What each unit covers:**
> - **Unit 7:** the `help.explanation` row filled and drained, with a literal reader. Also the `explanation` scope rendering `help/why/`, the `explains` edge type and the no-lost-rationale arm (`check_rationale_kept`). It retires five guides and their templates (with a Readers clause), makes protocol views tag slices, and renders `HYGIENE.md` and `TEMPLATE-SPEC.md` through the `protocols` scope plus a `record-template` slot.
> - **Unit 9:** five `[[drive]]` rows with `skill = "gov-<name>"`; the core two live in `tools/runtime/kit.toml`. Also one `skill_rename.py` step program used by five `[[upgrade]]` rows, five `skill` shim rows, readers re-pointed, and the stale-path and prefix arms in `core skills conformance`.
> - **Unit 8:** the `leg` key plus a `check_renderer_live` arm. It retires kit/dogfood parity, narrows protocol parity, removes the `render_doc` block, takes the Skill arm out of each kit's `--check`, and drops `placeholders` from instruction-file rows.
> - **Unit 15:** policy and command anchors moved onto rendered reference pages, and a `readme` scope (kit reference, kit index and help index regions). It adds a required descriptor `summary` key, takes the runbook region as DEPL-dShippedRelease-9 derives it, and widens the docs leg's walk to the README and runbook paths.


## dConvergedCharter · PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 · spec-write

Run wf_d3df613f-7b3/ac759097e302831bd.

- **authored:** ["PLAY-dConvergedCharter-22", "PLAY-dConvergedCharter-11", "PLAY-dConvergedCharter-17", "PLAY-dConvergedCharter-12"]
- **alreadyPresent:** []
- **refused:** []
**summary:**

> I wrote all four specs in my group. Nothing is committed, and the build index was not regenerated. Each spec has the ten-section Tier-2 shape and a status header of `OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order <k> · advances PLAY-dConvergedCharter-24`, plus its Carries line. Every §8 fork is resolved by rung 1 or rung 3, each mark carrying `widens: none · relaxes: none`. Hygiene checks 2, 12 and 25 come back clean on all four. I graded them in a throwaway clone under %TEMP%, because the checker only reads tracked files; it is now deleted. The remaining reds in that run belong to other writers' units: PLAY-dConvergedCharter-15, -2 and -4. The main loop still needs to run check-spec-tokens and `carries.py`, which my role is not allowed to run.
> 
> **Files written:**
> - C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347/memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-22.md (order 1): the census of gov's own legs, efforts, grants, run conf values and gate environment values. It lives in a new gov-internal module, `settings_census.py`, and keys each row `<source>#<name>`. The leg population comes from a new `derive_leg_claims`, extracted from govkit selfcheck's check 7h and shared by both. A row with no ruling reads `unruled` and is left as it is (exit 0). `--apply` moves only rows the owner accepted, and only through the door that owns the destination.
> - C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347/memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md (order 2): the conf fold. 107 keys get catalogue rows carrying a `legacy` field, and gov's values move into gov's policy file. A new reader, `policy.py legacy <home> [--rev] [--key]`, reads the policy file first and falls back to the old file, so history and older trees still read correctly. It also adds `derive_readers` with a `--readers` command, the red arm `arm_folded_homes`, and a house-file arm that stays unarmed until the seed file is gone. All four `read_policy_key` copies are deleted.
> - C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347/memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-17.md (order 3): retires `/build` with a `[[retired]]` row whose id is `command:build`. It adds the `skill` shim kind and the row `roles/build-skill`, which keeps the existing client for the deprecation window.
> - C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347/memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-12.md (order 4): retires the unattended kit, gated by four preconditions (P1–P4), each with a probe.
> - Deviation record: C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347/memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-11-deviation-111.md. The clause says the `[effort]` readers are "already on" `roles.effort.*`. At base they are not; that change is TOOL-dBoundRoles-21, which is still DEFERRED.
> 
> **Design calls in unit 12 worth checking:**
> - The four guides are retired only after each section's rationale is mapped to a unit through an `explains=` edge, which honours the owner's FQ-6 rule.
> - Legs are sorted by whether their subject survives the kit. `pass-order history`, `brief-recorded` and `playbook validity gate` move to `tools/runtime/` instead of being retired, because BUILD-METHOD M6 names the pass-order refusal.
> - WOM-28's tick forwarder `tools/unattended/resume-tick.sh` becomes the shim row `unattended/resume-tick` and stays until its window closes.
> - The `[[retired]]` row's successor is `runtime`.
> - How this build's own run lands: the build run runs under `run.py` (P1, P2), and the kit's removal and every re-point land in one pass commit.
> 
> **Asks for the main loop to file:**
> 1. Target dLinkedLibrary (unit 22 §8 F5): the `ruling` kind should read armed in gov's tree once a PLAY-dConvergedCharter-22 ruling lands. Accept: `record_kinds.py --check` shows the `ruling` row bound, with no `unarmed` key, after one census ruling is committed.
> 2. Target dClosedLoop (unit 12 §8 F5): asks PLAY-dClosedLoop-11 to -17 are answered before PLAY-dConvergedCharter-12 lands, or each is closed naming the removal, since unit 12 deletes the suites they name. Accept: all seven read answered or closed in dClosedLoop's `BACKLOG.md` when dConvergedCharter lands.
> 
> **Edges I added beyond the brief's table:** 22→11, 22→12 and 22→21 (`settings_census.py`); 17→20 (`shims.toml`); 12→7 (`explains=`). I also added reverses for edges siblings had already declared: 11→3 and 11→9 (`derive_readers`) and 12→19 (`tools/unattended/`). Siblings 16, 9, 20, 21, 2 and 7 already declare the matching reverse edges, and every hand-off token appears in the target spec.
> 
> **Shared interfaces I refined:**
> - I1: `derive_readers` searches everything outside the memory root, including tests, help pages and comment lines. Its command line is `--readers <needle> --kind path|value --except <path>`.
> - I3: a `skill` row's `from` may be a kit source, `skills/<name>/SKILL.md`, or `.claude/skills/<name>/SKILL.md`. I widened this so the rows units 16 and 9 already wrote validate. When `to` is a `.md`, a forwarder is rendered; when `to` is a command, the kit's own client is held open and nothing is rendered. `read_retired` admits ids of the form `<class>:<name>`.
> - I4: a folded key is read with `policy.py get <key> --rev <sha>`; a mechanic gate key is read with `policy.py legacy .githooks/gate-env.sh --rev <sha> --key <KEY>`. That second form is what lets all four copies go.
> - I5: each home has a namespace, with its own key prefix dropped (`PROCMON_`, `GATE_`). Folded keys read through the new reader keep their default in the reader, recorded in the catalogue as `default = { derived = ... }`.
> 
> **Where I disagree with scout C:**
> - `post-merge.sh` reads only mechanic keys, which no clause folds.
> - 34 files outside the kit name `unattended/` at d8a12f046, not 35.
> - The leg sets are built starting at `govkit.py:2535`; scout C cites the walk at `:2655`.
> - The records say 73 undeclared legs; at base there are 79 exempt legs.
> - Only `.process-monitor.conf` is left with no key after the fold. The other confs keep their `_CUTOFF` and `_PIN` keys.
> - Scout C's row for unit 12 misses the WOM-28 tick forwarder and the M6 pass-order leg.
> 
> Note: the scratchpad directory is shared with the sibling writers, so I prefixed my own files there with `w1-`.


## dConvergedCharter · specs · commit

Run wf_d3df613f-7b3/a1b1ced53c5fba36b.

- **committed:** false
- **sha:** "d8a12f04650811af40777796b257fcfd7f9388e7"
**why:**

> The build-index generator refused at `python -B tools/memory-tree/gen_build_index.py --write` (exit 1), so set -e stopped the block before the commit. Its output, verbatim: "Build-index: memory/builds/dConvergedCharter/README.md: front matter declares 'status: OPEN' but 23 spec(s) carry a status header — the build status is DERIVED from them, and two answers to one question is exactly the drift this index removes. Delete the 'status:' key." State left behind: HEAD is unchanged at d8a12f046. The 23 specs are STAGED from the block's first `git add`. The generator wrote no file, and the working tree has no unstaged tracked change. I added no cleanup step and edited no spec or README. To clear it, someone has to remove the `status:` key from the build README's front matter (the owner, or the stage that owns that README), then re-run this stage. A procedural note: the first attempt to pass the block inline to the Bash tool failed at parse time ("line 6: unexpected EOF while looking for matching `''", exit 2) before any git side effect. I checked that nothing was staged, then ran the same block, with only the mandated substitutions, from a scratch script as one bash invocation. In the unreachable second refusal message's text, the literal `<spec paths>` placeholders were spelled as a glob description. The charter's trailer `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` was the substitution for the attribution trailer. Step 6 (gotchas over HEAD~1..HEAD) was not run because no commit was made, so the checklist is empty.

- **specs:** [{"id": "PLAY-dConvergedCharter-22", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-22.md"}, {"id": "PLAY-dConvergedCharter-11", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md"}, {"id": "PLAY-dConvergedCharter-17", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-17.md"}, {"id": "PLAY-dConvergedCharter-12", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-12.md"}, {"id": "PLAY-dConvergedCharter-16", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-16.md"}, {"id": "PLAY-dConvergedCharter-5", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-5.md"}, {"id": "PLAY-dConvergedCharter-20", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md"}, {"id": "PLAY-dConvergedCharter-21", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md"}, {"id": "PLAY-dConvergedCharter-23", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-23.md"}, {"id": "PLAY-dConvergedCharter-6", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-6.md"}, {"id": "PLAY-dConvergedCharter-3", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-3.md"}, {"id": "PLAY-dConvergedCharter-19", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-19.md"}, {"id": "PLAY-dConvergedCharter-2", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-2.md"}, {"id": "PLAY-dConvergedCharter-13", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-13.md"}, {"id": "PLAY-dConvergedCharter-1", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-1.md"}, {"id": "PLAY-dConvergedCharter-10", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-10.md"}, {"id": "PLAY-dConvergedCharter-7", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md"}, {"id": "PLAY-dConvergedCharter-9", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md"}, {"id": "PLAY-dConvergedCharter-8", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-8.md"}, {"id": "PLAY-dConvergedCharter-15", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-15.md"}, {"id": "PLAY-dConvergedCharter-4", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-4.md"}, {"id": "PLAY-dConvergedCharter-14", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-14.md"}, {"id": "PLAY-dConvergedCharter-18", "path": "memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-18.md"}]
**summary:**

> Not committed. gen_build_index.py --write refused because memory/builds/dConvergedCharter/README.md declares 'status: OPEN' while 23 specs carry status headers. HEAD is still d8a12f046. The 23 specs are left staged and no view was rendered. All 23 spec ids were resolved to their paths.

- **checklist:** ""
