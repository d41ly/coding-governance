# TOOL-dFairHearing-12 — the scorer factory: one replay scorer, with aScoutedSeam's grader as its second instance

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 13 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0079@d8e61ab6 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

The repository scores experiments twice: `tools/workflows/review_replay.py` scores a review for
recall, and aScoutedSeam's `bench.py` grades reuse-scout arms, and neither knows the other
(`gap-test-18`). This unit extracts one deterministic scorer, `tools/workflows/replay_scorer.py`,
that re-derives every figure from committed raw outputs, pairs the cases every variant answered and
refuses a partial population. `review_replay.py`'s scoring core is its first instance and
aScoutedSeam's grader, taken by blob from commit `b0fe68f30`, its second. A factory test refuses
when only `review_replay.py`'s instance is present, and a conformance arm reds on a second scorer:
code outside the factory that pairs variants with cases (night pass two, point 2).

## 2. Scope (IN)

- **S1** — `tools/workflows/replay_scorer.py`, the factory. It holds `read_raw_output(src, repo)`,
  which reads a working-tree path, or a `<commit>:<path>` or bare 40-hex blob through one
  `git cat-file blob` call, and skips leading `//` lines as `bench.py`'s `read_json` does
  (`memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-4-bench.py:56-61`). An
  object git cannot read is a refusal naming it, never an empty arm. It holds
  `derive_paired_cases(case_ids, answers)`, the ONE place variants are paired with cases: it returns
  the ids every variant answered, in case order, and each variant's unanswered ids. It refuses an
  answer naming a case outside the population, a variant that answered nothing, and an empty pairing.
  It holds the `INSTANCES` table, keyed `review-replay` and `scouted-seam`, and one CLI,
  `replay_scorer.py --instance <key> …`. Observed by AC1, AC5 and AC8.
- **S2** — The `review-replay` instance. `review_replay.py`'s scoring core moves into the factory
  unedited: `extract_line_ref`, `extract_section_ref`, `read_record_kind`, `extract_subject_pins`,
  `extract_range`, `extract_stated_count`, `parse_appendix_rows`, `parse_record_findings`,
  `parse_candidates`, `check_same_file`, `measure_recall` and `measure_replay`
  (`tools/workflows/review_replay.py:87-305`), with the constants they read
  (`tools/workflows/review_replay.py:64-81`). `review_replay.py` keeps its CLI, `print_score`, the
  corpus listing and its 25 arms (`tools/workflows/review_replay.py:308-655`), importing the moved
  names, so the clause's `review_replay.py` stays the entry its callers run. Its scored output is
  byte-identical. Observed by AC3.
- **S3** — The address reading the shared key S4 agrees with. `extract_tag_ref(text)` returns
  `(path, key)` for a spec ref `<file>:<where>`: `key` is the FIRST `[tag]`, a lower-case slug in
  brackets, anywhere in `<where>`, as `TOOL-dFairHearing-4`'s `deriveAddressKey` reads the spec kind;
  failing one, it is the section `extract_section_ref` gives. It folds paths as that reader does. The
  `review-replay` instance's spec mode reads every known and candidate ref through it. A `[tag]` key
  is a string, so `measure_recall` at window 0 compares sections by equality and never by
  subtraction. Observed by AC4.
- **S4** — The `scouted-seam` instance. `check_hit`, `check_case` and their three token helpers
  (`bench.py:318-362`), and the `grade`, `compare` and `judged` readings (`bench.py:365-398`,
  `bench.py:630-660`), are ported from the grader blob `a03896116e3c5cbf853affda241c22d8408cb945` at
  `b0fe68f30`. The two comprehensions that pair arms with cases (`bench.py:384` and `bench.py:647`)
  become calls to `derive_paired_cases`. A result row without a `seams` list, or a judged cell
  without `primary` and `covered`, is a refusal naming the arm and the case. It is proven over the
  committed results, which need no corpus of case trees: the cases blob
  `921345a50b49d8fb87687b3e411611d1d0b8e740`, the results blob
  `c7ad6854565225c7190d1e284c70f53627bd11cc`, and the judge's verdicts inside it, all read at
  `b0fe68f30`. Observed by AC2 and AC7.
- **S5** — The factory's arms, run by the existing `review-replay selftest` leg:
  `review_replay.py`'s `run_selftest` runs its own 25 arms, then `replay_scorer.run_selftest`, and
  reports both counts against two declared totals. The factory's arms include `check_instances`, the
  factory test, red when the table holds fewer than both instances, and the S4 proof. Observed by
  AC5 and AC2.
- **S6** — The conformance arm, `scan_pairing_sites(root)`: an `ast` walk over every tracked `*.py`
  under the tool root the factory sits in, the factory itself excepted. It names each comprehension
  whose filter calls `all()` over a generator ranging over a second population, where that
  generator's element is an `in` membership test whose left side names the outer case and whose right
  side names the inner variant, or an `is not None` test naming both. One hit is a red naming file and
  line. Observed by AC6.

## 3. Non-goals (OUT)

- Editing any record under `memory/builds/aScoutedSeam/` or any instrument under
  `memory/builds/dClosedLoop/build/`. Both are frozen records; the conformance arm's population is
  product code (§8 F2), and the grader is read by blob.
- The retrieval benches `tools/memory-recall/bench.py`, `tools/memory-recall/union.py`,
  `tools/memory-recall/check-recall.py` and `tools/codebase-map/rank_harness.py`. Each scores a live
  ranking per query and pairs no answered-case population of committed outputs; the predicate reads
  them clean (§4 Evidence).
- The experiment method's rules (held-out set, one variable per arm, parsed counts, blind judge,
  union): `TOOL-dFairHearing-14`, in this module.
- The known-set file and its reader: `TOOL-dFairHearing-1` owns S11.
- Porting `bench.py`'s tree, collection, cost or judge-packet verbs. They build inputs and spawn
  agents; the factory reads committed outputs and runs no agent.
- A new gate leg. The factory's arms run inside `review-replay selftest` (§8 F3).

### Edges

- **consumes-from** `TOOL-dFairHearing-4` — `deriveAddressKey`'s spec-kind reading (first `[tag]`, else the leftmost section token), which S3's reading agrees with on the tag and the `§<n>` forms
- **hands-off** `TOOL-dFairHearing-14` — the factory module and `derive_paired_cases`, which its method rules extend in place, never in a second module
- **hands-off** `TOOL-dFairHearing-1` — the `review-replay` instance and the `[tag]` reading, which its known-set reader and adjudicated matches extend, and the factory its replays score through
- **hands-off** `TOOL-dFairHearing-15` — `derive_paired_cases`, through which its with-and-without replay pairs its two arms
- **hands-off** `TOOL-dFairHearing-18` — the `[tag]` address reading and the factory its walk's recall scores through

## 4. Design

### Evidence

Measured 2026-10-23 at `3dca04036`, PINNED.

- `git rev-parse b0fe68f30:<results>` resolves `2026-10-11-build-TOOL-aScoutedSeam-1-5-results.json` to
  blob `c7ad6854…`, so the results are present at `b0fe68f30`; the scout's reading that they are
  absent disagrees with source. `git log` of that path names `5f8ef021d` as its last writer (blob
  `219cf9a2…`, the system on both sets), an ancestor of `a60b0c7dc`, the night pass two's
  `origin/main`, and of this build's base. The cases, grader and judge script blobs are equal at
  `b0fe68f30` and at HEAD.
- `bench.py grade` over the `b0fe68f30` blobs prints `# m1b: positives 15 solved 10 · items 17/40 ·
  controls 4 decoy MUSTs 0 · graded 19 of 30`, the benchmark record's M1b row. `bench.py compare … m1b
  m1b@medium` prints `# common 19 (15 positive)`, `m1b solved 10/15 · items 17/40 · … MUST 97` and
  `m1b@medium solved 9/15 · items 17/40 · … MUST 114`, the record's paired row (10 → 9, 17 → 17,
  97 → 114). `bench.py judged … m1cA@medium` prints `# judged common 30 (24 positive)` and `primary
  17/24 · items 39/59`.
- The S6 predicate, run over every tracked `*.py` (150 files) before writing this spec, named two
  sites, both in aScoutedSeam's `bench.py`, at :384 and :647, and none under `tools/` (98 files).
  A looser first cut, any `all()` filter over a second iterable, also named
  `tools/drift-audit/drift_report.py:2040`, `tools/govkit/govkit.py:937`,
  `tools/govkit/selftest.py:8196` and `tools/run-gates/measure_legs.py:3582`, none of which pairs a
  variant with a case; the membership-shape requirement is what drops them.

### The factory

```
replay_scorer.py --instance scouted-seam --cases <src> --results <src> --grade <arm>
replay_scorer.py --instance scouted-seam --cases <src> --results <src> --compare <arm> <arm> [...]
replay_scorer.py --instance scouted-seam --cases <src> --results <src> --judged <arm|a+b> [...]
replay_scorer.py --instance review-replay --known <src> --candidate <src> [--window N]
replay_scorer.py --selftest
```

`<src>` is a path, `<commit>:<path>`, or a 40-hex blob. Every population arrives as an argument; the
module names no path outside its kit, as `review_replay.py` promises (`review_replay.py:4`). Exit 0
on a scored run, 1 on a red self-test, 2 on any refusal, the codes `review_replay.py` already uses.

Each figure line names its population first: `paired <n> of <N> · <variant> unanswered <ids>`, then
the scores. Output iterates the case file's order and the argument order of the variants, never a
set, so two runs over the same bytes print the same bytes.

`INSTANCES` maps each key to a plain dict of its readers and its measure function. Two entries, no
registry class: the second instance is the factory's reason to exist, and a third adds a row.

### What the `[tag]` reading moves

Of the 36 spec-audit records under `memory/builds/*/reviews/` carrying an appendix, the design-record
audits address findings by `[tag]` (994 appendix rows carry a lower-case bracketed slug, measured
2026-10-23). Today those refs fall to the item mapping or read as unscorable; after S3 they score by
tag. That is the change S3 exists for, and it moves those records' replay scores. A unit-spec audit
whose refs carry no `[tag]` scores exactly as before, which is why AC3 replays one.

### Why `review_replay.py` stays

The clause's own token is `review_replay.py`, and units 1 and 18 and the kit README
(`tools/workflows/README.md:477-534`) call it by that name. It becomes the `review-replay`
instance's thin adapter: argument parsing, `print_score`, `scan_corpus`, `resolve_commits`,
`print_corpus` and its arms. The adapter imports the moved names, so its 25 arms keep their bodies.

### The arms

`replay_scorer.run_selftest` declares its own `ARMS_DECLARED`, as `review_replay.py:84` does, and
`review_replay.py --selftest` exits 0 only when both runners reach their declared totals. The
factory's arms:

- `paired-refuses` — an empty pairing, an answer outside the population and a silent variant each
  refuse, by name.
- `row-refuses` — a result row without `seams` refuses naming the arm and the case.
- `tag-section` — the S3 readings of AC4.
- `instances` — `check_instances()` returns None with both entries and names the missing key when
  the table lacks one.
- `scouted-proof` — the S4 figures of AC2, read through `read_raw_output` at `b0fe68f30`. Where the
  tree holds `memory/builds/aScoutedSeam/`, a missing blob is red. Where it does not, the arm prints
  `SKIP scouted-proof: no aScoutedSeam records in this tree` and the count line names one arm
  skipped, so an install outside gov never reads that skip as a pass.
- `conformance` — S6 over the live tool root returns nothing; over the grader blob it names :384
  and :647; over a scratch module holding one pairing comprehension it names that file and line.
- `deterministic` — two runs of one compare print the same bytes.

What the arms do not check. The conformance walk reads Python only, so a JavaScript harness that
pairs variants is not seen, and it reads the comprehension shape, so a pairing written as a `for`
loop that builds a common list is not seen either. The proof pins figures of one past experiment;
it cannot show a future instance grades its own corpus correctly.

### Inventory

| Identifier | Kind | Lexicon verb |
|---|---|---|
| `tools/workflows/replay_scorer.py` | module | — |
| `read_raw_output` | function | read |
| `extract_tag_ref` | function | extract |
| `derive_paired_cases` | function | derive |
| `check_instances` | function | check |
| `scan_pairing_sites` | function | scan |
| `measure_scouted_grade`, `measure_scouted_compare`, `measure_scouted_judged` | functions | measure |
| `INSTANCES`, `ARMS_DECLARED` | constants | — |

The moved names keep their names; the ported `check_hit`, `check_case`, `derive_path_key`,
`extract_code_tokens` and `check_path_match` keep theirs.

### Files touched (estimate)

- `tools/workflows/replay_scorer.py`
- `tools/workflows/review_replay.py`
- `tools/workflows/README.md`

### Rollout

The kit README's `review_replay.py` section (`tools/workflows/README.md:477`) gains a paragraph
naming the factory and its two instances. The kit's version line moves with `tier2-review`'s edits
in the build run; this unit changes no rendered file.

### Alternatives rejected

- **A new leg for the factory's arms.** A new leg trips the meta-gates a new leg owes
  (`memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`), and a check inside an existing
  leg costs none of them.
- **The arms inside `review_replay.py`'s own runner.** Its fixtures promise no file or git access
  (`review_replay.py:395`), and the proof reads git blobs; the factory keeps its own runner.
- **Keeping the grader in place and calling it.** `bench.py` is a frozen record whose `main` reads
  `argv[1]` as its verb and prints; importing it couples the factory to a record nobody may edit.

## 5. Production-readiness checklist

- security — no new write path. `read_raw_output` runs one `git cat-file` with argv, never a shell,
  and refuses a source opening `-`.
- perf / scale — the results blob is 2.9 MB; one read and an in-memory grade, seconds.
- error / empty / loading states — every unreadable source, unparseable row, foreign case id and
  empty pairing is a named refusal at exit 2, never a zero.
- observability — each figure line names its paired population and each variant's unanswered ids.
- risks — moving the core can change a parser silently; AC3 holds the adapter's output byte-equal.
- testing — AC1 to AC8 as probes; the arms run in `review-replay selftest`, seen red at the close.
- migration — none: the adapter's CLI and output are unchanged.
- user docs — the kit README section; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python tools/workflows/replay_scorer.py --instance scouted-seam --cases
  b0fe68f30:memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-3-cases.json`
  runs `--grade m1b` over a scratch copy of the results whose `m1b` row for one case lacks `seams`,
  it exits 2 naming `m1b` and that case; and a `--compare` of two arms with no case in common exits 2
  naming the empty pairing.
  Red when: the reader skips the row and prints `graded 18 of 30` at exit 0.
- **AC2** — When the factory runs `--grade m1b`, `--compare m1b m1b@medium` and `--judged
  m1cA@medium` over the cases and results read at `b0fe68f30`, each figure equals what the grader
  blob `a03896116e3c5cbf853affda241c22d8408cb945`, run from scratch over the same blobs in the same
  probe, prints: `positives 15 solved 10`, `items 17/40`, `graded 19 of 30`; `common 19 (15
  positive)`, `solved 10/15` against `9/15`, `MUST 97` against `114`; `judged common 30 (24
  positive)`, `primary 17/24`, `items 39/59`.
  Red when: the port drops the decoy rule or the symbol-token rule of `check_hit`, so one figure moves.
  figure: DERIVED, the grader's own output in the same probe; the literals are PINNED at `b0fe68f30`.
- **AC3** — When `python tools/workflows/review_replay.py --known <r> --candidate <r>` runs for `<r>`
  each of `memory/builds/dUnstuckLanding/reviews/2026-10-04-review-TOOL-dUnstuckLanding-13-implementation-diff-round1.md`
  and `memory/builds/aEvidencedLens/reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md`,
  and `--corpus memory/builds` runs once, each stdout is byte-identical to the same command run on
  the base copy of `review_replay.py`, read by `git show` at `3708a705` and placed in scratch.
  Red when: a moved parser changes one line of output.
- **AC4** — When a probe calls `replay_scorer.extract_tag_ref` on
  `x.md:[supervise] Relaunch, [spawn] first bullet`, `x.md:§2 [act]`, `x.md:§2 S5` and
  `x.md:status header`, it returns `("x.md", "[supervise]")`, `("x.md", "[act]")`, `("x.md", 2)` and
  `None`; and `measure_recall` at window 0 over a known item at `[supervise]` and candidates at
  `[supervise]` and `[spawn]` matches the first only and raises nothing.
  Red when: the `§<n>` token wins over a later `[tag]`, or a tag string reaches the line subtraction
  and raises `TypeError`.
- **AC5** — When a probe imports `replay_scorer`, `check_instances()` returns None; after it deletes
  `INSTANCES["scouted-seam"]` in the same process, it returns a refusal naming `scouted-seam`.
  Red when: the check asks only that some instance exists, so `review_replay.py`'s alone passes.
- **AC6** — When a probe calls `replay_scorer.scan_pairing_sites` over the tool root it returns no
  site; over the grader blob read into scratch it names lines 384 and 647; over a scratch copy of
  `tools/` holding one more module whose function returns
  `[c for c in cases if all(c["id"] in rows for rows in arms.values())]` it names that module and
  line, and the factory's own `derive_paired_cases` is never named.
  Red when: the walk reads one directory or one spelling, so the planted module passes.
- **AC7** — When the probe runs AC2's `--compare` twice, the two stdouts are byte-identical, and a
  probe calling `replay_scorer.run_selftest()` sees its count line name `ARMS_DECLARED`.
  Red when: a figure line iterates a set, so variant order moves between runs.
- **AC8** — When `--results 0000000000000000000000000000000000000000` or
  `--results b0fe68f30:no-such-file.json` is passed, the factory exits 2 naming the object.
  Red when: an unreadable source reads as an empty arm and grades zero cases at exit 0.

## 7. Gates

`review-replay selftest` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/replay_scorer.py (its runner, called from `review_replay.py --selftest` in the `review-replay selftest` leg) · covers AC1 AC2 AC4 AC5 AC6 AC7 AC8 · the base tree, where no factory exists; then a staged deletion of the `scouted-seam` entry, and a planted pairing module under the tool root · none

The four `{prefix}/workflows/` legs are owed by the guard join on the Files-touched paths; the
lexicon leg grades the new function names.

## 8. Open questions

- **FACT-QUESTION · F1 — Which commit pins aScoutedSeam's later results?** Probe: `git rev-parse
  b0fe68f30:<results path>` and `git log --format=%h -- <results path>`. Observation: the results
  exist at `b0fe68f30` as blob `c7ad6854…`; the later results the night pass two cites land at
  `5f8ef021d` as blob `219cf9a2…`, an ancestor of `a60b0c7dc` and of base. Liveness: the same
  rev-parse of the held-out file at `b0fe68f30` exits 128, so the probe can read a path as absent.
  RESOLVED (agent, 2026-10-23, delegated): the grader, cases, results and judge are read by blob at
  `b0fe68f30` as the clause says, and `5f8ef021d` is the later results' pin, which
  `TOOL-dFairHearing-14`'s proof reads; nothing waits on a merge. Rung 2. widens: none · relaxes: none
- **FACT-QUESTION · F2 — Which population does the conformance arm scan, given `B/…-score.py`,
  `tools/codebase-map/rank_harness.py` and `tools/memory-recall/bench.py` also pair or score?** Probe:
  the S6 predicate over every tracked `*.py`. Observation: two sites, both in aScoutedSeam's frozen
  `bench.py`; none in the three named files or anywhere under `tools/`. Liveness: the grader blob is
  a real positive. RESOLVED (agent, 2026-10-23, delegated): tracked `*.py` under the tool root, the
  factory excepted; records under `memory/builds/` are frozen (the packet's Non-goals) and serve as
  the liveness fixture. Rung 2. widens: none · relaxes: none
- **F3 — Where do the factory's arms run?** (a) A new `replay-scorer selftest` leg. (b) Called from
  `review_replay.py --selftest`, inside the existing leg. (c) Inside `review_replay.py`'s own runner.
  (c) breaks that runner's no-git promise. (a) and (b) both survive every veto; (b) owes no new leg
  and no meta-gate (§4 Alternatives). Recommendation (b). Rung 3. RESOLVED (agent, 2026-10-23,
  delegated): (b). The factory's runner is `replay_scorer.run_selftest`, so an arm a later unit adds
  to "the factory's self-test" lands in that runner and is reached through the `review-replay
  selftest` leg; `TOOL-dFairHearing-18`'s §7, which calls it a leg this unit adds, reads it that way.
  widens: none · relaxes: none
- **F4 — Which unit builds the `[tag]` address reading?** Clause `cl-dClosedLoop-0085` names "the
  replay scorer reading `[tag]` addresses", and `TOOL-dFairHearing-18` builds at order 18, after
  `TOOL-dFairHearing-1` (order 15) scores `[tag]`-addressed design findings. (a) This unit, as S10's
  reading, under the name and contract `TOOL-dFairHearing-18`'s spec spells, `extract_tag_ref(text)`.
  (b) Unit 18, which leaves unit 1 unable to score (veto 1, M2's ordering axis). RESOLVED (agent,
  2026-10-23, delegated): (a); unit 18's builder finds `extract_tag_ref` present and builds its
  design grade on it rather than adding a second reader. Rung 3. widens: none · relaxes: none
- **F5 — Does S10's reading agree with S4 field for field?** S4 reads a whole-word `S<n>` or `AC<n>`
  as its own token; `review_replay.py` maps `S`, `AC` and `F` items to sections 2, 6 and 8 so a
  candidate citing `S5` matches a known `§2` item (`TOOL-aEvidencedLens-10`). (a) Agree on the `[tag]`
  and `§<n>` forms and keep the item-to-section mapping for matching. (b) Adopt S4's item tokens,
  which changes every past spec-audit score and fails AC3 (veto 1). RESOLVED (agent, 2026-10-23,
  delegated): (a); the brief's "field for field" holds for the two forms both readers address by.
  Rung 3. widens: none · relaxes: none
- **F6 — What is "judge" taken by blob?** The judge's verdicts are the `judge` arm inside the results
  blob; the script that produced them, `-1-6-judge.js` (blob `9b217f4d…`), spawns agents. (a) Read
  the verdicts and cite the script by blob. (b) Re-run the script, which spawns agents and is not
  re-deriving from committed outputs (veto 1). RESOLVED (agent, 2026-10-23, delegated): (a). Rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "score experiment variants against cases from
committed results and pair the cases every variant answered"` ranked `score`
(`tools/memory-recall/bench.py`) and the name stem `pair` (`merge-rows.test.sh`), both name-stem
hits that do not pair committed variant outputs; the probe did not rank `review_replay.py`, which
is the seam this unit extends: its `measure_recall` and `measure_replay`
(`tools/workflows/review_replay.py:263-305`) become the factory's first instance, and aScoutedSeam's
grader (`bench.py:318-398`, `:630-660`) its second. The recall query returned
`TOOL-aSightedSkeptic-9` (the replay benchmark), `TOOL-aEvidencedLens-10` (the spec mode, the source
of F5's item mapping), the research row naming dFairHearing the factory's owner, and the shape audit
calling the grader's branch unmerged, which F1's probe shows is stale: the records are on the default
branch. `TOOL-aWeighedCompass-19` named `tools/memory-recall/union.py` a scorer; it ranks substrates
live and pairs no committed outputs (§3).

Recall terms used: `python tools/memory-recall/query.py "where is the experiment scorer that grades
review replays and benchmark arms" --terms "review_replay measure_recall measure_replay bench.py
grader scorer factory aScoutedSeam replay recall paired arms"`
