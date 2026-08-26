## Verdict: CLEAN WITH FIXES

**Serves:** diff-review TOOL-aCollapsedScan-13

Node `a`, 2026-08-26 to 2026-08-27. Scoped to the one file `TOOL-aCollapsedScan-13` changed,
`20834a74..HEAD` over `tools/memory-tree/check-memory-hygiene.sh`. 7 raised, **6 confirmed**, 1
refuted, **0 blockers** — 3 medium and 3 low, collapsing to three distinct defects.

**Recorded against the UNIT, not the build.** `--review --subject aCollapsedScan` refused with
`check 37: this subject already carries a terminal review round, so the loop ended for it and
another round would rewrite that history`. The build-level closing loop CONVERGED at round 2, and
this unit was added afterwards by owner instruction. The driver is right: a converged loop is not
re-opened by a later unit, and that unit carries its own review. Worth knowing before anyone tries
to record a "round 3" against a build slug again.

## Why this review was the one that mattered

The unit shipped with what looked like conclusive evidence: clean-tree output byte-identical before
and after, two staged breaks producing byte-identical output from both checkers, every failure
message template unchanged. All true, and all of it passes over three real divergences, because it
samples three input states out of an infinite set and this is a string-handling refactor.

So the lenses were handed that evidence and told to hunt what it CANNOT reach: construct an input
where old and new differ. All three confirmed findings came back with the divergent input attached.

## The three defects

**`${var#*-}` is a NO-OP when there is no hyphen (medium, and the only one with teeth).** For a
two-segment tail like `TOOL-1`, `_r3=${_r2#*-}` returned the slug segment, the digit-run peel read
the slug's own leading digits, and `claimed` came out `TOOL-1-1` — an id present in no filename, no
`Serves:` line and no spec. The regex it replaced required a second hyphen and matched nothing. A
lens ran both predicates over **8796 synthetic stems: 12 divergences, every one of this class and
none of any other**, which is simultaneously the bug report and the evidence that the rest of the
refactor is equivalent.

Reachable through the gate's own filename rules: `2026-08-26-build-TOOL-1.md` is legal, because the
family qualifier in check 3's regex is optional and `[A-Za-z0-9]+` matches `TOOL` as a slug. The
usual outcome is a corrupted diagnostic — branch 4's message IS its whole product — and the narrow
one is a fail-to-pass flip if the record's `Serves:` line happens to list the fabricated id.

**`read` in a loop condition discards an unterminated final line (medium).** `read` returns
non-zero at EOF-without-delimiter having already assigned the variable, so `while [ "$_n" -lt 6 ] &&
IFS= read -r _l` read that line and dropped it where `sed -n '1,6p'` printed it. Confirmed directly:
a spec ending `**Status:** CLOSED Tier-2` with no trailing LF gave the header from the old code and
nothing from the new. No verdict differs today — such a file has no acceptance-criteria heading
after that line, so a later grep skips it anyway — which makes it a trap rather than a live bug, and
it is fixed as one.

**`${rest%%-*}` cannot see a hyphenated FAMILY (low here, live for an adopter).** Nothing forbids
one; the sibling Python builds the same alternation into a regex that accepts it. With
`FAMILIES="x:MY-FAM"`, a correctly named and correctly bound record passed under the old code and
failed under the new, with a message pointing at the filename rather than at the conf. Dark in this
repo, and every such record in that adopter's tree would red at once.

## The fix that nearly repeated the bug it fixed

The family fix resolves by longest declared prefix. Its first cut then did `_r2=${rest#*-}` — strip
to the first hyphen — which is wrong for exactly the hyphenated family the loop above it exists to
find. Corrected to `${rest#"$_f"-}`, stripping the matched family. Caught by reading the applied
diff, not by the harness, and recorded because it is the same reasoning slip twice in one function.

## What replaced eyeballing the diff

A differential harness runs both predicates over the named classes plus a shape sweep:
**560 inputs, 0 divergences**, and the hyphenated-family case agreeing. AC1 was then re-verified
after the fold, since a byte-identity proof taken before the last three changes proves nothing about
what lands: clean tree, exit 0, output identical, 297 s.

The diff was read carefully twice before this review and all three defects survived both readings.
That is the argument for the harness over the reading, and for `git diff` never being the last word
on an equivalence claim.
