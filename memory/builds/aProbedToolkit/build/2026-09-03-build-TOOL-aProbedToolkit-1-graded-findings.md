# Graded findings — the adversarial pass

**Serves:** journal TOOL-aProbedToolkit-1

Node `a`, 2026-09-03. One lens per kit over the four scratch clones, then five skeptics told to
REFUTE each finding and to re-run its reproducing command before accepting it. 45 findings, 44
CONFIRMED, 1 REFUTED.

The precision of 0.98 is high enough to state as a caveat rather than a result. The review protocol
in this tree treats precision as the token lever and warns below ~0.5; it says nothing about a rate
this close to 1.0, which usually means agreeable skeptics. Mitigating it here: every finding carried
a command, and the skeptics returned eleven `corrected` statements that narrowed or renumbered a
claim without refuting it — including two that corrected line numbers, one that cut a severity from
blocker to major, and one that pointed out a grep in the finding was case-sensitive and had hidden
its own counter-evidence. That is not the signature of a pass that rubber-stamped.

Raw graded list, verbatim from the run. Kept because the numbers in the report are drawn from it and
a reader should be able to see the ones that did not make the report.

```
[1] CONFIRMED · BLOCKER · armed-but-unreachable-rule
    P1 grades a population it was never designed for: 27% of gov's 461 offenders are test arms or nested closures, and 45% vanish if private helpers are excluded — no rename involved
    WHERE tools/lexicon/lexicon.py:219
    EVID  `_python_defs` uses `ast.walk`, so every FunctionDef is graded: module-level, methods, nested closures, dunders. Re-deriving the 461 with enclosing-scope context: 199 module-level public prod, 83 module-level private prod, 45 js, 12+14 nested prod, 9+1 methods, 1 dunder, and 97 in test/selftest/bench files (56 of those nested inside a test arm). 124 offenders (27%) are test-file arms or nested clo
    CORR  One scope correction that does not change the defect: `tools/memory-tree/kit.toml:108-112` declares this leg to adopters as `argv = ["bash", "{kit}/check-verdict-epoch.sh"]`, subject=repo, guard=[], so the DESCRIPTOR is prefix-parametrized while the script it names is not — which sharpens the findin

[2] CONFIRMED · BLOCKER · armed-but-unreachable-rule
    --suggest, the kit's whole author-facing remedy, answers 7 of this repo's 461 offenders (1.5%) — for the other 454 it prints the refusal plus a dump of the 23 verbs
    WHERE tools/lexicon/lexicon.py:850
    EVID  `run_suggest` resolves a replacement only through `build_banned_index`, which inverts the NOT clauses in `.lexicon.conf` — 23 tokens. The offenders carry 281 DISTINCT leading tokens; the intersection is 5 tokens (append, compute, log, search, validate) covering 7 of 461 sites. `python tools/lexicon/lexicon.py --suggest pytest_configure` / `__repr__` / `is_ancestor` / `repo_root` / `demand_safe_tok
    CORR  Two nuances worth carrying, neither of which rescues the runtime silence. (a) TOMBSTONE_ROOTS blank is legitimately an empty population — a repo with no old tree root to keep empty — so counting it as a disarmed rule inflates the total from six real ones to seven. (b) The adopter is told about three

[3] CONFIRMED · MAJOR · vacuous-selector-empty-population
    The offender pin is a one-way ledger with no tightening: 705 counts of slack pass GREEN and the run prints the true offender count in the same breath without noticing
    WHERE tools/lexicon/lexicon.py:697
    EVID  `if len(unwaived) > pin` — strictly greater, so a pin that has fallen out of date can never red. Demonstrated on a fresh adopter: VERB_OFFENDER_PIN="900" against 195 actual offenders exits 0 and prints 'lexicon OK' on the line after 'P1 verb graded=306 offenders=195'. Nothing in the kit compares the two. The one instrument in this repo whose job is exactly this — drift-audit's `signal_shrink_only`
    CORR  The count is 72, not 73. Everything else measures as written.

[4] CONFIRMED · MAJOR · fixture-passes-by-finding-nothing
    The whole gate can be legally green at 5.2% coverage: `dark` is free, there is no coverage floor, and the P3 hole is discharged by any two directories that exist
    WHERE tools/lexicon/lexicon.py:729
    EVID  Coverage is printed and decides nothing — no threshold, no pin, no red. Declaring an armed language `dark` is a legal LANGS value and skips DEAD PROBE entirely (the check at lexicon.py:~613 `continue`s on mode=='dark'). Demonstrated end to end on a fresh adopter: set py::dark, invent LAYERS rule `tools/lexicon/* -> tests/*` (two real directories that never import each other), stamp `ratified`, pin
    CORR  Two small corrections inside the fix text. TWO of the five ceilings sit within 5 bytes of the corpus max (Build-level rules 1800 vs 1799; the problem slot 900 vs 896), not three — the other three have 32 B, 56 B and 114 B of headroom. And `--bump` is not at gen_build_index.py:1721; the verb is dispa

[5] CONFIRMED · MAJOR · armed-but-unreachable-rule
    The predicate grades names the author is forbidden to change — pytest plugin hooks and Python protocol dunders — with no seeded waivers
    WHERE tools/lexicon/subtokens.py:29
    EVID  `leading_verb` strips leading underscores by design, so `__repr__` grades on `repr`, `__call__` on `call`, `__enter__` on `enter`. `__init__` passes only by the accident that `init` is a table row. gov currently carries one (`tools/lexicon/lexicon.py:192 __str__`) plus four pytest hooks in tools/pytest-parallel-guardrails/crashprobe.py:147,160,166,172 — `pytest_configure` and friends are the plugi
    CORR  The headline claim "exists in neither HYGIENE.template.md nor memory/HYGIENE.md" is false, and the finding's own grep is what hid it: the pattern `acceptance.ledger|ACCEPTANCE_LEDGER` is case-sensitive and the section is titled with a capital A. Both files carry `## Acceptance ledger — how a built u

[6] REFUTED · MAJOR · none
    On the flagship adopter the gate is dark over the entire frontend — 980 of 2216 definition-carrying files are .ts/.tsx, and the shipped js-regex already extracts 3711 defs from them
    WHERE tools/lexicon/lexicon.py:102
    EVID  `KNOWN_EXTS = {"py": ("python-ast", "parser"), "js": ("js-regex", "probe")}`. Scaffolding a seed for incms/main emits `ts::dark tsx::dark` among 42 dark declarations of 44 extensions, and measured coverage there is 1153 of 2216 definition-carrying files (52.0%) with the dark remainder being tsx 529, ts 451, sh 64. Running the EXISTING js-regex pattern set over incms's tracked .ts/.tsx finds 915 fi
    CORR  What is actually true and worth keeping: nc runs a 116-line local fork of the 2.49 engine while `KIT_MEMORY_TREE_VERSION=2.49` claims a pristine kit, so nc has no upgrade path — running the current kit there is exit 1 with 612 Serves findings AND a `check 3 FAILED` over nc's four extra `memory/proje

[7] CONFIRMED · MINOR · none
    The only adopted table in existence was never derived from the canon the kit ships; it is the frequency-ranked mirror the kit's own header calls 'the banned shape'
    WHERE .lexicon.conf:9
    EVID  gov's VERBS block was curated 2026-08-16 (b0626152) from the OLD --scaffold, which ranked the corpus's own leading tokens. The conf's own header says so: '--scaffold proposed 25 rows by leading-token frequency and ten of them were not verbs at all'. canon.py landed 2026-08-25 (dec46b82), nine days later, and its docstring offers gov's table as independent corroboration — 'The canon reproduces a cu
    CORR  Two corrections, one of which materially narrows the impact. (a) "a stray file there is a document a session may load and nothing watches" is false for two of the five strays, in gov and in any adopter carrying the codebase-map kit: `memory/guides/sub/deep.md` makes `gen_map.py --check` raise `map_l

[8] CONFIRMED · MINOR · none
    Both non-gov deployments are incomplete in ways that make the kit unadoptable and unrunnable, and nobody noticed because no gate leg names it
    WHERE tools/lexicon/kit.toml:4
    EVID  incms/main carries 13 of 14 kit files under scripts/lexicon/ and is MISSING kit.toml — govkit cannot see the kit at all, so no [adopt], no [check], no [gate_leg]. nicocares-package carries kit.toml but is MISSING SKILL.template.md, which routes check_skill() into the 'skip lexicon skill — SKILL.template.md not installed, nothing to render' branch and returns 0: an adopter there gets a green wiring
    CORR  Two precisions. The scaffolded taxonomy is the EXAMPLE's (ARCH/DEPL/DES), not the "built-in" one at :40-41 (which would have produced ARCH/DEPLOY/BLOCK/DES/PERF), so the :46 comment's literal wording — "never silently scaffold the built-in DEMO disciplines" — survives; what fails is its intent, sinc

[9] CONFIRMED · OBSERVATION · none
    The kit fails its own table: 10 of the 45 definitions in tools/lexicon/*.py are P1 offenders, including both public functions of subtokens.py
    WHERE tools/lexicon/subtokens.py:23
    EVID  22% offender rate inside the kit that ships the gate. `subtokens()` and `leading_verb()` — the two functions the whole predicate rests on — are both refused by the predicate. Also tools/lexicon/lexicon.py:196 `tracked_files`, :203 `ext_of`, :192 `__str__`, tools/lexicon/lexicon_conf.py:139 `langs`. Repo-wide the rate is 45% (416 of 925 py defs), so the kit is better than average and still cannot p
    CORR  The diagnosis in the title is wrong, and it matters for the fix. This is NOT "a checks-17-19 failure": findings from 17, 18 and 19 do carry their numbers — gotchas.py:265 emits `check 17: ...`, :276 `check 18: ...`, and :280/:283/:289 `check 19: ...`, all passed through the `print("HYGIENE " + line)

[10] CONFIRMED · BLOCKER · vacuous-selector-empty-population
    The gate verifies the map's name catalogues, never the source tree — nc passes all five legs with 0 of 182 source files attributable
    WHERE tools/codebase-map/test_codebase_map.py:78-93 (coverage assert is over inventory keys only); tools/codebase-map/map_lib.py:1340-1369 (compute_coverage's four asserts); tools/codebase-map/map_lib.py:1503-1534 (attribute_paths — globs asserted by nothing)
    EVID  The ratchet's both-direction guarantee applies ONLY to inventory keys. File-level attribution runs through dossier `paths.globs`, which the gate never touches (the map README states it: "Path globs are digest-only, never gated"). Measured, tracked source files (.py .js .ts .tsx .jsx .sh .mjs .cjs .vue, excluding memory/ records and node_modules/vendor) attributed by attribute_paths: nc 0/182 (0%),
    CORR  Two location corrections, neither of which changes the verdict. (1) The awk equality is at tools/memory-tree/check-memory-hygiene.sh:384, not :380. (2) The check that REFUSES a `review/` folder is check 4 (the build-folder shape check), not check 5 — though check 5 independently hardcodes the same p

[11] CONFIRMED · BLOCKER · vacuous-selector-empty-population
    In the repo that SHIPS the kit, 46 of 144 source files are unmapped — including six entrypoints AGENTS.md tells every session to run
    WHERE memory/map/features/*.md (gov: 73 globs across 19 dossiers); tools/codebase-map/map_lib.py:1503
    EVID  gov source-file attribution: 98/144 mapped, 46 UNMAPPED (32%). The unmapped set contains tools/push-main.sh (the lander named in AGENTS.md's command catalog), tools/drift-audit/drift_report.py (AGENTS.md: "Before theorizing about drift, run …"), tools/memory-tree/gotchas.py (AGENTS.md: "its stdout IS the bug-class checklist for that diff"), tools/check-wiring.sh (the SessionStart hook), tools/memo
    CORR  The measurements hold; three framing claims do not, and they are the whole justification the finding offers for stating it. (1) `exempt-pin: 67` is line 29 of memory/project/readme-contract.txt, not its first line — lines 1-27 are the header comment. (2) The pin is not 'shrink-only'. The header says

[12] CONFIRMED · MAJOR · armed-but-unreachable-rule
    baseline.toml is "shrink-only" in three docstrings and gated by nothing — 11 new keys entered gov's baseline after the backfill, 3 entered incms's
    WHERE tools/codebase-map/map_lib.py:1340-1369 (compute_coverage: four asserts, none of them "baseline did not grow"); tools/codebase-map/test_codebase_map.py:16 and :78-93; tools/codebase-map/gen_map.py:181 (_README rule text)
    EVID  The gate's own docstring says "`baseline.toml` additions are reserved for the initial backfill — do not add new keys"; the scaffolded README repeats it; AGENTS.md repeats it. compute_coverage asserts (1) inventory-claims-baseline=0, (2) claims-inventory=0, (3) baseline-inventory=0, (4) baseline&claims=0. There is no fifth assert comparing the baseline against its predecessor, so a NEW key parked i
    CORR  One rhetorical link is stretched and should be stated straight. The README's `9/12 = 0.75` at :168 is a value for the graded cell `records:fts5:r@5` — it is what a staged regression does to the number the floor reads. The CLI's 0.7500 is a different metric (top-5 of a 20-deep RRF fusion over two ind

[13] CONFIRMED · MAJOR · fixture-passes-by-finding-nothing
    symbols.json freshness is gated only when the symbol tier is non-empty — deleting the whole tier leaves a green gate and an orphaned corpus that reuse_lookup keeps serving
    WHERE tools/codebase-map/test_codebase_map.py:140-144; tools/codebase-map/gen_map.py:141-144; tools/codebase-map/reuse_lookup.py:153-154
    EVID  Both the renderer and the gate read `symbols = getattr(ext, "all_symbols", list)()` and then guard the artifact behind `if symbols:`. So an emptied or fully-failing SYMBOL tier removes symbols.json from the compared set instead of failing, and nothing deletes the committed file. STAGED BREAK on a copy of gov: replacing map_extractors.SYMBOL_EXTRACTORS with `{}` -> `test_codebase_map.py` prints 5x

[14] CONFIRMED · MAJOR · two-answers-to-one-question
    RECALL_DARK_LAYERS is a hand-typed second answer to what SYMBOL_EXTRACTORS covers — incms declares nothing dark while 54% of its source has no symbols and shell is 100% dark
    WHERE tools/codebase-map/reuse_lookup.py:172 (parses the conf string) and :320-329 (the partial-recall notice fires only on that string); .codebase-map.conf RECALL_DARK_LAYERS (incms:18 = "", gov:27 = "bash", nc: key absent entirely)
    EVID  Nothing anywhere compares the declared dark set against the extensions actually present in symbols.json or in the tree — a repo-wide grep for RECALL_DARK across the kit finds one hit outside reuse_lookup, and it is a selftest FIXTURE string (selftest.py:920). Measured coverage of incms's committed symbols.json against its tracked source: .sh 0 of 77 files, .js 0 of 23, .cjs 0 of 1, .py 394 of 1164

[15] CONFIRMED · MAJOR · vacuous-selector-empty-population
    reuse_lookup precision tracks symbol-tier coverage and the tool never says which regime it is in — nc returns .webp filenames as reusable seams
    WHERE tools/codebase-map/reuse_lookup.py:153-179 (corpus assembly folds inventory keys and prose fragments into the same ranked list as symbols) and :327-329 (the "tier not adopted" note prints AFTER the candidate list)
    EVID  Six realistic behavioural queries per repo ("send an email notification", "parse a yaml config file", "validate a user submitted form", "cache an expensive computation", "retry a failing network call", "normalise a path for windows"), counting how many of the top 10 candidates are real code symbols (a `[kind | <source file> | fan-in N]` row): incms 60/60 (100%), of which 57 clear the seam threshol

[16] CONFIRMED · MAJOR · pin-copied-from-another-corpus
    nc's decision to skip the symbol tier rests on a symbol count that is 27x low
    WHERE scripts/codebase-map/map_extractors.py:6-9 (nc)
    EVID  The docstring justifies the opt-out: "the kit's symbol/reuse tier is deliberately NOT used here: run against this repo it found 26 symbols and returned stem-matches like `favicon_file`, which is noise dressed as a shortlist." Re-measured with the kit's OWN parser (map_lib.python_symbols) over nc's tree: scripts/ 596, tests/ 109, brand/ 5, backend/ 9 = 719 python symbols, of which 254 across 28 fil
    CORR  One hair worth splitting so the fix note is accurate. The README's literal words are that the harnesses 'need a graded `fixture.json` that this kit deliberately does not ship' — and strictly, no file named `fixture.json` ships; the kit ships `recall-fixture.json`. That is the only reading under whic

[17] CONFIRMED · MINOR · pin-copied-from-another-corpus
    SEAM_FANIN_THRESHOLD is inherited, never measured — the adopter writes neither it nor RECALL_DARK_LAYERS
    WHERE tools/codebase-map/map_lib.py:858-871 (silent default on an absent key); tools/codebase-map/adopt-codebase-map.sh:149 ("EDIT IT (MAP_ROOT, GATE_FILE)" — the two recall knobs are not measured, not prompted, not written)
    EVID  `seam_fanin_threshold()` returns SEAM_FANIN_THRESHOLD_DEFAULT when the key is absent or empty, with no notice. Measured across the fleet: gov declares 3 with the comment "Kept at the kit default of 3 — this is a small tree and the threshold has not been re-measured against it" (self-admitted unmeasured pin); incms declares 3; nc declares neither SEAM_FANIN_THRESHOLD nor RECALL_DARK_LAYERS at all.
    CORR  Line numbers drift by a few: README.md:57 (finding says :56) and .claude/skills/memory-recall/SKILL.md:45 (finding says :42). Three supporting figures I could not verify and that do not carry the finding: the '99-row hard slice' (incms's fixture carries no `slice` key on its queries, so that partiti

[18] CONFIRMED · MINOR · vacuous-selector-empty-population
    Dossier globs rot into fiction — claims are gated both directions, globs in neither
    WHERE tools/codebase-map/map_lib.py:1503-1534 (attribute_paths); tools/codebase-map/test_codebase_map.py (no leg over tree.dossiers[].globs); tools/codebase-map/gen_map.py:184 (scaffolded README: "Claims are exact keys, gate-enforced BOTH directions … Path globs are digest-only, never gated")
    EVID  compute_coverage's assert #2 exists precisely so "dossiers can't rot into fiction", but it only covers `claims`. Measured over the tracked file list, dossier globs matching ZERO tracked files: gov 0 of 73, nc 0 of 1, incms 4 of 609 — ai-assistant: 'services/api/tests/test_assistant_migration.py'; entry-blocks: 'packages/blocks/src/entrySingles.test.tsx'; puck-editor-durability: 'apps/web/component
    CORR  Two adjustments. The junk run returns 40 hits on gov today, not 35, and the repro's term list is 29 tokens rather than the 30 the prose names — neither changes anything. And the one-sidedness is partly deliberate: the code carries an explicit comment at :1156-1157, 'Warn, never refuse: a caller who

[19] CONFIRMED · MINOR · armed-but-unreachable-rule
    The affordance grace is documented as shrinking mechanically; it only shrinks behind a manual flag with zero callers in any of the three repos
    WHERE tools/codebase-map/map_diff.py:12-15 ("Touching a graced feature's files mechanically removes its grace, so the next gate run demands its `## Reuse affordance` block — no human remembering.")
    EVID  `_drop_affordance_exempt` runs only under `--drop-affordance-exempt`. A grep for that flag across *.sh, *.json, *.yml, *.js in gov, incms and nc finds no caller outside the kit's own source and prose. Measured: incms's affordance-exempt.toml was seeded with 74 rows on 2026-07-22 and still holds 72 of 84 feature dossiers (86% graced) after one swap; the affordance corpus reuse_lookup ranks over is
    CORR  The one measurable query costs 10,153 B against a 7,812 B DECISIONS.md — 1.3x, not 1.5x. The 1.5x rests on a 10-question mean (11,750 B) computed from a question set I do not have and could not reproduce; treat the multiple as ~1.3x measured, and the 'priced for a corpus 16x larger' framing as the a

[20] CONFIRMED · OBSERVATION · two-answers-to-one-question
    187 KB of byte-identical duplicated JS sits outside the symbol corpus, so --converge's reinvention detector cannot see the one duplication gov actually has
    WHERE tools/codebase-map/map_extractors.py:233-247 (_build_js_layer walks ROOT/"tools" only); tools/codebase-map/map_diff.py:159-176 (_converge builds its reference index from symbols.json)
    EVID  .claude/hooks/agent-cap.js and tools/hooks/agent-cap.js are byte-identical at 93,786 bytes (cmp: IDENTICAL); .claude/hooks/scratch-guard.js and tools/hooks/scratch-guard.js likewise at 17,235. Neither .claude/ copy appears in symbols.json — the JS extractor walks tools/ only — so collision_flags is structurally incapable of flagging the pair, and dead_exports counts fan-in over a file set that omi

[21] CONFIRMED · OBSERVATION · none
    No command in the kit reports whole-tree coverage; the only number it prints is a per-range percentage dominated by memory/ records
    WHERE tools/codebase-map/gen_map.py:222-247 (modes: --scaffold/--write/--check/--seed-*; no coverage mode); tools/codebase-map/map_diff.py:266-270 (the only coverage line, per-range)
    EVID  `gen_map.py --help` offers no coverage report; `map_diff.py` requires a range and its percentage counts every changed file including records (F4). Run over full history the kit reports gov 201/1397 (14%) and nc 28/1953 (1%) — numbers no one would act on, and neither is the source-coverage figure (gov 68%, nc 0%). So the question this kit exists to answer, "what fraction of the system is mapped", i
    CORR  This is a FORK REGRESSION, not a layout mismatch — which makes it stronger than filed. Upstream incms's DURABLE (scripts/recall/extract.py:75-80) is flat-correct: `memory/DECISIONS\.md$|memory/backlog/[^/]+\.md$|memory/decisions/...`. Running it on incms's own flat tree yields `spine 3905 docs, 3431

[22] CONFIRMED · OBSERVATION · none
    Portability holds for the engine and for cwd; the hardcoded-prefix rot is confined to selftest.py (already logged as F3)
    WHERE tools/codebase-map/map_lib.py:83-154 (resolve_root/kit_dir/relative_kit — pure abspath path math, no directory counting, no resolve()); tools/codebase-map/selftest.py:1243,1287,1290,1296
    EVID  Reported as a NEGATIVE result so it is not re-hunted. Grepping map_lib.py, gen_map.py, map_diff.py, reuse_lookup.py, both templates and adopt-codebase-map.sh for a hardcoded "tools/" or `parents[N]` root derivation returns only prose and comments — every hit is documentation of the prefix-free rule, not an instance of breaking it. Running the CLIs from three different working directories in gov (t
    CORR  Two nits that make the fix bigger, not smaller. The SKILL.md disclosure is at line 69, not 66. And the offending sentence has TWO carriers: gov/AGENTS.md:204 and coding-governance-agents.template.md:132 — the template is the SHIPPED product, so every adopter inherits the overclaim. The one-sentence

[23] CONFIRMED · BLOCKER · grammar-bound-to-the-wrong-root
    check-verdict-epoch.sh hard-codes the kit prefix, so the leg that forces the version marker to move is dead at every adopter install shape but gov's
    WHERE tools/memory-tree/check-verdict-epoch.sh:68-69
    EVID  Line 68 is the literal `ENGINE=tools/memory-tree/check-memory-hygiene.sh` and line 70 turns a miss into `exit 2`. IS: at nc (kit at `scripts/`) and swydee (kit at `memory-tree/`), running the kit's OWN installed copy prints `verdict-epoch: tools/memory-tree/check-memory-hygiene.sh is missing - this gate reads the engine's own source` and exits 2 - a message naming a path that exists at neither ins

[24] CONFIRMED · MAJOR · vacuous-selector-empty-population
    The shipped .memory-tree.conf.example disarms check 12 (the largest check in the gate) and six other checks, silently and with no announce
    WHERE tools/memory-tree/.memory-tree.conf.example:23,30,36,39,55,60,66,140
    EVID  The example a fresh adopter gets ships `TOMBSTONE_ROOTS=""` (11 off), `SPEC_FORMAT_CUTOFF=""` (12 off entirely - 378 lines, check-memory-hygiene.sh:767-1145), `STREAMS_CUTOFF=""`, `SPEC_WITNESS_CUTOFF=""`, `SPEC10_EVIDENCE_CUTOFF=""`, `FORK_MARK_CUTOFF=""` (12's four sub-ratchets off), `REVIEW_VERDICT_CUTOFF=""` (22 off, arming test at :642), `ACCEPTANCE_LEDGER_CUTOFF=""` (23 off, arming test at :
    CORR  One sentence is wrong as written: '208 (45%) also carry a leading underscore' — only 111 of 461 (24%) do. 208 is the UNION of {in a test file} ∪ {nested} ∪ {leading underscore}, which I reproduce at exactly 208 (45.1%). The title's phrasing ('45% vanish if private helpers are excluded') is correct;

[25] CONFIRMED · MAJOR · amendment-leaves-its-other-half-standing
    FORK_MARK_CUTOFF blank - the shipped default and swydee's actual state - reds 73 correctly-resolved specs in gov's own corpus; swydee's EXTR-aPatientHarvest-4 is still live, not fixed
    WHERE tools/memory-tree/check-memory-hygiene.sh:1022-1023
    EVID  The tightened §8 reader (`bmark`, :1013-1020) matches a `RESOLVED (owner|agent, <date>[, delegated])` mark ANYWHERE in the section and is reached only under `fcut != ""`. The loose branch left standing at :1022 counts `resolved` only when the mark is on the item's OPENING line (:1002 `if (rng[i] ~ /RESOLVED/) resolved++`, inside the per-line item test). The kit's OWN comment at :967-969 says the m
    CORR  The fix is cheaper than the finding claims. lexicon.py ALREADY imports canon at line 84 and uses it in the S3 command at line 1065 — the finding's 'scaffold_lexicon.py imports it from the same directory and run_suggest does not' implies the module lacks the import. It does not. The change is one loo

[26] CONFIRMED · MAJOR · pin-copied-from-another-corpus
    The build-README advisory 'high-water' is a seeded median, not a high-water: 39 of 105 slot measurements breach it every run, 76% on one slot
    WHERE tools/memory-tree/build-readme-slot-highwater.txt:21-25
    EVID  `gen_build_index.py --check-format` is a bar leg (tools/gate-legs.json, "build README slot contract") and emits 8789 B / 79 lines at exit 0, all of it advisory. Measured over its 21-file bound population: `## Build-level rules` hw 823, 16 of 21 over (76%), max 1799; `## Parked decisions` hw 543, 11 of 21 (52%), max 1686; `## The problem this build exists to solve` hw 693, 9 of 21 (43%), max 896; `
    CORR  Two adjustments, one of which strengthens it. The conf records EIGHT raises, not nine (412->415->417->463 and 384->452->455->458->460->463 is 8 moves totalling +130). The '705 counts of slack' is from their fresh-adopter scenario; the same demo on gov yields 439. And the finding undersells itself: .

[27] CONFIRMED · MAJOR · two-answers-to-one-question
    Check 23 exists in the gate and the conf but in neither HYGIENE.template.md nor memory/HYGIENE.md, while README.md states '23 checks' - and the parity harness compares copy to copy, so it cannot see the gap
    WHERE tools/memory-tree/HYGIENE.template.md:253
    EVID  The gate's header calls HYGIENE.md the single source of truth ("HYGIENE.md's 'Check' section, CI, the pre-commit hook... all invoke THIS script"). Check 23 has four fail arms (check-memory-hygiene.sh:1377-1379), two conf keys (ACCEPTANCE_LEDGER_CUTOFF, ACCEPTANCE_LEDGER_GRANDFATHER), a `--staged` hold announcement and an empty-population announcement. IS: the numbered check list in tools/memory-tr
    CORR  The demo's specific numbers (147 tracked files, 19 verbs, 55 of 58 ungraded, 5.2%) are from a fresh adopter, not from gov — on gov the identical three edits drop coverage from 42.0% to 8.0% (11 of 138 definition-carrying files armed) and graded from 1047 to 122, with both legs still green. The concl

[28] CONFIRMED · MAJOR · amendment-leaves-its-other-half-standing
    RECORD_SERVES_CUTOFF was retired from the engine without a retired-key notice, so nc's upgrade path is a green gate turning into 612 findings with no explanation
    WHERE tools/memory-tree/corpus_ids.py:52
    EVID  nc runs memory-tree 2.49, whose check 21 branch A is filtered by `RECORD_SERVES_CUTOFF` (nc/scripts/check-memory-hygiene.sh:735,752,764) and which nc declares as `RECORD_SERVES_CUTOFF="2026-08-28"`. The key does not exist anywhere in the current 2.55 kit (`grep -r RECORD_SERVES_CUTOFF /tmp/kite/gov/tools/memory-tree/` is empty). IS: running the current kit against nc's tree turns nc's 178-byte exi
    CORR  Real, but the severity is overstated at major. No gate reds on any of these today: gov's VERB_OFFENDER_PIN absorbs all 461 offenders, and the five unrenameable ones are 1.1% of that pin. The live harm is confined to the advisory surfaces — a polluted `--list`, and `--suggest` refusing protocol slots

[29] CONFIRMED · MINOR · vacuous-selector-empty-population
    memory/guides/ and memory/archive/ accept any filename, any file kind and arbitrary nesting - no check in the kit reads them for placement or naming
    WHERE tools/memory-tree/check-memory-hygiene.sh:292-293
    EVID  Check 3's whitelist admits `D:guides` and `D:archive` and treats their contents as opaque; no other check imposes a name grammar there (checks 4 and 5 are anchored on `builds/`, check 6 caps guide BYTES only, check 10 reads only `archive/<INDEX>.<date>.md`). IS: five synthetic breaks staged on a clean gov clone, each committed to the index and run through the full gate, all `exit 0` with no output
    CORR  One count is off by one in each half: the incms scaffold declares 45 extensions, 43 of them dark (not "42 dark of 44") — the two armed are py and js. Everything else, including the fix and the argument against arming sh, stands as written.

[30] CONFIRMED · MINOR · fixture-passes-by-finding-nothing
    adopt-memory-tree.sh's stated invariant is false on the second run: it does scaffold the demo disciplines, and the kit carries two demo taxonomies that disagree
    WHERE tools/memory-tree/adopt-memory-tree.sh:46
    EVID  Line 46 reads "# .memory-tree.conf is REQUIRED - never silently scaffold the built-in DEMO disciplines into a real repo", enforced by :47-51 which copies the example, prints EDIT IT, and exits 1. IS: on the second invocation the conf exists, so :52 sources the UNEDITED example and :164 scaffolds `Scaffolded memory/ (3 disciplines)` with `memory/backlog/{ARCH,DEPL,DES}.md` - the example's demo taxo
    CORR  Accurate as filed, including its own severity call (minor, provenance not vocabulary). One nuance worth keeping: the docstring's claim #1 is specifically about the eleven NEGATIVE definitions, not the spellings — the author of canon.py had .lexicon.conf in the tree either way, so the independence cl

[31] CONFIRMED · MINOR · degradation-known-but-unreported
    A checks-17-19 failure prints without its check number, so the one delegate whose output is passed through raw cannot be attributed or grepped
    WHERE tools/memory-tree/check-memory-hygiene.sh:1181-1184
    EVID  Every shell-owned arm goes through `fail <n>` and emits `HYGIENE check <n> FAILED - ...`; the corpus_ids and row_grammar delegates carry their own `check 16:` / `check 20:` prefixes. gotchas.py's does not. IS: dropping one malformed record into memory/gotchas/ produces `HYGIENE memory/gotchas/zzjunk.md: no front matter - a record opens with a '---' block at line 1` and exit 1, with no check number
    CORR  The swydee pin figure is inflated by the measurement setup: on a clean clone where the copied kit is untracked, the scaffold reports 261 definitions and VERB_OFFENDER_PIN=185 (71%), not "195 of 306 (64%)". The quoted numbers silently include the kit's own 45 defs and 10 offenders, i.e. the finder's

[32] CONFIRMED · MINOR · two-answers-to-one-question
    swydee's EXTR-aPatientHarvest-3 was fixed upstream by correcting a default, but nothing machine-checks the answered value against the gate that refuses it
    WHERE tools/govkit/entries/playbook.kit.toml:219-232
    EVID  The row reads "AGENTS.md:167 prescribes a singular `review/` Tier-2 artifact folder, but memory hygiene check 4 sanctions only `reviews/`". Root cause: the charter template carries `{{REVIEW_DIR}}` (coding-governance-agents.template.md:250) and the value is answered per target. TOOL-aScouredKit-14 corrected the shipped default to `memory/builds/<slug>/reviews/` and its `why` says "must agree with
    CORR  The repro line's expected output is wrong: `--list | grep -c '^  tools/lexicon/'` prints 10, not 7. The "+3 more counted by scope" parenthetical is unnecessary — the single command already returns the full 10 the evidence claims.

[33] CONFIRMED · OBSERVATION · none
    --survey reports 67 of 88 build READMEs as unbound with 1041 violations at exit 0, and the slot contract's own registry exempts the same 67
    WHERE memory/project/readme-contract.txt:1
    EVID  `gen_build_index.py --survey` emits 87392 B / 1130 lines naming 67 distinct build READMEs and 1041 violations (534 'authored content between the title and the first canonical heading', 313 'canonical slot missing', 187 'heading outside the canon', 7 'out of order'), exit 0. The registry's first line is `exempt-pin: 67`, so the bar leg 'build README slot contract' grades 21 of 88 (24%). Not a defec
    CORR  Downgrade blocker to major, and drop the implication that the gate misreports its own contract. tools/codebase-map/README.md:62 states the limit outright — "path globs are digest-only and never gated" — so the ratchet is honest about covering keys in both directions and nothing else. The defect is n

[34] CONFIRMED · MAJOR · two-answers-to-one-question
    The recall floor grades a configuration the CLI does not ship: gate reports 0.8333, the shipped CLI delivers 0.7500 — the README's own RED value
    WHERE tools/memory-recall/check-recall.py:69
    EVID  `RECALL_FLOOR="records:fts5:r@5>=0.81"` (.memory-tree.conf:286) grades the `records` FTS5 index alone, on the raw un-rewritten question. The CLI (query.py:1177) serves `rrf([search(records), search(chunks)])` at a DEFAULT `--k 20` and REQUIRES `--terms`. Neither divergence is expressible in the pin grammar: `SETS = ("spine","records","chunks")` has no ensemble token, and `bench.rank_with` is fed `
    CORR  Same downgrade as its sibling: major, not blocker, and it shares one root cause with finding 33 (path globs are ungated by documented design) rather than being an independent defect. Treat the two as one mechanism measured in two repos — the interesting delta is that gov, which SHIPS the kit, has un

[35] CONFIRMED · MAJOR · fixture-passes-by-finding-nothing
    The floor's fixture is all one family: gov greens with three of its four declared id families mis-declared and 80 records silently out of the index
    WHERE tools/memory-recall/recall-fixture.json:1
    EVID  All 12 `expected_ids` are `TOOL-`. gov declares four families (`FAMILIES="playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL"`) and anchors 860 records: TOOL 780, DEPL 67, PLAY 12, KICK 1.

MEASURED with PLAY/KICK/DEPL mis-declared to PLAZ/KICZ/DEPZ:
  index 860 records -> 780 records (80 records, 9.3%, leave the record arm)
  check-recall: per-id ok -- every expected id resolves in records (12
    CORR  The gov evidence is a measurement artifact and must be withdrawn. `git log --follow` walks only commits that touched the file and diffs NON-ADJACENT snapshots across a branchy history. Re-measured against each commit's real parents, gov has 3 post-backfill additions, not 11 across 6 commits — and al

[36] CONFIRMED · MAJOR · armed-but-unreachable-rule
    The ZERO RECORDS diagnosis is a zero-predicate, so the one-character FAMILIES typo it was written for goes undiagnosed
    WHERE tools/memory-recall/extract.py:390
    EVID  The guard is `if n_records: return None`. Its own docstring names the motivating case: "Point the conf at a corpus whose ids it does not describe and upstream returns 'index 0 records + N chunks' and reports success -- a healthy-looking run that silently answers from half the index." A one-character typo in ONE of several declared families produces exactly that half-index run and never zero, so th
    CORR  Understated, if anything: I also ran the kit's own selftest on the broken copy and it prints PASS and exits 0. So an emptied symbol tier is invisible on EVERY codebase-map leg — the coverage gate, the freshness check, the kit selftest, and the recall consumer — not just the two named in the finding.

[37] CONFIRMED · MAJOR · two-answers-to-one-question
    memory-tree's backlog template and memory-recall's anchor grammar disagree, so a repo that follows the shipped template gets ZERO backlog rows into the record index
    WHERE tools/memory-recall/extract.py:115
    EVID  All four anchors require the id IMMEDIATELY after the list marker / heading / first table cell: `A_BOLD_LI = ^\s*[-*]\s+[`*]*(ID)\b...`, `A_DASH = ^\s*[-*]\s+[`*]*(ID)\b[`*]*\s*[·|]`. The memory-tree adopter writes each backlog with the header "> Mutable. Each row leads with one status token (OPEN…WONTDO)." (tools/memory-tree/adopt-memory-tree.sh:238).

A repo that obeys that sentence writes `- OP
    CORR  Accurate as written except for one conflation: RECALL_DARK_LAYERS names LAYERS (extractor roots), not extensions. incms's SYMBOL_EXTRACTORS are root-scoped - services/api/app, packages/{blocks,ui,theme}/src, apps/web - so the .py 394/1164 ratio mixes genuinely dark trees (scripts/, tests/, tools/) w

[38] CONFIRMED · MINOR · two-answers-to-one-question
    README declares bench.py and union.py "inert here" to justify not wiring them; both run against the kit's own committed fixture in one command
    WHERE tools/memory-recall/README.md:197
    EVID  README: "`bench.main()` / `union.main()` are the upstream benchmark harnesses, which are **inert here** — they need a graded `fixture.json` that this kit deliberately does not ship." The kit ships `recall-fixture.json`, and both accept it as a positional path.

MEASURED, from a fresh gov clone:
  python tools/memory-recall/extract.py . DATA --chunk-max 600
  python tools/memory-recall/bench.py DAT
    CORR  Two corrections. (1) nc's six queries return 12 candidates total, not 21 - three of the six ("parse a yaml config file", "cache an expensive computation", "retry a failing network call") honestly return the empty 'no seam fits' path. Precision is still 0/12 = 0%. (2) The title's "the tool never says

[39] CONFIRMED · MINOR · pin-copied-from-another-corpus
    query.py --help states the headline recall gain with no provenance; README and SKILL both say it is upstream's number on upstream's corpus
    WHERE tools/memory-recall/query.py:1
    EVID  query.py --help: "Rewriting is the measured half of the retrieval gain (records recall@20 0.71 -> 0.84, MRR 0.389 -> 0.530, for zero committed bytes)". No qualifier.
README.md:56: "the measured half of the retrieval gain upstream (records recall@20 0.71 → 0.84 on its hard slice)".
.claude/skills/memory-recall/SKILL.md:42: "Upstream measured the rewrite at records recall@20 0.71 → 0.84".
The figure
    CORR  The premise 'NicoCares ships no runtime code' is true of package/ and false of the repo. But the counting correction: 719 today and 435 at the adoption commit - so the docstring was ~17x low when written and is ~28x low now. The finding's '254 across 28 files are project-owned non-kit' is filter-dep

[40] CONFIRMED · OBSERVATION · armed-but-unreachable-rule
    TERM_BAND's upper bound is never a predicate — the CLI's mandated 8-14 input band is enforced on one side only
    WHERE tools/memory-recall/query.py:1155
    EVID  `TERM_BAND = (8, 14)` (query.py:133). The only test is `if has_terms and len(terms) < TERM_BAND[0]`; `TERM_BAND[1]` appears exclusively inside the warning's f-string. Supplying 30 terms is silently accepted; supplying 6 is warned about.
Over-supply is the likelier failure for a model told to write "8-14 words in repo jargon", and it is the unwarned side.
MEASURED — 10 gov questions, base terms (12
    CORR  Accurate. Worth adding for whoever fixes it: an adopt-time measurement of SEAM_FANIN_THRESHOLD is impossible in a repo whose symbol corpus is empty (nc has 0 symbols), so the adopter has to either measure-or-refuse-and-say-so rather than measure-always.

[41] CONFIRMED · MINOR · pin-copied-from-another-corpus
    DEFAULT_BUDGET is upstream's 40 MB-corpus measurement, unchanged in every adopter — on swydee one query costs 1.5x the entire ratified decision index it usually answers from
    WHERE tools/memory-recall/query.py:132
    EVID  `DEFAULT_BUDGET = 20_000`, commented "the MEASURED cost of the shipped configuration: union.py reports 19 606 B for records:fts5+chunks:fts5 at k=20 PER SOURCE" — measured on inCMS's 40 MB corpus and 184-query fixture. The same literal is in swydee's memory-recall 1.0 (query.py:122) against a 1.2 MB tree.

MEASURED on swydee (10 questions whose answers I established first by reading the whole corp
    CORR  Two corrections. The scaffolded-README line 'Path globs are digest-only, never gated' is gen_map.py:119, not :184. And 'each degrades attribution silently' overstates the effect: a glob naming a deleted file mis-attributes nothing, because the file is gone. The real exposure is a rename or replaceme

[42] CONFIRMED · OBSERVATION · armed-but-unreachable-rule
    The DEAD ALIAS diagnosis is also a zero-predicate: a 99%-dead alias layer is silent
    WHERE tools/memory-recall/query.py:270
    EVID  `if not a.get("ids") or a.get("joined"): return None` — one joining id disarms the whole diagnosis. This is DISCLOSED in the docstring ("Silent on a partial join: some ids resolving is the normal state of an alias file written ahead of the records it names"), so it is a decision, not an oversight — but the manifest already carries both `ids` and `joined`, so a coverage ratio costs one f-string and
    CORR  'Zero callers in any of the three repos' is wrong as stated, and the repro's --include list is what hides it: the only caller lives in a .md. gov's WIRE-INTO-PROJECT.md:319 prescribes `python <kit>/map_diff.py <base>..<head> --drop-affordance-exempt` as an adopter DoD step, repeating 'no human remem

[43] CONFIRMED · MINOR · grammar-bound-to-the-wrong-root
    The `spine` document set extracts to zero docs in every flat memory tree; DURABLE is bound to the pre-flat two-level layout
    WHERE tools/memory-recall/extract.py:127
    EVID  `DURABLE` requires `<MEMORY_ROOT>/<dir>/(DECISIONS|BACKLOG).md`, `<MEMORY_ROOT>/<dir>/decisions/*.md` or `<MEMORY_ROOT>/<dir>/archive/(DECISIONS|BACKLOG).*.md`. memory-tree 2.x is FLAT: gov, nc and swydee all keep `memory/DECISIONS.md` and `memory/backlog/<FAM>.md`, one level up from the pattern.
MEASURED: spine.jsonl is 0 rows / 0 bytes in all three (gov 860 records, nc 609, swydee 31); every ext
    CORR  Three corrections, none fatal. (1) The extractor is map_extractors.py:212-213 (`enumerate_exports(ROOT / "tools", ...)` + `scan_js_definitions(ROOT / "tools", ...)`), not :233-247. (2) '.claude/hooks/agent-cap.js and scratch-guard.js are unmapped' is not claimed but implied - in fact attribute_paths

[44] CONFIRMED · OBSERVATION · none
    The gov fork dropped the only pre-registered recall-vs-grep harness, and upstream's verdict on it is UNDERPOWERED
    WHERE tools/memory-recall/kit.toml:1
    EVID  Upstream ships `grep_study.py` (41 KB, "The recall-vs-grep head-to-head") plus `agent_queries.py`, `ceiling.py`, `redundancy.py`, `alias_bench.py`, `alias_distinct.py`, `rewrite_bench.py`, `session_stats.py`. The gov fork ships none of them.
Upstream's own committed verdict (incms memory/builds/aGrittedFlagstone/build/2026-08-02-build-aGrittedFlagstone-3-verdict.md): "**`verdict: UNDERPOWERED`.**
    CORR  The duplicate-claim half is REFUTED and should be dropped: the generated MAP.md renders every claimant on the key's own row - gov line 168 reads `| bounded-through-a-pipe-is-unbounded.md | run-gates, unattended |` - so a two-owner key does NOT look identical to a one-owner key. Only an aggregate cou

[45] CONFIRMED · OBSERVATION · none
    No adopter has a retrieval floor, and the one silent regression that exists is the one no adopter can see
    WHERE tools/memory-recall/kit.toml:20
    EVID  kit.toml withholds `recall-fixture.json`, `check-recall.py` and `test_recall_floor.py` as `project-owned`, with a well-argued rationale (shipping gov's question set to an adopter is `pin-copied-from-another-corpus`). Confirmed on the ground: nc and swydee ship the engine and none of the three, and neither declares any `RECALL_*` key. Copying check-recall.py in refuses correctly — `REFUSED -- RECAL
    CORR  Accurate, including its own caveat - I also did not exercise the linked-worktree arm, so that sub-claim remains unverified by this pass too. One addition worth carrying: gov's map_extractors.py:212-213 DOES hardcode ROOT/'tools' for the JS layer. That file is project-owned rather than kit source, so

```
