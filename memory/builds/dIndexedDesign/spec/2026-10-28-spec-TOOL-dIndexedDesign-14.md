# TOOL-dIndexedDesign-14 — the scout's bug classes by intent: at most five from the catalogue's index, armed only by a replay that beats the anchor ranking's top five

**Status:** OPEN · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 12 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0396@bf718415 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-b.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-b.md) | research | TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

The bug-class lookup selects by path. On code reviews it scored 6.2% precision, 82 hits in 1,317
classes selected, and on the one file a confirmed finding cites it picked the right class 18 times
in 98. The classes that carry the hits are shaped by an act, which a spec or an intent shows and a
path does not (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:446-484`).
The clause asks for "the reuse scout's return also naming at most five bug classes by intent, read
from the catalogue's one-line index against the unit's needs and sketch, each with its reason, for
the unit's spec to carry". That step is "armed only once a replay over the closed code reviews, each
scout given its unit's spec and the index as they stood before the build and never the review, scores
above the anchor ranking's top five with a precision of at least 20%, and retired unarmed if it does
not". This unit builds the replay, runs it, and ships the step only on a win. Both outcomes are
specced as acceptance.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: the scout's return grammar, its grader
`check_reuse_scout` and `read_reuse_scouts` (TOOL-dIndexedDesign-13, I10); `house_index.py` with its
`## Steps` and the slot that hands a scout record to a work order (TOOL-dLinkedLibrary-2 S2, S3, S7);
the experiment factory `experiment.js`, `experiment-args`, `--blind` and the `case_input` hook
(TOOL-dIndexedDesign-5, I12); `replay_scorer.py`'s `INSTANCES`, `case_evidence`,
`derive_paired_cases` and `--experiment` (TOOL-dFairHearing-12 S1, TOOL-dFairHearing-14 S1 to S5);
and the `experiment` entry with its overlay row (TOOL-dBoundRoles-16 S4, TOOL-dBoundRoles-20 S3).

The scout record is unit 13's `record-kind.seams` kind; this unit owns no node.

- **S1** — The anchor ranking, extracted. `derive_class_ranking(recs, paths, m)` in
  `tools/memory-tree/gotchas.py` holds the class half of `cmd_for_paths`'s selection
  (`tools/memory-tree/gotchas.py:688-710`). It takes every non-universal `kind: class` record that
  `selectable` (:340) anchors to a path, and orders them by best `derive_anchor_tier` (:358), then by
  reach, then by name. It returns their names. `cmd_for_paths` calls it, and its checklist is
  byte-identical before and after. "The anchor ranking's top five" is the first five names it
  returns. Observed by AC1.
- **S2** — The corpus, pre-registered.
  - The instrument `memory/builds/dIndexedDesign/build/<date>-build-TOOL-dIndexedDesign-14-replay-corpus.py`
    has two verbs. `write` writes `<date>-build-TOOL-dIndexedDesign-14-replay-cases.json`, opening
    with `// **Serves:** research TOOL-dIndexedDesign-14`. `check` re-derives that file and compares.
  - The population is every tracked diff-review record (`SERVES_PREFIX`,
    `tools/workflows/review_replay.py:65`) that meets three conditions: its appendix parses through
    `parse_appendix_rows` (:151) with a `classes` column; `extract_range` (:139) reads its range; and
    a unit it serves has a spec at the snapshot.
  - The snapshot `before` is the parent of the range's first commit that touches a path outside the
    memory root: the tree as it stood before the build (§8 F3).
  - Each case holds `id`, `review`, `before`, `confirmed` (the class names in confirmed rows'
    `classes` cells), `anchor` (the top five of `derive_class_ranking` over the range's changed paths
    and the catalogue at `before`), `control` (true when `confirmed` is empty), and `input`.
  - `input` holds only `spec`, each `<before>:<spec path>`, and `index`, the `name — description` of
    every `kind: class` record that `load_records_at(root, m, before)` (`gotchas.py:301`) returns.
    That is the catalogue's one-line index as it stood.
  - `write` prints the population: records considered, excluded by reason, cases and controls.

  Observed by AC2.
- **S3** — The variants file, `<date>-build-TOOL-dIndexedDesign-14-replay-cases.variants.md`, in
  TOOL-dIndexedDesign-5's grammar, committed with the cases before the run.
  - `## intent` is the step. Read each `spec` with `git show`, and read nothing else in the
    repository. Write the unit's needs and a concrete sketch from the spec first, as M1c's contract
    orders them. Then name at most five classes from the handed `index` whose act those needs and
    that sketch could repeat, each with its reason.
  - `## Returns` is `{"needs": [...], "sketch": [...], "classes": [{"name": "<index name>", "why":
    "<reason>"}]}`.
  - `## Losing` is the losing outcome, §4 "The verdict".

  Observed by AC5.
- **S4** — The scorer instance `bug-class-intent` in `tools/workflows/replay_scorer.py`'s `INSTANCES`
  (I12).
  - Its `case_evidence(case)` is `review` and `confirmed`. Its `case_input(case)` is `input` alone,
    so `confirmed`, `anchor`, `review` and `before` never reach a scout.
  - An answer naming more than `BUG_CLASS_CAP = 5` classes, or a name absent from its case's
    `index`, is refused naming the arm and the case.
  - Over `derive_paired_cases` it prints, per arm and for the anchor over the same cases,
    `hits <h> · named <n> · precision <p>%`. It then prints one `verdict <arm>: armed` or
    `verdict <arm>: unarmed — <the test it failed>` line per arm, and one
    `verdict bug-class-intent: armed|unarmed` line by §4 "The verdict".

  Observed by AC3 and AC4.
- **S5** — The entry. A repository `[[workflow]]` row `bug-class-intent` in
  `.governance/instructions.toml`, of kind `experiment`, with harness
  `{prefix}/workflows/experiment.js` and `stages = { subject = "gov-reuse-scout" }`. Its
  `[workflow.experiment]` table: `cases` the S2 file, `variants = ["intent"]`, `fan = 4`,
  `scorer = "bug-class-intent"`, `reruns = { "intent.medium" = 2 }`. Observed by AC5.
- **S6** — The replay. At the close the main loop runs §4 "The run", commits the results and the
  manifest under this build's folder, and runs `replay_scorer.py --experiment <manifest>`. The last
  verdict line decides S8 or S9. Observed by AC6.
- **S7** — The grade, dark. `BUG_CLASS_CAP = 0` sits beside `MATCH_CAP` and `MUST_CAP` in
  `tools/memory-tree/tree_lib.py` (TOOL-dIndexedDesign-13 S4). `check_reuse_scout` (its S5) gains a
  `## Bug classes` arm, with one finding for each of three faults:
  - a section holding more lines than `BUG_CLASS_CAP`, so at 0 it must read `none`;
  - a line outside `` - `<name>` — <why> ``;
  - a name with no `kind: class` record in the catalogue at the record's `**Index:**` sha, read
    through `load_records_at`.

  This lands in the instrument pass. The slot unit 13 places is graded from then on, and no scout is
  yet told to fill it. Observed by AC7.
- **S8** — The armed outcome, in one commit after the verdict:
  - `BUG_CLASS_CAP` becomes 5;
  - the `## intent` block's text becomes a step under `house_index.py`'s `## Steps`, and unit 13's
    Return step states the cap as a number beside the other two;
  - `gov-reuse-scout.agent.md`'s `returns:` line names the classes, and its renders re-render;
  - the slot hands the newest record's `## Bug classes` lines, read through `read_reuse_scouts`'
    `bug_classes` key, to the unit's spec writer.

  Observed by AC8.
- **S9** — The unarmed outcome. `BUG_CLASS_CAP` stays 0, so the slot must read `none` and no scout is
  told to fill it; that is the clause's "unarmed" disposition. The step text survives only in S3's
  frozen record. The outcome commit carries a `Decided:` trailer quoting the verdict line. The
  instance, the corpus and the entry stay, so the replay re-derives its verdict. Observed by AC9.
- **S10** — The docs. `help/experiments.md` gains a section on this replay: its population, its
  verdict rule and where the verdict is recorded. Observed by AC10.

## 3. Non-goals (OUT)

- Serving classes by path at writing time. Its retirement is NT-24's, carried by other builds
  (TOOL-dFurnishedOrders-4 S5); this unit does not touch the per-pass checklist.
- The `### Bug classes` spec field and `gotchas.py --for-names`: TOOL-dFurnishedOrders-4 S2 and S3,
  routed by §8 F4.
- The rest of the scout's return grammar and its other caps: TOOL-dIndexedDesign-13's.
- The factory itself: TOOL-dIndexedDesign-5's.
- A blind judge. The confirmed classes are objective evidence, so the deterministic scorer is the
  table's one choice.
- Gated classes. Once TOOL-dLinkedLibrary-24 S5 marks a class gated it leaves the index the corpus
  reads, and this unit reads whatever `load_records_at` returns at `before`.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-5` — `experiment.js`, with `experiment-args` and `--blind`, which S5 and S6 run the replay on; without it the replay has no harness
- **consumes-from** `TOOL-dIndexedDesign-13` — `read_reuse_scouts`, the widened reader whose `bug_classes` key the slot reads, and the `## Bug classes` slot S2 places, which S7 grades through `check_reuse_scout` and S8 arms; without them the classes have no section and no grade
- **consumes-from** external — dFairHearing: `INSTANCES`, `case_evidence`, `derive_paired_cases` and `--experiment` (TOOL-dFairHearing-12 S1, TOOL-dFairHearing-14 S1 to S5)
- **consumes-from** external — dBoundRoles: the `experiment` entry and the overlay row (TOOL-dBoundRoles-16 S4, TOOL-dBoundRoles-20 S3)
- **hands-off** external — dFurnishedOrders: the spec's `### Bug classes` field reading the scout record's `## Bug classes`, the ask of §8 F4
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 41, each a scope item of that batch unit

## 4. Design

### Evidence

- `cmd_for_paths` ranks a class by its best anchor tier, then by reach, then by name
  (`tools/memory-tree/gotchas.py:688-710`), and reads the working tree's catalogue only.
  `load_records_at` reads it at a commit with one `ls-tree` and one `cat-file --batch` (:301).
- `memory/gotchas/INDEX.md` lists notes, invariants and superseded records beside classes, so the
  corpus filters to `kind: class` (scout B, disagreement 3).
- `review_replay.py` prints no precision figure (its docstring, :46-49), so S4 adds one.
- A spec is absent at its own header `base`: `git cat-file -e` fails for
  `2026-10-26-spec-TOOL-dLinkedLibrary-2.md` at `5fede642` and for
  `2026-10-09-spec-DEPL-aBenchedProbe-1.md` at `2b26f187`, read 2026-10-28 (§8 F3).
- The night pass measured 47 closed reviews recording a range among the 66 whose appendices carry a
  `classes` column, PINNED at dispatch 135
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-night2-instruments.md:4031`).
  S2's `write` re-derives the population at the build's HEAD.

### The run

```
python <date>-build-TOOL-dIndexedDesign-14-replay-corpus.py write          # S2, committed with S3
python tools/roles/handoff.py experiment-args bug-class-intent
python tools/workflows/replay_scorer.py --blind bug-class-intent <cases>
Workflow { scriptPath: 'tools/workflows/experiment.js', args: { mode: 'experiment', … } }
python tools/workflows/replay_scorer.py --experiment <manifest>             # the verdict
```

### The verdict

An arm passes when three tests hold over its paired cases: its hits exceed the anchor's top five's
hits, its precision exceeds theirs, and its precision is at least 20%. The step is armed only when
every rerun arm passes (§8 F1). `## Losing` states the same rule before the run, so a loss reads as
a stated outcome, not a surprise.

The clause's "at most five" is spelled three times, and each spelling has a different job. The
corpus instrument cuts the anchor's top five. The scorer refuses an answer past five, which is the
replay's own rule. `tree_lib.py`'s `BUG_CLASS_CAP` is the live grade, 0 until a win and 5 after it.
The scorer is the workflows kit's and `tree_lib.py` the memory-tree kit's, and a kit imports no
sibling kit (TOOL-dGroundRules-1 §4), so neither reads the other's.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_class_ranking` | function, `gotchas.py` | `py.function`, answered OK by `lexicon.py --suggest` |
| `bug-class-intent` | `INSTANCES` key, repository workflow row | none |
| `BUG_CLASS_CAP` | constants, `tree_lib.py` (0 dark, 5 armed) and `replay_scorer.py` (5) | none: the lexicon declares no constant cell |
| `…-14-replay-corpus.py`, `…-14-replay-cases.json`, `…-14-replay-cases.variants.md` | build records | none |

### Rollout

Two passes. The instrument pass lands S1 to S5, S7 and S10, with the grade dark at 0. The outcome
pass lands S8 or S9 after the main loop's S6 run. The verdict is a committed record before the outcome pass begins, so the pass-order
history reads the decision before the code it decides.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`: S1 and its selftest arm
- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/check-memory-hygiene.test.sh`: S7, S8's cap, and the arm §7 declares
- `memory/builds/dIndexedDesign/build/` records named in S2 and S3: the corpus, the cases and the variants file
- `tools/workflows/replay_scorer.py`: S4 and its arm
- `.governance/instructions.toml`: S5
- `tools/codebase-map/house_index.py`: S8, the armed outcome only
- `tools/roles/agents/gov-reuse-scout.agent.md`, its render `.claude/agents/gov-reuse-scout.md`, and the render `tools/roles/README.md`: S8, the armed outcome only
- `help/experiments.md`: S10

### Alternatives rejected

- the spec read at its header `base` — lost to the probe `git cat-file -e 5fede642:memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-2.md`, which fails: a spec is written after the base it is grounded on · `memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-2.md`
- the step text landed dark in `house_index.py` and deleted on a loss — lost to the charter's `[yagni]` "delete rather than disable", read against S9: a loss would ship and then delete text no scout ever read, while S3's record already holds what the replay measured · `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`
- the `## Bug classes` section taken out of unit 13's grammar on a loss — lost to check 31, which grades every `seams` record by its own text: a record written before the removal would red on the section it holds · `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-13.md`
- the anchor baseline computed inside the scorer — lost to the kit boundary: `replay_scorer.py` is the workflows kit's and `gotchas.py` the memory-tree kit's, so the instrument computes `anchor` once and the cases file freezes it · `tools/workflows/kit.toml`
- a review's classes read from its checklist — lost to the night pass's measurement: the checklist is the path selection being beaten, and only the confirmed rows' `classes` cells are the labels · `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`

## 5. Production-readiness checklist

- security — a scout is handed a spec at a commit and the index rows only. The review, the confirmed
  classes and the anchor are withheld by `case_input`'s allow-list. A scout with Bash could still
  run `git log` past `before`, so the `## intent` block forbids it and the page says the blinding
  binds what is handed.
- perf / scale — one `load_records_at` per case at `write`, and about 47 cases times two reruns, 94
  agents, at a fan of four for the replay.
- error / empty / loading states — a record with no range, no `classes` column or no spec at
  `before` is excluded and counted. A case set with no control is refused by `--blind`. A malformed
  answer is refused per case by the scorer.
- observability — `write` prints the population and its exclusions. The scorer prints parsed counts,
  both rankings' figures and one verdict line per arm.
- risks — the corpus is the reviews of this repository's own builds, so a class anchored on this
  build's records can inflate the design side, as the night pass found at 19.9%. The verdict is read
  on code reviews alone.
- testing — the ranking's byte compare, the corpus check, the scorer over planted results on each
  side of each test, and the replay at the close.
- migration — none.
- user docs — `help/experiments.md`, S10.

## 6. Acceptance criteria

Exactly one of AC8 and AC9 applies, chosen by AC6's verdict line. The unit's ledger answers the other
with that verdict line.

- **AC1** — When `gotchas.py --for-paths` runs over the two paths `tools/memory-tree/gotchas.py`
  and `tools/memory-tree/tree_lib.py` before and after S1, the two outputs are byte-identical. A
  `python -c` call of `gotchas.derive_class_ranking` over the same records and paths returns the
  classes in the order the checklist prints them.
  Red when: the extraction reorders a tier or drops a class.
- **AC2** — When the corpus instrument's `check` verb runs over the committed cases file, it exits 0,
  and every case's `input` holds only `spec` and `index`. Each `spec` names a commit at which
  `git cat-file -e` finds that spec, and at least one case is a control. With a case planted whose
  `before` follows its range's first product commit, `check` exits 1 naming the case.
  Red when: a snapshot taken after the build passes, or a case carries a key past `input`.
  figure: the case and control counts are DERIVED by `write`; the 47 is PINNED at dispatch 135.
- **AC3** — When `python replay_scorer.py --experiment <manifest>` scores planted results on a
  three-case fixture, it refuses an answer naming six classes and one naming a class absent from the
  index, naming the arm and case. It prints `verdict intent@medium#1: armed` for hits 4 against 2 at
  40% against 15%. It prints `unarmed — precision` for 19%, and `unarmed — hits` for hits equal to the
  anchor's.
  Red when: an arm at 19% or at equal hits arms, or a six-class answer is scored.
- **AC4** — When `python replay_scorer.py --blind bug-class-intent <cases>` runs over the fixture, each
  printed case holds `spec` and `index` and nothing of `confirmed`, `anchor`, `review` or `before`.
  Red when: any withheld key prints.
- **AC5** — When `python handoff.py experiment-args bug-class-intent` runs, it prints the scorer
  `bug-class-intent`, the one variant `intent`, the rerun count 2, and the `## intent`, `## Returns`
  and `## Losing` blocks.
  Red when: the entry or a block is missing.
- **AC6** — When the main loop runs the `bug-class-intent` entry through `experiment.js` and scores
  the committed manifest with `replay_scorer.py --experiment`, the parsed lines print before the
  figures, and a final `verdict bug-class-intent:` line reads `armed` or `unarmed`.
  Red when: no verdict prints, or a figure prints before its parsed line.
  cost: about 94 agents at medium effort.
  permission: a Workflow run, the main loop's, at the close.
  figure: 20% and five are PINNED by the clause; the hits and precisions are DERIVED by the scorer.
- **AC7** — When `gen_build_index.py --reuse-scouts tFix --check` runs over a scratch build at the
  instrument pass, it exits 1 on a planted `seams` record whose `## Bug classes` holds one line,
  naming `BUG_CLASS_CAP`. It exits 0 when the section reads `none`. It exits 1 on a line naming a
  class absent from the catalogue at the record's `**Index:**` sha.
  Red when: a dark slot accepts a class, or an unknown class passes.
- **AC8** — When the verdict reads `armed`, `grep -n "BUG_CLASS_CAP = 5" tree_lib.py` in
  `tools/memory-tree/` prints the constant, and `grep -n "Bug classes" house_index.py` in
  `tools/codebase-map/` finds the step under `## Steps`. The same `--check` passes a planted record
  with five lines and refuses one with six. `grep -n "Bug classes" gov-reuse-scout.agent.md` in
  `tools/roles/agents/` finds the returns line.
  Red when: an armed verdict ships without the step, or six classes pass.
- **AC9** — When the verdict reads `unarmed`, `grep -n "BUG_CLASS_CAP = 0" tree_lib.py` in
  `tools/memory-tree/` prints the constant, `grep -c "Bug classes" house_index.py` in
  `tools/codebase-map/` prints 0, and `git log -1 --format=%B` on the unit's outcome commit holds a
  `Decided:` line quoting the verdict.
  Red when: an unarmed verdict ships the step or lifts the cap.
- **AC10** — When `grep -n "bug-class-intent" experiments.md` runs in `help/`, it finds the replay's
  section with its verdict rule.
  Red when: the page omits the replay.

## 7. Gates

`gotchas selftest` · `memory-hygiene self-test` · `policy fixtures` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `review-replay selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `roles catalogue` · `roles render wiring` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py · covers AC1 · `cmd_selftest` comparing the checklist with `derive_class_ranking`'s order over a fixture catalogue, staged by sorting reach before tier · none
New arm: tools/workflows/replay_scorer.py · covers AC3 AC4 · `run_selftest`'s `bug-class-intent` arms over planted results at 19% and at equal hits, staged by dropping the precision floor · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC7 · check 31 over a scratch build whose `seams` record holds one `## Bug classes` line under the dark cap, staged by dropping the section's arm from `check_reuse_scout` · none

## 8. Open questions

- **F1 — What does "scores above the anchor ranking's top five" compare, across reruns?** Options:
  (a) hits alone; (b) precision alone; (c) both hits and precision, every rerun arm. (a) arms a scout
  that names five classes per case and hits by volume. (b) arms a scout that names one class rarely.
  RESOLVED (agent, 2026-10-28, delegated): (c), rung 3, the most feature-rich option: it satisfies
  the clause under either reading and leaves no follow-up asking which was meant. widens: none ·
  relaxes: none
- **F2 — How does the `## Bug classes` slot unit 13 places follow the verdict?** Options: (a) this
  unit lands the section only on a win, against I10, which lists it under unit 13; (b) unit 13's slot
  stays, and a loss takes it out of the grammar; (c) unit 13's slot stays, and this unit grades it
  with a cap the verdict sets, 0 dark and 5 armed. (a) disagrees with unit 13's spec, which places
  the slot and hands its lines, cap and arming here. (b) reds every `seams` record already holding
  the section, since check 31 grades each by its own text. RESOLVED (agent, 2026-10-28, delegated):
  (c), rung 3, the most feature-rich survivor: it keeps one grammar, lands dark as the charter's
  `[small]` asks, and lets a win or a loss move one constant. widens: none · relaxes: none
- **FACT-QUESTION · F3 — At which commit do "its unit's spec and the index as they stood before the
  build" read?** Options: (a) the spec header's `base`, as the brief and scout B name; (b) `before`,
  the parent of the range's first commit outside the memory root. Probe: `git cat-file -e
  <base>:<spec path>` over sampled specs. Observation: it fails for both specs sampled, at `5fede642`
  and `2b26f187`, because a spec is committed after the base it is grounded on. Liveness: a spec
  committed before its own base would resolve, so the probe can return a positive. RESOLVED (agent,
  2026-10-28, delegated): (b), rung 2, the probe decides it; the catalogue is read at the same
  `before`. widens: none · relaxes: none
- **F4 — The spec's `### Bug classes` field is TOOL-dFurnishedOrders-4 S2's, and dFurnishedOrders is
  not an ancestor of this build.** Options: (a) a build-run precondition; (b) a stand-in field of
  this build's own; (c) the replay and the armed step need no spec field, and the carry is asked of
  dFurnishedOrders. (a) assumes a non-ancestor lands first. (b) mints a second spelling of one field.
  RESOLVED (agent, 2026-10-28, delegated): (c), rung 3. Ask for dFurnishedOrders, target build
  dFurnishedOrders: "TOOL-dFurnishedOrders-4 S2's `### Bug classes` field reads the newest reuse
  scout record's `## Bug classes` lines, where TOOL-dIndexedDesign-14 armed them" · accept the spec
  writer's work order carries those lines under its `bug-classes` slot, seen on a fixture unit whose
  scout record holds two. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 14, the night pass two's point 6
  (:446-503), I10, I12 and scout B's row for this unit.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from edge of TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.

## 10. Reuse audit

The seams extended are `cmd_for_paths`'s ranking (`tools/memory-tree/gotchas.py:688-710`), extracted
rather than copied; `load_records_at` (:301); `parse_appendix_rows` and `extract_range`
(`tools/workflows/review_replay.py:151`, :139); the scorer factory's `INSTANCES` (TOOL-dFairHearing-12
S1); and TOOL-dIndexedDesign-5's factory. Each line was verified at base. `python
tools/codebase-map/reuse_lookup.py "rank bug classes for a set of paths and measure precision against
confirmed review findings"` ranked name stems (`classify`, `rank_with`, `measure_typed_counts`). None
of them ranks a class or scores a precision, so no existing seam fits the replay's scoring beyond the
factory it extends. Scout B placed the snapshot at the spec's `base`; F3's probe shows the spec is
absent there. Scout B cited `cmd_for_paths` at :671; the ranking it holds runs :688-710.

Recall terms used: `python tools/memory-recall/query.py "how is the bug-class lookup armed by a replay over closed code reviews against the anchor ranking" --terms "bug class gotchas anchor ranking precision replay closed code reviews catalogue index intent scout armed retired"`
