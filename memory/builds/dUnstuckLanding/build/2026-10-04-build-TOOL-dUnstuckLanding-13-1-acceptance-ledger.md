# TOOL-dUnstuckLanding-13 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-13

No merge bar and no self-test suite ran in this pass. The driver criteria were observed through
hermetic probes assembled from the suites' own setup: the driver suite's prologue, its hold
fixture and the new hand-off arms, run on throwaway repositories under the user temp directory,
and the leg suite's prologue with its new arms the same way. The probes reported 73, 26 and 10
assertions passing. A staged break, a guard that admits any verdict, made the same driver probe red
on exactly the AC4 refusal and its no-write assertion. The suites themselves, the runlog and
drift-audit self-tests and the runlog record schema leg are owed to the close.

**Evidences:** TOOL-dUnstuckLanding-13
- AC1 — `hold-code: owner-landing` — under `LANDER_MODE="in-place"` over a seeded GREEN bar, the
  record read `phase: HELD`, `hold-code: owner-landing`, `hold-until: owner`, `resume-owed: none ·
  owner` and `units-at-landing: ARCH-tRun-1`, with one `handoff · item owner-landing` row whose
  reason carried `--prepare --slug tRun` and `--land --slug tRun` and not the free-text reason.
- AC2 — `run_hold` — over a dirty tree the hand-off printed the dirty-tree refusal and over a HELD
  record the already-HELD refusal, both `run_hold`'s text, and the record's blob hash was unchanged.
- AC3 — `--handoff` — `--hold` naming `owner-landing` and `owner-decision` each printed the fail 89
  text naming `--handoff`, and the record's blob hash was unchanged.
- AC4 — `its attribution reads` — a RED bar with leg `x` seeded `OWN` printed fail 83 ending in
  `its attribution reads x OWN` with the record unchanged; seeded `INHERITED` it was admitted; with
  no `gates-run` fact it printed `no gates-run fact in this record names a bar`.
- AC5 — `ran at` — a bar at the parent of a records-only HEAD was admitted; with a second path
  committed it was refused with `the bar it names ran at`. Over the records-only tree, `--close
  --override gates-green` and the out-of-scope `--abort` were each still refused with `ran at`.
- AC6 — `--park tRun --item q --reason r` — `owner-decision` over a record with no decision row
  printed fail 91 and wrote nothing; after a `--park` it was admitted over an OWN red.
- AC7 — `asks-at-landing:` — over the self-filed ask fixture the hand-off wrote
  `asks-at-landing: EXMP-tDispF-1=CLOSED`, the value `--landed` freezes over the same shape; with
  the stub answering nothing it printed fail 92 with the witness's DEAD PROBE reason and wrote nothing.
- AC8 — `LANDER_MODE="primary"` — the row read `in the primary tree: git merge --no-ff unit && echo
  land` and named no `--prepare`; with `LANDER` blank the hand-off printed fail 93 and wrote nothing.
- AC9 — `undocumented in the protocol: HANDOFF_CUTOFF` — the leg over the fixture printed that line
  with the protocol row removed, printed the import allow-list line naming `HANDOFF_CUTOFF` with its
  entry removed, and printed neither with all three in place.
- AC10 — `--abort tRun --code external-prerequisite --reason r` — under a `2026-01-01` cutoff the
  abort printed the notice naming `--handoff` and wrote `phase: ABORTED`; under `2099-01-01`, blank,
  a malformed value, and with `fork-unresolvable`, no notice printed and every abort proceeded.
- AC11 — `has shrunk below its floor` — both confs carry `HOLD_FLOOR="7"`, `grep -c` printing 1 in
  each, and the leg over a driver copy without `owner-decision` printed the pin with `6 against 7`.
- AC12 — `VERBS.template.md` — the Skill template invokes the verb as the grep asks, the verbs
  carrier has one `--handoff` entry, the stops carrier names `owner-landing`, and the protocol
  template names `HANDOFF_CUTOFF` twice.
- AC13 — `bash tools/unattended/adopt-unattended.sh --check` — it exited 0 after the re-render, and
  `cmp` reported no difference for the PROTOCOL, STOPS and VERBS template and render pairs.
- AC14 — `python tools/memory-tree/check-arms.py --report` — fail 89 to 93 and the new fail 10 branch
  read ARMED, `check-arms.py` exited 0, and neither unarmed-branch registry was touched.
- AC15 — `_RUN_PARK_KINDS_OWED` — a direct comparison read both driver sets equal to the drift-audit
  and runlog copies, each holding `handoff`, and the runlog `LEDGER_SOURCES` leading with the owed
  kinds then the two acts; a control with `handoff` dropped from the driver read unequal. The two
  runlog test functions this pass edited, called directly, passed all 32 of their checks.
