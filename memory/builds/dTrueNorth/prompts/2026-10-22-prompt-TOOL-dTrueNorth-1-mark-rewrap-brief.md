**Serves:** research TOOL-dTrueNorth-1

# Spec brief — re-wrap six §8 RESOLVED marks the departures report misreads

## The prompt

> `python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py --report dTrueNorth` prints five findings, `entry N's widens: [none ·] joins no record`, for entries 3, 4, 7, 8 and 9. Each is a §8 RESOLVED mark whose line breaks right after `widens: none ·`, so the next line begins `relaxes: none`. The instrument's `KEY` pattern ends a value at whitespace-`·`-whitespace or at the next key, and a newline after the `·` lets it read `none ·` as the value. The instrument's blob is pinned and is never edited, so the marks are re-wrapped.

## The brief

### Goal
Re-wrap each listed §8 mark so that no line ends in `·`: the `widens: none · relaxes: none` pair sits on one line, or the break falls before `widens:`. Author only: no product code, no commit, no gate.

### Items
1. `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-20.md` lines 474-475 and 477-478.
2. `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-8.md` lines 171-172.
3. `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-24.md` line 177 and the line after it.
4. `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-26.md` line 462 and the line after it.
5. `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-27.md` line 544 and the line after it, if its `widens:` value breaks the same way.
6. Only line breaks and the continuation indent move: no word, mark, rev, status line or §9 line changes. These specs are CLOSED, and the change is whitespace inside a mark, so no rev bump; if the spec template says otherwise for a whitespace-only edit, say so and make no edit.

### Acceptance
`grep -n 'widens: none ·$'` over `memory/builds/dTrueNorth/spec/` prints nothing; each edited spec's lines stay under the line-length cap the hygiene gate reads; `git diff --word-diff` shows no word changed.

### Gates
No gate runs in this pass.

### Non-goals
Any other line; any other spec; the instrument; product code.
