# TOOL-aMendedFleet-110 — a drift signal moved from BASELINES into PINS is graded against the base's BASELINES

**Status:** SPECCED · rev-1 · 2026-10-06 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-06 · order 107

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The shrink-only guard unit 56 added to drift-audit can be escaped: `build_baseline_findings` grades
only the signals the working `BASELINES` still lists, and returns nothing when that dict is empty.
Deleting a baselined signal from `BASELINES` and pinning it in `PINS` at any count therefore passes
`drift_report.py --check`, which lets new offenders up to that count stay green. This unit closes
finding 1 of the round-1 closing diff review, the build's one HIGH, with the skeptic's corrected fix:
every signal the base baselined is graded, and a move to `PINS` above the base set's size reds.

## 2. Scope (IN)

- **S1** — THE MOVE IS GRADED. In `tools/drift-audit/drift_report.py`, `build_baseline_findings`
  takes the working layer's `PINS` as a fourth parameter, and the `if not baselines: return []` early
  exit goes. After its existing loop over the working sets, it walks every signal the base's
  `BASELINES` holds that the working `BASELINES` does not. For each one the working `PINS` declares
  with a count above the size of the base's set, it returns one finding that names the signal, the
  working pin, the base set's size and the base ref, and says the move WEAKENS the bound. A signal the
  working `PINS` does not declare, or declares at or below that size, is no finding here. The one
  caller, in `main`, passes the same `PINS` dict the both-declared refusal reads. Observed by AC1,
  AC2, AC3, AC4.
  **Readers:** by name: the `--check` and `--offenders` block of `main` in
  `tools/drift-audit/drift_report.py`, the only caller, and the arms of `test_baselines` in
  `tools/drift-audit/selftest.py` that S3 adds. by value: the `ratchets` list in `main`, which
  `render_drift_offenders` keys for `--offenders` and the `--check` path prints as a weakened ratchet
  and turns into exit 1.
- **S2** — THE CLAIM MATCHES THE CODE. The comment above `build_baseline_findings`, the `BASELINES`
  header comment in `tools/drift-audit/drift_signals.py` and the `BASELINES` paragraph of
  `tools/drift-audit/README.md` each state the move rule: a signal leaving `BASELINES` for `PINS` may
  be pinned no higher than the size of the set the base held. The README sentence carries the phrase
  `pinned no higher than`. Observed by AC5.
  **Readers:** by name: READER NOT IN TREE, because these are prose read by people and no program
  spells them. by value: NO VALUE READERS, because no program reads, counts or derives from comment or
  README prose.
- **S3** — THE CLASS GATE. Three arms in `test_baselines` of `tools/drift-audit/selftest.py`, after
  the fixture commits its seeded `BASELINES` as the base. A MOVE arm calls `build_baseline_findings`
  directly with a non-empty working dict that names a different signal and omits the baselined one,
  and a `PINS` dict holding the baselined signal at 2, and expects one finding naming it. An EMPTY arm
  writes the layer with no `BASELINES` and the baselined signal in `PINS` at 2, runs `--check`, and
  expects exit 1 with a weakened-ratchet line naming the signal. A CONTROL arm writes the same layer
  with the pin at 1, the base set's size, and expects exit 0. `CHECK_FLOOR` moves by the checks the
  arms add. NOT OBSERVED by a criterion here: the suite runs once, after the build is complete, and
  the arms are declared under `New arm:` in §7 with the staged break that must red the MOVE and EMPTY
  arms before the fix lands.
  **Readers:** by name: the `test_baselines` call in the suite's `main` in
  `tools/drift-audit/selftest.py`, which already runs the function the arms join. by value:
  `CHECK_FLOOR`, which the suite compares against the checks it counted.

## 3. Non-goals (OUT)

- Grading an equal-count move as a weakening. The skeptic's corrected fix reds only a pin ABOVE the
  base set's size; §4 records why the stricter reading was rejected.
- Any change to `ratchet_findings` or the `RATCHETS` rows. A `PINS` key the base did not declare is
  still no comparison for that function, and this unit grades the one case that matters, a key the
  base bounded through `BASELINES` instead.
- The other sixteen confirmed findings of the round-1 review. They are promoted to their own units.
- Bumping the drift-audit kit version. Many units of this build move the kit, and the bump is owed
  once, at the close.

### Edges

- **consumes-from** external — the guard, the both-declared refusal and the `test_baselines`
  fixture that the CLOSED unit 56 of this build landed, which this unit extends; without them there
  is no `BASELINES` to grade.
- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `e83b29b6`, the tip the review read. PINNED, measured 2026-10-06.

- `build_baseline_findings` at lines 400 to 442 of `tools/drift-audit/drift_report.py` still opens
  with the early exit and still loops over the working dict alone, so the finding is not fixed.
- A probe imported `drift_report` and called `build_baseline_findings` against the layer at `HEAD`.
  An empty working dict returned no finding. A working dict that kept only
  `non_terminal_specs_cited_by_product_source`, the move of the other signal, returned no finding.
  The LIVENESS control, `closed_specs_with_no_product_commit` gaining one id, returned the expected
  `gained` finding, so the probe can produce a negative.
- Both baselined signals build their records with `"tolerance": 0`. A signal deleted from
  `BASELINES` and from `PINS` alike is therefore pinned at 0 and already reds as over its pin; the
  escape exists only when the move adds a `PINS` entry. That is why the EMPTY arm of S3 carries a pin
  above the base size: an arm that only empties `BASELINES` reds on the current code for an unrelated
  reason and could not observe the defect.
- `drift_report.py --check` exits 0 at that tip, with the two signals at values 2 and 1, equal to
  their listed sets.

### Mechanism

```
for sig in sorted(old_sets):
    if sig in baselines:          # graded by the existing loop
        continue
    size = len(set(old_sets[sig]))
    if sig in pins and pins[sig] > size:
        out.append(<signal, pins[sig], size, base_ref, WEAKENS>)
```

The base layer is still read with `ast.literal_eval`, and its parse and non-literal refusals are
unchanged. With the early exit gone, the base layer is read on every `--check` and `--offenders` run
whose layer exists, which costs one `git show` the run already paid whenever `BASELINES` was set.

### Inventory

No new definition. `build_baseline_findings` gains one parameter, `pins`. The arms sit inside the
existing `test_baselines` and define no helper of their own.

### Rollout

The fixture of `test_baselines` ends its existing arms with a committed layer that pins the signal
and holds no `BASELINES`, so the new arms first commit the seeded layer to make it the base. The
staged break for the left-shift is the new loop deleted and the early exit restored with the new
signature kept, so an arm fails on the predicate rather than on a call-signature error.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`

### Alternatives rejected

- **The finder's own proposal.** The review judged it UNSOUND, and the skeptic's correction is what
  §2 specifies.
- **Red any move out of `BASELINES` that is not a drain, an equal count included.** An equal-count
  pin does give up the swap detection the set bought. It is rejected because the first-seed rule
  already admits the reverse move at or below the base's pin, so the symmetric bound is the size; and
  a red with no remedy but keeping the set would make retiring a set to a count impossible.
- **A `RATCHETS` row per `PINS` key.** `ratchet_findings` compares a scalar the base already
  declares, and a key new to `PINS` has none, which is the gap itself.

## 5. Production-readiness checklist

- security — closes a governance-layer escape from a shrink-only guard; no new input or write path.
- perf / scale — one `git show` of the layer per `--check` run that previously skipped it when the
  working `BASELINES` was empty; seconds-tier budget unchanged.
- error / empty / loading states — an empty or absent working `BASELINES` is now graded rather than
  skipped; a layer new on the branch is still no comparison.
- observability — the finding names the signal, the pin, the base size and the base ref, so the
  remedy is readable from one line.
- risks — a deliberate retirement of a set to a larger count now reds; the remedy is to pin at the
  base size and drain first, which is the intended cost.
- testing — AC1 to AC5; the arms in S3, whose MOVE and EMPTY arms must red on the staged break.
- migration — N/A: no stored state changes, and the live layer moves no declaration.
- user docs — S2.

## 6. Acceptance criteria

- **AC1** — When, in a scratch clone of the unit's tip under a short `%TEMP%` path,
  `closed_specs_with_no_product_commit` is deleted from `BASELINES` in
  `tools/drift-audit/drift_signals.py` and added to `PINS` at 50, and
  `python tools/drift-audit/drift_report.py --check --base-ref HEAD` runs, it exits 1 and stderr
  carries a weakened-ratchet line naming that signal, 50 and the base size 1.
  Red when: it exits 0, or no line names the moved signal.
  fixture: the tree holds the live instance today, two baselined signals in the layer.
  figure: the base size is DERIVED from the layer at `HEAD`.
- **AC2** — When, in the same clone, the layer instead reads `BASELINES = {}` and `PINS` holds both
  baselined signals each at one above its base set's size, and the AC1 command runs, it exits 1 and
  stderr carries one weakened-ratchet line per signal.
  Red when: the empty working dict returns no finding, which is the early exit this unit removes.
- **AC3** — When, in the same clone, the layer reads `BASELINES = {}` and `PINS` holds both signals
  at exactly their base set sizes, and the AC1 command runs, it exits 0 and no weakened-ratchet line
  names either signal.
  Red when: a move at the base size reds, which is a guard refusing every move.
  figure: DERIVED; both values equal their listed sets at the unit's tip.
- **AC4** — When the loop over the base's sets is deleted and the early exit restored in the clone's
  `tools/drift-audit/drift_report.py`, signature kept, the AC1 and AC2 edits each exit 0.
  Red when: either still exits 1, so AC1 or AC2 cannot tell the fixed code from the broken one.
- **AC5** — When `grep -n "pinned no higher than" tools/drift-audit/README.md` runs, it hits the
  `BASELINES` paragraph.
  Red when: the README still says the set has no escape without stating the move rule.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · covers AC1 AC2 AC3 · the loop over the base's sets deleted and the early exit restored in `build_baseline_findings`, signature kept, reds the MOVE and EMPTY arms while the CONTROL arm stays ok · `CHECK_FLOOR` moves by the checks the arms add

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, from finding 1 of the round-1 closing diff review and its
  skeptic-corrected fix, re-verified against the tip `e83b29b6` by a direct call of the guard.

## 10. Reuse audit

The seam extended is `build_baseline_findings` in `tools/drift-audit/drift_report.py`, with the
both-declared refusal in `main` beside it and the `test_baselines` fixture in
`tools/drift-audit/selftest.py`; no new function is needed. `python tools/codebase-map/reuse_lookup.py
"compare a shrink-only declaration in the project layer against the base ref and report a
weakening"` returned name-stem neighbours only, such as `report` in the drift-audit selftest,
`check_shrink_row` and `load_project_layer`, none of which compares a `BASELINES` key against the
base, so no existing seam fits outside the guard itself; the scan reported no unscanned layer.
Recall returned the review record itself, the unit 56 spec's own reuse audit, and
`TOOL-aNumeralWarden-3`, the ask that a pin raise must not read as a drain, which this unit's move
rule serves. Where the report and the tree disagree: none; the finding reproduces at the tip.

Recall terms used: `python tools/memory-recall/query.py "how is a drift signal's shrink-only bound
kept from being escaped by moving it to another declaration" --terms "drift-audit BASELINES PINS
shrink-only ratchet weakens base_ref escape RATCHETS pin raise justification marker"`
