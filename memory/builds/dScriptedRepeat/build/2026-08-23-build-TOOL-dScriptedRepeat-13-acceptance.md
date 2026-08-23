**Serves:** journal TOOL-dScriptedRepeat-13

# TOOL-dScriptedRepeat-13 — the acceptance record

Node `d`, 2026-08-23. One line per numbered criterion, naming the observation that answered it. Every
one was observed on this tree; none is inferred from the code reading as if it would work.

**The unit moved file between rev-1 and rev-2 and that is the headline.** Rev-1 specced the scan into
`check-unattended.sh`, where check 11 lives. Measured before rev-2: `GITLS`, `declared_scalar` and the
playbook enumeration are all ZERO there and non-zero in `check-playbook.sh`. Building rev-1 would have
inlined a third copy of the parser past a gate that compares exactly two — so the scan is check 10 of
the playbook leg, and check 11 keeps run-state files. Two populations, two checks, each where its
machinery already is.

## The criteria

**Evidences:** TOOL-dScriptedRepeat-13

- **AC1** — `tools/unattended/check-playbook.test.sh` — a per-piece record with the flag appended reds
  check 10. Also observed on the REAL tree before any arm existed: appending the flag to
  `tools/unattended/fixture-records/set-dScriptedRepeat.md` red the leg, and restoring it went green.
- **AC2** — `tools/unattended/check-playbook.test.sh` — the set-scoped record, a different writer and a
  different path shape, reds the same way.
- **AC3** — check 11 in `check-unattended.sh` is untouched: the scan is a new check in a different
  file, no line of that one is in this diff, and the `kit gate` leg reports green at 28 s.
- **AC4** — both halves. The leg prints `bypass scan - <n> tracked evidence record(s) read` when a flag
  is declared and `bypass scan SKIPPED` when it is not, and an arm asserts each. On the real tree the
  count is 3, so a scan reaching zero is distinguishable from one reaching many and finding nothing.
- **AC5** — SHARING, not liveness, in `tools/unattended/check-playbook.test.sh` — the criterion rev-1
  could not have passed. The arm MOVES
  the declared `records` root — editing the playbook's declaration and `git mv`-ing the directory — and
  reds unless BOTH the census and the scan follow it. **Its own control was run:** hardcoding the
  scan's root to the old path makes the arm red with *"the census followed the moved root and the bypass
  scan did not, so the two readers derive their roots separately"*. A liveness arm would have passed
  over two independent derivations that agree today.
- **AC6** — `seed()` in `tools/unattended/check-playbook.test.sh` now writes a `.unattended.conf`
  declaring `BYPASS_BAN`. Without it every arm above grades the SKIP path while looking exactly like a
  clean scan.
- **AC7** — both record writers in `tools/unattended/unattended.sh` cite check 10 again. Round 2 found
  them citing check 11, which structurally cannot cover evidence records — a true refusal for a false
  reason — and the citation was removed rather than made true. The arm in
  `tools/unattended/unattended.test.sh` extracts the cited number and reds unless the playbook leg
  defines it; **control run:** rewriting the citation to `check 99` reds it.

## What this does not cover, and it is in the check's own header

`--record-set` accepts a caller-supplied records root, so a record written outside every declared root
is unreachable by check 10. That is the write-time guard's job and it holds there. Stated rather than
discovered, because coverage a reader assumes is total is worse than coverage whose shape they know.

## Counts at this commit

`check-playbook.test.sh` 99 assertions, up from 90. `run-unattended-gates.sh --checks` green: kit gate
28 s, playbook validity gate 12 s, skill wiring 0 s.
