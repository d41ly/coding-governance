<!-- gov:kit unattended@1.108 -->
# The unattended-run kit

The binding contract is not here. It is `UNATTENDED-PROTOCOL.md` together with
`UNATTENDED-VERBS.md`, both installed under the project's memory root by this kit's adopter. This
file covers only what a reader cannot get from those: what the adopter installs, and which of those
artifacts are generated rather than copied.

## What the adopter installs

Run `adopt-unattended.sh` from this directory; `--check` verifies without writing and is a gate leg.

| artifact | how it is produced |
|---|---|
| the `unattended` Skill | **rendered** from `SKILL.template.md` + `.unattended.conf`: a ROUTER, size-gated, into the verb carrier's `The paths, in order` section |
| the protocol | copied from `PROTOCOL.template.md` |
| the verb carrier | copied from `VERBS.template.md` |
| the playbook template | copied from `PLAYBOOK-TEMPLATE.template.md` |
| the playbook **fixture** | **rendered** from `playbook.fixture.template.md` |
| the fixture **records** | **rendered** from `fixture-record-one.template.md` and its sibling |

Copied artifacts carry no placeholder, so rendering them would be a second spelling of `cat`. The
rendered ones do carry placeholders, and for them a render is the only correct install.

**A kit declares the outputs its generators write, and check 23 reads the declarations.** Each is a
`[[generated]]` table in the kit's `kit.toml`, every key at column 0 as a double-quoted string:
`path` (tokens `{memory_root}`, `{map_root}` and `{kit}` only), `generator` (a file beside the
descriptor), `why`, and an optional `when = "<conf>:<KEY>=<value>"` that applies the row only when
that repo-root conf assigns exactly that value. govkit selfcheck refuses any other shape for those
four keys, because the shell reader would mangle or drop it. A row may also carry `write` and
`check`, argv arrays, and `stage`, an integer, all three or none, at column 0: the shell reader
ignores them, and the run-gates kit's `regen.py` reads them to regenerate the output or prove it
fresh before a bar (that kit's README, "Generated outputs"; TOOL-aPrimedIndex-1).
`GENERATED_INDEXES` in `.unattended.conf` only ADDS pairs to these (`TOOL-aWindowedPass-4`).

**One hook line is yours to wire, and no kit ships it.** Add
`bash <kit>/unattended.sh --check-commit "$1"` to your own `commit-msg` hook, ahead of anything that
exits early, and let exit 1 block the commit while any other exit lets it through. It refuses an
open pass's commit that stages a path outside its declaration while `--dispatch` can still widen it
(`TOOL-aWindowedPass-3`). This repo's `.githooks/commit-msg` is the reference; it is not shipped
because a hook file is copied whole and would overwrite yours. Its limits: a `--no-verify` commit
skips it, `Pass: none` is taken at its word, and check 23 grades both at the close.

**Why the verb entries are not in the protocol.** The move was a BYTE decision and is recorded as
one. That document had reached its cap EXACTLY, and a contract with no room left to state its next
rule has stopped being amendable — which is a failure mode of the contract, not of whoever wrote the
rule that would not fit. The sentence lived in the protocol itself until `TOOL-dDerivedDocket-3`
needed the bytes; it is the kit's own history rather than a rule any run follows, so it belongs
here, where nothing is capped.

**One Skill placeholder is probed rather than read.** The Skill tells a run to execute the
memory-tree kit's bug-class checklist, so it names that kit's `gotchas.py` by path. An adopter may
install the memory-tree kit flat in its tool root, so the adopter takes the first TRACKED of the
nested and the flat spelling, and refuses when git tracks neither. Nothing is written in that case.
`MEMORY_TREE_DIR=<dir>` in the environment overrides the probe, and it must name a directory whose
`gotchas.py` is tracked. The review-harness kit's build harness carries the same command and fills
it the same way.

**The Skill's harness citations resolve through the install receipt first** (`TOOL-dRenderedAnchor-6`).
Its `{{TOOL_ROOT}}<home>/<file>` citations name the review-harness kit's build harness and the child
it hands out, and govkit homes that kit by its entry id, so the tool root plus gov's home for them
names nothing in an adopter. The adopter derives them with `derive_kit_paths` over the Skill's
template, the receipt row first, and applies each held one whole before the plain `{{TOOL_ROOT}}`.
`--check` derives the same way, so it grades exactly what a render writes. A harness the
review-harness kit's hand render has not written yet is not held, so run this adopter after that
render; run before it, `--check` reads the Skill out of sync and names the re-render.
A held citation whose path is empty or holds a character outside `[A-Za-z0-9._/+@-]` is refused at
exit 2, in both modes and before anything is written, with one line naming the citation and its
path (`TOOL-dRenderedAnchor-7`): the Skill tells an agent to run it, where a space splits the
command. Fix the install receipt row that places it.

## The fixture is rendered, and this is the one thing to know about it

`playbook.fixture.md` is a **generated artifact**. Do not edit it — edit
`playbook.fixture.template.md` and re-run the adopter, or `--check` reds.

It became rendered in `TOOL-dRetiredFork-12`. Before that it shipped verbatim with this kit's own
directory spelled out five times in its `outputs`, `grain`, `records` and `legs`, so an adopter who
installed the kit anywhere other than the default prefix got a fixture describing a tree they did
not have: `check-playbook.sh` exited 1, reported both pieces as unrecorded, and the suite above it
could not follow a variable the fixture did not have.

**It carries exactly ONE token, `KIT_DIR`**, and deliberately not a second. All five spellings sat
under this kit's own directory, so one token covers every one of them. `TOOL_ROOT` is *not*
declared here and must not be: only the memory-tree kit's adopter computes that value, so declaring
it would ship an unresolved `{{TOOL_ROOT}}` brace to every adopter of this one.

**The fixture RECORDS are rendered with it.** Each is named for the piece it describes with `/`
written as `~`, so the prefix lives in their filenames as well as their bodies, and the adopter
derives both from the same value it renders the body with. This kit's own two copies are withheld
from every install, so nothing arrives under a foreign prefix and nothing is renamed over anything —
which is what the rename this replaced did to a target's own copy on every update. A record whose
body names a piece the tree does not hold is an orphan record to `check-playbook.sh` — coverage
nobody has.

**An unresolved token is a refusal, and no file is written.** Catching it at `--check` time alone
would still leave a rendered artifact on disk carrying a literal brace, and something reads that
file before anything runs `--check`.

## The act is refused at the tool call, not only forbidden

`gate-guard.js` is a `PreToolUse` hook on `Bash|PowerShell|AskUserQuestion`, wired by
`gate-guard.fragment.json` through the settings merger the hooks kit ships, and `--check` reports
it UNWIRED with the merge command as the remedy. While the run-state record on the CURRENT branch
is in any phase before `VERIFYING`, it exits 2 on a command that would run the flagged bar
(`GATE_FULL=` or `GATE_SELFTESTS=` with a non-empty value) or a self-test suite (a word ending
`run-selftests.sh`, `run-unattended-gates.sh` or `.test.sh` at command position, `bash -c` bodies
included). The read-only verbs — `--list`, `--check`, `--rank`, `--help`, `--render` — pass, the
plain bar passes, and a quoted mention of any shape is invisible. It keys the record to the branch
through the `run-branch:` fact `--preflight` writes on both anchors (protocol fact 13), falling
back to `branch-ref:` for a record written before that fact existed, and it fails open on every
unreadable input. Its suite, `gate-guard.test.sh`, is withheld like the others and runs at
`VERIFYING`; the predicate's coverage over real usage is the corpus probe in the build record of
`TOOL-aDeferredBar-3`.

The same hook refuses an unattended run's QUESTION (`TOOL-aOrientedCast-22`). An `AskUserQuestion`
call exits 2 when a run-state record leased to the payload's `session_id` — its `session:` fact,
read through `run-lease.js` — is in a phase outside `LANDED` and `ABORTED`, `HELD` included, and
the run is not finished. A lease is finished when the driver's `--liveness` reads TERMINAL
(`TOOL-aOrientedCast-24`), read through `stop-guard.js`'s own reader, so the two hooks ask one
question and get one answer; any other verdict denies and is named, and a liveness that cannot be
read leaves the recorded phase standing and says so. The deny names the run, its phase, liveness and
record, and `unattended.sh --park` with the question and its option labels quoted from the payload;
at `FINISHED-UNSTAMPED` it names `unattended.sh --landed` instead, the one act left. It keys on the
session, not the branch, so an owner's attended session in the same checkout holds no lease and may
still ask. It does not judge whether the question is one the protocol lets the run decide, and it
fires only where the harness routes the tool through `PreToolUse`, which the suite cannot see because
it feeds the hook its payload directly. The widened matcher reaches every session from its
next tool call, one already running included, because the harness re-reads the hooks settings on
each call (measured 2026-08-10, and recorded as a bug class in the memory tree).

`govkit update` and `govkit apply` wire every fragment an install lands, before the kit's own
`[check]` runs, through the target's `settings-merge.py` (a required kit since 1.33); a verify
rollback unwires what that run added. `GOVKIT_RERENDER=0` declines the step and says so.

## Two things the validity gate does not treat as playbooks

`check-playbook.sh` grades every tracked markdown carrying a `step_selector` and a `toml` block,
minus two exclusions. `PLAYBOOK-TEMPLATE.md` is the canon, whose values are a specimen. And **any
`*.template.md`** is excluded for the same reason one level up: a template for a rendered artifact
necessarily carries unresolved braces, so grading one reds on a target that is not meant to resolve
until render time. That second exclusion was widened from the first the moment a second template
existed.

## Two arguments moved out of the protocol's section 2

`TOOL-dDerivedDocket-22` needed protocol bytes for the derived terminal, and it funded them by moving
the REASONING behind two section 2 rules here, where nothing is capped. Both RULES stay in the
protocol: the roster at landing is frozen by `--landed` alone (by `--close` under `in-place`), and
facts 5-7 and 9-11 are evidence that is never read back as an input. What follows is why.

**Why the roster is frozen at landing.** While a run is LIVE the unit list derives from the build
README, which cannot go stale between reads. But a FINISHED record must still say which units the
run covered, and that README is mutable: a later build adding a unit would change a landed run's
answer retroactively. Freezing the ids keeps a terminal record a record.

**Why the evidence facts are never inputs.** A verb branching on the recorded anchor kind would take
a security decision from a value its subject wrote, the class this kit has been burned by three
times; the derivation is monotone instead. They exist so a party outside this process can re-derive
the pin without trusting a byte the run wrote, which is the only form of verification §9 concludes
actually binds.

**Why the local anchor is the exception.** Under `ANCHOR_SCOPE="local"` (`TOOL-aHomedAnchor-1`) the
recorded `base:` IS the input: the run started from local history with no push, so no observation
off this node exists to derive one from. The driver still refuses a base off HEAD's history and a
run that built nothing, and the leg admits such a BASE only when the conf at the remote's
default-branch tip declares `local`, a byte the run cannot write without landing.

## Why `brief-recorded` anchors on the build commit

`TOOL-dDerivedDocket-28` needed a protocol key-table row for `PROCMON_CMD` and funded it by moving
the ARGUMENT out of the `BRIEF_RECORDED_CUTOFF` row. The rule stays in the protocol: the anchor is
the build commit and NOT its first parent. Why, unlike its `PASS_ORDER_CUTOFF` sibling: `--brief`
STAGES its row, so the row lands in the same commit as the pass, and a first-parent anchor would red
the CONFORMING runs. The two terms are jointly satisfiable — a spec in an earlier commit, the brief
row alongside the code.

## The process ledger — why the driver's death defines an orphan

Every command the driver starts is recorded by identity in a per-slug ledger, and only a recorded
process whose driver is gone is reaped (`UNATTENDED-STOPS.md` §14 is the rule). Two narrower
definitions were rejected. "Any recorded process alive" kills the bar a background `--close` is
still waiting on. "Recorded under a different keepalive id" never reaps a same-session orphan, which
is the case that was observed: the harness killed the driver mid-bar and the session lived on.
Matching by command line was rejected outright, because five of the six same-named processes one run
found belonged to another repository. The driver never kills the pid itself either: a bare `kill -9`
on a tree's top left every descendant alive, and a native process ignores the MSYS signal, which is
why the declared reaper walks leaves first and verifies by a second census.

## Why `RECALL_CLI` and `MAP_CLI` are declarations

Both name a repo-relative path in `.unattended.conf` rather than carrying one in the driver, and the
argument for that form lives here rather than in the protocol's key table, which states what each key
IS. A kit literal in shipped bytes resolves to nothing in a tree installed at another prefix — the
carried-prefix ratchet reds on exactly that. `MAP_CLI` is a declaration for the same reason its sibling
is one. Until it existed the map log was a write-only surface: the unit that specced this reader shipped
the logger and not the reader, and its acceptance ledger recorded a gate accepting a declaration that was
nowhere in the product.

## The resume tick — registration is the owner's

`resume-tick.sh` is the one keepalive actor that does not share the session's process: an
OS-scheduled task that walks every worktree, asks the driver `--liveness` about every run whose
lease names a session, and on a verdict the protocol's section 5 names as acting appends an attempt
line under `<git-dir>/unattended/resume.<slug>.log` and launches `claude -p --resume <session>`
detached, with `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0` so the resumed session's background
Workflows outlive its turn ends. It kills only what it launched: a recorded pid that is alive with
no live launch of the tick's own is reported as `STALE OVER A LIVE PID`, and nothing is killed or
launched (`TOOL-aSparedHolder-1`). It reads the lease from the INDEX, never the working copy
— an untracked run-state file is announced and skipped, and so is a tracked one whose working copy
differs from its index blob, because a file write must buy neither a skip-permissions session nor
a kill aimed by hand — stands off a lease another node took, kills only a pid whose recorded image
still holds it and whose holder started before the lease, and treats the pid it launched as in
flight until the tree moves or the stale bound passes, after which it is killed as hung and the
run is launched again. The kit never registers it — `schtasks /create` and
`crontab` are the owner's acts, once per node, under the login whose CLI is authenticated — and
until it is registered the tick is inert; `--preflight` and the adopter's `--check` both say which,
through the library's one probe, `read_tick_registration`, with a `WARNING` line when it is not
registered or cannot be asked, and neither refuses on any answer.

Windows, from cmd or PowerShell (Git-Bash needs every `/` option doubled, `//create`, `//sc`, …):

```
schtasks /create /sc minute /mo 10 /tn gov-resume-tick /tr "\"<bash.exe>\" -lc \"<kit-dir>/resume-tick.sh --repo <root>\""
```

POSIX, one crontab line (the trailing comment names it the way the Windows task is named, and
`--check` finds either spelling in the listing):

```
*/10 * * * * <kit-dir>/resume-tick.sh --repo <root>  # gov-resume-tick
```

`<kit-dir>/resume-tick.sh --repo <root> --dry-run` prints the decision a tick would take for every
bound run and does nothing else — no kill, no launch, no attempt line, no login probe. The two knobs
it reads, `RESUME_ATTEMPTS` and `RESUME_TURNS`, are the root `.unattended.conf`'s and are announced
on stderr when absent.

The tick launches its session from the PATH CLI, which may be older than the one that launched the
run. So `--preflight` pins `cli-version` ONCE, read from `AI_AGENT` in its `claude-code_` shape
(`absent` when it carries none), beside the lease and never inside it; every resume that proceeds
compares the running session's version against it as integers and prints one line — the same, a
`WARNING` when this CLI is older, a `NOTE` when it is newer, or `UNKNOWN` naming the missing side.
It is a warning and never a refusal, and so is the tick line beside it.

A relaunch appends one `run-resumed` line, a launch that failed one `resume-failed` line, and a
live pid the tick spared one `stale-live-pid` line per tick, to the
health log under the git common dir that the orientation card counts; the driver appends
`claim-taken-over` when it takes over a stale claim (`TOOL-aGraftedHelix-8`), and
`claim-push-lock-broken` when it breaks a stale `claim-push.lock` under that lock's guard, or
`claim-push-guard-cleared` when it removes a guard a crashed writer left (`TOOL-aGraftedHelix-37`). The line format is the
header of the `health_log_sh` block in `lib-unattended.sh`.

## The sidecar

`<git-dir>/unattended/` is where the keepalive actors write, and it is the WORKTREE's git dir,
never the common dir, because a run lives in one worktree. Three kinds, one file per run each:
`stop.<slug>.log`, one JSON line per stop the stop-guard decided (unit 3); `stall.<slug>.log`, one
line per API-error end the stall-recorder saw (unit 4); `resume.<slug>.log`, one attempt line per
tick, with the launcher `resume.<slug>.<utc>.sh` and its `.out` beside it (unit 5). Append-only and
never tracked; read by `--liveness`, `--status`, `--landed` and the tick.

## The bar `--close` runs

`gates-green` runs `GATE_CMD` under a run id the driver pins, attributes a red against the tip the
remote advertises, and hands the bar the inherited-red policy it read at that tip. It then reads that
bar's own run record: an inherited-only red is met under `land`, the kit default, at any age; it
parks as the `inherited-red` hold under a declared `park`; and it files an ask for each inherited leg
once `ASKS_CMD` is declared, at SEV BLOCKER for a leg older than the age bound
(`TOOL-dUnstuckLanding-16`). After the bar, on every return code, it also reads the daily scheduled
held job of the workflow `HELD_CI_WORKFLOW` names and files one HIGH ask per red held suite the same
way, reusing an OPEN one in any build. The contract is `UNATTENDED-STOPS.md`. One residual moved here from the protocol's §3 when
that arm grew its decision table (`TOOL-dDerivedDocket-24`): two runs CLOSING together in one clone
contend on the bar's turnstile. Where the project declares a profile, the queue wait has its own term
in the bar's backstop and the second run waits it out; where it does not, the wait is charged
against `GATE_BOUND`, so the second can fail `gates-green` for contention.

After a clean `--close` or `--abort`, the driver writes that call's END line itself and then renders
the run record through the runlog kit, re-renders the index and stages both (`TOOL-aMendedFleet-63`);
under `in-place` the close commits them. A miss is one line, and no exit moves.

The close is decided at `VERIFYING`, so the move into that phase, and a resume that finds the record
there, prints what the close should carry, report-only: the open asks whose pointer names a file the
range from the pinned base to HEAD touched, read through `ASKS_CMD --json --path <paths> --limit 0`,
the asks companion's fourth call shape (`TOOL-aMendedFleet-66`), and then whether that range owes the
flagged bar, and then the stale-dossier list: the dossiers that range touched and did not refresh,
read through `map_diff.py <base>..HEAD --stale-dossiers --json` from the directory of the declared
`MAP_CLI`'s kit (`TOOL-aMendedFleet-83`). Each list is a disposition worklist; none refuses and no
exit moves.

## The bar's bound — wall, queue and margin

`TOOL-dDerivedDocket-27`, under owner ruling D12-i7. The unattended bar has ONE declared number,
`GATE_WALL`, the runner's whole-run wall, and `GATE_PROFILE_CMD` is the command that prints the
runner's resolved profile. `--preflight` runs that command under `GATE_BOUND` and pins the bar's
bound as the `gate-backstop` fact: the wall, plus the turnstile's queue bound, plus a margin that
is a source constant of the driver. The runner arms its wall only after the queue, so a bound that
charged the queue to `GATE_BOUND` killed a close for contention with its bar never started.

- **Blank `GATE_PROFILE_CMD` is where every adopter starts.** The bar has no backstop and stays at
  `GATE_BOUND`, announced at `--preflight` and at every `gates-green`. A profile that answers without
  a usable `wall` or `queue` falls back the same way and names the key it lacked. Probing
  `$GATE_CMD --print-profile` instead would guess that the declared gate is this repository's
  runner, and a gate that ignores its arguments would run a whole bar at preflight.
- **Blank `GATE_WALL` leaves the profile's own wall in force**, and the driver's NOTE says so. A value
  that is not a positive integer refuses at conf load, on `GATE_BOUND`'s terms. The driver hands a
  declared wall to `$GATE_CMD` and to no other command, so the push-boundary bar keeps the profile's.
- **A wall below the largest leg ceiling is refused**, by `--preflight` and by the kit gate, naming
  both numbers: it fires on a healthy bar that dispatches that leg. Where the profile cannot answer,
  the kit gate announces on its report channel that it cannot compare, and does not red.

`gates-green` then reads how the bar ended. An exit 3, TREE MOVED, runs it once more; an exit 4,
HOST, prints a `host-degraded` hold released by `probe host`. A kill at the backstop before the bar
printed `gate queue: acquired` prints a `host-degraded` hold released by `probe gate`. A kill after
that line is the bar never returning, which no hold fits.

## Two declared ceilings — the wiring check and preflight

`TOOL-aBriskPreflight-7`, under the owner's ruling "Name it, refuse only wiring": cost is a verdict,
but a refused preflight costs a whole re-run, so only the wiring check is killed. Both ceilings are
file constants of the driver, `WIRING_CEILING` and `PREFLIGHT_CEILING` in seconds, beside
`CEILING_SPAWN_MS`, the per-spawn cost both were derived to tolerate.

- **`WIRING_CEILING` kills.** The wiring child runs under the smaller of it and `GATE_BOUND`. When
  the ceiling is the smaller and fires, check 4 refuses naming it, the time the child was killed
  after, and one spawn's cost measured at the kill beside `CEILING_SPAWN_MS`, and prints whatever
  the check said before it died, indented. When `GATE_BOUND` is the smaller or equal, its own
  refusal fires unchanged; `GATE_BOUND` still bounds the wiring check, and the ceiling is a second,
  smaller kill beside it.
- **`PREFLIGHT_CEILING` names.** A `--preflight` whose wall from the driver's first statement passes
  it prints `unattended: preflight over its ceiling` with the wall, the ceiling and the same spawn
  figure, after the verb's own verdict, on every return path. It kills nothing, refuses nothing,
  leaves the exit status and the run-state file as the checks decided them, and under the ceiling
  prints nothing.
- **The spawn figure says load or regression.** One spawn far above `CEILING_SPAWN_MS` reads as this
  host's load; one near it reads as the check's own cost. It is measured only on a breach, five
  spawns of the external `true`, so a run that does not breach pays nothing.
- **The values are derived, never typed.** Per subject, from after-arm rows: the slowest untraced
  wall `W`, plus every traced exec `E` and fork `K` re-priced from that run's own per-spawn `S_m` and
  per-fork `K_m` to the worst on record, `S_w` (at least 2.5 s) and `K_w` (at least 0.91 s), plus `U`,
  each timed wait's bound less its traced window. `W`, `S_m` and `K_m` come from after-arm rows;
  `S_w` and `K_w` from every host row on record, any arm and any exit status
  (`TOOL-aBriskPreflight-11`). The sum rounds up to a multiple of 30 s:
  `W + E*max(0, S_w - S_m) + K*max(0, K_w - K_m) + U`. `CEILING_SPAWN_MS` is `S_w`. Only
  `WIRING_CEILING` must sit below `GATE_BOUND`, since it races that bound on one child;
  `PREFLIGHT_CEILING` kills nothing and may sit above it. The rows and the instrument that prints
  the three constant lines sit in that unit's build record, and a changed value is a re-derivation
  there.
- **Why no conf key.** A key owes a row in the protocol's key table, a governance carrier, and an
  environment read is a new public surface; a ceiling raisable from either leaves no diff behind.
  An adopter whose wiring check legitimately runs past `WIRING_CEILING` has no override until one is
  added there. On a node with no working `timeout -k` the ceiling is inert, and a second NOTE says so
  beside the one naming `GATE_BOUND`.

## Two restatements moved out of the protocol's key table

`TOOL-dDerivedDocket-27` widened the key table's `GATE_CMD` cell to carry the two keys above and
funded the bytes by moving one RESTATEMENT and one ARGUMENT here. Both RULES stay in the table:
`UNIT_STALL_BOUND` and `TASK_STALL_BOUND` are OPTIONAL on `GATE_BOUND`'s terms, and `REVIEW_ROUNDS` also refuses a value at
or above the runaway ceiling.

**What `GATE_BOUND`'s terms are, for `UNIT_STALL_BOUND`.** The row keeps the pointer, and the sibling
`GATE_BOUND` row states the terms in full. Spelled out, on one line so a reader can grep for the
passage the row gave up:
absent takes the kit default and says so on stderr; non-numeric or zero is a refusal.

**Why `REVIEW_ROUNDS` refuses a value at or above the runaway ceiling.** The row keeps the refusal;
this is its reason:
because the ceiling would fire first and the declared bound could never be reached.

## The overlap probe at `--preflight`

`--preflight` announces every unmerged remote ref that touches what this run touches, beside its
count of concurrent run-state files. That count sees only the records this clone tracks, and a
slug-keyed claim sees one slug; neither sees two builds on one subject, which would otherwise be
learned when the second one merges. The summary line always prints, opening
`unattended: overlap probe — `, so a clean result reads differently from a probe that did not run.

- **What it reads.** Every ref under the single remote's `refs/remotes/<remote>/` reachable from
  neither the observed default-branch tip nor `HEAD`, the remote's `HEAD` symref skipped. For each,
  the paths its diff from the observed tip changes, and the backticked paths under
  `### Files touched` of every spec that diff changes whose status is not `CLOSED` or `WONTDO`. It
  joins them with this run's own diff from that tip and its build's live specs: two paths are shared
  when equal or when one is a directory holding the other. Each shared path is tagged `diff` or
  `declared`, because a declared path is a spec's estimate rather than an edit.
- **It never fetches.** It reads the refs as of this clone's last fetch, and its summary line says so.
- **What it excludes.** A ref whose tip is older than the driver's `OVERLAP_AGE_DAYS`, counted on the summary line as aged
  out. A path under a `SHARED_RECORDS` entry or a `GENERATED_INDEXES` index: those reconcile
  additively or re-render, and are never contested. A diff path whose every added and removed line
  carries a kit version marker, unless a spec on the ref also declares it.
- **It refuses nothing.** A remote-tracking ref is a local write any process can move, so the
  overlap probe can add or remove an announcement and never a refusal; preflight's outcome is the
  same with or without it. With no observed tip it prints `overlap probe UNAVAILABLE` and the reason,
  and a ref whose diff cannot be read is counted as unreadable, never as clean.
- **An attended session reads it too.** `unattended.sh --overlaps` runs the same probe with no slug
  and exits 0 on every path. Its anchor is the local default-branch tracking ref,
  `refs/remotes/<remote>/HEAD`, never the remote's advertisement, so it reads no network; its own
  declared paths are the live specs its diff from that tip changed. Other than one remote, or that
  symref unset, prints `overlap probe UNAVAILABLE`. The session-kickoff kit's orientation card calls
  it once per session start, bounded, and prints its answer as the `overlaps —` cell
  (`KICK-aMendedFleet-2`).

## Running the kit's own checks

```
adopt-unattended.sh --check      # the installed artifacts are in sync, the hook wired
check-unattended.sh              # the kit gate
check-playbook.sh                # playbook validity, including the fixture
check-pass-order.sh              # refuses a unit built before it was specced
check-brief-recorded.sh          # refuses a closed unit whose build commit records no brief
                                 # both grade only the run's commits past the remote's tip, else all
run-unattended-gates.sh --serial # the kit's self-tests, ON DEMAND ONLY; the mode is declared,
                                 # --pooled withholds every cost verdict, and bare REFUSES
run-unattended-gates.sh --pooled # the DoD for work touching this kit: parity against the calibrated evidence
```

The self-tests are deliberately **not** on the merge bar. A suite that stages breaks into a copy of
a checker has a job only when that checker's source changes, and none at all in an adopter's repo
that copy-installs this kit and never edits it. So those suites left both the merge bar's leg
manifest and this kit's own `kit.toml`, and adopters stop receiving them too. The legs whose
subject is the *repository* stayed on the bar, because those go stale with nobody editing the kit;
`<prefix>/gate-legs.json` names which.
