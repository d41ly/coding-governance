# TOOL-dFairHearing-1 — the verdicts: each replay's figures against its bar, and the two defaults they flip

**Serves:** research TOOL-dFairHearing-1

This is spec S9 and AC9, written by pass (b). Each verdict is judged here from the raw returns committed beside
this record, against the bar spec §2 states and each staged input's `## The bar` section restates. The
first dispatch's return (`2026-11-03-build-TOOL-dFairHearing-1-3-builder-return`) was read as a draft and
re-judged, not copied.

## The verdicts

| Replay | Switch | Figures | Bar | Verdict | Default |
|---|---|---|---|---|---|
| 1, the design-audit preset blind | `review.pin`'s design-record mapping (`TOOL-dFairHearing-3`) | not run by this unit | 45/59 reviewed, 4/6 escaped, 7/8 high in each run | superseded: `TOOL-dFairHearing-25` runs, scores and verdicts it (spec §3, its hands-off edge) | `unit-spec`, unchanged here |
| 2, batches by address | `batchBy` (`TOOL-dFairHearing-4`) | under `address`, 4 of 8 twins meet one skeptic, with A59 in batch 5 and A38 in batch 4; under `id`, 0 of 8 | A59 joins A38 in one batch, and at least 4 of 8 twins meet one skeptic | MISS | `id`, unchanged |
| 3, twins shown | `addressTwins` (`TOOL-dFairHearing-7`) | run A `twinFlags` `[{59,38},{59,13}]`; run B `[{61,43},{61,28}]` | A59 with A38 and B61 with B43 flagged; the negative pairs 59/1 and 61/1 not flagged | HIT | `hidden` → `shown` |
| 4, the fix judged by class | `fixJudge` (`TOOL-dFairHearing-8`) | #23 `fixVerdict` `"instance"`; control `fixVerdict` `"sound"` | #23 judged `instance`; the control anything but `instance` | HIT | `instance` → `class` |

## Replay 1 — superseded

Spec §3's hands-off edge to `TOOL-dFairHearing-25` supersedes this unit's AC4, AC5 and AC9's replay-1 half
with that unit's AC1 to AC5 and AC7. So this unit ran no design-audit run, flips nothing in `review.pin`,
and files no ask in `BACKLOG.md`. R-1 stays as it is until unit 25's verdict.

## Replay 2 — MISS

- **Figures:** see `2026-11-03-build-TOOL-dFairHearing-1-replay-2` (its probe `fh1-batches.js` and its
  output, verbatim). Under `batchBy` `address`, 4 of 8 twins meet one skeptic: B61 with B43, aGraftedHelix
  #8 with #14, aSightedSkeptic #7 with #11, and aPairedSlots #18 with #8 and #29. Refuted A59 is in batch 5
  and A38 in batch 4. Under `id`, 0 of 8. That `id` figure is AC6's liveness half.
- **Against the bar:** the count meets 4, but the bar's first half fails, because A59 does not join A38.
  Both are `[supervise]`, and run A's long `[supervise]` run is cut at a batch boundary.
- **Verdict:** MISS, so `batchBy` keeps its `id` default and nothing changes.

## Replay 3 — HIT

The flags are read from each synthesizer's returned `twinFlags` field, never from its prose (AC7):

- **Run A:** `[{"refuted":59,"confirmed":38},{"refuted":59,"confirmed":13}]`. A59 with A38 is present. The
  negative pair, refuted 59 with confirmed 1, is absent. Raw return and report:
  `2026-11-03-build-TOOL-dFairHearing-1-replay-3-synthesis-a-return`. Staged input:
  `2026-11-03-build-TOOL-dFairHearing-1-replay-3-synthesis-a`.
- **Run B:** `[{"refuted":61,"confirmed":43},{"refuted":61,"confirmed":28}]`. B61 with B43 is present. The
  negative pair, refuted 61 with confirmed 1, is absent. Raw return and report:
  `2026-11-03-build-TOOL-dFairHearing-1-replay-3-synthesis-b-return`. Staged input:
  `2026-11-03-build-TOOL-dFairHearing-1-replay-3-synthesis-b`.
- **Verdict:** HIT on the bar as written, so the default of `addressTwins` becomes `shown`.

Data the bar does not grade. Each run also returned one flag on a defect the comparison record's `[map]`
places elsewhere:

- Run A's 59/13: A13 is `invariant-8-fixture` and A59 is `resume-tick-consumers`. 59/13 is not a pair in
  the prompt's SAME-ADDRESS PAIRS block, since A13 cites `[invariants]` and `[tests]`. The harness would
  keep it at `sameAddress` false.
- Run B's 61/28: B28 is `resume-tick-seed`. 61/28 is a pair in the handed block, both at `[supervise]`, so
  the harness would keep it at `sameAddress` true.

Both extra flags follow the synthesis's own merge: run A's item M19 holds ids 38 and 13, and run B's item
M16 holds ids 28 and 43. Neither is the bar's negative pair. So in each run, 1 of the 2 flags names the
verified twin and the other names a confirmed finding merged into that twin's item. A flag notes a twin
and moves no verdict, grade, item or count (`tools/workflows/README.md`). A wrong flag therefore costs one
misleading note in a report.

## Replay 4 — HIT

The bar reads each skeptic's returned `fixVerdict`. Each skeptic's claim `verdict` is not the bar (the
staged files' bar sections). Both skeptics refuted the claim as present at the range's base.

- **#23, `ff0b3dc3..5b4f964d5`:** the return quotes `"fixVerdict":"instance"`. Its `fixNote` names the
  three uncovered cutoff-day mints, `670436cd5`, `22efab659` and `d6aae9d18`, which a merge inside the range
  brought in. Raw return: `2026-11-03-build-TOOL-dFairHearing-1-replay-4-skeptic-23-return`. Staged input:
  `2026-11-03-build-TOOL-dFairHearing-1-replay-4-skeptic-23`.
- **The control, dSweptBranches #23 at fix `f0e00195e`, picked by §8 F4's rule:** the return quotes
  `"fixVerdict":"sound"`, so the control is not flagged. Raw return:
  `2026-11-03-build-TOOL-dFairHearing-1-replay-4-skeptic-control-return`. Staged input, with the pick and
  both records: `2026-11-03-build-TOOL-dFairHearing-1-replay-4-skeptic-control`.
- **Verdict:** HIT, so the default of `fixJudge` becomes `class`.

## The flips

- **`tools/workflows/tier2-review.template.js` and its render `tools/workflows/tier2-review.js`:**
  - absent `addressTwins` resolves to `'shown'`;
  - absent `fixJudge` resolves to `'class'`;
  - the header and the switch comments that described the old defaults, or the switches as dark, now say
    what the code does.

  `batchBy` and `preset` are untouched. The template and the render take identical edits, and their
  `diff` is byte-identical before and after (the render placeholders alone).
- **`tools/workflows/README.md`:** the two switch paragraphs state the new defaults. They also name the
  migration. Every run that passes no `fixJudge` now derives a new review key, since `class` joins the
  key, so files an earlier default run wrote are not reused. Every run that passes no `addressTwins` now
  requires `twinFlags` of its synthesis.
- **The suite arms that move with the flips:**
  - `tools/workflows/tier2-review.test.sh`:
    - `DIFF` and `SPEC` pin `addressTwins: 'hidden'` and `fixJudge: 'instance'`, so every arm built on
      them runs as it did before the flips;
    - the absent `addressTwins` arm resolves to `shown`;
    - the twins arm's second run is the explicit hidden one;
    - the `fixJudge` absent arms delete the pin, and assert that absent agrees with `class` and that
      `instance` keys apart.

    `FLOOR_ASSERTIONS` holds at 524, with its comment saying why.
  - `tools/workflows/unattended-build.test.sh`: the measured-tally synthesis double returns
    `twinFlags: []`, and the arm reading the synthesis prompt expects
    `Return JSON {path, items, summary, twinFlags}`.

## Departures

These are recorded beside §8 F7's, which is `2026-11-03-build-TOOL-dFairHearing-1-deviation-12`:

1. **Replays 3 and 4 ran as direct role spawns by the main loop**, not inside a Workflow script. The
   agent-cap hook admits no inline Workflow script. Bound: §4 Twins and Fix verdict's real synthesizer and
   skeptic handed the harness's render. The prompt each agent read is the harness's own render, so what
   differs is the channel, and with it the schema enforcement a Workflow spawn would add.
2. **The two synthesizers ran at their agent type's effort, high**, not the staged medium of run B's
   arguments (§4 The isolation). A direct spawn takes no effort argument. The two skeptics ran at medium.
3. **The synthesizers' reports went to the run's scratch**, not to the committed path their prompts name.
   Each return record copies its report whole.
4. **The first runs are void.** Each agent read its staged file's `## The bar` section
   (`2026-11-03-build-TOOL-dFairHearing-1-replay-void-runs`). The second runs read copies holding only the
   prompt and schema sections, with these sha256 prefixes, as each return record names them:

   | Run | sha256 prefix |
   |---|---|
   | synthesis A | `a315c96c3fc8` |
   | synthesis B | `04eacfdd0fe0` |
   | skeptic #23 | `2ce1760cb50a` |
   | control | `af376a662260` |
5. **This pass writes two files outside spec §4 Files touched:** `tools/workflows/tier2-review.test.sh` and
   `tools/workflows/unattended-build.test.sh`. These are the suite arms the build brief names as moving with
   a flip. Without them, the arms that read the old defaults go red.

## Owed at the close

These are not run in this pass:

- the §7 legs, the `tier2-review self-test`, `unattended-build self-test` and `review-protocol parity`
  among them;
- the New arm on `replay_scorer.py`, observed RED-first.

The `unattended-build self-test`'s measured-tally arms run their synthesis double under
`RUN_WF_SCHEMA=strict`. That double returns no `dispositions`, which the schema has required since
`TOOL-dFairHearing-8`. The first dispatch's return reported this, and this pass leaves it to the close.
