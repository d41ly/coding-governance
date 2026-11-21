**Serves:** research TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63

# Brief — dPlacedRequest: four §8 RESOLVED marks the departures report misreads

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

The close's departures report, `python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py --report dPlacedRequest`,
prints four findings of the shape `entry N's widens: [none ·] joins no record` or `entry N's relaxes: [none. Made] joins
no record`. The instrument's mark pattern ends a value at a space-`·`-space, at `; `, at the next key or at the end of
the text, so a line ending in `widens: none ·`, or a `relaxes: none` followed by `. Made`, reads a value other than
`none`. Correct each mark so both its values read exactly `none`; change nothing else.

### Items

1. In `TOOL-dPlacedRequest-46`'s spec, the §8 mark whose line ends `widens: none ·`: re-wrap it so no line of the mark ends in `·`, the `widens: none · relaxes: none` pair on one line or the break before `widens:`.
2. In `TOOL-dPlacedRequest-49`'s spec, the §8 mark whose line ends `widens: none ·`: the same re-wrap.
3. In `TOOL-dPlacedRequest-63`'s spec, the §8 mark whose line ends `widens: none ·`: the same re-wrap, and the period right after its `relaxes: none` replaced by ` ·`, so the sentence that follows stays as written.
4. In `TOOL-dPlacedRequest-62`'s spec, the §8 mark reading `relaxes: none. Made`: the period right after `relaxes: none` replaced by ` ·`.
5. These specs are CLOSED, and the change is whitespace and one separator inside a mark, made for the close's report: no rev bump, no status change, and one §9 line in each naming this brief.

### Acceptance

`grep -n 'widens: none ·$'` and `grep -n 'relaxes: none\. '` over the four specs print nothing, and
`check-memory-hygiene.sh --only 12,25 --spec` and the spec-token checker over each report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`) and the spec-token checker; no other.

### Non-goals

No product code, no commit, no index render, no status flip, no other line and no other spec. Never quote a check's
hit literally in prose.
