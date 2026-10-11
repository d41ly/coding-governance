# Acceptance ledger — TOOL-aSparedSpawn-8

**Serves:** journal TOOL-aSparedSpawn-8

Node `a`, 2026-10-11, bash 5.3.9 under MSYS. The pass ran no bar, no suite, no held leg and no slice
of a suite. Every check below is a changed program invoked directly, a checker run on a staged break
in a scratch copy, a `--selftest` flag, or a fixture built by hand in the pass's scratch root; the
before side of each comparison is the code at `4d2240a1d`, which the unit's spec commits leave unchanged, unless it says base
`22efab65`. `bash -n` passed on every changed shell file, the three converted suites, the two suites
whose spelling-coupled lines moved, and the extractor. Fork counts read no clock, so the runs that
shared the host are still exact counts. The converted driver was also run whole: `--status`,
`--plan` and `--liveness aSparedSpawn` through the parent's driver and the converted one gave
identical output but for `--liveness`'s wall-clock age.

**Evidences:** TOOL-aSparedSpawn-8
- AC1 — `grep -o '\$(fact '` over the driver, and the old and new `fact` bodies run on a hand-built
  `RUN.md` — no site is left; for a key above `## Run facts`, a valueless key, a CRLF line, a value
  with inner and trailing spaces, a key under `## Parked` and an absent key, the bytes of `_fact` were
  identical to what the old reader's substitution yielded (`52 55 4e 4e 49 4e 47`, empty,
  `61 20 20 62 20`, `76 31`, empty, empty); a read of a missing file after a hit returned 1 and left
  `_fact` empty.
- AC2 — check 39's block of `tools/unattended/check-unattended.sh`, run alone with `DRIVER` pointed at
  a scratch copy of the driver — on the unbroken driver it graded clean, so `C39-READERS-SEEN` was
  reached; with the converted `fact "$rel" phase` read moved into `verb_status` (check 39's own first
  arm, re-anchored) it redded naming `unattended.sh:7728 … inside verb_status()`. With `main` taken
  off the allow-list the unbroken driver redded naming `main()`, which is why the row was added. Two
  whole-checker runs over the tree were started first and stopped after 100 minutes unfinished.
- AC3 — the parent's `core_of` and `read_bare_const` against the one-pass readers, both over the
  driver with a key declared twice, an unterminated quoted line above a closed one, two bare integers
  and a non-digit bare value appended — all 161 `^[A-Z_]+=` keys answered identically: the first
  declaration won, the unterminated line was skipped, the first integer won, an absent key read empty.
- AC4 — `tools/gate-lint/sh_hygiene.py --spawn-idioms` and the per-callee count behind each row — the
  only reader S1 to S3 name that keeps a site in a converted file is `declared_scalar` and
  `declared_list` (7 in the driver, 8 in `check-playbook.sh`), and both rows' reason names check 28
  of the unattended gate, which reads that spelling; every other callee a converted file still
  carries is named with its count in that file's row.
- AC5 — `python3 tools/gate-lint/sh_hygiene.py --selftest` — PASS (81 assertions), each class firing
  on its specimen and silent on its near miss, a quoted-heredoc specimen and a commented one firing
  nothing. Two breaks staged in scratch copies each turned it RED: a BANNED row honoured instead of
  refused, and `$(<f)` with no second redirect graded a site.
- AC6 — `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt .
  ':!*.test.sh' ':!memory/'` over the tree — exit 0, each class's scanned, gated and near-miss counts
  printed, 0 sites for each BANNED class, 2099 registered sites in 292 rows; over a scratch copy of the
  shell population with `x=$(date +%s)` appended to `tools/check-wiring.sh` it exited 1 printing
  `tools/check-wiring.sh:1772: [epoch-date] x=$(date +%s) — use $EPOCHSECONDS…`, and with a pathspec
  selecting nothing it refused with 2. Every count in the registry was derived by the scan.
- AC7 — the parent's `resolve_kit_dir` wrapper against the converted one in `lib-unattended.sh`, over
  a hand-built receipt, a probe-only kit and a refusal, each plain and under `set -e` — all six
  stdout, stderr and exit codes identical; under `set -e` both hits ran on to the next command, so
  the `read -r -d ''` at EOF aborts nothing, and the refusal exited 1 in both.
- AC8 — `sh_hygiene.py --spawn-idioms` over the same scratch copy — one converted driver site put back as `ka=$(fact "$rel" keepalive)`
  exited 1 naming `tools/unattended/unattended.sh: the registry declares 40 site(s) at
  pure-fn-subst and the scan measures 41`; the one registered `pure-fn-subst` site of
  `check-unattended.sh` renamed out of the class with its row left exited 1 naming that row as one
  the scan no longer finds. The scratch copy's own unbroken run redded on rows for extensionless hooks
  its file filter dropped, which is the copy and not the tree.
- AC9 — `bash tools/gate-lint/fork-count.sh --selftest` — the specimen counted 5 forks on both runs, equal to its declaration, and a scratch copy with
  `SPECIMEN_FORKS=6` refused with exit 2 and the line "the counter cannot move"; PASS (2 assertions),
  repeated on the final file.
- AC10 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt <scratch root> --only
  unattended-status --sites` over a scratch repository holding the kits with `_ac10=$(:)` inserted
  below the driver's `set -u`, and over its unbroken twin — the staged root redded `measured 48 ·
  ceiling 47 · delta +1 · base 57` with the top ten `file:line` sites and the `--sites` hint, the twin
  read `ok … measured 47`, and the two `--sites` tables differed by `unattended.sh:58` alone once the
  sites below it were shifted back by one line. A first staged root that was no git repository read
  76, which is why every fixture here is a repository.
- AC11 — `bash tools/gate-lint/fork-count.sh <copy of the ceilings> .` — with `check-wiring` raised to 54 against its count of 50 (max(3, 5 %)
  is 3) redded `STALE ceiling 54 is more than 3 above the measured 50`, and a row whose setup is
  `exit 3` printed `skipped — unbuildable · its fixture setup exited 3…` and the summary read `0 passed
  · 1 red · 1 skipped`.
- AC12 — `bash tools/gate-lint/fork-count.sh` over each fixture, the tree at base `22efab65` and at
  the pass's tip side by side — forks per invocation, base then tip: `unattended-status` 57 → 47, `check-unattended` 709 →
  684, `run-gates-1leg` 72 → 72, `run-gates-2leg` 97 → 95, `memory-hygiene` 219 → 221 (the fixture
  copies the tree's conf, which grew), `manifest-check` 108 → 108, `check-wiring` 55 → 50. Every tip
  count repeated exactly on three runs except `run-gates-2leg`, which read 95, 95, 95 and 96, its pool
  polling its workers; its ceiling is 96 and the rest sit at their counts. The driver entrypoint is
  lower at the tip. A full run against the landed ceilings passed six rows and redded that row at 96
  before its ceiling moved; the leg's own green run over the final file is owed at VERIFYING.
- AC13 — `grep -cE '\$\((rec|review_out|derive_sidecar|audit|audit_rc) '` over the three suites — 0, 0
  and 0, and no `pure-fn-subst` row names `stop-guard.test.sh` or `transition-audit.test.sh`;
  `unattended-build.test.sh`'s row carries only `build_gh33_writer`, `build_dispose` and
  `build_gh33_args`, outside S10's helpers. `rec`, `review_out` and `derive_sidecar` write their
  global with `printf -v`, `audit` assigns its capture and `audit_rc` its status, each whole, so no
  trailing newline and no earlier value survives a call. The suites' own runs are owed at
  VERIFYING.
- AC14 — `2026-10-11-build-TOOL-aSparedSpawn-8-arm-inventory.sh` over each converted suite at the
  parent and after — the (helper, message) multisets were equal, 756, 170 and 136 calls, and
  `FLOOR_ASSERTIONS` stayed 566, 121 and 64; the staged deletion of one assertion line printed that
  pair. The `PASS (<n> assertions)` figures of the parent and child runs are owed at VERIFYING, with
  the record in `2026-10-11-build-TOOL-aSparedSpawn-8-arm-inventory.md`.

**Owed at VERIFYING**, because only a suite run observes them: the three converted suites and their
inventory PASS figures; the GH37 race arms of `tools/unattended/unattended.test.sh`, re-hooked from
`date` onto `mkdir` and `rm`; check 39's first arm in `tools/unattended/check-unattended.test.sh`
on its moved anchor; the driver suite's `_at` grep and `readme_of` stub; and the new legs on the bar,
with the meta-gates a new leg trips.
