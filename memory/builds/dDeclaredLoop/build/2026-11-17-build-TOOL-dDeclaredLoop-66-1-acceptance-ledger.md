# TOOL-dDeclaredLoop-66 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-66

No merge bar and no self-test suite ran in this pass, and no product file was written (F2). The criteria
were observed on node `d` (win32), at rev-4 of the spec, at this pass's base `677c81b50`: a `python -c`
probe importing `gen_build_index` in `tools/memory-tree/`, standing in for the five Parallel arms the
`build-index selftest` leg runs; and `grep` probes of the rendered regions and the readers, standing in
for nothing a leg runs. The section 5 sweep re-run at this pass's base held its design claims: steps 4,
38 and 39 of this build read `no`, step 2 of aTunedCompass reads `unknown`, the regions hold 128 PINNED
`yes`, 1529 PINNED `no` and 17 PINNED `unknown` rows over 214 PINNED READMEs, the lexicon offender pin
is 1215 PINNED, `SHARED_RECORDS` is not written, the refusal ceilings keep the driver at 343 PINNED and
the checker at 266 PINNED, and no edited path is on the kickoff watch list; its one stale figure is
deviation 663. This closes the round-2 spec audit's finding id 1, item H1, on the build's record.

Owed to the close: every leg section 7 names. Owed RED-first: none, since the unit adds no arm.

**Evidences:** TOOL-dDeclaredLoop-66
- AC1 — `derive_parallel_step` — the probe answered `['no', 'no', 'no', 'yes', 'no', 'unknown']` for one unit; two units declaring `tools/x.py`; `tools/sub/` over `tools/sub/y.py`; `tools/x.py` beside `tools/y.py`; the same with the second consuming from the first; and the second's writes None.
- AC2 — `| no |` — the grep printed two rows, step 4 over specs 16, 37, 38, 39, 40 and 57 and step 38 over specs 66, 67, 74 and 80, each ending `| no |`.
- AC3 — `FILES_TOUCHED_HEAD` — `read_spec_writes(text)` counted 1 PINNED in each of `tools/check-spec-tokens.py` and `tools/memory-tree/gen_build_index.py`; `FILES_TOUCHED_HEAD` counted 2 PINNED in `tools/memory-tree/design_lib.py` and occurs in no other file under `tools/`.
- AC4 — `| unknown |` — the grep printed one row, step 2 over aTunedCompass units 10, 11 and 2, ending `| unknown |`.
