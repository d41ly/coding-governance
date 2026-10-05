# TOOL-aMendedFleet-24 — dead repo paths in live build READMEs are reported, and the decision log's dead pointer is repaired

**Status:** SPECCED · rev-3 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 24

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Hygiene check 15 grades dead repo-path citations in the present-tense corpus only, and a build folder
is a record of a moment, so a LIVE build's README, which sessions read to orient, can cite a moved or
misspelled path and nothing says so. This unit has check 15 REPORT those citations, non-gating,
through its existing notes channel. It also repairs the one dead pointer the report named in the
decision log's header, `memory/DECISIONS.md` line 5, which sends a reader to a `decisions/`
directory this repo does not have.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/corpus_ids.py` gains `read_live_readmes`, which reads `<MEMORY_ROOT>/LIVE.md`,
  resolves each markdown link target relative to that file the way `walk` already resolves its
  relative links, and returns the targets that are tracked build READMEs together with the number of
  build links it read. Observed by AC1, AC4.
- **S2** — `walk` admits a file that is not present-tense when it is one of those READMEs. Such a file
  feeds no id citation and no check 15 key; each of its path tokens, with a trailing line locator of
  the form colon-digits or colon-digits-dash-digits cut first, goes through the SAME token filters
  check 15 applies and lands in a separate `advisory` map keyed `(file, path)` with a count. Observed
  by AC1, AC2, AC3.
- **S3** — When that map is non-empty, `walk` appends one note opening `advisory check 15:` naming the
  dead-citation count, the README count holding one, and the live README count, all derived; the
  existing print path gives it the `HYGIENE ` prefix. When `LIVE.md` links a build but none of its
  links resolves to a tracked README, the note says the population is empty instead of printing
  nothing. Neither changes the exit status. Observed by AC1, AC4.
- **S4** — `cmd_report` prints the advisory count and lists each `(file, path)` with its first line,
  beside the check 15 listing it already prints. Observed by AC2.
- **S5** — `--selftest` gains one arm over a fixture holding a `LIVE.md` that links one build, whose
  README cites one dead path and one tracked path with a line locator, plus a second build absent from
  `LIVE.md` citing a dead path. It asserts `--check` exits 0 with the advisory count 1, the check 15
  map stays empty, and the unlinked build is not read; a second fixture whose `LIVE.md` links a build
  with no tracked README asserts the empty-population note. Observed by AC4.
- **S6** — `memory/DECISIONS.md` line 5's sentence pointing at the `decisions/` directory is rewritten
  to point at the build folder that minted the id, `builds/<slug>/`, and no other line of the file
  changes. DELIVERED by the main loop's records commit `37ed0d324`, because the file is a SHARED_RECORDS
  path check 49 refuses in any pass write set; this unit's pass does not write it. Observed by AC5.
- **S7** — check 15's catalogue entry in `tools/memory-tree/HYGIENE.template.md` gains one sentence
  naming the advisory population, and `memory/HYGIENE.md` is re-rendered from it. Observed by AC6.
- **S8** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Gating the advisory, or registering its citations in `memory/project/corpus-path-unresolved.txt`.
  A build README is history: of the three dead citations at base, one names a script as it stood
  before the build moved it, one names a file in another repository, and one is a kit-relative short
  form. A gate would red records that are correct about their moment.
- Repairing those three citations, which belong to their builds' own folds.
- Cutting a line locator inside check 15 itself. That is the open ask `TOOL-aProbedToolkit-17`, which
  changes a gated verdict; this unit cuts it only in the advisory population, so check 15's `dead`
  map, its registry and `DEAD_PATH_PIN` are untouched.
- The adopter's seeded header in `tools/memory-tree/adopt-memory-tree.sh`, which carries the same
  `decisions/` sentence. The charter's §6 makes a two-tier log with per-decision detail files a
  legitimate adopter layout, so for an adopter the pointer can be true; it is dead only in this repo,
  whose detail lives in build folders.
- Moving the memory-tree kit version: the build moves each kit version it owes once, after the last
  pass that touches the kit, and the `kit epoch` leg grades that move at the close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-23` — the `add_offender_keys` skip for lines opening
  `HYGIENE advisory `; without it a red hygiene run would key this unit's note as an offender.

## 4. Design

### Evidence

Read at base `7af5f564`, whose bytes for every file below equal HEAD's at `6a88fbf7`.

- `walk` in `tools/memory-tree/corpus_ids.py` builds `present` from a fixed member list under
  `MEMORY_ROOT`; its `README\.md` member anchors at the memory root, so `builds/<slug>/README.md` is
  never present-tense and `if not now: continue` skips it before any path token is read.
- `memory/LIVE.md` links 23 builds as `builds/<slug>/README.md`, relative to itself; `walk` already
  resolves that shape for check 15, per its own comment beside the relative-resolution branch.
- A scratch probe replaying `walk`'s token filters over those 23 READMEs graded 186 citations and found
  10 unresolved. Seven were tracked files cited with a line locator, which S2's cut resolves. The three
  left: the pre-move run-gates script path in `memory/builds/aPacedTurnstile/README.md`, a
  short-form drift-audit selftest path in `memory/builds/aGradedDoorway/README.md`, and an inCMS
  install index named in `memory/builds/dNarrowedAnchor/README.md`.
- `memory/DECISIONS.md` line 5 ends "Detail in `decisions/`." and `memory/decisions/` does not exist.
  `git grep` finds no reader of that header's bytes outside the adopter that seeds it.
- The hygiene shell's corpus_ids block prints the module's output at every exit status already, so S3's
  note reaches the `memory hygiene` leg without a shell change.

### Mechanism

`read_live_readmes` runs once, before the loop, and returns an empty set when `LIVE.md` is untracked,
which is an adopter that renders no index and is not asked. In the loop the admission test is one
boolean beside `now`; the id-citation block stays behind `now`; the token loop is unchanged except for
the locator cut on admitted files and the choice of sink, `dead` when `now` and `advisory` otherwise.
No filter is copied: the advisory population passes the same elision, root, relative, tail and
`DEAD_PATH_EXCLUDE` tests check 15 does. The note:

```
advisory check 15: <n> dead repo-path citation(s) in <k> of <m> live build README(s) — corpus_ids.py --report lists them
```

### Inventory

- `read_live_readmes` — cell `py.function`; `python tools/lexicon/lexicon.py --suggest` answered OK.

### Rollout

Unit 23 writes both HYGIENE documents and adds the offender-key skip this unit's note relies on, so
this unit sequences after it. `memory/DECISIONS.md` is a shared mutable record, so this pass never
runs beside another that writes it. The re-render in S7 is the parity script's `--render` mode.

### Files touched (estimate)

- `tools/memory-tree/corpus_ids.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `memory/DECISIONS.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A drift-audit signal.** It would have to re-implement check 15's token filters, because a kit file
  names nothing outside its own kit, and two copies of one predicate is the class this kit refuses.
- **Derive liveness from the build-index generator's `collect`.** It re-parses every build to answer
  what `LIVE.md`, kept fresh by check 9, already states.
- **Delete the decision-log sentence instead of repointing it.** The prior review that first named it
  proposed deletion; a correct pointer costs the same bytes and tells a reader where detail lives.

## 5. Production-readiness checklist

- security — N/A: reads tracked files already read by the walk; no new input or write path.
- perf / scale — one extra read of `LIVE.md` and up to one README per live build.
- error / empty / loading states — untracked `LIVE.md` is not asked; links resolving to nothing print
  the empty-population note; a clean live set prints nothing.
- observability — the note in `--check` and the listing in `--report`.
- risks — the hygiene leg prints one more line at exit 0; unit 23's skip keeps it out of the offender
  set. Check 15's verdict and pin cannot move, which AC3 observes.
- testing — S5's selftest arm, plus AC1, AC2, AC3 and AC5 run directly.
- migration — N/A: no conf key, no registry row, no record format change.
- user docs — S7's sentence in the hygiene catalogue.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/corpus_ids.py --check` runs on the tree, it exits as it did
  at base and prints one line opening `HYGIENE advisory check 15:` whose counts equal the advisory
  listing `python tools/memory-tree/corpus_ids.py --report` prints.
  Red when: S3 is absent, or the note changes the exit status.
  figure: DERIVED at observation time; the base probe found 3 dead in 3 of 23 live READMEs.
- **AC2** — When `python tools/memory-tree/corpus_ids.py --report` runs, its advisory listing names
  `memory/builds/aPacedTurnstile/README.md`, and names no citation of
  `tools/check-wiring.sh`, which `memory/builds/aTetheredScratch/README.md` cites with a line locator.
  Red when: the locator is not cut, so a tracked file is listed as dead.
  fixture: both READMEs are live and hold those citations at base.
- **AC3** — When `python tools/memory-tree/corpus_ids.py --measure` runs, it prints the same
  `DEAD_PATH_PIN` value as at base.
  Red when: the advisory population leaks into check 15's `dead` map.
- **AC4** — When `python tools/memory-tree/corpus_ids.py --selftest` runs, S5's arm passes; with the
  sink choice reversed as a staged break, so admitted files feed `dead`, the arm reds.
  Red when: the arm's fixture links no build, so the advisory population is empty and cannot fail.
- **AC5** — When `git diff -U0 37ed0d324~1 37ed0d324 -- memory/DECISIONS.md` runs, it shows one
  removed and one added line, both at line 5, and `sed -n 5p memory/DECISIONS.md` no longer names the
  decisions directory.
  Red when: any decision row changes, or the sentence still names that directory.
- **AC6** — When `grep -n 'advisory' memory/HYGIENE.md` runs, it prints a line inside check 15's entry,
  and the same sentence is in `tools/memory-tree/HYGIENE.template.md`.
  Red when: the rendered copy and the template disagree, which the parity leg reds at the close.

## 7. Gates

`memory hygiene` · `corpus-ids selftest` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/corpus_ids.py --selftest · S5's live-README arm, staged red by routing admitted files into the dead map · none

## 8. Open questions

- **F1 — Is the decision-log repair a second mechanism that `--rescope` should split out?** The brief's
  rule 2 asks for a split when a point is two mechanisms. S6 is a one-line text repair with no code,
  no gate and no reader; the report and the brief name it as half of one point. Recommendation: keep
  it here, because a unit of its own would carry a spec longer than its diff.
  RESOLVED (agent, 2026-10-04, delegated): keep S6 in this unit; it builds no mechanism.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#20], a replay of check 15's filters
  over the live READMEs at base, and a read of the decision log's header.
- rev-2 · 2026-10-04 · §2 S8 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.
- rev-3 · 2026-10-04 · §2 S6 and §6 AC5 point at the main loop's records commit 37ed0d324: check 49 refuses memory/DECISIONS.md, a SHARED_RECORDS path, in any pass write set.

## 10. Reuse audit

The seam is `walk` in `tools/memory-tree/corpus_ids.py`, check 15's one token walk: S2 widens its
admission and adds a sink rather than copying a filter, and `read_live_readmes` reuses the relative
resolution `walk` already applies to `LIVE.md`'s own links. The map probe
`python tools/codebase-map/reuse_lookup.py "report dead repo paths cited by live build READMEs"`
returned only name-token seams in other kits, `report` and `repo_root` first, and nothing in the
memory-tree kit; read in source, `walk` is the seam and the probe's miss is a ranking miss. The
drift-audit signal `readme_mechanism_drift` in `tools/drift-audit/drift_report.py` also walks build
READMEs, over every build rather than live ones, and owns no path resolution, so it is not reused.
Recall returned `TOOL-aDrainedSluice-9`, which settled that a frozen record's dead citations are left
alone while a live one is repaired, and `TOOL-aProbedToolkit-17`, the open line-locator ask.

Where the report and the tree disagree: the report counted 1 of 43 dead; the replay counted 3 of 186
once line locators are cut, because it harvests backticked tokens as check 15 does and the report
counted links. The report's note that decision rows are excluded on purpose holds; line 5 is header
prose, not a row.

Recall terms used: `python tools/memory-recall/query.py "why are build READMEs outside the dead path citation check, and should live ones be reported" --terms "check 15 dead repo-path citations present-tense corpus builds record of a moment LIVE README registry advisory"`
