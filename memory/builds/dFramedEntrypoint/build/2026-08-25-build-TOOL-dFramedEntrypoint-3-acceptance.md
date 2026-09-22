**Serves:** journal TOOL-dFramedEntrypoint-3

# Acceptance ledger — TOOL-dFramedEntrypoint-3

*Node d, 2026-08-25. Every refusal below was staged against the live tree and observed RED before it
was armed, then unstaged.*

**Evidences:** TOOL-dFramedEntrypoint-3

- AC1 — `assert_contract_registry` — dropping `aBoundedVerdict`'s row from the live registry and
  running `python tools/memory-tree/gen_build_index.py --check-format` exits 1 naming that path and
  saying a new build would escape the contract by existing.
- AC2 — `gen_build_index.py --check-format` — adding `!memory/builds/ghostBuild/README.md` to the
  live registry exits 1 naming that row as not a tracked build README.
- AC3 — `bash tools/run-gates/run-gates.sh` legs individually green with the registry present.
  The bound count is ZERO by design at this unit's landing, and the leg prints that rather than a bare
  clean line; the count rises at unit 7, which owns the conversion.
- AC4 — `exempt-pin` — set to 99 against a measured 62, `--check-format` exits 1 naming both numbers.
  The pin is an EQUALITY: it reds ABOVE the count as well as below, because a pin left high after a
  drain is slack nothing reports. Armed as `the pin ABOVE the measured count refuses, not only below`.
- AC5 — `memory/project/readme-contract.txt` deleted, `--check-format` exits 1 naming the expected
  path and saying the canon and the budgets would bind nothing and report clean.
- AC6 — `--check-format` exits 1 quoting an exempt row stripped of its ` - <reason>` tail.
- AC7 — `python tools/memory-tree/gen_build_index.py --selftest` — PASS, 110 `arm ok` lines against
  102 before this unit. Both assertion directions were watched failing against staged breaks first.
- AC8 — `gen_build_index.py --check-format` prints the tracked count, the BOUND count and the empty-
  population note on every run.
- AC9 — `bash tools/memory-tree/check-memory-hygiene.sh` — check 3 passes with the registry present,
  observed RED first against the same tree with the allowlist entry removed, then restored.

## The handover this unit makes explicit

Unit 1 shipped `read_contract_registry` returning the EMPTY SET when the file is absent — a pass —
deliberately, so that it did not depend on a file this unit had not written. This unit makes an absent
registry a refusal, and INVERTS unit 1's selftest arm in the same commit rather than leaving two arms
asserting opposite things about one contract. Two of unit 1's arms failed the moment this landed,
which is how the handover announced itself.

## Seeded state, stated plainly

62 exempt rows, 0 bound, pin 62. The contract binds NOTHING on the day it lands. That is the honest
starting state the owner's fork-1 ruling chose over the alternative, which was binding the whole
corpus and opening a thirty-row waiver.

## Found while building, and parked

`tools/dead-path-waivers.txt` is keyed on `<path>:<line>`. Four comment lines added to
`check-memory-hygiene.sh` for the check-3 allowlist moved a waived `STATUS.md` mention from line 550
to 554, and the dead-path leg redded. Re-keyed by hand. This repo has ALREADY recorded that this
keying is the wrong one — `adopt-memory-tree.sh` says of `method-carriers.txt`, "Keyed on PATH alone,
never `<path>:<line>` — that keying is what unpinned install-prefix-waivers.txt" — so the lesson
exists and this registry did not receive it. Parked rather than fixed: it is another kit's registry
and the two alternative keyings trade one failure for another rather than removing it.
