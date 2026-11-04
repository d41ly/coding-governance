# PLAY-dOrderedCharter-64 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-64

Each line is a probe this pass ran, at rev-1 of the spec: the spec's scratch run of
`check-memory-hygiene.sh` over a committed fixture repository under the host temp directory, once at
base and once with the pass applied; a `grep` over the touched files; and an awk replay of the
rev-scope predicate over spec 4's revision log. The `memory-hygiene self-test` suite, its three new
arms' RED-first observations, the `memory hygiene` leg, the other legs the spec's section 7 names and
the merge bar are the main loop's at the close: a role agent runs none of them. This record cites no
code line.

**Evidences:** PLAY-dOrderedCharter-64
- AC1 — the scratch run's `grep -c 'tFixture-95.md (revision entries'` printed 0 with the pass applied; at base it printed 1
- AC2 — the same run's `grep -c 'tFixture-96.md (revision entries'` printed 0 with the pass applied; at base it printed 1
- AC3 — the same run's `grep -cF` for the full `tFixture-90.md` refusal ending `REV_SCOPE_CUTOFF 2026-08-20): rev-2` printed 1, at base and with the pass applied
- AC4 — the same run's `grep -cF` for the full `tFixture-97.md` refusal ending `REV_SCOPE_CUTOFF 2026-08-20): rev-2` printed 1, at base and with the pass applied
- AC5 — the rev-4 `grep -c` printed 1, `grep -c 'hygiene-fix-brief'` printed 0 and `grep -c '^- rev-'` printed 4
- AC6 — OWED: `check-memory-hygiene.sh --only 12` from the repo root did not return inside its 280 s bound and was skipped. Stand-in: an awk replay of the arm's three disjuncts over spec 4's rev-2 to rev-4 entries printed `pass` for each with the words disjunct and `RED` for rev-4 without it, the base predicate under the rewritten spec
- AC7 — `grep -c 'section <n>'` printed 2, 2, 1, 1, 1 and 1 over the two spec templates, the two hygiene templates, the example conf and the dogfooded conf; the `REV_SCOPE_CUTOFF=""` default's comment names no token list and no check number
- AC8 — the `git diff -U0` from the pass base piped through `grep -cE '§[0-9]|check [0-9]|M[0-9]'` over the added lines printed 0
