# TOOL-aRepatriatedFork-5 — pre-push runs only a tracked, unmodified gate command

**Status:** SPECCED · rev-1 · 2026-09-23 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close a security hole in the push boundary. Gov's `.githooks/pre-push` runs whatever `GOV_GATE_CMD`
names as the merge bar, so `GOV_GATE_CMD=true` lands a commit over a red bar and prints a decision
line indistinguishable from a real full run. NicoCares already carries the fix; this unit takes it
upstream, arms it, and makes the declared test escape unable to produce a recorded landing.

## 2. Scope (IN)

- **S1** — The hook accepts a non-empty `GOV_GATE_CMD` only when every path-shaped word in it names a
  file tracked at the pushed tip, each such file's working copy hashes to that blob, the first word is
  a tracked script or one of the interpreters `bash` or `sh`, and no option word precedes the first
  path-shaped word. Anything else is refused at exit 1 before the bar runs. The rules are nc's
  rev-3 guard (`.githooks/pre-push:556-652` at nc), taken without change. Observed by AC1, AC2 and AC3.
- **S2** — The decision line names the bar on both arms, as `— bar: <label>`, and the run-log END line
  carries a `bar` key whose value is `default`, `tracked` or `stub`. Observed by AC4 and AC5.
- **S3** — `GOV_GATE_CMD_TEST=1` is the ONE declared escape. It waives S1, labels the decision line
  `bar: STUB <command>`, and records `bar stub`. Observed by AC4 and AC6.
- **S4** — `tools/push-main.sh` writes no `LANDER_MARKER` for a push made under `GOV_GATE_CMD_TEST`,
  and says so, so a stub-gated push can never become an unattended `LANDED`. Observed by AC6.
- **S5** — Gov's own harnesses that stub the bar with an untracked script declare the escape:
  `.githooks/pre-push.test.sh`, `.githooks/pre-push.runlog.test.sh` and `tools/push-main.test.sh`.
  Observed by AC7.
- **S6** — The red-first control in `.githooks/pre-push.test.sh:355-357` reads a gov commit, so at any
  adopter it calls `bad` and reds the suite. It becomes an announced SKIP when that commit does not
  resolve, which is nc carve-out 25's form. Observed by AC8.
- **S7** — The prose that states the old contract is corrected: `AGENTS.md:534` says `GOV_GATE_CMD`
  "overrides the gate for testing", and `tools/unattended/PROTOCOL.template.md:542-543` lists
  "overriding the gate command" among what the kit does not close. Observed by AC9.

## 3. Non-goals (OUT)

- `--no-verify`, a `core.hooksPath` pointed at an empty directory, and a PATH that shadows `bash`,
  `sh` or `git`. Each bypasses the hook as a whole. The protocol already names the first two as open,
  and this unit leaves them there.
- `BASH_ENV`. Measured in §4 Threat model: it bypasses gov's hook and nc's hook alike, before either
  runs a line, and it can forge every artifact this unit protects. It is recorded as a residual of the
  protocol's shim class rather than fixed, because the hook is itself a bash script and cannot defend
  against the environment its own interpreter reads first.
- inCMS's project-owned hook. It carries the same class under another name and is handed off below.
- The refusal-token file and the lander's classification of a refusal. Those are
  `TOOL-aRepatriatedFork-8`, which consumes the refusals this unit adds.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-8` — the machine-readable refusal channel; this unit's refusals must reach push-main as tokens, and 8 writes that channel
- **hands-off** external — inCMS's project-owned `.githooks/pre-push:158-159` runs `eval "$INCMS_PUSH_GATE_CMD"` unguarded and needs the same rule until inCMS adopts gov's hook; an inCMS backlog row, minted by the inCMS session that takes it

## 4. Design

### Threat model

**Actor.** An agent session with shell access in a clone that pushes to the shared default branch,
most sharply an unattended run, which may land with no owner turn (`CLAUDE.md` ARCH-aWeighedAssay-3
at inCMS, `tools/unattended/PROTOCOL.template.md`).

**Capability.** It sets environment variables on the command that runs `git push` or
`tools/push-main.sh`, and it can write files in the working tree.

**What it can forge today.** A landing on the default branch over a red bar, with evidence that
reads as a gated landing:

1. the hook's decision line, `pre-push: FULL gate on main push (<sha>) — no recorded full green`,
   byte-identical to a real run's except for the sha;
2. a run-log END line with `decision full` and `rc 0`;
3. push-main's `landed … by push-main` lander marker, which `unattended.sh --landed` reads as the
   landing having gone through the sanctioned lander.

**Preconditions.** A push to the default branch with the `push-main-active` marker present and the
pushed tip checked out, which is exactly what `tools/push-main.sh` arranges.

**Why it matters though `--no-verify` exists.** The protocol's model is that an unauthorized
landing must be a visibly deliberate act (`tools/unattended/PROTOCOL.template.md:524-525`).
`--no-verify` leaves no decision line and no run-log END; `GOV_GATE_CMD=true` launders the bypass
through the knob the hook documents, and leaves the evidence of a real bar. This is the class
`TOOL-aStandingWrit-4` ruled on for `GOV_DEFAULT_BRANCH`: a classifier that takes the name of the
thing it classifies from the environment is a fail-open, not an override.

### The exploit path, from the code

- `.githooks/pre-push:445-447` sources `.githooks/gate-env.sh`, which could also set the variable.
- `.githooks/pre-push:528-531` prints the decision line naming the scope and not the bar.
- `.githooks/pre-push:546` reads `gate=${GOV_GATE_CMD:-bash $GOV_KITROOT/run-gates/run-gates.sh}`.
- `.githooks/pre-push:547` runs `$gate`, and `:550` exits with its status.
- `tools/push-main.sh:95-133` sees `git push` succeed and writes the lander marker.

Reproduced 2026-09-23 in a scratch repo and bare remote under the session scratchpad, with gov's hook
installed through `core.hooksPath` and a default bar that prints `REAL BAR RAN - RED` and exits 1.

| hook | environment | rc | remote moved | decision line |
|---|---|---|---|---|
| gov a7c78ad2 | none | 1 | no | `FULL gate … no recorded full green`, then the red bar |
| gov a7c78ad2 | `GOV_GATE_CMD=true` | 0 | yes | `FULL gate … no recorded full green`, and no bar ran |
| gov a7c78ad2 | `BASH_ENV=<file holding exit 0>` | 0 | yes | none |
| nc f69e2ffb | `GOV_GATE_CMD=true` | 1 | no | `REFUSING - GOV_GATE_CMD names no script at all` |
| nc f69e2ffb | `BASH_ENV=<file holding exit 0>` | 0 | yes | none |

nc's own `scripts/pre_push_bar_selftest.py`, pointed at gov's hook in a scratch copy, reports
9 failures: cases 1-8 and the mutation anchor M0. The same file passes at nc.

inCMS's project-owned hook, reproduced the same way with `INCMS_PUSH_GATE_CMD=true`: rc 0, remote
moved, under the line `pre-push: main push touches code — running the full gate (scripts/gate.sh)...`.

### What the fix buys, and what it does not

It makes the documented knob unable to substitute a bar silently. A value that is not a reviewed,
unmodified tracked script is refused before anything runs. The declared escape still lands, and it
labels itself on the decision line, in the run log and by the absent lander marker.

It does not make the push boundary tamper-proof against an actor who controls the environment.
`--no-verify` and a redirected `core.hooksPath` skip the hook and leave no decision line and no
run-log END. `BASH_ENV` is worse and is stated plainly: it runs the actor's own file inside the hook's
interpreter and inside push-main's, so it can print a forged decision line, exit 0 from the hook alone
and let push-main write a genuine lander marker. It is a shim of the tools this kit calls, which the
protocol already lists as open at `tools/unattended/PROTOCOL.template.md:541-542`, and it requires
the actor to author and point at a file of its own. What this unit closes is the case where no such
act is needed: the knob the hook itself documents, set to a four-letter word.

### Data model

The run-log END line gains one key, `bar`. `tools/runlog/README.md:29` states that a reader keeps a
line carrying an unknown key, so no reader changes.

| value | when |
|---|---|
| `default` | `GOV_GATE_CMD` empty; the kit's own runner ran |
| `tracked` | `GOV_GATE_CMD` passed S1 |
| `stub` | `GOV_GATE_CMD_TEST` waived S1 |

The four hostile values AC2 names, in nc's order. Each landed at rc 0 on some vintage of nc's guard.

| value | defeated |
|---|---|
| `bash <untracked>/stub.sh` | no tracked-name rule at all (rev-1 and earlier) |
| `gatepayload scripts/unattended-bar.sh` | a rule reading only path-shaped words (rev-2) |
| `bash -c gatepayload scripts/unattended-bar.sh` | a rule ignoring an interpreter option (rev-2) |
| `bash scripts/unattended-bar.sh`, working copy rewritten | a rule reading the blob name, not its bytes (rev-2) |

Two refusals are added, each writing `RUNLOG_DECISION=refuse-bar` and exiting 1 before the bar:
a value naming no script, and a value failing any S1 clause. Their messages are nc's, with
`$GOV_KITROOT` kept in the sanctioned-use hint.

### Placement

The guard sits between the forcing predicates and the decision line, at `.githooks/pre-push:527`,
so `$main_local` is resolved, `gate-env.sh` has been sourced and the decision line can name the
bar. It runs only on a default-branch push, which is the only push that runs a bar.

### Inventory

Identifiers minted, each in the shell-variable cell: `bar_label`, and the loop scratch
`_bar_tok`, `_bar_bad`, `_bar_first`, `_bar_opt`, `_bar_seen`, `_bar_dirty`, `_w`, `_wt`, `_bl`,
all nc's spellings. One run-log decision value, `refuse-bar`. One run-log key, `bar`. One
environment name, `GOV_GATE_CMD_TEST`, which nc already exports.

### Migration

| adopter | record | disposition |
|---|---|---|
| nc | the untagged guard block, `.githooks/pre-push:538-652` (`PKG-dCandidLodestar-5`) | gov bytes carry it |
| nc | `nc carve-out 14/24`, `.githooks/pre-push:299` | gov bytes; audit-D §3 measured gov's probe order deriving `scripts` at nc |
| nc | `nc carve-out 15/24`, `.githooks/pre-push:444-457`, and the `15/20` comment at `:21` | gov bytes; the scrub is gov's `:34` |
| nc | `nc carve-out 25/24`, `.githooks/pre-push.test.sh:431-448` | gov bytes after S6 |
| nc | arms 25-29b, `.githooks/pre-push.test.sh:274-341`, and the escape at `:18-21` | gov bytes after S5 and the new arms |
| nc | `scripts/push-main.test.sh:22-26` | gov bytes after S5 |
| nc | `scripts/pre_push_bar_selftest.py` | kept by nc, or retired if the owner takes F2's recommendation |
| nc | census denominator, `scripts/check-nc-wiring.sh:260-269` | falls by three in the same commit |
| inCMS | `.githooks/pre-push`, role `project-owned` (`kits.json` `role_dispositions`) | unchanged by this unit; see the external edge |

nc's `.claude/skills/unattended/SKILL.md:904` names `GOV_GATE_CMD='bash scripts/unattended-bar.sh'`,
a tracked script, so nc's one sanctioned consumer passes S1 unchanged.

### Rollout

One gov commit. `.githooks/pre-push` is `core.hooksPath`-resolved from the PRIMARY tree
(`.githooks/pre-push:7-18`), so the guard binds a clone's pushes once its primary tree checks the
change out. No kit version constant exists for push-main (`tools/govkit/entries/push-main.kit.toml:7`),
so no marker moves; the unattended kit bumps for S7's template edit.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/pre-push.runlog.test.sh`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`, `tools/unattended/check-pass-order.sh`, `tools/unattended/check-brief-recorded.sh` (the `KIT_UNATTENDED_VERSION` bump)
- `AGENTS.md`
- `tools/gate-legs.json` (a leg for the ported bar self-test, if F2 lands that way)

### Alternatives rejected

- **Delete `GOV_GATE_CMD`.** It has a sanctioned consumer at nc and every hook harness depends on it.
- **Accept only one named script.** A repo's bar is its own choice; the tracked-and-unmodified rule
  is what separates a reviewed bar from a substitute, and it needs no per-repo list.
- **Refuse `GOV_GATE_CMD_TEST` in the hook when an unattended run is live.** The hook cannot see run
  state cheaply, and S4 already denies the stub the one artifact a landing claim needs.

## 5. Production-readiness checklist

- security — this unit. The threat model and the residuals are in §4 and repeated in §3.
- perf / scale — one `git cat-file -e` and one `git hash-object` per path-shaped word, only when
  `GOV_GATE_CMD` is set, only on a default-branch push.
- error / empty / loading states — an empty `GOV_GATE_CMD` is the default path and is not a refusal;
  every refusal names the word that failed and the sanctioned spelling.
- observability — the decision line and the run-log `bar` key.
- risks — a legitimate adopter bar spelled with an interpreter option, for example `bash -e bar.sh`,
  is refused. nc measured its live tree and found no such value; gov has none.
- testing — the nc harness's cases and its three-arm mutation, ported; see §7.
- migration — none for data; adopters exporting an untracked stub must add `GOV_GATE_CMD_TEST=1`.
- user docs — `AGENTS.md:534` and the protocol template line.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture pushes with `GOV_GATE_CMD=true`, `.githooks/pre-push` exits 1
  with `names no script at all` and the remote does not move; the a7c78ad2 hook exits 0 and moves it.
  Red when: the hook still runs an unvetted value.
- **AC2** — When the fixture pushes with each of the four hostile values in the §4 evasion table,
  `.githooks/pre-push` refuses each before the named command prints anything.
  Red when: any one of the four lands; they are nc's rev-1, rev-2 and rev-3 evasions in order.
- **AC3** — When the fixture pushes with `GOV_GATE_CMD` naming `bash` and a bar script the fixture
  tracks unmodified, `.githooks/pre-push` lets the push land and the decision line carries `bar: bash`
  followed by that script's path.
  Red when: the guard refuses a legitimate bar, which would make AC1 and AC2 prove only that it
  refuses everything.
- **AC4** — When the fixture pushes under `GOV_GATE_CMD_TEST=1` with an untracked stub, the push lands
  and the decision line carries `bar: STUB `.
  Red when: the escape waives the check without saying so.
- **AC5** — When a default-branch push completes, the last `pushes.log` END line carries `bar default`,
  `bar tracked` or `bar stub` matching the case.
  Red when: the run log still cannot tell a stubbed landing from a gated one.
- **AC6** — When `tools/push-main.sh` lands under `GOV_GATE_CMD_TEST=1` in a fixture declaring
  `LANDER_MARKER` in `.unattended.conf`, no marker file is written and push-main prints why.
  Red when: a stub-gated push leaves the artifact `unattended.sh --landed` accepts.
- **AC7** — When `grep -L 'GOV_GATE_CMD_TEST' .githooks/pre-push.test.sh .githooks/pre-push.runlog.test.sh tools/push-main.test.sh`
  runs, it prints nothing.
  Red when: a harness stubs the bar with an untracked script and never declares the escape, so it
  now tests only the refusal path.
- **AC8** — When the red-first control at `.githooks/pre-push.test.sh:355-357` is evaluated in a
  scratch clone that does not carry `05455c45`, it prints `SKIP — AC1 red-first control NOT RUN` and
  records no failure.
  Red when: the control still calls `bad` and reds every adopter over gov's history.
  fixture: a scratch clone without gov history; none exists in the tree today.
- **AC9** — When `git grep -n 'overrides the gate for testing\|or by overriding the gate command' -- AGENTS.md tools/unattended`
  runs, it returns nothing.
  Red when: the contract prose still says the knob is an unguarded override.
- **AC10** — When the ported harness disables the first-word, option and working-copy arms in a copy
  of `.githooks/pre-push`, the three rev-3 evasions of AC2 land, and the unmutated hook refuses them.
  Red when: the mutation anchor is missing or the evasions do not land, so the arms are unproven.

## 7. Gates

`pre-push self-test` · `pre-push run-log line` · `push-main self-test` · `branch-guard self-test` · `lexicon naming predicates` · `unattended kit gate` · `run-gates canary` · `run-gates gov canary` · `kit version markers`

New arm: `.githooks/pre-push.test.sh` · nc's arms 25-29b, run first against the a7c78ad2 hook to observe `GOV_GATE_CMD=true` landing · none
New arm: `tools/push-main.test.sh` · a landing under `GOV_GATE_CMD_TEST=1` with `LANDER_MARKER` declared, observed first to write the marker · none
New arm: a port of nc's `scripts/pre_push_bar_selftest.py` under `.githooks/`, whose mutation arms M1-M3 observe the evasions landing on every run · none

## 8. Open questions

- **F1 — record the full bar command in the run log, or only its class?** The class is enough to tell
  a stub from a gate and keeps the line under `RUNLOG_MAX_BYTES` (`.githooks/pre-push:95`).
  Recommendation: the class.
- **F2 — port nc's python harness as its own leg, or fold its cases into `.githooks/pre-push.test.sh`?**
  Its mutation step re-disables the three arms on every run, which the shell suite does not do.
  Recommendation: port it as a leg beside the hook, since the mutation is the only control that keeps
  observing the arms fail.
- **F3 — should the guard also refuse `GOV_GATE_CMD_TEST` when `.unattended.conf` declares a live
  run?** S4 already withholds the lander marker. Recommendation: no.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, measured against gov a7c78ad2, nc f69e2ffb and inCMS 1bc57da27,
  with the exploit reproduced in a scratch repo under the session scratchpad.

## 10. Reuse audit

The fix is nc's guard, `.githooks/pre-push:538-652` at nc, taken without change, and its harness
`scripts/pre_push_bar_selftest.py` at nc. The cross-check shape is gov's own
`GOV_DEFAULT_BRANCH` rule at `.githooks/pre-push:316-346` (`TOOL-aStandingWrit-4`): the environment
may refuse, never select. `tools/codebase-map/reuse_lookup.py` scans no `.sh` and ranked only
unrelated `*Refused` classes, so no existing seam fits beyond those two.

Recall terms used: `GOV_GATE_CMD pre-push bar stub tracked override boundary decision-line scoped full landing`.
