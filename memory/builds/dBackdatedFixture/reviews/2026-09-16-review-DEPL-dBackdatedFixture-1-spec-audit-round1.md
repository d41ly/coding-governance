**Serves:** spec-audit DEPL-dBackdatedFixture-1

# dBackdatedFixture — spec audit of DEPL-dBackdatedFixture-1, round 1

*Node `d`, 2026-09-16. A Tier-2 adversarial pass over this build's one spec, before any code (BUILD-METHOD
M4). The shape was four primed finder lenses, then a skeptic stage in five batches prompted to REFUTE
each finding, then one synthesis. The owner's mandate was to decide which side of the 30-arm
`govkit selftest` failure at `4cf0944d` is wrong, fix it with a regression arm staged RED, and confirm
the suite passes in full. The spec answers "the arms", and this pass audits that answer. The lenses
hunted for criteria that cannot fail or cannot be observed, staged breaks that prove a mechanism only
for a synthetic value, scope items no criterion observes, contradictions between sections, and
unstated assumptions about the arms that consume the two backdating fixtures. The synthesis re-read at
source every claim the blocker and the high below rest on. The last section lists what it re-read and
what it did not run.*

**Round: 1.** The reviewed subject, pinned at the blob it was read at, is `memory/builds/dBackdatedFixture/spec/2026-09-16-spec-DEPL-dBackdatedFixture-1.md@39dfc1bb79e443de6dc37642150c78ecdc1e31c8`.

## Verdict: BLOCKED

One defect blocks the unit, and it is the one S4 says cannot happen. Section 4 chooses option A. Under
A, `update --write` lands `tools/check-wiring.fragment.json` as a new row inside the `verrefresh`
fixture, and that row alone satisfies all three `[dGV-9]` predicates. A build that follows the spec
therefore turns two of the 30 red labels green by disarming them. Those arms guard `update` refreshing
`version` on a row it moves, and they stay green with that refresh deleted. AC5 reads only `ok` labels,
so it reports the result as a pass. Four lenses found this independently, and the skeptic stage
measured it. One high comes at the same promise from the other side: S2 and AC3 derive the expected
`check` figures from the artefacts `check` itself reads, so a receipt that loses a row moves both sides
together. Five more defects are fold-sized, four medium and one low. No confirmed finding contests the
diagnosis. The engine is right and the fixtures are wrong, and nothing here reopens that.

**Review shape:** raw 31, confirmed 14, refuted 17, unverified 0, precision 0.45. Precision is under the
~0.5 floor `AGENTS.md` §8 sets, so round 2 should tighten lens priming rather than add agents. The
survivors show where to tighten: ten of the fourteen confirmed ids are three defects that several
lenses each reported, so round 2 needs sharper lenses, not a wider fan.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. The run is complete on its
own terms. So where a hunt item below drew no confirmed finding, that zero comes from a full read by all
four lenses and not from a dead one. It is still a spec audit's zero: it grades what the document says,
not what the built mechanism will do. The pipeline's duplicate pass found none. Grouping the fourteen
ids into seven defects is this record's own editorial fold. Each raw id takes the severity of the defect
it evidences, so the per-id table and the counts agree by construction.

**Adjudicated severities:** BLOCKER 4 ids (one defect), HIGH 1 id (one defect), MEDIUM 8 ids (four
defects), LOW 1 id (one defect).

Severity meaning in this record:

- **BLOCKER.** A build that follows the spec lands a regression arm that cannot fail and reports it
  green. The spec must change before a unit is dispatched.
- **HIGH.** A criterion as written weakens an arm the spec promises to keep, but the arm still catches
  part of its class. It is fixable inside the spec.
- **MEDIUM.** A claim is false against the source, or a named staged break cannot red what it names.
  An attentive builder still lands honestly, and the fix is a sentence or a named break.
- **LOW.** A scope clause names an observer that cannot see it.

Disposition follows BUILD-METHOD M4. This is round 1, so every finding folds into rev-2 with a §9 line,
and round 2 measures the fold. A BLOCKER or HIGH still standing when the rounds exit is promoted to a
unit, not folded.

| Defect | Severity | Raw ids | Spec address |
|---|---|---|---|
| B1 option A disarms the `[dGV-9]` version-refresh arms | BLOCKER | 1, 8, 16, 24 | §4 Alternatives rejected row A · §2 S1, S4 · §6 AC5 |
| H1 the `check` figures are derived from the side `check` reads | HIGH | 25 | §2 S2 · §6 AC3 |
| M1 one staged break cannot red the sidecar arm | MEDIUM | 4, 11, 17 | §6 AC3 · §7 second `New arm:` line · §5 testing |
| M2 S3 promises an outcome no mechanism delivers | MEDIUM | 6, 9, 21 | §2 S3 · §6 AC4 · §3 fourth non-goal · README expected improvement 3 |
| M3 the record cited as ratifying the landing says the opposite | MEDIUM | 26 | §3 first non-goal · §10 · README build-level rule 3 |
| M4 the helper's name reds the lexicon leg | MEDIUM | 28 | §4 Data model, Inventory · §7 |
| L1 the source-less clause has no observer | LOW | 15 | §2 S1 |

## Per-id severity table

| id | severity | defect | severity as the lens filed it |
|----|----------|--------|-------------------------------|
| 1 | BLOCKER | B1 | high |
| 8 | BLOCKER | B1 | high |
| 16 | BLOCKER | B1 | high |
| 24 | BLOCKER | B1 | high |
| 25 | HIGH | H1 | high |
| 4 | MEDIUM | M1 | medium |
| 11 | MEDIUM | M1 | medium |
| 17 | MEDIUM | M1 | high |
| 6 | MEDIUM | M2 | medium |
| 9 | MEDIUM | M2 | high |
| 21 | MEDIUM | M2 | medium |
| 26 | MEDIUM | M3 | medium |
| 28 | MEDIUM | M4 | medium |
| 15 | LOW | L1 | low |

Three ids move from the lens's severity. The four B1 ids rise from high to BLOCKER. They were measured
rather than reasoned, and they describe the exact green-by-absence outcome the owner's "confirm the
suite passes in full" cannot tell apart from a real pass. Ids 17 and 9 fall from high to MEDIUM. M1's
arm is already bound by the build rule that every new arm is observed RED, and M2 misstates an outcome
without disarming any arm.

---

## B1 — option A disarms the `[dGV-9]` version-refresh arms (BLOCKER; ids 1, 8, 16, 24)

**Address.** Spec §4 Alternatives rejected, candidate A and the paragraph choosing it; §2 S1's drop
branch and S4's "with no arm weakened"; §6 AC5.

**Finding.** The `verrefresh` block at `tools/govkit/selftest.py:705-722` works in four steps:

1. It builds a fixture with `stale_target`.
2. It overwrites every receipt row's `version` with `STALE-SENTINEL`.
3. It runs `update --write`.
4. It grades `_moved`, meaning every row whose `version` is no longer the sentinel, with three arms:
   `len(_moved) > 0`, `any("KIT_CHECK_WIRING_VERSION" in version)`, and `all(commit and sha256)`.

DEPL-dGaugedVintage-9 S1 wrote those arms to catch `update` failing to refresh `version` on a row it
moves. The writes they guard are `row["version"] = _resolve_ver_at(row)` at `govkit.py:6814`, `6950`
and `7069`. Under option A the fragment row is dropped before the sentinel loop ever runs, so
`update --write` lands it through the unclaimed-source path at `govkit.py:7289-7303`. That path appends
a row carrying these fields:

- `version: _resolve_ver_at({"kit": _eid})`, which is the same `KIT_CHECK_WIRING_VERSION=` source line
  a refreshed row gets;
- `sha256`, `gov_oid` and `commit`.

That row never held the sentinel, so it enters `_moved` by itself and satisfies all three predicates.
The skeptic stage measured this on a scratch clone, with `govkit.py:6814` staged as `pass`. Both
surviving rows stayed at `STALE-SENTINEL`. The landed row carried `KIT_CHECK_WIRING_VERSION=1.3` with
`commit` and `sha256` set. All three predicates came out True.

At `4cf0944d` the S9 refusal leaves `_moved` empty. The first two arms therefore fail and are among the
30 labels, while the third, an `all()` over an empty list, passes vacuously. AC5 would read the two
labels `ok` again, and the build would report a disarmed arm as fixed. Section 4 counts "puts the
landing path under the arms that already run" as a benefit of A. It never asks which of those arms the
landed row now satisfies, and no criterion attached to S4 could see the loss.

**Fix.**

1. Add a scope item: the `[dGV-9]` population is the rows the receipt held BEFORE the write. That is
   either the `kept` list the rewind helper returns or the receipt's paths read just before
   `update --write`, never every non-sentinel row.
2. Add a criterion with a liveness half. After the write, the landed `tools/check-wiring.fragment.json`
   row must be present in the receipt AND absent from `_moved`, so the exclusion is exercised and not
   vacuous.
3. Stage it RED by deleting the `version` write on the branch the fixture takes (`govkit.py:6814`, as
   measured). The first two `[dGV-9]` arms must go red while the landed row is still present. The third
   arm is an `all()` over the same list and is vacuously true once `_moved` is empty, so it cannot red
   on this break. That weakness predates this spec. This record notes it and does not count it. The
   fold can add a non-empty guard to that arm at no cost.
4. Rewrite S4 so it names every arm whose population a dropped-then-landed row changes, and states for
   each one whether it still grades what it was written for. At minimum that is `[dGV-9]`, the u2a
   second-run `current` arm, and the `[-12]` AC9 `missing` arm. Id 8 listed the last two, and this
   record did not re-read them.
5. Record in §4 that option A widens the population of every arm that reads `rec["files"]` after a
   `--write`.

**Left-shift.** The regression gate for this instance is item 2's liveness criterion together with item
3's staged break. The class is a fixture change that silently widens a population an existing arm
quantifies over. It is the neighbour of `memory/gotchas/vacuous-selector-empty-population.md`, and it
belongs there, or in a sibling gotcha, with this build as its "where it bit". The rule is that every
arm reading the receipt after a writing verb is re-staged RED against the product behaviour it guards,
never only against the fixture. `gotchas.py --for-diff` then puts it in front of the next diff that
touches `tools/govkit/selftest.py`.

## H1 — S2 and AC3 derive the `check` figures from the side `check` reads (HIGH; id 25)

**Address.** §2 S2; §6 AC3, its inputs and its "Red when".

**Finding.** AC3 derives the expected `integrity:`, `provenance:` and `sidecar:` figures from three
inputs: the target's files, `git rev-parse` over the receipt rows' `commit:source`, and `install.sums`.
All three are outputs of `apply`. `check` counts from the same receipt rows (`govkit.py:3071-3137`) and
the same sidecar (`govkit.py:3144-3157`). Suppose `apply` stops landing and recording one descriptor
file. Target, receipt and sums then shrink together, `check` prints `2/2`, the arm derives 2, and the
arm stays green.

The typed literal the spec removes was crude and is now stale, but it was the one thing tying the
figure to what the descriptor ships. That tie is the contract DEPL-aTetheredConvoy-5 S11 wrote for
these loops: "The expectation comes from the descriptors, not from the receipt". `check` itself reds
only at zero. S2 as written therefore removes a class of red the three arms had, which contradicts S4.
AC3's only staged break, skipping a row inside `check`'s own loop, never exercises a shrink on the
receipt side.

**Fix.** Derive the expected engine-row count from the `check-wiring` descriptor at the pin, through
`govkit_module()` (`resolve_entry` or `expand_rules` over `tools/govkit/entries/check-wiring.kit.toml`),
and never from an artefact `apply` wrote. Keep the non-zero floor. Add a second staged break that
removes one row from the fixture's receipt, its `install.sums` and its index before `check` runs, and
observe each of the three arms red.

**Left-shift.** That added staged break is the regression gate. The class is
`memory/gotchas/assertion-between-two-derived-values.md`, which already exists. The fold should cite it
in AC3 so the builder reads it before writing the derivation.

## M1 — one staged break cannot red the sidecar arm (MEDIUM; ids 4, 11, 17)

**Address.** §6 AC3 "Red when"; §7's second `New arm:` line; §5 testing ("each new or rewritten arm is
observed RED on a staged break").

**Finding.** §7 names one break for all three `u5a` arms: "skipping one engine row in `check`'s integrity
loop". The `integrity:` and `provenance:` counters (`n_engine`, `n_ok`, `n_prov`, `n_prov_ok`) are
incremented inside `for row in rows` (`govkit.py:3073-3137`), so that break moves both. The `sidecar:`
note is computed after the loop from `len(sums)` and
`len(want_pairs = {(sha256, path) for f in rows})` (`govkit.py:3144-3157`). A `continue` inside the loop
touches neither, so the line still reads `3 ... 3` and a derived sidecar arm stays green. That arm would
land without ever being seen RED, against §5 and against the build README's rule. This compounds H1: a
sidecar derivation that re-reads `install.sums` and the receipt rows is `check`'s own computation run a
second time, and with no break observed RED nothing would expose that. AC3 also never states what
population each of its three derived counts covers.

**Fix.** Split §7's line into one `New arm:` line per figure, each naming the break that reds it. For
the sidecar figure, a candidate break is dropping one parsed line from `sums`, or one pair from
`want_pairs`, in `check`'s sidecar block. In AC3, state the population behind each count: engine-role
rows for integrity, engine rows carrying both `source` and `commit` for provenance, and `install.sums`
as a set of (hash, path) pairs for the sidecar.

**Left-shift.** A documented spec-audit check, since no grammar can trace a break to a predicate: for
each staged break a §7 line names, trace it to the predicate of EVERY arm the line claims it reds. The
nearest existing class is `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`, and
this belongs there as a second instance.

## M2 — S3 promises an outcome no mechanism delivers (MEDIUM; ids 6, 9, 21)

**Address.** §2 S3's last sentence; §6 AC4; §3's fourth non-goal; the build README's third expected
improvement ("one arm naming the refusal, not 27 arms blaming the probe").

**Finding.** `check()` at `tools/govkit/selftest.py:186-191` appends to `FAILURES` and prints. It never
stops the run. Nothing in S1-S3 or §4 makes a downstream arm depend on the new acceptance arm, and the
fourth non-goal explicitly keeps their stdout-only details. Under AC1's staged break, which reproduces
the baseline refusal, the acceptance arm fails and every consumer of the refused fixture fails with it,
each still printing only the measurer's `UNVERIFIED` line. Those consumers are the arms at
`selftest.py:641-830` and `2654-2920`. The owner would get N+1 FAIL lines where the baseline gave N. S3's
"no longer fails a spread of downstream arms" and README improvement 3 describe something the design
does not do.

AC4 cannot observe the promise either. It grades one arm's rc and stderr over one `stale_target`
fixture, does not cover `delta_target`, and fixes no emission position relative to the first consumer
arm. The new FAIL line can therefore print after the first misleading one.

**Fix.** Choose one of two options:

1. **Reword.** S3 and README improvement 3 say what is built: one added arm whose detail carries stderr
   and names the refusal. If appearing first is the point, AC4 requires the arm to run before the first
   consumer arm, over both `stale_target` and `delta_target`.
2. **Add a mechanism.** Run the read-only acceptance `update` inside both fixture builders right after
   `settle`. On refusal, emit one FAIL carrying stderr and have the dependent arms print an announced
   skip. Add a criterion that, under the staged break, exactly one FAIL line names `REFUSING`.

**Left-shift.** Under option 2, the one-FAIL criterion is the gate. Under option 1 there is no machine
gate for a claim in prose, so this spec-audit record is the check.

## M3 — the record cited as ratifying the landing says the opposite (MEDIUM; id 26)

**Address.** §3's first non-goal ("`update --write` landing an unclaimed source (`TOOL-aScouredKit-25`)
is ratified"); §10 ("Recall confirmed … `TOOL-aScouredKit-25`, both ratified"); the build README's
third build-level rule.

**Finding.** The cited backlog row sits at `memory/backlog/TOOL.md:331`. It is CLOSED, its text reads
"`govkit update` CANNOT LAND A SOURCE GOV STARTED SHIPPING", and it was closed as a DUPLICATE of
TOOL-aFlaggedScaffold-3. That row, at `TOOL.md:36`, is still OPEN with the same can-not-land claim. The
record that actually ratified and built the landing is DEPL-dRatifiedSeam-1 S3, which is CLOSED and
landed at `3fe56d56` ("update lands a source the receipt never named"). It was built under the owner
ruling DEPL-dRetiredFork-13, which superseded the invariant. The non-goal still holds on the evidence:
§4's probe shows the landing working. Its justification, though, cites a record that says the reverse.
BUILD-METHOD M5 asks §10 to record where a recall hit and the source disagree, and §10 reports this hit
as "confirmed".

**Fix.** Cite DEPL-dRatifiedSeam-1 S3 at `3fe56d56` and DEPL-dRetiredFork-13 in §3, §10 and the README
rule. In §10, record that the recall hit and the still-OPEN duplicate disagree with the source. Record
the reconciliation of TOOL-aFlaggedScaffold-3 as a follow-up, either an annotation or a close naming
`3fe56d56`, so the next recall does not return the same wrong answer. That edit is not this unit's
mechanism, and folding it in would widen the unit.

**Left-shift.** The class is `memory/gotchas/two-answers-to-one-question.md`. A drift-audit signal is
worth considering: an OPEN backlog row whose headline claim is contradicted by a CLOSED spec's landed
commit. Any such signal needs the liveness assertion `AGENTS.md` §7 requires.

## M4 — the helper's name reds the lexicon leg (MEDIUM; id 28)

**Address.** §4 Data model and Inventory (`rewind_receipt`); §7, which names only `govkit selftest`.

**Finding.** `python tools/lexicon/lexicon.py --suggest rewind_receipt --as py.function` answers that
`rewind` is not in the declared table (re-run here). The `lexicon naming predicates` leg grades
definitions in `tools/govkit/selftest.py`, and the skeptic stage's `--list` showed `stale_target:615` and
`make_target:215` among them. It is pinned at `VERB_OFFENDER_PIN="983"` (`.lexicon.conf:195`). The spec
adds one new function and removes none, because the loops it replaces are inline, so the count goes to
984 and the leg reds. §7 does not name that leg. Units run no gates, so the red would first appear at
the post-build bar. `.lexicon.conf:193` records the same precedent for TOOL-aReplayedCard-2's helpers
`shipped_at` and `apply_all`, which measured 985 and were renamed.

**Fix.** Name the helper with a declared verb. `write_vintage_receipt` and `set_receipt_vintage` both
return OK from `--suggest` for `py.function` (re-run here). Add `lexicon naming predicates` to §7.

**Left-shift.** The leg is already the gate, and the gap is only that the spec named no leg. A
documented spec-audit check covers it: run `--suggest` over every definition §4 Inventory names. The
nearest class is `memory/gotchas/naming-leg-grades-what-python-named.md`.

## L1 — the source-less clause has no observer (LOW; id 15)

**Address.** §2 S1: "A row with no `source` is left untouched … Observed by AC1 and AC2."

**Finding.** `apply --kits check-wiring` writes receipt rows from the descriptor's three claims, and
every row writer in `govkit.py` sets `source` (the skeptic cited 4701, 4719, 4783 and 8122). Neither
fixture ever holds a row without one. AC1 grades rows carrying `commit` and `gov_oid`, and AC2 grades
rows whose source is absent at `24f39915`. Neither can tell a helper that leaves source-less rows alone
from one that rewrites or drops them.

**Fix.** Either delete "Observed by AC1 and AC2" from the clause, or add a helper-level arm that feeds a
row with no `source` through the helper and asserts it comes back byte-identical.

**Left-shift.** If the arm is added, it is the gate. Otherwise the clause is a stated invariant with no
observer, and it should say so.

---

## What this round did not cover

**Hunt items that drew no confirmed finding.** Because all four lenses returned, each of these is a zero
from a full read, but it is a spec audit's zero. This record was not given the refuted set, so it cannot
say whether a lens raised one of these and a skeptic refuted it.

- Whether AC2's liveness half reds for no defect.
- Whether a `govkit.py` defect is being wrongly excluded. M3 corrects the citation only, not the
  exclusion.
- Whether AC1's staged break proves the mechanism only for a synthetic value. The break reproduces the
  baseline's empty-blob `gov_oid`, which is the real failing state.

**Re-read at source by this synthesis:**

- `tools/govkit/selftest.py` at 186-191 (`check()`), 610-660 (`stale_target` and the u2a arms),
  690-725 (`[dGV-9]`), 936-956 (the `u5a` arms) and 3751-3777 (`delta_target`).
- `tools/govkit/govkit.py` at 3066-3157 (the evidence loop and the sidecar block), the three
  `version` writes at 6814, 6950 and 7069, and 7278-7303 (the landing row).
- `memory/backlog/TOOL.md` rows 36 and 331.
- DEPL-aTetheredConvoy-5 S11.
- DEPL-dRatifiedSeam-1 S3 and its status line.
- `.lexicon.conf` lines 193 and 195, and `lexicon.py --suggest` for three names.

**Not run here:**

- The full suite.
- The spec's §4 option-A probe.
- The skeptic stage's `verrefresh` measurement. B1's True/True/True is as that stage reports it. This
  record confirmed the mechanism by reading the code, not by running it.
- `lexicon.py --check`. The 983 figure is the pin as read, and 984 is the skeptic's measurement.
- The consumer arms id 8 names beyond `[dGV-9]`: the u2a second-run `current` arm and the `[-12]` AC9
  `missing` arm.

**Noticed while re-reading, not a finding:** `delta_target`'s `def` is at `selftest.py:3751`. The
spec's §10 cites 3754, which is its docstring. Fold that with the rev-2 edits.
