# TOOL-dTrueNorth-13 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-13

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon answered the two
names the pass mints (`--suggest`, one identifier each, both OK). Every criterion below was observed
by a probe of the changed code at the working tree over `4f2bc2595`, each run a second time over the
same file at `HEAD` so the probe is seen to move: a node cut of the review harness's prelude, a node
AsyncFunction run of the review harness and of the build harness over stub agents, and the
generator's `cmd_print_bindings` in-process over a fixture git repository under the user temp
directory, short-named, with the `HEAD` copy of the kit extracted by `git archive` beside it. The
probes stand in for the `tier2-review self-test`, `unattended-build self-test` and
`build-index selftest` legs; those, with the three `New arm:` lines' RED-first observations, are owed
to the close.

**Evidences:** TOOL-dTrueNorth-13
- AC1 — `tools/workflows/tier2-review.js` — the prelude cut as `tools/workflows/tier2-review.test.sh:67-81`
  cuts it, 598 lines, with `kind: 'spec-audit'`, round 1 and the two `build/` subjects sharing
  `PLAY-dX-1`: it proceeded. With `rev: 2` on the first it threw "spec-audit subject 0's `rev` is
  refused: its path "memory/builds/dX/build/a.md" holds no builds/<slug>/spec/ segment"; a subject on
  `memory/builds/dX/spec/c.md` with no rev threw "subject 0's `rev` must be the integer N", both naming
  `rev`. Over the `HEAD` render (561 lines) the two design subjects threw for a missing `rev`, the red.
- AC2 — `renderReviewedLine` — from that prelude, on `TOOL-x-1` at rev 3 under `builds/dX/spec/` and
  the two design subjects, `renderAuditBinding` returned exactly
  `**Serves:** spec-audit TOOL-x-1@rev-3 PLAY-dX-1` and `renderReviewedLine` returned `Reviewed: `
  followed by the three `<path>@<blob>` pairs joined by `, `.
  `grep -c 'renderReviewedLine(subjects)'` printed 2 over each of `tools/workflows/tier2-review.js` and
  `tools/workflows/tier2-review.template.js`, the definition and the call at line 1841 inside the
  synthesis prompt's `<<<REVIEWED` markers. A whole-script run over stub agents gave a design audit's
  synthesis prompt `**Serves:** spec-audit PLAY-dX-1` between the one marker pair and, between the
  other, `Reviewed: ` with the two `build/` subjects at their blobs, and no "naming each reviewed
  subject" sentence; over the `HEAD` render that run threw for a missing `rev`, and a two-spec run
  carried no `<<<REVIEWED` block and the composing sentence.
- AC3 — `nextAction` — an AsyncFunction run of `tools/workflows/unattended-build.js` in the shape of
  `tools/workflows/unattended-build.test.sh:164-237`, over that suite's `UNITS` fixture and an
  all-refuted clean round, withheld the roster and its `nextAction` read "a title line; a line that is
  exactly `Reviewed: s1@abc1234, s2@def5678`, with nothing added to it; a line stating the round".
  Over the `HEAD` render it read "a line naming the reviewed subjects `s1@abc1234, s2@def5678` and the
  round", with no `Reviewed: ` prefix, the red.
- AC4 — `cmd_print_bindings` — in-process over a fixture repository under `%TEMP%` whose conf sets
  `SPEC_AUDIT_PIN_CUTOFF="2026-01-01"` and whose `HEAD` commits `PLAY-tDoc-1`'s spec and two files under
  `build/`, exit 0: the 2026-02-01 design-only record `**Serves:** spec-audit PLAY-tDoc-1` naming the two
  committed `build/` files printed no `P` row; the record naming `PLAY-tDoc-1`'s spec file printed one;
  the record with no `Reviewed:` line printed one; the missing-path record serving `PLAY-tDoc-1` and
  `PLAY-tDoc-2`, naming one committed `build/` file and one path absent at `HEAD`, printed two, one per
  id; the `Q` row read 4 graded at 2026-01-01. The `HEAD` kit over the same fixture printed one `P` row
  for the design-only record, the red. Over the real tree the verb's output was byte-identical to the
  `HEAD` kit's, 3186 lines, `Q` 0 at 2026-10-22.
- AC5 — `grep -cE "path: '[a-z]+\.md'[^}]*rev:" tools/workflows/tier2-review.test.sh` — printed 0, and
  the other three greps AC5 names, the `kind: 'spec-audit'` grep, the `rab(\[{ id:` grep over
  `tools/workflows/tier2-review.test.sh` and the `^MT_ARGS=.*"path":"s1"` grep over
  `tools/workflows/unattended-build.test.sh`, each printed 0; over the `HEAD` files they printed 24,
  21, 1 and 1.

The `New arm:` lines of this unit on the Python selftests were observed at the close, in a scratch clone of `e583a7f42` with the breaks of `2026-10-22-build-TOOL-dTrueNorth-29-arm-breaks.md` staged one set at a time: under the `gen_build_index.py` selftest, the splice break (each product function the unit's pass commit changed put back to its text at that commit's parent, each function it added stubbed to raise), 2 of its 2 arms red. Each staged break was restored with a checkout, and at `92a0dcb96` every one of those selftests printed all arms held. Its lines on the shell suites the flagged bar runs are owed with that bar, which the owner deferred past this landing.
