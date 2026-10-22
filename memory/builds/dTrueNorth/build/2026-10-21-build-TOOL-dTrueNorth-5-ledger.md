# TOOL-dTrueNorth-5 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-5

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon answered the
names the pass mints (`--suggest`, one identifier each). Every criterion below was observed by a probe
of the changed code at the working tree over `a38ea1fcb`: a node cut of the review harness's prelude,
an AsyncFunction run of the build harness over stub hooks, the generator's own functions in-process
over a fixture git repository under the user temp directory, short-named, and check 21's audit-pin
branch read verbatim out of the engine by its own marker lines and evaluated over that fixture's
`--print-bindings` capture with `fail` and the legacy set stubbed. The probes stand in for the
`tier2-review self-test`, `unattended-build self-test`, `build-index selftest`,
`memory-hygiene self-test` and `memory hygiene` legs; those, with the four `New arm:` lines'
RED-first observations, are owed to the close.

**Evidences:** TOOL-dTrueNorth-5
- AC1 — `tools/workflows/tier2-review.js` — the prelude cut as the suite cuts it, 561 lines, threw at
  round 1 and at round 2 for the subject with no `rev`, the message naming the field in backticks; it
  threw naming `rev` for `rev: 0` and for `rev: '2'`, naming `id` for `id: 'x-1'`, and "subject 1's id
  TOOL-x-1 repeats subject 0's" for two subjects sharing an id. The subject pinned `TOOL-x-1` rev 2
  proceeded at rounds 1 and 2, and a diff review with no subjects proceeded. The template with its
  fan-out cap token rendered as 5 is byte-equal to the render.
- AC2 — `renderAuditBinding` — called from that prelude on `TOOL-x-1` rev 3 and `TOOL-x-2` rev 1 it
  returned `**Serves:** spec-audit TOOL-x-1@rev-3 TOOL-x-2@rev-1`; `grep -c 'renderAuditBinding(subjects)'`
  printed 2 over each of `tools/workflows/tier2-review.js` and `tools/workflows/tier2-review.template.js`,
  the definition and the call in the spec kind's synthesis sentence, which no longer says "the
  reviewed spec set defines".
- AC3 — `tools/workflows/unattended-build.js` — with the resolver stub returning `{path, blob, tree, rev: 2}`
  for the spec of `TOOL-x-1` and a clean callee, the callee's one subject carried `"id":"TOOL-x-1","rev":2`
  beside its path and blob, and `nextAction` carried `**Serves:** spec-audit TOOL-x-1@rev-2` as the
  record's line 1. A resolver entry with no rev threw "resolved subject 0 does not carry rev"; a caller
  subject with no id threw "subject 0's id is not a unit id", one with no rev "subject 0's rev is not an
  integer revision", neither spawning the callee; a resolved path no unit's `specPath` matches threw
  "no id can pin them: zz.md".
- AC4 — `cmd_print_bindings` — in-process over the fixture with `SPEC_AUDIT_PIN_CUTOFF="2026-01-01"` and
  `TOOL-tPin-1` at rev-2, exit 0: one `P` row for the unpinned 2026-02-01 record, "TOOL-tPin-1 carries
  no @rev-N pin", one for the record pinning `@rev-5`, "TOOL-tPin-1@rev-5 pins a revision its spec has
  not reached, header rev-2", none for the `@rev-2` record, the unpinned `diff-review` record or the
  unpinned 2025-12-31 spec audit, then the `Q` row with 3 graded and the cutoff. Blank: no `P` row and
  the `Q` row with 0 and `off`. The value `soon`: exit 2, printing one line naming
  `SPEC_AUDIT_PIN_CUTOFF`. `read_bindings` gave the `@rev-2` record `pins == {'TOOL-tPin-1': 2}`. Over
  the real tree the verb exited 0 with no `P` row and the `Q` row 0 and 2026-10-22.
- AC5 — `bash -n tools/memory-tree/check-memory-hygiene.sh` — exited 0. The branch, cut out of the
  engine and evaluated over AC4's capture, failed 21 naming both records and printed
  `the audit-pin arm graded 3` with the cutoff 2026-01-01; with the unpinned record in the legacy set,
  or `RECORD_SERVES_CUTOFF` at 2026-02-02, it named the over-pinned record alone; over the capture less
  its `Q` row it failed naming "the bindings parse printed N 0 and no Q row"; over the blank capture it
  printed `the audit-pin arm is off`. Both new fail branches carry a positive arm by the extractor
  `check-arms.py` itself uses. The engine's own run is the hygiene suite's `New arm:`, owed to the close.
- AC6 — `render_region` — through `plan` over the fixture: with the spec moved to rev-3 and its
  highest pin at rev-2 the region carried
  `Ids whose spec moved past its audited revision: TOOL-tPin-1@rev-2.`; with a pin at rev-3,
  `none — 1 of 1 unit id(s) carry a pin.`; with no pinned record, `none — 0 of 1`.
- AC7 — `grep -n '^SPEC_AUDIT_PIN_CUTOFF=' <conf>` — printed line 802 of `.memory-tree.conf` with
  2026-10-22, and line 377 of `tools/memory-tree/.memory-tree.conf.example` with `""`. The comment's
  ref reading over 55 refs and its worktree reading over 18 worktrees each returned 2026-10-21 as the
  newest review filename date, and the commit-day reading 2026-10-21, so the relation returns
  2026-10-22, strictly after both. `grep -c SPEC_AUDIT_PIN_CUTOFF` over `tools/memory-tree/kit.toml`
  printed 1.
- AC8 — `grep -n 'SPEC_AUDIT_PIN_CUTOFF'` — printed line 460, check 21's entry, and lines 592 and 602,
  "Record bindings", in both `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`; the grep
  for `@rev-<the revision you read>` printed line 140 of `memory/guides/BUILD-METHOD.md` and of
  `tools/memory-tree/BUILD-METHOD.template.md`; `wc -c memory/guides/BUILD-METHOD.md` printed 29354.
- AC9 — `grep -c '^- \[docs\]'` — printed 1 for each of the three renders under `.claude/agents/`;
  `python tools/roles/render_agents.py --check` exited 0, grading 9 agent types and 1 index; the
  `gov-builder`, `gov-spec-reviewer` and `gov-diff-reviewer` rows of the catalogue in
  `tools/roles/README.md` list `docs`, three of three.

The `New arm:` lines of this unit on the Python selftests were observed at the close, in a scratch clone of `e583a7f42` with the breaks of `2026-10-22-build-TOOL-dTrueNorth-29-arm-breaks.md` staged one set at a time: under the `gen_build_index.py` selftest, the splice break (each product function the unit's pass commit changed put back to its text at that commit's parent, each function it added stubbed to raise), 9 of its 9 arms red. Each staged break was restored with a checkout, and at `92a0dcb96` every one of those selftests printed all arms held. Its lines on the shell suites the flagged bar runs are owed with that bar, which the owner deferred past this landing.
