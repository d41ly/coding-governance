**Serves:** research TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18

# Spec brief — dFairHearing, the eighteen units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dFairHearing/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dFairHearing/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your unit's row under "The units", and "Shared interfaces", which every writer reads.

The design sources the clauses compress, all under `memory/builds/dClosedLoop/build/` (`B/` below): the review
system record `B/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md` (lenses and replay bar at its lines 106-242),
the lens research `B/2026-10-15-build-PLAY-dClosedLoop-1-research-review-lenses.md`, the night pass two record
`B/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md` (points 2, 6 and 7), the whole-design audit
`B/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md` (`[walk-table]`, `[recall]`), the gap register lines 386 and
438-456, and the fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never
edit an instrument, v2, the as-built view or the packet: the packet's Non-goals.

## Every spec, whatever its unit

- Path `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-<n>.md`; H1
  `# TOOL-dFairHearing-<n> — <title>`, an EM DASH, never a colon.
- Status header `DRAFT`, `Tier-2`, `base 3708a705`, `streams tooling`, the `order` verb your roster names, and
  `advances TOOL-dFairHearing-19` (the build's own open ask; the build run's last unit closes it).
- Binding lines, each at column 0 on a line of its own: `**Carries:** <Items id>@<hash8> whole`, and for the unit
  that owns a node, `**Carries:** node:<node>` (the owned-node table below).
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams below are a scout's reading at `9bcefeebc`: verify each line number against source before citing it.
- §8 forks: settle each by the README's rungs (execution plan lines 900-946), in the §8 mark shape TEMPLATE-SPEC
  states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and carries `widens:` and
  `relaxes:`, each a value or `none`. Never leave an open question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run.
  `tools/workflows/tier2-review.js` is RENDERED from `tools/workflows/tier2-review.template.js`
  (`check-protocol-parity.test.sh --render`), as `memory/guides/REVIEW-PROTOCOL.md` is from
  `tools/workflows/REVIEW-PROTOCOL.template.md` and `.claude/agents/*.md` from `tools/roles/agents/`: name the
  template as the edit and the render as its copy.
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README). Do not commit it.

## Shared interfaces — one spelling for every writer

Fixed so eighteen specs by five writers agree on the interface axis (M2). A writer who finds one wrong says so in
its §8 as a fork and settles it there; it never silently respells one.

- **S1 · the preset.** A `preset` argument of `tier2-review`, a closed set `unit-spec` (the default, today's
  `SPEC_LENSES`), `design-audit` (unit 2) and `whole-design` (unit 18), refused outside the set and refused beside
  the diff kind, in the shape `intensity` takes (template :213-217). The kind stays `spec-audit`, so the binding
  line and the agent-cap spec-audit rule are unchanged. The `preset` policy key itself is dKeptSession's: read it
  only as the argument.
- **S2 · the opt-in swap.** An `optIn` argument, `{ "<opt-in lens key>": "<default lens key it replaces>" }`,
  checked ONCE at the argument boundary beside the `lensNotes` check (template :852-879): an unknown lens, a default
  the preset lacks, a lens already present and a double swap each refuse by name. The five-slot literal keeps five
  slots after every swap. Owned by unit 3, read by units 9 and 13.
- **S3 · the lens catalogue.** `tools/workflows/lenses.toml`, one `[[lens]]` row per lens with `key`, `brief`,
  `kinds`, `presets`, `default_in` and `optin`, rendered into the harness's five-slot `LENSES` literal by the
  template render. Owned by unit 13; units 2, 3, 9 and 18 add their lenses as rows and code no lens literal.
- **S4 · the address key.** `deriveAddressKey(f)`, defined once in the template: the diff kind `file:line` within
  ±3 lines, the spec kind `file` plus the first `[tag]`, else `§<n>`, then the lens, id as the tie-break. Owned by
  unit 4; units 5, 7 and 18 call it, and the replay scorer's address reading (S10) agrees with it field for field.
- **S5 · the batch label.** `verify:batch-<n>`, the member ids inside the resume file. Owned by unit 4.
- **S6 · grades per item.** `items[].grades: { "<id>": "<binding grade>" }`, the item's `severity` its highest.
  Owned by unit 6; unit 7 reads it.
- **S7 · the disposition grammar.** One `disposition` per confirmed id: `class:<slug>` · `new:<slug>` ·
  `gate:<leg>` · `none`, the last legal only under `review.unclassed` (values `refuse`, `reason`, `owner-rules`,
  default `refuse`), written as a column of the review record's appendix after `classes`. Checked against a
  `legManifest` argument defaulting to the kit's `gate-legs.json` and the class slugs the harness hands over. Owned
  by unit 8; units 9 and 15 read it. dDeclaredLoop's `review.dispose` routes them later: a stand-in.
- **S8 · the round state.** A report field `roundState`, one of `CONVERGED`, `NON-CONVERGENT`, `BOUNDED`,
  `CEILING`, computed from a `roundLimit` argument and the prior rounds' blocker and high counts. Owned by unit 17,
  which settles in its §8 whether the unattended driver's `review_state` (`tools/unattended/unattended.sh`) then
  reads this field or stays a second answer, by the charter's `[one-fact]` rule. Unit 18 reads it.
- **S9 · the dark switch.** Units 2, 4, 7 and 8 ship their behaviour behind its argument or a default-off switch
  (charter `[small]`), so unit 1's replay can run each arm against today's. Unit 1 owns the verdict: a hit flips the
  default, a miss keeps the unit-spec preset for design records, contiguous batches or the per-instance fix verdict,
  and the verdict is recorded with the replay's raw outputs.
- **S10 · the scorer factory.** `tools/workflows/replay_scorer.py`, extracted from `review_replay.py`
  (`measure_recall`, `measure_replay`), with aScoutedSeam's grader as its second instance: one entry that re-derives
  every figure from committed raw outputs, pairs the cases every variant answered and refuses a partial population.
  Owned by unit 12; units 1, 14, 15 and 18 score through it and pair variants nowhere else.
- **S11 · the known-set file.** One row per known defect with `address`, `grade`, `escaped` and `tag`, read by S10.
  Owned by unit 1 (its 59 defects); units 15 and 18 reuse its shape.
- **S12 · the walk table.** `| Item | Scenario | Actor | Needs | Witness | Route | Verdict |`, the whole-design
  audit's `[walk-table]` grammar. Owned by unit 18.
- **S13 · the harness leg.** The slot count, the verifier total and the loop markers live in
  `tools/workflows/check-verifier-fanout.sh` (leg "verifier fan-out" in `tools/gate-legs.json`), and the ref-keyed
  join ban in `tools/workflows/check-review-join.sh` alone. Owned by unit 16; unit 13's slot count is a check there.
- **S14 · the policy keys.** `review.opt-in`, `review.design-audit.runs`, `review.design-audit.seed`,
  `review.unclassed` and `review.twin` with v2's values and defaults (the packet's Obligations). No policy file
  route exists yet: each is read through `review.pin`'s arguments (unit 3), a stand-in until dDeclaredLoop's
  `review.trigger` lands, and each owning unit names that stand-in.

## Owned nodes

| Node | Unit |
|---|---|
| `item.review.lens` | 13 |
| `item.review.pin` | 3 |
| `item.review.refute` | 4 |
| `item.review.report` | 8 |
| `record-kind.review` | 17 |
| `policy-key.review.opt-in` | 3 |
| `policy-key.review.unclassed` | 8 |
| `policy-key.review.twin` | 11 |
| `policy-key.review.design-audit.runs` | 18 |
| `policy-key.review.design-audit.seed` | 18 |

## The units

**Writer groups and build order.** The `order` value is the build order; each writer holds four consecutive orders
(the fifth two). A: 13 (order 1), 2 (2), 3 (3), 9 (4). B: 4 (5), 5 (6), 6 (7), 7 (8). C: 11 (9), 8 (10), 16 (11),
10 (12). D: 12 (13), 14 (14), 1 (15), 15 (16). E: 17 (17), 18 (18). Primitives land before their features: the
catalogue before the presets, the address key before its readers, the factory before every replay, and the
records brought in line after every behaviour they describe. Unit 17 edits `tools/unattended/` if its §8 so
settles, so it builds after every other harness unit.

- **TOOL-dFairHearing-13** — Items 13 (gap-review-09 in part). S3. Seen red on a planted sixth slot, green on a
  catalogue row added as data.
- **TOOL-dFairHearing-2** — Items 2 (gap-review-04). S1's `design-audit` preset: coherence, grounding flagging
  untested assumptions, reuse held to precedent, failure-envelope extended to trust boundaries, alternatives-and-cost
  in place of blast-radius, as catalogue rows; Design's breakpoint passes it when every pinned spec revision is a
  design record (RV-1). Behind S9.
- **TOOL-dFairHearing-3** — Items 3. S2, `review.pin` as the stand-in that maps `review.opt-in` and the pinned
  revisions' record kind to `optIn` and `preset`; the six opt-in lenses as catalogue rows, each shipping on its
  losing test (the lens research's line 191 onward). Owns `item.review.pin` and `policy-key.review.opt-in`.
- **TOOL-dFairHearing-9** — Items 9. Portability, topology and adopter migration as `memory/gotchas/` class records
  anchored to their paths, never universal; and lens notes passed by the callers (`unattended-build`), derived per
  preset after a swap, so the `lensNotes` boundary check never throws on a swapped key.
- **TOOL-dFairHearing-4** — Items 4 (gap-review-06). S4, S5: skeptic batches sorted by the address key before the
  fixed-count chunk, the hook-visible `gov:fixed-verifiers` shape kept. Behind S9. Owns `item.review.refute`.
- **TOOL-dFairHearing-5** — Items 5 (gap-review-08). A confirmed duplicate counted as a merged confirmation in
  precision and the verified counts, and the orphan-duplicate check run on both kinds.
- **TOOL-dFairHearing-6** — Items 6 (gap-review-05). S6, ranked by the highest grade; the synthesizer's merge-one-
  grade instruction removed.
- **TOOL-dFairHearing-7** — Items 7. Refuted claims and same-address twins (S4's key) handed to the synthesizer to
  flag. Behind S9.
- **TOOL-dFairHearing-11** — Items 11 (gap-review-12, gap-review-13). Every agent the harness spawns typed and
  declared in a stage, the resume probe included, seen red on a planted untyped spawn; the twin merge a review step
  runs when `review.twin` opts it in (RS-1), with its item, record kind and check. Owns `policy-key.review.twin`.
- **TOOL-dFairHearing-8** — Items 8 (gap-review-07, gap-review-10). Fix verdicts judged by class; S7. Behind S9 for
  the fix-verdict change. Owns `item.review.report` and `policy-key.review.unclassed`.
- **TOOL-dFairHearing-16** — Items 16. S13: each agent-cap review rule moved, each seen red on its planted case
  before agent-cap stops carrying it; the spec-audit opt-in as a review-kit pack on Workflow calls.
- **TOOL-dFairHearing-10** — Items 10 (gap-review-09). Each record the clause names brought in line with the code
  as the build run leaves it, each live copy re-rendered; `tools/check-agent-cap-restatement.sh` is in its reach.
- **TOOL-dFairHearing-12** — Items 12 (gap-test-18). S10. Its §8 settles two facts by probe: which commit pins
  aScoutedSeam's later results (the scout found `…-5-results.json` absent from `b0fe68f30`), and which population
  the conformance arm scans, given `B/…-score.py`, `tools/codebase-map/rank_harness.py` and
  `tools/memory-recall/bench.py` also pair or score.
- **TOOL-dFairHearing-14** — Items 14. The experiment shape's method as rules S10 enforces or records, in the
  factory's module, never a second one.
- **TOOL-dFairHearing-1** — Items 1. S11 and the blind replays at blob `767187aa` from a bundle of the history to
  `6cfd21619` cloned outside the repository, scored against the bar the clause states; S9's verdicts.
- **TOOL-dFairHearing-15** — Items 15 (gap-review-20). The checklist selected by the pinned range and ordered by
  anchors, handed by the harness itself so the lookup's charter line retires; the with/without replay over the
  known-defect corpus decides selection against every ungated class. The cut of fully gated classes is
  dLinkedLibrary's.
- **TOOL-dFairHearing-17** — Items 17 (gap-review-21). S8, seen red on a planted flat sequence and an oscillating
  one, BOUNDED on a strictly falling sequence that reaches its caller's limit and CEILING one run past it. Owns
  `record-kind.review`.
- **TOOL-dFairHearing-18** — Items 18 (gap-review-22). S1's `whole-design` preset: walkers sliced by scenario and by
  step under `review.design-audit.runs`, S12, a synthesis red on an empty cell, skeptics refuting a sample of clean
  cells, recall through S10 reading `[tag]` addresses and graded as `review.design-audit.seed` says, seen red on a
  planted gap the walk misses and on an empty cell. Owns both design-audit policy-key nodes.
