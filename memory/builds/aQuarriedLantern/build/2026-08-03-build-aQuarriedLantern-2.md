# TOOL-aQuarriedLantern — closing-review fixes, group G1 (the adoption surface)

**Serves:** journal TOOL-aQuarriedLantern-1  <!-- inferred: this build defines exactly one spec id, so the record can serve nothing else -->

Items F1 (blocker), F2, F5, F6, F8 from
`memory/tooling/builds/2026-08-03-TOOL-aQuarriedLantern/reviews/2026-08-03-review-aQuarriedLantern-2.md`.
Every number below came from a command run in-session.

**Applied** 2026-08-03 · node `a` · base `20f2337`

## One defect family, not five

The kit worked here and broke in an adopter, and its own tests were green because the fixtures
papered over the gap. Two roots: a fixture spelled like the adopter's MANDATED kit dir (F1), and no
runbook step that ever delivered `tools/settings-merge.py` into an adopting project (F2 → F5, F8,
and half of F6).

## F1 — the blocker

`selftest.py` built its fixture with `make_repo(kitname="memory-recall")` and then asserted
`here != kitdir.name`. `WIRE-INTO-PROJECT.md` §3c step 1 fixes the adopter's kit dir at exactly
`memory-recall/`, so the assertion tripped there — on a leg §3c step 3 makes a standing gate.

- Fixture renamed to `mrecall-fixture-kit`, a name no adoption layout can mandate. The
  `here != kitdir.name` assertion stays (it tests something real) and now holds against both
  spellings; a second assertion pins the fixture against the ADOPTER's name too.
- New arm `t_adopter_layout` runs the WHOLE selftest from a fixture repo whose kit sits at
  `<root>/memory-recall/`, so the shipped layout is on the merge bar. Nested exactly one level: the
  child sees `MRECALL_NESTED` and skips that arm, so the recursion terminates.

**Reproduced the review's way** — clone at a short path (MAX_PATH kills a deep one), copy the
working tree's fixes in, `git mv tools/memory-recall memory-recall`, run the leg:

| Kit `selftest.py` | Result in the adopter layout |
|---|---|
| pre-fix (`HEAD~2` blob) | **17/18, exit 1** — `fixture kit dir must not spell like this repo's (memory-recall)` |
| post-fix | **19/19, exit 0** |

## F2 · F5 · F8 — the undelivered tool

- `WIRE-INTO-PROJECT.md` §3c step 4 now copies `tools/settings-merge.py` into the project before the
  merge command, and the merge command is the project-relative path that then exists. Step 5's
  commit list and the Result section's memory-recall bullet name it too.
- `adopt-memory-recall.sh` resolves the tool (`tools/` then repo root) instead of hardcoding
  `tools/settings-merge.py`; when it genuinely is not installed it prints the `cp` step first rather
  than a command that dies with errno 2.
- `check-wiring.sh`'s recall arm no longer needs python at all: the wired signal is
  `grep -qF "<marker>" .claude/settings.json`, and the marker comes from the fragment —
  `settings-merge.py`'s own docstring already defines that substring as the deployer's is-it-wired
  test, so this states the predicate once instead of twice. That deletes the
  `skip … settings-merge.py absent, cannot verify` branch, which was **exit 0 on the state the
  runbook calls the one bad state**.

Measured end to end in the adopter-layout clone, running the printed remedy verbatim:

| Step | Before | After |
|---|---|---|
| `adopt … --with-hook` remedy, run verbatim | `[Errno 2]`, exit 2 | `wired recall-opened Read hook`, exit 0 |
| hook copied, merge skipped | `skip … cannot verify`, EXIT 0 | `UNWIRED recall`, EXIT 1 |

## F6 — the fifth state

- `settings-merge.py` refuses the merge when the fragment's `hook_path` does not exist (`--check` is
  exempt: it writes nothing and the hook file is not what it reports on). Verified in the clone:
  exit 2, `refusing to wire recall-opened — .claude/hooks/recall-opened.js does not exist`.
- The js-absent branch of `check-wiring.sh` consults settings.json before returning, so
  settings-dispatches-a-missing-script prints UNWIRED naming the missing path instead of
  `skip … opt-in not taken`. Both halves — marker and script path — are read from the fragment, so
  the arm asserts nothing the shipped kit does not itself declare.

The agent-cap arm keeps its plain skip in that direction, deliberately: its hook path is declared
nowhere this script can read (`settings-merge.py` hardcodes it), so "settings wired, script missing"
cannot be told from a deliberate out-of-tree copy. Its wired signal did move to the same `wired()`
grep, which removes the same false all-clear.

## Gates + mutation scoring

`bash tools/check-wiring.test.sh` **18/18** (was 16 — two new AC8 states: no `settings-merge.py`
present, and settings-wired-script-gone) · `python tools/settings-merge.py --selftest` PASS (case 11
added) · `python tools/memory-recall/selftest.py` **19/19 in 54.4 s** (was 18/18 in 24.9 s; the
nested adopter-layout run is the difference, and reports `18/19, 1 skipped` from inside).

`t_printed_invocations_resolve` now folds the adopt script's `--with-hook` stdout: **3 distinct
printed paths, all resolve** (was 1). `INVOKE_RE` had to learn `python3?` — every launcher this kit
prints is resolved python3-first, so the old bare-`python ` pattern matched none of them and the
fold would have been vacuous. A non-vacuity assertion now pins that the remedy reaches `seen`.

Six mutations, each asserted APPLIED on disk (bytes compared) and reverted afterwards:

| # | Mutation | Result |
|---|---|---|
| M1 | fixture kit dir back to `memory-recall` | KILLED — 17/19, both the direct guard and the nested run |
| M2 | `--with-hook` remedy prints a path no adopter has | KILLED — 16/19, `naming files that do not exist` |
| M2b | `INVOKE_RE` back to bare `python ` | KILLED — 17/19, `the --with-hook remedy printed no invocation` |
| M3 | restore the `cannot verify` skip | KILLED — 17/18, exactly the new no-`settings-merge.py` case |
| M4 | js-absent branch stops reading settings.json | KILLED — 17/18, exactly the new script-gone case |
| M5 | drop the missing-hook_path refusal | KILLED — `AssertionError` in `_selftest` case 11 |

M4's first attempt scored a **fake kill**: the mutation harness invoked a bare `bash`, which resolved
to the WSL shim (`ERROR: CreateProcessCommon … chdir failed`, exit 127, no gate output at all). Re-run
against `C:/Program Files/Git/usr/bin/bash.exe` after asserting a green baseline with that same
interpreter — the redo is the row above. M3's first attempt was an insertion-shaped mutation that
tripped the harness's own applied-check, not the gate; both were re-scored, neither counted.

## Not touched (other groups' items, observed in passing)

`$REL` came out ABSOLUTE in the adopter-layout clone (`--fragment /c/Users/DAILY-~1/…`) — F12's
mount-alias mechanism, reproduced incidentally from a `/c/Users/DAILY-~1/…` cwd. Harmless to every
assertion here; it belongs to whoever owns F12.
