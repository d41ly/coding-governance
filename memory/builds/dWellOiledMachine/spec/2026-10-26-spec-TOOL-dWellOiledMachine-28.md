# TOOL-dWellOiledMachine-28 — the unattended kit dissolved: its hooks and its tick taken into the runtime kit, `RESUME_SCHEDULE_*` retired, `/unattended` a client of `run`, with the upgrade steps that carry adopters across

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 61 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0306@a3aa83b5 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-48 |
| [2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

The hook surface spans five kits, the unattended kit wiring three hooks of its own (gap-tool-03), and
the kit restarts a held run through a durable task an agent files by hand (`RESUME_SCHEDULE_*`) while
its tick resumes a stalled one with `--dangerously-skip-permissions` (gap-rt-04). This unit dissolves
the kit into the runtime's own kit as the clause names it: its three hooks repacked as runtime packs
behind the one dispatcher entry per event, its supervisor seam `resume-tick.sh` taken into the runtime
kit with an adopter's hand-registered `gov-resume-tick` task kept as the node tick that starts and
restarts it, the `RESUME_SCHEDULE_*` task retired in favour of that tick, and `/unattended` made a
client of `run` until dConvergedCharter retires it. Each change an adopter's tree must cross is an
upgrade step (night pass `[p1-unattended]` point 1, P38; layer-runtime `[supervise]`).

## 2. Scope (IN)

- **S1** — The three hooks taken into the runtime kit (I1). `gate-guard.js`, `stop-guard.js`,
  `stall-recorder.js`, the module they share, `run-lease.js`, their three `*.fragment.json` and
  their three suites move from `tools/unattended/` to `tools/runtime/` with `git mv`, so blame
  follows. Each fragment's `hook_path` becomes `{kit}/runtime/<name>.js` and its pack fields
  (TOOL-dWellOiledMachine-10 S1, which gave these three fragments the fields in place) name `owner`
  `runtime`. The runtime descriptor `tools/runtime/kit.toml` gains `settings-merge` in `requires` and
  withholds the three moved suites with a `project-owned` row, on the ruling
  `tools/unattended/kit.toml:20-54` records; the unattended descriptor drops them from its
  `project-owned` row (`:54`) and drops `settings-merge` from `requires` (`:13`), whose only reason
  was shipping fragments (`:7-9`). Observed by AC1.
  **Readers:** by name: `.claude/settings.json` (a render, its lines 27, 91 and 106, re-rendered by S2);
  `tools/govkit/selftest.py:2341-2376` (`check_fragment_wiring`, which uses these three fragments as
  its subject through `KIT_NAMES['unattended']`, re-pointed to the runtime kit's);
  `tools/run-gates/selftest-budgets.txt:139-142` and `tools/run-gates/selftest-pooled-evidence.txt`
  (lines 49 and 52, the suite rows, S8); `tools/unattended/README.md`, `tools/unattended/kit.toml:54`. by value:
  `tools/unattended/adopt-unattended.sh:836-900`, the fragment loop over `"$KIT_DIR"/*.fragment.json`
  (`:875`), whose zero-population guard would red once the kit ships no fragment: the block goes, and
  the three packs are graded both ways by check-wiring's `check_packs` (TOOL-dWellOiledMachine-10 S4).
- **S2** — The repacked hooks wired through one dispatcher entry per event. `settings-merge.py`
  renders the three runtime fragments into the pack table and the `PreToolUse`, `Stop` and
  `StopFailure` entries whose command is `dispatch.js <Event>` (TOOL-dWellOiledMachine-10 S3); no
  settings entry names a moved hook. Observed by AC2.
- **S3** — One way from a moved file to the driver, `tools/runtime/driver.sh`. `driver.sh --dir`
  prints the unattended kit's directory, found by the canonical `resolve_kit_dir` block
  (`tools/lib/resolve_kit_dir.py`, carried inline in a quoted heredoc as every shell consumer carries
  it, so the resolve-python self-test's parity arm, which finds every copy by its marker line, grades
  it with no table edit): the install receipt,
  then the probe, then a refusal naming the three places looked, exit 2. `driver.sh <verb> <args>…`
  runs `bash <dir>/unattended.sh <verb> <args>…` with the caller's cwd. The moved packs call the driver
  only through it: `stop-guard.js`'s `runLiveness` (`tools/unattended/stop-guard.js:102-108`) spawns
  `bash <runtime dir>/driver.sh --liveness <slug>`, and the remedy texts that name the driver
  (`stop-guard.js:164-169`, `gate-guard.js:750-755`) print the directory `driver.sh --dir` resolved,
  relative to the repository root. Observed by AC3, AC4.
- **S4** — The supervisor seam taken. `resume-tick.sh` and its suite move to `tools/runtime/` with
  `git mv`, carrying TOOL-dWellOiledMachine-6's `run_supervisors` and `run_reconcile` with them. Its
  kit-directory derivation (`tools/unattended/resume-tick.sh:111-117`) splits in two: `KIT_DIR`, its
  own, for the runtime siblings, and the driver's directory from `driver.sh --dir`, from which it sources
  `lib-unattended.sh` (`read_tick_registration`, `check_pid_alive`, `read_bound_key`) and names
  `DRIVER`. The old path `tools/unattended/resume-tick.sh` keeps a forwarder of one command,
  `exec bash "<runtime dir>/resume-tick.sh" "$@"`, the runtime dir found by the same inline
  `resolve_kit_dir`, so an adopter's hand-registered `gov-resume-tick` task, which names that path,
  runs the node tick unchanged; the forwarder is deleted when `install.deprecation-window` closes over
  S7's step U2 (TOOL-dSafePassage-6 S5). `read_tick_registration`
  (`tools/unattended/lib-unattended.sh:674-686`) is unchanged: it asks for the task by its name,
  `gov-resume-tick`, never by its path. Observed by AC5.
  **Readers:** by name: the registration lines of `tools/unattended/README.md` (lines 224 and 231), which
  move to the runtime kit's README, READER NOT IN TREE until this unit creates it, naming the tick at its
  runtime path; the four budget rows of S8.
  by value: NO VALUE READERS — the task is matched by name.
- **S5** — The `--dangerously-skip-permissions` launch stays retired. TOOL-dWellOiledMachine-6 S11
  rebuilt the tick's one hand-built argv (`tools/unattended/resume-tick.sh:385`) through `launch_act`;
  this unit moves that file and adds S6's launch on the same path, so no file under either kit builds a
  skip-permissions argv. Observed by AC6.
  **Readers:** by name: `tools/unattended/resume-tick.sh` (moved by S4, its launch rebuilt by
  TOOL-dWellOiledMachine-6 S11) and `tools/unattended/resume-tick.test.sh`, whose arm on the launch
  moves with it. by value: NO VALUE READERS — the flag is an argv word no file reads back.
- **S6** — The restart a hold owes becomes the node tick's. `--hold` keeps computing the fire instant
  and recording `resume-owed <name> · fire <utc>` exactly as today
  (`tools/unattended/unattended.sh:6968-7020`), so `--status` and `--close` read the record unchanged;
  it prints `unattended: resume-owed <name> · fire <utc> — the node tick launches it` in place of the
  instruction to file a durable task (`:7070-7077`). A new driver verb `--restart-prompt <slug>` runs
  `print_restart_prompt`, the three prompt lines `:7074-7076` print today with the third rewritten to
  drop the durable task: "If the driver refuses or prints still held, delete the keepalive you
  scheduled for this resume, list your scheduler's jobs to confirm it is gone, and stop." The tick's
  HELD row (`resume-tick.sh:293-297`) becomes `run_held_restart`: `read_restart_due` reads
  `resume-owed`; on `none · <why>` it prints `skip · HELD · no restart owed (<why>)`; on a fire instant
  still ahead, `skip · HELD · fire <utc>`; on one passed, unless an attempt line for this `held-at`
  already exists in the slug's sidecar, it appends the attempt line `held <held-at> launched <pid> <utc>
  <image>` and launches one fresh act session in the run's worktree with the `--restart-prompt` lines as
  its prompt through the launch path TOOL-dWellOiledMachine-6 S11 gave the tick, printing `restart ·
  HELD · fire <utc> passed · attempt <n> · out <path>`. A second tick over the same `held-at` prints
  `skip · HELD · restart launched <pid> at <utc>`, so each hold is restarted once, as each durable task
  was ONE-SHOT; `RESUME_ATTEMPTS` caps the lines as it caps the STALE row's. `--dry-run` prints the row
  with ` (dry-run)` and launches nothing. Observed by AC7.
  **Readers:** by name: `tools/unattended/unattended.sh` (the print at lines 7070-7077) and
  `tools/unattended/STOPS.template.md`, the guide that tells an agent to file the durable task, rewritten
  by S7. by value: `tools/unattended/resume-tick.sh`, whose HELD row reads `resume-owed`, kept.
- **S7** — The `RESUME_SCHEDULE_*` task retired: all five keys, `RESUME_SCHEDULE`,
  `RESUME_SCHEDULE_CREATE`, `RESUME_SCHEDULE_DELETE`, `RESUME_SCHEDULE_DELAY` and
  `RESUME_SCHEDULE_LIMIT`. The driver stops reading them (`unattended.sh:564`, `:576-589`,
  `:657-662`, `:683-684`); the fire delay and the no-progress limit become the kit constants
  `HOLD_FIRE_DELAY_SECONDS=1800` and `HOLD_STREAK_LIMIT=6`, PINNED at today's defaults
  (`RESUME_SCHEDULE_DELAY_DEFAULT`, `RESUME_SCHEDULE_LIMIT_DEFAULT`, `:453-454`), read by
  `resolve_resume_fire` (`:1215`) and the streak test (`:6982`); the `off` and `no carrier` arms
  (`:6973-6981`) go, since the tick is the carrier and an adopter opts out by not registering
  `gov-resume-tick`, which keeps TOOL-dDerivedDocket-5's auto-resume on. `print_reap_targets`
  (`:1246-1255`) prints the keepalive alone. The kit gate's half of check 46 that grades the five keys
  (`tools/unattended/check-unattended.sh:3358-3388`), their initialisers (`:254-255`) and their allowlist
  row (`:338`) go; a conf still naming a key is ignored by the allowlist, never refused. The skill
  template drops `{{RESUME_SCHEDULE_CREATE}}` and `{{RESUME_SCHEDULE_DELETE}}` (`SKILL.template.md:130`,
  `:178`), the descriptor drops both from `placeholders` (`kit.toml:66`), `conditional_keys` (`:178`),
  its `why` (`:316`) and the discharge probe (`:338-348`), and the adopter drops their fill
  (`adopt-unattended.sh:137-138`, `:161-163`, `:710-711`). The guides lose the five-key table, the
  carrier rule and the filing steps (`STOPS.template.md:360-412`, `VERBS.template.md:356`, `:845`,
  `:963-967`, `PROTOCOL.template.md:520`), each replaced by one line naming the node tick as the
  restart. `tools/policy/legacy-homes.txt` is regenerated by `python policy.py lists --write`, its five
  rows (`:99-103`) dropping because no home holds them. Observed by AC8.
  **Readers:** by name: `.unattended.conf:141-153`, `tools/unattended/.unattended.conf.example:137-156`,
  `tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`,
  `tools/unattended/adopt-unattended.sh`, `tools/unattended/kit.toml`,
  `tools/unattended/resume-tick.sh:295`, `tools/unattended/SKILL.template.md`,
  `tools/unattended/STOPS.template.md`, `tools/unattended/VERBS.template.md`,
  `tools/unattended/PROTOCOL.template.md`, `tools/policy/legacy-homes.txt`, and the suites
  `tools/unattended/unattended.test.sh`, `tools/unattended/check-unattended.test.sh`,
  `tools/unattended/adopt-unattended.test.sh`, `tools/unattended/cross-component.test.sh`, whose arms
  asserting the retired behaviour are deleted; `tools/workflows/unattended-build.test.sh` (lines 2342 and 2380)
  writes two keys into a fixture conf and asserts nothing about them, so the lines are left inert;
  `tools/govkit/govkit.py:2382` names the key in a historical comment and is left. by value:
  `unattended.sh` `:657-662` (the switch), `:683-684` (delay and limit), `:1215`
  (`resolve_resume_fire`), `:6973-6985` (the hold's owed decision), `:7070-7077` (the print);
  `check-unattended.sh:3358-3388` (check 46's half); `adopt-unattended.sh:161-163`, `:710-711`;
  `kit.toml:178`, `:348`.
- **S8** — The moved suites' budget rows. `tools/run-gates/selftest-budgets.txt:139-142` become
  `runtime gate-guard selftest`, `runtime stall-recorder selftest`, `runtime stop-guard selftest` and
  `runtime resume-tick selftest`, each argv `bash {prefix}/runtime/<suite>`, budgets unchanged, so
  `run-selftests.sh --kit` lists them under the runtime kit; `selftest-pooled-evidence.txt:49,52`
  follow the names. Observed by AC1.
  **Readers:** by name: `tools/run-gates/selftest-budgets.txt`, `tools/run-gates/selftest-pooled-evidence.txt`.
  by value: `tools/unattended/run-unattended-gates.sh:451`, which counts the unattended kit's rows
  through `--kit` and keeps a non-zero population after the move, the driver, gate and checker rows
  staying.
- **S9** — `/unattended` a client of `run`. In `tools/unattended/SKILL.template.md`, the slug path's
  steps after preflight and kickoff end with `run <slug>`, the verb TOOL-dWellOiledMachine-25 ships,
  which registers the build with the node's supervisor; the "Drive by `scriptPath`" sentence
  (`:124-125`) is replaced by one saying the supervisor drives every pass and the session watches with
  `unattended.sh --status <slug>`. The prompt path's step 5 takes the same `run <slug>`. The rendered
  `.claude/skills/unattended/SKILL.md` is re-rendered by `adopt-unattended.sh --render`, and stays
  under the `unattended skill size` leg's ceiling, the template losing more lines than it gains. The
  keepalive section and the close, land and hold paths are unchanged. Observed by AC9.
  **Readers:** by name: `tools/unattended/SKILL.template.md` and its render `.claude/skills/unattended/SKILL.md`;
  `tools/unattended/check-unattended.sh`, which grades the skill's `scriptPath` sentence, re-pointed in
  the same unit with `tools/unattended/check-unattended.test.sh`. by value: NO VALUE READERS — a sentence
  an agent reads, never a value a program parses.
- **S10** — The upgrade steps, `[[upgrade]]` rows in TOOL-dSafePassage-1 S1's grammar, all run by one
  program `tools/govkit/steps/unattended_dissolve.py <step> up|down|witness {target} {prefix}`, writing
  its before-image with that spec's helpers from `tools/govkit/upgrade_steps.py`. Observed by AC10.
  - **U1** `runtime/unattended-hooks-to-packs`, in `tools/runtime/kit.toml`: up removes a target's
    per-fragment entries whose command names `<prefix>/unattended/<hook>.js` for the three hooks,
    through `remove_wired_fragments` (`tools/govkit/govkit.py:6180`), then re-renders through
    `run_fragment_merges` (`:6109`) so the dispatcher entries carry the packs at `<prefix>/runtime/`;
    witness exits 0 only when no settings hook names a moved hook and the pack table lists the three.
    `surfaces = ["file:.claude/settings.json", "file:.claude/hook-packs.json"]`.
  - **U2** `runtime/resume-tick-to-runtime`, in `tools/runtime/kit.toml`: up writes nothing, the
    forwarder shipping as an engine file; witness exits 0 when `<prefix>/unattended/resume-tick.sh
    --dry-run` and `<prefix>/runtime/resume-tick.sh --dry-run` print the same lines. `surfaces =
    ["file:{prefix}/unattended/resume-tick.sh"]`, the window member S4's forwarder is deleted by.
  - **U3** `unattended/resume-schedule-retired`, in `tools/unattended/kit.toml`: up removes every
    assignment of the five keys from the target's `.unattended.conf` with their comment lines; down
    restores the before-image; witness exits 0 when no line assigns one. `surfaces` names the five
    `conf-key:.unattended.conf#<key>` members. The durable tasks an adopter's agent already filed sit
    in a harness store no script reaches (`unattended.sh:7058-7061`): U3's up prints
    `unattended: <n> durable task(s) named unattended-resume-<slug> may remain in your harness
    scheduler; delete them with the tool RESUME_SCHEDULE_DELETE named` once per held slug it finds.
  **Readers:** by name: `.claude/settings.json` and `tools/govkit/govkit.py` (`remove_wired_fragments`,
  `run_fragment_merges`) for U1; `tools/unattended/resume-tick.sh` for U2; `.unattended.conf` and
  `tools/unattended/.unattended.conf.example` for U3. by value: NO VALUE READERS — the rows' `surfaces` are read by TOOL-dSafePassage-1 S1's upgrade
  helpers, unbuilt at HEAD, and the files the steps change are the readers by name holds.
- **S11** — The page. `help/runtime.md` gains a section: the three packs and `driver.sh`, the tick at
  its runtime path with the old path's forwarder, the HELD restart and its one-shot rule,
  `RESUME_SCHEDULE_*` retired with the opt-out now being not registering `gov-resume-tick`, `/unattended`
  as a client of `run`, and the three upgrade steps. `tools/unattended/README.md` points there.
  Observed by AC11.
  **Readers:** by name: `tools/unattended/README.md`, and the runtime help page, READER NOT IN TREE
  until TOOL-dWellOiledMachine-1 creates it; the retired keys' readers are S7's. by value: NO VALUE READERS — prose pages.

## 3. Non-goals (OUT)

- Moving `unattended.sh`, its checkers, its guides or its skill out of `tools/unattended/`: the kit
  keeps them as the `/unattended` shim's home and its backing verbs until dConvergedCharter retires
  `/unattended` (§8 F1). The driver functions v2 gives a loop-kit home reach it through their own
  units: the position ladder through TOOL-dDeclaredLoop-7 and TOOL-dWellOiledMachine-2, the owner's
  controls through TOOL-dWellOiledMachine-3, and the supervisor driving every pass through
  TOOL-dWellOiledMachine-25.
- The `run` verb and the supervisor as the only driver: TOOL-dWellOiledMachine-25. `/build` as a client
  of `run`: the same unit.
- The keepalive (`CronCreate` in the skill's first section, UNATTENDED-PROTOCOL.md section 5) and
  stop-guard's `session_crons`: a governance-carrier change no clause this unit carries names, so the
  shim keeps them; their retirement goes with `/unattended`'s, at dConvergedCharter.
  TOOL-dWellOiledMachine-13 §3 points the keepalive here; this unit does not take it (the return says so).
- The DURABILITY writes in three harnesses and `unattended-unit.js`'s `committed:false` (layer-runtime
  :1076-1078): not this clause's.
- The pack contract, the dispatcher and `check_packs`: TOOL-dWellOiledMachine-10. The tick's launch
  through `launch_act`: TOOL-dWellOiledMachine-6 S11.
- Re-registering an adopter's `gov-resume-tick` task: the owner's act, once per node; S4's forwarder is
  what keeps it working.
- Running the unattended or runtime suites: waived for this build's landing (README rule 8); their
  clean reading is owed with PLAY-dClosedLoop-15.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-10` — `dispatch.js`, the one entry per event the three repacked hooks run behind, with the pack fields and `check_packs` that grade them; without it S2 has no entry to render into
- **consumes-from** `TOOL-dWellOiledMachine-6` — `supervise.py` and `resume-tick.sh`, the supervisor seam this unit takes into the runtime kit, with the `launch_act` launch path S6 launches a held run's restart through
- **consumes-from** `TOOL-dWellOiledMachine-25` — `run`, the verb `/unattended` becomes a client of in S9
- **consumes-from** external — TOOL-dSafePassage-1 S1's `[[upgrade]]` row grammar and its `upgrade_steps.py` helpers, TOOL-dSafePassage-6 S5's window over `install.deprecation-window`
- **hands-off** external — dConvergedCharter retires `/unattended`, the kit's remaining files and the forwarder's last reader with it

## 4. Design

### Evidence

- The three hooks, their module and their suites are the kit's only hook files:
  `git ls-files tools/unattended | grep -E 'guard|recorder|run-lease'` lists 10 paths at this base, and
  `run-lease.js` has no requirer outside them but a comment (`unattended.sh:6243`).
- Each hook finds the driver beside itself (`stop-guard.js:102-108`, `gate-guard.js:710-722`), and the
  tick derives `DRIVER` and sources the library from its own directory (`resume-tick.sh:111-117`), so a
  move with no resolver breaks all four.
- `read_tick_registration` matches `gov-resume-tick` by task name under Windows and the string
  `resume-tick` in the crontab listing (`lib-unattended.sh:678-683`), and the registration lines put
  the kit path inside the task (`tools/unattended/README.md:224,231`).
- The durable restart is a prompt an agent files (`unattended.sh:7058-7077`), the tick skips HELD
  (`resume-tick.sh:293-297`), and the owner ruled auto-resume on (TOOL-dDerivedDocket-5,
  `memory/DECISIONS.md:119`).
- `check-unattended.sh`'s conf import is an allowlist (`:333-341`), so a key it drops is ignored.

### The node tick, after this unit

| Verdict | Row | Owner |
|---|---|---|
| HELD, no restart owed | `skip · HELD · no restart owed (<why>)` | S6 |
| HELD, fire ahead | `skip · HELD · fire <utc>` | S6 |
| HELD, fire passed, no attempt for this `held-at` | `restart · HELD · …`, one fresh act launched | S6 |
| HELD, attempt already made | `skip · HELD · restart launched <pid> at <utc>` | S6 |
| every other verdict | unchanged | TOOL-dWellOiledMachine-6 |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `driver.sh` with `--dir`, `resolve_driver_dir` | runtime kit file, shell function | `sh.function`, OK |
| `run_held_restart`, `read_restart_due` | shell functions in `resume-tick.sh` | `sh.function`, OK |
| `--restart-prompt`, `print_restart_prompt` | driver verb, shell function | `sh.function`, OK |
| `HOLD_FIRE_DELAY_SECONDS`, `HOLD_STREAK_LIMIT` | driver constants, 1800 and 6, PINNED | none |
| `unattended_dissolve.py` with `up`, `down`, `witness`, `fixture` | step program | asked at the pass |
| U1, U2, U3 step ids | `[[upgrade]]` rows | none |

The two constants are PINNED at the kit defaults the driver carries at this base (`:453-454`).

### Migration

An adopter's next govkit `update` lands the moved files, runs U1, U2 and U3 in TOOL-dSafePassage-1's
order, and re-renders the skill and the guides. A `.unattended.conf` that keeps a retired key after
U3's down is read as before by nothing: the allowlist ignores it. A node whose `gov-resume-tick` task
names the old path keeps ticking through the forwarder until the window closes; the runtime README
gives the new line for a re-registration.

### Files touched (estimate)

- `tools/runtime/gate-guard.js`, `tools/runtime/stop-guard.js`, `tools/runtime/stall-recorder.js`,
  `tools/runtime/run-lease.js` (moved from `tools/unattended/`)
- `tools/runtime/gate-guard.fragment.json`, `tools/runtime/stop-guard.fragment.json`,
  `tools/runtime/stall-recorder.fragment.json` (moved)
- `tools/runtime/gate-guard.test.sh`, `tools/runtime/stop-guard.test.sh`,
  `tools/runtime/stall-recorder.test.sh`, `tools/runtime/resume-tick.test.sh` (moved)
- `tools/runtime/resume-tick.sh` (moved), `tools/unattended/resume-tick.sh` (the forwarder)
- `tools/runtime/driver.sh`, `tools/runtime/kit.toml`, `tools/runtime/README.md`
- `tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`,
  `tools/unattended/adopt-unattended.sh`, `tools/unattended/kit.toml`, `tools/unattended/README.md`,
  `tools/unattended/.unattended.conf.example`
- `tools/unattended/SKILL.template.md`, `tools/unattended/STOPS.template.md`,
  `tools/unattended/VERBS.template.md`, `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/unattended.test.sh`, `tools/unattended/check-unattended.test.sh`,
  `tools/unattended/adopt-unattended.test.sh`, `tools/unattended/cross-component.test.sh`
- `tools/govkit/steps/unattended_dissolve.py`, `tools/govkit/selftest.py`
- `tools/run-gates/selftest-budgets.txt`, `tools/run-gates/selftest-pooled-evidence.txt`
- `tools/policy/legacy-homes.txt` (regenerated)
- `.unattended.conf`, `.memory-tree.conf` (`ARMS_FLOORS`, §7)
- `help/runtime.md`

The renders are copies, never edits: `.claude/settings.json` and `.claude/hook-packs.json` from the
fragments by settings-merge, `.claude/skills/unattended/SKILL.md` from the skill template, and
`memory/guides/UNATTENDED-STOPS.md`, `memory/guides/UNATTENDED-VERBS.md` and
`memory/guides/UNATTENDED-PROTOCOL.md` from their templates.

### Alternatives rejected

- **The whole kit moved under `tools/loop/` and `tools/runtime/` now.** §8 F1.
- **Keeping `RESUME_SCHEDULE_DELAY` and `RESUME_SCHEDULE_LIMIT` as conf keys.** §8 F2.
- **Each moved pack finding the driver at `__dirname/../unattended/`.** §8 F3.
- **No forwarder at the old tick path.** It breaks every registered node tick at the first update,
  which the clause keeps (§8 F4).

## 5. Production-readiness checklist

- security — no file under either kit builds a skip-permissions argv (AC6); a held run's restart
  launches through `launch_act` under `--permission-mode auto`, where a durable task launched whatever
  its harness gave it; the restart prompt carries no free-text hold reason, as today.
- perf / scale — the moved packs spawn the driver only where a run lease exists, as today, plus one
  `driver.sh` resolution; the tick adds one record read per HELD run per tick.
- error / empty / loading states — an unresolvable driver directory is exit 2 naming the three places
  looked, which the dispatcher treats as a failed pack under `runtime.hook-failure`; a HELD record
  whose `resume-owed` cannot be read is `skip · HELD · resume-owed unreadable`, launching nothing.
- observability — every tick decision on a HELD run is one line; each restart is an attempt line in the
  slug's sidecar.
- risks — a durable task an adopter's agent filed before U3 can still fire once beside the tick's
  restart; the driver's `--scheduled` refusals (`unattended.sh:9177-9182`) refuse the second resume of
  one hold, and U3 names the tasks to delete.
- testing — the fixture cases under AC1 to AC11 and the arms in §7.
- migration — §4 Migration; three upgrade steps.
- user docs — `help/runtime.md`, S11.

## 6. Acceptance criteria

The fixture is `python unattended_dissolve.py fixture <case> <dir>`, which plants a scratch adopter
tree under `%TEMP%` with a short name at this base's image: the unattended kit as shipped, a
`.unattended.conf` carrying the five retired keys, per-fragment settings entries for the three hooks,
and for the HELD cases a tracked run record whose `resume-owed` the case sets, with a stub `claude` on
`PATH` that records its argv.

- **AC1** — When `git ls-files tools/unattended | grep -cE '(gate-guard|stop-guard|stall-recorder|run-lease)'`
  runs it prints 0, and `python settings-merge.py --resolve-pack` over each moved fragment prints
  `owner=runtime` and a `hook_path` under `{kit}/runtime/`; the budget rows for the four moved suites
  read `runtime …` with argv under `{prefix}/runtime/`.
  Red when: a hook file stays under `tools/unattended/`, or a fragment still names `{kit}/unattended/`.
- **AC2** — When `grep -cE 'unattended/(gate-guard|stop-guard|stall-recorder)\.js' .claude/settings.json`
  runs after the re-render it prints 0, and `hook-packs.json` lists the three packs with commands under
  `runtime/`, the `PreToolUse`, `Stop` and `StopFailure` entries each naming `dispatch.js`.
  Red when: a per-fragment entry for a moved hook survives the render.
- **AC3** — When `bash driver.sh --dir` runs in the `pre-image` fixture it prints the unattended kit's
  directory; in `renamed-home`, whose receipt names the kit at another path, it prints that path; with
  the kit absent it exits 2 naming the receipt, the probe and the parent probe.
  Red when: it prints a guessed prefix, or a renamed home resolves to the probe path.
- **AC4** — When a `Stop` payload is piped to `node stop-guard.js` in the `stop-lease` fixture, which
  holds an open run lease and a stub driver at the resolved directory, it blocks with a reason naming
  the resolved directory's `unattended.sh --plan <slug>`, and the stub records one `--liveness` call.
  Red when: the pack spawns `unattended.sh` from its own directory.
- **AC5** — When `bash tools/unattended/resume-tick.sh --repo <dir> --dry-run` and the runtime copy
  run over one fixture, their stdout is byte-identical, and the forwarder is one command beyond its
  header.
  Red when: the old path runs no tick, or runs a second copy of the tick's logic.
- **AC6** — When `git grep -c -- '--dangerously-skip-permissions' -- tools/unattended '*resume-tick.sh'`
  runs it prints nothing, and the stub's recorded argv in AC7 carries `--permission-mode auto`.
  Red when: any launch line under the two kits carries the skip flag.
- **AC7** — When the tick runs over `held-past` it prints `restart · HELD · fire <utc> passed`, the stub
  records one launch whose prompt is the three lines `unattended.sh --restart-prompt <slug>` prints, and
  a second tick prints `skip · HELD · restart launched`; over `held-future` it prints
  `skip · HELD · fire <utc>` and over `held-owner` `skip · HELD · no restart owed (owner)`, launching
  nothing in either.
  Red when: a second tick launches again for one `held-at`, or a hold owing nothing is launched.
- **AC8** — When `git grep -nE 'RESUME_SCHEDULE' -- tools .claude memory/guides .unattended.conf`
  runs, every hit is in `unattended_dissolve.py`, a `[[upgrade]]` row's `surfaces`, the inert
  fixture lines of the unattended-build suite or the `govkit.py` comment S7 names; and `bash unattended.sh
  --hold` in `held-past`'s run with a `probe api` condition prints `the node tick launches it` and no
  line naming a delete or create tool.
  Red when: the driver, the kit gate, the adopter, the skill or a guide still reads or prints a key.
- **AC9** — When `grep -c 'run <slug>' SKILL.md` runs over the re-rendered
  `.claude/skills/unattended/SKILL.md` it prints at least 2, and `grep -c 'unattended-build.js'` over
  it prints 0.
  Red when: the skill still drives the harness itself.
- **AC10** — When `python unattended_dissolve.py <step> up <dir> tools` runs over the `pre-image`
  fixture for U1, U2 and U3 in turn, each step's `witness` exits 0 after its up and 1 before it, and
  `down` restores every path to its before-image bytes, `git -C <dir> diff --exit-code` exiting 0.
  Red when: a witness passes on the pre-image, or a down leaves a diff.
- **AC11** — When `grep -nE 'driver.sh|gov-resume-tick|RESUME_SCHEDULE|run <slug>' runtime.md` runs
  over the help page, each term is named.
  Red when: the page omits one.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended skill size` · `unattended protocol size` · `python resolver (behaviour + inline parity + idiom ban)` · `policy fixtures` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `check-wiring self-test` · `lexicon naming predicates` · `pre-push run-log line` · `run-gates turnstile` · `run-gates gov canary` · `run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `measure-legs selftest` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The unattended kit's self-test suites, and the four this unit moves into the runtime kit, are waived
for this build's landing (README rule 8); their clean reading is owed with PLAY-dClosedLoop-15. The
arms below are declared for the main loop's close.

New arm: tools/runtime/resume-tick.test.sh · covers AC3 AC5 AC6 AC7 · each HELD case staged against a tick with `run_held_restart` removed, a forwarder that runs nothing, and a `driver.sh` whose receipt step is removed · none
New arm: tools/govkit/selftest.py · covers AC10 · each step's witness run on the pre-image, and a down staged to skip one path · none
New arm: tools/runtime/gate-guard.test.sh · covers none · moved whole from the unattended kit, its staged breaks unchanged · none
New arm: tools/runtime/stop-guard.test.sh · covers AC4 · moved whole, plus a case staging a driver beside the pack and none at the resolved directory · none
New arm: tools/runtime/stall-recorder.test.sh · covers none · moved whole, its staged breaks unchanged · none
New arm: tools/unattended/check-unattended.test.sh · covers AC8 · check 46's key arms deleted with the keys · `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`, `tools/unattended/unattended.sh` and `tools/unattended/adopt-unattended.sh` lowered to `check-arms.py --emit-floors`'s reading, with this unit's id as the comment

The branches that go grade keys this unit retires, so their condition does not survive; that is why
they lower a floor with a stated reason rather than taking a `refusal-retirements.txt` row, whose R3
requires the condition to survive elsewhere.

## 8. Open questions

- **F1 — What leaves `tools/unattended/` in this unit?** (a) The three hooks, their module and suites,
  and `resume-tick.sh`, into the runtime kit, the driver, its checkers, its guides and the skill
  staying as the `/unattended` shim's home until dConvergedCharter; (b) the whole kit, the driver and
  checkers into `tools/loop/`, about 129 tracked files naming `tools/unattended` re-pointed and the kit
  id retired; (c) nothing moved, only the wiring changed. The clause keeps `/unattended` "until
  dConvergedCharter retires it", and v2's night pass gives the driver's functions their homes in other
  units (the position engine, the owner's controls, `next`) and names three parts with no home at all
  (night-pass `[p1-unattended]`), so the kit cannot empty before then; (c) leaves "its supervisor seam
  taken" and "its hooks repacked" into the runtime kit undone. Rung 1, v2 answers it. RESOLVED (agent,
  2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — How much of `RESUME_SCHEDULE_*` retires, and what restarts a hold?** (a) All five keys, the
  delay and limit kept as kit constants, the node tick launching each owed restart once; (b) the switch
  and carrier pair only, `RESUME_SCHEDULE_DELAY` and `RESUME_SCHEDULE_LIMIT` kept as conf keys; (c) all
  five, and no restart at all, a hold waiting for a person. Layer-runtime `[supervise]` retires "the
  desktop durable-restart task (`RESUME_SCHEDULE_*`)" whole and makes the node tick the restarter;
  (b) keeps two keys named for a task that no longer exists; (c) breaks the owner's TOOL-dDerivedDocket-5
  ruling that auto-resume ships on. Rung 3 between (a) and (b) after rung 1 removes (c): (a) meets
  every criterion with the fewer open names. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none
  · relaxes: none
- **F3 — How does a moved file find the driver?** (a) One `driver.sh` carrying the canonical
  `resolve_kit_dir` inline, receipt then probe, shared by the packs and the tick; (b) each JS pack
  joining `__dirname` with `../unattended/`, and the tick likewise; (c) settings-merge rendering the
  driver's path into each pack's command. (b) fails an adopter whose receipt homes the kit elsewhere,
  the case the resolver exists for; (c) leaves the tick, which no settings file renders, on (b). Rung 3,
  the most capable option, reusing the seam M5 found. RESOLVED (agent, 2026-10-26, delegated): (a).
  widens: none · relaxes: none
- **F4 — What happens to the old tick path?** (a) A forwarder kept for `install.deprecation-window`
  releases, the window member U2 declares; (b) the tick left at its old path; (c) moved with no
  forwarder. (b) does not take the seam into the runtime kit; (c) breaks every hand-registered
  `gov-resume-tick` task, which the clause keeps. Rung 1, the clause answers it. RESOLVED (agent,
  2026-10-26, delegated): (a). widens: none · relaxes: none
- **F5 — Does the `/unattended` stand-in take a `[[stand-in]]` row?** (a) No: TOOL-dDeclaredLoop-13 S8
  reds a stand-in row naming no row item, and `/unattended` is a skill, not a loop item; the hand-over
  is §3's external edge to dConvergedCharter. (b) A row naming a synthetic item. (b) fails S8's own
  check. Rung 1, the parent spec answers it. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none
  · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended: the moved files themselves, whose behaviour is unchanged; the canonical
`resolve_kit_dir` (`tools/lib/resolve_kit_dir.py`), which `reuse_lookup.py` ranked a SEAM with 75
installs and which every shell consumer already carries inline under the parity table, as `driver.sh`
and the forwarder do; govkit's `remove_wired_fragments` (`tools/govkit/govkit.py:6180`) and
`run_fragment_merges` (`:6109`) for U1; TOOL-dSafePassage-1's step grammar and before-image helpers for
all three steps; the tick's attempt sidecar and `RESUME_ATTEMPTS` cap for the one-shot HELD restart; and
the driver's own fire computation (`resolve_resume_fire`, `unattended.sh:1204-1219`), kept whole. The
probe `python tools/codebase-map/reuse_lookup.py "move a kit's hook and its scheduled tick into another
kit with an upgrade step for adopters"` also ranked `read_tick_registration`
(`lib-unattended.sh:674`, kept, name-matched) and `derive_kit_paths`, which renders kit paths into
documents and fits none of the four lookups here. Scout B's row cites `remove_wired_fragments` at
`:6180`, `read_tick_registration` at `:674`, the conf example at `:137-156` and legacy homes at
`:98-101`; the first three hold at this base, and legacy homes holds the rows at `:99-103`.

Recall terms used: `python tools/memory-recall/query.py "how is the unattended kit dissolved into the
runtime kit with its hooks repacked and the durable resume schedule retired" --terms "unattended kit
dissolve resume-tick gov-resume-tick RESUME_SCHEDULE durable restart hook fragment dispatcher upgrade
step shim"`
