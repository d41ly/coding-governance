# Research: retrofitting gov's practices into an existing repository, run A

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 83's return, verbatim. Its question is in
`prompts/2026-10-17-prompt-PLAY-dClosedLoop-1-1-researcher.md`, which dispatch 84 runs too, and its use is in
`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`.

---

I rate retrofit a system that cuts across the layers, built on one legacy ledger in the core. Every probe below was read-only, and no file in the repository changed: `git status --porcelain` showed 0 lines before and after. I did not open the gap register or the 2026-10-17 retrofit record, because the handoff doesn't name them. Paths are relative to `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\`.

## 1. Verdict

Retrofit is a system across the layers, like the five, and it is neither a layer nor an expansion. Its core is one **legacy ledger**. A single factory in `tools/lib` gives every check a seeder, and at adoption that seeder records the debt the check finds as `(check, subject, class) → count` rows stamped `seeded:<sha>`.

Gates refuse a ledger that grows against the branch base. Each unit drains the legacy sites inside the hunks it changes, under a cap, so legacy no unit touched never reds. A reconstructed record carries `origin: reconstructed`. Each of the repository's own practices gets one owner disposition, asked in order of instance count. Observability adds a worklist weighted by reads, and distribution runs the seed at install. The core needs neither.

## 2. Today

| Part | What it does | Measured | Where |
|---|---|---|---|
| codebase-map baseline | Inventory keys no dossier claims yet. The gate refuses a new unclaimed key, a stale row or a lazy row, and since 2026-10-05 refuses a key the base didn't carry | 69 keys at the 2026-08-09 seed, 36 now, flat since 2026-10-11. Inventory grew 72→365 items, and only 3 were claimed at seed | `test_codebase_map.py:138-174`, `54c8d081f` |
| What shrank it | 9 commits. All are unit work that wrote a dossier for code it was touching | the 5 kits still baselined are touched hard: workflows 287 and drift-audit 194 commits in 90 days. **Touching does not force a claim** | `git log --follow` (below) |
| affordance grace | Touching a graced dossier's files is supposed to drop its grace | seeded empty. `--drop-affordance-exempt` is invoked by nothing in `tools/`, `.claude/`, `.github/` or `.githooks/` | `map_diff.py:107-118`. **The record disagrees:** `WIRE-INTO-PROJECT.md:554` calls the drop mechanical, but it is a by-hand DoD step |
| Per-check legacy registries | Each check keeps its own shrink-only exemption file | 27 files, at least 6 row grammars. The `(path, class) → count` ratchet exists twice: `encoding_posture.py:165-221` and `sh_hygiene.py:384-470` (the second takes the shape as a parameter) | `memory/project/*.txt`, `tools/*waivers*.txt` |
| "Shrink-only" claims | Only the map baseline refuses growth against its base. The others red only on a stale row | unarmed-branches 9→159, spawn-idiom 292→303, substitution-fed 18→47→43, encoding 18→16. drift-audit tracks 5 of the 27 from a hand-typed list and reports 3 of those 5 not shrinking | `drift_signals.py:129-138`. **The record disagrees:** `unarmed-branches.txt:2` says SHRINK-ONLY |
| Date cutoffs | Grandfather records by date | 34 `*_CUTOFF` keys armed (24 in `.memory-tree.conf`), plus 6 pins | `cutoff_keys_armed` |
| Lexicon marginal rate | Offenders per added definition, graded against the adoption commit | 12.0% overall. **9.1% in fresh files against 16.1% in files that predate the declaration**: code added inside legacy copies legacy practice | `drift_report.py:1434-1540` |
| Leg guards | A leg runs only when its watched paths change | 76 of 140 legs carry a guard | `gate-legs.json`, `run-gates.sh:402-412` |
| Adopt-time seeding | Each kit's adopter seeds its own pins, telling the operator in prose to measure them against their own corpus | 4 adopters, 4 different mechanisms | `adopt-codebase-map.sh:199`, `adopt-memory-tree.sh:93,703,717`, `adopt-drift-audit.sh:263` |
| Record bindings | Hygiene check 21 reds an untouched tree on its first run, "by design" | the fix is a mechanical `none` pass, then a pin | `WIRE-INTO-PROJECT.md:396-430` |
| Deployer and census | What "retrofit" means today: installing kits, upgrading living docs, and a blob census of the adopter's kit files | brings no code under gov's practices | `governance-deployer-research.md:22-26,69-71`, `census.py:1-30` |
| Instruction docs (IW-1) | The legacy list is designed and not built | 44 docs at instruction paths, 623,241 B, 42 of them changed in 30 days | instruction paths (probe below) |
| Comment refs | Ids cited in source | 2 of 1,250 resolve to nothing | `source_cited_ids_resolving_to_no_record` |
| Authored descriptions decay | Dossiers written before the code they describe moved | 25 of 31 dossiers sit behind their paths | `dossiers_older_than_their_paths` |

**Touch reach.** gov's history starts 2026-07-01, so the 365-day window is the whole history.

| Measure | Result |
|---|---|
| Code files changed in the last 30 / 90 / 365 days | 230/236 (97.5%) / 236/236 / 236/236. Unchanged since landing: 6 (2.5%) |
| Code **lines**, by blame age | ≤7 days 11.5%, ≤30 days 51.4%, ≤90 days 98.9% |
| Concentration | the top 20% of files (46) take 65.1% of the 4,634 file-touches in 30 days |
| Reads, from 1,811 transcripts and 52,566 code reads (97.6% of them shell reads) | 99.3% land on files changed in the prior 30 days; 92.7% on files changed in the prior 7 days, though those files are only 61% of the tree; 64.5% on the top-20% churn files, a 3.2× lift |

**Sources a repository already holds,** as gov's tree yields them.

| Source | What gov yields | What a check could trust |
|---|---|---|
| Commit messages | 2,959 of 6,001 subjects carry a unit id; 1,829 `Decided:` trailers against 279 log rows; 539 `fix` subjects | the paths and the SHA, which are git fact. The text is typed, so it is a candidate only (P2) |
| Comments and docstrings | 5,905 comment lines cite ids, and 1,248 of 1,250 resolve; 69% of the 3,241 Python definitions and 100% of modules carry a docstring | resolved refs, as pointers. The prose is not trusted |
| Documents shaped like decision records | 26 files carry Status, Decision or Context headings, all gov's own records | candidates for the two-rater routing |
| Tests | 80 test files; 39 of 156 code files have a test sibling by name | run by the executor, never read as fact |
| CODEOWNERS and lint configuration | none in gov | not measurable here |

Commands and their output:
```
for c in $(git log --reverse --follow --format=%h -- memory/map/baseline.toml); do …grep -cE '^\s+"'; done
f9cf666c8 2026-08-09 keys=69 … 3b5f9b116 2026-08-26 keys=43 … 83269a93e 2026-10-11 keys=36
git log --since=2026-09-17 --name-only | comm -12 code.s → 30d 230 ; blame buckets → lines=279814 <=7d 11.5% <=30d 51.4%
python reads.py → reads 52566, r30 52216, r7 48726, top 33902 → 99.3% / 92.7% / 64.5%
python drift_report.py --json → lexicon_marginal 597/4963, fresh 262/2879 9.1%, predating 335/2084 16.1%;
  shrink_only_lists_not_shrinking 3/5; source_cited_ids 2/1250; dossiers_older_than_their_paths 25/31
```

**What gates do on code no record describes:**
- **Red:** map coverage on an unclaimed key outside the baseline; check 21 on unbound records; the designed annotation resolve check, which the systems record says reds on day one.
- **Pass by finding nothing:** every `gov:` check today (0 `gov:note` and 0 `gov:feature` lines). drift-audit's DEAD PROBE and not-asked states guard against reading that as clean.
- **Already read a baseline:** 27 registries, 34 cutoffs, 6 pins, the template high-water and the line-length limits.

## 3. Across the layers

| Layer | Retrofit needs from it | Retrofit gives it |
|---|---|---|
| instruction | IW-1's legacy list and the render gate; a slot in the work order | its seed of the adopter's own instruction files into IW-1's list; one charter line: "drain what you touch" |
| flow | `build.scope`, the scope base, and the patch-build entry at Design | the drain check inside `build.scope`; the adoption items; `retrofit.sweep` |
| roles | the builder and the two raters; the owner's dispositions | nothing new; it reuses the shapes |
| memory | the contract: record kinds, `origin` and the index | the ledger kind (it is the "gates' row registries" home, `layer-memory:559`), the census record, reconstructed records |
| runtime | command adapters with seed probes; the journal | a `seed` field on each check's registration |
| observability | Maintain's readings and the journal's reads | the `legacy.hot` reading and the not-draining reading |
| integrations | tracker and CI adapters | optional importers: tracker issues become candidate classes, and existing CI jobs stay alongside as legs |
| distribution | `kits.install` | the install calls `adopt.seed`, and the census runs once |

| System | Needs | Gives |
|---|---|---|
| tags | the grammar, and `check` tags for ledger rows | the positional-reference ratchet (`design-tags:218-220`) becomes a ledger instance |
| annotations | the touched-block budget (`design-annotations:252-253`) | the "≥9 lines" legacy ratchet becomes a ledger instance; the `refs=` sources come from the 1,248 resolved comment refs |
| instruction writing | IW-1's shrink-only list | the list is a ledger instance seeded at adoption |
| role shapes | the `single` shape and the panel for the raters | none |
| memory structure | `memory.legacy-anchors` | a reconstructed record holds `origin` as a required head field |

## 4. Candidates

| | A: seeded ledger with hunk drain | B: derived from the adoption SHA, with no stored rows | C: bulk reconstruction at adoption | D: cadence sweep, hottest first |
|---|---|---|---|---|
| Mechanism | One factory. Each check seeds `(check, subject, class) → count` at adoption. Gates refuse growth against the base and require drain in changed hunks | blame classifies a line as legacy or new against the adoption SHA, and a gate grades only new lines | agents write dossiers, annotations, decision rows and classes for the whole tree up front, then gate everything with no baseline | Maintain picks the legacy with the most reads each period and opens patch builds |
| Efficiency (method) | Drain per code commit, from site density × lines touched, over 1,093 commits in 30 days: median 0.03, mean 0.25, p90 0.46, max 35.1 sites. Slot ≤1 KB. 0 extra lookups | the same drain. Blame takes 13.3 s for the whole tree (about 0.06 s per file), so about 0.17 s for a median 3-file write set | gov's 1,829 decision candidates and 365 inventory keys all authored before any touch | adds reach only to code read but not recently touched |
| Smallest losing test | the subjects it cannot express | can it baseline subjects that aren't lines? | does a description authored ahead of touch stay true? | what share of reads does it add beyond touch? |
| Result | **survives.** The factory shape fits all 27 registries, line-keyed or key-keyed | **loses.** Only 7 of 27 registries key on a site. Feature coverage, record bindings, unarmed branches, tokens and instruction docs have no blame line, and blame can't hold a reason. It also needs full history: drift returns DEAD PROBE on a shallow clone (`drift_report.py:1502`) | **loses.** 25 of 31 authored dossiers are already behind their paths, and the owner would face 1,829 candidates for about 12 major decisions | **loses as the primary mechanism**: in gov it adds at most 0.7% of reads (100 − 99.3), and as an expansion it can't be what the core needs (P28). It stays as an add-on |

The scope of the drain separates the variants. **File-scoped** drain would put a median of 55 and a p90 of 303 sites on each code commit, and 831 of 1,093 code commits would carry some. That is rejected. **Hunk-scoped** drain gives the median of 0.03 above. Today's per-file count ratchet lets touched legacy persist: of 129 encoding-posture sites, 29 sit on lines edited after the leg was armed on 2026-09-23. That is the gap hunk drain closes.

```
python - (encoding_posture.scan_tree + blame -L) → hits 129, before arming 100, after arming 29
file-scoped: sites per code commit median 55 mean 117.0 p90 303 ; hunk-scoped: median 0.03 mean 0.25 p90 0.46 max 35.1, share>20 0.0018
```

## 5. The pick, specified (A)

**Row grammar:** `<check-tag> TAB <subject> TAB <class> TAB <count> TAB <seeded:<sha> | reason:<text> | keep:<ask-id>>`.
- The subject is a path, a key or a record id, never a line number (the existing house rule, `encoding_posture.py:179-182`).
- The rows stay in each check's home. The index of all ledgers is derived from the check registrations, which replaces drift's hand-typed list.

**The factory** is `tools/lib/legacy_ledger.py`. It extends `sh_hygiene.read_registry`/`check_registry` and `map_lib.resolve_compare_base`/`derive_baseline_additions`, and it sits beside `compute_coverage`, which is already moving to `tools/lib` (`design-tags:216`).

**Registration:** each check declares `ledger`, `seed` (an argv measured at a SHA), `subject` (site, key or record) and `drain` (hunk, key or none).

**Owner:** the gates under flow's Test. dWitnessedBar builds the factory, the leg and the seed. dTotalRecall declares the ledger and census kinds and the `origin` field. dBoundRoles renders the slot.

**Checks** (the `ledger` leg pack):

| Check | Red on |
|---|---|
| never gains | a row or count above the base's (generalizes `test_codebase_map.py:152`) |
| both ways | a measured site with no row, or a row the scan no longer finds |
| hunk drain | a site inside the unit's changed hunks still on the ledger, without a `keep:` row or a deferral within the cap |
| key claim on touch | a unit whose write set holds a baselined key it didn't claim (one claim per unit) |
| provenance | a library record anchored only to code that landed before the seed SHA, but missing `origin: reconstructed` |
| seeded | a registered check with no seed. It reads "unseeded", never green |
| populated | an empty ledger population after the seed. Arm this once a planted row has been seen red |

**Read-path cost:**
- The work order's legacy slot holds counts per (path, check) for the write set, at most 1 KB. Raw rows would run 884 B at the median and 7,012 B at p90, so beyond the cap an agent queries `gov legacy show <path>`.
- The slot renders in one of three states. It is 0 B when the write set holds no legacy.
- Orientation lookups: 0.
- The gate adds one `git diff -U0` over the unit's range.

**Progress reporting:**
- A derived `legacy` card cell shows, per check: seeded, now, and drained this period.
- Under observability, a second number gives the share of journal reads that land on ledgered files.

**Modes:**

| Mode | Covers | Cost | Practices |
|---|---|---|---|
| adoption | seed every check; census the repo's practices; import decision-shaped documents as reconstructed candidates | one seed run per check; owner decisions = practices found, about 6 in gov, plus major decisions ratified, about 12 | all checks, decisions, instruction units |
| touch (default) | changed hunks; touched features claimed | mean 0.25 sites per commit. At gov's rate that drains about 273 of 2,358 sites a month, an estimate | annotations, map and reuse, classes, tags |
| cadence (observability) | a read-weighted worklist, filed as asks only | one reading per period | all |
| owner's ask | a scope or check swept through a patch build | as sized at Design | any |

**Per practice:**

| Practice | Derived | Agent judgment | Owner |
|---|---|---|---|
| tags | ids and positional references found by scan | which tag a block gets | the namespaces |
| annotations | `refs=` from resolved comment refs | the note's definition, on touch | none |
| map and reuse | definitions and callers (generated) | dossiers and proposed entries, on touch | accepting entries (LR-6) |
| decision log | candidates from decision-shaped docs and trailers | two raters, kappa ≥ 0.8 (`layer-memory:562-566`) | ratifying the majors |
| bug classes | candidates from fix commits and issues | the class symptom | none |
| specs | none; legacy code has no spec, and cutoffs grandfather it | written only for new units | none |
| instruction units | the existing files go on IW-1's list | migration, on touch | retiring their own docs |
| records | bindings marked `none` | real bindings | none |

**Marking.** A reconstructed record carries `origin: reconstructed <sources>`. It is never a witness, and work orders label it.

**The repository's own practices:**
- The census rows each practice with its instance count.
- The owner disposes each one as import, translate, keep alongside or retire, asked largest first.
- Until the owner decides, a practice stays alongside, so nothing is retired without a disposition.

**What it never does without the owner's ask:**
- edit code outside a unit's write set;
- reformat code;
- write reconstructed records for untouched code;
- retire one of the repository's own practices.

## 6. Items and policies

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `adopt.seed` | command | runs every registered seed at HEAD and writes the ledgers | the seed record, and each check green at the seed SHA | unseeded check → as `retrofit.unseeded` says |
| `adopt.census` | command | detects the repository's practices and counts their instances | the census record | `adopt.practices` |
| `adopt.practices` | owner | disposes each practice | disposition rows | held → alongside |
| `adopt.decisions` | two raters, then the owner | routes the candidates; the owner ratifies the majors | kappa record, and rows marked reconstructed | kappa < 0.8 → rubric revised |
| `build.scope` (filled) | command | lists hunk-scoped legacy and checks the drain within the cap | the scope report | over cap → deferral rows plus an ask |
| `retrofit.sweep` | owner's ask | patch build at Design | the intake | Design |
| `maintain.read` (`legacy.hot`) | command (observability) | ranks ledgered files by reads | journal lines | over pin → `maintain.file` |

| Key | Values | Default | Why |
|---|---|---|---|
| `retrofit.drain` | hunk, file, off | hunk | file scope: median 55 sites per commit; hunk: 0.03 |
| `retrofit.drain-cap` | 5, 20, 50 sites per unit | 20 | binds on 0.18% of code commits (max 35.1) |
| `retrofit.claim-on-touch` | feature, off | feature | 5 baselined kits are touched hard and still unclaimed |
| `retrofit.reconstruct` | on-touch, at-adoption, on-ask | on-touch | 25 of 31 authored dossiers stale |
| `retrofit.decisions-import` | docs, docs-and-trailers, none | docs | 1,829 trailers against about 12 majors |
| `retrofit.practice-pending` | alongside, refuse | alongside | no retirement without a disposition |
| `retrofit.unseeded` | refuse, report | refuse | an unseeded check reds legacy on day one |
| `retrofit.slot-bytes` | 512, 1024, 2048 | 1024 | p90 of raw rows is 7 KB |

## 7. Gaps

Partly closed, from the named sections: `gap-mem-03` (claim-on-touch feeds reuse proposals) and `gap-mem-02` (major decisions found through the import and ratification path).

New gaps:
- **gap-retro-01, dWitnessedBar:** no ledger factory. 27 registries, at least 6 grammars, two copies of the count ratchet, and drift tracking 5 of them by hand.
- **gap-retro-02, dWitnessedBar:** the per-file count ratchet lets touched legacy persist (29 of 129 sites).
- **gap-retro-03, dWitnessedBar:** "shrink-only" is enforced only for the map baseline. unarmed-branches grew 9→159.
- **gap-retro-04, dTotalRecall:** touch-drop isn't wired, and the runbook says it is (`WIRE-INTO-PROJECT.md:554`).
- **gap-retro-05, dTotalRecall:** no census of practices, no `origin` field, and no progress cell.

These need checking against the register at the fold, since I didn't open it.

## 8. Forks

| Fork | Options, recommended first |
|---|---|
| RF-1 placement | a system across the layers with a core ledger; a new `retrofit` expansion, which fails P28 because the core's gates red on legacy without it; folding it into distribution |
| RF-2 drain scope | hunk; file; none |
| RF-3 mining decisions from commit trailers | only at the owner's ask; at adoption |
| RF-4 a repository practice not yet disposed | stays alongside; proposed for retirement |
| RF-5 gov's own 27 registries | migrate them onto the factory in dWitnessedBar; leave them as they are |

The probe scripts are in `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\` (`reads.py`, `bl.sh`, `drift.json`).
