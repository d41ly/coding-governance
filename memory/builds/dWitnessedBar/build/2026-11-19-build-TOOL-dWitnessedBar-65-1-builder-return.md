**Serves:** journal TOOL-dWitnessedBar-65

# TOOL-dWitnessedBar-65 — builder return 1 (run `wf_f61f66fe-f0a`), committed f2fcd51c6c51f1ed83568b7c19fb6a8ddbb26e06

## Why

I built TOOL-dWitnessedBar-65 from spec rev-5. Every claim I probed against current code matched the tree, so there was no divergence to report. One pass commit holds the 9 built items and the 4 arms that §7 declares. The spec header is set to CLOSED in the same commit, and the only other spec change is the records table the index generator rewrites.

## Summary

Built and committed as f2fcd51c6 on base f9688a4a8. The commit carries `Pass: TOOL-dWitnessedBar-65` and the spec header now reads CLOSED · 2026-11-21.

**What was built**
- **S2:** `resolve_generated_indexes` in tools/unattended/lib-unattended.sh now refuses an `exists:` path that the kit's own `normpath` reads as `.`. It prints the same skip line as the other refused forms.
- **S1, AC2:** `check_when_forms_agree` in tools/govkit/selftest.py adds 7 refused forms, giving 17, and 3 admitted controls that name no file (`a/b`, `a..b/c`, `.x/y`). It prints one line per form with each reader's outcome, and checks that selfcheck's line for the `a/../b` row names the entry, the row and the path, and holds no `deploy.toml`.
- **S8–S10:** changed in all three copies of the `legacy_ledger_py` block, which still read byte-identical.
  - With no repository root, `--population` prints its `unarmed … no HEAD:` line and `--all` prints `seed: no HEAD:` on stderr. Both exit 1 before reading any registration; `--home` still exits 2.
  - `_run_git` now catches a timeout as well as a spawn failure, and reports either as `git not runnable: <exception>`.
  - A given `--sha` is lowercased, must name a commit, and is stamped as that commit's full SHA. The all-zero SHA is accepted only on a repository with no commits yet.
- **S11, S21:** the signer-temp sweep in tools/run-gates/verdict_backends.py touches regular files only. A file already gone is silent; any other unlink failure prints one stderr line naming the file. The grace constant's comment now names `TAIL_GRACE_S` as the run-gates kit's own constant.
- **S15:** in .githooks/pre-push, each read in `read_green_file` keeps the last of a repeated key and strips one trailing CR.
- **S17:** the gov suite reads `PM_SCRUB` with awk up to the closing quote, drops anything after it, and fails on any name outside `^[A-Z_][A-Z0-9_]*$`. The last-name read is also awk now.
- **Test arms:** AC12 (the hook's `read_green_file` plus `read_tag_lines`, and the `key-no-tab` plant now writes a CRLF verdict line and two sha lines), AC14 (four post-merge copies), AC11 (evidence suite) and AC6/AC7/AC8 (section 2o). Floors moved 41→47 and 314→316.
- **Records:**
  - shell-role is widened through widen-8, with each row set to the measured count: 1314, 611, 2447 and 1319.
  - The acceptance ledger is memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-65-1-acceptance-ledger.md.
  - Deviation 653 is memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-65-deviation-653.md. AC8's upper-case prefix grows past 8 characters when those 8 are all digits, so the case-folding check can never pass vacuously.
  - The map generator rewrote nothing; the index generator rewrote LIVE.md, backlog/TOOL.md, the build README, this spec's records table and dClosedLoop's as-built file, all committed. That last path was outside the declared set, so I declared it with `--dispatch` before committing, along with shell-role.txt, widen-8 and deviation-653.

**Checks that ran (probes only; no gate, suite or bar ran)**
- Each `exists:` reader was called directly on S1's forms: regen's `check_when` and the selfcheck rule from python, and lib-unattended sourced over a scratch repo. All three agree on every form. This stands in for the `govkit selftest` and `govkit selfcheck` legs.
- A scratch probe of the seed command passed AC6, AC7 and AC8 in full, plus AC5. This stands in for `python resolver`.
- `verdict_backends.py --fixture` for `key-no-tab` exited 1 and for `peer-no-ssh-keygen` exited 0, both all held, with `signer temps left: 1 gov-signers-young`. `clean` exited 0. This stands in for `run-gates gov canary` (AC3, AC12).
- AC9: an `os.unlink` stand-in was given only the two files, never the directory or the link (this host could make one), and stderr named the second file once.
- `read_green_file` and `read_record_keys`, each cut out and sourced over scratch records, passed AC11 and AC12's hook half. This stands in for `pre-push bar self-test` and `run-gates evidence`.
- The new `PM_SCRUB` reader and `check_bar_scrub_parity`, cut from the suite, passed AC13 and AC14. The old `sed` range read 34 words on the comment copy, which is the failure the arm is there to catch.
- AC4, AC15 and AC16 greps were read and hold. All changed shell files pass `bash -n` and the Python files pass `py_compile`.
- The bug-class checklist (`gotchas --for-diff HEAD~1..HEAD`) selected 57 classes. I checked the matching-over-whole-output, new-local-collides, borrowed-machine-state and fixture-finds-nothing classes against the diff: every match is per line, no new variable name collides, and the scratch repos are isolated from the machine's git setup. Nothing needed fixing.

**Owed to the main loop at the close**
- **Arms to see red first:**
  - govkit/selftest.py (AC1, AC2): staged red by taking the `..`-segment clause out of `check_when` in the arm's copy, and by removing lib-unattended's `.` refusal.
  - run-gates.gov.test.sh (AC12–AC14): staged red by restoring the `sed` range.
  - run-gates.evidence.test.sh (AC11): staged red by removing the CR strip in `read_record_keys`.
  - resolve-python.test.sh (AC6–AC8): staged red by restoring the exit-2 refusal outside a work tree, and by dropping the `--sha` existence check.
- **Will stay green when staged:** §7's other break for the AC12 hook half, removing the hook's CR strip, cannot turn red. The only CR in that record is on `verdict`, which `read_green_file` never reads. §3 hands this to TOOL-dWitnessedBar-66, and the ledger says so.
- **Legs:** every leg §7 lists, ending with `memory hygiene`.
- **Ledger work at the close:** AC4, and AC10 with S12 and S13 (unit 62's AC7 line and unit 63's AC18 line, still to be written). Also AC16's line in unit 62's ledger, and S6, S18 and S22.

No command timed out or was skipped.
