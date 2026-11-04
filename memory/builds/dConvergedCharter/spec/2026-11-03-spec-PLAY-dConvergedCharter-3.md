# PLAY-dConvergedCharter-3 — records merged by evidence: two kinds the registry and the commit history call one become one, the other name an alias shipped as an upgrade step

**Status:** DEFERRED · rev-2 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 11 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0477@47475290 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-19 |
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 PLAY-dConvergedCharter-41 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

Records dominate the work: 1,598 of 2,827 commits in 30 days touched only `memory/` (gap-maint-04). The owner's
answer to CV3 was "Merge by evidence", and no design source states the evidence (scout A row 3). This unit states
it as a rule over the registry's own columns and the commit history, measures every pair of registered kinds
against it, reds a pair the rule calls one while both rows stand, and merges such a pair by the rename-plus-alias
precedent (TOOL-dTotalRecall-18 S7), the alias shipped to adopters as an upgrade step (TOOL-dTotalRecall-20 S1).

## 2. Scope (IN)

Build-run preconditions, each specced and DEFERRED at base `0d1c1dda`: TOOL-dTotalRecall-1 (the registry and
`check_record_kinds`), TOOL-dTotalRecall-18 (the `home`, `readers` and `lifecycle` columns, `KIND_ALIASES` and
`canonical_kind`), TOOL-dTotalRecall-20 S1 (the alias step `memory-tree/serves-journal-read-as-log` and its
program `tools/govkit/steps/memory_journal_alias.py`), TOOL-dTotalRecall-24 (the record events of the change
feed), and this build's PLAY-dConvergedCharter-6 (every tracked record home on a row) and
PLAY-dConvergedCharter-11 (`derive_readers`).

- **S1** — The rule. `derive_merge_pairs(root, rows, since)` in `tools/memory-tree/record_kinds.py` returns each
  unordered pair of rows that is one kind by evidence: equal `writer`, equal `lifecycle`, equal `readers` as a
  set, equal `schema.form`, and a commit share of at least `MERGE_SHARE_FLOOR = 0.9` over at least
  `MERGE_COMMIT_FLOOR = 20` commits touching the less-written kind, in the window of 30 days ending at the
  commit measured. The window is anchored on that commit and never on the wall clock:
  `derive_window_since(root, at)` returns the committer date of `at` less 30 days, `at` being the commit
  graded (HEAD, or a branch's merge-base with its base where the leg grades a branch), and every caller
  passes `since` and `at` explicitly, so the verdict at a fixed commit is the same on every run date.
  Every condition is necessary; §8 F1 states why the share alone is not. Observed by AC1, AC2 and AC7.
- **S2** — The measurement. `measure_commit_share(root, rows, since, at)` walks `git log <at> --no-merges
  --no-renames --name-only --since=<since>` over the memory root once, the walk TOOL-dTotalRecall-24 S3's appender takes,
  and gives each commit the set of kinds whose `home` admits a path it touches, through the home predicate
  PLAY-dConvergedCharter-6 S1 calls. The share of a pair is the commits touching both over the commits touching
  the less-written one. `python record_kinds.py --merge-evidence` prints one line per pair whose four columns
  agree, `merge-evidence: <a> <b> · share <s> over <n> · one|apart`, and a count line. Observed by AC3.
- **S3** — The arm. `check_merge_evidence(root, at)`, called by `check_record_kinds` on the leg
  `record-kinds` with `at` the commit it grades and `since` from `derive_window_since`, reds each pair
  `derive_merge_pairs` returns while both rows stand:
  `record-kinds: <a> and <b> are one kind by evidence, both rows standing`. The leg carries no path
  guard (TOOL-dTotalRecall-1's row), so no guarded or cached run keeps a verdict a later memory-root
  commit moved; were a guard ever added, it would have to admit every memory-root commit. Observed by
  AC1 and AC7.
- **S4** — A merge. For each pair S1 returns at the build run's tip, the kind with fewer tracked records
  (the earlier registry row on a tie) becomes the other's alias: `KIND_ALIASES` (TOOL-dTotalRecall-18 S7) gains
  `"<loser>": "<winner>"`, every writer of the loser's token writes the winner's, every reader comparing the
  value compares `canonical_kind(...)`, records already written keep their bytes, and the loser's row leaves
  `tools/memory-tree/record-kinds.toml`. Each merge's own readers are listed in its pass's commit from
  `derive_readers(repo, <loser>, "value")` (PLAY-dConvergedCharter-11 S6, I1). Observed by AC4.
  **Readers:** by name: the names of record kinds are spelled by `RECORD_KIND_TOKENS` in
  `tools/memory-tree/tree_lib.py`, by `tools/memory-tree/gen_build_index.py`, by the Serves-kind ledger arm of
  `tools/memory-tree/check-memory-hygiene.sh` and by `memory/HYGIENE.md`'s closed kind list · by value:
  `read_bindings`' kind classification (`tools/memory-tree/tree_lib.py:471`) and the acceptance-ledger set of
  check 23 in `check-memory-hygiene.sh`, each re-pointed through `canonical_kind`.
- **S5** — The alias step. The landed program of TOOL-dTotalRecall-20 S1,
  `tools/govkit/steps/memory_journal_alias.py`, is never edited: `check_frozen`
  (`tools/govkit/upgrade_steps.py:1038-1041`) reds any byte change to a landed step's program, argv kept
  or not. The pair-taking program ships as a new file, `tools/govkit/steps/record_kind_alias.py
  up|down|witness <target> <old> <new>`, both words required, its body the journal program's with the
  pair as arguments; each merge adds an `[[upgrade]]` row `memory-tree/serves-<loser>-read-as-<winner>` to
  `tools/memory-tree/kit.toml`, `surfaces = ["serves-kind:<loser>"]`, `resume = "atomic"`, its `up`,
  `down` and `witness` the new program with the pair. The journal row and its program keep their bytes.
  Observed by AC5.
- **S6** — The docs. `tools/memory-tree/README.md`'s registry section names the rule, its two floors, the
  `--merge-evidence` table and the alias step. Observed by AC6.

## 3. Non-goals (OUT)

- Registering kinds, and the residue of the memory tree's homes: PLAY-dConvergedCharter-6.
- Rewriting any written record: a merged kind's records keep their bytes and read as the winner through
  `canonical_kind`, exactly as `journal` reads as `log`.
- Merging two records of one kind, or two documents: the clause is about kinds, and gap-maint-04 counts
  commits, not files.
- A policy key for the floors: no clause names one (§8 F2).
- Kinds outside the tree, the `witness` rows of TOOL-dTotalRecall-18 S6: they hold no tracked path, so no commit
  touches them and S1 cannot measure them.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-6` — `record_kinds.py`, the registry with every tracked record home on a row, without which a kind's commits are uncounted and S2's share is false
- **consumes-from** `PLAY-dConvergedCharter-11` — `derive_readers`, the by-value inventory each merge's pass lists its readers through
- **consumes-from** external — TOOL-dTotalRecall-1, -18, -20 and -24, each specced and DEFERRED at base and landed in an ancestor before the build run

## 4. Design

### Evidence

- No design source states the rule: v2:1785 carries the clause's five words, the walkthrough records only the
  owner's CV3 pick (`2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md:816-818`), and
  research-observability-b leaves gap-maint-04 to this build. So §8 F1 settles it.
- The registry rows carry `writer`, `readers`, `lifecycle` and `schema.form` (TOOL-dTotalRecall-1 §4,
  TOOL-dTotalRecall-18 S1-S2): what writes a kind, who reads it, how it lives and how it is graded.
- TOOL-dTotalRecall-24's feed lines carry `blob` and `commit` and no path (TOOL-dPlacedRequest-13 S1), so a
  record event cannot be assigned a kind without its commit's paths. S2 walks the history the appender walks
  rather than reading the feed.
- The probe of §8 F1, run at base over the 3,334 non-merge commits touching `memory/` between 2026-10-04 and
  2026-11-03, grouping paths by home: `memory/builds/*/README.md` co-commits with `spec/` in 1,801 of 1,847
  commits (0.98), with `reviews/` in 273 of 276 (0.99) and with `memory/LIVE.md` in 871 of 904 (0.96). Those
  are generated regions re-rendered beside every record, not one record written twice.

### Data flow

```
record_kinds.py --check
  check_record_kinds ─ check_record_homes (unit 6) ─ check_merge_evidence
      derive_merge_pairs(rows) ─ four equal columns? ─ measure_commit_share ─ share >= 0.9 over >= 20?
                                                                           └ yes, both rows standing ─▶ red
record_kinds.py --merge-evidence ─ the table, every pair with four equal columns
```

### Migration

Per merge: `KIND_ALIASES` entry, writers re-pointed, the loser's row out of the registry, the `[[upgrade]]` row of
S5. An adopter's records keep their bytes; the step's witness reads every bound record of the old kind as the new
one through gov's `read_bindings`, as the journal step does.

### Inventory

Minted, each asked of `lexicon.py --suggest <name> --as py.function` at base and answered OK:
`derive_merge_pairs`, `measure_commit_share`, `check_merge_evidence`, `derive_window_since`. The step program
`record_kind_alias.py`. The constants `MERGE_SHARE_FLOOR` and
`MERGE_COMMIT_FLOOR`, the flags `--merge-evidence` and `--at <sha>` of `record_kinds.py`, and the step id grammar
`memory-tree/serves-<loser>-read-as-<winner>`.

### Files touched (estimate)

- `tools/memory-tree/record_kinds.py`: S1, S2, S3
- `tools/memory-tree/record-kinds.toml`, `tools/memory-tree/tree_lib.py`: S4, per merge
- each writer of a merged kind's token: S4, per merge, named in its pass from `derive_readers`
- `tools/govkit/steps/record_kind_alias.py` (new): S5; `tools/govkit/steps/memory_journal_alias.py` is
  not touched
- `tools/memory-tree/kit.toml`: S5, per merge
- `tools/memory-tree/README.md`: S6

### Alternatives rejected

- **The commit share alone.** Rejected by the probe of §4 "Evidence": generated regions put the build README at
  0.96 to 0.99 with three other homes, so the share alone would merge a build's index with its specs.
- **The four columns alone.** Two kinds one tool writes and the same roles read, each in its own act, would
  merge with no sign they are written together; `spec-audit` and `diff-review` share a writer and a form.
- **One record per stage**, the CV3 option the owner did not pick.
- **A merge that rewrites old records to the winner's token.** It moves bytes of frozen records and every
  generated records region beside them; the alias reads them unchanged.

## 5. Production-readiness checklist

- security — read-only measurement; a merge edits registry rows and writers the pass names, no new surface.
- perf / scale — one `git log` over 30 days of the memory root (3,334 commits at base) per `--check`.
- error / empty / loading states — a window with no commit prints `merge-evidence: no commit since <date>` and
  judges no pair apart; a pair under the commit floor prints `apart` with its count.
- observability — the `--merge-evidence` table prints every measured share, so the floors can be judged.
- risks — the floors are PINNED by judgment (§8 F2); the table makes a wrong floor visible.
- testing — AC1 to AC5, and the arm of §7.
- migration — S5, per merge.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When `python record_kinds.py --check` runs in a fixture registry with two planted rows of equal
  `writer`, `lifecycle`, `readers` and form, whose homes 25 fixture commits each touch together, it exits 1
  printing `are one kind by evidence, both rows standing` and both names.
  Red when: the planted pair is left unmerged and the arm is silent, the clause's seen-red case.
  fixture: a scratch repository under `%TEMP%/<short>`, its commits made by the fixture.
- **AC2** — When `python record_kinds.py --check` runs on the same fixture with the pair's writers made
  different, and again with only 19 shared commits, it exits 0 and `--merge-evidence` prints the pair `apart`.
  Red when: a pair failing one condition is called one.
- **AC3** — When `python record_kinds.py --merge-evidence` runs over the build run's tip, it prints a count line
  naming the pairs whose four columns agree and each pair's share and commit count.
  Red when: the table omits a pair whose columns agree, or prints a share above 1.
  figure: DERIVED at observation.
- **AC4** — When the fixture merges its planted pair, `--check` exits 0, `canonical_kind("<loser>")` returns the
  winner, a planted record of the loser's kind written before the merge keeps its bytes, and
  `read_bindings` classifies it as the winner.
  Red when: the merge rewrites the old record, or the loser's row still stands.
- **AC5** — When `python record_kind_alias.py witness <target> <old> <new>` runs on a fixture target holding
  records of `<old>`, it reads `<old>` as `<new>`; `git diff --quiet <base> -- memory_journal_alias.py`
  run in `tools/govkit/steps/` exits 0 at the unit's tip, and `python upgrade_steps.py` over the tree reports
  no frozen program moved.
  Red when: the landed journal program changes by a byte, or the pair is ignored.
- **AC6** — When `grep -n "merge-evidence" README.md` runs in `tools/memory-tree/`, the registry section names
  the rule's two floors and the flag.
  Red when: the README is silent on the rule.
- **AC7** — When `python record_kinds.py --merge-evidence --at <tip>` runs over AC1's fixture rebuilt with
  every commit's author and committer date set in 2020, it prints the planted pair `one` over its 25
  commits, as it does over the fixture dated today.
  Red when: the window is read from the wall clock, so a history older than 30 days before the run reads
  `no commit since` and a fixed commit's verdict moves with the run date.
## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `step-rows-frozen` · `upgrade-walk`

New arm: tools/memory-tree/record_kinds.py · covers AC1 AC2 AC4 · the `--selftest` merge plants, its failing case the planted pair left unmerged with the arm cut · none

New arm: tools/govkit/selftest.py · covers AC5 · the new alias program with a pair beside the untouched journal program, its failing case a pair ignored · none
New arm: tools/memory-tree/record_kinds.py · covers AC7 · the `--selftest` window plant over a 2020-dated fixture history, its failing case `since` read from the wall clock · none

## 8. Open questions

- **FACT-QUESTION · F1 — What evidence calls two kinds one?** Probe: the co-commit share of each pair of
  record homes over the 30 days before base (§4 "Evidence"), deciding whether the share alone separates kinds
  written together from kinds re-rendered together. Liveness: the probe can print a share under 0.9, and does:
  `memory/ledger/` with `memory/LIVE.md` reads 119 of 133 (0.89). Observation: the share alone calls the build README
  one with `spec/`, `reviews/` and `LIVE.md`, each a generated region, so it cannot stand alone; the four
  registry columns separate them, the README's writer being `gen_build_index.py --new-build` and a spec's
  `--new-spec`. Options: (a) the four columns and the share; (b) the share alone; (c) the columns alone; (d) the
  owner rules each pair. (b) fails by the probe; (c) merges kinds never written together; (d) leaves every pair a
  fork. RESOLVED (agent, 2026-11-03, delegated): (a), rung 2. widens: none · relaxes: none
- **F2 — Where do the floors live, and at what values?** (a) Constants in `record_kinds.py`, PINNED at 0.9 and
  20 with their reason, every measured share printed; (b) policy keys. (b) adds two public surfaces no clause
  names (veto 2 outside the grant). Under (a), 20 commits is the count below which one sprint's co-edits read
  as a kind, and 0.9 admits a pair written apart once in ten. Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F3 — Which name survives a merge?** (a) The kind with more tracked records, the earlier row on a tie;
  (b) the earlier row always. (a) aliases the fewer records, so fewer readers meet the old token. Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F4 — The ask this unit needs filed.** RESOLVED (agent, 2026-11-03, delegated): file A1. widens: none · relaxes: none
  Ask A1 for dTotalRecall, target build dTotalRecall: "TOOL-dTotalRecall-20 S1's program
  `memory_journal_alias.py` takes its alias pair from two optional argv words, defaulting to `journal log`, so
  a later kind merge ships its step through the same program"; accept: the journal step's `up`, `down` and
  `witness` keep their output with no pair given, and a fixture pair reads its old kind as the new one.

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the spec brief's unit row, scout A's row 3 and the co-commit probe
  of §8 F1.
- rev-2 · 2026-11-04 · S1 S2 S3 S4 S5 §4 AC5 AC7 §7 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1` findings 14 (the pair-taking alias program is a
  new file and the landed program keeps its bytes, `step-rows-frozen` and `upgrade-walk` named), 54 (the
  window anchored on the graded commit's date, `derive_window_since`, and the leg unguarded) and 18
  (`derive_readers` cited at PLAY-dConvergedCharter-11 S6).

## 10. Reuse audit

The seams extended: the registry's `check_record_kinds` (TOOL-dTotalRecall-1 S3), the rename-plus-alias
precedent of TOOL-dTotalRecall-18 S7 (`KIND_ALIASES`, `canonical_kind`), and TOOL-dTotalRecall-20 S1's alias
step program, which S5 makes the factory of every later alias step at its second instance.
`python tools/codebase-map/reuse_lookup.py "decide whether two record kinds are one by their writers readers and
commits"` ranked name stems only (`read_text`, `read`, `records` in `tools/memory-tree/gotchas.py`); scout A's
probe surfaced `merge` in `tools/memory-tree/merge-rows.py`, a git merge driver for conflicting rows that judges
no kind. No existing callable measures a kind pair, so no existing seam fits beyond the specced registry.
Where a record and source disagreed: the brief names the change feed as the commit-share source, and its lines
carry no path (TOOL-dPlacedRequest-13 S1), so S2 walks the history the feed's appender walks.

Recall terms used: `python tools/memory-recall/query.py "what evidence decides that two record kinds should be merged into one" --terms "merge record kinds evidence commit share writer readers lifecycle alias rename journal log upgrade step"`
— its hits were scout A's row, the brief and TOOL-dTotalRecall-18's rename section; none states a rule.
