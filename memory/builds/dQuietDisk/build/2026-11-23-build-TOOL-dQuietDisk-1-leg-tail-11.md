# TOOL-dQuietDisk-1 leg-tail 11 — spec-tokens self-test failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** spec-tokens self-test
- **Hash:** c4f8c81a73bd9c3bd70f2f72661e8de63e269192
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
arm ok    PG1 cited prints 'step cited moved 1 same 1' (got 'step cited moved 1 same 1 rc 1/1 graded 1')
arm ok    PG1 kit prints 'step kit moved 1 same 1' (got 'step kit moved 1 same 1 rc 1/1 graded 2')
arm ok    PG1 cutoff prints 'step cutoff moved 1 same 1' (got 'step cutoff moved 1 same 1 rc 1/1 graded 2')
warning: in the working copy of 'memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md', LF will be replaced by CRLF the next time Git touches it
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
arm ok    PG1 onespec prints 'step onespec moved 0 same 1' (got 'step onespec moved 0 same 1 rc 1/1 graded 1')
arm ok    PG1 AC4 after one spec's edit the run re-grades that spec alone
arm ok    PG1 AC5 an entry whose .inputs holds a run line, and one whose .json does not parse, are misses
arm ok    PG1 AC7 the input record of a cached run, cold and warm, is the plain run's bytes
arm ok    PG1 AC6 the run never writes the directory it reads, and each generation holds the live specs (generation ok)
arm ok    PG4 AC1 the generation lands in the named directory, every hit copied, and no .next name appears
arm ok    PG4 AC2 a named directory that does not exist is not created, and a file already in one survives the run
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
arm ok    PG4 AC3 SPEC_TOKENS_CACHE alone, and both variables naming one directory, leave the cache and its parent as they were
arm ok    PG8 AC1 a cached entry whose counts lack ao_bad is a miss, and the run prints the plain run's bytes
arm ok    PG8 AC2 a fresh counts set lacking ao_bad raises KeyError naming it, with no summary line
arm ok    TOOL-dGroundRules-40 check_writes_intersect and overlaps give each OVERLAP_PAIRS row its expected answer
check-spec-tokens: 2 of 291 assertion(s) failed
```
