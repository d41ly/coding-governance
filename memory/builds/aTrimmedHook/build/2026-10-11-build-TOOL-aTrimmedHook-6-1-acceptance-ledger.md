# TOOL-aTrimmedHook-6 — acceptance ledger

**Serves:** journal TOOL-aTrimmedHook-6

No merge bar and no self-test suite ran in this pass. The six new arms run in a clone of the hygiene
self-test's fixture, so nothing they commit reaches the tree the later arms read. They were observed
through a slice of the fixture prologue and the new block, run against three gates. Against the
pre-unit gate, the grandfather and rename arms failed. Against a copy with the four mechanisms
inverted, five arms failed, the four this unit closes plus the rename-parse arm. Against this pass's
gate all six held. The rename-parse arm's first draft renamed inside one build folder and passed
against the inverted parse, because the narrowing already held that folder; it now moves the file into
another build folder, and that is how its RED was observed. The close owes the whole
`memory-hygiene self-test` leg.

**Evidences:** TOOL-aTrimmedHook-6
- AC1 — `check-memory-hygiene.sh --staged` — with only a `legacy-files.txt` edit staged that drops the
  row for a committed free-named file, check 5 named the file and the whole-tree line printed; the
  pre-unit gate printed the no-new-name line and reported nothing, observed RED.
- AC2 — `check-memory-hygiene.sh --staged` — a staged `git mv` of a legacy-listed file to a conforming
  name made the stale-line guard report the old path; the pre-unit gate printed HELD, observed RED.
- AC3 — `check 9: render SKIPPED` — a staged no-id edit to `memory/DECISIONS.md` printed the relayed
  line, and a staged line citing a new id printed none; with the relay's print removed, the first arm
  failed, observed RED.
- AC4 — `check-memory-hygiene.sh --staged` — a staged `git mv` of a correctly named spec into another
  build folder under a malformed name made check 5 name the new path; with the parse keyed on the old
  path, it named nothing, observed RED.
