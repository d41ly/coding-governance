# TOOL-dQuietDisk-1 leg-tail 22 — line-length gate selftest failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** line-length gate selftest
- **Hash:** ad03d1d534acbc04df40190c60c26b7a4713757c
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
# run-gates | leg line-length gate selftest | exit 1
ok    control · a short subject passes
ok    an over-length line reds naming the line and its length
ok    with no policy kit beside the gate a breach refuses as before, saying so
ok    under budgets.enforce warn an over-length line prints BUDGET WARN and passes
ok    exactly at the limit passes
ok    the DECLARATION beats the environment
ok    an UNDECLARED subject honours the environment
ok    an undeclared subject with no environment falls through to 450
ok    a POSITIONAL beats the declaration
ok    a long line INSIDE a fence does not red
ok    a long line inside a TABLE does red
ok    a non-ASCII line is measured in CHARACTERS, not bytes
ok    a row naming an ABSENT path reds as stale
ok    a NON-NUMERIC limit is a named failure, not a shell error
ok    a declaration selecting NO subject is cannot-run
ok    a non-numeric POSITIONAL limit is a named failure, not a certified zero
ok    a non-numeric LINE_MAX is a named failure, not a certified zero
ok    a subject with NO gradeable line is a dead probe, not a clean verdict
FAIL  a scanner that dies mid-run is a named failure, not a certified zero — expected rc 1 naming 'the offender scan did not run for this subject, so no line was measured and OK would be a lie', got 0: line-length OK — subject.md: 0 over 450 characters (limit from the declaration) 
ok    an ABSENT declaration is NOT ADOPTED at exit 0, not a red install day
----
FAIL (1 of 20 arms, width 1)
```
