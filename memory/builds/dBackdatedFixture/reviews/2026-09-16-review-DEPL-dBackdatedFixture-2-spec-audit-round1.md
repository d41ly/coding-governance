**Serves:** spec-audit DEPL-dBackdatedFixture-2 DEPL-dBackdatedFixture-3

# dBackdatedFixture — spec audit of DEPL-dBackdatedFixture-2 and DEPL-dBackdatedFixture-3, round 1

*Node `d`, 2026-09-16. A Tier-2 adversarial pass over the two specs that spec audit round 1 of
DEPL-dBackdatedFixture-1 PROMOTED under BUILD-METHOD M4, before any code. Unit 2 closes that record's
BLOCKER B1: the `[dGV-9]` version-refresh arms were disarmed by the fragment row that `update --write`
lands. Unit 3 closes its HIGH H1: the `u5a` check figures were derived from the side `check` reads. The
shape was four primed finder lenses, then a skeptic stage in five batches prompted to REFUTE each
finding, then one synthesis. The lenses hunted for five things. The first was criteria that cannot fail,
or whose named staged break cannot red the named arm. The second was whether `resolve_entry` at
`canonical_ctx` yields the population that `apply` writes and `check` counts. The third was whether the
pre-write `_held` set is taken at the right moment. The fourth was whether the `[dBF]` liveness arm is a
synthetic-value proof. The fifth was contradictions between the two specs, unit 1 rev-3 and the README.
This synthesis re-read at source every claim the confirmed findings rest on. The last section lists what
it re-read and what it did not run.*

**Round: 1.** The reviewed subjects, pinned at the blobs they were read at, are
`memory/builds/dBackdatedFixture/spec/2026-09-16-spec-DEPL-dBackdatedFixture-2.md@03322c6e9e114ebc837622c67b427804b46bf53a`
and
`memory/builds/dBackdatedFixture/spec/2026-09-16-spec-DEPL-dBackdatedFixture-3.md@b316bf809b453c32770ab38fdf313173a7798c3d`.

## Verdict: CLEAN WITH FIXES

Neither promoted mechanism is contested. No confirmed finding says unit 2's pre-write scoping fails to
close B1. None says unit 3's descriptor derivation fails to close H1. The defects are in how the specs
prove their own arms. The worst one is unit 2's only new arm label, the `[dBF]` liveness arm. §7 names
one staged break for it, and the spec's own AC2 and AC3 say the arm stays `ok` under that break. A build
that follows the spec therefore lands that arm without ever seeing it RED, which the build README
forbids. That is the same class as round 1's M1 on unit 1, repeated in the spec written to fold round 1.
Three lenses reported it independently. The other two defects are one claim in unit 2 that no output
line can show, and one unit-3 scope clause that names observers which cannot see it. All three fold
inside the specs, and none is a blocker or a high.

**Review shape:** raw 19, confirmed 5, refuted 14, unverified 0, precision 0.26. Precision is well under
the ~0.5 floor `AGENTS.md` §8 sets, and lower than round 1's 0.45 on unit 1. Any further round over
these specs should tighten lens priming, not add agents. Three of the five confirmed ids are one defect,
so the confirmed set holds three distinct defects.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. The run is complete on its
own terms. Where a hunt item below drew no confirmed finding, that zero comes from a full read by all
four lenses, not from a dead one. It is still a spec audit's zero: it grades what the documents say, not
what the built arms will do. The pipeline's duplicate pass found none. Grouping ids 1, 6 and 10 into one
defect is this record's own editorial fold, as round 1's was. Each raw id takes the severity of the
defect it evidences, so the per-id table and the counts agree by construction.

**Adjudicated severities:** BLOCKER 0, HIGH 0, MEDIUM 4 ids (two defects), LOW 1 id (one defect).

Severity meanings are round 1's, kept so the build's records grade on one scale:

- **BLOCKER.** A build that follows the spec lands a regression arm that cannot fail and reports it
  green. The spec must change before a unit is dispatched.
- **HIGH.** A criterion as written weakens an arm the spec promises to keep, but the arm still catches
  part of its class.
- **MEDIUM.** A claim is false against the source, or a named staged break cannot red what it names. An
  attentive builder still lands honestly, and the fix is a sentence or a named break.
- **LOW.** A scope clause names an observer that cannot see it.

Disposition follows BUILD-METHOD M4. Nothing here is a BLOCKER or a HIGH, so nothing is promoted. Every
finding folds into rev-2 of its spec with a §9 line.

| Defect | Severity | Raw ids | Spec address |
|---|---|---|---|
| M1 the `[dBF]` liveness arm has no staged break that reds it | MEDIUM | 1, 6, 10 | unit 2 §7 `New arm:` line · §6 AC2, AC3 · §2 S2 |
| M2 AC2's ok-case detail is unobservable, and §5's observability claim is false | MEDIUM | 2 | unit 2 §6 AC2 · §5 observability · §4 Data model |
| L1 the non-zero floor names four observers, and none can see it | LOW | 9 | unit 3 §2 S2 · §6 AC1-AC4 · §5 error/empty states |

## Per-id severity table

| id | severity | defect | severity as the lens filed it |
|----|----------|--------|-------------------------------|
| 1 | MEDIUM | M1 | medium |
| 6 | MEDIUM | M1 | medium |
| 10 | MEDIUM | M1 | medium |
| 2 | MEDIUM | M2 | medium |
| 9 | LOW | L1 | low |

No id moves from the severity the lens filed it at. M1 stays MEDIUM, not HIGH. AC1's own staged break
already observes the first two `[dGV-9]` arms red while the landed row is present in `install.json`, so
at build time the scoping is proven to exclude a real row even if the liveness arm were always true.
What an always-true liveness arm loses is the future signal §5's risks item describes: the fixture
quietly ceasing to exercise the scoping. That is real, and it is fold-sized.

---

## M1 — the `[dBF]` liveness arm has no staged break that reds it (MEDIUM; ids 1, 6, 10)

**Address.** Unit 2 §7, the single `New arm:` line; §6 AC2 ("under AC1's staged break it still reads
`ok`") and AC3 ("while the AC2 liveness arm reads `ok`"); §2 S2.

**Finding.** §7 carries one `New arm:` line for two arm groups: "`[dGV-9]` scoping and `[dBF]` liveness,
staged RED by deleting the `version` refresh at `govkit.py:6814`". TEMPLATE-SPEC's grammar for that
field is "what stages its failing case", one line per arm (`memory/TEMPLATE-SPEC.md:193`, `:376`). The
build README's fourth rule is that every new arm is observed RED on a staged break before it lands.

The source confirms that the named break cannot red the liveness arm. `govkit.py:6814` sets `version` on
a row the raw-write branch MOVES. The landed fragment row is built separately, by the unclaimed-source
path in the `for _dest, _row0` loop at `govkit.py:7166`. Its dict literal at `govkit.py:7289-7303` takes
`version` from its own `_resolve_ver_at({"kit": _eid})` call and never reaches line 6814. Deleting 6814
therefore still adds the row, `_added` is still non-empty, and the arm reads `ok`. AC2 and AC3 both say
exactly that. No other break is named anywhere in the spec. AC2's "Red when: the write adds no row"
names a condition, not a break that produces it. One skeptic reported running unit 1's drop semantics
over `verrefresh` locally: it printed `landed tools/check-wiring.fragment.json`, and `_added` held that
one path. This synthesis confirmed the mechanism by reading the code, not by running it.

The consequence is that `len(_added) > 0` could be hard-wired true, or `_added` could be taken over
every post-write row, and every check the spec names would still pass. The one genuinely new arm label
this unit adds would land never seen RED.

**Fix.** Split §7 into two `New arm:` lines.

1. Keep the 6814 deletion for the three `[dGV-9]` arms only: the scoping in S1 and the non-empty guard
   in S3.
2. Give the `[dBF]` liveness arm its own line, with a break that empties `_added`. The fixture-side
   break is unit 1's own §7 break: make `write_vintage_receipt` rewind the absent fragment source
   instead of dropping it. S9 then refuses `update --write`, nothing lands, and `_added` is empty.
   Placing `continue` at the top of the loop at `govkit.py:7166` is an equivalent product-side break.
   The arm-side break, taking `_held` from the receipt re-read AFTER the write, is worth staging too,
   because it is the regression AC2's second Red-when clause names.
3. Add to AC2: under that break, the liveness arm reads `FAIL`, and its detail carries what M2's fix
   puts there.

**Left-shift.** This is the second round running in this build where a §7 line names a break that
cannot red an arm it claims (round 1's M1 on unit 1). It is this build's dominant spec-audit class. No
grammar can trace a break to a predicate, so the gate is a documented spec-audit check. For each arm a
§7 `New arm:` line names, find every criterion that states that arm's reading under that same break. A
criterion saying `ok` under the line's own break is a contradiction on its face. A cheap, text-shaped
hygiene check could flag one: an AC that cites "AC<n>'s staged break" and says an arm "reads `ok`",
where that arm's label appears on the §7 line naming AC<n>'s break. The class belongs in
`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` as an instance, with this build as
"where it bit". Round 1 recommended that entry and it has not landed: no gotcha names this build yet.

## M2 — AC2's ok-case detail is unobservable, and §5's observability claim is false (MEDIUM; id 2)

**Address.** Unit 2 §6 AC2 ("reads `ok` and its detail names `tools/check-wiring.fragment.json`"); §5
observability ("a red names what the write did or did not add"); §4 Data model ("with the added paths in
its detail").

**Finding.** `check()` at `tools/govkit/selftest.py:186-191` prints `ok   {label}` on success and
appends the detail only on `FAIL`. AC2's clause "reads `ok` and its detail names the fragment path"
therefore shows up in no output line. It is not an observable result, which TEMPLATE-SPEC §6 requires.
The only way a builder could make that clause checkable is to put the fragment path literal into the
predicate, and §4's Alternatives rejects exactly that. The red case fails the other way. When the arm is
red, `_added` is empty, so a detail of "the added paths" prints an empty list. §5's promise that a red
names what the write did or did not add is false as designed. It names neither.

The skeptic weakened one part of the lens's impact claim, and this record keeps that correction. The
likeliest cause of a red liveness arm is S9 refusing the receipt, and unit 1's S2 fixture-acceptance arm
already carries `update`'s stderr. So the refusal would not go wholly unreported. The unobservable
criterion and the false observability claim still stand.

**Fix.** Delete "and its detail names `tools/check-wiring.fragment.json`" from AC2's ok case. If the
added path is worth recording, record it in the staged-RED observation, not in the arm. Make the arm's
detail carry the post-write receipt paths, `_held`, and `p.stdout + p.stderr` from the `update --write`
run, so a red names what was held, what was and was not added, and any refusal. Rewrite §5
observability to match.

**Left-shift.** This is the "the command does not print that" shape in
`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`. Add it as an instance. The
documented check is short: a criterion may assert on an arm's detail only in that arm's `FAIL` state,
because `check()` prints nothing else.

## L1 — the non-zero floor names four observers, and none can see it (LOW; id 9)

**Address.** Unit 3 §2 S2 ("asserts its figure is non-zero … Observed by AC1, AC2, AC3 and AC4"); §5
error / empty / loading states ("each figure carries a non-zero floor").

**Finding.** S2 carries two clauses: a non-zero floor, and a shape match against `check`'s stdout. Every
criterion it names runs over the three-row `u5a` install, where N = P = H = 3. AC4's break drops `check`'s
figures to 2 against an expectation of 3, so it reds on the mismatch, not on a zero. The floor matters
only when the descriptor resolves to no writes AND `check` prints a zero figure. That state is
reachable: over a receipt with no rows, `check` prints `integrity: 0/0` at `govkit.py:3136` and `sidecar:
0 line(s) compared against 0 hashed row(s)` at `govkit.py:3157`. Its only zero-guard is the DEAD PROBE
fail, which requires `n_prov` to be non-zero. No criterion puts in that state, so deleting the floor
changes no AC outcome and S2's observed claim is false as written. `TEMPLATE-SPEC.md:274` requires each
item to name its observing criterion or say `NOT OBSERVED`, and that check is shape-only, so this passes
silently. Round 1's L1 was the same class, and unit 1 rev-3 folded it as `NOT OBSERVED` in its S4.

**Fix.** Choose one of two options.

1. **Mark it.** Split S2's floor clause out and mark it `NOT OBSERVED`, with the reason: no fixture
   resolves the descriptor to zero writes. That matches how unit 1 rev-3 folded its S4.
2. **Observe it.** Add a criterion whose staged break empties `_w`, for instance by resolving a
   descriptor with no `[[files]]`, over an install that landed nothing. Observe each of the three arms
   read `FAIL`.

**Left-shift.** Under option 2, that criterion is the gate. Under option 1 the clause is a stated
invariant with no observer, and it says so. The class has now appeared in two units of one build. The
documented spec-audit check is: for each scope clause, name the fixture state that distinguishes it
from its absence, and confirm some named criterion reaches that state. A clause whose distinguishing
state no criterion reaches is `NOT OBSERVED`, whatever it claims.

---

## What this round did not cover

**Hunt items that drew no confirmed finding.** All four lenses returned, so each of these is a zero from
a full read. It is still a spec audit's zero. This record was not given the refuted set, so it cannot say
whether a lens raised one of these and a skeptic refuted it.

- Whether `resolve_entry` at `canonical_ctx("check-wiring")` yields the population that
  `apply --kits check-wiring` over `DEPLOY_FULL` writes and `check` counts. This covers the role split,
  `src`-less rows, and whether `check-wiring.test.sh`, which the descriptor includes as `role = "engine"`,
  is withheld as a self-test. Unit 3 §4 records three writes, all `engine`, all with a `src`, measured
  on `4cf0944d`. This synthesis read the descriptor, which agrees with that, and did not run the
  expansion or `apply`.
- Whether `_held` is taken at the right moment. `write_receipt_pin` (`selftest.py:113`) runs only after
  `apply` and rewrites only `gov_commit`, so it cannot move the `files` paths between the sentinel loop
  and `update --write`.
- Whether AC1's staged break in unit 2 is a synthetic-value proof. It deletes the real product write,
  not a constant, so it is not.
- Contradictions between the two specs, unit 1 rev-3 and the README.
- The edge declarations, where both units consume from unit 1.

**Re-read at source by this synthesis:**

- `tools/govkit/selftest.py` at 110-146 (`write_receipt_pin` and `run`), 184-191 (`check()`), 695-722
  (the `verrefresh` block) and 936-956 (the `u5a` arms).
- `tools/govkit/govkit.py` at 3060-3157 (the evidence loop, its zero-guard and the sidecar block), 6805-6817
  (the raw-write `version` refresh), 7165-7180 (the unclaimed-source loop head) and 7276-7303 (the
  landed row).
- `tools/govkit/entries/check-wiring.kit.toml`.
- Unit 1 rev-3 §2 S3 and S4, and its §7 `New arm:` lines.
- `memory/TEMPLATE-SPEC.md` at 193, 268-278 and 376.
- `memory/guides/BUILD-METHOD.md` M4.
- The build README and round 1's record on unit 1.

**Not run here:**

- The full suite, and any staged break named in either spec.
- The skeptic's local run of unit 1's drop semantics over `verrefresh`. The `_added` result quoted under
  M1 is as that stage reports it. This record confirmed the mechanism by reading the code.
- `resolve_entry` over the `check-wiring` descriptor, and `check` over a zero-row receipt. The zero-figure
  output under L1 is read from the f-strings at `govkit.py:3136` and `3157`, not observed.
