**Serves:** diff-review DEPL-dBackdatedFixture-1 DEPL-dBackdatedFixture-2 DEPL-dBackdatedFixture-3

# dBackdatedFixture — closing diff review (BUILD-METHOD M8), round 1

*Node `d`, 2026-09-16. The Tier-2 adversarial pass over the cumulative diff of the build's three Tier-2
units, all in `tools/govkit/selftest.py`. The rest of the diff is `memory/` records. Unit 1 (`cfa7e6d9`)
replaces the two inline receipt-rewind loops with `write_vintage_receipt`, which drops rows the vintage
never shipped. Unit 2 (`879d502c`) scopes the `[dGV-9]` version-refresh arms to rows held before
`update --write`. Unit 3 (`2076d57a`) derives the `u5a` check figures from the descriptor. The shape was
four primed finder lenses, then a skeptic stage in four batches prompted to REFUTE each finding, then
one synthesis. The lenses took the M6 bug-class checklist for this range as their brief. This synthesis
re-read at source every claim the confirmed findings rest on and re-ran the one blocker's reproduction.
The last section lists what it re-read and what it did not run.*

**Round: 1.** Reviewed range: `4cf0944dbdce94714870f26760936bc5edabc64e...2076d57a`.

## Verdict: BLOCKED

The build's tip cannot land as committed. Unit 1 added a module-level function and did not regenerate
the codebase map's symbol inventory, so the unguarded `codebase-map coverage + freshness` leg reds on
every bar, including the one `.githooks/pre-push` runs. The fix is one regeneration command. No
confirmed finding says any of the three mechanisms fails to do what its spec promises. The suite's own
arms were not shown to grade the wrong population. The remaining defects are one unit-1 arm landed
without an observed failing case, and four places where comments or records state something false
against the source.

**Review shape:** raw 11, confirmed 8, refuted 3, unverified 0, precision 0.73. That is well above the
~0.5 floor `AGENTS.md` §8 sets, so the lens priming held. Two pairs of confirmed ids are the same defect
reported by two lenses, so the confirmed set holds six distinct defects.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 4/4 returned, 0 DIED; 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. The run is complete on its
own terms. Where a hunt item below drew no confirmed finding, that zero comes from a full read by all
four lenses, not from a dead one. The pipeline's duplicate pass found none. Grouping ids 5 and 8, and ids
3 and 7, is this record's own editorial fold. Each raw id takes the severity of the defect it evidences,
so the per-id table and the counts agree by construction.

**Adjudicated severities:** BLOCKER 2 ids (one defect), HIGH 0, MEDIUM 1 id (one defect), LOW 5 ids (four
defects).

Severity meanings for this closing review:

- **BLOCKER.** The build's tip cannot land: the merge bar reds on it, or a landed arm cannot fail.
- **HIGH.** An arm grades something other than what its label says, but still catches part of its class.
- **MEDIUM.** A new arm landed without its failing case observed, or a named staged break cannot red it.
  The arm may be correct, but nothing has shown that it can fail.
- **LOW.** Prose in code or in a record is false against the source. No arm's verdict changes.

| Defect | Severity | Raw ids | Address |
|---|---|---|---|
| B1 the symbol inventory was not regenerated, so the codebase-map leg reds | BLOCKER | 5, 8 | `selftest.py:215` · `memory/map/generated/symbols.json` · unit 1 §7 |
| M1 unit 1's liveness arm has never been observed RED | MEDIUM | 11 | `selftest.py:700` · unit 1 §5 and §7 · acceptance ledger |
| L1 the fixture is called an install OLD could produce, but two row fields stay at HEAD | LOW | 2 | `selftest.py:217` and `:679` |
| L2 the source-less branch is unobserved for a reason the source contradicts | LOW | 3, 7 | `selftest.py:230` · unit 1 §2 S4 |
| L3 two comments attribute all thirty red arms to the fixture refusal | LOW | 4 | `selftest.py:224` and `:670` |
| L4 two comments and the README say no failing arm carried stderr | LOW | 10 | `selftest.py:224` and `:683` · build README line 18 |

## Per-id severity table

| id | severity | defect | severity as the lens filed it |
|----|----------|--------|-------------------------------|
| 5 | BLOCKER | B1 | blocker |
| 8 | BLOCKER | B1 | blocker |
| 11 | MEDIUM | M1 | low |
| 2 | LOW | L1 | low |
| 3 | LOW | L2 | low |
| 7 | LOW | L2 | low |
| 4 | LOW | L3 | low |
| 10 | LOW | L4 | low |

Id 11 moves from low to MEDIUM. It is the class round 1's spec audit rated MEDIUM when it found the same
gap in unit 2's liveness arm (that record's M1). The build README also binds it as a rule: "Every new
arm is observed RED on a staged break before it lands." One scale for one class across the build's
records outweighs the lens's filing.

**Disposition** follows BUILD-METHOD. M8 says to fix every blocker and then re-review the FIX, not the
diff again. The exit rule at BUILD-METHOD line 140 promotes a BLOCKER to a unit whose mechanism closes
it, audited as a SPEC, and folds a MEDIUM or LOW into its spec as a rev-N bump with a §9 line. Round 2,
if one runs, starts from this round's recorded tip, `2076d57a`. Four of the five non-blocker fixes are
edits to `selftest.py` comments as well as to spec prose, so the fold touches code the next round
measures. The fold-text-is-unreviewed-surface class applies to it.

---

## B1 — the symbol inventory was not regenerated, so the codebase-map leg reds (BLOCKER; ids 5, 8)

**Address.** `tools/govkit/selftest.py:215`, the new module-level `def write_vintage_receipt`, and
`memory/map/generated/symbols.json`. Unit 1 §7, whose gate list omits the leg.

**Finding.** The codebase map's generated symbol inventory enumerates module-level functions. Unit 1
added one and did not run `gen_map.py --write`. Both lenses reproduced the result on a clean clone. At
`4cf0944d`, `python tools/codebase-map/test_codebase_map.py` exits 0. At `2076d57a` it exits 1 with
`FAIL test_generated_artifacts_are_fresh` and `STALE symbols.json`. Regenerating adds exactly one entry:
`{id: write_vintage_receipt, kind: function, file: tools/govkit/selftest.py}`.

This synthesis re-ran the test in this worktree, whose only local changes are staged `memory/builds/`
records. It printed the same `FAIL` and `STALE` lines, exited 1, and took 1.15 s. A grep of
`memory/map/generated/symbols.json` finds no `write_vintage_receipt`. In `tools/gate-legs.json` the leg
`codebase-map coverage + freshness` has `subject: repo` and no `guard`, so every bar runs it, including
the pre-push bar. `.githooks/pre-commit` does not run it, which is why three commits landed past it.

The acceptance ledger's GREEN run exited 0 with no `FAIL`, but that run is `govkit selftest` alone. Every
spec's §7 names only `govkit selftest` and `lexicon naming predicates`. A green suite is not a green bar.
The owner rule that units run no gates means the build-end bar would have caught this before a push.
As committed, though, the tip reds and `.githooks/pre-push` blocks it.

**Fix.**

1. Run `python tools/codebase-map/gen_map.py --write` and commit the regenerated
   `memory/map/generated/symbols.json`.
2. Re-run `python tools/codebase-map/test_codebase_map.py` and confirm it exits 0.
3. Add `codebase-map coverage + freshness` to unit 1's §7 gates, because any new module-level function
   in the suite reaches that leg.
4. Before landing, run the whole bar rather than the legs a spec names.

**Left-shift.** The leg costs about a second, so it fits the pre-commit fast leg. Gate it there whenever
the staged set touches a tracked `.py` file. That moves the red from the push boundary to the commit that
causes it. Where a spec names its gates by hand, the documented check is to derive the list from
`tools/gate-legs.json`: every unguarded `subject: repo` leg applies to every unit. Record the class under
`memory/gotchas/` with this build as "where it bit": a spec's hand-named gate list is green while the
bar is red.

## M1 — unit 1's liveness arm has never been observed RED (MEDIUM; id 11)

**Address.** `tools/govkit/selftest.py:700`, `[dBF] AC2 LIVENESS the descriptor ships a file OLD did
not, so the drop is exercised`. Unit 1 spec §5 testing (line 125) and §7 `New arm:` line (155). The
staged acceptance ledger.

**Finding.** Unit 1 §5 says "every new arm is observed RED on a staged break named in §7". §7 names one
break for all the AC1 and AC2 arms: make `write_vintage_receipt` rewind an absent source instead of
dropping it. The liveness predicate is `len(_bf_drop) > 0`. `_bf_drop` comes from `resolve_entry` over
the check-wiring descriptor and `git ls-tree` at OLD, and it never reads the helper. So the named break
cannot red it.

The build's own ledger confirms this. Under R2, with the drop branch staged as `if False:`, it records
that "the `LIVENESS` arm stayed `ok` because it reads only the descriptor and `ls-tree`". No other run
staged a break for it. The ledger's "does not claim" section lists the source-less branch and unit 3's
floors as NOT OBSERVED, but not this arm. §5's claim is therefore false, and the arm landed without the
observed failing case that `AGENTS.md` §7 and the build README require.

Unit 2 had the same gap in its spec. Round 1's spec audit flagged it, and unit 2's arm got its own break
(R3). Unit 3 marked its floors NOT OBSERVED. Unit 1 did neither.

**Fix.** Stage a break that makes the descriptor ship nothing OLD lacked, observe the arm read `FAIL`,
unstage, and record it.

- The preferred break is real rather than synthetic. Remove `check-wiring.fragment.json` from the
  descriptor's `include` and `claims` lists in `tools/govkit/entries/check-wiring.kit.toml`. OLD
  (`24f39915`) ships `tools/check-wiring.sh` and `tools/check-wiring.test.sh`, so `_bf_drop` empties.
  This is the very condition §5's risks line says the arm guards.
- The lens's proposed break, computing `_bf_old` at `39df2b1a`, also reds the arm. It substitutes the
  arm's input rather than the world's state, which is the staged-break-substitutes-a-synthetic-value
  class. Use it only if the descriptor break disturbs too many other arms to read.

Then add a separate `New arm:` line for the liveness arm to unit 1 §7, and an entry in the acceptance
ledger. If the break is not run, mark the arm NOT OBSERVED in §5 with its reason, as unit 3 did.

**Left-shift.** This is the third time in this build that an arm reached a record with a §7 break that
cannot red it. Round 1 on unit 1 and round 1 on units 2 and 3 each caught one, so the documented
spec-audit check has not been enough. A text-shaped hygiene check could close it. For each arm label a
spec's §7 `New arm:` line names, require that the build's acceptance ledger either shows that label
printed `FAIL` under a staged break, or lists it as NOT OBSERVED. Until that check exists, the documented
check is to run the same cross-reference by hand at the closing review.

## L1 — the fixture is called an install OLD could produce, but two row fields stay at HEAD (LOW; id 2)

**Address.** `tools/govkit/selftest.py:217`, the helper's opening line ("an install LANDED AT
`vintage`"). `tools/govkit/selftest.py:679`, the banner "THE FIXTURE IS AN INSTALL `OLD` COULD HAVE
PRODUCED".

**Finding.** The helper rewinds `commit`, `sha256` and `gov_oid` on each kept row (`selftest.py:254-256`).
It leaves `version` and `oid` as `apply` wrote them at HEAD. `git show 24f39915:tools/check-wiring.sh`
declares `KIT_CHECK_WIRING_VERSION=1.0`, and HEAD declares `1.3`. So `update` over the fixture compares
1.3 with 1.3 and prints `level` in its per-kit delta (`govkit.py:6531-6535`), where a real install at OLD
would print `DIFFERS`. The skeptic also measured the kept rows' `oid` as HEAD's blob (`3fcc7829`) while
the target's index holds OLD's (`5c4508e2`) after `settle`. This synthesis did not re-measure the blob
ids.

No current arm reads the version delta or the stored `oid` over these fixtures. The `[dGV-9]` arms
overwrite `version` with a sentinel first. So nothing is red today. The engine does treat `version` as
tied to the vintage of the bytes, though (the `[-PV]` W3 arm near `selftest.py:9310`). A future arm that
grades version drift or the `[-12]` S4 oid carve-out over these fixtures would grade a receipt no install
at OLD could produce, while both comments promise that it is one.

**Fix.** Narrow the claim in this build. Change the docstring and the banner to say that `commit`,
`sha256` and `gov_oid` are rewound, and that `version` and `oid` stay at `apply`'s vintage. Rewinding
the two fields is the fuller fix. It would set `oid` from `gk.blob_oid(b)` (the target pins
`core.autocrlf=false`) and `version` from `resolve_entry_version_at` (`govkit.py:431`) at `vintage`. But
that changes the fixture every consumer arm reads, so it is a unit's worth of work, not a fold.

**Left-shift.** If the fields are rewound, add a `[dBF]` arm that compares each kept row's `version` with
the descriptor's `version_from` line at the vintage. That is a real gate. If the claim is narrowed, the
documented check is that a fixture header claiming vintage fidelity names every receipt field and says
which ones it rewinds.

## L2 — the source-less branch is unobserved for a reason the source contradicts (LOW; ids 3, 7)

**Address.** `tools/govkit/selftest.py:230` ("no row writer emits one today"). Unit 1 spec §2 S4, lines
42-43 ("every row writer in `govkit.py` sets `source`").

**Finding.** Both statements are false. `_cmd_apply` at `govkit.py:4626` and adopt at `govkit.py:8246`
each append `{path: .gitattributes, role: attributes, kit: (govkit), ...}` with no `source` key whenever
the selection declares an `lf_pin`. The S9 preamble's own comment at `govkit.py:6113-6114` names "the
synthesized `attributes` row" as one that carries neither identity. Several shipped descriptors declare
pins, codebase-map, hooks and memory-tree among them.

The real reason no arm observes the branch is narrower. Both callers apply `--kits check-wiring`, and
the check-wiring descriptor declares no `lf_pin`. That NOT OBSERVED is accepted by design. Only its
stated reason is wrong. The reason matters because a maintainer who trusts "no writer emits one" and
deletes the guard would get `cat-file -e <vintage>:None` failing. The helper would then treat the
attributes row as not shipped and run `git rm -f .gitattributes` on the target.

**Fix.** Reword both places. `apply` and `adopt` emit a source-less `attributes` row whenever the
selection declares an `lf_pin` (`govkit.py:4626`, `8246`). Check-wiring declares none, so neither fixture
holds one and no arm observes the branch. Keep the guard.

**Left-shift.** An arm can turn this NOT OBSERVED into an observed one. Run `write_vintage_receipt` over
a fixture that applies a kit with an `lf_pin`, then assert that the attributes row is unchanged in the
receipt and that `.gitattributes` is still in the target's index. Without that arm, the documented check
is that a NOT OBSERVED reason asserting absence in the source ("no writer emits X") is grepped before it
is written.

## L3 — two comments attribute all thirty red arms to the fixture refusal (LOW; id 4)

**Address.** `tools/govkit/selftest.py:224` ("Thirty arms went red") and `tools/govkit/selftest.py:670`
("thirty on a row invented at a vintage that lacked its file").

**Finding.** Unit 1 spec §1, S3 (line 39) and AC4 (line 146) split the 30 red labels at `4cf0944d` into
27 built over `stale_target` or `delta_target` and 3 `u5a` `check` arms that typed `2/2`. Unit 3 fixes
the three, and they use neither builder. Unit 1's own commit message says the refusal reddened 27 arms.
So the comments disagree with both the spec and the commit that added them, on a measured figure. A
reader checking the fixture fix against "thirty" would look for three arms this change never meant to
turn green. This is the two-answers-to-one-question class.

**Fix.** Say 27 in both comments, or drop the figure and point at unit 1 §1, which owns the count.

**Left-shift.** `AGENTS.md` §7 already forbids typing a count beside the thing it counts. The
documented check is that a code comment citing a measured figure cites the record that measured it
instead. Add this build as an instance in `memory/gotchas/two-answers-to-one-question.md`.

## L4 — two comments and the README say no failing arm carried stderr (LOW; id 10)

**Address.** `tools/govkit/selftest.py:224-225` ("the refusal sat on stderr where none of their details
looked"). `tools/govkit/selftest.py:682-683` ("every consumer arm's stdout-only detail pointed at the
measurer's UNVERIFIED line"). Build README line 18 ("those arms print only stdout").

**Finding.** At `4cf0944d`, three of the failing arms already carried stderr in their details:

- `[-12] AC4 NEGATIVE`, with `_p4b.stdout + _p4b.stderr` (line 2708 at that commit, 2808 now).
- `[-12] AC9 NEGATIVE`, with `_p9b.stdout + _p9b.stderr` (2879 then, 2979 now).
- `[-8] AC1 the first update MERGES`, with `_r81.stderr[-600:]` (3789 then, 3886 now).

This synthesis read those lines in `4cf0944d`'s `selftest.py`. Each runs `update` over a fixture that
S9 refused, and S9 runs after the writable-target checks. The skeptic read the baseline run log and
found the S9 `REFUSING` text in four FAIL details, including `[-12] S4`. This synthesis did not re-read
that log. The universal claim is false. The accurate diagnosis is narrower: most consumer arms printed
only stdout, and the first FAIL lines a reader met named the probe instead of the refusal.

**Fix.** Narrow all three statements to that. One wording for the comments: "most of their details were
stdout-only, so the first FAIL lines named the probe instead of the refusal". The docstring sentence at
line 224 carries both L3 and L4, so fold them in one edit.

**Left-shift.** The documented check is that a diagnosis quantified over a population ("every", "none")
in a comment or record is tested against the evidence before commit. Here that means grepping the
baseline FAIL details for the refusal text. No gate is proposed, because such claims are free text.

---

## What this round did not cover

**The refuted set.** This record was given the confirmed findings only. It cannot say which hunt item,
if any, each of the three refuted findings addressed.

**Hunt items that drew no confirmed finding.** All four lenses returned, so each of these is a zero from
a full read, not from a dead lens. This synthesis did not independently re-derive them.

- Consumers of `stale_target` and `delta_target` whose population changed when the fragment row was
  dropped. This covers every arm after `selftest.py:640` that reads `rec["files"]`, `install.sums`,
  stdout words or verdicts after an `update`, including `[-12]` AC3, AC4, AC9 and S4, the `u2b` and
  `u2c` arms, the `[dGV-8]` ungraded arms, and `[-8]` AC1 to AC6. The staged ledger's GREEN run printed
  1240 `ok` and 0 `FAIL` at `2076d57a`, which shows none of them reds. It does not show that each still
  grades what its label says.
- Whether `git rm -q -f` on a path `apply` staged but never committed leaves the target in the state
  `settle` then commits.
- Whether the `[dBF]` arms placed before `up = stale_target("u2a")` and `t8 = delta_target("d8-ac1")`
  change any later arm's fixture, through the `bf` and `d8-bf` tmp directories.
- Whether `resolve_entry` at `canonical_ctx("check-wiring")` matches what `apply` over `DEPLOY_FULL`
  writes. Unit 3's ledger entry reads N, P and H as 3, 3 and 3 from the descriptor. This synthesis read
  the descriptor, which lists three files in one `engine` rule, and agrees.
- Contradictions between the specs and the code beyond those under M1, L2 and L3.

**Suite status.** The brief says the full-suite green run and the staged-break runs were still in
progress at the main loop. The staged, uncommitted acceptance ledger in this worktree already records
GREEN, R1, R2 and R3 results. This record quotes that ledger as it reads and did not run any of them.
The ledger also records a `FileNotFoundError` in the `[-ST1]` rollback arms near `selftest.py:5714`
under R3. That predates this build, no lens or skeptic adjudicated it, and it is not a finding here.

**Re-read at source by this synthesis:**

- `tools/govkit/selftest.py` at 210-262 (`write_vintage_receipt`) and 664-705 (`stale_target` and the
  `[dBF]` arms). Lines 2808, 2979 and 3886, and the same arms at `4cf0944d`.
- `tools/govkit/govkit.py` at 4618-4632 (the `apply` attributes row), 6108-6116 (the S9 preamble
  comment), 6528-6536 (the per-kit version delta) and 8240-8252 (the adopt attributes row). The
  definitions of `resolve_entry_version_at` and `entry_version`.
- `tools/govkit/entries/check-wiring.kit.toml`, and `git ls-tree` at `24f39915` for its three files.
- `KIT_CHECK_WIRING_VERSION` at `24f39915` and at the tip.
- `tools/gate-legs.json` at the `codebase-map coverage + freshness` leg, and `.githooks/pre-commit`.
- Unit 1 spec lines 39-44, 123-127, 146 and 155-156. The build README lines 16-20 and its rule on new
  arms. The staged acceptance ledger.
- `memory/guides/BUILD-METHOD.md` at 128-142 and M8.

**Run by this synthesis:** `python tools/codebase-map/test_codebase_map.py` in this worktree at
`2076d57a`, which exited 1 with `STALE symbols.json` in 1.15 s.

**Not run here:**

- `gen_map.py --write`. The one-entry diff under B1 is as the lenses report it.
- The suite, and every staged break named in the specs or proposed above.
- The `oid` measurement under L1, and `update` or `update --to 372e6b2a` over the fixture. The `level`
  and `DIFFERS` readings under L1 are read from `govkit.py:6531-6535`, not observed.
- The baseline run log at `4cf0944d`. L4 rests on the arm source at that commit instead.
