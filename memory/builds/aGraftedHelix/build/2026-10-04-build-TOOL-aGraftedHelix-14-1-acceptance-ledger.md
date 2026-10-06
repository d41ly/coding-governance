# Acceptance ledger — TOOL-aGraftedHelix-14

**Serves:** journal TOOL-aGraftedHelix-14

Node `a`, 2026-10-05. The build commit is `92e5c514`, over the dispatch records commit `7b41ee2a`.
No merge bar and no self-test suite ran in this pass. The direct checks were the engine commands
AC1 and AC2 name, run over the copy-install fixture the new arm builds, and a slice of the suite:
its prologue plus the new block alone, run from scratch with fixtures under `%TEMP%`, green at 4
arms. Each of the four arms was observed RED on a real staged break, each made in a scratch copy of
the kit and never in the tracked tree: the block's `status=1` deleted redded the branch arm, its
green-run print deleted redded the clean-main arm, its `add_offender_keys 27` line deleted redded
the `--offenders` arm, and the runner's `GOV_DEFAULT_BRANCH=main` pin removed redded the ambient arm.
The block unit 9 built needed no repair, so S2 owed nothing beyond the version line.

The base row is `ARCH-tOne-1 - rotation archives keep terminal rows only, and a live row never moves
into one`. The branch row is `ARCH-tTwo-1 - a live row is never moved into a rotation archive, which
holds only terminal rows`, a new slug so the own-session rule does not end its grading. Measured at
0.462, sharing `live`, `never` and `rotation`. Its words and their order differ from the base row's,
so no normalised content key can equal it. Checks 13 to 15 arm nothing in this fixture, because it
declares no pin, as the `_b1` tree it copies does. The new id is well-formed, but only check 16 grades it.

**Evidences:** TOOL-aGraftedHelix-14
- AC1 — `check 27:` — the fixture's copy of `tools/memory-tree/check-memory-hygiene.sh` on its branch under `GOV_DEFAULT_BRANCH=main` exited 1 and printed `check 27: ARCH-tTwo-1 (memory/DECISIONS.md:4) near-matches ARCH-tOne-1 at 0.462`, with no other line opening `check <n>:` and no `HYGIENE check` line. With `status=1` deleted in the fixture's copy it exited 0, and restored it exited 1.
- AC2 — `row-grammar: check 27 graded` — the same command on the fixture's `main` exited 0 and printed `row-grammar: check 27 graded 0 added record(s) in bb7cdb87..HEAD against 1 at base`. With `GOV_DEFAULT_BRANCH=no-such-branch` exported, the pinned run still exited 0, while the same run unpinned exited 1 with `check 27 is armed and found no mainline base`.
- AC3 — `bash skills/session-kickoff/manifest-check.sh` — at `92e5c514` it exited 0 and printed no `MANIFEST check 5 FAILED` line, and `python tools/govkit/govkit.py epoch --base 7b41ee2a` printed `epoch: memory-tree · clean · 2.124` with exit 0.
