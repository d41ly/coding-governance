**Serves:** journal TOOL-aHoistedPass-9

# Brief — TOOL-aHoistedPass-9, the adopter without the harness is told, on every bar

*Read this, then read the spec whole. The spec is the design; this says what the spec cannot — what
the run around you has already decided, and what verification is actually owed.*

## Where this unit sits

Eight of the ten units of `aHoistedPass` are built, committed and CLOSED before you. In particular
`TOOL-aHoistedPass-2` has already landed the M6 route sentence and the seventeen directive anchors in
`memory/guides/BUILD-METHOD.md`, and check 16 arm B's body term that keeps them there. **Your check 31
reads the route those anchors name.** If M6 does not carry a backticked `workflows/*.js` path when you
run, that is a finding about the landed unit and not a licence to type `M6` into your own check — S2
is explicit that the section comes out of the directive registry the leg has already parsed.

## What verification is owed, and what is not

- **Do not run the full bar.** `bash tools/run-gates/run-gates.sh` is the push boundary's job, and
  the parent run owns that. M6 charges a build pass the DIFF-SCOPED gates for what it touched.
- **The kit gate has NO narrow form for your check, and this is measured rather than assumed.**
  `--only` takes `28` and nothing else — `check-unattended.sh:87` refuses any other value at exit 2,
  because checks 1 to 27 share state and are one unit. The sibling pass that built
  `TOOL-aHoistedPass-6` was told otherwise by a brief I wrote and reported the refusal; this is the
  correction. Your check 31 sits after check 30 and outside both `SCOPE` blocks, so `--only 28` would
  not reach it either. Run the whole gate, once, and budget for it.
- **Hand-run your own suite and report its exit code**: `bash tools/unattended/check-unattended.test.sh`.
  The 2026-08-23 owner ruling took the unattended kit's `*.test.sh` legs off the bar, so nothing
  standing re-checks your arms afterwards. That hand-run IS the compensating check. If it cannot
  finish, say what you observed rather than reporting a green you did not see.
- **A sibling suite in this same kit is KNOWN BROKEN, so do not misattribute a red.**
  `tools/unattended/unattended.test.sh` has never run to completion in either mode: unsharded it
  aborts under `set -u` on a bare `$1` inside a `case` pattern, and sharded it reds 54 times on
  region-two arms that depend on region-one state. Measured by the `TOOL-aHoistedPass-6` pass against
  a pristine clone and filed as `TOOL-aHoistedPass-36`. It is not your suite and not your unit's to
  fix — but if you touch it or read a red from it, that is the reason.
- **The arms meta-gate is not optional.** `python3 tools/memory-tree/check-arms.py --check` must exit
  0, and adding branches RENUMBERS the per-check ordinals — a stranded arm is silent, and only that
  gate notices.

## The bounds

- **Declare the write set first**: `--dispatch aHoistedPass --pass TOOL-aHoistedPass-9 --writes <path>`,
  one `--writes` per path. Widen before the commit if you find another file; narrowing is refused.
- **S7 IS SPENT and the spec says so in place.** `DEPL-aHoistedPass-1` took the `unattended`
  1.17-to-1.18 bump at order 2. You assert `bash tools/check-kit-versions.sh` exit 0 and move the
  version no further. AC11 carries no literal version for the same reason — a criterion that passes
  on another unit's work witnesses nothing about yours.
- **This unit is NOT an owner turn.** rev-3 re-derived that from the carriers it actually edits —
  `check-unattended.sh` and its test file, neither on ruling D1's veto-2 list. Do not reintroduce the
  bump-derived classification.
- **A `fail` message may not carry a bare positional**, and an arm must contain the branch's ENTIRE
  literal signature up to the first interpolation. End the sentence, then interpolate.
- **Flip the spec status header to `CLOSED` in the SAME COMMIT as the code**, and write the
  acceptance ledger a closed Tier-2 unit owes — one line per numbered criterion, `**Serves:** journal`,
  under `memory/builds/aHoistedPass/build/`.
- **Run `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` after the commit** and act on
  what it names before you stop. It takes a COMMITTED range; run before the commit it prints
  "touches no file", which reads exactly like a clean checklist and is not one.
- Commit. Do not merge and do not push — the landing is the parent run's act.

## One trap this area has already sprung on this repo

A guard that a binding pair EXISTS is not a guard that it COVERS, and an absence-only assertion passes
when the subject was never there. S3's five announced-skip branches are what keep check 31 from
reporting a reassuring zero: a check that cannot compare must SAY it did not compare, on the kit's own
REPORT channel, in the file's existing `check <n> skipped for <subject> — <why>` grammar. F2 of the
spec settles that each unresolved path gets its own line, because a skip whose subject is a set is the
shape this build exists to remove.
