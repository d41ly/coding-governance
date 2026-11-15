# TOOL-aLightenedLoop-7 — acceptance ledger

**Serves:** journal TOOL-aLightenedLoop-7

No merge bar, no self-test suite and no gate ran in this pass. The criteria a probe can reach were
observed in the spec's probe fixture, unit 2's `wakefix.sh` with its base sha moved to `5701fafd3`,
built under `%TEMP%/wk7` with the base driver in `u0/` and this pass's driver in `u/`. The helpers
`run`, `run0`, `<reg>`, `<age>`, `<stale-beat>`, `<orphan>` and `<remote>` are unit 2's, and each
criterion started from a fresh fixture.

**Evidences:** TOOL-aLightenedLoop-7
- AC1 — `run --wake tWake --keepalive-id k1` — with the retired key appended to the conf and `<reg>`
  run, it exited 0 and printed exactly
  `unattended-wake: tWake · HEALTHY · tasks 1 open · cadence every 10 minutes`. Through `run0` the
  same call exited 0 and printed `... cadence every 30 minutes`, the base's answer.
- AC2 — `run --release-task tWake --task wf` — with the conf's `KEEPALIVE_INTERVAL`, the wake after
  `<reg>` ended `· tasks 1 open · cadence every 10 minutes` and after the release
  `· tasks 0 open · cadence every 10 minutes`. With `KEEPALIVE_INTERVAL=""` set before `<reg>` the
  lines ended `· tasks 1 open · cadence undeclared` and `· tasks 0 open · cadence undeclared`. Every
  call exited 0.
- AC3 — `run0 --wake tWake --keepalive-id <id>` — twelve fresh fixtures, unit 2's AC1 setup and its <!-- PINNED 2026-11-15 -->
  eleven AC2 breaks, each printed the same line through `run0` and `run`, byte for byte, both exit 0: <!-- PINNED 2026-11-15 -->
  `HEALTHY` for the setup, then `FULL` with `phase HELD`, `abandoned`, `asks moved`, `worktree`,
  `holder` (`k2`), `lease`, `claims unread`, `claim`, `orphans`, `tree idle` and `task stalled`.
- AC4 — `python tools/govkit/docs_leg.py --fingerprints` — printed `verb:unattended.sh:--wake`,
  `ef8efa49`, `help/idle-wake.md`. The driver diff against `5701fafd3`, comment lines dropped,
  printed three lines: the init line removed and re-added without `KEEPALIVE_TRACKED_INTERVAL="";`,
  and the tracked-cadence `if` line removed.
- AC5 — `python tools/policy/policy.py lists --check` — exited 0 with `green · 0 finding(s)` and no
  line holding `KEEPALIVE_TRACKED_INTERVAL`. The `git grep -n` over the criterion's six paths
  printed nothing, and `git grep -l` listed only paths under `memory/builds/`.
- AC6 — `python tools/govkit/docs_leg.py --run --page help/idle-wake.md` — printed one `docs: run · `
  line naming the page, the marked block and the `run: no` reason, a summary ending `0 findings`, no
  `docs: RUN help/idle-wake.md` line, and exited 2 with its `REFUSED` line, as the criterion states.
  The block's line is DERIVED from the built page: 57. `grep -c 'every 30 minutes'` and the <!-- PINNED 2026-11-15 -->
  replacement grep over `help/idle-wake.md` each printed 0; `grep -c '(idle-wake.md)' help/README.md`
  printed 1.
- AC7 — `bash tools/unattended/adopt-unattended.sh --check` — the close's to observe: scratch-guard
  refused it here as the `unattended skill wiring` leg. Observed in this pass: the renders were
  written by `bash tools/unattended/adopt-unattended.sh`; both `cmp` calls printed nothing; the
  `other than your job` grep printed 0 for `.claude/skills/unattended/SKILL.md` and
  `memory/guides/UNATTENDED-VERBS.md`; `grep -c 'unattended.sh --wake '` over the Skill printed 1; the
  verbs carrier's `<c>` line grep printed 1. The manifest's `last-audit` is re-stamped at this pass's
  base `85d1d95d`; `bash skills/session-kickoff/manifest-check.sh` is the close's, the
  `kickoff-manifest ratchet` leg.
- AC8 — `tools/template-size-limits.txt` — the diff against `5701fafd3` printed no row line. The
  CR-stripped renders measure 10668 for `.claude/skills/unattended/SKILL.md` and 68060 for <!-- PINNED 2026-11-15 -->
  `memory/guides/UNATTENDED-PROTOCOL.md`, under the rows of 10744 and 68216. <!-- PINNED 2026-11-15 -->

## Owed at the close

- The `New arm:` line of §7 in `tools/unattended/unattended.test.sh`: the rewritten `--wake` AC3
  block, RED on its two staged breaks and GREEN once restored.
- §7's legs, the driver suite in the unattended kit's pooled tier, and the merge bar.
