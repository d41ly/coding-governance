# TOOL-aGraftedHelix-1 — the driver claims a run on the remote as a compare-and-swap ref, and refuses a live foreign claim

**Status:** CLOSED · rev-7 · 2026-10-05 · node a · Tier-2 · base 5266d22e · streams tooling · order 1 · advances TOOL-aReapedTicket-5 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-1-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-0-run-mandate.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-0-run-mandate.md) | journal | — |
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md) | journal | TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |
| [2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |

<!-- /gen:spec-records -->

## 1. Goal

The lease that says which session drives a run lives in `RUN.md` on the run's own branch, so two
nodes can `--preflight` one slug and learn it only at merge. This unit gives every run a claim on
the remote the landing push goes to: one ref per slug, written by compare-and-swap, renewed while
the run lives, given a terminal status when it ends, and read by every other node before it starts
or takes over a run. A live claim held by another session refuses a second driver, and a run that
does not hold its claim cannot close.

## 2. Scope (IN)

- **S1** — The claim record, interface I1 of the build's spec brief. The ref is
  `refs/gov/runs/<slug>` on the remote; its target is a parentless commit over the empty tree whose
  message is the subject `gov-claim <slug>`, a blank line, then the eight `key: value` lines §4
  "The claim record" pins. `status` is the closed set `live`, `held`, `landed`, `aborted`.
  Observed by AC2 and AC4.
- **S2** — `read_claims` reads every claim in ONE bounded fetch into the driver's private cache
  namespace `refs/gov/remote/runs/`, then ONE `for-each-ref` call and ONE date conversion for all
  ages, and derives a verdict per claim: `live`, `stale`, `held`, `terminal` or `unknown`
  (§4 "Verdicts"). It writes no `FETCH_HEAD`, no branch and no remote-tracking ref. Observed by
  AC1, AC2, AC3 and AC16.
- **S3** — `write_claim` writes one claim through `git push --porcelain
  --force-with-lease=refs/gov/runs/<slug>:<observed sha>`, with an EMPTY expected sha for a create,
  and reports exactly one of three outcomes: written, lost (the porcelain status line reads
  `stale info` or `fetch first`), or not completed (anything else, named). Every write it makes
  leaves the ref in place on the remote. Observed by AC4, AC6, AC9 and AC17.
- **S4** — `check_claim_writable` decides, from the claim this call read and the run's lease
  identity, whether the call may write, must refuse, or takes the claim over, by the table in §4
  "Who may write a claim". A take-over of a claim whose verdict is `stale` is a branch of its own at
  both take-over sites and prints a `claim taken over` line naming the previous node, session and
  beat age. Every cell of that table is driven by `TOOL-aGraftedHelix-12`'s arm (§3 Edges).
  Observed by AC4, AC5, AC7, AC8 and AC19.
- **S5** — `--preflight` reads the claims right after `observe_anchor`. A foreign `live`, `held` or
  `unknown` claim on this slug is check 89, joining the other preconditions through `status`. The
  write runs after the write gate and BEFORE the rotation and `scaffold_runmd`, so a lost race
  (check 90) or a write that did not complete (check 91) leaves the tree untouched. Observed by
  AC4, AC5, AC6 and AC17.
- **S6** — `check_single_live` widens its announcement: after the local records it lists the
  claims on the remote naming OTHER slugs whose verdict is `live`, `held`, `stale` or `unknown`,
  one line each, and stays silent at zero. A `terminal` claim is not listed. Observed by AC11.
- **S7** — `--resume`. The holder row reads its claim and renews it when due (§4 "Renewal"); the
  `--replaces` block and the LANDING re-bind write the new keepalive into the claim; `run_takeover`
  reads and writes the claim after the authorization block and BEFORE `write_lease`. A claim that
  another session holds `live` refuses the holder row with check 90 and the take-over with check
  89, each before any local write. Observed by AC7, AC8 and AC18.
- **S8** — `--dispatch` and `--close` read the claim as the holder and renew it when due. `--close`
  refuses with check 90 when the run does not hold its claim, a foreign `stale` one included, and
  with check 91 when the claim cannot be read, before any DoD item is graded. `--dispatch` refuses
  with check 90 the same way and writes no row. Observed by AC10 and AC19.
- **S9** — Status writes. `--hold` writes `held`, `--landed` writes `landed` and `--abort` writes
  `aborted`, each after its own `stage_or_fail` succeeds; under `LANDER_MODE=in-place`, where
  `--landed` stages nothing and only observes, it writes `landed` once that observation is written.
  A claim this call may not write, or a
  write that does not complete, is announced on one line and never fails the verb; the local record
  is the truth and the claim ages to `stale`. A terminal claim stays on the remote for the next run
  of the slug to take over. Observed by AC9 and AC20.
- **S10** — Two verbs. `--claims` (interface I2, no slug) prints one TAB-separated line per claim,
  `slug`, `node`, `status`, `beat-age-s`, `verdict`, sorted by slug, or the single line
  `claims: none`, and exits 2 with check 91 when the remote does not answer. `--beat <slug>` is the
  resume tick's heartbeat: it renews the claim of a run `--liveness` reads `LIVE` on this host,
  prints exactly one `beat —` line, and refuses nothing but a missing record. Both get a header
  invocation line, an argv arm and a `VERBS_SLUG` entry where they take a slug. Observed by AC1,
  AC2, AC3 and AC12.
- **S11** — `tools/unattended/resume-tick.sh` gains a `LIVE` row in its decision table: it runs
  `--beat <slug>` in the run's worktree and prints `beat · <the driver's line>`. `--dry-run` prints
  the row with ` (dry-run)` and runs nothing. Observed by AC12.
- **S12** — The loser's exit. A new core halt code, `claim-lost`, joins `HALT_CODES_CORE`, and
  `HALT_FLOOR` rises from 7 to 8 in `.unattended.conf` and in
  `tools/unattended/.unattended.conf.example`. Check 90's message names `--abort <slug> --code
  claim-lost` as the remedy. Observed by AC7.
- **S13** — The contract documents, edited only where the shipped text would otherwise be false:
  the `--preflight`, `--resume`, `--close`, `--dispatch`, `--hold`, `--landed` and `--abort`
  entries of `tools/unattended/VERBS.template.md` plus new `--claims` and `--beat` entries; §7 and
  the holder row of §8 in `tools/unattended/STOPS.template.md`; the holder sentence of the
  tick text in `tools/unattended/SKILL.template.md`, which also gains one invocation of each new
  verb; and one row for `RUN_CLAIMS` in the §8 key table of `tools/unattended/PROTOCOL.template.md`,
  because the kit gate's check 22 joins every key the shipped example conf declares to that table,
  and a declared key with no row is the false contract that check exists to refuse. The comment
  above `check_single_live` stops stating a count of the driver's verbs. The guides and the Skill
  are re-rendered by `tools/unattended/adopt-unattended.sh` in the same commit. Observed by AC13.
- **S14** — Every kit whose shipped bytes move is bumped once after the last move; the kickoff
  manifest re-stamps its `last-audit` because `.unattended.conf` is on its watch list; the
  unattended-stops dossier gains the claim paragraph. Observed by AC14.
- **S15** — The cost of one claim read and one claim write is measured on node `a` and recorded in
  the unit's acceptance ledger. Observed by AC15.
- **S16** — Claims land dark. `RUN_CLAIMS` is a closed `on`/`off` switch in `.unattended.conf`.
  Blank or absent reads `off`, with one `unattended: NOTE` line naming the key; any other value is
  refused by name, as `RESUME_SCHEDULE`'s is. The NOTE is printed by `--preflight`, the verb that
  starts a run, and by no other verb, so a verb that never touches a claim prints nothing new.
  Off, no verb reads, writes or refuses on a claim:
  `--preflight`, `--resume`, `--dispatch`, `--close` and the status writes behave as at base, and
  `--beat` prints a `skipped:` line naming the switch. `--claims` stays the remote reader either
  way. This repository's `.unattended.conf` declares `RUN_CLAIMS="on"`, and the shipped
  `tools/unattended/.unattended.conf.example` declares `RUN_CLAIMS="off"` with its comment.
  Observed by AC21.

## 3. Non-goals (OUT)

- **A lock against a malicious run.** A run holding the push credential can force or delete the
  ref. The claim stops an ACCIDENTAL second driver, as the lease does; protocol §9 already states
  what a check under the run's own uid cannot buy, and this unit adds nothing to that list.
- **Deleting claims.** A terminal claim stays on the remote. The next run of the slug takes it
  over, and the card hides old ones (`TOOL-aGraftedHelix-2`).
- **A second bound.** `live` and `stale` split on `RESUME_STALE_BOUND`, the bound `--liveness`
  already reads. The one new conf key is S16's switch, which decides whether claims run at all and
  bounds nothing; with it on, a host that refuses the namespace refuses `--preflight` with check 91,
  named.
- **`--liveness` and `--status` stay offline.** Neither reads the remote; `--claims` is the remote
  reader.
- **The hooks and their lease binder.** `run-lease.js`, the stop-guard and the stall-recorder bind
  to the run-state lease and are not edited; the claim is not a lease file.
- **The pre-push hook.** It belongs to another kit. Which of its branches a claim push takes, and
  with which invocation, is `TOOL-aGraftedHelix-10`'s (§3 Edges); the branch-bar residual is §5's.
- **The orientation card line** is `TOOL-aGraftedHelix-2`; the health log is
  `TOOL-aGraftedHelix-8`.
- **A gate leg over claims.** The claim is a remote fact; the unattended kit gate keeps grading the
  tree.

### Edges

- **hands-off** `TOOL-aGraftedHelix-2` — the `--claims` output it renders on the card: the single
  line `claims: none`, one TAB-separated row of five fields per claim with the verdict last, and
  exit 2 with a named refusal when the remote does not answer.
- **hands-off** `TOOL-aGraftedHelix-8` — the take-over of a claim whose verdict is `stale`, a
  branch of its own at both take-over sites, where that unit sits its `claim-taken-over` event.
- **hands-off** `TOOL-aGraftedHelix-10` — the claim push's target: `write_claim` pushes to the URL
  `resolve_claim_remote` prints, which the tracked pre-push hook refuses wherever
  `GOV_DEFAULT_BRANCH` is unset (round-1 audit finding 38). That unit pushes by the remote's name
  and observes the write through the hook.
- **hands-off** `TOOL-aGraftedHelix-11` — the identity a renewal writes: `write_claim_beat` and the
  holder renewals read the session from the environment, which the OS-scheduled tick running
  `--beat` does not carry (finding 39). That unit copies identity from the lease record.
- **hands-off** `TOOL-aGraftedHelix-12` — per-cell coverage of the §4 table that
  `check_claim_writable` implements: the refusing cells, `--beat`'s declined writes and every
  other cell §6 does not observe (findings 2, 3 and 46).
- **hands-off** `TOOL-aGraftedHelix-19` — the table's two axes as declarations: the eight claim-read
  rows and the four modes become driver constants beside `check_claim_writable`, which refuses a
  value outside them, so the per-cell arm derives its cells instead of typing them (round-1 audit of
  units 10 to 15, finding 31).
- **hands-off** `TOOL-aGraftedHelix-20` — the holder row's claim write that does not land: the CAS
  moved ahead of `write_lease`, and a `prior-session` lease fact the `mine` test accepts on the
  holder and status-write columns, so an "announce, continue" holder write cannot leave the run
  reading its own claim as foreign (round-1 audit of units 16 to 19, finding 9).
- **hands-off** `TOOL-aGraftedHelix-23` — where `check_claim_writable` reads the `prior-session`
  fact and how it compares it: read from the run-state file inside the function for every holder and
  status-write site, never handed in by a caller, and tested as membership in a set whose empty
  value is the cleared state (round-1 audit of units 20 to 22, findings 6, 12, 2, 7 and 1).

## 4. Design

### Evidence

Read at base `5266d22e`, product code byte-identical to `HEAD` (`git diff --stat 5266d22e HEAD`
touches only records).

- `observe_anchor` (`tools/unattended/unattended.sh:1562`) refuses unless exactly one remote exists
  (check 24) and fetch and push name one endpoint (check 25). It keeps the remote's NAME local.
- `observe_remote` (`tools/unattended/unattended.sh:439`) is the one bounded network call:
  `timeout -k 5s $REMOTE_BOUND` with credential prompts off, stdout to a file, stderr discarded.
- `write_lease` (`tools/unattended/unattended.sh:5557`) records `keepalive`, `session`, `pid`,
  `host`, `pid-image` and `lease-utc`; `read_host_name` lowercases `COMPUTERNAME` or `hostname`.
- `check_single_live` (`tools/unattended/unattended.sh:2205`) announces non-terminal tracked
  records of other slugs and is silent at zero.
- `verb_resume` (`tools/unattended/unattended.sh:6447`) decides holder, restart, replacement and
  take-over from local clocks; `run_takeover` (`tools/unattended/unattended.sh:6312`) re-verifies
  the authorization through `observe_anchor` and only then calls `write_lease`.
- `--hold`, `--landed` and `--abort` end in `stage_or_fail` at
  `tools/unattended/unattended.sh:5033`, `tools/unattended/unattended.sh:4653` and
  `tools/unattended/unattended.sh:4760`.
- The tick acts on `STALE` and `FINISHED-UNSTAMPED` only; every other verdict reaches the generic
  skip at `tools/unattended/resume-tick.sh:289`.
- No reader in the tree enumerates the remote's refs outside `refs/heads/` and `HEAD`: predicate
  `git grep -n 'ls-remote' -- tools .githooks skills ':!*.test.sh' ':!*selftest*'`, nine call
  sites, each asking for `HEAD`, `--heads`, one named head or the URL. A ref under `refs/gov/` is
  invisible to every one of them. Near-miss: three hits that are prose or a message string.
- The pre-push hook exits `skip-nondefault` for a push that does not touch the default branch,
  unless `GOV_BRANCH_GATE_CMD` is declared (`.githooks/pre-push:884-904`); this repo declares none.

### The claim record

```
gov-claim <slug>

slug: <slug>
node: <USERNAME, else USER, else absent>
host: <read_host_name, else absent>
session: <CLAUDE_CODE_SESSION_ID, else absent>
keepalive: <the run's keepalive id>
status: live|held|landed|aborted
lease-utc: <YYYY-MM-DDTHH:MM:SSZ, when this session took the claim>
beat-utc: <YYYY-MM-DDTHH:MM:SSZ, this write>
```

The commit has no parent, so the remote holds one object per claim and an old beat becomes
unreachable. The tree is the empty tree, written by `git mktree` from empty input, so the id is
right in a SHA-256 repository too. `lease-utc` is kept across a holder's renewals and reset by a
take-over. The values are the ones `RUN.md` facts 14 to 16 already push on the run branch, so the
claim publishes nothing the run did not already publish.

**Reading.** `observe_remote` runs `git fetch --no-tags --no-write-fetch-head --no-auto-maintenance
--prune <push url> '+refs/gov/runs/*:refs/gov/remote/runs/*'`. One `git for-each-ref` over
`refs/gov/remote/runs/` prints name, object and body for every claim, records split by a sentinel
line, and one `awk` parses them. Every `beat-utc` that matches the stamp shape goes through ONE
`date -u -f - +%s`; no claim spawns a process of its own
(`memory/gotchas/process-creation-is-the-suite-cost.md`). That call skips a line it cannot parse
and exits 1, so a count of answers that differs from the count asked is a dead probe, and every
age it should have given reads `unknown` rather than shifting onto the next claim. Measured on node `a` 2026-10-04: the glob
fetch of an empty namespace answered in 0.67 s with exit 0, so "no claim" is a successful read and
never a failure.

**The remote.** `resolve_claim_remote` sets `CR_NAME` and `CR_URL`, the name and the push URL of
the clone's one remote, and refuses through check 24's existing message otherwise; `observe_anchor`'s
own remote count calls it, so the predicate is spelled once. It SETS rather than prints because
check 24 is a `fail`, and a `fail` inside a command substitution would be captured as the URL with
its status lost. Reads and writes both use that URL, so they reach the endpoint the landing push
goes to.

**The claim commit's identity.** `write_claim` gives `git commit-tree` a fixed author and committer,
`gov-claim <gov-claim@invalid>`, so a clone with no configured identity can still write a claim and
the claim publishes no address the run's commits do not already carry.

**Which row a claim reads as.** The identity rows are tested first: none, then `mine`, then `same
session`, and only a foreign claim is read by its verdict. A claim of this run's own lease whose beat
the date call could not age is therefore `mine` with an UNKNOWN age, which is due, so a malformed
claim of another slug cannot wedge a holder that the one date call aged as `unknown` beside it.

### Verdicts

| claim | verdict |
|---|---|
| `status: live`, beat age at most `RESUME_STALE_BOUND` | `live` |
| `status: live`, beat age over it | `stale` |
| `status: held` | `held`, whatever its age; a hold is a released lease and its restart is a schedule |
| `status: landed` or `aborted` | `terminal` |
| any of the eight keys missing, `slug` disagreeing with the ref name, a status outside the set, or a `beat-utc` that does not parse | `unknown`, with `beat-age-s` printed as `-` |

### Who may write a claim

`mine` is a claim whose `keepalive` AND `session` equal the run's lease: the record's
`keepalive` and `session` facts, or at `--preflight` and in a take-over the values that call is
about to record (`absent` compares literally, so two absent sessions fall back on the keepalive). `same session` is a claim whose
`session` equals `CLAUDE_CODE_SESSION_ID` when that is not `absent`: the holder's own restart.
`foreign` is everything else.

| claim read | preflight | take-over | holder | status write |
|---|---|---|---|---|
| none | create | create | create | create |
| mine | renew | renew | renew when due | write |
| same session | rewrite | take | take | write |
| foreign `live` | check 89 | check 89 | check 90 | announce |
| foreign `held` | check 89 | take | check 90 | announce |
| foreign `stale` | take, announced | take, announced | check 90 | write |
| foreign `terminal` | take | check 89 | check 90 | write |
| `unknown` | check 89 | check 89 | check 90 | announce |

The take-over column's `held` cell is the HELD rows of the resume matrix, which already decided
the release; a foreign `terminal` claim there means another driver finished the slug, so taking it
would land it twice. The holder column refuses a foreign `stale` claim: a holder whose claim
another session took has lost it, and must `--abort --code claim-lost`. The holder's own restart is
the `same session` row, and `--replaces` compares the claim with the record's own facts, so it
reads `mine`. So the stale take-over happens at exactly the two take-over sites, `--preflight` and
`run_takeover`, which is where `TOOL-aGraftedHelix-8` logs it. "Announce" is one line naming the holder, `unattended: claim not written —
<slug> is held <status> by session <s> on <node>, beat <n>s`, and the verb goes on.

### Call sites

| site | mode | lost race | not completed |
|---|---|---|---|
| `--preflight`, after the write gate, before rotation | preflight | check 90, tree untouched | check 91 |
| `run_takeover`, before `write_lease` | take-over | check 90, nothing written | check 91 |
| `--resume` holder row, and its `--replaces` block | holder | check 90 | announce, continue |
| the LANDING re-bind | status write | announce | announce |
| `--dispatch` | holder | check 90, no row written | announce, continue |
| `--close`, before the DoD | holder | check 90 | check 91 |
| `--hold`, `--landed`, `--abort`, after `stage_or_fail` | status write | announce | announce |
| `--beat` | holder, on `LIVE` and this host only | `beat —` skipped, named | `beat —` skipped, named |

The holder and the resume paths keep working offline, as they do at base; every path that STARTS
or LANDS a run needs the remote, as `--preflight` and `--close` already do through
`observe_anchor`.

### Renewal

A holder renews when due: the claim's beat is at least `RESUME_STALE_BOUND / 4` old, or a field the
write would set differs. Otherwise it reads, confirms, and pushes nothing, so a lost claim is still
found on every call. With this repo's bound of 5400 s that is at most one push per 1350 s per run
from any one renewer. Renewers are the holder's `--resume`, which the idle-wake runs every tick,
`--dispatch` at each pass, `--close`, and `--beat`, which the out-of-process tick runs on a `LIVE`
verdict. The tick matters for a session waiting on one long Workflow: the idle-wake does not fire
then, and `--liveness` still reads `LIVE` from the sub-agent transcripts.

### The outcome of a write

`git push --porcelain` prints one status line per ref. `!` with `[rejected] (stale info)` or
`(fetch first)` is LOST: the ref moved between this call's read and its write. Any other `!` line,
no status line, or exit 124 is NOT COMPLETED, and the refusal carries git's reason or the exit
code. A pre-push refusal falls in the second class, so it is never reported as a race.

### The two verbs

```
$ bash tools/unattended/unattended.sh --claims
aGraftedHelix	daily-agent	live	312	live
dOldBuild	agent-0	landed	914002	terminal
```

`--beat <slug>` prints `unattended: beat — <slug> · renewed <beat-utc>` or
`unattended: beat — <slug> · skipped: <why>`, where `<why>` is the verdict, another host, a claim
not this run's, a beat not yet due, a remote that did not answer, or `RUN_CLAIMS` off. It writes only through the
`none` and `mine` rows of the holder column; every other row is a skipped line, because the tick
is not the driver and the run's own next verb decides a lost claim. It reads the verdict from the
same derivation `--liveness` prints and never re-derives it. Each verb's header comment says what
it does not check: `--claims` decides nothing about who drives, and `--beat` never writes a claim
its run does not hold.

### Inventory

New functions, each in cell `sh.function` and each asked of `python tools/lexicon/lexicon.py
--suggest <name> --as sh.function` on 2026-10-04, all `OK`: `resolve_claim_remote`, `read_claims`,
`check_claim_writable`, `write_claim`, `write_claim_beat`, `print_claims`. New checks 89, 90 and
91; the highest at base is 88. New core halt code `claim-lost`. New conf key `RUN_CLAIMS` (S16),
declared in both conf files. No new file, gate leg or lexicon verb, so no inventory key of the
codebase map is minted.

### The switch

Charter §1 lands Tier-2 behaviour dark, behind a default-OFF flag. The last kit behaviour that
shipped on, auto-resume, did so by an owner ruling with an opt-out (`TOOL-dDerivedDocket-5`); this
unit has no such ruling, so it ships off. Blank and absent both read `off`, so an adopter with an
existing conf is never exposed by a kit update. The run mandate's ruling that a claim push needs no
ask is what lets this repository turn it on.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/resume-tick.sh`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/STOPS.template.md`
- `tools/unattended/SKILL.template.md`
- `tools/unattended/PROTOCOL.template.md`, the §8 key table only
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/resume-tick.test.sh`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `.claude/skills/unattended/SKILL.md`
- `.unattended.conf`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/features/unattended-stops.md`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

### Rollout

Dark in every adopter: the shipped example conf declares `RUN_CLAIMS="off"`, and a conf without
the key reads off. In this repository the key is on, and a run preflighted before this lands has no
claim; its holder's next `--resume` creates one through the `none` row. With the switch on, a clone
whose remote refuses `refs/gov/` refuses `--preflight` with check 91 naming the porcelain reason,
which is the honest state: a run that cannot publish its claim cannot be told from a second driver.

### Alternatives rejected

The M12 test of the chosen mechanism is the probe the main loop ran on node `a` against the real
remote on 2026-10-04: an empty-expect `--force-with-lease` create succeeded, a second create was
rejected `(stale info)`, a CAS update on the observed sha succeeded, a delete succeeded, and the
pre-push hook passed all four without running a bar. The rejected second create is the negative the
probe could produce, and it is the mutual exclusion this unit needs.

- **A tracked lock file on a shared branch.** Loses on the same probe: a writer whose expected value
  is stale is rejected, and on one branch the expected value is the branch tip, which every slug's
  writer moves. Two runs of UNRELATED slugs then reject each other and retry. A branch push also
  takes the pre-push hook's branch path, where a declared branch bar runs per heartbeat.
- **A per-node presence file.** Loses on the same probe from the other side: each node writes its
  own name, so no write can ever be rejected by another node's, and the exclusion the probe
  observed cannot happen. Two nodes claim one slug and both succeed; readers learn it after the
  fact, which is the defect this unit exists to close.
- **`ls-remote`, then a fetch by sha.** Two round trips and a window in which the sha moves; a
  fetch by sha of an object no longer a tip is also host-dependent. The glob fetch is one round
  trip and gives the ref and its object together.

## 5. Production-readiness checklist

- security — The claim is advisory against an accidental second driver (§3). It publishes the
  `RUN.md` lease values the run branch already carries, and no secret. Every network call goes
  through `observe_remote`, so the credential prompt stays off and the wall-clock bound applies.
- perf / scale — A read is one fetch plus two local spawns; a write is three spawns plus the push
  and the pre-push hook's non-default exit. Measured on node `a` 2026-10-04: `--version` startup
  1.89 s, `ls-remote` 0.81 s, the empty glob fetch 0.67 s. AC15 records the read and write.
- error / empty / loading states — No claim reads `claims: none`. A remote that does not answer
  is check 91 or an announcement per §4, never an empty list. A claim that does not parse is
  `unknown` and refuses a take-over rather than inviting one.
- observability — `--claims`, the `claim taken over` line, the announce line, the `beat —` line
  and checks 89, 90 and 91, each naming node, session and beat age.
- risks — A session silent longer than `RESUME_STALE_BOUND` with no tick registered reads `stale`
  remotely and can be taken over by another node's `--preflight`; its next claim read refuses it
  with check 90, so at most one of the two closes. Two driver calls on one node fetching at once
  can contend on a ref lock; the loser reads as not completed. An adopter declaring
  `GOV_BRANCH_GATE_CMD` runs that bar on every claim push, and its stdin carries the
  `refs/gov/runs/<slug>` line so it can skip one. Selected bug classes, from
  `python tools/memory-tree/gotchas.py --for-paths` over the touched files: a TAB-separated row
  with an empty field collapses under `read` (`memory/gotchas/empty-field-collapses-unless-it-is-last.md`),
  so every field has a value and `unknown` ages print `-`; the CAS precedes every local write
  (`memory/gotchas/destructive-step-before-its-precondition.md`); one verdict derivation for
  `--claims`, the take-over and `--beat` (`memory/gotchas/second-implementation-is-not-a-second-opinion.md`).
- testing — Arms in the driver and tick suites, each observed RED on a staged break first: the lost
  race staged by a `git` shim on `PATH` that moves the ref before forwarding the push, never by a
  sleep (`memory/gotchas/fixed-sleep-does-not-place-a-signal.md`); claims seeded with real
  `gov-claim` messages, never a simplified shape
  (`memory/gotchas/staged-break-substitutes-a-synthetic-value.md`).
- migration — None: a run without a claim gets one at its holder's next `--resume`.
- user docs — The verbs and stops guides and the rendered Skill, re-rendered in the same commit.

## 6. Acceptance criteria

The fixture for AC1 to AC3 is a `git clone --local` of this repository under `%TEMP%`, whose one
remote is re-pointed at a bare repository beside it; claims are seeded with `git commit-tree` over
the empty tree and pushed to `refs/gov/runs/<slug>`.

- **AC1** — When `bash tools/unattended/unattended.sh --claims` runs in the fixture with no claim on
  its remote, stdout is exactly `claims: none` and the exit is 0.
  Red when: an empty namespace prints nothing or exits non-zero.
- **AC2** — When the fixture's remote holds a fresh `live` claim, a `live` claim whose beat is older
  than `RESUME_STALE_BOUND`, an old `held` claim, a `landed` claim and one whose message lacks
  `beat-utc`, `--claims` prints five rows of five TAB-separated fields sorted by slug, with verdicts
  `live`, `stale`, `held`, `terminal` and `unknown`, and `-` as the unparsed claim's age.
  Red when: the stale split ignores the bound, or the malformed claim reads `live` or `stale`.
  figure: the bound is DERIVED from the fixture's `.unattended.conf` at observation time.
- **AC3** — When the fixture's remote URL names a path that does not exist, `--claims` exits 2 and
  prints `UNATTENDED check 91 FAILED`.
  Red when: it exits 0 with `claims: none`, the empty answer this refusal exists to replace.
- **AC4** — When a run `--preflight`s in the driver suite's fixture, `refs/gov/runs/<slug>` on its
  remote names that session with `status: live`; a second `--preflight` of the slug from another
  clone under another session and keepalive exits non-zero with `UNATTENDED check 89 FAILED`
  naming the first node, session and beat age, and that clone has no run-state file.
  Red when: the second clone creates its record.
  cost: the suite's claim blocks run as a slice, prologue plus those blocks; the whole suite is
  the main loop's at VERIFYING.
- **AC5** — When the slug's claim is seeded `stale`, and again when it is seeded `landed`, a
  `--preflight` from a new session succeeds and the claim then names that session with
  `status: live`; the stale case prints `claim taken over`.
  Red when: either is refused, or the claim still names the old session.
- **AC6** — When a `git` shim on `PATH` moves `refs/gov/runs/<slug>` between the driver's read and
  its push, `--preflight` exits with `UNATTENDED check 90 FAILED` and the run-state file does not
  exist. Run once more on a slug whose prior run left a terminal record, the prior record is
  byte-unchanged and unmoved after the check 90.
  Red when: the record is created over a lost claim, or the rotation ran before the CAS.
- **AC7** — When the holder runs `--resume <slug> --keepalive-id <recorded id>` with its claim's beat
  older than a quarter of `RESUME_STALE_BOUND`, `beat-utc` moves; with a younger beat the ref's sha
  is unchanged; with the claim rewritten to another session `live`, the exit is non-zero with
  `UNATTENDED check 90 FAILED` naming `--code claim-lost`, and `--abort <slug> --code claim-lost`
  is then accepted. `grep -c '^HALT_FLOOR="8"$' .unattended.conf tools/unattended/.unattended.conf.example`
  reports 1 for each file.
  Red when: the holder writes over another session's live claim, `claim-lost` is refused, or a
  floor left at 7 lets the new code be dropped silently.
- **AC8** — When a different session's `--resume` reaches `run_takeover` on a presumed-stopped
  record whose claim another session holds `live`, it exits with `UNATTENDED check 89 FAILED` and
  the run-state file is byte-unchanged; with that claim `stale`, the take-over completes and the
  claim names the new session.
  Red when: a take-over writes the lease over a live foreign claim.
- **AC9** — When `--hold`, then a released `--resume`, then `--abort` run on a fixture run, the
  claim reads `held`, then `live`, then `aborted`, and `git ls-remote` still lists
  `refs/gov/runs/<slug>`; when the claim is another session's `live` one, `--abort` still exits 0
  and prints `claim not written`.
  Red when: a status write deletes the ref, or a foreign live claim fails the local abort.
- **AC10** — When `--close` runs on a run whose claim another session holds `live`, it exits with
  `UNATTENDED check 90 FAILED` before any DoD line, and no LANDING record is written.
  Red when: a run that does not hold its claim closes.
- **AC11** — When `--preflight` runs while the remote holds one claim of another slug per verdict,
  `live`, `stale`, `held`, `unknown` and `terminal`, its output lists the first four under
  `claim(s) on the remote` and not the terminal one; with none present, it prints no such line.
  Red when: a terminal claim is listed, a stale, held or unknown one is omitted, or the line
  prints at zero.
- **AC12** — When the tick suite's `LIVE` fixture runs `tools/unattended/resume-tick.sh`, the
  decision line reads `beat · unattended: beat —` and the fixture claim's `beat-utc` moved; with
  `--dry-run` the line ends ` (dry-run)` and the ref is unchanged.
  Red when: a `LIVE` run falls to `skip · verdict LIVE`, or a dry run pushes.
  cost: the tick suite's new block runs as a slice.
- **AC13** — When `bash tools/unattended/adopt-unattended.sh --check` runs after the edit, it exits
  0, and `grep -n -- '--claims' memory/guides/UNATTENDED-VERBS.md` finds the new entry. Each file
  read as one line, `tr '\n' ' ' < .claude/skills/unattended/SKILL.md | grep -c 'For the holder it writes nothing'`
  prints 0, and so does the same probe over `tools/unattended/SKILL.template.md`; both print 1 at
  base, observed before the edit. `awk '/^## 7\. /,/^## 9\. /' memory/guides/UNATTENDED-STOPS.md | grep -c claim`
  prints a non-zero count, against 0 at base.
  Red when: a template moved without its render, or the S13 sentences were never edited, which
  render parity alone passes.
- **AC14** — When `bash tools/check-kit-versions.sh` runs, it exits 0, and
  `python tools/govkit/govkit.py epoch --base 5266d22e` names no unattended carrier left behind.
  Red when: a carrier of the unattended version kept the old one.
- **AC15** — When one `--claims` read runs against the real remote on node `a`, and one claim write
  runs against a bare repository on node `a`, their wall times are recorded in the unit's acceptance
  ledger beside the bash process count. The write is not taken against the real remote in this pass:
  on node `a` the tracked pre-push hook refuses a push to a URL while `GOV_DEFAULT_BRANCH` is unset
  (round-1 audit finding 38), so a real-remote write through the driver cannot complete until
  `TOOL-aGraftedHelix-10` lands, and that unit observes the write through the hook.
  Red when: either figure is absent from the ledger.
  figure: PINNED at the build pass, with the date and node.
- **AC16** — When the remote holds a claim whose `beat-utc` is stamp-shaped but invalid,
  `2026-02-30T00:00:00Z`, sorting before a fresh `live` claim, `--claims` prints every claim whose
  beat went through that `date -u -f -` call with verdict `unknown` and age `-`. This is a separate
  fixture from AC2's, whose ages it would otherwise turn `unknown`.
  Red when: any claim of that call reads `live` or `stale`, or prints an age taken from another
  claim's beat.
- **AC17** — When a `git` shim on `PATH` makes the claim push print a `!` status line that is
  neither `stale info` nor `fetch first`, and again when it makes the push exit 124, `--preflight`
  exits with `UNATTENDED check 91 FAILED`, never check 90, and the clone holds no run-state file.
  Red when: a refused or timed-out push is reported as a lost race.
- **AC18** — When `--resume <slug> --replaces <old> --keepalive-id <new>` runs, the claim's
  `keepalive` is `<new>`, and a following `--resume <slug> --keepalive-id <new>` exits 0 with
  `git ls-remote <bare> refs/gov/runs/<slug>` unchanged while the beat is not due; this runs once
  with `CLAUDE_CODE_SESSION_ID` unset. When the LANDING re-bind meets the prior session's claim
  seeded `stale`, the claim then names the re-binding session's keepalive; seeded as a fresh
  foreign `live` claim, it prints `claim not written` and exits 0. When a holder `--resume` meets a
  claim carrying this `CLAUDE_CODE_SESSION_ID` under an older keepalive, the claim is rewritten and
  the exit is 0.
  Red when: the run wedges on its own replacement with check 90, or the `same session` row is
  read as foreign.
- **AC19** — When a `git` shim on `PATH` fails only the fetch of `refs/gov/runs/*` while the anchor
  read still answers, `--close` exits with `UNATTENDED check 91 FAILED` before any DoD line. When
  the claim is rewritten to another session `live`, `--dispatch` exits with `UNATTENDED check 90 FAILED`
  and the run-state file is byte-unchanged. When it is rewritten to another session `stale`,
  `--close` and `--dispatch` each exit with check 90 naming `--code claim-lost`, and the claim ref
  is unmoved.
  Red when: a close lands a claim it never read, a dispatch writes a row for a run another session
  drives, or a holder takes a successor's stale claim.
- **AC20** — When `--landed` runs on a fixture run whose claim is `live` and its own, the claim then
  reads `status: landed` and `--claims` prints it with verdict `terminal`. This is its own case,
  because AC9's sequence ends at a terminal `--abort`.
  Red when: a landed run's claim stays `live` and ages to `stale`.
- **AC21** — When the fixture's `.unattended.conf` has no `RUN_CLAIMS` line, `--preflight` exits 0,
  prints one `unattended: NOTE` line naming `RUN_CLAIMS`, and `git ls-remote <bare> 'refs/gov/*'`
  prints nothing. With `RUN_CLAIMS="maybe"` it refuses naming the key. In the tree,
  `grep -c '^RUN_CLAIMS="on"$' .unattended.conf` prints 1 and
  `grep -c '^RUN_CLAIMS="off"$' tools/unattended/.unattended.conf.example` prints 1.
  Red when: a conf without the key writes a claim, or an unrecognised value selects a default.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `kickoff-manifest ratchet` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the claim read, the verdicts, checks 89, 90 and
91, the status writes and the close refusal, each staged by reverting its branch · the suite's
floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · AC16 to AC21, each staged by reverting its branch:
the answer-count alignment, the non-race refusal class, the replace and re-bind writes, the close
and dispatch holder reads, the landed write and the switch · the suite's floor rises by its new
arm count

These arms observe the cells §6 names. Every other cell of the §4 table is driven by
`TOOL-aGraftedHelix-12`'s table-driven arm, which marks a cell no path reaches as unreached.

New arm: tools/unattended/resume-tick.test.sh · the LIVE row runs --beat, and --dry-run pushes
nothing · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`); the main loop runs them
once, through the kit's own runner, at VERIFYING.

## 8. Open questions

- **FACT-QUESTION · F1 — Does the remote enforce compare-and-swap on one ref?** Probe: the main
  loop's four pushes on node `a`, 2026-10-04 (§4 "Alternatives rejected"). Deciding observation:
  the second empty-expect create was rejected `(stale info)`. Liveness: that rejection is the
  negative the probe produced, so the probe could have answered no.
  RESOLVED (agent, 2026-10-04, delegated): a ref per slug written by `--force-with-lease`.
- **F2 — What does `node` carry?** The registry tag needs the governing doc's node registry, which
  this kit can reach only through a path it does not own or a new conf key. The build README's
  `node:` names the node that OPENED the build, which a take-over on another node makes false. The
  OS user is what the registry's Machine/user column keys a node by, and `host` sits beside it.
  RESOLVED (agent, 2026-10-04, delegated): `USERNAME`, else `USER`, else `absent`.
- **F3 — What verdict does a claim that does not parse get?** The brief pins four verdicts. Reading
  it as `stale` invites a take-over of bytes nobody understands; reading it as `live` names a state
  it does not have. The kit's rule for a clock that answers nothing is UNKNOWN, announced, and
  declining the take-over (`tools/unattended/STOPS.template.md` §7).
  RESOLVED (agent, 2026-10-04, delegated): a fifth verdict, `unknown`, which refuses like `live`;
  the card renders it (`TOOL-aGraftedHelix-2`), the only other reader of I2.
- **F4 — How does a session that lost its claim end?** The stop-guard refuses a turn end while the
  record is non-terminal and not HELD, so the loser must abort or hold. A hold waits for a release
  that never comes. An existing halt code would hide the cause from the status line and the gate.
  RESOLVED (agent, 2026-10-04, delegated): a new core halt code `claim-lost`, named in check 90's
  remedy, with `HALT_FLOOR` raised so it cannot be dropped silently.
- **F5 — What renews the beat?** Every holder call pushing costs a push per idle tick per run.
  Only `--resume` leaves a session inside one long Workflow reading `stale` after the bound.
  RESOLVED (agent, 2026-10-04, delegated): renew when due at a quarter of the bound, from the
  holder's `--resume`, `--dispatch`, `--close`, and the tick's `--beat` on a `LIVE` verdict.
- **F6 — May a status write fail its verb?** Failing `--abort` over a claim another session holds
  wedges the stop-guard on a run that is trying to end; failing `--landed` hides a landing that
  happened. RESOLVED (agent, 2026-10-04, delegated): status writes announce and never fail the
  verb; the starting and landing paths refuse.
- **F7 — Does the Skill template's holder sentence get edited?** The brief names three templates.
  The sentence "For the holder it writes nothing" in `tools/unattended/SKILL.template.md` becomes
  false the day this lands, and that template is not a governance carrier.
  RESOLVED (agent, 2026-10-04, delegated): edited, on the same rule as the three: only where the
  shipped text would otherwise be false.
- **F8 — Do claims ship on, or behind a switch?** Charter §1 lands Tier-2 behaviour behind a
  default-OFF flag. Shipping on needs an owner ruling of `TOOL-dDerivedDocket-5`'s shape, which
  this build does not have, and leaves an adopter whose remote refuses `refs/gov/` with a downgrade
  as the only way out. A switch that reads off when absent exposes no adopter at a kit update, and
  this repository turns it on. RESOLVED (agent, 2026-10-04, delegated): the `RUN_CLAIMS` switch of
  S16, off when blank or absent.
- **F9 — Does a holder take over a foreign `stale` claim?** Taking it contradicts §1 and S8, puts
  a take-over outside the two sites unit 8 logs, and lets a displaced holder close over its
  successor once the successor goes stale. Refusing it costs nothing: the holder's own restart is
  the `same session` row. RESOLVED (agent, 2026-10-04, delegated): the holder column answers a
  foreign `stale` claim with check 90 and the `claim-lost` remedy.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 1 and the driver at base
  `5266d22e`.
- rev-2 · 2026-10-04 · §3 §4 §6 §7 §8 §10 · S2 S3 S4 S5 S7 S8 S9 S16 · AC6 AC7 AC11 AC13 AC16 AC17
  AC18 AC19 AC20 AC21 · folded the round-1 spec audit's MEDIUM and LOW findings on this unit:
  finding 1 (AC16, the answer-count alignment); 4 (AC18, the replace and re-bind writes and the
  `same session` row); 5 (AC19, the close's check 91 and the dispatch's holder read); 6 (AC17 and
  the AC6 rotation variant); 7 (AC20, the landed write); 8 (AC13, sentence probes observed at
  base); 32 (the holder column's foreign `stale` cell becomes check 90, §8 F9, AC19); 46 (per-cell
  coverage handed to `TOOL-aGraftedHelix-12`, §7, and `TOOL-dDerivedDocket-40` cited in §10); 47
  (the `RUN_CLAIMS` switch, S16, §8 F8, AC21); and 9 (AC11 per verdict, and the quoted
  `HALT_FLOOR` grep in AC7). §3 gains hands-off edges to the units promoted from findings 38, 31,
  39, 2 and 3, and its pre-push sentence stops claiming the non-default exit.
- rev-3 · 2026-10-04 · §3 · §3 gains the hands-off to `TOOL-aGraftedHelix-19`, promoted from
  finding 31 of the round-1 spec audit of units 10 to 15, which declares this unit's table axes as
  driver constants. No cell, scope item or criterion of this unit moves.
- rev-4 · 2026-10-04 · §3 · §3 gains the hands-off to `TOOL-aGraftedHelix-20`, promoted from
  finding 9 of the round-1 spec audit of units 16 to 19, which widens this unit's `mine` test by a
  `prior-session` lease fact on the holder and status-write columns. No cell, scope item or
  criterion of this unit moves.
- rev-5 · 2026-10-04 · §3 · §3 gains the hands-off to `TOOL-aGraftedHelix-23`, promoted from
  findings 6, 12, 2, 7 and 1 of the round-1 spec audit of units 20 to 22, which makes
  `check_claim_writable` read the `prior-session` set itself on the holder and status-write columns.
  No cell, scope item or criterion of this unit moves.
- rev-6 · 2026-10-05 · §2 §4 §6 · S13 S16 · AC15 · the build pass's divergences, made in the spec
  before the code. S13 adds the `RUN_CLAIMS` row to the protocol's §8 key table, which the kit
  gate's check 22 requires of every key the example conf declares; the spec named three templates
  and missed that join. S16 places the NOTE on `--preflight` alone. §4 "The remote" makes
  `resolve_claim_remote` set `CR_NAME` and `CR_URL` rather than print, because check 24 is a `fail`
  and a command substitution would capture it as the URL and drop its status; `TOOL-aGraftedHelix-10`
  S1 reads "prints two TAB-separated fields" and takes the name from `CR_NAME` instead. §4 gains the
  claim commit's fixed identity and the order the rows are tested in. AC15's write moves to a bare
  repository on node `a`, because finding 38 makes a real-remote write through the driver
  uncompletable on this node until unit 10 lands.
- rev-7 · 2026-10-05 · §2 · S9 · the in-place `--landed`, which stages nothing, writes `landed`
  after its landing observation; S9 said only "after its own `stage_or_fail`", and this repository
  lands in place, so every landed run's claim would otherwise have aged to `stale` and been
  announced at every later `--preflight`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "claim a run across nodes on the remote so two nodes
cannot drive one slug"` ranked name-stem neighbours only and printed `unscanned layers: .sh`, so
no shell seam was visible to it and its miss is no evidence. The seams this unit extends were found
by reading the driver at base: `observe_remote` for every network call, `observe_anchor`'s check
24 (extracted into `resolve_claim_remote`), `write_lease` and `read_host_name` for the identity
values, `check_single_live` for the announcement, `verb_resume` and `run_takeover` for the take-over
order, `RESUME_STALE_BOUND` as the one bound, and the tick's `run_tick` for the out-of-process
renewal. The recall probe returned the one-lease-record ruling (TOOL-dDerivedDocket-61), the lease
unit (TOOL-aWokenSentinel-1), the announcement that replaced the single-live refusal
(TOOL-aUnblockedFleet-1), and the open staleness-bound ask this unit advances
(TOOL-aReapedTicket-5). Where a hit and the code could seem to disagree: STOPS §7 says nothing
refreshes the lease, and that stays true, because the claim's beat is a remote fact and never
restages the tracked record, which was that ruling's reason. Prior art for the per-cell coverage
this unit hands to `TOOL-aGraftedHelix-12` is the open ask `TOOL-dDerivedDocket-40`, which records
the same class for the resume matrix of `TOOL-dDerivedDocket-4`; it is cited here and carries no
header verb, because per-cell arms over this table move neither that guide nor its leg.

Recall terms used: lease keepalive preflight concurrent run announcement check_single_live double drive take-over resume matrix staleness bound remote anchor

The question passed with them: "how do two nodes learn that they are driving the same unattended
slug before merge, and what decided the lease and the concurrent-run announcement".
