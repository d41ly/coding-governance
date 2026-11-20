# TOOL-dPlacedRequest-53 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-53

The unit was built from its spec at rev-3 on base `3dbec3254`. It touches no product file: it
observes unit 52's criteria as 52's rev-10 leaves them and sweeps the build's open specs for a
criterion that counts lines of one squeezed line. No gate, suite or bar ran in this pass. Every
reading below is a `sed`, `tr`, `awk` or `grep` probe over a spec of the tree, a blob read by
`git show`, or a hand-written scratch file under the session scratch.

**Evidences:** TOOL-dPlacedRequest-53
- AC1 — `flat`, defined as `sed '/^## 9\./,$d' <file> | tr -s '[:space:]' ' '`, over a scratch file holding `S25` in two paragraphs and once more below its `## 9.` heading: `grep -o 'S25' | wc -l` printed 2 and `grep -c 'S25'` printed 1. (PINNED)
- AC1 — RED: `grep -c 'S25'` over the same file unsqueezed printed 3, the line under the cut counted, so the cut and the squeeze are what the reading measures. (PINNED)
- AC2 — `grep -c` is carried by none of unit 52's AC1, AC6 and AC9 bullets, cut by `awk` from its section 6 at rev-10 (CLOSED): the count over the cut printed 0, no `- **AC6**` bullet stands (count 0), and the AC9 bullet names `check-spec-tokens.py` once, reading `tools/check-spec-tokens.py#read_size_ceilings` and the `size join` line. (DERIVED)
- AC2 — RED: the same cut over unit 52 at rev-9, read by `git show 0d700d256`, printed a `grep -c` count of 3. (PINNED)
- AC3 — `grep -L -E '^\*\*Status:\*\* (CLOSED|WONTDO)'` over the build's spec folder listed 12 open specs, 53 to 64, this unit INPROGRESS and the rest DEFERRED. (DERIVED)
- AC3 — `grep -n -A1 "grep -c"` over those 12 printed 201 lines; read for "at least", every hit asks at least 1, and the one with a higher figure, unit 59's, is a `grep -oE` pattern in its section 4 that spells the shape, not a criterion counting it. No hit is a section 6 criterion piping `flat` or a `tr -s` squeeze into a count above 1. (DERIVED)
- AC3 — a wider reading beside it: each open spec cut before its `## 9.` and squeezed, then `grep -oE` for a `grep -c` followed within 300 characters by `prints` a figure of 2 or more, printed 0 for each of the 12. (DERIVED)
- AC3 — RED: the same two reads over unit 52 at rev-9 found its old AC1, AC6 and AC9, the `-A1` read naming `at least 2` on two of them and `at least` on the third, and the wider read printing 3. (PINNED)

## Owed edits

None: the sweep found no hit in an open spec, so no spec-writer edit is owed.

## Items diverged

None: each criterion was observed as written.

## Owed at the close

- The legs the spec's Gates section names, run once by the main loop: memory hygiene, spec tokens, lexicon naming predicates, recall floor and recall floor arms. The spec declares no new arm.
