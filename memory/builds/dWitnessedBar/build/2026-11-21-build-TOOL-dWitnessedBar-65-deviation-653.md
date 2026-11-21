# TOOL-dWitnessedBar-65 deviation 653 — AC8's upper-case abbreviation lengthens past 8 where HEAD's first 8 characters are all digits

**Serves:** deviation TOOL-dWitnessedBar-65

- **Departs from:** `TOOL-dWitnessedBar-65@rev-5`
- **Hand-off:** spec-to-code
- **Before:** §6 AC8 gives `seed --sha` HEAD's first 8 hex characters in upper case, and section `2o`'s `New arm:` in §7 covers AC8 with that case.
- **After:** the arm in `tools/lib/resolve-python.test.sh` takes HEAD's first 8 characters, or the shortest longer prefix holding a letter, upper-cased, and asserts that the upper-cased value differs from the lowercase prefix before it counts the armed rows.
- **Cause:** builder discovery
- **Reason:** the fixture's HEAD is a fresh commit, so its sha varies by run, and a first 8 characters of digits only, (10/16)^8 or about 2.3% of runs, upper-cases to itself: the case would then pass without the fold S10 adds ever being read, a vacuous case. The lengthened prefix is still an abbreviation that must resolve, so AC8's red condition, a sha naming no commit stamped, is graded unchanged.
- **Evidence:** a scratch probe of the canonical `tools/lib/legacy_ledger.py` over a one-commit `git init` at `%TEMP%/u65s`, HEAD `0ce518f0…`, armed `p` from `--sha 0CE518F0` with rows at HEAD's full lowercase sha, exit 0. (DERIVED from the builder's probe)
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dWitnessedBar-65
