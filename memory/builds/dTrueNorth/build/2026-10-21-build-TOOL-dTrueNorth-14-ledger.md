# TOOL-dTrueNorth-14 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-14

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon answered the one
name the pass mints (`--suggest derive_audit_writers --as py.function`, OK). Every criterion below
was observed by a probe of the changed code at the working tree over `60919b0e7`: the generator's
`cmd_print_bindings` in-process and through its own `--print-bindings` CLI over fixture git
repositories under the user temp directory, short-named, with the `HEAD` copy of the kit extracted by
`git archive` beside them so the probe is seen to move; check 21's audit-pin branch cut verbatim out
of the engine and evaluated over that fixture's capture; and the grep AC5 names. The probes stand in
for the `build-index selftest` and `memory-hygiene self-test` legs; those, `memory hygiene`, and the
two `New arm:` lines' RED-first observations are owed to the close.

**Evidences:** TOOL-dTrueNorth-14
- AC1 — `cmd_print_bindings` — in-process over a fixture repository under `%TEMP%` whose commit A
  holds `tools/workflows/tier2-review.js` without `renderAuditBinding` and a conf setting
  `SPEC_AUDIT_PIN_CUTOFF="2026-01-01"`, branch `run` from A committing the unpinned
  `2026-02-02-review-ARCH-tOne-1-spec-audit.md`, commit L on the trunk adding the function, and `run`
  merged after L: exit 0, no `P` row for the record, and `Q<TAB>1<TAB>2026-01-01<TAB>1`. The same
  call with `derive_audit_writers` stubbed to return nothing printed the record's `P` row and a fourth
  field of 0, and the `HEAD` kit's `--print-bindings` over the same fixture printed the `P` row and the
  three-field `Q<TAB>1<TAB>2026-01-01`, the red.
- AC2 — `cmd_print_bindings` — the same fixture then committing the unpinned
  `2026-02-03-review-ARCH-tOne-1-spec-audit.md` on the trunk printed one `P` row for it,
  `ARCH-tOne-1 carries no @rev-N pin`, still none for the merged record, and `Q<TAB>2<TAB>2026-01-01<TAB>1`.
- AC3 — `cmd_print_bindings` — the unpinned `2026-02-04-review-ARCH-tOne-1-spec-audit.md` staged and not
  committed printed a `P` row for it and `Q<TAB>3<TAB>2026-01-01<TAB>1`. Beside it: with
  `backlog.resolve_kit_dir` stubbed to raise `LookupError` all three printed a `P` row and the fourth
  field read `-`; a record committed after the harness was deleted printed its `P` row, graded rather
  than exempt; `derive_audit_writers` over no record returned the empty set.
- AC4 — `tools/memory-tree/check-memory-hygiene.sh` check 21, its audit-pin branch cut out and evaluated over AC1's fixture capture — printed `1 written by a harness before renderAuditBinding`
  at the end of `the audit-pin arm graded 1 spec-audit record(s) from SPEC_AUDIT_PIN_CUTOFF=2026-01-01,`
  and no failure. The engine's own run over that fixture is a gate leg no role agent runs: the
  suite arm on the second `New arm:` line observes it at the close, owed. Beside it, a
  CR-terminated `Q<TAB>0<TAB>off<TAB>0` printed the off line; a parse with no `Q` row failed naming
  the missing row; a `P` row still failed. The `HEAD` engine's branch over the four-field row printed
  `SPEC_AUDIT_PIN_CUTOFF=2026-01-01<TAB>1` and no exempt count, the red.
- AC5 — `grep -n -B3 '^SPEC_AUDIT_PIN_CUTOFF=' .memory-tree.conf` — the three comment lines above the
  key, 804 to 806, read "the writer test (TOOL-dTrueNorth-14): a record whose adding commit's review
  harness lacks `renderAuditBinding` prints no P row". Over `HEAD` the same three lines were the
  `git log -1` reading and THE COST paragraph, naming neither, the red.

Over the real tree, `--print-bindings` printed `Q<TAB>0<TAB>2026-10-22<TAB>0`. With the cutoff passed
in-process as 2026-10-01 it graded 39 `spec-audit` records and exempted all 39, each added under a
harness that predates `renderAuditBinding`.
