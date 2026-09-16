# Spec briefs — aWokenSentinel, all seven units

**Serves:** journal TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7

What the SPEC stage's writers are handed, per unit. The orientation below was done by the run at
base `5f9648d6` (kit `unattended 1.24`); a writer verifies a line number against source before
citing it, because the driver is 5000 lines and moves. The design and every measured fact behind it
is `build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md` — read it whole first.

## Rules every spec obeys

- Shape: `memory/TEMPLATE-SPEC.md`, status header `**Status:** SPECCED · rev-1 · 2026-09-16 ·
  node a · Tier-2 · base 5f9648d6 · streams tooling · order <n>`. The `order` value is the unit
  number. Filename `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-<n>.md`.
  Every unit is Tier 2: each changes the unattended kit's contract (the manifest's tier rule).
- §6 acceptance names OBSERVATIONS — a command and what it prints, a staged red observed — never a
  path the unit will create. `tools/check-spec-tokens.py` grades every backticked path-shaped token
  in §6 against `git ls-files`, and the waiver file is shrink-only: name a file not yet built by its
  BASENAME without a directory, or in prose without backticks.
- §7 gates are what `--close` runs, NOT what the pass runs. State in §7: the pass verifies with the
  ONE check that exercises its change — a single test arm, a fixture, a grep over a rendered file —
  and nothing else. No `*.test.sh` suite whole, no `run-gates.sh`, no `GATE_*=` prefix, ever.
- §10 carries the recall terms used and the seam cited. The seam for every unit is named below.
- **A kit file names nothing outside itself by literal** (charter §12, `tools/hooks/README.md`): a
  hook derives its kit dir from `__dirname` and calls the driver beside it; a sibling kit is a render
  token. The install prefix of this repo is never spelled in a shipped file.
- A unit that edits a `*.template.*` file re-renders its output in the SAME commit with
  `bash tools/unattended/adopt-unattended.sh`; the parity legs byte-compare template and render.
- A unit that edits `.unattended.conf` (kickoff-manifest WATCH path) re-stamps `last-audit` in
  `memory/guides/SESSION-KICKOFF.md` in the same commit with a delta line in the commit message.
- Kit VERSION bumps are the closing pass's, once: unattended 1.24 → 1.25 across every carrier
  `bash tools/check-kit-versions.sh` names. A unit does NOT bump a version.
- Every new `fail <n>` branch in `tools/unattended/unattended.sh` needs an ARM in
  `tools/unattended/unattended.test.sh` asserting its literal text; `check-arms` is on the bar. The
  driver's `fail` high-water is 51 and the kit gate's `check` high-water is 48 at base — take the next
  free numbers. A unit observes its arm RED by running that arm's fixture alone, never the suite.
- Every new verb gets its entry in `tools/unattended/VERBS.template.md` (rendered to
  `memory/guides/UNATTENDED-VERBS.md`) in the same commit; check 26 joins the declared verb set to
  that file in both directions.
- **The sidecar root is ONE spelling, stated here so no two specs disagree:**
  `$(git rev-parse --git-dir)/unattended/` — the WORKTREE's git dir (where `gate-logs/` already
  lives), never the common dir, because a run lives in one worktree. Files inside it are named
  `<kind>.<slug>.log`, one JSON-compact or space-separated line per event, append-only, never
  tracked. The three kinds this build writes: `stop` (unit 3), `stall` (unit 4), `resume` (unit 5).
- **The lease facts are ONE spelling:** `session: <uuid|absent>` and `pid: <int|absent>` in the run-
  state file's `## Run facts` region, written only by the driver (unit 1). Every other unit READS
  them and never writes them.
- New conf knobs are read through the driver's `read_bound_key` (unattended.sh:358) — a kit default,
  ANNOUNCED on stderr when the project declares none, refused when not a positive integer — and
  documented in the shipped conf example the adopter renders. None of them is a REQUIRED key: an
  adopter on the previous kit keeps working with the announced default.
- Order is 1 → 2 → 3 → 4 → 5 → 6 → 7, and it is sequential: 3 and 4 share the adopter arm, the
  descriptor and the settings render; 5 reads 2's verb; 6 restates every earlier unit's vocabulary;
  7 reads 3's sidecar. `--dispatch` declares each pass's write set before it runs.

## Unit 1 — `TOOL-aWokenSentinel-1` — the run-state file records the LEASE (Tier 2)

**Defect.** The record names a cron job id and no session: the driver's `set_fact` keys are anchor-*,
base, branch-*, grain, halt-code, keepalive, landed-anchor, mode, phase, pieces, playbook, records,
units-at-landing, unpushed-at-landing, witness — measured over 56 records, none carries a session.
So nothing outside the session can find the session to resume. And `--keepalive-id` is accepted by
`--preflight` alone (`verb_preflight`, unattended.sh:2643), so a resumed session that schedules a
replacement job cannot record it — the Skill's `## Resume` tells the agent the record "cannot be
corrected in place" (`TOOL-cBriefedPilot-25`, `TOOL-aPrimedKeepalive-8`'s spec §1).

**Mechanism.** `verb_preflight`, right after `set_fact "$rel" keepalive "$kid"` (:2369 at an
earlier base — re-find it): `set_fact session` from `CLAUDE_CODE_SESSION_ID` and `set_fact pid` from
`CLAUDE_PID`, both measured present in a session's Bash env on node a. When either is unset, record
the literal `absent` and print ONE NOTE on stderr: this harness exposes no session id (or pid), so
no out-of-session resumer can find this run — the hooks and the tick then report it UNBOUND rather
than guess. `verb_resume` (:3079) gains the optional `--keepalive-id <id>`: on a NON-terminal record
it re-records `keepalive`, `session` and `pid` (the same three `set_fact` calls, so the resumed
session's lease replaces the dead one), prints what it replaced, and stages the file the way `--park`
does; on a terminal record it refuses through `refuse_if_terminal` (:1700). Without the option
`--resume` behaves as today. The scaffold's header comment (`scaffold_runmd`, ~:1541) lists what the
authored region holds — add the lease there, and grep every carrier for the "twelve facts" count
(`PROTOCOL.template.md` section 2 says the authored region "carries twelve facts") and make it
derive or correct it: a count typed beside the thing it counts is the class this repo names.

**Acceptance shape.** In the suite's fixture repo: `CLAUDE_CODE_SESSION_ID=abc CLAUDE_PID=4242
--preflight` → `grep -c '^session: abc'` and `'^pid: 4242'` both 1; with both unset → `absent` twice
and the NOTE text on stderr; `--resume <slug> --keepalive-id zzz` on a live record → `keepalive: zzz`
and the printed replacement line; on a terminal record → the refusal text. Each is one arm in
`unattended.test.sh`, observed red on a staged break of the one line it grades.

**Seam.** `set_fact` (:2876) and the `--preflight` option parser for `--keepalive-id` — extend the
parser to `--resume`, never a second parser. Recall terms: `keepalive id record preflight resume
run-state fact session pid lease replacement cannot be corrected in place`.

## Unit 2 — `TOOL-aWokenSentinel-2` — `--liveness <slug>`, the one predicate (Tier 2)

**Defect.** "Is this run alive" has no single answer. `--status` prints prose for a human; `--audit`
grades DISPATCHED UNITS against `UNIT_STALL_BOUND` (:2984-3070) and says nothing about the session
holding the run; `--preflight` alone knows that a LANDING record whose witness is an ancestor of the
anchor is a finished run missing a stamp (:1392). Six non-terminal records with CLOSED READMEs exist
today, so a reader keyed on `phase:` alone fires on all six forever.

**Mechanism.** A slug-addressed verb in `VERBS_SLUG` (:88), the header's invocation lines and the
dispatch `case`, read-only, exit 0 on any run-state file, printing `key: value` lines and nothing
else, in this order: `phase`, `state` (one of `terminal` — `is_terminal` (:613); `finished-unstamped`
— phase LANDING and the witness is an ancestor of the LOCAL default branch, the offline half of the
preflight predicate at :1374-1392, no network; `live` otherwise), `session`, `pid`, `pid-alive`
(`yes|no|unknown`: `tasklist //FI "PID eq <pid>"` under MSYS, `kill -0` elsewhere, `unknown` when
the pid fact is `absent`), `keepalive`, `last-move` (seconds since the NEWEST of: the newest file under
`<git-dir>/gate-logs/`, the newest `git status --porcelain` path's mtime and the last commit — the
same two joins `--audit` computes at :3040-3064, EXTRACTED into one function both verbs call, never a
third copy — and the session transcript when it can be derived: `~/.claude/projects/<cwd with every
`:`, `/` and `\` replaced by `-`>/<session>.jsonl`, the layout measured on node a), `last-stall`
(the last line of `<git-dir>/unattended/stall.<slug>.log` when that file exists, else `none` — unit
4 writes it; this unit only reads it), `stale` (`yes` when `last-move` exceeds `RESUME_STALE_BOUND`,
a new `read_bound_key` knob, default 5400 = the kit's `GATE_BOUND_DEFAULT` plus 1800, because a
healthy bar is 26 minutes of silence on every other signal and `GATE_BOUND` is the longest a bounded
command may run), and `verdict`: `TERMINAL`, `FINISHED-UNSTAMPED`, `UNBOUND` (session `absent`),
`STALE` (live, stale yes) or `LIVE`. A missing run-state file is a `fail <n>` with an arm; nothing
else refuses. The header states what it does NOT check: what the session is doing, whether a
process is hung — `tools/process-monitor/census.py` is the process-side probe where tracked.

**Acceptance shape.** Fixture records: a LANDED one prints `verdict: TERMINAL`; a LANDING one whose
witness is on the fixture's default branch prints `FINISHED-UNSTAMPED`; a BUILDING one with
`session: absent` prints `UNBOUND`; a BUILDING one with a session and every mtime older than the
bound (set `RESUME_STALE_BOUND=1` in the fixture conf) prints `STALE`, and with a fresh gate-log
file touched prints `LIVE`; the NOTE line for an undeclared bound appears on stderr once. One arm
each; the shared function's extraction is observed by `--audit`'s existing arms staying green.

**Seam.** `verb_audit`'s last-write/last-commit computation and `read_bound_key`. Recall terms:
`audit stall bound last-write last-commit dispatched unit idle PROGRESSING STALLED liveness
finished-unstamped witness ancestor`.

## Unit 3 — `TOOL-aWokenSentinel-3` — `stop-guard`, the `Stop` hook (Tier 2)

**Defect.** Four of six recorded stalls are class E: the run parked and ended its turn to wait for
an owner who had left. Nothing sees the act — the decision to stop — and the cron tick, when it
fires at all, hands a turn to an agent that asks again. Measured 2026-09-16 (research §6): a `Stop`
hook printing `{"decision":"block","reason":"…"}` continues the conversation with the reason
delivered as `Stop hook feedback:`; `Stop` fires for the MAIN agent only, a sub-agent fires
`SubagentStop`; and the stdin carries `session_id`, `stop_hook_active`, `last_assistant_message`,
`background_tasks` and `session_crons`.

**Mechanism.** `tools/unattended/stop-guard.js`, a `Stop` hook shipped with `stop-guard.fragment.json`
(`event: Stop`, no matcher — check `tools/settings-merge.py` and `tools/check-wiring.sh`'s fragment
reader accept an absent or empty `matcher` and extend them if they refuse; `tools/check-hook-
destinations.sh` picks the fragment up by its own enumeration) and `stop-guard.test.sh`. Behaviour,
in order, and the predicate is cheap where nothing is bound: read stdin JSON; resolve the memory
root from `.memory-tree.conf`'s `MEMORY_ROOT` under `CLAUDE_PROJECT_DIR` (default `memory`); scan
`builds/*/RUN.md` for a `session:` fact equal to the stdin `session_id` — none → exit 0 silently,
zero writes. Bound → call `unattended.sh --liveness <slug>` beside itself. Then: verdict
`TERMINAL` or `FINISHED-UNSTAMPED` → allow; `background_tasks` non-empty → allow, because the
harness re-invokes the session when a task completes and a blocked stop there is a wasted turn;
the block count for this session at or above `STOP_GUARD_BLOCKS` (a `read_bound_key` knob the hook
reads from `.unattended.conf` itself, default 12) → allow; else BLOCK, with a reason that names the
slug, the phase, the count `<n>/<N>`, and the absent-owner instruction verbatim: run `--plan <slug>`
and build the next READY unit, or `--abort <slug> --code <code>` if the run cannot proceed; never
end the turn by asking. EVERY stop on a bound session — allowed or blocked — appends one compact
JSON line to `<git-dir>/unattended/stop.<slug>.log`: utc, session, decision, reason-class, phase,
`background_tasks` count, and `session_crons` VERBATIM as the harness handed them. That last field is
unit 7's evidence. The block count is derived from that same file, never a second counter.
Honour `stop_hook_active`: it is true on every continuation and changes nothing here except that
the reason says so. The scan and the fact reader live in one sibling module (`run-lease.js`, say)
that unit 4 requires by `__dirname` — instance #2 is where the shared contract is extracted.
Wiring: the adopter arm at `adopt-unattended.sh:379-422` asserts ONE fragment by name; generalise
it to every `*.fragment.json` the kit dir ships, so unit 4's fragment is asserted by the same loop
and a fragment added later cannot ship unwired. Wire it in this repo with `python
tools/settings-merge.py --fragment tools/unattended/stop-guard.fragment.json`; the `.claude/
settings.json` render is part of the commit. Add the new files to `kit.toml`'s `[[files]]` rows the
way `gate-guard.*` are declared, and the test to the project-owned list.

**Acceptance shape.** `stop-guard.test.sh` arms, each feeding a stdin JSON and a fixture RUN.md,
observed red on a staged break: unbound session → no output, no sidecar; bound + BUILDING → block
JSON on stdout and one sidecar line; bound + LANDED → allow; bound + a non-empty `background_tasks`
→ allow with the sidecar line saying why; the twelfth block → allow; a sub-agent-shaped stdin
(`agent_id` present) is never delivered to this hook — assert the FRAGMENT's event is `Stop` and not
`SubagentStop` by grep, because the harness makes the split. `bash tools/unattended/adopt-unattended.sh
--check` green with the fragment wired; `bash tools/check-hook-destinations.sh` green.

**Seam.** `gate-guard.js`, `gate-guard.fragment.json` and the adopter's wiring arm — copy the shape,
not the predicate. Recall terms: `hook fragment settings-merge wiring adopter check gate-guard
PreToolUse sidechain marker matcher block reason stop`.

## Unit 4 — `TOOL-aWokenSentinel-4` — `stall-recorder`, the `StopFailure` hook (Tier 2)

**Defect.** A turn that ends on an API error — `rate_limit`, `overloaded`, `server_error`,
`max_output_tokens` — leaves nothing on disk that names the run. The transcript's last assistant
entry carries `isApiErrorMessage` (measured for an auth error only), which no reader of the run
consults. Four Tier-2 reviews died on limits and were found by a human reading a journal.

**Mechanism.** `tools/unattended/stall-recorder.js` with `stall-recorder.fragment.json` (`event:
StopFailure`; the docs list the matcher values, and the fragment declares NONE so every class is
recorded) and `stall-recorder.test.sh`. It requires the `run-lease` module unit 3 extracted, binds
the stdin `session_id` to a run the same way, and on a bound run appends ONE line to
`<git-dir>/unattended/stall.<slug>.log`: `<utc> <session> <error-class-or-unknown> <the whole stdin
JSON, compact>` — it assumes NO field beyond `session_id`, because the `StopFailure` stdin was never
measured; the raw line is what a later reader parses. Unbound → nothing. It prints nothing to stdout:
`StopFailure` discards hook output by documentation, so a hook that tried to block there would be
claiming an effect it cannot have. Zero API cost; it runs after the turn the API refused. The
adopter's generalised fragment loop from unit 3 asserts it wired; `.claude/settings.json` rendered;
`kit.toml` rows added.

**Acceptance shape.** Arms: bound + `{"session_id":…,"error":"rate_limit"}` → one sidecar line
carrying `rate_limit` and the compact JSON; bound + stdin with no `error` key → the line carries
`unknown`; unbound → no file; stdout empty in every case. `--liveness` on that fixture prints
`last-stall: <that line>` (unit 2's reader, exercised here by its one arm). Adopter `--check` and
`check-hook-destinations.sh` green.

**Seam.** The `run-lease` module and unit 3's fragment shape. Recall terms: `StopFailure API error
rate limit overloaded usage limit turn ended silently transcript isApiErrorMessage stall sidecar`.

## Unit 5 — `TOOL-aWokenSentinel-5` — `resume-tick.sh`, the out-of-process resumer (Tier 2)

**Defect.** Every recorded resume was a human starting a session. The one mechanism that can act
when the session is idle-on-error, hung, or dead is one that does not share its process: an
OS-scheduled tick. Measured: `schtasks /create /sc minute /mo 10` works unelevated (interactive-only);
`claude -p --resume <uuid>` returns the session's context under the same id and accepts
`--dangerously-skip-permissions`; `-p` warns after 3 s with no stdin; the CLI on node a is logged
in as of 2026-09-16; two concurrent resumers on one transcript both complete without corrupting it,
so the harm of a double resume is duplicated work, not a broken record.

**Mechanism.** `tools/unattended/resume-tick.sh [--repo <root>] [--dry-run]` and
`resume-tick.test.sh`. It derives its kit dir from `$0`, the repo root from `--repo` or `git
rev-parse --show-toplevel`, and walks `git worktree list --porcelain`; in each worktree, for each
`memory/builds/*/RUN.md` whose `session:` fact is not `absent`, it runs that worktree's
`unattended.sh --liveness <slug>` (the driver beside THIS script, invoked with `-C`-style cwd, since
the driver reads the conf of the tree it runs in). Decision per run, and `--dry-run` prints it and
exits: verdict not `STALE` → skip, one line naming the verdict; `STALE` and the attempts recorded in
`<git-dir>/unattended/resume.<slug>.log` reach `RESUME_ATTEMPTS` (knob, default 6) → skip with
`ATTEMPTS EXHAUSTED` and the last attempt's utc, which is the line an owner-notification would key
on (out of scope, backlog); else: `pid-alive: yes` → kill the recorded pid's TREE (`taskkill //PID
<pid> //T //F` under MSYS, `kill -- -<pgid>` elsewhere), because `TaskStop` and `timeout` leave
trees and a resumed turn re-stalls on the same contention; then `claude auth status` — not logged
in → print `SKIP — the CLI is not logged in on this node; nothing can resume <slug>` and exit 0
(an ANNOUNCED skip, never a pass); else append the attempt line and launch, DETACHED from the tick
so the scheduler's action returns: `cd <worktree> && claude -p --resume <session>
--dangerously-skip-permissions --max-turns <RESUME_TURNS, knob, default 40> "<CONTINUE payload>"
</dev/null`, stdout and stderr to `<git-dir>/unattended/resume.<slug>.<utc>.out`. The CONTINUE
payload is ONE string in this script: you are the resumed session of unattended run `<slug>`; first
run `bash <kit-rel>/unattended.sh --resume <slug> --keepalive-id <the cron id you schedule now,
per the Skill>` so this session's lease replaces the dead one; then continue from the phase the
run-state file names; the owner is absent — never park a question the protocol lets you decide,
take the option that makes no measured observable worse and record why; if the run is terminal,
reap the cron and stop. The `<kit-rel>` is derived, never spelled. Registration is the owner's, one
documented line per OS in the kit README (`schtasks /create /sc minute /mo 10 /tn gov-resume-tick
/tr '"<bash>" -lc "<abs tick> --repo <root>"'` and the crontab equivalent); `adopt-unattended.sh
--check` prints whether a task named `gov-resume-tick` exists as INFO, never red. A `--status` line
`resume-tick: <n> attempt(s), last <utc>|none` reads the sidecar.

**Acceptance shape.** `resume-tick.test.sh` with a STUB `claude` first on PATH that logs its argv
and answers `auth status` as instructed by an env var: fixture STALE record with a dead pid →
the stub was invoked with `--resume <session>` and the attempt line exists; LIVE record → not
invoked; attempts at the cap → not invoked, `ATTEMPTS EXHAUSTED` printed; stub says not logged in →
`SKIP` printed, not invoked; STALE with a live pid (a background `sleep` the fixture starts) → the
sleep is gone afterwards and the stub was invoked; `--dry-run` prints the decision and invokes
nothing. No arm runs the real `claude`.

**Seam.** `--liveness` (unit 2), `run_bounded` (:183) for the tick's own bounded calls, and the
Skill's keepalive prompt for the CONTINUE wording. Recall terms: `resume process death cross-node
takeover claude -p transcript session id schtasks tick attempts kill tree detached login`.

## Unit 6 — `TOOL-aWokenSentinel-6` — the contract (Tier 2)

**Defect.** The protocol's section 5 calls the cron job "the keepalive" and splits the obligation
between two actors; the Skill's `## Resume` says the record cannot be corrected in place; neither
names a mechanism outside the session. Every carrier that states the old shape becomes a
two-answers defect the moment unit 5 lands.

**Mechanism.** `tools/unattended/PROTOCOL.template.md` section 5 rewritten (render:
`memory/guides/UNATTENDED-PROTOCOL.md`): the cron job is the IDLE-WAKE — the agent schedules it as
the run's first act and reaps it, unchanged, and its limits carry a verified stamp: it fires only
while idle (documented), and is owner-reported on 2026-09-13, unmeasured, to stay silent while a
background task is pending; the KEEPALIVE is what wakes a run from outside its own turn — the
stop-guard at every turn end, the stall-recorder at every error end, the resume tick from the OS
scheduler — and the three actors are the agent (schedule, reap, run `--resume --keepalive-id` on
resume), the driver (record the lease, grade liveness, assert the reap), and the hooks with the tick
(refuse, record, resume). The CONTINUE payload rule is stated once: it forbids parking a question
the protocol lets the run decide and states the absent-owner default. The failure-domain rule from
the research is the section's opening sentence. `SKILL.template.md` (render `.claude/skills/
unattended/SKILL.md`): the keepalive section keeps `--audit` and adds the absent-owner instruction;
`## Resume` replaces "cannot be corrected in place" with `--resume <slug> --keepalive-id <id>`; one
short section names the two hooks and the tick, and points at the registration line in the kit
README rather than restating it. `README.md` of the kit: the registration lines and the sidecar
layout. `.unattended.conf` and the shipped example: the four knobs with their one-line rationale
each (`STOP_GUARD_BLOCKS`, `RESUME_STALE_BOUND`, `RESUME_ATTEMPTS`, `RESUME_TURNS`) — the units that
read them added the keys; this unit adds the prose. The kickoff manifest re-stamp for the watched
conf. `memory/map/features/unattended.md`: prose refreshed for the hooks and the tick (the DoD's
"dossier prose refreshed on touch"). The charter template's `Unattended runs` block points at the
protocol and does not change. Grep every carrier for `keepalive` and `cannot be corrected` before
declaring the set complete — `TOOL-dUnstalledConvoy-16` is the class where one carrier is fixed
and the others ship the refuted sentence.

**Acceptance shape.** `grep -c` of the new section-5 opening sentence in the template AND the
render; `grep -c 'cannot be corrected in place'` is 0 in the Skill template and render; `bash
tools/unattended/adopt-unattended.sh --check` green; `bash tools/unattended/check-unattended.sh`
green (it byte-compares protocol and render); `python tools/codebase-map/map_diff.py` reports the
dossier fresh; the manifest stamp advanced.

**Seam.** Section 5 of the protocol template and the Skill's two keepalive sections. Recall terms:
`protocol section 5 keepalive agent obligation actor split driver records reaps resume presumed
alive Skill render parity two answers one question`.

## Unit 7 — `TOOL-aWokenSentinel-7` — `keepalive-reaped` becomes CHECKED (Tier 2)

**Defect.** `keepalive-reaped` is agent-attested: `--close` greps `^keepalive-reaped: (yes|true)`
(:3909) and nothing can contradict it. `TOOL-aPromptedMandate-11` (OPEN since 2026-08-18): a run
attested it twice while `CronList` showed both jobs firing. Measured 2026-09-16: the `Stop` hook's
stdin carries `session_crons` — the store no script could reach — and unit 3 records it verbatim on
every stop.

**Mechanism.** The Skill's order is reap, then `--close`, in ONE turn; the stop that records the
post-reap listing ends that turn, so `--close` cannot read it. The verb that runs on the NEXT turn
is `--landed`: it reads the LAST line of `<git-dir>/unattended/stop.<slug>.log` and, when that
line's `session_crons` still names the recorded `keepalive` id, REFUSES with a `fail <n>` naming the
id and the utc the harness listed it at — the attestation is contradicted by the harness's own
listing. No sidecar, or a last line older than the record's LANDING phase change, → the attestation
stands and `--landed` prints `keepalive-reaped: attested, unchecked — no stop-guard record after the
close`. `--status` gains one line, `keepalive: <id> · last harness listing <utc>: present|absent|
unrecorded`. `--close`'s DoD row for `keepalive-reaped` says `attested; checked at --landed`. The
backlog row `TOOL-aPromptedMandate-11` is CLOSED in this unit's commit, citing the evidence.

**Acceptance shape.** Arms: a fixture stop log whose last line lists the recorded id → `--landed`
refuses with the id and utc; last line listing nothing → passes that arm; no log → the
`unchecked` line; the `--status` line in all three shapes. Observed red on a staged break.

**Seam.** `--landed`'s refusal ladder and `--status`'s line printer; the stop sidecar unit 3
defines. Recall terms: `keepalive-reaped attestable not checkable CronList firing forever
attestation read-back list verb landed status`.
