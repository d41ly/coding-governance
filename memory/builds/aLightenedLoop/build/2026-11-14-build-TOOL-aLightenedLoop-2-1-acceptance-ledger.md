# TOOL-aLightenedLoop-2 — acceptance ledger

**Serves:** journal TOOL-aLightenedLoop-2

No merge bar, no self-test suite and no gate ran in this pass. The criteria a probe can reach were
observed in the spec's probe fixture, `wakefix.sh` as §4 states it, built under `%TEMP%/wkfx` with
the base driver from `846d51d39` in `u0/` and this pass's driver in `u/`. The fixture's one change
from §4 is that its `rm -rf` also clears `$F.proc`, the orphan case's procfs stand-in. The helpers
`run`, `run0`, `<reg>`, `<age>`, `<stale-beat>`, `<orphan>`, `<remote>` and `<norm>` are §4's,
sourced from one scratch file; `$F` is spelled `C:/...`, so a heartbeat path is absolute to
`--register-task`. AC2's `abandoned` and `asks moved` breaks insert the fact on the line after
`phase:`, inside `## Run facts`, which is where `fact` reads; appended under `## Parked` the fact is
not a fact, and both the wake and the pair then read it as absent.

The parity rule's captures: AC4 compares the base and built driver's stdout and exit code per verb
after `<norm>`, in one fixture per scenario, and `git status --porcelain` after each side. The
timings are AC5's.

**Evidences:** TOOL-aLightenedLoop-2
- AC1 — `run --wake tWake --keepalive-id k1` — after `<reg>` in a fresh fixture it exited 0 and
  printed the one line `unattended-wake: tWake · HEALTHY · tasks 1 open · cadence every 10 minutes`;
  `git status --porcelain` printed nothing and `git hash-object <rec>` matched before and after.
  Through `run0` the same call is check 14's unknown argument, exit 1.
- AC2 — `· FULL · <reason> ·` — each staged break after `<reg>` printed, exit 0: `phase HELD`,
  `abandoned`, `asks moved`, `worktree`, `holder` (`--keepalive-id k2`), `lease` (`pid: 999`),
  `claims unread` (`RUN_CLAIMS="on"`, no remote), `claim` (`<remote>`), `orphans` (`<orphan>`),
  `tree idle` (`<age>`) and `task stalled` (`<stale-beat>`, `TASK_STALL_BOUND="60"`). After
  `run --resume tWake --keepalive-id k1` the `claim` fixture's wake printed `HEALTHY`. The pair then
  printed check 106, check 73 and check 58; `git ls-remote "$F.bare" refs/gov/runs/tWake` listed the
  claim; `reaping is OFF because PROCMON_CMD is blank, so 1 orphan(s)`; one `· STALLED` unit line;
  and one `task wf · ` line with `· STALLED`.
- AC3 — `run --release-task tWake --task wf` — with the tracked key and `<reg>` the line ended
  `· tasks 1 open · cadence every 30 minutes`, and after `run --release-task tWake --task wf`
  `· tasks 0 open · cadence every 10 minutes`. Without the key both lines named `every 10 minutes`.
  `KEEPALIVE_INTERVAL=""` with no task ended `cadence undeclared`, and so did a conf with no
  `KEEPALIVE_INTERVAL` line at all, exit 0 under `set -u`.
- AC4 — `<norm>` — `--audit tWake`, `--liveness tWake`, `--status tWake` and
  `--resume tWake --keepalive-id k1` through `run0` and then `run` printed identical normalised
  output and the same exit code after `<reg>`, after `<age>`, and after `<stale-beat>` with
  `TASK_STALL_BOUND="60"`: 12 of 12 pairs SAME, every exit 0. The `w2` register and release pair <!-- PINNED 2026-11-14 -->
  printed the same two lines on both drivers. `git status --porcelain` printed nothing after every
  call. Beyond the criterion, the lease row the `check_lease_current` extraction touches: with
  `pid: 999`, `--resume tWake --keepalive-id k1` printed the same normalised output on both drivers
  and staged the same normalised record diff.
- AC5 — `run --wake tWake --keepalive-id k1` — timed in the clone at `%TEMP%/wkreal`, its origin set to
  `%TEMP%/wkreal.bare` and pushed there, this pass's driver and library copied in, a `tWake` README
  and run-state file with `run-branch: refs/heads/branch/alightenedloop-eb7b8b` committed. Node `a`, <!-- PINNED 2026-11-14 -->
  load average 6.07 before and 4.51 after, 16 CPUs. Three `run --wake tWake --keepalive-id k1`: <!-- PINNED 2026-11-14 -->
  1534, 1595 and 1549 ms, median 1549 ms, each `FULL · claim` because no claim was on the bare yet. <!-- PINNED 2026-11-14 -->
  Three `run --resume tWake --keepalive-id k1` then `run --audit tWake`: 6499, 5817 and 6096 ms, <!-- PINNED 2026-11-14 -->
  median 6096 ms. After the pair wrote the claim, three more wakes read `HEALTHY` at 2909, 2951 and <!-- PINNED 2026-11-14 -->
  2844 ms, load 4.66: the healthy path reaches the tree-clock scan the claim row skips, and is still <!-- PINNED 2026-11-14 -->
  under the pair. `git ls-remote` of the real origin listed no `refs/gov/runs/tWake`, the bare
  listed one, and the real repository holds neither `refs/gov/runs/tWake` nor its cache ref.
- AC6 — `bash tools/unattended/adopt-unattended.sh --check` — the close's to observe: scratch-guard
  refused it here as the `unattended skill wiring` leg. Observed in this pass: the renders were
  written by `bash tools/unattended/adopt-unattended.sh`; both `cmp` calls printed nothing;
  `grep -c 'unattended.sh --wake ' .claude/skills/unattended/SKILL.md` printed 1, the verbs
  carrier's `--wake` entry grep 1, the protocol's `KEEPALIVE_TRACKED_INTERVAL` grep 1, the driver
  header grep 1, the conf example grep 1, the `kit.toml` grep 1, and the
  dossier `memory/map/features/unattended.md` grep for the old `--audit` sentence 0. The manifest's `last-audit` is
  re-stamped at this pass's base `b8477b3c`; `bash skills/session-kickoff/manifest-check.sh` is the
  close's, the `kickoff-manifest ratchet` leg.
- AC7 — `python tools/govkit/docs_leg.py --fingerprints` — the row reads
  `verb:unattended.sh:--wake` with `ef8efa49` and `help/idle-wake.md`, and the page's anchor
  `verb:unattended.sh:--wake ef8efa49 -->` greps once. `docs_leg.py --list --undocumented` printed
  no `--wake` id. `grep -c '(idle-wake.md)' help/README.md` printed 1. `verb:unattended.sh:--help`
  kept `965e3eb2`, so the header line moved no other verb's anchor.
- AC8 — `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh` — printed 319. <!-- PINNED 2026-11-14 -->
  `check_lease_current` and `check_tree_progressing` each grep 3, and
  `grep -c 'UNIT_STALL_BOUND" ]'` prints 1, the line inside `check_tree_progressing`.
- AC9 — `tools/template-size-limits.txt` — the CR-stripped renders measure 10744 for <!-- PINNED 2026-11-14 -->
  `.claude/skills/unattended/SKILL.md` and 68216 for `memory/guides/UNATTENDED-PROTOCOL.md`; each <!-- PINNED 2026-11-14 -->
  row is that figure, its comment `by TOOL-aLightenedLoop-2`, and the `**TOOL-aLightenedLoop-2**`
  row of `memory/DECISIONS.md` greps 1. `wc -c < memory/guides/UNATTENDED-VERBS.md` printed 97806, <!-- PINNED 2026-11-14 -->
  900 above its base of 96906 and under 98304. <!-- PINNED 2026-11-14 -->

## Owed at the close

- The `New arm:` lines of §7, all in `tools/unattended/unattended.test.sh`, RED against the driver at
  `846d51d39` and GREEN at the tip: the `wake` AC1 arms after the task-registry block, the AC2
  `check_wake_full` arms beside them plus the `orphans` hit in the process-ledger AC4 block, the AC3 cadence
  arms, and the parity table's `wake` row.
- §7's legs, `bash tools/unattended/run-unattended-gates.sh --pooled`, and the merge bar.
