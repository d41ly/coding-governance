# Research: the review system, which lenses gov should carry

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 37's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-16-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md`.
Its instruments are kept in `build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-lenses-instruments.md`.

---

I ran no gate, Workflow or review, and wrote nothing in the repository. Every instrument and its output is in the scratchpad (paths at the end).

**Recommendation: build a `design-audit` preset (candidate C3), and add no opt-in lenses to today's presets yet.** The presets fit unit specs and diffs: most escapes there are classes a preset brief already names, so they are recall misses, not missing lenses. They do not fit design records, which have no sections for alternatives, security, cost or migration. That is exactly where the runtime record's post-review defects fell. The replays that would settle this need a Workflow run, so I have written each one as the test the build must run.

## 1. [inventory]

**Lens sets as built** (`tools/workflows/tier2-review.js`):
- **Diff lenses (lines 705-731):** `security`, `correctness`, `seams`, `verification`, `intent`. The light set (line 735) is `correctness`, `seams`, `verification`.
- **Spec lenses (lines 741-767):** `coherence`, `grounding`, `reuse`, `blast-radius`, `failure-envelope`.
- The full briefs are in the code. Each spec brief is aimed at unit-spec sections: §2, §3, §4, §6 and §7 (coherence), §4 and §10 (grounding), §10 and §4 (reuse), §4 and §7 (blast-radius), §5 (failure-envelope).

**How a run picks its set:**
- `kind` is a closed set of two values, and the set follows from it (line 773, `const LENSES = isSpec ? SPEC_LENSES : DIFF_LENSES`, marked as fixed).
- `intensity: 'light'` exists for diffs only. The skip happens inside each lens's thunk; a spec audit refuses light. Only the caller picks it, and the unattended-build driver never passes it.
- `lensNotes` adds a note to one lens's brief. It cannot add a lens, and it refuses a key that is not a lens of the current kind (lines 790-806).

**Where each decision lives:**
- **Diff set:** TOOL-aSightedSkeptic-5. These are "the owner's five"; `regressions` was retired; `verification` was added because the repo's most frequent defect is a check that cannot fail (13-19% of findings in the owner's sample). `lensNotes` comes from the same unit.
- **Light set:** TOOL-aSightedSkeptic-7 F1 (70 of 76 classed findings in the owner's sample).
- **Spec set:** TOOL-aEvidencedLens-1 under the owner's 2026-10-05 mandate. It replaced `underspecification`, `contradiction`, `unstated-assumption` and `prior-art`. Prior-art was retired as the noisiest lens (precision 0.58) and its decision-record half folded into `reuse`.
- **Five-lens limit:** aNumeralWarden-1 F2, owner 2026-08-10, against that spec's recommendation. The earlier 6 came from a counter that scored a trailing comma as an element.
- **Lower fan-out cap:** TOOL-aRepatriatedFork-7 lets a repo declare a lower fan-out cap (`FANOUT_CAP`). The lens maximum does not move with it (`agent-cap.js:503`).
- **No row in DECISIONS.md** records any of these. The only rows that touch lenses are TOOL-aEvidencedLens-17 and -22.

**What is already planned:**
- **REVIEW-PROTOCOL.md** plans nothing new for lenses.
- **v2's policies:**
  - `review.<stage>`: off, opt-in, owed or owed-above-tier. The default is opt-in, with Build owed.
  - Also `review.<stage>.effort`, `review.design.rounds`, `review.follow-up`, `review.breakpoints` and others.
- **v2's dCalibratedLens row:** "lenses for Plan, Test, Deploy and Maintain".
- **Elsewhere in the dClosedLoop records:**
  - "one reviewer with a lens per step" (roles layer);
  - "lens packs" as an extension point (flow steps);
  - the diff lens for Build and the gate lens for Test (layer-flow);
  - maintenance-run and loop lenses arriving with observability;
  - a Plan-Review lens (research-plan B).

**Where records and code disagree:**
- `REVIEW-PROTOCOL.md:192` lists "security / correctness / data-integrity / dead-code / integration-seams". aSightedSkeptic-5 §3 parked this and it is still stale. Line 199 says "3-6 lenses"; the hook allows 5.
- The comment at `agent-cap.js:495` says "tier2-review has four" lenses. Both kinds now have five.
- "Five is the most the hook admits" is true **per array literal**, not per run. I checked this against the live hook (table below).
- gap-review-03 says "about 9 agents and 0.81 M tokens per spec audit". Today's recorded spec-audit runs use a median of 11 agents and 185k output tokens (3 runs). These are different token measures, but the agent count is 11-12, not 9.

## 2. [yield]

**Coverage:**
- Lens-level measures come from the 50 reports that have a parseable `## Appendix` (13 spec audits, 37 diff reviews), 1,122 finding rows in all. All of them are from October.
- The other 448 of the 498 reports name lenses only in prose and attribute no finding to a lens. No report records an `uncertain` or `unverified` verdict.
- Verdicts over all 498: spec audits 170 BLOCKED, 60 CLEAN WITH FIXES, 1 other, 25 with no verdict line. Diff reviews 120 BLOCKED, 85 CLEAN WITH FIXES, 1 other, 36 with no verdict line.

**Diff reviews (37 reports):**

| lens | confirmed / raw | precision | high + blocker share of confirmed |
|---|---|---|---|
| verification | 169 / 188 | 0.90 | 0.08 |
| seams | 133 / 156 | 0.85 | 0.16 |
| correctness | 124 / 150 | 0.83 | 0.21 |
| intent | 125 / 138 | 0.91 | 0.14 |
| security | 76 / 101 | 0.75 | 0.22 |

**Spec audits, current set:**
- On unit specs (3 reports) the yields are tiny: 4 to 12 confirmed findings per lens.
- On the two runs over the runtime design record:

| lens | confirmed | precision | highs |
|---|---|---|---|
| coherence | 26 | 0.93 | 4 |
| failure-envelope | 24 | 0.92 | 4 |
| grounding | 23 | 1.00 | 4 |
| reuse | 22 | 1.00 | 1 |
| blast-radius | 18 | 0.82 | 2 |

**Spec audits, retired set (8 reports):**

| lens | confirmed | precision | high + blocker share |
|---|---|---|---|
| underspecification | 81 | 0.87 | 0.10 |
| contradiction | 48 | 0.96 | 0.19 |
| unstated-assumption | 36 | 0.86 | 0.28, including 2 blockers |
| prior-art | 29 | 0.67 | 0.10 |

**Defects only one lens found, across both runtime rounds:** failure-envelope 12 (including the fencing high), coherence 9 (2 highs), reuse 8, grounding 6, blast-radius 4 (all medium or low).

**Checklist seam:** 120 of the 480 confirmed findings in reports with a `classes` column carry a catalogued bug class. `lensNotes` was supplied in 2 of about 49 reports from that period, and the unattended-build driver never passes it.

## 3. [escapes]

**Later rounds on the same subject:**
- Runtime A/B: 27 defects were found by one round only.
- The four precedent defects (`cli-floor-decision`, `permission-mode`, `parallel-cleared`, `owner-rulings`) were all found by `reuse`, and none was found by both rounds.
- Four defects were found after both rounds:
  - the act's missing wall-clock ceiling: cost;
  - fresh worktrees starting dirty on CRLF: portability;
  - kit confs beside the policy file: blast-radius or adopter migration;
  - a cheaper spawn backend: alternatives.
- The later floor probe found two more:
  - the version floor taken from a docs line: a grounding miss, an assumptions-type defect;
  - the allow rule that bypasses the dispatcher: security, for which the spec preset has no lens.
- In the older corpus, dBriefedPass rounds 2 and 3 each had 7 "pre-existing, missed" findings next to 13 and 18 that the fold itself had caused. The aEvidencedLens study (91 escapes over 13 builds) motivated today's spec set.

**Gotchas:**
- 121 records. 83 of them name a build that had a review on or before the date the gotcha was added. That join is a heuristic: it shows the build was reviewed, not that the defect was in the reviewed diff.
- My class for each, shown whole in `escape_class.py`:

| lens that should have caught it | gotchas | naming a reviewed build |
|---|---|---|
| verification | 28 | 18 |
| correctness | 28 | 22 |
| blast-radius | 11 | 7 |
| failure-envelope | 8 | 6 |
| security | 6 | 4 |
| seams | 4 | 4 |
| coherence | 3 | 3 |
| grounding | 1 | 1 |
| **portability** (no preset) | 9 | 5 |
| **topology** (no preset) | 7 | 6 |
| **adopter** (no preset) | 5 | 2 |
| **cost** (no preset) | 4 | 0 |
| **assumptions** (no preset) | 2 | 0 |
| no lens | 2 | — |
| not an escape (3 invariants) | 3 | — |

- So 89 of the 116 non-invariant gotchas sit inside some preset brief, and 27 sit outside every one. All 12 portability and topology records I checked are `universal: false`, so the checklist only hands them to a review whose diff touches their anchored paths.

## 4. [candidates]: one lens per candidate class

Each entry gives the evidence, the brief it would run, and the test that could make it lose. All of these tests are owed and none was run. The replays should be blind: run them at blob `767187aa` in a worktree at `6cfd21619`, which is before the comparison record and the floor probe existed.

- **security (spec and design)**
  - Evidence: the diff `security` lens has the highest high-and-blocker share (0.22) and the lowest precision (0.75). On a design record nothing prices trust boundaries, because there is no §5. It produced one post-review escape.
  - Brief: "trust boundaries the design creates or relies on; an enforcement a rule, setting, second path or dead dependency bypasses; input trusted without validation; a guarded action left allowed on failure."
  - Losing test: swapped in for blast-radius over two runs, neither run raises the allow-rule bypass, or half of its findings duplicate failure-envelope's.
- **precedent**
  - Evidence: 4 of the 4 known precedent defects came from `reuse`, and none was found by both rounds. The old prior-art lens had precision 0.67 here (0.58 in the study).
  - Brief: "a choice that re-opens a decision row, owner ruling or decided ask, or drops a condition a ruling rested on. Name the id and quote both texts."
  - Losing test: it fails to find at least 3 of the 4 in each of two runs at precision ≥0.85, or a `reuse` lens note that names the decision rows and owner prompts scores as well.
- **assumptions**
  - Evidence: unstated-assumption had the top high-and-blocker share among the old spec lenses (0.28). The floor escape is this class. The `grounding` brief already names platform claims.
  - Brief: "every load-bearing claim resting on a docs line or one observation: the observation that would overturn it, probed where the probe rules allow."
  - Losing test: `grounding` plus a lens note flags the docs-line floor just as well.
- **alternatives**
  - Evidence: only one data point, the spawn backend. Unit specs already carry a `### Alternatives rejected` section; design records do not.
  - Brief: "a materially simpler or cheaper mechanism meeting the same contract: an existing seam, a checker instead of an agent, one process instead of many. Say which acceptance or invariant it meets."
  - Losing test: it finds nothing on the runtime blob, or more than half of its findings are refuted as already considered.
- **cost**
  - Evidence: 4 gotchas, the act-ceiling escape, and the aEvidencedLens study, which lists cost among the places no lens was aimed. blast-radius covers budgets and grounding covers untimed goals, but only in part.
  - Brief: "agents, sessions, spawns, tokens and wall time added; one with no ceiling, no enforcer, or a ceiling nobody measured."
  - Losing test: it misses the act ceiling, or blast-radius plus a cost lens note catches it too.
- **portability**
  - Evidence: 9 gotchas, 3 ad hoc portability lenses used in July and August, and the CRLF escape. `grounding` names these traps on the spec kind only; the diff kind has none.
  - Brief: "CRLF and autocrlf in fresh worktrees, text-mode reads, MSYS rewriting, path length, Git for Windows signal semantics, spawn cost under antivirus, clock skew."
  - Losing test: a checklist-only replay, with the 9 portability gotchas made universal, catches as many over the ranges that produced them.
- **adopter migration**
  - Evidence: 5 gotchas; an ad hoc adopter lens found a BLOCKER in `aQuarriedLantern-1-2`; the kit-conf escape. Unit specs have §5 migration.
  - Brief: "what an adopter on the prior version meets: a changed key, shape, render or gate with no upgrade step; non-additive data; versions that must move in lockstep with no check; an assumed install layout."
  - Losing test: blast-radius plus an adopter lens note raises the kit-conf question too.
- **topology (suggested by the data)**
  - Evidence: 7 gotchas, of which 6 name a reviewed build, the highest share of any class; 10 if you count three I filed elsewhere. On the design record, failure-envelope and coherence already found merge-back and fencing, so the gap is on the diff side.
  - Brief: "worktrees, merges and concurrent runs: linked-worktree `GIT_DIR`, absolute hooks paths, a merge read as additions, half-staged moves, leases outliving holders, commits under a running suite."
  - Losing test: the same checklist test as portability.

## 5. [shape]

I probed each shape against the live `agent-cap.js` with a Workflow payload. This was a static check, run outside the repo; it writes nothing on that path.

| shape | hook result | added agents and output tokens (baseline: median full run 11 agents, 185-213k out) | test that makes it lose |
|---|---|---|---|
| swap into a preset (a ternary inside a 5-element literal) | admitted | none | on a blind replay, the dropped lens's sole-lens defects outnumber the new lens's unique confirmed findings. blast-radius is the cheapest slot to give up on design records (4 sole defects). |
| a 5-lens preset concatenated with opt-in lenses | **denied** ("can GROW") | — | — |
| a catalogue of more than 5 lenses, filtered | **denied** | — | — |
| second pass as a separate run (a filter over a ≤5 literal, as in drift-audit-state) | admitted | for 2-3 lenses, about 6-10 agents and 95-125k out (+50-65%), +12-14 min | it buys fewer than about 6.3 confirmed new defects per 100k output tokens. That is what a plain second round of the same preset bought in the runtime A/B: 13-14 new defects, 2 of them high, for about 215k. |
| second wave inside the same script | admitted | 5 + N finders | the hook bounds each receiver, not the run. This is a loophole against the protocol's 5-lens allowance; do not build on it. |
| per-stage preset (nested ternary of ≤5 literals) | admitted | none | there are 0 Plan, Test, Deploy or Maintain review reports to calibrate on, so its lenses would be chosen by feel. It also widens the closed `KINDS` set and the record-kind vocabulary. This belongs to dCalibratedLens. |
| design-audit preset | admitted | none | as for C3 below |

## The three candidates

- **C1, keep the presets and add nothing.** Losing test: escapes on a preset-reviewed subject in a class no brief names. **It loses for design records:** the spawn backend, the act ceiling and the dispatcher bypass fall outside every brief once a record has no §4 Alternatives and no §5. It holds for unit specs and diffs, where 89 of the 116 non-invariant gotchas are recall misses inside a brief.
- **C2, opt-in lenses on today's presets.** Losing test: the checklist (whose classes already show up on 25% of confirmed findings) plus lens notes give equal coverage at zero agents. **Not settled; the replay is owed.** The measured facts point against it: lens notes are almost never used, the candidate classes are anchor-only today, and concatenation is denied, so an opt-in lens can only swap out a default.
- **C3, a design-audit preset plus opt-in lenses.** Losing test: two blind runs at `767187aa` in a `6cfd21619` worktree must find at least 4 of the 6 known escapes, at least 7 of the 8 highs, and about 70% or more of the 59 known defects per run. The test costs about 24 agents and 430k output tokens. **Not run; owed.**
  - The proposed set: coherence; grounding with assumption flags; reuse with the precedent bar; failure-envelope with trust boundaries; alternatives-and-cost in place of blast-radius.
  - Portability, topology and adopter classes would go to the checklist as universal gotchas, and to lens notes passed by the driver.

## Instruments

Scratch directory: `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/lenses/`. Every script takes the repository root, `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297`, and runs with `python -I` unless noted.

- `lens_yield.py <repo>`: the yield tables and coverage counts above.
- `corpus.py <repo>`: verdict tokens over all 498 reports.
- `gotchas.py <repo>`: writes `gotchas.out`, joining each gotcha's add date (from git) to reviewed builds.
- `escape_class.py gotchas.out`: my class map, shown whole, and the escape table. It refuses if any gotcha is unmapped.
- `sole_lens.py`: the sole-lens counts. Run it from `memory/builds/dClosedLoop`.
- `shapes/s1…s6.js` and `shapes/run.py <agent-cap.js>`: the hook results in the shape table.

The cost medians came from an inline python over the `review-shape … at=synth` lines. I printed each script's output verbatim during the session, and the numbers above are copied from it; the main loop can re-run any script to save the output beside this return.

Sources read:
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/workflows/tier2-review.js`
- `…/tools/hooks/agent-cap.js`
- `…/memory/guides/REVIEW-PROTOCOL.md`
- `…/memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md`
- `…/memory/builds/aSightedSkeptic/spec/2026-10-01-spec-TOOL-aSightedSkeptic-5.md`
- `…/memory/builds/aNumeralWarden/spec/2026-08-10-spec-aNumeralWarden-1.md`
- `…/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md`
- `…/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
