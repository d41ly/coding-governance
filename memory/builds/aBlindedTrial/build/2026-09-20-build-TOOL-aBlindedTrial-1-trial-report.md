# The blinded trial — spec-first versus build-first, what was measured and what it says

**Serves:** journal TOOL-aBlindedTrial-1

Node `a`, 2026-09-20. Every figure below names the file under `results/` or the command that derives
it; the scratch root is `C:/Users/daily-agent/AppData/Local/Temp/xp/` (`XP`), untracked, and the
briefs are recorded verbatim in the sibling journal. Nothing in this record was typed from memory.

## 1. The question, and the two halves that answer it

Does writing a spec and having it adversarially audited before code produce better code than
building from the brief directly, and what does that cost? Half one reads this repo's own history.
Half two builds the same three briefs under three regimes and grades the tools blind.

## 2. Retrospective — what the tree says about its own practice

`retro.py` (scratchpad; `results/retro.json`), one `git log` walk over 610 specs in 114 builds.
Order is by committer timestamp of the first commit adding each artifact; a product commit is one
touching a path outside `memory/` whose subject names the unit id, falling back to the build slug.

| population | SPEC-FIRST | SAME-COMMIT | BUILD-FIRST | NO-PRODUCT |
|---|---|---|---|---|
| all 610 specs | 499 | 37 | 51 | 23 |
| CLOSED, n=548 | 465 | 36 | 31 | 16 |
| CLOSED, id-attributed, n=402 | 379 (94%) | 20 (5%) | 3 (<1%) | — |
| CLOSED, slug-attributed, n=130 | 86 | 16 | 28 | — |

The slug fallback is coarse — it takes the build's first product commit for every unit — so its
violation rate is an upper bound and the id figure is the trustworthy one. Spec→first-code lag on
CLOSED spec-first units: median 0.2 days, p25 0.1, p75 0.5. The spec is written hours before the
code, by the same session.

Audit ordering, CLOSED Tier-2 units (n=419): AUDIT-BEFORE-CODE 234 (56%), AUDIT-AFTER-CODE 53
(13%), NEVER-AUDITED 125 (30%). Spec-audit records: 193; `## Verdict:` BLOCKED 135, CLEAN WITH FIXES
32, CHANGES REQUESTED 2, none 24 (`grep -m1 '^## Verdict:'` over the `Serves: spec-audit` records).
Median rev of a CLOSED Tier-2 spec: 4.

Twenty CLOSED Tier-2 spec-first units read by five agents (`wf/retro-quali.js`,
`results/retro-quali.json`; sample deterministic by sha1 of the id, 14 audited-before-code and 6 with
no audit record found by the sampler, 18 with one found by the readers):

| measure | value |
|---|---|
| acceptance criteria, total / naming a concrete observable | 173 / 171 (99%) |
| satisfied in the product diff / violated / untestable | 146 (84%) / 23 / 4 — 18 of the 23 violations sit in three units |
| behaviours in the diff the spec never mentions, per unit | mean 1.75, range 0–6 |
| spec revised after the first product commit (scope, design or acceptance) | 12 of 20 |
| audit findings folded, per audited unit | median 5, range 0–21 |
| audit's fold visible in the built code | yes 13, partly 3, no 2, no audit 2 |
| reader's judgement: same change would have been built from the goal statement alone | likely 9, unlikely 10, unsure 1 |

## 3. The prospective trial — design as run

Three briefs (`XP/briefs/`, verbatim in the sibling journal): **A** a declared-population checker
with a stale-waiver rule, **B** a row-keyed three-way merge driver, **C** a gate-ledger reporter
with a liveness assertion. Each is a one-file Python 3.11 stdlib tool with example fixtures and
deliberate open points. Three arms, three replicates each, 27 cells, every cell its own git
repository under `XP/cells/`, forbidden to read outside itself:

- **B** — build from the brief; no design document.
- **P** — write an unreviewed `PLAN.md` of at most 40 lines (acceptance criteria, open points,
  approach), then build; one agent.
- **S** — this repo's method: a full `TEMPLATE-SPEC.md` Tier-2 spec → `tools/workflows/tier2-review.js`
  in its `spec-audit` kind (4 lenses, ≤5 skeptic batches, synthesis) → every confirmed finding folded
  to rev-2 and every §8 fork resolved → a different agent builds from the spec; to diverge it must
  bump to rev-3 first.

Grading, independent of every arm: a hidden pytest suite per brief written from the brief alone,
verified by a second agent, run against an exit-0 stub (every test must fail), sha256-frozen before
any arm ran (`results/hidden-freeze.json`: 43 / 42 / 42 tests; 26 / 21 / 24 `stated`, 7 / 14 / 11
`implied`, 10 / 7 / 7 `ambiguous`); a blind finder→skeptic review per tool under a salted code name
(`results/blind-map.json`), the skeptic defaulting to refuted; adherence judges over the S specs and
P plans; an edge probe per task fingerprinting behaviour on every open point the suite left unpinned
(AC11, amended in at rev-3 when the suites saturated); non-blank lines of code; per-agent token
usage from the transcripts, joined to cells by a prompt tag (`results/tokens.json`).

Runs: `arms-A/B/C.js` (45 + 44 + 45 agents), `eval-A/B/C.js` (24 each), `hidden.js` (6),
`probe.js` (3), `retro-quali.js` (5). A session limit at 17:40 killed 30 in-flight agents across
three runs; all three were resumed by run id with cached agents replayed, and no cell, spec or
verdict was lost (the two P adherence judgements that finished before the cut are in the resumed
result).

## 4. Results

### 4.1 Hidden suite — saturated

`harness.py run-hidden`, `results/hidden-results.json`: **every one of the 27 tools passes its
frozen suite at 100%** — 43/43 on A, 42/42 on B, 42/42 on C, in every arm, every replicate,
including every `ambiguous` test. The suites are live: an exit-0 stub fails all 127 tests, and a
one-token mutation of a passing A tool fails 10 of 43. For briefs this explicit, correctness against
a brief-derived suite does not separate the arms.

### 4.2 Edge probes — the open points

`harness.py probes`, `results/probe-results.json`. Probes per task 37 / 29 / 34 = 100.

| | A | B | C | all |
|---|---|---|---|---|
| probes where all nine tools behave identically | 28/37 | 23/29 | 28/34 | 79/100 |
| within-arm agreement, B | 32/37 | 28/29 | 31/34 | 91/100 |
| within-arm agreement, P | 35/37 | 28/29 | 31/34 | 94/100 |
| within-arm agreement, S | 32/37 | 24/29 | 32/34 | 88/100 |
| crashes or timeouts | 0 | 0 | 0 | 0 |

On the points the brief leaves open, the nine tools agree with each other four times in five
regardless of arm, and the three tools built from three independently authored and audited specs
agree with each other slightly *less* often than three tools built with no design document at all.

### 4.3 Blind adversarial review

`results/eval-{A,B,C}.json`, unblinded through `results/blind-map.json`. One finder and one skeptic
per tool; a finding survives only if the skeptic reproduces it and the brief requires what it
assumes.

| arm | raw findings | refuted | confirmed | confirmed / tool | blocker or high | B/H per tool | finder precision |
|---|---|---|---|---|---|---|---|
| B | 56 | 35 | 21 | 2.33 | 8 | 0.89 | 0.38 |
| P | 46 | 25 | 21 | 2.33 | 6 | 0.67 | 0.46 |
| S | 45 | 26 | 19 | 2.11 | 4 | 0.44 | 0.42 |

Per cell, confirmed (blocker-or-high in brackets): A — B 5(2) 3(0) 2(1), P 3(1) 1(0) 4(1), S 3(1)
1(0) 3(0); B — B 1(1) 1(1) 2(1), P 2(0) 2(1) 3(0), S 2(0) 4(1) 2(1); C — B 1(1) 3(0) 3(1), P 1(1)
3(1) 2(1), S 1(0) 2(0) 1(1).

Two-sided permutation test over the nine cells per arm (20 000 shuffles, seed 7): confirmed B vs S
p = 0.85, P vs S 0.82, B vs P 1.00; blocker-or-high B vs S p = 0.23, P vs S 0.64, B vs P 0.67. The
direction favours S on severity — half the high-severity defects of B — and nothing here is
distinguishable from chance at n = 9.

The defect classes are the same in every arm (counts are tools carrying at least one confirmed
finding of the class, from the confirmed lists in `eval-*.json`). A: stdout left on the Windows
console code page (4 tools: B/1 B/2 B/3 P/1), a non-UTF-8 `kits.toml` or `waivers.txt` escaping as
a traceback with exit 1 (4: B/1 P/3 S/1 S/3), a BOM glued to the first waiver (2: B/1 P/3),
`--root ""` accepted (2: S/2 S/3). B: a row one side *moved* is re-seated, duplicated or dropped
(6: B/2 B/3 P/2 S/1 S/2 S/3), rows mis-seated beside a text edit or conflict (3: B/3 P/3 S/2), a
delete-vs-change block placed under the wrong heading (2: B/1 P/1). C: a non-UTF-8 ledger escaping
as a traceback (5: B/1 B/2 B/3 P/1 P/3), a naive timestamp silently read as UTC (2: B/2 P/2), a
float ceiling compared against a Decimal median so a median equal to `12.7` reports BREACH (1: P/2).

**The S specs named these classes and the S builds still carried them.** `grep -ciE` over the nine
specs: A's three specs mention BOM / `utf-8-sig` 6, 1 and 3 times and non-UTF-8 input 3, 8 and 3
times; B's mention moved rows 5, 12 and 17 times; C's mention Decimal or float 9, 4 and 21 times.
A/S/1's spec pins "`waivers.txt` not decodable as UTF-8 → exit 2" in two places and says nothing
about `kits.toml`; the builder handled exactly the file the spec named, and the review confirmed a
high on the other. The spec is followed as a ceiling as much as a floor.

### 4.4 Adherence — were the specs and plans followed, and were they concrete

`results/eval-{A,B,C}.json`, `adherenceS` / `adherenceP`. Every criterion was run by the judge.

| | S specs (9) | P plans (9) |
|---|---|---|
| acceptance criteria, total | 164 | 101 |
| naming a concrete, failable observation | 164 (100%) | 100 (99%) |
| SATISFIED / VIOLATED / UNTESTABLE by the built tool | 164 / 0 / 0 | 97 / 4 / 0 |
| observable behaviours the document never mentions, per tool | 9.7 | 14.0 |
| builder diverged and bumped the spec (`deviationsFromSpec`) | 2 of 9 | n/a |
| document size | 26.7–46.6 KB, mean 33.8 KB | mean 3.2 KB |

The judges' notes call the specs "unusually prescriptive" — regexes pinned byte-for-byte,
algorithms as pseudocode with variable names, exact stderr strings, `main(argv)` signatures. The
owner's premise that specs are abstract is not what these specs are, and it is not what the
retrospective's 171 of 173 concrete criteria are either; the gates that require a backticked witness
and a `Red when:` clause have done that work.

### 4.5 The audit itself

`results/arms-{A,B,C}.json`, `S[*].audit`: nine audits, 186 raw findings, 72 confirmed (precision
0.39; the harness printed its "below 0.5 — tighten scope" line on seven of nine), 2 blockers, 14
highs. All 72 were folded (`S[*].fold.folded`). Acceptance criteria grew from 118 to 162 across the
nine folds (+37%). Audit reports: mean 18.5 KB each.

### 4.6 Size

Non-blank, non-comment lines: B 78 / 148 / 125 (mean 117), P 88 / 151 / 147 (129), S 120 / 193 /
151 (155) on A / B / C. The spec-first tools are 32% larger than the build-first ones for the same
hidden-suite score and the same defect classes.

### 4.7 Cost

`results/tokens.json` (`harness.py tokens` over the three arm transcript dirs; 0 untagged agents),
mean per cell:

| arm | agents | output tokens | cache writes | cache reads |
|---|---|---|---|---|
| B | 1.0 | 19.1 k | 0.18 M | 1.62 M |
| P | 1.0 | 21.2 k | 0.17 M | 2.43 M |
| S | 13.1 | 235.7 k | 3.50 M | 27.91 M |

S by step, output per cell: spec 37.0 k · audit lenses + synthesis 77.7 k · audit skeptics 63.7 k ·
fold 30.2 k · build 27.1 k. The audit is 60% of the arm. **S costs 12.3× B in output tokens and 17×
in cache reads**; P costs 1.1× B.

The trial's own bill (`results/trial-cost.json`, workflow agents only, the main loop not counted):
253 agents, 4.38 M output tokens, 63 M cache writes, 525 M cache reads.

## 5. What it says

1. **On tasks of this size and briefs this explicit, the ceremony buys no measurable correctness.**
   27 of 27 tools pass the hidden suite; open-point behaviour is 79% unanimous across arms; confirmed
   defect counts are indistinguishable (p ≥ 0.8). The one directional signal — S carries half the
   high-severity defects of B, 4 against 8 — is p = 0.23 at n = 9 and is worth a larger replicate
   before anyone acts on it.
2. **The cost side is not in doubt.** 12× the output tokens and 17× the cache reads, for a tool a
   third larger. The audit alone is 60% of the arm and its finder precision is 0.39.
3. **Plan-lite is the surprise.** One agent writing 40 lines before coding matched S on every quality
   measure, had the highest within-arm agreement on open points (94 vs 91 vs 88), the fewest raw
   findings for the skeptics to refute, and cost 1.1× B.
4. **Specs are followed — literally.** 164 of 164 criteria satisfied, and the residual defects sit
   exactly where the spec stopped: a class the spec covered for one input file and not the other. A
   spec's value is bounded by what its author thought of, and the audit did not extend that bound
   into the classes the blind review found, even where the spec already named them.
5. **The retrospective's version of the owner's complaint is narrower than stated.** Build-first
   ordering is ~6% of closed units by the trustworthy measure, not "often"; specs are concrete, not
   abstract; but 30% of closed Tier-2 units were never audited, 60% of specs were revised after the
   code landed, and in half the sampled units the reader judged the same change would have been built
   from the goal statement alone.

## 6. What it cannot say, stated so nobody over-reads it

- **Task size.** Every unit here fits one agent context and one file. The method's claimed value —
  order across many passes, regrounding after compaction, contract-first for two nodes — is not
  exercised by a 150-line tool and this trial says nothing about it.
- **Brief quality.** These briefs pin exit codes, output tokens and file formats; they are already
  half a spec. A three-sentence owner brief is the case where a spec has the most room to help, and
  it is the untested case. The follow-up that would settle it is a fourth task with a deliberately
  vague brief, same three arms.
- **Judges are the same model family as builders.** Blind, but not independent of the builders'
  blind spots; the shared Windows-encoding class in every arm may be one such.
- **n = 3 per cell.** Cost ratios are precise; quality contrasts smaller than about one defect per
  tool are invisible.
- **The S arm's audit ran once, round 1 only.** The repo's method allows a second round on BLOCKED;
  no audit here returned BLOCKED, so none was owed, but a multi-round audit was not measured.

## Acceptance ledger

**Evidences:** TOOL-aBlindedTrial-1
- AC1 — `retro.py` — 610 specs across 114 builds; order and audit distributions printed for all and
  for CLOSED, split by attribution; `retro.json` written, every §2 figure carried in it.
- AC2 — `retro-quali.js` — 20 of 20 sampled units graded, 5 batches, 0 dead.
- AC3 — `harness.py freeze-hidden` — three sha256 rows, 43 / 42 / 42 tagged tests; `run-hidden`
  asserts the hash before every run.
- AC4 — `python -m pytest test_A.py` with `SUT` at an exit-0 stub — 43 / 42 / 42 failed, 0 passed,
  on all three suites, run independently of the authors.
- AC5 — `git log --oneline` in each cell — 27 `[cell:T/arm/rep] build` commits; every S cell's
  `reviews/` holds one `tier2-review.js` report and its spec header reads rev-2 or rev-3.
- AC6 — `arms-*.json` `S[*].build.deviationsFromSpec` — 2 of 9 S builders diverged, both bumped
  to rev-3 (A/S/3, B/S/3); the count is in §4.4.
- AC7 — `hidden-results.json` — 27 cells, pass counts split by `stated` / `implied` / `ambiguous`,
  no cell missing.
- AC8 — `eval-A.json` `eval-B.json` `eval-C.json` — 27 review rows with raw, confirmed, refuted;
  the finder and skeptic prompts name a code and a brief and no arm.
- AC9 — `harness.py tokens` — 0 untagged agents over the three arm runs; skeptic batches attributed
  through the `EXP-<T>Cell-<rep>` spec path in the findings they judged.
- AC10 — this record — every figure names its `results/*.json` key or command; §4.7 states the
  trial's own cost beside the arms'.
- AC11 — `probe-results.json` — 100 probes over 27 tools, 0 crashes, distinct-behaviour count per
  probe and within-arm agreement per arm; the probe authors read the brief and `AMBIGUITIES.md` only.
