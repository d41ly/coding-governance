---
slug: aMendedFleet
node: a
opened: 2026-10-04
streams: tooling+kickoff+playbook
roster: TOOL+KICK+PLAY
authorized-by: prompt
status: OPEN
ids: TOOL-aMendedFleet-1
---

# aMendedFleet — the 2026-10-04 governance review, every point built as its own unit

## The problem this build exists to solve

A two-wave review of this repo at `ac65de998` found that units converge and the system does not. A
merge dropped two shipped units from main. Remote CI is red on every run. Detectors exist that nothing
consumes, the kits feed the stages almost nothing, and the context a run must read keeps growing. The
owner rules that every point of that review is built, each as its own unit, the data loss resolved
and every red leg fixed. The prompt, the owner's four answers and the report are under `prompts/`.

## Expected improvements

- Main carries the code the 01c22e155 merge dropped, and the lander refuses the next such merge.
- Remote CI goes green on the push bar and on the daily held job.
- The four memory kits rank, budget and feed what each stage needs.
- Drift readings persist and reach the card and the close.
- An agent reads less governance prose before its first line of code.

## Detriments if this is not built

- Main keeps losing shipped work silently, and remote CI stays red, so nobody reads it.
- Detectors keep reporting to nobody, idle work reads as live, and context keeps growing.

## Build-level rules

- One mechanism per unit, as the owner asked; the roster below is the review's every point.
- Data loss: restore from the parent the merge dropped, byte-identical to node d's own restore.
- Red legs: one unit per ROOT CAUSE; unit 7's census adds them with `--rescope --act add`.
- Units another live build already owns are retired WONTDO naming that build's unit as successor.
- Owner acts no run can take are parked, never guessed.
- No spec audit (owner, 2026-10-04); the closing diff review is every spec's first review.
- Every new refusal or gate clause is observed RED on a staged break before it lands.
- Per-unit dispatch is sequential (ratified `parallelism route: none`); specs fan out.
- Classified at kickoff (M2): every unit MISSING.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aMendedFleet-1` | 1 | restore `write_ask_views` and the `--status` verb entry that merge `01c22e155` dropped |
| 2 | `TOOL-aMendedFleet-2` | 1 | replay every merge since 09-01 at definition level and restore any further dropped definition |
| 3 | `TOOL-aMendedFleet-3` | 2 | the lander refuses a merge that drops a definition a parent added, unless a `superseded:` line names it |
| 4 | `TOOL-aMendedFleet-4` | 1 | the govkit acceptance matrix decodes subprocess output as UTF-8 on every host |
| 5 | `TOOL-aMendedFleet-5` | 1 | `transition-audit arms` passes on a clean Linux checkout |
| 6 | `TOOL-aMendedFleet-6` | 1 | the lexicon templates are pinned `eol=lf`, so `lexicon wiring` passes on a clean checkout |
| 7 | `TOOL-aMendedFleet-7` | 1 | a census of the daily held job's red suites by root cause, adding one unit per cause |
| 8 | `TOOL-aMendedFleet-8` | 1 | drift-audit reports `remote_ci_red_streak` |
| 9 | `TOOL-aMendedFleet-9` | 2 | the daily held job's red legs reach the inherited-red HIGH auto-file |
| 10 | `TOOL-aMendedFleet-10` | 2 | `--asks` rows carry the pointer, a 160-byte summary and a `--path` filter, ranked and capped |
| 11 | `TOOL-aMendedFleet-11` | 1 | the review protocol and `tier2-review.js` point reviewers at the filtered asks call |
| 12 | `TOOL-aMendedFleet-12` | 2 | LIVE.md carries a last-touch column and splits ACTIVE from DORMANT |
| 13 | `TOOL-aMendedFleet-13` | 2 | LIVE.md renders LANDED-UNCLOSED from the spec-to-commit join |
| 14 | `TOOL-aMendedFleet-14` | 1 | bulk backlog triage: generated DEFER rows for aged unlabelled asks, fixed-but-OPEN asks disposed |
| 15 | `TOOL-aMendedFleet-15` | 1 | the shrink-only pin on `backlog_asks_unlabelled` is re-armed |
| 16 | `TOOL-aMendedFleet-16` | 2 | `gotchas --for-diff` ranks classes by anchor specificity and cuts in tiers |
| 17 | `TOOL-aMendedFleet-17` | 2 | `tier2-review.js` keeps each finding's bug-class label in the committed appendix |
| 18 | `TOOL-aMendedFleet-18` | 1 | `tier2-review.js` prints one machine shape line with severity counts and output tokens |
| 19 | `TOOL-aMendedFleet-19` | 2 | `--doctor <slug>` prints every failing build-folder rule in one pass |
| 20 | `TOOL-aMendedFleet-20` | 1 | a `--new-spec` skeleton satisfies every active cutoff |
| 21 | `TOOL-aMendedFleet-21` | 2 | a new `*_CUTOFF` must retire an old one |
| 22 | `TOOL-aMendedFleet-22` | 1 | generated views merge neutrally, and month shards drop the Status column |
| 23 | `TOOL-aMendedFleet-23` | 2 | check 19 reports gotcha anchors that select zero paths |
| 24 | `TOOL-aMendedFleet-24` | 1 | dead paths in live build READMEs are reported, and the `DECISIONS.md` pointer is fixed |
| 25 | `TOOL-aMendedFleet-25` | 2 | specs carry a byte ceiling priced against a recorded high-water |
| 26 | `TOOL-aMendedFleet-26` | 1 | a `missing:<ID>` citation form with its own count |
| 27 | `TOOL-aMendedFleet-27` | 1 | recall excludes archived versioned snapshots, and a gold arm is answered by a live charter line |
| 28 | `TOOL-aMendedFleet-28` | 2 | the recall floor grades the served path, terms plus fusion |
| 29 | `TOOL-aMendedFleet-29` | 2 | a recall gold set harvested from spec section-10 probes, de-contaminated, graded at hit@10 |
| 30 | `TOOL-aMendedFleet-30` | 1 | superseded records are labelled in recall output |
| 31 | `TOOL-aMendedFleet-31` | 1 | recall output is trimmed adaptively |
| 32 | `TOOL-aMendedFleet-32` | 1 | recall evicts caches of deleted worktrees first, by last query |
| 33 | `TOOL-aMendedFleet-33` | 1 | the recall README and Skill drop stale typed figures |
| 34 | `TOOL-aMendedFleet-34` | 1 | answer-used is measured offline from query logs and later citations |
| 35 | `TOOL-aMendedFleet-35` | 2 | the map's symbol tier reads shell definitions through the lexicon parser |
| 36 | `TOOL-aMendedFleet-36` | 1 | `reuse_lookup.py` takes a byte budget |
| 37 | `TOOL-aMendedFleet-37` | 2 | dossier freshness is derived from git and reported as a drift signal and at the close |
| 38 | `TOOL-aMendedFleet-38` | 1 | `map_diff --converge`, its sink and its prescriptions are deleted |
| 39 | `TOOL-aMendedFleet-39` | 2 | a harness-hooks inventory, and `git-hooks` holds real hook names only |
| 40 | `TOOL-aMendedFleet-40` | 1 | `baseline.toml` never gains a key against the base |
| 41 | `TOOL-aMendedFleet-41` | 1 | `replay-phrases.py` takes a self-enforced `--floor` |
| 42 | `TOOL-aMendedFleet-42` | 1 | `fan_in` counts canonical-copy install sites, and `map_imports.py` gains a consumer or goes |
| 43 | `TOOL-aMendedFleet-43` | 1 | a generated feature card of at most 1 KB, with measured history moved out of dossiers |
| 44 | `TOOL-aMendedFleet-44` | 1 | dossier prose is linted against typed population counts |
| 45 | `TOOL-aMendedFleet-45` | 1 | reviewers' by-design source is the invariants registry |
| 46 | `TOOL-aMendedFleet-46` | 1 | a reuse miss signal, with its predictor measured first |
| 47 | `TOOL-aMendedFleet-47` | 1 | `run_records_nonterminal_but_merged` honours derived LANDED, and an unused-verb pin drops to 0 |
| 48 | `TOOL-aMendedFleet-48` | 2 | drift readings append to a history file |
| 49 | `TOOL-aMendedFleet-49` | 1 | the unattended close prints the BASE..HEAD drift delta |
| 50 | `TOOL-aMendedFleet-50` | 2 | a monthly escape-ratio report |
| 51 | `TOOL-aMendedFleet-51` | 1 | over-pin signals nobody acts on are retired, with a DEAD-for-N rule |
| 52 | `TOOL-aMendedFleet-52` | 1 | the hand-kept signal compares README names against the registry |
| 53 | `TOOL-aMendedFleet-53` | 1 | the dangling-pointer probe reads the declared auto-memory path |
| 54 | `TOOL-aMendedFleet-54` | 1 | drift reports live builds without activity |
| 55 | `TOOL-aMendedFleet-55` | 1 | drift reports open asks cited by product source |
| 56 | `TOOL-aMendedFleet-56` | 2 | stable-key drift signals move to identity baselines |
| 57 | `TOOL-aMendedFleet-57` | 1 | shrink-only lists are graded against their low-water mark |
| 58 | `TOOL-aMendedFleet-58` | 1 | gate yield per leg is reported from the run journals |
| 59 | `TOOL-aMendedFleet-59` | 1 | timeout retries are grouped by leg across every git dir |
| 60 | `TOOL-aMendedFleet-60` | 2 | a cross-run overlap probe over unmerged remote refs runs at preflight |
| 61 | `TOOL-aMendedFleet-61` | 2 | the CLI version is pinned at preflight and compared on resume, and a missing tick is loud |
| 62 | `TOOL-aMendedFleet-62` | 2 | the history legs grade the run's own range |
| 63 | `TOOL-aMendedFleet-63` | 1 | `--close` and `--abort` render the runlog record themselves |
| 64 | `TOOL-aMendedFleet-64` | 2 | `--fix` writes every kit-version carrier from `version_from` |
| 65 | `TOOL-aMendedFleet-65` | 2 | kit versions are minted at the lander, and the per-branch bump obligation goes |
| 66 | `TOOL-aMendedFleet-66` | 1 | the close lists the open asks that target files the build touched |
| 67 | `TOOL-aMendedFleet-67` | 2 | a read-only worker agent type that omits the charter import |
| 68 | `TOOL-aMendedFleet-68` | 2 | the unattended Skill becomes a router of at most 10 KB |
| 69 | `TOOL-aMendedFleet-69` | 1 | the agent-instructions kit warns past 32 KiB and its stale rows are fixed |
| 70 | `TOOL-aMendedFleet-70` | 1 | a tokens-to-READY report from the run journals |
| 71 | `TOOL-aMendedFleet-71` | 1 | present-tense counts in code comments are swept |
| 72 | `TOOL-aMendedFleet-72` | 1 | the dead `gate-timings.tsv` path is removed |
| 73 | `TOOL-aMendedFleet-73` | 2 | the vague-brief trial arm is run and recorded |
| 74 | `TOOL-aMendedFleet-74` | 2 | path-scoped rules and a budgeted pre-build checklist, after the diet is measured |
| 75 | `TOOL-aMendedFleet-75` | 1 | acceptance-criterion ids join the `New arm:` grammar |
| 76 | `KICK-aMendedFleet-1` | 1 | the orientation card shows the last drift-history row |
| 77 | `KICK-aMendedFleet-2` | 1 | the orientation card shows run overlaps and a stale-CLI note |
| 78 | `KICK-aMendedFleet-3` | 1 | kickoff Step 4 points at the two context commands the build method spells once |
| 79 | `PLAY-aMendedFleet-1` | 2 | the `AGENTS.md` wrapper loses its duplicate registry, repeated catalog and dated history |
| 80 | `PLAY-aMendedFleet-2` | 1 | an experiment's instrument and result rows are committed to its build folder |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-10-04 · streams tooling+kickoff+playbook
ids TOOL-aMendedFleet-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 3 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
