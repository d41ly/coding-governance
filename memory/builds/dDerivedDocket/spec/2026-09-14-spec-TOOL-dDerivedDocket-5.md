# TOOL-dDerivedDocket-5 — auto-resume from HELD

**Status:** SPECCED · rev-3 · 2026-09-16 · node d · Tier-2 · base abac6d59 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md) | spec-audit | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round2.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round2.md) | spec-audit | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |

<!-- /gen:spec-records -->

## 1. Goal

A run that ends HELD resumes only when someone types `/unattended --resume <slug>`, so a usage limit
that resets at 03:00 costs the whole night. Make `--hold` say, mechanically, whether a restart is owed
and when, have the agent file that restart with a DURABLE harness scheduler under a name derived from
the slug, and make a scheduled restart refuse unless the exact hold it was filed for is still the
record's state. The owner ruled the feature ON in the kit and in this repo, overriding charter §9's
default-off gate for this one feature, and this unit records that ruling as a decision row.

## 2. Scope (IN)

- **S1** Five conf keys, read by the driver and validated by the kit gate. `RESUME_SCHEDULE` takes
  the closed set `on` or `off`; absent or blank resolves to `on`, announced as defaulted; any other
  value is a numbered refusal. `RESUME_SCHEDULE_CREATE` and `RESUME_SCHEDULE_DELETE` name the durable
  carrier's tool pair and are required while the effective value is `on`. `RESUME_SCHEDULE_DELAY`
  (seconds, default 1800) and `RESUME_SCHEDULE_LIMIT` (count, default 6) are optional, announced
  when defaulted, and refused when not a positive integer. Observed by AC1, AC2 and AC13.
- **S2** The carrier may not be the keepalive's. A declared `RESUME_SCHEDULE_CREATE` equal to
  `KEEPALIVE_CREATE` is a numbered refusal in the kit gate, because this repo's conf declares that
  store session-scoped and a restart filed there dies with the session it exists to outlive.
  Observed by AC2.
- **S3** `--hold` decides whether a restart is owed, in the SAME write as unit 4's hold facts: one
  new fact, `resume-owed`, carrying either the schedule name and its fire instant, or `none` and the
  reason. The fire rule is the §4 table: `after` fires at its instant, `probe` fires `DELAY` seconds
  after `held-at`, `owner` owes nothing. Observed by AC3 and AC4.
- **S4** `--hold` prints the owed schedule as three lines the agent copies verbatim: the name, the
  fire instant in UTC, and the restart prompt. The prompt is rendered by the driver from validated
  shapes only, and never from the hold reason. Observed by AC3 and AC5.
- **S5** A no-progress bound. A second fact, `hold-streak`, counts consecutive holds between which no
  path changed other than the run's own records: the run-state file, and the build folder's
  `BACKLOG.md`, where the asks, SEV rows and KEEP rows filed about a stop are recorded and committed
  before `--hold`. A hold after any other path changed resets the count to 1. The hold and resume
  writes move HEAD, and the stop's own ask filing changes that `BACKLOG.md`, and neither is progress.
  At `RESUME_SCHEDULE_LIMIT` the hold still succeeds and `resume-owed` reads `none · limit`, so a run
  that cannot move stops spawning sessions. Observed by AC6.
- **S6** `--resume <slug> --scheduled <held-at>` is the only restart a schedule issues. Before any
  write it refuses, numbered, unless the record is HELD, its `held-at` equals the value passed, and,
  under `ANCHOR_SCOPE=published`, the tip the remote advertises for the run branch is HEAD or an
  ancestor of it, so no session anywhere has pushed work this worktree lacks. An unreachable remote
  refuses too. On success it runs unit 4's take-over unchanged, which requires the session's own
  `--keepalive-id`, and its history row carries `scheduled`. Observed by AC7 and AC8.
- **S7** `--status` on a HELD record prints the owed-schedule line beside unit 4's checkpoint.
  Observed by AC3.
- **S8** The Skill carries the agent's half. The hold step files the printed schedule with
  `{{RESUME_SCHEDULE_CREATE}}` under the printed name. Every resume path issues
  `{{RESUME_SCHEDULE_DELETE}}` against that name BEFORE the keepalive reap, and a take-over pushes
  its record before any other work, so a schedule on another node meets rule 3 of §4. A refused
  scheduled resume deletes its own task and stops. With the switch `off` the render writes a fixed
  "not scheduled" literal in place of both tool keys. Observed by AC9 and AC10.
- **S9** The `keepalive-reaped` attestation covers the resume schedule too. `--close` and `--abort`
  name every schedule the record's hold history owed, beside the keepalive id, so the agent attests
  over a list it was shown. No new DoD item: the core DoD count is the asks-disposed unit's to move.
  Observed by AC11.
- **S10** The contract text — keys, fire rule, streak, refusals, carrier requirements — goes to
  unit 4's companion guide `UNATTENDED-STOPS.md`. The protocol gains one sentence in §5 pointing at
  it, and the verb carrier documents `--scheduled`. Observed by AC10.
- **S11** Gov's `.unattended.conf` declares `RESUME_SCHEDULE="on"` and the desktop app's
  scheduled-task tool pair; the kit's conf example declares `on` with placeholder tool names.
  `tools/unattended/kit.toml`'s conf-placeholder hole extends its discharge probe to
  `RESUME_SCHEDULE_(CREATE|DELETE)`: an adopter who fills the example's keepalive keys and keeps its
  resume placeholders substitutes no `{{…}}` placeholder, so AC9's red never fires for that conf.
  Observed by AC13 and AC15.
- **S12** One `memory/DECISIONS.md` row under the TOOL heading, keyed by this unit's id, records the
  owner's ruling that auto-resume ships on and that it overrides charter §9's default-off gate for
  this feature only. Observed by AC12.

## 3. Non-goals (OUT)

- The HELD phase, `--hold`, the lease, the take-over matrix and `derived_phase()`. All are unit 4's;
  this unit adds two facts to the hold write and one refusal set in front of the take-over.
- Observing whether a schedule exists. No script can reach a harness scheduler store, so filing and
  reaping stay agent-attested, as the keepalive is (protocol §5).
- Scheduling a restart for an `owner` hold, or for a `presumed-stopped` record. The first needs a
  human act on the machine; the second has no hold to verify a schedule against.
- A per-node operating-system task (§8 F1).
- Closing the cross-node window. A take-over on another node that has not pushed its record yet is
  invisible to a schedule filed on the holding node. §5 states it.
- Migrating adopters' confs. Each adopter meets the new keys in its own deployer build; the
  standing placeholder is what makes that decision unmissable there.
- The unattended kit's version constant. It moves once per landing range, not per unit; the build's
  one move is the held-suite baseline unit's (`TOOL-dDerivedDocket-1` S9).

### Edges

- **consumes-from** `TOOL-dDerivedDocket-4` — `--hold` and its single write, the `held-at`,
  `hold-until` and `witness` facts, the released lease and the take-over steps a scheduled resume
  runs, and the `UNATTENDED-STOPS.md` companion this unit's contract text joins. Without them there
  is no hold to schedule against and no take-over to schedule.
- **consumes-from** `TOOL-dDerivedDocket-1` — the attributed criterion over the unattended suites
  this unit runs once at its end: `verdict clean`, with every inherited suite filed.

## 4. Design

### Data model

`--hold` writes two facts beside unit 4's, in that verb's one write, so no refusal can leave a HELD
record without its restart decision:

| Fact | Value |
|---|---|
| `resume-owed` | `<name> · fire <UTC instant>`, or `none · off`, `none · owner`, `none · limit`, `none · no carrier` |
| `hold-streak` | `<n> · at <sha8>`: n is 1, or the previous n plus 1 when every path changed between the previous value's sha and HEAD is the run-state file or the build folder's `BACKLOG.md` |

Unit 4's history row gains one field, ` · resume <name>|none(<why>)`. The streak carries its own sha
because the `witness` fact is rewritten by every later phase write, so it cannot say where the
previous hold stood; `hold-streak` is written only by `--hold`, and nothing else touches it. The
comparison is one `git diff --name-only` between that sha and HEAD, with those two paths excluded.

### The fire rule

| Condition | Owed | Fire instant |
|---|---|---|
| `after <instant>` | yes | the instant, or `held-at` plus 60 s when it has already passed |
| `probe host`, `probe gate`, `probe api` | yes | `held-at` plus `RESUME_SCHEDULE_DELAY` |
| `owner` | no | — |

Each schedule is ONE-SHOT. A `probe` resume whose probe fails holds again, and that hold owes a new
one-shot; there is no recurring task to outlive the run. The chain ends at the streak limit.

### The name and the prompt

The name is `unattended-resume-` followed by the slug in lower case. Any session holding only the
slug can therefore reap it, so no write on a HELD record is needed to record a carrier id. Lower case,
because a carrier that sanitises names to kebab case would otherwise store a name a later delete does
not match. The prompt the driver prints, and the agent files verbatim:

```text
Resume the unattended run for build <slug>. Work only in the git worktree at <absolute toplevel>.
Load the unattended skill and follow its Resume section with: --resume <slug> --scheduled <held-at> --keepalive-id <the id of the keepalive you schedule first>.
If the driver refuses, delete the scheduled task named <name> and stop.
```

Every interpolated value has a validated shape: the slug passed `check_slug`, the toplevel came from
`git rev-parse --show-toplevel`, and `held-at` matched the hold's own timestamp grammar. The hold
reason is free text and never reaches the prompt, because a durable prompt executes later in a
session no one watches.

The `--keepalive-id` placeholder is fixed prompt text, not an interpolated value. The scheduled
session fills it with the keepalive its own scheduler created, because the HELD unit's take-over
refuses a missing id.

### The scheduled-resume refusals

Evaluated in order, before unit 4's take-over writes anything:

| # | Refuses when | Why |
|---|---|---|
| 1 | the record is not HELD | a working phase belongs to the lease matrix, which refuses a session that cannot show the lease's keepalive, and a schedule is filed only for a hold |
| 2 | `held-at` differs from `--scheduled` | the hold this task was filed for has ended and a later one began |
| 3 | the remote-advertised run-branch tip is neither HEAD nor an ancestor of it, under `ANCHOR_SCOPE=published` | another session pushed work after the hold; a pushed hold commit of this worktree's own is an ancestor and passes |
| 4 | the remote does not answer | freshness cannot be shown, and a restart that might double-drive is worse than one that waits for a human |

Rule 3 reuses `observe_remote`, the bounded `ls-remote` the driver already runs at preflight. Under
another anchor scope `--hold` does not require the push, so rule 3 is skipped with an announcement.

### The carrier

Declared, never spelled in the driver, exactly as the keepalive pair is. It must be DURABLE — a filed
task outlives the session that filed it — and must accept a caller-chosen name. Gov declares the
desktop app's scheduled-task pair: its own tool contract, read 2026-09-14 on node `d`, stores tasks
on disk, fires a due task at the next launch when the app was closed, and takes a caller-chosen task
id and a one-shot instant. This repo's keepalive carrier states the opposite in its own contract:
jobs live only in the session and a durable flag has no effect.

### Rollout

The kit default is `on` by owner ruling. An adopter upgrading with an existing conf gets the default,
no declared carrier, and a standing `{{RESUME_SCHEDULE_CREATE}}` placeholder in its render, which the
skill-wiring check reds. That forces the choice — declare a carrier, or write `off` — at the upgrade,
in the adopter's own deployer build, rather than letting a hold silently schedule nothing. `--hold`
itself never refuses for a missing carrier: the hold is the safe state, and refusing it would push the
run back toward the ABORTED ending unit 4 exists to replace. That argument holds for an upgrader whose
key is absent. A fresh adopter who copies the example verbatim is already caught by the probe's
keepalive half. One who fills the keepalive keys and keeps the example's resume placeholders is
caught only by the extended probe.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `RESUME_SCHEDULE`, `RESUME_SCHEDULE_CREATE`, `RESUME_SCHEDULE_DELETE`, `RESUME_SCHEDULE_DELAY`, `RESUME_SCHEDULE_LIMIT` | conf keys | screaming snake, as every key there |
| `resume-owed`, `hold-streak` | run facts | kebab case, as every fact |
| `--scheduled` | flag on `--resume` | the verb carrier's flag table |
| the refusal and name helpers in the driver | shell functions | lexicon shell function cell; names pass `lexicon.py --suggest` before they are written |
| `{{RESUME_SCHEDULE_CREATE}}`, `{{RESUME_SCHEDULE_DELETE}}` | Skill placeholders | the adopter render |

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/adopt-unattended.sh` · `tools/unattended/SKILL.template.md` ·
`tools/unattended/VERBS.template.md` · `tools/unattended/PROTOCOL.template.md` · unit 4's companion
template · `tools/unattended/.unattended.conf.example` · `.unattended.conf` ·
`tools/unattended/kit.toml` · the three test files named in §7 · the rendered guides and Skill ·
`memory/DECISIONS.md`.

### Alternatives rejected

- **The keepalive's session-scoped scheduler.** Rejected by reading its own contract: jobs die with
  the session, and the stops this unit exists for include the session dying.
- **A per-node operating-system task written by a kit script.** It is a new install location and a
  standing configuration outside the repo on every node, which M3 veto 2 reserves to the owner, and
  it needs one implementation per host operating system.
- **Recording the carrier's returned id.** It needs a write on a HELD record after `--hold` or a
  schedule filed before a hold that may still refuse; the derived name needs neither.
- **A recurring schedule for `probe` holds.** It must be reaped on every successful restart and
  fires into live runs when it is not; a chain of one-shots cannot outlive the run.

## 5. Production-readiness checklist

- security — the durable prompt carries only validated shapes, never the hold reason (AC5). The
  carrier is a standing configuration outside the repo, which charter §9 gates default-off; the owner
  ruled this feature on, and S12 records it rather than leaving the override silent.
- perf / scale — at most one one-shot task per hold, and at most `RESUME_SCHEDULE_LIMIT` consecutive
  holds without progress; one bounded `ls-remote` per scheduled restart.
- error / empty / loading states — every refusal is numbered and writes nothing; an absent carrier
  records `none · no carrier` and says so at `--hold` and `--status`; a failed file call leaves the
  run HELD with the owed line naming a task that does not exist, which a manual restart clears.
- observability — the three `--hold` lines, the `--status` owed line, the `scheduled` field on the
  take-over history row, and the schedule names at `--close` and `--abort`.
- risks — a cross-node take-over that has not pushed yet is invisible to rule 3, so for that window
  two nodes can drive one slug; the Skill's take-over step pushes the record first to shrink it. A
  scheduled session that stops on a permission prompt is a stalled restart, visible in the app. Two
  slugs differing only in case map to one name.
- testing — `tools/unattended/unattended.test.sh`, `tools/unattended/check-unattended.test.sh` and
  `tools/unattended/adopt-unattended.test.sh` arms, each staged RED, plus one hand observation with a
  real carrier; the suites run once at the unit's end under unit 1's attribution.
- migration — additive facts, read as absent on every existing record. Adopters decide at their
  own upgrade (§4 Rollout).
- user docs — the companion guide section, the protocol §5 pointer, the verb carrier row and the
  Skill steps.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` grades a fixture conf declaring
  `RESUME_SCHEDULE="maybe"`, it reds naming the key and the legal set; with the key absent it reports
  the effective value `on` as defaulted and does not red on that account.
  Red when: an unrecognised spelling resolves silently to either value.
- **AC2** — When the fixture conf declares `RESUME_SCHEDULE_CREATE` equal to `KEEPALIVE_CREATE`,
  `bash tools/unattended/check-unattended.sh` reds naming both keys.
  Red when: the session-scoped keepalive tool is accepted as the durable carrier, so every restart
  dies with the session it was filed to outlive.
- **AC3** — When `--hold` runs on a HELD-capable fixture with `--until "after <future instant>"` and
  the switch on, the record gains `resume-owed` naming `unattended-resume-` plus the lower-cased slug
  and that exact instant, `--hold` prints the name, instant and prompt lines, the prompt spelling
  `--keepalive-id`, and `--status` prints the owed line.
  Red when: the fire instant is computed as `held-at` plus the delay for an `after` hold, so a
  usage-limit hold restarts into the same limit.
- **AC4** — When the fixture holds with `--until "probe host"`, `resume-owed` names `held-at` plus
  `RESUME_SCHEDULE_DELAY`; with `--until owner` it reads `none · owner` and no prompt line prints.
  Red when: an `owner` hold owes a schedule, restarting a machine into a stop only a human can clear.
- **AC5** — When the fixture's `--reason` carries the literal `EXMP-injected-text`, the prompt line
  `--hold` prints does not contain it, and `--status` still shows the reason only on unit 4's quoted
  reason line.
  Red when: the prompt interpolates the reason, so free text reaches a durable prompt.
- **AC6** — The fixture declares `RESUME_SCHEDULE_LIMIT="2"`. It holds, commits the hold together
  with a new row in the build's `BACKLOG.md`, resumes, commits the take-over, and holds again. The
  second hold writes `hold-streak` 2 and `resume-owed` `none · limit`. A third hold after a commit
  touching a file other than the run-state file and that `BACKLOG.md` writes streak 1 and owes a
  schedule again.
  Red when: the streak compares bare HEAD shas, so the hold's own commit reads as progress and the
  limit never binds; or the progress test counts the build's `BACKLOG.md`, so a hold for an inherited
  red whose Close sequence commits an auto-filed ask before every `--hold` restarts without end.
- **AC7** — When `--resume <slug> --scheduled <held-at>` runs in `tools/unattended/unattended.test.sh`
  against a working-phase record, against a HELD record with a different `held-at`, and against a
  HELD record whose local bare remote was advanced by a second clone, it refuses each time with a
  numbered message and the run-state file and lease are byte-unchanged; with the remote made
  unreachable it refuses naming the remote.
  Red when: the scheduled path falls through to the lease matrix on a working phase instead of
  refusing before it, so a scheduled session is treated as a resuming holder.
- **AC8** — When `--resume <slug> --scheduled <held-at> --keepalive-id C` runs against the matching
  HELD record, once with the remote at the pre-hold `witness` and once with the hold commit pushed,
  unit 4's take-over completes, records C, and the new history row carries `scheduled`. The same
  call without `--keepalive-id` refuses naming it, and the run-state file and lease are
  byte-unchanged.
  Red when: the scheduled path skips a take-over step, or its history row cannot be told from a
  manual restart's; or the scheduled restart carries no keepalive id, so every one is refused at the
  take-over.
- **AC9** — When `bash tools/unattended/adopt-unattended.sh --check` renders a fixture whose conf
  is on and declares no carrier, it reds on the standing `{{RESUME_SCHEDULE_CREATE}}` placeholder;
  with `RESUME_SCHEDULE="off"` it renders the fixed not-scheduled literal and passes.
  Red when: an on conf with no carrier renders a clean Skill, so an adopter learns at its first hold
  that nothing will restart it.
- **AC10** — When `bash tools/unattended/check-unattended.sh` and the skill-wiring check run over
  the rendered tree, `--scheduled` is carried by the verb guide, the Skill's hold step files the
  printed name with the create tool, its resume section deletes that name before the keepalive reap,
  and the companion guide renders byte-identical to its template.
  Red when: the resume section never deletes the schedule, so a manual restart leaves a durable task
  that later fires into a live run.
- **AC11** — When `--close` and `--abort` run on a fixture record whose history holds a hold row,
  each names that schedule beside the keepalive id in the attestation it asks for.
  Red when: the attestation names only the keepalive, so a durable task outlives the run under a
  green `keepalive-reaped`.
- **AC12** — When `memory/DECISIONS.md` is read, its TOOL heading carries one row keyed by this
  unit's id that names the owner's on-everywhere ruling and charter §9, within the 300-character
  entry budget.
  Red when: the override ships with no row, which is the silent override the owner ruled out.
- **AC13** — When `bash tools/unattended/check-unattended.sh` runs on the real tree after this unit,
  it reports the switch `on` with the declared carrier and no refusal from S1 or S2.
  Red when: gov declares the keepalive's tool as the carrier, or leaves the carrier undeclared.
- **AC14** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once at
  the unit's end, its attribution summary reads `verdict clean`: no NEW FAIL, no `DEAD PROBE at L`
  and no `OVER BUDGET at L`. Every suite it reports with INHERITED lines or `DEAD PROBE at R` is
  named by its file path in a filed backlog row or ask that is not CLOSED, as
  `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'` shows.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it; or the run is
  read by its NEW count alone, so a suite this unit's change aborted before its first FAIL line, or
  pushed past its budget, reads as clean; or an inherited failure is attributed away with no record
  filing it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: the owner's self-test lift for this build's unattended units covers this unit.
- **AC15** — The discharge command of `tools/unattended/kit.toml`'s conf-placeholder hole runs in a
  fixture whose `.unattended.conf` is the shipped example with its three `KEEPALIVE_` lines filled
  and its `RESUME_SCHEDULE_CREATE` and `RESUME_SCHEDULE_DELETE` lines left verbatim. It exits
  non-zero. With those two lines filled as well, it exits 0. The arm is staged RED by reverting the
  probe to the `KEEPALIVE_(CREATE|DELETE|INTERVAL)` alternation, under which the first fixture exits
  0.
  Red when: the probe covers only the keepalive keys, so the angle-bracket carrier names render as
  literal prose and the Skill tells an agent to file restarts with a tool named `<...>`; or the
  fixture is the verbatim example, whose keepalive placeholders red the probe with or without the
  extension.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `playbook validity gate` · `memory hygiene` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · HELD fixtures for each fire rule, the streak limit, and a scheduled resume against a moved and an unreachable local bare remote · none
New arm: `tools/unattended/check-unattended.test.sh` · fixture confs with an unrecognised switch value and a carrier equal to the keepalive tool · the check-unattended.sh arms floor, by the branches added
New arm: `tools/unattended/adopt-unattended.test.sh` · an on conf with no carrier declared · none

The observation that a real carrier accepts the printed name and instant is made once, by hand, in
this unit's pass with gov's declared pair, and recorded in the unit's journal. No gate can make it.

## 8. Open questions

- **F1** — Which carrier files the restart? (a) A harness durable scheduler named by a declared tool
  pair. (b) A per-node operating-system task written by a kit script. (c) The keepalive's scheduler.
  (c) fails the unit's own goal on the stops it exists for, and (b) trips M3 veto 2 as a new install
  location. RESOLVED (agent, 2026-09-14, delegated): (a), with the carrier requirements in §4.
- **F2** — How is the filed task identified later? (a) The id the carrier returns, recorded as a fact.
  (b) A name derived from the slug. (a) needs a write on a HELD record or a schedule filed before a
  hold that can still refuse. RESOLVED (agent, 2026-09-14, delegated): (b), lower-cased.
- **F3** — What does `--hold` do when the switch is on and no carrier is declared? (a) Refuse the
  hold. (b) Hold and record `none · no carrier`, loudly. (a) sends the run toward ABORTED, the ending
  HELD replaces. RESOLVED (agent, 2026-09-14, delegated): (b); the kit gate and the adopter check red
  the missing declaration instead.
- **F4** — What bounds a run that cannot progress? (a) Nothing. (b) A count of fires. (c) A streak of
  holds between which only the run-state file changed. (b) punishes a run that progresses between
  limits, and a bare HEAD comparison would reset on the hold's own commit. RESOLVED (agent,
  2026-09-14, delegated): (c), default 6. F7 widens (c)'s ignored paths to the build folder's
  `BACKLOG.md` as well.
- **F5** — FACT-QUESTION · Does the desktop carrier outlive the session and the app? Probe: read both
  carriers' own tool contracts. The same read produced the negative for the keepalive carrier, which
  is the liveness of the probe. RESOLVED (agent, 2026-09-14, delegated): yes for the desktop pair —
  on-disk tasks, fired at next launch when due while closed — and no for the keepalive pair.
- **F6** — How is a verbatim copy of the example's carrier placeholders caught? (a) Extend
  `kit.toml`'s conf-placeholder discharge probe to both keys. (b) Ship the keys absent, so the render
  placeholder survives. (b) removes the keys' documentation from the example. RESOLVED (agent,
  2026-09-14, delegated): (a).
- **F7 — which changed paths does the no-progress test ignore?** Options:
  - (a) the run-state file only, as rev-2;
  - (b) the run-state file and the build folder's `BACKLOG.md`;
  - (c) the run-state file only, with the inherited-red policy unit's auto-file reusing an OPEN ask
    for the same leg and R.

  Under (a), the auto-file the inherited-red policy unit stages on every `gates-green`, committed
  before `--hold`, resets the streak on every hold of the one stop class that cannot progress in-run.
  (c) moves the fix into a unit ordered after this one and leaves the predicate open to the next
  record the machinery writes. RESOLVED (agent, 2026-09-16, delegated): (b). Rows filed about a stop
  are bookkeeping, not progress on the build. Duplicate asks are then bounded by
  `RESUME_SCHEDULE_LIMIT`.
- The rulings this unit executes: D12-i9 put a durable resume scheduler in this build, and the single
  owner turn ruled it on everywhere, the kit shipping it on and adopters opting out, recorded as a
  decision row — RESOLVED (owner, 2026-09-14).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds one edge the brief's table does not list, consumes-from
  unit 1, reciprocating that spec's hands-off to this one.
- rev-2 · 2026-09-14 · §2 S11 · §3 · §4 · §6 AC7 AC15 · §8 F6 · round-1 spec-audit fold (G1 M14,
  with H2's and M11's consequences here). `kit.toml`'s conf-placeholder discharge probe extends to
  `RESUME_SCHEDULE_(CREATE|DELETE)`, so a verbatim copy of the example reds (F6, AC15). Refusal rule
  1 and AC7 point at the lease matrix, whose no-id row now refuses after the HELD unit restored KF7.
  §3 names the held-suite baseline unit as the build's one unattended version move.
- rev-3 · 2026-09-16 · spec-audit round 2 fold.
  - G1 M8 (26): S5's no-progress test also ignores the build folder's `BACKLOG.md`, so an auto-filed
    ask no longer resets `hold-streak` (§4 data model, F7, AC6). F4's resolution now points at F7.
  - G1 M12 (9, 25, 41): AC15's fixture fills the keepalive keys and keeps only the resume
    placeholders, and is staged RED against the keepalive-only probe; S11 and §4 Rollout are
    corrected.
  - G1 M5 (27): the §4 scheduled prompt, S6, AC3 and AC8 pass the session's own `--keepalive-id`.
  - G1 H1 (2, 24): AC14 reads `verdict clean`, and the §3 consumes-from edge to unit 1 is updated.

## 10. Reuse audit

No existing seam fits the scheduling half. `python tools/codebase-map/reuse_lookup.py "schedule a
durable restart of a paused unattended run at a future time"` returned name-stem neighbours only —
`run`, `run_bounded` in the process monitor, the `.unattended.conf` affordance seam — and reports the
shell layer unscanned, so it is blind to the driver. Read by hand, the seams this unit extends are the
keepalive's: a tool pair declared in `.unattended.conf` and rendered into the Skill by
`tools/unattended/adopt-unattended.sh`'s placeholder substitution, with the driver recording and never
calling; plus unit 4's `--hold` write and take-over, and the driver's `observe_remote`. Recall
returned `TOOL-aPromptedMandate-11`, which is why every reap here is by name and read back rather than
presumed, and the aWrittenMethod enforcement pass's note that the harness scheduler fires only while
the session is idle. Where the design and the source disagree: design §22.1 says the kit default is
OFF; the later single owner turn ruled it on everywhere, and this spec follows the ruling.

M12 losses, each tested by reading the candidate's own contract: the keepalive's session-scoped
scheduler states jobs die with the session; a per-node operating-system task is a new install
location (M3 veto 2); a recorded carrier id needs a write the HELD phase does not allow.

Recall terms used: `keepalive resume scheduler CronCreate session-scoped reap HELD durable default-OFF blast-radius standing-configuration`
