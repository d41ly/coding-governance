<!-- gov:kit unattended@1.32 -->
# The unattended-run kit

The binding contract is not here. It is `UNATTENDED-PROTOCOL.md` together with
`UNATTENDED-VERBS.md`, both installed under the project's memory root by this kit's adopter. This
file covers only what a reader cannot get from those: what the adopter installs, and which of those
artifacts are generated rather than copied.

## What the adopter installs

Run `adopt-unattended.sh` from this directory; `--check` verifies without writing and is a gate leg.

| artifact | how it is produced |
|---|---|
| the `unattended` Skill | **rendered** from `SKILL.template.md` + `.unattended.conf` |
| the protocol | copied from `PROTOCOL.template.md` |
| the verb carrier | copied from `VERBS.template.md` |
| the playbook template | copied from `PLAYBOOK-TEMPLATE.template.md` |
| the playbook **fixture** | **rendered** from `playbook.fixture.template.md` |
| the fixture **records** | **rendered** from `fixture-record-one.template.md` and its sibling |

Copied artifacts carry no placeholder, so rendering them would be a second spelling of `cat`. The
rendered ones do carry placeholders, and for them a render is the only correct install.

**One Skill placeholder is probed rather than read.** The Skill tells a run to execute the
memory-tree kit's bug-class checklist, so it names that kit's `gotchas.py` by path. An adopter may
install the memory-tree kit flat in its tool root, so the adopter takes the first TRACKED of the
nested and the flat spelling, and refuses when git tracks neither. Nothing is written in that case.
`MEMORY_TREE_DIR=<dir>` in the environment overrides the probe, and it must name a directory whose
`gotchas.py` is tracked. The review-harness kit's build harness carries the same command and fills
it the same way.

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

`gate-guard.js` is a `PreToolUse` hook on `Bash|PowerShell`, wired by
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

## Two things the validity gate does not treat as playbooks

`check-playbook.sh` grades every tracked markdown carrying a `step_selector` and a `toml` block,
minus two exclusions. `PLAYBOOK-TEMPLATE.md` is the canon, whose values are a specimen. And **any
`*.template.md`** is excluded for the same reason one level up: a template for a rendered artifact
necessarily carries unresolved braces, so grading one reds on a target that is not meant to resolve
until render time. That second exclusion was widened from the first the moment a second template
existed.

## The resume tick — registration is the owner's

`resume-tick.sh` is the one keepalive actor that does not share the session's process: an
OS-scheduled task that walks every worktree, asks the driver `--liveness` about every run whose
lease names a session, and on a verdict the protocol's section 5 names as acting kills the recorded
pid's tree, appends an attempt line under `<git-dir>/unattended/resume.<slug>.log` and launches
`claude -p --resume <session>` detached. It reads the lease from the INDEX, never the working copy
— an untracked run-state file is announced and skipped, and so is a tracked one whose working copy
differs from its index blob, because a file write must buy neither a skip-permissions session nor
a kill aimed by hand — stands off a lease another node took, kills only a pid whose recorded image
still holds it and whose holder started before the lease, and treats the pid it launched as in
flight until the tree moves or the stale bound passes, after which it is killed as hung and the
run is launched again. The kit never registers it — `schtasks /create` and
`crontab` are the owner's acts, once per node, under the login whose CLI is authenticated — and
until it is registered the tick is inert; the adopter's `--check` says which on an `INFO` line and
reds on neither answer.

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

## The sidecar

`<git-dir>/unattended/` is where the keepalive actors write, and it is the WORKTREE's git dir,
never the common dir, because a run lives in one worktree. Three kinds, one file per run each:
`stop.<slug>.log`, one JSON line per stop the stop-guard decided (unit 3); `stall.<slug>.log`, one
line per API-error end the stall-recorder saw (unit 4); `resume.<slug>.log`, one attempt line per
tick, with the launcher `resume.<slug>.<utc>.sh` and its `.out` beside it (unit 5). Append-only and
never tracked; read by `--liveness`, `--status`, `--landed` and the tick.

## Running the kit's own checks

```
adopt-unattended.sh --check      # the installed artifacts are in sync, the hook wired
check-unattended.sh              # the kit gate
check-playbook.sh                # playbook validity, including the fixture
check-pass-order.sh              # refuses a unit built before it was specced
check-brief-recorded.sh          # refuses a closed unit whose build commit records no brief
run-unattended-gates.sh --serial # the kit's self-tests, ON DEMAND ONLY; the mode is declared,
                                 # --pooled withholds every cost verdict, and bare REFUSES
run-unattended-gates.sh --pooled # the DoD for work touching this kit: parity against the calibrated evidence
```

The self-tests are deliberately **not** on the merge bar. A suite that stages breaks into a copy of
a checker has a job only when that checker's source changes, and none at all in an adopter's repo
that copy-installs this kit and never edits it. The legs whose subject is the *repository* stayed on
the bar, because those go stale with nobody editing the kit; `<prefix>/gate-legs.json` names which.
