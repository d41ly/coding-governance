# TOOL-dDerivedDocket-5 — auto-resume from HELD

**Status:** SPECCED · rev-5 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 5

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
  when defaulted, and refused when not a positive integer: the driver reads each through
  `read_bound_key`, as it reads `GATE_BOUND`, so each is a call and neither is a new `case`.
  Observed by AC1, AC2 and AC13.
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
- **S8** The Skill carries the agent's half. The hold step issues `{{RESUME_SCHEDULE_DELETE}}`
  against the printed name, going on when no task has it, then files the printed schedule with
  `{{RESUME_SCHEDULE_CREATE}}` under that name, because a task an ended hold filed can still hold
  the name (§8 F10). A take-over pushes its record before any other work, so a schedule on another
  node meets rule 3 of §4. The Resume section issues `{{RESUME_SCHEDULE_DELETE}}` against the name,
  going on when no task has it, as after an `owner` hold, which owes none. It does so only AFTER a
  take-over's `--resume` succeeds and its record is pushed, never before that `--resume`, and never
  when it refuses or prints `still held`, so a manual resume before an `after` hold's instant leaves
  the owed restart filed (§8 F9). A resume that refuses or prints `still held`,
  scheduled or manual, leaves the named task in place, reaps the keepalive it scheduled for the
  take-over, reads its scheduler's listing back to confirm the reap, and stops (§8 F8). With the
  switch `off` the render writes a fixed "not scheduled" literal in place of both tool keys.
  Observed by AC9 and AC10.
- **S9** The `keepalive-reaped` attestation covers the resume schedule too. `--close` and `--abort`
  name every schedule the record's hold history owed, beside the keepalive id, so the agent attests
  over a list it was shown. No new DoD item: the core DoD count is the asks-disposed unit's to move.
  Observed by AC11.
- **S10** The contract text — keys, fire rule, streak, refusals, carrier requirements — goes to
  unit 4's companion guide `UNATTENDED-STOPS.md`. The protocol gains one sentence in §5 pointing at
  it, and the verb carrier documents `--scheduled`. The GROSS growth on
  `memory/guides/UNATTENDED-PROTOCOL.md` and on its template is at most 300 bytes, which covers that
  sentence and ONE key-table row carrying this unit's five conf keys joined in a single first cell.
  That row is OWED and not optional: check 22 of `tools/unattended/check-unattended.sh` joins §8's
  table against `tools/unattended/.unattended.conf.example` and reds on a key declared in one and
  missing from the other. This unit lands NET ZERO OR NEGATIVE on that carrier and spends
  none of the shared headroom: it FUNDS those bytes by trimming §8's own table, which is the region
  it grows. The passage it trims, named precisely so that no sibling unit trims the same text: the
  declaration rationale in the `RECALL_CLI` cell at
  `tools/unattended/PROTOCOL.template.md:482`, opening "A DECLARATION rather than a path in the
  driver, because a kit literal", 196 bytes, together with its back-reference and the write-only-log
  provenance in the `MAP_CLI` cell at `tools/unattended/PROTOCOL.template.md:483`, 313 bytes. The
  two move TOGETHER, because the second sentence reads "for the same reason its sibling is one" and
  is unreadable apart from the first, and they go to `tools/unattended/README.md`, the kit README,
  which carries no size row in `tools/template-size-limits.txt` and owns kit prose. Each cell keeps
  its MEANING and its OPTIONAL terms; only the argument for the declaration form leaves. Neither
  moved sentence carries a kit-path literal, so the shipped-surface ban does not move. That is 509
  bytes trimmed against at most 300 added. No cap is raised: raising one is an owner turn, and the
  other units of this build draw on the same 1,116 bytes, which this unit leaves intact. Anything
  past the 300 stays in the companion guide, which draws on its own cap.
  Observed by AC10 and AC16.
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
  this unit's verification reads: `verdict clean`, with every inherited suite filed.

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
not match.

Every hold of a slug files under that one name, so the Skill's hold step deletes the name before it
files, and goes on when no task has it: gov's carrier keeps a fired one-shot listed, disabled, under
its id (§8 F10). The delete loses nothing a hold owes. `--hold` refuses on a HELD record, so any task
under the name belongs to a hold that has already ended, and rule 2 below refuses it on `held-at`.

The prompt the driver prints, and the agent files verbatim:

```text
Resume the unattended run for build <slug>. Work only in the git worktree at <absolute toplevel>.
Load the unattended skill and follow its Resume section with: --resume <slug> --scheduled <held-at> --keepalive-id <the id of the keepalive you schedule first>.
If the driver refuses or prints still held, delete the keepalive you scheduled for this resume, list your scheduler's jobs to confirm it is gone, leave the scheduled task named <name> in place because a later hold may have filed it, and stop.
```

Every interpolated value has a validated shape: the slug passed `check_slug`, the toplevel came from
`git rev-parse --show-toplevel`, and `held-at` matched the hold's own timestamp grammar. The hold
reason is free text and never reaches the prompt, because a durable prompt executes later in a
session no one watches.

The `--keepalive-id` placeholder is fixed prompt text, not an interpolated value. The scheduled
session fills it with the keepalive its own scheduler created, because the HELD unit's take-over
refuses a missing id.

The last line reaps that keepalive because nothing else would. A keepalive left firing after a
refusal ticks `--resume <slug> --keepalive-id <own id>` as its first act (the HELD unit's F6), and on
a HELD record that call goes down the take-over row with no `--scheduled`, so it skips rules 2 to 4
below, rule 3 among them. A `still held` resume writes nothing and takes no lease, so it leaves the
same job firing and reaps it the same way (§8 F8).

The same line leaves the named task alone. A session refused because a later hold began would
otherwise delete, under the one name every hold of the slug shares, the restart that later hold
filed. The Skill deletes the task only after a take-over's `--resume` succeeds (§8 F9).

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
`tools/unattended/kit.toml` · the three test files named in §7 · `tools/unattended/README.md`,
which receives the trimmed §8 rationale · the rendered guides and Skill ·
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
  run HELD with the owed line naming a task that does not exist, which a manual restart clears; a
  manual resume that prints `still held` leaves the owed task filed (§8 F9), while a scheduled
  resume refused under rule 3 or 4 has spent its one-shot and leaves the hold to a manual restart.
- observability — the three `--hold` lines, the `--status` owed line, the `scheduled` field on the
  take-over history row, and the schedule names at `--close` and `--abort`.
- risks — a cross-node take-over that has not pushed yet is invisible to rule 3, so for that window
  two nodes can drive one slug; the Skill's take-over step pushes the record first to shrink it. A
  scheduled session that stops on a permission prompt is a stalled restart, visible in the app. Two
  slugs differing only in case map to one name.
- testing — `tools/unattended/unattended.test.sh`, `tools/unattended/check-unattended.test.sh` and
  `tools/unattended/adopt-unattended.test.sh` arms, each staged RED in the pass, plus one hand
  observation with a real carrier; the suites run under unit 1's attribution at the build's one
  post-build bar.
- migration — additive facts, read as absent on every existing record. Adopters decide at their
  own upgrade (§4 Rollout).
- user docs — the companion guide section, the protocol §5 pointer, the verb carrier row and the
  Skill steps.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` grades a fixture conf declaring
  `RESUME_SCHEDULE="maybe"`, it reds naming the key and the legal set; with the key absent it reports
  the effective value `on` as defaulted and does not red on that account.
  Red when: an unrecognised spelling resolves silently to either value.
- **AC2** — When `bash tools/unattended/check-unattended.sh` grades a fixture conf declaring
  `RESUME_SCHEDULE_CREATE` equal to `KEEPALIVE_CREATE`, it reds naming both keys.
  Red when: the session-scoped keepalive tool is accepted as the durable carrier, so every restart
  dies with the session it was filed to outlive.
- **AC3** — When `--hold` runs on a HELD-capable fixture with `--until "after <future instant>"` and
  the switch on, the record gains `resume-owed` naming `unattended-resume-` plus the lower-cased slug
  and that exact instant, `--hold` prints the name, instant and prompt lines, the prompt spelling
  `--keepalive-id` and a last line that, on a refusal or `still held`, deletes the keepalive the
  session scheduled, listing the scheduler's jobs to confirm it, and leaves the named task in place,
  and `--status` prints the owed line.
  Red when: the fire instant is computed as `held-at` plus the delay for an `after` hold, so a
  usage-limit hold restarts into the same limit; or the prompt's refusal line does not delete the
  keepalive, so the job the scheduled session filed first keeps ticking a take-over that none of the
  scheduled-resume refusals guards; or it deletes the named task, so a session refused because a
  later hold began deletes that hold's restart, filed under the same name.
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
  permission: the arms are written and staged RED in the pass; the suite that executes them,
  `tools/unattended/unattended.test.sh`, sits on no bar leg at all, so the run that executes them is
  the VERIFYING run's attributed
  `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` and not its
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, which carries no leg for that
  suite.
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
  the rendered tree, `--scheduled` is carried by the verb guide; the Skill's hold step deletes the
  printed name with the delete tool and then files it with the create tool; its resume section
  deletes that name only after a take-over's `--resume` succeeds, and not before that `--resume` or
  on its refusal or `still held` branch; that branch, for a scheduled or a manual resume, leaves the
  named task in place, reaps the keepalive the session scheduled for the take-over and reads the
  scheduler's listing back before it stops; and the companion guide renders byte-identical to its
  template.
  Red when: the resume section never deletes the schedule, so a manual restart leaves a durable task
  that later fires into a live run; or it deletes the schedule before `--resume`, or on a refusal or
  `still held`, so a manual resume before an `after` hold's instant leaves the run HELD with no
  restart filed while `--status` names a deleted task; or the hold step files without clearing the
  name, so its create meets an id an ended hold's disabled one-shot still holds; or a refused resume
  stops with its new keepalive still scheduled, so that job's first tick takes the HELD record over
  with no `--scheduled`, past the remote-freshness refusal a schedule filed on another node relies
  on.
  permission: both run over the rendered tree rather than a fixture, so they are gate legs and are
  observed at the build's one post-build bar.
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
  permission: the leg runs over the real tree rather than a fixture, so it is observed at the
  build's one post-build bar.
- **AC14** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs at the
  build's one post-build bar, its attribution summary reads `verdict clean`: no NEW FAIL, no `DEAD PROBE at L`
  and no `OVER BUDGET at L`. Every suite it reports with INHERITED lines or `DEAD PROBE at R` is
  named by its file path in a filed backlog row or ask that is not CLOSED, as
  `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'` shows.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it; or the run is
  read by its NEW count alone, so a suite this unit's change aborted before its first FAIL line, or
  pushed past its budget, reads as clean; or an inherited failure is attributed away with no record
  filing it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: the run drives the unattended self-test suites, which `memory/guides/BUILD-METHOD.md`
  M6 keeps out of a unit pass, so it is the run the main loop makes at VERIFYING, after the
  last unit: the attributed `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>`
  made beside that run's `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, which
  carries no leg for these suites at any flag setting. This folds the conservative reading of
  the parked ruling conflict and decides nothing.
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
- **AC16** — When `git cat-file -s` reads `memory/guides/UNATTENDED-PROTOCOL.md` at this unit's
  build commit and at that commit's first parent, the build-commit size is NOT GREATER than the
  parent's and is below the 61440-byte guide cap declared in
  `tools/memory-tree/check-memory-hygiene.sh`. The same two readings hold for
  `tools/unattended/PROTOCOL.template.md`. The trim is taken and landed:
  `grep -c 'A DECLARATION rather than a path in the driver' tools/unattended/PROTOCOL.template.md`
  counts 2 at the parent and 0 at the build commit, and both sentences are present in
  `tools/unattended/README.md`; the `RECALL_CLI` and `MAP_CLI` cells still state their meaning and
  their OPTIONAL terms. The owed key-table row arrived:
  `grep -c 'RESUME_SCHEDULE' tools/unattended/PROTOCOL.template.md` counts 0 at the parent and 1 at
  the build commit, the one joined cell. The companion guide `UNATTENDED-STOPS.md`, which receives
  this unit's contract text, is read the same way at the build commit and is below the same
  61440-byte guide cap.
  Red when: the §5 pointer restates the contract, so the companion and the protocol answer one
  question twice and the 1,116 bytes the build's units share are spent here; or five separate
  key-table rows are written where one joined first cell carries all five keys; or the size is read
  against the figure written in this spec rather than against the parent commit, so a sibling's
  landing hides this unit's overspend; or the `MAP_CLI` sentence is moved without its sibling, which
  leaves a back-reference pointing at nothing; or the trim is taken and the text lands in no
  destination, which DELETES the argument rather than moving it; or the cap is raised to make the
  text fit, which is an owner turn; or the five keys reach §8's key table in no row at all, which
  reds check 22 of `tools/unattended/check-unattended.sh` on the next bar; or the companion is measured only in prose, so text pushed out of the
  protocol lands in a carrier nobody reads the size of.
  permission: a read, a byte count and two greps, no gate leg and no suite.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `playbook validity gate` · `memory hygiene` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · HELD fixtures for each fire rule, the streak limit, and a scheduled resume against a moved and an unreachable local bare remote · the driver suite's executed-assertion floor
New arm: `tools/unattended/check-unattended.test.sh` · fixture confs with an unrecognised switch value and a carrier equal to the keepalive tool · the leg suite's executed-assertion floor, by the branches added
New arm: `tools/unattended/adopt-unattended.test.sh` · an on conf with no carrier declared · none

The observation that a real carrier accepts the printed name and instant, and accepts that name
again after a delete of it (§8 F10), is made once, by hand, in this unit's pass with gov's declared
pair, and recorded in the unit's journal. No gate can make it.

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
  record the machinery writes. The inherited-red policy unit's §8 F8 has since adopted (c)'s reuse
  on its own side, so a repeated hold over one leg red at one R files no second ask. It does not
  make (b) redundant: a hold after R advances still files a new ask, which (a) would count as
  progress. RESOLVED (agent, 2026-09-16, delegated): (b). Rows filed about a stop are bookkeeping,
  not progress on the build. With the reuse in place, `RESUME_SCHEDULE_LIMIT` bounds only the asks
  filed as R advances.
- **F8 — what stops the keepalive a refused take-over scheduled from driving the slug?** The
  scheduled prompt, and the HELD unit's Resume rule for a manual take-over, both schedule a keepalive
  before the `--resume` that may refuse, and nothing reaped it at rev-3. Its tick runs
  `--resume <slug> --keepalive-id <own id>`, which on a HELD record takes the take-over row with no
  `--scheduled` and so skips rules 2 to 4 of §4; rule 3 is the double-drive this unit exists to stop.
  A `still held` resume writes nothing and leaves the same job firing. Options:
  - (a) reap it in the contract text: the prompt's last line, S8's Skill step and the HELD unit's
    Resume rule delete the keepalive the session scheduled for the take-over and read the listing
    back, whenever that resume refuses or prints `still held`;
  - (b) a lease-matrix row making a keepalive tick's `--resume` on a HELD record refuse rather than
    take over.

  (b) needs the driver to tell a tick from a deliberate restart, and both pass the same arguments,
  so it needs a new input. (a) adds no driver surface; its reap is agent-attested, as every
  keepalive reap is (§3). RESOLVED (agent, 2026-09-16, delegated), decided by the orchestrator: (a), observed here
  by AC3 and AC10 and in the HELD unit by its AC11.
- **F9 — when does the Skill delete the durable schedule a hold owes?** As the round-2 fold's second
  pass left S8, every resume path deleted it before the keepalive reap, and in the HELD unit's
  take-over rule that reap comes before `--resume`. A manual resume on an `after` hold before its
  instant therefore deleted the schedule, printed `still held`, reaped its own keepalive under F8
  and stopped: the run stayed HELD with nothing filed to restart it, and `--status` still printed an
  owed line naming the deleted task. Options:
  - (a) delete it only after a take-over's `--resume` succeeds, never before that `--resume`, and
    never on a refusal or `still held`, scheduled or manual;
  - (b) keep the early delete, and on `still held` have the manual take-over re-file the owed
    schedule from the `--status` owed line before it stops.

  (b) leaves a window between the delete and the re-file in which a stopped session loses the
  restart, and the re-file needs the prompt, which the `--status` owed line does not print. (a)
  leaves a restart filed until the resume it was filed for has happened. A task firing into a run a
  manual take-over made live, before that take-over deletes it, meets rule 1 of §4 and refuses, and
  the refusal leaves it listed for that take-over's own delete, or, when that delete never runs, for
  the next hold's clear (F10). A scheduled resume refused under rule 3 or 4 has spent its one-shot
  either way, so leaving its task in place loses nothing.
  RESOLVED (agent, 2026-09-16, delegated), decided by the orchestrator: (a), observed here by AC3 and
  AC10 and in the HELD unit by its AC11.
- **FACT-QUESTION · F10 — does the hold step need the name cleared before it files?** Every hold of a
  slug files under one name, and §4's carrier requirements say nothing about a name already taken;
  under F9 a refused or `still held` resume leaves its task in place. Probe: read the tool contract of
  gov's declared carrier pair. The observation that decides: whether a create under a taken id
  replaces the task there, and whether an ordinary run leaves ids taken, as a fired one-shot that
  stays listed would. Liveness: the same read can show a create that replaces a taken id, under
  which the clear is unnecessary. RESOLVED (agent, 2026-09-16, delegated): yes. The
  contract, read again 2026-09-16 on node `d`, says a one-time task disables itself after it fires
  rather than leaving the list, sends a change to an existing task to its update tool rather than its
  create tool, and leaves a deleted task's prompt file on disk. So the hold step deletes the name,
  going on when no task has it, before it files (S8). The delete loses nothing a hold owes, because
  `--hold` refuses on a HELD record, so a task under the name belongs to a hold that has ended. The
  contract does not say whether a create under a deleted id succeeds; §7's hand observation makes it.
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
- rev-4 · 2026-09-16 · round-2 fold, second pass. The verifier problem on units 5 and 4, a
  keepalive left firing after a refused take-over, decided by the orchestrator as option (a): the
  §4 scheduled prompt's last line and S8's Skill step delete the named task and then reap the
  keepalive the session scheduled, reading the listing back, when the resume refuses or prints
  `still held`, and §4 says why. AC3 checks the printed prompt and AC10 the rendered Skill. New §8
  F8. Unit 4's Resume rule carries the same clause, and its AC11 checks it. Spec-audit round 2
  fold, third pass, from the second pass's verifier problem on units 5 and 4, a manual resume on an
  `after` hold deleting the owed schedule, decided by the orchestrator as option (a) and recorded as
  new §8 F9: S8's Resume section deletes the named task only after a take-over's `--resume`
  succeeds, and a refusal or `still held`, scheduled or manual, leaves it in place, which withdraws
  the task delete this line's second-pass half gave the §4 prompt's last line and S8; §4 says why,
  and the prompt's last line now leaves the task in place. The hold step clears the name before it
  files, from a read of the carrier's contract (new §8 F10, S8, §4 The name and the prompt, §7).
  AC3's prompt line and AC10's Skill steps and `Red when:` clauses follow, and §5 names the
  `still held` state. §8 F7's reasoning says the inherited-red policy unit's §8 F8 adopts the
  OPEN-ask reuse F7 rejected as (c) here, and F7 keeps (b). Fold verification: S8's Resume delete
  goes on when no task has the name, as after an `owner` hold, and F9 says a task that fires into
  a take-over's live run before that take-over's delete is removed by that delete.
- rev-5 · 2026-09-16 · regrounded on fb07ca25 (origin/main). §2 S1's two numeric keys are read
  through `read_bound_key`, the helper TOOL-aProbedUnit-3 hoisted `GATE_BOUND`'s `case` into, whose
  header makes a later bound key a call. §10 gains a paragraph describing fb07ca25: the Skill's
  keepalive tick now runs `--audit`, where §4 and §8 F8 read the HELD unit's F6 tick, which the
  HELD unit keeps as the tick's first act with `--audit` second; the Resume section gained a
  `/session-kickoff` step (TOOL-aReplayedCard-3); AC15's probe still reads the keepalive-only
  alternation; and the protocol render's guide-cap headroom shrank to 1116 bytes, which S10's
  sentence and the leg check 22 key-table rows for S1's keys both spend. No S-item landed on main.
  AC14's unit-end run, which meets the gate-guard hook TOOL-aDeferredBar-3 landed, and the check 22
  rows S10 does not name, are reported to the orchestrator and not decided here.
  Extended 2026-09-20, regrounding consolidation, folding the conservative reading of that parked
  conflict and not deciding it. AC14 now reads the attributed run at the build's one post-build
  bar, the run the main loop makes at VERIFYING after the last unit, and §5 testing and the §3
  consumes-from edge to the baseline unit follow it;
  AC7, AC10 and AC13 gain `permission:` lines, AC7 because its arm lives in a held suite and the
  other two because they run a leg over the real or rendered tree. AC1, AC2, AC9 and AC15 keep
  their in-pass observation: each grades a FIXTURE, which M6 names as a pass's own direct check,
  and AC9's `--check` is on the hook's read-only list. S10 now states the 300-byte MAXIMUM this
  unit adds to the protocol, including the one joined key-table row check 22 may owe, and new AC16
  reads the file's size at the pass against the 61440-byte guide cap; no cap is raised. Re-priced
  to NET ZERO on 2026-09-20, on the orchestrator's ruling that a unit adding bytes to a capped
  carrier funds them itself: S10 now names the passage this unit trims — the declaration rationale
  in §8's `RECALL_CLI` and `MAP_CLI` cells, 509 bytes together, to `tools/unattended/README.md` —
  and AC16 reds if either carrier grew against this unit's parent commit rather than allowing 300
  bytes of growth. §7's
  `tools/unattended/unattended.test.sh` arm names the driver suite's executed-assertion floor
  instead of `none`; the `check-unattended.test.sh` arm's third field stopped naming the
  `check-unattended.sh` arms and now names the leg suite's executed-assertion floor, which is the
  `FLOOR_ASSERTIONS` its added branches move, and
  `tools/unattended/adopt-unattended.test.sh` pins none, so its `none` is correct. No criterion of
  this unit asserts a phrase counts zero, so the could-not-fail sweep found nothing here.
  Extended again on 2026-09-20, closing pass. The orchestrator ruled the check 22 key-table row
  OWED rather than pending, so S10 drops the conditional and states the joined row as a cost this
  unit carries inside its own 300-byte ceiling, which its 509-byte trim over-covers; AC16 now
  witnesses the row arriving, reds if the five keys reach no row, and reads the size of the
  companion guide this unit's contract text lands in, which is what a carrier with more than 2048
  bytes free owes under the same ruling. AC7's `permission:` line names
  WHICH run covers it: the suite holding its arms is on no bar leg, so the attributed
  `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` run covers it and
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` does not. Rule 1's narrow
  reading is ratified; AC2 now says in its first clause that the checker grades a FIXTURE conf,
  which it always meant, so no reader takes it for a real-tree run, and AC1, AC9 and AC15 stand.
  Closing verifier, same pass and rev: the `permission:` line of the criterion that reads the
  attributed run now names that run in the orchestrator's own terms, because
  `tools/gate-legs.json` carries no leg for `tools/unattended/unattended.test.sh` or
  `tools/unattended/check-unattended.test.sh` at any flag setting, so "the build's one
  post-build bar" alone would have read as a bar that covers them.

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

At fb07ca25, the base since rev-5, none of `--hold`, HELD, the lease, the `RESUME_SCHEDULE` keys or
`--scheduled` exists on main, and what did land bears on the seams above. The driver reads
bound keys through `read_bound_key` (`tools/unattended/unattended.sh:358`), which S1's two numeric
keys call. The Skill's keepalive section makes the tick's prompt `--audit <slug>`
(TOOL-aProbedUnit-3), while §4 and §8 F8 read the HELD unit's F6, a tick whose first act is
`--resume <slug> --keepalive-id <own id>`. The HELD unit composes the two: its rewritten keepalive
section keeps that `--resume` as the tick's first act and `--audit <slug>` as its second, so F8's
premise stands, and a change there to the tick's first act reopens F8 here. The
Resume section gained a `/session-kickoff` step after the reap and the re-schedule
(TOOL-aReplayedCard-3), which a scheduled session follows like any resume. `tools/unattended/kit.toml`
still probes the `KEEPALIVE_(CREATE|DELETE|INTERVAL)` alternation AC15 stages RED against, and
`memory/guides/UNATTENDED-PROTOCOL.md` sits 1116 bytes under its 61440-byte guide cap, where it sat
3625 under at `abac6d59` (PINNED 2026-09-16, `wc -c`). S10's one sentence spends from it, and so
does the §8 key-table row that leg check 22 joins against the example conf for each of S1's five
keys (`tools/unattended/check-unattended.sh:1689`), a row S10 does not yet name. The
wired gate-guard hook (`tools/unattended/gate-guard.js`) denies `run-unattended-gates.sh` and any
`*.test.sh` suite while this branch's record is before `VERIFYING`, so AC14's run could not have
executed inside a pass as rev-5 first wrote it. The 2026-09-20 consolidation moved it to the
build's one post-build bar; the ruling conflict with D12-i8 behind that move is the orchestrator's.

M12 losses, each tested by reading the candidate's own contract: the keepalive's session-scoped
scheduler states jobs die with the session; a per-node operating-system task is a new install
location (M3 veto 2); a recorded carrier id needs a write the HELD phase does not allow.

Recall terms used: `keepalive resume scheduler CronCreate session-scoped reap HELD durable default-OFF blast-radius standing-configuration`
