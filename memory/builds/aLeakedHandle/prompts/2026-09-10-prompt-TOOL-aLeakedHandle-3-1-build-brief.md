# Build brief — TOOL-aLeakedHandle-3

**Serves:** journal TOOL-aLeakedHandle-3

The pass this brief was handed to builds unit 3 of `aLeakedHandle` at rev-2. The spec is
`memory/builds/aLeakedHandle/spec/2026-09-10-spec-TOOL-aLeakedHandle-3.md` and it is authoritative.
This is the smallest unit of the build and the discipline is to keep it that way.

## What the pass builds

The rc=137 branch of `report_one` in `tools/run-gates/run-gates.sh` prints `$WORK/<i>.sec` — the same
value the ledger reads as field 2 — instead of `$WORK/<i>.bound`, which is the DECLARED CEILING. The
false `timed out` verb goes with it; the ceiling stays as a separate labelled field.

The defect, observed: a leg killed by an operator at 4168.392 s was reported as
`(timed out after 16040s, killed)` while `<git-dir>/gate-ledger.tsv` recorded the true 4168.392. The
summary and the ledger disagreed by a factor of four on the same run.

## What the audit already decided

- **rc=124 is deliberately left printing the ceiling.** There the ceiling IS the true cause, and two
  live arms pin it. Do not "fix" it.
- **The no-ceiling case is out of scope** and carries a backlog row. §8 F1 has a RESOLVED mark. Every
  leg in `tools/gate-legs.json` declares a ceiling today, so that branch would ship dead.
- **The wall-guard kill path is settled and your §4 states it correctly at rev-2**: `.pid` holds the
  `runleg` subshell's own `$BASHPID`, `scan_descendants` seeds its kill set with that root pid, so
  the subshell is SIGKILLed, neither `.sec` nor `.rc` is written, and `report_one` returns
  `(no result)` at its `[ ! -f "$WORK/$i.rc" ]` guard before any tail is built. Your new `.sec` read
  is safe because that branch is UNREACHABLE on the wall path, not because the file exists. Unit 1's
  AC2 third `Red when:` clause is the agreeing side and needs no change.

## The rules this pass is bound by

- The acceptance observation is a STAGED BREAK: a fixture leg running `kill -9 $$` under a declared
  ceiling of 600, asserting the seconds in the `GATE FAIL` tail equal that leg's `gate-ledger.tsv`
  field 2 byte for byte, observed RED against the unfixed source first.
- **Prove your arm actually ran.** The unit-2 pass had an observation driver report six breaks as
  unobserved because nothing had executed — a mangled path, exit 127, and an empty FAIL list is
  indistinguishable from a clean one. Assert a positive artifact of the work per arm.
- Commit at the end of the pass with the unit id in the subject, then run
  `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names first.
- Flip the spec's status header in the same commit as the code.

## What the pass must not do

- Do not redesign the summary format. Do not touch the ledger. Do not change any verdict. Only what
  the failure line SAYS.
- No sibling unit's files. Units 1 and 2 are CLOSED; leave `derive-ceilings.py`,
  `lib-unattended.sh` and the two new gate-lint legs alone.
- No ceiling VALUE is re-declared anywhere.
