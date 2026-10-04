# Spec brief — aMendedFleet, every unit

**Serves:** journal TOOL-aMendedFleet-1

The one spec brief every spec writer of this build reads. It names, per unit, the report point the
unit works out and where its evidence starts. The report is quoted in two records beside this one:
`2026-10-04-prompt-TOOL-aMendedFleet-1-1-source-report.md` (cited `[B#n]`, `Q3`, roadmap items) and
`2026-10-04-prompt-TOOL-aMendedFleet-1-2-source-synthesis.md` (cited `[A#n]`). Read the mandate
record `...-1-0-run-mandate.md` first: it carries the owner's four answers, which bind every spec.

## Rules every spec in this build follows

1. **Re-verify before you specify.** Every number and path in the report was true at `ac65de998`;
   main has moved since. Re-run the cheap probe behind any claim your spec rests on, and say in §10
   where the report and the tree now disagree. A point already fixed on main becomes a spec whose
   goal says so and whose acceptance observes it; it is not invented work.
2. **One mechanism per spec.** If a unit's point turns out to be two mechanisms, say so in §8 as a
   FACT-QUESTION or an open item; the run splits it with `--rescope`.
3. **Acceptance names an OBSERVATION, never a file the unit will create.** `tools/check-spec-tokens.py`
   grades every backticked path-shaped token in §6 against `git ls-files`, and its waiver file is
   shrink-only. Name the observing command or an existing tracked file.
4. **§7 names every gate leg §4's `### Files touched` trips.** Run
   `python tools/check-spec-tokens.py --list` and add the `NEAR [guards]` legs it prints.
5. **§10 is filled**: the seam you extend cited by path, or "no existing seam fits" with the evidence,
   AND the recall terms you used. Probes: `python tools/codebase-map/reuse_lookup.py "<behaviour>"`
   and `python tools/memory-recall/query.py "<question>" --terms "<8-14 words>"`.
6. **Never write an id-shaped token for an id main does not define.** Ids of node d's unlanded build
   (`dUnstuckLanding`) and of the live `aGraftedHelix` build exist only on their branches; a citation
   here creates an orphan. Paraphrase: "node d's dUnstuckLanding unit 25".
7. **Two live builds share this ground, and the owner ruled on both.**
   - **Node d's `dUnstuckLanding`** on `origin/branch/unattended-build-closing-f90fd9` is rewriting
     `tools/unattended/`. The owner ruled: build every report item here anyway. Where node d already
     BUILT the same mechanism, the spec REUSES its bytes (name the commit, read it with `git show`)
     so the later reconcile is identical hunks, not a conflict.
   - **`aGraftedHelix`** on `origin/branch/helixir-review-gov-adoption-ce32e1` owns a remote run
     claim (its unit 1), a card listing of claims (2), an invariants registry as reviewers' by-design
     source (3) and supersession status in recall rows (4). A unit here whose point is one of those
     is specced at Tier 1 with §1 naming the delivering unit by paraphrase, §6 observing nothing
     new, and §8 recording `RESOLVED · retire to that unit`; the run retires it.
8. **Every new refusal or gate clause is observed RED on a staged break** — say how in §6.
9. **Order**: the status header carries `order <n>`, `n` being the unit's roster row number.
10. **Never spell the literal `YYYY-MM-DD` or `<FAMILY-slug-seq>` anywhere in a spec**: hygiene check 12
    reads either as an unfilled skeleton placeholder. Write "the date" or a real date.
11. **No shell process substitution or parentheses glued to a path inside backticks** (`` `diff <(grep x a.md)` ``):
    `check-spec-tokens.py` reads `a.md)` as a path and reds. Describe the comparison in prose.
12. **A §2 item whose prose says a thing is removed, dropped, deleted or retired owes a `**Readers:**`
    clause** (hygiene check 25): `by name:` the readers that spell it, then `by value:` its readers or
    `NO VALUE READERS` and a reason. Add one whenever in doubt.
13. **No spec comes back FORKED on a split question.** Writers run concurrently and cannot mint
    roster numbers, so never author a second spec. If a unit is two mechanisms, mark the §8 item
    `RESOLVED (agent, 2026-10-04, delegated): split — <items> move to a new unit the run adds`; the
    run performs the split and rev-bumps this spec.

## Per-unit points

**Data loss and merge integrity**
- **1** — Merge `01c22e155` dropped the code of two CLOSED `dMendedRecall` units (`write_ask_views`
  in `tools/unattended/unattended.sh` and a `--status` verb entry). Restore from parent `ef1dcdb61`,
  byte-identical to node d's restore commit `e6e55d5ab`. Acceptance observes the function and its
  callers on the branch and the dMendedRecall acceptance re-observed. `[B#11]`.
- **2** — Replay every merge since 2026-09-01 at DEFINITION level (a name a parent added that the
  merge lacks). Report flagged three: `01c22e155` (confirmed), one documented rewrite, and
  `e2e840d08`'s loss of `parse_push_class` (unverified). Adjudicate each, restore any confirmed loss,
  record the census as a journal. `[B#11]`.
- **3** — `tools/push-main.sh --prepare` and `.githooks/pre-push` refuse a merge that drops a
  definition a parent added, unless the merge commit carries `superseded: <name> -> <successor>`.
  Definition-level, never line-level. Node d filed the same as a HIGH ask (its unit 26); read its
  text on their branch. `[B#11]`, Q3 rank 1.

**Red legs** — logs: `gh run list --repo d41ly/coding-governance --limit 15`, then
`gh run view <id> --log-failed`. Push runs red three legs; scheduled run `37196051126` reds 18 held suites.
- **4** — `govkit acceptance matrix`: `tools/govkit/matrix.py` decodes subprocess output with the
  locale codec (cp1252); decode UTF-8 explicitly. `[A#1]`.
- **5** — `transition-audit arms` fails AC11 on Linux CI (`delta() before the merge and --report
  after it disagree`). Find the root cause (the report suspected a fixture leaking `__pycache__`).
- **6** — `lexicon wiring` fails on a clean checkout because `tools/lexicon/*.template.md` lands CRLF;
  pin `eol=lf` in `.gitattributes` and renormalise. `[A#1]`.
- **7** — A CENSUS unit: classify each of the 18 held suites red on the daily job by ROOT CAUSE
  (several likely share one). Its build writes the census journal and adds one unit per cause with
  `--rescope --act add`. Red suites: codebase-map kit, govkit, foreign-prefix parity, manifest-check,
  process-monitor adopter, lexicon, memory-hygiene, python resolver, settings-merge, runlog,
  spec-tokens, row-grammar, unattended gate shards 2/8 and 8/8, unattended driver.
- **8** — drift-audit signal `remote_ci_red_streak`: consecutive failed runs of the remote CI
  workflow, report-only, with a liveness assertion (offline or no `gh` is DEAD PROBE, never 0). `[A#1]`.
- **9** — the daily held job's red legs reach the inherited-red machinery that already auto-files
  HIGH asks (`TOOL-aSightedSkeptic-11`). Decide the route in the spec. `[A#2]`.

**memory-tree** — wave-1 plan §2.1, final report Q2(a).
- **10** — `gen_build_index.py --asks` rows gain the `pointer` `backlog.py` already parses, a summary
  cut to 160 B and a `--path` filter; rank by severity then recency; cap. `[B#1]`.
- **11** — `memory/guides/REVIEW-PROTOCOL.md` (about lines 188-190) and `tools/workflows/tier2-review.js`
  (about line 480) stop pointing reviewers at the 164-312 KB `--asks --json` output and use unit 10's
  filtered call. `[B#1]`.
- **12** — LIVE.md gains a last-touch column from ONE `git log` pass (exclude sweep commits touching
  more than K build folders) and an ACTIVE/DORMANT split by a declared `LIVE_DORMANT_DAYS`. `[A#3] [A#13]`.
- **13** — LIVE.md renders LANDED-UNCLOSED by reusing drift-audit's spec-to-commit join. `[A#13]`.
- **14** — Bulk triage: generated DEFER disposition rows for aged unlabelled asks; dispose the
  fixed-but-OPEN asks the report names (`TOOL-aUnblockedFleet-7`, `-8`, `TOOL-aReplayedCard-9`) and
  close `TOOL-aWeighedCompass-16` as a duplicate of `TOOL-aProbedToolkit-10`. Re-verify each first. `[A#8] [A#59] [B#16] [B#21]`.
- **15** — re-arm a shrink-only pin on `backlog_asks_unlabelled` (blanked at the 09-28 switch-over). `[A#8]`.
- **16** — `gotchas.py --for-diff` ranks classes by anchor specificity (full path, directory,
  basename) and cuts in tiers rather than a hard top-12. Keep universals for markdown diffs. `[A#21]`.
- **17** — `tier2-review.js` drops each finding's `C<n>` class label at about lines 1064-1070; keep it
  in a `classes` column of the committed appendix so hit counts accrue. `[B#4]`.
- **18** — `tier2-review.js` prints one byte-stable shape line with severity counts and output-token
  spend. `[B#23]`.
- **19** — `--doctor <slug>` prints every failing build-folder rule in one pass. `[A#23]`.
- **20** — `--new-spec` writes a skeleton that satisfies every active cutoff. `[A#23]`.
- **21** — a new `*_CUTOFF` key must retire an old one (cutoff budget). `[A#16]`.
- **22** — `merge=ours` on LIVE.md, `ledger/*`, `gotchas/INDEX.md`; month shards drop the Status
  column. Check 9 already reds a stale render. `[A#14]`.
- **23** — check 19 reports gotcha anchors selecting zero paths (39 of 314 at review). `[A#25]`.
- **24** — dead paths in non-terminal build READMEs reported advisory; fix the dead `decisions/`
  pointer at `memory/DECISIONS.md` line 5. `[A#20]`.
- **25** — a spec byte ceiling priced against a recorded high-water, reusing the template's
  mechanism. `[A#4] [A#6]`.
- **26** — a `missing:<ID>` citation form for ids with no record, counted separately. `[A#18]`.

**memory-recall** — wave-1 plan §2.2.
- **27** — exclude archived versioned snapshots of live docs from the corpus (one glob or a
  `RECALL_EXCLUDE` key); add a gold arm answered by a live charter line. `[A#27]`.
- **28** — the floor grades the path the CLI serves (terms plus fusion), as the BLOCKED
  `aTunedCompass` unit 9 describes; read that spec. `[A#26]`.
- **29** — harvest a gold set from committed spec §10 probes, labelled by later-cited foreign ids,
  de-contaminated (drop ids the probe itself returned); report hit@10. `[B#5] [A#30]`.
- **30** — supersession labels: aGraftedHelix's unit 4 (rule 7). `[A#28]`.
- **31** — adaptive output trim; no hard top-5 (weak-term answers sat at ranks 9, 19, 35). `[A#29]`.
- **32** — cache eviction: deleted worktrees first, ordered by last query. `[A#33]`.
- **33** — delete stale typed figures from the recall README and Skill; miss advice becomes
  "re-query in the record's vocabulary, then grep". `[A#36]`.
- **34** — measure answer-used offline: join each logged query's result ids to the ids the
  worktree's next commit, spec or card cites. `[A#32]`.

**codebase-map** — wave-1 plan §2.3.
- **35** — wire `lexicon.parse_shell_defs` into `SYMBOL_EXTRACTORS`, drop `.sh` from the dark
  layers, fix the stale "shell is dark" texts (`TOOL-aWeighedCompass-8`). `[A#38]`.
- **36** — `reuse_lookup.py` byte budget with a "cut N, rerun with `--budget 0`" line; choose the
  default by `replay-phrases.py` hit@budget (`TOOL-aProbedToolkit-9`). `[A#40]`.
- **37** — dossier freshness DERIVED: dossier last commit vs newest commit on its globs; report-only
  drift signal with shrink-only pin, plus a close-time "touched, not refreshed" list. `[A#41] [B#7]`.
- **38** — delete `map_diff --converge`, its sink and the "closing loop" prescriptions (README,
  `WIRE-INTO-PROJECT.md`, `reuse-lookup.agent.md`). `[B#7]`.
- **39** — a harness-hooks inventory from `.claude/settings.json`, fail-closed; `git-hooks` holds real
  hook names only (`TOOL-aProbedToolkit-15`, `-8`). `[A#43] [A#44]`.
- **40** — assert `baseline.toml` never gains a key against the base ref. `[A#49]`.
- **41** — `replay-phrases.py --floor`, self-enforced, kept off the bar (owner ruling 2026-08-23). `[A#50]`.
- **42** — `fan_in` counts `>>> canonical-copy` markers as install sites; join legs to paths; give
  `map_imports.py` a consumer or delete it. `[A#46]`.
- **43** — a generated feature card of at most 1 KB from the toml fence; move measured history out of
  dossiers near the 20,480-byte cap. `[A#47]`.
- **44** — lint dossier prose for typed population counts. `[A#41]`.
- **45** — by-design source: aGraftedHelix's unit 3 (rule 7). `[B#2]`.
- **46** — a reuse miss signal; FIRST measure a predictor (seed coverage is not one). `[A#39]`.

**drift-audit** — wave-1 plan §2.4.
- **47** — `run_records_nonterminal_but_merged` applies the derived-LANDED rule (`read_landing_commit`
  ancestry, NOT `branch-sha`); lower `lexicon_verbs_declared_but_unused` pin 3 to 0. `[A#51] [A#52]`.
- **48** — the drift records leg appends one row per signal to `<git-common-dir>/drift-history.tsv`
  (sha, base ref and sha, value, of, key hash). `[A#55]`.
- **49** — the unattended close prints the BASE..HEAD drift delta. `[A#60]`.
- **50** — monthly escape-ratio report outside the seconds tier: n, 95% interval, DIRECT share; never
  claim an effect from one repo's before/after. `[B#18] [B#26]`.
- **51** — retire or demote over-pin report-only signals nobody acts on; DEAD for N readings → retired
  or filed; restrict `readme_mechanism_drift` to LIVE builds. `[A#54] [A#61] [A#62]`.
- **52** — `handkept_inventories_disagreeing_with_source` becomes a name-set comparison of the README
  table against `SIGNALS`; drop the Skill's second table. `[A#58]`.
- **53** — `dangling_pointers_in_own_ledger` reads an adopter-declared auto-memory path, checking
  backticked paths against `git ls-files`. `[A#56]`.
- **54** — signal `live_builds_without_activity`. `[A#59]`.
- **55** — signal `open_asks_cited_by_product_source`, report-only. `[A#59]`.
- **56** — stable-key signals move to identity baselines (`TOOL-dScaffoldedMirror-9` precedent). `[A#52]`.
- **57** — shrink-only lists graded against their low-water mark; records-only deliverable in the spec
  header (`TOOL-aProbedToolkit-18`). `[A#57]`.
- **58** — gate yield per leg as a mode over `runlog.py journal --producer gates`. `[B#24]`.
- **59** — timeout retries grouped by leg across every git dir, sharing 58's parser. `[A#53]`.

**Orchestration (`tools/unattended/`; rule 7 binds)**
- **60** — a cross-run overlap probe over unmerged remote refs joining specs' "Files touched" with
  diffs; ignore version-marker-only edits; age out abandoned refs; announce, never refuse; runs at
  `--preflight`. Complements, does not duplicate, aGraftedHelix's slug-keyed claim. `[B#10] [A#9]`.
- **61** — record the launching CLI version at preflight and compare on resume; a missing resume tick
  is announced loudly rather than at INFO. `[B#40] [B#13]`.
- **62** — the history legs grade the run's own range (RANGE mode). Node d built it: commits
  `d99cd0328` and `f8afa61bc`; reuse their bytes. `[B#14]`.
- **63** — `--close` and `--abort` render the runlog record themselves (6 of 9 runs skipped it). `[B#15]`.
- **64** — `govkit` `--fix` writes every kit-version carrier from `kit.toml` `version_from`
  (`TOOL-aBoundedVerdict-29`, `DEPL-aHoistedPass-10`). `[A#5]`.
- **65** — mint kit versions at the lander (`push-main --prepare`) and delete the per-branch bump
  obligation. `[B#12]`.
- **66** — the close lists open asks whose `→ path` targets files the build touched, for disposition,
  report-only. `[B#1]`.

**Context diet and quality** (owner: full diet)
- **67** — a read-only worker agent type with `omitClaudeMd` for tier2 and drift finders and skeptics;
  restart caveat; A/B one tier2 run on precision and first-turn tokens. `[B#29]`.
- **68** — the unattended Skill (about 88 KB) becomes a router of at most 10 KB; port Skill-only
  ordering into the protocol first. `[B#30]`.
- **69** — agent-instructions kit: announce past 32,768 B beside the byte count it prints; fix the
  "nothing extra" README row; stamp both environment claims. `[B#38] [B#35]`.
- **70** — a tokens-to-READY report mode over runlog's extractor. `[B#34]`.
- **71** — sweep present-tense counts in code comments (ANNOTATION-STYLE A4), e.g.
  `tools/unattended/unattended.sh` near lines 4017 and 4023 at review. `[B#32]`.
- **72** — remove the dead `gate-timings.tsv` path (superseded by the ledger). `[B#14]`.
- **73** — run the vague-brief P-versus-S trial arm and record it, instruments committed. `[B#19] [B#43]`.
- **74** — path-scoped rules and a budgeted pre-build checklist, built only after 67, 68 and 79 are
  measured. `[B#39] [B#37] [B#6]`.
- **75** — acceptance-criterion ids join the `New arm:` grammar. `[B#27] [B#45]`.
- **76** (KICK) — the orientation card shows the last drift-history row (0 s; never runs drift). `[A#60]`.
- **77** (KICK) — the orientation card shows unit 60's overlaps and a NOTE when the PATH CLI is older
  than the running session. `[B#10] [B#40]`.
- **78** (KICK) — kickoff Step 4 points at the two context commands the build method spells once
  (`gotchas.py --for-paths|--for-diff`, `gen_build_index.py --asks --path`). The engine is at its
  byte cap, so the step must shrink. `[B#3]`.
- **79** (PLAY) — the `AGENTS.md` wrapper loses its second node registry, the repeated command
  catalog and the dated measurement history in the merge-bar section, which moves to a guide. `[B#28] [B#39]`.
- **80** (PLAY) — an experiment's instrument and result rows are committed to its build folder, never
  left under `%TEMP%`; the vague-brief arm is filed as a HIGH ask that gates the charter's §1. `[B#19] [B#22]`.

**Added by the run** (splits recorded at speccing)
- **81** — split from 22: the month shards render Build, Node and Opened only. Specced by the run.
- **82** — split from 34 at its F2: each recall query-log row carries the worktree's HEAD sha, so the
  commit after a query is found by ancestry after the worktree is gone. A change to the served query
  path in `tools/memory-recall/query.py`; unit 34 reports the unattributed count and reads this field
  once it exists. Read unit 34's spec first.
- **83** — split from 37 at its F1: the unattended close prints the dossiers its BASE..HEAD range
  touched and did not refresh, by calling unit 37's `map_diff.py --stale-dossiers` range mode.
  Report-only. A close block in `tools/unattended/unattended.sh`; units 49 and 66 are sibling close
  blocks. Read unit 37's spec first.
- **84** — DISCOVERED at speccing, adopted under protocol section 11: this build's 83-unit roster pushes its README's generated build-index and build-order regions past check 6's 25600 B cap (measured 14626 B of index at 55 specs). A renderer-shaped overflow. Fix the RENDERER (or how check 6 prices generated regions) so a build of any size fits, and drain the `memory/project/curation-debt.txt` row this build added for its own README. Measure before choosing; nothing measured may get worse.
- **85** — split from 39 at its F1: the charter/template sentence overselling the map (half of `TOOL-aProbedToolkit-15`). A governance-carrier edit; the owner granted the full diet.
- **86** — split from 39 at its F1: `map_diff.py`'s digest coverage figure mixes code and records (`TOOL-aProbedToolkit-8`). Unit 40 owns the baseline shrink assert.
- **87** — split from 42 at its F1: the legs-to-paths join, a new query over `tools/gate-legs.json` guards.
- **88** — split from 42 at its F1: no tracked file imports it except the kit selftest, whose parity arm now skips. Deletion is the recommendation; re-verify consumers first.
- **89** — split from 43 at its F1: edit the prose of the seven dossiers near the 20480 B cap and decide where measured history lives. Unit 43 renders cards from the fences and never reads prose.
- **90** — split from 51 at its F1: the DEAD-for-N rule, after unit 48's history file exists.
- **91** — split from 57 at its F1: the records-only spec-header declaration of `TOOL-aProbedToolkit-18`; unit 57 keeps the low-water mark.
- **92** — split from 62 at its F1: check 23's range mode, the per-build budget key and the ceiling key it replaces, the measuring flag, the fleet line and the drift signal reading it. Node d built the same on its branch (commit `d99cd0328`, check 23 half); reuse its bytes.
- **93** — split from 67 at its F1: the A/B run (precision and first-turn tokens) and the default it may set, ordered after units 67 and 70.
- **94** (`PLAY-aMendedFleet-3`) — split from 69 at its F1: the charter template's §6 "Claude Code cannot read" clause and its render in `AGENTS.md`. Read unit 69's F3 probe result first.
- **95** (`TOOL-aMendedFleet-94`) — split from 74 at its F1: path-scoped rules, ordered after units 67, 68, 79 and 93; unit 74 keeps the pre-build checklist.
- **96** (`KICK-aMendedFleet-4`) — split from 77 (KICK-2) at its F1: the card compares PATH `claude --version` with the running session's version as unit 61 reads it.
- **97** (`PLAY-aMendedFleet-4`) — split from 79 (PLAY-1) at its F1: deduplicate the second node registry in the `AGENTS.md` wrapper; unit 79 keeps the table byte-identical.
