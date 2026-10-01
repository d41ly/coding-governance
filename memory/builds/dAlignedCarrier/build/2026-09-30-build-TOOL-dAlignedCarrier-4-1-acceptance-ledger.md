# TOOL-dAlignedCarrier-4 — acceptance ledger

**Serves:** journal TOOL-dAlignedCarrier-4

`--status` now reports check 73's pinned `asks:` line and check 58's holder worktree as fields on
its one line, pass included, through `check_asks_moved` and `derive_holder_where`, the predicates
the two refusals now call too. The stop contract's §8 paragraph and the comment above `verb_resume`
no longer tie regrounding to the no-id spelling. One scratch fixture under `%TEMP%` run against the
BASE and the built driver, the arms report, greps, `cmp` and the adopter's `--check` stood in for
the `unattended kit gate`, `harness arms` and `unattended skill wiring` legs. No suite ran: the new
suite arms are written and their run is not observed here, under the build README's waiver.

**Evidences:** TOOL-dAlignedCarrier-4
- AC1 — `· asks as pinned · worktree holds the run` — the fixture printed the built line as one
  stdout line ending in those two fields; with them cut out it equalled the line of the BASE
  driver extracted by `git archive 87c245b3`, and with a stop-guard listing planted the last field
  was still `keepalive k1 present`. With `asks` and `lease-utc` deleted both drivers printed
  identical bytes.
- AC2 — `asks moved at HEAD, check 73 refuses a resume` — printed on the one status line with
  `pinned [EXMP-aFoo-3..4] at HEAD [EXMP-aFoo-3]` after the fixture committed a moved `asks:` line,
  and the no-id `--resume` over the same commit printed `UNATTENDED check 73 FAILED`.
- AC3 — `worktree not the run's, check 58 refuses a resume here` — from the main worktree on
  `other`, followed by the path `git worktree list` gives the linked worktree holding the run
  branch; the no-id `--resume` there printed `UNATTENDED check 58 FAILED`. The linked worktree read
  `worktree holds the run` and no refusal field. With both branch facts deleted the main worktree
  read `worktree unanswerable` and its resume only announced it; with `lease-utc` deleted no
  worktree field printed.
- AC4 — `git status --porcelain` — and `git hash-object` of the record read the same before and
  after `--status` over the passing, moved, wrong-worktree, unanswerable and no-lease states, which
  exited 0 each time with no `FAILED` in its output. The same 34-check fixture pointed at the BASE
  driver printed six `FAIL` lines, one per field arm.
- AC5 — `check 73 branch 1  line 3581  ARMED` — `python tools/memory-tree/check-arms.py --report`
  printed that and `check 58 branch 1  line 6308  ARMED`; `grep -c 'fail 73 '` and
  `grep -c 'fail 58 '` over the driver printed 1 and 5, their BASE counts.
- AC6 — `in sync (skill rendered from template + .unattended.conf)` — the adopter's `--check`
  exited 0 after the render and `cmp` of the template and its render exited 0. The regrounding
  grep printed 0 over the render against 2 at BASE, the driver's `method's no-id spelling` grep
  printed 0 against 1, and the rewritten paragraph names `--status` and checks 58 and 73.
- AC7 — `16` — the five-spelling `grep -c -E` over the suite printed 16, where BASE prints 0. The
  arms sit in a new region-two block after the ask-mandate block; their run is the close bar's.
