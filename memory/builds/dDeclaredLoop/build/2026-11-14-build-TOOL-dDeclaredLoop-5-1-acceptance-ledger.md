# TOOL-dDeclaredLoop-5 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-5

No merge bar, no self-test suite and no gate leg ran in this pass. The `loop definition` leg's command,
`loop_lib.py --check`, and the unattended leg, `check-unattended.sh`, were not run as commands. The
criteria were observed on node `d` (win32) by probes of the unit's own code: `python -c` calls importing
`loop_lib` from the loop kit's directory, `loop_lib.main` called with each plant, the `--grade-site`
verb run as a command, check 53's block cut out of the leg and sourced under stub helpers, a scratch git
repository with a bare origin under a short temp directory, and the `grep`, `cut` and `bash -c` commands
the criteria spell.

Owed to the close: every leg the spec's section 7 names; AC7 as the criterion spells it, a staged
`DOD_EXTRA` and a real `--only 53` run; and the RED-first observation of both `New arm:` lines. The
first is the `witness-actor-unlisted` plant of `tools/loop/loop_lib.py`, staged by having
`check_actor_list` skip its unlisted-actor loop. The second is check 53's two arms in
`tools/unattended/check-unattended.test.sh`, staged by an unclassed entry in `mkconf` and by the loop
kit's directory removed beside the copy. That suite is waived under README rule 8, so its reading is
owed with PLAY-dClosedLoop-13.

**Evidences:** TOOL-dDeclaredLoop-5
- AC1 — `--check` — its parts, called in-process over gov's tree: `read_witness_classes` returned the
  three classes and `actor`; `check_witness_classes` returned one `history` witness per step;
  `read_actor_base` returned no comparison, the list being absent at the base it resolved;
  `check_actor_list` over the shipped list, that answer and the step sites returned no refusal. The red
  case: the same data with `step.build`'s `witness` removed raised `LoopError` naming `step.build`; a
  definition with no `[witnesses]` table raised naming the missing table.
- AC2 — `witness-no-class` — exit 1 naming `step.plan`'s witness with no class; `witness-bad-class`
  exit 1 naming `agent-said`; `witness-actor-unlisted` exit 1 naming `step.plan`;
  `witness-actor-listed` exit 0 printing `step.plan · until dWellOiledMachine`.
- AC3 — `actor-list-grown` — exit 1 naming the added `DOD_CORE reuse-probed` row; `actor-list-stale`
  exit 1 naming the `step.design` row; `actor-list-no-build` exit 1 naming `dNoSuchBuild`. In the
  scratch repository a row added on a branch was refused against the list at the merge-base with the
  origin's tip. The earlier plants `disposition-alias` and `missing-step` printed their messages as
  before.
- AC4 — `rc=1` — the `bash -c` the criterion spells printed `rc=1`, then `machine`.
- AC5 — `cut -f2,3 actor-witnesses.txt` — printed `keepalive-reaped` with `dWellOiledMachine` and
  `parked-decisions-surfaced` with `dShippedRelease`, nothing else.
- AC6 — `--grade-site DOD_CORE` — the three entries printed with their classes, exit 0; `DOD_EXTRA b`
  exit 1 naming `b`; `DOD_EXTRA b:said` exit 1 naming `said`; `DOD_EXTRA b:agent` exit 1 naming the
  missing row `DOD_EXTRA b`; `DOD_CORE gates-green:machine` exit 1 naming the two `DOD_CORE` rows. The
  driver's whole `DOD_CORE` graded exit 0, and a site outside `DECLARATION_SITES` exited 2.
- AC7 — `UNATTENDED check 53 FAILED` — check 53's block, sourced under stub helpers with the driver's
  `DOD_CORE`: `DOD_EXTRA` `b` printed that line quoting the refusal naming `b`, and set the status to 1;
  an empty `DOD_EXTRA` printed only its report line and kept the status at 0. With no loop kit, and
  with no python, the second branch printed, naming which. The `--only 53` run itself is owed.
- AC8 — `docs_leg.py --fingerprints` — its `loop_lib.py` row printed `036bc6db`, the fingerprint the
  `usage:` anchor in `help/loop.md` now carries, and `grep -c -- '--grade-site' help/loop.md` printed 1.
- AC9 — `grep -cE` — the census printed 266; the token grep printed
  `tools/unattended/check-unattended.sh:266:2026-11-14:TOOL-dDeclaredLoop-5`; the decision-row grep
  printed 1.
