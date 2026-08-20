# TOOL-aTetheredScratch-2 — sweep the litter, and stop the leak that is 71% of the crowding

**Status:** INPROGRESS · rev-3 · 2026-08-20 · node a · Tier-2 · base 56b945cb · streams tooling

Rev-1 specced a `TMPDIR` retarget. The spec audit measured it and the justification did not survive:
there is no external scratch root on this machine, the path spelling breaks a gate, the tripwire could
not fire, and unit 1's rev-2 allowlist made the retarget worthless to unit 1 anyway. (A fourth reason,
an unverifiable carrier, was withdrawn at rev-3 after unit 1's probe measured the opposite.) Rev-2
keeps the sweep and replaces the retarget with the root cause it was working around.

## 1. Goal

Remove the litter from the operator's home directory, and repair the cleanup that is generating the
`%TEMP%` crowding rather than relocating its output.

Measured on node `a` this session: `%TEMP%` holds 6865 entries and **4905 of them are `mrecall-*`**,
the residue of `tools/memory-recall/selftest.py`. That is 71% of the crowding from one already
diagnosed defect, `TOOL-aBranchedMandate-6`, OPEN since 2026-08-17 at 3,616 residues and now grown by
a further 1,289. The bar timeout at `memory/guides/SESSION-KICKOFF.md:223-226` is downstream of it.

## 2. Scope (IN)

- `tools/memory-recall/selftest.py` — `cleanup()` made correct on Windows and made VERIFYING: it
  clears the read-only bit that git sets on loose objects, retries, and REPORTS a survivor instead of
  swallowing it. One function, 31 call sites, all routing through it.
- The same file — one final arm asserting zero surviving scratch repos, modelled exactly on
  `tools/memory-recall/test_recall_floor.py:461-467`, which already sweeps a `_SCRATCH` list and FAILs
  if anything remains. That arm is the left-shift; without it the fix is a claim.
- The sweep, by EXACT NAME and never by glob: the sixteen log and rc files, the two verified `.bak`
  files, `~/.gov-push/`, and the `mrecall-*` residue in `%TEMP%`.
- `memory/backlog/TOOL.md` — `TOOL-aBranchedMandate-6` moved to CLOSED in place, with a pointer to
  this unit. The id is another build's and stays its own; only the status moves.
- `memory/gotchas/` — one new class for the environment trap the audit surfaced against this build's
  own rev-1: on Windows `%TEMP%` is a subtree of `$HOME`, so a guard keyed on a home prefix denies
  every legitimate temp write. It cost this build a blocker and it will cost the next one too.
- `memory/DECISIONS.md` — one appended row recording the diagnosis, since a future session reading
  "the gate bar writes to the user root" in a stale note needs the correction to be findable.

## 3. Non-goals (OUT)

- **Retargeting `TMPDIR`.** Refused on measurement — see §4. Rev-1 specced it; rev-2 records why it
  was dropped rather than deleting the reasoning, because the next session will have the same idea.
- **Sweeping the shared `%TEMP%` root itself.** `memory/guides/SESSION-KICKOFF.md:226` says not to,
  in as many words. Only the `mrecall-*` residue and `~/.gov-push/` are removed, both by name.
- **Any change to `tools/memory-recall/query.py`.** Its `_remove_cache_dir` is already correct and is
  the model being followed, not a thing to edit.
- **Re-opening `aBranchedMandate` as a build.** Only its backlog row's status moves.
- **The guard hook.** That is `TOOL-aTetheredScratch-1`, which does not depend on this unit.

## 4. Design

**Why the `TMPDIR` retarget was dropped, with the measurements.** Four findings, each independently
sufficient:

- **There is no external root.** `/tmp` on this node is an MSYS `usertemp` mount onto `%TEMP%`
  (`mount` reports `C:/Users/DAILY-~1/AppData/Local/Temp on /tmp type ntfs (binary,noacl,posix=0,usertemp)`),
  and `%TEMP%` is itself under `$HOME`. Every candidate root is inside the home directory the guard
  protects, so "external" was never available.
- **The spelling breaks a gate.** Measured both ways: ambient → `check-template-size.test.sh` PASSES;
  `TMPDIR="C:/Users/daily-agent/AppData/Local/Temp"` → **4 arms FAIL**, because
  `tools/check-template-size.sh:64` normalises its key through `cd && pwd` while `mktemp` echoes
  `TMPDIR`'s spelling verbatim, so the gate writes `/c/Users/…` and the test looks up `C:/Users/…`.
- **The tripwire could not fire.** Rev-1's abandonment condition rested on
  `tools/unattended/adopt-unattended.test.sh:137`, which compares `pwd` against
  `git rev-parse --show-toplevel`. That divergence is MSYS-form versus drive-letter form and is
  invariant under every `TMPDIR` value, so the condition would have passed no matter what — the
  charter's own "a gate you have only ever seen pass" class, inside the AC written to prevent it.
- **The carrier turned out to WORK, and it changes nothing.** Rev-2 refused the retarget partly
  because an `env` block in `.claude/settings.local.json` is undocumented for Bash-tool scope. Unit
  1's AC0 probe then measured it directly: a `settings.local.json` carrying both a hook and
  `env.SG_PROBE_OUT` fired mid-session with no restart, and the variable was readable from a
  subsequent Bash call. So that objection is withdrawn as a matter of fact. The refusal stands on
  the three above, which are about the destination rather than the delivery — a working carrier for
  a root that does not exist is still nothing to ship.

**The leak, and why one function fixes 31 call sites.** `tools/memory-recall/selftest.py:143-144` is
`shutil.rmtree(root, ignore_errors=True)`. The directories it is asked to remove are git repositories
created at `:86-90`; git writes loose objects read-only, and on Windows `unlink` of a read-only file
raises `PermissionError`, which `ignore_errors=True` swallows — so the directory survives and the
caller believes it was removed. `.git` is the only read-only thing in these fixtures, which is why the
same idiom works fine for the plain-JSONL `recallarm-*` dirs and fails only here. Every one of the 31
call sites routes through `cleanup()`, so the fix goes in the one place they all pass through.

**The repair follows the repo's own documented remedy.** `tools/memory-recall/query.py:483-494` already
carries the argument against `ignore_errors=True` on this platform, in its own docstring, and the shape
it prescribes: do the work, verify, and REPORT a failure rather than retrying or swallowing it.
`cleanup()` therefore clears the read-only bit on the failing entry and retries once, then asserts the
directory is gone and prints a named warning if it is not. Version-compat between `onerror` and `onexc`
is resolved by feature detection, not by pinning a Python.

**The final arm is what makes it a fix rather than a claim.** `test_recall_floor.py:461-467` is the
precedent: collect every scratch path the run created, sweep, then FAIL if any survived. The charter's
rule is that a new gate is not landed until its failing case has been observed, so the arm is staged
red against the unrepaired `cleanup()` before the repair lands.

**The sweep is by exact name.** The home directory also holds `.gitconfig`, `.ssh/`, `.aws/`,
`.claude.json` and a `.claude.json.tmp.5240.356c33de8f26` that any plausible `~/.*.tmp*` glob would
catch. So: eighteen literal names, no pattern, and the inventory written outside the home directory
before anything is removed. The two `.bak` files are not logs — they are pre-edit snapshots of
`memory/builds/aDeclaredBound/RUN.md` and `memory/builds/aPromptedMandate/RUN.md` carrying
`phase: LANDING` where the committed versions carry `phase: LANDED` — so each is diffed against its
committed counterpart and confirmed recoverable from `d1bc3f3` before removal, and that confirmation
goes in the build record.

## 5. Production-readiness checklist

- **Security** — none. A test-fixture cleanup and a file removal in the operator's own home.
- **Data loss** — the real risk, and the reason for exact names, a pre-written inventory, and the git
  verification of the two `.bak` files. Removal is announced before it happens because it is
  irreversible.
- **Perf** — `cleanup()` gains a retry on the failure path only; the success path is unchanged. The
  final arm is one `exists()` check per recorded path.
- **Blast radius** — one function in one selftest, plus deletions outside the repo. No gate leg's
  logic changes; `memory-recall kit selftest` gains an arm.
- **Rollback** — revert the commit. The swept files are gone either way, which is the point.
- **Observability** — a surviving scratch dir is now named on stdout and fails the suite, where before
  it was silent. That inversion is the whole unit.
- **Migration / i18n / a11y** — N/A.
- **Testing** — the final arm, staged red first. Plus the existing suite, which must stay green.

## 6. Acceptance criteria

- **AC1** — The failing case is OBSERVED before the repair: against the unrepaired `cleanup()`, the
  new final arm FAILS and names at least one surviving `mrecall-*` directory. A gate whose red has
  never been seen is an assertion about nothing.
- **AC2** — After the repair, `python tools/memory-recall/selftest.py` exits 0 and the final arm
  reports zero survivors.
- **AC3** — Measured, not assumed: the `mrecall-*` count in `%TEMP%` is recorded before and after a
  full selftest run, and the after-count does not exceed the before-count. Today a single run adds to
  it.
- **AC4** — The sweep is verified by exact name: after it, `ls -a ~` contains none of the eighteen
  recorded names and no `.gov-push`, AND the remaining entry set of `~` equals a recorded allowlist,
  so an unexpected removal reds rather than passing unnoticed.
- **AC5** — Each `.bak` file is diffed against its committed counterpart and shown recoverable from
  `d1bc3f3` before removal, with the diff summary in the build record.
- **AC6** — The `mrecall-*` residue is swept and the count recorded: `%TEMP%` entry count before and
  after, both in the build record.
- **AC7** — `TOOL-aBranchedMandate-6` reads CLOSED in `memory/backlog/TOOL.md` with a pointer to this
  unit, and `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 over the edited backlog.
- **AC8** — The full bar is GREEN: `GATE_FULL=1 bash tools/run-gates/run-gates.sh`, with
  `memory-recall kit selftest` among the legs that ran.

## 7. Gates

`GATE_FULL=1 bash tools/run-gates/run-gates.sh`. The legs this unit can red:
`memory-recall kit selftest`, `recall floor`, `recall floor arms`, `memory-hygiene self-test`,
`gotchas selftest`, `build-index selftest`.

`tools/memory-recall/` is not a watched pathspec of the kickoff manifest, so no `last-audit` re-stamp
follows from this unit; unit 1 carries that because it edits `tools/gate-legs.json`.

## 8. Open questions

- **RESOLVED — retarget versus repair.** Rev-1 chose to relocate the accumulation. Refused on the four
  measurements in §4, and because 4905 of 6865 entries are one defect rather than churn — relocating
  it would have left the leak generating rubble in a new place. Ratified: repair `cleanup()`.
  Resolver: the owner, on the audit's measurements, 2026-08-20.
- **RESOLVED — the two `.bak` files.** Considered leaving them, and considered preserving them in-repo.
  Ratified: verify each against `d1bc3f3`, record the diff, then remove — they are recoverable, so
  keeping a second copy in the repo would be storing what git already stores. Resolver: the owner.
- **OPEN — whether the final arm should FAIL the suite or only warn on a machine where the read-only
  bit cannot be cleared.** Failing is correct here and matches `test_recall_floor.py:465-467`. A
  hypothetical host where the retry legitimately cannot succeed would then red the bar for an
  environmental reason. Proceeding with FAIL, because a warning is how this defect stayed open for
  three days, and recording the question so a real occurrence is re-priced rather than argued from
  first principles.

## 9. Revision log

- **rev-1** — 2026-08-20 — authored as a `TMPDIR` retarget plus sweep, on the blast-radius recon.
- **rev-2** — 2026-08-20 — the M4 spec audit folded in, and the unit re-scoped by the owner. The
  retarget is dropped and its refusal recorded with four measurements: `/tmp` is `%TEMP%` and is inside
  `$HOME` so no external root exists; the Windows spelling breaks four arms of
  `check-template-size.test.sh`; rev-1's abandonment tripwire was `TMPDIR`-invariant and could not
  fire; and the carrier was unverifiable in-session. In its place, the root cause — 4905 of 6865
  `%TEMP%` entries are `TOOL-aBranchedMandate-6`. Sweep corrected to exact names after the audit found
  two of the eighteen files are run-state snapshots rather than logs, and AC4 strengthened from
  eighteen named absences to a whole-directory set comparison.

- **rev-3** — 2026-08-20 — one §4 measurement corrected rather than left standing. Rev-2 listed the
  unverifiable carrier among the reasons the `TMPDIR` retarget was refused; unit 1's AC0 probe
  measured the opposite, so the claim is withdrawn in place. The refusal is unchanged and rests on
  the three destination findings. A spec that keeps a disproved reason is the two-answers-to-one-
  question class, in the document that records the decision.

## 10. Reuse audit

The seam is `tools/memory-recall/query.py:483-494`, and it is followed rather than extended. That
docstring already carries the measured argument against `shutil.rmtree(ignore_errors=True)` on win32
and the shape that replaces it — do the work, verify, report rather than swallow. The repair applies
that reasoning to `selftest.py:143-144`; the two functions stay separate because they solve different
failure modes on the same platform (an open sqlite handle versus a read-only git object) and merging
them would couple a cache evictor to a test fixture.

The final arm reuses `tools/memory-recall/test_recall_floor.py:461-467` verbatim in shape: accumulate
the scratch paths, sweep, assert nothing survived, fail if something did. That file is in the same kit
and was fixed for the same class of defect, which is the strongest evidence available that the pattern
holds here.

Recall terms used, recorded so a resuming pass re-runs the same query:
`scratchpad TMPDIR mktemp hermetic scratch repo gate-logs HOME litter temp residue selftest cleanup redirect`.
The probe surfaced `TOOL-aBranchedMandate-6` as its top hit, which rev-1 read as adjacent context and
rev-2 makes the subject.
