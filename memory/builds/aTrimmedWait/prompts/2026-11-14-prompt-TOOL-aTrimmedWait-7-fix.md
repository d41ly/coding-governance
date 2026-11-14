# Fix — TOOL-aTrimmedWait-7: three lexicon offenders and a vacuous arm

**Serves:** research TOOL-aTrimmedWait-7

## The prompt

The main loop's pass-legs run over 9b0b45057..519bc24db reported, quoted:

> lexicon: verb offenders 1211 over pin 1208

The three new definitions are the suite helpers `a23` and `a23_cold` in `tools/roles/adopt-roles.test.sh`,
whose leading token is unruled, and the inline copy of `common_git_dir` in `tools/roles/handoff.py`.

The unit's own builder also reported, on its pass commit 519bc24db, quoted:

> In arm 23 as committed, three assertions can pass when there is no record to edit, because nothing checks that the record edit itself ran: the warm-mtime check, the transcript-edit check and the foreign-key loop. ... The fix is three small changes: check the edit's exit code in the poison step and in each foreign-loop step, and require a `*.json` to exist before the find-newer test.

## The brief

### Goal
Clear the lexicon leg and make arm 23 unable to pass vacuously, with no behaviour change in
`handoff.py`. Rename `a23` and `a23_cold` to names the lexicon accepts
(`python tools/lexicon/lexicon.py --suggest <name> --as sh.function`). The inline `common_git_dir`
must stay byte-identical to `tools/lib/common_dir.py`'s, so raise `VERB_OFFENDER_PIN` in
`.lexicon.conf` by one for it, with a `RE-MEASURED` comment in the shape of the PLAY-dOrderedCharter-49
row above the key, read off the lexicon's own measure. In arm 23, check the record edit's exit code in
the poison step and each foreign-key step, and require a `*.json` record to exist before the
find-newer test. Re-render the codebase map for the renames. Set the header CLOSED again as the last commit.

### Items
1. `tools/roles/adopt-roles.test.sh` holds no `a23` or `a23_cold` definition.
2. `.lexicon.conf` pins the measured verb-offender count, with its re-measure row.
3. Arm 23's three assertions each fail when the record edit did not run.
4. The acceptance ledger gains one row for this fix.

### Acceptance
- `python tools/lexicon/lexicon.py --check` exits 0.
- The pass's scratchpad probe `r6probe.py` prints PASS for all seven cases, as at 519bc24db.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
Copied from the build's brief: no verdict change, and no narrowing of the full hygiene run, the bar,
or `--dispatch`'s own refusals. No rename of the inline `common_git_dir`: the resolver parity leg
compares it to its canonical byte for byte.

### Limitations
Copied from the build's brief: every speed-up is keyed on what it read; measurements on node a, one
at a time; long suites on a frozen clone.

### Reuse
The `RE-MEASURED` rows above `VERB_OFFENDER_PIN` in `.lexicon.conf`.
