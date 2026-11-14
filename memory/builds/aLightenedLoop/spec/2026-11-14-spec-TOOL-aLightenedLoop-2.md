# TOOL-aLightenedLoop-2 — the idle-wake tick: one cheap `--wake` verb that ends a healthy turn, and a longer cadence while a registered task is open

**Status:** INPROGRESS · rev-1 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md](../build/2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md) | research | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 |
| [2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md) | research | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 |

<!-- /gen:spec-records -->

## 1. Goal

Each idle-wake tick today runs `--resume` and then `--audit`: about 12 s and 72 s, over 666 ticks in <!-- PINNED 2026-11-14 -->
dSafePassage that averaged 132 s of main-loop time each. This unit adds one driver verb, `--wake`, <!-- PINNED 2026-11-14 -->
that answers in one line whether those two acts would find anything to do. On `HEALTHY` the model
ends its turn, and on `FULL` it runs the pair exactly as today. The same line names the cadence the
idle-wake should run at, which is longer while a registered task is open. No existing verb's
verdict, refusal text or output byte moves.

## 2. Scope (IN)

- **S1** — The verb. `tools/unattended/unattended.sh` gains `--wake <slug> --keepalive-id <id>`,
  a function `print_wake`, and one line in each of four places: the header docstring, `VERBS_SLUG`,
  `VERB_REQUIRES` and the dispatch `case`. The verb prints exactly one stdout line, in §4's grammar,
  and writes nothing to the record or the worktree. Its claim read refreshes only the private claim
  cache, as `--resume`'s does. Observed by AC1, AC2 and AC3.
- **S2** — The shared predicates. Three expressions that `--wake` and an existing verb must both
  answer become one function or one counter each: `check_lease_current`, taken from `verb_resume`'s
  holder row; `check_tree_progressing`, taken from `print_audit`'s unit verdict; and `TA_OPEN` with
  `TA_STALLED`, set by `print_task_audit`. Every existing verb prints the same bytes afterwards.
  Observed by AC4 and AC8.
- **S3** — The cadence key. `KEEPALIVE_TRACKED_INTERVAL` is an optional conf key. It is declared
  blank in `tools/unattended/.unattended.conf.example`, listed in `tools/unattended/kit.toml`'s
  `optional_keys`, initialised blank on the driver's init block, and given a row in the protocol's
  §8 key table. This repo's `.unattended.conf` sets it to
  `every 30 minutes (cron 7-59/30 * * * *)`. Because the kickoff manifest watches that conf, the
  manifest's `last-audit` is re-stamped. Observed by AC3 and AC6.
- **S4** — The carriers. The Skill's "Before any path" paragraph, the verbs carrier's `--wake` entry
  and its idle-wake steps, protocol §5's sentence on the idle-wake's prompt, and the unattended
  feature dossier's matching sentence all say: run `--wake`, end the turn on `HEALTHY`, run the pair
  on `FULL`, and replace the job when the line's cadence differs from the job's. The three rendered
  copies are re-rendered from their templates. Observed by AC6.
- **S5** — The help page. A new `help/idle-wake.md` documents `--wake` and its cadence field, and
  carries the docs leg's anchor for `verb:unattended.sh:--wake`. `help/README.md` links it.
  Observed by AC7.
- **S6** — The size rows. The Skill's and the protocol's rows in `tools/template-size-limits.txt`
  rise to their measured renders, on that file's four terms, with this unit's row in
  `memory/DECISIONS.md`. The verbs carrier stays under the hygiene guide cap. Observed by AC9.
- **S7** — The suite. `tools/unattended/unattended.test.sh` gains a parity-table row for `--wake`
  and the arms §7 declares. NOT OBSERVED by a criterion: a pass runs no suite. The main loop observes
  each `New arm:` line RED and then GREEN at the close.

## 3. Non-goals (OUT)

- Any change to what `--resume`, `--audit`, `--liveness`, `--status`, `--register-task` or
  `--release-task` decide, print or write. `--wake` never takes the pair's place on a `FULL` verdict.
- Hang detection. `UNIT_STALL_BOUND`, `TASK_STALL_BOUND` and `RESUME_STALE_BOUND` keep their values,
  and the stop-guard, the stall-recorder and the resume tick are untouched. The stop-guard's
  liveness cache is TOOL-aLightenedLoop-5's.
- Scheduling. The driver still schedules and reaps nothing (its header, "It RECORDS a keepalive id",
  `tools/unattended/unattended.sh@95b8f8404cc3:50-53`). The agent replaces the job, through the
  existing `--resume --keepalive-id <new> --replaces <old>` row.
- A `FULL` verdict that is always right. `--wake` tests sufficient conditions, so it may answer
  `FULL` where the pair would then find nothing, which costs time and never a verdict (§4).
- A new numbered refusal. `--wake` reaches only the existing checks 10 and 112 and the slug refusal.
- Any kit version. The lander mints them.
- `--dispatch`, `run_spec_token_check` and `tools/workflows/unattended-unit.js`, which are
  TOOL-aLightenedLoop-3's. Any path under `memory/builds/dDeclaredLoop/`.

### Edges

none

## 4. Design

### Evidence

Read at `846d51d39`, the base. Blob ids are of that commit.

- The idle-wake's acts are written in three carriers:
  `tools/unattended/SKILL.template.md@7d1f6cf0121d:17-21`,
  `tools/unattended/VERBS.template.md@d9fea17448ac:444-470` and
  `tools/unattended/PROTOCOL.template.md@8c07e396aad2:391`. The feature dossier repeats the
  sentence at `memory/map/features/unattended.md@9ff4d82868af:84`.
- The holder's `--resume` writes nothing, and reaches no refusal, only when these hold
  (`tools/unattended/unattended.sh@95b8f8404cc3:9335-9566`). The record is not `abandoned` (check
  106, `:9343-9352`). The pinned asks have not moved (check 73, `check_asks_pinned` at `:5746`). The
  worktree is on the run branch (check 58, `check_holder_worktree` at `:9303`). The keepalive is the
  lease's, with `lease-utc` set and the session and pid matching the harness (`:9507`, `:9534`).
  Inside that row it also reads the claim when `RUN_CLAIMS` is `on`, through
  `check_claim_writable ... holder` (`:9531`, defined at `:2457`). That function returns 2 when the
  claim is this run's and not yet due, 0 when a write is due, and 1 with check 108 when another
  session holds the claim.
  Last, the row runs `run_orphan_reap` (`:9562`), which acts only on ledger lines that
  `derive_proc_state` (`:1987`) classes `orphan`.
- `--resume` derives the phase with `read_derived_phase`, which can ask the remote for its tip. For a
  recorded phase other than `LANDING` and a hand-off `HELD`, the derived phase is the recorded one
  (`:1653-1700`). So `--wake` reads `read_recorded_phase` (`:1840`), which is offline, and answers
  `FULL` on `LANDING`, `HELD`, any terminal phase, or none.
- `--audit` reads its clocks once through `read_tree_clocks` (`:8597`). It grades every open unit
  STALLED exactly when the newest commit and the newest write are both older than
  `UNIT_STALL_BOUND` (`:8691`). The clocks belong to the tree and not to the unit (`:8621-8623`), so
  "the tree is progressing" makes every open unit read `PROGRESSING` without reading which units are
  open. The registered tasks are graded by `print_task_audit` (`:8731`), and a dead probe sets
  `TA_DEAD` there.
- `read_claims` performs one bounded fetch (`:2332`). The `quiet` policy prints nothing, the
  policy `--beat` uses (`:2683`).
- The driver sources the whole conf (`:748`), so `KEEPALIVE_INTERVAL` is readable even though the
  init block at `:685-689` does not declare it.
- The stop-guard allows a turn to end while the harness lists a background task
  (`tools/unattended/stop-guard.js@241f63c7925b:33`). With none listed, it still blocks `run-open`.
  The turn `--wake` ends is graded there exactly as a tick's is today.
- Every verb but `--version` and `--plan` is journaled
  (`tools/unattended/VERBS.template.md@d9fea17448ac:474-476`). A `--wake` call is a journal line,
  so the journal-gap reading of a stalled run survives the pair no longer running on every tick.
- Probed on 2026-11-14 with the base driver, in the probe fixture below and in a clone of this
  tree. A current lease and a fresh commit leave `--resume --keepalive-id k1` writing nothing. With
  `CLAUDE_PID` exported by the harness, it re-records the lease and stages the record. That is the
  `lease` reason, and it is why every command below unsets the variable. A staged ledger line
  (AC2's orphan case) makes `--status` print `orphans 1`. In the clone, `--resume` took 30.7 s and
  `--audit` 13.9 s (PINNED, 2026-11-14, node `a`, beside a live run).

### Data model

The one stdout line:

```text
unattended-wake: <slug> · HEALTHY · tasks <n> open · cadence <cadence>
unattended-wake: <slug> · FULL · <reason> · tasks <n> open · cadence <cadence>
```

- `<n>` is the number of open registered tasks, which `print_task_audit` counts. It reads `unknown`
  when that function set `TA_DEAD`.
- `<cadence>` is `KEEPALIVE_TRACKED_INTERVAL` when `<n>` is at least 1 and that key is not blank.
  Otherwise it is `KEEPALIVE_INTERVAL`, or `undeclared` when that key is blank too. A `tasks unknown`
  line takes the second branch, the shorter cadence.
- Exit 0 for both verdicts. Exit 1 only for the slug refusal, check 112 (no `--keepalive-id`) and
  check 10 (no run-state file). Exit 2 for a malformed `TASK_STALL_BOUND`, through `read_bound_key`
  (`tools/unattended/lib-unattended.sh@a3e03db6b9f0:236`), as `--audit` does.

`<reason>` is the first row below that holds, in the order of `verb_resume`'s own rows. Each row
names what the pair then does, so a `FULL` line never hides a verdict:

| `<reason>` | holds when | the pair then |
|---|---|---|
| `phase <p>` | the recorded phase is empty (`absent`), terminal, `HELD` or `LANDING` | takes `--resume`'s phase rows |
| `abandoned` | the record carries an `abandoned` fact | refuses with check 106 |
| `asks moved` | `check_asks_moved` returns 0 | refuses with check 73 |
| `worktree` | `resolve_holder_worktree` returns 1 | refuses with check 58 |
| `holder` | `--keepalive-id` is not the record's `keepalive` fact | takes the take-over or restart rows |
| `lease` | `check_lease_current` returns 1 | re-records the lease |
| `claims unread` | `RUN_CLAIMS` is `on` and `read_claims quiet` returns 1 | announces the failed read |
| `claim` | `RUN_CLAIMS` is `on` and `check_claim_writable` in holder mode returns other than 2 | writes the claim, or refuses with check 108 |
| `orphans` | a ledger line from `read_proc_ledger` derives `orphan` | reaps it |
| `clock probe` | `read_tree_clocks` set `TC_DEAD` | `--audit` refuses with check 51 |
| `tree idle` | `check_tree_progressing` returns 1 | `--audit` prints `STALLED` for any open unit |
| `task probe` | `TA_DEAD` is set | `--audit` refuses with check 51 |
| `task stalled` | `TA_STALLED` is above 0 | `--audit` prints the task's `STALLED` line |

`HEALTHY` is the case where no row holds. The `claim` test runs `check_claim_writable` in a subshell
with its output discarded, so its check 108 never prints from `--wake`. A `holder` row reached with
`ls_sid` empty passes `absent`, exactly as `:9531` does.

### The extractions (S2)

- `check_lease_current` takes the lease-utc, session and pid facts. It returns 0 when `lease-utc` is
  set, the session equals `${CLAUDE_CODE_SESSION_ID:-absent}` and the pid equals
  `${CLAUDE_PID:-absent}`. `verb_resume`'s test at `:9534` becomes `! check_lease_current ...`.
- `check_tree_progressing` takes now, the commit clock and the write clock, and returns 1 under
  `:8691`'s condition. `print_audit` calls it in place of that condition.
- `print_task_audit` resets `TA_OPEN` and `TA_STALLED` to 0, and adds 1 to them beside its `n`
  (`:8753`) and its `STALLED` branch. It prints nothing new.

`print_wake` reads `TASK_STALL_BOUND` as `print_audit` does. It calls `print_task_audit` with its
stdout sent to `/dev/null`, a redirection rather than a substitution, so `TA_*` survive in this
shell. It reads `read_tree_clocks` only when no earlier row held. It spawns nothing per task or per
unit, and it makes one bounded fetch only when `RUN_CLAIMS` is `on`.

### The cadence switch (S3, S4)

The driver cannot reach the scheduler, so it says which cadence is due and the agent acts on that.
The verbs carrier's idle-wake steps gain one rule. When the `cadence` field differs from the cadence
of the job this session holds, `KEEPALIVE_DELETE` that job, `KEEPALIVE_CREATE` a new one at the
printed cadence, then run `--resume <slug> --keepalive-id <new> --replaces <old>`. That is the
existing holder replacement row (`:9603`), so the record names the live job. The main loop runs
`--wake` right after its own `--register-task` and `--release-task`, so the switch follows at once.
A task that a builder registers is seen at the main loop's next wake.

The repo's value is 30 minutes. That is the beat cadence a build brief asks a tracked task for, the
one `TASK_STALL_BOUND`'s comment names (`tools/unattended/.unattended.conf.example@19d8384985d9:89-92`):
a tick between two beats cannot see a new beat. The offset `7` keeps it off the base job's minute
`3`. While a task is open, a unit's `STALLED` line can arrive up to 30 minutes after its bound
instead of 10. §5 states that cost.

### The carriers' text

- Skill, "Before any path": "Each tick runs `unattended.sh --wake <slug> --keepalive-id <id>`.
  `HEALTHY` ends the turn. `FULL` runs `unattended.sh --resume <slug> --keepalive-id <id>`, then
  `unattended.sh --audit <slug>`. A `cadence` other than your job's replaces the job, as the verbs
  file says." The rest of the paragraph stays.
- Verbs carrier: a `- `--wake` — ` entry after `--audit`'s, giving §4's grammar, the reason table in
  one sentence per reason group, and the sufficiency rule. Step 2 of "Before any path — the
  idle-wake" becomes three acts. `--wake` is first. `--resume` and then `--audit` run only on
  `FULL`. The cadence rule follows them. Every existing sentence about acting on `STALLED` stays.
- Protocol §5, line 391: "Its prompt is `--wake --keepalive-id` with its own id, and
  `--resume --keepalive-id` then `--audit` on `FULL`." §8 gains the row
  `| `KEEPALIVE_TRACKED_INTERVAL` | the idle-wake's cadence while a registered task is open, printed
  by `--wake`. OPTIONAL: blank keeps `KEEPALIVE_INTERVAL` |`.
- Dossier, line 84: the prompt runs `--wake`, and `--resume` and `--audit` on `FULL`.

The three renders are `.claude/skills/unattended/SKILL.md`, `memory/guides/UNATTENDED-VERBS.md`
and `memory/guides/UNATTENDED-PROTOCOL.md`, all written by `bash tools/unattended/adopt-unattended.sh`.

### Byte budget

| file | at base, CR-stripped | ceiling | how this unit pays |
|---|---|---|---|
| `.claude/skills/unattended/SKILL.md` | 10580 | 10580, row at `tools/template-size-limits.txt@1e83100dad69:188` | raised to the measured render, no headroom |
| `memory/guides/UNATTENDED-PROTOCOL.md` | 68022 | 68022, row at `:166` | raised to the measured render, no headroom |
| `memory/guides/UNATTENDED-VERBS.md` | 96906 bytes, 1106 lines | 98304 bytes, 1200 lines, `GUIDE_CAP_BYTES` at `tools/memory-tree/check-memory-hygiene.sh@f064ddabb88e:152` | fits, and must, because the row is not this run's to raise | <!-- PINNED 2026-11-14 -->

The figures are PINNED, measured 2026-11-14. The 1398 bytes of verbs-carrier headroom are shared
with any sibling unit that edits that carrier, so this unit spends at most 900 of them.

### Why a page and a parity row are owed

- `memory/project/docs-undocumented.txt@6491053ec7ac:2-5` is shrink-only, and the docs leg reds a
  member with no anchor and no row. A new verb is a new member of the verb class
  (`tools/govkit/step_gate.py@11b2aceb9536:333`), so it needs a page. The conf key is not a member,
  because the conf class holds only required keys and `defaults` (`:312-321`).
- The suite's parity table refuses a verb with no row
  (`tools/unattended/unattended.test.sh@0d9cd1632c89:2505`). The kit gate's check 26 refuses a verb
  that is absent from the header, the verbs carrier or the Skill
  (`tools/unattended/check-unattended.sh@c43efbd9155f:4894-4950`), and the flag arm refuses one that
  no suite line names.

### The probe fixture

The builder saves this as `wakefix.sh` in its scratch directory and runs it as
`bash wakefix.sh <worktree> <F>`. `<F>` is a short path under `%TEMP%`, such as `$TEMP/wkfx`. It
builds the fixture repository with the base driver in `u0/` and the built driver in `u/`, a
holder's record leased to session `s1` with keepalive `k1`, and one open dispatched unit. It ran
green against the base driver on 2026-11-14.

```bash
set -eu
W=$1; F=$2; B=memory/builds/tWake
rm -rf "$F" "$F.beat" "$F.bare"; mkdir -p "$F/u0" "$F/u" "$F/$B/spec" "$F.beat"
for f in unattended.sh lib-unattended.sh; do
  git -C "$W" show "846d51d39:tools/unattended/$f" > "$F/u0/$f"
  cp "$W/tools/unattended/$f" "$F/u/$f"
done
printf 'MEMORY_ROOT=memory\nKEEPALIVE_INTERVAL="every 10 minutes"\nUNIT_STALL_BOUND="1800"\nTASK_STALL_BOUND="5400"\nRESUME_STALE_BOUND="5400"\n' > "$F/.unattended.conf"
printf '# tWake\n' > "$F/$B/README.md"
printf '# WAKE-tWake-1 — u\n\n**Status:** INPROGRESS · rev-1 · 2026-11-01 · node a · Tier-2 · base 0123abcd\n\n## 2. Scope (IN)\n\n- s\n\n## 6. Acceptance criteria\n\n- AC1 observable.\n\n## 7. Gates\n\n- g\n\n## 8. Open questions\n\nnone\n' > "$F/$B/spec/2026-11-01-spec-WAKE-tWake-1.md"
cd "$F"; git init -q -b main .; git config user.email t@t.test; git config user.name t; git config core.autocrlf false
git add -A >/dev/null; git commit -q -m base --no-verify
N=$(date -u +%Y-%m-%dT%H:%M:%SZ); H=$(git rev-parse HEAD)
printf '# tWake\n\n## Run facts\nphase: BUILDING\nwitness: %s\nkeepalive: k1\nsession: s1\npid: absent\nlease-utc: %s\nrun-branch: refs/heads/main\n\n## Parked\n\n%s dispatch · item %s WAKE-tWake-1 · reason work/one.txt\n' "$H" "$N" "$N" "$H" > "$B/RUN.md"
git add -A >/dev/null; git commit -q -m record --no-verify
echo beat > "$F.beat/beat"
```

In §6, each criterion starts from a fresh fixture, and these names stand:

- `run` is `env -u CLAUDE_PID -u GOV_REMOTE -u GOV_DEFAULT_BRANCH CLAUDE_CODE_SESSION_ID=s1 bash u/unattended.sh "$@" 2>/dev/null`,
  called from `<F>`. `run0` is the same with `u0/`.
- `<reg>` is `run --register-task tWake --task wf --heartbeat "$F.beat/beat"`.
- `<age>` is `sed -i 's/^UNIT_STALL_BOUND=.*/UNIT_STALL_BOUND="60"/; s/^TASK_STALL_BOUND=.*/TASK_STALL_BOUND="60"/' .unattended.conf`,
  then `git add -A`, then `GIT_COMMITTER_DATE="@$(( $(date +%s) - 3600 )) +0000" git commit -q -m aged --no-verify`.
  Together they leave a clean tree whose newest commit is an hour old.
- `<stale-beat>` is `touch -d "@$(( $(date +%s) - 3600 ))" "$F.beat/beat"`.
- `<orphan>` stages one ledger line that `derive_proc_state` classes `orphan`. It runs
  `sleep 600 & P=$!` and `D=$(bash -c 'echo $$')`, then writes `$P (sleep) S 1 2 … 25` to
  `$F.proc/$P/stat`. It appends `$P 19 $D - k1 2026-11-14T00:00:00Z sleep 600` to
  `.git/unattended/tWake.procs`, and every `run` in that criterion is prefixed with
  `UNATTENDED_PROCFS="$F.proc"` (the driver's override, `:925`).
- `<remote>` is `git init -q --bare "$F.bare" && git remote add origin "$F.bare" && git push -q origin main`,
  then `echo 'RUN_CLAIMS="on"' >> .unattended.conf`. The remote must be the fixture's own bare
  repository. A clone's default origin is the source repository, so a claim written there lands in
  the real repository's `refs/gov/runs/`. This spec's own probe did that, and removed the ref.
- `<rec>` is the fixture's run-state file, `memory/builds/tWake/RUN.md`, and `<page>` is the new
  help page, `help/idle-wake.md`.
- `<norm>` is `sed -E 's/[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z/<utc>/g; s/[0-9]+s/<n>s/g; s/^last-move: [0-9]+$/last-move: <n>/'`.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/kit.toml`
- `.unattended.conf`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/features/unattended.md`
- `tools/template-size-limits.txt`
- `memory/DECISIONS.md`
- `help/idle-wake.md`
- `help/README.md`

`memory/guides/SESSION-KICKOFF.md` is touched for its `last-audit` re-stamp alone. Its `watch:` list
names `.unattended.conf` (`memory/guides/SESSION-KICKOFF.md@c353dcd9417c:7`).

### Alternatives rejected

- **Name the verb `--tick`, the brief's word.** "Tick" already names the resume tick:
  `resume-tick.sh`, and `--beat`, "the tick's heartbeat"
  (`tools/unattended/unattended.sh@95b8f8404cc3:36`). `--wake` names the idle-wake that runs it.
- **A flag on `--resume` instead of a verb.** The brief asks for one verb. A flag would also leave
  `--audit`, the costly half, outside it, and make `--resume` mean two things.
- **Skip the claim read and route `FULL` once a quarter of `RESUME_STALE_BOUND` has passed.** It
  saves one bounded fetch, but it delays check 108 on a lost claim from one tick to as much as 22
  minutes. The brief forbids moving a verdict, and a delayed refusal is one.
- **Compute which units are open, so an idle tree with no open unit reads `HEALTHY`.** That costs
  `load_spec_facts` and `read_open_passes` on every tick. The idle-tree case is rare and costs only a
  `FULL`, so the conservative rule stays.
- **Render the tracked cadence into the Skill as a required placeholder.** Every adopter's conf
  would then need the key, which breaks an install that lacks it, and the charter's `[core]` asks
  for an additive change with a default. Read at run time and blank by default, the key changes
  nothing for an adopter that never sets it.
- **A fixed multiple of `KEEPALIVE_INTERVAL` written in prose.** That value is prose already, so
  "three times every 10 minutes (cron …)" is not a schedule an agent can copy, and no adopter could
  turn it off.

## 5. Production-readiness checklist

- security — No new write path. `--wake` writes nothing, and the claim fetch is `--resume`'s own,
  into the same private ref namespace. The printed cadence is the conf's own text, on one line.
- perf / scale — `--wake` is a driver launch, two fact reads, one `git log`, one dirty-path scan,
  one awk over the task registry and, under `RUN_CLAIMS`, one bounded fetch. AC5 measures it against
  the pair.
- error / empty / loading states — No run-state file is check 10, as `--audit` gives before
  `--preflight`, and the carriers keep that expected-refusal sentence. A dead probe answers `FULL`
  and never `HEALTHY`.
- observability — The reason names the first condition that failed, and every `--wake` call is a
  journal line.
- risks — While a task is open the job runs every 30 minutes, so a `STALLED` unit or task can be
  reported up to 20 minutes later than today. The bounds do not move, and the stop-guard and resume
  tick see stalls of the session as before. The job replacement re-records the lease twice per task
  lifetime. The census arm `FA9 AC15 the driver's census holds`
  (`tools/unattended/unattended.test.sh@0d9cd1632c89:3264`) is red at the base: the driver has 319
  `fail <n> "` sites and the arm allows 318. This unit adds no site.
- testing — AC1 to AC9 run in the probe fixture, in a clone, or as greps. §7 declares the suite arms.
- migration — None. A conf without the key prints `KEEPALIVE_INTERVAL` as its cadence, so the job is
  never replaced and the tick runs as now, with `--wake` first.
- user docs — `help/idle-wake.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `<reg>` runs in a fresh fixture and then `run --wake tWake --keepalive-id k1`, it
  exits 0 and prints exactly `unattended-wake: tWake · HEALTHY · tasks 1 open · cadence every 10 minutes`.
  `git status --porcelain` prints nothing, and `git hash-object <rec>` gives the
  same value before and after.
  Red when: a healthy record reads `FULL`, the line is not one line, or the verb writes the record.
- **AC2** — When each staged break below is applied to a fresh fixture after `<reg>`, then
  `run --wake tWake --keepalive-id k1` exits 0 and prints a line holding `· FULL · <reason> ·`, with
  the reason given:
  `phase: HELD` replacing the phase fact and committed gives `phase HELD`;
  an `abandoned: x` fact gives `abandoned`; an `asks: X-1` fact gives `asks moved`;
  `run-branch: refs/heads/other` gives `worktree`; `--keepalive-id k2` in place of `k1` gives
  `holder`; `pid: 999` gives `lease`; `echo 'RUN_CLAIMS="on"' >> .unattended.conf` with no remote
  gives `claims unread`; `<remote>` gives `claim`, and after `run --resume tWake --keepalive-id k1`
  the same wake gives `HEALTHY`; `<orphan>` gives `orphans`; `<age>` gives `tree idle`; and
  `<stale-beat>` with `TASK_STALL_BOUND="60"` gives `task stalled`. Each break that edits the record
  commits it with `git commit -qam b --no-verify`.
  Then, for the `abandoned`, `asks moved`, `worktree`, `claim`, `orphans`, `tree idle` and
  `task stalled` cases, `run --resume tWake --keepalive-id k1` followed by `run --audit tWake` prints
  check 106, check 73 and check 58; a claim that `git ls-remote "$F.bare" refs/gov/runs/tWake` then
  lists; `reaping is OFF because PROCMON_CMD is blank, so 1 orphan(s)`; `· STALLED`; and
  `task wf · ` with `· STALLED`, respectively.
  Red when: a condition the pair acts on reads `HEALTHY`, or a reason names the wrong condition.
- **AC3** — When `echo 'KEEPALIVE_TRACKED_INTERVAL="every 30 minutes"' >> .unattended.conf` and `<reg>`
  run in a fresh fixture, `run --wake tWake --keepalive-id k1` prints a line ending
  `· tasks 1 open · cadence every 30 minutes`. After `run --release-task tWake --task wf` it prints
  one ending `· tasks 0 open · cadence every 10 minutes`. Without the key, both lines name
  `every 10 minutes`. With `KEEPALIVE_INTERVAL=""` and no task, the line ends `cadence undeclared`.
  Red when: the cadence ignores the registry, a blank key changes the cadence, or a key that is not
  declared aborts the verb under `set -u`.
- **AC4** — When, in a fresh fixture after `<reg>`, each of `--audit tWake`, `--liveness tWake`,
  `--status tWake` and `--resume tWake --keepalive-id k1` runs through `run0` and then `run`, the two
  outputs are identical after `<norm>`, and so are the exit codes. The same holds after `<age>` and
  `<stale-beat>`. In order, `run0 --register-task tWake --task w2 --heartbeat "$F.beat/b2"`,
  `run0 --release-task tWake --task w2`, and the same two calls through `run` print the same two
  lines after `<norm>`, because a released name may register again. `git status --porcelain` prints
  nothing after every pair.
  Red when: an extraction moved an existing verb's byte, exit code or write.
- **AC5** — When the timing probe runs in a clone of the built tree, the median wall of three
  `run --wake tWake --keepalive-id k1` calls is below the median wall of three
  `run --resume tWake --keepalive-id k1` calls followed by `run --audit tWake`. Both figures, and the
  node's load, are recorded beside the instrument in the acceptance ledger. The probe is
  `git clone -q --no-hardlinks <worktree> "$TEMP/wkreal"`, then `<remote>`'s bare-repository step
  pointed at `"$TEMP/wkreal.bare"` with `git remote set-url origin`, then a `memory/builds/tWake/`
  folder holding a README and a run-state file like the fixture's, with
  `run-branch: refs/heads/<the clone's branch>`, committed.
  Red when: `--wake` costs as much as the pair, or the clone's claims reach the real repository.
  cost: about two minutes, mostly the clone.
  figure: DERIVED at observation time. The base pair's 30.7 s and 13.9 s are PINNED, 2026-11-14.
- **AC6** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it exits 0.
  `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` and
  `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` print nothing.
  `grep -c 'unattended.sh --wake ' .claude/skills/unattended/SKILL.md` prints at least 1.
  `grep -c -e '^- `--wake` — ' memory/guides/UNATTENDED-VERBS.md` prints 1.
  `grep -c 'KEEPALIVE_TRACKED_INTERVAL' memory/guides/UNATTENDED-PROTOCOL.md` prints at least 1.
  `grep -c '^#   unattended[.]sh --wake <slug> --keepalive-id ' tools/unattended/unattended.sh` prints 1.
  `grep -c '^KEEPALIVE_TRACKED_INTERVAL=""$' tools/unattended/.unattended.conf.example` prints 1.
  `grep -c '"KEEPALIVE_TRACKED_INTERVAL"' tools/unattended/kit.toml` prints 1.
  `grep -c 'then `--audit`' memory/map/features/unattended.md` prints 0.
  `bash skills/session-kickoff/manifest-check.sh` reports no stale `last-audit`.
  Red when: a render was hand-edited or not re-rendered, a carrier lacks the verb or the key, or the
  conf moved without the manifest's re-stamp.
- **AC7** — When `python tools/govkit/docs_leg.py --fingerprints` runs, the row for
  `verb:unattended.sh:--wake` carries a fingerprint that
  `grep -c "verb:unattended.sh:--wake <fingerprint> -->" <page>` finds once.
  `python tools/govkit/docs_leg.py --list --undocumented` does not print that id.
  `grep -c '(idle-wake.md)' help/README.md` prints 1.
  Red when: the page is missing, its anchor is stale, or the README does not link it.
  figure: the fingerprint is DERIVED from the built header at observation time.
- **AC8** — When `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh` runs, it
  prints 319. `grep -cE '^[^#]*check_lease_current' tools/unattended/unattended.sh` and
  `grep -cE '^[^#]*check_tree_progressing' tools/unattended/unattended.sh` each print 3: one
  definition and two calls. `grep -c 'UNIT_STALL_BOUND" ]' tools/unattended/unattended.sh` prints 1,
  the line inside `check_tree_progressing`.
  Red when: the wake added a refusal site, or a predicate was copied rather than shared.
  figure: 319 is PINNED, 2026-11-14, from the driver at `846d51d39`.
- **AC9** — When `tr -d '\r' < .claude/skills/unattended/SKILL.md | wc -c` and the same over
  `memory/guides/UNATTENDED-PROTOCOL.md` run, each prints the figure on that file's row of
  `tools/template-size-limits.txt`, and the comment above each row holds `by TOOL-aLightenedLoop-2`.
  `grep -c '^- \*\*TOOL-aLightenedLoop-2\*\*' memory/DECISIONS.md` prints 1.
  `wc -c < memory/guides/UNATTENDED-VERBS.md` prints at most 98304, and at most 900 above its base
  of 96906.
  Red when: a row kept its old value under a longer render, a row was given headroom, a raise landed
  with no decision row, or the verbs carrier overran its cap.
  figure: the new row values are DERIVED from the renders at the pass. 96906 is PINNED, 2026-11-14.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended skill size` · `unattended protocol size` · `docs` · `memory hygiene` · `kickoff-manifest ratchet` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` · `scratch-guard self-test` · `tier2-review self-test` · `check-wiring self-test` · `lexicon naming predicates` · `policy fixtures` · `recall floor` · `recall floor arms`

The first eight grade this unit's change directly, and the three after them grade the new shell
code. The last seven are owed because a path of the estimate trips their guard. The brief also owes
`bash tools/unattended/run-unattended-gates.sh --pooled`. The main loop runs it and the merge bar
once, at the close. No leg is added.

Every arm below uses the suite's `build_audit_fixture` and its task-registry block
(`tools/unattended/unattended.test.sh@0d9cd1632c89:9521` and `:9673`). The RED observation of each
is the suite run against the driver at `846d51d39`, where `--wake` is check 14's unknown argument.

New arm: tools/unattended/unattended.test.sh · covers AC1 · a leased holder record with a fresh registered task reads HEALTHY and leaves the record's hash unchanged · none
New arm: tools/unattended/unattended.test.sh · covers AC2 · each reason's staged break reads FULL with that reason, with the orphan case built from `write_pl_orphan` · none
New arm: tools/unattended/unattended.test.sh · covers AC3 · the cadence field with the tracked key declared, with it blank, and before and after a release · none
New arm: tools/unattended/unattended.test.sh · covers none · the parity table's `wake` row, in-process against a spawned process · none

What these arms do not check: that the agent replaces the job when the cadence changes, which is
an agent act no script observes, and the wall-clock saving, which AC5 measures once.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.

## 10. Reuse audit

No existing seam answers the question "would the pair act". The verb is new, and it reads only
predicates the pair already owns: `check_asks_moved`, `resolve_holder_worktree`, `read_claims` with
`check_claim_writable`, `read_proc_ledger` with `derive_proc_state`, `read_tree_clocks`,
`print_task_audit` and `read_bound_key`. Three inline expressions it would otherwise copy are
extracted, so each stays one predicate (S2). The probe was
`python tools/codebase-map/reuse_lookup.py "a cheap idle-wake tick that reports a healthy run without resuming or auditing"`,
which ranked name stems only (`run`, `report`, `audit`, and `read_tick_registration`, the resume
tick's) and named no seam that fits. Recall returned the slowdown analysis, the verbs carrier's
idle-wake section, protocol §5, TOOL-aRepatriatedFork-53 (the task registry) and
TOOL-dDerivedDocket-61 (the lease record). The analysis also names `verb_resume` near line 9335,
which matches the base.

Recall terms used: idle-wake keepalive tick resume audit register-task heartbeat cadence
KEEPALIVE_INTERVAL stalled liveness
