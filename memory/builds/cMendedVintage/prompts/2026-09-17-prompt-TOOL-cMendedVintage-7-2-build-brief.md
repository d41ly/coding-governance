# Build brief — TOOL-cMendedVintage-7

**Serves:** journal TOOL-cMendedVintage-7

Read the spec whole first. This is a SMALL unit — one loop added to a file the previous unit shipped
an hour ago — and the main risk is doing more than it asks.

*Standing note: sixteen briefs in this build carried a figure or mechanism measurement disproved, and
every one of the last nine units amended its own spec mid-build after measuring. Treat this as
evidence, not authority.*

## None of the meta-gates fire this time

`TOOL-cMendedVintage-6` shipped the leg, its descriptor row, its manifest row and its pin row one
unit ago, and six declarations had to move together. You add NO new leg, NO descriptor row and NO pin
row — you are adding a loop inside a file that is already declared. Do not re-run the declaration
dance; it will only produce a diff nobody asked for.

Read what that unit landed first, including its four built-in fixture arms, because S4 asks you to
add the fifth and sixth into that same harness rather than a new one.

## The one-word precision that is the whole unit

S1 keys on the EXACT string `evidence: "unattributed"`, never on the field being absent. Absence is
the synthesized-class state and is not a synonym for unattributed. Testing truthiness or absence
instead of the exact value is the same class that has already bitten two units in this build, both
times by silently changing which rows are in the graded population.

## S3 is not the skip rule, and do not "fix" it into one

With zero such rows the loop prints NOTHING. That looks like it contradicts the announced-skip rule
the previous unit was held to, and it does not: a SKIP says an arm went unexercised, while this is an
arm that ran and found nothing. A line that always appears carries no information and trains a reader
to skip it. Leave it silent on zero.

## It is a NOTE, and the reason it is a note is checkable

The loop does not fail the leg and does not become a failure in this build. The printed remedy
`govkit adopt --re-adopt --pin <path>=<rev> --write` only works after `DEPL-cMendedVintage-4`, which
is CLOSED at order 5 in this build — so the remedy your note points at does work in this release. The
note stays a note anyway: the spec's argument is that the release which fixes the remedy should not
also be the release that starts redding on it.

S5 wants one header sentence saying so and naming the follow-up that would make it a failure, so a
reader is not left deciding whether a silent note is a bug.

## The count is DERIVED

The spec cites 47 of inCMS's 95 rows from `DEPL-dGaugedVintage-8`. That is a historical measurement
of another repository at another time — do not carry it into a message, a comment or a test
expectation. Your fixture's count comes from your fixture.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf` — Python is a parser-mode language
here, so every definition is graded. Spell no `tools/<kit>/…` path in shipped prose or comments. The
file is a shipped `.py` written on Windows: check the STAGED bytes for CR.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-TOOL-cMendedVintage-7-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED. Keep every backticked span
whole on its own line — hygiene check 23 is HELD under `--staged`, so no commit hook will tell you a
witness is on the wrong line. Re-declare with `--dispatch` if your write set grows; `--dispatch`
refuses a declaration naming `RUN.md`. Bound every command at 900s or more.
