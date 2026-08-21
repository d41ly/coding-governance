# TOOL-dUnstalledConvoy-24 — built, with each arm observed RED before its fix

**Serves:** journal TOOL-dUnstalledConvoy-24

Two scope items, two arms, both observed failing against the pre-fix code and passing after it. The
staged break is named per arm below, which is what AC5 asks for.

## The arms, and the break each one was observed against

| arm | break staged | observed |
|---|---|---|
| S1 — `--close` names the commit | `COMMIT the run-state file, then land with:` reverted to `Land with:` | `FAIL missing: COMMIT the run-state file` |
| S2 — the refusal names the other tree | the `_elsewhere` worktree scan deleted from `verb_landed` | `FAIL missing: an UNCOMMITTED LANDING is sitting in:` |

Both restored, suite green at 524 assertions, up from 519.

## Two fixture defects this pass hit, and what they cost

**A literal path compare failed on working code.** The S2 arm first asserted the refusal contained
`$OTHER`, the path `mktemp -d` produced. The driver prints the same directory in Windows form
(`C:/Users/...`) while the fixture holds the MSYS form (`/tmp/...`), so the arm redded against a
correct implementation. Debug output is what separated the two readings — without it the obvious
conclusion was that the scan did not work. The arm now asserts the discriminating PHRASE, and the
negative control differs from the positive one only in the other tree's phase.

**An arm was inserted between a `before=$(sum)` capture and its assertion.** The S1/S2 block ran
`reset_tree` and `--preflight` in between, so a pre-existing arm measuring "the refused `--landed`
wrote nothing" compared a fresh sum against a stale capture and failed. Nothing was wrong with either
arm; the insertion point was. Moved past the pair.

Neither is a finding about the kit. Both are worth recording because both LOOKED like findings about
the kit for several minutes, and the second is a hazard of any suite whose arms share fixture state.

## What was NOT built

The staged-blob read and the `--abort` parity that rev-1 of the spec proposed. Both are listed OUT
with their reasons: `fact()` reads the working tree so the staged discriminator is empty in both trees
of the recorded incident, and `refuse_if_terminal` fires check 26 before check 31 is reached.

**Evidences:** TOOL-dUnstalledConvoy-24
- AC1 - `tools/unattended/unattended.test.sh` - the close success message names committing the run-state file, asserted on the first arm that already observes a successful close.
- AC2 - `tools/unattended/unattended.test.sh` - a second worktree holding LANDING makes the refusal name it; asserted on the discriminating phrase because the fixture and the driver spell the same directory differently.
- AC3 - `tools/unattended/unattended.test.sh` - the negative control on the SAME fixture, differing only in the other tree's phase, gets today's message.
- AC4 - `tools/unattended/unattended.test.sh` - both cases still REFUSE; the `a run reaches LANDED only from LANDING` assertion holds in each.
- AC5 - `2026-08-21-build-TOOL-dUnstalledConvoy-24-1-red-first.md` - the table above names the break staged per arm and the failure observed.
- AC6 - `bash tools/run-gates/run-gates.sh` - run over the built tree; the verdict is recorded in this build's landing report.
