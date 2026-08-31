# Round 4 spec audit — aGatheredDeclaration

**Serves:** spec-audit TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8

Round 4, over the eight specs at the blobs `d4450eb7..bb117908` produced. Range `d4450eb7..HEAD`.

## Verdict: BLOCKED

## READ THIS FIRST — who synthesized this report

**The harness's synthesis agent DIED**, on `You've hit your session limit`, after all four finder
lenses and all five skeptic batches had returned. No report was written by the harness and its result
carried `report: null`. The 28 findings and their 28 verdicts survived in the run journal at
`wf_70f95630-c3c/journal.jsonl`, and **this report was reconstructed from that journal by the RUN
ITSELF** — the same agent that authored the specs being graded.

**That is a conflict of interest and it is stated rather than hidden.** The three previous rounds
each recorded that their synthesis re-adjudicated severity rather than inheriting the finders'
grades, and round 2's said plainly that nothing was lowered to keep a count under a threshold. Here
the author of the specs performed that adjudication on their own work, with a live incentive: a
count of two or fewer would have re-armed the loop, and a count of three or more terminates it under
`BUILD-METHOD.md` M4. **The adjudicated count is FOUR, which is the answer against the author's
interest** — it ends the loop and forces promotion. That is the only assurance available and it is
weaker than an independent synthesis. A later reader who wants the raw material should read the
journal, not this file.

Nothing was dropped: all 23 confirmed findings appear below, de-duplicated but never discarded.

## Review shape

| | |
|---|---|
| raw findings | 28 |
| confirmed | 23 |
| refuted | 5 |
| precision | 0.82 |
| lenses run | 4, none dead |
| skeptic batches | 5, none dead |
| agents | 10, one FAILED (synthesis) |
| distinct defects after de-duplication | 14 |

Precision rose 0.42 → 0.54 → 0.60 → 0.82 across the four rounds. That is the finders running out of
wrong things to say about a spec set that has been folded three times, and it is the one number here
the author's adjudication cannot have moved: it is computed from the skeptics' verdicts.

## The convergence verdict — the loop TERMINATES

Confirmed blockers by round: **5 → 4 → 3 → 4.** Four is not strictly smaller than three, so under M4
this round is **NON-CONVERGENT** and the loop STOPS. It is not re-armed, there is no round 5, and
every blocker still standing after this round's fold is PROMOTED to a unit of this build, specced at
its tier and built.

**Three of the four blockers are one defect class, and it has a name in this tree:**
`memory/gotchas/amendment-leaves-its-other-half-standing.md` — *a criterion is amended and the
clause, scope item or log line that only made sense under the old wording is left behind, so one rule
now returns two verdicts.* The round-3 fold moved two criteria between units and respelled one output
contract. Each of those three operations left its other half standing. The class was on the checklist
this build ran at every pass boundary, and it was hit anyway, three times, in one fold.

## Findings

| # | Sev | Unit | Address | Defect | journal ids |
|---|---|---|---|---|---|
| B1 | BLOCKER | 6 | §4 Rollout, §6 AC5 | the replaced disposition AND the replaced count both survive the fold that removed them | 3, 6, 14, 22, 23 |
| B2 | BLOCKER | 4 | §4 Data model, last para | still prescribes the ceiling-column overwrite AC8 was rewritten to forbid | 1, 9, 25 |
| B3 | BLOCKER | 3 | §4 Inventory block | respells the "spelled ONCE" contract eleven lines below it, in the pre-fold shape | 2, 17, 24 |
| B4 | BLOCKER | 2, 4, 5 | u2 §2 S10 / §6 AC15 | the new partial-`[bar]` refusal makes u4 AC11 and u5's absent-key row unsatisfiable | 16 |
| H1 | HIGH | 6 | §2 S12, §6 AC17 vs §2 S7 | a below-floor target is promised "the legacy pair" by the unit that deletes half of it | 18 |
| H2 | HIGH | 2 | §4 stamp paragraph | `manifest_blob` has TWO writers, `:1430` and `:1021`; the fold froze one | 4 |
| H3 | HIGH | 6, 7 | u7 §2 S9, u6 §2 S12 | "ONE shared preflight" spans Python/bash and gov-internal/shipped | 5 |
| H4 | HIGH | 2 | §2 S13 | the fold-new one-seam requirement is graded by none of AC1–AC18 | 10 |
| H5 | HIGH | 6 | §7 vs §6 AC15 | AC15 calls `profile-bar selftest` "already a leg" and §7 does not name it | 19 |
| H6 | HIGH | 6 | §2 S1(e) | the clause asserts 21 and corrects itself to 18 three sentences later | 26, 13 |
| H7 | HIGH | 6 | §2 S1(d) vs §6 AC14 | S1(d) emits two `[bar]` keys, AC14 grades four | 27 |
| M1 | MEDIUM | 2 | §2 S5 | the per-ceiling comment requirement has no criterion; AC16 grades only the profile comments | 11 |
| M2 | MEDIUM | 2 | §4 TOML block vs §8 F3 | F3 promises a `full_only` schema comment the block does not carry | 12 |
| M3 | MEDIUM | 2 | §2 S13 | cites §4 for a reuse claim that lives in §10 | 28 |

## The four blockers

### B1 — unit 6's Rollout and AC5 still carry the disposition and the count rev-4 removed

`§2 S5` was rewritten at rev-4 to rule that the five removed suites STAY OFF the bar and that only
three declared legs route through `--leg`. The `§4 Rollout` paragraph twenty lines away still reads
*"Its seven leg names move into the declaration as `opt_in = true` rows carrying the 2026-08-23 owner
ruling as their comment"* — the exact disposition S5 reversed, attributing it to the very ruling it
would breach. `§6 AC5` still demands *"its seven leg names appear in the runner's own summary"*, which
S5 makes unsatisfiable: three legs can appear there, ever.

Five independent finder hits across three lenses. It is the most-confirmed finding of the round.

**Fix.** Rewrite the Rollout paragraph to S5's disposition and correct AC5 to the three legs that
route through `--leg`, naming the five that do not and why.

### B2 — unit 4's Design still prescribes the ceiling-column overwrite its own AC8 forbids

`§6 AC8` was rewritten at rev-4 so the ceiling column keeps its declared NUMBER and enforcement is
reported by an appended column. `§4 Data model`'s final paragraph still says the declared ceiling
*"is reported in `--manifest` as `declared, not enforced`"* — and in a third spelling that matches
neither AC8's `declared-only` nor unit 3's pinned row. §4 is the text an implementer builds from, so
the round-3 defect returns verbatim through the section the fold did not open.

**Fix.** Rewrite that paragraph to cite unit 3 §4's contract and drop the substitute string.

### B3 — unit 3 respells the contract it declares is spelled once

`§4` pins the header and `LEG` row as an OUTPUT CONTRACT *"spelled ONCE, here"*. Eleven lines below,
the `### Inventory` block spells both again in the pre-fold form: the header without its
`from <env|declaration|default>` clause, the row without the three appended columns. The paragraph
asserting single-spelling is refuted by the block beneath it, and unit 4's AC8 now cites "unit 3 §4's
contract" — which is ambiguous between the two.

**Fix.** Delete the Inventory block's duplicate and have it point at the contract paragraph.

### B4 — the new partial-`[bar]` refusal makes two absent-key criteria unsatisfiable

rev-4 added to unit 2 S10 a refusal for a `[bar]` table *"MISSING any key the loader resolves a
default against"*, adding that *"the same refusal covers a hand-written adopter manifest"*. Unit 4's
AC11 requires exactly that fixture — an adopter manifest with no `enforce_ceilings` — to RUN with
enforcement off and report that the default was taken. Unit 5's resolution table has the same third
row. The refusal and the criteria cannot both hold.

This one is a genuine DESIGN contradiction rather than editing residue, and the fold created it while
fixing R4.

**Fix.** Rule once, in unit 2 S10, which `[bar]` keys are REQUIRED and which are DEFAULTED.
`enforce_ceilings` and `turnstile` are defaulted — that is what "opt-in, default off" means — so the
refusal covers only keys with no defensible default. Then units 4 and 5 keep their absent-key row.

## The highs, in one line each with their fix

- **H1** — say where a below-floor target's profile table comes from after S7 deletes it, or amend
  S12 to emit the manifest alone with the built-in formula as a declared consequence, and scope unit
  7 AC8b so it cannot fire on a target gov itself created that way.
- **H2** — name both `manifest_blob` writers. `:1430` (the stamp predicate 7 reads) hardcodes the
  JSON with a comment naming unit 6; `:1021` (the run-record header) keeps `$LEGS_FILE` so `manifest`
  and `manifest_blob` stay consistent.
- **H3** — "one canonical probe, inlined per the kit's no-gov-internal-dependency rule", gated the
  way `resolve_python` already is, named in both units' files-touched.
- **H4** — add the criterion S13 lacks: a grep proving neither suite re-derives a manifest path.
- **H5** — add `profile-bar selftest` to unit 6 §7.
- **H6** — delete the superseded clause from S1(e); the correction three sentences later is the text.
- **H7** — S1(d) says four keys, matching AC14.

## What this report does NOT claim

- It is not an independent synthesis. See the first section.
- No severity was re-graded upward. Three findings the finders marked BLOCKER were folded into B1,
  B2 and B3 as duplicates rather than counted separately, which LOWERS the count from eleven raw
  blockers to four; every merge is listed in the findings table's `journal ids` column so a reader can
  disagree with any of them.
- The five refuted findings were not re-examined. They are in the journal with the skeptics' reasons.
