---
slug: aMendedFleet
node: a
opened: 2026-10-04
streams: tooling+kickoff+playbook
roster: TOOL+KICK+PLAY
authorized-by: prompt
ids: KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-95 TOOL-aMendedFleet-96 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 TOOL-aMendedFleet-106
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
- A pass touching a kickoff-manifest watched path re-stamps `last-audit` in its own commit, re-reads
  §B, and advances `last-body-change`.
- Dispatch follows the M2 cross-read's ordering constraints, not roster order.
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
| 70 | `TOOL-aMendedFleet-70` | 1 | a tokens-to-READY report from session transcripts |
| 71 | `TOOL-aMendedFleet-71` | 1 | present-tense counts in code comments are swept |
| 72 | `TOOL-aMendedFleet-72` | 1 | the dead `gate-timings.tsv` path is removed |
| 73 | `TOOL-aMendedFleet-73` | 2 | the vague-brief trial arm is run and recorded |
| 74 | `TOOL-aMendedFleet-74` | 2 | a dark, opt-in pre-build bug-class checklist in the unit harness |
| 75 | `TOOL-aMendedFleet-75` | 1 | acceptance-criterion ids join the `New arm:` grammar |
| 76 | `KICK-aMendedFleet-1` | 1 | the orientation card shows the last drift-history row |
| 77 | `KICK-aMendedFleet-2` | 1 | the orientation card shows run overlaps and a stale-CLI note |
| 78 | `KICK-aMendedFleet-3` | 1 | kickoff Step 4 points at the two context commands the build method spells once |
| 79 | `PLAY-aMendedFleet-1` | 2 | the `AGENTS.md` merge-bar section moves to a guide, without its repeated catalog or dated history |
| 80 | `PLAY-aMendedFleet-2` | 1 | an experiment's instrument and result rows are committed to its build folder |
| 81 | `TOOL-aMendedFleet-81` | 1 | the month shards carry only Build, Node and Opened, so the frozen claim holds |
| 82 | `TOOL-aMendedFleet-82` | 1 | each recall query-log row carries the worktree HEAD, so a later commit is found by ancestry |
| 83 | `TOOL-aMendedFleet-83` | 1 | the unattended close lists the dossiers its range touched and did not refresh |
| 84 | `TOOL-aMendedFleet-84` | 1 | a build README's generated regions stay inside the README cap at any roster size |
| 85 | `TOOL-aMendedFleet-85` | 1 | the template stops overclaiming what the codebase map covers |
| 86 | `TOOL-aMendedFleet-86` | 1 | the map digest reports code coverage apart from record coverage |
| 87 | `TOOL-aMendedFleet-87` | 1 | a query joins gate legs to the paths they guard |
| 88 | `TOOL-aMendedFleet-88` | 1 | `map_imports.py` is deleted, having no consumer |
| 89 | `TOOL-aMendedFleet-89` | 1 | measured history moves out of the dossiers near the byte cap |
| 90 | `TOOL-aMendedFleet-90` | 1 | a report-only drift signal DEAD for N readings is retired or filed |
| 91 | `TOOL-aMendedFleet-91` | 1 | a spec header can declare a records-only deliverable |
| 92 | `TOOL-aMendedFleet-92` | 2 | check 23 grades the run's own range under a per-build budget |
| 93 | `TOOL-aMendedFleet-93` | 2 | one tier2 run is A/B-tested with and without the charter import, and the default follows the result |
| 94 | `PLAY-aMendedFleet-3` | 1 | the charter's wiring rule states a version-neutral reason instead of which file Claude Code reads |
| 95 | `TOOL-aMendedFleet-94` | 2 | path-scoped rules for editing areas, after the diet is measured |
| 96 | `KICK-aMendedFleet-4` | 1 | the orientation card notes a PATH CLI older than the running session |
| 97 | `PLAY-aMendedFleet-4` | 1 | the `AGENTS.md` wrapper carries one node registry |
| 98 | `TOOL-aMendedFleet-97` | 1 | held-red C1: the kits' Python stdio is UTF-8 on a host whose code page is cp1252 |
| 99 | `TOOL-aMendedFleet-98` | 1 | held-red C2: a Python suite's `bash` resolves to Git-Bash, never the System32 WSL launcher |
| 100 | `TOOL-aMendedFleet-99` | 1 | held-red C3: the held job runs its suites from the tree path the bar job uses |
| 101 | `TOOL-aMendedFleet-100` | 1 | held-red C4: the shard 2/8 fixture commits under its own git identity |
| 102 | `TOOL-aMendedFleet-101` | 1 | held-red C5: the G0 fixture writes the grant path its greps expect |
| 103 | `TOOL-aMendedFleet-102` | 1 | held-red C6: the inline `resolve_kit_dir` copies match their canonical source |
| 104 | `TOOL-aMendedFleet-103` | 1 | held-red C7: the python-parity arm exempts `GRAMMAR_WHERE` beside `GRAMMAR_DIR` |
| 105 | `TOOL-aMendedFleet-104` | 1 | held-red C8: `review_replay.py --selftest` honours the foreign-prefix probe or is declared whole |
| 106 | `TOOL-aMendedFleet-105` | 1 | held-red C9: the census live-tree arm's kill is not refused on the hosted runner |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 106 unit(s) · node a · opened 2026-10-04 · streams tooling+kickoff+playbook
ids KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6
ids TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20
ids TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34
ids TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48
ids TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62
ids TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81
ids TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-95
ids TOOL-aMendedFleet-96 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 TOOL-aMendedFleet-106

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aMendedFleet-1 — restore the views helper and the `--status` entry merge 01c22e155 lost](spec/2026-10-04-spec-TOOL-aMendedFleet-1.md) | 1 | 1 | CLOSED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-2 — a definition-level census of every merge since 2026-09-01](spec/2026-10-04-spec-TOOL-aMendedFleet-2.md) | 2 | 1 | CLOSED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-3 — the lander refuses a merge that loses a definition a parent carried](spec/2026-10-04-spec-TOOL-aMendedFleet-3.md) | 3 | 2 | CLOSED | rev-4 | 2026-10-05 |
| [TOOL-aMendedFleet-4 — the govkit acceptance matrix reads its children as UTF-8 on every host](spec/2026-10-04-spec-TOOL-aMendedFleet-4.md) | 4 | 1 | CLOSED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-5 — `transition-audit arms` passes on the hosted runner: the audit writes UTF-8](spec/2026-10-04-spec-TOOL-aMendedFleet-5.md) | 5 | 1 | CLOSED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-6 — `lexicon wiring` passes on the hosted runner: the conf reader writes UTF-8](spec/2026-10-04-spec-TOOL-aMendedFleet-6.md) | 6 | 1 | CLOSED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-7 — a census of the daily held job's red suites by root cause, adding one unit per cause](spec/2026-10-04-spec-TOOL-aMendedFleet-7.md) | 7 | 1 | CLOSED | rev-4 | 2026-10-05 |
| [TOOL-aMendedFleet-8 — drift-audit reports `remote_ci_red_streak`](spec/2026-10-04-spec-TOOL-aMendedFleet-8.md) | 8 | 1 | CLOSED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-9 — the daily held job's red suites reach the inherited-red HIGH auto-file](spec/2026-10-04-spec-TOOL-aMendedFleet-9.md) | 9 | 2 | CLOSED | rev-3 | 2026-10-05 |
| [TOOL-aMendedFleet-10 — `--asks` rows carry the pointer and a 160-byte summary, and `--path` ranks and caps them](spec/2026-10-04-spec-TOOL-aMendedFleet-10.md) | 10 | 2 | CLOSED | rev-3 | 2026-10-05 |
| [TOOL-aMendedFleet-11 — the review protocol and the review harness point reviewers at the filtered asks call](spec/2026-10-04-spec-TOOL-aMendedFleet-11.md) | 11 | 1 | CLOSED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-12 — LIVE.md carries each build's last record date and splits ACTIVE from DORMANT](spec/2026-10-04-spec-TOOL-aMendedFleet-12.md) | 12 | 2 | CLOSED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-13 — LIVE.md counts each build's landed-unclosed units from drift-audit's own join](spec/2026-10-04-spec-TOOL-aMendedFleet-13.md) | 13 | 2 | CLOSED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-14 — bulk backlog triage: aged unlabelled asks deferred on one triage ask, and five fixed-but-OPEN asks disposed](spec/2026-10-04-spec-TOOL-aMendedFleet-14.md) | 14 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-15 — the shrink-only pin on `backlog_asks_unlabelled` is re-armed](spec/2026-10-04-spec-TOOL-aMendedFleet-15.md) | 15 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-16 — `gotchas.py --for-diff` ranks classes by anchor specificity and cuts in tiers](spec/2026-10-04-spec-TOOL-aMendedFleet-16.md) | 16 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-17 — `tier2-review.js` keeps each finding's bug-class label in the committed appendix](spec/2026-10-04-spec-TOOL-aMendedFleet-17.md) | 17 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-18 — `tier2-review.js` prints one machine shape line with severity counts and output tokens](spec/2026-10-04-spec-TOOL-aMendedFleet-18.md) | 18 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-19 — `gen_build_index.py --doctor <slug>` prints every failing build-folder rule in one pass](spec/2026-10-04-spec-TOOL-aMendedFleet-19.md) | 19 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-20 — `--new-spec` writes a skeleton that already carries every shape a cutoff demands](spec/2026-10-04-spec-TOOL-aMendedFleet-20.md) | 20 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-21 — a cutoff budget: armed `*_CUTOFF` keys are a pinned drift signal, so a new one must displace an old one](spec/2026-10-04-spec-TOOL-aMendedFleet-21.md) | 21 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-22 — the generated views merge by taking one side](spec/2026-10-04-spec-TOOL-aMendedFleet-22.md) | 22 | 1 | SPECCED | rev-3 | 2026-10-04 |
| [TOOL-aMendedFleet-23 — check 19 reports the gotcha anchors that select no tracked path](spec/2026-10-04-spec-TOOL-aMendedFleet-23.md) | 23 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-24 — dead repo paths in live build READMEs are reported, and the decision log's dead pointer is repaired](spec/2026-10-04-spec-TOOL-aMendedFleet-24.md) | 24 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-25 — live specs carry a declared byte ceiling, and a spec already over it is held at its recorded high-water](spec/2026-10-04-spec-TOOL-aMendedFleet-25.md) | 25 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-26 — a `missing:` citation form names an id that has no record, with its own count](spec/2026-10-04-spec-TOOL-aMendedFleet-26.md) | 26 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-27 — recall excludes archived versioned snapshots by a declared pattern, and an arm proves a live line answers instead](spec/2026-10-04-spec-TOOL-aMendedFleet-27.md) | 27 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-28 — the recall floor grades the served path, terms plus fusion](spec/2026-10-04-spec-TOOL-aMendedFleet-28.md) | 28 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-29 — a recall gold set harvested from spec §10 probes, de-contaminated, graded at hit@10](spec/2026-10-04-spec-TOOL-aMendedFleet-29.md) | 29 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-30 — superseded records are labelled in recall output](spec/2026-10-04-spec-TOOL-aMendedFleet-30.md) | 30 | 1 | WONTDO | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-31 — recall output keeps every hit and prints snippets only for the head](spec/2026-10-04-spec-TOOL-aMendedFleet-31.md) | 31 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-32 — recall cache eviction removes deleted worktrees first and orders the rest by last query](spec/2026-10-04-spec-TOOL-aMendedFleet-32.md) | 32 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-33 — the recall README and Skill stop typing corpus figures, and a miss re-queries before grep](spec/2026-10-04-spec-TOOL-aMendedFleet-33.md) | 33 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-34 — recall measures offline whether an answer was used, from the query log and the worktree's next commit](spec/2026-10-04-spec-TOOL-aMendedFleet-34.md) | 34 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-35 — the map's symbol tier reads shell definitions through the lexicon's tokenizer](spec/2026-10-04-spec-TOOL-aMendedFleet-35.md) | 35 | 2 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-36 — `reuse_lookup.py` prints within a byte budget and names what it cut](spec/2026-10-04-spec-TOOL-aMendedFleet-36.md) | 36 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-37 — dossier freshness is derived from git, and drift-audit reports the dossiers older than their paths](spec/2026-10-04-spec-TOOL-aMendedFleet-37.md) | 37 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-38 — `map_diff --converge`, its sink and its prescriptions are deleted](spec/2026-10-04-spec-TOOL-aMendedFleet-38.md) | 38 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-39 — a harness-hooks inventory, and `git-hooks` holds real hook names only](spec/2026-10-04-spec-TOOL-aMendedFleet-39.md) | 39 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-40 — the coverage gate refuses a `baseline.toml` that gained a key against its base](spec/2026-10-04-spec-TOOL-aMendedFleet-40.md) | 40 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-41 — `replay-phrases.py --floor` grades a frozen phrase population against recorded floors](spec/2026-10-04-spec-TOOL-aMendedFleet-41.md) | 41 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-42 — the reuse probe counts canonical-copy install sites beside fan-in](spec/2026-10-04-spec-TOOL-aMendedFleet-42.md) | 42 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-43 — the map renders a card of at most 1 KB per feature from its dossier's toml fence](spec/2026-10-04-spec-TOOL-aMendedFleet-43.md) | 43 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-44 — the map gate refuses a present-tense count of an inventory population in dossier prose](spec/2026-10-04-spec-TOOL-aMendedFleet-44.md) | 44 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-45 — reviewers' by-design list comes from one source, the invariant records](spec/2026-10-04-spec-TOOL-aMendedFleet-45.md) | 45 | 1 | WONTDO | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-46 — the replay harness measures which shortlist quantity predicts a reuse miss, before any miss signal ships](spec/2026-10-04-spec-TOOL-aMendedFleet-46.md) | 46 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-47 — `run_records_nonterminal_but_merged` honours derived LANDED, and the unused-verb pin drops to 0](spec/2026-10-04-spec-TOOL-aMendedFleet-47.md) | 47 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-48 — drift readings append to a node-local history file](spec/2026-10-04-spec-TOOL-aMendedFleet-48.md) | 48 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-49 — the unattended close prints the BASE..HEAD drift delta](spec/2026-10-04-spec-TOOL-aMendedFleet-49.md) | 49 | 1 | SPECCED | rev-3 | 2026-10-04 |
| [TOOL-aMendedFleet-50 — a monthly escape-ratio report, outside the seconds tier](spec/2026-10-04-spec-TOOL-aMendedFleet-50.md) | 50 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-51 — report-only drift signals over a pin nobody drains print pinless, and `readme_mechanism_drift` reads live builds only](spec/2026-10-04-spec-TOOL-aMendedFleet-51.md) | 51 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-52 — the hand-kept signal compares the drift README's signal names against the names the engine reports](spec/2026-10-04-spec-TOOL-aMendedFleet-52.md) | 52 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-53 — the dangling-pointer signal reads the declared auto-memory directory and checks its backticked paths against the tracked tree](spec/2026-10-04-spec-TOOL-aMendedFleet-53.md) | 53 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-54 — drift reports `live_builds_without_activity` from the dormant rows LIVE.md renders](spec/2026-10-04-spec-TOOL-aMendedFleet-54.md) | 54 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-55 — drift reports `open_asks_cited_by_product_source`, report-only](spec/2026-10-04-spec-TOOL-aMendedFleet-55.md) | 55 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-56 — gateable stable-key drift signals are bounded by a shrink-only set of offender ids instead of a count](spec/2026-10-04-spec-TOOL-aMendedFleet-56.md) | 56 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-57 — shrink-only lists are graded against their low-water mark](spec/2026-10-04-spec-TOOL-aMendedFleet-57.md) | 57 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-58 — gate yield per leg is reported from the gates journal](spec/2026-10-04-spec-TOOL-aMendedFleet-58.md) | 58 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-59 — timeout retries are grouped by leg across every git dir of the clone](spec/2026-10-04-spec-TOOL-aMendedFleet-59.md) | 59 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-60 — a cross-run overlap probe over unmerged remote refs runs at preflight](spec/2026-10-04-spec-TOOL-aMendedFleet-60.md) | 60 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-62 — the two history legs grade the run's own range, reusing node d's bytes](spec/2026-10-04-spec-TOOL-aMendedFleet-62.md) | 61 | 2 | SPECCED | rev-4 | 2026-10-04 |
| [TOOL-aMendedFleet-61 — preflight pins the launching CLI version and every resume compares it, and a missing resume tick is announced loudly](spec/2026-10-04-spec-TOOL-aMendedFleet-61.md) | 62 | 2 | SPECCED | rev-4 | 2026-10-04 |
| [TOOL-aMendedFleet-63 — `--close` and `--abort` render the run record themselves, after their own END line](spec/2026-10-04-spec-TOOL-aMendedFleet-63.md) | 63 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-64 — `govkit selfcheck --fix` writes every kit-version carrier from its `version_from` constant](spec/2026-10-04-spec-TOOL-aMendedFleet-64.md) | 64 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-65 — the lander mints kit versions, so a branch owes no bump](spec/2026-10-04-spec-TOOL-aMendedFleet-65.md) | 65 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-66 — the unattended close sequence lists the open asks that target files the run touched](spec/2026-10-04-spec-TOOL-aMendedFleet-66.md) | 66 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-67 — review and drift harnesses can spawn their judges as a read-only agent type that omits the charter](spec/2026-10-04-spec-TOOL-aMendedFleet-67.md) | 67 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-68 — the unattended Skill becomes a router of at most 10 KiB](spec/2026-10-04-spec-TOOL-aMendedFleet-68.md) | 68 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-69 — the agent-instructions kit announces a canonical file past 32 KiB and states both tool facts as verified](spec/2026-10-04-spec-TOOL-aMendedFleet-69.md) | 69 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-70 — runlog's extractor reports what a session spends in tokens and minutes before it reaches READY](spec/2026-10-04-spec-TOOL-aMendedFleet-70.md) | 70 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-71 — one sweep gives every present-tense count in a code comment one of ANNOTATION-STYLE A4's three dispositions](spec/2026-10-04-spec-TOOL-aMendedFleet-71.md) | 71 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-72 — the gate runner reaps the dead `gate-timings.tsv` it no longer reads](spec/2026-10-04-spec-TOOL-aMendedFleet-72.md) | 72 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-73 — the vague-brief trial arm: a full spec against a short plan, on a three-sentence brief](spec/2026-10-04-spec-TOOL-aMendedFleet-73.md) | 73 | 2 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-74 — a unit can be handed the bug-class checklist for its write set before it writes code](spec/2026-10-04-spec-TOOL-aMendedFleet-74.md) | 74 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-75 — a `New arm:` line declares the acceptance criteria its arm keeps observed](spec/2026-10-04-spec-TOOL-aMendedFleet-75.md) | 75 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [KICK-aMendedFleet-1 — the orientation card shows the last drift reading from the node's history](spec/2026-10-04-spec-KICK-aMendedFleet-1.md) | 76 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [KICK-aMendedFleet-2 — the orientation card shows which unmerged remote refs share paths with this tree's branch](spec/2026-10-04-spec-KICK-aMendedFleet-2.md) | 77 | 1 | SPECCED | rev-3 | 2026-10-04 |
| [KICK-aMendedFleet-3 — kickoff Step 4 points at the two context commands the build method spells once](spec/2026-10-04-spec-KICK-aMendedFleet-3.md) | 78 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [PLAY-aMendedFleet-1 — the AGENTS.md wrapper's merge-bar section moves to a guide, without its repeated catalog or dated history](spec/2026-10-04-spec-PLAY-aMendedFleet-1.md) | 79 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [PLAY-aMendedFleet-2 — an experiment's instruments and result rows are committed beside its record, and the vague-brief arm gates §1 as a HIGH ask](spec/2026-10-04-spec-PLAY-aMendedFleet-2.md) | 80 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-81 — the month shards carry only what never changes after their month](spec/2026-10-04-spec-TOOL-aMendedFleet-81.md) | 81 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-82 — each recall query row carries the worktree's HEAD, so `--used` attributes a query after its worktree is gone](spec/2026-10-04-spec-TOOL-aMendedFleet-82.md) | 82 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-83 — the unattended close sequence lists the dossiers its range touched and did not refresh](spec/2026-10-04-spec-TOOL-aMendedFleet-83.md) | 83 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-84 — hygiene check 6 prices a build README by its authored bytes, so generated regions never bill the cap](spec/2026-10-04-spec-TOOL-aMendedFleet-84.md) | 84 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-85 — the charter states what the codebase map's ratchet binds, and stops promising an inventory that cannot rot](spec/2026-10-04-spec-TOOL-aMendedFleet-85.md) | 85 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-86 — the map digest reports code coverage apart from record coverage](spec/2026-10-04-spec-TOOL-aMendedFleet-86.md) | 86 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-87 — a query joins changed paths to the gate legs that guard them](spec/2026-10-04-spec-TOOL-aMendedFleet-87.md) | 87 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-88 — `map_imports.py` is deleted, having no consumer](spec/2026-10-04-spec-TOOL-aMendedFleet-88.md) | 88 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-89 — measured history leaves the dossiers near the byte cap for the records that measured it](spec/2026-10-04-spec-TOOL-aMendedFleet-89.md) | 89 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-90 — a report-only drift signal DEAD for N recorded readings is named for retirement or a filed ask](spec/2026-10-04-spec-TOOL-aMendedFleet-90.md) | 90 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-91 — a spec's status header declares a records-only deliverable, and the product-commit signal reads it](spec/2026-10-04-spec-TOOL-aMendedFleet-91.md) | 91 | 1 | SPECCED | rev-1 | 2026-10-04 |
| [TOOL-aMendedFleet-92 — check 23 prints a fleet line, and drift-audit reads it from the newest bar run](spec/2026-10-04-spec-TOOL-aMendedFleet-92.md) | 92 | 2 | SPECCED | rev-3 | 2026-10-04 |
| [TOOL-aMendedFleet-93 — one tier2 review run with and without the charter, and the review default follows the reading](spec/2026-10-04-spec-TOOL-aMendedFleet-93.md) | 93 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [PLAY-aMendedFleet-3 — the charter's wiring rule stops stating which file Claude Code reads](spec/2026-10-04-spec-PLAY-aMendedFleet-3.md) | 94 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-94 — the wrapper's product-only prose loads from a path-scoped rule when a session opens a product file](spec/2026-10-04-spec-TOOL-aMendedFleet-94.md) | 95 | 2 | SPECCED | rev-2 | 2026-10-04 |
| [KICK-aMendedFleet-4 — the orientation card notes a PATH CLI older than the running session](spec/2026-10-04-spec-KICK-aMendedFleet-4.md) | 96 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [PLAY-aMendedFleet-4 — the `AGENTS.md` wrapper carries one node registry](spec/2026-10-04-spec-PLAY-aMendedFleet-4.md) | 97 | 1 | SPECCED | rev-2 | 2026-10-04 |
| [TOOL-aMendedFleet-97 — held-red C1: the kits' Python stdio is UTF-8 on a host whose code page is cp1252](spec/2026-10-05-spec-TOOL-aMendedFleet-97.md) | 98 | 1 | SPECCED | rev-1 | 2026-10-05 |
| [TOOL-aMendedFleet-98 — held-red C2: a Python suite's `bash` resolves to Git-Bash, never the System32 WSL launcher](spec/2026-10-05-spec-TOOL-aMendedFleet-98.md) | 99 | 1 | SPECCED | rev-1 | 2026-10-05 |
| [TOOL-aMendedFleet-99 — the held job runs its suites from the tree path the bar job uses](spec/2026-10-05-spec-TOOL-aMendedFleet-99.md) | 100 | 1 | SPECCED | rev-1 | 2026-10-05 |
| [TOOL-aMendedFleet-100 — the shard 2/8 fixture's bare origin commits under its own git identity](spec/2026-10-05-spec-TOOL-aMendedFleet-100.md) | 101 | 1 | SPECCED | rev-1 | 2026-10-05 |
| [TOOL-aMendedFleet-101 — the G0 grant fixture writes the `may:` path its own assertions read](spec/2026-10-05-spec-TOOL-aMendedFleet-101.md) | 102 | 1 | SPECCED | rev-1 | 2026-10-05 |
| [TOOL-aMendedFleet-102 — the two drifted inline `resolve_kit_dir` copies match their canonical source](spec/2026-10-05-spec-TOOL-aMendedFleet-102.md) | 103 | 1 | SPECCED | rev-1 | 2026-10-05 |
| [TOOL-aMendedFleet-103 — the hygiene suite's python-parity arm exempts `GRAMMAR_WHERE` beside `GRAMMAR_DIR`](spec/2026-10-05-spec-TOOL-aMendedFleet-103.md) | 104 | 1 | SPECCED | rev-1 | 2026-10-05 |
| [TOOL-aMendedFleet-104 — the foreign-prefix leg declares `review-replay selftest` a whole run](spec/2026-10-05-spec-TOOL-aMendedFleet-104.md) | 105 | 1 | SPECCED | rev-1 | 2026-10-05 |
| [TOOL-aMendedFleet-105 — the reaper's verification settles, so a member dying as it is signalled is not a survivor](spec/2026-10-05-spec-TOOL-aMendedFleet-105.md) | 106 | 1 | SPECCED | rev-1 | 2026-10-05 |
<!-- /gen:build-units -->

Records: 15 bound to this build, across 3 record folder(s).

Ids no record names: KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-11 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18
TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32
TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-4 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45
TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-5 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58
TOOL-aMendedFleet-59 TOOL-aMendedFleet-6 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71
TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-8 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89
TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99.

Ids no `spec-audit` record has ever named: KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12
TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-2 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25
TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-3 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38
TOOL-aMendedFleet-39 TOOL-aMendedFleet-4 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-5 TOOL-aMendedFleet-50
TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-6 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63
TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-7 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-8
TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-9 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93
TOOL-aMendedFleet-94 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aMendedFleet-1` | no |
| 2 | `TOOL-aMendedFleet-2` | no |
| 3 | `TOOL-aMendedFleet-3` | no |
| 4 | `TOOL-aMendedFleet-4` | no |
| 5 | `TOOL-aMendedFleet-5` | no |
| 6 | `TOOL-aMendedFleet-6` | no |
| 7 | `TOOL-aMendedFleet-7` | no |
| 8 | `TOOL-aMendedFleet-8` | no |
| 9 | `TOOL-aMendedFleet-9` | no |
| 10 | `TOOL-aMendedFleet-10` | no |
| 11 | `TOOL-aMendedFleet-11` | no |
| 12 | `TOOL-aMendedFleet-12` | no |
| 13 | `TOOL-aMendedFleet-13` | no |
| 14 | `TOOL-aMendedFleet-14` | no |
| 15 | `TOOL-aMendedFleet-15` | no |
| 16 | `TOOL-aMendedFleet-16` | no |
| 17 | `TOOL-aMendedFleet-17` | no |
| 18 | `TOOL-aMendedFleet-18` | no |
| 19 | `TOOL-aMendedFleet-19` | no |
| 20 | `TOOL-aMendedFleet-20` | no |
| 21 | `TOOL-aMendedFleet-21` | no |
| 22 | `TOOL-aMendedFleet-22` | no |
| 23 | `TOOL-aMendedFleet-23` | no |
| 24 | `TOOL-aMendedFleet-24` | no |
| 25 | `TOOL-aMendedFleet-25` | no |
| 26 | `TOOL-aMendedFleet-26` | no |
| 27 | `TOOL-aMendedFleet-27` | no |
| 28 | `TOOL-aMendedFleet-28` | no |
| 29 | `TOOL-aMendedFleet-29` | no |
| 30 | `TOOL-aMendedFleet-30` | no |
| 31 | `TOOL-aMendedFleet-31` | no |
| 32 | `TOOL-aMendedFleet-32` | no |
| 33 | `TOOL-aMendedFleet-33` | no |
| 34 | `TOOL-aMendedFleet-34` | no |
| 35 | `TOOL-aMendedFleet-35` | no |
| 36 | `TOOL-aMendedFleet-36` | no |
| 37 | `TOOL-aMendedFleet-37` | no |
| 38 | `TOOL-aMendedFleet-38` | no |
| 39 | `TOOL-aMendedFleet-39` | no |
| 40 | `TOOL-aMendedFleet-40` | no |
| 41 | `TOOL-aMendedFleet-41` | no |
| 42 | `TOOL-aMendedFleet-42` | no |
| 43 | `TOOL-aMendedFleet-43` | no |
| 44 | `TOOL-aMendedFleet-44` | no |
| 45 | `TOOL-aMendedFleet-45` | no |
| 46 | `TOOL-aMendedFleet-46` | no |
| 47 | `TOOL-aMendedFleet-47` | no |
| 48 | `TOOL-aMendedFleet-48` | no |
| 49 | `TOOL-aMendedFleet-49` | no |
| 50 | `TOOL-aMendedFleet-50` | no |
| 51 | `TOOL-aMendedFleet-51` | no |
| 52 | `TOOL-aMendedFleet-52` | no |
| 53 | `TOOL-aMendedFleet-53` | no |
| 54 | `TOOL-aMendedFleet-54` | no |
| 55 | `TOOL-aMendedFleet-55` | no |
| 56 | `TOOL-aMendedFleet-56` | no |
| 57 | `TOOL-aMendedFleet-57` | no |
| 58 | `TOOL-aMendedFleet-58` | no |
| 59 | `TOOL-aMendedFleet-59` | no |
| 60 | `TOOL-aMendedFleet-60` | no |
| 61 | `TOOL-aMendedFleet-62` | no |
| 62 | `TOOL-aMendedFleet-61` | no |
| 63 | `TOOL-aMendedFleet-63` | no |
| 64 | `TOOL-aMendedFleet-64` | no |
| 65 | `TOOL-aMendedFleet-65` | no |
| 66 | `TOOL-aMendedFleet-66` | no |
| 67 | `TOOL-aMendedFleet-67` | no |
| 68 | `TOOL-aMendedFleet-68` | no |
| 69 | `TOOL-aMendedFleet-69` | no |
| 70 | `TOOL-aMendedFleet-70` | no |
| 71 | `TOOL-aMendedFleet-71` | no |
| 72 | `TOOL-aMendedFleet-72` | no |
| 73 | `TOOL-aMendedFleet-73` | no |
| 74 | `TOOL-aMendedFleet-74` | no |
| 75 | `TOOL-aMendedFleet-75` | no |
| 76 | `KICK-aMendedFleet-1` | no |
| 77 | `KICK-aMendedFleet-2` | no |
| 78 | `KICK-aMendedFleet-3` | no |
| 79 | `PLAY-aMendedFleet-1` | no |
| 80 | `PLAY-aMendedFleet-2` | no |
| 81 | `TOOL-aMendedFleet-81` | no |
| 82 | `TOOL-aMendedFleet-82` | no |
| 83 | `TOOL-aMendedFleet-83` | no |
| 84 | `TOOL-aMendedFleet-84` | no |
| 85 | `TOOL-aMendedFleet-85` | no |
| 86 | `TOOL-aMendedFleet-86` | no |
| 87 | `TOOL-aMendedFleet-87` | no |
| 88 | `TOOL-aMendedFleet-88` | no |
| 89 | `TOOL-aMendedFleet-89` | no |
| 90 | `TOOL-aMendedFleet-90` | no |
| 91 | `TOOL-aMendedFleet-91` | no |
| 92 | `TOOL-aMendedFleet-92` | no |
| 93 | `TOOL-aMendedFleet-93` | no |
| 94 | `PLAY-aMendedFleet-3` | no |
| 95 | `TOOL-aMendedFleet-94` | no |
| 96 | `KICK-aMendedFleet-4` | no |
| 97 | `PLAY-aMendedFleet-4` | no |
| 98 | `TOOL-aMendedFleet-97` | no |
| 99 | `TOOL-aMendedFleet-98` | no |
| 100 | `TOOL-aMendedFleet-99` | no |
| 101 | `TOOL-aMendedFleet-100` | no |
| 102 | `TOOL-aMendedFleet-101` | no |
| 103 | `TOOL-aMendedFleet-102` | no |
| 104 | `TOOL-aMendedFleet-103` | no |
| 105 | `TOOL-aMendedFleet-104` | no |
| 106 | `TOOL-aMendedFleet-105` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
