**Serves:** journal TOOL-dDerivedDocket-5

# TOOL-dDerivedDocket-5 — acceptance ledger

Every observation below was made in the build pass by a DIRECT check: the kit gate run over a
fixture conf, the adopter run over a rendered fixture repository, the driver run over a scratch
fixture repository with its own bare origin, the `kit.toml` discharge probe run over a fixture conf,
or a read of the tracked files. No gate leg, no merge bar and no self-test suite ran in this pass.
Four criteria carry a `permission:` line deferring their observation and get no line here: AC7,
whose arms live in a suite on no bar leg, AC10 and AC13, which grade the real or rendered tree, and
AC14, the attributed unattended run the main loop makes at VERIFYING.

**Evidences:** TOOL-dDerivedDocket-5

- AC1 — `bash tools/unattended/check-unattended.sh` — over a fixture conf declaring
  `RESUME_SCHEDULE="maybe"` check 36 reds naming the key and the set it read off the driver's marked
  line (`on off`); over one with the key absent it prints `RESUME_SCHEDULE on (defaulted)` and reds
  on no account of it.
- AC2 — `bash tools/unattended/check-unattended.sh` — over a fixture conf whose
  `RESUME_SCHEDULE_CREATE` and `KEEPALIVE_CREATE` are both `CronCreate`, check 36 reds naming both
  keys and the value; over one declaring the switch on and neither carrier key it reds once per key.
- AC3 — `--hold` — on a scratch HELD-capable fixture with `--until "after 2099-01-01T00:00:00Z"` the
  record gains `resume-owed: unattended-resume-trun · fire 2099-01-01T00:00:00Z` — the condition's
  own instant, not `held-at` plus the delay — and the verb prints the name line, the fire line and
  the three prompt lines, the second spelling `--keepalive-id` and the third telling a refused or
  `still held` session to delete the keepalive it scheduled, list its scheduler's jobs to confirm,
  and leave the named task in place. `--status` then prints
  `resume · unattended-resume-trun · fire 2099-01-01T00:00:00Z · streak 1 · at <sha8>`.
- AC4 — `--until "probe host"` — the same fixture records
  `unattended-resume-trun · fire <held-at + 1800s>`, computed against the `held-at` the record
  carries; with `--until owner` it records `none · owner`, prints `resume-owed none · owner` and
  prints no prompt line at all.
- AC5 — `EXMP-injected-text` — a hold whose `--reason` carries that literal prints it zero times in
  the whole of `--hold`'s output, prompt included, and `--status` carries it on exactly one line,
  the quoted `reason ·` line.
- AC6 — `hold-streak` — a fixture declaring `RESUME_SCHEDULE_LIMIT="2"` holds (streak 1, a schedule
  owed), commits that hold together with a new row in the build's `BACKLOG.md`, resumes, commits the
  take-over, and holds again: streak 2 and `resume-owed` `none · limit`. A third hold after a commit
  touching `progress.txt` writes streak 1 and owes a schedule again.
- AC8 — `--scheduled` — `--resume tRun --scheduled <held-at> --keepalive-id C` against the matching
  HELD record completes the take-over, records `keepalive: C`, and writes
  `resume · item tRun · reason held · keepalive C · scheduled`, observed both with the remote at the
  pre-hold witness and with the hold commit pushed; a manual restart of the same record writes the
  same row ending `manual`. The same call without `--keepalive-id` refuses, numbered, with the
  run-state file's blob hash unchanged.
- AC9 — `bash tools/unattended/adopt-unattended.sh --check` — over a rendered fixture whose conf is
  on and declares no carrier, the render refuses naming `{{RESUME_SCHEDULE_CREATE}}` and `--check`
  exits 1 naming the same placeholder in the render it just made; with `RESUME_SCHEDULE="off"` the
  render carries the fixed literal `not scheduled: RESUME_SCHEDULE is off` in place of both tool
  names and `--check` exits 0.
- AC11 — `--close` — on a fixture whose history holds one hold row that owed a schedule, it prints the
  reap list beside the keepalive id: `keepalive kC · durable schedule unattended-resume-trun`.
  `--abort` prints the same line before it asks for the attestation, and a fixture whose holds owed
  none says so instead of naming a task nobody filed.
- AC12 — `memory/DECISIONS.md` — its TOOL heading carries one row keyed `TOOL-dDerivedDocket-5`
  recording the owner's on-everywhere ruling and the charter §9 override, 292 characters against the
  300-character entry budget.
- AC15 — `tools/unattended/kit.toml` — the conf-placeholder hole's discharge command, read out of
  the descriptor, exits 1 over a fixture holding the shipped example with its three `KEEPALIVE_`
  lines filled and its two resume placeholder lines verbatim, and exits 0 once those two are filled
  as well. Staged RED by reverting the probe to the `KEEPALIVE_(CREATE|DELETE|INTERVAL)`
  alternation, under which the first fixture exits 0.
- AC16 — `git cat-file -s` — `memory/guides/UNATTENDED-PROTOCOL.md` and
  `tools/unattended/PROTOCOL.template.md` each go 60275 bytes at the parent to 60036 at this commit
  and 673 lines to 673, against the 61440 and 750 resolved from the single
  `tools/memory-tree/check-memory-hygiene.sh` line that declares `GUIDE_CAP_BYTES` and
  `GUIDE_CAP_LINES`. The trim landed:
  `grep -c 'A DECLARATION rather than a path in the driver'` counts 2 at the parent and 0 here, both
  sentences are in `tools/unattended/README.md`, and the `RECALL_CLI` and `MAP_CLI` cells keep their
  meaning and their OPTIONAL terms. The owed row arrived: `grep -c 'RESUME_SCHEDULE'` counts 0 at
  the parent and 1 here, one joined first cell. `UNATTENDED-STOPS.md` reads 23997 bytes and 377
  lines at the build commit and 24059 bytes and 377 lines after the checklist fold that follows it,
  under both halves of the same cap either way. No cap was raised.
