# Acceptance ledger — TOOL-dLoggedFlight-1

**Serves:** journal TOOL-dLoggedFlight-1

Tier-2 · node d · 2026-09-13 · the build pass of the runlog kit, against spec rev-5. Every line is
OBSERVED. Where a criterion was answered by something other than what it names, the line says so.

## The criteria

**Evidences:** TOOL-dLoggedFlight-1

- AC1 — `python tools/govkit/govkit.py selfcheck` — rc 0 with `runlog` an entry, `runlog selftest` on
  an `[[exempt_leg]]` row, and its subject pin regenerated. The codebase-map leg is green with the new
  dossier claiming the kit and the leg. Selfcheck does NOT red when the self-test turns landable:
  deleting its `project-owned` rule left it at rc 0. That condition is observed by `govkit plan` into a
  scratch target, which lists `selftest.py` and all four fixtures as `ORDER [project-owned]` and only
  the four engine files as `write`, and by the self-test's declaration arm. Spec rev-6 rewrote AC1 to
  name those two, after the checklist over the build commit found rev-5 had amended only its log. The
  same plan exposed a defect: a `fixtures/**` element claimed nothing, because a list include drops
  glob elements, so each fixture is now named.
  RED seen three ways. Removing the registry entry took selfcheck to rc 1 with `tools/runlog`
  unclaimed. Removing the dossier's leg claim took the coverage leg to rc 1, UNCLAIMED. Three
  declaration breaks each redded the arm: a fixture left off the list, a glob instead of the list, and
  `role = "engine"` on the self-test.
- AC2 — `parse_line` in `test_ac2_escape_round_trip` — twelve values carrying TAB, LF, CR,
  backslash, literal `\t` text, `=` and non-ASCII round-trip byte-identical, and a hand-escaped line of
  the kind a shell producer writes unescapes correctly. RED seen with the escape dropped on write
  (2 arms) and with it dropped on read (15 arms).
- AC3 — `tools/runlog/fixtures/journal-mixed.txt` through `read_journal` — 3 lines and a bad count of
  2. The dotted uppercase key, two indexed keys and `zz_unknown` are all kept, and each refusal is
  named. RED seen with a bad line silently dropped: the count read 0.
- AC4 — `tools/runlog/fixtures/invocations.txt` through `build_invocations` — `ended`,
  `killed-or-running` and `orphan-end`, and a `once` line is no invocation. Over 100,000 lines the
  patched `re.compile`, `re._compile` and `subprocess.Popen` counted 0 and 0, and a liveness probe
  moved both counters. Wall time is 0.7 s, report-only. RED seen three ways: an unmatched start read
  as ended, a per-line compile counted 200000, and a per-line spawn was refused and counted.
- AC5 — `runlog: <path> absent` — in a scratch clone with no journal, `journal --producer driver` exits
  0, prints that line on stderr with `<path>` the clone's `<common-dir>/runlog/driver.log`, and prints
  nothing on stdout. RED seen with the absent line removed.
- AC6 — `bash tools/run-gates/run-selftests.sh --kit tools/runlog` — `ok runlog selftest 2s` against
  its 60 s budget row, at 183 assertions against a floor of 183. AMENDED to that runner, which the
  criterion's cost line allows: the unit runs only the new leg and never the held chunk. RED seen
  three ways. Deleting the budget row took `run-selftests.sh --check` to rc 1. Deleting the dossier
  claim took the coverage leg to rc 1. A copy with its floor raised to 184 exited 1, "under its floor".
- AC7 — `tools/runlog/selftest.py` `test_ac5_ac7_ac9_journal_and_root` — the primary tree and a
  linked worktree of one scratch clone resolve one absolute `<common-dir>/runlog`. A control shows the
  linked tree's own git dir IS under `.git/worktrees/`, and the CLI names the same path from both
  trees. RED seen with `--git-dir` (7 arms) and with `--path-format=absolute` dropped (3 arms).
- AC8 — `tools/runlog/fixtures/golden-lines.txt` — the driver START and END, the gate line and the
  push START parse with a bad count of 0. Every key in them passes `check_line` alone. A line of 30
  indexed fields renders at or under 2048 bytes, with `ref_more` counting the drops, highest index
  first, and no value cut. RED seen three ways: the key grammar lowercased (14 arms), cutting before
  dropping (3), and a producer's own `_more` overwritten (2).
- AC9 — `python tools/runlog/runlog.py journal --producer driver` over
  `tools/runlog/fixtures/driver-torn.txt` — two JSON objects whose keys equal the fixture's, split
  without the kit's parser. stderr carries `lines=2 bad=1`, the resolved path, and why line 3 was
  refused. Checked from both trees. RED seen with the count omitted and with the torn tail uncounted.
- AC10 — `tools/runlog/selftest.py` `test_ac10_memory_root` — `docs/mem/` reads as `docs/mem`, and an
  unset key or an absent conf reads as `memory`. `/`, an empty value, `""`, `../x`, `docs/../../x`,
  `C:/x` and a backslash each refuse with a line naming `MEMORY_ROOT`. RED seen five ways: a literal
  `memory`, an empty root accepted, `..` accepted, a drive accepted, and two of the sourcing rules.

## Staged RED

41 breaks, each applied to a COPY of the kit in a scratch dir, never to the working tree. All 41 went
RED. 37 of them failed a named arm. The other four crashed the suite with a traceback rather than a
named arm: the required-key, unknown-escape, lone-backslash and cut-splits-an-escape breaks. That
still exits 1. A second byte-cap test that sat inside `read_journal`'s loop was deleted before the
sweep rather than graded: `parse_line` owns the cap, so no arm could have turned that copy red, and a
branch nothing can arm reads as coverage.

## Residue

- The brief's one-line leg runner resolves `bash` through Python's `subprocess` on this node. That
  reached WSL's bash, and the three bash legs exited 2 with "not a git repository". Each bash leg was
  run directly under Git Bash instead, and all were green.
- `playbook parity` reds on a kit directory neither the charter template nor the runbook names. That
  was confirmed by running it with the new waiver row removed, and the row is why it is green.
