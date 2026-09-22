**Serves:** journal TOOL-aHoistedPass-3

# Acceptance ledger — TOOL-aHoistedPass-3

Tier-2 · node a · 2026-09-05 · landed at `f13c071a`

`BUILD-METHOD.template.md` declared its own budget in prose and no checker read the figure. The byte
half is now an integer, declared where the existing size gate already looks, with one term that stops
the number drifting between the document and the declaration.

## Acceptance criteria

**Evidences:** TOOL-aHoistedPass-3

- AC1 — MET — `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` exits 0 printing one
  `template-size OK` line naming the measured bytes against `27648`, and its output carries NO
  `no-ratchet` line. The `no-ratchet` clause is what makes this criterion able to fail: before S9's
  `--bump` the same command exited 0 while announcing that the growth it was built to price was
  unpriced.
- AC2 — MET — the staged break. Filler appended to a scratch copy past 27648 exits `1` with
  `the file is over its size budget: big.md is 30745 bytes, 3097 over 27648`. Scratch only; the
  tracked subject and the tracked limits file were never written.
- AC3 — MET, both directions — prose moved and row unmoved exits `6` naming `'30000'` against
  `27648`; row moved and prose unmoved exits `6` naming `'27648'` against `30000`.
- AC4 — MET — a scratch copy whose budget line is rewritten to `≤27 KB` exits `6` with
  `'no bytes figure'` in the message, so a prose rewrite cannot disarm the term.
- AC5 — MET — `AGENTS.md`, `skills/session-kickoff/SKILL.md` and
  `coding-governance-agents.template.md` each exit 0 with zero `check 6` lines: each has a declared
  row and no `^**Budget:` line, which is the second guard.
- AC6 — MET — `bash tools/check-template-size.test.sh` exits 0 with 28 arms held, including the two
  the spec asked for and two controls it did not: an agreeing pair is not a check 6, and a declared
  subject with no budget line is never compared.
- AC7 — MET — `python3 tools/memory-tree/check-arms.py --check` exits 0 with the new `fail 6` branch
  ARMED rather than pinned, against the floor S10 raised from `6:6` to `7:7`.
- AC8 — MET — `govkit selfcheck` exits 0 reporting `legs: 94 in the manifest · 69 claimed · 25
  exempt`, one more leg and one more exempt than before, which is what proves the `[[exempt_leg]]`
  row exists and carries a `subject`.
- AC9 — MET — `python3 tools/codebase-map/test_codebase_map.py` exits 0 and
  `gen_map.py --check` exits 0, so the dossier claim landed and the artifacts were regenerated in the
  same commit.
- AC10 — MET — `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0: the render came from
  `--render` and not from a hand edit.
- AC11 — MET — `bash skills/session-kickoff/manifest-check.sh` exits 0 with `last-audit` re-stamped,
  which four watched paths in this diff required.
- AC12 — OWED AT THE PUSH BOUNDARY, not met here: the one open row, and it is `run-gates.sh` in full.
  `bash tools/run-gates/run-gates.sh` in full, reporting `build-method size` among its legs, is a push-boundary
  observation; the build method runs the full bar ONCE, there. What was run here is every leg the
  diff reaches, individually, each named above.
- AC13 — MET — `tools/template-size-highwater.txt` carries a row keyed on
  `memory/guides/BUILD-METHOD.md`, written by `--bump` and not by hand.
- AC14 — MET — `grep -c 'No gate enforces the pair'` returns `0` in both the template and the render,
  and the sentence that replaced it names the `build-method size` leg and states that the LINE axis
  stays ungated.
- AC15 — MET — `bash tools/check-kit-versions.sh` exits 0 with `KIT_MEMORY_TREE_VERSION` and every
  tracked `memory-tree` marker at `2.61`; staging `HYGIENE.template.md` back to `2.60` exits non-zero
  NAMING that carrier, and restoring it returns to 0.
- AC16 — MET AS AMENDED — the header names 4 and 6 beside 1, 2, 3 and 5, and its `Exit <n> =` codes equal
  the file's distinct `FAIL_CODE` values: header `[1,2,3,4,5,6]`, assigned `[1,2,3,4,5,6]`.

## What the spec could not have known

**A staged break can pass while proving nothing, and this one did on its first cut.** The gate keys a
subject outside the repo on its ABSOLUTE POSIX path — the form `cd && pwd` answers — and the scratch
limits file was written with the drive-letter form the shell was handed. Every row missed, the gate
fell through to its 49152 hard default, and all four arms passed. The tell was that none of them went
RED, which is the fixture-passes-by-finding-nothing class. Recorded in the test file's own header so
the next author of a scratch-subject arm does not repeat it.

**AC16 could not pass as first written.** It compared the header's whole exit set to the `FAIL_CODE`
set, and the header documents exit 0, which is never a `FAIL_CODE`. Corrected before it was graded.
