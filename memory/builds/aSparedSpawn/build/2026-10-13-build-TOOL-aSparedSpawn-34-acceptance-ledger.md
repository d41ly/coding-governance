# Acceptance ledger — TOOL-aSparedSpawn-34

**Serves:** journal TOOL-aSparedSpawn-34

Node `a`, 2026-10-13, the second attempt at the reconcile. The first, a workflow subagent, was
refused by the write gate at its first conflict edit and aborted its merge; this pass reused its
dispatch and brief rows. Local `main` read `6081d92e4a4552078474f29505dad4b1f24c6592` when the pass
started, the sha the spec names, so the merge took it; the merge-base is origin/main `6e8f8b1da`.
The same 15 files conflicted as in the driver's trial, with no difference. No suite, bar or slice ran.

Commits: the merge `f5a63b77e` (`Pass: none`), and the pass commit after it, which carries the two
re-measured fork rows, this ledger and the spec's CLOSED header.

How the hand-merged hunks compose:

- `tools/run-gates/run-gates.sh` — `KNOWN_KNOBS` carries both `spawnpause` and `slots`; the profile
  parse reads both; the profile line is local main's one template, `render_prof_line`, rebuilt after
  the turnstile, carrying this build's calibrated-width note and spawn-pause field. The spawn field
  is renamed `prof_sp`, because both sides named their field `prof_s`. `ts_try_reap` and the claim
  take local main's slot-by-slot design. This build removed `ts_now` (`TOOL-aSparedSpawn-16` S15),
  so every `$(ts_now)` call in local main's lines reads `$EPOCHSECONDS`: nine sites, seven of them
  in hunks git auto-merged, which as merged named an undefined function. The run header keeps local
  main's slot keys and writes `reuse` once, where `TOOL-aSparedSpawn-32` composed it: local main's
  copy of that line is the one the `TOOL-aSparedSpawn-32` ledger's AC9 saw written twice.
- `tools/unattended/unattended.sh` — `init_bounded` keeps local main's `RB_HANDLE` reset and this
  build's `$EPOCHSECONDS` start. `read_bounded` keeps local main's `up.end` stamp, with
  `$EPOCHSECONDS` as its fallback where local main had `$(date +%s)`. The dispatch-phase reader
  keeps local main's `DPC_` cache and, on a miss, reads `fact` through `_fact` as this build does.
- Floors, each the shared base plus both sides' moves: drift-audit `CHECK_FLOOR` 478 + 4 + 4 = 486;
  the run-gates suite 326 + 62 + 13 = 401; the run-log suite 211 + 9 + 6 = 226; the hygiene suite
  557 + 61 + 16 = 634; manifest-check 279 + 1 + 30 = 310; the unattended suite 2808 - 66 + 34 = 2776,
  with shard 5 at 270 - 7 + 34 = 297 and the other shards at this build's values, since local main
  moved none of them. Every comment line of both sides is kept.
- `.githooks/pre-push.test.sh` — `GATE_TURNSTILE_SLOTS` joins `BAR_INERT_KNOBS` beside this build's
  knobs, with local main's class comment. Arm 23b, which this build added, called `decide_on`, which
  local main renamed to `run_push_selftests`: the merge left it calling an undefined function, and it
  now calls the new name.
- `tools/run-gates/run-gates.test.sh` — `PINNED_KNOBS` is the union, with this build's runner-set arm.
- `tools/run-gates/gate-profiles.txt` keeps this build's `spawnpause` item and calibrated-width
  paragraph, with local main's `slots=<n>` item between them.
- `tools/memory-tree/check-memory-hygiene.sh` keeps local main's `NAMES_GRADED` block above this
  build's `if check_selected 1; then`.

**Evidences:** TOOL-aSparedSpawn-34
- AC1 — the two-parent diff over the staged merge: every line `git diff -U0 6e8f8b1da main -- F` adds, searched for in the result, per conflicted product or suite file — absent, and each a composite named above: 11 in the runner (the knob list, the profile initialiser, the template line, and the eight lines local main added that call `ts_now`), 3 in the driver, 2 in the unattended suite, 2 in the run-gates suite, 1 each in the run-log suite, the hygiene suite, the drift-audit selftest, the manifest-check suite and the pre-push suite (each a floor or a union list), and 0 in `gate-profiles.txt` and `check-memory-hygiene.sh`.
- AC2 — the same diff from `249b4ab6`'s side (`git diff -U0 6e8f8b1da HEAD -- F` before the merge commit) — absent, each the same composite seen from this side: 9 in the runner (the knob list, the initialiser, the `spawnpause` case arm split from its `esac`, the renamed `prof_sp` line, the template line and its two comment lines moved above `render_prof_line`, one comment line extended, and the reap's clock line indented into the slot loop), 3 in the driver, 3 in the run-gates suite (the floor, the pin and its comment), 2 in the unattended suite, 2 in the pre-push suite (the knob list and `decide_on`), and 1 floor each in the run-log, hygiene, drift-audit and manifest-check suites. No line of the reuse composition or the digest view is absent: `reused_cache`, `GATE_REUSE_DIGEST_ENV` and `REUSE_SCHEMA` are present in the runner, `GATE_REUSE_DIGEST_ENV` in the hook, and the header's `reuse` key is written once.
- AC3 — `python tools/codebase-map/gen_map.py --check` exit 0 on the merge commit; `python tools/memory-tree/gen_build_index.py --write` re-run on the merge commit left no diff.
- AC4 — `grep -n 'last-audit\|last-body-change' memory/guides/SESSION-KICKOFF.md` — the merge took local main's stamps, `last-audit … @ cfce31b6f` and `last-body-change 5e4b391e`; the body kept this build's `--calibrate-width` bar line, which git auto-merged. The re-stamp at the merge's sha is the records commit after the pass, so AC4's observation follows it.
- AC5 — `python tools/govkit/govkit.py selfcheck` was REFUSED by `scratch-guard` (a role agent runs no gate) and is owed at VERIFYING. In its place, a probe of every tracked `gov:kit <id>@<ver>` marker and every `KIT_*_VERSION` constant: both are identical in the merge index and at local main, which minted every kit past this build's base, while this build minted none. Local main's multi-version rows (memory-tree, process-monitor, vk) are its own fixtures, unchanged.
- AC6 — `bash -n` exit 0 on every shell file both sides changed, the conflicted eight included, and `py_compile` clean on the three python files; `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only run-gates-1leg` RED at the merge, measured 55 against 53 (four readings), and `--only run-gates-2leg` RED, 57 against 55. The `--sites` listing attributes the +2 to one line not in the build's parent, local main's `printf | cat >>` run-log append (`TOOL-aPairedSlots-7`, two concurrent writers); the rows are raised to 55 and 57 with both readings, and both exit 0 on the pass tree. `python tools/memory-tree/check-arms.py --check`, the `sh_hygiene.py --spawn-idioms` argv and `python tools/check-spec-tokens.py` were REFUSED by `scratch-guard` and are owed at VERIFYING. `check-memory-hygiene.sh --staged` ran in the merge commit's pre-commit hook, over the whole tree because the merge stages the conf, and passed.
- AC7 — `git merge-tree --write-tree main HEAD` exit 0 and no conflicted file, at the merge commit and again after the pass commit, with local main still at `6081d92e4`.

## Owed at VERIFYING

- `govkit.py selfcheck`, `check-arms.py --check` and `check-spec-tokens.py`, each refused to this role.
- `sh_hygiene.py --spawn-idioms`: refused too, and expected RED. Local main's new code adds sites the registry does not yet count. In the runner these are the slot loop's and the docs-beacon sweep's `$(cat …)` reads and the sweep's `$(date -r …)`. The other files local main moved add more. The rows in `memory/project/spawn-idiom-sites.txt` are re-measured from the leg's own output, as `TOOL-aSparedSpawn-32` did.
- Every suite whose floor moved here, at the summed floors above: the drift-audit selftest, the run-gates, run-log, hygiene, manifest-check, unattended and pre-push suites. The run-gates canary and its profile-line arms, in particular, now meet a line that carries both `spawnpause` and, above one slot, `slots`.
