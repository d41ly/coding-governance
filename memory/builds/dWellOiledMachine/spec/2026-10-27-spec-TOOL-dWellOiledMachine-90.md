# TOOL-dWellOiledMachine-90 — the promotions audit's 55 medium and low findings, batched: claims, fixtures, readers, registries and the sibling records that drifted

**Status:** DEFERRED · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 65 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-90-deviation-901.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-90-deviation-901.md) | deviation | — |
| [2026-10-27-build-TOOL-dWellOiledMachine-90-deviation-902.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-90-deviation-902.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`)
exited CONVERGED with 55 confirmed findings below HIGH. BUILD-METHOD M4 promotes every one of them,
batched into ONE unit, and this is that unit. It closes, by report id:

- MEDIUM (46): 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 19, 20, 21, 22, 23, 24, 25, 26, 27, 31, 32, 33, 35,
  38, 42, 43, 44, 45, 46, 52, 53, 54, 55, 56, 57, 58, 59, 60, 62, 64, 65, 66, 67, 68, 69.
- LOW (9): 12, 14, 17, 29, 36, 37, 47, 48, 49.

Several findings share a report item (M7: 8, 55; M9: 10, 15, 52; M10: 11, 25, 26, 44, 67; M13: 21, 32,
43; M15: 23, 64; M17: 27, 57; M19: 33, 53; M22: 42, 58; L2: 14, 17, 49), and each keeps its own scope
item here. Each finding takes the fix its skeptic judged SOUND, or the skeptic's corrected fix where
the report marks the finder's UNSOUND (findings 36, 53, 57). The findings land on many units, so this
unit repairs none in particular and sits after every unit of the build. One unit, not two: the fixes
meet in `tools/runtime/supervise.py` (findings 23, 24, 54, 64), `tools/memory-tree/door_fixture.py`
(6, 24, 36, 66), `tools/memory-tree/gov_record.py` (17, 36, 66) and `tools/gate-legs.json` (4, 45, 47),
so no split into two disjoint halves exists under M6.

## 2. Scope (IN)

Each item names its finding, its report item and the unit or spec it lands on. "Spec N takes a rev
bump" means spec N is amended at this unit's pass, its §9 line naming this unit and the finding.

- **S1** — Finding 2 (M1), on TOOL-dWellOiledMachine-68 and -13. `read_spec_writes`
  (`tools/memory-tree/design_lib.py`) adds the suite path of every `New arm:` line of a spec's §7 to
  that spec's write set, so `derive_parallel_step` (`tools/memory-tree/gen_build_index.py:1724`) and
  `--dispatch` see the file an arm writes; the README's build-order region is re-rendered. Observed by
  AC1.
- **S2** — Finding 3 (M2), on TOOL-dWellOiledMachine-74 and -7. Spec 74 takes a rev bump listing
  `tools/runtime/supervise.py` under Files touched, the file its AC3 plant and §7 arm write, so S1's
  join and the estimate agree. Observed by AC2.
- **S3** — Finding 4 (M3), on TOOL-dWellOiledMachine-79 S13. The `runtime selftest` row unit 1 added to
  `tools/run-gates/selftest-budgets.txt` is re-pointed, never duplicated, and the leg's command in
  `tools/gate-legs.json` runs `selftest.py --modules`. Observed by AC3.
- **S4** — Finding 5 (M4), on TOOL-dWellOiledMachine-79 S7. `commit_keys.py`'s salt cases run under a
  scratch policy whose `runtime.secret-home` is `env-injected`, the home `read_secret_ref` reads
  (TOOL-dWellOiledMachine-17 S4); an unset variable is a refusal case; no case writes the real
  keychain. Spec 79 takes a rev bump restating S7 as resolved from that one home. Observed by AC4.
- **S5** — Finding 6 (M5), on TOOL-dWellOiledMachine-79 S47. `door_fixture.py` gains
  `bindings-foreign-tag`, a `refs/gov/bindings/` write naming another fleet tag, refused, and
  `bindings-own-supervisor`, the sessionless supervisor's own binding write, admitted. The attendance
  half is TOOL-dWellOiledMachine-84's. Observed by AC5.
- **S6** — Finding 7 (M6), on TOOL-dWellOiledMachine-79 S1 and -67 AC3.
  `tools/runtime/fixtures/conformance/claude-code-2.1.292/` gains a prompt-submit log marked
  `synthetic`, as TOOL-dWellOiledMachine-36 S3 does for codex, and specs 79 and 67 take rev bumps
  spelling the replay argument as 36's directory path. Observed by AC6.
- **S7** — Finding 8 (M7, with 55), on TOOL-dWellOiledMachine-65 AC4. Spec 65 takes a rev bump whose AC4
  is the class grep of S41 here, never the one line unit 34 S7 removes before 65 builds. Observed by
  AC7.
- **S8** — Finding 9 (M8), on specs 14, 16, 38, 8, 12 and 9. Each correction a round-1 promotion
  promised its sibling is checked by text only that correction adds, and written where missing: spec
  14's `eight` `to` rows (unit 68), spec 16's §4 naming `check_commitment` (unit 72), and specs 38, 8
  and 12 each carrying a §9 entry with the literal `correction for finding <n>` for findings 50
  (unit 73), 59 (unit 74) and 63 (unit 77), the words their existing edge lines never spell; spec 9 no
  longer claims its lock `survives` (unit 70). Observed by AC8.
- **S9** — Finding 10 (M9, with 15, 52), on TOOL-dWellOiledMachine-64 S4. The load probe becomes static:
  for each moved module under `tools/runtime/`, every `require(path.join(__dirname, '<f>'))` literal
  in its source, lazy ones included, is resolved with `require.resolve` from `tools/runtime/`, and a
  miss fails naming the module and the sibling. Observed by AC9.
- **S10** — Finding 11 (M10), on TOOL-dWellOiledMachine-79 AC37. The registry check's population is
  derived from TOOL-dWellOiledMachine-28 S1's moved-file list: every moved file's old path has zero
  rows in `memory/project/spawn-idiom-sites.txt` and `memory/project/substitution-fed-loops.txt`.
  Observed by AC10.
- **S11** — Finding 12 (L1), on TOOL-dWellOiledMachine-65 S1. Spec 65 takes a rev bump stating the
  reset's format once, as extended with seconds and a trailing `Z` (as `2026-10-27T09:00:00Z`), the form TOOL-dWellOiledMachine-81 renders,
  and dropping "basic". Observed by AC11.
- **S12** — Finding 14 (L2, with 17, 49), on TOOL-dWellOiledMachine-63 AC6. Spec 63 takes a rev bump
  whose AC6 greps `help/runtime.md`, never a bare `runtime.md`. Observed by AC12.
- **S13** — Finding 15 (M9), on TOOL-dWellOiledMachine-64 §4. Spec 64 takes a rev bump correcting its
  Evidence to read: `gate-guard.js` requires `run-lease.js` and `stop-guard.js` lazily inside
  `checkAsk` (`tools/unattended/gate-guard.js:710`, `:721`), never at load. Observed by AC13.
- **S14** — Finding 17 (L2), on TOOL-dWellOiledMachine-63 S5. `check_writer_binding`'s docstring in
  `tools/memory-tree/gov_record.py` states the node writer's reach, the first of 63 S5's three places.
  Observed by AC14.
- **S15** — Finding 19 (M11), on TOOL-dWellOiledMachine-70 §3 and §10. Spec 70 takes a rev bump: the
  turnstile's holder reaps use a nonce-guarded `rm -rf` (`tools/run-gates/run-gates.sh:1757`,
  `:1766`), not a rename, and its race is a named open item linking TOOL-aReapedTicket-4. Observed by
  AC15.
- **S16** — Finding 20 (M12), on TOOL-dWellOiledMachine-72. `tools/runlog/selftest.py` gains the case
  `idle-and-unparseable`: one producer emptied and one starting with an unparseable line in ONE
  journal, verifying `pruned` under the rules of TOOL-dWellOiledMachine-86 and -88 together.
  Observed by AC16.
- **S17** — Finding 21 (M13), on TOOL-dWellOiledMachine-74 S2. The input print joins the label as a
  segment before the stage: `renderAgentLabel(scope, stage, inputPrint)` renders
  `<slug> · <scope> · #<print> · <stage>` in `tools/workflows/tier2-review.template.js`,
  `tools/workflows/unattended-build.template.js` and `tools/workflows/unattended-unit.js`, and 74 S2's
  `renderKeptLabel` is deleted, so the stage stays the last segment. Observed by AC17.
  **Readers:** by name: READER NOT IN TREE — `renderKeptLabel` is TOOL-dWellOiledMachine-74's, unbuilt at
  HEAD, its call sites re-pointed to `renderAgentLabel`. by value: `tools/workflows/tier2-review.test.sh`
  and `tools/workflows/unattended-build.test.sh`, which pop the last segment as the stage, unchanged.
- **S18** — Finding 22 (M14), on TOOL-dWellOiledMachine-75 AC1, AC2. The fail-closed plant makes
  `requests` a regular file in place of the directory, a write failure on Windows, where a read-only
  directory still accepts files. Observed by AC18.
- **S19** — Finding 23 (M15, with 64), on TOOL-dWellOiledMachine-78 S3. The tick records the Windows pid
  under MSYS (`cat /proc/$$/winpid`), `$$` elsewhere, with its image and its start stamp, and judges
  it with `check_pid_alive <pid> <image> <stamp>`, as `derive_winpid` in
  `tools/unattended/resume-tick.test.sh:240` reasons. Observed by AC19.
- **S20** — Finding 24 (M16), on TOOL-dWellOiledMachine-78 and -63 S6. Every Python fixture that spawns
  a bash script, `supervise.py --fixture` and `door_fixture.py`, resolves the interpreter with
  `resolve_bash()` (`tools/lib/resolve_bash.py:15`), never a bare `bash`. Observed by AC20.
- **S21** — Finding 25 (M10), on TOOL-dWellOiledMachine-79 S35. `resume-tick.test.sh` reads the health
  events through `journal.py read --producer health`, never `$FX_GITDIR/health.log`. Observed by AC21.
- **S22** — Finding 26 (M10), on TOOL-dWellOiledMachine-79 S37. The four `stall-recorder.test.sh` rows
  and three `stop-guard.test.sh` rows of `spawn-idiom-sites.txt`, the `gate-guard.test.sh` row of
  `substitution-fed-loops.txt:62` and `resume-tick.sh`'s rows are re-keyed to `tools/runtime/`.
  Observed by AC10.
- **S23** — Finding 27 (M17), on TOOL-dWellOiledMachine-68. Every by-value reader of
  `.claude/skills/runlog/` or `.claude/skills/unattended/` under `tools/`, outside the kit descriptors
  and suites (`tools/unattended/check-unattended.sh:5710`, `caps.toml:83`, `:87`,
  `tools/policy/check_policy.py:3490`, `tools/template-size-limits.txt:154`, `tools/gate-legs.json:144`),
  is either resolved through the `{skill_home}` value or listed in `help/runtime.md` as a
  claude-code-only reader. Observed by AC23.
- **S24** — Finding 29 (L3), on TOOL-dWellOiledMachine-79 S22. `derive_abs_dir` compares under MSYS
  with both sides lower-cased, so a case-variant `core.hooksPath` matches the trusted copy. Observed
  by AC24.
- **S25** — Finding 31 (M18), on TOOL-dWellOiledMachine-79 S3. `harness.py --read` is deleted;
  check-wiring's session arm runs `harness.py capability claude-code on-failure --version <v>`
  (TOOL-dWellOiledMachine-14 S3), takes its first ` · ` field and reads exit 1 as `no`. Observed by AC25.
  **Readers:** by name: `tools/check-wiring.sh`, the one caller, re-pointed here. by value: NO VALUE READERS — the verb's output is read only by that caller.
- **S26** — Finding 32 (M13), on TOOL-dWellOiledMachine-74 S3. `readKeptReturn` keys on the whole label
  of S17, and spec 74 takes a rev bump whose §5 drops "readers matching by prefix keep matching".
  Observed by AC17.
  **Readers:** by name: READER NOT IN TREE — `readKeptReturn` is TOOL-dWellOiledMachine-8's, unbuilt at HEAD. by value: NO VALUE READERS — the label is read only by that function.
- **S27** — Finding 33 (M19), on TOOL-dWellOiledMachine-65 §3 and §10. Spec 65 takes a rev bump whose
  third non-goal and §10 name the measured transcript record TOOL-dWellOiledMachine-81 reads.
  Observed by AC11.
- **S28** — Finding 35 (M20), on TOOL-dWellOiledMachine-79 S28. `tools/runtime/tickets.py` holds all
  four ticket functions 45 S2 names, `remove_stale_tickets` included, and `commit_queue.py` calls the
  sweep before it reads its queue. Observed by AC28.
- **S29** — Finding 36 (L4), on TOOL-dWellOiledMachine-63 S2, the skeptic's corrected fix. One Python
  `read_host_name()` in `gov_record.py` spells the bash rule (`tools/unattended/lib-unattended.sh:528`),
  and `door_fixture.py --case host-parity` pins the two to one output. Observed by AC29.
- **S30** — Finding 37 (L5), on TOOL-dWellOiledMachine-79 §7. Spec 79 takes a rev bump naming
  `push-main self-test` and `settings-merge selftest` on its leg line, with a `New arm:` line for each.
  Observed by AC30.
- **S31** — Finding 38 (M21), on TOOL-dWellOiledMachine-77 S1. The binding value `machine` gets an
  explicit arm in each reader of `owner`: card replay (TOOL-dWellOiledMachine-12 S3), the map extra
  (-23 S3), the `Gov-*` trailer filler (-33 S4) and the session node (-35 S2) treat it as `yes`; the
  orientation exemption (-38 S4) does not exempt it. Observed by AC31.
- **S32** — Finding 42 (M22, with 58), on TOOL-dWellOiledMachine-70 S1, S3. A graveyard entry carries
  a file `reaper` holding the reaper's pid, image and start stamp, so the sweep calls
  `check_pid_alive`; every ledger reader counts only `slot.<k>` and skips `graveyard/`. Observed by
  AC32.
- **S33** — Finding 43 (M13), on TOOL-dWellOiledMachine-74 §4. `tools/workflows/tier2-review.test.sh`,
  `tools/workflows/unattended-build.test.sh` and `tools/workflows/README.md` are updated for S17's
  label, and spec 74 takes a rev bump listing them under Files touched. Observed by AC17.
- **S34** — Finding 44 (M10), on TOOL-dWellOiledMachine-79 S35. `tools/process-monitor/selftest.py`
  reads the health events through `journal.py read --producer health`, never
  `os.path.join(tmp, "health.log")` or `resolve_health_log`. Observed by AC21.
- **S35** — Finding 45 (M23), on TOOL-dWellOiledMachine-73 §7. The `manifest-check self-test` guard in
  `tools/gate-legs.json` gains `tools/runtime/session_binding.py`. Observed by AC35.
- **S36** — Finding 46 (M24), on TOOL-dWellOiledMachine-64 §4. Spec 64 takes a rev bump whose Files
  touched names the moved renderer's old path unbackticked, so no bare `tools/unattended/` token
  widens its write set. Observed by AC36.
- **S37** — Finding 47 (L6), on TOOL-dWellOiledMachine-79 S13. `selftest.py --modules` is measured once
  and that figure plus a stated margin is written into its budget row and the leg's `ceiling`, the
  row's reason naming the measurement and its date. Observed by AC37.
- **S38** — Finding 48 (L7), on TOOL-dWellOiledMachine-79 S36. The `stop-guard.js` EXEMPT row of check
  36 (`tools/unattended/check-unattended.sh:4863`) is removed with the `resume-tick.sh` row, and the
  check's comment says the moved hooks' keys are no longer derived. Observed by AC38.
  **Readers:** by name: `tools/unattended/check-unattended.sh`, the one file spelling the row. by value: NO VALUE READERS — the row feeds only check 36.
- **S39** — Finding 49 (L2), on TOOL-dWellOiledMachine-63 S5. `help/runtime.md` states the node
  writer's reach, the third of 63 S5's places, checked by its own grep. Observed by AC14.
- **S40** — Finding 52 (M9), on TOOL-dWellOiledMachine-64. `stop-guard.js` and `stall-recorder.js` each
  get a refusal case driving the hook end to end with its renderer renamed in a scratch copy, as 64
  AC4 does for gate-guard. Observed by AC9.
- **S41** — Finding 55 (M7), on TOOL-dWellOiledMachine-65 S4. The retired-sidecar grep covers both
  languages:
  `git grep -nE "stall\.[^ ]*\.log|'stall'.*\.log|unattended/stall" -- tools/runtime tools/unattended`,
  and any Python reader it finds in `supervise.py` or `limits_fixture.py` is deleted. Observed by AC7.
  **Readers:** by name: READER NOT IN TREE — the supervisor and the limits fixture are TOOL-dWellOiledMachine-6's and -47's, unbuilt at HEAD. by value: NO VALUE READERS — the sidecar is retired, so nothing reads it.
- **S42** — Finding 53 (M19), on TOOL-dWellOiledMachine-65 §5 and AC1, the skeptic's corrected fix.
  Spec 65 takes a rev bump whose §5 risk line names the reset's measured source
  (TOOL-dWellOiledMachine-81) instead of "today's field", and whose AC1 names that source.
  Observed by AC11.
- **S43** — Finding 54 (M25), on TOOL-dWellOiledMachine-65 S2. The hold reads only recorder lines, those
  carrying `error=`, newer than the act's `act-launch` line, the last `limit-hold` close and the
  owner's last `resume`; a `reset=none` line holds as a reset at TOOL-dWellOiledMachine-47's hold
  ceiling, so its hand-over ends it. Observed by AC43.
- **S44** — Finding 56 (M26), on TOOL-dWellOiledMachine-67 S1. 32 S5's `ACT_START_SECONDS` timeout,
  tree kill, `state: failed` and exit 3 move onto the `returned` branch in `launch_act`, and spec 32
  takes a rev bump keying S5 on `returned`. Observed by AC44.
- **S45** — Finding 57 (M17), on TOOL-dWellOiledMachine-68, the skeptic's corrected fix. Check 31 of
  `tools/unattended/check-unattended.sh` resolves its Skill path from the target's harness adapter
  value (TOOL-dWellOiledMachine-14 S5, S6, through `harness.py`), falling back to `.claude/skills`.
  Observed by AC45.
- **S46** — Finding 58 (M22), on TOOL-dWellOiledMachine-70 S3. The sweep restores, never deletes, a
  graveyard entry whose `res` names a reservation still held (owner pid alive, heartbeat fresh), by
  70 S2's rule. Observed by AC32.
- **S47** — Finding 59 (M27), on TOOL-dWellOiledMachine-70 S1, S2, S5. Each rename names its outcomes:
  `FileNotFoundError` is a lost race; `PermissionError` or another `OSError` skips and retries at the
  next beat; a restore never overwrites, a file restored by `os.link` then `os.unlink`, a slot falling
  through to the next free index. Observed by AC47.
- **S48** — Finding 60 (M28), on TOOL-dWellOiledMachine-71 and -10. One table-location rule:
  `<target root>/.claude/hook-packs.json` whatever the settings path, read by `dispatch.js` and
  `settings-merge.py`, which takes `--table <path>` for the stale probe's scratch copy; each row's
  `fragment` is normalised to a repo-relative POSIX path. Observed by AC48.
- **S49** — Finding 62 (M29), on TOOL-dWellOiledMachine-73 S1, S2. The legacy-home fallback fires on any
  non-zero `put-card` exit, printing the cause. Observed by AC49.
- **S50** — Finding 64 (M15), on TOOL-dWellOiledMachine-78 S4. A claim whose recorded tick reads
  `unknown` is judged by the age bound alone: stale once its stamp is older than two beats; a claim
  reading `yes` is kept at any age. Observed by AC19.
- **S51** — Finding 65 (M30), on TOOL-dWellOiledMachine-79 S22. `derive_abs_dir` returns non-zero on a
  missing directory, and the lander refuses naming it. Observed by AC51.
- **S52** — Finding 66 (M31), on TOOL-dWellOiledMachine-79 S47 and -57 S1. `PAYLOAD_POPULATIONS` gains
  `life`, `attendance`, `binding` and `decision`, one per namespace S47 scans, and the door reads a
  scan exit 2 as `door — refused · <ref> · scan-unknown-population`. Observed by AC52.
- **S53** — Finding 67 (M10), on TOOL-dWellOiledMachine-79 AC35. The health-log check greps the class,
  `health\.log|resolve_health_log`, over the four suites, never the one spelling `\.git/health\.log`.
  Observed by AC21.
- **S54** — Finding 68 (M32), on TOOL-dWellOiledMachine-79 S31. S31's population is every pack and
  JavaScript producer under `tools/`, `tools/process-monitor/procmon-hook.js:117` included, each
  spawning Python through `pyrun.sh`. Observed by AC54.
- **S55** — Finding 69 (M33), on TOOL-dWellOiledMachine-79 S7. First-use salt creation runs under an
  exclusive node-local `hold_lock` (TOOL-dWellOiledMachine-12) and re-reads after taking it; with no
  writable backend it refuses `commit keys — no backend can store the node salt`. Observed by AC55.

## 3. Non-goals (OUT)

- Every HIGH of the report: TOOL-dWellOiledMachine-80 to -89, one unit each.
- The report's left-shift gates that are spec-set lints (a field-source lint, a reader-inventory lint,
  a chmod-plant ban and their kin): each finding here is closed by its own criterion, and a lint over
  specs is a separate mechanism (M2). S1 is the one exception, because the parallel join is the
  finding itself.
- No re-measurement of a live harness: S6 adds a synthetic log as 36 S3 does, marked so.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-10` — the dispatcher's pack-table read (S48)
- **consumes-from** `TOOL-dWellOiledMachine-12` — the card replay keyed on `owner` and `hold_lock` (S31, S55)
- **consumes-from** `TOOL-dWellOiledMachine-14` — `harness.py capability` and the adapter's skill home (S25, S45)
- **consumes-from** `TOOL-dWellOiledMachine-23` — the map extra keyed on `owner` (S31)
- **consumes-from** `TOOL-dWellOiledMachine-28` — the moved-file list, the moved suites and registries (S10, S21, S22)
- **consumes-from** `TOOL-dWellOiledMachine-32` — `launch_act`'s start-event timeout (S44)
- **consumes-from** `TOOL-dWellOiledMachine-33` — the `Gov-*` trailer filler keyed on `owner` and `commit_keys.py` (S4, S31, S55)
- **consumes-from** `TOOL-dWellOiledMachine-34` — `journal.py read --producer health` (S21, S34, S53)
- **consumes-from** `TOOL-dWellOiledMachine-35` — the session node keyed on `owner` (S31)
- **consumes-from** `TOOL-dWellOiledMachine-36` — the claude-code conformance record (S6)
- **consumes-from** `TOOL-dWellOiledMachine-38` — the orientation exemption keyed on `owner` (S31)
- **consumes-from** `TOOL-dWellOiledMachine-57` — `PAYLOAD_POPULATIONS` and the scan's exit 2 (S52)
- **consumes-from** `TOOL-dWellOiledMachine-58` — the door and `door_fixture.py` (S5, S20, S52)
- **consumes-from** `TOOL-dWellOiledMachine-63` — the node writer, its docstring and its fixture cases (S12, S14, S20, S29, S39)
- **consumes-from** `TOOL-dWellOiledMachine-64` — the moved hooks' load probe and refusal cases (S9, S13, S36, S40)
- **consumes-from** `TOOL-dWellOiledMachine-65` — the stall line, the hold and its reader grep (S7, S11, S27, S41, S42, S43)
- **consumes-from** `TOOL-dWellOiledMachine-67` — the `returned` branch of `launch_act` (S6, S44)
- **consumes-from** `TOOL-dWellOiledMachine-68` — the Skills' `{skill_home}` destination (S23, S45)
- **consumes-from** `TOOL-dWellOiledMachine-70` — the graveyard, its sweep and its renames (S15, S32, S46, S47)
- **consumes-from** `TOOL-dWellOiledMachine-71` — the one-fragment upsert and its stale probe (S48)
- **consumes-from** `TOOL-dWellOiledMachine-72` — the `pruned` predicate (S16)
- **consumes-from** `TOOL-dWellOiledMachine-73` — the card fallback and its held suite (S35, S49)
- **consumes-from** `TOOL-dWellOiledMachine-74` — the kept-return label, `readKeptReturn` and its plant (S2, S17, S26, S33)
- **consumes-from** `TOOL-dWellOiledMachine-75` — the intake's fail-closed plant (S18)
- **consumes-from** `TOOL-dWellOiledMachine-77` — the `owner: machine` value (S31)
- **consumes-from** `TOOL-dWellOiledMachine-78` — the start claim's recorded pid and stale test, and the fixture plants (S19, S20, S50)
- **consumes-from** `TOOL-dWellOiledMachine-79` — the salt, the door's scan, `harness.py`, `derive_abs_dir`, the tickets, the `runtime selftest` leg, the health-log re-point and check 36 (S3, S4, S5, S6, S21, S24, S25, S28, S30, S34, S37, S38, S51, S52, S53, S54, S55)
- **consumes-from** `TOOL-dWellOiledMachine-80` — `check_supervisor_claim_stale`, whose `unknown` reading S50 adds (S50)
- **consumes-from** `TOOL-dWellOiledMachine-86` — the empty-file reading of `pruned` (S16)
- **consumes-from** `TOOL-dWellOiledMachine-88` — the population and head of `pruned` (S16)
- **hands-off** `TOOL-dWellOiledMachine-93` — S1's arm paths in the build-order write set, which that unit moves out of `read_spec_writes` into the caller (finding 25)
- **hands-off** `TOOL-dWellOiledMachine-94` — S1, S4, S10, S22, S23, S48 and S54, and AC4, AC6, AC7, AC14, AC19, AC20, AC23, AC31, AC48 and AC55 (findings 2, 4, 7, 8, 9, 10, 11, 12, 13, 14, 26, 27, 30, 32, 34)
- **hands-off** `TOOL-dWellOiledMachine-95` — S1, AC1, Files touched and the sentences naming S1 as built here, rewritten before this unit builds so S1 is 93's caller-side join and this unit edits no `design_lib` spec reader (round-3 promotions audit, finding 1)

## 4. Design

### Evidence

Each finding's evidence is its row of the report's appendix, which its skeptic re-read and confirmed;
the items cite the clause they correct. Probes re-run for this spec at base `0689e7fa`:

- `derive_parallel_step` reads `writes` from `design_lib.read_spec_writes(text)`
  (`tools/memory-tree/gen_build_index.py:548`, `:1724-1744`), which reads Files touched only (S1).
- `tools/run-gates/run-gates.sh:1757` and `:1766` reap with `rm -rf "$d"` (S15).
- `tools/unattended/gate-guard.js:710` and `:721` require siblings inside `checkAsk` (S13).
- `tools/unattended/check-unattended.sh:4862-4863` holds the `resume-tick.sh` and `stop-guard.js`
  EXEMPT rows (S38), and `:5710` hard-codes `_c31_skill=".claude/skills/unattended/SKILL.md"` (S45).
- `tools/process-monitor/procmon-hook.js:117` spawns `process.env.PROCMON_PYTHON || 'python'` (S54).
- `tools/lib/resolve_bash.py:15` defines `resolve_bash(script)` (S20).
- The `manifest-check self-test` guard is `skills/session-kickoff/` and `{prefix}/lib/`
  (`tools/gate-legs.json`) (S35).
- `tools/workflows/tier2-review.test.sh:338-342` takes `full.split(' · ').pop()` as the stage, and
  `renderAgentLabel(scope, stage)` joins slug, scope and stage (`tools/workflows/tier2-review.template.js:305-306`)
  (S17).
- `tools/unattended/resume-tick.test.sh:240` defines `derive_winpid` (S19).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_host_name` (Python) | function, `gov_record.py` | `read`, OK |
| `--table` | `settings-merge.py` option | none |
| `life`, `attendance`, `binding`, `decision` | `PAYLOAD_POPULATIONS` members | none |
| `reaper` | file inside a graveyard entry | none |
| `bindings-foreign-tag`, `bindings-own-supervisor`, `host-parity` | `door_fixture.py` cases | none |
| `idle-and-unparseable` | `tools/runlog/selftest.py` case | none |
| `stall-from-admission-newest`, `reset-none-after-resume`, `msys-winpid`, `unknown-old-claim` | `supervise.py --fixture` plants | none |
| `killed-reaper-holding-successor`, `open-handle` | `slots.py --fixture` plants | none |

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`, `tools/memory-tree/gen_build_index.py`,
  `memory/builds/dWellOiledMachine/README.md` (re-rendered)
- `tools/memory-tree/gov_record.py`, `tools/memory-tree/door_fixture.py`
- `tools/runtime/supervise.py`, `tools/runtime/resume-tick.sh`, `tools/runtime/limits_fixture.py`,
  `tools/runtime/commit_keys.py`, `tools/runtime/tickets.py`, `tools/runtime/commit_queue.py`,
  `tools/runtime/slots.py`, `tools/runtime/locks.py`, `tools/runtime/secret_scan.py`,
  `tools/runtime/act.py`, `tools/runtime/harness.py`, `tools/runtime/session_binding.py`,
  `tools/runtime/session_node.py`, `tools/runtime/dispatch.js`, `tools/runtime/intake.py`,
  `tools/runtime/selftest.py`, `tools/runtime/resume-tick.test.sh`
- `tools/runtime/fixtures/conformance/claude-code-2.1.292/`
- `tools/runtime/stop-guard.js`, `tools/runtime/stall-recorder.js`, `tools/runtime/gate-guard.js`
- `tools/workflows/tier2-review.template.js`, `tools/workflows/tier2-review.js`,
  `tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js`,
  `tools/workflows/unattended-unit.js`, `tools/workflows/tier2-review.test.sh`,
  `tools/workflows/unattended-build.test.sh`, `tools/workflows/README.md`
- `tools/settings-merge.py`, `tools/govkit/govkit.py`, `tools/check-wiring.sh`, `tools/push-main.sh`
- `tools/runlog/selftest.py`
- `tools/process-monitor/selftest.py`, `tools/process-monitor/procmon-hook.js`
- `tools/unattended/check-unattended.sh`, `tools/gate-legs.json`, `tools/run-gates/selftest-budgets.txt`
- `memory/project/spawn-idiom-sites.txt`, `memory/project/substitution-fed-loops.txt`
- `skills/session-kickoff/manifest-check.sh`, `help/runtime.md`
- the rev bumps of specs 8, 9, 12, 14, 16, 32, 38, 63, 64, 65, 67, 70, 74 and 79 under
  `memory/builds/dWellOiledMachine/spec/`

### Alternatives rejected

- **Two batches split by kit.** The fixes meet in `supervise.py`, `door_fixture.py`, `gov_record.py` and
  `tools/gate-legs.json` (§1), so the halves would share write paths and M6 forbids running them
  together.
- **Age alone for every claim (S50).** The skeptic's other option; it reaps a live slow tick's claim,
  which S19's exact pid read now keeps.

## 5. Production-readiness checklist

- security — S4 and S55 keep the salt fixtures off the real keychain and the first-use creation
  exclusive; S5 and S52 put the binding and decision namespaces behind the door's fleet-tag rule and
  scan; S31 stops a machine-launched session from losing its trailers or skipping orientation.
- perf / scale — S37 prices the widened `runtime selftest` leg.
- error / empty / loading states — S43 gives `reset=none` a finite hold; S47 names every rename
  outcome; S49 and S51 fail closed on a failed preferred path and a missing directory.
- observability — S2's and S1's re-rendered build order shows which steps are serial.
- risks — until this unit builds, steps 8 and 32 of the build order must be dispatched serially: the
  builders of units 68 and 74 add the arm file to the path list `--dispatch` records. The criteria
  these findings name stand answered by this unit's criterion of the same finding.
- testing — AC1 to AC55 and the arms in §7.
- migration — S48 normalises `fragment` keys on the next call; a table written with a second spelling
  is rewritten to one row.
- user docs — S23's and S39's `help/runtime.md` lines.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --write` re-renders the build README, the
  build-order row of step 8 reads `no`. Red when: a `New arm:` path stays outside the write set and
  step 8 reads `yes`.
- **AC2** — When the same render runs, step 32's row reads `no`, and `grep -n "supervise.py"`
  over spec 74's Files touched prints a line. Red when: step 32 reads `yes`.
- **AC3** — When `grep -c "runtime selftest"` over the run-gates budget file `selftest-budgets.txt`
  prints 1, and `grep -l -- --fixture` over the runtime kit's Python modules lists every module the
  runner's `--modules` population names. Red when: the row is duplicated, or the population is staged empty and the list exits 0.
- **AC4** — When `python commit_keys.py --fixture --case env-salt` runs under a scratch policy with
  `runtime.secret-home = "env-injected"` and `GOV_SECRET_NODE_SALT=ab`, the digest is the HMAC under
  `ab`; with the variable unset it refuses. Red when: the variable is ignored and a digest prints.
- **AC5** — When `python door_fixture.py --case bindings-foreign-tag` runs, the write is refused
  `cross-session`, and `--case bindings-own-supervisor` is admitted. Red when: the fleet-tag rule is
  absent.
- **AC6** — When `python conformance.py run --replay claude-code-2.1.292`
  runs, it writes a `prompt-submit` row marked `synthetic`. Red when: the row stays `unmeasured`.
- **AC7** — When `git grep -nE "stall\.[^ ]*\.log|'stall'.*\.log|unattended/stall" -- tools/runtime tools/unattended`
  runs, it prints nothing outside a retirement note. Red when: a scratch `supervise.py` opening
  `<git-dir>/unattended/stall.<slug>.log` is matched.
- **AC8** — When `grep -c "eight .to. rows"` runs over spec 14's file `2026-10-26-spec-TOOL-dWellOiledMachine-14.md`
  it prints 1 or more, the same over spec 16 for `check_commitment`, over specs 38, 8 and 12 for
  `correction for finding 50`, `correction for finding 59` and `correction for finding 63`, and
  `grep -c "survives"` over spec 9 prints 0. Red when: a promised correction is missing, as each of
  these greps reads at this spec's base.
- **AC9** — When the static probe runs over a scratch `tools/runtime/` with `render-message.js`
  renamed, it exits 1 naming each module requiring it, `gate-guard.js` included; the `stop-guard.js`
  and `stall-recorder.js` refusal cases each fail with the renderer renamed. Red when: a lazy require
  goes unprobed.
- **AC10** — When `grep -c` runs over `spawn-idiom-sites.txt` and `substitution-fed-loops.txt` for every
  old path in 28 S1's moved list, each prints 0. Red when: a stale path-keyed row remains.
- **AC11** — When `grep -c "basic form"` runs over spec 65's file it prints 0, and
  `grep -n "TOOL-dWellOiledMachine-81"` there names its third non-goal, its §5 risk line, its AC1 and
  its §10, beyond the §3 edge line it carries at this spec's base. Red when: the format or the
  field's source is still unstated.
- **AC12** — When `grep -c "VERBS.template.md runtime.md"` runs over spec 63's file it prints 0, and its
  AC6 names `runtime.md`. Red when: AC6 still names a bare `runtime.md`, as it does at this
  spec's base.
- **AC13** — When `grep -c "lazily inside"` runs over spec 64's file it prints 1 or more. Red when: §4
  still calls `gate-guard.js:710` a load-time require, as it does at this spec's base.
- **AC14** — When `grep -c "node writer" gov_record.py` and
  `grep -c "node writer" runtime.md` run, each prints 1 or more. Red when: either is 0.
- **AC15** — When `grep -n "rm -rf"` and `grep -n "TOOL-aReapedTicket-4"` run over spec 70's file, both
  print. Red when: §10 still claims a rename reap.
- **AC16** — When the `idle-and-unparseable` fixture case, on its §7 `New arm:` line, runs, `verify` prints
  `pruned` and exits 0. Red when: either cut alone reads `mismatch`.
- **AC17** — When the tier2-review stub runner spawns a kept-return agent, `label.split(' · ').pop()`
  returns the bare stage and `full` carries `#<print>`. Red when: the stage segment carries the print.
- **AC18** — When `python intake.py fixture --case requests-unwritable` replaces `requests/` with a file,
  the pack fails and the dispatcher refuses the prompt, on node a. Red when: the write succeeds.
- **AC19** — When `python supervise.py --fixture --plant msys-winpid` runs a live tick older than two
  beats, its claim is kept; `--plant unknown-old-claim` with a failing probe reaps it after two beats.
  Red when: a live tick's claim is reaped, or an `unknown` claim blocks every start.
- **AC20** — When `git grep -nE "\[\"bash\"|\['bash'" -- supervise.py door_fixture.py`
  runs, it prints nothing. Red when: a bare `bash` argv remains.
- **AC21** — When `git grep -nE "health\.log|resolve_health_log"` runs over the four suites of 79 S35,
  it prints nothing outside `journal.py read --producer health` call sites. Red when: a suite reads
  the retired log.
- **AC23** — When `git grep -n '\.claude/skills/\(runlog\|unattended\)' -- tools` runs outside kit
  descriptors and suites, each hit is listed in `runtime.md`'s claude-code-only readers or
  reads `{skill_home}`. Red when: an unlisted hard-coded reader remains.
- **AC24** — When the lander's fixture stores the trusted path as `C:/PROJECTS/…` and `core.hooksPath`
  as `c:/projects/…`, the landing is not refused. Red when: a case variant compares unequal.
- **AC25** — When `grep -c -- "--read" harness.py` runs it prints 0, and
  `grep -n "harness.py capability" tools/check-wiring.sh` prints the session arm. Red when: a second
  verb over `read_capability` remains.
- **AC28** — When `git grep -nE "def (add_ticket|read_queue|remove_ticket|remove_stale_tickets)" -- tools/runtime`
  runs, it prints only `tickets.py`, and the commit queue's `dead-head-ticket` case commits. Red when:
  the sweep is dropped and a dead head ticket blocks the queue.
- **AC29** — When `python door_fixture.py --case host-parity` runs with `COMPUTERNAME=AbC` and with it
  unset, the Python and bash readers print the same name. Red when: they differ.
- **AC30** — When `grep -n "push-main self-test"` runs over spec 79's §7, the leg line names it with
  `settings-merge selftest`. Red when: either leg is absent.
- **AC31** — When a session is resumed under the tick's environment, binding `machine`, its card is
  replayed and its commit carries `Gov-*` trailers, and the orientation gate still asks for a card.
  Red when: `machine` reads as not-`yes` in any of the five readers.
- **AC32** — When `python slots.py --fixture --plant killed-reaper-holding-successor` runs, the sweep
  restores the successor's slot, and `slots.py status` over a non-empty graveyard counts only
  `slot.<k>`. Red when: the sweep deletes a held reservation's slot.
- **AC35** — When `python -c` reads `tools/gate-legs.json`, the `manifest-check self-test` guard lists
  `session_binding.py`. Red when: the held suite's guard misses the kit.
- **AC36** — When `grep -n "moved from"` runs over spec 64's file and finds the bare directory token, it prints
  nothing. Red when: the bare directory token remains.
- **AC37** — When `grep -n "runtime selftest" tools/run-gates/selftest-budgets.txt` runs, its reason
  names the measured figure and its date, and the leg's `ceiling` is at least that figure. Red when:
  the leg was widened unpriced.
- **AC38** — When `grep -c "stop-guard.js" tools/unattended/check-unattended.sh` runs over check 36's
  EXEMPT rows, it prints 0 there. Red when: the dead row remains.
- **AC43** — When `python supervise.py --fixture --plant stall-from-admission-newest` and
  `--plant reset-none-after-resume` run, the first holds on the recorder line, and the second, after
  the owner's `resume`, launches without holding again. Red when: the hold reads an admission line or
  loops on a stale `reset=none`.
- **AC44** — When `act.py`'s fixture launches a stub that never prints its start event under
  `preset-session-id = returned`, `launch_act` kills it after `ACT_START_SECONDS`, records
  `state: failed` and exits 3. Red when: the launch reads forever.
- **AC45** — When `check-unattended.sh` runs on a scratch target adopted under `.agents/skills` with no
  environment override, check 31 runs rather than printing `check 31 skipped`. Red when: the
  hard-coded path skips it.
- **AC47** — When `python slots.py --fixture --plant open-handle` holds a handle open inside a slot on
  node a, the reap skips it and retries at the next beat, and a restore onto an occupied index takes
  the next free one. Red when: a sharing violation crashes the reap or a restore overwrites.
- **AC48** — When `settings-merge.py` runs with `GOV_SETTINGS_JSON` naming a relative `config` settings file, the
  table is written at the repository's own `hook-packs.json`, and one fragment upserted under two spellings yields one row.
  Red when: the table moves with the settings path or a fragment is spelled twice.
- **AC49** — When the card store's fixture makes `put-card` exit 2, the card lands at its legacy home
  and the cause is printed. Red when: no card is written in either home.
- **AC51** — When the `push-main.sh` fixture names a trusted copy that is absent, the landing is refused
  naming the missing directory. Red when: two missing directories compare equal.
- **AC52** — When `python door_fixture.py --case life-token`, `--case attendance-token`,
  `--case binding-token` and `--case decision-token` each write a record carrying a token, each is
  refused by the scan. Red when: a namespace has no population and exit 2 is read as clean.
- **AC54** — When `git grep -nE "'python'" -- tools` runs over packs and JavaScript producers, it prints
  only the exempt list. Red when: `procmon-hook.js` still spawns a bare `python`.
- **AC55** — When `python commit_keys.py --fixture --case first-use-race` starts two first users
  together twenty times, every run ends with one salt and both digests equal. Red when: two salts are
  minted.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `pre-push run-log line` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `process-monitor census selftest` · `runlog selftest` · `run-gates canary` · `run-gates gov canary` · `run-gates run-log line` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `transition-audit arms` · `straggler-guard arms` · `check-wiring self-test` · `push-main self-test` · `settings-merge selftest` · `unattended kit gate` · `python resolver (behaviour + inline parity + idiom ban)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/memory-tree/door_fixture.py · covers AC5 AC29 AC52 · each case staged against the door with the fleet-tag rule, the host parity and the new populations removed · none
New arm: tools/runtime/supervise.py · covers AC19 AC43 · the plants staged against a claim recording `$$` and a hold reading every `stall` line · none
New arm: tools/runlog/selftest.py · covers AC16 · the combined cut staged against a predicate reading the first line as the head · none
New arm: tools/runtime/slots.py · covers AC32 AC47 · the killed-reaper and open-handle plants staged against a sweep that deletes by nonce · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the promotions audit's 55 medium and low findings batched.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-93, TOOL-dWellOiledMachine-94.
- rev-3 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-3
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-95.

## 10. Reuse audit

Each item extends the seam its finding names: `read_spec_writes` (S1), `read_secret_ref` (S4, S55),
the door and `door_fixture.py` (S5, S29, S52), `derive_conformance_rows`' synthetic record (S6),
`resolve_bash` (S20), `journal.py read` (S21, S34, S53), `harness.py capability` (S25),
`check_pid_alive` and `derive_winpid`'s reasoning (S19, S50), `renderAgentLabel` (S17), `hold_lock`
(S55) and `pyrun.sh` (S54). The probe `python tools/codebase-map/reuse_lookup.py "batch the spec audit
minor findings"` ranked spec readers rather than any fix's seam, so the seams are the per-item ones
above; no item mints a module.

Recall terms used: `python tools/memory-recall/query.py "how are a spec audit's medium and low
findings batched" --terms "minors batch spec audit medium low promoted findings write set capability
rows pyrun"`
