# TOOL-dQuietDisk-1 leg-tail 17 — template size gate selftest failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** template size gate selftest
- **Hash:** 74e106227097578fe485831df63c80878a8f7dc8
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
arm ok    A25c a refused policy file reaches check 8, which prints the reader's refusal
arm ok    A25d ...and its clause no longer names the handed-in default as the cause
warning: in the working copy of '.governance/policy.toml', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tools/template-size-limits.txt', LF will be replaced by CRLF the next time Git touches it
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
arm ok    A24 with no python launcher an over-cap subject refuses at check 5
arm ok    A3 a missing subject exits 2
warning: in the working copy of '.governance/policy.toml', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tools/template-size-limits.txt', LF will be replaced by CRLF the next time Git touches it
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
arm ok    A4 CRLF at the limit still exits 0
arm ok    A7 at the recorded high-water: no warn
arm ok    A6 one byte past the high-water warns AND exits 0
arm ok    A6m the warning's next line is the marker, keyed as its high-water row
arm ok    A7m at the recorded high-water: no marker
arm ok    A8 --bump re-records and names the delta
arm ok    A8b the row now holds the measured size
arm ok    A9 bumping one subject leaves the other row untouched
arm ok    A10 an absent RECORD says so and exits 0
arm ok    A10b a record with no ROW for this subject says so and exits 0
arm ok    A13 an unwritable record is a named failure, not a false BUMP
arm ok    A11 a non-numeric row is a NAMED failure, not a shell error
arm ok    A12 the record key is the literal repo-relative path
arm ok    harness left the tracked high-water record unmodified
check-template-size.test.sh FAILED — 1 arm(s)
```
