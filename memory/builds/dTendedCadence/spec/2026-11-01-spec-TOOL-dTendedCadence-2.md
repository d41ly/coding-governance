# TOOL-dTendedCadence-2 — the cadence: Maintain's row on Runtime's hosts, its period, its event runs and the session-start host

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 18 · closes TOOL-dTendedCadence-19

**Carries:** cl-dClosedLoop-0443@06da9bab whole
**Carries:** node:policy-key.maintain.host
**Carries:** node:policy-key.maintain.cadence
**Carries:** node:policy-key.maintain.events

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 |
| [2026-11-01-build-TOOL-dTendedCadence-1-reuse-scout-a.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-reuse-scout-a.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-3 TOOL-dTendedCadence-6 TOOL-dTendedCadence-8 TOOL-dTendedCadence-10 |
| [2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-1 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 |

<!-- /gen:spec-records -->

## 1. Goal

No declared cadence item runs on a schedule (gap-maint-01): the only scheduled actors are the resume
tick, the desktop restart task and CI's read-only cron. This unit turns Maintain on, last, because it
needs everything Maintain runs: Maintain's row at `point.cadence-items`, run on the host
`maintain.host` names, per the period `maintain.cadence` names, and once per event and sha for the
events `maintain.events` names, `release-verify-failed` rendered not installed where integrations is
not installed; and the `session-start` host, `maintain.host`'s default, which the runtime build hands
to this one (TOOL-dWellOiledMachine-13 §3, TOOL-dWellOiledMachine-59 §3).

## 2. Scope (IN)

- **S1** — The row: one `[[adapter]]` row at `point.cadence-items` in `tools/runtime/points.toml`
  (TOOL-dWellOiledMachine-59 S1), `name = "maintain"`, `host-key = "maintain.host"`, `period-key =
  "maintain.cadence"`, `run = ["python", "tools/drift-audit/maintain.py"]` (I1, TOOL-dTendedCadence-1)
  and `events = ["default-branch-red", "release-verify-failed", "session-start-breach"]`, with the
  grant, tenancy, retention and region fields the point's rows carry. The period is the policy value,
  read by the tick as it reads `host-key`, and `every-session` is keyed by the waking session (ask TOOL-dTendedCadence-29,
  §8 F1). Build-run precondition: TOOL-dWellOiledMachine-59 and ask TOOL-dTendedCadence-29 landed. Observed by AC1 and AC3.
  The node pass's row beside it: a second `[[adapter]]` row, `name = "maintain-node"`, the same
  `host-key` and `period-key`, `run = ["python", "tools/drift-audit/maintain.py", "--scope", "node"]`,
  the `--scope node` pass TOOL-dTendedCadence-16 S6 adds, `per-node = true` so its period lease is
  keyed `<period>.<node>` and each node runs it once a period, and no `events`. It waits on ask
  TOOL-dTendedCadence-32, which gives a cadence row `per-node`: until that lands the row is not
  registered, and only the period's lease holder reads node-scoped readings, the `lease-holder`
  behaviour (TOOL-dTendedCadence-16 §8 F5). Observed by AC1.
- **S2** — The host. `maintain.host`'s values are host rows at `point.host-adapters`:
  `os-scheduler` and `requesting-node` are the node tick (TOOL-dWellOiledMachine-13 S2), `session-start`
  is S5's, and `cloud-routine` has no row until integrations registers one, so the tick prints `host
  cloud-routine not ready` and runs nothing (TOOL-dWellOiledMachine-59 S3). Each wake runs only the rows
  its own host serves, `cadence.py tick --host <name>` (ask TOOL-dTendedCadence-30, §8 F2). Build-run precondition: ask TOOL-dTendedCadence-30
  landed. Observed by AC2.
- **S3** — Maintain's event wake, added to the tables TOOL-dTendedCadence-13 S7 builds in
  `tools/drift-audit/cadence_events.py`. `EVENT_WAKES` gains `maintain`, host key `maintain.host`,
  whose selector reads `maintain.events` through I2, a bounded `policy.py get maintain.events`
  subprocess with the key a string literal, and returns its members in the row's order, `[]` printing
  `cadence — maintain · no event named`. `EVENT_PRODUCERS` gains Maintain's three events:
  `default-branch-red`, read by `read_bar_red(repo)` as one bounded `git ls-remote <remote>
  refs/gov/bar-red`, the ref `tools/run-gates/post-merge.sh:252` pushes when the default branch's bar
  reds, absent meaning no event; `release-verify-failed` (S4); `session-start-breach` (S6). Each
  selected event whose producer names a sha runs once through `run_event_runs`, keyed
  `<event>.<sha12>`, the period segment `derive_event_key` returns (TOOL-dTendedCadence-8 S6), under the
  `maintain` cadence segment (I7), so Maintain's program reads the event from its
  `GOV_CADENCE_KEY` (ask TOOL-dTendedCadence-27) and carries only the readings whose events name it (TOOL-dTendedCadence-1
  S3, TOOL-dTendedCadence-8). Observed by
  AC4.
- **S4** — `release-verify-failed` rendered not installed. Integrations is installed when a kit
  descriptor under the install prefix declares `layer = "layer.integrations"` (PLAY-dOrderedCharter-16
  S2), read by `read_installed_layers(prefix)` over the descriptors' TOML. Absent, the event prints
  `cadence — maintain · event release-verify-failed · not-installed: integrations`, the state word of
  PLAY-dOrderedCharter-17 S9's slot line; present and with no producer registered in
  `EVENT_PRODUCERS`, it prints `· no producer registered`; neither runs. dShippedRelease registers the
  release slot's exit-record reader there. Observed by AC5.
- **S5** — The `session-start` host: an `[[adapter]]` row at `point.host-adapters` in
  `tools/runtime/points.toml`, `name = "session-start"`, `tick = "gov-maintain-session"`, `fragment =
  "tools/drift-audit/maintain-session.fragment.json"`, `remote-time = "http-date"`, `grant = { service
  = "local", scopes = [], secret = "anonymous" }` and I4's `tenancy`, `retention` and `region`, which
  `check_host_row` accepts (TOOL-dWellOiledMachine-13 S3) and whose readiness is that fragment wired,
  asked as `settings-merge.py --check --fragment <path>` asks it (ask TOOL-dTendedCadence-30). The fragment is
  `{"name": "maintain-session", "event": "SessionStart", "matcher": "startup", "marker":
  "maintain_session.py", "hook_path": "{kit}/drift-audit/maintain_session.py"}`, the shape of
  `tools/process-monitor/procmon-session.fragment.json`, listed in `tools/drift-audit/kit.toml` as an
  `engine` file so the hook-destination leg grades it. `adopt-drift-audit.sh --scaffold` merges it
  through `tools/settings-merge.py --fragment` and `--check` reports it wired or not; this repository's
  `.claude/settings.json` takes the merge. Observed by AC8 and AC10.
- **S6** — The hook, `tools/drift-audit/maintain_session.py`, the session-start host's wake. It reads
  the SessionStart payload from stdin, at most 64 KiB, takes `session_id` only when it matches
  `[A-Za-z0-9-]{1,64}`, and starts two detached processes, `python <runtime kit>/cadence.py tick --host
  session-start` with `GOV_SESSION_ID` set to that id (ask TOOL-dTendedCadence-29's every-session key source) and `python
  cadence_events.py tick --tick gov-maintain-session`, then exits 0 at once, writing nothing on stdout,
  which a SessionStart hook would put into the session's context. A missing or malformed id, an
  unreadable payload or a failed start writes one line on stderr, starts nothing and still exits 0, so
  the session is never blocked. `--dry-run` prints the two argvs and the id instead. At this wake only,
  `read_session_breach(repo)` is `session-start-breach`'s producer: the newest complete group of
  `drift-history.tsv` in the git common dir, the source the card's `drift —` cell reads
  (`skills/session-kickoff/manifest-check.sh:441-447`), holding a signal whose state is `dead`, the one
  breach that cell names (`<signal> DEAD`, `:466`), answers the group's sha; any other wake answers no
  event and prints `· session-start-breach · session-start wake only` (§8 F4). Observed by AC6 and AC9.
- **S7** — The parity: `python cadence_events.py --check` exits 1 naming each event that the
  `maintain` row's `events` and the `maintain.events` catalogue row's allowed set
  (`tools/policy/catalogue.toml:1138-1143`) do not both name, and naming any `EVENT_WAKES` entry with no
  row at `point.cadence-items`; it exits 0 printing `cadence events — <n> wake(s), <m> event(s)` on the
  tree. One fact is spelled twice and the check compares them. Observed by AC7.
- **S8** — The catalogue rows of `maintain.host` (`catalogue.toml:1113-1117`), `maintain.cadence`
  (`:1119-1123`) and `maintain.events` (`:1138-1143`) gain `summary` and `usage`, and `python
  tools/policy/policy.py lists --write` drains the three names from
  `tools/policy/unsummarised-keys.txt` (`:111`, `:113`, `:115`); values and defaults stay as written.
  The literal readers are the tick's `host-key` and `period-key` reads and S3's selector. Observed by
  AC11.
- **S9** — The docs: the page `help/maintain.md` gains a section "The cadence": the row, the four
  hosts, the three periods, the three events and their producers, the not-installed line, the
  session-start hook and how to unwire it. `KIT_DRIFT_AUDIT_VERSION` moves once per pass that changes
  the kit. Observed by AC12.

## 3. Non-goals (OUT)

- The Maintain program, its items and its readings: TOOL-dTendedCadence-1 and -8. This unit names
  `maintain.py` as the row's argv and registers nothing it runs.
- The tick, the period key, the period witness, the lease and the budget: TOOL-dWellOiledMachine-59
  and -13, and the two changes asks TOOL-dTendedCadence-29 and TOOL-dTendedCadence-30 ask of them.
- The release slot's exit record and its reader: dShippedRelease's; S4 renders the event's absence.
- A breach cell of the card's own: the card's cells are rendered by the kickoff engine, and S6 reads
  the `drift —` cell's source rather than adding a cell.
- `kits.host` and `kits.watch-cadence`: dShippedRelease's keys, which name the same `session-start`
  host and the same `every-session` kind and reuse S5 and ask TOOL-dTendedCadence-29.
- Reaping a hook-started process that outlives its session: process-monitor's census and
  TOOL-dTendedCadence-3's `reap` fix.

### Edges

- **consumes-from** `TOOL-dTendedCadence-1` — `maintain.py`, the argv S1's row runs, reading its key from `GOV_CADENCE_KEY`, a period or S3's `<event>.<sha12>`
- **consumes-from** `TOOL-dTendedCadence-13` — `run_event_runs`, with `EVENT_PRODUCERS` and `EVENT_WAKES`, which S3, S4 and S6 extend with Maintain's wake and its three events
- **consumes-from** `TOOL-dTendedCadence-16` — `--scope node`, the node pass S1's `maintain-node` row runs once a period on each node, under ask TOOL-dTendedCadence-32
- **consumes-from** `TOOL-dTendedCadence-8` — the event run key I7 spells, `<event>.<sha12>` as `derive_event_key` returns it, under the `maintain` segment, which S3's event runs take
- **consumes-from** external — TOOL-dWellOiledMachine-59's `point.cadence-items`, `check_cadence_row` and tick, -13's `point.host-adapters`, `check_host_row`, `hosts.py ready` and `cadence.py run`, each with asks TOOL-dTendedCadence-29 and TOOL-dTendedCadence-30; PLAY-dOrderedCharter-16's `layer` key; `tools/settings-merge.py`, landed
- **hands-off** external — dShippedRelease registers `release-verify-failed`'s producer in `EVENT_PRODUCERS`; dWellOiledMachine builds asks TOOL-dTendedCadence-29 and TOOL-dTendedCadence-30
- **hands-off** `TOOL-dTendedCadence-41` — `maintain-session.fragment.json` and its hook, which that unit launches through a `bash` shim (review id 30)
- **consumes-from** `TOOL-dTendedCadence-35` — the `session` family of `RECORD_KEY_FAMILIES`, which admits the `s-<12hex>` key an `every-session` run writes its record under (review id 1)
- **hands-off** `TOOL-dTendedCadence-48` — the `maintain.events` read through the one adapter, the version rows and the hook's dossier claim, which the minors batch repairs (review ids 26, 32, 36)

## 4. Design

### Evidence

- The three catalogue rows exist and answer today: `policy.py get maintain.host` prints
  `session-start`, `maintain.cadence` `daily`, and `maintain.events` the three defaults (scout A,
  re-read at `catalogue.toml:1113-1143`).
- A row's `period` is a literal `daily` or `weekly` (TOOL-dWellOiledMachine-59 S1), so neither a
  policy-chosen period nor `every-session` has a home; `kits.watch-cadence` has the same gap
  (`catalogue.toml:1095-1096`).
- `read_tick_registration` asks only for `gov-resume-tick` (`tools/unattended/lib-unattended.sh:674-686`),
  so a session-start host asked through it answers for the node tick.
- The default branch's red is published now: `post-merge.sh:252` sets `PM_RED_REF=refs/gov/bar-red`.

### The wakes

| Wake | Started by | Runs | Event producers it reads |
|---|---|---|---|
| node tick | `tools/unattended/resume-tick.sh` | `cadence.py tick --host` each node-tick host; `cadence_events.py tick --tick gov-resume-tick` | `landed`, `default-branch-red` |
| session start | `maintain_session.py`, the SessionStart hook | `cadence.py tick --host session-start`; `cadence_events.py tick --tick gov-maintain-session` | those, and `session-start-breach` |

A row runs only at the wake its host key's value names, so Maintain runs at session start by default
and at the node tick under `os-scheduler` or `requesting-node`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `maintain` | `[[adapter]]` row at `point.cadence-items` and its cadence segment | none |
| `maintain-node` | `[[adapter]]` row at `point.cadence-items`, the node pass's, and its cadence segment | none |
| `session-start`, `gov-maintain-session` | host row and its tick name | none |
| `fragment` | host-row field, ask TOOL-dTendedCadence-30's | none |
| `maintain-session.fragment.json`, `maintain_session.py` | hook fragment and hook | none |
| `read_bar_red`, `read_session_breach`, `read_installed_layers` | Python functions | `py.function`, `read`, OK |
| `cadence_events.py --check` | CLI form | none |

### Files touched (estimate)

- `tools/runtime/points.toml`: the `maintain` row and the `session-start` host row
- `tools/drift-audit/cadence_events.py`: Maintain's wake, its producers, `--check` and plants
- `tools/drift-audit/maintain_session.py`: the hook
- `tools/drift-audit/maintain-session.fragment.json`: the fragment
- `tools/drift-audit/kit.toml`: the fragment's `[[files]]` row
- `tools/drift-audit/adopt-drift-audit.sh`: `--scaffold` merges and `--check` reads the fragment
- `tools/drift-audit/selftest.py`: the plants' cases
- `tools/drift-audit/drift_report.py`: `KIT_DRIFT_AUDIT_VERSION`
- `.claude/settings.json`: this repository's merge of the fragment
- `tools/policy/catalogue.toml`: three rows' `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`: the render that drains them
- `help/maintain.md`

### Alternatives rejected

- **Two rows, `maintain-daily` and `maintain-weekly`, each exiting at once when the key names the
  other.** Each period's witness would then certify a run that ran nothing, and `every-session` would
  still have no key. The test: a weekly key on the daily row leaves seven `landed` witnesses a week
  for zero Maintain runs.
- **Event runs as declared waits** (TOOL-dWellOiledMachine-18 S1-S4). A wait is keyed to a build and
  ends at its first wake, so a recurring event re-declares after every wake and a Maintain run has no
  build; the test is S4's wake, which runs only for a build no lease holds.
- **A session-start host asked through the tick probe.** It answers whether `gov-resume-tick` is
  registered (`lib-unattended.sh:674-686`), so a node with the tick reads ready while no hook is wired.
- **A live signal over its pin as the session breach.** `drift-history.tsv` carries no pin
  (`HISTORY_COLUMNS`, `drift_report.py:3758`), so the hook would run the report at session start.

## 5. Production-readiness checklist

- security — the hook reads at most 64 KiB of stdin, admits a session id only by a closed character
  class before it reaches an environment variable, passes no payload text to a shell, and starts its
  two processes with argument lists; its failures never block a session. The producers read refs and
  one tracked-file-free log; nothing is written but by the programs the lease admits.
- perf / scale — the hook returns at once; each detached process reads two to four policy keys and
  one lease before it runs anything, and the period witness keeps Maintain to once per period across
  the fleet; `every-session` leaves one lease ref per session, the owner's chosen cost.
- error / empty / loading states — no remote: `default-branch-red` answers no event; `maintain.events`
  empty: one line, no event run; host not ready: the tick's line; a missing `drift-history.tsv`: no
  breach; integrations absent: the not-installed line.
- observability — one line per wake decision and per event; the lease records and the maintenance
  record are the run's history.
- risks — every session start in this repository now starts two short processes; `maintain.host:
  os-scheduler` moves Maintain to the node tick and leaves the hook a no-op.
- testing — the fixture plants of §6, and §7's arm.
- migration — N/A: the rows are new and the catalogue values unchanged; an adopter's `--scaffold`
  merges the fragment and `settings-merge.py --unwire` removes it.
- user docs — `help/maintain.md` (S9).

## 6. Acceptance criteria

- **AC1** — When `python cadence.py --check` runs over the tree, it registers `maintain` with no
  refusal line naming it, and, once ask TOOL-dTendedCadence-32 has landed, `maintain-node` with
  `per-node = true` and a `run` ending `--scope node`.
  Red when: the row's `host-key` or `period-key` names no catalogue row, or `maintain-node` runs the
  period walk rather than the node pass.
  permission: `cadence.py` is TOOL-dWellOiledMachine-59's, built with ask TOOL-dTendedCadence-29 before this unit's build run.
- **AC2** — When `python cadence_events.py --fixture --plant host-os-scheduler` commits `maintain.host
  = "os-scheduler"` and runs `cadence.py tick --host os-scheduler --dry-run` and `--host session-start
  --dry-run`, the first prints a decision to run `maintain` and the second none; `host-session-start`
  prints the reverse; `host-cloud-routine` prints `cadence — maintain · host cloud-routine not ready`
  under both.
  Red when: a wake runs a row hosted on another host.
  fixture: a bare remote and a clone under `%TEMP%` with short names; policy is read at the landed
  revision (`tools/policy/policy.py:724-736`), so each plant commits `.governance/policy.toml`.
- **AC3** — When the plants `cadence-daily`, `cadence-weekly` and `cadence-every-session` run the tick
  dry run at `2026-11-01T09:00:00Z`, the period keys are `2026-11-01`, `2026-W44` and `s-` followed by
  the first 12 hex of SHA-256 over the planted `GOV_SESSION_ID`.
  Red when: `every-session` keys by date, or the row's literal period wins over the key.
  figure: the keys are DERIVED by `derive_period` at the fixed `--now`.
- **AC4** — When the plant `events-default` pushes a commit `R` to the bare remote's
  `refs/gov/bar-red` and runs `python cadence_events.py tick --tick gov-resume-tick --dry-run`, it
  prints `cadence — maintain · event default-branch-red.<R12> · run`; `events-empty` (`maintain.events
  = []`) prints `cadence — maintain · no event named`; `bar-red-witnessed`, whose lease for that key
  reads `landed`, prints no run for it.
  Red when: an empty `maintain.events` runs an event, or a witnessed red runs again.
- **AC5** — When the plant `events-default` runs the same dry run, it prints `cadence — maintain ·
  event release-verify-failed · not-installed: integrations`; the plant `integrations-installed`, whose
  fixture tree carries a kit descriptor declaring `layer = "layer.integrations"`, prints `· no producer
  registered`; neither runs the event.
  Red when: the event runs, or prints nothing, where integrations is absent.
- **AC6** — When the plant `session-breach` writes a `drift-history.tsv` whose newest group at sha `S`
  holds one `dead` signal, `cadence_events.py tick --tick gov-maintain-session --dry-run` prints `event
  session-start-breach.<S12> · run`, and `--tick gov-resume-tick` prints `session-start-breach ·
  session-start wake only`; the plant `session-no-breach`, all signals live, prints no run.
  Red when: the node tick reads the breach, or a live group fires it.
- **AC7** — When `python cadence_events.py --check` runs over the tree, it exits 0 printing the wake
  and event counts; the plant `row-events-drift`, whose `maintain` row omits `session-start-breach`,
  exits 1 naming that event.
  Red when: the drifted row passes.
- **AC8** — When `python hosts.py --check` runs over the tree, it refuses no `session-start` row; in
  the fixture, `python hosts.py ready session-start` prints `host — session-start · ready` after
  `settings-merge.py --fragment` merges the fragment into the fixture's settings and `host —
  session-start · not registered` before.
  Red when: readiness follows the resume tick's registration instead of the fragment.
  permission: `hosts.py` is TOOL-dWellOiledMachine-13's, built with ask TOOL-dTendedCadence-30 before this unit's build run.
- **AC9** — When `python maintain_session.py --dry-run` reads `{"session_id": "abc-123"}` on stdin, it
  prints the two argvs with `GOV_SESSION_ID=abc-123` and exits 0 with nothing else on stdout; given
  `{"session_id": "../x"}` or 70 KiB of input it prints nothing on stdout, one line on stderr, starts
  nothing and exits 0.
  Red when: a malformed id reaches the environment, or a refusal exits non-zero.
- **AC10** — When `bash tools/drift-audit/adopt-drift-audit.sh --check` runs in the fixture before and
  after `--scaffold`, it reports the `maintain-session` fragment not wired, then wired, and the
  fixture's settings carry the hook once after a second `--scaffold`.
  Red when: a second scaffold adds a second entry.
- **AC11** — When `grep -n -A6` reads the three rows of `tools/policy/catalogue.toml`, each shows
  `summary` and `usage`; `grep -cxE 'maintain\.(host|cadence|events)'
  tools/policy/unsummarised-keys.txt` prints `0`; `grep -n '"maintain.events"' cadence_events.py`
  names S3's literal read.
  Red when: a row lacks either field, or the selector reads the key through a variable.
- **AC12** — When `grep -n 'session-start-breach' maintain.md` runs over the help page, it prints the
  section's line naming the event and its producer.
  Red when: the section is absent.

## 7. Gates

`drift-audit selftest` · `drift-audit wiring` · `hook destinations (every declared hook path ships)` · `check-wiring self-test` · `settings-merge selftest` · `lexicon naming predicates` · `policy fixtures` · `policy check` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC9 AC10 · the fixture plants, staged against a selector that ignores `maintain.events`, a producer table missing `release-verify-failed`'s not-installed arm, a breach read at the node tick, and a hook that exports an unchecked id · none

## 8. Open questions

- **F1 — How does `maintain.cadence` set the row's period, `every-session` included?** A row's
  `period` is a literal kind and `derive_period` takes `daily` and `weekly` only (scout A disagreement
  2). (a) Two literal rows that exit when the key names the other, which certify empty periods (§4);
  (b) ask dWellOiledMachine for a key-read period and a session kind; (c) drop `every-session` from the
  catalogue, a departure from v2:1320. (b) meets every value of the key and serves dShippedRelease's
  `kits.watch-cadence` too. Rung 3. RESOLVED (agent, 2026-11-01, delegated): (b), new ask TOOL-dTendedCadence-29 ·
  dWellOiledMachine · a `point.cadence-items` row may carry `period-key`, a catalogue key the tick reads
  through `policy.py get` as it reads `host-key`, in place of `period`; `derive_period` takes
  `every-session`, its key `s-` and the first 12 hex of SHA-256 over `GOV_SESSION_ID` · accept the tick
  over a row whose `period-key` holds `weekly` runs it once per ISO week, and one holding
  `every-session` once per session id, seen on two plants. Build-run precondition.
  widens: none · relaxes: none
- **F2 — How is the `session-start` host ready, and how does a wake run only its own rows?**
  `check_host_row` requires a `tick` and `hosts.py ready` asks the resume tick's probe (scout A
  disagreement 3), and `cadence.py tick` runs every row whose host is ready, so the node tick would run
  a session-start row. (a) Ask dWellOiledMachine for a host row's `fragment` readiness and a `--host`
  filter on the tick; (b) move `maintain.host`'s default to `os-scheduler`, a departure from v2:1319;
  (c) a hook that calls `cadence.py run` itself, bypassing the tick's budget. Rung 3, (a) the only
  option keeping the default and the budget. RESOLVED (agent, 2026-11-01, delegated): (a), new ask TOOL-dTendedCadence-30 ·
  dWellOiledMachine · a host row may carry `fragment = "<path>"`, and `hosts.py ready` answers it as
  `settings-merge.py --check --fragment <path>` answers, in place of the tick probe; `cadence.py tick
  --host <name>` runs only the rows whose host key's value is `<name>`, and the node tick passes each
  host whose row's `tick` is `gov-resume-tick` · accept on a fixture with one row on `os-scheduler` and
  one on `session-start`, the node tick runs only the first and `--host session-start` only the
  second, and `hosts.py ready session-start` follows the fragment's wiring. Build-run precondition.
  widens: none · relaxes: none
- **F3 — What fires an event run?** WOM-59 S1 declares a row's `events` and no parent fires them.
  (a) TOOL-dTendedCadence-13's `run_event_runs`, extended here; (b) an ask that the tick fire them;
  (c) declared waits, which end at their first wake and are keyed to a build (§4). (a) is buildable
  in this build and reuses the one event wake it already has; the second cadence row outside this
  build that takes events extracts it to the runtime kit. Rung 3. RESOLVED (agent, 2026-11-01,
  delegated): (a). widens: none · relaxes: none
- **F4 — What produces `session-start-breach`?** layer-expansions:234 names "the card's cells", and no
  cell emits a breach a machine reads. (a) The `drift —` cell's source group holding a `dead` signal,
  the one breach that cell prints as such; (b) a live signal over its pin, which the history cannot
  answer; (c) the card's `BUDGET WARN` lines (`manifest-check.sh:1313`), a size cap's breach, which
  `budgets.enforce` already owns. Rung 3. RESOLVED (agent, 2026-11-01, delegated): (a), read at the
  session-start wake only. widens: none · relaxes: none
- **F5 — How does the program learn its period?** As TOOL-dTendedCadence-1 §8 F3: ask TOOL-dTendedCadence-27,
  `GOV_CADENCE_KEY` set by `run_cadence_period`; an event run's key is `<event>.<sha12>`, so no
  argument carries the event. RESOLVED (agent, 2026-11-01, delegated): ask TOOL-dTendedCadence-27.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 35, 41, 48); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended: the cadence row of TOOL-dWellOiledMachine-59 S1 and its tick (S3), the host rows,
`check_host_row` and `hosts.py ready` of TOOL-dWellOiledMachine-13 S2-S4, each with the change asks TOOL-dTendedCadence-29
and TOOL-dTendedCadence-30 name; TOOL-dTendedCadence-13's `run_event_runs` and its two tables; the SessionStart fragment
shape of `tools/process-monitor/procmon-session.fragment.json` merged by `tools/settings-merge.py
--fragment`; the bar's red ref, `tools/run-gates/post-merge.sh:252`; the `drift —` cell's source,
`skills/session-kickoff/manifest-check.sh:441-472`; and the layer key of PLAY-dOrderedCharter-16 S2.
The probe `python tools/codebase-map/reuse_lookup.py "register a program on a schedule with its host
and its period and run it once per period at the node tick or at session start"` ranked
`read_tick_registration` and `read_host_name` (SEAM, read and rejected as the session host's probe,
§4) and otherwise matched name stems only (`run`, `run_git`, `extract_session`); so no existing seam
fits the wakes themselves, and they are new over the seams above. Where scout A's record and source
disagree at this base: its catalogue lines `:1114`, `:1120` and `:1139` are each row's `name` line, the
rows opening one line earlier; its disagreements 2 and 3 hold and are asks TOOL-dTendedCadence-29 and TOOL-dTendedCadence-30; its "event run key
… must pass `check_cadence_segment`" holds for the cadence segment only, the period segment being held
by `check_lease_segment` (TOOL-dPlacedRequest-1 S1, TOOL-dPlacedRequest-18 S1), so `<event>.<sha12>`
with its dot is legal there.

Recall terms used: `python tools/memory-recall/query.py "how does a cadence item run on a host per
period and fire event runs keyed by event and sha" --terms "cadence period lease host session-start
os-scheduler resume-tick event bar-red maintain.host derive_period witness"`
