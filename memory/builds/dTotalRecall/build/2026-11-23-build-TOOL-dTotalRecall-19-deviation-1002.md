# TOOL-dTotalRecall-19 deviation 1002 — the legacy-records table keeps its section cell verbatim

**Serves:** deviation TOOL-dTotalRecall-19

- **Departs from:** TOOL-dTotalRecall-19@rev-9
- **Hand-off:** spec-to-code
- **Before:** S7's [[ledger]] table of tools/govkit/registry.toml names population, leg, seed, key, fields path and section, drain, direction and home, and no verbatim key (TOOL-dTotalRecall-19@rev-9 S7).
- **After:** the table also carries verbatim = ["section"], so legacy_ledger.py#_parse_rows reads a numeric heading anchor in the section cell as a key, never as a line number.
- **Cause:** builder discovery
- **Reason:** 7 heading anchors of the tracked Markdown records are bare numbers (DERIVED, the builder's derive_anchor probe over tree_lib.record_paths at 9d7afdc6a), the first 2 in memory/builds/dScaffoldedMirror/build/2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md, and legacy_ledger.py#LINE_NUMBER_RE refuses such a key, so the seed would print a malformed row and leave the home unarmed; verbatim is the ledger factory's own escape for a key field that is not a line number (legacy_ledger.py#_check_table).
- **Evidence:** tools/memory-tree/legacy_ledger.py#_parse_rows and #_check_table; the seed's armed line in the pass commit
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dTotalRecall-19 under the build's author-recorded value (PLAY-dClosedLoop-4)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-19
- **Made-by:** lease-dTotalRecall
