**Serves:** diff-review DEPL-dBackdatedFixture-1 DEPL-dBackdatedFixture-2 DEPL-dBackdatedFixture-3

# dBackdatedFixture — closing diff review (BUILD-METHOD M8), round 2

*Node `d`, 2026-09-16. The Tier-2 adversarial pass over the FOLD that answered round 1
([round 1's record](2026-09-16-review-DEPL-dBackdatedFixture-1-closing-diff-round1.md), BLOCKED), not over
the build's diff again. The fold regenerates `memory/map/generated/symbols.json`, rewrites three comment
sites in `tools/govkit/selftest.py`, takes unit 1's spec to rev-4, changes one README word, and adds the
acceptance ledger for units 1 to 3 plus the round-1 record. The shape was four primed finder lenses
given round 1's six confirmed defects as `priorFindings`, then a skeptic stage in four batches prompted
to REFUTE each finding, then one synthesis. This synthesis re-read at source every claim the confirmed
findings rest on and re-ran the one test that closes round 1's blocker. The last section lists what it
re-read and what it did not run.*

**Round: 2.** Reviewed range: `2076d57a...ac3580ce`.

## Verdict: CLEAN WITH FIXES

The fold closes round 1's blocker. `memory/map/generated/symbols.json` now carries
`write_vintage_receipt`, and `python tools/codebase-map/test_codebase_map.py` exits 0 at `ac3580ce`. No
confirmed finding in this round is BLOCKER or HIGH. No arm's verdict changes, and no confirmed finding
says any mechanism fails to do what its spec promises. The fold did introduce four defects, all in text
it wrote. One is MEDIUM: inserting the new liveness `New arm:` line into unit 1 §7 re-pointed the AC3
line's "that same break" at a break that cannot red AC3. That brings back round 1's M1 class, and makes
§5's testing claim false again. The other three are LOW prose defects: two narrowed claims that
over-corrected or stayed half-narrowed, and one necessity claim the source contradicts.

**Review shape:** raw 11, confirmed 7, refuted 4, unverified 0, precision 0.64. That is above the ~0.5
floor `AGENTS.md` §8 sets. Three confirmed ids (2, 5, 8) are one defect reported by three lenses, and
two (4, 7) are one defect reported by two, so the confirmed set holds four distinct defects. For M8's
convergence predicate, the confirmed count is 7 against round 1's 8.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 4/4 returned, 0 DIED; 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. The run is complete on its
own terms. The pipeline's duplicate pass found none. Grouping ids 2, 5 and 8, and ids 4 and 7, is this
record's own editorial fold, as round 1 did. Each raw id takes the severity of the defect it evidences,
so the per-id table and the counts agree by construction.

**Adjudicated severities:** BLOCKER 0, HIGH 0, MEDIUM 3 ids (one defect), LOW 4 ids (three defects).

Severity meanings are round 1's, kept so one class carries one rating across the build's records:

- **BLOCKER.** The build's tip cannot land: the merge bar reds on it, or a landed arm cannot fail.
- **HIGH.** An arm grades something other than what its label says, but still catches part of its class.
- **MEDIUM.** A new arm landed without its failing case observed, or a named staged break cannot red it.
- **LOW.** Prose in code or in a record is false against the source. No arm's verdict changes.

Defect ids below carry an `R2-` prefix so they cannot be confused with round 1's B1, M1 and L1 to L4.

| Defect | Severity | Raw ids | Address |
|---|---|---|---|
| R2-M1 the AC3 `New arm:` line's "that same break" now names the descriptor break, which cannot red AC3 | MEDIUM | 2, 5, 8 | unit 1 spec §7 line 160 and §5 line 128 |
| R2-L1 the docstring's `level` versus DIFFERS example inverts under `update --to` | LOW | 3 | `selftest.py:232-233` |
| R2-L2 S4 says `apply` emits a source-less row "only when the selection declares an `lf_pin`" | LOW | 4, 7 | unit 1 spec §2 S4 lines 44-45 · `selftest.py:236-238` |
| R2-L3 the spec still promises a fixture a real adopter can hold, which round 1's L1 refuted | LOW | 10 | unit 1 spec H1 line 1, §1 line 23 · README generated row line 67 |

## Per-id severity table

| id | severity | defect | severity as the lens filed it |
|----|----------|--------|-------------------------------|
| 2 | MEDIUM | R2-M1 | medium |
| 5 | MEDIUM | R2-M1 | medium |
| 8 | MEDIUM | R2-M1 | medium |
| 3 | LOW | R2-L1 | low |
| 4 | LOW | R2-L2 | low |
| 7 | LOW | R2-L2 | low |
| 10 | LOW | R2-L3 | low |

No id moves from its lens filing. R2-M1 sits at the gentle end of MEDIUM. The AC3 arms WERE observed RED
under R2's rewind break, per the ledger at lines 23-26, so nothing is unobserved. Only the record names
the wrong break. It stays MEDIUM because round 1's scale names that exact case: "a named staged break
cannot red it".

## Round 1's findings — closed by the fold, or only re-worded

| Round 1 | Closed? | Evidence at `ac3580ce` |
|---|---|---|
| B1 symbol inventory stale | CLOSED | `symbols.json` gains the one `write_vintage_receipt` entry. This synthesis re-ran `test_codebase_map.py`, which exited 0 with no `FAIL` in 1.09 s. Unit 1 §7 line 156 names `codebase-map coverage + freshness`, spelled as `tools/gate-legs.json:619` spells it. Round 1's left-shift, the pre-commit fast leg, is not built. It was a suggestion, not a fix step. |
| M1 liveness arm never observed RED | CLOSED for the arm, with a new defect | The ledger at lines 19-22 records `FAIL [dBF] AC2 LIVENESS` under the descriptor break, and §7 line 159 names that break. The line was inserted above the AC3 line, which produces R2-M1. |
| L1 fixture called an install OLD could produce | CLOSED in code, with a new defect and a residue | `selftest.py:217` and the banner at `:687-689` now say what is and is not rewound. The replacement example at `:232-233` is R2-L1. The spec still carries the refuted claim, which is R2-L3. |
| L2 source-less branch unobserved for a false reason | PARTLY CLOSED | The docstring at `:236-238` says "whenever", which is true as a sufficient condition. The spec's S4 was rewritten into a necessity claim, which is false for `apply` and is R2-L2. The docstring's consequence sentence is true: without the `if not src` guard at `:251`, `src` is `None`, so `cat-file -e <vintage>:None` fails at `:254` and `:257` runs `git rm -q -f -- .gitattributes`. |
| L3 thirty red arms | CLOSED | `selftest.py:224` says twenty-seven over the two builders, and `:678` says 27. Both agree with unit 1 §2 S3 and AC4. |
| L4 no failing arm carried stderr | CLOSED | `selftest.py:224-225`, the banner at `:691-692` and README line 18 each say "most". |

**The acceptance ledger** (new in this fold) was read against the criteria it answers. Every
`**Evidences:**` line carries a backticked token that also appears in its criterion's text: unit 1's AC1
to AC4, unit 2's AC1 to AC3, and unit 3's AC1 to AC5. Each block numbers exactly the criteria its spec
§6 numbers, and the binding line is `**Serves:** journal` over all three ids. The observations
themselves agree with the spec criteria where they overlap. Unit 2's AC1 cites `govkit.py:6814`, which is
the `row["version"] = _resolve_ver_at(row)` line. Unit 2's AC2 records all three `[dGV-9]` arms `ok`
under R3, where the criterion requires two, which is a superset. Unit 1's AC4 matched all 30 baseline
labels where the criterion requires 27, also a superset. No confirmed finding contradicts a ledger
line. R2-M1 rests on one: the ledger at lines 20-22 is the evidence that the descriptor break leaves AC3
green.

**Disposition** follows BUILD-METHOD. The exit rule at line 140 disposes every confirmed finding by
severity. There is no BLOCKER or HIGH to promote. The MEDIUM and the three LOWs FOLD into unit 1's spec
as rev-5 with a §9 line, and R2-L1 and R2-L2's docstring half are comment edits in `selftest.py`. Folding
does not re-arm the loop. The fold is still text nobody has reviewed, and this round is the proof: every
defect it confirmed was written by round 1's fold. So the documented compensating check is a Tier-1
self-read of the rev-5 diff against this record before landing, and it costs no agents. Round 1's
fix step 4 still stands as a landing precondition: run the whole bar, not only the legs a spec names.

---

## R2-M1 — the AC3 `New arm:` line's "that same break" now names a break that cannot red AC3 (MEDIUM; ids 2, 5, 8)

**Address.** `memory/builds/dBackdatedFixture/spec/2026-09-16-spec-DEPL-dBackdatedFixture-1.md:160`.
The claim it falsifies is at §5 line 128.

**Finding.** Before the fold, §7 held two `New arm:` lines. The AC3 line's "staged RED by that same
break" pointed at the line above it: make `write_vintage_receipt` rewind an absent source instead of
dropping it. The fold answered round 1's M1 by inserting a new line 159 between them, for the AC2
liveness arm. Its break removes `check-wiring.fragment.json` from the check-wiring descriptor's
`include` and `claims`. Line 160 was left unchanged, so read in order, "that same break" now means the
descriptor break.

That break cannot red AC3. With the fragment out of the descriptor, `apply` never lands it, so
`_bf_drop` at `selftest.py:699` is empty and nothing is dropped or invented. S9 then has no row to
refuse, and `update` over either fixture exits 0, so the arms at `selftest.py:718` and `:3884` stay
`ok`. The fold's own ledger records exactly that at lines 20-22: under the descriptor break, "the other
four `[dBF]` arms `ok`". The `stale_target` AC3 arm at `:718` is one of those four. AC3 was observed RED
only under R2's rewind break, at ledger lines 23-26.

So §7 names a break that cannot red the arms it lists. §5 line 128 says "every new arm is observed RED on
a staged break named in §7", and as written that is false again for AC3. Anyone who re-stages AC3's
break from §7 would watch it stay green and conclude the arm cannot fail. This is round 1's M1 class,
brought back by the fold that closed M1. It is also the amendment-leaves-its-other-half-standing
shape: a line was added to an ordered list, and a later line that refers backward was not re-read.

**Fix.** Make line 160 name its break outright, with no positional back-reference: "`[dBF]` AC3
acceptance arms, staged RED by making `write_vintage_receipt` rewind an absent source instead of
dropping it". Moving the LIVENESS line below the AC3 line would also work, but it leaves the
back-reference in place for the next insertion. Log the correction in a rev-5 §9 line.

**Left-shift.** Gate the class. Add a check that refuses a spec §7 `New arm:` line which refers to another
line's break by position, such as "that same break", "the same break" or "as above". Every `New arm:`
line must name its own break. The predicate is text-shaped and costs nothing, and this spec's line 160
is its observed RED case before the fix lands. Run it over every tracked spec first and print the hits
and near-misses, as `AGENTS.md` §7 requires before wiring. Round 1's proposed cross-reference is still
open and would catch this too: for each label a §7 `New arm:` line names, the ledger shows that label
`FAIL` under the break the line names, or lists it NOT OBSERVED.

## R2-L1 — the docstring's `level` versus DIFFERS example inverts under `update --to` (LOW; id 3)

**Address.** `tools/govkit/selftest.py:232-233`: "`update`'s per-kit delta over this fixture reads
`level` where a real install at `24f39915` reads DIFFERS".

**Finding.** The sentence holds only when `update` runs at the pin. The per-kit delta at
`govkit.py:6507-6535` compares each kit's stored `version` with `resolve_entry_version_at(root, d,
to_commit)`. `apply` stamps the rows with HEAD's `KIT_CHECK_WIRING_VERSION`, and the helper never rewinds
`version`. This synthesis read the constant at each commit the fixtures touch: `24f39915` 1.0, `0f4d3084`
1.0, `372e6b2a` 1.0, `9ddcc5c9` 1.1, HEAD 1.3.

At the pin, the fixture's stored 1.3 meets gov's 1.3 and reads `level`. A real 24f39915 install stores
1.0 and reads DIFFERS, as the docstring says. But `delta_target` (`selftest.py:3860-3874`) uses the same
helper, and its consumer arms run `update --to` at `:3892`, `:3923`, `:3935` and `:3954`. At
`--to 372e6b2a` or `0f4d3084` the verdicts swap: the fixture reads DIFFERS, stored 1.3 against gov's 1.0,
and a real install reads `level`. At `--to 9ddcc5c9` both read DIFFERS. The lens reproduced the swap in a
scratch run, `check-wiring  level` with no `--to` and `check-wiring  DIFFERS — stored 1.3, gov has 1.0`
under `--to 372e6b2a`. This synthesis did not re-run it.

Round 1's L1 narrowing therefore replaced one inaccuracy with another, for half of the helper's callers.
The harm is small. The next sentence at `:234` still says an arm grading either field must rewind first.
But someone writing a version-delta arm over the `[-8]` fixtures would expect the opposite verdict.

**Fix.** Either drop the example and say only that the delta compares HEAD's `version` rather than the
vintage's. Or scope it: "at the pin, `update`'s per-kit delta reads `level` where a real install at
`vintage` reads DIFFERS; under `--to` it compares HEAD's version with gov's at `--to`, so the verdict can
invert, as it does for `delta_target`'s `--to 372e6b2a`." The first is shorter and cannot rot.

**Left-shift.** The gate is the fuller fix round 1's L1 named. Rewind `version` from
`resolve_entry_version_at` at `vintage` (`govkit.py:431`) and `oid` from `gk.blob_oid`, then add a `[dBF]`
arm comparing each kept row's `version` with the vintage's declared version. That removes the example's
subject. Without it, the documented check is to test an example of a verb's output over a shared helper's
fixture against every caller's invocation of that verb, `--to` included, not just the first caller.

## R2-L2 — S4 says `apply` emits a source-less row "only when the selection declares an `lf_pin`" (LOW; ids 4, 7)

**Address.** `memory/builds/dBackdatedFixture/spec/2026-09-16-spec-DEPL-dBackdatedFixture-1.md:44-45`
(§2 S4). The docstring at `tools/govkit/selftest.py:236-238` answers the same question differently.

**Finding.** `apply` computes its pins at `govkit.py:4608` over
`sorted(set(selection) | set((receipt or {}).get("kits") or []))`. That is the selection PLUS every kit the
existing receipt already claims, and the comment at `:4604-4607` says why: a narrower later apply must not
un-pin kits still installed. `if pins:` at `:4611` then appends the source-less `attributes` row at
`:4626`. Only `adopt` uses the selection alone, at `:8239`. So for `apply`, "only when the selection
declares an `lf_pin`" is a necessity claim the source contradicts. A re-apply of `check-wiring` over a
receipt that already claims a pinned kit emits the row with no pin in the selection.

The lens reproduced this on a scratch target. It applied `push-main`, which declares two `[[lf_pin]]` at
`push-main.kit.toml:69` and `:72`, committed with `settle`, then ran `apply --kits check-wiring`. That
printed `[2/ATTRIBUTES] 2 pin(s) [spliced]` and wrote a `.gitattributes` row with no `source`. This
synthesis read the source and the descriptor and did not re-run it.

Round 1's L2 fix said "whenever", and the docstring kept it. As a sufficient condition "whenever" is true,
though incomplete for `apply`. Only the spec was rewritten into "only when". The spec's conclusion still
holds: both builders apply `check-wiring`, which declares no `lf_pin`, to a fresh `make_target` with no
receipt, so neither fixture holds such a row. This is round 1's L2 class again: a NOT OBSERVED reason
that asserts an absence the source contradicts.

**Fix.** Reword S4 and make the docstring give the same answer: "`apply` emits a source-less
`attributes` row whenever the selection, or a kit its receipt already records, declares an `lf_pin`
(`govkit.py:4608`), and `adopt` whenever the selection does (`:8239`). Both builders apply check-wiring,
which declares none, to a fresh target with no receipt, so neither holds one."

**Left-shift.** Round 1's L2 left-shift arm is still unbuilt, and it would make the branch OBSERVED and
this reason moot. Extend it to the re-apply case. Apply a pinned kit, settle, apply `check-wiring`, run
`write_vintage_receipt`, and assert that the `attributes` row is unchanged in the receipt and
`.gitattributes` is still in the target's index. Without that arm, the documented check is to test a
claim about WHEN the engine emits a row against the condition that computes it (`:4608`, `:8239`), not
only against the row literal (`:4626`, `:8246`).

## R2-L3 — the spec still promises a fixture a real adopter can hold, which round 1's L1 refuted (LOW; id 10)

**Address.** Unit 1 spec H1, line 1: "the vintage fixtures model an install the old vintage could have
produced". The H1 is carried verbatim into the generated unit row at
`memory/builds/dBackdatedFixture/README.md:67`. Unit 1 spec §1, line 23: "This unit makes the two
fixtures model a state a real adopter can hold." Weaker: §4 line 112, "It models what every adopter who
installed `check-wiring` before 2026-09-14 holds."

**Finding.** Round 1's L1 found this claim false against the source. `version` and `oid` stay at HEAD, so
the fixture is not an install OLD could produce. The fold narrowed it only at the two addresses round 1
named, `selftest.py:217` and the banner, which now reads "HOLDS ONLY ROWS `OLD` SHIPPED". The spec that
owns the unit's promise, edited in the same fold, still makes it at H1 and at line 23. The code and the
spec now give two answers to what the fixture models. A later arm written against the spec's stated
contract would grade a receipt the spec misdescribes.

Two parts of the lens's report are weaker, and this record does not rest on them. Line 112 sits in the
§4 alternatives table, where it compares row populations across candidates A, B and C, and it is
defensible in that context. The rev-4 §9 line omits L1, but L1 named no spec address and §9 logs spec
changes, so that omission is by design.

**Fix.** Narrow line 23 to the helper's wording: the fixtures hold only rows OLD shipped, with `commit`,
`sha256` and `gov_oid` at OLD, and `version` and `oid` left at HEAD. Retitling the H1 is optional. If it
is retitled, re-render the README's `gen:build-units` block in the same commit, because that block is
generated from it. Log the change on the rev-5 §9 line alongside R2-M1 and R2-L2.

**Left-shift.** The documented check is that a fold narrowing a claim greps the claim's key phrase across
the whole build folder, meaning spec H1, §1, §4 and the README's generated rows, not only the addresses
the finding named. Record this build as an instance in `memory/gotchas/two-answers-to-one-question.md`,
and as a second instance in `memory/gotchas/fold-text-is-unreviewed-surface.md`. No gate is proposed,
because the claim is free text. `readme_mechanism_drift` reports only pairs spelled identically, and
the spec's wording and the helper's narrowed wording are not.

---

## What this round did not cover

**The refuted set.** This record was given the confirmed findings only. It cannot say what the four
refuted findings addressed, or whether any of them bore on a round-1 closure above.

**Round 1's unchanged code.** Out of scope by the brief. The diff reviewed is the fold alone.
`selftest.py` changed only in comments at `:217-240`, `:676-678` and `:687-692`, so no arm's predicate
was re-read for this round, beyond the lines R2-M1 and R2-L1 cite.

**Suite status.** The brief reports these, and this synthesis did not run them. A full `govkit selftest`
at `2076d57a` exited 0 with 1240 `ok` and 0 `FAIL`. The M1 liveness break was observed `FAIL`. The fold
changed only comments in `selftest.py`, so that green carries to `ac3580ce` for the suite. It says
nothing about the whole bar, which has not been run at `ac3580ce`.

**Observed, not adjudicated, not a finding.** The ledger's header at lines 5-9 describes four concurrent
suite runs, GREEN and R1 to R3. The descriptor-break observation at lines 19-22 came from a fifth run,
stopped early, which the header does not list. No lens or skeptic raised it. It does not change a
criterion's answer, and it is not counted above. The rev-5 fold may choose to name that run in the
header.

**Re-read at source by this synthesis:**

- The fold diff `2076d57a..ac3580ce` for every file, and round 1's record in full.
- `tools/govkit/selftest.py` at 215-270 (`write_vintage_receipt`), 670-720 (`stale_target` and the
  `[dBF]` arms), 3839-3842 (`V8`), 3860-3874 (`delta_target`), and the `update --to` call sites at 3892,
  3923, 3935, 3938 and 3954.
- `tools/govkit/govkit.py` at 3399-3411 (`lf_pins`), 4598-4632 (the `apply` pins and attributes row),
  6498-6540 (the per-kit version delta), 6808-6818 (the version refresh unit 2's ledger cites), and
  8230-8252 (the `adopt` pins and attributes row).
- `KIT_CHECK_WIRING_VERSION` at `24f39915`, `0f4d3084`, `372e6b2a`, `9ddcc5c9` and HEAD.
- `[[lf_pin]]` in `tools/govkit/entries/push-main.kit.toml` (two) and `check-wiring.kit.toml` (none).
- Unit 1 spec lines 1, 18-46, 105-160 and 176-183. Unit 2 and unit 3 spec §6. The acceptance ledger in
  full. README lines 14-20 and its generated unit table.
- `tools/gate-legs.json` leg names at 619, 1039 and 1052.
- `memory/HYGIENE.md` "Record bindings" and "Acceptance ledger". `memory/guides/BUILD-METHOD.md` at
  126-145 and M8.

**Run by this synthesis:** `python tools/codebase-map/test_codebase_map.py` in this worktree at
`ac3580ce`, with a clean tree. It exited 0 with no `FAIL` in 1.09 s.

**Not run here:**

- The suite, the whole bar, and every staged break named in the specs, the ledger or above.
- The scratch reproductions under R2-L1 and R2-L2. Both findings rest on the lens's run and on this
  synthesis's read of the source lines cited.
- The hunt for a positional back-reference predicate over other specs, proposed under R2-M1.
