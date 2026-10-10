# DEPL-aBenchedProbe-3 — 7j4's liveness reds bind only where a self-test population exists

**Status:** CLOSED · rev-1 · 2026-10-10 · node a · Tier-2 · base 2b26f187 · streams deployer · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-DEPL-aBenchedProbe-3-1-acceptance-ledger.md](../build/2026-10-09-build-DEPL-aBenchedProbe-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-10-build-DEPL-aBenchedProbe-1-runlog-d8d21d0e.md](../build/2026-10-10-build-DEPL-aBenchedProbe-1-runlog-d8d21d0e.md) | journal | DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2 DEPL-aBenchedProbe-4 TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 |
| [2026-10-09-prompt-DEPL-aBenchedProbe-3-1-spec-brief.md](../prompts/2026-10-09-prompt-DEPL-aBenchedProbe-3-1-spec-brief.md) | journal | DEPL-aBenchedProbe-4 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit selfcheck`'s arm 7j4 reds every minimal scratch-gov fixture `tools/govkit/selftest.py`
builds, so the govkit self-test suite is red on its own fixtures while gov's real tree is green.
This unit makes the arm's liveness reds bind only where a population they protect exists, and
repairs the two fixtures that are genuinely in 7j4's red class. It closes the closing review's HIGH
H1 (finding id 2) in `memory/builds/aBenchedProbe/reviews/`, round 1.

## 2. Scope (IN)

- **S1** — The zero-graded and zero-shaped reds in 7j4 (`tools/govkit/govkit.py`, the arm after
  7j3) bind only when gov's leg manifest carries at least one row whose `chunk` is `selftests`.
  Otherwise each becomes an `r.note`, and the arm's existing count note line gains the population
  figure and, when it is zero, the clause `the zero-population reds stand down`. Observed by AC1,
  AC2, AC4 and AC5.
- **S2** — An absent `tools/gate-legs.json` makes 7j4 print a note, not a refusal, whatever the
  descriptors declare. The note keeps the arm's current wording up to `so no leg's chunk is known`
  and says nothing was graded, which is 7h's own rule for an absent manifest (§4). Observed by AC1
  and AC5.
- **S3** — `build_scratch_gov_conf` in `tools/govkit/selftest.py` declares `subject = "kit"` for a
  leg whose chunk is `selftests`, in the descriptor, the manifest row and the fixture pin alike, and
  `repo` for every other leg as today. That fixture's premise is a tree where every declared fact
  agrees, and a `selftests` leg declared `repo` is now a disagreement 7j4 grades. Observed by AC1.
- **S4** — The ratchet fixture's AC5 arms in `tools/govkit/selftest.py` keep subject `repo` and the
  pin-row assertion. The `selfcheck --write` run is expected to exit 1 and to print a line carrying
  `7j4: entry 'demo' gate leg 'demo'`, and the arm's label stops saying it passes. Observed by AC3.
- **S5** — Two persistent liveness arms in the same block, each on one scratch gov built by that
  block's `scratch_gov` with its own tag, and no new function. One has a manifest row in chunk
  `selftests` and no descriptor `[[gate_leg]]`, and asserts exit 1 with
  `7j4: graded zero descriptor gate legs`. The other has one descriptor leg that is not
  self-test-shaped beside an unclaimed `selftests` manifest row, and asserts exit 1 with
  `7j4: found zero self-test-shaped legs`. Observed by AC4.
- **S6** — Two assertions that make each stand-down announce itself. The clean scratch fixture's
  green arm also asserts the stand-down clause in its output. The `[-6]` fixture whose descriptor
  declares legs and whose tree has no manifest gets one more check asserting exit 0 and the S2
  note. Observed by AC5.
- **S7** — 7j4's header comment states the two stand-downs and what covers them on gov's tree:
  7h2's chunk pins catch every `selftests` chunk vanishing from the manifest, and 7h grades no leg
  at all without a manifest. Observed by AC6.

## 3. Non-goals (OUT)

- Not the review's MEDIUM and LOW items. The receipt-after-keep arm, the 7j4 and 7h staged-break
  arms in the gov-copy block, the `manifest_chunk` pre-initialisation and its comment, and CE4's
  leg assertion are all `DEPL-aBenchedProbe-4`.
- Not a change to 7j4's red predicate or its exemption. A self-test-shaped, non-exempt leg whose
  descriptor subject is not `kit` still reds wherever the manifest exists.
- Not a new gate for H1's class. The review proposed a spec-tokens guard mapping
  `tools/govkit/govkit.py` to the `govkit selftest` leg. That join already exists:
  `govkit selftest` guards the govkit directory, and `DEPL-aBenchedProbe-1`'s §7 named it. What that
  unit lacked was an observation of the fixtures, because no pass runs the suite. This spec's §6
  observes them directly, sliced, and `memory/gotchas/hand-named-gate-list-green-while-the-bar-reds.md`
  already carries the class.
- No edit to another unit's fixture or arm beyond S3's fixture, S4's AC5 arms and S6's two
  assertions. The `scratch_gov` fixtures stay as they are, because a tree with no `selftests` row
  is now a true zero.
- No new function or nested helper in either file, so the lexicon and codebase-map legs are not
  moved.
- No kit-version bump inside this unit. The build bumps each touched kit once, after the last unit.
- No edit to `memory/DECISIONS.md`, any backlog, `WIRE-INTO-PROJECT.md`, or anything the
  concurrent run owns.

### Edges

- **consumes-from** `DEPL-aBenchedProbe-1` — the 7j4 arm whose liveness this unit scopes. Without
  it there is no arm to change.
- **hands-off** `DEPL-aBenchedProbe-4` — the persistent staged-break arms for 7j4's red and exempt
  branches, and the `manifest_chunk` pre-initialisation. This unit keeps 7j4's own manifest-presence
  guard and turns its branch into a note, so the pre-initialisation stays dead either way.

## 4. Design

### What reds today, measured

Five blocks of `main()` in `tools/govkit/selftest.py` were run as slices at 54ba9c0e on 2026-10-09
(the method is below). Nineteen arms failed, and each failure is 7j4 alone. These figures are
PINNED as measured then. AC1 re-derives them at build time.

| slice (start anchor) | arms red | 7j4 cause | secs |
|---|---|---|---|
| `===== unit 3: the convergence ratchet =====` | 1: the agreeing-leg LIVENESS arm | zero shaped | 54 |
| `liveness of the two derived assertions` | 12 | zero shaped | 471 |
| same slice | 2: 7c2's `selftests` arm, and AC5's `--write` | the subject red | (above) |
| `` DEPL-cMendedVintage-8: A `rendered` ROW `` | 2: the two AC3 CONTROL arms | absent manifest | 41 |
| `FORK_SRC = {` | 1: `[-10] LIVENESS` | absent manifest | 34 |
| `A6_REG = (` | 1: `[-6] S4 ...while a leg whose engine IS shipped` | absent manifest | 113 |

Two of these the review did not name. 7c2's `selftests` arm in `build_scratch_gov_conf` reds on the
SUBJECT clause, not on liveness, so S1 alone leaves it red, and S3 is its repair. The `[-6]` arm's
descriptor declares two gate legs and its tree has no manifest, which decides §8 F2.

`selfcheck --write` writes the pin and then still exits 1 on a 7j4 red. Observed in the same slice:
AC5's failure detail carries the pin row `demo\trepo\tselftests` and the `wrote 1 subject pin(s)`
line. The write sits inside 7h, which runs before 7j4, and `selfcheck` has no early return.

### Every selftest function that runs `selfcheck`

Enumerated with an `ast` walk over `tools/govkit/selftest.py` for calls whose arguments carry the
string `selfcheck`.

| function | what it runs on | can this unit move it |
|---|---|---|
| `check_fix_carriers` | `selfcheck --bogus` | no: refused before any arm |
| `check_adopter_owned` | a scratch gov with no manifest | no: its arms assert text, and the one that reads the exit expects 1 |
| `check_halved_install_arms` | a copy of gov | no: the real manifest, where nothing changes |
| `main`, gov-copy block (`_run_selfcheck`) | a copy of gov | no, same reason |
| `main.scratch_gov` (unit 3) | a one-leg tree, no chunk | yes: S1 turns it green |
| `main.run_in` / `run_in_gov`, five fixture families | the trees in the table above | yes: S1 to S4 |
| `main`, real-tree runs of `run("selfcheck")` | gov itself | only through the 7j4 note line, AC2 |

### The slice

An arm inside `main()` cannot be called alone, so each criterion runs a slice. A slice is the source
of `main()` cut between two anchor lines, dedented, and executed with `tools/govkit/selftest.py`'s
module globals plus `tmp` and `NL`. Blocks that borrow `run_in` and `build_scratch_gov_kit` get a
prelude cut from `def run_in(g: pathlib.Path)` to `def build_scratch_gov_role`. The runner then
prints `FAILURES`. It lives in the run's scratchpad and is never committed: an untracked script under
`tools/` lands in the codebase map's symbol set. Its temporary root is a short directory under
`%TEMP%`, because a fixture root under the scratchpad false-reds on path length.

| slice | start anchor | end anchor | prelude |
|---|---|---|---|
| A | `===== unit 3: the convergence ratchet =====` | `# Over gov itself both correspondences are COMPLETE` | none |
| B | `================= liveness of the two derived assertions` | `# ---- M5: the gate-policy predicate's two evasions` | none |
| C | `` DEPL-cMendedVintage-8: A `rendered` ROW `` | `========== DEPL-dCarriedReceipt-12` | `run_in` |
| D | `FORK_SRC = {` | `` # ---- AC5: `plan` marks the forked source `` | `run_in` |
| E | `A6_REG = (` | `# ---- AC4: THE FALSE-POSITIVE GUARD` | `run_in` |

The build keeps every anchor line byte-identical, and puts S5's arms inside slice B.

### The population predicate

The population is the count of manifest rows in chunk `selftests`, read from the `manifest_chunk`
map 7h already builds. It is 61 on gov's tree (DERIVED; counted 2026-10-09). With it non-zero,
both liveness reds bind exactly as they do now. With it zero, nothing in the tree is held by chunk,
so a zero-shaped or zero-graded result is TRUE rather than a broken predicate. That is the rule 7c2's
own liveness clause in the same file states, and S1 copies its shape rather than inventing one.

What gov's tree loses is the zero-shaped red in the case where every `selftests` chunk vanishes
from the manifest. It would not have fired there anyway. A read-only probe re-ran 7j4's predicate
over the real descriptors with every `selftests` chunk taken out of the manifest map. It still
found 22 shaped legs, all through the filename clause, and none of them reds. In that case 7h2 reds
each of the 61 chunk pins, and AC6 observes it.

The spec brief asked for two staged breaks on a copy of gov. The first, every `selftests` chunk
taken out, cannot show a liveness red turning into a note, because by the probe above that red
never fires there; AC6 observes the stand-down note and 7h2's cover instead. The second, the
descriptor legs emptied with the chunks kept, is observed on S5's scratch fixture, which is
committed and costs one small tree rather than a gov copy.

### The absent manifest

7h, 7c and 7c2 each grade nothing when `tools/gate-legs.json` is absent, and say nothing. 7j4 now
agrees with them, and announces the skip in a note. Its own `if not legs_path.is_file()` guard
stays, because without it 7j4 would read an empty chunk map and grade every leg as chunkless.

### Inventory

- One note clause, `the zero-population reds stand down`, and one figure on the existing
  `held self-test legs:` note line, `population <n> in chunk selftests`.
- No new function, constant or arm label.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

See §8. Each fork records the test that rejected each losing option.

## 5. Production-readiness checklist

- security: N/A — a read-only check over gov's own descriptors and its test fixtures; no write path.
- perf / scale: one count over a map 7h already built; the two S5 arms add two selfcheck runs on
  one-leg trees, about 15 s each at slice B's measured rate, and S6 adds one more.
- error / empty / loading states: an absent manifest and an empty population are each a named note
  (S1, S2); a population with nothing graded or shaped is a named red (S5).
- observability: the 7j4 note line prints the population beside its graded, shaped and exempt
  figures on every run.
- risks: loosening a liveness red can hide a broken predicate. The population condition keeps the
  red on any tree that holds a leg by chunk, and AC6 shows 7h2 covers the case it gives up.
- testing: AC1 to AC6, each a direct `selfcheck` run, a slice of `main()`, or a staged break.
- migration: N/A — no data shape changes.
- user docs: N/A — no user-facing `help/` surface; the note text is the documentation.

## 6. Acceptance criteria

- **AC1** — When the five slices of the govkit self-test's `main()` named in §4 run before the edit, the
  nineteen arms in §4's table fail. When they run after it, each slice prints zero failures,
  including the arms S4, S5 and S6 add.
  Red when: any slice prints a failure after the edit, or the before-run fails none of the nineteen.
  cost: about 715 s per state on node a, measured 2026-10-09; slice B is 471 s of it.
  fixture: the slice runner from §4, in the run's scratchpad, with a short temporary root under
  `%TEMP%`.
  figure: nineteen is PINNED as measured at 54ba9c0e; the before-run re-derives it.
- **AC2** — When `python tools/govkit/govkit.py selfcheck` runs on the real tree after the edit, it
  exits 0. Its `held self-test legs:` note names 59 graded, 22 shaped and the three exempt legs, and a
  non-zero population, and it carries no stand-down clause.
  Red when: the run exits non-zero, the note reads a zero, or the stand-down clause prints on gov.
  cost: about 141 s on node a.
  figure: DERIVED at observation; 59, 22, 3 and 61 were counted at 54ba9c0e and are not pinned.
- **AC3** — When slice B runs after the edit, the AC5 `selfcheck --write` arm passes on exit 1, the
  pin row `demo\trepo\tselftests`, and a line carrying `7j4: entry 'demo' gate leg 'demo'`. Stage
  7j4's subject test to pass every leg and re-run the slice, and that arm fails. Restore, and it
  passes.
  Red when: the arm passes with the subject test disabled, or fails on the restored tree.
- **AC4** — When slice B runs after the edit, S5's two arms pass, each naming its own 7j4 line. Stage
  the population count in `tools/govkit/govkit.py` to read zero always, and both arms fail. Restore,
  and both pass.
  Red when: either arm passes with the count forced to zero, or fails on the restored tree.
- **AC5** — When slices B and E run after the edit, the clean fixture's output carries
  `the zero-population reds stand down`, and the `[-6]` check sees exit 0 and
  `is absent, so no leg's chunk is known` on a tree whose descriptor declares gate legs. Stage the
  population condition away, so the reds bind everywhere again, and slice B's clean-fixture arms fail
  as they did before the edit. Restore, and they pass.
  Red when: a stand-down is silent, the absent-manifest case reds, or the staged break leaves slice
  B green.
- **AC6** — When every `selftests` chunk is taken out of `tools/gate-legs.json` in a copy of the
  edited tree, and `python tools/govkit/govkit.py selfcheck` runs there, 7j4 prints no refusal and
  its note carries the stand-down clause. 7h2 reds the moved chunk pins. The header comment above
  7j4 names both stand-downs and 7h2 as the cover.
  Red when: 7j4 refuses on that copy, 7h2 stays green, or the comment omits either stand-down.
  cost: one copy and one selfcheck, about 150 s.
  fixture: a copy made the way the govkit self-test's gov-copy block makes one (no `.git`, a fresh
  repo, one commit), under a short directory in `%TEMP%`.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms`

New arm: tools/govkit/selftest.py main, liveness block, 7j4 population present with zero graded and with zero shaped · covers AC4 · the population count forced to zero · none
New arm: tools/govkit/selftest.py main, ratchet block AC5, the 7j4 subject red on --write · covers AC3 · 7j4's subject test passing every leg · none
New arm: tools/govkit/selftest.py main, the clean fixture and the [-6] fixture announce each stand-down · covers AC5 · the population condition taken away · none

The guarded legs above are the ones whose guard, the govkit directory, the estimate's paths trip,
plus `govkit selfcheck`, which runs on every bar. No new function is added, so the lexicon and
codebase-map legs are not moved. The close runs these legs; no pass does.

## 8. Open questions

- **F1 — What population must exist for 7j4's zero-graded and zero-shaped reds to bind?**
  Four options were tested against the fixtures and the real tree, each by reading the fixture state
  each arm runs selfcheck on and the slice results in §4.
  (a) At least one manifest row in chunk `selftests`, the skeptic's fix. It turns every
  zero-shaped arm in slices A and B green, and keeps both reds on gov's 61-row tree.
  (b) Keep the reds whenever any leg was graded. It leaves all thirteen zero-shaped arms red, so it
  fails the criterion this unit exists for.
  (c) Drop both liveness reds and keep the note. It passes every fixture, but it gives up the
  broken-predicate red on gov's own tree, which `DEPL-aBenchedProbe-1` S4 set.
  (d) At least one manifest row the runner holds, by `subject == kit` or chunk `selftests`. The
  ratchet fixture's AC2 arm writes subject `kit` on a `true` leg with no chunk, so (d) reds it on
  zero shaped.
  Recommendation: (a). It is the only option that keeps gov's liveness red and fails no fixture.
  RESOLVED (agent, 2026-10-09, delegated): (a), a manifest row in chunk `selftests`.
- **F2 — What does 7j4 do when `tools/gate-legs.json` is absent?**
  (a) A note always, agreeing with 7h, 7c and 7c2, which grade nothing without the manifest.
  (b) The skeptic's fix: a note, unless some descriptor declares a `[[gate_leg]]`, and then a red.
  The discriminating test is the `[-6]` fixture in slice E. Its descriptor declares two gate legs,
  its tree has no manifest, and its arm asserts green. Under (b) it stays red, and repairing it
  means writing a manifest and a pin into another unit's fixture. Option (b) is also a third rule
  for an absent manifest, beside 7h's.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-09, delegated): (a), a note, whatever the descriptors declare.
- **F3 — Does the AC5 fixture keep subject `repo` and expect a red, or move to `kit` and stay green?**
  Keeping `repo` needs `selfcheck --write` to write the pin on a red run. Slice B observed that it
  does (§4). It also leaves a committed arm that observes 7j4's subject red. Moving to `kit`
  changes the pin row that AC5 asserts, and observes nothing new.
  Recommendation: keep `repo`.
  RESOLVED (agent, 2026-10-09, delegated): keep subject `repo`, and expect exit 1 with the 7j4 line.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The seam is 7c2's liveness clause in `selfcheck` in `tools/govkit/govkit.py`. It refuses a zero
only when the registry declares a root conf, and its comment says a refusal there "would red every
fixture that is not about this check". `tools/codebase-map/reuse_lookup.py` on "a liveness refusal
that binds only where the population it grades exists" returned no checker of this shape. Its top
hits were `refusal` in `tools/memory-recall/recall_conf.py` and `population` in
`tools/govkit/refusal_join.py`, and neither is a liveness gate. The arms are inline in `selfcheck`
and invisible to the symbol tier, so the seam was confirmed by reading source at lines 2486-2538 and
2667-2683. The 7j4 enumeration was re-run read-only through `load_registry`, `read_descriptors`,
`canonical_ctx` and `resolve_tokens`, and it agreed with `DEPL-aBenchedProbe-1`: 59 graded, 22 shaped,
3 exempt, 0 red. The recall probe returned the review record and this unit's brief. It also returned
the `DEPL-aTetheredConvoy-1` spec, whose precedence note does not red on a true zero "because
reddening on a true state is how a gate teaches people to waive it", and two gotcha classes,
`vacuous-selector-empty-population` and `liveness-negative-from-another-population`. The candidates
tested and rejected are in §8.

Recall terms used: `python tools/memory-recall/query.py "when should a selfcheck liveness red stand down on a scratch fixture tree with no population to grade" --terms "liveness zero population selfcheck fixture scratch gov manifest absent note refusal stand down vacuous"`
