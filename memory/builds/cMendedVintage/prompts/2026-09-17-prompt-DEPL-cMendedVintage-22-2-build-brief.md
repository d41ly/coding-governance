# Build brief — DEPL-cMendedVintage-22

**Serves:** journal DEPL-cMendedVintage-22

Read the spec whole first, then read finding **B1** in
`memory/builds/cMendedVintage/reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md`.
The review section carries the evidence this spec compresses, and it is worth reading in full.

*Standing note: this unit exists because the closing review returned BLOCKED. The build is 31 units
done and cannot land until this and its three siblings are fixed. Twenty briefs in this build carried
a claim measurement disproved; treat this one as evidence, not authority.*

## The failure mode to avoid is the one that already happened once

This exact mechanism was confirmed as a HIGH in
`memory/builds/aPacedTurnstile/reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md`,
finding D3, described there as *the target is permanently wedged*. That fix went to the offending
kit's descriptor row rather than to the predicate, so the class survived and this build re-armed it
by shipping another argv change.

**Do not fix a descriptor.** The predicate is the subject. A change to `tools/gate-lint/kit.toml`
that makes today's symptom go away is the same non-fix a second time, and your spec's §3 says so.

## The code already admits the gap, in its own words

`tools/govkit/selftest.py` around `:1384-1388` records that *tampering the RUNNER changes neither
side and apply silently repairs it* — filed as a fixture inconvenience rather than as a defect. That
comment is the shipped code's own confession, and S4 turns it into the arm it should always have
been. Do not leave the comment standing beside the arm that falsifies it; that is this repo's
`amendment-leaves-its-other-half-standing` class, which has fired four times in this build.

## AC1 is a behaviour change on arrival, and that is intended

A target carrying a hand-edit it has been getting away with will red after this lands, truthfully,
with the message that already exists. Do not soften it. The message names the leg and the file, which
is what an operator needs; §8 Q1 records why no remedy sentence is added.

## AC3 is the guard, and narrowing is how you would fail it

The refusal keeps withholding the WHOLE manifest. A per-leg skip looks like a kinder fix and writes a
manifest half-graded against a file the target tampered with. Observe it: when the tamper refusal
fires, assert no leg in that run reached the target's manifest.

## Measure the wedge before you fix it

The review says an adopter who applied in the `f1a05f8e` window holds a three-element argv and reds
on a manifest byte-identical to what gov wrote, and that neither `update` nor `apply` clears it.
Reproduce that end to end on a scratch fixture first — the receipt stamped with the old rows, the
second run comparing identically. A fix whose failing case you have not seen is an assertion about
nothing, and this one is cheap to stage.

## Line numbers

The review cites `tools/govkit/govkit.py:2728`, `:2734`, `:2757`, `:2802`, `:5590`, `:8635` and
`:8766`. Those were read at `b6cc8f6f`; the tree has moved since. Locate every site by symbol and by
the text the review quotes.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to
`selftest.py` or `matrix.py`. Spell no `tools/<kit>/…` path in shipped prose or comments.

## Required of every unit

gov keeps no govkit receipt, so no criterion here is observable against this repo — each needs a
scratch fixture target under the run's scratch root. Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-22-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape.** `memory/HYGIENE.md` gives the form as `- AC1 — <token> — what was
observed` with the backticked witness on the bullet's FIRST line, immediately after the label. Check
23 reads form from that line alone, so a witness on a continuation line is graded `bad` however tidy
it looks — eleven bullets in this build failed exactly that way. The AMENDED form is
`- AC2 — amended rev-<n> — …` and carries no backtick. The token must share content with the
criterion's own backticked token, case-folded either way round, and a criterion whose own span wraps
across a line break offers no token for anything to join.

The run is in VERIFYING, so `gate-guard.js` no longer denies the suites. You MAY and SHOULD run
`python tools/govkit/govkit.py selftest` — it is your unit's own gate and it is currently RED on the
full bar for reasons the main loop has already repaired. Report its verdict either way. Bound every
command at 900s or more.
